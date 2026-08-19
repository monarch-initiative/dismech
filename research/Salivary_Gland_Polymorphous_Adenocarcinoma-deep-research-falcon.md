---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-05T22:50:39.637814'
end_time: '2026-08-05T22:58:13.510924'
duration_seconds: 453.87
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Salivary Gland Polymorphous Adenocarcinoma
  mondo_id: ''
  category: Cancer
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
  path: Salivary_Gland_Polymorphous_Adenocarcinoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Salivary Gland Polymorphous Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Salivary Gland Polymorphous Adenocarcinoma** covering all of the
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
- **Disease Name:** Salivary Gland Polymorphous Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Salivary Gland Polymorphous Adenocarcinoma** covering all of the
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


# Salivary Gland Polymorphous Adenocarcinoma: Research Report

## Executive summary

Polymorphous adenocarcinoma (PAC) is a rare malignant epithelial neoplasm arising predominantly in the minor salivary glands, especially those of the palate. It combines cytologic uniformity with marked architectural diversity and infiltrative growth. Most conventional PACs behave indolently, but local recurrence, nodal metastasis, distant metastasis, and occasional high-grade transformation are possible; accordingly, the World Health Organization removed “low-grade” from the former name *polymorphous low-grade adenocarcinoma*. The cribriform subtype lies within the current PAC spectrum but is enriched for PRKD-family rearrangements and may have greater nodal metastatic potential than conventional PAC. The strongest established molecular feature is a somatic alteration of the protein kinase D family—particularly **PRKD1 p.Glu710Asp (E710D)** in conventional PAC and PRKD1/PRKD2/PRKD3 rearrangements in cribriform tumors. Diagnosis remains morphology-first, supported by immunohistochemistry and, in difficult cases, PRKD molecular testing. Complete surgical excision is the principal treatment; evidence for systemic or genotype-directed therapy is currently insufficient. (nonaka2022immunohistochemicalprofileof pages 1-3, iyer2021anoverviewon pages 11-12)

The evidence retrieved for this report is strongest for classification, pathology, immunophenotype, and molecular diagnosis, but weaker for disease-specific incidence, quality of life, prospective treatment outcomes, and experimental models.

