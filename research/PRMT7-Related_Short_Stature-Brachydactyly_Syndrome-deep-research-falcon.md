---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T18:44:36.825283'
end_time: '2026-08-01T18:52:09.304529'
duration_seconds: 452.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: PRMT7-Related Short Stature-Brachydactyly Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 13
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: PRMT7-Related_Short_Stature-Brachydactyly_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PRMT7-Related Short Stature-Brachydactyly Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PRMT7-Related Short Stature-Brachydactyly Syndrome** covering all of the
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
- **Disease Name:** PRMT7-Related Short Stature-Brachydactyly Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PRMT7-Related Short Stature-Brachydactyly Syndrome** covering all of the
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


# PRMT7-Related Short Stature–Brachydactyly Syndrome: Research Report

## Executive summary

PRMT7-related short stature–brachydactyly syndrome is an ultra-rare autosomal-recessive neurodevelopmental disorder caused by biallelic variants in **PRMT7**. It is commonly called **SBIDDS**—short stature, brachydactyly, intellectual developmental disability, and seizures—and is also described as *PRMT7-related disorder* or *short stature, brachydactyly, intellectual developmental disability, and seizures syndrome*. The defining clinical combination is developmental delay/intellectual disability, hypotonia, short stature, brachydactyly/metacarpal-metatarsal shortening, characteristic craniofacial morphology, variably occurring seizures, and frequently later-onset obesity.

The best current clinical evidence is the January 2023 *Genetics in Medicine* study of 51 affected people from 39 families. This remains a small, largely cross-sectional cohort rather than a population-based natural-history study; therefore, percentages below should be interpreted as observed cohort frequencies, not definitive penetrance estimates. (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 1-2)

