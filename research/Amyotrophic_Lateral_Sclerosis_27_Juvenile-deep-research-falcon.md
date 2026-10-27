---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T21:00:37.799402'
end_time: '2026-08-19T21:12:29.613521'
duration_seconds: 711.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Amyotrophic Lateral Sclerosis 27, Juvenile
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
reference_validation:
  total_references: 8
  verified: 7
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.125
  relevance_assessed: 7
  on_topic: 5
  unresolved_references:
  - "DOI:10.3233/JND-240014\u2014current"
  needs_review: true
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Amyotrophic_Lateral_Sclerosis_27_Juvenile-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Amyotrophic Lateral Sclerosis 27, Juvenile
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Amyotrophic Lateral Sclerosis 27, Juvenile** covering all of the
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
- **Disease Name:** Amyotrophic Lateral Sclerosis 27, Juvenile
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Amyotrophic Lateral Sclerosis 27, Juvenile** covering all of the
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


# Amyotrophic Lateral Sclerosis 27, Juvenile (SPTLC1-Associated)

## Executive summary

Amyotrophic lateral sclerosis 27, juvenile (ALS27) is an exceptionally rare, Mendelian motor-neuron disease caused by heterozygous gain-of-function variants in **SPTLC1**, encoding a core subunit of serine palmitoyltransferase (SPT). It usually begins in childhood with lower-limb spasticity, toe walking, gait disturbance, distal weakness, and later diffuse upper- and lower-motor-neuron involvement. Sensory function is characteristically preserved. Unlike typical adult ALS, progression is often measured in decades, although bulbar and respiratory dysfunction can eventually occur. The central mechanism is failure of ORMDL-mediated feedback inhibition of SPT, causing excessive synthesis of canonical sphingolipids rather than the abnormal 1-deoxysphingolipids characteristic of SPTLC1-related hereditary sensory and autonomic neuropathy type 1 (HSAN1). (wang2023clinicalfeaturedifference pages 5-6, lone2022sptlc1variantsassociated pages 1-3, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)

The most immediately actionable disease-specific points are: (1) include **SPTLC1** in genetic testing for childhood motor-neuron/HSP-like presentations; (2) use EMG and sensory studies to distinguish ALS27 from pure hereditary spastic paraplegia and HSAN1; (3) consider sphingolipid profiling as a research-level supportive biomarker; and (4) **avoid empiric L-serine supplementation**, because it may increase pathogenic canonical sphingolipid production. No targeted therapy or disease-specific clinical trial has established efficacy. (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 7-9, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)

