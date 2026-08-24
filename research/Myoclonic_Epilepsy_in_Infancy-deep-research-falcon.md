---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-05T20:24:18.087270'
end_time: '2026-08-05T20:33:01.438872'
duration_seconds: 523.35
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Myoclonic Epilepsy in Infancy
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 8
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Myoclonic_Epilepsy_in_Infancy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Myoclonic Epilepsy in Infancy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Myoclonic Epilepsy in Infancy** covering all of the
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
- **Disease Name:** Myoclonic Epilepsy in Infancy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Myoclonic Epilepsy in Infancy** covering all of the
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


# Myoclonic Epilepsy in Infancy: Disease-Characteristics Report

## Executive summary and scope

**Myoclonic epilepsy in infancy (MEI)** is a rare, usually self-limited generalized epilepsy syndrome beginning in an otherwise normally developing infant. Its defining events are brief generalized myoclonic seizures, particularly of the head and upper limbs, occurring repeatedly in wakefulness and sleep. The most authoritative current definition is the International League Against Epilepsy (ILAE) 2022 position statement on neonatal- and infant-onset epilepsy syndromes, published May 2022 (DOI: https://doi.org/10.1111/epi.17239). (zuberi2022ilaeclassificationand pages 12-14)

A critical terminology warning is required: **MEI is not Dravet syndrome**, whose historical name was “severe myoclonic epilepsy in infancy” (SMEI). Dravet syndrome is a developmental and epileptic encephalopathy, usually associated with *SCN1A*, prolonged febrile or afebrile hemiclonic/generalized convulsive seizures, pharmacoresistance, and developmental impairment. MEI must also not be merged with **familial infantile myoclonic epilepsy**, a separately indexed genetic entity associated in disease databases with genes including *TBC1D24*, *SCN8A*, *CPLX1*, and *KIF5A*. Open Targets gives classic MEI as MONDO_0100566 but reports no established disease–target association for that entity. (OpenTargets Search: myoclonic epilepsy in infancy, zuberi2022ilaeclassificationand pages 12-14)

| Domain | Evidence summary for Myoclonic Epilepsy in Infancy (MEI) | Suggested ontology terms | Key citation |
|---|---|---|---|
| Classification / scope | Rare infant-onset epilepsy syndrome recognized by ILAE 2022; a self-limited infantile generalized epilepsy syndrome. **Do not conflate** with Dravet syndrome (formerly severe myoclonic epilepsy in infancy; developmental/epileptic encephalopathy, usually SCN1A-related) or with **familial infantile myoclonic epilepsy** (distinct familial/genetic entity). MONDO: **MONDO_0100566**. | MONDO: MONDO_0100566; NCIT: Epilepsy syndrome-related concept; HPO: HP:0002123 (Generalized myoclonic seizure) | (OpenTargets Search: myoclonic epilepsy in infancy, zuberi2022ilaeclassificationand pages 12-14) |
| Epidemiology | Rare: **<0.8%** of children with epilepsy in specialty settings; **1.1%** of all epilepsy with onset before 36 months in a population-based cohort. Male predominance about **2:1**. | PATO/clinical descriptor: male predominance | (zuberi2022ilaeclassificationand pages 12-14) |
| Onset | Usual onset **4 months to 3 years**, with peak **6–18 months**. Onset at **≤4 months** or **>3 years** is a warning/exclusionary feature for classic MEI. | HPO: HP:0011463 (Childhood onset), HP:0003593 (Infantile onset) | (zuberi2022ilaeclassificationand pages 12-14, zuberi2022ilaeclassificationand pages 14-16, bayat2021epilepsysyndromesin pages 6-8) |
| Core seizures | Mandatory phenotype: frequent **myoclonic seizures** involving **head and upper limbs/upper arms**, occurring **multiple times daily**, during **wakefulness and sleep**. At syndrome onset, other seizure types should be absent. | HPO: HP:0002123 (Generalized myoclonic seizure) | (zuberi2022ilaeclassificationand pages 12-14, bayat2021epilepsysyndromesin pages 6-8) |
| Triggers / reflex features | About **one-third** have reflex-provoked seizures triggered by **sudden noise, touch, or startle**; intermittent photic stimulation may also precipitate events in some reports. | HPO: HP:0025258 (Startle-induced seizure) or related reflex-seizure descriptor | (zuberi2022ilaeclassificationand pages 12-14, zuberi2022ilaeclassificationand pages 14-16) |
| EEG | Background typically **normal while awake**. Interictal EEG shows **generalized spike-wave or polyspike-wave** discharges, often around **~3 Hz**, more evident in **early sleep**. If sleep EEG lacks generalized spike-wave, **ictal EEG is strongly recommended** because some myoclonic events may lack a clear EEG correlate. | HPO: HP:0010848 (Abnormality of EEG); EDAM/EEG descriptor: generalized spike-wave discharge | (zuberi2022ilaeclassificationand pages 12-14, zuberi2022ilaeclassificationand pages 14-16) |
| MRI / imaging | **No causal lesion** expected; **nonlesional brain MRI** supports diagnosis. Structural lesion argues against classic MEI. | UBERON: brain; RadLex/SNOMED descriptor: normal brain MRI | (zuberi2022ilaeclassificationand pages 14-16) |
| Development / exam | **Development before seizure onset is typically normal** and neurological examination is normal. Long-term development is normal in **63–85%**; some later show **mild intellectual disability, learning disorder, or attention problems**; rarely moderate-severe ID occurs. | HPO: HP:0001263 (Global developmental delay) when present; HP:0001249 (Intellectual disability); HP:0007018 (Attention deficit) | (zuberi2022ilaeclassificationand pages 12-14) |
| Genetics | Family history of epilepsy or febrile seizures in about **10%**. **No causal genes are established for classic MEI** in the ILAE 2022 definition. Reported gene-associated “myoclonic epilepsy of infancy” cases should be interpreted cautiously as possible **phenocopies/etiology-specific epilepsies**, not proof of monogenic classic MEI. | No validated causal gene annotation for classic MEI; avoid asserting SCN1A/SLC2A1/YWHAG as established MEI causes | (zuberi2022ilaeclassificationand pages 12-14, zuberi2022ilaeclassificationand pages 14-16, bayat2021epilepsysyndromesin pages 6-8) |
| Course / prognosis | Favorable seizure course: myoclonic seizures remit in **nearly all cases** within **6 months to 5 years**; most children can discontinue antiseizure medication. About **10%** later develop another epilepsy, most commonly **juvenile myoclonic epilepsy**. | HPO: HP:0011458 (EEG with generalized spike-wave); clinical course descriptor: self-limited/remitting | (zuberi2022ilaeclassificationand pages 12-14, bayat2021epilepsysyndromesin pages 6-8) |
| Diagnosis / differential | Diagnosis is syndrome-based using age at onset, seizure semiology, normal development, normal exam, normal/nonlesional MRI, and generalized spike-/polyspike-wave on EEG. Exclusionary seizure types at onset include **absence, atonic, epileptic spasms, focal seizures, generalized tonic-clonic, or clonic seizures**. Key differentials: **benign myoclonus of infancy**, **hyperekplexia**, **hypnic jerks**, **Dravet syndrome**, and **epilepsy with myoclonic-atonic seizures**. | HPO: HP:0002376 (Febrile seizures) when present; SNOMED/NCIT differential diagnosis descriptors | (zuberi2022ilaeclassificationand pages 12-14, zuberi2022ilaeclassificationand pages 14-16) |
| Treatment / evidence gaps | No MEI-specific modern trials were identified. Standard practice in reviews has favored antiseizure medication with later withdrawal after remission; ILAE evidence notes that **most children discontinue treatment** after remission, but robust comparative data are lacking. **Evidence gaps:** no established biomarker, no confirmed molecular pathway, no precision therapy, no prevention strategy, no disease-specific clinical trials located for classic MEI. | NCIT: Anticonvulsant therapy; evidence-gap flag for biomarker/genetic/advanced-therapy fields | (zuberi2022ilaeclassificationand pages 12-14, bayat2021epilepsysyndromesin pages 6-8) |


*Table: This table compiles ontology-ready, knowledge-base-focused evidence for classic Myoclonic Epilepsy in Infancy, centered on the 2022 ILAE definition and supporting review data. It highlights key diagnostic and prognostic facts while explicitly separating MEI from Dravet syndrome and familial infantile myoclonic epilepsy.*

## 1. Disease information

### Definition and classification

MEI is an electroclinical syndrome—an age-dependent cluster of seizure and EEG features—rather than a disease currently defined by a single molecular lesion. The ILAE places it among epilepsy syndromes beginning in neonates and infants and describes a self-limited course in most affected children. Data are aggregated from syndrome-level clinical cohorts, specialty-center series, population-based epilepsy cohorts, and expert consensus; they are **not individual-patient EHR data** in this report. (zuberi2022ilaeclassificationand pages 12-14)

**Preferred name:** Myoclonic epilepsy in infancy.  
**Common synonyms:** myoclonic epilepsy of infancy; benign myoclonic epilepsy in infancy; benign myoclonic epilepsy of infancy. “Benign” is now generally avoided because 15–37% of reported patients do not have completely normal long-term neurodevelopment and approximately 10% later develop another epilepsy. The reflex-predominant phenotype may be called **reflex myoclonic epilepsy in infancy**. (zuberi2022ilaeclassificationand pages 14-16, zuberi2022ilaeclassificationand pages 12-14)

**Identifiers:**

- **MONDO:** MONDO:0100566, myoclonic epilepsy in infancy. (OpenTargets Search: myoclonic epilepsy in infancy)
- **EFO:** EFO:0700105, myoclonic epilepsy of infancy, as returned by Open Targets. (OpenTargets Search: myoclonic epilepsy in infancy)
- **OMIM/Orphanet:** no confidently verified disease-specific identifier was recovered for classic sporadic MEI; do not substitute identifiers for familial infantile myoclonic epilepsy or Dravet syndrome.
- **ICD-10/ICD-11:** coding is generally under epilepsy/generalized epilepsy categories; a uniquely validated MEI-specific billable code was not established in the retrieved evidence.
- **MeSH:** use the broader epilepsy/myoclonic epilepsy concepts; no uniquely verified MEI descriptor was identified.

## 2. Etiology, risk, and protective factors

The cause of classic MEI remains unresolved. Approximately **10%** have a family history of epilepsy or febrile seizures, supporting genetic susceptibility, but the ILAE review states that **no causal gene has been identified** for the classic syndrome. Therefore, *SCN1A*, *SLC2A1*, *YWHAG*, *TBC1D24*, or other epilepsy genes should not be annotated as established MEI causes without evidence that the individual satisfies classic ILAE MEI criteria and that competing etiology-specific syndromes have been excluded. (zuberi2022ilaeclassificationand pages 14-16, bayat2021epilepsysyndromesin pages 6-8)

No reproducible susceptibility locus, modifier gene, protective allele, epigenetic signature, or chromosomal abnormality is established. The relevant inheritance model is consequently **unknown/complex**, not proven autosomal dominant or recessive. Penetrance, carrier frequency, anticipation, founder effects, and germline-mosaicism rates cannot presently be assigned.

No toxin, pollutant, occupation, diet, infection, vaccination, smoking exposure, or other lifestyle factor is established as a cause. Sudden sound, touch, startle, and occasionally intermittent photic stimulation can **precipitate individual seizures** but are reflex triggers, not causes of the underlying epilepsy. Febrile seizures occur in up to one-third and may precede or follow the myoclonic seizures, but fever should not be interpreted as a demonstrated etiologic exposure. (zuberi2022ilaeclassificationand pages 12-14, zuberi2022ilaeclassificationand pages 14-16)

No validated genetic or environmental protective factor, formal gene–environment interaction, or primary prevention strategy is known.

## 3. Phenotypes

### Core seizure phenotype

The mandatory clinical phenotype is frequent brief myoclonic seizures involving the **head and upper arms/upper limbs**, commonly producing head nods, shoulder or arm jerks, or brief loss of hand control. Events occur several or multiple times daily, in both wakefulness and sleep. Consciousness is usually preserved or only too briefly affected to assess. Approximately one-third of patients have reflex events induced by noise, touch, or startle. (zuberi2022ilaeclassificationand pages 12-14, bayat2021epilepsysyndromesin pages 6-8)

Suggested terms include **generalized myoclonic seizure (HPO HP:0002123)**, **infantile onset (HP:0003593)**, **febrile seizures (HP:0002376)** when present, and an appropriate reflex/startle-induced seizure term when supported by the record. Because ontology labels evolve, identifiers should be checked against the production HPO release before ingestion.

### EEG phenotype

The awake background is typically normal. Interictal EEG demonstrates generalized spike-wave or polyspike-wave discharges, commonly more evident in early sleep. The electroclinical discharge is often described at approximately 3 Hz. A sleep recording is therefore important. If interictal sleep EEG does not show generalized spike-wave, ictal video-EEG is strongly recommended to distinguish epileptic myoclonus from nonepileptic infantile myoclonus, hyperekplexia, or physiological hypnic jerks. (zuberi2022ilaeclassificationand pages 12-14, zuberi2022ilaeclassificationand pages 14-16)

Suggested annotations are **abnormal EEG (HP:0010848)** and generalized spike-wave/polyspike-wave descriptors. The ictal event and EEG correlate should be represented separately where the data model permits.

### Development, behavior, and examination

Development before seizure onset and neurological examination are ordinarily normal. Long-term development is reported as normal in **63–85%**. A minority develops mild intellectual disability, learning difficulties, or attention problems; moderate-to-severe intellectual disability is rare and is not necessarily proportional to seizure frequency. Relevant conditional terms include intellectual disability (**HP:0001249**), global developmental delay (**HP:0001263**), learning disability, and attention deficit. (zuberi2022ilaeclassificationand pages 12-14)

### Other clinical findings

Febrile seizures occur in up to one-third. At onset, absence, atonic, focal, clonic, generalized tonic-clonic seizures, or epileptic spasms are exclusionary for classic MEI. Falls, persistent focal deficits, dysmorphism, movement disorder, regression, and systemic laboratory abnormalities are not defining features and should prompt reassessment. (zuberi2022ilaeclassificationand pages 12-14)

### Quality of life

No MEI-specific EQ-5D, SF-36, PROMIS, or validated caregiver quality-of-life statistics were identified. During the active phase, multiple daily jerks can impair feeding, object handling, sleep, safety, and caregiver confidence. Later learning or attention problems may affect school functioning even after seizure remission, which helps explain why “benign” is an imperfect label. These functional effects are clinically plausible but are not quantified in the available syndrome literature.

## 4. Genetic and molecular information

There is presently **no validated causal gene, recurrent pathogenic variant, HGNC-defined gene set, allele frequency, or established loss-/gain-of-function mechanism for classic MEI**. Consequently, no variant should be classified as “pathogenic for MEI” solely because it occurs in a person with infantile myoclonus. Molecular findings must be interpreted under ACMG/AMP criteria and against the gene-specific phenotype.

The database distinction is especially important: Open Targets links **familial infantile myoclonic epilepsy** (MONDO:0011506) to *TBC1D24*, *SCN8A*, *CPLX1*, and *KIF5A*, while its classic MEI record has no associated targets. These associations cannot be transferred across disease records. (OpenTargets Search: myoclonic epilepsy in infancy)

No established modifier gene, DNA-methylation signature, histone abnormality, pathogenic copy-number change, or recurrent chromosomal rearrangement has been demonstrated. Reports of gene-positive MEI-like phenotypes should be represented as **gene-associated epilepsy with an MEI-like presentation** pending replication and nosological validation.

## 5. Environmental information

No causal environmental exposure or infectious agent has been identified. Sound, tactile stimulation, startle, and occasionally light stimulation activate susceptible seizure networks in reflex MEI. Practical stimulus management may reduce provoked events, but excessive avoidance can adversely affect normal infant development and is not disease-modifying. There is no evidence that diet, exercise, alcohol, tobacco, pollution, radiation, or occupational exposure has a disease-specific role in infants with classic MEI. (zuberi2022ilaeclassificationand pages 12-14, zuberi2022ilaeclassificationand pages 14-16)

## 6. Mechanism and pathophysiology

### Current mechanistic model

The best-supported causal chain is electroclinical rather than molecular:

1. An unknown, probably developmentally regulated susceptibility alters excitability in bilateral generalized cortical–subcortical networks.
2. Sleep-state transitions or abrupt sensory input can synchronize these networks.
3. Generalized spike-/polyspike-wave activity recruits bilateral motor cortex and descending motor pathways.
4. Brief synchronous muscle activation produces head and upper-limb myoclonus.
5. Maturation and/or antiseizure treatment reduces network susceptibility, accounting for remission in nearly all cases.

Steps 1 and 5 remain hypotheses; no MEI-specific channel, receptor, transmitter, inflammatory, metabolic, or mTOR/PI3K-AKT pathway defect is established. The normal neurological examination, normal awake background, and nonlesional MRI support functional network dysregulation rather than progressive tissue destruction. (zuberi2022ilaeclassificationand pages 12-14, zuberi2022ilaeclassificationand pages 14-16)

Suggested broad GO annotations, to be used as mechanistic hypotheses rather than demonstrated disease mechanisms, include **regulation of membrane potential (GO:0042391)**, **synaptic signaling (GO:0099536)**, **regulation of neuronal action potential**, and **synchronization of neuronal activity**. Candidate cell types include excitatory and inhibitory neurons—**glutamatergic neuron (CL:0000679)** and **GABAergic neuron (CL:0000617)**—but no MEI-specific cellular pathology has been shown.

No disease-specific transcriptomic, single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, CRISPR-screen, or multi-omics result was identified. There is likewise no established immune activation, oxidative injury, neurodegeneration, apoptosis, autophagy defect, enzyme deficiency, or tissue-damage mechanism.

## 7. Anatomical structures affected

The clinically affected organ is the **central nervous system**, particularly bilateral brain networks generating generalized epileptiform activity and motor output. Suggested anatomical annotations are **brain (UBERON:0000955)**, **cerebral cortex (UBERON:0000956)**, and possibly thalamus/generalized thalamocortical network as a systems-level inference. There is no consistent focal lesion, lateralization, or secondary organ involvement. (zuberi2022ilaeclassificationand pages 14-16)

At subcellular level, neuronal plasma membrane, axon, synapse, and postsynaptic membrane are biologically plausible compartments, but none is specifically proven. A normal/nonlesional MRI is expected; a causal structural lesion argues against classic MEI.

## 8. Temporal development

Onset is usually **4 months to 3 years**, peaking at **6–18 months**. Onset at or before 4 months or after 3 years is an alert against the classic diagnosis. The beginning may be abrupt from the caregiver’s perspective, but the course is episodic, with multiple daily seizures during the active phase. (zuberi2022ilaeclassificationand pages 12-14, zuberi2022ilaeclassificationand pages 14-16)

Myoclonic seizures remit in nearly all patients **within 6 months to 5 years after onset**. Most ultimately discontinue antiseizure medication. Approximately **10%** develop another epilepsy in later childhood or adolescence, most often juvenile myoclonic epilepsy. Developmental surveillance should therefore continue after seizure remission. (bayat2021epilepsysyndromesin pages 6-8, zuberi2022ilaeclassificationand pages 12-14)

There are no validated early/intermediate/advanced stages. The useful clinical phases are active infantile myoclonus, seizure remission, medication withdrawal where appropriate, and longer-term monitoring for learning/attention difficulties or later generalized epilepsy.

## 9. Inheritance and population

MEI constitutes **<0.8% of children with epilepsy seen in specialty centers** and approximately **1.1% of epilepsies beginning before 36 months** in the population-based evidence summarized by ILAE. Male predominance is approximately **2:1**. These figures do not provide robust prevalence per 100,000 or annual incidence estimates, and geographic or ancestry-specific differences have not been established. (zuberi2022ilaeclassificationand pages 12-14)

Family history of epilepsy or febrile seizures occurs in about 10%, but Mendelian inheritance, penetrance, expressivity, carrier frequency, anticipation, founder effects, and consanguinity effects remain undefined. (zuberi2022ilaeclassificationand pages 14-16, bayat2021epilepsysyndromesin pages 6-8)

## 10. Diagnostics

### Clinical and electrophysiological diagnosis

Diagnosis rests on the age-dependent electroclinical pattern:

- onset between 4 months and 3 years;
- normal pre-onset development and neurological examination;
- multiple daily generalized myoclonic seizures of head/upper limbs in wakefulness and sleep;
- generalized spike-wave or polyspike-wave, especially in sleep;
- no causal structural lesion;
- no competing seizure types at onset. (zuberi2022ilaeclassificationand pages 12-14, zuberi2022ilaeclassificationand pages 14-16)

**Video-EEG including sleep** is the key test. Ictal recording is particularly valuable if habitual jerks have no clear interictal correlate. Brain MRI is expected to be nonlesional; MRI is appropriate when there are focal findings, atypical development, abnormal examination, or an atypical EEG. Routine blood chemistry, metabolic studies, CSF, biopsy, PET, EMG, ECG, or other biomarkers are not diagnostic for classic MEI and should be guided by atypical features.

### Genetic testing

Genetic testing is not required to confirm a textbook MEI phenotype because no causal gene is established. Nevertheless, an infantile epilepsy panel or exome/genome sequencing is reasonable when there is developmental delay/regression, dysmorphism, drug resistance, focal or multiple seizure types, abnormal MRI, very early onset, a strong family history, or failure to meet ILAE criteria. Such testing primarily detects **alternative etiologies**, not classic MEI. Broad early-onset epilepsy literature supports panels, exomes, or genomes because they can identify actionable phenocopies, but this evidence is not an MEI-specific diagnostic-yield estimate. (bayat2021epilepsysyndromesin pages 6-8)

CMA is appropriate when developmental or congenital abnormalities suggest a copy-number disorder. Karyotype, FISH, mitochondrial DNA, RNA sequencing, and repeat-expansion testing are not routine MEI tests unless another phenotype indicates them.

### Differential diagnosis

- **Benign myoclonus of early infancy:** similar jerks but no epileptiform ictal EEG.
- **Hyperekplexia:** exaggerated pathological startle, often with stiffness, without generalized epileptic EEG correlate.
- **Hypnic jerks:** physiological sleep-onset myoclonus without epileptic correlate.
- **Dravet syndrome:** usually prolonged febrile/afebrile hemiclonic or generalized convulsive seizures beginning in the first year, later multiple seizure types, developmental slowing, and frequent *SCN1A* pathogenic variants.
- **Epilepsy with myoclonic-atonic seizures:** later polymorphic generalized epilepsy with myoclonic-atonic/drop seizures.
- **Infantile epileptic spasms syndrome:** clusters of spasms, developmental concerns, and hypsarrhythmia or related EEG pattern.
- **Early myoclonic encephalopathy/DEE:** neonatal or very early onset, abnormal development/examination, severe EEG abnormality, and poor course.
- **Focal structural epilepsy:** focal semiology/EEG or causal MRI lesion. (zuberi2022ilaeclassificationand pages 12-14, zuberi2022ilaeclassificationand pages 14-16)

There is no population or newborn screening program for MEI. Screening asymptomatic relatives is not supported because no validated causal gene exists.

## 11. Outcome and prognosis

Seizure prognosis is excellent: nearly all patients remit over 6 months to 5 years, and most eventually stop medication. Long-term neurodevelopment is normal in 63–85%, but mild intellectual, learning, or attention problems occur in a clinically important minority. Approximately 10% later develop another epilepsy. (zuberi2022ilaeclassificationand pages 12-14)

No MEI-specific 5- or 10-year survival rate, excess mortality rate, SUDEP estimate, or reduction in life expectancy was identified. Current evidence does not characterize classic MEI as a progressive or lethal disorder. Prognostically adverse signals include atypical onset age, abnormal development or examination, additional seizure types, focal EEG/MRI abnormalities, persistent drug resistance, or failure of expected remission; these features should trigger diagnostic reconsideration rather than automatically being labeled severe MEI.

No validated molecular prognostic biomarker or disease-specific quality-of-life instrument exists.

## 12. Treatment

### Pharmacotherapy and strategy

Evidence consists mainly of observational series and expert practice rather than modern randomized MEI trials. A broad-spectrum antiseizure medication is used when seizures are frequent, disruptive, or diagnostically secure. Historical and review-based practice most commonly favors **valproate** as first-line monotherapy for generalized myoclonus; levetiracetam, clonazepam, or topiramate may be considered when valproate is unsuitable or ineffective. These alternatives have substantially weaker MEI-specific evidence. The ILAE evidence establishes that most patients ultimately discontinue therapy after remission but does not provide comparative response rates. (zuberi2022ilaeclassificationand pages 12-14)

Suggested NCIT-level intervention concepts are **anticonvulsant therapy**, **valproic acid**, **levetiracetam**, **clonazepam**, and **topiramate**; exact NCIT identifiers should be verified against the current release. Medication selection and withdrawal should be supervised by a pediatric neurologist. Valproate requires age-appropriate counseling and monitoring for hepatic toxicity, pancreatitis, thrombocytopenia, hyperammonemia, weight/metabolic effects, and future reproductive risk. Benzodiazepines may cause sedation or tolerance; levetiracetam may cause behavioral adverse effects; topiramate can impair appetite, cognition, acid-base balance, and renal-stone risk.

A practical algorithm is: confirm epileptic myoclonus with video-EEG including sleep; treat frequent events with a broad-spectrum ASM; reassess seizure and developmental response; investigate phenocopies if resistant or atypical; and consider gradual withdrawal after sustained electroclinical remission. There is no evidence for epilepsy surgery because MEI is generalized and nonlesional. Ketogenic diet, vagus-nerve stimulation, immunotherapy, or other interventions are not routine for classic MEI; needing them should prompt reconsideration of the diagnosis.

### Advanced and experimental therapy

No MEI-specific gene therapy, ASO, siRNA, mRNA, cell therapy, CRISPR therapy, targeted small molecule, immunotherapy, or interventional clinical trial was identified. Trials retrieved for *SCN1A*-Dravet syndrome—including zorevunersen/STK-001 studies—are **not MEI trials** and should not populate the MEI treatment record.

Supportive care includes seizure first-aid education, individualized safety advice, developmental and school surveillance, and speech, occupational, behavioral, or educational intervention when deficits are detected.

## 13. Prevention

Primary prevention is unavailable because the cause is unknown. Vaccination is not a disease-specific preventive intervention and routine immunization should follow standard pediatric recommendations. Avoidance of known abrupt sensory triggers may reduce individual reflex seizures but does not prevent MEI and should be balanced against normal development.

Secondary prevention consists of prompt recognition, video-EEG confirmation, treatment when warranted, and avoidance of diagnostic delay. Tertiary prevention includes injury precautions, fever/seizure plans, monitoring treatment toxicity, developmental surveillance, and follow-up into adolescence for later generalized epilepsy. There is no validated carrier, prenatal, preimplantation, newborn, or cascade-screening program for classic MEI. Genetic counseling should emphasize uncertain etiology and avoid assigning a Mendelian recurrence risk without a specific molecular diagnosis.

## 14. Other species and natural disease

No naturally occurring veterinary disorder was identified as a validated species homolog of classic human MEI. Animal epilepsies involving myoclonus or orthologues such as *Scn1a*, *Scn8a*, or *Tbc1d24* model other genetic epilepsies and must not automatically be labeled MEI. No zoonotic transmission or cross-species infectious susceptibility applies.

## 15. Model organisms

No validated disease-specific mouse, rat, zebrafish, Drosophila, *C. elegans*, organoid, iPSC, or cellular model of classic MEI was identified, consistent with the absence of a confirmed molecular cause. Generalized spike-wave and reflex-seizure models can test network excitability or antiseizure drugs, but they do not reproduce the complete age, seizure, EEG, remission, and developmental phenotype required for construct and face validity. Gene-specific models are appropriate only for the corresponding etiology-specific epilepsy or phenocopy.

## Evidence appraisal and recent developments

The decisive modern development is the **2022 ILAE standardized syndrome definition**, which provides epidemiology, mandatory criteria, alerts, exclusions, EEG expectations, imaging findings, and natural history. Its abstract defines an epilepsy syndrome as an electroclinical cluster and separates self-limited infantile syndromes from developmental and epileptic encephalopathies; this is the appropriate framework for MEI. Publication: May 2022; DOI URL: https://doi.org/10.1111/epi.17239. (zuberi2022ilaeclassificationand pages 12-14)

A 2021 genetics review states that comprehensive panels, exomes, and genomes have increased diagnostic yield in early-onset epilepsies and enabled precision medicine, while specifically noting that causal genes for MEI had not been identified. Its abstract states that “early genetic testing is a cornerstone” of precision strategies in monogenic epilepsies; for MEI, the principal present utility is finding an alternative molecular diagnosis. Publication: July 2021; DOI URL: https://doi.org/10.3390/genes12071051. (bayat2021epilepsysyndromesin pages 6-8)

No 2023–2024 primary study was found that overturns the 2022 ILAE understanding of classic MEI, establishes a causal gene, supplies population prevalence per 100,000, or demonstrates a disease-specific therapy. The most defensible current expert position is therefore conservative: diagnose MEI electroclinically, preserve strict separation from Dravet syndrome and familial infantile myoclonic epilepsy, use genetic testing for atypical presentations/phenocopies, and explicitly mark molecular, omics, prevention, model, and trial fields as unresolved.

References

1. (zuberi2022ilaeclassificationand pages 12-14): Sameer M. Zuberi, Elaine Wirrell, Elissa Yozawitz, Jo M. Wilmshurst, Nicola Specchio, Kate Riney, Ronit Pressler, Stephane Auvin, Pauline Samia, Edouard Hirsch, Santiago Galicchio, Chahnez Triki, O. Carter Snead, Samuel Wiebe, J. Helen Cross, Paolo Tinuper, Ingrid E. Scheffer, Emilio Perucca, Solomon L. Moshé, and Rima Nabbout. Ilae classification and definition of epilepsy syndromes with onset in neonates and infants: position statement by the ilae task force on nosology and definitions. Epilepsia, 63:1349-1397, May 2022. URL: https://doi.org/10.1111/epi.17239, doi:10.1111/epi.17239. This article has 1122 citations and is from a domain leading peer-reviewed journal.

2. (OpenTargets Search: myoclonic epilepsy in infancy): Open Targets Query (myoclonic epilepsy in infancy, 24 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (zuberi2022ilaeclassificationand pages 14-16): Sameer M. Zuberi, Elaine Wirrell, Elissa Yozawitz, Jo M. Wilmshurst, Nicola Specchio, Kate Riney, Ronit Pressler, Stephane Auvin, Pauline Samia, Edouard Hirsch, Santiago Galicchio, Chahnez Triki, O. Carter Snead, Samuel Wiebe, J. Helen Cross, Paolo Tinuper, Ingrid E. Scheffer, Emilio Perucca, Solomon L. Moshé, and Rima Nabbout. Ilae classification and definition of epilepsy syndromes with onset in neonates and infants: position statement by the ilae task force on nosology and definitions. Epilepsia, 63:1349-1397, May 2022. URL: https://doi.org/10.1111/epi.17239, doi:10.1111/epi.17239. This article has 1122 citations and is from a domain leading peer-reviewed journal.

4. (bayat2021epilepsysyndromesin pages 6-8): Allan Bayat, Michael Bayat, Guido Rubboli, and Rikke S. Møller. Epilepsy syndromes in the first year of life and usefulness of genetic testing for precision therapy. Genes, 12:1051, Jul 2021. URL: https://doi.org/10.3390/genes12071051, doi:10.3390/genes12071051. This article has 119 citations.

## Artifacts

- [Edison artifact artifact-00](Myoclonic_Epilepsy_in_Infancy-deep-research-falcon_artifacts/artifact-00.md)