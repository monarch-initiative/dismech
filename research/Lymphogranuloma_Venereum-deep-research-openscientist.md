---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-24T23:00:00.758798'
end_time: '2026-09-24T23:18:48.812693'
duration_seconds: 1128.06
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Lymphogranuloma Venereum
  mondo_id: MONDO:0005834
  category: Infectious Disease
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
citation_count: 23
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 23
  on_topic: 10
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 25
  verified: 23
  not_found: 0
  obsolete: 2
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 24
  labels_matching: 17
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0005834
    reported_labels:
    - MONDO
    ontology_label: lymphogranuloma venereum
  - term_id: HP:0200037
    reported_labels:
    - Genital ulceration
    ontology_label: Skin vesicle
  - term_id: HP:0002607
    reported_labels:
    - rectal
    ontology_label: Bowel incontinence
  - term_id: GO:0030260
    reported_labels:
    - entry into host cell
    ontology_label: GO_0030260
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0009405
    ontology_label: obsolete pathogenesis
  - term_id: GO:0030260
    ontology_label: GO_0030260
    replaced_by: GO:0044409
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Lymphogranuloma_Venereum-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Lymphogranuloma_Venereum-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lymphogranuloma Venereum
- **MONDO ID:** MONDO:0005834 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Lymphogranuloma Venereum** covering all of the
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

# Lymphogranuloma Venereum (MONDO:0005834): A Comprehensive Disease Characteristics Report

**Target disease:** Lymphogranuloma Venereum · **MONDO:0005834** · Category: Infectious Disease
**Report type:** Disease-level synthesis from primary literature and clinical guidelines (no patient-level data files were provided; all evidence is aggregated/literature-derived).
**Date:** 2026-09-25

## Summary

**Lymphogranuloma venereum (LGV)** is an invasive, systemic sexually transmitted infection caused by the **L-biovar of *Chlamydia trachomatis*** (serovars L1, L2, L2b, and L3). Unlike the non-invasive "trachoma" biovar that causes ocular and uncomplicated urogenital chlamydial infection, the LGV strains are lymphotropic and macrophage-tropic, enabling them to disseminate from the mucosal inoculation site into the regional lymphatics. This distinction — genomic and biological rather than genetic-in-the-host — is the central determinant of the disease. LGV is **not a human Mendelian disease**; there are no causal human genes, pathogenic germline variants, or heritable susceptibility loci. The "genotype" that matters is the pathogen's, defined by *ompA*/*pmpH* genovar and the cryptic virulence plasmid.

Clinically, LGV classically unfolds in three stages: (1) a transient primary papule or ulcer at the site of inoculation; (2) secondary regional (usually unilateral) inguinal lymphadenopathy with buboes — or, in the modern epidemic among men who have sex with men (MSM), a hemorrhagic **anorectal proctitis**; and (3) a tertiary fibrotic "genito-anorectal syndrome" producing rectal strictures, fistulae, and genital elephantiasis if left untreated. Since 2003, LGV has re-emerged across Europe, North America, Australia, and New Zealand as an epidemic among predominantly **HIV-positive MSM**, driven overwhelmingly by the **L2b** genovar, with proctitis now the dominant presentation and roughly a quarter of anorectal infections asymptomatic.

