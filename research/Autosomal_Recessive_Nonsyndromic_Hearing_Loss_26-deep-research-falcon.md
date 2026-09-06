---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T23:48:21.755907'
end_time: '2026-09-03T23:55:28.697783'
duration_seconds: 426.94
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Autosomal Recessive Nonsyndromic Hearing Loss 26
  mondo_id: ''
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
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 1
  validator_version: 0.2.1
term_validation:
  total_terms: 20
  verified: 20
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
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_26-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 26
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 26** covering all of the
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
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 26
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 26** covering all of the
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


# Autosomal Recessive Nonsyndromic Hearing Loss 26 (DFNB26): Disease-Characteristics Report

## Executive summary and evidence limits

DFNB26 is an exceptionally rare Mendelian form of **prelingual, bilateral, severe-to-profound sensorineural hearing loss**. Current evidence is centered on one large consanguineous Pakistani pedigree, PK-2. The disease allele is homozygous **GAB1 c.347G>A, p.(Gly116Glu)**, a hypomorphic missense substitution in the pleckstrin-homology domain. A second locus, DFNM1, contains a dominant **METTL13 c.1631G>A, p.(Arg544Gln)** modifier that can suppress deafness in individuals homozygous for the GAB1 allele. Consequently, penetrance cannot be interpreted from GAB1 genotype alone in this family. Functional support comes from biochemical and cell assays, patient lymphoblastoid cells, zebrafish perturbation/rescue, mouse inner-ear localization, and more recent mouse cochlear single-cell data—not from a disease-specific mammalian knock-in model. (yousaf2018modifiervariantof pages 1-3, yousaf2018modifiervariantof pages 8-10, yousaf2018modifiervariantof pages 7-8, yousaf2018modifiervariantof pages 3-4)

| Evidence domain | DFNB26 finding | Evidence status | Source |
|---|---|---|---|
| Disease/locus | Autosomal recessive nonsyndromic hearing loss 26 (**DFNB26**), originally linked in Pakistani family PK-2 to a 1.5-cM interval at chromosome **4q31** | Demonstrated by human linkage and segregation | (yousaf2018modifiervariantof pages 1-3, yousaf2018modifiervariantof pages 3-4) |
| Causal variant | Homozygous **GAB1** transcript NM_207123 **c.347G>A, p.(Gly116Glu)**; affects a conserved residue in the pleckstrin-homology domain and was absent from the examined controls and 1000 Genomes, NHLBI-ESP, and ExAC | Demonstrated in one extended pedigree; functional evidence supports a hypomorphic allele | (yousaf2018modifiervariantof pages 7-8, yousaf2018modifiervariantof pages 3-4) |
| Phenotype | Prelingual, bilateral, severe-to-profound/profound sensorineural hearing loss without reported extra-auditory manifestations | Demonstrated clinically in PK-2; exact thresholds, ages, progression, and individual-level audiograms were not reported in the extracted evidence | (yousaf2018modifiervariantof pages 7-8, naz2020growthfactorand pages 21-23) |
| Genetic modifier | A dominant modifier at **DFNM1**, **METTL13 c.1631G>A, p.(Arg544Gln)**, was carried by normal-hearing individuals homozygous for GAB1 p.Gly116Glu; affected homozygotes lacked the modifier | Demonstrated by pedigree segregation; suppression supported experimentally. One extracted passage reports c.1634G>A, but the primary-study sequence-level result is c.1631G>A, so transcript-version verification is advisable | (yousaf2018modifiervariantof pages 1-3, yousaf2018modifiervariantof pages 7-8, yousaf2018modifiervariantof pages 3-4) |
| Molecular mechanism | GAB1 functions as an adaptor in **HGF–MET** signaling. p.Gly116Glu impairs PH-domain lipid-related function; affected lymphoblastoid cells showed selective **SPRY2** upregulation, and GAB1, METTL13, and SPRY2 formed a supported tripartite complex | GAB1 dysfunction and signaling dysregulation are experimentally supported; the complete cochlear chain from variant to hair-cell dysfunction is inferred rather than demonstrated | (yousaf2018modifiervariantof pages 8-10, yousaf2018modifiervariantof pages 6-7, mujtaba2015amutationof pages 4-6) |
| Evidence systems | Human linkage, exome sequencing, segregation, and lymphoblastoid-cell expression; biochemical lipid-binding and co-immunoprecipitation assays; COS-7 interaction assays; zebrafish morpholino/mRNA rescue; mouse inner-ear expression and colocalization; later mouse cochlear single-cell transcriptomic context | Mixed human, in vitro, zebrafish, mouse-localization, and transcriptomic evidence; no reported mammalian GAB1 p.Gly116Glu knock-in model | (yousaf2018modifiervariantof pages 1-3, yousaf2018modifiervariantof pages 8-10, yousaf2018modifiervariantof pages 6-7, faridi2024deafnessdfnb128associated pages 8-10) |
| Major data gaps | No replicated unrelated DFNB26 families, disease-specific prevalence/incidence, quantitative penetrance, carrier frequency, longitudinal natural history, validated prognostic biomarkers, DFNB26-specific therapy/trial, or definitive disease-specific mammalian model identified | Unavailable; mechanism, penetrance, and genotype–phenotype estimates remain constrained by a single pedigree | (yousaf2018modifiervariantof pages 1-3, yousaf2018modifiervariantof pages 7-8, naz2020growthfactorand pages 21-23) |


