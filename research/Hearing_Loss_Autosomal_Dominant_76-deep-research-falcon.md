---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-01T10:06:06.321772'
end_time: '2026-09-01T10:14:54.947714'
duration_seconds: 528.63
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hearing Loss Autosomal Dominant 76 (DFNA76, PLS1-related)
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 16
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 7
  verified: 7
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hearing_Loss_Autosomal_Dominant_76-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hearing Loss Autosomal Dominant 76 (DFNA76, PLS1-related)
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Dominant 76 (DFNA76, PLS1-related)** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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
- **Disease Name:** Hearing Loss Autosomal Dominant 76 (DFNA76, PLS1-related)
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Dominant 76 (DFNA76, PLS1-related)** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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


# Hearing Loss, Autosomal Dominant 76 (DFNA76; PLS1-related)

## Executive summary

DFNA76 is an ultra-rare Mendelian form of autosomal-dominant, usually nonsyndromic hearing loss caused by heterozygous variants in **PLS1**, which encodes plastin-1/fimbrin, an actin-filament crosslinker enriched in inner-ear hair-cell stereocilia. Reported disease ranges from congenital, apparently stable hearing impairment in one Hungarian Roma family to childhood- or adult-recognized, progressive, predominantly medium/high-frequency sensorineural hearing loss in other families. The evidence base remains small: principally several families reported in 2019 and one Chinese splice-variant family subsequently investigated with cell and zebrafish models. There are no reliable prevalence estimates, formal penetrance studies, disease-specific clinical criteria, targeted therapies, or PLS1-specific clinical trials.

The following table provides a knowledge-base-oriented synopsis.

