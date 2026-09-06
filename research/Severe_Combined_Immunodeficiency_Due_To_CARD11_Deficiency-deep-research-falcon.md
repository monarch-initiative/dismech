---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-06T02:47:26.273526'
end_time: '2026-09-06T03:04:13.672003'
duration_seconds: 1007.4
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Severe Combined Immunodeficiency Due to CARD11 Deficiency
  mondo_id: MONDO:0014081
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 36
  verified: 32
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0014081
    reported_labels:
    - if available
    ontology_label: severe combined immunodeficiency due to CARD11 deficiency
  - term_id: NCIT:C106497
    reported_labels:
    - Whole Exome Sequencing
    ontology_label: Age at Menopause
  obsolete_terms:
  - term_id: GO:0032088
    ontology_label: obsolete negative regulation of NF-kappaB transcription factor
      activity
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Severe_Combined_Immunodeficiency_Due_To_CARD11_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Severe Combined Immunodeficiency Due to CARD11 Deficiency
- **MONDO ID:** MONDO:0014081 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Severe Combined Immunodeficiency Due to CARD11 Deficiency** covering all of the
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
- **Disease Name:** Severe Combined Immunodeficiency Due to CARD11 Deficiency
- **MONDO ID:** MONDO:0014081 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Severe Combined Immunodeficiency Due to CARD11 Deficiency** covering all of the
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


# Severe Combined Immunodeficiency Due to CARD11 Deficiency

## Executive summary and scope

Severe combined immunodeficiency due to CARD11 deficiency is an ultra-rare, congenital inborn error of immunity caused by **biallelic germline loss-of-function (LOF) variants in CARD11**. Complete LOF produces an early, profound combined immunodeficiency (CID/SCID-spectrum disease) despite often-normal circulating T- and B-cell counts and normal T-cell receptor excision circles (TRECs). Severe hypomorphic biallelic variants can produce a broader CID phenotype with enteropathy and atopic skin disease. The defining defect is failure of antigen-receptor-induced CARD11–BCL10–MALT1 (CBM) signaling in lymphocytes, impairing NF-κB, JNK, MALT1 paracaspase activity, regulatory T-cell development, T-follicular-helper function, and B-cell maturation. Allogeneic hematopoietic stem-cell transplantation (HSCT) is the only established definitive treatment. (lu2018thecbmopathies—arapidly pages 4-5, (henry)2023definingthepathogenesis pages 75-79, lu2021mechanisticunderstandingof pages 17-20, lu2021mechanisticunderstandingof pages 20-23)

A critical nomenclature distinction is necessary:

* **Biallelic LOF CARD11** → autosomal-recessive profound CID/SCID, the subject of this report.
* **Heterozygous dominant-negative CARD11** → CARD11-associated atopy with dominant interference of NF-κB signaling (**CADINS**; immunodeficiency 11B), usually less profound and strongly atopic.
* **Heterozygous activating CARD11** → B-cell expansion with NF-κB and T-cell anergy (**BENTA**), characterized by constitutive NF-κB signaling and lymphocytosis. (garciamartinez2025fromsyndromicclues pages 3-5, garciamartinez2025fromsyndromicclues pages 1-2)

