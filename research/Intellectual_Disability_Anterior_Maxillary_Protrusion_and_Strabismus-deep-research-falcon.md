---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T20:17:37.743732'
end_time: '2026-07-31T20:27:39.905700'
duration_seconds: 602.16
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Intellectual Disability, Anterior Maxillary Protrusion, and Strabismus
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 11
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Intellectual_Disability_Anterior_Maxillary_Protrusion_and_Strabismus-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Disability, Anterior Maxillary Protrusion, and Strabismus
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability, Anterior Maxillary Protrusion, and Strabismus** covering all of the
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
- **Disease Name:** Intellectual Disability, Anterior Maxillary Protrusion, and Strabismus
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability, Anterior Maxillary Protrusion, and Strabismus** covering all of the
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


# Comprehensive disease-characteristics report

## Executive summary and evidence status

**Intellectual disability, anterior maxillary protrusion, and strabismus** is an ultra-rare, autosomal-recessive neurodevelopmental syndrome caused by biallelic germline variants in **SOBP** (*sine oculis binding protein homolog*). It has also been called **mental retardation, anterior maxillary protrusion, and strabismus (MRAMS) syndrome**. The defining manifestations are developmental/intellectual impairment, characteristic maxillary or craniofacial dysmorphism, and strabismus. Curated resources map the disorder to **MONDO:0013353** and uniquely associate it with SOBP (**Ensembl ENSG00000112320**), citing the foundational human reports PMID **17618476** and PMID **21035105** (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus).

The principal limitation is the extraordinarily small evidence base. No disease-specific 2023–2024 human cohort, registry, natural-history study, prevalence estimate, diagnostic guideline, biomarker study, treatment trial, or multi-omics investigation was identified. Accordingly, numerical frequencies from the original kindred must not be interpreted as population estimates. Recent work has primarily refined **preclinical SOBP biology**, especially its participation in SIX1/EYA1-dependent craniofacial and sensory-organ development (neal2024usingxenopusto pages 9-11).

The following table provides a compact knowledge-base abstraction; the narrative afterward distinguishes direct human evidence from model-based inference.