*Table: Compact summary of the human genetic, modifier, mechanistic, and model-system evidence for GAB1-related DFNB26. It distinguishes demonstrated findings from pathway-level inference and highlights the major knowledge gaps.*

**Evidence caveat.** No replicated unrelated DFNB26 families, disease-specific prevalence estimate, prospective natural-history cohort, or targeted clinical trial was identified. Many requested database fields therefore remain unknown rather than negative.

## 1. Disease information

### Definition

DFNB26 is an autosomal-recessive, nonsyndromic auditory disorder caused by biallelic pathogenic variation in **GAB1**, encoding GRB2-associated binding protein 1. The reported phenotype is prelingual, bilateral, severe-to-profound or profound sensorineural deafness without recognized extra-auditory manifestations. An authoritative growth-factor review describes GAB1 as a mediator of HGF and IGF1 signaling and lists the DFNB26 phenotype as “prelingual, bilateral, sensorineural, and profound.” (yousaf2018modifiervariantof pages 7-8, naz2020growthfactorand pages 21-23)

### Identifiers and synonyms

- **Preferred name:** autosomal recessive nonsyndromic hearing loss 26.
- **Synonyms:** DFNB26; deafness, autosomal recessive 26; GAB1-related nonsyndromic hearing loss; GAB1-associated profound deafness.
- **Locus:** chromosome **4q31**, initially delimited to approximately 1.5 cM.
- **OMIM:** DFNB26 is commonly catalogued as **OMIM #605428**; GAB1 is **OMIM *604439**. These identifiers should be verified against the live OMIM record before automated ingestion because OMIM was not directly available through the retrieval interface.
- **MONDO:** no confidently verified DFNB26-specific MONDO identifier was retrieved. The broader parent “hearing loss, autosomal recessive” is **MONDO:0019588**, but it is not equivalent to DFNB26. Open Targets did not return a specific GAB1–DFNB26 record in its top results, illustrating incomplete aggregation for this ultra-rare disorder. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss 26)
- **Orphanet:** no disease-specific Orpha code was verified.
- **ICD-10-CM:** no genotype-specific code; phenotype may be represented under **H90.3**, sensorineural hearing loss, bilateral.
- **ICD-11/MeSH:** use the relevant nonsyndromic/genetic sensorineural hearing-loss parent concept; no DFNB26-specific code was verified.

The evidence is principally **family-level research data**, not EHR-derived surveillance or an aggregated population registry. Whole-exome sequencing included six deaf relatives from six sibships, one normal-hearing nonpenetrant relative, and an unrelated normal control. (yousaf2018modifiervariantof pages 3-4)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The only reported disease allele is germline homozygous **GAB1 NM_207123:c.347G>A, p.(Gly116Glu)**. It affects a conserved residue in the GAB1 pleckstrin-homology domain and was absent from the examined Pakistani/Indian controls and from 1000 Genomes, NHLBI-ESP, and ExAC. Eight computational predictors called it damaging, while lipid-binding and zebrafish experiments supported a partial-loss-of-function, or hypomorphic, effect. (yousaf2018modifiervariantof pages 7-8, yousaf2018modifiervariantof pages 3-4)

### Genetic risk and protection

- **Primary risk:** inheritance of two GAB1 p.Gly116Glu alleles.
- **Family history/consanguinity:** recessive inheritance makes parental relatedness a major ascertainment factor. The discovery family was consanguineous.
- **Protective modifier:** heterozygous **METTL13 c.1631G>A, p.(Arg544Gln)** at DFNM1 behaved as a dominant suppressor. Normal-hearing relatives could be homozygous for GAB1 p.Gly116Glu if they carried this modifier; affected GAB1 homozygotes lacked it. Functional zebrafish rescue supported suppression. (yousaf2018modifiervariantof pages 1-3, yousaf2018modifiervariantof pages 8-10, yousaf2018modifiervariantof pages 3-4)
- **Nomenclature caution:** one extracted passage gave METTL13 c.1634G>A, but the primary sequence-level result was c.1631G>A/p.Arg544Gln. Transcript and genome-build normalization should precede database loading. (yousaf2018modifiervariantof pages 7-8, yousaf2018modifiervariantof pages 3-4)