| Field | Evidence-based summary | Suggested ontology/identifier |
|---|---|---|
| Disease definition | DFNA76 is a very rare form of **autosomal dominant nonsyndromic hearing loss** caused by heterozygous **PLS1** variants. Human reports identify PLS1 as a deafness gene in multiple unrelated families; phenotype is isolated hearing loss without consistent syndromic findings (morgan2019mutationsinpls1 pages 1-2, diaz‐horta2019novelvariantp.e269k pages 1-5, schrauwen2019hearingimpairmentlocus pages 2-3). | Disease label: Hearing loss, autosomal dominant 76 / DFNA76; MONDO: **not confidently verified**; MeSH/ICD exact disease-specific ID: **not confidently verified** |
| Inheritance | Inheritance is **autosomal dominant** with familial segregation across reported kindreds from Hungarian Roma, Italian, US, French, Turkish, and Chinese families (morgan2019mutationsinpls1 pages 1-2, diaz‐horta2019novelvariantp.e269k pages 1-5, schrauwen2019hearingimpairmentlocus pages 2-3). Formal penetrance estimates have not been established. | HP:0000006 Autosomal dominant inheritance |
| Gene/protein | Causal gene: **PLS1** (plastin 1, fimbrin), encoding an actin-bundling protein highly expressed in inner-ear stereocilia and also detected in the cuticular plate of hair cells in mouse studies (morgan2019mutationsinpls1 pages 1-2, taylor2015absenceofplastin pages 2-3, xu2022anovelpls1 pages 10-13). Protein architecture includes N-terminal EF-hand calcium-binding motifs and two actin-binding domains, ABD1 and ABD2 (xu2026pathogenicmechanismof pages 1-4, xu2022anovelpls1 pages 10-13). | HGNC: **PLS1**; NCBI Gene/Ensembl/UniProt exact IDs: **not confidently verified here**; GO suggestions: actin filament binding, actin bundling |
| Established/reported variants | Reported DFNA76-associated variants include **p.Leu363Phe** in Hungarian Roma family 6012, **p.Phe128Ser**, **p.Leu238Arg**, and recurrent **p.Glu269Lys** in European/Turkish families, plus **c.981+1G>A** splice variant in a Chinese family (morgan2019mutationsinpls1 pages 1-2, diaz‐horta2019novelvariantp.e269k pages 1-5, schrauwen2019hearingimpairmentlocus pages 2-3, xu2022anovelpls1 pages 10-13). Available summaries indicate these are rare/absent in population databases used in the original studies, but precise allele counts/frequencies are not fully available in current context. | Sequence Ontology suggestions: missense_variant; splice_donor_variant |
| Core phenotype | Core phenotype is **bilateral or sometimes asymmetric/unilateral nonsyndromic hearing loss**, usually sensorineural, often affecting **medium-to-high or high frequencies**; severity ranges from mild to profound across families. Mixed hearing loss was reported in some Hungarian Roma individuals (morgan2019mutationsinpls1 pages 1-2, diaz‐horta2019novelvariantp.e269k pages 1-5, schrauwen2019hearingimpairmentlocus pages 7-9). | HP:0000365 Hearing impairment; HP:0000407 Sensorineural hearing impairment; HP:0011003 Abnormality of hearing physiology |
| Onset/course | Onset appears **variable across families**: congenital/non-progressive in the Hungarian Roma cohort context, versus childhood/post-lingual to adult detection with **progressive** decline in several other families. One Italian patient was diagnosed at age 8, while an affected mother recognized loss around age 30 (morgan2019mutationsinpls1 pages 1-2, diaz‐horta2019novelvariantp.e269k pages 1-5, schrauwen2019hearingimpairmentlocus pages 2-3). | HPO suggestions: HP:0003577 Congenital onset; HP:0003596 Middle age onset; HP:0003676 Progressive hearing impairment |
| Anatomy/cell/subcellular site | Primary site is the **inner ear**, especially the **organ of Corti** and **cochlear hair-cell stereocilia**; vestibular hair-cell expression is also reported in model/mechanistic literature. Subcellular localization includes **stereocilia F-actin cores** and **cuticular plate** (taylor2015absenceofplastin pages 2-3, xu2026pathogenicmechanismof pages 1-4). | UBERON: inner ear / cochlea / organ of Corti / stereocilium (**exact IDs not confidently verified**); CL: auditory hair cell (**exact ID not confidently verified**); GO CC: stereocilium, actin cytoskeleton |
| Mechanism | Best-supported mechanism is disruption of **actin bundling/crosslinking in stereocilia**, impairing stereocilia architecture and long-term maintenance. Human missense variants are modeled to destabilize **ABD1** and weaken F-actin interaction; splice variant **c.981+1G>A** causes exon 8 skipping or partial deletion in ABD1. **PI3K-AKT upregulation is provisional**, supported by the **2022 preprint / later 2023 publication stream** and cell/zebrafish work, but not yet established as the definitive human disease mechanism (morgan2019mutationsinpls1 pages 1-2, xu2022anovelpls1 pages 10-13, xu2026pathogenicmechanismof pages 1-4, xu2022anovelpls1 pages 13-19). | GO suggestions: actin filament bundle assembly, stereocilium organization, sensory perception of sound |
| Models | **Pls1 knockout mice** develop moderate progressive hearing loss with shortened/thinner inner-hair-cell stereocilia and later degeneration, supporting a maintenance role for plastin 1. **Zebrafish** expressing/perturbed for the splice-variant context show abnormal otolith/cochlear morphometry and reduced swimming behavior (taylor2015absenceofplastin pages 2-3, taylor2015absenceofplastin pages 1-1, xu2022anovelpls1 pages 10-13). | Model systems: mouse knockout; zebrafish transient model |
| Diagnosis | Diagnosis currently relies on **audiologic phenotyping plus molecular testing**. Reported methods include next-generation sequencing or whole-exome sequencing with segregation testing, Sanger confirmation, and for splice variants, **minigene assays** to demonstrate aberrant splicing (morgan2019mutationsinpls1 pages 1-2, xu2022anovelpls1 pages 1-4, xu2022anovelpls1 pages 13-19). | NCIT suggestions: Genetic Testing; Audiometry; Sanger Sequencing; Whole Exome Sequencing |
| Treatment | No **PLS1-specific molecular therapy** or genotype-directed clinical trial was identified. Current care is standard hereditary hearing-loss management: longitudinal audiologic follow-up, **hearing aids**, and **cochlear implantation** when indicated by severity/function, extrapolating from broader DFNA practice (morgan2019mutationsinpls1 pages 1-2, diaz‐horta2019novelvariantp.e269k pages 1-5). | NCIT suggestions: Hearing Aid Device; Cochlear Implantation; Genetic Counseling |
| Epidemiology | DFNA76 is **ultra-rare**; evidence is limited to a small number of reported families from several ancestries. No robust prevalence, incidence, sex ratio, or carrier-frequency estimates are available (morgan2019mutationsinpls1 pages 1-2, diaz‐horta2019novelvariantp.e269k pages 1-5, schrauwen2019hearingimpairmentlocus pages 2-3). | Orphanet/MONDO prevalence term: **not confidently verified** |
| Key evidence gaps | Major gaps include lack of validated disease-specific identifiers in readily available context, no firm penetrance estimates, sparse natural-history data, minimal variant-level population frequency detail, no disease-specific QoL/outcome studies, no established modifier genes, no confirmed epigenetic mechanism, and no approved targeted therapy. The **PI3K-AKT** link remains **hypothesis-generating/provisional** rather than clinically established (xu2022anovelpls1 pages 10-13, xu2022anovelpls1 pages 13-19). | Knowledge-gap annotation; MONDO/HPO/UBERON exact IDs to be added after manual verification |


*Table: This table summarizes the current evidence base for PLS1-related autosomal dominant nonsyndromic hearing loss (DFNA76), including clinical features, variants, mechanism, models, and gaps. It is designed as a compact artifact for knowledge-base population while clearly flagging uncertain identifiers and provisional mechanistic claims.*

