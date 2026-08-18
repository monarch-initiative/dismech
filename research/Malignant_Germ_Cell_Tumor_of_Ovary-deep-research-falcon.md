---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T23:33:04.468182'
end_time: '2026-07-31T23:41:55.749609'
duration_seconds: 531.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Malignant Germ Cell Tumor of Ovary
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Malignant_Germ_Cell_Tumor_of_Ovary-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Malignant Germ Cell Tumor of Ovary
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Malignant Germ Cell Tumor of Ovary** covering all of the
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
- **Disease Name:** Malignant Germ Cell Tumor of Ovary
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Malignant Germ Cell Tumor of Ovary** covering all of the
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


# Malignant Germ Cell Tumor of the Ovary: Disease-Characteristics Report

## Executive summary

Malignant ovarian germ-cell tumors (MOGCTs) are a heterogeneous group of rare, rapidly growing neoplasms derived from primordial germ-cell lineages. They predominantly affect children, adolescents, and young adults, most often presenting with acute or subacute abdominal pain and a rapidly enlarging adnexal mass. Major histologies are dysgerminoma, yolk-sac tumor (YST), immature teratoma, mixed germ-cell tumor, embryonal carcinoma, and nongestational choriocarcinoma. Unlike epithelial ovarian cancers, MOGCTs usually have a low point-mutation burden but marked chromosomal, imprinting, and DNA-methylation abnormalities. Fertility-sparing surgery and platinum-based chemotherapy cure most newly diagnosed patients; recurrent, platinum-resistant YST is the principal unmet clinical need. (pinto2023molecularbiologyof pages 4-6, saani2023clinicalchallengesin pages 2-3, pinto2023molecularbiologyof pages 1-3, pinto2023molecularbiologyof pages 16-18)

The following matrix summarizes the most transferable evidence.

| Domain | Key quantitative findings | Practical interpretation | Evidence type and date |
|---|---|---|---|
| Disease definition / epidemiology | Malignant ovarian germ cell tumors (MOGCTs) are rare, comprising 2–5% of ovarian cancers; annual incidence reported as 4:100,000 and approximately 4 per 1,000,000 women; most occur at ages 10–25 years with median diagnosis age 18; 60–70% present as early-stage disease; common symptoms are abdominal pain (87%) and palpable mass (85%) (saani2023clinicalchallengesin pages 1-2, saani2023clinicalchallengesin pages 2-3, saani2023clinicalchallengesin pages 5-6) | Rare, usually adolescent/young-adult ovarian cancers that often present early but require rapid evaluation because symptoms are nonspecific | Human clinical review, 2023; review with compiled epidemiology, 2023 |
| Major subtypes | Dysgerminoma accounts for 35–50% globally; dysgerminoma and immature teratoma together comprise 65–70% of cases; yolk sac tumor (YST) 14.5%; mixed germ cell tumors 5.3%; embryonal carcinoma ~4%; bilateral disease occurs in 10–15% of pure dysgerminomas and 5–10% of mixed tumors (saani2023clinicalchallengesin pages 2-3, pinto2023molecularbiologyof pages 4-6) | Histology strongly determines marker use, surgical decisions, and adjuvant chemotherapy needs | Human clinical and molecular reviews, 2023 |
| Biomarkers | AFP is elevated in YST and can be elevated in embryonal carcinoma/immature teratoma; β-hCG is associated with choriocarcinoma and some embryonal carcinomas; LDH is used in dysgerminoma; in a 2024 pelvic YST series, AFP rose in all 16/16 and CA125 increased in 58.33% (7/12); YST ultrasound series showed 81.25% ovarian location (13/16) with rich vascularity in solid/cystic-solid lesions (saani2023clinicalchallengesin pages 2-3, saani2023clinicalchallengesin pages 3-5) | AFP/β-hCG/LDH remain the core clinical markers; imaging plus markers helps distinguish subtype and guide fertility-preserving planning | Human clinical review, 2023; single-center retrospective imaging/pathology study, 2024 |
| Genomics / epigenetics | Overall mutation burden is low; chromosome 12p gain is a keystone feature, observed in 44% (15/34) of malignant GCTs in one series and in 10/14 tumors in patients <15 years in another summary; KIT was the most significantly mutated gene with 4/24 cases (16.7%) in a genetic landscape study; PIK3CA amplification occurred in 21.8% (19/87) and AKT amplification in 20.6% (18/87); pediatric cohort copy-number gains included 20q (57%) and 12p (39%), with 40% of the 12p-gain group carrying i(12p); dysgerminomas/germinomas are globally hypomethylated, while more differentiated tumors such as YST are relatively hypermethylated; 8,481 differentially methylated regions were identified in one pediatric cohort; miR-371~373 and miR-302 clusters are recurrently overexpressed across malignant GCTs (pinto2023molecularbiologyof pages 9-11, pinto2023molecularbiologyof pages 11-12, pinto2023molecularbiologyof pages 12-13) | Biology is driven more by copy-number/epigenetic dysregulation than high mutational burden; KIT/RAS/PI3K and methylation states are the main molecular leads for stratification and research | Human molecular review synthesizing genomic/epigenetic studies, 2023 |
| Standard treatment | Stage IA dysgerminoma and grade 1 stage IA immature teratoma: unilateral salpingo-oophorectomy (USO) with surveillance; higher-risk stage I disease often receives 3–4 cycles BEP; stages II–IV generally receive surgery plus 3–4 cycles BEP, with EP considered in older patients; stage IA pure dysgerminoma has a surgery-only recurrence rate of 15–25%; BEP doses summarized as bleomycin 30 IU, cisplatin 20 mg/m² days 1–5, etoposide 100 mg/m² days 1–5 every 3 weeks for 3–4 cycles; ongoing phase III MOGCT-01 randomizes paclitaxel/carboplatin vs BEP, planned enrollment 129 (saani2023clinicalchallengesin pages 5-6, pinto2023molecularbiologyof pages 6-7, saani2023clinicalchallengesin pages 6-8, NCT02429687 chunk 1) | Fertility-sparing surgery is standard whenever feasible; BEP remains the backbone, but de-escalation/substitution strategies are under active testing to reduce toxicity | Human clinical reviews, 2023; ClinicalTrials.gov registry updated 2023 |
| Prognosis / fertility | Early-stage survival reported as 82–100% and late-stage survival as 75%; stage I disease has about 90% long-term disease-free survival; in one long follow-up fertility-preservation cohort, 42/45 women achieved pregnancy, with 65 pregnancies and 56 births among 40 survivors; another cohort had 31/39 patients with 33 uneventful pregnancies; 75.6% maintained regular menstruation after treatment; published pregnancy rates range 18.8–55.7% (saani2023clinicalchallengesin pages 3-5, saani2023clinicalchallengesin pages 5-6) | Cure rates are high and post-treatment fertility is often preserved, supporting conservative surgery and survivorship counseling | Human clinical review summarizing cohort studies, 2023 |
| Relapse / current research | Recurrences commonly occur within 2 years and often involve peritoneal/retroperitoneal lymph nodes; more than 50% of relapsed YST patients die of disease; salvage regimens include TIP, VeIP, and TI-CE with stem-cell support; targeted agents such as everolimus, imatinib, sunitinib, and pazopanib showed reported response rates of 0–13%; brentuximab vedotin produced responses in 2/9 patients (22%); accelerated BEP is under phase III evaluation in GCTs (NCT02582697) and ovarian-specific MOGCT-01 compares paclitaxel/carboplatin with BEP (saani2023clinicalchallengesin pages 6-8, saani2023clinicalchallengesin pages 8-9, pinto2023molecularbiologyof pages 16-18, NCT02429687 chunk 1) | Relapse remains the main unmet need; current research focuses on optimizing salvage chemotherapy and testing lower-toxicity or targeted/immunologic approaches, but evidence is still limited | Human clinical and molecular reviews, 2023; clinical trial registry updated 2023 |
| Models | Ovarian-specific models remain scarce; NOY1/NOY2 were the first ovarian YST cell lines; cisplatin-resistant NOY1-CR became 22.3-fold more cisplatin-resistant than parent cells; GSTA1 overexpression was linked to resistance and its inhibition restored cisplatin sensitivity; TC587 is a YST line expressing AFP and SALL4 with NRAS, KIT, KMT2C, RSF1, and TP53 mutations; NOY1-CR formed larger mouse xenografts and showed CAM micrometastasis; a pediatric ovarian YST PDX treated with bleomycin/etoposide/cisplatin mirrored clinical response; the review states no established dedicated ovarian GCT PDX platform was yet available broadly (pinto2023molecularbiologyof pages 13-15, pinto2023molecularbiologyof pages 15-16) | Preclinical work is possible but limited by model scarcity; current models are strongest for studying cisplatin resistance and candidate targeted therapies in YST | In vitro/in vivo model review, 2023 |


