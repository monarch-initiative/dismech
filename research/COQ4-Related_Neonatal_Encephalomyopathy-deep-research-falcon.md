---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T18:43:44.390245'
end_time: '2026-08-01T18:51:32.672348'
duration_seconds: 468.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: COQ4-Related Neonatal Encephalomyopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 12
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: COQ4-Related_Neonatal_Encephalomyopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** COQ4-Related Neonatal Encephalomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **COQ4-Related Neonatal Encephalomyopathy** covering all of the
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
- **Disease Name:** COQ4-Related Neonatal Encephalomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **COQ4-Related Neonatal Encephalomyopathy** covering all of the
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


# COQ4-Related Neonatal Encephalomyopathy: Disease Characteristics Report

## Executive summary

COQ4-related neonatal encephalomyopathy is the severe, prenatal/neonatal end of **primary coenzyme Q10 deficiency type 7 (COQ10D7)**, an autosomal-recessive mitochondrial disorder caused by biallelic pathogenic variants in **COQ4**. The defining biology is failure of mitochondrial coenzyme-Q biosynthesis, with reduced CoQ10, accumulation of the intermediate 6-demethoxyubiquinone (6-DMQ), impaired respiratory-chain electron transfer, and preferential injury to the developing brain, skeletal muscle, heart, and respiratory system. The neonatal phenotype commonly comprises prenatal brain abnormalities, profound hypotonia, epileptic encephalopathy, respiratory failure, feeding failure, lactic acidosis, cerebellar hypoplasia/atrophy, and cardiomyopathy. Prognosis is poor: a 2024 aggregation of 24 neonatal cases found mean survival of **60.0 ± 98.0 days** and 20 deaths, although ascertainment and publication bias are substantial. Oral CoQ10 is used immediately because the disorder is biochemically actionable, but established neonatal CNS disease usually responds incompletely. (pan2024thespectrumof pages 1-2, laugwitz2022humancoq4deficiency pages 1-3, laugwitz2022humancoq4deficiency pages 8-10)

The most useful quantitative evidence is summarized below.

| domain | best quantitative finding | interpretation | source/date/DOI or PMID if available |
|---|---:|---|---|
| Neonatal cohort size | 24 neonatal-onset cases total (4 new + 20 literature cases) | Best current neonatal-focused summary of COQ4 disease burden is still based on small case aggregation, underscoring rarity and likely ascertainment bias (pan2024thespectrumof pages 1-2) | Pan et al., *Front Pediatr* (Sep 2024), doi:10.3389/fped.2024.1410133 |
| Neonatal mortality/survival | Mean survival 60.0 ± 98.0 days; mortality 75% in Chinese cases (9/12) and 91.7% in non-Chinese cases (11/12), P=0.27 | Neonatal COQ4 disease has very poor short-term survival overall, with no statistically significant regional mortality difference in this review (pan2024thespectrumof pages 1-2) | Pan et al., *Front Pediatr* (Sep 2024), doi:10.3389/fped.2024.1410133 |
| Neonatal biochemical abnormality | Hyperlactatemia in 75% (18/24) | Elevated lactate is common and useful diagnostically, but not universal; absence of lactate elevation does not exclude disease (pan2024thespectrumof pages 1-2) | Pan et al., *Front Pediatr* (Sep 2024), doi:10.3389/fped.2024.1410133 |
| Neonatal genetic diagnosis | 20/24 diagnosed by whole-exome sequencing | WES is the dominant real-world diagnostic route for neonatal COQ4 disease (pan2024thespectrumof pages 1-2) | Pan et al., *Front Pediatr* (Sep 2024), doi:10.3389/fped.2024.1410133 |
| Prenatal risk signals | Prenatal abnormalities more frequent in preterm than full-term infants: 66.7% vs 16.7%, P=0.02 | Supports prenatal/perinatal disease onset in the severest neonatal presentations (pan2024thespectrumof pages 1-2) | Pan et al., *Front Pediatr* (Sep 2024), doi:10.3389/fped.2024.1410133 |
| Largest human cohort | 44 individuals from 36 families; 23 variants identified | COQ4 deficiency is clinically heterogeneous but now sufficiently characterized to define subtypes (laugwitz2022humancoq4deficiency pages 1-3) | Laugwitz et al., *J Med Genet* (Oct 2022), doi:10.1136/jmedgenet-2021-107729 |
| Core phenotype frequencies | Respiratory distress 24/34; feeding difficulties 20/28; hypertrophic cardiomyopathy 15/35; hyperlactataemia 22/31 | Multisystem neonatal/infantile disease commonly affects brain, cardiorespiratory status, feeding, and metabolism (laugwitz2022humancoq4deficiency pages 7-8) | Laugwitz et al., *J Med Genet* (Oct 2022), doi:10.1136/jmedgenet-2021-107729 |
| Neuroimaging frequencies | Cerebral atrophy 18 patients; cerebellar atrophy 15/36; cerebellar hypoplasia 10 cases; stroke-like lesions 8 patients; delayed myelination in ~50% of MRI studies | Neuroimaging often shows a mitochondrial encephalopathy pattern, with cerebellar involvement especially prominent in severe neonatal disease (laugwitz2022humancoq4deficiency pages 7-8, laugwitz2022humancoq4deficiency pages 10-12) | Laugwitz et al., *J Med Genet* (Oct 2022), doi:10.1136/jmedgenet-2021-107729 |
| Clinical subtypes | 3 patterns: type 1 neonatal brain anomalies/epileptic encephalopathy; type 2 stroke-like lesions; type 3 moderate stable disease | Helps stratify prognosis: type 1 is most severe and often neonatal, type 3 relatively milder (laugwitz2022humancoq4deficiency pages 1-3, laugwitz2022humancoq4deficiency pages 10-12) | Laugwitz et al., *J Med Genet* (Oct 2022), doi:10.1136/jmedgenet-2021-107729 |
| Survival in broader cohort | Only 5/44 reached adulthood | Confirms high childhood mortality, especially in early-onset encephalopathic forms (laugwitz2022humancoq4deficiency pages 8-10) | Laugwitz et al., *J Med Genet* (Oct 2022), doi:10.1136/jmedgenet-2021-107729 |
| Treatment exposure and response | CoQ10 given to 29 patients at 15–60 mg/kg/day; 16/29 no response; 12/29 limited improvement/stabilization | Oral CoQ10 is widely used in practice but usually yields modest or absent neurologic benefit in COQ4 disease (laugwitz2022humancoq4deficiency pages 7-8) | Laugwitz et al., *J Med Genet* (Oct 2022), doi:10.1136/jmedgenet-2021-107729 |
| Current treatment recommendation | Oral CoQ10 should be started immediately in suspected CoQ biosynthesis disorders and titrated to at least 30 mg/kg/day after genetic confirmation; one COQ4 case also received idebenone 20 mg/kg/day | Expert practice favors early empiric high-dose CoQ10 despite limited evidence for reversing advanced neonatal neurodegeneration (wahedi2024clinicalfeaturesbiochemistry pages 10-10) | Wahedi et al., *Neurol Genet* (Dec 2024), doi:10.1212/NXG.0000000000200209 |
| Cellular mechanism | Patient fibroblasts: reduced cellular CoQ10 in most lines; elevated 6-demethoxyubiquinone (6-DMQ); severe galactose-growth defect with partial rescue by CoQ10 | Strong in vitro evidence that COQ4 variants impair CoQ biosynthesis and mitochondrial energy metabolism; exogenous CoQ10 only partially corrects the defect (laugwitz2022humancoq4deficiency pages 21-23) | Laugwitz et al., *J Med Genet* (Oct 2022), doi:10.1136/jmedgenet-2021-107729 |
| Protein-level mechanism | COQ4 protein reduced in patient fibroblasts, often with secondary reductions in COQ7/COQ9 | Supports the model that COQ4 helps stabilize the CoQ biosynthetic complex (Q-synthome), so deficiency destabilizes the pathway beyond a single enzymatic step (laugwitz2022humancoq4deficiency pages 21-23, laugwitz2022humancoq4deficiency pages 7-8, xie2022primarycoenzymeq10 pages 1-2) | Laugwitz et al. 2022; Xie et al., *Front Genet* (Jan 2022), doi:10.3389/fgene.2021.776807 |


