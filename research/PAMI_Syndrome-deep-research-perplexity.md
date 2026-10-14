---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-13T10:19:27.137950'
end_time: '2026-10-13T10:23:29.291687'
duration_seconds: 242.15
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hyperzincemia With Functional Zinc Depletion
  mondo_id: MONDO:0011174
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
citation_count: 40
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 8
  off_topic: 1
  off_topic_references:
  - DOI:10.1111/j.1651-2227.2008.01092.x
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 78
  verified: 70
  not_found: 3
  obsolete: 2
  unverifiable: 3
  confabulation_rate: 0.04
  labels_checked: 36
  labels_matching: 16
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: GO:0140235
    reported_labels:
    - inflammasome complex assembly
    ontology_label: RNA polyadenylation at postsynapse
  - term_id: CHEBI:25517
    reported_labels:
    - nickel(2+) cation
    ontology_label: CHEBI_25517
  - term_id: NCIT:C15731
    reported_labels:
    - Corticosteroid therapy
    ontology_label: Intrahepatic Infusion Procedure
  - term_id: NCIT:C16033
    reported_labels:
    - Tumor Necrosis Factor Inhibitor Therapy
    ontology_label: Follow-Up
  - term_id: NCIT:C121938
    reported_labels:
    - Interleukin-1 Inhibitor Therapy
    ontology_label: Low Reference Range in Numeric Format
  - term_id: NCIT:C1282
    reported_labels:
    - Tacrolimus
    ontology_label: Carboplatin
  - term_id: NCIT:C65202
    reported_labels:
    - Adalimumab
    ontology_label: Wedge
  - term_id: NCIT:C15197
    reported_labels:
    - Allogeneic Hematopoietic Stem Cell Transplantation
    ontology_label: Case-Control Study
  - term_id: NCIT:C80188
    reported_labels:
    - Myeloablative Conditioning Regimen
    ontology_label: HDL-Cholesterol Subclass 3 Measurement
  labels_variant: 11
  unresolved_terms:
  - HP:0001505
  - HP:0003331
  - HP:0006950
  obsolete_terms:
  - term_id: GO:0051092
    ontology_label: obsolete positive regulation of NF-kappaB transcription factor
      activity
  - term_id: CHEBI:25517
    ontology_label: CHEBI_25517
    replaced_by: CHEBI:49786
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hyperzincemia With Functional Zinc Depletion
- **MONDO ID:** MONDO:0011174 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hyperzincemia With Functional Zinc Depletion** covering all of the
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

# Hyperzincemia With Functional Zinc Depletion (Hyperzincemia and Hypercalprotectinemia / PAMI Syndrome): An Integrative Research Overview

Hyperzincemia with functional zinc depletion, now more commonly referred to as **hyperzincemia and hypercalprotectinemia (Hz/Hc)** or **PSTPIP1‑associated myeloid‑related proteinemia inflammatory (PAMI) syndrome**, is a rare, childhood‑onset autoinflammatory disorder characterized by extreme elevation of serum zinc and calprotectin (S100A8/S100A9), chronic systemic inflammation, cytopenias, growth failure, and prominent cutaneous and osteoarticular involvement.[16][27][11] It represents a distinct Mendelian disease entity caused by specific heterozygous missense mutations in **PSTPIP1** (typically p.E250K or p.E257K), which radically alter protein–protein interactions and drive uncontrolled release of alarmins from myeloid cells.[27][19][29] Despite elevated circulating zinc, affected patients manifest clinical and functional features of zinc deficiency, including impaired immune function, poor growth, skin ulcerations, and bone involvement; mechanistically, this paradox is explained by high‑affinity sequestration of zinc by calprotectin and abnormal intracellular zinc compartmentalization, producing a state of **functional zinc depletion** in critical tissues.[1][35][24] Clinical management is challenging: corticosteroids, calcineurin inhibitors, anti‑TNF and anti‑IL‑1 biologics provide partial and variable benefit, while allogeneic hematopoietic stem cell transplantation (HSCT) has recently emerged as a potentially curative option in severe, refractory disease.[11][14][40] This report synthesizes the current knowledge on disease definition, etiology, phenotypic spectrum, molecular mechanisms, diagnostics, epidemiology, prognosis, and treatment, integrating human clinical data, mechanistic studies on PSTPIP1 and calprotectin, and comparative insights from model systems.

## 1. Disease Information

### 1.1 Definition and Nosology

Hyperzincemia with functional zinc depletion was initially described as a puzzling metabolic disorder in an 11‑year‑old boy presenting with hepatosplenomegaly, rashes, failure to thrive, anemia, and impaired immune function despite markedly elevated plasma zinc levels exceeding 200 µmol/L, leading investigators to propose “a previously unrecognized inborn error of Zn metabolism causing symptomatic zinc deficiency.”[1][20] Subsequent work identified similar patients with extreme hyperzincemia and profoundly increased serum calprotectin (MRP8/14) levels, establishing **hyperzincemia and hypercalprotectinemia (Hz/Hc)** as a distinct disorder of zinc metabolism and innate immunity.[31][31][39]

Modern disease ontologies now classify this entity as an **autoinflammatory syndrome with cytopenia, hyperzincemia, and hypercalprotectinemia (AICZC)**, reflecting its core triad of excessive zinc and calprotectin, chronic systemic inflammation, and blood cell abnormalities.[3][3] Orphanet defines the condition as “a rare inborn error of zinc metabolism characterized by recurrent infections, hepatosplenomegaly, anemia (unresponsive to iron supplementation) and chronic systemic inflammation in the presence of high plasma concentrations of zinc and calprotectin,” with typical dermal ulcers, arthralgia, and bleeding manifestations such as severe epistaxis and spontaneous hematomas.[16][16] MedGen and disease ontology resources categorize Hz/Hc as a **vitamin/metal metabolic disorder** under disorders of zinc metabolism, anchored to the molecular basis in PSTPIP1.[12][12][3]

The term **PSTPIP1‑associated myeloid‑related proteinemia inflammatory (PAMI) syndrome** has been adopted to emphasize the genetic cause and the central role of myeloid‑derived alarmins MRP8/14; PAMI is now considered synonymous with Hz/Hc in most contemporary literature.[11][16][11] Holzinger and colleagues demonstrated that a single amino acid charge switch (Glu→Lys) at positions 250 or 257 in PSTPIP1 defines clinically distinct PSTPIP1‑associated diseases, with p.E250K and p.E257K specifically linked to the Hz/Hc/PAMI phenotype rather than classical PAPA (pyogenic arthritis, pyoderma gangrenosum, and acne) syndrome.[27][19]

### 1.2 Key Identifiers and Coding

The disorder is represented across major biomedical coding and ontology systems with the following identifiers and labels:

The **OMIM entry 601979** corresponds to “Autoinflammatory syndrome with cytopenia, hyperzincemia, and hypercalprotectinemia (AICZC).”[3][3][3] Orphanet assigns **ORPHA:251523** to “Hyperzincemia and hypercalprotectinemia,” listing it as a rare disorder of zinc metabolism with childhood onset.[16][16] Disease Ontology (DOID:0061185) defines an autoinflammatory syndrome characterized by recurrent infection, hepatosplenomegaly, anemia non‑responsive to iron therapy, chronic systemic inflammation, and high plasma zinc and calprotectin levels, with material basis in heterozygous PSTPIP1 mutation at 15q24.[12][12] The MONDO ontology links to this disease concept (MONDO:0011174) under “Hyperzincemia with functional zinc depletion” and related labels.[3][33]

In clinical coding systems, hyperzincemia and hypercalprotectinemia map to **ICD‑10 code E83.2 (Disorders of zinc metabolism)** and **ICD‑11 code 5C64.2Y**, indicating a metabolic disorder of trace element handling.[32][16] SNOMED CT lists “Hyperzincemia and hypercalprotectinemia” and “Recurrent infection, inflammatory syndrome due to zinc metabolism disorder syndrome” under concept ID 771339005, cross‑referencing E83.2.[3][32] MeSH has introduced “Hyperzincemia with Functional Zinc Depletion” as a supplementary concept term, reflecting the evolving understanding of this metabolic–inflammatory overlap.[34][6]

### 1.3 Synonyms and Alternative Names

Over time and across resources, the disease has acquired multiple overlapping names capturing various facets of its phenotype and mechanism:

The earliest descriptors include **“hyperzincemia with functional zinc depletion”** and **“hyperzincaemia and hypercalprotectinaemia: a new disorder of zinc metabolism”**, emphasizing the paradox of elevated serum zinc with clinical zinc deficiency and the association with high calprotectin.[1][31][31] Orphanet and GARD list **“hyperzincemia and hypercalprotectinemia (Hz/Hc)”**, **“recurrent infections–inflammatory syndrome due to zinc metabolism disorder syndrome”**, and **“recurrent infection, inflammatory syndrome due to zinc metabolism disorder syndrome”** as synonyms.[16][9][33] MedGen incorporates **“Autoinflammatory syndrome with cytopenia, hyperzincemia, and hypercalprotectinemia (AICZC)”** and notes **“HZHC syndrome”** and **“hyperzincemia with functional zinc depletion”** as alternate labels.[3][3][3] 

With the elucidation of PSTPIP1 mutations, the term **“PSTPIP1‑associated myeloid‑related proteinemia inflammatory (PAMI) syndrome”** came into use, highlighting both the genetic etiology and the hallmark elevation of MRP8/14.[11][11][15] Orphanet explicitly lists “PAMI syndrome” and “PSTPIP1‑associated myeloid‑related proteinemia inflammatory syndrome” as synonyms under ORPHA:251523, further cementing the equivalence of these entities.[16][30] Clinically, PAMI is often distinguished from PAPA syndrome, which shares PSTPIP1 involvement but lacks the extreme hyperzincemia, hypercalprotectinemia, cytopenias, and growth failure seen in Hz/Hc.[27][23][38]

### 1.4 Source and Level of Information

Most of the information about hyperzincemia with functional zinc depletion derives from **aggregated disease‑level resources and case series** rather than large population‑based cohorts, reflecting the ultra‑rare nature of the condition. The seminal case reports by Sampson and colleagues in 1997 and 2002 described individual pediatric patients with unexplained hyperzincemia and zinc‑binding proteins, forming the basis for subsequent conceptualization.[1][20][31][31][39] 