*Table: Compact evidence matrix summarizing the highest-yield disease, molecular, diagnostic, treatment, prognosis, relapse, and model findings for malignant ovarian germ cell tumors. It is useful for quickly transferring supported facts into a disease knowledge-base entry.*

## 1. Disease information

### Definition and classification

MOGCT is an umbrella disease category rather than one molecularly uniform cancer. It comprises malignant neoplasms showing germinoma-like, extraembryonic, embryonal, or somatic differentiation:

* **Dysgerminoma**—ovarian counterpart of testicular seminoma.
* **Yolk-sac tumor/endodermal sinus tumor**.
* **Immature teratoma**, graded by the amount of immature neuroepithelium.
* **Mixed germ-cell tumor** containing two or more malignant components.
* **Embryonal carcinoma** and **nongestational choriocarcinoma**, both very rare.
* Gonadoblastoma is a precursor/mixed lesion arising especially in dysgenetic gonads and can be overgrown by dysgerminoma.

Dysgerminoma and immature teratoma together account for approximately 65–70% of cases; YST accounts for about 14.5%, mixed tumors 5.3%, and embryonal carcinoma approximately 4%. Dysgerminoma alone represents roughly 35–50% of MOGCTs. (pinto2023molecularbiologyof pages 4-6, saani2023clinicalchallengesin pages 3-5, saani2023clinicalchallengesin pages 2-3)

A useful verbatim summary from the 2023 molecular review is: **“OGCTs are rare tumors … [and] occur predominantly in children, adolescents, and young adults.”** The same review stresses that few ovarian-specific molecular studies exist. (pinto2023molecularbiologyof pages 1-3)

### Identifiers and synonyms

* **Preferred label:** malignant ovarian germ cell tumor; malignant germ cell tumor of ovary.
* **Synonyms:** ovarian germ-cell cancer, malignant ovarian germ-cell neoplasm, MOGCT, malignant OGCT.
* **MeSH:** *Ovarian Germ Cell Cancer*, MeSH supplementary concept **C562841**; broader term *Ovarian Neoplasms*, **D010051**. (NCT02429687 chunk 1, NCT02429687 chunk 2)
* **ICD-10-CM:** generally coded by site as **C56.-, malignant neoplasm of ovary**; morphology requires an oncology morphology system such as ICD-O-3.
* **ICD-O-3:** histology-specific morphology codes should be used—for example, dysgerminoma, yolk-sac tumor, immature teratoma, or mixed germ-cell tumor—together with ovarian topography C56.9.
* **MONDO/Orphanet/OMIM:** a single umbrella identifier was not verified in the retrieved primary literature. The individual histologies may have separate ontology entries. Curators should resolve the current MONDO and Orphanet release rather than assign an unverified identifier. OMIM is not the primary classification system for this mostly somatic cancer.

The report synthesizes **aggregated disease-level literature and trial records**, not individual EHR data. Some cited cohorts were retrospective patient-level studies, but no identifiable patient record was accessed.

## 2. Etiology, risk, and protective factors

### Causal framework

Most cases are sporadic. The best-supported model is aberrant transformation of a primordial germ cell or oocyte-lineage cell during germ-cell specification, migration, gonadal colonization, meiosis, or epigenetic reprogramming. Pluripotency programs involving **POU5F1/OCT3/4, NANOG, SOX2/SOX17, PRDM1, and PRDM14** remain active; subsequent copy-number changes, KIT–RAS signaling, lineage-specific methylation, and differentiation state determine histology. Immature teratomas appear particularly related to meiotic error and parthenogenetic/oocyte-like development rather than recurrent somatic driver mutations. (pinto2023molecularbiologyof pages 4-6, saani2023clinicalchallengesin pages 8-9)