| Domain | Best-supported finding | Quantitative data | Evidence type | Suggested ontology terms |
|---|---|---:|---|---|
| Disease definition | PRMT7-related SBIDDS is a recognizable syndromic neurodevelopmental disorder caused by biallelic PRMT7 variants; OMIM phenotype entry reported as 617157 (cali2023biallelicprmt7pathogenic pages 1-2, cali2023biallelicprmt7pathogenic pages 2-5) | 51 affected individuals from 39 families in the largest cohort (cali2023biallelicprmt7pathogenic pages 1-2) | Human clinical cohort | OMIM 617157; MONDO: not established here; disease label: PRMT7-related short stature-brachydactyly syndrome / SBIDDS |
| Synonyms | Common labels include SBIDDS and PRMT7-related disorder; expanded 2023 description emphasizes short stature, obesity, craniofacial and digital abnormalities (halabelian2021structureandfunction pages 8-9, cali2023biallelicprmt7pathogenic pages 5-6) | N/A | Human clinical + review | SBIDDS; “PRMT7-related disorder” |
| Core neurodevelopmental phenotype | Global developmental delay / intellectual disability was universal in the 2023 cohort (cali2023biallelicprmt7pathogenic pages 1-2, cali2023biallelicprmt7pathogenic pages 5-6) | 100% GDD/ID; severity mild 27%, moderate 33%, severe 40% (cali2023biallelicprmt7pathogenic pages 1-2) | Human clinical cohort | HPO: Global developmental delay (HP:0001263); Intellectual disability (HP:0001249) |
| Seizures | Seizures are a major but non-universal feature, often treatment-responsive (cali2023biallelicprmt7pathogenic pages 1-2) | 67–70%; median onset 3 years; range 7 months–45 years; ~16% intractable (cali2023biallelicprmt7pathogenic pages 1-2) | Human clinical cohort | HPO: Seizure (HP:0001250) |
| Growth phenotype | Short stature is one of the defining manifestations (cali2023biallelicprmt7pathogenic pages 1-2, cali2023biallelicprmt7pathogenic pages 5-6) | ~80% short stature (cali2023biallelicprmt7pathogenic pages 1-2, cali2023biallelicprmt7pathogenic pages 5-6) | Human clinical cohort | HPO: Short stature (HP:0004322) |
| Digital/skeletal phenotype | Brachydactyly with metacarpal/metatarsal shortening is characteristic (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 5-6) | ~70% brachydactyly; delayed bone age ~50%; decreased bone density ~40% (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 1-2) | Human clinical cohort | HPO: Brachydactyly (HP:0001156); Delayed bone age (HP:0002750); Decreased bone mineral density (standard HPO label) |
| Hypotonia | Hypotonia is frequent early in life (cali2023biallelicprmt7pathogenic pages 1-2) | 88% (cali2023biallelicprmt7pathogenic pages 1-2) | Human clinical cohort | HPO: Hypotonia (HP:0001252) |
| Head size | Microcephaly occurs in a substantial subset, but is not universal (cali2023biallelicprmt7pathogenic pages 1-2) | ~40% (cali2023biallelicprmt7pathogenic pages 1-2) | Human clinical cohort | HPO: Microcephaly (HP:0000252) |
| Obesity/metabolic phenotype | Obesity is common and tends to emerge later, especially after puberty (cali2023biallelicprmt7pathogenic pages 5-6) | ~50–54%; delayed onset, often >10 years (cali2023biallelicprmt7pathogenic pages 5-6, cali2023biallelicprmt7pathogenic pages 1-2) | Human clinical cohort | HPO: Obesity (HP:0001513) |
| Prenatal/perinatal findings | Prenatal growth impairment is relatively common (cali2023biallelicprmt7pathogenic pages 2-5) | Intrauterine growth restriction / prenatal manifestations ~45–55%; small for gestational age ~46–50% (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 5-6) | Human clinical cohort | HPO: Intrauterine growth restriction (HP:0001511); Small for gestational age (HP:0001518) |
| Craniofacial phenotype | Distinctive facial gestalt supports recognition in clinic (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 5-6) | Frontal bossing ~70%; prognathism 72.5%; tall/prominent chin ~75% (cali2023biallelicprmt7pathogenic pages 2-5) | Human clinical cohort | HPO: Frontal bossing (HP:0002007); Prognathism (HP:0000303) |
| Ophthalmologic / auditory findings | Strabismus and hearing impairment are recurrent associated findings (cali2023biallelicprmt7pathogenic pages 2-5) | Strabismus ~45%; hearing impairment ~30% (cali2023biallelicprmt7pathogenic pages 2-5) | Human clinical cohort | HPO: Strabismus (HP:0000486); Hearing impairment (HP:0000365) |
| Neuroimaging | Brain MRI may be normal or show nonspecific abnormalities (cali2023biallelicprmt7pathogenic pages 2-5) | 13/37 MRIs unremarkable; others nonspecific (ventricular enlargement, white-matter changes) (cali2023biallelicprmt7pathogenic pages 2-5) | Human clinical cohort | HPO: Abnormal brain MRI (standard label) |
| Gene | The causal gene is PRMT7 (OMIM *610087), encoding a protein arginine methyltransferase (cali2023biallelicprmt7pathogenic pages 1-2, halabelian2021structureandfunction pages 8-9) | Single established causal gene in current evidence base (cali2023biallelicprmt7pathogenic pages 2-5) | Human genetics + review | HGNC: PRMT7; OMIM *610087 |
| Inheritance | Disease is autosomal recessive due to biallelic PRMT7 variants (cali2023biallelicprmt7pathogenic pages 1-2, cali2023biallelicprmt7pathogenic pages 5-6) | 25 compound heterozygous, 26 homozygous; consanguinity in 44% of families (cali2023biallelicprmt7pathogenic pages 2-5) | Human clinical cohort | HP:0000007 Autosomal recessive inheritance |
| Variant spectrum | The cohort showed broad allelic heterogeneity, mostly loss-of-function classes but also missense and splice variants (cali2023biallelicprmt7pathogenic pages 2-5) | 46 variants total; 34 novel; 19 truncating (9 frameshift, 10 nonsense), 1 in-frame deletion, 9 splice, 14 missense, 3 large indels; 28 pathogenic, 3 likely pathogenic, 12 VUS (cali2023biallelicprmt7pathogenic pages 2-5) | Human clinical cohort | Sequence variant classes: nonsense, frameshift, splice-site, missense, in-frame deletion, indel |
| Diagnostic approach | Current real-world diagnosis relies on next-generation sequencing with confirmatory segregation testing and phenotype review (cali2023biallelicprmt7pathogenic pages 1-2, cali2023biallelicprmt7pathogenic pages 2-5) | Largest study: candidate variants confirmed by Sanger sequencing; dysmorphology assessment aided recognition (cali2023biallelicprmt7pathogenic pages 2-5) | Human clinical practice / cohort | NCIT: Sanger Sequencing; Whole exome/genome sequencing (standard labels); HPO-based phenotyping |
| Differential diagnosis | Differential diagnosis overlaps with other syndromic obesity / neurodevelopmental disorders (cali2023biallelicprmt7pathogenic pages 5-6) | Named comparators include Börjeson-Forssman-Lehmann, CHOPS, Chung-Jansen, Cohen, TRAPPC9-related disorders (cali2023biallelicprmt7pathogenic pages 5-6) | Human clinical interpretation | No ontology IDs asserted here |
| Mechanism: enzyme function | PRMT7 is a type III protein arginine methyltransferase that catalyzes arginine monomethylation; chromatin and non-histone substrates are implicated (halabelian2021structureandfunction pages 8-9, halabelian2021structureandfunction pages 6-8, halabelian2021structureandfunction pages 5-6) | Qualitative; no disease-specific patient biomarker established (cali2023biallelicprmt7pathogenic pages 8-8) | Review + in vitro + model organism | GO: protein arginine methyltransferase activity; histone arginine methylation |
| Mechanism: neuronal | Experimental work links PRMT7 loss to altered neuronal excitability and developmental pathways, providing a plausible basis for ID/seizures, but not yet a complete human causal chain (halabelian2021structureandfunction pages 8-9, cali2023biallelicprmt7pathogenic pages 2-5) | Qualitative | Model organism / in vitro | GO: regulation of neuron excitability; Cell Ontology: neuron |
| Mechanism: muscle/metabolism | Prmt7 deficiency in mice causes reduced skeletal muscle oxidative metabolism and age-related obesity, aligning with the human obesity/endurance phenotype (halabelian2021structureandfunction pages 8-9, halabelian2021structureandfunction pages 6-8) | Qualitative; mouse phenotypes include age-related obesity and reduced oxidative metabolism (halabelian2021structureandfunction pages 8-9) | Model organism | GO: skeletal muscle tissue development; oxidative phosphorylation; adipogenesis |
| Mechanism: bone/growth | Mouse data support a role in skeletal growth and bone formation; review reports reduced body size, shortened fifth metatarsals, and reduced bone mineral content in knockout mice (halabelian2021structureandfunction pages 8-9). A 2024 preprint links PRMT7 to PTEN-mediated osteogenesis and female-specific dwarfism in conditional knockout mice (zhang2024prmt7mediatedpten pages 4-7) | Qualitative; 2024 report notes dwarfism by 6 weeks in female CKO mice (zhang2024prmt7mediatedpten pages 4-7) | Model organism; 2024 evidence includes preprint | GO: ossification; osteoblast differentiation; Cell Ontology: osteoblast, bone marrow mesenchymal stem cell |
| Management | No disease-modifying therapy is established; care is supportive and symptom-directed, especially seizure management, developmental services, and surveillance of growth/obesity/skeletal issues (cali2023biallelicprmt7pathogenic pages 1-2, cali2023biallelicprmt7pathogenic pages 6-7) | Most seizures responsive to topiramate / sodium valproate; ~16% intractable (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 1-2) | Human clinical cohort | NCIT: Anticonvulsant Therapy; Physical Therapy; Occupational Therapy; Genetic Counseling |
| Current applications / implementation | Main current application is rare-disease molecular diagnosis and family counseling; syndrome recognition can improve testing yield and management planning (cali2023biallelicprmt7pathogenic pages 6-7, cali2023biallelicprmt7pathogenic pages 5-6) | 2023 cohort expanded recognizable phenotype to 51 individuals (cali2023biallelicprmt7pathogenic pages 2-5) | Clinical implementation | NCIT: Genetic Counseling; Molecular Diagnostic Testing |
| Clinical trials | No disease-specific interventional trial was identified in the available search results (tool search summary; no relevant PRMT7/SBIDDS trial returned) | 0 relevant disease-specific trials identified | Trial search / evidence gap | Not applicable |
| Unknowns / evidence gaps | Prevalence, incidence, penetrance, carrier frequency, founder variants, validated biomarkers, mortality, life expectancy, quality-of-life instruments, and gene-specific prevention strategies remain unestablished in the available literature (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 8-8) | Not reported in retrieved evidence | Evidence gap | Not applicable |


*Table: This table summarizes the strongest currently available evidence for PRMT7-related SBIDDS, centered on the 2023 51-person cohort and supported by mechanistic model data. It is useful for rapid knowledge-base population because it combines phenotype frequencies, inheritance and variant classes, diagnostics, management, and explicit evidence gaps in one place.*

## 1. Disease information

### Definition and identifiers

* **Disease:** Mendelian syndromic neurodevelopmental disorder caused by biallelic PRMT7 variants.
* **OMIM phenotype:** **617157**.
* **Causal gene:** **PRMT7**, OMIM **610087**.
* **Inheritance:** Autosomal recessive.
* **Common names:** SBIDDS; PRMT7-related disorder; PRMT7-related short stature–brachydactyly syndrome; short stature, brachydactyly, intellectual developmental disability, and seizures syndrome.
* **MONDO:** A stable MONDO identifier was not established from the retrieved authoritative evidence; it should not be inferred from the OMIM number.
* **Orphanet, MeSH, ICD-10/ICD-11:** No disease-specific identifiers were established in the retrieved evidence. In practice, broader codes for genetic neurodevelopmental disorder, intellectual disability, epilepsy, short stature, or congenital malformations may be used, but these are not equivalent to a disease-specific code.

