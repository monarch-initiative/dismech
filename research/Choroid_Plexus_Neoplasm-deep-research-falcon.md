---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T06:54:01.536219'
end_time: '2026-08-01T07:02:48.315073'
duration_seconds: 526.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Choroid Plexus Neoplasm
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 41
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Choroid_Plexus_Neoplasm-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Choroid Plexus Neoplasm
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Choroid Plexus Neoplasm** covering all of the
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
- **Disease Name:** Choroid Plexus Neoplasm
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Choroid Plexus Neoplasm** covering all of the
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


# Choroid Plexus Neoplasm: Disease-Characteristics Research Report

**Scope and evidence date.** This report treats *choroid plexus neoplasm/tumor* (CPT) as an umbrella diagnosis encompassing choroid plexus papilloma (CPP), atypical CPP (aCPP), and choroid plexus carcinoma (CPC). Recent human molecular studies from 2023–2024 are prioritized, supplemented by landmark clinical, genetic, and model-system evidence. Database identifiers and ontology mappings should be verified against the release used by the target knowledge base.

## Executive summary

Choroid plexus neoplasms are rare intraventricular epithelial tumors arising from the cerebrospinal-fluid-producing choroid plexus. WHO CNS classification recognizes **CPP (grade 1), aCPP (grade 2), and CPC (grade 3)**. They account for less than 1% of all brain tumors but approximately 10–20% of tumors arising during the first year of life; one 2024 pediatric cohort review gives 2–6% of all pediatric brain tumors. CPP is usually cured by complete resection, aCPP has increased recurrence risk, and CPC is an aggressive, highly vascular tumor prone to invasion and cerebrospinal-fluid dissemination. (garcia2023genomicprofileof pages 1-2, li2022disruptionofgmncmcidas pages 1-2, choi2024comprehensivemultiomicsanalysis pages 1-2, thomas2021thegeneticlandscape pages 1-3)

The strongest established predisposition is **autosomal-dominant heritable TP53-related cancer/Li–Fraumeni syndrome (LFS)**. Tumor TP53 status is also prognostic: in the prospective SJYC07 cohort, 5-year progression-free survival (PFS) was 100% for TP53-wild-type CPC versus 28.6% for TP53-mutant CPC. Current translational advances include methylation classification, paired tumor-normal sequencing, 2024 single-nucleus transcriptomics, multiomics identification of cell-cycle/epithelial–mesenchymal-transition programs, and experimental locoregional chemotherapy and CAR-T approaches. (liu2021outcomeandmolecular pages 1-2, hill2024singlenucleusrnaseqdissection pages 1-2, choi2024comprehensivemultiomicsanalysis pages 1-2)

| Entity | WHO grade | Typical demographics/site | Molecular features | Clinical behavior | Standard management |
|---|---:|---|---|---|---|
| Choroid plexus papilloma (CPP) | 1 | Intraventricular choroid plexus tumor; often pediatric but also occurs in adults; molecular subgrouping supports pediatric supratentorial low-risk and adult infratentorial low-risk groups (ontology/site labels requiring validation) (garcia2023genomicprofileof pages 1-2, hill2024singlenucleusrnaseqdissection pages 1-2) | Usually lacks recurrent driver mutations; adult CPTs may harbor TERT promoter mutations (7/28 adults across CPTs, associated with shorter PFS) or rare CCDC47-PRKCA fusion in aggressive adult CPP; chromosome 9 amplification reported as CPP-specific in one 2024 multiomics cohort (hill2024singlenucleusrnaseqdissection pages 1-2) | Generally benign/low-risk; favorable prognosis relative to CPC; recurrence risk lower than aCPP/CPC but molecular subgroup can refine risk (garcia2023genomicprofileof pages 1-2, hill2024singlenucleusrnaseqdissection pages 1-2) | Maximal safe surgical resection is standard; adjuvant therapy usually not required after complete resection (general CPT management evidence), with radiotherapy considered selectively in incompletely resected/recurrent cases (garcia2023genomicprofileof pages 1-2) |
| Atypical choroid plexus papilloma (aCPP) | 2 | Pediatric intraventricular tumor; example pediatric case with hydrocephalus and ataxia; grouped with low-risk or high-risk methylation classes depending age/site, requiring molecular risk assessment (garcia2023genomicprofileof pages 2-5, hill2024singlenucleusrnaseqdissection pages 1-2) | Example tumor had BRD1 frameshift deletion with gains of chromosomes 12/18/20 and losses of 13q/22q; p53 IHC may be negative; no recurrent universal somatic driver established (garcia2023genomicprofileof pages 2-5, garcia2023genomicprofileof pages 1-2) | Intermediate behavior; higher recurrence risk than CPP; histology alone can be insufficient for risk stratification, so methylation profiling may add prognostic value (garcia2023genomicprofileof pages 1-2, hill2024singlenucleusrnaseqdissection pages 1-2) | Surgery is primary treatment; adjuvant radiotherapy/chemotherapy individualized, especially for subtotal resection or higher-risk molecular features; one reported case received 36 Gy RT and remained disease-free at 78 months (garcia2023genomicprofileof pages 2-5) |
| Choroid plexus carcinoma (CPC) | 3 | Rare aggressive malignant CPT of infancy/early childhood; median diagnosis age about 3 years, annual incidence about 0.3 per million; often supratentorial/pediatric high-risk methylation class; highly vascular, invasive, CSF-disseminating (liu2021outcomeandmolecular pages 1-2, hill2024singlenucleusrnaseqdissection pages 1-2) | TP53 is the dominant recurrent alteration: TP53 mutations in 7/47 CPTs overall and frequent in CPC; germline TP53/Li-Fraumeni common, with estimates of 50-80% in children with CPC from LFS guidelines; LOH at TP53, hyperdiploidy/genomic instability, whole-chromosome CNAs, chromosome 1 amplification, mutually exclusive TP53 and EPHA7 point mutations in one 2024 cohort; hypomethylation of repeat elements; multiciliogenesis program disruption (GMNC-MCIDAS), NOTCH/SHH involvement, MYC/TP53 cooperation in models (liu2021outcomeandmolecular pages 1-2, garcia2023genomicprofileof pages 5-8, fortuno2024cancerrisksassociated pages 1-2, hill2024singlenucleusrnaseqdissection pages 1-2) | Most aggressive subtype; recurrent/metastatic propensity and worse survival, especially with TP53 mutation. In SJYC07, 5-year PFS 61.5% and OS 68.4%; TP53-wild-type 5-year PFS 100% vs 28.6% for TP53-mutant tumors (liu2021outcomeandmolecular pages 9-10, liu2021outcomeandmolecular pages 1-2) | Maximal safe resection plus intensive chemotherapy is standard backbone; SJYC07 used high-dose methotrexate-containing non-myeloablative therapy with durable survival in >50% of patients. Radiotherapy is individualized and may be avoided or minimized in germline TP53 carriers because of secondary malignancy risk (liu2021outcomeandmolecular pages 9-10, liu2021outcomeandmolecular pages 1-2, frebourg2020guidelinesforthe pages 7-8) |
| Choroid plexus tumor molecular subgroup: pediatric A (pedA) | Not a WHO histologic grade; methylation subgroup | Young age, supratentorial, favorable-risk subgroup (ontology label requiring validation) (hill2024singlenucleusrnaseqdissection pages 1-2) | Defined by DNA methylation profiling rather than unique recurrent driver mutation; part of 3-group epigenetic framework (hill2024singlenucleusrnaseqdissection pages 1-2) | Favorable prognosis relative to pedB (hill2024singlenucleusrnaseqdissection pages 1-2) | Supports risk stratification alongside histology; not a standalone treatment entity (hill2024singlenucleusrnaseqdissection pages 1-2) |
| Choroid plexus tumor molecular subgroup: pediatric B (pedB) | Not a WHO histologic grade; methylation subgroup | Predominantly pediatric high-risk subgroup; includes many CPCs and some histologically lower-grade CPTs; frequent recurrences (liu2021outcomeandmolecular pages 9-10, hill2024singlenucleusrnaseqdissection pages 1-2) | Frequent chromosomal copy-number alterations; S/G2/M hyperproliferative enrichment on snRNA-seq; methylation-defined high-risk biology (liu2021outcomeandmolecular pages 9-10, hill2024singlenucleusrnaseqdissection pages 3-4, hill2024singlenucleusrnaseqdissection pages 1-2) | Higher risk of recurrence/aggressive course than pedA/adult subgroup, even when histology is not overtly carcinoma (hill2024singlenucleusrnaseqdissection pages 1-2) | Indicates need for closer surveillance and may justify therapy intensification in future stratified protocols (liu2021outcomeandmolecular pages 9-10, hill2024singlenucleusrnaseqdissection pages 1-2) |
| Choroid plexus tumor molecular subgroup: adult | Not a WHO histologic grade; methylation subgroup | Adult, often infratentorial low-risk subgroup (ontology/site label requiring validation) (hill2024singlenucleusrnaseqdissection pages 1-2) | TERT promoter mutations found in 7/28 adult CPTs and associated with shorter PFS; rare CCDC47-PRKCA fusion described in aggressive adult CPP; adult tumors showed higher macrophage proportion by snRNA-seq (22.4% vs 8.2% in pediatric high-risk tumors) (hill2024singlenucleusrnaseqdissection pages 3-4, hill2024singlenucleusrnaseqdissection pages 1-2) | Usually more favorable than pediatric high-risk subgroup, but adverse molecular lesions can signal worse course (hill2024singlenucleusrnaseqdissection pages 1-2) | Primarily surgical management; molecular profiling may identify adults needing closer follow-up (hill2024singlenucleusrnaseqdissection pages 1-2) |


