---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T17:08:31.654572'
end_time: '2026-08-01T17:15:51.141803'
duration_seconds: 439.49
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Superior Mesenteric Artery Syndrome
  mondo_id: ''
  category: Structural
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
  path: Superior_Mesenteric_Artery_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Superior Mesenteric Artery Syndrome
- **MONDO ID:**  (if available)
- **Category:** Structural

## Research Objectives

Please provide a comprehensive research report on **Superior Mesenteric Artery Syndrome** covering all of the
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
- **Disease Name:** Superior Mesenteric Artery Syndrome
- **MONDO ID:**  (if available)
- **Category:** Structural

## Research Objectives

Please provide a comprehensive research report on **Superior Mesenteric Artery Syndrome** covering all of the
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


# Superior Mesenteric Artery Syndrome: Disease-Characteristics Report

**Scope and evidence note.** Superior mesenteric artery syndrome (SMAS) is rare, and its literature is dominated by retrospective cohorts, small prospective series, and case reports rather than large randomized trials. The most recent 2023–2024 literature located was primarily surgical or case-based; therefore, foundational reviews and the prospective cohort indexed as PMID 30291587 remain important. Numerical epidemiologic and mortality estimates should be treated cautiously because they often derive from older, selected series rather than population registries.

| Domain | Summary | Key structured fields / suggested mappings | Evidence |
|---|---|---|---|
| Definition / category | Superior Mesenteric Artery Syndrome (SMAS, Wilkie syndrome) is a **rare structural/acquired duodenal obstruction** caused by compression of the third/horizontal duodenum in the narrowed space between the abdominal aorta and superior mesenteric artery. | Category: Structural; Disease class: duodenal obstruction / gastrointestinal compression syndrome | (galimov2022thecomplicationof pages 2-3, galimov2022thecomplicationof pages 1-2, NCT03416647 chunk 1) |
| Identifiers / synonyms | Secure identifier present in evidence: **MeSH D013478**. Synonyms documented in retrieved evidence include **Wilkie syndrome**, **chronic duodenal obstruction**, and **CAST syndrome**. A prospective institutional study is linked to **PMID 30291587**; relevant trials include **NCT03416647**, **NCT07115472**, **NCT04515251**, **NCT03937193**, **NCT06970093**. | Exact IDs asserted: MeSH D013478; PMID 30291587; NCT03416647; NCT07115472; NCT04515251; NCT03937193; NCT06970093 | (galimov2022thecomplicationof pages 3-4, NCT03416647 chunk 1, NCT07115472 chunk 1, NCT04515251 chunk 1, NCT06970093 chunk 1, NCT03937193 chunk 1) |
| Core anatomy | Primary lesion site is the **third/transverse/horizontal part of the duodenum** compressed between the **SMA** anteriorly and **abdominal aorta/spine** posteriorly; retroperitoneal fat loss narrows this space. | Suggested anatomy labels: duodenum (3rd part), superior mesenteric artery, abdominal aorta, retroperitoneal fat pad | (galimov2022thecomplicationof pages 2-3, galimov2022thecomplicationof pages 3-4, galimov2022thecomplicationof pages 1-2, NCT03937193 chunk 1) |
| Major phenotypes | Core phenotype cluster: **postprandial epigastric/abdominal pain, nausea, vomiting, reflux, bloating, difficulty eating, weight loss, low BMI/underweight**, sometimes severe complications such as aspiration pneumonia or acute pancreatitis. | Suggested HPO labels: abdominal pain; epigastric pain; nausea; vomiting; abdominal bloating; gastroesophageal reflux; early satiety/feeding difficulty; weight loss; low body mass index; malnutrition; dehydration | (galimov2022thecomplicationof pages 2-3, galimov2022thecomplicationof pages 3-4, NCT03416647 chunk 1, NCT07115472 chunk 1, NCT06970093 chunk 1) |
| Mechanism / causal chain | Typical causal chain: **rapid weight loss or altered anatomy → loss/reduction of retroperitoneal fat cushion → decreased aortomesenteric angle/distance → extrinsic compression of D3 → impaired chyme passage / proximal obstruction → meal-related symptoms, reduced intake, further weight loss, and possible severe gastric or aspiration/pancreatic complications**. | Suggested process labels: intestinal obstruction; impaired gastric emptying/proximal stasis; nutritional deficiency; positive feedback worsening via weight loss | (galimov2022thecomplicationof pages 2-3, galimov2022thecomplicationof pages 3-4, NCT03416647 chunk 1, galimov2022thecomplicationof pages 4-5, NCT03937193 chunk 1) |
| Diagnostic imaging thresholds | Diagnosis is imaging-centered and usually combines symptoms with CT/MR angiography and/or contrast studies. Evidence shows **normal** aortomesenteric angle roughly **35–65°** or **38–80°** and distance **10–28 mm**; commonly used abnormal thresholds are **angle <22°** and **distance <8 mm**; broader abnormal cutoffs **<35°** and **<10 mm** also appear in case literature. | Imaging modalities in evidence: CT with oral contrast, CT/MR angiography, suggestive barium swallow; example case: angle 14°, distance 6 mm | (galimov2022thecomplicationof pages 2-3, galimov2022thecomplicationof pages 3-4, galimov2022thecomplicationof pages 1-2, NCT03416647 chunk 1, NCT07115472 chunk 1) |
| Major acquired risk factors | Major non-genetic/acquired drivers are **rapid weight loss**, **underweight/low BMI**, feeding difficulty, and **anatomic distortion**; trial exclusion/observational protocols also flag conditions such as **severe scoliosis/spinal fixation**, abdominal masses, and cachectic states as relevant anatomical confounders/risk contexts. | Suggested risk labels: rapid weight loss; low BMI; loss of retroperitoneal adipose tissue; postoperative/anatomic change; scoliosis-associated distortion | (galimov2022thecomplicationof pages 2-3, NCT03416647 chunk 1, NCT07115472 chunk 1, NCT04515251 chunk 1, NCT03937193 chunk 1) |
| First-line management | Initial management is generally conservative: restore nutrition/weight, treat dehydration/electrolyte problems, decompress when needed, and use medical/supportive therapy; the refractory-SMAS trial defines failed conservative care as failure of **gastrointestinal decompression, enteral nutrition, and parenteral nutrition**. | Suggested intervention labels: nutritional rehabilitation; enteral nutrition; parenteral nutrition; gastrointestinal decompression; symptom-directed medical therapy | (galimov2022thecomplicationof pages 3-4, NCT03416647 chunk 1, NCT07115472 chunk 1) |
| Surgical management | For persistent/refractory disease, **duodenojejunostomy** is the most consistently represented operation in the evidence and was used for all patients in the prospective single-institution study; case evidence also describes **laparoscopic Strong’s operation** / duodenal mobilization strategies. A randomized trial is comparing **One Anastomosis Gastric Bypass (OAGB)** vs **Duodenojejunostomy (DJ)**. | Exact trial/intervention IDs: NCT03416647 (duodenojejunostomy cohort), NCT06970093 (OAGB vs DJ); suggested NCIT-style labels: duodenojejunostomy; gastric bypass procedure | (galimov2022thecomplicationof pages 1-2, NCT03416647 chunk 1, NCT06970093 chunk 1, NCT06970093 chunk 2) |
| Epidemiology | SMAS is rare. Retrieved case literature reports prevalence estimates around **0.1%–0.78%**, female predominance around **2:1**, and peak occurrence in **10–30 years**, though it can occur outside this range. One CT normative study planned **500 non-SMAS vs 10 SMAS** cases in a young Chinese cohort, illustrating rarity in imaging datasets. | Epidemiology fields: rare disease; female predominance; pediatric-to-young-adult skew with broader age range possible | (galimov2022thecomplicationof pages 2-3, NCT03937193 chunk 1) |
| Prognosis / complications | Prognosis improves with timely recognition and decompressive treatment. Documented serious complications include **gastric perforation, acute pancreatitis, aspiration pneumonia**, ulcer disease, and in older literature/case review **life-threatening deterioration with reported mortality up to 33% if untreated**. Prospective studies track symptom scores, BMI recovery, and reduced need for acid suppression/prokinetics over long follow-up. | Outcome fields: symptom relief; BMI gain; complication prevention; long-term follow-up in prospective cohort median 47 months (IQR 34–72) | (galimov2022thecomplicationof pages 2-3, NCT03416647 chunk 1, galimov2022thecomplicationof pages 4-5) |
| Evidence gaps (genetics / omics / models) | No secure evidence in the retrieved materials supports a **causal gene, pathogenic variant, Mendelian inheritance pattern, molecular biomarker, omics signature, infectious etiology, or validated model organism**. Current evidence base is dominated by clinical imaging studies, case reports/series, and small interventional cohorts/trials. | KB note: mark genetics/omics/animal-model fields as **not established in retrieved evidence** rather than negative | (NCT03416647 chunk 1, NCT07115472 chunk 1, NCT03937193 chunk 1) |


