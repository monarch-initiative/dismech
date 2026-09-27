---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T07:17:59.756590'
end_time: '2026-08-01T07:28:09.787326'
duration_seconds: 610.03
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Isolated Anophthalmia-Microphthalmia Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 40
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Isolated_Anophthalmia-Microphthalmia_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Isolated Anophthalmia-Microphthalmia Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Isolated Anophthalmia-Microphthalmia Syndrome** covering all of the
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
- **Disease Name:** Isolated Anophthalmia-Microphthalmia Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Isolated Anophthalmia-Microphthalmia Syndrome** covering all of the
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


# Isolated Anophthalmia–Microphthalmia Syndrome: Research Report

## Executive summary and scope

**Isolated anophthalmia–microphthalmia (A/M)** is not one molecularly uniform syndrome. It is a phenotypic category within the microphthalmia–anophthalmia–coloboma (MAC) spectrum in which the principal recognized abnormalities are ocular. The same causal gene—and sometimes the same variant—may cause isolated disease in one person and systemic disease in another because of incomplete penetrance, mosaicism, and variable expressivity. “Isolated” should therefore be treated as an ascertainment-time phenotype qualifier rather than proof that extraocular manifestations can never occur.

Anophthalmia denotes absent ocular tissue; clinically, it is usually defined as no visible globe, although microscopic remnants can distinguish extreme microphthalmia from true anophthalmia. Microphthalmia is a structurally small eye with axial length at least 2 standard deviations below the age-adjusted mean. Suggested thresholds are <14 mm in a newborn and <21 mm in an adult; a prospective clinic used <16 mm at birth, <19 mm at 12 months, and <21 mm in adults. “Simple” microphthalmia has otherwise preserved architecture, whereas “complex” microphthalmia includes other anterior- or posterior-segment abnormalities. Severe microphthalmia has been defined by corneal diameter <4 mm plus axial length <10 mm at birth or <12 mm after one year. (plaisancie2019geneticsofanophthalmia pages 2-3, plaisancie2019geneticsofanophthalmia pages 1-2, harding2023realworldclinicaland pages 2-3)

The combined A/M prevalence is approximately **1–3 per 10,000 live births**, with broader MAC estimates of 1–4 per 10,000. A/M accounts for an estimated 3–12% of childhood visual impairment, and MAC may contribute up to 15% of childhood blindness worldwide. These estimates combine isolated and syndromic cases and vary by surveillance system. (plaisancie2019geneticsofanophthalmia pages 2-3, harding2023realworldclinicaland pages 1-2)