### Established genetic/developmental risk

The strongest recognized predisposition is a **disorder/difference of sex development with a dysgenetic gonad and Y-chromosome material**, especially the gonadoblastoma region of Y. In a 22-patient pediatric series, 6/22 (27.3%) had gonadal neoplasia. Rates were 4/6 (66.7%) in 46,XY complete gonadal dysgenesis, 1/10 (10%) in Turner syndrome with Y material, and 1/6 (16.6%) in androgen synthesis/action disorders. All tumors arose in streak-gonad tissue; gonadoblastoma and dysgerminoma predominated. Estimates are imprecise because cohorts are small and management practices differ. (lu2022gonadaltumorrisk pages 6-7, lu2022gonadaltumorrisk pages 1-2, lu2022gonadaltumorrisk pages 5-6)

Risk is enhanced by an intra-abdominal gonad, incomplete germ-cell maturation, expression of OCT3/4 and TSPY, and increasing age. A 2023 Swyer-syndrome report emphasized that primary amenorrhea and absent secondary sexual development should trigger DSD assessment even when imaging and serum markers are unrevealing. (sowinskaprzepiera2023latediagnosisof pages 1-2, piazza2019germcelltumors pages 1-2)

### Environmental, lifestyle, infectious, and protective factors

No reproducible causal association with smoking, alcohol, diet, obesity, occupational toxins, pollution, radiation, or an infectious agent was established in the retrieved ovarian-specific literature. No validated protective germline allele, dietary intervention, medication, or vaccine is known. Complete androgen insensitivity may confer lower childhood malignant transformation risk than complete gonadal dysgenesis, but it should not be treated as a general protective factor; risk rises with age and remains management-dependent. (piazza2019germcelltumors pages 4-5, lanciotti2019differentclinicalpresentations pages 3-5)

Accordingly, no clinically validated gene–environment interaction has been established. Apparent references to carcinogen-related methylation are generic cancer biology and not evidence that a specific exposure causes MOGCT. (pinto2023molecularbiologyof pages 11-12)

## 3. Phenotypes

The typical onset is pediatric, adolescent, or young-adult. Most cases occur at 10–25 years, with a reported median age of 18. Symptoms often develop over only 2–4 weeks, reflecting rapid tumor growth. Abdominal pain occurs in approximately 87% and a palpable abdominal/pelvic mass in 85%. Possible manifestations include abdominal distension, nausea/vomiting, torsion or rupture, menstrual disturbance, precocious puberty or virilization from hormone-producing components, ascites, and symptoms from metastatic peritoneal, nodal, hepatic, or pulmonary disease. (saani2023clinicalchallengesin pages 2-3, saani2023clinicalchallengesin pages 1-2)

Suggested HPO annotations are **Abdominal pain (HP:0002027)**, abdominal distention, pelvic mass, ovarian neoplasm, nausea and vomiting, ascites, menstrual irregularity, primary amenorrhea, elevated serum AFP, elevated serum β-hCG, and elevated serum LDH. Frequencies beyond pain and palpable mass are not robustly quantified.

Laboratory phenotype depends on histology:

* **YST:** AFP elevation is characteristic.
* **Choriocarcinoma:** β-hCG elevation.
* **Embryonal carcinoma:** AFP and/or β-hCG.
* **Dysgerminoma:** LDH may be elevated; a minority containing syncytiotrophoblast can produce β-hCG.
* **Immature teratoma:** AFP should prompt evaluation for a YST component, although modest elevations can occur.

A 2024 series of 16 female pelvic YSTs found AFP elevation in every patient and CA-125 elevation in 7/12 (58.33%). Thirteen of 16 lesions (81.25%) were ovarian. These data are useful but derive from a small referral cohort. 

Quality-of-life burdens include acute pain, hospitalization, chemotherapy toxicity, fear of recurrence, altered body image and sexuality, premature ovarian insufficiency, and uncertainty about fertility. Fertility-sparing treatment improves reproductive opportunity, but formal EQ-5D, SF-36, or PROMIS estimates were not available in the retrieved ovarian-specific evidence. (saani2023clinicalchallengesin pages 5-6)

## 4. Genetic and molecular information

### Somatic alterations

MOGCT is not usually a single-gene Mendelian disorder. Its defining molecular pattern is low somatic point-mutation burden with aneuploidy, copy-number imbalance, and epigenetic reprogramming. Recurrent alterations include:

* **12p gain or i(12p):** a keystone feature of postpubertal malignant GCT. One series found 12p gain in 15/34 (44%) malignant tumors. In a pediatric multi-omic cohort, 12p gain occurred in 39%, and 40% of that group carried i(12p).
* Other recurrent gains include **20q, 21, 8, and 1q**; chromosome 13 loss occurs in some tumors.
* **KIT** activating mutations, commonly exon 17, are enriched in dysgerminoma. In one 87-tumor landscape study, nonsynonymous KIT variants occurred in 4/24 sequenced cases (16.7%).
* **KRAS/NRAS** mutations occur less frequently; recurrent KRAS codon-12 variants have been reported.
* **PIK3CA amplification** occurred in 19/87 (21.8%) and **AKT amplification** in 18/87 (20.6%).
* YST studies report **KRAS, KIT**, occasional **TP53**, deletion of **ARID1A/PARK2**, and amplification of **ZNF217, CDKN1B,** and **KRAS**.
* Immature teratomas often have near-diploid genomes with extensive loss of heterozygosity but few or no recurrent somatic driver mutations. (pinto2023molecularbiologyof pages 7-9, pinto2023molecularbiologyof pages 9-11)

These are predominantly **somatic** alterations. Population allele frequencies are therefore not meaningful in the way they are for inherited disorders. Their presence does not currently mandate routine germline testing. Germline karyotyping or DSD-focused testing is appropriate when there is primary amenorrhea, absent puberty, virilization, bilateral dysgenetic gonads, Turner mosaicism, or other syndromic findings.

