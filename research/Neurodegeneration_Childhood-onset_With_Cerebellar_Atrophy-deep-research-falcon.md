---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-31T20:43:38.373600'
end_time: '2026-08-31T20:54:54.510547'
duration_seconds: 676.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neurodegeneration Childhood-onset With Cerebellar Atrophy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 41
  verified: 41
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
  path: Neurodegeneration_Childhood-onset_With_Cerebellar_Atrophy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodegeneration Childhood-onset With Cerebellar Atrophy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodegeneration Childhood-onset With Cerebellar Atrophy** covering all of the
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
- **Disease Name:** Neurodegeneration Childhood-onset With Cerebellar Atrophy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodegeneration Childhood-onset With Cerebellar Atrophy** covering all of the
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


# Neurodegeneration, Childhood-Onset, with Cerebellar Atrophy (CONDCA): Disease-Characteristics Report

## Executive summary

CONDCA is an ultra-rare, usually infantile-onset, progressive autosomal-recessive neurodegenerative disorder caused by biallelic loss-of-function or damaging hypomorphic variants in **AGTPBP1**, which encodes cytosolic carboxypeptidase 1 (**CCP1/NNA1**). The best-established disease axis is cerebellar Purkinje-cell degeneration combined with spinal motor-neuron and peripheral motor-axon disease. The molecular lesion disrupts the neuronal “tubulin code”: loss of CCP1-mediated deglutamylation produces excessive, predominantly TTLL1-dependent tubulin polyglutamylation, reduced Δ2-tubulin formation, impaired axonal cargo transport, and selective neuronal degeneration. Human evidence remains limited to small case series and reports; no population prevalence, validated clinical criteria, approved disease-modifying therapy, or disease-specific interventional trial was identified. (shashi2018lossoftubulin pages 1-2, shashi2018lossoftubulin pages 2-4, bodakuntla2021distinctrolesof pages 1-2, magiera2018excessivetubulinpolyglutamylation pages 1-2)

| domain | best-supported finding | quantitative evidence | evidence type | key source/date |
|---|---|---|---|---|
| Identity / inheritance | CONDCA is a rare autosomal recessive neurodegenerative disease caused by biallelic AGTPBP1 (CCP1) variants; OMIM 618276 | Foundational cohort: 13 affected individuals from 10 unrelated families; later summaries cite ~18-20 reported patients | Human clinical-genetic cohort; disease database association | Shashi et al., *EMBO J* 2018, published 2018-11-12, DOI: https://doi.org/10.15252/embj.2018100540, PMID 30420557 (shashi2018lossoftubulin pages 1-2, shashi2018lossoftubulin pages 2-4); Open Targets EFO_0010256 (OpenTargets Search: Neurodegeneration childhood-onset with cerebellar atrophy) |
| Core phenotypes and frequencies | Early infantile/childhood-onset progressive neurologic disease with motor delay, hypotonia, weakness, cognitive impairment, cerebellar atrophy, and motor neuropathy/lower motor neuron involvement | Aggregated review of ~20 patients: motor delay 20/20; hypotonia 19/20; muscle weakness 16/18; cognitive delay 17/20; microcephaly 11/20; feeding difficulties 13/20; respiratory distress 9/20; cerebellar atrophy 18/20; corpus callosum dysplasia 6/20; muscle atrophy 9/18 | Human case-series synthesis from primary reports/review | Baltanás et al., *Biomedicines* 2021, DOI: https://doi.org/10.3390/biomedicines9091157 (baltanas2021thechildhoodonsetneurodegeneration pages 7-9, baltanas2021thechildhoodonsetneurodegeneration pages 9-10) |
| Natural history / onset | Onset is usually from birth to 20 months with progressive worsening; disease can be severe and fatal in childhood, though milder survivors exist | In the 2018 cohort, 6/13 had a fatal course; one summarized review reports 7/18 deaths; patient ages at presentation ranged from 7 months to 14 years in one review summary | Human cohort and review synthesis | Shashi et al. 2018 (shashi2018lossoftubulin pages 1-2); Baltanás et al. 2021 (baltanas2021thechildhoodonsetneurodegeneration pages 9-10, baltanas2021thechildhoodonsetneurodegeneration pages 6-7) |
| MRI / neurodiagnostics | Brain MRI most consistently shows cerebellar atrophy; corpus callosum abnormalities and microcephaly are frequent co-findings | Cerebellar atrophy in 18/20 in aggregated review; severe or moderate cerebellar atrophy shown across many individuals in foundational cohort | Human imaging evidence | Shashi et al. 2018 (shashi2018lossoftubulin pages 1-2, shashi2018lossoftubulin pages 2-4); Baltanás et al. 2021 (baltanas2021thechildhoodonsetneurodegeneration pages 7-9) |
| Electrophysiology / peripheral nerve | Disease affects cerebellum, spinal motor neurons, and peripheral nerves, typically with axonal motor neuropathy and denervation, while sensory involvement is less emphasized | Aggregated review: denervation 5/20, neurogenic changes 2/20, axonal motor neuropathy 5/20 | Human neurophysiology and pathology | Shashi et al. 2018 (shashi2018lossoftubulin pages 1-2); Baltanás et al. 2021 (baltanas2021thechildhoodonsetneurodegeneration pages 9-10, baltanas2021thechildhoodonsetneurodegeneration pages 7-9) |
| Molecular mechanism | AGTPBP1/CCP1 loss causes defective tubulin deglutamylation, reduced D2-tubulin generation, and excess tubulin polyglutamylation, linking microtubule PTM dysregulation to neurodegeneration | Human muscle biopsy showed polyglutamylated tubulin accumulation; missense mutants lacked detectable catalytic activity for D2-tubulin generation in cell assays | Human molecular pathology; cell-based functional evidence | Shashi et al. 2018, DOI above (shashi2018lossoftubulin pages 2-4) |
| Mechanistic downstream effects | Excess polyglutamylation impairs neuronal transport and is sufficient to drive neuron-autonomous degeneration; TTLL1 is a major pathogenic counter-enzyme in CCP1 deficiency | In mouse models, simultaneous TTLL1 loss fully rescued degeneration of selected neurons; transport defects affected multiple cargo classes in hippocampal neurons | Mouse genetics; cultured neuron experiments | Magiera et al., *EMBO J* 2018, DOI: https://doi.org/10.15252/embj.2018100440 (magiera2018excessivetubulinpolyglutamylation pages 1-2); Bodakuntla et al., *EMBO J* 2021, published 2021-07-26, DOI: https://doi.org/10.15252/embj.2021108498 (bodakuntla2021distinctrolesof pages 1-2) |
| Diagnostics | Whole-exome sequencing is the key diagnostic approach because phenotype overlaps other pediatric neurodegenerative/cerebellar atrophy disorders; segregation testing is used for confirmation | 2024 Egyptian WES cohort: 7 patients from 6 families overall; 2 AGTPBP1 cases identified; sequencing described at ~50x average coverage | Human diagnostic study | Ashaat et al., *Molecular Neurobiology* 2024, published online 2023-12-28, DOI: https://doi.org/10.1007/s12035-023-03866-y (ashaat2024thediagnosticvalue pages 1-2, ashaat2024thediagnosticvalue pages 7-10) |
| Variant spectrum | Reported AGTPBP1 disease variants include nonsense, frameshift, splice, deletion, and missense alleles; truncating genotypes trend more severe than some missense genotypes | Foundational cohort identified 6 loss-of-function and 6 missense variants; variants were absent or extremely rare in population databases (AF below 0.00005 in cited summary) | Human clinical-genetic and functional evidence | Shashi et al. 2018 (shashi2018lossoftubulin pages 2-4); Baltanás et al. 2021 (baltanas2021thechildhoodonsetneurodegeneration pages 6-7) |
| Expanded phenotypes | Phenotypic spectrum may extend beyond classic cerebellar atrophy/motor neuron disease to atypical imaging or systemic findings | 2021 report described 2 siblings with homozygous c.3293G>A and neurodegeneration without cerebellar atrophy; 2023 case reported homozygous c.2447A>C (p.Gln816Pro) with seizures, dystonia, dilated cardiomyopathy, and caudate/putaminal/cerebellar atrophy | Human case reports | Türay et al., *Neurogenetics* 2021, DOI: https://doi.org/10.1007/s10048-021-00643-8 (turay2021anovelpathogenic pages 1-2); Samur et al., *J Pediatr Neurol* 2023, DOI: https://doi.org/10.1055/s-0042-1749669 (samur2023childhoodonsetneurodegenerationwith pages 1-2) |
| Recent 2024 human developments | New AGTPBP1 cases continue to expand mutational and phenotypic spectrum in consanguineous families | Ashaat 2024 reported 2 homozygous AGTPBP1 variants in Egyptian patients: novel c.2650A>C (p.Thr884Pro), likely pathogenic; and c.1534A>G (p.Thr512Ala), classified as VUS in that paper; cohort age range 1.5-18 years, all families consanguineous | Human WES cohort | Ashaat et al. 2024 (ashaat2024thediagnosticvalue pages 10-11, ashaat2024thediagnosticvalue pages 1-2, ashaat2024thediagnosticvalue pages 7-10) |
| Prognosis | Prognosis is generally poor with severe disability, progressive neurologic decline, and childhood mortality, but expressivity is variable | 6/13 fatal in Shashi 2018; milder survivors included a 14-year-old with spastic-ataxic movement disorder and mild intellectual disability in the foundational cohort | Human cohort | Shashi et al. 2018 (shashi2018lossoftubulin pages 1-2, shashi2018lossoftubulin pages 2-4) |
| Treatment status | No approved disease-modifying therapy or disease-specific clinical trial was identified; management is currently supportive and genetics-guided | Clinical trial search found no relevant registered interventional trial; supportive treatment reversed cardiomyopathy in one 2023 case report, but not the neurologic disease | Clinical trial landscape; case report | ClinicalTrials search result (OpenTargets Search: Neurodegeneration childhood-onset with cerebellar atrophy); Samur et al. 2023 (samur2023childhoodonsetneurodegenerationwith pages 1-2) |
| Preclinical therapy signals (2025) | In the PCD mouse model, rhVEGF-B showed neuroprotective benefit, whereas rhIGF-1 did not under tested conditions | Abstract reports rhVEGF-B at moderate dosage "stopped the process of neuronal death" and restored motor, cognitive, and social functions; increased dosing was detrimental; rhIGF-1 showed no neuroprotective effect | Mouse preclinical therapeutic study | Pérez-Revuelta et al., *Int J Mol Sci* 2025, published 2025-01-10, DOI: https://doi.org/10.3390/ijms26020538 (perezrevuelta2025neuroprotectiveeffectsof pages 1-2, perezrevuelta2025neuroprotectiveeffectsof pages 4-7, perezrevuelta2025neuroprotectiveeffectsof pages 10-12, perezrevuelta2025neuroprotectiveeffectsof pages 19-20) |
| Model organism | The Purkinje cell degeneration (pcd) mouse is the best-established model and recapitulates cerebellar atrophy plus broader neurodegeneration; sheep are cited as having lower motor neuron-like disease with AGTPBP1 involvement | Mouse model shows Purkinje cell loss, cerebellar atrophy, peripheral nerve pathology, reduced motor neurons, excess polyglutamylation, and decreased D2-tubulin; review also cites ovine lower motor neuron disease | Mouse and comparative-animal evidence | Shashi et al. 2018 (shashi2018lossoftubulin pages 6-7); Baltanás et al. 2021 (baltanas2021thechildhoodonsetneurodegeneration pages 19-21, baltanas2021thechildhoodonsetneurodegeneration pages 21-22) |