| Domain | Established Finding | Quantitative/Current Evidence | Ontology Suggestions | Evidence Limitations |
| :--- | :--- | :--- | :--- | :--- |
| **Identity / IDs** | Severe combined immunodeficiency (SCID) / profound CID due to AR biallelic *CARD11* loss-of-function. Explicitly distinct from AD CADINS (dominant-negative) and AD BENTA (gain-of-function). (OpenTargets Search: Severe combined immunodeficiency due to CARD11 deficiency-CARD11, garciamartinez2025fromsyndromicclues pages 1-2) | Entity mapped to Immunodeficiency 11A. Literature explicitly classifies complete CARD11 deficiency as an AR CID/SCID-spectrum disorder, distinct from OMIM 617638 (CADINS) and OMIM 616452 (BENTA). (garciamartinez2025fromsyndromicclues pages 1-2) | MONDO:0014081, OMIM:615206, ORPHA:325636 | Nomenclature varies; often historically termed simply "CARD11 deficiency" which risks conflation with CADINS. |
| **Genetics / Variants** | Caused by biallelic loss-of-function variants (nonsense, large deletions) or severe hypomorphic missense variants in the *CARD11* gene. (lu2018thecbmopathies—arapidly pages 4-5, meshaal2024novelhomozygouscard11 pages 1-2, lu2021mechanisticunderstandingof pages 20-23) | Documented variants include p.Gln945\*, p.Cys150\*, p.Arg837\*, p.Phe902_Glu946del (complete loss-of-function) and p.Glu947Lys, p.Pro568Arg (hypomorphic missense). Typically identified in consanguineous families. (lu2018thecbmopathies—arapidly pages 4-5, meshaal2024novelhomozygouscard11 pages 1-2, lu2021mechanisticunderstandingof pages 20-23) | HGNC:16393 (CARD11) | Very few unique variants (<15) have been characterized worldwide, limiting large-scale genotype-phenotype correlations. |
| **Phenotype** | Early-onset (3-15 months) profound combined immunodeficiency with severe respiratory infections, *Pneumocystis jirovecii* pneumonia (PJP), chronic enteropathy/diarrhea, and atopic dermatitis. ((henry)2023definingthepathogenesis pages 67-71, meshaal2024novelhomozygouscard11 pages 2-4, lu2021mechanisticunderstandingof pages 20-23) | PJP/pneumonia present in 100% (3/3) of earliest reported complete deficiency cases. Missense variant cases presented with severe early-onset allergic skin disease and respiratory failure. ((henry)2023definingthepathogenesis pages 67-71, meshaal2024novelhomozygouscard11 pages 2-4) | HP:0006510 (Pneumocystis jirovecii pneumonia), HP:0002721 (Immunodeficiency), HP:0040226 (Atopic dermatitis), HP:0025345 (Enteropathy) | Phenotype overlaps significantly with other SCID/CID syndromes; atypical missense cases may mimic AD CADINS. |
| **Immune Laboratory Signature** | Progressive panhypogammaglobulinemia, defective T-cell activation/proliferation, absent Tregs, expanded transitional B cells, and severely reduced class-switched memory B cells. ((henry)2023definingthepathogenesis pages 75-79, (henry)2023definingthepathogenesis pages 67-71) | 3/3 classic patients had normal total T/B numbers but predominantly naive T-cells and severely diminished Tregs. Normal TRECs and KRECs frequently noted, leading to missed newborn screening. ((henry)2023definingthepathogenesis pages 75-79, (henry)2023definingthepathogenesis pages 67-71) | HP:0004313 (Decreased circulating antibody level), HP:0005403 (Decreased Treg count), HP:0005372 (Decreased class switched memory B cell count) | Normal total lymphocyte counts and TRECs initially confound SCID diagnosis. |
| **Mechanism** | Loss of CARD11 scaffold disrupts CARD11-BCL10-MALT1 (CBM) complex, abolishing canonical NF-κB, JNK, and MALT1 paracaspase activity following antigen receptor stimulation. (turvey2014thecard11bcl10malt1(cbm) pages 2-4, lu2021mechanisticunderstandingof pages 17-20) | Patient lymphocytes show impaired p65 phosphorylation, failed IκBα degradation, and defective MALT1 cleavage of substrates (e.g., HOIL1). ERK/p38 activation pathways remain intact. (lu2021mechanisticunderstandingof pages 17-20) | GO:0043123 (positive regulation of I-kappaB kinase/NF-kappaB signaling), GO:0032088 (regulation of NF-kappaB transcription factor activity) | Paracaspase (MALT1) and JNK downstream failures are well demonstrated, but exact targets driving specific sub-phenotypes remain under study. |
| **Diagnosis** | Relies on targeted/whole-exome sequencing and in vitro functional testing (PMA/ionomycin stimulation followed by NF-κB or IL-2/CD25 induction assessment). (turvey2014thecard11bcl10malt1(cbm) pages 5-7, (henry)2023definingthepathogenesis pages 75-79, meshaal2024novelhomozygouscard11 pages 2-4) | CD25 upregulation following ionomycin stimulation fails in patient T cells (e.g., 2% induction vs. 9-13% in healthy controls). (meshaal2024novelhomozygouscard11 pages 2-4) | NCIT:C106497 (Whole Exome Sequencing) | TREC newborn screening is an unreliable diagnostic due to variable early T-cell output. |
| **Treatment / Outcome** | Often fatal in early childhood without curative allogeneic hematopoietic stem cell transplantation (HSCT). Bridging therapies include IVIG and PJP prophylaxis. (turvey2014thecard11bcl10malt1(cbm) pages 5-7, (henry)2023definingthepathogenesis pages 75-79, lu2021mechanisticunderstandingof pages 20-23) | 3 of 5 earliest reported cases died within 2 years. Transplanted survivors achieved donor chimerism, full restoration of CBM signaling, and correction of naive/Tfh/B-cell subset defects. ((henry)2023definingthepathogenesis pages 75-79, lu2021mechanisticunderstandingof pages 20-23) | NCIT:C20005 (Allogeneic Hematopoietic Stem Cell Transplantation), NCIT:C28254 (Intravenous Immunoglobulin) | Long-term HSCT follow-up data specifically for CARD11 deficiency is limited to single case reports. |
| **Epidemiology** | Ultra-rare congenital disorder, primarily affecting pediatric populations born to consanguineous parents. (lu2018thecbmopathies—arapidly pages 4-5, (henry)2023definingthepathogenesis pages 67-71) | Fewer than 20 cases of completely recessive complete/hypomorphic CARD11 deficiency have been formally reported in peer-reviewed literature globally. (meshaal2024novelhomozygouscard11 pages 1-2, (henry)2023definingthepathogenesis pages 67-71) | - | True prevalence likely underrepresented due to missed diagnoses from normal TREC screening. |
| **2023-2024 Developments** | Identification of novel hypomorphic AR variants causing CID and severe atopy; discovery that CARD11 regulates thymic Tregs via an NF-κB-independent AKT/FOXO1 pathway. (meshaal2024novelhomozygouscard11 pages 1-2, hu2024card11regulatesthe pages 1-2) | 2024 studies (Meshaal et al.) described patients with AR hypomorphic missense variants presenting with CADINS-like skin disease. Hu et al. (2024) demonstrated murine/in vitro NF-κB-independent Treg regulation. (meshaal2024novelhomozygouscard11 pages 1-2, hu2024card11regulatesthe pages 1-2) | - | Murine model data regarding the non-canonical AKT/FOXO1 Treg pathway requires extensive validation in primary human CARD11-deficient patient cells. |


*Table: A concise table summarizing the genetic, clinical, mechanistic, and diagnostic features of biallelic CARD11-associated severe combined immunodeficiency, clearly distinguishing it from dominant forms of CARD11 disease.*

## 1. Disease information

**Definition.** This disease is a monogenic disorder of lymphocyte activation in which CARD11 deficiency interrupts signaling from the T-cell receptor (TCR) and B-cell receptor (BCR) to the CBM signalosome. It is often called “profound combined immunodeficiency” rather than classical lymphopenic SCID because lymphocyte production can initially be quantitatively preserved while antigen-receptor-dependent function is profoundly defective. (turvey2014thecard11bcl10malt1(cbm) pages 5-7, (henry)2023definingthepathogenesis pages 75-79)

**Identifiers and names**

* **MONDO:** MONDO:0014081, *severe combined immunodeficiency due to CARD11 deficiency*.
* **OMIM phenotype:** **615206**, commonly termed *Immunodeficiency 11A*.
* **Gene:** CARD11, approved name *caspase recruitment domain family member 11*; Ensembl ENSG00000198286. Open Targets links CARD11 as the sole associated target for MONDO:0014081. (OpenTargets Search: Severe combined immunodeficiency due to CARD11 deficiency-CARD11)
* **Suggested Orphanet mapping:** ORPHA:325636, subject to verification in the current Orphanet release.
* **Synonyms:** CARD11 deficiency; CARD11-associated severe combined immunodeficiency; autosomal-recessive CARD11 deficiency; immunodeficiency 11A; complete human CARD11 deficiency; CARD11-related profound combined immunodeficiency.
* **ICD/MeSH:** No uniquely specific ICD-10-CM or ICD-11 code was established in the retrieved evidence; use the relevant broader SCID/combined-immunodeficiency code locally. MeSH indexing is likewise generally under severe combined immunodeficiency/primary immunodeficiency rather than a CARD11-specific heading.

