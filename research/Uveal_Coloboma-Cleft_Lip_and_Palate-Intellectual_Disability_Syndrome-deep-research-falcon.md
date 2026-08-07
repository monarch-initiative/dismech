---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T17:51:56.613685'
end_time: '2026-08-01T18:00:44.747169'
duration_seconds: 528.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Uveal Coloboma-Cleft Lip and Palate-Intellectual Disability Syndrome
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
  path: Uveal_Coloboma-Cleft_Lip_and_Palate-Intellectual_Disability_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Uveal Coloboma-Cleft Lip and Palate-Intellectual Disability Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Uveal Coloboma-Cleft Lip and Palate-Intellectual Disability Syndrome** covering all of the
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
- **Disease Name:** Uveal Coloboma-Cleft Lip and Palate-Intellectual Disability Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Uveal Coloboma-Cleft Lip and Palate-Intellectual Disability Syndrome** covering all of the
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


# Uveal Coloboma–Cleft Lip/Palate–Intellectual Disability Syndrome

## Executive summary

This is an exceptionally rare, congenital Mendelian developmental disorder best regarded as the **syndromic end of the YAP1-related ocular-coloboma spectrum**, rather than a well-characterized epidemiologic syndrome. It was originally reported as “an autosomal dominant syndrome of uveal colobomata, cleft lip and palate, and mental retardation.” Subsequent molecular studies linked the broader phenotype—including isolated coloboma, syndromic coloboma, hearing impairment, cleft lip/palate, hematuria, and learning or developmental difficulties—to heterozygous **YAP1** variants. The principal mechanism is **YAP1 loss of function/haploinsufficiency**, disrupting Hippo-YAP-regulated ocular morphogenesis and retinal pigment epithelium (RPE) cell-fate specification. Inheritance is autosomal dominant, but penetrance is incomplete and expression highly variable. (deyoung2022denovoframeshift pages 5-6, deyoung2022denovoframeshift pages 6-6)

The available evidence consists chiefly of individual families and case reports, not registries or population cohorts. Consequently, prevalence, incidence, phenotype percentages, penetrance estimates, survival, and treatment-response statistics cannot presently be calculated reliably. No syndrome-specific clinical trial, approved molecular treatment, or 2023–2024 clinical natural-history study was identified.