*Table: This table condenses the strongest available evidence for AGTPBP1-related childhood-onset neurodegeneration with cerebellar atrophy across clinical, molecular, diagnostic, prognostic, and model-system domains. It is useful as a quick-reference scaffold for a fuller disease knowledge-base entry.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** Neurodegeneration, childhood-onset, with cerebellar atrophy.
* **Abbreviation:** CONDCA.
* **OMIM:** **618276**.
* **Defining gene:** **AGTPBP1**, also called **CCP1** or **NNA1**; Open Targets/EFO maps the disorder as **EFO:0010256** and identifies AGTPBP1 as the strongest associated target. The additional Open Targets association with ABHD12 reflects phenotypic/database overlap and should not be treated as a defining cause of AGTPBP1-related CONDCA. (OpenTargets Search: Neurodegeneration childhood-onset with cerebellar atrophy)
* **MONDO:** A precise MONDO accession was not confirmed in the retrieved evidence; it should therefore be left unresolved rather than inferred from OMIM/EFO cross-mapping.
* **Orphanet, MeSH, ICD-10/ICD-11:** No disease-specific codes were confirmed. Coding generally requires broader categories such as hereditary ataxia, neurodegenerative disease, cerebellar atrophy, or motor-neuron disease.
* **Synonyms:** AGTPBP1-related neurodegeneration; CCP1 deficiency; infantile-onset neurodegeneration due to CCP1 loss; childhood-onset neurodegeneration with cerebellar atrophy syndrome; AGTPBP1-related cerebellar degeneration and motor neuropathy.

This entry is an **aggregated disease-level synthesis**, not an individual EHR record. Its principal evidence consists of published patients, family studies, functional assays, and animal models. The landmark study identified 13 affected individuals from 10 unrelated families. Its abstract states: “We found biallelic rare and damaging variants in the gene encoding CCP1 in 13 individuals with infantile-onset neurodegeneration.” (shashi2018lossoftubulin pages 1-2)

## 2. Etiology, risk, and protective factors

### Causal factor

The established cause is **biallelic germline AGTPBP1 dysfunction**. Nonsense, frameshift, canonical splice, exon/gene-region deletion, and damaging missense alleles have been reported. Null alleles abolish functional CCP1; tested missense proteins were unstable and lacked detectable catalytic activity for Δ2-tubulin generation. This supports loss of function rather than gain of function or dominant-negative action. (shashi2018lossoftubulin pages 2-4)

### Genetic risk

* Having two pathogenic or likely pathogenic alleles is the principal risk factor.
* Consanguinity increases the probability of homozygosity but is not required. An aggregated series reported consanguinity in 14/19 assessed patients; the 2024 Egyptian cohort was entirely consanguineous. (baltanas2021thechildhoodonsetneurodegeneration pages 7-9, ashaat2024thediagnosticvalue pages 1-2)
* In the foundational series, disease alleles were absent or extremely rare in population databases, with reported allele frequencies below 0.00005. The probability of randomly observing the implicated biallelic genotypes from gnomAD frequencies was calculated as 3.08×10⁻⁶. (shashi2018lossoftubulin pages 1-2, shashi2018lossoftubulin pages 2-4)
* A preliminary genotype–phenotype trend suggests biallelic truncating alleles more often produce critically severe/fatal disease, whereas residual-function missense genotypes may be milder. Exceptions occur, so this is not a validated prognostic rule. (shashi2018lossoftubulin pages 2-4)

