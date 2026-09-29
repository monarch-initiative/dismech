---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-01T16:14:00.357993'
end_time: '2026-09-01T16:29:10.612881'
duration_seconds: 910.25
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dilated Cardiomyopathy 1BB
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 50
  verified: 49
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  obsolete_terms:
  - term_id: GO:0062023
    ontology_label: obsolete collagen-containing extracellular matrix
    replaced_by: GO:0031012
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Dilated_Cardiomyopathy_1BB-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 1BB
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1BB** covering all of the
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
- **Disease Name:** Dilated Cardiomyopathy 1BB
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1BB** covering all of the
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


# Dilated Cardiomyopathy 1BB (DSG2-associated cardiomyopathy): comprehensive disease-characteristics report

## Executive summary and scope

Dilated cardiomyopathy 1BB (DCM1BB) is a rare genetic cardiomyopathy associated with **DSG2**, which encodes the desmosomal cadherin desmoglein-2. The specific ontology entry is **MONDO:0013030**. Modern evidence indicates substantial overlap among DSG2-associated dilated, biventricular, and arrhythmogenic cardiomyopathy phenotypes; therefore, “DCM1BB” should not be treated as a completely discrete clinicopathological entity. Direct DCM1BB evidence is limited, and much of the mechanistic and natural-history evidence comes from broader DSG2-associated arrhythmogenic cardiomyopathy (ACM), human myocardial specimens, induced pluripotent stem-cell cardiomyocytes (iPSC-CMs), and Dsg2 mouse models. Open Targets links MONDO:0013030 specifically to DSG2 and cites supporting literature including PMIDs **18678517, 23500315, 27532257, and 29567486**. (OpenTargets Search: Dilated cardiomyopathy 1BB)

The strongest current interpretation is that pathogenic DSG2 variants impair cardiomyocyte–cardiomyocyte adhesion and intercalated-disc organization, producing electrical instability, cardiomyocyte injury, inflammation, fibrosis, ventricular dilation, and systolic failure. Monoallelic variants often have incomplete, age-dependent penetrance and can require genetic or environmental modifiers; biallelic loss-of-function or severe missense genotypes generally produce earlier and more severe biventricular disease. (shiba2021phenotypicrecapitulationand pages 2-3, pinci2026integrativegenomicand pages 1-6, zhang2024hyperactivationofatf4tgfβ1 pages 1-2, sumida2024fourcardiomyopathypatients pages 1-2)

The following evidence map summarizes the distinction between direct DCM1BB evidence and broader DSG2-ACM extrapolation.

| Domain | Disease-specific finding | Evidence type | Key quantitative detail | Source/year |
|---|---|---|---|---|
| Identity | Dilated cardiomyopathy 1BB is mapped to MONDO:0013030 and linked to **DSG2** (desmoglein-2); evidence base is small and overlaps strongly with broader DSG2-associated arrhythmogenic cardiomyopathy literature | Curated disease-target association | 1 disease-target association listed for DCM1BB: DSG2 | Open Targets disease-target mapping (OpenTargets Search: Dilated cardiomyopathy 1BB) |
| Human genetics: p.Arg119Ter | Heterozygous **DSG2 p.Arg119Ter** occurs in cardiomyopathy patients with variable phenotypes including DCM; supports desmosomal impairment as a contributor/exacerbator rather than proving fully penetrant monogenic DCM1BB alone | Human cohort/case series | 4 unrelated carriers among 808 nonischemic cardiomyopathy patients; cohort allele frequency **0.0037**; described as **>50-fold** above general Japanese population; diagnoses included ARVC, DCM after VSD repair, DCM, end-stage HCM | Sumida et al., 2024 (sumida2024fourcardiomyopathypatients pages 1-2) |
| Human genetics: p.Phe531Cys family | Homozygous **DSG2 p.Phe531Cys / F531C** segregated with severe familial ACM featuring fibrosis/dysfunction; highly informative for DSG2 biology, but broader ACM evidence rather than direct DCM1BB nomenclature | Human family study + knock-in model | **8 affected family members**, all homozygous; desmosomal-gene variants account for **~two-thirds** of ACM; DSG2 described as second most prevalent ACM gene | Zhang et al., 2024 (zhang2024hyperactivationofatf4tgfβ1 pages 1-2) |
| Human cellular disease model | Complete DSG2 deficiency can present clinically as severe juvenile-onset biventricular cardiomyopathy diagnosed as idiopathic DCM, supporting DSG2-deficient DCM as a real disease mechanism | Human case + iPSC-derived cardiomyocytes | Homozygous **c.355C>T (p.R119X)**; VAD implantation at **age 21**; heterozygous parents unaffected; mutant tissue-ring force reduced and corrected after repair | Shiba et al., 2021 (shiba2021phenotypicrecapitulationand pages 2-3, shiba2021phenotypicrecapitulationand pages 1-1) |
| iPSC correction / AAV rescue | Disease phenotypes from DSG2 deficiency were reversed by isogenic correction and improved by AAV-mediated DSG2 replacement, providing preclinical precision-medicine proof of concept | Human iPSC-CM and engineered tissue | Contractile force improved from **49 ± 6 to 86 ± 1 μN** after correction; AAV-mediated DSG2 replacement significantly recovered contraction force | Shiba et al., 2021 (shiba2021phenotypicrecapitulationand pages 10-11, shiba2021phenotypicrecapitulationand pages 1-1) |
| 2024 immune mechanism | In DSG2-mutant mouse ACM, **NFκB signaling in cardiomyocytes** recruits **CCR2+ macrophages**, driving myocardial injury, dysfunction, arrhythmias, and fibro-inflammatory remodeling; mechanistically relevant but preclinical and broader ACM | Mouse genetics + single-nucleus/single-cell profiling | Disease prevented/attenuated when cardiac-myocyte NFκB signaling was blocked; snRNA-seq/CITE-seq implicated cardiomyocytes, fibroblasts, and CCR2+ macrophages | Chelko et al., 2024 (chelko2024nfĸbsignalingdrives pages 1-2) |
| 2024 fibrosis mechanism | Variant DSG2 protein can misfold in the ER, activate **BiP → PERK → ATF4 → TGF-β1**, and stimulate fibroblasts paracrinally, explaining progressive fibrosis in DSG2 cardiomyopathy | Human family-supported mouse/mechanistic study | Inhibition of PERK-ATF4 attenuated fibrosis and systolic dysfunction in **Dsg2F536C/F536C** mice | Zhang et al., 2024 (zhang2024hyperactivationofatf4tgfβ1 pages 1-2) |
| 2024 exercise interaction | Endurance training can unmask a right-ventricular arrhythmogenic phenotype in **heterozygous Dsg2** mice; relevant gene-environment interaction for DSG2 disease counseling | Mouse exercise model | DSG2 mutations reported in **5–10%** of ARVC; training increased RV diameter, decreased RV function, prolonged activation times, and induced pacing-triggered arrhythmia without obvious fibrosis/inflammation | Fabritz et al., 2024 (sumida2024fourcardiomyopathypatients pages 1-2) |
| Diagnostic implementation | Current care relies on phenotype-first cardiomyopathy workup with **echocardiography, CMR, ECG/Holter, biomarkers, pedigree analysis, and genetic testing/counseling**; DCM1BB has no standalone diagnostic criteria beyond inherited cardiomyopathy practice | Guideline/review | Genetic testing is described as a **first-tier diagnostic test for every patient with DCM**; CMR is gold standard for fibrosis/phenotyping; imaging + genetics guide ICD decisions | Stroeks et al., 2023; Grasso et al., 2024; Gasior, 2024 (stroeks2023diagnosticandprognostic pages 1-2, grasso2024thenew2023 pages 1-2, gasior2024advancesincardiac pages 1-2) |
| Epidemiology caveat | There are **no subtype-specific prevalence/incidence data** for DCM1BB; only broader DCM/ACM estimates are available, so population burden must be inferred cautiously | Review / broader disease epidemiology | ACM prevalence estimated **1:2000–1:5000**; DCM prevalence estimated **~1:220 to 1:250** in modern datasets, far higher than older **~1:2500** estimates | Vencato et al., 2024; Newman & Burke, 2024 (vencato2024animalmodelsand pages 1-2, newman2024dilatedcardiomyopathya pages 1-2) |
| Therapy status | **No DSG2-specific approved therapy** and **no DSG2-specific registered interventional clinical trial** were identified; current treatment remains standard HF/arrhythmia management, while gene therapy evidence is preclinical | Clinical-trial search + literature | Identified ACM trials were observational or targeted other genes/inflammatory pathways (e.g., PKP2 gene therapy), not DSG2-specific | Clinical-trial search context + field literature (OpenTargets Search: Dilated cardiomyopathy 1BB) |


