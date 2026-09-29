---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T17:01:56.426121'
end_time: '2026-09-02T17:16:17.838763'
duration_seconds: 861.41
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Heart Defects, Multiple Types, 2
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 1
  verified: 1
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
  path: Congenital_Heart_Defects_Multiple_Types_2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Heart Defects, Multiple Types, 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Heart Defects, Multiple Types, 2** covering all of the
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
- **Disease Name:** Congenital Heart Defects, Multiple Types, 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Heart Defects, Multiple Types, 2** covering all of the
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


# Congenital Heart Defects, Multiple Types, 2: comprehensive disease-characteristics report

## Executive summary

**Congenital heart defects, multiple types, 2** is the historical Mendelian label for **TAB2-related congenital heart disease**, now understood as part of a broader, autosomal-dominant **TAB2-related multisystem disorder**. Heterozygous loss-of-function variants or deletions involving **TAB2 at 6q25.1** cause highly variable congenital valvular and septal disease, cardiomyopathy that may appear in infancy or adulthood, and, frequently, connective-tissue, skeletal, growth, craniofacial, sensory, and neurodevelopmental findings. Consequently, “isolated CHD” is too narrow for many affected people. In the largest retrieved aggregation of sequence-variant cases (n=39), 86% had structural cardiac abnormalities, 51% had functional cardiac abnormalities, and 64% had cardiac disease plus extracardiac manifestations. These estimates are case-series frequencies, not population prevalence. (hanson2022tab2variantscause pages 3-5, hanson2022tab2variantscause pages 1-3, hanson2022tab2variantscause pages 12-13)

The strongest current mechanism is **TAB2 haploinsufficiency**: inadequate TAB2 compromises assembly or regulation of the TAK1 signaling complex, alters MAPK/AP-1 and NF-κB signaling, disturbs extracellular-matrix (ECM) homeostasis, and—within myocardium—releases RIPK1-dependent apoptotic and necroptotic signaling. The 2023 development of a scalable AP-1 reporter assay that reclassified 22/32 tested variants of uncertain significance (VUSs) is the most important recent diagnostic advance identified. (xu2023assigningpathogenicityfor pages 1-2, yin2022tab2deficiencyinduces pages 10-11, morlino2019tab2c.1398dupvariant pages 4-7)

