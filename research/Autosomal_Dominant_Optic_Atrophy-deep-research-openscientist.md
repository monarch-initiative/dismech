---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-10T16:37:18.625331'
end_time: '2026-09-10T16:56:44.374822'
duration_seconds: 1165.75
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Autosomal Dominant Optic Atrophy
  mondo_id: MONDO:0008134
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 28
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 28
  on_topic: 21
  validator_version: 0.2.1
term_validation:
  total_terms: 35
  verified: 31
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 1
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0008134
    reported_labels:
    - if available
    ontology_label: autosomal dominant optic atrophy, classic form
  - term_id: HP:0007766
    reported_labels:
    - RNFL / ganglion-cell-layer thinning (OCT)
    ontology_label: Optic disc hypoplasia
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0000002
    ontology_label: obsolete mitochondrial genome maintenance
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
  path: Autosomal_Dominant_Optic_Atrophy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Autosomal_Dominant_Optic_Atrophy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Optic Atrophy
- **MONDO ID:** MONDO:0008134 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Optic Atrophy** covering all of the
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

# Autosomal Dominant Optic Atrophy (ADOA): A Comprehensive Disease Characterization

**Disease:** Autosomal Dominant Optic Atrophy (ADOA / DOA / Kjer-type optic atrophy)
**MONDO ID:** MONDO:0008134 · **OMIM:** #165500 (OPA1) · **Orphanet:** ORPHA:98673 (isolated DOA), ORPHA:1215 (DOA-plus) · **ICD-10:** H47.2 · **ICD-11:** 9C40.0 · **MeSH:** D029242 (Optic Atrophy, Autosomal Dominant)
**Category:** Mendelian (autosomal dominant mitochondrial optic neuropathy)

---

## Summary

Autosomal Dominant Optic Atrophy is the most common **inherited** optic neuropathy and, together with Leber hereditary optic neuropathy (LHON), one of the two archetypal **mitochondrial** optic neuropathies. It is caused predominantly by heterozygous loss-of-function mutations in **OPA1** (chromosome 3q29), a nuclear gene encoding a dynamin-related GTPase that is imported into mitochondria and anchored in the inner membrane. OPA1 mediates inner-membrane fusion, sculpts the cristae, maintains mitochondrial DNA (mtDNA), supports oxidative phosphorylation, and independently gates apoptosis by keeping cristae junctions tight around sequestered cytochrome *c*. The great majority of pathogenic OPA1 alleles destabilize the transcript and produce **haploinsufficiency** — roughly half-normal OPA1 dosage — which is sufficient to trigger disease. OPA1 accounts for ~60–90% of ADOA; a growing set of additional genes (ACO2, OPA3, SSBP1, WFS1, DNM1L, MFN2) explains the remainder and reflects a shared convergence on mitochondrial biology.

The clinical picture is remarkably stereotyped: bilateral, symmetric, painless, insidious loss of central visual acuity beginning in the first decade of life (median onset ~6 years), accompanied by colour-vision deficits (classically blue-yellow/tritan), centrocecal or paracentral scotomas, and temporal pallor of the optic disc with thinning of the retinal nerve fibre layer. The molecular lesion is expressed in every cell, yet the pathology is exquisitely restricted to **retinal ganglion cells (RGCs)** — specifically the smallest, unmyelinated axons of the papillomacular bundle. This selective vulnerability arises from the peculiar anatomy and energetics of these fibres, whose long unmyelinated prelaminar segments and steep mitochondrial gradient at the lamina cribrosa leave them least able to tolerate a chronic mitochondrial deficit. Disease progression is very slow — a meta-analysis found visual-acuity decline of only 0.022 LogMAR/year, statistically indistinguishable from zero — but the deficit is lifelong and irreversible.

ADOA is genetically dominant with **incomplete penetrance (~88%)** and **highly variable expressivity**, modulated by mtDNA haplotype background (haplogroup J over-represented in some cohorts) and secondary hypomorphic OPA1 alleles. About 20% of OPA1 carriers develop syndromic **"DOA-plus,"** with sensorineural deafness, ataxia, myopathy, peripheral neuropathy, and progressive external ophthalmoplegia; this is enriched for missense/GTPase-domain (dominant-negative) alleles that cause multiple mtDNA deletions in muscle. Minimum point prevalence is ~2.87 per 100,000, with a historically higher figure in Denmark from a founder effect. There is currently **no curative therapy**; management is supportive (low-vision aids, avoidance of mitochondrial toxins, genetic counselling), the neuroprotectant idebenone has shown only limited/mixed effect, and the most advanced disease-specific strategies are **variant-agnostic gene-expression modulation and antisense approaches** targeting OPA1 haploinsufficiency, now entering early-phase human safety evaluation.

---

## Key Findings

### Finding 1 — OPA1 haploinsufficiency is the predominant molecular cause

Heterozygous mutations in **OPA1** (3q29) are the single most frequent molecular cause of DOA, accounting for approximately 60–90% of cases. The centralized OPA1 Variome database registers **516 unique variants across 831 patients** (697 with isolated DOA, 47 with DOA-plus, 83 asymptomatic/unclassified), documenting the breadth of the mutational spectrum. Critically, the dominant mechanism is *loss of dosage rather than a toxic product*: in an international series of probands with bilateral optic atrophy, **76% of pathogenic mutations, observed in 71% of probands, were predicted to yield unstable transcripts and hence haploinsufficiency**. This establishes that a roughly 50% reduction in OPA1 protein is sufficient to precipitate RGC degeneration — a foundation that directly rationalizes gene-augmentation and expression-upregulation therapeutic strategies.