### Epigenetics, transcriptomics, and noncoding RNA

Dysgerminoma/germinoma is globally hypomethylated and retains pluripotency expression. More differentiated YST, teratoma, and choriocarcinoma are relatively hypermethylated; embryonal carcinoma is intermediate. In 154 pediatric GCTs, 8,481 differentially methylated regions were identified, with dysgerminoma/germinoma showing reduced methylation in angiogenesis and immune pathways and YST showing tumor-suppressor hypermethylation. All eight ovarian GCTs in one IGF2/H19 study were hypomethylated at that imprinting-control region. (pinto2023molecularbiologyof pages 11-12)

YSTs overexpress endodermal programs such as **GATA6** and **FOXA2** and show WNT/β-catenin and TGF-β/BMP pathway enrichment. The **miR-371–373** and **miR-302–367** clusters are overexpressed across malignant GCT sites and histologies. Their clinical use in ovarian disease remains investigational; the strongest validation currently comes from testicular GCT, where miR-371a-3p reached 84.7% sensitivity and 99% specificity in one cited study. (pinto2023molecularbiologyof pages 9-11, pinto2023molecularbiologyof pages 12-13)

### Suggested annotations

* **GO biological processes:** primordial germ-cell development; germ-cell migration; DNA methylation/demethylation; genomic imprinting; regulation of cell proliferation; MAPK cascade; PI3K–AKT signaling; Wnt signaling; BMP signaling; epithelial-to-mesenchymal transition; nucleotide-excision repair; apoptotic process.
* **Cell Ontology:** primordial germ cell; oogonium; oocyte; ovarian germ cell; tumor cell; peritoneal mesothelial cell; immune cell.
* **GO cellular components:** nucleus, chromatin, chromosome, plasma membrane, receptor tyrosine-kinase complex, mitotic spindle.

## 5–6. Environment and pathophysiology

The principal causal chain is:

1. **Upstream developmental vulnerability:** primordial germ cells undergo migration, imprint erasure, and global epigenetic reprogramming.
2. **Persistence of an immature/pluripotent state:** OCT3/4, NANOG, SOX factors, KIT/KITLG, and related programs support survival rather than normal differentiation.
3. **Genomic/epigenomic change:** 12p gain, aneuploidy, KIT or RAS activation, PI3K–AKT amplification, imprinting defects, and histology-specific methylation alter proliferation and lineage commitment.
4. **Histologic divergence:** germinoma-like cells produce dysgerminoma; endodermal differentiation produces YST; pluripotent somatic differentiation produces teratoma; mixed differentiation produces mixed tumors.
5. **Downstream behavior:** rapid proliferation causes a large ovarian mass, pain, rupture/torsion, and peritoneal or nodal dissemination. AFP, β-hCG, and LDH reflect lineage and tumor burden.
6. **Treatment response/resistance:** cisplatin DNA adducts normally trigger apoptosis. Resistance can involve nucleotide-excision repair, TP53-pathway change, cancer-stem-cell programs, EMT, and detoxification. **OVOL2** overexpression correlates with resistant YST; in NOY1-CR cells, **GSTA1**, ABCG2, CD133, and ALDH programs were increased. (pinto2023molecularbiologyof pages 16-18, pinto2023molecularbiologyof pages 13-15, pinto2023molecularbiologyof pages 15-16)

Immune involvement is incompletely characterized. Dysgerminomas often contain conspicuous lymphocytes and show immune-pathway epigenetic differences, but no ovarian-specific immune biomarker currently selects checkpoint therapy. Proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, and CRISPR-screen evidence is too sparse for routine annotation. (saani2023clinicalchallengesin pages 8-9, pinto2023molecularbiologyof pages 11-12)

## 7. Anatomical structures

The primary organ is the **ovary**—suggested UBERON term *ovary* (**UBERON:0000992**)—usually one ovary. Bilaterality occurs in approximately 10–15% of pure dysgerminomas and 5–10% of mixed tumors; bilateral YST and immature teratoma are uncommon. Secondary sites include pelvic and abdominal peritoneum, omentum, retroperitoneal lymph nodes, liver, and lung. (pinto2023molecularbiologyof pages 4-6, saani2023clinicalchallengesin pages 2-3)

Relevant tissues/cells are ovarian parenchyma and germ-cell lineage, with tumor-associated stroma, vasculature, lymphocytes, and peritoneal mesothelium. At subcellular level, the nucleus/chromatin and chromosomes are central because copy-number and epigenetic abnormalities dominate.

## 8–9. Temporal development, inheritance, and population

MOGCT commonly has acute/subacute presentation and rapid progression, not a long premalignant symptomatic phase. Approximately 60–70% present at an early stage. FIGO ovarian staging is used: stage I is confined to ovaries/fallopian tubes; II involves pelvic extension; III includes extrapelvic peritoneal or retroperitoneal nodal disease; IV denotes distant metastasis. Most relapses occur in the first two years, frequently in peritoneal or retroperitoneal nodal sites. (saani2023clinicalchallengesin pages 3-5, saani2023clinicalchallengesin pages 5-6)

MOGCTs account for approximately 2–5% of ovarian cancers. The 2023 review gives a global incidence near **4 per million women per year**; its separate “4 per 100,000” estimate appears internally inconsistent and should not be combined with the per-million estimate without checking the underlying source. Higher proportional frequencies have been reported in Asian and African populations and in Saudi Arabia—13.8% of ovarian tumors versus approximately 5% in Western series—but proportions are affected by the younger population structure and referral patterns. (saani2023clinicalchallengesin pages 2-3, saani2023clinicalchallengesin pages 1-2)

The usual inheritance pattern is **sporadic/multifactorial**, with no established penetrance, anticipation, carrier frequency, founder variant, or germline-mosaicism model. DSD-associated risk follows the underlying condition—for example, 46,XY gonadal dysgenesis or mosaic Y-chromosome material—not an inheritance pattern intrinsic to MOGCT.

## 10. Diagnosis

### Clinical work-up

A rapidly enlarging adnexal mass in a child or young adult should prompt:

1. Pelvic/abdominal ultrasonography with Doppler.
2. Serum **AFP, β-hCG, LDH**, complete blood count, renal and hepatic function; CA-125 can assist but is nonspecific.
3. Contrast-enhanced abdominal/pelvic CT or MRI for extent; chest imaging for metastases. PET is selective, not routine.
4. Fertility and endocrine assessment before treatment where feasible.
5. Histopathologic confirmation and FIGO staging. (saani2023clinicalchallengesin pages 2-3)

YSTs are often solid or mixed solid-cystic, highly vascular masses. A 2024 cohort described rapid enhancement, rich low-resistance arterial flow, and a “fissure sign,” but these are supportive rather than diagnostic.

### Pathology and immunohistochemistry

Useful panels include:

* **Broad germ-cell marker:** SALL4.
* **Dysgerminoma:** OCT3/4, SALL4, SOX17, D2-40, KIT/CD117; typically AFP-negative.
* **YST:** AFP, glypican-3, SALL4; Schiller–Duval bodies and hyaline globules are classic.
* **Embryonal carcinoma:** OCT3/4, SALL4, CD30, cytokeratin.
* **Choriocarcinoma:** β-hCG in syncytiotrophoblast.
* **Immature teratoma:** immature neuroepithelial rosettes/tubules; thorough sampling is essential.

Chromosome-12p FISH may support a malignant postpubertal GCT but is not required in every classic case. (saani2023clinicalchallengesin pages 2-3)

Differential diagnoses include benign mature cystic teratoma, epithelial ovarian carcinoma, sex-cord stromal tumor, small-cell carcinoma of hypercalcemic type, lymphoma, metastatic carcinoma, gestational choriocarcinoma, and pregnancy. Gestational versus nongestational choriocarcinoma may require clinical history and genotyping.

Routine WES/WGS, methylation profiling, or liquid biopsy is not standard. Tumor sequencing is reasonable in relapsed/refractory disease or research protocols; karyotype and targeted DSD testing are indicated when phenotype suggests gonadal dysgenesis. No population screening test exists.

## 11. Outcomes and prognosis

Early-stage survival is approximately 82–100%; late-stage survival is near 75% in compiled series. Stage I disease has about 90% long-term disease-free survival. Dysgerminoma is exceptionally chemotherapy-sensitive. Adverse factors include advanced stage, residual disease, older/postmenopausal age, YST histology, slow or incomplete tumor-marker decline, platinum resistance, and relapse. Stage IV ovarian GCT in patients aged at least 11 years has been reported to have under 70% long-term disease-free survival. More than half of patients with relapsed YST may die from disease. (saani2023clinicalchallengesin pages 3-5, pinto2023molecularbiologyof pages 16-18, pinto2023molecularbiologyof pages 6-7)

Long-term morbidity is often treatment-related: bleomycin pulmonary toxicity; cisplatin nephrotoxicity, ototoxicity, neuropathy and cardiovascular/metabolic risk; etoposide-related myelosuppression and rare therapy-related leukemia; infertility or premature ovarian insufficiency; and psychosocial/sexual effects.

Fertility outcomes are generally favorable after conservative treatment. One cohort reported pregnancy in 42/45 women, yielding 65 pregnancies and 56 births among 40 survivors; another reported 33 uneventful pregnancies among 31/39 patients. Across studies, 75.6% retained regular menstruation and pregnancy rates ranged from 18.8% to 55.7%, though denominators and attempts to conceive varied. (saani2023clinicalchallengesin pages 3-5, saani2023clinicalchallengesin pages 5-6)

## 12. Treatment and current applications

### Standard algorithm

* **Stage IA dysgerminoma:** unilateral salpingo-oophorectomy (USO), staging, and surveillance. Surgery-only recurrence is approximately 15–25%, but relapse is usually salvageable.
* **Stage IA grade-1 immature teratoma:** USO, staging, surveillance.
* **Grade 2–3 stage-I immature teratoma:** surveillance versus 3–4 cycles BEP remains controversial; pediatric practice is more surveillance-oriented.
* **Stage-I YST or incompletely staged/marker-positive disease:** generally postoperative BEP; surveillance after completely staged, marker-negative disease is investigational and not universally accepted.
* **Stages II–IV:** fertility-sparing cytoreduction when feasible followed by 3–4 cycles BEP. Extensive mutilating surgery should be avoided because of chemosensitivity. EP may be used when bleomycin is unsuitable, particularly in older patients. (saani2023clinicalchallengesin pages 6-8, saani2023clinicalchallengesin pages 5-6, pinto2023molecularbiologyof pages 6-7)

BEP comprises **bleomycin, etoposide, and cisplatin**. Suggested NCI Thesaurus intervention concepts are unilateral salpingo-oophorectomy, fertility-sparing surgery, tumor-debulking surgery, BEP regimen, EP regimen, active surveillance, and autologous hematopoietic stem-cell transplantation. Chemotherapy agents should also be annotated individually; cisplatin is a platinum coordination compound and etoposide a topoisomerase-II inhibitor.

### Relapse and refractory disease

Options include complete resection of operable residual disease and salvage **TIP** (paclitaxel/ifosfamide/cisplatin), **VeIP** (vinblastine/ifosfamide/cisplatin), or high-dose **TI-CE** with autologous stem-cell rescue. Evidence is mostly extrapolated from testicular GCT. Growing teratoma syndrome—enlarging masses during/after chemotherapy with normalized markers and mature teratoma histology—is chemotherapy-resistant and requires complete surgical resection. (saani2023clinicalchallengesin pages 6-8)

Targeted agents remain experimental. Everolimus, imatinib, sunitinib, and pazopanib produced only 0–13% response rates in recurrent GCT series. Brentuximab vedotin produced responses in 2/9 patients. Pembrolizumab and avelumab studies in predominantly male refractory GCT have not shown convincing benefit; these cannot be assumed effective in ovarian disease. (saani2023clinicalchallengesin pages 6-8, saani2023clinicalchallengesin pages 8-9)

### Recent trial development