| Domain | Established finding | Ontology suggestions | Evidence strength / limitations |
|---|---|---|---|
| Disease identity / identifiers | Rare Mendelian developmental disorder originally described as an autosomal-dominant syndrome of uveal colobomata, cleft lip/palate, and intellectual disability; current evidence places it within the YAP1-related ocular coloboma spectrum. OMIM phenotype: **#120433**. Causal gene: **YAP1 (HGNC:16262)**. Do **not** assign MONDO/Orphanet IDs without external confirmation. (deyoung2022denovoframeshift pages 6-6, deyoung2022denovoframeshift pages 5-6) | OMIM: 120433; Gene: YAP1/HGNC:16262; possible disease label string: YAP1-related ocular coloboma syndrome | Strong gene-disease linkage from multiple human families/cases; disease naming and cross-database mapping remain ambiguous. |
| Core ocular phenotype | Congenital uveal/ocular coloboma is the defining feature; reported involvement includes iris, retina/choroid, and optic nerve, often bilateral; microphthalmia/microcornea and nystagmus can co-occur. (deyoung2022denovoframeshift pages 1-3, deyoung2022denovoframeshift pages 3-5) | HPO: **Coloboma (HP:0000589)**; **Uveal coloboma (HP:0007707)**; **Iris coloboma (HP:0000612)**; **Chorioretinal coloboma (HP:0000539)**; **Optic nerve coloboma (HP:0000588)**; **Microphthalmia (HP:0000568)**; **Microcornea (HP:0000482)**; **Nystagmus (HP:0000639)** | Strong for ocular phenotype; exact frequency and laterality distribution unavailable due to very small case numbers. |
| Craniofacial / neurodevelopmental syndrome features | Syndromic YAP1-associated disease includes **cleft lip with or without cleft palate**, **learning difficulties/developmental delay/intellectual disability**, and dysmorphic features; historic reports include a stillbirth with anencephaly and cleft lip/palate. (deyoung2022denovoframeshift pages 5-6, deyoung2022denovoframeshift pages 6-6, jauss2022routinediagnosticsconfirm pages 6-7) | HPO: **Cleft upper lip (HP:0000204)**; **Cleft palate (HP:0000175)**; **Intellectual disability (HP:0001249)**; **Global developmental delay (HP:0001263)**; **Learning disability (HP:0001328)**; **Anencephaly (HP:0002323)** | Moderate: recurrently cited across later papers, but original 1982 family details were not directly extracted here. |
| Extra-ocular features | Additional reported syndromic manifestations include **sensorineural hearing loss** and **hematuria**; these broaden the phenotype beyond eye and craniofacial findings. (deyoung2022denovoframeshift pages 5-6) | HPO: **Sensorineural hearing impairment (HP:0000407)**; **Hematuria (HP:0000790)** | Moderate: based mainly on earlier family reports summarized in later publications. |
| Representative pathogenic / likely pathogenic variants | Reported variants include **NM_001130145.3:c.178dupG p.(Asp60GlyfsTer52)**, a de novo exon-1 frameshift absent from gnomAD; **c.284T>C p.(Phe95Ser)** in a family with isolated coloboma; and **NM_001130145.3:c.1196_1199del** reported as likely pathogenic in routine diagnostics. (deyoung2022denovoframeshift pages 3-5, oatts2017novelheterozygousmutation pages 1-6, jauss2022routinediagnosticsconfirm pages 6-7) | Sequence Ontology: **frameshift_variant**, **missense_variant**; ACMG/AMP concepts: **likely pathogenic**, **de novo** | Strong for existence of these variants; broader allelic series is incompletely captured in available context. |
| Molecular mechanism | Best-supported mechanism is **YAP1 haploinsufficiency / loss of function** affecting **Hippo-YAP signaling**. YAP1 is a transcriptional co-activator regulated by Hippo pathway phosphorylation and TEAD binding; loss disrupts developmental growth-control programs. (deyoung2022denovoframeshift pages 3-5, deyoung2022denovoframeshift pages 5-6) | GO: **Hippo signaling (GO:0035329)**; **regulation of cell proliferation (GO:0042127)**; **positive regulation of transcription by RNA polymerase II (GO:0045944)** | Strong mechanistic plausibility from human genetics plus animal/in vitro developmental data; direct human tissue functional assays are limited. |
| Developmental pathophysiology | Evidence supports a role in **optic fissure closure / ocular morphogenesis** and **retinal pigment epithelium (RPE) cell-fate specification**; FAT1-Hippo-YAP dysregulation is a plausible upstream pathway. (deyoung2022denovoframeshift pages 5-6, deyoung2022denovoframeshift pages 6-6) | GO: **eye morphogenesis (GO:0048592)**; **optic fissure closure**; **retinal pigment epithelium development (GO:0061299)**; CL: **retinal pigment epithelial cell (CL:0002586)** | Moderate-to-strong from model systems; exact causal chain for clefting/intellectual disability remains less well defined than for ocular defects. |
| Anatomy / tissues affected | Primary structures: **uvea/iris, retina-choroid, optic nerve, globe size**, and likely embryonic ocular tissues including **RPE, periocular mesenchyme, lens vesicle, neural retina** during development. (deyoung2022denovoframeshift pages 5-6) | UBERON: **eye (UBERON:0000970)**, **iris (UBERON:0001769)**, **retina (UBERON:0000966)**, **optic nerve (UBERON:0001138)**, **lens vesicle**, **periocular mesenchyme** | Moderate: anatomy is well supported for eye; non-ocular tissue localization is less disease-specific. |
| Inheritance / penetrance | Inheritance is **autosomal dominant** with **incomplete penetrance** and **variable expressivity**; both familial heterozygous and **de novo** cases are reported. An unaffected mother carrying p.Phe95Ser illustrates reduced penetrance (or possible germline mosaicism). (oatts2017novelheterozygousmutation pages 1-6, deyoung2022denovoframeshift pages 5-6, deyoung2022denovoframeshift pages 3-5) | HPO inheritance terms: **Autosomal dominant inheritance (HP:0000006)**; **Incomplete penetrance (HP:0003829)**; **Variable expressivity (HP:0003828)** | Strong. Quantitative penetrance estimates are not available. |
| Temporal course | Ocular anomalies are **congenital / early infancy-onset**. Visual function may be impaired from infancy and can worsen in some individuals; one reported patient declined from 20/200 to hand movements over 3 years. (deyoung2022denovoframeshift pages 1-3, oatts2017novelheterozygousmutation pages 1-6) | HPO: **Congenital onset (HP:0003577)**; **Reduced visual acuity (HP:0007663)** | Limited natural-history data; no formal staging studies. |
| Diagnostics | Most informative test is **molecular sequencing** (WES/WGS or ocular malformation/developmental disorder panels including YAP1), interpreted with phenotype-driven review and careful read-depth assessment. Ophthalmic evaluation may include fundus photography, OCT, and autofluorescence. (deyoung2022denovoframeshift pages 5-6, oatts2017novelheterozygousmutation pages 6-8, jauss2022routinediagnosticsconfirm pages 6-7) | NCIT: **Molecular Genetic Testing**; HPO-driven phenotyping; eye imaging terms; possible panel category: coloboma / microphthalmia panel | Strong for sequencing utility; no disease-specific biomarker, lab assay, or diagnostic criteria guideline identified. |
| Management / real-world care | No disease-modifying therapy is established. Current care is **supportive and multidisciplinary**: ophthalmology/low-vision care, monitoring for cataract and refractive error, cleft team care if present, developmental assessment/support, audiology, and renal/urinary evaluation when indicated by phenotype. (deyoung2022denovoframeshift pages 5-6, deyoung2022denovoframeshift pages 1-3) | NCIT: **Supportive Care**, **Ophthalmologic Examination**, **Vision Rehabilitation**, **Cleft Lip Repair**, **Speech Therapy**, **Genetic Counseling** | Indirect but clinically standard; syndrome-specific treatment-outcome studies are lacking. |
| Genetic counseling / prevention | Because AD inheritance with reduced penetrance is documented, **genetic counseling**, family testing/segregation analysis, and consideration of prenatal or preimplantation testing after familial variant identification are reasonable. (oatts2017novelheterozygousmutation pages 1-6, deyoung2022denovoframeshift pages 5-6, deyoung2022denovoframeshift pages 3-5) | NCIT: **Genetic Counseling**; HPO inheritance terms above | Strong rationale from inheritance pattern; no formal prevention studies exist. |
| Model organisms | **Zebrafish**: yap1 and wwtr1/taz are required for proper **RPE fate specification** in eye development. **Mouse**: heterozygous Yap1 alteration causes Müller glia dysfunction and late-onset cone degeneration; broader Yap1 developmental roles support plausibility. (deyoung2022denovoframeshift pages 5-6, deyoung2022denovoframeshift pages 3-5) | NCBI Taxon: **Danio rerio**, **Mus musculus**; CL: **Müller cell (CL:0002573)** | Moderate: models support ocular developmental biology, but no single model fully recapitulating the full human syndromic triad was identified. |
| Recent developments (2023-2024) | No syndrome-specific 2023-2024 clinical expansion or interventional trial was identified in available searches. Recent work mainly strengthens broader YAP biology and developmental pathway crosstalk rather than this exact syndrome. (deyoung2022denovoframeshift pages 5-6) | GO/Pathway terms above | Important evidence gap; absence of evidence should not be read as disproving future developments. |
| Explicit evidence gaps | No robust data were found for **syndrome prevalence/incidence**, **sex ratio**, **standardized prognosis**, **environmental risk/protective factors**, **gene-environment interactions**, **approved targeted therapy**, or **relevant clinical trials**. (deyoung2022denovoframeshift pages 5-6, jauss2022routinediagnosticsconfirm pages 6-7) | Use “not established” rather than assigning ontology IDs | Strong confidence that these are gaps in currently available evidence, not confirmed negatives. |


