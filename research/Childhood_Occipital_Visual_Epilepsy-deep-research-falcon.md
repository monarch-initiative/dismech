---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-05T19:00:25.186843'
end_time: '2026-08-05T19:09:10.081975'
duration_seconds: 524.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Childhood Occipital Visual Epilepsy
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 10
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Childhood_Occipital_Visual_Epilepsy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Childhood Occipital Visual Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Childhood Occipital Visual Epilepsy** covering all of the
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
- **Disease Name:** Childhood Occipital Visual Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Childhood Occipital Visual Epilepsy** covering all of the
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


# Childhood Occipital Visual Epilepsy: Disease-Characteristics Research Report

**Scope and evidence caveat.** Childhood occipital visual epilepsy (COVE) is rare, and recent syndrome-specific primary research is sparse. The strongest current source is the 2022 International League Against Epilepsy (ILAE) classification, summarized in a 2024 pediatric update and a 2025 classification review. Much of the quantitative literature predates 2023 and was not available in full text during this retrieval. Consequently, this report distinguishes established COVE findings from broader focal-epilepsy practice and does not assign genes, variants, frequencies, or ontology identifiers without adequate evidence.

## Executive summary

COVE is a childhood-onset, self-limited focal epilepsy characterized by brief focal sensory visual seizures arising from occipital networks. Elementary visual hallucinations—often colored, circular forms—and transient visual loss are characteristic; seizures may spread to produce eye/head deviation, impaired awareness, or bilateral tonic–clonic activity, and postictal headache can mimic migraine. The modern name replaces “late-onset benign occipital epilepsy” and “idiopathic childhood occipital epilepsy of Gastaut.” The ILAE places COVE among childhood self-limited focal epilepsies and regards its inheritance as presumed complex rather than established monogenic. Most patients remit by adolescence, although a minority continue to have seizures. EEG and appropriate MRI are central to diagnosis; no disease-specific molecular biomarker, causal gene, precision therapy, or validated COVE-specific animal model is established in the retrieved evidence. (manokaran2024the2022international pages 2-4, manokaran2024the2022international pages 4-5, wirrell2025epilepsysyndromesclassification. pages 6-7)

