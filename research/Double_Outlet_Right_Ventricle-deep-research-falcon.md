---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T16:57:07.911074'
end_time: '2026-07-31T17:04:21.767465'
duration_seconds: 433.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Double Outlet Right Ventricle
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Double_Outlet_Right_Ventricle-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Double Outlet Right Ventricle
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Double Outlet Right Ventricle** covering all of the
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
- **Disease Name:** Double Outlet Right Ventricle
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Double Outlet Right Ventricle** covering all of the
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


# Double Outlet Right Ventricle: Comprehensive Disease-Characteristics Report

## Executive summary

Double outlet right ventricle (DORV) is a **congenital ventriculoarterial connection phenotype** in which both great arterial roots arise predominantly from the morphologic right ventricle. It is not one uniform disease: physiology, clinical presentation, operation, and prognosis depend principally on the ventricular septal defect (VSD), its relationship to the arterial roots, great-artery orientation, outflow obstruction, ventricular adequacy, and associated cardiac or extracardiac abnormalities. A 2024 review estimates that DORV constitutes **1–3% of congenital heart disease (CHD)** and occurs in approximately **3–9 per 100,000 live births**. (moscatelli2024importanceofcardiovascular pages 8-10)

The strongest current model is multifactorial developmental causation. Human and experimental evidence implicates chromosomal abnormalities, rare sequence variants, cilia/left–right patterning, second-heart-field and cardiac-neural-crest development, noncanonical Wnt/planar-cell-polarity signaling, actomyosin organization, and tightly regulated retinoic-acid signaling. No single gene accounts for most cases. Treatment is individualized anatomical reconstruction—usually biventricular repair when feasible—or staged single-ventricle palliation when two-ventricle circulation cannot be constructed safely.

The following evidence table distinguishes DORV-specific findings from broader CHD evidence used to inform testing or management.