| domain | key finding | quantitative evidence | suggested ontology terms | evidence/source year |
|---|---|---|---|---|
| disease scope | Isolated anophthalmia-microphthalmia is best treated as a congenital phenotype spectrum within MAC; “isolated/non-syndromic” is a phenotype qualifier, not a single molecular disorder, and many causative genes also produce syndromic disease | Combined MAC prevalence ~1–4/10,000 live births; A/M contributes 3–12% of childhood visual impairment/blindness estimates in reviews/cohorts | anophthalmia, microphthalmia, congenital eye malformation, non-syndromic phenotype qualifier | 2019–2023 (plaisancie2019geneticsofanophthalmia pages 2-3, harding2023realworldclinicaland pages 1-2) |
| definitions | Anophthalmia = absence of visible globe/eye tissue; microphthalmia = axial length ≥2 SD below age-adjusted mean; severe microphthalmia includes very short axial length and small cornea | Adult axial length <21 mm; newborn <14 mm in one review, and operational clinic thresholds <16 mm at birth, <19 mm at 12 months, <21 mm in adults in a prospective cohort | HP:0000528 Anophthalmia; HP:0000568 Microphthalmia; severe microphthalmia; simple microphthalmia; complex microphthalmia | 2019, 2023 (plaisancie2019geneticsofanophthalmia pages 1-2, harding2023realworldclinicaland pages 2-3) |
| onset/natural history | Disorder is congenital and usually recognized neonatally/infancy; laterality is variable and asymmetry is common | Mean cohort age 13 years in prospective MAC clinic; severe forms present at birth; both unilateral and bilateral disease occur | congenital onset, unilateral, bilateral, asymmetric involvement | 2019, 2023 (plaisancie2019geneticsofanophthalmia pages 2-3, harding2023realworldclinicaland pages 2-3) |
| major ocular phenotypes | Core phenotype is absent or small eye; additional ocular anomalies may occur even in apparently isolated cases, especially coloboma, cataract, glaucoma, retinal dystrophy/detachment | In a prospective cohort, 44% had complex ocular features; retinal detachment 9%; no diagnosis in exclusive coloboma subgroup in that cohort | HP:0000528 Anophthalmia; HP:0000568 Microphthalmia; coloboma; cataract; glaucoma; retinal detachment | 2019, 2023 (harding2023realworldclinicaland pages 9-10, harding2023realworldclinicaland pages 8-9, plaisancie2019geneticsofanophthalmia pages 6-8) |
| non-ocular qualifier | “Isolated” requires absence of extra-ocular findings at ascertainment, but some genes show incomplete penetrance/variable expressivity so systemic findings may emerge or be subtle | In a pediatric cohort, isolated A/M occurred in 16/35, while 19/35 had somatic/psychomotor/neuroradiologic/genetic pathology | non-syndromic, syndromic, variable expressivity, incomplete penetrance | 2022 (fahnehjelm2022anophthalmiaandmicrophthalmia pages 1-3) |
| core genes: AD | Major dominant genes include SOX2 and OTX2; both are dosage-sensitive developmental transcription factors and may cause isolated or syndromic disease | SOX2: 10–15% of all A/M, 15–40% of bilateral severe AM; OTX2: ~0.7–10% or 2–8% of AM in reviews; SOX2+OTX2 together account for ≥60% of bilateral severe cases in one review | SOX2, OTX2, haploinsufficiency, autosomal dominant, de novo, mosaicism | 2019 (harding2019themolecularbasis pages 15-17, plaisancie2019geneticsofanophthalmia pages 6-8, plaisancie2019geneticsofanophthalmia pages 5-6) |
| core genes: AR | Important recessive genes include RAX, VSX2, ALDH1A3, and some MAB21L2 cases; these often present with bilateral severe disease | RAX biallelic variants: ~2–3% of AM; ALDH1A3 responsible for ~11% of recessively inherited severe developmental eye anomalies; all 9 affected individuals in Kesim 2023 had bilateral A/M | RAX, VSX2, ALDH1A3, MAB21L2, autosomal recessive, bilateral severe A/M | 2019–2023 (harding2019themolecularbasis pages 15-17, plaisancie2019geneticsofanophthalmia pages 6-8, plaisancie2019geneticsofanophthalmia pages 9-11, kesim2023clinicalandgenetic pages 1-2) |
| additional genes / CNVs | Other genes and copy-number changes contribute, including FOXE3, PAX6, BMP7, BCOR, KMT2D, EPHA2, MAB21L2 and large deletions; some are more often syndromic but can appear in isolated MAC presentations | Prospective cohort solved cases involved SOX2, PAX6, KMT2D, EPHA2, MAB21L2, ALDH1A3, BCOR, FOXE3 plus deletions on chromosomes 10, 11 and X; chromosomal anomalies reported up to ~15% overall | FOXE3, PAX6, BMP7, BCOR, KMT2D, EPHA2, CNV, chromosomal deletion | 2019, 2023 (harding2023realworldclinicaland pages 1-2, harding2023realworldclinicaland pages 9-10, harding2023realworldclinicaland pages 8-9, plaisancie2019geneticsofanophthalmia pages 9-11) |
| inheritance nuances | De novo disease, parental mosaicism, incomplete penetrance, and variable expressivity are common and complicate counseling; unilateral vs bilateral severity can differ within gene/family | SOX2 mostly de novo with parental mosaicism reported; OTX2 ~50% de novo with high non-penetrance; MAB21L2 shows AD and AR examples with dominant-negative effect proposed for monoallelic missense variants | incomplete penetrance, variable expressivity, gonosomal mosaicism, dominant negative, haploinsufficiency | 2019 (harding2019themolecularbasis pages 15-17, plaisancie2019geneticsofanophthalmia pages 6-8, plaisancie2019geneticsofanophthalmia pages 9-11) |
| developmental pathways | Core upstream mechanism is disruption of eye-field specification and optic vesicle/cup morphogenesis involving SOX2-OTX2-RAX/PAX6/SIX3 networks, SHH patterning, WNT/FGF balance, BMP signaling, and retinoic acid metabolism | Reviews identify conserved transcription factor and signaling pathway modules rather than a single pathway; PTCH1 variants may contribute up to 10% of ocular developmental anomalies in one sequencing study | eye field specification, optic vesicle formation, optic cup morphogenesis, SHH signaling, WNT signaling, BMP signaling, retinoic acid signaling | 2015–2020 (dash2020themastertranscription pages 3-3, eintracht2020theuseof pages 7-8, reis2015conservedgeneticpathways pages 28-29) |
| mechanistic examples | SOX2/OTX2 coregulate RAX; PTCH1 links SOX2 network to SHH; ALDH1A3 and STRA6 impair retinoic acid biology; VSX2 loss shifts neural retina toward RPE fate with WNT upregulation | PTCH1 study estimated contribution up to 10% of ocular developmental anomalies; VSX2 hiPSC optic vesicles showed WNT11/BMP8A up, FGF19 down, and rescue with WNT inhibition in cited model literature | RAX regulation, PTCH1, SHH effector, ALDH1A3, STRA6, neural retina, retinal pigment epithelium | 2016–2020 (jackson2020moleculardiagnosticchallenges pages 9-10, eintracht2020theuseof pages 8-9, harding2019themolecularbasis pages 19-20, eintracht2020theuseof pages 7-8) |
| anatomy / tissues / cells | Primary structures affected are globe, optic vesicle/cup, neuroretina, retinal pigment epithelium, lens placode, and ventral optic cup; retinal progenitor cells are a key implicated cell population | ALDH1A3/Raldh3 knockout data support ventral retina shortening; RAX and VSX2 are tied to retinal progenitor establishment/specification | eye globe, optic vesicle, optic cup, neuroretina, retinal pigment epithelium, lens placode, retinal progenitor cell | 2019–2020 (plaisancie2019geneticsofanophthalmia pages 6-8, eintracht2020theuseof pages 8-9, harding2019themolecularbasis pages 19-20) |
| epidemiology / demographics | Rare congenital disorder spectrum with variable ascertainment by registry and clinic; childhood blindness burden is substantial | Prevalence estimates range ~1–3 or 1–4 per 10,000 live births; one prospective clinic cohort was 60% female but not population-representative | rare disease, congenital anomaly epidemiology | 2019, 2023 (plaisancie2019geneticsofanophthalmia pages 2-3, harding2023realworldclinicaland pages 1-2, harding2023realworldclinicaland pages 2-3) |
| diagnostics: clinical | Diagnosis is clinical plus imaging/biometry, with classification into simplex, mixed, complex, and syndromic vs non-syndromic; neuroimaging is important when bilateral or developmental concerns exist | Brain MRI abnormalities in 7/28 scanned prospective MAC patients; 6/7 with intracranial findings had bilateral MAC; neuroimaging abnormalities in 14/20 in the pediatric QoL cohort, corpus callosum dysgenesis 6/20 | ocular examination, axial length biometry, orbital MRI, neuroimaging, phenotype classification | 2022, 2023 (harding2023realworldclinicaland pages 2-3, harding2023realworldclinicaland pages 10-11, fahnehjelm2022anophthalmiaandmicrophthalmia pages 1-3) |
| diagnostics: molecular | Testing strategy should include gene panel/exome/genome plus CNV analysis; WGS/WES improves yield but many cases remain unsolved, especially milder/unilateral disease | >50% remain undiagnosed even after WES/WGS in review; clinic diagnostic rates ~28–34%; WGS yield 15.7% for MAC in Genomics England cohort; cES in nonisolated MAC 32.3–48.1% | gene panel, WES, WGS, chromosomal microarray, CNV analysis, HPO phenotyping | 2019–2024 (plaisancie2019geneticsofanophthalmia pages 1-2, harding2023realworldclinicaland pages 8-9, jackson2020moleculardiagnosticchallenges pages 1-2, kunisetty2024highclinicalexome pages 1-2) |
| diagnostic yield in real-world care | Both unilateral and bilateral cases merit testing; yields are not negligible in unilateral disease and CNVs can be important | Prospective Moorfields cohort: 28% overall solved among tested families, 33% in both unilateral and bilateral cohorts; aCGH 3/3, WGS 4/17, targeted panel 3/18, single-gene 1/1 | routine genetic testing, bilateral disease, unilateral disease, array CGH | 2023 (harding2023realworldclinicaland pages 8-9, harding2023realworldclinicaland pages 1-1, harding2023realworldclinicaland pages 10-11) |
| management / real-world implementation | No disease-restoring therapy is established; management is supportive, visual rehabilitation-focused, and often includes multidisciplinary genetics/ophthalmology care and socket/prosthetic planning | Review explicitly states “currently no treatments are available” for microphthalmia; in prospective care, 66% did not require custom prostheses and 7/50 were advised customized contact shells | supportive care, low vision care, ocular prosthesis, customized contact shell, multidisciplinary care, genetic counseling | 2021, 2023 (harding2021animalandcellular pages 21-22, harding2023realworldclinicaland pages 10-11) |
| prognosis / complications | Vision ranges from normal in fellow eye to blindness; complications depend on anatomy and associated anomalies; lifelong follow-up may be needed | In pediatric cohort, 10/35 were totally blind or had light perception; retinal detachment reported in 9% in prospective cohort and occurred from first to third decade | blindness, light perception only, retinal detachment, lifelong follow-up | 2022, 2023 (harding2023realworldclinicaland pages 9-10, fahnehjelm2022anophthalmiaandmicrophthalmia pages 1-3) |
| quality of life | Health-related quality of life is reduced in affected children/families | Parent-reported PedsQL median total score 52.4 (range 22.6–100) in ages 2–12 | quality of life impairment, pediatric QoL | 2022 (fahnehjelm2022anophthalmiaandmicrophthalmia pages 1-3) |
| prevention / counseling | Primary prevention is limited because many cases are monogenic/de novo, but molecular diagnosis informs recurrence risk, prenatal options, and family counseling; environmental contributors are recognized but incompletely quantified for isolated Mendelian cases | Reviews note both genetic and environmental causes; mosaicism and incomplete penetrance materially affect recurrence-risk counseling | genetic counseling, recurrence risk, prenatal diagnosis, environmental teratogen assessment | 2019–2021 (plaisancie2019geneticsofanophthalmia pages 1-2, harding2021animalandcellular pages 21-22) |
| model organisms | Mouse, zebrafish, Xenopus and human iPSC optic vesicles/cups are leading models; they reproduce many but not all human phenotypes | Review notes mouse, zebrafish and Xenopus as main systems; hiPSC optic cups effectively modeled VSX2-related microphthalmia; species differences limit direct translation | mouse model, zebrafish model, Xenopus model, hiPSC, optic vesicle organoid, optic cup organoid | 2020–2021 (eintracht2020theuseof pages 8-9, harding2019themolecularbasis pages 19-20, harding2021animalandcellular pages 21-22) |
| model-specific insights | Human iPSC models are particularly valuable for early human-specific fate defects and therapy screening, while animal models reveal conserved pathways and whole-organism effects | VSX2 null hiPSC vesicles showed WNT upregulation/RPE misexpression and pharmacologic rescue with WNT inhibition; zebrafish/CRISPR and mouse data support SOX2, PTCH1 and retinoid mechanisms | disease modeling, pathway rescue, human-specific developmental model | 2016–2020 (jackson2020moleculardiagnosticchallenges pages 9-10, eintracht2020theuseof pages 8-9, harding2019themolecularbasis pages 19-20) |


