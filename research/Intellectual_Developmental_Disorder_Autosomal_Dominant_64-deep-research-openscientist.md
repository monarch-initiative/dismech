---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-19T08:00:02.431210'
end_time: '2026-10-19T08:29:03.629639'
duration_seconds: 1741.2
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: ZNF292-Related Neurodevelopmental Disorder (Intellectual Developmental
    Disorder, Autosomal Dominant 64)
  mondo_id: MONDO:0030934
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
citation_count: 3
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 32
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 7
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0030934
    reported_labels:
    - Mondo
    ontology_label: intellectual developmental disorder, autosomal dominant 64
  - term_id: DOID:0061037
    reported_labels:
    - Disease Ontology
    ontology_label: autosomal dominant intellectual developmental disorder 64
  - term_id: UBERON:0002264
    reported_labels:
    - ventral telencephalon / medial ganglionic eminence
    ontology_label: olfactory bulb
  - term_id: CL:0000617
    reported_labels:
    - Cell types involved:** GABAergic cortical interneurons
    ontology_label: GABAergic neuron
  labels_variant: 6
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Intellectual_Developmental_Disorder_Autosomal_Dominant_64-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Intellectual_Developmental_Disorder_Autosomal_Dominant_64-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ZNF292-Related Neurodevelopmental Disorder (Intellectual Developmental Disorder, Autosomal Dominant 64)
- **MONDO ID:** MONDO:0030934 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ZNF292-Related Neurodevelopmental Disorder (Intellectual Developmental Disorder, Autosomal Dominant 64)** covering all of the
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

# ZNF292-Related Neurodevelopmental Disorder (Intellectual Developmental Disorder, Autosomal Dominant 64 / MRD64)

**Comprehensive Disease Characteristics Report**
**MONDO:0030934 · OMIM #619188 · Orphanet ORPHA:178469 · Category: Mendelian (autosomal dominant)**

---

## Summary

