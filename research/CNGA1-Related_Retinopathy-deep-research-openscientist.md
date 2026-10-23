---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T15:02:51.669704'
end_time: '2026-10-14T15:20:49.567211'
duration_seconds: 1077.9
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: CNGA1-Related Retinopathy
  mondo_id: MONDO:0800405
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
citation_count: 22
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 35
  quotes_valid: 34
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:25268133
  relevance_assessed: 22
  on_topic: 16
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 35
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 4
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0000572
    reported_labels:
    - Reduced visual acuity
    ontology_label: Visual loss
  - term_id: NCIT:C15262
    reported_labels:
    - Suggested NCIT terms:** Gene Therapy
    ontology_label: Immunotherapy
  labels_variant: 9
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
  path: CNGA1-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: CNGA1-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CNGA1-Related Retinopathy
- **MONDO ID:** MONDO:0800405 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CNGA1-Related Retinopathy** covering all of the
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

# CNGA1-Related Retinopathy (Retinitis Pigmentosa 49): A Comprehensive Disease Characterization

**Disease:** CNGA1-Related Retinopathy / Retinitis Pigmentosa 49 (RP49)
**MONDO ID:** MONDO:0800405 · **Gene:** *CNGA1* (HGNC:2000) · **Locus:** 4p12 · **OMIM phenotype:** #613756 · **OMIM gene:** *123825*
**Category:** Mendelian, autosomal recessive, non-syndromic inherited retinal degeneration
**Evidence base:** Literature review (PubMed, 43 papers), gnomAD constraint data, cryo-EM structural studies, human cohorts, and mouse/dog/iPSC models. No primary patient data file was provided; all content derives from aggregated disease-level resources and primary literature.

---

## Summary

CNGA1-Related Retinopathy is a non-syndromic, **autosomal recessive rod–cone dystrophy** (a form of retinitis pigmentosa, RP) caused by biallelic loss-of-function variants in *CNGA1*, the gene encoding the pore-forming α-subunit of the rod cyclic nucleotide-gated (CNG) channel. The native rod channel is a heterotetramer of three CNGA1 and one CNGB1 subunits that opens in response to cytoplasmic cGMP, carrying the depolarizing Na⁺/Ca²⁺ "dark current" that underlies rod phototransduction. When CNGA1 function is lost, the channel cannot assemble or open, the dark current is abolished, and rods degenerate — followed by secondary cone loss and retinal pigment epithelium (RPE) atrophy. *CNGA1* accounts for an estimated **2–8% of autosomal recessive RP**, making it one of the more common arRP genes, particularly in East Asian (Japanese, Chinese) populations.

Clinically, the disease follows a stereotyped natural history: **childhood-onset night blindness** (the universal first symptom, present in ~88% of patients by childhood), **preserved central visual acuity until roughly age 30**, then a slow progressive decline (~0.029 logMAR/year) with constriction of the visual field to tunnel vision (≤10°) by a median age of ~39 years, and legal blindness in about one-third of patients by age 72. The disease is bilateral, highly symmetric, non-syndromic, and non-lethal — morbidity is entirely visual. Diagnosis rests on full-field electroretinography (showing extinguished/markedly reduced rod responses), spectral-domain OCT (ellipsoid-zone width), fundus autofluorescence (hyperautofluorescent ring), and molecular genetic testing.

There is currently **no approved disease-specific therapy**; management is supportive (low-vision rehabilitation, treatment of cataract and cystoid macular edema, genetic counseling). However, the field is moving rapidly toward disease-modifying treatment: AAV-mediated *CNGA1* gene augmentation restored vision and preserved photoreceptors in a *Cnga1*-knockout mouse, and a **phase I/II human gene therapy trial (NCT06291935) is ongoing**. The relatively long window of preserved photoreceptors (central acuity intact for ~3 decades) makes CNGA1-RP an attractive gene-therapy target, and the regulatory precedent of voretigene neparvovec (Luxturna) for RPE65-associated IRD establishes subretinal AAV gene therapy as a viable modality. This report synthesizes 14 confirmed findings across 43 reviewed papers, organized by the 15 requested disease-characteristic sections, with ontology term suggestions and PMID-anchored evidence throughout.

---

## Key Findings

### Finding 1 — Molecular identity: loss of the rod CNG channel α-subunit

CNGA1-RP is an autosomal recessive rod–cone retinitis pigmentosa caused by loss of the rod CNG channel α-subunit. *CNGA1* and *CNGB1* encode the α and β subunits, respectively, of the rod cyclic nucleotide-gated channel, a cGMP-gated cation channel located in the plasma membrane of the rod outer segment. The native rod channel is a **heterotetramer with 3:1 CNGA1:CNGB1 stoichiometry**. Biallelic mutations in either gene produce a progressive rod–cone retinopathy, and *CNGA1* mutations account for ~2–8% of autosomal recessive RP, for which there is currently no approved treatment.

