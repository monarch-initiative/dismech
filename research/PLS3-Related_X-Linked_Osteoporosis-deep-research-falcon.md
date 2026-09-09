---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T11:51:51.522621'
end_time: '2026-09-05T12:00:28.367656'
duration_seconds: 516.85
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: PLS3-Related X-Linked Osteoporosis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 16
  verified: 16
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PLS3-Related_X-Linked_Osteoporosis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PLS3-Related X-Linked Osteoporosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PLS3-Related X-Linked Osteoporosis** covering all of the
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
- **Disease Name:** PLS3-Related X-Linked Osteoporosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PLS3-Related X-Linked Osteoporosis** covering all of the
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


# PLS3-Related X-Linked Osteoporosis: Disease-Characteristics Research Report

## Executive summary

PLS3-related X-linked osteoporosis is a rare, usually childhood-onset Mendelian bone-fragility disorder caused principally by germline loss-of-function variants in **PLS3**, which encodes the calcium-regulated F-actin-bundling protein plastin-3/T-plastin. Hemizygous males typically develop very low bone mineral density (BMD), recurrent low-trauma long-bone fractures, and vertebral compression fractures; heterozygous females range from clinically unaffected to early-onset or postmenopausal osteoporosis. Unlike classical collagen-related osteogenesis imperfecta (OI), blue sclerae, dentinogenesis imperfecta, and generalized joint hypermobility are usually absent. The best-supported mechanism is a multicellular defect in cytoskeletal organization, mechanosensing, and mineralization involving osteoblasts and osteocytes, with an additional—but not independently sufficient—osteoclast phenotype. No curative or PLS3-specific therapy exists; treatment evidence consists mainly of small uncontrolled series using bisphosphonates or teriparatide.

The following table provides a compact curation summary; the narrative sections provide qualification and evidence details.

| Domain | Curated finding | Evidence type/strength | Suggested ontology terms |
|---|---|---|---|
| Identity and inheritance | Rare Mendelian skeletal-fragility disorder caused by germline **PLS3** variants; X-linked inheritance produces predominantly severe disease in hemizygous males and variable expression in heterozygous females. The 2024 series comprised **five families and ten mutation-positive individuals**; all five index cases were male. (costa2024pls3mutationsin pages 2-4, costa2024pls3mutationsin pages 1-2) | Strong human familial segregation evidence; landmark and replicated family studies | **HP:0000939** osteoporosis; X-linked inheritance; Mendelian disease |
| Causal gene and protein | **PLS3** encodes plastin-3/T-plastin, a calcium-sensitive F-actin-binding and actin-bundling protein. Pathogenic alleles include nonsense, frameshift, splice, exon-level, and whole-gene deletions; loss of function is the principal established mechanism, although function-altering missense variants occur. (dijk2013pls3mutationsin pages 6-6, costa2024pls3mutationsin pages 11-12, chin2023theactinbundlingprotein pages 1-2) | Strong human genetic evidence plus cellular and animal functional evidence | PLS3; plastin-3; GO: actin filament binding; actin filament bundle assembly; calcium-ion-dependent protein regulation |
| Core phenotypes | Recurrent low-trauma peripheral/long-bone fractures, vertebral compression fractures, low BMD, bone pain, and sometimes kyphosis, scoliosis, or thoracic deformity. Lumbar-spine BMD Z-scores can be extremely low—approximately **−5** in a severely affected child. Classic collagen-related OI findings such as blue sclerae, dentinogenesis imperfecta, and generalized joint hyperlaxity are often absent, although occasional extraskeletal findings are reported. (costa2024pls3mutationsin pages 11-12, costa2024pls3mutationsin pages 1-2) | Strong recurring phenotype across small human cohorts; exact frequencies remain uncertain | **HP:0000939** osteoporosis; **HP:0002757** recurrent fractures; **HP:0002953** vertebral compression fractures; **HP:0004349** reduced bone mineral density |
| Onset and course | Usually chronic, lifelong, childhood-onset bone fragility. In the five-family 2024 cohort, first clinical fracture occurred from **1.5–13 years**. Fractures may accumulate through childhood and adulthood; severity and female-carrier manifestations are variable. (costa2024pls3mutationsin pages 11-12, costa2024pls3mutationsin pages 1-2) | Moderate-to-strong human natural-history evidence from case series; no large prospective cohort | Childhood onset; progressive bone fragility; variable expressivity |
| Histopathology and material properties | Iliac-crest biopsies show low-turnover osteoporosis, markedly reduced trabecular volume and bone formation/resorption; one series reported about **80% less osteoblast-covered** and **90% less osteoclast-covered** trabecular surface. Increased matrix mineralization/hypermineralization can occur. (balasubramanian2018novelpls3variants pages 11-14, balasubramanian2018novelpls3variants pages 1-5) | Direct human biopsy evidence, but very small samples | Low bone turnover; reduced trabecular bone volume; abnormal bone mineralization |
| Mechanism | PLS3 dysfunction impairs F-actin bundling and focal-adhesion responses to extracellular-matrix stiffness, leading to defective osteoblast mechanosensing and matrix mineralization. Altered osteocyte signaling and osteoclast podosome/NF-κB–NFATC1 regulation may contribute. Osteoclast-specific knockout increases resorption in vitro but does **not** cause osteoporosis in vivo, indicating that osteoclast dysfunction alone is insufficient and that disease is multicellular. (neugebauer2018plastin3influences pages 3-4, chin2023theactinbundlingprotein pages 1-2, maus2024osteoclastspecificplastin3 pages 1-2) | Strong mechanistic evidence in cells and animals; the complete human causal pathway remains partly inferred | GO: actin cytoskeleton organization; mechanosensory behavior; focal-adhesion organization; biomineral tissue development; bone remodeling; Wnt signaling |
| Anatomy, cells, and compartments | Primary involvement is generalized cortical and trabecular bone, especially vertebral bodies and long bones. Relevant cells are **osteoblasts, osteocytes, and osteoclasts**. Relevant subcellular sites include F-actin bundles, focal adhesions, osteocyte dendritic processes, osteoclast podosomes/sealing zones, cytoplasm, and plasma-membrane-associated adhesion structures. (neugebauer2018plastin3influences pages 3-4, chin2023theactinbundlingprotein pages 1-2, maus2024osteoclastspecificplastin3 pages 1-2) | Human imaging/biopsy supported by cellular localization and animal models | UBERON: bone; skeleton; vertebral column; long bone; CL: osteoblast; osteocyte; osteoclast; GO: actin cytoskeleton; focal adhesion; podosome |
| Diagnostics | Suspect in unexplained childhood or young-adult osteoporosis, recurrent low-trauma fractures, vertebral compression, very low BMD, or an X-linked pedigree. Evaluation includes fracture/family history, DXA, lateral spine imaging or vertebral-fracture assessment, skeletal radiographs, and laboratory exclusion of secondary causes. Confirm with a bone-fragility multigene panel including **PLS3**, or exome/genome sequencing with copy-number analysis; test and clinically assess relatives. Bone biopsy is optional when turnover or mineralization defects remain unclear. (balasubramanian2018novelpls3variants pages 11-14, balasubramanian2018novelpls3variants pages 1-5, costa2024pls3mutationsin pages 1-2) | Expert diagnostic synthesis plus human case-series evidence; no disease-specific consensus criteria | Genetic testing; DXA; radiography; vertebral-fracture assessment; cascade testing |
| Treatment | No PLS3-specific approved therapy or curative treatment exists. Calcium/vitamin-D sufficiency, fracture care, pain management, physiotherapy, and specialist-guided anti-osteoporosis therapy are used. In 2024, four patients treated with pamidronate or zoledronate showed lumbar-spine BMD improvement and vertebral reshaping over **10 months–2 years**. One adult receiving teriparatide plus calcium/vitamin D had femoral-neck and total-hip BMD gains of **2.4% and 4.1% at 10 months**, without new fractures or reported adverse events. Evidence remains uncontrolled, and prolonged bisphosphonate exposure requires caution. No registered disease-specific interventional trial was found. (costa2024pls3mutationsin pages 2-4, costa2024pls3mutationsin pages 1-2) | Very low-to-low certainty: case reports/series and animal treatment studies; no disease-specific randomized trial | NCIT: bisphosphonate therapy; pamidronate; zoledronic acid; teriparatide therapy; calcium supplementation; vitamin D supplementation; physical therapy |
| Prevention | The genotype cannot presently be prevented after conception. Secondary/tertiary prevention includes early molecular diagnosis, family cascade testing, adequate calcium/vitamin D, safe weight-bearing activity, fall and high-impact-trauma reduction, avoidance of smoking/excess alcohol and unnecessary bone-toxic drugs, surveillance for silent vertebral fractures, and timely therapy. Genetic counseling may include prenatal or preimplantation testing after identification of a familial pathogenic variant. | General bone-health and genetic-counseling practice; little PLS3-specific comparative evidence | Genetic counseling; cascade screening; fracture prevention; fall prevention; prenatal genetic testing |
| Epidemiology | Disease-specific prevalence, incidence, carrier frequency, and population sex ratio are **unknown**; reported families are geographically diverse and the disorder is probably substantially underdiagnosed. No validated founder effect or population-specific enrichment is established. (dijk2013pls3mutationsin pages 6-6, costa2024pls3mutationsin pages 1-2) | Sparse ascertainment-based family literature; no population registry estimate | Rare disease; orphan disease; epidemiology unknown |
| Models | **Zebrafish:** pls3 knockdown causes craniofacial/axial skeletal abnormalities rescued by human PLS3 mRNA or ACTN1/ACTN4. **Mouse:** ubiquitous loss causes cortical/trabecular osteoporosis, whereas osteoclast-specific loss does not; Pls3 deficiency particularly impairs cortical acquisition. **Rat:** patient-relevant **PLS3 E10–16 deletion** causes reduced cortical thickness, mineral apposition and bone strength; alendronate and teriparatide improve microarchitecture, with teriparatide improving strength. **Cells:** PLS3-depleted MC3T3-E1 osteoblasts fail to adapt to matrix stiffness and mineralize normally; MLO-Y4 RNA-seq found 259 upregulated and 368 downregulated transcripts with Wnt/Th17-associated enrichment. (dijk2013pls3mutationsin pages 6-6, hu2023impairedbonestrength pages 7-8, chin2023theactinbundlingprotein pages 1-2, maus2024osteoclastspecificplastin3 pages 1-2, n2024functionalinsightsin pages 10-12) | Strong cross-model functional support; model-specific differences limit direct clinical translation | Danio rerio; Mus musculus; Rattus norvegicus; osteoblast cell model; osteocyte-like cell model; knockout; knockdown; rescue model |