*Table: This table condenses the strongest quantitative evidence for COQ4-related neonatal encephalomyopathy across neonatal case aggregation, the largest human cohort, current treatment practice, and cellular mechanism studies. It is useful for rapidly extracting disease severity, diagnostic yield, treatment response, and mechanistic support from the available literature.*

---

## 1. Disease information

### Definition and scope

The disease is a **Mendelian primary mitochondrial CoQ10-biosynthesis disorder**. “COQ4-related neonatal encephalomyopathy” is best treated as a severe age-defined presentation within the broader COQ4-deficiency spectrum, rather than as a completely separate molecular disease. The largest systematic cohort separated the spectrum into: (1) prenatal/neonatal brain anomalies and epileptic encephalopathy; (2) an intermediate, stroke-like phenotype; and (3) a moderate, relatively stable phenotype. (laugwitz2022humancoq4deficiency pages 1-3, laugwitz2022humancoq4deficiency pages 10-12)

### Identifiers and synonyms

- **MONDO:** **MONDO:0014562**, *neonatal encephalomyopathy–cardiomyopathy–respiratory distress syndrome*.
- **OMIM/MIM disease:** **616227**, generally indexed as *Coenzyme Q10 deficiency, primary, 7 (COQ10D7)*.
- **Gene:** **COQ4**, Ensembl **ENSG00000167113**; approved name *coenzyme Q4*.
- Common names: **COQ4 deficiency**, **primary coenzyme Q10 deficiency 7**, **COQ10D7**, **COQ4-related mitochondrial disease**, **COQ4-related encephalomyopathy**, and **neonatal encephalomyopathy–cardiomyopathy–respiratory distress syndrome**. Open Targets associates MONDO:0014562 specifically with COQ4 and cites primary literature including PMIDs **25658047, 26741492, 27604308, 30659264, 31396399, 33215859, 33704555, 36047608,** and **38013626**. (OpenTargets Search: primary coenzyme Q10 deficiency 7-COQ4)
- No unique, disease-specific ICD-10, ICD-11, or MeSH code was established in the retrieved evidence; coding ordinarily falls under mitochondrial-metabolism/encephalomyopathy categories.

The evidence is overwhelmingly **aggregated disease-level literature**, assembled from published case reports, family series, and research cohorts—not population-scale EHR data. The 2022 cohort contained 44 individuals from 36 families, including 16 newly reported patients. (laugwitz2022humancoq4deficiency pages 1-3)

---

## 2. Etiology and risk factors

### Causal factor

The necessary cause is **biallelic germline COQ4 dysfunction**, usually homozygous or compound-heterozygous sequence variants, inherited in an autosomal-recessive manner. Reported classes include missense, nonsense, frameshift, splice-altering, and larger deletion alleles. Examples from primary literature include p.Leu82Gln/p.Arg158Gln and homozygous p.Pro64Ser; a chromosome 9q34.13 deletion encompassing COQ4 has also been described. (berardo2020redefininginfantileonsetmultisystem pages 4-6, sondheimer2017novelrecessivemutations pages 4-4)

