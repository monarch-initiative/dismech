---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T19:01:59.634521'
end_time: '2026-08-28T19:12:05.411098'
duration_seconds: 605.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: cone-rod dystrophy and hearing loss 2 (CRDHL2, biallelic CEP250)
  mondo_id: MONDO:0020780
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 35
  verified: 32
  not_found: 1
  obsolete: 2
  unverifiable: 0
  confabulation_rate: 0.029
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0020780
    reported_labels:
    - if available
    ontology_label: cone-rod dystrophy and hearing loss 2
  - term_id: HP:0000613
    reported_labels:
    - Case-level, frequency unknown
    ontology_label: Photophobia
  unresolved_terms:
  - HP:0001731
  obsolete_terms:
  - term_id: HP:0000547
    ontology_label: obsolete Tapetoretinal degeneration
    replaced_by: HP:0000510
  - term_id: GO:0005932
    ontology_label: GO_0005932
    replaced_by: GO:0036064
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Cone-rod_Dystrophy_And_Hearing_Loss_2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** cone-rod dystrophy and hearing loss 2 (CRDHL2, biallelic CEP250)
- **MONDO ID:** MONDO:0020780 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **cone-rod dystrophy and hearing loss 2 (CRDHL2, biallelic CEP250)** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** cone-rod dystrophy and hearing loss 2 (CRDHL2, biallelic CEP250)
- **MONDO ID:** MONDO:0020780 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **cone-rod dystrophy and hearing loss 2 (CRDHL2, biallelic CEP250)** covering all of the
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


# Cone-rod dystrophy and hearing loss 2 (CRDHL2; biallelic **CEP250**): disease-characteristics report

## Executive summary

CRDHL2 is an exceptionally rare, autosomal-recessive, progressive oto-retinal disorder caused by biallelic pathogenic variants in **CEP250**, which encodes the centrosome-linker protein C-Nap1. The best-supported clinical pattern is progressive, usually noncongenital sensorineural hearing loss (SNHL), followed by or accompanied by a relatively mild, cone-predominant retinal dystrophy. It is frequently called **CEP250-related atypical Usher syndrome** or an **Usher-like disorder**, although it does not consistently fit classic Usher types 1–3. Published human evidence remains limited to a small number of families and retrospective cases; consequently, prevalence, penetrance, phenotype frequencies, and long-term prognosis cannot yet be estimated reliably. A 2021 multicenter series included only three CEP250-affected individuals. Their ocular onset ranged from 13–30 years, hearing-loss onset from under 10–24 years, and best-corrected visual acuity (BCVA) from 20/60–20/200; all had progressive SNHL and none reported vestibular symptoms. (igelman2021expandingtheclinical pages 5-7)

The most important 2023–2024 developments are mouse studies reproducing retinal degeneration and hearing loss, identification of photoreceptor apoptosis and candidate cGMP–PKG–MAPK/EDN2–FGF2 responses, and demonstration that cochlear hair-cell loss is concentrated in the basal/high-frequency region. These establish useful preclinical platforms but have not yet produced a CEP250-specific clinical trial or disease-modifying treatment. (chen2023rnaseqanalysisreveals pages 1-2, nan2024thecochlearmorphology pages 5-8, abudiab2023homozygousknockoutof pages 1-2)

## 1. Disease information

### Definition and identifiers

- **Preferred name:** cone-rod dystrophy and hearing loss 2.
- **Abbreviation:** CRDHL2.
- **MONDO:** **MONDO:0020780** (identifier supplied in the target specification; users should verify the current MONDO release).
- **OMIM phenotype:** **618358**.
- **Causal gene:** **CEP250**, OMIM **609689**; approved gene symbol CEP250; protein name **centrosomal protein 250/C-Nap1**.
- **Common synonyms:** CEP250-related cone-rod dystrophy with hearing loss; CEP250-related retinal dystrophy and hearing loss; CEP250-associated atypical Usher syndrome; CEP250-associated Usher-like disease.
- **Orphanet/MeSH:** no disease-specific Orphanet or MeSH descriptor was identified in the retrieved evidence. Broader descriptors such as cone-rod dystrophy, hereditary retinal dystrophy, sensorineural hearing loss, and Usher syndrome may be used for retrieval but should not replace the molecular diagnosis.
- **ICD-10/ICD-11:** no unique CRDHL2 code was identified. In practice, component manifestations are coded under inherited retinal dystrophy/cone-rod dystrophy and sensorineural hearing loss. A specific CEP250 molecular annotation should therefore accompany clinical coding.

The disease definition comes from aggregated disease-level literature and small research cohorts, not population-scale EHR evidence. The 2018 diagnostic study analyzed 77 unrelated suspected Usher cases and identified two CEP250 nonsense variants in one individual; its overall panel detection rate was 82.8%, but that statistic applies to the full Usher cohort—not CRDHL2. (fustergarcia2018highthroughputsequencingfor pages 1-2)

A central classification caveat is **allelic heterogeneity**: CEP250 variants have also been reported with nonsyndromic retinitis pigmentosa (RP) and with progressive nonsyndromic hearing loss. Consequently, “biallelic CEP250 disease” is broader than CRDHL2, and a molecular result alone does not establish that both sensory phenotypes are already present. (kang2023novelvariantin pages 9-11, kang2023novelvariantin pages 1-2, huang2019functionalcharacterizationof pages 1-2)

## 2. Etiology, risk, and protective factors

### Primary cause

CRDHL2 is caused by **germline biallelic CEP250 variants**, most convincingly truncating nonsense or frameshift alleles, inherited in an autosomal-recessive pattern. In the 2021 atypical-Usher cohort, all CEP250 variants were novel nonsense or frameshift variants. Compound-heterozygous and homozygous families have been reported. (igelman2021expandingtheclinical pages 5-7, fustergarcia2018highthroughputsequencingfor pages 4-5)

The causal model is loss of normal C-Nap1 function or localization rather than environmental injury. A 2023 functional study showed that p.Gln1171Ter was translated but failed to localize to centrosomes, dispersing in the cytosol; the investigators found no dominant-negative effect on wild-type CEP250. (kang2023novelvariantin pages 6-9, kang2023novelvariantin pages 11-12)

### Risk factors and modifiers

- **Established risk:** two pathogenic CEP250 alleles in trans.
- **Family history/consanguinity:** increase the prior probability of recessive disease but are not required. The founding report involved a consanguineous Iranian-Jewish family; other cases were compound heterozygotes. (chen2023rnaseqanalysisreveals pages 1-2, fustergarcia2018highthroughputsequencingfor pages 10-10)
- **Possible modifier:** the original Iranian-Jewish family also carried a heterozygous nonsense variant in **C2orf71/PCARE**, creating uncertainty about a digenic or modifying contribution. Later independent CEP250-only families strengthened CEP250 causality, but the modifying role of C2orf71 remains unresolved. (huang2019functionalcharacterizationof pages 4-6, chen2023rnaseqanalysisreveals pages 1-2)
- **Age:** not an etiologic risk factor, but expression is age-dependent; retinal and auditory abnormalities can emerge or worsen over decades.
- **Sex:** no sex effect is established.
- **Protective variants:** none established.
- **Environmental, occupational, infectious, dietary, smoking, alcohol, or exercise effects:** none demonstrated specifically for CRDHL2.
- **Gene–environment interactions:** no CRDHL2-specific evidence.

Ordinary retinal and hearing health measures may be prudent, but they must not be represented as proven disease-modifying interventions.

## 3. Phenotypes

### Core human phenotype

