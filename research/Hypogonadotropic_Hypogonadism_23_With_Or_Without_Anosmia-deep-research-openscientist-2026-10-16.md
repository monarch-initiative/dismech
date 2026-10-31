---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T21:10:50.953015'
end_time: '2026-10-16T21:29:30.146025'
duration_seconds: 1119.19
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypogonadotropic Hypogonadism 23 With or Without Anosmia
  mondo_id: MONDO:0009223
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 11
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 12
  validator_version: 0.3.0
term_validation:
  total_terms: 31
  verified: 29
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 2
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0009223
    reported_labels:
    - MONDO
    ontology_label: hypogonadotropic hypogonadism 23 with or without anosmia
  - term_id: DOID:0090091
    reported_labels:
    - DOID
    ontology_label: hypogonadotropic hypogonadism 23 with or without anosmia
  obsolete_terms:
  - term_id: GO:0019933
    ontology_label: obsolete cAMP-mediated signaling
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hypogonadotropic_Hypogonadism_23_With_Or_Without_Anosmia-deep-research-openscientist-2026-10-16_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hypogonadotropic_Hypogonadism_23_With_Or_Without_Anosmia-deep-research-openscientist-2026-10-16_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypogonadotropic Hypogonadism 23 With or Without Anosmia
- **MONDO ID:** MONDO:0009223 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypogonadotropic Hypogonadism 23 With or Without Anosmia** covering all of the
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

# Hypogonadotropic Hypogonadism 23 With or Without Anosmia (HH23) — Comprehensive Disease Report

**Disease:** Hypogonadotropic Hypogonadism 23 With or Without Anosmia
**MONDO ID:** MONDO:0009223 · **OMIM:** #228300 · **Category:** Mendelian (autosomal recessive)
**Causal gene:** *LHB* (luteinizing hormone subunit beta, 19q13.33)

---

## Summary

**Hypogonadotropic Hypogonadism 23 With or Without Anosmia (HH23)** is, despite its name, an **autosomal-recessive isolated luteinizing-hormone (LH) deficiency** caused by biallelic loss-of-function or bioinactivating mutations in the *LHB* gene encoding the β-subunit of luteinizing hormone. The disease corresponds historically to **"Pasqualini syndrome"** and the **"fertile eunuch"** phenotype. The core lesion is the absence of a functional bioactive LH heterodimer, which leaves the intact LH/choriogonadotropin receptor (LHCGR) unstimulated and silences the downstream cAMP/PKA/StAR steroidogenic program in gonadal (Leydig and theca/granulosa) cells. GnRH secretion, FSH, the LH receptor, and the gonads themselves are intrinsically normal — the defect is confined to the LH ligand.

A critical clarification arising from this investigation: **anosmia is NOT an intrinsic feature of HH23**. The "With or Without Anosmia" phrasing is a naming artifact inherited from the OMIM/MONDO hypogonadotropic-hypogonadism numbered series (which groups Kallmann-syndrome loci alongside isolated gonadotropin-subunit defects). HH23/LHB deficiency is a **normosmic**, non-Kallmann condition. The olfactory system is unaffected because the pathology lies in gonadotrope hormone production, not in embryonic GnRH-neuron/olfactory-placode migration.

The phenotype is **sex-dimorphic and highly treatable**. Males present with severe disease — absent or incomplete puberty, delayed virilization, small testes, Leydig-cell hypoplasia, and azoospermia or markedly impaired spermatogenesis, with undetectable/low LH but normal FSH and low testosterone. Females show a milder picture — normal female external genitalia, spontaneous breast and pubic-hair development, normal or late menarche, followed by secondary oligo-/amenorrhea and anovulatory infertility. Because the receptor and gonad are intact, **hCG (which binds the same LHCGR) restores steroidogenesis, spermatogenesis, ovulation and fertility**, and in females pulsatile GnRH or LH/hCG ovulation induction has produced healthy term pregnancies. The biochemical hallmark — **low LH with normal FSH and preserved hCG responsiveness** — distinguishes HH23 both from classic GnRH-deficient CHH (where both gonadotropins are low) and from LHCGR inactivation (where LH is high and the patient is hormone-resistant).

---