The evidence is predominantly **aggregated disease-level literature derived from a very small number of individually described patients**, not population EHR data. Consequently, case counts, phenotype frequencies, survival estimates, and variant penetrance remain imprecise.

## 2. Etiology, risk, and protective factors

The initiating cause is a **germline biallelic CARD11 variant that abolishes or markedly reduces protein expression or function**. Reported complete-deficiency alleles include exon-21 deletion/p.Phe902_Glu946del, p.Gln945Ter, p.Cys150Ter, p.Arg837Ter, and other truncating/compound-heterozygous alleles; newer hypomorphic cases include homozygous p.Glu947Lys and p.Pro568Arg. (lu2018thecbmopathies—arapidly pages 4-5, turvey2014thecard11bcl10malt1(cbm) pages 5-7, meshaal2024novelhomozygouscard11 pages 1-2, lu2021mechanisticunderstandingof pages 20-23)

**Genetic risk factors.** Autosomal-recessive inheritance makes parental relatedness and a family history of infant deaths, opportunistic infection, or unexplained immunodeficiency important risk indicators. The earliest complete-deficiency patients were from consanguineous families; consanguinity increases the probability that a rare familial allele becomes homozygous but is not itself a biological cause. (lu2018thecbmopathies—arapidly pages 4-5, (henry)2023definingthepathogenesis pages 67-71)

**Environmental and infectious factors.** No toxin, diet, occupation, smoking exposure, or lifestyle factor causes the genetic defect. Pathogen exposure determines when clinical disease becomes apparent. Pneumocystis jirovecii, respiratory viruses, norovirus, Candida, and ordinary bacterial respiratory pathogens act as complications or triggers of decompensation, not etiologic agents. (turvey2014thecard11bcl10malt1(cbm) pages 2-4, meshaal2024novelhomozygouscard11 pages 2-4, lu2021mechanisticunderstandingof pages 20-23)

No validated protective CARD11 allele, modifier gene, epigenetic signature, or gene–environment interaction has been demonstrated. Infection avoidance, antimicrobial prophylaxis, immunoglobulin replacement, and early HSCT are clinically protective interventions rather than factors preventing inheritance.

## 3. Phenotypes

### Core severe/complete-deficiency phenotype

* **Early severe or opportunistic respiratory infection**, commonly between 3 and 15 months; Pneumocystis pneumonia occurred in all three patients in an early complete-deficiency series. Suggested HPO: immunodeficiency (HP:0002721), recurrent respiratory infections (HP:0002205), pneumonia (HP:0002090), and Pneumocystis jirovecii pneumonia. ((henry)2023definingthepathogenesis pages 67-71, (henry)2023definingthepathogenesis pages 75-79)
* **Progressive hypogammaglobulinemia or agammaglobulinemia**, often developing during infancy despite initially present B cells. Suggested HPO: hypogammaglobulinemia (HP:0004313) and decreased antibody response to vaccination. (turvey2014thecard11bcl10malt1(cbm) pages 2-4, (henry)2023definingthepathogenesis pages 75-79)
* **Defective cellular immunity:** impaired antigen-receptor-induced T-cell proliferation and cytokine production, with predominantly naïve T cells and severely reduced or absent Tregs. Suggested HPO: abnormal T-cell physiology, decreased regulatory T-cell count, and impaired lymphocyte proliferation. ((henry)2023definingthepathogenesis pages 75-79, (henry)2023definingthepathogenesis pages 67-71)
* **B-cell maturation abnormality:** increased transitional/naïve B cells and reduced class-switched memory B cells. Suggested HPO: decreased class-switched memory B-cell count and abnormal B-cell differentiation. (meshaal2024novelhomozygouscard11 pages 2-4, lu2021mechanisticunderstandingof pages 20-23)
* **Enteropathy:** chronic diarrhea, inflammatory gastrointestinal disease, failure to thrive, and in some patients severe colitis. Suggested HPO: chronic diarrhea (HP:0002028), enteropathy, intestinal inflammation, and failure to thrive (HP:0001508). (meshaal2024novelhomozygouscard11 pages 2-4, lu2021mechanisticunderstandingof pages 20-23)

### Expanded hypomorphic phenotype

The February 2024 Meshaal series described two unrelated patients with recurrent pneumonia requiring intensive care, chronic diarrhea, and pruritic atopic skin disease. The authors’ abstract states: **“Missense variants causing CARD11 deficiency may affect the protein function rather than the expression and can result in a phenotype combining the atopic skin disease and the features of CID.”** Both had markedly reduced Tregs and switched-memory B cells, expanded transitional B cells, and failure to induce CD25 after stimulation. Suggested HPO terms include atopic dermatitis (HP:0001047), exfoliative dermatitis, oral candidiasis, cutaneous warts, recurrent skin abscesses, and pruritus. (meshaal2024novelhomozygouscard11 pages 1-2, meshaal2024novelhomozygouscard11 pages 2-4)

A sibling with homozygous p.Cys150Ter plus somatic p.Cys150Leu reversion developed an Omenn-like phenotype with erythroderma/eczema, lymphoproliferation, oligoclonal T cells, high IgE, infections, and only partial NF-κB restoration. This illustrates how somatic rescue can alter, but not necessarily normalize, disease expression. ((henry)2023definingthepathogenesis pages 67-71)

No validated CARD11-specific EQ-5D, SF-36, PROMIS, or other quality-of-life data exist. Severe infection, ICU admission, diarrhea, growth failure, skin pruritus, isolation, repeated hospitalization, and transplantation predict a major burden, but quantitative QoL effects have not been measured.

## 4. Genetic and molecular information