*Table: This compact table summarizes knowledge-base-ready findings for isolated anophthalmia-microphthalmia, including definitions, phenotypes, genes, mechanisms, diagnostics, care, prognosis, and models. It emphasizes that isolated A/M is a phenotypic category within a heterogeneous developmental eye-disorder spectrum rather than a single molecular entity.*

## 1. Disease information

### Definition and terminology

Common terms include **isolated anophthalmia**, **isolated microphthalmia**, **non-syndromic anophthalmia/microphthalmia**, **anophthalmia–microphthalmia spectrum**, and **A/M**. “Clinical anophthalmia” means no clinically visible eye despite possible residual tissue. MAC is broader and includes ocular coloboma; it should not be used as a synonym for isolated A/M.

Suggested ontology annotations are **HP:0000528 Anophthalmia**, **HP:0000568 Microphthalmia**, congenital onset, unilateral/bilateral involvement, and simple or complex microphthalmia. No single MONDO, OMIM, or Orphanet entry adequately represents every isolated A/M case because the phenotype spans numerous gene-specific disorders. The disease label should be linked to the relevant molecular diagnosis when known. Identifier mapping should be curated against the current MONDO/OMIM/Orphanet release rather than inferred from phenotype names. ICD coding is similarly phenotype-based and does not encode molecular subtype.

The evidence summarized here is primarily **aggregated disease-level evidence** from cohorts, reviews, and experimental studies—not individual EHR data. The 2023 Moorfields study is prospective real-world clinical data from 50 patients, while the 2022 pediatric study includes clinical records, examinations, neuroimaging, genetics, and parent-reported quality of life. (harding2023realworldclinicaland pages 1-1, fahnehjelm2022anophthalmiaandmicrophthalmia pages 1-3)

## 2. Etiology

### Genetic causes

Genetic disruption of early eye development is the principal established cause. More than 90–100 genes have been associated with A/M or MAC, but approximately 30 are recurrently implicated in non-syndromic families. Major classes include eye-field transcription factors, retinoid-pathway genes, BMP/TGF-β signaling genes, and regulators of optic-vesicle patterning. More than half of patients may remain molecularly undiagnosed after exome/genome sequencing, particularly those with unilateral or mild disease. (plaisancie2019geneticsofanophthalmia pages 1-2, harding2023realworldclinicaland pages 1-2)

**High-confidence genes include:**

* **SOX2:** usually heterozygous loss of function/haploinsufficiency; autosomal dominant, most often de novo, with parental germline or gonosomal mosaicism documented. Deletions, nonsense, frameshift, and missense variants occur. Reviews estimate SOX2 variants in 10–15% of all A/M and 15–40% of bilateral severe A/M. Missense variants affecting DNA-binding domains may have lower penetrance and milder ocular presentations. SOX2 disease can be isolated or syndromic. (harding2019themolecularbasis pages 15-17, plaisancie2019geneticsofanophthalmia pages 5-6)
* **OTX2:** heterozygous deletions, truncating, or missense variants; autosomal dominant with approximately 40–50% de novo occurrence, marked nonpenetrance, variable expressivity, and mosaicism. Estimates range from 0.7–10% of A/M. Together, SOX2 and OTX2 may explain at least 60% of some cohorts with bilateral severe A/M. (harding2019themolecularbasis pages 15-17, plaisancie2019geneticsofanophthalmia pages 6-8)
* **RAX:** biallelic loss-of-function or damaging variants; autosomal recessive, generally bilateral and severe. It accounts for roughly 2–3% of A/M in reviews. Heterozygous carriers are usually unaffected. Neurologic features in some individuals mean that a RAX diagnosis is not automatically “isolated.” (harding2019themolecularbasis pages 15-17)
* **VSX2/CHX10:** biallelic variants, usually causing bilateral microphthalmia, often with coloboma, cataract, glaucoma, or retinal dystrophy. The principal mechanism is defective retinal-progenitor specification and failure to suppress RPE fate. (plaisancie2019geneticsofanophthalmia pages 6-8, eintracht2020theuseof pages 8-9)
* **FOXE3:** biallelic variants are associated with bilateral non-syndromic microphthalmia/coloboma, whereas monoallelic variants can produce anterior-segment phenotypes. (harding2023realworldclinicaland pages 9-10)
* **ALDH1A3:** biallelic variants impair retinoic-acid synthesis. A 2023 series described nine affected people from seven families—four compound-heterozygous and three homozygous families—with bilateral A/M in every affected individual. Variants included missense, nonsense, and splice-site changes such as c.1144G>A p.(Gly382Arg), c.434C>T p.(Ala145Val), c.566G>A p.(Trp189*), and c.1233+2T>C. ALDH1A3 may explain approximately 11% of recessively inherited severe developmental eye anomalies. Neurodevelopmental findings were variably present, so isolated status must be assessed individually. (kesim2023clinicalandgenetic pages 2-3, kesim2023clinicalandgenetic pages 4-5, kesim2023clinicalandgenetic pages 1-2)
* **MAB21L2:** both dominant and recessive disease occur. Heterozygous p.Arg51 substitutions can cause severe bilateral disease and may operate through dominant-negative effects; homozygous p.Arg247Gln produced a milder phenotype in a consanguineous family. Protein destabilization is predicted for reported missense variants. (plaisancie2019geneticsofanophthalmia pages 9-11)
* Additional credible genes include **PAX6, VAX1, ATOH7, SALL2, SALL4, MAF, BMP4, BMP7, GDF3, GDF6, STRA6, RARB, ABCB6, TENM3, MFRP, PRSS56**, and **PTCH1**, although phenotype specificity and isolated-versus-syndromic presentation differ by gene and allele. (plaisancie2019geneticsofanophthalmia pages 2-3, reis2015conservedgeneticpathways pages 28-29)

Large deletions, duplications, regulatory variants, and other structural changes are also important. Chromosomal anomalies may account for up to approximately 15% of broadly ascertained MAC, although array-detectable abnormalities appear less frequent in strictly non-syndromic A/M. A 2023 prospective cohort identified deletions involving chromosomes 10, 11, and X. Regulatory variants remain underrepresented in exome-based studies, supporting WGS and CNV analysis. (harding2023realworldclinicaland pages 1-2, harding2023realworldclinicaland pages 8-9, plaisancie2019geneticsofanophthalmia pages 5-6)

Reported pathogenic variants are overwhelmingly **germline**, not somatic cancer mutations. Population frequencies should be compatible with rarity and inheritance—usually absent or extremely rare in gnomAD—but must be checked variant by variant. A blanket allele frequency cannot be assigned to the disease.

### Environmental and infectious factors

Early pregnancy is the critical environmental window. Reviews recognize maternal infection, vitamin-A/retinoid imbalance, alcohol or teratogenic drug exposure, and other first-trimester insults as potential causes of microphthalmia. Congenital toxoplasmosis and other TORCH infections belong in the differential, especially when ocular or neurologic inflammation is present. However, quantitative causal evidence specific to *isolated Mendelian* A/M is limited, and no environmental exposure should be presumed causal without an appropriate maternal, fetal, and infectious evaluation. (fahnehjelm2022anophthalmiaandmicrophthalmia pages 1-3, harding2021animalandcellular pages 21-22)