| domain | disease-specific finding | quantitative/detail | evidence type/limitations |
|---|---|---|---|
| Disease identity | Amyotrophic lateral sclerosis 27, juvenile; Mendelian juvenile ALS subtype linked to **SPTLC1** | **MONDO:0859529**; target association **SPTLC1 / ENSG00000090054** (OpenTargets Search: Amyotrophic lateral sclerosis 27, juvenile-SPTLC1) | Disease-level ontology and target-association resource; does not provide full clinical detail (OpenTargets Search: Amyotrophic lateral sclerosis 27, juvenile-SPTLC1) |
| Causal gene / mechanism class | **SPTLC1** pathogenic variants cause a **dominant gain-of-function** disorder of sphingolipid biosynthesis | Pathogenic effect is increased/unrestrained SPT activity via impaired ORMDL regulation rather than classic loss of function (lone2022sptlc1variantsassociated pages 1-3, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) | Primary mechanistic human/cell studies and review synthesis; selective motor-neuron vulnerability remains incompletely explained (lone2022sptlc1variantsassociated pages 1-3, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) |
| Inheritance | Usually **autosomal dominant**, commonly **de novo** | 2023 compilation table lists many cases as **de novo**; AD familial cases also reported, including multiple **p.Leu39del** relatives (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) | Derived largely from case reports/small pedigrees; penetrance not well quantified (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) |
| Established disease variants | Recurrently implicated ALS27 variants cluster in **SPTLC1 exon 2 / N-terminal transmembrane domain** | Five established variants emphasized in reviews/comparative data: **p.A20S, p.Y23F, p.L38R, p.Leu39del, p.Phe40_Ser41del**; **p.A20T** reported as a novel case in 2023 (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) | Variant set based on early case series/reviews through 2024; later expansion possible (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) |
| Age at onset / natural history | Very early childhood onset with unusually slow course relative to FUS-JALS | In 17-patient SPTLC1 JALS comparison: **AAO 7.9 ± 4.6 years**, **100% spinal onset**, disease duration **512.0 months** (95% CI **416.7–607.3**) vs FUS-JALS **33.4 months** (95% CI **21.6–45.1**) (wang2023clinicalfeaturedifference pages 5-6) | Cohort assembled from literature plus new cases; small numbers and publication bias likely (wang2023clinicalfeaturedifference pages 5-6) |
| Core phenotype | Combined upper and lower motor neuron disease, often beginning in legs | Early **lower-limb spasticity**, toe walking/gait abnormality, weakness/atrophy; symptoms may start as early as **3–4 years**; bulbar/respiratory involvement can occur later (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) | Mostly retrospective case data; severity varies across variants/families (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) |
| Sensory / cognitive profile | Sensory system usually spared; cognition usually preserved | **No sensory neuropathy** is typical even late; normal sensory studies and at least one normal sural biopsy reported; cognitive dysfunction generally **not reported** in SPTLC1-ALS, unlike some SPTLC2 cases (mohassel2024serinepalmitoyltransferase(spt)related pages 4-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) | Important disease discriminator, but systematic neuropsychology is limited (mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) |
| Electrophysiology / pathology | Motor neuron disorder pattern supports ALS over HSP | EMG/NCS: **normal sensory studies** with **diffuse acute and chronic denervation in multiple myotomes** and no demyelinating features; extensive neurogenic damage helps distinguish from HSP (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) | Disease-specific but based on relatively few deeply phenotyped patients (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) |
| Molecular mechanism | Variants disrupt **ORMDL-SPTLC1** interaction at the ER SPT complex | SPT resides in **ER**/ER-mitochondrial contact sites; ALS variants in the **N-terminal TMD** impair ORMDL binding and feedback inhibition, causing excess canonical sphingolipid synthesis (lone2022sptlc1variantsassociated pages 1-3, lone2022sptlc1variantsassociated pages 6-8, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) | Strong cell-biochemical evidence; downstream pathway from lipid excess to motor-neuron death remains partly unresolved (lone2022sptlc1variantsassociated pages 6-8, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) |
| Biomarker signature | Distinct **canonical sphingolipid / ceramide** signature rather than HSAN1-like deoxySL excess | Elevated canonical sphingolipids, including unusual **C18:0, C20:0, C22:0** acyl-chain species; generally **not 1-deoxysphingolipid-driven** unless substrate conditions shift (lone2022sptlc1variantsassociated pages 6-8, lone2022sptlc1variantsassociated pages 1-3, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) | Promising biochemical biomarker from serum/fibroblast/cell studies; no standardized clinical cutoff/assay yet (lone2022sptlc1variantsassociated pages 6-8, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) |
| Diagnostic approach | Suspect in children with slowly progressive spastic-paraparetic/motor neuron syndrome and no sensory loss | Recommended work-up from disease-specific evidence: **broad genetic testing (WES/WGS or ALS/HSP panels including SPTLC1)** + EMG/NCS + clinical exclusion of HSP/HSAN1; lipidomics may support mechanism where available (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) | No dedicated formal diagnostic criteria for ALS27; practice extrapolated from juvenile ALS genetics literature (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) |
| Differential diagnosis | Often confused early with **hereditary spastic paraplegia**; biochemically distinct from **HSAN1** | HSP mimic: early spastic gait; ALS27 favored by LMN involvement/EMG denervation. HSAN1 differs by sensory neuropathy and deoxysphingolipid excess (wang2023clinicalfeaturedifference pages 5-6, lone2022sptlc1variantsassociated pages 1-3, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) | Differential framework is strong, but based on expert synthesis more than prospective studies (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) |
| Treatment caveat | **Avoid L-serine supplementation** in SPT-related motor-neuron disease | Reviews and mechanistic studies predict serine may **exacerbate canonical sphingolipid overproduction**; iPSC-derived motor neurons with **p.F40_S41del** reportedly worsened with serine supplementation (mohassel2024serinepalmitoyltransferase(spt)related pages 7-9, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) | Key actionable caution; not based on controlled clinical trials in ALS27 (mohassel2024serinepalmitoyltransferase(spt)related pages 7-9, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) |
| Current treatment status | No disease-specific approved therapy or registered disease-specific trial identified | Standard care remains supportive/ALS multidisciplinary management; **partial SPT inhibition** is proposed conceptually but not established clinically for ALS27 (mohassel2024serinepalmitoyltransferase(spt)related pages 7-9) | No disease-specific interventional trial retrieved; evidence for therapy is preclinical/expert-opinion level (mohassel2024serinepalmitoyltransferase(spt)related pages 7-9) |
| Models | Human cell systems provide main mechanistic evidence | Evidence includes **HEK293/COS-7** systems, **patient fibroblasts**, and **iPSC-derived lower motor neuron-like cells** with elevated canonical sphingolipids; **no murine SPT-related ALS model reported so far** in 2024 review (lone2022sptlc1variantsassociated pages 1-3, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) | Major translational gap: limited in vivo disease modeling for ALS27 specifically (mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) |
| Evidence gaps | Major unknowns remain despite strong gene-mechanism link | Missing/limited: prevalence and incidence, penetrance, validated prognosis markers, standardized lipid biomarker thresholds, controlled treatment data, and explanation for selective motor-neuron vulnerability (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) | Knowledge base should mark many epidemiology/outcome fields as **not established** rather than infer from general ALS (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7) |


*Table: This compact table summarizes the most actionable disease-specific facts for SPTLC1-associated juvenile ALS (ALS27), including identity, variants, phenotype, mechanism, diagnostics, and treatment caveats. It is designed for direct reuse in a knowledge-base entry while clearly flagging evidence limitations and unknowns.*

## 1. Disease information

### Definition and classification

