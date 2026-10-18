---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T23:25:25.578538'
end_time: '2026-10-15T23:32:08.531725'
duration_seconds: 402.95
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Acrokeratosis Verruciformis
  mondo_id: MONDO:0007048
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
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 12
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 17
  quotes_valid: 16
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:28498512
  relevance_assessed: 19
  on_topic: 14
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 24
  verified: 22
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.043
  labels_checked: 12
  labels_matching: 4
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0007048
    reported_labels:
    - MONDO
    ontology_label: acrokeratosis verruciformis
  - term_id: CL:0000312
    reported_labels:
    - keratinocytes
    - Cell types involved:** Epidermal **keratinocytes
    - Cell level:** Epidermal **keratinocytes
    ontology_label: keratinocyte
  - term_id: NCIT:C1516
    reported_labels:
    - Keratolytic Agent
    ontology_label: Lisofylline
  labels_variant: 5
  unresolved_terms:
  - HP:0007531
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Acrokeratosis_Verruciformis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Acrokeratosis_Verruciformis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acrokeratosis Verruciformis
- **MONDO ID:** MONDO:0007048 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Acrokeratosis Verruciformis** covering all of the
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

# Acrokeratosis Verruciformis of Hopf — Comprehensive Disease Characterization Report

**Disease:** Acrokeratosis Verruciformis of Hopf (AVH / AKV)
**MONDO ID:** MONDO:0007048 · **OMIM:** #101900 · **Category:** Mendelian (autosomal dominant genodermatosis)
**Causal gene:** *ATP2A2* (SERCA2) · **Allelic disorder:** Darier disease (OMIM #124200)

---

## Summary

Acrokeratosis verruciformis of Hopf (AVH) is a rare, benign, autosomal dominant disorder of keratinization first described by Gustav Hopf in 1931. It is caused by heterozygous missense variation in *ATP2A2*, the gene encoding SERCA2 — the sarco/endoplasmic reticulum Ca²⁺-ATPase isoform 2 that pumps calcium into the endoplasmic reticulum (ER) of keratinocytes. The disease is **allelic to Darier disease**: whereas Darier disease arises from a broad spectrum of mostly loss-of-function *ATP2A2* variants, AVH is characteristically associated with a single recurrent missense change, **p.(Pro602Leu) (c.1805C>T)**, which differentiates it genetically and clinically from Darier disease ([PMID: 28498512](https://pubmed.ncbi.nlm.nih.gov/28498512/); [PMID: 42205461](https://pubmed.ncbi.nlm.nih.gov/42205461/)).

Clinically, AVH presents with multiple flat-topped, skin-colored to wart-like (verrucous) hyperkeratotic papules distributed symmetrically on the **dorsal surfaces of the hands and feet**, frequently accompanied by nail changes (V-shaped notch, longitudinal striations, nail-plate thickening, subungual hemorrhages). Histopathology is distinctive and diagnostic: marked hyperkeratosis, acanthosis, papillomatosis, and "**church-spire**"-like epidermal elevations **without** the acantholysis and dyskeratosis that characterize Darier disease ([PMID: 40256087](https://pubmed.ncbi.nlm.nih.gov/40256087/); [PMID: 31696902](https://pubmed.ncbi.nlm.nih.gov/31696902/)). The mechanistic thread connecting genotype to phenotype runs from reduced SERCA2 pump activity → dysregulated ER/intracellular calcium → impaired desmosomal/keratinocyte adhesion and disordered epidermal differentiation → the acral hyperkeratotic papules ([PMID: 41466489](https://pubmed.ncbi.nlm.nih.gov/41466489/); [PMID: 39207315](https://pubmed.ncbi.nlm.nih.gov/39207315/)).

AVH follows a chronic, lifelong but benign course with normal life expectancy; morbidity is essentially cosmetic/psychosocial plus nail dystrophy. There is no curative therapy — management combines keratolytics, topical/systemic retinoids, and destructive/ablative methods (cryotherapy, laser), with superficial ablation considered first-line; responses are variable and lesions recur ([PMID: 41054640](https://pubmed.ncbi.nlm.nih.gov/41054640/); [PMID: 38854358](https://pubmed.ncbi.nlm.nih.gov/38854358/)). Notably, although SERCA2-haploinsufficient *Atp2a2*(+/−) mice develop squamous cell tumors, an increased skin-cancer risk is **not** established in human AVH ([PMID: 11389134](https://pubmed.ncbi.nlm.nih.gov/11389134/)). This report synthesizes 11 confirmed findings across 19 reviewed papers into a full characterization spanning the 15 requested domains.

---

## 1. Disease Information

**Overview.** Acrokeratosis verruciformis of Hopf is a rare heritable autosomal dominant genodermatosis and disorder of keratinization, first described in 1931 by Hopf ([PMID: 31696902](https://pubmed.ncbi.nlm.nih.gov/31696902/)). It manifests as multiple flat, skin-colored to verrucous keratotic papules concentrated on the dorsa of the hands and feet. It is now understood to be part of the *ATP2A2*/SERCA2 disease spectrum and allelic to Darier disease ([PMID: 28498512](https://pubmed.ncbi.nlm.nih.gov/28498512/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (disease) | #101900 (Acrokeratosis verruciformis of Hopf) |
| MONDO | MONDO:0007048 |
| Gene (OMIM) | *ATP2A2* \*108740 |
| Allelic disorder | Darier disease, OMIM #124200 |
| HGNC | HGNC:812 |
| NCBI Gene (Entrez) | 488 |
| Ensembl | ENSG00000174437 |
| Cytoband | 12q24.11 (GRCh38 chr12:110,280,603–110,351,093) |
| UniProt | P16615 (SERCA2) |

(Gene identifiers verified via mygene.info; finding F007.)

**Synonyms / alternative names.** Acrokeratosis verruciformis of Hopf (AVH, AKV); Hopf disease; Hopf keratosis.

**Information source.** Knowledge for this disease is derived almost entirely from **aggregated disease-level resources** (OMIM, MONDO) and **individual published case reports / small case series**, rather than EHR-scale cohorts — a reflection of the disorder's rarity.

---

## 2. Etiology

**Primary cause — genetic.** AVH is a monogenic Mendelian disease caused by a **heterozygous missense variant in *ATP2A2***. The characteristic, recurrent allele is **p.(Pro602Leu) (c.1805C>T)**, which specifically associates with AVH and distinguishes it from Darier disease ([PMID: 42205461](https://pubmed.ncbi.nlm.nih.gov/42205461/); [PMID: 28498512](https://pubmed.ncbi.nlm.nih.gov/28498512/); [PMID: 40256087](https://pubmed.ncbi.nlm.nih.gov/40256087/)). As stated in the 2026 review, AVH "is due to the heterozygous missense mutation p.(Pro602Leu) in the ATPase sarcoplasmic/endoplasmic reticulum Ca" transporter ([PMID: 42205461](https://pubmed.ncbi.nlm.nih.gov/42205461/)).

**Genetic risk factors.** The single causal determinant is a pathogenic *ATP2A2* variant inherited in an autosomal dominant fashion. No independent susceptibility loci or GWAS signals are described (consistent with a Mendelian disorder).

**Environmental risk / protective factors.** No established environmental risk factors cause AVH. However, within the allelic SERCA2 disorder spectrum, lesions can "wax and wane in response to environmental factors" — in Darier disease, well-documented exacerbating triggers include heat, sweat, sun exposure, friction, and infection ([PMID: 38536168](https://pubmed.ncbi.nlm.nih.gov/38536168/)). No protective alleles or dietary/lifestyle protective factors have been defined for AVH.

**Gene–environment interactions / two-hit mechanism.** The strongest mechanistic insight into gene–environment interplay comes from the allelic condition Darier disease, where "All 11 persistent skin lesions were associated with second-hit somatic variants in the ATP2A2 gene" across 9 germline-heterozygous patients, with these variants classified as highly deleterious; transient lesions instead "wax and wane in response to environmental factors" ([PMID: 38536168](https://pubmed.ncbi.nlm.nih.gov/38536168/)). This provides a molecular basis for localized, persistent lesions superimposed on a germline-heterozygous background (finding F009).

---

## 3. Phenotypes

**Phenotype type: physical manifestations / clinical signs (cutaneous and nail).**

| Phenotype | Description | Suggested HPO term |
|---|---|---|
| Acral keratotic papules | Multiple flat-topped, skin-colored to verrucous hyperkeratotic papules on dorsa of hands/feet | HP:0000962 (Hyperkeratosis); HP:0007531 (Acral keratoses) |
| Verrucous/wart-like morphology | Wart-like papules, cobblestone peripheral dermoscopy | HP:0200043 (Verrucae) |
| Nail dystrophy | V-shaped notch, longitudinal striations, nail-plate thickening, subungual hemorrhages | HP:0008404 (Nail dystrophy); HP:0001809 (Longitudinal ridging of nails) |
| Palmoplantar involvement (variable) | Punctate keratoses / pits may occur | HP:0000982 (Palmoplantar keratoderma) |

**Characteristics.**
- **Age of onset:** Usually early life (infancy/childhood); rare sporadic adult/late-onset cases reported ([PMID: 31696902](https://pubmed.ncbi.nlm.nih.gov/31696902/)).
- **Severity:** Mild; benign; primarily cosmetic.
- **Progression:** Stable to slowly progressive, with persistent lesions accruing over life (chronic, lifelong).
- **Frequency among affected:** Acral papules and the "church-spire" histology are essentially universal diagnostic features; nail involvement is common but not invariable.

**Clinical description.** Lesions are "multiple flat skin colored papules, mainly localized at the dorsal region of the hands and feet" ([PMID: 31696902](https://pubmed.ncbi.nlm.nih.gov/31696902/)), with keratotic lesions "primarily on the dorsal surfaces of the hands and feet" ([PMID: 40256087](https://pubmed.ncbi.nlm.nih.gov/40256087/)). Additional sites (neck, inguinal region) and warty plaques have been reported. Dermoscopy of dorsal-hand lesions shows "a white network and papules with a central homogeneous area and a peripheral cobblestone appearance" ([PMID: 41054640](https://pubmed.ncbi.nlm.nih.gov/41054640/)).

**Quality-of-life impact.** Impact is predominantly cosmetic and psychosocial; nail changes may cause minor functional/aesthetic concern. No formal EQ-5D/SF-36 data exist for this rare disorder. There is no organ-threatening or life-limiting involvement.

---

## 4. Genetic / Molecular Information

**Causal gene.** *ATP2A2* (SERCA2), HGNC:812, Entrez 488, Ensembl ENSG00000174437, cytoband 12q24.11, UniProt P16615; OMIM gene \*108740 (finding F007).

**Pathogenic variant.**
- **Variant:** p.(Pro602Leu), c.1805C>T — recurrent missense change.
- **Classification:** Pathogenic (disease-causing; recurrent across independent AVH families).
- **Variant type:** Missense (single amino acid substitution Pro→Leu at residue 602 of SERCA2).
- **Origin:** Germline, heterozygous, autosomal dominant. (Within the allelic spectrum, second-hit *somatic* variants drive persistent lesions — finding F009.)
- **Functional consequence:** Reduced SERCA2 pump function. In contrast to the broad **loss-of-function** spectrum underlying Darier disease, the milder p.Pro602Leu substitution produces the AVH phenotype (hyperkeratotic/papillomatous lesions without overt acantholysis) ([PMID: 28498512](https://pubmed.ncbi.nlm.nih.gov/28498512/); [PMID: 42205461](https://pubmed.ncbi.nlm.nih.gov/42205461/)).

**Allele frequency.** The p.Pro602Leu variant is a rare pathogenic allele; it is not a common population polymorphism (consistent with a rare Mendelian disorder). No high-frequency population data apply.

**Modifier genes / epigenetics / chromosomal abnormalities.** No specific modifier genes, epigenetic marks, or chromosomal abnormalities have been established for AVH. The second-hit somatic *ATP2A2* model (finding F009) functions as a genetic modifier of lesion persistence within the SERCA2 spectrum.

---

## 5. Environmental Information

- **Environmental factors:** None causal. Lesion activity in the allelic SERCA2 spectrum is modulated by environmental factors ("wax and wane"); Darier disease triggers (heat, sweat, UV, friction, infection) are the best-characterized analogues ([PMID: 38536168](https://pubmed.ncbi.nlm.nih.gov/38536168/)).
- **Lifestyle factors:** No established lifestyle determinants for AVH.
- **Infectious agents:** AVH is not infectious. (Of note, the allelic Darier disease exhibits cutaneous microbial dysbiosis with *Staphylococcus aureus*/*S. warneri* expansion correlating with severity — [PMID: 37496039](https://pubmed.ncbi.nlm.nih.gov/37496039/) — but this is a secondary feature of the more severe allelic disorder, not AVH per se.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (genotype → phenotype)

1. A **heterozygous germline missense variant in *ATP2A2*** (characteristically p.Pro602Leu) **leads to** production of a partially dysfunctional SERCA2 Ca²⁺-ATPase.
2. Reduced SERCA2 pump activity **results in** impaired pumping of Ca²⁺ into the endoplasmic reticulum, **leading to** dysregulated ER/intracellular calcium stores ([PMID: 41466489](https://pubmed.ncbi.nlm.nih.gov/41466489/); [PMID: 39207315](https://pubmed.ncbi.nlm.nih.gov/39207315/)).
3. Calcium dysregulation **impairs keratinocyte cell–cell adhesion**, causing desmosomal dysfunction and mislocalization of desmosomal proteins ([PMID: 41466489](https://pubmed.ncbi.nlm.nih.gov/41466489/)).
4. Disrupted adhesion plus **disordered epidermal differentiation leads to** abnormal keratinization. *Branch:* in Darier disease (severe LOF alleles) this manifests as suprabasal **acantholysis and dyskeratosis**; in AVH (milder p.Pro602Leu) it manifests as **hyperkeratosis/papillomatosis without overt acantholysis** ([PMID: 28498512](https://pubmed.ncbi.nlm.nih.gov/28498512/); [PMID: 40256087](https://pubmed.ncbi.nlm.nih.gov/40256087/)).
5. The altered epidermal architecture **produces** the clinically visible flat-topped verrucous acral papules and "church-spire" histology.
6. *(Inferred/modifier branch)* A **second-hit somatic *ATP2A2* variant** in a clone of epidermal cells **drives persistent, localized lesions**, whereas transient lesions fluctuate with environmental triggers ([PMID: 38536168](https://pubmed.ncbi.nlm.nih.gov/38536168/)).

### Detail by category

- **Molecular pathway:** ER calcium homeostasis via the SERCA2 pump (the ER Ca²⁺-ATPase). "Darier disease and Hailey-Hailey disease arise from mutations in the endoplasmic reticulum calcium pump, SERCA2, and the Golgi calcium/manganese pump, SPCA1, respectively" ([PMID: 39207315](https://pubmed.ncbi.nlm.nih.gov/39207315/)). Suggested GO: GO:0006874 (cellular calcium ion homeostasis), GO:0070588 (calcium ion transmembrane transport), GO:0005388 (P-type calcium transporter / SERCA activity).
- **Cellular processes:** Disrupted keratinocyte adhesion/desmosome assembly, epidermal differentiation; downstream barrier disruption. Suggested GO: GO:0007009 (plasma membrane organization / cell adhesion), GO:0030216 (keratinocyte differentiation), GO:0002009 (morphogenesis of epithelium).
- **Protein dysfunction:** SERCA2 pump hypofunction (reduced Ca²⁺-ATPase activity); the AVH p.Pro602Leu allele is a milder functional change than the LOF alleles of Darier disease.
- **Immune/tissue mechanisms:** Secondary barrier disruption; in the severe allelic disorder, inflammation, immune-defence pathway upregulation, and microbial dysbiosis occur ([PMID: 37496039](https://pubmed.ncbi.nlm.nih.gov/37496039/)). These are not prominent in benign AVH.
- **Cell types involved:** Epidermal **keratinocytes** (CL:0000312). Melanocyte–keratinocyte adhesion defects (via defective E-cadherin) are implicated in the guttate-leukoderma variant of the allelic disorder.

**Key supporting quotes.** "caused by mutations in the ATP2A2 gene, resulting in calcium dysregulation and impaired keratinocyte adhesion" and "including acantholysis, desmosomal dysfunction and barrier disruption, with mislocalisation of desmosomal proteins" ([PMID: 41466489](https://pubmed.ncbi.nlm.nih.gov/41466489/)).

```
ATP2A2 p.Pro602Leu (germline, heterozygous)
        │  reduced SERCA2 Ca2+-ATPase activity
        ▼
ER / intracellular Ca2+ dysregulation
        │  impaired desmosome assembly & protein localization
        ▼
Impaired keratinocyte adhesion + disordered differentiation
        ├── (severe LOF alleles) → acantholysis/dyskeratosis → DARIER DISEASE
        └── (mild p.Pro602Leu)   → hyperkeratosis/papillomatosis (no acantholysis) → AVH
        │
        ▼ (+ second-hit somatic ATP2A2 variant)
Persistent, localized acral verrucous papules ("church-spire" histology)
```

---

## 7. Anatomical Structures Affected

- **Organ level:** Skin (UBERON:0002097, skin of body) is the sole primary organ. No secondary organ involvement; the integumentary system alone is affected.
- **Tissue level:** Epithelial tissue — the **epidermis** (UBERON:0001003, skin epidermis); specifically acral epidermis of the dorsal hands and feet. Nail apparatus (nail plate/matrix) is involved (onychopathy).
- **Cell level:** Epidermal **keratinocytes** (CL:0000312).
- **Subcellular level:** **Endoplasmic reticulum** (GO:0005783) — site of SERCA2 calcium pumping; desmosomes (GO:0030057) at the plasma membrane are functionally affected.
- **Localization / lateralization:** Bilateral, roughly symmetric distribution over the dorsa of hands and feet; additional reported sites include the neck and inguinal region. Dermoscopy and nail findings as above ([PMID: 41054640](https://pubmed.ncbi.nlm.nih.gov/41054640/); [PMID: 40256087](https://pubmed.ncbi.nlm.nih.gov/40256087/)).

---

## 8. Temporal Development

- **Onset:** Typically congenital to childhood/early life; onset pattern is insidious and chronic. Rare sporadic adult/late-onset, non-familial cases are documented: "Usually, it arises in early life but rare sporadic cases with adult onset have been reported" ([PMID: 31696902](https://pubmed.ncbi.nlm.nih.gov/31696902/)); patients without family history occur ([PMID: 40256087](https://pubmed.ncbi.nlm.nih.gov/40256087/)).
- **Progression:** Slow, stable-to-progressive; papules persist and slowly accrue.
- **Course pattern:** Chronic, lifelong; benign. Persistent lesions do not spontaneously resolve (contrast transient lesions in the allelic spectrum that fluctuate with environment).
- **Remission / critical periods:** No spontaneous remission; treatment-induced clearance is temporary (recurrence after ablation). No specific developmental critical window for intervention.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal dominant. "Acrokeratosis verruciformis of Hopf is a rare heritable autosomal dominant genodermatosis and keratinization disorder, first described in 1931 by Hopf" ([PMID: 31696902](https://pubmed.ncbi.nlm.nih.gov/31696902/); [PMID: 28498512](https://pubmed.ncbi.nlm.nih.gov/28498512/)).
- **Penetrance / expressivity:** Consistent with other *ATP2A2* disorders — high penetrance with variable expressivity; precise penetrance figures are not established for AVH.
- **Sporadic/de novo:** Non-familial cases without family history occur ([PMID: 40256087](https://pubmed.ncbi.nlm.nih.gov/40256087/); [PMID: 31696902](https://pubmed.ncbi.nlm.nih.gov/31696902/)).
- **Germline mosaicism / founder effects / consanguinity / carrier frequency:** Not specifically established for AVH. As an autosomal dominant disorder, recessive carrier-screening concepts do not apply.
- **Epidemiology:** Very rare; true prevalence and incidence are **not established** (no registry data). Reported worldwide without a strong sex predilection; onset usually in childhood (finding F011).
- **Geographic / ethnic distribution:** No defined endemic area; cases reported across populations (e.g., Indian, European, and other reports in the reviewed literature).

---

## 10. Diagnostics

**Diagnostic approach — clinicopathologic, genetically confirmable.**

- **Clinical:** Characteristic acral flat-topped verrucous papules; nail changes; supportive dermoscopy (white network; central homogeneous area with peripheral cobblestone appearance) ([PMID: 41054640](https://pubmed.ncbi.nlm.nih.gov/41054640/)).
- **Histopathology (diagnostic):** "marked hyperkeratosis, acanthosis, papillomatosis, and church spire-like epidermal elevations, confirming the diagnosis of AVH," with **absence of acantholysis/corps ronds** ([PMID: 40256087](https://pubmed.ncbi.nlm.nih.gov/40256087/)). Diagnosis relies "primarily on clinical presentation and histopathological characteristics" ([PMID: 41054640](https://pubmed.ncbi.nlm.nih.gov/41054640/)).
- **Genetic testing:** Single-gene *ATP2A2* sequencing (or WES) identifying **p.(Pro602Leu)** confirms the diagnosis and distinguishes AVH from Darier disease ([PMID: 28498512](https://pubmed.ncbi.nlm.nih.gov/28498512/)).
- **Biomarkers / labs / imaging:** No specific blood or serum biomarker exists; imaging and electrophysiology are not applicable.

**Differential diagnosis.** "AVH poses diagnostic challenges due to its similarity to other conditions, such as seborrheic keratosis, lichen planus, and Darier disease" ([PMID: 40256087](https://pubmed.ncbi.nlm.nih.gov/40256087/)). Also consider verruca plana/vulgaris, epidermodysplasia verruciformis, and stucco keratosis.

| Differential | Distinguishing feature from AVH |
|---|---|
| Darier disease (allelic) | Suprabasal acantholysis + dyskeratosis; seborrheic distribution; broad LOF *ATP2A2* variants |
| Seborrheic keratosis | "Stuck-on" appearance; different histology; acquired, non-hereditary |
| Lichen planus | Violaceous polygonal papules; Wickham striae; interface dermatitis histology |
| Verruca (viral warts) | HPV-driven; koilocytes; no church-spire pattern; not hereditary |

**Screening.** Cascade clinical/genetic evaluation of first-degree relatives is reasonable given autosomal dominant inheritance; no population-based newborn/carrier screening is indicated for this benign disorder.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** Benign disorder with **normal life expectancy** and **no disease-specific mortality** (finding F011).
- **Morbidity / function:** Limited to cosmetic/psychosocial burden plus nail changes; no disability.
- **Disease course:** Chronic lifelong; persistent lesions; treatment-induced clearance is temporary with recurrence.
- **Malignancy risk:** Although *Atp2a2*(+/−) mice show squamous tumor predisposition (finding F005), **an increased skin-cancer risk is NOT established in human AVH**. "SERCA2 haploinsufficiency predisposes murine keratinocytes to neoplasia" ([PMID: 11389134](https://pubmed.ncbi.nlm.nih.gov/11389134/)) — a model-organism observation that has not translated to a demonstrated human AVH cancer risk.
- **Prognostic factors / biomarkers:** None established.

---

## 12. Treatment

**No curative therapy exists.** "Management typically involves keratolytic agents and retinoids, though superficial ablation is considered first-line treatment" ([PMID: 41054640](https://pubmed.ncbi.nlm.nih.gov/41054640/)).

| Modality | Examples | Evidence / notes | Suggested NCIT |
|---|---|---|---|
| Superficial ablation (first-line) | Cryotherapy, laser, electrodesiccation | Destroys lesions; recurrence common | NCIT:C15226 (Cryosurgery); NCIT:C15431 (Laser therapy) |
| Keratolytics | Topical salicylic acid, urea | Adjunct symptom control | NCIT:C1516 (Keratolytic Agent) |
| Retinoids | Acitretin, etretinate | Variable/often refractory; one report of response to combined acitretin + cryotherapy; a 1987 report notes unsuccessful etretinate | NCIT:C1570 (Retinoid); NCIT:C47587 (Acitretin) |

Supporting evidence: "An Atypical Case of Acrokeratosis Verruciformis of Hopf Responding to Combined Acitretin and Cryotherapy" ([PMID: 38854358](https://pubmed.ncbi.nlm.nih.gov/38854358/)); "the unsuccessful therapy with etretinate" ([PMID: 3323700](https://pubmed.ncbi.nlm.nih.gov/3323700/)) — together documenting **variable and frequently refractory** response (finding F004).

**Advanced / experimental therapeutics.** No approved gene, cell, RNA-based, targeted, or immunotherapy for AVH; no registered AVH-specific clinical trials identified. Pharmacogenomics: not applicable.

---

## 13. Prevention

- **Primary prevention:** Not possible for a monogenic inherited disorder; **genetic counseling** (autosomal dominant, 50% transmission risk) is the principal preventive tool, with options for prenatal/preimplantation genetic testing when the familial *ATP2A2* variant is known.
- **Secondary/tertiary prevention:** Early recognition and symptomatic management; avoidance of friction/irritation that may provoke lesions; treatment of secondary nail/skin issues.
- **Immunization / public health / prophylaxis:** Not applicable (non-infectious, non-environmental disease).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human (*Homo sapiens*, NCBI:txid9606) is the species of clinical disease. Laboratory mouse (*Mus musculus*, NCBI:txid10090) is used experimentally.
- **Orthologous gene:** Mouse *Atp2a2* (NCBI Gene 11938, chromosome 5), ortholog of human *ATP2A2* (finding F007).
- **Natural disease in other species:** No well-characterized naturally occurring AVH analogue in companion animals/wildlife is documented in the reviewed literature; relevance to veterinary medicine is limited.
- **Comparative biology / conservation:** SERCA2/ER calcium homeostasis is deeply evolutionarily conserved; the mouse recapitulates key epidermal consequences of SERCA2 haploinsufficiency (see Section 15).
- **Transmission / zoonotic potential:** None (genetic, non-communicable disease).

---

## 15. Model Organisms

**Principal model: *Atp2a2*(+/−) heterozygous null mouse (mammalian, in vivo).**

- **Model type:** Germline heterozygous null (knockout of one *Atp2a2* allele), modeling SERCA2 haploinsufficiency.
- **Phenotype:** "aged heterozygous mutant (Atp2a2(+/-)) mice develop squamous cell tumors of the forestomach, esophagus, oral mucosa, tongue, and skin" — observed in 13/14 aged mice versus 0/age-and-sex-matched wild-type controls, with reduced SERCA2 protein in skin and affected tissues ([PMID: 11389134](https://pubmed.ncbi.nlm.nih.gov/11389134/)).
- **Mechanistic conclusion:** "The development of squamous cell tumors in aged Atp2a2(+/-) mice indicates that SERCA2 haploinsufficiency predisposes murine keratinocytes to neoplasia" ([PMID: 11389134](https://pubmed.ncbi.nlm.nih.gov/11389134/)) — the first direct demonstration that perturbed Ca²⁺ homeostasis can be a primary initiating event in cancer.
- **Phenotype recapitulation / limitations:** The mouse captures SERCA2-dependent epidermal Ca²⁺ biology but models **tumor predisposition** rather than the benign human AVH papular phenotype — a notable divergence (human AVH has no established malignancy risk; finding F011).

**In vitro / organoid models.** Human epidermal organoids and SERCA2 keratinocyte systems reproduce the adhesion/calcium phenotype: these models show that *ATP2A2* mutation causes "calcium dysregulation and impaired keratinocyte adhesion" with "acantholysis, desmosomal dysfunction and barrier disruption, with mislocalisation of desmosomal proteins" ([PMID: 41466489](https://pubmed.ncbi.nlm.nih.gov/41466489/)). These are primarily Darier-disease models but inform the shared SERCA2 mechanism.

**Resources:** MGI (mouse *Atp2a2*), IMPC, and standard rodent repositories.

---

## Mechanistic Model / Interpretation

AVH is best understood as the **mild end of the *ATP2A2*/SERCA2 allelic spectrum**. A single recurrent germline missense change, p.Pro602Leu, modestly reduces SERCA2 pump activity. Because the ER calcium pump is central to keratinocyte desmosome assembly and orderly differentiation, even a modest reduction in pump function destabilizes keratinocyte adhesion. The *degree* of SERCA2 dysfunction dictates which clinical disorder emerges along a shared pathway:

| Feature | AVH (p.Pro602Leu) | Darier disease (broad LOF spectrum) |
|---|---|---|
| *ATP2A2* variant class | Recurrent mild missense | Broad loss-of-function |
| SERCA2 functional deficit | Mild | More severe |
| Histology | Hyperkeratosis, papillomatosis, "church-spire"; **no acantholysis** | Suprabasal **acantholysis + dyskeratosis** |
| Distribution | Dorsal hands/feet (acral) | Seborrheic areas, flexures, nails |
| Severity | Benign, cosmetic | More morbid; malodour, dysbiosis, infections |
| Shared | Autosomal dominant; nail changes; ER Ca²⁺/SERCA2 mechanism | Same gene/pump |

Within this framework, the **two-hit somatic model** explains lesion persistence: a germline-heterozygous background plus a second-hit somatic *ATP2A2* variant in a skin clone yields a fixed, persistent lesion, while transient lesions track environmental triggers ([PMID: 38536168](https://pubmed.ncbi.nlm.nih.gov/38536168/)). The mouse model additionally reveals a latent oncogenic potential of SERCA2 haploinsufficiency that, importantly, has **not** manifested as elevated cancer risk in human AVH — an instructive example of species-specific divergence between model and patient.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [28498512](https://pubmed.ncbi.nlm.nih.gov/28498512/) | Recurrent *ATP2A2* p.(Pro602Leu) differentiates AVH from Darier | Establishes AD inheritance, ATP2A2 cause, and p.Pro602Leu as molecular discriminator (F001, F010) |
| [42205461](https://pubmed.ncbi.nlm.nih.gov/42205461/) | AVH: Genetic, clinicopathologic, therapeutic (Review, 2026) | Confirms recurrent heterozygous p.(Pro602Leu) SERCA2 mutation (F001, F007) |
| [40256087](https://pubmed.ncbi.nlm.nih.gov/40256087/) | AVH in a young Indian female — case report/review | Histology, acral distribution, nail notch, differentials, rarity (F002, F006, F008, F010, F011) |
| [31696902](https://pubmed.ncbi.nlm.nih.gov/31696902/) | Late-onset non-familial AVH | AD genodermatosis, 1931 Hopf description, early-onset + rare adult onset (F002, F006) |
| [41466489](https://pubmed.ncbi.nlm.nih.gov/41466489/) | Mimicking Darier in vitro — epidermal organoid | Calcium dysregulation, desmosomal dysfunction, mislocalization (F003, mechanism) |
| [39207315](https://pubmed.ncbi.nlm.nih.gov/39207315/) | Targeting calcium pumps in Darier/Hailey-Hailey/Grover | SERCA2 as the ER calcium pump underlying the spectrum (F003) |
| [11389134](https://pubmed.ncbi.nlm.nih.gov/11389134/) | Squamous cell tumors in *Atp2a2*(+/−) mice | Mouse model; SERCA2 haploinsufficiency → keratinocyte neoplasia (F005, F011) |
| [38536168](https://pubmed.ncbi.nlm.nih.gov/38536168/) | Persistent Darier lesions & second-hit somatic *ATP2A2* | Two-hit mechanism; environmental modulation (F009) |
| [41054640](https://pubmed.ncbi.nlm.nih.gov/41054640/) | Sporadic AVH with unusual presentation | First-line ablation; dermoscopy; nail changes; clinicopathologic diagnosis (F004, F008, F010) |
| [38854358](https://pubmed.ncbi.nlm.nih.gov/38854358/) | AVH responding to acitretin + cryotherapy | Documents a treatment response (F004) |
| [3323700](https://pubmed.ncbi.nlm.nih.gov/3323700/) | Hopf AVH, non-familial case (1987) | Unsuccessful etretinate — refractoriness (F004) |

Supporting/contextual: [40933297](https://pubmed.ncbi.nlm.nih.gov/40933297/) (AVH–Darier clinical overlap), [32155025](https://pubmed.ncbi.nlm.nih.gov/32155025/) (guttate leukoderma + AVH in Darier), [21668031](https://pubmed.ncbi.nlm.nih.gov/21668031/) (longitudinal erythronychia/nail associations), [37822398](https://pubmed.ncbi.nlm.nih.gov/37822398/) (AVH case series with dermoscopy), [40565511](https://pubmed.ncbi.nlm.nih.gov/40565511/) (Darier genetics/SERCA2), [37496039](https://pubmed.ncbi.nlm.nih.gov/37496039/) (Darier microbial dysbiosis), [42555718](https://pubmed.ncbi.nlm.nih.gov/42555718/) (metabolic stress adaptation in Darier), [36896697](https://pubmed.ncbi.nlm.nih.gov/36896697/) (Darier KVE/immune context).

---

## Limitations and Knowledge Gaps

1. **Rarity and evidence quality.** Nearly all AVH knowledge comes from individual case reports and small series; there are no registries, no prevalence/incidence estimates, and no quality-of-life instruments applied to AVH.
2. **Genotype–phenotype resolution.** While p.Pro602Leu is the recurrent AVH allele, the precise biophysical reason this specific substitution yields the AVH (vs Darier) phenotype is not fully resolved; functional assays comparing pump kinetics across alleles are limited.
3. **Mechanistic borrowing from Darier disease.** Much mechanistic detail (desmosomal mislocalization, two-hit somatic lesions, dysbiosis, organoid phenotypes) derives from Darier-disease models/patients and is **inferred** to apply to AVH as the allelic, milder disorder — not all has been directly demonstrated in AVH tissue.
4. **Cancer risk translation.** The mouse tumor phenotype has no demonstrated human AVH counterpart; whether any long-term neoplastic risk exists in human AVH is unknown but appears clinically negligible.
5. **Penetrance/expressivity figures** and population genetics (founder effects, carrier data) are not quantified for AVH specifically.

---

## Proposed Follow-up Experiments / Actions

1. **Functional characterization of p.Pro602Leu:** Measure SERCA2 Ca²⁺-ATPase kinetics (Vmax, Ca²⁺ affinity) and ER store dynamics for p.Pro602Leu versus representative Darier LOF alleles in keratinocytes/organoids to explain the milder phenotype.
2. **AVH-specific lesional sequencing:** Apply the paired lesional-vs-blood deep-sequencing strategy ([PMID: 38536168](https://pubmed.ncbi.nlm.nih.gov/38536168/)) directly to persistent AVH papules to test whether second-hit somatic *ATP2A2* variants drive AVH lesion persistence as in Darier disease.
3. **Transcriptomic/desmosomal profiling of AVH skin:** Characterize desmosomal protein localization, barrier-gene expression (e.g., claudin-4, cadherin-4), and differentiation markers in AVH versus Darier versus normal acral epidermis.
4. **Natural-history / registry study:** Establish a multicenter AVH registry to estimate prevalence, define penetrance/expressivity, document nail involvement frequency, and formally assess any long-term malignancy risk.
5. **Comparative treatment evaluation:** Prospectively compare ablative modalities (cryotherapy, laser) ± retinoids/keratolytics for durable clearance and recurrence rates, given current reliance on anecdotal responses.
6. **Humanized/organoid AVH model:** Engineer p.Pro602Leu into human epidermal organoids/iPSC-keratinocytes to create a dedicated AVH model distinct from Darier LOF models and test candidate SERCA2-modulating interventions.

---

*Report compiled from 11 confirmed findings across 19 reviewed papers (5 completed investigation iterations). Evidence types span human clinical case reports/series, model-organism (mouse), and in vitro/organoid studies, as annotated per section.*


## Artifacts

- [OpenScientist final report](Acrokeratosis_Verruciformis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Acrokeratosis_Verruciformis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 17 |
| Quoted claims found in source | 16 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 19 |
| On topic | 14 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:28498512` *(abstract only)*: "Acrokeratosis verruciformis of Hopf is a rare heritable autosomal dominant genodermatosis and keratinization disorder, first described in 1931 by Hopf"
  - closest text in source: "Darier disease and Acrokeratosis Verruciformis of Hopf (AKV) are rare disorders of keratinization with autosomal dominant inheritance and very distinct clinical pictures"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 12 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007048` (2 mentions) - the report calls it "MONDO"; MONDO calls it **acrokeratosis verruciformis**
- `CL:0000312` (2 mentions) - the report calls it "keratinocytes", "Cell types involved:** Epidermal **keratinocytes", "Cell level:** Epidermal **keratinocytes"; CL calls it **keratinocyte**
- `NCIT:C1516` (1 mention) - the report calls it "Keratolytic Agent"; NCIT calls it **Lisofylline**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0007531` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006874` (1 mention) - the report calls it "cellular calcium ion homeostasis"; GO calls it **intracellular calcium ion homeostasis**, and lists "cellular calcium ion homeostasis" among its other names
- `GO:0005388` (1 mention) - the report calls it "P-type calcium transporter / SERCA activity"; GO calls it **P-type calcium transporter activity**
- `GO:0007009` (1 mention) - the report calls it "plasma membrane organization / cell adhesion"; GO calls it **plasma membrane organization**
- `GO:0002009` (1 mention) - the report calls it "morphogenesis of epithelium"; GO calls it **morphogenesis of an epithelium**
- `GO:0005783` (1 mention) - the report calls it "Endoplasmic reticulum", "Subcellular level:** **Endoplasmic reticulum"; GO calls it **endoplasmic reticulum**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000312` - called "keratinocytes", "Cell types involved:** Epidermal **keratinocytes", "Cell level:** Epidermal **keratinocytes"
- `GO:0005783` - called "Endoplasmic reticulum", "Subcellular level:** **Endoplasmic reticulum"