*Table: This table summarizes the main choroid plexus neoplasm subtypes and molecular subgroups using only evidence gathered in the conversation. It is useful for quickly comparing histology, demographics, molecular findings, clinical behavior, and management while flagging site/ontology labels that require validation.*

## 1. Disease information

### Definition and classification

CPTs are **primary intraventricular neoplasms derived from choroid plexus epithelium**. Their three histologic entities form a biologic spectrum rather than a single uniform disease:

* **CPP:** WHO grade 1, papillary and generally indolent.
* **aCPP:** WHO grade 2, defined principally by increased mitotic activity and associated with greater recurrence risk.
* **CPC:** WHO grade 3, malignant, invasive, mitotically active, and often necrotic.

A useful direct statement from the 2024 multiomics study is: **“Choroid plexus tumors (CPTs) are intraventricular tumors derived from the choroid plexus epithelium and occur frequently in children.”** Published June 2024; DOI/URL: https://doi.org/10.1186/s40478-024-01814-y. (choi2024comprehensivemultiomicsanalysis pages 1-2)

### Identifiers and synonyms

* **MONDO umbrella:** choroid plexus neoplasm, **MONDO:0016717**.
* **MONDO subtype identifiers:** choroid plexus papilloma, **MONDO:0009837**; choroid plexus carcinoma, **MONDO:0016718**; benign choroid plexus neoplasm, **MONDO:0044764**. (OpenTargets Search: choroid plexus carcinoma,choroid plexus papilloma-TP53)
* **Synonyms:** choroid plexus tumor/CPT; choroid plexus papilloma/CPP; atypical choroid plexus papilloma/aCPP; choroid plexus carcinoma/CPC; tumor of choroid plexus epithelium.
* **MeSH:** *Choroid Plexus Neoplasms* is the preferred disease concept; confirm the current MeSH unique identifier in the production terminology release.
* **ICD:** ICD-10-CM coding is site/behavior based rather than disease-specific—e.g., malignant neoplasm of brain/ventricle for CPC and benign neoplasm of brain for CPP. Histology should therefore be retained separately with ICD-O morphology/topography. ICD-11 and ICD-O codes should be release-validated before ingestion.
* **OMIM/Orphanet:** the umbrella sporadic tumor does not behave like a single Mendelian OMIM phenotype. The clinically important inherited entry is LFS/heritable TP53-related cancer syndrome rather than “CPT” itself. Exact Orphanet identifiers were not established from the retrieved evidence and should not be inferred.

The evidence summarized here is predominantly **aggregated disease-level literature, registries, prospective trials, and molecular cohorts**, not individual EHR data. Two 2023 Brazilian cases are patient-level primary evidence and should not be used alone to estimate population frequencies. (garcia2023genomicprofileof pages 1-2, garcia2023genomicprofileof pages 5-8, garcia2023genomicprofileof pages 2-5)

## 2. Etiology, risk, and protective factors

### Causal and predisposing factors

Most CPTs are sporadic and lack a recurrent point-mutation driver. The clearest causal predisposition is a **germline pathogenic TP53 variant**, producing autosomal-dominant LFS/heritable TP53-related cancer syndrome; tumorigenesis commonly involves loss of the remaining wild-type allele and genomic instability. In one CPC, germline **TP53 c.718A>G (p.Ser240Gly)** was accompanied by 17p13.1 loss/LOH and hyperdiploidy. (garcia2023genomicprofileof pages 1-2, garcia2023genomicprofileof pages 5-8)

Published estimates place TP53 alterations in approximately **44–67% of CPCs**; the SJYC07 cohort found 7/13 TP53-mutant tumors, including four germline carriers. In the broader 47-CPT series, TP53 mutations occurred in 7/47 tumors (15%), five in children, illustrating that prevalence depends strongly on subtype composition. (liu2021outcomeandmolecular pages 1-2, choi2024comprehensivemultiomicsanalysis pages 1-2, thomas2021thegeneticlandscape pages 1-3)

### Other genetic risks

* Pediatric tumors show recurrent whole-chromosome changes rather than a universal driver: gains of chromosomes 1, 2, and 21q characterize pediatric-B enrichment.
* Adult CPTs may harbor **TERT promoter mutations**: 7/28 adults (25%) in one series, associated with shorter PFS (log-rank *P*=0.015).
* A rare **CCDC47–PRKCA** fusion caused by a chromosome-17 inversion was found in an aggressive adult CPP.
* A 2024 cohort identified mutually exclusive **TP53** and **EPHA7** point mutations plus chromosome-1 amplification only in CPC, whereas chromosome-9 amplification was CPP-specific; these are cohort-level candidates, not yet universal diagnostic markers. (choi2024comprehensivemultiomicsanalysis pages 1-2, thomas2021thegeneticlandscape pages 1-3)

### Environmental, infectious, lifestyle, and protective factors

No reproducible toxin, infection, diet, smoking, alcohol, occupation, or other lifestyle exposure is established as a CPT cause. No validated protective allele, dietary factor, vaccine, or medication prevents CPT. Apparent environmental modifiers of LFS penetrance remain speculative; reviews discuss lifestyle, diet, exposures, telomere length, MDM2/TP53 polymorphisms, and epigenetic modifiers, but individualized gene–environment risk estimates are unavailable. (gargallo2020li–fraumenisyndromeheterogeneity pages 7-8)