### Risk, protective, and gene–environment factors

Family history, parental mosaicism, consanguinity for recessive disease, and a previously affected pregnancy are major genetic risk indicators. No validated common susceptibility locus, protective allele, diet, or lifestyle intervention specifically prevents monogenic isolated A/M. Retinoic-acid biology provides biological plausibility for gene–environment interaction: variants in **STRA6, ALDH1A3**, or **RARB** perturb the same pathway influenced by vitamin-A availability and exogenous retinoids. Nevertheless, clinically actionable variant-by-exposure interaction estimates are unavailable. Avoidance of teratogenic retinoid exposure and appropriate maternal infection prevention are general pregnancy measures, not proven prevention for genetically determined A/M. (harding2019themolecularbasis pages 19-20)

## 3. Phenotypes

The defining findings are congenital unilateral or bilateral anophthalmia or microphthalmia. Severity ranges from a mildly short but organized globe to a tiny cystic remnant or absent globe. Involvement can be markedly asymmetric. The structural deficit itself is generally stable, but secondary ocular complications can emerge later. (plaisancie2019geneticsofanophthalmia pages 2-3, plaisancie2019geneticsofanophthalmia pages 1-2)

Associated ocular findings include coloboma, cataract, iris hypoplasia, anterior-segment dysgenesis, glaucoma, retinal dystrophy, optic-nerve abnormalities, orbital cyst, and retinal detachment. In the 2023 Moorfields cohort, 44% had non-MAC complex ocular features, cataract was the most frequent, and retinal detachment occurred in 9%, from the first through third decades. These figures come from a mixed MAC cohort and should not be interpreted as isolated-A/M-specific prevalence. (harding2023realworldclinicaland pages 9-10, harding2023realworldclinicaland pages 1-1)

Potential extraocular findings include developmental delay/intellectual disability, seizures, autism, pituitary or genital abnormalities, brain malformations, hearing loss, facial dysmorphism, and heart defects, depending on genotype. Their presence changes classification to syndromic or nonisolated disease. In a pediatric A/M cohort, only 16/35 were isolated; 19/35 had somatic, psychomotor, neuroradiologic, or genetic abnormalities. Neuroimaging was abnormal in 14/20, with corpus-callosum dysgenesis in 6/20. (fahnehjelm2022anophthalmiaandmicrophthalmia pages 1-3)

Visual function depends on laterality and retained anatomy. Bilateral severe A/M may produce profound blindness; unilateral cases may have useful or normal vision in the fellow eye but remain vulnerable to amblyopia and injury. Ten of 35 children in the 2022 cohort were totally blind or had only light perception. Parent-reported PedsQL in children aged 2–12 had a median total score of **52.4** (range 22.6–100), documenting substantial quality-of-life impact. (fahnehjelm2022anophthalmiaandmicrophthalmia pages 1-3)

Suggested HPO annotations include anophthalmia, microphthalmia, bilateral or unilateral involvement, ocular coloboma, cataract, glaucoma, retinal detachment, retinal dystrophy, optic-nerve hypoplasia, visual impairment/blindness, developmental delay, intellectual disability, seizures, corpus-callosum abnormality, sensorineural hearing impairment, and congenital heart defect. Phenotypes absent at the initial visit should not be encoded as definitively absent without age-appropriate examination.

## 4. Genetic and molecular information

The principal molecular mechanisms are:

1. **Haploinsufficiency/dosage loss:** typical of SOX2 and many OTX2 alleles.
2. **Biallelic loss of function:** typical of RAX, VSX2, ALDH1A3, and many FOXE3 presentations.
3. **Dominant-negative protein dysfunction:** proposed for specific heterozygous MAB21L2 missense substitutions.
4. **Regulatory/CNV mechanisms:** deletions or enhancer disruption can alter dosage without a coding SNV.
5. **Pathway dysregulation:** PTCH1 variants can produce overactive SHH signaling; retinoid genes alter morphogen synthesis/uptake; VSX2 loss dysregulates WNT and RPE/neural-retina fate. (harding2019themolecularbasis pages 15-17, plaisancie2019geneticsofanophthalmia pages 9-11, jackson2020moleculardiagnosticchallenges pages 9-10, harding2019themolecularbasis pages 19-20)

ClinVar classifications must be assessed per variant using ACMG/AMP criteria and phenotype/inheritance concordance. The 2024 exome study reclassified variants using contemporary ACMG criteria and found a 32.3–48.1% diagnostic range in 189 people with **nonisolated** MAC. It proposed low-penetrance MAC expansions involving **BRCA2, BRIP1, KAT6A, KAT6B, NSF, RAC1, SMARCA4, SMC1A**, and **TUBA1A**. These findings are relevant to differential diagnosis but should not be imported uncritically into an isolated-A/M gene set because the cohort was nonisolated and many genes are pleiotropic. (kunisetty2024highclinicalexome pages 1-2)

No reproducible modifier gene or protective allele is ready for clinical annotation. Epigenetic dysregulation is biologically plausible—especially for chromatin regulators—but there is no validated A/M-specific methylation signature, histone biomarker, metabolomic profile, proteomic marker, or circulating biomarker for routine diagnosis.

## 5. Environmental information

Environmental causation is best considered when genetic testing is negative, maternal history is suggestive, or infection-related findings are present. Relevant history includes first-trimester medication and retinoid exposure, alcohol and substance use, severe nutritional disturbance, febrile/infectious illness, occupational/chemical exposure, diabetes and other maternal disease, and prenatal imaging. Evidence for individual environmental risk factors remains heterogeneous and often combines A/M with other congenital eye anomalies.

There is no infectious transmission, zoonotic cycle, lifestyle contagion, or postnatal environmental trigger: A/M is a prenatal developmental malformation. Infection can be causal only through maternal–fetal exposure during development.

## 6. Mechanism and pathophysiology

### Causal chain

The upstream event is a pathogenic germline variant, CNV/regulatory alteration, or early embryonic environmental insult. This perturbs eye-field specification or signaling during the first trimester. SOX2 and OTX2 normally bind regulatory elements and activate **RAX, PAX6**, and **SIX3**; SHH separates the early eye field and patterns optic structures; BMP and retinoic-acid signals support lens placode and optic-cup morphogenesis; WNT/β-catenin favors RPE fate, while FGF and VSX2 support neural-retina specification. Failure at an early stage can abort globe formation (anophthalmia); partial failure reduces proliferation, invagination, or tissue specification, producing microphthalmia and associated coloboma or retinal/anterior-segment defects. (dash2020themastertranscription pages 3-3, eintracht2020theuseof pages 7-8, eintracht2020theuseof pages 4-7)

**Retinoid mechanism:** STRA6 mediates vitamin-A uptake; ALDH1A3 synthesizes retinoic acid; RARB transduces the signal. Disruption impairs ventral optic-cup and anterior-eye development. Raldh3-null mice show shortening of ventral retina, and STRA6 disruption produces microphthalmia in zebrafish. (harding2019themolecularbasis pages 19-20)

**VSX2–WNT mechanism:** patient-derived VSX2-null optic-vesicle models show elevated WNT11 and BMP8A, reduced FGF19, persistent MITF/RPE identity, and defective neural-retina/RPE boundary specification. WNT inhibition rescued aspects of the model phenotype, establishing pathway causality in vitro but not yet a prenatal or postnatal human therapy. (eintracht2020theuseof pages 8-9, harding2019themolecularbasis pages 19-20)

