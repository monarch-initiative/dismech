---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T17:01:07.663377'
end_time: '2026-09-02T17:15:40.833488'
duration_seconds: 873.17
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Short-Rib Thoracic Dysplasia 9 With or Without Polydactyly
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 76
  verified: 71
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - OMIM
  - Taxon
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Short-Rib_Thoracic_Dysplasia_9_With_Or_Without_Polydactyly-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Short-Rib Thoracic Dysplasia 9 With or Without Polydactyly
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Short-Rib Thoracic Dysplasia 9 With or Without Polydactyly** covering all of the
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
- **Disease Name:** Short-Rib Thoracic Dysplasia 9 With or Without Polydactyly
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Short-Rib Thoracic Dysplasia 9 With or Without Polydactyly** covering all of the
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


# Short-Rib Thoracic Dysplasia 9 With or Without Polydactyly

## Executive summary

Short-rib thoracic dysplasia 9 with or without polydactyly (SRTD9) is an ultra-rare, congenital, autosomal-recessive skeletal ciliopathy caused principally by **biallelic pathogenic variants in IFT140**. It overlaps clinically with **Mainzer–Saldino syndrome (MSS; conorenal syndrome)**, Jeune/asphyxiating thoracic dystrophy, and, less commonly, cranioectodermal dysplasia/Sensenbrenner syndrome. Its most characteristic combination is cone-shaped phalangeal epiphyses and other skeletal abnormalities, progressive nephronophthisis-like kidney disease, and early retinal dystrophy; a short, narrow thorax and polydactyly are variable rather than obligatory. The severity ranges from severe prenatal skeletal disease or respiratory compromise to a relatively mild thoracic phenotype with childhood renal failure and progressive visual disability. (sharova2023rareift140associatedphenotype pages 1-2, perrault2012mainzersaldinosyndromeisa pages 1-1, sharova2023rareift140associatedphenotype pages 5-7)

The evidence base is limited chiefly to small family series and case reports. Consequently, prevalence, penetrance of individual manifestations, survival, and treatment-response percentages cannot be estimated reliably. Recent 2023–2024 work has chiefly expanded the prenatal phenotype and demonstrated that **whole-genome or dedicated copy-number analysis is sometimes necessary to find a recurrent IFT140 exons 27–30 tandem duplication missed by routine panel or exome analysis**. (sharova2023rareift140associatedphenotype pages 1-2, margiotti2024compoundheterozygousvariants pages 3-4, sharova2023rareift140associatedphenotype pages 5-7)

A concise ontology-ready summary precedes the detailed report.

