---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T23:24:15.331616'
end_time: '2026-09-03T23:31:48.778441'
duration_seconds: 453.45
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Perisylvian Polymicrogyria with Cerebellar Hypoplasia and Arthrogryposis
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
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 11
  verified: 11
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Polymicrogyria_Perisylvian_With_Cerebellar_Hypoplasia_And_Arthrogryposis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Perisylvian Polymicrogyria with Cerebellar Hypoplasia and Arthrogryposis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Perisylvian Polymicrogyria with Cerebellar Hypoplasia and Arthrogryposis** covering all of the
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
- **Disease Name:** Perisylvian Polymicrogyria with Cerebellar Hypoplasia and Arthrogryposis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Perisylvian Polymicrogyria with Cerebellar Hypoplasia and Arthrogryposis** covering all of the
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


# Research report: Perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis

## Executive summary and evidence limits

This is an **ultra-rare, congenital, autosomal-recessive PI4KA disorder** defined by bilateral perisylvian polymicrogyria (PMG), cerebellar hypoplasia/dysplasia, and fetal arthrogryposis. The defining evidence is unusually narrow: the original 2015 report described **three affected female fetuses from one family**, all carrying the same compound-heterozygous PI4KA variants. Later studies established a broader and clinically heterogeneous PI4KA-related disorder spectrum, but most such patients do **not** necessarily have the complete named triad. Consequently, the original family’s 3/3 frequencies must not be interpreted as population penetrance estimates. (pagnamenta2015germlinerecessivemutations pages 1-2, pagnamenta2015germlinerecessivemutations pages 2-4, verdura2021biallelicpi4kavariants pages 1-2)

No disease-specific publication from 2023–2024 materially expanded the narrowly defined syndrome in the retrieved literature. The most important later evidence is the 2021 PI4KA cohort and a 2022 expert PI4KA-related-disorder review. No relevant disease-specific interventional trial was identified.

| Domain | Best-supported finding | Evidence scope/strength | Key identifiers or quantitative details |
|---|---|---|---|
| Entity and gene | A severe congenital Mendelian disorder caused by biallelic **PI4KA** variants and defined by perisylvian polymicrogyria, cerebellar hypoplasia, and arthrogryposis. | Curated disease–gene association plus primary human familial evidence. (pagnamenta2015germlinerecessivemutations pages 1-2, OpenTargets Search: perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis-PI4KA) | **OMIM 616531**; **MONDO:0014679**; PI4KA/ENSG00000241973; PMID **25855803**. |
| Original cohort | Three affected female fetuses occurred in one nonconsanguineous European-ancestry family; three additional early miscarriages were reported. | Single-family case series; strong segregation but very small ascertainment base. (pagnamenta2015germlinerecessivemutations pages 2-4, pagnamenta2015germlinerecessivemutations pages 1-2) | Pregnancy terminations at **34, 28, and 16 gestational weeks**. |
| Causal variants | All three fetuses were compound heterozygous for a paternal stop-gain and maternal catalytic-domain missense variant. | Segregation confirmed by Sanger sequencing; missense effect supported experimentally. (pagnamenta2015germlinerecessivemutations pages 1-2, pagnamenta2015germlinerecessivemutations pages 4-6, pagnamenta2015germlinerecessivemutations pages 2-4) | **NM_058004.3:c.2386C>T, p.(Arg796Ter)** and **c.5560G>A, p.(Asp1854Asn)**; germline, autosomal recessive. |
| Cardinal brain phenotype | Bilateral perisylvian polymicrogyria and cerebellar hypoplasia/dysplasia were present in all three reported fetuses. | Prenatal MRI and fetal neuropathology; **3/3**, but frequencies are family-specific rather than population estimates. (pagnamenta2015germlinerecessivemutations pages 2-4) | PMG **3/3 (100%)**; cerebellar hypoplasia/dysplasia **3/3 (100%)**; abnormal vermis/dentate nuclei also described. |
| Cardinal musculoskeletal phenotype | Congenital arthrogryposis/joint contractures with bilateral talipes equinovarus and externally rotated hips occurred in all three fetuses. | Direct fetal examination/pathology; **3/3** in the original family. (pagnamenta2015germlinerecessivemutations pages 2-4) | Arthrogryposis/contractures **3/3 (100%)**; bilateral talipes equinovarus **3/3 (100%)**; flexed knees and wrist contracture varied. |
| Other congenital findings | Micrognathia was consistent; variable findings included dolichocephaly, ventriculomegaly, small pons, dysplastic olivary nuclei, renal pelviectasis, and mild/borderline pulmonary hypoplasia. | Patient-level fetal observations; frequencies generally limited to the three-family cohort. (pagnamenta2015germlinerecessivemutations pages 2-4) | Micrognathia **3/3 (100%)**; normal muscle histology argues against a primary myopathy in this family. (pagnamenta2015germlinerecessivemutations pages 2-4) |
| Inheritance and recurrence | The disorder follows autosomal-recessive inheritance; heterozygous carriers are considered asymptomatic. | Strong intrafamilial segregation and broader PI4KA disease curation. (baple2022pi4karelateddisorder pages 1-3, baple2022pi4karelateddisorder pages 11-14) | If both parents are carriers: **25% affected, 50% carrier, 25% neither variant** per pregnancy. |
| Biochemical mechanism | PI4KA/PI4KIIIα generates plasma-membrane phosphatidylinositol-4-phosphate needed to sustain PI(4,5)P₂ and downstream membrane signaling. p.Asp1854Asn abolishes detectable catalytic activity in vitro. | Direct COS-7 biochemical assay for p.Asp1854Asn; downstream developmental chain remains inferred. (pagnamenta2015germlinerecessivemutations pages 4-6, pagnamenta2015germlinerecessivemutations pages 7-8, pagnamenta2015germlinerecessivemutations pages 6-7) | Mutant and wild-type protein abundance was comparable in the assay; activity of p.Asp1854Asn was indistinguishable from negative controls. p.Arg796Ter protein function was not directly tested. |
| Broader PI4KA spectrum | Other biallelic PI4KA genotypes produce a continuum from severe developmental encephalopathy, hypomyelination, structural brain abnormalities, immune/GI disease, and contractures to pure hereditary spastic paraplegia. | Ten-patient multicenter cohort plus later case reports; informative for gene-level disease but not equivalent to the narrowly defined 616531 phenotype. (verdura2021biallelicpi4kavariants pages 4-4, verdura2021biallelicpi4kavariants pages 7-9, verdura2021biallelicpi4kavariants pages 1-2) | In the 2021 cohort, **10 unrelated patients** were reported; one additional p.Asp1854Asn-homozygous patient had bilateral perisylvian PMG. |
| Diagnosis | Diagnosis rests on compatible prenatal/postnatal neuroimaging and contractures plus identification of biallelic pathogenic/likely pathogenic PI4KA variants with parental segregation. | Expert disease review supported by primary exome-sequencing discovery. (pagnamenta2015germlinerecessivemutations pages 1-2, baple2022pi4karelateddisorder pages 1-3) | Fetal ultrasound/MRI; postnatal brain MRI when applicable; multigene panel, WES, or WGS with CNV analysis. PI4KAP1/PI4KAP2 pseudogenes require assay-specific validation. A VUS alone is not diagnostic. |
| Treatment and trials | No disease-modifying therapy is established; management is manifestation-directed and multidisciplinary. No relevant interventional trial was identified in the retrieved ClinicalTrials.gov search. | Expert management recommendations extrapolated from the broader PI4KA spectrum; no syndrome-specific treatment trial or response-rate evidence. (baple2022pi4karelateddisorder pages 1-3, baple2022pi4karelateddisorder pages 10-11) | PT/OT, mobility and communication aids, standard antiseizure therapy, spasticity treatment, feeding support/gastrostomy, and indicated GI, immune, hearing, and vision care. Leflunomide remains investigational. |
| Epidemiology and prognosis gaps | Population prevalence, incidence, penetrance, sex ratio, survival, life expectancy, quality-of-life scores, and prognostic biomarkers have not been established for the specific syndrome. | Evidence is inadequate because the defining report comprised only three terminated pregnancies in one family. (pagnamenta2015germlinerecessivemutations pages 2-4, pagnamenta2015germlinerecessivemutations pages 1-2) | The observed **3/3** phenotype frequencies must not be interpreted as general-population penetrance estimates; no live-born natural-history cohort exists for the narrowly defined disorder. |