*Table: Compact disease-knowledge table integrating human clinical findings, mechanisms, diagnostics, management, and model evidence for PLS3-related X-linked osteoporosis. It highlights quantitative cohort data and explicitly identifies major evidence gaps.*

## 1. Disease information

### Definition and nomenclature

The disease is a monogenic primary osteoporosis characterized by reduced bone mass and bone strength, vertebral and peripheral fractures, and onset commonly during childhood. The landmark report identified pathogenic PLS3 variants in five families with X-linked osteoporosis; zebrafish rescue experiments supplied initial functional support. The same study also associated a rare PLS3 allele with approximately twofold higher fracture risk in elderly heterozygous women, suggesting that PLS3 variation can influence both monogenic and complex osteoporosis. (dijk2013pls3mutationsin pages 6-6)

**Preferred name:** PLS3-related X-linked osteoporosis.

**Synonyms:**

- X-linked osteoporosis with fractures
- PLS3-related osteoporosis
- Plastin-3 deficiency/PLS3 deficiency
- X-linked early-onset osteoporosis
- PLS3-related bone fragility
- PLS3-related X-linked osteogenesis imperfecta or X-linked OI—used by some authors, although many affected individuals lack classic OI extraskeletal features
- Idiopathic juvenile osteoporosis, when used as the historical presenting diagnosis rather than a molecularly specific synonym (balasubramanian2018novelpls3variants pages 1-5)

### Identifiers

- **OMIM phenotype:** *Osteoporosis, X-linked*, **OMIM 300910**; **PLS3 gene: OMIM 300131**. These identifiers should be version-checked before automated ingestion.
- **MONDO:** a distinct PLS3/X-linked osteoporosis concept may be represented through OMIM cross-references, but a stable disease-specific MONDO identifier could not be verified from the retrieved primary literature. Do not assign one automatically without checking the current MONDO release.
- **Orphanet:** no verified disease-specific ORPHA number was recovered.
- **MeSH:** no dedicated PLS3-disease heading; use broader headings such as *Osteoporosis*, *Osteoporosis, Juvenile*, *Fractures, Bone*, and *Genetic Diseases, X-Linked*.
- **ICD-10/ICD-11:** no PLS3-specific code. Coding generally falls under osteoporosis with/without pathological fracture or a genetic skeletal disorder; the exact code depends on age, fracture status, and local coding rules.