| Domain | High-confidence finding | Suggested ontology identifiers/terms | Evidence type/strength |
|---|---|---|---|
| Identifiers | Short-rib thoracic dysplasia 9 with or without polydactyly (SRTD9) is an IFT140-related skeletal ciliopathy overlapping Mainzer–Saldino syndrome, Jeune/asphyxiating thoracic dystrophy, and occasionally cranioectodermal dysplasia. (OpenTargets Search: Short-rib thoracic dysplasia 9 with or without polydactyly-IFT140, sharova2023rareift140associatedphenotype pages 1-2, walczaksztulpa2022identicalift140variants pages 1-2) | MONDO:0009964; OMIM:266920; Mainzer–Saldino syndrome; conorenal syndrome | Curated resources and human molecular studies; **high** |
| Gene and inheritance | SRTD9 is caused by biallelic germline pathogenic variants in **IFT140** and is autosomal recessive. Homozygous and compound-heterozygous cases are established. (margiotti2024compoundheterozygousvariants pages 3-4, perrault2012mainzersaldinosyndromeisa pages 1-1, helm2017partialuniparentalisodisomy pages 1-2) | IFT140; HGNC:29077; ENSG00000187535; HP:0000007 Autosomal recessive inheritance | Human segregation and functional evidence; **high** |
| Allelic distinction | Monoallelic IFT140 loss-of-function variants cause a distinct autosomal-dominant polycystic-kidney-disease spectrum, not SRTD9. IFT172 may cause an overlapping Mainzer–Saldino phenotype but is not the defining gene for IFT140-related SRTD9. (OpenTargets Search: Short-rib thoracic dysplasia 9 with or without polydactyly-IFT140, senum2022monoallelicift140pathogenic pages 1-4, senum2022monoallelicift140pathogenic pages 7-10) | MONDO:0100509 IFT140-related recessive ciliopathy; IFT172; HP:0000006 Autosomal dominant inheritance | Human cohorts and curated associations; **high** |
| Variant spectrum | Disease alleles include missense, nonsense, frameshift, splice-altering variants, and multiexon tandem duplications. A recurrent exons 27–30 duplication may be missed by routine exome analysis. Viable patients commonly retain at least one hypomorphic/nontruncating allele, suggesting complete biallelic loss may be embryonically lethal. (margiotti2024compoundheterozygousvariants pages 3-4, sharova2023rareift140associatedphenotype pages 5-7, walczaksztulpa2022identicalift140variants pages 1-2, senum2022monoallelicift140pathogenic pages 15-17) | SO:0001583 missense; SO:0001587 stop-gained; SO:0001589 frameshift; SO:0001574 splice acceptor; SO:0001742 copy-number gain | Human molecular evidence; lethality inference **moderate–high** |
| Skeletal phenotype | Congenital findings include shortened limbs or short stature, short ribs, narrow thorax, brachydactyly, and characteristic cone-shaped phalangeal epiphyses. Polydactyly is variable and not required. (sharova2023rareift140associatedphenotype pages 1-2, margiotti2024compoundheterozygousvariants pages 3-4, sharova2023rareift140associatedphenotype pages 5-7, senum2022monoallelicift140pathogenic pages 7-10) | HP:0000774 Narrow chest; HP:0000894 Short ribs; HP:0004322 Short stature; HP:0001156 Brachydactyly; HP:0010579 Cone-shaped epiphysis; HP:0010442 Polydactyly | Repeated human observations; **high**, percentages unavailable |
| Respiratory phenotype | Thoracic restriction ranges from mild narrowing to pulmonary hypoplasia or restrictive respiratory insufficiency. Recurrent respiratory infections and pneumonia occur in some patients. (sharova2023rareift140associatedphenotype pages 1-2, margiotti2024compoundheterozygousvariants pages 3-4) | HP:0002091 Restrictive respiratory insufficiency; HP:0002089 Pulmonary hypoplasia; HP:0002205 Recurrent respiratory infections | Human cases and reviews; **moderate** |
| Renal phenotype | Progressive nephronophthisis-like tubulointerstitial or cystic kidney disease is a core manifestation and can cause childhood chronic kidney disease and end-stage kidney disease requiring dialysis or transplantation. (sharova2023rareift140associatedphenotype pages 1-2, helm2017partialuniparentalisodisomy pages 1-2, sharova2023rareift140associatedphenotype pages 5-7, walczaksztulpa2020compoundheterozygousift140 pages 10-10) | HP:0000090 Nephronophthisis; HP:0012622 Chronic kidney disease; HP:0003774 End-stage renal disease; HP:0000107 Renal cyst; UBERON:0002113 kidney | Multiple human reports; **high** |
| Ocular phenotype | Early retinal dystrophy, commonly rod–cone degeneration or retinitis pigmentosa, may cause nystagmus, nyctalopia, refractive error, abnormal electroretinography, and progressive visual impairment. Rare renal-skeletal cases lack retinopathy, showing variable expressivity. (sharova2023rareift140associatedphenotype pages 1-2, helm2017partialuniparentalisodisomy pages 1-2, sharova2023rareift140associatedphenotype pages 5-7) | HP:0000556 Retinal dystrophy; HP:0000510 Rod-cone dystrophy; HP:0000662 Nyctalopia; HP:0000639 Nystagmus; UBERON:0000966 retina; CL:0000210 photoreceptor cell | Human ophthalmic phenotyping; **high**, penetrance unquantified |
| Other phenotypes | Craniosynostosis, craniofacial dysmorphism, ectodermal abnormalities, liver disease, congenital heart defects, scoliosis, and possible hearing impairment occur variably across the IFT140 ciliopathy spectrum; none is obligatory. (sharova2023rareift140associatedphenotype pages 1-2, margiotti2024compoundheterozygousvariants pages 3-4, walczaksztulpa2022identicalift140variants pages 1-2) | HP:0001363 Craniosynostosis; HP:0002650 Scoliosis; HP:0000365 Hearing impairment; HP:0001392 Abnormal liver morphology; HP:0001627 Abnormal heart morphology | Small series and cases; **low–moderate** |
| Mechanism | IFT140 is a core IFT-A component required for retrograde transport from the ciliary tip to base and for ciliary membrane-cargo handling. Pathogenic variants cause absent, shortened, or bulbous cilia and abnormal accumulation or localization of IFT proteins. (margiotti2024compoundheterozygousvariants pages 3-4, perrault2012mainzersaldinosyndromeisa pages 1-1, senum2022monoallelicift140pathogenic pages 1-4, senum2022monoallelicift140pathogenic pages 15-17) | GO:0035721 Intraciliary retrograde transport; GO:0060271 Cilium assembly; GO:0005929 Cilium; GO:0036064 Ciliary basal body | Patient cells and experimental models; **high** |
| Tissue pathophysiology | Defective ciliary transport perturbs developmental signaling, especially Hedgehog and possibly Wnt, in chondrocytes, renal tubular epithelia, and photoreceptors. This is inferred to produce abnormal endochondral ossification, tubulointerstitial/cystic renal injury, and defective photoreceptor transport followed by degeneration. (perrault2012mainzersaldinosyndromeisa pages 1-1, senum2022monoallelicift140pathogenic pages 7-10) | GO:0007224 Smoothened signaling; GO:0060070 Canonical Wnt signaling; GO:0001503 Ossification; GO:0072080 Nephron tubule development; CL:0000138 Chondrocyte | Human cellular and animal evidence; downstream human chain partly inferred; **moderate–high** |
| Functional evidence | Patient fibroblasts show reduced ciliation and abnormal IFT localization. Urine-derived renal epithelial cells showed IFT88 accumulation at ciliary tips in **41%** of cells; engineered rescue assays reproduced impaired retrograde transport. (perrault2012mainzersaldinosyndromeisa pages 1-1) | GO:0035721 Intraciliary retrograde transport; GO:0005929 Cilium; renal epithelial cell | Direct patient-cell and engineered-cell experiments; **high** |
| Diagnosis | Diagnosis combines prenatal or postnatal skeletal imaging, renal assessment, retinal examination, and identification of two pathogenic or likely pathogenic IFT140 alleles in trans. Useful studies include skeletal survey, renal ultrasonography, serum creatinine/eGFR, urinalysis, retinal imaging, and electroretinography. | HPO-based phenotyping; LOINC creatinine, eGFR, urinalysis, and electroretinography concepts | Multidisciplinary clinical practice supported by human reports; **moderate–high** |
| Genetic testing | Use a skeletal-ciliopathy or renal-retinal ciliopathy panel with deletion/duplication analysis, or trio exome sequencing. If only one allele is found, use genome sequencing, CNV/read-depth analysis, breakpoint PCR, and possibly RNA studies to detect tandem duplications or cryptic splice variants. (sharova2023rareift140associatedphenotype pages 1-2, sharova2023rareift140associatedphenotype pages 5-7, sharova2023rareift140associatedphenotype pages 8-9) | NCIT:C101296 Next-Generation Sequencing; NCIT:C101295 Whole Exome Sequencing; NCIT:C101294 Whole Genome Sequencing; NCIT:C116160 Copy Number Variation Analysis | Human diagnostic evidence; **high** |
| Differential diagnosis | Major alternatives include other short-rib thoracic dysplasias involving DYNC2H1, WDR19, WDR35, IFT122, IFT172, and IFT80; cranioectodermal dysplasia; Senior–Løken syndrome; isolated IFT140 retinal dystrophy; and monoallelic IFT140-associated ADPKD. (OpenTargets Search: Short-rib thoracic dysplasia 9 with or without polydactyly-IFT140, sharova2023rareift140associatedphenotype pages 1-2, senum2022monoallelicift140pathogenic pages 1-4, walczaksztulpa2022identicalift140variants pages 1-2) | MONDO skeletal ciliopathy; HP:0000894 Short ribs; HP:0000090 Nephronophthisis; HP:0000556 Retinal dystrophy | Genetic and phenotypic-overlap evidence; **high** |
| Epidemiology | SRTD9 is ultra-rare. Reliable prevalence, incidence, carrier-frequency, sex-ratio, and geographic-distribution estimates are **unavailable**. The foundational study identified IFT140 variants in 7 of 16 selected Mainzer–Saldino families, which is not a population prevalence estimate. (perrault2012mainzersaldinosyndromeisa pages 1-1) | MONDO:0009964; rare disease | Small, ascertainment-biased family series; **insufficient for population frequency** |
| Prognosis | Prognosis is highly variable and is driven principally by thoracic insufficiency and renal decline. Survivors may develop progressive visual disability and lifelong skeletal morbidity. Childhood kidney failure occurs, but transplantation is feasible. Disease-specific survival and life-expectancy estimates are **unavailable**. (sharova2023rareift140associatedphenotype pages 1-2, sharova2023rareift140associatedphenotype pages 5-7, walczaksztulpa2020compoundheterozygousift140 pages 10-10) | HP:0002091 Restrictive respiratory insufficiency; HP:0003774 End-stage renal disease; HP:0000556 Retinal dystrophy | Human cases and small series; **moderate**, quantitative survival data absent |
| Management | Management is multidisciplinary and organ-directed: respiratory support and infection treatment; renal-function, blood-pressure, and imaging surveillance; standard CKD care, dialysis, and transplantation; retinal surveillance and low-vision services; orthopedic, audiologic, nutritional, rehabilitation, and developmental support. | NCIT:C15329 Supportive Care; NCIT:C15231 Dialysis; NCIT:C15263 Kidney Transplantation; NCIT:C16268 Physical Therapy; NCIT:C16882 Genetic Counseling | Expert-practice extrapolation and reported transplantation; **moderate** |
| Disease-modifying therapy | **No approved SRTD9 disease-modifying drug, gene therapy, RNA therapy, or cell therapy exists, and no disease-specific interventional trial was identified.** Pathway-directed treatments studied in other renal-ciliopathy models remain experimental. | NCIT:C1908 Gene Therapy; NCIT:C15747 Investigational New Drug | Trial search and literature review; **high confidence for current absence** |
| Prevention and counseling | Lifestyle or environmental modification cannot prevent the congenital disorder. Familial-variant testing enables carrier and cascade testing, prenatal diagnosis, and preimplantation genetic testing. For two carrier parents, each pregnancy has 25% affected, 50% carrier, and 25% unaffected/non-carrier probabilities. | HP:0000007 Autosomal recessive inheritance; NCIT:C16882 Genetic Counseling; prenatal and preimplantation genetic testing | Mendelian genetics and established reproductive practice; **high** |
| Model organisms | ENU/hypomorphic and conditional **Ift140** mouse models reproduce ciliary, skeletal, renal, craniofacial, cardiac, pulmonary, and polydactyly phenotypes; renal collecting-duct deletion causes cysts, fibrosis, and short cilia. Zebrafish complementation supports loss of function, and C. elegans variant models reproduce short cilia, IFT accumulation, and cargo mislocalization. (helm2017partialuniparentalisodisomy pages 1-2, senum2022monoallelicift140pathogenic pages 7-10) | NCBI Taxon:10090 Mus musculus; NCBI Taxon:7955 Danio rerio; NCBI Taxon:6239 Caenorhabditis elegans; MGI Ift140 | Multiple induced genetic models; **high mechanistic value**, incomplete human phenocopy |
| Natural disease in animals | No well-established naturally occurring veterinary SRTD9 caused by orthologous biallelic IFT140 variants was identified. Reported animal systems are predominantly experimentally induced models. | NCBI Taxonomy; OMIA—no confirmed entry identified | Database/literature gap; **unavailable** |


