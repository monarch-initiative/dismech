---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T00:42:17.719572'
end_time: '2026-07-31T00:52:42.472394'
duration_seconds: 624.75
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Say-Barber-Biesecker-Young-Simpson Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 28
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Say-Barber-Biesecker-Young-Simpson_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Say-Barber-Biesecker-Young-Simpson Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Say-Barber-Biesecker-Young-Simpson Syndrome** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
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
- **Disease Name:** Say-Barber-Biesecker-Young-Simpson Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Say-Barber-Biesecker-Young-Simpson Syndrome** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Say–Barber–Biesecker–Young–Simpson syndrome: disease-characteristics report

## Executive summary

Say–Barber–Biesecker–Young–Simpson syndrome (SBBYSS) is an ultra-rare, congenital, multisystem Mendelian chromatinopathy caused by a heterozygous pathogenic variant in **KAT6B**, usually arising *de novo*. It is best regarded as one part of a continuous **KAT6B-related disorder spectrum** that also includes genitopatellar syndrome (GPS) and intermediate phenotypes. Hallmarks are developmental delay/intellectual disability, hypotonia, blepharophimosis and ptosis, mask-like facial appearance, long thumbs/great toes, feeding difficulties, patellar abnormalities, and variably cardiac, genital, renal, thyroid, auditory, ocular, palatal, and cerebral anomalies. There is no curative or approved molecular therapy; current care is multidisciplinary and complication-directed. A major 2024 advance was proof-of-concept rescue of behavioral and molecular abnormalities in human cells and *Kat6b*-haploinsufficient mice by increasing histone acetylation, but this has not yet established efficacy or safety in patients. (bergamasco2024increasinghistoneacetylation pages 1-2, zhang2020furtherdelineationof pages 1-2, magdalena2023clinicalheterogeneityof pages 1-2)

The principal evidence is summarized below.

