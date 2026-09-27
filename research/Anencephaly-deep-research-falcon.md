---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T23:29:49.890578'
end_time: '2026-07-31T23:38:30.075260'
duration_seconds: 520.18
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Anencephaly
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Anencephaly-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Anencephaly
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Anencephaly** covering all of the
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
- **Disease Name:** Anencephaly
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Anencephaly** covering all of the
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


# Anencephaly: comprehensive disease-characteristics report

## Executive summary and evidence scope

Anencephaly is a congenital, open cranial neural-tube defect caused by failure of cranial neurulation during the first month after fertilization. It is characterized by partial or complete absence of the calvarium and destruction or absence of most of the brain. It is not compatible with prolonged survival: death occurs prenatally or usually within hours to days after birth. Most nonsyndromic cases are sporadic and multifactorial rather than attributable to one diagnostic gene. The best-supported model combines polygenic or oligogenic susceptibility with maternal nutrition, metabolic disease, medications, hyperthermia, and other environmental exposures. Human sequencing has implicated several pathways, especially non-canonical Wnt/planar-cell-polarity (PCP) signaling, but most reported variants remain susceptibility alleles or variants requiring additional evidence rather than universally causal mutations. (munteanu2020theetiopathogenicand pages 1-2, munteanu2020theetiopathogenicand pages 2-3, ishida2018atargetedsequencing pages 1-5)

The most effective intervention is **primary prevention before neural-tube closure**, especially periconceptional folic acid and population food fortification. Prenatal ultrasound permits early diagnosis but does not alter the malformation. There is no curative fetal surgery, pharmacotherapy, gene therapy, or postnatal repair for anencephaly. Much modern mechanistic and prevention literature reports neural-tube defects (NTDs) collectively; such findings should not automatically be encoded as anencephaly-specific.

## 1. Disease information

### Definition and classification

Anencephaly is defined morphologically by total or partial absence of the cranial vault and brain. Brainstem, cerebellar, and diencephalic remnants may persist; therefore, “complete absence of all neural tissue” is not required. Morphologic subdivisions include **meroacrania** (partial cranial defect), **holoacrania** (extensive cranial defect), and **holoacrania with rachischisis/craniorachischisis**. It belongs to the open NTD spectrum but must be distinguished from acalvaria, in which calvarial bones are absent while cerebral tissue is relatively preserved. (munteanu2020theetiopathogenicand pages 1-2)