| Domain | Best quantitative finding or key result | Evidence type/model | Interpretation/limitation | Source with year and DOI URL |
|---|---|---|---|---|
| Clinical spectrum | Among 39 people with pathogenic TAB2 sequence variants, structural cardiac abnormalities occurred in 33/39 (86%): mitral-valve involvement 26/39 (67%), tricuspid 19/39 (49%), aortic 14/39 (36%), pulmonic 6/39 (15%), bicuspid aortic valve 6/39 (15%), patent ductus arteriosus 6/39 (15%), ventricular septal defect 5/39 (13%), and atrial septal defect 3/39 (8%). Functional abnormalities occurred in 20/39 (51%), including dilated cardiomyopathy in 18/39 (46%). | Human case series plus literature aggregation; 15 newly reported and 24 published individuals | Largest compiled sequence-variant cohort available in the retrieved evidence, but subject to ascertainment, publication, and missing-data bias; frequencies should not be treated as population prevalence. | Hanson et al., 2022, [DOI](https://doi.org/10.1111/cge.14085) (hanson2022tab2variantscause pages 3-5, hanson2022tab2variantscause pages 12-13) |
| Syndromic and extracardiac spectrum | Syndromic CHD or adult-onset cardiomyopathy with extracardiac findings occurred in 25/39 (64%). Reported aggregate findings included facial dysmorphism 23/39 (59%), skeletal abnormalities 21/39 (54%), joint/skin findings 16/39 (41%), growth abnormalities 10/39 (26%), and hearing loss and myopia 7/39 each (18%). Developmental delay occurred in 8/15 (53%) of the newly reported cohort. | Human case series and literature review | Supports classification as a multisystem TAB2-related disorder rather than exclusively nonsyndromic CHD; developmental-delay frequency derives from the newly ascertained subgroup and may reflect referral bias. | Hanson et al., 2022, [DOI](https://doi.org/10.1111/cge.14085) (hanson2022tab2variantscause pages 1-3, hanson2022tab2variantscause pages 5-7, hanson2022tab2variantscause pages 12-13) |
| Variant functional classification | A cell-based luciferase platform tested 47 TAB2 variants; AP-1, but not NF-κB, transcriptional activity predicted pathogenicity. The assay reclassified 22/32 tested VUSs (68.8%) and detected both loss- and gain-of-function effects. | CRISPR TAB2-knockout and transfected HEK293T cells; reporter assays, immunoblotting, imaging, flow cytometry, and structural modeling | Provides scalable functional evidence useful for ACMG/AMP interpretation, especially missense variants. Clinical validation remains limited, and HEK293T signaling may not reproduce embryonic valve or cardiomyocyte biology. | Xu et al., 2023, [DOI](https://doi.org/10.1093/hmg/ddac252) (xu2023assigningpathogenicityfor pages 10-11, xu2023assigningpathogenicityfor pages 1-2) |
| Extracellular-matrix mechanism | Patient fibroblasts carrying heterozygous TAB2 c.1398dup showed altered expression of 22/30 assayed ECM-related transcripts—16 upregulated and 6 downregulated—plus disorganized collagen III/V networks, cytoplasmic collagen accumulation, markedly reduced fibronectin matrix, and impaired proliferation with G0/G1 enrichment. | Primary dermal fibroblasts from two affected individuals; nonsense-mediated-decay studies, targeted PCR array, immunofluorescence, and signaling assays | Demonstrates haploinsufficiency, defective TAK1 binding/autophosphorylation, altered NF-κB/MAPK signaling, and ECM disruption in patient cells. Dermal fibroblast findings support but do not directly prove embryonic cardiac-valve pathology. | Morlino et al., 2019, [DOI](https://doi.org/10.1002/humu.23834) (morlino2019tab2c.1398dupvariant pages 7-9, morlino2019tab2c.1398dupvariant pages 4-7, morlino2019tab2c.1398dupvariant pages 9-12) |
| Cardiomyopathy and cell-death mechanism | Cardiomyocyte-specific Tab2 deletion caused dilated cardiomyopathy with apoptosis and necroptosis. TAB2 normally enables TAK1-dependent RIPK1 Ser321 phosphorylation; loss permits RIPK1-FADD-caspase-8 apoptotic and RIPK1-RIPK3 necroptotic complexes. Forced TAK1 activation rescued cell death, and kinase-dead Ripk1-K45A substantially rescued remodeling and dysfunction. | Conditional neonatal and inducible adult mouse knockouts; primary cardiomyocyte and genetic-rescue experiments | Strong causal evidence for myocardial homeostasis and a candidate RIPK1-targeted strategy, but it models TAB2 deficiency in cardiomyocytes rather than congenital valve morphogenesis; no human therapeutic efficacy is established. | Yin et al., 2022, [DOI](https://doi.org/10.1172/JCI152297) (yin2022tab2deficiencyinduces pages 10-11) |
| Recent pathogenic variant | A child with growth restriction, facial differences, and CHD carried a novel heterozygous TAB2 c.1056delC, p.Ser353fsTer8 frameshift; both parents were wild type, supporting de novo occurrence. In-vitro expression indicated that the variant may abolish detectable protein expression. | Single human case; trio whole-exome sequencing, plasmid expression, and immunoblotting | Expands the loss-of-function spectrum and supports haploinsufficiency, but a single case cannot establish penetrance, phenotype frequency, or treatment response. Growth-hormone benefit was not established. | Deng et al., 2023, [DOI](https://doi.org/10.3892/etm.2023.11957) (deng2023growthrestrictionand pages 4-5) |


*Table: Key quantitative clinical and experimental findings supporting TAB2-related congenital heart disease, its multisystem spectrum, variant interpretation, and proposed mechanisms. Limitations distinguish human cohort evidence from cellular and animal-model inference.*

## 1. Disease information

### Definition and scope

TAB2-related disease is a congenital-developmental and sometimes progressive cardiovascular disorder caused principally by heterozygous TAB2 loss of function. Cardiac manifestations include congenital dysplasia, prolapse, stenosis, or regurgitation of one or several valves; septal defects; patent ductus arteriosus; bicuspid aortic valve; left-sided obstructive lesions; and dilated cardiomyopathy. The current clinical spectrum also includes a recognizable connective-tissue/multisystem phenotype. Rare missense alleles may produce different functional effects and phenotypes, including frontometaphyseal dysplasia without CHD; these should not automatically be equated with classic haploinsufficiency. (hanson2022tab2variantscause pages 1-3, hanson2022tab2variantscause pages 7-9, xu2023assigningpathogenicityfor pages 1-2)

### Identifiers and synonyms

* **Preferred knowledge-base label:** TAB2-related disorder or TAB2-related congenital heart disease.
* **OMIM disease label:** Congenital heart defects, multiple types, 2. The precise numeric OMIM accession was not present in the retrieved full-text evidence and should be verified directly against the current OMIM record before ingestion.
* **Gene:** **TAB2**, TGF-beta activated kinase 1 (MAP3K7) binding protein 2; chromosome **6q25.1**; reference transcript used in the principal cohorts **NM_015093.5**. (chen2020anoveltab2 pages 4-6, hanson2022tab2variantscause pages 3-5)
* **Synonyms:** TAB2-related syndrome; TAB2 haploinsufficiency syndrome; 6q25.1/TAB2 microdeletion syndrome; TAB2-associated polyvalvular heart disease; TAB2-related connective-tissue disorder; TAB2-related cardiomyopathy.
* **MONDO/Orphanet:** A disease-specific accession could not be validated from retrieved evidence. Do not substitute a general congenital-heart-disease MONDO term without curator verification.
* **ICD-10/ICD-11 and MeSH:** No unique TAB2-specific code exists in the evidence reviewed. Code the observed lesion(s)—for example congenital mitral insufficiency, bicuspid aortic valve, septal defect, or congenital cardiomyopathy—plus the genetic syndrome where local coding rules permit.

The evidence is **aggregated disease-level literature**, including clinically ascertained families, exome cohorts, literature reviews, and experimental models. It is not derived from a single EHR population. The largest phenotype estimates combine 15 newly ascertained subjects and 24 published cases and therefore carry ascertainment and publication bias. (hanson2022tab2variantscause pages 3-5, hanson2022tab2variantscause pages 1-3)

## 2. Etiology

### Causal factors and genetic risk

The primary established cause is a **germline heterozygous pathogenic TAB2 variant** or a deletion encompassing TAB2. Nonsense, frameshift, canonical splice-site variants and larger 6q25.1 deletions support haploinsufficiency. In one 15-person cohort, variants were 11/15 nonsense, two splice, one frameshift, and one missense; inheritance included five de novo, three maternal, three paternal, and four unknown events. (hanson2022tab2variantscause pages 3-5)

Examples include:

* **c.446C>G, p.Ser149Ter (p.S149X):** segregated in five affected members of a three-generation Chinese family and was absent from eight unaffected tested relatives; classified as pathogenic under ACMG/AMP criteria. The family had heterogeneous mitral, tricuspid, aortic, and pulmonic disease, and a child had sudden cardiac death at age two. (chen2020anoveltab2 pages 4-6)
* **c.1056delC, p.Ser353fsTer8:** apparently de novo in a child with CHD, growth restriction, and facial differences; mutant-expression experiments suggested loss of protein expression. (deng2023growthrestrictionand pages 4-5)
* **c.1398dup:** undergoes substantial nonsense-mediated decay; residual truncated protein lacks the C-terminal region required for normal TAK1 interaction. (morlino2019tab2c.1398dupvariant pages 7-9, morlino2019tab2c.1398dupvariant pages 4-7)
* Recurrent reported alleles include **c.679C>T (p.Arg227Ter), c.1491T>A (p.Tyr497Ter), c.1636C>T (p.Arg546Ter), and c.1764+1G>A**. (hanson2022tab2variantscause pages 3-5)

### Environmental, infectious, and lifestyle risks

No TAB2-specific maternal toxin, infection, diet, smoking, occupational exposure, or other environmental cause was demonstrated in the retrieved literature. General CHD teratogens should not be attributed specifically to this Mendelian disorder. Likewise, no replicated modifier gene, genetic protective allele, environmental protective factor, or formal TAB2 gene–environment interaction is established.

Pathological cardiac stress may interact with TAB2 deficiency **after development**: Tab2-deficient mice were more susceptible to adverse remodeling after pressure overload or myocardial infarction. This is model-organism evidence for stress-dependent myocardial vulnerability, not evidence that these exposures cause the congenital lesions in humans. (yin2022tab2deficiencyinduces pages 10-11)

## 3. Phenotypes

### Cardiac manifestations

In the 39-person sequence-variant aggregation, 33/39 (86%) had structural abnormalities. Mitral involvement occurred in 26/39 (67%), tricuspid in 19/39 (49%), aortic in 14/39 (36%), and pulmonary-valve involvement in 6/39 (15%). Bicuspid aortic valve and patent ductus arteriosus each occurred in 6/39 (15%), ventricular septal defect in 5/39 (13%), atrial septal defect in 3/39 (8%), and coarctation and supravalvular aortic stenosis in two subjects each. Functional disease occurred in 20/39 (51%), with dilated cardiomyopathy in 18/39 (46%). (hanson2022tab2variantscause pages 12-13)

Suggested HPO annotations include **Abnormality of the cardiac valves (HP:0001654)**, Mitral regurgitation, Tricuspid regurgitation, Aortic valve stenosis, Bicuspid aortic valve, **Polyvalvular dysplasia**, Patent ductus arteriosus, Ventricular septal defect, Atrial septal defect, Coarctation of aorta, Supravalvular aortic stenosis, Dilated cardiomyopathy, Hypertrophic cardiomyopathy, Supraventricular tachycardia, and Sudden cardiac death. Exact HPO accessions for each subordinate term should be resolved against the current HPO release.

### Extracardiac manifestations

Across the same aggregation, facial dysmorphism occurred in 23/39 (59%), skeletal findings in 21/39 (54%), joint/skin findings in 16/39 (41%), growth abnormalities in 10/39 (26%), and hearing loss and myopia in seven subjects each (18%). In the newly ascertained subgroup, developmental delay/failure to thrive/hypotonia occurred in 8/15 (53%). Overall, 25/39 (64%) had syndromic CHD or adult-onset cardiomyopathy with extracardiac features, and 23/25 syndromic cases had at least two extracardiac manifestations. (hanson2022tab2variantscause pages 1-3, hanson2022tab2variantscause pages 5-7, hanson2022tab2variantscause pages 7-9)

Suggested terms include Short stature, Failure to thrive, Joint hypermobility, Joint contracture, Abnormal skin elasticity/texture, Scoliosis, Hypotonia, Global developmental delay, Facial dysmorphism, Hearing impairment, and Myopia. Phenotypes are variable even within families; absence of connective-tissue or developmental findings does not exclude the disorder. (chen2020anoveltab2 pages 4-6, hanson2022tab2variantscause pages 7-9)

### Onset, severity, progression, and quality of life

Structural lesions are congenital, although diagnosis in the recent cohort ranged from three months to 26 years. Cardiomyopathy may begin in infancy or adulthood and can progress to heart failure, transplantation, or sudden death. Valvular dysfunction may be stable or progressive depending on valve anatomy and loading conditions. Published disease-specific patient-reported quality-of-life data, EQ-5D scores, and phenotype-specific functional-impact percentages were not found. Nevertheless, surgery, heart failure, rhythm disease, developmental delay, visual/hearing impairment, and musculoskeletal limitations are expected to affect education, exercise, employment, and daily function; this is clinical inference rather than quantified TAB2-specific evidence. (hanson2022tab2variantscause pages 3-5, hanson2022tab2variantscause pages 7-9)

## 4. Genetic and molecular information

### Gene and variant interpretation

TAB2 encodes an adaptor in the ubiquitin-responsive **TAK1/MAP3K7 signaling complex**. Classic disease-causing variants are germline and heterozygous; somatic disease is not established. Truncating and deletion alleles usually produce loss of function through nonsense-mediated decay, reduced protein abundance, loss of TAK1 binding, or combinations of these effects. Population allele frequencies for individual pathogenic alleles were not reported in the retrieved passages; bona fide severe loss-of-function alleles are expected to be rare, but each allele must be checked in the current gnomAD release rather than assigned a generic frequency. (morlino2019tab2c.1398dupvariant pages 7-9, morlino2019tab2c.1398dupvariant pages 4-7)

Missense interpretation is particularly challenging. Xu and colleagues noted 295 missense variants among 576 nonsynonymous TAB2 variants in gnomAD and 16/73 ClinVar entries; 15/16 ClinVar missense entries were VUSs at the time analyzed. Their 2023 assay tested 47 variants and reclassified 22/32 VUSs (68.8%). AP-1 reporter activity, but not NF-κB reporter activity, predicted pathogenicity; the assay detected both loss- and gain-of-function effects. The authors’ abstract states: **“the transcriptional activity of AP-1 but not NF-κB predicts the TAB2 variant pathogenicity.”** (xu2023assigningpathogenicityfor pages 1-2, xu2023assigningpathogenicityfor pages 10-11)

Partial loss-of-function alleles appeared to produce less CHD but more developmental delay, hypotonia, and dysmorphism than complete loss of function, although numbers were small. NZF-domain structural stability was particularly important for AP-1 activation. These genotype–phenotype observations require replication before clinical prediction. (xu2023assigningpathogenicityfor pages 10-11)

### Chromosomal and epigenetic findings

Deletions at **6q25.1** encompassing TAB2 can produce the same core syndrome, although deletion size and neighboring genes can broaden the phenotype. No recurrent aneuploidy, balanced translocation, repeat expansion, mitochondrial-DNA lesion, or disease-specific methylation episignature was established in the retrieved evidence. No validated protective or modifier locus was identified.

## 5. Environmental information

This is fundamentally a genetic developmental disorder. No disease-specific toxin, radiation exposure, pollution source, infectious pathogen, maternal lifestyle factor, diet, or occupational exposure has been shown to cause TAB2-related disease. Rubella, diabetes, retinoids, alcohol, and other general CHD risks should remain separate annotations unless documented in an individual case. There is no indication of transmissibility or zoonosis.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous TAB2 deletion or loss-of-function variant **leads to** reduced functional TAB2 dosage through nonsense-mediated decay, absent protein, or defective protein interactions. (deng2023growthrestrictionand pages 4-5, morlino2019tab2c.1398dupvariant pages 7-9)
2. Reduced TAB2 **leads to** impaired recruitment/regulation of the MAP3K7/TAK1 complex and altered TAK1 abundance or autophosphorylation. (morlino2019tab2c.1398dupvariant pages 7-9, morlino2019tab2c.1398dupvariant pages 4-7)
3. Impaired TAK1-complex signaling **results in** abnormal MAPK–AP-1 and NF-κB pathway responses; AP-1 dysfunction is the stronger experimentally scalable predictor of variant pathogenicity. (xu2023assigningpathogenicityfor pages 1-2, xu2023assigningpathogenicityfor pages 10-11)
4. **Developmental branch—partly inferred:** altered signaling in endocardial/endothelial and mesenchymal lineages **is proposed to disrupt** endothelial-to-mesenchymal transition, cushion remodeling, and valve/outflow-tract morphogenesis, **leading to** valve dysplasia, septal defects, and obstructive lesions. EndMT involvement is biologically supported but was not directly demonstrated in affected human embryonic heart tissue. (chen2020anoveltab2 pages 6-7)
5. **ECM branch—demonstrated in patient fibroblasts, inferred in valves:** TAB2 deficiency **leads to** dysregulated collagen/ECM transcription, impaired fibroblast proliferation, and abnormal collagen/fibronectin organization, which **may lead to** connective-tissue laxity and malformed or mechanically abnormal valves. (morlino2019tab2c.1398dupvariant pages 4-7, morlino2019tab2c.1398dupvariant pages 9-12)
6. **Myocardial branch—demonstrated in mice:** loss of TAB2-mediated TAK1 phosphorylation of RIPK1 at Ser321 **leads to** RIPK1 kinase activation and formation of RIPK1–FADD–caspase-8 apoptotic and RIPK1–RIPK3 necroptotic complexes. (yin2022tab2deficiencyinduces pages 10-11)
7. Cardiomyocyte apoptosis/necroptosis **results in** myocardial loss and adverse remodeling, **leading to** ventricular dilation, reduced contractility, heart failure, and susceptibility to pathological stress. Translation of this exact chain to human TAB2 cardiomyopathy remains strongly plausible but incompletely demonstrated. (yin2022tab2deficiencyinduces pages 10-11)

### Cellular, biochemical, and molecular-profile detail

Patient c.1398dup fibroblasts showed reduced TAK1 abundance/autophosphorylation and reduced NF-κB and phosphorylated-MAPK responses after TGF-β treatment. Twenty-two of 30 assayed ECM transcripts were altered—16 increased and six decreased—and collagen III/V accumulated intracellularly instead of forming normal fibrillar networks; fibronectin matrix was markedly reduced. Cells proliferated less and accumulated in G0/G1. This is targeted PCR-array and imaging evidence, not whole-transcriptome or proteomic profiling. (morlino2019tab2c.1398dupvariant pages 4-7, morlino2019tab2c.1398dupvariant pages 9-12)

In mouse cardiomyocytes, forced TAK1 activation rescued TAB2-loss-associated death, while genetic RIPK1 kinase inactivation substantially rescued remodeling and cardiac dysfunction. RIPK3 deletion was only partly protective, indicating contributions from both apoptosis and necroptosis. RIPK1 inhibition is therefore a mechanistically credible research direction, but not a validated treatment in patients. (yin2022tab2deficiencyinduces pages 10-11)

Suggested ontology annotations:

* **GO biological process:** protein ubiquitination-dependent signaling; MAPK cascade; NF-κB signaling; AP-1 transcriptional regulation; regulation of programmed cell death; apoptotic process; necroptotic process; extracellular-matrix organization; collagen fibril organization; endothelial-to-mesenchymal transition; cardiac valve morphogenesis; heart development.
* **GO cellular component:** cytosol; TAK1–TAB signaling complex; nucleus; extracellular matrix; collagen-containing extracellular matrix; focal adhesion.
* **Cell Ontology:** cardiomyocyte; endocardial cell; vascular endothelial cell; cardiac-valve interstitial cell; cardiac fibroblast; mesenchymal cell; dermal fibroblast.

No disease-specific single-cell atlas, spatial transcriptomic study, unbiased proteomic/metabolomic/lipidomic signature, or clinically validated epigenomic profile was found for 2023–2024.

## 7. Anatomical structures affected

The primary organ is the **heart**, especially the mitral, tricuspid, aortic, and pulmonary valves; ventricular and atrial septa; ductus arteriosus; left-ventricular outflow tract; aortic arch; and ventricular myocardium. Suggested UBERON annotations include heart, cardiac valve, mitral valve, tricuspid valve, aortic valve, pulmonary valve, interventricular septum, interatrial septum, left ventricle, right ventricle, ascending aorta, and aortic arch. (hanson2022tab2variantscause pages 12-13)

Secondary systems include connective tissue, skeleton/joints, skin, craniofacial structures, eye, ear, and nervous/developmental systems. There is no characteristic lateralization. At the subcellular level, the best-supported compartments are the cytosolic TAK1 signaling complex, nucleus/AP-1 and NF-κB transcriptional outputs, and extracellular collagen/fibronectin matrix. (hanson2022tab2variantscause pages 1-3, morlino2019tab2c.1398dupvariant pages 4-7)

## 8. Temporal development

The initiating lesion is present from conception, and structural cardiac malformations arise during embryogenesis. Clinical recognition may occur prenatally, neonatally, in childhood, or after an affected relative is identified. Valvular dysfunction and cardiomyopathy can evolve over decades; intrafamilial variation in onset and severity is prominent. Reported outcomes include childhood sudden death, adult-onset cardiomyopathy, severe heart failure, and transplantation, but no robust stage-specific survival curve exists. (chen2020anoveltab2 pages 4-6, hanson2022tab2variantscause pages 7-9)

Critical windows are: (1) embryonic cushion/valve and outflow-tract development; (2) fetal/neonatal detection of severe lesions; and (3) lifelong surveillance for progressive regurgitation, stenosis, ventricular dilation, systolic dysfunction, and arrhythmia. There is no biological remission of the genotype. Hemodynamic abnormalities can be corrected or palliated, but repaired patients remain at risk for residual or progressive disease.

## 9. Inheritance and population

Inheritance is **autosomal dominant**. Both de novo and inherited variants occur. Each child of a heterozygous individual has a theoretical 50% transmission risk, but clinical expression is unpredictable. Penetrance is not reliably quantified; segregation in some families is strong, while broader literature demonstrates variable expressivity and age-dependent recognition. Germline mosaicism is theoretically possible after an apparently de novo case but was not quantified. Genetic anticipation, recurrent founder variants, a consanguinity effect, and population-specific carrier frequencies are not established. (chen2020anoveltab2 pages 4-6, hanson2022tab2variantscause pages 3-5, hanson2022tab2variantscause pages 7-9)

Disease-specific prevalence and incidence are unknown. General CHD occurs in approximately 7–9 per 1,000 live births, but this must not be reported as TAB2 prevalence. TAB2-related disease is rare and current estimates are dominated by referral cohorts. No reliable sex ratio, ethnic enrichment, or geographic concentration has been established. Reports from European, North American, Chinese, and other families support worldwide occurrence. The Chinese p.S149Ter report was the first published TAB2 pathogenic variant in that population, not evidence of population enrichment. (chen2020anoveltab2 pages 4-6)

## 10. Diagnostics

### Clinical evaluation

Diagnosis begins with detailed personal and three-generation family history, physical examination for dysmorphism/connective-tissue findings, and comprehensive **transthoracic echocardiography** assessing all four valves, septa, outflow tracts, aortic arch, chamber size, and ventricular function. ECG and ambulatory rhythm monitoring are appropriate where palpitations, syncope, cardiomyopathy, or family sudden death is present. Cardiac MRI can quantify ventricular volume, function, and fibrosis when echocardiography is incomplete or cardiomyopathy is suspected. No disease-specific blood, urine, enzyme, histopathology, or circulating biomarker is validated.

### Genetic testing strategy

1. **Chromosomal microarray (CMA):** first-line where CHD co-occurs with growth restriction, dysmorphism, developmental delay, or multiple congenital anomalies; detects 6q25.1 deletions.
2. **CHD/cardiomyopathy multigene panel or exome sequencing:** include TAB2 with deletion/duplication analysis. Exome testing identified many recent cases and the de novo c.1056delC variant. (hanson2022tab2variantscause pages 3-5, deng2023growthrestrictionand pages 4-5)
3. **Single-gene TAB2 sequencing:** reasonable in a highly suggestive polyvalvular/connective-tissue phenotype or for familial testing.
4. **Genome sequencing:** useful after nondiagnostic CMA/exome, especially for structural or noncoding variants, although TAB2-specific incremental yield is unknown.
5. **Segregation testing:** test parents and informative relatives to clarify de novo status and support interpretation.
6. **Functional testing:** the 2023 AP-1 reporter assay can provide evidence for selected VUSs, but it is not yet a universally available clinical assay. (xu2023assigningpathogenicityfor pages 1-2, xu2023assigningpathogenicityfor pages 10-11)

Karyotype/FISH may detect large rearrangements but are less comprehensive than CMA. Mitochondrial DNA and repeat-expansion tests are not routine for this condition. RNA analysis may demonstrate altered splicing or nonsense-mediated decay for selected variants; broad clinical transcriptomic, proteomic, metabolomic, epigenomic, and liquid-biopsy diagnostics are not established.

### Differential diagnosis and screening

Differentials include other genetic polyvalvular/CHD syndromes and cardiomyopathy genes, particularly RASopathies, FLNA-related valvular disease, NOTCH1/SMAD6-associated left-sided lesions, connective-tissue/aortopathy syndromes, and chromosomal CNVs. Distinguishing features favoring TAB2 include multivalve involvement, dilated cardiomyopathy, short stature, joint/skin abnormalities, and a compatible dominant pedigree.

Once a familial pathogenic variant is known, offer cascade testing, fetal echocardiography, chorionic-villus/amniotic molecular testing, and preimplantation genetic testing after nondirective counseling. Molecular prenatal diagnosis was implemented in the p.S149Ter family. (chen2020anoveltab2 pages 6-7)

## 11. Outcome and prognosis

No reliable 5- or 10-year survival rates or genotype-specific life-expectancy estimates exist. Prognosis ranges from mild valve disease compatible with adulthood to severe congenital obstruction, progressive dilated cardiomyopathy, transplantation, or sudden cardiac death. Important adverse prognostic features are severe multivalve dysfunction, ventricular dilation or systolic impairment, arrhythmia/syncope, early heart failure, and family history of sudden death. (chen2020anoveltab2 pages 4-6, hanson2022tab2variantscause pages 7-9)

Potential chronic morbidity includes repeated interventions, heart failure, exercise limitation, arrhythmia, anticoagulation after some valve procedures, developmental/educational difficulties, hearing or vision impairment, and musculoskeletal symptoms. No validated TAB2-specific prognostic biomarker or risk calculator exists. Published frequencies cannot be converted into individual risk because of small samples and ascertainment bias.

## 12. Treatment

There is **no approved TAB2-directed pharmacotherapy, gene therapy, RNA therapy, or cell therapy**, and the targeted ClinicalTrials.gov search found no relevant TAB2 interventional trial. Management is individualized to the cardiac lesion and functional status:

* observation with serial echocardiography for mild valve disease;
* guideline-directed heart-failure therapy for systolic dysfunction;
* rhythm monitoring and standard antiarrhythmic/device management where indicated;
* catheter-based or surgical closure of appropriate septal/ductal lesions;
* valve repair or replacement for severe stenosis/regurgitation;
* repair/palliation of coarctation, outflow obstruction, or hypoplastic-left-heart physiology;
* transplantation for refractory end-stage cardiomyopathy.

Suggested NCIt intervention concepts include Echocardiography, Cardiac Magnetic Resonance Imaging, Electrocardiography, Ambulatory Electrocardiographic Monitoring, Cardiac Valve Repair, Cardiac Valve Replacement, Ventricular Septal Defect Repair, Patent Ductus Arteriosus Closure, Heart Failure Therapy, Pacemaker Therapy, Implantable Cardioverter-Defibrillator Therapy, and Heart Transplantation. Exact NCIt codes should be resolved against the current release.

RIPK1 inhibition rescued cellular and mouse phenotypes and is an experimental target—not a clinical recommendation. Growth hormone was used in one child, but benefit was not established. Supportive care should include developmental assessment/therapy, audiology, ophthalmology, growth/nutrition evaluation, and physical/occupational therapy as indicated. (deng2023growthrestrictionand pages 4-5, yin2022tab2deficiencyinduces pages 10-11)

## 13. Prevention

Primary prevention of the pathogenic variant is not possible after conception. Genetic counseling supports reproductive choices, including preimplantation testing, prenatal molecular diagnosis, and fetal echocardiography. Avoid implying that maternal lifestyle modification can eliminate a monogenic 50% transmission risk.

Secondary prevention consists of early identification: cascade testing of relatives, baseline echocardiography even in apparently asymptomatic carriers, and prenatal/neonatal assessment. Tertiary prevention consists of lifelong cardiology surveillance and timely intervention before irreversible ventricular dysfunction, arrhythmia, or decompensation. Multidisciplinary monitoring of growth, development, hearing, vision, and connective tissue has been recommended in recent case literature. (deng2023growthrestrictionand pages 4-5)

Routine immunization follows general congenital-heart-disease guidance; there is no TAB2-specific vaccine. Infective-endocarditis prophylaxis should follow standard lesion/prosthetic-material guidelines rather than genotype alone.

## 14. Other species and natural disease

Orthologous Tab2 genes are conserved in **Mus musculus** (NCBI Taxon 10090) and **Danio rerio** (NCBI Taxon 7955), supporting comparative developmental and signaling studies. No well-established, naturally occurring TAB2 haploinsufficiency syndrome in a companion-animal breed, livestock, or wildlife population was identified; no VBO breed term is therefore justified. The condition is genetic and noninfectious, with no zoonotic or cross-species transmission.

## 15. Model organisms and experimental systems

### Mouse

Cardiomyocyte-specific neonatal and inducible adult **Tab2 knockout** mice develop dilated cardiomyopathy, apoptosis, and necroptosis and show increased vulnerability to pressure overload or myocardial infarction. Genetic RIPK1 kinase inactivation substantially rescues remodeling and dysfunction. This model strongly recapitulates myocardial disease but does not reproduce the full heterozygous human valve/connective-tissue syndrome. (yin2022tab2deficiencyinduces pages 10-11)

### Zebrafish

Zebrafish tab2 haploinsufficiency produces developmental defects and supports dosage sensitivity. Advantages include live imaging and rapid embryonic functional testing; limitations include a two-chambered heart and imperfect correspondence between fish and human valve phenotypes. (morlino2019tab2c.1398dupvariant pages 1-2)

### Human cellular models

* **Patient dermal fibroblasts:** directly demonstrate c.1398dup nonsense-mediated decay, defective TAK1 interaction/signaling, reduced proliferation, and ECM disorganization. Limitation: dermal fibroblasts are proxies for embryonic valve interstitial cells. (morlino2019tab2c.1398dupvariant pages 7-9, morlino2019tab2c.1398dupvariant pages 4-7)
* **CRISPR TAB2-knockout HEK293T cells and variant-expression assays:** enable high-throughput AP-1/NF-κB functional classification and structural analysis. Limitation: transformed kidney-derived cells do not model cardiac morphogenesis. (xu2023assigningpathogenicityfor pages 10-11)
* **Human iPSC-cardiomyocytes:** no 2023–2024 TAB2 disease-model publication was identified in the retrieved evidence. Such models remain a logical platform for testing myocardial mechanisms and allele-specific rescue.

## Recent developments and evidence gaps

The principal 2023 advance was Xu et al.’s scalable functional assay, which linked variant pathogenicity more closely to AP-1 than NF-κB activity and resolved 68.8% of tested VUSs. Deng et al. added a de novo frameshift case with experimental evidence of absent mutant protein. No equally disease-specific 2024 clinical cohort, guideline, therapy trial, single-cell atlas, or spatial/multi-omics study was retrieved. (deng2023growthrestrictionand pages 4-5, xu2023assigningpathogenicityfor pages 1-2)

The highest priorities are prospective natural-history registries; unbiased penetrance estimates from population sequencing; standardized valve/cardiomyopathy surveillance; cardiac-lineage and organoid models; single-cell analysis of endocardial, valve-interstitial, fibroblast, and cardiomyocyte effects; and preclinical evaluation of TAK1/RIPK1 pathway interventions without disrupting essential immune and developmental signaling.

## Key publications and abstract quotations

* **Xu et al., Human Molecular Genetics, published online October 2022/volume 32 (2023), DOI:** https://doi.org/10.1093/hmg/ddac252. Abstract: **“22 out of 32 tested VUSs were reclassified.”** It also concludes: **“we developed a highly effective functional assay for TAB2 variant prediction and interpretation.”** (xu2023assigningpathogenicityfor pages 1-2)
* **Hanson et al., Clinical Genetics 101:214–220, 2022, DOI:** https://doi.org/10.1111/cge.14085. Abstract: **“64% (25/39) of individuals with disease resulting from TAB2 single nucleotide variants (SNV) had syndromic CHD or adult-onset cardiomyopathy with one or more extra-cardiac features.”** (hanson2022tab2variantscause pages 1-3)
* **Morlino et al., Human Mutation 40:1886–1898, published October 2019, DOI:** https://doi.org/10.1002/humu.23834. The study demonstrated nonsense-mediated decay, loss of normal TAK1 binding, altered downstream signaling, and ECM disorganization in patient fibroblasts. (morlino2019tab2c.1398dupvariant pages 7-9, morlino2019tab2c.1398dupvariant pages 4-7)
* **Yin et al., Journal of Clinical Investigation 132, published February 2022, DOI:** https://doi.org/10.1172/JCI152297. The central conclusion was that TAB2 regulates myocardial homeostasis by suppressing RIPK1-dependent apoptosis and necroptosis. (yin2022tab2deficiencyinduces pages 10-11)
* **Deng et al., Experimental and Therapeutic Medicine 25:258, published April 2023, DOI:** https://doi.org/10.3892/etm.2023.11957. Abstract: **“When haploid dosage is insufficient, it can lead to CHD or cardiomyopathy.”** (deng2023growthrestrictionand pages 4-5)

PMIDs were not consistently present in the retrieved full texts and therefore are not supplied where they could not be verified. DOI URLs above provide stable primary-source links.

References

1. (hanson2022tab2variantscause pages 3-5): Jennifer Hanson, Daniel Brezavar, Susan Hughes, Shivarajan Amudhavalli, Emily Fleming, Dihong Zhou, Joseph T. Alaimo, and Penelope E. Bonnen. <scp><i>tab2</i></scp> variants cause cardiovascular heart disease, connective tissue disorder, and developmental delay. Nov 2022. URL: https://doi.org/10.1111/cge.14085, doi:10.1111/cge.14085. This article has 23 citations and is from a peer-reviewed journal.

2. (hanson2022tab2variantscause pages 1-3): Jennifer Hanson, Daniel Brezavar, Susan Hughes, Shivarajan Amudhavalli, Emily Fleming, Dihong Zhou, Joseph T. Alaimo, and Penelope E. Bonnen. <scp><i>tab2</i></scp> variants cause cardiovascular heart disease, connective tissue disorder, and developmental delay. Nov 2022. URL: https://doi.org/10.1111/cge.14085, doi:10.1111/cge.14085. This article has 23 citations and is from a peer-reviewed journal.

3. (hanson2022tab2variantscause pages 12-13): Jennifer Hanson, Daniel Brezavar, Susan Hughes, Shivarajan Amudhavalli, Emily Fleming, Dihong Zhou, Joseph T. Alaimo, and Penelope E. Bonnen. <scp><i>tab2</i></scp> variants cause cardiovascular heart disease, connective tissue disorder, and developmental delay. Nov 2022. URL: https://doi.org/10.1111/cge.14085, doi:10.1111/cge.14085. This article has 23 citations and is from a peer-reviewed journal.

4. (xu2023assigningpathogenicityfor pages 1-2): Weiyi Xu, Andrea Graves, Monika Weisz-Hubshman, Lamees Hegazy, Christina Magyar, Zian Liu, Eleni Nasiotis, Md Abul Hassan Samee, Thomas Burris, Seema Lalani, and Lilei Zhang. Assigning pathogenicity for tab2 variants using a novel scalable functional assay and expanding tab2 disease spectrum. Human molecular genetics, 32:959-970, Oct 2023. URL: https://doi.org/10.1093/hmg/ddac252, doi:10.1093/hmg/ddac252. This article has 0 citations and is from a domain leading peer-reviewed journal.

5. (yin2022tab2deficiencyinduces pages 10-11): Haifeng Yin, Xiaoyun Guo, Yi Chen, Yachang Zeng, Xiaoliang Mo, Siqi Hong, Hui He, Jing Li, Rachel Steinmetz, and Qinghang Liu. Tab2 deficiency induces dilated cardiomyopathy by promoting ripk1-dependent apoptosis and necroptosis. Feb 2022. URL: https://doi.org/10.1172/jci152297, doi:10.1172/jci152297. This article has 56 citations and is from a highest quality peer-reviewed journal.

6. (morlino2019tab2c.1398dupvariant pages 4-7): Silvia Morlino, Annalucia Carbone, Marco Ritelli, Carmela Fusco, Vincenzo Giambra, Grazia Nardella, Angelantonio Notarangelo, Patrizio Panelli, Gianluigi Mazzoccoli, Nicoletta Zoppi, Paola Grammatico, Emma M Wade, Marina Colombi, Marco Castori, and Lucia Micale. Tab2 c.1398dup variant leads to haploinsufficiency and impairs extracellular matrix homeostasis. Human Mutation, 40:1886-1898, Oct 2019. URL: https://doi.org/10.1002/humu.23834, doi:10.1002/humu.23834. This article has 9 citations and is from a domain leading peer-reviewed journal.

7. (hanson2022tab2variantscause pages 5-7): Jennifer Hanson, Daniel Brezavar, Susan Hughes, Shivarajan Amudhavalli, Emily Fleming, Dihong Zhou, Joseph T. Alaimo, and Penelope E. Bonnen. <scp><i>tab2</i></scp> variants cause cardiovascular heart disease, connective tissue disorder, and developmental delay. Nov 2022. URL: https://doi.org/10.1111/cge.14085, doi:10.1111/cge.14085. This article has 23 citations and is from a peer-reviewed journal.

8. (xu2023assigningpathogenicityfor pages 10-11): Weiyi Xu, Andrea Graves, Monika Weisz-Hubshman, Lamees Hegazy, Christina Magyar, Zian Liu, Eleni Nasiotis, Md Abul Hassan Samee, Thomas Burris, Seema Lalani, and Lilei Zhang. Assigning pathogenicity for tab2 variants using a novel scalable functional assay and expanding tab2 disease spectrum. Human molecular genetics, 32:959-970, Oct 2023. URL: https://doi.org/10.1093/hmg/ddac252, doi:10.1093/hmg/ddac252. This article has 0 citations and is from a domain leading peer-reviewed journal.

9. (morlino2019tab2c.1398dupvariant pages 7-9): Silvia Morlino, Annalucia Carbone, Marco Ritelli, Carmela Fusco, Vincenzo Giambra, Grazia Nardella, Angelantonio Notarangelo, Patrizio Panelli, Gianluigi Mazzoccoli, Nicoletta Zoppi, Paola Grammatico, Emma M Wade, Marina Colombi, Marco Castori, and Lucia Micale. Tab2 c.1398dup variant leads to haploinsufficiency and impairs extracellular matrix homeostasis. Human Mutation, 40:1886-1898, Oct 2019. URL: https://doi.org/10.1002/humu.23834, doi:10.1002/humu.23834. This article has 9 citations and is from a domain leading peer-reviewed journal.

10. (morlino2019tab2c.1398dupvariant pages 9-12): Silvia Morlino, Annalucia Carbone, Marco Ritelli, Carmela Fusco, Vincenzo Giambra, Grazia Nardella, Angelantonio Notarangelo, Patrizio Panelli, Gianluigi Mazzoccoli, Nicoletta Zoppi, Paola Grammatico, Emma M Wade, Marina Colombi, Marco Castori, and Lucia Micale. Tab2 c.1398dup variant leads to haploinsufficiency and impairs extracellular matrix homeostasis. Human Mutation, 40:1886-1898, Oct 2019. URL: https://doi.org/10.1002/humu.23834, doi:10.1002/humu.23834. This article has 9 citations and is from a domain leading peer-reviewed journal.

11. (deng2023growthrestrictionand pages 4-5): Qian Deng, Xin Wang, Jianxin Gao, Xiaowei Xia, Yun-gong Wang, Yin Zhang, and Yuqing Chen. Growth restriction and congenital heart disease caused by a novel tab2 mutation: a case report. Experimental and Therapeutic Medicine, Apr 2023. URL: https://doi.org/10.3892/etm.2023.11957, doi:10.3892/etm.2023.11957. This article has 9 citations and is from a peer-reviewed journal.

12. (hanson2022tab2variantscause pages 7-9): Jennifer Hanson, Daniel Brezavar, Susan Hughes, Shivarajan Amudhavalli, Emily Fleming, Dihong Zhou, Joseph T. Alaimo, and Penelope E. Bonnen. <scp><i>tab2</i></scp> variants cause cardiovascular heart disease, connective tissue disorder, and developmental delay. Nov 2022. URL: https://doi.org/10.1111/cge.14085, doi:10.1111/cge.14085. This article has 23 citations and is from a peer-reviewed journal.

13. (chen2020anoveltab2 pages 4-6): Jia Chen, Huizhen Yuan, Kang Xie, Xinrong Wang, Linglong Tan, Yongyi Zou, Yan Yang, Lu Pan, Junfang Xiao, Ge Chen, and Yanqiu Liu. A novel tab2 nonsense mutation (p.s149x) causing autosomal dominant congenital heart defects: a case report of a chinese family. BMC Cardiovascular Disorders, Jan 2020. URL: https://doi.org/10.1186/s12872-019-01322-1, doi:10.1186/s12872-019-01322-1. This article has 23 citations and is from a peer-reviewed journal.

14. (chen2020anoveltab2 pages 6-7): Jia Chen, Huizhen Yuan, Kang Xie, Xinrong Wang, Linglong Tan, Yongyi Zou, Yan Yang, Lu Pan, Junfang Xiao, Ge Chen, and Yanqiu Liu. A novel tab2 nonsense mutation (p.s149x) causing autosomal dominant congenital heart defects: a case report of a chinese family. BMC Cardiovascular Disorders, Jan 2020. URL: https://doi.org/10.1186/s12872-019-01322-1, doi:10.1186/s12872-019-01322-1. This article has 23 citations and is from a peer-reviewed journal.

15. (morlino2019tab2c.1398dupvariant pages 1-2): Silvia Morlino, Annalucia Carbone, Marco Ritelli, Carmela Fusco, Vincenzo Giambra, Grazia Nardella, Angelantonio Notarangelo, Patrizio Panelli, Gianluigi Mazzoccoli, Nicoletta Zoppi, Paola Grammatico, Emma M Wade, Marina Colombi, Marco Castori, and Lucia Micale. Tab2 c.1398dup variant leads to haploinsufficiency and impairs extracellular matrix homeostasis. Human Mutation, 40:1886-1898, Oct 2019. URL: https://doi.org/10.1002/humu.23834, doi:10.1002/humu.23834. This article has 9 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Congenital_Heart_Defects_Multiple_Types_2-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.