**NCT02429687/MOGCT-01**, a randomized open-label phase III Chinese study, compares paclitaxel 175 mg/m² plus carboplatin AUC 5–6 every 21 days for 4–6 cycles against BEP for 3–4 cycles. Estimated enrollment is 129; outcomes include five-year progression-free survival, overall survival, response, and toxicity. The registry was updated April 25, 2023 and listed estimated primary completion in May 2025 and completion in 2030. Importantly, the retrieved eligibility field inconsistently described sex-cord stromal histologies despite the title and intervention summary specifying MOGCT; eligibility should therefore be verified directly before referral: https://clinicaltrials.gov/study/NCT02429687. (NCT02429687 chunk 1)

## 13. Prevention

There is no established primary prevention for sporadic MOGCT, no vaccine, and no population-based ovarian screening program. Secondary prevention consists of rapid evaluation of symptoms and longitudinal marker/imaging surveillance after treatment.

The principal risk-directed primary prevention is **prophylactic bilateral gonadectomy for high-risk dysgenetic gonads**, especially confirmed 46,XY complete gonadal dysgenesis. In lower-risk DSD groups, timing should be individualized through multidisciplinary endocrine, genetics, gynecology, pathology, fertility, and psychosocial counseling. Ultrasound/MRI cannot reliably exclude early gonadal neoplasia, and no liquid biomarker has sufficient validation to replace histologic risk management. (lu2022gonadaltumorrisk pages 7-8, sowinskaprzepiera2023latediagnosisof pages 1-2)

Tertiary prevention includes fertility counseling and cryopreservation where feasible, pulmonary/renal/auditory monitoring during BEP, avoidance of unnecessary radical surgery, structured surveillance for early relapse, and long-term survivorship care.

## 14–15. Other species and model systems

No well-validated naturally occurring veterinary disease was found that is sufficiently characterized to serve as a direct homolog of human MOGCT; zoonotic transmission is not applicable. Germ-cell developmental pathways are evolutionarily conserved, but spontaneous ovarian GCTs in companion animals should not be treated as equivalent without comparative pathology and molecular confirmation.

Available experimental systems are limited:

* **NOY1/NOY2 human ovarian YST cell lines**; NOY1-CR was generated by 12 months of stepwise cisplatin exposure and became 22.3-fold more resistant. GSTA1 inhibition restored cisplatin sensitivity.
* **TC587**, derived from a 12-year-old with ovarian YST, expresses AFP and SALL4 and carries NRAS, KIT, KMT2C, RSF1, and TP53 alterations.
* **Three-dimensional spheroids and quail chorioallantoic-membrane assays** model invasion and micrometastasis.
* **Immunodeficient-mouse xenografts** reproduce tumor formation but lack an intact human immune microenvironment.
* A pediatric ovarian-YST PDX reportedly mirrored clinical response to bleomycin/etoposide/cisplatin; nevertheless, no broad, well-validated ovarian-GCT PDX panel or organoid biobank exists. (pinto2023molecularbiologyof pages 13-15, pinto2023molecularbiologyof pages 15-16)

These models are useful for cisplatin resistance, stemness, and candidate-drug testing but incompletely capture developmental origin, histologic diversity, host immunity, fertility effects, and patient-to-patient heterogeneity.

## Evidence limitations and authoritative interpretation

The most authoritative recent ovarian-specific reviews emphasize that rarity has produced small, retrospective, histologically mixed cohorts and substantial extrapolation from testicular GCT. Apparent genomic frequencies can therefore vary by age and subtype. Molecular findings such as KIT, PI3K, methylation, and miR-371–373 are biologically compelling but are not yet routine predictive biomarkers. The central expert consensus is consequently conservative: preserve fertility whenever oncologically safe, use histology/stage/marker kinetics rather than unvalidated sequencing to guide first-line care, avoid overtreatment of low-risk stage-I disease where surveillance is supported, and refer recurrent disease to a specialist GCT center or clinical trial. (pinto2023molecularbiologyof pages 7-9, pinto2023molecularbiologyof pages 1-3, pinto2023molecularbiologyof pages 16-18)

### Principal recent sources

* Pinto MT et al. **Molecular Biology of Pediatric and Adult Ovarian Germ Cell Tumors: A Review.** *Cancers*. Published May 29, 2023. DOI: https://doi.org/10.3390/cancers15112990. (pinto2023molecularbiologyof pages 4-6)
* Saani I et al. **Clinical Challenges in the Management of Malignant Ovarian Germ Cell Tumours.** *International Journal of Environmental Research and Public Health*. Published June 15, 2023. DOI: https://doi.org/10.3390/ijerph20126089. (saani2023clinicalchallengesin pages 3-5)
* Lu L et al. **Gonadal tumor risk in pediatric and adolescent phenotypic females with disorders of sex development and Y chromosomal constitution.** *Frontiers in Pediatrics*. Published July 2022. DOI: https://doi.org/10.3389/fped.2022.856128. (lu2022gonadaltumorrisk pages 1-2)
* Berek JS et al. **Cancer of the ovary, fallopian tube, and peritoneum: 2021 update.** *International Journal of Gynecology & Obstetrics*. Published October 2021. DOI: https://doi.org/10.1002/ijgo.13878. (berek2021cancerofthe pages 17-18)

PMIDs were not reliably exposed in the retrieved full-text metadata and therefore are not fabricated here; DOI URLs are supplied for source resolution.

References

1. (pinto2023molecularbiologyof pages 4-6): Mariana Tomazini Pinto, Gisele Eiras Martins, Ana Glenda Santarosa Vieira, Janaina Mello Soares Galvão, Cristiano de Pádua Souza, Carla Renata Pacheco Donato Macedo, and Luiz Fernando Lopes. Molecular biology of pediatric and adult ovarian germ cell tumors: a review. Cancers, 15:2990, May 2023. URL: https://doi.org/10.3390/cancers15112990, doi:10.3390/cancers15112990. This article has 24 citations.

2. (saani2023clinicalchallengesin pages 2-3): Iqra Saani, Nitish Raj, Raja Sood, Shahbaz Ansari, Haider Abbas Mandviwala, Elisabet Sanchez, and Stergios Boussios. Clinical challenges in the management of malignant ovarian germ cell tumours. International Journal of Environmental Research and Public Health, 20:6089, Jun 2023. URL: https://doi.org/10.3390/ijerph20126089, doi:10.3390/ijerph20126089. This article has 87 citations.

