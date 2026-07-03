---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-11T19:16:42.093708'
end_time: '2026-06-11T19:25:14.177347'
duration_seconds: 512.08
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Reelin Pathway Lissencephaly
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_tokens: 12000
    max_embedded_images: 8
citation_count: 36
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Reelin_Pathway_Lissencephaly-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Reelin Pathway Lissencephaly
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Reelin Pathway Lissencephaly** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
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
- **Disease Name:** Reelin Pathway Lissencephaly
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Reelin Pathway Lissencephaly** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Reelin Pathway Lissencephaly (Reelin-pathway LIS/LCH): Comprehensive Research Report

## Executive summary
“Reelin pathway lissencephaly” is best captured clinically as **lissencephaly with cerebellar hypoplasia (LCH)** / **lissencephaly 2 (LIS2; Norman–Roberts syndrome)** caused primarily by **biallelic loss-of-function variants in RELN**, with overlapping/related phenotypes caused by **biallelic DAB1** variants (RELN-like mild lissencephaly with cerebellar hypoplasia) and **biallelic VLDLR** variants (cerebellar hypoplasia with gyral simplification). The core mechanism is disruption of the canonical **Reelin→VLDLR/ApoER2→DAB1 phosphorylation** pathway required for neuronal migration and cortical/cerebellar lamination. Recent (2024) work demonstrates that **de novo monoallelic RELN missense** variants can cause **dominant** neuronal migration disorders via a **dominant-negative** mechanism, broadening inheritance models beyond classic autosomal recessive disease. (hong2000autosomalrecessivelissencephaly pages 1-2, smits2021biallelicdab1variants pages 4-5, donato2022monoallelicandbiallelic pages 1-3, riva2024denovomonoallelic pages 17-17)

