---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-06T02:48:42.568615'
end_time: '2026-09-06T03:09:57.679109'
duration_seconds: 1275.11
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Multiple Mitochondrial Dysfunctions Syndrome 5
  mondo_id: MONDO:0033282
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 45
  verified: 44
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0033282
    reported_labels:
    - if available
    ontology_label: multiple mitochondrial dysfunctions syndrome 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Multiple_Mitochondrial_Dysfunctions_Syndrome_5-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Multiple Mitochondrial Dysfunctions Syndrome 5
- **MONDO ID:** MONDO:0033282 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Multiple Mitochondrial Dysfunctions Syndrome 5** covering all of the
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
- **Disease Name:** Multiple Mitochondrial Dysfunctions Syndrome 5
- **MONDO ID:** MONDO:0033282 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Multiple Mitochondrial Dysfunctions Syndrome 5** covering all of the
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


# Multiple Mitochondrial Dysfunctions Syndrome 5 (MMDS5): Disease-Characteristics Report

## Executive summary

Multiple mitochondrial dysfunctions syndrome 5 (MMDS5) is an ultra-rare, autosomal-recessive mitochondrial leukodystrophy caused by biallelic pathogenic variants in **ISCA1**, a nuclear gene required for late-stage maturation of mitochondrial iron–sulfur proteins. The defining clinical pattern is infantile-onset developmental failure or regression, progressive spastic neurologic disease, and extensive cerebral/cerebellar white-matter abnormalities, often accompanied by lactic acidosis and impaired mitochondrial protein lipoylation. Evidence remains exceptionally sparse: the most systematic published synthesis identified only **seven affected individuals from five families**, of whom five had died between 11 months and 11 years. No population incidence or prevalence, validated clinical criteria, disease-specific quality-of-life study, disease-modifying treatment, or relevant interventional trial was identified. (lebigot2021areviewof pages 17-18)

The most recent directly relevant development identified for this report is a **2023 neuron-specific Isca1-knockout rat**, which develops epilepsy, developmental and memory impairment, neuronal loss, mitochondrial structural injury, respiratory-chain-protein reduction, and ATP depletion. No new 2023–2024 human MMDS5 cohort or disease-specific omics study was found. (sheng2023aneuron‐specificisca1 pages 1-2)

The following structured summary highlights the principal evidence.

| Domain | Established finding | Quantitative evidence | Evidence type | Key source/date/DOI |
|---|---|---:|---|---|
| Disease identity | Multiple mitochondrial dysfunctions syndrome 5 (MMDS5), also called ISCA1-related multiple mitochondrial dysfunctions syndrome (ISCA1-MMDS); autosomal-recessive mitochondrial iron-sulfur-cluster biogenesis disorder | OMIM phenotype 617613; ISCA1 OMIM 611006; locus 9q21.33; protein 129 aa | Curated disease resource | GeneReviews, created 2019 (mp1993isca1relatedmultiplemitochondriala pages 10-13, mp1993isca1relatedmultiplemitochondrialc pages 1-3) |
| Reported cases | Published evidence summarized five Indian individuals, one Italian individual, and one Egyptian individual from five families | 7 patients; 5 families | Systematic review of human cases | Lebigot et al., 2021; DOI: https://doi.org/10.3390/biomedicines9080989 (lebigot2021areviewof pages 17-18) |
| Core phenotype | Early progressive encephalopathy or neurodegeneration with developmental failure or regression, spasticity, and leukodystrophy; severity ranges from severe neonatal disease to a moderately severe, longer-surviving course | Spasticity 7/7; onset from neonatal period to 20 months | Aggregated human clinical evidence | Lebigot et al., 2021; DOI: https://doi.org/10.3390/biomedicines9080989 (lebigot2021areviewof pages 17-18) |
| Neurologic frequencies | Nystagmus and seizures occur but are not universal in the very small series | Nystagmus 2/7; seizures 2/7 | Aggregated human clinical evidence | Lebigot et al., 2021; DOI: https://doi.org/10.3390/biomedicines9080989 (lebigot2021areviewof pages 17-18) |
| Neuroimaging | Diffuse cerebral and cerebellar white-matter disease, sometimes cavitating or vacuolating; ventriculomegaly, pachygyria, thin corpus callosum, delayed myelination, and brainstem or spinal-cord involvement have been reported | MRS lipid-lactate peak in 4/4 evaluated individuals in the curated summary | Human MRI and MRS evidence | Shukla et al., 2017; DOI: https://doi.org/10.1038/jhg.2017.35; GeneReviews, 2019 (shukla2017homozygousp.(glu87lys)variant pages 1-2, mp1993isca1relatedmultiplemitochondrialc pages 3-6) |
| Prognosis | Prognosis is generally poor but survival varies; one individual died during pneumonia at age 11 years | Deaths 5/7; reported death ages 11 months to 11 years | Human natural-history evidence | Torraco et al., 2018; DOI: https://doi.org/10.1093/hmg/ddy273; Lebigot et al., 2021 (torraco2018isca1mutationin pages 1-2, lebigot2021areviewof pages 17-18) |
| Founder variant | Homozygous ISCA1 c.259G>A, p.(Glu87Lys), causes MMDS5 and is a probable southwestern Indian founder allele | Four affected children in the initial two families; shared 3.3-Mb homozygous region; ExAC AF 0.000008427; gnomAD AF 0.000004163; later reported in four families | Human segregation, population, and computational evidence | Shukla et al., published March 30, 2017; DOI: https://doi.org/10.1038/jhg.2017.35 (shukla2017homozygousp.(glu87lys)variant pages 1-2, shukla2017homozygousp.(glu87lys)variant pages 3-5, mp1993isca1relatedmultiplemitochondrialc pages 1-3) |
| Presequence variant | Homozygous ISCA1 c.29T>G, p.(Val10Gly), affects the N-terminal mitochondrial presequence and reduces protein stability and functional complementation; both parents were heterozygous | One patient; fibroblast ATP synthesis reduced 67% with succinate, 31% with malate, and 26% with pyruvate plus malate | Human case, fibroblast, autopsy-tissue, and complementation evidence | Torraco et al., August 2018; DOI: https://doi.org/10.1093/hmg/ddy273 (torraco2018isca1mutationin pages 3-4, torraco2018isca1mutationin pages 2-3, torraco2018isca1mutationin pages 8-9) |
| Fe-S-stability variant | Homozygous NM_030940.4:c.302A>G, p.(Tyr101Cys); both parents were heterozygous; mutant ISCA1 carried an unstable Fe-S cluster, and fibroblasts showed defective lipoylation and complex-II-linked respiration | One patient; lactate 3.2 mmol/L; pyruvate 0.23 mmol/L; complex II to citrate-synthase ratio 0.23 versus reference 0.24-0.38 | Human case, fibroblast biochemistry, and recombinant-protein evidence | Lebigot et al., online February 21, 2020; DOI: https://doi.org/10.1016/j.mito.2020.02.008 (lebigot2020expandingthephenotype pages 1-2, lebigot2020expandingthephenotype pages 3-4) |
| Mechanism | Reduced ISCA1 function disrupts late mitochondrial [4Fe-4S] protein maturation while tested [2Fe-2S] clients are relatively preserved; affected clients include respiratory complexes I and II, aconitase, ETFDH, and lipoic-acid synthase | Mutant complementation left some complex I and II activities up to 50% below wild-type-complemented cells | Patient-derived and engineered-cell functional evidence | Torraco et al., 2018; DOI: https://doi.org/10.1093/hmg/ddy273 (torraco2018isca1mutationin pages 4-5, torraco2018isca1mutationin pages 1-2, torraco2018isca1mutationin pages 12-13) |
| Downstream metabolism | Lipoic-acid-synthase dysfunction reduces lipoylation and function of PDH and alpha-ketoglutarate dehydrogenase; respiratory impairment reduces ATP and contributes to lactate accumulation. The final link to white-matter loss is partly inferred | Elevated blood lactate in 6/7; urinary glycine elevation in one individual | Human biochemical evidence plus mechanistic inference | GeneReviews, 2019; Torraco et al., 2018; Lebigot et al., 2021 (mp1993isca1relatedmultiplemitochondrialc pages 3-6, torraco2018isca1mutationin pages 6-7, lebigot2021areviewof pages 17-18) |
| Diagnosis | Confirm by identifying biallelic pathogenic ISCA1 variants. Use an ISCA1-containing leukodystrophy or mitochondrial panel, exome sequencing, or genome sequencing; targeted founder testing is reasonable for southwestern Indian ancestry. MRI, MRS, lactate, CPK, respiratory-chain assays, and lipoylation studies are supportive but nonspecific | ISCA1 sequence analysis detected pathogenic variants in 5/5 probands in the curated summary; targeted c.259G>A testing detected 4/5 | Curated diagnostic guidance supported by cases | GeneReviews, created October 3, 2019 (mp1993isca1relatedmultiplemitochondriala pages 1-3, mp1993isca1relatedmultiplemitochondrialc pages 1-3, mp1993isca1relatedmultiplemitochondriald pages 1-3) |
| Treatment | No established disease-modifying therapy. Care is phenotype-directed, including seizure and spasticity treatment, rehabilitation, nutritional and swallowing support, assistive devices, aspiration surveillance, and palliative support. Bicarbonate, Nissen fundoplication, and gastrostomy were used in one patient | No controlled response rates | Expert guidance and observed supportive care | GeneReviews, 2019; Torraco et al., 2018; DOI: https://doi.org/10.1093/hmg/ddy273 (mp1993isca1relatedmultiplemitochondriald pages 8-10, torraco2018isca1mutationin pages 1-2) |
| Clinical trials | No MMDS5-specific interventional study or NCT identifier was found; cellular rescue with wild-type ISCA1 is proof of mechanism, not clinical gene therapy | 0 relevant trials identified | Trial-registry search and preclinical evidence | ClinicalTrials.gov search; Torraco et al., 2018 (torraco2018isca1mutationin pages 1-2, mp1993isca1relatedmultiplemitochondriala pages 10-13) |
| Constitutive rat model | Whole-body Isca1 knockout causes embryonic lethality, demonstrating an essential developmental role but preventing postnatal disease modeling | Abnormal development by embryonic day 8.5; no homozygotes recovered among 83 litters | CRISPR-Cas9 rat model | Yang et al., March 2019; DOI: https://doi.org/10.1002/ame2.12059 (yang2019knockoutofisca1 pages 1-2, yang2019knockoutofisca1 pages 2-5) |
| Myocardial rat model | Alpha-MHC-Cre myocardial Isca1 deletion causes mitochondrial and iron-homeostasis abnormalities, reduced ATP, cardiomyocyte oncosis, heart failure, and neonatal death; this cardiac phenotype is model evidence and is not established as a frequent human manifestation | Knockout efficiency 84.26%; all homozygous knockout pups died by postnatal day 10 | Conditional CRISPR and Cre-Lox rat model | Ling et al., May 2022; DOI: https://doi.org/10.1016/j.lfs.2022.120485 (ling2022myocardiumspecificisca1knockout pages 5-9, ling2021isca1deficiencyinduces pages 12-15, ling2022myocardiumspecificisca1knockout pages 1-2) |
| Neuronal rat model | NeuN-Cre neuron-specific Isca1 knockout recapitulates developmental delay, epilepsy, motor and memory impairment, neuronal loss, dendritic-spine loss, mitochondrial fragmentation, cristae damage, reduced respiratory-chain proteins, and ATP depletion | Survival approximately 8 weeks | Conditional CRISPR and Cre-Lox neurological rat model | Sheng et al., April 2023; DOI: https://doi.org/10.1002/ame2.12318 (sheng2023aneuron‐specificisca1 pages 1-2, sheng2023aneuron‐specificisca1 pages 2-3) |
| Epidemiology | Population prevalence, incidence, birth prevalence, carrier frequency, geographic distribution, and sex ratio are unavailable; published-case counts must not be treated as epidemiologic rates | Unavailable; seven published patients in five families in the 2021 synthesis | Evidence-gap assessment | Lebigot et al., 2021; DOI: https://doi.org/10.3390/biomedicines9080989 (lebigot2021areviewof pages 17-18) |
| Omics | No MMDS5-specific unbiased transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or integrated multi-omic study was identified; available studies used targeted biochemical, imaging, RNAi, and complementation assays | Unavailable for disease-specific omics | Evidence-gap assessment | Torraco et al., 2018; Ling et al., 2022; Sheng et al., 2023 (torraco2018isca1mutationin pages 2-3, torraco2018isca1mutationin pages 8-9, ling2022myocardiumspecificisca1knockout pages 5-9, sheng2023aneuron‐specificisca1 pages 1-2) |