| Domain | Key findings | Numeric details | Evidence type | Source year / DOI | Citation |
|---|---|---|---|---|---|
| Entity / classification | Polymorphous adenocarcinoma (PAC) is a malignant salivary gland tumor, predominantly of minor salivary glands, with morphologic diversity, infiltrative growth, and generally low metastatic potential; originally described as polymorphous low-grade adenocarcinoma and renamed by WHO to PAC to reflect a broader biologic spectrum including higher-grade variants. | Systematic review dataset: 409 PAC cases from 32 studies (1988-2021). | Systematic review / meta-analysis; narrative review | 2022, https://doi.org/10.1007/s12105-022-01453-6; 2021, https://doi.org/10.3390/cancers13153910 | (nonaka2022immunohistochemicalprofileof pages 1-3, iyer2021anoverviewon pages 11-12) |
| Anatomy / clinical course | PAC arises mainly in minor salivary glands; diagnosis is often straightforward in the palate but can be difficult in uncommon sites such as the oropharynx, sinonasal tract, and nasopharynx. Clinical course is usually indolent/favorable, though aggressive behavior can occur. | Common-site emphasis: palate; uncommon sites specifically listed: oropharynx, sinonasal tract, nasopharynx. | Systematic review / meta-analysis; narrative review | 2022, https://doi.org/10.1007/s12105-022-01453-6; 2021, https://doi.org/10.3390/cancers13153910 | (nonaka2022immunohistochemicalprofileof pages 1-3, nonaka2022immunohistochemicalprofileof pages 4-6, iyer2021anoverviewon pages 11-12) |
| Pathology / IHC | Characteristic features include cytologic uniformity with architectural diversity, infiltrative borders/growth, and possible myxohyaline matrix. Helpful IHC profile: CK7+/CK20−, p63+/p40−, S100+, vimentin+, GFAP−; p63+/p40− is especially useful against adenoid cystic carcinoma. | Positive staining rates: pan-cytokeratin 97.3%, CK7 96.8%, CK7/8 97.4%, E-cadherin 90%, vimentin 92.5%, S100 97%, p63 91.7%, SOX10 100%; negative: CK20 0%, p40 0%, GFAP 5%; p63+/p40− in PAC 38/39 (97.4%) vs ACC 1/155 (0.006%); OR 801.32; mean MIB-1 labeling index 3.78%. | Systematic review / meta-analysis | 2022, https://doi.org/10.1007/s12105-022-01453-6 | (nonaka2022immunohistochemicalprofileof pages 8-10, nonaka2022immunohistochemicalprofileof pages 1-3, nonaka2022immunohistochemicalprofileof pages 4-6) |
| Molecular genetics | PAC is associated with PRKD1 alterations on chromosome 14; the PRKD1 E710D hotspot mutation is highlighted as a useful ancillary diagnostic marker. PRKD-family signaling is linked to migration/differentiation through MAPK and RAS-related pathways. Cribriform adenocarcinoma has been incorporated into the PAC spectrum, although debate remains. | Specific retrieved numeric frequency not available in current evidence; hotspot named: PRKD1 E710D. | Narrative review | 2021, https://doi.org/10.3390/cancers13153910 | (iyer2021anoverviewon pages 11-12) |
| Diagnosis | Diagnosis remains morphology-based, with IHC and molecular testing as adjuncts. The most clinically important differential diagnosis is adenoid cystic carcinoma; p63+/p40− strongly favors PAC. FISH has shown reasonable success for detecting PRKD1 alterations. | Differential performance metric: OR 801.32 for p63+/p40− pattern distinguishing PAC from ACC; PAC 38/39 vs ACC 1/155. | Systematic review / meta-analysis; narrative review | 2022, https://doi.org/10.1007/s12105-022-01453-6; 2021, https://doi.org/10.3390/cancers13153910 | (nonaka2022immunohistochemicalprofileof pages 8-10, nonaka2022immunohistochemicalprofileof pages 1-3, iyer2021anoverviewon pages 11-12) |
| Treatment | Retrieved disease-specific evidence indicates correct diagnosis is clinically important because management differs from mimics; broader salivary gland review states surgical resection is principal treatment for most salivary gland neoplasms, with other modalities used according to behavior/stage. | No PAC-specific response-rate or regimen-level numeric outcomes available in retrieved evidence. | Systematic review commentary; narrative review | 2022, https://doi.org/10.1007/s12105-022-01453-6; 2021, https://doi.org/10.3390/cancers13153910 | (nonaka2022immunohistochemicalprofileof pages 8-10, iyer2021anoverviewon pages 11-12) |
| Prognosis | PAC generally has a favorable prognosis, but regional and distant metastases can occur and may become difficult to control; WHO renaming reflects recognition that behavior is not uniformly “low grade.” | No survival percentage, recurrence rate, or metastasis rate captured in current retrieved evidence. | Systematic review / meta-analysis; narrative review | 2022, https://doi.org/10.1007/s12105-022-01453-6; 2021, https://doi.org/10.3390/cancers13153910 | (nonaka2022immunohistochemicalprofileof pages 8-10, nonaka2022immunohistochemicalprofileof pages 1-3, iyer2021anoverviewon pages 11-12) |
| Evidence gaps | Current retrieved evidence is strongest for classification, morphology, and IHC; it is comparatively weak for PAC-specific epidemiology, environmental risk factors, treatment algorithms, survival statistics, and modern omics/clinical-trial data. | Missing from retrieved evidence: incidence/prevalence, sex ratio, age distribution, survival %, recurrence %, metastatic %, prospective trials, validated biomarkers beyond diagnostic adjuncts. | Evidence synthesis gap assessment | Based on retrieved 2021-2022 evidence | (nonaka2022immunohistochemicalprofileof pages 8-10, nonaka2022immunohistochemicalprofileof pages 1-3, iyer2021anoverviewon pages 11-12, nonaka2022immunohistochemicalprofileof pages 4-6) |


*Table: This table condenses the most relevant retrieved evidence on salivary gland polymorphous adenocarcinoma, emphasizing classification, diagnostic pathology, PRKD-related molecular findings, and where the current evidence remains limited.*

## 1. Disease information

### Definition and classification

