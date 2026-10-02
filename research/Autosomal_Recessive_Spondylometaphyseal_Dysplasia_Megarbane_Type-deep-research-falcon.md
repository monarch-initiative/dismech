---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-31T10:08:06.760513'
end_time: '2026-08-31T10:15:18.443676'
duration_seconds: 431.68
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal Recessive Spondylometaphyseal Dysplasia, Megarbane Type
  mondo_id: MONDO:0013223
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 4
  verified: 4
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0013223
    reported_labels:
    - if available
    - MONDO
    ontology_label: autosomal recessive spondylometaphyseal dysplasia, Megarbane type
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Recessive_Spondylometaphyseal_Dysplasia_Megarbane_Type-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Spondylometaphyseal Dysplasia, Megarbane Type
- **MONDO ID:** MONDO:0013223 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Spondylometaphyseal Dysplasia, Megarbane Type** covering all of the
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
- **Disease Name:** Autosomal Recessive Spondylometaphyseal Dysplasia, Megarbane Type
- **MONDO ID:** MONDO:0013223 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Spondylometaphyseal Dysplasia, Megarbane Type** covering all of the
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


# Autosomal Recessive Spondylometaphyseal Dysplasia, Megarbane Type

## Executive summary

Autosomal recessive spondylometaphyseal dysplasia, Megarbane–Dagher–Melki type (SMDMDM), is an exceptionally rare, congenital skeletal dysplasia caused by biallelic pathogenic variants in **PAM16**, historically called **MAGMAS**. The best-characterized allele, **NM_016069:c.226A>G (p.Asn76Asp)**, was found homozygously in four children from two Lebanese consanguineous families. The phenotype comprised prenatal and postnatal growth restriction, disproportionate short stature, severe neonatal platyspondyly, metaphyseal and pelvic abnormalities, delayed epiphyseal ossification, developmental delay, narrow thorax, and lethal respiratory or cardiac complications. All four original patients died by age two years. A later **p.Gln74Pro** case reportedly had a milder course and longer survival, but detailed primary data were not retrievable for this report; therefore, the original four-patient frequencies must not be generalized as population estimates. (mehawej2014theimpairmentof pages 2-4, zhao2023mitochondrialskeletaldisorders pages 45-50, OpenTargets Search: spondylometaphyseal dysplasia Megarbane type-PAM16)

The molecular defect is a mitochondrial protein-import disorder. PAM16/MAGMAS is a J-like regulator within the presequence translocase-associated motor of the TIM23 complex. The p.Asn76Asp allele destabilized the protein in yeast, impaired mitochondrial matrix-protein import, fragmented mitochondria, promoted pexophagy, and caused temperature-sensitive loss of viability. How these defects produce human growth-plate failure is biologically plausible but remains partly inferred rather than directly demonstrated in patient chondrocytes. (mehawej2014theimpairmentof pages 6-8, mehawej2014theimpairmentof pages 4-6)

The following table summarizes the highest-value evidence for knowledge-base curation.