ZNF292-related neurodevelopmental disorder — formally **Intellectual Developmental Disorder, Autosomal Dominant 64 (MRD64; OMIM #619188)** — is a rare Mendelian condition caused by heterozygous, predominantly *de novo* **loss-of-function (truncating) variants in ZNF292**, a highly conserved C2H2 zinc-finger transcription factor on chromosome 6q14.3. The disorder was delineated as a discrete entity by Mirzaa and colleagues in 2020 from a cohort of 28 families, and the gene-disease relationship is now curated as **Definitive** by ClinGen/GenCC. The operative disease mechanism is **haploinsufficiency**: ZNF292 is among the most loss-of-function–intolerant genes in the human genome (gnomAD pLI = 1.0, LOEUF = 0.16), so a single inactivating allele is sufficient to cause disease.

Clinically, MRD64 is dominated by a neurodevelopmental triad — **intellectual disability/global developmental delay (~96%), speech and language delay (~93%), and autism spectrum disorder features (~55–70%)** — accompanied by a variable set of features including motor delay/hypotonia, ADHD, seizures, short stature, nonspecific facial dysmorphism, ocular abnormalities, feeding difficulties, and nonspecific brain MRI findings (e.g., ventriculomegaly). The condition has **low clinical recognizability** — there is no distinctive syndromic gestalt — so diagnosis is essentially molecular, achieved through trio exome/genome sequencing or multi-gene ID/ASD panels. Variants cluster in the large terminal exon 8, escape nonsense-mediated decay, and are predicted to produce a stable truncated protein.

Mechanistic work in human pluripotent stem-cell (hPSC)-derived cortical interneuron models (Kaushik et al., *Cell Reports* 2025) shows that ZNF292 exerts **stage-specific transcriptional control over GABAergic interneuron development**: it restrains differentiation genes in progenitors and promotes maturation genes in neurons. Its loss causes precocious progenitor differentiation, impaired interneuron maturation, altered ion-channel activity, elevated GABA responsiveness, and neuronal hyperactivity — pointing toward an **excitatory/inhibitory (E/I) imbalance** as the proximate cause of the neurodevelopmental phenotype. There is **no targeted or curative therapy**; management is entirely supportive and manifestation-based. Recurrence risk for siblings of a *de novo* proband is low (~1%, from possible parental germline mosaicism), while an affected individual has a 50% transmission risk.

---

## 1. Disease Information

**Overview.** MRD64 is an autosomal dominant intellectual developmental disorder characterized by mildly to severely impaired intellectual development with prominent speech delay, frequently accompanied by autism spectrum disorder. It was formally defined by **Mirzaa et al., 2020** (*De novo and inherited variants in ZNF292 underlie a neurodevelopmental disorder with features of autism spectrum disorder*, *Genet Med* 22(3):538–546; [PMID: 31723249](https://pubmed.ncbi.nlm.nih.gov/31723249/); DOI 10.1038/s41436-019-0693-9).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | **#619188** (Intellectual developmental disorder, autosomal dominant 64) |
| OMIM (gene) | *616213 (ZNF292) |
| Mondo | **MONDO:0030934** |
| Orphanet | ORPHA:178469; ORPHA:528084 |
| Disease Ontology | DOID:0061037 |
| HGNC | HGNC:18410 |
| NCBI Gene | 23036 |
| Ensembl | ENSG00000188994 |
| MANE Select transcript | NM_015021.3 (ENST00000369577.8) |
| Cytoband | 6q14.3 (GRCh38 chr6:87,155,565–87,265,943) |
| ICD-11 / MeSH | No gene-specific code; coded under broad "disorders of intellectual development" / ASD categories; MeSH uses the gene term ZNF292 |

**Synonyms / alternative names.** MRD64; ZNF292-related neurodevelopmental disorder; ZNF292-related intellectual disability. Gene aliases: Zn-15, Zn-16, ZFP292, KIAA0530.

**Information source.** Derived largely from **aggregated disease-level resources and published patient cohorts** (OMIM, Orphanet, ClinVar/DECIPHER/DDD, and primary case series) rather than individual EHR records. The foundational cohort is the 28-family series of Mirzaa 2020, supplemented by later case reports and a 2026 series of 8 individuals ([PMID: 42650143](https://pubmed.ncbi.nlm.nih.gov/42650143/)).

---

## 2. Etiology

**Disease causal factors.** The cause is **genetic and monogenic**: heterozygous loss-of-function variants in *ZNF292*. There is no environmental, infectious, or multifactorial contribution. In the defining cohort, **27 of 28 families carried *de novo* variants** and 1 was inherited from a mildly affected mother (Mirzaa 2020, [PMID: 31723249](https://pubmed.ncbi.nlm.nih.gov/31723249/)).

**Genetic risk factors.** The causal variants themselves are the risk factor — predominantly frameshift and nonsense truncating variants. ZNF292 is **extraordinarily loss-of-function–intolerant** (gnomAD pLI = 1.0, LOEUF = 0.16; DECIPHER %HI = 26.56), so a single inactivating allele confers disease. No separate susceptibility loci or validated modifier genes have been established.

**Environmental risk factors.** None identified. Advanced parental age is a general (nonspecific) contributor to *de novo* mutation burden but has not been specifically linked to MRD64.

**Protective factors.** No genetic or environmental protective factors are known. The presence of 5 predicted-LoF ZNF292 variants in gnomAD population controls, and a family with an unaffected transmitting father of three affected siblings, suggests **rare incomplete penetrance**, implying that unknown genetic/stochastic modifiers can buffer the phenotype — but no specific protective allele has been identified.

**Gene–environment interactions.** No established GxE interactions. The disorder is a cell-autonomous developmental consequence of ZNF292 dosage reduction.

---

## 3. Phenotypes

The core phenotype is a neurodevelopmental triad with variable syndromic add-ons. Feature frequencies below derive primarily from the Mirzaa 2020 cohort (n = 28 families) and later series.

| Phenotype | HPO term | Frequency | Type |
|---|---|---|---|
| Intellectual disability / global developmental delay | HP:0001249 / HP:0001263 | ~96% | Cognitive |
| Delayed speech & language development | HP:0000750 | ~93% | Cognitive/behavioral |
| Autistic behavior / ASD | HP:0000729 | ~55–70% (≈61%) | Behavioral |
| Motor delay / hypotonia | HP:0001252 | ≥30% | Clinical sign |
| ADHD | HP:0007018 | Variable | Behavioral |
| Seizures / epilepsy | HP:0001250 | Variable minority | Clinical sign |
| Brain MRI abnormality (e.g., ventriculomegaly) | HP:0002119 | Variable | Imaging |
| Microcephaly | HP:0000252 | Minority | Physical |
| Short stature | HP:0004322 | Variable–high* | Physical |
| Feeding difficulties | HP:0011968 | Variable | Clinical sign |
| Constipation | HP:0002019 | Variable | Clinical sign |
| Strabismus / nystagmus | HP:0000486 / HP:0000639 | Minority | Clinical sign |
| Facial dysmorphism (thin upper lip, smooth philtrum, upturned nasal tip, synophrys, epicanthus, prominent forehead) | — | Nonspecific | Physical |

\*A 2026 series of 8 individuals ([PMID: 42650143](https://pubmed.ncbi.nlm.nih.gov/42650143/)) found **short stature in all 8**, suggesting growth failure may be more consistent than previously appreciated. Importantly, IGF-1 is typically normal, distinguishing this from growth hormone deficiency.

**Phenotype characteristics.**
- **Age of onset:** congenital/neurodevelopmental; delays recognized in infancy to early childhood.
- **Severity:** variable (mild to severe).
- **Progression:** stable/static — a non-progressive (static) encephalopathy; features are lifelong but do not degenerate.
- **Expressivity:** highly variable even for identical recurrent variants (see Section 9).

**Quality-of-life impact.** Lifelong cognitive, communicative, and behavioral impairment produces substantial effects on daily functioning, educational attainment, and independence. No disease-specific QoL instrument (EQ-5D/SF-36/PROMIS) data exist; impact is inferred from the ID/ASD phenotype.

---

## 4. Genetic / Molecular Information

**Causal gene.** *ZNF292* (OMIM *616213; HGNC:18410; NCBI Gene 23036; Ensembl ENSG00000188994), 6q14.3. Encodes a 2,192-amino-acid, ~156 kDa Krüppel C2H2-type zinc-finger transcription factor with **15–16 C2H2 zinc fingers**, N-terminal tandem TFIIIA-type fingers, long C-terminal linkers enabling cooperative DNA binding, 2–3 nuclear localization signals, and coiled-coil domains. UniProt **O60281** (ZN292_HUMAN); AlphaFold model AF-O60281-F7; InterPro IPR013087 / Pfam PF00096 (zf-C2H2). Paralog: RLF.

**Pathogenic variants.**
- **Classification:** Pathogenic / Likely Pathogenic truncating variants per ACMG/AMP. ClinVar holds roughly **44 pathogenic + 54 likely pathogenic** alleles; DECIPHER/DDD lists >13 P/LP entries.
- **Variant type/class:** Predominantly **frameshift and nonsense** (truncating). In Mirzaa 2020: 24 distinct heterozygous nonsense/frameshift variants across 28 patients — **19 frameshift + 7 nonsense (26 of 28)** residing in **terminal exon 8**, plus 1 *de novo* frameshift in exon 4 and 1 *de novo* nonsense in exon 2.
- **NMD escape:** Exon 8 encodes all 16 C2H2 zinc-finger domains (~85% of the coding sequence). Because variants fall in the last exon, they **largely escape nonsense-mediated decay** and produce a stable truncated protein (RT-PCR confirmed stable transcript from both alleles).
- **Recurrent variants:** c.3066_3069delAAGA (p.Glu1022AspfsTer3; NM_015021.2; ClinVar Variation ID 431106, Pathogenic); and c.6160_6161del (p.Glu2054Lysfs*14), now the most frequently observed variant (7 individuals across unrelated families, [PMID: 42650143](https://pubmed.ncbi.nlm.nih.gov/42650143/)). Newer variants include c.4189C>T (p.Arg1397Ter), c.6343C>T (p.Arg2115Ter), c.1533del (p.Ile511Metfs*11), c.3094dup (p.Ser1032Phefs*18), c.5977_5978del (p.Gln1993fs).
- **Allele frequency:** All but one variant absent from gnomAD v2.1; variants are private/ultra-rare.
- **Origin:** **Germline**, overwhelmingly *de novo*. (Somatic ZNF292 mutations occur in gastric/colorectal cancer and CLL — a separate, non-germline tumor-suppressor context, not MRD64.)
- **Functional consequence:** **Loss of function via haploinsufficiency.**

**Modifier genes.** None validated. Incomplete penetrance in rare families implies unidentified modifiers.

**Epigenetic information.** **No validated ZNF292-specific DNA-methylation episignature** exists in the published record (not part of the EpiSign classifier).

**Chromosomal abnormalities.** Whole-gene **6q14.3 deletions encompassing ZNF292** have been reported in ASD cohorts; detectable by chromosomal microarray.

---

## 5. Environmental Information

- **Environmental factors:** None implicated. MRD64 is a purely genetic, cell-autonomous developmental disorder.
- **Lifestyle factors:** Not applicable.
- **Infectious agents:** Not applicable.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **heterozygous truncating variant** in *ZNF292* (frameshift/nonsense, usually in terminal exon 8) arises *de novo* in the germline → **leads to** a transcript that largely **escapes nonsense-mediated decay**.
2. NMD escape **results in** a **stable truncated ZNF292 protein** lacking normal function; combined with the normal allele this **produces haploinsufficiency** (ZNF292 is pLI = 1.0 / LOEUF = 0.16, i.e., dosage-sensitive). *[Loss of function is the demonstrated mechanism; whether the truncated protein also exerts a dominant-negative effect is not established — inferred open question.]*
3. Reduced functional ZNF292 dosage in the developing forebrain **disrupts stage-specific transcriptional programs** that ZNF292 normally governs (ZNF292 is a nuclear DNA-binding TF, GO:0005634 nucleus; biological process GO:0006355 regulation of transcription).
4. **Branch A — progenitors (medial ganglionic eminence / ventral telencephalon, UBERON:0002264):** ZNF292 normally **restrains** differentiation, neuronal morphogenesis/axon-guidance, and synapse/ion-channel genes (direct targets including NKX2.1, ASCL1, SATB1, WNT5B). Its loss **up-regulates** these targets → **precocious differentiation** of GABAergic interneuron progenitors.
5. **Branch B — maturing neurons (cortical interneurons, CL:0000617 GABAergic interneuron):** ZNF292 normally **promotes** interneuron maturation genes (including other NDD genes). Loss reduces ZNF292 genome-wide binding and **down-regulates** these targets → **compromised interneuron maturation/function**.
6. These converge to **altered ion-channel activity, elevated GABA responsiveness, and neuronal hyperactivity** → **excitatory/inhibitory (E/I) imbalance** in cortical circuits.
7. Disrupted GABAergic interneuron development and E/I imbalance **result in** the clinical phenotype: intellectual disability, speech/language delay, autism spectrum features, and variable epilepsy/ADHD. *[The link from stem-cell phenotypes to human clinical features is inferred, not directly demonstrated in patients.]*

```
ZNF292 truncating variant (exon 8)
        │ escapes NMD
        ▼
 Stable truncated protein → HAPLOINSUFFICIENCY (pLI 1.0)
        │ reduced TF dosage in developing forebrain
        ▼
  ┌─────────────────────────┬──────────────────────────┐
  │ PROGENITORS (MGE)        │ MATURING INTERNEURONS     │
  │ ZNF292 normally represses│ ZNF292 normally activates │
  │ differentiation genes    │ maturation genes          │
  │ → UP-regulated on loss   │ → DOWN-regulated on loss  │
  │ → precocious differentn. │ → impaired maturation     │
  └─────────────┬────────────┴──────────────┬────────────┘
                ▼                            ▼
   altered ion channels · ↑GABA response · neuronal hyperactivity
                         │
                         ▼
              Excitatory/Inhibitory IMBALANCE
                         │
                         ▼
        ID · speech delay · ASD · (epilepsy/ADHD)
```

### Detail by category

- **Molecular pathways / cellular processes:** Transcriptional regulation of neural differentiation and synaptogenesis. ZNF292 binding sites are enriched for **bHLH, homeodomain, and Ets** transcription-factor motifs, indicating cooperative transcriptional networks. Processes: neuron differentiation (GO:0030182), interneuron migration/maturation, synapse formation, ion-channel organization.
- **Protein dysfunction:** Loss of function of a C2H2 zinc-finger DNA-binding protein; truncation removes/disrupts the zinc-finger DNA-binding array encoded by exon 8.
- **Cell types involved:** GABAergic cortical interneurons (CL:0000617), interneurons (CL:0000099), and neuronal stem/progenitor cells (CL:0000047), originating in the medial ganglionic eminence.
- **Biochemical/electrophysiological abnormality:** Altered ion-channel activities, elevated GABA responsiveness, and neuronal hyperactivity in ZNF292-deficient interneurons.
- **Molecular profiling evidence:** Genome-wide ZNF292 occupancy plus transcriptomics in CRISPRi-knockdown hPSC-derived MGE-like NPCs (D15) and cortical interneurons (D30) (Kaushik et al., *Cell Reports* 2025 May 27;44(5):115597; [PMID: 40257863](https://pubmed.ncbi.nlm.nih.gov/40257863/)). Human ZNF292 expression peaks ~12 weeks post-conception and continues lifelong.
- **Evolutionary/functional context:** ZNF292 is the human ortholog of rat Zn-15 / mouse Zn-16, originally characterized as a **growth-hormone-gene transcriptional activator cooperating with POU1F1/Pit-1 (GHF-1)** — a plausible (inferred) link to the short-stature phenotype via the GH axis.

**Upstream vs downstream:** The mutation and haploinsufficiency are the most upstream events; transcriptional dysregulation of interneuron programs is intermediate; altered channel physiology, GABAergic hyperexcitability, and E/I imbalance are downstream; clinical neurodevelopmental features are the terminal manifestation.

---

## 7. Anatomical Structures Affected

- **Primary organ/system:** Brain / central nervous system — UBERON:0000955 (brain), UBERON:0000956 (cerebral cortex); developmental origin UBERON:0002264 (ventral telencephalon / medial ganglionic eminence). Body system: **nervous system**.
- **Tissue/cell level:** Nervous tissue; GABAergic interneurons (CL:0000617), interneurons (CL:0000099), neuronal progenitors (CL:0000047).
- **Subcellular level:** Nucleus (GO:0005634); ZNF292 localizes to nucleus/nucleoplasm/nuclear membrane and acts as a DNA-binding transcription factor.
- **Secondary / variable involvement:** Endocrine (pituitary/GH axis → short stature; UBERON:0000007 pituitary gland), musculoskeletal (short stature, hypotonia), visual system (strabismus/nystagmus; UBERON:0000970 eye), digestive system (feeding difficulties, constipation; UBERON:0001555 digestive tract), occasional cardiac involvement.
- **Lateralization:** Bilateral / systemic — not lateralized.

---

## 8. Temporal Development

- **Onset:** Congenital/neurodevelopmental; delays recognized in infancy to early childhood. Onset pattern is **chronic/insidious** (developmental), not acute.
- **Progression:** **Static (non-progressive)** encephalopathy — features are stable and lifelong rather than degenerative.
- **Disease course:** Chronic, lifelong.
- **Remission:** No spontaneous remission; developmental gains occur with intervention but underlying impairment persists.
- **Critical periods:** The vulnerable window is prenatal/early-postnatal corticogenesis (ZNF292 expression peaks ~12 weeks post-conception), when interneuron specification and maturation occur — the putative window for any future intervention.

---

## 9. Inheritance and Population

- **Inheritance pattern:** **Autosomal dominant** (OMIM #619188), predominantly *de novo* (27/28 families in Mirzaa 2020). Rare transmitted cases exist (1 family, variant from a mildly affected mother).
- **Penetrance:** High but **not complete** — 5 predicted-LoF ZNF292 variants in gnomAD controls and one unaffected transmitting father of three affected siblings indicate rare non-penetrance.
- **Expressivity:** **Highly variable** — the recurrent c.6160_6161del (p.Glu2054Lysfs*14) produces presentations from severe global DD to mild neurodevelopmental impairment ([PMID: 42650143](https://pubmed.ncbi.nlm.nih.gov/42650143/)).
- **Anticipation / germline mosaicism:** No anticipation (not a repeat-expansion disorder). Parental germline mosaicism is the basis for the low (~1%) sibling recurrence risk in *de novo* cases.
- **Founder effects / consanguinity / carrier frequency:** None — dominant, mostly *de novo*; carrier screening not applicable.
- **Epidemiology:** No dedicated Orphanet prevalence or life-expectancy estimate; recently described and rare.
- **Demographics:** No strong sex bias established; no ethnic or geographic clustering reported. Age distribution: diagnosed in childhood.

Feature frequencies (n = 28): DD/ID 96%; speech delay 93%; ASD/autistic features ~61%; ADHD, tone abnormalities, structural brain abnormalities, dysmorphism, ocular features, and growth failure each in ≥30%.

---

## 10. Diagnostics

- **Primary approach:** Molecular — diagnosis is **sequencing-driven** given low clinical recognizability. Trio **exome sequencing (ES)**, **genome sequencing (WGS)**, or multi-gene **ID/ASD NGS panels**, with Sanger confirmation of *de novo* status in proband and parents (Mirzaa 2020, [PMID: 31723249](https://pubmed.ncbi.nlm.nih.gov/31723249/); 2026 series used WES in 8 unrelated individuals finding 7 *de novo* variants, [PMID: 42650143](https://pubmed.ncbi.nlm.nih.gov/42650143/)). ZNF292 is a strong candidate in exome-negative idiopathic DD/ID/ASD.
- **Chromosomal microarray (CMA):** Detects 6q14.3 deletions encompassing ZNF292.
- **Biomarkers / labs:** No specific biomarker or metabolic test. IGF-1 is typically **normal** (distinguishes from GH deficiency despite short stature).
- **Imaging:** Brain MRI findings are nonspecific (ventriculomegaly, variable).
- **Electrophysiology:** No disease-specific EEG protocol; standard epilepsy workup applies when seizures occur.
- **Omics diagnostics / episignature:** No validated DNA-methylation episignature.
- **Clinical criteria:** No formal diagnostic criteria; molecular confirmation defines the diagnosis.
- **Differential diagnosis:** Low syndromic recognizability — distinguish from other monogenic ID/ASD causes, childhood apraxia of speech/oral-motor apraxia/velopharyngeal insufficiency, Noonan syndrome (ZNF292 lacks cardiac defects/typical facies), GH deficiency (normal IGF-1 in ZNF292), and Turner syndrome (via karyotype/CMA).
- **Screening:** Not part of newborn or carrier screening panels; cascade testing recommended given rare inherited cases and incomplete penetrance.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** No evidence of reduced life expectancy; not a life-limiting condition per se (no disease-specific mortality data).
- **Morbidity / function:** Lifelong cognitive, communicative, and behavioral disability is the main burden; degree correlates with ID severity.
- **Disease course:** Static (non-progressive); developmental progress achievable with intervention.
- **Complications:** Seizures, ADHD, feeding/growth issues, and ophthalmologic problems when present.
- **Prognostic factors:** Severity of baseline ID, presence of epilepsy, and access to early intervention; no validated molecular prognostic biomarker (genotype–phenotype correlation is weak, given variable expressivity of recurrent variants).
- **Quality of life:** No disease-specific QoL measures published.

---

## 12. Treatment

**There is no disease-specific, targeted, or curative therapy.** Management is **supportive and multidisciplinary**, directed at individual manifestations:

- **Developmental / rehabilitative:** Early intervention, special education, **speech-language therapy** (NCIT: Speech Therapy), occupational therapy, physical therapy.
- **Behavioral:** ASD behavioral therapy; ADHD management.
- **Pharmacotherapy (symptomatic):** Standard antiseizure medications for epilepsy; ADHD pharmacotherapy as indicated. No pharmacogenomic considerations specific to ZNF292.
- **Monitoring:** Growth/feeding surveillance; ophthalmologic monitoring (strabismus/nystagmus).
- **Advanced / experimental therapeutics:** None approved or in trials specific to ZNF292 (no gene, cell, or RNA-based therapy).
- **Personalized medicine:** Not yet applicable beyond molecular diagnosis.

NCIT suggestions where applicable: Speech Therapy, Occupational Therapy, Physical Therapy, Behavioral Therapy, Supportive Care.

---

## 13. Prevention

- **Primary prevention:** None possible (de novo genetic etiology; no environmental cause).
- **Secondary/tertiary prevention:** Early developmental intervention and surveillance for complications (seizures, growth, vision) mitigate functional impact.
- **Genetic counseling:** For a proband with a *de novo* variant, sibling recurrence risk is low (~1%, from possible parental germline mosaicism); an affected individual has a **50% transmission risk** (AD). Variable expressivity and rare incomplete penetrance should be discussed.
- **Prenatal / preimplantation testing:** PGT-M and prenatal diagnosis are possible once a familial variant is identified.
- **Screening programs / immunization / public health:** Not applicable; not part of newborn or carrier screening.

---

## 14. Other Species / Natural Disease

- **Orthologs (DIOPT):** Mouse *Zfp292* (MGI:1353423; NCBI Gene 30046; chr4; aliases Zn-15/Zn-16/Zfp-15/Krox-10; score 16/16); rat *Zfp292* (RGD 11811932; 14/14); zebrafish duplicates *znf292a* (ZFIN ZDB-GENE-071004-18) and *znf292b* (ZFIN ZDB-GENE-030131-9559; best fish ortholog 13/15). **No Drosophila ortholog** — the gene is vertebrate-restricted (1 human, 1 mouse, 1 rat, 2 zebrafish).
- **Natural disease in other species:** No naturally occurring ZNF292-related disease has been catalogued (no OMIA entry noted).
- **Comparative biology:** The rat Zn-15 / mouse Zn-16 ortholog was characterized as a growth-hormone-gene transcriptional activator cooperating with Pit-1/POU1F1 — evolutionarily conserved transcriptional function.
- **Transmission / zoonosis:** Not applicable.

---

## 15. Model Organisms

- **Principal disease model:** **Human pluripotent stem-cell (hPSC)-derived cortical interneuron systems** using CRISPRi (dCas9-KRAB) knockdown to model haploinsufficiency (Kaushik et al., *Cell Reports* 2025; [PMID: 40257863](https://pubmed.ncbi.nlm.nih.gov/40257863/)). These differentiate to MGE-like ventral telencephalic NPCs (D15) and cortical interneurons (D30) and recapitulate haploinsufficiency-driven differentiation/maturation defects and GABAergic hyperexcitability.
- **Mouse resources:** IMPC/MGI lists ~75 alleles (gene-trap, targeted, endonuclease-mediated) across 151 strains, but **no published ZNF292-disease-specific mouse study recapitulating MRD64** was identified.
- **Model limitations:** Stem-cell models capture cell-autonomous developmental and electrophysiological phenotypes but not whole-organism behavior, cognition, or systemic (e.g., growth) features; no validated behavioral animal model exists.
- **Resources:** MGI, IMPC, ZFIN, RGD, Cellosaurus/ATCC (for hPSC lines).

---

## Mechanistic Model / Interpretation

The data converge on a coherent model in which **ZNF292 is a dosage-sensitive master transcriptional regulator of cortical GABAergic interneuron development**. Its defining genetic feature — truncating variants in terminal exon 8 that escape NMD — is unusual in that it produces a *stable* truncated protein, yet the functional and population-genetic evidence (pLI = 1.0, LOEUF = 0.16) indicate the operative mechanism is **loss of function through haploinsufficiency** rather than a classic degraded null. Whether the truncated protein additionally exerts a dominant-negative effect remains an open, testable question.

Functionally, ZNF292 acts in a **stage-dependent, bidirectional manner**: a transcriptional brake on differentiation genes in progenitors, and an activator of maturation genes in neurons. Removing one allele's worth of this regulator simultaneously accelerates progenitor exit (precocious differentiation) and impairs the maturation program, yielding interneurons with altered ion-channel profiles, exaggerated GABA responses, and network hyperactivity. The downstream clinical correlate — **E/I imbalance** — is a recurring theme across monogenic ID/ASD/epilepsy disorders and plausibly links the molecular lesion to the ID–speech-delay–autism triad and the variable epilepsy/ADHD.

The **weak genotype–phenotype correlation** (identical recurrent variants producing severe-to-mild phenotypes) and **rare incomplete penetrance** argue that genetic background and stochastic developmental factors substantially shape outcome — a key consideration for counseling and for any future precision approach.

---

## Evidence Base

| PMID | Study | Type | Contribution |
|---|---|---|---|
| [31723249](https://pubmed.ncbi.nlm.nih.gov/31723249/) | Mirzaa et al., *Genet Med* 2020;22(3):538–546 | Human clinical cohort (28 families) | Defines MRD64; establishes *de novo* truncating LoF variants clustered in exon 8, NMD escape, AD inheritance, core phenotype frequencies |
| [40257863](https://pubmed.ncbi.nlm.nih.gov/40257863/) | Kaushik et al., *Cell Reports* 2025;44(5):115597 | hPSC / CRISPRi model + genomics | Stage-specific transcriptional control of cortical interneurons; precocious differentiation, impaired maturation, GABAergic hyperexcitability, direct targets and motif enrichment |
| [42650143](https://pubmed.ncbi.nlm.nih.gov/42650143/) | 2026 series (8 individuals) | Human clinical series | Expands phenotype (short stature in all 8), recurrent c.6160_6161del with variable expressivity, WES diagnostic yield |

Supporting resource-level evidence: OMIM #619188 / *616213; gnomAD constraint metrics (pLI 1.0, LOEUF 0.16); ClinGen/GenCC Definitive classification; ClinVar (~44 P + ~54 LP alleles); UniProt O60281; DIOPT ortholog scores; MGI/IMPC allele catalogs.

---

## Limitations and Knowledge Gaps

1. **No animal model of the disease** recapitulating MRD64 — the mechanism rests heavily on a single hPSC/CRISPRi study; in vivo validation of E/I imbalance and behavioral correlates is lacking.
2. **LoF vs. dominant-negative** — stable truncated protein raises the possibility of a dominant-negative or neomorphic contribution that has not been experimentally excluded.
3. **Weak genotype–phenotype correlation and incomplete penetrance** — modifiers are unidentified; prognosis prediction is limited.
4. **Epidemiology is unquantified** — no prevalence, incidence, sex ratio, or natural-history/survival data; cohorts are small.
5. **Short stature mechanism** — the GH-axis link (via the ortholog's role with POU1F1/Pit-1) is suggestive but unproven in patients; IGF-1 is normal.
6. **No biomarker or episignature** — diagnosis depends entirely on sequencing; no functional confirmatory assay.
7. **No therapeutics pipeline** — no targeted, gene, or RNA-based therapy exists or is in trials.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a conditional *Zfp292* mouse (and/or zebrafish) model** to test interneuron developmental defects, E/I balance, seizure susceptibility, cognition/social behavior, and growth in vivo.
2. **Distinguish LoF from dominant-negative mechanism** by comparing heterozygous knockout vs. truncation knock-in in isogenic hPSC lines and in vivo models.
3. **Establish a patient registry / natural-history study** to quantify prevalence, feature frequencies, genotype–phenotype correlations, and long-term outcomes; standardize QoL/functional measures.
4. **Characterize the GH-axis/short-stature link** (endocrine profiling across a larger cohort; test ZNF292 regulation of GH/POU1F1 targets in relevant cell types).
5. **Search for modifiers of penetrance/expressivity** via genome-wide analysis in discordant carriers (e.g., the unaffected transmitting father and mildly affected relatives).
6. **Evaluate E/I-rebalancing pharmacology** (e.g., agents modulating GABAergic hyperexcitability) in the hPSC interneuron model as a therapeutic-hypothesis screen.
7. **Assess for a DNA-methylation episignature** across a larger patient set to determine whether a confirmatory epigenetic classifier is feasible.

---

*Report compiled from 11 confirmed findings across 5 investigation iterations. Evidence sources span human clinical cohorts (Mirzaa 2020; 2026 series), an in vitro hPSC/CRISPRi functional-genomics study (Kaushik 2025), and curated resource databases (OMIM, gnomAD, ClinGen/GenCC, ClinVar, UniProt, MGI/IMPC, DIOPT).*


## Artifacts

- [OpenScientist final report](Intellectual_Developmental_Disorder_Autosomal_Dominant_64-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Intellectual_Developmental_Disorder_Autosomal_Dominant_64-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 17 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030934` (2 mentions) - the report calls it "Mondo"; MONDO calls it **intellectual developmental disorder, autosomal dominant 64**
- `DOID:0061037` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **autosomal dominant intellectual developmental disorder 64**
- `UBERON:0002264` (2 mentions) - the report calls it "ventral telencephalon / medial ganglionic eminence"; UBERON calls it **olfactory bulb**
- `CL:0000617` (3 mentions) - the report calls it "Cell types involved:** GABAergic cortical interneurons"; CL calls it **GABAergic neuron**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000750` (1 mention) - the report calls it "Delayed speech & language development"; HP calls it **Delayed speech and language development**
- `HP:0000729` (1 mention) - the report calls it "Autistic behavior / ASD"; HP calls it **Autistic behavior**, and lists "Autistic behaviors" among its other names
- `HP:0001252` (1 mention) - the report calls it "Motor delay / hypotonia"; HP calls it **Hypotonia**, and lists "Central hypotonia" among its other names
- `HP:0001250` (1 mention) - the report calls it "Seizures / epilepsy"; HP calls it **Seizure**, and lists "Seizures" among its other names
- `HP:0002119` (1 mention) - the report calls it "Brain MRI abnormality (e.g., ventriculomegaly)"; HP calls it **Ventriculomegaly**
- `GO:0005634` (2 mentions) - the report calls it "Subcellular level:** Nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.