CARD11 encodes an approximately 130-kDa, 1,154-amino-acid lymphocyte-enriched scaffold. Principal structural regions are the N-terminal CARD, LATCH, coiled-coil, inhibitory domain, and C-terminal MAGUK region comprising PDZ, SH3, and GUK subdomains. (lu2018thecbmopathies—arapidly pages 4-5, garciamartinez2025fromsyndromicclues pages 1-2, meshaal2024novelhomozygouscard11 pages 1-2)

Reported pathogenic classes include large exon deletion, nonsense, frameshift, splice-disrupting or compound-heterozygous LOF alleles, and severe homozygous missense alleles. Complete LOF generally causes absent/truncated protein; hypomorphic missense alleles may leave reduced protein expression but severely impair activation. The p.Arg837Ter allele was absent from referenced population databases, had a CADD score of 40, and was considered pathogenic under ACMG/AMP criteria. (garciamartinez2025fromsyndromicclues pages 3-5, (henry)2023definingthepathogenesis pages 120-125, lu2021mechanisticunderstandingof pages 20-23)

All established causal variants are **germline**. The p.Cys150Leu event noted above was a **somatic reversion**, not a primary somatic cause. No recurrent chromosomal rearrangement, aneuploidy, anticipation, founder allele, validated modifier gene, disease-specific methylation change, or carrier-frequency estimate has been established. Because individual variants are exceptionally rare, current population-database frequency should be checked for each exact HGVS allele during interpretation.

## 5. Environmental information

Environmental toxins, radiation, pollution, occupation, diet, exercise, alcohol, and smoking have no demonstrated causal role. Infectious exposures reveal the underlying defect and drive morbidity. Live vaccines may pose a risk in profound T-cell dysfunction and should be withheld until specialist immune evaluation. Household hygiene, safe food/water practices, avoidance of infectious contacts, and prompt treatment reduce exposure consequences but do not modify the genotype.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic CARD11 LOF leads to** absent, truncated, unstable, or nonfunctional CARD11 in lymphocytes. (lu2018thecbmopathies—arapidly pages 4-5, garciamartinez2025fromsyndromicclues pages 3-5)
2. **Defective CARD11 activation leads to** failure to convert the scaffold from its resting closed state to the open, signaling-competent state after PKCθ-dependent TCR or PKCβ-dependent BCR stimulation. (turvey2014thecard11bcl10malt1(cbm) pages 2-4, garciamartinez2025fromsyndromicclues pages 1-2)
3. **Failure of scaffold opening leads to** deficient recruitment/oligomerization of BCL10–MALT1 and impaired incorporation of TRAF6, IKKγ/NEMO, and HOIP into the CBM signalosome. ((henry)2023definingthepathogenesis pages 120-125, turvey2014thecard11bcl10malt1(cbm) pages 2-4)
4. **Defective CBM assembly leads to** reduced IKKα/β and p65 phosphorylation, defective IκBα degradation, impaired canonical NF-κB nuclear signaling, impaired JNK1/2 activation, and loss of MALT1 cleavage of HOIL1, RELB, N4BP1, and CYLD. ERK, p38, MEK, and MKK4 activation are relatively preserved. (lu2021mechanisticunderstandingof pages 17-20)
5. **Defective signaling leads to** poor induction of IL-2, IL-4, IFN-γ, CD25, ICOS, and CD69 and impaired lymphocyte proliferation after antigen-receptor stimulation. ((henry)2023definingthepathogenesis pages 120-125)
6. **T-cell branch:** defective activation and CARD11-dependent lineage regulation **lead to** reduced Tregs and circulating Tfh cells, impaired tolerance, and inadequate germinal-center help. A 2024 mouse/patient-sample study further suggests that CARD11 negatively regulates AKT–FOXO1 during thymic Treg development independently of NF-κB; its direct contribution in complete human deficiency remains incompletely demonstrated. (hu2024card11regulatesthe pages 1-2, lu2021mechanisticunderstandingof pages 20-23)
7. **B-cell branch:** defective BCR signaling and inadequate Tfh help **lead to** accumulation of transitional/naïve B cells, reduced memory and class-switched B cells, deficient germinal centers, and progressive hypogammaglobulinemia. (lu2021mechanisticunderstandingof pages 20-23, lu2021mechanisticunderstandingof pages 1-6)
8. **Combined cellular and humoral failure leads to** severe viral, fungal, and bacterial infection, PJP, chronic enteropathy, bronchiectasis, growth failure, sepsis, and early death without immune reconstitution. The direct attribution of every tissue complication to a specific molecular branch is partly inferred. ((henry)2023definingthepathogenesis pages 75-79, lu2021mechanisticunderstandingof pages 20-23)

**Suggested ontology annotations:** GO:0007166 signal transduction; GO:0050851 antigen-receptor-mediated signaling; GO:0043123 positive regulation of IκB kinase/NF-κB signaling; GO:0007254 JNK cascade; GO:0042110 T-cell activation; GO:0042113 B-cell activation; GO:0030183 B-cell differentiation; GO:0045061 thymic T-cell selection. Cell Ontology candidates include T lymphocyte (CL:0000084), B lymphocyte (CL:0000236), regulatory T cell (CL:0000815), follicular helper T cell, transitional B cell, memory B cell, plasma cell, and NK cell.

RNA sequencing of patient cells showed blunted induction of CARD11/NF-κB, inflammatory/tolerogenic, and germinal-center programs and reduced TNF–NF-κB, IFN-γ, IL-6–JAK–STAT3, and IL-2–STAT5 signatures; PI3K–AKT–mTOR and mTORC1 enrichment was reportedly unaffected. No reproducible disease-specific metabolomic, lipidomic, spatial-transcriptomic, or single-cell signature has been established. (lu2021mechanisticunderstandingof pages 17-20)

## 7. Anatomical structures affected

The **primary biological compartment** is hematopoietic/lymphoid tissue: peripheral blood, thymus, lymph nodes, spleen, tonsils, and bone marrow-derived lymphocyte lineages. Suggested UBERON terms include blood (UBERON:0000178), thymus (UBERON:0002370), lymph node (UBERON:0000029), spleen (UBERON:0002106), and bone marrow (UBERON:0002371).