*Table: This table summarizes the most decision-relevant evidence for DSG2-associated dilated cardiomyopathy 1BB, distinguishing direct DCM1BB findings from broader DSG2-arrhythmogenic cardiomyopathy data. It is useful for rapidly identifying what is established in humans, what remains preclinical, and where evidence gaps persist.*

## 1. Disease information

### Definition

DCM is defined clinically by left-ventricular or biventricular dilation and systolic dysfunction not sufficiently explained by coronary artery disease or abnormal loading conditions such as hypertension or valvular disease. The 2023 ESC framework defines cardiomyopathies as myocardial disorders with structural or functional abnormality in the absence of coronary, hypertensive, valvular, or congenital disease sufficient to explain it. (grasso2024thenew2023 pages 1-2, stroeks2023diagnosticandprognostic pages 1-2)

DCM1BB denotes the DSG2-associated genetic form. Because DSG2 disease often combines dilation, fibrosis, ventricular arrhythmias, and right-ventricular involvement, affected patients may instead receive diagnoses of DCM, arrhythmogenic right-ventricular cardiomyopathy (ARVC), arrhythmogenic biventricular cardiomyopathy, or end-stage cardiomyopathy. A 2024 series found the same heterozygous p.Arg119Ter allele among patients diagnosed with ARVC, two forms of DCM, and end-stage hypertrophic cardiomyopathy, illustrating this phenotypic continuum. (sumida2024fourcardiomyopathypatients pages 1-2)

### Identifiers and synonyms

- **MONDO:** MONDO:0013030.
- **Causal gene:** DSG2, desmoglein-2; Ensembl ENSG00000046604. (OpenTargets Search: Dilated cardiomyopathy 1BB)
- **Common names:** dilated cardiomyopathy 1BB; DCM1BB; DSG2-related dilated cardiomyopathy; desmoglein-2 cardiomyopathy; DSG2-associated cardiomyopathy.
- **Overlapping clinical terms:** DSG2-related arrhythmogenic cardiomyopathy, arrhythmogenic right-ventricular cardiomyopathy, biventricular arrhythmogenic cardiomyopathy.
- **Broader coding:** ICD-10-CM I42.0, dilated cardiomyopathy; I42.8/I42.9 may be used depending on local phenotype and coding practice. ICD-11 and MeSH generally classify the phenotype under dilated or arrhythmogenic cardiomyopathy rather than a DCM1BB-specific code.
- **OMIM/Orphanet:** A separate subtype-level identifier was not verified in the retrieved full-text evidence. Knowledge-base implementations should retain MONDO:0013030 and link DSG2-associated ARVC/ACM records rather than infer an unverified number.

This report synthesizes **aggregated disease resources and published cohorts**, not individual EHR records. Some primary evidence derives from individual patients or families, notably the homozygous p.Arg119Ter patient and the p.Phe531Cys pedigree. (shiba2021phenotypicrecapitulationand pages 2-3, zhang2024hyperactivationofatf4tgfβ1 pages 1-2)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factors

The initiating lesion is a germline pathogenic or likely pathogenic variant in **DSG2**. Desmoglein-2 is a calcium-dependent transmembrane cadherin at cardiac desmosomes and the area composita of intercalated discs. DSG2 and desmocollin-2 connect neighboring cardiomyocytes extracellularly and anchor through armadillo/plakin proteins to the cytoskeleton. (vencato2024animalmodelsand pages 1-2)

Disease-associated classes include missense substitutions affecting extracellular calcium-binding or adhesive domains, premature-termination variants, splice variants, frameshifts, and copy-number loss. Functional consequences vary and include reduced abundance, nonsense-mediated decay/haploinsufficiency, complete deficiency in biallelic loss, dominant-negative adhesive dysfunction, protein misfolding, and impaired cytoskeletal anchoring. (pinci2026integrativegenomicand pages 26-31, shiba2021phenotypicrecapitulationand pages 2-3, zhang2024hyperactivationofatf4tgfβ1 pages 1-2)

### Genetic risk factors and modifiers

- **Allele dosage:** Biallelic or multilocus genotypes are associated with earlier onset, greater biventricular involvement, and more complete penetrance than isolated monoallelic variants. (pinci2026integrativegenomicand pages 1-6)
- **Second variants:** In the 2024 p.Arg119Ter series, one patient also carried DSG2 p.Arg292Cys and another carried BAG3 p.His166SerfsTer6, supporting oligogenic modification. (sumida2024fourcardiomyopathypatients pages 1-2)
- **Variant location:** Extracellular calcium-binding residues, the furin-cleavage region, and intracellular PKP2-binding/cytoskeletal anchoring regions are enriched for clinically important variants. (pinci2026integrativegenomicand pages 26-31)
- **General DCM architecture:** Up to 40% of idiopathic DCM may be attributable to a core set of causal genes, but more than 200 genes have been reported and evidence for many is weak. This cautions against attributing disease to a DSG2 VUS without segregation or functional evidence. (newman2024dilatedcardiomyopathya pages 1-2, stroeks2023diagnosticandprognostic pages 1-2)

### Environmental and lifestyle risk factors

High-intensity or endurance exercise is the best-supported environmental accelerator for desmosomal ACM. A 2024 review reports up to a fivefold greater sudden-death risk in affected athletes, although this estimate is for ACM generally and is not DCM1BB-specific. (vencato2024animalmodelsand pages 1-2)

Sports, hypertension, diabetes, obesity, pregnancy, and toxic exposures can modulate dilation, dysfunction, and arrhythmia expression in cardiomyopathy broadly. Alcohol, cardiotoxic chemotherapy, myocarditis/infection, nutritional deficiency, and autoimmune disease are important alternative or interacting causes of DCM and should be assessed rather than assumed causal in an individual DSG2 carrier. (newman2024dilatedcardiomyopathya pages 1-2, gasior2024advancesincardiac pages 1-2)

The 2024 p.Arg119Ter investigators explicitly concluded that desmosomal impairment combined with additional genetic or environmental factors may promote dysfunction. In Dsg2 heterozygous mice, endurance training increased right-ventricular size, reduced right-ventricular function, prolonged activation, and increased inducible ventricular arrhythmia, supporting a mechanically mediated gene–exercise interaction, although translation to humans remains inferential. (sumida2024fourcardiomyopathypatients pages 1-2)

### Protective factors

