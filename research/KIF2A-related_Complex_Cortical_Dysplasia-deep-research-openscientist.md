---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-13T20:17:36.022551'
end_time: '2026-10-13T20:47:01.577377'
duration_seconds: 1765.55
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: KIF2A-related Complex Cortical Dysplasia
  mondo_id: MONDO:0014170
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
citation_count: 13
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 10
  validator_version: 0.3.0
term_validation:
  total_terms: 34
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 2
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0014170
    reported_labels:
    - MONDO
    ontology_label: complex cortical dysplasia with other brain malformations 3
  - term_id: HP:0001339
    reported_labels:
    - Lissencephaly (agyria/pachygyria, posterior-predominant)
    ontology_label: Lissencephaly
  - term_id: NCIT:C15296
    reported_labels:
    - Rehabilitation Therapy
    ontology_label: Isolated Chemotherapeutic Perfusion
  - term_id: NCIT:C15277
    reported_labels:
    - Supportive Care
    ontology_label: Mastectomy
  labels_variant: 5
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: KIF2A-related_Complex_Cortical_Dysplasia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: KIF2A-related_Complex_Cortical_Dysplasia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** KIF2A-related Complex Cortical Dysplasia
- **MONDO ID:** MONDO:0014170 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **KIF2A-related Complex Cortical Dysplasia** covering all of the
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

# KIF2A-related Complex Cortical Dysplasia (CDCBM3): Comprehensive Disease Dossier

**Disease:** KIF2A-related Complex Cortical Dysplasia / Cortical Dysplasia, Complex, with Other Brain Malformations 3 (CDCBM3)
**MONDO:** MONDO:0014170 · **OMIM:** #615411 · **Category:** Mendelian (autosomal dominant)
**Causal gene:** *KIF2A* (HGNC:6318; NCBI Gene 3796; UniProt O00139; chromosome 5q12.1)
**Evidence base:** Human clinical case reports/series, model-organism (mouse, zebrafish) studies, and in vitro/computational structural analyses. No disease-specific patient dataset was provided; this report is literature-derived.

---

## Summary