| Domain | Curated finding | Suggested ontology/identifier | Evidence level/limitations |
|---|---|---|---|
| Disease entity | Ultra-rare Mendelian neurodevelopmental syndrome recorded as **intellectual disability, anterior maxillary protrusion, and strabismus** | **MONDO:0013353** | Disease identity supported by curated disease-target mapping; literature base is very small and largely historical (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus) |
| Source type | Evidence is derived from **aggregated disease-level curation** linked to a very small number of published human families/cases, not from EHR-scale cohorts | MONDO disease record; Open Targets disease-target association | No modern registry, cohort, or natural-history dataset identified (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus) |
| Causal gene | The disorder is linked to **SOBP** (*sine oculis binding protein homolog*) | **SOBP**; **ENSG00000112320** | Unique disease-target association found; foundational literature cited in the disease-target resource includes PMIDs **17618476** and **21035105** (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus) |
| Inheritance | **Autosomal recessive** disorder caused by **germline** biallelic pathogenic variation in **SOBP** | Suggested term: autosomal recessive inheritance | Direct disease-specific human evidence is sparse; inheritance assignment is based on curated disease-gene linkage and legacy syndrome descriptions (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus) |
| Variant/mechanism class | Human syndrome is associated with **loss/truncation** of SOBP; model and review evidence indicate **truncated proteins lacking the C-terminal nuclear localization signal** can impair nuclear localization | Suggested terms: loss of function; protein truncation; impaired nuclear localization | Strong mechanistic support from model/review synthesis, but detailed human variant spectrum is not recoverable from the presently available full text in this tool session (neal2024usingxenopusto pages 9-11, chen2008jxc1sobpencodinga pages 3-4, chen2008jxc1sobpencodinga pages 1-2) |
| Core phenotype: cognition | **Intellectual disability / developmental delay** is a core feature | Suggested HPO terms: Intellectual disability; Global developmental delay | Core phenotype consistently referenced in disease naming and syndrome summaries; precise severity/frequency not established from current accessible primary text (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus, neal2024usingxenopusto pages 9-11) |
| Core phenotype: craniofacial | **Anterior maxillary protrusion** and broader **craniofacial dysmorphism** are defining features | Suggested HPO term: Anterior maxillary protrusion; suggested broader term: Abnormal facial shape | Syndrome-defining feature in the disease label; recent review-level model synthesis notes craniofacial abnormalities in all affected individuals discussed there, but exact human denominator is limited (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus, neal2024usingxenopusto pages 9-11) |
| Core phenotype: ocular | **Strabismus** is a defining ocular phenotype | Suggested HPO term: Strabismus | Ocular association is part of the disease name and included in a 2025 review of strabismus across genetic syndromes; detailed subtype/frequency remains unclear from currently accessible text (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus, kilic2025strabismusingenetic pages 24-26) |
| Additional phenotype | **Possible hearing loss** may occur in some affected individuals | Suggested HPO term: Hearing impairment | Evidence appears limited/inconsistent; a recent review excerpt states hearing loss occurred in **one patient** in a human MRAMS-context summary, so this should be treated as possible rather than universal (neal2024usingxenopusto pages 9-11) |
| Molecular function | SOBP encodes a **nuclear zinc-finger protein** involved in developmental transcriptional regulation | Suggested GO terms: nucleus; DNA-binding/transcriptional regulation-related functions | Directly supported in mouse work showing nuclear localization and developmental roles; extrapolation to human neurocognitive phenotype remains inferential (chen2008jxc1sobpencodinga pages 3-4, chen2008jxc1sobpencodinga pages 1-2) |
| Pathophysiology | Current working model: **germline truncating/loss-of-function SOBP variants → impaired nuclear localization / altered transcriptional cofactor activity → abnormal craniofacial, sensory, and neurodevelopmental patterning → syndromic phenotype** | Suggested GO/process names: craniofacial development; sensory organ development; regulation of transcription | Causal chain is biologically plausible and supported by animal/cellular evidence, but not fully demonstrated in human patient tissues (neal2024usingxenopusto pages 9-11, chen2008jxc1sobpencodinga pages 3-4, chen2008jxc1sobpencodinga pages 1-2, chen2008jxc1sobpencodinga pages 5-7) |
| Pathway/cofactor biology | Xenopus/review evidence indicates **SOBP binds Six1 directly** and also **binds Eya1**, modulating Six1-dependent transcription and affecting craniofacial/otic development | Suggested pathway names: Six1/Eya1 developmental transcriptional network | Mechanistic evidence is preclinical and should not be overinterpreted as fully established human disease mechanism (neal2024usingxenopusto pages 9-11) |
| Anatomy affected | Primary systems implicated: **central nervous system/development**, **craniofacial structures (maxilla/facial skeleton/cartilage)**, **ocular alignment pathways**, and possibly **inner ear/auditory system** | Suggested anatomy terms: maxilla; eye; brain; inner ear | Human anatomic resolution is limited; several assignments rely partly on model data and syndrome naming (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus, neal2024usingxenopusto pages 9-11, chen2008jxc1sobpencodinga pages 1-2, chen2008jxc1sobpencodinga pages 5-7) |
| Mouse model | **Jxc1/Sobp** mutant mice show **deafness**, **shortened cochlea**, disrupted **organ of Corti patterning**, supernumerary/ectopic hair cells, and mutant protein mislocalization from nucleus toward cytoplasm | Suggested model identifier: mouse *Sobp* / *Jxc1* mutant | Strong primary experimental evidence for ear-development roles; does **not** directly model the full human intellectual-disability/strabismus phenotype (chen2008jxc1sobpencodinga pages 3-4, chen2008jxc1sobpencodinga pages 1-2, chen2008jxc1sobpencodinga pages 5-7) |
| Xenopus model | **sobp** knockdown disrupts **otic vesicle** and **craniofacial cartilage** development; expression overlaps Six1 in neural tube, placodal progenitor epithelium, and otic vesicle | Suggested model: *Xenopus* sobp loss-of-function | Useful for developmental mechanism and tissue specificity; cognitive and ocular alignment phenotypes are not directly modeled (neal2024usingxenopusto pages 9-11, neal2024usingxenopusto pages 36-37) |
| Diagnostics | Practical diagnosis is currently **genetics-led**, with consideration of **exome/genome sequencing** or neurodevelopmental/intellectual-disability panels that include **SOBP** when phenotype is compatible | Suggested test identifiers: SOBP sequence analysis; WES/WGS | No disease-specific diagnostic guideline, biomarker, or standardized criteria document identified in 2023–2024 sources (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus) |
| Biomarkers | **No validated disease-specific biomarkers identified** | None established | No biomarker studies found (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus) |
| Epidemiology | **No reliable prevalence or incidence estimates identified** | None established | Too few reported patients/families; no registry or epidemiologic study found (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus) |
| Natural history | **No formal natural-history study identified** | None established | Onset is likely developmental/congenital or early childhood based on syndrome features, but longitudinal course data are lacking (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus) |
| Prognosis | **Insufficient disease-specific prognosis data**; morbidity likely dominated by neurodevelopmental impairment and treatable sensory/craniofacial manifestations | None established | No survival, life-expectancy, or prognostic biomarker studies located (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus) |
| Treatment | **No disease-specific therapy identified**; management is expected to be **supportive and phenotype-directed** (developmental services, ophthalmology/strabismus care, audiology if indicated, craniofacial/dental assessment) | Suggested NCIT intervention names: supportive care; physical therapy; occupational therapy; speech therapy; strabismus surgery | Supportive approach is inferred from standard care for syndromic neurodevelopmental disorders; no SOBP-specific interventional study located (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus, kilic2025strabismusingenetic pages 24-26) |
| Clinical trials | **No disease-specific clinical trials identified** | None | Dedicated trial search was negative (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus) |
| Prevention/genetic counseling | Because inheritance is **autosomal recessive**, **genetic counseling**, carrier testing in relatives, and reproductive counseling are relevant once familial variants are known | Suggested terms: genetic counseling; carrier testing | General Mendelian best practice; no disease-specific prevention program or screening guideline found (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus) |


