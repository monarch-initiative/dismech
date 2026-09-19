---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T11:47:17.791312'
end_time: '2026-08-01T12:02:44.245271'
duration_seconds: 926.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dilated Cardiomyopathy 1AA
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Dilated_Cardiomyopathy_1AA-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 1AA
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1AA** covering all of the
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
- **Disease Name:** Dilated Cardiomyopathy 1AA
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1AA** covering all of the
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


# Dilated Cardiomyopathy 1AA (ACTN2-related cardiomyopathy): comprehensive disease-characteristics report

## Executive summary and scope

**Dilated cardiomyopathy 1AA (DCM1AA)** is a legacy subtype designation for rare, usually familial cardiomyopathy attributed to pathogenic variation in **ACTN2**, which encodes the Z-disc protein α-actinin-2. Modern evidence supports viewing it as part of an **ACTN2-related intrinsic cardiomyopathy spectrum**, rather than as a uniformly dilated phenotype: reported manifestations include dilated cardiomyopathy (DCM), left-ventricular noncompaction (LVNC), arrhythmogenic presentations, hypertrophic cardiomyopathy (HCM), and—particularly with biallelic truncation—restrictive cardiomyopathy (RCM). Open Targets links ACTN2 to general DCM (MONDO:0005021), familial DCM (MONDO:0016333), and familial isolated DCM (MONDO:0700335), but the retrieved current resources did **not** expose a reliable distinct MONDO record specifically labelled “DCM1AA.” Therefore, database ingestion should retain the legacy name while mapping primarily to **ACTN2-related cardiomyopathy/familial DCM**, with the phenotype recorded separately. (OpenTargets Search: dilated cardiomyopathy-ACTN2, lindholm2021monoandbiallelic pages 1-3)

The evidence base is small and variant-specific. The first ACTN2 missense variant in a DCM patient was reported in 2003 (Mohapatra et al.; PMID **14567970**). Later studies provided segregation and functional evidence for dominant disease and demonstrated recessive disease from a homozygous C-terminal truncation. Accordingly, epidemiologic, penetrance, prognosis, and treatment estimates for general DCM must not be misrepresented as DCM1AA-specific. (lindholm2021monoandbiallelic pages 1-3, lindholm2021monoandbiallelic pages 3-4)

| domain | best-supported finding | evidence type | key quantitative detail or variant | source/year |
|---|---|---|---|---|
| Identity / causal gene | Dilated Cardiomyopathy 1AA is best interpreted as rare ACTN2-related familial/intrinsic dilated cardiomyopathy within a broader ACTN2 cardiomyopathy spectrum; modern resources strongly support ACTN2 as a DCM-associated target, but a distinct current MONDO record for the legacy subtype label is not clearly exposed | Curated disease-target association + review + primary human genetics | ACTN2 association score present for dilated cardiomyopathy/familial DCM; first DCM ACTN2 report noted in 2003 | Open Targets / literature synthesis 2024-2025 (OpenTargets Search: dilated cardiomyopathy-ACTN2, lindholm2021monoandbiallelic pages 1-3) |
| Inheritance | ACTN2 cardiomyopathy can be autosomal dominant or recessive depending on variant class; dominant disease is supported for heterozygous indel/missense variants, while recessive severe disease is supported for homozygous truncation | Human clinical genetics + family segregation + functional validation | Heterozygous exon 8-10 deletion family; homozygous p.Gln860Ter (Q860X) restrictive/end-stage phenotype; recessive causality established | Lindholm et al. 2021 (lindholm2021monoandbiallelic pages 1-3, lindholm2021monoandbiallelic pages 3-4, lindholm2021monoandbiallelic pages 4-6) |
| Phenotypic spectrum | ACTN2 variants cause a mixed cardiomyopathy spectrum including DCM, arrhythmic phenotypes, LV noncompaction, restrictive cardiomyopathy, heart failure, and sudden death in some families | Human clinical + review | Family 2 had ventricular tachyarrhythmias, atrial fibrillation, LV noncompaction, symptomatic HF, and 2 early sudden cardiac deaths; Q860X patient required transplant at 23 years | Lindholm et al. 2021; review synthesis 2024 (lindholm2021monoandbiallelic pages 3-4, micolonghi2024unveilingthespectrum pages 29-30) |
| Core mechanism | Disease mechanisms converge on Z-disc/sarcomere dysfunction with impaired contractility, structural disarray, abnormal Ca2+ handling, and disrupted protein interactions; mechanism differs by zygosity | iPSC-CM, EM, RNA-seq, AP-MS, CRISPR | Heterozygous indel protein incorporates into sarcomeres with aberrant Z-disc ultrastructure; C-terminal truncation disrupts ACTN1 and GJA1 interactions | Lindholm et al. 2021 (lindholm2021monoandbiallelic pages 1-3, lindholm2021monoandbiallelic pages 8-9, lindholm2021monoandbiallelic pages 4-6) |
| Recent 2023 mouse study | A CRISPR knock-in Actn2 p.Met228Thr mouse provided recent in vivo evidence that ACTN2 dysfunction can drive cardiomyopathy-related biology via protein instability, mitochondrial dysfunction, and cell-cycle abnormalities | Mouse model + proteomics | Heterozygotes had no overt phenotype except molecular changes in mature males; homozygotes were embryonic lethal at/after E15.5 analysis | Broadway-Stringer et al. 2023 (broadwaystringer2023insightsintothe pages 1-2, broadwaystringer2023insightsintothe pages 2-4) |
| 2023 human deletion case | A pediatric case with 1q43 deletion involving ACTN2 and RYR2 linked ACTN2 loss to severe early-onset DCM with LV noncompaction and reduced EF | Human case report | chr1:236,686,454-237,833,988 (hg38) deletion; enlarged LV with LVIDd 48 mm, Z-score 3.81; follow-up LVEF 41%; transplant recommended | Zhou et al. 2023 (zhou2023impairedcardiomyocytematuration pages 3-7, zhou2023impairedcardiomyocytematuration pages 7-8) |
| Molecular profiling | ACTN2 disease models show transcriptional and proteomic abnormalities consistent with fibrosis, hypertrophy, metabolic remodeling, and altered interaction networks | RNA-seq + GSEA + proteomics | Elevated MYL2; enriched extracellular matrix remodeling/collagen biosynthesis in Q860X tissue; induced respiratory electron transport and gluconeogenesis in hiPSC-CMs | Lindholm et al. 2021 (lindholm2021monoandbiallelic pages 3-4, lindholm2021monoandbiallelic pages 4-6) |
| Developmental / model evidence | Loss of ACTN2 perturbs cardiomyocyte maturation and cardiac development; zebrafish and mammalian models support reduced chamber/cell size and structural defects | Zebrafish LOF + mouse + human case synthesis | Zebrafish ACTN2 depletion reduced end-diastolic diameter, cardiomyocyte size/number, and ventricular chamber size; ACTN3 could not rescue LOF phenotype | Wadmore 2021; Lindholm 2021; Zhou 2023 (lindholm2021monoandbiallelic pages 8-9, wadmore2021theroleof pages 2-4, zhou2023impairedcardiomyocytematuration pages 7-8) |
| Diagnosis / prognosis | For DCM generally, diagnosis relies on multimodal imaging and genetics; prognosis is informed by genotype and CMR fibrosis burden more than EF alone in some contexts | Guideline review + population study + meta-analysis | DCM true prevalence estimated about 1:250 and 1:220 by UK Biobank CMR; in NIDCM, LGE HR 1.81 for all-cause mortality and 2.69 for arrhythmic events; Q860X patient progressed to transplant | Newman 2024; Eichhorn 2024; Lindholm 2021 (newman2024dilatedcardiomyopathya pages 1-2, eichhorn2024riskstratificationin pages 1-2, lindholm2021monoandbiallelic pages 3-4) |
| Current treatment status | No ACTN2-specific approved therapy or ACTN2-directed clinical trial was found; management follows standard DCM/HFrEF care, arrhythmia surveillance, family screening, devices, and advanced HF therapies when indicated | Guideline review + trial landscape + case report | Standard “quadruple” HFrEF drug classes apply broadly; pediatric deletion case received digoxin, captopril, metoprolol, levocarnitine/creatine phosphate, but remained severe; no ACTN2-specific interventional trial identified | Badger 2023 / MacDonald 2023 summaries, trial search, Zhou 2023 (zhou2023impairedcardiomyocytematuration pages 3-7) |
| Major evidence gaps | Evidence remains sparse, mostly case-based, with limited penetrance data, no subtype-specific epidemiology, and no validated preventive or genotype-specific treatment pathway for ACTN2-DCM | Evidence-gap synthesis | Do not overstate prevalence for DCM1AA specifically; available epidemiology/penetrance figures are for broader DCM gene sets or general DCM, not ACTN2 subtype alone | Shah 2022; Newman 2024; review synthesis 2024 (shah2022frequencypenetranceand pages 10-12, newman2024dilatedcardiomyopathya pages 1-2, micolonghi2024unveilingthespectrum pages 29-30) |