PAC is an infiltrating salivary carcinoma characterized by **monomorphic tumor cells but polymorphous architecture**, including tubular, trabecular, cribriform, targetoid, papillary, and solid configurations. It was recognized as a distinct entity in 1984 under the name *polymorphous low-grade adenocarcinoma* (PLGA). WHO classification subsequently adopted *polymorphous adenocarcinoma*, reflecting the fact that not every tumor is biologically low grade. Cribriform adenocarcinoma of salivary gland is currently included in the PAC spectrum, although its precise taxonomic separation remains debated. (nonaka2022immunohistochemicalprofileof pages 1-3, iyer2021anoverviewon pages 11-12, nonaka2022immunohistochemicalprofileof pages 4-6)

**Synonyms:** polymorphous adenocarcinoma; polymorphous low-grade adenocarcinoma; PLGA; terminal duct carcinoma; lobular carcinoma of salivary gland. “Cribriform adenocarcinoma of salivary gland/minor salivary gland” and “cribriform adenocarcinoma of the tongue” are related historical terms, but should not be treated as exact synonyms without recording the cribriform subtype.

**Identifiers and coding:**

- **MONDO:** a PAC-specific MONDO identifier could not be verified from the retrieved primary literature; use the current MONDO release rather than inferring an identifier.
- **MeSH:** generally indexed under *Adenocarcinoma* and *Salivary Gland Neoplasms*; a uniquely specific MeSH descriptor was not established in the retrieved evidence.
- **ICD-10-CM:** coding is anatomical rather than histology-specific—typically C05.- for palate, C06.- for other/unspecified mouth, C08.0-C08.9 for other salivary glands, or another site-appropriate malignant-neoplasm code.
- **ICD-O:** malignant salivary tumor coding requires both a topography code and morphology code; the current registry/WHO edition should be consulted because older records may retain PLGA terminology.
- **OMIM/Orphanet:** PAC is a sporadic neoplasm, not an established Mendelian disorder; no disease-specific OMIM entry was verified. An Orphanet-specific identifier was not confirmed in the retrieved literature.
- **Suggested ontology concept:** NCIT *Polymorphous Adenocarcinoma*; MONDO mapping should be curated against the current release rather than generated from the name alone.

The information summarized here is **aggregated disease-level evidence** from systematic reviews and clinicopathologic literature, not individual EHR data. The 2022 immunohistochemical meta-analysis included **409 PAC cases from 32 studies published during 1988–2021**. (nonaka2022immunohistochemicalprofileof pages 1-3)

## 2. Etiology and risk factors

PAC is best understood as a **sporadic, somatically driven neoplasm**. PRKD alterations are tumor-acquired molecular drivers/diagnostic markers; they are not presently evidence of inherited susceptibility. No reproducible germline causal variant, Mendelian inheritance pattern, founder mutation, carrier frequency, or PAC-specific polygenic-risk model has been established in the retrieved evidence. (iyer2021anoverviewon pages 11-12)

No PAC-specific causal association has been demonstrated for tobacco, alcohol, diet, occupational toxins, ionizing radiation, pollution, chronic inflammation, or infectious agents. Age and female sex have been overrepresented in historical clinical series, but these are demographic associations rather than proven causal exposures. Likewise, no genetic or environmental protective factors and no validated gene–environment interaction are known. These conclusions denote **absence of established evidence**, not proof that such effects are impossible.

## 3. Phenotypes

PAC usually presents in adulthood as a **slow-growing, painless, firm submucosal mass**, most often on the palate. Ulceration, pain, paresthesia, dysphagia, dysarthria, or fixation can occur with larger, ulcerated, or nerve-involving lesions. The clinical course is commonly chronic and insidious. Regional lymph-node enlargement may be the first indication of a cribriform-subtype tumor. PAC can exhibit perineural invasion microscopically even without prominent neurologic symptoms. Architectural patterns include cribriform, tubular, and solid growth with infiltrative borders. (nonaka2022immunohistochemicalprofileof pages 8-10, nonaka2022immunohistochemicalprofileof pages 4-6)

Suggested phenotype annotations include:

- Oral mass — **HP:0031000, Oral cavity neoplasm** or the most specific current HPO neoplasm term.
- Palatal mass — map through oral-cavity neoplasm plus palate anatomy.
- Slow tumor growth — **HP:0003002, Breast carcinoma** is not appropriate; a general neoplasm/progression annotation should instead be represented in a disease-course ontology because HPO lacks a consistently granular “slow-growing tumor” term.
- Pain — **HP:0012531, Pain**.
- Dysphagia — **HP:0002015**.
- Dysarthria — **HP:0001260**.
- Paresthesia — **HP:0003401**.
- Enlarged cervical lymph nodes — **HP:0025280, Cervical lymphadenopathy**.
- Perineural invasion, recurrence, and metastasis are better represented using NCIT/SNOMED cancer-pathology concepts than patient-phenotype HPO terms.

Reliable phenotype frequencies, validated patient-reported outcome scores, and PAC-specific EQ-5D, SF-36, or PROMIS data were not identified. Quality-of-life effects therefore must be inferred from site and treatment: oral pain, impaired speech/swallowing, palatal defects, xerostomia after irradiation, and anxiety associated with prolonged recurrence surveillance.

## 4. Genetic and molecular information

### Core somatic alterations

The principal molecular association is **PRKD-family activation**. Conventional PAC is associated particularly with **PRKD1 E710D**, a hotspot missense substitution in the kinase domain. PRKD1 is located on chromosome 14 and encodes a serine/threonine protein kinase involved in cellular migration and differentiation and linked to RAS/MAPK-associated signaling. The mutation is an acquired tumor alteration and is used as an ancillary diagnostic marker rather than as a germline predictive test. (iyer2021anoverviewon pages 11-12)

Cribriform-subtype PAC is more often associated with rearrangements involving **PRKD1, PRKD2, or PRKD3**, with diverse fusion partners reported in the literature. Recent developments include increasingly broad RNA-sequencing identification of novel PRKD1 partners, reinforcing the concept that the conserved event is kinase-family dysregulation rather than one universal fusion partner. These rearrangements are structural somatic alterations; their population allele frequency is therefore not meaningfully assessed in gnomAD as an inherited allele.

**Variant interpretation:** PRKD1 E710D and recurrent PRKD-family fusions are oncogenic/pathogenic at the **somatic tumor level**. Germline ACMG/AMP categories should not automatically be applied to them. No validated inherited penetrance, anticipation, mosaic carrier risk, or reproductive recurrence risk is known.

### Immunophenotype and proliferation

A 2022 systematic review/meta-analysis found PAC positivity for pan-cytokeratin **97.3%**, CK7 **96.8%**, CK7/8 **97.4%**, E-cadherin **90%**, vimentin **92.5%**, S100 **97%**, p63 **91.7%**, and SOX10 **100%**. CK20 and p40 were reported as 0% positive, GFAP as 5%, and mean MIB-1/Ki-67 labeling index as **3.78%**. The practical profile is **CK7+/CK20−, S100+, vimentin+, p63+/p40−, GFAP−**. These data are aggregated and marker estimates may be affected by small denominators and inter-study assay variation. (nonaka2022immunohistochemicalprofileof pages 1-3)

No validated PAC-specific modifier genes, methylation signature in routine practice, proteomic/metabolomic/lipidomic signature, circulating biomarker, or inherited pharmacogenomic marker was identified. Recent methylation-classification work in salivary tumors is promising but is not yet a standard PAC diagnostic test.

## 5. Environmental information

No environmental, lifestyle, or infectious trigger is established specifically for PAC. Tobacco and alcohol are major exposures for mucosal squamous carcinoma but should not be imported as proven PAC risk factors. No bacterial, viral, fungal, or parasitic etiology is recognized. Consequently, there is no PAC-specific CHEBI toxicant annotation supported by current evidence.

## 6. Mechanism and pathophysiology

A plausible disease chain is:

1. A minor-salivary-gland epithelial progenitor acquires a **somatic PRKD1 hotspot mutation** or PRKD-family rearrangement.
2. Altered protein kinase D signaling affects kinase activity and downstream programs governing epithelial differentiation, adhesion, migration, and RAS/MAPK-linked signaling.
3. A cytologically uniform clone develops multiple architectural growth patterns.
4. Infiltrative and targetoid growth around nerves produces local tissue invasion and microscopic perineural invasion.
5. Additional, incompletely defined events may produce papillary/cribriform dominance, nodal spread, recurrence, or rare high-grade transformation. (iyer2021anoverviewon pages 11-12, nonaka2022immunohistochemicalprofileof pages 4-6)