*Table: Knowledge-base summary of the defining PI4KA-associated fetal syndrome, separating direct evidence from the original family from findings across the broader PI4KA-related disorder spectrum. It highlights quantitative observations and major diagnostic, therapeutic, epidemiologic, and prognostic gaps.*

---

## 1. Disease information

### Definition

Perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis is a prenatal-onset malformation syndrome caused by biallelic pathogenic PI4KA variants. PMG is a malformation of cortical development characterized by excessive small gyri and abnormal cortical organization/lamination; in this syndrome it predominantly involves the cortex surrounding both Sylvian fissures. Cerebellar underdevelopment/dysplasia and congenital joint contractures complete the defining phenotype. (pagnamenta2015germlinerecessivemutations pages 1-2, pagnamenta2015germlinerecessivemutations pages 2-4)

### Identifiers and synonyms

- **MONDO:** MONDO:0014679.
- **OMIM phenotype:** 616531.
- **Causal target:** PI4KA, phosphatidylinositol 4-kinase alpha; Ensembl ENSG00000241973.
- **Common name:** *Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis*.
- **Useful alternative:** *PI4KA-related perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis*.
- **Broader umbrella term:** *PI4KA-related disorder*; this includes hypomyelinating leukodystrophy, gastrointestinal/immunologic disease, and hereditary spastic paraplegia and is not synonymous with the complete fetal triad. (baple2022pi4karelateddisorder pages 1-3, OpenTargets Search: perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis-PI4KA, verdura2021biallelicpi4kavariants pages 1-2)
- **ICD-10/ICD-11 and MeSH:** no unique disease-specific code or descriptor was established in the retrieved sources. Coding ordinarily requires broader congenital brain-malformation, arthrogryposis, and genetic-disease categories.
- **Orphanet:** no confidently verified disease-specific identifier was recovered.

The evidence is **aggregated disease-level literature derived from individual family/patient observations**, not an EHR-derived cohort or population registry.

### Foundational reference