*Table: This table summarizes the strongest currently available evidence for Dilated Cardiomyopathy 1AA as ACTN2-related cardiomyopathy, separating subtype-specific findings from broader DCM context. It is useful for quickly identifying what is well supported, what remains generic to DCM, and where major evidence gaps remain.*

## 1. Disease information

### Definition

DCM is a myocardial disorder characterized by ventricular systolic dysfunction and chamber dilation not explained solely by abnormal loading or coronary disease. In DCM1AA, the initiating lesion is germline ACTN2 dysfunction, affecting the sarcomeric Z-disc, force transmission, mechanosignaling, calcium handling, and cardiomyocyte maturation. ACTN2 is highly expressed in cardiac and skeletal muscle and cross-links actin and titin at the Z-disc. (lindholm2021monoandbiallelic pages 1-3, broadwaystringer2023insightsintothe pages 1-2)

### Identifiers and nomenclature

- **Preferred knowledge-base label:** ACTN2-related dilated cardiomyopathy / ACTN2-related intrinsic cardiomyopathy.
- **Legacy synonym:** Dilated cardiomyopathy 1AA; DCM1AA; familial dilated cardiomyopathy due to ACTN2.
- **Gene:** ACTN2, actinin alpha 2; Ensembl **ENSG00000077522**; chromosome **1q42–q43**.
- **MONDO mappings supported by retrieved curation:** DCM **MONDO:0005021**; familial DCM **MONDO:0016333**; familial isolated DCM **MONDO:0700335**. A unique DCM1AA MONDO identifier was not verified. (OpenTargets Search: dilated cardiomyopathy-ACTN2)
- **Broad clinical coding:** ICD-10-CM **I42.0** (dilated cardiomyopathy); ICD-11 generally classifies it under dilated cardiomyopathy. These phenotype codes do not encode ACTN2 etiology.
- **MeSH:** Dilated Cardiomyopathy.
- **OMIM:** ACTN2 is the implicated locus; because legacy numbered DCM labels have changed across resources, the exact DCM1AA OMIM number should be verified directly in the live OMIM record before ingestion rather than inferred from secondary sources.

The present report is based on **aggregated disease-level resources, published families, individual case reports, and experimental models**, not longitudinal EHR-derived patient data.

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factors

The primary cause is a **germline ACTN2 variant** that disrupts α-actinin-2 structure, abundance, localization, or interactions. Both monoallelic and biallelic mechanisms occur:

1. **Dominant-negative or altered-function disease:** a truncated or missense protein remains expressed and may incorporate into the Z-disc, disrupting sarcomeric architecture.
2. **Loss-of-function/haploinsufficiency:** large deletions or destabilizing variants reduce functional α-actinin-2.
3. **Recessive truncation:** homozygous p.Gln860Ter causes loss of the C-terminal interaction region and severe early disease. Lindholm et al. concluded that their data “**establish recessive inheritance of ACTN2 truncation as causative of disease**.” (lindholm2021monoandbiallelic pages 1-3, lindholm2021monoandbiallelic pages 8-9)

### Genetic risk factors and modifiers

The strongest disease-level risk factor is a pathogenic/likely pathogenic ACTN2 variant plus a compatible phenotype and segregation pattern. Variant interpretation must be conservative: in 2021, ClinVar contained 14 pathogenic/likely pathogenic ACTN2 variants—eight missense, one splice-acceptor, and three nonsense variants—but 390 laboratory-reported VUS; ACTN2 was strongly loss-of-function constrained (**pLI 1.0**). These historical counts are not current and should be refreshed from ClinVar/gnomAD at ingestion. (lindholm2021monoandbiallelic pages 4-6)

Common regulatory variation also modifies heart-failure susceptibility. A large GWAS identified a chromosome-1 regulatory locus interacting with ACTN2; deletion of the enhancer in human embryonic-stem-cell-derived cardiomyocytes reduced ACTN2 expression. The discovery involved 10,976 cases and 437,573 controls, followed by replication in 24,829 cases and 1,614,513 controls; the ACTN2-region Hi-C interaction had **P=0.00002**. This is susceptibility evidence for heart failure, not proof that the common variant causes monogenic DCM1AA. (arvanitis2020genomewideassociationand pages 1-2)

Possible modifiers include other sarcomeric/calcium-handling variants. A 2023 child with a 1q43 deletion affecting **ACTN2, RYR2, and MTR** had severe DCM/LVNC, but the blended deletion prevents attribution to ACTN2 alone. No validated DCM1AA-specific modifier gene, protective allele, founder mutation, or polygenic score is established. (zhou2023impairedcardiomyocytematuration pages 3-7, zhou2023impairedcardiomyocytematuration pages 7-8)