The evidence is predominantly **aggregated disease-level literature assembled from deeply phenotyped individual families**, not population EHR data. The 2024 series comprised five families and ten variant-positive individuals from Sweden, Greece, Germany, and Portugal. (costa2024pls3mutationsin pages 2-4, costa2024pls3mutationsin pages 1-2)

## 2. Etiology, risk, protective factors, and environment

### Causal factor

The primary cause is a **germline pathogenic PLS3 variant on Xq23**. Most well-supported alleles abolish or markedly impair protein function: nonsense, frameshift, canonical splice, exon-level deletion, multi-exon deletion, and whole-gene deletion variants have been reported. Pathogenic or candidate function-altering missense alleles also occur. The 2024 cohort contained three stop-gain variants and two partial/whole-gene deletions; four of five family variants were maternally inherited. (costa2024pls3mutationsin pages 11-12, costa2024pls3mutationsin pages 1-2)

### Genetic risk and modifiers

- Hemizygosity is the major severity determinant: males have only one PLS3 allele and generally show earlier, more severe disease.
- Female risk is variable, plausibly reflecting X-inactivation/escape, age, hormonal state, and background skeletal risk; affected females can nevertheless be severe. In one childhood cohort, a girl with a de novo missense variant had multiple long-bone and vertebral fractures and BMD Z-score −6.6 at age six. (balasubramanian2018novelpls3variants pages 1-5)
- A severely affected eight-year-old with near-generalized vertebral compression and lumbar-spine Z-score about −5 also carried an **LRP5** variant of uncertain significance. This raises—but does not prove—a modifying or digenic effect. (costa2024pls3mutationsin pages 11-12)
- No validated protective PLS3 allele, modifier gene, polygenic score, founder mutation, or population-specific susceptibility locus has been established.

### Environmental and lifestyle factors

No infectious, toxic, radiation, pollution, or occupational cause is known. Calcium or vitamin-D deficiency, undernutrition, immobility, smoking, excess alcohol, glucocorticoids, and other bone-toxic medicines may compound skeletal fragility, but this is extrapolated from general osteoporosis rather than demonstrated PLS3-specific gene–environment interaction. Secondary causes—including celiac disease, inflammatory bowel disease, eating disorders, and calcium/vitamin-D deficiency—should be excluded because they can mimic or worsen the phenotype. (balasubramanian2018novelpls3variants pages 11-14)

Adequate calcium/vitamin D and safe mechanical loading are biologically reasonable protective measures, but neither prevents the genetic lesion nor has a quantified PLS3-specific effect. In one family report, correction of hypovitaminosis D coincided with short-term BMD improvement, but the uncontrolled observation cannot establish disease modification. (brlek2021xlinkedosteogenesisimperfecta pages 10-11)

## 3. Phenotypes

### Core skeletal phenotype

| Phenotype | Characterization | Suggested HPO term |
|---|---|---|
| Osteoporosis | Usually generalized, severe, and early onset; variable among females | Osteoporosis, **HP:0000939** |
| Reduced BMD | Lumbar spine is consistently affected; reported Z-scores extend to approximately −5 or lower in severe children | Reduced bone mineral density, **HP:0004349** |
| Recurrent fractures | Low-trauma peripheral and long-bone fractures, including radius, ulna, humerus, femur, tibia, metacarpals, and hip | Recurrent fractures, **HP:0002757**; Pathologic fracture, **HP:0002756** |
| Vertebral compression | Multiple thoracic/lumbar compression or wedge fractures; may be clinically silent or cause pain and deformity | Vertebral compression fracture, **HP:0002953** |
| Back/bone pain | Often associated with vertebral injury and accumulated fractures | Bone pain, **HP:0002653**; Back pain, **HP:0003418** |
| Kyphosis/scoliosis/thoracic deformity | Secondary to vertebral collapse or severe skeletal fragility; not universal | Kyphosis, **HP:0002808**; Scoliosis, **HP:0002650**; Pectus excavatum, **HP:0000767** |
| Abnormal bone microarchitecture | Reduced trabecular volume, cortical thinning, and hypermineralized matrix in selected biopsies/models | Abnormality of bone structure, **HP:0011842** |

In the 2024 five-family study, all index patients were hemizygous males with long-bone and vertebral compression fractures and low lumbar-spine BMD; first clinical fracture occurred at **1.5–13 years**. One eight-year-old had eight low-energy fractures, vertebral wedging, and lumbar-spine Z-score −1.6; a different severe child had compression of almost every vertebral body and Z-score near −5. (costa2024pls3mutationsin pages 11-12, costa2024pls3mutationsin pages 2-4, costa2024pls3mutationsin pages 1-2)

Human biopsy evidence supports a predominantly **low-turnover** phenotype. In a small series, trabecular volume was markedly reduced, while osteoblast-covered and osteoclast-covered trabecular surfaces were approximately 80% and 90% lower, respectively; cortical and trabecular matrix was hypermineralized. (balasubramanian2018novelpls3variants pages 11-14)

### Variable or occasional findings

Pectus deformity, pes planus, broad/short digits, syndactyly, kyphoscoliosis, poor jaw trabeculation, facial or palate abnormalities, and joint symptoms have been reported, but their disease specificity and frequencies are unclear. Autism in one patient and occasional patellar subluxation in another should not presently be treated as core PLS3 phenotypes. (brlek2021xlinkedosteogenesisimperfecta pages 10-11, balasubramanian2018novelpls3variants pages 1-5, costa2024pls3mutationsin pages 2-4)

Blue sclerae, dentinogenesis imperfecta, hearing loss, and generalized joint hyperlaxity are usually absent, helping distinguish this condition from classical COL1A1/COL1A2-related OI, although isolated reports mean they are not absolute exclusions. (brlek2021xlinkedosteogenesisimperfecta pages 10-11, costa2024pls3mutationsin pages 1-2)

### Quality of life

No validated PLS3-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life dataset was found. Recurrent fractures, pain, spinal deformity, surgery, mobility restriction, and fear of injury are expected to impair school/work participation and physical functioning, but disease-specific effect sizes are unavailable.

## 4. Genetic and molecular information

**Causal gene:** **PLS3** (plastin 3/T-plastin), Xq23; HGNC symbol **PLS3**. The protein contains calcium-regulatory EF-hand regions and two actin-binding domains. It bundles F-actin and participates in focal adhesions, cell spreading, vesicle trafficking, and mechanotransduction. (chin2023theactinbundlingprotein pages 1-2, maus2024osteoclastspecificplastin3 pages 2-3)