Pagnamenta et al., *Human Molecular Genetics*, published online **8 April 2015**, DOI: [10.1093/hmg/ddv117](https://doi.org/10.1093/hmg/ddv117), **PMID 25855803**. Its abstract states: “exome sequencing in a family where three fetuses had all been diagnosed with PMG and cerebellar hypoplasia” identified compound-heterozygous PI4KA variants, and concludes that the findings “emphasize the importance of phosphoinositide signalling in early brain development.” (pagnamenta2015germlinerecessivemutations pages 1-2, OpenTargets Search: perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis-PI4KA)

---

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The established initiating cause is **germline biallelic PI4KA dysfunction**. In the defining family, the paternal allele was NM_058004.3:c.2386C>T, p.(Arg796Ter), and the maternal allele was c.5560G>A, p.(Asp1854Asn). Both were present in all three affected fetuses and segregated under an autosomal-recessive model. (pagnamenta2015germlinerecessivemutations pages 1-2, pagnamenta2015germlinerecessivemutations pages 2-4)

### Risk factors

- **Genetic:** two pathogenic or likely pathogenic PI4KA alleles in trans are the principal risk factor. A prior affected pregnancy and parental carrier status create a 25% recurrence probability in each pregnancy.
- **Family history/consanguinity:** the original parents were unrelated and of European ancestry; consanguinity is therefore not required. (pagnamenta2015germlinerecessivemutations pages 1-2, baple2022pi4karelateddisorder pages 11-14)
- **Environmental, lifestyle, occupational, infectious, age, or sex risks:** none are established for the named syndrome. All three defining fetuses were female, but the sample is too small and family-specific to imply sex limitation. General reports that diet can modulate PI4KA expression or that PI4KA participates in hepatitis C biology do not demonstrate disease risk or G×E interaction. (pagnamenta2015germlinerecessivemutations pages 2-4, zhang2022asynonymousmutation pages 8-10)

### Protective factors

No genetic protective alleles, modifier variants, diets, medications, or environmental exposures have been demonstrated. Heterozygous carriers are considered clinically unaffected, but carrier state should not be described as a “protective factor.” (baple2022pi4karelateddisorder pages 11-14)

### Gene–environment interaction

No syndrome-specific G×E interaction has been demonstrated. The developmental phenotype appears primarily determined by severe inherited PI4KA dysfunction; variable residual enzyme activity and protein-complex interactions are more plausible modifiers than documented environmental exposures.

---

## 3. Phenotypes

Frequencies below refer only to the original three fetuses and are therefore **observed family frequencies**, not robust disease-wide estimates.

| Phenotype | Type, onset, observed frequency and course | Suggested HPO term |
|---|---|---|
| Bilateral perisylvian PMG | Congenital structural CNS malformation; 3/3; fixed developmental lesion | Polymicrogyria, HP:0002126; bilateral perisylvian PMG where available |
| Cerebellar hypoplasia/dysplasia | Congenital imaging/pathology sign; 3/3; fixed | Cerebellar hypoplasia, HP:0001321 |
| Arthrogryposis/joint contractures | Congenital physical manifestation; 3/3 | Arthrogryposis multiplex congenita, HP:0002804; congenital joint contracture |
| Bilateral talipes equinovarus | Congenital limb deformity; 3/3 | Talipes equinovarus, HP:0001762 |
| Externally rotated hips | Congenital postural/deformation finding; 3/3 | Abnormality of the hip joint/position |
| Micrognathia | Craniofacial sign; 3/3 | Micrognathia, HP:0000347 |
| Flexed knees | Contracture; present in II-2 and II-3, 2/3 | Knee flexion contracture |
| Wrist contracture | Contracture; left wrist in II-3, 1/3 | Wrist flexion contracture |
| Dolichocephaly | Cranial shape; II-2 and II-3, 2/3 | Dolichocephaly, HP:0000268 |
| Small pons/brainstem abnormality | Congenital neuropathologic sign; variably reported | Pontine hypoplasia |
| Ventriculomegaly | Prenatal imaging sign; variable | Ventriculomegaly, HP:0002119 |
| Dysplastic dentate nuclei | Neuropathologic manifestation | Abnormal cerebellar morphology |
| Dysplastic olivary nuclei | Neuropathologic manifestation in II-3 | Abnormality of the inferior olivary nucleus |
| Renal pelviectasis | Congenital renal imaging finding; variable | Pyelectasis/hydronephrosis |
| Mild/borderline lung hypoplasia | Congenital secondary/deformation finding; variable | Pulmonary hypoplasia, HP:0002089 |

Prenatal MRI showed bilateral perisylvian PMG and a small cerebellum; II-2 also had delayed sulcation. Neuropathology documented abnormal vermis, dentate nuclei, and, in II-3, olivary nuclei. Muscle histology was normal, favoring fetal akinesia secondary to neurologic dysfunction rather than a demonstrated primary myopathy. (pagnamenta2015germlinerecessivemutations pages 2-4)

The broader PI4KA spectrum can include developmental delay/intellectual disability, absent or poor speech, seizures, axial hypotonia, peripheral spasticity/hyperreflexia, ataxia, dystonia, nystagmus, feeding difficulty, hypomyelination, thin corpus callosum, cerebral/cerebellar atrophy, intestinal disease, and immune defects. These should be attached to the umbrella PI4KA-related disorder, not automatically asserted in every patient with the named fetal syndrome. (baple2022pi4karelateddisorder pages 1-3, zhang2022asynonymousmutation pages 1-2, verdura2021biallelicpi4kavariants pages 1-2)

### Functional and quality-of-life impact

No EQ-5D, SF-36, PROMIS, caregiver-burden, or disease-specific quality-of-life study exists. The defining pregnancies were terminated at 34, 28, and 16 weeks, so live-born developmental function cannot be estimated from the original family. In surviving patients elsewhere in the PI4KA spectrum, severe motor, communication, feeding, seizure, and spasticity phenotypes can substantially impair independence, but that is gene-spectrum rather than triad-specific evidence. (pagnamenta2015germlinerecessivemutations pages 2-4, baple2022pi4karelateddisorder pages 1-3)

---

## 4. Genetic and molecular information

### Causal gene

**PI4KA** encodes the approximately 240-kDa phosphatidylinositol 4-kinase IIIα (PI4KIIIα), highly expressed in brain and placenta and functioning with regulatory partners including TTC7A/TTC7B, FAM126/HYCC1, and EFR3 at membranes. (pagnamenta2015germlinerecessivemutations pages 6-7, zhang2022asynonymousmutation pages 2-4)

### Defining variants

1. **c.2386C>T, p.(Arg796Ter)** — paternal, exon 20 stop-gain, germline. It predicts premature truncation. The transcript was detectable in adult parental blood without substantial nonsense-mediated decay, but truncated-protein production, stability, localization, and catalytic function were not directly tested. (pagnamenta2015germlinerecessivemutations pages 4-6, pagnamenta2015germlinerecessivemutations pages 2-4)
2. **c.5560G>A, p.(Asp1854Asn)** — maternal, exon 48 missense variant at a highly conserved catalytic-domain residue. Structural modeling places Asp1854 as important to ATP-binding-pocket folding. Expressed mutant protein had **no measurable kinase activity** despite abundance comparable with wild type. (pagnamenta2015germlinerecessivemutations pages 4-6, pagnamenta2015germlinerecessivemutations pages 7-8)

The original report predated current routine ACMG/AMP deposition practices in the evidence retrieved. The segregation, rarity, predicted truncation, conservation, and functional assay strongly support pathogenicity, but database-level ClinVar review status and current gnomAD counts should be checked directly before assigning a contemporary laboratory classification.

### Additional molecular findings

Two later Turkish individuals were described as homozygous for p.Asp1854Asn; at least one had bilateral perisylvian PMG, strengthening recurrence of the cortical phenotype. A 2021 study of 10 unrelated patients found eight compound heterozygotes and two homozygotes and suggested that surviving patients often retain residual PI4KA function—no patient carried two unequivocal loss-of-function alleles. (baple2022pi4karelateddisorder pages 6-8, verdura2021biallelicpi4kavariants pages 4-4, verdura2021biallelicpi4kavariants pages 7-9)

No validated disease-specific modifier gene, methylation signature, epigenetic mechanism, recurrent chromosomal abnormality, somatic variant, or genetic anticipation is known. PI4KAP1 and PI4KAP2 are nearby pseudogenes that create an important **technical testing hazard**, not causal loci. (pagnamenta2015germlinerecessivemutations pages 8-9, baple2022pi4karelateddisorder pages 1-3)

---

## 5. Environmental information

No toxin, radiation, pollutant, medication, occupational exposure, smoking, alcohol, diet, exercise pattern, or pathogen has been shown to cause or modify this Mendelian syndrome. Prenatal infection and vascular disruption remain general differentials for PMG, but are not established etiologies in the genetically confirmed PI4KA family. Thus, environmental and infectious annotations should be entered as **not demonstrated**, not “absent by proof.”

---

## 6. Mechanism/pathophysiology

### Ordered causal chain

1. **Biallelic germline PI4KA variants lead to** severe reduction of functional PI4KIIIα; catalytic inactivity is demonstrated for p.Asp1854Asn, whereas the protein-level consequence of p.Arg796Ter is inferred.
2. **Reduced PI4KIIIα activity leads to** deficient conversion of phosphatidylinositol to phosphatidylinositol-4-phosphate [PI(4)P] at the plasma membrane; this step is established PI4KA biochemistry but was not measured in the original fetal tissue.
3. **Reduced PI(4)P leads to** impaired maintenance of plasma-membrane PI(4,5)P₂ and altered membrane trafficking/signaling; inferred for the defining fetuses.
4. **Altered phosphoinositide pools lead to** disturbed PLC–IP3–Ca²⁺ and PI3K–AKT–mTOR-linked signaling and membrane organization during neurodevelopment; biologically plausible but not directly demonstrated in fetal cortex. (pagnamenta2015germlinerecessivemutations pages 4-6, pagnamenta2015germlinerecessivemutations pages 6-7)
5. **Developmental signaling/membrane defects lead to** abnormal cortical organization/migration and cerebellar/brainstem morphogenesis; inferred from phenotype and broader patient-cell evidence.
6. **Abnormal cerebral, cerebellar, and motor-system development branches into:**
   - **cortical disorganization →** bilateral perisylvian PMG;
   - **hindbrain developmental impairment →** vermian/cerebellar hypoplasia and dysplastic dentate/olivary nuclei;
   - **reduced fetal motor output →** fetal akinesia, joint contractures, talipes, and arthrogryposis; this last link is inferred, supported by normal fetal muscle histology. (pagnamenta2015germlinerecessivemutations pages 2-4)

### Direct versus inferred evidence

**Direct human biochemical evidence:** HA-tagged wild-type and p.Asp1854Asn PI4KA were expressed in COS-7 cells, immunoprecipitated, and tested with ATP and phosphatidylinositol in an ADP-GLO assay. Mutant activity was indistinguishable from negative controls while Western blotting showed comparable protein recovery. (pagnamenta2015germlinerecessivemutations pages 4-6, pagnamenta2015germlinerecessivemutations pages 7-8)

**Direct broader-spectrum cellular evidence:** fibroblasts and peripheral-blood mononuclear cells from patients with other biallelic PI4KA genotypes showed reduced protein, reduced PI4KA activity, and altered PI/PIP/PIP₂ measurements. (verdura2021biallelicpi4kavariants pages 7-9, verdura2021biallelicpi4kavariants pages 1-2)

**Not demonstrated:** fetal single-cell or spatial transcriptomics, proteomics, metabolomics, lipidomics of affected brain, CRISPR screens, immune activation, oxidative injury, apoptosis, autophagy, or a disease-specific epigenetic signature.

### Suggested mechanistic ontology annotations

- **GO biological process:** phosphatidylinositol phosphorylation; phosphoinositide-mediated signaling; regulation of plasma-membrane organization; nervous-system development; cerebral-cortex development; cerebellum development; neuron migration; myelination—the latter is broader-spectrum evidence.
- **GO molecular function:** phosphatidylinositol 4-kinase activity (GO:0004430); ATP binding.
- **GO cellular component:** plasma membrane (GO:0005886); PI4KIIIα membrane-associated complex.
- **Candidate cell types (CL):** neural progenitor cell, radial glial cell, migrating neuron, cortical neuron, cerebellar granule-neuron precursor, Purkinje cell, oligodendrocyte, skeletal-muscle cell. The first five are mechanistically plausible targets; direct cell-type-specific fetal data are unavailable.
- **Chemical entities:** phosphatidylinositol, PI(4)P, PI(4,5)P₂, ATP, ADP, and Ca²⁺; CHEBI identifiers should be validated against the release used by the knowledge base.

---

## 7. Anatomical structures affected

### Organ/system level

The primary system is the **central nervous system**, particularly bilateral perisylvian cerebral cortex, cerebellum/vermis, dentate nuclei, pons, and inferior olivary nuclei. The musculoskeletal system is secondarily affected through congenital contractures, feet, knees, wrists, fingers, and hip posture. Variable renal-pelvis and pulmonary findings occurred. (pagnamenta2015germlinerecessivemutations pages 2-4)

Suggested UBERON concepts include cerebral cortex, Sylvian fissure/perisylvian region, cerebellum, cerebellar vermis, dentate nucleus, pons, medulla oblongata/inferior olivary nucleus, skeletal muscle, hip joint, knee joint, wrist joint, and foot. No consistent lateralization was described for PMG—it was bilateral—although individual limb contractures could be asymmetric.

### Tissue/cell/subcellular level

Affected tissue is principally developing nervous tissue and cortical/cerebellar architecture. Normal muscle histology provides no evidence for primary muscle degeneration. The implicated subcellular site is the plasma membrane and its phosphoinositide lipid pool; direct ultrastructural fetal data are lacking. (pagnamenta2015germlinerecessivemutations pages 6-7, pagnamenta2015germlinerecessivemutations pages 2-4)

---

## 8. Temporal development

The disorder begins **antenatally during brain and motor-system development**. PMG may be difficult to recognize before approximately 24 gestational weeks; targeted ultrasound and fetal MRI improve detection, although the third fetus was recognized at 16 weeks through a broader recurrent-malformation pattern. The three pregnancies ended at 34, 28, and 16 weeks. (pagnamenta2015germlinerecessivemutations pages 1-2, pagnamenta2015germlinerecessivemutations pages 2-4)

PMG, cerebellar hypoplasia, and congenital contractures are developmental and structurally fixed rather than relapsing. Progressive cerebellar atrophy, hypomyelination, spasticity, or neurologic decline occurs in some broader PI4KA genotypes, but there is no postnatal natural-history series for the complete fetal triad. No remission pattern or staged disease classification exists. Critical windows are fetal cortical organization, hindbrain development, and fetal movement; no proven therapeutic window has been defined.

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive.
- **Recurrence:** when both parents are carriers, each conception has 25% affected, 50% carrier, and 25% non-carrier probability.
- **Carriers:** generally asymptomatic.
- **Penetrance/expressivity:** penetrance of two severe alleles has not been quantified. Expressivity across all PI4KA disorders is broad, ranging from lethal congenital disease to childhood encephalopathy or later spastic paraplegia. (baple2022pi4karelateddisorder pages 1-3, baple2022pi4karelateddisorder pages 11-14, verdura2021biallelicpi4kavariants pages 1-2)
- **Mosaicism/anticipation:** not reported.
- **Consanguinity:** not required; original parents were unrelated.
- **Founder effect:** a broader PI4KA phenotype has an Amish p.Tyr1623Asp founder allele reported at frequency 0.0006, but this is not the defining p.Arg796Ter/p.Asp1854Asn genotype and should not be assigned specifically to OMIM 616531. (baple2022pi4karelateddisorder pages 11-14)
- **Prevalence/incidence/carrier frequency:** unknown. No cases-per-100,000 estimate, registry, or population-based incidence exists.
- **Demography:** three defining fetuses were female and European ancestry; no valid sex ratio, ethnic predisposition, or geographic distribution can be inferred. (pagnamenta2015germlinerecessivemutations pages 2-4, pagnamenta2015germlinerecessivemutations pages 1-2)

---

## 10. Diagnostics

### Clinical and imaging workflow

1. Suspect a fetal akinesia/brain-malformation syndrome when prenatal ultrasound shows reduced movement, contractures, talipes, abnormal cortical sulcation, ventriculomegaly, or a small posterior fossa.
2. Perform expert fetal neurosonography and **fetal MRI**, specifically evaluating bilateral perisylvian cortex, sulcation, cerebellar size/vermis, pons, ventricles, and corpus callosum.
3. Document limb contractures and search for pulmonary, renal, gastrointestinal, and growth abnormalities.
4. Obtain chromosomal microarray to identify pathogenic CNVs; a conventional karyotype was normal, 46,XX, in the first fetus.
5. Use trio/family **WES or WGS**, or a comprehensive malformations-of-cortical-development/fetal-akinesia panel including PI4KA. Confirm variants and phase by parental Sanger testing.
6. Ensure assay design distinguishes PI4KA from PI4KAP1/PI4KAP2 pseudogenes. RNA testing or functional kinase studies may help resolve splice variants or strong VUS, but are not routine diagnostic biomarkers. (pagnamenta2015germlinerecessivemutations pages 1-2, pagnamenta2015germlinerecessivemutations pages 8-9, baple2022pi4karelateddisorder pages 1-3)

WGS may add noncoding, structural-variant, and uniform CNV detection; WES was sufficient in the discovery family. Karyotyping/FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line unless another diagnosis is suspected. No enzyme assay, metabolite, liquid biopsy, or validated circulating biomarker exists.

### Diagnostic criterion

A definitive molecular diagnosis requires a compatible phenotype and **biallelic pathogenic/likely pathogenic PI4KA variants**, ideally confirmed in trans. A VUS alone neither establishes nor excludes the diagnosis. (baple2022pi4karelateddisorder pages 1-3)

### Differential diagnosis

Important alternatives include congenital CMV or other prenatal insults; vascular/disruptive PMG; chromosomal CNVs such as 22q11.2 or 1p36 deletion; and monogenic PMG/fetal-akinesia disorders involving tubulin/cytoskeletal, phosphoinositide, ion-pump, or motor-neuron pathways. Specific gene differentials include PIK3CA, PIK3R2, AKT3, WDR62, TUBA1A, TUBB2B, COL4A1/COL4A2, BICD2, GRIN1, ATP1A2/ATP1A3, SMPD4, and ARL6IP1. For hypomyelination or intestinal/immunologic presentations, FAM126A and TTC7A are particularly relevant. (zhang2022asynonymousmutation pages 2-4, verdura2021biallelicpi4kavariants pages 1-2)

### Screening

There is no newborn population screening. In a molecularly confirmed family, targeted carrier/cascade testing, prenatal diagnosis using chorionic-villus or amniotic-fluid DNA, and preimplantation genetic testing are appropriate.

---

## 11. Outcome and prognosis

No live-born natural-history cohort exists for the narrowly defined syndrome. Therefore, survival rate, life expectancy, mortality, recovery probability, disability scale, and prognostic biomarkers are unknown. The original pregnancies were terminated because of severe multiple congenital abnormalities, which indicates serious prenatal morbidity but does not establish inevitable lethality. (pagnamenta2015germlinerecessivemutations pages 2-4, pagnamenta2015germlinerecessivemutations pages 1-2)

Likely morbidity includes profound motor disability, feeding and respiratory risk, epilepsy, communication impairment, and orthopedic complications, based on anatomy and broader PI4KA disease; these are informed projections rather than measured outcomes for the complete triad. Residual PI4KA activity and severity of brainstem, cerebellar, pulmonary, gastrointestinal, and immune involvement are plausible prognostic variables, but none is validated.

---

## 12. Treatment and current applications

There is **no approved disease-modifying, gene, cell, RNA, or PI4KA-targeted therapy**. Real-world implementation is supportive and multidisciplinary:

- PT/OT, stretching, positioning, splinting, mobility equipment, and orthopedic assessment for contractures and talipes.
- Baclofen, diazepam, or botulinum toxin for clinically significant spasticity.
- Standard antiseizure medication chosen by seizure type and EEG.
- Speech-language therapy and augmentative communication.
- Swallow evaluation, nutrition support, reflux treatment, and gastrostomy when necessary.
- Respiratory monitoring where pulmonary hypoplasia, aspiration, or weakness is present.
- Hearing, vision, developmental, neurologic, orthopedic, gastrointestinal, and immunologic follow-up guided by phenotype. (baple2022pi4karelateddisorder pages 1-3, baple2022pi4karelateddisorder pages 10-11)

Suggested NCIT intervention concepts include Physical Therapy, Occupational Therapy, Speech Therapy, Orthopedic Surgery, Gastrostomy, Anticonvulsant Therapy, Baclofen, Diazepam, and Botulinum Toxin Therapy; local NCIT codes should be release-validated.

Management of intestinal atresia, inflammatory bowel disease, or immunodeficiency belongs mainly to the broader PI4KA spectrum. Parenteral nutrition, intestinal surgery/transplant, immunoglobulin replacement, immunosuppression, or HSCT may be considered according to the actual phenotype, but evidence is sparse and intestinal benefit from HSCT is uncertain. Leflunomide remains investigational. (baple2022pi4karelateddisorder pages 10-11, zhang2022asynonymousmutation pages 4-6)

No treatment-response percentage, pharmacogenomic rule, or disease-specific adverse-event dataset is available. No relevant interventional ClinicalTrials.gov study was recovered.

---

## 13. Prevention

Primary lifestyle or environmental prevention is not available because the disorder is inherited and congenital. Effective prevention is reproductive/genetic:

- genetic counseling and parental phase confirmation;
- targeted carrier testing of at-risk relatives;
- prenatal molecular diagnosis after chorionic-villus sampling or amniocentesis;
- preimplantation genetic testing for monogenic disease;
- fetal ultrasound/MRI for early structural assessment. (baple2022pi4karelateddisorder pages 1-3, baple2022pi4karelateddisorder pages 11-14)

Secondary prevention consists of early recognition and planning of neonatal neurologic, respiratory, feeding, orthopedic, and seizure care. Tertiary prevention includes contracture management, aspiration and malnutrition prevention, seizure control, and surveillance for complications. Vaccination, public-health sanitation, environmental remediation, behavioral intervention, and prophylactic medication do not prevent the genetic syndrome.

---

## 14. Other species and natural disease

No naturally occurring veterinary syndrome confidently attributable to orthologous PI4KA variants was identified, and there is no zoonotic or cross-species transmission. The disorder is inherited, not infectious.

Orthologous PI4KA function is evolutionarily conserved. Experimental disruption affects **Mus musculus** (NCBI Taxon 10090), **Danio rerio** (7955), **Drosophila melanogaster** (7227), and **Saccharomyces cerevisiae** (4932). These findings support fundamental biological essentiality but are induced/model phenotypes, not documented natural veterinary disease. (pagnamenta2015germlinerecessivemutations pages 6-7, pagnamenta2015germlinerecessivemutations pages 8-9)

---

## 15. Model organisms and experimental systems

- **Mouse:** conventional Pi4ka knockout reportedly causes early embryonic lethality. Acute pharmacologic inhibition in adults causes cardiovascular-collapse-like death, while inducible whole-body inactivation causes gastrointestinal necrosis before brain consequences can be evaluated. These models demonstrate essentiality but poorly recapitulate the human cortical triad. (pagnamenta2015germlinerecessivemutations pages 6-7, pagnamenta2015germlinerecessivemutations pages 8-9)
- **Zebrafish:** Pi4ka downregulation disrupts brain, heart, trunk, and pectoral-fin development. It provides a developmental vertebrate model but lacks demonstrated faithful bilateral perisylvian PMG, a human gyral phenotype. (pagnamenta2015germlinerecessivemutations pages 6-7)
- **Drosophila/yeast:** orthologue inactivation is lethal; useful for conserved phosphoinositide biology, but anatomically remote from human cortical malformation. (pagnamenta2015germlinerecessivemutations pages 6-7)
- **Cellular systems:** COS-7 expression/immunoprecipitation directly established p.Asp1854Asn catalytic inactivity. Patient fibroblasts and PBMCs from the broader disorder support reduced PI4KA abundance/activity and altered phosphoinositide pools. (pagnamenta2015germlinerecessivemutations pages 4-6, verdura2021biallelicpi4kavariants pages 1-2)
- **Unavailable models:** no reported disease-specific p.Arg796Ter/p.Asp1854Asn knock-in mouse, cerebral organoid, patient-derived iPSC neural model, single-cell atlas, or spatial-transcriptomic model was found.

These models are best applied to PI4KA catalytic function, phosphoinositide homeostasis, membrane trafficking, myelination, and developmental essentiality. A human cortical organoid or conditional neural-lineage knock-in model would be needed to test the inferred sequence from PI(4)P deficiency to cortical dyslamination and fetal motor dysfunction.

---

## Evidence appraisal

The causal gene assignment is strong because the variants segregated recessively in three affected siblings, were the only plausible variants in the shared interval, and p.Asp1854Asn abolished kinase activity. Nevertheless, syndrome-specific phenotype frequencies, prognosis, and management evidence remain weak because all defining cases came from one family and none contributed postnatal natural history. Later PI4KA studies strengthen gene-level causality and reveal a broad allelic spectrum, but they should not be used to inflate evidence for the exact PMG–cerebellar hypoplasia–arthrogryposis triad. (pagnamenta2015germlinerecessivemutations pages 1-2, pagnamenta2015germlinerecessivemutations pages 4-6, verdura2021biallelicpi4kavariants pages 1-2)

References

1. (pagnamenta2015germlinerecessivemutations pages 1-2): Alistair T. Pagnamenta, Malcolm F. Howard, Eva Wisniewski, Niko Popitsch, Samantha J.L. Knight, David A. Keays, Gerardine Quaghebeur, Helen Cox, Phillip Cox, Tamas Balla, Jenny C. Taylor, and Usha Kini. Germline recessive mutations in pi4ka are associated with perisylvian polymicrogyria, cerebellar hypoplasia and arthrogryposis. Human Molecular Genetics, 24:3732-3741, Apr 2015. URL: https://doi.org/10.1093/hmg/ddv117, doi:10.1093/hmg/ddv117. This article has 96 citations and is from a domain leading peer-reviewed journal.

2. (pagnamenta2015germlinerecessivemutations pages 2-4): Alistair T. Pagnamenta, Malcolm F. Howard, Eva Wisniewski, Niko Popitsch, Samantha J.L. Knight, David A. Keays, Gerardine Quaghebeur, Helen Cox, Phillip Cox, Tamas Balla, Jenny C. Taylor, and Usha Kini. Germline recessive mutations in pi4ka are associated with perisylvian polymicrogyria, cerebellar hypoplasia and arthrogryposis. Human Molecular Genetics, 24:3732-3741, Apr 2015. URL: https://doi.org/10.1093/hmg/ddv117, doi:10.1093/hmg/ddv117. This article has 96 citations and is from a domain leading peer-reviewed journal.

3. (verdura2021biallelicpi4kavariants pages 1-2): Edgard Verdura, Agustí Rodríguez-Palmero, Valentina Vélez-Santamaria, Laura Planas-Serra, Irene de la Calle, Miquel Raspall-Chaure, Agathe Roubertie, Mehdi Benkirane, Francesco Saettini, Lisa Pavinato, Giorgia Mandrile, Melanie O’Leary, Emily O’Heir, Estibaliz Barredo, Almudena Chacón, Vincent Michaud, Cyril Goizet, Montserrat Ruiz, Agatha Schlüter, Isabelle Rouvet, Julia Sala-Coromina, Chiara Fossati, Maria Iascone, Francesco Canonico, Anna Marcé-Grau, Precilla de Souza, David R Adams, Carlos Casasnovas, Heidi L Rehm, Heather C Mefford, Luis González Gutierrez-Solana, Alfredo Brusco, Michel Koenig, Alfons Macaya, and Aurora Pujol. Biallelic pi4ka variants cause a novel neurodevelopmental syndrome with hypomyelinating leukodystrophy. Brain, 144:2659-2669, Aug 2021. URL: https://doi.org/10.1093/brain/awab124, doi:10.1093/brain/awab124. This article has 67 citations and is from a highest quality peer-reviewed journal.

4. (OpenTargets Search: perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis-PI4KA): Open Targets Query (perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis-PI4KA, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (pagnamenta2015germlinerecessivemutations pages 4-6): Alistair T. Pagnamenta, Malcolm F. Howard, Eva Wisniewski, Niko Popitsch, Samantha J.L. Knight, David A. Keays, Gerardine Quaghebeur, Helen Cox, Phillip Cox, Tamas Balla, Jenny C. Taylor, and Usha Kini. Germline recessive mutations in pi4ka are associated with perisylvian polymicrogyria, cerebellar hypoplasia and arthrogryposis. Human Molecular Genetics, 24:3732-3741, Apr 2015. URL: https://doi.org/10.1093/hmg/ddv117, doi:10.1093/hmg/ddv117. This article has 96 citations and is from a domain leading peer-reviewed journal.

6. (baple2022pi4karelateddisorder pages 1-3): EL Baple, C Salter, H Uhlig, and NI Wolf. Pi4ka-related disorder. Unknown journal, 2022.

7. (baple2022pi4karelateddisorder pages 11-14): EL Baple, C Salter, H Uhlig, and NI Wolf. Pi4ka-related disorder. Unknown journal, 2022.

8. (pagnamenta2015germlinerecessivemutations pages 7-8): Alistair T. Pagnamenta, Malcolm F. Howard, Eva Wisniewski, Niko Popitsch, Samantha J.L. Knight, David A. Keays, Gerardine Quaghebeur, Helen Cox, Phillip Cox, Tamas Balla, Jenny C. Taylor, and Usha Kini. Germline recessive mutations in pi4ka are associated with perisylvian polymicrogyria, cerebellar hypoplasia and arthrogryposis. Human Molecular Genetics, 24:3732-3741, Apr 2015. URL: https://doi.org/10.1093/hmg/ddv117, doi:10.1093/hmg/ddv117. This article has 96 citations and is from a domain leading peer-reviewed journal.

9. (pagnamenta2015germlinerecessivemutations pages 6-7): Alistair T. Pagnamenta, Malcolm F. Howard, Eva Wisniewski, Niko Popitsch, Samantha J.L. Knight, David A. Keays, Gerardine Quaghebeur, Helen Cox, Phillip Cox, Tamas Balla, Jenny C. Taylor, and Usha Kini. Germline recessive mutations in pi4ka are associated with perisylvian polymicrogyria, cerebellar hypoplasia and arthrogryposis. Human Molecular Genetics, 24:3732-3741, Apr 2015. URL: https://doi.org/10.1093/hmg/ddv117, doi:10.1093/hmg/ddv117. This article has 96 citations and is from a domain leading peer-reviewed journal.

10. (verdura2021biallelicpi4kavariants pages 4-4): Edgard Verdura, Agustí Rodríguez-Palmero, Valentina Vélez-Santamaria, Laura Planas-Serra, Irene de la Calle, Miquel Raspall-Chaure, Agathe Roubertie, Mehdi Benkirane, Francesco Saettini, Lisa Pavinato, Giorgia Mandrile, Melanie O’Leary, Emily O’Heir, Estibaliz Barredo, Almudena Chacón, Vincent Michaud, Cyril Goizet, Montserrat Ruiz, Agatha Schlüter, Isabelle Rouvet, Julia Sala-Coromina, Chiara Fossati, Maria Iascone, Francesco Canonico, Anna Marcé-Grau, Precilla de Souza, David R Adams, Carlos Casasnovas, Heidi L Rehm, Heather C Mefford, Luis González Gutierrez-Solana, Alfredo Brusco, Michel Koenig, Alfons Macaya, and Aurora Pujol. Biallelic pi4ka variants cause a novel neurodevelopmental syndrome with hypomyelinating leukodystrophy. Brain, 144:2659-2669, Aug 2021. URL: https://doi.org/10.1093/brain/awab124, doi:10.1093/brain/awab124. This article has 67 citations and is from a highest quality peer-reviewed journal.

11. (verdura2021biallelicpi4kavariants pages 7-9): Edgard Verdura, Agustí Rodríguez-Palmero, Valentina Vélez-Santamaria, Laura Planas-Serra, Irene de la Calle, Miquel Raspall-Chaure, Agathe Roubertie, Mehdi Benkirane, Francesco Saettini, Lisa Pavinato, Giorgia Mandrile, Melanie O’Leary, Emily O’Heir, Estibaliz Barredo, Almudena Chacón, Vincent Michaud, Cyril Goizet, Montserrat Ruiz, Agatha Schlüter, Isabelle Rouvet, Julia Sala-Coromina, Chiara Fossati, Maria Iascone, Francesco Canonico, Anna Marcé-Grau, Precilla de Souza, David R Adams, Carlos Casasnovas, Heidi L Rehm, Heather C Mefford, Luis González Gutierrez-Solana, Alfredo Brusco, Michel Koenig, Alfons Macaya, and Aurora Pujol. Biallelic pi4ka variants cause a novel neurodevelopmental syndrome with hypomyelinating leukodystrophy. Brain, 144:2659-2669, Aug 2021. URL: https://doi.org/10.1093/brain/awab124, doi:10.1093/brain/awab124. This article has 67 citations and is from a highest quality peer-reviewed journal.

12. (baple2022pi4karelateddisorder pages 10-11): EL Baple, C Salter, H Uhlig, and NI Wolf. Pi4ka-related disorder. Unknown journal, 2022.

13. (zhang2022asynonymousmutation pages 8-10): Kaihui Zhang, Lili Kang, Haozheng Zhang, Lu Bai, Huanping Pang, Qinghua Liu, Xinyi Zhang, Dong Chen, Haihua Yu, Yuqiang Lv, Min Gao, Yi Liu, Zhongtao Gai, Dong Wang, and Xiaoying Li. A synonymous mutation in pi4ka impacts the transcription and translation process of gene expression. Frontiers in Immunology, Oct 2022. URL: https://doi.org/10.3389/fimmu.2022.987666, doi:10.3389/fimmu.2022.987666. This article has 15 citations and is from a peer-reviewed journal.

14. (zhang2022asynonymousmutation pages 1-2): Kaihui Zhang, Lili Kang, Haozheng Zhang, Lu Bai, Huanping Pang, Qinghua Liu, Xinyi Zhang, Dong Chen, Haihua Yu, Yuqiang Lv, Min Gao, Yi Liu, Zhongtao Gai, Dong Wang, and Xiaoying Li. A synonymous mutation in pi4ka impacts the transcription and translation process of gene expression. Frontiers in Immunology, Oct 2022. URL: https://doi.org/10.3389/fimmu.2022.987666, doi:10.3389/fimmu.2022.987666. This article has 15 citations and is from a peer-reviewed journal.

15. (zhang2022asynonymousmutation pages 2-4): Kaihui Zhang, Lili Kang, Haozheng Zhang, Lu Bai, Huanping Pang, Qinghua Liu, Xinyi Zhang, Dong Chen, Haihua Yu, Yuqiang Lv, Min Gao, Yi Liu, Zhongtao Gai, Dong Wang, and Xiaoying Li. A synonymous mutation in pi4ka impacts the transcription and translation process of gene expression. Frontiers in Immunology, Oct 2022. URL: https://doi.org/10.3389/fimmu.2022.987666, doi:10.3389/fimmu.2022.987666. This article has 15 citations and is from a peer-reviewed journal.

16. (baple2022pi4karelateddisorder pages 6-8): EL Baple, C Salter, H Uhlig, and NI Wolf. Pi4ka-related disorder. Unknown journal, 2022.

17. (pagnamenta2015germlinerecessivemutations pages 8-9): Alistair T. Pagnamenta, Malcolm F. Howard, Eva Wisniewski, Niko Popitsch, Samantha J.L. Knight, David A. Keays, Gerardine Quaghebeur, Helen Cox, Phillip Cox, Tamas Balla, Jenny C. Taylor, and Usha Kini. Germline recessive mutations in pi4ka are associated with perisylvian polymicrogyria, cerebellar hypoplasia and arthrogryposis. Human Molecular Genetics, 24:3732-3741, Apr 2015. URL: https://doi.org/10.1093/hmg/ddv117, doi:10.1093/hmg/ddv117. This article has 96 citations and is from a domain leading peer-reviewed journal.

18. (zhang2022asynonymousmutation pages 4-6): Kaihui Zhang, Lili Kang, Haozheng Zhang, Lu Bai, Huanping Pang, Qinghua Liu, Xinyi Zhang, Dong Chen, Haihua Yu, Yuqiang Lv, Min Gao, Yi Liu, Zhongtao Gai, Dong Wang, and Xiaoying Li. A synonymous mutation in pi4ka impacts the transcription and translation process of gene expression. Frontiers in Immunology, Oct 2022. URL: https://doi.org/10.3389/fimmu.2022.987666, doi:10.3389/fimmu.2022.987666. This article has 15 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Polymicrogyria_Perisylvian_With_Cerebellar_Hypoplasia_And_Arthrogryposis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0004430` (1 mention) - the report calls it "GO molecular function:** phosphatidylinositol 4-kinase activity"; GO calls it **1-phosphatidylinositol 4-kinase activity**
- `GO:0005886` (1 mention) - the report calls it "GO cellular component:** plasma membrane"; GO calls it **plasma membrane**, and lists "integral component of plasma membrane" among its other names

Every term resolved, and every label the report gave matched.