For TP53 carriers, **avoiding unnecessary ionizing radiation and genotoxic therapy** is a risk-reduction principle for subsequent cancers, not proven primary prevention of the index CPT. (frebourg2020guidelinesforthe pages 7-8)

## 3. Phenotypes

Clinical manifestations principally result from tumor bulk, CSF overproduction or outflow obstruction, hemorrhage/vascularity, invasion, and dissemination.

| Phenotype | Type and characteristics | Suggested HPO term |
|---|---|---|
| Hydrocephalus/increased intracranial pressure | Common presenting mechanism; progressive or subacute; particularly important in infants | Hydrocephalus **HP:0000238**; increased intracranial pressure |
| Headache | Subjective symptom, especially in older children/adults; variable severity | Headache **HP:0002315** |
| Nausea/vomiting | Symptom of raised intracranial pressure; vomiting documented in infant CPC | Vomiting **HP:0002013**; nausea |
| Bulging fontanelle/macrocephaly | Infant physical sign; reflects raised pressure | Bulging anterior fontanelle; macrocephaly **HP:0000256** |
| Papilledema | Ophthalmic sign of raised pressure | Papilledema **HP:0001085** |
| Ataxia/gait impairment | Neurologic sign, more likely with fourth-ventricular/posterior-fossa effects | Ataxia **HP:0001251**; gait disturbance **HP:0001288** |
| Cranial-nerve deficit | Focal neurologic sign; depends on location | Cranial nerve abnormality |
| Seizures | Less common neurologic symptom | Seizure **HP:0001250** |
| Developmental delay/cognitive impairment | May arise from hydrocephalus, tumor injury, surgery, chemotherapy, or radiation; important survivorship outcome | Global developmental delay **HP:0001263**; intellectual disability **HP:0001249** |
| Leptomeningeal dissemination | Imaging/pathologic manifestation, concentrated in CPC; may be present at diagnosis or emerge during follow-up | Neoplasm of the meninges/leptomeningeal disease; ontology mapping requires validation |

The classic review lists headache, hydrocephalus, papilledema, nausea, vomiting, cranial-nerve deficits, gait impairment, and seizures. A 2023 CPC infant had vomiting, bulging fontanelle, hydrocephalus, and transependymal edema. In the 2024 multiomics cohort, 5/11 CPC patients had leptomeningeal seeding, versus none with CPP; all seeded cases with known follow-up died. (garcia2023genomicprofileof pages 5-8, choi2024comprehensivemultiomicsanalysis pages 1-2, safaee2013choroidplexuspapillomas pages 1-2)

**Quality of life.** Tumor- and treatment-related hydrocephalus, neurodevelopmental delay, sensory deficits, endocrine effects, and impaired mobility can affect schooling, independence, and caregiver burden. A historical estimate gives 56% 5-year CPC survival, with many survivors experiencing long-term cognitive/developmental deficits. Disease-specific EQ-5D/SF-36 norms and robust per-phenotype frequencies were not identified. (thomas2021thegeneticlandscape pages 1-3)

## 4. Genetic and molecular information

### Principal genes and variants

* **TP53**—HGNC:11998; tumor-suppressor loss of function, usually germline or somatic missense/nonsense/indel with LOH. Germline pathogenic variants establish heritable TP53-related cancer risk; a tumor-only result does not prove germline origin. Open Targets ranks TP53 as the strongest supported disease target for the umbrella CPT and both CPP/CPC. (OpenTargets Search: choroid plexus carcinoma,choroid plexus papilloma-TP53)
* **TERT promoter**—somatic adult-CPT alteration; not a germline CPT cause.
* **EPHA7**—candidate somatic CPC alteration in one 20-patient cohort.
* **BRD1**—one aCPP carried a high-VAF frameshift deletion, classified AMP tier II; it is a case-specific candidate, not an established germline causal gene.
* **CCDC47–PRKCA**—rare somatic fusion in aggressive adult CPP.
* **TAF12, NFYC, RAD54L**—chromosome-1 candidate oncogenes; validation as routine biomarkers is incomplete. (garcia2023genomicprofileof pages 2-5, hill2024singlenucleusrnaseqdissection pages 1-2, choi2024comprehensivemultiomicsanalysis pages 1-2, thomas2021thegeneticlandscape pages 1-3)

Variant interpretation should use ACMG/AMP rules for germline TP53 and AMP/ASCO/CAP somatic tiers for tumor variants. Population frequencies must be checked variant-by-variant in gnomAD; no single carrier frequency applies to sporadic CPT. The Brazilian founder TP53 p.Arg337His allele is geographically enriched—historically reported near 1/300 newborns in southern/southeastern Brazil—but this does not represent global frequency. (bittar2021clinicalandmolecular pages 9-10, giacomazzi2015pediatriccancerand pages 1-2)

### Chromosomal and epigenetic abnormalities

CPTs commonly exhibit numerical aneuploidy and whole-chromosome copy-number alterations. Pediatric-B tumors are enriched for gains of chromosomes 1, 2, and 21q; adult tumors for gains of 5 and 9 and loss of 21q. The Brazilian aCPP had gains of 12, 18, and 20 and losses of 13q and 22q; its CPC had a hyperdiploid genome and TP53-locus loss. (garcia2023genomicprofileof pages 1-2, garcia2023genomicprofileof pages 2-5, thomas2021thegeneticlandscape pages 1-3)

DNA methylation resolves three clinically meaningful groups:

1. **Pediatric A:** supratentorial pediatric low-risk CPP/aCPP.
2. **Pediatric B:** supratentorial pediatric high-risk group containing CPP, aCPP, and CPC.
3. **Adult:** predominantly infratentorial low-risk CPP/aCPP.

Methylation complements rather than replaces histology. CPC-associated methylation biomarkers include **AK1, PER2, and PLSCR4**; homozygous TP53-mutant CPCs form a particularly adverse group. (liu2021outcomeandmolecular pages 9-10, hill2024singlenucleusrnaseqdissection pages 1-2, thomas2021thegeneticlandscape pages 1-3)

## 5. Environmental information

No infectious agent or environmental carcinogen has been causally linked to CPT. Consequently, CTD-style chemical annotations, pathogen taxonomy, lifestyle dose-response associations, and CHEBI preventive-agent annotations are **not currently justified**. Radiation is clinically relevant mainly as a treatment and as a subsequent-neoplasm hazard in germline TP53 carriers. (frebourg2020guidelinesforthe pages 7-8)

## 6. Mechanism and pathophysiology

### Causal chain

**Upstream predisposition:** germline or somatic TP53 dysfunction, uncommon adult TERT-promoter activation/fusion events, and/or chromosome-wide dosage imbalance → **checkpoint failure and genomic instability** → dysregulated cell cycle, replication stress, epithelial–mesenchymal transition, and impaired epithelial differentiation → expansion of choroid plexus epithelial tumor cells → hypervascular intraventricular mass, CSF obstruction/overproduction and hydrocephalus → invasion, leptomeningeal spread, neurologic injury, and developmental morbidity. (nagar2018anewgenetically pages 6-8, choi2024comprehensivemultiomicsanalysis pages 1-2, thomas2021thegeneticlandscape pages 1-3)

### Multiciliogenesis and developmental signaling