No validated protective DSG2 allele, diet, supplement, or chemopreventive agent is established. Avoidance of competitive/high-intensity endurance exercise is the principal modifiable protective strategy extrapolated from ACM data. Control of hypertension, obesity, diabetes, alcohol exposure, and cardiotoxic drugs plausibly reduces additional myocardial stress but has not been quantified specifically for DCM1BB. Preload reduction prevented exercise-induced disease features in heterozygous Dsg2 mice, but this remains preclinical. (gasior2024advancesincardiac pages 1-2, vencato2024animalmodelsand pages 1-2)

## 3. Phenotypes

The phenotype is heterogeneous, age-dependent, and progressive. Frequencies below are generally unavailable for DCM1BB specifically.

| Manifestation | Type/course | Suggested HPO term |
|---|---|---|
| Left-ventricular dilation | Imaging sign; progressive/variable | **HP:0001644**, Dilated cardiomyopathy |
| Reduced LV systolic function | Imaging/functional abnormality | **HP:0001686**, Loss of left ventricular function |
| Biventricular dilation/dysfunction | Severe structural-functional sign; common in biallelic cases | **HP:0001717**, Right ventricular dilatation; HP:0001644 |
| Heart failure | Symptom/sign; exertional limitation to end-stage failure | **HP:0001635**, Congestive heart failure |
| Ventricular arrhythmia/tachycardia | Electrophysiological sign; may precede dilation | **HP:0004308**, Ventricular arrhythmia; **HP:0004756**, Ventricular tachycardia |
| Palpitations, syncope | Symptoms, episodic | **HP:0001962**, Palpitations; **HP:0001279**, Syncope |
| Sudden cardiac arrest/death | Severe outcome; sometimes first manifestation in ACM spectrum | **HP:0001699**, Sudden death |
| Myocardial fibrosis/scarring | CMR/pathology finding; progressive | **HP:0001685**, Myocardial fibrosis |
| Abnormal ECG/conduction | Electrophysiological sign | **HP:0003115**, Abnormal EKG; **HP:0031546**, Abnormal cardiac conduction |
| Cardiomegaly | Imaging/physical sign | **HP:0001640**, Cardiomegaly |
| Exercise intolerance/dyspnea/fatigue | Symptoms affecting daily activity | **HP:0003546**, Exercise intolerance; **HP:0002094**, Dyspnea; **HP:0012378**, Fatigue |

The homozygous p.Arg119Ter case was normal at birth but developed juvenile-onset severe biventricular failure, uncontrolled ventricular arrhythmia, progressive dilation, and required ventricular-assist-device implantation at 21 years. Both heterozygous parents were reportedly unaffected, supporting recessive severe disease for complete deficiency. (shiba2021phenotypicrecapitulationand pages 9-10, shiba2021phenotypicrecapitulationand pages 2-3)

Quality-of-life studies specific to DCM1BB were not found. Expected impacts include reduced exercise capacity, medication and surveillance burden, driving/employment restrictions after arrhythmia, ICD shocks, hospitalization, and advanced-HF disability. These are extrapolated from DCM/ACM rather than measured with EQ-5D or SF-36 in DCM1BB.

## 4. Genetic and molecular information

### Gene and protein

**DSG2** encodes desmoglein-2, a calcium-binding desmosomal cadherin enriched in myocardium. The protein spans extracellular cadherin domains, a transmembrane region, and a cytoplasmic region that participates in desmosomal assembly and linkage to plakoglobin/plakophilin/desmoplakin and the intermediate-filament cytoskeleton. (pinci2026integrativegenomicand pages 26-31, vencato2024animalmodelsand pages 1-2)

Suggested annotations include **GO:0007155 cell adhesion**, **GO:0098609 cell–cell adhesion**, **GO:0005916 fascia adherens**, **GO:0030057 desmosome**, **GO:0005911 cell–cell junction**, and **GO:0009986 cell surface**.

### Representative variants

- **NM_001943.5:c.355C>T, p.Arg119Ter (R119X):** stop-gain. Homozygosity caused complete DSG2 deficiency and severe juvenile biventricular cardiomyopathy. Heterozygous pathogenicity is less certain and may act as an incompletely penetrant risk/exacerbating allele. (shiba2021phenotypicrecapitulationand pages 2-3, sumida2024fourcardiomyopathypatients pages 1-2)
- **p.Phe531Cys (F531C; reported c.1592T>G):** homozygous missense variant in a five-generation family with eight affected members. The protein misfolded and activated ER-stress signaling in the corresponding knock-in model. (zhang2024hyperactivationofatf4tgfβ1 pages 1-2)
- **p.Asn266Ser:** experimentally associated with dose-dependent dominant-negative disease and provides foundational mechanistic evidence, although the retrieved primary support is mainly in the broader DSG2-ACM literature.
- Other reported truncating examples include **E418fsX419, G678fsX681, and Q558X**. (shiba2021phenotypicrecapitulationand pages 10-11)
- Copy-number variants and compound heterozygous combinations may be especially severe; complete deletion/splice combinations have been described in recessive early-onset ACM.

In the 2024 Japanese study, p.Arg119Ter had a worldwide gnomAD MAF of approximately **9.297×10⁻⁶**; reported counts included 9/44,826 East-Asian alleles and 6/1,179,852 non-Finnish European alleles. Japanese jMorp frequency was 7/108,574, approximately 6.9-fold above total gnomAD. Among 808 nonischemic-cardiomyopathy patients, four unrelated carriers produced a study allele frequency of 0.0037, described as over 50-fold above the general Japanese population. (sumida2024fourcardiomyopathypatients pages 1-2)

All known causal variants are **germline**; no somatic DSG2 mechanism is established for DCM1BB. Variant assertions should follow ACMG/AMP criteria with ClinGen disease-specific evidence, segregation, population frequency, transcript consequence, and functional studies. A VUS must not be used alone for predictive cascade testing or irreversible management decisions. Expanded testing from 48 to 299 genes in 225 panel-negative DCM patients produced many VUSs—186 in 127 patients—but only one newly found variant clearly explained phenotype, supporting focused use of robust genes and careful VUS interpretation. (stroeks2023diagnosticandprognostic pages 1-2)

### Epigenetics and structural abnormalities

No reproducible DCM1BB-specific DNA-methylation, histone, chromatin, aneuploidy, translocation, or inversion signature is established. DSG2 deletions/CNVs are relevant and require CNV-capable sequencing or array analysis. Epigenetic findings in generic DCM/ACM should not be entered as DCM1BB-specific without direct evidence.

## 5. Environmental information

There is no infectious agent, toxin, radiation exposure, or occupational exposure that independently causes DCM1BB. Viral myocarditis, alcohol, cocaine/amphetamines, anthracyclines, trastuzumab, nutritional deficiency, pregnancy, and autoimmune disease are clinically important triggers, modifiers, or differentials for a DSG2 carrier. The evidence for a direct DSG2-specific interaction is strongest for **mechanical load/endurance exercise**. (newman2024dilatedcardiomyopathya pages 1-2, gasior2024advancesincardiac pages 1-2, vencato2024animalmodelsand pages 1-2)