*Table: This table condenses the highest-yield disease-characteristics fields for Superior Mesenteric Artery Syndrome, including secure identifiers, anatomy, phenotypes, mechanism, diagnostic thresholds, treatment, epidemiology, and major evidence gaps. It is designed for direct use in a structured disease knowledge base.*

## 1. Disease information

### Definition

SMAS is an **extrinsic mechanical obstruction of the third, horizontal portion of the duodenum (D3)** where it passes between the superior mesenteric artery (SMA) anteriorly and the abdominal aorta/spine posteriorly. Reduction of the intervening mesenteric-retroperitoneal fat cushion narrows the aortomesenteric angle and distance, compressing D3. It is a structural gastrointestinal compression syndrome, not mesenteric ischemia or SMA dissection. (galimov2022thecomplicationof pages 2-3, galimov2022thecomplicationof pages 3-4, galimov2022thecomplicationof pages 1-2)

A useful exact abstract quotation from Galimov et al. (published July 2022) is: **“the distal part of the duodenum is compressed between the abdominal aorta, spine, and SMA,”** producing mechanical obstruction. The authors also emphasize that delayed diagnosis may lead to life-threatening complications. DOI: https://doi.org/10.24060/2076-3093-2022-12-2-123-127. (galimov2022thecomplicationof pages 1-2)