The 2023 paper describes the condition as a “recognizable syndromic neurodevelopmental disorder with short stature, obesity, and craniofacial and digital abnormalities.” It combined 36 newly described individuals with 15 previously reported individuals. DOI: [10.1016/j.gim.2022.09.016](https://doi.org/10.1016/j.gim.2022.09.016), published January 2023. (cali2023biallelicprmt7pathogenic pages 1-2)

The evidence is principally **aggregated disease-level research assembled from individually phenotyped patients and literature cases**, not an EHR-derived population dataset. Photographs, clinical records, sequencing results, and segregation studies contributed to the cohort characterization. (cali2023biallelicprmt7pathogenic pages 2-5)

## 2. Etiology, risk, and protective factors

The primary and presently sufficient cause is **germline biallelic variation in PRMT7**. The cohort contained 25 compound-heterozygous and 26 homozygous individuals, supporting a recessive disease model. Consanguinity was recorded in 44% of families, increasing the probability of homozygosity but not constituting an independent biological cause. (cali2023biallelicprmt7pathogenic pages 2-5)

No reproducible susceptibility loci, modifier genes, genetic protective alleles, environmental causes, toxins, infections, dietary factors, or gene–environment interactions have been demonstrated for SBIDDS. Sex is not an established human risk modifier: the largest cohort included 23 males and 28 females. Family history and parental relatedness affect recurrence probability rather than severity in a proven manner. (cali2023biallelicprmt7pathogenic pages 2-5)

Environmental and lifestyle factors may modify secondary obesity, fitness, or bone health in the same general way they do in other patients, but there is no evidence that they cause or prevent the syndrome. The female-specific skeletal phenotype reported in a 2024 conditional-mouse study is hypothesis-generating and cannot yet be treated as evidence of sex-specific human penetrance. (zhang2024prmt7mediatedpten pages 4-7)

## 3. Phenotypes and quality-of-life implications

### Neurodevelopment

Global developmental delay or intellectual disability occurred in **100%** of the 2023 cohort: 27% mild, 33% moderate, and 40% severe. Hypotonia occurred in approximately **88%**. These congenital/early-childhood manifestations are chronic rather than episodic and commonly affect mobility, communication, learning, independence, and educational needs. Suggested HPO terms are **Global developmental delay (HP:0001263)**, **Intellectual disability (HP:0001249)**, and **Hypotonia (HP:0001252)**. (cali2023biallelicprmt7pathogenic pages 1-2)

### Seizures and brain findings

Approximately **67–70%** developed seizures. Median onset was three years, with a wide reported range of seven months to 45 years. Generalized-onset seizures predominated among characterized cases, although focal seizures also occurred. Most responded to treatment; approximately **16%** were intractable. Suggested term: **Seizure (HP:0001250)**. (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 1-2)

MRI is not diagnostic: 13 of 37 reported scans were unremarkable, while other patients had heterogeneous, nonspecific findings such as ventricular enlargement or white-matter abnormalities. A normal MRI therefore does not exclude the disorder. (cali2023biallelicprmt7pathogenic pages 2-5)

### Growth, skeleton, and digits

Short stature occurred in approximately **80%**, and brachydactyly in approximately **70%**. Hand/foot radiographs may show shortened metacarpals or metatarsals. Delayed bone age was reported in about **50%** and decreased bone density in about **40%** of assessed patients. Suggested terms include **Short stature (HP:0004322)**, **Brachydactyly (HP:0001156)**, **Delayed bone age (HP:0002750)**, and decreased bone mineral density. (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 5-6, cali2023biallelicprmt7pathogenic pages 1-2)

Prenatal growth disturbance is frequent but not universal: roughly 45–55% had intrauterine growth restriction or other prenatal manifestations, and approximately 46–50% were small for gestational age. Suggested terms: **Intrauterine growth retardation (HP:0001511)** and **Small for gestational age (HP:0001518)**. (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 5-6)

### Obesity and muscle-related manifestations

Obesity occurred in approximately **50–54%** and was more prevalent after age ten or after puberty, suggesting an age-dependent phenotype rather than a universal congenital feature. Some patients had reduced exercise endurance. Suggested term: **Obesity (HP:0001513)**. (cali2023biallelicprmt7pathogenic pages 5-6, cali2023biallelicprmt7pathogenic pages 1-2)

### Craniofacial, ophthalmic, auditory, and other findings

The recognizable gestalt includes bifrontal narrowing or frontal bossing, prominent supraorbital ridges, sparse eyebrows, a short nose with broad tip, thin upper lip, full/everted lower lip, and prominent or squared jaw/chin. Reported frequencies included frontal bossing around 70%, prognathism 72.5%, and tall/prominent chin 75%. Strabismus occurred in approximately 45%, hearing impairment in 30%, microcephaly in 40%, and failure to thrive in 51%. Suggested terms include **Frontal bossing (HP:0002007)**, **Prognathism (HP:0000303)**, **Strabismus (HP:0000486)**, **Hearing impairment (HP:0000365)**, and **Microcephaly (HP:0000252)**. (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 1-2)

No disease-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or other formal quality-of-life study was identified. Functional burden is inferred from intellectual disability, seizures, hypotonia, reduced endurance, sensory impairment, short stature, and obesity—not quantified by validated instruments. (cali2023biallelicprmt7pathogenic pages 2-5)

## 4. Genetic and molecular information

**PRMT7** encodes protein arginine methyltransferase 7. The 2023 cohort reported **46 variants, 34 novel**: 19 truncating variants (nine frameshift and ten nonsense), nine splice variants, 14 missense variants, one in-frame deletion, and three large indels. Reported classifications were 28 pathogenic, three likely pathogenic, and 12 variants of uncertain significance; interpretation of a VUS requires segregation, phenotype, population, and functional evidence and should not be treated as diagnostic by itself. (cali2023biallelicprmt7pathogenic pages 2-5)

The broad distribution of nonsense, frameshift, splice-disrupting, and deletion alleles supports **loss of function** as the predominant mechanism. Disease-associated variants are germline; no somatic disease mechanism is established. The retrieved main-text evidence did not expose a reliable complete HGVS-level variant list or variant-specific gnomAD frequencies, so these should be imported directly from the paper’s supplement and ClinVar rather than reconstructed. No validated modifier gene, founder allele, recurrent protective allele, chromosomal rearrangement syndrome, anticipation, or established germline-mosaicism rate has been reported. (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 5-6)

PRMT7 regulates both histone and nonhistone substrates. It is generally characterized as the mammalian type III PRMT catalyzing arginine monomethylation, although older literature reports context-dependent symmetric dimethyl marks. Known experimental substrates or pathways include histones, HSP70, RNA-binding proteins, NALCN, p38-MAPK/eIF2α-related stress biology, and chromatin regulators. Exact disease-relevant substrates in human developing brain, growth plate, and digits remain unresolved. (halabelian2021structureandfunction pages 8-9, halabelian2021structureandfunction pages 6-8, halabelian2021structureandfunction pages 5-6)

## 5. Environmental information

No toxin, radiation exposure, pollutant, occupation, smoking, alcohol, diet, exercise pattern, or infectious agent is known to initiate SBIDDS. It is not infectious or transmissible. Lifestyle management may influence obesity, mobility, cardiovascular risk, or bone density after diagnosis but cannot correct the underlying biallelic genotype. No SBIDDS-specific CTD-type chemical association or infectious trigger was supported by the retrieved literature.

## 6. Mechanism and pathophysiology

### Evidence-calibrated causal model

The most defensible upstream chain is:

**biallelic PRMT7 loss-of-function → reduced or altered protein-arginine methylation and chromatin/nonhistone regulation → tissue-specific disturbances of developmental gene expression, neuronal excitability, muscle metabolism, adipogenesis, and osteogenesis → developmental disability/seizures, hypotonia/reduced endurance, later obesity, short stature, low bone density, and digital abnormalities.**

The first link is firmly supported by human genetics; most intermediate links derive from cell and animal models and are not yet validated molecular biomarkers in patients. (cali2023biallelicprmt7pathogenic pages 2-5)

### Neuronal mechanisms

PRMT7 has experimental links to neuronal development through MLL4/Wnt-related chromatin regulation and to excitability through ion-channel regulation. In mouse dentate granule neurons, PRMT7 methylation of NALCN at Arg1653 promotes inhibitory phosphorylation; deficiency increases firing through enhanced NALCN signaling. These observations provide plausible mechanisms for seizures and neurodevelopmental impairment but do not establish that NALCN dysregulation is the sole human disease mechanism. Suggested terms: **GO regulation of neuron excitability**, **GO nervous system development**; cell terms **neuron**, **dentate granule cell**, and **hippocampal pyramidal neuron**. (halabelian2021structureandfunction pages 8-9, cali2023biallelicprmt7pathogenic pages 2-5)

### Muscle, adipose, and metabolism

Whole-body Prmt7-deficient mice exhibit impaired muscle regeneration, loss of the PAX7-positive satellite-cell pool, reduced oxidative metabolism/PGC-1α expression, altered fiber composition, and age-associated obesity. PRMT7 loss also promotes adipogenesis through C/EBP-β/PPAR-γ-related regulation. These findings align with human hypotonia, reduced endurance, and delayed obesity, but patient muscle transcriptomic or metabolomic confirmation is unavailable. Suggested terms: **GO muscle cell differentiation**, **GO skeletal muscle tissue regeneration**, **GO oxidative phosphorylation**, **GO adipocyte differentiation**; cells **skeletal muscle satellite cell**, **myoblast**, **myofiber**, and **adipocyte**. (halabelian2021structureandfunction pages 8-9, halabelian2021structureandfunction pages 12-13, halabelian2021structureandfunction pages 6-8)

### Bone and craniofacial mechanisms—2024 development

Prmt7-knockout mice show reduced body size, shortened fifth metatarsals, and reduced bone mineral content, reproducing key aspects of human growth and digital disease. (halabelian2021structureandfunction pages 8-9)

A July 31, 2024 bioRxiv preprint reported that PRMT7 promotes osteogenesis through PTEN: H3R2me1 enrichment at the PTEN promoter enhanced transcription, while a separate methyltransferase-independent effect stabilized nuclear PTEN. Conditional loss in Prrx1- or Sp7-lineage cells caused female-specific dwarfism by six weeks, impaired long-bone formation/regeneration, reduced trabecular bone and mineral density, and craniofacial/dental abnormalities; PRMT7 deficiency reduced alkaline-phosphatase activity and RUNX2 expression in mouse and human bone-marrow mesenchymal stem cells. DOI: [10.1101/2024.07.31.605998](https://doi.org/10.1101/2024.07.31.605998). Because this is preprint/model evidence and sex specificity has not been established in patients, it should be annotated as provisional. Suggested terms: **GO ossification**, **GO osteoblast differentiation**, **GO bone development**; cells **bone-marrow mesenchymal stem cell** and **osteoblast**. (zhang2024prmt7mediatedpten pages 4-7)

### Other tissue mechanisms

Experimental Prmt7 loss can disrupt alveolar myofibroblast proliferation/differentiation and FOXM1-associated alveologenesis, and cardiomyocyte deletion can produce hypertrophy/fibrosis through β-catenin dysregulation. These are tissue-specific mouse findings, not established routine manifestations of human SBIDDS, and should not be converted into human phenotype assertions without clinical evidence.

No SBIDDS patient-level single-cell atlas, spatial transcriptomic study, proteomic signature, metabolomic/lipidomic biomarker, integrated multi-omics study, organoid model, or disease-focused CRISPR screen was identified. The available molecular profiling is predominantly bulk transcriptomic or targeted biochemical work in experimental systems.

## 7. Anatomical structures affected

The primary clinically affected systems are the **central nervous system**, **skeleton/growth apparatus**, **digits**, **craniofacial complex**, **skeletal muscle**, and **adipose/metabolic system**. Secondary/recurrent involvement includes eyes and auditory pathways. Suggested anatomical annotations include brain, cerebral white matter, skeletal system, long bone, metacarpal bone, metatarsal bone, hand digit, foot digit, craniofacial skeleton, skeletal muscle, and adipose tissue; exact UBERON identifiers should be ontology-validated during ingestion rather than guessed.

At cell level, plausible affected populations are neurons, neural progenitors, skeletal-muscle satellite cells/myoblasts, adipocytes and precursors, bone-marrow mesenchymal stromal cells, osteoblast-lineage cells, and growth-plate chondrocytes. Direct patient evidence is strongest for organ-level phenotype; cell assignments are largely mechanistic extrapolations from models. (halabelian2021structureandfunction pages 8-9, zhang2024prmt7mediatedpten pages 4-7, cali2023biallelicprmt7pathogenic pages 2-5)

At subcellular level, PRMT7 acts in the **nucleus/chromatin** and cytoplasmic protein/RNA complexes. Suggested GO cellular components include nucleus, chromatin, cytoplasm, and protein-containing complex. Lateralization is not characteristic: short stature, brachydactyly, and craniofacial findings are generally systemic/bilateral rather than consistently unilateral.

## 8. Temporal development

The condition is congenital and lifelong, although different components emerge at different ages. Prenatal growth restriction may be detectable before birth. Hypotonia and developmental delay usually become evident in infancy or early childhood. Short stature and brachydactyly become clearer with growth; seizures have highly variable onset, including rare adult onset. Obesity is frequently delayed until later childhood, adolescence, or after puberty. (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 1-2)

There is no validated staging system. The course is best understood as chronic neurodevelopmental disability with age-dependent emergence of seizures, skeletal findings, and obesity, rather than relapsing-remitting disease. Seizures may remit or become controlled with medication, but genetic and developmental manifestations do not spontaneously resolve. Critical practical periods include early developmental intervention, early seizure recognition, longitudinal growth/bone surveillance, and anticipatory weight management before adolescence.

## 9. Inheritance and population

Inheritance is autosomal recessive. For two confirmed heterozygous parents, each pregnancy has a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of inheriting neither familial allele, assuming conventional Mendelian segregation. The observed 44% consanguinity is consistent with enrichment of homozygous rare alleles. (cali2023biallelicprmt7pathogenic pages 2-5)

The cohort’s 23:28 male:female distribution does not suggest a major sex bias. Patients were recruited internationally, including Europe, North America, the Middle East, and Iran; this reflects ascertainment rather than measured geographic prevalence. No population-based prevalence, incidence, carrier frequency, penetrance estimate, founder effect, ethnic-risk estimate, or geographic variant-frequency map is available. The observation of 51 recognized individuals must not be interpreted as worldwide prevalence. (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 7-8)

Expressivity is variable, particularly for ID severity, seizures, obesity, microcephaly, and MRI findings. Anticipation is not expected and has not been reported. Germline mosaicism remains theoretically possible for most Mendelian disorders but has no quantified disease-specific rate.

## 10. Diagnostics

### Clinical evaluation

Clinical suspicion should arise from developmental delay/ID plus hypotonia, short stature, brachydactyly or shortened metacarpals/metatarsals, characteristic facial morphology, seizures, and later-onset obesity. Recommended baseline characterization is phenotype-driven rather than based on formal diagnostic criteria:

1. Detailed developmental, neurologic, growth, and three-generation family history.
2. Physical and dysmorphology assessment, including hands and feet.
3. Height, weight/BMI, head circumference, and longitudinal growth trajectory.
4. Hand/foot or bone-age radiography when clinically indicated; consider bone-density assessment where low density or fractures are suspected.
5. EEG for suspected seizures and MRI according to neurologic indications; neither EEG nor MRI is disease-specific.
6. Hearing and ophthalmologic assessment because hearing impairment and strabismus recur.

No diagnostic enzyme assay, blood metabolite, protein biomarker, histopathology pattern, ECG, EMG, or liquid-biopsy test is validated. Routine endocrine or metabolic testing is useful to exclude alternative causes of growth failure or obesity, not to confirm SBIDDS.

### Molecular confirmation

The preferred test is a neurodevelopmental-disorder, epilepsy, syndromic-short-stature, skeletal-dysplasia, or syndromic-obesity panel containing **PRMT7**, or trio whole-exome/whole-genome sequencing. Candidate variants should be confirmed and phased/segregated, conventionally by Sanger sequencing; this was used in the major cohort. WGS may improve detection of noncoding, copy-number, or structural variants, while exome sequencing has already demonstrated substantial utility. (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 1-2)

Single-gene sequencing is reasonable when the phenotype is highly characteristic and should include deletion/duplication analysis. CMA may detect large deletions but will miss most sequence variants. Karyotyping and FISH are low-yield unless another cytogenetic disorder is suspected. Mitochondrial, repeat-expansion, and somatic testing are not routine. RNA sequencing may help resolve a suspected splice variant but is not a validated first-line assay.

### Differential diagnosis

Important alternatives include Börjeson–Forssman–Lehmann syndrome, CHOPS syndrome, Chung–Jansen syndrome, Cohen syndrome, TRAPPC9-related intellectual disability/obesity, pseudohypoparathyroidism/Albright hereditary osteodystrophy-like conditions, and other syndromic obesity or brachydactyly-ID disorders. Molecular testing is important because the phenotypic overlap is substantial. (halabelian2021structureandfunction pages 8-9, cali2023biallelicprmt7pathogenic pages 5-6)

No population or newborn screening program exists. Cascade testing of adult relatives and targeted testing of at-risk siblings are appropriate after familial variants are established.

## 11. Outcome and prognosis

No survival curve, five- or ten-year survival rate, disease-specific mortality rate, or life-expectancy estimate is available. The oldest person in the 2023 cohort was 55 years old, demonstrating survival into later adulthood but not proving normal life expectancy. (cali2023biallelicprmt7pathogenic pages 2-5)

Morbidity is chiefly neurodevelopmental and functional: persistent cognitive impairment, hypotonia, seizures, sensory problems, skeletal/growth abnormalities, and obesity. Most reported seizures were medication-responsive, while roughly 16% were intractable. The broad ID-severity distribution and heterogeneous MRI findings demonstrate variable expressivity. (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 1-2)

No validated prognostic biomarker exists. Likely clinical prognostic factors—ID severity, seizure control, mobility, swallowing/nutritional status, obesity, and bone health—are reasonable for care planning but have not been validated in longitudinal models. Recovery of the underlying syndrome is not expected; functional improvement through seizure control, therapy, communication support, education, and management of secondary complications is plausible but unquantified.

## 12. Treatment and current implementation

There is no approved PRMT7-restoring or disease-modifying therapy and no disease-specific treatment algorithm supported by trials. Current real-world implementation consists of molecular diagnosis, genetic counseling, developmental services, and organ-directed surveillance. The major cohort reported that most seizures responded to agents including **topiramate** or **sodium valproate**, although treatment must follow seizure type, age, sex/reproductive considerations, comorbidity, and local epilepsy guidance. (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 1-2)

A practical multidisciplinary strategy includes:

* standard antiseizure therapy and rescue planning;
* early physical, occupational, speech/language, feeding, and behavioral therapies;
* individualized education and augmentative communication where needed;
* periodic hearing and ophthalmologic evaluation;
* growth, nutrition, BMI, and metabolic-risk surveillance;
* bone-health assessment, adequate calcium/vitamin D according to general guidelines, and orthopedic/endocrine referral when indicated;
* mobility, endurance, and fall-risk support;
* psychosocial and caregiver support.

Suggested NCIT intervention labels include **Anticonvulsant Therapy**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Nutritional Counseling**, and **Genetic Counseling**. No PRMT7-directed gene therapy, CRISPR treatment, RNA therapy, cell therapy, immunotherapy, or validated targeted small molecule has entered disease-specific clinical practice. PRMT7 inhibitors studied in cancer would be mechanistically inappropriate as replacement therapy for a loss-of-function syndrome and could theoretically worsen deficient activity.

The ClinicalTrials.gov-oriented search found no relevant SBIDDS/PRMT7 interventional study; an obesity exercise trial returned by broad text matching was not disease-specific and should not be linked to this syndrome. Treatment-response rates beyond seizure-control observations and systematic adverse-event data are unavailable.

## 13. Prevention

Primary prevention through vaccination, lifestyle, exposure reduction, or medication is not applicable to occurrence of this inherited disorder. Reproductive prevention options after identifying familial pathogenic variants include genetic counseling, carrier testing of relatives, prenatal diagnosis, and preimplantation genetic testing for monogenic disease. Testing decisions require informed consent and local ethical/legal practice.

Secondary prevention consists of early molecular diagnosis and anticipatory surveillance—not population screening. Tertiary prevention aims to reduce complications through seizure control, developmental therapies, hearing/vision care, mobility and bone support, and early obesity management. Routine immunization remains appropriate but does not specifically prevent SBIDDS. No prophylactic medication is disease-specific.

## 14. Other species and natural disease

No naturally occurring PRMT7-related SBIDDS analogue in a companion-animal breed or wildlife population was identified. Accordingly, there is no evidence of veterinary transmission, zoonotic potential, or cross-species contagion. Orthologous PRMT7 genes are evolutionarily conserved in common experimental species, including mouse and zebrafish, permitting comparative functional studies. Precise NCBI Taxonomy/Gene and VBO identifiers should be obtained directly from the relevant databases during structured curation.

## 15. Model organisms

### Mouse

Whole-body Prmt7 knockout is the principal disease-relevant model. Reported phenotypes include subviability in some strain backgrounds, reduced body size, shortened fifth metatarsals, lower bone mineral content, impaired muscle regeneration, satellite-cell depletion, reduced oxidative metabolism, altered muscle-fiber composition, and age-related obesity. It recapitulates growth, digital/skeletal, muscle, and obesity features, but does not fully model the spectrum or frequencies of human ID, seizures, facial gestalt, and sensory findings. (halabelian2021structureandfunction pages 8-9)

Conditional mouse models dissect tissue-specific biology. Neuronal experiments support altered NALCN-dependent excitability. Prrx1-Cre and Sp7-Cre skeletal-lineage knockout models support defective osteogenesis, but the 2024 female-specific phenotype remains preprint evidence. Cardiomyocyte- and lung-myofibroblast-focused models show broader PRMT7 physiology but do not establish cardiac or pulmonary SBIDDS manifestations. (halabelian2021structureandfunction pages 8-9, zhang2024prmt7mediatedpten pages 4-7)

### Cellular and in-vitro models

C2C12 muscle cells, primary myofibroblasts, mouse and human bone-marrow mesenchymal cells, neuronal preparations, and other engineered cell systems have been used to study chromatin marks, senescence, myogenesis, stress responses, osteogenesis, and substrate methylation. PRMT7 knockdown in muscle cells alters Dnmt3b/Cdkn1a regulation and promotes premature senescence; HSP70 methylation supports stress-associated substrate refolding. These models are useful for pathway dissection and therapeutic screening but do not reproduce whole-patient development. (halabelian2021structureandfunction pages 8-9, zhang2024prmt7mediatedpten pages 4-7, halabelian2021structureandfunction pages 5-6)

### Zebrafish and other systems

Zebrafish studies support conserved roles in antiviral/RIG-I-associated biology, but this is peripheral to the defining human phenotype. No robust SBIDDS patient-derived iPSC, cerebral organoid, growth-plate organoid, or humanized knock-in platform was identified. Appropriate model resources include MGI, IMPC, KOMP, IMSR/MMRRC, ZFIN, and Cellosaurus, with model identity and allele details verified at retrieval.

## Evidence gaps and research priorities

1. A prospective international registry with standardized HPO phenotyping and longitudinal growth, seizure, obesity, bone-density, developmental, and quality-of-life outcomes.
2. Variant-level functional assessment, particularly for missense and splice VUS, with ClinVar deposition and population frequencies.
3. Patient-derived neuronal, myogenic, adipogenic, and osteogenic models to connect PRMT7 substrates to human phenotypes.
4. Patient transcriptomic/proteomic/methyl-proteomic biomarkers and studies of genotype–phenotype correlation.
5. Formal natural-history endpoints suitable for future therapeutic trials.
6. Validation of the 2024 PTEN/osteogenesis mechanism in peer-reviewed work and human tissue, including whether its reported sex effect is biologically relevant to patients. (zhang2024prmt7mediatedpten pages 4-7, cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 6-7)

## Key references

* **Cali E, et al.** “Biallelic PRMT7 pathogenic variants are associated with a recognizable syndromic neurodevelopmental disorder with short stature, obesity, and craniofacial and digital abnormalities.” *Genetics in Medicine*. Published January 2023;25:135–142. DOI: [10.1016/j.gim.2022.09.016](https://doi.org/10.1016/j.gim.2022.09.016). This is the definitive 51-person human cohort. A PMID was not exposed in the retrieved record and is therefore not guessed. (cali2023biallelicprmt7pathogenic pages 2-5, cali2023biallelicprmt7pathogenic pages 1-2)
* **Halabelian L, Barsyte-Lovejoy D.** “Structure and Function of Protein Arginine Methyltransferase PRMT7.” *Life*. Published July 2021;11:768. DOI: [10.3390/life11080768](https://doi.org/10.3390/life11080768). Review integrating enzyme structure, substrates, and model phenotypes. (halabelian2021structureandfunction pages 8-9, halabelian2021structureandfunction pages 12-13)
* **Zhang Y, et al.** “PRMT7 mediated PTEN activation promotes bone formation in female mice.” bioRxiv preprint, posted July 2024. DOI: [10.1101/2024.07.31.605998](https://doi.org/10.1101/2024.07.31.605998). This is recent but not equivalent to peer-reviewed human evidence. (zhang2024prmt7mediatedpten pages 4-7)

**Evidence limitation:** Exact abstract quotations were only available indirectly in the retrieved records. To avoid fabricating quotation marks or PMIDs, this report quotes only the verified 2023 title phrase and otherwise paraphrases the evidence. Individual HGVS variants, database-specific ClinVar accessions, allele frequencies, and uncertain ontology IDs require direct database/supplemental-table verification before knowledge-base ingestion.

References

1. (cali2023biallelicprmt7pathogenic pages 2-5): Elisa Cali, Mohnish Suri, Marcello Scala, Matteo P. Ferla, Shahryar Alavi, Eissa Ali Faqeih, Emilia K. Bijlsma, Kristen M. Wigby, Diana Baralle, Mohammad Y.V. Mehrjardi, Jennifer Schwab, Konrad Platzer, Katharina Steindl, Mais Hashem, Marilyn Jones, Dmitriy M. Niyazov, Jennifer Jacober, Rebecca Okashah Littlejohn, Denisa Weis, Neda Zadeh, Lance Rodan, Alice Goldenberg, François Lecoquierre, Marina Dutra-Clarke, Gabriella Horvath, Dana Young, Naama Orenstein, Shahad Bawazeer, Anneke T. Vulto-van Silfhout, Yvan Herenger, Mohammadreza Dehghani, Seyed Mohammad Seyedhassani, Amir Bahreini, Mahya E. Nasab, A. Gulhan Ercan-Sencicek, Zahra Firoozfar, Mojtaba Movahedinia, Stephanie Efthymiou, Pasquale Striano, Ehsan Ghayoor Karimiani, Vincenzo Salpietro, Jenny C. Taylor, Melody Redman, Alexander P.A. Stegmann, Andreas Laner, Ghada Abdel-Salam, Megan Li, Mario Bengala, Amelie Johanna Müller, Maria C. Digilio, Anita Rauch, Murat Gunel, Hannah Titheradge, Daniela N. Schweitzer, Alison Kraus, Irene Valenzuela, Scott D. McLean, Chanika Phornphutkul, Mustafa Salih, Amber Begtrup, Rhonda E. Schnur, Erin Torti, Tobias B. Haack, Carlos E. Prada, Fowzan S. Alkuraya, Henry Houlden, and Reza Maroofian. Biallelic prmt7 pathogenic variants are associated with a recognizable syndromic neurodevelopmental disorder with short stature, obesity, and craniofacial and digital abnormalities. Genetics in Medicine, 25:135-142, Jan 2023. URL: https://doi.org/10.1016/j.gim.2022.09.016, doi:10.1016/j.gim.2022.09.016. This article has 13 citations and is from a highest quality peer-reviewed journal.

2. (cali2023biallelicprmt7pathogenic pages 1-2): Elisa Cali, Mohnish Suri, Marcello Scala, Matteo P. Ferla, Shahryar Alavi, Eissa Ali Faqeih, Emilia K. Bijlsma, Kristen M. Wigby, Diana Baralle, Mohammad Y.V. Mehrjardi, Jennifer Schwab, Konrad Platzer, Katharina Steindl, Mais Hashem, Marilyn Jones, Dmitriy M. Niyazov, Jennifer Jacober, Rebecca Okashah Littlejohn, Denisa Weis, Neda Zadeh, Lance Rodan, Alice Goldenberg, François Lecoquierre, Marina Dutra-Clarke, Gabriella Horvath, Dana Young, Naama Orenstein, Shahad Bawazeer, Anneke T. Vulto-van Silfhout, Yvan Herenger, Mohammadreza Dehghani, Seyed Mohammad Seyedhassani, Amir Bahreini, Mahya E. Nasab, A. Gulhan Ercan-Sencicek, Zahra Firoozfar, Mojtaba Movahedinia, Stephanie Efthymiou, Pasquale Striano, Ehsan Ghayoor Karimiani, Vincenzo Salpietro, Jenny C. Taylor, Melody Redman, Alexander P.A. Stegmann, Andreas Laner, Ghada Abdel-Salam, Megan Li, Mario Bengala, Amelie Johanna Müller, Maria C. Digilio, Anita Rauch, Murat Gunel, Hannah Titheradge, Daniela N. Schweitzer, Alison Kraus, Irene Valenzuela, Scott D. McLean, Chanika Phornphutkul, Mustafa Salih, Amber Begtrup, Rhonda E. Schnur, Erin Torti, Tobias B. Haack, Carlos E. Prada, Fowzan S. Alkuraya, Henry Houlden, and Reza Maroofian. Biallelic prmt7 pathogenic variants are associated with a recognizable syndromic neurodevelopmental disorder with short stature, obesity, and craniofacial and digital abnormalities. Genetics in Medicine, 25:135-142, Jan 2023. URL: https://doi.org/10.1016/j.gim.2022.09.016, doi:10.1016/j.gim.2022.09.016. This article has 13 citations and is from a highest quality peer-reviewed journal.

3. (halabelian2021structureandfunction pages 8-9): Levon Halabelian and Dalia Barsyte-Lovejoy. Structure and function of protein arginine methyltransferase prmt7. Life, 11:768, Jul 2021. URL: https://doi.org/10.3390/life11080768, doi:10.3390/life11080768. This article has 31 citations.

4. (cali2023biallelicprmt7pathogenic pages 5-6): Elisa Cali, Mohnish Suri, Marcello Scala, Matteo P. Ferla, Shahryar Alavi, Eissa Ali Faqeih, Emilia K. Bijlsma, Kristen M. Wigby, Diana Baralle, Mohammad Y.V. Mehrjardi, Jennifer Schwab, Konrad Platzer, Katharina Steindl, Mais Hashem, Marilyn Jones, Dmitriy M. Niyazov, Jennifer Jacober, Rebecca Okashah Littlejohn, Denisa Weis, Neda Zadeh, Lance Rodan, Alice Goldenberg, François Lecoquierre, Marina Dutra-Clarke, Gabriella Horvath, Dana Young, Naama Orenstein, Shahad Bawazeer, Anneke T. Vulto-van Silfhout, Yvan Herenger, Mohammadreza Dehghani, Seyed Mohammad Seyedhassani, Amir Bahreini, Mahya E. Nasab, A. Gulhan Ercan-Sencicek, Zahra Firoozfar, Mojtaba Movahedinia, Stephanie Efthymiou, Pasquale Striano, Ehsan Ghayoor Karimiani, Vincenzo Salpietro, Jenny C. Taylor, Melody Redman, Alexander P.A. Stegmann, Andreas Laner, Ghada Abdel-Salam, Megan Li, Mario Bengala, Amelie Johanna Müller, Maria C. Digilio, Anita Rauch, Murat Gunel, Hannah Titheradge, Daniela N. Schweitzer, Alison Kraus, Irene Valenzuela, Scott D. McLean, Chanika Phornphutkul, Mustafa Salih, Amber Begtrup, Rhonda E. Schnur, Erin Torti, Tobias B. Haack, Carlos E. Prada, Fowzan S. Alkuraya, Henry Houlden, and Reza Maroofian. Biallelic prmt7 pathogenic variants are associated with a recognizable syndromic neurodevelopmental disorder with short stature, obesity, and craniofacial and digital abnormalities. Genetics in Medicine, 25:135-142, Jan 2023. URL: https://doi.org/10.1016/j.gim.2022.09.016, doi:10.1016/j.gim.2022.09.016. This article has 13 citations and is from a highest quality peer-reviewed journal.

5. (halabelian2021structureandfunction pages 6-8): Levon Halabelian and Dalia Barsyte-Lovejoy. Structure and function of protein arginine methyltransferase prmt7. Life, 11:768, Jul 2021. URL: https://doi.org/10.3390/life11080768, doi:10.3390/life11080768. This article has 31 citations.

6. (halabelian2021structureandfunction pages 5-6): Levon Halabelian and Dalia Barsyte-Lovejoy. Structure and function of protein arginine methyltransferase prmt7. Life, 11:768, Jul 2021. URL: https://doi.org/10.3390/life11080768, doi:10.3390/life11080768. This article has 31 citations.

7. (cali2023biallelicprmt7pathogenic pages 8-8): Elisa Cali, Mohnish Suri, Marcello Scala, Matteo P. Ferla, Shahryar Alavi, Eissa Ali Faqeih, Emilia K. Bijlsma, Kristen M. Wigby, Diana Baralle, Mohammad Y.V. Mehrjardi, Jennifer Schwab, Konrad Platzer, Katharina Steindl, Mais Hashem, Marilyn Jones, Dmitriy M. Niyazov, Jennifer Jacober, Rebecca Okashah Littlejohn, Denisa Weis, Neda Zadeh, Lance Rodan, Alice Goldenberg, François Lecoquierre, Marina Dutra-Clarke, Gabriella Horvath, Dana Young, Naama Orenstein, Shahad Bawazeer, Anneke T. Vulto-van Silfhout, Yvan Herenger, Mohammadreza Dehghani, Seyed Mohammad Seyedhassani, Amir Bahreini, Mahya E. Nasab, A. Gulhan Ercan-Sencicek, Zahra Firoozfar, Mojtaba Movahedinia, Stephanie Efthymiou, Pasquale Striano, Ehsan Ghayoor Karimiani, Vincenzo Salpietro, Jenny C. Taylor, Melody Redman, Alexander P.A. Stegmann, Andreas Laner, Ghada Abdel-Salam, Megan Li, Mario Bengala, Amelie Johanna Müller, Maria C. Digilio, Anita Rauch, Murat Gunel, Hannah Titheradge, Daniela N. Schweitzer, Alison Kraus, Irene Valenzuela, Scott D. McLean, Chanika Phornphutkul, Mustafa Salih, Amber Begtrup, Rhonda E. Schnur, Erin Torti, Tobias B. Haack, Carlos E. Prada, Fowzan S. Alkuraya, Henry Houlden, and Reza Maroofian. Biallelic prmt7 pathogenic variants are associated with a recognizable syndromic neurodevelopmental disorder with short stature, obesity, and craniofacial and digital abnormalities. Genetics in Medicine, 25:135-142, Jan 2023. URL: https://doi.org/10.1016/j.gim.2022.09.016, doi:10.1016/j.gim.2022.09.016. This article has 13 citations and is from a highest quality peer-reviewed journal.

8. (zhang2024prmt7mediatedpten pages 4-7): Yingfei Zhang, Jia Qing, Yang Li, Xin Gao, Dazhuang Lu, Yiyang Wang, Lanxin Gu, Hui Zhang, Zechuan Li, Xu Wang, Yongsheng Zhou, and Ping Zhang. Prmt7 mediated pten activation promotes bone formation in female mice. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.31.605998, doi:10.1101/2024.07.31.605998. This article has 0 citations.

9. (cali2023biallelicprmt7pathogenic pages 6-7): Elisa Cali, Mohnish Suri, Marcello Scala, Matteo P. Ferla, Shahryar Alavi, Eissa Ali Faqeih, Emilia K. Bijlsma, Kristen M. Wigby, Diana Baralle, Mohammad Y.V. Mehrjardi, Jennifer Schwab, Konrad Platzer, Katharina Steindl, Mais Hashem, Marilyn Jones, Dmitriy M. Niyazov, Jennifer Jacober, Rebecca Okashah Littlejohn, Denisa Weis, Neda Zadeh, Lance Rodan, Alice Goldenberg, François Lecoquierre, Marina Dutra-Clarke, Gabriella Horvath, Dana Young, Naama Orenstein, Shahad Bawazeer, Anneke T. Vulto-van Silfhout, Yvan Herenger, Mohammadreza Dehghani, Seyed Mohammad Seyedhassani, Amir Bahreini, Mahya E. Nasab, A. Gulhan Ercan-Sencicek, Zahra Firoozfar, Mojtaba Movahedinia, Stephanie Efthymiou, Pasquale Striano, Ehsan Ghayoor Karimiani, Vincenzo Salpietro, Jenny C. Taylor, Melody Redman, Alexander P.A. Stegmann, Andreas Laner, Ghada Abdel-Salam, Megan Li, Mario Bengala, Amelie Johanna Müller, Maria C. Digilio, Anita Rauch, Murat Gunel, Hannah Titheradge, Daniela N. Schweitzer, Alison Kraus, Irene Valenzuela, Scott D. McLean, Chanika Phornphutkul, Mustafa Salih, Amber Begtrup, Rhonda E. Schnur, Erin Torti, Tobias B. Haack, Carlos E. Prada, Fowzan S. Alkuraya, Henry Houlden, and Reza Maroofian. Biallelic prmt7 pathogenic variants are associated with a recognizable syndromic neurodevelopmental disorder with short stature, obesity, and craniofacial and digital abnormalities. Genetics in Medicine, 25:135-142, Jan 2023. URL: https://doi.org/10.1016/j.gim.2022.09.016, doi:10.1016/j.gim.2022.09.016. This article has 13 citations and is from a highest quality peer-reviewed journal.

10. (halabelian2021structureandfunction pages 12-13): Levon Halabelian and Dalia Barsyte-Lovejoy. Structure and function of protein arginine methyltransferase prmt7. Life, 11:768, Jul 2021. URL: https://doi.org/10.3390/life11080768, doi:10.3390/life11080768. This article has 31 citations.

11. (cali2023biallelicprmt7pathogenic pages 7-8): Elisa Cali, Mohnish Suri, Marcello Scala, Matteo P. Ferla, Shahryar Alavi, Eissa Ali Faqeih, Emilia K. Bijlsma, Kristen M. Wigby, Diana Baralle, Mohammad Y.V. Mehrjardi, Jennifer Schwab, Konrad Platzer, Katharina Steindl, Mais Hashem, Marilyn Jones, Dmitriy M. Niyazov, Jennifer Jacober, Rebecca Okashah Littlejohn, Denisa Weis, Neda Zadeh, Lance Rodan, Alice Goldenberg, François Lecoquierre, Marina Dutra-Clarke, Gabriella Horvath, Dana Young, Naama Orenstein, Shahad Bawazeer, Anneke T. Vulto-van Silfhout, Yvan Herenger, Mohammadreza Dehghani, Seyed Mohammad Seyedhassani, Amir Bahreini, Mahya E. Nasab, A. Gulhan Ercan-Sencicek, Zahra Firoozfar, Mojtaba Movahedinia, Stephanie Efthymiou, Pasquale Striano, Ehsan Ghayoor Karimiani, Vincenzo Salpietro, Jenny C. Taylor, Melody Redman, Alexander P.A. Stegmann, Andreas Laner, Ghada Abdel-Salam, Megan Li, Mario Bengala, Amelie Johanna Müller, Maria C. Digilio, Anita Rauch, Murat Gunel, Hannah Titheradge, Daniela N. Schweitzer, Alison Kraus, Irene Valenzuela, Scott D. McLean, Chanika Phornphutkul, Mustafa Salih, Amber Begtrup, Rhonda E. Schnur, Erin Torti, Tobias B. Haack, Carlos E. Prada, Fowzan S. Alkuraya, Henry Houlden, and Reza Maroofian. Biallelic prmt7 pathogenic variants are associated with a recognizable syndromic neurodevelopmental disorder with short stature, obesity, and craniofacial and digital abnormalities. Genetics in Medicine, 25:135-142, Jan 2023. URL: https://doi.org/10.1016/j.gim.2022.09.016, doi:10.1016/j.gim.2022.09.016. This article has 13 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](PRMT7-Related_Short_Stature-Brachydactyly_Syndrome-deep-research-falcon_artifacts/artifact-00.md)