No other validated susceptibility, protective, or modifier alleles are known specifically for DFNB26. There is no evidence for anticipation.

### Environmental factors and interactions

No noise, infection, drug, diet, smoking, alcohol, occupational exposure, or other environmental factor has been shown to cause or modify DFNB26. General ototoxic exposures may add acquired injury to genetically impaired hearing, but this is clinical precaution rather than a demonstrated DFNB26 gene–environment interaction. No infectious etiology applies.

## 3. Phenotypes

| Phenotype | Characteristics in DFNB26 | Suggested HPO term |
|---|---|---|
| Sensorineural hearing impairment | Primary clinical sign; bilateral | **HP:0000407**, sensorineural hearing impairment; **HP:0008619**, bilateral sensorineural hearing impairment |
| Severe-to-profound/profound hearing loss | Reported in affected PK-2 relatives; exact individual thresholds were unavailable in the extracted report | **HP:0012715**, severe hearing impairment; **HP:0012714**, profound hearing impairment |
| Prelingual onset | Present before speech acquisition; exact neonatal versus infant age was not reported | **HP:0000399**, prelingual sensorineural hearing impairment; consider **HP:0003577**, congenital onset only if confirmed for an individual |
| Nonsyndromic presentation | No extra-auditory manifestations reported | Encode absence cautiously; do not infer normality for every organ from incomplete examinations |
| Speech/language consequences | Expected with untreated prelingual profound loss, but not quantified in PK-2 | **HP:0000750**, delayed speech and language development, only when documented |

The hearing phenotype is described as severe-to-profound in the primary investigation and as profound in later summaries. Frequencies cannot be estimated beyond saying that hearing loss tracked GAB1 homozygosity in relatives lacking the suppressor. Exact audiograms, vestibular measurements, longitudinal progression, tinnitus, and quantitative speech outcomes were not available. (yousaf2018modifiervariantof pages 7-8, naz2020growthfactorand pages 21-23)

**Quality of life.** Disease-specific EQ-5D, SF-36, PROMIS, or hearing-related quality-of-life measurements have not been reported. Untreated prelingual profound hearing loss can materially affect spoken-language acquisition, education, communication, and social participation, but those generic consequences should not be stored as observed PK-2 outcomes.

## 4. Genetic and molecular information

- **Causal gene:** **GAB1**, GRB2-associated binding protein 1, OMIM *604439; chromosome 4q31. It encodes a cytoplasmic docking/adaptor protein downstream of receptor tyrosine kinases.
- **Disease variant:** NM_207123:c.347G>A, p.(Gly116Glu), missense, germline, homozygous in affected subjects; functionally characterized as hypomorphic. It lies in the pleckstrin-homology domain, affecting lipid-related membrane recruitment/function. (yousaf2018modifiervariantof pages 7-8, yousaf2018modifiervariantof pages 3-4)
- **Modifier gene:** **METTL13**, with c.1631G>A, p.(Arg544Gln) at DFNM1. The allele behaves dominantly as a suppressor rather than as the primary cause of DFNB26. (yousaf2018modifiervariantof pages 1-3, yousaf2018modifiervariantof pages 3-4)
- **Population frequency:** absent from the historical reference datasets and controls examined in the 2018 study. A contemporary gnomAD allele count/frequency was not retrieved and should be checked directly using a normalized transcript/genome coordinate.
- **ACMG/AMP classification:** the human segregation and functional evidence support pathogenicity, but a current ClinVar assertion was not verified. For knowledge-base purposes, record the published disease association and functional evidence separately from any unverified ClinVar classification.
- **Somatic status:** not applicable; this is a constitutional germline disorder.
- **Structural variants/chromosomal abnormalities:** none demonstrated. The 4q31 linkage interval is not itself a pathogenic copy-number change.
- **Epigenetics:** no DFNB26-specific methylation, chromatin, histone, or imprinting abnormality is known.

## 5. Environmental information