Examples of reported alleles include **c.1543del (p.Asp515Metfs*11)**, **c.827G>A (p.Trp276\*)**, **c.994_995delGA (p.Asp332\*)**, **c.1765del**, and exon 10–16 or larger deletions. A candidate missense allele **c.685G>A (p.Gly229Arg)** remains less secure and was reported with computational pathogenicity evidence rather than definitive functional validation. (brlek2021xlinkedosteogenesisimperfecta pages 10-11, balasubramanian2018novelpls3variants pages 1-5, costa2024pls3mutationsin pages 11-12, costa2024pls3mutationsin pages 2-4)

For curation:

- **Origin:** germline; inherited or de novo. No somatic disease mechanism is established.
- **Functional class:** predominantly loss of function/haploinsufficiency in heterozygous females and functional null status in hemizygous males; some missense alleles alter actin bundling or calcium regulation.
- **Population frequency:** causal variants are expected to be absent or extremely rare in gnomAD; every variant should be checked against the current database and ancestry-matched coverage before ACMG classification.
- **Classification:** use ACMG/AMP evidence separately for each allele. A PLS3 VUS should not diagnose disease without segregation, phenotype concordance, RNA/protein evidence, or validated functional results.
- **Structural abnormalities:** exon and whole-gene deletions require copy-number detection. Large contiguous deletions may produce additional findings from neighboring genes. (costa2024pls3mutationsin pages 10-11, costa2024pls3mutationsin pages 1-2)
- **Epigenetics:** variable X-inactivation is a plausible female-expression mechanism, but no validated disease methylation signature or clinical epigenetic assay exists.
- **Modifier genes:** none validated; LRP5 is a candidate in an isolated severe case. (costa2024pls3mutationsin pages 11-12)

## 5. Mechanism/pathophysiology

### Ordered causal chain

1. A germline loss-of-function or function-disrupting **PLS3** variant **leads to** absent, reduced, or abnormally regulated plastin-3 activity.
2. Plastin-3 dysfunction **leads to** impaired calcium-sensitive F-actin bundling and abnormal organization of focal adhesions, osteocyte processes, and osteoclast podosome-associated structures. This is demonstrated in cellular and animal models but incompletely verified in human bone. (neugebauer2018plastin3influences pages 3-4, chin2023theactinbundlingprotein pages 1-2)
3. In osteoblast-lineage cells, defective cytoskeletal organization **leads to** reduced responsiveness to extracellular-matrix stiffness and impaired cell spreading; patient-associated mutants fail to rescue these defects. (chin2023theactinbundlingprotein pages 1-2)
4. Impaired mechanosensing **leads to** defective mineralization of deposited collagen matrix, while initial matrix deposition may remain relatively preserved. (chin2023theactinbundlingprotein pages 1-2)
5. **Branch A—osteocyte signaling:** altered actin-dependent mechanotransduction **is inferred to lead to** abnormal remodeling signals. MLO-Y4 RNA-seq found 259 upregulated and 368 downregulated transcripts with Wnt- and Th17-associated enrichment, but these pathway associations are not yet proven causal. (n2024functionalinsightsin pages 10-12, n2024functionalinsightsin pages 1-2)
6. **Branch B—osteoclasts:** PLS3 loss **leads to** podosome/NKRF–NF-κB–NFATC1 dysregulation and increased resorptive activity in vitro. However, osteoclast-specific deletion does not cause osteoporosis in vivo, demonstrating that this branch alone is insufficient. (neugebauer2018plastin3influences pages 3-4, maus2024osteoclastspecificplastin3 pages 1-2)
7. Combined abnormalities in osteoblasts, osteocytes, and osteoclast coupling **lead to** low bone formation/turnover, impaired cortical acquisition and trabecular architecture, and abnormal matrix mineralization. (balasubramanian2018novelpls3variants pages 11-14, neugebauer2018plastin3influences pages 5-5, hu2023impairedbonestrength pages 7-8)
8. Reduced bone quantity, architecture, and material quality **result in** low BMD, vertebral collapse, and recurrent low-trauma peripheral fractures.

### Recent mechanistic developments

A 2023 MC3T3-E1 study showed that PLS3 depletion spared early collagen-matrix deposition but “severely” impaired subsequent mineralization. Control osteoblasts increased cell size and focal-adhesion number/length on 100-kPa versus 6-kPa substrates; PLS3-depleted cells did not. Wild-type PLS3 rescued spreading, whereas three patient-associated mutants with abnormal actin bundling did not. This supplies direct evidence linking actin bundling to osteoblast mechanosensation. (chin2023theactinbundlingprotein pages 1-2)

A 2024 osteoclast-specific knockout study found markedly increased resorption in vitro but normal micro-CT and three-point bending outcomes at 12, 24, and 48 weeks. Expert interpretation is therefore shifting from an osteoclast-centric model to a **multicellular bone-remodeling disorder**. (maus2024osteoclastspecificplastin3 pages 1-2)

A 2024 multi-model study found that ACTN1 and ACTN4—but not FSCN1—could rescue zebrafish skeletal abnormalities, suggesting partial redundancy among actin-bundling proteins. Patient fibroblast-derived osteoblast-like cells showed increased WNT2, while osteocyte-like cells showed Wnt/Th17-associated transcriptional changes; the small samples and absence of pathway-specific rescue preclude declaring Wnt or immune signaling primary. (n2024functionalinsightsin pages 12-14, n2024functionalinsightsin pages 10-12, n2024functionalinsightsin pages 1-2)

**Suggested GO processes:** actin filament bundle assembly; actin cytoskeleton organization; cellular response to mechanical stimulus; focal-adhesion assembly; biomineral tissue development; ossification; bone mineralization; bone remodeling; osteoblast differentiation; osteoclast differentiation; canonical Wnt signaling. **Suggested cell types:** osteoblast, **CL:0000062**; osteocyte, **CL:0000137**; osteoclast, **CL:0000092**. Immune involvement is presently a transcriptomic association, not demonstrated inflammatory disease.

No reproducible PLS3-specific metabolomic, lipidomic, spatial-transcriptomic, single-cell, or integrated human multi-omic signature has been established. A sex-dependent serum microRNA profile has been explored, but it is not a validated diagnostic or prognostic biomarker.

## 6. Anatomy