*Table: Compact ontology-ready summary of the genetic basis, phenotypes, mechanism, diagnosis, management, prognosis, epidemiologic gaps, and experimental models for SRTD9. Evidence strength distinguishes established human findings from mechanistic inference and unavailable data.*

## 1. Disease information

### Definition and scope

SRTD9 is a developmental disorder of primary cilia in which defective IFT140-dependent intraflagellar transport affects cartilage and bone, kidney tubules, photoreceptors, and sometimes additional tissues. In contemporary usage, “SRTD9” is the molecularly defined **IFT140-related skeletal ciliopathy**, whereas “Mainzer–Saldino syndrome” denotes a recognizable clinical presentation dominated by phalangeal cone-shaped epiphyses, renal disease, and retinal dystrophy. IFT140-related disease nevertheless forms a continuum; rigid assignment to MSS, Jeune syndrome, or Sensenbrenner syndrome may be less accurate than “IFT140-related recessive ciliopathy” followed by a detailed phenotype. Identical IFT140 alleles have produced MZSDS-like and CED-like phenotypes in unrelated patients. (sharova2023rareift140associatedphenotype pages 1-2, walczaksztulpa2022identicalift140variants pages 1-2)

### Identifiers and synonyms

- **MONDO:** **MONDO:0009964**, short-rib thoracic dysplasia 9 with or without polydactyly.
- **OMIM phenotype:** **266920**.
- **Broader/current molecular concept:** MONDO:0100509, IFT140-related recessive ciliopathy.
- **Causal gene:** IFT140; Ensembl ENSG00000187535; HGNC:29077.
- **Common names:** SRTD9; Mainzer–Saldino syndrome; Mainzer-Saldino syndrome; conorenal syndrome; IFT140-related skeletal ciliopathy; IFT140-related recessive ciliopathy. “Jeune/asphyxiating thoracic dystrophy” and “cranioectodermal dysplasia/Sensenbrenner syndrome” may describe overlapping presentations but are not exact synonyms in every patient. (OpenTargets Search: Short-rib thoracic dysplasia 9 with or without polydactyly-IFT140, sharova2023rareift140associatedphenotype pages 1-2)
- **Orphanet:** MSS is represented in Orphanet, but a reliable disease-specific Orpha number was not established from the retrieved primary sources and should be verified directly before database ingestion.
- **ICD-10/ICD-11 and MeSH:** no uniquely specific SRTD9 code or MeSH descriptor was established. Coding generally falls under congenital osteochondrodysplasia/skeletal dysplasia and relevant organ complications; such broad codes should not be treated as disease-specific identifiers.

This report synthesizes **aggregated disease-level literature and curated resources**, not individual EHR data. Patient-level observations come from published case reports or small research cohorts.

## 2. Etiology and risk/protective factors

### Primary cause

SRTD9 is caused by **germline biallelic loss-of-function or hypomorphic IFT140 alleles**, inherited in homozygous or compound-heterozygous state. IFT140 encodes a 1,462-amino-acid WD/TPR-repeat protein and core component of intraflagellar transport complex A (IFT-A), which participates in retrograde transport from the ciliary tip toward the base and in entry/handling of ciliary membrane cargo. (margiotti2024compoundheterozygousvariants pages 3-4, perrault2012mainzersaldinosyndromeisa pages 1-1, senum2022monoallelicift140pathogenic pages 1-4)

The 2012 foundational series studied 16 families meeting clinical MSS criteria and found IFT140 mutations in seven families. This **7/16 is an ascertainment-dependent diagnostic fraction, not prevalence**. The conference abstract summarized MSS as “a rare disorder characterized by phalangeal cone-shaped epiphyses, chronic renal failure and early-onset severe retinal dystrophy.” The corresponding AJHG report is Perrault et al., published May 2012, PMID **22503633**, DOI/URL: https://doi.org/10.1016/j.ajhg.2012.03.006. (perrault2012mainzersaldinosyndromeisa pages 1-1, sharova2023rareift140associatedphenotype pages 8-9)

### Genetic risk factors and variant classes

Reported pathogenic or likely pathogenic alleles include missense, nonsense, frameshift, canonical splice-site and multiexon duplication variants. Examples include:

- c.634G>A, p.Gly212Arg, which predominantly caused aberrant splicing and a premature termination codon in a patient with segmental maternal uniparental isodisomy;
- c.1565G>A, p.Gly522Glu;
- r.2765_2768del, p.Tyr923Leufs*28;
- the recurrent exons 27–30 tandem duplication, predicted p.Tyr1152_Thr1394dup;
- 2024 prenatal compound-heterozygous p.Ser580dup and p.Gly522Glu alleles. (margiotti2024compoundheterozygousvariants pages 3-4, helm2017partialuniparentalisodisomy pages 1-2, sharova2023rareift140associatedphenotype pages 5-7, walczaksztulpa2022identicalift140variants pages 1-2)

Population frequency must be assessed separately for each variant in gnomAD and ancestry-matched databases. Pathogenic recessive alleles are expected to be absent or very rare; no defensible aggregate carrier frequency is available. Viable affected people commonly retain at least one missense or otherwise hypomorphic allele, suggesting—but not proving—that complete biallelic IFT140 loss is often embryonically lethal. (senum2022monoallelicift140pathogenic pages 15-17)

All established SRTD9 alleles are germline. Somatic mutation is not part of the known disease mechanism. No recurrent aneuploidy, translocation, or pathogenic methylation signature defines SRTD9. Segmental uniparental isodisomy of chromosome 16 is a rare mechanism that can render a single parental allele homozygous. (helm2017partialuniparentalisodisomy pages 1-2)

### Modifier effects

No modifier gene is clinically validated. However, one CED-like patient with the same biallelic IFT140 variants as an MZSDS-like patient also carried a likely pathogenic heterozygous **INTU** variant; the authors proposed that this might contribute to severity through the ciliary transport network. This remains a single-patient modifier hypothesis. Broader “ciliary mutational load,” epistasis, and genetic background are plausible explanations for variable expressivity but are not ready for predictive use. (walczaksztulpa2022identicalift140variants pages 1-2)

### Environmental, lifestyle, infectious and protective factors

No toxin, infection, diet, activity pattern, parental age, sex, or occupational exposure is known to cause or materially alter SRTD9. No protective genetic allele, diet, drug, or environmental exposure has been established. Environmental measures can reduce complications—such as avoiding smoke exposure in a patient with restrictive lung disease—but do not prevent the Mendelian disorder. Gene–environment interactions have not been demonstrated.

## 3. Phenotypes

Because cohorts are very small and differently ascertained, the literature supports qualitative frequencies—core, common, variable, or rare—rather than population percentages.

### Skeletal and thoracic manifestations