| Manifestation | Character and timing | Available frequency evidence | Suggested HPO term |
|---|---|---|---|
| Sensorineural hearing impairment | Bilateral, progressive, mild-to-moderate or moderate-severe; onset reported from <10 to 24 years in the three-patient series | 3/3 in that selected CEP250 cohort; not a population estimate | HP:0000407; progressive hearing impairment HP:0001731 |
| Cone/cone-rod retinal dystrophy | Usually mild and progressive; ocular onset 13–30 years in the series; one ffERG showed mild cone dysfunction with normal rods | 3/3 had retinal disease by study design; one had reported ffERG | Cone-rod dystrophy HP:0000548; cone dystrophy HP:0000547 |
| Reduced visual acuity | Progressive; latest BCVA 20/60–20/200 in the three cases | Reported in the small case series | Reduced visual acuity HP:0007663 |
| Photophobia | Prominent in some patients; RP1973 developed photophobia with late progressive visual decline | Case-level, frequency unknown | HP:0000613 |
| Outer retinal atrophy | OCT: ONL thinning and/or subtle ellipsoid/interdigitation-zone disruption | All three CEP250 cases had some outer retinal atrophy | Suggested: outer retinal atrophy; retinal degeneration HP:0000546 |
| Abnormal fundus autofluorescence | May be subtle peripheral or peripapillary hyper-autofluorescence; FAF may also be normal | Variable among three cases | Abnormal fundus autofluorescence HP:0030636 |
| Visual-field constriction | Variable, from approximately 100° to approximately 20° horizontally with a V4e target in reported siblings | 2 tested siblings | Visual-field defect HP:0001123; constricted visual fields HP:0001133 |
| RP-like fundus changes | Mid-peripheral bone-spicule pigment and vessel attenuation in RP1973; other cases can have a normal-appearing color fundus | Variable | Retinitis pigmentosa HP:0000510; bone-spicule pigmentation HP:0007703 |
| Vestibular dysfunction | Not reported in the three CEP250 cases; mouse swimming behavior also normal | 0/3 reported, but sample is inadequate to exclude rare involvement | Abnormal vestibular function HP:0001751, marked absent when appropriate |

The multicenter study explicitly reported: “Age of onset ranged from 13 to 30 years,” “All patients demonstrated progressive SNHL,” and “There were no reports of vestibular symptoms.” Color fundus findings were normal in all three, illustrating that OCT/FAF/ERG can detect disease despite subtle ophthalmoscopy. (igelman2021expandingtheclinical pages 5-7)

A deeply characterized 2018 patient, RP1973, developed bilateral moderate-severe progressive hearing loss at 13 years and underwent the first reported ophthalmic examination at 44 years after late progressive visual decline and photophobia. BCVA was 0.6 right and 0.5 left; examination showed mid-peripheral bone-spicule pigment and peripheral vessel narrowing. (fustergarcia2018highthroughputsequencingfor pages 4-5)

### Quality-of-life impact

No CEP250-specific EQ-5D, SF-36, PROMIS, educational, mobility, or employment study was found. Nevertheless, combined progressive hearing and visual impairment plausibly compromises communication, reading, driving, orientation, and independent mobility. These are clinical inferences—not measured CRDHL2 outcomes. Dual-sensory rehabilitation should begin before severe loss because one sensory system becomes progressively less able to compensate for the other.

## 4. Genetic and molecular information

### Gene and variant spectrum

CEP250 encodes a large coiled-coil centrosomal protein, C-Nap1, which anchors linker proteins including rootletin at proximal centriole ends and contributes to interphase centrosome cohesion. CEP250 also localizes in photoreceptor ciliary/basal-body contexts and interacts with rootletin, NEK2, and CEP78. (kang2023novelvariantin pages 1-2, huang2019functionalcharacterizationof pages 1-2)

Reported alleles relevant to the phenotypic spectrum include:

- **c.3463C>T, p.Arg1155Ter:** homozygous in the original atypical-Usher family, alongside heterozygous C2orf71/PCARE p.Gln1097Ter. (huang2019functionalcharacterizationof pages 4-6, chen2023rnaseqanalysisreveals pages 1-2)
- **c.361C>T, p.Arg121Ter** and **c.562C>T, p.Arg188Ter:** compound heterozygous in a Japanese family with mild cone-rod dystrophy and SNHL. (huang2019functionalcharacterizationof pages 4-6)
- **p.Lys1113Ter and p.Arg1336Ter:** compound heterozygous in a later case with progressive hearing loss and late-onset CRD. (abudiab2023homozygousknockoutof pages 1-2)
- **c.562C>T, p.Arg188Ter:** also reported homozygously with nonsyndromic RP during follow-up to age 28, demonstrating phenotype overlap rather than a one-variant/one-phenotype rule. A knock-in mouse carrying the corresponding allele had severe retinal dysfunction. (abudiab2023homozygousknockoutof pages 1-2, huang2019functionalcharacterizationof pages 1-2)
- **c.1826C>T, p.Ala609Val:** reported with nonsyndromic RP; its relatively high Ashkenazi-Jewish frequency (>1/600 alleles in the cited report) warrants especially careful contemporary ClinVar/gnomAD and segregation review before classification. (huang2019functionalcharacterizationof pages 4-6)
- **c.3511C>T, p.Gln1171Ter:** homozygous progressive nonsyndromic SNHL without retinal degeneration at the time of study; affected adults were only in their late 30s/early 40s, so delayed retinal disease was not excluded. (kang2023novelvariantin pages 9-11, kang2023novelvariantin pages 1-2)

Additional novel nonsense/frameshift variants were present in the 2021 series, but exact table-level HGVS data were not recoverable from the retrieved text. Every variant should be assessed independently under current ACMG/AMP criteria; historical labels such as “UV4” are not equivalent to a current ClinVar consensus. Current gnomAD frequencies and ClinVar review status were not available in the retrieved evidence and should not be inferred.

All reported disease alleles are germline. No somatic CEP250 mechanism, recurrent pathogenic chromosomal rearrangement, repeat expansion, mitochondrial variant, or disease-specific epigenetic abnormality is established. No validated modifier gene beyond the unresolved C2orf71/PCARE observation is known.

### Pathogenic consequence

The strongest direct functional example is p.Gln1171Ter: a roughly 150-kDa truncated product was made but failed centrosomal localization. In murine cochlea, Cep250 is expressed in inner and outer hair cells; knockout produced hair-cell degeneration and progressive hearing loss. The authors’ abstract states: “a nonsense variant in CEP250 results in a deficit of centrosome localization and hair cell degeneration in the cochlea.” Published 21 September 2023; DOI: https://doi.org/10.3390/cells12182328. (kang2023novelvariantin pages 1-2)

## 5. Environmental information

No toxin, radiation, pollution, occupational exposure, infection, medication, diet, exercise pattern, tobacco exposure, or alcohol exposure is known to cause or trigger CRDHL2. Likewise, no preventive drug, nutrient, antioxidant, or exposure avoidance strategy has demonstrated CEP250-specific benefit. The disorder should therefore be represented as **genetic**, with environmental fields marked “no disease-specific evidence,” rather than populated from generic retinal-degeneration associations.

## 6. Mechanism and pathophysiology

### Proposed causal chain

1. **Upstream genetic lesion:** biallelic damaging CEP250 variants reduce functional C-Nap1 or prevent its centrosomal localization.
2. **Organelle-level defect:** impaired proximal-centriole linker/centrosome cohesion and disturbed specialized ciliary-rootlet or basal-body homeostasis.
3. **Cell-specific vulnerability:** photoreceptors depend on continuous protein transport and structural maintenance across the connecting cilium; cochlear hair cells depend on highly polarized cytoskeletal/centrosomal organization.
4. **Downstream injury:** mislocalization of photoreceptor outer-segment proteins, photoreceptor dysfunction and apoptosis; degeneration of cochlear hair cells, particularly basal-turn outer hair cells.
5. **Clinical expression:** cone-predominant or cone-rod dystrophy with photophobia and progressive visual loss, plus progressive high-frequency-predominant SNHL. (kang2023novelvariantin pages 6-9, nan2024thecochlearmorphology pages 5-8, huang2019functionalcharacterizationof pages 1-2, chen2023rnaseqanalysisreveals pages 1-2)