The primary affected organ is the **skeleton**, involving both cortical and trabecular compartments. Clinically important sites are vertebral bodies, long-bone shafts/metaphyses, hip/femoral neck, forearm, and occasionally small bones. Disease is generalized rather than lateralized. Suggested anatomy terms are **UBERON:0002091** (bone), **UBERON:0004288** (skeleton), vertebral column, vertebral body, femur, humerus, radius, ulna, and tibia.

At tissue level, affected structures include cortical bone, trabecular bone, bone matrix, osteoid/mineralization fronts, and the osteocyte lacuno-canalicular network. Relevant subcellular terms include actin cytoskeleton, actin filament bundle, focal adhesion, podosome, cytoplasm, and plasma membrane-associated adhesion complexes. (balasubramanian2018novelpls3variants pages 11-14, neugebauer2018plastin3influences pages 3-4, chin2023theactinbundlingprotein pages 1-2)

## 7. Temporal development and inheritance/population

Onset is usually insidious but becomes clinically apparent with a fracture in childhood; the documented range in the recent five-family cohort was 1.5–13 years. Disease is chronic and lifelong, with episodic fractures superimposed on persistent skeletal fragility. Growth and puberty may modify BMD trajectory, and childhood represents an important window for vertebral reshaping and peak-bone-mass acquisition. (costa2024pls3mutationsin pages 11-12, costa2024pls3mutationsin pages 1-2)

Inheritance is X-linked. A heterozygous woman has a 50% probability of transmitting the variant in each pregnancy; sons who inherit it are hemizygous, while daughters are heterozygous and variably affected. An affected male transmits the variant to all daughters and no sons. Male penetrance appears high for clearly loss-of-function alleles but has not been quantified; female penetrance is incomplete and age dependent. There is no evidence for anticipation. Germline mosaicism is theoretically possible but not quantified. Consanguinity is not relevant to the X-linked mechanism.

Disease-specific prevalence, incidence, carrier frequency, ethnic enrichment, geographic distribution, and male:female case ratio are unknown. Published families span multiple ancestries and regions, consistent with a globally distributed but underdiagnosed disorder. (dijk2013pls3mutationsin pages 6-6, costa2024pls3mutationsin pages 1-2)

## 8. Diagnostics

### Clinical evaluation

1. Document age and mechanism of every fracture, vertebral pain/height loss, family history through the maternal lineage, medications, diet, mobility, puberty, and secondary disease.
2. Obtain DXA with age-, sex-, and size-adjusted Z-scores in children; image the lateral spine because vertebral fractures may occur even when symptoms are limited.
3. Use targeted radiographs for acute fractures and deformity; consider vertebral-fracture assessment and, in specialized centers, high-resolution peripheral QCT.
4. Exclude secondary causes with calcium, phosphate, alkaline phosphatase, creatinine, liver tests, 25-hydroxyvitamin D, parathyroid hormone, blood count/inflammatory testing, thyroid studies, celiac testing, and sex-hormone/puberty evaluation as clinically indicated.
5. Bone-turnover markers may be low or normal but are not diagnostic. Transiliac biopsy can document turnover, mineralization, and material abnormalities when diagnosis or treatment choice remains uncertain. (balasubramanian2018novelpls3variants pages 11-14, balasubramanian2018novelpls3variants pages 1-5)

### Molecular testing

A comprehensive early-onset osteoporosis/bone-fragility panel should include **PLS3, COL1A1, COL1A2, WNT1, LRP5, SGMS2, IFITM5, SERPINF1, P3H1, FKBP10, ALPL**, and other phenotype-appropriate genes. Sequencing must be paired with exon-level copy-number analysis because partial and whole-gene PLS3 deletions are established causes. WES is useful for genetically heterogeneous cases; WGS adds noncoding, structural, and breakpoint detection but does not replace variant interpretation. CMA is useful for large or contiguous deletions. Routine karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are not first-line unless another diagnosis is suspected. (costa2024pls3mutationsin pages 11-12, costa2024pls3mutationsin pages 1-2)

After diagnosis, perform cascade testing and skeletal assessment in at-risk relatives—including apparently asymptomatic women. PLS3 screening is warranted in both male and female patients with severe childhood-onset primary osteoporosis. (balasubramanian2018novelpls3variants pages 11-14, balasubramanian2018novelpls3variants pages 1-5)

### Differential diagnosis

Major alternatives are COL1A1/COL1A2-related OI; WNT1-, LRP5-, and SGMS2-related osteoporosis; idiopathic juvenile osteoporosis; hypophosphatasia; nutritional rickets/osteomalacia; glucocorticoid or chronic-inflammatory osteoporosis; celiac disease; eating disorders; endocrine hypogonadism/hyperthyroidism/hyperparathyroidism; renal disease; and nonaccidental injury. Normal mineral chemistry does not exclude PLS3 disease, while persistently low alkaline phosphatase favors hypophosphatasia.

No standardized PLS3-specific diagnostic criteria, FDA-qualified biomarker, newborn-screening program, or validated omics diagnostic exists.

## 9. Outcomes and prognosis

Life expectancy and disease-specific mortality have not been quantified and are not known to be intrinsically reduced. Morbidity is dominated by recurrent fractures, vertebral deformity, chronic pain, orthopedic procedures, possible mobility limitation, and failure to attain normal peak bone mass. A 40-year-old originally diagnosed with juvenile osteoporosis later sustained a hip fracture, illustrating persistence into adulthood. (balasubramanian2018novelpls3variants pages 1-5)

Prognostic indicators probably include hemizygous male status, early first fracture, vertebral involvement, very low lumbar BMD, accumulated fracture burden, large loss-of-function deletions, and coexisting skeletal risks. These have not been validated in a prognostic model. BMD response does not necessarily equal restored bone strength; fracture outcomes and vertebral morphology should also be followed.

## 10. Treatment and real-world implementation

There is no PLS3-specific guideline or approved molecular therapy. Management should occur in a pediatric or adult metabolic-bone center.