### Environmental and acquired risk factors

No ACTN2-specific exposure interaction has been quantified. By analogy with genetic DCM, pregnancy/peripartum stress, cardiotoxic chemotherapy, heavy alcohol exposure, myocarditis, tachyarrhythmia, hypertension, obesity, and sustained high hemodynamic load may reveal latent disease. These should be recorded as potential **second hits**, not ACTN2-specific causes. Population studies show that expression of DCM-gene variants depends on family history, genomic context, polygenic background, and environment. (shah2022frequencypenetranceand pages 10-12)

### Protective factors

No reproducible genetic protective factor is known. Environmental risk reduction is prudent: avoid cardiotoxins and binge/heavy alcohol, treat hypertension and arrhythmia, maintain vaccination and infection prevention, and use individualized exercise advice. These measures prevent additional myocardial injury but have not been shown to prevent ACTN2 penetrance.

## 3. Phenotypes

ACTN2 disease exhibits marked variable expressivity. Frequencies cannot be estimated reliably because reports comprise a few families and cases.

- **Ventricular dilation and systolic dysfunction:** central DCM phenotype; suggest **HP:0001644 Dilated cardiomyopathy**, **HP:0001722 Decreased cardiac output**, and **HP:0012664 Reduced left ventricular ejection fraction**. In the 2023 deletion case, LV internal diameter in diastole was **48 mm (Z=3.81)** and follow-up LVEF remained **41%**. Severity ranges from subclinical to transplant-level heart failure. (zhou2023impairedcardiomyocytematuration pages 3-7)
- **Heart failure symptoms:** exertional intolerance, dyspnea/tachypnea, fatigue, diaphoresis, poor feeding in children, and edema in advanced disease; suggest **HP:0001635 Congestive heart failure**, **HP:0002094 Dyspnea**, **HP:0002878 Respiratory distress**, and **HP:0003073 Hypohidrosis/diaphoresis only if clinically appropriate**. The p.Gln860Ter patient presented in infancy with tachypnea and reduced EF and progressed to transplantation at 23. (lindholm2021monoandbiallelic pages 3-4)
- **Arrhythmias and conduction/repolarization abnormalities:** atrial fibrillation, nonsustained or sustained ventricular tachyarrhythmia, T-wave inversion, conduction delay, syncope, and sudden death. Suggested HPO: **HP:0005110 Atrial fibrillation**, **HP:0004756 Ventricular tachycardia**, **HP:0001279 Syncope**, **HP:0001645 Sudden cardiac death**, and **HP:0011714 Abnormality of cardiac conduction**. In one deletion family, the proband had exertional syncope at 16; relatives had atrial arrhythmia, ventricular tachyarrhythmia, conduction delay, and two early sudden deaths. (lindholm2021monoandbiallelic pages 3-4)
- **LV noncompaction/hypertrabeculation:** suggested **HP:0030682 Left ventricular noncompaction**. This occurred in the dominant deletion family and in the 2023 multigene deletion case. (zhou2023impairedcardiomyocytematuration pages 3-7, lindholm2021monoandbiallelic pages 3-4)
- **Restrictive physiology and biatrial enlargement:** especially with biallelic p.Gln860Ter; suggest **HP:0001723 Restrictive cardiomyopathy**, **HP:0005114 Atrial enlargement**, and **HP:0001639 Abnormality of the pericardium only when present**. The reported patient developed severe biatrial enlargement, moderate biventricular dysfunction, diastolic dysfunction, equalized filling pressures, atrial fibrillation, and severe fibrosis. (lindholm2021monoandbiallelic pages 9-11, lindholm2021monoandbiallelic pages 3-4)
- **Myocardial fibrosis/hypertrophy:** biopsy or CMR phenotype; suggest **HP:0030858 Myocardial fibrosis** and **HP:0001639 Hypertrophic cardiomyopathy** only when the actual phenotype is hypertrophic. Explanted p.Gln860Ter myocardium had severe interstitial fibrosis. (lindholm2021monoandbiallelic pages 3-4)
- **Skeletal-muscle phenotype:** ACTN2 is expressed in skeletal muscle and dominant ACTN2 myopathy has been reported, but skeletal weakness is not established as a defining DCM1AA phenotype. Record separately when present.

Quality-of-life burden follows heart-failure severity: reduced exercise capacity, school/work limitations, recurrent monitoring and hospitalization, anxiety regarding sudden death, device shocks, and transplant burden. No ACTN2-specific EQ-5D, SF-36, or PROMIS study was found.

## 4. Genetic and molecular information

### Gene and protein

**ACTN2** encodes the 894-amino-acid α-actinin-2 homodimer. Each monomer contains an N-terminal actin-binding domain with **CH1/CH2 calponin-homology domains**, four spectrin-like repeats forming the rod/dimer interface, and a C-terminal calmodulin-like region with EF hands that participates in titin and partner interactions. The protein cross-links antiparallel actin filaments, anchors titin, organizes Z-disc architecture, regulates ion-channel complexes, and participates in mechanosensitive transcription. (lindholm2021monoandbiallelic pages 1-3, broadwaystringer2023insightsintothe pages 1-2)

Suggested annotations include **GO:0055003 cardiac myofibril assembly**, **GO:0030239 myofibril assembly**, **GO:0007015 actin filament organization**, **GO:0030049 muscle filament sliding**, **GO:0006936 muscle contraction**, **GO:0007512 adult heart development**, **GO:0005925 focal adhesion**, and cellular components **GO:0030018 Z disc**, **GO:0030017 sarcomere**, and **GO:0015629 actin cytoskeleton**.

### Illustrative variants

- **p.Gln860Ter (Q860X):** homozygous, absent from gnomAD in the report; C-terminal truncation causing infantile-onset progressive RCM/heart failure and transplant at 23. Protein persisted at near-normal abundance but lost selected interactions. (lindholm2021monoandbiallelic pages 8-9, lindholm2021monoandbiallelic pages 3-4)
- **NC_000001.10:g.236898807_236903093del**, deleting exons 8–10 with a 41-bp intronic insertion: heterozygous in-frame alteration producing a 771-aa protein versus 894 aa; segregated with arrhythmia, LVNC, and early heart-failure manifestations in seven family members. Truncated transcript represented about **20–30%** of full-length transcript in patient cells. (lindholm2021monoandbiallelic pages 3-4, lindholm2021monoandbiallelic pages 4-6)
- **p.Lys? / original 2003 DCM variant:** the retrieved evidence confirms an ACTN2 missense DCM report (PMID 14567970), but exact HGVS should be taken from the primary record before database entry.
- **p.Leu320Arg:** reported in a Chinese family with DCM and ventricular tachycardia. (micolonghi2024unveilingthespectrum pages 29-30)
- **p.Gly111Val, p.Ala119Thr, p.Met228Thr, p.Thr247Met:** primarily HCM-associated actin-binding-domain variants; useful for mechanism and phenotypic spectrum but should not automatically be annotated as DCM1AA variants. (broadwaystringer2023insightsintothe pages 1-2, broadwaystringer2023insightsintothe pages 2-4)
- **Large 1q43 deletion:** chr1:236,686,454–237,833,988 (hg38), affecting ACTN2, RYR2, and MTR; germline heterozygous CNV with DCM/LVNC. Its pathogenic contribution is multigenic. (zhou2023impairedcardiomyocytematuration pages 3-7)