*Table: This table summarizes the compact evidence base for uveal coloboma-cleft lip/palate-intellectual disability syndrome as part of the YAP1-related ocular coloboma spectrum. It highlights established findings, ontology suggestions, and important limitations for knowledge-base curation.*

## 1. Disease information

### Definition and nomenclature

The defining malformation is **congenital uveal coloboma**, caused by defective embryonic optic-fissure closure, occurring with cleft lip with or without cleft palate and neurodevelopmental impairment in the classic syndromic presentation. Modern evidence indicates that this historical syndrome overlaps the broader entity **YAP1-related developmental eye disorder/ocular coloboma**. YAP1 variants can produce either isolated ocular disease or multisystem disease, so the triad should not be treated as obligatory in every molecularly confirmed individual. (deyoung2022denovoframeshift pages 6-6, deyoung2022denovoframeshift pages 5-6)

**Identifiers and synonyms**

- **OMIM phenotype:** #120433, ocular coloboma with or without hearing impairment, cleft lip/palate, and/or intellectual or learning impairment.
- **Gene:** *YAP1*; HGNC:16262.
- **MONDO:** no exact MONDO identifier could be verified from the retrieved evidence; it should remain unassigned rather than inferred.
- **Orphanet:** no exact syndrome-specific ORPHA identifier was verified.
- **ICD-10/ICD-11 and MeSH:** no unique syndrome-specific code was identified. Component manifestations are coded separately, such as congenital ocular coloboma, cleft lip/palate, and intellectual developmental disorder.
- **Synonyms:** autosomal dominant syndrome of uveal colobomata, cleft lip and palate, and mental retardation; uveal coloboma–cleft lip/palate–intellectual disability syndrome; syndromic YAP1-related ocular coloboma; YAP1-related developmental eye disorder.

The foundational report is Kingston, Harper, and Jones, *Journal of Medical Genetics*, December 1982, DOI: https://doi.org/10.1136/jmg.19.6.444. The retrieved system did not provide a verified PMID, so none is guessed here. Later literature explicitly cites this report as an autosomal-dominant uveal-coloboma/clefting/intellectual-disability syndrome. (deyoung2022denovoframeshift pages 6-6)