This chain is biologically coherent but only the genotype-to-phenotype association is directly demonstrated in humans. Intermediate mechanisms derive predominantly from cultured cells and mice.

### Molecular profiling

In a 2023 Cep250-knockout retina study, OCT/ERG and histology at P90 and P180 showed reduced outer nuclear layer (ONL), inner/outer segment, and whole-retinal thickness; reduced scotopic and photopic a- and b-waves; fewer photoreceptors; and increased TUNEL labeling. RNA-seq at P90 found **298 differentially expressed genes: 149 upregulated and 149 downregulated**. cGMP–PKG, MAPK, EDN2–FGF2, and thyroid-hormone synthesis pathways were enriched upward, whereas endoplasmic-reticulum protein processing was downregulated. Increased Pde3a, Pde3b, Gfap, Edn2, Fgf2, and Tyr expression was validated. These changes may represent downstream stress/reactive responses rather than the initiating lesion. Published 16 May 2023; DOI: https://doi.org/10.3390/ijms24108843. (chen2023rnaseqanalysisreveals pages 1-2, chen2023rnaseqanalysisreveals pages 5-7)

No validated human CRDHL2 transcriptomic, proteomic, metabolomic, lipidomic, epigenomic, spatial-transcriptomic, patient-iPSC, retinal-organoid, or multi-omics signature was identified. A 2024 mouse preprint mined cochlear single-cell RNA-seq across P1–P100 and found increasing Cep250 expression in auditory hair cells but little expression in vestibular hair cells; this provides a possible explanation for auditory disease without vestibular dysfunction but is not human proof. (nan2024thecochlearmorphology pages 5-8, nan2024thecochlearmorphology pages 8-16)

### Suggested mechanism ontologies

- **GO cellular component:** centrosome GO:0005813; centriole GO:0005814; basal body GO:0005932; cilium GO:0005929; photoreceptor connecting cilium; cytosol GO:0005829.
- **GO biological process:** cilium organization GO:0044782; centrosome cycle; microtubule cytoskeleton organization; photoreceptor-cell maintenance; sensory perception of sound; visual perception; apoptotic process GO:0006915; MAPK cascade GO:0000165.
- **Cell Ontology:** photoreceptor cell CL:0000679; rod photoreceptor CL:0000604; cone photoreceptor CL:0000710; auditory hair cell CL:0000589; inner and outer hair-cell child terms where supported.

## 7. Anatomical structures affected

The primary organs are bilateral **retina** and **inner ear/cochlea**. Retinal injury is concentrated in photoreceptors and the outer retina—ONL, inner/outer segments, ellipsoid zone, and interdigitation zone—with secondary retinal pigment epithelial/fundus changes in some cases. Cochlear evidence implicates inner and outer hair cells, especially outer hair cells of the basal, high-frequency turn. Spiral-ganglion expression occurs in mice, but direct neuronal degeneration has not been established. (kang2023novelvariantin pages 6-9, nan2024thecochlearmorphology pages 5-8, igelman2021expandingtheclinical pages 5-7)

Suggested anatomical terms include retina **UBERON:0000966**, eye **UBERON:0000970**, inner ear **UBERON:0001844**, cochlea **UBERON:0001853**, organ of Corti, retinal photoreceptor layer, and retinal outer nuclear layer. Disease is generally bilateral. No consistent brain, kidney, skeletal, cardiac, respiratory, gastrointestinal, immune, endocrine, or metabolic organ involvement has been demonstrated in humans.

## 8. Temporal development

CRDHL2 is chronic, lifelong, insidious, and progressive. Hearing loss often begins in childhood or adolescence and may precede recognized retinal disease by decades. Ocular onset in the available multicenter cases was 13–30 years; RP1973’s first documented ophthalmic evaluation was at 44 years. Progression rates vary and formal stages have not been validated. (igelman2021expandingtheclinical pages 5-7, fustergarcia2018highthroughputsequencingfor pages 4-5)

A pragmatic—not validated—clinical staging framework is:

- **Presymptomatic molecular stage:** biallelic CEP250 variants; normal or near-normal functional testing.
- **Early auditory stage:** high-frequency or moderate SNHL, potentially before visual complaints.
- **Early retinal stage:** photophobia, declining acuity, mild cone-predominant ffERG abnormality, subtle OCT/FAF change.
- **Established dual-sensory stage:** progressive SNHL plus cone/cone-rod dystrophy and visual-field loss.
- **Advanced stage:** severe dual-sensory disability; frequency and timing unknown.

There is no evidence of spontaneous remission, relapsing-remitting disease, or treatment-induced reversal. The likely therapeutic window is before irreversible photoreceptor and hair-cell loss, but no human biomarker-defined window has been established.

## 9. Inheritance and population

Inheritance is autosomal recessive. For two heterozygous carrier parents, each pregnancy has a theoretical 25% affected, 50% carrier, and 25% noncarrier probability. Heterozygous mice showed no significant auditory phenotype in the 2024 study, consistent with recessive inheritance, although this does not prove complete absence of subtle effects in human carriers. (nan2024thecochlearmorphology pages 1-5)

Disease-specific prevalence, incidence, carrier frequency, sex ratio, penetrance, age-specific penetrance, and geographic distribution are unknown. Published families include Iranian-Jewish, Japanese, European/Spanish, Chinese, and Korean ascertainments, but these do not establish population enrichment. No validated founder allele for CRDHL2 was identified. The approximately 1/4,000 RP prevalence and general Usher estimates sometimes cited in source papers must not be assigned to CRDHL2. (abudiab2023homozygousknockoutof pages 1-2, nan2024thecochlearmorphology pages 1-5)

Expressivity is clearly variable: biallelic CEP250 variants can yield dual-sensory disease, retinal-only disease, or hearing-only disease at the age examined. Anticipation is not expected and has not been reported. Germline mosaicism has not been documented but cannot be excluded as a general reproductive possibility.

## 10. Diagnostics

### Clinical evaluation

There are no validated disease-specific diagnostic criteria. Diagnosis requires concordance of phenotype, molecular findings, segregation, and exclusion of more common causes.

**Ophthalmic assessment:** BCVA and refraction; slit-lamp examination; dilated fundus examination; color photography; spectral-domain OCT; fundus autofluorescence; kinetic/static perimetry; and full-field ERG. A normal-looking fundus does not exclude early CEP250 retinal disease. (igelman2021expandingtheclinical pages 5-7)

**Audiovestibular assessment:** pure-tone air and bone-conduction audiometry, speech audiometry, tympanometry as indicated, otoacoustic emissions, and ABR when behavioral testing is unreliable. The 2023 human study measured air thresholds at 250–8,000 Hz and bone thresholds at 250–4,000 Hz. Vestibular history/examination should be documented despite its apparent sparing. (kang2023novelvariantin pages 1-2)

Routine blood chemistry, enzyme assays, biopsy, MRI, CT, or systemic imaging have no disease-specific diagnostic role unless another diagnosis is suspected.

### Genetic testing strategy