- **Cone-shaped phalangeal epiphyses** are the classic radiographic hallmark and may become more conspicuous with age. Suggested HPO: **HP:0010579 Cone-shaped epiphysis**.
- **Short limbs/short stature**, rhizomelic shortening, shortened or thick long bones, brachydactyly and pelvic abnormalities are common but variable. HPO: HP:0004322, HP:0008905, HP:0001156.
- **Short ribs and narrow thorax** range from mild to severe. HPO: HP:0000894 and HP:0000774.
- **Polydactyly** may be preaxial or postaxial but is not required, despite its inclusion in the disease name. HPO: HP:0010442 or the anatomically specific subtype.
- **Scoliosis, craniosynostosis and craniofacial dysmorphism** occur in portions of the IFT140 spectrum. HPO: HP:0002650, HP:0001363. (sharova2023rareift140associatedphenotype pages 1-2, margiotti2024compoundheterozygousvariants pages 3-4, sharova2023rareift140associatedphenotype pages 5-7, senum2022monoallelicift140pathogenic pages 7-10)

Onset is prenatal/congenital. Skeletal disproportion is generally persistent; spinal and functional consequences may progress during growth. A November 2024 prenatal report described increased nuchal translucency, shortened and thick long bones, hypoplastic tibiae/fibulae, flat nose, frontal bossing and apparent absent bladder in a fetus with compound-heterozygous IFT140 variants. It expands prenatal recognition but does not establish the frequency of these features. DOI: https://doi.org/10.3390/diagnostics14222601. (margiotti2024compoundheterozygousvariants pages 3-4)

### Respiratory phenotype

A narrow rib cage can reduce lung volume and cause neonatal or childhood restrictive respiratory insufficiency; pulmonary hypoplasia and early death are possible at the severe end. Milder MSS presentations may have thoracic narrowing without asphyxia. Recurrent respiratory infection or pneumonia has been reported. Suggested HPO terms: HP:0002091 Restrictive respiratory insufficiency, HP:0002089 Pulmonary hypoplasia, HP:0002205 Recurrent respiratory infections. Respiratory morbidity directly affects feeding, mobility, hospitalization burden and survival. (sharova2023rareift140associatedphenotype pages 1-2, margiotti2024compoundheterozygousvariants pages 3-4)

### Renal phenotype

Progressive nephronophthisis-like tubulointerstitial disease, renal cysts and fibrosis are core manifestations. Presentations include polyuria/polydipsia, impaired concentrating ability, anemia, growth failure, proteinuria, elevated creatinine, metabolic acidosis, hypertension, chronic kidney disease and end-stage kidney disease. Childhood dialysis and transplantation have been reported, including progression to dialysis by age seven in one IFT140-spectrum patient. HPO: HP:0000090 Nephronophthisis, HP:0000107 Renal cyst, HP:0012622 CKD, HP:0003774 ESKD, HP:0001947 Renal tubular acidosis where documented. (helm2017partialuniparentalisodisomy pages 1-2, sharova2023rareift140associatedphenotype pages 5-7, walczaksztulpa2020compoundheterozygousift140 pages 10-10)

A February 2024 case described a 20-month-old boy with recurrent pneumonia, elevated creatinine, proteinuria and high-anion-gap partially compensated metabolic acidosis; genetic testing redirected an initial biopsy-based diagnosis of Alport syndrome to MSS. The abstract states that MSS “typically presents with a triad of nephronophthisis (NPHP), retinitis pigmentosa (RP), and cone-shaped epiphysis (CSE) with varying degrees of severity.” DOI: https://doi.org/10.7759/cureus.53889. This is one case and should not be used to infer frequency. 

### Ocular phenotype

Retinal degeneration often begins in infancy or childhood and may include nystagmus, poor fixation, nyctalopia, rod–cone dystrophy/retinitis pigmentosa, reduced electroretinographic responses, high myopia or hypermetropia, strabismus, optic atrophy and progressive visual loss. HPO: HP:0000556 Retinal dystrophy, HP:0000510 Rod-cone dystrophy, HP:0000662 Nyctalopia, HP:0000639 Nystagmus, HP:0000545 Myopia. Some patients with renal-skeletal disease have no retinopathy, demonstrating incomplete manifestation or age-dependent ascertainment. (sharova2023rareift140associatedphenotype pages 1-2, helm2017partialuniparentalisodisomy pages 1-2, sharova2023rareift140associatedphenotype pages 5-7)

Biallelic IFT140 variants can also cause nonsyndromic retinal dystrophy: eight patients from five families retained useful visual acuity into at least the second decade and lacked skeletal manifestations or renal failure at ages 13–67 years. Such cases are allelic IFT140 disease, but they should not automatically be labeled SRTD9.

### Additional variable phenotypes

Craniofacial abnormalities, thin hair, short/thin nails, small teeth, sagittal or other craniosynostosis, liver fibrosis/dysfunction, congenital heart malformations, hearing difficulty and developmental abnormalities have been reported across the IFT140 ciliopathy spectrum. Evidence for hearing impairment as an IFT140 manifestation is preliminary: in one child no alternative hearing-loss variant was found, but causality was not proved. Suggested HPO: HP:0000365 Hearing impairment, HP:0001392 Abnormal liver morphology, HP:0001627 Abnormal heart morphology, HP:0001595 Abnormal hair morphology, HP:0001597 Abnormal nail morphology. (sharova2023rareift140associatedphenotype pages 1-2, walczaksztulpa2022identicalift140variants pages 1-2)

No characteristic behavioral or psychiatric phenotype and no disease-specific circulating biomarker have been established. Quality-of-life studies using EQ-5D, SF-36 or PROMIS have not been published specifically for SRTD9. Likely burdens include visual disability, CKD treatment, respiratory limitation, short stature, orthopedic impairment and frequent multidisciplinary care, but quantitative utility scores are unavailable.

## 4. Genetic and molecular information

### Causal-gene assignment

**IFT140 is the defining causal gene for SRTD9.** OpenTargets gives the IFT140–SRTD9 association the strongest score and cites human genetic evidence including PMIDs 22503633, 23418020, 24009529, 28288023 and 28724397. IFT172 is associated with an overlapping MSS/Jeune phenotype, but it should not be entered as a second causal gene for the specifically molecularly defined IFT140-related SRTD9 record without an explicit nosologic policy. (OpenTargets Search: Short-rib thoracic dysplasia 9 with or without polydactyly-IFT140)

### Functional consequences and classification

The disease mechanism is reduced IFT140 function rather than demonstrated gain of function or dominant negativity. Pathogenicity evidence can include segregation in trans, rarity, predicted loss of function, aberrant RNA, defective basal-body/ciliary localization, abnormal cilia morphology, IFT88 accumulation at ciliary tips, and rescue in engineered cells. In patient urine-derived renal epithelial cells, **41%** of cells showed IFT88 tip accumulation, absent in controls, supporting impaired retrograde transport. (perrault2012mainzersaldinosyndromeisa pages 1-1)

Variants should be classified individually under current ACMG/AMP criteria; an IFT140 missense change must not be called pathogenic from phenotype or computational prediction alone. A VUS is not diagnostic. Functional assays are particularly helpful but are not standardized clinical tests. The 2024 p.Ser580dup report applied PM2, PM3 and PM4 evidence and classified it as likely pathogenic. (margiotti2024compoundheterozygousvariants pages 3-4)

### Important allelic distinction

Monoallelic IFT140 loss-of-function variants cause a separate, autosomal-dominant atypical polycystic-kidney-disease spectrum, generally featuring a few large cysts, mild/late renal insufficiency and few liver cysts—not the recessive skeletal-retinal SRTD9 phenotype. In a 2022 study, monoallelic IFT140 variants accounted for 1.9% of previously unresolved ADPKD families and 2.1% of Genomics England cystic-kidney probands. These statistics must not be used as SRTD9 prevalence estimates. DOI: https://doi.org/10.1016/j.ajhg.2021.11.016. (senum2022monoallelicift140pathogenic pages 1-4)