Secondary injury commonly involves lung/airway through pneumonia and bronchiectasis; gastrointestinal mucosa through infectious or inflammatory enteropathy; and skin through dermatitis, candidiasis, abscesses, or viral warts. No lateralization is expected. At the subcellular level, CARD11 is a cytoplasmic membrane-proximal signalosome scaffold; relevant GO cellular-component annotations include cytoplasm, plasma-membrane-associated signaling complex, and CBM complex.

## 8. Temporal development

The defect is congenital, but manifestations generally begin in infancy after pathogen exposure and loss of maternally transferred antibody. Earliest complete cases presented at approximately 3–15 months with PJP or severe viral pneumonia. Hypomorphic cases may present later or with a more chronic atopy/enteropathy-predominant course. ((henry)2023definingthepathogenesis pages 67-71, meshaal2024novelhomozygouscard11 pages 2-4)

Untreated complete deficiency is progressive: recurrent infection is followed by worsening hypogammaglobulinemia, chronic lung or gastrointestinal damage, sepsis, and death. An early synthesis reported death before two years in 3/5 described patients; both survivors had received HSCT. These numbers are historical case-series observations, not a modern survival estimate. ((henry)2023definingthepathogenesis pages 75-79)

There is no recognized spontaneous remission except rare somatic reversion, which may produce an atypical Omenn phenotype rather than cure. The critical intervention window is **before opportunistic infection and irreversible organ damage**.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Parents of affected children are generally asymptomatic heterozygous carriers. Recurrence risk for each pregnancy of two confirmed carriers is 25% affected, 50% carrier, and 25% unaffected/non-carrier. Penetrance of complete biallelic null alleles appears high, but penetrance and expressivity of hypomorphic combinations cannot be quantified. No anticipation is expected.

The condition is ultra-rare: no population prevalence or annual incidence per 100,000 has been established. The 2024 report stated that only eight autosomal-recessive cases had previously been reported, then added two unrelated patients; differing publications count complete, hypomorphic, and somatically reverted cases differently. (meshaal2024novelhomozygouscard11 pages 1-2)

Both sexes are affected. Reported ancestries include Palestinian, Central European/German, Turkish, French, Middle Eastern/North African, and other families, without evidence for a sex bias or geographically restricted founder effect. Apparent clustering in consanguineous families reflects recessive inheritance and ascertainment.

## 10. Diagnostics

### Clinical and immune evaluation

Suspect CARD11 deficiency in an infant or child with PJP, severe viral pneumonia, chronic diarrhea/colitis, progressive hypogammaglobulinemia, atopy, or failure to thrive—especially when total T- and B-cell counts and TRECs are normal.

Recommended evaluation includes CBC with differential; lymphocyte subsets; naïve/memory T-cell, Treg, transitional/naïve/memory/class-switched B-cell panels; IgG, IgA, IgM, IgE; vaccine antibody titers where safe; lymphocyte proliferation to anti-CD3/CD28 and mitogens; and microbiological investigation for PJP, respiratory viruses, CMV/EBV, norovirus, Candida, and bacterial infection. Normal TREC/KREC or recent thymic emigrants do **not** exclude the disease. (turvey2014thecard11bcl10malt1(cbm) pages 5-7, (henry)2023definingthepathogenesis pages 75-79, (henry)2023definingthepathogenesis pages 67-71)

Functional confirmation can measure CARD11 protein, stimulated IκBα degradation, p65/IKK phosphorylation, NF-κB reporter activity, IL-2 secretion, CD25/CD69/ICOS induction, CBM assembly, and MALT1 substrate cleavage. In the 2024 hypomorphic cases, CD25-positive cells were approximately 2% before stimulation and only 2.6–2.8% afterward, compared with a control change from 9% to 13%. (meshaal2024novelhomozygouscard11 pages 2-4)

### Genetic testing

Use a validated IEI/SCID/CID panel containing **CARD11**, or rapid WES/WGS when the phenotype is nonspecific. Confirm candidate variants and segregation by Sanger sequencing; assess copy-number changes because exon deletions occur. RNA studies may clarify splice variants. Functional testing is particularly important for missense variants and VUSs.

Single-gene sequencing is reasonable where the functional phenotype strongly implicates CARD11. CMA, karyotype, FISH, mitochondrial sequencing, and repeat-expansion assays are not first-line unless another diagnosis is suspected.

### Differential diagnosis and screening

Differentials include BCL10, MALT1, IKBKB/IKK2, NFKB1/NFKB2, DOCK8, IL2RG, JAK3, RAG1/2, DCLRE1C, ZAP70, MHC-II deficiency, activated PI3Kδ syndrome, Wiskott–Aldrich syndrome, Omenn syndrome, and other atopic CIDs. CADINS and BENTA must be distinguished by inheritance, lymphocyte phenotype, and variant function.

TREC newborn screening can miss CARD11 deficiency because thymic output may be preserved. Genomic newborn screening could theoretically identify affected infants, but it is not yet standard disease-specific practice. Cascade testing of relatives is strongly indicated. (turvey2014thecard11bcl10malt1(cbm) pages 5-7, (henry)2023definingthepathogenesis pages 75-79)

## 11. Outcome and prognosis

Untreated complete deficiency carries a high risk of infant death from respiratory failure, opportunistic infection, or sepsis. Chronic complications include bronchiectasis, persistent viral infection, inflammatory enteropathy, malnutrition, skin disease, and organ injury from infection. No disease-specific 5- or 10-year survival, life-expectancy, disability, or QoL estimate is available. ((henry)2023definingthepathogenesis pages 75-79, lu2021mechanisticunderstandingof pages 20-23)

Prognosis is expected to improve with molecular diagnosis, infection control, and early HSCT. Poor prognostic indicators include PJP or disseminated infection before transplant, chronic viral infection, bronchiectasis, severe enteropathy, and transplant complications. Complete donor immune chimerism and restoration of CARD11 signaling are favorable biomarkers, although the number of documented patients is too small for validated prediction models. (lu2021mechanisticunderstandingof pages 17-20)