### Environmental, infectious, and lifestyle factors

No toxin, infection, radiation, occupation, diet, smoking, alcohol exposure, or other environmental cause has been demonstrated. No validated gene–environment interaction is known. Environmental or lifestyle modifiers remain speculative, particularly because intrafamilial variability can occur. (ashaat2024thediagnosticvalue pages 10-11)

### Protective factors

No protective human allele or environmental exposure has been established. **Ttll1 deletion** is strongly protective in CCP1-deficient mice, but this is an experimental genetic rescue, not a naturally occurring human protective factor. (bodakuntla2021distinctrolesof pages 1-2, magiera2018excessivetubulinpolyglutamylation pages 1-2)

## 3. Phenotypes

Reported frequencies vary because denominators combine small, incompletely phenotyped cohorts. The following estimates are best treated as provisional.

| Phenotype | Characteristics and approximate frequency | Suggested HPO term |
|---|---|---|
| Global motor delay | Usually begins in infancy; progressive; 20/20 in an aggregated summary | Global developmental delay, **HP:0001263**; Motor delay, **HP:0001270** |
| Hypotonia | Early, usually severe and progressive; 19/20 | Muscular hypotonia, **HP:0001252** |
| Muscle weakness/tetraparesis | 16/18; often generalized and function-limiting | Muscle weakness, **HP:0001324**; Tetraparesis, **HP:0002273** |
| Cognitive/developmental impairment | 17/20; ranges from mild intellectual disability to profound impairment or regression | Intellectual disability, **HP:0001249**; Developmental regression, **HP:0002376** |
| Cerebellar atrophy | Hallmark but not invariant; 18/20; may be early and progressive | Cerebellar atrophy, **HP:0001272** |
| Ataxia | Variable visibility because profound weakness may prevent walking | Cerebellar ataxia, **HP:0001251**; Gait ataxia, **HP:0002066** |
| Microcephaly | 11/20 | Microcephaly, **HP:0000252** |
| Feeding difficulty/failure to thrive | 13/20; clinically important aspiration/nutrition risk | Feeding difficulties, **HP:0011968**; Failure to thrive, **HP:0001508** |
| Respiratory insufficiency/distress | 9/20; likely related to neuromuscular weakness in severe disease | Respiratory insufficiency, **HP:0002093** |
| Muscle atrophy | 9/18; neurogenic pathology documented | Muscular atrophy, **HP:0003202** |
| Motor neuropathy/denervation | Axonal motor neuropathy 5/20; denervation 5/20; sensory involvement generally absent | Motor axonal neuropathy, **HP:0007002**; Areflexia, **HP:0001284** |
| Abnormal eye movements | Oculomotor apraxia, hypometric saccades, strabismus, or poor fixation; frequent but not universal | Oculomotor apraxia, **HP:0000657**; Abnormality of eye movement, **HP:0000496** |
| Spasticity/dystonia/tremor | Variable mixed upper- and lower-motor/cerebellar movement disorder | Spasticity, **HP:0001257**; Dystonia, **HP:0001332**; Tremor, **HP:0001337** |
| Corpus-callosum abnormality | Dysplasia/hypoplasia in approximately 6/20 | Abnormal corpus callosum morphology, **HP:0001273** |
| Seizures | Not a defining feature, but reported in expanded cases | Seizure, **HP:0001250** |
| Cardiomyopathy | One 2023 case had reversible dilated cardiomyopathy; association requires replication | Dilated cardiomyopathy, **HP:0001644** |

These frequencies derive from a synthesis in which motor delay was 20/20, hypotonia 19/20, weakness 16/18, cognitive delay 17/20, microcephaly 11/20, feeding difficulty 13/20, respiratory distress 9/20, cerebellar atrophy 18/20, and callosal dysplasia 6/20. (baltanas2021thechildhoodonsetneurodegeneration pages 7-9)

Quality of life has not been measured with EQ-5D, SF-36, PROMIS, or a CONDCA-specific instrument. Nevertheless, inability to walk independently, tetraparesis, feeding and respiratory dependence, visual/oculomotor impairment, contractures, and profound cognitive disability indicate major effects on mobility, self-care, communication, schooling, and caregiver burden. This is clinical inference from functional manifestations, not formal patient-reported-outcome evidence. (baltanas2021thechildhoodonsetneurodegeneration pages 9-10, ashaat2024thediagnosticvalue pages 7-10)

## 4. Genetic and molecular information

### Gene and protein

**AGTPBP1** lies at chromosome 9q21 and encodes CCP1, a cytosolic metallocarboxypeptidase. CCP1 removes glutamate residues from polyglutamate side chains on α/β-tubulin and removes gene-encoded C-terminal glutamates from detyrosinated α-tubulin to generate Δ2/Δ3 tubulin. Suggested annotations include **GO:0008237** metallopeptidase activity, **GO:0006508** proteolysis, **GO:0070507** regulation of microtubule cytoskeleton organization, and tubulin deglutamylation as the specific biological process. (shashi2018lossoftubulin pages 1-2, shashi2018lossoftubulin pages 2-4)

### Variant classes and selected variants

The foundational cohort identified six loss-of-function and six distinct missense alleles, including a deletion of upstream/N-terminal exons and the splice variant **c.2336-1G>T**, which activated a cryptic splice site, removed 29 nucleotides, and caused **p.Met780fs**. Variant segregation supported autosomal-recessive inheritance. (shashi2018lossoftubulin pages 2-4)

Additional reported variants include:

* **c.3293G>A, p.Ser1098Asn**: homozygous in two siblings with neurodegeneration but reportedly no cerebellar atrophy or lower-motor-neuron findings, illustrating phenotypic expansion. (turay2021anovelpathogenic pages 1-2)
* **c.2447A>C, p.Gln816Pro**: novel homozygous missense variant reported in 2023 with seizures, dystonia, dilated cardiomyopathy, and caudate, putaminal, and cerebellar atrophy; no homozygotes were reported in gnomAD v2.1.1. (samur2023childhoodonsetneurodegenerationwith pages 1-2)
* **c.2650A>C, p.Thr884Pro**: novel homozygous missense variant, classified likely pathogenic by the 2024 authors. (ashaat2024thediagnosticvalue pages 7-10)
* **c.1534A>G, p.Thr512Ala**: homozygous missense variant, classified as a VUS in the 2024 report; it should not be upgraded without additional evidence. (ashaat2024thediagnosticvalue pages 7-10)

The Ashaat paper contains an internal transcript/variant-label inconsistency elsewhere, describing **p.Gly884Arg** under another nucleotide representation. For knowledge-base curation, the original sequencing files/LOVD submission should be checked before harmonizing that record. (ashaat2024thediagnosticvalue pages 10-11, ashaat2024thediagnosticvalue pages 7-10)

All known disease-causing alleles are germline. No somatic CONDCA mechanism, pathogenic repeat expansion, mitochondrial-DNA lesion, recurrent aneuploidy, translocation, or inversion is established. The foundational series did include a homozygous genomic deletion, so copy-number analysis remains relevant. No validated modifier gene or disease-associated epigenetic signature has been reported.

## 5. Environmental information