1. Use an inherited-retinal-disease, hearing-loss, or comprehensive Usher/dual-sensory panel that includes **CEP250**, with sequencing and exon-level deletion/duplication analysis.
2. If negative or only one allele is found, proceed to trio WES or preferably WGS, including CNV, splice-region, and structural-variant analysis.
3. Confirm candidate variants by orthogonal testing and parental segregation to establish trans configuration.
4. Reanalyze periodically because phenotype assignment and variant classification are evolving.
5. RNA/minigene analysis is appropriate for suspected splice variants, although the minigene-positive variants in the 2018 paper were in other Usher genes, not CEP250. (fustergarcia2018highthroughputsequencingfor pages 3-4, fustergarcia2018highthroughputsequencingfor pages 4-5)

The 2018 panel covered all 32 CEP250 coding exons using transcript NM_007186.4 and achieved 100% designed target coverage for CEP250. WES was used in RP1973 to search for competing causes. The authors concluded that thorough clinical examination—particularly of cone involvement—is needed because different CEP250 alleles produce overlapping phenotypes. (fustergarcia2018highthroughputsequencingfor pages 3-4, fustergarcia2018highthroughputsequencingfor pages 10-10)

CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are not first-line unless the broader presentation suggests another disorder.

### Differential diagnosis

Important alternatives include classic Usher syndrome (**MYO7A, USH1C, CDH23, PCDH15, USH1G, CIB2, USH2A, ADGRV1, WHRN, CLRN1**), **CEP78**-related CRDHL1, and atypical Usher-like disease due to **ARSG** or **ABHD12**. Other considerations include Alström syndrome, peroxisomal/mitochondrial disease, isolated inherited retinal dystrophy with unrelated hearing loss, and nonsyndromic CEP250-associated RP or deafness. Genotype-first classification is especially valuable because the retinal phenotype may be cone-predominant and the hearing loss noncongenital. (igelman2021expandingtheclinical pages 3-5, igelman2021expandingtheclinical pages 5-7)

## 11. Outcome and prognosis

No survival curve, mortality rate, life-expectancy estimate, or disease-specific cause of death has been published. Available evidence suggests that CRDHL2 affects sensory function rather than lifespan. Morbidity is driven by progressive visual and auditory disability; individual endpoints such as legal blindness, cochlear implantation, loss of independent mobility, or employment outcomes have not been quantified.

Prognosis is difficult to predict from genotype alone. Truncating variants are enriched in reported dual-sensory cases, but truncating alleles can also appear hearing-only or retinal-only at a particular age. Baseline OCT/ERG, visual fields, audiometric configuration, and longitudinal rates of change are therefore more defensible prognostic measures than variant class alone. (kang2023novelvariantin pages 9-11, abudiab2023homozygousknockoutof pages 1-2, igelman2021expandingtheclinical pages 5-7)

## 12. Treatment and current implementation

No CEP250-specific pharmacotherapy, gene therapy, cell therapy, RNA therapy, gene editing, or approved disease-modifying treatment was identified. No relevant CEP250/CRDHL2 interventional ClinicalTrials.gov study was found in the tool search. Mouse models are described as platforms for future treatment or gene-therapy development, not evidence of human efficacy. (abudiab2023homozygousknockoutof pages 1-2)

Current real-world management is multidisciplinary:

- **Hearing:** hearing aids; remote microphone and communication systems; speech/auditory rehabilitation; cochlear-implant evaluation when conventional amplification no longer provides adequate benefit. CEP250-specific implant outcomes are unavailable.
- **Vision:** correction of refractive error; tinted lenses for photophobia; low-vision rehabilitation; magnification, screen readers, orientation/mobility training; management of cataract or epiretinal membrane when clinically indicated.
- **Surveillance:** periodic audiograms and ophthalmic examination with OCT, FAF, visual fields, and ERG according to age and findings.
- **Communication planning:** introduce accessible communication and dual-sensory supports early rather than waiting for advanced visual loss.
- **Genetic care:** molecular confirmation, cascade testing, and reproductive counseling.

Suggested NCIT intervention concepts include Genetic Testing, Genetic Counseling, Electroretinography, Optical Coherence Tomography, Pure Tone Audiometry, Hearing Aid Device, Cochlear Implantation, Low Vision Rehabilitation, Assistive Device, and Gene Therapy—the last marked experimental. No CEP250 pharmacogenomic association or treatment-response statistic is available.

## 13. Prevention

Primary prevention through lifestyle modification, immunization, medication, or environmental control is not available. Vaccination and infectious prophylaxis are not disease-specific. Reproductive options after identifying familial variants include carrier testing of relatives/partners, prenatal diagnosis, and preimplantation genetic testing for monogenic disease, undertaken with nondirective genetic counseling.

Secondary prevention consists of **cascade testing and anticipatory surveillance**. At-risk siblings with biallelic variants should receive baseline audiology and retinal evaluation even if asymptomatic because hearing or retinal manifestations may be delayed. Tertiary prevention includes prompt amplification, accessible communication, low-vision rehabilitation, fall and mobility assessment, and educational/workplace accommodations. Population newborn screening for CEP250 is not established; standard newborn hearing screening may miss later-progressive loss.

## 14. Other species and natural disease

The orthologous **Cep250** gene has been studied in laboratory mouse (*Mus musculus*, NCBI Taxonomy **10090**). C-Nap1/CEP250 is evolutionarily conserved in vertebrate centrosome-linker biology. No well-validated naturally occurring veterinary syndrome exactly equivalent to human CRDHL2, breed-specific risk, VBO annotation, zoonotic transmission, or cross-species infectious susceptibility was identified. The condition is genetic and noncommunicable.

## 15. Model organisms and experimental systems

### Mouse models

1. **p.Arg188Ter-corresponding knock-in mouse (2019):** homozygotes showed reduced retinal thickness and ERG responses, with ciliary/outer-segment protein mislocalization. It models retinal disease but hearing was not initially evaluated. The human-study abstract states: “The homozygous knockin mice showed significantly reduced retinal thickness and ERG responses.” DOI: https://doi.org/10.1002/humu.23759; accepted 2 April 2019. (huang2019functionalcharacterizationof pages 1-2)

2. **Exon 6–7 knockout (2023):** ffERG was normal at six months but declined progressively; by 20 months photopic and scotopic amplitudes were very low, histology confirmed retinal degeneration, and ABR thresholds were significantly increased. This late-onset dual-sensory phenotype is unusually faithful relative to many Usher mouse models. Published 1 March 2023; DOI: https://doi.org/10.1167/tvst.12.3.3. (abudiab2023homozygousknockoutof pages 1-2)

3. **CRISPR deletion of exons 3–12/8,593 bp (2023 retinal study):** at P90/P180, mice exhibited retinal thinning, reduced ERG responses, photoreceptor loss/apoptosis, and the 298-gene RNA-seq signature described above. (chen2023rnaseqanalysisreveals pages 1-2, chen2023rnaseqanalysisreveals pages 5-7)

4. **Same/similar exons 3–12 knockout, cochlear analysis (2023–2024):** hearing thresholds were elevated particularly at 20–30 kHz; basal-turn hair-cell loss was highly significant (reported p<0.0001), while heterozygotes and swimming behavior were normal. The June 2024 report is a **preprint**, so its conclusions require peer-reviewed confirmation. DOI: https://doi.org/10.21203/rs.3.rs-4515679/v1. (nan2024thecochlearmorphology pages 1-5, nan2024thecochlearmorphology pages 5-8)

### Cellular systems

NIH3T3 heterologous expression demonstrated cytosolic mislocalization of p.Gln1171Ter C-Nap1. CEP250-disrupted retinal/RPE-derived cellular systems have also supported ciliary involvement. Limitations include overexpression, nonhuman cell context, and the observation that general primary cilia can form normally after C-Nap1 loss; specialized photoreceptor and hair-cell maintenance may therefore be more relevant than universal ciliogenesis failure. (kang2023novelvariantin pages 6-9, kang2023novelvariantin pages 11-12)