All documented disease variants are germline. No somatic ACTN2 mechanism is established. Population frequencies must be variant-specific and taken from current gnomAD; absence or rarity alone is insufficient for ACMG/AMP pathogenicity. Segregation, phenotype specificity, functional evidence, predicted molecular consequence, and gene-level disease validity are required. CMA/WGS is important for exon-level or multigene deletions that sequencing-only panels may miss.

### Epigenetic and chromosomal findings

No reproducible DCM1AA-specific DNA-methylation or histone signature is established. A cardiomyocyte-specific enhancer regulating ACTN2 is supported by chromatin conformation, developmental activation, and genome editing, providing a regulatory-genomic—not classical epigenetic-disease—mechanism. (arvanitis2020genomewideassociationand pages 1-2)

## 5. Environmental information

ACTN2-related disease is not infectious, toxic, or zoonotic. Viral myocarditis and toxins are differential or superimposed injuries rather than primary causes. No pathogen, pollutant, radiation exposure, occupational agent, smoking pattern, diet, or alcohol threshold has been demonstrated specifically to cause DCM1AA. Clinically, avoid excessive alcohol, cocaine/amphetamines, anabolic agents, and unnecessary cardiotoxic drugs; manage metabolic and vascular risk factors. Exercise prescriptions should be individualized because arrhythmia and sudden death occur in some ACTN2 families, but evidence is insufficient to impose an ACTN2-specific universal exercise ban.

## 6. Mechanism and pathophysiology

### Causal chain

**Upstream:** pathogenic ACTN2 variant or regulatory loss → altered α-actinin-2 folding, stability, abundance, domain architecture, or partner binding.

**Intermediate:** abnormal actin/titin cross-linking and Z-disc assembly → sarcomeric disarray and defective force transmission; altered interaction with ion-channel and sarcolemmal proteins; impaired calcium handling; abnormal mechanosensitive transcription and cardiomyocyte maturation; mitochondrial energetic stress and proteostasis activation.

**Downstream:** reduced contractile velocity and compensatory hypertrophy → chamber dilation or restrictive remodeling, fibrosis, systolic/diastolic dysfunction, conduction abnormalities and arrhythmia → heart failure, sudden death, mechanical support, or transplantation. (lindholm2021monoandbiallelic pages 1-3, lindholm2021monoandbiallelic pages 8-9, lindholm2021monoandbiallelic pages 4-6, lindholm2021monoandbiallelic pages 3-4)

### Variant-dependent mechanisms

In heterozygous exon 8–10 indel cells, the truncated protein entered sarcomeres and distorted Z-disc ultrastructure—a dominant-negative mechanism. Patient hiPSC cardiomyocytes were hypertrophic, structurally disarrayed, had impaired contractility and abnormal calcium signaling. (lindholm2021monoandbiallelic pages 1-3)

In homozygous p.Gln860Ter cells, loss of the C-terminal region disrupted interactions with **ACTN1** and **GJA1/connexin-43**, potentially linking the variant to relaxation and electrical phenotypes. CRISPR introduction of the truncation into control cells reproduced the direction of contractile abnormalities, although the contractile-velocity result was borderline (**P=0.058**), an important limitation. (lindholm2021monoandbiallelic pages 8-9, lindholm2021monoandbiallelic pages 4-6)

RNA sequencing of p.Gln860Ter myocardium showed extracellular-matrix remodeling, collagen biosynthesis, and mRNA-splicing enrichment; COL1A1, COL1A2, COL4A1, fibronectin, TGF-β, NPPA and NPPB were elevated. Patient hiPSC cardiomyocytes had marked **MYL2** induction (log fold change 5.23 for Q860X and 4.90 for deletion cells) and enrichment of respiratory electron transport and gluconeogenesis, indicating metabolic remodeling. (lindholm2021monoandbiallelic pages 3-4, lindholm2021monoandbiallelic pages 4-6)

The 2023 Actn2 p.Met228Thr mouse study found a destabilized mutant protein, increased ubiquitin–proteasome activity, sarcomeric quantitative abnormalities, mitochondrial dysfunction and cell-cycle defects. Its abstract states: “**This missense variant in alpha-actinin renders the protein less stable**.” These data support proteostasis and bioenergetic mechanisms, but the model represents an HCM-associated allele and should not be assumed to reproduce DCM1AA. (broadwaystringer2023insightsintothe pages 1-2)

### Cells, anatomy, and ontology

Primary cell: **cardiac muscle cell/cardiomyocyte — CL:0000746**. Secondary cells implicated by fibrosis and remodeling include cardiac fibroblasts; direct ACTN2 pathology in fibroblasts is not established. Primary tissue is ventricular myocardium, particularly left ventricle; both ventricles and atria may become involved secondarily. Suggested anatomy: **UBERON:0000948 heart**, **UBERON:0002084 heart left ventricle**, **UBERON:0002080 heart right ventricle**, and myocardium/ventricular myocardium terms where supported. Disease is bilateral/nonlateralized at organ level; “left” reflects the dominant phenotype, not body lateralization.

Relevant processes include sarcomere organization, actin binding, calcium-ion homeostasis, mitochondrial ATP generation, ubiquitin-dependent proteolysis, cell-cycle regulation, hypertrophic signaling, extracellular-matrix organization, and fibrosis. No ACTN2-specific single-cell or spatial-transcriptomic atlas was found.

## 7. Anatomical structures affected

The **heart** is primary, particularly ventricular myocardium and cardiomyocyte Z-discs. Left-ventricular dilation, hypertrabeculation/noncompaction and systolic dysfunction predominate in DCM presentations. Right-ventricular dysfunction, biatrial enlargement, conduction tissue dysfunction and diffuse interstitial fibrosis can develop in severe disease. Secondary structures affected by heart failure include lungs (pulmonary congestion), liver and kidneys (venous congestion/hypoperfusion), and skeletal muscle through deconditioning; these are complications, not primary ACTN2 lesions.

Subcellular compartments include the Z-disc, sarcomere, actin thin filaments, titin-anchoring complex, sarcolemma/gap junction neighborhood, mitochondria, and ubiquitin–proteasome system. (lindholm2021monoandbiallelic pages 1-3, lindholm2021monoandbiallelic pages 8-9, broadwaystringer2023insightsintothe pages 1-2)

