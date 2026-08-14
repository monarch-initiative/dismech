---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-05T19:26:15.519852'
end_time: '2026-08-05T19:35:24.994687'
duration_seconds: 549.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Photosensitive Occipital Lobe Epilepsy
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Photosensitive_Occipital_Lobe_Epilepsy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Photosensitive Occipital Lobe Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Photosensitive Occipital Lobe Epilepsy** covering all of the
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
- **Disease Name:** Photosensitive Occipital Lobe Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Photosensitive Occipital Lobe Epilepsy** covering all of the
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


# Photosensitive Occipital Lobe Epilepsy: Disease Characteristics Report

**Evidence date:** literature searched through 2024, with emphasis on the 2023 syndrome-delineation study and recent supporting literature.  
**Disease category:** complex reflex epilepsy phenotype.  
**Evidence caveat:** photosensitive occipital lobe epilepsy (POLE), historically called *idiopathic photosensitive occipital lobe epilepsy* (IPOE), is rare. Much of the quantitative literature concerns **photosensitive epilepsy generally**, not POLE specifically. Such extrapolations are labeled below. PubMed identifiers are omitted where they could not be verified from the retrieved records; DOI links are provided instead.

The following table summarizes the calibration of the evidence used in this report.

| Domain | POLE-specific conclusion | Strongest quantitative/contextual evidence | Evidence type and applicability | Key source with date/DOI or NCT |
|---|---|---|---|---|
| Definition / classification | Photosensitive occipital lobe epilepsy (POLE; also reported historically as idiopathic photosensitive occipital lobe epilepsy) is best treated as a rare reflex focal epilepsy phenotype at the intersection of photosensitive epilepsy and occipital epilepsy, not as synonymous with all photosensitive epilepsies. | Search history identified syndrome-specific publications from 1995, 2014, 2015, 2023, but accessible evidence in this session was largely broader photosensitivity literature; therefore syndrome boundaries are real but direct quantitative extraction here is limited. | Mixed: indirect/contextual; high face validity but limited direct extractable POLE data in-session. | POLE-specific papers identified in search history: Guerrini et al., 1995, DOI: 10.1111/j.1528-1157.1995.tb01631.x; Politi-Elishkevich et al., 2014, DOI: 10.1177/0883073812473366; Koutroumanidis et al., 2015, DOI: 10.1684/epd.2015.0765; Cerrahoğlu Şirin et al., 2023, DOI: 10.1002/epd2.20011 (OpenTargets Search: photosensitive epilepsy) |
| Identifiers / ontology | No dedicated POLE MONDO identifier was established from retrieved evidence; MONDO does contain photosensitive epilepsy. A disease-knowledge entry should therefore map POLE provisionally beneath focal reflex/photosensitive epilepsy concepts until a dedicated ontology term is confirmed. | Open Targets returned MONDO_0015643 for “photosensitive epilepsy,” with no disease-target associations and no POLE-specific target record retrieved. | Direct database-context for broader photosensitive epilepsy; only partial applicability to POLE. | Open Targets context for MONDO:0015643 “photosensitive epilepsy” (OpenTargets Search: photosensitive epilepsy) |
| Genetics | No single causal gene is established for POLE specifically from retrieved evidence. Genetic conclusions should not be overgeneralized from broader photosensitive epilepsy cohorts. | In a 35-patient cohort with genetic photosensitivity, pathogenic variants involved SCN1A (7), CHD2 (6), TPP1 (3), SYNGAP1 (3), GABRA1 (2), plus single cases in GABRG2, KCTD7, MFSD8, KCNC1, GBA, CACNA1A, KCNMA1, FLNA, SZT2, SLC2A1, one 5q33.2-34 deletion, and 3 mitochondrial variants; ion-channel genes accounted for 46.7%; 77.7% remained photosensitive at 1 year. | Direct human cohort for genetic photosensitivity; extrapolation to POLE only, because the cohort was heterogeneous and not occipital-lobe-specific. | Niu et al., 2022, Front Neurol, DOI: 10.3389/fneur.2022.907228 (niu2022geneticandphenotypic pages 6-8, niu2022geneticandphenotypic pages 12-13, niu2022geneticandphenotypic pages 1-3, niu2022geneticandphenotypic pages 13-14) |
| EEG / diagnosis | POLE diagnosis should rely on electroclinical correlation: visually triggered focal occipital seizures and/or occipital-dominant photoparoxysmal/photoconvulsive responses, with careful distinction from generalized photosensitivity syndromes. | Broader PSE literature shows IPS is most sensitive around 15–20 flashes/s; ~49% may also react at 50 flashes/s; standardized IPS can detect epileptiform discharges in 85% of susceptible patients in one cited series; PPR may begin in occipital cortex and spread to parietal/central regions at higher frequencies. | Human EEG/IPS evidence; strong for photosensitivity evaluation, moderate extrapolation to POLE diagnostic workflow. | da Silva & Leal, 2017, Seizure, DOI: 10.1016/j.seizure.2017.04.001 (silva2017photosensitivityandepilepsy pages 10-12, silva2017photosensitivityandepilepsy pages 1-3, silva2017photosensitivityandepilepsy pages 9-10, silva2017photosensitivityandepilepsy pages 4-6); Covanis et al., 2004, Epilepsia, DOI: 10.1111/j.0013-9580.2004.451006.x (covanis2004treatmentofphotosensitivity pages 1-2) |
| Epidemiology | True POLE prevalence/incidence remains unclear from retrieved evidence; it appears under-recognized and much rarer than generic photosensitive epilepsy. | Broader PSE occurs in ~1 in 4,000 population, incidence ~1.1/100,000/year, ~5-fold higher at ages 7–19, with female excess; PPR prevalence in epilepsy clinic populations cited at 5.6%, and 7.3% in ages 10–20 years. | Broader epidemiologic extrapolation only; not POLE-specific. | da Silva & Leal, 2017, DOI: 10.1016/j.seizure.2017.04.001 (silva2017photosensitivityandepilepsy pages 1-3, silva2017photosensitivityandepilepsy pages 3-4, silva2017photosensitivityandepilepsy pages 4-6) |
| Triggers / environmental factors | POLE is expected to share the core visual-trigger architecture of photosensitive epilepsies: flicker, pattern, luminance contrast, and specific color combinations. | Triggering frequencies are typically 8–50 Hz with maximum sensitivity around 20 Hz; long-wavelength red light and red-blue alternation are especially provocative, blue-green less so; reported real-world triggers include television, video games, flashlights, discotheques, venetian blinds, escalators, and patterned materials; sleep deprivation, alcohol, and stress lower threshold. | Human observational/review evidence; strong for trigger counseling, indirect for POLE. | Covanis et al., 2004, DOI: 10.1111/j.0013-9580.2004.451006.x (covanis2004treatmentofphotosensitivity pages 1-2, covanis2004treatmentofphotosensitivity pages 2-3); da Silva & Leal, 2017, DOI: 10.1016/j.seizure.2017.04.001 (silva2017photosensitivityandepilepsy pages 10-12, silva2017photosensitivityandepilepsy pages 9-10, silva2017photosensitivityandepilepsy pages 4-6) |
| Treatment | No POLE-specific randomized treatment data were retrieved. In practice, management is likely to combine trigger reduction with standard antiseizure therapy selected for seizure type and syndrome context. | In broader visual-sensitive epilepsy, valproate was reported as first-line, with 85% seizure freedom in one visually sensitive series and 81% seizure freedom in 67 IPS-sensitive patients; benzodiazepines and ethosuximide also reported effective. Colored lenses suppressed PPR in 77% and reduced it in 19% in one review summary. | Human clinical review evidence for broader photosensitivity; extrapolation to POLE, especially if focal semiology predominates. | Covanis et al., 2004, DOI: 10.1111/j.0013-9580.2004.451006.x (covanis2004treatmentofphotosensitivity pages 2-3); da Silva & Leal, 2017, DOI: 10.1016/j.seizure.2017.04.001 (silva2017photosensitivityandepilepsy pages 10-12) |
| Prognosis | POLE prognosis is insufficiently quantified from retrieved direct evidence; available literature suggests many photosensitive epilepsies are time-limited, but this cannot be assumed uniformly for POLE. | Broader PSE data suggest remission in the second decade in about two-thirds of valproate-treated patients and over 50% of untreated patients; 80% of pattern-sensitive epilepsy patients were seizure-free for >2 years in one cited series. In the genetic photosensitivity cohort, 77.7% still showed photosensitivity at 1 year. | Mixed: broader syndrome extrapolation plus heterogeneous genetic cohort; low-to-moderate direct applicability to POLE. | da Silva & Leal, 2017, DOI: 10.1016/j.seizure.2017.04.001 (silva2017photosensitivityandepilepsy pages 1-3, silva2017photosensitivityandepilepsy pages 4-6); Niu et al., 2022, DOI: 10.3389/fneur.2022.907228 (niu2022geneticandphenotypic pages 1-3, niu2022geneticandphenotypic pages 13-14) |
| Trials / real-world implementation | Clinical trials in this space largely use the human photosensitivity model (suppression of PPR/SPR during IPS) rather than POLE-specific seizure outcomes. | Completed/terminated trials include brivaracetam (NCT00401648, n=20), JNJ-26489112 (NCT00579384, n=12), BGG492/AMPA antagonist (NCT00784212, n=13), ICA-105665 (NCT00979004, terminated after SAE; n=13), ACT-709478 (NCT03239691, n=5), E2730 (NCT03603639, n=6), specialty lenses (NCT04076410, n=28), RLS103 (NCT05678881, n=2), NPT 2042 (NCT06525649, n=5). Endpoints are EEG biomarker suppression, not POLE natural-history endpoints. | Direct interventional evidence for photosensitivity-platform pharmacodynamics; indirect for POLE treatment efficacy. | ClinicalTrials.gov records: NCT00401648, NCT00579384, NCT00784212, NCT00979004, NCT03239691, NCT03603639, NCT04076410, NCT05678881, NCT06525649 (NCT00579384 chunk 1, NCT00979004 chunk 1, NCT03603639 chunk 1, NCT00401648 chunk 1, NCT00784212 chunk 1, NCT03239691 chunk 1, NCT04076410 chunk 2, NCT03603639 chunk 2) |
| Animal model / comparative biology | No POLE-specific animal model was retrieved. The strongest natural model is the photosensitive baboon, but it models genetic generalized photosensitive epilepsy rather than focal occipital POLE. | In Papio hamadryas papio, generalized spike-wave discharges occurred in 49% of 671 baboons at 4–6 Hz; photoepileptic responses in 23% of epileptic baboons, maximal at 20–25 Hz IPS; heritability estimates included h2=0.33 for spontaneous seizures and h2=0.19 for IEDs; RBFOX1 emerged as a candidate association. Imaging and intracranial EEG implicate widespread visual, parietal, frontal, motor, and thalamic networks. | Direct natural-disease/model evidence for photosensitive GGE; only mechanistic extrapolation to POLE. | Szabo & Salinas, 2021, DOI: 10.1016/j.yebeh.2021.108012 (szabo2021thebaboonin pages 1-2, szabo2021thebaboonin pages 2-3); Szabo & Salinas, 2022, DOI: 10.3389/fvets.2022.908801 (szabo2022neuroimaginginthe pages 1-2); Szabó et al., 2012, DOI: 10.1016/j.eplepsyres.2012.02.016 (szabo2012baboonmodelof pages 1-2, szabo2012baboonmodelof pages 8-10) |
| Major evidence gaps | The main limitation is lack of accessible POLE-specific primary data in this session for identifiers, prevalence, inheritance, variant spectrum, standardized diagnostic criteria, prognosis, and therapy response. | No retrieved POLE-specific omics, epigenetic studies, infectious causes, validated biomarkers, WES/WGS utility studies, surgery series, gene/cell/RNA therapy, or dedicated animal model. Open Targets showed no disease-target associations for MONDO photosensitive epilepsy. | Direct evidence-gap conclusion. This should be made explicit in the final report to avoid overclaiming from broader PSE literature. | Open Targets context plus retrieved literature/trials landscape (OpenTargets Search: photosensitive epilepsy, NCT00579384 chunk 1, NCT00979004 chunk 1, NCT03603639 chunk 1, NCT00401648 chunk 1, NCT00784212 chunk 1, NCT03239691 chunk 1, NCT04076410 chunk 2, NCT03603639 chunk 2) |


