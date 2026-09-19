---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T17:30:03.779592'
end_time: '2026-07-31T17:41:38.076424'
duration_seconds: 694.3
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Craniofacial Microsomia
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Craniofacial_Microsomia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Craniofacial Microsomia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Craniofacial Microsomia** covering all of the
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
- **Disease Name:** Craniofacial Microsomia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Craniofacial Microsomia** covering all of the
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


# Craniofacial Microsomia: Disease-Characteristics Research Report

**Scope and evidence note.** Craniofacial microsomia (CFM) is heterogeneous, terminology is inconsistent, and many clinical recommendations rest on retrospective cohorts rather than randomized trials. This report prioritizes 2023–2024 evidence where retrievable and uses older landmark studies when they remain the best quantitative evidence. “Causal” genes are separated from susceptibility or candidate genes. PMID links are given where verified from the retrieved evidence; DOI links are supplied otherwise.

## Executive summary

CFM is a congenital developmental spectrum involving hypoplasia of first- and second-pharyngeal-arch derivatives, especially the mandible, ear, facial soft tissue, facial nerve, and orbit. It is usually unilateral, but bilateral and extracraniofacial disease are important. In a 991-person multicenter cohort, 83% were unilateral, 12% bilateral, and 47% had at least one extracraniofacial anomaly; vertebral (28%) and circulatory (21%) anomalies were most frequent. Bilateral disease carried greater extracraniofacial burden (68% versus 44%). (renkema2019extracraniofacialanomaliesin pages 1-2)

The strongest recent molecular advance is the April 2023 demonstration that pathogenic **FOXI3** variants account for a small molecularly defined subset: 18 likely pathogenic variants occurred in 21 of 670 probands (3.1%). Human segregation, transcription/localization assays, and knock-in mice support causality. **SF3B2** haploinsufficiency is another established cause, while **CHAF1A**, **MYT1**, and several other genes have emerging or phenotype-overlap evidence. Most CFM remains unexplained and is best considered multifactorial, with genetic susceptibility, incomplete penetrance, modifiers, and prenatal environmental/vascular influences. (OpenTargets Search: craniofacial microsomia, mao2023foxi3pathogenicvariants pages 1-2, mao2023foxi3pathogenicvariants pages 5-6)

There is no disease-modifying drug. Current implementation is multidisciplinary and phenotype-directed: hearing and airway care, feeding and speech therapy, dental/orthodontic management, mandibular reconstruction or distraction, orthognathic surgery, ear reconstruction, facial reanimation, and soft-tissue augmentation. Evidence for timing and comparative superiority remains limited.

The following table provides a compact knowledge-base view.

| Domain | Key annotations | Suggested ontology terms | Evidence |
|---|---|---|---|
| Identity / identifiers | **Craniofacial microsomia (CFM)** is a **congenital** disorder/spectrum characterized by unilateral or bilateral underdevelopment of structures derived largely from the **first and second pharyngeal arches**; commonly overlaps conceptually with **hemifacial microsomia**, **oculoauriculovertebral spectrum (OAVS)**, and sometimes **Goldenhar spectrum** in clinical literature. Disease-level information here is derived primarily from **aggregated cohort studies, disease resources, and research cohorts**, not EHR-only sources. **MONDO:** MONDO:0015397 (craniofacial microsomia). | MONDO:0015397; UBERON: pharyngeal arch; UBERON: mandible; UBERON: external ear | (renkema2019extracraniofacialanomaliesin pages 1-2, NCT02639312 chunk 1) |
| Core phenotype | Typical manifestations include **facial asymmetry**, **mandibular hypoplasia**, **microtia/ear dysplasia**, **preauricular tags/pits**, and related first/second arch anomalies; laterality is usually **unilateral** but may be bilateral. In a 991-patient cohort: **83% unilateral**, **12% bilateral**; in the same cohort, **53% male / 47% female**. Clinical severity is commonly described with **OMENS / OMENS+** and mandibular grading with **Pruzansky-Kaban**. | HPO: Facial asymmetry; HPO: Microtia; HPO: Mandibular hypoplasia; HPO: Preauricular tag; HPO: Hearing impairment; UBERON: mandible; UBERON: pinna; NCIT: Diagnostic Procedure | (renkema2019extracraniofacialanomaliesin pages 1-2, mao2023foxi3pathogenicvariants pages 9-10) |
| Extracraniofacial systems with frequencies | Large retrospective multicenter cohort (**n=991**) found extracraniofacial anomalies in **47%** overall. By system: **vertebral 28%**, **circulatory 21%**, **CNS 11%**, **urogenital 11%**, **gastrointestinal 9%**, **respiratory 3%**. Bilateral CFM had higher extracraniofacial anomaly prevalence (**68%**) than unilateral (**44%**). | HPO: Vertebral anomaly; HPO: Congenital heart defect; HPO: Central nervous system abnormality; HPO: Genitourinary abnormality; HPO: Gastrointestinal malformation; HPO: Respiratory system abnormality; UBERON: vertebral column; UBERON: heart; UBERON: kidney; UBERON: brain | (renkema2019extracraniofacialanomaliesin pages 7-8, renkema2019extracraniofacialanomaliesin pages 1-2) |
| Causal genes / susceptibility genes | **Higher-confidence causal gene evidence:** **FOXI3** (Nature Communications 2023; likely pathogenic variants in **21/670 probands = 3.1%**; variant classes included **14 missense, 2 in-frame deletions, 1 frameshift, 1 truncating** across 18 distinct variants; evidence from human genetics + in vitro assays + knock-in mice). **SF3B2** is strongly associated in disease-target resources and prior human genetic literature. **Emerging / candidate genes:** **CHAF1A** (resource-level association), **MYT1**, **EYA3**, **EFTUD2**, **VWA1**, and family-based candidates including **SIX1, PDGFRA, KDR/VEGFR2**. **Susceptibility loci / candidate genes from GWAS:** **ROBO1, GATA3, GBX2, FGF3, NRP2, EDNRB, SHROOM3, SEMA7A, ARID3B, KLF12, EPAS1, PLCD3**. | GO: DNA-binding transcription factor activity; GO: RNA splicing; GO: neural crest cell migration; CL: cranial neural crest cell | (OpenTargets Search: craniofacial microsomia, petrin2026familialoculoauriculovertebralspectrum pages 11-13, petrin2026familialoculoauriculovertebralspectrum pages 1-3, mao2023foxi3pathogenicvariants pages 6-7, mao2023foxi3pathogenicvariants pages 1-2, mao2023foxi3pathogenicvariants pages 4-5, mao2023foxi3pathogenicvariants pages 5-6, zhang2016genomewideassociationstudy pages 4-5, zhang2016genomewideassociationstudy pages 7-8, zhang2016genomewideassociationstudy pages 3-3) |
| Inheritance / penetrance | Most CFM is **sporadic**, but familial forms occur. For **FOXI3**, inheritance can be **autosomal dominant with reduced penetrance** and/or **autosomal recessive**. Reduced penetrance is supported by transmission from apparently unaffected parents and a proposed **modifier haplotype / gene-dosage** model. Family-based OAVS/CFM studies further support **incomplete penetrance** and **variable expressivity**. | HPO: Reduced penetrance; HPO: Variable expressivity | (petrin2026familialoculoauriculovertebralspectrum pages 1-3, mao2023foxi3pathogenicvariants pages 1-2, mao2023foxi3pathogenicvariants pages 7-8, mao2023foxi3pathogenicvariants pages 8-9, petrin2026familialoculoauriculovertebralspectrum pages 10-11, petrin2026familialoculoauriculovertebralspectrum pages 15-19) |
| Developmental mechanism / pathophysiology | Best-supported model is **disturbed development of first/second pharyngeal arch derivatives during the first ~6 weeks of embryogenesis**, involving **cranial neural crest cell migration/differentiation** and likely **vascular patterning / mandibular growth** defects. GWAS candidates are enriched for **embryonic development, organ/system development, and cell migration** pathways. **FOXI3** variants reduce transcriptional activity; NLS variants impair **nuclear entry**, forkhead-domain variants can cause **intranuclear aggregation**. | GO: Neural crest cell migration; GO: embryonic craniofacial morphogenesis; GO: regulation of transcription by RNA polymerase II; GO: angiogenesis; CL: cranial neural crest cell; UBERON: Meckel cartilage; UBERON: pharyngeal arch | (mao2023foxi3pathogenicvariants pages 6-7, mao2023foxi3pathogenicvariants pages 5-6, renkema2019extracraniofacialanomaliesin pages 1-2, zhang2016genomewideassociationstudy pages 4-5, zhang2016genomewideassociationstudy pages 3-3, petrin2026familialoculoauriculovertebralspectrum pages 10-11) |
| Model-organism evidence | **Knock-in mouse models** of **Foxi3** support causality. Homozygotes showed severe craniofacial phenotypes including **underdeveloped mandible**, **microtia/absent external ear**, **asymmetric skull**, **cleft palate in ~50%**, absent ear bones, and **syngnathia**; heterozygotes showed milder or variable abnormalities. This provides strong experimental recapitulation of human disease mechanisms. | CL: cranial neural crest cell; GO: animal organ morphogenesis; UBERON: mandible; UBERON: palate; HPO analog terms for human mapping: cleft palate, microtia, mandibular hypoplasia | (mao2023foxi3pathogenicvariants pages 6-7, mao2023foxi3pathogenicvariants pages 7-8, mao2023foxi3pathogenicvariants pages 9-10, mao2023foxi3pathogenicvariants pages 12-13) |
| Diagnostics | Diagnosis is primarily **clinical + imaging-based**, using **OMENS/OMENS+** and **Pruzansky-Kaban** classification. Recommended workup includes **physical examination** plus targeted screening for extracraniofacial anomalies: **electrocardiography/echocardiography**, **renal ultrasound**, **spinal radiographs**, and **brain/spine MRI when indicated**. Research and specialty-center phenotyping increasingly use **3D imaging / cone-beam CT** and genomic sequencing. | NCIT: Magnetic Resonance Imaging; NCIT: Echocardiography; NCIT: Ultrasonography; NCIT: Computed Tomography; NCIT: Genetic Testing; UBERON: kidney; UBERON: vertebral column; UBERON: brain | (renkema2019extracraniofacialanomaliesin pages 7-8, renkema2019extracraniofacialanomaliesin pages 1-2, NCT02639312 chunk 1, NCT03270618 chunk 1) |
| Management / real-world implementation | Current care is **multidisciplinary** and predominantly **surgical/reconstructive** plus hearing, speech, dental/orthodontic, and psychosocial support. Active real-world/research implementations include **mandibular distraction osteogenesis** with **CAD/CAM or computer-guided templates**, **fat grafting** with or without **adipose-derived regenerative cells (ADRC)** for soft-tissue augmentation, and regenerative adjuncts such as **bone marrow aspirate concentrate**. Observational registries/natural-history cohorts are also major current applications. | NCIT: Mandibular Distraction Osteogenesis; NCIT: Fat Grafting; NCIT: Reconstructive Surgical Procedure; NCIT: Orthodontic Procedure; NCIT: Speech Therapy; NCIT: Psychosocial Intervention | (NCT01674439 chunk 1, NCT03270618 chunk 1, NCT03869021 chunk 2, NCT03806361 chunk 1, NCT03861650 chunk 2, NCT00340964 chunk 1) |
| Epidemiology | Frequently cited birth prevalence estimate is approximately **1 in 7,500 live births** (from NIH natural-history protocol context). Sex distribution in a large cohort was **53% male / 47% female**. Disease burden spans childhood into adulthood because facial growth, occlusion, hearing, airway, and reconstructive needs evolve over time. | HPO: Congenital onset; HPO: Facial asymmetry | (renkema2019extracraniofacialanomaliesin pages 1-2, NCT02639312 chunk 1) |
| Environmental / prenatal risk factors | Evidence supports **multifactorial etiology**. Environmental factors mentioned in human studies/reviews include **maternal obesity**, **periconceptional folic acid use**, and **vasoactive exposures during pregnancy** as studied/implicated risk modifiers, but effect sizes and causal certainty remain less robust than for the strongest recent genetic evidence. | CHEBI term suggestions if curating exposures: folic acid; vasoactive agents | (zhang2016genomewideassociationstudy pages 7-8) |
| Evidence gaps / unavailable or limited data | No validated **disease-specific blood/urine biomarkers** were identified in retrieved evidence. No established **pharmacotherapy**, **gene therapy**, or routine **omics-based diagnostic biomarker** is in clinical use. Protective genetic/environmental factors are poorly defined. Population-specific prevalence, mortality, life expectancy, penetrance estimates for most genes, and standardized treatment-response rates remain limited. Some recent 2023–2024 surveys/reviews were not fully retrievable in this session, so large parts of current practice still rely on older cohort data plus ongoing trials/registries. | NCIT: Biomarker; NCIT: Gene Therapy; NCIT: Clinical Trial | (OpenTargets Search: craniofacial microsomia, NCT01674439 chunk 1, NCT02639312 chunk 1) |