*Table: Compact knowledge-base-ready summary of MMDS5 identity, reported patients, phenotypes, causal variants, mechanism, diagnosis, management, and rat models. It also identifies major evidence gaps in epidemiology, clinical trials, and omics.*

## Evidence conventions and limitations

* **Human clinical evidence** refers to molecularly confirmed patients.
* **Human functional evidence** refers principally to patient fibroblasts and autopsy tissues.
* **Model evidence** includes engineered HeLa cells and rat knockouts and must not be interpreted as an established human phenotype.
* Because published reports are very small, fractions such as 7/7 are **case-series frequencies, not population estimates**.
* The retrieval set did not reliably expose PubMed identifiers for every paper. DOI URLs and publication dates are therefore given rather than inventing PMIDs. The apparent “1993” metadata attached to retrieved GeneReviews text is erroneous; the chapter states that it was created **October 3, 2019**.

---

## 1. Disease information

### Definition

MMDS5 is an inherited disorder of mitochondrial iron–sulfur-cluster maturation. Loss of ISCA1 function compromises selected mitochondrial [4Fe–4S] proteins, producing combined respiratory-chain, tricarboxylic-acid-cycle, and lipoic-acid-dependent enzyme dysfunction. Clinically, it is primarily a severe early-onset neurodegenerative leukodystrophy. (mp1993isca1relatedmultiplemitochondrialc pages 1-3, lebigot2021areviewof pages 17-18)

### Identifiers and synonyms

* **MONDO:** MONDO:0033282, as specified in the target record; this identifier was not independently verified in the retrieved literature.
* **OMIM phenotype:** **617613**, Multiple mitochondrial dysfunctions syndrome 5.
* **Causal-gene OMIM:** **ISCA1, 611006**.
* **Gene/locus:** **ISCA1**, chromosome **9q21.33**; protein length reported as 129 amino acids.
* **Synonyms:** MMDS5; multiple mitochondrial dysfunctions syndrome type 5; ISCA1-related multiple mitochondrial dysfunctions syndrome; ISCA1-MMDS; ISCA1-related mitochondrial leukodystrophy. (mp1993isca1relatedmultiplemitochondriala pages 10-13, mp1993isca1relatedmultiplemitochondrialb pages 10-13)
* **Orphanet, MeSH, ICD-10, ICD-11:** no MMDS5-specific identifier was established from the retrieved sources. In practice, broader mitochondrial-metabolism or leukodystrophy codes may be used, but these should not be treated as disease-specific mappings.