## 12. Treatment

### Definitive therapy

**Allogeneic HSCT** is the established curative strategy because CARD11 expression and the clinically critical defect are centered in hematopoietic cells. Published patients achieved immune reconstitution after matched or alternative-donor transplantation; patient-cell studies demonstrated post-HSCT restoration of CARD11 protein, NF-κB/JNK/MALT1 activity, lymphocyte activation, and differentiation. Conditioning regimens reported in early cases included fludarabine/antithymocyte globulin or treosulfan/fludarabine/alemtuzumab, but no CARD11-specific standard regimen or response percentage exists. (turvey2014thecard11bcl10malt1(cbm) pages 5-7, garciamartinez2025fromsyndromicclues pages 3-5, lu2021mechanisticunderstandingof pages 17-20)

Transplantation is not risk-free: infections, graft-versus-host disease, mixed chimerism, and neurologic/vascular complications have occurred; one p.Arg837Ter patient died after presumed posterior reversible encephalopathy-associated intracranial bleeding despite signaling restoration. (lu2021mechanisticunderstandingof pages 17-20)

Suggested NCIT intervention terms: allogeneic hematopoietic stem-cell transplantation; bone-marrow transplantation; peripheral-blood stem-cell transplantation; conditioning regimen; graft-versus-host-disease prophylaxis.

### Bridging and supportive care

* Immunoglobulin replacement, intravenous or subcutaneous.
* Pneumocystis prophylaxis, usually trimethoprim–sulfamethoxazole when tolerated.
* Pathogen-directed antibacterial, antiviral, or antifungal therapy.
* Nutritional support and treatment of enteropathy.
* Dermatologic treatment for barrier disease and infection.
* Avoidance of live vaccines while profound cellular immunodeficiency persists.

A 2024 report described dupilumab benefit for prurigo-like atopic dermatitis in CARD11-associated SCID, but this is symptomatic case-level evidence and does not correct immunodeficiency. No CARD11-specific drug, pharmacogenomic guideline, approved gene therapy, RNA therapy, or CRISPR treatment exists. The tool search identified no disease-specific interventional clinical trial or NCT identifier. Direct correction or replacement of CARD11 in autologous hematopoietic stem cells remains conceptual rather than clinical.

## 13. Prevention

The inherited disease cannot be prevented by lifestyle change. **Primary genetic prevention** consists of carrier testing, genetic counseling, reproductive options including preimplantation genetic testing, and prenatal diagnosis when familial variants are known.

**Secondary prevention** includes cascade testing, rapid molecular diagnosis in symptomatic infants, and evaluation of at-risk newborn siblings even if TREC screening is normal. **Tertiary prevention** includes immunoglobulin replacement, PJP prophylaxis, infection avoidance, inactivated vaccines where appropriate, withholding live vaccines, CMV-safe/irradiated blood products when indicated, and HSCT before organ damage. Genetic counseling should explain the 25% recurrence risk for carrier couples.

## 14. Other species and natural disease

CARD11 orthologues are evolutionarily conserved in vertebrates. The principal comparative organism is **Mus musculus** (NCBI Taxonomy 10090). No well-established naturally occurring veterinary syndrome directly equivalent to human biallelic CARD11 SCID, breed predisposition, zoonotic transmission, or cross-species infectious transmission was identified. This is a genetic, noncommunicable disorder.

## 15. Model organisms and experimental systems

**Mouse models.** Card11-null mice reproduce major cellular features: defective antigen-receptor-induced NF-κB/JNK signaling, impaired B- and T-cell proliferation, deficient antibody responses, reduced Tregs, and abnormal Tfh/B-cell biology. They are useful for dissecting immune signaling and lineage development but do not fully reproduce the timing, pathogen spectrum, ICU-level infection, or transplant course of human infants. (lu2018thecbmopathies—arapidly pages 4-5, (henry)2023definingthepathogenesis pages 67-71)

The April 8, 2024 Hu study used Card11 knockout and pathogenic E134G/K215M transgenic mice, patient samples, in-vitro suppression assays, and retrovirally transduced bone-marrow chimeras. Its abstract reports that CARD11’s **“noncanonical function… negatively regulates the AKT/FOXO1 signal pathway”** and regulates thymic Treg generation independently of canonical NF-κB. This is an important mechanistic advance, but extrapolation to complete human deficiency requires further patient validation. DOI: https://doi.org/10.3389/fimmu.2024.1364957. (hu2024card11regulatesthe pages 1-2)

**Cellular systems.** Patient primary lymphocytes, EBV-transformed B-cell lines, CARD11-deficient Jurkat cells, transient NF-κB reporter assays, co-immunoprecipitation, RNA-seq, and multiplexed functional assays are established platforms for evaluating variant effects. They are valuable for ACMG functional evidence but may not model tissue-specific infection or developmental timing. ((henry)2023definingthepathogenesis pages 120-125, lu2021mechanisticunderstandingof pages 17-20)

## Recent developments and evidence appraisal

1. **2023:** a biallelic LOF report expanded the phenotype to autosomal-recessive inflammatory skin disease, reinforcing that recessive CARD11 disease is not uniformly infection-only.
2. **February 2024:** Meshaal et al. added two homozygous missense variants—p.Glu947Lys and p.Pro568Arg—and demonstrated a hypomorphic CID/atopy phenotype with reduced rather than absent CARD11 expression. DOI: https://doi.org/10.1186/s43042-024-00489-3. (meshaal2024novelhomozygouscard11 pages 1-2, meshaal2024novelhomozygouscard11 pages 2-4)
3. **April 2024:** Hu et al. identified an NF-κB-independent CARD11–AKT–FOXO1 contribution to thymic Treg development in mouse/chimera systems. (hu2024card11regulatesthe pages 1-2)
4. Current expert interpretation is therefore a **functional continuum**: complete biallelic LOF produces profound early CID/SCID; partial biallelic LOF may retain protein expression and add atopy/inflammation; heterozygous dominant-negative and GOF alleles define CADINS and BENTA, respectively. Functional validation is essential when genotype alone cannot assign the mechanism. (garciamartinez2025fromsyndromicclues pages 3-5, meshaal2024novelhomozygouscard11 pages 1-2)