The upstream event is the PRKD alteration; downstream features include altered migration/differentiation, infiltrative growth, perineural invasion, and metastatic competence. Evidence for the exact intermediate substrates and obligate downstream pathways remains largely inferential rather than established through PAC-specific functional screens.

**Suggested GO biological-process terms:** protein phosphorylation (**GO:0006468**), intracellular signal transduction (**GO:0035556**), MAPK cascade (**GO:0000165**), regulation of cell migration (**GO:0030334**), epithelial-cell differentiation (**GO:0030855**), cell adhesion (**GO:0007155**), and regulation of cell proliferation (**GO:0042127**).

**Suggested cell types:** salivary-gland epithelial cell; ductal epithelial cell (**CL mapping should be checked against the current Cell Ontology release**). No single-cell or spatial-transcriptomic atlas has yet established a PAC-specific cell of origin or tumor microenvironment. No reproducible PAC-specific immune, metabolic, autophagic, or oxidative-stress mechanism is established.

## 7. Anatomical structures affected

PAC predominantly affects **minor salivary gland tissue**, with the palate as the characteristic site. It can occur in the buccal mucosa, lip, retromolar region, floor of mouth, tongue/base of tongue, oropharynx, nasopharynx, and sinonasal tract; major-salivary-gland examples are uncommon. Diagnosis is particularly difficult in uncommon sites such as the oropharynx, sinonasal tract, and nasopharynx. (iyer2021anoverviewon pages 11-12, nonaka2022immunohistochemicalprofileof pages 4-6)

Secondary involvement may include adjacent oral soft tissue or bone, peripheral nerves, cervical lymph nodes, and—rarely—distant organs. Lesions are usually unilateral/localized rather than bilateral.

**Suggested anatomy terms:** UBERON palate (**UBERON:0001716**), tongue (**UBERON:0001723**), oral cavity (**UBERON:0000165**), salivary gland (**UBERON:0001044**), and minor salivary gland using the most specific current UBERON child term. Relevant compartments include plasma membrane, cytoplasm, and nucleus for signaling and transcriptional consequences; no disease-specific organelle pathology is established.

## 8. Temporal development

Onset is typically adult and insidious, although rare pediatric or adolescent cases have been reported. The untreated lesion usually enlarges slowly over months or years. Following excision, many patients remain disease-free, but recurrence may be delayed; long-term surveillance is therefore appropriate. There is no recognized premalignant stage, relapsing-remitting pattern, spontaneous remission, or developmental critical period.

Staging follows the **AJCC/UICC anatomic staging system for the primary site**, not a PAC-specific staging system. Clinically important progression events are increasing primary size/local invasion, positive margins, perineural invasion, nodal metastasis, distant metastasis, and rare high-grade transformation.

## 9. Inheritance, epidemiology, and population

PAC is rare and represents a small fraction of salivary malignancies, predominantly minor-salivary-gland cancers. A defensible disease-specific incidence per 100,000/year or point prevalence was not available in the retrieved evidence. Published population and institutional series suggest predominance in middle-aged to older adults and commonly a female excess, but precise ratios vary by cohort and should not be treated as universal.

There is no established autosomal-dominant, autosomal-recessive, X-linked, mitochondrial, polygenic, or familial inheritance pattern. PRKD alterations are somatic. Penetrance, carrier frequency, founder effect, consanguinity, genetic anticipation, and germline mosaicism are therefore not applicable under present knowledge. No consistent ethnic or geographic concentration has been demonstrated.

## 10. Diagnostics

### Standard work-up

Clinical examination should document lesion dimensions, mucosal ulceration, fixation, cranial-nerve symptoms, and cervical nodes. MRI is useful for deep extent and perineural disease; contrast-enhanced CT evaluates bone involvement and nodal disease. Ultrasound is useful principally for accessible neck nodes or major-gland lesions. Imaging is not histologically specific.