### Genotype–phenotype observations

- Truncating-plus-missense genotypes were enriched in the severe type-1 phenotype; no individuals with two unequivocal loss-of-function alleles were identified, suggesting complete COQ4 loss may be embryonically nonviable. (laugwitz2022humancoq4deficiency pages 10-12)
- A proposed exon relationship places variants in exons 1–4 with later, milder, more treatment-responsive disease and variants in exons 5–7 with early severe disease and early death. This remains an observational—not deterministic—rule. (xie2022primarycoenzymeq10 pages 1-2)
- **c.370G>A (p.Gly124Ser; historically reported as p.G124S)** is enriched in East Asian/Chinese families and has been associated with intermediate multisystem disease. It should be regarded as a population-enriched pathogenic allele, not proof that southern Chinese ancestry alone causes disease. (berardo2020redefininginfantileonsetmultisystem pages 4-6, xie2022primarycoenzymeq10 pages 1-2)

### Other risk, protective, and gene–environment factors

- **Family history and parental consanguinity** increase the probability of biallelic inheritance; the recurrence risk is 25% for each pregnancy when both parents are heterozygous carriers.
- No validated environmental, infectious, toxic, occupational, lifestyle, age-related, or sex-specific cause exists. Sex was not associated with severity in the available analysis. (xie2022primarycoenzymeq10 pages 1-2)
- No reproducible protective allele, modifier gene, environmental protective factor, or specific gene–environment interaction is established.
- Claims that epigenetic factors explain intrafamilial variation remain speculative; there is no validated COQ4-specific methylation or chromatin signature. (laugwitz2022humancoq4deficiency pages 10-12)

---

## 3. Phenotypes

### Major neonatal manifestations

| Phenotype | Character/course and frequency | Suggested HPO term |
|---|---|---|
| Neonatal encephalopathy | Severe from birth or first days; frequently progressive | Neonatal encephalopathy, **HP:0012768** |
| Seizures/epileptic encephalopathy | Neonatal seizures, recurrent seizures, sometimes status epilepticus | Seizure **HP:0001250**; status epilepticus **HP:0002133** |
| Global developmental impairment | Profound in survivors; regression may occur | Global developmental delay **HP:0001263**; developmental regression **HP:0002376** |
| Hypotonia/weakness | Severe axial or generalized hypotonia, decreased movement/cry | Muscular hypotonia **HP:0001252** |
| Respiratory distress/failure | 24/34 in the broader cohort; often ventilatory dependence | Respiratory distress **HP:0002098**; respiratory failure **HP:0002878** |
| Feeding difficulty | 20/28; may require tube feeding | Feeding difficulties **HP:0011968** |
| Cardiomyopathy | Hypertrophic cardiomyopathy in 15/35; may cause shock | Hypertrophic cardiomyopathy **HP:0001639**; cardiogenic shock **HP:0030149** |
| Hyperlactatemia/lactic acidosis | 22/31 in the broader cohort and 18/24 neonatal cases; not universal | Lactic acidosis **HP:0003128**; increased serum lactate **HP:0011964** |
| Cerebellar abnormality | Hypoplasia, atrophy, or cystic degeneration; often prenatal in type 1 | Cerebellar hypoplasia **HP:0001321**; cerebellar atrophy **HP:0001272** |
| Cerebral atrophy/delayed myelination | Cerebral atrophy in 18; delayed myelination in about half of MRI studies | Cerebral atrophy **HP:0002059**; delayed CNS myelination **HP:0002188** |
| Movement disorder | Ataxia, dystonia, spasticity, tremor mainly in longer survivors | Ataxia **HP:0001251**; dystonia **HP:0001332**; spasticity **HP:0001257** |
| Visual/oculomotor impairment | 17/22 in the broader cohort | Visual impairment **HP:0000505**; abnormal eye movements **HP:0012547** |
| Stroke-like episodes | Type-2 disease; parieto-occipital lesions, 8–9 reported patients | Stroke-like episode **HP:0002401** |

The frequencies come from a clinically heterogeneous, referral-enriched cohort and should not be interpreted as population prevalence. (laugwitz2022humancoq4deficiency pages 8-10, laugwitz2022humancoq4deficiency pages 7-8)

### Quality of life

No COQ4-specific EQ-5D, SF-36, PROMIS, or caregiver-burden study was found. Nevertheless, profound developmental disability, refractory epilepsy, ventilatory and feeding support, movement disability, visual impairment, recurrent hospitalization, and early mortality imply extreme patient and caregiver burden. This is a clinical inference rather than a formally measured outcome. (laugwitz2022humancoq4deficiency pages 8-10)

---

## 4. Genetic and molecular information

**COQ4** encodes a mitochondrial protein required for integrity/stability of the multisubunit CoQ biosynthetic complex (“Q-synthome”); it is not simply a freely acting metabolic enzyme. Reduced COQ4 protein can secondarily lower COQ7 and COQ9, explaining disruption across the pathway. (berardo2020redefininginfantileonsetmultisystem pages 4-6, laugwitz2022humancoq4deficiency pages 21-23, laugwitz2022humancoq4deficiency pages 7-8)

Variants are **constitutional/germline**, not somatic cancer mutations. Pathogenic interpretation should follow ACMG/AMP criteria using segregation, rarity in population databases, predicted consequence, patient biochemical phenotype, and functional complementation/rescue where available. Exact gnomAD frequencies and ClinVar classifications are variant- and transcript-specific and should be imported directly from current ClinVar/gnomAD records rather than generalized from case literature.