| domain | established finding | suggested ontology mapping | evidence strength/limitation |
|---|---|---|---|
| nomenclature/classification | The current ILAE name is **Childhood Occipital Visual Epilepsy (COVE)**; it replaced **late-onset (benign) occipital epilepsy** / **idiopathic childhood occipital epilepsy–Gastaut type**. COVE is grouped among **self-limited focal epilepsies** with childhood onset; later reviews also note it among focal epilepsy syndromes with presumed complex inheritance. (manokaran2024the2022international pages 2-4, manokaran2024the2022international pages 4-5) | MONDO: not established here; MeSH/ICD: not established here; NCIT: epilepsy syndrome concept if needed | Strong for modern nomenclature/classification from ILAE-derived secondary sources; no disease-specific external identifier confirmed in available context, so none should be asserted. |
| core phenotype | COVE seizures are described as **occipital** seizures with **sensory visual symptoms** and **elementary visual phenomena**; broader ILAE review notes visual phenomena such as **hallucinations or blindness** in occipital epilepsies. Typical onset is in **childhood (2–12 years syndromic group)**. (manokaran2024the2022international pages 4-5, wirrell2025epilepsysyndromesclassification. pages 6-7) | HPO suggestions: Visual hallucinations; Transient visual loss/blindness; Focal aware seizure; Childhood onset | Moderate: phenotype is directly stated, but exact frequency and age-distribution figures for COVE are not available in retrieved context. |
| EEG | ILAE update states the syndrome name reflects **occipital semiology and EEG findings**. Specific EEG morphology/mandatory criteria were not present in retrieved text. (manokaran2024the2022international pages 4-5) | HPO suggestion: Abnormality of EEG; possible occipital epileptiform discharges (term not confirmed here) | Moderate-to-limited: syndrome-level association with occipital EEG findings is established, but exact interictal/ictal patterns are unavailable in accessible sources. |
| anatomy | Primary system affected is the **central nervous system**, especially the **occipital lobe/cortex** as the seizure-generating region implied by syndrome name and visual semiology. (wirrell2025epilepsysyndromesclassification. pages 6-7) | UBERON suggestions: brain; occipital lobe; visual cortex | Moderate: anatomy is strongly implied by syndrome definition, but no COVE-specific imaging-pathology localization dataset was available. |
| etiology/genetics | Available ILAE-derived review characterizes COVE among focal epilepsy syndromes with **presumed complex inheritance**. No single causal gene is established for COVE in the retrieved evidence. Adjacent **GRIN2A** evidence concerns epilepsy-aphasia syndromes and should **not** be treated as COVE-specific. (manokaran2024the2022international pages 4-5, thompsonlake2024perisylvianandhippocampal pages 1-2, thompsonlake2024perisylvianandhippocampal pages 5-6) | Inheritance: multifactorial/complex; HGNC gene mapping: none established for COVE | Moderate for “complex inheritance” label; strong limitation against assigning monogenic causation based on current context. |
| environmental/protective factors | No specific environmental, infectious, toxic, or protective factors were identified in the retrieved COVE-focused evidence. | none established | Low/absent evidence in available sources. |
| pathophysiology/mechanism | Syndrome-level mechanism is best summarized as **focal occipital cortical hyperexcitability** producing elementary visual seizures; direct molecular pathway evidence specific to COVE was not retrieved. (wirrell2025epilepsysyndromesclassification. pages 6-7) | GO suggestion: regulation of membrane potential; neuronal action potential; CL suggestion: cortical excitatory neuron/inhibitory interneuron (generic only) | Limited: mechanistic inference is electroclinical, not molecularly resolved for COVE in available evidence. |
| disease course/prognosis | COVE belongs to the **self-limited focal epilepsies**. Review text states that **most cases remit in adolescence**, though **a small subset may have persistent seizures**. (wirrell2025epilepsysyndromesclassification. pages 6-7, wirrell2025epilepsysyndromesclassification. pages 5-6) | HPO suggestions: Episodic course; Remission in adolescence | Moderate-to-strong for overall favorable course; exact remission percentages were not available in retrieved accessible sources. |
| diagnosis/workup | Recognition of childhood-onset syndromes requires **seizure semiology**, **developmental status**, and **EEG features**; **brain MRI** and sometimes **genetic studies** may be used in selected cases. For COVE specifically, diagnosis is framed by **occipital semiology and EEG findings**. (manokaran2024the2022international pages 4-5) | Diagnostic modality terms: EEG; Brain MRI | Strong for general workup principles from ILAE update; limited because mandatory/alert/exclusionary COVE criteria were not accessible in retrieved text. |
| differential diagnosis | The nomenclature change explicitly separates COVE from **self-limited epilepsy with autonomic seizures (SeLEAS/Panayiotopoulos syndrome)** and from **photosensitive occipital lobe epilepsy (POLE)**. SeLEAS emphasizes autonomic seizures; POLE emphasizes photic-induced visual seizures. (manokaran2024the2022international pages 2-4, manokaran2024the2022international pages 4-5, wirrell2025epilepsysyndromesclassification. pages 6-7) | Differential concepts: SeLEAS; POLE | Moderate: directly supported at syndrome-classification level; detailed bedside distinguishing criteria were not fully available. |
| treatment | No COVE-specific randomized trials or precision therapies were retrieved. As a self-limited focal epilepsy, treatment is generally antiseizure-medication based when needed, but the available context does not support a syndrome-specific preferred drug claim. (manokaran2024the2022international pages 4-5, wirrell2025epilepsysyndromesclassification. pages 6-7) | NCIT suggestions: Anticonvulsant therapy; Electroencephalography; Magnetic Resonance Imaging | Limited: evidence supports management context but not a definitive drug algorithm from retrieved sources. |
| cognition/quality of life | The ILAE update emphasizes that the old term **benign** was replaced because self-limited focal epilepsies can still have **cognitive and behavioral comorbidities**; however, COVE-specific QoL metrics were not retrieved. (manokaran2024the2022international pages 4-5) | HPO suggestions: Behavioral abnormality; Neurodevelopmental abnormality (generic only) | Moderate for possibility of comorbidity at syndrome-group level; limited for COVE-specific rates/severity. |
| imaging | MRI is part of the workup for childhood epilepsy syndromes when indicated, but no characteristic COVE-specific structural imaging biomarker was established in the retrieved evidence. Adjacent GRIN2A MRI findings are not COVE-specific. (manokaran2024the2022international pages 4-5, thompsonlake2024perisylvianandhippocampal pages 1-2, thompsonlake2024perisylvianandhippocampal pages 5-6) | Brain MRI | Moderate for MRI role; low for disease-specific imaging signature. |
| omics/models unavailable | No COVE-specific **transcriptomic, proteomic, metabolomic, lipidomic, epigenomic, single-cell, spatial transcriptomic, or dedicated animal/cellular model** evidence was identified in the retrieved sources. Generic epilepsy models exist, but they are not disease-specific for COVE. (rubio2024classificationofcurrent pages 1-2) | GO/CL/model ontology: none established for COVE | Strong negative statement for retrieved evidence scope; absence here should be interpreted as “not found in available context,” not proof of nonexistence. |