Fine-needle aspiration or core biopsy may suggest a salivary neoplasm, but PAC’s architectural heterogeneity and overlapping cytology can cause underclassification. Definitive diagnosis generally requires adequate tissue and correlation of architecture, cytology, invasion, immunophenotype, and—when necessary—molecular findings. PAC shows cytologic uniformity, architectural diversity, infiltrative borders, and sometimes myxohyaline matrix. (nonaka2022immunohistochemicalprofileof pages 4-6)

### Immunohistochemical and molecular testing

The most useful differential pattern is **p63-positive/p40-negative**. It was present in **38/39 PACs (97.4%)** versus **1/155 adenoid cystic carcinomas** in the underlying meta-analysis, with an odds ratio of **801.32 (p<0.00001)**. The reported ACC percentage of “0.006%” in the extracted source is arithmetically inconsistent with 1/155 (approximately 0.65%); the raw counts should therefore be retained in the knowledge base. (nonaka2022immunohistochemicalprofileof pages 8-10)

PRKD1 E710D testing can be performed by targeted DNA sequencing. Rearrangements are better assessed using break-apart FISH, anchored multiplex RNA sequencing, or another fusion-capable RNA panel. FISH has shown diagnostic utility for PRKD1 alterations, but a negative assay does not exclude PAC because alteration type and fusion partner vary. WES/WGS may identify alterations but are usually unnecessary for a localized, morphologically typical tumor; chromosomal microarray, karyotyping, mitochondrial sequencing, and repeat-expansion testing have no routine role. (iyer2021anoverviewon pages 11-12)

### Differential diagnosis

- **Adenoid cystic carcinoma:** often more hyperchromatic/biphasic, typically p40-positive in abluminal cells and commonly CD117-positive; MYB/MYBL1 rearrangement supports ACC. PAC’s p63+/p40− phenotype strongly favors PAC. (nonaka2022immunohistochemicalprofileof pages 8-10)
- **Pleomorphic adenoma:** circumscription, chondromyxoid stroma, and benign ductal/myoepithelial differentiation favor pleomorphic adenoma.
- **Secretory carcinoma:** mammaglobin/GATA3 positivity and an ETV6-family fusion favor secretory carcinoma.
- **Epithelial-myoepithelial carcinoma:** overt biphasic ductal and clear myoepithelial layers favor that diagnosis.
- **Clear-cell carcinoma:** hyalinizing stroma and EWSR1 rearrangement favor clear-cell carcinoma.
- **Low-grade papillary/cystic salivary tumors and metastatic tumors:** require site, morphology, and lineage-specific IHC/molecular correlation.

There is no population screening, liquid-biopsy assay, serum marker, or validated asymptomatic genetic test for PAC.

## 11. Outcome and prognosis

Conventional PAC generally has favorable disease-specific survival, but the label “low grade” was removed because regional and distant metastases can occur and occasionally become uncontrollable. Cribriform, papillary, solid, high-grade, or transformed morphology; nodal disease; advanced stage; incomplete excision; and recurrent disease are concerning features. (nonaka2022immunohistochemicalprofileof pages 8-10, nonaka2022immunohistochemicalprofileof pages 1-3, iyer2021anoverviewon pages 11-12)

The retrieved full-text evidence did not provide sufficiently robust PAC-specific 5- or 10-year survival, recurrence, nodal-metastasis, distant-metastasis, or disease-specific mortality estimates. Numerical estimates from older small series vary substantially with follow-up duration, inclusion of cribriform tumors, and historical diagnostic criteria. Such figures should not be merged without stratifying conventional PAC from cribriform subtype and high-grade transformation.

Potential long-term morbidity includes recurrent oral tumor, swallowing or speech impairment, palatal fistula/velopharyngeal dysfunction after resection, sensory deficits from nerve involvement, nodal surgery morbidity, and xerostomia or osteoradionecrosis after radiotherapy. PAC-specific validated quality-of-life statistics were not identified.

## 12. Treatment and real-world implementation

### Localized disease

**Complete surgical excision with negative margins** is the standard treatment. The operation is site dependent and may range from local mucosal excision to partial maxillectomy, tongue-base/oropharyngeal resection, or major-gland surgery. Reconstruction should preserve speech, swallowing, and separation of the oral and nasal cavities. Surgical resection is the principal treatment modality across salivary neoplasms, although disease-specific PAC prospective trials are lacking. (iyer2021anoverviewon pages 11-12)