Normal choroid plexus epithelium contains multiciliated cells. Human CPCs show solitary cilia and reduced **GMNC–MCIDAS–FOXJ1** differentiation activity. In mouse systems, NOTCH activation suppresses GMNC/MCIDAS; disrupting the NOTCH complex restores multiciliation and decreases growth, while GMNC/MCIDAS overexpression suppresses tumor-cell proliferation. Combined NOTCH and Sonic Hedgehog defects generated CPC-like tumors. This is mechanistically strong model evidence but not yet a clinically validated therapeutic intervention. (li2022disruptionofgmncmcidas pages 1-2)

Suggested annotations include **GO:0007049 cell cycle**, **GO:0006281 DNA repair**, **GO:0007059 chromosome segregation**, **GO:0035082 axoneme assembly**, **GO:0060271 cilium assembly**, **GO:0048870 cell motility**, **GO:0001837 epithelial-to-mesenchymal transition**, and **GO:0007155 cell adhesion**. Relevant cells include **choroid plexus epithelial cell**, multiciliated epithelial cell, endothelial cell, macrophage, mesenchymal stromal cell, T cell, neuron, and glial cell; exact CL identifiers should be release-validated.

### Recent molecular profiling

**2024 multiomics.** Whole-genome, whole-transcriptome, and methylation sequencing of 20 tumors found CPC enrichment for cell-cycle and epithelial–mesenchymal-transition genes, metastasis/progression programs in disseminated CPC, and broad hypomethylation of LINEs, SINEs, LTRs, and retrotransposons. The authors concluded that loss of epigenetic transposable-element silencing may contribute to CPC tumorigenesis. Cohort composition was 6 CPP, 2 aCPP, 1 mixed CPP/papillary ependymoma, and 11 CPC; mean age was 5.2 years. (choi2024comprehensivemultiomicsanalysis pages 1-2)

**2024 single-nucleus RNA-seq.** Analysis of **23,906 nuclei from four disease-free choroid plexuses and 11 tumors** resolved epithelial, endothelial, mesenchymal, macrophage, neuronal, glial, and T-cell populations. Pediatric-B tumors were enriched for S/G2/M proliferative states; adult tumors had more macrophages (22.4% versus 8.2%, *P*=0.046), and tumors had fewer mesenchymal cells than normal tissue. The study’s abstract states that it identified “altered macrophage and mesenchymal cell states, as well as changes in extracellular matrix components.” Published October 2024; DOI/URL: https://doi.org/10.1038/s44318-024-00283-2. (hill2024singlenucleusrnaseqdissection pages 3-4, hill2024singlenucleusrnaseqdissection pages 1-2)

Proteomic, metabolomic, lipidomic, spatial-transcriptomic, and large CRISPR-screen signatures are not sufficiently validated for clinical annotation. No established metabolic enzyme deficiency or autoimmune mechanism exists.

## 7. Anatomical structures affected

* **Primary organ/system:** central nervous system/brain; ventricular system.
* **Primary tissue:** choroid plexus epithelial tissue over vascular stroma.
* **Sites:** lateral ventricles, third ventricle, fourth ventricle; rare cerebellopontine-angle, parenchymal, suprasellar, spinal, or disseminated neuraxial disease.
* **Age-site pattern:** children usually have lateral-ventricular/supratentorial tumors; adults more often have fourth-ventricular/infratentorial CPP. More than 80% of supratentorial CPPs in one review occurred before age 20. Median ages by CPP site were 1.5 years for lateral or third ventricle, 22.5 for fourth ventricle, and 35.5 for cerebellopontine angle. (safaee2013choroidplexuspapillomas pages 1-2)
* **Secondary structures:** meninges/leptomeninges, spinal neuraxis, periventricular white matter affected by edema, and brain parenchyma affected by pressure or invasion.
* **Subcellular compartments:** nucleus/chromatin (TP53, methylation and chromosome instability); centrosome/cilium/axoneme; plasma membrane and extracellular matrix.
* **Lateralization:** no intrinsic left/right disease rule, although older CPP series reported left-lateral-ventricular predominance. Bilateral or multifocal disease is unusual and should prompt evaluation for dissemination or predisposition.

Suggested UBERON concepts: brain, cerebral ventricle, lateral ventricle, third ventricle, fourth ventricle, choroid plexus, cerebrospinal fluid, meninges, and spinal cord; identifiers should be validated against the deployed UBERON release.

## 8. Temporal development

CPTs are predominantly pediatric and may be congenital; CPP has been detected in utero. Median CPP diagnosis is about 3.5 years, while CPC is concentrated in infancy/early childhood. Symptoms may develop subacutely or progressively as hydrocephalus increases. (liu2021outcomeandmolecular pages 1-2, safaee2013choroidplexuspapillomas pages 1-2)

There is no AJCC-style stage system. Clinically useful dimensions are histologic grade, localized versus disseminated disease, extent of resection, TP53 status, and methylation class. CPP may remain stable after complete resection; aCPP can recur, with one review reporting an approximately fivefold greater 5-year recurrence risk than grade-1 CPP; CPC may progress rapidly, recur, and metastasize through CSF. Treatment-induced remission is common after gross-total CPP resection and possible in CPC with multimodal therapy. Spontaneous durable remission is not a recognized management strategy. (liu2021outcomeandmolecular pages 1-2, safaee2013choroidplexuspapillomas pages 1-2)

## 9. Inheritance and population

### Epidemiology

CPTs represent **<1% of all brain tumors**, but approximately **10–20% of first-year brain tumors**. CPP incidence is approximately **0.3 per million person-years**, constitutes about 0.3–0.6% of intracranial tumors, and historically outnumbers CPC about 5:1. CPC incidence has likewise been estimated near 0.3 per million annually in childhood datasets. (garcia2023genomicprofileof pages 1-2, liu2021outcomeandmolecular pages 1-2, li2022disruptionofgmncmcidas pages 1-2, safaee2013choroidplexuspapillomas pages 1-2)

A historical CPP male:female ratio was 1.2:1; no consistent ethnicity-specific CPT excess is established. Geographic variation in inherited risk is relevant in southern/southeastern Brazil because of TP53 p.Arg337His. (giacomazzi2015pediatriccancerand pages 1-2, safaee2013choroidplexuspapillomas pages 1-2)

### Inheritance

Sporadic CPT is not inherited. LFS-associated predisposition is **autosomal dominant**, with variable, age-dependent penetrance and expressivity. De novo and constitutional mosaic TP53 variants occur; no anticipation, consanguinity effect, or general CPT carrier frequency is established. In a 2024 analysis of 146 TP53-positive families/4,028 individuals, cumulative risk of any cancer by age 50 was 92.4% in females and 59.7% in males. These figures describe TP53 carriers—not CPT penetrance specifically. (fortuno2024cancerrisksassociated pages 1-2)

## 10. Diagnostics

### Clinical and imaging work-up

1. Neurologic and developmental examination, head circumference/fontanelle assessment in infants, and fundoscopy when feasible.
2. Contrast-enhanced brain MRI: typically an intraventricular, lobulated/frond-like, intensely enhancing, highly vascular mass; assess hydrocephalus, edema, hemorrhage, invasion, and residual disease.
3. For suspected CPC/aCPP, obtain spine MRI and CSF staging when safe because of dissemination risk.
4. CT may show calcification or acute hemorrhage but adds radiation; MRI is preferred, especially in TP53 carriers.
5. Routine blood/CSF laboratory tests are nonspecific. No validated circulating protein or metabolite biomarker exists.

### Histopathology