*Table: This table condenses the currently retrievable disease-knowledge-base facts for intellectual disability, anterior maxillary protrusion, and strabismus. It emphasizes the confirmed SOBP/MONDO linkage, core phenotypes, model-organism mechanism data, and major evidence gaps such as absent epidemiology, biomarkers, trials, and disease-specific therapy.*

## 1. Disease information

### Definition and identifiers

- **Preferred name:** Intellectual disability, anterior maxillary protrusion, and strabismus.
- **MONDO:** **MONDO:0013353**.
- **OMIM:** Commonly catalogued as **MRAMS syndrome, OMIM #613671**; this identifier should be verified against the live OMIM record before production ingestion because the present retrieval tool did not return the OMIM page itself.
- **Causal gene:** **SOBP**, *sine oculis binding protein homolog*; Ensembl **ENSG00000112320**. The disease–target association is supported by the original linkage and mutation literature, PMIDs 17618476 and 21035105 (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus).
- **Synonyms:** MRAMS syndrome; mental retardation–anterior maxillary protrusion–strabismus syndrome; SOBP-related intellectual-developmental disorder. “Mental retardation” is retained only as a historical indexing term.
- **Orphanet/MeSH:** No disorder-specific identifier was verified in the retrieved evidence. It may be represented under broader rare intellectual-disability or dysmorphism concepts.
- **ICD-10/ICD-11:** No specific code exists in the evidence reviewed. Clinical coding would use broader intellectual-developmental-disorder, strabismus, and congenital craniofacial-abnormality codes.

This entry is based on **aggregated disease-level curation and a very small number of published related individuals**, not EHR-scale individual-patient data (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus).

## 2. Etiology, risk factors, and protective factors

The established cause is **biallelic germline SOBP dysfunction**, inherited in an autosomal-recessive manner. Available experimental synthesis indicates that human and murine disease alleles can produce truncated proteins lacking a C-terminal nuclear-localization signal, thereby compromising normal nuclear localization and developmental transcriptional regulation (neal2024usingxenopusto pages 9-11, chen2008jxc1sobpencodinga pages 3-4).

No reproducible susceptibility loci, modifier genes, protective alleles, environmental causes, infectious triggers, toxins, lifestyle risks, or gene–environment interactions have been demonstrated. Consanguinity increases the probability that two carriers of the same rare recessive allele will have an affected child, but it is a reproductive-genetic circumstance rather than a molecular cause. For two confirmed heterozygous parents, the standard per-pregnancy risks are 25% affected, 50% carrier, and 25% unaffected/non-carrier.