The evidence is predominantly **aggregated disease-level literature and curated-resource information**, derived originally from individual case reports and families rather than EHR-scale patient data. The 2021 review aggregated seven patients from five families. (lebigot2021areviewof pages 17-18)

---

## 2. Etiology

### Causal factor

The primary cause is **germline biallelic ISCA1 loss of function or severe hypomorphic dysfunction**. All clearly described patients were homozygous for a rare missense allele; healthy parents were heterozygous where tested. The inheritance pattern is autosomal recessive. (shukla2017homozygousp.(glu87lys)variant pages 3-5, torraco2018isca1mutationin pages 3-4, lebigot2020expandingthephenotype pages 3-4)

### Genetic risk factors

Three disease-associated variants were documented:

1. **c.259G>A, p.(Glu87Lys)** — probable southwestern Indian founder allele. It affects a highly conserved residue in the Fe–S-biogenesis domain. Two initial families shared a 3.3-Mb homozygous region around ISCA1. Contemporary frequencies reported in the original analysis were 1/118,662 alleles in ExAC (AF 8.427×10⁻⁶) and 1/240,238 in gnomAD (AF 4.163×10⁻⁶). Modeling predicted loss of a Glu87–Lys49 salt bridge and protein destabilization. (shukla2017homozygousp.(glu87lys)variant pages 3-5)
2. **c.29T>G, p.(Val10Gly)** — homozygous in one affected boy, heterozygous in both healthy parents, absent from databases consulted in the report, and located in the N-terminal mitochondrial targeting/presequence region. Functional experiments demonstrated reduced protein stability and defective [4Fe–4S]-protein maturation. (torraco2018isca1mutationin pages 3-4, torraco2018isca1mutationin pages 8-9)
3. **NM_030940.4:c.302A>G, p.(Tyr101Cys)** — homozygous in an Egyptian-origin patient and heterozygous in both parents; absent from 1000 Genomes, dbSNP, and ExAC at publication. Recombinant mutant protein carried an unstable Fe–S cluster, while patient fibroblasts had defective lipoylation and complex-II-linked respiration. (lebigot2020expandingthephenotype pages 1-2, lebigot2020expandingthephenotype pages 3-4)

Formal current ClinVar assertions and ACMG/AMP evidence codes were not available in the retrieved evidence and should be checked directly at ingestion time. No pathogenic deletion/duplication had been reported in the GeneReviews testing summary. (mp1993isca1relatedmultiplemitochondriala pages 1-3)

### Environmental, protective, and gene–environment factors

No established environmental toxin, radiation, occupational, lifestyle, dietary, infectious, immune, or sex-specific causal factor has been demonstrated. No protective variant or environmental protective factor is known. Intercurrent infection may worsen clinical vulnerability—the p.Val10Gly patient died during pneumonia and an affected sibling reportedly died after infection—but this does not establish a specific gene–infection interaction or infection-triggered metabolic-crisis mechanism. (mp1993isca1relatedmultiplemitochondriald pages 8-10, torraco2018isca1mutationin pages 1-2)

Consanguinity increases the probability that two carriers share a rare allele but is not required: one original Indian family was consanguineous and another was not; the p.Val10Gly patient’s parents were described as non-consanguineous in the primary report. (shukla2017homozygousp.(glu87lys)variant pages 1-2, torraco2018isca1mutationin pages 2-3)

---

## 3. Phenotypes

### Aggregate clinical spectrum

Among the seven patients summarized in 2021, **spasticity occurred in 7/7**, nystagmus in **2/7**, and seizures in **2/7**. Onset ranged from the neonatal period or 2–3 months to 20 months. Severe patients attained few or no milestones; a milder patient regained walking but remained easily fatigued with severe language delay. Five of seven had died. These figures are vulnerable to ascertainment and reporting bias. (lebigot2020expandingthephenotype pages 1-2, lebigot2021areviewof pages 17-18)

Suggested phenotype annotations include:

* Developmental delay/intellectual disability — **HP:0001263, HP:0001249**; usually severe and progressive.
* Developmental regression — **HP:0002376**; infantile onset, although not universal in the same form.
* Spasticity — **HP:0001257**; reported in 7/7.
* Seizure — **HP:0001250**; reported in 2/7 in the aggregated review, although all four children in the first series had early seizures.
* Hypotonia/weakness — **HP:0001252, HP:0001324**; reported variably.
* Ataxia/spastic ataxia — **HP:0001251**; prominent in the longer-surviving p.Val10Gly patient.
* Nystagmus — **HP:0000639**; 2/7.
* Feeding difficulty/weak suck/dysphagia — **HP:0011968, HP:0008872, HP:0002015**.
* Neurogenic bladder/urinary retention — **HP:0000011, HP:0000016**; documented in the p.Val10Gly patient.
* Pigmentary retinal change — **HP:0007703**; observed in one original patient, but frequency is uncertain.
* Lactic acidosis/elevated lactate — **HP:0003128, HP:0002151**; plasma lactate was elevated in 6/7 in the curated summary.
* Elevated creatine kinase — **HP:0003236**; at least one patient.
* Hyperglycinuria/elevated glycine — **HP:0003108** where appropriate; only one MMDS5 case had elevated urinary glycine in the review.
* Leukodystrophy/abnormal cerebral white matter — **HP:0002415, HP:0002500**.
* Pachygyria — **HP:0001302**.
* Ventriculomegaly — **HP:0002119**.
* Thin corpus callosum — **HP:0002079**.

The initial four children developed neonatal or early-infantile neurologic deterioration and seizures at 2–5 months. Death occurred at 11 months, 1 year 7 months, 2 years 3 months, and 5 years. (shukla2017homozygousp.(glu87lys)variant pages 1-2)

The p.Val10Gly patient lost head control at three months, later recovered some abilities, developed severe spastic ataxia, dysarthria, persistent nystagmus, dysphagia, and neurogenic bladder, and died from pneumonia at age 11. At eight years, bicarbonate was 14.6 mM, base excess −9.0 mEq, and lactate 2.8 mM. (torraco2018isca1mutationin pages 1-2)

The p.Tyr101Cys patient first regressed at 20 months, losing gait and language. By four years he had regained walking but fatigued easily and retained severe language delay, illustrating meaningful phenotypic variability. (lebigot2020expandingthephenotype pages 1-2)

### Imaging and laboratory abnormalities

MRI findings include bilateral cerebral and cerebellar leukodystrophy, delayed/dysmyelination, cavitation or vacuolation, thin corpus callosum, ventriculomegaly, pachygyria, and occasional brainstem/spinal-cord involvement. MRS showed a lipid–lactate peak in all four individuals evaluated in one curated summary. (mp1993isca1relatedmultiplemitochondrialc pages 1-3, mp1993isca1relatedmultiplemitochondrialc pages 3-6)

Laboratory abnormalities are supportive rather than diagnostic. Reported values include blood lactate 36 and 40.5 mg/dL and CPK 568 versus 42 IU/L in two original patients. The p.Tyr101Cys patient had lactate 3.2 mmol/L and pyruvate 0.23 mmol/L with a normal lactate/pyruvate ratio. (shukla2017homozygousp.(glu87lys)variant pages 3-5, lebigot2020expandingthephenotype pages 3-4)

### Quality-of-life impact