### Identifiers and synonyms

- **MeSH:** D013478, *Superior Mesenteric Artery Syndrome*—securely present in the retrieved ClinicalTrials.gov records. (NCT03416647 chunk 1)
- **MONDO, OMIM, Orphanet, ICD-10, ICD-11:** an exact current identifier was not securely recovered from the accessed evidence and should be verified directly against the live ontology release before knowledge-base ingestion. SMAS is not established as an OMIM Mendelian disorder.
- **Synonyms:** Wilkie syndrome/Wilkie’s syndrome; chronic duodenal obstruction; arteriomesenteric duodenal compression syndrome; cast syndrome/CAST syndrome. “Chronic duodenal obstruction” and “Wilkie’s syndrome” occur in the prospective-study record. (galimov2022thecomplicationof pages 3-4, NCT03416647 chunk 1)
- **Do not conflate with:** SMA thrombosis, embolism, dissection, aneurysm, or acute/chronic mesenteric ischemia.

The report describes aggregated disease-level evidence. The cited prospective study included 39 consecutive patients; no individual EHR-derived patient record is used here. (NCT03416647 chunk 1)

## 2. Etiology

### Causal and predisposing factors

The best-established causal sequence is **rapid or substantial weight loss → depletion of the aortomesenteric fat pad → narrowing of the aortomesenteric angle/distance → D3 compression**. Once obstruction impairs eating, further weight loss can create a self-amplifying cycle. (galimov2022thecomplicationof pages 2-3, NCT03937193 chunk 1)

Recognized clinical contexts include:

- severe or rapid weight loss, low BMI, malnutrition, cachexia, or feeding restriction;
- eating disorders and other illnesses causing reduced intake or catabolism;
- major burns, trauma, malignancy, malabsorption, prolonged immobilization, or severe systemic illness;
- corrective spinal surgery, marked scoliosis, body casting, or rapid linear growth, which can alter the relationship between the SMA, aorta, spine, and duodenum;
- abdominal or retroperitoneal operations that change intestinal fixation or tension.

The prospective surgical protocol regarded BMI below 18.5 kg/m² with difficulty eating as a major clinical feature. Imaging studies specifically examine BMI, visceral fat, and retroperitoneal fat because these influence angle and distance; severe scoliosis and spinal fixation are treated as important anatomical modifiers. (NCT03416647 chunk 1, NCT04515251 chunk 1, NCT03937193 chunk 1)

### Genetics, environment, and protective factors

No validated causal gene, susceptibility locus, pathogenic variant, modifier gene, Mendelian inheritance pattern, or gene–environment interaction has been established. Congenital/anatomical configurations may predispose an individual, but that is not equivalent to a demonstrated genetic disorder.

No toxin, pollutant, occupational exposure, or infectious agent is established as a direct cause. Lifestyle and environmental effects are principally mediated through nutritional depletion or acquired anatomical change. Maintaining adequate nutrition and avoiding rapid, unmonitored weight loss in vulnerable patients are plausible protective measures, but no controlled study establishes a specific protective diet, allele, drug, or supplement.

## 3. Phenotypes

SMAS can occur in children or adults and may present acutely after a precipitating event or insidiously over months or years. Severity ranges from intermittent postprandial discomfort to complete high intestinal obstruction and severe malnutrition. The 39-patient protocol defined clinically important disease through severe symptoms occurring at least weekly, poor quality of life, refractory response to medical treatment, underweight, or serious complications. (NCT03416647 chunk 1)

