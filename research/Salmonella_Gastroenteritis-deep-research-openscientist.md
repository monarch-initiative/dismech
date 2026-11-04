---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T03:14:56.585732'
end_time: '2026-09-30T03:35:55.525051'
duration_seconds: 1258.94
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Salmonella Gastroenteritis
  mondo_id: MONDO:0005950
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 36
reference_validation:
  total_references: 36
  verified: 36
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 36
  on_topic: 23
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 30
  verified: 28
  not_found: 0
  obsolete: 2
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 6
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: GO:0052192
    reported_labels:
    - movement in host
    ontology_label: obsolete movement in environment of other organism involved in
      symbiotic interaction
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0052192
    ontology_label: obsolete movement in environment of other organism involved in
      symbiotic interaction
  - term_id: GO:0097202
    ontology_label: obsolete activation of cysteine-type endopeptidase activity
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Salmonella_Gastroenteritis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Salmonella_Gastroenteritis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Salmonella Gastroenteritis
- **MONDO ID:** MONDO:0005950 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Salmonella Gastroenteritis** covering all of the
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

# Salmonella Gastroenteritis (MONDO:0005950): A Comprehensive Disease Characterization

## Summary

**Salmonella gastroenteritis** is a self-limited, foodborne zoonotic enterocolitis caused chiefly by **non-typhoidal *Salmonella enterica* (NTS)** serovars — predominantly **S. Typhimurium** and **S. Enteritidis** — and represents one of the leading bacterial causes of diarrheal illness worldwide. The disease is fundamentally an **infectious**, not a genetic, entity: the initiating lesion is ingestion of *Salmonella* in contaminated food or water, and the causal chain runs from bacterial invasion of the distal ileal/cecal/colonic epithelium through host inflammasome activation and neutrophilic colitis to inflammatory-secretory diarrhea. A defining mechanistic insight, established across multiple lines of evidence in this investigation, is that *Salmonella* does not merely tolerate host inflammation but actively **exploits it** — inflammation oxidizes luminal thiosulfate to **tetrathionate**, which the pathogen uses as a respiratory electron acceptor to outcompete the fermentative resident microbiota and bloom in the gut lumen.

Clinically, most immunocompetent patients present with **diarrhea (~96%)**, **fever (~62–66%)**, **abdominal pain (~32–42%)**, **vomiting (~34%)**, and less often **bloody diarrhea (~19%)**, after an incubation period of roughly **6–72 hours** (dose-dependent), and recover spontaneously within **2–7 days** with **oral/IV rehydration alone**. Antibiotics do not shorten uncomplicated illness and may prolong fecal carriage; they are therefore reserved for severe disease and high-risk hosts. A distinct and dangerous **invasive NTS (iNTS)** branch causes bacteremia and extraintestinal focal infection (mycotic aortitis, endovascular infection, osteomyelitis, meningitis) in the very young, the elderly, and immunocompromised hosts — especially those with **HIV, malaria, malnutrition, anemia, sickle cell disease, or inborn errors of the IL-12/IL-23/IFN-γ axis**. iNTS carries a case-fatality rate of ~15–25% and is concentrated in sub-Saharan Africa, where the multidrug-resistant **S. Typhimurium ST313** lineage drives epidemics.

This report synthesizes **19 confirmed findings** drawn from **94 reviewed papers**, organized against the 15-section disease-characterization template. Because Salmonella gastroenteritis is an infectious disease, several template sections designed for Mendelian genetic disorders (causal genes, pathogenic variants, inheritance patterns) are **not applicable in the classical sense** and are reframed around *host susceptibility genetics* and *bacterial virulence genetics*, which are the biologically meaningful analogues.

---

## 1. Disease Information

**Overview.** Salmonella gastroenteritis is an acute inflammatory enterocolitis of the distal small bowel and colon caused by non-typhoidal serovars of the Gram-negative facultative intracellular bacterium *Salmonella enterica* subsp. *enterica*. It is the enteric-limited form of non-typhoidal salmonellosis, distinct from enteric (typhoid/paratyphoid) fever caused by the host-restricted serovars Typhi and Paratyphi.

**Key identifiers.**
- **MONDO:** MONDO:0005950 (Salmonella gastroenteritis / salmonella food poisoning)
- **MeSH:** Salmonella Infections; Salmonella Food Poisoning
- **ICD-10:** A02.0 (Salmonella enteritis); ICD-11: 1A07 (Enteritis due to *Salmonella*)
- **SNOMED CT:** Salmonella gastroenteritis
- **NCBI Taxonomy:** *Salmonella enterica* (txid28901); serovar Typhimurium, serovar Enteritidis
- OMIM/Orphanet: not a Mendelian disease; no primary OMIM entry (host susceptibility loci discussed in Section 4/9).

**Synonyms:** non-typhoidal salmonellosis, Salmonella enterocolitis, Salmonella food poisoning, NTS gastroenteritis.

**Data source type.** The knowledge in this report derives predominantly from **aggregated disease-level resources** — epidemiological surveillance (GBD, CDC, WHO), clinical cohort studies, systematic reviews, and mechanistic model-organism/in-vitro experiments — rather than from individual EHR-level patient records.