| Concept | Evidence-supported details | Key citations (pqac ids) | URL/publication year where available |
|---|---|---|---|
| Core disease label | Reelin-pathway lissencephaly is most directly represented in the evidence as **lissencephaly with cerebellar hypoplasia (LCH)**, a cortical malformation/neurodevelopmental disorder with simplified or smooth gyri plus cerebellar hypoplasia. | (hong2000autosomalrecessivelissencephaly pages 1-2, lossi2019thereelermouse pages 3-6, chang2007theroleof pages 5-6) | Hong et al., *Nature Genetics* (2000): https://doi.org/10.1038/79246; Lossi et al., *J Clin Med* (2019): https://doi.org/10.3390/jcm8122088 |
| Alternative disease labels / synonyms | The evidence explicitly states **“Lissencephaly 2 (LIS2)”** and that LIS2 is also referred to as **“lissencephaly syndrome, Norman–Roberts type or Norman–Roberts syndrome.”** | (lossi2019thereelermouse pages 3-6) | Lossi et al., *J Clin Med* (2019): https://doi.org/10.3390/jcm8122088 |
| OMIM identifier explicitly present | **OMIM #257320** is explicitly attached in the evidence to **Lissencephaly 2 (LIS2) / Norman–Roberts syndrome**. | (lossi2019thereelermouse pages 3-6) | Lossi et al., *J Clin Med* (2019): https://doi.org/10.3390/jcm8122088 |
| Primary causal gene: RELN | Strongest disease-defining gene in the evidence. Autosomal recessive **RELN** mutations were linked to LCH/LIS2; 2022 evidence further shows **biallelic RELN** variants cause severe LIS-CBLH, while **monoallelic RELN** variants can produce milder/intermediate neuronal migration disorders. | (hong2000autosomalrecessivelissencephaly pages 1-2, donato2022monoallelicandbiallelic pages 4-5, donato2022monoallelicandbiallelic pages 1-3, riva2024denovomonoallelic pages 17-17) | Hong et al. (2000): https://doi.org/10.1038/79246; Di Donato et al. (2022): https://doi.org/10.1093/brain/awac164; Riva et al. (2024): https://doi.org/10.1172/jci153097 |
| Reelin-pathway gene: DAB1 | **Biallelic DAB1** splice variants were reported to cause **mild lissencephaly and cerebellar hypoplasia** with a RELN-like phenotype, supporting inclusion of DAB1-related disease within the Reelin-pathway lissencephaly spectrum. | (smits2021biallelicdab1variants pages 4-5) | Smits et al., *Neurology Genetics* (2021): https://doi.org/10.1212/nxg.0000000000000558 |
| Reelin-pathway gene: VLDLR | **Biallelic VLDLR** loss-of-function variants cause a related recessive Reelin-pathway disorder characterized by cerebellar hypoplasia with **cerebral gyral simplification**; evidence supports overlap with the broader Reelin-pathway lissencephaly/cerebellar hypoplasia spectrum, although some literature distinguishes VLDLR cerebellar hypoplasia from classic RELN-LIS2. | (ozcelik2008mutationsinthe pages 1-3, holling2024ahomozygousnonsense pages 1-2, donato2018analysisof17 pages 2-4) | Ozcelik et al., *PNAS* (2008): https://doi.org/10.1073/pnas.0710010105; Holling et al. (2024): https://doi.org/10.1038/s10038-024-01279-w; Di Donato et al. (2018): https://doi.org/10.1038/gim.2018.8 |
| Inheritance pattern | **RELN-LIS2/LCH:** autosomal recessive in classic disease. **DAB1-related RELN-like lissencephaly:** recessive in the reported case. **VLDLR-related cerebellar hypoplasia/gyral simplification:** recessive. Newer evidence shows **monoallelic/dominant RELN** variants can also cause neuronal migration disorders, but the classic Norman–Roberts/LIS2 phenotype remains recessive. | (hong2000autosomalrecessivelissencephaly pages 1-2, smits2021biallelicdab1variants pages 4-5, donato2022monoallelicandbiallelic pages 4-5, lossi2019thereelermouse pages 3-6, ozcelik2008mutationsinthe pages 1-3, riva2024denovomonoallelic pages 17-17) | Hong et al. (2000): https://doi.org/10.1038/79246; Smits et al. (2021): https://doi.org/10.1212/nxg.0000000000000558; Di Donato et al. (2022): https://doi.org/10.1093/brain/awac164; Riva et al. (2024): https://doi.org/10.1172/jci153097 |
| Hallmark MRI / neuroimaging findings | Across the evidence, hallmark imaging includes **moderate lissencephaly/pachygyria**, **thick cerebral cortex (~5–10 mm)**, **simplified gyral pattern** (often frontotemporal/temporal-predominant in RELN-related cases), **profound/very hypoplastic cerebellum with reduced or absent folia**, **hypoplastic inferior vermis and hemispheres**, **malformed or flattened hippocampus**, **thin corpus callosum**, **small pons/brainstem**, and **enlarged lateral ventricles**. VLDLR-related imaging emphasizes **inferior cerebellar vermis/hemisphere hypoplasia**, **simplified cortical gyration**, and **small brain stem**. | (hong2000autosomalrecessivelissencephaly pages 1-2, lossi2019thereelermouse pages 3-6, donato2022monoallelicandbiallelic pages 4-5, holling2024ahomozygousnonsense pages 1-2, ozcelik2008mutationsinthe pages 1-3) | Hong et al. (2000): https://doi.org/10.1038/79246; Lossi et al. (2019): https://doi.org/10.3390/jcm8122088; Di Donato et al. (2022): https://doi.org/10.1093/brain/awac164; Holling et al. (2024): https://doi.org/10.1038/s10038-024-01279-w; Ozcelik et al. (2008): https://doi.org/10.1073/pnas.0710010105 |
| Identifier/diagnostic context in sequencing cohorts | In a large lissencephaly cohort, **RELN accounted for ~1%** of diagnosed cases and **VLDLR for <1%**, supporting that Reelin-pathway lissencephaly is genetically rare within the broader lissencephaly spectrum. | (donato2018analysisof17 pages 2-4) | Di Donato et al., *Genetics in Medicine* (2018): https://doi.org/10.1038/gim.2018.8 |


*Table: This table summarizes the evidence-supported disease names, identifiers, causal genes, inheritance patterns, and hallmark imaging findings for Reelin-pathway lissencephaly. It is useful for mapping the disorder across historical labels such as LIS2 and Norman–Roberts syndrome while distinguishing RELN-, DAB1-, and VLDLR-related forms.*

## 1. Disease information
### 1.1 Definition and overview
Lissencephaly is a **neuronal migration disorder** with a “thickened, simplified cortex,” and the Reelin-pathway form is classically **lissencephaly with cerebellar hypoplasia (LCH)** due to RELN deficiency. (hong2000autosomalrecessivelissencephaly pages 1-2)

A widely used clinical label for the RELN form is **Lissencephaly 2 (LIS2)**, also referred to as **“Norman–Roberts type” / “Norman–Roberts syndrome.”** (lossi2019thereelermouse pages 3-6)

### 1.2 Key identifiers (available from retrieved evidence)
- **OMIM:** LIS2 / Norman–Roberts syndrome **OMIM #257320** (explicit in reviewed evidence). (lossi2019thereelermouse pages 3-6)
- **MONDO / Orphanet / ICD-10/ICD-11 / MeSH:** Not directly retrievable from the current evidence corpus using the available tools; therefore not reported here.

### 1.3 Common synonyms and alternative names
- Lissencephaly with cerebellar hypoplasia (LCH) (hong2000autosomalrecessivelissencephaly pages 1-2)
- Lissencephaly 2 (LIS2) (lossi2019thereelermouse pages 3-6)
- Norman–Roberts type lissencephaly syndrome / Norman–Roberts syndrome (lossi2019thereelermouse pages 3-6)