**SHH mechanism:** PTCH1 inhibits SHH signaling. Patient variants tested in zebrafish altered SHH signaling, and SOX2 was shown to bind and regulate PTCH1. The authors estimated PTCH1 variants could contribute to as much as 10% of broadly defined ocular developmental anomalies and proposed overactive SHH as a mechanism. This estimate is not specific to isolated A/M. (reis2015conservedgeneticpathways pages 28-29)

**Post-transcriptional SOX2 regulation:** RBM24 binds AU-rich elements in the SOX2 3′ UTR and stabilizes its mRNA. Rbm24 loss in mouse or zebrafish reduces Sox2 and produces anophthalmia/microphthalmia with ocular apoptosis and reduced Lhx2, Pax6, Jag1, E-cadherin, and crystallin expression. This is experimental model evidence, not yet a routinely recognized human A/M subtype. (dash2020themastertranscription pages 3-3)

Suggested GO concepts include eye-field specification, camera-type eye development, optic-vesicle morphogenesis, optic-cup morphogenesis, retina development, retinal-progenitor-cell proliferation, cell-fate specification, canonical WNT signaling, BMP signaling, SHH signaling, retinoic-acid biosynthesis/signaling, transcriptional regulation, and apoptosis. Suggested cell types are retinal progenitor cell, neuroepithelial cell, retinal pigment epithelial cell, lens epithelial cell, neural-crest-derived periocular mesenchymal cell, retinal neuron, and Müller glial cell.

There is no established primary inflammatory, autoimmune, fibrotic, mitochondrial, lysosomal, or metabolic-storage mechanism. Immune involvement is relevant chiefly to congenital infection, not inherited isolated A/M.

## 7. Anatomical structures affected

The primary organ is the eye and orbit. Developmentally implicated structures include the eye field, optic sulcus/vesicle, optic cup, neural retina, RPE, lens placode/lens, ciliary margin, optic nerve, and periocular mesenchyme. Severe loss of globe volume also affects postnatal orbital and facial growth.

Suggested UBERON concepts include eye, eyeball, orbit, optic vesicle, optic cup, neural retina, retinal pigment epithelium, lens, cornea, iris, ciliary body, optic nerve, and periocular mesenchyme. Relevant GO cellular compartments depend on gene product: SOX2, OTX2, RAX, VSX2, and FOXE3 act principally in the nucleus/chromatin; STRA6 is a plasma-membrane receptor/transporter; ALDH1A3 is a cytosolic enzyme; PTCH1 is a membrane protein.

Lateralization may be unilateral, bilateral, or asymmetric. Severe bilateral disease is more often molecularly diagnosed, but recent real-world data demonstrate meaningful yield in unilateral cases as well. (harding2023realworldclinicaland pages 1-1, harding2023realworldclinicaland pages 10-11)

## 8. Temporal development

A/M is **congenital**, with the causal developmental disturbance occurring during early embryonic eye formation. The structural deficit is permanent and is not a relapsing or remitting disorder. The visual and cosmetic consequences are lifelong.

Secondary manifestations can evolve: refractive error or amblyopia may become apparent in childhood; glaucoma, retinal dystrophy, or retinal detachment can develop later; orbital and facial asymmetry can become more apparent with growth. Retinal detachment occurred from the first to third decade in the prospective MAC series. (harding2023realworldclinicaland pages 9-10)

Critical windows are prenatal eye-field and optic-vesicle/cup development for causation, infancy/early childhood for orbital expansion and amblyopia management, and lifelong surveillance for complications. There is no spontaneous anatomical remission.

## 9. Inheritance and population

Inheritance may be autosomal dominant, autosomal recessive, X-linked in selected syndromic genes such as BCOR, or sporadic through de novo mutation/CNV. Dominant SOX2/OTX2 disease often shows incomplete penetrance, variable expressivity, and parental mosaicism. Recessive ALDH1A3, RAX, VSX2, and FOXE3 disease is enriched in consanguineous families, but compound heterozygosity occurs in nonconsanguineous families. (harding2019themolecularbasis pages 15-17, plaisancie2019geneticsofanophthalmia pages 6-8, kesim2023clinicalandgenetic pages 1-2)

No genetic anticipation is established. Germline/gonosomal mosaicism is clinically important because recurrence risk after an apparently de novo diagnosis is not zero. Founder variants may occur locally, but no universal founder effect or carrier frequency exists across this heterogeneous group. Carrier frequency must be calculated for the family’s gene and population.

No robust sex predilection is established. The 2023 clinic cohort was 60% female, but it was small and referral-based and should not be interpreted as a population sex ratio. (harding2023realworldclinicaland pages 2-3)

## 10. Diagnostics

### Clinical and imaging work-up

Diagnosis begins with comprehensive pediatric ophthalmologic examination: inspection for globe tissue, corneal diameter, axial length by ultrasound/biometry, anterior- and posterior-segment examination where possible, refraction, intraocular pressure, visual behavior/acuity, and evaluation of the fellow eye. Orbital ultrasound or MRI distinguishes absent globe, extreme microphthalmia, cyst, and other orbital lesions. Electrodiagnostic testing may characterize residual retinal function. (plaisancie2019geneticsofanophthalmia pages 2-3, harding2023realworldclinicaland pages 2-3)

Systemic assessment should include growth and development, neurologic examination, hearing, endocrine/genital assessment where SOX2/OTX2 is suspected, cardiac and renal examination as indicated, and dysmorphology/genetics review. Brain/orbital MRI is particularly appropriate for bilateral severe disease, developmental delay, seizures, optic-nerve abnormality, or suspected midline/pituitary involvement. In the 2023 cohort, 7/28 scanned patients had intracranial abnormalities, six of whom had bilateral MAC. (harding2023realworldclinicaland pages 10-11)

Prenatal ultrasound can detect absent or very small globes, and fetal MRI can clarify anatomy. A molecular diagnosis in a family permits targeted prenatal diagnosis or preimplantation genetic testing.

### Molecular testing strategy

A practical sequence is:

1. **Chromosomal microarray/CNV analysis**, especially with bilateral severe disease, dysmorphism, developmental findings, or multiple anomalies.
2. **Comprehensive developmental-eye-disorder panel** including dominant, recessive, and CNV-capable analysis.
3. **Trio exome or genome sequencing** if panel/CMA is nondiagnostic; WGS is preferred when regulatory, deep-intronic, structural, or complex variants are suspected.
4. **Reanalysis** as gene–disease knowledge improves and careful HPO terms are added.
5. Parental testing for phase, de novo status, and mosaicism.

Karyotyping or FISH is reserved for a suspected cytogenetic rearrangement; mitochondrial or repeat-expansion testing is not routine. RNA studies may help resolve splice variants but are not standard first-line diagnostics. (plaisancie2019geneticsofanophthalmia pages 5-6, jackson2020moleculardiagnosticchallenges pages 1-2, jackson2020moleculardiagnosticchallenges pages 9-10)

Real-world yields vary by cohort. In the 2023 Moorfields study, 11/39 families were solved (28%); non-syndromic cases had a 28% yield (8/29), and unilateral and bilateral groups each had a reported 33% rate. WGS solved 4/17, targeted panels 3/18, and aCGH 3/3, although the method-specific samples were too small for comparative effectiveness claims. (harding2023realworldclinicaland pages 8-9, harding2023realworldclinicaland pages 1-1)

In Genomics England, WGS yielded 15.7% for MAC. In contrast, 2024 clinical-exome analysis of 189 **nonisolated** MAC patients produced a 32.3–48.1% range, reflecting different definitions of a causal result. These data support sequencing but also demonstrate that diagnostic yield depends strongly on phenotype and interpretation. (jackson2020moleculardiagnosticchallenges pages 1-2, kunisetty2024highclinicalexome pages 1-2)

### Differential diagnosis