3. (pinto2023molecularbiologyof pages 1-3): Mariana Tomazini Pinto, Gisele Eiras Martins, Ana Glenda Santarosa Vieira, Janaina Mello Soares Galvão, Cristiano de Pádua Souza, Carla Renata Pacheco Donato Macedo, and Luiz Fernando Lopes. Molecular biology of pediatric and adult ovarian germ cell tumors: a review. Cancers, 15:2990, May 2023. URL: https://doi.org/10.3390/cancers15112990, doi:10.3390/cancers15112990. This article has 24 citations.

4. (pinto2023molecularbiologyof pages 16-18): Mariana Tomazini Pinto, Gisele Eiras Martins, Ana Glenda Santarosa Vieira, Janaina Mello Soares Galvão, Cristiano de Pádua Souza, Carla Renata Pacheco Donato Macedo, and Luiz Fernando Lopes. Molecular biology of pediatric and adult ovarian germ cell tumors: a review. Cancers, 15:2990, May 2023. URL: https://doi.org/10.3390/cancers15112990, doi:10.3390/cancers15112990. This article has 24 citations.

5. (saani2023clinicalchallengesin pages 1-2): Iqra Saani, Nitish Raj, Raja Sood, Shahbaz Ansari, Haider Abbas Mandviwala, Elisabet Sanchez, and Stergios Boussios. Clinical challenges in the management of malignant ovarian germ cell tumours. International Journal of Environmental Research and Public Health, 20:6089, Jun 2023. URL: https://doi.org/10.3390/ijerph20126089, doi:10.3390/ijerph20126089. This article has 87 citations.

6. (saani2023clinicalchallengesin pages 5-6): Iqra Saani, Nitish Raj, Raja Sood, Shahbaz Ansari, Haider Abbas Mandviwala, Elisabet Sanchez, and Stergios Boussios. Clinical challenges in the management of malignant ovarian germ cell tumours. International Journal of Environmental Research and Public Health, 20:6089, Jun 2023. URL: https://doi.org/10.3390/ijerph20126089, doi:10.3390/ijerph20126089. This article has 87 citations.

7. (saani2023clinicalchallengesin pages 3-5): Iqra Saani, Nitish Raj, Raja Sood, Shahbaz Ansari, Haider Abbas Mandviwala, Elisabet Sanchez, and Stergios Boussios. Clinical challenges in the management of malignant ovarian germ cell tumours. International Journal of Environmental Research and Public Health, 20:6089, Jun 2023. URL: https://doi.org/10.3390/ijerph20126089, doi:10.3390/ijerph20126089. This article has 87 citations.

8. (pinto2023molecularbiologyof pages 9-11): Mariana Tomazini Pinto, Gisele Eiras Martins, Ana Glenda Santarosa Vieira, Janaina Mello Soares Galvão, Cristiano de Pádua Souza, Carla Renata Pacheco Donato Macedo, and Luiz Fernando Lopes. Molecular biology of pediatric and adult ovarian germ cell tumors: a review. Cancers, 15:2990, May 2023. URL: https://doi.org/10.3390/cancers15112990, doi:10.3390/cancers15112990. This article has 24 citations.

9. (pinto2023molecularbiologyof pages 11-12): Mariana Tomazini Pinto, Gisele Eiras Martins, Ana Glenda Santarosa Vieira, Janaina Mello Soares Galvão, Cristiano de Pádua Souza, Carla Renata Pacheco Donato Macedo, and Luiz Fernando Lopes. Molecular biology of pediatric and adult ovarian germ cell tumors: a review. Cancers, 15:2990, May 2023. URL: https://doi.org/10.3390/cancers15112990, doi:10.3390/cancers15112990. This article has 24 citations.

10. (pinto2023molecularbiologyof pages 12-13): Mariana Tomazini Pinto, Gisele Eiras Martins, Ana Glenda Santarosa Vieira, Janaina Mello Soares Galvão, Cristiano de Pádua Souza, Carla Renata Pacheco Donato Macedo, and Luiz Fernando Lopes. Molecular biology of pediatric and adult ovarian germ cell tumors: a review. Cancers, 15:2990, May 2023. URL: https://doi.org/10.3390/cancers15112990, doi:10.3390/cancers15112990. This article has 24 citations.

11. (pinto2023molecularbiologyof pages 6-7): Mariana Tomazini Pinto, Gisele Eiras Martins, Ana Glenda Santarosa Vieira, Janaina Mello Soares Galvão, Cristiano de Pádua Souza, Carla Renata Pacheco Donato Macedo, and Luiz Fernando Lopes. Molecular biology of pediatric and adult ovarian germ cell tumors: a review. Cancers, 15:2990, May 2023. URL: https://doi.org/10.3390/cancers15112990, doi:10.3390/cancers15112990. This article has 24 citations.

12. (saani2023clinicalchallengesin pages 6-8): Iqra Saani, Nitish Raj, Raja Sood, Shahbaz Ansari, Haider Abbas Mandviwala, Elisabet Sanchez, and Stergios Boussios. Clinical challenges in the management of malignant ovarian germ cell tumours. International Journal of Environmental Research and Public Health, 20:6089, Jun 2023. URL: https://doi.org/10.3390/ijerph20126089, doi:10.3390/ijerph20126089. This article has 87 citations.

13. (NCT02429687 chunk 1): Beihua Kong. TC or BEP in Treating Patients With Malignant Ovarian Germ Cell Tumors. Beihua Kong. 2015. ClinicalTrials.gov Identifier: NCT02429687

14. (saani2023clinicalchallengesin pages 8-9): Iqra Saani, Nitish Raj, Raja Sood, Shahbaz Ansari, Haider Abbas Mandviwala, Elisabet Sanchez, and Stergios Boussios. Clinical challenges in the management of malignant ovarian germ cell tumours. International Journal of Environmental Research and Public Health, 20:6089, Jun 2023. URL: https://doi.org/10.3390/ijerph20126089, doi:10.3390/ijerph20126089. This article has 87 citations.