*Table: This table condenses the evidence-supported knowledge base fields for Childhood Occipital Visual Epilepsy using only retrieved context. It highlights what is established, what can be mapped provisionally to ontologies, and where the evidence is currently limited or unavailable.*

## 1. Disease information

### Definition and classification

COVE is an electroclinical epilepsy syndrome whose defining cluster comprises childhood onset, focal sensory visual seizures, and occipital epileptiform EEG findings. The 2024 ILAE update places it among four childhood self-limited focal epilepsies and states that its name reflects “occipital semiology and EEG findings.” Childhood-onset syndromes in this framework generally begin from ages 2–12 years. (manokaran2024the2022international pages 4-5)

**Current and historical names**

- Childhood occipital visual epilepsy (COVE)—current ILAE term.
- Idiopathic childhood occipital epilepsy–Gastaut type.
- Gastaut-type childhood occipital epilepsy.
- Late-onset benign childhood occipital epilepsy.
- Benign occipital epilepsy of childhood, late-onset type.

The authoritative terminology table explicitly maps COVE to “late onset (benign) occipital epilepsy” and “idiopathic childhood occipital epilepsy–Gastaut type.” “Benign” has been replaced by “self-limited,” because spontaneous remission does not guarantee absence of cognitive, behavioral, or psychosocial morbidity. (manokaran2024the2022international pages 2-4, manokaran2024the2022international pages 4-5)

### Identifiers

- **MONDO:** no confidently verified COVE-specific MONDO identifier was found. Do not populate one without direct MONDO confirmation.
- **OMIM/Orphanet:** no dedicated syndrome-specific entry was verified in the retrieved evidence.
- **ICD-10:** usually coded under focal/localization-related epilepsy, selected according to intractability and status-epilepticus qualifiers; there is no verified COVE-specific code.
- **ICD-11:** classified within focal epilepsy/epilepsy syndromes rather than by a unique verified COVE code.
- **MeSH:** “Epilepsy, Occipital Lobe” is the closest disease concept; a separate COVE-specific heading was not verified.

These are aggregated disease-level findings from classifications and published cohorts—not individual EHR-derived observations.

## 2. Etiology

### Causal and risk factors

COVE is currently best regarded as a **presumed genetic epilepsy with complex or multifactorial inheritance**, not a single-gene disorder. The 2024 review specifically places COVE and photosensitive occipital lobe epilepsy among focal syndromes with presumed complex inheritance. No gene has sufficient syndrome-specific evidence to be annotated as a definitive COVE causal gene. (manokaran2024the2022international pages 4-5)

A family history of epilepsy or migraine may occur in historical cohorts, but penetrance, recurrence risk, susceptibility loci, founder variants, and carrier frequency remain undefined. Reported GABA-receptor or other epilepsy-gene variants in families with occipital epilepsy should not automatically be equated with classic COVE because structural, familial focal, photosensitive, and neurodevelopmental occipital epilepsies are heterogeneous.

### Environmental, protective, and gene–environment factors

No toxin, infection, diet, lifestyle, occupational exposure, or immune trigger is established as a cause of COVE. Sleep deprivation, illness, or missed medication can lower seizure threshold in epilepsy generally but are not proven causes of this syndrome. Visually induced seizures instead suggest **photosensitive occipital lobe epilepsy**, an important separate syndrome. No validated genetic or environmental protective factors or COVE-specific gene–environment interactions were identified.

## 3. Phenotypes

### Core manifestations