> "The genes CNGA1 and CNGB1 encode the alpha and beta subunits of the rod CNG channel, a ligand-gated cation channel whose activity is controlled by cyclic guanosine monophosphate (cGMP). Autosomal inherited mutations in either of the genes lead to a progressive rod-cone retinopathy known as retinitis pigmentosa (RP)." — [PMID: 37054604](https://pubmed.ncbi.nlm.nih.gov/37054604/)

> "Mutations in cyclic nucleotide-gated channel alpha 1 (CNGA1) account for 2-8% of autosomal recessive RP with no available treatment." — [PMID: 40897815](https://pubmed.ncbi.nlm.nih.gov/40897815/)

> "the native rod CNG functions as a heterotetramer consisting of three A1 and one B1 subunits" — [PMID: 34699778](https://pubmed.ncbi.nlm.nih.gov/34699778/)

### Finding 2 — Natural history: childhood night blindness, stable acuity until ~30, then progressive decline

A large Chinese cohort (n=58 patients, 52 families) defined the natural history. **Night blindness was the universal initial symptom**, with onset in childhood in 88% of patients. Best-corrected visual acuity (BCVA) remained stable at ~0.09 logMAR until a mean age of 30.7 years, after which it declined at **0.029 logMAR per year**; by age 72, 32% of patients had become blind (BCVA > 1.30 logMAR). Visual-field impairment began in childhood and progressed to tunnel vision (≤10°) at a median age of 39.4 years. Disease showed **high interocular symmetry**. A separate multicenter cohort reported 57 patients (mean age 42 ± 16 years).

> "Night blindness was the universal initial symptom, with most patients (88%) experiencing onset during childhood. BCVA remained stable (0.09 logMAR) until age of 30.7 years, followed by a progressive decline at 0.029 logMAR per year; by age of 72 years, 32% of patients had developed blindness (BCVA > 1.30 logMAR). VF impairment began in childhood and progressed to tunnel vision (VF ≤ 10°) at a median age of 39.4 years." — [PMID: 41448483](https://pubmed.ncbi.nlm.nih.gov/41448483/)

This natural-history curve defines the **optimal intervention window**: a multi-decade period of preserved central photoreceptors during which gene augmentation could rescue function before irreversible cell death.

| Age (yr) | Clinical status |
|---------|-----------------|
| Childhood | Night blindness onset (88%); visual-field impairment begins |
| ~10–30 | Central BCVA stable (~0.09 logMAR) |
| ~31+ | Progressive BCVA decline (~0.029 logMAR/yr) |
| ~39 (median) | Tunnel vision (VF ≤ 10°) |
| 72 | 32% legally blind |

### Finding 3 — Pathomechanism: oxidative stress, microglial activation, autophagy/apoptosis

In a CRISPR *Cnga1*-knockout mouse, loss of the channel produced progressive retinal thinning and a functional deficit — the typical RP phenotype. TUNEL and immunofluorescence confirmed **progressive degeneration of rods and cones**, accompanied in parallel by **microglial activation and oxidative-stress damage**. RNA-sequencing showed downregulation of synaptic transmission and phototransduction genes as early as postnatal day 9 — **before measurable cell death** — and downregulation of the PI3K–AKT–mTOR pathway indicating upregulated autophagy, with chaperone-mediated autophagy coinciding temporally with photoreceptor death.

> "We observed progressive retinal thinning and a concomitant functional deficit in vivo as typical phenotypes for RP. Immunofluorescence and TUNEL staining showed progressive degeneration in rods and cones. Moreover, microglial activation and oxidative stress damage occurred in parallel. RNA-sequencing analysis of the retinae suggested down-regulated synaptic transmission and phototransduction as early as 9 days postnatal" — [PMID: 34418172](https://pubmed.ncbi.nlm.nih.gov/34418172/)

> "the down-regulated PI3K-AKT-mTOR pathway indicated upregulation of autophagic process, and chaperone-mediated autophagy was further shown to coincide with the time course of photoreceptor death" — [PMID: 34418172](https://pubmed.ncbi.nlm.nih.gov/34418172/)

### Finding 4 — Gene augmentation therapy rescues vision; active clinical trial

AAV-mediated *Cnga1* gene augmentation in *Cnga1*-deficient mice restored retinal function and vision-guided behavior and preserved photoreceptors — the **first demonstration of vision restoration in a CNGA1-RP animal model**. A phase I/II gene augmentation trial (**NCT06291935**) is ongoing in patients. Cross-channel support comes from the paralogous CNGB1 model: AAV *CNGB1a* gene therapy in *CNGB1⁻/⁻* mice restored CNGA1 levels, channel assembly, rod responses, and vision-guided behavior.

> "this work demonstrates for the first time that a gene augmentation approach can restore vision and preserves photoreceptors in an animal model of CNGA1-RP" — [PMID: 40897815](https://pubmed.ncbi.nlm.nih.gov/40897815/)

> "a phase I/II gene augmentation trial (NCT06291935) is currently ongoing highlighting the necessity to differentiate benign from pathogenic variants" — [PMID: 42192302](https://pubmed.ncbi.nlm.nih.gov/42192302/)

> "the treatment not only led to expression of full-length CNGB1a, but also restored normal levels of the previously degraded CNGA1 subunit of the rod CNG channel" — [PMID: 22802073](https://pubmed.ncbi.nlm.nih.gov/22802073/)

### Finding 5 — Genetics: *CNGA1* at 4p12 (RP49); diverse loss-of-function variants

*CNGA1* maps to chromosome **4p12** (the RP49 locus; original linkage lod 2.90 in a Pakistani family). The variant spectrum is dominated by loss-of-function alleles: frameshift (e.g., c.265delC p.L89Ffs\*4; c.626_627delTA p.Ser209fs\*26), nonsense, splice-site, and missense (e.g., c.1621G>A p.R420Q; p.G509R) variants. In Japanese arRP, *CNGA1* was mutated in **5.1% (5/99)** of patients — one of the most frequent arRP genes in that population. A systematic functional study identified 86 missense *CNGA1* variants, 65.1% initially classified as VUS, which were resolved by an aequorin-based functional assay to refine ACMG/AMP classification. Missense variants affecting the cyclic nucleotide-binding domain (CNBD) are pathogenic in both human patients and an ENU-mutagenesis mouse.

> "Screening of an additional 69 arRP/spRP patients for the CNGA1 gene mutation revealed one patient with a homozygous mutation. This is the first identification of CNGA1 mutations in arRP Japanese patients. The frequency of CNGA1 gene mutation was 5.1% (5/99 patients). CNGA1 mutations are one of the most frequent arRP-causing mutations in Japanese patients." — [PMID: 25268133](https://pubmed.ncbi.nlm.nih.gov/25268133/)

> "autosomal recessive retinitis pigmentosa in this Pakistani family showed linkage to an 11.7 cM region of chromosome 4p12 between D4S405 and D4S1592 with a maximum lod score of 2.90" — [PMID: 15570217](https://pubmed.ncbi.nlm.nih.gov/15570217/)

> "Data mining revealed 86 missense CNGA1 variants - including three novel - most of them lacking functional data; 65.1% of the variants were initially classified as VUS." — [PMID: 42192302](https://pubmed.ncbi.nlm.nih.gov/42192302/)

> "we identified a missense variation in CNGA1 affecting the cyclic nucleotide binding domain (CNBD) and characterized a mouse model developed with mutated CNBD" — [PMID: 36115851](https://pubmed.ncbi.nlm.nih.gov/36115851/)

### Finding 6 — Epidemiology and genetic constraint

Inherited retinal degenerations (IRDs) have a global prevalence of **~1 in 2,000 to 1 in 4,000**; RP is the most frequent IRD. *CNGA1* causes 1–8% of arRP (1% in an Italian cohort; 5.1% in Japanese; 2–8% overall). gnomAD constraint metrics (GRCh38, ENSG00000198515, chr4:47,935,977–48,016,681) show **pLI ≈ 3.7×10⁻¹⁴, observed/expected LoF = 0.76 (90% CI 0.61–0.96), and missense Z = 1.08** — i.e., *CNGA1* tolerates heterozygous loss-of-function, exactly as expected for a recessive disease gene (carriers are unaffected; disease requires biallelic loss). Recessive IRDs cluster strongly with consanguinity (~70% of Pakistani IRD cases consanguineous; 88.8% homozygous variants).

> "Inherited retinal degenerations (IRDs) are a group of rare genetic conditions affecting retina of the eye that range in prevalence from 1 in 2000 to 1 in 4000 people globally" — [PMID: 38317096](https://pubmed.ncbi.nlm.nih.gov/38317096/)

> "In around 70% cases, parents of the index patient were consanguineously married, and approximately 88.81% of the detected variants were found in a homozygous state. Overall, more than 95% of the IRDs cases were recessively inherited." — [PMID: 38317096](https://pubmed.ncbi.nlm.nih.gov/38317096/)

> "Pathogenic variants in CNGA1 and CNGB1 genes, respectively, accounting for 1% and 4% of cases" — [PMID: 38705136](https://pubmed.ncbi.nlm.nih.gov/38705136/)

### Finding 7 — Diagnosis: ERG, OCT, fundus autofluorescence, and molecular testing

In the Italian CNGA1/CNGB1 cohort (n=29; 11 CNGA1), diagnosis combined best-corrected visual acuity, ellipsoid-zone (EZ) width on OCT, fundus photographs, and short-wavelength fundus autofluorescence (SW-AF); the CNGA1 group had a larger mean EZ width than the CNGB1 group. Natural-history cohorts deployed ultra-widefield imaging, SD-OCT, full-field ERG (ISCEV standards), full-field stimulus threshold (FST), multiluminance mobility testing (MLMT), and static perimetry; FAF typically shows a **hyperautofluorescent ring**. The electrophysiological hallmark is **rod-predominant dysfunction** (extinguished or markedly reduced rod ERG responses) with later cone involvement.

> "best-corrected visual acuity (BCVA), ellipsoid zone (EZ) width, fundus photographs, and short-wavelength fundus autofluorescence (SW-AF) images" — [PMID: 38705136](https://pubmed.ncbi.nlm.nih.gov/38705136/)

> "ultra-widefield retinal imaging, spectral-domain OCT, full-field electroretinography, full-field stimulus threshold (FST), multiluminance mobility testing (MLMT), and static perimetry" — [PMID: 42440411](https://pubmed.ncbi.nlm.nih.gov/42440411/)

### Finding 8 — Model organisms

CNGA1-RP is well supported by model systems: (1) a CRISPR *Cnga1*-knockout mouse recapitulating progressive rod–cone degeneration, retinal thinning, and functional deficit ([PMID: 34418172](https://pubmed.ncbi.nlm.nih.gov/34418172/)), used for AAV gene-augmentation rescue ([PMID: 40897815](https://pubmed.ncbi.nlm.nih.gov/40897815/)); (2) an ENU-derived CNBD-mutant mouse ([PMID: 36115851](https://pubmed.ncbi.nlm.nih.gov/36115851/)); and (3) patient-derived iPSC lines SJTUGHi002-A (c.265delC frameshift) and BTHBIOi001-A (c.1621G>A p.R420Q) for in vitro modeling ([PMID: 38340451](https://pubmed.ncbi.nlm.nih.gov/38340451/), [PMID: 40795580](https://pubmed.ncbi.nlm.nih.gov/40795580/)). Paralog models for the same rod channel — CNGB1-deficient mouse and dog — show early rod-function loss then slow rod loss with secondary cone decline, mirroring human disease, with robust AAV rescue in the dog.

> "we developed a mouse model of CNGA1 knock-out using CRISPR/Cas9 technology. We observed progressive retinal thinning and a concomitant functional deficit in vivo as typical phenotypes for RP" — [PMID: 34418172](https://pubmed.ncbi.nlm.nih.gov/34418172/)

> "CNGB1-deficient RP patients and mouse and dog models had a similar phenotype characterized by early loss of rod function and slow rod photoreceptor loss with a secondary decline in cone function... gene augmentation using adeno-associated virus vectors robustly sustained the rescue of rod function and preserved retinal structure in the dog model" — [PMID: 29202463](https://pubmed.ncbi.nlm.nih.gov/29202463/)

> "we established the human induced pluripotent stem cell line (iPSC) SJTUGHi002-A, generated from peripheral blood mononuclear cells of a 36-year-old male RP patient, who carried a homozygous frameshift variant in CNGA1 gene (c.265delC; p.L89Ffs*4)" — [PMID: 38340451](https://pubmed.ncbi.nlm.nih.gov/38340451/)

### Finding 9 — Protein-level mechanism: the cGMP-gated pore and the dark current

Cryo-EM structures of human rod CNGA1 (homotetramer) and the native CNGA1/CNGB1 heterotetramer resolve the ligand-gating mechanism. cGMP binds the C-terminal cyclic-nucleotide-binding domain (CNBD) and opens a central hydrophobic gate located in the middle of the membrane; the selectivity filter (residue E365) coordinates Ca²⁺ and governs non-selective cation (Na⁺/Ca²⁺) permeation. In the native 3:1 channel, CNGB1 residue R994 provides an **additional pore gate** absent from homomeric CNGA channels. In darkness, high cGMP keeps the channel open, sustaining the depolarizing dark current; loss-of-function *CNGA1* variants prevent channel assembly/opening and abolish this current. The channel is further regulated by Ca²⁺/calmodulin and **inhibited by PIP2** binding at an allosteric site between the voltage-sensing, pore, and C-linker domains.

> "we reveal the structural mechanism of ligand gating in human rod CNGA1 channel by determining its cryo-EM structures in both the apo closed and cGMP-bound open states. Distinct from most other members of voltage-gated tetrameric cation channels, CNGA1 forms a central channel gate in the middle of the membrane, occluding the central cavity" — [PMID: 33651975](https://pubmed.ncbi.nlm.nih.gov/33651975/)

> "The arginine residue R994 of CNGB1 reaches into the ionic pathway and blocks the pore, thus introducing an additional gate, which is different from the central hydrophobic gate known from homomeric CNGA channels" — [PMID: 34969975](https://pubmed.ncbi.nlm.nih.gov/34969975/)

> "PIP2 binds at the interface between voltage-sensing, pore, and C-linker domains, stabilizing closed states and sterically preventing channel opening" — [PMID: 42830318](https://pubmed.ncbi.nlm.nih.gov/42830318/)

### Finding 10 — Phenotype spectrum and HPO mapping

The core phenotype is a progressive rod–cone dystrophy. Key features and suggested HPO terms:

| Phenotype | HPO term | Characteristics / frequency |
|-----------|----------|------------------------------|
| Night blindness (nyctalopia) | HP:0000662 | Universal first symptom; childhood onset in ~88% |
| Constriction of peripheral visual field (tunnel vision) | HP:0001133 | Progresses to ≤10° by median age ~39 yr |
| Abnormal electroretinogram | HP:0000512 | Reduced/undetectable rod ERG, then cone decline |
| Rod-cone dystrophy | HP:0000510 | Defining disease category |
| Bone spicule-like pigmentary changes | HP:0007737 | Classic pigmentary retinopathy |
| Attenuated retinal vessels | HP:0007843 | Common RP fundus sign |
| Optic disc pallor (waxy) | HP:0000543 | Late finding |
| Reduced visual acuity | HP:0000572 | Relative central preservation until ~30s |
| Abnormal visual electrophysiology | HP:0000504 | — |
| Posterior subcapsular cataract | HP:0007787 | Common RP complication |
| Cystoid macular edema | HP:0011505 | Common RP complication |

Disease is highly symmetric between eyes.

> "Night blindness was the universal initial symptom, with most patients (88%) experiencing onset during childhood." — [PMID: 41448483](https://pubmed.ncbi.nlm.nih.gov/41448483/)

> "Autosomal inherited mutations in either of the genes lead to a progressive rod-cone retinopathy known as retinitis pigmentosa (RP)." — [PMID: 37054604](https://pubmed.ncbi.nlm.nih.gov/37054604/)

### Finding 11 — Anatomy affected

The rod CNG channel is expressed in the plasma membrane of the **rod outer segment**. CNGA1 loss primarily injures **rod photoreceptors** (CL:0000604) with secondary **cone photoreceptor** (CL:0000573) degeneration and **retinal pigment epithelial** atrophy. The disease is confined to the eye (non-syndromic), bilateral, and largely symmetric. Microglial activation occurs in the degenerating retina. Suggested UBERON terms: retina (UBERON:0000966), photoreceptor outer segment (UBERON:0001787), retinal pigment epithelium (UBERON:0001782). Suggested GO cellular-component terms: plasma membrane (GO:0005886), photoreceptor outer segment (GO:0001750), cyclic nucleotide-gated ion channel complex.

> "The rod CNG channel is expressed in the plasma membrane of the outer segment and functions as a molecular switch" — [PMID: 37054604](https://pubmed.ncbi.nlm.nih.gov/37054604/)

> "characterized by photoreceptor cell death and retinal pigment epithelial atrophy" — [PMID: 38340451](https://pubmed.ncbi.nlm.nih.gov/38340451/)

### Finding 12 — Prognosis and management

CNGA1-RP is non-syndromic and non-lethal (normal life expectancy); morbidity is visual disability. Central acuity is stable until ~age 30, then declines ~0.029 logMAR/yr, with 32% blind by age 72 and tunnel vision by median age ~39 ([PMID: 41448483](https://pubmed.ncbi.nlm.nih.gov/41448483/)). There is no FDA-approved disease-specific pharmacotherapy; management is **supportive**: low-vision rehabilitation, treatment of complications (cystoid macular edema, cataract), UV protection, and (for some RP genotypes) consideration of nutritional therapy. Disease-modifying therapy is on the horizon: AAV gene augmentation restored vision in *Cnga1*-KO mice ([PMID: 40897815](https://pubmed.ncbi.nlm.nih.gov/40897815/)) and a phase I/II trial is ongoing (NCT06291935). The approval of voretigene neparvovec (Luxturna) for RPE65-IRD establishes the subretinal AAV gene-therapy paradigm.

> "a gene augmentation approach can restore vision and preserves photoreceptors in an animal model of CNGA1-RP" — [PMID: 40897815](https://pubmed.ncbi.nlm.nih.gov/40897815/)

> "Nutritional approaches to treatment have proved successful in the case of the common forms of retinitis pigmentosa (supplementation with vitamin A)" — [PMID: 11064860](https://pubmed.ncbi.nlm.nih.gov/11064860/)

> "Voretigene neparvovec is the first approved gene therapy for inherited retinal disease" — [PMID: 42425207](https://pubmed.ncbi.nlm.nih.gov/42425207/)

### Finding 13 — Prevention and etiology

The etiology is **purely monogenic** (biallelic CNGA1 loss-of-function); no infectious, toxic, or lifestyle cause is known, and no environmental risk or protective factor has been established. Primary prevention is not possible for an inherited monogenic disease; prevention operates through reproductive genetic counseling, carrier screening (especially in consanguineous families where recessive IRDs cluster), cascade testing of relatives, and preimplantation/prenatal genetic testing. **Secondary prevention** = early molecular diagnosis to enable monitoring and timely gene-therapy trial enrollment within the preserved-photoreceptor window. Functional variant assays (aequorin-based) help resolve VUS to inform counseling and trial eligibility.

> "In around 70% cases, parents of the index patient were consanguineously married" — [PMID: 38317096](https://pubmed.ncbi.nlm.nih.gov/38317096/)

> "disease relevance remains elusive, impeding molecular genetic diagnostics, patients` and family genetic counseling, and identification of patients eligible for clinical trials" — [PMID: 42192302](https://pubmed.ncbi.nlm.nih.gov/42192302/)

### Finding 14 — Differential diagnosis and genotype–phenotype correlation

CNGA1-RP must be distinguished from other causes of pigmentary rod–cone degeneration: CNGB1-RP (same channel, β-subunit), other arRP genes (PDE6A/B, RHO, USH2A, EYS, SAG, TULP1, RPGR), congenital stationary night blindness (stationary, not progressive), choroideremia, and syndromic RP (Usher, Bardet–Biedl). In a head-to-head Italian cohort (11 CNGA1 vs 18 CNGB1), BCVA was comparable between genes and between predicted "low"- and "high"-impact variant groups, but the CNGA1 group had a **larger mean ellipsoid-zone (EZ) width** than CNGB1 — indicating only a modest genotype–phenotype correlation and a potential differentiating biomarker. Dual/second IRD genotypes can co-occur and confound (e.g., ABCA4+CNGA1 "Stargardt's pigmentosa"; co-occurring SNCAIP/CNGA1 variants in a Parkinson's-plus-RP patient).

> "BCVA was comparable between CNGA1 and CNGB1 groups, as well as between low and high groups. CNGA1 group had a larger mean EZ width compared to C[NGB1]" — [PMID: 38705136](https://pubmed.ncbi.nlm.nih.gov/38705136/)

> "Biallelic mutations were found in ABCA4 and CNGA1 genes. Although not common, different IRDs may be present in a same patient at the same time." — [PMID: 37748682](https://pubmed.ncbi.nlm.nih.gov/37748682/)

---

## Section-by-Section Report

### 1. Disease Information

CNGA1-Related Retinopathy is a non-syndromic, autosomal recessive **retinitis pigmentosa** (progressive rod–cone dystrophy) in which rod photoreceptors degenerate first, followed by cones and RPE, producing night blindness, progressive visual-field loss, and eventual central-vision decline.

- **Identifiers:** MONDO:0800405; OMIM phenotype #613756 (Retinitis pigmentosa 49, RP49); OMIM gene *CNGA1* 123825; HGNC:2000; locus 4p12. ICD-11 maps to retinitis pigmentosa (9B70-family); ICD-10 H35.52 (pigmentary retinal dystrophy). MeSH: Retinitis Pigmentosa (D012174). Orphanet: within the RP group (ORPHA:791).
- **Synonyms:** Retinitis pigmentosa 49; RP49; CNGA1-related RP; CNGA1-associated retinitis pigmentosa; rod CNG channel α-subunit retinopathy.
- **Information source:** Aggregated, disease-level resources and published patient cohorts (Chinese n=58, Italian n=29, Japanese n=99, multicenter n=57), not EHR-level individual data.

### 2. Etiology

- **Causal factor:** Genetic — biallelic loss-of-function variants in *CNGA1* (Findings 1, 5). No environmental, infectious, or mechanical cause.
- **Genetic risk factors:** The only established risk factor is possession of two pathogenic *CNGA1* alleles. No susceptibility loci or validated modifier genes are documented. Consanguinity markedly increases risk of biallelic (usually homozygous) genotypes (Findings 6, 13).
- **Environmental/lifestyle risk factors:** None established (Finding 13).
- **Protective factors:** None genetically or environmentally established; carriers (heterozygotes) are unaffected, consistent with LoF tolerance (Finding 6).
- **Gene–environment interactions:** None documented. CHEBI-relevant small molecules in the pathway include cGMP (CHEBI:16356), Ca²⁺ (CHEBI:29108), Na⁺ (CHEBI:29101), PIP2 (CHEBI:83416).

### 3. Phenotypes

See the Finding 10 table for the HPO-mapped phenotype list, onset, and frequencies. **Quality-of-life impact:** night blindness impairs navigation in dim environments from childhood; progressive peripheral-field loss causes mobility difficulty, loss of driving ability, and eventual legal blindness in a subset — a substantial progressive disability, though central reading vision is preserved for roughly three decades. No disease-specific EQ-5D/SF-36 data were identified; impact is inferred from the natural-history trajectory (Finding 2).

### 4. Genetic/Molecular Information

- **Causal gene:** *CNGA1* (4p12; OMIM 123825; HGNC:2000). Encodes the α-subunit of the rod CNG channel (Findings 1, 5).
- **Variant types:** Predominantly loss-of-function — frameshift (c.265delC p.L89Ffs\*4; c.626_627delTA p.Ser209fs\*26), nonsense, splice-site, and missense (c.1621G>A p.R420Q; p.G509R; CNBD missense). 86 missense variants catalogued, 65.1% initially VUS (Finding 5).
- **ACMG classification:** Many variants remain VUS pending functional data; aequorin-based assays reclassify them (Findings 5, 13).
- **Allele frequency / constraint:** gnomAD pLI ≈ 3.7×10⁻¹⁴, o/e LoF = 0.76, missense Z = 1.08 — LoF-tolerant, consistent with recessive mechanism (Finding 6).
- **Origin:** Germline (Findings 1, 5). No somatic involvement.
- **Functional consequence:** Loss of function — channel fails to assemble/open (Finding 9).
- **Modifier genes / epigenetics / chromosomal abnormalities:** None established for CNGA1-RP.

### 5. Environmental Information

Not applicable. No environmental factors, lifestyle factors, or infectious agents are implicated in this monogenic disease (Finding 13).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic loss-of-function *CNGA1* variants** → absence of functional CNGA1 α-subunit protein (demonstrated; Findings 1, 5).
2. Loss of CNGA1 → **failure to assemble the 3:1 CNGA1/CNGB1 rod CNG channel** in the outer-segment plasma membrane (inferred from stoichiometry and paralog data; Findings 1, 8, 9).
3. No functional channel → **the cGMP-gated Na⁺/Ca²⁺ dark current is abolished** (demonstrated structurally/functionally; Finding 9).
4. Loss of dark current → **phototransduction failure and chronically hyperpolarized rods** → night blindness (demonstrated clinically/electrophysiologically; Findings 2, 7, 10).
5. In parallel, dysregulated Ca²⁺/cGMP homeostasis and early downregulation of synaptic-transmission and phototransduction gene programs (from P9, before cell death) → cellular stress (demonstrated in KO mouse RNA-seq; Finding 3).
6. Cellular stress → **oxidative-stress damage and microglial activation** (branch: neuroinflammation) + **PI3K–AKT–mTOR downregulation → increased autophagy / chaperone-mediated autophagy** → these converge on **rod apoptosis** (demonstrated; Finding 3).
7. Progressive rod death → **secondary cone degeneration and RPE atrophy** (demonstrated; Findings 3, 11) → visual-field constriction, tunnel vision, central-acuity decline, legal blindness in a subset (demonstrated clinically; Finding 2).

```
CNGA1 biallelic LoF
      │
      ▼
No CNGA1 α-subunit protein
      │
      ▼
Rod CNG channel (3 A1 : 1 B1) fails to assemble
      │
      ▼
cGMP-gated Na+/Ca2+ "dark current" abolished
      │
      ├───────────────► Phototransduction failure → NIGHT BLINDNESS
      ▼
Ca2+/cGMP dysregulation + early transcriptional changes (P9)
      │
      ├──► Oxidative stress ──────────┐
      ├──► Microglial activation ─────┤
      └──► PI3K-AKT-mTOR↓ → autophagy ┘
                                   │
                                   ▼
                             ROD APOPTOSIS
                                   │
                                   ▼
          Secondary CONE degeneration + RPE atrophy
                                   │
                                   ▼
   Visual-field constriction → tunnel vision → central vision loss
```

- **Molecular pathways:** cGMP phototransduction cascade; PI3K–AKT–mTOR (downregulated → autophagy).
- **Cellular processes (GO):** visual perception / phototransduction (GO:0007601, GO:0007602); apoptotic process (GO:0006915); autophagy (GO:0006914); chaperone-mediated autophagy (GO:0061684); microglial cell activation (GO:0001774); response to oxidative stress (GO:0006979).
- **Protein dysfunction:** Loss-of-function; failure of channel assembly/gating (Finding 9).
- **Ion channel defect:** Abolition of the cGMP-gated cation (Na⁺/Ca²⁺) current (Finding 9).
- **Cell types (CL):** rod photoreceptor (CL:0000604) upstream; cone photoreceptor (CL:0000573) and RPE downstream; microglial cell (CL:0000129).

### 7. Anatomical Structures Affected

- **Organ:** eye / retina (UBERON:0000966); non-syndromic — no extra-ocular organ involvement.
- **Tissue/cell:** neural retina photoreceptor layer; rod photoreceptors (primary, CL:0000604), cone photoreceptors (secondary, CL:0000573), RPE (secondary).
- **Subcellular (GO CC):** photoreceptor outer segment (GO:0001750); plasma membrane (GO:0005886); cyclic nucleotide-gated channel complex.
- **Localization/lateralization:** Bilateral, highly symmetric (Findings 2, 11).

### 8. Temporal Development

- **Onset:** Childhood (night blindness in ~88% by childhood); congenital predisposition with early functional onset (Finding 2).
- **Course:** Chronic, slowly progressive, lifelong. Central acuity stable until ~30, then ~0.029 logMAR/yr decline; tunnel vision by median ~39; 32% blind by 72 (Finding 2).
- **Critical period:** The multi-decade window of preserved central photoreceptors is the therapeutic opportunity window for gene augmentation (Findings 2, 4).

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive; complete biallelic penetrance expected; variable expressivity (modest; Finding 14). No anticipation (not a repeat-expansion disorder).
- **Epidemiology:** IRD prevalence ~1/2,000–1/4,000; CNGA1 = 1–8% of arRP (Findings 1, 6).
- **Carrier frequency / constraint:** LoF-tolerant gene; heterozygous carriers unaffected (Finding 6).
- **Consanguinity / founder effects:** Consanguinity strongly enriches recessive IRD, including CNGA1-RP (~70% consanguineous, 88.8% homozygous in Pakistani IRD cohort) (Finding 6). Enriched in East Asian (Japanese 5.1%) populations (Finding 5).
- **Sex ratio:** No sex predilection (autosomal). **Age distribution:** affected lifelong from childhood onset.

### 10. Diagnostics

- **Electrophysiology:** Full-field ERG (ISCEV) — extinguished/markedly reduced scotopic rod responses, later cone decline (Findings 7, 10).
- **Imaging:** SD-OCT (ellipsoid-zone width, photoreceptor loss); fundus autofluorescence (hyperautofluorescent ring); ultra-widefield fundus photography (bone-spicule pigmentation, vessel attenuation, waxy disc pallor) (Finding 7).
- **Functional:** full-field stimulus threshold (FST), multiluminance mobility testing (MLMT), static perimetry (Finding 7).
- **Genetic testing:** The definitive diagnostic. Approaches: targeted IRD gene panels, whole-exome and whole-genome sequencing, single-gene testing; functional assays (aequorin-based) to resolve VUS (Findings 5, 13). WES identified CNGA1 as a frequent arRP cause in Japanese patients (Finding 5).
- **Differential diagnosis:** CNGB1-RP, PDE6A/B-RP, RHO, USH2A/EYS, CSNB, choroideremia, syndromic RP (Finding 14). Larger EZ width distinguishes CNGA1 from CNGB1 (Finding 14).
- **Screening:** Carrier and cascade screening in families; prenatal/PGT where desired (Finding 13).

### 11. Outcome/Prognosis

- **Mortality:** None — normal life expectancy; non-lethal (Finding 12).
- **Morbidity:** Progressive bilateral visual disability; legal blindness in ~32% by age 72 (Findings 2, 12).
- **Prognostic factors:** Age, EZ width, baseline BCVA, residual photoreceptor reserve. Recovery potential: none spontaneously; potential functional rescue with gene therapy if treated within the preserved-photoreceptor window (Findings 4, 12).

### 12. Treatment

- **Current (supportive):** Low-vision rehabilitation; management of cataract and cystoid macular edema; UV protection; genetic counseling. No approved disease-specific drug (Finding 12). Nutritional (vitamin A palmitate) has a precedent in common RP forms but is not CNGA1-specific and must be weighed against genotype (Finding 12).
- **Advanced/experimental:** **AAV-mediated *CNGA1* gene augmentation** — restored vision and preserved photoreceptors in *Cnga1*-KO mice (Finding 4); **phase I/II trial NCT06291935** ongoing (Finding 4). Cross-channel proof-of-concept: AAV *CNGB1a* in CNGB1⁻/⁻ mice and dogs (Findings 4, 8).
- **Regulatory precedent:** Voretigene neparvovec (Luxturna, subretinal AAV) for RPE65-IRD — the first approved IRD gene therapy — validates the modality (Finding 12).
- **Suggested NCIT terms:** Gene Therapy (NCIT:C15262); Adeno-associated Virus Vector; Supportive Care (NCIT:C15346); Rehabilitation Therapy.

### 13. Prevention

Primary prevention is not possible (monogenic). Prevention = **reproductive genetic counseling, carrier/cascade screening, PGT/prenatal testing**, and **secondary prevention via early molecular diagnosis** for monitoring and trial eligibility within the therapeutic window (Finding 13). Variant functional classification supports accurate counseling (Finding 13).

### 14. Other Species / Natural Disease

- **Orthologs/models:** Mouse *Cnga1* (CRISPR KO and ENU CNBD-mutant); the paralogous rod-channel β-subunit has natural disease models in **mouse and dog** (CNGB1), and a dog PDE6A model of RP exists (Finding 8). Residual desensitized rod ERG in CNGB1-mutant dogs is attributed to low outer-segment CNGA1 (Finding 8). No companion-animal natural CNGA1 disease is specifically documented in the reviewed literature. Suggested NCBI Taxon IDs: *Mus musculus* (10090), *Canis lupus familiaris* (9615).
- **Comparative biology:** The rod CNG channel's 3 CNGA1 : 1 CNGB1 stoichiometry is conserved across vertebrates; phenotype concordance across mouse, dog, and human supports strong evolutionary conservation of the mechanism (Finding 8).

### 15. Model Organisms

| Model | Type | Variant / method | Phenotype recapitulation | PMID |
|-------|------|------------------|--------------------------|------|
| *Cnga1* KO mouse | Mammalian, knockout | CRISPR/Cas9 | Progressive rod–cone degeneration, retinal thinning, functional deficit; oxidative stress, microglial activation | [34418172](https://pubmed.ncbi.nlm.nih.gov/34418172/) |
| CNBD-mutant mouse | Mammalian, point mutant | ENU, CNBD missense | arRP-like degeneration | [36115851](https://pubmed.ncbi.nlm.nih.gov/36115851/) |
| *Cnga1*-deficient mouse (gene therapy) | Mammalian | AAV gene augmentation | Vision restored, photoreceptors preserved | [40897815](https://pubmed.ncbi.nlm.nih.gov/40897815/) |
| iPSC SJTUGHi002-A | Human in vitro | c.265delC p.L89Ffs*4 | Patient-specific disease modeling | [38340451](https://pubmed.ncbi.nlm.nih.gov/38340451/) |
| iPSC BTHBIOi001-A | Human in vitro | c.1621G>A p.R420Q | Patient-specific disease modeling | [40795580](https://pubmed.ncbi.nlm.nih.gov/40795580/) |
| CNGB1 mouse/dog (paralog) | Mammalian | CNGB1 LOF | Early rod loss, slow degeneration, secondary cone decline; AAV rescue | [29202463](https://pubmed.ncbi.nlm.nih.gov/29202463/) |

**Model limitations:** Mouse retina lacks a macula, so central-vision/macular aspects of human disease are imperfectly modeled; rapid rodent degeneration compresses the slow human time course. iPSC/organoid models capture early molecular events but not whole-tissue circuitry or long-term progression.

---

## Mechanistic Model / Interpretation

CNGA1-RP is, at its core, a **channelopathy that becomes a degeneration**. The primary lesion is purely genetic and purely loss-of-function: without CNGA1, the rod outer-segment CNG channel cannot assemble in its native 3:1 configuration, and the cGMP-gated dark current that depolarizes rods in darkness is lost. This immediately explains the **earliest and most constant symptom, childhood night blindness** — rods cannot signal. The transition from a functional defect to irreversible structural degeneration is driven downstream by a stereotyped stress cascade seen in the knockout mouse: early (pre-death) transcriptional downregulation of phototransduction and synaptic genes, then oxidative stress, microglial (neuroinflammatory) activation, and a shift toward autophagic/apoptotic cell death via PI3K–AKT–mTOR downregulation and chaperone-mediated autophagy. Rods die first; cones and RPE follow secondarily, producing the classic centripetal progression from mid-peripheral pigmentary retinopathy to tunnel vision and, eventually, central-vision loss.

The key clinical corollary is the **long therapeutic window**: because central cones are preserved for roughly three decades, and because the defect is a single missing gene product, **gene augmentation is mechanistically ideal** — restoring CNGA1 reconstitutes the channel, as directly demonstrated both in the *Cnga1*-KO mouse (vision restored) and in the paralogous CNGB1 system (where CNGB1a delivery even restored the degraded CNGA1 subunit). This mechanistic logic is why CNGA1-RP has advanced to a phase I/II human trial (NCT06291935), riding the regulatory and technical precedent of Luxturna.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|------|------------------|---------------------|
| [37054604](https://pubmed.ncbi.nlm.nih.gov/37054604/) | *CNG channel-related retinitis pigmentosa* | Defines gene products, channel, ligand, disease class, outer-segment localization |
| [40897815](https://pubmed.ncbi.nlm.nih.gov/40897815/) | *Gene augmentation restores vision in Cnga1 mouse* | CNGA1 = 2–8% arRP; preclinical gene-therapy proof-of-concept |
| [34699778](https://pubmed.ncbi.nlm.nih.gov/34699778/) | *Native human rod CNG channel structure* | 3:1 CNGA1:CNGB1 stoichiometry |
| [41448483](https://pubmed.ncbi.nlm.nih.gov/41448483/) | *Natural history, large Chinese cohort* | Quantitative onset/progression; intervention window |
| [34418172](https://pubmed.ncbi.nlm.nih.gov/34418172/) | *Cnga1 KO mouse retinal degeneration* | Pathomechanism: oxidative stress, microglia, autophagy/apoptosis |
| [42192302](https://pubmed.ncbi.nlm.nih.gov/42192302/) | *Systematic CNGA1 missense variant evaluation* | Variant burden/VUS; confirms trial NCT06291935 |
| [22802073](https://pubmed.ncbi.nlm.nih.gov/22802073/) | *CNGB1 gene therapy, mouse* | Cross-channel rescue; restores CNGA1 |
| [25268133](https://pubmed.ncbi.nlm.nih.gov/25268133/) | *CNGA1 in Japanese arRP* | 5.1% frequency; East Asian enrichment |
| [15570217](https://pubmed.ncbi.nlm.nih.gov/15570217/) | *Pakistani family linkage* | Maps RP49 to 4p12 |
| [36115851](https://pubmed.ncbi.nlm.nih.gov/36115851/) | *CNBD mutations, human + mouse* | CNBD missense pathogenicity cross-species |
| [38317096](https://pubmed.ncbi.nlm.nih.gov/38317096/) | *Pakistan IRD systematic review* | IRD prevalence; consanguinity role |
| [38705136](https://pubmed.ncbi.nlm.nih.gov/38705136/) | *CNGA1/CNGB1 cohort characterization* | Diagnostics; CNGA1 vs CNGB1 EZ width |
| [42440411](https://pubmed.ncbi.nlm.nih.gov/42440411/) | *Clinical/molecular features cohort* | Diagnostic/endpoint battery |
| [38340451](https://pubmed.ncbi.nlm.nih.gov/38340451/) | *iPSC SJTUGHi002-A* | Patient iPSC model; RPE atrophy |
| [29202463](https://pubmed.ncbi.nlm.nih.gov/29202463/) | *CNGB1 patients + mouse/dog models* | Cross-species concordance, gene-therapy rescue |
| [33651975](https://pubmed.ncbi.nlm.nih.gov/33651975/) | *CNGA1 gating/selectivity cryo-EM* | cGMP gating, central gate |
| [34969975](https://pubmed.ncbi.nlm.nih.gov/34969975/) | *Native bovine CNGA1/CNGB1 structure* | CNGB1 R994 additional gate |
| [42830318](https://pubmed.ncbi.nlm.nih.gov/42830318/) | *PIP2 inhibition of rod CNG channel* | Allosteric PIP2 regulation (drug target) |
| [11064860](https://pubmed.ncbi.nlm.nih.gov/11064860/) | *Nutrition and retinal degenerations* | Vitamin A precedent in RP |
| [42425207](https://pubmed.ncbi.nlm.nih.gov/42425207/) | *Voretigene neparvovec outcomes* | Subretinal AAV regulatory precedent |
| [37748682](https://pubmed.ncbi.nlm.nih.gov/37748682/) | *ABCA4+CNGA1 dual IRD* | Differential diagnosis / dual genotypes |

**Challenges/caveats in the evidence:** PMID 29202463 and several paralog (CNGB1) papers address the β-subunit disease, not CNGA1 directly; they are used as mechanistic analogies, clearly flagged. The Luxturna papers (RPE65) establish modality precedent, not CNGA1-specific efficacy.

---

## Limitations and Knowledge Gaps

1. **No population-specific prevalence** for CNGA1-RP as a distinct entity — only its fraction of arRP (1–8%) is known; absolute cases/100,000 are not established.
2. **Human efficacy unknown.** Gene-therapy evidence is preclinical (mouse) plus an ongoing phase I/II trial with no published outcomes yet.
3. **Variant interpretation remains incomplete** — 65% of missense variants were initially VUS; functional data are still being generated.
4. **No validated modifier genes, epigenetic mechanisms, or QoL instruments** specific to CNGA1-RP were identified.
5. **Genotype–phenotype correlation is weak** — only EZ width modestly distinguishes CNGA1 from CNGB1; no clear severity predictors from variant class.
6. **Natural-history data are cohort-based** (China, Italy, Japan), potentially limiting generalizability; longitudinal prospective data are sparse.
7. **Model limitations:** rodent models lack a macula and progress too fast to model the human central-vision time course.

---

## Proposed Follow-up Experiments / Actions

1. **Track NCT06291935 outcomes** — safety, BCVA, FST, and visual-field endpoints will be the decisive human efficacy data; define biomarker-based patient-selection criteria (EZ width, residual rod function).
2. **Build a CNGA1 variant functional-evidence database** — extend the aequorin-based assay to all catalogued missense variants to convert VUS to actionable classifications for diagnosis, counseling, and trial eligibility.
3. **Prospective multi-ethnic natural-history registry** with standardized SD-OCT (EZ width), FAF ring metrics, FST, and perimetry to refine the intervention window and identify prognostic biomarkers.
4. **Generate retinal organoids** from CNGA1-patient iPSC lines (SJTUGHi002-A, BTHBIOi001-A) to model channel-assembly defects and screen neuroprotective/anti-oxidative adjuncts that could extend the treatment window.
5. **Test adjunctive neuroprotection** (antioxidants, microglial modulators, autophagy modulators) in the *Cnga1*-KO mouse, targeting the downstream stress cascade (oxidative stress, microglial activation, CMA) to slow degeneration independent of gene replacement.
6. **Explore the PIP2 allosteric site** structurally identified in the rod CNG channel as a potential small-molecule modulatory target for residual/partial-function alleles.
7. **Estimate carrier frequency and absolute prevalence** using gnomAD LoF-allele frequencies and population genetics to inform screening-program design, especially in consanguineous and East Asian populations.

---

*Report compiled from 14 confirmed findings across 43 reviewed papers over 5 investigation iterations. Evidence-source types span human clinical cohorts, model organisms (mouse, dog), in vitro (iPSC), and computational/structural (cryo-EM, gnomAD constraint) studies, as indicated throughout.*


## Artifacts

- [OpenScientist final report](CNGA1-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](CNGA1-Related_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 35 |
| Quoted claims found in source | 34 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 22 |
| On topic | 16 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:25268133`: "Screening of an additional 69 arRP/spRP patients for the CNGA1 gene mutation revealed one patient with a homozygous mutation. This is the first identification of CNGA1 mutations in arRP Japanese patients. The frequency of CNGA1 gene mutation was 5.1% (5/99 patients). CNGA1 mutations are one of the most frequent arRP-causing mutations in Japanese patients."
  - closest text in source: "Screening of an additional 69 arRP/spRP patients for the CNGA1 gene mutation revealed one patient with a homozygous mutation"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 15 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000572` (1 mention) - the report calls it "Reduced visual acuity"; HP calls it **Visual loss**
- `NCIT:C15262` (1 mention) - the report calls it "Suggested NCIT terms:** Gene Therapy"; NCIT calls it **Immunotherapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000662` (1 mention) - the report calls it "Night blindness (nyctalopia)"; HP calls it **Nyctalopia**, and lists "Night blindness" among its other names
- `HP:0001133` (1 mention) - the report calls it "Constriction of peripheral visual field (tunnel vision)"; HP calls it **Constriction of peripheral visual field**
- `HP:0007737` (1 mention) - the report calls it "Bone spicule-like pigmentary changes"; HP calls it **Spicular pigmentation of the retina**, and lists "Bone spicule pigmentation of the retina" among its other names
- `HP:0007843` (1 mention) - the report calls it "Attenuated retinal vessels"; HP calls it **Attenuation of retinal blood vessels**
- `HP:0000543` (1 mention) - the report calls it "Optic disc pallor (waxy)"; HP calls it **Optic disc pallor**
- `HP:0000504` (1 mention) - the report calls it "Abnormal visual electrophysiology"; HP calls it **Abnormality of vision**
- `CL:0000604` (3 mentions) - the report calls it "rod photoreceptors"; CL calls it **retinal rod cell**, and lists "rod" among its other names
- `CL:0000573` (3 mentions) - the report calls it "cone photoreceptor"; CL calls it **retinal cone cell**, and lists "cone" among its other names
- `UBERON:0000966` (2 mentions) - the report calls it "Organ:** eye / retina"; UBERON calls it **retina**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.