## 3. Phenotypes

### Core human manifestations

1. **Intellectual disability/developmental delay** — a neurodevelopmental symptom and defining feature. Onset is developmental, ordinarily recognized in infancy or childhood. Severity, language profile, adaptive-function scores, and progression have not been quantified in a modern cohort. Suggested HPO terms: **Intellectual disability (HP:0001249)** and, where documented, **Global developmental delay (HP:0001263)**.
2. **Anterior maxillary protrusion** — a congenital/developmental craniofacial sign. Suggested HPO annotation: *Anterior maxillary protrusion*; broader fallback terms include **Abnormality of the maxilla** and **Abnormal facial shape (HP:0001999)**. Quantitative cephalometric data are unavailable.
3. **Strabismus** — an ocular-motor sign and defining feature; suggested **Strabismus (HP:0000486)**. Available records do not reliably specify esotropia versus exotropia, comitance, laterality, amblyopia, stereopsis, or surgical history. This is a recognized general limitation in genetic-syndrome literature: “strabismus” is often reported without direction, comitance, amblyopia, or stereopsis, making syndrome-specific frequency and mechanism difficult to estimate (ye2020towardstheidentification pages 103-108).
4. **Craniofacial dysmorphism** — broader facial abnormalities were reported in affected individuals summarized by recent developmental literature. Suggested HPO: **Abnormal facial shape (HP:0001999)** (neal2024usingxenopusto pages 9-11).
5. **Hearing impairment** — possible rather than defining. A recent review-level synthesis reports hearing loss in one affected human patient, while experimental models strongly implicate SOBP in inner-ear development. Suggested HPO: **Hearing impairment (HP:0000365)**. It should not be assigned as universal (neal2024usingxenopusto pages 9-11).

No defensible disease-level percentages, standardized behavioral findings, laboratory abnormalities, or quality-of-life scores are available. Functional burden is nevertheless expected from impaired learning/adaptive skills, binocular alignment and possible amblyopia, craniofacial/dental needs, and occasional auditory impairment.

## 4. Genetic and molecular information

### Gene and variant interpretation

**SOBP** encodes a nuclear zinc-finger protein containing two FCS-type zinc-finger domains and nuclear-localization signals. Wild-type murine protein localizes to the nucleus, whereas experimentally studied truncated mutant isoforms show partial cytoplasmic retention (chen2008jxc1sobpencodinga pages 3-4, chen2008jxc1sobpencodinga pages 1-2).

The disease mechanism is most consistent with **biallelic loss of function or severe truncation**. Variants are germline, not somatic. The retrieved evidence did not support a complete clinically curated variant list, exact HGVS nomenclature for every reported human allele, ClinVar review status, or allele frequencies; these fields should therefore be populated directly from the current ClinVar and gnomAD records rather than inferred. Because the syndrome is extremely rare and recessive, a causal allele would ordinarily be expected to be absent or exceptionally rare in population databases, especially in homozygous form.

No validated modifier gene, anticipation, parent-of-origin effect, recurrent chromosomal rearrangement, disease-specific methylation signature, or epigenetic biomarker is known. Large deletions involving 6q may include SOBP but should not automatically be equated with this single-gene recessive syndrome because contiguous-gene effects can produce a different phenotype.

## 5. Environmental and infectious information

No non-genetic environmental, occupational, dietary, smoking, alcohol, radiation, pollutant, or infectious etiology has been established. Vaccination and antimicrobial prophylaxis have no disease-specific preventive role. General prenatal health measures reduce unrelated developmental risks but do not prevent an inherited biallelic SOBP genotype.

## 6. Mechanism and pathophysiology

### Working causal chain

**Biallelic truncating/functional SOBP variation** → reduced functional nuclear SOBP and/or impaired nuclear localization → disturbed developmental transcriptional-cofactor activity, including the **SIX1/EYA1 network** → abnormal craniofacial, placodal/sensory-organ, ocular-alignment, and nervous-system development → maxillary dysmorphism, strabismus, possible hearing impairment, and intellectual disability.