No SRTD9-specific DNA-methylation, histone, chromatin, somatic-mosaic, repeat-expansion or mitochondrial-DNA mechanism is established. Germline mosaicism is theoretically possible for any recessive allele but has not emerged as a characteristic mechanism.

## 5. Environmental information

SRTD9 is not infectious, transmissible, toxicant-induced or lifestyle-mediated. Smoking, alcohol, diet, exercise, radiation and pollution have no established etiologic role. Respiratory irritant avoidance, adequate nutrition, vaccination and infection prevention are complication-reduction measures, not causal treatment or primary prevention.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic IFT140 variants lead to** reduced abundance, stability, localization or function of IFT140 within IFT-A. (margiotti2024compoundheterozygousvariants pages 3-4, perrault2012mainzersaldinosyndromeisa pages 1-1, helm2017partialuniparentalisodisomy pages 1-2)
2. **IFT140 dysfunction leads to** defective retrograde intraflagellar transport and abnormal ciliary membrane-cargo entry/turnover. (senum2022monoallelicift140pathogenic pages 1-4, senum2022monoallelicift140pathogenic pages 15-17)
3. **Defective transport results in** absent, shortened or bulbous primary cilia and accumulation/mislocalization of IFT proteins, including IFT88 at the ciliary tip; these changes are demonstrated in patient cells and experimental models. (perrault2012mainzersaldinosyndromeisa pages 1-1, senum2022monoallelicift140pathogenic pages 7-10)
4. **Abnormal primary cilia lead to** altered cilium-dependent developmental signaling, particularly Hedgehog and probably Wnt/planar-cell-polarity pathways; the pathway link is strongly supported in skeletal-ciliopathy models but is partly inferred for individual SRTD9 patients.
5. **In growth-plate chondrocytes, altered ciliary signaling leads to** disturbed chondrocyte organization/differentiation and endochondral ossification, resulting in short ribs, shortened long bones, cone-shaped epiphyses, thoracic narrowing and digit-patterning abnormalities.
6. **Branch A—thorax:** short ribs and abnormal chest development **lead to** reduced thoracic volume and, in severe cases, pulmonary hypoplasia/restrictive respiratory failure.
7. **Branch B—kidney:** ciliary dysfunction in tubular and collecting-duct epithelial cells **leads to** abnormal epithelial homeostasis and cystogenesis, followed by tubulointerstitial fibrosis and progressive CKD/ESKD; the exact molecular sequence in human SRTD9 remains incompletely demonstrated. (senum2022monoallelicift140pathogenic pages 7-10)
8. **Branch C—retina:** defective IFT in photoreceptor connecting cilia **leads to** impaired trafficking between inner and outer segments, photoreceptor degeneration and rod–cone retinal dystrophy.
9. **Additional tissue-specific ciliary defects lead to** variable craniofacial, cardiac, hepatic, ectodermal or auditory manifestations; these branches have weaker SRTD9-specific evidence.

### Protein, cellular and pathway detail

IFT-A and dynein-2 mediate retrograde movement along axonemal microtubules. Patient fibroblasts have shown reduced or absent primary cilia, reduced IFT140 basal-body localization and altered localization of anterograde IFT proteins. The urine-cell study and CRISPR-rescue experiment directly linked a patient missense allele to IFT88 tip accumulation. Thus, defective ciliary trafficking—not primary inflammation, autoimmunity, mitochondrial failure or enzyme deficiency—is upstream. (perrault2012mainzersaldinosyndromeisa pages 1-1)

Relevant GO terms include GO:0035721 intraciliary retrograde transport, GO:0060271 cilium assembly, GO:0007224 Smoothened signaling pathway, GO:0060070 canonical Wnt signaling, GO:0001503 ossification, GO:0072080 nephron tubule development and GO:0045494 photoreceptor cell maintenance. Cellular-component terms include GO:0005929 cilium, GO:0036064 ciliary basal body, GO:0097542 ciliary tip and GO:0097730 nonmotile cilium. Suggested cell types include CL:0000138 chondrocyte, CL:0002306 epithelial cell of proximal tubule, CL:0000653 podocyte, collecting-duct epithelial cell, CL:0000210 photoreceptor cell and CL:0000573 retinal pigment epithelial cell.

### Omics and advanced technologies

Patient-derived fibroblasts and urine-derived renal epithelial cells are established functional systems. Patient-iPSC kidney organoids have been used to validate a ciliopathic renal phenotype, but no SRTD9 biomarker or clinically deployable transcriptomic/proteomic/metabolomic signature has resulted. No mature SRTD9-specific single-cell atlas, spatial-transcriptomic study, lipidomic signature or CRISPR drug-screen result was identified. These are research gaps, not negative biological findings.

## 7. Anatomical structures affected

- **Primary skeletal sites:** ribs, thoracic cage, appendicular long bones, growth plates, phalanges, pelvis and sometimes vertebral column/skull. Suggested UBERON:0002228 rib, UBERON:0000915 thoracic segment, UBERON:0003606 growth plate cartilage, UBERON:0001448 long bone.
- **Kidney:** nephron tubules, collecting ducts and tubulointerstitium; UBERON:0002113 kidney, UBERON:0001285 nephron, UBERON:0001232 collecting duct.
- **Eye:** retina, photoreceptor connecting cilium and outer segment; UBERON:0000966 retina.
- **Secondary/variable:** lungs, liver/bile ducts, heart, inner ear, skin appendages and teeth.
- **Subcellular:** primary cilium, basal body, axoneme, ciliary tip and IFT trains.

Skeletal and renal abnormalities are generally bilateral/systemic rather than consistently lateralized. Polydactyly or individual malformations can be asymmetric, but no disease-defining lateralization is known.

## 8. Temporal development

The skeletal lesion begins embryonically and may be recognized on prenatal ultrasound through short long bones, short ribs, narrow chest or polydactyly. Respiratory risk is greatest in late gestation and the neonatal period when thoracic size determines pulmonary development. Cone-shaped epiphyses may be easier to recognize later in childhood. Renal disease can be occult initially but commonly progresses during childhood; retinal dystrophy can present in infancy or early childhood and is usually progressive. (sharova2023rareift140associatedphenotype pages 1-2, margiotti2024compoundheterozygousvariants pages 3-4, sharova2023rareift140associatedphenotype pages 5-7)

There are no validated disease stages. A clinically useful sequence is: prenatal/congenital skeletal disease; neonatal respiratory assessment; presymptomatic or early renal/retinal surveillance; progressive CKD and visual loss; and, in severe renal disease, dialysis/transplantation. Skeletal and genetic disease do not remit. Kidney transplantation can correct renal failure but not skeletal or retinal disease.

## 9. Inheritance and population

Inheritance is autosomal recessive. For two confirmed heterozygous parents, each conception has a 25% probability of an affected child, 50% probability of an unaffected carrier and 25% probability of an unaffected non-carrier. Both sexes are expected to be affected equally. Penetrance of a clearly pathogenic biallelic genotype is likely high for an IFT140-related phenotype, but organ-specific penetrance and severity are variable and not numerically established. There is no evidence of anticipation. Consanguinity increases the probability of homozygous rare alleles but is not required; compound heterozygosity is common. (margiotti2024compoundheterozygousvariants pages 3-4, perrault2012mainzersaldinosyndromeisa pages 1-1, walczaksztulpa2022identicalift140variants pages 1-2)

SRTD9 is ultra-rare. Reliable prevalence, incidence, carrier frequency, sex ratio, ethnic enrichment, founder effect and geographic distribution are unavailable. Published families come from multiple ancestries and countries, supporting worldwide occurrence rather than an endemic distribution.