**Evidence granularity:** the evidence is primarily **human family-level or individual-patient clinical data**, subsequently aggregated in OMIM and later case reports. It is not based on EHR-scale analyses.

## 2. Etiology

### Causal factor

The best-supported cause is a **germline heterozygous loss-of-function variant in YAP1**. Nonsense and frameshift alleles support haploinsufficiency; familial missense variants have also been reported. Both inherited and de novo variants occur. A 2022 case carried de novo NM_001130145.3:c.178dupG, p.(Asp60GlyfsTer52), predicted to undergo nonsense-mediated decay and remove amino acids 61–504. (deyoung2022denovoframeshift pages 3-5, deyoung2022denovoframeshift pages 1-3)

### Risk factors

- **Genetic:** a pathogenic/likely pathogenic heterozygous *YAP1* allele is the established risk factor. A positive family history raises risk, but an unaffected carrier may transmit disease because penetrance is incomplete.
- **Modifiers:** alternative YAP1 transcriptional start sites and variable expression from the normal allele have been proposed to explain variable expression. These remain hypotheses rather than validated clinical modifiers. (oatts2017novelheterozygousmutation pages 1-6, deyoung2022denovoframeshift pages 3-5)
- **Environmental, infectious, lifestyle, occupational, sex, or age-related risks:** none is established for this specific syndrome.
- **Gene–environment interaction:** no syndrome-specific evidence was found.

Environmental associations reported for anophthalmia/microphthalmia broadly must not be assigned to YAP1-related disease without direct evidence.

### Protective factors

No protective allele, diet, medication, behavior, or exposure has been demonstrated. Reduced penetrance in carriers is not equivalent to an identified protective factor.

## 3. Phenotypes

Because published denominators are very small and ascertainment differs among reports, frequencies should be recorded as **unknown/variable**, not converted into percentages.

### Ocular manifestations

- **Uveal/ocular coloboma:** congenital, often bilateral, involving iris, choroid/retina, and/or optic nerve; severity ranges from structurally evident disease with preserved acuity to major visual impairment. Suggested HPO: Coloboma HP:0000589; Uveal coloboma HP:0007707; Iris coloboma HP:0000612; Chorioretinal coloboma HP:0000539; Optic nerve coloboma HP:0000588.
- **Microphthalmia and microcornea:** congenital and variably present. HPO: Microphthalmia HP:0000568; Microcornea HP:0000482.
- **Nystagmus, reduced visual acuity, astigmatism, cataract:** secondary or associated ocular findings. In one molecularly confirmed one-year-old, visual acuity was 20/200, with nystagmus, bilateral microcornea, right microphthalmia, and an inferior cortical cataract. (deyoung2022denovoframeshift pages 1-3, deyoung2022denovoframeshift pages 3-5)

One 2017 family illustrates extreme variability: a 20-year-old had bilateral iris/retinal colobomas and acuity declining from 20/200 to hand movements over three years, whereas his 12-year-old half-brother had bilateral retinal/optic-disc colobomas with normal acuity. Their clinically unaffected mother carried the same p.Phe95Ser variant. (oatts2017novelheterozygousmutation pages 1-6)

### Craniofacial and neurodevelopmental manifestations

- **Cleft lip with or without cleft palate:** congenital and surgically relevant; frequency unknown. HPO: Cleft upper lip HP:0000204; Cleft palate HP:0000175.
- **Developmental delay, learning difficulty, or intellectual disability:** recognized syndromic manifestations, with variable severity. HPO: Global developmental delay HP:0001263; Learning disability HP:0001328; Intellectual disability HP:0001249. A 2022 diagnostic report broadened the phenotype by associating a likely pathogenic *YAP1* deletion with developmental delay and additional syndromic features. (deyoung2022denovoframeshift pages 5-6, jauss2022routinediagnosticsconfirm pages 6-7)
- **Anencephaly:** reported in a stillbirth from an earlier family, together with cleft lip/palate; this is a rare observation, not an established routine feature. HPO: Anencephaly HP:0002323. (deyoung2022denovoframeshift pages 5-6)

### Other manifestations

Sensorineural hearing impairment and hematuria have been reported in syndromic families. Suggested HPO terms are Sensorineural hearing impairment HP:0000407 and Hematuria HP:0000790. Possible hemifacial microsomia, tubular nose, and spina bifida occulta were noted in one 2022 proband but should be regarded as provisional extensions rather than core findings. (deyoung2022denovoframeshift pages 5-6, deyoung2022denovoframeshift pages 1-3)

### Quality-of-life effects

No EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life study was found. Expected burdens include visual disability, educational and adaptive-function limitations, hearing-related communication difficulties, and feeding, speech, dental, and psychosocial burdens associated with clefting. These are clinical inferences from the manifestations, not syndrome-specific quantitative outcomes.

## 4. Genetic and molecular information

### Gene and protein