- **Foundational care:** ensure calcium and vitamin-D sufficiency; encourage supervised, low-impact weight-bearing and muscle-strengthening activity; avoid unnecessary immobilization and bone-toxic drugs; provide pain control, physiotherapy, occupational adaptation, and fall/injury prevention.
- **Fracture/orthopedic care:** standard fracture stabilization, monitoring for vertebral collapse and deformity, and individualized surgery. Severe vertebral injury may require fusion, as in a 26-year-old with an L1 fracture. (costa2024pls3mutationsin pages 2-4)
- **Bisphosphonates:** pamidronate or zoledronic acid are the most reported pediatric agents; alendronate has also been used. In the recent cohort, four treated patients showed lumbar-spine BMD increase and vertebral reshaping over 10 months–2 years. One eight-year-old had no new fractures during ten months of monthly pamidronate. These uncontrolled observations support possible benefit but cannot establish response rates. (costa2024pls3mutationsin pages 2-4, costa2024pls3mutationsin pages 1-2)
- **Teriparatide:** limited to skeletally mature patients. One adult receiving teriparatide plus calcium/vitamin D had 2.4% femoral-neck and 4.1% total-hip BMD gains at ten months without new fractures or reported adverse events. Evidence remains sparse. (costa2024pls3mutationsin pages 2-4)
- **Safety:** prolonged antiresorptive exposure requires specialist review; an atypical femoral fracture has been reported in a bisphosphonate-treated adolescent with PLS3 disease, but causality and absolute risk are unknown.

In a patient-derived rat model, alendronate and teriparatide improved BMD/microarchitecture, while teriparatide—but not alendronate—significantly improved bone strength. This is translational evidence, not proof of comparative clinical efficacy. (hu2023impairedbonestrength pages 7-8)

Suggested NCIT intervention concepts include bisphosphonate therapy, pamidronate, zoledronic acid, alendronate, teriparatide therapy, calcium supplementation, vitamin-D supplementation, physical therapy, orthopedic surgery, and genetic counseling. No disease-specific interventional ClinicalTrials.gov study was identified in the tool search. Gene replacement, CRISPR editing, RNA therapy, cell therapy, and targeted PLS3 pathway therapy remain preclinical concepts.

## 11. Prevention

**Primary prevention:** no postnatal intervention prevents the inherited disorder. Genetic counseling permits informed reproductive planning. Once a familial pathogenic variant is known, prenatal diagnosis and preimplantation genetic testing are technically feasible subject to local regulation and patient preference.

**Secondary prevention:** identify disease before multiple fractures through cascade testing, DXA and spine imaging of relatives, including heterozygous women. Evaluate children with unexplained vertebral compression or recurrent low-trauma fractures promptly.

**Tertiary prevention:** maintain calcium/vitamin-D sufficiency, safe activity and muscle strength; reduce falls/high-impact trauma; avoid smoking, excess alcohol, and unnecessary glucocorticoids; monitor spinal morphology, growth, puberty, BMD, pain, mobility, and treatment toxicity. Vaccination and infectious prophylaxis are not disease-specific.

## 12. Other species and model organisms

No confirmed naturally occurring veterinary PLS3 osteoporosis syndrome or zoonotic/transmissible process was found. Orthologous biology is conserved in **Homo sapiens** (NCBI Taxon 9606), **Mus musculus** (10090), **Rattus norvegicus** (10116), and **Danio rerio** (7955).

- **Zebrafish:** morpholino pls3 knockdown causes craniofacial, axial, tail, muscle, and F-actin abnormalities; human PLS3 mRNA dose-dependently rescues the phenotype. ACTN1 and ACTN4 also rescue major skeletal defects, while FSCN1 does not adequately compensate. Limitations include morpholino artifacts, developmental rather than adult osteoporosis phenotypes, and anatomical differences from mammalian bone. (dijk2013pls3mutationsin pages 6-6, n2024functionalinsightsin pages 12-14, n2024functionalinsightsin pages 1-2)
- **Ubiquitous knockout mouse:** cortical and trabecular osteoporosis occurs in both sexes, more prominently in males, with reduced trabecular number, greater separation, and reduced cortical thickness/area. PLS3 overexpression thickens cortical bone and increases strength, but also alters trabecular structure, indicating dose-sensitive biology. (neugebauer2018plastin3influences pages 3-4, neugebauer2018plastin3influences pages 5-5)
- **Conditional mouse:** LysMCre-mediated osteoclast deletion markedly increases in-vitro resorption but produces no osteoporosis or mechanical weakness through 48 weeks. This is a powerful negative-causality experiment showing that osteoclast-autonomous loss is insufficient. (maus2024osteoclastspecificplastin3 pages 1-2)
- **Patient-relevant rat:** hemizygous PLS3 exon 10–16 deletion reduces cortical thickness, mineral apposition, and femoral/vertebral strength and causes cortical porosity and collagen disorganization. It is useful for longitudinal biomechanics and pharmacology, although rodents do not fully model human X-inactivation or decades-long fracture history. (hu2023impairedbonestrength pages 7-8)
- **Cell models:** MC3T3-E1 osteoblasts model focal-adhesion mechanosensing and mineralization; MLO-Y4 cells permit osteocyte-like transcriptomics; patient fibroblast-derived osteoblast-like cells permit genotype-specific assays. Limitations include immortalized lineage states, artificial substrate mechanics, small donor numbers, and incomplete recapitulation of the mineralized lacuno-canalicular environment. (chin2023theactinbundlingprotein pages 1-2, n2024functionalinsightsin pages 10-12)

## 13. Evidence gaps and research priorities

The principal gaps are accurate prevalence and penetrance; prospective natural history; systematic female-carrier phenotyping; variant-specific functional assays; robust BMD-independent strength biomarkers; single-cell/spatial profiling of human bone; clarification of osteoblast–osteocyte–osteoclast coupling; and adequately powered treatment trials with fracture, vertebral-reshaping, pain, function, and safety outcomes. The 2024 finding that isolated osteoclast dysfunction is insufficient is particularly important: future therapeutic development should target integrated cytoskeletal mechanobiology rather than presuming a purely antiresorptive disease. (n2024functionalinsightsin pages 12-14, maus2024osteoclastspecificplastin3 pages 1-2)

### Selected recent and landmark sources