## 10. Diagnostics

### Clinical and imaging evaluation

Prenatal ultrasound should assess long-bone length and shape, thoracic circumference, ribs, hands/feet, kidneys/bladder, amniotic fluid, heart and associated malformations. Postnatally, obtain a complete skeletal survey; characteristic findings include short ribs, long-bone shortening, brachydactyly and cone-shaped phalangeal epiphyses. Chest radiography or low-dose CT is reserved for clinically necessary thoracic assessment; pulmonary function testing is useful in cooperative older children.

Baseline and serial renal evaluation should include blood pressure, serum creatinine/eGFR, electrolytes and bicarbonate, complete blood count, urinalysis/protein quantification and renal ultrasonography. Ophthalmic evaluation should include age-appropriate visual assessment, dilated examination, fundus imaging, OCT where possible and electroretinography. Audiology, echocardiography and liver chemistry/ultrasound are reasonable baseline evaluations because extra-skeletal involvement is variable.

Kidney biopsy is not required when the clinical-genetic diagnosis is clear and can be misleading, as illustrated by the 2024 case initially interpreted as Alport syndrome. No disease-specific enzyme assay, circulating biomarker or newborn biochemical screen exists.

### Genetic-testing strategy

1. Use a comprehensive skeletal-ciliopathy or renal-retinal ciliopathy NGS panel that includes **IFT140** and validated exon-level deletion/duplication calling, or trio WES when the phenotype is broad.
2. Confirm candidate variants and phase them through parental testing.
3. If only one pathogenic IFT140 allele is found despite a compelling phenotype, perform read-depth/CNV analysis, targeted testing for the recurrent exons 27–30 tandem duplication, or WGS with breakpoint analysis. RNA studies can resolve suspected splice variants.
4. CMA may reveal copy-number changes or long regions of homozygosity/uniparental disomy but will miss most sequence-level disease alleles. Karyotyping and FISH are not routine diagnostic tests. mtDNA and repeat-expansion testing are not indicated unless an alternative disorder is suspected. (sharova2023rareift140associatedphenotype pages 1-2, helm2017partialuniparentalisodisomy pages 1-2, sharova2023rareift140associatedphenotype pages 5-7, sharova2023rareift140associatedphenotype pages 8-9)

The 2023 report is particularly instructive: panel or exome testing initially found only one allele in two MSS patients; WGS identified an exons 27–30 tandem duplication in one, and junction-targeted screening identified it in another. The authors wrote that WGS and duplication screening were important for “the formation of the correct diagnostic path.” Published 28 July 2023; DOI: https://doi.org/10.3390/genes14081553. (sharova2023rareift140associatedphenotype pages 1-2, sharova2023rareift140associatedphenotype pages 5-7)

### Differential diagnosis

Important alternatives include SRTD caused by **DYNC2H1, WDR19, WDR35, IFT122, IFT172, IFT80, WDR60, TTC21B** and related ciliary genes; cranioectodermal dysplasia; Senior–Løken syndrome; Bardet–Biedl syndrome; isolated inherited retinal degeneration; nephronophthisis; and nonciliary skeletal dysplasias. Distinguishing evidence comes from the precise radiographic pattern, thoracic severity, ectodermal findings, renal histology/imaging, retinal phenotype and—most decisively—biallelic molecular findings.

Monoallelic IFT140-related ADPKD must be separated from SRTD9. The former is dominant and mainly renal; the latter is recessive and usually multisystem. (senum2022monoallelicift140pathogenic pages 1-4, cristalli2025clinicalrelevanceof pages 8-9, cristalli2025clinicalrelevanceof pages 4-5)

## 11. Outcome and prognosis

Prognosis is highly variable. The strongest adverse factors are severe neonatal thoracic restriction/pulmonary hypoplasia and early progressive renal failure. Survivors can develop lifelong short stature and orthopedic disability, recurrent respiratory morbidity, progressive visual impairment and ESKD. Childhood transplantation is feasible, including in IFT140-associated CED-spectrum patients. (sharova2023rareift140associatedphenotype pages 1-2, sharova2023rareift140associatedphenotype pages 5-7, walczaksztulpa2020compoundheterozygousift140 pages 10-10)

No defensible 5-year or 10-year survival rate, life-expectancy estimate, disease-specific mortality rate, renal-failure probability or validated prognostic biomarker exists. Genotype alone does not reliably predict severity: identical alleles can produce MZSDS-like and CED-like disease. Thoracic size, neonatal respiratory requirement, serial eGFR, kidney imaging, and retinal function are clinically more useful than current molecular prognostication. (walczaksztulpa2022identicalift140variants pages 1-2)

## 12. Treatment and real-world implementation

There is **no approved disease-modifying pharmacotherapy, gene therapy, RNA therapy, cell therapy or genotype-specific treatment for SRTD9**. The ClinicalTrials.gov search identified no disease-specific interventional trial. Management is individualized and multidisciplinary:

- **Respiratory:** neonatal respiratory support, treatment of infections, vaccination, airway-clearance support where indicated, sleep evaluation and longitudinal pulmonary assessment. Severe thoracic insufficiency requires specialist thoracic/orthopedic review; evidence for expansion surgery is disorder- and anatomy-specific, not SRTD9-specific.
- **Renal:** avoid nephrotoxins and dehydration; manage hypertension, acidosis, anemia, mineral-bone disease and nutrition according to pediatric/adult CKD standards; use dialysis and **kidney transplantation** for ESKD. Transplantation treats renal failure but not retinal or skeletal disease.
- **Ophthalmic:** refractive correction, low-vision services, educational accommodations, mobility training and monitoring for treatable complications. No IFT140 retinal gene therapy is approved.
- **Orthopedic/rehabilitative:** physical and occupational therapy, pain management, monitoring of scoliosis and limb alignment, and surgery only for standard functional indications.
- **Other:** audiology and hearing support; dental care; nutrition and growth assessment; liver/cardiac surveillance guided by baseline findings; psychosocial and educational support.

Suggested NCIT terms include C15329 Supportive Care, C15231 Dialysis, C15263 Kidney Transplantation, C16268 Physical Therapy, C159524 Low Vision Rehabilitation and C16882 Genetic Counseling. There is no established pharmacogenomic guidance or treatment-response percentage. Experimental Hedgehog, cAMP/PKA and mTOR modulation has shown activity in other renal-ciliopathy models, but there is no evidence supporting off-label use for SRTD9. (senum2022monoallelicift140pathogenic pages 7-10)

## 13. Prevention

Primary prevention by lifestyle, vaccination or exposure modification is not possible. Secondary prevention consists of early molecular diagnosis and surveillance before irreversible respiratory, renal, visual or orthopedic complications. Tertiary prevention includes CKD control, infection prevention, respiratory support, rehabilitation and timely transplantation.

After familial variants are known, options include carrier and cascade testing, prenatal diagnosis by chorionic-villus sampling or amniocentesis, and preimplantation genetic testing for monogenic disease. Prenatal molecular testing should include the familial structural variant when applicable; exome sequencing alone may miss the exons 27–30 duplication. Population newborn screening is not available or currently justified by evidence. (sharova2023rareift140associatedphenotype pages 1-2, sharova2023rareift140associatedphenotype pages 5-7)

## 14. Other species and natural disease

No well-established naturally occurring companion-animal or livestock disease caused by orthologous biallelic IFT140 variants was identified. There is no zoonotic or cross-species transmission: SRTD9 is inherited, not infectious. Relevant orthologues are evolutionarily conserved in mouse, zebrafish and C. elegans, but published systems are predominantly induced experimental models.

