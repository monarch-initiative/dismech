---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-04T00:05:13.464815'
end_time: '2026-06-04T00:23:43.157833'
duration_seconds: 1109.69
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mandibulofacial dysostosis with microcephaly
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Mandibulofacial_Dysostosis_with_Microcephaly-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Mandibulofacial_Dysostosis_with_Microcephaly-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mandibulofacial dysostosis with microcephaly
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mandibulofacial dysostosis with microcephaly** covering all of the
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
- **Disease Name:** Mandibulofacial dysostosis with microcephaly
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mandibulofacial dysostosis with microcephaly** covering all of the
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


# Comprehensive Disease Characteristics Report: Mandibulofacial dysostosis with microcephaly (MFDM)

## Executive summary
Mandibulofacial dysostosis with microcephaly (MFDM) is a rare, predominantly de novo autosomal dominant craniofacial malformation syndrome caused by heterozygous loss-of-function variants or deletions in **EFTUD2**, which encodes the U5-116kD spliceosomal GTPase (a U5 snRNP core factor). Clinically, MFDM features mandibular/malar hypoplasia, external ear malformations with hearing loss, choanal and/or aural atresia, cleft palate, microcephaly, and developmental delay with prominent expressive language impairment; extracranial anomalies (cardiac defects, esophageal atresia/TEF, limb anomalies, seizures) occur in a substantial minority. Mechanistically, vertebrate models support a causal chain from EFTUD2-mediated splicing defects to p53-pathway activation and apoptosis in cranial neural crest and neural progenitor populations, driving craniofacial and neurodevelopmental phenotypes; p53 inhibition partially rescues craniofacial development in a mouse model but genetic Trp53 deletion does not fully rescue, implying additional p53-independent mechanisms. (lines2012haploinsufficiencyofa pages 1-2, lines2012haploinsufficiencyofa pages 4-5, beauchamp2022craniofacialdefectsin pages 1-2, beauchamp2021mutationineftud2 pages 10-12, chen2024atypicalmandibulofacialdysostosis pages 1-2)

## Target disease
- **Disease name:** Mandibulofacial dysostosis with microcephaly (MFDM) (lines2012haploinsufficiencyofa pages 1-2, luquetti2013“mandibulofacialdysostosiswith pages 1-3)
- **Category:** Mendelian
- **MONDO ID:** **MONDO_0012516** (“mandibulofacial dysostosis-microcephaly syndrome”) (OpenTargets Search: mandibulofacial dysostosis with microcephaly)

## 1. Disease information
### 1.1 Definition / overview
MFDM is a rare craniofacial-malformation syndrome characterized by mandibulofacial dysostosis and microcephaly with developmental delay and a recognizable facial gestalt; major recurrent findings include choanal atresia, cleft palate, and hearing loss. (lines2012haploinsufficiencyofa pages 1-2, lines2012haploinsufficiencyofa pages 4-5)

### 1.2 Key identifiers
- **OMIM phenotype:** **610536** (MFDM) (chen2024atypicalmandibulofacialdysostosis pages 5-6, luquetti2013“mandibulofacialdysostosiswith pages 1-3)
- **MONDO:** **MONDO_0012516** (OpenTargets Search: mandibulofacial dysostosis with microcephaly)

**Not retrieved with available tools in this run:** Orphanet ID, MeSH descriptor, ICD-10/ICD-11 codes.

### 1.3 Synonyms and alternative names
- “Mandibulofacial dysostosis with microcephaly (MFDM)” (lines2012haploinsufficiencyofa pages 1-2, luquetti2013“mandibulofacialdysostosiswith pages 1-3)
- “Mandibulofacial dysostosis, Guion-Almeida type” / “Guion-Almeida syndrome” (used in mechanistic and review contexts) (beauchamp2020missplicingofmdm2 pages 19-23, park2022thecoresplicing pages 13-14)
- “Mandibulofacial dysostosis-microcephaly syndrome” (MONDO naming) (OpenTargets Search: mandibulofacial dysostosis with microcephaly)

### 1.4 Evidence source type
Evidence used here is derived from **aggregated disease-level resources** (OpenTargets disease–gene association) and **primary patient cohorts/case reports/case series** plus **experimental model-organism studies**. (OpenTargets Search: mandibulofacial dysostosis with microcephaly, lines2012haploinsufficiencyofa pages 1-2, kohailan2022adenovo pages 2-4, beauchamp2021mutationineftud2 pages 10-12)

## 2. Etiology
### 2.1 Disease causal factors
**Genetic cause:** Heterozygous loss-of-function (LoF) variants and deletions in **EFTUD2** causing **haploinsufficiency** are the established cause of MFDM. (lines2012haploinsufficiencyofa pages 1-2, lines2012haploinsufficiencyofa pages 4-5, gandomi2015array‐cghisan pages 1-2)

A cohort-defining study concluded: **“Taken together, our findings are consistent with de novo haploinsufficiency of EFTUD2 as the cause of MFDM in all cases assessed to date.”** (lines2012haploinsufficiencyofa pages 4-5)

### 2.2 Risk factors
- **Genetic:** Pathogenic EFTUD2 variants (de novo most common). (lines2012haploinsufficiencyofa pages 1-2, jacob2020adenovo pages 1-2)
- **Environmental:** No MFDM-specific environmental risk factors were identified in the retrieved evidence.

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No MFDM-specific gene–environment interaction data were identified in the retrieved evidence.

## 3. Phenotypes
### 3.1 Core craniofacial and ENT phenotypes (with frequencies where available)
Large phenotype summaries compiled in recent MFDM literature report high-frequency craniofacial/ear manifestations, including:
- **Micrognathia:** 93/95 (98%) (kohailan2022adenovo pages 2-4)
- **Small/dysplastic pinnae:** 90/93 (97%) (kohailan2022adenovo pages 2-4)
- **Malar hypoplasia:** 84/90 (93%) (kohailan2022adenovo pages 2-4)
- **Microcephaly:** 84/95 (88%) (kohailan2022adenovo pages 2-4)
- **Cleft palate:** 45/94 (48%) (kohailan2022adenovo pages 2-4)
- **Hearing loss:** 75/89 (84%), with conductive 33/55 (60%), mixed 15/55 (27%), sensorineural 7/55 (13%) (kohailan2022adenovo pages 2-4)
- **Auditory canal atresia/stenosis:** 50/78 (64%) (kohailan2022adenovo pages 2-4)

In the original 12-person cohort, “Hearing loss, generally conductive, was reported in 10 of the 12 individuals,” and choanal/aural atresia, cleft palate, and congenital heart defects were each present in >50% of individuals. (lines2012haploinsufficiencyofa pages 4-5)