The leading global role of NTS is well documented: *"Bacterial pathogens cause approximately 10-15% of episodes, most often Shigella, nontyphoidal Salmonella (NTS) Campylobacter and Shiga toxin-producing Escherichia coli (STEC)"* ([PMID: 35165210](https://pubmed.ncbi.nlm.nih.gov/35165210/)), and *"Salmonella enterica serovar Enteritidis (S. Enteritidis) is a commonly reported pathogen which adapts to multiple hosts and causes critical disease burden at a global level"* ([PMID: 39855357](https://pubmed.ncbi.nlm.nih.gov/39855357/)). *(Finding F001)*

---

## 2. Etiology

**Primary cause — infectious.** The disease is caused by ingestion of viable *Salmonella enterica* NTS serovars. S. Typhimurium and S. Enteritidis are the most common serovars worldwide.

**Environmental / lifestyle risk factors.**
- **Contaminated food and water** — poultry, eggs, dairy, beef, and produce are principal vehicles (Section 5, 12).
- **Gastric acid suppression.** Gastric acid is a key host defense barrier. A population case-control study (6,414 cases vs 50,000 controls) found current PPI use raised bacterial gastroenteritis risk **RR 2.9 (95% CI 2.5–3.5)**, rising to **RR 5.0** with a doubled PPI dose, while H2-receptor antagonists showed no significant effect: *"Current use of PPIs was associated with an increased risk of bacterial GE compared with nonuse, regardless of the treatment duration (RR, 2.9; 95% confidence interval [CI], 2.5-3.5)"* ([PMID: 18054750](https://pubmed.ncbi.nlm.nih.gov/18054750/)). A systematic review confirmed *"PPIs appear to increase susceptibility to the following bacterial enteropathogens: Salmonella, Campylobacter jejuni, invasive strains of Escherichia coli"* ([PMID: 21999643](https://pubmed.ncbi.nlm.nih.gov/21999643/)). *(Finding F011)*
- **Age extremes** (infants, elderly), **immunocompromise** (HIV), **malaria, malnutrition, anemia, sickle cell disease** — chiefly risk factors for the invasive branch (Section 8/9).

**Host genetic risk factors.** Inborn errors of the **IL-12/IL-23/IFN-γ axis** (Mendelian Susceptibility to Mycobacterial Disease, MSMD; >17 genes) predispose to severe/recurrent NTS. *"Mendelian susceptibility to mycobacterial disease is a rare clinical condition... Other infections such as salmonellosis and candidiasis are also reported"* ([PMID: 28865061](https://pubmed.ncbi.nlm.nih.gov/28865061/)); *"Autosomal recessive complete IL-12Rβ1 deficiency is the most frequent genetic etiology of MSMD"* ([PMID: 29995221](https://pubmed.ncbi.nlm.nih.gov/29995221/)). Relevant genes: **IL12B, IL12RB1, IFNGR1, IFNGR2, STAT1, IL23R**. In mouse models, **Slc11a1 (NRAMP1)** genotype strongly controls Salmonella susceptibility. *(Finding F010)*

**Protective factors.** Intact gastric acid barrier; a healthy, competitive gut microbiota (Section 6); defined-microbiota administration is protective in animal models (Section 15).

**Gene–environment interaction.** Susceptibility emerges from the intersection of host immune-genetic status (IL-12/IFN-γ axis, HIV, hemoglobinopathy) and environmental exposure (ingested dose, acid suppression). This interaction is most consequential for the invasive branch.

---

## 3. Phenotypes

The clinical phenotype is well characterized in pediatric cohorts:

| Phenotype | Frequency | HPO term | Source |
|---|---|---|---|
| Diarrhea | ~95–96% | HP:0002014 | PMID:36449648, 27668899 |
| Fever | ~61–66% | HP:0001945 | PMID:36449648, 27668899 |
| Abdominal pain | ~32–42% | HP:0002027 | PMID:36449648, 27668899 |
| Vomiting | ~34% | HP:0002013 | PMID:27668899 |
| Bloody diarrhea | ~19% | HP:0025085 | PMID:36449648 |
| Dehydration (moderate/severe) | ~16% | HP:0001944 | PMID:27668899 |
| Loss of appetite | ~7% | HP:0004396 | PMID:27668899 |
| Malaise | ~7% | HP:0033834 | PMID:27668899 |
| Elevated CRP / leukocytosis / elevated ESR | common (lab) | HP:0011227 / HP:0001974 | PMID:27668899 |

An Istanbul pediatric cohort (n=172) reported: *"The most common clinical symptoms were diarrhea (n = 166, 96.5%), fever (n = 113, 65.7%) and abdominal pain (n = 73, 42.4%). Bloody diarrhea was seen in 19.2% of patients"* ([PMID: 36449648](https://pubmed.ncbi.nlm.nih.gov/36449648/)). A second cohort (n=67) corroborated: *"The presenting symptoms were diarrhoea (95.5%), fever (61.1%), vomiting (34.3%), abdominal pain (32.8%), loss of appetite (7.4%) and malaise (7.4%)"* ([PMID: 27668899](https://pubmed.ncbi.nlm.nih.gov/27668899/)). *(Finding F015)*

- **Phenotype type:** predominantly symptoms/clinical signs (diarrhea, fever, pain) plus laboratory abnormalities (elevated CRP/ESR, leukocytosis).
- **Age of onset:** any age; pediatric predominance in reported cohorts (median age ~59 months).
- **Severity:** mild-to-moderate and self-limited in immunocompetent hosts; variable.
- **Progression:** acute, episodic, self-limited.
- **Quality of life:** transient; acute illness confines patients for days (dose-dependent bed confinement, Section 8), with generally full recovery. Post-infectious reactive arthritis (Section 11) can cause lasting morbidity.

---

## 4. Genetic/Molecular Information

Salmonella gastroenteritis is **not a Mendelian human genetic disease**, so "causal genes," "pathogenic variants," and germline classification per ACMG do not apply in the standard sense. The biologically meaningful genetics fall into two categories:

**A. Host susceptibility genes.**
- **IL12B, IL12RB1, IFNGR1, IFNGR2, STAT1, IL23R** (MSMD axis) — loss-of-function variants cause severe/disseminated salmonellosis. Documented variants include biallelic **IL12RB1 C291Y** (absent IFN-γ production) and an **IL12B frameshift c.527_528delCT (p.S176Cfs*12)** ([PMID: 29995221](https://pubmed.ncbi.nlm.nih.gov/29995221/)). Functional consequence: loss of IFN-γ–dependent macrophage killing of intracellular *Salmonella*. *(Finding F010)*
- **SLC11A1 (NRAMP1)** — divalent-cation transporter at the phagosomal membrane; genotype controls Salmonella susceptibility in mouse models (multiple *Ity* QTL mapped).
- **HLA-B27** — a major susceptibility allele for the post-infectious complication reactive arthritis (Section 11). *(Finding F004)*

**B. Bacterial virulence genes** (the true "molecular drivers" of disease):
- **SPI-1 (Salmonella Pathogenicity Island 1)** T3SS and effectors **SipA, SipB, SipC, SopB, SopE2** — drive epithelial invasion and inflammation.
- **SPI-2** — intracellular survival/systemic spread.
- Regulators **hilD, hilC, rtsA, hilA** control SPI-1 expression.

No epigenetic host mechanisms, chromosomal abnormalities, or germline/somatic variant frameworks are applicable to this infectious disease.

---

## 5. Environmental Information

**Infectious agent.** *Salmonella enterica* subsp. *enterica*, NTS serovars — chiefly **Typhimurium** and **Enteritidis**; also **S. Choleraesuis** (swine-associated, invasive), **S. Dublin** (cattle-adapted), and reptile-associated serovars (S. Poona, S. Paratyphi B var Java, S. Agbeni, S. Cotham).

**Transmission — zoonotic, fecal-oral.** *"Human infection occurs by fecal-oral transmission through ingestion of contaminated food, milk, or water (inter-human or zoonotic transmission)"* ([PMID: 31321641](https://pubmed.ncbi.nlm.nih.gov/31321641/)). Reptile reservoirs are an increasing source: *"Reptile-associated outbreaks of human Salmonella infections are increasing in Canada, coinciding with a rise in the popularity of reptiles as pets"* ([PMID: 41017027](https://pubmed.ncbi.nlm.nih.gov/41017027/)), with documented pet-turtle→child transmission of S. Poona confirmed by identical genomic fragment patterns. *(Finding F012)*

**Lifestyle/environmental factors.** Consumption of undercooked poultry/eggs, raw dairy, contaminated produce, and contaminated water; contact with reptiles/amphibians and livestock. **Multidrug resistance** is rising (e.g., nalidixic acid resistance 97.67% in a Chinese S. Enteritidis collection).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Ingestion** of *Salmonella* in contaminated food/water → bacteria transit the stomach (gastric acid is a barrier; acid suppression **increases risk**, F011) → **reach the distal ileum, cecum, and colon**.
2. Bacteria access the mucosa via **two portals**: (a) **M cells** of the follicle-associated epithelium over Peyer's patches, via the **GP2–FimH** receptor interaction; and (b) **direct invasion of enterocytes** via the SPI-1 T3SS. → *leads to* epithelial entry.
3. **SPI-1 T3SS** injects effector proteins (**SipA, SopE2, SopB, SipB, SipC**) into host cells → *results in* cytoskeletal rearrangement and bacterial internalization (membrane ruffling/macropinocytosis).
4. **SipB binds and activates caspase-1** → *results in* cleavage of pro-IL-1β to mature IL-1β (inflammasome activation).
5. Effector activity + inflammasome → *drives* **massive neutrophil recruitment** into the cecal/colonic lumen and lamina propria → acute neutrophilic colitis (SPI-1/invA-dependent).
6. **SopB (inositol phosphatase)** activity → *causes* fluid/electrolyte secretion → **secretory-inflammatory diarrhea** (cell death itself is *not required* for enteritis — an inferred but experimentally supported branch point).
7. Host inflammation → *generates* reactive oxygen/nitrogen species that **oxidize luminal thiosulfate to tetrathionate** → *enables* *Salmonella* anaerobic respiration of **ethanolamine** (host-derived) → **luminal growth advantage** over the fermentative microbiota → sustained bloom and transmission. *(Finding F007)*
8. **Branch — invasive (iNTS):** in immunocompromised/susceptible hosts (HIV, malaria, malnutrition, anemia, sickle cell, IL-12/IFN-γ axis defects), bacteria that survive within macrophages (via SPI-2) → *lead to* **bacteremia** (~5% of NTS gastroenteritis) → **extraintestinal focal infection** (~40% of bacteremias): mycotic aortitis, endovascular infection, osteomyelitis, meningitis. *(Findings F008, F013)*

### Detail

**Molecular pathways & effectors (F002).** The SPI-1 T3SS is *"a syringe-like protein injection apparatus that translocates bacterial effector proteins into host cells and is essential for epithelial invasion and early stages of pathogenesis"* ([PMID: 41212225](https://pubmed.ncbi.nlm.nih.gov/41212225/)). An in-vivo neonatal-mouse study showed *"the critical but redundant role of SopE2 and SipA for enterocyte invasion, prerequisite for transcriptional stimulation and mucosal translocation in vivo"* ([PMID: 29522566](https://pubmed.ncbi.nlm.nih.gov/29522566/)). Pharmacologic T3SS inhibition (Xanthotoxol, downregulating *hilD/hilC/rtsA/hilA*) reduces epithelial invasion without affecting bacterial growth.

**Entry portal (F014).** M cells are the avid uptake portal: *"GP2 interacts with FimH, a major component of the type 1 pilus on the outer membrane of a subset of gram-negative enterobacilli such as E. coli and Salmonella enterica"* ([PMID: 21468225](https://pubmed.ncbi.nlm.nih.gov/21468225/)), and RANKL-driven M-cell differentiation confers *"avid uptake of Salmonella and Yersinia organisms"* ([PMID: 19828638](https://pubmed.ncbi.nlm.nih.gov/19828638/)).

**Inflammasome & neutrophils (F003).** *"Large numbers of luminal neutrophils were observed in the ceca of WT-infected, but not in invAmut or ssaRmut infected mice"* ([PMID: 21327114](https://pubmed.ncbi.nlm.nih.gov/21327114/)); *"SipB binds and activates caspase-1, which in turn activates the proinflammatory cytokine interleukin-1beta through cleavage"* ([PMID: 11402005](https://pubmed.ncbi.nlm.nih.gov/11402005/)) — and in bovine ileal loops the *sopB* mutant was attenuated for fluid secretion, showing effectors, not host cell death, drive enteritis.

**Metabolic exploitation of inflammation (F007).** *"By inducing intestinal inflammation, S. Typhimurium sidesteps nutritional competition and gains the ability to use an abundant simple substrate, ethanolamine, which is provided by the host"* ([PMID: 21969563](https://pubmed.ncbi.nlm.nih.gov/21969563/)) — the tetrathionate-respiration mechanism is the mechanistic centerpiece of NTS colonization.

**Suggested ontology terms.** GO biological processes: GO:0006954 (inflammatory response), GO:0044406 (adhesion to host), GO:0052192 (movement in host), GO:0097202 (activation of cysteine-type endopeptidase/caspase-1), GO:0009410 (response to xenobiotic). Cell types (CL): CL:0000584 (enterocyte), CL:0000682 (M cell of gut), CL:0000775 (neutrophil), CL:0000235 (macrophage). Chemical entities (CHEBI): tetrathionate (CHEBI:48889), ethanolamine (CHEBI:16000).

---

## 7. Anatomical Structures Affected

- **Primary organs (Organ level):** distal small intestine (**ileum**, UBERON:0002116), **cecum** (UBERON:0001153), and **colon** (UBERON:0001155) — the digestive system.
- **Secondary/complication organs:** bloodstream, **aorta** (mycotic aortitis, UBERON:0000947), bone (osteomyelitis), meninges (meningitis), gallbladder (carriage), pancreas (rare acute pancreatitis) — in invasive disease.
- **Body systems:** digestive (primary); cardiovascular, skeletal, and nervous (invasive complications); immune.
- **Tissue level:** intestinal **epithelium** (follicle-associated epithelium and villous enterocytes); lamina propria (neutrophil infiltration).
- **Cell populations:** enterocytes (CL:0000584), M cells (CL:0000682), neutrophils (CL:0000775), macrophages (CL:0000235), goblet cells (depleted in colitis).
- **Subcellular compartments (GO CC):** *Salmonella*-containing vacuole (GO:0020005 symbiont-containing vacuole), host plasma membrane (GO:0005886), actin cytoskeleton (GO:0015629), inflammasome (GO:0061702).
- **Localization/lateralization:** bilateral/diffuse mucosal involvement of the distal bowel; not lateralized.

---

## 8. Temporal Development

**Onset.** Acute; incubation period **~6–72 hours** (median ~12–38 h across outbreaks). Dose-dependent: a classic S. Enteritidis outbreak (n=169) showed *"As dose increased, median incubation period decreased (37 h in the low exposure group v. 21 h in the medium exposure group v. 17.5 h in the high exposure group, P = 0.006)"* ([PMID: 8119352](https://pubmed.ncbi.nlm.nih.gov/8119352/)) — with higher doses also producing more vomiting, greater weight loss, more stools, and longer bed confinement. *(Finding F018)*

**Progression & duration.** Self-limited; median duration ~1–5 days (typically 2–3): *"Median incubation period was 19 h (range: 3-26 h). Median duration of illness was 5 days (range: 1-11 days)"* ([PMID: 21824356](https://pubmed.ncbi.nlm.nih.gov/21824356/)). Convalescent fecal shedding can persist for weeks.

**Course pattern.** Acute, episodic, self-limited in immunocompetent hosts. **Critical window for intervention:** early rehydration prevents complications; for invasive disease, early susceptibility-matched antibiotics on day 0–1 improve survival (Section 12).

**Chronic branch (model).** Chronic murine infection produces persistent intestinal fibrosis (TGF-β1, CTGF, IGF-I upregulation; type I collagen deposition peaking day 21, present to day 70) — an inferred correlate of rare human chronic sequelae (F005).

---

## 9. Inheritance and Population

**Epidemiology.** NTS is a leading foodborne diarrheal pathogen. Global estimates place non-typhoidal salmonellosis at **~90+ million gastroenteritis cases/year**. GBD 2021 estimated **509,976 (95%UI 413,361–606,167) incident iNTS cases** in 2021: *"GBD 2021 estimated 509976...incident cases of iNTS worldwide in 2021, with the most cases and highest age-standardized rate (ASR) in Western Sub-Saharan Africa"* ([PMID: 40168434](https://pubmed.ncbi.nlm.nih.gov/40168434/)). Foodborne bacterial pathogens (incl. NTS) caused *"an estimated 364,500 deaths from diarrheal diseases (age-standardized death rate, ASDR 3.63/100,000)"* ([PMID: 42241982](https://pubmed.ncbi.nlm.nih.gov/42241982/)) and 24.6M DALYs in 2021. *(Finding F016)*

**Inheritance.** Not applicable — infectious, not heritable. *Host susceptibility* traits (MSMD axis) follow autosomal-recessive inheritance; HLA-B27 (reactive arthritis) is a co-dominant HLA allele.

**Population demographics.**
- **Age distribution:** skews to young children; iNTS peaks *"early in the second year of life, declining before the age of 3 years"* ([PMID: 40684736](https://pubmed.ncbi.nlm.nih.gov/40684736/)) and in the <1-year group by GBD. Elderly are at high risk of invasive vascular complications.
- **Sex ratio:** slight male predominance in pediatric cohorts (M:F ~55:45).
- **Geographic distribution:** global; invasive burden concentrated in **sub-Saharan Africa and South Asia** (78.7% of DALYs). S. Typhimurium ST313 drives African epidemics.

---

## 10. Diagnostics

**Stool culture** remains the gold standard, increasingly supplemented by **multiplex PCR gastrointestinal panels** (BioFire FilmArray GI, QIAstat-Dx), which detect ~23 pathogens in ~80 minutes with markedly higher yield: *"QGP demonstrated a higher pathogen detection rate (42.3%; 2,033/4,801) than stool culture (12.6%; 255/2,018) and O&P examination (6.3%; 63/986)"* ([PMID: 42153668](https://pubmed.ncbi.nlm.nih.gov/42153668/)), with >98% negative and near-100% positive agreement. In a Saudi pediatric cohort, Salmonella was the most common pathogen detected (22.1%). *(Finding F009)*

| Test | Role | Performance / Note |
|---|---|---|
| Stool culture | Gold standard; enables serotyping & susceptibility | Detection ~12.6% yield; slower |
| Multiplex PCR GI panel | Rapid syndromic diagnosis | 42.3% yield; ~80 min turnaround |
| **Blood culture** | Essential for invasive disease | iNTS *"presentation... is often with fever alone, so clinical diagnosis is impossible without blood culture confirmation"* ([PMID: 30657108](https://pubmed.ncbi.nlm.nih.gov/30657108/)) |
| Inflammatory markers (CRP, ESR, WBC) | Support bacterial etiology | Elevated in bacterial AGE |
| CT angiography / FDG-PET | Detect mycotic aneurysm/endovascular focus | For complicated bacteremia |

**Differential diagnosis:** other bacterial enteritides (Shigella, Campylobacter, STEC, Yersinia), viral gastroenteritis (rotavirus, norovirus), C. difficile, inflammatory bowel disease. Multiplex panels aid discrimination but require clinical correlation given asymptomatic carriage.

---

## 11. Outcome / Prognosis

**Immunocompetent hosts.** Excellent prognosis; self-limited recovery in 2–7 days, negligible mortality.

**Invasive NTS.** High morbidity and mortality. A systematic review of Africa (1966–2014) found *"NTS have been responsible for up to 39% of community acquired blood stream infections in sub-Saharan Africa with an average CFR of 19%"* ([PMID: 28056035](https://pubmed.ncbi.nlm.nih.gov/28056035/)). In DR Congo children <5, *"overall in-hospital case fatality was 25.1% (60/239)"* with 60% extensively drug-resistant ([PMID: 41429348](https://pubmed.ncbi.nlm.nih.gov/41429348/)). *(Findings F008, F013)*

**Complications.**
- **Bacteremia:** ~5% of NTS gastroenteritis; **~40% of bacteremias develop extraintestinal focal infection** — *"Approximately 5% of patients with NTS gastroenteritis develop bacteremia and the incidence of extra-intestinal focal infection in NTS bacteremia is about 40%"* ([PMID: 31321641](https://pubmed.ncbi.nlm.nih.gov/31321641/)). NTS causes ~40% of all infective aortitis; reported fatal cases include ruptured mycotic abdominal aortic aneurysm and aortoesophageal fistula (S. Choleraesuis). *(Finding F013)*
- **Reactive arthritis (post-infectious).** A major sequela strongly linked to HLA-B27: in a hospitalized cohort (n=63), *"HLA-B27 was present in 88%"* ([PMID: 9370874](https://pubmed.ncbi.nlm.nih.gov/9370874/)); in a 592-person outbreak, *"HLA-B27 was present more frequently in those who developed Salmonella infection than in healthy controls (OR 3.0)"* ([PMID: 18528961](https://pubmed.ncbi.nlm.nih.gov/18528961/)). HLA-B27+ patients had higher ESR and were the only ones to develop sacroiliitis; 8/50 progressed to chronic spondyloarthropathy at 5–22 yr follow-up. *(Finding F004)*
- Toxic megacolon/intestinal perforation (pediatric, rare).

**Prognostic factors:** host immune status, age extremes, ingested dose, serovar, antimicrobial susceptibility, presence of endovascular/prosthetic material, severe anemia.

---

## 12. Treatment

**Core principle.** Uncomplicated Salmonella gastroenteritis is managed with **rehydration alone**; antibiotics are **reserved for severe/high-risk cases and invasive disease**. European ESPID/ESPGHAN guidance: *"There is no argument to treat moderate salmonella gastroenteritis or carriage. However, the severe cases and those occurring in high risk patient must be treated (ciprofloxacin or ceftriaxone)"* ([PMID: 19000862](https://pubmed.ncbi.nlm.nih.gov/19000862/)). Antibiotics do not shorten uncomplicated illness and may prolong carriage. *(Finding F017)*

| Treatment | Class / NCIT-type | Indication |
|---|---|---|
| Oral/IV rehydration & electrolytes | Supportive care (NCIT: Fluid Replacement) | All patients — mainstay |
| Ciprofloxacin | Fluoroquinolone (NCIT: Ciprofloxacin) | Severe/high-risk, invasive |
| Ceftriaxone / cefotaxime | 3rd-gen cephalosporin (NCIT: Ceftriaxone) | Severe/invasive, pediatric |
| Azithromycin | Macrolide (NCIT: Azithromycin) | Alternative |
| Subcutaneous IFN-γ | Immunomodulator | MSMD-associated disseminated salmonellosis |

**High-risk groups warranting therapy:** infants <3 months, elderly, immunocompromised (HIV, MSMD), hemoglobinopathy, and patients with prosthetic/endovascular grafts.

**Susceptibility-guided therapy is critical for invasive disease.** In DR Congo children, *"susceptibility-matched third-generation cephalosporin treatment on hospital day 0-1 had better 14-day in-hospital survival"* ([PMID: 41429348](https://pubmed.ncbi.nlm.nih.gov/41429348/)); with extensive drug resistance in 60% of isolates, empiric mismatches worsen outcomes.

No gene, cell, or RNA-based therapies apply. Surgical intervention (graft excision, aneurysm repair) is required for endovascular complications.

---

## 13. Prevention

**Primary prevention centers on food and water safety.** *"Proper food and water treatment, better sanitary facilities, public awareness campaigns, and adherence to food safety laws are all part of prevention measures"* ([PMID: 38021876](https://pubmed.ncbi.nlm.nih.gov/38021876/)). Key measures: safe food handling/cooking (poultry, eggs), pasteurization, hand hygiene, reptile-contact precautions, and One Health surveillance of animal reservoirs and antimicrobial resistance. *(Finding F006)*

**Vaccination.** **No licensed human NTS vaccine exists.** Candidates in preclinical/animal development include:
- Live attenuated strains — e.g., ΔmanA ΔsteD (RAST002): *"Protective efficacy was assessed through challenge studies, demonstrating up to 80% protection against the homologous strain"* ([PMID: 41398587](https://pubmed.ncbi.nlm.nih.gov/41398587/)) (60–80% heterologous).
- Outer-membrane vesicle (OMV) vaccines.
- Probiotic-derived antimicrobial peptides.

**Prevention levels.** Primary — food/water safety, (future) vaccination, gastric-acid preservation (avoid unnecessary PPIs in at-risk patients). Secondary — early rehydration and diagnosis. Tertiary — susceptibility-guided antibiotics and surveillance for endovascular complications in bacteremic patients. Public-health: sanitation, health education, livestock/reptile reservoir control.

---

## 14. Other Species / Natural Disease

Salmonella gastroenteritis is fundamentally **zoonotic**, with broad animal reservoirs.

- **Taxonomy:** *Salmonella enterica* subsp. *enterica* (NCBI txid59201); serovars Typhimurium, Enteritidis, Dublin, Choleraesuis.
- **Reservoir species:** poultry and eggs, cattle, pigs (S. Choleraesuis), and reptiles/amphibians (turtles, snakes, bearded dragons).
- **Natural disease in animals.** **S. Dublin is a cattle-adapted (host-restricted) serovar** causing bovine salmonellosis (systemic disease, abortion, calf enteritis) and serving as a reservoir for human invasive NTS. WGS links human isolates to dairy-cattle isolates and interstate cattle movement ([PMID: 42742664](https://pubmed.ncbi.nlm.nih.gov/42742664/); [PMID: 42308994](https://pubmed.ncbi.nlm.nih.gov/42308994/)). Salmonella is detectable in bovine deep-tissue lymph nodes (~10.8% pooled prevalence) and cow milk (~9.56%), providing zoonotic exposure routes. *(Finding F019)*
- **Comparative pathology:** broad-host-range serovars (Typhimurium, Enteritidis) dominate human sporadic gastroenteritis, whereas host-adapted serovars (Dublin–cattle, Choleraesuis–swine) tend toward invasive disease.
- **Zoonotic transmission:** reptile-associated salmonellosis with serovar-specificity (S. Paratyphi B var Java–snakes; S. Agbeni–turtles; S. Cotham/Chester/Tennessee–bearded dragons) is well documented and rising ([PMID: 41017027](https://pubmed.ncbi.nlm.nih.gov/41017027/)). *(Finding F012)*

---

## 15. Model Organisms

**The streptomycin-pretreated mouse colitis model** is the principal system recapitulating human Salmonella gastroenteritis. Streptomycin pretreatment of C57BL/6 mice before oral S. Typhimurium produces cecal/colonic colonization with acute neutrophilic mucosal inflammation, edema, epithelial damage, and goblet-cell depletion. *(Finding F005)*

- **MyD88 (TLR adaptor)** is required for full mucosal inflammation and drives fibrosis: *"they were impaired in the development of mucosal inflammation"* ([PMID: 22679002](https://pubmed.ncbi.nlm.nih.gov/22679002/)).
- **Chronic model:** *"Infection led to chronic Salmonella colonization of the cecum and colon followed by edema, mucosal ulcerations, and severe transmural inflammation"* ([PMID: 18325390](https://pubmed.ncbi.nlm.nih.gov/18325390/)), with persistent fibrosis.
- **Microbiota protection:** defined microbiota MET-1 protects — *"Infected mice receiving MET-1 lost less weight, had reduced serum cytokines, reduced NF-κB nuclear staining, and decreased neutrophil infiltration in the cecum"* ([PMID: 26531327](https://pubmed.ncbi.nlm.nih.gov/26531327/)) — by preserving tight junctions and reducing systemic translocation without lowering intestinal CFU.

**Other systems:** neonatal mouse (enterocyte invasion, F002); bovine ileal loop (fluid secretion, effector dependence, F003); calf enteritis (S. Dublin); in-vitro Caco-2/Raji M-cell co-culture (M-cell translocation, F014); HeLa/epithelial invasion assays.

**Model types:** mammalian (mouse, calf), cellular/in-vitro (Caco-2/Raji, HeLa). **Genetic models:** MyD88−/−, Slc11a1 (Nramp1) congenic strains, IL-12/IFN-γ axis knockouts.

**Phenotype recapitulation.** The streptomycin mouse reproduces neutrophilic colitis, microbiota disruption, tetrathionate-driven blooming, and (chronically) fibrosis. **Limitations:** requires antibiotic pretreatment (mice are naturally colitis-resistant); the streptomycin model mimics human enterocolitis but not the human-restricted typhoid syndrome; does not fully capture human iNTS host-genetic diversity.

---

## Mechanistic Model / Interpretation

```
 INGESTION (contaminated food/water) ── gastric acid barrier (down by PPIs, F011)
        |
        v
 DISTAL ILEUM / CECUM / COLON
        |
   +----+-----------------------------+
   v                                  v
 M CELLS (GP2-FimH, F014)     ENTEROCYTES (SPI-1 T3SS: SipA/SopE2/SopB, F002)
   |                                  |
   +----------------+-----------------+
                    v
        SipB -> caspase-1 -> IL-1beta (inflammasome, F003)
                    v
        NEUTROPHIL COLITIS + SopB-driven fluid secretion (F003)
                    v
        INFLAMMATION oxidizes thiosulfate -> TETRATHIONATE
                    v
        Salmonella respires ETHANOLAMINE -> LUMINAL BLOOM (F007)
                    v
        INFLAMMATORY-SECRETORY DIARRHEA (self-limited, 2-7 d, F015/F018)
                    |
                    v (susceptible host: HIV/malaria/malnutrition/anemia/SCD/IL-12-IFNg, F008/F010)
        MACROPHAGE SURVIVAL (SPI-2) -> BACTEREMIA (~5%)
                    v
        FOCAL INFECTION (~40%): mycotic aortitis, osteomyelitis, meningitis (F013)
                    |
                    v (post-infectious, HLA-B27, F004)
        REACTIVE ARTHRITIS / spondyloarthropathy
```

The central, distinguishing insight is that *Salmonella* **weaponizes host inflammation**: rather than a bystander, inflammation supplies a unique anaerobic electron acceptor (tetrathionate) and nutrient (ethanolamine) that the pathogen alone can exploit, converting the host defense into a competitive advantage. This "inflammation-as-nutrient-niche" paradigm unifies the invasion (SPI-1), inflammasome, and microbiota-bloom findings into a single coherent narrative and explains why the disease is simultaneously inflammatory and self-limited in immunocompetent hosts, while diverging into a lethal invasive branch when macrophage-based control (IFN-γ axis) fails.

---

## Evidence Base

| PMID | Contribution | Finding |
|---|---|---|
| [35165210](https://pubmed.ncbi.nlm.nih.gov/35165210/) | NTS a leading bacterial diarrheal cause | F001 |
| [39855357](https://pubmed.ncbi.nlm.nih.gov/39855357/) | S. Enteritidis global burden, MDR | F001 |
| [41212225](https://pubmed.ncbi.nlm.nih.gov/41212225/) | SPI-1 T3SS essential for invasion | F002 |
| [29522566](https://pubmed.ncbi.nlm.nih.gov/29522566/) | SopE2/SipA redundant for enterocyte invasion | F002 |
| [21327114](https://pubmed.ncbi.nlm.nih.gov/21327114/) | SPI-1-dependent neutrophil recruitment | F003 |
| [11402005](https://pubmed.ncbi.nlm.nih.gov/11402005/) | SipB-caspase-1-IL-1beta; SopB fluid secretion | F003 |
| [9370874](https://pubmed.ncbi.nlm.nih.gov/9370874/) | HLA-B27 88% in reactive salmonella arthritis | F004 |
| [18528961](https://pubmed.ncbi.nlm.nih.gov/18528961/) | HLA-B27 OR 3.0 for Salmonella infection | F004 |
| [22679002](https://pubmed.ncbi.nlm.nih.gov/22679002/) | MyD88 required for mucosal inflammation | F005 |
| [18325390](https://pubmed.ncbi.nlm.nih.gov/18325390/) | Chronic mouse colitis/fibrosis model | F005 |
| [26531327](https://pubmed.ncbi.nlm.nih.gov/26531327/) | Defined microbiota protection | F005 |
| [41398587](https://pubmed.ncbi.nlm.nih.gov/41398587/) | Live attenuated NTS vaccine 80% efficacy | F006 |
| [38021876](https://pubmed.ncbi.nlm.nih.gov/38021876/) | Prevention: food/water safety | F006 |
| [21969563](https://pubmed.ncbi.nlm.nih.gov/21969563/) | Tetrathionate/ethanolamine bloom | F007 |
| [28056035](https://pubmed.ncbi.nlm.nih.gov/28056035/) | iNTS 39% of BSI, CFR 19% in Africa | F008 |
| [30657108](https://pubmed.ncbi.nlm.nih.gov/30657108/) | iNTS host risk factors; blood culture | F008/F009 |
| [40684736](https://pubmed.ncbi.nlm.nih.gov/40684736/) | iNTS age distribution | F008 |
| [42153668](https://pubmed.ncbi.nlm.nih.gov/42153668/) | Multiplex PCR yield 42.3% vs culture | F009 |
| [28865061](https://pubmed.ncbi.nlm.nih.gov/28865061/) | MSMD-salmonellosis link | F010 |
| [29995221](https://pubmed.ncbi.nlm.nih.gov/29995221/) | IL12RB1 leading MSMD defect | F010 |
| [18054750](https://pubmed.ncbi.nlm.nih.gov/18054750/) | PPI RR 2.9 for bacterial GE | F011 |
| [21999643](https://pubmed.ncbi.nlm.nih.gov/21999643/) | PPIs increase Salmonella susceptibility | F011 |
| [31321641](https://pubmed.ncbi.nlm.nih.gov/31321641/) | Fecal-oral zoonotic transmission; 5% bacteremia | F012/F013 |
| [41017027](https://pubmed.ncbi.nlm.nih.gov/41017027/) | Reptile reservoirs, serovar-specific | F012 |
| [41429348](https://pubmed.ncbi.nlm.nih.gov/41429348/) | iNTS 25.1% CFR; susceptibility-matched Rx | F013/F017 |
| [21468225](https://pubmed.ncbi.nlm.nih.gov/21468225/) | GP2-FimH M-cell uptake | F014 |
| [19828638](https://pubmed.ncbi.nlm.nih.gov/19828638/) | RANKL/M-cell avid uptake | F014 |
| [36449648](https://pubmed.ncbi.nlm.nih.gov/36449648/) | Symptom frequencies (n=172) | F015 |
| [27668899](https://pubmed.ncbi.nlm.nih.gov/27668899/) | Symptom frequencies (n=67) | F015 |
| [40168434](https://pubmed.ncbi.nlm.nih.gov/40168434/) | GBD 2021 iNTS 509,976 cases | F016 |
| [42241982](https://pubmed.ncbi.nlm.nih.gov/42241982/) | Foodborne bacterial mortality burden | F016 |
| [19000862](https://pubmed.ncbi.nlm.nih.gov/19000862/) | Antibiotics reserved for severe/high-risk | F017 |
| [8119352](https://pubmed.ncbi.nlm.nih.gov/8119352/) | Dose-dependent incubation/severity | F018 |
| [21824356](https://pubmed.ncbi.nlm.nih.gov/21824356/) | Incubation ~19h, illness self-limited | F018 |
| [42742664](https://pubmed.ncbi.nlm.nih.gov/42742664/) | S. Dublin human-cattle WGS link | F019 |

---

## Limitations and Knowledge Gaps

1. **Template–disease mismatch.** The disease-characterization template is designed for Mendelian genetic disorders. Sections on causal genes, pathogenic variant classification (ACMG/AMP), inheritance patterns, penetrance, and germline/somatic origin are **not applicable** to an infectious disease and were reframed around host susceptibility and bacterial virulence genetics.
2. **Mechanistic evidence is largely from model organisms.** The SPI-1 invasion, inflammasome, tetrathionate-bloom, and M-cell findings derive chiefly from mouse, calf, and in-vitro models; direct human intestinal mechanistic validation is limited.
3. **Symptom-frequency data** come predominantly from pediatric cohorts (Istanbul, Turkey), which may not generalize to adults or to different serovar distributions.
4. **iNTS burden and CFR** rely on regional African surveillance with heterogeneous diagnostics; global iNTS estimates carry wide uncertainty intervals.
5. **No licensed human vaccine**; efficacy data are preclinical/murine.
6. **Quality-of-life and long-term functional outcome data** (per-phenotype) are sparse for the acute self-limited illness; better characterized only for reactive arthritis sequelae.
7. **Antimicrobial resistance dynamics** (e.g., ST313, 3rd-gen cephalosporin resistance) are evolving rapidly and region-specific.

---

## Proposed Follow-up Experiments / Actions

1. **Human mucosal validation** of the tetrathionate/ethanolamine niche using ex-vivo human intestinal organoids or biopsy-derived enteroids challenged with S. Typhimurium, measuring luminal tetrathionate and ethanolamine-utilization genes.
2. **Prospective adult and mixed-serovar cohorts** to refine symptom frequencies, complication rates, and quality-of-life metrics beyond pediatric data.
3. **Advance NTS vaccine candidates** (RAST002 live-attenuated, OMV) into early-phase human trials, prioritizing sub-Saharan African pediatric populations at highest iNTS risk.
4. **Host-genetic screening study** correlating IL-12/IFN-γ axis variants (IL12RB1, IL12B, IFNGR1/2, STAT1) and SLC11A1 genotypes with invasive-disease risk in prospective iNTS cohorts.
5. **Antimicrobial stewardship & resistance surveillance** integrated with multiplex-PCR diagnostics to guide susceptibility-matched therapy and track ST313 spread.
6. **One Health interventions** targeting the S. Dublin cattle-movement transmission network and reptile reservoirs, using WGS-based source attribution.
7. **Therapeutics targeting the inflammation-niche axis** (e.g., tetrathionate-pathway or SPI-1 T3SS inhibitors such as Xanthotoxol) as anti-virulence adjuncts that reduce microbiota disruption.

---

*Report compiled from 19 confirmed findings across 5 investigation iterations and 94 reviewed papers. Evidence source types span human clinical cohorts/surveillance, model-organism (mouse, calf) experiments, and in-vitro cellular studies, as annotated throughout.*


## Artifacts

- [OpenScientist final report](Salmonella_Gastroenteritis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Salmonella_Gastroenteritis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 36 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 0 |
| Terms whose name was checked | 12 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0052192` (1 mention) - the report calls it "movement in host"; GO calls it **obsolete movement in environment of other organism involved in symbiotic interaction**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0052192` (obsolete movement in environment of other organism involved in symbiotic interaction) (1 mention)
- `GO:0097202` (obsolete activation of cysteine-type endopeptidase activity) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0005950` (2 mentions) - the report calls it "Salmonella gastroenteritis / salmonella food poisoning"; MONDO calls it **Salmonella gastroenteritis**
- `GO:0044406` (1 mention) - the report calls it "adhesion to host"; GO calls it **adhesion of symbiont to host**, and lists "adhesion to host" among its other names
- `GO:0097202` (1 mention) - the report calls it "activation of cysteine-type endopeptidase/caspase-1"; GO calls it **obsolete activation of cysteine-type endopeptidase activity**
- `GO:0009410` (1 mention) - the report calls it "response to xenobiotic"; GO calls it **response to xenobiotic stimulus**
- `CL:0000584` (2 mentions) - the report calls it "enterocyte", "Cell populations:** enterocytes"; CL calls it **enterocyte**, and lists "mature enterocyte" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000584` - called "enterocyte", "Cell populations:** enterocytes"