Suggested NCIT concepts include **Surgical Resection**, **Wide Local Excision**, **Partial Maxillectomy**, **Neck Dissection**, **External Beam Radiation Therapy**, **Intensity-Modulated Radiation Therapy**, and **Supportive Care**; exact NCIT codes should be validated against the current release.

Elective neck dissection is not routine for a small clinically node-negative conventional PAC. Therapeutic neck dissection is appropriate for confirmed nodal disease. Greater consideration of nodal evaluation is reasonable for cribriform-subtype, tongue-base, advanced, or clinically node-positive tumors.

Postoperative radiotherapy is individualized for positive/unresectable margins, advanced local disease, extensive perineural invasion, nodal disease, recurrent disease, or high-grade transformation. There is no PAC-specific randomized evidence demonstrating an overall-survival advantage for routine adjuvant irradiation after complete excision of a low-risk lesion.

### Recurrent or metastatic disease

Resectable local or nodal recurrence is usually managed with salvage surgery, with radiotherapy considered according to prior treatment and risk. For unresectable/metastatic PAC, treatment is extrapolated from broader salivary-carcinoma practice: palliative irradiation, cytotoxic therapy, or biomarker-directed therapy if an independently actionable alteration is found. No PRKD inhibitor, immunotherapy, gene therapy, cell therapy, or RNA therapy is approved specifically for PAC, and PRKD alterations are presently more useful diagnostically than therapeutically.

The clinical-trial search did not identify a clearly PAC-specific interventional study. Enrollment in histology-agnostic or rare-salivary-cancer trials may be considered for advanced disease after comprehensive DNA/RNA profiling, but expected benefit cannot be inferred merely from a PRKD alteration.

Supportive care may include dental evaluation, nutritional support, speech/swallow therapy, prosthodontic obturation or reconstructive rehabilitation, analgesia, xerostomia management, and surveillance for recurrence.

## 13. Prevention

No primary prevention strategy, vaccine, prophylactic drug, or validated lifestyle intervention is known because no modifiable PAC-specific cause has been established. Population screening and germline cascade screening are not recommended. Secondary prevention consists of prompt evaluation and biopsy of a persistent palatal or other minor-salivary-gland mass. Tertiary prevention includes complete initial excision, management of adverse pathology, oral/dental rehabilitation, and prolonged surveillance for delayed recurrence.

Routine genetic counseling is not indicated solely because a tumor harbors PRKD1 E710D or a PRKD fusion; counseling would become relevant only if personal/family history suggested a separate hereditary cancer syndrome.

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart specifically matching human PRKD-altered PAC was identified. Salivary carcinomas occur in dogs, cats, and other mammals, but histologic resemblance alone does not establish molecular equivalence. There is no zoonotic potential or cross-species transmission. Human taxonomy is **Homo sapiens, NCBI Taxon 9606**. Orthologues of PRKD-family genes exist in model species, but conservation of the genes does not by itself validate an animal PAC model.

## 15. Model organisms and experimental systems

No widely accepted PAC-specific genetically engineered mouse, patient-derived xenograft, organoid, or continuously available reference cell line was identified. Generic PRKD gain-of-function systems may study kinase signaling but do not reproduce the salivary architecture, perineural invasion, or prolonged clinical course of PAC. Important future models would include:

1. salivary epithelial organoids engineered with PRKD1 E710D;
2. conditional salivary-epithelial PRKD1 knock-in mice;
3. fusion-positive cribriform-subtype organoids or xenografts; and
4. spatial/single-cell studies comparing conventional and cribriform PAC.

These are research priorities rather than established resources. The absence of validated models limits causal pathway dissection and preclinical therapeutic testing.

## Recent developments, evidence appraisal, and authoritative interpretation