CONDCA is a monogenic disorder. No causal toxin, pollutant, occupational exposure, radiation, dietary deficiency, infection, or lifestyle factor is known. Routine vaccination has no disease-specific preventive role, although standard immunization remains important because respiratory weakness may increase complications of infection. Evidence for environmental modulation is presently absent.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic damaging AGTPBP1 variants lead to** absent, unstable, truncated, or catalytically inactive CCP1 protein. (shashi2018lossoftubulin pages 2-4)
2. **Loss of CCP1 activity leads to** failure to shorten tubulin polyglutamate side chains and reduced conversion of detyrosinated α-tubulin to Δ2/Δ3 tubulin. (shashi2018lossoftubulin pages 1-2, shashi2018lossoftubulin pages 6-7)
3. **Continued TTLL-family glutamylase activity—especially TTLL1 on α-tubulin—leads to** excessive neuronal microtubule polyglutamylation. TTLL7 mainly modifies β-tubulin and does not drive the same CCP1-deficient degeneration. (bodakuntla2021distinctrolesof pages 1-2)
4. **Hyperglutamylated microtubules lead to** reduced axonal transport efficiency for mitochondria, lysosomes, LAMP1-positive endosomes, and BDNF vesicles; direct evidence comes from cultured neurons and mouse models, whereas its quantitative contribution in human neurons is inferred. (magiera2018excessivetubulinpolyglutamylation pages 1-2, baltanas2021thechildhoodonsetneurodegeneration pages 1-2)
5. **Transport failure and microtubule dysfunction lead to** impaired neuronal maintenance, organelle/axoplasmic disorganization, mitochondrial stress, and ultimately cell-autonomous degeneration. The exact death-signaling sequence in human CONDCA remains incompletely defined. (magiera2018excessivetubulinpolyglutamylation pages 1-2)
6. **Selective vulnerability leads to** early Purkinje-cell loss and later/parallel injury to spinal α-motor neurons and peripheral myelinated motor axons; other vulnerable populations in pcd mice include olfactory mitral, thalamic, retinal photoreceptor, and inferior olivary neurons. (baltanas2021thechildhoodonsetneurodegeneration pages 1-2, baltanas2021thechildhoodonsetneurodegeneration pages 9-10)
7. **Purkinje-cell loss leads to** cerebellar atrophy, ataxia, impaired motor learning, and likely cognitive/social cerebellar dysfunction. (perezrevuelta2025neuroprotectiveeffectsof pages 1-2)
8. **Motor-neuron and peripheral-axon loss leads to** hypotonia, weakness, areflexia, neurogenic muscle atrophy, contractures, tetraparesis, feeding difficulty, and respiratory compromise. (baltanas2021thechildhoodonsetneurodegeneration pages 9-10, shashi2018lossoftubulin pages 6-7)
9. **Axonal/myelin degeneration leads to** secondary macrophage/microglial activation and debris clearance; inflammation appears downstream rather than the initiating lesion. (shashi2018lossoftubulin pages 6-7)

### Evidence strength and rescue experiments

Human muscle biopsy demonstrated accumulation of polyglutamylated tubulin, and transfected patient missense proteins failed to generate detectable Δ2-tubulin. Thus, defective enzymatic activity is demonstrated in human-derived material/cell assays. (shashi2018lossoftubulin pages 2-4)

Causality of hyperglutamylation is strongest in mice: Purkinje-specific CCP1 loss caused cell-intrinsic degeneration, while simultaneous **Ttll1** deletion preserved Purkinje cells for up to 18 months. A later study showed that TTLL1, but not TTLL7, deletion prevented Purkinje-cell and peripheral myelinated-axon degeneration and increased mitochondrial motility. The primary study summarized its conclusion as: “Degeneration of selected neurons in CCP1-deficient mice can be fully rescued by simultaneous knockout of the counteracting polyglutamylase TTLL1.” (bodakuntla2021distinctrolesof pages 1-2, magiera2018excessivetubulinpolyglutamylation pages 1-2)

Suggested process terms include microtubule-based transport (**GO:0099111**), axonal transport (**GO:0098930**), regulation of microtubule polymerization/depolymerization, mitochondrial transport, neuron apoptotic process (**GO:0051402**), and neuroinflammatory response. Suggested cell types include Purkinje neuron (**CL:0000121**), motor neuron (**CL:0000100**), retinal photoreceptor (**CL:0000210**), skeletal muscle cell (**CL:0000188**), macrophage (**CL:0000235**), and microglial cell (**CL:0000129**).

### Omics and advanced technologies

No validated patient transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omics signature was identified. Current profiling is principally targeted immunoblotting, immunohistology, cell biology, and mouse genetics. Accordingly, omics biomarkers should be marked unavailable.

## 7. Anatomical structures affected

The primary system is the nervous system, involving both central and peripheral compartments.

* **Cerebellum**, especially Purkinje-cell layer and cerebellar vermis: suggested **UBERON:0002037** and Purkinje-cell layer term; disease is usually bilateral/diffuse rather than unilateral.
* **Spinal cord ventral horn** and α-motor neurons: suggested **UBERON:0002240** and ventral-horn annotation.
* **Peripheral motor nerves/myelinated axons**: reduced axon number and caliber, disorganized axoplasm, and secondary myelin abnormalities are demonstrated in mice. (shashi2018lossoftubulin pages 6-7)
* **Skeletal muscle**: secondary neurogenic atrophy with grouped fiber atrophy and fatty replacement, not a primary myopathy. (shashi2018lossoftubulin pages 2-4)
* **Corpus callosum/cerebrum/basal ganglia**: variably involved on MRI; caudate and putaminal atrophy were reported in the 2023 expanded case. (samur2023childhoodonsetneurodegenerationwith pages 1-2)
* **Retina/optic system**: photoreceptor degeneration is prominent in pcd mice; visual/optic dysfunction occurs in some human cases, but systematic prevalence is unknown. (baltanas2021thechildhoodonsetneurodegeneration pages 21-22, ashaat2024thediagnosticvalue pages 7-10)
* **Heart:** dilated cardiomyopathy is currently an isolated expanded-phenotype observation, not established routine organ involvement. (samur2023childhoodonsetneurodegenerationwith pages 1-2)

At the subcellular level, the principal compartment is the **microtubule cytoskeleton** (**GO:0015630**), with secondary involvement of axons, mitochondria, lysosomes/endosomes, Golgi apparatus, and vesicular-transport machinery. (magiera2018excessivetubulinpolyglutamylation pages 1-2, baltanas2021thechildhoodonsetneurodegeneration pages 18-19)

## 8. Temporal development

Onset is usually congenital-to-infantile, between birth and approximately 20 months, and is typically insidious rather than acute. Early hypotonia, delayed motor acquisition, abnormal eye movements, feeding difficulty, or microcephaly is followed by progressive weakness, cerebellar atrophy, neuropathy, spasticity/dystonia, contractures, respiratory impairment, and severe disability. (baltanas2021thechildhoodonsetneurodegeneration pages 9-10, baltanas2021thechildhoodonsetneurodegeneration pages 7-9)

There is no validated staging system. A practical descriptive framework is:

1. **Early/presymptomatic-developmental phase:** normal or mildly delayed initial development in some children.
2. **Early symptomatic phase:** hypotonia, motor delay, feeding or oculomotor abnormalities, emerging cerebellar atrophy.
3. **Progressive multisystem neurologic phase:** ataxia, weakness, motor neuropathy, regression, muscle wasting, spasticity/dystonia.
4. **Advanced phase:** loss/non-acquisition of ambulation, tetraparesis, contractures, nutritional and respiratory complications.

The course is chronic and usually progressive, not episodic or relapsing-remitting. Spontaneous neurologic remission has not been documented. The pcd mouse suggests an early pre-degenerative therapeutic window before Purkinje-cell death: cellular changes appear around postnatal days 15–18, with overt death from day 18 and very few Purkinje cells outside lobule X by day 40. Translation of that interval to humans is unknown. (perezrevuelta2025neuroprotectiveeffectsof pages 1-2)