| Domain | Key finding / statistic | Evidence type and cohort | Source / date / DOI URL |
|---|---|---|---|
| Disease identity / identifiers | Say-Barber-Biesecker-Young-Simpson syndrome (SBBYSS), a variant of Ohdo syndrome; OMIM 603736; Orphanet ORPHA:3047; part of the broader KAT6B disorder spectrum with overlap with genitopatellar syndrome (GPS, OMIM 606170) (zhang2020furtherdelineationof pages 1-2, shin2021aneonatewith pages 1-3, magdalena2023clinicalheterogeneityof pages 1-2) | Human disease descriptions and cohort review | Zhang et al., *Genetics in Medicine*, 2020. https://doi.org/10.1038/s41436-020-0811-8 ; Shin et al., *J Genet Med*, 2021. https://doi.org/10.5734/JGM.2021.18.2.147 ; Magdalena et al., *Mol Genet Genomic Med*, 2023. https://doi.org/10.1002/mgg3.2265 |
| Synonyms / nomenclature | Also called “SBBYSS,” “SBBYS variant of Ohdo syndrome,” “Say-Barber/Biesecker/Young-Simpson syndrome”; recent literature increasingly uses “KAT6B-related disorders” or “KAT6B spectrum disorders” because GPS/SBBYSS boundaries blur (zhang2020furtherdelineationof pages 1-2, magdalena2023clinicalheterogeneityof pages 1-2) | Human reviews and cohort papers | Zhang et al., 2020. https://doi.org/10.1038/s41436-020-0811-8 ; Magdalena et al., 2023. https://doi.org/10.1002/mgg3.2265 |
| Epidemiology / rarity | Ultra-rare; 2025 review cited 152 molecularly confirmed KAT6B cases globally (86 SBBYSS, 33 GPS, 33 intermediate); prevalence described as <1/million in review text (maglione2025phenotypiccharacterizationof pages 6-7, maglione2025phenotypiccharacterizationof pages 2-2) | Literature review / compiled human cases | Maglione et al., *Am J Med Genet A*, 2025. https://doi.org/10.1002/ajmg.a.64100 |
| Inheritance | Autosomal dominant; most pathogenic variants are de novo; rare inherited mild familial cases have been reported, including maternal transmission of a splice defect in the Zhang cohort (zhang2020furtherdelineationof pages 1-2, zhang2020furtherdelineationof pages 7-8, shin2021aneonatewith pages 1-3, davarnia2024denovokat6b pages 1-2) | Human cohort + case reports | Zhang et al., 2020. https://doi.org/10.1038/s41436-020-0811-8 ; Shin et al., 2021. https://doi.org/10.5734/JGM.2021.18.2.147 ; Davarnia et al., 2024. https://doi.org/10.1186/s13256-023-04237-w |
| Core phenotype | Hallmark SBBYSS features include blepharophimosis/ptosis, mask-like facies, long thumbs/great toes, developmental delay/intellectual disability, hypotonia, feeding problems, patellar anomalies, congenital heart disease, thyroid dysfunction, hearing loss, genital anomalies (lundsgaard2017denovokat6b pages 1-2, shin2021aneonatewith pages 1-3, magdalena2023clinicalheterogeneityof pages 1-2) | Human case reports and cohort summaries | Lundsgaard et al., *Mol Syndromol*, 2017. https://doi.org/10.1159/000452258 ; Shin et al., 2021. https://doi.org/10.5734/JGM.2021.18.2.147 ; Magdalena et al., 2023. https://doi.org/10.1002/mgg3.2265 |
| Major phenotype frequencies (Zhang 2020 cohort) | Cleft/high-arched palate in 14/32 (44%); patellar anomalies in 8/32 (25%); long thumbs and/or long great toes in 12/15 SBBYSS individuals (80%); other digital anomalies in 12/32 (38%); congenital heart defects in 15/32 (47%) (zhang2020furtherdelineationof pages 4-5) | Human cohort, 32 previously unreported individuals plus literature review | Zhang et al., 2020. https://doi.org/10.1038/s41436-020-0811-8 |
| Additional phenotype burden (Zhang 2020) | Feeding difficulties / reflux / emesis present in 9 individuals; intestinal malrotation highlighted as a serious but underrecognized complication; genital anomalies frequent, especially in GPS; optic nerve hypoplasia and broader cerebral anomalies more common than initially recognized (zhang2020furtherdelineationof pages 4-5, zhang2020furtherdelineationof pages 1-2, zhang2020furtherdelineationof pages 7-8) | Human cohort review | Zhang et al., 2020. https://doi.org/10.1038/s41436-020-0811-8 |
| Variant spectrum | Previously published KAT6B spectrum included 56 variants: 22 substitutions, 22 small intragenic deletions, 10 small intragenic duplications, 2 deletion-insertions; Zhang added 24 novel variants including 14 frameshift, 7 nonsense, 1 missense, 2 intronic/splicing; most variants cluster in exon 18 (zhang2020furtherdelineationof pages 1-2, zhang2020furtherdelineationof pages 7-8) | Human molecular cohort / allelic series | Zhang et al., 2020. https://doi.org/10.1038/s41436-020-0811-8 |
| Genotype–phenotype regions | Variants causing GPS cluster in proximal exon 18, amino acids 1150–1515; in this region, phenotypes were GPS 60%, SBBYSS 19%, intermediate 19%; variants outside this region more often cause SBBYSS/intermediate phenotypes (zhang2020furtherdelineationof pages 7-8) | Human genotype–phenotype analysis | Zhang et al., 2020. https://doi.org/10.1038/s41436-020-0811-8 |
| Mechanistic model of alleles | More proximal variants may undergo nonsense-mediated decay (NMD) causing haploinsufficiency and milder disease; final/penultimate exon variants may escape NMD and produce truncated proteins with abnormal or dominant-negative effects; this remains partly unvalidated experimentally (bergamasco2024increasinghistoneacetylation pages 1-2, magdalena2023clinicalheterogeneityof pages 1-2) | Human mechanistic inference + translational review | Bergamasco et al., *J Clin Invest*, 2024. https://doi.org/10.1172/JCI167672 ; Magdalena et al., 2023. https://doi.org/10.1002/mgg3.2265 |
| Molecular function / complex biology | KAT6B is a highly conserved MYST-family histone acetyltransferase that regulates gene expression and functions in a multisubunit complex with BRPF1, ING5, and MEAF6; reported histone targets include H3K14, H3K23, and broader H2A/H2B/H3/H4/H1 acetylation in assays (zhang2020furtherdelineationof pages 1-2, zu2022brpf1kat6akat6bcomplexmolecular pages 4-6, bergamasco2024increasinghistoneacetylation pages 1-2) | Review + mechanistic translational study | Zhang et al., 2020. https://doi.org/10.1038/s41436-020-0811-8 ; Zu et al., *Cancers*, 2022. https://doi.org/10.3390/cancers14174068 ; Bergamasco et al., 2024. https://doi.org/10.1172/JCI167672 |
| 2023 Polish cohort | Six Polish patients with one known and five novel KAT6B variants; all had facial dysmorphism and developmental/speech delay; all but one had hypotonia, ocular anomalies, and long thumbs; knee defects were often milder than classic aplasia/agenesis, supporting broader spectrum classification (magdalena2023clinicalheterogeneityof pages 1-2, magdalena2023clinicalheterogeneityof pages 10-10) | Human case series, 6 patients | Magdalena et al., *Mol Genet Genomic Med*, 2023. https://doi.org/10.1002/mgg3.2265 |
| 2024 translational advance | In CRISPR-engineered human cells with SBBYSS mutations and Kat6b+/- mice, KAT6B deficiency reduced H3K9 acetylation; mice showed learning, memory, and social deficits; valproic acid and acetyl-L-carnitine increased histone acetylation, partially normalized gene expression, improved sociability, and ALCAR restored learning/memory (bergamasco2024increasinghistoneacetylation pages 1-2, bergamasco2024increasinghistoneacetylation pages 15-17) | Human cell lines + mouse model | Bergamasco et al., *J Clin Invest*, 2024. https://doi.org/10.1172/JCI167672 |
| Anatomical / cell-level mechanism | Kat6b is highly expressed in developing brain and adult subventricular zone; deficiency impairs neural stem-cell self-renewal and neuronal differentiation, reduces ventricular-zone proliferation, cortical plate size, cortical layer V pyramidal neurons, and interneurons (bergamasco2024increasinghistoneacetylation pages 1-2, lundsgaard2017denovokat6b pages 1-2, zu2022brpf1kat6akat6bcomplexmolecular pages 4-6) | Mouse / review / human case contextualization | Bergamasco et al., 2024. https://doi.org/10.1172/JCI167672 ; Lundsgaard et al., 2017. https://doi.org/10.1159/000452258 ; Zu et al., 2022. https://doi.org/10.3390/cancers14174068 |
| Diagnostics | Molecular diagnosis is typically achieved by NGS/WES or targeted sequencing of KAT6B; chromosomal microarray/karyotype can be normal in affected individuals; if a blepharophimosis syndrome or SBBYSS is suspected, KAT6B sequencing is recommended (lundsgaard2017denovokat6b pages 1-2, shin2021aneonatewith pages 1-3) | Human diagnostic case reports | Lundsgaard et al., 2017. https://doi.org/10.1159/000452258 ; Shin et al., 2021. https://doi.org/10.5734/JGM.2021.18.2.147 |
| Surveillance / management | Suggested baseline/routine evaluations include brain MRI and seizure surveillance, ophthalmology, periodic hearing exams, thyroid function testing, echocardiogram, renal ultrasound, and monitoring for contractures/spine anomalies and intestinal malrotation; management is multidisciplinary and symptomatic (zhang2020furtherdelineationof pages 7-8, shin2021aneonatewith pages 1-3, davarnia2024denovokat6b pages 1-2) | Human cohort recommendations + case management | Zhang et al., 2020. https://doi.org/10.1038/s41436-020-0811-8 ; Shin et al., 2021. https://doi.org/10.5734/JGM.2021.18.2.147 ; Davarnia et al., 2024. https://doi.org/10.1186/s13256-023-04237-w |
| Prognosis / course | Congenital onset is typical; developmental delay persists; some severe GPS-spectrum cases die in infancy; Zhang reported 3 infant deaths in GPS due to pulmonary hypoplasia/renal disease, prematurity with multiorgan complications, and influenza H1N1 infection (zhang2020furtherdelineationof pages 7-8, shin2021aneonatewith pages 1-3) | Human cohort + neonatal case | Zhang et al., 2020. https://doi.org/10.1038/s41436-020-0811-8 ; Shin et al., 2021. https://doi.org/10.5734/JGM.2021.18.2.147 |
| Biomarker / omics development | A 2023 study (not directly readable here) reported DNA methylation episignatures for KAT6A/KAT6B variants; later summaries indicate potential utility for variant interpretation/VUS support, but disease-specific performance metrics should be verified from the primary paper before database use (maglione2025phenotypiccharacterizationof pages 9-9, maglione2025phenotypiccharacterizationof pages 10-11) | Secondary reporting of omics biomarker work | Maglione et al., 2025 citing 2023 episignature work. https://doi.org/10.1002/ajmg.a.64100 |
| Evidence gaps | No disease-specific approved therapy; no human interventional trial identified for SBBYSS/KAT6B disorders in the current search; prevalence/incidence remain imprecise; penetrance and long-term adult natural history are poorly defined; some mechanistic claims (dominant-negative vs haploinsufficiency by region) remain incompletely validated (bergamasco2024increasinghistoneacetylation pages 1-2, zhang2020furtherdelineationof pages 7-8, magdalena2023clinicalheterogeneityof pages 1-2) | Synthesis of human cohort + translational evidence | Bergamasco et al., 2024. https://doi.org/10.1172/JCI167672 ; Zhang et al., 2020. https://doi.org/10.1038/s41436-020-0811-8 ; Magdalena et al., 2023. https://doi.org/10.1002/mgg3.2265 |


*Table: This table summarizes core evidence for Say-Barber-Biesecker-Young-Simpson syndrome within the KAT6B disorder spectrum, spanning identifiers, inheritance, phenotype frequencies, variant architecture, recent cohorts, translational studies, and current clinical practice gaps.*

## 1. Disease information

### Definition and classification

SBBYSS is an autosomal-dominant multiple-congenital-anomaly and neurodevelopmental syndrome caused by pathogenic variation in **KAT6B** at chromosome 10q22.2. It belongs to the Mendelian chromatinopathies because KAT6B is a MYST-family lysine acetyltransferase that regulates developmentally important transcription. Increasing clinical overlap with GPS has led experts to favor the umbrella terms **KAT6B-related disorder** or **KAT6B spectrum disorder**, while retaining SBBYSS and GPS as useful clinical subtypes. (zhang2020furtherdelineationof pages 1-2, magdalena2023clinicalheterogeneityof pages 1-2)