No validated EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life data exist. Nevertheless, severe motor and cognitive disability, epilepsy, dysphagia, communication impairment, mobility loss, bladder dysfunction, and need for gastrostomy or palliative support imply profound effects on independence and family caregiving. This is a clinical inference, not a quantified patient-reported outcome. (torraco2018isca1mutationin pages 1-2, mp1993isca1relatedmultiplemitochondrialb pages 8-10)

---

## 4. Genetic and molecular information

**ISCA1** encodes a mitochondrial Fe–S carrier/assembly protein participating with ISCA2 and IBA57 in late [4Fe–4S]-cluster biogenesis. Suggested annotations include **HGNC:28660** (verify against HGNC before production use), GO biological process **iron–sulfur cluster assembly (GO:0016226)** and **mitochondrial respiratory-chain-complex assembly**, and GO cellular component **mitochondrial matrix (GO:0005759)**. The protein contains a conserved C-terminal HESB-related signature. (shukla2017homozygousp.(glu87lys)variant pages 3-5, mp1993isca1relatedmultiplemitochondriald pages 10-13)

All established MMDS5 variants are germline missense substitutions. Functional consequences support loss-of-function or severe hypomorphic behavior rather than gain of function or dominant-negative action. No somatic etiology is implicated. No modifier gene, epigenetic signature, DNA-methylation abnormality, chromosomal rearrangement, repeat expansion, anticipation, or germline mosaicism has been established. Penetrance appears high for individuals with the reported homozygous genotypes, but the sample is too small for a formal estimate. (torraco2018isca1mutationin pages 3-4, lebigot2020expandingthephenotype pages 3-4, mp1993isca1relatedmultiplemitochondriald pages 10-13)

---

## 5. Environmental information

MMDS5 is not known to be caused by toxins, pollution, radiation, occupational exposure, smoking, alcohol, diet, or an infectious agent. Immune deficiency or autoimmunity has not been demonstrated. No evidence-based lifestyle modification changes primary disease risk. Clinically important secondary risks include dysphagia, aspiration, malnutrition, constipation, respiratory insufficiency, and intercurrent infection. (mp1993isca1relatedmultiplemitochondriald pages 8-10, mp1993isca1relatedmultiplemitochondrialb pages 8-10)

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic ISCA1 variants lead to reduced or dysfunctional ISCA1 protein.** This is demonstrated by segregation and patient-cell studies. (torraco2018isca1mutationin pages 3-4, lebigot2020expandingthephenotype pages 3-4)
2. **Reduced ISCA1 stability/function leads to failure of late mitochondrial [4Fe–4S]-cluster maturation.** For p.Val10Gly, reduced abundance and increased proteolytic turnover are demonstrated; involvement of the ISCA1–ISCA2–IBA57 transfer node is strongly supported by pathway biology but not measured directly in the patient. (torraco2018isca1mutationin pages 1-2, torraco2018isca1mutationin pages 8-9)
3. **Defective [4Fe–4S] maturation leads to dysfunction of selected client proteins**, particularly respiratory complexes I and II, aconitase/ACO2, ETFDH, and lipoic-acid synthase (LIAS), while tested [2Fe–2S] clients such as the complex-III Rieske protein are relatively preserved. (torraco2018isca1mutationin pages 6-7, torraco2018isca1mutationin pages 12-13)
4. **Respiratory-chain dysfunction leads to reduced oxidative phosphorylation and ATP synthesis.** In p.Val10Gly fibroblasts, ATP synthesis was reduced by 67% with succinate, 31% with malate, and 26% with pyruvate plus malate. (torraco2018isca1mutationin pages 2-3)
5. **LIAS dysfunction leads to reduced protein lipoylation**, which results in secondary impairment of pyruvate dehydrogenase, α-ketoglutarate dehydrogenase, and potentially branched-chain ketoacid dehydrogenase. Loss of PDH-E2 and KGDH-E2 lipoylation is demonstrated; the full BCKDH contribution in MMDS5 is partly inferred. (torraco2018isca1mutationin pages 6-7, torraco2018isca1mutationin pages 4-5)
6. **Respiratory and dehydrogenase failure leads to impaired pyruvate/TCA-cycle flux and lactate accumulation.** Hyperlactatemia is clinically demonstrated, whereas precise flux causality has not been directly measured in patients. (lebigot2021areviewof pages 17-18, lebigot2020expandingthephenotype pages 3-4)
7. **Energy failure branches by tissue:**
   * **Neural branch:** energy failure and mitochondrial structural injury are inferred to lead to neuronal/axonal dysfunction, dysmyelination or white-matter degeneration, which results in regression, spasticity, seizures, ataxia, and leukodystrophy. Neuronal oncosis and synaptic injury are demonstrated in the conditional rat, not human tissue. (sheng2023aneuron‐specificisca1 pages 1-2)
   * **Muscle/respiratory branch:** impaired bioenergetics likely leads to weakness, fatigability, dysphagia, and vulnerability to respiratory complications; the causal tissue sequence is incompletely demonstrated in humans. (torraco2018isca1mutationin pages 1-2, lebigot2020expandingthephenotype pages 3-4)
   * **Cardiac branch:** Isca1 loss leads to iron dysregulation, mitochondrial damage, ATP loss, cardiomyocyte oncosis, and heart failure in conditional rats. This branch is model-derived and should not be coded as a common human MMDS5 manifestation. (ling2022myocardiumspecificisca1knockout pages 5-9, ling2022myocardiumspecificisca1knockout pages 1-2)

No specific Wnt, MAPK, mTOR, PI3K–AKT, or immune-inflammatory pathway has been validated in MMDS5. The principal pathway is mitochondrial Fe–S-cluster biogenesis coupled to OXPHOS, the TCA cycle, fatty-acid electron transfer, and lipoate metabolism.

Suggested terms include GO:0016226 iron–sulfur cluster assembly; GO:0032981 mitochondrial respiratory-chain-complex I assembly; GO:0006121 complex-II-linked electron transport; GO:0045454 cellular redox homeostasis; GO:0006099 TCA cycle; GO:0006096 glycolytic process; GO:0046034 ATP metabolic process; GO:0007005 mitochondrion organization; and GO:0005759 mitochondrial matrix. Suggested cell terms include **CL:0000540 neuron**, **CL:0000127 astrocyte**, **CL:0000128 oligodendrocyte**, and **CL:0000746 cardiomyocyte**; only neurons and cardiomyocytes have direct conditional-model evidence, while oligodendrocyte involvement is inferred from leukodystrophy.

### Molecular profiling and advanced technologies

No MMDS5-specific unbiased transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or integrated multi-omic dataset was identified. Available work consists of targeted immunoblotting, enzyme assays, oxygen consumption, ATP synthesis, RNAi/complementation, recombinant-protein biophysics, MRI/MRS, and electron microscopy. CRISPR/Cas9 has been used to generate rat models, not as therapy. (torraco2018isca1mutationin pages 2-3, ling2022myocardiumspecificisca1knockout pages 5-9, sheng2023aneuron‐specificisca1 pages 1-2)

---

## 7. Anatomical structures affected

The **central nervous system** is primary: cerebral and cerebellar white matter, corpus callosum, cerebral cortex/migration, brainstem, and sometimes spinal cord. Suggested anatomy terms include **UBERON:0000955 brain**, **UBERON:0002316 white matter**, **UBERON:0002037 cerebellum**, **UBERON:0002336 corpus callosum**, **UBERON:0002298 brainstem**, and **UBERON:0002240 spinal cord**. Lesions are typically bilateral and relatively symmetric rather than lateralized. (mp1993isca1relatedmultiplemitochondrialc pages 1-3, mp1993isca1relatedmultiplemitochondrialc pages 3-6)