## 9. Inheritance and population

Inheritance is autosomal recessive. For two confirmed heterozygous parents, each pregnancy has a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of a non-carrier. Both sexes are affected; no convincing sex bias is evident. One synthesis contained approximately equal numbers of females and males. (baltanas2021thechildhoodonsetneurodegeneration pages 6-7, baltanas2021thechildhoodonsetneurodegeneration pages 7-9)

Penetrance for clearly pathogenic biallelic null alleles appears high, but cannot be formally estimated. Expressivity is marked: the foundational cohort ranged from critically ill infants to a 14-year-old with spastic-ataxic movement disorder and mild intellectual disability. Anticipation is not expected, and no founder allele, germline-mosaicism rate, carrier frequency, ethnic predominance, incidence, or prevalence has been established. (shashi2018lossoftubulin pages 1-2, shashi2018lossoftubulin pages 2-4)

Published families originate from multiple regions, including Europe, the Middle East, North Africa, and Turkey, but this reflects ascertainment and consanguinity rather than established geographic enrichment. Reported case counts—roughly 20 in early syntheses plus subsequent reports—are too small to calculate cases per 100,000. (baltanas2021thechildhoodonsetneurodegeneration pages 6-7, ashaat2024thediagnosticvalue pages 1-2)

## 10. Diagnostics

### Clinical and laboratory evaluation

There are no consensus diagnostic criteria. Suspect CONDCA in an infant or child with progressive hypotonia/weakness, developmental delay or regression, cerebellar atrophy, areflexia or axonal motor neuropathy, especially after spinal muscular atrophy testing is negative or when upper-motor/cerebellar signs coexist.

Recommended work-up includes:

* Brain MRI with attention to cerebellum, vermis, corpus callosum, cerebral volume, and basal ganglia.
* Nerve conduction studies and EMG to identify predominantly axonal motor neuropathy/denervation.
* Swallowing, nutrition, respiratory function, and sleep assessment.
* Ophthalmology with ocular-motor examination; ERG/VEP when vision is impaired.
* EEG when seizures or regression occur.
* Echocardiography/ECG at baseline may be reasonable because cardiomyopathy has been reported, although evidence is insufficient for a formal surveillance guideline. (samur2023childhoodonsetneurodegenerationwith pages 1-2)
* CK and routine metabolic testing are mainly useful to exclude mimics; no diagnostic blood/urine metabolite or enzyme assay is validated.
* Muscle biopsy can show chronic denervation and tubulin hyperglutamylation, but is invasive and unnecessary when molecular diagnosis is available. (shashi2018lossoftubulin pages 2-4)

### Genetic testing strategy

1. **First tier:** trio WES or WGS, or a comprehensive childhood-onset ataxia/neurodegeneration/motor-neuropathy panel including **AGTPBP1**.
2. Confirm candidate variants by Sanger sequencing and parental segregation.
3. Ensure copy-number calling; if negative despite strong suspicion, use genome sequencing, exome-array CNV analysis, or targeted deletion/duplication testing because an AGTPBP1 genomic deletion is known.
4. RNA studies can clarify splice variants or deep-intronic candidates.
5. Reanalyse VUS periodically and do not diagnose from a single heterozygous allele without a second pathogenic allele or compelling functional evidence.

WES was particularly useful in the 2024 Egyptian series because clinical and MRI features overlapped several neurodegenerative disorders. The study sequenced seven patients from six families at approximately 50× mean coverage and found two homozygous AGTPBP1 genotypes. Its abstract reports: “Three novel variants were identified in three genes MFSD8, AGTPBP1, and APTX.” Published online 28 December 2023; 2024 volume; DOI: https://doi.org/10.1007/s12035-023-03866-y. (ashaat2024thediagnosticvalue pages 4-5, ashaat2024thediagnosticvalue pages 1-2, ashaat2024thediagnosticvalue pages 7-10)

CMA/karyotype/FISH are not routine first-line tests for classic CONDCA but may detect large deletions or alternative diagnoses. Mitochondrial-DNA and repeat-expansion testing are differential-diagnosis tools, not specific AGTPBP1 tests. No newborn screening assay is available.

### Differential diagnosis

Important alternatives include PCH-spectrum disorders, EXOSC3/VRK1/ASAH1-related motor-neuron disorders, SMA, PLA2G6-associated neurodegeneration, COASY/FA2H disorders, mitochondrial disease, congenital disorders of glycosylation, neuronal ceroid lipofuscinosis, AOA1/APTX, PNKP-related disease, and other hereditary ataxias/complex neuropathies. Cerebellar **atrophy** after postnatal degeneration, combined with motor neuropathy and biallelic AGTPBP1 variants, favors CONDCA over primary cerebellar hypoplasia. (ashaat2024thediagnosticvalue pages 10-11)

## 11. Outcome and prognosis

Prognosis is frequently poor but variable. Six of the 13 foundational patients had a fatal course; a later 18-patient synthesis recorded seven deaths. Severe truncating genotypes were enriched among critically ill/fatal cases, whereas some missense genotypes survived longer with less cognitive impairment. These observations are preliminary and not suitable for individual survival prediction. (baltanas2021thechildhoodonsetneurodegeneration pages 9-10, shashi2018lossoftubulin pages 1-2, shashi2018lossoftubulin pages 2-4)

No 5-year/10-year survival curves, median life expectancy, standardized mortality rate, or validated prognostic biomarker exists. Major morbidity includes severe motor disability, non-ambulation, feeding/aspiration problems, respiratory insufficiency, contractures/scoliosis, communication and cognitive impairment, and caregiver dependence. Recovery of lost neurologic function has not been demonstrated. Quality-of-life instruments have not been reported.

Potential adverse prognostic indicators are very early onset, biallelic truncating alleles, rapid regression, severe respiratory or bulbar involvement, and profound early cerebellar atrophy; all require validation.

## 12. Treatment and current applications

### Current care

No approved disease-modifying treatment exists. Management is multidisciplinary and supportive:

* Physical and occupational therapy, mobility aids, contracture prevention, orthoses, and scoliosis surveillance.
* Speech/augmentative communication and feeding therapy.
* Caloric support, swallow-safety management, and gastrostomy when indicated.
* Airway clearance, non-invasive ventilation, vaccination, and prompt respiratory-infection treatment.
* Standard antiseizure therapy when seizures occur; treatment should be phenotype- and EEG-guided.
* Standard management of dystonia/spasticity, pain, sleep disturbance, visual impairment, and cardiomyopathy.
* Palliative-care involvement for advanced disease.

Suggested NCIT intervention concepts include Physical Therapy, Occupational Therapy, Speech Therapy, Gastrostomy, Noninvasive Ventilation, Anticonvulsant Therapy, Genetic Counseling, and Palliative Care. Exact NCIT codes should be assigned from the current NCIT release rather than inferred.

### Experimental approaches