**Identifiers and nomenclature**

- **OMIM:** 603736.
- **Orphanet:** ORPHA:3047.
- **MONDO:** a dedicated MONDO mapping should be confirmed against the current MONDO release before database ingestion; the retrieved primary sources did not supply a MONDO identifier.
- **Related allelic disorder:** genitopatellar syndrome, OMIM 606170.
- **Synonyms:** SBBYSS; SBBYS syndrome; Say–Barber/Biesecker/Young–Simpson syndrome; Young–Simpson syndrome; Ohdo syndrome, SBBYS variant; Say–Barber–Biesecker–Young–Simpson variant of Ohdo syndrome.
- **ICD-10/ICD-11 and MeSH:** no disease-specific code or descriptor was established in the retrieved sources. Coding generally requires broader congenital-malformation, intellectual-disability, or genetic-syndrome categories.

The report is based primarily on **aggregated disease-level resources and published cohorts/case reports**, not patient-level EHR data. The most informative human series comprised 32 previously unreported molecularly confirmed individuals; a later compilation identified 152 published molecularly confirmed KAT6B-spectrum cases—86 SBBYSS, 33 GPS, and 33 intermediate. (maglione2025phenotypiccharacterizationof pages 6-7, zhang2020furtherdelineationof pages 1-2)

## 2. Etiology, risk, and protective factors

### Causal factor

The primary cause is a **germline heterozygous pathogenic KAT6B variant**. Most are truncating frameshift or nonsense variants; splice variants, rare missense variants, and larger loss-of-function alleles also occur. Zhang et al. catalogued 56 previously published variants and added 24: 14 frameshift, seven nonsense, one missense, and two intronic variants predicted to alter splicing. Most clustered in exon 18. (zhang2020furtherdelineationof pages 1-2, zhang2020furtherdelineationof pages 7-8)

### Risk factors

- **Genetic:** presence of a pathogenic KAT6B allele is the decisive risk factor. Most cases are sporadic and *de novo*, although rare mildly affected transmitting parents and multigenerational families demonstrate that inherited disease occurs. (zhang2020furtherdelineationof pages 1-2, zhang2020furtherdelineationof pages 7-8)
- **Parental age, sex, ancestry, consanguinity:** no reproducible disease-specific associations are established.
- **Environmental, infectious, toxic, lifestyle, or occupational risks:** none are known to cause SBBYSS.
- **Family history:** usually absent, but becomes important where a parent is mildly affected or mosaic.

### Protective factors and gene–environment interaction

No validated protective allele, modifier gene, diet, lifestyle intervention, or environmental exposure is known to prevent disease or reduce penetrance. Because the causal lesion acts during embryonic development, ordinary postnatal lifestyle modification cannot prevent the congenital syndrome. Acetyl-CoA availability and drugs affecting acetylation could theoretically modify downstream chromatin states, but this remains experimental rather than an established gene–environment interaction. The 2024 mouse study supports biochemical modifiability after birth but does not prove a human protective effect. (bergamasco2024increasinghistoneacetylation pages 15-17, bergamasco2024increasinghistoneacetylation pages 1-2)

## 3. Phenotypes

SBBYSS is recognizable at birth, but expression is variable and boundaries with GPS are imperfect. In the 2023 Polish series, all six patients had facial dysmorphism and developmental/speech delay; five of six had hypotonia, ocular abnormalities, and long thumbs. Knee abnormalities ranged from dysplasia and recurrent dislocation to subluxation rather than uniformly severe patellar agenesis. (magdalena2023clinicalheterogeneityof pages 1-2)

### Core phenotype map

| Domain | Manifestation, onset/course, and frequency evidence | Suggested HPO terms |
|---|---|---|
| Neurodevelopment | Global developmental delay and variable intellectual disability begin in infancy/childhood and are chronic. Speech is often disproportionately delayed; autism-like behavior, poor eye contact, ADHD traits, and seizures occur in subsets. | Global developmental delay (HP:0001263); Intellectual disability (HP:0001249); Delayed speech and language development; Autistic behavior; Seizure |
| Neuromuscular | Generalized hypotonia is usually congenital or infantile and contributes to delayed milestones and feeding problems. Contractures may occur, especially toward the GPS end of the spectrum. | Hypotonia (HP:0001252); Joint contracture |
| Craniofacial/ocular | Blepharophimosis, ptosis, mask-like immobile face, bulbous/tubular nose, broad nasal bridge, long philtrum, thin upper lip, micro/retrognathia, lacrimal-duct anomalies, strabismus, refractive errors, and optic-nerve hypoplasia. | Blepharophimosis (HP:0000581); Ptosis (HP:0000508); Mask-like facies; Bulbous nose; Lacrimal duct stenosis; Optic nerve hypoplasia |
| Skeletal/digital | Long thumbs/great toes are characteristic; patellar hypoplasia, agenesis, delayed ossification or displacement, scoliosis, clubfoot, hip/knee contractures, polydactyly, syndactyly, and other digital anomalies vary. | Long thumb; Long great toe; Patellar hypoplasia; Absent patella; Scoliosis; Clubfoot; Polydactyly |
| Feeding/GI/airway | Neonatal or infant feeding difficulty, reflux, recurrent emesis, constipation, laryngomalacia and respiratory problems occur. Intestinal malrotation is uncommon but potentially fatal. | Feeding difficulties; Gastroesophageal reflux; Constipation; Intestinal malrotation; Laryngomalacia |
| Cardiac | Congenital heart disease, especially atrial/ventricular septal defect, patent ductus arteriosus or patent foramen ovale. Arrhythmia is occasionally reported. | Atrial septal defect; Ventricular septal defect; Patent ductus arteriosus |
| Genitourinary | Cryptorchidism, micropenis, scrotal hypoplasia, hypospadias, testicular agenesis, clitoromegaly or labial hypoplasia; renal dysplasia/hypoplasia, hydronephrosis and reflux occur more often toward GPS. | Cryptorchidism (HP:0000028); Micropenis; Hypospadias; Renal hypoplasia; Hydronephrosis |
| Endocrine | Congenital or later hypothyroidism is recurrent and treatable. Delayed puberty/hypogonadism may occur. | Congenital hypothyroidism; Hypogonadism; Delayed puberty |
| Hearing/dental/palatal | Sensorineural or conductive hearing loss, delayed or absent/hypoplastic teeth, cleft or high-arched palate, and occasionally Pierre Robin sequence. | Sensorineural hearing impairment; Hypodontia; Delayed eruption of teeth; Cleft palate; High-arched palate |
| CNS imaging | Corpus-callosum agenesis/hypoplasia, microcephaly, altered myelination, and other cerebral anomalies, though MRI can be normal. | Agenesis of corpus callosum; Abnormality of cerebral white matter; Microcephaly |

In the 32-person Zhang cohort, cleft/high-arched palate occurred in **14/32 (44%)**, patellar abnormalities in **8/32 (25%)**, other digital anomalies in **12/32 (38%)**, and congenital heart defects in **15/32 (47%)**. Among clinically classified SBBYSS cases with available data, long thumbs and/or great toes occurred in **12/15 (80%)**. Feeding difficulty, reflux or recurrent emesis affected nine individuals. Published-series estimates must be interpreted cautiously because ascertainment, missingness, and subtype assignment differ. (zhang2020furtherdelineationof pages 4-5)

### Functional and quality-of-life effects