Secondary clinically involved systems include skeletal/respiratory muscle, swallowing apparatus, eyes/retina, auditory pathways, and urinary bladder. The heart is biologically vulnerable in rat models, but recurrent human cardiomyopathy has not been established. At the subcellular level, the central compartment is the mitochondrial matrix and inner-membrane respiratory apparatus; enlarged mitochondria and cristae loss follow depletion of ISCA proteins in experimental systems. (torraco2018isca1mutationin pages 1-2, ling2022myocardiumspecificisca1knockout pages 5-9, yang2019knockoutofisca1 pages 1-2)

---

## 8. Temporal development

Onset is usually neonatal or in early infancy, although onset at 20 months documents a broader range. The usual course is chronic and progressive, with failure to attain milestones or developmental regression, increasing spasticity, and progressive white-matter disease. Some functions can be regained: the p.Val10Gly patient recovered head control and later sat unsupported, while the p.Tyr101Cys patient regained walking. Thus, progression is not necessarily monotonic. (torraco2018isca1mutationin pages 1-2, lebigot2020expandingthephenotype pages 1-2)

No validated staging system exists. Pragmatic stages are: presymptomatic/early infancy; developmental arrest or regression; established spastic leukodystrophy with feeding and mobility disability; and advanced multisystem disease with aspiration/respiratory vulnerability. No spontaneous remission has been documented. Early genomic testing is the principal actionable window because it ends the diagnostic odyssey and enables anticipatory care and reproductive counseling, rather than because a proven disease-modifying treatment exists. (mp1993isca1relatedmultiplemitochondrialc pages 1-3, mp1993isca1relatedmultiplemitochondriald pages 8-10)

---

## 9. Inheritance and population

Inheritance is autosomal recessive. When both parents are carriers, each pregnancy has a **25% affected, 50% carrier, and 25% unaffected/non-carrier** probability. Heterozygous carriers are expected to be asymptomatic. (mp1993isca1relatedmultiplemitochondriala pages 10-13, mp1993isca1relatedmultiplemitochondrialb pages 10-13)

The published patients summarized in 2021 comprised five Indian individuals, one Italian individual, and one Egyptian-origin individual. The c.259G>A/p.Glu87Lys allele is a likely southwestern Indian founder variant. There are no reliable prevalence, incidence, birth-prevalence, overall carrier-frequency, sex-ratio, or geographic-rate data. The count of seven published patients must not be converted into an epidemiologic rate. No anticipation has been reported. (lebigot2021areviewof pages 17-18, shukla2017homozygousp.(glu87lys)variant pages 3-5)

---

## 10. Diagnostics

### Clinical and biochemical evaluation

MMDS5 should be considered in an infant or young child with progressive developmental failure/regression, spasticity, seizures or nystagmus, symmetric leukodystrophy, and biochemical evidence of mitochondrial dysfunction. Plasma lactate, pyruvate, CK, plasma/urine amino acids including glycine, urine organic acids, blood gas/bicarbonate, liver/renal studies, glucose, and nutritional indices are reasonable initial tests. Normal metabolic studies do not exclude the disorder. (mp1993isca1relatedmultiplemitochondrialc pages 1-3, lebigot2021areviewof pages 18-20)

Brain MRI with diffusion-sensitive sequences and **MR spectroscopy** is highly informative but nonspecific. EEG, ophthalmologic examination, audiology/brainstem responses, swallowing assessment, respiratory evaluation, and urodynamics should be directed by the phenotype. Respiratory-chain enzyme assays, oxygen-consumption/ATP studies, and immunoblotting of lipoylated PDH-E2/KGDH-E2 in fibroblasts or muscle can support pathogenicity, but sensitivity and specimen dependence are unknown. (torraco2018isca1mutationin pages 1-2, mp1993isca1relatedmultiplemitochondrialc pages 3-6, lebigot2020expandingthephenotype pages 3-4)

### Molecular confirmation

Diagnosis requires **biallelic pathogenic or likely pathogenic ISCA1 variants** in an appropriate phenotype. Preferred approaches are:

1. An ISCA1-containing mitochondrial-disease, leukodystrophy, or neurodegeneration panel.
2. Trio WES, ideally with mtDNA analysis; WGS is reasonable when WES is negative.
3. Single-gene ISCA1 sequencing followed by deletion/duplication analysis when suspicion is high.
4. Targeted p.Glu87Lys testing in an appropriate southwestern Indian founder context, followed by full sequencing if negative. (mp1993isca1relatedmultiplemitochondrialc pages 1-3, mp1993isca1relatedmultiplemitochondriald pages 1-3)

The curated summary reported sequence-level variants in 5/5 probands and targeted p.Glu87Lys detection in 4/5, but these tiny numbers are not clinical-sensitivity estimates. No diagnostic copy-number variant had been reported. CMA, karyotyping, FISH, repeat-expansion testing, and mtDNA-only testing are not first-line MMDS5 assays unless another diagnosis is suspected. RNA sequencing may help resolve a splice variant, but no MMDS5-specific clinical RNA-seq evidence was found. (mp1993isca1relatedmultiplemitochondriala pages 1-3, mp1993isca1relatedmultiplemitochondrialc pages 1-3)

### Differential diagnosis

Key differentials include MMDS1–4 and other Fe–S disorders (**NFU1, BOLA3, IBA57, ISCA2**), PMPCB-related MMDS, primary pyruvate-dehydrogenase/lipoate disorders, mitochondrial respiratory-chain disease, Leigh syndrome, nonketotic hyperglycinemia, POLG-related disease, and other infantile leukodystrophies. Molecular testing is essential because lactate, glycine, and MRI findings are not MMDS5-specific. (shukla2017homozygousp.(glu87lys)variant pages 1-2, lebigot2021areviewof pages 18-20)

No consensus clinical diagnostic criteria or population newborn-screening program exists. Once familial variants are known, carrier testing, cascade testing, prenatal diagnosis, and preimplantation genetic testing are technically possible. (mp1993isca1relatedmultiplemitochondriald pages 1-3, mp1993isca1relatedmultiplemitochondrialb pages 10-13)

---

## 11. Outcome and prognosis

Five of seven patients in the 2021 synthesis died between 11 months and 11 years. The four p.Glu87Lys children in the initial report died at 11 months to five years; the p.Val10Gly patient survived to 11 years and died during pneumonia. No five- or ten-year survival curve, mortality rate, or genotype-adjusted life expectancy is available. (shukla2017homozygousp.(glu87lys)variant pages 1-2, lebigot2021areviewof pages 17-18)

Major morbidity includes profound neurodevelopmental disability, spasticity, seizures, ataxia, visual/auditory impairment, feeding failure, aspiration risk, loss of mobility, neurogenic bladder, and respiratory vulnerability. Prognostic factors are not validated. Later onset and residual protein function may plausibly predict a milder course, as suggested by p.Tyr101Cys and p.Val10Gly cases, but the evidence is too small for a firm genotype–phenotype model. No prognostic biomarker has been validated. (lebigot2020expandingthephenotype pages 1-2, torraco2018isca1mutationin pages 1-2)

---

## 12. Treatment

There is **no established disease-modifying pharmacotherapy**, gene therapy, cell therapy, RNA therapy, or approved ISCA1-targeted treatment. No MMDS5-specific interventional ClinicalTrials.gov record or NCT identifier was found in the searches performed for this report. Wild-type ISCA1 complementation rescued cellular defects experimentally, but this is proof of mechanism rather than clinical gene therapy. (torraco2018isca1mutationin pages 1-2, mp1993isca1relatedmultiplemitochondriala pages 10-13)