*YAP1* encodes Yes-associated protein 1, a transcriptional co-activator and central Hippo-pathway effector. YAP1 lacks intrinsic DNA-binding activity and acts through transcription factors including TEAD proteins. When growth-suppressive Hippo signaling is inactive, nuclear YAP1/TAZ promotes pro-growth and anti-apoptotic transcription. (deyoung2022denovoframeshift pages 3-5)

### Representative variants

1. **NM_001130145.3:c.178dupG, p.(Asp60GlyfsTer52)**: de novo heterozygous exon-1 frameshift; absent from gnomAD; predicted nonsense-mediated decay; classified likely pathogenic using PS2 and PM2 evidence in the 2022 report. (deyoung2022denovoframeshift pages 3-5)
2. **c.284T>C, p.(Phe95Ser)**: heterozygous missense variant in a family with isolated ocular coloboma. It was absent from contemporary variant databases and affects a residue conserved across nine species. In-silico predictions were discordant—SIFT 0.04, damaging; PolyPhen-2 0.085, tolerated—so its interpretation relies importantly on segregation and phenotype data. (oatts2017novelheterozygousmutation pages 1-6)
3. **NM_001130145.3:c.1196_1199del**: paternal, likely pathogenic four-base deletion reported in a neurodevelopmental diagnostic cohort. (jauss2022routinediagnosticsconfirm pages 6-7)

The variants are **germline**, not somatic cancer variants. The established mechanism is loss of function/haploinsufficiency, not gain of function or dominant negative action. No validated modifier gene, syndrome-specific epigenetic signature, recurrent chromosomal rearrangement, founder allele, or disease-relevant methylation biomarker was identified.

## 5. Environmental information

No toxin, radiation exposure, pollution source, maternal infection, nutritional deficiency, smoking, alcohol exposure, exercise pattern, or infectious organism has been causally linked to this exact YAP1 syndrome. Environmental factors associated with ocular malformations generally are differential etiologic considerations, but they do not replace molecular diagnosis and should not be annotated as syndrome causes.

## 6. Mechanism and pathophysiology

### Proposed causal chain

**Upstream germline YAP1 loss-of-function variant → reduced functional YAP1 dosage → abnormal Hippo-YAP/TEAD transcriptional output during embryogenesis → altered proliferation, survival, migration, and cell-fate specification in developing ocular tissues → defective optic-fissure closure and uveal coloboma.** Microphthalmia and microcornea plausibly reflect broader disturbance of ocular growth. Zebrafish evidence particularly implicates failure of proper RPE specification. (deyoung2022denovoframeshift pages 5-6, deyoung2022denovoframeshift pages 3-5)

YAP1 is expressed during optic-fissure closure in presumptive RPE, periocular mesenchyme, lens vesicle, and scattered neural-retinal cells. Zebrafish *yap1* and *wwtr1/taz* are required for RPE fate; FAT1 knockdown, affecting an upstream Hippo regulator implicated in coloboma, causes nuclear YAP1 accumulation in vitro. These observations position Hippo regulation upstream, and abnormal developmental transcription and tissue morphogenesis downstream. (deyoung2022denovoframeshift pages 5-6)

The mechanistic bridge from YAP1 deficiency to clefting and intellectual disability is less directly resolved than the ocular mechanism. It likely reflects the broader requirement for YAP1-regulated growth and lineage decisions in craniofacial and neural development, but direct syndrome-specific single-cell, spatial-transcriptomic, proteomic, metabolomic, or human organoid evidence was not identified.

**Suggested GO terms:** Hippo signaling GO:0035329; regulation of cell proliferation GO:0042127; positive regulation of transcription by RNA polymerase II GO:0045944; eye morphogenesis GO:0048592; retinal pigment epithelium development GO:0061299; regulation of apoptotic process GO:0042981.

**Suggested cell types:** retinal pigment epithelial cell CL:0002586; Müller glial cell CL:0002573; neural retinal cell; periocular mesenchymal cell; lens epithelial cell. Exact CL identifiers should be ontology-validated before ingestion where not listed.

There is no established metabolic, immune, inflammatory, fibrotic, or biochemical-enzyme defect in this syndrome.

## 7. Anatomical structures affected

The primary organ is the **eye**, particularly the uvea/iris, retina and choroid, optic disc/nerve, and globe. Suggested UBERON terms include eye UBERON:0000970, retina UBERON:0000966, iris UBERON:0001769, and optic nerve UBERON:0001138. Developmentally relevant tissues include RPE, periocular mesenchyme, lens vesicle, and neural retina. (deyoung2022denovoframeshift pages 1-3, deyoung2022denovoframeshift pages 5-6)

Secondary systems can include the lip and palate, central nervous system/neurodevelopment, auditory system, and urinary tract/kidneys. Coloboma may be unilateral or bilateral and can be anatomically asymmetric; bilateral disease is prominent in several molecularly documented cases. (deyoung2022denovoframeshift pages 1-3, oatts2017novelheterozygousmutation pages 1-6)