## 8. Temporal development

Onset ranges from infancy to adulthood and may be insidious or arrhythmia-first. The homozygous p.Gln860Ter patient presented in infancy, developed progressive heart failure and atrial fibrillation in her twenties, and underwent transplantation at 23. The dominant-deletion proband presented at 16 with exertional syncope; relatives showed variable arrhythmic, LVNC, and heart-failure phenotypes. (lindholm2021monoandbiallelic pages 3-4)

A practical course model is:

1. **Genotype-positive/phenotype-negative:** no imaging or electrical abnormality.
2. **Early electrical or structural expression:** T-wave changes, conduction delay, atrial/ventricular ectopy, mild dilation, noncompaction, or reduced strain.
3. **Overt cardiomyopathy:** dilation and reduced EF, or restrictive/noncompaction phenotype.
4. **Advanced disease:** recurrent arrhythmia, fibrosis, decompensated HF, device therapy, VAD, or transplantation.

The course is chronic and variably progressive. Reverse remodeling may occur with contemporary therapy in DCM generally, but ACTN2-specific remission rates are unavailable. Critical opportunities are presymptomatic family identification and initiation of therapy at the first evidence of dysfunction or arrhythmia.

## 9. Inheritance and population

### Inheritance

Most reported ACTN2 cardiomyopathy is **autosomal dominant**, with variable expressivity and likely age-dependent, incomplete penetrance. Biallelic truncating variants can cause **autosomal-recessive** severe disease. Germline mosaicism is biologically possible but not documented as a characteristic. No genetic anticipation, sex-linked transmission, mitochondrial inheritance, established founder effect, or consanguinity-specific burden was identified. (lindholm2021monoandbiallelic pages 1-3, lindholm2021monoandbiallelic pages 8-9, broadwaystringer2023insightsintothe pages 2-4)

### Epidemiology

No credible ACTN2/DCM1AA-specific prevalence, incidence, carrier frequency, sex ratio, geographic distribution, or ethnic enrichment is available. General DCM prevalence is estimated near **1:250**, with UK Biobank CMR suggesting **1:220** among more than 39,000 participants; these figures must not be assigned to DCM1AA. Definitive DCM genes collectively explain up to about **40%** of cases, while ACTN2 represents a rare minor-gene cause. (newman2024dilatedcardiomyopathya pages 1-2)

General-population penetrance studies likewise are not ACTN2-specific. In 18,665 UK Biobank participants, 7.8% carried at least one “putative pathogenic” variant under a broad 44-gene strategy, but combined penetrance remained ≤30%; broad filtering likely included variants that would not meet modern clinical pathogenicity standards. Another study found pathogenic/likely pathogenic DCM variants in approximately **1:251**, with phenotype penetrance only **1.2–3.1%** in the population setting. These observations reinforce the need for variant-level interpretation, family history, and serial phenotyping. (shah2022frequencypenetranceand pages 10-12)

## 10. Diagnostics

### Clinical evaluation

Diagnosis requires demonstration of a compatible cardiac phenotype and exclusion of more common causes. Recommended assessment includes:

- Three-generation pedigree, sudden-death history and extracardiac myopathy review.
- Physical examination, ECG, ambulatory rhythm monitoring and exercise testing where appropriate.
- Echocardiography for chamber dimensions, EF, diastolic function and trabeculation.
- Cardiac MRI for volumes, function, noncompaction morphology, edema and fibrosis/LGE.
- BNP/NT-proBNP and high-sensitivity troponin; CBC, electrolytes, renal/liver/thyroid indices, iron studies and CK according to presentation.
- Coronary evaluation when ischemia is plausible; viral/immune testing only when clinically indicated.
- Endomyocardial biopsy for selected rapidly progressive, inflammatory, infiltrative or unexplained presentations—not routine confirmation of ACTN2 disease.

### Genetic testing

Use a **clinically curated cardiomyopathy panel** including ACTN2 and established DCM genes, with copy-number analysis. WES/WGS is appropriate when the panel is negative, disease is early/severe, or blended/syndromic disease is suspected. WGS offers improved noncoding and structural-variant detection. RNA sequencing can clarify splice effects but remains adjunctive. CMA is useful for large deletions such as the 1q43 ACTN2–RYR2 deletion; karyotype/FISH are not routine unless a chromosomal rearrangement is suspected. Mitochondrial DNA or repeat-expansion testing is phenotype-directed, not standard for isolated ACTN2 disease. (zhou2023impairedcardiomyocytematuration pages 3-7, lindholm2021monoandbiallelic pages 3-4)

A VUS must not establish diagnosis or direct predictive testing. Confirm pathogenic/likely pathogenic variants by an orthogonal method where required, test segregation, and periodically reanalyze. Once a causal familial variant is established, offer targeted cascade testing with genetic counseling.

### Screening

First-degree relatives should receive ECG and cardiac imaging, with periodic reassessment guided by age, genotype, family onset and symptoms. Genotype-positive relatives require longitudinal surveillance even when initially normal. Newborn population screening is not established. Prenatal diagnosis and preimplantation genetic testing are possible when a familial pathogenic variant and inheritance model are known.

### Differential diagnosis

Exclude ischemic, hypertensive, valvular, congenital, tachycardia-induced, alcohol/toxin/chemotherapy-related, peripartum, inflammatory/myocarditic, endocrine/metabolic, infiltrative and neuromuscular cardiomyopathy. Genetically, distinguish TTN-, LMNA-, FLNC-, DSP-, RBM20-, BAG3-, PLN-, DES-, SCN5A-, sarcoglycan-, dystrophin- and mitochondrial disease. HCM, RCM, LVNC and arrhythmogenic cardiomyopathy are not merely differentials: they may be alternate ACTN2 phenotypes.

## 11. Outcome and prognosis

ACTN2-specific survival curves do not exist. Documented outcomes range from asymptomatic carriers to sudden death and transplantation. The homozygous p.Gln860Ter case demonstrates severe progression and transplant at 23, while a dominant deletion family included two early sudden deaths. The 2023 multigene-deletion child remained dilated with LVEF 41% and was referred for transplantation. (zhou2023impairedcardiomyocytematuration pages 3-7, lindholm2021monoandbiallelic pages 3-4)

For broader nonischemic DCM, a 2024 meta-analysis of **103 studies and 29,687 patients** found that CMR LGE predicted all-cause mortality (**HR 1.81**), cardiovascular mortality (**HR 2.43**), arrhythmic events (**HR 2.69**) and HF events (**HR 1.98**). Each 1% increase in LGE extent was associated with HRs of 1.07, 1.15, 1.07 and 1.06, respectively. LVEF was not significantly associated with mortality or arrhythmic outcomes in that analysis. These are general NIDCM prognostic data, not ACTN2-specific estimates. (eichhorn2024riskstratificationin pages 1-2)