## 1. Disease information

**Definition.** DFNA76 is isolated hereditary hearing impairment attributable to a heterozygous pathogenic or likely pathogenic **PLS1** variant. The principal clinical lesion is cochlear hearing dysfunction; consistent retinal, neurologic, skeletal, renal, or vestibular disease has not been demonstrated. The foundational human studies reported Hungarian Roma, Italian, US, French, and Turkish families, followed by a Chinese family with a splice-site variant. (morgan2019mutationsinpls1 pages 1-2, diaz‐horta2019novelvariantp.e269k pages 1-5, schrauwen2019hearingimpairmentlocus pages 2-3)

**Names and identifiers.** Appropriate names include *hearing loss, autosomal dominant 76*; *DFNA76*; *PLS1-related autosomal-dominant nonsyndromic hearing loss*; and *plastin-1/fimbrin-related hearing loss*. The exact disease-specific MONDO, Orphanet, MeSH, ICD-10, and ICD-11 identifiers were not securely recoverable from the retrieved primary literature and should not be inferred. ICD coding in practice would use a general sensorineural-hearing-loss category rather than a DFNA76-specific code. OMIM and ClinVar identifiers should likewise be verified directly against their current records before database ingestion.

**Evidence granularity.** Clinical descriptions derive from individual pedigrees and patients, subsequently aggregated in locus/gene-level resources. They are not EHR-derived population estimates. Thus, statements about “typical” DFNA76 remain provisional and vulnerable to ascertainment bias.

## 2. Etiology, risk, protective factors, and gene–environment interaction

The primary cause is a **germline heterozygous PLS1 sequence variant** that segregates in an autosomal-dominant pattern. Evidence supports missense variants affecting actin-binding regions and a splice-donor variant disrupting exon 8. (morgan2019mutationsinpls1 pages 1-2, diaz‐horta2019novelvariantp.e269k pages 1-5, xu2022anovelpls1 pages 1-4)

A positive family history is the principal clinical risk indicator. Each child of a heterozygous affected individual has a theoretical 50% probability of inheriting the familial variant, although variant-specific penetrance is unknown. No modifier gene, protective allele, sex effect, anticipation, or germline-mosaicism rate has been established. No DFNA76-specific environmental cause or protective diet/lifestyle intervention is known.

Noise exposure, ototoxic medication, infection, and aging can independently damage hearing, but a quantitative **PLS1 × environment** interaction has not been demonstrated. Avoiding excessive noise and unnecessary ototoxic exposure is therefore prudent general hearing conservation—not proven primary prevention of genetically initiated DFNA76.

## 3. Phenotypes

The core phenotype is hearing impairment, most often **sensorineural**, bilateral, symmetric, and more marked at medium-to-high frequencies. Severity across reported individuals ranges from mild to profound. In an Italian family, a 12-year-old had bilateral symmetric, down-sloping medium/high-frequency loss detected at age 8, while her 48-year-old mother had moderate-to-severe high-frequency loss recognized around age 30. Normal bone-conduction assessment, type-A tympanograms, and normal reflexes excluded conductive disease in that family. (morgan2019mutationsinpls1 pages 1-2)

A Turkish family contained five affected people across three generations; four examined individuals had symmetric, moderate, post-lingually diagnosed, progressive sensorineural loss. Otoacoustic emissions were absent while acoustic reflexes were present. No vertigo, dizziness, nystagmus, balance difficulty, or motor-developmental delay was reported. (diaz‐horta2019novelvariantp.e269k pages 1-5)

The Hungarian Roma PLS1 family had mild-to-profound, high-frequency-biased impairment. Two individuals had mixed hearing loss and one had sensorineural loss; concurrent otitis media with effusion in one person may explain at least part of the conductive component. The wider Roma cohort was described as congenital and non-progressive, with diagnoses between ages 2 and 7, illustrating possible interfamily heterogeneity. (schrauwen2019hearingimpairmentlocus pages 2-3, schrauwen2019hearingimpairmentlocus pages 7-9)

No consistent behavioral or laboratory abnormality belongs to DFNA76. Disease-specific tinnitus frequency, speech-recognition trajectories, vestibular-test results, and quality-of-life scores have not been published. Expected functional consequences of significant hearing loss include impaired speech perception—particularly in noise—communication, education, employment, and social participation, but these have not been quantified specifically for PLS1 disease.

**Suggested HPO terms:** hearing impairment (**HP:0000365**); sensorineural hearing impairment (**HP:0000407**); bilateral hearing impairment; high-frequency hearing impairment; progressive hearing impairment; congenital onset where applicable; and mixed hearing impairment only for appropriately phenotyped individuals. Frequencies should be recorded as “unknown,” not universal.

## 4. Genetic and molecular information