The dominant functional consequence is **loss of function or hypomorphic loss of function** through reduced protein stability or impaired Q-synthome assembly. Normal COQ4 mRNA with low protein in fibroblasts supports post-transcriptional instability/turnover for some alleles. Missense alleles can leave residual function; complete biallelic loss may be incompatible with survival. (laugwitz2022humancoq4deficiency pages 8-10, laugwitz2022humancoq4deficiency pages 10-12)

No validated modifier gene, disease-specific epigenetic signature, recurrent pathogenic chromosomal rearrangement other than rare deletions encompassing COQ4, or somatic mechanism has been demonstrated.

---

## 5. Environmental information

No toxin, radiation exposure, pollutant, occupation, smoking, alcohol use, diet, exercise pattern, or infectious agent has been shown to cause COQ4 deficiency. Environmental stressors such as fasting, fever, hypoxia, or intercurrent infection may plausibly worsen mitochondrial energy failure, but a COQ4-specific interaction has not been quantified. Accordingly, this is a genetic metabolic disease and not an infectious, lifestyle, or environmentally acquired condition.

---

## 6. Mechanism and pathophysiology

### Causal chain

1. **Biallelic COQ4 variant** → reduced/stable-but-dysfunctional COQ4 protein.
2. **Q-synthome destabilization** → secondary reduction of other biosynthetic proteins, including COQ7/COQ9.
3. **Defective CoQ synthesis** → low CoQ10 and accumulation of **6-DMQ**.
4. **Electron-transfer failure** between respiratory-chain complexes I/II and III → decreased oxidative phosphorylation and ATP availability.
5. **Compensatory glycolysis** → elevated lactate/lactic acidosis.
6. Loss of CoQ-dependent antioxidant/redox functions may increase oxidative membrane injury and vulnerability to ferroptotic processes; CoQ also participates in pyrimidine metabolism, fatty-acid oxidation, and respiratory-complex stabilization. These broader effects are biologically credible, but their relative contribution in neonatal COQ4 disease has not been quantified. (sondheimer2017novelrecessivemutations pages 4-4, laugwitz2022humancoq4deficiency pages 21-23, xie2022primarycoenzymeq10 pages 1-2)
7. High-energy tissues fail first: developing neurons and glia, myocardium, skeletal/respiratory muscle → seizures, cerebral/cerebellar injury, hypotonia, cardiomyopathy, respiratory failure, and death.

### Direct evidence

Patient fibroblasts showed reduced COQ4 protein, reduced CoQ10 in most lines, 6-DMQ accumulation, and marked growth failure when forced to rely on oxidative metabolism in galactose medium. CoQ10 only partially rescued viability. Muscle studies found low CoQ10 and impaired complex I, II+III, III, and sometimes IV activities. (sondheimer2017novelrecessivemutations pages 4-4, laugwitz2022humancoq4deficiency pages 21-23)

Suggested annotations include:

- **GO biological process:** coenzyme Q biosynthetic process; mitochondrial electron transport, NADH to ubiquinone; mitochondrial ATP synthesis coupled electron transport; cellular response to oxidative stress; regulation of ferroptosis.
- **GO cellular component:** mitochondrion **GO:0005739**; mitochondrial inner membrane **GO:0005743**; respiratory-chain complex/Q-synthome.
- **Cell Ontology:** neuron **CL:0000540**, astrocyte **CL:0000127**, oligodendrocyte **CL:0000128**, cardiomyocyte **CL:0000746**, skeletal muscle cell **CL:0000188**.
- **CHEBI:** coenzyme Q10/ubiquinone-10; ubiquinol-10; lactate; 6-demethoxyubiquinone.

No disease-specific single-cell, spatial-transcriptomic, proteomic, lipidomic, or integrated multi-omic atlas is established. Existing molecular profiling is chiefly targeted immunoblotting, respiratory-chain enzymology, and CoQ/intermediate measurement.

---

## 7. Anatomical structures affected

The primary systems are the **central nervous system**, **skeletal/respiratory muscle**, and **heart**. Brain MRI shows bilateral or diffuse cerebral and cerebellar involvement, delayed myelination, thalamic lesions, and—particularly in type 2—parasagittal/parieto-occipital stroke-like lesions. Cerebellar hypoplasia may originate prenatally. (laugwitz2022humancoq4deficiency pages 21-23, laugwitz2022humancoq4deficiency pages 10-12)

Suggested anatomy terms include brain (**UBERON:0000955**), cerebral cortex (**UBERON:0000956**), cerebellum (**UBERON:0002037**), thalamus (**UBERON:0001897**), heart (**UBERON:0000948**), myocardium, skeletal muscle tissue (**UBERON:0001134**), and mitochondrion (**GO:0005739**). Imaging abnormalities are generally bilateral/diffuse rather than consistently lateralized. Renal disease, prominent in several other CoQ-biosynthesis defects, is not a defining COQ4 feature. (berardo2020redefininginfantileonsetmultisystem pages 4-6)

---

## 8. Temporal development

Type-1 disease may begin prenatally with cerebellar hypoplasia, abnormal fetal imaging, prematurity, or impaired fetal well-being. Clinical deterioration is often acute at birth or during the first days, followed by rapidly progressive seizures, respiratory failure, feeding failure, cardiomyopathy, and severe neurodevelopmental injury. In the neonatal review, prenatal abnormalities were more frequent among preterm than term infants (**66.7% versus 16.7%, P=0.02**). (pan2024thespectrumof pages 1-2, laugwitz2022humancoq4deficiency pages 10-12)