1. **Elementary visual hallucinations**—positive visual phenomena such as small multicolored circles or spots, commonly moving or multiplying in a visual hemifield. These are focal sensory visual seizures, abrupt, stereotyped, and usually brief. Suggested HPO: **Visual hallucination**, **Focal sensory seizure**, **Abnormality of vision**.
2. **Transient ictal blindness or visual loss**—a negative visual symptom that may involve a field or the whole visual scene. Suggested HPO: **Transient visual loss**, **Blindness**, **Visual field defect**.
3. **Eye or head deviation**—reflecting spread from visual cortex to adjacent cortical networks. Suggested HPO: **Versive seizure**, **Abnormal eye movement**.
4. **Impaired awareness, hemiclonic, or focal-to-bilateral tonic–clonic seizure**—downstream manifestations when an occipital discharge propagates. Suggested HPO: **Focal impaired awareness seizure**, **Focal to bilateral tonic-clonic seizure**.
5. **Ictal or postictal headache, nausea, or vomiting**—clinically important because visual aura plus headache may be mistaken for migraine. Suggested HPO: **Headache**, **Nausea and vomiting**.

Current reviews succinctly characterize COVE seizures as sensory visual symptoms with elementary visual phenomena; occipital seizures can manifest as hallucinations or blindness. (wirrell2025epilepsysyndromesclassification. pages 6-7)

### Timing, severity, and progression

Onset is pediatric, typically school age in the historical Gastaut phenotype. Attacks are episodic rather than progressive. Seizure frequency varies substantially: some patients have few attacks, whereas others have frequent seizures requiring treatment. Baseline neurological examination, development, and routine structural imaging are generally expected to be normal in a prototypical self-limited syndrome; developmental regression, persistent neurological deficits, or major MRI abnormalities should prompt reassessment.

### Quality of life

Transient blindness, hallucinations, impaired awareness, headache, and tonic–clonic spread can disrupt school, sports, bathing, travel, and other safety-sensitive activities. Anxiety and diagnostic confusion with migraine may add burden. Although “self-limited,” these epilepsies can have cognitive or behavioral comorbidity; no COVE-specific EQ-5D, PedsQL, PROMIS, or neuropsychological prevalence estimates were found. The ILAE deliberately abandoned “benign” because self-limited syndromes can still carry such morbidity. (manokaran2024the2022international pages 4-5)

## 4. Genetic and molecular information

No definitive **causal gene, HGNC locus, pathogenic variant spectrum, chromosomal abnormality, modifier gene, epigenetic signature, allele frequency, or somatic mosaic mechanism** is established for classic COVE. Therefore:

- A COVE knowledge-base entry should not list **GRIN2A** as causal. GRIN2A is strongly associated with epilepsy–aphasia syndromes, particularly speech-language impairment, Landau–Kleffner syndrome, and rolandic-spectrum epilepsy—not specifically COVE. A 2024 GRIN2A MRI study involved only 10 affected individuals from three families and found bilateral occipital cortical-thickness differences, but its phenotype was epilepsy–aphasia syndrome. This is mechanistically adjacent evidence, not validation of a COVE gene. (thompsonlake2024perisylvianandhippocampal pages 1-2, thompsonlake2024perisylvianandhippocampal pages 5-6)
- In that GRIN2A study, pathogenic-variant carriers had greater left pars-opercularis thickness than controls, with partial η²=0.37, and corrected whole-brain analysis retained bilateral lateral-occipital thickness increases. The authors’ abstract states: “Pathogenic variants in GRIN2A are associated with a spectrum of epilepsy-aphasia syndromes.” These data should be stored under GRIN2A-related epilepsy–aphasia, not COVE. Published April 2024; DOI URL: https://doi.org/10.1212/NXG.0000000000200129. (thompsonlake2024perisylvianandhippocampal pages 1-2, thompsonlake2024perisylvianandhippocampal pages 5-6)

Clinical genetic testing is consequently not routine for an otherwise typical, normally developing child with classic COVE. It becomes appropriate when onset or course is atypical, development is impaired, seizures are drug-resistant, MRI is abnormal, examination is abnormal, or there is a strong multigenerational phenotype.

## 5. Environmental information

No COVE-specific association with pollution, radiation, heavy metals, smoking, alcohol, diet, exercise, infection, autoimmunity, or occupational exposure was identified. Photosensitivity is not a defining environmental cause of COVE: consistent precipitation by patterned light, television, or video games favors POLE. General seizure-safety measures—adequate sleep, adherence to medication, avoiding individual triggers—reduce provoked attacks but do not prevent the syndrome from arising.