## 15. Model organisms

### Mouse—Mus musculus, NCBI Taxon 10090

The ENU-induced **cauli** Ift140 allele causes mid-gestation lethality in homozygotes with neural-tube, craniofacial, digit, cardiac and somite-patterning defects, supporting developmental Hedgehog dysregulation. Kidney collecting-duct-specific Ift140 deletion produces extensive cystic growth, fibrosis and short/stumpy cilia by postnatal day 20, modeling the renal branch rather than the complete human phenotype. PMID **24009529** for the cauli model; DOI: https://doi.org/10.1371/journal.pgen.1003746. Conditional-timing experiments published in December 2023 further showed temporospatial requirements for Ift140 in heart looping, outflow development, craniofacial development and body-wall closure. These models have strong mechanistic value but often produce more severe embryonic disease than hypomorphic human SRTD9. (senum2022monoallelicift140pathogenic pages 7-10)

### Zebrafish—Danio rerio, NCBI Taxon 7955

In-vivo complementation demonstrated loss of function of the p.Gly212Arg-associated transcript in the uniparental-isodisomy case. Zebrafish permit rapid testing of ciliary, renal and developmental phenotypes, but their pronephros and skeletal anatomy do not fully reproduce human thoracic dysplasia. (helm2017partialuniparentalisodisomy pages 1-2)

### C. elegans—NCBI Taxon 6239

CRISPR/matched-variant studies of the IFT140 orthologue **ift-140/che-11** showed that selected variants reproduce short cilia, IFT accumulation, membrane-protein mislocalization and inappropriate entry of nonciliary proteins. This is useful for functional variant interpretation, but the worm cannot model human ribs, lungs, kidneys or retina directly.

### Human cellular and organoid models

Patient fibroblasts and urine-derived renal epithelial cells directly demonstrate ciliary abnormalities; engineered Ift140-null rescue systems can compare wild-type and mutant constructs. Patient-iPSC-derived kidney organoids model renal epithelial cilia and are promising for functional validation and drug screening. Their limitations include fetal-like maturation, incomplete collecting-duct/vascular/immune representation and absence of whole-body thoracic-retinal interactions.

## Recent developments and expert interpretation

1. **2023—structural-variant-aware diagnosis:** Sharova et al. showed that WGS or targeted breakpoint assays may be necessary after panel/WES detects only one IFT140 allele. Published 28 July 2023; DOI: https://doi.org/10.3390/genes14081553. (sharova2023rareift140associatedphenotype pages 1-2, sharova2023rareift140associatedphenotype pages 5-7)
2. **2023—thoracic-insufficiency genomics:** WES in 42 children with thoracic insufficiency yielded a molecular diagnosis in 24/42 (57%); 18/24 were definitive. Ciliary genes were prominent, and IFT140 was found in one proband. This supports broad sequencing for phenotypically overlapping thoracic disorders, but the percentages are not SRTD9-specific.
3. **2023—functional variant modeling:** C. elegans matched-variant work provided scalable experimental support for selected IFT140 alleles, addressing the persistent VUS bottleneck.
4. **2024—prenatal expansion:** Margiotti et al. reported compound-heterozygous p.Ser580dup/p.Gly522Glu in a fetus with severe long-bone and additional anomalies, reinforcing exome-based prenatal diagnosis while broadening—not redefining—the phenotype. Published November 2024; DOI: https://doi.org/10.3390/diagnostics14222601. (margiotti2024compoundheterozygousvariants pages 3-4)
5. **2024—renal diagnostic caution:** The 20-month-old MSS case initially labeled Alport syndrome illustrates the real-world value of molecular diagnosis when biopsy and nonspecific renal findings are misleading.
6. **Current expert view:** IFT140 disease is an allelic and phenotypic continuum. A molecularly anchored label plus explicit organ-level annotation is more informative than forcing every patient into one historical syndrome. Structural-variant analysis and functional testing should be considered whenever phenotype–genotype concordance is strong but routine sequencing is incomplete. (sharova2023rareift140associatedphenotype pages 1-2, walczaksztulpa2022identicalift140variants pages 1-2)

## Evidence limitations

The disease literature lacks population-based registries, prospective natural-history cohorts, standardized phenotype-frequency tables, patient-reported outcome studies and interventional trials. Much mechanistic detail is extrapolated from Ift140-deficient animals, other IFT-A disorders or general renal/retinal ciliopathy biology. Accordingly, exact percentages should be stored only when tied to a named cohort, and evidence from monoallelic IFT140-associated ADPKD must not be merged with biallelic SRTD9. The strongest actionable conclusions are the biallelic IFT140 etiology, marked variable expressivity, need for deletion/duplication or WGS analysis when a second allele is missing, and the importance of lifelong renal, retinal, respiratory and skeletal surveillance. (OpenTargets Search: Short-rib thoracic dysplasia 9 with or without polydactyly-IFT140, sharova2023rareift140associatedphenotype pages 1-2, senum2022monoallelicift140pathogenic pages 1-4, walczaksztulpa2022identicalift140variants pages 1-2)

References

1. (sharova2023rareift140associatedphenotype pages 1-2): Margarita Sharova, Tatyana Markova, Maria Sumina, Marina Petukhova, Maria Bulakh, Oxana Ryzhkova, Tatyana Nagornova, Sofya Ionova, Andrey Marakhonov, Elena Dadali, and Sergey Kutsev. Rare ift140-associated phenotype of cranioectodermal dysplasia and features of diagnostic journey in patients with suspected ciliopathies. Genes, 14:1553, Jul 2023. URL: https://doi.org/10.3390/genes14081553, doi:10.3390/genes14081553. This article has 8 citations.

2. (perrault2012mainzersaldinosyndromeisa pages 1-1): I. Perrault, S. Saunier, S. Hanein, E. Filhol, A. Bizet, F. Collins, M. Salih, E. Silva, V. Baudouin, M. Oud, N. Shannon, M. le Merrer, C. Pietrement, P. Beales, H. Arts, A. Munnich, J. Kaplan, C. Antignac, V. Cormier Daire, and J. Rozet. Mainzer-saldino syndrome is a ciliopathy caused by mutations in the ift140 gene. Cilia, 1:O28-O28, Nov 2012. URL: https://doi.org/10.1186/2046-2530-1-s1-o28, doi:10.1186/2046-2530-1-s1-o28. This article has 4 citations.

3. (sharova2023rareift140associatedphenotype pages 5-7): Margarita Sharova, Tatyana Markova, Maria Sumina, Marina Petukhova, Maria Bulakh, Oxana Ryzhkova, Tatyana Nagornova, Sofya Ionova, Andrey Marakhonov, Elena Dadali, and Sergey Kutsev. Rare ift140-associated phenotype of cranioectodermal dysplasia and features of diagnostic journey in patients with suspected ciliopathies. Genes, 14:1553, Jul 2023. URL: https://doi.org/10.3390/genes14081553, doi:10.3390/genes14081553. This article has 8 citations.

4. (margiotti2024compoundheterozygousvariants pages 3-4): Katia Margiotti, Marco Fabiani, Antonella Cima, Antonella Viola, Francesca Monaco, Chiara Alì, Costanza Zangheri, Carmela Abramo, Claudio Coco, Alvaro Mesoraca, and Claudio Giorlandino. Compound heterozygous variants in the ift140 gene associated with skeletal ciliopathies. Nov 2024. URL: https://doi.org/10.3390/diagnostics14222601, doi:10.3390/diagnostics14222601. This article has 4 citations.