* **Reducing TTLL1-mediated polyglutamylation:** strongest target-validation evidence. Ttll1 deletion rescues Purkinje cells and peripheral axons in CCP1-deficient mice. No selective clinical TTLL1 inhibitor or human efficacy evidence is available. (bodakuntla2021distinctrolesof pages 1-2, magiera2018excessivetubulinpolyglutamylation pages 1-2)
* **rhVEGF-B:** a mouse study received 7 November 2024 and was published 10 January 2025. Moderate dosing improved motor behavior, normalized recognition memory and social preference, increased Purkinje-cell density, and delayed/partially inhibited apoptosis. Higher-frequency dosing was detrimental, indicating a narrow, inverted-U exposure response. These findings are preclinical and do not establish pediatric safety or efficacy. DOI: https://doi.org/10.3390/ijms26020538. The abstract states that moderate rhVEGF-B “stopped the process of neuronal death and restored motor, cognitive, and social functions,” but this wording refers to the **PCD mouse**, not treated patients. (perezrevuelta2025neuroprotectiveeffectsof pages 1-2, perezrevuelta2025neuroprotectiveeffectsof pages 10-12)
* **rhIGF-1:** daily P20–P30 administration did not improve motor, memory, social, or Purkinje-cell survival outcomes in the same model. Earlier schedules remain untested in that experiment. (perezrevuelta2025neuroprotectiveeffectsof pages 4-7, perezrevuelta2025neuroprotectiveeffectsof pages 19-20)
* **Minocycline, NMDA antagonism, cerebellar grafts, and bone-marrow-derived cells:** explored historically in pcd mice, with limited or surrogate effects; none is established for human CONDCA. (baltanas2021thechildhoodonsetneurodegeneration pages 18-19, baltanas2021thechildhoodonsetneurodegeneration pages 19-21)
* **Gene replacement/editing/RNA therapy:** biologically plausible for a recessive loss-of-function disorder but no human trial was identified in the searches used for this report.

No disease-specific ClinicalTrials.gov interventional study or NCT identifier was found. No CONDCA pharmacogenomic guideline, CPIC recommendation, combination regimen, response rate, or disease-specific adverse-event dataset exists.

## 13. Prevention

There is no lifestyle, vaccine, environmental, or drug-based primary prevention for a de novo family diagnosis. Effective genetic prevention options are:

* Carrier testing of relatives after familial variants are established.
* Cascade screening and reproductive genetic counseling.
* Prenatal diagnosis by chorionic-villus or amniotic-fluid testing.
* Preimplantation genetic testing for monogenic disease.
* Partner testing where a pathogenic AGTPBP1 allele is known.

Secondary prevention consists of early molecular diagnosis and prospective surveillance for feeding, respiratory, orthopedic, visual, seizure, and possibly cardiac complications. Tertiary prevention includes aspiration precautions, respiratory support, nutrition, rehabilitation, positioning, and contracture/scoliosis management. Population newborn screening is not justified because prevalence, screening performance, and effective presymptomatic therapy are unknown.

## 14. Other species and natural disease

* **Mouse, Mus musculus (NCBI Taxon 10090):** spontaneous or engineered Agtpbp1-deficient pcd alleles cause ataxia, Purkinje-cell degeneration, cerebellar atrophy, retinal degeneration, peripheral neuropathy, motor-neuron loss, and infertility. (shashi2018lossoftubulin pages 6-7)
* **Sheep, Ovis aries (NCBI Taxon 9940):** AGTPBP1 defects have been linked to a naturally occurring lower-motor-neuron-like disease, supporting evolutionary conservation of motor-neuron vulnerability. (baltanas2021thechildhoodonsetneurodegeneration pages 21-22)
* **Drosophila melanogaster (Taxon 7227), Caenorhabditis elegans (Taxon 6239), and zebrafish, Danio rerio (Taxon 7955):** ortholog perturbation has been used to study mitochondrial, ciliary, neuronal, or drug-response biology; these are models rather than confirmed naturally occurring veterinary CONDCA. (baltanas2021thechildhoodonsetneurodegeneration pages 21-22)

There is no zoonotic potential or cross-species transmission: CONDCA is inherited, not infectious. A veterinary breed-ontology identifier or breed-specific prevalence was not established.

## 15. Model organisms

The **pcd mouse** is the principal disease model. It reproduces the causal gene defect, tubulin hyperglutamylation, reduced Δ2-tubulin, cerebellar atrophy, Purkinje-cell loss, peripheral myelinated-axon degeneration, and spinal motor-neuron loss. It also permits temporal and cell-specific genetic manipulation. (shashi2018lossoftubulin pages 6-7)

Key model applications include:

* Testing cell autonomy with Purkinje-specific conditional knockout.
* Dissecting the tubulin code through Ccp1/Ttll1/Ttll7 compound mutants.
* Measuring transport of mitochondria and vesicular cargo in cultured neurons.
* Testing neuroprotective compounds and intervention timing.
* Studying downstream macrophage/microglial responses.

Limitations are substantial. Mouse Purkinje-cell degeneration is temporally compressed; human patients show wider genetic and clinical heterogeneity; respiratory, cognitive, and systemic manifestations are incompletely reproduced; dosing and blood–brain-barrier behavior differ; and rescue of mouse histology does not establish developmental recovery in children. The model is therefore highly informative mechanistically but only partially predictive therapeutically. (perezrevuelta2025neuroprotectiveeffectsof pages 1-2, magiera2018excessivetubulinpolyglutamylation pages 1-2)

## Recent developments and authoritative interpretation

The most important 2023–2024 developments were not new therapies, but **phenotypic and diagnostic expansion**. The 2023 report added a homozygous **p.Gln816Pro** case with basal-ganglia atrophy, seizures, dystonia, and reversible dilated cardiomyopathy. The 2024 Egyptian WES study added two homozygous AGTPBP1 genotypes and emphasized exome sequencing for phenotypically overlapping childhood cerebellar-atrophy syndromes. These reports strengthen the argument for broad sequencing rather than relying on a rigid “classic” phenotype. (samur2023childhoodonsetneurodegenerationwith pages 1-2, ashaat2024thediagnosticvalue pages 1-2, ashaat2024thediagnosticvalue pages 7-10)

Mechanistically, authoritative experimental work supports tubulin hyperglutamylation—not nonspecific neuroinflammation—as the upstream actionable lesion. Magiera and colleagues concluded that excessive polyglutamylation is a “cell-autonomous mechanism for neurodegeneration,” while the Shashi cohort linked this directly to human CCP1 deficiency. The most rational therapeutic directions are therefore early AGTPBP1 replacement or controlled reduction of TTLL1-dependent glutamylation. Both remain experimental, and intervention may need to precede irreversible Purkinje-cell and motor-neuron loss. (magiera2018excessivetubulinpolyglutamylation pages 1-2, shashi2018lossoftubulin pages 1-2)

## Evidence and data gaps

Reliable prevalence/incidence, longitudinal natural-history curves, complete variant penetrance, carrier frequencies, formal genotype–phenotype models, standardized quality-of-life outcomes, fluid biomarkers, patient omics, validated staging criteria, clinical guidelines, and controlled treatment studies are unavailable. Exact phenotype frequencies should be updated through an international registry using uniform HPO phenotyping, serial MRI, motor/respiratory scales, and centralized variant curation. The most urgent translational needs are a prospective natural-history cohort, pharmacodynamic biomarkers of tubulin polyglutamylation, and safety studies for gene replacement or TTLL1-directed therapy.

References