**Gene/protein.** The causal gene is **PLS1**; the encoded plastin-1 protein has N-terminal EF-hand calcium-binding motifs and two tandem actin-binding domains, ABD1 and ABD2, each constructed from calponin-homology domains. Reported boundaries in the experimental literature are approximately ABD1 residues 120–379 and ABD2 residues 394–623. (xu2026pathogenicmechanismof pages 1-4, xu2022anovelpls1 pages 10-13)

**Reported variants:**

- **c.383T>C, p.(Phe128Ser)** — missense, reported in a European-ancestry family.
- **c.713G>T, p.(Leu238Arg)** — missense, reported in a European-ancestry family.
- **c.805G>A, p.(Glu269Lys)** — missense, independently reported in European and Turkish families; modeling predicts destabilized ABD1 and impaired stable PLS1–ACTB interaction.
- **p.(Leu363Phe)** — missense in a Hungarian Roma family; affects the CH2 region involved in actin binding.
- **c.981+1G>A** — canonical splice-donor variant in a Chinese family; minigene experiments demonstrated exon-8 skipping or a 47-bp deletion, affecting residues approximately 297–327 in ABD1. (morgan2019mutationsinpls1 pages 1-2, diaz‐horta2019novelvariantp.e269k pages 1-5, schrauwen2019hearingimpairmentlocus pages 2-3, xu2022anovelpls1 pages 10-13)

Original investigators filtered rare variants against databases including gnomAD, ESP6500, and the Greater Middle East variome; the Hungarian study used a minor-allele-frequency threshold below 0.02. PLS1 showed reported gnomAD observed/expected values of 0.42 for predicted loss-of-function and 0.76 for missense variation. Exact current allele counts and ClinVar classifications must be rechecked against the current transcript/version before clinical reporting. (schrauwen2019hearingimpairmentlocus pages 2-3, schrauwen2019hearingimpairmentlocus pages 7-9)

All reported disease variants are constitutional/germline. No somatic etiology, recurrent chromosomal rearrangement, copy-number syndrome, epigenetic signature, modifier gene, or disease-specific methylation abnormality is established. The molecular behavior may combine partial loss of function and dominant-negative interference, but this remains less firmly demonstrated for the missense alleles than segregation and phenotype association.

## 5. Environmental and infectious information

No toxin, pollutant, radiation exposure, occupational agent, smoking pattern, alcohol use, diet, or infectious organism is known to cause PLS1-related DFNA76. These factors can produce independent or additive acquired hearing loss and should be documented clinically. DFNA76 is not infectious or transmissible.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous **PLS1 missense or splice-disrupting variant leads to** structurally altered or quantitatively/functionally deficient plastin-1 in inner-ear hair cells. (morgan2019mutationsinpls1 pages 1-2, xu2022anovelpls1 pages 10-13)
2. Altered plastin-1 **leads to** impaired regulation and crosslinking of stereociliary F-actin; for missense alleles this is supported chiefly by structural modeling, while exon-8 disruption has experimental splicing and model-system support. (morgan2019mutationsinpls1 pages 1-2, xu2026pathogenicmechanismof pages 1-4)
3. Abnormal F-actin organization **results in** defective stereocilia width, length, packing, and long-term maintenance; this step is demonstrated in Pls1-null mice. (taylor2015absenceofplastin pages 2-3, taylor2015absenceofplastin pages 1-1)
4. Progressive stereociliary architectural failure **leads to** altered hair-bundle/mechanoelectrical-transduction performance; most baseline electrophysiologic properties remain initially preserved in knockout mice, but adaptation is abnormal. (taylor2015absenceofplastin pages 1-1)
5. Reduced fidelity of cochlear mechanotransduction **results in** elevated auditory thresholds and predominantly sensorineural hearing loss.
6. **Provisional branch:** PLS1 depletion **leads to** altered expression of PI3K–AKT-associated genes, which may modify hair-cell survival or cytoskeletal homeostasis; causality in human DFNA76 is not established. (xu2022anovelpls1 pages 10-13, xu2022anovelpls1 pages 13-19)

Plastin-1 localizes to stereocilia and the cuticular plate of mouse inner and outer hair cells. It is present in immature stereocilia and retained in mature bundles, supporting a continuing maintenance function. PLS1 is not indispensable for initial bundle formation: knockout hair cells develop, but adult stereocilia become shorter and thinner. The longest-row width is reduced by about 10–20%; minimum inner-hair-cell stereocilium width was approximately 0.15 μm in knockout versus 0.32 μm in wild type. Outer-hair-cell bundles are initially less affected but develop age-related degeneration. Hearing loss is moderate, progressive, and present across tested frequencies without being explained by early hair-cell death. (taylor2015absenceofplastin pages 2-3, taylor2015absenceofplastin pages 1-1)