KIF2A-related Complex Cortical Dysplasia (CDCBM3; **OMIM #615411**, **MONDO:0014170**) is an **ultra-rare, autosomal dominant malformation of cortical development (MCD)** caused by predominantly *de novo* heterozygous missense variants in *KIF2A*, the gene encoding a **kinesin-13 family ATP-dependent microtubule depolymerase**. Pathogenic variants cluster in the kinesin **motor / ATP-nucleotide-binding domain (NBD)**, with recurrent *de novo* hotspots at residues **Ser317 and His321** (e.g., p.Ser317Asn, p.His321Pro/Asp) and p.Gly318Arg. These variants impair ATP hydrolysis and the microtubule-depolymerizing function of KIF2A, derailing the microtubule-dependent processes that build the cerebral cortex ([PMID: 23603762](https://pubmed.ncbi.nlm.nih.gov/23603762/); [PMID: 27747449](https://pubmed.ncbi.nlm.nih.gov/27747449/); [PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/)).

The core clinical phenotype is a **posterior-predominant lissencephaly / agyria–pachygyria** almost indistinguishable from LIS1-related lissencephaly, accompanied by **congenital and postnatal microcephaly** (up to −5 SD in ~75% of patients), **severe motor and cognitive impairment**, **absent or limited speech**, and **drug-resistant epilepsy**; clinical involvement is largely restricted to the central nervous system and facial dysmorphism. Variant position along the protein predicts severity, defining a graded "**KIF2A syndrome**": NBD variants → severe CDCBM3; motor-domain-but-outside-NBD variants → epilepsy; variants outside the motor domain → autism spectrum ([PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/); [PMID: 37488893](https://pubmed.ncbi.nlm.nih.gov/37488893/)).

There is **no disease-specific or curative therapy**. Diagnosis is made by trio whole-exome/whole-genome sequencing plus brain MRI, and management is symptomatic (antiseizure medication plus developmental/rehabilitative support). Inheritance is autosomal dominant with nearly all variants arising *de novo*; recurrence risk is low but non-zero owing to documented **parental germline mosaicism** (e.g., KIF2A p.G440R in two affected brothers) ([PMID: 35315043](https://pubmed.ncbi.nlm.nih.gov/35315043/); [PMID: 37331001](https://pubmed.ncbi.nlm.nih.gov/37331001/)). Disease mechanism is strongly supported by a conditional knock-in mouse bearing the human p.His321Asp variant, which recapitulates microcephaly, neuroanatomical anomalies, behavioral deficits and epilepsy susceptibility, showing increased apoptosis and abnormal multipolar-to-bipolar transition of migrating neurons ([PMID: 31919497](https://pubmed.ncbi.nlm.nih.gov/31919497/)).

---

## Key Findings

### Finding 1 — *KIF2A* is the causal gene; *de novo* motor-domain missense variants cluster around the ATP pocket

CDCBM3 is a rare autosomal dominant syndrome caused by heterozygous *KIF2A* variants. Recurrent *de novo* missense mutations target residues around the ATP nucleotide-binding pocket of the kinesin motor domain, notably hotspots **Ser317 and His321** (e.g., p.Ser317Asn, p.His321Pro/Asp) and **p.Gly318Arg**. These recur as *de novo* events, are typically **absent from gnomAD/1000 Genomes (ACMG PM2)** and are predicted deleterious. As stated in the literature, *"Cortical dysplasia, complex, with other brain malformations 3 (CDCBM3) is a rare autosomal dominant syndrome caused by Kinesin family Member 2A (KIF2A) gene mutation"* ([PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/)), and *"the identification of mutations only in the residues Ser317 and His321 suggests these are hotspots for de novo mutations"* ([PMID: 27747449](https://pubmed.ncbi.nlm.nih.gov/27747449/)). A rare recurrence mechanism is parental germline mosaicism: *"Findings in this case also suggest a rare parental germline mosaicism of KIF2A G440R"* ([PMID: 37331001](https://pubmed.ncbi.nlm.nih.gov/37331001/)).

### Finding 2 — Pathogenic variants impair microtubule depolymerization, increasing apoptosis and disrupting the multipolar-to-bipolar transition

A conditional knock-in mouse bearing the human **KIF2A p.His321Asp** missense variant showed microcephaly, neuroanatomical anomalies, behavioral deficits, and epilepsy susceptibility — faithfully recapitulating the human phenotype. Mechanistically, *"the expression of the p.His321Asp pathogenic variant increases apoptosis and causes abnormal multipolar to bipolar transition in newborn neurons,"* and *"the observed cellular phenotypes are likely to be linked to deficiency in the microtubule depolymerizing function of KIF2A"* ([PMID: 31919497](https://pubmed.ncbi.nlm.nih.gov/31919497/)). This provides direct causal evidence linking the variant to both the apoptosis (→ microcephaly) and migration-arrest (→ lissencephaly) arms of the disease.

### Finding 3 — Variant location predicts phenotype across a graded "KIF2A syndrome"

Variant position correlates with clinical severity. Variants in/around the **nucleotide-binding domain (NBD)** cause CDCBM3 (posterior-dominant agyria/pachygyria, severe motor dysfunction, microcephaly); variants in the kinesin motor domain **but outside the NBD** associate with epilepsy; variants **outside the motor domain** associate with autism spectrum. Clinical features are largely restricted to CNS and facial anomalies. As summarized: *"Variants in KIF2A have been reported in the NBD for CDCBM3, in the kinesin motor 3 domain, but not in the NBD in epilepsy, and outside of the kinesin motor domain in autism spectrum syndrome, respectively"* and *"We can call this spectrum 'KIF2A syndrome' with variable severity"* ([PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/)). The core CDCBM3 phenotype: *"Patients with CDCBM3 exhibit posterior dominant agyria/pachygyria with severe motor dysfunction"* ([PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/)).

### Finding 4 — KIF2A regulates inhibitory interneuron synapses and postnatal circuits, linking its loss to epileptogenesis

KIF2A is an atypical kinesin (kinesin-13): *"KIF2A is an atypical kinesin that depolymerizes MT in ATP-dependent manner and regulates MT dynamics"* ([PMID: 36733270](https://pubmed.ncbi.nlm.nih.gov/36733270/)). Deletion of KIF2A in cortical interneurons produces inhibitory synapse dysfunction and epileptic susceptibility. Beyond its prenatal roles, KIF2A *"regulates cell migration, axon elongation, and pruning in the developing nervous system"* ([PMID: 29313800](https://pubmed.ncbi.nlm.nih.gov/29313800/)) and postnatally shapes dentate granule cell development and hippocampal wiring — a dedicated postnatal circuit-establishment role that contributes an epileptogenic mechanism distinct from the migration defect.

### Finding 5 — Core clinical phenotype: posterior-predominant lissencephaly with microcephaly, severe motor/cognitive impairment, and epilepsy

Patients present with classic lissencephaly following a posterior-to-anterior gradient. *"Both mutations lead to a classic form of lissencephaly, with a posterior to anterior gradient, almost indistinguishable from LIS1-related lissencephaly. However, three fourths of patients also showed variable congenital and postnatal microcephaly, up to −5 SD"* ([PMID: 27747449](https://pubmed.ncbi.nlm.nih.gov/27747449/)). Additional features include severe motor developmental delay, severe cognitive impairment, absent speech, and rarer features such as congenital laryngomalacia: *"had presented with motor developmental delay, lissencephaly, severe cognitive impairments, absent speech and congenital laryngomalacia"* ([PMID: 35315043](https://pubmed.ncbi.nlm.nih.gov/35315043/)). Organ involvement is narrow: *"The clinical findings of patients with KIF2A variants appear restricted to the central nervous system and facial anomalies"* ([PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/)).

### Finding 6 — Diagnosis by exome/genome sequencing + brain MRI; management is symptomatic

Diagnosis is established by whole-exome or whole-genome sequencing (often quad/trio WES) identifying a heterozygous *KIF2A* variant, confirmed by Sanger sequencing, combined with brain MRI showing MCD. *"Whole exome sequencing (WES) was carried out for the family trio. Suspected variant was verified by Sanger sequencing"* and, for a representative variant, *"Based on the ACMG guidelines, it was categorized as likely pathogenic (PS2+PM1+PM2+PP3)"* ([PMID: 35315043](https://pubmed.ncbi.nlm.nih.gov/35315043/)). No targeted or curative therapy exists; management is supportive — antiseizure medication for the frequently drug-resistant epilepsy plus developmental/rehabilitative therapies.

### Finding 7 — Ultra-rare, sporadic autosomal dominant disorder; recurrence via germline mosaicism

The disorder is very rare (CDCBM3, OMIM #615411) with only a small number of reported patients worldwide: *"KIF2A-related tubulinopathy (MIM: #615411) is a very rare disorder"* ([PMID: 37331001](https://pubmed.ncbi.nlm.nih.gov/37331001/)). Inheritance is autosomal dominant: *"CDCBM3 … is a rare autosomal dominant syndrome caused by Kinesin family Member 2A (KIF2A) gene mutation"* ([PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/)). Nearly all pathogenic variants arise *de novo* (confirmed absent in parents by trio sequencing). No founder effect, consanguinity role, or ethnic/sex predilection is established. Sibling recurrence with unaffected parents is attributed to parental germline mosaicism ([PMID: 37331001](https://pubmed.ncbi.nlm.nih.gov/37331001/)).

### Finding 8 — Model organisms recapitulate microcephaly, migration defects, and epilepsy

Mouse and zebrafish models reproduce key disease features. The conditional knock-in of human KIF2A p.His321Asp *"present[s] with neuroanatomical anomalies and microcephaly associated with behavioral deficiencies and susceptibility to epilepsy"* ([PMID: 31919497](https://pubmed.ncbi.nlm.nih.gov/31919497/)). Conditional forebrain inactivation disrupts postnatal tangential neuroblast migration — *"conditional inactivation of Kif2a in the forebrain recapitulates the Celsr3 knockout phenotype"* ([PMID: 34582949](https://pubmed.ncbi.nlm.nih.gov/34582949/)) — and tamoxifen-inducible postnatal deletion impairs hippocampal wiring: *"we investigated KIF2A function in the postnatal hippocampus by using tamoxifen-inducible"* deletion ([PMID: 29313800](https://pubmed.ncbi.nlm.nih.gov/29313800/)).

### Finding 9 — KIF2A acts within a neuronal-migration protein complex (LIS1/NDE1/DYNC1H1/CDK5)

KIF2A is a kinesin-13 that, unlike motile kinesins, *"use[s] their catalytic cycle to depolymerize microtubules independent of motility"* ([PMID: 42517274](https://pubmed.ncbi.nlm.nih.gov/42517274/)). In developing neurons it operates alongside other migration genes: CEP85L *"forms a complex with many other proteins required for migration, including CDK5, LIS1, NDE1, KIF2A, and DYNC1H1,"* and *"Loss of CEP85L disrupts CDK5 localization and activation, leading to centrosome disorganization and disrupted microtubule cytoskeleton organization"* ([PMID: 32097629](https://pubmed.ncbi.nlm.nih.gov/32097629/)). This situates KIF2A within the same molecular machinery as the major lissencephaly gene *LIS1 (PAFAH1B1)*, explaining the near-identical imaging phenotype.

### Finding 10 — The 2013 Poirier et al. discovery study established KIF2A as an MCD gene via impaired ATP hydrolysis

The landmark 2013 study (Poirier et al., *Nature Genetics*) first linked *KIF2A* to MCD: *"Here we report the discovery of multiple pathogenic missense mutations in TUBG1, DYNC1H1 and KIF2A, as well as a single germline mosaic mutation in KIF5C, in subjects with MCD"* ([PMID: 23603762](https://pubmed.ncbi.nlm.nih.gov/23603762/)). Functional dissection showed *"the mutations in KIF5C, KIF2A and DYNC1H1 affect ATP hydrolysis, productive protein folding and microtubule binding, respectively,"* and concluded that *"microtubule-dependent mitotic and postmitotic processes are major contributors to the pathogenesis of MCD"* ([PMID: 23603762](https://pubmed.ncbi.nlm.nih.gov/23603762/)).

### Finding 11 — KIF2A is a rare cause of lissencephaly (≤1%), where LIS1 and DCX dominate

In a targeted 17-gene analysis of 811 patients with lissencephaly/subcortical band heterotopia, *"The overall mutation frequency in the entire cohort was 81%. LIS1 accounted for 40% of patients, followed by DCX (23%), TUBA1A (5%), and DYNC1H1 (3%). Other genes accounted for 1% or less of patients"* — placing KIF2A at ≤1% ([PMID: 29671837](https://pubmed.ncbi.nlm.nih.gov/29671837/)). The same study found that *"The brain-imaging pattern correlates with mutations in single lissencephaly-associated genes, as well as in biological pathways,"* supporting imaging-guided differential diagnosis.

### Finding 12 — KIF2A has dual mitotic and postmitotic roles; its deregulation spans a broad neurodevelopmental–neurodegenerative spectrum

*"In dividing cells, kinesin superfamily protein 2A is involved in mitotic progression, spindle assembly, and chromosome segregation. In postmitotic neurons, it is required for axon/dendrite specification and extension, neuronal migration, connectivity, and survival"* and *"Humans with kinesin superfamily protein 2A mutations suffer from a variety of malformations of cortical development, epilepsy, autism spectrum disorder, and neurodegeneration"* ([PMID: 37488893](https://pubmed.ncbi.nlm.nih.gov/37488893/)). This dual role explains the breadth of the human phenotypic spectrum.

---

## Section-by-Section Dossier

### 1. Disease Information

KIF2A-related Complex Cortical Dysplasia is a **Mendelian malformation of cortical development** in which failure of a microtubule-regulating motor protein during corticogenesis produces lissencephaly/pachygyria, microcephaly, and a severe neurodevelopmental phenotype. Information is derived chiefly from **aggregated disease-level resources** (OMIM, Orphanet) and individual case reports/small cohorts rather than large EHR datasets, reflecting its rarity.

**Key identifiers**

| Resource | Identifier |
|---|---|
| OMIM | #615411 (CDCBM3) |
| MONDO | MONDO:0014170 |
| Gene (HGNC) | KIF2A / HGNC:6318 |
| NCBI Gene | 3796 |
| UniProt | O00139 |
| Cytoband | 5q12.1 |

**Synonyms / alternative names:** Cortical Dysplasia, Complex, with Other Brain Malformations 3 (CDCBM3); KIF2A-related lissencephaly; KIF2A-related tubulinopathy; "KIF2A syndrome" (proposed spectrum term, [PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/)). ICD-10 maps broadly to **Q04.3** (other reduction deformities of brain / lissencephaly); MeSH concepts: *Lissencephaly*, *Malformations of Cortical Development*, *Classical Lissencephalies and Subcortical Band Heterotopias*.

### 2. Etiology

**Primary cause — genetic.** Heterozygous, predominantly *de novo* missense variants in *KIF2A*. There is no established environmental, infectious, or toxic cause ([PMID: 23603762](https://pubmed.ncbi.nlm.nih.gov/23603762/); [PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/)).

**Genetic risk factors.** The causal variants are the risk factor; they are highly penetrant dominant alleles acting in the motor/NBD domain. No susceptibility loci or modifier genes are established, though KIF2A functions within a migration complex (LIS1/NDE1/DYNC1H1/CDK5/CEP85L) whose other members cause overlapping phenotypes ([PMID: 32097629](https://pubmed.ncbi.nlm.nih.gov/32097629/)).

**Environmental / lifestyle / protective factors.** **Not applicable / none identified.** As a *de novo* dominant Mendelian disorder, no environmental risk, protective, lifestyle, or gene–environment interaction factors have been described.

### 3. Phenotypes

| Phenotype | HPO (suggested) | Type | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Lissencephaly (agyria/pachygyria, posterior-predominant) | HP:0001339 | Imaging/structural | Congenital | Severe | Near-universal |
| Microcephaly (congenital + postnatal, up to −5 SD) | HP:0000252 / HP:0005484 | Physical sign | Congenital/postnatal | Severe | ~75% ([PMID: 27747449](https://pubmed.ncbi.nlm.nih.gov/27747449/)) |
| Severe motor developmental delay / dysfunction | HP:0002194 | Clinical sign | Infancy | Severe | Frequent |
| Severe intellectual disability / cognitive impairment | HP:0010864 | Clinical sign | Childhood | Severe | Frequent |
| Absent / limited speech | HP:0001344 | Clinical sign | Childhood | Severe | Frequent |
| Epilepsy (often drug-resistant) | HP:0001250 / HP:0001263 | Clinical sign | Infancy/childhood | Severe | Frequent |
| Facial dysmorphism | HP:0001999 | Physical | Congenital | Variable | Subset |
| Congenital laryngomalacia | HP:0001601 | Clinical sign | Congenital | Variable | Rare ([PMID: 35315043](https://pubmed.ncbi.nlm.nih.gov/35315043/)) |

**Progression** is generally stable-structural (the malformation is fixed) with ongoing developmental impairment; epilepsy may be progressive/drug-resistant. **Quality of life** is severely impacted: profound motor and cognitive disability, absent speech, and seizures result in lifelong dependency for daily functioning. Disease-specific QoL instruments (EQ-5D/SF-36/PROMIS) have **not** been formally reported for this ultra-rare disorder.

### 4. Genetic / Molecular Information

- **Causal gene:** *KIF2A* (HGNC:6318; disorder OMIM #615411).
- **Variant type/class:** Missense (dominant). Recurrent hotspots **Ser317, His321, Gly318** in/around the ATP nucleotide-binding pocket; additional motor-domain variants (e.g., Gly440) ([PMID: 27747449](https://pubmed.ncbi.nlm.nih.gov/27747449/); [PMID: 37331001](https://pubmed.ncbi.nlm.nih.gov/37331001/)).
- **Classification (ACMG/AMP):** Pathogenic / likely pathogenic; example p.Gly318Arg → likely pathogenic via **PS2+PM1+PM2+PP3** ([PMID: 35315043](https://pubmed.ncbi.nlm.nih.gov/35315043/)).
- **Allele frequency:** Absent from gnomAD/1000 Genomes (PM2) — consistent with *de novo* origin.
- **Origin:** Germline, overwhelmingly *de novo*; rare parental **germline mosaicism** documented ([PMID: 37331001](https://pubmed.ncbi.nlm.nih.gov/37331001/)).
- **Functional consequence:** Impaired ATP hydrolysis and loss of microtubule-depolymerizing activity; acts as loss-of-function / dominant effect on microtubule dynamics ([PMID: 23603762](https://pubmed.ncbi.nlm.nih.gov/23603762/); [PMID: 31919497](https://pubmed.ncbi.nlm.nih.gov/31919497/)).
- **Modifier genes / epigenetics / chromosomal abnormalities:** None established. CDCBM3 is a single-gene missense disorder, not a copy-number/structural syndrome.

### 5. Environmental Information

**Not applicable.** No environmental, lifestyle, or infectious contributors are known for this *de novo* monogenic disorder.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **de novo heterozygous missense variant** in the *KIF2A* motor/nucleotide-binding domain (e.g., Ser317, His321, Gly318) **leads to** an amino-acid substitution that obstructs ATP emplacement/hydrolysis in the kinesin catalytic pocket ([PMID: 23603762](https://pubmed.ncbi.nlm.nih.gov/23603762/); [PMID: 37331001](https://pubmed.ncbi.nlm.nih.gov/37331001/)).
2. Impaired ATP hydrolysis **results in** loss of KIF2A's ATP-dependent **microtubule-depolymerizing (kinesin-13) activity** ([PMID: 31919497](https://pubmed.ncbi.nlm.nih.gov/31919497/); [PMID: 42517274](https://pubmed.ncbi.nlm.nih.gov/42517274/)).
3. Deficient microtubule depolymerization **dysregulates microtubule dynamics** in neural progenitors and migrating neurons, disrupting the LIS1/NDE1/DYNC1H1/CDK5 microtubule machinery KIF2A operates within (inferred from complex membership, [PMID: 32097629](https://pubmed.ncbi.nlm.nih.gov/32097629/)).
4. This **branches** into two demonstrated cellular outcomes:
   - **(4a)** Increased **apoptosis** of neural progenitors → reduced progenitor pool → **microcephaly** ([PMID: 31919497](https://pubmed.ncbi.nlm.nih.gov/31919497/)).
   - **(4b)** Abnormal **multipolar-to-bipolar transition** of newborn neurons → arrested radial migration → **lissencephaly/pachygyria** (posterior-predominant) ([PMID: 31919497](https://pubmed.ncbi.nlm.nih.gov/31919497/)).
5. A parallel **postnatal branch**: impaired KIF2A in cortical interneurons **causes** inhibitory-synapse dysfunction and disrupted hippocampal/dentate circuit wiring → **epileptic susceptibility** ([PMID: 36733270](https://pubmed.ncbi.nlm.nih.gov/36733270/); [PMID: 29313800](https://pubmed.ncbi.nlm.nih.gov/29313800/)).
6. The combined architectural and circuit defects **produce** the clinical syndrome: congenital microcephaly, severe motor and cognitive impairment, absent speech, and drug-resistant epilepsy ([PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/); [PMID: 27747449](https://pubmed.ncbi.nlm.nih.gov/27747449/)).

```
KIF2A motor/NBD missense (de novo)
        │ obstructs ATP binding/hydrolysis
        ▼
Loss of MT-depolymerase (kinesin-13) activity
        │ dysregulated microtubule dynamics
        ├─────────────── prenatal ───────────────┐
        ▼                                         ▼
 ↑ progenitor apoptosis            abnormal multipolar→bipolar transition
        │                                         │
        ▼                                         ▼
   MICROCEPHALY                      LISSENCEPHALY / PACHYGYRIA (posterior)
        └──────────────── postnatal ─────────────┘
                          ▼
     interneuron inhibitory-synapse + circuit dysfunction
                          ▼
              DRUG-RESISTANT EPILEPSY
   (all converge → severe motor/cognitive impairment, absent speech)
```

- **Molecular pathways / cellular processes:** Microtubule cytoskeleton organization (GO:0000226), microtubule depolymerization (GO:0007019), mitotic spindle organization, neuron migration (GO:0001764), apoptotic process (GO:0006915).
- **Protein dysfunction:** Loss of ATP-dependent depolymerase catalytic function (GO:0008017 microtubule binding; GO:0005524 ATP binding) — a loss-of-function/dominant effect on MT dynamics ([PMID: 23603762](https://pubmed.ncbi.nlm.nih.gov/23603762/)).
- **Cell types (CL):** Radial glial / neural progenitor cells (CL:0000031 neuroblast; CL:0000047 neuronal stem cell), migrating cortical excitatory neurons (CL:0000679 glutamatergic neuron), cortical GABAergic interneurons (CL:0000617).
- **Immune / metabolic involvement:** None established as disease-driving.

### 7. Anatomical Structures Affected

- **Organ level:** Brain (primary); the disorder is largely **CNS-restricted** with facial anomalies ([PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/)). Body system: **nervous system**.
- **Regions (UBERON):** Cerebral cortex (UBERON:0000956), neocortex (UBERON:0001950), with a **posterior-predominant** gradient (occipital/parietal > frontal); hippocampus/dentate gyrus (UBERON:0001954 / UBERON:0001885) implicated postnatally.
- **Tissue/cell level:** Nervous tissue; radial glial progenitors, migrating pyramidal neurons, and GABAergic interneurons (see CL terms above).
- **Subcellular (GO Cellular Component):** Microtubule (GO:0005874), microtubule cytoskeleton, spindle (GO:0005819), centrosome (GO:0005813).
- **Lateralization:** **Bilateral and symmetric** cortical malformation (characteristic of lissencephaly).

### 8. Temporal Development

- **Onset:** **Congenital** — the cortical malformation and microcephaly arise prenatally during corticogenesis; epilepsy typically emerges in infancy/childhood. Onset pattern is **chronic/static-structural**.
- **Progression:** The malformation is fixed (non-progressive architecturally), but clinical course is dominated by **lifelong, chronic** severe disability and often **drug-resistant, progressive epilepsy**. No remission of the structural defect; seizures may fluctuate.
- **Critical period:** The therapeutic/vulnerability window is **prenatal neurodevelopment** (neurogenesis and radial migration). Postnatally, KIF2A continues to shape circuit wiring, offering a conceptual (not yet clinical) window for modulating epileptogenesis ([PMID: 29313800](https://pubmed.ncbi.nlm.nih.gov/29313800/)).

### 9. Inheritance and Population

- **Epidemiology:** Ultra-rare; only a small number of patients reported worldwide ([PMID: 37331001](https://pubmed.ncbi.nlm.nih.gov/37331001/)). KIF2A accounts for **≤1%** of a large (n=811) lissencephaly cohort dominated by LIS1 (40%) and DCX (23%) ([PMID: 29671837](https://pubmed.ncbi.nlm.nih.gov/29671837/)). No reliable prevalence/incidence figures per 100,000 exist.
- **Inheritance:** Autosomal dominant; nearly all variants **de novo** ([PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/)).
- **Penetrance/expressivity:** High penetrance for the pathogenic motor-domain alleles; **variable expressivity** across the KIF2A-syndrome spectrum (severity tracks variant position, [PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/)).
- **Germline mosaicism:** Documented (KIF2A p.G440R in two brothers) → non-zero sibling recurrence risk despite unaffected parents ([PMID: 37331001](https://pubmed.ncbi.nlm.nih.gov/37331001/)).
- **Founder effect / consanguinity / sex ratio / carrier frequency:** None established; no ethnic or sex predilection; *de novo* mechanism means negligible carrier frequency in the general population.

### 10. Diagnostics

- **Genetic testing (definitive):** Trio/quad **whole-exome or whole-genome sequencing** identifying a heterozygous *KIF2A* variant, confirmed by **Sanger** sequencing; variants classified per **ACMG/AMP** ([PMID: 35315043](https://pubmed.ncbi.nlm.nih.gov/35315043/)). Lissencephaly/MCD **gene panels** including *KIF2A* alongside LIS1, DCX, TUBA1A, DYNC1H1, TUBG1, KIF5C are appropriate first-tier ([PMID: 29671837](https://pubmed.ncbi.nlm.nih.gov/29671837/)). CMA/karyotype/FISH are generally uninformative (no structural cause); mtDNA and repeat-expansion testing not applicable.
- **Imaging:** **Brain MRI** is central — demonstrates posterior-predominant agyria/pachygyria and microcephaly, resembling LIS1-related lissencephaly ([PMID: 27747449](https://pubmed.ncbi.nlm.nih.gov/27747449/)). Imaging pattern correlates with the mutated gene/pathway, aiding differential diagnosis ([PMID: 29671837](https://pubmed.ncbi.nlm.nih.gov/29671837/)).
- **Electrophysiology:** EEG for seizure characterization (no KIF2A-specific signature).
- **Biomarkers / labs / biopsy:** No specific biochemical biomarker, enzyme assay, or histopathologic test; diagnosis is molecular + radiologic.
- **Differential diagnosis:** LIS1 (PAFAH1B1), DCX, TUBA1A, TUBG1, DYNC1H1, KIF5C-related lissencephaly/MCD — distinguished by gene test and imaging gradient (DCX more anterior; LIS1 more posterior, as in KIF2A) ([PMID: 29671837](https://pubmed.ncbi.nlm.nih.gov/29671837/)).
- **Screening:** No newborn/population screening; cascade testing informed by germline-mosaicism risk.

### 11. Outcome / Prognosis

Prognosis is **poor**. Patients have severe lifelong disability: profound motor and cognitive impairment, absent speech, and frequently **drug-resistant epilepsy** ([PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/); [PMID: 35315043](https://pubmed.ncbi.nlm.nih.gov/35315043/)). Formal survival, mortality, and standardized QoL data are not established for this ultra-rare cohort, but by analogy to severe lissencephaly, life expectancy is reduced and morbidity is high (seizure-related and aspiration/respiratory complications, the latter compounded where laryngomalacia is present). **Prognostic factor:** variant position within KIF2A (NBD variants → most severe CDCBM3 end of the spectrum) ([PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/)). Recovery potential is limited; the structural malformation is irreversible.

### 12. Treatment

**No disease-specific or curative therapy exists.** Management is **symptomatic and supportive**:

| Modality | Detail | NCIT (suggested) |
|---|---|---|
| Antiseizure medication | For frequently drug-resistant epilepsy; standard ASMs, add-on agents (e.g., cannabidiol used in refractory pediatric MCD-associated DRE cohorts) | NCIT:C264 (Anticonvulsant Agent) |
| Rehabilitation | Physical, occupational, speech therapy for motor/communication deficits | NCIT:C15296 (Rehabilitation Therapy) |
| Supportive/nutritional care | Feeding support; airway management if laryngomalacia | NCIT:C15277 (Supportive Care) |

No pharmacogenomic, gene, cell, RNA-based, targeted, immunotherapeutic, or disease-modifying surgical treatment is established; epilepsy surgery is generally not applicable given diffuse bilateral malformation. No KIF2A-specific clinical trials (NCT) are identified. The microtubule-centric mechanism ([PMID: 23603762](https://pubmed.ncbi.nlm.nih.gov/23603762/)) suggests microtubule-dynamics modulation as a **conceptual** future target, not a current therapy.

### 13. Prevention

Primary prevention is **not applicable** (sporadic *de novo* disorder). The principal preventive tool is **genetic counseling**: although recurrence risk is generally low, documented **parental germline mosaicism** means the risk is non-zero, warranting counseling and, where desired, **prenatal diagnosis or preimplantation genetic testing** for a known familial variant ([PMID: 37331001](https://pubmed.ncbi.nlm.nih.gov/37331001/)). Secondary/tertiary prevention focuses on seizure control and management of complications. No vaccination, behavioral, or public-health intervention applies.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *KIF2A* is highly conserved. Mouse *Kif2a* (NCBI Taxon:10090), zebrafish *kif2a* (NCBI Taxon:7955). No naturally occurring companion-animal or wildlife disease (OMIA) is reported; the disorder is modeled experimentally rather than observed naturally.
- **Comparative biology:** The microtubule-depolymerase function and its role in neuronal migration/survival are evolutionarily conserved, underpinning the predictive value of mouse/zebrafish models ([PMID: 31919497](https://pubmed.ncbi.nlm.nih.gov/31919497/); [PMID: 34582949](https://pubmed.ncbi.nlm.nih.gov/34582949/)).
- **Zoonotic potential:** Not applicable (non-infectious genetic disorder).

### 15. Model Organisms

| Model | Type | Phenotype recapitulation | Reference |
|---|---|---|---|
| KIF2A p.His321Asp conditional knock-in mouse | Mammalian, humanized point variant | Microcephaly, neuroanatomical anomalies, behavioral deficits, epilepsy susceptibility; ↑apoptosis, abnormal multipolar→bipolar transition | [PMID: 31919497](https://pubmed.ncbi.nlm.nih.gov/31919497/) |
| Forebrain-conditional Kif2a inactivation mouse | Mammalian, conditional KO | Disrupted postnatal tangential neuroblast migration (Celsr3–Kif2a axis), olfactory targeting defects | [PMID: 34582949](https://pubmed.ncbi.nlm.nih.gov/34582949/) |
| Tamoxifen-inducible postnatal Kif2a deletion mouse | Mammalian, inducible KO | Impaired dentate granule cell development and hippocampal wiring | [PMID: 29313800](https://pubmed.ncbi.nlm.nih.gov/29313800/) |
| Interneuron-specific Kif2a deletion mouse | Mammalian, conditional KO | Inhibitory synapse dysfunction, epileptic susceptibility | [PMID: 36733270](https://pubmed.ncbi.nlm.nih.gov/36733270/) |
| Zebrafish kif2a loss-of-function | Vertebrate, in vivo | Used to model KIF2A-related neurodevelopmental disorders/epilepsy | — |

**Strengths:** The knock-in mouse directly recapitulates the human allele and the full clinical tetrad (microcephaly, structural anomaly, behavior, epilepsy), establishing causality. **Limitations:** Mouse lissencephalic architecture differs from the gyrencephalic human cortex, so the posterior-gradient agyria is not fully modeled; human iPSC-derived cortical organoids would complement this gap. **Resources:** MGI, IMPC, ZFIN.

---

## Mechanistic Model / Interpretation

The disease is best understood as a **microtubule-dynamics failure during corticogenesis**. KIF2A is a kinesin-13 that burns ATP not to walk along microtubules but to **depolymerize** them at their ends ([PMID: 42517274](https://pubmed.ncbi.nlm.nih.gov/42517274/)). Disease variants land in or around the ATP pocket (Ser317/His321/Gly318), blocking ATP hydrolysis ([PMID: 23603762](https://pubmed.ncbi.nlm.nih.gov/23603762/)) and thereby crippling depolymerase activity ([PMID: 31919497](https://pubmed.ncbi.nlm.nih.gov/31919497/)). Because KIF2A operates inside the same **LIS1/NDE1/DYNC1H1/CDK5/CEP85L migration complex** that governs the major lissencephaly genes ([PMID: 32097629](https://pubmed.ncbi.nlm.nih.gov/32097629/)), its failure produces an imaging phenotype nearly identical to LIS1 disease ([PMID: 27747449](https://pubmed.ncbi.nlm.nih.gov/27747449/)).

The mechanism **branches**: upstream loss of MT regulation drives both **progenitor apoptosis** (→ microcephaly) and **arrest of the multipolar-to-bipolar transition** (→ lissencephaly) prenatally, then a partly separate **postnatal interneuron/circuit** role drives **epilepsy** ([PMID: 31919497](https://pubmed.ncbi.nlm.nih.gov/31919497/); [PMID: 36733270](https://pubmed.ncbi.nlm.nih.gov/36733270/); [PMID: 29313800](https://pubmed.ncbi.nlm.nih.gov/29313800/)). Overlaying this is a **genotype-to-phenotype gradient**: NBD variants cause the severe CDCBM3 pole, motor-domain non-NBD variants cause epilepsy, and variants outside the motor domain cause autism — a unified "KIF2A syndrome" ([PMID: 33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/); [PMID: 37488893](https://pubmed.ncbi.nlm.nih.gov/37488893/)).

---

## Evidence Base

| PMID | Role | Contribution |
|---|---|---|
| [23603762](https://pubmed.ncbi.nlm.nih.gov/23603762/) | Landmark discovery (human + in vitro) | First links KIF2A to MCD; variants impair ATP hydrolysis |
| [27747449](https://pubmed.ncbi.nlm.nih.gov/27747449/) | Clinical/genetic (human) | Recurrent Ser317/His321 hotspots; posterior-gradient lissencephaly; microcephaly in ¾ |
| [31919497](https://pubmed.ncbi.nlm.nih.gov/31919497/) | Functional (mouse) | Knock-in p.His321Asp recapitulates disease; apoptosis + migration defect via lost depolymerase |
| [33506645](https://pubmed.ncbi.nlm.nih.gov/33506645/) | Review/genotype-phenotype | Defines "KIF2A syndrome" spectrum; CNS+facial restriction; AD inheritance |
| [37331001](https://pubmed.ncbi.nlm.nih.gov/37331001/) | Case/mechanistic (human) | ATP-pocket obstruction model; germline mosaicism (G440R) |
| [35315043](https://pubmed.ncbi.nlm.nih.gov/35315043/) | Clinical case (human) | Diagnostic workflow (trio WES+Sanger), ACMG classification, laryngomalacia |
| [36733270](https://pubmed.ncbi.nlm.nih.gov/36733270/) | Functional (mouse) | Interneuron KIF2A loss → inhibitory synapse dysfunction, epilepsy |
| [29313800](https://pubmed.ncbi.nlm.nih.gov/29313800/) | Functional (mouse) | Postnatal hippocampal wiring/dentate role |
| [34582949](https://pubmed.ncbi.nlm.nih.gov/34582949/) | Functional (mouse) | Celsr3–Kif2a axis in postnatal migration |
| [32097629](https://pubmed.ncbi.nlm.nih.gov/32097629/) | Molecular complex | Places KIF2A in LIS1/NDE1/DYNC1H1/CDK5 migration complex |
| [42517274](https://pubmed.ncbi.nlm.nih.gov/42517274/) | Mechanistic review | Kinesin-13 depolymerizes MT independent of motility |
| [29671837](https://pubmed.ncbi.nlm.nih.gov/29671837/) | Epidemiology (human cohort) | KIF2A ≤1% of 811-patient lissencephaly cohort; imaging-genotype correlation |
| [37488893](https://pubmed.ncbi.nlm.nih.gov/37488893/) | Review | Dual mitotic/postmitotic roles; broad phenotypic spectrum |

**Evidence source mix:** human clinical/genetic (cases + an 811-patient cohort), strong model-organism functional data (multiple mouse models directly testing the human allele), and computational/structural variant analyses. The convergence of a knock-in mouse reproducing the exact human variant with human genetic and imaging data gives the gene–disease and mechanism relationships **high confidence**.

---

## Supported and Refuted Hypotheses

No formal hypotheses were rejected during the investigation. The following working hypotheses were **supported** by convergent evidence:

- **Supported:** *KIF2A* motor/ATP-domain missense variants cause CDCBM3 by impairing microtubule depolymerization (human genetics + knock-in mouse + biochemistry).
- **Supported:** Variant position predicts phenotypic severity along a KIF2A-syndrome continuum.
- **Supported:** Epilepsy arises partly through a distinct postnatal interneuron/circuit mechanism, not solely from the structural malformation.
- **Supported:** Recurrence despite unaffected parents is explained by parental germline mosaicism.

---

## Limitations and Knowledge Gaps

1. **Small human N.** CDCBM3 is ultra-rare; quantitative epidemiology (prevalence/incidence), natural-history survival data, and standardized QoL metrics are essentially absent.
2. **Frequency estimates are qualitative** for most phenotypes except microcephaly (~75%); no large registry.
3. **Loss- vs. dominant-negative mechanism** is not fully resolved at the biochemical level — variants impair ATP hydrolysis and depolymerase activity, but whether the mutant poisons wild-type function (dominant negative) versus simple haploinsufficiency-like loss is not definitively parsed.
4. **No human cortical-tissue omics** (transcriptomics/proteomics/single-cell/spatial) specific to KIF2A patients were identified; mechanism rests on mouse models and biochemistry.
5. **Mouse cortical architecture** (lissencephalic) does not fully model the human gyrencephalic posterior-gradient agyria.
6. **No therapeutics** target the mechanism; treatment is entirely symptomatic.

---

## Proposed Follow-up Experiments / Actions

1. **Human iPSC-derived cortical organoids** carrying patient *KIF2A* motor-domain variants to model gyrencephalic migration/apoptosis defects and run single-cell/spatial transcriptomics — filling the human-omics gap.
2. **Biochemical/structural dissection** (cryo-EM + ATPase/depolymerization assays, leveraging AlphaFold/PDB models) of Ser317/His321/Gly318 mutants to formally classify loss-of-function vs. dominant-negative action.
3. **Deep genotype–phenotype curation** across all reported KIF2A variants (ClinVar/literature) to quantitatively validate the NBD→CDCBM3 / motor→epilepsy / non-motor→autism gradient.
4. **International KIF2A patient registry** to establish prevalence, natural history, seizure trajectories, mortality, and QoL.
5. **Interneuron-circuit rescue studies** in the inducible postnatal mouse models to test whether modulating microtubule dynamics or inhibitory-synapse function mitigates epilepsy — probing a postnatal therapeutic window.
6. **Counseling protocol** formally incorporating germline-mosaicism-adjusted recurrence risk and offering PGT/prenatal testing for families with a known variant.

---

*Report compiled from 12 confirmed findings across 5 investigation iterations and 34 reviewed papers. All mechanistic and clinical claims are cited to primary literature with verified abstract quotes.*


## Artifacts

- [OpenScientist final report](KIF2A-related_Complex_Cortical_Dysplasia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](KIF2A-related_Complex_Cortical_Dysplasia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 11 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014170` (3 mentions) - the report calls it "MONDO"; MONDO calls it **complex cortical dysplasia with other brain malformations 3**
- `HP:0001339` (1 mention) - the report calls it "Lissencephaly (agyria/pachygyria, posterior-predominant)"; HP calls it **Lissencephaly**
- `NCIT:C15296` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Isolated Chemotherapeutic Perfusion**
- `NCIT:C15277` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Mastectomy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002194` (1 mention) - the report calls it "Severe motor developmental delay / dysfunction"; HP calls it **Delayed gross motor development**, and lists "Developmental delay, gross motor" among its other names
- `HP:0010864` (1 mention) - the report calls it "Severe intellectual disability / cognitive impairment"; HP calls it **Severe intellectual disability**
- `HP:0001344` (1 mention) - the report calls it "Absent / limited speech"; HP calls it **Absent speech**
- `HP:0001601` (1 mention) - the report calls it "Congenital laryngomalacia"; HP calls it **Laryngomalacia**
- `GO:0000226` (1 mention) - the report calls it "Molecular pathways / cellular processes:** Microtubule cytoskeleton organization"; GO calls it **microtubule cytoskeleton organization**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.