*Table: This table calibrates what can be concluded specifically for photosensitive occipital lobe epilepsy versus what must be extrapolated from broader photosensitive epilepsy research. It is useful for structuring a cautious, evidence-graded disease report without overstating gene, epidemiology, or treatment claims.*

## 1. Disease information

### Definition and scope

POLE is an electroclinical phenotype in which visual stimulation reproducibly provokes seizures with an occipital onset or occipital semiology. It occupies the boundary between **reflex focal epilepsy** and the wider genetically influenced photosensitivity spectrum. It should not be equated with either (1) an isolated photoparoxysmal response (PPR) in a person without visually induced seizures or (2) generalized photosensitive syndromes such as juvenile myoclonic epilepsy, epilepsy with eyelid myoclonia, Dravet syndrome, or progressive myoclonus epilepsy.

The principal syndrome literature includes Guerrini et al. (1995; [DOI](https://doi.org/10.1111/j.1528-1157.1995.tb01631.x)), Politi-Elishkevich et al. (2014; [DOI](https://doi.org/10.1177/0883073812473366)), Koutroumanidis et al. (2015; [DOI](https://doi.org/10.1684/epd.2015.0765)), and the important 2023 long-term reassessment by Cerrahoğlu Şirin et al. ([DOI](https://doi.org/10.1002/epd2.20011)). These reports support recognition of an underdiagnosed reflex focal phenotype, although POLE is not presently among the best-established, separately codified ILAE epilepsy syndromes.

### Identifiers and synonyms

- **MONDO:** no dedicated POLE entry was established in the retrieved evidence. The broader concept **photosensitive epilepsy** is **MONDO:0015643**. Open Targets returned no associated targets for that MONDO disease record, underscoring the absence of a validated POLE-specific target set. (OpenTargets Search: photosensitive epilepsy)
- **OMIM/Orphanet:** no dedicated, verified POLE record was found.
- **ICD-10/ICD-11:** no unique POLE code was verified; coding generally falls under focal epilepsy/reflex epilepsy according to local coding rules.
- **MeSH:** use broader concepts such as *Epilepsy, Reflex* and *Epilepsy, Partial/Occipital Lobe Epilepsy*; no distinct POLE descriptor was verified.
- **Synonyms:** photosensitive occipital lobe epilepsy; idiopathic photosensitive occipital lobe epilepsy; idiopathic/possibly genetic photosensitive occipital epilepsy; visually induced occipital epilepsy.

This report synthesizes **aggregated disease-level literature**, not individual EHR records. Small cohorts and case reports are nevertheless prominent because of the syndrome’s rarity.

## 2. Etiology

### Causal and risk factors

POLE is most plausibly a **complex genetically influenced network epilepsy** in which visual stimuli recruit an unusually excitable occipital cortex. No single gene, pathogenic variant, infectious agent, toxin, or structural lesion has been proven to cause the syndrome as presently defined.

Broader genetic-photosensitivity data demonstrate marked locus and syndrome heterogeneity. A 2022 cohort selected 35 patients with pathogenic genetic findings and photosensitivity: **SCN1A** variants occurred in 7, **CHD2** in 6, **TPP1** in 3, **SYNGAP1** in 3, and **GABRA1** in 2; other findings included GABRG2, KCTD7, MFSD8, KCNC1, GBA, CACNA1A, KCNMA1, FLNA, SZT2, SLC2A1, a 5q33.2–q34 deletion, and mitochondrial variants. Ion-channel genes represented 46.7% of cases. This cohort chiefly comprised progressive myoclonus epilepsy, Dravet syndrome, and developmental/epileptic encephalopathies—not POLE—so these genes are **differential-diagnostic or susceptibility candidates, not established POLE genes**. (niu2022geneticandphenotypic pages 6-8, niu2022geneticandphenotypic pages 12-13, niu2022geneticandphenotypic pages 1-3)

An exact abstract statement from that study is: **“The most common genes for epilepsy with genetic photosensitivity are SCN1A and CHD2, and the most common syndromes are PME and Dravet syndrome.”** The authors also proposed MFSD8, KCNMA1, SZT2, FLNA, and SLC2A1 as candidates, which should not be interpreted as validated POLE associations. ([Published August 2022](https://doi.org/10.3389/fneur.2022.907228)) (niu2022geneticandphenotypic pages 1-3, niu2022geneticandphenotypic pages 13-14)

### Environmental and modifying risks

Relevant provocations include binocular flicker, high-contrast striped patterns, television/video games, flashing lamps, discotheque lighting, sunlight flickering through trees, escalators, blinds, and patterned fabrics. Sensitivity generally spans approximately **8–50 Hz**, peaking near **15–20 Hz**; long-wavelength red and alternating red-blue stimuli are particularly provocative. Sleep deprivation, stress, and alcohol can lower seizure threshold. (silva2017photosensitivityandepilepsy pages 10-12, covanis2004treatmentofphotosensitivity pages 1-2, silva2017photosensitivityandepilepsy pages 9-10)

Female sex, adolescence, and family history are established correlates of broader photosensitivity, but POLE-specific risk ratios are unavailable. Broader photosensitive epilepsy is approximately twice as common in females and often begins around puberty. (silva2017photosensitivityandepilepsy pages 1-3, silva2017photosensitivityandepilepsy pages 4-6)

### Protective factors and gene–environment interaction

No validated protective allele is known. Environmental protection comprises reducing stimulus contrast, frequency, duration, and visual-field exposure; increasing screen distance; avoiding sleep deprivation; and using monocular occlusion or tested tinted lenses. The causal interaction is best expressed as:

**Inherited/developmental cortical susceptibility → excessive visual-cortical synchronization during provocative stimulation → occipital epileptiform discharge → propagation through parietal, temporal, motor, and thalamocortical networks → focal visual seizure, impaired awareness, motor manifestations, or bilateral tonic-clonic seizure.** (silva2017photosensitivityandepilepsy pages 1-3, covanis2004treatmentofphotosensitivity pages 1-2, silva2017photosensitivityandepilepsy pages 12-13)

## 3. Phenotypes

| Phenotype | Characteristics and suggested HPO term |
|---|---|
| Elementary visual seizure | Brief multicolored or bright circular spots, flashes, phosphenes, or formed visual phenomena; episodic, commonly seconds to minutes. **HP:0000576 Visual hallucination**; consider **HP:0032792 Focal aware seizure**. |
| Ictal blindness/visual loss | Transient obscuration or loss of vision. **HP:0000618 Blindness** qualified as ictal/transient. |
| Visual-field disturbance | Hemifield or quadrant symptoms may indicate contralateral occipital onset. **HP:0001123 Visual field defect**. |
| Eye/head deviation | Tonic deviation may accompany spread from occipital cortex. **HP:0007359 Focal motor seizure**. |
| Headache, nausea, vomiting | May follow occipital seizures and creates overlap with migraine. **HP:0002315 Headache**, **HP:0002018 Nausea**, **HP:0002013 Vomiting**. |
| Impaired awareness | Occurs after propagation beyond occipital cortex. **HP:0002384 Focal impaired awareness seizure**. |
| Bilateral tonic-clonic seizure | May follow focal occipital onset. **HP:0007334 Bilateral tonic-clonic seizure**. |
| Photosensitivity/PPR | EEG epileptiform response to intermittent photic stimulation; not itself synonymous with clinical epilepsy. Suggested **HP:0012452 Abnormal electroencephalogram** plus a local modifier for photoparoxysmal response. |

Severity is variable: some patients have only avoidable reflex focal seizures; others also have spontaneous seizures or focal-to-bilateral convulsions. The course is episodic rather than continuously progressive. Disease-specific frequencies and validated POLE quality-of-life scores were not retrieved. Likely burdens include screen avoidance, educational/work limitations, driving restrictions, anxiety around public lighting, injury risk, and medication adverse effects. A lens study explicitly included six-month satisfaction and quality-of-life assessment, illustrating current real-world attention to these outcomes. (NCT04076410 chunk 2)

## 4. Genetic and molecular information

- **Established POLE-causal genes:** none.
- **Established POLE pathogenic variants/HGNC IDs:** none; therefore no defensible POLE-specific allele frequencies, somatic/germline classification, or variant-level ACMG assertions can be supplied.
- **Potential broader-photosensitivity genes:** CHD2, SCN1A, GABRA1, GABRG2, SYNGAP1 and genes causing progressive myoclonus epilepsy or developmental encephalopathy. Their presence usually argues for a broader syndromic diagnosis rather than isolated POLE. (niu2022geneticandphenotypic pages 6-8, niu2022geneticandphenotypic pages 12-13)
- **Chromosomal findings:** a 5q33.2–q34 deletion occurred in one heterogeneous genetic-photosensitivity cohort; it is not a recurrent POLE lesion. (niu2022geneticandphenotypic pages 1-3)
- **Modifier genes, anticipation, founder effects, germline mosaicism, protective alleles:** not established for POLE.
- **Epigenetics:** no POLE-specific methylation, histone, or chromatin signature was found.

Consequently, POLE should not currently be represented in a knowledge base as a Mendelian disorder with a fixed gene–disease relationship.

## 5. Environmental information

Visual stimulation is a **trigger**, not generally the underlying cause. Television was reported as a trigger in 41% and patterns in 39.7% of a broader photosensitive cohort. PPR-positive patients reported visually induced seizures much more often than PPR-negative patients (63% versus 2.3%). These figures are not POLE-specific. (silva2017photosensitivityandepilepsy pages 3-4, silva2017photosensitivityandepilepsy pages 4-6)

No association with smoking, diet, exercise, occupational toxins, ionizing radiation, pollution, bacteria, viruses, fungi, or parasites is established. Alcohol, fatigue, and sleep deprivation are clinically relevant threshold modifiers. (covanis2004treatmentofphotosensitivity pages 1-2)

## 6. Mechanism and pathophysiology

### Causal network

1. **Upstream trigger:** rhythmic luminance/color contrast or spatial pattern activates binocularly innervated neurons in primary and extrastriate visual cortex.
2. **Local susceptibility:** deficient inhibition and/or excessive excitation permits hypersynchronous activity in occipital networks. At lower stimulation frequencies PPR may remain occipital; increasing frequency facilitates parietal and central spread. (silva2017photosensitivityandepilepsy pages 1-3, silva2017photosensitivityandepilepsy pages 3-4)
3. **Network propagation:** abnormal occipital–parietal, occipital–supplementary-motor, prefrontal, and thalamocortical connectivity transforms a visual response into an epileptic discharge. Increased occipital–supplementary motor connectivity is one proposed route to motor manifestations. (silva2017photosensitivityandepilepsy pages 1-3, silva2017photosensitivityandepilepsy pages 12-13)
4. **Clinical output:** local occipital discharge produces visual hallucination or blindness; spread produces eye/head deviation, altered awareness, myoclonus, or focal-to-bilateral tonic-clonic seizure.

### Molecular/cellular interpretation

Broader genetic findings implicate voltage-gated sodium/calcium/potassium channels, GABA receptors, synaptic regulation, chromatin remodeling, and lysosomal/mitochondrial disease. These converge on excitation–inhibition imbalance but do not define a unique POLE biochemical pathway. No consistent inflammation, autoimmunity, neurodegeneration, oxidative injury, metabolic signature, protein aggregation, or tissue destruction has been demonstrated in isolated POLE.

**Suggested GO biological processes:** GO:0050804 modulation of chemical synaptic transmission; GO:0099536 synaptic signaling; GO:0007214 gamma-aminobutyric acid signaling pathway; GO:0007268 chemical synaptic transmission; GO:0007601 visual perception; GO:0007610 behavior; GO:0019228 neuronal action potential.  
**Suggested cellular components:** GO:0045202 synapse; GO:0098794 postsynapse; GO:0030425 dendrite; GO:0030424 axon; GO:0005886 plasma membrane; GO:0034702 ion-channel complex.  
**Suggested cell types:** CL:0000540 neuron; CL:0000099 interneuron; CL:0000617 GABAergic neuron; CL:0000679 glutamatergic neuron; retinal photoreceptors are stimulus sensors, not proven diseased cells.

No POLE-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, multi-omic, or CRISPR-screen study was identified.

## 7. Anatomical structures affected

The primary system is the **central nervous system**, particularly bilateral or unilateral occipital visual cortex. Relevant structures include primary visual cortex, extrastriate cortex, parieto-occipital junction, posterior parietal association cortex, and propagation pathways to temporal, frontal/motor, and thalamic networks. Broader imaging research supports abnormal visual-cortex structure/connectivity but not destructive occipital pathology. (silva2017photosensitivityandepilepsy pages 1-3, silva2017photosensitivityandepilepsy pages 12-13)

**Suggested UBERON terms:** UBERON:0000955 brain; UBERON:0002021 occipital lobe; UBERON:0000411 visual cortex; UBERON:0001897 dorsal thalamus; UBERON:0001871 temporal lobe; UBERON:0001870 frontal cortex. The disease can be left-sided, right-sided, bilateral, or rapidly bilateral; no fixed lateralization is defining. Routine MRI is usually expected to be normal in an idiopathic/possibly genetic phenotype. A structural occipital lesion should prompt classification as structural focal epilepsy rather than uncomplicated POLE.

## 8. Temporal development

Onset is most often pediatric or adolescent, but adult-onset photosensitivity and POLE-like presentations are documented. Onset is episodic and stimulus-linked rather than anatomically progressive. Broader photosensitive epilepsy incidence is about fivefold higher at ages 7–19 years. (silva2017photosensitivityandepilepsy pages 4-6)

The course may include:

- reflex seizures only;
- reflex plus spontaneous focal seizures;
- focal-to-bilateral convulsions;
- decreasing photosensitivity after adolescence; or
- persistent photosensitivity into adulthood.

Broader literature reports second-decade remission in approximately two-thirds of valproate-treated and over half of untreated patients, whereas **77.7%** of a severely affected genetic cohort retained photosensitivity after one year. These discrepant figures demonstrate that prognosis depends strongly on the underlying syndrome and must not be transferred uncritically to POLE. (niu2022geneticandphenotypic pages 1-3, silva2017photosensitivityandepilepsy pages 1-3)

## 9. Inheritance and population

No reliable POLE-specific prevalence, incidence, sex ratio, penetrance, carrier frequency, or population distribution was found. Broader photosensitive epilepsy estimates are approximately **1 in 4,000 population** and **1.1 new cases per 100,000/year**, with typical onset near puberty and an approximately twofold female excess. Clinic PPR prevalence is about 5.6%, rising to 7.3% at ages 10–20 in cited datasets. (silva2017photosensitivityandepilepsy pages 3-4, silva2017photosensitivityandepilepsy pages 4-6)

Familial clustering supports complex/polygenic inheritance with incomplete, age-dependent penetrance and variable expressivity. Autosomal-dominant CHD2-related photosensitivity is relevant to differential diagnosis, but a monogenic POLE inheritance pattern is unproven. No anticipation, consanguinity effect, founder mutation, or geographic variant distribution has been established. (silva2017photosensitivityandepilepsy pages 9-10)

## 10. Diagnostics

### Core evaluation

1. **Detailed history/video:** characterize elementary visual symptoms, duration, visual-field location, awareness, eye/head deviation, headache, and exact visual triggers.
2. **Routine video-EEG with standardized intermittent photic stimulation (IPS):** test eyes-open, eye-closure, and eyes-closed conditions, stopping stimulation promptly if a generalized or escalating discharge occurs. IPS around 15–20 flashes/s is generally most sensitive; broader protocols survey approximately 2–60 Hz. (silva2017photosensitivityandepilepsy pages 10-12, silva2017photosensitivityandepilepsy pages 9-10, NCT03603639 chunk 2)
3. **Pattern stimulation** where appropriate, performed in a controlled neurophysiology setting.
4. **Brain MRI using an epilepsy protocol:** exclude occipital tumor, malformation, vascular lesion, gliosis, or other structural cause.
5. **Formal ophthalmologic assessment** when persistent field loss or retinal disease is possible.

A PPR is an EEG biomarker, not sufficient alone for POLE. Diagnosis requires concordant clinical seizures or compelling occipital electroclinical evidence. PPR can occur in otherwise healthy individuals; broader estimates include 7.6% in healthy children in one cited dataset. (silva2017photosensitivityandepilepsy pages 3-4)

### Differential diagnosis

- migraine with visual aura—typically slower evolution and longer visual symptoms;
- childhood occipital visual epilepsy/Gastaut-type epilepsy without a photosensitive requirement;
- epilepsy with eyelid myoclonia, juvenile myoclonic epilepsy, and other generalized photosensitive epilepsies;
- pattern-sensitive epilepsy;
- structural occipital epilepsy;
- syncope or psychogenic nonepileptic events;
- retinal/optic-nerve disease;
- Dravet syndrome, CHD2 encephalopathy, progressive myoclonus epilepsy, GLUT1 deficiency, and mitochondrial/lysosomal disease when development, neurologic examination, MRI, or EEG background is abnormal. A genetic cohort showed abnormal background and MRI principally in progressive myoclonus epilepsy, which is useful diagnostically. (niu2022geneticandphenotypic pages 6-8, niu2022geneticandphenotypic pages 1-3)

### Genetic testing

Routine single-gene testing is not indicated for a developmentally normal, MRI-negative, otherwise typical POLE presentation. Use an epilepsy panel or WES/WGS when there is developmental delay, drug resistance, early onset, abnormal neurologic examination/MRI, generalized/myoclonic features, or a strong family history. Panels should include CHD2, SCN1A, GABRA1, GABRG2, SYNGAP1 and phenotype-directed PME/metabolic genes. CMA is reasonable for syndromic developmental epilepsy; karyotype, FISH, mitochondrial DNA, and repeat-expansion testing are phenotype-driven. No POLE-specific omics diagnostic or population-screening program exists.

## 11. Outcome and prognosis

POLE itself is not known to shorten life expectancy, and no syndrome-specific survival or mortality rate is available. Morbidity arises from convulsive injury, impaired awareness, driving limitations, educational/occupational restrictions, anxiety, and treatment toxicity. General epilepsy risks, including status epilepticus and sudden unexpected death in epilepsy, depend more on uncontrolled convulsive-seizure burden than on photosensitivity alone.

Favorable factors probably include reflex-only seizures, reliable trigger avoidance, normal development/MRI/background EEG, and medication responsiveness. Unfavorable indicators include spontaneous seizures, generalized convulsions, broad PPR frequency range, developmental impairment, abnormal MRI/background EEG, and an underlying encephalopathy or PME. In broader pattern-sensitive epilepsy, 80% in one series were seizure-free for over two years, but a POLE-specific rate remains unavailable. (silva2017photosensitivityandepilepsy pages 4-6)

## 12. Treatment

### Practical strategy

1. Educate the patient and family about triggers and immediate countermeasures.
2. If exposure occurs, **cover one eye completely and turn away**; simply closing both eyes may retain binocular stimulation through the lids.
3. Increase screen distance—historically at least three screen widths—use well-lit rooms and modern high-refresh/low-flicker displays, reduce contrast/brightness, avoid provocative patterns, and maintain sleep. (covanis2004treatmentofphotosensitivity pages 1-2, covanis2004treatmentofphotosensitivity pages 2-3)
4. Consider individually EEG-tested colored or polarized lenses. Broader evidence found PPR disappearance in **77%** and reduction in **19%** with colored filters; a 28-participant study tested Z1 and four experimental lenses with EEG and quality-of-life endpoints (NCT04076410). (silva2017photosensitivityandepilepsy pages 10-12, NCT04076410 chunk 2)
5. Prescribe antiseizure medication when avoidance is impractical, spontaneous seizures occur, or events are severe.

### Pharmacotherapy

Valproate has the strongest historical evidence across generalized/visually sensitive epilepsies, with reported seizure freedom of **81% in 67 IPS-sensitive patients** and 85% in another visually sensitive series. It requires major caution in people who could become pregnant. Levetiracetam is commonly used and is often preferable where pregnancy-related valproate risk is important. Lamotrigine or other focal-seizure agents may be considered according to the complete electroclinical syndrome, but some sodium-channel agents can aggravate particular generalized/myoclonic epilepsies. (covanis2004treatmentofphotosensitivity pages 2-3)

The human photosensitivity model demonstrates rapid PPR suppression by SV2A ligands. In a randomized crossover study of nine completers, intravenous brivaracetam eliminated PPR at a median **2 minutes**, versus **7.5 minutes** for levetiracetam; combined analyses estimated 61% faster elimination, but the authors cautioned that clinical-outcome comparisons remain necessary. Exact abstract wording: **“Outcome studies directly comparing LEV and BRV are needed to define the clinical utility of the response with BRV.”** ([Published September 2020](https://doi.org/10.1007/s40263-020-00761-1))

**Suggested NCIt intervention concepts:** Anticonvulsant Therapy; Valproic Acid; Levetiracetam; Brivaracetam; Benzodiazepine; Patient Education; Avoidance Intervention; Protective Eyewear. No POLE-specific pharmacogenomic rule, surgery series, gene therapy, cell therapy, RNA therapy, or immunotherapy was identified. Surgery is reserved for a demonstrable, concordant structural occipital epileptogenic lesion, not the typical bilateral reflex phenotype.

### Experimental trials

The field uses reproducible IPS-induced PPR suppression as a small, efficient Phase IIa pharmacodynamic platform rather than as proof of long-term seizure control. Examples include brivaracetam NCT00401648 (n=20), JNJ-26489112 NCT00579384 (n=12), the AMPA/kainate antagonist BGG492 NCT00784212 (n=13), ACT-709478 NCT03239691 (n=5), and E2730 NCT03603639 (n=6). BGG492 showed dose-dependent PPR suppression; ICA-105665 NCT00979004 was terminated after a serious adverse event at 600 mg. None was POLE-specific. (NCT00579384 chunk 1, NCT00979004 chunk 1, NCT03603639 chunk 1, NCT00401648 chunk 1, NCT00784212 chunk 1, NCT03239691 chunk 1)

## 13. Prevention

- **Primary prevention:** no method prevents the inherited/developmental susceptibility. Public-facing media standards that limit flash rate, red saturation, luminance transitions, and high-contrast patterns reduce population exposure.
- **Secondary prevention:** there is no population or newborn screening. Targeted EEG/IPS is reasonable after visually induced events or in selected high-risk epilepsy syndromes; routine testing of asymptomatic people is unsupported.
- **Tertiary prevention:** trigger education, sleep hygiene, medication adherence, rescue planning, injury precautions, individualized lens testing, and control of spontaneous convulsions.
- **Genetic counseling:** recurrence risk is generally empirical unless testing establishes another defined genetic syndrome. Prenatal or preimplantation testing is not available for nonsyndromic POLE without a familial pathogenic variant.
- **Vaccination/infectious prophylaxis:** not applicable.

Nonpharmacologic management alone may suffice when seizures are exclusively visual, rare, and reliably avoidable. (covanis2004treatmentofphotosensitivity pages 1-2, covanis2004treatmentofphotosensitivity pages 2-3)

## 14. Other species and natural disease

The principal natural comparative model is the **Senegalese baboon, Papio hamadryas papio** (NCBI Taxonomy identification should be verified against the current taxonomy record before database ingestion). It naturally develops myoclonic, absence, and generalized tonic-clonic seizures with photosensitivity. This is a model of **genetic generalized epilepsy**, not a homologous focal POLE disease.

Among 671 baboons, 49% displayed 4–6-Hz generalized spike-wave discharges; photoepileptic responses occurred in 23% of epileptic animals and were maximal at 20–25-Hz stimulation. Pedigree estimates were h²=0.33 for spontaneous seizures and h²=0.19 for interictal discharges; RBFOX1 was a candidate association. (szabo2022neuroimaginginthe pages 1-2, szabo2021thebaboonin pages 1-2)

There is no zoonotic transmission. No companion-animal breed with a validated natural POLE equivalent was identified.

## 15. Model organisms

### Baboon model

Intracranial EEG, PET, MRI/fMRI, and MEG in photosensitive baboons implicate occipital, parietal, orbitofrontal, motor, insular, and thalamic networks. Myoclonic and generalized tonic-clonic seizures can occur spontaneously or after intermittent light stimulation. The model’s gyrencephalic brain, visual-system similarity, and pedigreed colonies confer high translational value for network mapping and antiseizure-drug proof of principle. (szabo2012baboonmodelof pages 1-2, szabo2022neuroimaginginthe pages 1-2, szabo2021thebaboonin pages 2-3, szabo2011functionalpetevaluation pages 1-2)

Limitations include expense, limited availability, subspecies differences, imperfect seizure provocation, electrode displacement/injury, effects of anesthesia and medication, and its generalized rather than focal-occipital electroclinical phenotype. Maximal photic sensitivity also differs—approximately 20–25 Hz in baboons versus roughly 12–20 Hz in humans. (szabo2021thebaboonin pages 1-2, szabo2012baboonmodelof pages 8-10)

No validated POLE-specific mouse, rat, zebrafish, Drosophila, organoid, iPSC, knock-in, or conditional model was identified. Generic ion-channel and CHD2 models may illuminate photosensitivity but cannot presently be claimed to recapitulate POLE.

## Overall assessment

POLE is best represented as a **rare, under-recognized reflex focal epilepsy phenotype characterized by visually induced occipital seizures and supportive occipital EEG/PPR findings**. Its most defensible mechanistic model is visual-cortical hyperexcitability with network propagation, rather than a single-gene or structural disorder. The 2023 syndrome reassessment is the most recent directly relevant publication located, but recent molecular and interventional advances largely concern broader photosensitive epilepsy. Priority research needs are a consensus case definition, multinational registry, POLE-specific prevalence and natural-history estimates, harmonized IPS/video-EEG phenotyping, genomic case-control studies, and prospective comparative treatment studies.

References

1. (OpenTargets Search: photosensitive epilepsy): Open Targets Query (photosensitive epilepsy, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (niu2022geneticandphenotypic pages 6-8): Yue Niu, Pan Gong, Xianru Jiao, Zhao Xu, Yuehua Zhang, and Zhixian Yang. Genetic and phenotypic spectrum of chinese patients with epilepsy and photosensitivity. Frontiers in Neurology, Aug 2022. URL: https://doi.org/10.3389/fneur.2022.907228, doi:10.3389/fneur.2022.907228. This article has 18 citations and is from a peer-reviewed journal.

3. (niu2022geneticandphenotypic pages 12-13): Yue Niu, Pan Gong, Xianru Jiao, Zhao Xu, Yuehua Zhang, and Zhixian Yang. Genetic and phenotypic spectrum of chinese patients with epilepsy and photosensitivity. Frontiers in Neurology, Aug 2022. URL: https://doi.org/10.3389/fneur.2022.907228, doi:10.3389/fneur.2022.907228. This article has 18 citations and is from a peer-reviewed journal.

4. (niu2022geneticandphenotypic pages 1-3): Yue Niu, Pan Gong, Xianru Jiao, Zhao Xu, Yuehua Zhang, and Zhixian Yang. Genetic and phenotypic spectrum of chinese patients with epilepsy and photosensitivity. Frontiers in Neurology, Aug 2022. URL: https://doi.org/10.3389/fneur.2022.907228, doi:10.3389/fneur.2022.907228. This article has 18 citations and is from a peer-reviewed journal.

5. (niu2022geneticandphenotypic pages 13-14): Yue Niu, Pan Gong, Xianru Jiao, Zhao Xu, Yuehua Zhang, and Zhixian Yang. Genetic and phenotypic spectrum of chinese patients with epilepsy and photosensitivity. Frontiers in Neurology, Aug 2022. URL: https://doi.org/10.3389/fneur.2022.907228, doi:10.3389/fneur.2022.907228. This article has 18 citations and is from a peer-reviewed journal.

6. (silva2017photosensitivityandepilepsy pages 10-12): A. Martins da Silva and Bárbara Leal. Photosensitivity and epilepsy: current concepts and perspectives—a narrative review. Seizure, 50:209-218, Aug 2017. URL: https://doi.org/10.1016/j.seizure.2017.04.001, doi:10.1016/j.seizure.2017.04.001. This article has 148 citations.

7. (silva2017photosensitivityandepilepsy pages 1-3): A. Martins da Silva and Bárbara Leal. Photosensitivity and epilepsy: current concepts and perspectives—a narrative review. Seizure, 50:209-218, Aug 2017. URL: https://doi.org/10.1016/j.seizure.2017.04.001, doi:10.1016/j.seizure.2017.04.001. This article has 148 citations.

8. (silva2017photosensitivityandepilepsy pages 9-10): A. Martins da Silva and Bárbara Leal. Photosensitivity and epilepsy: current concepts and perspectives—a narrative review. Seizure, 50:209-218, Aug 2017. URL: https://doi.org/10.1016/j.seizure.2017.04.001, doi:10.1016/j.seizure.2017.04.001. This article has 148 citations.

9. (silva2017photosensitivityandepilepsy pages 4-6): A. Martins da Silva and Bárbara Leal. Photosensitivity and epilepsy: current concepts and perspectives—a narrative review. Seizure, 50:209-218, Aug 2017. URL: https://doi.org/10.1016/j.seizure.2017.04.001, doi:10.1016/j.seizure.2017.04.001. This article has 148 citations.

10. (covanis2004treatmentofphotosensitivity pages 1-2): Athanasios Covanis, Stefan R. G. Stodieck, and Arnold J. Wilkins. Treatment of photosensitivity. Epilepsia, 45:40-45, Jan 2004. URL: https://doi.org/10.1111/j.0013-9580.2004.451006.x, doi:10.1111/j.0013-9580.2004.451006.x. This article has 99 citations and is from a domain leading peer-reviewed journal.

11. (silva2017photosensitivityandepilepsy pages 3-4): A. Martins da Silva and Bárbara Leal. Photosensitivity and epilepsy: current concepts and perspectives—a narrative review. Seizure, 50:209-218, Aug 2017. URL: https://doi.org/10.1016/j.seizure.2017.04.001, doi:10.1016/j.seizure.2017.04.001. This article has 148 citations.

12. (covanis2004treatmentofphotosensitivity pages 2-3): Athanasios Covanis, Stefan R. G. Stodieck, and Arnold J. Wilkins. Treatment of photosensitivity. Epilepsia, 45:40-45, Jan 2004. URL: https://doi.org/10.1111/j.0013-9580.2004.451006.x, doi:10.1111/j.0013-9580.2004.451006.x. This article has 99 citations and is from a domain leading peer-reviewed journal.

13. (NCT00579384 chunk 1):  A Study of the Effects of JNJ-26489112 on the Photic Induced Paroxysmal Electroencephalogram (EEG) Response in Patients With Photosensitive Epilepsy. Johnson & Johnson Pharmaceutical Research & Development, L.L.C.. 2007. ClinicalTrials.gov Identifier: NCT00579384

14. (NCT00979004 chunk 1):  A Study to Investigate the Effect of ICA-105665 in Photosensitive Epilepsy Patients. Pfizer. 2009. ClinicalTrials.gov Identifier: NCT00979004

15. (NCT03603639 chunk 1):  A Study to Evaluate the Pharmacodynamic Activity of E2730 in Adult Participants With Photosensitive Epilepsy. Eisai Inc.. 2018. ClinicalTrials.gov Identifier: NCT03603639

16. (NCT00401648 chunk 1):  Effect of Brivaracetam in Photosensitive Epileptic Subjects. UCB Pharma. 2002. ClinicalTrials.gov Identifier: NCT00401648

17. (NCT00784212 chunk 1):  Effect of BGG492 on EEG in Patients With Photosensitive Epilepsy. Novartis Pharmaceuticals. 2008. ClinicalTrials.gov Identifier: NCT00784212

18. (NCT03239691 chunk 1):  A Study to Evaluate the Effect of ACT-709478 in Photosensitive Epilepsy Patients. Idorsia Pharmaceuticals Ltd.. 2017. ClinicalTrials.gov Identifier: NCT03239691

19. (NCT04076410 chunk 2): Ana Checa-Ros, MD, PhD. Efficacy of Lenses in Abolishing Photoparoxysmal Responses. Aston University. 2021. ClinicalTrials.gov Identifier: NCT04076410

20. (NCT03603639 chunk 2):  A Study to Evaluate the Pharmacodynamic Activity of E2730 in Adult Participants With Photosensitive Epilepsy. Eisai Inc.. 2018. ClinicalTrials.gov Identifier: NCT03603639

21. (szabo2021thebaboonin pages 1-2): C. Ákos Szabó and Felipe S. Salinas. The baboon in epilepsy research: revelations and challenges. Aug 2021. URL: https://doi.org/10.1016/j.yebeh.2021.108012, doi:10.1016/j.yebeh.2021.108012. This article has 14 citations and is from a peer-reviewed journal.

22. (szabo2021thebaboonin pages 2-3): C. Ákos Szabó and Felipe S. Salinas. The baboon in epilepsy research: revelations and challenges. Aug 2021. URL: https://doi.org/10.1016/j.yebeh.2021.108012, doi:10.1016/j.yebeh.2021.108012. This article has 14 citations and is from a peer-reviewed journal.

23. (szabo2022neuroimaginginthe pages 1-2): C. Akos Szabo and Felipe S. Salinas. Neuroimaging in the epileptic baboon. Frontiers in Veterinary Science, Jul 2022. URL: https://doi.org/10.3389/fvets.2022.908801, doi:10.3389/fvets.2022.908801. This article has 8 citations and is from a peer-reviewed journal.

24. (szabo2012baboonmodelof pages 1-2): C. Ákos Szabó, Felipe S. Salinas, M. Michelle Leland, Jean-Louis Caron, Martha A. Hanes, Koyle D. Knape, Dongbin Xie, and Jeff T. Williams. Baboon model of generalized epilepsy: continuous intracranial video-eeg monitoring with subdural electrodes. Epilepsy Research, 101:46-55, Aug 2012. URL: https://doi.org/10.1016/j.eplepsyres.2012.02.016, doi:10.1016/j.eplepsyres.2012.02.016. This article has 31 citations and is from a peer-reviewed journal.

25. (szabo2012baboonmodelof pages 8-10): C. Ákos Szabó, Felipe S. Salinas, M. Michelle Leland, Jean-Louis Caron, Martha A. Hanes, Koyle D. Knape, Dongbin Xie, and Jeff T. Williams. Baboon model of generalized epilepsy: continuous intracranial video-eeg monitoring with subdural electrodes. Epilepsy Research, 101:46-55, Aug 2012. URL: https://doi.org/10.1016/j.eplepsyres.2012.02.016, doi:10.1016/j.eplepsyres.2012.02.016. This article has 31 citations and is from a peer-reviewed journal.

26. (silva2017photosensitivityandepilepsy pages 12-13): A. Martins da Silva and Bárbara Leal. Photosensitivity and epilepsy: current concepts and perspectives—a narrative review. Seizure, 50:209-218, Aug 2017. URL: https://doi.org/10.1016/j.seizure.2017.04.001, doi:10.1016/j.seizure.2017.04.001. This article has 148 citations.

27. (szabo2011functionalpetevaluation pages 1-2): C. Ákos Szabó, Felipe S Salinas, and Shalini Narayana. Functional pet evaluation of the photosensitive baboon. The Open Neuroimaging Journal, 5:206-215, Nov 2011. URL: https://doi.org/10.2174/1874440001105010206, doi:10.2174/1874440001105010206. This article has 18 citations.

## Artifacts

- [Edison artifact artifact-00](Photosensitive_Occipital_Lobe_Epilepsy-deep-research-falcon_artifacts/artifact-00.md)