| Phenotype | Type/course and impact | Suggested HPO annotation |
|---|---|---|
| Postprandial epigastric or upper-abdominal pain | Symptom; episodic after meals or persistent in advanced obstruction; limits eating and activity | Epigastric pain; Abdominal pain |
| Nausea and bilious/non-bilious vomiting | Symptoms; intermittent to severe; may cause dehydration and aspiration | Nausea; Vomiting |
| Early satiety, feeding difficulty, bloating, reflux | Symptoms; worsened by meals; substantially impairs nutrition and social eating | Early satiety; Feeding difficulties; Abdominal distention; Gastroesophageal reflux |
| Weight loss, underweight, low BMI | Physical/nutritional phenotype; often progressive and both cause and consequence | Weight loss; Decreased body weight; Low body mass index |
| Malnutrition/dehydration/electrolyte disturbance | Laboratory/systemic consequences; severity varies with duration | Malnutrition; Dehydration; Electrolyte abnormality |
| Gastric and proximal duodenal dilation | Imaging/physical manifestation of obstruction | Duodenal obstruction; Gastric dilatation |
| Aspiration pneumonia, acute pancreatitis, gastric perforation | Uncommon but severe complications | Aspiration pneumonia; Acute pancreatitis; Gastrointestinal perforation |

Abdominal pain, nausea, vomiting, reflux, and bloating were explicitly captured in the prospective cohort’s symptom score; severe complications included gastric perforation, acute pancreatitis, and aspiration pneumonia. (NCT03416647 chunk 1)

Formal SMAS-specific EQ-5D, SF-36, or PROMIS norms were not identified. Nevertheless, inability to tolerate meals, recurrent vomiting, nutritional dependence, and chronic pain can markedly impair physical, psychological, educational, occupational, and social functioning. The prospective study explicitly required poor quality of life for one clinical inclusion pathway. (NCT03416647 chunk 1)

## 4. Genetic and molecular information

SMAS is not currently defined by a molecular lesion. No causal gene, HGNC identifier, pathogenic germline or somatic variant, variant class, allele frequency, penetrance, anticipation, founder effect, carrier frequency, modifier gene, epigenetic defect, or recurrent chromosomal abnormality was identified.

Accordingly:

- **ClinVar-style variant classification:** not applicable.
- **WES/WGS, gene panels, CMA, karyotyping, FISH, mtDNA, and repeat-expansion testing:** not indicated for diagnosing SMAS itself.
- Genetic evaluation may be appropriate only when a separate syndromic, connective-tissue, developmental, or neuromuscular disorder is clinically suspected.
- No validated pharmacogenomic recommendation exists for SMAS treatment.

## 5. Environmental and lifestyle information

The clinically meaningful “environmental” exposures are circumstances producing weight loss or anatomical distortion rather than toxicants. Restrictive eating, inadequate caloric intake, prolonged illness, catabolic states, spinal correction, and postoperative anatomical changes are the principal acquired contexts. Retroperitoneal fat is directly relevant: a 510-participant CT study was designed to relate aortomesenteric geometry to visceral and subcutaneous fat, with 500 non-SMAS and 10 SMAS participants. (NCT03937193 chunk 1)

Smoking and alcohol have no established disease-specific causal association. Exercise is not intrinsically causal, although extreme energy imbalance could contribute indirectly. No bacterial, viral, fungal, or parasitic trigger is established.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream trigger:** rapid weight loss, low visceral fat, altered spinal/mesenteric anatomy, or postoperative tension.
2. **Structural intermediate:** reduced fat cushion and narrowing of the SMA–aorta angle and distance.
3. **Primary lesion:** extrinsic compression of D3.
4. **Functional consequence:** impaired chyme passage, proximal duodenal/gastric stasis and dilation, vomiting, reflux, and postprandial pain.
5. **Downstream systemic effects:** reduced intake, dehydration, electrolyte abnormalities, malnutrition, and additional fat loss.
6. **Complications:** mucosal injury/ulceration, aspiration, perforation, pancreatitis, and potentially severe metabolic deterioration. (galimov2022thecomplicationof pages 2-3, galimov2022thecomplicationof pages 3-4, NCT03416647 chunk 1, galimov2022thecomplicationof pages 4-5)

This is principally a biomechanical obstruction. No disease-defining Wnt, MAPK, mTOR, PI3K–AKT, immune, inflammatory, apoptotic, autophagic, protein-folding, receptor, ion-channel, or enzyme-deficiency pathway is established. Likewise, no reproducible transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, multi-omic, or CRISPR-screen signature was identified.