At the subcellular level, the relevant localization is principally **cytoplasmic versus nuclear YAP1**, controlled by Hippo-dependent phosphorylation and nuclear translocation. Suggested GO cellular-component annotations include nucleus and cytoplasm; these are gene-level rather than disease-specific annotations. (deyoung2022denovoframeshift pages 3-5)

## 8. Temporal development

The structural defects arise prenatally and are present at birth. There are no recognized acute, relapsing-remitting, or remitting stages. Clefting and coloboma are structurally stable congenital malformations, but their consequences are lifelong. Visual function may remain stable or deteriorate because of retinal complications, cataract, refractive error, or other secondary ocular disease; the 2017 report documents substantial decline in one individual over three years. (oatts2017novelheterozygousmutation pages 1-6, oatts2017novelheterozygousmutation pages 6-8)

Critical intervention periods are infancy and childhood: prompt ophthalmic characterization and visual habilitation, cleft feeding/surgical pathways, hearing assessment, and early developmental intervention may reduce secondary disability. No disease-specific longitudinal staging framework exists.

## 9. Inheritance and population

Inheritance is **autosomal dominant**. Both multigenerational familial transmission and de novo occurrence are documented. Penetrance is incomplete, and expression varies from an unaffected carrier or isolated ocular coloboma to multisystem disease. The unaffected mother carrying p.Phe95Ser is direct evidence of reduced penetrance, although germline mosaicism was also discussed. (oatts2017novelheterozygousmutation pages 1-6, deyoung2022denovoframeshift pages 5-6)

No numeric penetrance, prevalence, incidence, carrier frequency, sex ratio, age distribution, founder effect, ethnic enrichment, geographic clustering, anticipation, or consanguinity effect is established. The disorder is so rare that general coloboma prevalence must not be substituted for syndrome prevalence. Germline mosaicism is possible in principle but has not been quantified.

For a heterozygous affected individual, the formal transmission probability is 50% per conception, but the probability and severity of clinical expression in a carrier cannot be predicted accurately because of reduced penetrance and variable expressivity.

## 10. Diagnostics

### Clinical evaluation

Diagnosis begins with recognition of congenital ocular coloboma, particularly when accompanied by microphthalmia, clefting, developmental impairment, hearing loss, hematuria, or a dominant family history. Detailed ophthalmic evaluation should define iris, chorioretinal, and optic-nerve involvement and assess acuity, refraction, cataract, nystagmus, and retinal complications. Fundus photography, fundus autofluorescence, and optical coherence tomography have been used in reported families. (oatts2017novelheterozygousmutation pages 6-8)

Audiology, developmental/neuropsychological assessment, cleft-team evaluation, and urinalysis/renal assessment are phenotype-directed. Brain imaging is not a universal diagnostic requirement but is appropriate for neurologic abnormalities or major developmental impairment.

### Genetic testing strategy

1. **Trio exome or genome sequencing** is appropriate for syndromic coloboma, especially in sporadic cases.
2. A **microphthalmia–anophthalmia–coloboma or developmental-eye-disorder panel** should include *YAP1* and major differential genes.
3. **Single-gene YAP1 sequencing with deletion/duplication analysis** is reasonable where the phenotype or family segregation is compelling.
4. Review exon-level read depth because inadequate coverage can lead to missed calls; the 2022 authors specifically cautioned that unbiased exome analysis alone can be misleading. (deyoung2022denovoframeshift pages 5-6)
5. **Chromosomal microarray** is useful for syndromic congenital anomalies but does not exclude a sequence-level *YAP1* variant. Karyotype/FISH should be reserved for suspected large rearrangements.

RNA sequencing may help resolve a suspected splice variant, but no validated transcriptomic diagnostic signature exists. Mitochondrial, repeat-expansion, liquid-biopsy, proteomic, and metabolomic tests are not indicated routinely.

### Differential diagnosis

Important alternatives include CHARGE syndrome (*CHD7*), branchio-oculo-facial syndrome (*TFAP2A*), renal-coloboma syndrome (*PAX2*), Cat-eye syndrome, Kabuki syndrome, and other MAC-spectrum disorders involving *SOX2, OTX2, PAX6, MAB21L2, SALL2,* or *FAT1*. Distinction relies on the complete phenotype and molecular testing. No universally accepted syndrome-specific clinical criteria exist.

## 11. Outcome and prognosis

No five- or ten-year survival estimates, mortality rate, or life-expectancy data exist. The syndrome is not known to be intrinsically degenerative or lethal in its usual presentation, although severe congenital anomalies can affect individual prognosis. A stillbirth with anencephaly in one historical family demonstrates that rare severe outcomes may occur but does not establish a general mortality risk. (deyoung2022denovoframeshift pages 5-6)