| Domain | Knowledge-base fact | Quantitative data | Evidence type/year | Ontology suggestions |
|---|---|---|---|---|
| Definition & anatomic determinants **(DORV-specific)** | DORV is defined by both great arteries arising primarily from the morphologic right ventricle; practical classification depends on **VSD location**, **great-artery relationship**, and **presence/level of outflow tract obstruction**, all of which drive surgical strategy and imaging needs. (moscatelli2024importanceofcardiovascular pages 8-10) | Represents **1–3% of all CHD**; incidence **3–9 per 100,000 live births**. (moscatelli2024importanceofcardiovascular pages 8-10) | Narrative review of pediatric CMR / 2024 (moscatelli2024importanceofcardiovascular pages 8-10) | MeSH: Double Outlet Right Ventricle; UBERON: right ventricle, ventricular septum, outflow tract; HPO: Ventricular septal defect, Abnormality of the outflow tract |
| Incidence / population burden **(DORV-specific + general CHD context)** | Available retrieved evidence supports DORV as a rare complex CHD within the conotruncal/outflow-tract spectrum. General CHD prevalence context should not be substituted for DORV prevalence. (moscatelli2024importanceofcardiovascular pages 8-10, shorbaji2024currentgeneticmodels pages 1-2) | DORV: **3–9/100,000 live births**; general CHD prevalence in review literature: **9.41 per 1000 live births** globally (not DORV-specific). (moscatelli2024importanceofcardiovascular pages 8-10, shorbaji2024currentgeneticmodels pages 1-2) | DORV imaging review / 2024; CHD models review / 2024 (moscatelli2024importanceofcardiovascular pages 8-10, shorbaji2024currentgeneticmodels pages 1-2) | MONDO: congenital heart disease / DORV if mapped; MeSH: Heart Defects, Congenital |
| Imaging & preoperative assessment **(DORV-specific)** | Transthoracic echocardiography is first-line for defining anatomy; **preoperative CMR** is valuable for detailed visualization of the VSD and spatial relationships relevant to repair planning; **postoperative CMR** helps evaluate late complications. (moscatelli2024importanceofcardiovascular pages 8-10) | No sensitivity/specificity reported in retrieved DORV-specific source; 4D flow noted as useful for estimating RVOT diameters and flow characterization. (moscatelli2024importanceofcardiovascular pages 8-10) | Narrative review / 2024 (moscatelli2024importanceofcardiovascular pages 8-10) | NCIT: Magnetic Resonance Imaging; LOINC/RadLex terms for echocardiography/CMR; UBERON: right ventricular outflow tract |
| Real-world implementation: virtual surgical planning **(DORV-specific)** | A prospective observational study used standard-of-care **MRI, 3D echo, and CT** to reconstruct patient-specific anatomy and perform **virtual surgery** for complex lesions including DORV, aiming to compare planned vs implemented repairs. (NCT00972608 chunk 1) | Trial enrollment **66**; age up to **22 years**; study completed. (NCT00972608 chunk 1) | ClinicalTrials.gov observational study / first posted 2009, last updated 2022 (NCT00972608 chunk 1) | NCIT: Surgical Planning; NCIT: Three Dimensional Imaging; MeSH: Computer Simulation |
| Genetic testing yield **(general CHD evidence; relevant to DORV workup, not DORV-specific)** | Genetic etiologies are common enough in complex CHD that chromosomal and sequencing-based testing is clinically relevant; CMA is used as a nontargeted first-line approach when a specific syndrome is not suspected. (findley2022congenitalheartdefects pages 1-2, yasuhara2021geneticsofcongenital pages 9-10) | Genetic etiology identifiable in **20–30%** of CHD; postnatal CMA yield **4–28%** in prior CHD studies; in one neonatal cohort, pathogenic CNV in **21.3% (61/287)** by CMA and aneuploidy in additional **11% (58/525)** overall; conotruncal defects had **27.2%** CMA yield. (findley2022congenitalheartdefects pages 1-2) | Retrospective neonatal cohort / 2022; CHD genetics review / 2021 (findley2022congenitalheartdefects pages 1-2, yasuhara2021geneticsofcongenital pages 9-10) | NCIT: Chromosomal Microarray Analysis; NCIT: Exome Sequencing; SO: copy number variant |
| Variant interpretation workflow **(general CHD evidence; relevant to DORV)** | Exome-based CHD studies prioritize rare variants using population frequency filters and classify them with **ACMG/AMP** frameworks, supported by ClinGen/ClinVar/VarSome/Franklin. (yasuhara2021geneticsofcongenital pages 9-10) | Example family-based diagnostic rates cited in the review: **31%** with targeted NGS panels in CHD families; **33%** in one small familial CHD series. (yasuhara2021geneticsofcongenital pages 9-10) | Narrative review / 2021 (yasuhara2021geneticsofcongenital pages 9-10) | NCIT: Genetic Counseling; SO: missense variant, frameshift variant; ECO: clinical sequencing evidence |
| Mechanism: PCP–SHROOM3 **(DORV-specific mechanistic model evidence)** | In mouse, **SHROOM3** functions downstream of noncanonical **Wnt/planar cell polarity (PCP)** signaling; loss of function disrupts cardiomyocyte polarity, actomyosin organization, proliferation, and morphology, producing a CHD spectrum that includes **DORV**. (durbin2020shroom3isdownstream pages 1-7) | DORV reported as part of a **variable penetrance spectrum** in Shroom3 knockout mice; no percentage given in retrieved text. (durbin2020shroom3isdownstream pages 1-7) | Mouse mechanistic study / 2020 (durbin2020shroom3isdownstream pages 1-7) | GO: planar cell polarity pathway; GO: actomyosin structure organization; CL: cardiomyocyte, cardiac neural crest cell, second heart field cell |
| Mechanism: FOXJ1–motile cilia / left-right patterning **(DORV-specific human + model evidence)** | A truncating **FOXJ1** variant identified by clinical exome sequencing was associated with isolated CHD including **DORV** and TGA; functional data support impaired ciliogenesis/transactivation, and Foxj1 loss-of-function mice show abnormal looping and complex CHD including **DORV**, linking DORV to cilia-dependent **left-right organizer/NODAL-axis** biology. (padua2023congenitalheartdefects pages 1-2) | Single reported proband in retrieved paper; CHD overall affects nearly **11 per 1000 newborns** in the paper’s introduction (general, not DORV-specific). (padua2023congenitalheartdefects pages 1-2) | Human genetics + functional assays + mouse model / 2023 (padua2023congenitalheartdefects pages 1-2) | GO: cilium movement; GO: determination of left/right symmetry; CL: ciliated epithelial cell; HPO: Dextrocardia, Transposition of the great arteries |
| Mechanism: retinoic acid / second heart field **(general developmental pathway relevant to DORV)** | Properly controlled **retinoic acid (RA)** signaling is required for outflow-tract elongation and septation by maintaining/differentiating cardiogenic progenitors in the **second heart field**; defective or excess RA signaling is a recognized route to outflow-tract CHD and is therefore mechanistically relevant to DORV. (nakajima2019retinoicacidsignaling pages 1-2) | No DORV-specific frequency in retrieved source. (nakajima2019retinoicacidsignaling pages 1-2) | Developmental biology review / 2019 (nakajima2019retinoicacidsignaling pages 1-2) | GO: retinoic acid receptor signaling pathway; GO: heart development; CL: second heart field progenitor cell |
| Environmental / teratogenic factors **(general CHD evidence; not DORV-specific)** | Retrieved recent review evidence lists environmental contributors to CHD including **dioxins, pesticides, polychlorinated biphenyls**, and maternal exposure to **alcohol, isotretinoin, thalidomide, antiseizure medications, and antiretrovirals**; these should be treated as CHD-level rather than DORV-proven risks unless lesion-specific data are available. (shorbaji2024currentgeneticmodels pages 1-2) | No DORV-specific effect sizes reported in retrieved evidence. (shorbaji2024currentgeneticmodels pages 1-2) | CHD models/background review / 2024 (shorbaji2024currentgeneticmodels pages 1-2) | CHEBI: retinoic acid, ethanol; MeSH: Teratogens |
| Prenatal diagnosis & care pathways **(general complex CHD / single-ventricle context; partly applicable to selected DORV)** | Prenatal echocardiography and fetal cardiac MRI can delineate complex CHD and support **planned delivery at tertiary centers**, improving survival outcomes; this is particularly relevant for DORV cases with functionally univentricular physiology or severe associated lesions. (corno2023narrativereviewof pages 1-2) | Most heart malformations recognizable at **16–18 weeks**; reported sensitivity **>96%** and specificity **approaching 100%** in cited review text for prenatal recognition generally. (corno2023narrativereviewof pages 1-2) | Narrative review / 2023 (corno2023narrativereviewof pages 1-2) | NCIT: Fetal Echocardiography; NCIT: Magnetic Resonance Imaging; HPO: Prenatal onset |
| Treatment pathways **(DORV-specific)** | DORV treatment is anatomy-driven: imaging must define whether **biventricular repair** is feasible and characterize VSD-arterial alignment/outflow obstruction; postoperative CMR surveillance is used for late structural/functional complications. Retrieved evidence supports surgical planning rather than a single universal operation. (moscatelli2024importanceofcardiovascular pages 8-10, NCT00972608 chunk 1) | No single outcome rate supported in retrieved DORV-specific contexts. (moscatelli2024importanceofcardiovascular pages 8-10, NCT00972608 chunk 1) | CMR review / 2024; observational surgical-planning study / 2022 update (moscatelli2024importanceofcardiovascular pages 8-10, NCT00972608 chunk 1) | NCIT: Cardiac Surgical Procedure; NCIT: Biventricular Repair; NCIT: Fontan Procedure |
| Model organisms & experimental systems **(general CHD, includes DORV-relevant models)** | Current CHD model platforms include **mouse, zebrafish, Xenopus, chick, canine, primate, Drosophila, and iPSCs**; for DORV-relevant mechanisms, mouse and zebrafish are especially useful for outflow-tract, cilia, PCP, and second-heart-field biology, while iPSCs support variant interrogation but have maturation/2D limitations. (shorbaji2024currentgeneticmodels pages 1-2, yasuhara2021geneticsofcongenital pages 9-10) | No DORV-specific model prevalence data. (shorbaji2024currentgeneticmodels pages 1-2, yasuhara2021geneticsofcongenital pages 9-10) | Models review / 2024; genetics review / 2021 (shorbaji2024currentgeneticmodels pages 1-2, yasuhara2021geneticsofcongenital pages 9-10) | NCBI Taxon: Mus musculus, Danio rerio, Xenopus; EFO/NCIT: induced pluripotent stem cell |
| Septal anatomy relevant to repair **(general anatomy with direct DORV relevance)** | In hearts with valvar overriding and DORV-related ventricular septal deficiency, the clinically relevant “defect” is the **curved right-ventricular boundary** around which a surgeon places a patch to tunnel flow to the appropriate outflow, underscoring why septal topology matters for DORV repair planning. (spicer2014ventricularseptaldefect pages 1-2) | No DORV-specific percentages. (spicer2014ventricularseptaldefect pages 1-2) | Anatomic/pathology review / 2014 (spicer2014ventricularseptaldefect pages 1-2) | UBERON: ventricular septum; HPO: Overriding aorta; NCIT: Patch Closure |