Smoking cessation, moderation/avoidance of alcohol, weight and blood-pressure control, vaccination and infection prevention, and avoidance of nonessential cardiotoxins follow general heart-failure prevention principles. They are sensible but not demonstrated as genotype-specific protective interventions.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A pathogenic germline DSG2 variant leads to** reduced, absent, mislocalized, structurally unstable, or misfolded desmoglein-2.
2. **Altered desmoglein-2 leads to** defective calcium-dependent desmosomal adhesion and disturbed assembly of the intercalated disc/area composita.
3. **Junctional disruption leads to** reduced mechanical cohesion during contraction and secondary abnormalities in desmocollin-2, desmoplakin, connexin-43, and electrical coupling; some channel effects remain inferred rather than demonstrated in every human genotype. (shiba2021phenotypicrecapitulationand pages 10-11, shiba2021phenotypicrecapitulationand pages 1-1, vencato2024animalmodelsand pages 1-2, sumida2024fourcardiomyopathypatients pages 1-2)
4. **Mechanical and electro-coupling failure leads to two interacting branches:**
   - **Branch A:** conduction slowing and heterogeneous propagation **lead to** ventricular ectopy, tachycardia, syncope, and sudden-death risk;
   - **Branch B:** mechanical stress and tissue fragility **lead to** cardiomyocyte apoptosis/necrosis and loss of contractile myocardium.
5. **Cardiomyocyte injury leads to** release of damage signals and cardiomyocyte-intrinsic NF-κB activation, which **results in** CCL2/CCR2-positive monocyte/macrophage recruitment and fibro-inflammatory crosstalk; this is strongly demonstrated in Dsg2 mice and supported in patient-derived iPSC-CMs. (chelko2024nfĸbsignalingdrives pages 1-2)
6. **In susceptible missense variants, DSG2 misfolding leads to** BiP recognition and ER stress, which **activates** PERK–ATF4 signaling; ATF4 **increases** cardiomyocyte TGF-β1, which **activates** fibroblasts by paracrine signaling. This branch is demonstrated for p.Phe531Cys/F531C and should not automatically be generalized to all variants. (zhang2024hyperactivationofatf4tgfβ1 pages 1-2)
7. **Inflammation, TGF-β signaling, and repair lead to** replacement/interstitial fibrosis and, in the ACM spectrum, possible fibrofatty remodeling. Wnt/β-catenin inhibition with Hippo and TGF-β activation is supported mainly by animal models and remains partly inferential for human DCM1BB. (zhang2024hyperactivationofatf4tgfβ1 pages 1-2, vencato2024animalmodelsand pages 1-2, chelko2024nfĸbsignalingdrives pages 1-2)
8. **Myocyte loss plus fibrosis leads to** reduced force, chamber dilation, neurohormonal activation, and progressive left- or biventricular systolic failure.
9. **Fibrosis and ventricular dilation further lead to** electrical heterogeneity, valvular regurgitation, thromboembolic risk, end-stage heart failure, transplantation/VAD requirement, or death.
10. **Endurance exercise and other hemodynamic stressors lead to** greater junctional load and can accelerate the electrical and structural branches in genetically susceptible individuals. (vencato2024animalmodelsand pages 1-2)

### Human tissue and cellular evidence

The p.Arg119Ter patient’s myocardium showed abnormal cytoplasmic deposition of desmosomal proteins, disrupted intercalated discs, vacuoles, and absent desmoglein-2 staining. Patient-derived iPSC-CMs reproduced abnormal excitation, disrupted desmosomes, tissue fragility, and weak force. Isogenic HDR correction restored DSG2 expression and improved force from approximately **49±6 to 86±1 μN** in engineered tissue, establishing causality at the cellular level. AAV-mediated DSG2 replacement also improved contraction. (shiba2021phenotypicrecapitulationand pages 10-11, shiba2021phenotypicrecapitulationand pages 2-3, shiba2021phenotypicrecapitulationand pages 1-1)

A direct abstract quotation is: **“Adeno-associated virus-mediated replacement of DSG2 significantly recovered the contraction force”** in patient-derived tissue rings. This is proof of concept, not evidence of human therapeutic safety or efficacy. (shiba2021phenotypicrecapitulationand pages 10-11)

### 2024 mechanistic advances

Zhang et al. connected DSG2 protein misfolding to fibrosis through **BiP–PERK–ATF4–TGF-β1**. Their abstract states: **“Increased ATF4 facilitated the expression of TGF-β1 in cardiomyocytes, thereby activating cardiac fibroblasts through paracrine signaling.”** Pharmacological/genetic pathway inhibition attenuated fibrosis and systolic dysfunction in knock-in mice. Published September 2024, DOI: https://doi.org/10.1186/s12916-024-03593-8. (zhang2024hyperactivationofatf4tgfβ1 pages 1-2)

Chelko et al. used genetic perturbation, single-nucleus RNA-seq, and CITE-seq in Dsg2-mutant mice. Their central result was that cardiomyocyte NF-κB mobilizes CCR2-positive macrophages, which mediate injury and arrhythmia; transcriptional changes involved cardiomyocytes, fibroblasts, and macrophages. Published April 2, 2024, DOI: https://doi.org/10.1172/JCI172014. This is advanced preclinical evidence, not yet a validated treatment pathway in people. (chelko2024nfĸbsignalingdrives pages 1-2)

Suggested GO terms include **GO:0007155 cell adhesion**, **GO:0007162 negative regulation of cell adhesion**, **GO:0008219 cell death**, **GO:0006915 apoptotic process**, **GO:0006954 inflammatory response**, **GO:0006955 immune response**, **GO:0062023 collagen-containing extracellular matrix organization**, **GO:0048771 tissue remodeling**, **GO:0030199 collagen fibril organization**, **GO:0034976 response to endoplasmic-reticulum stress**, **GO:0006986 response to unfolded protein**, **GO:0030511 positive regulation of TGF-β receptor signaling**, and **GO:0060048 cardiac muscle contraction**.

Suggested Cell Ontology annotations are **CL:0000746 cardiac muscle cell/cardiomyocyte**, **CL:0000057 fibroblast**, **CL:0000863 inflammatory macrophage**, **CL:0000235 macrophage**, **CL:0000576 monocyte**, **CL:0000775 neutrophil**, and cardiac conduction-system cardiomyocyte terms where supported.

## 7. Anatomical structures affected

The primary organ is the **heart** (**UBERON:0000948**), particularly ventricular myocardium (**UBERON:0002349 myocardium**), left ventricle (**UBERON:0002084**), right ventricle (**UBERON:0002080**), and interventricular/biventricular myocardium. Disease is not inherently lateralized. Intercalated discs and desmosomes are the principal subcellular sites; the ER is additionally implicated for misfolding variants. (zhang2024hyperactivationofatf4tgfβ1 pages 1-2, vencato2024animalmodelsand pages 1-2)

At tissue level, cardiomyocytes are primarily injured, with secondary activation of resident/recruited macrophages and cardiac fibroblasts. At organ level, advanced low-output failure can secondarily affect lungs, liver, kidneys, skeletal muscle, and brain through congestion, hypoperfusion, embolism, or arrhythmic syncope; these are complications rather than primary DSG2 targets.

Suggested GO cellular components are **GO:0030057 desmosome**, **GO:0030018 Z disc** where relevant, **GO:0005911 cell–cell junction**, **GO:0070161 anchoring junction**, **GO:0005783 endoplasmic reticulum**, **GO:0005886 plasma membrane**, and **GO:0030315 T-tubule** only if specifically demonstrated.

## 8. Temporal development

Onset ranges from juvenile to adult and may be insidious. A “concealed” electrical phase can precede overt dilation or systolic failure. Biallelic loss can present early and progress rapidly, whereas heterozygous carriers may remain asymptomatic for decades or develop arrhythmia, fibrosis, or systolic dysfunction later. The homozygous p.Arg119Ter patient was normal at birth, developed juvenile disease, and required VAD support by 21; this suggests postnatal mechanical load can expose deficient junctional reserve. (shiba2021phenotypicrecapitulationand pages 9-10, shiba2021phenotypicrecapitulationand pages 2-3)