## 6. Mechanism and pathophysiology

### Syndrome-level causal chain

**Upstream predisposition of uncertain polygenic basis → age-dependent hyperexcitability/synchronization in occipital cortical networks → focal ictal discharge in primary or associative visual cortex → positive visual phenomena or transient blindness → propagation to parietal, temporal, frontal, or bilateral networks → eye/head deviation, impaired awareness, motor seizure, or bilateral tonic–clonic activity → postictal headache/nausea.**

The relevant organ is brain; tissue is cerebral cortex; principal cell classes are glutamatergic cortical projection neurons and GABAergic interneurons. This is an electroclinical model rather than a proven COVE-specific molecular pathway. No direct evidence establishes mTOR, PI3K–AKT, Wnt, MAPK, immune, oxidative-stress, mitochondrial, or metabolic pathology in classic COVE.

**Suggested ontology mappings**

- GO biological process: regulation of membrane potential; neuronal action potential; chemical synaptic transmission; visual perception; regulation of synaptic transmission.
- GO cellular component: neuron projection; synapse; postsynaptic membrane; axon initial segment.
- CL: neuron; glutamatergic neuron; GABAergic neuron; cortical pyramidal neuron.

No disease-specific transcriptomic, proteomic, metabolomic, lipidomic, methylomic, single-cell, spatial-transcriptomic, CRISPR-screen, or integrated multi-omic study was found. Generic chemically induced epilepsy models are insufficiently specific: one retrieved rat penicillin model used cortical epileptiform induction, but it does not reproduce the age dependence, visual semiology, EEG signature, or spontaneous remission of COVE. (rubio2024classificationofcurrent pages 1-2)

## 7. Anatomical structures affected

- **Organ/system:** brain and central nervous system.
- **Primary site:** occipital lobe and visual cortex; suggested UBERON: brain, cerebral cortex, occipital lobe, primary visual cortex.
- **Networks:** extrastriate visual association cortex and propagation pathways into parietal, temporal, and frontal regions.
- **Cells:** cortical excitatory projection neurons and inhibitory interneurons; these are inferred network participants rather than histologically demonstrated targets.
- **Subcellular structures:** neuronal membrane, ion channels, synapses, and axons are generic electrophysiological compartments; no COVE-specific protein defect is established.
- **Lateralization:** seizures may begin in either occipital hemisphere. Visual symptoms can be lateralized to a hemifield; EEG abnormalities may be unilateral, bilateral, or shift in predominance. Fixed unilateral deficits are atypical and raise concern for structural disease.

## 8. Temporal development

COVE starts in childhood, usually with sudden, brief, recurrent visual seizures. It is episodic and nondegenerative. Current expert review states that most cases remit in adolescence, although a small subset has persistent seizures. (wirrell2025epilepsysyndromesclassification. pages 6-7)

There are no accepted early/intermediate/advanced stages. A practical temporal framework is: onset and diagnostic characterization; active seizure period; treatment-controlled or spontaneous remission; and, rarely, persistent epilepsy. Developmental regression or an increasingly diffuse sleep-activated EEG pattern is not expected and warrants evaluation for developmental/epileptic encephalopathy with spike-wave activation in sleep or another diagnosis.

## 9. Inheritance and population

Reliable population-based incidence and prevalence per 100,000 are not available from the retrieved evidence. COVE is substantially less common than self-limited epilepsy with centrotemporal spikes and self-limited epilepsy with autonomic seizures. Published samples are generally small referral-center cohorts, which limits precise sex ratios, ethnic comparisons, geographic variation, and outcome estimates.

Inheritance is presumed **complex/polygenic**, with incomplete and unquantified penetrance and variable expression. Anticipation, founder effects, consanguinity effects, carrier frequency, and germline mosaic recurrence have not been established. No robust sex predilection or ancestry-specific enrichment should be entered without direct cohort evidence.

## 10. Diagnostics

### Clinical and EEG diagnosis

Diagnosis requires a stereotyped occipital seizure phenotype and supportive EEG. The ILAE framework distinguishes:

- **Mandatory features:** features that must be present.
- **Alerts:** unusual findings that require diagnostic reconsideration and further investigation but do not alone exclude the syndrome.
- **Exclusionary features:** findings incompatible with the syndrome. (manokaran2024the2022international pages 2-4)