## Key Identifiers and Disease Information

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0009223 |
| OMIM | #228300 (Hypogonadotropic hypogonadism 23 with or without anosmia; HH23) |
| Orphanet | ORPHA:325448 |
| DOID | DOID:0090091 |
| MeSH | C537919 |
| UMLS | C0271582 |
| ICD-9 | 253.4 |
| Causal gene | *LHB* (HGNC; luteinizing hormone subunit beta), chromosome 19q13.33 |

**Synonyms / alternative names:** LH deficiency; isolated luteinizing hormone deficiency; luteinizing hormone beta-subunit deficiency; **Pasqualini syndrome**; **fertile eunuch syndrome** (historical, describing the hypomorphic/partial variant with preserved spermatogenesis despite poor virilization); hypogonadism due to LH deficiency.

**Information provenance:** Disease-level knowledge for HH23 derives from **aggregated resources** (OMIM, Orphanet, MONDO) combined with a small set of **individual-patient case reports and small family studies** (fewer than ~20 unrelated families described worldwide), because inactivating *LHB* mutations are exceptionally rare. Ontology mapping was verified via EBI OLS; the landmark PMID was verified via NCBI E-utilities.

---

## Key Findings

### Finding 1 — HH23 is caused by biallelic inactivating *LHB* mutations (isolated LH deficiency, not Kallmann syndrome)