5. (OpenTargets Search: Short-rib thoracic dysplasia 9 with or without polydactyly-IFT140): Open Targets Query (Short-rib thoracic dysplasia 9 with or without polydactyly-IFT140, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (walczaksztulpa2022identicalift140variants pages 1-2): Joanna Walczak-Sztulpa, Anna Wawrocka, Cenna Doornbos, Ronald van Beek, Anna Sowińska-Seidler, Aleksander Jamsheer, Ewelina Bukowska-Olech, Anna Latos-Bieleńska, Ryszard Grenda, Ernie M. H. F. Bongers, Miriam Schmidts, Ewa Obersztyn, Maciej R. Krawczyński, and Machteld M. Oud. Identical ift140 variants cause variable skeletal ciliopathy phenotypes—challenges for the accurate diagnosis. Frontiers in Genetics, Jul 2022. URL: https://doi.org/10.3389/fgene.2022.931822, doi:10.3389/fgene.2022.931822. This article has 15 citations and is from a peer-reviewed journal.

7. (helm2017partialuniparentalisodisomy pages 1-2): Benjamin M. Helm, Jason R. Willer, Azita Sadeghpour, Christelle Golzio, Eric Crouch, Samantha Schrier Vergano, Nicholas Katsanis, and Erica E. Davis. Partial uniparental isodisomy of chromosome 16 unmasks a deleterious biallelic mutation in ift140 that causes mainzer-saldino syndrome. Human Genomics, Jul 2017. URL: https://doi.org/10.1186/s40246-017-0111-9, doi:10.1186/s40246-017-0111-9. This article has 31 citations and is from a peer-reviewed journal.

8. (senum2022monoallelicift140pathogenic pages 1-4): Sarah R. Senum, Ying (Sabrina) M. Li, Katherine A. Benson, Giancarlo Joli, Eric Olinger, Sravanthi Lavu, Charles D. Madsen, Adriana V. Gregory, Ruxandra Neatu, Timothy L. Kline, Marie-Pierre Audrézet, Patricia Outeda, Cherie B. Nau, Esther Meijer, Hamad Ali, Theodore I. Steinman, Michal Mrug, Paul J. Phelan, Terry J. Watnick, Dorien J.M. Peters, Albert C.M. Ong, Peter J. Conlon, Ronald D. Perrone, Emilie Cornec-Le Gall, Marie C. Hogan, Vicente E. Torres, John A. Sayer, and Peter C. Harris. Monoallelic ift140 pathogenic variants are an important cause of the autosomal dominant polycystic kidney-spectrum phenotype. Jan 2022. URL: https://doi.org/10.1016/j.ajhg.2021.11.016, doi:10.1016/j.ajhg.2021.11.016. This article has 194 citations.

9. (senum2022monoallelicift140pathogenic pages 7-10): Sarah R. Senum, Ying (Sabrina) M. Li, Katherine A. Benson, Giancarlo Joli, Eric Olinger, Sravanthi Lavu, Charles D. Madsen, Adriana V. Gregory, Ruxandra Neatu, Timothy L. Kline, Marie-Pierre Audrézet, Patricia Outeda, Cherie B. Nau, Esther Meijer, Hamad Ali, Theodore I. Steinman, Michal Mrug, Paul J. Phelan, Terry J. Watnick, Dorien J.M. Peters, Albert C.M. Ong, Peter J. Conlon, Ronald D. Perrone, Emilie Cornec-Le Gall, Marie C. Hogan, Vicente E. Torres, John A. Sayer, and Peter C. Harris. Monoallelic ift140 pathogenic variants are an important cause of the autosomal dominant polycystic kidney-spectrum phenotype. Jan 2022. URL: https://doi.org/10.1016/j.ajhg.2021.11.016, doi:10.1016/j.ajhg.2021.11.016. This article has 194 citations.

10. (senum2022monoallelicift140pathogenic pages 15-17): Sarah R. Senum, Ying (Sabrina) M. Li, Katherine A. Benson, Giancarlo Joli, Eric Olinger, Sravanthi Lavu, Charles D. Madsen, Adriana V. Gregory, Ruxandra Neatu, Timothy L. Kline, Marie-Pierre Audrézet, Patricia Outeda, Cherie B. Nau, Esther Meijer, Hamad Ali, Theodore I. Steinman, Michal Mrug, Paul J. Phelan, Terry J. Watnick, Dorien J.M. Peters, Albert C.M. Ong, Peter J. Conlon, Ronald D. Perrone, Emilie Cornec-Le Gall, Marie C. Hogan, Vicente E. Torres, John A. Sayer, and Peter C. Harris. Monoallelic ift140 pathogenic variants are an important cause of the autosomal dominant polycystic kidney-spectrum phenotype. Jan 2022. URL: https://doi.org/10.1016/j.ajhg.2021.11.016, doi:10.1016/j.ajhg.2021.11.016. This article has 194 citations.

11. (walczaksztulpa2020compoundheterozygousift140 pages 10-10): Joanna Walczak-Sztulpa, Renata Posmyk, Ewelina M. Bukowska-Olech, Anna Wawrocka, Aleksander Jamsheer, Machteld M. Oud, Miriam Schmidts, Heleen H. Arts, Anna Latos-Bielenska, and Anna Wasilewska. Compound heterozygous ift140 variants in two polish families with sensenbrenner syndrome and early onset end-stage renal disease. Orphanet Journal of Rare Diseases, Feb 2020. URL: https://doi.org/10.1186/s13023-020-1303-2, doi:10.1186/s13023-020-1303-2. This article has 27 citations and is from a peer-reviewed journal.

12. (sharova2023rareift140associatedphenotype pages 8-9): Margarita Sharova, Tatyana Markova, Maria Sumina, Marina Petukhova, Maria Bulakh, Oxana Ryzhkova, Tatyana Nagornova, Sofya Ionova, Andrey Marakhonov, Elena Dadali, and Sergey Kutsev. Rare ift140-associated phenotype of cranioectodermal dysplasia and features of diagnostic journey in patients with suspected ciliopathies. Genes, 14:1553, Jul 2023. URL: https://doi.org/10.3390/genes14081553, doi:10.3390/genes14081553. This article has 8 citations.

13. (cristalli2025clinicalrelevanceof pages 8-9): Carlotta Pia Cristalli, Sara Calabrese, Luca Caramanna, Andrea Pietra, Giulia Vitetta, Bianca De Nicolo, Elena Bonora, Giulia Severi, Soara Menabò, Simona Ferrari, Francesca Ciurli, Valeria Aiello, Irene Capelli, Andrea Pasini, Irene Alberici, Roberto Pillon, Claudio La Scola, Cesare Rossi, Francesca Montanari, and Claudio Graziano. Clinical relevance of ift140 loss-of-function variants in development of renal cysts. Genes, 16:472, Apr 2025. URL: https://doi.org/10.3390/genes16050472, doi:10.3390/genes16050472. This article has 0 citations.

14. (cristalli2025clinicalrelevanceof pages 4-5): Carlotta Pia Cristalli, Sara Calabrese, Luca Caramanna, Andrea Pietra, Giulia Vitetta, Bianca De Nicolo, Elena Bonora, Giulia Severi, Soara Menabò, Simona Ferrari, Francesca Ciurli, Valeria Aiello, Irene Capelli, Andrea Pasini, Irene Alberici, Roberto Pillon, Claudio La Scola, Cesare Rossi, Francesca Montanari, and Claudio Graziano. Clinical relevance of ift140 loss-of-function variants in development of renal cysts. Genes, 16:472, Apr 2025. URL: https://doi.org/10.3390/genes16050472, doi:10.3390/genes16050472. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Short-Rib_Thoracic_Dysplasia_9_With_Or_Without_Polydactyly-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 76 |
| Resolved | 71 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Taxon`.

71 of 76 terms resolved to a current term; the rest could not be looked up either way.