A practical temporal model is: genotype-positive/phenotype-negative → early ECG or CMR abnormalities → ventricular arrhythmia and/or regional fibrosis → LV or biventricular dilation and systolic dysfunction → advanced HF, ICD therapies, VAD/transplantation, or death. Progression is variable and not inevitably linear.

Reverse remodeling can occur with guideline-directed HF therapy, but genetic myocardial substrate and scar may persist. There is no reliable spontaneous-remission rate for DCM1BB. Critical opportunities are presymptomatic cascade detection, avoidance of high-intensity exercise, treatment at the first evidence of ventricular dysfunction, and timely sudden-death risk assessment.

## 9. Inheritance and population

### Inheritance

Both **autosomal-dominant, incompletely penetrant** and **autosomal-recessive/biallelic severe** patterns occur across DSG2 cardiomyopathy. Monoallelic missense or truncating variants may act dominantly, sometimes with oligogenic or environmental modifiers. Homozygous or compound heterozygous loss-of-function variants can produce early, severe biventricular disease. (shiba2021phenotypicrecapitulationand pages 2-3, pinci2026integrativegenomicand pages 1-6, zhang2024hyperactivationofatf4tgfβ1 pages 1-2, sumida2024fourcardiomyopathypatients pages 1-2)

Penetrance is age-dependent and variable. A recent integrated DSG2 cohort estimated approximately **42% penetrance** among genotype-positive relatives; in 95 carriers, 13% had major ventricular arrhythmias, 3% underwent transplantation, and 3% died. These 2026 data are informative but postdate the user’s preferred 2023–2024 window and concern broader DSG2-ACM rather than DCM1BB alone. (pinci2026integrativegenomicand pages 1-6)

No convincing genetic anticipation is established. Germline mosaicism is biologically possible but not a defining feature. Founder effects may occur for individual variants, but no universal DCM1BB founder population is known. Consanguinity increases the likelihood of biallelic disease. Carrier frequency is variant- and ancestry-specific and cannot be inferred from DCM prevalence.

### Epidemiology

Subtype-specific incidence and prevalence are unknown. Broader modern DCM prevalence is approximately **1 in 220–250** (0.4–0.45%), with older incidence estimates around 6–8 per 100,000 person-years; these numbers must not be assigned directly to DCM1BB. In a UK Biobank CMR analysis, DCM prevalence was 1 in 220, 0.45% (95% CI 0.39–0.53%). Broader ACM prevalence is estimated at 1:2,000–1:5,000. (newman2024dilatedcardiomyopathya pages 1-2, vencato2024animalmodelsand pages 1-2)

No reliable DCM1BB sex ratio, age distribution, or geographic distribution exists. Male sex often increases penetrance and arrhythmic expression in desmosomal ACM generally, but a DSG2-specific quantitative estimate was not verified here.

## 10. Diagnostics

### Clinical evaluation

Diagnosis requires confirmation of the cardiomyopathy phenotype and exclusion of sufficient acquired causes. Recommended assessment includes:

1. Three-generation pedigree, personal history, exercise exposure, pregnancy, alcohol, cardiotoxic drugs, infection/myocarditis, and neuromuscular/cutaneous findings.
2. Physical examination and **12-lead ECG**.
3. **Ambulatory ECG/Holter** for premature ventricular complexes, nonsustained/sustained VT, and conduction disease.
4. **Transthoracic echocardiography** for LV/RV dimensions, ejection fraction, strain, valvular regurgitation, and hemodynamics.
5. **CMR** for chamber phenotype, function, edema, and late-gadolinium-enhancement fibrosis; contemporary reviews regard CMR as the reference noninvasive modality for scar and tissue phenotyping. (gasior2024advancesincardiac pages 1-2)
6. Laboratory testing: BNP/NT-proBNP, high-sensitivity troponin, complete blood count, electrolytes, renal/liver function, thyroid studies, iron indices, creatine kinase, and directed infectious/autoimmune/metabolic tests.
7. Exercise testing when clinically safe for functional and arrhythmic assessment, not to provoke maximal athletic exposure.
8. Endomyocardial biopsy only when myocarditis, infiltrative/storage disease, or another biopsy-actionable diagnosis is suspected; it is not routinely required for genetic DCM. (grasso2024thenew2023 pages 1-2)

### Genetic testing

A cardiomyopathy/arrhythmogenic-cardiomyopathy NGS panel containing **DSG2** and other robust genes is preferred, with deletion/duplication analysis. Testing should include genes for overlapping DCM/ACM phenotypes—at minimum major desmosomal genes and robust DCM genes—and must be coupled to genetic counseling. Genetic testing is considered a first-tier DCM investigation, but indiscriminately larger panels increase VUS burden more than diagnostic yield. (grasso2024thenew2023 pages 1-2, stroeks2023diagnosticandprognostic pages 1-2)

Single-gene DSG2 testing is reasonable when a known familial variant exists. WES/WGS is useful after a negative high-quality panel, in severe early-onset disease, consanguinity, suspected oligogenic disease, or when CNV/noncoding analysis is needed. WGS may detect structural and deep intronic variants but does not eliminate interpretation uncertainty. CMA can detect larger deletions but is not first-line for an isolated sequence-level disorder. Karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not routine unless another syndrome is suspected.

RNA sequencing from blood may be uninformative if DSG2 is poorly expressed; myocardial or iPSC RNA studies can clarify splicing but remain specialized. Proteomics, metabolomics, epigenomics, and liquid biopsy have no validated diagnostic role.

### Differential diagnosis

Exclude ischemic cardiomyopathy; myocarditis/sarcoidosis; alcohol or stimulant toxicity; anthracycline/trastuzumab injury; peripartum cardiomyopathy; tachycardia-mediated cardiomyopathy; valvular/hypertensive disease; congenital shunts; endocrine, iron, nutritional, mitochondrial, and neuromuscular disease; and other genetic cardiomyopathies such as TTN, LMNA, FLNC, RBM20, DSP, PKP2, DSC2, BAG3, DES, and PLN disease.

Family screening should combine cascade genetic testing for a confirmed P/LP familial variant with serial ECG, ambulatory monitoring, echocardiography, and selective CMR. A negative targeted familial test generally releases a relative from genotype-specific surveillance, whereas a VUS should not drive predictive testing.

## 11. Outcomes and prognosis

There are no robust 5- or 10-year survival estimates specific to DCM1BB. Outcomes range from lifelong phenotype negativity to sudden arrhythmic death or end-stage biventricular failure. Adverse features plausibly include biallelic/multilocus disease, early onset, ventricular arrhythmia, extensive CMR fibrosis, reduced LV/RV ejection fraction, recurrent myocarditis-like injury, high exercise exposure, and progressive HF. (pinci2026integrativegenomicand pages 1-6, zhang2024hyperactivationofatf4tgfβ1 pages 1-2, vencato2024animalmodelsand pages 1-2)

For broader nonischemic DCM, approximately 50% experienced life-threatening arrhythmia, unplanned cardiovascular hospitalization, or cardiovascular death over 12 years in one contemporary long-term dataset; 17% experienced death, transplantation, or VAD implantation over eight years in another. These are context estimates, not DCM1BB-specific. Pathogenic/likely pathogenic variants generally confer worse prognosis than gene-elusive DCM. (newman2024dilatedcardiomyopathya pages 1-2)