For COVE, practical mandatory elements are childhood-onset focal sensory visual seizures and an EEG compatible with occipital epilepsy. EEG should include wakefulness, eye opening/closure, sleep or sleep deprivation, and intermittent photic stimulation. Interictal recordings commonly show posterior/occipital spikes or spike-wave discharges, often enhanced by eye closure or elimination of fixation; ictal EEG begins in an occipital region. A normal short routine EEG does not exclude epilepsy, so prolonged or video EEG can be useful.

### Imaging and other testing

Brain MRI with an epilepsy protocol is appropriate, particularly at first presentation or where the phenotype is incomplete, to exclude occipital cortical dysplasia, tumor, vascular lesion, injury, or other structural cause. A causal structural lesion argues for structural occipital lobe epilepsy rather than classic COVE. Routine blood, urine, CSF, biopsy, PET, SPECT, or metabolic testing is not diagnostic in typical COVE and should be driven by clinical red flags.

### Differential diagnosis

- **Migraine with visual aura:** usually gradual evolution over minutes, zig-zag/scintillating or achromatic patterns, longer duration, and migraine sequence; COVE phenomena are sudden, brief, stereotyped, often colored and circular.
- **SeLEAS/Panayiotopoulos syndrome:** prominent autonomic features, especially vomiting, pallor, cardiorespiratory change, and often prolonged nocturnal seizures; EEG is often multifocal without consistent localization. (wirrell2025epilepsysyndromesclassification. pages 6-7)
- **POLE:** visual seizures consistently induced by visual stimuli or photic stimulation. The ILAE explicitly distinguishes POLE by photic-induced focal sensory visual seizures. (manokaran2024the2022international pages 4-5, wirrell2025epilepsysyndromesclassification. pages 6-7)
- Structural occipital epilepsy, posterior reversible encephalopathy, stroke, tumor, malformation, infection, and metabolic disease.
- Syncope, psychogenic nonepileptic events, retinal/ophthalmologic disease, and visual release phenomena.

### Genetic and omics testing

WES/WGS, epilepsy panels, CMA, mtDNA sequencing, karyotyping, FISH, and repeat-expansion testing are not first-line tests for a classic presentation. Consider trio WES/WGS or a broad epilepsy panel in atypical or severe cases rather than a COVE-specific panel, because no validated COVE gene set exists. No omics diagnostic has demonstrated clinical utility.

Population, newborn, carrier, or prenatal screening is not recommended. Cascade testing is relevant only if a separate pathogenic familial epilepsy variant is established.

## 11. Outcome and prognosis

The seizure prognosis is generally favorable: most cases remit in adolescence, but a minority persist. (wirrell2025epilepsysyndromesclassification. pages 6-7) No COVE-specific five- or ten-year survival decrement, mortality rate, life-expectancy reduction, or disease-attributable mortality estimate was found. Severe injury, status epilepticus, and sudden unexpected death in epilepsy are general epilepsy risks, but available evidence does not establish elevated syndrome-specific rates.

Normal long-term neurological function is expected in prototypical cases. Morbidity is chiefly recurrent seizures, temporary visual incapacity, headaches, medication adverse effects, psychosocial restriction, and occasional cognitive/behavioral concerns. Poorer-outcome signals include atypical onset, frequent generalized convulsions, drug resistance, developmental impairment, abnormal examination, persistent background slowing, multifocal/diffuse EEG abnormalities, or a causal MRI lesion—features that may indicate misclassification rather than severe COVE.

## 12. Treatment

### Strategy

Whether to start daily therapy is individualized. Observation can be reasonable after rare, brief seizures when diagnosis is secure, MRI and development are reassuring, and family risk tolerance permits. Treatment is more compelling for recurrent/frequent seizures, focal-to-bilateral tonic–clonic events, injury risk, prolonged attacks, substantial school/QoL effects, or family preference.

Commonly used focal-seizure antiseizure medicines include carbamazepine or oxcarbazepine, levetiracetam, and lamotrigine; valproate may be used when generalized seizure susceptibility is a concern. Historical evidence includes a small levetiracetam-monotherapy study, but no modern COVE-specific randomized comparative trial was retrieved. Therefore no single drug can be labeled evidence-based first-line specifically for COVE.