*Table: This table condenses the main knowledge-base annotations for craniofacial microsomia, covering identity, phenotype, genetics, mechanisms, diagnostics, management, and gaps. It is useful as a compact structured summary for ontology mapping and evidence-backed curation.*

## 1. Disease information

### Definition and terminology

CFM is **congenital unilateral or bilateral underdevelopment of facial structures derived predominantly from the first and second pharyngeal arches**. Its minimum diagnostic phenotype is debated; ear anomalies, mandibular hypoplasia, facial asymmetry, epibulbar dermoid, and facial tags are variably included. (renkema2019extracraniofacialanomaliesin pages 1-2)

Common names include **hemifacial microsomia**, **oculo-auriculo-vertebral spectrum (OAVS)**, **oculoauriculovertebral dysplasia**, **first-and-second branchial-arch syndrome**, and, less precisely, **Goldenhar syndrome/spectrum**. “Goldenhar” is often reserved for CFM/OAVS with ocular dermoids and vertebral anomalies. These terms overlap but should not automatically be treated as exact synonyms in computational curation.

### Identifiers

- **MONDO:** **MONDO:0015397**, craniofacial microsomia. A narrower genetic entry, “craniofacial microsomia 2,” is represented as MONDO:0958194 in Open Targets. (OpenTargets Search: craniofacial microsomia)
- **MeSH:** the literature is commonly indexed under *Facial Hemiatrophy*, *Goldenhar Syndrome*, *Microtia*, or related craniofacial-abnormality headings; no single MeSH term perfectly captures the modern CFM spectrum.
- **ICD-10-CM:** no unique, validated CFM code. Coding generally uses Q67.4 (other congenital deformities of skull, face and jaw), Q87.0 (congenital malformation syndromes predominantly affecting facial appearance), and component-specific codes such as microtia or mandibular hypoplasia. Administrative-code case ascertainment can therefore misclassify disease.
- **ICD-11:** component abnormalities or broader congenital craniofacial-malformation categories are generally used; a dedicated universally adopted CFM code was not established in the retrieved evidence.
- **OMIM/Orphanet:** CFM is genetically heterogeneous rather than one uniformly mapped Mendelian entity; gene-defined forms and OAVS-related entries should be curated separately. Exact resource identifiers should be verified against the live databases before production ingestion.

The evidence summarized here is **aggregated disease-level evidence** from cohorts, trials, genetic studies, and curated resources—not individual EHR data.

## 2. Etiology and risk factors

### Causal model

CFM is a **developmental field defect with heterogeneous causes**. The likely vulnerable interval is approximately the first six weeks of embryogenesis, when cranial neural-crest cells migrate into the pharyngeal arches and interact with mesoderm, ectoderm, endoderm, and developing vasculature. Disruption can impair mandibular, auricular, facial-muscle, nerve, and soft-tissue development. (renkema2019extracraniofacialanomaliesin pages 1-2, zhang2016genomewideassociationstudy pages 4-5)

### Genetic factors

Higher-confidence causes include **FOXI3** pathogenic variants and **SF3B2** haploinsufficiency. Open Targets associates CFM with SF3B2, FOXI3, and CHAF1A, but database association alone does not establish equal causal certainty. (OpenTargets Search: craniofacial microsomia)