The Chinese splice-variant experiments reported 478 upregulated and 309 downregulated genes after PLS1 knockdown. Upregulated genes were enriched in PI3K–AKT signaling; qPCR confirmed increased **COL6A3, SPP1, ITGB3**, and **HGF** expression. These results came from a cell model/HEI-OC1 context and zebrafish work rather than patient cochlear tissue; accordingly, PI3K–AKT should be annotated as hypothesis-generating. (xu2022anovelpls1 pages 10-13, xu2022anovelpls1 pages 13-19)

No validated disease-specific metabolomic, lipidomic, proteomic, epigenomic, single-cell, spatial-transcriptomic, organoid, or CRISPR-screen signature is available.

**Suggested GO terms:** actin filament binding; actin filament bundle assembly; actin cytoskeleton organization; stereocilium organization; maintenance of stereocilium; sensory perception of sound; mechanosensory behavior. **Suggested cell types:** inner hair cell, outer hair cell, auditory hair cell, and vestibular hair cell. Exact GO/CL accession numbers should be ontology-verified before loading.

## 7. Anatomical structures affected

The primary organ is the **inner ear**, particularly the cochlea and organ of Corti. The key tissue is mechanosensory epithelium, and the principal cells are inner and outer hair cells. The crucial subcellular structures are the apical stereocilia/F-actin core and cuticular plate. Plastin-1 is also expressed in vestibular hair-cell stereocilia, but a consistent human vestibular syndrome has not been observed. (diaz‐horta2019novelvariantp.e269k pages 1-5, taylor2015absenceofplastin pages 2-3, xu2026pathogenicmechanismof pages 1-4)

Hearing loss is generally bilateral and symmetric, although unilateral/asymmetric presentation has been reported in the later Chinese-family account. No reproducible secondary-organ involvement is known. Suggested anatomy concepts are UBERON inner ear, cochlea, organ of Corti, cochlear duct, and stereocilium; identifiers require formal ontology lookup.

## 8. Temporal development

Onset is heterogeneous: congenital or early-childhood disease was reported in the Hungarian Roma cohort, childhood detection occurred in the Italian proband, and adult recognition occurred in her mother. Turkish cases were post-lingual with uncertain exact onset. (morgan2019mutationsinpls1 pages 1-2, diaz‐horta2019novelvariantp.e269k pages 1-5, schrauwen2019hearingimpairmentlocus pages 2-3)

The prevalent pattern outside the original Roma family is insidious, chronic, and progressive. The mouse phenotype similarly emerges after essentially normal hair-bundle development and worsens with age, biologically supporting surveillance throughout life. There are no validated clinical stages, progression-rate equations, remission patterns, or disease-specific critical intervention windows. Spontaneous recovery is not expected for established genetic sensorineural loss.

## 9. Inheritance and population

Inheritance is **autosomal dominant**. Multigenerational segregation has been observed, including five affected members across three generations in the Turkish family. Formal penetrance and age-dependent penetrance estimates are unavailable; apparent segregation suggests substantial penetrance in ascertained families, but unaffected young carriers cannot be excluded without longitudinal data. (diaz‐horta2019novelvariantp.e269k pages 1-5)

DFNA76 is ultra-rare, known from a small number of families of Hungarian Roma, Italian, US, French, Turkish, Chinese, and other European ancestries. No prevalence per 100,000, annual incidence, carrier frequency, sex ratio, or reliable geographic gradient has been established. The Roma p.(Leu363Phe) allele could reflect a private or population-enriched familial allele, but a founder effect has not been proven. Consanguinity is not etiologically required for this dominant disorder, and anticipation has not been reported.

## 10. Diagnostics

Diagnosis requires: (1) history, including onset, progression, noise/ototoxic exposure, and three-generation pedigree; (2) otoscopy and tympanometry to exclude conductive disease; (3) age-appropriate pure-tone or behavioral audiometry with air and bone thresholds; (4) speech testing; (5) otoacoustic emissions and, where needed, auditory brainstem responses; and (6) molecular confirmation.

A comprehensive hereditary-hearing-loss NGS panel containing **PLS1** is generally preferable to initial single-gene testing because nonsyndromic hearing loss is highly heterogeneous. Exome sequencing is useful when a panel is negative or when the phenotype is atypical; genome sequencing can interrogate structural, deep-intronic, and regulatory variants missed by exome/panel testing. The original reports used NGS/WES, Sanger confirmation, and segregation analysis; the splice-site study added a minigene assay. (morgan2019mutationsinpls1 pages 1-2, xu2022anovelpls1 pages 1-4, xu2022anovelpls1 pages 13-19)

CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion analysis are not first-line tests for a phenotype strongly suggestive of DFNA76 unless additional findings indicate an alternative diagnosis. RNA analysis can clarify splice variants but is not an established routine biomarker. There is no blood chemistry, imaging, biopsy, proteomic, or metabolomic diagnostic marker.