- **Sodium-channel blockers:** reduce high-frequency neuronal firing; adverse effects include dizziness, diplopia, rash, hyponatremia, and hematologic/hepatic reactions depending on agent.
- **Levetiracetam:** binds SV2A; behavioral irritability and somnolence are important pediatric adverse effects.
- **Lamotrigine:** sodium-channel modulation; requires slow titration because of serious rash risk.
- **Valproate:** broad-spectrum effects; weight gain, tremor, hepatic/pancreatic toxicity, thrombocytopenia, and major teratogenic risk require careful selection.

Suggested NCIT intervention concepts: **Anticonvulsant Therapy**, **Carbamazepine**, **Oxcarbazepine**, **Levetiracetam**, **Lamotrigine**, **Valproic Acid**, **Electroencephalography**, and **Magnetic Resonance Imaging**; exact NCIT codes should be validated in the terminology service.

A written rescue plan and benzodiazepine rescue medication may be indicated for a child with prolonged convulsive seizures. Education should cover water/heights safety, sleep, adherence, first aid, and school planning.

### Surgery and advanced therapeutics

Resective surgery is not a treatment for classic self-limited COVE. Drug-resistant “COVE” should trigger repeat video EEG and high-resolution MRI to seek a structural occipital focus; surgery may then apply to the structural epilepsy, not COVE itself. No gene therapy, cell therapy, ASO/siRNA, immune therapy, or syndrome-specific targeted drug is available.

The clinical-trial search found no COVE-specific interventional study. A generic wireless pediatric/adult EEG validation study, NCT05123469, does not constitute a COVE treatment trial.

## 13. Prevention

There is no established primary prevention because the causal predisposition is unknown and cannot currently be modified. Vaccination, antimicrobial prophylaxis, or environmental remediation has no COVE-specific role.

Secondary/tertiary prevention consists of prompt recognition, exclusion of structural disease, seizure treatment when indicated, adherence, adequate sleep, individualized avoidance of triggers, water/heights precautions, helmets only for selected injury risks, school rescue plans, and counseling about driving when age relevant. Routine newborn, population, carrier, prenatal, or preimplantation screening is not supported. Genetic counseling should explain that inheritance appears complex and that a precise recurrence percentage is unavailable unless another molecular diagnosis is found.

## 14. Other species and natural disease

No naturally occurring animal disorder has been validated as an orthologous COVE syndrome. Dogs and other mammals can develop focal visual/occipital seizures, but equivalence to the human age-dependent, self-limited electroclinical syndrome is unproven. Thus no NCBI Taxon, breed/VBO, orthologous causal gene, zoonotic transmission, or cross-species susceptibility annotation is warranted. COVE is noninfectious and nonzoonotic.

## 15. Model organisms

No dedicated mouse, rat, zebrafish, Drosophila, organoid, iPSC, knock-in, knockout, conditional, or humanized model recapitulates all defining COVE features. Generic cortical seizure models can study excitation/inhibition, occipital propagation, and antiseizure pharmacology but lack syndrome specificity. For example, the retrieved penicillin rat model produced dose-dependent cortical epileptiform activity but did not model childhood onset, elementary visual hallucinations, spontaneous adolescent remission, or complex inheritance. (rubio2024classificationofcurrent pages 1-2)

A useful future model would need: age-restricted occipital seizures; visual behavioral correlates; posterior EEG discharges modulated by fixation/eye closure; normal baseline development and anatomy; polygenic susceptibility; and spontaneous remission at maturation.

## Recent developments and expert assessment

1. **Nosology is the major recent advance.** The ILAE replaced the ambiguous “benign/Gastaut-type” terminology with the descriptive COVE label and separated it from autonomic and photosensitive occipital syndromes. The pediatric update was published February 2024; DOI: https://doi.org/10.1007/s13312-024-3115-2. (manokaran2024the2022international pages 2-4, manokaran2024the2022international pages 4-5)
2. **Current expert framing emphasizes syndrome utility.** A 2025 review states that syndrome identification guides high-yield investigation, treatment selection, and prognosis. Its exact abstract wording is: epilepsy syndromes are associated with “a characteristic cluster of clinical and EEG features, often supported by specific etiologic findings.” DOI: https://doi.org/10.1002/epi4.70026. For COVE, that utility is mainly electroclinical because a specific etiology has not been established. (wirrell2025epilepsysyndromesclassification. pages 6-7)
3. **Molecular precision remains an unmet need.** Recent GRIN2A imaging and broad pediatric-genetics work should not be overgeneralized to COVE. The available evidence supports careful phenotyping before sequencing and strict gene–disease validity standards. (thompsonlake2024perisylvianandhippocampal pages 1-2, thompsonlake2024perisylvianandhippocampal pages 5-6)