Morbidity includes exercise limitation, recurrent arrhythmia, ICD implantation and shocks, hospitalization, thromboembolism, progressive HF, VAD, and transplantation. Recovery of ejection fraction is possible with treatment, but treatment withdrawal is generally inappropriate in genetic DCM because relapse risk persists.

## 12. Treatment and current applications

### Current standard care

There is no approved DSG2-corrective therapy. Management follows DCM/HFrEF and ACM principles:

- **ARNI** sacubitril/valsartan or an ACE inhibitor/ARB; NCIT concept: angiotensin-receptor/neprilysin inhibitor or renin–angiotensin-system inhibitor.
- Evidence-based **beta-blocker**.
- **Mineralocorticoid-receptor antagonist** such as spironolactone or eplerenone.
- **SGLT2 inhibitor** such as dapagliflozin or empagliflozin.
- Loop diuretic for congestion.
- Anticoagulation for atrial fibrillation, intracardiac thrombus, or another standard indication—not solely for DSG2 status.
- Antiarrhythmics and catheter ablation for recurrent ventricular arrhythmia, recognizing recurrence can occur as disease progresses.
- **ICD** for secondary prevention and selected primary prevention based on ventricular function, scar, arrhythmic history, syncope, and overall genotype/phenotype risk.
- CRT for standard electrical/mechanical dyssynchrony indications.
- VAD and heart transplantation for refractory advanced HF.

No CPIC or PharmGKB genotype-guided dosing recommendation specific to DSG2 was identified. Treatment should be phenotype- and risk-guided rather than based on a DSG2 VUS.

### Lifestyle and rehabilitation

Competitive and high-intensity endurance exercise should generally be avoided in affected individuals and discussed cautiously in genotype-positive relatives. Stable patients may undertake individualized low-to-moderate activity through cardiology/cardiac-rehabilitation supervision; complete inactivity has its own harms. Sodium/fluid advice, vaccination, weight control, smoking cessation, and psychosocial support follow HF standards. (gasior2024advancesincardiac pages 1-2, vencato2024animalmodelsand pages 1-2)

### Experimental therapy

Human DSG2-deficient iPSC-CMs provide proof of concept for **HDR correction** and **AAV-mediated gene replacement**, with restoration of desmosomes, electrophysiology, tissue strength, and contractile force. These experiments support precision-therapy development but do not establish clinical feasibility, dosing, durability, immunogenicity, or safety. (shiba2021phenotypicrecapitulationand pages 10-11, shiba2021phenotypicrecapitulationand pages 2-3, shiba2021phenotypicrecapitulationand pages 1-1)

Potential preclinical targets include PERK–ATF4–TGF-β1, NF-κB/CCR2 macrophage signaling, Wnt/Hippo balance, connexin-43, and fibrosis pathways. The 2024 studies make ATF4/TGF-β1 and NF-κB/CCR2 especially compelling, but systemic immune or ER-stress inhibition could have substantial off-target effects. (zhang2024hyperactivationofatf4tgfβ1 pages 1-2, chelko2024nfĸbsignalingdrives pages 1-2)

No DSG2-specific interventional clinical trial was identified in the trial search. Current gene-therapy trials in ACM target **PKP2**, not DSG2; these demonstrate field momentum but should not be represented as DCM1BB treatments. Relevant field studies include NCT06109181 and NCT05885412 (PKP2 gene replacement), NCT05569356 (observational ACM study), and NCT06275893 (anti-inflammatory intervention). ClinicalTrials.gov URLs follow the form https://clinicaltrials.gov/study/NCT06109181.

## 13. Prevention

### Primary prevention

The germline variant cannot currently be prevented after conception. Reproductive options include preconception genetic counseling, partner testing when recessive disease is possible, preimplantation genetic testing for a known familial P/LP variant, and prenatal diagnosis after informed counseling. Population or newborn screening for DSG2 is not currently recommended.

### Secondary prevention

Cascade testing and longitudinal phenotyping are the most important preventive measures. Early ECG, Holter, echocardiography, and CMR can identify electrical disease, scar, or ventricular dysfunction before symptoms. Surveillance intervals should be individualized by age, genotype, family history, exercise, and prior findings.

### Tertiary prevention

Guideline-directed HF therapy, exercise restriction, ICD selection, arrhythmia treatment, vaccination, management of pregnancy risk, and timely referral for advanced HF reduce complications. There is no disease-specific vaccine or prophylactic medication. Genetic counseling should explain incomplete penetrance, variable expressivity, uncertain significance of many variants, and the possibility of biallelic or multilocus inheritance.

## 14. Other species and natural disease

Orthologous **Dsg2** is conserved across vertebrates, reflecting the conserved requirement for desmosomal adhesion in mechanically stressed tissues. Naturally occurring dilated or arrhythmogenic cardiomyopathy occurs in dogs and other mammals, but a verified naturally occurring DSG2-defined veterinary counterpart with breed/VBO identifier was not established from the retrieved evidence. No zoonotic transmission is possible because this is an inherited, noninfectious disorder.

Suggested taxa for experimental comparative annotation include **Homo sapiens, NCBI Taxon 9606** and **Mus musculus, NCBI Taxon 10090**. Orthologue-specific NCBI Gene identifiers should be retrieved directly from NCBI Gene before production ingestion rather than inferred here.

## 15. Model organisms and experimental systems

### Mouse models

Available models include homozygous and heterozygous knock-in mutants, cardiac-specific knockout, and variant-overexpression models. They reproduce combinations of cardiomyocyte death, inflammation, fibrosis, ventricular dilation, reduced function, conduction delay, ventricular arrhythmia, and premature death. (shiba2021phenotypicrecapitulationand pages 1-2, zhang2024hyperactivationofatf4tgfβ1 pages 1-2, chelko2024nfĸbsignalingdrives pages 1-2)

The **Dsg2F536C/F536C** knock-in model reproduces the human F531C family’s cardiac enlargement, biventricular fibrosis, and dysfunction and enabled transcriptomic and mass-spectrometric discovery of PERK–ATF4–TGF-β1 signaling. (zhang2024hyperactivationofatf4tgfβ1 pages 1-2)

The **Dsg2mut/mut** model supports single-cell resolution of cardiomyocyte–macrophage–fibroblast interactions. Blocking cardiomyocyte NF-κB or CCR2-positive-cell recruitment attenuated injury, demonstrating causal immune participation. (chelko2024nfĸbsignalingdrives pages 1-2)

Heterozygous Dsg2 mice have limited spontaneous phenotype but develop RV dilation, dysfunction, activation delay, and inducible arrhythmia after endurance training. This model is useful for incomplete penetrance and gene–environment studies. (vencato2024animalmodelsand pages 1-2)

Limitations include species differences in cardiac loading, electrophysiology, lifespan, allele dosage, and adipose remodeling. Complete DSG2 deficiency can have different developmental consequences in mice and humans; therefore, mouse rescue cannot be assumed to predict clinical efficacy. (shiba2021phenotypicrecapitulationand pages 9-10)

### Human cellular models

Patient-derived p.Arg119Ter iPSC-CMs and isogenic HDR-corrected controls are the most disease-specific platform. They reproduce abnormal excitation, desmosomal ultrastructure, reduced desmocollin-2, tissue fragility, and weak contraction, while correction or AAV replacement rescues key phenotypes. (shiba2021phenotypicrecapitulationand pages 10-11, shiba2021phenotypicrecapitulationand pages 4-5, shiba2021phenotypicrecapitulationand pages 1-1)

Limitations include fetal-like iPSC-CM maturation, absent systemic immunity and neurohormonal loading, variable cell composition, and short experimental duration. Three-dimensional tissues, electrical/mechanical conditioning, multicellular organoids, and isogenic controls improve relevance.