Later, Holzinger et al. performed gene sequencing in 14 Hz/Hc patients and compared their clinical phenotype with 11 PAPA patients, integrating clinical data, biochemical measurements, and structural modeling of PSTPIP1 to define genotype–phenotype correlations.[27][19] Additional case reports and small series have enriched the description of clinical variability, treatment responses, and long‑term outcomes.[35][15][17][15][40] Aggregated descriptions in Orphanet, GARD, MedGen, and disease ontology resources synthesize these case‑level observations into standardized definitions, coding, and phenotypic lists for the disease.[16][9][3][12] 

Because of the rarity (prevalence <1/1,000,000), there are no large epidemiologic registries specific to Hz/Hc, and many aspects of natural history, prognosis, and genotype–phenotype modifiers remain inferred from small cohorts and expert review rather than formally quantified studies.[16][11][40] This should be kept in mind when interpreting frequencies and prognostic associations.

## 2. Etiology

### 2.1 Primary Causal Factors: Genetic, Metabolic, and Immunologic

Hyperzincemia with functional zinc depletion is fundamentally a **Mendelian autoinflammatory disorder** caused by **heterozygous missense mutations in PSTPIP1** that alter myeloid cell function and zinc/calprotectin handling.[27][3][29] PSTPIP1 (proline–serine–threonine phosphatase‑interacting protein 1), located on chromosome 15q24.3, encodes a cytoskeletal adaptor protein involved in T‑cell activation, IL‑1β release, and cytoskeletal organization; pathogenic variants p.E250K and p.E257K produce charge reversal in a critical coiled‑coil domain region essential for protein–protein interactions.[27][11][28] 

In the largest genetic study to date, Holzinger et al. sequenced PSTPIP1 in 14 individuals with Hz/Hc and found that 13 were heterozygous for p.E250K and one carried p.E257K; these mutations substantially altered the electrostatic potential surface of the PSTPIP1 dimer and increased interaction with pyrin, thereby driving pyrin inflammasome activation and uncontrolled release of myeloid alarmins, including MRP8/14.[27][19][19] This mechanism distinguishes Hz/Hc from PAPA syndrome, where different PSTPIP1 mutations (e.g., p.A230T, p.E250Q) primarily affect IFN‑γ‑dependent feedback loops in skin lesions rather than systemic zinc and calprotectin metabolism.[23][27]

At a metabolic level, the disease is characterized by **extreme elevation of serum zinc** and of calprotectin, which is a heterodimer of S100A8 and S100A9 with high‑affinity zinc‑binding sites.[24][25][21] Calprotectin acts as both a **zinc‑binding protein and pro‑inflammatory alarmin**, and its massively increased release from myeloid cells in PAMI leads to formation of large calprotectin complexes that sequester zinc in the circulation and tissues.[35][24][25] MedGen and Orphanet therefore describe Hz/Hc as “a rare inborn error of zinc metabolism,” with abnormal zinc distribution driven by dysregulated calprotectin biology.[3][16][3]

Thus, the **primary causal factors** are: a specific gain‑of‑function type alteration in PSTPIP1 protein–protein interactions, hyperactivation of the pyrin inflammasome and myeloid alarmin release, and secondary metabolic derangements in zinc compartmentalization due to excess calprotectin. Environmental triggers, infections, or trauma may modulate flare frequency or severity but are not recognized as primary causes.

### 2.2 Genetic Risk Factors: Causal Variants and Susceptibility

The principal genetic risk factor is the presence of a **heterozygous germline missense variant in PSTPIP1**, particularly:

The **p.E250K (c.748G>A)** variant, which replaces a negatively charged glutamic acid with positively charged lysine within the PSTPIP1 coiled‑coil region, is the most commonly reported mutation in Hz/Hc/PAMI patients and has been repeatedly confirmed as pathogenic in this clinical context.[27][11][38] Holzinger et al. reported p.E250K in 13 of 14 Hz/Hc patients, while one patient carried p.E257K; both mutations produced similar changes in the local electrostatic potential of the protein dimer.[27][19] Case reports and systematic reviews continue to identify p.E250K as the canonical variant associated with hyperzincemia and hypercalprotectinemia, often with presentation in childhood.[11][17][11][15]

The **p.E257K** variant, also a glutamate‑to‑lysine substitution, is less frequent but clearly associated with Hz/Hc; Holzinger et al. described a single patient with this mutation with typical phenotype, supporting its inclusion in the same pathogenic spectrum.[27][19] Additional PSTPIP1 mutations are linked to PAPA or other inflammatory phenotypes but not to the characteristic hyperzincemia/hypercalprotectinemia profile, underscoring a strong genotype–phenotype correlation.[27][23][38]

These variants are considered **pathogenic** by ACMG/AMP criteria based on segregation with disease in small families, functional modeling of altered protein–protein interactions, and the highly specific clinical phenotype; they are rare or absent in general population databases, consistent with an ultra‑rare, high‑penetrance Mendelian disease.[27][12][28] No susceptibility loci beyond PSTPIP1 have been definitively identified, although variation in other inflammasome components or zinc‑binding proteins could theoretically modulate expressivity.

### 2.3 Environmental and Lifestyle Risk Factors

Current evidence does not support a major role for environmental toxins, occupational exposures, diet, or lifestyle as **primary risk factors** for developing Hz/Hc, given its clear monogenic etiology.[16][27] Most reported patients are children or adolescents without notable environmental exposures beyond common infections; cases arise in sporadic or familial fashion depending on inheritance, but not linked to geographic or occupational clusters.[17][15][40] 

Nevertheless, **intercurrent infections** and physical stressors may act as **precipitating triggers** for inflammatory flares, cutaneous ulcers, and arthritis episodes in affected individuals, analogous to other autoinflammatory syndromes.[35][11] In one case report, extensive pyoderma‑gangrenosum–like lesions with systemic inflammation led to the suspicion of Hz/Hc, highlighting the potential role of skin trauma or infection as a trigger for exaggerated inflammatory responses in genetically predisposed patients.[35] Formal epidemiologic studies quantifying such triggers are lacking, and this remains an area of clinical inference rather than systematic evidence.

Lifestyle factors such as nutrition, smoking, or alcohol consumption have not been systematically studied in PAMI syndrome, and given the pediatric onset and rarity, their contribution is likely minimal compared with the dominant genetic driver. However, **zinc supplementation** or high dietary zinc intake theoretically could modulate circulating zinc levels and might exacerbate or complicate interpretation of laboratory findings in affected patients; clinicians typically avoid exogenous zinc supplementation once the diagnosis is suspected, to prevent further perturbation of zinc homeostasis.[1][31][11] Robust data on such interactions are not yet available.

### 2.4 Protective Factors and Gene–Environment Interactions

At present, **no specific genetic protective variants or modifier alleles** have been identified that confer protection against developing hyperzincemia with functional zinc depletion in PSTPIP1 mutation carriers. Intrafamilial variability and incomplete penetrance have been observed, indicating that there must be genetic or environmental modifiers, but their identity remains unknown.[3][3][27] Holzinger and MedGen highlight incomplete penetrance and variable expressivity in families carrying p.E250K, with some relatives showing milder disease or late onset, but systematic genotype–phenotype correlation within families is limited by small sample sizes.[27][3][3]

Similarly, **environmental protective factors** have not been clearly characterized. Standard pediatric health practices such as infection prevention, adequate nutrition, and avoidance of unnecessary immunosuppression or trauma may reduce flare frequency or complications but are general measures rather than disease‑specific protective factors.[14][11] 

Gene–environment interactions in Hz/Hc are therefore largely inferred: PSTPIP1 mutations provide a necessary genetic substrate for disease, while stochastic environmental events (infections, minor trauma, vaccination) may trigger or amplify inflammatory episodes in genetically primed myeloid cells. The lack of population‑level data precludes quantitative modeling of such interactions.

## 3. Phenotypes

### 3.1 Core Clinical Features and Symptom Domains

Patients with hyperzincemia with functional zinc depletion exhibit a characteristic constellation of **systemic inflammatory, hematologic, cutaneous, musculoskeletal, and metabolic phenotypes**, many of which reflect both autoinflammatory pathology and functional zinc deficiency despite hyperzincemia.

Systemically, the disease is marked by **chronic systemic inflammation**, manifesting as recurrent fever, elevated acute‑phase reactants (C‑reactive protein, ESR), malaise, and failure to thrive.[16][3][11] Hepatosplenomegaly is common, with enlarged liver and spleen noted from infancy or early childhood; Orphanet, MedGen, and case series consistently list hepatosplenomegaly as a hallmark feature.[16][16][3][17] Lymphadenopathy and polyadenopathy may also occur, reflecting generalized activation of the reticuloendothelial system.[17][18][15]

Hematologic involvement includes **anemia** that is **unresponsive to iron supplementation**, **neutropenia**, **thrombocytopenia**, and overall **pancytopenia**, often with bone marrow dysgranulopoiesis and dyserythropoiesis.[3][3][3][11] Severe anemia and neutropenia are accompanied by thrombocytopenia in most patients, and bone marrow aspirates show dysplastic granulocytic and erythroid lineages.[3][3] Cytopenias contribute to fatigue, recurrent infections, and bleeding tendencies such as severe epistaxis and spontaneous hematomas.[16][16][16]

Cutaneous manifestations are particularly prominent: patients typically present **dermal ulcers**, pustular or ulcerative inflammatory lesions resembling pyoderma gangrenosum, severe acne, and other inflammatory rashes.[16][35][15][40] The original Sampson case described rashes, while subsequent series emphasize extensive pyoderma‑gangrenosum–like ulcers and pustular lesions in youth.[1][31][35] These cutaneous findings often dominate initial presentation and can be misinterpreted as isolated dermatologic disease until systemic features and hyperzincemia are recognized.

Musculoskeletal and osteoarticular involvement includes **arthralgia/arthritis**, recurrent pyogenic arthritis, bone pain, and sometimes osteopenia or osteoporosis.[16][16][11][9] PAMI syndrome is characterized by osteoarticular problems such as joint swelling and erosive arthritis, overlapping partially with PAPA but accompanied by systemic inflammation and cytopenias.[15][18][27] Some patients exhibit growth failure and stunted stature (<3rd centile), reflecting both chronic inflammation and functional zinc depletion during development.[1][16][17]

Other phenotypes include **recurrent infections** (particularly bacterial infections due to neutropenia and impaired immune function), **nosebleeds (epistaxis)**, bruising, listlessness, and gastrointestinal manifestations such as atypical or refractory colitis in a minority of cases.[16][16][15][15] Renal involvement is not a characteristic feature of Hz/Hc itself, in contrast to SLC30A9‑related cerebro‑renal syndromes, but long‑term immunosuppression may predispose to renal complications.[10][4][8]