- Costa A, et al. **PLS3 Mutations in X-Linked Osteoporosis: Clinical and Genetic Features in Five New Families.** *Calcified Tissue International*. Online December 2023; issue 2024;114:157–170. https://doi.org/10.1007/s00223-023-01162-4. Abstract conclusion: “early treatment with bisphosphonates may influence the disease course and reduce the progression of osteoporosis.” (costa2024pls3mutationsin pages 1-2)
- Chin SM, et al. **The actin-bundling protein, PLS3, is part of the mechanoresponsive machinery that regulates osteoblast mineralization.** *Frontiers in Cell and Developmental Biology*. Published November 27, 2023. https://doi.org/10.3389/fcell.2023.1141738. The abstract concludes that PLS3 actin bundling forms part of the mechanosensitive mechanism promoting osteoblast mineralization. (chin2023theactinbundlingprotein pages 1-2)
- Maus I, et al. **Osteoclast-specific Plastin 3 knockout in mice fail to develop osteoporosis despite dramatic increased osteoclast resorption activity.** *JBMR Plus*. Published January 4, 2024. https://doi.org/10.1093/jbmrpl/ziad009. Its central finding is that osteoclast-specific loss does not reproduce systemic osteoporosis. (maus2024osteoclastspecificplastin3 pages 1-2)
- Zhong W, et al. **Functional Insights in PLS3-Mediated Osteogenic Regulation.** *Cells*. Published September 9, 2024;13:1507. https://doi.org/10.3390/cells13171507. The study links PLS3 loss to actin-bundling compensation and Wnt/Th17-associated transcription while emphasizing broader, unresolved bone pathways. (n2024functionalinsightsin pages 12-14, n2024functionalinsightsin pages 1-2)
- Hu J, et al. **Impaired bone strength and bone microstructure in a novel early-onset osteoporotic rat model with a clinically relevant PLS3 mutation.** *eLife*. April 2023;12:e80365. https://doi.org/10.7554/eLife.80365. (hu2023impairedbonestrength pages 7-8)
- van Dijk FS, et al. **PLS3 Mutations in X-Linked Osteoporosis with Fractures.** *New England Journal of Medicine*. October 17, 2013;369:1529–1536. https://doi.org/10.1056/NEJMoa1308223. The abstract states that PLS3 is involved in F-actin-bundle formation and that pathogenic variants in five families established its importance in human bone health. (dijk2013pls3mutationsin pages 6-6)

PMIDs were not consistently present in the retrieved full-text metadata; DOI URLs are therefore supplied rather than risking incorrect PMID assignment.

References

1. (costa2024pls3mutationsin pages 2-4): Adriana Costa, Andreia Martins, Catarina Machado, Elena Lundberg, Ola Nilsson, Fan Wang, Alice Costantini, Symeon Tournis, Jakob Höppner, Corinna Grasemann, and Outi Mäkitie. Pls3 mutations in x-linked osteoporosis: clinical and genetic features in five new families. Calcified Tissue International, 114:157-170, Dec 2024. URL: https://doi.org/10.1007/s00223-023-01162-4, doi:10.1007/s00223-023-01162-4. This article has 11 citations and is from a peer-reviewed journal.

2. (costa2024pls3mutationsin pages 1-2): Adriana Costa, Andreia Martins, Catarina Machado, Elena Lundberg, Ola Nilsson, Fan Wang, Alice Costantini, Symeon Tournis, Jakob Höppner, Corinna Grasemann, and Outi Mäkitie. Pls3 mutations in x-linked osteoporosis: clinical and genetic features in five new families. Calcified Tissue International, 114:157-170, Dec 2024. URL: https://doi.org/10.1007/s00223-023-01162-4, doi:10.1007/s00223-023-01162-4. This article has 11 citations and is from a peer-reviewed journal.

3. (dijk2013pls3mutationsin pages 6-6): Fleur S. van Dijk, M. Carola Zillikens, Dimitra Micha, Markus Riessland, Carlo L.M. Marcelis, Christine E. de Die-Smulders, Janine Milbradt, Anton A. Franken, Arjan J. Harsevoort, Klaske D. Lichtenbelt, Hans E. Pruijs, M. Estela Rubio-Gozalbo, Rolf Zwertbroek, Youssef Moutaouakil, Jaqueline Egthuijsen, Matthias Hammerschmidt, Renate Bijman, Cor M. Semeins, Astrid D. Bakker, Vincent Everts, Jenneke Klein-Nulend, Natalia Campos-Obando, Albert Hofman, Gerard J. te Meerman, Annemieke J.M.H. Verkerk, André G. Uitterlinden, Alessandra Maugeri, Erik A. Sistermans, Quinten Waisfisz, Hanne Meijers-Heijboer, Brunhilde Wirth, Marleen E.H. Simon, and Gerard Pals. <i>pls3</i> mutations in x-linked osteoporosis with fractures. Oct 2013. URL: https://doi.org/10.1056/nejmoa1308223, doi:10.1056/nejmoa1308223. This article has 261 citations and is from a highest quality peer-reviewed journal.

4. (costa2024pls3mutationsin pages 11-12): Adriana Costa, Andreia Martins, Catarina Machado, Elena Lundberg, Ola Nilsson, Fan Wang, Alice Costantini, Symeon Tournis, Jakob Höppner, Corinna Grasemann, and Outi Mäkitie. Pls3 mutations in x-linked osteoporosis: clinical and genetic features in five new families. Calcified Tissue International, 114:157-170, Dec 2024. URL: https://doi.org/10.1007/s00223-023-01162-4, doi:10.1007/s00223-023-01162-4. This article has 11 citations and is from a peer-reviewed journal.

5. (chin2023theactinbundlingprotein pages 1-2): Samantha M. Chin, Carmela Unnold-Cofre, Teri Naismith, and Silvia Jansen. The actin-bundling protein, pls3, is part of the mechanoresponsive machinery that regulates osteoblast mineralization. Frontiers in Cell and Developmental Biology, Nov 2023. URL: https://doi.org/10.3389/fcell.2023.1141738, doi:10.3389/fcell.2023.1141738. This article has 6 citations.

6. (balasubramanian2018novelpls3variants pages 11-14): Meena Balasubramanian, Nadja Fratzl‐Zelman, Rory O'Sullivan, Mary Bull, Nicola FA Peel, Rebecca C Pollitt, Rebecca Jones, Elizabeth Milne, Kath Smith, Paul Roschger, Klaus Klaushofer, and Nicholas J Bishop. Novel pls3 variants in x‐linked osteoporosis: exploring bone material properties. American Journal of Medical Genetics Part A, 176:1578-1586, May 2018. URL: https://doi.org/10.1002/ajmg.a.38830, doi:10.1002/ajmg.a.38830. This article has 43 citations.

7. (balasubramanian2018novelpls3variants pages 1-5): Meena Balasubramanian, Nadja Fratzl‐Zelman, Rory O'Sullivan, Mary Bull, Nicola FA Peel, Rebecca C Pollitt, Rebecca Jones, Elizabeth Milne, Kath Smith, Paul Roschger, Klaus Klaushofer, and Nicholas J Bishop. Novel pls3 variants in x‐linked osteoporosis: exploring bone material properties. American Journal of Medical Genetics Part A, 176:1578-1586, May 2018. URL: https://doi.org/10.1002/ajmg.a.38830, doi:10.1002/ajmg.a.38830. This article has 43 citations.