Important differentials include extreme microphthalmia versus true anophthalmia; microphthalmia with orbital cyst; isolated coloboma; cryptophthalmos/Fraser syndrome; congenital cystic eye; anterior-segment dysgenesis; nanophthalmos; congenital cataract obscuring a globe; retinopathy of prematurity or acquired phthisis; TORCH-related ocular destruction; and syndromic A/M such as SOX2 disorder, OTX2-related pituitary disease, STRA6-related Matthew-Wood syndrome, CHARGE, Lenz microphthalmia, and BCOR-related disease.

There are no serum, urine, biopsy, liquid-biopsy, proteomic, or metabolomic biomarkers diagnostic of isolated A/M. Histopathology is not required clinically.

## 11. Outcome and prognosis

Life expectancy is generally expected to be normal in genuinely isolated disease; mortality is driven by associated systemic malformations rather than the ocular anomaly itself. No validated 5- or 10-year survival statistics exist for isolated A/M.

Vision depends principally on bilaterality, residual retinal/optic-nerve development, coloboma, and fellow-eye status. Severe bilateral anophthalmia causes lifelong blindness; unilateral disease may preserve functional independence with protection and optimization of the fellow eye. The malformed globe does not recover anatomically. Secondary glaucoma, cataract, retinal dystrophy/detachment, amblyopia, socket contraction, prosthesis problems, and facial asymmetry contribute to morbidity. (harding2023realworldclinicaland pages 9-10, fahnehjelm2022anophthalmiaandmicrophthalmia pages 1-3)

Useful prognostic variables are laterality, axial length, residual retinal function, optic-nerve and brain imaging, associated ocular defects, developmental status, and molecular diagnosis. There is no validated prognostic molecular biomarker beyond genotype–phenotype correlations.

## 12. Treatment and current implementation

There is **no approved pharmacologic, gene, RNA, cell, or immune therapy that reconstructs an absent or severely malformed eye**. The 2021 model review states directly that “currently no treatments are available,” referring to disease-restoring treatment for microphthalmia. Management is therefore supportive, rehabilitative, cosmetic, and complication-directed. (harding2021animalandcellular pages 21-22)

Key interventions include:

* Early low-vision and developmental services; orientation/mobility training for bilateral visual loss.
* Refraction, amblyopia treatment, and treatment of cataract, glaucoma, retinal detachment, or other remediable pathology.
* Polycarbonate protection for a functional fellow eye.
* Serial socket conformers, customized contact shells, or prosthetic eyes to support orbital symmetry and cosmesis; selected severe sockets may require expandable implants or reconstructive surgery.
* Psychosocial support and school accommodations.
* Multidisciplinary ophthalmology, oculoplastics, ocularist, clinical genetics, pediatrics, neurology/endocrinology, and rehabilitation care according to genotype and findings.

In the Moorfields real-world cohort, 66% did not need customized prostheses, while 7/50 were advised customized contact shells because of small eye size. These figures illustrate individualized care rather than a universal treatment algorithm. (harding2023realworldclinicaland pages 10-11)

Suggested NCIT intervention concepts include genetic counseling, ophthalmologic examination, magnetic resonance imaging, ocular ultrasound, low-vision rehabilitation, ocular prosthesis, reconstructive surgery, cataract surgery, glaucoma treatment, and retinal-detachment repair. No A/M-specific pharmacogenomic guidance exists.

The clinical-trial search found socket/prosthetic or imaging studies but **no active disease-modifying trial specifically restoring congenital isolated A/M**. Experimental WNT rescue in VSX2-mutant optic vesicles is a mechanistic proof of concept, not a human treatment. (eintracht2020theuseof pages 8-9, harding2019themolecularbasis pages 19-20)

## 13. Prevention

Primary prevention is limited for monogenic or de novo disease. General measures include avoiding known teratogenic retinoids, optimizing maternal health and nutrition without excessive vitamin A, preventing and treating maternal infections, and reviewing medications before pregnancy. There is no A/M-specific vaccine or prophylactic drug.

Secondary prevention consists of prenatal imaging in high-risk pregnancies, targeted prenatal testing when a familial variant is known, newborn eye examination, prompt molecular diagnosis, and early screening for syndromic manifestations. Population newborn biochemical screening is not applicable.

Tertiary prevention includes early orbital/socket management, amblyopia prevention, protection of the fellow eye, surveillance for glaucoma and retinal detachment, low-vision rehabilitation, and developmental/educational support.

Genetic counseling should explain gene-specific inheritance, incomplete penetrance, variable expressivity, and mosaicism. Reproductive options include natural conception with targeted prenatal diagnosis, IVF with preimplantation genetic testing for a known familial variant, donor gametes, and adoption. Recurrence risk cannot be assigned from the phenotype alone.

## 14. Other species and natural disease

Congenital microphthalmia/anophthalmia occurs naturally in domestic and laboratory animals, but this review retrieved stronger experimental than veterinary natural-history evidence. Species relevant to comparative biology include **Mus musculus** (NCBI Taxon 10090), **Danio rerio** (7955), and **Xenopus** species, with conserved orthologs of SOX2, OTX2, RAX, VSX2, ALDH1A3, PTCH1, and BMP-pathway genes. No zoonotic transmission is possible because this is a developmental phenotype, not an infectious disease.

Breed-specific VBO annotations, veterinary prevalence, and natural founder variants require separate OMIA/VBO curation; they are not established by the retrieved evidence.

## 15. Model organisms and advanced technologies

Mouse, zebrafish, Xenopus, and chick models have defined conserved eye-field, retinoid, BMP, WNT, and SHH pathways. Knockout, knockdown, CRISPR, and dosage-sensitive models of Sox2, Otx2, Rax, Vsx2, Raldh3/Aldh1a3, Stra6, Ptch1, Bmp7, and Rbm24 reproduce anophthalmia, microphthalmia, retinal-patterning defects, or related ocular phenotypes. (harding2019themolecularbasis pages 19-20, harding2021animalandcellular pages 21-22, reis2015conservedgeneticpathways pages 28-29)

Species differences are important. For example, zebrafish double loss of vsx genes can preserve neural-retina specification despite severe bipolar-cell depletion, whereas mammalian VSX2 loss produces microphthalmia. Corneal timing, neural-crest migration, retinal regeneration, and gene redundancy differ across organisms, limiting direct extrapolation. (harding2019themolecularbasis pages 19-20)

Patient-derived **hiPSC optic vesicles/cups** are the most clinically relevant emerging platform. They recapitulate human fetal developmental transcriptional programs and can model patient-specific defects. VSX2-null vesicles demonstrated WNT upregulation and RPE mis-specification, with partial pathway rescue by WNT inhibition. Such organoids lack complete vasculature, immune interactions, and whole-orbit biomechanics, but they provide a platform for functional variant analysis and drug screening. (eintracht2020theuseof pages 8-9, eintracht2020theuseof pages 4-7)

Single-cell transcriptomics and spatial methods are promising for mapping human eye-development cell states, but no validated isolated-A/M single-cell, spatial, proteomic, metabolomic, or multi-omic clinical signature is currently available. The main immediate application is mechanistic research rather than diagnosis.

## Recent developments and expert interpretation