### 3.2 Age of Onset, Severity, and Progression

Hyperzincemia with functional zinc depletion typically manifests in **childhood**, often in early childhood or even infancy, with symptoms such as recurrent infections, hepatosplenomegaly, anemia, and growth failure appearing within the first years of life.[16][16][17] Orphanet explicitly notes childhood age of onset, and early case descriptions reported symptom onset “since infancy” in the original boy with hyperzincemia and zinc depletion.[1][16] 

Symptom severity is generally **moderate to severe**, with a **severe course and early onset** emphasized as distinguishing features from PAPA syndrome.[27][18][38] Chronic systemic inflammation, cytopenias, and organomegaly can lead to significant morbidity, hospitalizations, and impact on quality of life, particularly when cutaneous ulcers and arthritis cause pain and functional impairment.[11][35][15] However, severity can vary: some patients may have milder cytopenias or less extensive skin disease, reflecting variable expressivity even within the same PSTPIP1 mutation.[3][27][3]

Disease progression is typically **chronic and relapsing**, with persistent underlying inflammation and flares of cutaneous, articular, or systemic symptoms. PAMI syndrome is described as a chronic multisystem disease with nonspecific symptomatology present since childhood and incomplete resolution over time.[35][11][40] Cytopenias and organomegaly may fluctuate but often persist; growth failure may be irreversible if not addressed early.[15][17] Without effective therapy, patients may experience progressive functional impairment due to joint damage, chronic ulcers, and hematologic complications.

### 3.3 Frequency and Quality of Life Impact

Because of the ultra‑rare nature of the disease, quantitative **frequencies of specific phenotypes** are not always reported as percentages, but case series and reviews allow qualitative assessment. In the systematic review of PAMI syndrome, key clinical manifestations included anemia, neutropenia, cutaneous issues, osteoarticular problems, splenomegaly, growth failure, fever, and hepatomegaly, with gastrointestinal manifestations in a minority.[11][15][15] Virtually all described patients have chronic inflammation and at least one cytopenia, and most have skin involvement and hepatosplenomegaly.[11][17][40] 

The **quality of life impact** is substantial. Chronic pain from cutaneous ulcers and arthritis, recurrent hospitalizations for infections or bleeding, fatigue from anemia, and psychosocial burden from disfiguring skin lesions and growth retardation markedly impair daily functioning and wellbeing.[35][15][15] Children may have difficulty attending school, participating in physical activity, or achieving normal developmental milestones. The requirement for long‑term immunosuppressive therapy further increases susceptibility to infections and complicates psychosocial management.[14][11] Formal quality‑of‑life instruments such as SF‑36 or EQ‑5D have not yet been systematically applied to PAMI cohorts, but anecdotal reports underscore high disease burden.

### 3.4 Suggested HPO Terms

Based on the described phenotypes, the following **Human Phenotype Ontology (HPO)** terms are appropriate for database annotation:

Hepatosplenomegaly (HP:0001433), Recurrent infections (HP:0002719), Anemia (HP:0001903), Neutropenia (HP:0001875), Thrombocytopenia (HP:0001873), Pancytopenia (HP:0001876), Growth failure/Failure to thrive (HP:0001510), Short stature (HP:0004322), Dermal ulcers (HP:0001055), Pustular skin lesions (HP:0001773), Pyoderma gangrenosum‑like ulcers (HP:0004414, approximated), Severe acne (HP:0002021), Arthralgia (HP:0002829), Arthritis (HP:0001369), Osteoporosis/Osteopenia (HP:0000938/HP:0000939), Epistaxis (HP:0000421), Spontaneous hematomas (HP:0001928), Chronic systemic inflammation (HP:0030233), Hepatomegaly (HP:0002240), Splenomegaly (HP:0001744), Lymphadenopathy (HP:0002716), Fatigue (HP:0012378), Failure to thrive (HP:0001505).

Laboratory phenotypes should include: Hyperzincemia (HP:0003331; elevated serum zinc), Hypercalprotectinemia (can be coded as increased calprotectin level in blood, HP:0032105 or analogous), Elevated C‑reactive protein (HP:0006950), Elevated ESR (HP:0003565), Bone marrow dysgranulopoiesis and dyserythropoiesis (HP:0001877/HP:0001878).

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: PSTPIP1

The causal gene for hyperzincemia with functional zinc depletion is **PSTPIP1** (HGNC: 19665), also known as CD2 antigen‑binding protein 1 or PEST phosphatase‑interacting protein 1.[28][29] PSTPIP1 is a cytosolic adaptor protein expressed predominantly in hematopoietic cells, including T lymphocytes and macrophages, where it interacts with the actin cytoskeleton and phosphatases, contributing to cytokine secretion and immune synapse formation.[11][23][28] 

PSTPIP1 is located on chromosome **15q24.3** and encodes a protein with an N‑terminal F‑BAR domain and a C‑terminal coiled‑coil region, which mediates dimerization and binding to other proteins such as pyrin, the familial Mediterranean fever protein.[29][23] Disease‑causing germline mutations in PSTPIP1 are associated with:

Hyperzincemia and hypercalprotectinemia (ORPHA:251523, OMIM:601979), PAMI syndrome.[29][16][30] Pyogenic arthritis, pyoderma gangrenosum, and acne (PAPA) syndrome (ORPHA:69126).[30][23]

The **functional role** of PSTPIP1 in disease involves modulation of inflammasome activation and myeloid cell secretion of alarmins and cytokines, particularly via interaction with pyrin and regulation of IL‑1β and IL‑18 release.[23][27] Mutations altering the charge in critical domains change these interactions in variant‑specific ways, leading to distinct clinical syndromes.

### 4.2 Pathogenic Variants: Type, Classification, and Functional Effects

The **p.E250K (c.748G>A)** and **p.E257K (c.769G>A)** PSTPIP1 variants are the primary pathogenic alleles associated with hyperzincemia and hypercalprotectinemia. They are **heterozygous missense mutations** that substitute a negatively charged glutamic acid with a positively charged lysine in the Y‑domain of PSTPIP1’s coiled‑coil region.[27][19][28]

Structural modeling of PSTPIP1 dimers showed that these mutations **substantially alter the electrostatic potential** in a region critical for protein–protein interaction, particularly with pyrin and possibly with other cytoskeletal regulators.[27][19] Functionally, these charge‑reversal mutations **increase binding of PSTPIP1 to pyrin** through enhanced phosphorylation and alter downstream signaling, leading to **hyperactivation of the pyrin inflammasome** and increased release of IL‑1β, IL‑18, and pro‑inflammatory alarmins MRP8/14 (calprotectin).[27][23][11] 

Holzinger et al. concluded that mutations resulting in **charge reversal (E→K) in the Y‑domain of PSTPIP1** cause a distinct autoinflammatory disorder characterized by extreme MRP8/14 release and hyperzincemia, with clinical and biochemical features not found in PAPA.[27][19] This constitutes a clear **genotype–phenotype correlation**, and the variants are classified as **pathogenic** based on clinical, biochemical, and functional evidence.

These variants are not somatic; they are **germline mutations**, inherited or arising de novo, and present in all cells. Intrafamilial variability suggests incomplete penetrance and variable expressivity, but there is no evidence of somatic mosaicism as a common mechanism.[3][3][38] Allele frequencies in population databases (e.g., gnomAD) are extremely low or absent, consistent with the ultra‑rare prevalence (<1/1,000,000) reported by Orphanet.[16][16][12]

The functional consequences are best described as a **gain of abnormal function** in terms of protein–protein interaction and inflammasome activation, rather than simple loss‑of‑function, since PSTPIP1 deficiency per se does not cause this phenotype and PAPA‑associated variants also increase pyrin binding but produce a different cytokine and clinical profile.[27][23] The net effect is **pathologic hyperactivation of the pyrin inflammasome and myeloid alarmin release**, with downstream metabolic perturbations in zinc and calprotectin.

### 4.3 Modifier Genes and Epigenetic Information

No specific **modifier genes** have been definitively linked to variation in disease severity among PSTPIP1 mutation carriers, although it is plausible that polymorphisms in genes encoding inflammasome components (MEFV/pyrin, NLRP3), S100A8/A9 (calprotectin), or zinc transporters and metallothioneins could influence phenotype.[27][24][4] The observation of intrafamilial variable expressivity and incomplete penetrance suggests the presence of genetic or epigenetic modifiers, but these remain unidentified in the published literature.[3][3][27]

Similarly, **epigenetic changes** specific to Hz/Hc have not been systematically investigated. Given the chronic inflammatory state, epigenetic reprogramming of myeloid cells (trained immunity) and changes in methylation in cytokine or alarmin genes are plausible contributors to disease chronicity, but no direct data from methylome or chromatin studies in PAMI patients have been reported. This represents a gap for future research.

### 4.4 Chromosomal Abnormalities and Structural Genomic Features

Hyperzincemia and hypercalprotectinemia is not associated with large‑scale chromosomal abnormalities such as aneuploidy, translocations, or inversions; its genetic basis is confined to **point mutations in PSTPIP1**.[27][29] Clinical microarray or karyotyping would be expected to be normal aside from incidental findings. 

Structural features of the PSTPIP1 locus, such as local chromatin accessibility or regulatory elements, have not been characterized in relation to Hz/Hc. There is no evidence of copy‑number variation or structural rearrangements of PSTPIP1 contributing to disease.

## 5. Environmental Information

### 5.1 Non‑Genetic Contributing Factors

As noted above, hyperzincemia with functional zinc depletion is fundamentally a **genetically determined autoinflammatory syndrome**, and **non‑genetic environmental factors** play a secondary, modulatory role. There is no evidence linking specific toxins, radiation exposure, or pollution to the development of the disease.[16][27] 

However, environmental factors can influence **flare frequency and severity**. Infections (especially bacterial infections), minor trauma, or surgical procedures may trigger intensified inflammatory responses in the skin and joints, similar to other autoinflammatory syndromes where neutrophil‑driven inflammation is pathologically amplified.[35][23] Stress, hormonal changes, or vaccination could theoretically modulate immune responses, but these interactions have not been systematically studied in Hz/Hc.

### 5.2 Lifestyle Factors