15. (pinto2023molecularbiologyof pages 13-15): Mariana Tomazini Pinto, Gisele Eiras Martins, Ana Glenda Santarosa Vieira, Janaina Mello Soares Galvão, Cristiano de Pádua Souza, Carla Renata Pacheco Donato Macedo, and Luiz Fernando Lopes. Molecular biology of pediatric and adult ovarian germ cell tumors: a review. Cancers, 15:2990, May 2023. URL: https://doi.org/10.3390/cancers15112990, doi:10.3390/cancers15112990. This article has 24 citations.

16. (pinto2023molecularbiologyof pages 15-16): Mariana Tomazini Pinto, Gisele Eiras Martins, Ana Glenda Santarosa Vieira, Janaina Mello Soares Galvão, Cristiano de Pádua Souza, Carla Renata Pacheco Donato Macedo, and Luiz Fernando Lopes. Molecular biology of pediatric and adult ovarian germ cell tumors: a review. Cancers, 15:2990, May 2023. URL: https://doi.org/10.3390/cancers15112990, doi:10.3390/cancers15112990. This article has 24 citations.

17. (NCT02429687 chunk 2): Beihua Kong. TC or BEP in Treating Patients With Malignant Ovarian Germ Cell Tumors. Beihua Kong. 2015. ClinicalTrials.gov Identifier: NCT02429687

18. (lu2022gonadaltumorrisk pages 6-7): Liangsheng Lu, Feihong Luo, and Xiang Wang. Gonadal tumor risk in pediatric and adolescent phenotypic females with disorders of sex development and y chromosomal constitution with different genetic etiologies. Frontiers in Pediatrics, Jul 2022. URL: https://doi.org/10.3389/fped.2022.856128, doi:10.3389/fped.2022.856128. This article has 16 citations.

19. (lu2022gonadaltumorrisk pages 1-2): Liangsheng Lu, Feihong Luo, and Xiang Wang. Gonadal tumor risk in pediatric and adolescent phenotypic females with disorders of sex development and y chromosomal constitution with different genetic etiologies. Frontiers in Pediatrics, Jul 2022. URL: https://doi.org/10.3389/fped.2022.856128, doi:10.3389/fped.2022.856128. This article has 16 citations.

20. (lu2022gonadaltumorrisk pages 5-6): Liangsheng Lu, Feihong Luo, and Xiang Wang. Gonadal tumor risk in pediatric and adolescent phenotypic females with disorders of sex development and y chromosomal constitution with different genetic etiologies. Frontiers in Pediatrics, Jul 2022. URL: https://doi.org/10.3389/fped.2022.856128, doi:10.3389/fped.2022.856128. This article has 16 citations.

21. (sowinskaprzepiera2023latediagnosisof pages 1-2): Elżbieta Sowińska-Przepiera, Mariola Krzyścin, Adam Przepiera, Agnieszka Brodowska, Ewelina Malanowska, Mateusz Kozłowski, and Aneta Cymbaluk-Płoska. Late diagnosis of swyer syndrome in a patient with bilateral germ cell tumor treated with a contraceptive due to primary amenorrhea. International Journal of Environmental Research and Public Health, 20:2139, Jan 2023. URL: https://doi.org/10.3390/ijerph20032139, doi:10.3390/ijerph20032139. This article has 6 citations.

22. (piazza2019germcelltumors pages 1-2): Mauri José Piazza and Almir Antonio Urbanetz. Germ cell tumors in dysgenetic gonads. Clinics, 74:e408, Nov 2019. URL: https://doi.org/10.6061/clinics/2019/e408, doi:10.6061/clinics/2019/e408. This article has 37 citations and is from a peer-reviewed journal.

23. (piazza2019germcelltumors pages 4-5): Mauri José Piazza and Almir Antonio Urbanetz. Germ cell tumors in dysgenetic gonads. Clinics, 74:e408, Nov 2019. URL: https://doi.org/10.6061/clinics/2019/e408, doi:10.6061/clinics/2019/e408. This article has 37 citations and is from a peer-reviewed journal.

24. (lanciotti2019differentclinicalpresentations pages 3-5): Lucia Lanciotti, Marta Cofini, Alberto Leonardi, Mirko Bertozzi, Laura Penta, and Susanna Esposito. Different clinical presentations and management in complete androgen insensitivity syndrome (cais). International Journal of Environmental Research and Public Health, 16:1268, Apr 2019. URL: https://doi.org/10.3390/ijerph16071268, doi:10.3390/ijerph16071268. This article has 126 citations.

25. (pinto2023molecularbiologyof pages 7-9): Mariana Tomazini Pinto, Gisele Eiras Martins, Ana Glenda Santarosa Vieira, Janaina Mello Soares Galvão, Cristiano de Pádua Souza, Carla Renata Pacheco Donato Macedo, and Luiz Fernando Lopes. Molecular biology of pediatric and adult ovarian germ cell tumors: a review. Cancers, 15:2990, May 2023. URL: https://doi.org/10.3390/cancers15112990, doi:10.3390/cancers15112990. This article has 24 citations.

26. (lu2022gonadaltumorrisk pages 7-8): Liangsheng Lu, Feihong Luo, and Xiang Wang. Gonadal tumor risk in pediatric and adolescent phenotypic females with disorders of sex development and y chromosomal constitution with different genetic etiologies. Frontiers in Pediatrics, Jul 2022. URL: https://doi.org/10.3389/fped.2022.856128, doi:10.3389/fped.2022.856128. This article has 16 citations.

27. (berek2021cancerofthe pages 17-18): Jonathan S. Berek, Malte Renz, Sean Kehoe, Lalit Kumar, and Michael Friedlander. Cancer of the ovary, fallopian tube, and peritoneum: 2021 update. International Journal of Gynaecology and Obstetrics, 155:61-85, Oct 2021. URL: https://doi.org/10.1002/ijgo.13878, doi:10.1002/ijgo.13878. This article has 726 citations.

## Artifacts

- [Edison artifact artifact-00](Malignant_Germ_Cell_Tumor_of_Ovary-deep-research-falcon_artifacts/artifact-00.md)