*Table: This table summarizes DORV-specific facts and carefully separated general CHD evidence relevant to a disease knowledge-base entry. It highlights anatomic determinants, imaging, genetics, developmental mechanisms, treatment planning, and model systems while avoiding unsupported lesion-specific claims.*

## 1. Disease information

### Definition and classification

DORV is best regarded as a **morphologic descriptor**, not a single physiologic entity. Both great arteries arise primarily from the right ventricle, and the left ventricle ejects through a VSD. Classification should document:

1. VSD relationship: subaortic, subpulmonary, doubly committed/juxtaarterial, or remote/noncommitted.
2. Great-artery relationship and conal anatomy.
3. Pulmonary or systemic outflow obstruction.
4. Ventricular size and atrioventricular-valve anatomy.
5. Coronary anatomy, arch disease, heterotaxy, and other associated lesions.

The clinically relevant VSD is often a curved three-dimensional communication; its borders determine whether a patch or tunnel can direct left-ventricular blood to an arterial root without obstructing inflow, outflow, or conduction tissue. (spicer2014ventricularseptaldefect pages 1-2)

### Identifiers and synonyms

- **MeSH:** Double Outlet Right Ventricle, **D004310**. (NCT00972608 chunk 1)
- **ICD-10-CM:** **Q20.1**, Double outlet right ventricle.
- **ICD-11:** classified among congenital anomalies of ventriculoarterial connections; local coding-browser verification is advised before database ingestion because extension codes vary by release.
- **MONDO:** DORV is represented in MONDO, but the exact release-specific identifier should be verified through the current MONDO API before production use.
- **OMIM:** no single unitary OMIM disorder adequately represents nonsyndromic DORV; OMIM entries are generally gene- or syndrome-specific.
- Common names: **DORV**, double-outlet right ventricle, double outlet of right ventricle. Historical physiologic labels include **Taussig–Bing anomaly** for a subpulmonary-VSD/DORV phenotype.

This report synthesizes **aggregated disease-level resources, cohorts, reviews, clinical-trial records, and primary experimental studies**. It is not derived from one patient’s EHR.

## 2. Etiology, risk, and protective factors

### Causal architecture

DORV results from disturbed embryonic alignment and septation of the ventricular outlets. Etiology is heterogeneous:

- **Chromosomal/CNV:** aneuploidies and pathogenic copy-number variants, including syndromic conotruncal disease, are important.
- **Monogenic/oligogenic:** variants affecting transcription, chromatin, cilia, laterality, second-heart-field, neural-crest, and cytoskeletal pathways can produce DORV.
- **Multifactorial:** many isolated cases remain unexplained and probably reflect combinations of rare/common variants, developmental stochasticity, and maternal/environmental influences.

General CHD evidence—not a DORV-specific yield—suggests a genetic cause in **20–30%** of affected patients. In a 525-neonate CHD cohort, CMA found pathogenic CNVs in **21.3% (61/287)** of those tested; karyotype/FISH identified aneuploidy in another **11% (58/525)** of the overall cohort, and conotruncal lesions had a **27.2% CMA yield**. These figures support genetic evaluation in complex DORV but must not be presented as DORV-specific estimates. (findley2022congenitalheartdefects pages 1-2)

### Environmental and maternal risks

Recent CHD-level literature identifies maternal diabetes, obesity, phenylketonuria, smoking, alcohol, retinoids such as isotretinoin, thalidomide, selected antiseizure drugs, some antiretrovirals, and exposure to pesticides, dioxins, or polychlorinated biphenyls as possible teratogenic risks. Lesion-specific effect sizes for DORV are generally unavailable; causality must not be assigned to an individual exposure solely because DORV occurred. (shorbaji2024currentgeneticmodels pages 1-2)

Retinoic acid is particularly biologically plausible: it is both a morphogen and teratogen, and excessive or deficient signaling disturbs cardiac development in dose- and stage-dependent fashion. (nakajima2019retinoicacidsignaling pages 1-2)

### Protective factors and gene–environment interaction

No reproducible **DORV-specific protective allele, diet, supplement, or lifestyle factor** is established. General preconception measures—glycemic control, management of phenylketonuria, folate sufficiency, avoidance of known teratogens, smoking cessation, medication review, and rubella immunization—reduce broader congenital-anomaly risk but do not guarantee prevention of DORV. Retinoid biology illustrates gene–environment interaction: variants in synthesis, degradation, receptor, or downstream developmental pathways could plausibly alter sensitivity to maternal retinoid exposure, although clinically validated DORV-specific interaction estimates are lacking.

## 3. Phenotypes

Presentation ranges from critical neonatal cyanosis to pulmonary overcirculation and heart failure. Frequency is anatomy-dependent, so universal percentages are inappropriate.

- **DORV anatomy:** congenital, invariant structural sign; HPO **Double outlet right ventricle (HP:0001719)**.
- **VSD/interventricular communication:** essentially integral to viable LV egress; HPO **Ventricular septal defect (HP:0001629)**.
- **Cyanosis/hypoxemia:** neonatal or infantile, particularly with pulmonary stenosis/atresia, unfavorable streaming, or parallel circulations; severity variable; HPO **Cyanosis (HP:0000961)**.
- **Tachypnea, feeding difficulty, diaphoresis, failure to thrive:** arise with excessive pulmonary flow or heart failure; usually progressive over weeks without treatment; HPO terms include **Tachypnea (HP:0002789)**, **Feeding difficulties (HP:0011968)**, and **Failure to thrive (HP:0001508)**.
- **Cardiac murmur:** variable and determined by VSD/outflow obstruction; HPO **Cardiac murmur (HP:0030148)**.
- **Pulmonary stenosis/atresia:** produces reduced pulmonary flow and cyanosis; HPO **Pulmonary stenosis (HP:0001642)** or **Pulmonary atresia (HP:0004935)**.
- **Pulmonary hypertension:** downstream of a large unrestricted pulmonary circuit if repair is delayed; HPO **Pulmonary hypertension (HP:0002092)**.
- Associated phenotypes can include TGA-type arterial relationships, atrioventricular-valve abnormalities, ventricular hypoplasia, aortic arch anomalies, dextrocardia, situs abnormalities/heterotaxy, and extracardiac syndromic findings.

Quality of life is shaped less by the label DORV than by repair type, residual obstruction or regurgitation, ventricular function, arrhythmia, exercise capacity, neurodevelopment, repeated procedures, and—after Fontan palliation—multisystem Fontan morbidity. Complex CHD survivors are at increased neurodevelopmental risk through genetic disease, altered fetal oxygen delivery, perioperative injury, repeated hospitalization, and socioeconomic stressors. (findley2022congenitalheartdefects pages 1-2, corno2023narrativereviewof pages 1-2)

## 4. Genetic and molecular information

### Genes and variants

There is no definitive short list of genes that explains most isolated DORV. Reported or mechanistically supported genes include **FOXJ1, SHROOM3, CHD7, TBX1, NKX2-5, GATA4/GATA6, ZFPM2, NOTCH-pathway genes, NODAL-pathway genes**, and numerous ciliary/chromatin genes. Associations range from established syndromic causation to candidate-level evidence; each variant requires gene–disease and ACMG/AMP assessment.

A particularly informative 2023 primary study reported a truncating **FOXJ1 c.784_799dup; p.Glu267Glyfs*12** variant identified by clinical exome sequencing in a patient with atrial and ventricular septal defects, DORV, and TGA. The mutant failed to induce ectopic cilia in frog epidermis or activate an ADGB promoter assay, while Foxj1-loss mice developed randomized looping and complex defects including DORV. The authors concluded: **“These results indicate that pathogenic variants in FOXJ1 can cause isolated CHD.”** This is compelling human-plus-functional evidence but still represents a rare cause, not a common DORV gene. Published 9 May 2023; DOI: https://doi.org/10.1093/hmg/ddad065. (padua2023congenitalheartdefects pages 1-2)