No validated CEP250 patient-derived iPSC retinal organoid, cochlear organoid, zebrafish CRDHL2 model, Drosophila model, or therapeutic rescue study was identified in the retrieved evidence.

## Knowledge-base ontology crosswalk

The following crosswalk distinguishes direct human observations from model-derived suggestions.

| Domain | Item | Suggested ontology mapping(s) | Key details for KB entry | Evidence level | Citations |
|---|---|---|---|---|---|
| Disease identifiers | Cone-rod dystrophy and hearing loss 2 | MONDO:0020780; OMIM: 618358 | Rare Mendelian oto-retinal disorder linked to biallelic CEP250; often described as atypical Usher-like disease rather than classic Usher subtype | Direct human disease-level resource and case-series context | (abudiab2023homozygousknockoutof pages 1-2, igelman2021expandingtheclinical pages 3-5, fustergarcia2018highthroughputsequencingfor pages 10-10) |
| Synonyms | CEP250-related CRDHL2; atypical Usher syndrome; Usher-like disease; cone-rod dystrophy with sensorineural hearing loss | Suggested synonym set only | Literature uses overlapping labels; disease boundaries remain somewhat fluid because CEP250 alleles can also present as nonsyndromic RP or nonsyndromic hearing loss | Direct human, with nomenclature caveat | (kang2023novelvariantin pages 1-2, fustergarcia2018highthroughputsequencingfor pages 10-10) |
| Core phenotype | Progressive sensorineural hearing loss | Suggested HPO: Sensorineural hearing impairment HP:0000407; Progressive hearing impairment HP:0001731 | Human CEP250 series: onset reported from <10 to 24 years; RP1973 had bilateral moderate-severe progressive hearing loss starting at age 13; no vestibular symptoms reported in the 2021 series | Direct human | (igelman2021expandingtheclinical pages 5-7, fustergarcia2018highthroughputsequencingfor pages 4-5) |
| Core phenotype | Mild cone-predominant retinal dysfunction / cone-rod dystrophy spectrum | Suggested HPO: Cone-rod dystrophy HP:0000548; Cone dystrophy HP:0000547; Abnormality of electroretinogram HP:0001311 | Age of ocular onset in CEP250 cases ranged 13-30 years in multicenter series; one tested patient showed mild cone dystrophy with normal rod function on ffERG; literature also includes late-onset cone-rod dystrophy | Direct human | (igelman2021expandingtheclinical pages 5-7, abudiab2023homozygousknockoutof pages 1-2, fustergarcia2018highthroughputsequencingfor pages 10-10) |
| Core phenotype | Photophobia and reduced visual acuity | Suggested HPO: Photophobia HP:0000613; Reduced visual acuity HP:0007663 | RP1973 had late-onset progressive visual decline with photophobia; BCVA in CEP250 series ranged about 20/60 to 20/200 | Direct human | (fustergarcia2018highthroughputsequencingfor pages 4-5, igelman2021expandingtheclinical pages 5-7) |
| Core phenotype | Subtle to mild retinal structural abnormality | Suggested HPO: Outer retinal atrophy HP:0030498; Thinning of outer nuclear layer HP:0033667; Abnormal fundus autofluorescence HP:0030636 | Color fundus may be normal or mildly abnormal; FAF showed subtle peripheral/peripapillary changes; OCT showed outer retinal atrophy, ONL thinning, and subtle EZ/IZ disruption | Direct human | (igelman2021expandingtheclinical pages 5-7, fustergarcia2018highthroughputsequencingfor pages 4-5) |
| Core phenotype | Retinitis pigmentosa-like fundus changes in some cases | Suggested HPO: Retinitis pigmentosa HP:0000510; Bone spicule pigmentation of the retina HP:0007703; Attenuated retinal blood vessels HP:0007763 | RP1973 showed mid-peripheral bone-spicule pigment migration and narrowed peripheral vessels, supporting overlap with RP/Usher-like phenotypes | Direct human | (fustergarcia2018highthroughputsequencingfor pages 4-5) |
| Core phenotype | Vestibular involvement | Suggested HPO: Abnormal vestibular function HP:0001751 | No vestibular symptoms were reported in the CEP250 patients of the 2021 multicenter series; vestibular dysfunction therefore appears absent or uncommon in currently described CRDHL2 cases | Direct human negative finding | (igelman2021expandingtheclinical pages 5-7) |
| Gene / protein | CEP250 / C-Nap1 | HGNC gene symbol: CEP250; OMIM gene: 609689 | Encodes centrosome-associated C-Nap1, a centrosome linker/cohesion protein also localized in photoreceptor/basal-body contexts | Human molecular + broader cell biology | (kang2023novelvariantin pages 1-2, huang2019functionalcharacterizationof pages 1-2) |
| Inheritance | Autosomal recessive | Suggested HPO: Autosomal recessive inheritance HP:0000007 | Disease is associated with biallelic CEP250 variants; reported affected individuals include homozygous and compound-heterozygous cases | Direct human | (abudiab2023homozygousknockoutof pages 1-2, igelman2021expandingtheclinical pages 5-7, fustergarcia2018highthroughputsequencingfor pages 4-5) |
| Variant spectrum relevant to CRDHL2 | Truncating alleles predominate | Suggested sequence ontology classes: nonsense_variant, frameshift_variant | All CEP250 variants in the 2021 atypical Usher cohort were novel nonsense or frameshift variants; reported syndromic examples include p.R1155*, p.K1113*, p.R1336*, and Japanese family compound heterozygous nonsense variants | Direct human, partially summarized across studies | (igelman2021expandingtheclinical pages 5-7, abudiab2023homozygousknockoutof pages 1-2, fustergarcia2018highthroughputsequencingfor pages 10-10, huang2019functionalcharacterizationof pages 4-6) |
| Allelic heterogeneity caveat | Nonsyndromic RP or nonsyndromic hearing loss can also result from CEP250 variants | Suggested note, not ontology assertion | Missense and some nonsense alleles have been reported in nonsyndromic RP or progressive hearing loss without retinal degeneration at time of report; genotype-phenotype correlation remains incomplete | Direct human with caution | (kang2023novelvariantin pages 1-2, huang2019functionalcharacterizationof pages 1-2, kang2023novelvariantin pages 9-11) |
| Organ / system | Eye / retina | Suggested UBERON: retina UBERON:0000966; eye UBERON:0000970 | Primary visual tissue affected; human imaging points to outer retina involvement | Direct human | (igelman2021expandingtheclinical pages 5-7, fustergarcia2018highthroughputsequencingfor pages 4-5) |
| Organ / system | Inner ear / cochlea | Suggested UBERON: inner ear UBERON:0001844; cochlea UBERON:0001853 | Primary auditory tissue affected; progressive SNHL is a core disease manifestation | Direct human; mouse supports tissue localization | (igelman2021expandingtheclinical pages 5-7, kang2023novelvariantin pages 1-2, nan2024thecochlearmorphology pages 1-5) |
| Tissue / cell type | Photoreceptors | Suggested CL: photoreceptor cell CL:0000679; rod photoreceptor cell CL:0000604; cone photoreceptor cell CL:0000710 | Human ffERG and OCT support photoreceptor dysfunction, with cone involvement possibly greater in some cases | Direct human; mouse mechanistic support | (igelman2021expandingtheclinical pages 5-7, chen2023rnaseqanalysisreveals pages 1-2) |
| Tissue / cell type | Cochlear hair cells | Suggested CL: auditory hair cell CL:0000589; inner hair cell / outer hair cell suggested | Cep250 is expressed in murine inner and outer hair cells; knockout models show hair-cell degeneration and high-frequency hearing loss | Mouse/in vitro inference supporting human auditory phenotype | (kang2023novelvariantin pages 1-2, nan2024thecochlearmorphology pages 1-5) |
| Subcellular compartment | Centrosome / centriole proximal end / basal body / ciliary region | Suggested GO CC: centrosome GO:0005813; centriole GO:0005814; basal body GO:0005932; ciliary basal body suggested | C-Nap1 is a centrosomal linker protein; human variant p.Gln1171Ter mislocalized from centrosome to cytosol in NIH3T3 cells; literature places CEP250 in photoreceptor ciliary/basal-body contexts | In vitro + broader biology; indirect for CRDHL2 | (kang2023novelvariantin pages 1-2, huang2019functionalcharacterizationof pages 1-2, kang2023novelvariantin pages 6-9) |
| Biological process | Centrosome cohesion / ciliogenesis / cilium organization | Suggested GO BP: centrosome cycle / centrosome cohesion suggested; cilium organization GO:0044782; ciliogenesis suggested | Mechanistic model: loss of C-Nap1 disrupts centrosome localization/cohesion and ciliary homeostasis, impairing photoreceptor and hair-cell maintenance | In vitro + mouse inference | (kang2023novelvariantin pages 1-2, huang2019functionalcharacterizationof pages 1-2, kang2023novelvariantin pages 6-9) |
| Biological process | Photoreceptor degeneration and apoptosis | Suggested GO BP: photoreceptor cell maintenance suggested; apoptotic process GO:0006915 | Cep250-deficient retina shows reduced photoreceptors and increased TUNEL positivity in mice | Mouse inference | (chen2023rnaseqanalysisreveals pages 1-2) |
| Biological process | Stress/signaling dysregulation in retina | Suggested GO/Pathway terms: MAPK cascade GO:0000165; cyclic nucleotide signaling suggested | RNA-seq in Cep250 KO retina found 149 upregulated and 149 downregulated genes; enriched pathways included cGMP-PKG, MAPK, edn2-fgf2 axis, thyroid hormone synthesis; ER protein processing downregulated | Mouse inference | (chen2023rnaseqanalysisreveals pages 1-2, chen2023rnaseqanalysisreveals pages 5-7) |
| Diagnostics | Molecular diagnosis | Suggested NCIT: Genetic Testing; Whole Exome Sequencing; Targeted Next-Generation Sequencing Panel | WES and targeted high-throughput panels have identified causal biallelic CEP250 variants; useful especially in atypical Usher/dual sensory phenotypes | Direct human real-world implementation | (kang2023novelvariantin pages 1-2, fustergarcia2018highthroughputsequencingfor pages 10-10, igelman2021expandingtheclinical pages 3-5) |
| Diagnostics | Ophthalmic functional testing | Suggested NCIT: Electroretinography | ffERG can show mild cone dystrophy with normal rod function in some human CEP250 cases; useful for disease characterization | Direct human | (igelman2021expandingtheclinical pages 5-7) |
| Diagnostics | Retinal imaging | Suggested NCIT: Optical Coherence Tomography; Fundus Autofluorescence Imaging; Fundus Photography; Visual Field Examination | Human cases showed OCT outer retinal atrophy/ONL thinning/EZ-IZ disruption and subtle FAF abnormalities; visual fields may range from near-normal wide fields to marked constriction | Direct human | (igelman2021expandingtheclinical pages 5-7, fustergarcia2018highthroughputsequencingfor pages 4-5, igelman2021expandingtheclinical pages 3-5) |
| Diagnostics | Audiologic testing | Suggested NCIT: Pure Tone Audiometry; Auditory Brainstem Response | Progressive SNHL is central; pure-tone audiograms used clinically in human hearing studies; ABR is established in mouse models and can support translational studies | Human + mouse | (kang2023novelvariantin pages 1-2, abudiab2023homozygousknockoutof pages 1-2, nan2024thecochlearmorphology pages 1-5) |
| Differential diagnosis | Classic Usher syndrome types 1-3; CEP78-, ARSG-, ABHD12-related atypical Usher; nonsyndromic RP; nonsyndromic AR hearing loss | Suggested note | Clinical overlap is substantial; genotype-first evaluation is recommended in atypical presentations combining retinal disease with progressive SNHL | Direct human | (igelman2021expandingtheclinical pages 3-5, igelman2021expandingtheclinical pages 5-7, fustergarcia2018highthroughputsequencingfor pages 10-10) |
| Management | Sensory surveillance and supportive care | Suggested NCIT: Ophthalmologic Examination; Audiologic Monitoring; Genetic Counseling | No CEP250-specific disease-modifying therapy identified; current care centers on longitudinal eye/hearing follow-up and counseling | Direct evidence for absence of targeted therapy; standard-of-care inference | (fustergarcia2018highthroughputsequencingfor pages 10-10) |
| Management | Hearing rehabilitation | Suggested NCIT: Hearing Aid Device; Cochlear Implantation | Disease-specific CEP250 outcome data not identified, but progressive SNHL makes standard hearing rehabilitation relevant in practice | Indirect clinical inference | (fustergarcia2018highthroughputsequencingfor pages 10-10, kang2023novelvariantin pages 1-2) |
| Management | Low-vision and disability support | Suggested NCIT: Low Vision Rehabilitation; Assistive Device | Disease-specific studies absent, but visual acuity loss, photophobia, and retinal degeneration support standard low-vision measures | Indirect clinical inference | (igelman2021expandingtheclinical pages 5-7, fustergarcia2018highthroughputsequencingfor pages 4-5) |
| Advanced therapeutics | Gene therapy / RNA therapy / trials | Suggested NCIT: Gene Therapy | No CEP250-specific interventional trial or approved therapy was identified in gathered evidence; mouse models were proposed as platforms for future therapy development | Negative evidence + preclinical rationale | (abudiab2023homozygousknockoutof pages 1-2, fustergarcia2018highthroughputsequencingfor pages 10-10) |
| Evidence caveat | Human evidence base is very small | Suggested note | Current phenotype definition relies on a small number of families/cases, plus retrospective multicenter aggregation of only three CEP250 patients in one series | Direct human caveat | (igelman2021expandingtheclinical pages 5-7, fustergarcia2018highthroughputsequencingfor pages 10-10) |
| Evidence caveat | Variant-phenotype correlation remains unresolved | Suggested note | Truncating alleles are enriched in syndromic cases, but CEP250 can also underlie nonsyndromic retinal or auditory disease; penetrance and age dependence are not yet well quantified | Direct human caveat | (kang2023novelvariantin pages 1-2, huang2019functionalcharacterizationof pages 1-2, kang2023novelvariantin pages 9-11) |
| Evidence caveat | Epidemiology and modifiers largely unavailable | Suggested note | No robust disease-specific prevalence, incidence, penetrance, sex ratio, environmental modifiers, or protective factors were identified in the gathered literature | Absence of evidence | (fustergarcia2018highthroughputsequencingfor pages 10-10) |