The broader spectrum is lifelong and variable: type 2 can progress through stroke-like episodes and movement disorder into adulthood, whereas type 3 can be comparatively stable. There is no established staging system or spontaneous-remission pattern. The principal therapeutic window is likely **before irreversible CNS injury**, ideally at molecular diagnosis or even presymptomatically, although proof that neonatal neurologic outcome can be prevented is lacking. (laugwitz2022humancoq4deficiency pages 10-12, wahedi2024clinicalfeaturesbiochemistry pages 10-10)

---

## 9. Inheritance, epidemiology, and population

Inheritance is **autosomal recessive**. Parents of an affected child are typically obligate heterozygotes; each subsequent pregnancy has a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability. Penetrance appears high for genuinely pathogenic biallelic genotypes, but expressivity is broad. Anticipation is not expected. Germline mosaicism has not emerged as a characteristic mechanism, though low residual recurrence risk after apparently de novo findings cannot be universally excluded.

No reliable birth incidence, point prevalence, carrier frequency, or sex ratio exists. A 2024 review stated that approximately 300 patients with all forms of primary CoQ10 deficiency had been diagnosed worldwide; this is not a COQ4-specific prevalence estimate. Half of the 24 neonatal cases in that review were Chinese, probably reflecting p.Gly124Ser enrichment, referral patterns, and publication bias rather than a proven regional incidence. Chinese versus non-Chinese mortality did not differ significantly (**75% versus 91.7%, P=0.27**). (pan2024thespectrumof pages 1-2)

---

## 10. Diagnostics

### Recommended approach

1. **Immediate clinical recognition:** neonatal seizures/encephalopathy plus hypotonia, respiratory or cardiac failure, feeding difficulty, lactic acidosis, and cerebellar abnormalities should prompt mitochondrial evaluation.
2. **Parallel testing:** blood gas, lactate/pyruvate, glucose, ammonia, CK, liver and renal indices, plasma amino acids, urine organic acids, acylcarnitines, ECG/echocardiography, EEG, brain MRI and, where available, MR spectroscopy.
3. **Rapid genomic testing:** rapid trio WES/WGS is preferred in critically ill neonates. In the 2024 review, **20/24** cases were diagnosed by WES. A nuclear mitochondrial/CoQ panel including COQ4 is reasonable if rapid and comprehensive, but exome/genome analysis better accommodates phenotypic overlap. (pan2024thespectrumof pages 1-2)
4. **Confirmation:** demonstrate biallelic variants with parental segregation. For novel or uncertain variants, measure CoQ10 and respiratory-chain activity in muscle or cultured fibroblasts; COQ4/COQ7/COQ9 immunoblotting and 6-DMQ measurement can provide strong functional support. A normal blood lactate or even normal fibroblast CoQ10 does not exclude disease. (laugwitz2022humancoq4deficiency pages 10-12, xie2022primarycoenzymeq10 pages 7-8)

Muscle biopsy is no longer obligatory when genetics are definitive, but it remains valuable for VUS resolution. CMA can detect a deletion encompassing COQ4 but is insensitive to most pathogenic sequence variants. Karyotype, FISH, mitochondrial-DNA sequencing, and repeat-expansion testing are not first-line tests for isolated suspected COQ4 disease.

### Differential diagnosis

Important alternatives include other primary CoQ deficiencies (**PDSS1, PDSS2, COQ2, COQ5, COQ6, COQ7, COQ8A/ADCK3, COQ8B/ADCK4, COQ9, HPDL**), mtDNA maintenance/translation defects, pyruvate dehydrogenase deficiency, respiratory-chain complex deficiencies, POLG-related disease, neonatal epileptic encephalopathies, congenital disorders of glycosylation, peroxisomal disease, hypoxic–ischemic encephalopathy, infection/sepsis, and structural brain malformations. COQ4 is favored by biallelic COQ4 variants, CoQ/6-DMQ abnormalities, severe cerebellar involvement, cardiomyopathy, and the characteristic parieto-occipital stroke-like pattern in longer survivors. (laugwitz2022humancoq4deficiency pages 1-3, laugwitz2022humancoq4deficiency pages 10-12)

There are no consensus clinical diagnostic criteria, validated newborn biochemical screen, or disease-specific liquid-biopsy/epigenomic test.

---

## 11. Outcome and prognosis

The neonatal phenotype has very high mortality. In 24 neonatal-onset cases, mean survival was **60.0 ± 98.0 days**; mortality was 9/12 in Chinese and 11/12 in non-Chinese cases. These values are based on published cases and should not be treated as unbiased survival estimates. All four survivors had received CoQ10, but only nine patients were treated, and this uncontrolled observation does not prove efficacy. (pan2024thespectrumof pages 1-2)

Across the broader 44-patient spectrum, only five reached adulthood; cardiorespiratory failure secondary to progressive CNS disease was the principal cause of death. Survivors may have profound intellectual/developmental disability, epilepsy, feeding and mobility dependence, visual impairment, dystonia/spasticity/ataxia, and recurrent stroke-like episodes. No validated 5- or 10-year survival curve, life-expectancy estimate, prognostic calculator, or formal quality-of-life dataset exists. (laugwitz2022humancoq4deficiency pages 8-10)

Poor prognostic indicators include prenatal abnormalities, neonatal onset, profound cerebellar malformation, refractory seizures, cardiorespiratory failure, severe CoQ depletion, and truncating-plus-missense genotypes. These associations remain limited by cohort size.

---

## 12. Treatment and current implementation

### CoQ10 replacement