### 1.4 Evidence source types
- **Human genetic case series / family studies:** e.g., classic RELN-LCH linkage/variant study. (hong2000autosomalrecessivelissencephaly pages 1-2)
- **Cohort sequencing studies:** large lissencephaly cohorts with panel/WES yields including RELN and VLDLR. (donato2018analysisof17 pages 2-4)
- **Functional and model-organism studies:** mechanism and phenotypic recapitulation (mouse). (smits2021biallelicdab1variants pages 4-5, lossi2019thereelermouse pages 1-3)

## 2. Etiology
### 2.1 Disease causal factors
**Primary causal factor:** germline pathogenic variants disrupting Reelin signaling, most often resulting in **loss of Reelin function (RELN)** or impaired receptor/adaptor signaling (**VLDLR, DAB1**). (hong2000autosomalrecessivelissencephaly pages 1-2, smits2021biallelicdab1variants pages 4-5, ozcelik2008mutationsinthe pages 1-3)

### 2.2 Genetic risk factors (causal genes/variants)
#### RELN (Reelin)
- Classic disease: autosomal recessive RELN mutations causing LCH (Norman–Roberts/LIS2). (hong2000autosomalrecessivelissencephaly pages 1-2, lossi2019thereelermouse pages 3-6)
- Spectrum expansion (important recent development): **dominant neuronal migration disorders from monoallelic RELN missense variants via dominant-negative effects**.
  - Abstract quote (JCI 2024): “**The pachygyria-associated de novo heterozygous RELN variants acted as dominant-negative by preventing WT RELN secretion** in culture, animal models, and patients, thereby causing dominant NMDs.” (riva2024denovomonoallelic pages 17-17)

#### DAB1 (Disabled-1)
- Biallelic splice variants affecting the PTB domain are associated with **mild lissencephaly and cerebellar hypoplasia**, and authors propose considering **loss-of-function DAB1 variants in patients with RELN-like cortical malformations**. (smits2021biallelicdab1variants pages 4-5)

#### VLDLR (Very low-density lipoprotein receptor)
- Biallelic VLDLR loss-of-function variants cause a recessive neurodevelopmental disorder with cerebellar hypoplasia and gyral simplification; early work mapped families to chromosome 9p24 and identified truncating variants (e.g., R257X). (ozcelik2008mutationsinthe pages 1-3)
- 2024 isoform-specific insight: a homozygous nonsense variant in alternatively spliced exon 4 was reported in two sisters with ID and microcephaly but **normal brain imaging**, with authors suggesting that expression of exon-4–lacking neuronal isoforms may protect from the classic cerebellar hypoplasia phenotype. (holling2024ahomozygousnonsense pages 1-2)
  - Abstract quote (J Hum Genet 2024): “**The characteristic MRI findings include hypoplasia of the inferior portion of the cerebellar vermis and hemispheres, simplified cortical gyration, and a small brain stem.**” (holling2024ahomozygousnonsense pages 1-2)

### 2.3 Environmental risk/protective factors and gene–environment interactions
No environmental risk factors, protective factors, or gene–environment interaction evidence specific to Reelin-pathway lissencephaly were identified in the retrieved corpus; the disorder is best supported as a **Mendelian neurodevelopmental malformation** driven by germline variants. (hong2000autosomalrecessivelissencephaly pages 1-2, donato2022monoallelicandbiallelic pages 1-3)

## 3. Phenotypes
### 3.1 Core clinical phenotype (human)
In autosomal recessive RELN-associated LCH, reported clinical features include severe neurodevelopmental disability and epilepsy alongside ocular and tone abnormalities.
- Human clinical features summarized in the classic study include **hypotonia**, **severe delay in neurological and cognitive development**, **myopia and nystagmus**, and **generalized seizures** (noted as medication-controllable in those cases). (hong2000autosomalrecessivelissencephaly pages 1-2)

For VLDLR-related disease, reported neurologic findings include ataxia and severe ID.
- Primary report described **truncal ataxia**, **profound intellectual disability**, and **dysarthric speech**. (ozcelik2008mutationsinthe pages 1-3)

### 3.2 Neuroimaging phenotype
RELN-LCH neuroimaging can include a thickened simplified cortex and marked cerebellar hypoplasia.
- Review synopsis of LIS2 MRI: “**5–10 mm thick cerebral cortex, a malformed hippocampus and a very hypoplastic cerebellum, almost completely devoid of folia**.” (lossi2019thereelermouse pages 3-6)
- Classic RELN-LCH MRI description includes moderate lissencephaly plus **profound cerebellar hypoplasia** and associated brainstem/ventricle abnormalities. (hong2000autosomalrecessivelissencephaly pages 1-2)