Adverse prognostic factors likely include earlier onset, biallelic or severe truncating variants, progressive EF decline, ventricular arrhythmia, syncope, fibrosis/LGE, biventricular dysfunction, elevated natriuretic peptides, recurrent hospitalization and failure to reverse-remodel. No validated ACTN2-specific prognostic biomarker exists.

## 12. Treatment

### Current standard care

There is **no approved ACTN2-directed therapy**. Treat the expressed phenotype according to heart-failure and arrhythmia guidelines.

For HFrEF, foundational therapy comprises:

1. ARNI—or ACE inhibitor/ARB if ARNI unsuitable.
2. Evidence-based β-blocker.
3. Mineralocorticoid-receptor antagonist.
4. SGLT2 inhibitor.

Add loop diuretics for congestion; consider ivabradine, hydralazine/isosorbide dinitrate, vericiguat, digoxin, iron replacement and anticoagulation according to standard indications. Continue therapy after EF improvement because genetic substrate persists. Relevant NCIT intervention concepts include angiotensin-receptor/neprilysin inhibitor therapy, beta-blocker therapy, mineralocorticoid-receptor antagonist therapy, SGLT2-inhibitor therapy, diuretic therapy and anticoagulation therapy.

Arrhythmia management includes ambulatory surveillance, β-blockade, antiarrhythmic drugs or catheter ablation when indicated. ICD decisions should integrate EF, symptoms, fibrosis, syncope, ventricular arrhythmia and family history; there is no validated ACTN2-specific threshold. CRT follows conventional QRS/LBBB and EF criteria. Advanced disease may require LVAD or heart transplantation.

The 2023 child with the ACTN2–RYR2 deletion received creatine phosphate, levocarnitine, digoxin, captopril and metoprolol, but remained severely affected and was referred for transplant; this is a case history, not evidence for genotype-specific efficacy. (zhou2023impairedcardiomyocytematuration pages 3-7)

A p.Thr247Met hiPSC model showed reduced L-type calcium-channel interaction and QT prolongation, with reported benefit from diltiazem in that individual. This is precision-treatment proof of concept for an ACTN2 electrophysiologic/HCM phenotype, not established DCM1AA treatment. (wadmore2021theroleof pages 2-4)

### Experimental therapy and real-world implementation

Searches found no ACTN2-specific gene therapy, RNA therapy, cell therapy or interventional clinical trial. Contemporary trials target other genetic DCM forms, including BAG3 AAV replacement, and cannot be extrapolated directly. ACTN2 replacement/editing faces challenges including cardiac delivery, dominant-negative alleles, isoform dosage, immunity and off-target effects.

Real-world HFrEF implementation remains incomplete: a 2024 retrospective study of 73 hospitalized patients reported that only about one-third left hospital receiving all four recommended drug classes. This was not an ACTN2 cohort but illustrates the implementation gap.

## 13. Prevention

**Primary prevention:** germline occurrence cannot generally be prevented. Genetic counseling can support reproductive planning, including prenatal or preimplantation testing. Avoid additional myocardial insults and control blood pressure, alcohol exposure, obesity, diabetes, sleep apnea and arrhythmia.

**Secondary prevention:** targeted cascade testing plus serial ECG, rhythm monitoring and imaging offer the strongest opportunity to detect presymptomatic disease. Begin standard therapy promptly when ventricular dysfunction emerges. No population newborn or adult ACTN2 screening program is recommended.

**Tertiary prevention:** optimize guideline-directed therapy, vaccination and infection management, monitor renal function/electrolytes, treat congestion and arrhythmia, assess sudden-death risk, and refer early to inherited-cardiomyopathy and advanced-HF centers. There is no disease-specific vaccine or chemoprophylaxis.

## 14. Other species and naturally occurring disease

ACTN2 is evolutionarily conserved across vertebrates. Suggested taxa for comparative annotation include **Homo sapiens (NCBI Taxon 9606)**, **Mus musculus (10090)** and **Danio rerio (7955)**. Ortholog identifiers should be obtained from the current NCBI Gene/Alliance records during database loading.

No well-validated naturally occurring veterinary disorder specifically equivalent to human ACTN2-related DCM was identified. Cardiomyopathy is common in dogs and cats, and feline studies have explored ACTN2 variation, but this does not establish a naturally occurring DCM1AA ortholog or breed-specific VBO entity. There is no transmission or zoonotic potential.

## 15. Model organisms and experimental systems

### Human iPSC cardiomyocytes

Patient-derived hiPSC cardiomyocytes reproduce hypertrophy, sarcomeric disarray, reduced contractile velocity and aberrant calcium signaling. RNA-seq, electron microscopy, immunostaining and interactome mass spectrometry have connected genotype to cellular phenotype. CRISPR introduction of p.Gln860Ter into an isogenic control supported causality. Advantages are human genetic context and suitability for drug screening; limitations include fetal-like maturation, absence of whole-heart loading and incomplete multicellular architecture. (lindholm2021monoandbiallelic pages 4-6, lindholm2021monoandbiallelic pages 1-3)

### Mouse

The 2023 CRISPR knock-in **Actn2 p.Met228Thr** mouse was viable as a heterozygote; only mature males developed molecular cardiomyopathy markers without an overt phenotype. Homozygotes were embryonically lethal and E15.5 hearts showed morphological abnormalities, sarcomeric changes, cell-cycle defects, mitochondrial dysfunction and proteasome activation. It is valuable for developmental/proteostasis mechanisms but models an HCM-associated allele and has limited fidelity to adult human DCM. (broadwaystringer2023insightsintothe pages 1-2, broadwaystringer2023insightsintothe pages 2-4)

### Zebrafish

Morpholino depletion of actn2 impaired lateral Z-disc alignment, reduced cardiac function, cardiomyocyte number and size, end-diastolic dimension and ventricular chamber size. Other reported loss models showed dilated hearts, thickened Z-discs, weakness and immobility; ACTN3 did not rescue the phenotype. Zebrafish are useful for rapid developmental and modifier screens, but morpholino artifacts, cardiac anatomy and dosage differences limit direct clinical translation. (lindholm2021monoandbiallelic pages 8-9, wadmore2021theroleof pages 2-4)

### In vitro structural/biochemical models

Crystal and binding studies of actin-binding-domain variants show reduced thermal stability, altered tertiary structure, weaker actin binding, defective Z-disc incorporation and aggregation. These clarify molecular consequences but cannot establish penetrance or clinical pathogenicity alone. (wadmore2021theroleof pages 2-4)

## Recent developments, expert interpretation, and evidence gaps

