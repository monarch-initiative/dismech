---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T17:53:05.777471'
end_time: '2026-08-01T17:59:30.107734'
duration_seconds: 384.33
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: PRR12-Related Neuroocular Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 3
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PRR12-Related_Neuroocular_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PRR12-Related Neuroocular Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PRR12-Related Neuroocular Syndrome** covering all of the
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
- **Disease Name:** PRR12-Related Neuroocular Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PRR12-Related Neuroocular Syndrome** covering all of the
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


# PRR12-Related Neuroocular Syndrome: Disease Characteristics Report

## Executive summary and evidence scope

PRR12-related neuroocular syndrome is an ultra-rare, autosomal-dominant developmental disorder caused primarily by heterozygous loss of PRR12 function. Its defining combination is developmental impairment—often intellectual disability—with highly variable congenital ocular abnormalities and frequent cardiac, renal, growth, and hypotonia phenotypes. The principal disease-defining study remains Chowdhury *et al.*, published in *Genetics in Medicine* in July 2021 (accepted 11 February 2021; DOI: [10.1038/s41436-021-01129-6](https://doi.org/10.1038/s41436-021-01129-6)). It assembled 24 individuals, aged 5 months–36 years, including 11 females and 13 males. Focused searches did not identify a disease-specific 2023–2024 cohort, natural-history study, clinical guideline, or therapeutic trial; therefore, “current understanding” still rests predominantly on this 2021 cohort and earlier ocular case reports. A PMID was not recoverable from the retrieved material, so the DOI is supplied rather than an uncertain PMID. (chowdhury2021haploinsufficiencyofprr12 pages 2-2, chowdhury2021haploinsufficiencyofprr12 pages 1-2)

The authors’ abstract-level conclusion is directly applicable: **“These findings support PRR12 haploinsufficiency as a cause for a novel disorder with a wide clinical spectrum marked chiefly by neurodevelopmental and eye abnormalities.”** (chowdhury2021haploinsufficiencyofprr12 pages 1-2)

| Domain | Summary | Evidence type | Key citations |
|---|---|---|---|
| Definition | PRR12-related neuroocular syndrome is a newly delineated Mendelian developmental disorder caused by PRR12 haploinsufficiency, characterized chiefly by developmental impairment/intellectual disability with variable structural and functional eye abnormalities plus multisystem involvement. | Observed human cohort evidence | (chowdhury2021haploinsufficiencyofprr12 pages 1-2, chowdhury2021haploinsufficiencyofprr12 pages 2-2) |
| Evidence cohort | Disease-defining cohort: 24 individuals total, including 3 previously reported and 21 newly added; sex distribution 11 female/13 male; age range 5 months-36 years. Four additional DECIPHER individuals with de novo PRR12 variants and one additional DECIPHER microdeletion involving PRR12 were noted as supportive evidence. | Observed human cohort evidence | (chowdhury2021haploinsufficiencyofprr12 pages 1-2, chowdhury2021haploinsufficiencyofprr12 pages 2-2, chowdhury2021haploinsufficiencyofprr12 pages 2-3) |
| Inheritance | Variants were de novo when parental testing/sequencing was possible; pattern is consistent with autosomal dominant disease due to haploinsufficiency. No established evidence for recessive inheritance, anticipation, or founder effect. | Observed human cohort evidence with interpretation | (chowdhury2021haploinsufficiencyofprr12 pages 2-2) |
| Gene / variant mechanism | PRR12 encodes a 211-kDa nuclear protein with suspected DNA-binding activity. In the 24-patient cohort: 12 frameshift, 6 nonsense, 1 splice-site, 2 missense variants, and 1 gross deletion involving PRR12. Truncating/splice variants are predicted loss-of-function via nonsense-mediated decay; the overall disease mechanism is haploinsufficiency. Two de novo missense variants were predicted damaging in silico: c.3505C>T (p.Arg1169Trp) and c.5909T>C (p.Leu1970Pro). PRR12 is highly constrained for loss-of-function variation (pLI 1.00; o/e 0.0, 90% CI 0-0.05; LOEUF 0.051). | Observed human genetic evidence; some mechanistic prediction | (chowdhury2021haploinsufficiencyofprr12 pages 1-2, chowdhury2021haploinsufficiencyofprr12 pages 2-3, chowdhury2021haploinsufficiencyofprr12 pages 2-2) |
| Core phenotype frequencies | Developmental impairment: all sequence-variant cases described; among 23 with sequence variants, 17 global developmental delay, 3 isolated motor delay, 4 isolated speech-language delay. Intellectual disability documented in all 11/11 individuals older than 7 years with available data. Structural eye defects in 12/24 (50%). Globe defects/anophthalmia or microphthalmia in 4/24 (16.7%), observed only in females in this cohort. Coloboma in 7/24 (29%). Visual impairment in 17/22 (77%). Strabismus in 8/22 (36%). | Observed human cohort evidence | (chowdhury2021haploinsufficiencyofprr12 pages 2-2, chowdhury2021haploinsufficiencyofprr12 pages 6-8) |
| Other systemic frequencies | Hypotonia 14/23 (61%). Congenital heart defects 12/23 (52%) including atrial septal defects (6), ventricular septal defects (2), pulmonary stenosis (3), with one patient having two defects. Kidney anomalies 8/23 (35%), including hydronephrosis, duplicated ureters, and vesicoureteral reflux. Failure to thrive 13/24 (54%). Microcephaly 7/24 (29%). Cleft palate 4/24 (17%). Intestinal malrotation 2/24 (8%). Meckel diverticulum 1/24 (4%). Cryptorchidism 5/13 males (38%). | Observed human cohort evidence | (chowdhury2021haploinsufficiencyofprr12 pages 6-8, chowdhury2021haploinsufficiencyofprr12 pages 8-9) |
| Expression / mechanism | Observed: PRR12 is ubiquitously expressed, with highest levels reported in brain (especially cerebellum/pituitary), thyroid, and female reproductive tissues; protein is nuclear-localized; fetal mouse and fetal human brain expression exceeds adult brain expression. PRR12 is associated with poised chromatin regions in embryonic/iPSC/neural progenitor contexts. Hypothesis: PRR12 likely functions in early neurodevelopment and transcriptional/chromatin regulation, possibly involving AT-hook-mediated DNA binding and networks enriched for transcription factors, chromatin regulators, SET-domain proteins, bromodomain proteins, and candidate interactors such as USP7, SOX2, and ESR2; these interactions remain unproven experimentally. | Mixed: observed expression/bioinformatic evidence; mechanistic hypotheses clearly labeled | (chowdhury2021haploinsufficiencyofprr12 pages 9-10, chowdhury2021haploinsufficiencyofprr12 pages 10-11) |
| Diagnosis | Current diagnosis is gene-first and molecular, typically via exome/genome sequencing or other broad genomic testing, supported by the recurrent phenotype of developmental impairment plus variable ocular anomalies. A PRR12-containing microdeletion can also support diagnosis. Ophthalmologic evaluation is important because some posterior-chamber defects may be missed on physical exam; incomplete eye assessments were a study limitation. ClinVar submissions were reported for several variants. | Observed human cohort evidence with practical diagnostic implication | (chowdhury2021haploinsufficiencyofprr12 pages 1-2, chowdhury2021haploinsufficiencyofprr12 pages 6-8, chowdhury2021haploinsufficiencyofprr12 pages 10-11) |
| Management | No disease-specific therapy or standardized treatment algorithm was established in the evidence reviewed. Management is supportive and phenotype-directed in practice, especially developmental services and organ-system evaluation (ophthalmology, cardiology, nephrology) based on observed multisystem involvement; however, explicit surveillance guidelines were not provided in the paper. | Evidence gap / limited inference from observed phenotype | (chowdhury2021haploinsufficiencyofprr12 pages 1-2, chowdhury2021haploinsufficiencyofprr12 pages 6-8) |
| Epidemiology | Prevalence and incidence are not established. Evidence consists of rare case aggregation and database-supported cases. PRR12 loss-of-function variants are extremely rare in population databases, supporting rarity and intolerance to haploinsufficiency. | Observed rarity / evidence gap | (chowdhury2021haploinsufficiencyofprr12 pages 1-2, chowdhury2021haploinsufficiencyofprr12 pages 2-2) |
| Trials / therapies | No relevant interventional clinical trials were identified in the available search results. No gene therapy, RNA therapy, or targeted therapy specific to PRR12-related neuroocular syndrome was established in the available evidence. | Evidence gap | (chowdhury2021haploinsufficiencyofprr12 pages 1-2) |
| Key limitations | Phenotypic variability is substantial. Three individuals had additional genetic findings that could confound attribution. Some ophthalmologic evaluations were incomplete. Genotype-phenotype correlation remains uncertain, especially regarding isoform-specific effects. Functional evidence is limited mainly to expression/bioinformatic data; animal-model validation and mechanistic studies were explicitly called for. | Observed study limitations and explicit author uncertainty | (chowdhury2021haploinsufficiencyofprr12 pages 6-8, chowdhury2021haploinsufficiencyofprr12 pages 10-11, chowdhury2021haploinsufficiencyofprr12 pages 9-10) |


*Table: This table condenses the current disease-defining evidence for PRR12-related neuroocular syndrome into knowledge-base-ready fields. It separates observed human findings from mechanistic hypotheses and highlights where evidence is still lacking.*

## 1. Disease information

### Definition and names

The preferred descriptive name is **PRR12-related neuroocular syndrome**. Literature alternatives include **PRR12-related disorder**, **PRR12 haploinsufficiency disorder**, and **neurodevelopmental, eye, and multisystem abnormalities due to PRR12 haploinsufficiency**. “Dominant complex microphthalmia due to PRR12 variants” describes the ocular-predominant end of the spectrum rather than every affected person, because 12/24 had no documented structural eye defect. (chowdhury2021haploinsufficiencyofprr12 pages 1-2, chowdhury2021haploinsufficiencyofprr12 pages 6-8)

### Identifiers

* **Gene:** *PRR12* (proline rich 12); historical alias **KIAA1205**.
* **Locus:** chromosome 19q13.33–q13.41 region; the disease-causing sequence variants are intragenic, while one reported patient had a 3.352-Mb deletion spanning chr19:50,012,428–53,364,114 (hg19) and many additional genes. (chowdhury2021haploinsufficiencyofprr12 pages 3-4, chowdhury2021haploinsufficiencyofprr12 pages 9-10)
* **MONDO, Orphanet, disease-specific OMIM, MeSH, ICD-10, and ICD-11 identifiers:** no dedicated identifier was verified in the retrieved evidence. A knowledge base should not assign a code without direct database confirmation. Existing ICD/HPO terms can encode component manifestations, but not the molecular syndrome itself.

The evidence is an **aggregated disease-level case series**, assembled through clinical genetics teams and matchmaking platforms, not a population EHR cohort. A separate PrediXcan analysis used BioVU electronic health records from approximately 25,000 genotyped European Americans, but it examined associations with genetically predicted PRR12 expression and does not establish syndrome prevalence or penetrance. (chowdhury2021haploinsufficiencyofprr12 pages 1-2, chowdhury2021haploinsufficiencyofprr12 pages 8-9)

## 2. Etiology, risk, and protective factors

The primary cause is a **germline heterozygous pathogenic PRR12 alteration**, usually arising *de novo*. The supported mechanism is haploinsufficiency. Truncating and splice variants introduce premature termination codons before the penultimate exon and are predicted to undergo nonsense-mediated mRNA decay. (chowdhury2021haploinsufficiencyofprr12 pages 2-3, chowdhury2021haploinsufficiencyofprr12 pages 2-2)

No environmental, infectious, toxic, lifestyle, occupational, or dietary causal factor has been demonstrated. No protective allele, modifier gene, protective exposure, or gene–environment interaction has been established. Additional diagnoses may modify individual presentations: three cohort members carried other clinically relevant variants, including *PIK3CA*, *KDM6B*, and *LZTR1* findings, making attribution of every feature to PRR12 uncertain. (chowdhury2021haploinsufficiencyofprr12 pages 8-9, chowdhury2021haploinsufficiencyofprr12 pages 9-10)

## 3. Phenotypes

The following frequencies are from the 24-person disease-defining cohort and should not be interpreted as population prevalence.

### Neurodevelopment

* **Developmental impairment:** present in all reported sequence-variant cases; 17 had global developmental delay, 3 isolated motor delay, and 4 isolated speech-language delay. Suggested terms: **HP:0001263 Global developmental delay**, **HP:0001270 Motor delay**, and **HP:0000750 Delayed speech and language development**. (chowdhury2021haploinsufficiencyofprr12 pages 2-2)
* **Intellectual disability:** documented in all 11 evaluable individuals older than seven years, ranging from mild to severe. Suggested term: **HP:0001249 Intellectual disability**. (chowdhury2021haploinsufficiencyofprr12 pages 2-2)
* **Hypotonia:** 14/23 (61%), during or beyond the neonatal period. Suggested term: **HP:0001252 Hypotonia**. (chowdhury2021haploinsufficiencyofprr12 pages 8-9)
* Behavioral observations included ADHD, autism-spectrum features, aggression, repetitive or self-injurious behavior in individual cases, but reliable cohort frequencies were not extractable. No validated behavioral profile is established. (chowdhury2021haploinsufficiencyofprr12 pages 5-6)

### Eye and visual system

* **Any structural eye abnormality:** 12/24 (50%).
* **Anophthalmia/microphthalmia:** 4/24 (16.7%); all four were female in this small cohort. Suggested terms: **HP:0000528 Anophthalmia**, **HP:0000568 Microphthalmia**.
* **Coloboma:** 7/24 (29%), most often iris but also optic nerve, macula, chorioretina, and lens; **HP:0000589 Coloboma** and site-specific child terms.
* **Visual impairment:** 17/22 (77%); **HP:0000505 Visual impairment**.
* **Strabismus:** 8/22 (36%); **HP:0000486 Strabismus**.
* Other reported structures included retinal dysplasia, persistent pupillary membrane, Rieger anomaly, optic-nerve hypoplasia or abnormal shape, retinal pigment-epithelium hypertrophy, ptosis, and nystagmus. Patient 1 had bilateral anophthalmia with absent optic nerves, tracts, and chiasm on MRI. (chowdhury2021haploinsufficiencyofprr12 pages 2-3, chowdhury2021haploinsufficiencyofprr12 pages 6-8)

Eye severity therefore ranges from no apparent structural defect to bilateral anophthalmia and profound visual disability. Four individuals lacked complete ophthalmological assessment, so posterior abnormalities may be under-ascertained. (chowdhury2021haploinsufficiencyofprr12 pages 6-8)

### Multisystem findings

* **Congenital heart defect:** 12/23 (52%): six atrial septal defects, two ventricular septal defects, and three pulmonary stenoses, with one person having two defects. Suggested terms: **HP:0001627 Abnormal heart morphology**, **HP:0001631 Atrial septal defect**, **HP:0001629 Ventricular septal defect**, **HP:0001642 Pulmonic stenosis**. (chowdhury2021haploinsufficiencyofprr12 pages 6-8)
* **Kidney/urinary anomaly:** 8/23 (35%), including hydronephrosis, duplicated ureter, and vesicoureteral reflux. Suggested umbrella term: **HP:0012210 Abnormal renal morphology**, plus the corresponding specific HPO terms. (chowdhury2021haploinsufficiencyofprr12 pages 6-8)
* **Failure to thrive:** 13/24 (54%); **HP:0001508 Failure to thrive**.
* **Microcephaly:** 7/24 (29%); **HP:0000252 Microcephaly**.
* **Cryptorchidism:** 5/13 males (38%); **HP:0000028 Cryptorchidism**.
* **Cleft palate:** 4/24 (17%); **HP:0000175 Cleft palate**.
* **Intestinal malrotation:** 2/24 (8%); **HP:0002566 Intestinal malrotation**.
* **Meckel diverticulum:** 1/24 (4%). (chowdhury2021haploinsufficiencyofprr12 pages 8-9, chowdhury2021haploinsufficiencyofprr12 pages 6-8)

Facial findings—wide-set eyes, epicanthal folds, low-set ears, upturned nasal tip, and thin vermilion—each occurred in at least 25%, but the authors found no recognizable gestalt. (chowdhury2021haploinsufficiencyofprr12 pages 8-9, chowdhury2021haploinsufficiencyofprr12 pages 6-8)

No disease-specific EQ-5D, SF-36, PROMIS, educational-attainment, caregiver-burden, or quality-of-life study exists. Nevertheless, intellectual disability, visual impairment, feeding/growth difficulty, and congenital organ disease plausibly impair communication, learning, mobility, and independent functioning; this is clinical inference, not a measured outcome.

## 4. Genetic and molecular information

The cohort contained **12 frameshift, 6 nonsense, 1 splice-site, 2 missense variants, and one gross deletion**. Twenty-one distinct sequence variants were represented. Examples include recurrent c.1521T>G (p.Tyr507*) and c.3273delC (p.Lys1092Argfs*131), and the missense changes c.3505C>T (p.Arg1169Trp) and c.5909T>C (p.Leu1970Pro). The missense changes had PolyPhen-2 scores of 0.998 and 1.000 but remain less directly supported mechanistically than truncating alleles. (chowdhury2021haploinsufficiencyofprr12 pages 2-2, chowdhury2021haploinsufficiencyofprr12 pages 2-3)

PRR12 is strongly constrained against loss of function: pLI 1.00, observed/expected LOF ratio 0.0 (90% CI 0–0.05), and LOEUF 0.051; its missense Z score was +2.98. These are population-constraint metrics, not patient-specific pathogenicity criteria. Disease alleles are germline; no somatic disease mechanism is reported. (chowdhury2021haploinsufficiencyofprr12 pages 2-2)

The main transcript used was **NM_020719.3/ENST00000418929.7**. A shorter 1,215-amino-acid, approximately 130-kDa isoform (**ENST00000615927.1**) omits exons 1–3 and most of exon 4. Eight variants were predicted to spare this short isoform, but phenotype differences between isoform groups were not statistically significant. (chowdhury2021haploinsufficiencyofprr12 pages 2-2, chowdhury2021haploinsufficiencyofprr12 pages 10-11)

No validated modifier gene, methylation episignature, allele-specific expression biomarker, or pathogenic structural rearrangement restricted solely to PRR12 has been established. The large deletion case is informative but confounded by loss of 146 annotated genes, including *PPP2R1A*. (chowdhury2021haploinsufficiencyofprr12 pages 9-10)

## 5. Environmental information

Environmental contributors, infectious triggers, smoking, alcohol, diet, exercise, radiation, pollution, and occupational exposures are **not implicated**. This is a constitutional Mendelian developmental disorder. Standard healthy-lifestyle measures remain appropriate but are not disease-preventive.

## 6. Mechanism and pathophysiology

### Evidence-supported causal chain

1. A heterozygous truncating/splice/deletion allele reduces functional PRR12 dosage, usually through nonsense-mediated decay.
2. PRR12 is a nuclear protein expressed strongly during fetal brain development and in the mouse visual system.
3. Reduced dosage during embryonic development likely disrupts developmental gene regulation in neural, ocular, cardiac, and renal progenitor programs.
4. Abnormal morphogenesis produces congenital ocular and organ defects; altered neural development produces delay, intellectual disability, and hypotonia. Steps 1–2 are supported; steps 3–4 remain a biologically plausible model rather than experimentally proven pathway mapping. (chowdhury2021haploinsufficiencyofprr12 pages 1-2, chowdhury2021haploinsufficiencyofprr12 pages 9-10, chowdhury2021haploinsufficiencyofprr12 pages 2-3)

PRR12 contains two predicted AT-hook DNA-binding domains and is restricted to the nucleus. Coexpression neighborhoods are enriched for transcriptional regulation, chromatin regulators, SET-domain proteins, bromodomain proteins, zinc-finger proteins, and BAH-domain proteins. Candidate interactions with USP7, SOX2, and ESR2 could connect PRR12 to neurodevelopment and eye formation, but the authors emphasize that these interactions and consequences remain experimentally unproven. (chowdhury2021haploinsufficiencyofprr12 pages 10-11)

A useful exact quotation is: **“The exact role of PRR12 in transcriptional regulation remains unclear and will require further functional studies to elucidate.”** (chowdhury2021haploinsufficiencyofprr12 pages 10-11)

Suggested annotations, all provisional except nuclear localization: **GO:0005634 nucleus**; **GO:0006355 regulation of DNA-templated transcription**; **GO:0007420 brain development**; **GO:0001654 eye development**; **GO:0048856 anatomical structure development**; candidate cell types **CL:0000047 neuronal stem cell** and **CL:0000127 astrocyte/other neural lineage terms only where future evidence supports them**. No validated metabolic, immune, inflammatory, autophagic, mitochondrial, lipidomic, metabolomic, proteomic, single-cell, spatial-transcriptomic, CRISPR-screen, or multi-omic disease signature is available.

## 7. Anatomical structures affected

Primary systems are the **central nervous system and eye**; frequent secondary involvement includes heart, kidney/urinary tract, craniofacial structures, gastrointestinal tract, and male genital tract. Suggested UBERON annotations include **UBERON:0000955 brain**, **UBERON:0000970 eye**, **UBERON:0000948 heart**, and **UBERON:0002113 kidney**. Ocular disease may involve globe, iris, optic nerve, retina/choroid, macula, lens, and visual pathways. Findings may be unilateral, bilateral, or asymmetric; severe globe defects were not uniformly bilateral. (chowdhury2021haploinsufficiencyofprr12 pages 2-3, chowdhury2021haploinsufficiencyofprr12 pages 6-8)

At the subcellular level, PRR12 localizes to the **nucleus (GO:0005634)**. Specific vulnerable human cell populations have not been established experimentally. Neural progenitor involvement is inferred from developmental expression and poised chromatin observations, not demonstrated by patient single-cell data. (chowdhury2021haploinsufficiencyofprr12 pages 9-10)

## 8. Temporal development

The disorder is congenital/developmental. Structural eye, heart, kidney, palate, and gastrointestinal abnormalities arise prenatally; hypotonia may be neonatal or persist beyond that period. Developmental delay becomes apparent in infancy or childhood, while intellectual disability is assessable later. The available ages span 5 months–36 years. (chowdhury2021haploinsufficiencyofprr12 pages 2-2, chowdhury2021haploinsufficiencyofprr12 pages 8-9)

There are no defined stages, progression rate, remission pattern, critical treatment window, or prospective natural-history data. Congenital malformations are generally static, whereas developmental capabilities may change with maturation and intervention. Whether retinal, renal, or neuropsychiatric manifestations progress is unknown.

## 9. Inheritance and population

The pattern is **autosomal dominant**, predominantly *de novo*. Recurrence risk for unaffected parents is usually low but not zero because parental germline mosaicism cannot be excluded; an affected individual would theoretically have a 50% transmission risk per pregnancy, subject to currently uncertain penetrance and expressivity. No familial multigenerational series establishes penetrance. Expressivity is clearly variable, especially for ocular severity. (chowdhury2021haploinsufficiencyofprr12 pages 2-2, chowdhury2021haploinsufficiencyofprr12 pages 6-8)

No incidence, prevalence, carrier frequency, founder effect, consanguinity association, ethnic enrichment, geographic concentration, anticipation, or reliable sex ratio exists. The cohort’s 11:13 female-to-male distribution does not demonstrate sex bias. The female-only globe defects are hypothesis-generating because only four such cases occurred. (chowdhury2021haploinsufficiencyofprr12 pages 2-2, chowdhury2021haploinsufficiencyofprr12 pages 6-8)

## 10. Diagnostics

Diagnosis requires identification of a pathogenic/likely pathogenic heterozygous PRR12 variant or deletion in an appropriate phenotype, followed by segregation testing. **Trio exome or genome sequencing** is efficient because the phenotype is broad and frequently *de novo*. Genome sequencing may better detect structural and noncoding variants; chromosomal microarray is appropriate when multiple congenital anomalies suggest a copy-number change. Single-gene sequencing or a neurodevelopmental/anophthalmia–microphthalmia–coloboma panel is reasonable when PRR12 is included. Karyotype/FISH can characterize a suspected translocation but are not first-line for small sequence variants. Mitochondrial and repeat-expansion tests have no disease-specific role. (chowdhury2021haploinsufficiencyofprr12 pages 1-2, chowdhury2021haploinsufficiencyofprr12 pages 9-10)

Baseline phenotyping should include formal pediatric ophthalmology—not merely external inspection—developmental and neurologic assessment, growth/head circumference, echocardiography, renal ultrasound, hearing assessment, and examination for palate, genital, and gastrointestinal anomalies. This is phenotype-directed expert synthesis; no society guideline has yet standardized surveillance. Incomplete ophthalmologic examination demonstrably risks missing posterior defects. (chowdhury2021haploinsufficiencyofprr12 pages 6-8)

Differential diagnoses include *SOX2*-related anophthalmia, *OTX2*-related disease, PAX6 disorders, CHD7/CHARGE syndrome, *PAX2* renal-coloboma syndrome, and *SALL4*-related acro-renal-ocular/Okihiro spectrum. PRR12 disease is distinguished molecularly and by its combination of developmental impairment with variable eye, cardiac, renal, and growth findings. (chowdhury2021haploinsufficiencyofprr12 pages 10-11, chowdhury2021haploinsufficiencyofprr12 pages 9-10)

No biochemical assay, circulating biomarker, diagnostic methylation signature, biopsy finding, or validated RNA/proteomic/metabolomic test exists.

## 11. Outcomes and prognosis

No survival curve, mortality rate, life-expectancy estimate, prospective adult cohort, or prognostic biomarker exists. The oldest reported participant was 36 years, demonstrating survival into adulthood but not normal life expectancy. Morbidity is driven by intellectual/developmental disability, visual impairment, hypotonia, feeding/growth problems, and congenital organ defects. (chowdhury2021haploinsufficiencyofprr12 pages 2-2, chowdhury2021haploinsufficiencyofprr12 pages 6-8)

Recovery of congenital structural defects is not expected, although developmental function and adaptive skills may improve with therapy. Prognosis should be individualized according to visual severity, level of intellectual disability, feeding/growth status, and cardiac/renal disease. These predictors are clinically reasonable but have not been statistically validated for this syndrome.

## 12. Treatment and current applications

There is **no disease-modifying drug, gene therapy, RNA therapy, cell therapy, or PRR12-targeted treatment**, and no relevant registered interventional trial was identified. Management is supportive and multidisciplinary:

* early developmental, speech-language, occupational, and physical therapy;
* low-vision services, refractive/amblyopia treatment, and surgical management of strabismus, cataract, glaucoma risk, coloboma complications, or anophthalmic sockets as individually indicated;
* standard cardiology care for septal defects or pulmonary stenosis;
* nephrology/urology care for hydronephrosis, reflux, or duplicated collecting systems;
* nutritional/feeding support and growth monitoring;
* standard treatment of cleft palate, cryptorchidism, and intestinal malrotation;
* behavioral and educational supports.

Suggested NCIT intervention concepts include **Genetic Counseling**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Supportive Care**, and the appropriate procedure-specific concepts. No response-rate, comparative-effectiveness, adverse-event, pharmacogenomic, or combination-therapy data are available.

## 13. Prevention

The causal *de novo* event cannot presently be prevented through lifestyle or vaccination. Primary prevention is therefore limited to reproductive options after molecular diagnosis: genetic counseling, parental testing, prenatal diagnosis, and preimplantation genetic testing. Secondary prevention consists of early molecular diagnosis and prompt identification of ocular, cardiac, renal, feeding, and developmental complications. Tertiary prevention is multidisciplinary surveillance and rehabilitation intended to reduce avoidable visual loss, developmental disability, renal injury, and cardiac morbidity. Population newborn or carrier screening is not supported by current evidence.

## 14. Other species and natural disease

PRR12 coding sequence is conserved among vertebrates, and developmental mouse expression is strongest in fetal E15 brain relative to adult brain; expression in the mouse visual system has also been reported. However, no naturally occurring PRR12-associated veterinary syndrome, breed predisposition, zoonotic potential, or cross-species transmission is known. (chowdhury2021haploinsufficiencyofprr12 pages 1-2, chowdhury2021haploinsufficiencyofprr12 pages 9-10)

Suggested taxa for comparative work are **Homo sapiens (NCBI Taxon 9606)**, **Mus musculus (10090)**, and **Danio rerio (7955)**. Ortholog-specific NCBI Gene identifiers should be confirmed directly before database loading.

## 15. Model organisms and research priorities

No published PRR12 knockout/knock-in animal model was identified that demonstrably recapitulates the human neuroocular syndrome. No patient-derived iPSC, organoid, or validated cellular disease model was found. The disease-defining authors explicitly stated that mouse and zebrafish models would be valuable for defining PRR12 function and pathogenetic mechanisms. (chowdhury2021haploinsufficiencyofprr12 pages 10-11)

Priority studies are:

1. heterozygous and conditional *Prr12* knockout mice to test brain, eye, heart, and kidney morphogenesis;
2. zebrafish knockdown/knockout with rescue by human wild-type and variant PRR12;
3. patient-derived neural and retinal organoids to assess dosage-sensitive transcriptional programs;
4. RNA sequencing, chromatin accessibility, DNA methylation, and protein-interaction studies;
5. prospective natural-history and standardized ophthalmology cohorts;
6. functional comparison of truncating and missense alleles and the long versus short isoforms.

## Overall assessment

The gene–disease relationship is strongly supported for heterozygous PRR12 loss of function by recurrent *de novo* truncating alleles, population constraint, a consistent developmental phenotype, and supportive ocular cases. The best-established clinical statistics are developmental impairment in essentially all reported individuals, structural eye defects in 50%, visual impairment in 77% of those assessed, hypotonia in 61%, heart defects in 52%, failure to thrive in 54%, and renal anomalies in 35%. Mechanism beyond haploinsufficiency remains preliminary: developmental nuclear gene regulation and chromatin-associated function are credible hypotheses, but not yet a validated signaling pathway. The major unmet needs are a contemporary expanded cohort, prospective natural history, functional models, formal diagnostic criteria, surveillance guidance, and disease-modifying therapy. (chowdhury2021haploinsufficiencyofprr12 pages 1-2, chowdhury2021haploinsufficiencyofprr12 pages 6-8, chowdhury2021haploinsufficiencyofprr12 pages 10-11)

References

1. (chowdhury2021haploinsufficiencyofprr12 pages 2-2): Fuad Chowdhury, Lei Wang, Mohammed Al-Raqad, David J. Amor, Alice Baxová, Šárka Bendová, Elisa Biamino, Alfredo Brusco, Oana Caluseriu, Nancy J. Cox, Tawfiq Froukh, Meral Gunay-Aygun, Miroslava Hančárová, Devon Haynes, Solveig Heide, George Hoganson, Tadashi Kaname, Boris Keren, Kenjiro Kosaki, Kazuo Kubota, Jennifer M. Lemons, Maria A. Magriña, Paul R. Mark, Marie T. McDonald, Sarah Montgomery, Gina M. Morley, Hidenori Ohnishi, Nobuhiko Okamoto, David Rodriguez-Buritica, Patrick Rump, Zdeněk Sedláček, Krista Schatz, Haley Streff, Tomoko Uehara, Jagdeep S. Walia, Patricia G. Wheeler, Antje Wiesener, Christiane Zweier, Koichi Kawakami, Ingrid M. Wentzensen, Seema R. Lalani, Victoria M. Siu, Weimin Bi, and Tugce B. Balci. Haploinsufficiency of prr12 causes a spectrum of neurodevelopmental, eye, and multisystem abnormalities. Genetics in Medicine, 23:1234-1245, Jul 2021. URL: https://doi.org/10.1038/s41436-021-01129-6, doi:10.1038/s41436-021-01129-6. This article has 30 citations and is from a highest quality peer-reviewed journal.

2. (chowdhury2021haploinsufficiencyofprr12 pages 1-2): Fuad Chowdhury, Lei Wang, Mohammed Al-Raqad, David J. Amor, Alice Baxová, Šárka Bendová, Elisa Biamino, Alfredo Brusco, Oana Caluseriu, Nancy J. Cox, Tawfiq Froukh, Meral Gunay-Aygun, Miroslava Hančárová, Devon Haynes, Solveig Heide, George Hoganson, Tadashi Kaname, Boris Keren, Kenjiro Kosaki, Kazuo Kubota, Jennifer M. Lemons, Maria A. Magriña, Paul R. Mark, Marie T. McDonald, Sarah Montgomery, Gina M. Morley, Hidenori Ohnishi, Nobuhiko Okamoto, David Rodriguez-Buritica, Patrick Rump, Zdeněk Sedláček, Krista Schatz, Haley Streff, Tomoko Uehara, Jagdeep S. Walia, Patricia G. Wheeler, Antje Wiesener, Christiane Zweier, Koichi Kawakami, Ingrid M. Wentzensen, Seema R. Lalani, Victoria M. Siu, Weimin Bi, and Tugce B. Balci. Haploinsufficiency of prr12 causes a spectrum of neurodevelopmental, eye, and multisystem abnormalities. Genetics in Medicine, 23:1234-1245, Jul 2021. URL: https://doi.org/10.1038/s41436-021-01129-6, doi:10.1038/s41436-021-01129-6. This article has 30 citations and is from a highest quality peer-reviewed journal.

3. (chowdhury2021haploinsufficiencyofprr12 pages 2-3): Fuad Chowdhury, Lei Wang, Mohammed Al-Raqad, David J. Amor, Alice Baxová, Šárka Bendová, Elisa Biamino, Alfredo Brusco, Oana Caluseriu, Nancy J. Cox, Tawfiq Froukh, Meral Gunay-Aygun, Miroslava Hančárová, Devon Haynes, Solveig Heide, George Hoganson, Tadashi Kaname, Boris Keren, Kenjiro Kosaki, Kazuo Kubota, Jennifer M. Lemons, Maria A. Magriña, Paul R. Mark, Marie T. McDonald, Sarah Montgomery, Gina M. Morley, Hidenori Ohnishi, Nobuhiko Okamoto, David Rodriguez-Buritica, Patrick Rump, Zdeněk Sedláček, Krista Schatz, Haley Streff, Tomoko Uehara, Jagdeep S. Walia, Patricia G. Wheeler, Antje Wiesener, Christiane Zweier, Koichi Kawakami, Ingrid M. Wentzensen, Seema R. Lalani, Victoria M. Siu, Weimin Bi, and Tugce B. Balci. Haploinsufficiency of prr12 causes a spectrum of neurodevelopmental, eye, and multisystem abnormalities. Genetics in Medicine, 23:1234-1245, Jul 2021. URL: https://doi.org/10.1038/s41436-021-01129-6, doi:10.1038/s41436-021-01129-6. This article has 30 citations and is from a highest quality peer-reviewed journal.

4. (chowdhury2021haploinsufficiencyofprr12 pages 6-8): Fuad Chowdhury, Lei Wang, Mohammed Al-Raqad, David J. Amor, Alice Baxová, Šárka Bendová, Elisa Biamino, Alfredo Brusco, Oana Caluseriu, Nancy J. Cox, Tawfiq Froukh, Meral Gunay-Aygun, Miroslava Hančárová, Devon Haynes, Solveig Heide, George Hoganson, Tadashi Kaname, Boris Keren, Kenjiro Kosaki, Kazuo Kubota, Jennifer M. Lemons, Maria A. Magriña, Paul R. Mark, Marie T. McDonald, Sarah Montgomery, Gina M. Morley, Hidenori Ohnishi, Nobuhiko Okamoto, David Rodriguez-Buritica, Patrick Rump, Zdeněk Sedláček, Krista Schatz, Haley Streff, Tomoko Uehara, Jagdeep S. Walia, Patricia G. Wheeler, Antje Wiesener, Christiane Zweier, Koichi Kawakami, Ingrid M. Wentzensen, Seema R. Lalani, Victoria M. Siu, Weimin Bi, and Tugce B. Balci. Haploinsufficiency of prr12 causes a spectrum of neurodevelopmental, eye, and multisystem abnormalities. Genetics in Medicine, 23:1234-1245, Jul 2021. URL: https://doi.org/10.1038/s41436-021-01129-6, doi:10.1038/s41436-021-01129-6. This article has 30 citations and is from a highest quality peer-reviewed journal.

5. (chowdhury2021haploinsufficiencyofprr12 pages 8-9): Fuad Chowdhury, Lei Wang, Mohammed Al-Raqad, David J. Amor, Alice Baxová, Šárka Bendová, Elisa Biamino, Alfredo Brusco, Oana Caluseriu, Nancy J. Cox, Tawfiq Froukh, Meral Gunay-Aygun, Miroslava Hančárová, Devon Haynes, Solveig Heide, George Hoganson, Tadashi Kaname, Boris Keren, Kenjiro Kosaki, Kazuo Kubota, Jennifer M. Lemons, Maria A. Magriña, Paul R. Mark, Marie T. McDonald, Sarah Montgomery, Gina M. Morley, Hidenori Ohnishi, Nobuhiko Okamoto, David Rodriguez-Buritica, Patrick Rump, Zdeněk Sedláček, Krista Schatz, Haley Streff, Tomoko Uehara, Jagdeep S. Walia, Patricia G. Wheeler, Antje Wiesener, Christiane Zweier, Koichi Kawakami, Ingrid M. Wentzensen, Seema R. Lalani, Victoria M. Siu, Weimin Bi, and Tugce B. Balci. Haploinsufficiency of prr12 causes a spectrum of neurodevelopmental, eye, and multisystem abnormalities. Genetics in Medicine, 23:1234-1245, Jul 2021. URL: https://doi.org/10.1038/s41436-021-01129-6, doi:10.1038/s41436-021-01129-6. This article has 30 citations and is from a highest quality peer-reviewed journal.

6. (chowdhury2021haploinsufficiencyofprr12 pages 9-10): Fuad Chowdhury, Lei Wang, Mohammed Al-Raqad, David J. Amor, Alice Baxová, Šárka Bendová, Elisa Biamino, Alfredo Brusco, Oana Caluseriu, Nancy J. Cox, Tawfiq Froukh, Meral Gunay-Aygun, Miroslava Hančárová, Devon Haynes, Solveig Heide, George Hoganson, Tadashi Kaname, Boris Keren, Kenjiro Kosaki, Kazuo Kubota, Jennifer M. Lemons, Maria A. Magriña, Paul R. Mark, Marie T. McDonald, Sarah Montgomery, Gina M. Morley, Hidenori Ohnishi, Nobuhiko Okamoto, David Rodriguez-Buritica, Patrick Rump, Zdeněk Sedláček, Krista Schatz, Haley Streff, Tomoko Uehara, Jagdeep S. Walia, Patricia G. Wheeler, Antje Wiesener, Christiane Zweier, Koichi Kawakami, Ingrid M. Wentzensen, Seema R. Lalani, Victoria M. Siu, Weimin Bi, and Tugce B. Balci. Haploinsufficiency of prr12 causes a spectrum of neurodevelopmental, eye, and multisystem abnormalities. Genetics in Medicine, 23:1234-1245, Jul 2021. URL: https://doi.org/10.1038/s41436-021-01129-6, doi:10.1038/s41436-021-01129-6. This article has 30 citations and is from a highest quality peer-reviewed journal.

7. (chowdhury2021haploinsufficiencyofprr12 pages 10-11): Fuad Chowdhury, Lei Wang, Mohammed Al-Raqad, David J. Amor, Alice Baxová, Šárka Bendová, Elisa Biamino, Alfredo Brusco, Oana Caluseriu, Nancy J. Cox, Tawfiq Froukh, Meral Gunay-Aygun, Miroslava Hančárová, Devon Haynes, Solveig Heide, George Hoganson, Tadashi Kaname, Boris Keren, Kenjiro Kosaki, Kazuo Kubota, Jennifer M. Lemons, Maria A. Magriña, Paul R. Mark, Marie T. McDonald, Sarah Montgomery, Gina M. Morley, Hidenori Ohnishi, Nobuhiko Okamoto, David Rodriguez-Buritica, Patrick Rump, Zdeněk Sedláček, Krista Schatz, Haley Streff, Tomoko Uehara, Jagdeep S. Walia, Patricia G. Wheeler, Antje Wiesener, Christiane Zweier, Koichi Kawakami, Ingrid M. Wentzensen, Seema R. Lalani, Victoria M. Siu, Weimin Bi, and Tugce B. Balci. Haploinsufficiency of prr12 causes a spectrum of neurodevelopmental, eye, and multisystem abnormalities. Genetics in Medicine, 23:1234-1245, Jul 2021. URL: https://doi.org/10.1038/s41436-021-01129-6, doi:10.1038/s41436-021-01129-6. This article has 30 citations and is from a highest quality peer-reviewed journal.

8. (chowdhury2021haploinsufficiencyofprr12 pages 3-4): Fuad Chowdhury, Lei Wang, Mohammed Al-Raqad, David J. Amor, Alice Baxová, Šárka Bendová, Elisa Biamino, Alfredo Brusco, Oana Caluseriu, Nancy J. Cox, Tawfiq Froukh, Meral Gunay-Aygun, Miroslava Hančárová, Devon Haynes, Solveig Heide, George Hoganson, Tadashi Kaname, Boris Keren, Kenjiro Kosaki, Kazuo Kubota, Jennifer M. Lemons, Maria A. Magriña, Paul R. Mark, Marie T. McDonald, Sarah Montgomery, Gina M. Morley, Hidenori Ohnishi, Nobuhiko Okamoto, David Rodriguez-Buritica, Patrick Rump, Zdeněk Sedláček, Krista Schatz, Haley Streff, Tomoko Uehara, Jagdeep S. Walia, Patricia G. Wheeler, Antje Wiesener, Christiane Zweier, Koichi Kawakami, Ingrid M. Wentzensen, Seema R. Lalani, Victoria M. Siu, Weimin Bi, and Tugce B. Balci. Haploinsufficiency of prr12 causes a spectrum of neurodevelopmental, eye, and multisystem abnormalities. Genetics in Medicine, 23:1234-1245, Jul 2021. URL: https://doi.org/10.1038/s41436-021-01129-6, doi:10.1038/s41436-021-01129-6. This article has 30 citations and is from a highest quality peer-reviewed journal.

9. (chowdhury2021haploinsufficiencyofprr12 pages 5-6): Fuad Chowdhury, Lei Wang, Mohammed Al-Raqad, David J. Amor, Alice Baxová, Šárka Bendová, Elisa Biamino, Alfredo Brusco, Oana Caluseriu, Nancy J. Cox, Tawfiq Froukh, Meral Gunay-Aygun, Miroslava Hančárová, Devon Haynes, Solveig Heide, George Hoganson, Tadashi Kaname, Boris Keren, Kenjiro Kosaki, Kazuo Kubota, Jennifer M. Lemons, Maria A. Magriña, Paul R. Mark, Marie T. McDonald, Sarah Montgomery, Gina M. Morley, Hidenori Ohnishi, Nobuhiko Okamoto, David Rodriguez-Buritica, Patrick Rump, Zdeněk Sedláček, Krista Schatz, Haley Streff, Tomoko Uehara, Jagdeep S. Walia, Patricia G. Wheeler, Antje Wiesener, Christiane Zweier, Koichi Kawakami, Ingrid M. Wentzensen, Seema R. Lalani, Victoria M. Siu, Weimin Bi, and Tugce B. Balci. Haploinsufficiency of prr12 causes a spectrum of neurodevelopmental, eye, and multisystem abnormalities. Genetics in Medicine, 23:1234-1245, Jul 2021. URL: https://doi.org/10.1038/s41436-021-01129-6, doi:10.1038/s41436-021-01129-6. This article has 30 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PRR12-Related_Neuroocular_Syndrome-deep-research-falcon_artifacts/artifact-00.md)