### 3.3 Suggested HPO terms (non-exhaustive; for KB annotation)
(These are ontology suggestions aligned to the evidence-backed clinical/imaging findings; they are not claimed as exhaustive.)
- Lissencephaly (HP:0001339)
- Pachygyria (HP:0001302)
- Cerebellar hypoplasia (HP:0001321)
- Abnormal cerebellar vermis morphology (HP:0001320)
- Global developmental delay (HP:0001263)
- Intellectual disability (HP:0001249)
- Hypotonia (HP:0001252)
- Seizures (HP:0001250)
- Nystagmus (HP:0000639)
- Myopia (HP:0000545)
- Ventriculomegaly (HP:0002119)

### 3.4 Onset, severity, progression
The phenotype is **congenital/early-onset** with structural malformations evident on neuroimaging and severe developmental impairment in classic RELN-LCH. (hong2000autosomalrecessivelissencephaly pages 1-2)

### 3.5 Frequency and QoL impact
Robust phenotype frequencies and standardized QoL instruments (e.g., EQ-5D/SF-36) were not identified in the retrieved corpus for this rare Mendelian disorder. Available evidence is largely from families/cases and malformation cohorts. (hong2000autosomalrecessivelissencephaly pages 1-2, donato2018analysisof17 pages 2-4)

## 4. Genetic / molecular information
### 4.1 Causal genes and pathway positioning
- **RELN** encodes Reelin, a secreted glycoprotein essential for cerebral cortex development; recessive deficiency causes LCH/LIS2. (hong2000autosomalrecessivelissencephaly pages 1-2, riva2024denovomonoallelic pages 17-17)
- **VLDLR** encodes a Reelin receptor (lipoprotein receptor family) required for cortical/cerebellar development. (ozcelik2008mutationsinthe pages 1-3)
- **DAB1** encodes an intracellular adaptor; Reelin binding to VLDLR/ApoER2 induces DAB1 tyrosine phosphorylation. (smits2021biallelicdab1variants pages 4-5)

### 4.2 Variant classes and functional consequences
- RELN: splice-disrupting variants causing low/undetectable protein in classic autosomal recessive disease; monoallelic missense can be dominant-negative (reduced secretion) in 2024 mechanistic work. (hong2000autosomalrecessivelissencephaly pages 1-2, riva2024denovomonoallelic pages 17-17)
- DAB1: biallelic splice variants affecting the PTB domain cause loss of normal transcripts and are proposed pathogenic for RELN-like cortical malformations. (smits2021biallelicdab1variants pages 4-5)
- VLDLR: truncating variants; 2024 work highlights alternative splicing (exon 4/16) as potentially modifying phenotype severity. (holling2024ahomozygousnonsense pages 1-2, ozcelik2008mutationsinthe pages 1-3)

### 4.3 Population allele frequency information
Population frequencies (e.g., gnomAD AF) and carrier frequencies were not extractable from the retrieved full-text excerpts; one study notes monoallelic RELN rare variants “not seen in gnomAD,” but specific allele frequency values were not captured in the available evidence snippets. (donato2022monoallelicandbiallelic pages 4-5)

## 5. Environmental information
No disease-specific environmental, lifestyle, or infectious contributors were identified in the retrieved evidence; the disorder is primarily genetically determined. (hong2000autosomalrecessivelissencephaly pages 1-2)

## 6. Mechanism / pathophysiology
### 6.1 Canonical causal chain (molecular → cellular → anatomical → clinical)
1. **Initiating trigger:** germline pathogenic variants in **RELN**, **VLDLR**, or **DAB1**. (hong2000autosomalrecessivelissencephaly pages 1-2, smits2021biallelicdab1variants pages 4-5, ozcelik2008mutationsinthe pages 1-3)
2. **Upstream molecular defect:** reduced/absent Reelin secretion or impaired receptor/adaptor engagement.
   - RELN recessive variants produce low/undetectable Reelin. (hong2000autosomalrecessivelissencephaly pages 1-2)
   - 2024 dominant-negative RELN missense prevent secretion of wild-type RELN. (riva2024denovomonoallelic pages 17-17)
3. **Signal transduction defect:** Reelin normally binds VLDLR/ApoER2 and induces DAB1 phosphorylation; loss of this cascade disrupts migration/lamination programs. (smits2021biallelicdab1variants pages 4-5)
4. **Cellular process:** defective neuronal migration and impaired laminar organization.
5. **Anatomical phenotype:** simplified/thickened cortex (lissencephaly/pachygyria), hippocampal malformation, and cerebellar hypoplasia (often severe in classic RELN-LCH). (hong2000autosomalrecessivelissencephaly pages 1-2, lossi2019thereelermouse pages 3-6)
6. **Clinical manifestations:** profound developmental delay/intellectual disability, hypotonia/ataxia, seizures, ocular motor findings, etc. (hong2000autosomalrecessivelissencephaly pages 1-2, ozcelik2008mutationsinthe pages 1-3)