**Suggested HPO terms:** see ontology mapping table below (artifact-01).

### 3.2 Neurodevelopmental phenotypes
- **Developmental delay** is near-universal in compiled cohorts (e.g., 89/89, 100%). (kohailan2022adenovo pages 2-4)
- Expressive language is disproportionately affected; in the AJHG cohort, only ~50% attained any speech and **first words typically occurred at 20–30 months**. (lines2012haploinsufficiencyofa pages 3-4)

### 3.3 Extracranial phenotypes (examples with quantitative estimates)
Reported extracranial manifestations include:
- **Congenital heart defects:** 29/95 (31%) in a compiled summary (kohailan2022adenovo pages 2-4); in some descriptions, congenital heart disease is ~40% (jacob2020adenovo pages 1-2)
- **Esophageal atresia:** 24/91 (26%) in a compiled summary (kohailan2022adenovo pages 2-4); ~40% in a case-report summary (jacob2020adenovo pages 1-2)
- **Thumb anomalies:** 25/83 (30%) (kohailan2022adenovo pages 2-4)
- **Epileptic seizures:** 23/83 (28%) in a compiled summary (kohailan2022adenovo pages 2-4)

### 3.4 Onset, severity, progression
MFDM can present congenitally or with postnatal evolution. One cohort summary reports **congenital onset in 36/57 (63%)** versus **postnatal onset in 21/57 (37%)**. (kohailan2022adenovo pages 2-4)

Microcephaly can be progressive and severe; the original cohort reports head circumference eventually **3–6 SD below the mean** in severe/progressive cases. (lines2012haploinsufficiencyofa pages 1-2)

### 3.5 Imaging and laboratory phenotypes
Brain MRI can be normal or show nonspecific abnormalities; in one small subset of the original cohort, **2/4 MRIs were normal** and **2/4 showed delayed myelination or nonspecific white matter changes**. (lines2012haploinsufficiencyofa pages 3-4)

### 3.6 Quality of life impact
Direct, standardized QoL instruments (e.g., SF-36, EQ-5D) were not found in the retrieved MFDM-specific evidence. Functional impacts inferred from the phenotype include hearing impairment, airway/feeding problems, and developmental delay. (gandomi2015array‐cghisan pages 1-2, lines2012haploinsufficiencyofa pages 3-4)

## 4. Genetic / molecular information
### 4.1 Causal gene(s)
- **EFTUD2** (OMIM *603892; per case-report literature), encoding spliceosomal GTPase U5-116kD. (chen2024atypicalmandibulofacialdysostosis pages 5-6, jacob2020adenovo pages 1-2)

OpenTargets disease–gene association also identifies EFTUD2 as the sole top target linked to MONDO_0012516, with supporting literature. (OpenTargets Search: mandibulofacial dysostosis with microcephaly)

### 4.2 Pathogenic variant types and examples
MFDM-associated variants span multiple classes consistent with haploinsufficiency:
- **Deletions/CNVs** (supporting aCGH/CMA utility) (gandomi2015array‐cghisan pages 1-2)
- **Frameshift/nonsense/splice-site** variants in early cohort studies (lines2012haploinsufficiencyofa pages 4-5)
- **Synonymous splice-disrupting variant** demonstrated by RT-PCR showing exon 9 skipping and frameshift/premature stop (jacob2020adenovo pages 1-2)
- **Functionally verified splice-site variant** via minigene assay (lines2012haploinsufficiencyofa pages 4-5)

**2024 variant-spectrum expansion:** A novel heterozygous frameshifting insertion (c.215_216insT) was reported; the authors state it causes a premature stop and truncation, consistent with LoF. (chen2024atypicalmandibulofacialdysostosis pages 5-6)

### 4.3 Inheritance, penetrance, mosaicism
Inheritance is autosomal dominant with most cases de novo. Literature summaries note familial transmission occurs in a minority (e.g., ~19%) and germline mosaicism around ~6%. (jacob2020adenovo pages 1-2, chen2024atypicalmandibulofacialdysostosis pages 1-2)

### 4.4 Modifier genes / epigenetics
No MFDM-specific modifier gene or epigenetic mechanism evidence was identified in the retrieved sources.

## 5. Environmental information
No MFDM-specific environmental, lifestyle, or infectious contributors were identified in the retrieved evidence.

## 6. Mechanism / pathophysiology
### 6.1 Current mechanistic model (causal chain)
Evidence from vertebrate disease models supports the following chain:
1. **EFTUD2 haploinsufficiency** → impaired U5 snRNP spliceosome function and widespread splicing defects (lines2012haploinsufficiencyofa pages 1-2, beauchamp2021mutationineftud2 pages 1-2)
2. Recurrent **mis-splicing of Mdm2** (notably exon 3 skipping) → **p53 stabilization/activation** (beauchamp2021mutationineftud2 pages 10-12, beauchamp2021mutationineftud2 pages 1-2)
3. p53 activation → apoptosis in neural crest and neural progenitor contexts → depletion of craniofacial precursor cells (beauchamp2021mutationineftud2 pages 10-12, beauchamp2021mutationineftud2 pages 1-2)
4. Depletion/morphogenetic failure → craniofacial malformations and neurodevelopmental abnormalities (beauchamp2021mutationineftud2 pages 10-12, beauchamp2021mutationineftud2 pages 1-2)

A key statement from the Xenopus-focused review summarizes a common theme: “Animal models of NRS and MFDM indicate that MFD results from an early depletion of neural crest progenitors through a mechanism that involves apoptosis.” (park2022thecoresplicing pages 13-14)

### 6.2 Upstream vs downstream mechanisms
- **Upstream:** spliceosome dysfunction / alternative splicing defects (GO:0000398; GO:0000381) (lines2012haploinsufficiencyofa pages 1-2, beauchamp2021mutationineftud2 pages 1-2)
- **Intermediate:** p53 pathway activation; intrinsic apoptotic signaling (beauchamp2021mutationineftud2 pages 10-12)
- **Downstream:** reduced cranial neural crest cells; impaired craniofacial morphogenesis; microcephaly and developmental delay (beauchamp2021mutationineftud2 pages 10-12, beauchamp2021mutationineftud2 pages 1-2)

### 6.3 Key cell types and tissues implicated
- **Cranial neural crest cells** and **neural progenitors** are most strongly supported in model systems. (beauchamp2021mutationineftud2 pages 10-12, park2022thecoresplicing pages 13-14)

**Suggested CL terms:** see artifact-01.