CPP has orderly papillary fronds lined by relatively uniform cuboidal/columnar epithelium. aCPP shows increased mitoses; ancillary findings may include increased cellularity, pleomorphism, architectural blurring, and necrosis. CPC exhibits overt malignancy—high cellularity, loss of papillary architecture, brisk mitoses, pleomorphism, necrosis, and invasion. One review describes CPC as having at least four of these malignant features. Cytokeratin positivity supports epithelial differentiation; Ki-67 and p53 staining assist grading/risk assessment but do not replace sequencing. (garcia2023genomicprofileof pages 5-8, garcia2023genomicprofileof pages 2-5, safaee2013choroidplexuspapillomas pages 1-2)

Differential diagnoses include ependymoma, papillary tumor of the pineal region, papillary meningioma/intraventricular meningioma, metastatic papillary carcinoma, atypical teratoid/rhabdoid tumor, medulloblastoma/embryonal tumor, and choroid plexus hyperplasia. Diagnosis should integrate morphology, immunohistochemistry, imaging/site, and methylation classification.

### Molecular and genetic testing

* Perform tumor sequencing with **TP53**, copy-number analysis, and preferably DNA-methylation classification in CPC, diagnostically ambiguous tumors, aggressive aCPP, and recurrence.
* Perform **paired germline TP53 testing with genetic counseling for every child with CPC**, irrespective of family history; tumor-only testing can miss or misclassify constitutional disease.
* A pediatric CNS predisposition panel or WES/WGS is reasonable when phenotype/family history is broader or TP53 testing is negative. WGS adds structural-variant and copy-number resolution; WES is useful for coding variants but may miss promoter, methylation, and some structural events.
* CMA/SNP array can define aneuploidy/LOH. Karyotype and FISH are not routine first-line tests but may validate selected structural findings. Mitochondrial and repeat-expansion tests are not indicated.
* RNA-seq can detect fusions; methylation arrays can resolve pedA/pedB/adult classes. Liquid biopsy/CSF cell-free tumor DNA remains investigational.

## 11. Outcome and prognosis

CPP generally has excellent long-term control after gross-total resection. aCPP recurrence risk is intermediate and affected by resection completeness and molecular class. CPC historically has approximately **56% 5-year survival**, with substantial neurodevelopmental morbidity among survivors. (thomas2021thegeneticlandscape pages 1-3)

In SJYC07, 13 children younger than three years received maximal surgery plus high-dose-methotrexate-containing therapy: 5-year PFS was **61.5% ±13.5%** and overall survival **68.4% ±13.1%**. Five progressed and died; eight—including five initially high-risk patients—remained progression-free. TP53 status was the only significant prognostic variable: 5-year PFS was **100% wild type versus 28.6% ±17.1% mutant**, *P*=0.012. Extent of resection, metastatic status, and radiotherapy were not statistically significant in this very small cohort and should not be interpreted as proof that they are clinically irrelevant. (liu2021outcomeandmolecular pages 1-2)

Adverse indicators include CPC histology, TP53 mutation—especially biallelic dysfunction—pediatric-B methylation class, dissemination, incomplete local control, TERT-promoter mutation in adults, and selected high-risk copy-number/genomic patterns. Morbidity includes hydrocephalus, neurologic deficits, developmental/cognitive impairment, hearing loss and organ toxicity from chemotherapy, endocrine/vascular effects of radiation, and subsequent cancers in TP53 carriers.

## 12. Treatment and current applications

### Standard strategy

1. **Maximal safe surgical resection** is the cornerstone for all CPTs (NCIt: Surgical Resection; Gross Total Resection). Preoperative planning must account for extreme vascularity, blood volume in infants, and possible staged/second-look surgery.
2. **CPP:** observation after complete resection; reoperate for accessible recurrence/residual disease. Radiotherapy or chemotherapy is reserved for unusual unresectable, recurrent, or disseminated disease.
3. **aCPP:** surgery first. After complete resection, close MRI surveillance is often favored; adjuvant treatment is individualized for residual, recurrent, disseminated, or molecularly high-risk disease.
4. **CPC:** maximal surgery plus multiagent chemotherapy. Regimens commonly include platinum, etoposide, vincristine, cyclophosphamide, and/or high-dose methotrexate; no single universally accepted regimen exists because trials are small.
5. **Radiotherapy:** consider age, dissemination, residual disease, response, and genotype. Avoid or minimize where feasible in germline TP53 carriers because of secondary-cancer risk; proton therapy may reduce integral dose but does not abolish mutagenic risk. (liu2021outcomeandmolecular pages 9-10, liu2021outcomeandmolecular pages 1-2, frebourg2020guidelinesforthe pages 7-8)

SJYC07 demonstrates a real-world protocol: high-dose methotrexate-containing induction, focal irradiation for localized intermediate-risk disease, additional chemotherapy for metastatic disease, and oral antiangiogenic maintenance. Its results support non-myeloablative therapy as a potentially less toxic curative approach for some young children. (liu2021outcomeandmolecular pages 1-2)

### Experimental and precision approaches

* A molecularly guided case targeting mTOR, PDGFRB, FGF2, and HDAC pathways with sirolimus, thalidomide, sunitinib, and vorinostat achieved a reported 92% tumor reduction. This is a single case, not a standard regimen.
* **NCT04994977** tested intra-arterial melphalan/carboplatin/topotecan before second-look surgery. It enrolled one patient and terminated for low accrual; efficacy cannot be inferred. https://clinicaltrials.gov/study/NCT04994977. (NCT04994977 chunk 1)
* **NCT03500991**, HER2-specific locoregional CAR-T for HER2-positive recurrent pediatric CNS tumors including CPC, enrolled ten and is active but not recruiting. https://clinicaltrials.gov/study/NCT03500991. (NCT03500991 chunk 1)
* **NCT04185038**, B7-H3-specific locoregional CAR-T, includes recurrent/refractory CPC within a broader CNS basket; estimated enrollment is 90. CPC-specific efficacy is unproven. https://clinicaltrials.gov/study/NCT04185038. (NCT04185038 chunk 1)
* **NCT03173950**, phase II nivolumab for recurrent rare adult CNS tumors including all CPT subtypes, completed with 133 total basket participants; subtype-specific benefit was not available in the retrieved record. https://clinicaltrials.gov/study/NCT03173950. (NCT03173950 chunk 1)

No approved CPT-specific gene therapy, RNA therapy, CAR-T product, checkpoint inhibitor, or pharmacogenomic dosing rule exists. Suggested NCIt intervention terms include Surgical Resection, Chemotherapy, Radiation Therapy, Proton Beam Radiation Therapy, Methotrexate, Carboplatin, Etoposide, Vincristine, Cyclophosphamide, Topotecan, Melphalan, Nivolumab, and Chimeric Antigen Receptor T-Cell Therapy.

Supportive care includes CSF diversion when required, seizure treatment, transfusion/hemostatic planning, antiemetics, infection prophylaxis, nutrition, audiology, neuropsychology, physical/occupational/speech therapy, school support, and long-term endocrine/second-cancer surveillance.

## 13. Prevention and screening

There is no population screening, vaccine, lifestyle prevention, or chemoprophylaxis for sporadic CPT. Secondary prevention is targeted to **TP53 carriers** and relatives:

* genetic counseling, confirmatory germline testing, and cascade testing;
* annual whole-body and brain MRI beginning in childhood for variants associated with childhood cancer, plus clinical examination and abdominal ultrasound every six months under European TP53 guidance;
* minimize diagnostic and therapeutic ionizing radiation where clinically reasonable;
* discuss reproductive options, including prenatal or preimplantation genetic testing, non-directively.