Important 2023–2024 developments include the 2023 Actn2 knock-in mouse/proteomics study, a 2023 human ACTN2–RYR2 deletion case linking cardiomyocyte maturation to severe pediatric DCM/LVNC, 2024 reviews emphasizing cautious interpretation of minor cardiomyopathy genes, and a 2024 CMR meta-analysis strengthening fibrosis-based risk assessment. (zhou2023impairedcardiomyocytematuration pages 3-7, broadwaystringer2023insightsintothe pages 1-2, eichhorn2024riskstratificationin pages 1-2)

The most defensible expert interpretation is that ACTN2 is a biologically compelling but **rare and phenotypically pleiotropic** cardiomyopathy gene. A clinical diagnosis should not be based on the “DCM1AA” label or an ACTN2 VUS alone. Strong evidence requires a compatible phenotype, a very rare variant with an appropriate molecular consequence, segregation or de novo evidence, and preferably functional support. Current major gaps are subtype-specific epidemiology, penetrance by variant class, prospective natural history, standardized sudden-death prediction, single-cell/spatial profiling, and ACTN2-directed therapy.

### Selected primary-source quotations

- Lindholm et al. 2021: “**Patient-derived iPSC-cardiomyocytes were hypertrophic, displayed sarcomeric structural disarray, impaired contractility, and aberrant Ca2+-signaling.**” DOI: https://doi.org/10.1161/CIRCGEN.121.003419; published December 2021. (lindholm2021monoandbiallelic pages 1-3)
- Broadway-Stringer et al. 2023: “**Heterozygous Actn2 p.Met228Thr mice have no overt phenotype. Only mature males show molecular parameters indicative of cardiomyopathy.**” DOI: https://doi.org/10.3390/cells12050721; published 24 February 2023. (broadwaystringer2023insightsintothe pages 1-2)
- Arvanitis et al. 2020: “**Genome-editing in human embryonic stem cell-derived cardiomyocytes confirms the influence of the identified regulatory region in the expression of ACTN2.**” DOI: https://doi.org/10.1038/s41467-020-14843-7; published February 2020. (arvanitis2020genomewideassociationand pages 1-2)

**Overall evidence grade:** moderate for ACTN2 as a cause of an intrinsic cardiomyopathy spectrum; lower for DCM1AA as a sharply bounded disease entity; high for the general DCM diagnostic and heart-failure treatment framework; insufficient for ACTN2-specific prevalence, penetrance, prognosis, prevention, or targeted therapy.

References