DFNB26 is genetically initiated. No toxin, radiation, pollution, occupation, lifestyle behavior, or pathogen has been causally associated with it. Standard hearing-conservation measures—avoiding excessive noise and unnecessary ototoxic medication, vaccination against preventable infections that can damage hearing, and prompt treatment of otitis—may preserve residual auditory function but do not prevent inheritance or reverse GAB1 dysfunction.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Homozygous GAB1 p.Gly116Glu alters the pleckstrin-homology domain**, which **leads to** reduced lipid-associated/membrane adaptor function; this hypomorphic effect is experimentally supported. (yousaf2018modifiervariantof pages 7-8, yousaf2018modifiervariantof pages 3-4)
2. Reduced GAB1 function **leads to** abnormal propagation/regulation of receptor-tyrosine-kinase signals, especially the **HGF–MET–GAB1 axis**; the pathway placement is established, whereas its exact magnitude in human cochlear cells is inferred. (naz2020growthfactorand pages 21-23, mujtaba2015amutationof pages 4-6)
3. Altered signaling **results in** dysregulation of downstream effectors. Patient lymphoblastoid cells showed more-than-twofold changes in several HGF/MET-pathway genes and selective **SPRY2 upregulation in deaf—but not modifier-protected—GAB1 homozygotes**. PI3K was upregulated in both affected and nonpenetrant groups, so PI3K expression alone does not explain penetrance. (yousaf2018modifiervariantof pages 6-7)
4. **Branch A—without the METTL13 suppressor:** abnormal GAB1–SPRY2 pathway regulation is inferred to **lead to** impaired development or maintenance of cochlear neural/strial/supporting-cell systems, which **results in** bilateral severe-to-profound sensorineural hearing loss.
5. **Branch B—with METTL13 p.Arg544Gln:** altered METTL13 action within a supported GAB1–METTL13–SPRY2 complex **leads to** normalization or compensation of critical signaling and **results in** preserved hearing despite GAB1 homozygosity. Human segregation demonstrates suppression, while the precise biochemical corrective step remains unresolved. (yousaf2018modifiervariantof pages 1-3, yousaf2018modifiervariantof pages 8-10, yousaf2018modifiervariantof pages 6-7)

### Pathways and cellular processes

Activated MET recruits GAB1/GRB2 and can engage **PI3K**, **PTPN11/SHP2**, **PTK2**, **STAT**, and RAS–RAF–MAPK/ERK signaling. These pathways regulate proliferation, survival, migration, morphogenesis, and tissue maintenance. Related HGF, MET, GAB1, and MAP3K1 deafness genes reinforce a shared auditory signaling network, but it is not established that every branch is abnormal in DFNB26 cochleae. (faridi2024deafnessdfnb128associated pages 1-2, mujtaba2015amutationof pages 4-6, naz2020growthfactorand pages 5-7)

Suggested terms include **GO:0007169** transmembrane receptor protein tyrosine kinase signaling; **GO:0008286** insulin receptor signaling pathway, where appropriate for GAB1; **GO:0048011** neurotrophin TRK receptor signaling; **GO:0043066** negative regulation of apoptotic process; **GO:0007165** signal transduction; **GO:0048870** cell motility; and **GO:0007420** brain development. Exact GAB1 annotations should be drawn from the current GO release rather than inferred wholesale from the pathway.

### Cell and anatomical context

Mouse immunolocalization found overlapping Gab1/Mettl13 expression in spiral ganglion neurons, cochlear sensory-neuron fibers, supporting cells, and vestibular/cochlear regions. A 2024 mouse cochlear single-cell/single-nucleus analysis provided newer pathway context: **Gab1, Hgf, and Map3k1** were detected in stria-vascularis marginal cells; **Met** in intermediate cells; pathway components also occurred in spiral ganglion neurons, with little expression in inner or outer hair cells in those datasets. This argues against assuming that DFNB26 is a hair-cell-autonomous disorder. (yousaf2018modifiervariantof pages 6-7, faridi2024deafnessdfnb128associated pages 8-10)

Suggested CL terms: **CL:0000210** photoreceptor-like sensory receptor cell is not recommended because it is too broad; use current ontology terms for **spiral ganglion neuron**, **inner-ear supporting cell**, **stria vascularis marginal cell**, and **stria vascularis intermediate cell** after ontology-browser verification. Suggested processes include neuronal signaling, epithelial morphogenesis, survival, and cochlear ion-homeostasis support.

### Molecular profiling and advanced technology

- **Transcript/expression:** patient lymphoblastoid-cell qPCR/expression comparisons implicated SPRY2 and other HGF/MET components. This is an accessible surrogate tissue, not direct human cochlea. (yousaf2018modifiervariantof pages 6-7)
- **Proteomics/interactome:** NanoSPD/co-immunoprecipitation and COS-7 assays supported association among GAB1, METTL13, and SPRY2; the disease and modifier substitutions did not simply abolish GAB1–METTL13 binding. (yousaf2018modifiervariantof pages 8-10, yousaf2018modifiervariantof pages 6-7)
- **Single-cell:** 2024 mouse cochlear data refined likely strial and neuronal cell contexts but did not directly profile DFNB26 tissue. (faridi2024deafnessdfnb128associated pages 8-10)
- **Metabolomics/lipidomics/spatial transcriptomics/CRISPR screens:** no disease-specific results found.
- **Immune, inflammatory, fibrotic, ischemic, or metabolic injury:** not demonstrated as central DFNB26 mechanisms.

## 7. Anatomical structures affected