### 6.2 Recent mechanistic developments (prioritize 2023–2024)
- **Dominant-negative vs gain-/loss-of-function effects in RELN missense variants (2024):**
  - Abstract quote (JCI 2024): “**Polymicrogyria-associated variants behaved as gain-of-function… while those linked to pachygyria behaved as loss-of-function… The pachygyria-associated de novo heterozygous RELN variants acted as dominant-negative**…” (riva2024denovomonoallelic pages 17-17)
- **Isoform-level modulation in VLDLR (2024):** alternative splicing of exon 4/16 may modulate clinical expressivity (brain isoforms lacking exon 4 potentially protective in one family). (holling2024ahomozygousnonsense pages 1-2)

### 6.3 Suggested ontology terms for mechanism annotation
**GO (biological process) suggestions:**
- Neuron migration (GO:0001764)
- Neuron projection development (GO:0031175)
- Cerebral cortex development (GO:0021987)
- Cerebellum development (GO:0021549)

**Cell Ontology (CL) suggestions:**
- Cortical pyramidal neuron (e.g., CL:0000540)
- Cerebellar Purkinje cell (CL:0000121)
- Cerebellar granule cell (CL:0000120)

## 7. Anatomical structures affected
### 7.1 Organ/tissue level
Primary: central nervous system—**cerebral cortex**, **cerebellum**, **hippocampus**, and often brainstem/pons and ventricles on imaging. (hong2000autosomalrecessivelissencephaly pages 1-2, lossi2019thereelermouse pages 3-6)

**UBERON suggestions:**
- Cerebral cortex (UBERON:0000956)
- Cerebellum (UBERON:0002037)
- Hippocampus (UBERON:0001954)
- Pons (UBERON:0000988)
- Lateral ventricle (UBERON:0002081)

## 8. Temporal development
The malformation pattern is congenital/early developmental with structural abnormalities detectable on MRI and severe early developmental impact in classic RELN-LCH. (hong2000autosomalrecessivelissencephaly pages 1-2)

## 9. Inheritance and population
### 9.1 Inheritance
- **Classic RELN-LCH / LIS2 (Norman–Roberts):** autosomal recessive. (hong2000autosomalrecessivelissencephaly pages 1-2, lossi2019thereelermouse pages 3-6)
- **DAB1-related RELN-like lissencephaly + cerebellar hypoplasia:** autosomal recessive (biallelic splice variants reported). (smits2021biallelicdab1variants pages 4-5)
- **VLDLR-related cerebellar hypoplasia with gyral simplification:** autosomal recessive. (ozcelik2008mutationsinthe pages 1-3)
- **Important update:** **dominant** neuronal migration disorders due to **de novo monoallelic RELN missense** variants via dominant-negative mechanism. (riva2024denovomonoallelic pages 17-17)

### 9.2 Epidemiology and population genetics (what is and is not available)
Direct prevalence/incidence for “Reelin pathway lissencephaly” was not identified in retrieved sources.

However, large sequencing cohorts provide useful rarity estimates within lissencephaly:
- In a cohort of **811** patients with lissencephaly/subcortical band heterotopia, overall mutation frequency across 17 genes was **81%**, and **RELN accounted for ~1%** while **VLDLR accounted for <1%** of subjects. (donato2018analysisof17 pages 2-4)

## 10. Diagnostics
### 10.1 Clinical and neuroimaging hallmarks
Hallmark MRI patterns include thickened/simplified cortex (often frontotemporal/temporal-predominant in some RELN-related presentations), hippocampal malformation, and cerebellar hypoplasia (often severe with reduced foliation in classic disease). (hong2000autosomalrecessivelissencephaly pages 1-2, lossi2019thereelermouse pages 3-6, donato2022monoallelicandbiallelic pages 1-3)

### 10.2 Genetic testing strategies and real-world implementation
**Sequencing-based diagnosis is central to clinical implementation**:
- Large lissencephaly cohort testing supports multi-gene panels and/or WES as effective strategies.
  - Abstract quote (Genet Med 2018): “**The overall mutation frequency in the entire cohort was 81%.**” (donato2018analysisof17 pages 2-4)
- Exome sequencing for brain malformations in routine practice:
  - Abstract quote (Brain Communications 2024): “**The overall diagnostic yield for the clinical singleton exome sequencing was 36%, which increased to 43% after research follow-up.**” (kooshavar2024diagnosticutilityof pages 1-3)