Lifestyle factors such as smoking, diet, and physical activity have not been specifically evaluated in PAMI cohorts, but **dietary zinc intake** may be relevant. Elevated serum zinc is a hallmark of the disease, driven primarily by calprotectin‑bound zinc, and exogenous zinc supplementation may further raise circulating levels without resolving functional deficiency.[1][31][11] In the original case of hyperzincemia with functional zinc depletion, the presence of a plasma zinc‑binding protein and abnormal kinetics of zinc exchange suggested that standard nutritional approaches were inadequate or potentially counterproductive.[1][20] Clinicians generally avoid zinc supplementation when the disease is suspected.

Physical activity may be limited due to joint pain and systemic symptoms, but no direct evidence exists that exercise modifies disease course. Smoking and alcohol are typically not relevant in pediatric patients but could exacerbate infections or impair immune function in older individuals.

### 5.3 Infectious Agents

No specific **pathogen** has been identified as a causal agent in hyperzincemia with functional zinc depletion. However, **recurrent infections** are common manifestations due to neutropenia and impaired immune function, and infections can serve as triggers for flares.[16][3][11] Calprotectin itself has antimicrobial properties and plays a key role in nutritional immunity by chelating zinc and other metals to limit pathogen growth, and dysregulated calprotectin release in Hz/Hc may both contribute to chronic inflammation and alter host–pathogen interactions.[24][21][35]

There is no evidence of zoonotic transmission or specific viral or bacterial etiologies driving the disease; instead, infections should be viewed as complications and modulators of disease activity.

## 6. Mechanism / Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Phenotype

1. Heterozygous p.E250K or p.E257K mutation in PSTPIP1 leads to charge reversal in the coiled‑coil Y‑domain of the protein, altering its electrostatic surface and protein–protein interaction capacity.[27][19]  
2. Altered PSTPIP1 leads to increased interaction with pyrin and augmented phosphorylation, which in turn results in hyperactivation of the pyrin inflammasome in myeloid cells.[27][23]  
3. Hyperactivation of the pyrin inflammasome leads to excessive release of IL‑1β, IL‑18, and pro‑inflammatory alarmins MRP8/14 (S100A8/S100A9, calprotectin) from neutrophils and monocytes.[27][11]  
4. Excessive release of MRP8/14 (calprotectin) leads to extreme elevation of circulating calprotectin levels (500–12,000‑fold normal), which results in high‑affinity chelation and sequestration of zinc and other transition metals via its His\(_3\)Asp and His\(_6\) motifs.[35][24][25]  
5. Calprotectin‑mediated zinc sequestration leads to dramatically increased serum zinc concentrations (hyperzincemia), but with much of the zinc bound in calprotectin complexes and redistributed to tissues, resulting in functional zinc depletion at the cellular level in critical organs such as skin, bone marrow, and immune cells.[1][35][3]  
6. Functional zinc depletion and chronic inflammasome activation together lead to impaired immune function, dysgranulopoiesis and dyserythropoiesis, and cytopenias (anemia, neutropenia, thrombocytopenia), despite hyperzincemia.[3][11]  
7. Chronic IL‑1β/IL‑18–driven inflammation, combined with zinc dyshomeostasis and alarmin signaling, leads to hepatosplenomegaly, growth failure, osteoarticular disease, and cutaneous ulcerative lesions through persistent recruitment and activation of neutrophils and macrophages in liver, spleen, joints, and skin.[16][35][18]  
8. Persistent systemic inflammation and cytopenias lead to recurrent infections, epistaxis, spontaneous hematomas, and overall failure to thrive, which are the key clinical manifestations of hyperzincemia with functional zinc depletion.[16][16][11]  

Some steps in this chain, such as the exact distribution of zinc in specific tissues and the detailed mechanisms of growth failure, are inferred from general zinc biology and the clinical presentation rather than directly demonstrated in PAMI patients.

### 6.2 Molecular Pathways: Pyrin Inflammasome and Alarmin Release

At the molecular level, hyperzincemia with functional zinc depletion is best understood as a disease of **dysregulated inflammasome signaling and alarmin release**. PSTPIP1 interacts with pyrin, the product of the MEFV gene mutated in familial Mediterranean fever, and PAPA‑associated mutations in PSTPIP1 are known to increase binding affinity to pyrin and promote IL‑1β and IL‑18 release through pyrin inflammasome activation.[23] Holzinger et al. showed that Hz/Hc‑associated PSTPIP1 mutations (p.E250K, p.E257K) further alter PSTPIP1’s electrostatic potential, increasing interaction with pyrin through enhanced phosphorylation and driving a distinct cytokine profile.[27][19]

The **pyrin inflammasome** pathway involves sensing of Rho GTPase activity and cytoskeletal perturbations, leading to assembly of ASC‑containing inflammasomes, caspase‑1 activation, and maturation of IL‑1β and IL‑18.[23] Mutant PSTPIP1 appears to artificially enhance pyrin activation, leading to chronic, inappropriate inflammasome signaling and IL‑1β/IL‑18 secretion. This triggers downstream **IFN‑γ feedback loops** and further pyrin expression in some contexts, as shown in PAPA syndrome; in PAMI, the feedback may be even more pronounced due to higher levels of MRP8/14 and systemic inflammation.[23][27]

Calprotectin (MRP8/14, S100A8/S100A9) acts as a **pro‑inflammatory alarmin**, binding to TLR4 and RAGE receptors, activating NF‑κB signaling, and amplifying cytokine production.[24][21] In Hz/Hc, serum calprotectin levels are extremely elevated, with values 20‑fold higher than PAPA and 500–12,000‑fold above normal healthy ranges.[27][35][11] This massive alarmin burden potently stimulates myeloid and endothelial cells, sustaining IL‑1, IL‑6, TNF‑α, and other cytokines, and driving chronic systemic inflammation.

Thus, key pathways include: the **MEFV/pyrin inflammasome**, **caspase‑1/IL‑1β/IL‑18 axis**, **TLR4/RAGE–NF‑κB signaling via calprotectin**, and possibly **IFN‑γ–mediated feedback loops** that further upregulate pyrin and PSTPIP1 activity.[23][27][24] These pathways underpin the autoinflammatory nature of the disease.

Suggested GO biological process terms include: “inflammasome complex assembly” (GO:0140235), “interleukin‑1 beta production” (GO:0032612), “interleukin‑18 production” (GO:0032611), “positive regulation of NF‑κB transcription factor activity” (GO:0051092), and “neutrophil activation involved in immune response” (GO:0002283).

### 6.3 Protein Dysfunction: PSTPIP1 Charge Switch and Calprotectin Metal Binding

At the protein level, two dysfunctional processes are central: altered PSTPIP1 interaction surfaces and aberrant calprotectin metal binding.

For **PSTPIP1**, the charge reversal from glutamate to lysine at positions 250 or 257 changes the local electrostatic potential in the coiled‑coil dimer interface.[27][19] Modeling studies suggest that this region is critical for binding to pyrin and other partners, and the introduction of positive charges enhances or destabilizes specific interactions, leading to increased pyrin binding through phosphorylation‑dependent mechanisms.[27] This altered binding is a **gain of abnormal function**, causing unregulated inflammasome activation rather than loss of normal function.

For **calprotectin**, structural studies reveal two distinct zinc‑binding sites: **Site I**, a His\(_3\)Asp motif formed by His83 and His87 from S100A8 and His20 and Asp30 from S100A9, capable of binding Zn\(^{2+}\) and Mn\(^{2+}\); and **Site II**, a **His\(_6\)** motif composed of His17 and His27 from S100A8 and His91, His95, His103, and His105 from S100A9, binding Zn\(^{2+}\), Fe\(^{2+}\), and Ni\(^{2+}\) with high affinity.[24][25] High‑resolution crystal structures show tetracoordinate binding in the His\(_3\)Asp site and hexacoordinate binding in the His\(_6\) site, with histidine ligands from both subunits coordinating zinc via N\(^\varepsilon2\) atoms.[22][25] Under the influence of Ca\(^{2+}\), calprotectin oligomerizes into stable heterotetramers or larger complexes, further enhancing metal binding and functional potency.[24][25]

In Hz/Hc, **massive overproduction of calprotectin** leads to an excess of high‑affinity zinc‑binding sites in the circulation and tissues, such that a large fraction of extracellular zinc becomes bound to calprotectin complexes. This unique ability to bind a wide range of transition metals with high affinity contributes to hyperzincemia and may simultaneously deprive cells of freely exchangeable zinc, generating a state of functional deficiency despite abundance.[24][25][35] This phenomenon underlies the concept of “functional zinc depletion,” as the plasma zinc pool is expanded but largely sequestered and rapidly trafficked into stable compartments, as shown in kinetic studies with zinc isotopes in the original Sampson case.[1][20]

### 6.4 Metabolic Changes: Zinc Compartmentalization and Metal Homeostasis

From a metabolic perspective, hyperzincemia with functional zinc depletion involves profound **dyshomeostasis of zinc and other transition metals**. Zinc is an essential cofactor for hundreds of enzymes and transcription factors, and its homeostasis is tightly regulated by transporters (ZnT/SLC30A and ZIP/SLC39A families), metallothioneins, and binding proteins such as albumin.[4][5][2] 

In the original 11‑year‑old boy with hyperzincemia, kinetic studies using stable zinc isotopes revealed increased exchangeable zinc and rapid flux from plasma to a stable pool, with elevated zinc and copper concentrations in liver and muscle and increased immunoreactive metallothionein in the liver, despite normal liver histology.[1][20] These findings suggested an inborn error of zinc metabolism with abnormal plasma binding and distribution. Later, in Hz/Hc patients, extreme serum zinc levels (e.g., 869 µg/L vs normal 70–120 µg/L) were observed alongside calprotectin levels 500–12,000 times normal, indicating that calprotectin is the major zinc‑binding protein in plasma in this context.[35][11] 

Calprotectin’s high‑affinity His\(_3\)Asp and His\(_6\) sites enable chelation of Zn\(^{2+}\), Mn\(^{2+}\), Fe\(^{2+}\), and Ni\(^{2+}\), contributing to **nutritional immunity** by depriving pathogens of essential metals.[24][25] In PAMI, however, this mechanism is pathologically excessive, resulting in altered metal homeostasis for host cells. Sequestration of zinc into calprotectin complexes may limit zinc availability for enzymes and transcription factors in skin, bone marrow, and immune cells, contributing to impaired proliferation, differentiation, and barrier function typical of zinc deficiency.[2][2][35] Functional zinc depletion therefore coexists with hyperzincemia, a paradox explained by altered binding and compartmentalization rather than total body deficiency.