- **Organ/system:** bilateral inner ear and auditory system; no demonstrated systemic organ disease.
- **Primary site:** cochlea (**UBERON:0001844**).
- **Relevant structures:** organ of Corti (**UBERON:0002227**, verify current release), spiral ganglion, stria vascularis, cochlear supporting tissues, and auditory nerve fibers.
- **Cellular compartments:** cytosol and plasma-membrane-associated signaling regions; GAB1’s PH domain mediates phospholipid-related localization. Suggested GO cellular-component terms include **GO:0005737 cytoplasm**, **GO:0005886 plasma membrane**, and receptor-signaling complexes where directly annotated.
- **Lateralization:** bilateral. No consistent asymmetry has been reported. (naz2020growthfactorand pages 21-23)

## 8. Temporal development

Onset is **prelingual** and likely congenital or very early childhood, but a precise birth-to-diagnosis interval was not reported. The available family data do not establish whether thresholds are stable or progressive. The condition should therefore be represented as chronic/lifelong severe auditory impairment, with progression coded **unknown**, not stable. There are no defined stages, spontaneous remissions, or episodic attacks.

The critical clinical period is early infancy and childhood, when auditory access is required for spoken-language development. Newborn detection, prompt etiologic testing, amplification, communication support, and timely cochlear-implant evaluation are therefore important even though no DFNB26-specific timing trial exists.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive at the GAB1 locus, complicated by dominant suppression at METTL13/DFNM1.
- **Recurrence risk:** if both parents carry the familial GAB1 allele, each pregnancy has a nominal 25% probability of GAB1 homozygosity, 50% carrier probability, and 25% probability of inheriting neither allele. Phenotypic risk may be lower when the protective METTL13 allele segregates; counseling requires joint two-locus analysis.
- **Penetrance:** incomplete when GAB1 is considered alone; apparently high among homozygotes lacking the modifier in PK-2, but no defensible percentage can be calculated from the extracted data.
- **Expressivity:** severe-to-profound/profound among affected relatives; broader variability is unknown.
- **Anticipation:** not expected or reported.
- **Germline mosaicism:** not reported; standard residual risk applies.
- **Founder effect/carrier frequency:** unknown. The allele was identified in one Pakistani family and absent from tested regional controls; that is insufficient to establish a founder mutation. (yousaf2018modifiervariantof pages 3-4)
- **Sex ratio:** no sex bias expected for an autosomal trait; disease-specific ratio unavailable.
- **Prevalence/incidence:** no cases-per-100,000 or annual incidence estimate exists. A 2024 Pakistani review reported more than 148 hearing-loss genes and 170 loci overall and 51 autosomal-recessive nonsyndromic genes identified in Pakistan; common genes explain over half of profound cases, while individually uncommon genes contribute under 2%. These are background statistics, not DFNB26 prevalence estimates. GAB1 remains an ultra-rare cause. (faridi2024deafnessdfnb128associated pages 1-2)

## 10. Diagnostics

### Clinical evaluation

1. Newborn physiologic screening with otoacoustic emissions and/or automated auditory brainstem response.
2. Diagnostic age-appropriate behavioral audiometry and frequency-specific auditory brainstem response to document bilateral sensorineural thresholds.
3. Tympanometry and otoscopy to exclude conductive disease; speech detection/perception testing when developmentally appropriate.
4. Vestibular assessment only if symptoms or implant planning warrant it; vestibular phenotype is not established.
5. Renal, ophthalmic, cardiac, or other syndromic testing should be driven by clinical findings rather than DFNB26 itself.

No blood chemistry, metabolite, protein biomarker, biopsy, or characteristic imaging sign diagnoses DFNB26. CT/MRI is used for cochlear-implant planning or suspected structural abnormalities, not molecular confirmation.

### Genetic testing strategy

- **First line:** a comprehensive hearing-loss panel that includes **GAB1**, copy-number analysis, and established differential genes such as GJB2/GJB6, SLC26A4, OTOF, STRC, TMC1, MYO15A, CDH23, TMPRSS3, and ancestry-relevant genes.
- **Familial variant testing:** targeted sequencing for GAB1 c.347G>A plus METTL13 c.1631G>A when the PK-2-associated alleles or pedigree linkage are relevant.
- **Exome/genome sequencing:** appropriate after a negative panel, in consanguineous families, or when modifier/digenic architecture is suspected. Segregation analysis is essential; the original discovery required exome sequencing plus linkage and family cosegregation. (yousaf2018modifiervariantof pages 1-3, yousaf2018modifiervariantof pages 3-4)
- **WGS:** potentially superior for regulatory, intronic, and structural variants, but no DFNB26-specific incremental yield has been quantified.
- **CMA/karyotype/FISH/mtDNA/repeat testing:** not routine for isolated DFNB26 unless phenotype or family history suggests another diagnosis.
- **RNA studies:** not standard clinically; lymphoblastoid-cell cDNA confirmed expression of the reported variants in research. (yousaf2018modifiervariantof pages 3-4)