ALS27 is a genetic form of juvenile ALS affecting upper and lower motor neurons, generally with onset before age 25 and commonly in early childhood. It should not be conflated with all juvenile ALS, a genetically heterogeneous group that also includes FUS-, ALS2-, SETX-, SIGMAR1-, SPG11-, and other gene-associated disorders. The defining gene–disease association is **SPTLC1–ALS27**. Open Targets records one associated target, SPTLC1, supported by five evidence records and literature including PMIDs **34059824, 34459874, 35900868, 36204986, and 40027730**. (OpenTargets Search: Amyotrophic lateral sclerosis 27, juvenile-SPTLC1)

**Identifiers and names**

- **MONDO:** MONDO:0859529.
- **Gene:** SPTLC1, serine palmitoyltransferase long-chain base subunit 1; Ensembl **ENSG00000090054**. (OpenTargets Search: Amyotrophic lateral sclerosis 27, juvenile-SPTLC1)
- **Common synonyms:** amyotrophic lateral sclerosis type 27; ALS27; juvenile ALS 27; SPTLC1-associated juvenile ALS; SPTLC1-related childhood-onset ALS; SPT-related motor-neuron disease.
- **OMIM:** commonly catalogued as an ALS27/juvenile ALS entry linked to SPTLC1; the exact OMIM accession was not independently recoverable from the retrieved evidence and should be verified directly in OMIM before database loading.
- **Orphanet:** no disease-specific ORPHA identifier was established from the retrieved evidence.
- **ICD-10:** no subtype-specific code; operational coding generally falls under **G12.21 Amyotrophic lateral sclerosis** in ICD-10-CM or the relevant G12 motor-neuron-disease category.
- **MeSH:** Amyotrophic Lateral Sclerosis; no separate ALS27 descriptor was identified.

The available evidence is principally **aggregated disease-level literature**, small case series, pedigrees, and mechanistic studies—not individual-patient EHR data.

### Key primary and recent publications

1. Mohassel et al., *Childhood amyotrophic lateral sclerosis caused by excess sphingolipid synthesis*, 2021, PMID **34059824**—foundational human genetic/mechanistic study.
2. Johnson et al., *Association of variants in the SPTLC1 gene with juvenile amyotrophic lateral sclerosis*, *JAMA Neurology*, 2021, PMID **34459874**, DOI: https://doi.org/10.1001/jamaneurol.2021.2598.
3. Lone et al., *SPTLC1 variants associated with ALS produce distinct sphingolipid signatures through impaired interaction with ORMDL proteins*, *Journal of Clinical Investigation*, July 2022, PMID **35900868**, DOI: https://doi.org/10.1172/JCI161908. Its abstract states: “ORMDL binding to the holoenzyme complex is impaired…resulting in increased SL synthesis and a distinct lipid signature.” (lone2022sptlc1variantsassociated pages 6-8, lone2022sptlc1variantsassociated pages 1-3)
4. Wang et al., *Clinical feature difference between juvenile amyotrophic lateral sclerosis with SPTLC1 and FUS mutations*, *Chinese Medical Journal*, February 2023, DOI: https://doi.org/10.1097/CM9.0000000000002495. (wang2023clinicalfeaturedifference pages 5-6)
5. Mohassel et al., *Serine Palmitoyltransferase (SPT)-related Neurodegenerative and Neurodevelopmental Disorders*, *Journal of Neuromuscular Diseases*, May 2024, DOI: https://doi.org/10.3233/JND-240014—current authoritative synthesis. (mohassel2024serinepalmitoyltransferase(spt)related pages 7-9, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)
6. Syeda et al., *Recurrent de novo SPTLC2 variant causes childhood-onset ALS by excess sphingolipid synthesis*, *JNNP* 95:103–113, online 2023/issue 2024, DOI: https://doi.org/10.1136/jnnp-2023-332132. This is not ALS27, but independently corroborates excess SPT activity as a juvenile motor-neuron-disease mechanism. (syeda2024recurrentdenovo pages 1-2)

## 2. Etiology, risk, and protective factors

### Causal factor

ALS27 is caused by **germline heterozygous SPTLC1 variants** that confer a biochemical gain of function. Most reported patients carry de novo variants, although vertical transmission and autosomal-dominant pedigrees—particularly involving p.Leu39del—are documented. The variants cluster in exon 2/N-terminal transmembrane sequences involved in binding ORMDL negative regulators. (wang2023clinicalfeaturedifference pages 5-6, lone2022sptlc1variantsassociated pages 1-3, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)

This is not a conventional multifactorial ALS susceptibility association: rare, high-effect variants are sufficient to cause a Mendelian syndrome. No infectious cause has been implicated.

### Genetic risk and modifiers

A pathogenic allele is the principal risk factor. Penetrance has not been quantified reliably; the ascertainment of affected transmitting relatives suggests substantial penetrance, but unaffected-carrier studies are insufficient. The literature provides no validated modifier gene, polygenic score, anticipation, or germline-mosaicism frequency. Parental mosaicism remains biologically possible in apparently de novo disease and should be considered in recurrence counseling.

### Environment and substrate availability