## Evidence gaps for knowledge-base curation

High-priority gaps are: a verified MONDO/Orphanet mapping; contemporary population-based incidence and prevalence; prospective cohorts using 2022 ILAE criteria; standardized seizure-frequency and QoL outcomes; controlled medication comparisons; well-powered genomic studies restricted to rigorously phenotyped COVE; and COVE-specific network, single-cell, and developmental models. Until those data exist, the safest curation is **syndrome-level electroclinical disease; presumed complex inheritance; no definitive causal gene; no molecular biomarker; favorable but not universally remitting course**.

References

1. (manokaran2024the2022international pages 2-4): Ranjith Kumar Manokaran, Suvasini Sharma, and Rajesh Ramachandrannair. The 2022 international league against epilepsy classification and definition of childhood epilepsy syndromes: an update for pediatricians. Indian Pediatrics, 61:179-183, Feb 2024. URL: https://doi.org/10.1007/s13312-024-3115-2, doi:10.1007/s13312-024-3115-2. This article has 25 citations and is from a peer-reviewed journal.

2. (manokaran2024the2022international pages 4-5): Ranjith Kumar Manokaran, Suvasini Sharma, and Rajesh Ramachandrannair. The 2022 international league against epilepsy classification and definition of childhood epilepsy syndromes: an update for pediatricians. Indian Pediatrics, 61:179-183, Feb 2024. URL: https://doi.org/10.1007/s13312-024-3115-2, doi:10.1007/s13312-024-3115-2. This article has 25 citations and is from a peer-reviewed journal.

3. (wirrell2025epilepsysyndromesclassification. pages 6-7): Elaine C. Wirrell, Nicola Specchio, Rima Nabbout, Phillip L. Pearl, and Kate Riney. Epilepsy syndromes classification. Epilepsia open, Mar 2025. URL: https://doi.org/10.1002/epi4.70026, doi:10.1002/epi4.70026. This article has 6 citations and is from a peer-reviewed journal.

4. (thompsonlake2024perisylvianandhippocampal pages 1-2): Daisy G.Y. Thompson-Lake, Frederique J. Liegeois, Ruth O. Braden, Graeme D. Jackson, Samantha J. Turner, Lottie Morison, Michael Hildebrand, Ingrid E. Scheffer, and Angela T. Morgan. Perisylvian and hippocampal anomalies in individuals with pathogenic <i>grin2a</i> variants. Neurology Genetics, Apr 2024. URL: https://doi.org/10.1212/nxg.0000000000200129, doi:10.1212/nxg.0000000000200129. This article has 2 citations.

5. (thompsonlake2024perisylvianandhippocampal pages 5-6): Daisy G.Y. Thompson-Lake, Frederique J. Liegeois, Ruth O. Braden, Graeme D. Jackson, Samantha J. Turner, Lottie Morison, Michael Hildebrand, Ingrid E. Scheffer, and Angela T. Morgan. Perisylvian and hippocampal anomalies in individuals with pathogenic <i>grin2a</i> variants. Neurology Genetics, Apr 2024. URL: https://doi.org/10.1212/nxg.0000000000200129, doi:10.1212/nxg.0000000000200129. This article has 2 citations.

6. (wirrell2025epilepsysyndromesclassification. pages 5-6): Elaine C. Wirrell, Nicola Specchio, Rima Nabbout, Phillip L. Pearl, and Kate Riney. Epilepsy syndromes classification. Epilepsia open, Mar 2025. URL: https://doi.org/10.1002/epi4.70026, doi:10.1002/epi4.70026. This article has 6 citations and is from a peer-reviewed journal.

7. (rubio2024classificationofcurrent pages 1-2): Carmen Rubio, Héctor Romo-Parra, Alejandro López-Landa, and Moisés Rubio-Osornio. Classification of current experimental models of epilepsy. Brain Sciences, 14:1024, Oct 2024. URL: https://doi.org/10.3390/brainsci14101024, doi:10.3390/brainsci14101024. This article has 14 citations.

## Artifacts

- [Edison artifact artifact-00](Childhood_Occipital_Visual_Epilepsy-deep-research-falcon_artifacts/artifact-00.md)