*Table: This table condenses the gathered evidence into a compact knowledge-base crosswalk for CEP250-associated CRDHL2, linking phenotype, anatomy, mechanism, diagnostics, and management to suggested ontology terms. It also flags where statements are supported directly by human data versus mouse or in-vitro inference.*

## Key primary sources and exact abstract quotations

1. **Fuster-García et al., Scientific Reports, published November 2018.** DOI: https://doi.org/10.1038/s41598-018-35085-0. Abstract: “we detected two novel nonsense mutations in CEP250 in a patient with a disease mimicking Usher syndrome that associates visual impairment due to cone-rod dystrophy and progressive hearing loss.” The study’s 82.8% detection ratio concerns the complete 77-person Usher cohort. (fustergarcia2018highthroughputsequencingfor pages 1-2)

2. **Huang et al., Human Mutation, accepted 2 April 2019.** DOI: https://doi.org/10.1002/humu.23759. Abstract: “we report the identification of a mutation (c.562C>T, p.R188*) in the CEP250 in a consanguineous family with nonsyndromic RP” and “The homozygous knockin mice showed significantly reduced retinal thickness and ERG responses.” (huang2019functionalcharacterizationof pages 1-2)

3. **Igelman et al., Ophthalmic Genetics, 2021.** DOI: https://doi.org/10.1080/13816810.2021.1946704. Abstract: “Nonsense and frameshift variants in CEP250 showed mild retinal disease with progressive, non-congenital SNHL.” This is the best comparative human phenotype series, but it included only three CEP250 patients. (igelman2021expandingtheclinical pages 5-7)