### 6.4 Therapeutic mechanistic experiments (preclinical)
In a neural-crest-specific Eftud2 mouse model, p53 inhibition with **pifithrin-α** partially improved craniofacial development; one report noted **midbrain improvement in 3/11 treated mutants vs 0/41 untreated (p=0.0139)** and increased first pharyngeal arch size (p<0.05). (beauchamp2020missplicingofmdm2 pages 15-19, beauchamp2021mutationineftud2 pages 10-12)

However, genetic Trp53 deletion reduced apoptosis without rescuing craniofacial morphology or survival, supporting additional p53-independent contributions (mis-splicing of other transcripts). (beauchamp2022craniofacialdefectsin pages 1-2, beauchamp2022craniofacialdefectsin pages 10-12)

## 7. Anatomical structures affected
Primary affected structures include craniofacial skeleton and external/middle ear; choanae and palate are commonly involved, with variable CNS and extracranial organ involvement (heart, esophagus). (gandomi2015array‐cghisan pages 1-2, kohailan2022adenovo pages 2-4)

**Suggested UBERON terms:** see artifact-01.

## 8. Temporal development
MFDM is typically congenital or early childhood in presentation, with congenital vs postnatal onset reported (63% vs 37% in one summary). Microcephaly may be congenital or progressive postnatally. (kohailan2022adenovo pages 2-4, lines2012haploinsufficiencyofa pages 1-2)

## 9. Inheritance and population
### 9.1 Epidemiology
A 2024 report states MFDM prevalence is **<1/1,000,000** and that only approximately **150** cases with EFTUD2 mutations had been reported, acknowledging underestimation. (chen2024atypicalmandibulofacialdysostosis pages 1-2)

A separate 2024 report notes **126 cases** reported to date (context-dependent case counting). (lyulchevabennett2024dualdiagnosisof pages 1-2)

### 9.2 Population demographics
No robust sex ratio, geographic distribution, or founder-effect variants were identified in the retrieved evidence.

## 10. Diagnostics
### 10.1 Clinical recognition and differential diagnosis
MFDM may be misdiagnosed due to overlap with other craniofacial dysostoses (e.g., Treacher Collins syndrome, Nager syndrome, oculo-auriculo-vertebral spectrum, and atypical CHARGE). (chen2024atypicalmandibulofacialdysostosis pages 5-6, luquetti2013“mandibulofacialdysostosiswith pages 1-3)

### 10.2 Genetic testing strategy (real-world implementation)
- **WES/WGS (trio preferred)** is repeatedly used to resolve ambiguous craniofacial diagnoses and identify de novo EFTUD2 variants, with **Sanger confirmation**. (chen2024atypicalmandibulofacialdysostosis pages 5-6, luquetti2013“mandibulofacialdysostosiswith pages 1-3)
- For splice/synonymous candidates, **RNA-level functional validation** (RT-PCR) or **minigene assays** can demonstrate splicing disruption. (jacob2020adenovo pages 1-2, lines2012haploinsufficiencyofa pages 4-5)
- **Array-CGH/CMA** can detect EFTUD2 deletions and has been proposed as a **first-tier** test for EFTUD2-associated MFDM in congenital contexts. (gandomi2015array‐cghisan pages 1-2)

**2024 real-world genomics example:** A complex **EFTUD2 intragenic rearrangement** was detected via large-scale genomics programs (DDD and 100,000 Genomes), illustrating structural variant contributions and the utility of genome-wide testing beyond standard single-variant pipelines. (lyulchevabennett2024dualdiagnosisof pages 1-2)

### 10.3 Imaging and ancillary tests
- Craniofacial CT may help define zygomatic arch defects; the 2013 series recommended craniofacial CT for zygomatic arch clefting. (luquetti2013“mandibulofacialdysostosiswith pages 1-3)
- Audiology and ear evaluation are indicated due to high hearing-loss prevalence. (kohailan2022adenovo pages 2-4)

## 11. Outcome / prognosis
Long-term survival and life expectancy are not well quantified in the retrieved MFDM-specific sources. Severe neonatal airway/feeding problems, congenital heart defects, and esophageal atresia/TEF can drive early morbidity; some individuals survive into adolescence with special education support. (luquetti2013“mandibulofacialdysostosiswith pages 3-4, gandomi2015array‐cghisan pages 1-2)

## 12. Treatment
MFDM management is primarily supportive and multidisciplinary.

### 12.1 Supportive and surgical interventions
- **Airway/feeding:** Tracheostomy is reported in **11/54 (20%)** in a compiled summary; gastrostomy is reported in cohort descriptions and case series tables (without consistently extractable denominators in the retrieved excerpts). (kohailan2022adenovo pages 2-4, lines2012haploinsufficiencyofa pages 3-4)
- **Hearing:** High prevalence of conductive/mixed hearing loss supports hearing evaluation and management (e.g., hearing aids, surgical/ENT management), although device/surgery utilization rates were not available in the extracted evidence. (kohailan2022adenovo pages 2-4)
- **Speech/language and developmental supports:** Speech therapy and developmental interventions are used in practice (explicitly noted in at least one case report’s workup/management). (kohailan2022adenovo pages 2-4)

### 12.2 Experimental / mechanism-based approaches (preclinical)
Preclinical work in mouse suggests that reducing p53 activity (e.g., pifithrin-α) can partially rescue craniofacial development, but this is not a clinical therapy and p53 deletion does not fully rescue. (beauchamp2021mutationineftud2 pages 10-12, beauchamp2022craniofacialdefectsin pages 10-12)

### 12.3 MAXO term suggestions
See artifact-01.

## 13. Prevention
Primary prevention is not established for MFDM given its genetic etiology. Prevention in practice focuses on:
- **Genetic counseling** for autosomal dominant inheritance with predominant de novo occurrence and the possibility of parental mosaicism. (jacob2020adenovo pages 1-2, chen2024atypicalmandibulofacialdysostosis pages 1-2)
- **Prenatal/early diagnosis** using genome-wide testing (WES/WGS/CMA), especially in fetuses/newborns with suggestive anomalies. (gandomi2015array‐cghisan pages 1-2, chen2024atypicalmandibulofacialdysostosis pages 5-6)

## 14. Other species / natural disease
No naturally occurring veterinary MFDM analogs were identified in the retrieved evidence.

## 15. Model organisms
### 15.1 Zebrafish
Zebrafish eftud2 mutants show abnormal brain development with neuronal apoptosis and transcriptome-wide splicing defects, supporting a neurodevelopmental disease model and a p53-dependent apoptosis mechanism. (beauchamp2020missplicingofmdm2 pages 19-23)

### 15.2 Mouse
A neural crest-specific conditional Eftud2 deletion model produces craniofacial and brain malformations and lethality and implicates Mdm2 mis-splicing and p53 activation; partial rescue occurs with p53 inhibition. (beauchamp2021mutationineftud2 pages 10-12, beauchamp2022craniofacialdefectsin pages 1-2)