In Xenopus and mouse, SOBP expression overlaps SIX1 in neural tube, placodal progenitor epithelium, and otic vesicle. Experimental evidence indicates that SOBP directly binds Six1 and also binds Eya1, modifies Eya1 nuclear translocation, and reduces Six1-driven reporter activation. Sobp depletion disrupts otic-vesicle and craniofacial-cartilage development (neal2024usingxenopusto pages 9-11). These data support transcriptional dysregulation as an **upstream** mechanism; altered tissue patterning and cell fate are **downstream** consequences. They do not yet demonstrate the complete mechanism in human patient-derived neural cells.

Relevant suggested GO concepts include **nucleus (GO:0005634)**, regulation of DNA-templated transcription, craniofacial development, inner-ear morphogenesis, sensory-organ development, cell-fate specification, and tissue patterning. Relevant cell/tissue concepts include neural progenitor cells, cranial neural-crest derivatives, preplacodal ectoderm, otic epithelial cells, cochlear hair cells, supporting cells, and spiral/acoustic ganglion neurons. Exact CL identifiers should be assigned by ontology lookup rather than guessed.

No disease-specific metabolic, immune, inflammatory, oxidative-stress, autophagy, lipidomic, proteomic, spatial-transcriptomic, patient single-cell, or multi-omics signature has been established.

## 7. Anatomical structures affected

The primary systems are:

- **Central nervous system:** developmental cognitive circuitry; precise brain regions and imaging signatures are unknown.
- **Craniofacial skeleton:** maxilla and related facial/cartilaginous structures.
- **Visual/ocular-motor system:** pathways controlling binocular alignment; the exact extraocular muscle, cranial nerve, or supranuclear lesion is uncharacterized.
- **Auditory system:** possible cochlear involvement based on occasional human hearing loss and strong animal evidence.

Suggested UBERON concepts include brain, maxilla, eye, extraocular muscle, inner ear, cochlea, organ of Corti, craniofacial skeleton, and neural tube. At the subcellular level, the best-supported compartment is the **nucleus**; mutant protein can be abnormally retained in cytoplasm (chen2008jxc1sobpencodinga pages 3-4, chen2008jxc1sobpencodinga pages 1-2). No consistent lateralization is known.

## 8. Temporal development and natural history

The disorder is **congenital/developmental**, with manifestations emerging during craniofacial and nervous-system development and developmental delay recognized in childhood. It is expected to be lifelong. There are no validated stages, remission pattern, progression rate, or longitudinal developmental trajectories. Strabismus and amblyopia have clinically important early-childhood treatment windows, while speech, hearing, and developmental interventions are most useful when initiated promptly; these are general pediatric principles rather than SOBP-specific trial findings.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive.
- **Penetrance:** apparently high for the core syndrome among reported biallelic affected relatives, but cannot be estimated robustly.
- **Expressivity:** insufficiently characterized; hearing loss appears variable (neal2024usingxenopusto pages 9-11).
- **Anticipation:** not expected and not reported.
- **Germline mosaicism:** not documented, although low residual recurrence risk can apply generally after an apparently de novo variant.
- **Founder effect/carrier frequency:** unknown.
- **Consanguinity:** relevant to the original recessive-family ascertainment and recurrence risk, but no population carrier estimate exists.
- **Prevalence/incidence:** unknown; no cases-per-100,000 estimate is defensible.
- **Sex ratio, ethnicity, geography, and age distribution:** not established beyond the small original family literature.

## 10. Diagnostics

### Clinical and genetic approach

There are no standardized syndrome-specific diagnostic criteria or biochemical biomarkers. Diagnosis should combine developmental assessment, dysmorphology examination, ophthalmologic evaluation, and molecular confirmation.

A practical testing sequence is:

1. **Chromosomal microarray** as appropriate for syndromic developmental delay, especially when copy-number variation is suspected.
2. **Trio whole-exome or whole-genome sequencing**, with recessive analysis of SOBP and other neurodevelopmental genes. WGS adds noncoding and structural-variant detection.
3. A comprehensive intellectual-disability/developmental-delay panel containing **SOBP** when exome/genome sequencing is unavailable.
4. Confirm candidate variants by an orthogonal method and test parental segregation.
5. Use deletion/duplication analysis if read-depth data suggest an exon-level or whole-gene event.