8. (neugebauer2018plastin3influences pages 3-4): Janine Neugebauer, Juliane Heilig, Seyyedmohsen Hosseinibarkooie, Bryony C Ross, Natalia Mendoza-Ferreira, Franziska Nolte, Miriam Peters, Irmgard Hölker, Kristina Hupperich, Theresa Tschanz, Vanessa Grysko, Frank Zaucke, Anja Niehoff, and Brunhilde Wirth. Plastin 3 influences bone homeostasis through regulation of osteoclast activity. Human Molecular Genetics, 27:4249–4262, Sep 2018. URL: https://doi.org/10.1093/hmg/ddy318, doi:10.1093/hmg/ddy318. This article has 72 citations and is from a domain leading peer-reviewed journal.

9. (maus2024osteoclastspecificplastin3 pages 1-2): Ilka Maus, Maren Dreiner, Sebastian Zetzsche, Fabian Metzen, Bryony C Ross, Daniela Mählich, Manuel Koch, Anja Niehoff, and Brunhilde Wirth. Osteoclast-specific plastin 3 knockout in mice fail to develop osteoporosis despite dramatic increased osteoclast resorption activity. JBMR Plus, Jan 2024. URL: https://doi.org/10.1093/jbmrpl/ziad009, doi:10.1093/jbmrpl/ziad009. This article has 3 citations and is from a peer-reviewed journal.

10. (hu2023impairedbonestrength pages 7-8): Jing Hu, Bingna Zhou, Xiaoyun Lin, Qian Zhang, Feifei Guan, Lei Sun, Jiayi Liu, Ou Wang, Yan Jiang, Wei-bo Xia, Xiaoping Xing, and Mei Li. Impaired bone strength and bone microstructure in a novel early-onset osteoporotic rat model with a clinically relevant pls3 mutation. Apr 2023. URL: https://doi.org/10.7554/elife.80365, doi:10.7554/elife.80365. This article has 9 citations and is from a domain leading peer-reviewed journal.

11. (n2024functionalinsightsin pages 10-12): Victoriano Baladr ó n, Gianpaolo Papaccio, Wenchao Zhong, Janine Neugebauer, J. Pathak, Xingyang Li, G. Pals, M. Zillikens, E. M. Eekhoff, Nathalie Bravenboer, Qingbin Zhang, Matthias Hammerschmidt, Brunhilde Wirth, and D. Micha. Functional insights in pls3-mediated osteogenic regulation. Sep 2024. URL: https://doi.org/10.3390/cells13171507, doi:10.3390/cells13171507. This article has 5 citations.

12. (brlek2021xlinkedosteogenesisimperfecta pages 10-11): Petar Brlek, Darko Antičević, Vilim Molnar, Vid Matišić, Kristina Robinson, Swaroop Aradhya, Dalibor Krpan, and Dragan Primorac. X-linked osteogenesis imperfecta possibly caused by a novel variant in pls3. Genes, 12:1851, Nov 2021. URL: https://doi.org/10.3390/genes12121851, doi:10.3390/genes12121851. This article has 20 citations.

13. (maus2024osteoclastspecificplastin3 pages 2-3): Ilka Maus, Maren Dreiner, Sebastian Zetzsche, Fabian Metzen, Bryony C Ross, Daniela Mählich, Manuel Koch, Anja Niehoff, and Brunhilde Wirth. Osteoclast-specific plastin 3 knockout in mice fail to develop osteoporosis despite dramatic increased osteoclast resorption activity. JBMR Plus, Jan 2024. URL: https://doi.org/10.1093/jbmrpl/ziad009, doi:10.1093/jbmrpl/ziad009. This article has 3 citations and is from a peer-reviewed journal.

14. (costa2024pls3mutationsin pages 10-11): Adriana Costa, Andreia Martins, Catarina Machado, Elena Lundberg, Ola Nilsson, Fan Wang, Alice Costantini, Symeon Tournis, Jakob Höppner, Corinna Grasemann, and Outi Mäkitie. Pls3 mutations in x-linked osteoporosis: clinical and genetic features in five new families. Calcified Tissue International, 114:157-170, Dec 2024. URL: https://doi.org/10.1007/s00223-023-01162-4, doi:10.1007/s00223-023-01162-4. This article has 11 citations and is from a peer-reviewed journal.

15. (n2024functionalinsightsin pages 1-2): Victoriano Baladr ó n, Gianpaolo Papaccio, Wenchao Zhong, Janine Neugebauer, J. Pathak, Xingyang Li, G. Pals, M. Zillikens, E. M. Eekhoff, Nathalie Bravenboer, Qingbin Zhang, Matthias Hammerschmidt, Brunhilde Wirth, and D. Micha. Functional insights in pls3-mediated osteogenic regulation. Sep 2024. URL: https://doi.org/10.3390/cells13171507, doi:10.3390/cells13171507. This article has 5 citations.

16. (neugebauer2018plastin3influences pages 5-5): Janine Neugebauer, Juliane Heilig, Seyyedmohsen Hosseinibarkooie, Bryony C Ross, Natalia Mendoza-Ferreira, Franziska Nolte, Miriam Peters, Irmgard Hölker, Kristina Hupperich, Theresa Tschanz, Vanessa Grysko, Frank Zaucke, Anja Niehoff, and Brunhilde Wirth. Plastin 3 influences bone homeostasis through regulation of osteoclast activity. Human Molecular Genetics, 27:4249–4262, Sep 2018. URL: https://doi.org/10.1093/hmg/ddy318, doi:10.1093/hmg/ddy318. This article has 72 citations and is from a domain leading peer-reviewed journal.

17. (n2024functionalinsightsin pages 12-14): Victoriano Baladr ó n, Gianpaolo Papaccio, Wenchao Zhong, Janine Neugebauer, J. Pathak, Xingyang Li, G. Pals, M. Zillikens, E. M. Eekhoff, Nathalie Bravenboer, Qingbin Zhang, Matthias Hammerschmidt, Brunhilde Wirth, and D. Micha. Functional insights in pls3-mediated osteogenic regulation. Sep 2024. URL: https://doi.org/10.3390/cells13171507, doi:10.3390/cells13171507. This article has 5 citations.

## Artifacts

- [Edison artifact artifact-00](PLS3-Related_X-Linked_Osteoporosis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.