### Differential diagnosis

The differential includes other congenital/prelingual AR nonsyndromic hearing losses, auditory neuropathy such as OTOF-related disease, enlarged-vestibular-aqueduct/SLC26A4 disease, congenital CMV, ototoxic exposure, and syndromic disorders whose non-auditory findings emerge later. DFNB26 is distinguished by biallelic pathogenic GAB1 variants with compatible segregation and, where relevant, METTL13 modifier status.

## 11. Outcome and prognosis

DFNB26 is not known to shorten life expectancy or cause disease-specific mortality. The principal morbidity is lifelong auditory disability and its communication, educational, and psychosocial consequences. Untreated sensory-neural function is not expected to recover spontaneously. Hearing technology can improve auditory access but does not restore normal GAB1 signaling.

No DFNB26-specific survival statistics, disability-adjusted life years, cochlear-implant speech scores, validated prognostic biomarkers, or recovery rates are available. Important practical prognostic variables are age at identification/intervention, hearing level, residual hearing, consistent device use, communication access, educational support, and implant candidacy—not the GAB1 genotype alone. METTL13 status is a biologically compelling penetrance marker but has been demonstrated in only one pedigree.

## 12. Treatment and real-world implementation

There is **no approved GAB1- or METTL13-directed pharmacotherapy**, no established pharmacogenomic rule, and no DFNB26-specific gene, RNA, cell, or immune therapy. The clinical-trial search found no relevant interventional DFNB26 trial.

Current care follows pediatric severe-to-profound hearing-loss practice:

- appropriately fitted **hearing aids** and verification of aided audibility;
- early auditory, speech-language, sign-language, and educational intervention according to family goals;
- remote-microphone and classroom-access technology;
- **cochlear implantation** when appropriately fitted hearing aids provide insufficient benefit;
- longitudinal audiology and device programming;
- family and psychosocial support.

Suggested NCIT concepts include **Hearing Aid Device**, **Cochlear Implantation**, **Speech and Language Therapy**, **Audiologic Rehabilitation**, and **Genetic Counseling**; exact NCIT identifiers should be resolved in the current NCI Thesaurus release.

Experimental HGF delivery has ameliorated chemically induced hearing impairment in rats, and HGF–MET signaling is an attractive pathway, but this neither demonstrates efficacy in DFNB26 nor justifies off-label pathway stimulation. MET signaling is pleiotropic and oncologically important, so nonspecific manipulation could carry substantial risk. (mujtaba2015amutationof pages 6-8, mujtaba2015amutationof pages 4-6)

## 13. Prevention

- **Primary prevention of inherited disease:** genetic counseling, partner testing where a familial allele is known, reproductive carrier testing, prenatal diagnosis, and preimplantation genetic testing for monogenic disease. Two-locus counseling should include METTL13 but should not assume complete protection outside PK-2.
- **Secondary prevention:** universal newborn hearing screening, rapid diagnostic audiology, molecular testing, and cascade testing of relatives.
- **Tertiary prevention:** early communication access, amplification/implantation, educational accommodations, and avoidance of additional noise or ototoxic injury.
- **Vaccination/public health:** routine immunization can prevent some acquired infectious hearing losses but does not prevent DFNB26.
- **Prophylactic medication:** none.

## 14. Other species and natural disease

No naturally occurring veterinary disorder attributable to an orthologous GAB1 DFNB26 allele was identified. Relevant orthologs include mouse **Gab1** (*Mus musculus*, NCBI Taxon **10090**) and zebrafish **gab1** (*Danio rerio*, NCBI Taxon **7955**). These systems support evolutionary conservation of developmental and receptor-signaling functions. There is no zoonotic or cross-species transmission because DFNB26 is inherited, not infectious.

## 15. Model organisms

### Zebrafish

Gab1 morpholino perturbation produced developmental phenotypes, and human GAB1/METTL13 mRNA experiments supported the hypomorphic disease allele and suppressor relationship. Coinjection experiments used 1,000 pg GAB1 and 250 pg METTL13 mRNA; suppressor METTL13 partially rescued the GAB1-associated phenotype. This is the strongest whole-organism functional evidence, but a morpholino developmental phenotype is not identical to human isolated deafness, and zebrafish lateral-line/inner-ear biology cannot establish human cochlear penetrance quantitatively. (yousaf2018modifiervariantof pages 8-10, yousaf2018modifiervariantof pages 3-4)

### Mouse