## Key 2023–2024 developments and authoritative interpretation

1. **December 20, 2024—p.Arg119Ter human cohort:** Four carriers among 808 nonischemic-cardiomyopathy patients demonstrated broad phenotypic expression and ultrastructural desmosomal disruption. The authors concluded that the allele may be a latent exacerbating factor rather than uniformly sufficient monoallelic disease. DOI: https://doi.org/10.1038/s41439-024-00304-w. Their abstract reports **“pale and fragmented desmosomes and widened gaps between intercalated discs.”** (sumida2024fourcardiomyopathypatients pages 1-2)
2. **September 2024—variant-specific fibrosis pathway:** F531C misfolding linked DSG2 to BiP/PERK/ATF4/TGF-β1 and paracrine fibroblast activation. DOI: https://doi.org/10.1186/s12916-024-03593-8. (zhang2024hyperactivationofatf4tgfβ1 pages 1-2)
3. **April 2, 2024—single-cell immune mechanism:** Cardiomyocyte NF-κB and recruited CCR2-positive macrophages were shown to drive injury and arrhythmia in Dsg2 mice. DOI: https://doi.org/10.1172/JCI172014. (chelko2024nfĸbsignalingdrives pages 1-2)
4. **June 5, 2024—model synthesis:** Contemporary review emphasized Wnt/β-catenin inhibition, Hippo/TGF-β activation, intercalated-disc biology, and exercise as an ACM accelerator. DOI: https://doi.org/10.3390/ijms25116208. (vencato2024animalmodelsand pages 1-2)
5. **2023–2024 clinical implementation:** ESC-informed practice now integrates deep phenotype, CMR, pedigree, and genetic testing, rather than using morphology or genotype alone. Large uncurated panels add VUSs with little incremental diagnostic yield. DOI: https://doi.org/10.1038/s41431-023-01384-y; https://doi.org/10.1093/eurheartjsupp/suae002; https://doi.org/10.3390/jcm13237166. (grasso2024thenew2023 pages 1-2, stroeks2023diagnosticandprognostic pages 1-2, gasior2024advancesincardiac pages 1-2)

## Evidence-quality assessment and major gaps

**Strongest disease-specific evidence:** human genotype–phenotype observations, myocardial pathology, p.Arg119Ter iPSC-CM disease reproduction, and isogenic correction. **Strong mechanistic but preclinical evidence:** Dsg2 knock-in/knockout mice, single-cell immune profiling, ER-stress signaling, and exercise loading. **Broader extrapolation:** prevalence, exercise-risk magnitude, HF outcomes, and treatment response are derived largely from general DCM or ACM.

Critical gaps are: no population prevalence for DCM1BB; no prospective DSG2-only natural-history cohort in the 2023–2024 literature; uncertain pathogenic sufficiency of many monoallelic variants; no validated DSG2-specific biomarker; sparse sex- and ancestry-stratified penetrance; no subtype-specific quality-of-life data; no approved molecular therapy; and no DSG2-targeted interventional trial. Consequently, knowledge-base entries should encode evidence provenance and avoid transferring generic ACM frequencies or mouse pathways to every DSG2 variant without qualification.

References