Treatment should not await every confirmatory biochemical result when primary CoQ deficiency is strongly suspected. Recent expert practice recommends starting oral **CoQ10 promptly** and titrating to at least **30 mg/kg/day** after molecular confirmation. Historical COQ4 regimens ranged from **15–60 mg/kg/day**; the 2024 broader CoQ cohort used doses as high as 70 mg/kg/day. (laugwitz2022humancoq4deficiency pages 7-8, wahedi2024clinicalfeaturesbiochemistry pages 10-10)

However, the COQ4-specific evidence is weak and uncontrolled: among 29 treated patients, **16 had no response** and **12 had limited improvement or stabilization**, with no clear dose–response relationship. Oral absorption, cellular delivery, and blood–brain-barrier penetration are major limitations. Neurologic injury already present at treatment is generally not reversible. (laugwitz2022humancoq4deficiency pages 7-8)

Direct abstract statement from Laugwitz et al.: **“Due to the insufficient clinical response to oral CoQ10 supplementation, alternative treatment strategies are warranted.”** The article was published in October 2022; DOI: https://doi.org/10.1136/jmedgenet-2021-107729. (laugwitz2022humancoq4deficiency pages 1-3)

### Other interventions

- **Idebenone:** one 2024 COQ4 case received 20 mg/kg/day alongside CoQ10 for seizure control, but efficacy cannot be isolated. Idebenone and MitoQ did not improve viability in one COQ4 fibroblast model. (wahedi2024clinicalfeaturesbiochemistry pages 10-10, laugwitz2022humancoq4deficiency pages 8-10)
- **Antiseizure therapy:** individualized EEG-guided treatment; avoid valproate when POLG disease has not been excluded or significant hepatic mitochondrial dysfunction exists.
- **Cardiorespiratory care:** ventilation, cardiomyopathy/heart-failure therapy, rhythm surveillance, and intensive-care support.
- **Nutrition and rehabilitation:** enteral feeding when needed; dietetic, physical, occupational, speech/swallowing, vision, and palliative-care support.
- **Experimental therapy:** CoQ precursors/bypass molecules, improved formulations, mitochondrial targeting, and gene replacement/editing are preclinical concepts. No approved COQ4 gene, RNA, or cell therapy exists.

The ClinicalTrials.gov search retrieved no relevant COQ4-specific interventional trial. No pharmacogenomic dosing guideline or validated genotype-guided treatment algorithm exists.

Suggested NCIt intervention concepts: **Coenzyme Q10**, **idebenone**, anticonvulsant therapy, mechanical ventilation, enteral nutrition, physical therapy, occupational therapy, speech therapy, and genetic counseling.

---

## 13. Prevention

The molecular defect cannot currently be prevented by vaccination, lifestyle modification, or environmental control.

- **Primary genetic prevention:** carrier testing for relatives, reproductive counseling, partner testing, prenatal diagnosis by CVS/amniocentesis, and preimplantation genetic testing for a known familial genotype.
- **Secondary prevention:** cascade testing and rapid testing of at-risk newborn siblings; early CoQ10 may prevent or slow some tissue injury, although protection against severe neonatal encephalopathy is unproven.
- **Tertiary prevention:** aggressive seizure control, aspiration prevention, nutritional support, cardiopulmonary surveillance, prompt treatment of infection, and avoidance of prolonged fasting/dehydration.

COQ4 is not included in routine biochemical newborn screening. Genome-based newborn screening is conceptually relevant but requires evidence that presymptomatic treatment changes neurologic outcome. (wahedi2024clinicalfeaturesbiochemistry pages 10-10)

---

## 14. Other species and natural disease

No well-established naturally occurring COQ4 encephalomyopathy in companion animals, livestock, or wildlife was identified, and there is no zoonotic or cross-species transmission. COQ4 is evolutionarily conserved across eukaryotes because CoQ biosynthesis is fundamental to mitochondrial respiration. Relevant research species include **Homo sapiens** (NCBI Taxon 9606), **Mus musculus** (10090), **Danio rerio** (7955), and **Saccharomyces cerevisiae** (4932). Veterinary breed ontology annotations are therefore not currently applicable.

---

## 15. Model organisms and experimental systems

The strongest disease-specific model is the **patient-derived dermal fibroblast** system. It reproduces reduced COQ4, secondary COQ7/COQ9 reduction, low CoQ10, 6-DMQ accumulation, respiratory dependence, and partial rescue by CoQ10. Its limitation is that fibroblasts do not model developing neurons, glia, myocardium, or blood–brain-barrier delivery. (laugwitz2022humancoq4deficiency pages 21-23)

Yeast provides conserved Q-synthome and complementation systems for studying Coq4 and screening pathway-bypass compounds, but yeast CoQ side-chain chemistry and organismal neurobiology differ from humans. Zebrafish COQ4-loss models have been used to study CNS consequences and therapeutic electron-transfer rescue; their strengths are rapid development and whole-organism imaging, while limitations include species-specific development and drug pharmacokinetics. Robust COQ4 patient-derived iPSC neurons, cerebral/cardiac organoids, and conditional mammalian models remain important unmet needs.

---

## Recent developments and authoritative interpretation

The principal 2023–2024 advances were not a new curative therapy but improved phenotypic definition and treatment implementation. The September 2024 neonatal review quantified the exceptionally poor neonatal survival and showed that WES had become the real-world diagnostic route in 20/24 cases. (pan2024thespectrumof pages 1-2) The December 2024 specialist-center cohort emphasized immediate genome-wide diagnosis and high-dose CoQ10 while cautioning that neonatal neurologic disease can remain fatal despite treatment. Its abstract states: **“there are no pathognomonic blood, muscle, or imaging biomarkers of these diseases”** and recommends high-dose treatment as soon as possible. DOI: https://doi.org/10.1212/NXG.0000000000200209; published December 2024. (wahedi2024clinicalfeaturesbiochemistry pages 10-10)