Principal long-term morbidity is visual impairment, potentially compounded by hearing loss, intellectual/developmental disability, and cleft-related speech, feeding, dental, and psychosocial effects. Prognosis depends more on anatomical coloboma extent, retinal/optic-nerve involvement, associated anomalies, and developmental severity than on a validated molecular biomarker. No syndrome-specific prognostic model or quality-of-life instrument has been studied.

## 12. Treatment

There is **no approved pharmacologic, gene, cell, RNA, targeted, or immunologic therapy** that corrects YAP1 haploinsufficiency or restores embryonic optic-fissure closure. No relevant syndrome-specific ClinicalTrials.gov study was identified.

Management is individualized and supportive:

- pediatric and lifelong ophthalmology; refractive correction, amblyopia treatment where feasible, cataract management, retinal surveillance, and low-vision services;
- cleft feeding support, staged cleft-lip/palate repair, dentistry/orthodontics, and speech therapy;
- early developmental, educational, occupational, physical, and behavioral supports;
- audiologic monitoring and hearing devices when indicated;
- renal/urinary investigation when hematuria is present;
- genetic counseling and family testing.

Suggested NCIt concepts include Genetic Counseling, Molecular Genetic Testing, Supportive Care, Ophthalmologic Examination, Vision Rehabilitation, Cleft Lip Repair, Cleft Palate Repair, Speech Therapy, Occupational Therapy, and Hearing Aid. There are no syndrome-specific response-rate or adverse-event data.

## 13. Prevention

Primary prevention through lifestyle, vaccination, diet, or medication is not available because this is a germline developmental disorder. Secondary and tertiary prevention are nevertheless important:

- identify the disorder early and initiate visual, hearing, developmental, and cleft interventions;
- perform cascade testing after a familial variant is found;
- offer prenatal diagnosis or preimplantation genetic testing when the familial pathogenic variant is known;
- counsel families about the 50% transmission probability and unpredictable clinical expression.

Routine population or newborn molecular screening is not recommended. Prenatal ultrasound may detect clefting, microphthalmia, or major CNS malformations, but a normal scan cannot exclude coloboma or later neurodevelopmental impairment.

## 14. Other species and natural disease

No naturally occurring veterinary syndrome confidently homologous to the complete human triad was identified. Accordingly, no affected breed, VBO term, zoonotic potential, transmission risk, or cross-species natural-disease epidemiology can be assigned. YAP1 and Hippo signaling are evolutionarily conserved, making experimental comparative biology highly informative, but this does not establish spontaneous disease in another species.

## 15. Model organisms

### Zebrafish

Genetic studies show that *yap1* and *wwtr1/taz* are required for proper RPE cell-fate specification. These models support the causal chain from abnormal Hippo-YAP signaling to defective ocular differentiation and coloboma-like developmental abnormalities. Their strengths are accessible embryology, live imaging, and genetic manipulation; limitations include anatomical differences from human craniofacial and cortical development and incomplete recapitulation of the full human syndrome. (deyoung2022denovoframeshift pages 5-6)

A 2024 zebrafish reporter study—Astone et al., published September 2024, DOI: https://doi.org/10.3390/ijms251810005—showed broad developmental crosstalk between Wnt/β-catenin and Yap/Taz activity using pharmacologic and genetic perturbations. This is a recent mechanistic development relevant to YAP biology, but it is not direct evidence about patients with this syndrome.

### Mouse

YAP1 is expressed in developing RPE, periocular mesenchyme, lens vesicle, and neural retina. Heterozygous Yap1 alteration has been associated with Müller-glial dysfunction and late-onset cone degeneration, supporting roles in retinal differentiation and maintenance. Mouse models are valuable for mammalian retinal cell biology but do not yet provide a validated full model of the ocular-cleft-neurodevelopmental triad. (deyoung2022denovoframeshift pages 5-6)

### Cellular and advanced models

FAT1 knockdown causes nuclear YAP1 accumulation in vitro, providing pathway-level evidence connecting an upstream Hippo regulator to coloboma biology. No syndrome-specific human iPSC, ocular-organoid, craniofacial-organoid, single-cell, spatial-transcriptomic, CRISPR-screen, or multi-omics model was identified. These are major opportunities for future research. (deyoung2022denovoframeshift pages 5-6)

## Recent-development and evidence assessment

The latest syndrome-specific clinical evidence retrieved was published in 2022: DeYoung et al., DOI: https://doi.org/10.1080/13816810.2022.2028299, describing a de novo *YAP1* frameshift, and Jauss et al., December 2022, DOI: https://doi.org/10.3390/genes13122305, broadening the neurodevelopmental phenotype. The former directly states that its patient had “bilateral uveal coloboma and microphthalmia,” while the latter’s abstract states that routine diagnostics can “broaden the phenotypic spectrum” for genes including *YAP1*. (deyoung2022denovoframeshift pages 3-5, jauss2022routinediagnosticsconfirm pages 6-7)