| domain | best-supported finding | quantitative/detail | evidence type/strength | key identifier or ontology |
|---|---|---|---|---|
| Disease identity | Ultra-rare early-lethal skeletal dysplasia mapped to PAM16/MAGMAS | MONDO disease-target association supports PAM16; review tables list disease as SMDMDM, Megarbane-Dagher-Melki type (OpenTargets Search: spondylometaphyseal dysplasia Megarbane type-PAM16, zhao2020skeletalphenotypesdue pages 5-6) | Curated database + review; moderate for identifiers | MONDO:0013223; OMIM: 613320 |
| Nomenclature | Synonyms center on spondylometaphyseal/spondylodysplastic dysplasia and Megarbane-Dagher-Melki type | Literature uses “early lethal spondylometaphyseal dysplasia,” “severe spondylodysplastic dysplasia,” and “SMDMDM” (mehawej2014theimpairmentof pages 1-2, zhao2020skeletalphenotypesdue pages 5-6) | Primary paper + review; strong | autosomal recessive spondylometaphyseal dysplasia, Megarbane type |
| Causal gene | Disease is caused by biallelic PAM16 variants; PAM16 encodes MAGMAS, a PAM/TIM23 import motor component | PAM16 = presequence translocase associated motor 16; MAGMAS is the commonly used protein/gene alias (mehawej2014theimpairmentof pages 2-4, mehawej2014theimpairmentof pages 1-2) | Primary human genetics; strong | PAM16 / MAGMAS |
| Primary pathogenic variant | Recurrent homozygous missense variant p.Asn76Asp is the best-supported disease-causing allele | NM_016069: c.226A>G; p.Asn76Asp; predicted damaging by MutationTaster 0.99999957, SIFT 0.006, PROVEAN -24.021, PolyPhen-2 0.728 (mehawej2014theimpairmentof pages 2-4) | Primary variant discovery + segregation + functional follow-up; very strong | p.Asn76Asp |
| Human cases | Original evidence comprises four affected individuals from two unrelated Lebanese consanguineous families | Family 1: 2 affected sibs; Family 2: 2 affected sibs; all four had severe early-lethal disease (mehawej2014theimpairmentof pages 1-2, mehawej2014theimpairmentof pages 2-4) | Human clinical primary evidence; strong | Lebanese founder-associated cases |
| Inheritance | Autosomal recessive inheritance is strongly supported | Affected individuals homozygous; parents/unaffected sibs heterozygous; disease seen in consanguineous pedigrees (mehawej2014theimpairmentof pages 2-4, mehawej2014theimpairmentof pages 6-8) | Segregation in 2 pedigrees; strong | autosomal recessive inheritance |
| Consanguinity/founder effect | Shared ancestral allele likely in Lebanese population | Family 2 consanguinity coefficient F=1/16; minimal shared ancestral homozygous haplotype 1.9 Mb on 16p13.3 between D16S758 and D16S243 (mehawej2014theimpairmentof pages 2-4) | Human mapping evidence; strong | chromosome 16p13.3 founder haplotype |
| Population frequency | Variant was not seen in local controls in original report | Absent in 550 Lebanese control chromosomes (mehawej2014theimpairmentof pages 2-4) | Case-control absence only; moderate | rare/private founder variant |
| Core phenotype | Severe skeletal dysplasia with vertebral and metaphyseal abnormalities | Pre/postnatal growth retardation, short limbs, narrow thorax with short ribs, prominent abdomen, dysmorphic features, developmental delay (mehawej2014theimpairmentof pages 2-4) | Human clinical primary evidence; strong | short stature; developmental delay |
| Radiographic phenotype | Characteristic spine/pelvis/long-bone abnormalities define the disorder | Severe platyspondyly at birth with some improvement over time; square iliac bones; horizontal acetabulae; abnormal long-bone modeling; widening of distal femoral metaphyses; delayed epiphyseal ossification (mehawej2014theimpairmentof pages 2-4, mehawej2014theimpairmentof pages 4-6) | Human imaging primary evidence; strong | platyspondyly; delayed epiphyseal ossification |
| Extra-skeletal manifestations | Cardiopulmonary complications are major contributors to mortality | Respiratory insufficiency in Family 1; heart failure/cardiomyopathy in Family 2; developmental delay reported (mehawej2014theimpairmentof pages 2-4, mehawej2014theimpairmentof pages 6-8, zhao2020skeletalphenotypesdue pages 5-6) | Human clinical primary evidence + review; strong | cardiomyopathy |
| Survival/prognosis | Prognosis in the original families was uniformly poor | Deaths: 9 months, 2 years, 2 years, and 2 years (mehawej2014theimpairmentof pages 2-4) | Human natural history primary evidence; strong | early lethality |
| Tissue expression | MAGMAS is expressed in skeletal tissues relevant to endochondral ossification | Expression confirmed in bone and cartilage; enriched in hypertrophic chondrocytes and osteoblasts/primary spongiosa during development (mehawej2014theimpairmentof pages 1-2, mehawej2014theimpairmentof pages 6-8, mehawej2014theimpairmentof pages 4-6) | Human cell-expression + mouse histology; strong | hypertrophic chondrocyte; osteoblast |
| Mechanism: proximal | PAM16/MAGMAS dysfunction impairs mitochondrial matrix protein import via PAM/TIM23 | MAGMAS is an essential PAM component regulating preprotein translocation into mitochondrial matrix after TOM passage through TIM23 motor complex (mehawej2014theimpairmentof pages 2-4, mehawej2014theimpairmentof pages 4-6, jain2024hotspotsfordiseasecausing pages 7-8) | Primary mechanistic + authoritative review; strong | mitochondrial protein import; TIM23 complex |
| Mechanism: variant effect | p.Asn76Asp destabilizes MAGMAS and compromises function | Variant lies in helix II of the J-like domain; lower mutant protein at non-permissive temperature; deleterious effect seen in homozygous state (mehawej2014theimpairmentof pages 6-8, mehawej2014theimpairmentof pages 4-6) | Primary functional evidence; strong | J-like domain |
| Mechanism: downstream cellular defects | Mutant MAGMAS causes import failure and organelle stress | Non-processed Hsp60 accumulated in mutant yeast at 37°C; punctate/fragmented mitochondria and enhanced pexophagy observed (mehawej2014theimpairmentof pages 4-6) | Yeast functional model; strong for cellular mechanism | Hsp60 precursor accumulation; mitochondrial fragmentation |
| Mechanism: disease inference | Import failure likely disrupts ossification in growth-plate cartilage and trabecular bone | Authors conclude deleterious MAGMAS mutations support a key role for this mitochondrial protein in ossification; direct human growth-plate mechanism remains inferred (mehawej2014theimpairmentof pages 1-2, mehawej2014theimpairmentof pages 6-8) | Primary paper inference from expression + model data; moderate | endochondral ossification |
| Model systems | Yeast and mouse tissue localization are the main disease-relevant models | Yeast complementation showed slow growth at 34°C and inviability at 36°C/37°C in mutant conditions; WT mouse distal femur staining localized MAGMAS in growth plate (mehawej2014theimpairmentof pages 6-8, mehawej2014theimpairmentof pages 4-6) | Experimental models; strong | Saccharomyces cerevisiae; mouse distal femur |
| Diagnosis | Diagnosis currently relies on phenotype/radiography plus molecular confirmation | Exome sequencing identified causal homozygous variant; Sanger sequencing confirmed segregation; radiographs showed defining skeletal pattern (mehawej2014theimpairmentof pages 2-4, mehawej2014theimpairmentof pages 4-6) | Standard rare-disease workflow documented in primary study; strong | exome sequencing; Sanger confirmation |
| Differential nosology | Disease belongs among mitochondrial skeletal disorders affecting protein homeostasis/import | Reviews classify PAM16 disease with mitochondrial skeletal disorders and distinguish it from other spondylo-epi-(meta)-physeal dysplasias (zhao2020skeletalphenotypesdue pages 5-6, zhao2023mitochondrialskeletaldisorders pages 45-50) | Review synthesis; moderate | mitochondrial skeletal disorder |
| Treatment/management | No disease-specific pharmacologic therapy established; management appears supportive | No interventional trials identified in tool search; literature retrieved did not report targeted treatment, surgery, or disease-modifying therapy (mehawej2014theimpairmentof pages 1-2, OpenTargets Search: spondylometaphyseal dysplasia Megarbane type-PAM16) | Evidence-gap conclusion from available sources; moderate | supportive care |
| Trials/real-world implementation | No disease-specific interventional trials were retrieved | Clinical-trial search returned no relevant interventional studies for SMDMDM/MAGMAS in available tooling (OpenTargets Search: spondylometaphyseal dysplasia Megarbane type-PAM16) | Database search negative finding; low-to-moderate | no disease-specific trial found |
| Recent developments (2023-2024) | Current understanding places PAM16 disease within TIM23/PAM importopathies | 2024 review notes Tim14/Tim16 regulate mtHsp70 ATPase activity and protein import; recent TIM23 reviews emphasize developmental phenotypes from import-complex mutations (jain2024hotspotsfordiseasecausing pages 7-8, palmer2021mitochondrialproteinimport pages 21-24) | Recent authoritative reviews; moderate | TIM23/PAM complex |
| Evidence gap: additional cases | A fifth, reportedly milder PAM16 case exists in secondary sources but was not directly extractable here | Review-level mention of Q74P and longer survival appears in secondary literature/open-targets links to PMID 27354339, but detailed primary-case extraction was unavailable in retrieved full text (zhao2023mitochondrialskeletaldisorders pages 45-50, OpenTargets Search: spondylometaphyseal dysplasia Megarbane type-PAM16) | Review/database only; limited | p.Gln74Pro (reported) |
| Evidence gap: epidemiology | Prevalence/incidence are unknown | Only a handful of reported patients/families; no registry-derived population estimate located in available evidence (mehawej2014theimpairmentof pages 1-2, OpenTargets Search: spondylometaphyseal dysplasia Megarbane type-PAM16) | Sparse literature; low | epidemiology not established |
| Evidence gap: biomarkers/omics | No validated disease-specific biomarkers or omics signatures found | No disease-specific proteomics, transcriptomics, metabolomics, or screening biomarker evidence identified in retrieved sources (jain2024hotspotsfordiseasecausing pages 7-8, palmer2021mitochondrialproteinimport pages 21-24) | Absence in available literature set; low | no validated biomarker identified |