* **2023 real-world management:** Harding et al., published October 2023, prospectively studied 50 MAC patients and found 44% complex ocular disease, 34% systemic involvement, and a 28% family-level molecular yield. Their conclusion supports routine testing in unilateral as well as bilateral cases. DOI: https://doi.org/10.1136/bjo-2022-321991. (harding2023realworldclinicaland pages 1-1)
* **2023 ALDH1A3 expansion:** Kesim et al., published March 2023, reported seven families with biallelic variants. The abstract states: “All affected individuals had bilateral anophthalmia/microphthalmia,” while neurodevelopmental features showed marked variability. DOI: https://doi.org/10.1038/s41431-023-01342-8. (kesim2023clinicalandgenetic pages 1-2)
* **2024 clinical exomes:** Kunisetty et al., published March 19, 2024, found cES efficacy of 32.3–48.1% in 189 nonisolated MAC cases and emphasized that many implicated genes were absent from commercial ophthalmic panels. DOI: https://doi.org/10.1167/iovs.65.3.25. This result supports broad exome/genome testing but does not directly define isolated A/M yield. (kunisetty2024highclinicalexome pages 1-2)
* **Human developmental models:** Patient-derived optic-vesicle studies show that developmental pathway defects can be modeled and pharmacologically modulated in vitro. Experts regard these systems as valuable for discovering targets, but prenatal timing and irreversible structural loss make postnatal translation especially challenging. (eintracht2020theuseof pages 8-9, harding2019themolecularbasis pages 19-20)

## Evidence limitations

Published cohorts frequently combine anophthalmia, microphthalmia, and coloboma and mix isolated with syndromic disease. Consequently, many frequencies in this report are MAC-wide and are explicitly labeled as such. Gene-specific penetrance, carrier frequency, environmental effect sizes, treatment-response rates, survival statistics, and population-stratified prevalence are generally unavailable. Exact PMIDs were not present in the retrieved full-text metadata; DOI URLs and publication dates are therefore supplied rather than risking incorrect PMID assignment.

References

1. (plaisancie2019geneticsofanophthalmia pages 2-3): Julie Plaisancié, Fabiola Ceroni, R. Holt, C. Z. Seco, P. Calvas, N. Chassaing, and N. Ragge. Genetics of anophthalmia and microphthalmia. part 1: non-syndromic anophthalmia/microphthalmia. Human Genetics, 138:799-830, Feb 2019. URL: https://doi.org/10.1007/s00439-019-01977-y, doi:10.1007/s00439-019-01977-y. This article has 136 citations and is from a peer-reviewed journal.

2. (plaisancie2019geneticsofanophthalmia pages 1-2): Julie Plaisancié, Fabiola Ceroni, R. Holt, C. Z. Seco, P. Calvas, N. Chassaing, and N. Ragge. Genetics of anophthalmia and microphthalmia. part 1: non-syndromic anophthalmia/microphthalmia. Human Genetics, 138:799-830, Feb 2019. URL: https://doi.org/10.1007/s00439-019-01977-y, doi:10.1007/s00439-019-01977-y. This article has 136 citations and is from a peer-reviewed journal.

3. (harding2023realworldclinicaland pages 2-3): Philippa Harding, Sri Gore, Samantha Malka, Jayashree Rajkumar, Ngozi Oluonye, and Mariya Moosajee. Real-world clinical and molecular management of 50 prospective patients with microphthalmia, anophthalmia and/or ocular coloboma. The British Journal of Ophthalmology, 107:1925-1935, Oct 2023. URL: https://doi.org/10.1136/bjo-2022-321991, doi:10.1136/bjo-2022-321991. This article has 27 citations.

4. (harding2023realworldclinicaland pages 1-2): Philippa Harding, Sri Gore, Samantha Malka, Jayashree Rajkumar, Ngozi Oluonye, and Mariya Moosajee. Real-world clinical and molecular management of 50 prospective patients with microphthalmia, anophthalmia and/or ocular coloboma. The British Journal of Ophthalmology, 107:1925-1935, Oct 2023. URL: https://doi.org/10.1136/bjo-2022-321991, doi:10.1136/bjo-2022-321991. This article has 27 citations.

5. (harding2023realworldclinicaland pages 9-10): Philippa Harding, Sri Gore, Samantha Malka, Jayashree Rajkumar, Ngozi Oluonye, and Mariya Moosajee. Real-world clinical and molecular management of 50 prospective patients with microphthalmia, anophthalmia and/or ocular coloboma. The British Journal of Ophthalmology, 107:1925-1935, Oct 2023. URL: https://doi.org/10.1136/bjo-2022-321991, doi:10.1136/bjo-2022-321991. This article has 27 citations.

6. (harding2023realworldclinicaland pages 8-9): Philippa Harding, Sri Gore, Samantha Malka, Jayashree Rajkumar, Ngozi Oluonye, and Mariya Moosajee. Real-world clinical and molecular management of 50 prospective patients with microphthalmia, anophthalmia and/or ocular coloboma. The British Journal of Ophthalmology, 107:1925-1935, Oct 2023. URL: https://doi.org/10.1136/bjo-2022-321991, doi:10.1136/bjo-2022-321991. This article has 27 citations.

7. (plaisancie2019geneticsofanophthalmia pages 6-8): Julie Plaisancié, Fabiola Ceroni, R. Holt, C. Z. Seco, P. Calvas, N. Chassaing, and N. Ragge. Genetics of anophthalmia and microphthalmia. part 1: non-syndromic anophthalmia/microphthalmia. Human Genetics, 138:799-830, Feb 2019. URL: https://doi.org/10.1007/s00439-019-01977-y, doi:10.1007/s00439-019-01977-y. This article has 136 citations and is from a peer-reviewed journal.

8. (fahnehjelm2022anophthalmiaandmicrophthalmia pages 1-3): Cecilia Fahnehjelm, Eva Dafgård Kopp, Josephine Wincent, Evin Güven, Mattias Nilsson, Monica Olsson, and Kristina Teär Fahnehjelm. Anophthalmia and microphthalmia in children: associated ocular, somatic and genetic morbidities and quality of life. Ophthalmic Genetics, 43:172-183, Feb 2022. URL: https://doi.org/10.1080/13816810.2021.1989600, doi:10.1080/13816810.2021.1989600. This article has 21 citations and is from a peer-reviewed journal.

9. (harding2019themolecularbasis pages 15-17): Philippa Harding and Mariya Moosajee. The molecular basis of human anophthalmia and microphthalmia. Journal of Developmental Biology, 7:16, Aug 2019. URL: https://doi.org/10.3390/jdb7030016, doi:10.3390/jdb7030016. This article has 103 citations.

10. (plaisancie2019geneticsofanophthalmia pages 5-6): Julie Plaisancié, Fabiola Ceroni, R. Holt, C. Z. Seco, P. Calvas, N. Chassaing, and N. Ragge. Genetics of anophthalmia and microphthalmia. part 1: non-syndromic anophthalmia/microphthalmia. Human Genetics, 138:799-830, Feb 2019. URL: https://doi.org/10.1007/s00439-019-01977-y, doi:10.1007/s00439-019-01977-y. This article has 136 citations and is from a peer-reviewed journal.

11. (plaisancie2019geneticsofanophthalmia pages 9-11): Julie Plaisancié, Fabiola Ceroni, R. Holt, C. Z. Seco, P. Calvas, N. Chassaing, and N. Ragge. Genetics of anophthalmia and microphthalmia. part 1: non-syndromic anophthalmia/microphthalmia. Human Genetics, 138:799-830, Feb 2019. URL: https://doi.org/10.1007/s00439-019-01977-y, doi:10.1007/s00439-019-01977-y. This article has 136 citations and is from a peer-reviewed journal.

12. (kesim2023clinicalandgenetic pages 1-2): Yesim Kesim, Fabiola Ceroni, Alejandra Damián, Fiona Blanco-Kelly, Carmen Ayuso, Kathy Williamson, Véronique Paquis-Flucklinger, Dorine A Bax, Julie Plaisancié, Claudine Rieubland, Mostafa Chamlal, Marta Cortón, Nicolas Chassaing, Patrick Calvas, and Nicola K Ragge. Clinical and genetic analysis further delineates the phenotypic spectrum of aldh1a3-related anophthalmia and microphthalmia. European Journal of Human Genetics, 31:1175-1180, Mar 2023. URL: https://doi.org/10.1038/s41431-023-01342-8, doi:10.1038/s41431-023-01342-8. This article has 7 citations and is from a domain leading peer-reviewed journal.