The current expert interpretation is therefore balanced: COQ4 deficiency is one of the few inherited mitochondrial disorders with a rational replacement therapy, so delay is inappropriate; nevertheless, oral CoQ10 has poor CNS bioavailability and cannot reliably reverse prenatal or neonatal brain injury. Earlier molecular diagnosis, better delivery across the blood–brain barrier, and validated pathway-bypass or gene-replacement strategies are the highest-priority research needs. (laugwitz2022humancoq4deficiency pages 1-3, wahedi2024clinicalfeaturesbiochemistry pages 10-10, laugwitz2022humancoq4deficiency pages 8-10)

## Evidence limitations

All clinical evidence consists of case reports, retrospective cohorts, and literature aggregations. There are no randomized trials, unbiased population registries, validated prevalence estimates, formal QoL studies, standardized outcome measures, or robust natural-history survival analyses. Variant-level database fields—ClinVar status, gnomAD frequency, transcript, and HGVS—must be checked at the time of knowledge-base ingestion because classifications and reference transcripts change. Mechanistic statements about ferroptosis, inflammation, and non-bioenergetic CoQ functions are supported mainly by broader CoQ biology; direct quantification in neonatal COQ4 human brain is absent.

References

1. (pan2024thespectrumof pages 1-2): Pianpian Pan, Na Zhou, Yi Sun, Zhengrong Chen, Jin Han, and Wei Zhou. The spectrum of clinical manifestations in newborns with the coq4 mutation: case series and literature review. Frontiers in Pediatrics, Sep 2024. URL: https://doi.org/10.3389/fped.2024.1410133, doi:10.3389/fped.2024.1410133. This article has 4 citations.

2. (laugwitz2022humancoq4deficiency pages 1-3): Lucia Laugwitz, Annette Seibt, Diran Herebian, Susana Peralta, Imke Kienzle, Rebecca Buchert, Ruth Falb, Darja Gauck, Amelie Müller, Mona Grimmel, Stefanie Beck-Woedel, Jan Kern, Karim Daliri, Pegah Katibeh, Katharina Danhauser, Steffen Leiz, Viola Alesi, Fabian Baertling, Gessica Vasco, Robert Steinfeld, Matias Wagner, Ahmet Okay Caglayan, Hakan Gumus, Margit Burmeister, Ertan Mayatepek, Diego Martinelli, Parag Mohan Tamhankar, Vasundhara Tamhankar, Pascal Joset, Katharina Steindl, Anita Rauch, Penelope E Bonnen, Tawfiq Froukh, Samuel Groeschel, Ingeborg Krägeloh-Mann, Tobias B Haack, and Felix Distelmaier. Human coq4 deficiency: delineating the clinical, metabolic and neuroimaging phenotypes. Journal of Medical Genetics, 59:878-887, Oct 2022. URL: https://doi.org/10.1136/jmedgenet-2021-107729, doi:10.1136/jmedgenet-2021-107729. This article has 35 citations and is from a domain leading peer-reviewed journal.

3. (laugwitz2022humancoq4deficiency pages 8-10): Lucia Laugwitz, Annette Seibt, Diran Herebian, Susana Peralta, Imke Kienzle, Rebecca Buchert, Ruth Falb, Darja Gauck, Amelie Müller, Mona Grimmel, Stefanie Beck-Woedel, Jan Kern, Karim Daliri, Pegah Katibeh, Katharina Danhauser, Steffen Leiz, Viola Alesi, Fabian Baertling, Gessica Vasco, Robert Steinfeld, Matias Wagner, Ahmet Okay Caglayan, Hakan Gumus, Margit Burmeister, Ertan Mayatepek, Diego Martinelli, Parag Mohan Tamhankar, Vasundhara Tamhankar, Pascal Joset, Katharina Steindl, Anita Rauch, Penelope E Bonnen, Tawfiq Froukh, Samuel Groeschel, Ingeborg Krägeloh-Mann, Tobias B Haack, and Felix Distelmaier. Human coq4 deficiency: delineating the clinical, metabolic and neuroimaging phenotypes. Journal of Medical Genetics, 59:878-887, Oct 2022. URL: https://doi.org/10.1136/jmedgenet-2021-107729, doi:10.1136/jmedgenet-2021-107729. This article has 35 citations and is from a domain leading peer-reviewed journal.

4. (laugwitz2022humancoq4deficiency pages 7-8): Lucia Laugwitz, Annette Seibt, Diran Herebian, Susana Peralta, Imke Kienzle, Rebecca Buchert, Ruth Falb, Darja Gauck, Amelie Müller, Mona Grimmel, Stefanie Beck-Woedel, Jan Kern, Karim Daliri, Pegah Katibeh, Katharina Danhauser, Steffen Leiz, Viola Alesi, Fabian Baertling, Gessica Vasco, Robert Steinfeld, Matias Wagner, Ahmet Okay Caglayan, Hakan Gumus, Margit Burmeister, Ertan Mayatepek, Diego Martinelli, Parag Mohan Tamhankar, Vasundhara Tamhankar, Pascal Joset, Katharina Steindl, Anita Rauch, Penelope E Bonnen, Tawfiq Froukh, Samuel Groeschel, Ingeborg Krägeloh-Mann, Tobias B Haack, and Felix Distelmaier. Human coq4 deficiency: delineating the clinical, metabolic and neuroimaging phenotypes. Journal of Medical Genetics, 59:878-887, Oct 2022. URL: https://doi.org/10.1136/jmedgenet-2021-107729, doi:10.1136/jmedgenet-2021-107729. This article has 35 citations and is from a domain leading peer-reviewed journal.