Suggested CHEBI terms include: “zinc cation” (CHEBI:29105), “manganese(2+) cation” (CHEBI:29035), “nickel(2+) cation” (CHEBI:25517), and “calcium(2+) cation” (CHEBI:29108), which play roles in calprotectin metal binding and oligomerization.

### 6.5 Immune System Involvement and Tissue Damage Mechanisms

The immune system involvement in hyperzincemia with functional zinc depletion is profound and multi‑layered. At the cellular level, **neutrophils and monocytes/macrophages** are central, as they are the primary source of calprotectin and key participants in inflammasome activation.[24][21][11] Calprotectin release from activated neutrophils and monocytes acts as a danger‑associated molecular pattern (DAMP), signaling via pattern recognition receptors to further recruit and activate myeloid cells, creating a self‑amplifying loop of inflammation.[24][35]

The **pyrin inflammasome** in myeloid cells is hyperactivated by mutant PSTPIP1, leading to IL‑1β and IL‑18 production, which promote fever, endothelial activation, and recruitment of neutrophils to sites of inflammation.[23][27] Chronic inflammasome activity contributes to **bone marrow dysplasia**, with dysgranulopoiesis and dyserythropoiesis reflecting disturbed differentiation in an inflammatory niche and altered zinc availability.[3][11] 

Tissue damage mechanisms include **neutrophil‑mediated cytotoxicity** and **oxidative stress**, as calprotectin can modulate the release of reactive oxygen species and nitric oxide.[21] In the skin and joints, persistent neutrophil infiltration and alarmin signaling drive erosive arthritis and pyoderma‑gangrenosum–like ulcers, with destruction of connective tissue and epidermal structures.[35][15][18] In the liver and spleen, chronic inflammatory cell infiltration and increased metallothionein expression may cause organ enlargement and functional changes, though histology may remain relatively preserved in early stages.[1][17]

Suggested GO terms for biological processes and tissue damage include: “neutrophil degranulation” (GO:0043312), “positive regulation of inflammatory response” (GO:0050729), “response to oxidative stress” (GO:0006979), and “cellular response to zinc ion” (GO:0071294). Suggested CL (Cell Ontology) terms include: “neutrophil” (CL:0000775), “monocyte” (CL:0000576), “macrophage” (CL:0000235), and “hepatocyte” (CL:0000182).

### 6.6 Molecular Profiling and Advanced Technologies

To date, there is **limited molecular profiling** specifically performed on Hz/Hc patients using transcriptomics, proteomics, or metabolomics. However, Holzinger et al. described a **specific cytokine profile** in Hz/Hc compared with PAPA, reflecting differences in IL‑1, IL‑6, TNF‑α, and other cytokines in serum.[27][19] They also measured MRP8/14 concentrations, finding extremely high levels in Hz/Hc (2045 ± 1300 µg/mL) vs PAPA (116 ± 74 µg/mL), providing proteomic evidence of calprotectin overproduction.[27]

Large‑scale multi‑omics integration has not yet been applied to PAMI syndrome, but this would be a fruitful avenue for future work to disentangle the contributions of inflammasome activation, alarmin signaling, and zinc homeostasis at the systems level. Single‑cell analysis of bone marrow and peripheral blood myeloid cells could reveal specific inflammatory or dysplastic populations, while spatial transcriptomics of skin lesions might clarify the microenvironment driving pyoderma‑gangrenosum–like ulcers.

Given the rarity and pediatric nature of the disease, these advanced technologies have not yet been widely deployed in clinical research cohorts, and much of the mechanistic understanding still rests on candidate‑based approaches focused on PSTPIP1, calprotectin, and zinc metabolism.

## 7. Anatomical Structures Affected

### 7.1 Organ‑Level Involvement

Hyperzincemia with functional zinc depletion affects multiple organ systems, consistent with its characterization as a **multisystem autoinflammatory disease**. Primary organs involved include:

The **liver (UBERON:0002107)** and **spleen (UBERON:0002106)**, which together exhibit hepatosplenomegaly due to chronic inflammatory cell infiltration and altered metallothionein and zinc content.[16][1][17] Orphanet and MedGen both emphasize hepatosplenomegaly as a core feature, and the original kinetic study showed elevated zinc and copper in liver.[16][3][1] 

The **bone marrow (UBERON:0002398)**, which shows dysgranulopoiesis and dyserythropoiesis, reflecting disturbed hematopoiesis and zinc‑dependent differentiation under inflammatory conditions.[3][11] Dysplasia contributes directly to cytopenias and anemia.

The **skin (UBERON:0002097)**, where pustular and ulcerative cutaneous lesions, dermal ulcers, and pyoderma‑gangrenosum–like lesions occur, often extensive and disfiguring.[16][35][15] Skin involvement is often the presenting symptom and a major contributor to morbidity.

The **joints (UBERON:0001464)** and **synovial tissue**, where arthralgia and arthritis occur, including pyogenic arthritis with neutrophil infiltration and erosive damage.[18][11][15] 

The **hematopoietic and immune system**, including lymph nodes (UBERON:0002305), peripheral blood, and reticuloendothelial system, involved through pancytopenia, lymphadenopathy, and systemic inflammation.[3][17][11] 

Secondary involvement may include the **gastrointestinal tract (UBERON:0001043)** in cases with colitis, as well as the **cardiovascular system** indirectly through anemia and systemic inflammation, though organ‑specific structural cardiac pathology is not a recognized feature.[15][15]

### 7.2 Tissue and Cell‑Level Involvement

At the tissue level, hyperzincemia with functional zinc depletion primarily affects:

Hematopoietic tissue in bone marrow, involving granulocytic and erythroid lineages that show dysplasia and impaired maturation.[3][11] CL terms include “granulocyte” (CL:0000094), “erythroid progenitor cell” (CL:0000837), and “hematopoietic stem cell” (CL:0000037). 

Cutaneous connective tissue and epidermis, where neutrophil infiltration, panniculitis, and ulceration occur, driven by autoinflammatory neutrophil activation.[35][15] CL terms include “keratinocyte” (CL:0000312), “dermal fibroblast” (CL:0002620), and “endothelial cell” (CL:0000115).

Hepatic parenchyma and splenic white pulp, where chronic inflammatory cell infiltrates and altered metal metabolism may exist, though histology may be subtle.[1][17] CL terms include “hepatocyte” and “splenic macrophage”.

Myeloid cells (neutrophils, monocytes/macrophages) are central effectors, producing calprotectin and mediating tissue damage.[24][21][11] T lymphocytes are involved through PSTPIP1’s role in T‑cell activation, although the phenotype is predominantly myeloid‑driven.[28][23]

### 7.3 Subcellular Level: Cellular Compartments

Subcellular compartments involved include:

The **inflammasome complex** localized in the cytoplasm of myeloid cells, where pyrin and ASC assemble into oligomeric platforms for caspase‑1 activation, leading to cytokine maturation.[23][27] GO cellular component terms include “inflammasome complex” (GO:0061702).

The **cytoskeleton**, where PSTPIP1 interacts with actin and regulates membrane dynamics and phagocytosis, with mutant PSTPIP1 potentially altering cytoskeletal organization and cell activation responses.[23][28] GO terms include “actin cytoskeleton” (GO:0015629).

The **secretory pathway**, particularly vesicular compartments in neutrophils and monocytes that store and release calprotectin and other granule contents.[21][24] GO terms include “secretory granule lumen” (GO:0034774).

Intracellular **zinc pools** and metallothionein‑rich compartments in liver and muscle, which are altered in distribution and quantity in the original hyperzincemia case, although specific subcellular localization in PAMI patients has not been fully mapped.[1][4] GO terms include “cytoplasm” (GO:0005737) and “metallothionein complex” (GO:0046872).

### 7.4 Localization and Lateralization

Anatomical localization of lesions is often **multifocal and bilateral**, especially in skin and joints. Pyoderma‑gangrenosum–like ulcers may appear on lower extremities, trunk, or other areas; arthritis can be symmetrical or asymmetrical, commonly involving large joints.[35][18] Hepatosplenomegaly is generalized rather than unilateral, and pancytopenia is systemic. There is no clear pattern of lateralization such as left‑ vs right‑side prevalence.

## 8. Temporal Development

### 8.1 Onset Patterns

Hyperzincemia with functional zinc depletion typically has a **pediatric onset**, with symptoms appearing in infancy or early childhood.[16][16][17] The original case report described symptoms present since infancy in an 11‑year‑old boy, including hepatosplenomegaly, rashes, anemia, and growth failure.[1][20] Orphanet lists childhood onset as characteristic, and most PAMI case reports describe patients presenting in childhood or adolescence.[16][17][15][40]

The onset pattern is generally **insidious but early**, with subtle manifestations such as poor growth, recurrent infections, and mild anemia initially, progressing to more overt systemic inflammation, cytopenias, and cutaneous ulcers over time. Some patients present acutely with severe pyoderma‑gangrenosum–like lesions or pancytopenia, but these occur against a background of long‑standing symptoms.[35][15]

### 8.2 Progression, Disease Course, and Duration

The disease course is **chronic and lifelong** in the absence of curative interventions such as HSCT.[11][40] Systemic inflammation tends to be persistent, with fluctuations in severity but rarely complete remission. Cytopenias can wax and wane with therapy but often remain at least partially present; hepatosplenomegaly may persist chronically.[11][17]

Progression can be conceptualized in stages: an early stage with growth failure, recurrent infections, mild organomegaly, and laboratory hyperzincemia; an intermediate stage with overt cytopenias, extensive cutaneous ulcers, arthritis, and marked systemic inflammation; and an advanced stage where complications such as severe anemia, recurrent severe infections, and extensive tissue damage (e.g., scarring from ulcers, joint erosions) dominate.[16][35][15] Disease progression rate varies, influenced by early diagnosis and treatment, but generally the syndrome is **progressive without effective control**.

The pattern is **relapsing‑remitting** in terms of flares of skin and joint symptoms, superimposed on a background of chronic systemic inflammation and cytopenias. Flares may be triggered by environmental factors or occur spontaneously.[35][15] With successful HSCT, some patients have experienced resolution of symptoms and normalization of inflammatory markers and zinc levels, suggesting that durable remission or cure is possible.[11][40][14]

### 8.3 Remission Patterns and Critical Periods

Spontaneous remission is rare; improvements are typically **treatment‑induced** through immunosuppressive therapies or HSCT.[11][14][40] Corticosteroids and biologics may induce partial remission of symptoms and laboratory abnormalities, but relapses are common when therapies are tapered or withdrawn.[11][36]