Karyotyping and FISH are not first-line for a sequence-level SOBP disorder unless cytogenetic findings are suspected. Mitochondrial-DNA and repeat-expansion testing are phenotype-driven rather than specifically indicated. RNA sequencing may clarify a suspected splice variant, but no validated SOBP transcriptomic diagnostic signature exists.

Recommended phenotyping includes formal developmental/cognitive and adaptive assessment, pediatric ophthalmology with amblyopia evaluation, audiology, dental/orthodontic or craniofacial assessment, and neurological examination. Brain MRI, EEG, or other studies should be symptom-directed because characteristic disease-specific findings are not established.

Differential diagnoses include other recessive syndromic intellectual disabilities with strabismus or dysmorphism, congenital cranial dysinnervation disorders, craniofacial syndromes, and chromosomal disorders. The distinguishing feature is a compatible phenotype plus **biallelic pathogenic/likely pathogenic SOBP variants**.

## 11. Outcome and prognosis

No survival curves, mortality rates, life-expectancy estimates, formal disability outcomes, EQ-5D/SF-36 data, or prognostic biomarkers exist. The available phenotype does not itself establish a life-limiting visceral disorder, but the evidence is too sparse to claim normal life expectancy. Long-term morbidity is likely driven by intellectual/adaptive impairment, communication needs, visual consequences of strabismus/amblyopia, and possible hearing or dental/craniofacial problems. Recovery of the underlying neurodevelopmental disorder is not expected, although functional gains can occur with education, rehabilitation, and correction of treatable sensory deficits.

## 12. Treatment and current applications

There is **no approved SOBP-directed therapy**, gene therapy, RNA therapy, small-molecule treatment, or validated pharmacogenomic strategy. Searches found no disease-specific interventional clinical trial.

Management is multidisciplinary and phenotype-directed:

- early developmental and educational services;
- speech-language, occupational, and physical therapy as indicated;
- behavioral and adaptive support;
- pediatric ophthalmology, refractive correction, amblyopia therapy, prisms where appropriate, and strabismus surgery when clinically indicated;
- baseline and follow-up audiology, with hearing aids or other standard interventions if loss is found;
- dental, orthodontic, oral-maxillofacial, or craniofacial assessment for functional maxillary abnormalities;
- neurology and seizure evaluation only when clinically indicated;
- social-work support and individualized educational planning.

Suggested NCIT intervention concepts include **Supportive Care**, **Speech Therapy**, **Occupational Therapy**, **Physical Therapy**, **Hearing Aid**, and **Strabismus Surgery**. No disease-specific response rates or adverse-event statistics are available.

## 13. Prevention

Primary prevention by lifestyle modification is not possible for a biallelic inherited genotype. Relevant measures are reproductive and secondary/tertiary prevention:

- genetic counseling and parental carrier confirmation;
- cascade testing of at-risk adult relatives after identification of the familial variants;
- prenatal diagnosis by chorionic-villus sampling or amniocentesis;
- preimplantation genetic testing for monogenic disease where desired and legally available;
- early developmental, visual, and hearing surveillance to prevent avoidable secondary disability, particularly amblyopia and delayed language access.

Population newborn or carrier screening is not presently supported because prevalence, variant spectrum, and clinical utility have not been established.

## 14. Other species and natural disease

No naturally occurring veterinary syndrome equivalent to human MRAMS was identified. There is no zoonotic or cross-species transmission because this is an inherited genetic disorder.

Orthologous Sobp genes are evolutionarily conserved in vertebrates. Mouse and Xenopus experiments show conserved roles in craniofacial and sensory-organ development; human and Xenopus proteins have been reported as highly similar in recent review synthesis (neal2024usingxenopusto pages 9-11). Relevant taxa are **Mus musculus** (NCBI Taxon **10090**) and **Xenopus** species, commonly *X. laevis* (Taxon **8355**) or *X. tropicalis* (Taxon **8364**), depending on the experiment.

## 15. Model organisms and advanced experimental evidence

### Mouse Jxc1/Sobp model — primary experimental evidence

Recessive **Jxc1/Sobp** mutant mice develop deafness caused by cochlear developmental arrest. Wild-type Jxc1/Sobp localizes to nuclei; mutant isoforms are partially retained in cytoplasm. In homozygotes, cochlear-duct length was reduced by **28%**, with premature growth arrest, supernumerary outer hair-cell rows, ectopic inner hair cells, and mirror-image organ-of-Corti duplications (chen2008jxc1sobpencodinga pages 3-4). Ectopic vestibular-like hair-cell patches averaged **7 ± 0.8 per cochlea** (chen2008jxc1sobpencodinga pages 5-7).