4. **Abu-Diab et al., Translational Vision Science & Technology, published 1 March 2023.** DOI: https://doi.org/10.1167/tvst.12.3.3. Abstract: “At 6 months, the ffERG was normal, but it decreased gradually with age” and “ABR tests illustrated that hearing threshold significantly increased at the age of 20 months.” (abudiab2023homozygousknockoutof pages 1-2)

5. **Chen et al., International Journal of Molecular Sciences, published 16 May 2023.** DOI: https://doi.org/10.3390/ijms24108843. Abstract: “An RNA-seq analysis showed that 149 genes were upregulated and another 149 genes were downregulated” and “The dysregulation of the cGMP-PKG-MAPK pathways may contribute to the pathogenesis of cilia-related retinal degeneration.” (chen2023rnaseqanalysisreveals pages 1-2)

6. **Kang et al., Cells, published 21 September 2023.** DOI: https://doi.org/10.3390/cells12182328. Abstract: “we identified a novel nonsense homozygous variant in CEP250 (c.3511C>T; p.Gln1171Ter)” in progressive nonsyndromic SNHL and found that the truncated protein “was not localized at the centrosome but was dispersed in the cytosol.” (kang2023novelvariantin pages 1-2)

7. **Nan et al., preprint posted 19 June 2024.** DOI: https://doi.org/10.21203/rs.3.rs-4515679/v1. Abstract: Cep250-null mice had high-frequency hearing impairment, reduced cochlear hair-cell numbers, unaffected swimming behavior, and no significant heterozygous hearing change. This is recent but not equivalent to peer-reviewed clinical evidence. (nan2024thecochlearmorphology pages 1-5)

## Evidence limitations and expert interpretation

The principal limitation is extreme data scarcity. Percentages from cohorts selected for retinal disease or atypical Usher syndrome are subject to ascertainment bias and must not be treated as penetrance estimates. Genotype–phenotype correlations are provisional: truncating alleles predominate in CRDHL2, yet apparently similar alleles can present as retinal-only or hearing-only disease, possibly because of age, residual protein function, background modifiers, or incomplete phenotyping. The most defensible current practice is therefore a **genotype-informed but phenotype-led longitudinal diagnosis**: any person with biallelic CEP250 variants and one sensory manifestation should undergo repeated assessment of the other sensory system. The 2018 investigators similarly recommended “thorough clinical examinations,” particularly for cone involvement. (kang2023novelvariantin pages 9-11, fustergarcia2018highthroughputsequencingfor pages 10-10)

No disease-specific epidemiology, validated clinical criteria, prognostic biomarker, environmental modifier, quality-of-life statistic, approved targeted treatment, or human therapeutic trial was identified. Those fields should be marked unavailable rather than extrapolated from general Usher syndrome or inherited-retinal-disease data.

References

1. (igelman2021expandingtheclinical pages 5-7): Austin D. Igelman, Cristy Ku, Mariana Matioli da Palma, Michalis Georgiou, Elena R. Schiff, Byron L. Lam, Eeva-Marja Sankila, Jeeyun Ahn, Lindsey Pyers, Ajoy Vincent, Juliana Maria Ferraz Sallum, Wadih M. Zein, Jin Kyun Oh, Ramiro S. Maldonado, Joseph Ryu, Stephen H. Tsang, Michael B. Gorin, Andrew R. Webster, Michel Michaelides, Paul Yang, and Mark E. Pennesi. Expanding the clinical phenotype in patients with disease causing variants associated with atypical usher syndrome. Ophthalmic Genetics, 42:664-673, Jul 2021. URL: https://doi.org/10.1080/13816810.2021.1946704, doi:10.1080/13816810.2021.1946704. This article has 35 citations and is from a peer-reviewed journal.

2. (chen2023rnaseqanalysisreveals pages 1-2): Chong Chen, Yu Rong, Youyuan Zhuang, Cheng Tang, Qian Liu, Peng Lin, Dandan Li, Xinyi Zhao, Fan Lu, Jia Qu, and Xinting Liu. Rna-seq analysis reveals an essential role of the cgmp-pkg-mapk pathways in retinal degeneration caused by cep250 deficiency. International Journal of Molecular Sciences, 24:8843, May 2023. URL: https://doi.org/10.3390/ijms24108843, doi:10.3390/ijms24108843. This article has 3 citations.

3. (nan2024thecochlearmorphology pages 5-8): Benyu Nan, Xi Gu, Xinlei Wu, Keyang Chen, Chuqin Zhang, Qijun Fan, Yingying Chen, Bobei Chen, and Xiufeng Huang. The cochlear morphology alteration and hearing loss in cep250 knockout mice. Jun 2024. URL: https://doi.org/10.21203/rs.3.rs-4515679/v1, doi:10.21203/rs.3.rs-4515679/v1.

4. (abudiab2023homozygousknockoutof pages 1-2): Alaa Abu-Diab, Prakadeeswari Gopalakrishnan, Chen Matsevich, Marije de Jong, Alexey Obolensky, Ayat Khalaileh, Manar Salameh, Ayala Ejzenberg, Menachem Gross, Eyal Banin, Dror Sharon, and Samer Khateb. Homozygous knockout of cep250 leads to a relatively late-onset retinal degeneration and sensorineural hearing loss in mice. Translational Vision Science & Technology, 12:3, Mar 2023. URL: https://doi.org/10.1167/tvst.12.3.3, doi:10.1167/tvst.12.3.3. This article has 6 citations and is from a peer-reviewed journal.

5. (fustergarcia2018highthroughputsequencingfor pages 1-2): Carla Fuster-García, Gema García-García, Teresa Jaijo, Neus Fornés, Carmen Ayuso, Miguel Fernández-Burriel, Ana Sánchez-De la Morena, Elena Aller, and José M. Millán. High-throughput sequencing for the molecular diagnosis of usher syndrome reveals 42 novel mutations and consolidates cep250 as usher-like disease causative. Scientific Reports, Nov 2018. URL: https://doi.org/10.1038/s41598-018-35085-0, doi:10.1038/s41598-018-35085-0. This article has 55 citations and is from a peer-reviewed journal.

6. (kang2023novelvariantin pages 9-11): Minjin Kang, Jung Ah Kim, Mee Hyun Song, Sun Young Joo, Se Jin Kim, Seung Hyun Jang, Ho Lee, Je Kyung Seong, Jae Young Choi, Heon Yung Gee, and Jinsei Jung. Novel variant in cep250 causes protein mislocalization and leads to nonsyndromic autosomal recessive type of progressive hearing loss. Cells, 12:2328, Sep 2023. URL: https://doi.org/10.3390/cells12182328, doi:10.3390/cells12182328. This article has 8 citations.

7. (kang2023novelvariantin pages 1-2): Minjin Kang, Jung Ah Kim, Mee Hyun Song, Sun Young Joo, Se Jin Kim, Seung Hyun Jang, Ho Lee, Je Kyung Seong, Jae Young Choi, Heon Yung Gee, and Jinsei Jung. Novel variant in cep250 causes protein mislocalization and leads to nonsyndromic autosomal recessive type of progressive hearing loss. Cells, 12:2328, Sep 2023. URL: https://doi.org/10.3390/cells12182328, doi:10.3390/cells12182328. This article has 8 citations.