*Table: This table compiles the highest-confidence evidence for autosomal recessive spondylometaphyseal dysplasia, Megarbane-Dagher-Melki type, emphasizing identifiers, human cases, PAM16/MAGMAS genetics, mechanism, diagnosis, and key evidence gaps. It is useful as a compact audit trail for knowledge-base curation.*

## 1. Disease information

### Definition and identifiers

SMDMDM is a **Mendelian, autosomal recessive, mitochondrial protein-import–related spondylodysplastic dysplasia**. “Spondylometaphyseal dysplasia” denotes combined vertebral and metaphyseal abnormalities; the original molecular paper also used the broader term “severe spondylodysplastic dysplasia.” (zhao2020skeletalphenotypesdue pages 5-6, mehawej2014theimpairmentof pages 1-2)

* **MONDO:** [MONDO:0013223](https://monarchinitiative.org/disease/MONDO:0013223)
* **OMIM:** **613320**, Spondylometaphyseal dysplasia, Megarbane-Dagher-Melki type
* **Causal gene:** **PAM16**, Ensembl **ENSG00000217930**; approved name, *presequence translocase associated motor 16*
* **Synonyms:** SMDMDM; Megarbane–Dagher–Melki-type spondylometaphyseal dysplasia; autosomal recessive SMD, Megarbane type; early-lethal spondylometaphyseal dysplasia; MAGMAS-associated severe spondylodysplastic dysplasia
* **ICD/MeSH:** No disease-specific ICD-10, ICD-11, or MeSH code was established in the retrieved evidence. Broader congenital osteochondrodysplasia categories would lose molecular specificity.

Open Targets maps MONDO:0013223 to PAM16 using five evidence records, including PMID **24786642** and PMID **27354339**. (OpenTargets Search: spondylometaphyseal dysplasia Megarbane type-PAM16)

**Evidence granularity:** Published information is principally aggregated from a very small number of individually described patients and pedigrees, not from EHR cohorts, registries, or population surveillance. The molecular landmark is Mehawej et al., *PLoS Genetics*, published **1 May 2014**, PMID **24786642**, DOI [10.1371/journal.pgen.1004311](https://doi.org/10.1371/journal.pgen.1004311). Its abstract states: “*Here, we report a homozygous mutation … in a novel and severe spondylodysplastic dysplasia*.” (mehawej2014theimpairmentof pages 1-2)

## 2. Etiology

The cause is **germline biallelic PAM16 dysfunction**. In the original families, affected children were homozygous for p.Asn76Asp, whereas parents and unaffected siblings were heterozygous. This segregation, absence from 550 Lebanese control chromosomes, conservation of Asn76, a shared founder haplotype, and functional impairment together provide strong causal evidence. (mehawej2014theimpairmentof pages 2-4)

* **Genetic risk:** Two pathogenic alleles inherited in trans. Consanguinity increases the probability that relatives carry the same founder allele but does not itself cause disease.
* **Family-history risk:** For two carrier parents, Mendelian expectations are 25% affected, 50% carrier, and 25% unaffected/non-carrier for each pregnancy.
* **Environmental, infectious, lifestyle, age, and sex risks:** None established. This is congenital genetic disease, not an acquired exposure-related disorder.
* **Protective variants/modifier genes:** None reported.
* **Gene–environment interaction:** No human evidence. Yeast temperature sensitivity is an experimental stress phenotype and should not be interpreted as evidence that fever or ambient temperature modifies human disease. (mehawej2014theimpairmentof pages 4-6)

## 3. Phenotypes

The original four cases support the following phenotype profile, although percentages are descriptive only because **n=4** and ascertainment was family-based. (mehawej2014theimpairmentof pages 2-4)

| Phenotype | Type, onset, course and observed frequency | Suggested HPO term |
|---|---|---|
| Prenatal and postnatal growth retardation | Sign/manifestation; congenital and progressive growth failure; reported as a shared feature | Intrauterine growth retardation; Postnatal growth retardation; Short stature |
| Short limbs/short long bones | Physical/radiographic; congenital, severe | Disproportionate short stature; Short long bones; Micromelia |
| Platyspondyly | Radiographic sign; severe at birth, improving somewhat with age | Platyspondyly (**HP:0000926**) |
| Metaphyseal abnormality | Radiographic; distal femoral widening and abnormal modeling | Metaphyseal abnormality; Metaphyseal widening |
| Pelvic abnormality | Square iliac bones and horizontal acetabulae | Abnormality of the ilium; Abnormal acetabulum morphology |
| Delayed epiphyseal ossification | Radiographic, infancy | Delayed epiphyseal ossification |
| Narrow thorax and short ribs | Physical/radiographic, congenital; clinically severe | Narrow chest; Short ribs |
| Prominent abdomen | Physical sign, childhood | Protuberant abdomen |
| Dysmorphic facial features | Physical sign; details incompletely captured | Abnormal facial shape |
| Developmental delay | Neurodevelopmental manifestation; reported across the syndrome | Global developmental delay (**HP:0001263**) |
| Respiratory insufficiency | Complication; lethal in both affected children of family 1 | Respiratory insufficiency/failure |
| Cardiomyopathy or heart failure | Complication; lethal in both affected children of family 2 | Cardiomyopathy (**HP:0001638**); Heart failure |

Quality-of-life instruments such as EQ-5D, SF-36, or PROMIS have not been reported. Severe growth restriction, thoracic compromise, developmental delay, and cardiopulmonary disease would be expected to profoundly impair mobility and daily functioning, but this is clinical inference rather than measured patient-reported evidence.

## 4. Genetic and molecular information

**PAM16/MAGMAS** lies at **16p13.3**, contains five exons in the reference used by the discovery study, and encodes an essential component of the mitochondrial PAM import motor. The main validated allele is **NM_016069:c.226A>G, p.Asn76Asp**, a germline homozygous missense variant in helix II of the protein’s J-like domain. (mehawej2014theimpairmentof pages 2-4, mehawej2014theimpairmentof pages 6-8)

Evidence supporting pathogenicity includes:

1. Complete cosegregation in two pedigrees.
2. Absence from 550 ethnically matched control chromosomes.
3. A 1.9-Mb common ancestral homozygous haplotype between D16S758 and D16S243.
4. Computational scores: MutationTaster 0.99999957, SIFT 0.006, PROVEAN −24.021, and PolyPhen-2 0.728.
5. Functional evidence for protein instability, defective import, and loss of yeast viability. (mehawej2014theimpairmentof pages 2-4, mehawej2014theimpairmentof pages 4-6)

These data would strongly support an ACMG/AMP pathogenic interpretation, although the retrieved article predates routine presentation under the current ACMG evidence-code framework. A second homozygous missense allele, **p.Gln74Pro**, is linked to PMID **27354339** and reportedly produced a milder phenotype and longer survival; detailed transcript notation, segregation, and present-day gnomAD frequency were not independently verified here. (zhao2023mitochondrialskeletaldisorders pages 45-50, OpenTargets Search: spondylometaphyseal dysplasia Megarbane type-PAM16)

No pathogenic structural variant, chromosomal rearrangement, somatic mutation, modifier gene, disease-specific methylation signature, or other epigenetic lesion has been established.

## 5. Environmental information

No toxin, radiation, pollution, occupation, diet, smoking, alcohol, exercise pattern, or infectious agent is known to initiate SMDMDM. Environmental avoidance cannot prevent the inherited genotype. General respiratory infection prevention and adequate nutrition may reduce complications but are supportive measures, not disease-specific protective factors.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic PAM16 missense variation leads to** altered residues in the MAGMAS J-like domain.
2. **The altered domain leads to** reduced MAGMAS stability and impaired PAM motor function; protein instability and import failure were demonstrated in yeast for p.Asn76Asp. (mehawej2014theimpairmentof pages 4-6)
3. **PAM dysfunction leads to** defective ATP-dependent translocation of presequence-bearing proteins through TIM23 into the mitochondrial matrix. (jain2024hotspotsfordiseasecausing pages 7-8, mehawej2014theimpairmentof pages 4-6)
4. **Defective import leads to** accumulation of unprocessed matrix precursors, exemplified by Hsp60 precursor, and disturbed mitochondrial proteostasis. (mehawej2014theimpairmentof pages 4-6)
5. **Proteostatic stress leads to** mitochondrial fragmentation, abnormal peroxisomal handling/pexophagy, impaired growth, and cell death in yeast. (mehawej2014theimpairmentof pages 6-8, mehawej2014theimpairmentof pages 4-6)
6. **In developing hypertrophic chondrocytes and osteoblast-lineage cells, these defects are inferred to lead to** impaired endochondral ossification; this tissue-level link is supported by developmental expression but has not been directly demonstrated in patient growth plates.
7. **Disordered ossification leads to** platyspondyly, metaphyseal modeling defects, delayed epiphyseal ossification, short limbs, and severe growth restriction.
8. **Thoracic skeletal restriction branches to respiratory insufficiency**, while **mitochondrial dysfunction in myocardium may branch to cardiomyopathy/heart failure**; direct causal partitioning remains unproven. (mehawej2014theimpairmentof pages 2-4, mehawej2014theimpairmentof pages 6-8)

### Molecular and cellular detail

PAM16/Tim16 partners with the J-protein Tim14/DNAJC19 to regulate mitochondrial HSPA9/mtHsp70 ATPase activity. The PAM motor supplies the inward pulling force for matrix-directed precursors traversing TIM23 after passage through TOM. A 2024 review identifies Tim14/Tim16 as regulators of mtHsp70-mediated protein import and places these disorders among early developmental TIM23 importopathies. (jain2024hotspotsfordiseasecausing pages 7-8)

MAGMAS was detected in trabecular bone, growth-plate cartilage, hypertrophic chondrocytes, primary spongiosa, osteoblasts, and osteocytes during early skeletal development. It was not appreciably detected in proliferative or resting-zone chondrocytes in the examined mouse growth plates. (mehawej2014theimpairmentof pages 6-8, mehawej2014theimpairmentof pages 4-6)

Suggested annotations:

* **GO biological process:** mitochondrial protein import; protein targeting to mitochondrion; mitochondrial transmembrane transport; mitochondrial organization; endochondral ossification; chondrocyte differentiation; osteoblast differentiation.
* **GO cellular component:** mitochondrial inner membrane; TIM23 mitochondrial import inner-membrane translocase complex; presequence translocase-associated import motor; mitochondrial matrix.
* **Cell Ontology:** hypertrophic chondrocyte; chondrocyte; osteoblast; osteocyte.

No disease-specific immune, inflammatory, lipidomic, metabolomic, single-cell, spatial-transcriptomic, patient proteomic, CRISPR-screen, or multi-omic signature has been reported. The 2024 TIM23 literature includes proteomics for other TIM23-component disorders, but those findings cannot be assigned to PAM16-associated SMDMDM. (jain2024hotspotsfordiseasecausing pages 7-8)

## 7. Anatomical structures affected

* **Primary system:** skeleton/connective tissue—vertebral bodies, growth plates, metaphyses, epiphyses, long bones, pelvis, ribs, and thorax.
* **Secondary organs:** lungs/respiratory apparatus through thoracic restriction; heart through cardiomyopathy or heart failure.
* **Tissue level:** growth-plate cartilage, trabecular bone, primary spongiosa.
* **Cell level:** especially hypertrophic chondrocytes and osteoblast/osteocyte lineages.
* **Subcellular level:** mitochondrial inner membrane, PAM/TIM23 machinery, and matrix-protein import pathway; peroxisomal abnormalities were observed only in the yeast model.
* **Lateralization:** generalized/bilateral skeletal involvement; no consistent unilateral or asymmetric pattern reported. (mehawej2014theimpairmentof pages 2-4, mehawej2014theimpairmentof pages 6-8)

Suggested UBERON concepts include vertebral body, rib, thorax, femur, metaphysis, epiphysis, growth plate, articular/epiphyseal cartilage, ilium, acetabulum, trabecular bone, heart, and lung. Exact identifiers should be ontology-validated during ingestion rather than inferred from labels.

## 8. Temporal development

Onset is **prenatal or congenital**, with prenatal growth restriction and skeletal abnormalities evident at birth. The disorder is chronic and progressive in its effect on growth, although neonatal platyspondyly may improve radiographically over time. In the original severe genotype, the critical period extends through fetal ossification and the first two postnatal years. Death occurred at 9 months or 2 years; no remission or recovery was described. (mehawej2014theimpairmentof pages 2-4)

No validated staging system or longitudinal progression model exists. The p.Gln74Pro report suggests genotype-dependent survival and expressivity, but the available evidence is too sparse for reliable stage or risk prediction. (zhao2023mitochondrialskeletaldisorders pages 45-50)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Homozygous affected children and heterozygous unaffected relatives support high penetrance for p.Asn76Asp in the observed families, but formal age-adjusted penetrance cannot be estimated. Expressivity is likely allele-dependent because p.Gln74Pro was reportedly milder. Genetic anticipation is not expected and has not been reported. Germline mosaicism has not been documented. (zhao2023mitochondrialskeletaldisorders pages 45-50, mehawej2014theimpairmentof pages 2-4)

The original cohort comprised two unrelated consanguineous Lebanese families with four affected children; family 2 had a reported consanguinity coefficient of **F=1/16**. A shared 1.9-Mb 16p13.3 segment supports a Lebanese founder effect for p.Asn76Asp. (mehawej2014theimpairmentof pages 2-4)

Prevalence, incidence, carrier frequency, sex ratio, and geographic distribution are unknown. “Four original cases” is a literature count, not an epidemiologic rate. No evidence supports sex-limited expression.

## 10. Diagnostics

### Recommended approach

1. **Clinical assessment:** prenatal/postnatal growth, body proportions, thoracic size, respiratory status, developmental assessment, and dysmorphology examination.
2. **Skeletal survey:** AP/lateral spine, pelvis, thorax, and long bones to identify platyspondyly, square iliac bones, horizontal acetabulae, short abnormally modeled long bones, widened distal femoral metaphyses, and delayed epiphyseal ossification. (mehawej2014theimpairmentof pages 2-4)
3. **Cardiopulmonary evaluation:** echocardiography, ECG as clinically indicated, oxygenation and respiratory assessment because heart failure and respiratory insufficiency caused death in the original families.
4. **Molecular confirmation:** sequence and deletion/duplication analysis of **PAM16**. A comprehensive skeletal-dysplasia/mitochondrial-disease panel or trio WES is efficient when the phenotype is not distinctive. WGS can detect coding, splice, copy-number, and deep-intronic variants missed by conventional testing.
5. **Variant confirmation:** Sanger confirmation and parental segregation; assess phase for two heterozygous variants.

The discovery study successfully used exome sequencing with homozygosity-by-descent filtering, followed by Sanger segregation. CMA, karyotype, FISH, mtDNA sequencing, and repeat-expansion testing are not first-line tests for an isolated, sequence-level PAM16 disorder unless another diagnosis is suspected. (mehawej2014theimpairmentof pages 2-4)

There are no standardized biochemical biomarkers, enzyme assays, histopathologic criteria, newborn-screening tests, or validated RNA/proteomic diagnostic signatures. Normal routine metabolic tests would not exclude disease.

### Differential diagnosis

The differential includes other severe spondylodysplastic and spondylo-epi-metaphyseal dysplasias, including **TRIP11**-related achondrogenesis 1A, **SLC35D1**-related Schneckenbecken dysplasia, Sedaghatian-type SMD, **SBDS**-related disease, **COL11A1** fibrochondrogenesis, **INPPL1** opsismodysplasia, **EXTL3**-related SEMD, and mitochondrial skeletal disorders involving **HSPA9, IARS2, PISD,** and **AIFM1**. Cardiomyopathy plus ataxia raises **DNAJC19**-related DCMA; ataxia was absent in the original PAM16 cases. (zhao2020skeletalphenotypesdue pages 5-6, mehawej2014theimpairmentof pages 1-2, mehawej2014theimpairmentof pages 6-8)

## 11. Outcome and prognosis

The original p.Asn76Asp cohort had severe morbidity and early mortality: one child died from respiratory insufficiency at **9 months**, another from respiratory insufficiency at **2 years**, and two died from heart failure at **2 years**. Thus, observed mortality was 4/4 by two years in those families, not a generalizable survival rate. (mehawej2014theimpairmentof pages 2-4)

Expected morbidity includes profound short stature, skeletal deformity, restricted thoracic capacity, developmental disability, and cardiopulmonary compromise. No formal disability, quality-of-life, 5-year survival, or life-expectancy study exists. Residual PAM16 function and genotype are plausible prognostic factors, but no validated biomarker or prognostic model is available.

## 12. Treatment

No approved disease-modifying pharmacotherapy, gene therapy, RNA therapy, cell therapy, enzyme replacement, or genotype-directed treatment has been reported. No relevant disease-specific interventional trial was retrieved. Current implementation is therefore supportive and multidisciplinary.

Reasonable care, extrapolated from skeletal-dysplasia and mitochondrial practice rather than tested in SMDMDM, includes:

* respiratory surveillance and prompt management of hypoxemia/infection;
* serial cardiology evaluation and guideline-based treatment of cardiomyopathy/heart failure;
* nutrition and growth monitoring;
* physical and occupational therapy with avoidance of unsafe skeletal loading;
* orthopedic and spine surveillance, with surgery individualized to anatomy and anesthetic risk;
* developmental therapies, mobility aids, pain management, and palliative-care involvement in severe disease.

No response rate, comparative outcome, adverse-event series, pharmacogenomic recommendation, or treatment algorithm is available. Suggested NCIt intervention concepts include genetic counseling, physical therapy, occupational therapy, respiratory therapy, echocardiography, orthopedic surgery, supportive care, and palliative care; exact NCIt codes should be validated before database loading.

## 13. Prevention

Primary lifestyle or vaccine prevention is not applicable to the genetic lesion. Reproductive prevention options include carrier testing of relatives, partner testing, preimplantation genetic testing for monogenic disease, chorionic-villus sampling, amniocentesis, or targeted prenatal testing when familial variants are known. Cascade screening is particularly relevant in an extended family carrying a founder allele.

Secondary prevention consists of early molecular diagnosis and cardiopulmonary surveillance. Tertiary prevention aims to reduce respiratory, cardiac, orthopedic, nutritional, and developmental complications. Genetic counseling should explain autosomal recessive recurrence risk, reproductive options, variable expressivity, and the limited natural-history evidence.

## 14. Other species and natural disease

No naturally occurring veterinary disease equivalent, breed association, zoonotic potential, or cross-species transmission is established. PAM16 is evolutionarily conserved. Human and murine mature MAGMAS proteins share **120 of 125 amino acids**, while deletion of the yeast ortholog is lethal; these findings support conservation of essential cellular function. (mehawej2014theimpairmentof pages 4-6)

Relevant taxa are *Homo sapiens* (**NCBI Taxon 9606**), *Mus musculus* (**10090**), *Saccharomyces cerevisiae* (**4932**), and *Drosophila melanogaster* (**7227**). The latter species supply comparative functional evidence, not naturally occurring clinical analogues.

## 15. Model organisms

The principal functional model is **S. cerevisiae pam16Δ complemented with human wild-type or p.Asn76Asp MAGMAS**. Wild-type human MAGMAS rescued growth, whereas mutant-expressing cells grew slowly at 34°C and failed to grow at 36°C under relevant conditions. At 37°C, mutant cells accumulated unprocessed Hsp60, had reduced MAGMAS protein, fragmented mitochondria, enhanced pexophagy, and loss of viability. This model strongly tests conserved import function but cannot reproduce vertebral anatomy, growth-plate physiology, cardiomyopathy, or human development. (mehawej2014theimpairmentof pages 4-6)

Wild-type mouse distal femur sections from embryonic day 16.5 through two weeks postnatal localized MAGMAS to hypertrophic chondrocytes, primary spongiosa, and bone cells. This is an expression/localization model, not a PAM16 disease knock-in or knockout model. (mehawej2014theimpairmentof pages 6-8, mehawej2014theimpairmentof pages 4-6)

Drosophila knockdown/deletion literature supports a conserved role in mitochondrial morphology, cell integrity, and viability, but no retrieved model was shown to reproduce the full human skeletal syndrome. No patient iPSC, chondrocyte organoid, zebrafish, conditional mouse, humanized knock-in, or PAM16 CRISPR disease model was identified.

## Recent developments and expert assessment

The most relevant 2023–2024 development is conceptual rather than therapeutic: SMDMDM is increasingly grouped with **mitochondrial skeletal disorders** and **TIM23/PAM importopathies**. A 2024 review emphasizes that TIM23 imports a large proportion of the nuclear-encoded mitochondrial proteome and that Tim16/PAM16 helps regulate mtHsp70-dependent import. This strengthens the mechanistic framework but does not add a large clinical cohort or intervention. (jain2024hotspotsfordiseasecausing pages 7-8, zhao2020skeletalphenotypesdue pages 5-6)

The strongest expert interpretation remains the discovery paper’s conclusion: “*The finding of deleterious MAGMAS mutations in an early lethal skeletal dysplasia supports a key role for this mitochondrial protein in the ossification process*.” It also directly reported that the mutation “*impairs the import of mitochondrial matrix pre-proteins and induces cell death*.” These are exact abstract statements, but the experiments underlying import failure and death were predominantly yeast-based. (mehawej2014theimpairmentof pages 1-2)

### Evidence limitations

This knowledge base entry rests mainly on two original families, one additional published case referenced by PMID 27354339, model-system experiments, and later reviews. Frequencies, penetrance, prognosis, and genotype–phenotype relationships therefore remain uncertain. No 2023–2024 patient cohort, registry, clinical trial, validated biomarker, disease-specific treatment, natural animal disease, or patient-derived multi-omics study was found. Claims not directly established—especially the precise link from mitochondrial import failure to human chondrocyte dysfunction—should be stored as **inferred mechanism**, not demonstrated human causality.

References

1. (mehawej2014theimpairmentof pages 2-4): Cybel Mehawej, Agnès Delahodde, Laurence Legeai-Mallet, Valérie Delague, Nabil Kaci, Jean-Pierre Desvignes, Zoha Kibar, José-Mario Capo-Chichi, Eliane Chouery, Arnold Munnich, Valérie Cormier-Daire, and André Mégarbané. The impairment of magmas function in human is responsible for a severe skeletal dysplasia. PLoS Genetics, 10:e1004311, May 2014. URL: https://doi.org/10.1371/journal.pgen.1004311, doi:10.1371/journal.pgen.1004311. This article has 61 citations and is from a domain leading peer-reviewed journal.

2. (zhao2023mitochondrialskeletaldisorders pages 45-50): Tian Rui Zhao. Mitochondrial skeletal disorders provide insight into the effect of mitochondrial proteostatic stress on steroidogenesis. Sep 2023. URL: https://doi.org/10.11575/prism/42113, doi:10.11575/prism/42113. This article has 0 citations.

3. (OpenTargets Search: spondylometaphyseal dysplasia Megarbane type-PAM16): Open Targets Query (spondylometaphyseal dysplasia Megarbane type-PAM16, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (mehawej2014theimpairmentof pages 6-8): Cybel Mehawej, Agnès Delahodde, Laurence Legeai-Mallet, Valérie Delague, Nabil Kaci, Jean-Pierre Desvignes, Zoha Kibar, José-Mario Capo-Chichi, Eliane Chouery, Arnold Munnich, Valérie Cormier-Daire, and André Mégarbané. The impairment of magmas function in human is responsible for a severe skeletal dysplasia. PLoS Genetics, 10:e1004311, May 2014. URL: https://doi.org/10.1371/journal.pgen.1004311, doi:10.1371/journal.pgen.1004311. This article has 61 citations and is from a domain leading peer-reviewed journal.

5. (mehawej2014theimpairmentof pages 4-6): Cybel Mehawej, Agnès Delahodde, Laurence Legeai-Mallet, Valérie Delague, Nabil Kaci, Jean-Pierre Desvignes, Zoha Kibar, José-Mario Capo-Chichi, Eliane Chouery, Arnold Munnich, Valérie Cormier-Daire, and André Mégarbané. The impairment of magmas function in human is responsible for a severe skeletal dysplasia. PLoS Genetics, 10:e1004311, May 2014. URL: https://doi.org/10.1371/journal.pgen.1004311, doi:10.1371/journal.pgen.1004311. This article has 61 citations and is from a domain leading peer-reviewed journal.

6. (zhao2020skeletalphenotypesdue pages 5-6): Tian Zhao, Caitlin Goedhart, Gerald Pfeffer, Steven C Greenway, Matthew Lines, Aneal Khan, A Micheil Innes, and Timothy E Shutt. Skeletal phenotypes due to abnormalities in mitochondrial protein homeostasis and import. Nov 2020. URL: https://doi.org/10.3390/ijms21218327, doi:10.3390/ijms21218327. This article has 11 citations.

7. (mehawej2014theimpairmentof pages 1-2): Cybel Mehawej, Agnès Delahodde, Laurence Legeai-Mallet, Valérie Delague, Nabil Kaci, Jean-Pierre Desvignes, Zoha Kibar, José-Mario Capo-Chichi, Eliane Chouery, Arnold Munnich, Valérie Cormier-Daire, and André Mégarbané. The impairment of magmas function in human is responsible for a severe skeletal dysplasia. PLoS Genetics, 10:e1004311, May 2014. URL: https://doi.org/10.1371/journal.pgen.1004311, doi:10.1371/journal.pgen.1004311. This article has 61 citations and is from a domain leading peer-reviewed journal.

8. (jain2024hotspotsfordiseasecausing pages 7-8): Sahil Jain, Eyal Paz, and Abdussalam Azem. Hotspots for disease-causing mutations in the mitochondrial tim23 import complex. Genes, 15:1534, Nov 2024. URL: https://doi.org/10.3390/genes15121534, doi:10.3390/genes15121534. This article has 1 citations.

9. (palmer2021mitochondrialproteinimport pages 21-24): Catherine S. Palmer, Alexander J. Anderson, and Diana Stojanovski. Mitochondrial protein import dysfunction: mitochondrial disease, neurodegenerative disease and cancer. Jan 2021. URL: https://doi.org/10.1002/1873-3468.14022, doi:10.1002/1873-3468.14022. This article has 151 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Recessive_Spondylometaphyseal_Dysplasia_Megarbane_Type-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013223` (7 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **autosomal recessive spondylometaphyseal dysplasia, Megarbane type**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0013223` - called "if available", "MONDO"