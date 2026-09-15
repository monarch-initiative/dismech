---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T17:55:48.092187'
end_time: '2026-09-05T18:06:03.158779'
duration_seconds: 615.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hereditary Hyperferritinemia with Congenital Cataracts
  mondo_id: MONDO:0010952
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 59
reference_validation:
  total_references: 10
  verified: 9
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.1
  relevance_assessed: 9
  on_topic: 2
  unresolved_references:
  - DOI:10.1007/s00439-017-1835-3
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 4
  verified: 4
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 2
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0010952
    reported_labels:
    - if available
    ontology_label: hereditary hyperferritinemia with congenital cataracts
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hereditary_Hyperferritinemia_With_Congenital_Cataracts-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Hyperferritinemia with Congenital Cataracts
- **MONDO ID:** MONDO:0010952 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Hyperferritinemia with Congenital Cataracts** covering all of the
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
- **Disease Name:** Hereditary Hyperferritinemia with Congenital Cataracts
- **MONDO ID:** MONDO:0010952 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Hyperferritinemia with Congenital Cataracts** covering all of the
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


# Hereditary Hyperferritinemia–Cataract Syndrome (HHCS)

## Executive summary

Hereditary hyperferritinemia–cataract syndrome (HHCS), also called hereditary hyperferritinemia with congenital cataracts, is a rare Mendelian disorder caused by germline noncoding variants in the iron-responsive element (IRE) of **FTL**, the ferritin light-chain gene. These variants impair post-transcriptional repression of FTL, causing iron-independent overproduction of L-ferritin. The defining phenotype is persistent, often marked hyperferritinemia **without systemic iron overload**, together with bilateral, usually early-onset and slowly progressive nuclear cataracts containing L-ferritin-rich deposits. The major clinical hazard is not systemic disease but misdiagnosis as hemochromatosis, followed by unnecessary liver biopsy, phlebotomy, or iron chelation. Cataract surgery is the only established phenotype-directed intervention; there is no treatment indication for the ferritin elevation itself. (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7, eris2023hereditaryhyperferritinemiacataractsyndrome pages 4-5, piperno2023hereditaryhyperferritinemia pages 10-12)

The most useful knowledge-base summary is:

| Knowledge-base field | Evidence-supported summary | Key sources |
|---|---|---|
| Disease / identifiers | Hereditary hyperferritinemia-cataract syndrome (HHCS; OMIM #600886) is a rare Mendelian disorder characterized by persistent hyperferritinemia unrelated to body iron stores and early-onset bilateral cataracts. | [Piperno et al., 2023](https://doi.org/10.3390/ijms24032560); [Moravikova et al., 2020](https://doi.org/10.1016/j.jaapos.2020.07.014) (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7, piperno2023hereditaryhyperferritinemia pages 10-12) |
| Causal gene / inheritance | **FTL** (ferritin light-chain gene); usually heterozygous autosomal-dominant inheritance. De novo disease and rare homozygous affected individuals have been documented. | [Moravikova et al., 2020](https://doi.org/10.1016/j.jaapos.2020.07.014); [Van de Sompele et al., 2017](https://doi.org/10.1007/s00439-017-1835-3) (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7, sompele2017functionalcharacterizationofa pages 2-3) |
| Molecular lesion | Pathogenic noncoding substitutions, deletions, and insertion-deletions affect the iron-responsive element (IRE) in the **FTL** 5′ untranslated region, especially its upper stem, conserved hexaloop, and cytosine bulge. A 2019 review catalogued 36 point mutations, nine deletions, and two insertion-deletions associated with HHCS. | [Cadenas et al., 2019](https://doi.org/10.3390/ph12010017); [Millonig et al., 2010](https://doi.org/10.1186/1479-7364-4-4-250) (millonig2010hyperferritinaemiacataractsyndromeworldwide pages 9-10, cadenas2019lferritinonegene pages 5-8) |
| Core mechanism | IRE disruption reduces binding of iron-regulatory proteins IRP1/IRP2 and releases normal iron-dependent translational repression, causing constitutive excess L-ferritin synthesis. Functional EMSA evidence showed reduced IRP1 affinity for the c.-151A>G IRE. L-ferritin-rich deposits/crystals in the lens diffract light and produce cataract; absence of systemic iron excess distinguishes HHCS from hemochromatosis. | [Van de Sompele et al., 2017](https://doi.org/10.1007/s00439-017-1835-3); [Piperno et al., 2023](https://doi.org/10.3390/ijms24032560) (piperno2023hereditaryhyperferritinemia pages 10-12, sompele2017functionalcharacterizationofa pages 8-9, sompele2017functionalcharacterizationofa pages 2-3) |
| Ferritin / iron laboratory pattern | Persistent, often marked serum hyperferritinemia with normal serum iron, transferrin saturation, and body-iron stores. Reported serum ferritin is commonly about 700–2,000 µg/L; one seven-kindred series recorded minima of 740–1,960 µg/L (median 1,420 µg/L). Ferritin may fluctuate but did not increase with age in that series. | [Lachlan et al., 2004](https://doi.org/10.1038/sj.ejhg.5201252); [Cosentino et al., 2016](https://doi.org/10.3109/13816810.2015.1059460) (lachlan2004clinicalfeaturesand pages 1-2, cosentino2016hyperferritinemiacataractsyndromelongterm pages 1-6) |
| Ocular phenotype / onset | Bilateral, generally symmetrical nuclear cataracts can be congenital or recognized in infancy, childhood, or later adulthood. Typical findings include punctate white “breadcrumb-like,” crystalline, sunflower-like, or radial opacities. Cataracts are usually slowly progressive; visual severity and age at surgery vary within and among families. In one British series, median diagnosis was five years and median extraction age was 25 years (range 22–42). | [Lachlan et al., 2004](https://doi.org/10.1038/sj.ejhg.5201252); [Cosentino et al., 2016](https://doi.org/10.3109/13816810.2015.1059460) (lachlan2004clinicalfeaturesand pages 3-4, lachlan2004clinicalfeaturesand pages 1-2, cosentino2016hyperferritinemiacataractsyndromelongterm pages 1-6) |
| Epidemiology | Worldwide distribution; approximate prevalence **1:200,000**, but this is an estimate rather than a population-registry measurement. A 2018 report noted approximately 160 known families/cases. No established sex bias is supported. | [Piperno et al., 2023](https://doi.org/10.3390/ijms24032560); [Ferro et al., 2018](https://doi.org/10.1177/1093526618755200) (ferro2018ftlc.168g>cmutation pages 1-2, piperno2023hereditaryhyperferritinemia pages 10-12) |
| Diagnosis | Suspect HHCS when isolated familial hyperferritinemia coexists with early bilateral cataracts and normal transferrin saturation. Evaluate blood count, serum iron, transferrin/TIBC, transferrin saturation, liver enzymes, and inflammatory causes; slit-lamp examination can reveal characteristic opacities. Confirm by sequencing the **FTL** 5′UTR/IRE and test relatives. Liver biopsy is generally unnecessary when iron overload has been excluded. | [Millonig et al., 2010](https://doi.org/10.1186/1479-7364-4-4-250); [Moravikova et al., 2020](https://doi.org/10.1016/j.jaapos.2020.07.014) (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7, millonig2010hyperferritinaemiacataractsyndromeworldwide pages 3-4) |
| Management | Hyperferritinemia itself requires no iron-removal treatment. Avoid phlebotomy and iron chelation unless independent iron overload is proven; misdiagnosis has caused iron-deficiency anemia and, in one report, life-threatening hyperammonemia during deferasirox therapy. Monitor vision and perform standard cataract extraction with intraocular-lens management when visual function warrants it. | [Moravikova et al., 2020](https://doi.org/10.1016/j.jaapos.2020.07.014); [Piperno et al., 2023](https://doi.org/10.3390/ijms24032560) (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7, eris2023hereditaryhyperferritinemiacataractsyndrome pages 4-5, piperno2023hereditaryhyperferritinemia pages 10-12) |
| Prognosis | Life-threatening systemic disease or shortened survival has not been demonstrated. Morbidity is predominantly visual and usually amenable to cataract surgery. Serum hyperferritinemia is lifelong but is not, by itself, evidence of organ iron injury. | [Millonig et al., 2010](https://doi.org/10.1186/1479-7364-4-4-250); [Piperno et al., 2023](https://doi.org/10.3390/ijms24032560) (millonig2010hyperferritinaemiacataractsyndromeworldwide pages 3-4, piperno2023hereditaryhyperferritinemia pages 10-12) |
| Evidence gaps | No robust incidence, sex-ratio, penetrance, quality-of-life, survival, or population carrier-frequency studies were identified. Genotype–phenotype prediction remains weak except that rare biallelic variants may be more severe. No HHCS-specific therapeutic trials, validated pharmacotherapy, gene/RNA therapy, direct disease animal model, or single-cell, spatial-transcriptomic, epigenomic, proteomic, metabolomic, or multi-omics study was found in the gathered evidence. | [Cadenas et al., 2019](https://doi.org/10.3390/ph12010017); [Shiels, 2024](https://doi.org/10.3390/genes15060785) (sompele2017functionalcharacterizationofa pages 8-9, cadenas2019lferritinonegene pages 5-8, shiels2024throughthecatmapa pages 20-21, shiels2024throughthecatmap pages 19-21) |


*Table: Concise evidence table covering the defining clinical, molecular, diagnostic, management, and epidemiologic features of HHCS, together with major evidence gaps. Claims are restricted to the gathered literature and distinguish estimated figures from directly observed findings.*

## Evidence framework and limitations

Evidence consists chiefly of multigeneration human families, small case series, biochemical studies of mutant IRE–IRP binding, and reviews. HHCS is so rare that registry-quality incidence, penetrance, survival, quality-of-life, and treatment-response data are unavailable. The most current disease-focused synthesis retrieved was Piperno et al., published January 2023; a June 2024 cataract-genetics review places FTL within the contemporary inherited-cataract landscape but adds no HHCS-specific therapy or model. (piperno2023hereditaryhyperferritinemia pages 10-12, shiels2024throughthecatmap pages 3-4, shiels2024throughthecatmap pages 19-21)

PMIDs were not present in the retrieved full-text metadata and therefore are not supplied speculatively. DOI links and publication dates are provided. Short quotations below are limited to wording verifiable in retrieved abstracts.

---

## 1. Disease information

### Definition

HHCS is an autosomal-dominant disorder characterized by persistent elevation of serum L-ferritin, normal body-iron stores and transferrin saturation, and bilateral congenital, juvenile, or presenile cataract. It should not be classified as hereditary hemochromatosis: the elevated ferritin reflects dysregulated ferritin synthesis rather than excess stored iron. (lachlan2004clinicalfeaturesand pages 1-2, millonig2010hyperferritinaemiacataractsyndromeworldwide pages 3-4, piperno2023hereditaryhyperferritinemia pages 10-12)

A landmark review defines it as follows: **“The hereditary hyperferritinaemia-cataract syndrome (HHCS) is characterised by an autosomal dominant cataract and high levels of serum ferritin without iron overload.”** [Millonig et al., April 2010](https://doi.org/10.1186/1479-7364-4-4-250). (millonig2010hyperferritinaemiacataractsyndromeworldwide pages 3-4)

### Identifiers and synonyms

- **MONDO:** MONDO:0010952, as supplied in the request.
- **OMIM phenotype:** **600886**.
- **Causal gene:** **FTL**, ferritin light polypeptide/ferritin light chain; chromosome 19.
- **Orphanet:** commonly represented as hereditary hyperferritinemia–cataract syndrome; database releases should be checked before storing a numeric ORPHA identifier because identifiers were not visible in the retrieved source text.
- **ICD-10/ICD-11:** no uniquely disease-specific code was verified. Operational coding generally requires separate cataract and abnormal-serum-enzyme/protein findings plus a rare-genetic-disease code where local systems permit.
- **MeSH:** no dedicated HHCS descriptor was verified; likely indexing concepts include *Cataract*, *Hyperferritinemia*, *Ferritins*, and *Genetic Diseases, Inborn*.
- **Synonyms:** hereditary hyperferritinemia-cataract syndrome; hereditary hyperferritinaemia-cataract syndrome; hyperferritinemia-cataract syndrome; hyperferritinaemia-cataract syndrome; HHCS; HCS; hereditary hyperferritinemia with congenital/early-onset cataract.

The report concerns **aggregated disease-level literature and published patients/families**, not individual EHR records.

---

## 2. Etiology, risk, protection, and environment

### Primary cause

The cause is a **germline FTL 5′-UTR IRE variant**—usually a heterozygous substitution, deletion, or insertion-deletion. The altered RNA stem-loop has reduced affinity for iron-regulatory proteins, releasing the normal iron-sensitive block on translation. (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7, millonig2010hyperferritinaemiacataractsyndromeworldwide pages 9-10, cadenas2019lferritinonegene pages 5-8)

A 2019 catalog reported **36 point mutations, nine deletions, and two insertion-deletions** associated with HHCS. Examples include c.-161C>T, c.-167C>T, c.-168G>C, c.-151A>G, and c.-164_-158del7. Nomenclature varies historically because variants were numbered relative to the IRE rather than consistently by HGVS; clinical reports should normalize against **NM_000146.3 or the current MANE transcript**. (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7, sompele2017functionalcharacterizationofa pages 2-3, cadenas2019lferritinonegene pages 3-5, cadenas2019lferritinonegene pages 5-8)

### Risk factors

- **Genetic:** carrying a pathogenic FTL IRE allele is the principal risk factor. Family history is strongly informative, but a confirmed de novo c.-167C>T case shows that a negative family history does not exclude HHCS. (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7)
- **Family history:** each child of a heterozygous affected person has a theoretical 50% transmission probability.
- **Biallelic state:** exceptionally, homozygous IRE variants occur. In the c.-151A>G family, the homozygous proband was more severely affected than heterozygous relatives, supporting a dosage effect for at least some alleles. This is not a general penetrance estimate. (sompele2017functionalcharacterizationofa pages 8-9, sompele2017functionalcharacterizationofa pages 2-3)
- **Sex, ancestry, age:** no causal sex or ancestry bias is established. Age affects cataract recognition and visual impact, not the existence of the germline lesion.

### Protective factors and modifiers

No validated protective allele, modifier gene, diet, drug, or lifestyle intervention has been shown to prevent HHCS. Intrafamilial variability indicates that modifiers probably exist, but none is established. Ferritin level and cataract severity do not show a reliable one-to-one relationship. (lachlan2004clinicalfeaturesand pages 1-2, piperno2023hereditaryhyperferritinemia pages 10-12)

### Gene–environment interaction

No disease-specific gene–environment interaction has been demonstrated. Inflammation, alcohol use, metabolic syndrome, malignancy, infection, and liver disease can independently raise ferritin and obscure the characteristic biochemical pattern, but they do not cause the inherited syndrome. Coexisting iron deficiency or true iron overload can occur independently and must be assessed on its own evidence. (eris2023hereditaryhyperferritinemiacataractsyndrome pages 4-5, millonig2010hyperferritinaemiacataractsyndromeworldwide pages 3-4)

There is no infectious cause, toxin-associated cause, occupational risk, or zoonotic component.

---

## 3. Phenotypes

### Core phenotype table

| Phenotype | Type and course | Frequency/evidence | Suggested HPO term |
|---|---|---|---|
| Hyperferritinemia | Laboratory abnormality; usually lifelong, persistent but quantitatively fluctuating | Defining biochemical feature; commonly about 700–2,000 µg/L. Seven British kindreds had minimum recorded values 740–1,960 µg/L, median 1,420 µg/L | **Hyperferritinemia** (HP:0003281; verify current release) |
| Bilateral nuclear cataract | Clinical sign/structural ocular phenotype; congenital, infantile, childhood, or presenile; usually slowly progressive | Defining clinical manifestation, although timing and severity vary | **Cataract** (HP:0000518); **Congenital cataract**; **Nuclear cataract** |
| Punctate/crystalline lens opacities | Slit-lamp sign: breadcrumb-like, pulverulent, sunflower/radial, peripheral flecks or crystalline inclusions | Highly characteristic but morphology is not invariant | **Lens opacity** / cataract morphology terms |
| Reduced visual acuity | Functional consequence; ranges from mild to surgery-requiring | Four young members in one family had acuity below 20/40; many remain mildly affected for years | **Reduced visual acuity** (HP:0007663) |
| Normal transferrin saturation/body iron | Negative diagnostic feature | Typical and central to distinction from hemochromatosis | Use laboratory annotation rather than a disease HPO term |

(lachlan2004clinicalfeaturesand pages 3-4, lachlan2004clinicalfeaturesand pages 1-2, cosentino2016hyperferritinemiacataractsyndromelongterm pages 1-6, ferro2018ftlc.168g>cmutation pages 1-2)

### Cataract onset, severity, and progression

In seven British kindreds, cataract was diagnosed at a median age of five years; most affected people eventually underwent extraction at a median age of 25 years (range 22–42). Infant lenses could show sparse posterior breadcrumb-like opacities, adolescent lenses sunflower-like radial opacities, and extracted lenses crystalline inclusions immunoreactive for L-ferritin. Severity varied substantially within and between families. (lachlan2004clinicalfeaturesand pages 3-4, lachlan2004clinicalfeaturesand pages 1-2)

Long-term observations in an Italian family found limited progression over approximately 18 years, supporting a generally slow adult course. Other families show progressive visual impairment requiring surgery, so “slowly progressive and variable” is more accurate than “stable.” (cosentino2016hyperferritinemiacataractsyndromelongterm pages 1-6, ferro2018ftlc.168g>cmutation pages 1-2)

### Quality of life

No HHCS-specific EQ-5D, SF-36, PROMIS, utility, educational, or employment study was identified. The principal impact is visual: glare, blur, impaired reading/driving or school performance, and—if dense cataract obstructs vision during early childhood—risk of deprivation amblyopia. General congenital-cataract guidance emphasizes early optical rehabilitation in visually significant infantile disease. (shiels2024throughthecatmap pages 3-4, shiels2024throughthecatmapa pages 4-5)

No reproducible behavioral, neurologic, hepatic, endocrine, cardiac, or inflammatory syndrome belongs to classic HHCS. Neurologic manifestations should prompt assessment for other FTL allelic disorders, especially neuroferritinopathy, or a second diagnosis. (cadenas2019lferritinonegene pages 1-3, cadenas2019lferritinonegene pages 5-8)

---

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** FTL, ferritin light chain.
- **Product:** L-ferritin, one of the subunits forming the 24-mer ferritin shell.
- **Disease mechanism:** regulatory gain of expression—not protein-coding loss of function and not a classic dominant-negative effect.
- **Origin:** constitutional/germline. Somatic FTL variants are not the recognized cause.

Serum ferritin is largely L-ferritin-rich, relatively iron-poor material; in HHCS, constitutive synthesis yields excess L-rich ferritin, including H0-L24 homopolymers. (piperno2023hereditaryhyperferritinemia pages 10-12, cadenas2019lferritinonegene pages 1-3)

### Variant spectrum and classification

Pathogenic HHCS variants cluster in structurally critical portions of the IRE: the conserved CAGUGX hexaloop, upper stem, and cytosine bulge. They include single-nucleotide substitutions and short indels. Examples with human segregation evidence include:

- c.-161C>T, c.-167C>T, c.-168G>C;
- c.-151A>G (“Ghent +49A>G”);
- c.-164_-158del7 (“Esplugues +36_42del7”);
- older reports using IRE-relative descriptions such as +32G>T or +32G>C. (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7, ferro2018ftlc.168g>cmutation pages 1-2, millonig2010hyperferritinaemiacataractsyndromeworldwide pages 9-10, sompele2017functionalcharacterizationofa pages 2-3, cadenas2019lferritinonegene pages 3-5)

The c.-151A>G functional study used RNA-structure prediction and EMSA. Mutant RNA retained IRP1 binding but showed a greater than fivefold impairment in apparent affinity relative to wild type, demonstrating that partial—not only complete—loss of repression can cause disease. (sompele2017functionalcharacterizationofa pages 8-9, sompele2017functionalcharacterizationof pages 8-9)

ClinVar classifications must be retrieved variant by variant and transcript-normalized. Many classic alleles have strong pathogenic evidence from segregation, characteristic phenotype, rarity, critical RNA location, and functional assays, but the report should not automatically label every IRE variant pathogenic.

### Population frequency

Pathogenic alleles are expected to be extremely rare. Variant-specific gnomAD/TOPMed frequencies were not available in the retrieved evidence and must be queried using normalized genomic coordinates. No reliable carrier-frequency estimate exists.

### Modifiers, epigenetics, and chromosomal abnormalities

No validated modifier gene, disease-associated methylation signature, histone/chromatin abnormality, large deletion, translocation, inversion, aneuploidy, or recurrent structural variant has been established. HHCS is ordinarily a small noncoding sequence disorder.

---

## 5. Environmental and lifestyle information

Environmental exposure, diet, smoking, exercise, alcohol, radiation, pollution, and infectious agents are not established contributors to HHCS initiation. These factors may cause other cataracts or alter serum ferritin independently and therefore complicate diagnosis. Iron intake does not correct or normalize the regulatory defect, and a high ferritin value alone is not a reason to restrict dietary iron. Conversely, documented iron deficiency should not be left untreated merely because serum ferritin is high in HHCS; iron status must be assessed using transferrin saturation, hemoglobin, red-cell indices, and the broader clinical context. (eris2023hereditaryhyperferritinemiacataractsyndrome pages 4-5, millonig2010hyperferritinaemiacataractsyndromeworldwide pages 3-4)

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A **germline FTL 5′-UTR IRE substitution or indel leads to** distortion or destabilization of the IRE RNA stem-loop. (millonig2010hyperferritinaemiacataractsyndromeworldwide pages 9-10, cadenas2019lferritinonegene pages 5-8)
2. The altered IRE **leads to** reduced binding/functional repression by IRP1 and IRP2; reduced IRP1 affinity has been demonstrated directly for selected variants by EMSA. (sompele2017functionalcharacterizationofa pages 8-9, sompele2017functionalcharacterizationof pages 8-9)
3. Loss of iron-sensitive repression **results in** constitutive FTL translation even when cytosolic iron is low or normal. (lachlan2004clinicalfeaturesand pages 1-2, piperno2023hereditaryhyperferritinemia pages 10-12)
4. Constitutive translation **leads to** excess L-ferritin-rich apoferritin within cells and elevated circulating ferritin that is uncoupled from body-iron stores. (lachlan2004clinicalfeaturesand pages 1-2, piperno2023hereditaryhyperferritinemia pages 10-12)
5. In the lens, excess L-ferritin **results in** intracellular L-ferritin-rich deposits/crystalline aggregates; this tissue-selective accumulation is demonstrated histologically, while the precise basis of lens selectivity remains incompletely resolved. (lachlan2004clinicalfeaturesand pages 3-4, piperno2023hereditaryhyperferritinemia pages 10-12)
6. Lens deposits **lead to** refractive-index discontinuities and light diffraction/scattering—an accepted but partly inferred physical mechanism—which **results in** punctate, crystalline, pulverulent, or sunflower-like opacities. (lachlan2004clinicalfeaturesand pages 3-4, piperno2023hereditaryhyperferritinemia pages 10-12)
7. Progressive accumulation **leads to** bilateral nuclear cataract and, when sufficiently dense, reduced visual acuity and need for cataract extraction. (lachlan2004clinicalfeaturesand pages 3-4, cosentino2016hyperferritinemiacataractsyndromelongterm pages 1-6)
8. **Parallel branch:** excess circulating ferritin without increased transferrin saturation **does not result in** hemochromatotic organ iron deposition; treating the ferritin number with venesection instead **leads to** iatrogenic iron deficiency. (eris2023hereditaryhyperferritinemiacataractsyndrome pages 4-5, millonig2010hyperferritinaemiacataractsyndromeworldwide pages 3-4)

### Pathway and process interpretation

This is primarily an **IRE–IRP post-transcriptional iron-homeostasis disorder**, not a canonical Wnt, MAPK, mTOR, PI3K–AKT, hepcidin–ferroportin, immune, or inflammatory disease. Upstream events are RNA structural change and impaired translational repression; downstream events are L-ferritin overexpression, aggregation/deposition, optical scattering, and cataract.

An additional 2019 mechanistic study identified human eIF3 as a distinct repressor of FTL translation and showed that some hyperferritinemia-associated 5′-UTR variants can disrupt eIF3-mediated repression. This broadens current understanding of FTL translational control, although the gathered evidence does not establish eIF3 disruption for every clinically pathogenic HHCS allele.

### Suggested ontology annotations

- **GO biological process:** cellular iron-ion homeostasis; iron-ion storage; regulation of translation; negative regulation of translation; response to iron ion; protein complex assembly.
- **GO molecular function:** ferric-iron binding; ferroxidase-associated ferritin complex functions; RNA binding for IRP1/IRP2; translation-regulator activity.
- **GO cellular component:** ferritin complex; cytosol; extracellular region/serum; lens fiber-cell cytoplasm.
- **Cell Ontology:** lens epithelial cell; lens fiber cell; hepatocyte and macrophage may contribute serum ferritin biology, but their HHCS-specific contribution has not been resolved.
- **CHEBI:** iron(2+), iron(3+), ferric iron; identifiers should be validated against the production ontology release.

No HHCS-specific immune activation, apoptosis signature, mitochondrial defect, lipidopathy, or systemic oxidative-injury phenotype is established.

### Molecular profiling and advanced technologies

No HHCS-specific single-cell RNA-seq, spatial transcriptomics, comprehensive proteomics, metabolomics, lipidomics, epigenomics, multi-omics integration, organoid study, or CRISPR/RNAi screen was identified. Lens immunoreactivity for L-ferritin and IRE-binding assays are the principal molecular-level evidence. (lachlan2004clinicalfeaturesand pages 3-4, shiels2024throughthecatmapa pages 20-21, shiels2024throughthecatmap pages 19-21)

---

## 7. Anatomical structures affected

### Organ and tissue level

The directly affected organ is the **eye**, specifically the **crystalline lens**, usually bilaterally and relatively symmetrically. Opacities frequently involve the embryonic/fetal nucleus and may extend centrifugally into cortical regions. No secondary systemic organ damage is expected from classic HHCS itself. (lachlan2004clinicalfeaturesand pages 3-4, ferro2018ftlc.168g>cmutation pages 1-2)

Suggested terms:

- **UBERON:** eye; lens of eye; lens epithelium; lens fiber; lens nucleus—validate exact identifiers in the current Uberon release.
- **HPO:** bilateral cataract; congenital cataract; juvenile cataract; nuclear cataract; reduced visual acuity.
- **CL:** lens epithelial cell; lens fiber cell.
- **GO cellular component:** cytosol and ferritin complex.

At the subcellular level, the key lesion is excess cytosolic L-ferritin and formation of high-molecular-weight/crystalline deposits. A primary nuclear-genome mutation is present, but the pathogenic deposits are not a nuclear-organelle lesion.

---

## 8. Temporal development

Serum hyperferritinemia is constitutional and likely present from early life, although it is often discovered incidentally during anemia evaluation, pregnancy screening, or family testing. Cataracts can be congenital or first recognized in infancy, childhood, adolescence, or adulthood. The 2023 synthesis places reported presentation approximately between ages 1 and 45 years. (lachlan2004clinicalfeaturesand pages 1-2, piperno2023hereditaryhyperferritinemia pages 10-12)

There is no formal staging system. A useful clinical sequence is:

1. asymptomatic hyperferritinemia and subtle punctate lens deposits;
2. slowly increasing nuclear/cortical opacities;
3. functional visual impairment;
4. cataract extraction when indicated.

The disorder is lifelong, generally chronic, and slowly progressive rather than episodic or relapsing. Cataracts do not spontaneously remit. Surgery removes the opaque lens, whereas serum hyperferritinemia persists. Dense infantile cataract represents the critical period because delayed optical correction risks irreversible amblyopia; milder adult disease can be monitored according to function. (lachlan2004clinicalfeaturesand pages 3-4, cosentino2016hyperferritinemiacataractsyndromelongterm pages 1-6, shiels2024throughthecatmap pages 3-4)

---

## 9. Inheritance and population

HHCS is predominantly **autosomal dominant**. Penetrance of biochemical hyperferritinemia appears high in reported mutation-positive families, but ascertainment is strong and no unbiased numerical estimate is available. Cataract expressivity and age at recognition are variable. No genetic anticipation has been demonstrated. Germline mosaicism is theoretically possible but not established as a recurrent phenomenon. (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7, lachlan2004clinicalfeaturesand pages 1-2)

The best available prevalence estimate is approximately **1 per 200,000**, worldwide, but this is not based on population-wide screening. A 2018 report cited roughly 160 known families/cases, indicating substantial under-recognition is plausible. Incidence, carrier frequency, and sex ratio are unknown. (ferro2018ftlc.168g>cmutation pages 1-2, piperno2023hereditaryhyperferritinemia pages 10-12)

Affected families have been reported across Europe, Asia, and the Americas and among multiple ancestries. No established ethnic restriction exists. Recurrent alleles may reflect mutationally sensitive IRE positions rather than a single universal founder. Consanguinity is not generally relevant to this dominant disease, although it enabled homozygosity in the c.-151A>G family. (sompele2017functionalcharacterizationofa pages 2-3)

---

## 10. Diagnostics

### Practical diagnostic algorithm

1. **Confirm ferritin elevation** and review age- and sex-appropriate laboratory reference ranges.
2. Measure **serum iron, transferrin/TIBC, transferrin saturation, complete blood count, reticulocyte indices as appropriate, CRP/ESR, and liver enzymes**.
3. Exclude common acquired causes: inflammation/infection, metabolic liver disease, alcohol-related disease, malignancy, liver injury, and iron supplementation.
4. Determine whether true iron overload is present. Normal transferrin saturation and absent organ iron loading strongly favor HHCS when cataract is present.
5. Obtain a **three-generation history** of cataracts, high ferritin, phlebotomy, anemia, and liver disease.
6. Perform **slit-lamp examination**, looking for bilateral punctate breadcrumb-like, pulverulent, crystalline, sunflower/radial, or nuclear opacities.
7. Confirm by sequencing the **FTL 5′UTR IRE**, with deletion/indel-sensitive analysis and transcript-normalized interpretation.
8. Offer targeted testing and ophthalmic evaluation to relatives. (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7, eris2023hereditaryhyperferritinemiacataractsyndrome pages 4-5, millonig2010hyperferritinaemiacataractsyndromeworldwide pages 3-4)

### Genetic-testing modalities

- **Preferred:** targeted Sanger or high-depth NGS of the FTL 5′UTR/IRE when the phenotype is characteristic.
- **Cataract/iron-disorder panels:** useful if the phenotype is atypical; the panel must cover the noncoding FTL IRE, since coding-only designs may miss HHCS.
- **WES:** may be useful for heterogeneous inherited cataract but can inadequately capture or filter the relevant 5′UTR. A 2024 review reports 50–90% molecular diagnosis for genetic pediatric cataract using modern panels/high-throughput sequencing overall, not specifically HHCS. (shiels2024throughthecatmapa pages 20-21, shiels2024throughthecatmap pages 19-21)
- **WGS:** potentially useful if targeted testing is negative, particularly for noncoding or structural lesions, but no HHCS-specific diagnostic-yield study was identified.
- **CMA, karyotype, FISH, mitochondrial sequencing, and repeat-expansion testing:** not routine for classic HHCS.
- **RNA-seq/proteomics/metabolomics/epigenomics/liquid biopsy:** no validated diagnostic role.

### Imaging, biopsy, and pathology

MRI-based liver iron assessment may be used when biochemical or clinical findings genuinely suggest coincident iron overload. Routine liver biopsy is inappropriate merely for high ferritin in a characteristic HHCS case. Extracted lenses can contain crystalline, immunoreactive L-ferritin inclusions, but lens biopsy is not a diagnostic requirement. (lachlan2004clinicalfeaturesand pages 3-4, millonig2010hyperferritinaemiacataractsyndromeworldwide pages 3-4)

### Differential diagnosis

- **HFE or non-HFE hemochromatosis:** typically increased transferrin saturation and evidence of iron loading; cataract morphology is not characteristic.
- **Ferroportin disease:** hyperferritinemia may coexist with normal/low transferrin saturation but tissue iron is increased.
- **Inflammatory, infectious, malignant, hepatic, alcohol-related, or metabolic hyperferritinemia:** distinguished by clinical context and inflammatory/liver findings.
- **Benign FTL-related hyperferritinemia:** high ferritin without cataract, associated with a different FTL variant class.
- **Neuroferritinopathy:** coding FTL variants, movement/cognitive disorder and basal-ganglia iron accumulation, often low or normal serum ferritin rather than classic HHCS.
- **Other inherited cataracts:** crystallin, connexin, transcription-factor, metabolic, infectious, traumatic, steroid, or radiation-associated cataracts; serum ferritin pattern distinguishes HHCS. (cadenas2019lferritinonegene pages 1-3, cadenas2019lferritinonegene pages 5-8, shiels2024throughthecatmap pages 3-4)

There are no universally adopted society diagnostic criteria. The combination of isolated hyperferritinemia, normal iron loading, typical bilateral cataract, dominant pedigree, and a pathogenic FTL IRE variant is diagnostic.

---

## 11. Outcome and prognosis

Life expectancy is expected to be normal, and no HHCS-specific mortality signal, organ-failure risk, five- or ten-year survival estimate, or disease-specific death rate has been demonstrated. The principal morbidity is visual impairment. Hyperferritinemia is lifelong but does not itself signify progressive hepatic, cardiac, pancreatic, or neurologic iron injury. (millonig2010hyperferritinaemiacataractsyndromeworldwide pages 3-4, piperno2023hereditaryhyperferritinemia pages 10-12)

Visual prognosis after appropriately timed standard cataract treatment is generally favorable, although pediatric outcome depends on cataract density, age at intervention, amblyopia prevention, refractive rehabilitation, and postoperative complications. Quantitative HHCS-specific surgical response rates are unavailable. Some operated adults later required Nd:YAG capsulotomy, a common treatment for posterior capsule opacification rather than recurrence of the native lens cataract. (ferro2018ftlc.168g>cmutation pages 1-2)

Adverse prognosis is more likely to reflect delayed cataract treatment or iatrogenic iron depletion from inappropriate venesection than intrinsic systemic HHCS. No validated molecular prognostic biomarker beyond the causal genotype has been established.

---

## 12. Treatment

### Established strategy

1. **Do not treat ferritin elevation alone.** Neither phlebotomy nor chelation lowers the genetically dysregulated synthesis in a clinically useful way.
2. **Treat independent iron deficiency normally**, guided by complete iron assessment.
3. **Monitor vision and lens morphology.** Use refraction and amblyopia therapy in children where needed.
4. **Perform cataract extraction with optical rehabilitation** when opacity materially impairs vision or threatens visual development.
5. Continue routine postoperative surveillance, including posterior-capsule and glaucoma monitoring in pediatric cases. (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7, eris2023hereditaryhyperferritinemiacataractsyndrome pages 4-5, piperno2023hereditaryhyperferritinemia pages 10-12, shiels2024throughthecatmap pages 3-4)

Suggested NCIT concepts include **Cataract Surgery**, **Lens Extraction**, **Intraocular Lens Implantation**, **Phacoemulsification**, **Genetic Counseling**, and **Observation**; identifiers should be mapped against the current NCIT release.

### Avoidable harms

Misdiagnosed patients have undergone repeated venesection and developed iron-deficiency anemia. One patient received deferasirox and developed life-threatening acute hyperammonemia. These reports make avoidance of unindicated iron-removal therapy a central safety intervention. (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7, eris2023hereditaryhyperferritinemiacataractsyndrome pages 4-5)

### Experimental treatments and trials

No validated pharmacotherapy, ferritin-lowering drug, genotype-guided medication, gene therapy, CRISPR therapy, antisense oligonucleotide, siRNA, cell therapy, immunotherapy, or HHCS-specific interventional trial was identified. NCT05659017 (“Candidate Gene for Hyperferritinemia”) was retrieved as an observational study planned for 100 participants with status listed as unknown; it is not evidence of an HHCS treatment.

Gene editing and pharmacologic anti-cataract approaches are being studied for other cataract genes, but none can currently be extrapolated as HHCS therapy. (shiels2024throughthecatmapa pages 20-21, shiels2024throughthecatmap pages 19-21)

---

## 13. Prevention

### Primary prevention

The occurrence of a de novo or inherited pathogenic allele cannot currently be prevented through lifestyle change or vaccination. Reproductive options following identification of a familial variant include prenatal diagnosis and preimplantation genetic testing after nondirective counseling, subject to local law and family preferences.

### Secondary prevention

- Cascade testing of first-degree relatives.
- Baseline slit-lamp examination in mutation-positive children.
- Early recognition of visually significant cataract during the developmental critical period.
- Correct identification of isolated hyperferritinemia before invasive iron-overload investigations. (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7, shiels2024throughthecatmap pages 3-4)

### Tertiary prevention

- Prevent amblyopia through timely surgery, refractive correction, and occlusion therapy when indicated.
- Prevent iatrogenic anemia and chelator toxicity by avoiding phlebotomy/chelation without proven iron overload.
- Educate patients to tell clinicians that their high ferritin is genetically driven and does not automatically indicate iron overload. (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7, eris2023hereditaryhyperferritinemiacataractsyndrome pages 4-5)

No immunization, chemoprophylaxis, environmental intervention, or population newborn-screening program is indicated. Population carrier screening is not supported by current prevalence or outcome data.

---

## 14. Other species and natural disease

FTL and the IRE–IRP regulatory system are evolutionarily conserved across mammals, but no naturally occurring companion-animal, livestock, or wildlife syndrome convincingly equivalent to human HHCS was identified. Consequently, no breed-specific VBO annotation, veterinary prevalence, transmission pattern, cross-species susceptibility, or zoonotic potential can be assigned. HHCS is genetic and noncommunicable.

For comparative annotation, **Mus musculus** (NCBI Taxonomy 10090), **Danio rerio** (7955), and other vertebrates possess ferritin/iron-regulatory orthologs useful for studying general iron biology, but that does not constitute natural HHCS.

---

## 15. Model organisms and experimental systems

### Available evidence

The strongest disease-specific experimental model is **in vitro RNA–protein analysis**. Mutant and wild-type FTL IRE RNAs have been assessed by structure prediction and direct/competitive EMSA with recombinant IRP1. The c.-151A>G mutant retained binding but had markedly impaired affinity, providing functional support for pathogenicity. (sompele2017functionalcharacterizationofa pages 8-9, sompele2017functionalcharacterizationof pages 8-9, sompele2017functionalcharacterizationofa pages 2-3)

Human extracted-lens material showing crystalline, immunoreactive L-ferritin deposits provides ex vivo pathological validation. (lachlan2004clinicalfeaturesand pages 3-4)

### Model gaps

No well-validated mouse, rat, rabbit, zebrafish, Drosophila, organoid, or patient-iPSC model reproducing the complete HHCS triad—pathogenic FTL IRE allele, serum hyperferritinemia without iron overload, and characteristic ferritin cataract—was identified in the gathered evidence. FTL coding-mutant mice used for neuroferritinopathy and CRISPR models of other cataract genes should not be mislabeled as HHCS models. (shiels2024throughthecatmapa pages 20-21, shiels2024throughthecatmapa pages 29-30, shiels2024throughthecatmap pages 19-21)

A useful future model would be an FTL-IRE knock-in animal or human lens organoid carrying a recurrent pathogenic allele, with quantitative IRP occupancy, ribosome profiling, ferritin composition, lens transparency, aggregate imaging, and rescue by allele-selective translational repression.

---

## Recent developments and expert interpretation

- **2023:** Piperno, Pelucchi, and Mariani consolidated HHCS within hereditary hyperferritinemias with normal transferrin saturation and emphasized stepwise biochemical/genetic diagnosis and avoidance of iron-removal treatment. [Published January 2023; DOI 10.3390/ijms24032560](https://doi.org/10.3390/ijms24032560). (piperno2023hereditaryhyperferritinemia pages 10-12)
- **2023 human safety lesson:** an HHCS family with coexisting HFE H63D illustrated that incidental HFE findings can anchor clinicians incorrectly on hemochromatosis; the patient had received ineffective phlebotomy and chelation. [Published March 2023; DOI 10.7759/cureus.36253](https://doi.org/10.7759/cureus.36253). (eris2023hereditaryhyperferritinemiacataractsyndrome pages 4-5)
- **2024:** contemporary cataract-genetics review supports broad panel/WES/WGS testing for heterogeneous inherited cataract, but HHCS remains best detected by ensuring explicit coverage of the noncoding FTL IRE. [Published June 2024; DOI 10.3390/genes15060785](https://doi.org/10.3390/genes15060785). (shiels2024throughthecatmap pages 3-4, shiels2024throughthecatmap pages 19-21)

The expert consensus across these sources is that HHCS is usually medically benign outside the lens, highly recognizable when ferritin and cataract are considered together, and disproportionately harmful when mistaken for iron overload. The most effective “precision medicine” implementation today is therefore accurate molecular diagnosis, cascade assessment, avoidance of venesection/chelation, and individualized ophthalmic care. (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7, eris2023hereditaryhyperferritinemiacataractsyndrome pages 4-5, piperno2023hereditaryhyperferritinemia pages 10-12)

## Key references

1. Piperno A, Pelucchi S, Mariani R. **Hereditary Hyperferritinemia.** *Int J Mol Sci.* Published January 2023. [https://doi.org/10.3390/ijms24032560](https://doi.org/10.3390/ijms24032560). (piperno2023hereditaryhyperferritinemia pages 10-12)
2. Shiels A. **Through the Cat-Map Gateway: A Brief History of Cataract Genetics.** *Genes.* Published June 2024. [https://doi.org/10.3390/genes15060785](https://doi.org/10.3390/genes15060785). (shiels2024throughthecatmap pages 3-4, shiels2024throughthecatmap pages 19-21)
3. Moravikova J, et al. **Hereditary hyperferritinemia-cataract syndrome in three Czech families.** *J AAPOS.* Published December 2020. [https://doi.org/10.1016/j.jaapos.2020.07.014](https://doi.org/10.1016/j.jaapos.2020.07.014). (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7)
4. Cadenas B, et al. **L-Ferritin: One Gene, Five Diseases.** *Pharmaceuticals.* Published January 2019. [https://doi.org/10.3390/ph12010017](https://doi.org/10.3390/ph12010017). (cadenas2019lferritinonegene pages 1-3, cadenas2019lferritinonegene pages 5-8)
5. Millonig G, Muckenthaler MU, Mueller S. **Hyperferritinaemia-cataract syndrome: worldwide mutations and phenotype.** *Human Genomics.* Published April 2010. [https://doi.org/10.1186/1479-7364-4-4-250](https://doi.org/10.1186/1479-7364-4-4-250). (millonig2010hyperferritinaemiacataractsyndromeworldwide pages 3-4, millonig2010hyperferritinaemiacataractsyndromeworldwide pages 9-10)
6. Lachlan KL, Temple IK, Mumford AD. **Clinical features and molecular analysis of seven British kindreds.** *Eur J Hum Genet.* Published online July 28, 2004; issue October 2004. [https://doi.org/10.1038/sj.ejhg.5201252](https://doi.org/10.1038/sj.ejhg.5201252). (lachlan2004clinicalfeaturesand pages 3-4, lachlan2004clinicalfeaturesand pages 1-2)
7. Ferro E, et al. **FTL c.-168G>C Mutation in HHCS.** *Pediatr Dev Pathol.* Published February 2018. [https://doi.org/10.1177/1093526618755200](https://doi.org/10.1177/1093526618755200). (ferro2018ftlc.168g>cmutation pages 1-2)
8. Cosentino I, et al. **Long-term ophthalmic observations in an Italian family.** *Ophthalmic Genet.* Published February 5, 2016. [https://doi.org/10.3109/13816810.2015.1059460](https://doi.org/10.3109/13816810.2015.1059460). (cosentino2016hyperferritinemiacataractsyndromelongterm pages 1-6)

References

1. (moravikova2020hereditaryhyperferritinemiacataractsyndrome pages 1-7): Jana Moravikova, Tomas Honzik, Eva Jadvidzakova, Katerina Zdrahalova, Radka Kremlikova Pourova, Marta Korbasova, Petra Liskova, and Lubica Dudakova. Hereditary hyperferritinemia-cataract syndrome in three czech families: molecular genetic testing and clinical implications. Dec 2020. URL: https://doi.org/10.1016/j.jaapos.2020.07.014, doi:10.1016/j.jaapos.2020.07.014. This article has 11 citations.

2. (eris2023hereditaryhyperferritinemiacataractsyndrome pages 4-5): Tansu Eris, Ahmet Mert Yanik, Derya Demirtas, Asu Fergun Yilmaz, and Tayfur Toptas. Hereditary hyperferritinemia-cataract syndrome in a family with hfe-h63d mutation. Mar 2023. URL: https://doi.org/10.7759/cureus.36253, doi:10.7759/cureus.36253. This article has 6 citations.

3. (piperno2023hereditaryhyperferritinemia pages 10-12): Alberto Piperno, Sara Pelucchi, and Raffaella Mariani. Hereditary hyperferritinemia. International Journal of Molecular Sciences, 24:2560, Jan 2023. URL: https://doi.org/10.3390/ijms24032560, doi:10.3390/ijms24032560. This article has 32 citations.

4. (sompele2017functionalcharacterizationofa pages 2-3): S Van de Sompele, L Pécheux, J Couso, and A Meunier. Functional characterization of a novel non-coding mutation “ghent+ 49a> g” in the iron-responsive element of l-ferritin causing hereditary hyperferritinaemia-cataract …. Unknown journal, 2017.

5. (millonig2010hyperferritinaemiacataractsyndromeworldwide pages 9-10): Gunda Millonig, Martina U Muckenthaler, and Sebastian Mueller. Hyperferritinaemia-cataract syndrome: worldwide mutations and phenotype of an increasingly diagnosed genetic disorder. Human Genomics, 4:250-262, Apr 2010. URL: https://doi.org/10.1186/1479-7364-4-4-250, doi:10.1186/1479-7364-4-4-250. This article has 69 citations and is from a peer-reviewed journal.

6. (cadenas2019lferritinonegene pages 5-8): Beatriz Cadenas, Josep Fita-Torró, Mar Bermúdez-Cortés, Inés Hernandez-Rodriguez, José Luis Fuster, María Esther Llinares, Ana María Galera, Julia Lee Romero, Santiago Pérez-Montero, Cristian Tornador, and Mayka Sanchez. L-ferritin: one gene, five diseases; from hereditary hyperferritinemia to hypoferritinemia—report of new cases. Pharmaceuticals, 12:17, Jan 2019. URL: https://doi.org/10.3390/ph12010017, doi:10.3390/ph12010017. This article has 38 citations.

7. (sompele2017functionalcharacterizationofa pages 8-9): S Van de Sompele, L Pécheux, J Couso, and A Meunier. Functional characterization of a novel non-coding mutation “ghent+ 49a> g” in the iron-responsive element of l-ferritin causing hereditary hyperferritinaemia-cataract …. Unknown journal, 2017.

8. (lachlan2004clinicalfeaturesand pages 1-2): Katherine L Lachlan, I Karen Temple, and Andrew D Mumford. Clinical features and molecular analysis of seven british kindreds with hereditary hyperferritinaemia cataract syndrome. European Journal of Human Genetics, 12:790-796, Oct 2004. URL: https://doi.org/10.1038/sj.ejhg.5201252, doi:10.1038/sj.ejhg.5201252. This article has 26 citations and is from a domain leading peer-reviewed journal.

9. (cosentino2016hyperferritinemiacataractsyndromelongterm pages 1-6): Ilaria Cosentino, Fabrizio Zeri, Peter G. Swann, Silvia Majore, Francesca Clementina Radio, Paolo Palumbo, Paola Grammatico, and Vincenzo Petitti. Hyperferritinemia-cataract syndrome: long-term ophthalmic observations in an italian family. Ophthalmic Genetics, 37:318-322, Feb 2016. URL: https://doi.org/10.3109/13816810.2015.1059460, doi:10.3109/13816810.2015.1059460. This article has 9 citations and is from a peer-reviewed journal.

10. (lachlan2004clinicalfeaturesand pages 3-4): Katherine L Lachlan, I Karen Temple, and Andrew D Mumford. Clinical features and molecular analysis of seven british kindreds with hereditary hyperferritinaemia cataract syndrome. European Journal of Human Genetics, 12:790-796, Oct 2004. URL: https://doi.org/10.1038/sj.ejhg.5201252, doi:10.1038/sj.ejhg.5201252. This article has 26 citations and is from a domain leading peer-reviewed journal.

11. (ferro2018ftlc.168g>cmutation pages 1-2): Elisa Ferro, Anna Paola Capra, Giuseppina Zirilli, Alessandro Meduri, Mario Urso, Silvana Briuglia, and Maria Angela La Rosa. Ftl c.-168g>c mutation in hereditary hyperferritinemia cataract syndrome: a new italian family. Pediatric and Developmental Pathology, 21:456-460, Feb 2018. URL: https://doi.org/10.1177/1093526618755200, doi:10.1177/1093526618755200. This article has 14 citations and is from a peer-reviewed journal.

12. (millonig2010hyperferritinaemiacataractsyndromeworldwide pages 3-4): Gunda Millonig, Martina U Muckenthaler, and Sebastian Mueller. Hyperferritinaemia-cataract syndrome: worldwide mutations and phenotype of an increasingly diagnosed genetic disorder. Human Genomics, 4:250-262, Apr 2010. URL: https://doi.org/10.1186/1479-7364-4-4-250, doi:10.1186/1479-7364-4-4-250. This article has 69 citations and is from a peer-reviewed journal.

13. (shiels2024throughthecatmapa pages 20-21): A Shiels. Through the cat-map gateway: a brief history of cataract genetics. genes 2024, 15, 785. Unknown journal, 2024.

14. (shiels2024throughthecatmap pages 19-21): Alan Shiels. Through the cat-map gateway: a brief history of cataract genetics. Jun 2024. URL: https://doi.org/10.3390/genes15060785, doi:10.3390/genes15060785. This article has 22 citations.

15. (shiels2024throughthecatmap pages 3-4): Alan Shiels. Through the cat-map gateway: a brief history of cataract genetics. Jun 2024. URL: https://doi.org/10.3390/genes15060785, doi:10.3390/genes15060785. This article has 22 citations.

16. (cadenas2019lferritinonegene pages 3-5): Beatriz Cadenas, Josep Fita-Torró, Mar Bermúdez-Cortés, Inés Hernandez-Rodriguez, José Luis Fuster, María Esther Llinares, Ana María Galera, Julia Lee Romero, Santiago Pérez-Montero, Cristian Tornador, and Mayka Sanchez. L-ferritin: one gene, five diseases; from hereditary hyperferritinemia to hypoferritinemia—report of new cases. Pharmaceuticals, 12:17, Jan 2019. URL: https://doi.org/10.3390/ph12010017, doi:10.3390/ph12010017. This article has 38 citations.

17. (shiels2024throughthecatmapa pages 4-5): A Shiels. Through the cat-map gateway: a brief history of cataract genetics. genes 2024, 15, 785. Unknown journal, 2024.

18. (cadenas2019lferritinonegene pages 1-3): Beatriz Cadenas, Josep Fita-Torró, Mar Bermúdez-Cortés, Inés Hernandez-Rodriguez, José Luis Fuster, María Esther Llinares, Ana María Galera, Julia Lee Romero, Santiago Pérez-Montero, Cristian Tornador, and Mayka Sanchez. L-ferritin: one gene, five diseases; from hereditary hyperferritinemia to hypoferritinemia—report of new cases. Pharmaceuticals, 12:17, Jan 2019. URL: https://doi.org/10.3390/ph12010017, doi:10.3390/ph12010017. This article has 38 citations.

19. (sompele2017functionalcharacterizationof pages 8-9): S Van de Sompele, L Pécheux, J Couso, and A Meunier. Functional characterization of a novel non-coding mutation “ghent+ 49a> g” in the iron-responsive element of l-ferritin causing hereditary hyperferritinaemia-cataract …. Unknown journal, 2017.

20. (shiels2024throughthecatmapa pages 29-30): A Shiels. Through the cat-map gateway: a brief history of cataract genetics. genes 2024, 15, 785. Unknown journal, 2024.

## Artifacts

- [Edison artifact artifact-00](Hereditary_Hyperferritinemia_With_Congenital_Cataracts-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 2 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1007/s00439-017-1835-3` (3 mentions) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 3 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0010952` (2 mentions) - the report calls it "if available"; MONDO calls it **hereditary hyperferritinemia with congenital cataracts**