**Suggested GO biological-process labels:** digestive-system process; gastrointestinal motility; regulation of body weight; response to nutrient; intestinal absorption. These are annotation suggestions, not demonstrated molecular mechanisms. Relevant cell populations are ordinary duodenal epithelium, smooth-muscle cells, enteric neurons, vascular endothelial/smooth-muscle cells, and adipocytes; none is a selectively diseased cell type. Suggested CL labels therefore include enterocyte, intestinal epithelial cell, smooth-muscle cell, enteric neuron, endothelial cell, and adipocyte.

## 7. Anatomical structures affected

- **Primary organ/site:** D3, the horizontal/transverse duodenum.
- **Compression boundaries:** SMA anteriorly; abdominal aorta and vertebral column posteriorly.
- **Relevant tissue:** the aortomesenteric/retroperitoneal adipose cushion.
- **Secondary involvement:** proximal duodenum and stomach through dilation and stasis; esophagus and lungs through reflux/aspiration; pancreas in rare obstructive pancreatitis.
- **Body systems:** primarily digestive; secondarily nutritional/metabolic and respiratory.
- **Lateralization:** not applicable.
- **Subcellular compartment:** none specifically implicated.

Suggested UBERON labels are *duodenum*, *third part of duodenum*, *superior mesenteric artery*, *abdominal aorta*, *retroperitoneal region*, *adipose tissue*, *stomach*, and *vertebral column*. Exact ontology IDs should be mapped against the selected UBERON release rather than inferred from names.

## 8. Temporal development

Onset can be acute following rapid weight loss, trauma, or spinal/abdominal surgery, or chronic and insidious. The highest reported occurrence is in adolescents and young adults, but disease is documented across childhood, adulthood, and older age. One reviewed source reports a peak at 10–30 years. (galimov2022thecomplicationof pages 2-3)

There is no universally accepted stage system. A practical clinical sequence is:

1. intermittent postprandial symptoms;
2. persistent obstruction with reduced intake and weight loss;
3. severe nutritional/metabolic compromise or complications;
4. recovery after restoration of the fat cushion or surgical bypass.

The course may remit with successful weight restoration, recur if weight is again lost, or remain chronic if obstruction and nutritional depletion perpetuate each other. The principal intervention window is before profound malnutrition, aspiration, perforation, or other complications develop.

## 9. Inheritance and population epidemiology

Reported prevalence estimates vary approximately from **0.1% to 0.78%** in selected radiographic or clinical populations, with a reported female-to-male ratio near **2:1** and concentration in the 10–30-year age range. These are not robust population-incidence estimates and should not be interpreted as contemporary global prevalence. No reliable annual incidence per 100,000 was identified. (galimov2022thecomplicationof pages 2-3)

No established ethnic founder population, endemic geography, consanguinity association, carrier state, penetrance, or expressivity framework applies. Geographic differences are likely dominated by referral patterns, nutritional exposures, surgical practice, and ascertainment. The Chinese normative CT study illustrates active work to derive population-specific reference distributions rather than assuming one universal angle or distance threshold. (NCT03937193 chunk 1)

## 10. Diagnostics

### Diagnostic approach

Diagnosis requires **both** a compatible obstructive phenotype and imaging evidence of D3 compression. A narrow angle or distance alone can occur without symptomatic SMAS and should not be treated as diagnostic in isolation.

**Preferred imaging:** contrast-enhanced abdominal CT with sagittal reconstruction measures the aortomesenteric angle; axial images measure distance and show D3 compression and proximal gastric/duodenal dilation. CT or MR angiography can define vascular geometry. Oral water-soluble contrast or an upper-GI/barium series may show proximal dilation, abrupt hold-up at D3, delayed transit, and sometimes positional improvement. Ultrasound can measure angle/distance without radiation but is operator- and body-habitus-dependent. (galimov2022thecomplicationof pages 2-3, galimov2022thecomplicationof pages 3-4, galimov2022thecomplicationof pages 1-2, NCT03416647 chunk 1)

Commonly used values are:

- normal angle approximately 35–65° or 38–80°;
- normal distance approximately 10–28 mm;
- strongly suggestive abnormal geometry: angle **<22°** and/or distance **<8 mm**;
- broader case-literature cutoffs: angle **<35°** and distance **<10 mm**.

A published case measured 14° and 6 mm. Variation in normal and abnormal cutoffs reinforces the need for clinical-radiological concordance. (galimov2022thecomplicationof pages 2-3, galimov2022thecomplicationof pages 3-4, NCT07115472 chunk 1)

A current pediatric observational study, NCT04515251, is prospectively establishing age-, BMI-, and fat-adjusted ultrasound ranges in 289 children aged 10–15 years, highlighting that pediatric reference standards remain under development. ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT04515251. (NCT04515251 chunk 1)