The principal recent advance is refinement of PAC as a **molecularly coherent PRKD-family tumor spectrum**, accompanied by recognition that conventional mutation-positive PAC and fusion-positive cribriform tumors may differ clinically. The 2022 meta-analysis supplied the most quantitative diagnostic evidence: a broad epithelial/S100/SOX10 phenotype and the highly discriminating p63+/p40− pattern. Its abstract-level conclusion characterizes PAC as a malignant minor-salivary-gland tumor with “morphological diversity, an infiltrative growth pattern, and low metastatic potential”—a useful concise disease definition. (nonaka2022immunohistochemicalprofileof pages 1-3)

Expert interpretation should remain conservative: morphology is primary; IHC is supportive rather than independently definitive; and PRKD testing is most valuable in small biopsies, unusual sites, or difficult differentials. Rare-head-and-neck-tumor reviews emphasize specialist pathology review, molecular analysis where appropriate, and multidisciplinary management. The limited number of prospective studies means that management recommendations rest mostly on retrospective human series and extrapolation from salivary-cancer guidelines, not randomized PAC trials. (iyer2021anoverviewon pages 11-12, nonaka2022immunohistochemicalprofileof pages 4-6)

## Key sources and publication details

1. Nonaka T, Takei H. **Immunohistochemical Profile of Polymorphous Adenocarcinoma of Minor Salivary Gland: A Systematic Review and Meta-Analysis.** *Head and Neck Pathology.* Published May 2022;16:980–990. DOI/URL: https://doi.org/10.1007/s12105-022-01453-6. Evidence type: systematic review/meta-analysis of 409 cases. (nonaka2022immunohistochemicalprofileof pages 8-10, nonaka2022immunohistochemicalprofileof pages 1-3, nonaka2022immunohistochemicalprofileof pages 4-6)
2. Iyer J, et al. **An Overview on the Histogenesis and Morphogenesis of Salivary Gland Neoplasms and Evolving Diagnostic Approaches.** *Cancers.* Published August 2021;13:3910. DOI/URL: https://doi.org/10.3390/cancers13153910. Evidence type: peer-reviewed molecular/pathology review. (iyer2021anoverviewon pages 11-12)

PMIDs were not exposed in the retrieved full-text metadata and are therefore not supplied speculatively. Likewise, exact abstract quotations beyond text present in the retrieved evidence have not been fabricated. Primary-study claims that could not be verified in accessible full text have been identified as evidence gaps rather than assigned unsupported statistics.

References

1. (nonaka2022immunohistochemicalprofileof pages 1-3): Taichiro Nonaka and Hidehiro Takei. Immunohistochemical profile of polymorphous adenocarcinoma of minor salivary gland: a systematic review and meta-analysis. Head and Neck Pathology, 16:980-990, May 2022. URL: https://doi.org/10.1007/s12105-022-01453-6, doi:10.1007/s12105-022-01453-6. This article has 19 citations and is from a peer-reviewed journal.

2. (iyer2021anoverviewon pages 11-12): Janaki Iyer, Arvind Hariharan, Uyen Minh Nha Cao, Crystal To Tam Mai, Athena Wang, Parisa Khayambashi, Bich Hong Nguyen, Lydia Safi, and Simon D. Tran. An overview on the histogenesis and morphogenesis of salivary gland neoplasms and evolving diagnostic approaches. Cancers, 13:3910, Aug 2021. URL: https://doi.org/10.3390/cancers13153910, doi:10.3390/cancers13153910. This article has 67 citations.

3. (nonaka2022immunohistochemicalprofileof pages 4-6): Taichiro Nonaka and Hidehiro Takei. Immunohistochemical profile of polymorphous adenocarcinoma of minor salivary gland: a systematic review and meta-analysis. Head and Neck Pathology, 16:980-990, May 2022. URL: https://doi.org/10.1007/s12105-022-01453-6, doi:10.1007/s12105-022-01453-6. This article has 19 citations and is from a peer-reviewed journal.

4. (nonaka2022immunohistochemicalprofileof pages 8-10): Taichiro Nonaka and Hidehiro Takei. Immunohistochemical profile of polymorphous adenocarcinoma of minor salivary gland: a systematic review and meta-analysis. Head and Neck Pathology, 16:980-990, May 2022. URL: https://doi.org/10.1007/s12105-022-01453-6, doi:10.1007/s12105-022-01453-6. This article has 19 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Salivary_Gland_Polymorphous_Adenocarcinoma-deep-research-falcon_artifacts/artifact-00.md)