> *"we demonstrated that heterozygous mutations in OPA1 are the most frequent molecular cause of DOA"* — [PMID: 33340656](https://pubmed.ncbi.nlm.nih.gov/33340656/)

> *"76% of pathogenic mutations observed in 30 (71%) of 42 probands were evaluated to lead to unstable transcripts resulting in haploinsufficiency"* — [PMID: 27860320](https://pubmed.ncbi.nlm.nih.gov/27860320/)

> *"now covers a total of 831 patients: 697 with isolated dominant optic atrophy (DOA), 47 with DOA 'plus'… It comprises 516 unique OPA1 variants"* — [PMID: 31500643](https://pubmed.ncbi.nlm.nih.gov/31500643/)

### Finding 2 — OPA1 is a mitochondrial inner-membrane dynamin GTPase controlling fusion, cristae, and apoptosis

OPA1 encodes a **dynamin-related GTPase** imported into mitochondria and localized to the inner membrane and intermembrane space. Alternative splicing of three exons yields multiple isoforms that oligomerize to structure the cristae and mediate fusion of both the inner and outer membranes, thereby shaping the entire mitochondrial network. Beyond fusion, OPA1 supports oxidative phosphorylation, mtDNA maintenance, calcium homeostasis, and apoptosis regulation. Patient-derived fibroblasts carrying heterozygous OPA1 mutations reproducibly display **defective mitochondrial fusion, distorted cristae ultrastructure, and reduced respiratory (complex IV) function** — confirming that the genetic lesion translates into measurable organelle dysfunction in human cells.

> *"OPA1 encodes a dynamin-related GTPase imported into mitochondria and located to the inner membrane and intermembrane space. The many OPA1 isoforms… form complex homopolymers that structure mitochondrial cristae, and contribute to fusion of the outer membrane, thus shaping the whole mitochondrial network."* — [PMID: 33340656](https://pubmed.ncbi.nlm.nih.gov/33340656/)

> *"fibroblasts with heterozygous OPA1 mutations present with several mitochondrial alterations"* — [PMID: 22800932](https://pubmed.ncbi.nlm.nih.gov/22800932/)

*Note:* One study of mitochondria from 16 ADOA patients found respiratory-chain activity largely preserved ([PMID: 18783614](https://pubmed.ncbi.nlm.nih.gov/18783614/)), arguing that the primary defect lies in cristae/fusion architecture rather than a simple bioenergetic block — a nuance reflected in the mechanism section below.

### Finding 3 — DOA-plus (syndromic disease) affects ~20% of carriers via a dominant-negative, mtDNA-instability mechanism

Extra-ocular neurological complications occur in **up to 20% of OPA1 mutation carriers**. In a series of 104 patients from 45 families, the syndromic phenotype comprised sensorineural deafness (typically emerging in late childhood/early adulthood), followed by ataxia, myopathy, peripheral neuropathy, and progressive external ophthalmoplegia from the third decade onward. Genotype strongly modulates this risk: **missense mutations (OR = 3.06, 95% CI 1.44–6.49; P = 0.0027)** and **mutations within the GTPase domain (OR = 2.29, 95% CI 1.08–4.82; P = 0.0271)** confer higher syndromic risk than truncating alleles. Mechanistically, DOA-plus patients harbour **multiple mtDNA deletions in skeletal muscle** with COX-negative ragged-red fibres, revealing a role for OPA1 in mtDNA stability and implicating a **dominant-negative** (not merely haploinsufficient) mode of action for these alleles.

> *"extra-ocular neurological complications are common in OPA1 disease, and affect up to 20% of all mutational carriers"* — [PMID: 20157015](https://pubmed.ncbi.nlm.nih.gov/20157015/)

> *"these patients all harboured multiple deletions of mitochondrial DNA (mtDNA) in their skeletal muscle, thus revealing an unrecognized role of the OPA1 protein in mtDNA stability"* — [PMID: 18158317](https://pubmed.ncbi.nlm.nih.gov/18158317/)

### Finding 4 — Mouse models recapitulate RGC dendropathy and bioenergetic failure; idebenone effect is limited

The heterozygous **B6;C3-Opa1(Q285STOP)** mouse (~50% Opa1 reduction) is the workhorse ADOA model. It shows RGC **dendritic pruning**, reduced synaptic connectivity (decreased PSD-95, loss of glutamatergic synapses in the inner plexiform layer), mitochondrial fragmentation, and impaired respiration (reduced basal, ATP-linked, and reserve capacity in purified RGCs). A randomized, placebo-controlled trial of **idebenone (2000 mg/kg/day; 56 mutant + 63 WT mice)** raised brain ATP by 97.7% (P = 0.035) and transiently improved the optokinetic response (P = 0.003), but produced **no substantive RGC rescue** and increased hepatic oxidative damage (+80.35%, P = 0.011). The model thus validates the RGC-selective, dendrite-first pathology and underscores the limited efficacy of first-generation neuroprotection.

> *"Opa1 deficiency leads to significant fragmentation of mitochondrial morphology, activation of mitochondrial motility and impaired respiratory function in RGCs from the B6; C3-Opa1Q285STOP mouse model"* — [PMID: 32561926](https://pubmed.ncbi.nlm.nih.gov/32561926/)

> *"ATP levels were raised by 0.57 nmol/mg (97.73%, p=0.035) in brain from idebenone-treated Opa1 mutant mice, but in the liver there was an 80.35% (p=0.011) increase in oxidative damage"* — [PMID: 26820596](https://pubmed.ncbi.nlm.nih.gov/26820596/)

> *"We observed decreased levels of postsynaptic density protein 95 in Opa1(+/-) mutant mice consistent with synaptic loss in the inner plexiform layer"* — [PMID: 22300878](https://pubmed.ncbi.nlm.nih.gov/22300878/)

### Finding 5 — Epidemiology: point prevalence ~2.87/100,000 with slow, childhood-onset progression

A population-based study in the north of England established a **minimum point prevalence of 2.87 per 100,000**. OPA1 detection was 57.6% among familial probands versus 14.0% among singletons, and ~64% of DOA families carried an OPA1 mutation. Onset is typically in the first decade (median ~6 years; range 3–24 in a Chinese cohort). A systematic review/meta-analysis of longitudinal biomarkers quantified visual-acuity decline at only **0.022 LogMAR/year (95% CI −0.008 to 0.052; Z = 1.4, p = 0.155)** — not statistically different from zero — confirming an indolent natural history. Denmark historically reports a higher prevalence (~1:10,000) attributed to a founder effect.

> *"The minimum point prevalence of DOA in the north of England was 2.87 per 100,000"* — [PMID: 20417570](https://pubmed.ncbi.nlm.nih.gov/20417570/)

> *"the rate of yearly visual acuity decline (0.022 LogMAR/year… 95% CI: -0.008 to 0.052) was not significantly different from zero (Z = 1.4, p = 0.155)"* — [PMID: 40329928](https://pubmed.ncbi.nlm.nih.gov/40329928/)

### Finding 6 — OCT inner-retinal thinning is the key diagnostic biomarker; missense variants cause worse disease

In a cohort of 108 OPA1-ADOA patients, **spectral-domain OCT** measures of peripapillary retinal nerve fibre layer (pRNFL) and macular ganglion cell layer (mGCL) thickness were the principal structural determinants of visual function: ~0.1 logMAR worsening per 3.2 µm of mGCL loss (P < 0.001); papillomacular-bundle mean-deviation loss of 0.75 dB per µm mGCL (P = 0.002); mGCL thinning with age (−0.06 µm/yr) and over follow-up (−0.26 µm/yr). Genotype stratified severity: **missense variants produced worse acuity (0.83 vs 0.49 logMAR, P = 0.016), worse field mean deviation (−11.48 vs −3.04 dB, P = 0.005), and thinner pRNFL (52.41 vs 66.41 µm, P < 0.001)** than haploinsufficiency variants. The cardinal diagnostic constellation is reduced acuity, colour-vision deficits, centrocecal scotomas, and temporal optic-disc pallor.

> *"Missense variants caused worse VA (0.83 vs. 0.49 logMAR, P = 0.016), MD (-11.48 vs. -3.04 decibel [dB], P = 0.005)… than haploinsufficiency variants"* — [PMID: 41944540](https://pubmed.ncbi.nlm.nih.gov/41944540/)

> *"Their clinical features comprise reduced visual acuity, colour vision deficits, centro-caecal scotomas and optic disc pallor with thinning of the retinal nerve fibre layer"* — [PMID: 37181108](https://pubmed.ncbi.nlm.nih.gov/37181108/)

### Finding 7 — Genetic heterogeneity beyond OPA1

While OPA1 dominates, next-generation sequencing has identified additional DOA genes that converge on mitochondrial function. **ACO2** (aconitase 2) is now "one of the most frequent causes of dominant optic atrophy" (55 patients/37 families; median BCVA 0.46 logMAR). **SSBP1** (p.Arg38Gln) causes DOA-plus-foveopathy with incomplete penetrance. **OPA3** causes autosomal-recessive Costeff syndrome (optic atrophy + 3-methylglutaconic aciduria, ataxia, chorea, spastic paraparesis), near-exclusive to Iraqi-Jewish descent (founder mutation), and rare ADOA. Dominant **WFS1** variants cause optic atrophy with low-frequency sensorineural hearing loss (median optic-atrophy diagnosis age 10 years). Additional genes include **DNM1L** and **MFN2**.

> *"Aconitase 2 (ACO2) gene variants are one of the most frequent causes of dominant optic atrophy (DOA)"* — [PMID: 41954904](https://pubmed.ncbi.nlm.nih.gov/41954904/)

> *"Dominant optic atrophy (DOA) is genetically heterogeneous and most commonly caused by mutations in OPA1"* — [PMID: 34548540](https://pubmed.ncbi.nlm.nih.gov/34548540/)

> *"identification of the disease-causing mutation in the OPA3 gene"* — [PMID: 25201222](https://pubmed.ncbi.nlm.nih.gov/25201222/)

### Finding 8 — No approved therapy; gene-modulation/antisense and neuroprotection lead the pipeline

There is currently **no curative therapy** for ADOA. Strategies span prevention, compensation (neuroprotection), replacement (gene augmentation), and repair. Idebenone (approved for LHON) is being explored in DOA. For ADOA specifically, **antisense therapies targeting OPA1 haploinsufficiency are among the most advanced approaches "currently under human safety evaluation,"** and early-phase trials use variant-agnostic gene-expression modulation. Because a substantial fraction of RGC loss may be developmental, late-stage intervention efficacy could be limited — a key uncertainty for trial design.

> *"Antisense therapies targeting OPA1 haploinsufficiency are among the more advanced ADOA treatments currently under human safety evaluation"* — [PMID: 42101483](https://pubmed.ncbi.nlm.nih.gov/42101483/)

> *"Early phase clinical trials are underway for ADOA caused by variants in the nuclear gene OPA1 using innovative techniques to modulate gene expression in a variant-agnostic manner"* — [PMID: 41318849](https://pubmed.ncbi.nlm.nih.gov/41318849/)

> *"There is currently only one approved treatment and no curative therapy is available"* — [PMID: 37181108](https://pubmed.ncbi.nlm.nih.gov/37181108/)

### Finding 9 — Incomplete penetrance and variable expressivity are modulated by mtDNA background and secondary alleles

Both OPA1-positive and OPA1-negative DOA families exhibit variable expressivity and incomplete penetrance (classically ~88% for OPA1). **Mitochondrial DNA haplotype acts as a genetic modifier**: haplogroup J was three-fold over-represented among OPA1-negative patients. In compound/biallelic cases, a second hypomorphic OPA1 allele "considered asymptomatic by itself" can act as a phenotypic modifier, producing severe early-onset Behr-like disease. Missense/GTPase-domain alleles increase both syndromic risk and structural/functional severity.

> *"Both OPA1-positive and OPA1-negative families exhibit variable expressivity and incomplete penetrance"* — [PMID: 16617242](https://pubmed.ncbi.nlm.nih.gov/16617242/)

> *"haplogroup J was three-fold over-represented in OPA1-negative patients"* — [PMID: 16617242](https://pubmed.ncbi.nlm.nih.gov/16617242/)

> *"the second is considered asymptomatic by itself but has been reported in patients with DOA phenotype and is presumed to act as a phenotypic modifier"* — [PMID: 35741767](https://pubmed.ncbi.nlm.nih.gov/35741767/)

### Finding 10 — Conserved cross-species RGC-selective mitochondrial pathology

Multiple in vivo models reproduce OPA1/Opa1 disease with conserved features. The **zebrafish** Opa1 knockout — the first developmentally viable vertebrate Opa1 KO — and a **Drosophila** model both show reduced survival but viable larvae with impaired visual (not locomotor) function, mitochondrial fragmentation, and disordered cristae in neuronal axons. A naturally occurring/engineered **rhesus macaque** ADOA model has also been reported. Retinal neurons are "particularly sensitive to Opa1 loss," confirming conserved RGC vulnerability.

> *"zebrafish Opa1 KO larvae show impaired visual function but unchanged locomotor function, indicating that retinal neurons are particularly sensitive to Opa1 loss"* — [PMID: 40202868](https://pubmed.ncbi.nlm.nih.gov/40202868/)

> *"mitochondrial fragmentation and disordered cristae organization were observed in neuronal axons in both models highlighting Opa1's highly conserved role in regulating mitochondrial morphology and function in neuronal axons"* — [PMID: 40202868](https://pubmed.ncbi.nlm.nih.gov/40202868/)

### Finding 11 — OPA1 requires balanced proteolytic processing (l-OPA1/s-OPA1); stress tips the balance to fragmentation

Inner-membrane-anchored **long OPA1 (l-OPA1)** is constitutively cleaved by the proteases **YME1L (site S2)** and **OMA1 (site S1)** to yield **short OPA1 (s-OPA1)**; balanced accumulation of both forms maintains fusion. Under mitochondrial stress (membrane depolarization, low ATP), **OMA1 is activated and converts OPA1 completely to short isoforms, inhibiting fusion and triggering fragmentation**. This proteolytic switch is a plausible amplifier that tips already-haploinsufficient RGC mitochondria over the edge, and identifies OMA1 as a candidate therapeutic target.

> *"Constitutive OPA1 cleavage by YME1L and OMA1 at two distinct sites leads to the accumulation of both long and short forms of OPA1 and maintains mitochondrial fusion. Stress-induced OPA1 processing by OMA1 converts OPA1 completely into short isoforms, inhibits fusion, and triggers mitochondrial fragmentation."* — [PMID: 24616225](https://pubmed.ncbi.nlm.nih.gov/24616225/)

> *"Inner membrane-anchored long forms of OPA1 (l-OPA1) are proteolytically processed by the OMA1 or YME1L proteases, acting at cleavage sites S1 and S2, respectively, to produce short forms (s-OPA1)"* — [PMID: 33237841](https://pubmed.ncbi.nlm.nih.gov/33237841/)

### Finding 12 — OPA1 independently gates apoptosis by sequestering cytochrome *c* at cristae junctions

Beyond fusion, OPA1 protects against apoptosis by controlling cristae-junction shape. OPA1 oligomers — of a soluble intermembrane-space form and an integral inner-membrane form — **keep cristae junctions tight, sequestering cytochrome *c*** within the cristae. The pro-apoptotic BID widens junctions and disrupts these oligomers, releasing cytochrome *c*. This anti-apoptotic function is **"genetically and molecularly distinct"** from OPA1's fusion role, and proper processing (e.g., by the rhomboid protease PARL) is required: Parl-/- mitochondria undergo faster cristae remodeling and cytochrome *c* release. Reduced OPA1 therefore lowers the apoptotic threshold of RGCs independently of any fusion defect.

> *"Optic Atrophy 1 (OPA1)… protects from apoptosis by preventing cytochrome c release independently from mitochondrial fusion"* — [PMID: 16839885](https://pubmed.ncbi.nlm.nih.gov/16839885/)

> *"it controls the shape of mitochondrial cristae, keeping their junctions tight during apoptosis. Tightness of cristae junctions correlates with oligomerization of two forms of OPA1"* — [PMID: 16839885](https://pubmed.ncbi.nlm.nih.gov/16839885/)

> *"Parl-/- mitochondria undergo faster apoptotic cristae remodeling and cytochrome c release"* — [PMID: 16839884](https://pubmed.ncbi.nlm.nih.gov/16839884/)

### Finding 13 — RGC selective vulnerability arises from papillomacular-bundle anatomy and energetics

DOA (Kjer disease) and LHON share selective loss of the **smallest RGC axons of the papillomacular bundle**, producing central vision loss. This vulnerability reflects anatomical peculiarities: an asymmetric myelination pattern (long **unmyelinated prelaminar** segments with high metabolic demand) and a **differential mitochondrial gradient at the lamina cribrosa**, together with dependence on axonal transport and cytoskeleton. Importantly, the trigger for RGC loss is "much more complex than a simple bioenergetic crisis," involving mitochondrial network dynamics, mtDNA maintenance, and axonal transport — and is modulated by the local cellular milieu and exogenous factors (e.g., mitochondrial toxins).

> *"Both disorders share striking pathological similarities, marked by the selective loss of retinal ganglion cells (RGCs) and the early involvement of the papillomacular bundle"* — [PMID: 21112411](https://pubmed.ncbi.nlm.nih.gov/21112411/)

> *"the trigger for RGC loss is much more complex than a simple bioenergetic crisis and other important disease mechanisms have emerged relating to mitochondrial network dynamics, mtDNA maintenance, axonal transport, and the involvement of the cytoskeleton in maintaining a differential mitochondrial gradient at sites such as the lamina cribosa"* — [PMID: 21112411](https://pubmed.ncbi.nlm.nih.gov/21112411/)

> *"Selective degeneration of the smallest fibers (papillo-macular bundle) of the human optic nerve occurs in a large number of optic neuropathies characterized primarily by loss of central vision"* — [PMID: 11850115](https://pubmed.ncbi.nlm.nih.gov/11850115/)

---

## Mechanistic Model / Interpretation

### Causal chain (initiating lesion → clinical manifestation)

1. Heterozygous **OPA1** mutation → **~50% reduction in functional OPA1 protein** (haploinsufficiency), or a dominant-negative missense product. *(demonstrated — PMID 27860320, 18158317)*
2. Reduced/mutant OPA1 → **impaired inner-membrane fusion + disordered cristae architecture**. *(demonstrated in patient fibroblasts — PMID 22800932, 33340656)*
3. In parallel, reduced OPA1 → **loosened cristae junctions**, lowering the apoptotic threshold by making cytochrome *c* more releasable — a *fusion-independent* branch. *(demonstrated in vitro — PMID 16839885, 16839884)*
4. For dominant-negative alleles → **mtDNA instability / multiple deletions** in post-mitotic tissue → OXPHOS decline (DOA-plus branch). *(demonstrated in muscle — PMID 18158317)*
5. Metabolic/oxidative stress → **OMA1 activation → complete conversion of l-OPA1 to s-OPA1 → mitochondrial fragmentation** (a stress-gated amplifier). *(demonstrated in vitro; inferred in RGCs — PMID 24616225, 33237841)*
6. Steps 2–5 converge on **energetic + apoptotic vulnerability of RGCs**, most acutely in the **smallest unmyelinated papillomacular-bundle axons** with high metabolic demand and a steep mitochondrial gradient at the lamina cribrosa. *(anatomy demonstrated; RGC mechanism inferred — PMID 21112411, 11850115)*
7. → **RGC dendritic pruning, synaptic loss, and apoptosis**. *(demonstrated in mouse — PMID 22300878, 32561926)*
8. → **Optic-nerve axonal degeneration and RNFL/GCL thinning** → **central visual loss, dyschromatopsia, centrocecal scotoma, temporal disc pallor**. *(demonstrated clinically — PMID 37181108, 41944540)*

```
 OPA1 mutation (3q29, heterozygous)
        │
        ├── LoF / unstable transcript ──► ~50% OPA1 protein (HAPLOINSUFFICIENCY)
        │                                        │
        └── Missense (GTPase/BSE) ──► dominant-negative ──► mtDNA instability (deletions)
                                                 │                     │  (DOA-plus branch)
                                                 ▼                     ▼
                              ┌─────────────────────────────────────────────┐
                              │  Impaired inner-membrane fusion              │
                              │  Disordered cristae architecture             │
                              │  Loosened cristae junctions (↓cyt-c hold)    │
                              │  ↓ OXPHOS reserve                            │
                              └─────────────────────────────────────────────┘
                                                 │
                    metabolic / oxidative stress ─► OMA1 activation
                                                 │  (l-OPA1 → s-OPA1, fragmentation)
                                                 ▼
             SELECTIVE VULNERABILITY of small unmyelinated papillomacular RGC axons
             (high energy demand; mitochondrial gradient at lamina cribrosa)
                                                 │
                 RGC dendritic pruning ► synaptic loss ► apoptosis (cyt-c/caspase)
                                                 │
                    Optic-nerve degeneration ► RNFL/GCL thinning
                                                 │
        Central visual loss · dyschromatopsia · centrocecal scotoma · temporal disc pallor
```

**Upstream vs downstream:** OPA1 dosage/processing is upstream; RGC apoptosis and vision loss are downstream. The apoptotic (cristae-junction) and fusion branches are molecularly distinct; the OMA1 switch is a stress-gated amplifier. **Ontology anchors:** biological processes — mitochondrial fusion (GO:0008053), cristae formation (GO:0042407), OXPHOS (GO:0006119), intrinsic apoptosis (GO:0006915), mtDNA maintenance (GO:0000002); cell type — retinal ganglion cell (CL:0000740); compartments — mitochondrial inner membrane (GO:0005743), cristae (GO:0030061), intermembrane space (GO:0005758); protein — OPA1 (UniProt O60313), OMA1 (Q96E52), YME1L1 (Q96TA2).

---

## Section-by-Section Disease Dossier

### 1. Disease Information
ADOA is a slowly progressive, bilateral, symmetric optic neuropathy caused by selective degeneration of retinal ganglion cells, presenting in childhood with central visual loss, dyschromatopsia, and temporal optic-disc pallor. **Identifiers:** MONDO:0008134; OMIM #165500; Orphanet ORPHA:98673 (isolated), ORPHA:1215 (DOA-plus); ICD-10 H47.2; ICD-11 9C40.0; MeSH D029242. **Synonyms:** Kjer-type optic atrophy, Kjer optic atrophy, dominant optic atrophy (DOA), optic atrophy type 1 (OPA1), autosomal dominant optic atrophy and deafness (DOAD, for DOA-plus). Information here is derived from **aggregated, disease-level resources** (OMIM, Orphanet, the OPA1 Variome of 831 patients/516 variants, and cohort/natural-history studies), not from individual EHR data.

### 2. Etiology
**Primary cause:** heterozygous pathogenic variants in **OPA1** (most commonly haploinsufficiency; missense/GTPase alleles dominant-negative). **Genetic risk factors:** OPA1 causal variants (516 catalogued); additional genes ACO2, OPA3, SSBP1, WFS1, DNM1L, MFN2; modifiers include mtDNA haplogroup (J over-represented in OPA1-negative disease) and secondary hypomorphic OPA1 alleles. **Environmental risk factors / triggers:** because RGC survival is energetically marginal, mitochondrial toxins and stressors (tobacco, alcohol, and drugs impairing OXPHOS) are plausible aggravators, mirroring LHON; formal ADOA-specific evidence is limited. **Protective factors:** none genetically established; avoidance of mitochondrial toxins is prudent. **Gene–environment interaction:** OPA1 dosage sets a low reserve; environmental/metabolic stress (via OMA1 activation) can tip mitochondria into fragmentation (Findings 11, 13).

### 3. Phenotypes
| Phenotype | HPO term | Type | Onset | Severity/Course | Frequency |
|---|---|---|---|---|---|
| Optic atrophy / temporal disc pallor | HP:0000648 | Clinical sign | Childhood | Progressive | ~100% |
| Reduced visual acuity | HP:0007663 | Symptom | 1st decade (median ~6 y) | Mild→severe, very slow | ~100% |
| Colour-vision defect (tritan/blue-yellow) | HP:0000551 / HP:0500020 | Symptom | Childhood | Stable–progressive | Common |
| Centrocecal / central scotoma | HP:0000575 / HP:0030532 | Sign | Childhood | Progressive | Common |
| RNFL / ganglion-cell-layer thinning (OCT) | HP:0007766 | Lab/imaging | Childhood | Progressive | ~100% |
| Sensorineural hearing loss (DOA-plus) | HP:0000407 | Sign | Late childhood/adult | Progressive | Subset of ~20% |
| Progressive external ophthalmoplegia (DOA-plus) | HP:0000590 | Sign | 3rd decade+ | Progressive | DOA-plus |
| Ataxia / myopathy / peripheral neuropathy (DOA-plus) | HP:0001251 / HP:0003198 / HP:0009830 | Signs | Adult | Progressive | DOA-plus |

Incomplete penetrance (HP:0003829, ~88%) and variable expressivity (HP:0003828). **Quality of life:** central-vision loss impairs reading, driving, education/employment, and face recognition; peripheral field is spared, so mobility is often preserved. Many reach low-vision/legal-blindness thresholds but rarely total blindness.

### 4. Genetic/Molecular Information
**Causal gene:** OPA1 (HGNC:8140; NCBI Gene 4976; 3q29; OMIM *605290). **Variant classes:** predominantly loss-of-function (nonsense, frameshift, splice-site) yielding unstable transcripts → haploinsufficiency (~76% of pathogenic alleles); missense (often GTPase/BSE domains) act dominant-negatively. Classification per ACMG/AMP; ClinVar and the OPA1 Variome are primary references (>80% of the 516 variants pathogenic). **Allele frequency:** individually rare in gnomAD (consistent with a Mendelian disease). **Origin:** germline; de novo cases occur. **Functional consequences:** loss of function (haploinsufficiency) and dominant-negative (mtDNA instability). **Modifier genes/alleles:** mtDNA haplogroup; secondary OPA1 hypomorphs. **Other genes:** ACO2, OPA3, SSBP1, WFS1, DNM1L, MFN2. **Chromosomal abnormalities / epigenetics:** not characteristic; no established primary epigenetic driver.

### 5. Environmental Information
No infectious agent. Environmental contribution is limited to mitochondrial-toxic exposures — **tobacco, alcohol, B-vitamin/folate deficiency**, and toxins such as **ethambutol, chloramphenicol, methanol, carbon monoxide, cyanide** — which cause phenocopy optic neuropathies affecting the same papillomacular RGCs and may unmask/aggravate the energetically marginal ADOA phenotype (by analogy to LHON; PMID 11850115, 21112411). CHEBI anchors: ethanol (CHEBI:16236), nicotine (CHEBI:18723), ethambutol (CHEBI:4877).

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model / Interpretation** section above for the full ordered causal chain, branch structure, and ontology anchors. In brief: OPA1 dosage loss → impaired fusion + disordered cristae + lowered apoptotic threshold (+ mtDNA instability for dominant-negative alleles) → stress-gated OMA1 fragmentation → selective papillomacular RGC apoptosis → optic-nerve atrophy → central vision loss.

### 7. Anatomical Structures Affected
**Primary organ:** eye — retina and optic nerve (UBERON:0000970 eye; UBERON:0000966 retina; UBERON:0001791 retinal ganglion cell layer; UBERON:0000941 optic nerve). **Cell/tissue:** retinal ganglion cells (CL:0000740), especially small papillomacular-bundle axons; inner plexiform-layer synapses. **Secondary (DOA-plus):** cochlea/auditory nerve, cerebellum, skeletal muscle, peripheral nerve, extraocular muscles. **Subcellular:** mitochondrion (inner membrane/cristae/intermembrane space). **Lateralization:** bilateral and symmetric.

### 8. Temporal Development
**Onset:** childhood/first decade (median ~6 y; range early childhood–adult), insidious/chronic. **Progression:** very slow and progressive, often plateauing; acuity decline ~0.022 LogMAR/yr (not significantly different from zero). **Course:** chronic, lifelong, irreversible; largely non-remitting (occasional stepwise worsening). DOA-plus features emerge later (deafness in late childhood; PEO/ataxia from the 3rd decade). **Critical period:** a developmental component of RGC loss suggests earliest intervention may be most effective (relevant to gene-therapy timing).

### 9. Inheritance and Population
**Prevalence:** ~2.87/100,000 (north England, minimum); higher in Denmark (~1:10,000, founder effect). **Inheritance:** autosomal dominant (OPA1); rare AR/biallelic forms cause severe Behr-like disease. **Penetrance:** incomplete (~88%), age-dependent. **Expressivity:** highly variable. **Modifiers:** mtDNA haplogroup J; secondary OPA1 alleles. **Anticipation:** not a repeat-expansion disorder; not characteristic. **Founder effects:** Danish (OPA1); Iraqi-Jewish (OPA3/Costeff). **Sex ratio:** roughly equal, no strong bias. **Detection:** OPA1 found in 57.6% of familial vs 14.0% of singleton probands. **Age distribution:** presents in childhood, diagnosed across the lifespan.

### 10. Diagnostics
**Ophthalmic/functional:** best-corrected visual acuity; colour vision (tritan defect); automated perimetry (central/centrocecal scotoma); fundoscopy (temporal disc pallor). **Imaging biomarker:** SD-OCT peripapillary RNFL and macular ganglion-cell-layer thinning — the key structural biomarker (~0.1 logMAR per 3.2 µm mGCL loss; missense alleles thinner pRNFL 52 vs 66 µm). **Electrophysiology:** pattern VEP (delayed/reduced), PERG (RGC dysfunction). **Genetic testing:** OPA1 sequencing + MLPA for large rearrangements, then a multigene hereditary-optic-neuropathy panel / WES for ACO2, OPA3, SSBP1, WFS1, DNM1L, MFN2; mtDNA testing to exclude LHON. **Differential diagnosis:** LHON (mtDNA m.11778/m.3460/m.14484; often subacute, male, central scotoma), WFS1/Wolfram (arcuate defects, later onset), POLG, glaucoma, and compressive/toxic/nutritional optic neuropathies. ADOA shows the greatest peripapillary RNFL thinning of the optic-atrophy syndromes.

### 11. Outcome/Prognosis
**Survival:** normal life expectancy in isolated DOA; DOA-plus adds neuromuscular morbidity. **Visual outcome:** slowly progressive, moderate-to-severe bilateral central impairment; legal blindness in a subset; total blindness rare; peripheral field usually preserved; recovery is not expected. **Morbidity:** central-vision disability affecting reading/driving/education. **Prognostic factors:** variant class (missense/GTPase → worse acuity, fields, RNFL), degree of GCL/RNFL thinning, age, and DOA-plus status. **Prognostic biomarker candidate for trials:** macular GCL thickness.

### 12. Treatment
**No curative therapy.** **Supportive/rehabilitative:** low-vision aids, occupational support, avoidance of mitochondrial toxins (tobacco/alcohol/toxic drugs), genetic counselling; audiology/neurology for DOA-plus (NCIT: supportive care C15277). **Pharmacotherapy/neuroprotection:** **idebenone** (benzoquinone electron carrier/antioxidant; NCIT:C61637; approved in LHON) explored in DOA with limited/mixed effect (mouse trial: transient optokinetic improvement, no major RGC recovery). **Advanced/experimental (most promising):** **variant-agnostic OPA1 gene-expression modulation and antisense oligonucleotide** approaches targeting haploinsufficiency, now in early-phase human safety evaluation; AAV gene augmentation, gene editing, and stem-cell optic-nerve regeneration in preclinical development. **Personalized medicine:** genotype (missense vs LoF) informs prognosis and potentially therapy selection.

### 13. Prevention
No primary prevention (Mendelian). **Secondary:** OCT-based early detection; cascade genetic testing of at-risk relatives. **Reproductive/genetic screening:** genetic counselling; prenatal/preimplantation genetic testing for known familial variants. **Counselling:** 50% transmission risk per offspring; counsel on incomplete penetrance, variable expressivity, and DOA-plus risk for missense/GTPase alleles. **Tertiary:** low-vision rehabilitation, avoid mitochondrial stressors, manage DOA-plus complications. No immunization applicable.

### 14. Other Species / Natural Disease
OPA1 is deeply conserved. Orthologues: mouse *Opa1* (NCBI Gene 74143), zebrafish *opa1* (30129), *Drosophila* *Opa1-like*. Engineered/model disease exists in mouse (*Mus musculus*, Taxon 10090), zebrafish (*Danio rerio*, 7955), fruit fly (*Drosophila melanogaster*, 7227), and a **rhesus macaque** (*Macaca mulatta*, 9544) ADOA model. Naturally occurring companion-animal ADOA is not a recognized veterinary entity; models are experimental. The mitochondrial fusion/cristae mechanism is evolutionarily conserved (PMID 40202868). Not zoonotic.

### 15. Model Organisms
| Model | Type | Key phenotype recapitulated | Limitation | Resource |
|---|---|---|---|---|
| B6;C3-Opa1(Q285STOP) mouse | Heterozygous KO (mammalian) | RGC dendropathy, synaptic (PSD-95) loss, mitochondrial fragmentation, impaired respiration | Modest, slow visual deficit | MGI |
| Zebrafish opa1 KO | Vertebrate KO | Impaired visual (not locomotor) function, axonal mitochondrial fragmentation/cristae disorder | Reduced survival; developmental | ZFIN |
| Drosophila Opa1 | Invertebrate | Conserved axonal mitochondrial pathology, reduced respiration | Anatomical divergence from human eye | FlyBase |
| Rhesus macaque | Primate ADOA model | Human-like ocular anatomy, translational | New/limited characterization | — |
| Patient fibroblasts | In vitro (human) | Fusion defect, cristae distortion, complex IV reduction | Non-neuronal | — |

**Recapitulation/limitations:** models reproduce degenerative RGC/mitochondrial pathology and RGC-selective vulnerability, but the slow, variable human phenotype and the possible developmental RGC-loss component are captured imperfectly.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [33340656](https://pubmed.ncbi.nlm.nih.gov/33340656/) | OPA1 as leading cause; protein biology | Review (human) |
| [27860320](https://pubmed.ncbi.nlm.nih.gov/27860320/) | Haploinsufficiency in 76% of pathogenic alleles | Human cohort |
| [31500643](https://pubmed.ncbi.nlm.nih.gov/31500643/) | OPA1 Variome: 516 variants, 831 patients | Database |
| [22800932](https://pubmed.ncbi.nlm.nih.gov/22800932/) | Fusion/cristae/complex-IV defects in patient fibroblasts | In vitro (human) |
| [18783614](https://pubmed.ncbi.nlm.nih.gov/18783614/) | OXPHOS often preserved → structural not bioenergetic primacy | In vitro (human) |
| [20157015](https://pubmed.ncbi.nlm.nih.gov/20157015/) | DOA-plus ~20%; missense/GTPase risk ORs | Human cohort |
| [18158317](https://pubmed.ncbi.nlm.nih.gov/18158317/) | mtDNA deletions → dominant-negative mechanism | Human tissue |
| [32561926](https://pubmed.ncbi.nlm.nih.gov/32561926/) | Mouse RGC bioenergetic/morphological phenotype | Mouse |
| [22300878](https://pubmed.ncbi.nlm.nih.gov/22300878/) | RGC synaptic/dendritic pathology (PSD-95) | Mouse |
| [26820596](https://pubmed.ncbi.nlm.nih.gov/26820596/) | Idebenone RCT — limited/mixed effect | Mouse RCT |
| [20417570](https://pubmed.ncbi.nlm.nih.gov/20417570/) | Prevalence 2.87/100,000; OPA1 detection rates | Epidemiology |
| [40329928](https://pubmed.ncbi.nlm.nih.gov/40329928/) | Slow natural history (0.022 LogMAR/yr) | Meta-analysis |
| [41944540](https://pubmed.ncbi.nlm.nih.gov/41944540/) | OCT biomarker; missense-vs-LoF severity | Human cohort |
| [37181108](https://pubmed.ncbi.nlm.nih.gov/37181108/) | Clinical features; no curative therapy | Review |
| [41954904](https://pubmed.ncbi.nlm.nih.gov/41954904/) | ACO2 as major DOA gene | Human cohort |
| [34548540](https://pubmed.ncbi.nlm.nih.gov/34548540/) | SSBP1; genetic heterogeneity | Human cohort |
| [25201222](https://pubmed.ncbi.nlm.nih.gov/25201222/) | OPA3/Costeff syndrome | Human cohort |
| [16617242](https://pubmed.ncbi.nlm.nih.gov/16617242/) | Penetrance/expressivity; mtDNA haplogroup J modifier | Human cohort |
| [35741767](https://pubmed.ncbi.nlm.nih.gov/35741767/) | Secondary OPA1 allele as phenotypic modifier | Case series |
| [40202868](https://pubmed.ncbi.nlm.nih.gov/40202868/) | Zebrafish/Drosophila conserved RGC pathology | Model organisms |
| [24616225](https://pubmed.ncbi.nlm.nih.gov/24616225/) | YME1L/OMA1 processing; stress fragmentation | In vitro |
| [33237841](https://pubmed.ncbi.nlm.nih.gov/33237841/) | S1/S2 cleavage; s-OPA1 roles | In vitro |
| [16839885](https://pubmed.ncbi.nlm.nih.gov/16839885/) | Fusion-independent anti-apoptotic role | In vitro |
| [16839884](https://pubmed.ncbi.nlm.nih.gov/16839884/) | PARL processing required for cristae/apoptosis control | In vitro (mouse) |
| [21112411](https://pubmed.ncbi.nlm.nih.gov/21112411/) | RGC/papillomacular selective vulnerability; multifactorial | Review |
| [11850115](https://pubmed.ncbi.nlm.nih.gov/11850115/) | Smallest-fibre papillomacular degeneration | Review |
| [42101483](https://pubmed.ncbi.nlm.nih.gov/42101483/) | Antisense/haploinsufficiency-targeting therapy | Review |
| [41318849](https://pubmed.ncbi.nlm.nih.gov/41318849/) | Variant-agnostic gene-modulation trials | Review |

**Converging vs challenging evidence:** Findings are strongly convergent across human cohorts, patient cells, and multiple animal models. The main internal tension is between the fusion/cristae paradigm (Findings 2, 11, 12) and the observation that whole-cell OXPHOS can be preserved in ADOA patient mitochondria ([PMID: 18783614](https://pubmed.ncbi.nlm.nih.gov/18783614/)); this is reconciled by localizing the deficit to cristae architecture, apoptotic priming, and the *energetically marginal* papillomacular RGC axon rather than a global respiratory block.

---

## Supported and Refuted Hypotheses

**Supported:**
1. OPA1 haploinsufficiency is the predominant cause of ADOA (PMID 27860320, 31500643, 33340656).
2. OPA1 dysfunction acts via impaired mitochondrial fusion/cristae → RGC bioenergetic failure and apoptotic priming (PMID 33340656, 22800932, 32561926, 16839885).
3. Missense/GTPase (dominant-negative) alleles cause more severe and syndromic disease via mtDNA instability (PMID 20157015, 18158317, 41944540).
4. Penetrance/expressivity are modified by mtDNA background and secondary alleles (PMID 16617242, 35741767).
5. The OMA1/YME1L proteolytic balance is a stress-gated amplifier of fragmentation (PMID 24616225, 33237841).

**Refuted / nuanced:**
- The hypothesis that OPA1 mutations cause disease chiefly by directly impairing electron transport was **not supported** in one patient study (electron transport unaltered; pathology attributed to structure/fusion role) — favouring the cristae/fusion + apoptotic-priming mechanism (PMID 18783614).

---

## Limitations and Knowledge Gaps

- **Developmental vs degenerative RGC loss is unresolved.** If much RGC loss is developmental, post-symptomatic gene therapy may have a narrow therapeutic window — a pivotal uncertainty for trial design (Finding 8).
- **No human therapeutic efficacy data yet.** Idebenone benefit in ADOA is inferred from LHON and mouse data; ADOA-specific RCTs are lacking. Antisense/gene-modulation approaches are only at the safety-evaluation stage.
- **Penetrance/modifier biology is incompletely mapped.** The mechanistic basis of ~88% penetrance, mtDNA haplogroup effects, and secondary-allele modifiers is correlational, not causally dissected.
- **Prevalence is likely under-ascertained.** The 2.87/100,000 figure is a *minimum*; incomplete penetrance and mild cases inflate the true carrier frequency.
- **Environmental triggers are hypothesized, not quantified** for ADOA specifically (extrapolated from LHON).
- **OMA1 as a drug target** (Finding 11) is mechanistically attractive but untested in ADOA models.
- **Literature-based synthesis** without primary patient-level data; frequencies are cohort-dependent.

---

## Proposed Follow-up Experiments / Actions

1. **Test OMA1 inhibition** (genetic or pharmacological) in Opa1+/- mouse and zebrafish models to determine whether blocking the stress-fragmentation switch preserves RGCs — a targeted extension of Findings 11 and 4.
2. **Define the developmental window** using conditional/inducible Opa1 knockdown at defined postnatal ages to quantify how much RGC loss is developmental vs adult-onset, informing gene-therapy timing.
3. **Genotype-stratified natural-history/OCT study** contrasting missense/GTPase vs LoF alleles longitudinally to build a prognostic model with macular GCL thickness as endpoint (extends Findings 6, 9).
4. **AAV-OPA1 gene augmentation and antisense upregulation** dose-ranging in the rhesus macaque model (human-like eye) as a bridge to clinical trials.
5. **mtDNA-haplogroup modifier study** in large OPA1 cohorts (cybrid experiments) to establish causality for haplogroup J and identify protective backgrounds (extends Finding 9).
6. **Cristae-junction/apoptosis-targeted neuroprotection** (e.g., stabilizing OPA1 oligomers or blocking cytochrome *c* release) tested in RGCs, exploiting the fusion-independent branch (Finding 12).
7. **Systematic ADOA drug-toxicity registry** to quantify environmental/pharmacological aggravators and generate evidence-based avoidance guidance (extends Finding 13).

---

*Report compiled from 13 confirmed findings and 46 reviewed papers across five investigation iterations. Evidence types are labelled (human clinical, model organism, in vitro, database/computational). All quotations are verbatim from the cited abstracts.*


## Artifacts

- [OpenScientist final report](Autosomal_Dominant_Optic_Atrophy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Autosomal_Dominant_Optic_Atrophy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 28 |
| On topic | 21 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 6 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008134` (3 mentions) - the report calls it "if available"; MONDO calls it **autosomal dominant optic atrophy, classic form**
- `HP:0007766` (1 mention) - the report calls it "RNFL / ganglion-cell-layer thinning (OCT)"; HP calls it **Optic disc hypoplasia**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0000002` (obsolete mitochondrial genome maintenance) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000648` (1 mention) - the report calls it "Optic atrophy / temporal disc pallor"; HP calls it **Optic atrophy**
- `HP:0000407` (1 mention) - the report calls it "Sensorineural hearing loss (DOA-plus)"; HP calls it **Sensorineural hearing impairment**, and lists "Sensorineural hearing loss" among its other names
- `HP:0000590` (1 mention) - the report calls it "Progressive external ophthalmoplegia (DOA-plus)"; HP calls it **Progressive external ophthalmoplegia**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `ORPHA:98673` - called "isolated DOA", "isolated"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