No conventional ALS environmental exposure—smoking, pesticides, metals, military service, strenuous exercise, or trauma—has been shown to cause or modify ALS27 specifically. The best-supported gene–environment/metabolic interaction is **amino-acid substrate availability**. Limiting L-serine relative to L-alanine shifted mutant SPTLC1 lipid production toward 1-deoxysphingolipids and an HSAN1-like phenotype; a p.Leu39del family member with sensory disease had an elevated alanine/serine ratio and L-serine deficiency. Thus diet and systemic amino-acid metabolism may modify biochemical phenotype, but clinical effect sizes remain unknown. (lone2022sptlc1variantsassociated pages 6-8, lone2022sptlc1variantsassociated pages 8-9, mohassel2024serinepalmitoyltransferase(spt)related pages 7-9)

No genetic or environmental protective factor has been validated. L-serine is **not protective in ALS27** and may be harmful.

## 3. Phenotypes

### Core phenotype and frequency

In a 2023 analysis of **17 SPTLC1-JALS cases**, mean onset was **7.9 ± 4.6 years**; all 17 had spinal onset, versus 62.8% among 43 FUS-JALS cases. Bulbar onset was 0%, although bulbar involvement can emerge later. Mean estimated disease duration was **512.0 months** (95% CI 416.7–607.3; approximately 42.7 years), versus 33.4 months for FUS-JALS. These estimates derive from a literature-assembled, small cohort and are susceptible to survival and publication bias. (wang2023clinicalfeaturedifference pages 5-6)

| Phenotype | Character/course | Suggested HPO term |
|---|---|---|
| Childhood onset | Usually insidious; reported from age 3–4 years, occasionally second/third decade | HP:0011463 Childhood onset; HP:0003581 Adult onset where applicable |
| Lower-limb spasticity/hyperreflexia | Often an early UMN manifestation; progressive | HP:0001257 Spasticity; HP:0001347 Hyperreflexia |
| Toe walking/abnormal gait | Common presenting manifestation before age 10 | HP:0040083 Toe walking; HP:0001288 Gait disturbance |
| Distal leg weakness and atrophy | Progressive LMN involvement; may spread to multiple myotomes | HP:0009053 Distal lower-limb muscle weakness; HP:0003202 Skeletal muscle atrophy |
| Diffuse denervation | Acute and chronic neurogenic changes on EMG | HP:0003457 EMG abnormality; HP:0003448 Decreased motor nerve conduction amplitude |
| Pes cavus/scoliosis | Secondary to longstanding asymmetric or distal weakness | HP:0001761 Pes cavus; HP:0002650 Scoliosis |
| Bulbar dysfunction | Not typical at onset; may occur in later disease | HP:0001283 Bulbar palsy; HP:0002015 Dysphagia; HP:0002167 Dysarthria |
| Respiratory dysfunction | Late complication in some patients | HP:0002878 Respiratory insufficiency |
| Sensory sparing | Normal sensory examination/NCS is characteristic | encode as absence of HP:0000763 Sensory neuropathy |
| Cognitive function | Usually preserved; not systematically tested | absence of HP:0100543 Cognitive impairment, with caution |

A newly reported de novo p.Ala20Thr patient developed lower-limb spasticity and weakness at age seven, followed by progressive spread over 12.3 years, severe distal weakness, scoliosis, and pes cavus, without sensory or cognitive impairment. (wang2023clinicalfeaturedifference pages 5-6)

### Quality-of-life impact

No ALS27-specific EQ-5D, SF-36, PROMIS, or caregiver-burden study was identified. Expected impacts include progressive loss of ambulation and self-care, orthopedic deformity, communication/swallowing difficulty, and eventual ventilatory dependence. These impacts should be recorded as clinically plausible consequences, not disease-specific quantified outcomes.

## 4. Genetic and molecular information

### Gene and variant spectrum

**SPTLC1** encodes the long-chain base subunit 1 of SPT. Reported ALS-associated variants include **p.Ala20Ser, p.Tyr23Phe, p.Leu38Arg, p.Leu39del, p.Phe40_Ser41del**, and exon-2 skipping caused by an Ala20-associated splice effect; **p.Ala20Thr** was reported in 2023. The 2023 compilation included 17 patients, many de novo and several familial p.Leu39del cases. (wang2023clinicalfeaturedifference pages 5-6, lone2022sptlc1variantsassociated pages 1-3, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)

These are missense, in-frame deletion, or splice-altering alleles—not a simple haploinsufficiency series. They are germline, not somatic. Population frequencies were not provided in the retrieved studies, but pathogenic de novo variants underlying such an ultra-rare dominant pediatric disorder are expected to be absent or extremely rare in reference populations; each variant nevertheless requires direct gnomAD and ClinVar review before clinical classification.

The functional consequence is best classified as **toxic/dysregulated gain of function**: mutant complexes retain or increase sphingolipid synthesis while escaping ORMDL feedback. Complete SPTLC1 loss would not be mechanistically equivalent. No large recurrent chromosomal abnormality has been established.

### Pleiotropy and genotype–phenotype distinction

C-terminal/cytoplasmic SPTLC1 variants, especially around Cys133 and Ser331, classically cause HSAN1 through altered substrate use and increased 1-deoxysphingolipids. Ser331 substitutions can produce mixed sensory/motor phenotypes and early cataracts. Therefore, “SPTLC1-related disorder” is broader than ALS27, and variant position plus lipid biochemistry are important for interpretation. (lone2022sptlc1variantsassociated pages 1-3, mohassel2024serinepalmitoyltransferase(spt)related pages 4-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)