### Laboratory and other testing

There is no disease-specific blood, urine, tissue, genetic, or circulating biomarker. Laboratory studies assess consequences and alternative diagnoses: CBC, electrolytes, bicarbonate, renal and hepatic function, glucose, magnesium, phosphate, calcium, albumin/prealbumin with appropriate caution, inflammatory markers, lipase, and nutritional deficiencies. Endoscopy may exclude luminal lesions and evaluate retained contents or mucosal injury but cannot by itself establish extrinsic D3 compression. Biopsy, electrophysiology, PET, and omics testing have no routine role.

### Differential diagnosis

Important alternatives include gastroparesis, functional dyspepsia, cyclic vomiting/cannabinoid hyperemesis, eating disorders, peptic ulcer disease, pancreatitis, annular pancreas, malrotation/Ladd bands, duodenal web or tumor, Crohn disease, retroperitoneal mass, adhesions, chronic intestinal pseudo-obstruction, and other vascular-compression syndromes. Malignancy, motility disorders, and severe psychiatric illness were specifically excluded from the prospective surgical protocol, illustrating the need to avoid attributing nonspecific symptoms to incidental vascular geometry. (NCT03416647 chunk 1)

There is no population, newborn, carrier, or cascade screening program. Targeted imaging is reasonable in a high-risk patient with rapid weight loss or recent spinal surgery who develops persistent postprandial pain and vomiting.

## 11. Outcome and prognosis

Timely diagnosis and reversal or bypass of obstruction generally permit nutritional recovery and symptom improvement. A prospective cohort enrolled 39 patients, all treated with duodenojejunostomy, and assessed symptoms, BMI, and medication requirements at a median **47 months** (IQR 34–72). PMID 30291587; publication: *Journal of Gastrointestinal Surgery*, May 2019; https://pubmed.ncbi.nlm.nih.gov/30291587/. (NCT03416647 chunk 1)

A 2022 case had an uncomplicated postoperative course, pain relief, weight gain, and discharge nine days after surgery. This is illustrative but not a population response rate. (galimov2022thecomplicationof pages 3-4, galimov2022thecomplicationof pages 1-2)

Potential morbidity includes chronic pain, inability to eat, malnutrition, dehydration, electrolyte disorders, aspiration pneumonia, acute pancreatitis, gastric perforation, ulcer disease, and repeated hospitalization. Older case-based literature reports mortality as high as **33% in untreated or severely delayed disease**, but this figure is likely affected by historical care and selection bias and should not be presented as a modern average mortality rate. (galimov2022thecomplicationof pages 2-3, galimov2022thecomplicationof pages 4-5)

No validated five- or ten-year survival estimate, life-expectancy decrement, prognostic molecular biomarker, or disease-specific quality-of-life instrument was identified. Favorable factors are early recognition, reversible weight-loss trigger, successful nutritional restoration, and absence of severe complications; persistent symptoms despite adequate nutrition and coexisting motility or functional disorders complicate prognosis.

## 12. Treatment

### Initial conservative management

For a hemodynamically stable patient without perforation or another surgical emergency:

1. nasogastric decompression when vomiting or marked dilation is present;
2. intravenous fluid, electrolyte, and acid–base correction;
3. antiemetic and symptom-directed therapy;
4. small, frequent, energy-dense meals when tolerated;
5. enteral feeding distal to the obstruction, such as nasojejunal feeding, if oral intake is inadequate;
6. parenteral nutrition when enteral feeding is impossible or insufficient;
7. positional maneuvers—left lateral decubitus, prone, or knee-chest—may transiently reduce compression;
8. multidisciplinary treatment of the precipitating illness or eating disorder.

The objective is weight restoration and reconstitution of the fat pad, not merely suppression of nausea. The refractory-SMAS trial operationally defines failed conservative therapy as failure of decompression, enteral nutrition, and parenteral nutrition. (NCT07115472 chunk 1)

Suggested NCIT-style intervention labels include *Gastrointestinal Decompression*, *Enteral Nutrition*, *Parenteral Nutrition*, *Nutritional Support*, and *Antiemetic Therapy*. No SMAS-specific pharmacotherapy is approved, and no pharmacogenomic algorithm applies.

### Surgery and intervention

**Laparoscopic duodenojejunostomy** bypasses the compressed segment and is the best-supported definitive operation for refractory disease. Indications include persistent obstruction despite an adequate nutritional trial, inability to restore weight, recurrent hospitalization, severe complications, or a fixed anatomical cause. The 39-patient prospective cohort used duodenojejunostomy, with or without duodenal resection. (NCT03416647 chunk 1)