## Key references

* Stepensky et al. *Deficiency of caspase recruitment domain family, member 11 (CARD11), causes profound combined immunodeficiency in human subjects.* Published February 2013. PMID **23374270**; DOI: https://doi.org/10.1016/j.jaci.2012.11.050. (OpenTargets Search: Severe combined immunodeficiency due to CARD11 deficiency-CARD11, (henry)2023definingthepathogenesis pages 67-71)
* Greil et al. *Whole-exome sequencing links CARD11 inactivation to severe combined immunodeficiency.* Published May 2013. PMID **23561803**; DOI: https://doi.org/10.1016/j.jaci.2013.02.012. (OpenTargets Search: Severe combined immunodeficiency due to CARD11 deficiency-CARD11, turvey2014thecard11bcl10malt1(cbm) pages 2-4)
* Turvey et al. *The CARD11-BCL10-MALT1 signalosome complex: stepping into the limelight of human primary immunodeficiency.* Published August 2014. DOI: https://doi.org/10.1016/j.jaci.2014.06.015. (turvey2014thecard11bcl10malt1(cbm) pages 5-7)
* Lu et al. *Mechanistic understanding of the combined immunodeficiency in complete human CARD11 deficiency.* Published December 2021. DOI: https://doi.org/10.1016/j.jaci.2021.04.006. (lu2021mechanisticunderstandingof pages 17-20, lu2021mechanisticunderstandingof pages 20-23)
* Meshaal et al. *Novel homozygous CARD11 variants in two patients with combined immunodeficiency and atopic skin disease.* Published February 2024. DOI: https://doi.org/10.1186/s43042-024-00489-3. (meshaal2024novelhomozygouscard11 pages 1-2)
* Hu et al. *CARD11 regulates the thymic Treg development in an NF-κB-independent manner.* Published April 8, 2024. DOI: https://doi.org/10.3389/fimmu.2024.1364957. (hu2024card11regulatesthe pages 1-2)

### Knowledge-base confidence statement

Confidence is **high** for causality, recessive inheritance, CBM/NF-κB pathway failure, characteristic functional immunophenotype, and HSCT as definitive therapy. Confidence is **moderate** for the full phenotypic spectrum and genotype–phenotype relationships, and **low/insufficient** for prevalence, penetrance of hypomorphic alleles, variant-specific prognosis, long-term QoL, treatment-response rates, modifier genes, epigenomics, and advanced single-cell/spatial/metabolomic biomarkers because the literature consists mainly of fewer than a few dozen individually reported patients.

References

1. (lu2018thecbmopathies—arapidly pages 4-5): Henry Y. Lu, Bradly M. Bauman, Swadhinya Arjunaraja, Batsukh Dorjbal, Joshua D. Milner, Andrew L. Snow, and Stuart E. Turvey. The cbm-opathies—a rapidly expanding spectrum of human inborn errors of immunity caused by mutations in the card11-bcl10-malt1 complex. Frontiers in Immunology, Sep 2018. URL: https://doi.org/10.3389/fimmu.2018.02078, doi:10.3389/fimmu.2018.02078. This article has 143 citations and is from a peer-reviewed journal.

2. ((henry)2023definingthepathogenesis pages 75-79): Yi-Chin (Henry) Lu. Defining the pathogenesis of human inborn errors of immunity affecting the card11-bcl10-malt1 complex. ArXiv, Jan 2023. URL: https://doi.org/10.14288/1.0394898, doi:10.14288/1.0394898. This article has 0 citations.

3. (lu2021mechanisticunderstandingof pages 17-20): Henry Y. Lu, Mehul Sharma, Ashish A. Sharma, Atilano Lacson, Ashley Szpurko, Joanne Luider, Poonam Dharmani-Khan, Afshin Shameli, Peter A. Bell, Gregory M.T. Guilcher, Victor A. Lewis, Marta Rojas Vasquez, Sunil Desai, Lyle McGonigle, Luis Murguia-Favela, Nicola A.M. Wright, Consolato Sergi, Eytan Wine, Christopher M. Overall, Sneha Suresh, and Stuart E. Turvey. Mechanistic understanding of the combined immunodeficiency in complete human card11 deficiency. Dec 2021. URL: https://doi.org/10.1016/j.jaci.2021.04.006, doi:10.1016/j.jaci.2021.04.006. This article has 38 citations and is from a highest quality peer-reviewed journal.

4. (lu2021mechanisticunderstandingof pages 20-23): Henry Y. Lu, Mehul Sharma, Ashish A. Sharma, Atilano Lacson, Ashley Szpurko, Joanne Luider, Poonam Dharmani-Khan, Afshin Shameli, Peter A. Bell, Gregory M.T. Guilcher, Victor A. Lewis, Marta Rojas Vasquez, Sunil Desai, Lyle McGonigle, Luis Murguia-Favela, Nicola A.M. Wright, Consolato Sergi, Eytan Wine, Christopher M. Overall, Sneha Suresh, and Stuart E. Turvey. Mechanistic understanding of the combined immunodeficiency in complete human card11 deficiency. Dec 2021. URL: https://doi.org/10.1016/j.jaci.2021.04.006, doi:10.1016/j.jaci.2021.04.006. This article has 38 citations and is from a highest quality peer-reviewed journal.

5. (garciamartinez2025fromsyndromicclues pages 3-5): Elena García-Martínez, María Teresa Schiaffino, Marisa Di Natale, María de las Mercedes Díaz Luna, Daniel Alejandro Viteri Álvarez, and María Alejandra Mejía González. From syndromic clues to diagnosis: understanding card11-driven disorders. Frontiers in Immunology, Jun 2025. URL: https://doi.org/10.3389/fimmu.2025.1626065, doi:10.3389/fimmu.2025.1626065. This article has 3 citations and is from a peer-reviewed journal.