These measures seek early detection of multiple LFS-spectrum cancers, not merely recurrent CPT. (fortuno2024cancerrisksassociated pages 1-2, frebourg2020guidelinesforthe pages 7-8)

Tertiary prevention comprises complete local control where safe, neuraxis surveillance for CPC/high-risk aCPP, treatment of hydrocephalus, rehabilitation, neurocognitive monitoring, and avoidance of unnecessary radiation in TP53 carriers.

## 14. Other species and natural disease

Naturally occurring CPP/CPC has been reported in dogs (**Canis lupus familiaris**, NCBI Taxon 9615), cats (**Felis catus**, 9685), and rarely horses (**Equus caballus**, 9796). Canine CPC can shed malignant cells into CSF and canine high-grade tumors show microvascular proliferation, desmoplasia, and high proliferative indices. Evidence is primarily case reports and small pathology series; breed predisposition, VBO mappings, incidence, and validated ortholog-specific variants are not established in the retrieved material. There is no transmission or zoonotic potential because CPT is neoplastic, not infectious.

Relevant orthologs include canine/feline/equine **TP53**, **MYC**, **RB1**, **GMNC**, and **MCIDAS**, but NCBI Gene IDs should be obtained directly from current NCBI orthology records before database loading.

## 15. Model organisms

### Genetically engineered mouse models

Conditional stabilized **MycT58A** expression plus **Trp53** deletion in newborn Otx2-lineage/choroid plexus epithelial cells produced CPC with **100% penetrance**; half of mice died by 100 days and all by 150 days, mainly from hydrocephalus. Tumors reproduced human CPC hypercellularity, pleomorphism, vascularity, mitotic activity, and choroid plexus lineage identity. They also showed replication stress, DNA-repair/checkpoint dysregulation, and upregulated **AurA** and **Plk1**, providing a preclinical therapeutic platform. Published February 2018; DOI/URL: https://doi.org/10.1016/j.bbrc.2017.11.192. (nagar2018anewgenetically pages 3-4, nagar2018anewgenetically pages 6-8)

Conditional **Trp53/Rb1** loss and NOTCH/SHH perturbation models reproduce monociliation and GMNC–MCIDAS suppression. Restoring GMNC/MCIDAS reduced proliferation, supporting a differentiation-suppressor mechanism. (li2022disruptionofgmncmcidas pages 1-2)

### Other models and limitations

SV40 large-T-antigen, E2F1, and retinoblastoma-pathway models can generate choroid plexus tumors; Xenopus CRISPR disruption of retinoblastoma-family genes also produces choroid plexus lesions. Cell lines and primary tumor cultures permit drug/pathway studies, but validated patient-derived organoid and xenograft resources remain scarce.

Limitations include engineered lesions that are not universal in humans, compressed latency, species-specific ventricular development and immunity, and incomplete modeling of leptomeningeal dissemination, treatment toxicity, and human developmental outcomes. Models should therefore support—not substitute for—human methylation, genomic, and clinical evidence.

## Knowledge gaps and evidence cautions

* Exact phenotype frequencies, adult natural history, quality-of-life utilities, and comparative treatment effectiveness remain poorly quantified because cohorts are small and retrospective.
* Methylation classes and 2024 single-cell/multiomic discoveries are important for stratification but are not yet independent therapeutic indications.
* No validated environmental cause, protective factor, circulating biomarker, metabolomic/lipidomic signature, or CPT-specific approved targeted therapy exists.
* Trial basket enrollment should not be interpreted as demonstrated CPT efficacy.
* PMID numbers were not exposed for several retrieved full texts; DOI links are therefore supplied rather than inventing PMIDs. Key literature includes Choi et al., published June 2024, https://doi.org/10.1186/s40478-024-01814-y; Hill et al., October 2024, https://doi.org/10.1038/s44318-024-00283-2; Garcia et al., February 2023, https://doi.org/10.1101/mcs.a006245; and Thomas et al., 2021, https://doi.org/10.1093/neuonc/noaa267. (garcia2023genomicprofileof pages 1-2, hill2024singlenucleusrnaseqdissection pages 1-2, choi2024comprehensivemultiomicsanalysis pages 1-2, thomas2021thegeneticlandscape pages 1-3)

References

1. (garcia2023genomicprofileof pages 1-2): Felipe Antonio de Oliveira Garcia, Adriane Feijó Evangelista, Bruna Minniti Mançano, Daniel Antunes Moreno, Gustavo Noriz Berardinelli, Flávia Escremim de Paula, Augusto Perazzolo Antoniazzi, Carlos Almeida Júnior, Ismael Lombardi, Iara Santana, Gustavo Ramos Teixeira, Caio Evangelista Costa, and Rui Manuel Reis. Genomic profile of two brazilian choroid plexus tumors by whole-exome sequencing. Cold Spring Harbor Molecular Case Studies, 9:a006245, Feb 2023. URL: https://doi.org/10.1101/mcs.a006245, doi:10.1101/mcs.a006245. This article has 2 citations and is from a peer-reviewed journal.

2. (li2022disruptionofgmncmcidas pages 1-2): Qun Li, Zhiyuan Han, Navleen Singh, Berta Terré, Ryann M. Fame, Uzayr Arif, Thomas D. Page, Tasneem Zahran, Ahmed Abdeltawab, Yuan Huang, Ping Cao, Jun Wang, Hao Lu, Hart G. W. Lidov, Kameswaran Surendran, Lizhao Wu, James Q. Virga, Ying-Tao Zhao, Ulrich Schüller, Robert J. Wechsler-Reya, Maria K. Lehtinen, Sudipto Roy, Zhongmin Liu, Travis H. Stracker, and Haotian Zhao. Disruption of gmnc-mcidas multiciliogenesis program is critical in choroid plexus carcinoma development. Cell Death and Differentiation, 29:1596-1610, Mar 2022. URL: https://doi.org/10.1038/s41418-022-00950-z, doi:10.1038/s41418-022-00950-z. This article has 18 citations and is from a domain leading peer-reviewed journal.

3. (choi2024comprehensivemultiomicsanalysis pages 1-2): Yeonsong Choi, Seung Ah Choi, Eun Jung Koh, Ilsun Yun, Suhyun Park, Sungwon Jeon, Yeonkyung Kim, Sangbeen Park, Donggeon Woo, Ji Hoon Phi, Sung-Hye Park, Dong-Seok Kim, Se Hoon Kim, Jung Won Choi, Ji Won Lee, Tae-Young Jung, Jong Bhak, Semin Lee, and Seung-Ki Kim. Comprehensive multiomics analysis reveals distinct differences between pediatric choroid plexus papilloma and carcinoma. Acta Neuropathologica Communications, Jun 2024. URL: https://doi.org/10.1186/s40478-024-01814-y, doi:10.1186/s40478-024-01814-y. This article has 5 citations and is from a peer-reviewed journal.

4. (thomas2021thegeneticlandscape pages 1-3): Christian Thomas, Patrick Soschinski, Melissa Zwaig, Spyridon Oikonomopoulos, Konstantin Okonechnikov, Kristian W Pajtler, Martin Sill, Leonille Schweizer, Arend Koch, Julia Neumann, Ulrich Schüller, Felix Sahm, Laurèl Rauschenbach, Kathy Keyvani, Martin Proescholdt, Markus J Riemenschneider, Jochen Segewiß, Christian Ruckert, Oliver Grauer, Camelia-Maria Monoranu, Katrin Lamszus, Annarita Patrizi, Uwe Kordes, Reiner Siebert, Marcel Kool, Jiannis Ragoussis, William D Foulkes, Werner Paulus, Barbara Rivera, and Martin Hasselblatt. The genetic landscape of choroid plexus tumors in children and adults. Neuro-oncology, 23:650-660, Nov 2021. URL: https://doi.org/10.1093/neuonc/noaa267, doi:10.1093/neuonc/noaa267. This article has 66 citations and is from a domain leading peer-reviewed journal.