Variant classes reported across DORV-associated disorders include germline missense, nonsense, frameshift, splice, CNV, and aneuploid variants. Population frequency should be checked against ancestry-matched gnomAD data; a credible highly penetrant severe-developmental allele is usually absent or extremely rare. Somatic mutation is not an established general cause of DORV.

### Chromosomal and epigenetic abnormalities

Relevant abnormalities include aneuploidies and pathogenic CNVs such as 22q11.2-region disease in the broader conotruncal differential. Chromatin regulators can cause syndromic CHD, but no DORV-specific methylation signature is clinically validated. Histone regulation is mechanistically relevant to second-heart-field transcription, yet clinical epigenomic testing is not routine.

### Modifiers, penetrance, and inheritance

Inheritance depends on the diagnosis: de novo autosomal-dominant variants are common in severe syndromic CHD; inherited AD, AR, X-linked, and oligogenic mechanisms also occur. Penetrance and expressivity are often incomplete and variable. Anticipation, a general founder effect, and a single carrier frequency are not established for DORV as a phenotype. Recurrence counseling must therefore use the identified syndrome/gene when available; otherwise, empiric CHD-family recurrence estimates are used.

## 5. Environmental information

DORV is not infectious, contagious, occupationally acquired after birth, or lifestyle-induced in the affected infant. Maternal metabolic disease, medication/teratogen exposure, and environmental toxicants are relevant during early embryogenesis. No pathogen is established as a specific cause, although maternal infections such as rubella are recognized general CHD risks. Exposure ascertainment should be prospective where possible because retrospective recall and confounding are major limitations.

## 6. Mechanism and pathophysiology

### Causal developmental chain

1. **Upstream disturbance:** genetic/CNV/teratogenic perturbation affects laterality, cardiac progenitor specification, neural-crest migration, second-heart-field addition, or cytoskeletal polarity.
2. **Morphogenesis:** abnormal heart-tube looping, outflow elongation, conal rotation/alignment, and outlet septation leave both arterial roots supported predominantly by the right ventricle.
3. **Anatomic routing defect:** the LV can reach an arterial root only through the VSD.
4. **Hemodynamic phenotype:** VSD position and resistance/obstruction determine systemic-versus-pulmonary streaming, cyanosis, pulmonary overcirculation, ventricular pressure load, and heart failure.
5. **Downstream injury:** chronic hypoxemia, pulmonary vascular remodeling, ventricular hypertrophy/dysfunction, arrhythmia substrate, and postoperative scar/conduit/valve disease.

### Major pathways and cells

- **Noncanonical Wnt/planar-cell-polarity–actomyosin pathway:** Shroom3 gene-trap mice show variable VSD, DORV, and thin LV myocardium. SHROOM3 is expressed in ventricular cardiomyocytes, cardiac neural crest, and second-heart-field cells and acts downstream of DVL2; loss disrupts actomyosin organization, polarity, proliferation, and morphology. DOI: https://doi.org/10.1016/j.ydbio.2020.05.013. (durbin2020shroom3isdownstream pages 1-7)
- **Motile cilia–NODAL laterality:** FOXJ1-dependent cilia generate leftward organizer flow; disruption randomizes looping and great-artery position. (padua2023congenitalheartdefects pages 1-2)
- **Retinoic-acid signaling:** correctly bounded RA signaling maintains/differentiates second-heart-field progenitors required for outflow elongation and septation. (nakajima2019retinoicacidsignaling pages 1-2)
- **Cardiac neural crest and second heart field:** defective migration, proliferation, or integration impairs conotruncal septation/alignment.

Suggested annotations: GO **heart development**, **cardiac chamber morphogenesis**, **outflow tract morphogenesis**, **determination of left/right symmetry**, **cilium movement**, **planar cell polarity pathway**, **actomyosin structure organization**, and **retinoic-acid receptor signaling**. Suggested cell types are cardiomyocyte, cardiac neural crest cell, second-heart-field cardiac progenitor, endocardial cell, vascular smooth-muscle cell, and ciliated organizer cell. Suitable CL identifiers should be release-validated because some developmental cardiac-cell terms remain ontology-dependent.

No DORV-specific reproducible plasma metabolomic, proteomic, lipidomic, or immune signature is established. Inflammation is downstream of surgery or heart failure rather than a primary mechanism.

## 7. Anatomical structures affected

Primary structures are the morphologic right and left ventricles, ventricular septum, conal/outflow myocardium, aortic and pulmonary roots, semilunar valves, and proximal great arteries. Secondary involvement may include atrioventricular valves, coronary arteries, pulmonary arteries, aortic arch, conduction tissue, lungs/pulmonary vasculature, liver and lymphatics after Fontan circulation, and brain through altered oxygen delivery.

Suggested UBERON annotations: heart, right ventricle, left ventricle, interventricular septum, cardiac outflow tract, ascending aorta, pulmonary trunk, aortic valve, and pulmonary valve. Relevant subcellular compartments include motile cilium/axoneme, nucleus/chromatin, adherens/cytoskeletal structures, actomyosin cortex, and extracellular matrix. DORV itself is not lateralized, but associated situs and dextrocardia can be.