6. (garciamartinez2025fromsyndromicclues pages 1-2): Elena García-Martínez, María Teresa Schiaffino, Marisa Di Natale, María de las Mercedes Díaz Luna, Daniel Alejandro Viteri Álvarez, and María Alejandra Mejía González. From syndromic clues to diagnosis: understanding card11-driven disorders. Frontiers in Immunology, Jun 2025. URL: https://doi.org/10.3389/fimmu.2025.1626065, doi:10.3389/fimmu.2025.1626065. This article has 3 citations and is from a peer-reviewed journal.

7. (OpenTargets Search: Severe combined immunodeficiency due to CARD11 deficiency-CARD11): Open Targets Query (Severe combined immunodeficiency due to CARD11 deficiency-CARD11, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (meshaal2024novelhomozygouscard11 pages 1-2): S. Meshaal, Rabab E. EL Hawary, Dalia Abd Elaziz, Alia S. Eldash, Rania Darwish, Aya Erfan, Sohilla Lotfy, Maii Saad, Engy A. Chohayeb, Radwa Alkady, Jeannette A. Boutros, Nermeen M. Galal, and A. Elmarsafy. Novel homozygous card11 variants in two patients with combined immunodeficiency and atopic skin disease. Egyptian Journal of Medical Human Genetics, Feb 2024. URL: https://doi.org/10.1186/s43042-024-00489-3, doi:10.1186/s43042-024-00489-3. This article has 7 citations and is from a peer-reviewed journal.

9. ((henry)2023definingthepathogenesis pages 67-71): Yi-Chin (Henry) Lu. Defining the pathogenesis of human inborn errors of immunity affecting the card11-bcl10-malt1 complex. ArXiv, Jan 2023. URL: https://doi.org/10.14288/1.0394898, doi:10.14288/1.0394898. This article has 0 citations.

10. (meshaal2024novelhomozygouscard11 pages 2-4): S. Meshaal, Rabab E. EL Hawary, Dalia Abd Elaziz, Alia S. Eldash, Rania Darwish, Aya Erfan, Sohilla Lotfy, Maii Saad, Engy A. Chohayeb, Radwa Alkady, Jeannette A. Boutros, Nermeen M. Galal, and A. Elmarsafy. Novel homozygous card11 variants in two patients with combined immunodeficiency and atopic skin disease. Egyptian Journal of Medical Human Genetics, Feb 2024. URL: https://doi.org/10.1186/s43042-024-00489-3, doi:10.1186/s43042-024-00489-3. This article has 7 citations and is from a peer-reviewed journal.

11. (turvey2014thecard11bcl10malt1(cbm) pages 2-4): Stuart E. Turvey, Anne Durandy, Alain Fischer, Shan-Yu Fung, Raif S. Geha, Andreas Gewies, Thomas Giese, Johann Greil, Bärbel Keller, Margaret L. McKinnon, Bénédicte Neven, Jacob Rozmus, Jürgen Ruland, Andrew L. Snow, Polina Stepensky, and Klaus Warnatz. The card11-bcl10-malt1 (cbm) signalosome complex: stepping into the limelight of human primary immunodeficiency. The Journal of allergy and clinical immunology, 134 2:276-84, Aug 2014. URL: https://doi.org/10.1016/j.jaci.2014.06.015, doi:10.1016/j.jaci.2014.06.015. This article has 174 citations.

12. (turvey2014thecard11bcl10malt1(cbm) pages 5-7): Stuart E. Turvey, Anne Durandy, Alain Fischer, Shan-Yu Fung, Raif S. Geha, Andreas Gewies, Thomas Giese, Johann Greil, Bärbel Keller, Margaret L. McKinnon, Bénédicte Neven, Jacob Rozmus, Jürgen Ruland, Andrew L. Snow, Polina Stepensky, and Klaus Warnatz. The card11-bcl10-malt1 (cbm) signalosome complex: stepping into the limelight of human primary immunodeficiency. The Journal of allergy and clinical immunology, 134 2:276-84, Aug 2014. URL: https://doi.org/10.1016/j.jaci.2014.06.015, doi:10.1016/j.jaci.2014.06.015. This article has 174 citations.

13. (hu2024card11regulatesthe pages 1-2): Yu Hu, Lingli Han, Wenwen Xu, Tianci Li, Qifang Zhao, Wei Lu, Jinqiao Sun, and Ying Wang. Card11 regulates the thymic treg development in an nf-κb-independent manner. Frontiers in Immunology, Apr 2024. URL: https://doi.org/10.3389/fimmu.2024.1364957, doi:10.3389/fimmu.2024.1364957. This article has 8 citations and is from a peer-reviewed journal.

14. ((henry)2023definingthepathogenesis pages 120-125): Yi-Chin (Henry) Lu. Defining the pathogenesis of human inborn errors of immunity affecting the card11-bcl10-malt1 complex. ArXiv, Jan 2023. URL: https://doi.org/10.14288/1.0394898, doi:10.14288/1.0394898. This article has 0 citations.

15. (lu2021mechanisticunderstandingof pages 1-6): Henry Y. Lu, Mehul Sharma, Ashish A. Sharma, Atilano Lacson, Ashley Szpurko, Joanne Luider, Poonam Dharmani-Khan, Afshin Shameli, Peter A. Bell, Gregory M.T. Guilcher, Victor A. Lewis, Marta Rojas Vasquez, Sunil Desai, Lyle McGonigle, Luis Murguia-Favela, Nicola A.M. Wright, Consolato Sergi, Eytan Wine, Christopher M. Overall, Sneha Suresh, and Stuart E. Turvey. Mechanistic understanding of the combined immunodeficiency in complete human card11 deficiency. Dec 2021. URL: https://doi.org/10.1016/j.jaci.2021.04.006, doi:10.1016/j.jaci.2021.04.006. This article has 38 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Severe_Combined_Immunodeficiency_Due_To_CARD11_Deficiency-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014081` (4 mentions) - the report calls it "if available"; MONDO calls it **severe combined immunodeficiency due to CARD11 deficiency**
- `NCIT:C106497` (1 mention) - the report calls it "Whole Exome Sequencing"; NCIT calls it **Age at Menopause**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0032088` (obsolete negative regulation of NF-kappaB transcription factor activity) (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.