A disease-specific review’s abstract states directly: **“Anencephaly is a severe malformation of the central nervous system … defined as total or partial absence of the calvarium, with absence of the brain.”** Published August 2020; DOI: [10.47162/rjme.61.2.03](https://doi.org/10.47162/rjme.61.2.03). (munteanu2020theetiopathogenicand pages 1-2)

### Identifiers and synonyms

* **MONDO:** Anencephaly; the exact current MONDO identifier should be verified against the live MONDO release before ingestion.
* **ICD-10-CM:** **Q00.0**, anencephaly.
* **ICD-10 category:** Q00, anencephaly and similar malformations.
* **ICD-11, Orphanet, OMIM, and MeSH:** use the current entries titled *Anencephaly*; exact release-specific identifiers were not established by the retrieved literature and should be verified directly rather than inferred.
* Common terms: **anencephalus, anencephalic fetus, congenital absence of brain and skull, cranial open neural-tube defect**. Exencephaly is the earlier exposed-brain phenotype that can undergo degeneration and become anencephaly; the terms are developmentally related but not exactly synonymous.

The report primarily summarizes **aggregated disease-level resources, reviews, population studies, and research cohorts**, not individual EHR records. The sequencing study comprised 85 anencephaly and five craniorachischisis cases. (ishida2018atargetedsequencing pages 1-5)

| Domain | Recommended identifier/ontology term | Meaning/use | Evidence caveat |
|---|---|---|---|
| Disease | MONDO: verify in source ontology | Preferred disease ontology anchor for anencephaly in cross-resource integration | Exact MONDO ID not confirmed from retrieved context; verify before database ingestion (munteanu2020theetiopathogenicand pages 1-2) |
| Disease | Orphanet: anencephaly — verify in source ontology | Rare-disease registry identifier for disease-level aggregation | Exact Orphanet code not confirmed in retrieved context; verify in Orphanet (munteanu2020theetiopathogenicand pages 1-2) |
| Disease | ICD-10: Q00.0 Anencephaly | Billing/classification code for congenital CNS malformation | Commonly used code; not directly confirmed in retrieved context, so verify against current ICD release (munteanu2020theetiopathogenicand pages 1-2) |
| Disease | ICD-11: verify in source ontology | International classification term for contemporary coding/interoperability | Exact ICD-11 stem code not confirmed from retrieved context; verify in WHO browser (munteanu2020theetiopathogenicand pages 1-2) |
| Disease | MeSH: Anencephaly (verify descriptor ID) | Literature indexing term for PubMed/biomedical retrieval | Descriptor name is standard; exact MeSH unique ID not confirmed here (munteanu2020theetiopathogenicand pages 1-2) |
| Disease concept | Open neural tube defect | High-level grouping used for etiologic and mechanistic aggregation | Much mechanistic evidence is NTD-wide rather than anencephaly-specific (avagliano2019overviewonneural pages 1-2, rai2023aquestfor pages 2-3) |
| Phenotype (HPO) | HP:0002323 Anencephaly | Core phenotype/disease-defining cranial neural tube closure defect | Primary phenotype; use as top phenotype assertion (munteanu2020theetiopathogenicand pages 1-2, ishida2018atargetedsequencing pages 1-5) |
| Phenotype (HPO) | HP:0000248 Microcephaly or verify more specific cranial-abnormality term | Differential/related cranial size abnormality in prenatal imaging/pathology context | Mentioned mainly for differential diagnosis; exact best-fit term should be curated (munteanu2020theetiopathogenicand pages 7-8) |
| Phenotype (HPO) | HP:0001363 Craniorachischisis | Associated severe open NTD phenotype/subclassification when present | Not present in all cases; use only where explicitly documented (munteanu2020theetiopathogenicand pages 1-2, ishida2018atargetedsequencing pages 1-5) |
| Phenotype (HPO) | HP:0000238 Hydrocephalus / verify relevance | Potential associated CNS phenotype in broader NTD contexts | Association is broader NTD-wide; not core to isolated anencephaly (avagliano2019overviewonneural pages 1-2) |
| Prenatal imaging sign | “Mickey Mouse” sign — verify ontology mapping | Useful prenatal ultrasound annotation for first-trimester detection | Imaging descriptor, not a standard disease ontology term (munteanu2020theetiopathogenicand pages 8-9) |
| Anatomy (UBERON) | UBERON:0000955 brain | Primary malformed/absent organ structure | Central anatomic entity for disease localization (munteanu2020theetiopathogenicand pages 1-2) |
| Anatomy (UBERON) | UBERON:0003129 calvaria | Absent/partially absent calvarium is part of defining morphology | Verify exact UBERON term label/version in target pipeline (munteanu2020theetiopathogenicand pages 1-2) |
| Anatomy (UBERON) | UBERON:0001049 neural tube | Embryonic structure whose cranial closure failure causes disease | Core developmental anatomy term (munteanu2020theetiopathogenicand pages 2-3, ishida2018atargetedsequencing pages 1-5) |
| Anatomy (UBERON) | UBERON:0001891 surface ectoderm / verify | Relevant tissue in neurulation and some model mechanisms | Stronger support from model systems than direct human pathology (avagliano2019overviewonneural pages 1-2) |
| Cell type (CL) | CL:0000031 neuroepithelial cell / verify | Principal embryonic cell population participating in neurulation | Exact CL mapping should be checked in target ontology version (avagliano2019overviewonneural pages 1-2, rai2023aquestfor pages 2-3) |
| Cell type (CL) | Neural fold cells — verify CL term | Developmentally relevant cells for cranial neural tube elevation/fusion | Often described anatomically/developmentally rather than by stable CL code (munteanu2020theetiopathogenicand pages 2-3, avagliano2019overviewonneural pages 1-2) |
| Biological process (GO) | GO:0001841 neural tube formation | Broad developmental process disrupted in anencephaly | High-confidence process-level annotation (munteanu2020theetiopathogenicand pages 2-3, avagliano2019overviewonneural pages 1-2) |
| Biological process (GO) | GO:0001838 embryonic epithelial tube formation / verify specificity | Supports morphogenetic framing of neurulation failure | Use if broader developmental annotation is desired; may be less specific (avagliano2019overviewonneural pages 1-2) |
| Biological process (GO) | GO:0035252 planar cell polarity pathway involved in neural tube closure / verify | Mechanistically relevant pathway implicated by human and animal studies | Exact GO child term should be verified; evidence mostly NTD-wide (munteanu2020theetiopathogenicand pages 2-3, rai2023aquestfor pages 2-3) |
| Biological process (GO) | Convergent extension — verify GO term | Key morphogenetic mechanism downstream of PCP/Wnt signaling | Strong mechanistic support, but usually broader NTD rather than isolated anencephaly (rai2023aquestfor pages 2-3) |
| Pathway | Non-canonical Wnt/planar cell polarity signaling | Important pathway for neurulation genes such as VANGL/CELSR | Pathway evidence is robust but not specific to every anencephaly case (munteanu2020theetiopathogenicand pages 2-3, rai2023aquestfor pages 2-3) |
| Gene-level annotation | MTHFR | Folate metabolism susceptibility gene frequently discussed in risk/prevention context | Association often based on polymorphism/risk studies, not monogenic causation (munteanu2020theetiopathogenicand pages 1-2, munteanu2020theetiopathogenicand pages 2-3) |
| Gene-level annotation | PDGFRA | Candidate/causal-susceptibility gene with rare damaging variants reported in anencephaly | Variant evidence comes from sequencing cohorts and likely oligogenic models (ishida2018atargetedsequencing pages 1-5) |
| Gene-level annotation | VANGL1 / VANGL2 / CELSR1 | PCP pathway genes implicated in neurulation defects | Often stronger in NTD-wide aggregation and model systems than isolated anencephaly-only cohorts (munteanu2020theetiopathogenicand pages 1-2, munteanu2020theetiopathogenicand pages 2-3, rai2023aquestfor pages 2-3) |
| Chemical (CHEBI) | CHEBI:27470 folic acid | Prevention exposure/intervention and nutrient ontology anchor | Central preventive chemical entity; exact CHEBI version should be checked (samaniegovaesken2024supplementationwithfolic pages 2-4, samaniegovaesken2024supplementationwithfolic pages 1-2) |
| Chemical (CHEBI) | folate / tetrahydrofolate derivatives — verify CHEBI term | Nutrient class for one-carbon metabolism annotations | Multiple related CHEBI entities exist; choose level appropriate to data model (samaniegovaesken2024supplementationwithfolic pages 2-4, samaniegovaesken2024supplementationwithfolic pages 1-2) |
| Chemical (CHEBI) | 5-methyltetrahydrofolate (5-MTHF) — verify CHEBI term | Alternative supplemental folate form discussed in recent literature | Evidence for equivalence to folic acid in prevention remains insufficient (samaniegovaesken2024supplementationwithfolic pages 2-4, samaniegovaesken2024supplementationwithfolic pages 1-2) |
| Exposure/risk | Valproic acid — map to CHEBI/Drug ontology in implementation | Major teratogenic exposure/risk factor to capture in exposure model | Evidence is NTD-wide; not unique to anencephaly (munteanu2020theetiopathogenicand pages 2-3, rai2023aquestfor pages 2-3) |
| Exposure/risk | Maternal diabetes / obesity / hyperthermia | Key maternal risk factor concepts for epidemiology and prevention annotations | These are clinical exposure concepts rather than disease ontology IDs here (munteanu2020theetiopathogenicand pages 2-3, rai2023aquestfor pages 2-3) |
| Intervention (NCIT) | NCIT: folic acid supplementation — verify exact NCIT code | Primary prevention intervention for at-risk or general reproductive-age populations | Exact NCIT code not confirmed; term should be checked in NCIt browser (samaniegovaesken2024supplementationwithfolic pages 2-4, samaniegovaesken2024supplementationwithfolic pages 1-2) |
| Intervention (NCIT) | Prenatal ultrasonography — verify exact NCIT code | Main diagnostic/screening intervention, especially first trimester | Exact NCIT code not confirmed; disease detection evidence strong (munteanu2020theetiopathogenicand pages 1-2, munteanu2020theetiopathogenicand pages 7-8) |
| Intervention (NCIT) | Maternal serum alpha-fetoprotein measurement — verify exact NCIT code | Ancillary prenatal screening biomarker test | Less specific than ultrasound; exact NCIT code should be verified (munteanu2020theetiopathogenicand pages 1-2) |
| Intervention (NCIT) | Pregnancy termination counseling/management — verify exact NCIT concept | Real-world management consequence after prenatal diagnosis of lethal anomaly | Sensitive management domain; terminology should follow local governance and ontology policy (munteanu2020theetiopathogenicand pages 7-8) |
| Public health | Mandatory folic acid food fortification | Population-level primary prevention implementation concept | Strong NTD-prevention evidence, but policy effect is usually reported for combined spina bifida/anencephaly burden (munteanu2020theetiopathogenicand pages 2-3, samaniegovaesken2024supplementationwithfolic pages 2-4) |
| Data provenance | Aggregated disease-level resource | Most current information comes from literature reviews, sequencing cohorts, and public-health studies rather than individual-patient EHR data | Distinguish curated disease knowledge from case-level records in KB design (munteanu2020theetiopathogenicand pages 1-2, ishida2018atargetedsequencing pages 1-5, samaniegovaesken2024supplementationwithfolic pages 2-4) |


*Table: This table provides a compact, database-oriented set of recommended identifiers and ontology terms for representing anencephaly across disease, phenotype, anatomy, mechanism, exposure, and intervention domains. It also flags where exact codes should be verified rather than assumed, which is important for safe knowledge-base population.*

## 2. Etiology, risks, protection, and gene–environment interaction

### Overall causal architecture

Nonsyndromic anencephaly is a **complex multifactorial threshold disorder**. Familial aggregation and heritability estimates as high as approximately 70% support substantial genetic contribution, but most cases are sporadic and molecular diagnosis is uncommon. A prior affected pregnancy raises recurrence risk to approximately **2–10%**, compared with a much lower background risk; the wide range reflects population, ascertainment, folate exposure, and whether all NTDs or anencephaly alone were counted. (munteanu2020theetiopathogenicand pages 2-3, ishida2018atargetedsequencing pages 1-5)

### Genetic risk factors

Human evidence supports candidate genes in several functional groups:

* **PCP/convergent extension:** *VANGL1, VANGL2, CELSR1* and other non-canonical Wnt components. Disrupted PCP impairs mediolateral cell intercalation and neural-plate narrowing/elongation, preventing cranial folds from apposing.
* **Growth-factor/cytoskeletal and closure biology:** *PDGFRA, TRIM36, CFL1, PRKCA, PRKCB, CITED2*.
* **Transcription/developmental regulation:** *PAX3, ZIC1, ZIC2, ZIC3*.
* **Redox, DNA-damage, apoptosis, and proliferation:** *TXN2, TP53, BRCA1, NOS2*.
* **Metabolic candidates:** *MTHFR, MAT1A* and related one-carbon genes.
* **Hippo–YAP signaling:** biallelic loss-of-function in *NUAK2* has been reported in severe NTD/anencephaly families, but this represents a rare cause rather than the usual architecture. (munteanu2020theetiopathogenicand pages 2-3, rai2023aquestfor pages 2-3, isakovic2022overviewofneural pages 24-25)

The strongest anencephaly-focused sequencing evidence comes from Ishida et al., published February 2018, DOI [10.1111/cge.13189](https://doi.org/10.1111/cge.13189). A 191-gene panel in 90 cranial-NTD cases found **397 variants with MAF <1%**, including **21 previously unreported variants predicted damaging**: one *PDGFRA* frameshift, stop-gained variants in *MAT1A* and *NOS2*, and 18 missense variants. The findings support an oligogenic model but do not establish every variant as ACMG pathogenic. (ishida2018atargetedsequencing pages 1-5)

**Variant-curation caution:** no single recurrent germline variant explains most anencephaly. Candidate variants should be stored with the original laboratory classification, segregation, functional data, and population frequency. Predicted damaging does not equal ClinVar pathogenic. Somatic mutation, repeat expansion, mitochondrial inheritance, anticipation, and a characteristic founder mutation are not established general features.

### Chromosomal abnormalities

Most isolated cases have a normal karyotype. Chromosomal abnormalities are reported in only a minority—approximately **1–5%** in one review, with broader NTD estimates under 10%. Trisomy 18 is a recognized association, particularly when additional malformations are present. Karyotype or chromosomal microarray is therefore most informative in non-isolated cases. (munteanu2020theetiopathogenicand pages 1-2, munteanu2020theetiopathogenicand pages 2-3, avagliano2019overviewonneural pages 1-2)

### Maternal and environmental risks

Supported or repeatedly reported NTD risks include:

* low periconceptional folate status and vitamin B12 insufficiency;
* pregestational diabetes and poor glycemic control;
* maternal obesity;
* valproate and some other antiseizure drugs;
* fever, sauna/hot-tub exposure, or other hyperthermia during the neurulation window;
* occupational organic solvents and epidemiologic associations with pesticides, arsenic, and polycyclic aromatic hydrocarbons;
* restrictive diets, malabsorption, drug–nutrient interactions, and cooking-related folate loss.

Some studies report associations with frequent sprouted-potato consumption, but this is much weaker evidence than folate deficiency, diabetes, obesity, valproate, or hyperthermia and may reflect glycoalkaloid exposure or confounding. No infectious organism is an established cause, and anencephaly is neither communicable nor zoonotic. (munteanu2020theetiopathogenicand pages 2-3, munteanu2020theetiopathogenicand pages 7-8, rai2023aquestfor pages 2-3, samaniegovaesken2024supplementationwithfolic pages 2-4)

### Protective factors and gene–environment interaction

Folic acid is the best-established protective exposure. Randomized evidence for recurrent NTD prevention indicates approximately **50–70% risk reduction** with high-dose folic acid; broader estimates state that up to 70% of NTDs may be folic-acid preventable. Not all cases are folate responsive. (ishida2018atargetedsequencing pages 1-5, rai2023aquestfor pages 2-3)

Gene–environment interaction is biologically credible because folate supplies one-carbon units for nucleotide synthesis and methylation, while closure genes govern morphogenesis. Low folate may expose susceptibility produced by variants such as *PAX3* or folate-pathway alleles. The common *MTHFR* c.677C>T polymorphism reduces enzyme activity, particularly under low-folate conditions, but it is a modest susceptibility factor—not a deterministic diagnostic mutation. Maternal metabolic or teratogenic stress can similarly shift a genetically susceptible embryo beyond the closure-failure threshold. (munteanu2020theetiopathogenicand pages 1-2, rai2023aquestfor pages 2-3)

## 3. Phenotypes and quality-of-life consequences

| Phenotype | Type, timing, course, and frequency | Suggested HPO term |
|---|---|---|
| Absent/partially absent calvarium | Defining physical sign; congenital, severe, stable structural defect | Anencephaly, **HP:0002323**; abnormality of skull ossification—verify precise child term |
| Absent/destructed cerebral hemispheres | Defining CNS malformation; begins after failed cranial closure and exposure/degeneration | Anencephaly; abnormal cerebral morphology |
| Exposed vascular neural tissue | Prenatal physical/pathologic sign of open cranial NTD; progressively degenerates | Open neural-tube defect—verify HPO code |
| Protruding orbits/absent frontal bones | Common craniofacial appearance; “frog-eye” or first-trimester “Mickey Mouse” imaging appearance | Abnormality of orbit/skull—select granular terms per case |
| Polyhydramnios | Variable prenatal complication, related partly to impaired fetal swallowing | Polyhydramnios, **HP:0001561** |
| Adrenal hypoplasia and growth restriction | Variable downstream endocrine/organ findings; impaired hypothalamic–pituitary–adrenal function has been described | Adrenal hypoplasia; intrauterine growth retardation, **HP:0001511** |
| Craniorachischisis | Severe associated extension through spine; not present in isolated anencephaly | Craniorachischisis, **HP:0001363** |
| Additional congenital anomalies | Approximately **12–25%** in one review; examine heart, kidneys, gastrointestinal tract, limbs, and face | Code each observed anomaly separately |

Onset is embryonic, not neonatal: cranial neurulation occurs around postfertilization days 17–28, with neuropore closure expected around days 25–28. Severity is uniformly profound. There is no remission or recovery. Conventional patient-reported quality-of-life instruments are inapplicable because sustained consciousness and long-term survival are absent. The principal quality-of-life burden falls on the pregnant patient and family through grief, complex reproductive decisions, delivery planning, and recurrence anxiety. (munteanu2020theetiopathogenicand pages 2-3, avagliano2019overviewonneural pages 1-2)

## 4. Genetic, molecular, epigenetic, and omics information

There is no single “anencephaly gene,” no clinically complete gene panel, and no meaningful population carrier frequency for nonsyndromic disease. Most implicated alleles are germline rare variants or common susceptibility polymorphisms with incomplete penetrance and variable expression across the NTD spectrum. Oligogenic inheritance is plausible; dominant, recessive, and digenic mechanisms can occur in rare families. (ishida2018atargetedsequencing pages 1-5)

Epigenetically, folate-dependent S-adenosylmethionine production links maternal nutrition to DNA and histone methylation. Experimental studies identify altered methylation or expression of developmental regulators such as *GATA4, CDX2, PAX6,* and *NES*, while arsenic may perturb DNA methylation. These findings are mechanistically informative but are not validated diagnostic methylation signatures for human anencephaly. (rai2023aquestfor pages 2-3)

Human disease-level transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, and multi-omic classifiers remain investigational. Tissue availability, gestational heterogeneity, postmortem degeneration, and mixed etiologies complicate interpretation. Maternal serum alpha-fetoprotein is a clinical screening analyte, not a disease-specific molecular subtype marker.

## 5. Environmental and lifestyle information

The critical exposure window is **before many pregnancies are recognized**. Prevention should therefore target all who may become pregnant rather than begin after the first prenatal visit. Clinically actionable measures are adequate folic acid, diabetes optimization, healthy preconception weight, medication review—especially avoiding valproate when a safe effective alternative exists—and prompt management of fever/avoidance of sustained extreme heat early in pregnancy. Smoking and alcohol are undesirable in pregnancy generally, but neither is as specifically established for anencephaly as folate deficiency, diabetes, obesity, valproate, and hyperthermia.

Environmental chemical associations are often observational and NTD-wide. They should be recorded as risk evidence with exposure timing and confidence, not as individually sufficient causes. There is no recognized bacterial, viral, fungal, or parasitic trigger. (munteanu2020theetiopathogenicand pages 2-3, rai2023aquestfor pages 2-3)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream susceptibility/exposure:** closure-gene variants, inadequate one-carbon nutrition, maternal diabetes/obesity, valproate, hyperthermia, or toxicant exposure.
2. **Molecular/cellular disruption:** altered PCP/Wnt signaling and convergent extension; disturbed cytoskeletal dynamics and cell adhesion; imbalanced proliferation/apoptosis; oxidative stress; impaired nucleotide synthesis and methylation.
3. **Morphogenetic failure:** cranial neural folds fail to elevate, converge, adhere, and fuse during weeks 3–4.
4. **Open neuroepithelium/exencephaly:** the developing brain remains exposed to amniotic fluid and mechanical injury.
5. **Secondary tissue degeneration:** exposed cerebral tissue undergoes progressive destruction, yielding the characteristic absent brain and calvarium.
6. **Clinical outcome:** endocrine/autonomic dysfunction, impaired swallowing and polyhydramnios, fetal loss, stillbirth, or death soon after delivery.

The PCP pathway is especially relevant: defective non-canonical Wnt signaling impairs convergent extension, a morphogenetic process required to narrow and lengthen the neural plate so the folds can meet. This mechanism is strongly supported across vertebrate models and by rare human variants, but the proportion of human anencephaly attributable to PCP dysfunction remains uncertain. (munteanu2020theetiopathogenicand pages 2-3, rai2023aquestfor pages 2-3)

Suggested annotations include **GO:0001841 neural tube formation**, neural-tube closure, convergent extension, canonical/non-canonical Wnt signaling, epithelial cell migration, actin-cytoskeleton organization, cell–cell adhesion, one-carbon metabolism, DNA methylation, oxidative-stress response, cell proliferation, and apoptotic process. Relevant cells include **neuroepithelial cells (CL:0000031; verify release)**, neural-fold cells, surface ectoderm, cranial mesenchyme, and neural crest. No single protein-misfolding, lysosomal, ion-channel, immune, or autoimmune mechanism defines the disease.

## 7. Anatomical structures affected

The primary site is the **cranial neural tube** and its derivatives: forebrain, midbrain, hindbrain, overlying meninges, cranial mesenchyme, and calvarial bones. Brainstem, cerebellum, and diencephalic tissue may be partly retained. The skull base and facial bones are less severely affected than the cranial vault. In craniorachischisis, the open defect extends caudally into spinal neural tube and vertebral arches. (munteanu2020theetiopathogenicand pages 1-2, ishida2018atargetedsequencing pages 1-5)

Suggested anatomy mappings are neural tube (**UBERON:0001049**), brain (**UBERON:0000955**), neuroepithelium, forebrain, midbrain, hindbrain, cranial meninges, calvaria, skull, cranial mesenchyme, surface ectoderm, and—when present—spinal cord and vertebral column. The lesion is a midline developmental defect, not a unilateral disorder. Relevant subcellular structures include nucleus/chromatin, actin cytoskeleton, adherens junctions, and mitochondria/redox systems; these are pathway-level annotations, not universal histologic abnormalities.

## 8. Temporal development and natural history

* **Initiation:** embryonic days 17–28 after fertilization.
* **Primary lesion:** failure of cranial neuropore closure by approximately day 25.
* **Evolution:** exposed brain initially resembles exencephaly and degenerates during gestation.
* **Prenatal course:** miscarriage, stillbirth, or continued pregnancy with possible polyhydramnios and atypical gestational duration.
* **Postnatal course:** irreversible and rapidly fatal; rare longer survival does not constitute recovery.

There are no conventional early/intermediate/end-stage categories, relapses, remission, or chronic survivorship. The only effective biological intervention window is **before closure**, explaining why postdiagnosis folate cannot repair an established lesion. (munteanu2020theetiopathogenicand pages 1-2, munteanu2020theetiopathogenicand pages 2-3)

## 9. Inheritance and population epidemiology

Published rates vary sharply with whether spontaneous losses and terminations are included. A disease review cited **1–5 per 1,000 births** and approximately **1 in 4,600 births in the United States**, while NTD-wide global prevalence estimates are around 18.6–19 per 10,000 births. These measures are not interchangeable. Birth prevalence underestimates conceptions because prenatal diagnosis and termination are common. (munteanu2020theetiopathogenicand pages 1-2)

Higher historical rates have been reported in parts of northern China, Mexico, Turkey, the British Isles, and some low-resource settings. Food fortification, supplementation, ascertainment, pregnancy termination, maternal nutrition, diabetes/obesity prevalence, and ancestry all contribute. Anencephaly shows a consistent **female excess**, unlike many spinal NTD series, but its mechanism is unresolved. (munteanu2020theetiopathogenicand pages 2-3, avagliano2019overviewonneural pages 1-2, ishida2018atargetedsequencing pages 1-5)

Inheritance is best encoded as **multifactorial/polygenic with occasional oligogenic or rare Mendelian forms**. Penetrance is incomplete and exposure dependent; expressivity may span anencephaly, craniorachischisis, encephalocele, or spinal NTD in a family. Anticipation is not established. Consanguinity may enrich rare recessive causes but is not a general prerequisite. “Carrier frequency” is not meaningful for common nonsyndromic anencephaly.

## 10. Diagnostics and screening

### Prenatal diagnosis

First-trimester ultrasonography is the principal diagnostic method. Findings include absent cranial ossification above the orbits, absent or abnormal cerebral tissue, exposed disorganized tissue, and characteristic coronal appearances. The 2020 review reports detection of essentially all cases in contemporary first-trimester screening, although real-world sensitivity depends on gestational age, operator skill, equipment, and access. Three-dimensional ultrasound refines anatomic definition. Fetal MRI is rarely needed when ultrasound is definitive. (munteanu2020theetiopathogenicand pages 1-2, munteanu2020theetiopathogenicand pages 7-8)

Maternal serum **alpha-fetoprotein** is typically markedly elevated because fetal tissue is openly exposed, but AFP is a screening test and is not specific. Amniotic-fluid AFP/acetylcholinesterase can support diagnosis when imaging is uncertain. There is no role for EEG, EMG, biopsy, liquid biopsy, or newborn biochemical screening.

### Differential diagnosis

Distinguish:

* **acrania/exencephaly/anencephaly sequence:** related developmental stages;
* **acalvaria:** absent skull vault with preserved brain and skin;
* **encephalocele:** herniated brain/meninges through a localized skull defect;
* **iniencephaly:** occipital/cervical defect with extreme retroflexion;
* **craniorachischisis:** cranial defect continuous with open spine;
* **severe microcephaly:** small but present skull and brain;
* **amniotic-band disruption:** asymmetric craniofacial defects and constriction/amputation findings. (munteanu2020theetiopathogenicand pages 7-8)

### Genetic testing approach

After confirmation, perform a detailed anatomic survey. Offer **karyotype or chromosomal microarray**, especially for non-isolated disease. Trio exome/genome sequencing may be considered in recurrent, familial, consanguineous, or syndromic cases, but diagnostic yield for isolated anencephaly is uncertain. Research NTD panels may include PCP, folate, cytoskeletal, ciliary, and developmental genes, but no panel excludes multifactorial recurrence. Mitochondrial sequencing, repeat-expansion testing, FISH, and single-gene testing are not routine unless another phenotype directs them. (ishida2018atargetedsequencing pages 1-5)

## 11. Outcome and prognosis

Prognosis is uniformly lethal: the disease-specific review reports **100% mortality in utero or within hours or days after birth**. There are no meaningful 5- or 10-year survival rates. Associated anomalies occur in approximately 12–25%, but prognosis is driven by the cranial defect itself. (munteanu2020theetiopathogenicand pages 1-2)

A Japanese dataset covering more than 311,000 pregnancies in 2014–2015 reported pregnancy termination in approximately **80%** of diagnosed cases; another cited estimate exceeded 83%. Such proportions are jurisdiction- and ascertainment-dependent and should not be interpreted as a biological outcome. (munteanu2020theetiopathogenicand pages 1-2, munteanu2020theetiopathogenicand pages 7-8)

For continuing pregnancies, planning should address polyhydramnios, malpresentation, labor, neonatal comfort care, family presence, memory-making, and bereavement. Aggressive neonatal resuscitation does not reverse the underlying condition. Long-term disability and rehabilitation metrics are not applicable.

## 12. Treatment and current applications

There is **no disease-modifying treatment**. Open-spina-bifida fetal surgery must not be extrapolated to anencephaly because the essential brain and cranial structures cannot be reconstructed. Likewise, no pharmacotherapy, gene therapy, cell therapy, RNA therapy, immunotherapy, organ transplantation, or genotype-guided therapy has demonstrated benefit.

Current real-world management consists of:

1. confirmatory high-quality ultrasound and assessment for additional anomalies;
2. nondirective counseling regarding prognosis and legally available pregnancy options;
3. maternal–fetal medicine, clinical genetics, neonatology/palliative-care, and psychosocial support;
4. if pregnancy continues, individualized delivery and neonatal comfort-care planning;
5. post-pregnancy pathology/genetic evaluation when consented and recurrence-prevention counseling.

Relevant NCIt concepts include prenatal ultrasonography, genetic counseling, palliative care, folic-acid supplementation, and pregnancy management; exact current NCIt codes should be verified before ingestion.

The trial search identified observational NTD genetics and exposure studies, but no credible disease-modifying anencephaly intervention. Fetoscopic repair trials concern myelomeningocele and are **not treatments for anencephaly**.

## 13. Prevention

### Primary prevention

For average-risk people capable of pregnancy, authoritative organizations converge on **400 µg (0.4 mg) folic acid daily**, beginning at least one month before conception and continuing through the first trimester; many prenatal preparations continue it throughout pregnancy. Dietary folate has approximately 50% bioavailability, fortified-food folic acid about 85%, and supplements taken fasting approximately 100%. Published September 2024; DOI: [10.3390/nu16183154](https://doi.org/10.3390/nu16183154). (samaniegovaesken2024supplementationwithfolic pages 2-4, samaniegovaesken2024supplementationwithfolic pages 1-2)

For a previous folate-sensitive NTD pregnancy or selected very-high-risk circumstances, guidelines commonly recommend **4 mg/day**, started before conception and continued through early pregnancy under clinical supervision. This exceeds the general adult tolerable upper intake level of 1 mg/day and therefore should not be self-prescribed or obtained by multiplying prenatal multivitamins. Randomized evidence indicates approximately 50–70% recurrent-NTD reduction. (rai2023aquestfor pages 2-3, samaniegovaesken2024supplementationwithfolic pages 1-2)

Mandatory fortification is a proven, cost-effective population strategy because the neural tube closes before many pregnancies are recognized. The United States fortification program has been credited with preventing roughly **1,300 NTD cases annually**. The 2024 review notes implementation in the United States, Canada, and Chile, contrasted with incomplete fortification coverage elsewhere. (munteanu2020theetiopathogenicand pages 2-3, samaniegovaesken2024supplementationwithfolic pages 2-4)

A recent nutritional survey cited mean folate intake of only **156.3 µg/day** in Spain, with merely **3.0% of women** meeting adequate intake, illustrating the adherence gap where mandatory fortification is absent. (samaniegovaesken2024supplementationwithfolic pages 2-4)

**5-MTHF:** although biologically plausible and commercially available, the September 2024 review concludes that clinical evidence is insufficient to establish equivalence to folic acid for NTD prevention, including optimal dose, timing, efficacy, and safety. Folic acid remains the evidence-based standard. (samaniegovaesken2024supplementationwithfolic pages 1-2)

Additional prevention comprises preconception diabetes control, weight optimization, vitamin B12 assessment where indicated, medication review, avoiding valproate when clinically feasible, and avoiding sustained hyperthermia. Medication changes must be supervised because uncontrolled epilepsy also endangers parent and fetus.

### Secondary and tertiary prevention

Secondary prevention means early prenatal ultrasound and informed reproductive care; it detects but does not prevent or treat the defect. Tertiary prevention is limited to avoiding maternal complications and providing proportionate palliative care. There is no vaccine or infectious prophylaxis.

## 14. Other species and natural disease

Congenital cranial NTDs, including anencephaly-like/acrania–exencephaly phenotypes, occur naturally in domestic mammals and livestock, but the retrieved evidence does not support a single common breed-specific Mendelian anencephaly syndrome suitable for confident VBO annotation. Veterinary cases are rare, usually lethal, and may involve genetic, nutritional, toxic, or sporadic developmental causes. There is no transmission or zoonotic potential.

Mechanisms are evolutionarily conserved across vertebrates: neural-fold morphogenesis, PCP signaling, cytoskeletal remodeling, folate/one-carbon biology, proliferation, and apoptosis. Species terminology matters—**exencephaly in mouse embryos** is often the experimental counterpart of human anencephaly because exposed mouse brain may still be present when embryos are examined.

## 15. Model organisms and advanced technologies

### Mouse

Mouse is the dominant mammalian model. Hundreds of genes can produce NTDs, and more than 400 closure-related genes have been identified in animal models. PCP mutants, cytoskeletal mutants, folate-pathway perturbations, maternal diabetes, hyperthermia, and valproate exposure model different causal routes. Models reproduce closure failure and exposed cranial neuroepithelium well, enable timed perturbation and rescue experiments, and support oligogenic/G×E testing. Limitations include strain-dependent penetrance, species-specific closure sites, placentation/metabolism differences, and examination at exencephaly rather than later degenerative anencephaly. (avagliano2019overviewonneural pages 1-2, rai2023aquestfor pages 2-3)

### Other vertebrates

Zebrafish and amphibian embryos permit live imaging and rapid manipulation of PCP, convergent extension, cell polarity, and folate-responsive development. Their neurulation morphology and cranial anatomy differ from mammals, so they are pathway models rather than complete anencephaly replicas.

### Human cellular models and organoids

Human pluripotent-stem-cell neural-tube organoids and neuruloids can model neural induction, epithelial polarization, lumen formation, closure-like morphogenesis, and genotype/exposure effects. They are valuable because direct experimental observation of human neurulation in vivo is ethically impossible. The organoid review describes them as an emerging system for cellular and molecular investigation of NTDs. Published April 2021; DOI: [10.1096/fj.202002348R](https://doi.org/10.1096/fj.202002348R). Their limitations are absence of complete extraembryonic tissues, maternal metabolism, vasculature, biomechanical context, and whole-embryo anterior–posterior patterning. They are research tools, not validated diagnostics or treatment platforms.

## Current interpretation and knowledge gaps

The authoritative interpretation is that anencephaly is a **developmental endpoint shared by heterogeneous causes**, not one molecular disease. The strongest actionable evidence concerns prevention and prenatal diagnosis; gene discovery has not yet produced routine precision therapy. Priorities include ancestrally diverse trio WGS, rigorous functional classification of rare variants, integrated maternal–fetal exposure data, human neuruloid validation, and quantification of residual folate-resistant risk.

The most important 2023–2024 development is not a curative therapy but renewed emphasis on universal fortification and closing global prevention gaps, alongside recognition that 5-MTHF lacks the outcome evidence supporting folic acid. Exact ontology and coding identifiers should be checked against current live releases before database ingestion, and every mechanistic assertion should retain an evidence tag—human anencephaly cohort, broader human NTD study, model organism, in vitro/organoid, or computational prediction.

References

1. (munteanu2020theetiopathogenicand pages 1-2): Octavian Munteanu, Monica Mihaela Cîrstoiu, Florin Mihail Filipoiu, Maria Narcisa Neamţu, Irina Stavarache, Tiberiu Augustin Georgescu, Ovidiu Gabriel Bratu, Gabriela Iorgulescu, and Roxana Elena Bohîlţea. The etiopathogenic and morphological spectrum of anencephaly: a comprehensive review of literature. Romanian Journal of Morphology and Embryology, 61:335-343, Aug 2020. URL: https://doi.org/10.47162/rjme.61.2.03, doi:10.47162/rjme.61.2.03. This article has 50 citations and is from a peer-reviewed journal.

2. (munteanu2020theetiopathogenicand pages 2-3): Octavian Munteanu, Monica Mihaela Cîrstoiu, Florin Mihail Filipoiu, Maria Narcisa Neamţu, Irina Stavarache, Tiberiu Augustin Georgescu, Ovidiu Gabriel Bratu, Gabriela Iorgulescu, and Roxana Elena Bohîlţea. The etiopathogenic and morphological spectrum of anencephaly: a comprehensive review of literature. Romanian Journal of Morphology and Embryology, 61:335-343, Aug 2020. URL: https://doi.org/10.47162/rjme.61.2.03, doi:10.47162/rjme.61.2.03. This article has 50 citations and is from a peer-reviewed journal.

3. (ishida2018atargetedsequencing pages 1-5): M. Ishida, T. Cullup, Christopher Boustred, C. James, J. Docker, C. English, N. Lench, A. Copp, G. Moore, N. Greene, and P. Stanier. A targeted sequencing panel identifies rare damaging variants in multiple genes in the cranial neural tube defect, anencephaly. Clinical Genetics, 93:870-879, Feb 2018. URL: https://doi.org/10.1111/cge.13189, doi:10.1111/cge.13189. This article has 36 citations and is from a peer-reviewed journal.

4. (avagliano2019overviewonneural pages 1-2): Laura Avagliano, Valentina Massa, Timothy M. George, Sarah Qureshy, Gaetano Pietro Bulfamante, and Richard H. Finnell. Overview on neural tube defects: from development to physical characteristics. Birth Defects Research, 111:1455-1467, Nov 2019. URL: https://doi.org/10.1002/bdr2.1380, doi:10.1002/bdr2.1380. This article has 362 citations and is from a peer-reviewed journal.

5. (rai2023aquestfor pages 2-3): Sunil Rai, Larissa Leydier, Shivani Sharma, Jigar Katwala, and Anurag Sahu. A quest for genetic causes underlying signaling pathways associated with neural tube defects. Frontiers in Pediatrics, May 2023. URL: https://doi.org/10.3389/fped.2023.1126209, doi:10.3389/fped.2023.1126209. This article has 26 citations.

6. (munteanu2020theetiopathogenicand pages 7-8): Octavian Munteanu, Monica Mihaela Cîrstoiu, Florin Mihail Filipoiu, Maria Narcisa Neamţu, Irina Stavarache, Tiberiu Augustin Georgescu, Ovidiu Gabriel Bratu, Gabriela Iorgulescu, and Roxana Elena Bohîlţea. The etiopathogenic and morphological spectrum of anencephaly: a comprehensive review of literature. Romanian Journal of Morphology and Embryology, 61:335-343, Aug 2020. URL: https://doi.org/10.47162/rjme.61.2.03, doi:10.47162/rjme.61.2.03. This article has 50 citations and is from a peer-reviewed journal.

7. (munteanu2020theetiopathogenicand pages 8-9): Octavian Munteanu, Monica Mihaela Cîrstoiu, Florin Mihail Filipoiu, Maria Narcisa Neamţu, Irina Stavarache, Tiberiu Augustin Georgescu, Ovidiu Gabriel Bratu, Gabriela Iorgulescu, and Roxana Elena Bohîlţea. The etiopathogenic and morphological spectrum of anencephaly: a comprehensive review of literature. Romanian Journal of Morphology and Embryology, 61:335-343, Aug 2020. URL: https://doi.org/10.47162/rjme.61.2.03, doi:10.47162/rjme.61.2.03. This article has 50 citations and is from a peer-reviewed journal.

8. (samaniegovaesken2024supplementationwithfolic pages 2-4): María de Lourdes Samaniego-Vaesken, Carmen Morais-Moreno, Alejandra Carretero-Krug, Ana María Puga, Ana María Montero-Bravo, Teresa Partearroyo, and Varela-Moreiras Gregorio. Supplementation with folic acid or 5-methyltetrahydrofolate and prevention of neural tube defects: an evidence-based narrative review. Nutrients, 16:3154, Sep 2024. URL: https://doi.org/10.3390/nu16183154, doi:10.3390/nu16183154. This article has 26 citations.

9. (samaniegovaesken2024supplementationwithfolic pages 1-2): María de Lourdes Samaniego-Vaesken, Carmen Morais-Moreno, Alejandra Carretero-Krug, Ana María Puga, Ana María Montero-Bravo, Teresa Partearroyo, and Varela-Moreiras Gregorio. Supplementation with folic acid or 5-methyltetrahydrofolate and prevention of neural tube defects: an evidence-based narrative review. Nutrients, 16:3154, Sep 2024. URL: https://doi.org/10.3390/nu16183154, doi:10.3390/nu16183154. This article has 26 citations.

10. (isakovic2022overviewofneural pages 24-25): Jasmina Isaković, Iva Šimunić, Denis Jagečić, Valentina Hribljan, and Dinko Mitrečić. Overview of neural tube defects: gene–environment interactions, preventative approaches and future perspectives. Biomedicines, 10:965, Apr 2022. URL: https://doi.org/10.3390/biomedicines10050965, doi:10.3390/biomedicines10050965. This article has 75 citations.

## Artifacts

- [Edison artifact artifact-00](Anencephaly-deep-research-falcon_artifacts/artifact-00.md)