8. (huang2019functionalcharacterizationof pages 1-2): Xiu‐Feng Huang, Lue Xiang, Xiao‐Long Fang, Wei‐Qin Liu, You‐Yuan Zhuang, Zhen‐Ji Chen, Ren‐Juan Shen, Wan Cheng, Ru‐Yi Han, Si‐Si Zheng, Xue‐Jiao Chen, Xiaoling Liu, and Zi‐Bing Jin. Functional characterization of <i>cep250</i> variant identified in nonsyndromic retinitis pigmentosa. Apr 2019. URL: https://doi.org/10.1002/humu.23759, doi:10.1002/humu.23759. This article has 27 citations and is from a domain leading peer-reviewed journal.

9. (fustergarcia2018highthroughputsequencingfor pages 4-5): Carla Fuster-García, Gema García-García, Teresa Jaijo, Neus Fornés, Carmen Ayuso, Miguel Fernández-Burriel, Ana Sánchez-De la Morena, Elena Aller, and José M. Millán. High-throughput sequencing for the molecular diagnosis of usher syndrome reveals 42 novel mutations and consolidates cep250 as usher-like disease causative. Scientific Reports, Nov 2018. URL: https://doi.org/10.1038/s41598-018-35085-0, doi:10.1038/s41598-018-35085-0. This article has 55 citations and is from a peer-reviewed journal.

10. (kang2023novelvariantin pages 6-9): Minjin Kang, Jung Ah Kim, Mee Hyun Song, Sun Young Joo, Se Jin Kim, Seung Hyun Jang, Ho Lee, Je Kyung Seong, Jae Young Choi, Heon Yung Gee, and Jinsei Jung. Novel variant in cep250 causes protein mislocalization and leads to nonsyndromic autosomal recessive type of progressive hearing loss. Cells, 12:2328, Sep 2023. URL: https://doi.org/10.3390/cells12182328, doi:10.3390/cells12182328. This article has 8 citations.

11. (kang2023novelvariantin pages 11-12): Minjin Kang, Jung Ah Kim, Mee Hyun Song, Sun Young Joo, Se Jin Kim, Seung Hyun Jang, Ho Lee, Je Kyung Seong, Jae Young Choi, Heon Yung Gee, and Jinsei Jung. Novel variant in cep250 causes protein mislocalization and leads to nonsyndromic autosomal recessive type of progressive hearing loss. Cells, 12:2328, Sep 2023. URL: https://doi.org/10.3390/cells12182328, doi:10.3390/cells12182328. This article has 8 citations.

12. (fustergarcia2018highthroughputsequencingfor pages 10-10): Carla Fuster-García, Gema García-García, Teresa Jaijo, Neus Fornés, Carmen Ayuso, Miguel Fernández-Burriel, Ana Sánchez-De la Morena, Elena Aller, and José M. Millán. High-throughput sequencing for the molecular diagnosis of usher syndrome reveals 42 novel mutations and consolidates cep250 as usher-like disease causative. Scientific Reports, Nov 2018. URL: https://doi.org/10.1038/s41598-018-35085-0, doi:10.1038/s41598-018-35085-0. This article has 55 citations and is from a peer-reviewed journal.

13. (huang2019functionalcharacterizationof pages 4-6): Xiu‐Feng Huang, Lue Xiang, Xiao‐Long Fang, Wei‐Qin Liu, You‐Yuan Zhuang, Zhen‐Ji Chen, Ren‐Juan Shen, Wan Cheng, Ru‐Yi Han, Si‐Si Zheng, Xue‐Jiao Chen, Xiaoling Liu, and Zi‐Bing Jin. Functional characterization of <i>cep250</i> variant identified in nonsyndromic retinitis pigmentosa. Apr 2019. URL: https://doi.org/10.1002/humu.23759, doi:10.1002/humu.23759. This article has 27 citations and is from a domain leading peer-reviewed journal.

14. (chen2023rnaseqanalysisreveals pages 5-7): Chong Chen, Yu Rong, Youyuan Zhuang, Cheng Tang, Qian Liu, Peng Lin, Dandan Li, Xinyi Zhao, Fan Lu, Jia Qu, and Xinting Liu. Rna-seq analysis reveals an essential role of the cgmp-pkg-mapk pathways in retinal degeneration caused by cep250 deficiency. International Journal of Molecular Sciences, 24:8843, May 2023. URL: https://doi.org/10.3390/ijms24108843, doi:10.3390/ijms24108843. This article has 3 citations.

15. (nan2024thecochlearmorphology pages 8-16): Benyu Nan, Xi Gu, Xinlei Wu, Keyang Chen, Chuqin Zhang, Qijun Fan, Yingying Chen, Bobei Chen, and Xiufeng Huang. The cochlear morphology alteration and hearing loss in cep250 knockout mice. Jun 2024. URL: https://doi.org/10.21203/rs.3.rs-4515679/v1, doi:10.21203/rs.3.rs-4515679/v1.

16. (nan2024thecochlearmorphology pages 1-5): Benyu Nan, Xi Gu, Xinlei Wu, Keyang Chen, Chuqin Zhang, Qijun Fan, Yingying Chen, Bobei Chen, and Xiufeng Huang. The cochlear morphology alteration and hearing loss in cep250 knockout mice. Jun 2024. URL: https://doi.org/10.21203/rs.3.rs-4515679/v1, doi:10.21203/rs.3.rs-4515679/v1.

17. (fustergarcia2018highthroughputsequencingfor pages 3-4): Carla Fuster-García, Gema García-García, Teresa Jaijo, Neus Fornés, Carmen Ayuso, Miguel Fernández-Burriel, Ana Sánchez-De la Morena, Elena Aller, and José M. Millán. High-throughput sequencing for the molecular diagnosis of usher syndrome reveals 42 novel mutations and consolidates cep250 as usher-like disease causative. Scientific Reports, Nov 2018. URL: https://doi.org/10.1038/s41598-018-35085-0, doi:10.1038/s41598-018-35085-0. This article has 55 citations and is from a peer-reviewed journal.

18. (igelman2021expandingtheclinical pages 3-5): Austin D. Igelman, Cristy Ku, Mariana Matioli da Palma, Michalis Georgiou, Elena R. Schiff, Byron L. Lam, Eeva-Marja Sankila, Jeeyun Ahn, Lindsey Pyers, Ajoy Vincent, Juliana Maria Ferraz Sallum, Wadih M. Zein, Jin Kyun Oh, Ramiro S. Maldonado, Joseph Ryu, Stephen H. Tsang, Michael B. Gorin, Andrew R. Webster, Michel Michaelides, Paul Yang, and Mark E. Pennesi. Expanding the clinical phenotype in patients with disease causing variants associated with atypical usher syndrome. Ophthalmic Genetics, 42:664-673, Jul 2021. URL: https://doi.org/10.1080/13816810.2021.1946704, doi:10.1080/13816810.2021.1946704. This article has 35 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Cone-rod_Dystrophy_And_Hearing_Loss_2-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 2 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0020780` (3 mentions) - the report calls it "if available"; MONDO calls it **cone-rod dystrophy and hearing loss 2**
- `HP:0000613` (2 mentions) - the report calls it "Case-level, frequency unknown"; HP calls it **Photophobia**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0001731` (2 mentions) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0000547` (obsolete Tapetoretinal degeneration) (2 mentions) - replaced by `HP:0000510`
- `GO:0005932` (GO_0005932) (2 mentions) - replaced by `GO:0036064`