SOBP/Jxc1 is expressed in sensory hair cells, supporting cells, spiral/acoustic ganglia, developing retina, olfactory epithelium, trigeminal ganglion, and hair follicles. Absence from the early E9.5 otocyst, followed by later sensory-epithelium expression, suggests action after initial inner-ear specification, in growth, cell-fate determination, and patterning (chen2008jxc1sobpencodinga pages 1-2, chen2008jxc1sobpencodinga pages 5-7).

A representative primary-study conclusion is captured by its title: **“Jxc1/Sobp, Encoding a Nuclear Zinc Finger Protein, Is Critical for Cochlear Growth, Cell Fate, and Patterning of the Organ of Corti.”** Chen et al., *Journal of Neuroscience*, published June 2008; DOI: https://doi.org/10.1523/JNEUROSCI.1280-08.2008 (chen2008jxc1sobpencodinga pages 3-4).

### Xenopus model — developmental and functional evidence

Sobp is expressed in neural tube, placodal progenitor epithelium, and otic vesicle. Knockdown disrupts otic-vesicle and craniofacial-cartilage development, while biochemical assays support interactions with Six1 and Eya1 and altered Six1-dependent transcription (neal2024usingxenopusto pages 9-11). This model is well suited to studying placodal, cranial-neural-crest, cartilage, and transcriptional mechanisms.

A 2024 review summarized the conservation and translational rationale: SOBP expression overlaps Six1; mouse and human truncations remove the C-terminal nuclear-localization signal; and Xenopus depletion produces otic and craniofacial defects (neal2024usingxenopusto pages 9-11). Neal et al., *Journal of Experimental Zoology Part B*, published October 2024; DOI: https://doi.org/10.1002/jez.b.23222.

### Model limitations

Neither model fully validates the human intellectual-disability mechanism, the precise neural substrate of strabismus, penetrance, or treatment response. Mouse cochlear phenotypes are strong evidence for sensory-organ biology but not proof that hearing loss is universal in humans. Xenopus craniofacial and reporter assays establish developmental plausibility but cannot substitute for patient-derived neural or craniofacial cells. No disease-specific human iPSC, cerebral organoid, single-cell, spatial-transcriptomic, CRISPR-rescue, proteomic, metabolomic, or multi-omic model was identified.

## Current expert interpretation and research priorities

The most defensible contemporary interpretation is that MRAMS is a **SOBP dosage/function disorder of developmental transcriptional regulation**, with its craniofacial and sensory manifestations plausibly arising from disruption of SIX1/EYA1-associated developmental programs. The strongest mechanistic evidence concerns nuclear localization, cochlear cell fate and patterning, and craniofacial/otic development—not the detailed human cognitive phenotype (neal2024usingxenopusto pages 9-11, chen2008jxc1sobpencodinga pages 3-4, chen2008jxc1sobpencodinga pages 1-2).

Priority research needs are: international case aggregation; standardized HPO phenotyping; publication of exact variants and segregation data; gnomAD/ClinVar reconciliation; longitudinal cognitive, ophthalmologic, audiologic, and craniofacial follow-up; patient-derived iPSC neural and cranial-neural-crest models; transcriptomic definition of SOBP-regulated networks; and rescue experiments to determine whether disease alleles cause null, hypomorphic, or context-dependent dominant-negative effects.

## Key source record

- Foundational human disease literature: **PMID 17618476** and **PMID 21035105**, linked by the curated SOBP–MONDO:0013353 association (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus).
- Chen Z et al. “Jxc1/Sobp, Encoding a Nuclear Zinc Finger Protein, Is Critical for Cochlear Growth, Cell Fate, and Patterning of the Organ of Corti.” *J Neurosci.* June 2008. https://doi.org/10.1523/JNEUROSCI.1280-08.2008 (chen2008jxc1sobpencodinga pages 3-4, chen2008jxc1sobpencodinga pages 1-2).
- Neal SJ et al. “Using Xenopus to discover new candidate genes involved in BOR and other congenital hearing loss syndromes.” *J Exp Zool B Mol Dev Evol.* October 2024. https://doi.org/10.1002/jez.b.23222 (neal2024usingxenopusto pages 9-11).