5. (liu2021outcomeandmolecular pages 1-2): Anthony P Y Liu, Gang Wu, Brent A Orr, Tong Lin, Jason M Ashford, Johnnie K Bass, Daniel C Bowers, Tim Hassall, Paul G Fisher, Daniel J Indelicato, Paul Klimo, Frederick Boop, Heather Conklin, Arzu Onar-Thomas, Thomas E Merchant, David W Ellison, Amar Gajjar, and Giles W Robinson. Outcome and molecular analysis of young children with choroid plexus carcinoma treated with non-myeloablative therapy: results from the sjyc07 trial. Neuro-oncology Advances, Dec 2021. URL: https://doi.org/10.1093/noajnl/vdaa168, doi:10.1093/noajnl/vdaa168. This article has 28 citations and is from a peer-reviewed journal.

6. (hill2024singlenucleusrnaseqdissection pages 1-2): Anthony D Hill, Konstantin Okonechnikov, Marla K Herr, Christian Thomas, Supat Thongjuea, Martin Hasselblatt, and Annarita Patrizi. Single-nucleus rna-seq dissection of choroid plexus tumor cell heterogeneity. The EMBO Journal, 43:6766-6791, Oct 2024. URL: https://doi.org/10.1038/s44318-024-00283-2, doi:10.1038/s44318-024-00283-2. This article has 4 citations.

7. (garcia2023genomicprofileof pages 2-5): Felipe Antonio de Oliveira Garcia, Adriane Feijó Evangelista, Bruna Minniti Mançano, Daniel Antunes Moreno, Gustavo Noriz Berardinelli, Flávia Escremim de Paula, Augusto Perazzolo Antoniazzi, Carlos Almeida Júnior, Ismael Lombardi, Iara Santana, Gustavo Ramos Teixeira, Caio Evangelista Costa, and Rui Manuel Reis. Genomic profile of two brazilian choroid plexus tumors by whole-exome sequencing. Cold Spring Harbor Molecular Case Studies, 9:a006245, Feb 2023. URL: https://doi.org/10.1101/mcs.a006245, doi:10.1101/mcs.a006245. This article has 2 citations and is from a peer-reviewed journal.

8. (garcia2023genomicprofileof pages 5-8): Felipe Antonio de Oliveira Garcia, Adriane Feijó Evangelista, Bruna Minniti Mançano, Daniel Antunes Moreno, Gustavo Noriz Berardinelli, Flávia Escremim de Paula, Augusto Perazzolo Antoniazzi, Carlos Almeida Júnior, Ismael Lombardi, Iara Santana, Gustavo Ramos Teixeira, Caio Evangelista Costa, and Rui Manuel Reis. Genomic profile of two brazilian choroid plexus tumors by whole-exome sequencing. Cold Spring Harbor Molecular Case Studies, 9:a006245, Feb 2023. URL: https://doi.org/10.1101/mcs.a006245, doi:10.1101/mcs.a006245. This article has 2 citations and is from a peer-reviewed journal.

9. (fortuno2024cancerrisksassociated pages 1-2): Cristina Fortuno, Bing-Jian Feng, Courtney Carroll, Giovanni Innella, Wendy Kohlmann, Conxi Lázaro, Joan Brunet, Lidia Feliubadaló, Silvia Iglesias, Mireia Menéndez, Alex Teulé, Mandy L. Ballinger, David M. Thomas, Ainsley Campbell, Mike Field, Marion Harris, Judy Kirk, Nicholas Pachter, Nicola Poplawski, Rachel Susman, Kathy Tucker, Mathew Wallis, Rachel Williams, Elisa Cops, David Goldgar, Paul A. James, Amanda B. Spurdle, David Amor, Lesley Andrews, Yoland Antill, Rosemary Balleine, Jonathan Beesley, Ian Bennett, Michael Bogwitz, Simon Bodek, Leon Botes, Meagan Brennan, Melissa Brown, Michael Buckley, Jo Burke, Phyllis Butow, Liz Caldon, Ian Campbell, Michelle Cao, Anannya Chakrabarti, Deepa Chauhan, Manisha Chauhan, Georgia Chenevix-Trench, Alice Christian, Paul Cohen, Alison Colley, Ashley Crook, James Cui, Eliza Courtney, Margaret Cummings, Sarah-Jane Dawson, Anna deFazio, Martin Delatycki, Rebecca Dickson, Joanne Dixon, Ted Edkins, Stacey Edwards, Gelareh Farshid, Andrew Fellows, Georgina Fenton, Michael Field, James Flanagan, Peter Fong, Laura Forrest, Stephen Fox, Juliet French, Michael Friedlander, Clara Gaff, Mike Gattas, Peter George, Sian Greening, Marion Harris, Stewart Hart, Nick Hayward, John Hopper, Cass Hoskins, Clare Hunt, Paul James, Mark Jenkins, Alexa Kidd, Judy Kirk, Jessica Koehler, James Kollias, Sunil Lakhani, Mitchell Lawrence, Jason Lee, Shuai Li, Geoff Lindeman, Jocelyn Lippey, Lara Lipton, Liz Lobb, Sherene Loi, Graham Mann, Deborah Marsh, Sue Anne McLachlan, Bettina Meiser, Roger Milne, Sophie Nightingale, Shona O'Connell, Sarah O'Sullivan, David Gallego Ortega, Nick Pachter, Jia-Min Pang, Gargi Pathak, Briony Patterson, Amy Pearn, Kelly Phillips, Ellen Pieper, Susan Ramus, Edwina Rickard, Bridget Robinson, Mona Saleh, Anita Skandarajah, Elizabeth Salisbury, Christobel Saunders, Jodi Saunus, Peter Savas, Rodney Scott, Clare Scott, Adrienne Sexton, Joanne Shaw, Andrew Shelling, Shweta Srinivasa, Peter Simpson, Melissa Southey, Amanda Spurdle, Jessica Taylor, Renea Taylor, Heather Thorne, Alison Trainer, Kathy Tucker, Jane Visvader, Logan Walker, Rachael Williams, Ingrid Winship, Mary Ann Young, and Milita Zaheed. Cancer risks associated with tp53 pathogenic variants: maximum likelihood analysis of extended pedigrees for diagnosis of first cancers beyond the li-fraumeni syndrome spectrum. JCO Precision Oncology, Feb 2024. URL: https://doi.org/10.1200/po.23.00453, doi:10.1200/po.23.00453. This article has 38 citations and is from a peer-reviewed journal.

10. (liu2021outcomeandmolecular pages 9-10): Anthony P Y Liu, Gang Wu, Brent A Orr, Tong Lin, Jason M Ashford, Johnnie K Bass, Daniel C Bowers, Tim Hassall, Paul G Fisher, Daniel J Indelicato, Paul Klimo, Frederick Boop, Heather Conklin, Arzu Onar-Thomas, Thomas E Merchant, David W Ellison, Amar Gajjar, and Giles W Robinson. Outcome and molecular analysis of young children with choroid plexus carcinoma treated with non-myeloablative therapy: results from the sjyc07 trial. Neuro-oncology Advances, Dec 2021. URL: https://doi.org/10.1093/noajnl/vdaa168, doi:10.1093/noajnl/vdaa168. This article has 28 citations and is from a peer-reviewed journal.