No validated ALS27-specific modifier gene or epigenetic signature has been reported.

## 5. Environmental and lifestyle information

There is no evidence that toxins, radiation, pollution, infection, smoking, alcohol, or exercise initiate ALS27. Dietary amino-acid balance is a plausible biochemical modifier, but no preventive diet has been validated. The absence of evidence should not be interpreted as proof that systemic metabolism cannot influence severity. The p.Leu39del biochemical observations specifically motivate measurement of serine, alanine, and sphingolipids in atypical mixed motor-sensory cases. (lone2022sptlc1variantsassociated pages 6-8, mohassel2024serinepalmitoyltransferase(spt)related pages 7-9)

## 6. Mechanism and pathophysiology

### Upstream causal chain

1. **Heterozygous SPTLC1 variant** affects the N-terminal transmembrane/ORMDL-interaction region.
2. Mutant SPTLC1 is incorporated into the ER-resident SPT holoenzyme, although exon-2 deletion can impair ER integration and partially destabilize SPTLC2.
3. Binding or regulatory communication with **ORMDL1–3** is weakened.
4. Ceramide-dependent feedback inhibition fails.
5. SPT excessively condenses L-serine and palmitoyl-CoA, increasing de novo long-chain bases, ceramides, and complex canonical sphingolipids.
6. Lipid-membrane composition, organelle homeostasis, signaling, and axonal maintenance are presumed to become toxic to corticospinal and lower motor neurons.
7. Progressive motor-neuron/axon dysfunction produces spasticity, denervation, muscle atrophy, orthopedic deformity, and eventually bulbar/respiratory disease. Steps 1–5 are strongly supported; the precise molecular bridge from lipid excess to selective motor-neuron death remains unresolved. (lone2022sptlc1variantsassociated pages 6-8, lone2022sptlc1variantsassociated pages 1-3, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)

SPT occupies the **endoplasmic-reticulum membrane** and ER–mitochondrial contact sites. The complex includes SPTLC1/SPTLC2 catalytic components, SPTSSA/SPTSSB activating subunits, and ORMDL inhibitors. Relevant suggested terms include GO:0005783 endoplasmic reticulum; GO:0005789 ER membrane; GO:0006665 sphingolipid metabolic process; GO:0030148 sphingolipid biosynthetic process; GO:0046513 ceramide biosynthetic process; and GO:0045768 positive regulation of anti-apoptotic signaling only if demonstrated in future disease-specific work. (syeda2024recurrentdenovo pages 1-2, lone2022sptlc1variantsassociated pages 1-3)

### Lipidomics and molecular profiling

Patient serum, fibroblasts, and engineered cells show excessive canonical sphingolipid synthesis. Particularly informative species include sphingolipids bearing **C18:0, C20:0, and C22:0 acyl chains**, which are normally minor. In contrast, 1-deoxysphingolipids are generally not the dominant ALS27 signature. L-serine restriction can increase 1-deoxysphingolipids, demonstrating substrate-dependent biochemical plasticity. (lone2022sptlc1variantsassociated pages 6-8, lone2022sptlc1variantsassociated pages 12-14)

No robust disease-specific transcriptomic, proteomic, spatial-transcriptomic, single-cell, epigenomic, or metabolomic signature beyond targeted/untargeted sphingolipidomics has been validated. iPSC-derived lower-motor-neuron-like cells carrying p.Phe40_Ser41del showed increased canonical sphingolipids but, in the limited reported characterization, no clear differentiation, morphology, or survival defect. (mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)

**Cell Ontology suggestions:** CL:0000127 astrocyte, CL:0000129 microglial cell, CL:0000236 B cell should not be asserted as primary disease cells without direct evidence; the supported targets are motor neurons, especially CL:0000100 motor neuron and CL:0000104 lower motor neuron. Skeletal myofibers are downstream denervation targets.

## 7. Anatomical structures affected

Primary disease sites are the motor system: corticospinal upper motor neurons, anterior-horn/lower motor neurons, brainstem motor nuclei in later disease, motor roots/axons, neuromuscular junctions, and secondarily skeletal muscle. Suggested anatomy terms include UBERON:0002240 spinal cord; UBERON:0000955 brain; UBERON:0002298 brainstem; UBERON:0002439 myotome; UBERON:0001134 skeletal muscle tissue; and UBERON:0001021 nerve. ER and ER–mitochondrial contact regions are the principal subcellular sites. (lone2022sptlc1variantsassociated pages 1-3, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)

Onset is often bilateral lower-limb/spinal rather than bulbar. Individual asymmetry can occur, but consistent lateralization has not been established.

## 8. Temporal development

Onset is usually chronic and insidious in early childhood. An HSP-like phase—spastic gait or toe walking—may precede recognizable diffuse LMN disease. The course is relentlessly progressive rather than episodic or relapsing-remitting, but often much slower than FUS-JALS or adult ALS. Late stages may include bulbar and respiratory compromise. No spontaneous remission is documented. (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)