A GWAS of 939 cases and 2,012 controls implicated 13 regions/candidate genes—including **ROBO1, GATA3, EPAS1, PARD3B, GBX2, SHROOM3, FGF3, KLF12, EDNRB, SEMA7A, PLCD3**, and others—enriched in embryonic-development and neural-crest migration processes. These are susceptibility findings, not individually diagnostic Mendelian causes. (zhang2016genomewideassociationstudy pages 4-5, zhang2016genomewideassociationstudy pages 3-3)

Other reported or emerging genes include **MYT1, EYA3, EFTUD2, VWA1, ZYG11B**, and family-based candidates **SIX1, PDGFRA**, and **KDR/VEGFR2**. Digenic EYA3–EFTUD2 and multilocus models have been proposed, but replication and penetrance estimates remain inadequate. (petrin2026familialoculoauriculovertebralspectrum pages 11-13, petrin2026familialoculoauriculovertebralspectrum pages 10-11, petrin2026familialoculoauriculovertebralspectrum pages 15-19)

### Environmental and maternal factors

Reported associations include maternal diabetes/obesity, multiple gestation, assisted reproduction, vasoactive medications or vascular-disrupting exposures, smoking, and altered periconceptional folate exposure. The retrieved GWAS discussion specifically notes maternal obesity, periconceptional folic-acid use, and vasoactive exposures. These associations should be treated as **risk modifiers**, not proven deterministic causes; confounding and exposure heterogeneity are substantial. (zhang2016genomewideassociationstudy pages 7-8)

No infectious agent is established as a specific cause. Alcohol, retinoids, thalidomide, and other teratogens can produce overlapping first/second-arch phenotypes but should not be equated with idiopathic CFM without exposure evidence.

### Protective factors and gene–environment interaction

No validated protective allele or intervention specifically prevents CFM. Standard preconception folate, diabetes control, smoking/alcohol avoidance, medication review, and avoidance of known teratogens are prudent general congenital-anomaly prevention measures, but CFM-specific risk reduction has not been quantified. FOXI3 provides a plausible gene-modifier model: a common allele/haplotype in trans may reduce expression of the normal allele, increasing phenotypic expression of a rare pathogenic allele. Environmental or epigenetic effects could further alter this dosage-sensitive developmental system, but direct human G×E estimates are unavailable. (mao2023foxi3pathogenicvariants pages 1-2, mao2023foxi3pathogenicvariants pages 7-8, mao2023foxi3pathogenicvariants pages 8-9)

## 3. Phenotypes

CFM is present at birth, although asymmetry may become more conspicuous with growth. Severity and combinations vary markedly.

- **Mandibular/craniofacial hypoplasia:** mandibular ramus/condyle deficiency, micrognathia, chin deviation, malocclusion, maxillary cant, and facial asymmetry. Usually chronic; growth can magnify asymmetry. Suggested HPO: *Mandibular hypoplasia*, *Micrognathia* (HP:0000347), *Facial asymmetry* (HP:0000324), *Malocclusion*.
- **Ear and hearing:** microtia/anotia, external auditory canal atresia/stenosis, preauricular tags/pits, ossicular abnormalities, and usually conductive hearing loss; sensorineural or mixed loss may occur. Suggested HPO: *Microtia* (HP:0008551), *Preauricular skin tag* (HP:0000384), *External auditory canal atresia*, *Conductive hearing impairment* (HP:0000405).
- **Soft tissue/muscle:** unilateral facial soft-tissue deficiency and masticatory-muscle hypoplasia; stable defect but relative asymmetry may evolve. Suggested HPO: *Hemifacial hypoplasia*, *Abnormality of facial soft tissue*.
- **Facial nerve:** partial facial weakness involving one or more branches, affecting expression, eye closure, oral competence, and speech. Suggested HPO: *Facial palsy* (HP:0010628).
- **Orbit/eye:** orbital size or position asymmetry, epibulbar dermoid/lipodermoid, upper-eyelid coloboma, and ocular motility/vision problems. Suggested HPO: *Epibulbar dermoid*, *Orbital asymmetry*, *Coloboma of eyelid*.
- **Oral clefts/macrostomia:** lateral facial cleft/macrostomia and cleft lip/palate occur in subsets. Suggested HPO: *Macrostomia* (HP:0000182), *Cleft palate* (HP:0000175).
- **Airway, feeding, and sleep:** neonatal airway obstruction is possible in severe micrognathia or bilateral disease; dysphagia, prolonged feeding, aspiration risk, and obstructive sleep apnea may occur.
- **Speech/language and neurodevelopment:** hearing loss, facial/oral structural differences, and treatment burden can affect articulation and language. Population-level neurodevelopment is variable rather than uniformly impaired.
- **Psychosocial:** visible difference, repeated operations, stigma, teasing, and communication impairment may affect self-esteem, social participation, and family stress. The Positive Exposure pilot explicitly measured self-esteem, perceived stigma, and hope, but with only 44 participants and no power for efficacy conclusions. (NCT00340964 chunk 1)

### Extracraniofacial phenotype frequencies

Among 991 patients, 47% had extracraniofacial anomalies: vertebral 28%, circulatory 21%, CNS 11%, urogenital 11%, gastrointestinal 9%, and respiratory 3%. Bilateral disease and more severe mandibular, facial-nerve, or soft-tissue scores predicted greater systemic burden. (renkema2019extracraniofacialanomaliesin pages 7-8, renkema2019extracraniofacialanomaliesin pages 1-2)

Quality-of-life effects are phenotype-dependent: hearing and speech affect education and communication; mandibular/occlusal disease affects chewing and appearance; airway disease affects sleep and safety; facial weakness and ocular disease affect function; and visible difference affects psychosocial participation. Validated CFM-specific minimal clinically important differences remain limited.

## 4. Genetic and molecular information

### FOXI3

The landmark April 2023 Nature Communications study examined 670 unrelated CFM pedigrees/probands of European and Chinese ancestry and found 18 likely pathogenic **FOXI3** variants in 21 probands (**3.1%**; 5/124, 4.0%, in the European subset). Variant classes were 14 missense, two in-frame deletions, one frameshift, and one truncating variant. (mao2023foxi3pathogenicvariants pages 1-2, mao2023foxi3pathogenicvariants pages 4-5)