**Practical diagnostic workflow (evidence-aligned):**
1) Brain MRI phenotype classification (to guide differential and gene prioritization). (donato2018analysisof17 pages 2-4)
2) Chromosomal microarray (often required/used as first-tier in malformation programs), followed by WES or targeted panels when CMA is negative. (kooshavar2024diagnosticutilityof pages 1-3)
3) Variant interpretation with attention to inheritance (biallelic LoF typical for classic LCH; de novo monoallelic missense possible for dominant RELN-related migration disorders). (riva2024denovomonoallelic pages 17-17)

### 10.3 Differential diagnosis
Not exhaustively derivable from the retrieved evidence corpus. In practice, different lissencephaly genes produce distinct imaging patterns; cohort studies emphasize that “brain-imaging pattern correlates with mutations in single lissencephaly-associated genes, as well as in biological pathways.” (donato2018analysisof17 pages 2-4)

### 10.4 Screening and prevention
No newborn screening or biochemical screening is supported by retrieved evidence. Prevention in Mendelian disease is primarily via genetic counseling, carrier testing, and prenatal/preimplantation options (not directly evidenced in retrieved excerpts).

## 11. Outcome / prognosis
Long-term outcome statistics (survival curves, standardized disability scales) were not identified in the retrieved corpus. The classic RELN-LCH description supports a severe neurodevelopmental outcome with profound impairment and seizures (sometimes medication-controlled). (hong2000autosomalrecessivelissencephaly pages 1-2)

## 12. Treatment
### 12.1 Current management (real-world implementation)
No disease-modifying therapy is established in the retrieved evidence. Management is supportive and symptom-directed.
- In classic autosomal recessive RELN-LCH families, **generalized seizures** were reported and “could be controlled with medication.” (hong2000autosomalrecessivelissencephaly pages 1-2)

**MAXO suggestions (supportive-care aligned):**
- Antiseizure therapy (e.g., MAXO:0000757 [anticonvulsant therapy] — term suggestion)
- Physical therapy / rehabilitation (MAXO term suggestions)
- Feeding therapy / management of oral motor difficulty (noted in DAB1 case). (smits2021biallelicdab1variants pages 4-5)

### 12.2 Experimental therapies and clinical trials
A ClinicalTrials.gov query for “RELN OR reelin AND lissencephaly” did not retrieve lissencephaly-specific interventional trials in the current tool state (retrieved trials were largely unrelated to congenital malformations). Therefore, no disease-specific NCT identifiers can be supported from this search output.

## 13. Prevention
Evidence in the retrieved corpus does not address primary prevention beyond genetic etiology. For affected families, prevention is typically via reproductive genetic counseling, but such recommendations are not explicitly supported by the retrieved excerpts.

## 14. Other species / natural disease
- **Sheep:** a RELN deletion causing lissencephaly with cerebellar hypoplasia has been reported (comparative genetics evidence). (ozcelik2008mutationsinthe pages 1-3)

## 15. Model organisms
- **Mouse (reeler; Reln−/−):** widely used translational model; review summarizes disrupted lamination of cerebral cortex/hippocampus/cerebellum and motor phenotype, and notes that disruption of pathway components (e.g., DAB1, receptors) yields similar phenotypes. (lossi2019thereelermouse pages 1-3)
- **Mouse receptor/adaptor loss:** DAB1 loss or receptor loss produces “Reeler/Disabled-like disruption of neuronal migration” (reviewed). (chang2007theroleof pages 5-6)

## Evidence gaps and limitations (explicit)
- MONDO/Orphanet/ICD/MeSH identifiers, prevalence/incidence, carrier frequencies, and systematic phenotype frequencies/QoL measures were not retrievable from the current tool-accessible full texts.
- Some key recent disease-specific case reports mentioned by search results (e.g., a 2023 Pediatric Neurology “new RELN mutation”) were listed as unobtainable and could not be included.

## Key recent sources (2023–2024 prioritized)
- Riva M et al. “De novo monoallelic Reelin missense variants cause dominant neuronal migration disorders via a dominant-negative mechanism.” *J Clin Invest*. **2024-07**. https://doi.org/10.1172/jci153097 (riva2024denovomonoallelic pages 17-17)
- Holling T et al. “A homozygous nonsense variant in the alternatively spliced VLDLR exon 4…” *Journal of Human Genetics*. **2024-07**. https://doi.org/10.1038/s10038-024-01279-w (holling2024ahomozygousnonsense pages 1-2)
- Kooshavar D et al. “Diagnostic utility of exome sequencing followed by research reanalysis in human brain malformations.” *Brain Communications*. **2024-02**. https://doi.org/10.1093/braincomms/fcae056 (kooshavar2024diagnosticutilityof pages 1-3)