Differential diagnosis includes other dominant nonsyndromic hearing-loss genes—particularly **KCNQ4, TECTA, ACTG1, WFS1, POU4F3, MYO6**, and **EYA4**—plus GJB2-related disease, otosclerosis, congenital infection, noise injury, ototoxicity, and syndromic disorders such as Usher syndrome. Lack of retinal or vestibular findings supports a nonsyndromic diagnosis but does not substitute for longitudinal assessment.

Cascade testing should be offered after a familial pathogenic variant is established. Newborn hearing screening may identify congenital cases but can miss mild or later-onset disease.

## 11. Outcome and prognosis

DFNA76 is not known to shorten life expectancy or cause disease-specific mortality. Morbidity is auditory and depends on onset, severity, progression, speech discrimination, access to amplification, and educational/communication support. Some patients progress from mild/moderate to severe loss; profound loss has occurred in the reported spectrum. (morgan2019mutationsinpls1 pages 1-2, schrauwen2019hearingimpairmentlocus pages 7-9)

No DFNA76-specific survival, disability-weight, EQ-5D, SF-36, PROMIS, treatment-response, or cochlear-implant outcome dataset exists. Residual hearing does not spontaneously regenerate. Serial audiometry is the most practical prognostic measure; genotype-specific prognostic biomarkers are unavailable.

## 12. Treatment and current implementation

There is no approved PLS1-directed drug, ASO, RNA therapy, gene replacement, gene editing, or cell therapy. No PLS1/DFNA76-specific interventional clinical trial was identified. Current real-world management is phenotype-directed:

1. periodic audiologic surveillance;
2. appropriately fitted bilateral hearing aids for aidable loss;
3. remote-microphone, classroom, workplace, captioning, and communication accommodations;
4. speech/language and auditory rehabilitation when needed;
5. cochlear-implant evaluation for severe-to-profound loss with inadequate aided speech understanding;
6. treatment of coincident conductive disease, such as otitis media; and
7. genetic counseling and cascade testing.

General 2023 research emphasizes that inner-ear gene replacement, augmentation, and editing are advancing rapidly, but delivery, cell targeting, therapeutic timing, dominant-negative allele suppression, durability, and safety remain major translational barriers. For DFNA76 specifically, a dominant-negative mechanism could require allele-specific silencing or editing rather than simple gene addition; this is expert mechanistic inference, not an existing therapy.

Suggested NCIT concepts include Genetic Testing, Audiometry, Hearing Aid Device, Cochlear Implantation, Speech Therapy, Auditory Rehabilitation, and Genetic Counseling. Pharmacogenomic guidance and combination pharmacotherapy are not applicable.

## 13. Prevention

The inherited variant cannot presently be prevented by vaccination, medication, diet, or lifestyle. **Primary prevention** consists of reproductive options after counseling—prenatal diagnosis or PGT-M where legally and ethically appropriate—and general protection from excessive noise and avoidable ototoxicity. **Secondary prevention** comprises newborn/childhood screening, molecular cascade testing, and regular audiometry to detect progression early. **Tertiary prevention** comprises prompt amplification, rehabilitation, communication access, and implantation when indicated. There is no immunization or antimicrobial prophylaxis specific to DFNA76.

## 14. Other species and natural disease

No naturally occurring veterinary PLS1-associated hearing-loss syndrome was identified. The mechanism is evolutionarily conserved because stereociliary actin architecture and plastin-family crosslinking are conserved across vertebrates. DFNA76 has no zoonotic potential and no cross-species transmission.

## 15. Model organisms

**Mouse, genetic knockout.** Pls1-null mice reproduce moderate, progressive, pan-frequency hearing loss and adult stereocilia thinning/shortening. Hair-cell differentiation and initial bundle formation are relatively preserved, making this a strong model of downstream stereocilia-maintenance failure. Limitations are that complete knockout may not model heterozygous missense dominant-negative alleles and the human phenotype is more variable in frequency pattern and onset. (taylor2015absenceofplastin pages 2-3, taylor2015absenceofplastin pages 1-1)

A concise primary-study conclusion was: **“plastin 1 is dispensable for the initial formation of stereocilia”** but is required for preservation of adult stereocilia and optimal hearing. This directly supports maintenance failure rather than a universal congenital morphogenesis defect. (taylor2015absenceofplastin pages 1-1)

**Zebrafish, induced/transient variant model.** The c.981+1G>A/exon-8-disruption work reported reduced mean otolith distance, anterior and posterior otolith diameters, and cochlear diameter, together with reduced swimming speed and distance; reported morphometric differences were significant at *P*<0.05. This supports inner-ear and behavioral consequences but does not directly quantify mammalian hearing and may conflate auditory and vestibular behavior. (xu2022anovelpls1 pages 10-13, xu2022anovelpls1 pages 1-4)

**Cell model.** PLS1 knockdown in an auditory-cell-line context enabled RNA-seq and PI3K–AKT-pathway analysis. This is useful for pathway generation but cannot establish that the same expression changes occur in human cochlear hair cells in vivo. (xu2022anovelpls1 pages 10-13, xu2022anovelpls1 pages 13-19)