The optimal intervention window is unknown. Mechanistically, treatment before extensive denervation would be preferable, but no presymptomatic biomarker threshold or trial evidence defines such a window.

## 9. Inheritance and population

Inheritance is **autosomal dominant**, with many cases arising de novo and some transmitted through affected families. Recurrence risk for an affected heterozygous individual is theoretically 50% per pregnancy. For parents of an apparently de novo case, recurrence is low but not zero because parental germline mosaicism has not been excluded systematically.

No ALS27-specific incidence, prevalence, carrier frequency, sex ratio, founder effect, or geographic concentration is established. The 2023 compilation contained 6 males and 11 females, but **6:11 is not a reliable population sex ratio** because of the tiny, literature-ascertained sample. Cases have been reported in multiple ancestries and countries, arguing against restriction to one population. (wang2023clinicalfeaturedifference pages 5-6)

There is no evidence for anticipation. Expressivity is variable in onset, rate of progression, and late bulbar/respiratory involvement.

## 10. Diagnostics

### Clinical and electrophysiologic diagnosis

ALS27 should be considered in a child or young adult with progressive spastic paraparesis plus distal weakness/atrophy, diffuse denervation, and preserved sensation. EMG typically shows diffuse acute and chronic denervation across multiple myotomes; nerve-conduction studies show normal sensory responses and no primary demyelinating process. A sural-nerve biopsy in at least one patient showed sensory preservation, but biopsy is not routinely required. (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)

There is no ALS27-specific MRI pattern. MRI is mainly used to exclude structural brain/spinal-cord disease. Pulmonary function, swallowing assessment, nutrition, speech, and serial motor-functional measures are required for staging and management.

### Genetic testing strategy

1. Use a comprehensive juvenile motor-neuron disease/ALS/HSP panel that includes **SPTLC1**, or trio WES/WGS.
2. Trio analysis is particularly useful for demonstrating de novo status.
3. Inspect exon-level sequence and splice effects; routine filtering should retain in-frame deletions and splice-altering variants, not only missense/nonsense variants.
4. Confirm by an orthogonal method and test parents/relatives.
5. Interpret variants using phenotype, domain location, segregation, absence/rarity in population data, and functional/lipidomic evidence.

CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion assays do not directly diagnose ALS27, although broader testing may be needed when the phenotype is unresolved. WGS may detect intronic/splice or structural lesions missed by panels/WES.

### Biomarkers

Plasma/serum or fibroblast sphingolipidomics may demonstrate elevated canonical ceramides and unusual acyl-chain species and can support pathogenicity, but no certified cutoff, sensitivity, specificity, or regulatory-qualified assay exists. Neurofilament light may be useful in ALS generally, but it is not validated specifically in slowly progressive ALS27.

### Differential diagnosis

Major alternatives are hereditary spastic paraplegia, FUS-JALS, ALS2-related disease, SETX-associated ALS4, SPG11, SIGMAR1 disease, spinal muscular atrophy, distal hereditary motor neuropathy, primary lateral sclerosis, structural myelopathy, leukodystrophy, and metabolic motor-neuron disorders. ALS27 is favored over pure HSP by widespread LMN denervation; over HSAN1 by sensory sparing and canonical rather than deoxy-sphingolipid excess. (wang2023clinicalfeaturedifference pages 5-6, lone2022sptlc1variantsassociated pages 1-3, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)

Cascade testing is appropriate after a familial variant is identified. Population or newborn screening is not currently recommended.

## 11. Outcome and prognosis

ALS27 is severely disabling but often slower than other ALS forms. Long survival into the fifth or sixth decade has been reported, and cognition may remain preserved; nevertheless, progression is described as universal and relentless, and bulbar/respiratory failure can occur. Disease-specific 5- or 10-year survival, mortality rates, median life expectancy, validated prognostic scores, and treatment-adjusted outcomes are unavailable. (wang2023clinicalfeaturedifference pages 5-6, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)

Important morbidity includes gait loss, contractures, scoliosis, pes cavus, weakness, communication/swallowing impairment, malnutrition, secretion problems, and respiratory insufficiency. Recovery of lost motor neurons is not expected with current care.

## 12. Treatment and current implementation

### Disease-specific therapy

No approved SPTLC1-targeted treatment and no relevant disease-specific interventional trial were identified. Proposed approaches remain experimental:

- **Partial SPT inhibition:** mechanistically rational, but systemic SPT is essential. Myriocin and L-/D-cycloserine inhibit SPT; toxicity, off-target effects, dosing, and CNS delivery prevent clinical recommendation. D-cycloserine is approved for tuberculosis, not ALS27. (mohassel2024serinepalmitoyltransferase(spt)related pages 7-9)
- **RNA-directed reduction of mutant SPTLC1:** allele-selective ASO/siRNA strategies are conceptually attractive for a dominant gain-of-function disorder but lack ALS27 clinical evidence.
- **Substrate manipulation:** serine depletion has theoretical risks, and no safe therapeutic regimen is established.
- **Critical contraindication/caution:** avoid L-serine supplementation outside specialist research oversight. Serine enhanced consequences of SPT overactivity in p.Phe40_Ser41del iPSC-derived motor neurons and is predicted to worsen canonical sphingolipid overproduction. (mohassel2024serinepalmitoyltransferase(spt)related pages 7-9)