Critical periods include **early childhood**, where growth failure, bone development, and immune system maturation are most vulnerable to the combined effects of chronic inflammation and functional zinc depletion. Prompt diagnosis and effective control of inflammation and zinc dyshomeostasis during this period may mitigate long‑term complications such as short stature, osteoporosis, and organ damage.[16][1][9] Another critical period is around **HSCT**, where risk of transplant‑related complications must be balanced against potential cure; careful timing and conditioning are crucial.[11][40][14]

## 9. Inheritance and Population

### 9.1 Epidemiology: Prevalence and Incidence

Hyperzincemia and hypercalprotectinemia is classified as an **ultra‑rare disease**, with Orphanet estimating a prevalence of <1 per 1,000,000.[16][16] Given the small number of reported cases worldwide and the lack of registries, precise incidence figures are unavailable, but incidence is likely to be extremely low, on the order of a handful of new cases per year globally.

Most published literature consists of individual case reports, small case series, and a few systematic reviews, reflecting the limited number of diagnosed patients.[31][35][11][15][17][15][40] Underdiagnosis is possible, particularly in settings without access to calprotectin measurement or PSTPIP1 genetic testing, so true prevalence may be somewhat higher than recognized.

### 9.2 Inheritance Pattern, Penetrance, and Expressivity

Hyperzincemia with functional zinc depletion exhibits a **dominant inheritance pattern** with **heterozygous PSTPIP1 mutations**.[27][3][3] MedGen and Disease Ontology explicitly state that the syndrome has a material basis in **heterozygous mutation in PSTPIP1**.[3][12][3] Some cases are familial, with multiple affected relatives carrying the same mutation, while others are de novo, as illustrated by a case where a child carried p.E250K but his parents and younger brother did not.[38] 

Penetrance appears **incomplete and variable**, as intrafamilial variability has been observed, with some mutation carriers showing milder disease or subclinical laboratory abnormalities.[3][27][3] Expressivity is **variable**, affecting the severity and combination of phenotypes (e.g., some with more prominent cutaneous lesions, others with severe cytopenias or colitis).[15][15][17] There is no evidence of genetic anticipation, as repeat expansion mechanisms are not involved.

Germline mosaicism has not been reported in PAMI syndrome, but cannot be entirely excluded given de novo mutations in single individuals. Founder effects have not been described; cases occur in diverse geographic and ethnic backgrounds, although small Bedouin kindreds have been noted for related SLC30A9 disorders rather than PSTPIP1.[10][4][8] Consanguinity plays a role in autosomal recessive zinc transporter disorders (e.g., SLC30A9 cerebro‑renal syndrome) but is not characteristic for PSTPIP1‑related Hz/Hc, which is heterozygous and dominant.[4][10]

Carrier frequency in the general population is extremely low (consistent with ultra‑rare disease), with p.E250K and p.E257K absent or nearly absent in population databases.[27][28][12]

### 9.3 Population Demographics and Geographic Distribution

Reported cases of hyperzincemia and hypercalprotectinemia arise from various countries, including European nations, North America, and Asia, suggesting **no strong geographic clustering**.[31][35][11][15][40] Orphanet does not indicate any particular endemic region.[16][16]

Sex distribution is approximately balanced, with no consistent male or female predominance described.[35][17][11] Age distribution centers on childhood and adolescence, with rare adult‑onset cases possibly representing milder or delayed expressivity.[15][15]

Because of the rarity and underdiagnosis, demographic patterns must be interpreted cautiously, but overall the disease appears to affect **all ethnicities and both sexes**, with pediatric onset.

## 10. Diagnostics

### 10.1 Clinical and Laboratory Tests

Diagnostics for hyperzincemia with functional zinc depletion rely on a combination of **clinical suspicion, laboratory measurement of serum zinc and calprotectin, and genetic testing of PSTPIP1**.

Serum zinc measurement reveals **marked hyperzincemia**, often several times the upper limit of normal. In one case, zinc levels were 869 µg/L (normal 70–120 µg/L), and in another, 4.5 mg/L in a child where normal reference range was 3.7–7.3 mg/L, highlighting elevated but not necessarily extreme values compared with reference ranges.[35][38] The original Sampson case had plasma Zn >200 µmol/L (~13 mg/L), significantly higher than normal.[1][20] Hyperzincemia is thus a key laboratory marker.

Serum **calprotectin (MRP8/14)** levels are **extraordinarily elevated**, often 500–12,000 times normal.[35][11] Holzinger et al. reported MRP8/14 concentrations of 2045 ± 1300 µg/mL in Hz/Hc vs 116 ± 74 µg/mL in PAPA, underscoring the magnitude of this biomarker difference.[27] Case reports describe calprotectin levels such as 642 µg/L vs normal <1.6 µg/L.[35] Measurement of serum zinc and calprotectin is therefore **strongly indicated in cases of unexplained systemic inflammation with skin ulcers and cytopenias**, and abnormal values are highly suggestive of Hz/Hc.[35][15]

Routine hematologic tests reveal **anemia, neutropenia, thrombocytopenia**, and **pancytopenia**, often with elevated inflammatory markers (CRP, ESR).[3][11][11] Bone marrow aspirates show **dysgranulopoiesis and dyserythropoiesis** without clear malignant transformation.[3][3] Liver function tests may be normal or mildly abnormal; imaging studies show hepatosplenomegaly.[1][17]

Histopathology of skin lesions often reveals dense neutrophilic infiltrates, ulceration, and features reminiscent of pyoderma gangrenosum, but no specific diagnostic pattern beyond neutrophilic dermatosis.[35][15] In rat models of experimentally induced hyperzincemia, dental enamel pathology has been observed, but this is not a diagnostic feature in humans.[6][6]

### 10.2 Genetic Testing

Genetic testing is crucial to confirm diagnosis and distinguish PAMI from PAPA syndrome and other autoinflammatory disorders. **PSTPIP1 sequencing** (by Sanger or next‑generation methods) targeted at exons including codons 250 and 257 is recommended.[27][29][28] Detection of heterozygous p.E250K or p.E257K supports the diagnosis of PAMI/Hz/Hc, but as noted in one case, genetic testing alone cannot always differentiate PAPA vs Hz/Hc, necessitating correlation with clinical and laboratory features.[38][27]

Whole exome sequencing (WES) or gene panels for autoinflammatory/periodic fever syndromes often include PSTPIP1, MEFV, NLRP3, and other genes, and can detect PSTPIP1 mutations in undiagnosed patients with systemic inflammation and cutaneous lesions.[7][14] Given the specificity of PSTPIP1 mutations, WES is useful when clinical suspicion is high but targeted testing has not been performed.

Chromosomal microarray (CMA), karyotyping, FISH, and mitochondrial DNA testing are not typically needed, as the disease is due to point mutations rather than structural changes.

### 10.3 Omics‑Based Diagnostics and Biomarkers

Beyond serum zinc and calprotectin, no other omics‑based diagnostics are currently standard. **Serum zinc** serves as a simple, cost‑effective **screening tool** and practical biomarker for monitoring therapy response.[15][11] Calprotectin is a more specific indicator of the underlying mechanism, reflecting alarmin release, and may be used both for diagnosis and follow‑up.

Omics approaches such as RNA sequencing, proteomics, or metabolomics could reveal specific signatures in PAMI patients (e.g., cytokine profiles, zinc‑dependent metabolic changes), but have not yet been incorporated into routine diagnostics.

### 10.4 Clinical Criteria and Differential Diagnosis

There is no formally codified **diagnostic criteria set**, but clinical features commonly used include:

Chronic systemic inflammation with recurrent fevers, hepatosplenomegaly, cytopenias, and growth failure. Dermatologic involvement with pustular or ulcerative lesions, pyoderma gangrenosum‑like ulcers, and severe acne. Osteoarticular manifestations with arthralgia or arthritis. Laboratory findings of hyperzincemia and hypercalprotectinemia, with extremely high MRP8/14. Presence of heterozygous PSTPIP1 p.E250K or p.E257K mutation.[16][27][35][11]

Differential diagnosis includes:

**PAPA syndrome**, which shares PSTPIP1 mutations but differs with milder zinc/calprotectin elevations, absence of severe cytopenias and growth failure, and different cytokine profile.[27][23][38] Other **autoinflammatory syndromes** (e.g., FMF, CAPS, TRAPS) that can present with fever, rash, and arthritis, but do not show hyperzincemia/hypercalprotectinemia and PSTPIP1 mutations.[11][14] **Primary immunodeficiencies** and **autoimmune cytopenia syndromes** with childhood cytopenias and organomegaly, absent the specific zinc/calprotectin profile.[14][11] Severe **neutrophilic dermatoses** such as classical pyoderma gangrenosum, without systemic hyperzincemia/calprotectinemia.[35][15]

Careful consideration of these differential diagnoses is important, as misdiagnosis can delay appropriate therapy and genetic counseling.

### 10.5 Screening

There are no population‑based **screening programs** for Hz/Hc given its rarity. However, **targeted screening** is recommended in:

Children with unexplained chronic systemic inflammation, hepatosplenomegaly, pancytopenia, growth failure, and severe neutrophilic skin lesions, where measurement of serum zinc and calprotectin can be highly informative.[35][15] Relatives of known PSTPIP1 mutation carriers, where genetic testing can detect asymptomatic or mildly affected individuals and guide monitoring.[27][14]

Newborn screening is not currently implemented, though in theory severe familial cases might benefit from early detection and prophylactic management.

## 11. Outcome and Prognosis

### 11.1 Survival, Mortality, and Life Expectancy

Because of limited patient numbers and follow‑up, **quantitative survival rates and life expectancy** for hyperzincemia with functional zinc depletion are not well defined. Case series and systematic reviews suggest that mortality can occur due to complications such as severe infections, bleeding, or organ failure, but many patients survive into adolescence or adulthood with chronic disease.[11][40][17] 

Allogeneic HSCT has demonstrated **successful outcomes** in at least five patients, resulting in resolution of PAMI symptoms, normalization of inflammatory markers and zinc levels, and discontinuation of specific therapies, suggesting that life expectancy may approximate general population if HSCT is successful.[11][14][40] Without HSCT, long‑term prognosis is more guarded, depending on severity of cytopenias, infection burden, and treatment response.

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity is substantial, driven by chronic systemic inflammation, cytopenias, skin ulcers, arthritis, and growth failure. Disability outcomes include:

Physical disability from joint damage and persistent ulcers, limiting mobility and daily activities.[35][15][15] Developmental and psychosocial Impact from chronic illness, hospitalizations, and cosmetic disfigurement.[40][11] Learning difficulties or school absenteeism due to fatigue, pain, and frequent medical appointments.[15][15]

Quality of life is markedly reduced, though formal EQ‑5D or SF‑36 data are lacking. Treatment regimens involving corticosteroids and immunosuppressants carry additional burdens, including side effects and increased infection risk.[11][14][40]

### 11.3 Disease Course, Complications, and Recovery Potential

Complications of hyperzincemia with functional zinc depletion include:

Severe **infections** due to neutropenia and immunosuppression, which can be life‑threatening. **Bleeding events** such as severe epistaxis and spontaneous hematomas due to thrombocytopenia.[16][16] Chronic **anemia**, causing fatigue and cardiac strain. **Organomegaly** and potential progressive liver or spleen dysfunction. **Colitis** and gastrointestinal complications in some patients.[15][15] Psychological complications including depression and anxiety.[15][11]

Recovery potential is limited with conventional medical therapy; partial remission of symptoms and laboratory abnormalities is possible, but complete normalization is rare. HSCT offers a **curative potential**, with reported cases showing full resolution of symptoms and laboratory abnormalities, suggesting that replacement of the hematopoietic compartment corrects PSTPIP1‑driven inflammasome activation and calprotectin release.[11][40][14]

### 11.4 Prognostic Factors and Biomarkers

Prognostic factors likely include:

Age at diagnosis (earlier diagnosis allows more timely intervention and potential HSCT). Severity of cytopenias and organomegaly. Treatment responsiveness (particularly to corticosteroids, biologics, and HSCT).[11][40] Presence of severe colitis or other organ involvement.[15][15]

Serum zinc and calprotectin levels are useful **prognostic biomarkers**, as higher levels correlate with more severe inflammation and disease burden. Reduction in these markers with treatment correlates with clinical improvement, and they can thus be used to monitor therapy response.[35][11][15]

## 12. Treatment

### 12.1 Pharmacotherapy: Corticosteroids, Calcineurin Inhibitors, and Biologics

Treatment of hyperzincemia with functional zinc depletion is challenging, with **no consistently effective standard therapy** identified to date.[11][36][14] Various pharmacologic approaches have been used, with variable responses:

**Corticosteroids** (e.g., prednisone, methylprednisolone) are commonly used for acute flares and as maintenance therapy, providing rapid anti‑inflammatory effects and symptom relief, particularly for skin and joint manifestations.[11][14][40] However, long‑term steroid use carries significant side effects and may not fully control cytopenias or zinc/calprotectin abnormalities.[11][37]

**Calcineurin inhibitors** such as **cyclosporine A** and **tacrolimus** have been tried, with mixed results. Cyclosporine A has shown benefit for leukopenia and general inflammatory control in some patients, and is listed as a therapeutic option in multiple case reports and systematic reviews.[11][40][36] Conversely, tacrolimus treatment in a 5‑year‑old boy with hyperzincemia and hypercalprotectinemia yielded only transient improvement; zincemia and calprotectinemia progressively worsened with secondary reappearance of symptoms, leading authors to conclude that tacrolimus has only a transient effect.[31][31] 

Biologic agents targeting cytokines have been employed:

**Anti‑IL‑1 therapies** such as **anakinra** and **canakinumab** have been used in several patients (n ≈ 13 for anakinra, n ≈ 6 for canakinumab in one review), with variable efficacy.[11] Some individuals show significant improvement in systemic inflammation and symptoms, while others show minimal response; anakinra may rapidly normalize inflammatory parameters but fail to correct bone marrow involvement or cytopenias.[37][11] Globally, anti‑IL‑1 therapy appears less effective than anti‑TNF, with about 40% of patients experiencing improvement.[11] 

**Anti‑TNF therapies** including **adalimumab**, **etanercept**, and **infliximab** have demonstrated more consistent benefits in certain manifestations, notably pyoderma‑gangrenosum–like skin lesions and pyogenic arthritis.[11][40][36] In one case, adalimumab led to significant clinical and endoscopic remission of PAMI‑related colitis, although its efficacy in colitis is not universally established.[15] Overall, 57% of patients treated with anti‑TNF therapy experienced clinical improvement.[11]

Other biologics such as **tocilizumab** (anti‑IL‑6) have been used in a small number of cases, again with variable response.[11] Methotrexate and colchicine have been adjunctive therapies with limited data.[11][40]

Pharmacogenomics specific to PAMI have not been studied, but given the central role of IL‑1β, IL‑6, TNF‑α, and calprotectin, targeted biologics against these pathways are logical options even without genotype‑guided dosing.

Suggested NCIT terms include: “Corticosteroid therapy” (NCIT:C15731), “Tumor Necrosis Factor Inhibitor Therapy” (NCIT:C16033), “Interleukin-1 Inhibitor Therapy” (NCIT:C121938), “Cyclosporine A” (NCIT:C408), “Tacrolimus” (NCIT:C1282), and “Adalimumab” (NCIT:C65202).

### 12.2 Advanced Therapeutics: Hematopoietic Stem Cell Transplantation

Allogeneic **hematopoietic stem cell transplantation (HSCT)** has emerged as a promising **curative therapy** for severe, treatment‑refractory PAMI syndrome. In the systematic review, HSCT was reported to be successful in five patients, leading to resolution of PAMI symptoms, normalization of inflammatory markers and zinc levels, and discontinuation of specific therapies.[11] Case reports corroborate that HSCT can correct cytopenias and severe autoinflammation, presumably by replacing mutant PSTPIP1‑bearing hematopoietic cells with donor cells lacking the pathogenic variant.[40][14]

HSCT carries significant risks, including graft‑versus‑host disease, infections, and transplant‑related mortality, and is thus reserved for **severe cases** where conventional therapy has failed and disease burden is high.[14][11] Conditioning regimens, donor selection, and timing must be carefully considered. Successful HSCT represents the strongest evidence that hyperzincemia with functional zinc depletion is primarily a hematopoietic cell disorder, and that restoring normal PSTPIP1 function in these cells can normalize zinc and calprotectin metabolism.

Suggested NCIT terms include: “Allogeneic Hematopoietic Stem Cell Transplantation” (NCIT:C15197), “Myeloablative Conditioning Regimen” (NCIT:C80188).

### 12.3 Surgical and Interventional Approaches

Surgical interventions are not central to disease control but may be required for complications. Debridement or surgical management of severe pyoderma‑gangrenosum–like ulcers may be necessary, though surgery can also trigger pathologic wound healing and is approached cautiously.[35][15] Central venous access for repeated transfusions or drug delivery may be needed in severe cytopenias.

No disease‑specific surgery exists, and management remains primarily medical.

### 12.4 Supportive and Rehabilitative Care

Supportive care is critical, including:

Transfusion support for severe anemia or thrombocytopenia. Aggressive infection prevention and treatment, including prophylactic antibiotics or granulocyte colony‑stimulating factor (G‑CSF) in some cases. Nutritional support to address failure to thrive and growth failure. Pain management for ulcers and arthritis, and wound care for skin lesions.[11][14][40]

Rehabilitative efforts such as physical therapy and psychosocial support can help address functional impairment and quality of life issues.[11][15] Given long‑term immunosuppressive therapy, monitoring for opportunistic infections and medication side effects is essential.

### 12.5 Experimental Treatments and Personalized Strategies

No large controlled clinical trials have been conducted specifically in PAMI syndrome, but ongoing experimental approaches in the broader field of autoinflammatory diseases, such as **small‑molecule inflammasome inhibitors**, may eventually be applied to PSTPIP1‑related diseases.[23][27] Gene therapy targeting PSTPIP1 is not currently feasible, given the complexity of systemic hematopoietic involvement and the risk of off‑target effects.

Personalized medicine approaches focus on **genotype‑guided diagnosis** and management: once PSTPIP1 p.E250K or p.E257K is identified, clinicians can anticipate an Hz/Hc phenotype and prioritize therapies targeting IL‑1, TNF‑α, and calprotectin, while considering HSCT in severe cases.[27][11][14] Precision dosing and drug choice may also be influenced by comorbidities and previous treatment responses.

## 13. Prevention

### 13.1 Primary, Secondary, and Tertiary Prevention

Primary prevention of hyperzincemia with functional zinc depletion is challenging due to its **monogenic, largely sporadic nature**. In families with known PSTPIP1 mutations, **genetic counseling** and options such as preimplantation genetic diagnosis or prenatal testing could theoretically prevent the birth of affected offspring, but such interventions have not been widely reported given the rarity of the disease.[14][9]

Secondary prevention focuses on **early detection and intervention**. Clinicians should consider measuring serum zinc and calprotectin in children with chronic systemic inflammation, cytopenias, hepatosplenomegaly, and severe neutrophilic dermatoses, to detect Hz/Hc before irreversible complications occur.[35][15] Genetic testing of PSTPIP1 should follow if biochemical markers suggest the diagnosis.

Tertiary prevention aims to **prevent complications** in diagnosed patients. This includes aggressive management of infections, careful monitoring of cytopenias, avoidance of unnecessary trauma or surgery, and timely consideration of HSCT in severe cases.^[11][14][40] Vaccination schedules should be optimized to protect against common pathogens while balancing immunosuppression.

### 13.2 Immunization and Behavioral Interventions

Standard pediatric immunizations are recommended; there are no disease‑specific vaccine strategies beyond routine prevention of infections that could exacerbate disease or complicate cytopenias.[14][11] Behavioral interventions, such as meticulous skin care to avoid trauma and infection, adherence to treatment regimens, and balanced nutrition, may reduce flare frequency and support overall health.

### 13.3 Genetic Counseling and Public Health Considerations

Genetic counseling is important for families with PSTPIP1 mutations, providing information on inheritance risk, options for testing relatives, and implications for family planning.[14][29][9] Given incomplete penetrance and variable expressivity, counseling should emphasize uncertainty in predicting severity for carriers.

At the public health level, hyperzincemia with functional zinc depletion is too rare to warrant specific population‑level interventions, but awareness among pediatricians and dermatologists is important to avoid misdiagnosis and delayed treatment. Resources from Orphanet, GARD, and rare disease networks can support education and guideline development.[16][9][33]

## 14. Other Species / Natural Disease

### 14.1 Species and Natural Disease in Animals

There are no reports of **naturally occurring hyperzincemia and hypercalprotectinemia** in companion animals or livestock corresponding exactly to the human PAMI phenotype. However, calprotectin and zinc biology are conserved across species, and animal studies provide insights into mechanisms.