Diagnosis requires a two-step laboratory approach: detection of *C. trachomatis* by nucleic acid amplification test (NAAT) followed by LGV-discriminatory genotyping (*pmpH*/*ompA* PCR). First-line therapy is **doxycycline 100 mg twice daily for 21 days**, which achieves a pooled microbial cure rate of **98.5%** in rectal LGV. Prevention rests on condoms, partner treatment, screening, and increasingly **doxycycline post-exposure prophylaxis (doxy-PEP)**; no vaccine exists. The pathophysiology is best understood as a causal chain running from Type III secretion system (T3SS)-mediated epithelial invasion, through productive replication in macrophages and lymphatic dissemination, to an IFN-γ/Th1-driven chronic inflammatory response in which matrix metalloproteinase (MMP)-mediated tissue remodeling produces the characteristic scarring and fibrosis. This report synthesizes 15 evidence-backed findings drawn from 37 reviewed papers, organized against the 15-section disease-characteristics template.

---

## Key Findings

### 1. Disease Information

LGV is an invasive systemic infection caused by *C. trachomatis* serovars L1, L2, and L3 (with L2b predominating in current outbreaks), following a three-stage clinical course. As the etiologic review by Ceovic and Gulin states: *"The etiological agent of LGV is Chlamydia trachomatis serotypes L1, L2 and L3, and current outbreaks are mostly sustained by L2b type. The clinical course can be classically divided into three stages: an initial papule, which may ulcerate at the site of inoculation, followed by regional lymphoadenopathy (second stage, generally unilateral). In the tertiary stage, lymphatic obstruction, with elephantiasis of genitalia, and rectal involvement can lead to the formation of strictures and fistulae that may require surgical treatment"* ([PMID: 24518282](https://pubmed.ncbi.nlm.nih.gov/24518282/)).

**Key identifiers and synonyms:**

| Resource | Identifier / Term |
|----------|-------------------|
| MONDO | MONDO:0005834 |
| ICD-10 | A55 (Chlamydial lymphogranuloma [venereum]) |
| ICD-11 | 1A75 (Lymphogranuloma venereum) |
| MeSH | Lymphogranuloma Venereum (D008219) |
| SNOMED CT | 186946009 |
| Synonyms | Lymphogranuloma inguinale; Durand-Nicolas-Favre disease; climatic bubo; tropical bubo; poradenitis; lymphopathia venereum; "anorectal syndrome" (modern) |

The information is derived from **aggregated disease-level resources** — clinical reviews, surveillance datasets, guideline documents, and case series — rather than individual EHR records. (Sources: [PMID: 24518282](https://pubmed.ncbi.nlm.nih.gov/24518282/); [PMID: 39915233](https://pubmed.ncbi.nlm.nih.gov/39915233/))

### 2. Etiology

**Causal factor: infectious.** LGV is caused entirely by infection with the invasive L-biovar of *C. trachomatis*. There is no genetic (host) etiology, no heritable susceptibility variant, no modifier gene, and no gene–environment interaction in the classical human-genetics sense. The determinism lies in the pathogen: *C. trachomatis* comprises **two biovariants — the non-invasive "trachoma" biovar** (ocular and genital serovars A–K) **and the invasive "lymphogranuloma venereum" strains** — and *"the plasmid has been linked to chlamydial virulence"* ([PMID: 19460133](https://pubmed.ncbi.nlm.nih.gov/19460133/)).

**Risk factors (environmental/behavioral):**
- Being a man who has sex with men (MSM) — 93.8% of a 161-isolate Spanish series were MSM ([PMID: 39053939](https://pubmed.ncbi.nlm.nih.gov/39053939/))
- HIV coinfection — ≥43.5% in the same series; ~74% of UK diagnoses in 2013 ([PMID: 39053939](https://pubmed.ncbi.nlm.nih.gov/39053939/); [PMID: 32762828](https://pubmed.ncbi.nlm.nih.gov/32762828/))
- Condomless anal sex, multiple partners, concurrent STIs, chemsex
- Receptive anal intercourse (anatomical route for the dominant anorectal syndrome)

**Protective factors:** condom use (imperfect), partner notification and treatment, and doxycycline post-exposure prophylaxis (see Section 13). There are **no known genetic protective variants** because the host genome does not determine disease.

### 3. Phenotypes

LGV presents as two overlapping clinical syndromes: the **classic inguinal syndrome** and the modern **anorectal proctitis syndrome**.

| Phenotype | Type | Suggested HPO term | Frequency / notes |
|-----------|------|-------------------|-------------------|
| Genital papule/ulcer (primary) | Physical manifestation | HP:0200037 (Genital ulceration) | Often transient/unnoticed |
| Inguinal lymphadenopathy / buboes | Clinical sign | HP:0002716 (Lymphadenopathy) | Classically unilateral |
| Proctitis (anorectal pain, tenesmus, discharge, bleeding) | Symptom/sign | HP:0002607 (rectal); proctitis | Proctitis in 73.3% of symptomatic MSM |
| Anorectal bleeding | Symptom | HP:0002573 (Hematochezia) | Common in proctitis |
| Constipation / tenesmus | Symptom | HP:0002019 (Constipation) | Common |
| Rectal stricture (tertiary) | Physical manifestation | Rectal fibrosis/stricture | Late complication |
| Fistula formation (tertiary) | Physical manifestation | Anal fistula | Late complication |
| Genital elephantiasis (tertiary) | Physical manifestation | HP:0001004 (Lymphedema) | Late complication |
| Asymptomatic carriage | — | — | ~25% of anorectal infections |

The 2019 European guideline notes: *"Among MSM, about 25% of the anorectal LGV infections are asymptomatic"* ([PMID: 31243838](https://pubmed.ncbi.nlm.nih.gov/31243838/)). Proctitis symptoms are detailed in the 2021 European proctitis guideline: *"The symptoms of proctitis include anorectal itching, pain, tenesmus, bleeding, constipation and discharge in and around the anal canal. The majority of rectal chlamydia and gonococcal infections are asymptomatic and can only be detected by laboratory tests"* ([PMID: 34057249](https://pubmed.ncbi.nlm.nih.gov/34057249/)). The modern picture is dominated by *"progressive ulcerative proctitis, the so called anorectal syndrome"* ([PMID: 24518282](https://pubmed.ncbi.nlm.nih.gov/24518282/)).

**Onset/severity/progression:** adult-onset; severity ranges mild-to-severe and is **serovar-dependent** (L1 milder than L2, see Finding 12); progression is from acute proctitis to chronic fibrosis if untreated. **Quality-of-life impact** is substantial in symptomatic proctitis (pain, tenesmus, bleeding) and severe in the tertiary stage (disfiguring elephantiasis, strictures requiring surgery), but disease-specific validated QoL instruments (EQ-5D/SF-36) have not been applied — a knowledge gap.

### 4. Genetic/Molecular Information

**Not applicable to the human host.** LGV has **no causal human genes, pathogenic germline/somatic variants, modifier genes, host epigenetic lesions, or chromosomal abnormalities**. The relevant molecular information belongs to the pathogen:

- **Pathogen biovar/genovar:** the invasive LGV biovar is genomically distinct from the trachoma biovar ([PMID: 19460133](https://pubmed.ncbi.nlm.nih.gov/19460133/)).
- **Cryptic plasmid:** the ~7.5-kb *C. trachomatis* plasmid is linked to virulence and is a key diagnostic target ([PMID: 19460133](https://pubmed.ncbi.nlm.nih.gov/19460133/)).
- **Genotyping markers:** *ompA* (encoding the major outer membrane protein, MOMP) and *pmpH* (polymorphic membrane protein H) discriminate LGV from non-LGV strains ([PMID: 22517888](https://pubmed.ncbi.nlm.nih.gov/22517888/)).
- **Ongoing evolution:** long-term reference-laboratory surveillance (Portuguese NRL, 1,188 LGV isolates) has identified newly emerging genovars, including a recently emerging **L1-like variant** ([PMID: 39915233](https://pubmed.ncbi.nlm.nih.gov/39915233/)).

### 5. Environmental Information

**Infectious agent:** *Chlamydia trachomatis* (NCBI Taxonomy ID 813), L-biovar (serovars L1, L2, L2b, L3). An obligate intracellular Gram-negative bacterium. The relevant "environmental" factors are behavioral (sexual network exposure among MSM, chemsex, condomless anal sex) rather than chemical/toxic. No toxin, radiation, pollutant, occupational exposure, or dietary factor is causally implicated. Transmission is sexual (skin/mucosa contact), with the anorectal mucosa the dominant portal in the current epidemic. (Sources: [PMID: 24518282](https://pubmed.ncbi.nlm.nih.gov/24518282/); [PMID: 39053939](https://pubmed.ncbi.nlm.nih.gov/39053939/))

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating infection → clinical manifestation):**

1. Sexual exposure deposits infectious **elementary bodies (EBs)** of the L-biovar onto genital or anorectal mucosal epithelium → **leads to** attachment and entry.
2. *C. trachomatis* delivers T3SS effectors into the host epithelial cell → **facilitates** invasion and formation of the membrane-bound inclusion (loss of even a single effector such as CT622 strongly reduces invasion). *(demonstrated in vitro)*
3. Inside the inclusion, EBs differentiate to metabolically active **reticulate bodies (RBs)**, replicate, and re-differentiate to EBs (biphasic developmental cycle) → **results in** host-cell egress and local spread. *(demonstrated)*
4. Unlike non-disseminating urogenital serovars, the disseminating **serovar L2 replicates productively in monocyte-derived macrophages** → **enables** the bacteria to survive within phagocytes and be carried into regional lymphatics. *(demonstrated in vitro; the key branch point that makes LGV invasive)*
5. Infected/activated cells release a distinctive cytokine profile (greater IL-8, IL-11; differential TNF-α; IDO upregulation) → **drives** neutrophil and macrophage recruitment and a pro-dissemination inflammatory milieu. *(demonstrated in vitro)*
6. Lymphatic spread to draining nodes → **produces** lymphangitis, lymphadenitis, and buboes (inguinal syndrome) or hemorrhagic proctitis (anorectal syndrome). *(clinical)*
7. A sustained **IFN-γ-dependent Th1** response controls the organism but, when chronic, together with altered **matrix metalloproteinase (MMP)** activity, injures tissue → **causes** fibrosis, strictures, fistulae, and elephantiasis. *(extrapolated from trachoma, the best-characterized chlamydial scarring disease)*

```
EB attachment ──T3SS──> epithelial invasion ──> inclusion / RB replication
      │                                                     │
      │                                          macrophage tropism (L2)  ← KEY branch
      │                                                     │
      └──> local proctitis/ulcer          lymphatic dissemination ──> buboes / lymphadenitis
                                                             │
                                          chronic IFN-γ/Th1 + MMP remodeling
                                                             │
                                          FIBROSIS: strictures, fistulae, elephantiasis
```

**Supporting evidence.** The T3SS mechanism: *"C. trachomatis delivers an arsenal of virulence factors into the eukaryotic cell via a type 3 secretion system (T3SS) that facilitates invasion, manipulation of host vesicular trafficking, subversion of host defense mechanisms and promotes bacteria egress at the conclusion of the developmental cycle"*; and *"All chlamydiae are obligate intracellular bacteria that replicate within a membrane-bound vacuole termed the inclusion"* ([PMID: 33512479](https://pubmed.ncbi.nlm.nih.gov/33512479/)). Macrophage tropism: *"In contrast to the abortive replication of C. trachomatis in monocytes, monocyte-derived macrophages permitted replication as indicated by one-step growth experiments and TEM"* ([PMID: 3759241](https://pubmed.ncbi.nlm.nih.gov/3759241/)). Differential cytokine induction: *"Infection of HeLa cells with C. trachomatis E or L2 induced a strong and similar PMN chemotactic response, but larger amounts of interleukin (IL)-8 and IL-11 were released after infection with serovar L2"* ([PMID: 11207588](https://pubmed.ncbi.nlm.nih.gov/11207588/)), with additional differential TNF-α/IDO signaling ([PMID: 12011019](https://pubmed.ncbi.nlm.nih.gov/12011019/)). Scarring mechanism: *"An increasing number of studies indicate that innate immune responses arising from the epithelium and other innate immune cells, along with changes in matrix metalloproteinase activity, are important in the development of tissue damage and scarring,"* and *"The resolution of Ct infection in animal models is IFNγ-dependent, involving Th1 cells"* ([PMID: 23457650](https://pubmed.ncbi.nlm.nih.gov/23457650/)).

**Suggested ontology terms:** GO:0009405 (pathogenesis); GO:0051701 (biological process involved in interaction with host); GO:0030260 (entry into host cell); GO:0006954 (inflammatory response); GO:0042088 (T-helper 1 type immune response); GO:0030574 (collagen catabolic process / MMP activity). Cell types: CL:0000235 (macrophage); CL:0000775 (neutrophil); CL:0000066 (epithelial cell); CL:0000545 (T-helper 1 cell). Chemical entities: CHEBI:15551 (prostaglandin-related mediators, illustrative); CHEBI:doxycycline (CHEBI:50845).

### 7. Anatomical Structures Affected

| Level | Structure | UBERON / CL / GO term |
|-------|-----------|------------------|
| Primary organ | Rectum / anorectal mucosa (modern) | UBERON:0001052 (rectum) |
| Primary organ | External genitalia / inguinal skin (classic) | UBERON:0000079 (male reproductive system) |
| Primary organ | Regional lymph nodes (inguinal, iliac, perirectal) | UBERON:0000029 (lymph node) |
| Secondary | Lymphatic vessels | UBERON:0001473 (lymphatic vessel) |
| Body system | Lymphatic/immune; lower digestive tract; genital system | — |
| Tissue | Mucosal epithelium; connective tissue (fibrosis) | UBERON:0000483 (epithelium) |
| Cells targeted | Epithelial cells; macrophages/monocytes | CL:0000066; CL:0000235 |
| Subcellular | Membrane-bound inclusion (pathogen vacuole) | GO:0030430 (host cell cytoplasm) |

**Lateralization:** the classic inguinal syndrome is characteristically **unilateral** ([PMID: 24518282](https://pubmed.ncbi.nlm.nih.gov/24518282/)); anorectal disease is midline/rectal.

### 8. Temporal Development

- **Onset:** adult-onset, acute-to-subacute. Primary lesion appears days to weeks after exposure; secondary stage weeks later.
- **Stages:** primary (papule/ulcer) → secondary (lymphadenitis/buboes or proctitis) → tertiary (fibrosis).
- **Progression:** untreated disease is slowly progressive toward fibrosis; treated disease resolves promptly. In a Polish case series the **median diagnostic delay was 6 months** (range 2 weeks–7 months), with patients consulting a median of 3 physicians before diagnosis, and colonoscopy findings *"initially suggesting inflammatory bowel disease or malignancy"* ([PMID: 42151834](https://pubmed.ncbi.nlm.nih.gov/42151834/)).
- **Duration/remission:** self-limited/curable with antibiotics; tertiary damage may be irreversible. Delayed treatment (≥6 months) is associated with **persistent anorectal symptoms** despite therapy ([PMID: 42151834](https://pubmed.ncbi.nlm.nih.gov/42151834/)).
- **Critical period for intervention:** early antibiotic therapy (before fibrosis) is the window of opportunity.

### 9. Inheritance and Population

**Inheritance:** none — this is an infectious disease with **no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency** in the human genetic sense.

**Epidemiology and demographics:**
- **Predominant population:** HIV-positive MSM. In Spain (2018–2019, 161 isolates): *"Most of the 161 LGV isolates (93.8%) were detected in men who have sex with men (MSM). At least 43.5% of the patients presented with HIV coinfection and 53.4% were symptomatic, with proctitis being the most prevalent symptom (73.3%)"* ([PMID: 39053939](https://pubmed.ncbi.nlm.nih.gov/39053939/)).
- **Geographic:** re-emergent since 2003 across Europe, Australia, New Zealand, the US, and Canada ([PMID: 24518282](https://pubmed.ncbi.nlm.nih.gov/24518282/)). Historically endemic in tropical/subtropical regions.
- **Sex ratio:** heavily male-predominant in the current epidemic; heterosexual LGV is *"extremely rare"* in Europe with no evidence of heterosexual transmission ([PMID: 31243838](https://pubmed.ncbi.nlm.nih.gov/31243838/)).
- **Anatomical distribution:** genital:anorectal ratio ≈ **1:15** among MSM; L2b and L2 predominate ([PMID: 31243838](https://pubmed.ncbi.nlm.nih.gov/31243838/)).
- **Surveillance trend (UK):** annual diagnoses rose from **28 (2004) to 904 (2016)**, then fell to 641 (2017); test positivity halved from **14.8% (2015) to 7.3% (2018)**; the HIV-positive share of diagnoses fell from **74% (2013) to 48% (2018)** ([PMID: 32762828](https://pubmed.ncbi.nlm.nih.gov/32762828/)).

### 10. Diagnostics

**Two-step laboratory algorithm:** (1) detect *C. trachomatis* by NAAT (e.g., Aptima Combo 2) on the relevant anatomical site; (2) confirm LGV by genotyping. In a Finnish diagnostic study: *"Altogether 140 C trachomatis NAAT-positive rectal and pharyngeal samples were genotyped by pmpH and ompA real-time PCR. Of the 140 NAAT-positive rectal and pharyngeal specimens, 114 (81%) were successfully typed by pmpH PCR"* — with LGV (mostly L2b) found mainly in rectal samples ([PMID: 22517888](https://pubmed.ncbi.nlm.nih.gov/22517888/)). The 2019 European guideline defines diagnosis as a *C. trachomatis*-positive NAAT confirmed by an LGV-discriminatory NAAT ([PMID: 31243838](https://pubmed.ncbi.nlm.nih.gov/31243838/)).

**Diagnosis is often delayed** and requires clinical suspicion: *"Diagnosis is often delayed, requires a high index of clinical suspicion and must rely on the use of nucleic acid amplification tests"* ([PMID: 24518282](https://pubmed.ncbi.nlm.nih.gov/24518282/)).

**Endoscopy/histopathology:** LGV proctitis endoscopically and histologically **mimics inflammatory bowel disease (IBD)** and malignancy. In HIV-infected men: *"four cases of chlamydial proctitis in HIV-infected individuals, who had different clinical presentations but very similar endoscopic and histopathologic features, as well as prompt and complete response to therapy"* ([PMID: 16721218](https://pubmed.ncbi.nlm.nih.gov/16721218/)).

**Differential diagnosis:** IBD (Crohn's proctitis), rectal malignancy, other ulcerative STIs (syphilis, HSV, chancroid, donovanosis), and non-LGV chlamydial/gonococcal proctitis. **Serology** (complement fixation) is historical and non-specific. **Genetic testing / omics-based diagnostics / newborn or carrier screening: not applicable.**

### 11. Outcome / Prognosis

**Prognosis is excellent with timely antibiotic therapy** and poor-to-morbid if untreated. Early treatment yields prompt, complete resolution ([PMID: 16721218](https://pubmed.ncbi.nlm.nih.gov/16721218/)). Untreated tertiary disease causes disfiguring, potentially irreversible complications — rectal strictures, fistulae, chronic proctocolitis, and genital elephantiasis — that may require surgery ([PMID: 24518282](https://pubmed.ncbi.nlm.nih.gov/24518282/)).

- **Mortality:** LGV is essentially non-fatal with treatment; deaths are exceptional and relate to untreated complications or secondary infection. No formal survival statistics apply.
- **Morbidity:** substantial in the tertiary stage (disability from strictures/lymphedema); moderate in symptomatic proctitis.
- **Prognostic factor:** diagnostic delay. Patients with delays ≥6 months reported persistent anorectal symptoms despite standard therapy ([PMID: 42151834](https://pubmed.ncbi.nlm.nih.gov/42151834/)).
- **Recovery:** high with early treatment; incomplete once fibrosis is established.

### 12. Treatment

**First-line pharmacotherapy: doxycycline 100 mg orally twice daily for 21 days** (NCIT: C312 Doxycycline; ATC J01AA02; CHEBI:50845). This prolonged tetracycline course reflects the invasive, systemic nature of LGV versus the 7-day/single-dose regimens used for uncomplicated urogenital chlamydia. In a Polish case series, *"All received doxycycline 100 mg twice daily for 21 days"* ([PMID: 42151834](https://pubmed.ncbi.nlm.nih.gov/42151834/)). The 2019 European guideline recommends the same regimen — *"Doxycycline 100 mg twice a day orally for 21 days is the recommended treatment for LGV. This same treatment is recommended also in asymptomatic patients and contacts of LGV patients. If another regimen is used, a test of cure (TOC) must be performed"* ([PMID: 31243838](https://pubmed.ncbi.nlm.nih.gov/31243838/)).

**Efficacy (quantitative):** A systematic review and meta-analysis of 9 studies (282 MSM with rectal LGV) found: *"The fixed-effects pooled efficacy for doxycycline was 98.5% (95% CI 96.3%-100%, I² = 0%; p = 0.993). Doxycycline at 100 mg twice daily for 21 days demonstrated a high microbial cure rate"* ([PMID: 27513890](https://pubmed.ncbi.nlm.nih.gov/27513890/)).

| Regimen | Dose / duration | Role | NCIT / evidence |
|---------|-----------------|------|----------------|
| **Doxycycline** | 100 mg BID × 21 days | First-line | NCIT C312; 98.5% cure ([PMID: 27513890](https://pubmed.ncbi.nlm.nih.gov/27513890/)) |
| Azithromycin | 1 g weekly × 3 weeks | Alternative (requires TOC) | NCIT C1264; guideline ([PMID: 31243838](https://pubmed.ncbi.nlm.nih.gov/31243838/)) |
| Erythromycin | 500 mg QID × 21 days | Alternative (e.g., pregnancy) | NCIT C609; guideline |

**Surgical/interventional:** drainage/aspiration of fluctuant buboes; surgical repair of strictures/fistulae in tertiary disease. **Supportive care** for proctitis symptoms. **Pharmacogenomics, gene/cell/RNA therapy, targeted/immunotherapy: not applicable.** Partners and asymptomatic contacts are treated ([PMID: 31243838](https://pubmed.ncbi.nlm.nih.gov/31243838/)).

### 13. Prevention

- **Primary prevention:** condom use (imperfect protection), reduction in partner numbers, partner notification and empiric treatment of contacts ([PMID: 31243838](https://pubmed.ncbi.nlm.nih.gov/31243838/)); condoms *"do not guarantee protection"* ([PMID: 34057249](https://pubmed.ncbi.nlm.nih.gov/34057249/)).
- **Doxycycline post-exposure prophylaxis (doxy-PEP):** doxycycline 200 mg after condomless sex substantially reduces chlamydia (and syphilis) incidence among high-risk MSM and is being rolled out (England, 2025). *"Doxycycline post-exposure prophylaxis (doxy-PEP) has been shown to reduce the incidence of chlamydia and syphilis among men who have sex with men (MSM) at high risk of sexually transmitted infections (STIs)"* ([PMID: 42565264](https://pubmed.ncbi.nlm.nih.gov/42565264/)); independently, *"Promising prevention innovations include doxycycline post-exposure prophylaxis, which substantially reduces chlamydia and syphilis incidence"* ([PMID: 42538441](https://pubmed.ncbi.nlm.nih.gov/42538441/)). Population modelling estimates doxy-PEP could add ~4.4 million defined daily doses of doxycycline per year in the EU/EEA, raising **antimicrobial-resistance concerns** ([PMID: 42565264](https://pubmed.ncbi.nlm.nih.gov/42565264/)).
- **Secondary prevention:** screening of asymptomatic high-risk individuals (multisite NAAT) with LGV genotyping of positives; treatment guideline publication was temporally associated with peaks in testing/diagnosis ([PMID: 32762828](https://pubmed.ncbi.nlm.nih.gov/32762828/)).
- **Tertiary prevention:** prompt full-course therapy to prevent fibrotic complications.
- **Immunization:** **no vaccine exists** for LGV/*C. trachomatis*.

### 14. Other Species / Natural Disease

- **Taxonomy of the pathogen:** *Chlamydia trachomatis* (NCBI Taxon 813). Humans are the natural host; LGV is a **human-specific** disease with no established natural animal reservoir.
- **Zoonotic potential:** none established for the L-biovar.
- **Comparative biology:** related *Chlamydia* species cause disease in animals (e.g., *C. muridarum* in mice, *C. suis* in pigs, *C. abortus/psittaci* in livestock/birds), providing comparative models but not natural LGV.
- **Cross-species susceptibility:** notably, the human serovar **L2 can infect mice directly** (unlike most human serovars), which underpins its use in laboratory models (see Section 15).

### 15. Model Organisms

Mouse models of LGV use the human serovar L2 directly:

| Model | System | Application | Evidence |
|-------|--------|-------------|----------|
| Lung infection | C57BL/6J, serovars D and L2 | Antibiotic (tetracycline, azithromycin) and vaccine screening; survival, bacterial load, histology, MPO, IFN-γ, TNF-α, MCP-1, IL-6 | *"we established an optimized lung infection model for the human intracellular bacterium C. trachomatis serovar D (and L2) in immunocompetent C57BL/6J mice"* ([PMID: 26676260](https://pubmed.ncbi.nlm.nih.gov/26676260/)) |
| Genital immunization | Attenuated plasmidless L2(25667R), intravaginal | Vaccine immunogenicity; partial protection | *"Intravaginal immunization induced both chlamydial specific serum antibody and systemic CD4(+) Th1 biased immune responses"* ([PMID: 20004265](https://pubmed.ncbi.nlm.nih.gov/20004265/)) |
| Cross-protection | MoPn/human biovar challenge | Heterotypic immunity | Prior infection generates broadly cross-reactive T cells protecting against L2 challenge ([PMID: 10338514](https://pubmed.ncbi.nlm.nih.gov/10338514/)) |
| Serovar comparison | Female upper genital tract | Immunopathology | *"Infection with serovar D induces severe tissue inflammation in the female upper genital tract, whereas infection with serovar L2 does not"* ([PMID: 42413199](https://pubmed.ncbi.nlm.nih.gov/42413199/)) |

**Recapitulation/limitations:** these models capture chlamydial replication, Th1/IFN-γ immunity, and antibiotic/vaccine responses, but the murine genital/lung models do **not** fully reproduce the human tertiary lymphatic fibrosis (buboes, strictures, elephantiasis) that defines LGV. In vitro models — HeLa/epithelial infection, monocyte-derived macrophage cultures, and T3SS-effector mutants — resolve the macrophage-tropism and invasion mechanisms. **Model databases:** MGI (mouse), Cellosaurus (HeLa, THP-1 cell lines).

---

## Mechanistic Model / Interpretation

The unifying theme across all 15 findings is that **LGV is a pathogen-determined disease** — its distinctiveness among chlamydial infections flows entirely from the biology of the L-biovar, not from any host predisposition. Two pathogen properties convert a superficial mucosal infection into an invasive, fibrosing systemic disease:

1. **Macrophage tropism** (Finding 3): serovar L2 replicates productively in monocyte-derived macrophages, whereas non-disseminating urogenital serovars abort in these cells. This single biological difference provides the vehicle for lymphatic dissemination and is the mechanistic root of the "invasive" phenotype.

2. **A pro-dissemination inflammatory program** (Findings 3, 15): differential induction of IL-8, IL-11, TNF-α, and IDO shapes a recruitment and effector environment distinct from that of non-invasive strains.

Upstream of both sits the **T3SS-driven obligate intracellular developmental cycle** (Finding 13) common to all chlamydiae, which enables epithelial invasion and immune subversion. Downstream, the **IFN-γ/Th1 response controls the organism but, when chronic, together with MMP-mediated matrix remodeling, drives the scarring** (Finding 15) that produces the tertiary strictures, fistulae, and elephantiasis. The scarring paradigm is extrapolated from trachoma — the best-characterized chlamydial fibrosing disease — and represents the least directly demonstrated (but most biologically coherent) link in the LGV chain.

Clinically, this chain explains everything the surveillance and treatment data show: the anorectal-predominant proctitis of the MSM epidemic (Findings 2, 6, 10) is the mucosal expression; buboes are the lymphatic expression; and both are highly curable with a 21-day doxycycline course (Findings 5, 6, 14) precisely because antibiotics interrupt the cycle before irreversible fibrosis. Diagnostic delay (Finding 2) is the principal modifiable determinant of bad outcomes because it allows the chronic-inflammatory fibrotic arm to progress and because LGV proctitis masquerades as IBD or malignancy (Findings 2, 12).

---

## Evidence Base

| PMID | Role in report | What it supports |
|------|----------------|------------------|
| [24518282](https://pubmed.ncbi.nlm.nih.gov/24518282/) | Foundational review | Etiology, 3-stage course, re-emergence, anorectal syndrome, NAAT diagnosis |
| [39053939](https://pubmed.ncbi.nlm.nih.gov/39053939/) | Multicentre genetic study (Spain) | MSM 93.8%, HIV ≥43.5%, proctitis 73.3% |
| [31243838](https://pubmed.ncbi.nlm.nih.gov/31243838/) | 2019 European guideline | Strain distribution, 25% asymptomatic, 1:15 ratio, doxycycline regimen, contact treatment |
| [27513890](https://pubmed.ncbi.nlm.nih.gov/27513890/) | Systematic review/meta-analysis | 98.5% doxycycline cure rate |
| [32762828](https://pubmed.ncbi.nlm.nih.gov/32762828/) | UK surveillance | Diagnosis trends, positivity decline, HIV share |
| [22517888](https://pubmed.ncbi.nlm.nih.gov/22517888/) | Finnish genotyping study | Two-step NAAT-then-pmpH/ompA diagnosis |
| [42151834](https://pubmed.ncbi.nlm.nih.gov/42151834/) | Polish case series | 6-month delay, IBD/malignancy mimicry, persistent symptoms, 21-day doxycycline |
| [3759241](https://pubmed.ncbi.nlm.nih.gov/3759241/) | In vitro | L2 macrophage tropism |
| [11207588](https://pubmed.ncbi.nlm.nih.gov/11207588/) | In vitro | Differential IL-8/IL-11 cytokines |
| [12011019](https://pubmed.ncbi.nlm.nih.gov/12011019/) | In vitro | Differential TNF-α/IDO signaling |
| [33512479](https://pubmed.ncbi.nlm.nih.gov/33512479/) | Molecular review | T3SS, inclusion, developmental cycle |
| [23457650](https://pubmed.ncbi.nlm.nih.gov/23457650/) | Trachoma immunology review | IFN-γ/Th1 protection; MMP-mediated scarring (extrapolated) |
| [19460133](https://pubmed.ncbi.nlm.nih.gov/19460133/) | Genomics | Distinct invasive biovar; plasmid virulence |
| [39915233](https://pubmed.ncbi.nlm.nih.gov/39915233/) | Reference-lab surveillance | Genovar evolution, emerging L1-like variant |
| [16721218](https://pubmed.ncbi.nlm.nih.gov/16721218/) | Clinical/pathology | IBD-mimicking histopathology; prompt therapy response |
| [7756478](https://pubmed.ncbi.nlm.nih.gov/7756478/) | Historical cluster (L1) | Serovar-dependent severity (L1 milder than L2) |
| [34057249](https://pubmed.ncbi.nlm.nih.gov/34057249/) | 2021 European proctitis guideline | Proctitis symptoms; asymptomatic fraction; condom limits |
| [26676260](https://pubmed.ncbi.nlm.nih.gov/26676260/) | Mouse model | L2 lung model for antibiotic/vaccine screening |
| [20004265](https://pubmed.ncbi.nlm.nih.gov/20004265/) | Mouse vaccine model | Attenuated L2, Th1 immunity, partial protection |
| [10338514](https://pubmed.ncbi.nlm.nih.gov/10338514/) | Mouse cross-protection | Broadly cross-reactive T cells vs L2 |
| [42413199](https://pubmed.ncbi.nlm.nih.gov/42413199/) | Mouse comparison | Serovar-specific immunopathology (D vs L2) |
| [42565264](https://pubmed.ncbi.nlm.nih.gov/42565264/) | Modelling | Doxy-PEP efficacy; AMR concern |
| [42538441](https://pubmed.ncbi.nlm.nih.gov/42538441/) | Review | Doxy-PEP reduces chlamydia incidence |

Evidence source types span **human clinical** (reviews, guidelines, case series, surveillance), **model organism** (murine L2 infection/vaccine studies), and **in vitro** (macrophage tropism, cytokine profiling, T3SS-effector mutants). No computational/structural predictions were required.

---

## Limitations and Knowledge Gaps

1. **Tertiary fibrosis mechanism is extrapolated, not directly demonstrated for LGV.** The IFN-γ/Th1 + MMP scarring paradigm (Finding 15) is drawn from trachoma; LGV-specific molecular studies of stricture/fistula formation are lacking.
2. **No human host-genetics data.** Because LGV is infectious, sections on causal genes, variants, inheritance, penetrance, epigenetics, and chromosomal abnormalities are genuinely not applicable — but this also means host susceptibility modifiers (e.g., HIV-related immune status) are underexplored mechanistically.
3. **Quality-of-life data are anecdotal.** No validated EQ-5D/SF-36/PROMIS measurements for LGV proctitis or tertiary disease were found.
4. **Serovar–severity relationship is based on small/historical data.** The L1-milder-than-L2 claim rests on a single 1980s cluster ([PMID: 7756478](https://pubmed.ncbi.nlm.nih.gov/7756478/)); the newly emerging L1-like variant's virulence is unknown.
5. **Incidence/prevalence rates in per-100,000 terms are not well established** — LGV is reported as counts within MSM sexual-health surveillance rather than population rates.
6. **Doxy-PEP evidence for LGV specifically** is inferred from chlamydia-wide efficacy; direct LGV-endpoint trials and AMR surveillance are still maturing.
7. **Antimicrobial resistance in *C. trachomatis*** to tetracyclines is currently not a documented clinical problem, but doxy-PEP scale-up warrants monitoring.

---

## Proposed Follow-up Experiments / Actions

1. **Define the LGV fibrosis mechanism directly.** Use human anorectal biopsy transcriptomics/spatial transcriptomics (GEO) and MMP profiling from LGV proctitis/stricture tissue to test whether the trachoma MMP/Th1 model holds for LGV.
2. **Characterize the emerging L1-like variant** ([PMID: 39915233](https://pubmed.ncbi.nlm.nih.gov/39915233/)) — whole-genome sequencing, macrophage-tropism assays, and cytokine profiling versus L2b to assess virulence.
3. **Establish validated QoL outcomes.** Apply EQ-5D/PROMIS instruments prospectively in symptomatic LGV proctitis and tertiary cohorts.
4. **Longitudinal doxy-PEP surveillance** for LGV-specific incidence and tetracycline-resistance markers in *C. trachomatis*, given projected ~4.4M DDD/year increase in the EU/EEA ([PMID: 42565264](https://pubmed.ncbi.nlm.nih.gov/42565264/)).
5. **Reduce diagnostic delay** by embedding reflex LGV genotyping of all rectal *C. trachomatis*-positive NAATs in MSM and by clinician education on the IBD/malignancy mimicry (median 6-month delay; [PMID: 42151834](https://pubmed.ncbi.nlm.nih.gov/42151834/)).
6. **Develop an animal model of tertiary LGV** that recapitulates lymphatic fibrosis, since current murine genital/lung L2 models do not capture strictures/elephantiasis.
7. **Vaccine research:** leverage the attenuated plasmidless L2(25667R) Th1 platform ([PMID: 20004265](https://pubmed.ncbi.nlm.nih.gov/20004265/)) toward a broadly protective *C. trachomatis* vaccine, currently the major unmet prevention need.

---

*Report generated from 15 evidence-backed findings and 37 reviewed papers across 5 investigation iterations. All mechanistic and clinical claims are attributed to primary literature by PMID with verbatim abstract quotes.*


## Artifacts

- [OpenScientist final report](Lymphogranuloma_Venereum-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Lymphogranuloma_Venereum-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 23 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 0 |
| Terms whose name was checked | 24 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005834` (3 mentions) - the report calls it "MONDO"; MONDO calls it **lymphogranuloma venereum**
- `HP:0200037` (1 mention) - the report calls it "Genital ulceration"; HP calls it **Skin vesicle**
- `HP:0002607` (1 mention) - the report calls it "rectal"; HP calls it **Bowel incontinence**
- `GO:0030260` (1 mention) - the report calls it "entry into host cell"; GO calls it **GO_0030260**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0009405` (obsolete pathogenesis) (1 mention)
- `GO:0030260` (GO_0030260) (1 mention) - replaced by `GO:0044409`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0009405` (1 mention) - the report calls it "pathogenesis"; GO calls it **obsolete pathogenesis**
- `GO:0030574` (1 mention) - the report calls it "collagen catabolic process / MMP activity"; GO calls it **collagen catabolic process**
- `CHEBI:15551` (1 mention) - the report calls it "prostaglandin-related mediators, illustrative"; CHEBI calls it **prostaglandin E2**