1. (OpenTargets Search: Dilated cardiomyopathy 1BB): Open Targets Query (Dilated cardiomyopathy 1BB, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (shiba2021phenotypicrecapitulationand pages 2-3): Mikio Shiba, Shuichiro Higo, Takumi Kondo, Junjun Li, Li Liu, Yoshihiko Ikeda, Yasuaki Kohama, Satoshi Kameda, Tomoka Tabata, Hiroyuki Inoue, Satoki Nakamura, Maki Takeda, Emiko Ito, Seiji Takashima, Shigeru Miyagawa, Yoshiki Sawa, Shungo Hikoso, and Yasushi Sakata. Phenotypic recapitulation and correction of desmoglein-2-deficient cardiomyopathy using human-induced pluripotent stem cell-derived cardiomyocytes. Human Molecular Genetics, 30:1384-1397, May 2021. URL: https://doi.org/10.1093/hmg/ddab127, doi:10.1093/hmg/ddab127. This article has 41 citations and is from a domain leading peer-reviewed journal.

3. (pinci2026integrativegenomicand pages 1-6): Serena Pinci, Rudy Celeghin, Marika Martini, Monica De Gaspari, Maria Bueno Marinas, Giulia Tosato, Francesca Dalla Zanna, Marco Cason, Ilaria Rigato, Gaetano Thiene, Stefania Rizzo, Domenico Corrado, Cristina Basso, Barbara Bauce, and Kalliopi Pilichou. Integrative genomic and literature assessment of desmoglein 2-related arrhythmogenic cardiomyopathy with italian cohort validation. Communications Medicine, Feb 2026. URL: https://doi.org/10.1038/s43856-026-01416-w, doi:10.1038/s43856-026-01416-w. This article has 1 citations and is from a peer-reviewed journal.

4. (zhang2024hyperactivationofatf4tgfβ1 pages 1-2): Baowei Zhang, Yizhang Wu, Chunjiang Zhou, Jiaxi Xie, Youming Zhang, Xingbo Yang, Jing Xiao, Dao Wu Wang, Congjia Shan, Xiujuan Zhou, Yaozu Xiang, and Bing Yang. Hyperactivation of atf4/tgf-β1 signaling contributes to the progressive cardiac fibrosis in arrhythmogenic cardiomyopathy caused by dsg2 variant. BMC Medicine, Sep 2024. URL: https://doi.org/10.1186/s12916-024-03593-8, doi:10.1186/s12916-024-03593-8. This article has 18 citations and is from a domain leading peer-reviewed journal.

5. (sumida2024fourcardiomyopathypatients pages 1-2): Takuya Sumida, Shou Ogawa, Shuichiro Higo, Yuki Kuramoto, Ryo Eto, Yoshihiko Ikeda, Congcong Sun, Junjun Li, Li Liu, Tomoka Tabata, Yoshihiro Asano, Mikio Shiba, Yasuhiro Akazawa, Daisuke Nakamura, Takafumi Oka, Tomohito Ohtani, and Yasushi Sakata. Four cardiomyopathy patients with a heterozygous dsg2 p.arg119ter variant. Human Genome Variation, Dec 2024. URL: https://doi.org/10.1038/s41439-024-00304-w, doi:10.1038/s41439-024-00304-w. This article has 2 citations.

6. (shiba2021phenotypicrecapitulationand pages 1-1): Mikio Shiba, Shuichiro Higo, Takumi Kondo, Junjun Li, Li Liu, Yoshihiko Ikeda, Yasuaki Kohama, Satoshi Kameda, Tomoka Tabata, Hiroyuki Inoue, Satoki Nakamura, Maki Takeda, Emiko Ito, Seiji Takashima, Shigeru Miyagawa, Yoshiki Sawa, Shungo Hikoso, and Yasushi Sakata. Phenotypic recapitulation and correction of desmoglein-2-deficient cardiomyopathy using human-induced pluripotent stem cell-derived cardiomyocytes. Human Molecular Genetics, 30:1384-1397, May 2021. URL: https://doi.org/10.1093/hmg/ddab127, doi:10.1093/hmg/ddab127. This article has 41 citations and is from a domain leading peer-reviewed journal.

7. (shiba2021phenotypicrecapitulationand pages 10-11): Mikio Shiba, Shuichiro Higo, Takumi Kondo, Junjun Li, Li Liu, Yoshihiko Ikeda, Yasuaki Kohama, Satoshi Kameda, Tomoka Tabata, Hiroyuki Inoue, Satoki Nakamura, Maki Takeda, Emiko Ito, Seiji Takashima, Shigeru Miyagawa, Yoshiki Sawa, Shungo Hikoso, and Yasushi Sakata. Phenotypic recapitulation and correction of desmoglein-2-deficient cardiomyopathy using human-induced pluripotent stem cell-derived cardiomyocytes. Human Molecular Genetics, 30:1384-1397, May 2021. URL: https://doi.org/10.1093/hmg/ddab127, doi:10.1093/hmg/ddab127. This article has 41 citations and is from a domain leading peer-reviewed journal.

8. (chelko2024nfĸbsignalingdrives pages 1-2): Stephen P. Chelko, Vinay R. Penna, Morgan Engel, Emily A. Shiel, Ann M. Centner, Waleed Farra, Elisa N. Cannon, Maicon Landim-Vieira, Niccole Schaible, Kory Lavine, and Jeffrey E. Saffitz. Nfĸb signaling drives myocardial injury via ccr2+ macrophages in a preclinical model of arrhythmogenic cardiomyopathy. The Journal of Clinical Investigation, Jul 2024. URL: https://doi.org/10.1172/jci183441, doi:10.1172/jci183441. This article has 48 citations.

9. (stroeks2023diagnosticandprognostic pages 1-2): Sophie L. V. M. Stroeks, Debby Hellebrekers, Godelieve R. F. Claes, Ingrid P. C. Krapels, Michiel H. T. M. Henkens, Maurits Sikking, Els K. Vanhoutte, Apollonia Helderman-van den Enden, Han G. Brunner, Arthur van den Wijngaard, and Job A. J. Verdonschot. Diagnostic and prognostic relevance of using large gene panels in the genetic testing of patients with dilated cardiomyopathy. European Journal of Human Genetics, 31:776-783, May 2023. URL: https://doi.org/10.1038/s41431-023-01384-y, doi:10.1038/s41431-023-01384-y. This article has 10 citations and is from a domain leading peer-reviewed journal.

10. (grasso2024thenew2023 pages 1-2): Maurizia Grasso, Davide Bondavalli, Viviana Vilardo, Claudia Cavaliere, Ilaria Gatti, Alessandro Di Toro, Lorenzo Giuliani, Mario Urtis, Michela Ferrari, Barbara Cattadori, Alessandra Serio, Carlo Pellegrini, and Eloisa Arbustini. The new 2023 esc guidelines for the management of cardiomyopathies: a guiding path for cardiologist decisions. European Heart Journal Supplements : Journal of the European Society of Cardiology, 26:i1-i5, Apr 2024. URL: https://doi.org/10.1093/eurheartjsupp/suae002, doi:10.1093/eurheartjsupp/suae002. This article has 18 citations.

11. (gasior2024advancesincardiac pages 1-2): Tomasz Gasior. Advances in cardiac imaging and genetic testing for diagnosis and risk stratification in cardiomyopathies: 2024 update. Journal of Clinical Medicine, 13:7166, Nov 2024. URL: https://doi.org/10.3390/jcm13237166, doi:10.3390/jcm13237166. This article has 12 citations.

12. (vencato2024animalmodelsand pages 1-2): Sara Vencato, Chiara Romanato, Alessandra Rampazzo, and Martina Calore. Animal models and molecular pathogenesis of arrhythmogenic cardiomyopathy associated with pathogenic variants in intercalated disc genes. Jun 2024. URL: https://doi.org/10.3390/ijms25116208, doi:10.3390/ijms25116208. This article has 10 citations.

13. (newman2024dilatedcardiomyopathya pages 1-2): Noah A. Newman and Michael A. Burke. Dilated cardiomyopathy: a genetic journey from past to future. International Journal of Molecular Sciences, 25:11460, Oct 2024. URL: https://doi.org/10.3390/ijms252111460, doi:10.3390/ijms252111460. This article has 28 citations.

14. (pinci2026integrativegenomicand pages 26-31): Serena Pinci, Rudy Celeghin, Marika Martini, Monica De Gaspari, Maria Bueno Marinas, Giulia Tosato, Francesca Dalla Zanna, Marco Cason, Ilaria Rigato, Gaetano Thiene, Stefania Rizzo, Domenico Corrado, Cristina Basso, Barbara Bauce, and Kalliopi Pilichou. Integrative genomic and literature assessment of desmoglein 2-related arrhythmogenic cardiomyopathy with italian cohort validation. Communications Medicine, Feb 2026. URL: https://doi.org/10.1038/s43856-026-01416-w, doi:10.1038/s43856-026-01416-w. This article has 1 citations and is from a peer-reviewed journal.

15. (shiba2021phenotypicrecapitulationand pages 9-10): Mikio Shiba, Shuichiro Higo, Takumi Kondo, Junjun Li, Li Liu, Yoshihiko Ikeda, Yasuaki Kohama, Satoshi Kameda, Tomoka Tabata, Hiroyuki Inoue, Satoki Nakamura, Maki Takeda, Emiko Ito, Seiji Takashima, Shigeru Miyagawa, Yoshiki Sawa, Shungo Hikoso, and Yasushi Sakata. Phenotypic recapitulation and correction of desmoglein-2-deficient cardiomyopathy using human-induced pluripotent stem cell-derived cardiomyocytes. Human Molecular Genetics, 30:1384-1397, May 2021. URL: https://doi.org/10.1093/hmg/ddab127, doi:10.1093/hmg/ddab127. This article has 41 citations and is from a domain leading peer-reviewed journal.

16. (shiba2021phenotypicrecapitulationand pages 1-2): Mikio Shiba, Shuichiro Higo, Takumi Kondo, Junjun Li, Li Liu, Yoshihiko Ikeda, Yasuaki Kohama, Satoshi Kameda, Tomoka Tabata, Hiroyuki Inoue, Satoki Nakamura, Maki Takeda, Emiko Ito, Seiji Takashima, Shigeru Miyagawa, Yoshiki Sawa, Shungo Hikoso, and Yasushi Sakata. Phenotypic recapitulation and correction of desmoglein-2-deficient cardiomyopathy using human-induced pluripotent stem cell-derived cardiomyocytes. Human Molecular Genetics, 30:1384-1397, May 2021. URL: https://doi.org/10.1093/hmg/ddab127, doi:10.1093/hmg/ddab127. This article has 41 citations and is from a domain leading peer-reviewed journal.

17. (shiba2021phenotypicrecapitulationand pages 4-5): Mikio Shiba, Shuichiro Higo, Takumi Kondo, Junjun Li, Li Liu, Yoshihiko Ikeda, Yasuaki Kohama, Satoshi Kameda, Tomoka Tabata, Hiroyuki Inoue, Satoki Nakamura, Maki Takeda, Emiko Ito, Seiji Takashima, Shigeru Miyagawa, Yoshiki Sawa, Shungo Hikoso, and Yasushi Sakata. Phenotypic recapitulation and correction of desmoglein-2-deficient cardiomyopathy using human-induced pluripotent stem cell-derived cardiomyocytes. Human Molecular Genetics, 30:1384-1397, May 2021. URL: https://doi.org/10.1093/hmg/ddab127, doi:10.1093/hmg/ddab127. This article has 41 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Dilated_Cardiomyopathy_1BB-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 50 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0062023` (obsolete collagen-containing extracellular matrix) (1 mention) - replaced by `GO:0031012`

49 of 50 terms resolved to a current term; the rest could not be looked up either way.