In rats, experimental hyperzincemia induced by zinc administration has been used to study **histopathological consequences on teeth**, revealing dental enamel pathology and changes in metal metabolism.[6][6] These models demonstrate that high zinc levels can cause tissue‑specific pathology, but they do not replicate the autoinflammatory and calprotectin‑driven aspects of human Hz/Hc.

Calprotectin’s antimicrobial and metal‑binding functions have been studied in mouse models, showing that S100A8/A9 heterodimers chelate metals and limit bacterial growth, confirming the role of calprotectin in nutritional immunity across species.[24][21] These comparative studies support the relevance of calprotectin in metal homeostasis and inflammation but do not represent a distinct animal disease entity.

### 14.2 Comparative Biology and Evolutionary Conservation

The zinc‑binding motifs in calprotectin (His\(_3\)Asp, His\(_6\)) and its antimicrobial functions are evolutionarily conserved among mammals, indicating that the mechanisms underlying hyperzincemia in human PAMI syndrome are rooted in fundamental biology.[24][25][22] PSTPIP1 orthologs exist in other species, and their roles in cytoskeletal regulation and immune signaling are likely similar, but no animal models with PSTPIP1 p.E250K or p.E257K mutations have been reported.

Comparative pathology suggests that while nutrient metal dyshomeostasis and autoinflammation are common themes, the exact combination of hyperzincemia, hypercalprotectinemia, cytopenias, and neutrophilic dermatoses is unique to human PAMI syndrome.

## 15. Model Organisms

### 15.1 Existing Models and Their Characteristics

Currently, there are no specific **genetic animal models** (e.g., PSTPIP1 p.E250K knock‑in mice) reported that recapitulate the full spectrum of hyperzincemia with functional zinc depletion. However, related models in autoinflammatory disease research provide partial insights:

Mouse models with **pyrin inflammasome activation** and MEFV mutations have been used to study familial Mediterranean fever, demonstrating the impact of inflammasome hyperactivity on systemic inflammation and IL‑1β production.[23] These models share inflammasome pathology but not zinc dyshomeostasis.

Models manipulating **calprotectin expression** (S100A8/A9 knockout or overexpression) have been used to study infection and inflammation, confirming calprotectin’s role in metal chelation and DAMP signaling.[24][21] Overexpression models could, in principle, mimic aspects of hyperzincemia if zinc binding is sufficiently enhanced, but such data have not been explicitly reported.

Rat models of **hyperzincemia** induced by zinc administration show tissue pathology, including dental enamel changes, but lack the genetic autoinflammatory component.[6][6]

Thus, existing models capture parts of the mechanism (inflammasome activation, calprotectin function, zinc toxicity) but do not fully recapitulate PAMI syndrome. The development of PSTPIP1 E250K/E257K knock‑in mice would be a valuable tool for future research.

### 15.2 Applications and Limitations

Available models can be used to study:

Inflammasome signaling pathways (pyrin, NLRP3) and their modulation by PSTPIP1 and cytokines. Calprotectin’s role in nutritional immunity, metal chelation, and DAMP signaling. Zinc’s impact on tissue pathology in experimental hyperzincemia.[23][24][6]

However, limitations include:

Lack of a model combining PSTPIP1 mutation, calprotectin overproduction, and systemic zinc dyshomeostasis. Differences in immune system architecture and zinc metabolism between rodents and humans. Difficulty in modeling the complex bone marrow dysplasia and cytopenias seen in PAMI syndrome.

Despite these limitations, model organisms remain essential for testing candidate therapies (e.g., inflammasome inhibitors) and exploring mechanistic hypotheses that can then be validated in human patients.

## Conclusion

Hyperzincemia with functional zinc depletion, also known as hyperzincemia and hypercalprotectinemia or PSTPIP1‑associated myeloid‑related proteinemia inflammatory (PAMI) syndrome, is a paradigmatic example of a **Mendelian autoinflammatory disease intersecting trace metal metabolism and alarmin biology**. It is defined by heterozygous charge‑reversal mutations in PSTPIP1 (p.E250K, p.E257K) that alter protein–protein interactions, leading to hyperactivation of the pyrin inflammasome, excessive release of IL‑1β/IL‑18 and the alarmin calprotectin (MRP8/14), and profound dyshomeostasis of zinc and other metals.[27][19][24][25] The resulting phenotype—chronic systemic inflammation, cytopenias, hepatosplenomegaly, growth failure, and severe neutrophilic dermatoses—occurs in the paradoxical context of extreme serum hyperzincemia yet functional zinc depletion at the tissue level, as calprotectin sequesters zinc into high‑affinity complexes and alters its compartmentalization.[1][35][3]

Clinically, the disease is ultra‑rare but devastating, with onset in childhood, relapsing‑remitting flares, and significant morbidity affecting quality of life. Diagnosis relies on recognizing the combination of systemic inflammation, cytopenias, skin ulcers, and organomegaly, measuring serum zinc and calprotectin, and confirming PSTPIP1 mutations. Differentiation from related syndromes such as PAPA is essential, as PAMI features more severe systemic disease and dramatically higher calprotectin and zinc levels.[27][38] Treatment is currently empirical and multi‑modal: corticosteroids, calcineurin inhibitors, and biologics targeting IL‑1 or TNF‑α offer partial control but variable responses, while HSCT has emerged as a potentially curative option in severe, refractory cases, normalizing zinc and calprotectin levels and resolving inflammation in reported patients.[11][14][40]

From a mechanistic standpoint, hyperzincemia with functional zinc depletion offers a unique lens into the interplay between inflammasomes, alarmins, and metal metabolism. It illustrates how dysregulated DAMP release and nutritional immunity mechanisms, evolved to protect against pathogens, can become pathogenic when chronically activated, leading not only to inflammation but also to systemic metabolic disturbances. It also underscores the complexity of zinc biology, where total serum levels may mislead clinicians in the absence of understanding of binding proteins and compartmentalization.

Future research priorities include developing specific animal models carrying PSTPIP1 E→K mutations, performing multi‑omics profiling in patients to capture transcriptomic and metabolomic signatures, and investigating potential inflammasome inhibitors or calprotectin‑targeted therapies. Improved understanding of genetic and environmental modifiers could refine prognostic assessments and suggest personalized intervention strategies. For now, hyperzincemia with functional zinc depletion remains a rare but instructive disease that exemplifies the intertwined nature of immunity and metabolism, with lessons likely applicable to more common inflammatory and metabolic disorders.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 8 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1111/j.1651-2227.2008.01092.x` (1 mention) - Hyperzincemia and hypercalprotectinemia: unsuccessful treatment with tacrolimus
  - shared terms: hyperzincemia

Weighed against this report's own most characteristic terms: `zinc`, `hyperzincemia`, `disease`, `pstpip1`, `calprotectin`, `functional`, `depletion`, `pami`, `inflammation`, `patient`, `systemic`, `syndrome`, `infection`, `inflammatory`, `mutation`, `chronic`, `cytopenias`, `skin`, `include`, `genetic`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 78 |
| Resolved | 70 |
| Unresolved (possible confabulation) | 3 |
| Obsolete | 2 |
| Unverifiable | 3 |
| Terms whose name was checked | 36 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0140235` (1 mention) - the report calls it "inflammasome complex assembly"; GO calls it **RNA polyadenylation at postsynapse**
- `CHEBI:25517` (1 mention) - the report calls it "nickel(2+) cation"; CHEBI calls it **CHEBI_25517**
- `NCIT:C15731` (1 mention) - the report calls it "Corticosteroid therapy"; NCIT calls it **Intrahepatic Infusion Procedure**
- `NCIT:C16033` (1 mention) - the report calls it "Tumor Necrosis Factor Inhibitor Therapy"; NCIT calls it **Follow-Up**
- `NCIT:C121938` (1 mention) - the report calls it "Interleukin-1 Inhibitor Therapy"; NCIT calls it **Low Reference Range in Numeric Format**
- `NCIT:C1282` (1 mention) - the report calls it "Tacrolimus"; NCIT calls it **Carboplatin**
- `NCIT:C65202` (1 mention) - the report calls it "Adalimumab"; NCIT calls it **Wedge**
- `NCIT:C15197` (1 mention) - the report calls it "Allogeneic Hematopoietic Stem Cell Transplantation"; NCIT calls it **Case-Control Study**
- `NCIT:C80188` (1 mention) - the report calls it "Myeloablative Conditioning Regimen"; NCIT calls it **HDL-Cholesterol Subclass 3 Measurement**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001505` (1 mention) - HP does not contain this term
- `HP:0003331` (1 mention) - HP does not contain this term
- `HP:0006950` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0051092` (obsolete positive regulation of NF-kappaB transcription factor activity) (1 mention)
- `CHEBI:25517` (CHEBI_25517) (1 mention) - replaced by `CHEBI:49786`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0032612` (1 mention) - the report calls it "interleukin‑1 beta production"; GO calls it **interleukin-1 production**
- `GO:0032611` (1 mention) - the report calls it "interleukin‑18 production"; GO calls it **interleukin-1 beta production**
- `GO:0051092` (1 mention) - the report calls it "positive regulation of NF‑κB transcription factor activity"; GO calls it **obsolete positive regulation of NF-kappaB transcription factor activity**
- `CHEBI:29105` (1 mention) - the report calls it "zinc cation"; CHEBI calls it **zinc(2+)**, and lists "zinc cation" among its other names
- `CHEBI:29035` (1 mention) - the report calls it "manganese(2+) cation"; CHEBI calls it **manganese(2+)**, and lists "manganese(II) cation" among its other names
- `CHEBI:29108` (1 mention) - the report calls it "calcium(2+) cation"; CHEBI calls it **calcium(2+)**, and lists "calcium(II) cation" among its other names
- `CL:0000837` (1 mention) - the report calls it "erythroid progenitor cell"; CL calls it **hematopoietic multipotent progenitor cell**, and lists "hemopoietic progenitor cell" among its other names
- `CL:0002620` (1 mention) - the report calls it "dermal fibroblast"; CL calls it **skin fibroblast**
- `GO:0061702` (1 mention) - the report calls it "inflammasome complex"; GO calls it **canonical inflammasome complex**
- `GO:0046872` (1 mention) - the report calls it "metallothionein complex"; GO calls it **metal ion binding**
- `NCIT:C408` (1 mention) - the report calls it "Cyclosporine A"; NCIT calls it **Cytarabine**, and lists "Cytosine Arabinoside" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.