### 15.3 Xenopus
Knockdown studies of core splicing factors (including eftud2) implicate a requirement for neural crest formation and craniofacial development. (park2022thecoresplicing pages 13-14)

### 15.4 Model limitations
A simple heterozygous mouse exon 2 deletion line does not recapitulate MFDM well, suggesting the need for tissue-specific or allele-specific modeling strategies. (park2022thecoresplicing pages 13-14)

---

## High-value curated summaries

| Category | Summary |
|---|---|
| Disease | Mandibulofacial dysostosis with microcephaly (MFDM), also called mandibulofacial dysostosis-microcephaly syndrome / Guion-Almeida type (OpenTargets Search: mandibulofacial dysostosis with microcephaly, lines2012haploinsufficiencyofa pages 1-2, luquetti2013“mandibulofacialdysostosiswith pages 1-3) |
| Identifiers | MONDO: MONDO_0012516; OMIM: 610536 (OpenTargets Search: mandibulofacial dysostosis with microcephaly, chen2024atypicalmandibulofacialdysostosis pages 5-6, luquetti2013“mandibulofacialdysostosiswith pages 1-3) |
| Causal gene | EFTUD2 (elongation factor Tu GTP binding domain containing 2), encoding the U5-116 kD spliceosomal GTPase (OpenTargets Search: mandibulofacial dysostosis with microcephaly, chen2024atypicalmandibulofacialdysostosis pages 5-6, lines2012haploinsufficiencyofa pages 1-2, jacob2020adenovo pages 1-2) |
| Inheritance | Autosomal dominant; most reported cases are de novo heterozygous loss-of-function variants or deletions consistent with haploinsufficiency (lines2012haploinsufficiencyofa pages 1-2, jacob2020adenovo pages 1-2, lines2012haploinsufficiencyofa pages 4-5, gandomi2015array‐cghisan pages 1-2) |
| Variant spectrum | Deletions, frameshift, nonsense, splice-site, missense, start-loss, and synonymous splice-disrupting variants have been reported (jacob2020adenovo pages 1-2, lines2012haploinsufficiencyofa pages 4-5) |
| Core craniofacial features | Mandibular and maxillary hypoplasia, micrognathia, microtia/external ear anomalies, choanal atresia, cleft palate, characteristic dysmorphism (luquetti2013“mandibulofacialdysostosiswith pages 3-4, lines2012haploinsufficiencyofa pages 1-2, lines2012haploinsufficiencyofa pages 4-5, gandomi2015array‐cghisan pages 1-2, luquetti2013“mandibulofacialdysostosiswith pages 1-3) |
| Neurodevelopmental features | Microcephaly, developmental delay / intellectual disability, delayed psychomotor milestones; microcephaly may be congenital or postnatal and can become severe/progressive (luquetti2013“mandibulofacialdysostosiswith pages 3-4, lines2012haploinsufficiencyofa pages 1-2, jacob2020adenovo pages 1-2) |
| Quantitative clinical findings | Choanal/aural atresia, cleft palate, and congenital heart defects each reported in >50% of affected individuals in the original 12-person cohort; hearing loss in 10/12; head circumference eventually 3–6 SD below the mean in severe/progressive cases (lines2012haploinsufficiencyofa pages 1-2, lines2012haploinsufficiencyofa pages 4-5) |
| Extracranial findings | Esophageal atresia ~40%, congenital heart disease ~40%, thumb abnormalities ~25%, short stature in ~1/3; feeding/airway problems and abnormal brain myelination/white matter changes also reported (jacob2020adenovo pages 1-2, gandomi2015array‐cghisan pages 1-2) |
| Diagnostic approach | Clinical suspicion based on craniofacial pattern plus microcephaly/developmental delay; molecular confirmation by WES/WGS or trio exome; Sanger confirmation; RNA studies/minigene assays for splice variants; aCGH/CMA can detect pathogenic EFTUD2 deletions and has been proposed as a first-tier test in some congenital presentations (chen2024atypicalmandibulofacialdysostosis pages 5-6, jacob2020adenovo pages 1-2, gandomi2015array‐cghisan pages 1-2, luquetti2013“mandibulofacialdysostosiswith pages 1-3) |
| Differential diagnosis clues | Phenotypic overlap with Treacher Collins syndrome, Nager syndrome, oculoauriculovertebral spectrum, and atypical CHARGE syndrome can delay diagnosis (chen2024atypicalmandibulofacialdysostosis pages 5-6, luquetti2013“mandibulofacialdysostosiswith pages 1-3) |
| Mechanistic chain | EFTUD2 haploinsufficiency → impaired U5 spliceosome function / transcriptome-wide splicing defects → increased exon skipping including Mdm2 exon 3 skipping → p53 stabilization/activation → apoptosis of neural crest and neural progenitor cells → depletion of craniofacial precursor cells → craniofacial malformations and microcephaly (beauchamp2020missplicingofmdm2 pages 15-19, beauchamp2022craniofacialdefectsin pages 1-2, beauchamp2020missplicingofmdm2 pages 19-23, beauchamp2020missplicingofmdm2 pages 1-5, beauchamp2021mutationineftud2 pages 10-12, beauchamp2021mutationineftud2 pages 1-2) |
| Affected developmental cell populations | Cranial neural crest cells and neural progenitors are the best-supported vulnerable populations in model systems (park2022thecoresplicing pages 13-14, beauchamp2020missplicingofmdm2 pages 15-19, beauchamp2022craniofacialdefectsin pages 1-2, beauchamp2021mutationineftud2 pages 10-12) |
| Model-organism evidence | Zebrafish eftud2 mutants show abnormal brain development and p53-dependent apoptosis; neural-crest-specific mouse Eftud2 loss causes brain/craniofacial malformations and prenatal lethality; Xenopus knockdown supports a neural crest/craniofacial developmental requirement (park2022thecoresplicing pages 13-14, beauchamp2020missplicingofmdm2 pages 19-23, beauchamp2020missplicingofmdm2 pages 1-5, beauchamp2021mutationineftud2 pages 10-12) |
| Rescue evidence | Pharmacologic p53 inhibition with pifithrin-α partially improved morphology in the mouse model: midbrain improvement in 3/11 treated mutants vs 0/41 untreated; first pharyngeal arch size increased significantly (p<0.05). However, Trp53 deletion reduced apoptosis without fully rescuing craniofacial defects or survival, indicating additional p53-independent mis-splicing mechanisms (beauchamp2020missplicingofmdm2 pages 15-19, beauchamp2022craniofacialdefectsin pages 1-2, beauchamp2021mutationineftud2 pages 10-12, beauchamp2022craniofacialdefectsin pages 10-12) |
| Current understanding | MFDM is best understood as an EFTUD2-related craniofacial spliceosomopathy with dominant loss-of-function, variable expressivity, and disease mechanisms centered on selective developmental vulnerability of cranial neural crest and neuroepithelial lineages (lines2012haploinsufficiencyofa pages 1-2, park2022thecoresplicing pages 13-14, beauchamp2022craniofacialdefectsin pages 1-2, beauchamp2021mutationineftud2 pages 1-2) |