13. (dash2020themastertranscription pages 3-3): Soma Dash, Lindy K Brastrom, Shaili D Patel, C Anthony Scott, Diane C Slusarski, and Salil A Lachke. The master transcription factor sox2, mutated in anophthalmia/microphthalmia, is post-transcriptionally regulated by the conserved rna-binding protein rbm24 in vertebrate eye development. Human Molecular Genetics, 29(4):591-604, Dec 2020. URL: https://doi.org/10.1093/hmg/ddz278, doi:10.1093/hmg/ddz278. This article has 54 citations and is from a domain leading peer-reviewed journal.

14. (eintracht2020theuseof pages 7-8): Jonathan Eintracht, Maria Toms, and Mariya Moosajee. The use of induced pluripotent stem cells as a model for developmental eye disorders. Frontiers in Cellular Neuroscience, Aug 2020. URL: https://doi.org/10.3389/fncel.2020.00265, doi:10.3389/fncel.2020.00265. This article has 28 citations.

15. (reis2015conservedgeneticpathways pages 28-29): Linda M. Reis and Elena V. Semina. Conserved genetic pathways associated with microphthalmia, anophthalmia, and coloboma. Birth defects research. Part C, Embryo today : reviews, 105 2:96-113, Jun 2015. URL: https://doi.org/10.1002/bdrc.21097, doi:10.1002/bdrc.21097. This article has 91 citations.

16. (jackson2020moleculardiagnosticchallenges pages 9-10): Daniel Jackson, Samantha Malka, Philippa Harding, Juliana Palma, Hannah Dunbar, and Mariya Moosajee. Molecular diagnostic challenges for non‐retinal developmental eye disorders in the united kingdom. American Journal of Medical Genetics. Part C, Seminars in Medical Genetics, 184:578-589, Aug 2020. URL: https://doi.org/10.1002/ajmg.c.31837, doi:10.1002/ajmg.c.31837. This article has 55 citations.

17. (eintracht2020theuseof pages 8-9): Jonathan Eintracht, Maria Toms, and Mariya Moosajee. The use of induced pluripotent stem cells as a model for developmental eye disorders. Frontiers in Cellular Neuroscience, Aug 2020. URL: https://doi.org/10.3389/fncel.2020.00265, doi:10.3389/fncel.2020.00265. This article has 28 citations.

18. (harding2019themolecularbasis pages 19-20): Philippa Harding and Mariya Moosajee. The molecular basis of human anophthalmia and microphthalmia. Journal of Developmental Biology, 7:16, Aug 2019. URL: https://doi.org/10.3390/jdb7030016, doi:10.3390/jdb7030016. This article has 103 citations.

19. (harding2023realworldclinicaland pages 10-11): Philippa Harding, Sri Gore, Samantha Malka, Jayashree Rajkumar, Ngozi Oluonye, and Mariya Moosajee. Real-world clinical and molecular management of 50 prospective patients with microphthalmia, anophthalmia and/or ocular coloboma. The British Journal of Ophthalmology, 107:1925-1935, Oct 2023. URL: https://doi.org/10.1136/bjo-2022-321991, doi:10.1136/bjo-2022-321991. This article has 27 citations.

20. (jackson2020moleculardiagnosticchallenges pages 1-2): Daniel Jackson, Samantha Malka, Philippa Harding, Juliana Palma, Hannah Dunbar, and Mariya Moosajee. Molecular diagnostic challenges for non‐retinal developmental eye disorders in the united kingdom. American Journal of Medical Genetics. Part C, Seminars in Medical Genetics, 184:578-589, Aug 2020. URL: https://doi.org/10.1002/ajmg.c.31837, doi:10.1002/ajmg.c.31837. This article has 55 citations.

21. (kunisetty2024highclinicalexome pages 1-2): Bhavana Kunisetty, Bailey A. Martin-Giacalone, Xiaonan Zhao, Pamela N. Luna, Brian P. Brooks, Robert B. Hufnagel, Chad A. Shaw, Jill A. Rosenfeld, A. J. Agopian, Philip J. Lupo, and Daryl A. Scott. High clinical exome sequencing diagnostic rates and novel phenotypic expansions for nonisolated microphthalmia, anophthalmia, and coloboma. Investigative Opthalmology &amp; Visual Science, 65:25, Mar 2024. URL: https://doi.org/10.1167/iovs.65.3.25, doi:10.1167/iovs.65.3.25. This article has 8 citations.

22. (harding2023realworldclinicaland pages 1-1): Philippa Harding, Sri Gore, Samantha Malka, Jayashree Rajkumar, Ngozi Oluonye, and Mariya Moosajee. Real-world clinical and molecular management of 50 prospective patients with microphthalmia, anophthalmia and/or ocular coloboma. The British Journal of Ophthalmology, 107:1925-1935, Oct 2023. URL: https://doi.org/10.1136/bjo-2022-321991, doi:10.1136/bjo-2022-321991. This article has 27 citations.

23. (harding2021animalandcellular pages 21-22): Philippa Harding, Dulce Lima Cunha, and Mariya Moosajee. Animal and cellular models of microphthalmia. Therapeutic Advances in Rare Disease, Jan 2021. URL: https://doi.org/10.1177/2633004021997447, doi:10.1177/2633004021997447. This article has 15 citations.

24. (kesim2023clinicalandgenetic pages 2-3): Yesim Kesim, Fabiola Ceroni, Alejandra Damián, Fiona Blanco-Kelly, Carmen Ayuso, Kathy Williamson, Véronique Paquis-Flucklinger, Dorine A Bax, Julie Plaisancié, Claudine Rieubland, Mostafa Chamlal, Marta Cortón, Nicolas Chassaing, Patrick Calvas, and Nicola K Ragge. Clinical and genetic analysis further delineates the phenotypic spectrum of aldh1a3-related anophthalmia and microphthalmia. European Journal of Human Genetics, 31:1175-1180, Mar 2023. URL: https://doi.org/10.1038/s41431-023-01342-8, doi:10.1038/s41431-023-01342-8. This article has 7 citations and is from a domain leading peer-reviewed journal.

25. (kesim2023clinicalandgenetic pages 4-5): Yesim Kesim, Fabiola Ceroni, Alejandra Damián, Fiona Blanco-Kelly, Carmen Ayuso, Kathy Williamson, Véronique Paquis-Flucklinger, Dorine A Bax, Julie Plaisancié, Claudine Rieubland, Mostafa Chamlal, Marta Cortón, Nicolas Chassaing, Patrick Calvas, and Nicola K Ragge. Clinical and genetic analysis further delineates the phenotypic spectrum of aldh1a3-related anophthalmia and microphthalmia. European Journal of Human Genetics, 31:1175-1180, Mar 2023. URL: https://doi.org/10.1038/s41431-023-01342-8, doi:10.1038/s41431-023-01342-8. This article has 7 citations and is from a domain leading peer-reviewed journal.

26. (eintracht2020theuseof pages 4-7): Jonathan Eintracht, Maria Toms, and Mariya Moosajee. The use of induced pluripotent stem cells as a model for developmental eye disorders. Frontiers in Cellular Neuroscience, Aug 2020. URL: https://doi.org/10.3389/fncel.2020.00265, doi:10.3389/fncel.2020.00265. This article has 28 citations.

## Artifacts

- [Edison artifact artifact-00](Isolated_Anophthalmia-Microphthalmia_Syndrome-deep-research-falcon_artifacts/artifact-00.md)