## Recent developments and evidence appraisal

The most important disease-specific development near the requested 2023–2024 window was publication of the Chinese **c.981+1G>A** splice-variant work, initially posted in March 2022 and subsequently associated with a 2023 *Clinical Genetics* publication stream. It expanded PLS1 disease beyond missense alleles and supplied experimental splicing, zebrafish, and transcriptomic evidence. The authors’ abstract-level conclusion was that the variant causes hearing loss by inducing exon-8 skipping/deletion and that PI3K–AKT upregulation “plays an important role”; the latter should remain provisional because it is not corroborated in patient cochlear tissue. (xu2022anovelpls1 pages 10-13, xu2022anovelpls1 pages 1-4)

A central 2019 abstract stated: **“We used next-generation sequencing to identify causal variants in PLS1 … in three unrelated families of European ancestry with autosomal dominant NSHL.”** It further reported that modeling suggested destabilization of ABD1 and reduced F-actin binding. (morgan2019mutationsinpls1 pages 1-2)

Another 2019 study summarized the likely variant-specific mechanism as hearing loss arising from **“loss of a stable PLS1-ACTB interaction.”** This is an authoritative structural interpretation, but direct patient-cell biochemical validation remains lacking. (diaz‐horta2019novelvariantp.e269k pages 1-5)

Overall evidence certainty is **moderate for the gene–disease relationship**, supported by multiple segregating families and a concordant mouse phenotype; **moderate for stereociliary actin-maintenance dysfunction**; and **low-to-preliminary for PI3K–AKT as a necessary human disease pathway**. The highest priorities are additional unrelated families, standardized longitudinal audiometry, current ClinVar/gnomAD curation, allele-specific functional assays, heterozygous knock-in models, patient-derived inner-ear organoids, and preclinical testing matched to the dominant molecular mechanism.

## Key source links and publication dates

- Schrauwen et al., *European Journal of Human Genetics*, published March 2019: https://doi.org/10.1038/s41431-019-0372-y. (schrauwen2019hearingimpairmentlocus pages 2-3)
- Morgan et al., *Human Mutation*, published October 2019: https://doi.org/10.1002/humu.23891. (morgan2019mutationsinpls1 pages 1-2)
- Diaz-Horta et al., *Clinical Genetics*, published December 2019: https://doi.org/10.1111/cge.13626. (diaz‐horta2019novelvariantp.e269k pages 1-5)
- Taylor et al., *Human Molecular Genetics*, 2015: https://doi.org/10.1093/hmg/ddu417. (taylor2015absenceofplastin pages 2-3)
- Xu et al., preprint posted March 2022: https://doi.org/10.1101/2022.03.17.484618. (xu2022anovelpls1 pages 10-13)

PMIDs were not present in the retrieved evidence records and therefore are not supplied rather than guessed.

References

1. (morgan2019mutationsinpls1 pages 1-2): Anna Morgan, Daniel C. Koboldt, Elizabeth S. Barrie, Erin R. Crist, Gema García García, Massimo Mezzavilla, Flavio Faletra, Theresa Mihalic Mosher, Richard K. Wilson, Catherine Blanchet, Kandamurugu Manickam, Anne‐Francoise Roux, Paolo Gasparini, Daniele Dell’Orco, and Giorgia Girotto. Mutations in pls1, encoding fimbrin, cause autosomal dominant nonsyndromic hearing loss. Human Mutation, 40:2286-2295, Oct 2019. URL: https://doi.org/10.1002/humu.23891, doi:10.1002/humu.23891. This article has 37 citations and is from a domain leading peer-reviewed journal.

2. (diaz‐horta2019novelvariantp.e269k pages 1-5): Oscar Diaz‐Horta, Guney Bademci, Suna Tokgoz‐Yilmaz, Shengru Guo, Faraz Zafeer, Claire J. Sineni, Duygu Duman, Amjad Farooq, and Mustafa Tekin. Novel variant p.e269k confirms causative role of pls1 mutations in autosomal dominant hearing loss. Clinical Genetics, 96:575-578, Dec 2019. URL: https://doi.org/10.1111/cge.13626, doi:10.1111/cge.13626. This article has 16 citations and is from a peer-reviewed journal.

3. (schrauwen2019hearingimpairmentlocus pages 2-3): Isabelle Schrauwen, Béla I. Melegh, Imen Chakchouk, Anushree Acharya, Abdul Nasir, Alexis Poston, Diana M. Cornejo-Sanchez, Zsolt Szabo, Tamás Karosi, Judit Bene, Béla Melegh, and Suzanne M. Leal. Hearing impairment locus heterogeneity and identification of pls1 as a new autosomal dominant gene in hungarian roma. European Journal of Human Genetics, 27:869-878, Mar 2019. URL: https://doi.org/10.1038/s41431-019-0372-y, doi:10.1038/s41431-019-0372-y. This article has 23 citations and is from a domain leading peer-reviewed journal.