## 8. Temporal development

The lesion forms during early embryonic cardiogenesis and is therefore **congenital and non-remitting**. Structural heart development is substantially established in the first trimester; fetal imaging commonly recognizes major CHD during the second trimester. A 2023 review reported that most malformations are recognizable at **16–18 weeks**, with sensitivity above 96% and specificity approaching 100% in the cited specialist-imaging literature, although these are not DORV-specific population-screening values. (corno2023narrativereviewof pages 1-2)

Clinical onset is variable: critical cyanosis may occur immediately after birth; pulmonary-overcirculation symptoms often emerge as pulmonary vascular resistance falls over days to weeks. Without definitive management, physiology may progress to severe cyanosis, heart failure, growth failure, or irreversible pulmonary vascular disease. After repair, DORV becomes a lifelong repaired CHD requiring surveillance rather than a cured developmental predisposition.

## 9. Inheritance and population

DORV incidence is approximately **3–9/100,000 live births**, representing **1–3% of CHD**. (moscatelli2024importanceofcardiovascular pages 8-10) No consistent sex ratio, ethnic restriction, endemic region, founder variant, or age-dependent prevalence can be assigned confidently from the retrieved DORV-specific evidence. Apparent geographic variation is affected by prenatal detection, pregnancy outcome, registry definitions, access to echocardiography, and surgical referral.

The phenotype is usually sporadic and multifactorial. If a molecular diagnosis is found, inheritance follows that disorder. Germline mosaicism is possible for apparently de novo variants but has not been quantified for DORV overall. Consanguinity becomes relevant when an AR syndrome or laterality disorder is suspected.

## 10. Diagnostics

### Clinical and imaging diagnosis

Fetal echocardiography can identify both arteries arising from the right ventricle, VSD position, great-artery relationship, outflow obstruction, ventricular balance, arch anatomy, rhythm, and extracardiac markers. Postnatally, transthoracic echocardiography is first-line. ECG, pulse oximetry, chest radiography, blood gases, lactate, and routine laboratory studies assess physiology but are not diagnostic biomarkers.

CMR supplies ventricular volumes/function, flow, VSD-to-artery spatial relationships, great-vessel anatomy, and postoperative assessment without ionizing radiation. The 2024 review states that preoperative CMR is valuable for detailed VSD and spatial visualization; 4D flow can characterize RVOT dimensions and flow dynamics. CT is useful when high spatial resolution, airway, coronary, or rapid acquisition is needed. Catheterization is reserved for unresolved anatomy, intervention, coronary/hemodynamic questions, or pulmonary vascular resistance assessment. (moscatelli2024importanceofcardiovascular pages 8-10)

Patient-specific reconstruction is already implemented in research and selected centers. **NCT00972608**, a completed prospective case-only study enrolling 66 patients up to age 22, used MRI, CT, or 3D echocardiography for virtual reconstruction and simulated operations in complex lesions including DORV. ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT00972608. (NCT00972608 chunk 1)

### Genetic-testing strategy

1. Clinical genetics examination and three-generation pedigree.
2. Rapid karyotype/FISH or rapid genomic testing when aneuploidy or 22q11.2 disease is strongly suspected.
3. **CMA** for complex DORV, extracardiac anomalies, developmental differences, or no recognizable syndrome.
4. Trio CHD/laterality panel or **trio exome sequencing** after nondiagnostic CMA; genome sequencing may add noncoding, balanced structural, and complex CNV detection.
5. Mitochondrial or targeted testing only when phenotype indicates it. Repeat-expansion and tumor/somatic testing are not routine.

Variants should be classified under ACMG/AMP criteria using ClinVar/ClinGen and population databases. Exome interpretation remains challenging; functional validation and periodic reanalysis are valuable. (yasuhara2021geneticsofcongenital pages 9-10)

### Differential diagnosis

Distinguish DORV from tetralogy of Fallot, d-TGA with VSD, overriding aorta not meeting DORV criteria, pulmonary atresia/VSD, truncus arteriosus, congenitally corrected TGA, single-ventricle lesions, and complex heterotaxy. The key discriminator is segmental anatomy and the degree of arterial-root commitment to each ventricle, not physiology alone.

## 11. Outcome and prognosis

There is no scientifically defensible single DORV survival rate because morphology and surgical pathway differ profoundly. Favorable factors include two adequate ventricles, a routable VSD, preserved ventricular/atrioventricular-valve function, absence of major extracardiac syndrome, and repair before pulmonary vascular disease. Risk rises with remote VSD, ventricular imbalance, heterotaxy, pulmonary atresia, coronary/arch complexity, genetic syndromes, prematurity, and Fontan dependence.

Long-term complications include residual/recurrent LV or RV outflow obstruction, conduit stenosis/regurgitation, semilunar-valve disease, ventricular dysfunction, arrhythmia, heart block, endocarditis, reoperation, exercise limitation, and neurodevelopmental or psychosocial morbidity. Fontan patients additionally face venous hypertension, liver disease, lymphatic failure, protein-losing enteropathy, thrombosis, and eventual Fontan failure. Lifelong adult-congenital-heart-disease follow-up is essential. CMR is particularly useful for detecting late structural and functional complications. (moscatelli2024importanceofcardiovascular pages 8-10)