*Table: This table condenses the main identifiers, genetics, clinical spectrum, diagnostic approaches, and disease mechanism for EFTUD2-related mandibulofacial dysostosis with microcephaly. It is useful as a quick-reference scaffold for a fuller disease knowledge base entry.*

| Section | Item | Suggested ontology term(s) | Notes/frequency |
|---|---|---|---|
| Phenotype | Microcephaly | Microcephaly (HP:0000252) | Common and often severe/progressive; reported in 84/95 (88%), with congenital or postnatal onset in reported cohorts |
| Phenotype | Micrognathia / mandibular hypoplasia | Micrognathia (HP:0000347); Mandibular hypoplasia (HP:0000347) | Very common; micrognathia 93/95 (98%) in one summary cohort |
| Phenotype | Malar hypoplasia | Malar flattening (HP:0000272) | Common; 84/90 (93%) in one summary cohort |
| Phenotype | Microtia / dysplastic external ears | Microtia (HP:0008551); Abnormality of the pinna (HP:0000377); Dysplastic pinna (HP:0008553) | Very common; small/dysplastic pinnae 90/93 (97%) |
| Phenotype | Preauricular tags | Preauricular skin tag (HP:0000384) | Recurrent ear-associated feature |
| Phenotype | Hearing loss | Hearing impairment (HP:0000365); Conductive hearing impairment (HP:0000405); Mixed hearing impairment (HP:0000408); Sensorineural hearing impairment (HP:0000407) | Common; hearing loss 75/89 (84%); conductive predominates |
| Phenotype | Auditory canal stenosis / atresia | External auditory canal stenosis (HP:0000400); External auditory canal atresia (HP:0000413) | Frequent; auditory atresia/stenosis 50/78 (64%) |
| Phenotype | Choanal atresia | Choanal atresia (HP:0000453) | Recurrent major craniofacial finding |
| Phenotype | Cleft palate | Cleft palate (HP:0000175) | Common; 45/94 (48%) in one cohort summary |
| Phenotype | Cleft zygomatic arch / zygomatic defect | Abnormal zygomatic bone morphology (HP:0011327) | Expanded phenotype; CT can show unilateral or bilateral zygomatic arch clefting |
| Phenotype | Maxillary hypoplasia / midface hypoplasia | Maxillary hypoplasia (HP:0000327); Midface retrusion (HP:0011800) | Recurrent craniofacial feature |
| Phenotype | Global developmental delay | Global developmental delay (HP:0001263) | Very common; developmental delay reported in essentially all compiled cases |
| Phenotype | Intellectual disability | Intellectual disability (HP:0001249) | Common; severity variable |
| Phenotype | Speech delay / expressive language delay | Delayed speech and language development (HP:0000750); Expressive language delay (HP:0002474) | Common; first words often at 20–30 months |
| Phenotype | Motor delay | Delayed gross motor development (HP:0002194) | Common; delayed walking/sitting reported |
| Phenotype | Seizures | Seizure (HP:0001250) | Reported in subsets; 23/83 (28%) in one summary cohort |
| Phenotype | Congenital heart defect | Congenital heart malformation (HP:0001627); Atrial septal defect (HP:0001631) | Recurrent extracranial feature; ~31% in one summary cohort |
| Phenotype | Esophageal atresia / tracheoesophageal anomaly | Esophageal atresia (HP:0002031); Tracheoesophageal fistula (HP:0002575) | Recurrent extracranial feature; esophageal atresia 24/91 (26%) |
| Phenotype | Thumb anomalies | Abnormal thumb morphology (HP:0009609); Triphalangeal thumb (HP:0001199); Proximally placed thumb (HP:0009623) | Reported in subsets; ~25–30% |
| Phenotype | Short stature / growth delay | Short stature (HP:0004322); Postnatal growth retardation (HP:0008897) | Reported in about one-third in some summaries |
| Phenotype | Feeding difficulty / dysphagia | Feeding difficulties (HP:0011968); Dysphagia (HP:0002015) | Common in severe neonatal cases; may accompany Pierre Robin sequence or EA/TEF |
| Phenotype | Delayed myelination | Delayed CNS myelination (HP:0012447) | Seen on MRI in a subset |
| Phenotype | White matter abnormality | Abnormality of cerebral white matter (HP:0002500) | Nonspecific white matter changes reported on MRI |
| Phenotype | Ventricular enlargement | Ventriculomegaly (HP:0002119) | Mild posterior lateral ventricular dilation reported in some cases |
| Phenotype | Epibulbar dermoid | Epibulbar dermoid (HP:0001140) | Expanded phenotype; reported in individual cases |
| Mechanism | Pre-mRNA splicing defect | mRNA splicing, via spliceosome (GO:0000398) | Core upstream disease mechanism |
| Mechanism | Alternative splicing dysregulation | Regulation of alternative mRNA splicing, via spliceosome (GO:0000381) | Includes exon skipping events such as Mdm2 exon 3 skipping |
| Mechanism | Neural crest development defect | Neural crest cell development (GO:0014032); Neural crest cell migration (GO:0001755) | Best-supported developmental cell-population vulnerability |
| Mechanism | Apoptotic cell death | Apoptotic process (GO:0006915); Intrinsic apoptotic signaling pathway (GO:0097193) | Increased in neural crest/neural progenitor contexts |
| Mechanism | p53 pathway activation | Signal transduction by p53 class mediator (GO:0072331); Regulation of transcription by p53 class mediator (GO:0072332) | Supported by mouse and zebrafish mechanistic studies |
| Mechanism | Craniofacial morphogenesis defect | Craniofacial skeletal system development (GO:1904888); Branchiomeric skeletal muscle development / pharyngeal arch development-related annotation | Downstream morphogenetic consequence |
| Mechanism | Neurodevelopmental defect | Brain development (GO:0007420); Forebrain development (GO:0030900) | Relevant to microcephaly and developmental delay |
| Cell type | Cranial neural crest cells | Neural crest cell (CL:0000007); Cranial neural crest cell (CL:0002320) | Strongest disease-relevant cell population from models |
| Cell type | Neural progenitor cells | Neural progenitor cell (CL:0000047) | Supported by zebrafish and brain-development studies |
| Cell type | Neuroepithelial cells | Neuroepithelial cell (CL:0000644) | Relevant to early CNS development |
| Cell type | Chondrocytes | Chondrocyte (CL:0000138) | Relevant to craniofacial cartilage development |
| Cell type | Osteoblast lineage cells | Osteoblast (CL:0000062) | Relevant to mandibular/zygomatic/maxillary hypoplasia |
| Anatomy | Mandible | mandible (UBERON:0001684) | Primary craniofacial skeletal site |
| Anatomy | Maxilla | maxilla (UBERON:0001685) | Primary craniofacial skeletal site |
| Anatomy | Zygomatic bone / arch | zygomatic bone (UBERON:0001687) | Site of clefting/hypoplasia in some patients |
| Anatomy | External ear / pinna | external ear (UBERON:0001032); pinna (UBERON:0001691) | Major affected structure |
| Anatomy | External auditory canal | external auditory canal (UBERON:0000912) | Frequent stenosis/atresia |
| Anatomy | Choana | choana (UBERON:0001719) | Choanal atresia site |
| Anatomy | Palate | secondary palate (UBERON:0001708) | Cleft palate site |
| Anatomy | Brain / cerebral white matter | brain (UBERON:0000955); cerebral white matter (UBERON:0002316) | Relevant to microcephaly, delayed myelination, white matter abnormalities |
| Anatomy | Esophagus | esophagus (UBERON:0001043) | Relevant to esophageal atresia |
| Anatomy | Heart / atrial septum | heart (UBERON:0000948); atrial septum (UBERON:0002085) | Relevant to congenital heart disease/ASD |
| Treatment/management | Tracheostomy | tracheostomy (MAXO:0000128) | Reported in severe airway cases; 11/54 (20%) in one cohort summary |
| Treatment/management | Gastrostomy / feeding tube support | gastrostomy (MAXO:0000126); enteral tube feeding (MAXO:0000106) | Used in severe feeding/airway cases |
| Treatment/management | Hearing support | hearing aid use (MAXO:0000058) | Reasonable management action for conductive/mixed hearing loss |
| Treatment/management | Speech therapy | speech therapy (MAXO:0000016) | Common supportive intervention for expressive language delay |
| Treatment/management | Genetic testing | sequence analysis (MAXO:0000147); exome sequencing (MAXO:0000137); genome sequencing (MAXO:0000138); chromosomal microarray analysis (MAXO:0000014) | Core diagnostic/management action in modern care pathways |
| Treatment/management | Airway support | airway management (MAXO:0000112) | Relevant for choanal atresia, glossoptosis, neonatal respiratory compromise |
| Treatment/management | Feeding support | feeding therapy (MAXO:0000104); nutritional supplementation/support (MAXO:0000105) | Relevant for dysphagia and poor suck/swallow coordination |
| Treatment/management | Craniofacial surgery | craniofacial surgical intervention (MAXO:0001173) | Disease-specific reconstructive needs may arise; evidence is case-based |
| Treatment/management | Cardiac evaluation/intervention | cardiology evaluation/intervention (MAXO term family) | Supportive management for CHD/ASD |
| Treatment/management | Experimental p53 inhibition | small molecule inhibitor treatment (MAXO:0000013) | Preclinical only; pifithrin-α partially rescued mouse craniofacial phenotype |