**Curation caution:** claims for which no direct disease-specific human evidence was retrieved—especially exact phenotype frequencies, prevalence, prognosis, and treatment effectiveness—should remain explicitly marked **unknown**, rather than extrapolated from general intellectual-disability care or animal models.

References

1. (OpenTargets Search: Intellectual disability, anterior maxillary protrusion, and strabismus): Open Targets Query (Intellectual disability, anterior maxillary protrusion, and strabismus, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (neal2024usingxenopusto pages 9-11): Scott J. Neal, Anindita Rajasekaran, Nisveta Jusić, Louis Taylor, Mai Read, Dominique Alfandari, Francesca Pignoni, and Sally A. Moody. Using xenopus to discover new candidate genes involved in bor and other congenital hearing loss syndromes. Journal of experimental zoology. Part B, Molecular and developmental evolution, 342:212-240, Oct 2024. URL: https://doi.org/10.1002/jez.b.23222, doi:10.1002/jez.b.23222. This article has 8 citations.

3. (chen2008jxc1sobpencodinga pages 3-4): Z. Chen, M. Montcouquiol, R. Calderon, N. A. Jenkins, N. G. Copeland, M. W. Kelley, and K. Noben-Trauth. Jxc1/sobp, encoding a nuclear zinc finger protein, is critical for cochlear growth, cell fate, and patterning of the organ of corti. The Journal of Neuroscience, 28:6633-6641, Jun 2008. URL: https://doi.org/10.1523/jneurosci.1280-08.2008, doi:10.1523/jneurosci.1280-08.2008. This article has 39 citations.

4. (chen2008jxc1sobpencodinga pages 1-2): Z. Chen, M. Montcouquiol, R. Calderon, N. A. Jenkins, N. G. Copeland, M. W. Kelley, and K. Noben-Trauth. Jxc1/sobp, encoding a nuclear zinc finger protein, is critical for cochlear growth, cell fate, and patterning of the organ of corti. The Journal of Neuroscience, 28:6633-6641, Jun 2008. URL: https://doi.org/10.1523/jneurosci.1280-08.2008, doi:10.1523/jneurosci.1280-08.2008. This article has 39 citations.

5. (kilic2025strabismusingenetic pages 24-26): Seyda Kilic, Jillian Bove, Bethany Nahri So, and Mary C. Whitman. Strabismus in genetic syndromes: a review. Clinical & Experimental Ophthalmology, Feb 2025. URL: https://doi.org/10.1111/ceo.14507, doi:10.1111/ceo.14507. This article has 4 citations and is from a peer-reviewed journal.

6. (chen2008jxc1sobpencodinga pages 5-7): Z. Chen, M. Montcouquiol, R. Calderon, N. A. Jenkins, N. G. Copeland, M. W. Kelley, and K. Noben-Trauth. Jxc1/sobp, encoding a nuclear zinc finger protein, is critical for cochlear growth, cell fate, and patterning of the organ of corti. The Journal of Neuroscience, 28:6633-6641, Jun 2008. URL: https://doi.org/10.1523/jneurosci.1280-08.2008, doi:10.1523/jneurosci.1280-08.2008. This article has 39 citations.

7. (neal2024usingxenopusto pages 36-37): Scott J. Neal, Anindita Rajasekaran, Nisveta Jusić, Louis Taylor, Mai Read, Dominique Alfandari, Francesca Pignoni, and Sally A. Moody. Using xenopus to discover new candidate genes involved in bor and other congenital hearing loss syndromes. Journal of experimental zoology. Part B, Molecular and developmental evolution, 342:212-240, Oct 2024. URL: https://doi.org/10.1002/jez.b.23222, doi:10.1002/jez.b.23222. This article has 8 citations.

8. (ye2020towardstheidentification pages 103-108): Xin Ye. Towards the identification of causal genes and contributing molecular processes underlying strabismus. ArXiv, Jan 2020. URL: https://doi.org/10.14288/1.0379323, doi:10.14288/1.0379323. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Intellectual_Disability_Anterior_Maxillary_Protrusion_and_Strabismus-deep-research-falcon_artifacts/artifact-00.md)