## Foundational primary sources
- Hong SE et al. “Autosomal recessive lissencephaly with cerebellar hypoplasia is associated with human RELN mutations.” *Nature Genetics*. **2000-09**. https://doi.org/10.1038/79246 (hong2000autosomalrecessivelissencephaly pages 1-2)
- Smits DJ et al. “Biallelic DAB1 variants are associated with mild lissencephaly and cerebellar hypoplasia.” *Neurology Genetics*. **2021-04**. https://doi.org/10.1212/nxg.0000000000000558 (smits2021biallelicdab1variants pages 4-5)
- Di Donato N et al. “Monoallelic and biallelic mutations in RELN underlie a graded series of neurodevelopmental disorders.” *Brain*. **2022-06**. https://doi.org/10.1093/brain/awac164 (donato2022monoallelicandbiallelic pages 1-3)
- Di Donato N et al. “Analysis of 17 genes detects mutations in 81% of 811 patients with lissencephaly.” *Genetics in Medicine*. **2018-11**. https://doi.org/10.1038/gim.2018.8 (donato2018analysisof17 pages 2-4)


References

1. (hong2000autosomalrecessivelissencephaly pages 1-2): Susan E. Hong, Yin Yao Shugart, David T. Huang, Saad Al Shahwan, P. Ellen Grant, Jonathan O'B. Hourihane, Neil D.T. Martin, and Christopher A. Walsh. Autosomal recessive lissencephaly with cerebellar hypoplasia is associated with human reln mutations. Nature Genetics, 26:93-96, Sep 2000. URL: https://doi.org/10.1038/79246, doi:10.1038/79246. This article has 1067 citations and is from a highest quality peer-reviewed journal.

2. (smits2021biallelicdab1variants pages 4-5): MD Msc Daphne J. Smits, BSc Rachel Schot, PhD Martina Wilke, PhD Marjon van Slegtenhorst, Marie Claire, MD Y. de Wit, Marjolein H.G. Dremmen PhD, M. W. B. Md, PhD A. James Barkovich, and PhD Grazia M.S. Mancini. Biallelic <i>dab1</i> variants are associated with mild lissencephaly and cerebellar hypoplasia. Neurology Genetics, Apr 2021. URL: https://doi.org/10.1212/nxg.0000000000000558, doi:10.1212/nxg.0000000000000558. This article has 13 citations.

3. (donato2022monoallelicandbiallelic pages 1-3): Nataliya Di Donato, Renzo Guerrini, Charles J Billington, A James Barkovich, Philine Dinkel, Elena Freri, Michael Heide, Elliot S Gershon, Tracy S Gertler, Robert J Hopkin, Suma Jacob, Sarah K Keedy, Daniz Kooshavar, Paul J Lockhart, Dietmar R Lohmann, Iman G Mahmoud, Elena Parrini, Evelin Schrock, Giulia Severi, Andrew E Timms, Richard I Webster, Mary J H Willis, Maha S Zaki, Joseph G Gleeson, Richard J Leventer, and William B Dobyns. Monoallelic and biallelic mutations in reln underlie a graded series of neurodevelopmental disorders. Brain : a journal of neurology, 145:3274-3287, Jun 2022. URL: https://doi.org/10.1093/brain/awac164, doi:10.1093/brain/awac164. This article has 26 citations.

4. (riva2024denovomonoallelic pages 17-17): Martina Riva, Sofia Ferreira, Kotaro Hayashi, Yoann Saillour, Vera P. Medvedeva, Takao Honda, Kanehiro Hayashi, Claire Altersitz, Shahad Albadri, Marion Rosello, Julie Dang, Malo Serafini, Frédéric Causeret, Olivia J. Henry, Charles-Joris Roux, Céline Bellesme, Elena Freri, Dragana Josifova, Elena Parrini, Renzo Guerrini, Filippo Del Bene, Kazunori Nakajima, Nadia Bahi-Buisson, and Alessandra Pierani. De novo monoallelic reelin missense variants cause dominant neuronal migration disorders via a dominant-negative mechanism. The Journal of Clinical Investigation, Jul 2024. URL: https://doi.org/10.1172/jci153097, doi:10.1172/jci153097. This article has 9 citations.

5. (lossi2019thereelermouse pages 3-6): Laura Lossi, Claudia Castagna, Alberto Granato, and Adalberto Merighi. The reeler mouse: a translational model of human neurological conditions, or simply a good tool for better understanding neurodevelopment? Journal of Clinical Medicine, 8:2088, Dec 2019. URL: https://doi.org/10.3390/jcm8122088, doi:10.3390/jcm8122088. This article has 50 citations.

6. (chang2007theroleof pages 5-6): Bernard S. Chang, Fusun Duzcan, Seonhee Kim, Mine Cinbis, Abha Aggarwal, Kira A. Apse, Osman Ozdel, Munevver Atmaca, Sevil Zencir, Huseyin Bagci, and Christopher A. Walsh. The role of reln in lissencephaly and neuropsychiatric disease. American Journal of Medical Genetics Part B: Neuropsychiatric Genetics, 144B:58-63, Jan 2007. URL: https://doi.org/10.1002/ajmg.b.30392, doi:10.1002/ajmg.b.30392. This article has 105 citations.