Mouse evidence is primarily expression/localization: Gab1 and Mettl13 overlap in spiral ganglion neurons, auditory nerve fibers, supporting cells, and other inner-ear structures. Later single-cell datasets place HGF–MET–GAB1-related components prominently in strial and neuronal populations. No reported Gab1 p.Gly116Glu knock-in mouse directly reproduces DFNB26. (yousaf2018modifiervariantof pages 6-7, faridi2024deafnessdfnb128associated pages 8-10)

### Cellular and biochemical systems

Patient lymphoblastoid cells enabled pathway-expression comparisons; COS-7 cells, NanoSPD, co-immunoprecipitation, and filopodial-tip assays supported GAB1–METTL13–SPRY2 interaction; lipid-binding assays supported PH-domain dysfunction. Limitations include non-cochlear cell context and uncertain correspondence between expression changes and auditory-cell physiology. (yousaf2018modifiervariantof pages 8-10, yousaf2018modifiervariantof pages 6-7)

## Recent developments and authoritative interpretation

The principal disease-defining study remains Yousaf et al., **March 2018**, *Journal of Clinical Investigation*, “Modifier variant of METTL13 suppresses human GAB1-associated profound deafness,” DOI: [10.1172/JCI97350](https://doi.org/10.1172/JCI97350). Its central finding was that a dominant METTL13 allele can suppress a recessive GAB1-associated phenotype, making DFNB26 a particularly clear human example of modified Mendelian penetrance. (yousaf2018modifiervariantof pages 1-3)

Recent 2024 work has refined context rather than changed the causal assignment. Faridi et al., published **27 June 2024**, placed GAB1/DFNB26 in a broader HGF–MET–GAB1–MAP3K1 deafness network and used mouse cochlear single-cell data to emphasize strial and spiral-ganglion expression rather than a simple hair-cell-only mechanism: [DOI 10.3390/genes15070845](https://doi.org/10.3390/genes15070845). (faridi2024deafnessdfnb128associated pages 1-2, faridi2024deafnessdfnb128associated pages 8-10) A 2024 review of Pakistani AR nonsyndromic hearing loss underscores how consanguineous pedigrees have enabled rare-gene discovery while showing that most individually uncommon genes each explain under 2% of cases; this supports describing DFNB26 as ultra-rare rather than assigning an unsupported prevalence. (faridi2024deafnessdfnb128associated pages 1-2)

## Knowledge-base conclusions

1. **High-confidence fields:** AR inheritance; GAB1; c.347G>A/p.Gly116Glu; prelingual bilateral severe-to-profound sensorineural hearing loss; 4q31; METTL13 p.Arg544Gln suppressor; HGF–MET adaptor-signaling involvement.
2. **Moderate-confidence mechanistic fields:** PH-domain hypomorphism, SPRY2 dysregulation, and a GAB1–METTL13–SPRY2 regulatory complex.
3. **Inference-only fields:** exact cochlear lesion, specific affected human cell type, pathway branch that directly causes auditory failure, and degree of protection conferred by METTL13 outside PK-2.
4. **Unavailable fields:** DFNB26-specific MONDO/Orpha verification, prevalence, incidence, carrier frequency, quantitative penetrance, audiometric progression, quality-of-life scores, treatment-response rates, prognostic biomarkers, natural veterinary disease, and targeted clinical trials.
5. **PMID note:** the retrieved full-text evidence exposed DOI records but not reliable PMIDs. PMIDs should therefore be resolved through PubMed by DOI before knowledge-base ingestion rather than guessed.

References

1. (yousaf2018modifiervariantof pages 1-3): Rizwan Yousaf, Zubair M. Ahmed, Arnaud P.J. Giese, Robert J. Morell, Ayala Lagziel, Alain Dabdoub, Edward R. Wilcox, Sheikh Riazuddin, Thomas B. Friedman, and Saima Riazuddin. Modifier variant of mettl13 suppresses human gab1–associated profound deafness. Mar 2018. URL: https://doi.org/10.1172/jci97350, doi:10.1172/jci97350. This article has 58 citations and is from a highest quality peer-reviewed journal.

2. (yousaf2018modifiervariantof pages 8-10): Rizwan Yousaf, Zubair M. Ahmed, Arnaud P.J. Giese, Robert J. Morell, Ayala Lagziel, Alain Dabdoub, Edward R. Wilcox, Sheikh Riazuddin, Thomas B. Friedman, and Saima Riazuddin. Modifier variant of mettl13 suppresses human gab1–associated profound deafness. Mar 2018. URL: https://doi.org/10.1172/jci97350, doi:10.1172/jci97350. This article has 58 citations and is from a highest quality peer-reviewed journal.

3. (yousaf2018modifiervariantof pages 7-8): Rizwan Yousaf, Zubair M. Ahmed, Arnaud P.J. Giese, Robert J. Morell, Ayala Lagziel, Alain Dabdoub, Edward R. Wilcox, Sheikh Riazuddin, Thomas B. Friedman, and Saima Riazuddin. Modifier variant of mettl13 suppresses human gab1–associated profound deafness. Mar 2018. URL: https://doi.org/10.1172/jci97350, doi:10.1172/jci97350. This article has 58 citations and is from a highest quality peer-reviewed journal.

4. (yousaf2018modifiervariantof pages 3-4): Rizwan Yousaf, Zubair M. Ahmed, Arnaud P.J. Giese, Robert J. Morell, Ayala Lagziel, Alain Dabdoub, Edward R. Wilcox, Sheikh Riazuddin, Thomas B. Friedman, and Saima Riazuddin. Modifier variant of mettl13 suppresses human gab1–associated profound deafness. Mar 2018. URL: https://doi.org/10.1172/jci97350, doi:10.1172/jci97350. This article has 58 citations and is from a highest quality peer-reviewed journal.

5. (naz2020growthfactorand pages 21-23): Sadaf Naz and Thomas B. Friedman. Growth factor and receptor malfunctions associated with human genetic deafness. Clinical Genetics, 97:138-155, Oct 2020. URL: https://doi.org/10.1111/cge.13641, doi:10.1111/cge.13641. This article has 17 citations and is from a peer-reviewed journal.

6. (yousaf2018modifiervariantof pages 6-7): Rizwan Yousaf, Zubair M. Ahmed, Arnaud P.J. Giese, Robert J. Morell, Ayala Lagziel, Alain Dabdoub, Edward R. Wilcox, Sheikh Riazuddin, Thomas B. Friedman, and Saima Riazuddin. Modifier variant of mettl13 suppresses human gab1–associated profound deafness. Mar 2018. URL: https://doi.org/10.1172/jci97350, doi:10.1172/jci97350. This article has 58 citations and is from a highest quality peer-reviewed journal.

7. (mujtaba2015amutationof pages 4-6): Ghulam Mujtaba, Julie M Schultz, Ayesha Imtiaz, Robert J Morell, Thomas B Friedman, and Sadaf Naz. A mutation of met, encoding hepatocyte growth factor receptor, is associated with human dfnb97 hearing loss. Journal of Medical Genetics, 52:548-552, May 2015. URL: https://doi.org/10.1136/jmedgenet-2015-103023, doi:10.1136/jmedgenet-2015-103023. This article has 49 citations and is from a domain leading peer-reviewed journal.

8. (faridi2024deafnessdfnb128associated pages 8-10): Rabia Faridi, Rizwan Yousaf, Sayaka Inagaki, Rafal Olszewski, Shoujun Gu, Robert Morell, Elizabeth Wilson, Ying Xia, Tanveer Qaiser, Muhammad Rashid, Cristina Fenollar-Ferrer, Michael Hoa, Sheikh Riazuddin, and Thomas Friedman. Deafness dfnb128 associated with a recessive variant of human map3k1 recapitulates hearing loss of map3k1-deficient mice. Genes, 15:845, Jun 2024. URL: https://doi.org/10.3390/genes15070845, doi:10.3390/genes15070845. This article has 3 citations.

9. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss 26): Open Targets Query (autosomal recessive nonsyndromic hearing loss 26, 37 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

10. (faridi2024deafnessdfnb128associated pages 1-2): Rabia Faridi, Rizwan Yousaf, Sayaka Inagaki, Rafal Olszewski, Shoujun Gu, Robert Morell, Elizabeth Wilson, Ying Xia, Tanveer Qaiser, Muhammad Rashid, Cristina Fenollar-Ferrer, Michael Hoa, Sheikh Riazuddin, and Thomas Friedman. Deafness dfnb128 associated with a recessive variant of human map3k1 recapitulates hearing loss of map3k1-deficient mice. Genes, 15:845, Jun 2024. URL: https://doi.org/10.3390/genes15070845, doi:10.3390/genes15070845. This article has 3 citations.

11. (naz2020growthfactorand pages 5-7): Sadaf Naz and Thomas B. Friedman. Growth factor and receptor malfunctions associated with human genetic deafness. Clinical Genetics, 97:138-155, Oct 2020. URL: https://doi.org/10.1111/cge.13641, doi:10.1111/cge.13641. This article has 17 citations and is from a peer-reviewed journal.

12. (mujtaba2015amutationof pages 6-8): Ghulam Mujtaba, Julie M Schultz, Ayesha Imtiaz, Robert J Morell, Thomas B Friedman, and Sadaf Naz. A mutation of met, encoding hepatocyte growth factor receptor, is associated with human dfnb97 hearing loss. Journal of Medical Genetics, 52:548-552, May 2015. URL: https://doi.org/10.1136/jmedgenet-2015-103023, doi:10.1136/jmedgenet-2015-103023. This article has 49 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_26-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.