1. (shashi2018lossoftubulin pages 1-2): Vandana Shashi, Maria M Magiera, Dennis Klein, Maha Zaki, Kelly Schoch, Sabine Rudnik‐Schöneborn, Andrew Norman, Osorio Lopes Abath Neto, Marina Dusl, Xidi Yuan, Luca Bartesaghi, Patrizia De Marco, Ahmed A Alfares, Ronit Marom, Stefan T Arold, Francisco J Guzmán‐Vega, Loren DM Pena, Edward C Smith, Maja Steinlin, Mohamed OE Babiker, Payam Mohassel, A Reghan Foley, Sandra Donkervoort, Rupleen Kaur, Partha S Ghosh, Valentina Stanley, Damir Musaev, Caroline Nava, Cyril Mignot, Boris Keren, Marcello Scala, Elisa Tassano, Paolo Picco, Paola Doneda, Chiara Fiorillo, Mahmoud Y Issa, Ali Alassiri, Ahmed Alahmad, Amanda Gerard, Pengfei Liu, Yaping Yang, Birgit Ertl‐Wagner, Peter G Kranz, Ingrid M Wentzensen, Rolf Stucka, Nicholas Stong, Andrew S Allen, David B Goldstein, Benedikt Schoser, Kai M Rösler, Majid Alfadhel, Valeria Capra, Roman Chrast, Tim M Strom, Erik‐Jan Kamsteeg, Carsten G Bönnemann, Joseph G Gleeson, Rudolf Martini, Carsten Janke, and Jan Senderek. Loss of tubulin deglutamylase ccp1 causes infantile‐onset neurodegeneration. The EMBO Journal, Nov 2018. URL: https://doi.org/10.15252/embj.2018100540, doi:10.15252/embj.2018100540. This article has 152 citations.

2. (shashi2018lossoftubulin pages 2-4): Vandana Shashi, Maria M Magiera, Dennis Klein, Maha Zaki, Kelly Schoch, Sabine Rudnik‐Schöneborn, Andrew Norman, Osorio Lopes Abath Neto, Marina Dusl, Xidi Yuan, Luca Bartesaghi, Patrizia De Marco, Ahmed A Alfares, Ronit Marom, Stefan T Arold, Francisco J Guzmán‐Vega, Loren DM Pena, Edward C Smith, Maja Steinlin, Mohamed OE Babiker, Payam Mohassel, A Reghan Foley, Sandra Donkervoort, Rupleen Kaur, Partha S Ghosh, Valentina Stanley, Damir Musaev, Caroline Nava, Cyril Mignot, Boris Keren, Marcello Scala, Elisa Tassano, Paolo Picco, Paola Doneda, Chiara Fiorillo, Mahmoud Y Issa, Ali Alassiri, Ahmed Alahmad, Amanda Gerard, Pengfei Liu, Yaping Yang, Birgit Ertl‐Wagner, Peter G Kranz, Ingrid M Wentzensen, Rolf Stucka, Nicholas Stong, Andrew S Allen, David B Goldstein, Benedikt Schoser, Kai M Rösler, Majid Alfadhel, Valeria Capra, Roman Chrast, Tim M Strom, Erik‐Jan Kamsteeg, Carsten G Bönnemann, Joseph G Gleeson, Rudolf Martini, Carsten Janke, and Jan Senderek. Loss of tubulin deglutamylase ccp1 causes infantile‐onset neurodegeneration. The EMBO Journal, Nov 2018. URL: https://doi.org/10.15252/embj.2018100540, doi:10.15252/embj.2018100540. This article has 152 citations.

3. (bodakuntla2021distinctrolesof pages 1-2): Satish Bodakuntla, Xidi Yuan, Mariya Genova, Sudarshan Gadadhar, Sophie Leboucher, Marie‐Christine Birling, Dennis Klein, Rudolf Martini, Carsten Janke, and Maria M Magiera. Distinct roles of α‐ and β‐tubulin polyglutamylation in controlling axonal transport and in neurodegeneration. The EMBO Journal, Jul 2021. URL: https://doi.org/10.15252/embj.2021108498, doi:10.15252/embj.2021108498. This article has 70 citations.

4. (magiera2018excessivetubulinpolyglutamylation pages 1-2): Maria M Magiera, Satish Bodakuntla, Jakub Žiak, Sabrina Lacomme, Patricia Marques Sousa, Sophie Leboucher, Torben J Hausrat, Christophe Bosc, Annie Andrieux, Matthias Kneussel, Marc Landry, André Calas, Martin Balastik, and Carsten Janke. Excessive tubulin polyglutamylation causes neurodegeneration and perturbs neuronal transport. The EMBO Journal, Nov 2018. URL: https://doi.org/10.15252/embj.2018100440, doi:10.15252/embj.2018100440. This article has 183 citations.