Other operations include Strong’s procedure—division of the ligament of Treitz and duodenal mobilization—gastrojejunostomy, duodenal derotation, and selected alternative bypass procedures. Terminology must be used carefully: Strong’s procedure is anatomically distinct from duodenojejunostomy, although some case reports describe combined mobilization and anastomosis. A 2022 report achieved symptom resolution after laparoscopic operative treatment. (galimov2022thecomplicationof pages 3-4, galimov2022thecomplicationof pages 4-5)

Potential surgical adverse events include leak, bleeding, infection, delayed gastric emptying, persistent symptoms, adhesive obstruction, nutritional problems, and reoperation. Evidence comparing procedures remains limited.

### Recent and ongoing clinical research

- **NCT03416647:** completed, single-group prospective cohort; 39 participants; duodenojejunostomy; outcomes included symptom score, BMI, and medical-treatment need over median 47 months. The linked publication is PMID 30291587. https://clinicaltrials.gov/study/NCT03416647. (NCT03416647 chunk 1)
- **NCT06970093:** small randomized, open-label comparison of one-anastomosis gastric bypass versus duodenojejunostomy; 20 participants, 12-month symptoms and BMI endpoints. Although enrollment began in March 2024, the registry was first posted in May 2025; no efficacy results were available in the retrieved record. https://clinicaltrials.gov/study/NCT06970093. (NCT06970093 chunk 1, NCT06970093 chunk 2)
- **NCT07115472:** 45-patient single-group study of fluoxetine, 20–60 mg/day, in refractory SMAS specifically with DSM-5 somatic symptom disorder. This tests treatment of a comorbidity, not reversal of anatomical compression, and should not be generalized to routine SMAS. No posted efficacy result was retrieved. https://clinicaltrials.gov/study/NCT07115472. (NCT07115472 chunk 1)
- **NCT03937193:** completed 510-participant CT study of angle, distance, and retroperitoneal fat in a young Chinese population. https://clinicaltrials.gov/study/NCT03937193. (NCT03937193 chunk 1)
- **NCT04515251:** recruiting pediatric normative ultrasound study with estimated enrollment of 289 and estimated completion in December 2026. (NCT04515251 chunk 1)

Gene, cell, RNA, targeted molecular, and immunotherapies have no established role.

## 13. Prevention

### Primary prevention

There is no vaccine, prophylactic medication, genetic screening, or universal prevention program. In high-risk settings, practical measures are nutritional assessment before and after major surgery, prevention of excessive perioperative weight loss, early dietitian involvement, and close monitoring of patients with severe scoliosis, spinal correction, catabolic illness, or restrictive eating.

### Secondary prevention

Persistent vomiting and postprandial pain after rapid weight loss or spinal/abdominal surgery should prompt early imaging. Angle and distance should be interpreted with demonstrated duodenal obstruction rather than used as asymptomatic screening tests.

### Tertiary prevention

Prevent recurrence and complications through sustained nutritional rehabilitation, treatment of the precipitating disorder, monitoring of weight/electrolytes, aspiration precautions when vomiting is severe, and timely surgery when conservative treatment fails. Genetic counseling and reproductive testing are not indicated for isolated SMAS.

## 14. Other species and natural disease

No well-characterized naturally occurring veterinary counterpart, breed predisposition, orthologous causal gene, zoonotic potential, or cross-species transmission was identified. Because SMAS is a mechanical relationship among the duodenum, SMA, aorta, spine, and fat pad, conceptually similar compression could occur in another species, but this should not be entered as a validated comparative-disease association without veterinary primary evidence.

## 15. Model organisms

No standardized mouse, rat, zebrafish, invertebrate, cellular, organoid, iPSC, knockout, knock-in, or humanized model was identified. Experimental manipulation of body weight or surgical alteration of mesenteric anatomy might model selected biomechanical features, but such an induced model would not reproduce the full human symptom complex and could create major welfare and translational limitations. Human CT/MR/ultrasound measurements, computational geometry, and clinical cohorts are currently more directly relevant than molecular model organisms.

## Expert synthesis and knowledge-base recommendations