1. (OpenTargets Search: dilated cardiomyopathy-ACTN2): Open Targets Query (dilated cardiomyopathy-ACTN2, 7 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (lindholm2021monoandbiallelic pages 1-3): Malene E. Lindholm, David Jimenez-Morales, Han Zhu, Kinya Seo, David Amar, Chunli Zhao, Archana Raja, Roshni Madhvani, Sarah Abramowitz, Cedric Espenel, Shirley Sutton, Colleen Caleshu, Gerald J. Berry, Kara S. Motonaga, Kyla Dunn, Julia Platt, Euan A. Ashley, and Matthew T. Wheeler. Mono- and biallelic protein-truncating variants in alpha-actinin 2 cause cardiomyopathy through distinct mechanisms. Circulation: Genomic and Precision Medicine, Dec 2021. URL: https://doi.org/10.1161/circgen.121.003419, doi:10.1161/circgen.121.003419. This article has 31 citations.

3. (lindholm2021monoandbiallelic pages 3-4): Malene E. Lindholm, David Jimenez-Morales, Han Zhu, Kinya Seo, David Amar, Chunli Zhao, Archana Raja, Roshni Madhvani, Sarah Abramowitz, Cedric Espenel, Shirley Sutton, Colleen Caleshu, Gerald J. Berry, Kara S. Motonaga, Kyla Dunn, Julia Platt, Euan A. Ashley, and Matthew T. Wheeler. Mono- and biallelic protein-truncating variants in alpha-actinin 2 cause cardiomyopathy through distinct mechanisms. Circulation: Genomic and Precision Medicine, Dec 2021. URL: https://doi.org/10.1161/circgen.121.003419, doi:10.1161/circgen.121.003419. This article has 31 citations.

4. (lindholm2021monoandbiallelic pages 4-6): Malene E. Lindholm, David Jimenez-Morales, Han Zhu, Kinya Seo, David Amar, Chunli Zhao, Archana Raja, Roshni Madhvani, Sarah Abramowitz, Cedric Espenel, Shirley Sutton, Colleen Caleshu, Gerald J. Berry, Kara S. Motonaga, Kyla Dunn, Julia Platt, Euan A. Ashley, and Matthew T. Wheeler. Mono- and biallelic protein-truncating variants in alpha-actinin 2 cause cardiomyopathy through distinct mechanisms. Circulation: Genomic and Precision Medicine, Dec 2021. URL: https://doi.org/10.1161/circgen.121.003419, doi:10.1161/circgen.121.003419. This article has 31 citations.

5. (micolonghi2024unveilingthespectrum pages 29-30): Caterina Micolonghi, Federica Perrone, Marco Fabiani, Silvia Caroselli, Camilla Savio, Antonio Pizzuti, Aldo Germani, Vincenzo Visco, Simona Petrucci, Speranza Rubattu, and Maria Piane. Unveiling the spectrum of minor genes in cardiomyopathies: a narrative review. International Journal of Molecular Sciences, 25:9787, Sep 2024. URL: https://doi.org/10.3390/ijms25189787, doi:10.3390/ijms25189787. This article has 10 citations.

6. (lindholm2021monoandbiallelic pages 8-9): Malene E. Lindholm, David Jimenez-Morales, Han Zhu, Kinya Seo, David Amar, Chunli Zhao, Archana Raja, Roshni Madhvani, Sarah Abramowitz, Cedric Espenel, Shirley Sutton, Colleen Caleshu, Gerald J. Berry, Kara S. Motonaga, Kyla Dunn, Julia Platt, Euan A. Ashley, and Matthew T. Wheeler. Mono- and biallelic protein-truncating variants in alpha-actinin 2 cause cardiomyopathy through distinct mechanisms. Circulation: Genomic and Precision Medicine, Dec 2021. URL: https://doi.org/10.1161/circgen.121.003419, doi:10.1161/circgen.121.003419. This article has 31 citations.

7. (broadwaystringer2023insightsintothe pages 1-2): Sophie Broadway-Stringer, He Jiang, Kirsty Wadmore, Charlotte Hooper, Gillian Douglas, Violetta Steeples, Amar J. Azad, Evie Singer, Jasmeet S. Reyat, Frantisek Galatik, Elisabeth Ehler, Pauline Bennett, Jacinta I. Kalisch-Smith, Duncan B. Sparrow, Benjamin Davies, Kristina Djinovic-Carugo, Mathias Gautel, Hugh Watkins, and Katja Gehmlich. Insights into the role of a cardiomyopathy-causing genetic variant in actn2. Cells, 12:721, Feb 2023. URL: https://doi.org/10.3390/cells12050721, doi:10.3390/cells12050721. This article has 21 citations.

8. (broadwaystringer2023insightsintothe pages 2-4): Sophie Broadway-Stringer, He Jiang, Kirsty Wadmore, Charlotte Hooper, Gillian Douglas, Violetta Steeples, Amar J. Azad, Evie Singer, Jasmeet S. Reyat, Frantisek Galatik, Elisabeth Ehler, Pauline Bennett, Jacinta I. Kalisch-Smith, Duncan B. Sparrow, Benjamin Davies, Kristina Djinovic-Carugo, Mathias Gautel, Hugh Watkins, and Katja Gehmlich. Insights into the role of a cardiomyopathy-causing genetic variant in actn2. Cells, 12:721, Feb 2023. URL: https://doi.org/10.3390/cells12050721, doi:10.3390/cells12050721. This article has 21 citations.

9. (zhou2023impairedcardiomyocytematuration pages 3-7): Letao Zhou, Jinglan Huang, Hong Li, Hongyu Duan, Yimin Hua, Yuxuan Guo, Kaiyu Zhou, and Yifei Li. Impaired cardiomyocyte maturation leading to dcm: a case report and literature review. Medicina, 59:1158, Jun 2023. URL: https://doi.org/10.3390/medicina59061158, doi:10.3390/medicina59061158. This article has 2 citations.

10. (zhou2023impairedcardiomyocytematuration pages 7-8): Letao Zhou, Jinglan Huang, Hong Li, Hongyu Duan, Yimin Hua, Yuxuan Guo, Kaiyu Zhou, and Yifei Li. Impaired cardiomyocyte maturation leading to dcm: a case report and literature review. Medicina, 59:1158, Jun 2023. URL: https://doi.org/10.3390/medicina59061158, doi:10.3390/medicina59061158. This article has 2 citations.

11. (wadmore2021theroleof pages 2-4): Kirsty Wadmore, Amar J. Azad, and Katja Gehmlich. The role of z-disc proteins in myopathy and cardiomyopathy. International Journal of Molecular Sciences, 22:3058, Mar 2021. URL: https://doi.org/10.3390/ijms22063058, doi:10.3390/ijms22063058. This article has 75 citations.

12. (newman2024dilatedcardiomyopathya pages 1-2): Noah A. Newman and Michael A. Burke. Dilated cardiomyopathy: a genetic journey from past to future. International Journal of Molecular Sciences, 25:11460, Oct 2024. URL: https://doi.org/10.3390/ijms252111460, doi:10.3390/ijms252111460. This article has 26 citations.

13. (eichhorn2024riskstratificationin pages 1-2): Christian Eichhorn, David Koeckerling, Rohin K Reddy, Maddalena Ardissino, Marek Rogowski, Bernadette Coles, Lukas Hunziker, Simon Greulich, Isaac Shiri, Norbert Frey, Jens Eckstein, Stephan Windecker, Raymond Y Kwong, George C M Siontis, and Christoph Gräni. Risk stratification in nonischemic dilated cardiomyopathy using cmr imaging: a systematic review and meta-analysis. JAMA, Sep 2024. URL: https://doi.org/10.1001/jama.2024.13946, doi:10.1001/jama.2024.13946. This article has 43 citations.

14. (shah2022frequencypenetranceand pages 10-12): Ravi A. Shah, Babken Asatryan, Ghaith Sharaf Dabbagh, Nay Aung, Mohammed Y. Khanji, Luis R. Lopes, Stefan van Duijvenboden, Anthony Holmes, Daniele Muser, Andrew P. Landstrom, Aaron Mark Lee, Pankaj Arora, Christopher Semsarian, Virend K. Somers, Anjali T. Owens, Patricia B. Munroe, Steffen E. Petersen, and C. Anwar A. Chahal. Frequency, penetrance, and variable expressivity of dilated cardiomyopathy–associated putative pathogenic gene variants in uk biobank participants. Circulation, 146:110-124, Jul 2022. URL: https://doi.org/10.1161/circulationaha.121.058143, doi:10.1161/circulationaha.121.058143. This article has 104 citations and is from a highest quality peer-reviewed journal.

15. (arvanitis2020genomewideassociationand pages 1-2): Marios Arvanitis, Emmanouil Tampakakis, Yanxiao Zhang, Wei Wang, Adam Auton, Michelle Agee, Stella Aslibekyan, Robert K. Bell, Katarzyna Bryc, Sarah K. Clark, Sarah L. Elson, Kipper Fletez-Brant, Pierre Fontanillas, Nicholas A. Furlotte, Pooja M. Gandhi, Karl Heilbron, Barry Hicks, David A. Hinds, Karen E. Huber, Ethan M. Jewett, Yunxuan Jiang, Aaron Kleinman, Keng-Han Lin, Nadia K. Litterman, Jennifer C. McCreight, Matthew H. McIntyre, Kimberly F. McManus, Joanna L. Mountain, Sahar V. Mozaffari, Priyanka Nandakumar, Elizabeth S. Noblin, Carrie A. M. Northover, Jared O’Connell, Steven J. Pitts, G. David Poznik, J. Fah Sathirapongsasuti, Anjali J. Shastri, Janie F. Shelton, Suyash Shringarpure, Chao Tian, Joyce Y. Tung, Robert J. Tunney, Vladimir Vacic, Xin Wang, Amir S. Zare, Diptavo Dutta, Stephanie Glavaris, Ali Keramati, Nilanjan Chatterjee, Neil C. Chi, Bing Ren, Wendy S. Post, and Alexis Battle. Genome-wide association and multi-omic analyses reveal actn2 as a gene linked to heart failure. Nature Communications, Feb 2020. URL: https://doi.org/10.1038/s41467-020-14843-7, doi:10.1038/s41467-020-14843-7. This article has 92 citations and is from a highest quality peer-reviewed journal.

16. (lindholm2021monoandbiallelic pages 9-11): Malene E. Lindholm, David Jimenez-Morales, Han Zhu, Kinya Seo, David Amar, Chunli Zhao, Archana Raja, Roshni Madhvani, Sarah Abramowitz, Cedric Espenel, Shirley Sutton, Colleen Caleshu, Gerald J. Berry, Kara S. Motonaga, Kyla Dunn, Julia Platt, Euan A. Ashley, and Matthew T. Wheeler. Mono- and biallelic protein-truncating variants in alpha-actinin 2 cause cardiomyopathy through distinct mechanisms. Circulation: Genomic and Precision Medicine, Dec 2021. URL: https://doi.org/10.1161/circgen.121.003419, doi:10.1161/circgen.121.003419. This article has 31 citations.

## Artifacts

- [Edison artifact artifact-00](Dilated_Cardiomyopathy_1AA-deep-research-falcon_artifacts/artifact-00.md)