Treatment is multidisciplinary and manifestation-directed:

* Standard antiseizure medication — suggested NCIt concept: **Anticonvulsant Agent**.
* Physical/occupational rehabilitation, stretching, positioning, orthoses, and mobility/communication devices — **Physical Therapy**, **Occupational Therapy**.
* Baclofen or botulinum toxin type A for problematic spasticity — **Baclofen**, **Botulinum Toxin Type A**.
* Dietitian and swallowing-team management; nasogastric or gastrostomy feeding when oral intake is unsafe — **Nutritional Support**, **Gastrostomy**.
* Ophthalmologic and hearing interventions, including hearing aids where appropriate.
* Respiratory surveillance, aspiration prevention, constipation management, social work, home nursing, respite, and palliative care. (mp1993isca1relatedmultiplemitochondriald pages 8-10, mp1993isca1relatedmultiplemitochondriala pages 8-10)

Observed care in the p.Val10Gly patient included bicarbonate for metabolic acidosis and Nissen fundoplication with gastrostomy for progressive dysphagia. No response rate or adverse-event estimate is available. No disease-specific pharmacogenomic guidance exists. (torraco2018isca1mutationin pages 1-2)

---

## 13. Prevention

Primary prevention through lifestyle or exposure modification is not possible because MMDS5 is a recessive genetic disorder. Reproductive prevention options, after molecular confirmation, include carrier/cascade testing, partner testing, prenatal diagnosis, and PGT-M. Preconception genetic counseling should explain the 25% recurrence risk for carrier couples. (mp1993isca1relatedmultiplemitochondriala pages 10-13, mp1993isca1relatedmultiplemitochondrialb pages 10-13)

Secondary prevention consists of early molecular diagnosis and anticipatory assessment of seizures, vision, hearing, swallowing, nutrition, aspiration, respiratory function, development, growth, and family support. Tertiary prevention includes safe feeding, gastrostomy when indicated, mobility/positioning care, constipation prevention, respiratory monitoring, and timely palliative support. No MMDS5-specific vaccine, antimicrobial prophylaxis, antioxidant, vitamin, or “mitochondrial cocktail” has proven efficacy. Routine age-appropriate immunization is reasonable general care but is not disease-specific evidence. (mp1993isca1relatedmultiplemitochondriald pages 8-10, mp1993isca1relatedmultiplemitochondrialb pages 8-10)

---

## 14. Other species and natural disease

No naturally occurring ISCA1-related MMDS5 was identified in companion animals, livestock, or wildlife, and there is no zoonotic or transmissible component. The experimentally studied ortholog is rat **Isca1** in **Rattus norvegicus (NCBI Taxonomy 10116)**. Conservation of the Fe–S pathway and embryonic lethality after complete knockout indicate strong evolutionary constraint. Veterinary breed associations and VBO terms are not applicable based on current evidence. (yang2019knockoutofisca1 pages 1-2, yang2019knockoutofisca1 pages 2-5)

---

## 15. Model organisms

### Cellular models

ISCA1 RNAi in HeLa cells reproduces selective mitochondrial [4Fe–4S]-protein defects. Wild-type complementation restores respiratory and lipoylation phenotypes more effectively than p.Val10Gly. These systems are useful for variant interpretation and pathway dissection but lack neural tissue architecture and organismal disease progression. (torraco2018isca1mutationin pages 4-5, torraco2018isca1mutationin pages 1-2)

### Constitutive rat knockout

CRISPR/Cas9 replacement of Isca1 exon 1 produced a whole-body knockout. Homozygous embryos developed abnormally by embryonic day 8.5 and died early, demonstrating an essential developmental role but preventing postnatal MMDS5 modeling. No homozygotes were recovered among 83 litters in the reported breeding analysis. (yang2019knockoutofisca1 pages 1-2, yang2019knockoutofisca1 pages 2-5)

### Myocardium-specific rat

An α-MHC-Cre conditional deletion achieved 84.26% myocardial knockout. Homozygous pups developed mitochondrial injury, disturbed iron metabolism, reduced ATP, cardiomyocyte oncosis, severe heart failure, and death by postnatal day 10. STEAP3 was proposed as an ISCA1-interacting iron-metabolism factor. The model is useful for tissue-specific bioenergetics and target discovery, but its dramatic cardiac phenotype should not be generalized to human MMDS5 without clinical corroboration. (ling2022myocardiumspecificisca1knockout pages 5-9, ling2021isca1deficiencyinduces pages 12-15, ling2022myocardiumspecificisca1knockout pages 1-2)

### 2023 neuron-specific rat

The Isca1^flox/flox–NeuN-Cre rat developed developmental delay, dyskinesia, epilepsy, memory impairment, neuronal loss/oncosis, fewer Nissl bodies and dendritic spines, mitochondrial fragmentation and cristae fracture, reduced respiratory-chain proteins, and ATP depletion. Survival to approximately eight weeks provides a therapeutic-study window that the constitutive knockout lacks. Limitations include complete neuronal deletion rather than a patient-specific hypomorphic allele, a shorter lifespan than the longest-surviving patients, and inability of severely weak animals to complete the Morris water maze. (sheng2023aneuron‐specificisca1 pages 2-3, sheng2023aneuron‐specificisca1 pages 1-2)

---

## Key primary-source abstract quotations

* Shukla et al., published online **March 30, 2017**, DOI: https://doi.org/10.1038/jhg.2017.35: “**We report on two unrelated families, with two affected children each with early onset neurological deterioration, seizures, extensive white matter abnormalities, cortical migrational abnormalities, lactic acidosis and early demise.**” The abstract further states that exome sequencing identified homozygous **c.259G>A [p.(Glu87Lys)]** and that the shared homozygous region suggested a founder effect. (shukla2017homozygousp.(glu87lys)variant pages 1-2)
* Lebigot et al., online **February 21, 2020**, DOI: https://doi.org/10.1016/j.mito.2020.02.008: the report describes a patient with p.(Tyr101Cys) who “**initially presented a psychomotor regression with loss of gait and language**”; functional evidence showed impaired lipoic-acid synthesis, reduced complexes I/II, and an unstable mutant Fe–S cluster. (lebigot2020expandingthephenotype pages 1-2)
* Sheng et al., **April 2023**, DOI: https://doi.org/10.1002/ame2.12318: “**This study established a rat model simulating MMDS5 disease in the nervous system to investigate its pathological features and neuronal death.**” (sheng2023aneuron‐specificisca1 pages 1-2)

## Overall assessment

Authoritative interpretation is constrained more by scarcity of patients than by uncertainty over the core cause. The evidence strongly supports biallelic **ISCA1** dysfunction causing a selective late mitochondrial [4Fe–4S]-maturation disorder with secondary OXPHOS and lipoylation failure. The largest immediate knowledge gaps are prospective natural history, standardized phenotype frequencies, contemporary variant curation, patient-centered outcomes, disease-specific metabolomic/proteomic signatures, and development of an allele-faithful preclinical model and targeted therapy.

References

1. (lebigot2021areviewof pages 17-18): Elise Lebigot, Manuel Schiff, and Marie-Pierre Golinelli-Cohen. A review of multiple mitochondrial dysfunction syndromes, syndromes associated with defective fe-s protein maturation. Aug 2021. URL: https://doi.org/10.3390/biomedicines9080989, doi:10.3390/biomedicines9080989. This article has 35 citations.