The abstract states: **“We identify 18 likely pathogenic variants in 21 probands (3.1%) in FOXI3.”** It further concludes that the findings indicate **“autosomal dominant inheritance with reduced penetrance, and/or autosomal recessive inheritance.”** [Mao et al., published April 2023; DOI: https://doi.org/10.1038/s41467-023-37703-6; PMID: https://pubmed.ncbi.nlm.nih.gov/37041148/] (mao2023foxi3pathogenicvariants pages 1-2)

All tested variants reduced transcriptional activation. Nuclear-localization-signal variants impaired nuclear entry; forkhead-domain variants caused abnormal intranuclear aggregation; other variants had less obvious localization effects. ClinVar submissions include SCV003803092–SCV003803100 and SCV003806728–SCV003806732. (mao2023foxi3pathogenicvariants pages 5-6, mao2023foxi3pathogenicvariants pages 12-13)

### SF3B2 and other genes

**SF3B2** haploinsufficiency is supported as a Mendelian cause of CFM/OAVS-like disease (PMID: https://pubmed.ncbi.nlm.nih.gov/34344887/). Its likely mechanism is loss of function affecting spliceosome function and neural-crest development. Open Targets ranks SF3B2, FOXI3, and CHAF1A as associated targets, but CHAF1A evidence is currently less mature for routine CFM interpretation. (OpenTargets Search: craniofacial microsomia, petrin2026familialoculoauriculovertebralspectrum pages 11-13)

Reported chromosomal abnormalities include heterogeneous deletions/duplications—among them 1p36 and 1p32–p34 regions—but no single recurrent copy-number change explains most CFM. (petrin2026familialoculoauriculovertebralspectrum pages 11-13)

### Variant interpretation

- Most causal findings are **germline**, not somatic.
- Expected pathogenic mechanisms include FOXI3 transcription-factor loss/dysfunction and SF3B2 haploinsufficiency.
- Population frequency should be checked variant-by-variant in current gnomAD; a universal CFM allele frequency is not meaningful.
- Reduced penetrance means an inherited variant from an unaffected parent is not automatically benign.
- Most panel/WES findings in candidate genes remain VUS unless segregation, phenotype, population frequency, and functional evidence satisfy ACMG/AMP criteria.

No validated epigenetic signature, disease-specific methylation episignature, proteomic biomarker, metabolomic signature, or modifier gene suitable for routine diagnosis was identified.

## 5. Environmental information

The vascular-disruption hypothesis is biologically plausible because pharyngeal-arch growth depends on transient embryonic arteries and neural-crest–vascular signaling. Reported maternal vasoactive exposures and vascular-risk states are compatible with this model, but causal attribution in an individual pregnancy is generally impossible. (zhang2016genomewideassociationstudy pages 7-8, petrin2026familialoculoauriculovertebralspectrum pages 10-11)

Smoking, alcohol, poor glycemic control, obesity, and teratogenic medications are modifiable general pregnancy risks. Exercise is not known to alter CFM risk. CFM is not infectious, contagious, occupationally acquired, or zoonotic.

## 6. Mechanism and pathophysiology

### Proposed causal chain

1. **Upstream trigger:** rare damaging variants (e.g., FOXI3 or SF3B2), polygenic susceptibility, chromosomal variation, and/or an embryonic vascular/environmental insult.
2. **Cellular disturbance:** altered transcription or RNA splicing; impaired cranial neural-crest specification, migration, survival, differentiation, or signaling with arch mesoderm and vasculature.
3. **Developmental field effect:** abnormal first/second pharyngeal-arch patterning and Meckel-cartilage/mandibular, auricular, ossicular, muscle, nerve, and soft-tissue morphogenesis.
4. **Primary phenotype:** microtia, mandibular hypoplasia, facial asymmetry, facial tags, ocular dermoids, facial-nerve weakness.
5. **Downstream consequences:** conductive hearing loss, malocclusion, feeding/speech impairment, airway obstruction/OSA, altered facial growth, and psychosocial burden.

GWAS genes are enriched in cell differentiation, migration, and organ development. VEGF–KDR signaling is a plausible vascular/mechanistic bridge: neural-crest-derived VEGF supports vessel growth and Meckel-cartilage/mandibular development. (zhang2016genomewideassociationstudy pages 4-5, zhang2016genomewideassociationstudy pages 3-3, petrin2026familialoculoauriculovertebralspectrum pages 10-11)

Suggested annotations include **GO: neural crest cell migration; embryonic craniofacial morphogenesis; pharyngeal system development; angiogenesis; RNA splicing; regulation of transcription by RNA polymerase II**. Relevant cell types are **cranial neural crest cell**, pharyngeal-arch mesenchymal cell, chondrocyte, osteoblast, myocyte, Schwann-cell/facial motor-neuron lineage, endothelial cell, and otic epithelial cell. Relevant compartments for FOXI3 include nucleus and cytoplasm; SF3B2 localizes to the spliceosomal/nuclear machinery.

There is no established primary immune, inflammatory, metabolic, mitochondrial, lysosomal, or protein-aggregation mechanism. Multi-omics, single-cell, spatial-transcriptomic, and CRISPR-screen evidence in human CFM remains research-stage.

## 7. Anatomical structures affected

Primary sites include the mandible (ramus, condyle, temporomandibular joint), maxilla, zygoma, temporal bone, external/middle ear, orbit, facial soft tissue and muscles of mastication, facial nerve, oral commissure, and pharyngeal airway. Secondary systems include vertebral column, heart/great vessels, kidney/urogenital tract, CNS, gastrointestinal, and respiratory systems. (renkema2019extracraniofacialanomaliesin pages 1-2)

Suggested UBERON terms: **pharyngeal arch, mandible, Meckel cartilage, temporomandibular joint, maxilla, zygomatic bone, pinna, external acoustic meatus, middle ear, orbit, facial nerve, vertebral column, heart, kidney, brain, pharynx**.

CFM is characteristically asymmetric: 83% unilateral and 12% bilateral in the large cohort; percentages do not sum to 100% because of missing/other classification data. (renkema2019extracraniofacialanomaliesin pages 1-2)

## 8. Temporal development

Onset is prenatal/congenital, not acute or episodic. The malformation itself does not remit. Its clinical expression changes with growth: hearing and airway problems may be evident in infancy; speech, dental, and educational consequences emerge in childhood; skeletal asymmetry and malocclusion may become more pronounced during facial growth; definitive orthognathic correction is often deferred until near skeletal maturity.

Critical windows are: early embryogenesis for causation; neonatal infancy for airway, feeding, and hearing detection; early childhood for language and psychosocial development; mixed dentition for orthodontic planning; and skeletal maturity for definitive jaw correction. NIH protocol NCT02639312 follows participants across developmental strata for as long as 17 years, illustrating the need for longitudinal rather than single-time-point assessment. (NCT02639312 chunk 1)

## 9. Inheritance and population

A commonly cited birth prevalence is approximately **1 in 7,500 live births** (about 13.3/100,000), although estimates vary by definition and ascertainment. The 991-person cohort was 53% male and 47% female. (renkema2019extracraniofacialanomaliesin pages 1-2, NCT02639312 chunk 1)

Most cases are sporadic. Gene-defined families may show autosomal-dominant inheritance with incomplete penetrance and variable expressivity; FOXI3 also supports recessive or compound dosage models. Anticipation is not established. Germline mosaicism is possible in principle but not quantified. No robust founder variant, carrier frequency, consanguinity effect, or ancestry-specific incidence is established for CFM overall. (mao2023foxi3pathogenicvariants pages 1-2, mao2023foxi3pathogenicvariants pages 7-8)

## 10. Diagnostics

### Clinical diagnosis

Diagnosis is based on physical examination and imaging. **OMENS/OMENS+** scores the orbit, mandible, ear, facial nerve, soft tissue, and extracraniofacial findings; **Pruzansky–Kaban** grades mandibular/TMJ deficiency. These are severity/classification systems, not perfectly validated binary diagnostic criteria. The 2023 FOXI3 study used OMENS phenotyping. (mao2023foxi3pathogenicvariants pages 9-10)

### Baseline evaluation

A craniofacial team should assess airway/sleep, feeding/swallowing, growth, ear anatomy and hearing, speech/language, vision, facial nerve, occlusion/dentition, spine, cardiac examination, renal/urogenital findings, development, and psychosocial needs.

Because 47% of a large cohort had extracraniofacial anomalies, authors recommended careful circulatory, renal, and neurologic examination, ECG/echocardiography, renal ultrasound, spinal imaging when indicated, and brain/spine MRI where neurologic abnormalities warrant it. Local guidelines differ on universal versus phenotype-triggered screening. (renkema2019extracraniofacialanomaliesin pages 7-8)

Useful tests include newborn/diagnostic audiology, temporal-bone CT for conductive anatomy and implant planning, low-dose craniofacial CT or cone-beam CT for skeletal planning, 3D photography, polysomnography when OSA is suspected, ophthalmologic examination, echocardiography, renal ultrasound, and spine radiography/MRI. No diagnostic blood chemistry, enzyme assay, biopsy, EEG, or disease-specific circulating biomarker exists.

### Genetic testing

A reasonable algorithm is:

1. Clinical genetics examination and three-generation pedigree.
2. **Chromosomal microarray** when there are multiple congenital anomalies, developmental delay, or dysmorphism beyond typical CFM.
3. **Trio exome or genome sequencing**, preferably with CNV/SV analysis, for bilateral/severe disease, positive family history, or syndromic findings.
4. Include **FOXI3 and SF3B2**; broader craniofacial/OAVS panels may include MYT1 and differential-diagnosis genes. Candidate-gene results require cautious interpretation.
5. Targeted parental testing for segregation and penetrance assessment.

WGS is attractive because CFM may involve coding variants, CNVs, structural variants, and noncoding modifiers; however, routine diagnostic yield for unselected CFM is not established. The NIH natural-history study combines 3D imaging and genomic testing. (NCT02639312 chunk 1)

### Differential diagnosis

Important alternatives include Treacher Collins syndrome (**TCOF1, POLR1D, POLR1C**; usually bilateral symmetric zygomatic/mandibular disease), mandibulofacial dysostosis with microcephaly (**EFTUD2**), Nager syndrome (**SF3B4**, preaxial limb defects), auriculocondylar syndrome (**PLCB4, GNAI3, EDN1**), CHARGE (**CHD7**), branchio-oto-renal syndrome (**EYA1/SIX1**), isolated microtia, craniofacial clefts, Parry–Romberg syndrome/progressive hemifacial atrophy (acquired progressive tissue loss), and teratogenic embryopathies.

There is no population newborn genetic screen or general carrier screen. Newborn hearing screening is clinically important but is not CFM-specific.

## 11. Outcome and prognosis

CFM itself usually does not shorten life expectancy. Mortality and five- or ten-year survival estimates are not established because prognosis depends on associated cardiac, airway, neurologic, and other anomalies. Severe neonatal airway obstruction or major congenital heart disease drives the greatest medical risk.

Long-term morbidity includes hearing impairment, speech/language difficulty, malocclusion and chewing impairment, OSA, feeding problems, facial weakness, visual problems, spinal disease, repeated surgery, and psychosocial burden. More severe OMENS/Pruzansky–Kaban findings and bilateral disease predict greater systemic anomaly burden. (renkema2019extracraniofacialanomaliesin pages 1-2, renkema2019extracraniofacialanomaliesin pages 7-8)

Anatomic “recovery” does not occur spontaneously. Treatment can improve airway, hearing, occlusion, symmetry, and participation, but growth-related recurrence/residual asymmetry and revision surgery are common. No validated molecular prognostic biomarker exists.

## 12. Treatment and current implementation

### Multidisciplinary strategy

Care should be individualized through craniofacial surgery, otology/audiology, orthodontics, maxillofacial surgery, speech-language pathology, ophthalmology, sleep/airway specialists, clinical genetics, pediatrics, psychology, and social work.

- **Airway:** positioning and noninvasive support in mild cases; tongue–lip adhesion, tracheostomy, or mandibular distraction in severe obstruction, selected by anatomy and physiology.
- **Hearing:** bone-conduction amplification in infancy, conventional aids where feasible, canal/ossicular reconstruction in selected patients, and implantable bone-conduction devices.
- **Mandible/TMJ:** mandibular distraction osteogenesis, costochondral graft or vascularized bone reconstruction for severe ramus/condyle absence, and orthognathic surgery at/near maturity. Early distraction can relieve airway or severe asymmetry but does not reliably eliminate later orthognathic surgery.
- **Orthodontics:** functional appliances in selected growing children, occlusal management, presurgical orthodontics.
- **Ear:** autologous rib-cartilage reconstruction, porous polyethylene reconstruction, or prosthetic rehabilitation; coordinate timing with hearing surgery.
- **Soft tissue:** structural fat grafting, free-flap augmentation, or other contour procedures.
- **Facial nerve:** eye protection, static procedures, nerve/muscle transfer, or free functional muscle transfer in selected patients.
- **Rehabilitation:** feeding therapy, speech/language treatment, dental care, physical therapy where spine/limb anomalies occur, and psychosocial support.

Suggested NCIt intervention concepts include *reconstructive surgery*, *mandibular distraction osteogenesis*, *orthognathic surgery*, *bone grafting*, *fat grafting*, *hearing aid*, *cochlear/osseointegrated hearing device*, *speech therapy*, *orthodontic treatment*, and *psychosocial intervention*.

### Trials and applications

- **NCT01674439:** completed phase 2 randomized double-blind trial, 29 participants aged 10–35, comparing adipose-derived regenerative-cell-supplemented fat grafting with standard grafting; primary outcome was six-month CT volume retention. (NCT01674439 chunk 1)
- **NCT03806361:** completed randomized pediatric trial, 30 children, comparing the same strategies with serial 3D-photogrammetric retention outcomes. (NCT03806361 chunk 1)
- **NCT03270618:** approximately 30 participants; evaluated CAD/CAM/3D-printed templates for osteotomy and distractor placement. (NCT03270618 chunk 1)
- **NCT03869021:** randomized 12-person comparison of computer-guided versus free-hand mandibular distraction, assessing six-month cephalometric/cosmetic outcomes. (NCT03869021 chunk 2)
- **NCT03861650:** controlled BMAC-versus-saline adjunct study during mandibular distraction, using six-month CBCT bone density. This is regenerative-surgery research, not established stem-cell therapy. (NCT03861650 chunk 2)
- **NCT02639312:** recruiting NIH observational natural-history/genomics study, target enrollment 2,400; not a treatment trial. (NCT02639312 chunk 1)

No approved CFM-specific pharmacotherapy, pharmacogenomic algorithm, gene therapy, RNA therapy, immunotherapy, or molecularly targeted treatment exists.

## 13. Prevention

Primary prevention is limited because most cases are sporadic and causes are incompletely known. Recommended measures are standard preconception/pregnancy care: folic acid at guideline doses, glycemic and weight optimization, smoking/alcohol avoidance, review of vasoactive or teratogenic medicines, and avoidance of known teratogens. These measures should not be represented as proven CFM-specific prophylaxis. (zhang2016genomewideassociationstudy pages 7-8)

Secondary/tertiary prevention is more actionable: prenatal ultrasound may detect micrognathia, facial asymmetry, microtia, or systemic anomalies; postnatal early hearing, airway, feeding, cardiac, renal, spinal, visual, and developmental assessment can prevent avoidable complications. Early amplification and speech intervention reduce secondary communication disability.

For a known familial pathogenic variant, genetic counseling should explain incomplete penetrance and variable expressivity. Prenatal diagnosis and preimplantation genetic testing may be technically possible for a clearly pathogenic familial variant, but phenotype severity may remain unpredictable. No vaccine or medication prevents CFM.

## 14. Other species and natural disease

CFM is not transmissible or zoonotic. Naturally occurring **FOXI3** variation in hairless dog breeds produces ectodermal hair/dental phenotypes rather than a complete human CFM analogue, illustrating conserved FOXI3 developmental biology but limited phenotypic equivalence. (mao2023foxi3pathogenicvariants pages 8-9)

Species annotations of relevance include *Homo sapiens* (NCBI Taxon 9606), *Mus musculus* (10090), *Danio rerio* (7955), and *Canis lupus familiaris* (9615). Ortholog studies support conservation of FOXI3 and neural-crest/pharyngeal-arch pathways. No veterinary syndrome should be labeled identical to human CFM without direct comparative evidence.

## 15. Model organisms

The strongest model is the CRISPR knock-in mouse. Foxi3 F218L, R224H, and triple-mutant R220W/R222Q/R224H lines were developed. Homozygous mutants showed mandibular underdevelopment, absent or severe microtia, skull asymmetry, absent ear bones, syngnathia, and cleft palate in approximately 50%; the triple homozygous state was embryonic/neonatal lethal, while heterozygotes were viable with milder/variable skeletal findings. (mao2023foxi3pathogenicvariants pages 6-7, mao2023foxi3pathogenicvariants pages 7-8, mao2023foxi3pathogenicvariants pages 12-13)

These models recapitulate ear, jaw, palate, and craniofacial skeletal abnormalities and support FOXI3 dosage sensitivity. Limitations are greater severity and lethality than typical human heterozygous CFM, species-specific craniofacial anatomy, and incomplete modeling of psychosocial, hearing-language, and long-term surgical outcomes.

GWAS candidate-gene mutant mice and developmental zebrafish systems are useful for neural-crest migration, pharyngeal-arch patterning, vascular signaling, cartilage, and osteogenesis studies. Nine GWAS candidate-gene mouse models reportedly displayed craniofacial abnormalities, but they model pathway perturbation rather than proving each locus causes human CFM. (zhang2016genomewideassociationstudy pages 4-5)

## Recent developments, expert interpretation, and evidence gaps

The most consequential 2023 development was FOXI3 gene validation across human genetics, cell biology, and knock-in mice. Its diagnostic contribution is real but modest—3.1% in the reported cohort—so a negative FOXI3 result does not exclude CFM. The study’s modifier-haplotype result also explains why apparently unaffected parents can transmit a clinically important allele. (mao2023foxi3pathogenicvariants pages 1-2, mao2023foxi3pathogenicvariants pages 8-9)

Recent work has also emphasized standardized research criteria, 3D phenotyping, registries, longitudinal outcomes, psychosocial experience, and digitally guided surgery. The field is moving from descriptive morphology toward integrated genomic–phenomic models, but practice remains variable and comparative treatment trials are small.

Major knowledge gaps are: validated diagnostic criteria; ancestry-diverse incidence estimates; penetrance and genotype–phenotype data for genes other than FOXI3; rigorous G×E estimates; disease-specific biomarkers or omics signatures; standardized patient-reported outcomes; and adequately powered comparisons of distraction, grafting, orthognathic, ear, and soft-tissue strategies. The 991-patient anomaly cohort is authoritative for systemic burden but retrospective and referral-center based, while current interventional studies generally enroll only 12–30 participants. (renkema2019extracraniofacialanomaliesin pages 1-2, NCT01674439 chunk 1, NCT03869021 chunk 2, NCT03806361 chunk 1)

## Key references

1. Mao K, et al. **FOXI3 pathogenic variants cause one form of craniofacial microsomia.** *Nature Communications*. Published April 2023. DOI: https://doi.org/10.1038/s41467-023-37703-6. PMID: https://pubmed.ncbi.nlm.nih.gov/37041148/ (mao2023foxi3pathogenicvariants pages 1-2)
2. Renkema RW, et al. **Extracraniofacial anomalies in craniofacial microsomia: retrospective analysis of 991 patients.** *International Journal of Oral and Maxillofacial Surgery*. Published September 2019. DOI: https://doi.org/10.1016/j.ijom.2019.01.031. (renkema2019extracraniofacialanomaliesin pages 1-2)
3. Zhang Y-B, et al. **Genome-wide association study identifies multiple susceptibility loci for craniofacial microsomia.** *Nature Communications*. Published February 2016. DOI: https://doi.org/10.1038/ncomms10605. (zhang2016genomewideassociationstudy pages 4-5, zhang2016genomewideassociationstudy pages 3-3)
4. Open Targets. **Craniofacial microsomia–target associations**: SF3B2, FOXI3, and CHAF1A; includes PMID 34344887 for SF3B2 and PMIDs 36260083/37041148 for FOXI3. Accessed through the current tool query. (OpenTargets Search: craniofacial microsomia)
5. ClinicalTrials.gov. **Natural History of Craniofacial Anomalies and Developmental Growth Variants**, NCT02639312. NIH/NIDCR; recruiting observational study, planned enrollment 2,400. https://clinicaltrials.gov/study/NCT02639312 (NCT02639312 chunk 1)
6. ClinicalTrials.gov. **Clinical Trial of Fat Grafts Supplemented With Adipose-derived Regenerative Cells**, NCT01674439. https://clinicaltrials.gov/study/NCT01674439 (NCT01674439 chunk 1)

**Curation conclusion:** CFM should be represented as a congenital, complex, etiologically heterogeneous craniofacial-developmental spectrum. Gene-defined FOXI3- and SF3B2-associated forms can be separately annotated, but most cases remain multifactorial/unsolved. Phenotype and systemic screening data are stronger than evidence for any one reconstructive treatment algorithm.

References

1. (renkema2019extracraniofacialanomaliesin pages 1-2): R.W. Renkema, C.J.J.M. Caron, E. Pauws, E.B. Wolvius, J.A.M. Schipper, W. Rooijers, D.J. Dunaway, C.R. Forrest, B.L. Padwa, and M.J. Koudstaal. Extracraniofacial anomalies in craniofacial microsomia: retrospective analysis of 991 patients. International journal of oral and maxillofacial surgery, 48:1169-1176, Sep 2019. URL: https://doi.org/10.1016/j.ijom.2019.01.031, doi:10.1016/j.ijom.2019.01.031. This article has 50 citations and is from a peer-reviewed journal.

2. (OpenTargets Search: craniofacial microsomia): Open Targets Query (craniofacial microsomia, 7 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (mao2023foxi3pathogenicvariants pages 1-2): Ke Mao, Christelle Borel, Muhammad Ansar, Angad Jolly, Periklis Makrythanasis, Christine Froehlich, Justyna Iwaszkiewicz, Bingqing Wang, Xiaopeng Xu, Qiang Li, Xavier Blanc, Hao Zhu, Qi Chen, Fujun Jin, Harinarayana Ankamreddy, Sunita Singh, Hongyuan Zhang, Xiaogang Wang, Peiwei Chen, Emmanuelle Ranza, Sohail Aziz Paracha, Syed Fahim Shah, Valentina Guida, Francesca Piceci-Sparascio, Daniela Melis, Bruno Dallapiccola, Maria Cristina Digilio, Antonio Novelli, Monia Magliozzi, Maria Teresa Fadda, Haley Streff, Keren Machol, Richard A. Lewis, Vincent Zoete, Gabriella Maria Squeo, Paolo Prontera, Giorgia Mancano, Giulia Gori, Milena Mariani, Angelo Selicorni, Stavroula Psoni, Helen Fryssira, Sofia Douzgou, Sandrine Marlin, Saskia Biskup, Alessandro De Luca, Giuseppe Merla, Shouqin Zhao, Timothy C. Cox, Andrew K. Groves, James R. Lupski, Qingguo Zhang, Yong-Biao Zhang, and Stylianos E. Antonarakis. Foxi3 pathogenic variants cause one form of craniofacial microsomia. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37703-6, doi:10.1038/s41467-023-37703-6. This article has 41 citations and is from a highest quality peer-reviewed journal.

4. (mao2023foxi3pathogenicvariants pages 5-6): Ke Mao, Christelle Borel, Muhammad Ansar, Angad Jolly, Periklis Makrythanasis, Christine Froehlich, Justyna Iwaszkiewicz, Bingqing Wang, Xiaopeng Xu, Qiang Li, Xavier Blanc, Hao Zhu, Qi Chen, Fujun Jin, Harinarayana Ankamreddy, Sunita Singh, Hongyuan Zhang, Xiaogang Wang, Peiwei Chen, Emmanuelle Ranza, Sohail Aziz Paracha, Syed Fahim Shah, Valentina Guida, Francesca Piceci-Sparascio, Daniela Melis, Bruno Dallapiccola, Maria Cristina Digilio, Antonio Novelli, Monia Magliozzi, Maria Teresa Fadda, Haley Streff, Keren Machol, Richard A. Lewis, Vincent Zoete, Gabriella Maria Squeo, Paolo Prontera, Giorgia Mancano, Giulia Gori, Milena Mariani, Angelo Selicorni, Stavroula Psoni, Helen Fryssira, Sofia Douzgou, Sandrine Marlin, Saskia Biskup, Alessandro De Luca, Giuseppe Merla, Shouqin Zhao, Timothy C. Cox, Andrew K. Groves, James R. Lupski, Qingguo Zhang, Yong-Biao Zhang, and Stylianos E. Antonarakis. Foxi3 pathogenic variants cause one form of craniofacial microsomia. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37703-6, doi:10.1038/s41467-023-37703-6. This article has 41 citations and is from a highest quality peer-reviewed journal.

5. (NCT02639312 chunk 1):  Natural History of Craniofacial Anomalies and Developmental Growth Variants. National Institute of Dental and Craniofacial Research (NIDCR). 2016. ClinicalTrials.gov Identifier: NCT02639312

6. (mao2023foxi3pathogenicvariants pages 9-10): Ke Mao, Christelle Borel, Muhammad Ansar, Angad Jolly, Periklis Makrythanasis, Christine Froehlich, Justyna Iwaszkiewicz, Bingqing Wang, Xiaopeng Xu, Qiang Li, Xavier Blanc, Hao Zhu, Qi Chen, Fujun Jin, Harinarayana Ankamreddy, Sunita Singh, Hongyuan Zhang, Xiaogang Wang, Peiwei Chen, Emmanuelle Ranza, Sohail Aziz Paracha, Syed Fahim Shah, Valentina Guida, Francesca Piceci-Sparascio, Daniela Melis, Bruno Dallapiccola, Maria Cristina Digilio, Antonio Novelli, Monia Magliozzi, Maria Teresa Fadda, Haley Streff, Keren Machol, Richard A. Lewis, Vincent Zoete, Gabriella Maria Squeo, Paolo Prontera, Giorgia Mancano, Giulia Gori, Milena Mariani, Angelo Selicorni, Stavroula Psoni, Helen Fryssira, Sofia Douzgou, Sandrine Marlin, Saskia Biskup, Alessandro De Luca, Giuseppe Merla, Shouqin Zhao, Timothy C. Cox, Andrew K. Groves, James R. Lupski, Qingguo Zhang, Yong-Biao Zhang, and Stylianos E. Antonarakis. Foxi3 pathogenic variants cause one form of craniofacial microsomia. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37703-6, doi:10.1038/s41467-023-37703-6. This article has 41 citations and is from a highest quality peer-reviewed journal.

7. (renkema2019extracraniofacialanomaliesin pages 7-8): R.W. Renkema, C.J.J.M. Caron, E. Pauws, E.B. Wolvius, J.A.M. Schipper, W. Rooijers, D.J. Dunaway, C.R. Forrest, B.L. Padwa, and M.J. Koudstaal. Extracraniofacial anomalies in craniofacial microsomia: retrospective analysis of 991 patients. International journal of oral and maxillofacial surgery, 48:1169-1176, Sep 2019. URL: https://doi.org/10.1016/j.ijom.2019.01.031, doi:10.1016/j.ijom.2019.01.031. This article has 50 citations and is from a peer-reviewed journal.

8. (petrin2026familialoculoauriculovertebralspectrum pages 11-13): Aline L Petrin, Ligiane Alves Machado-Paula, Austin Hinkle, Luke Hovey, Waheed Awotoye, Michael Chimenti, Benjamin Darbro, Lucilene A Ribeiro-Bicudo, Shareef M Dabdoub, Tabitha Peter, Patrick Breheny, Jeffrey C Murray, Eric Van Otterloo, Shankar Rengasamy Venugopalan, and Lina M Moreno-Uribe. Familial oculoauriculovertebral spectrum: a genomic investigation of autosomal dominant inheritance. The Cleft palate-craniofacial journal : official publication of the American Cleft Palate-Craniofacial Association, pages 10556656241306202, Jan 2026. URL: https://doi.org/10.1177/10556656241306202, doi:10.1177/10556656241306202. This article has 0 citations.

9. (petrin2026familialoculoauriculovertebralspectrum pages 1-3): Aline L Petrin, Ligiane Alves Machado-Paula, Austin Hinkle, Luke Hovey, Waheed Awotoye, Michael Chimenti, Benjamin Darbro, Lucilene A Ribeiro-Bicudo, Shareef M Dabdoub, Tabitha Peter, Patrick Breheny, Jeffrey C Murray, Eric Van Otterloo, Shankar Rengasamy Venugopalan, and Lina M Moreno-Uribe. Familial oculoauriculovertebral spectrum: a genomic investigation of autosomal dominant inheritance. The Cleft palate-craniofacial journal : official publication of the American Cleft Palate-Craniofacial Association, pages 10556656241306202, Jan 2026. URL: https://doi.org/10.1177/10556656241306202, doi:10.1177/10556656241306202. This article has 0 citations.

10. (mao2023foxi3pathogenicvariants pages 6-7): Ke Mao, Christelle Borel, Muhammad Ansar, Angad Jolly, Periklis Makrythanasis, Christine Froehlich, Justyna Iwaszkiewicz, Bingqing Wang, Xiaopeng Xu, Qiang Li, Xavier Blanc, Hao Zhu, Qi Chen, Fujun Jin, Harinarayana Ankamreddy, Sunita Singh, Hongyuan Zhang, Xiaogang Wang, Peiwei Chen, Emmanuelle Ranza, Sohail Aziz Paracha, Syed Fahim Shah, Valentina Guida, Francesca Piceci-Sparascio, Daniela Melis, Bruno Dallapiccola, Maria Cristina Digilio, Antonio Novelli, Monia Magliozzi, Maria Teresa Fadda, Haley Streff, Keren Machol, Richard A. Lewis, Vincent Zoete, Gabriella Maria Squeo, Paolo Prontera, Giorgia Mancano, Giulia Gori, Milena Mariani, Angelo Selicorni, Stavroula Psoni, Helen Fryssira, Sofia Douzgou, Sandrine Marlin, Saskia Biskup, Alessandro De Luca, Giuseppe Merla, Shouqin Zhao, Timothy C. Cox, Andrew K. Groves, James R. Lupski, Qingguo Zhang, Yong-Biao Zhang, and Stylianos E. Antonarakis. Foxi3 pathogenic variants cause one form of craniofacial microsomia. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37703-6, doi:10.1038/s41467-023-37703-6. This article has 41 citations and is from a highest quality peer-reviewed journal.

11. (mao2023foxi3pathogenicvariants pages 4-5): Ke Mao, Christelle Borel, Muhammad Ansar, Angad Jolly, Periklis Makrythanasis, Christine Froehlich, Justyna Iwaszkiewicz, Bingqing Wang, Xiaopeng Xu, Qiang Li, Xavier Blanc, Hao Zhu, Qi Chen, Fujun Jin, Harinarayana Ankamreddy, Sunita Singh, Hongyuan Zhang, Xiaogang Wang, Peiwei Chen, Emmanuelle Ranza, Sohail Aziz Paracha, Syed Fahim Shah, Valentina Guida, Francesca Piceci-Sparascio, Daniela Melis, Bruno Dallapiccola, Maria Cristina Digilio, Antonio Novelli, Monia Magliozzi, Maria Teresa Fadda, Haley Streff, Keren Machol, Richard A. Lewis, Vincent Zoete, Gabriella Maria Squeo, Paolo Prontera, Giorgia Mancano, Giulia Gori, Milena Mariani, Angelo Selicorni, Stavroula Psoni, Helen Fryssira, Sofia Douzgou, Sandrine Marlin, Saskia Biskup, Alessandro De Luca, Giuseppe Merla, Shouqin Zhao, Timothy C. Cox, Andrew K. Groves, James R. Lupski, Qingguo Zhang, Yong-Biao Zhang, and Stylianos E. Antonarakis. Foxi3 pathogenic variants cause one form of craniofacial microsomia. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37703-6, doi:10.1038/s41467-023-37703-6. This article has 41 citations and is from a highest quality peer-reviewed journal.

12. (zhang2016genomewideassociationstudy pages 4-5): Yong-Biao Zhang, Jintian Hu, Jiao Zhang, Xu Zhou, Xin Li, Chaohao Gu, Tun Liu, Yangchun Xie, Jiqiang Liu, Mingliang Gu, Panpan Wang, Tingting Wu, Jin Qian, Yue Wang, Xiaoqun Dong, Jun Yu, and Qingguo Zhang. Genome-wide association study identifies multiple susceptibility loci for craniofacial microsomia. Nature Communications, Feb 2016. URL: https://doi.org/10.1038/ncomms10605, doi:10.1038/ncomms10605. This article has 46 citations and is from a highest quality peer-reviewed journal.

13. (zhang2016genomewideassociationstudy pages 7-8): Yong-Biao Zhang, Jintian Hu, Jiao Zhang, Xu Zhou, Xin Li, Chaohao Gu, Tun Liu, Yangchun Xie, Jiqiang Liu, Mingliang Gu, Panpan Wang, Tingting Wu, Jin Qian, Yue Wang, Xiaoqun Dong, Jun Yu, and Qingguo Zhang. Genome-wide association study identifies multiple susceptibility loci for craniofacial microsomia. Nature Communications, Feb 2016. URL: https://doi.org/10.1038/ncomms10605, doi:10.1038/ncomms10605. This article has 46 citations and is from a highest quality peer-reviewed journal.

14. (zhang2016genomewideassociationstudy pages 3-3): Yong-Biao Zhang, Jintian Hu, Jiao Zhang, Xu Zhou, Xin Li, Chaohao Gu, Tun Liu, Yangchun Xie, Jiqiang Liu, Mingliang Gu, Panpan Wang, Tingting Wu, Jin Qian, Yue Wang, Xiaoqun Dong, Jun Yu, and Qingguo Zhang. Genome-wide association study identifies multiple susceptibility loci for craniofacial microsomia. Nature Communications, Feb 2016. URL: https://doi.org/10.1038/ncomms10605, doi:10.1038/ncomms10605. This article has 46 citations and is from a highest quality peer-reviewed journal.

15. (mao2023foxi3pathogenicvariants pages 7-8): Ke Mao, Christelle Borel, Muhammad Ansar, Angad Jolly, Periklis Makrythanasis, Christine Froehlich, Justyna Iwaszkiewicz, Bingqing Wang, Xiaopeng Xu, Qiang Li, Xavier Blanc, Hao Zhu, Qi Chen, Fujun Jin, Harinarayana Ankamreddy, Sunita Singh, Hongyuan Zhang, Xiaogang Wang, Peiwei Chen, Emmanuelle Ranza, Sohail Aziz Paracha, Syed Fahim Shah, Valentina Guida, Francesca Piceci-Sparascio, Daniela Melis, Bruno Dallapiccola, Maria Cristina Digilio, Antonio Novelli, Monia Magliozzi, Maria Teresa Fadda, Haley Streff, Keren Machol, Richard A. Lewis, Vincent Zoete, Gabriella Maria Squeo, Paolo Prontera, Giorgia Mancano, Giulia Gori, Milena Mariani, Angelo Selicorni, Stavroula Psoni, Helen Fryssira, Sofia Douzgou, Sandrine Marlin, Saskia Biskup, Alessandro De Luca, Giuseppe Merla, Shouqin Zhao, Timothy C. Cox, Andrew K. Groves, James R. Lupski, Qingguo Zhang, Yong-Biao Zhang, and Stylianos E. Antonarakis. Foxi3 pathogenic variants cause one form of craniofacial microsomia. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37703-6, doi:10.1038/s41467-023-37703-6. This article has 41 citations and is from a highest quality peer-reviewed journal.

16. (mao2023foxi3pathogenicvariants pages 8-9): Ke Mao, Christelle Borel, Muhammad Ansar, Angad Jolly, Periklis Makrythanasis, Christine Froehlich, Justyna Iwaszkiewicz, Bingqing Wang, Xiaopeng Xu, Qiang Li, Xavier Blanc, Hao Zhu, Qi Chen, Fujun Jin, Harinarayana Ankamreddy, Sunita Singh, Hongyuan Zhang, Xiaogang Wang, Peiwei Chen, Emmanuelle Ranza, Sohail Aziz Paracha, Syed Fahim Shah, Valentina Guida, Francesca Piceci-Sparascio, Daniela Melis, Bruno Dallapiccola, Maria Cristina Digilio, Antonio Novelli, Monia Magliozzi, Maria Teresa Fadda, Haley Streff, Keren Machol, Richard A. Lewis, Vincent Zoete, Gabriella Maria Squeo, Paolo Prontera, Giorgia Mancano, Giulia Gori, Milena Mariani, Angelo Selicorni, Stavroula Psoni, Helen Fryssira, Sofia Douzgou, Sandrine Marlin, Saskia Biskup, Alessandro De Luca, Giuseppe Merla, Shouqin Zhao, Timothy C. Cox, Andrew K. Groves, James R. Lupski, Qingguo Zhang, Yong-Biao Zhang, and Stylianos E. Antonarakis. Foxi3 pathogenic variants cause one form of craniofacial microsomia. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37703-6, doi:10.1038/s41467-023-37703-6. This article has 41 citations and is from a highest quality peer-reviewed journal.

17. (petrin2026familialoculoauriculovertebralspectrum pages 10-11): Aline L Petrin, Ligiane Alves Machado-Paula, Austin Hinkle, Luke Hovey, Waheed Awotoye, Michael Chimenti, Benjamin Darbro, Lucilene A Ribeiro-Bicudo, Shareef M Dabdoub, Tabitha Peter, Patrick Breheny, Jeffrey C Murray, Eric Van Otterloo, Shankar Rengasamy Venugopalan, and Lina M Moreno-Uribe. Familial oculoauriculovertebral spectrum: a genomic investigation of autosomal dominant inheritance. The Cleft palate-craniofacial journal : official publication of the American Cleft Palate-Craniofacial Association, pages 10556656241306202, Jan 2026. URL: https://doi.org/10.1177/10556656241306202, doi:10.1177/10556656241306202. This article has 0 citations.

18. (petrin2026familialoculoauriculovertebralspectrum pages 15-19): Aline L Petrin, Ligiane Alves Machado-Paula, Austin Hinkle, Luke Hovey, Waheed Awotoye, Michael Chimenti, Benjamin Darbro, Lucilene A Ribeiro-Bicudo, Shareef M Dabdoub, Tabitha Peter, Patrick Breheny, Jeffrey C Murray, Eric Van Otterloo, Shankar Rengasamy Venugopalan, and Lina M Moreno-Uribe. Familial oculoauriculovertebral spectrum: a genomic investigation of autosomal dominant inheritance. The Cleft palate-craniofacial journal : official publication of the American Cleft Palate-Craniofacial Association, pages 10556656241306202, Jan 2026. URL: https://doi.org/10.1177/10556656241306202, doi:10.1177/10556656241306202. This article has 0 citations.

19. (mao2023foxi3pathogenicvariants pages 12-13): Ke Mao, Christelle Borel, Muhammad Ansar, Angad Jolly, Periklis Makrythanasis, Christine Froehlich, Justyna Iwaszkiewicz, Bingqing Wang, Xiaopeng Xu, Qiang Li, Xavier Blanc, Hao Zhu, Qi Chen, Fujun Jin, Harinarayana Ankamreddy, Sunita Singh, Hongyuan Zhang, Xiaogang Wang, Peiwei Chen, Emmanuelle Ranza, Sohail Aziz Paracha, Syed Fahim Shah, Valentina Guida, Francesca Piceci-Sparascio, Daniela Melis, Bruno Dallapiccola, Maria Cristina Digilio, Antonio Novelli, Monia Magliozzi, Maria Teresa Fadda, Haley Streff, Keren Machol, Richard A. Lewis, Vincent Zoete, Gabriella Maria Squeo, Paolo Prontera, Giorgia Mancano, Giulia Gori, Milena Mariani, Angelo Selicorni, Stavroula Psoni, Helen Fryssira, Sofia Douzgou, Sandrine Marlin, Saskia Biskup, Alessandro De Luca, Giuseppe Merla, Shouqin Zhao, Timothy C. Cox, Andrew K. Groves, James R. Lupski, Qingguo Zhang, Yong-Biao Zhang, and Stylianos E. Antonarakis. Foxi3 pathogenic variants cause one form of craniofacial microsomia. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37703-6, doi:10.1038/s41467-023-37703-6. This article has 41 citations and is from a highest quality peer-reviewed journal.

20. (NCT03270618 chunk 1): Xudong Wang. Accuracy of a CAD/CAM Surgical Template for Mandible Distraction. Shanghai Ninth People's Hospital Affiliated to Shanghai Jiao Tong University. 2014. ClinicalTrials.gov Identifier: NCT03270618

21. (NCT01674439 chunk 1): Daniela Y. S. Tanikawa. Clinical Trial of Fat Grafts Supplemented With Adipose-derived Regenerative Cells. University of Sao Paulo. 2010. ClinicalTrials.gov Identifier: NCT01674439

22. (NCT03869021 chunk 2): Yasser Mohamed Nabil Ahmed Khirat El Hadidi. Computer Guided for Mandibular Distraction Osteogenesis. Yasser Mohamed Nabil Ahmed Khirat El Hadidi. 2015. ClinicalTrials.gov Identifier: NCT03869021

23. (NCT03806361 chunk 1): Daniela S Tanikawa. Fat Grafts With Adipose-derived Regenerative Cells for Soft Tissue Reconstruction in Children. Hospital Sirio-Libanes. 2019. ClinicalTrials.gov Identifier: NCT03806361

24. (NCT03861650 chunk 2): Yasser Mohamed Nabil Ahmed Khirat El Hadidi. Evaluation of Effect of Bone Marrow Aspirate Concentrate on Distracted Mandibular Bone Properties. Yasser Mohamed Nabil Ahmed Khirat El Hadidi. 2015. ClinicalTrials.gov Identifier: NCT03861650

25. (NCT00340964 chunk 1):  Positive Exposure: A Photography and Video Intervention for Individuals With Craniofacial Differences. National Human Genome Research Institute (NHGRI). 2005. ClinicalTrials.gov Identifier: NCT00340964

## Artifacts

- [Edison artifact artifact-00](Craniofacial_Microsomia-deep-research-falcon_artifacts/artifact-00.md)