Suggested NCIt concepts include Antisense Oligonucleotide Therapy, Gene Silencing Therapy, Physical Therapy, Occupational Therapy, Speech Therapy, Noninvasive Ventilation, Gastrostomy, and Palliative Care; precise NCIt identifiers should be resolved against the current NCIt release.

### Supportive real-world management

Until targeted therapy exists, management should follow a multidisciplinary pediatric/young-adult motor-neuron-disease pathway: physical and occupational therapy, stretching and contracture prevention, orthoses and mobility aids, scoliosis surveillance, spasticity treatment, speech/augmentative communication, swallowing and nutritional monitoring, cough augmentation, noninvasive ventilation when indicated, secretion management, psychosocial support, and advance-care planning. Riluzole and edaravone have not been studied specifically in ALS27; use is an individualized specialist decision rather than evidence-based genotype-specific therapy.

## 13. Prevention

Primary prevention through lifestyle modification or vaccination is not applicable. Secondary prevention consists of identifying at-risk relatives and recognizing early motor signs. Tertiary prevention aims to limit contractures, falls, malnutrition, aspiration, respiratory complications, and communication loss.

Genetic counseling should cover dominant transmission, frequent de novo occurrence, parental testing, possible germline mosaicism, cascade testing, and reproductive options—including prenatal diagnosis and preimplantation genetic testing when a familial pathogenic variant is known. There is no population screening program or prophylactic medication.

## 14. Other species and natural disease

No naturally occurring veterinary analogue of SPTLC1-ALS27, breed predisposition, zoonotic transmission, or cross-species infectious susceptibility was identified. Orthologous Sptlc1 genes are widely conserved in vertebrates, reflecting the essential role of sphingolipid synthesis. This is a noncommunicable genetic disease with no zoonotic potential.

## 15. Models and research resources

**Disease-specific cellular models:** COS-7 and HEK293/SPTLC1-knockout complementation systems, patient fibroblasts, serum lipidomics, and p.Phe40_Ser41del iPSC-derived lower-motor-neuron-like cells. These reproduce impaired ORMDL regulation and lipid excess but have not yet robustly reproduced progressive motor-neuron death. (lone2022sptlc1variantsassociated pages 12-14, lone2022sptlc1variantsassociated pages 1-3, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)

**Animal evidence:** as of the 2024 review, no published mouse carrying an ALS27-specific SPTLC1 allele had been established; knock-in models were under development. Indirect models support the pathway: loss of two Ormdl isoforms causes neurodegeneration, and conditional expression of constitutively active fusion-SPT causes high sphingolipids, progressive hindlimb paralysis, and sciatic-nerve pathology. The spontaneous Sptssb “stellar” mouse develops early ataxia and premature death, but none is a faithful ALS27 model. (mohassel2024serinepalmitoyltransferase(spt)related pages 7-9, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)

Relevant resources include MGI/IMSR for future mouse alleles, ZFIN for zebrafish, FlyBase for Drosophila SPT-pathway models, Cellosaurus for cell lines, and GEO/SRA for future transcriptomic datasets.

## Expert interpretation and principal knowledge gaps

The strongest current interpretation is that ALS27 is a **metabolic motor-neuron disease caused by dysregulated sphingolipid flux**, not merely another protein-aggregation ALS. The convergence of SPTLC1 and SPTLC2 juvenile ALS supports causality, while the contrast with HSAN1 demonstrates that the *type* of lipid produced—not simply increased SPT activity—helps determine neuronal selectivity. Nevertheless, why canonical sphingolipid excess preferentially injures motor neurons remains unanswered. (syeda2024recurrentdenovo pages 1-2, mohassel2024serinepalmitoyltransferase(spt)related pages 6-7)

Priority gaps are: prospective natural-history cohorts; penetrance and prevalence estimates; standardized plasma/CSF lipid biomarkers; motor-neuron-specific lipidomics and single-cell studies; faithful knock-in animal models; allele-selective silencing; and safe, partial, nervous-system-targeted SPT inhibition. Epidemiology, formal quality-of-life statistics, validated prognostic biomarkers, and controlled treatment-response rates should be entered in a knowledge base as **not established**, rather than extrapolated from common adult ALS.

References

1. (wang2023clinicalfeaturedifference pages 5-6): Pei-Shan Wang, Qiao Wei, Hongfu Li, and Zhi-Ying Wu. Clinical feature difference between juvenile amyotrophic lateral sclerosis with sptlc1 and fus mutations. Chinese Medical Journal, Feb 2023. URL: https://doi.org/10.1097/cm9.0000000000002495, doi:10.1097/cm9.0000000000002495. This article has 4 citations and is from a peer-reviewed journal.

2. (lone2022sptlc1variantsassociated pages 1-3): Museer A. Lone, Mari J. Aaltonen, Aliza Zidell, Helio F. Pedro, Jonas Alex Morales Saute, Shalett Mathew, Payam Mohassel, Carsten Bonnemann, Eric A. Shoubridge, and Thorsten Hornemann. Sptlc1 variants associated with childhood onset amyotrophic lateral sclerosis produce distinct sphingolipid signatures through impaired interaction with ormdl proteins. BioRxiv, Apr 2022. URL: https://doi.org/10.1101/2022.04.29.490031, doi:10.1101/2022.04.29.490031. This article has 0 citations.