## 12. Treatment

### Anatomy-driven strategy

- **Neonatal stabilization:** oxygen only as physiologically appropriate; ventilation, diuretics/inotropes for heart failure; prostaglandin E1 for duct-dependent pulmonary or systemic flow; atrial septostomy when mixing is inadequate in TGA-like physiology.
- **Subaortic VSD without pulmonary stenosis:** intraventricular tunnel from LV through VSD to aorta, with closure/rerouting tailored to anatomy.
- **Subpulmonary VSD/Taussig–Bing physiology:** commonly arterial switch plus VSD-to-pulmonary-root routing, with arch repair when required.
- **DORV with pulmonary stenosis/atresia:** Rastelli-type LV-to-aorta tunnel with RV–PA conduit, REV, Nikaidoh/root-translocation strategies, or other individualized reconstruction.
- **Remote/noncommitted VSD:** complex tunnel, VSD enlargement, root translocation, staged ventricular recruitment, or single-ventricle palliation depending on obstruction and ventricular geometry.
- **Unbalanced ventricles/unsafe biventricular route:** staged palliation—systemic/pulmonary flow control, bidirectional Glenn, then Fontan completion.

No drug corrects DORV anatomy, and there is no approved DORV-specific gene, RNA, cell, targeted, or immunotherapy. Pharmacotherapy is supportive. Rehabilitation includes nutrition, developmental surveillance, physical activity counseling, school support, and cardiac rehabilitation where indicated. Suggested NCIT intervention concepts include cardiac surgical procedure, ventricular septal-defect repair, arterial switch operation, Rastelli procedure, cavopulmonary shunt, Fontan procedure, cardiac catheterization, prostaglandin E1 therapy, diuretic therapy, and cardiac transplantation.

Recent innovation focuses on CMR/CT-based 3D reconstruction, virtual reality, 3D printing, computational flow, and individualized tunnel design rather than a new disease-modifying drug. (moscatelli2024importanceofcardiovascular pages 8-10, NCT00972608 chunk 1)

## 13. Prevention

**Primary prevention:** most DORV cannot presently be prevented. Preconception genetic counseling, control of diabetes/phenylketonuria, avoidance of isotretinoin and other established teratogens, medication review, smoking/alcohol avoidance, folate sufficiency, and recommended vaccination are prudent general measures.

**Secondary prevention:** prenatal anomaly screening and fetal echocardiography do not prevent formation but enable genetic testing, counseling, delivery planning, and immediate neonatal care. Prenatal recognition of complex CHD supports coordinated delivery at a tertiary cardiac center. (corno2023narrativereviewof pages 1-2)

**Tertiary prevention:** timely repair before pulmonary vascular disease, endocarditis prevention according to current high-risk guidelines, immunization, dental hygiene, thrombosis management where indicated, home monitoring after staged palliation, neurodevelopmental screening, and lifelong imaging reduce complications. Cascade testing is appropriate only when a familial pathogenic variant or chromosome disorder is identified. Preimplantation or prenatal diagnosis can then be offered, recognizing variable expressivity.

## 14. Other species and natural disease

DORV-like congenital malformations can occur sporadically in veterinary species, but the retrieved evidence did not establish a common naturally occurring, breed-specific syndrome or zoonotic relevance. It is noninfectious and nontransmissible. Comparative value lies primarily in experimentally induced or genetically engineered models rather than natural animal disease.

Relevant taxa include **Mus musculus** (NCBI Taxon 10090), **Danio rerio** (7955), **Xenopus** species, chick, and human iPSC-derived cardiac systems. Orthologs of FOXJ1, SHROOM3, DVL, NODAL, and RA-pathway genes are evolutionarily conserved.

## 15. Model organisms

- **Shroom3 gene-trap mouse:** reproduces VSD, DORV, and thin LV myocardium with variable penetrance; useful for PCP, actomyosin, neural-crest, second-heart-field, and cardiomyocyte-polarity studies. Limitation: developmental lethality and species-specific anatomy. (durbin2020shroom3isdownstream pages 1-7)
- **Foxj1-loss mouse:** randomized looping, dextrocardia/abnormal looping, AVSD, DORV, single ventricle, and abnormal great-artery position; strong model for motile cilia and left–right patterning. (padua2023congenitalheartdefects pages 1-2)
- **Zebrafish/Xenopus:** rapid, accessible embryos support cilia, laterality, second-heart-field, and CRISPR studies. Limitations include two-chambered zebrafish anatomy, gene duplication, and imperfect antibody/tool transfer.
- **Chick:** valuable for neural-crest ablation, lineage tracing, and hemodynamic manipulation, but genetic resources and human correspondence are less complete.
- **Human iPSC/cardiac organoid systems:** permit patient-variant editing and cell-autonomous assays; limitations include immaturity, incomplete three-dimensional outflow anatomy, genomic instability, and inability to reproduce maternal–placental circulation. A 2024 review emphasizes that model choice must match the question; no single platform reproduces the full human DORV phenotype. DOI: https://doi.org/10.6026/973206300200415. (shorbaji2024currentgeneticmodels pages 1-2)