*Table: This table maps evidence-based mandibulofacial dysostosis with microcephaly features to suggested ontology terms across HPO, GO, CL, UBERON, and MAXO. It is useful as a knowledge-base curation scaffold for phenotype, mechanism, anatomy, cell type, and management annotations. (lines2012haploinsufficiencyofa pages 1-2, lines2012haploinsufficiencyofa pages 4-5, park2022thecoresplicing pages 13-14, beauchamp2022craniofacialdefectsin pages 1-2, chen2024atypicalmandibulofacialdysostosis pages 1-2, lyulchevabennett2024dualdiagnosisof pages 1-2, gandomi2015array‐cghisan pages 1-2, kohailan2022adenovo pages 2-4, lines2012haploinsufficiencyofa pages 3-4)*

---

## Recent developments (2023–2024) and real-world implementations
- **2024 variant expansion and updated epidemiology:** A 2024 MFDM case report emphasizes rarity (prevalence <1/1,000,000) and ~150 molecularly confirmed cases, and reports a new pathogenic EFTUD2 frameshift insertion detected by WES. (Apr 2024; https://doi.org/10.1002/mgg3.2426) (chen2024atypicalmandibulofacialdysostosis pages 1-2, chen2024atypicalmandibulofacialdysostosis pages 5-6)
- **2024 structural variant detection via national genome projects:** A 2024 report demonstrates that WGS in large-scale genomics programs (DDD, 100,000 Genomes) can detect **complex intragenic EFTUD2 rearrangements**, supporting the adoption of SV-aware pipelines when MFDM is suspected. (Sep 2024; https://doi.org/10.1186/s12920-024-01999-0) (lyulchevabennett2024dualdiagnosisof pages 1-2)

## Expert opinion / analysis (from authoritative sources in this evidence set)
- The cohort-defining AJHG study positioned MFDM as the first multiple-malformation syndrome attributed to a defect of the major spliceosome and established the haploinsufficiency mechanism for EFTUD2 in MFDM. (Feb 2012; https://doi.org/10.1016/j.ajhg.2011.12.023) (lines2012haploinsufficiencyofa pages 1-2, lines2012haploinsufficiencyofa pages 4-5)
- Mechanistic mouse work proposes a testable causal link from Mdm2 mis-splicing to p53 overactivation and neural crest apoptosis and demonstrates partial phenotypic rescue by p53 inhibition, but also indicates additional p53-independent contributions to lethality and malformations. (Feb 2021; https://doi.org/10.1093/hmg/ddab051; Aug 2022; https://doi.org/10.3390/ijms23169033) (beauchamp2021mutationineftud2 pages 10-12, beauchamp2022craniofacialdefectsin pages 1-2)

## Key limitations of this report (evidence gaps)
- This run could not retrieve Orphanet/MeSH/ICD codes, ClinVar allele frequencies, or formal clinical practice guidelines.
- Robust long-term survival/life expectancy statistics and standardized QoL measurements were not found in the retrieved MFDM-specific literature.
- No MFDM-specific interventional clinical trials were identified in ClinicalTrials.gov via available tools.


References

1. (lines2012haploinsufficiencyofa pages 1-2): Matthew A. Lines, Lijia Huang, Jeremy Schwartzentruber, Stuart L. Douglas, Danielle C. Lynch, Chandree Beaulieu, Maria Leine Guion-Almeida, Roseli Maria Zechi-Ceide, Blanca Gener, Gabriele Gillessen-Kaesbach, Caroline Nava, Geneviève Baujat, Denise Horn, Usha Kini, Almuth Caliebe, Yasemin Alanay, Gulen Eda Utine, Dorit Lev, Jürgen Kohlhase, Arthur W. Grix, Dietmar R. Lohmann, Ute Hehr, Detlef Böhm, Jacek Majewski, Dennis E. Bulman, Dagmar Wieczorek, and Kym M. Boycott. Haploinsufficiency of a spliceosomal gtpase encoded by eftud2 causes mandibulofacial dysostosis with microcephaly. American journal of human genetics, 90 2:369-77, Feb 2012. URL: https://doi.org/10.1016/j.ajhg.2011.12.023, doi:10.1016/j.ajhg.2011.12.023. This article has 252 citations and is from a highest quality peer-reviewed journal.

2. (lines2012haploinsufficiencyofa pages 4-5): Matthew A. Lines, Lijia Huang, Jeremy Schwartzentruber, Stuart L. Douglas, Danielle C. Lynch, Chandree Beaulieu, Maria Leine Guion-Almeida, Roseli Maria Zechi-Ceide, Blanca Gener, Gabriele Gillessen-Kaesbach, Caroline Nava, Geneviève Baujat, Denise Horn, Usha Kini, Almuth Caliebe, Yasemin Alanay, Gulen Eda Utine, Dorit Lev, Jürgen Kohlhase, Arthur W. Grix, Dietmar R. Lohmann, Ute Hehr, Detlef Böhm, Jacek Majewski, Dennis E. Bulman, Dagmar Wieczorek, and Kym M. Boycott. Haploinsufficiency of a spliceosomal gtpase encoded by eftud2 causes mandibulofacial dysostosis with microcephaly. American journal of human genetics, 90 2:369-77, Feb 2012. URL: https://doi.org/10.1016/j.ajhg.2011.12.023, doi:10.1016/j.ajhg.2011.12.023. This article has 252 citations and is from a highest quality peer-reviewed journal.

3. (beauchamp2022craniofacialdefectsin pages 1-2): Marie-Claude Beauchamp, Alexia Boucher, Yanchen Dong, Rachel Aber, and Loydie A. Jerome-Majewska. Craniofacial defects in embryos with homozygous deletion of eftud2 in their neural crest cells are not rescued by trp53 deletion. International Journal of Molecular Sciences, 23:9033, Aug 2022. URL: https://doi.org/10.3390/ijms23169033, doi:10.3390/ijms23169033. This article has 13 citations.

4. (beauchamp2021mutationineftud2 pages 10-12): Marie-Claude Beauchamp, Anissa Djedid, Eric Bareke, Fjodor Merkuri, Rachel Aber, Annie S Tam, Matthew A Lines, Kym M Boycott, Peter C Stirling, Jennifer L Fish, Jacek Majewski, and Loydie A Jerome-Majewska. Mutation in eftud2 causes craniofacial defects in mice via mis-splicing of mdm2 and increased p53. Human molecular genetics, 30:739-757, Feb 2021. URL: https://doi.org/10.1093/hmg/ddab051, doi:10.1093/hmg/ddab051. This article has 41 citations and is from a domain leading peer-reviewed journal.

5. (chen2024atypicalmandibulofacialdysostosis pages 1-2): Ying Chen, Run Yang, Xin Chen, Naier Lin, Chenlong Li, Yaoyao Fu, Aijuan He, Yimin Wang, Tianyu Zhang, and Jing Ma. Atypical mandibulofacial dysostosis with microcephaly diagnosed through the identification of a novel pathogenic mutation in eftud2. Molecular Genetics & Genomic Medicine, Apr 2024. URL: https://doi.org/10.1002/mgg3.2426, doi:10.1002/mgg3.2426. This article has 6 citations and is from a peer-reviewed journal.

6. (luquetti2013“mandibulofacialdysostosiswith pages 1-3): Daniela V. Luquetti, Anne V. Hing, Mark J. Rieder, Deborah A. Nickerson, Emily H. Turner, Joshua Smith, Sarah Park, and Michael L. Cunningham. “mandibulofacial dysostosis with microcephaly” caused by eftud2 mutations: expanding the phenotype. American Journal of Medical Genetics Part A, 161:108-113, Jan 2013. URL: https://doi.org/10.1002/ajmg.a.35696, doi:10.1002/ajmg.a.35696. This article has 90 citations.

7. (OpenTargets Search: mandibulofacial dysostosis with microcephaly): Open Targets Query (mandibulofacial dysostosis with microcephaly, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (chen2024atypicalmandibulofacialdysostosis pages 5-6): Ying Chen, Run Yang, Xin Chen, Naier Lin, Chenlong Li, Yaoyao Fu, Aijuan He, Yimin Wang, Tianyu Zhang, and Jing Ma. Atypical mandibulofacial dysostosis with microcephaly diagnosed through the identification of a novel pathogenic mutation in eftud2. Molecular Genetics & Genomic Medicine, Apr 2024. URL: https://doi.org/10.1002/mgg3.2426, doi:10.1002/mgg3.2426. This article has 6 citations and is from a peer-reviewed journal.

9. (beauchamp2020missplicingofmdm2 pages 19-23): Marie-Claude Beauchamp, Anissa Djedid, Eric Bareke, Fjodor Merkuri, Rachel Aber, Annie S. Tam, Matthew A. Lines, Kym M. Boycott, Peter C. Stirling, Jennifer L. Fish, Jacek Majewski, and Loydie A. Jerome-Majewska. Mis-splicing of mdm2 leads to increased p53-activity and craniofacial defects in a mfdm eftud2 mutant mouse model. bioRxiv, Sep 2020. URL: https://doi.org/10.1101/2020.09.22.308205, doi:10.1101/2020.09.22.308205. This article has 1 citations.

10. (park2022thecoresplicing pages 13-14): Byung-Yong Park, Melanie Tachi-Duprat, Chibuike Ihewulezi, Arun Devotta, and Jean-Pierre Saint-Jeannet. The core splicing factors eftud2, snrpb and txnl4a are essential for neural crest and craniofacial development. Journal of Developmental Biology, 10:29, Jul 2022. URL: https://doi.org/10.3390/jdb10030029, doi:10.3390/jdb10030029. This article has 26 citations.

11. (kohailan2022adenovo pages 2-4): Muhammad Kohailan, Omayma Al-Saei, Sujitha Padmajeya, Waleed Aamer, Najwa Elbashir, Ammira Al-Shabeeb Akil, Abdul-Rauf Kamboh, and Khalid Fakhro. A de novo start-loss in eftud2 associated with mandibulofacial dysostosis with microcephaly: case report. Cold Spring Harbor Molecular Case Studies, 8:a006206, Jun 2022. URL: https://doi.org/10.1101/mcs.a006206, doi:10.1101/mcs.a006206. This article has 7 citations and is from a peer-reviewed journal.

12. (gandomi2015array‐cghisan pages 1-2): S.K. Gandomi, M. Parra, D. Reeves, V. Yap, and C.‐L. Gau. Array‐cgh is an effective first‐tier diagnostic test for eftud2‐associated congenital mandibulofacial dysostosis with microcephaly. Clinical Genetics, 87:80-84, Jan 2015. URL: https://doi.org/10.1111/cge.12328, doi:10.1111/cge.12328. This article has 27 citations and is from a peer-reviewed journal.

13. (jacob2020adenovo pages 1-2): Arthur Jacob, Jennifer Pasquier, Raphael Carapito, Frédéric Auradé, Anne Molitor, Philippe Froguel, Khalid Fakhro, Najeeb Halabi, Géraldine Viot, Seiamak Bahram, and Arash Rafii. A de novo synonymous variant in eftud2 disrupts normal splicing and causes mandibulofacial dysostosis with microcephaly: case report. BMC Medical Genetics, Sep 2020. URL: https://doi.org/10.1186/s12881-020-01121-y, doi:10.1186/s12881-020-01121-y. This article has 16 citations and is from a peer-reviewed journal.

14. (lines2012haploinsufficiencyofa pages 3-4): Matthew A. Lines, Lijia Huang, Jeremy Schwartzentruber, Stuart L. Douglas, Danielle C. Lynch, Chandree Beaulieu, Maria Leine Guion-Almeida, Roseli Maria Zechi-Ceide, Blanca Gener, Gabriele Gillessen-Kaesbach, Caroline Nava, Geneviève Baujat, Denise Horn, Usha Kini, Almuth Caliebe, Yasemin Alanay, Gulen Eda Utine, Dorit Lev, Jürgen Kohlhase, Arthur W. Grix, Dietmar R. Lohmann, Ute Hehr, Detlef Böhm, Jacek Majewski, Dennis E. Bulman, Dagmar Wieczorek, and Kym M. Boycott. Haploinsufficiency of a spliceosomal gtpase encoded by eftud2 causes mandibulofacial dysostosis with microcephaly. American journal of human genetics, 90 2:369-77, Feb 2012. URL: https://doi.org/10.1016/j.ajhg.2011.12.023, doi:10.1016/j.ajhg.2011.12.023. This article has 252 citations and is from a highest quality peer-reviewed journal.

15. (beauchamp2021mutationineftud2 pages 1-2): Marie-Claude Beauchamp, Anissa Djedid, Eric Bareke, Fjodor Merkuri, Rachel Aber, Annie S Tam, Matthew A Lines, Kym M Boycott, Peter C Stirling, Jennifer L Fish, Jacek Majewski, and Loydie A Jerome-Majewska. Mutation in eftud2 causes craniofacial defects in mice via mis-splicing of mdm2 and increased p53. Human molecular genetics, 30:739-757, Feb 2021. URL: https://doi.org/10.1093/hmg/ddab051, doi:10.1093/hmg/ddab051. This article has 41 citations and is from a domain leading peer-reviewed journal.

16. (beauchamp2020missplicingofmdm2 pages 15-19): Marie-Claude Beauchamp, Anissa Djedid, Eric Bareke, Fjodor Merkuri, Rachel Aber, Annie S. Tam, Matthew A. Lines, Kym M. Boycott, Peter C. Stirling, Jennifer L. Fish, Jacek Majewski, and Loydie A. Jerome-Majewska. Mis-splicing of mdm2 leads to increased p53-activity and craniofacial defects in a mfdm eftud2 mutant mouse model. bioRxiv, Sep 2020. URL: https://doi.org/10.1101/2020.09.22.308205, doi:10.1101/2020.09.22.308205. This article has 1 citations.

17. (beauchamp2022craniofacialdefectsin pages 10-12): Marie-Claude Beauchamp, Alexia Boucher, Yanchen Dong, Rachel Aber, and Loydie A. Jerome-Majewska. Craniofacial defects in embryos with homozygous deletion of eftud2 in their neural crest cells are not rescued by trp53 deletion. International Journal of Molecular Sciences, 23:9033, Aug 2022. URL: https://doi.org/10.3390/ijms23169033, doi:10.3390/ijms23169033. This article has 13 citations.

18. (lyulchevabennett2024dualdiagnosisof pages 1-2): Ekaterina Lyulcheva-Bennett, Christopher Kershaw, Eleanor Baker, Stuart Gillies, Emma McCarthy, Jenny Higgs, Natalie Canham, Dawn Hennigan, Chris Parks, and Daimark Bennett. Dual diagnosis of achondroplasia and mandibulofacial dysostosis with microcephaly. BMC Medical Genomics, Sep 2024. URL: https://doi.org/10.1186/s12920-024-01999-0, doi:10.1186/s12920-024-01999-0. This article has 4 citations and is from a peer-reviewed journal.

19. (luquetti2013“mandibulofacialdysostosiswith pages 3-4): Daniela V. Luquetti, Anne V. Hing, Mark J. Rieder, Deborah A. Nickerson, Emily H. Turner, Joshua Smith, Sarah Park, and Michael L. Cunningham. “mandibulofacial dysostosis with microcephaly” caused by eftud2 mutations: expanding the phenotype. American Journal of Medical Genetics Part A, 161:108-113, Jan 2013. URL: https://doi.org/10.1002/ajmg.a.35696, doi:10.1002/ajmg.a.35696. This article has 90 citations.

20. (beauchamp2020missplicingofmdm2 pages 1-5): Marie-Claude Beauchamp, Anissa Djedid, Eric Bareke, Fjodor Merkuri, Rachel Aber, Annie S. Tam, Matthew A. Lines, Kym M. Boycott, Peter C. Stirling, Jennifer L. Fish, Jacek Majewski, and Loydie A. Jerome-Majewska. Mis-splicing of mdm2 leads to increased p53-activity and craniofacial defects in a mfdm eftud2 mutant mouse model. bioRxiv, Sep 2020. URL: https://doi.org/10.1101/2020.09.22.308205, doi:10.1101/2020.09.22.308205. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](Mandibulofacial_Dysostosis_with_Microcephaly-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Mandibulofacial_Dysostosis_with_Microcephaly-deep-research-falcon_artifacts/artifact-01.md)