No validated SBBYSS-specific EQ-5D, SF-36, PROMIS, or natural-history quality-of-life dataset was found. Nevertheless, developmental and speech impairment, hypotonia, feeding dependence, hearing/vision loss, orthopedic abnormalities, behavioral problems, and congenital-organ disease can substantially limit communication, mobility, education, self-care, and independent living. A 14-year-old reported in 2024 required institutional support, physiotherapy, and speech therapy and lacked sphincter control, illustrating severe—but not universal—functional impact. (davarnia2024denovokat6b pages 1-2)

## 4. Genetic and molecular information

### Causal gene

- **Gene:** KAT6B, lysine acetyltransferase 6B.
- **Location:** chromosome 10q22.2.
- **Aliases:** MYST4, MORF; mouse ortholog *Kat6b*/*Querkopf* or *Qkf*.
- **Protein:** a nuclear chromatin-associated MYST-family acetyltransferase with NEMM, tandem PHD, catalytic MYST, acidic, and serine/methionine-rich regions. (bergamasco2024increasinghistoneacetylation pages 1-2, zhang2020furtherdelineationof pages 7-8)

### Variant architecture and consequence

Most clinically causal alleles are germline and heterozygous. Somatic KAT6B alterations reported in cancer are biologically distinct and do not define SBBYSS. Pathogenic germline truncating variants are expected to be absent or extremely rare in population databases; however, individual gnomAD frequencies should be checked against the precise transcript and genome build during clinical interpretation.

The prevailing allelic model is location dependent:

1. **Upstream truncating alleles** may trigger nonsense-mediated decay (NMD), reducing KAT6B dosage and causing haploinsufficiency.
2. **Penultimate/final-exon truncations** may escape NMD and produce abnormal truncated proteins, potentially exerting dominant-negative or altered-function effects.
3. This framework explains some genotype–phenotype differences but remains incompletely validated for individual mutant proteins. (bergamasco2024increasinghistoneacetylation pages 1-2, magdalena2023clinicalheterogeneityof pages 1-2)

Variants in proximal exon 18, amino acids approximately **1150–1515**, were associated in Zhang et al. with GPS in 60%, SBBYSS in 19%, and an intermediate phenotype in 19%. More distal variants—particularly beyond codon 1520—more often produce SBBYSS, while variants around codons 1208–1321 frequently produce GPS/intermediate disease. Genotype alone cannot reliably assign phenotype. (maglione2025phenotypiccharacterizationof pages 9-9, zhang2020furtherdelineationof pages 7-8)

Illustrative variants include **c.4943C>G, p.Ser1648Ter**, identified *de novo* by WES, and **c.5206C>T, p.Gln1736Ter**, a *de novo* exon-18 nonsense variant in a neonate with hypothyroidism, ASD, hearing loss, genital anomalies, and classic facies. (lundsgaard2017denovokat6b pages 1-2, shin2021aneonatewith pages 1-3)

### Modifier genes and chromosomal abnormalities

No validated clinical modifier gene or founder allele is known. Whole-gene deletions or larger copy-number changes may cause KAT6B haploinsufficiency, but classic SBBYSS is usually due to an intragenic sequence variant. Conventional karyotype and chromosomal microarray can therefore be normal. (shin2021aneonatewith pages 1-3, magdalena2023clinicalheterogeneityof pages 1-2)

### Epigenetic information

A KAT6A/KAT6B peripheral-blood DNA-methylation episignature was reported in 2023 and may help classify uncertain variants. It is a **downstream biomarker of chromatin-regulator dysfunction**, not the inherited causal alteration itself. Disease-specific sensitivity and specificity should be taken directly from the primary assay publication before clinical implementation; those metrics were not available in the retrievable text. (maglione2025phenotypiccharacterizationof pages 10-11, maglione2025phenotypiccharacterizationof pages 9-9)

## 5. Environmental information

No toxin, radiation exposure, diet, smoking, alcohol, exercise pattern, occupational exposure, or infectious agent is established as causal. SBBYSS is not contagious and has no zoonotic component. Environmental factors may influence ordinary health and complications—nutrition affects growth, infections can be more consequential in medically fragile children, and teratogenic valproate exposure is itself hazardous during pregnancy—but they do not explain the Mendelian syndrome.

## 6. Mechanism and pathophysiology

### Upstream causal chain

**Pathogenic KAT6B allele → reduced or abnormal KAT6B protein → deficient chromatin acetyltransferase activity and altered recruitment of the BRPF1–ING5/ING4–MEAF6 complex → reduced acetylation at developmentally important chromatin and abnormal gene expression → impaired neural progenitor proliferation/differentiation and disturbed craniofacial, skeletal, cardiac, genital, renal, thyroid and other organogenesis → congenital anomalies plus lifelong neurodevelopmental disability.** (bergamasco2024increasinghistoneacetylation pages 1-2, zhang2020furtherdelineationof pages 1-2, zu2022brpf1kat6akat6bcomplexmolecular pages 4-6)

KAT6B transfers acetyl groups from acetyl-CoA to lysines on histones. Reported substrates vary by assay and cell type: H3K14 was emphasized in earlier work, H3K23 in cancer-cell contexts, and the 2024 SBBYSS models showed reduced **H3K9 acetylation**. Cell-free assays also demonstrate activity toward H1, H2A, H2B, H3 and H4. Thus, “global histone hypoacetylation” is too broad; H3K9ac reduction currently has the strongest direct SBBYSS-model evidence. (bergamasco2024increasinghistoneacetylation pages 1-2, zhang2020furtherdelineationof pages 1-2)

### Neural cellular mechanism

KAT6B is highly expressed in embryonic brain and the adult subventricular zone. Deficiency reduces ventricular-zone proliferation, cortical-plate size, layer-V pyramidal neurons and cortical interneurons; adult neural stem cells are fewer and show impaired self-renewal and neuronal differentiation. These upstream defects provide a coherent route to developmental delay, intellectual disability, altered social behavior, hypotonia, and structural brain anomalies. (bergamasco2024increasinghistoneacetylation pages 1-2, lundsgaard2017denovokat6b pages 1-2, zu2022brpf1kat6akat6bcomplexmolecular pages 4-6)

**Suggested ontology annotations**

- **GO biological process:** histone acetylation; chromatin organization; regulation of transcription by RNA polymerase II; neural stem-cell proliferation; neurogenesis; neuron differentiation; skeletal-system development; embryonic organ morphogenesis.
- **GO molecular function:** histone acetyltransferase activity; lysine N-acetyltransferase activity; chromatin binding.
- **GO cellular component:** nucleus; nucleoplasm; chromatin; histone acetyltransferase complex.
- **Cell Ontology:** neural stem cell; neural progenitor cell; cortical neuron; pyramidal neuron; cortical interneuron; chondrocyte; osteoblast; cardiac progenitor cell. Direct disease evidence is strongest for neural stem/progenitor cells and cortical neurons.

### Metabolism, immunity, and tissue injury

No primary enzyme deficiency, storage product, metabolomic/lipidomic signature, autoimmunity, inflammatory cascade, fibrosis, ischemia, or necrosis defines SBBYSS. Acetyl-CoA is the biochemical donor for KAT6B, and the 2024 study observed gene-expression changes involving mitochondrial and neurodegeneration-associated pathways, but did not establish a primary mitochondrial disorder. Immune abnormalities have not been systematically characterized.

### Molecular profiling and advanced technologies

Patient-derived/CRISPR-engineered human cells and embryonic cortical-neuron RNA-seq demonstrate reduced H3K9ac and altered transcription that can be partly normalized by valproic acid or acetyl-L-carnitine. No disease-defining single-cell atlas, spatial transcriptomic map, proteomic signature, metabolomic panel, or lipidomic biomarker is yet established for SBBYSS. (bergamasco2024increasinghistoneacetylation pages 15-17, bergamasco2024increasinghistoneacetylation pages 1-2)

## 7. Anatomical structures affected

SBBYSS is multisystemic:

- **Primary systems:** central nervous system, craniofacial structures/eyelids, skeleton and joints, digits, heart, genital tract, endocrine thyroid, eye and auditory system.
- **Variable secondary systems:** kidneys/urinary tract, gastrointestinal tract, palate/airway, dentition, spine and respiratory system.
- **Key UBERON suggestions:** brain (UBERON:0000955), cerebral cortex, corpus callosum, eyelid, optic nerve, patella, thumb, great toe, heart, kidney, thyroid gland, testis, uterus, palate and larynx.
- **Subcellular site:** nucleus/chromatin and the histone acetyltransferase complex.
- **Laterality:** most dysmorphic and skeletal traits are bilateral; individual hearing, renal, testicular and ocular abnormalities may be unilateral or asymmetric. (zhang2020furtherdelineationof pages 4-5, shin2021aneonatewith pages 1-3)

## 8. Temporal development

Disease begins **prenatally**, with occasional increased nuchal translucency/cystic hygroma, growth restriction, polyhydramnios, renal anomalies, or other malformations. The phenotype is usually recognizable congenitally from facial, genital, digital, cardiac, palatal or skeletal findings. Developmental delay, speech impairment and intellectual disability become clearer over infancy and childhood. (maglione2025phenotypiccharacterizationof pages 6-7, zhang2020furtherdelineationof pages 1-2)

There is no validated stage system. The course is chronic and lifelong rather than relapsing-remitting. Congenital structural abnormalities are generally stable unless surgically corrected, whereas consequences such as scoliosis, contractures, feeding problems, thyroid dysfunction, behavioral difficulties and educational needs may evolve. There is no spontaneous molecular remission. Early thyroid replacement, hearing/vision treatment, nutritional support, and developmental therapy represent important windows for preventing avoidable secondary disability.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant.
- **Origin:** overwhelmingly *de novo* in reported cases; rare inherited mild alleles show variable expressivity.
- **Penetrance:** likely high for a clinically relevant phenotype, but precise penetrance is unknown and mildly affected carriers may be overlooked.
- **Expressivity:** markedly variable, including within families.
- **Anticipation:** not reported; this is not a repeat-expansion disorder.
- **Germline mosaicism:** biologically possible and relevant to counseling, but no disease-specific rate is established.
- **Founder effect/carrier frequency:** none established; “carrier” is not the usual concept for a dominant disorder.
- **Consanguinity:** not etiologically important.

Prevalence is estimated at **<1 per million**, but incidence and population-based prevalence have not been measured. No consistent ethnic, geographic, or sex predominance is established. Cases have been reported across multiple ancestries, including European, East Asian, Middle Eastern and African-American individuals. A 2025 review counted 152 molecularly confirmed KAT6B-spectrum patients, illustrating the small and ascertainment-biased evidence base. (maglione2025phenotypiccharacterizationof pages 6-7, maglione2025phenotypiccharacterizationof pages 2-2, davarnia2024denovokat6b pages 1-2)

## 10. Diagnostics

### Clinical recognition

Clinical suspicion should arise from developmental delay/hypotonia plus blepharophimosis or ptosis, mask-like facies, long thumbs/great toes, patellar abnormalities, genital anomalies, congenital heart disease, thyroid disease, hearing loss or lacrimal-duct abnormalities. As Lundsgaard et al. stated in the abstract, **“If a patient is suspected of having a blepharophimosis syndrome or SBBYSS, we recommend sequencing the KAT6B gene.”** (lundsgaard2017denovokat6b pages 1-2)

### Molecular testing strategy

1. **First line:** trio exome/genome sequencing or a comprehensive developmental-disorder/blepharophimosis panel including KAT6B.
2. **Phenotype strongly suggestive:** full KAT6B sequencing with coverage of all coding exons and splice junctions, not only exon 18.
3. **If sequencing is negative:** deletion/duplication analysis or genome sequencing for CNVs and difficult intronic/structural variants.
4. **Parental testing:** establish *de novo* status, identify mildly affected parents, and refine recurrence counseling.
5. **VUS:** integrate phenotype, segregation, population frequency, predicted NMD, RNA studies where feasible, and potentially a validated blood DNA-methylation episignature.
6. **CMA/karyotype:** useful in the general evaluation of multiple anomalies but may be normal in SBBYSS. FISH, mitochondrial DNA analysis, and repeat-expansion testing are not routine disease-specific tests. (maglione2025phenotypiccharacterizationof pages 9-9, lundsgaard2017denovokat6b pages 1-2, shin2021aneonatewith pages 1-3)

### Baseline clinical evaluation

Recommended evaluations include growth and developmental assessment; brain MRI and seizure review; ophthalmology; audiology; echocardiography; renal ultrasound; thyroid function; feeding/swallow and airway assessment; genital/endocrine evaluation; orthopedic examination including patellae, hips, knees and spine; and assessment for cleft palate, dental disease and intestinal malrotation when clinically indicated. Zhang et al. specifically recommended MRI/neurological evaluation, seizure surveillance, ophthalmology, periodic hearing tests, thyroid testing, echocardiography, and renal ultrasonography. (zhang2020furtherdelineationof pages 7-8)

### Differential diagnosis

Important alternatives are GPS and intermediate KAT6B disease, KAT6A/Arboleda–Tham syndrome, MED12-related Ohdo syndrome, blepharophimosis-ptosis-epicanthus inversus syndrome due to FOXL2, Kabuki syndrome, Coffin–Siris spectrum, Bohring–Opitz syndrome, Toriello–Carey syndrome, and other chromatinopathies. Patellar/genital anomalies favor KAT6B disease; long thumbs/great toes and mask-like blepharophimosis favor SBBYSS. Molecular testing is necessary because clinical overlap is substantial. (zhang2020furtherdelineationof pages 1-2, zhang2020furtherdelineationof pages 7-8)

### Screening

SBBYSS is not included in routine newborn screening. Population carrier screening is inappropriate for a predominantly *de novo* dominant disorder. Targeted prenatal or preimplantation testing becomes possible once the familial variant is known.

## 11. Outcome and prognosis

No reliable 5- or 10-year survival estimates, life-expectancy curves, mortality rates, or validated prognostic biomarkers exist. Many individuals survive into adolescence or adulthood, but severity spans mild familial disease to lethal neonatal/infant complications. In the Zhang cohort, three children with GPS died in infancy—from pulmonary hypoplasia secondary to renal hypoplasia/dysplasia, extreme prematurity with multiorgan complications, and influenza H1N1 infection. These deaths should not be extrapolated as a SBBYSS mortality rate. (zhang2020furtherdelineationof pages 7-8)

Long-term morbidity is driven by intellectual/developmental disability, limited speech, behavioral disorders, hearing/vision impairment, feeding problems, hypotonia, mobility-limiting skeletal disease, hypothyroidism, and congenital cardiac/renal disease. Recovery from the genetic disorder is not expected, but treatable complications and functional abilities can improve substantially with early intervention. Prognosis is most influenced by cardiac, renal, respiratory and CNS severity, feeding safety, hearing/vision status, thyroid treatment, and access to developmental support.

## 12. Treatment

### Current standard care

There is no approved disease-modifying therapy. Treatment is individualized and multidisciplinary:

- **Development:** early-intervention services, special education, speech/language therapy, augmentative communication, occupational therapy, and physical therapy.
- **Feeding:** nutritional monitoring, feeding therapy, swallow evaluation, reflux treatment, and enteral support when necessary.
- **Endocrine:** levothyroxine for hypothyroidism; assessment/treatment of hypogonadism or delayed puberty.
- **Cardiac:** standard medical or surgical management of congenital heart disease and arrhythmia; one reported infant underwent ASD patch closure at nine months.
- **Hearing/vision:** hearing aids or other audiological intervention, correction of refractive error/strabismus/ptosis, and lacrimal-duct procedures where indicated.
- **Orthopedic:** physiotherapy, mobility aids, surveillance for scoliosis and contractures, and orthopedic surgery when functionally necessary.
- **Neurologic/behavioral:** standard antiseizure medication if seizures occur and individualized behavioral/psychiatric care.
- **Genitourinary/palatal/GI:** orchiopexy, hypospadias or palate repair, renal/urological treatment, and urgent evaluation of symptoms suggesting malrotation/volvulus. (zhang2020furtherdelineationof pages 7-8, shin2021aneonatewith pages 1-3, davarnia2024denovokat6b pages 1-2)

**Suggested MAXO annotations:** genetic counseling; exome sequencing; sequence analysis of KAT6B; brain MRI; echocardiography; renal ultrasonography; thyroid-function testing; hearing evaluation; ophthalmologic examination; developmental assessment; physical therapy; occupational therapy; speech therapy; feeding therapy; thyroid-hormone replacement; surgical correction of congenital heart defect; orchiopexy; orthopedic surveillance.

### Experimental therapy

The strongest translational development is Bergamasco et al., published **1 April 2024** in *Journal of Clinical Investigation* (DOI: https://doi.org/10.1172/JCI167672). Their abstract states: **“Both compounds improved sociability in Kat6b+/– mice, and ALCAR treatment restored learning and memory.”** Valproic acid, an HDAC inhibitor, and acetyl-L-carnitine, an acetyl donor, increased histone acetylation in mutant human cells and mouse brain/blood, partly normalized cortical-neuron transcription, and improved selected behaviors. (bergamasco2024increasinghistoneacetylation pages 15-17, bergamasco2024increasinghistoneacetylation pages 1-2)

This is preclinical evidence only. Valproate can impair cognition in some settings and is a major human teratogen; neither valproate nor acetyl-L-carnitine should be considered an established SBBYSS therapy. No relevant disease-specific interventional clinical trial or NCT identifier was identified in the registry search. Gene replacement, CRISPR, ASO/siRNA, mRNA, cell therapy, immunotherapy, and genotype-guided pharmacotherapy remain unavailable.

## 13. Prevention

Primary prevention by lifestyle, vaccination, or environmental avoidance is not possible. Prevention is principally reproductive and complication-focused:

- **Genetic counseling:** explain autosomal-dominant inheritance, predominantly *de novo* occurrence, variable expressivity, and residual recurrence risk from parental germline mosaicism.
- **Parental testing:** essential before assigning a low recurrence risk.
- **Reproductive options:** targeted prenatal diagnosis by chorionic-villus sampling/amniocentesis and preimplantation genetic testing for monogenic disease when the familial variant is known.
- **Secondary/tertiary prevention:** newborn recognition, prompt thyroid treatment, hearing and vision correction, safe feeding, cardiac/renal surveillance, vaccination and ordinary infection prevention, developmental therapies, and monitoring for orthopedic and GI complications.

There is no vaccine, chemoprophylaxis, public-health environmental intervention, or population screening program specific to SBBYSS.

## 14. Other species and natural disease

No well-established naturally occurring veterinary analogue of SBBYSS was identified, and the disorder has no zoonotic potential. The relevant comparative species is the laboratory mouse, **Mus musculus** (NCBI Taxonomy 10090), whose ortholog is *Kat6b* (*Querkopf/Qkf*). KAT6B developmental functions are evolutionarily conserved, particularly in neural stem/progenitor biology, cortical development and skeletogenesis. Naturally occurring breed-specific disease, VBO mapping and cross-species transmission are not applicable.

## 15. Model organisms and experimental systems

### Mouse models

*Kat6b* heterozygous mice provide the most disease-relevant model. They show approximately 50% cortical *Kat6b* transcript reduction and deficits in learning, memory and social behavior. Homozygous deficiency produces underdeveloped jaws and frontal bones, delayed neonatal respiratory adaptation and death before weaning. Earlier models also showed reduced cortical progenitor proliferation, cortical-plate hypoplasia, reduced pyramidal neurons/interneurons, and impaired adult neural-stem-cell maintenance. These models recapitulate neurodevelopmental, craniofacial and behavioral aspects but do not reproduce every human congenital feature or the full allelic complexity of NMD-escaping truncations. (bergamasco2024increasinghistoneacetylation pages 1-2, zu2022brpf1kat6akat6bcomplexmolecular pages 4-6)

### Human cellular models

CRISPR-engineered HEK293T clones carrying SBBYSS-specific KAT6B variants and primary/cultured cortical-neuron systems demonstrated reduced KAT6B expression, reduced H3K9ac and altered gene expression. Their key strength is allele-specific molecular testing; limitations include non-developmental cell context for HEK293T cells and inability to model whole-organ morphogenesis. (bergamasco2024increasinghistoneacetylation pages 1-2)

No validated SBBYSS patient iPSC, cerebral-organoid, zebrafish, *Drosophila*, *C. elegans*, or naturally diseased animal model was established in the retrieved evidence. Future priorities include patient-derived neural and mesenchymal iPSCs, allele-specific knock-in models, single-cell developmental atlases, and direct functional comparison of NMD-sensitive versus NMD-escaping variants.

## Recent developments and expert interpretation

1. **Spectrum rather than rigid syndromes:** the 2023 Polish cohort documented six molecularly confirmed patients with shared facial/developmental findings but variable and sometimes mild knee disease. Its conclusion—that phenotypic differences support a broader spectrum—is consistent with the 32-person allelic-series study. (zhang2020furtherdelineationof pages 1-2, magdalena2023clinicalheterogeneityof pages 1-2)
2. **Epigenomic diagnosis:** 2023 KAT6A/KAT6B methylation work introduced a potentially useful functional biomarker for VUS resolution, although primary performance metrics require verification before clinical deployment. (maglione2025phenotypiccharacterizationof pages 10-11, maglione2025phenotypiccharacterizationof pages 9-9)
3. **Postnatal reversibility:** the 2024 human-cell/mouse study is the first strong proof that at least some downstream acetylation, transcriptional and behavioral abnormalities remain pharmacologically modifiable after birth. It supports therapeutic development, not off-label clinical use. (bergamasco2024increasinghistoneacetylation pages 15-17, bergamasco2024increasinghistoneacetylation pages 1-2)
4. **Continuing phenotype expansion:** a 2024 Iranian report added detailed skeletal and white-matter findings, but individual case reports cannot establish frequency or causality for newly observed features. (davarnia2024denovokat6b pages 1-2)

## Evidence limitations

The evidence base consists mainly of retrospective cohorts, literature compilations and case reports. Frequencies are vulnerable to referral bias, incomplete phenotyping and changing subtype definitions. There are no population registries, controlled human trials, longitudinal adult cohorts, validated patient-reported outcome measures, or robust penetrance estimates. Mechanistic evidence is strongest for KAT6B deficiency, H3K9 hypoacetylation and neural progenitor dysfunction; dominant-negative effects of terminal truncations remain plausible but not conclusively proven. PMIDs were not present in the retrievable source text and therefore are not invented here; DOI URLs and publication dates are supplied for traceability.

References

1. (bergamasco2024increasinghistoneacetylation pages 1-2): Maria I. Bergamasco, Hannah K. Vanyai, Alexandra L. Garnham, Niall D. Geoghegan, Adam P. Vogel, Samantha Eccles, Kelly L. Rogers, Gordon K. Smyth, Marnie E. Blewitt, Anthony J. Hannan, Tim Thomas, and Anne K. Voss. Increasing histone acetylation improves sociability and restores learning and memory in kat6b-haploinsufficient mice. The Journal of Clinical Investigation, Apr 2024. URL: https://doi.org/10.1172/jci167672, doi:10.1172/jci167672. This article has 21 citations.

2. (zhang2020furtherdelineationof pages 1-2): Li Xin Zhang, Gabrielle Lemire, Claudia Gonzaga-Jauregui, Sirinart Molidperee, Carolina Galaz-Montoya, David S. Liu, Alain Verloes, Amelle G. Shillington, Kosuke Izumi, Alyssa L. Ritter, Beth Keena, Elaine Zackai, Dong Li, Elizabeth Bhoj, Jennifer M. Tarpinian, Emma Bedoukian, Mary K. Kukolich, A. Micheil Innes, Grace U. Ediae, Sarah L. Sawyer, Karippoth Mohandas Nair, Para Chottil Soumya, Kinattinkara R. Subbaraman, Frank J. Probst, Jennifer A. Bassetti, Reid V. Sutton, Richard A. Gibbs, Chester Brown, Philip M. Boone, Ingrid A. Holm, Marco Tartaglia, Giovanni Battista Ferrero, Marcello Niceta, Maria Lisa Dentici, Francesca Clementina Radio, Boris Keren, Constance F. Wells, Christine Coubes, Annie Laquerrière, Jacqueline Aziza, Charlotte Dubucs, Sheela Nampoothiri, David Mowat, Millan S. Patel, Ana Bracho, Francisco Cammarata-Scalisi, Alper Gezdirici, Alberto Fernandez-Jaen, Natalie Hauser, Yuri A. Zarate, Katherine A. Bosanko, Klaus Dieterich, John C. Carey, Jessica X. Chong, Deborah A. Nickerson, Michael J. Bamshad, Brendan H. Lee, Xiang-Jiao Yang, James R. Lupski, and Philippe M. Campeau. Further delineation of the clinical spectrum of kat6b disorders and allelic series of pathogenic variants. Genetics in Medicine, 22:1338-1347, Aug 2020. URL: https://doi.org/10.1038/s41436-020-0811-8, doi:10.1038/s41436-020-0811-8. This article has 64 citations and is from a highest quality peer-reviewed journal.

3. (magdalena2023clinicalheterogeneityof pages 1-2): Klaniewska Magdalena, Bolanowska‐Tyszko Anna, Latos‐Bielenska Anna, Jezela‐Stanek Aleksandra, Szczaluba Krzysztof, Krajewska‐Walasek Malgorzata, Ciara Elzbieta, Pelc Magdalena, Jurkiewicz Dorota, Stawinski Piotr, Zubkiewicz‐Kucharska Agnieszka, Rydzanicz Małgorzata, Ploski Rafal, and Smigiel Robert. Clinical heterogeneity of polish patients with kat6b–related disorder. Molecular Genetics & Genomic Medicine, Sep 2023. URL: https://doi.org/10.1002/mgg3.2265, doi:10.1002/mgg3.2265. This article has 6 citations and is from a peer-reviewed journal.

4. (shin2021aneonatewith pages 1-3): Ji Hye Shin, Han Hyuk Lim, Mi Hyeon Gang, Seon Young Kim, Shin-seung Yang, and Mea-young Chang. A neonate with say–barber–biesecker–young–simpson syndrome with a novel pathogenic mutation in kat6b gene: a case report. Journal of Genetic Medicine, 18:147-151, Dec 2021. URL: https://doi.org/10.5734/jgm.2021.18.2.147, doi:10.5734/jgm.2021.18.2.147. This article has 2 citations.

5. (maglione2025phenotypiccharacterizationof pages 6-7): Vittorio Maglione, Antonio Pizzuti, Gioia Mastromoro, Eleonora Cresta, Paola Favata, Maria Cristina Digilio, Rossella Capolino, Maria Lisa Dentici, Lorenzo Sinibaldi, Antonio Novelli, Marco Tartaglia, Gianluca Terrin, and Viviana Cardilli. Phenotypic characterization of seven pediatric patients diagnosed with kat6b-related disorders: case series and review of the literature. American journal of medical genetics. Part A, pages e64100, Apr 2025. URL: https://doi.org/10.1002/ajmg.a.64100, doi:10.1002/ajmg.a.64100. This article has 1 citations and is from a peer-reviewed journal.

6. (maglione2025phenotypiccharacterizationof pages 2-2): Vittorio Maglione, Antonio Pizzuti, Gioia Mastromoro, Eleonora Cresta, Paola Favata, Maria Cristina Digilio, Rossella Capolino, Maria Lisa Dentici, Lorenzo Sinibaldi, Antonio Novelli, Marco Tartaglia, Gianluca Terrin, and Viviana Cardilli. Phenotypic characterization of seven pediatric patients diagnosed with kat6b-related disorders: case series and review of the literature. American journal of medical genetics. Part A, pages e64100, Apr 2025. URL: https://doi.org/10.1002/ajmg.a.64100, doi:10.1002/ajmg.a.64100. This article has 1 citations and is from a peer-reviewed journal.

7. (zhang2020furtherdelineationof pages 7-8): Li Xin Zhang, Gabrielle Lemire, Claudia Gonzaga-Jauregui, Sirinart Molidperee, Carolina Galaz-Montoya, David S. Liu, Alain Verloes, Amelle G. Shillington, Kosuke Izumi, Alyssa L. Ritter, Beth Keena, Elaine Zackai, Dong Li, Elizabeth Bhoj, Jennifer M. Tarpinian, Emma Bedoukian, Mary K. Kukolich, A. Micheil Innes, Grace U. Ediae, Sarah L. Sawyer, Karippoth Mohandas Nair, Para Chottil Soumya, Kinattinkara R. Subbaraman, Frank J. Probst, Jennifer A. Bassetti, Reid V. Sutton, Richard A. Gibbs, Chester Brown, Philip M. Boone, Ingrid A. Holm, Marco Tartaglia, Giovanni Battista Ferrero, Marcello Niceta, Maria Lisa Dentici, Francesca Clementina Radio, Boris Keren, Constance F. Wells, Christine Coubes, Annie Laquerrière, Jacqueline Aziza, Charlotte Dubucs, Sheela Nampoothiri, David Mowat, Millan S. Patel, Ana Bracho, Francisco Cammarata-Scalisi, Alper Gezdirici, Alberto Fernandez-Jaen, Natalie Hauser, Yuri A. Zarate, Katherine A. Bosanko, Klaus Dieterich, John C. Carey, Jessica X. Chong, Deborah A. Nickerson, Michael J. Bamshad, Brendan H. Lee, Xiang-Jiao Yang, James R. Lupski, and Philippe M. Campeau. Further delineation of the clinical spectrum of kat6b disorders and allelic series of pathogenic variants. Genetics in Medicine, 22:1338-1347, Aug 2020. URL: https://doi.org/10.1038/s41436-020-0811-8, doi:10.1038/s41436-020-0811-8. This article has 64 citations and is from a highest quality peer-reviewed journal.

8. (davarnia2024denovokat6b pages 1-2): Behzad Davarnia, Mohammad Panahi, Bahareh Rahimi, Hassan Anari, Reza Farajollahi, Ehsan Abbaspour Rodbaneh, and Farhad Jeddi. De novo kat6b mutation causes say–barber–biesecker–young–simpson variant of ohdo syndrome in an iranian boy: a case report. Journal of Medical Case Reports, Jan 2024. URL: https://doi.org/10.1186/s13256-023-04237-w, doi:10.1186/s13256-023-04237-w. This article has 7 citations and is from a peer-reviewed journal.

9. (lundsgaard2017denovokat6b pages 1-2): Malene Lundsgaard, Vang Q. Le, Anja Ernst, Hans C. Laugaard-Jacobsen, Kirsten Rasmussen, Inge S. Pedersen, and Michael B. Petersen. De novo kat6b mutation identified with whole-exome sequencing in a girl with say-barber/biesecker/young-simpson syndrome. Molecular Syndromology, 8:24-29, Nov 2017. URL: https://doi.org/10.1159/000452258, doi:10.1159/000452258. This article has 12 citations and is from a peer-reviewed journal.

10. (zhang2020furtherdelineationof pages 4-5): Li Xin Zhang, Gabrielle Lemire, Claudia Gonzaga-Jauregui, Sirinart Molidperee, Carolina Galaz-Montoya, David S. Liu, Alain Verloes, Amelle G. Shillington, Kosuke Izumi, Alyssa L. Ritter, Beth Keena, Elaine Zackai, Dong Li, Elizabeth Bhoj, Jennifer M. Tarpinian, Emma Bedoukian, Mary K. Kukolich, A. Micheil Innes, Grace U. Ediae, Sarah L. Sawyer, Karippoth Mohandas Nair, Para Chottil Soumya, Kinattinkara R. Subbaraman, Frank J. Probst, Jennifer A. Bassetti, Reid V. Sutton, Richard A. Gibbs, Chester Brown, Philip M. Boone, Ingrid A. Holm, Marco Tartaglia, Giovanni Battista Ferrero, Marcello Niceta, Maria Lisa Dentici, Francesca Clementina Radio, Boris Keren, Constance F. Wells, Christine Coubes, Annie Laquerrière, Jacqueline Aziza, Charlotte Dubucs, Sheela Nampoothiri, David Mowat, Millan S. Patel, Ana Bracho, Francisco Cammarata-Scalisi, Alper Gezdirici, Alberto Fernandez-Jaen, Natalie Hauser, Yuri A. Zarate, Katherine A. Bosanko, Klaus Dieterich, John C. Carey, Jessica X. Chong, Deborah A. Nickerson, Michael J. Bamshad, Brendan H. Lee, Xiang-Jiao Yang, James R. Lupski, and Philippe M. Campeau. Further delineation of the clinical spectrum of kat6b disorders and allelic series of pathogenic variants. Genetics in Medicine, 22:1338-1347, Aug 2020. URL: https://doi.org/10.1038/s41436-020-0811-8, doi:10.1038/s41436-020-0811-8. This article has 64 citations and is from a highest quality peer-reviewed journal.

11. (zu2022brpf1kat6akat6bcomplexmolecular pages 4-6): Gaoyu Zu, Ying Liu, Jingli Cao, Baicheng Zhao, Hang Zhang, and Linya You. Brpf1-kat6a/kat6b complex: molecular structure, biological function and human disease. Cancers, 14:4068, Aug 2022. URL: https://doi.org/10.3390/cancers14174068, doi:10.3390/cancers14174068. This article has 35 citations.

12. (magdalena2023clinicalheterogeneityof pages 10-10): Klaniewska Magdalena, Bolanowska‐Tyszko Anna, Latos‐Bielenska Anna, Jezela‐Stanek Aleksandra, Szczaluba Krzysztof, Krajewska‐Walasek Malgorzata, Ciara Elzbieta, Pelc Magdalena, Jurkiewicz Dorota, Stawinski Piotr, Zubkiewicz‐Kucharska Agnieszka, Rydzanicz Małgorzata, Ploski Rafal, and Smigiel Robert. Clinical heterogeneity of polish patients with kat6b–related disorder. Molecular Genetics & Genomic Medicine, Sep 2023. URL: https://doi.org/10.1002/mgg3.2265, doi:10.1002/mgg3.2265. This article has 6 citations and is from a peer-reviewed journal.

13. (bergamasco2024increasinghistoneacetylation pages 15-17): Maria I. Bergamasco, Hannah K. Vanyai, Alexandra L. Garnham, Niall D. Geoghegan, Adam P. Vogel, Samantha Eccles, Kelly L. Rogers, Gordon K. Smyth, Marnie E. Blewitt, Anthony J. Hannan, Tim Thomas, and Anne K. Voss. Increasing histone acetylation improves sociability and restores learning and memory in kat6b-haploinsufficient mice. The Journal of Clinical Investigation, Apr 2024. URL: https://doi.org/10.1172/jci167672, doi:10.1172/jci167672. This article has 21 citations.

14. (maglione2025phenotypiccharacterizationof pages 9-9): Vittorio Maglione, Antonio Pizzuti, Gioia Mastromoro, Eleonora Cresta, Paola Favata, Maria Cristina Digilio, Rossella Capolino, Maria Lisa Dentici, Lorenzo Sinibaldi, Antonio Novelli, Marco Tartaglia, Gianluca Terrin, and Viviana Cardilli. Phenotypic characterization of seven pediatric patients diagnosed with kat6b-related disorders: case series and review of the literature. American journal of medical genetics. Part A, pages e64100, Apr 2025. URL: https://doi.org/10.1002/ajmg.a.64100, doi:10.1002/ajmg.a.64100. This article has 1 citations and is from a peer-reviewed journal.

15. (maglione2025phenotypiccharacterizationof pages 10-11): Vittorio Maglione, Antonio Pizzuti, Gioia Mastromoro, Eleonora Cresta, Paola Favata, Maria Cristina Digilio, Rossella Capolino, Maria Lisa Dentici, Lorenzo Sinibaldi, Antonio Novelli, Marco Tartaglia, Gianluca Terrin, and Viviana Cardilli. Phenotypic characterization of seven pediatric patients diagnosed with kat6b-related disorders: case series and review of the literature. American journal of medical genetics. Part A, pages e64100, Apr 2025. URL: https://doi.org/10.1002/ajmg.a.64100, doi:10.1002/ajmg.a.64100. This article has 1 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Say-Barber-Biesecker-Young-Simpson_Syndrome-deep-research-falcon_artifacts/artifact-00.md)