## Evidence appraisal and key gaps

The most authoritative recent DORV-specific evidence retrieved was a 2024 CMR review and the 2023 FOXJ1 human/functional study. Primary DORV cohorts remain heterogeneous in nomenclature, era, anatomy, and operation, limiting pooled survival or phenotype-frequency estimates. There is no validated DORV-specific biomarker, molecular signature, protective factor, pharmacogenomic rule, or disease-modifying medical therapy. Genomic yields quoted above are principally from broader CHD/conotruncal cohorts and must be labeled accordingly. Several retrieved records supplied DOI and publication date but not PMID; therefore, DOI URLs are reported rather than inventing unverified PMID values.

References

1. (moscatelli2024importanceofcardiovascular pages 8-10): Sara Moscatelli, Alice Pozza, Isabella Leo, Jessica Ielapi, Alessandra Scatteia, Sofia Piana, Annachiara Cavaliere, Elena Reffo, and Giovanni Di Salvo. Importance of cardiovascular magnetic resonance applied to congenital heart diseases in pediatric age: a narrative review. Children, 11:878, Jul 2024. URL: https://doi.org/10.3390/children11070878, doi:10.3390/children11070878. This article has 17 citations.

2. (shorbaji2024currentgeneticmodels pages 1-2): Ayat Shorbaji, Peter Natesan Pushparaj, Sherin Bakhashab, Ayat B Ayat B Al-Ghafari, Rana R Al-Rasheed, Loubna Siraj Mira, Mohammad Abdullah Basabrain, Majed Alsulami, Isam M. Abu Zeid, Muhammad Imran Naseer, and Mahmood Rasool. Current genetic models for studying congenital heart diseases: advantages and disadvantages. Bioinformation, 20:415-429, May 2024. URL: https://doi.org/10.6026/973206300200415, doi:10.6026/973206300200415. This article has 1 citations.

3. (NCT00972608 chunk 1): Timothy Slesnick. Surgical Planning for Reconstruction of Complex Heart Defects. Emory University. 2009. ClinicalTrials.gov Identifier: NCT00972608

4. (findley2022congenitalheartdefects pages 1-2): Tina O. Findley, Alyssa K. Crain, Smridhi Mahajan, Ahmed Deniwar, Jessica Davis, Ana S. Solis Zavala, Antonio F. Corno, and David Rodriguez‐Buritica. Congenital heart defects and copy number variants associated with neurodevelopmental impairment. American Journal of Medical Genetics Part A, 188:13-23, Sep 2022. URL: https://doi.org/10.1002/ajmg.a.62484, doi:10.1002/ajmg.a.62484. This article has 19 citations.

5. (yasuhara2021geneticsofcongenital pages 9-10): Jun Yasuhara and Vidu Garg. Genetics of congenital heart disease: a narrative review of recent advances and clinical implications. Translational Pediatrics, 10:2366-2386, Sep 2021. URL: https://doi.org/10.21037/tp-21-297, doi:10.21037/tp-21-297. This article has 130 citations and is from a peer-reviewed journal.

6. (durbin2020shroom3isdownstream pages 1-7): Matthew D. Durbin, James O’Kane, Samuel Lorentz, Anthony B. Firulli, and Stephanie M. Ware. Shroom3 is downstream of the planar cell polarity pathway and loss-of-function results in congenital heart defects. Developmental Biology, 464:124-136, Aug 2020. URL: https://doi.org/10.1016/j.ydbio.2020.05.013, doi:10.1016/j.ydbio.2020.05.013. This article has 42 citations and is from a peer-reviewed journal.

7. (padua2023congenitalheartdefects pages 1-2): Maria B Padua, Benjamin M Helm, John R Wells, Amanda M Smith, Helen M Bellchambers, Arthi Sridhar, and Stephanie M Ware. Congenital heart defects caused by foxj1. Human molecular genetics, 32:2335-2346, May 2023. URL: https://doi.org/10.1093/hmg/ddad065, doi:10.1093/hmg/ddad065. This article has 21 citations and is from a domain leading peer-reviewed journal.

8. (nakajima2019retinoicacidsignaling pages 1-2): Yuji Nakajima. Retinoic acid signaling in heart development. genesis, Jul 2019. URL: https://doi.org/10.1002/dvg.23300, doi:10.1002/dvg.23300. This article has 58 citations and is from a peer-reviewed journal.

9. (corno2023narrativereviewof pages 1-2): Antonio F. Corno, Tina O. Findley, and Jorge D. Salazar. Narrative review of single ventricle: where are we after 40 years? Translational Pediatrics, 12:221-244, Feb 2023. URL: https://doi.org/10.21037/tp-22-573, doi:10.21037/tp-22-573. This article has 25 citations and is from a peer-reviewed journal.

10. (spicer2014ventricularseptaldefect pages 1-2): Diane E Spicer, Hao H Hsu, Jennifer Co-Vu, Robert H. Anderson, and F. J. Fricker. Ventricular septal defect. Orphanet Journal of Rare Diseases, Dec 2014. URL: https://doi.org/10.1186/s13023-014-0144-2, doi:10.1186/s13023-014-0144-2. This article has 130 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Double_Outlet_Right_Ventricle-deep-research-falcon_artifacts/artifact-00.md)