No syndrome-specific 2023–2024 clinical cohort, natural-history study, therapeutic trial, or guideline was found. The strongest expert interpretation from the current literature is therefore that *YAP1*-related disease is a **variable, incompletely penetrant developmental spectrum**, not a uniform triad. Diagnostic practice should combine detailed phenotyping with sequencing and segregation analysis, while care remains multidisciplinary and manifestation-directed. (oatts2017novelheterozygousmutation pages 1-6, deyoung2022denovoframeshift pages 5-6)

## Key limitations for knowledge-base curation

1. Do not infer phenotype frequencies from single families.
2. Do not assign an unverified MONDO or Orphanet identifier.
3. Do not treat every *YAP1* variant as pathogenic; missense alleles require rigorous ACMG/AMP and segregation assessment.
4. Do not extrapolate environmental risks or prevalence from nonspecific coloboma/MAC studies.
5. Record epidemiology, standardized prognosis, protective factors, pharmacogenomics, targeted treatment, and clinical-trial evidence as **not established** rather than “none” in an absolute biological sense.
6. PMID fields should remain blank where a PMID was not directly verified; the DOI URLs above provide stable source links.

References

1. (deyoung2022denovoframeshift pages 5-6): Charles DeYoung, Bin Guan, Ehsan Ullah, Delphine Blain, Robert B. Hufnagel, and Brian P. Brooks. De novo frameshift mutation in yap1 associated with bilateral uveal coloboma and microphthalmia. Ophthalmic Genetics, 43:513-517, Mar 2022. URL: https://doi.org/10.1080/13816810.2022.2028299, doi:10.1080/13816810.2022.2028299. This article has 9 citations and is from a peer-reviewed journal.

2. (deyoung2022denovoframeshift pages 6-6): Charles DeYoung, Bin Guan, Ehsan Ullah, Delphine Blain, Robert B. Hufnagel, and Brian P. Brooks. De novo frameshift mutation in yap1 associated with bilateral uveal coloboma and microphthalmia. Ophthalmic Genetics, 43:513-517, Mar 2022. URL: https://doi.org/10.1080/13816810.2022.2028299, doi:10.1080/13816810.2022.2028299. This article has 9 citations and is from a peer-reviewed journal.

3. (deyoung2022denovoframeshift pages 1-3): Charles DeYoung, Bin Guan, Ehsan Ullah, Delphine Blain, Robert B. Hufnagel, and Brian P. Brooks. De novo frameshift mutation in yap1 associated with bilateral uveal coloboma and microphthalmia. Ophthalmic Genetics, 43:513-517, Mar 2022. URL: https://doi.org/10.1080/13816810.2022.2028299, doi:10.1080/13816810.2022.2028299. This article has 9 citations and is from a peer-reviewed journal.

4. (deyoung2022denovoframeshift pages 3-5): Charles DeYoung, Bin Guan, Ehsan Ullah, Delphine Blain, Robert B. Hufnagel, and Brian P. Brooks. De novo frameshift mutation in yap1 associated with bilateral uveal coloboma and microphthalmia. Ophthalmic Genetics, 43:513-517, Mar 2022. URL: https://doi.org/10.1080/13816810.2022.2028299, doi:10.1080/13816810.2022.2028299. This article has 9 citations and is from a peer-reviewed journal.

5. (jauss2022routinediagnosticsconfirm pages 6-7): Robin-Tobias Jauss, Sophia Schließke, and Rami Abou Jamra. Routine diagnostics confirm novel neurodevelopmental disorders. Genes, 13:2305, Dec 2022. URL: https://doi.org/10.3390/genes13122305, doi:10.3390/genes13122305. This article has 13 citations.

6. (oatts2017novelheterozygousmutation pages 1-6): Julius T. Oatts, Sarah Hull, Michel Michaelides, Gavin Arno, Andrew R. Webster, and Anthony T. Moore. Novel heterozygous mutation in yap1 in a family with isolated ocular colobomas. Ophthalmic Genetics, 38:281-283, May 2017. URL: https://doi.org/10.1080/13816810.2016.1188122, doi:10.1080/13816810.2016.1188122. This article has 22 citations and is from a peer-reviewed journal.

7. (oatts2017novelheterozygousmutation pages 6-8): Julius T. Oatts, Sarah Hull, Michel Michaelides, Gavin Arno, Andrew R. Webster, and Anthony T. Moore. Novel heterozygous mutation in yap1 in a family with isolated ocular colobomas. Ophthalmic Genetics, 38:281-283, May 2017. URL: https://doi.org/10.1080/13816810.2016.1188122, doi:10.1080/13816810.2016.1188122. This article has 22 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Uveal_Coloboma-Cleft_Lip_and_Palate-Intellectual_Disability_Syndrome-deep-research-falcon_artifacts/artifact-00.md)