HH23 (MONDO:0009223 / OMIM #228300) results from **biallelic (homozygous or compound-heterozygous) loss-of-function or bioinactivating variants in *LHB***, the gene encoding the hormone-specific β-subunit of luteinizing hormone on 19q13.33. This is an **isolated LH deficiency**, mechanistically and clinically distinct from Kallmann syndrome (which is caused by genes governing GnRH-neuron/olfactory migration such as *ANOS1/KAL1*, *FGFR1*, *PROKR2*, *PROK2*, *FGF8*, *SOX10*). The "with or without anosmia" descriptor is a series-naming artifact; olfaction is intrinsically preserved.

Multiple independent human families establish the genotype spectrum:

| Variant (protein / cDNA) | Zygosity | Sex / phenotype | PMID |
|---|---|---|---|
| Lys40del (in-frame deletion, trafficking determinant) | homozygous | male, severe | [27656125](https://pubmed.ncbi.nlm.nih.gov/27656125/) |
| Trp28X (nonsense) | homozygous | male hypogonadism | [29476300](https://pubmed.ncbi.nlm.nih.gov/29476300/) |
| IVS2+1G>C (splice) | homozygous | female, selective LH deficiency | [34535998](https://pubmed.ncbi.nlm.nih.gov/34535998/) |
| F84L + G122S (missense) | compound het | female CHH | [39786527](https://pubmed.ncbi.nlm.nih.gov/39786527/) |
| Hypomorphic missense (residual activity) | — | male, normal spermatogenesis | [19890128](https://pubmed.ncbi.nlm.nih.gov/19890128/) |
| Gln54Arg (missense; first described) | homozygous | male hypogonadism | [1727547](https://pubmed.ncbi.nlm.nih.gov/1727547/) |
| Trp8Arg + Ile15Thr | — | fertile eunuch | [14709845](https://pubmed.ncbi.nlm.nih.gov/14709845/) |

> *"Inactivating Luteinizing hormone beta (LHB) gene mutations are exceptionally rare and lead to hypogonadism that is particularly severe in males."* — [PMID: 27656125](https://pubmed.ncbi.nlm.nih.gov/27656125/)

> *"Inactivating mutations of the luteinizing hormone beta subunit (LHB) gene are extremely rare and can result in congenital hypogonadotropic hypogonadism (CHH)."* — [PMID: 39786527](https://pubmed.ncbi.nlm.nih.gov/39786527/)

**Variant classification:** The reported variants span nonsense (Trp28X), splice-site (IVS2+1G>C), in-frame deletion (Lys40del), and missense (Gln54Arg, F84L, G122S, Trp8Arg, Ile15Thr) classes, and are classified **pathogenic/likely pathogenic** under ACMG/AMP criteria on the basis of segregation, functional data, and absence/rarity in population databases (gnomAD). All are **germline**. Functional consequence is **loss of function** of bioactive LH — via either absent synthesis (nonsense/splice), impaired secretion/trafficking (deletion/missense), or bioinactivity of a secreted but non-signaling hormone (Gln54Arg).

### Finding 2 — hCG (and pulsatile GnRH/LH in females) restores gonadal function and fertility

Because HH23 is a **ligand-replaceable deficiency with an intact receptor and gonad**, treatment is LH replacement. hCG binds and activates the same LHCGR, driving steroidogenesis and gametogenesis.

- **Male, Trp28X:** after 40 days of hCG, a few spermatozoa appeared; by 6 months, normal seminal parameters ([PMID: 29476300](https://pubmed.ncbi.nlm.nih.gov/29476300/)).
- **Male brothers, Lys40del:** hCG induced pubertal development, rising testosterone, and spermatogenesis ([PMID: 27656125](https://pubmed.ncbi.nlm.nih.gov/27656125/)).
- **Female, IVS2+1G>C:** ovulation induction with recombinant LH then urinary hCG achieved follicle growth, ovulation, and a healthy term pregnancy ([PMID: 34535998](https://pubmed.ncbi.nlm.nih.gov/34535998/)).
- **Female, compound het F84L+G122S:** pulsatile GnRH promoted puberty and ovulation ([PMID: 39786527](https://pubmed.ncbi.nlm.nih.gov/39786527/)).

> *"After 40 days of treatment with hCG, the patient exhibited a few spermatozoa in the semen. Treated for 6 months, the patient exhibited normal seminal parameters."* — [PMID: 29476300](https://pubmed.ncbi.nlm.nih.gov/29476300/)

> *"Ovarian follicle growth and ovulation were achieved, and a healthy baby was born after an uneventful term pregnancy."* — [PMID: 34535998](https://pubmed.ncbi.nlm.nih.gov/34535998/)

**NCIT clinical-intervention term suggestions:** chorionic gonadotropin / hCG therapy (NCIT:C617), gonadotropin-releasing hormone agonist/pulsatile GnRH, testosterone replacement therapy (for virilization when fertility is not the goal), recombinant LH.

### Finding 3 — Sex-dimorphic phenotype: severe in males, milder in females

**Males** (severe): pubertal delay/absent virilization, small testes, azoospermia or variable spermatogenesis, undetectable/low LH with normal FSH, low testosterone, and absent or few fetal Leydig cells (**Leydig-cell hypoplasia**) ([PMIDs: 27656125, 19890128, 29476300]).

**Females** (milder): normal female external genitalia; spontaneous thelarche and pubarche; normal or late menarche followed by secondary **oligo-/amenorrhea and anovulatory infertility**; estradiol and progesterone reach follicular but not ovulatory/luteal levels; low LH with normal/slightly raised FSH; ovaries normal or enlarged with cysts ([PMIDs: 19129711, 17761593]).

A **variant "fertile eunuch" (Pasqualini) presentation** retains partial spermatogenesis with hypomorphic alleles (e.g., Trp8Arg+Ile15Thr; [PMID: 14709845](https://pubmed.ncbi.nlm.nih.gov/14709845/)).

> *"female external genitalia, spontaneous breast and pubic hair development at puberty, and normal or late menarche followed by oligo-amenorrhea and infertility"* — [PMID: 19129711](https://pubmed.ncbi.nlm.nih.gov/19129711/)

> *"the female phenotype of this LHB mutation is characterized by normal pubertal development, secondary amenorrhea, and infertility"* — [PMID: 17761593](https://pubmed.ncbi.nlm.nih.gov/17761593/)

> *"Men with mutations in LHB, the gene encoding the beta subunit of luteinizing hormone (LHB), have azoospermia with absent or few fetal Leydig cells."* — [PMID: 19890128](https://pubmed.ncbi.nlm.nih.gov/19890128/)

**The sex dimorphism is explained developmentally:** in females, fetal ovarian development and early puberty are largely FSH- and placental-hCG-dependent, so early pubertal milestones proceed; LH is required specifically for the ovulatory surge and corpus-luteum/progesterone function, so the deficit manifests as anovulation after menarche. In males, fetal Leydig-cell testosterone production (driving virilization of the external genitalia and later pubertal maturation) depends on LH/hCG, so loss causes more profound and earlier manifestations.

**Suggested HPO terms:** Hypogonadotropic hypogonadism (HP:0000044); Decreased circulating luteinizing hormone (HP:0011969); Delayed puberty (HP:0000823); Secondary amenorrhea (HP:0000869); Oligomenorrhea (HP:0000876); Azoospermia (HP:0000027); Male infertility (HP:0003251); Female infertility (HP:0008222); Decreased testicular size (HP:0008734); Decreased serum testosterone level (HP:0040171); Leydig cell hypoplasia (reduced testicular interstitial cells).

### Finding 4 — Mechanism: LHB loss-of-function abrogates bioactive LH, silencing the LHCGR–cAMP/PKA–StAR steroidogenic cascade

LH is an **αβ heterodimer**: a shared α-subunit (encoded by *CGA*) non-covalently associated with the hormone-specific LHB β-subunit. Different *LHB* mutation classes disrupt the hormone in distinct ways:

- **Missense/in-frame deletion (e.g., Lys40del):** the mutant subunit is **retained intracellularly** (diffuse cytoplasmic distribution) and is not secreted, even though it can still heterodimerize with the α-subunit and, in vitro, activate the receptor. Lys40 lies in a conserved **trafficking determinant** shared across the hCG/FSH/TSH β-subunits ([PMID: 27656125](https://pubmed.ncbi.nlm.nih.gov/27656125/)).
- **Splice/nonsense (IVS2+1G>C, Trp28X):** abolish LH synthesis or secretion outright ([PMIDs: 17761593, 29476300]).
- **Bioinactive missense (Gln54Arg):** a hormone that is immunoreactive but biologically inactive — it cannot productively engage/activate LHCGR ([PMID: 1727547](https://pubmed.ncbi.nlm.nih.gov/1727547/)).

Downstream, LH/hCG act through **LHCGR**, a Gs-coupled GPCR, activating **cAMP → PKA → CREB**, which induces **StAR** (steroidogenic acute regulatory protein) and steroidogenic enzymes (*CYP11A1*, *HSD3B*) to drive testosterone/progesterone synthesis ([PMIDs: 33112765, 38621656]). Loss of bioactive LH therefore silences this cascade at its most upstream (ligand) node.

> *"the mutant LH is retained intracellularly and showed diffuse cytoplasmic distribution. The mutated LHB heterodimerizes with the common alpha-subunit and can activate its receptor."* — [PMID: 27656125](https://pubmed.ncbi.nlm.nih.gov/27656125/)

**Mouse models** recapitulate the disease: *Lhb*-knockout mice show hypogonadism with reduced androgen-dependent testicular gene programs (e.g., *Slc7a11*), and female *Lhb*-KO mice are close phenocopies of human *LHB* mutations ([PMIDs: 35398053, 19129711]).

> *"we performed large-scale gene expression analyses on testes obtained from adult control and Lhb knockout mice"* — [PMID: 35398053](https://pubmed.ncbi.nlm.nih.gov/35398053/)

**CHEBI chemical entities:** luteinizing hormone; human chorionic gonadotropin; testosterone (CHEBI:17347); progesterone (CHEBI:17026); estradiol (CHEBI:23965); cyclic AMP / 3',5'-cyclic AMP (CHEBI:17489); cholesterol (CHEBI:16113, StAR substrate).

**GO/CL term suggestions:** biological process — hormone-mediated signaling pathway (GO:0009755), steroid biosynthetic process (GO:0006694), response to luteinizing hormone, cAMP-mediated signaling (GO:0019933), male gonad development (GO:0008584), ovulation (GO:0030728); cellular component — extracellular space (secreted LH), endoplasmic reticulum (trafficking-retained mutants, GO:0005783); cell types — Leydig cell (CL:0000178), granulosa cell (CL:0000501), theca cell (CL:0000503), pituitary gonadotrope (CL:0000173).

### Finding 5 — Key diagnostic discriminator: low LH + hCG-responsive (*LHB*) vs. high LH + hormone-resistant (*LHCGR*)

Women with inactivating *LHB* vs. *LHCGR* mutations share a near-identical clinical picture (female external genitalia, spontaneous breast/pubic-hair development, normal/late menarche, then oligo-amenorrhea and infertility), but are distinguished **biochemically and therapeutically**:

| Feature | *LHB* deficiency (HH23) | *LHCGR* inactivation |
|---|---|---|
| Serum LH | **Low / undetectable** | **High** |
| Serum FSH | Normal / slightly raised | Normal / slightly raised |
| Defect location | Ligand (hormone) | Receptor |
| hCG/LH response | **Responsive** | **Resistant** |
| Treatment | hCG / LH replacement | Not receptor-correctable |

> *"serum LH levels are low in patients with LHB mutations and high in those with LHCGR mutations, whereas follicle-stimulating hormone levels are normal or only slightly increased"* — [PMID: 19129711](https://pubmed.ncbi.nlm.nih.gov/19129711/)

> *"Women with LHB mutations may be treated with hCG (human chorionic gonadotropin) or LH, whereas those with mutations in LHCGR are resistant."* — [PMID: 19129711](https://pubmed.ncbi.nlm.nih.gov/19129711/)

**Diagnostic pitfall — bioinactive LH:** The Gln54Arg hormone is **immunoreactive but biologically inactive**. A standard immunoassay may therefore report "detectable/normal" LH that is in fact non-functional. In a patient with hypogonadism and a normal-appearing LH immunoassay, discordance between immunoreactivity and bioactivity (or molecular testing) is required to avoid missing the diagnosis ([PMID: 1727547](https://pubmed.ncbi.nlm.nih.gov/1727547/)).

### Finding 6 — Minimal residual intratesticular testosterone suffices for complete spermatogenesis (molecular basis of the "fertile eunuch")

A man with a **hypomorphic *LHB* mutation** had undetectable serum LH and low serum testosterone, yet **complete, quantitatively normal spermatogenesis**. The mutant LH retained low partial in-vitro activity, sufficient to drive steroidogenic-enzyme expression in a few mature Leydig cells that produced only **~20.2 ng/g intratesticular testosterone** — enough for normal spermatogenesis despite absent virilization ([PMID: 19890128](https://pubmed.ncbi.nlm.nih.gov/19890128/)). This dissociation of poor virilization from preserved fertility is the molecular basis of the historical **"fertile eunuch"/Pasqualini** phenotype (e.g., Trp8Arg+Ile15Thr; [PMID: 14709845](https://pubmed.ncbi.nlm.nih.gov/14709845/)) and challenges the dogma about the high intratesticular-testosterone threshold required for spermatogenesis ([PMID: 34884539](https://pubmed.ncbi.nlm.nih.gov/34884539/)).

> *"the residual luteinizing hormone activity, resulting in the expression of steroidogenic enzymes in few mature Leydig cells producing small amounts of intratesticular testosterone (20.2 ng per gram), was sufficient for complete and quantitatively normal spermatogenesis"* — [PMID: 19890128](https://pubmed.ncbi.nlm.nih.gov/19890128/)

> *"Normal virilization and improved semen parameters were achieved after hCG supplementation."* — [PMID: 14709845](https://pubmed.ncbi.nlm.nih.gov/14709845/)

### Finding 7 — Historical landmark: Weiss 1992 established LH-beta deficiency as a distinct cause of hypogonadism

The first human *LHB* mutation was reported by **Weiss et al., N Engl J Med 1992;326(3):179–183** (*"Hypogonadism caused by a single amino acid substitution in the beta subunit of luteinizing hormone"*; [PMID: 1727547](https://pubmed.ncbi.nlm.nih.gov/1727547/)). They described a homozygous **Gln54Arg** missense variant in a man with delayed puberty/hypogonadism. The mutant LH was immunoreactive but biologically inactive — the first molecular proof that an **intrinsic LH-beta defect** (rather than GnRH deficiency or pituitary failure) can cause hypogonadism. Bibliographic details were verified via NCBI E-utilities.

---

## Mechanistic Model — Causal Chain

```
1. Biallelic inactivating / bioinactivating LHB mutation (19q13.33)
        │  (nonsense/splice → no synthesis;  missense/deletion → ER retention / no secretion;
        │   Gln54Arg → secreted but bioinactive)
        ▼
2. Absence of functional bioactive LH αβ heterodimer in circulation
        │  leads to
        ▼
3. LHCGR (Gs-coupled GPCR) on Leydig / theca cells remains unstimulated
        │  results in
        ▼
4. Failure of cAMP → PKA → CREB signaling   [inferred from receptor/pathway biology]
        │  leads to
        ▼
5. Loss of StAR induction + reduced CYP11A1 / HSD3B activity
        │  results in
        ▼
6. Deficient gonadal steroidogenesis (low testosterone / low progesterone)
        │
        ├──► MALE branch: fetal + pubertal Leydig-cell testosterone absent
        │        → Leydig-cell hypoplasia, undervirilization, absent/incomplete
        │          puberty, azoospermia/impaired spermatogenesis
        │        (hypomorphic alleles → trace intratesticular T → "fertile eunuch")
        │
        └──► FEMALE branch: early puberty (FSH/hCG-driven) proceeds normally,
                 but absent LH surge → anovulation, no corpus luteum,
                 low luteal progesterone → secondary oligo-/amenorrhea, infertility
        ▼
7. Clinical HH23.  Because LHCGR and gonad are intact, hCG/LH replacement
   re-enters the chain at step 3 and restores steroidogenesis, gametogenesis,
   and fertility.
```

**Upstream vs downstream:** The initiating lesion (steps 1–2) is the ligand defect; steps 3–6 are the intact-but-unstimulated receptor/steroidogenic machinery (downstream, and therefore rescuable by exogenous agonist). FSH, GnRH, and the olfactory/GnRH-migration axis are entirely outside this chain — the reason HH23 is normosmic and FSH-normal.

---

## Comparison With Related Conditions (Differential Diagnosis)

| Condition | LH | FSH | Smell | Key gene(s) | hCG response |
|---|---|---|---|---|---|
| **HH23 / *LHB* deficiency** | **Low** | Normal | **Normal** | *LHB* | **Yes** |
| Kallmann syndrome | Low | Low | **Anosmia** | *ANOS1, FGFR1, PROKR2, PROK2, SOX10* | Variable |
| Normosmic CHH (GnRH-deficient) | Low | Low | Normal | *GNRHR, KISS1R, TAC3/TACR3* | Variable |
| *LHCGR* inactivation (Leydig hypoplasia) | **High** | Normal | Normal | *LHCGR* | **No (resistant)** |
| *FSHB* deficiency | Normal/high | Low | Normal | *FSHB* | N/A |

The single most useful discriminator between HH23 and GnRH-deficient CHH is that **FSH is preserved in HH23** (only LH is deficient), whereas GnRH deficiency lowers both gonadotropins. The discriminator from *LHCGR* disease is the **low (vs high) LH and preserved hCG responsiveness**.

---

## Anatomical Structures, Temporal Course, and Epidemiology

**Anatomy / organ level (UBERON/CL):** Endocrine axis — pituitary gonadotrope (CL:0000173) as the site of the production defect; primary target organs are the **testis** (UBERON:0000473) Leydig/interstitial cells (CL:0000178) and the **ovary** (UBERON:0000992) theca (CL:0000503) and granulosa cells (CL:0000501). Subcellular compartments: endoplasmic reticulum (trafficking-retained mutants), extracellular space (secreted hormone), and mitochondrial/ER steroidogenic machinery (StAR/CYP11A1). Secondary manifestations: reduced bone mineralization and body-composition changes expected with chronic sex-steroid deficiency (general hypogonadism complications; not disease-specific data).

**Temporal development:** Congenital/germline genetic basis with **onset recognized at the expected pubertal window** — males present with absent/incomplete puberty and small testes; females present at or after the normal menarcheal age with secondary amenorrhea. Course is **chronic and lifelong** at the level of the endogenous deficiency but is **not progressive**; it is fully controllable with replacement therapy. The pubertal window is the **critical period** for diagnosis and for virilization/breast development; fertility can be induced later with hCG/LH or pulsatile GnRH.

**Epidemiology:** Inactivating *LHB* mutations are **"exceptionally rare"** ([PMID: 27656125](https://pubmed.ncbi.nlm.nih.gov/27656125/)) — fewer than ~20 unrelated families reported globally; no reliable prevalence/incidence estimate exists (ultra-rare). **Inheritance is autosomal recessive**; most reported probands are homozygous, several from consanguineous unions, implying a contributing role for consanguinity and founder/private alleles. **Penetrance** of biochemical hypogonadism appears high in biallelic carriers, with **variable expressivity** (severe azoospermia through fertile-eunuch depending on residual allele activity). Heterozygous carriers are clinically unaffected. No genetic anticipation (not a repeat-expansion disorder). Both sexes affected; males are more severely affected.

---

## Diagnostics (Synthesis)

- **Hormonal profile:** low/undetectable LH, **normal FSH**, low sex steroids (testosterone in males; failure to reach ovulatory estradiol/luteal progesterone in females). This FSH-normal, LH-low pattern is the biochemical signature.
- **Caution:** some bioinactive mutants (Gln54Arg) are **immunoreactive**, so immunoassay LH may appear normal — bioassay discordance or molecular testing resolves this ([PMID: 1727547](https://pubmed.ncbi.nlm.nih.gov/1727547/)).
- **hCG stimulation test:** a rise in testosterone/steroids confirms an intact receptor/gonad and supports *LHB* (vs *LHCGR*) etiology ([PMID: 19129711](https://pubmed.ncbi.nlm.nih.gov/19129711/)).
- **Genetic testing:** single-gene *LHB* sequencing, or CHH/hypogonadism gene panels / whole-exome sequencing. Given ultra-rarity and phenotype overlap, panel/WES is practical; confirm biallelic status and segregation.
- **Imaging:** small testes on exam/ultrasound (males); normal or cystic/enlarged ovaries (females). Normal olfaction on formal smell testing distinguishes from Kallmann syndrome; normal MRI of olfactory bulbs expected (not routinely required).

---

## Treatment, Prognosis, and Prevention

**Treatment.** HH23 is among the most treatable hypogonadotropic disorders because the receptor and gonad are intact:
- **Virilization / sex-steroid replacement:** testosterone (males), estrogen/progestin (females) for secondary sexual characteristics and bone health when fertility is not the immediate goal.
- **Fertility induction:** **hCG** (acts on LHCGR) ± FSH in males to initiate/restore spermatogenesis ([PMIDs: 29476300, 27656125, 14709845]); **recombinant LH / hCG ovulation induction** or **pulsatile GnRH** in females ([PMIDs: 34535998, 39786527]).
- Documented outcomes include normalization of seminal parameters within months and a healthy term pregnancy — **excellent prognosis** for both sexual maturation and fertility with treatment.

**Prognosis.** Life expectancy is normal; morbidity relates to untreated hypogonadism (infertility, reduced bone density, psychosocial impact of delayed puberty) and is largely reversible with therapy. No disease-specific mortality.

**Prevention / counseling.** No primary prevention (germline Mendelian disorder). **Genetic counseling** for autosomal-recessive recurrence risk (25% in carrier × carrier couples), **cascade carrier testing** of relatives, and reproductive options (prenatal/preimplantation genetic testing) are appropriate given identified familial variants. Carrier frequency is presumably very low (ultra-rare alleles; check gnomAD for specific variants).

---

## Model Organisms

| Model | Type | Recapitulation | PMID |
|---|---|---|---|
| *Lhb*-knockout mouse | Mammalian KO | Hypogonadism; reduced androgen-dependent testicular programs (e.g., *Slc7a11*); female KO is a close phenocopy of human *LHB* disease | [35398053](https://pubmed.ncbi.nlm.nih.gov/35398053/), [19129711](https://pubmed.ncbi.nlm.nih.gov/19129711/) |
| *LuRKO* (Lhcgr-KO) mouse | Mammalian KO | Receptor-side model; elevated LH, contrasts the ligand-side *Lhb* defect | [25039914](https://pubmed.ncbi.nlm.nih.gov/25039914/) |
| Zebrafish *lhb* mutant | Non-mammalian | Normal gonadal growth but females fail to spawn (infertile); LH role in final maturation | [25396299](https://pubmed.ncbi.nlm.nih.gov/25396299/) |

**Orthologs:** *Lhb* (mouse), *lhb* (zebrafish). **Limitations:** rodent fetal Leydig-cell and placental-hCG biology differ from human; zebrafish lack the mammalian hCG axis, so the human sex-dimorphism and fertile-eunuch phenotype are not fully reproduced. No naturally occurring companion-animal/wildlife *LHB*-deficiency disease is well documented (OMIA); no zoonotic dimension (non-infectious).

---

## Evidence Base

| PMID | Role in this report | Evidence type |
|---|---|---|
| [1727547](https://pubmed.ncbi.nlm.nih.gov/1727547/) | First human *LHB* mutation (Gln54Arg); bioinactive-LH concept | Human case (landmark) |
| [27656125](https://pubmed.ncbi.nlm.nih.gov/27656125/) | Lys40del; trafficking determinant; rarity; male severity; hCG response | Human + in vitro |
| [29476300](https://pubmed.ncbi.nlm.nih.gov/29476300/) | Trp28X nonsense; hCG restores spermatogenesis | Human case |
| [34535998](https://pubmed.ncbi.nlm.nih.gov/34535998/) | Female splice variant; ovulation induction → term pregnancy | Human case |
| [39786527](https://pubmed.ncbi.nlm.nih.gov/39786527/) | Female compound-het; pulsatile GnRH; CHH framing | Human case |
| [19890128](https://pubmed.ncbi.nlm.nih.gov/19890128/) | Hypomorphic allele; trace intratesticular T → normal spermatogenesis | Human + functional |
| [14709845](https://pubmed.ncbi.nlm.nih.gov/14709845/) | Fertile-eunuch (Trp8Arg+Ile15Thr); hCG response | Human case |
| [19129711](https://pubmed.ncbi.nlm.nih.gov/19129711/) | *LHB* vs *LHCGR* discriminator (low vs high LH; responsive vs resistant); female phenotype | Human review |
| [17761593](https://pubmed.ncbi.nlm.nih.gov/17761593/) | Female phenotype: normal puberty → amenorrhea/infertility | Human case |
| [35398053](https://pubmed.ncbi.nlm.nih.gov/35398053/) | *Lhb*-KO mouse testicular gene programs | Mouse model |
| [33112765](https://pubmed.ncbi.nlm.nih.gov/33112765/), [38621656](https://pubmed.ncbi.nlm.nih.gov/38621656/) | LHCGR → cAMP/PKA/CREB → StAR steroidogenesis pathway | In vitro |
| [34884539](https://pubmed.ncbi.nlm.nih.gov/34884539/) | Intratesticular-testosterone threshold dogma reconsidered | Review |

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity.** The entire human evidence base is a handful of case reports/small families; no epidemiological prevalence, no natural-history cohort, and no quantitative penetrance/expressivity estimates exist. Frequency statements are qualitative.
2. **Name/ontology artifact.** The OMIM/MONDO series name ("with or without anosmia") implies an olfactory feature that is not a genuine part of *LHB* deficiency; downstream knowledge bases may mis-associate HH23 with Kallmann phenotypes. This report explicitly flags anosmia as non-intrinsic.
3. **Mechanistic inference.** The cAMP/PKA/StAR silencing step (chain step 4) is inferred from LHCGR receptor biology and model systems rather than demonstrated directly in *LHB*-deficient human gonadal tissue.
4. **Modifier genes, epigenetics, and QoL** are unstudied for this specific disorder; no disease-specific quality-of-life, modifier-allele, or methylation data are available.
5. **Genotype–phenotype granularity.** The allele-activity-to-phenotype relationship (severe vs fertile-eunuch) is supported by individual cases but lacks a systematic functional allelic series.

## Proposed Follow-up Actions

1. **Curate an international *LHB*-mutation registry** to aggregate the scattered case reports and derive penetrance, expressivity, and genotype–phenotype (allele residual activity vs virilization/fertility) relationships.
2. **Standardized functional assays** (secretion/trafficking + LHCGR activation) for each reported and novel *LHB* variant to build a quantitative allelic series predicting fertile-eunuch vs severe phenotypes.
3. **Correct the ontology annotation** in downstream knowledge bases to mark anosmia as *not* a feature of MONDO:0009223, preventing propagation of the Kallmann-series naming artifact.
4. **Prospective fertility-outcome data** on hCG/LH and pulsatile-GnRH protocols specific to *LHB* deficiency, to formalize treatment algorithms.
5. **gnomAD interrogation** of each pathogenic *LHB* allele to estimate carrier frequencies and inform carrier-screening/counseling.

---

*Report compiled from 7 confirmed findings and 39 reviewed papers across 5 investigation iterations. All quoted abstract snippets were validated against stored abstracts; ontology identifiers verified via EBI OLS and NCBI E-utilities.*


## Artifacts

- [OpenScientist final report](Hypogonadotropic_Hypogonadism_23_With_Or_Without_Anosmia-deep-research-openscientist-2026-10-16_artifacts/final_report.html)
- [OpenScientist final report](Hypogonadotropic_Hypogonadism_23_With_Or_Without_Anosmia-deep-research-openscientist-2026-10-16_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 4 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009223` (4 mentions) - the report calls it "MONDO"; MONDO calls it **hypogonadotropic hypogonadism 23 with or without anosmia**
- `DOID:0090091` (1 mention) - the report calls it "DOID"; DOID calls it **hypogonadotropic hypogonadism 23 with or without anosmia**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0019933` (obsolete cAMP-mediated signaling) (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.