7. (donato2022monoallelicandbiallelic pages 4-5): Nataliya Di Donato, Renzo Guerrini, Charles J Billington, A James Barkovich, Philine Dinkel, Elena Freri, Michael Heide, Elliot S Gershon, Tracy S Gertler, Robert J Hopkin, Suma Jacob, Sarah K Keedy, Daniz Kooshavar, Paul J Lockhart, Dietmar R Lohmann, Iman G Mahmoud, Elena Parrini, Evelin Schrock, Giulia Severi, Andrew E Timms, Richard I Webster, Mary J H Willis, Maha S Zaki, Joseph G Gleeson, Richard J Leventer, and William B Dobyns. Monoallelic and biallelic mutations in reln underlie a graded series of neurodevelopmental disorders. Brain : a journal of neurology, 145:3274-3287, Jun 2022. URL: https://doi.org/10.1093/brain/awac164, doi:10.1093/brain/awac164. This article has 26 citations.

8. (ozcelik2008mutationsinthe pages 1-3): Tayfun Ozcelik, Nurten Akarsu, Elif Uz, Safak Caglayan, Suleyman Gulsuner, Onur Emre Onat, Meliha Tan, and Uner Tan. Mutations in the very low-density lipoprotein receptor vldlr cause cerebellar hypoplasia and quadrupedal locomotion in humans. Proceedings of the National Academy of Sciences, 105:4232-4236, Mar 2008. URL: https://doi.org/10.1073/pnas.0710010105, doi:10.1073/pnas.0710010105. This article has 132 citations and is from a highest quality peer-reviewed journal.

9. (holling2024ahomozygousnonsense pages 1-2): Tess Holling, Ibrahim M. Abdelrazek, Ghada M. Elhady, Marwa Abd Elmaksoud, Seung Woo Ryu, Ebtesam Abdalla, and Kerstin Kutsche. A homozygous nonsense variant in the alternatively spliced vldlr exon 4 causes a neurodevelopmental disorder without features of vldlr cerebellar hypoplasia. Journal of Human Genetics, 69:623-628, Jul 2024. URL: https://doi.org/10.1038/s10038-024-01279-w, doi:10.1038/s10038-024-01279-w. This article has 4 citations and is from a peer-reviewed journal.

10. (donato2018analysisof17 pages 2-4): Nataliya Di Donato, Andrew E. Timms, Kimberly A. Aldinger, Ghayda M. Mirzaa, James T. Bennett, Sarah Collins, Carissa Olds, Davide Mei, Sara Chiari, Gemma Carvill, Candace T. Myers, Jean-Baptiste Rivière, Maha S. Zaki, Joseph G. Gleeson, Andreas Rump, Valerio Conti, Elena Parrini, M.Elizabeth Ross, David H. Ledbetter, Renzo Guerrini, and William B. Dobyns. Analysis of 17 genes detects mutations in 81% of 811 patients with lissencephaly. Genetics in Medicine, 20:1354-1364, Nov 2018. URL: https://doi.org/10.1038/gim.2018.8, doi:10.1038/gim.2018.8. This article has 161 citations and is from a highest quality peer-reviewed journal.

11. (lossi2019thereelermouse pages 1-3): Laura Lossi, Claudia Castagna, Alberto Granato, and Adalberto Merighi. The reeler mouse: a translational model of human neurological conditions, or simply a good tool for better understanding neurodevelopment? Journal of Clinical Medicine, 8:2088, Dec 2019. URL: https://doi.org/10.3390/jcm8122088, doi:10.3390/jcm8122088. This article has 50 citations.

12. (kooshavar2024diagnosticutilityof pages 1-3): Daniz Kooshavar, David J Amor, Kirsten Boggs, Naomi Baker, Christopher Barnett, Michelle G de Silva, Samantha Edwards, Michael C Fahey, Justine E Marum, Penny Snell, Kiymet Bozaoglu, Kate Pope, Shekeeb S Mohammad, Kate Riney, Rani Sachdev, Ingrid E Scheffer, Sarah Schenscher, John Silberstein, Nicholas Smith, Melanie Tom, Tyson L Ware, Paul J Lockhart, and Richard J Leventer. Diagnostic utility of exome sequencing followed by research reanalysis in human brain malformations. Brain Communications, Feb 2024. URL: https://doi.org/10.1093/braincomms/fcae056, doi:10.1093/braincomms/fcae056. This article has 6 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Reelin_Pathway_Lissencephaly-deep-research-falcon_artifacts/artifact-00.md)