2. (sheng2023aneuron‐specificisca1 pages 1-2): Hanxuan Sheng, Dan Lu, Xiaolong Qi, Yahao Ling, Jing Li, Xu Zhang, Wei Dong, Wei Chen, Shan Gao, Xiang Gao, Li Zhang, and Lianfeng Zhang. A neuron‐specific isca1 knockout rat developments multiple mitochondrial dysfunction syndromes. Animal Models and Experimental Medicine, 6:155-167, Apr 2023. URL: https://doi.org/10.1002/ame2.12318, doi:10.1002/ame2.12318. This article has 5 citations.

3. (mp1993isca1relatedmultiplemitochondriala pages 10-13): FJ MP and GM Mirzaa. Isca1-related multiple mitochondrial dysfunctions syndrome. Unknown journal, 1993.

4. (mp1993isca1relatedmultiplemitochondrialc pages 1-3): FJ MP and GM Mirzaa. Isca1-related multiple mitochondrial dysfunctions syndrome. Unknown journal, 1993.

5. (shukla2017homozygousp.(glu87lys)variant pages 1-2): Anju Shukla, Malavika Hebbar, Anshika Srivastava, Rajagopal Kadavigere, Priyanka Upadhyai, Anil Kanthi, Oliver Brandau, Stephanie Bielas, and Katta M Girisha. Homozygous p.(glu87lys) variant in isca1 is associated with a multiple mitochondrial dysfunctions syndrome. Mar 2017. URL: https://doi.org/10.1038/jhg.2017.35, doi:10.1038/jhg.2017.35. This article has 75 citations and is from a peer-reviewed journal.

6. (mp1993isca1relatedmultiplemitochondrialc pages 3-6): FJ MP and GM Mirzaa. Isca1-related multiple mitochondrial dysfunctions syndrome. Unknown journal, 1993.

7. (torraco2018isca1mutationin pages 1-2): Alessandra Torraco, Oliver Stehling, Claudia Stümpfig, Ralf Rösser, Domenico De Rasmo, Giuseppe Fiermonte, Daniela Verrigni, Teresa Rizza, Angelo Vozza, Michela Di Nottia, Daria Diodato, Diego Martinelli, Fiorella Piemonte, Carlo Dionisi-Vici, Enrico Bertini, Roland Lill, and Rosalba Carrozzo. Isca1 mutation in a patient with infantile-onset leukodystrophy causes defects in mitochondrial [4fe–4s] proteins. Human Molecular Genetics, 27(20):3650-3650, Aug 2018. URL: https://doi.org/10.1093/hmg/ddy273, doi:10.1093/hmg/ddy273. This article has 41 citations and is from a domain leading peer-reviewed journal.

8. (shukla2017homozygousp.(glu87lys)variant pages 3-5): Anju Shukla, Malavika Hebbar, Anshika Srivastava, Rajagopal Kadavigere, Priyanka Upadhyai, Anil Kanthi, Oliver Brandau, Stephanie Bielas, and Katta M Girisha. Homozygous p.(glu87lys) variant in isca1 is associated with a multiple mitochondrial dysfunctions syndrome. Mar 2017. URL: https://doi.org/10.1038/jhg.2017.35, doi:10.1038/jhg.2017.35. This article has 75 citations and is from a peer-reviewed journal.

9. (torraco2018isca1mutationin pages 3-4): Alessandra Torraco, Oliver Stehling, Claudia Stümpfig, Ralf Rösser, Domenico De Rasmo, Giuseppe Fiermonte, Daniela Verrigni, Teresa Rizza, Angelo Vozza, Michela Di Nottia, Daria Diodato, Diego Martinelli, Fiorella Piemonte, Carlo Dionisi-Vici, Enrico Bertini, Roland Lill, and Rosalba Carrozzo. Isca1 mutation in a patient with infantile-onset leukodystrophy causes defects in mitochondrial [4fe–4s] proteins. Human Molecular Genetics, 27(20):3650-3650, Aug 2018. URL: https://doi.org/10.1093/hmg/ddy273, doi:10.1093/hmg/ddy273. This article has 41 citations and is from a domain leading peer-reviewed journal.

10. (torraco2018isca1mutationin pages 2-3): Alessandra Torraco, Oliver Stehling, Claudia Stümpfig, Ralf Rösser, Domenico De Rasmo, Giuseppe Fiermonte, Daniela Verrigni, Teresa Rizza, Angelo Vozza, Michela Di Nottia, Daria Diodato, Diego Martinelli, Fiorella Piemonte, Carlo Dionisi-Vici, Enrico Bertini, Roland Lill, and Rosalba Carrozzo. Isca1 mutation in a patient with infantile-onset leukodystrophy causes defects in mitochondrial [4fe–4s] proteins. Human Molecular Genetics, 27(20):3650-3650, Aug 2018. URL: https://doi.org/10.1093/hmg/ddy273, doi:10.1093/hmg/ddy273. This article has 41 citations and is from a domain leading peer-reviewed journal.

11. (torraco2018isca1mutationin pages 8-9): Alessandra Torraco, Oliver Stehling, Claudia Stümpfig, Ralf Rösser, Domenico De Rasmo, Giuseppe Fiermonte, Daniela Verrigni, Teresa Rizza, Angelo Vozza, Michela Di Nottia, Daria Diodato, Diego Martinelli, Fiorella Piemonte, Carlo Dionisi-Vici, Enrico Bertini, Roland Lill, and Rosalba Carrozzo. Isca1 mutation in a patient with infantile-onset leukodystrophy causes defects in mitochondrial [4fe–4s] proteins. Human Molecular Genetics, 27(20):3650-3650, Aug 2018. URL: https://doi.org/10.1093/hmg/ddy273, doi:10.1093/hmg/ddy273. This article has 41 citations and is from a domain leading peer-reviewed journal.

12. (lebigot2020expandingthephenotype pages 1-2): E. Lebigot, M. Hully, L. Amazit, P. Gaignard, T. Michel, M. Rio, M. Lombès, P. Thérond, A. Boutron, and M.P. Golinelli-Cohen. Expanding the phenotype of mitochondrial disease: novel pathogenic variant in isca1 leading to instability of the iron-sulfur cluster in the protein. May 2020. URL: https://doi.org/10.1016/j.mito.2020.02.008, doi:10.1016/j.mito.2020.02.008. This article has 7 citations and is from a peer-reviewed journal.

13. (lebigot2020expandingthephenotype pages 3-4): E. Lebigot, M. Hully, L. Amazit, P. Gaignard, T. Michel, M. Rio, M. Lombès, P. Thérond, A. Boutron, and M.P. Golinelli-Cohen. Expanding the phenotype of mitochondrial disease: novel pathogenic variant in isca1 leading to instability of the iron-sulfur cluster in the protein. May 2020. URL: https://doi.org/10.1016/j.mito.2020.02.008, doi:10.1016/j.mito.2020.02.008. This article has 7 citations and is from a peer-reviewed journal.

14. (torraco2018isca1mutationin pages 4-5): Alessandra Torraco, Oliver Stehling, Claudia Stümpfig, Ralf Rösser, Domenico De Rasmo, Giuseppe Fiermonte, Daniela Verrigni, Teresa Rizza, Angelo Vozza, Michela Di Nottia, Daria Diodato, Diego Martinelli, Fiorella Piemonte, Carlo Dionisi-Vici, Enrico Bertini, Roland Lill, and Rosalba Carrozzo. Isca1 mutation in a patient with infantile-onset leukodystrophy causes defects in mitochondrial [4fe–4s] proteins. Human Molecular Genetics, 27(20):3650-3650, Aug 2018. URL: https://doi.org/10.1093/hmg/ddy273, doi:10.1093/hmg/ddy273. This article has 41 citations and is from a domain leading peer-reviewed journal.