5. (laugwitz2022humancoq4deficiency pages 10-12): Lucia Laugwitz, Annette Seibt, Diran Herebian, Susana Peralta, Imke Kienzle, Rebecca Buchert, Ruth Falb, Darja Gauck, Amelie Müller, Mona Grimmel, Stefanie Beck-Woedel, Jan Kern, Karim Daliri, Pegah Katibeh, Katharina Danhauser, Steffen Leiz, Viola Alesi, Fabian Baertling, Gessica Vasco, Robert Steinfeld, Matias Wagner, Ahmet Okay Caglayan, Hakan Gumus, Margit Burmeister, Ertan Mayatepek, Diego Martinelli, Parag Mohan Tamhankar, Vasundhara Tamhankar, Pascal Joset, Katharina Steindl, Anita Rauch, Penelope E Bonnen, Tawfiq Froukh, Samuel Groeschel, Ingeborg Krägeloh-Mann, Tobias B Haack, and Felix Distelmaier. Human coq4 deficiency: delineating the clinical, metabolic and neuroimaging phenotypes. Journal of Medical Genetics, 59:878-887, Oct 2022. URL: https://doi.org/10.1136/jmedgenet-2021-107729, doi:10.1136/jmedgenet-2021-107729. This article has 35 citations and is from a domain leading peer-reviewed journal.

6. (wahedi2024clinicalfeaturesbiochemistry pages 10-10): Azizia Wahedi, Sniya Sudhakar, Amanda Lam, Jose Ignacio Rodriguez Ciancio, Philippa Mills, Paul Gissen, Alice Gardham, Jogesh Kapadia, Jane Hassell, Simon Heales, and Shamima Rahman. Clinical features, biochemistry, imaging, and treatment response in a single-center cohort with coenzyme q <sub>10</sub> biosynthesis disorders. Neurology Genetics, Dec 2024. URL: https://doi.org/10.1212/nxg.0000000000200209, doi:10.1212/nxg.0000000000200209. This article has 6 citations.

7. (laugwitz2022humancoq4deficiency pages 21-23): Lucia Laugwitz, Annette Seibt, Diran Herebian, Susana Peralta, Imke Kienzle, Rebecca Buchert, Ruth Falb, Darja Gauck, Amelie Müller, Mona Grimmel, Stefanie Beck-Woedel, Jan Kern, Karim Daliri, Pegah Katibeh, Katharina Danhauser, Steffen Leiz, Viola Alesi, Fabian Baertling, Gessica Vasco, Robert Steinfeld, Matias Wagner, Ahmet Okay Caglayan, Hakan Gumus, Margit Burmeister, Ertan Mayatepek, Diego Martinelli, Parag Mohan Tamhankar, Vasundhara Tamhankar, Pascal Joset, Katharina Steindl, Anita Rauch, Penelope E Bonnen, Tawfiq Froukh, Samuel Groeschel, Ingeborg Krägeloh-Mann, Tobias B Haack, and Felix Distelmaier. Human coq4 deficiency: delineating the clinical, metabolic and neuroimaging phenotypes. Journal of Medical Genetics, 59:878-887, Oct 2022. URL: https://doi.org/10.1136/jmedgenet-2021-107729, doi:10.1136/jmedgenet-2021-107729. This article has 35 citations and is from a domain leading peer-reviewed journal.

8. (xie2022primarycoenzymeq10 pages 1-2): Jieqiong Xie, Jiayang Jiang, and Qiwei Guo. Primary coenzyme q10 deficiency-7 and pathogenic coq4 variants: clinical presentation, biochemical analyses, and treatment. Frontiers in Genetics, Jan 2022. URL: https://doi.org/10.3389/fgene.2021.776807, doi:10.3389/fgene.2021.776807. This article has 17 citations and is from a peer-reviewed journal.

9. (OpenTargets Search: primary coenzyme Q10 deficiency 7-COQ4): Open Targets Query (primary coenzyme Q10 deficiency 7-COQ4, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

10. (berardo2020redefininginfantileonsetmultisystem pages 4-6): Andres Berardo and Catarina M. Quinzii. Redefining infantile-onset multisystem phenotypes of coenzyme q10-deficiency in the next-generation sequencing era. Journal of translational genetics and genomics, 4:22-35, Apr 2020. URL: https://doi.org/10.20517/jtgg.2020.02, doi:10.20517/jtgg.2020.02. This article has 17 citations.

11. (sondheimer2017novelrecessivemutations pages 4-4): Neal Sondheimer, Stacy Hewson, Jessie M. Cameron, Gino R. Somers, Jane Dunning Broadbent, Marcello Ziosi, Catarina Maria Quinzii, and Ali B. Naini. Novel recessive mutations in coq4 cause severe infantile cardiomyopathy and encephalopathy associated with coq 10 deficiency. Sep 2017. URL: https://doi.org/10.1016/j.ymgmr.2017.05.001, doi:10.1016/j.ymgmr.2017.05.001. This article has 43 citations.

12. (xie2022primarycoenzymeq10 pages 7-8): Jieqiong Xie, Jiayang Jiang, and Qiwei Guo. Primary coenzyme q10 deficiency-7 and pathogenic coq4 variants: clinical presentation, biochemical analyses, and treatment. Frontiers in Genetics, Jan 2022. URL: https://doi.org/10.3389/fgene.2021.776807, doi:10.3389/fgene.2021.776807. This article has 17 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](COQ4-Related_Neonatal_Encephalomyopathy-deep-research-falcon_artifacts/artifact-00.md)