3. (mohassel2024serinepalmitoyltransferase(spt)related pages 6-7): Payam Mohassel, Meher Abdullah, Florian S. Eichler, and Teresa M. Dunn. Serine palmitoyltransferase (spt)-related neurodegenerative and neurodevelopmental disorders. Journal of Neuromuscular Diseases, 11:735-747, May 2024. URL: https://doi.org/10.3233/jnd-240014, doi:10.3233/jnd-240014. This article has 10 citations and is from a peer-reviewed journal.

4. (mohassel2024serinepalmitoyltransferase(spt)related pages 7-9): Payam Mohassel, Meher Abdullah, Florian S. Eichler, and Teresa M. Dunn. Serine palmitoyltransferase (spt)-related neurodegenerative and neurodevelopmental disorders. Journal of Neuromuscular Diseases, 11:735-747, May 2024. URL: https://doi.org/10.3233/jnd-240014, doi:10.3233/jnd-240014. This article has 10 citations and is from a peer-reviewed journal.

5. (OpenTargets Search: Amyotrophic lateral sclerosis 27, juvenile-SPTLC1): Open Targets Query (Amyotrophic lateral sclerosis 27, juvenile-SPTLC1, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (mohassel2024serinepalmitoyltransferase(spt)related pages 4-6): Payam Mohassel, Meher Abdullah, Florian S. Eichler, and Teresa M. Dunn. Serine palmitoyltransferase (spt)-related neurodegenerative and neurodevelopmental disorders. Journal of Neuromuscular Diseases, 11:735-747, May 2024. URL: https://doi.org/10.3233/jnd-240014, doi:10.3233/jnd-240014. This article has 10 citations and is from a peer-reviewed journal.

7. (lone2022sptlc1variantsassociated pages 6-8): Museer A. Lone, Mari J. Aaltonen, Aliza Zidell, Helio F. Pedro, Jonas Alex Morales Saute, Shalett Mathew, Payam Mohassel, Carsten Bonnemann, Eric A. Shoubridge, and Thorsten Hornemann. Sptlc1 variants associated with childhood onset amyotrophic lateral sclerosis produce distinct sphingolipid signatures through impaired interaction with ormdl proteins. BioRxiv, Apr 2022. URL: https://doi.org/10.1101/2022.04.29.490031, doi:10.1101/2022.04.29.490031. This article has 0 citations.

8. (syeda2024recurrentdenovo pages 1-2): Safoora B Syeda, Museer A Lone, Payam Mohassel, Sandra Donkervoort, Pinki Munot, Marcondes C França, Juan Eli Galarza-Brito, Matthias Eckenweiler, Alexander Asamoah, Kenneth Gable, Anirban Majumdar, Anke Schumann, Sita D Gupta, Arpita Lakhotia, Perry B Shieh, A Reghan Foley, Kelly E Jackson, Katherine R Chao, Thomas L Winder, Francesco Catapano, Lucy Feng, Janbernd Kirschner, Francesco Muntoni, Teresa M Dunn, Thorsten Hornemann, and Carsten G Bönnemann. Recurrent de novo sptlc2 variant causes childhood-onset amyotrophic lateral sclerosis (als) by excess sphingolipid synthesis. Journal of Neurology, Neurosurgery, and Psychiatry, 95:103-113, Nov 2024. URL: https://doi.org/10.1136/jnnp-2023-332132, doi:10.1136/jnnp-2023-332132. This article has 23 citations.

9. (lone2022sptlc1variantsassociated pages 8-9): Museer A. Lone, Mari J. Aaltonen, Aliza Zidell, Helio F. Pedro, Jonas Alex Morales Saute, Shalett Mathew, Payam Mohassel, Carsten Bonnemann, Eric A. Shoubridge, and Thorsten Hornemann. Sptlc1 variants associated with childhood onset amyotrophic lateral sclerosis produce distinct sphingolipid signatures through impaired interaction with ormdl proteins. BioRxiv, Apr 2022. URL: https://doi.org/10.1101/2022.04.29.490031, doi:10.1101/2022.04.29.490031. This article has 0 citations.

10. (lone2022sptlc1variantsassociated pages 12-14): Museer A. Lone, Mari J. Aaltonen, Aliza Zidell, Helio F. Pedro, Jonas Alex Morales Saute, Shalett Mathew, Payam Mohassel, Carsten Bonnemann, Eric A. Shoubridge, and Thorsten Hornemann. Sptlc1 variants associated with childhood onset amyotrophic lateral sclerosis produce distinct sphingolipid signatures through impaired interaction with ormdl proteins. BioRxiv, Apr 2022. URL: https://doi.org/10.1101/2022.04.29.490031, doi:10.1101/2022.04.29.490031. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Amyotrophic_Lateral_Sclerosis_27_Juvenile-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 5 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.3233/JND-240014—current` (2 mentions) - Identifier did not resolve to a record