15. (torraco2018isca1mutationin pages 12-13): Alessandra Torraco, Oliver Stehling, Claudia Stümpfig, Ralf Rösser, Domenico De Rasmo, Giuseppe Fiermonte, Daniela Verrigni, Teresa Rizza, Angelo Vozza, Michela Di Nottia, Daria Diodato, Diego Martinelli, Fiorella Piemonte, Carlo Dionisi-Vici, Enrico Bertini, Roland Lill, and Rosalba Carrozzo. Isca1 mutation in a patient with infantile-onset leukodystrophy causes defects in mitochondrial [4fe–4s] proteins. Human Molecular Genetics, 27(20):3650-3650, Aug 2018. URL: https://doi.org/10.1093/hmg/ddy273, doi:10.1093/hmg/ddy273. This article has 41 citations and is from a domain leading peer-reviewed journal.

16. (torraco2018isca1mutationin pages 6-7): Alessandra Torraco, Oliver Stehling, Claudia Stümpfig, Ralf Rösser, Domenico De Rasmo, Giuseppe Fiermonte, Daniela Verrigni, Teresa Rizza, Angelo Vozza, Michela Di Nottia, Daria Diodato, Diego Martinelli, Fiorella Piemonte, Carlo Dionisi-Vici, Enrico Bertini, Roland Lill, and Rosalba Carrozzo. Isca1 mutation in a patient with infantile-onset leukodystrophy causes defects in mitochondrial [4fe–4s] proteins. Human Molecular Genetics, 27(20):3650-3650, Aug 2018. URL: https://doi.org/10.1093/hmg/ddy273, doi:10.1093/hmg/ddy273. This article has 41 citations and is from a domain leading peer-reviewed journal.

17. (mp1993isca1relatedmultiplemitochondriala pages 1-3): FJ MP and GM Mirzaa. Isca1-related multiple mitochondrial dysfunctions syndrome. Unknown journal, 1993.

18. (mp1993isca1relatedmultiplemitochondriald pages 1-3): FJ MP and GM Mirzaa. Isca1-related multiple mitochondrial dysfunctions syndrome. Unknown journal, 1993.

19. (mp1993isca1relatedmultiplemitochondriald pages 8-10): FJ MP and GM Mirzaa. Isca1-related multiple mitochondrial dysfunctions syndrome. Unknown journal, 1993.

20. (yang2019knockoutofisca1 pages 1-2): Xinlan Yang, Dan Lu, Xu Zhang, Wei Chen, Shan Gao, Wei Dong, Yuanwu Ma, and Lianfeng Zhang. Knockout of isca1 causes early embryonic death in rats. Animal Models and Experimental Medicine, 2:18-24, Mar 2019. URL: https://doi.org/10.1002/ame2.12059, doi:10.1002/ame2.12059. This article has 15 citations.

21. (yang2019knockoutofisca1 pages 2-5): Xinlan Yang, Dan Lu, Xu Zhang, Wei Chen, Shan Gao, Wei Dong, Yuanwu Ma, and Lianfeng Zhang. Knockout of isca1 causes early embryonic death in rats. Animal Models and Experimental Medicine, 2:18-24, Mar 2019. URL: https://doi.org/10.1002/ame2.12059, doi:10.1002/ame2.12059. This article has 15 citations.

22. (ling2022myocardiumspecificisca1knockout pages 5-9): Yahao Ling, Xinlan Yang, Xu Zhang, Feifei Guan, Xiaolong Qi, Wei Dong, Mengdi Liu, Jiaxin Ma, Xiaoyu Jiang, Kai Gao, Jing Li, Wei Chen, Shan Gao, Xiang Gao, Shuo Pan, Jizheng Wang, Yuanwu Ma, Dan Lu, and Lianfeng Zhang. Myocardium-specific isca1 knockout causes iron metabolism disorder and myocardial oncosis in rat. May 2022. URL: https://doi.org/10.1016/j.lfs.2022.120485, doi:10.1016/j.lfs.2022.120485. This article has 10 citations and is from a peer-reviewed journal.

23. (ling2021isca1deficiencyinduces pages 12-15): Yahao Ling, Xinlan Yang, Xu Zhang, Feifei Guan, Xiaolong Qi, Wei Dong, Mengdi Liu, Jiaxin Ma, Xiaoyu Jiang, Kai Gao, Jing Li, Wei Chen, Shan Gao, Xiang Gao, Shuo Pan, Yuanwu Ma, Jizheng Wang, Dan Lu, and lianfeng zhang. Isca1 deficiency induces iron metabolism disorder and myocardial oncosis in rat. ArXiv, Jul 2021. URL: https://doi.org/10.21203/rs.3.rs-648138/v1, doi:10.21203/rs.3.rs-648138/v1. This article has 0 citations.

24. (ling2022myocardiumspecificisca1knockout pages 1-2): Yahao Ling, Xinlan Yang, Xu Zhang, Feifei Guan, Xiaolong Qi, Wei Dong, Mengdi Liu, Jiaxin Ma, Xiaoyu Jiang, Kai Gao, Jing Li, Wei Chen, Shan Gao, Xiang Gao, Shuo Pan, Jizheng Wang, Yuanwu Ma, Dan Lu, and Lianfeng Zhang. Myocardium-specific isca1 knockout causes iron metabolism disorder and myocardial oncosis in rat. May 2022. URL: https://doi.org/10.1016/j.lfs.2022.120485, doi:10.1016/j.lfs.2022.120485. This article has 10 citations and is from a peer-reviewed journal.

25. (sheng2023aneuron‐specificisca1 pages 2-3): Hanxuan Sheng, Dan Lu, Xiaolong Qi, Yahao Ling, Jing Li, Xu Zhang, Wei Dong, Wei Chen, Shan Gao, Xiang Gao, Li Zhang, and Lianfeng Zhang. A neuron‐specific isca1 knockout rat developments multiple mitochondrial dysfunction syndromes. Animal Models and Experimental Medicine, 6:155-167, Apr 2023. URL: https://doi.org/10.1002/ame2.12318, doi:10.1002/ame2.12318. This article has 5 citations.

26. (mp1993isca1relatedmultiplemitochondrialb pages 10-13): FJ MP and GM Mirzaa. Isca1-related multiple mitochondrial dysfunctions syndrome. Unknown journal, 1993.

27. (mp1993isca1relatedmultiplemitochondrialb pages 8-10): FJ MP and GM Mirzaa. Isca1-related multiple mitochondrial dysfunctions syndrome. Unknown journal, 1993.

28. (mp1993isca1relatedmultiplemitochondriald pages 10-13): FJ MP and GM Mirzaa. Isca1-related multiple mitochondrial dysfunctions syndrome. Unknown journal, 1993.

29. (lebigot2021areviewof pages 18-20): Elise Lebigot, Manuel Schiff, and Marie-Pierre Golinelli-Cohen. A review of multiple mitochondrial dysfunction syndromes, syndromes associated with defective fe-s protein maturation. Aug 2021. URL: https://doi.org/10.3390/biomedicines9080989, doi:10.3390/biomedicines9080989. This article has 35 citations.

30. (mp1993isca1relatedmultiplemitochondriala pages 8-10): FJ MP and GM Mirzaa. Isca1-related multiple mitochondrial dysfunctions syndrome. Unknown journal, 1993.

## Artifacts

- [Edison artifact artifact-00](Multiple_Mitochondrial_Dysfunctions_Syndrome_5-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0033282` (2 mentions) - the report calls it "if available"; MONDO calls it **multiple mitochondrial dysfunctions syndrome 5**