4. (taylor2015absenceofplastin pages 2-3): Ruth Taylor, Anwen Bullen, Stuart L. Johnson, Eva-Maria Grimm-Günter, Francisco Rivero, Walter Marcotti, Andrew Forge, and Nicolas Daudet. Absence of plastin 1 causes abnormal maintenance of hair cell stereocilia and a moderate form of hearing loss in mice. Human Molecular Genetics, 24:37-49, Aug 2015. URL: https://doi.org/10.1093/hmg/ddu417, doi:10.1093/hmg/ddu417. This article has 79 citations and is from a domain leading peer-reviewed journal.

5. (xu2022anovelpls1 pages 10-13): Liangpu Xu, Xinrui Wang, Jia Li, Lingji Chen, Haiwei Wang, Shiyi Xu, Yanhong Zhang, Wei Li, Pengcheng Yao, Meihua Tan, Si Zhou, Meihuan Chen, Yali Pan, Xuemei Chen, Xiaolan Chen, Yunliang Liu, Na Lin, Hailong Huang, and Hua Cao. A novel pls1 c.981+1g&gt;a variant causes autosomal-dominant hereditary hearing loss in a family via up-regulation of the pi3k-akt signaling pathway. Mar 2022. URL: https://doi.org/10.1101/2022.03.17.484618, doi:10.1101/2022.03.17.484618. This article has 0 citations.

6. (xu2026pathogenicmechanismof pages 1-4): Tingting Xu, Tao Yang, Haiwei Wang, and Liangpu Xu. Pathogenic mechanism of the pls1 gene variant in hearing loss and functional validation in a zebrafish model. Scientific Reports, Apr 2026. URL: https://doi.org/10.1038/s41598-026-47079-4, doi:10.1038/s41598-026-47079-4. This article has 0 citations and is from a peer-reviewed journal.

7. (schrauwen2019hearingimpairmentlocus pages 7-9): Isabelle Schrauwen, Béla I. Melegh, Imen Chakchouk, Anushree Acharya, Abdul Nasir, Alexis Poston, Diana M. Cornejo-Sanchez, Zsolt Szabo, Tamás Karosi, Judit Bene, Béla Melegh, and Suzanne M. Leal. Hearing impairment locus heterogeneity and identification of pls1 as a new autosomal dominant gene in hungarian roma. European Journal of Human Genetics, 27:869-878, Mar 2019. URL: https://doi.org/10.1038/s41431-019-0372-y, doi:10.1038/s41431-019-0372-y. This article has 23 citations and is from a domain leading peer-reviewed journal.

8. (xu2022anovelpls1 pages 13-19): Liangpu Xu, Xinrui Wang, Jia Li, Lingji Chen, Haiwei Wang, Shiyi Xu, Yanhong Zhang, Wei Li, Pengcheng Yao, Meihua Tan, Si Zhou, Meihuan Chen, Yali Pan, Xuemei Chen, Xiaolan Chen, Yunliang Liu, Na Lin, Hailong Huang, and Hua Cao. A novel pls1 c.981+1g&gt;a variant causes autosomal-dominant hereditary hearing loss in a family via up-regulation of the pi3k-akt signaling pathway. Mar 2022. URL: https://doi.org/10.1101/2022.03.17.484618, doi:10.1101/2022.03.17.484618. This article has 0 citations.

9. (taylor2015absenceofplastin pages 1-1): Ruth Taylor, Anwen Bullen, Stuart L. Johnson, Eva-Maria Grimm-Günter, Francisco Rivero, Walter Marcotti, Andrew Forge, and Nicolas Daudet. Absence of plastin 1 causes abnormal maintenance of hair cell stereocilia and a moderate form of hearing loss in mice. Human Molecular Genetics, 24:37-49, Aug 2015. URL: https://doi.org/10.1093/hmg/ddu417, doi:10.1093/hmg/ddu417. This article has 79 citations and is from a domain leading peer-reviewed journal.

10. (xu2022anovelpls1 pages 1-4): Liangpu Xu, Xinrui Wang, Jia Li, Lingji Chen, Haiwei Wang, Shiyi Xu, Yanhong Zhang, Wei Li, Pengcheng Yao, Meihua Tan, Si Zhou, Meihuan Chen, Yali Pan, Xuemei Chen, Xiaolan Chen, Yunliang Liu, Na Lin, Hailong Huang, and Hua Cao. A novel pls1 c.981+1g&gt;a variant causes autosomal-dominant hereditary hearing loss in a family via up-regulation of the pi3k-akt signaling pathway. Mar 2022. URL: https://doi.org/10.1101/2022.03.17.484618, doi:10.1101/2022.03.17.484618. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Hearing_Loss_Autosomal_Dominant_76-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.