5. (OpenTargets Search: Neurodegeneration childhood-onset with cerebellar atrophy): Open Targets Query (Neurodegeneration childhood-onset with cerebellar atrophy, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (baltanas2021thechildhoodonsetneurodegeneration pages 7-9): F Calvo Baltanás, MT Berciano, E Santos, and M Lafarga. The childhood-onset neurodegeneration with cerebellar atrophy (condca) disease caused by agtpbp1 gene mutations: the purkinje cell degeneration …. Unknown journal, 2021.

7. (baltanas2021thechildhoodonsetneurodegeneration pages 9-10): F Calvo Baltanás, MT Berciano, E Santos, and M Lafarga. The childhood-onset neurodegeneration with cerebellar atrophy (condca) disease caused by agtpbp1 gene mutations: the purkinje cell degeneration …. Unknown journal, 2021.

8. (baltanas2021thechildhoodonsetneurodegeneration pages 6-7): F Calvo Baltanás, MT Berciano, E Santos, and M Lafarga. The childhood-onset neurodegeneration with cerebellar atrophy (condca) disease caused by agtpbp1 gene mutations: the purkinje cell degeneration …. Unknown journal, 2021.

9. (ashaat2024thediagnosticvalue pages 1-2): Engy A. Ashaat, Hoda A. Ahmed, Nesma M. Elaraby, Alaaeldin Fayez, Ammal M. Metwally, Mona K. Mekkawy, Dalia Farouk Hussen, Neveen A. Ashaat, Rasha M. Elhossini, Heba Ahmed ElAwady, Randa H. A. Abdelgawad, Mona El Gammal, Mohamed Ahmed Al Kersh, and Dina Amin Saleh. The diagnostic value of whole-exome sequencing in a spectrum of rare neurological disorders associated with cerebellar atrophy. Molecular Neurobiology, 61:4949-4961, Dec 2024. URL: https://doi.org/10.1007/s12035-023-03866-y, doi:10.1007/s12035-023-03866-y. This article has 5 citations and is from a peer-reviewed journal.

10. (ashaat2024thediagnosticvalue pages 7-10): Engy A. Ashaat, Hoda A. Ahmed, Nesma M. Elaraby, Alaaeldin Fayez, Ammal M. Metwally, Mona K. Mekkawy, Dalia Farouk Hussen, Neveen A. Ashaat, Rasha M. Elhossini, Heba Ahmed ElAwady, Randa H. A. Abdelgawad, Mona El Gammal, Mohamed Ahmed Al Kersh, and Dina Amin Saleh. The diagnostic value of whole-exome sequencing in a spectrum of rare neurological disorders associated with cerebellar atrophy. Molecular Neurobiology, 61:4949-4961, Dec 2024. URL: https://doi.org/10.1007/s12035-023-03866-y, doi:10.1007/s12035-023-03866-y. This article has 5 citations and is from a peer-reviewed journal.

11. (turay2021anovelpathogenic pages 1-2): Sevim Türay, Recep Eröz, and A. Nazlı Başak. A novel pathogenic variant in the 3ʹ end of the agtpbp1 gene gives rise to neurodegeneration without cerebellar atrophy: an expansion of the disease phenotype? neurogenetics, 22:127-132, Apr 2021. URL: https://doi.org/10.1007/s10048-021-00643-8, doi:10.1007/s10048-021-00643-8. This article has 16 citations and is from a peer-reviewed journal.

12. (samur2023childhoodonsetneurodegenerationwith pages 1-2): Bahadir M. Samur, Gulhan A. Ercan-Sencicek, Ahmet Okay Caglayan, Huseyin Per, Hakan Gumus, Gulsum Gumus, and Ali Baykan. Childhood-onset neurodegeneration with cerebellar atrophy syndrome: severe neuronal degeneration and cardiomyopathy with loss of tubulin deglutamylase cytosolic carboxypeptidase 1. Aug 2023. URL: https://doi.org/10.1055/s-0042-1749669, doi:10.1055/s-0042-1749669. This article has 1 citations and is from a peer-reviewed journal.

13. (ashaat2024thediagnosticvalue pages 10-11): Engy A. Ashaat, Hoda A. Ahmed, Nesma M. Elaraby, Alaaeldin Fayez, Ammal M. Metwally, Mona K. Mekkawy, Dalia Farouk Hussen, Neveen A. Ashaat, Rasha M. Elhossini, Heba Ahmed ElAwady, Randa H. A. Abdelgawad, Mona El Gammal, Mohamed Ahmed Al Kersh, and Dina Amin Saleh. The diagnostic value of whole-exome sequencing in a spectrum of rare neurological disorders associated with cerebellar atrophy. Molecular Neurobiology, 61:4949-4961, Dec 2024. URL: https://doi.org/10.1007/s12035-023-03866-y, doi:10.1007/s12035-023-03866-y. This article has 5 citations and is from a peer-reviewed journal.

14. (perezrevuelta2025neuroprotectiveeffectsof pages 1-2): Laura Pérez-Revuelta, David Pérez-Boyero, Ester Pérez-Martín, Valeria Lorena Cabedo, Pablo González Téllez de Meneses, Eduardo Weruaga, David Díaz, and José Ramón Alonso. Neuroprotective effects of vegf-b in a murine model of aggressive neuronal loss with childhood onset. Jan 2025. URL: https://doi.org/10.3390/ijms26020538, doi:10.3390/ijms26020538. This article has 4 citations.

15. (perezrevuelta2025neuroprotectiveeffectsof pages 4-7): Laura Pérez-Revuelta, David Pérez-Boyero, Ester Pérez-Martín, Valeria Lorena Cabedo, Pablo González Téllez de Meneses, Eduardo Weruaga, David Díaz, and José Ramón Alonso. Neuroprotective effects of vegf-b in a murine model of aggressive neuronal loss with childhood onset. Jan 2025. URL: https://doi.org/10.3390/ijms26020538, doi:10.3390/ijms26020538. This article has 4 citations.

16. (perezrevuelta2025neuroprotectiveeffectsof pages 10-12): Laura Pérez-Revuelta, David Pérez-Boyero, Ester Pérez-Martín, Valeria Lorena Cabedo, Pablo González Téllez de Meneses, Eduardo Weruaga, David Díaz, and José Ramón Alonso. Neuroprotective effects of vegf-b in a murine model of aggressive neuronal loss with childhood onset. Jan 2025. URL: https://doi.org/10.3390/ijms26020538, doi:10.3390/ijms26020538. This article has 4 citations.

17. (perezrevuelta2025neuroprotectiveeffectsof pages 19-20): Laura Pérez-Revuelta, David Pérez-Boyero, Ester Pérez-Martín, Valeria Lorena Cabedo, Pablo González Téllez de Meneses, Eduardo Weruaga, David Díaz, and José Ramón Alonso. Neuroprotective effects of vegf-b in a murine model of aggressive neuronal loss with childhood onset. Jan 2025. URL: https://doi.org/10.3390/ijms26020538, doi:10.3390/ijms26020538. This article has 4 citations.

18. (shashi2018lossoftubulin pages 6-7): Vandana Shashi, Maria M Magiera, Dennis Klein, Maha Zaki, Kelly Schoch, Sabine Rudnik‐Schöneborn, Andrew Norman, Osorio Lopes Abath Neto, Marina Dusl, Xidi Yuan, Luca Bartesaghi, Patrizia De Marco, Ahmed A Alfares, Ronit Marom, Stefan T Arold, Francisco J Guzmán‐Vega, Loren DM Pena, Edward C Smith, Maja Steinlin, Mohamed OE Babiker, Payam Mohassel, A Reghan Foley, Sandra Donkervoort, Rupleen Kaur, Partha S Ghosh, Valentina Stanley, Damir Musaev, Caroline Nava, Cyril Mignot, Boris Keren, Marcello Scala, Elisa Tassano, Paolo Picco, Paola Doneda, Chiara Fiorillo, Mahmoud Y Issa, Ali Alassiri, Ahmed Alahmad, Amanda Gerard, Pengfei Liu, Yaping Yang, Birgit Ertl‐Wagner, Peter G Kranz, Ingrid M Wentzensen, Rolf Stucka, Nicholas Stong, Andrew S Allen, David B Goldstein, Benedikt Schoser, Kai M Rösler, Majid Alfadhel, Valeria Capra, Roman Chrast, Tim M Strom, Erik‐Jan Kamsteeg, Carsten G Bönnemann, Joseph G Gleeson, Rudolf Martini, Carsten Janke, and Jan Senderek. Loss of tubulin deglutamylase ccp1 causes infantile‐onset neurodegeneration. The EMBO Journal, Nov 2018. URL: https://doi.org/10.15252/embj.2018100540, doi:10.15252/embj.2018100540. This article has 152 citations.

19. (baltanas2021thechildhoodonsetneurodegeneration pages 19-21): F Calvo Baltanás, MT Berciano, E Santos, and M Lafarga. The childhood-onset neurodegeneration with cerebellar atrophy (condca) disease caused by agtpbp1 gene mutations: the purkinje cell degeneration …. Unknown journal, 2021.

20. (baltanas2021thechildhoodonsetneurodegeneration pages 21-22): F Calvo Baltanás, MT Berciano, E Santos, and M Lafarga. The childhood-onset neurodegeneration with cerebellar atrophy (condca) disease caused by agtpbp1 gene mutations: the purkinje cell degeneration …. Unknown journal, 2021.

21. (baltanas2021thechildhoodonsetneurodegeneration pages 1-2): F Calvo Baltanás, MT Berciano, E Santos, and M Lafarga. The childhood-onset neurodegeneration with cerebellar atrophy (condca) disease caused by agtpbp1 gene mutations: the purkinje cell degeneration …. Unknown journal, 2021.

22. (baltanas2021thechildhoodonsetneurodegeneration pages 18-19): F Calvo Baltanás, MT Berciano, E Santos, and M Lafarga. The childhood-onset neurodegeneration with cerebellar atrophy (condca) disease caused by agtpbp1 gene mutations: the purkinje cell degeneration …. Unknown journal, 2021.

23. (ashaat2024thediagnosticvalue pages 4-5): Engy A. Ashaat, Hoda A. Ahmed, Nesma M. Elaraby, Alaaeldin Fayez, Ammal M. Metwally, Mona K. Mekkawy, Dalia Farouk Hussen, Neveen A. Ashaat, Rasha M. Elhossini, Heba Ahmed ElAwady, Randa H. A. Abdelgawad, Mona El Gammal, Mohamed Ahmed Al Kersh, and Dina Amin Saleh. The diagnostic value of whole-exome sequencing in a spectrum of rare neurological disorders associated with cerebellar atrophy. Molecular Neurobiology, 61:4949-4961, Dec 2024. URL: https://doi.org/10.1007/s12035-023-03866-y, doi:10.1007/s12035-023-03866-y. This article has 5 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Neurodegeneration_Childhood-onset_With_Cerebellar_Atrophy-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.