11. (frebourg2020guidelinesforthe pages 7-8): T. Frébourg, Svetlana Bajalica Lagercrantz, Carla Oliveira, R. Mágenheim, D. Evans, Nicoline Marjolijn Marleen Rianne Rolf Gareth Emma Marc Eam Hoogerbrugge Ligtenberg Kets Oostenbrink Sijmons E, N. Hoogerbrugge, M. Ligtenberg, M. Kets, R. Oostenbrink, R. Sijmons, G. Evans, E. Woodward, M. Tischkowitz, E. Maher, R. Ferner, S. Aretz, I. Spier, V. Steinke-Lange, E. Holinski-Feder, E. Schröck, T. Frébourg, C. Houdayer, C. Colas, P. Wolkenstein, V. Bours, E. Legius, B. Poppe, K. Claes, R. de Putter, I. Guillermo, G. Capellá, J. B. Vidal, C. Lázaro, J. Balmaña, H. S. Hernández, Carla Oliveira, M. Teixeira, S. Bajalica-Lagercrantz, E. Tham, J. Lubiński, K. Ertmańska, B. Melegh, M. Krajc, A. Blatnik, S. Peltonen, and M. Hietala. Guidelines for the li–fraumeni and heritable tp53-related cancer syndromes. European Journal of Human Genetics, 28:1379-1386, May 2020. URL: https://doi.org/10.1038/s41431-020-0638-4, doi:10.1038/s41431-020-0638-4. This article has 405 citations and is from a domain leading peer-reviewed journal.

12. (hill2024singlenucleusrnaseqdissection pages 3-4): Anthony D Hill, Konstantin Okonechnikov, Marla K Herr, Christian Thomas, Supat Thongjuea, Martin Hasselblatt, and Annarita Patrizi. Single-nucleus rna-seq dissection of choroid plexus tumor cell heterogeneity. The EMBO Journal, 43:6766-6791, Oct 2024. URL: https://doi.org/10.1038/s44318-024-00283-2, doi:10.1038/s44318-024-00283-2. This article has 4 citations.

13. (OpenTargets Search: choroid plexus carcinoma,choroid plexus papilloma-TP53): Open Targets Query (choroid plexus carcinoma,choroid plexus papilloma-TP53, 16 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

14. (gargallo2020li–fraumenisyndromeheterogeneity pages 7-8): P. Gargallo, Y. Yáñez, V. Segura, A. Juan, B. Torres, J. Balaguer, S. Oltra, V. Castel, and A. Cañete. Li–fraumeni syndrome heterogeneity. Clinical and Translational Oncology, 22:978-988, Nov 2020. URL: https://doi.org/10.1007/s12094-019-02236-2, doi:10.1007/s12094-019-02236-2. This article has 52 citations and is from a peer-reviewed journal.

15. (safaee2013choroidplexuspapillomas pages 1-2): Michael Safaee, Michael C. Oh, Orin Bloch, Matthew Z. Sun, Gurvinder Kaur, Kurtis I. Auguste, Tarik Tihan, and Andrew T. Parsa. Choroid plexus papillomas: advances in molecular biology and understanding of tumorigenesis. Neuro-oncology, 15 3:255-67, Mar 2013. URL: https://doi.org/10.1093/neuonc/nos289, doi:10.1093/neuonc/nos289. This article has 108 citations and is from a domain leading peer-reviewed journal.

16. (bittar2021clinicalandmolecular pages 9-10): Camila Matzenbacher Bittar, Yasminne Marinho de Araújo Rocha, Igor Araujo Vieira, Clévia Rosset, Tiago Finger Andreis, Ivaine Tais Sauthier Sartor, Osvaldo Artigalás, Cristina B. O. Netto, Barbara Alemar, Gabriel S. Macedo, and Patricia Ashton-Prolla. Clinical and molecular characterization of patients fulfilling chompret criteria for li-fraumeni syndrome in southern brazil. PLoS ONE, 16:e0251639, Sep 2021. URL: https://doi.org/10.1371/journal.pone.0251639, doi:10.1371/journal.pone.0251639. This article has 10 citations and is from a peer-reviewed journal.

17. (giacomazzi2015pediatriccancerand pages 1-2): Cristina Rossi Giacomazzi, Juliana Giacomazzi, Cristina B.O. Netto, Patricia Santos-Silva, Simone Geiger Selistre, Ana Luiza Maia, Viviane Ziebell de Oliveira, Suzi Alves Camey, José Roberto Goldim, and Patricia Ashton-Prolla. Pediatric cancer and li-fraumeni/li-fraumeni-like syndromes: a review for the pediatrician. Revista da Associacao Medica Brasileira, 61 3:282-9, Jun 2015. URL: https://doi.org/10.1590/1806-9282.61.03.282, doi:10.1590/1806-9282.61.03.282. This article has 29 citations.

18. (nagar2018anewgenetically pages 6-8): Salsabiel El Nagar, Frederique Zindy, Charlotte Moens, Luc Martin, Damien Plassard, Martine F. Roussel, Thomas Lamonerie, and Nathalie Billon. A new genetically engineered mouse model of choroid plexus carcinoma. Biochemical and biophysical research communications, 496 2:568-574, Feb 2018. URL: https://doi.org/10.1016/j.bbrc.2017.11.192, doi:10.1016/j.bbrc.2017.11.192. This article has 14 citations and is from a peer-reviewed journal.

19. (NCT04994977 chunk 1):  Intra-Arterial Chemotherapy for Newly Diagnosed, Residual, or Recurrent Atypical Choroid Plexus Papilloma and Choroid Plexus Carcinoma Prior to Second-Look Surgery. Weill Medical College of Cornell University. 2023. ClinicalTrials.gov Identifier: NCT04994977

20. (NCT03500991 chunk 1): Colleen Annesley. HER2-specific CAR T Cell Locoregional Immunotherapy for HER2-positive Recurrent/Refractory Pediatric CNS Tumors. Seattle Children's Hospital. 2018. ClinicalTrials.gov Identifier: NCT03500991

21. (NCT04185038 chunk 1): Colleen Annesley. Study of B7-H3-Specific CAR T Cell Locoregional Immunotherapy for Diffuse Intrinsic Pontine Glioma/Diffuse Midline Glioma and Recurrent or Refractory Pediatric Central Nervous System Tumors. Seattle Children's Hospital. 2019. ClinicalTrials.gov Identifier: NCT04185038

22. (NCT03173950 chunk 1):  Immune Checkpoint Inhibitor Nivolumab in People With Recurrent Select Rare CNS Cancers. National Cancer Institute (NCI). 2017. ClinicalTrials.gov Identifier: NCT03173950

23. (nagar2018anewgenetically pages 3-4): Salsabiel El Nagar, Frederique Zindy, Charlotte Moens, Luc Martin, Damien Plassard, Martine F. Roussel, Thomas Lamonerie, and Nathalie Billon. A new genetically engineered mouse model of choroid plexus carcinoma. Biochemical and biophysical research communications, 496 2:568-574, Feb 2018. URL: https://doi.org/10.1016/j.bbrc.2017.11.192, doi:10.1016/j.bbrc.2017.11.192. This article has 14 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Choroid_Plexus_Neoplasm-deep-research-falcon_artifacts/artifact-00.md)