1. Classify SMAS as an **acquired structural duodenal-obstruction syndrome**, not a genetic or primary vascular-occlusive disease.
2. Encode the primary causal chain as **loss of aortomesenteric adipose cushion/anatomical distortion → reduced angle and distance → extrinsic D3 compression → proximal obstruction → reduced intake and further weight loss**.
3. Require clinical-radiological concordance; **<22° and <8 mm are supportive thresholds, not stand-alone diagnostic criteria**. Population-, age-, BMI-, and technique-dependent reference variation remains an active research issue. (NCT07115472 chunk 1, NCT04515251 chunk 1, NCT03937193 chunk 1)
4. Treat nutritional restoration and decompression as first-line care, with laparoscopic duodenojejunostomy as the principal definitive operation for persistent, fixed, or complicated disease. (NCT03416647 chunk 1)
5. Mark gene, variant, inheritance, molecular pathway, omics, biomarker, animal-disease, and model-organism fields as **“not established”**, rather than filling them with speculative associations.
6. Evidence certainty is moderate for the core anatomy and diagnostic concept, but low-to-moderate for exact epidemiology, optimal duration of conservative therapy, comparative surgical effectiveness, and long-term quality-of-life outcomes.

References

1. (galimov2022thecomplicationof pages 2-3): O. V. Galimov, V. O. Khanov, H.M. H. Karkhani, Sh. Bhawna, and T. R. Ibragimov. The complication of decrease in aorto-mesenteric angle and distance its diagnosis and treatment: case report. Creative surgery and oncology, 12:123-127, Jul 2022. URL: https://doi.org/10.24060/2076-3093-2022-12-2-123-127, doi:10.24060/2076-3093-2022-12-2-123-127. This article has 0 citations.

2. (galimov2022thecomplicationof pages 1-2): O. V. Galimov, V. O. Khanov, H.M. H. Karkhani, Sh. Bhawna, and T. R. Ibragimov. The complication of decrease in aorto-mesenteric angle and distance its diagnosis and treatment: case report. Creative surgery and oncology, 12:123-127, Jul 2022. URL: https://doi.org/10.24060/2076-3093-2022-12-2-123-127, doi:10.24060/2076-3093-2022-12-2-123-127. This article has 0 citations.

3. (NCT03416647 chunk 1): Angelica Ganss. SMAS: a Prospective Study in a Single Institution. Azienda Ospedaliera di Padova. 2008. ClinicalTrials.gov Identifier: NCT03416647

4. (galimov2022thecomplicationof pages 3-4): O. V. Galimov, V. O. Khanov, H.M. H. Karkhani, Sh. Bhawna, and T. R. Ibragimov. The complication of decrease in aorto-mesenteric angle and distance its diagnosis and treatment: case report. Creative surgery and oncology, 12:123-127, Jul 2022. URL: https://doi.org/10.24060/2076-3093-2022-12-2-123-127, doi:10.24060/2076-3093-2022-12-2-123-127. This article has 0 citations.

5. (NCT07115472 chunk 1): Zhifeng Zhao, PhD. Fluoxetine in Refractory Superior Mesenteric Artery Syndrome by Targeting Comorbid Somatic Symptom Disorder. Xijing Hospital of Digestive Diseases. 2024. ClinicalTrials.gov Identifier: NCT07115472

6. (NCT04515251 chunk 1): Marirosa Cristallo Lacalamita. Ultrasound Evaluation of Superior Mesenteric Artery Measurements in a Healthy Pediatric Population. Ente Ospedaliero Cantonale, Bellinzona. 2020. ClinicalTrials.gov Identifier: NCT04515251

7. (NCT06970093 chunk 1):  Comparison of One Anastomisis Gastric Bypass and Duodeno-Jejunostomy for Treating SMA Syndrome. Ain Shams University. 2024. ClinicalTrials.gov Identifier: NCT06970093

8. (NCT03937193 chunk 1): Professor Winnie W.C. Chu. Normal Range of Superior Mesenteric Artery in Young Chinese Population and Its Correlation With Retroperitoneal Adipose Tissue. Chinese University of Hong Kong. 2019. ClinicalTrials.gov Identifier: NCT03937193

9. (galimov2022thecomplicationof pages 4-5): O. V. Galimov, V. O. Khanov, H.M. H. Karkhani, Sh. Bhawna, and T. R. Ibragimov. The complication of decrease in aorto-mesenteric angle and distance its diagnosis and treatment: case report. Creative surgery and oncology, 12:123-127, Jul 2022. URL: https://doi.org/10.24060/2076-3093-2022-12-2-123-127, doi:10.24060/2076-3093-2022-12-2-123-127. This article has 0 citations.

10. (NCT06970093 chunk 2):  Comparison of One Anastomisis Gastric Bypass and Duodeno-Jejunostomy for Treating SMA Syndrome. Ain Shams University. 2024. ClinicalTrials.gov Identifier: NCT06970093

## Artifacts

- [Edison artifact artifact-00](Superior_Mesenteric_Artery_Syndrome-deep-research-falcon_artifacts/artifact-00.md)