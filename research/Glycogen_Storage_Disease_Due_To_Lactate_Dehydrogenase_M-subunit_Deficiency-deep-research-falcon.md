---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T23:47:27.809306'
end_time: '2026-09-03T23:56:05.664153'
duration_seconds: 517.85
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Glycogen Storage Disease Due To Lactate Dehydrogenase M-subunit Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
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
  total_terms: 20
  verified: 18
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - ORPHA
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Glycogen_Storage_Disease_Due_To_Lactate_Dehydrogenase_M-subunit_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glycogen Storage Disease Due To Lactate Dehydrogenase M-subunit Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Glycogen Storage Disease Due To Lactate Dehydrogenase M-subunit Deficiency** covering all of the
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
- **Disease Name:** Glycogen Storage Disease Due To Lactate Dehydrogenase M-subunit Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Glycogen Storage Disease Due To Lactate Dehydrogenase M-subunit Deficiency** covering all of the
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


# Glycogen Storage Disease Due to Lactate Dehydrogenase M-Subunit Deficiency

## Executive summary

**LDHA-related glycogen storage disease type XI (GSD XI)** is an exceptionally rare autosomal-recessive metabolic myopathy caused by biallelic loss-of-function variants in **LDHA**, which encodes the muscle-type M subunit of lactate dehydrogenase. Loss of M-subunit-containing LDH isoenzymes limits lactate formation and NAD⁺ regeneration during high glycolytic demand. The characteristic phenotype is poor tolerance of short, intense, predominantly anaerobic exercise, with myalgia, cramps or stiffness, hyper-CK-emia, myoglobinuria, and episodic rhabdomyolysis. Psoriasiform dermatitis is an important but inconsistent extramuscular manifestation. Evidence remains almost entirely case-based: a 2021 synthesis found only 14 historical patients, and the most informative modern primary report described two additional Spanish patients in 2022. No population prevalence, standardized guideline, approved disease-modifying therapy, or disease-specific therapeutic trial was identified. (serranolorenzo2022clinicalbiochemicaland pages 5-7, serranolorenzo2022clinicalbiochemicaland pages 1-2, serranolorenzo2022clinicalbiochemicaland pages 7-9, ariceta2021hepaticlactatedehydrogenase pages 2-4)

| Domain | Established finding | Quantitative detail | Evidence level / caveat |
|---|---|---|---|
| Disease identity | LDHA-related glycogen storage disease type XI; synonyms include GSD XI, lactate dehydrogenase A deficiency, LDH-A deficiency, muscle LDH deficiency, and lactate dehydrogenase M-subunit deficiency | OMIM **612933**; ORPHA **284426** | Authoritative resource synthesis. “GSD XI” may also refer to GLUT2-deficient Fanconi–Bickel syndrome; specify **LDHA-related GSD XI**. (serranolorenzo2022clinicalbiochemicaland pages 1-2, ellingwood2018biochemicalandclinical pages 12-16) |
| Gene and inheritance | Biallelic germline loss-of-function variants in **LDHA** cause an autosomal-recessive metabolic myopathy | Chromosome **11p15.1**; 7 exons; approximately 12 kb; protein 333 amino acids | Established through human pedigrees, segregation, molecular testing, and enzyme studies. (serranolorenzo2022clinicalbiochemicaland pages 5-7, serranolorenzo2022clinicalbiochemicaland pages 1-2, kanungo2018glycogenmetabolismand pages 5-6) |
| Core muscle phenotype | Poor tolerance of short, high-intensity or predominantly anaerobic exercise, with exertional myalgia, cramps, stiffness, weakness, myoglobinuria, and episodic rhabdomyolysis | In the 2022 series, anaerobic-exercise intolerance and rhabdomyolysis occurred in **2/2** patients; basal CK was approximately **2–5 times** the reference value | Demonstrated in two young women and consistent with historical cases; tiny, ascertainment-biased samples do not yield population frequencies. (serranolorenzo2022clinicalbiochemicaland pages 2-5, serranolorenzo2022clinicalbiochemicaland pages 5-7) |
| Aggregate phenotype data | Manifestations are predominantly muscular, but recurrent rhabdomyolysis is not universal | Review of 14 historical patients: **6 female and 8 male**; **17/23 manifestations, or 74%,** were muscular. A separate family-level synthesis reported recurrent rhabdomyolysis in **4/14 families** | Aggregates use different denominators—patients, manifestations, and families—and must not be combined as prevalence estimates. (serranolorenzo2022clinicalbiochemicaland pages 7-9, ariceta2021hepaticlactatedehydrogenase pages 2-4) |
| Skin phenotype | Psoriasis-like or psoriasiform dermatitis may occur alone or with myopathy and may vary with stress or season | Present in **1/2** patients in the 2022 series and reported in **8/14 historical families** | The human association is established; proposed causation through NAD⁺ or ATP depletion and inflammatory mediator release is not directly demonstrated. (serranolorenzo2022clinicalbiochemicaland pages 9-11, serranolorenzo2022clinicalbiochemicaland pages 7-9) |
| Exercise-test signature | Non-ischemic forearm exercise produces a flat or nearly flat lactate curve with exaggerated ammonium generation; elevated pyruvate may help distinguish LDHA deficiency from McArdle disease | In the 2022 cases, lactate lacked the normal **4–6-fold** rise; ammonium increased approximately **25–30-fold**, versus a normal **5–10-fold** increase | Demonstrated human biochemical finding in two molecularly confirmed cases; provocative testing requires specialist supervision. (serranolorenzo2022clinicalbiochemicaland pages 2-5, serranolorenzo2022clinicalbiochemicaland pages 7-9, serranolorenzo2022clinicalbiochemicaland pages 5-7) |
| LDH isoenzymes | M-subunit-containing tetramers are absent, leaving LDH-1, the H4 homotetramer composed of LDHB subunits; total plasma LDH may remain normal or slightly increased | Complete absence of M-containing LDH isoenzymes in the 2022 cases | Strong functional evidence that the variants abolish LDHA M-subunit function; total LDH alone is an insensitive screen. (serranolorenzo2022clinicalbiochemicaland pages 5-7, serranolorenzo2022clinicalbiochemicaland pages 7-9) |
| 2022 pathogenic variants | Novel nonsense alleles **LDHA c.410C>A, p.Ser137Ter**, and **c.750G>A, p.Trp250Ter** | Patient 1 was homozygous for p.Ser137Ter; Patient 2 was compound heterozygous for p.Ser137Ter and p.Trp250Ter | Classified as pathogenic in the report; segregation, premature termination, and isoenzyme electrophoresis supported loss of function. A shared haplotype suggests, but does not prove, a founder allele. (serranolorenzo2022clinicalbiochemicaland pages 5-7, serranolorenzo2022clinicalbiochemicaland pages 7-9) |
| Mechanism | Loss of LDHA-mediated pyruvate-to-lactate conversion impairs NAD⁺ regeneration, limits anaerobic glycolytic flux and rapid ATP production, and predisposes active myofibers to energetic failure and injury | Human evidence includes the flat lactate response and loss of M-containing isoenzymes; direct intramuscular NAD⁺ and ATP flux measurements are unavailable | The reaction defect and exercise phenotype are demonstrated; the complete NAD⁺ depletion to ATP failure to rhabdomyolysis chain remains partly inferred. (serranolorenzo2022clinicalbiochemicaland pages 1-2, rai2026drosophilamelanogasterlactate pages 20-24, serranolorenzo2022clinicalbiochemicaland pages 5-7) |
| Epidemiology | The disorder is extremely rare and has been reported in Japanese, Italian, U.S., and Spanish families | A 2021 review identified **14 unique historical patients**; a 2022 report added two affected individuals from two Spanish families | No population-based prevalence, incidence, carrier frequency, or sex ratio is available; published counts are susceptible to underdiagnosis and reporting bias. (serranolorenzo2022clinicalbiochemicaland pages 1-2, ariceta2021hepaticlactatedehydrogenase pages 2-4) |
| Treatment | No approved disease-modifying pharmacotherapy, enzyme replacement, gene therapy, RNA therapy, or validated treatment algorithm was identified | No response-rate or comparative-treatment data are available | Management is supportive and focuses on avoiding intense anaerobic exertion and promptly treating rhabdomyolysis; disease-specific trials and formal guidelines are absent. |
| Clinical trials | No disease-specific therapeutic trial was identified; one observational study plans to assess home lactate and glucose meters in GSD types Ia, Ib, and XI | **NCT07459582**; planned enrollment **10**; approximately 8 hours of hourly measurements | This is not a treatment trial and is not restricted to LDHA-related GSD XI; the registry record was first posted March 10, 2026. (NCT07459582 chunk 1) |
| Prognosis | Case reports suggest a chronic, episodic disorder compatible with survival into adulthood, with morbidity concentrated around exertional attacks and possible skin disease | No survival curves, mortality rate, life-expectancy estimate, renal-failure risk, or validated quality-of-life data are available | Adult survival is inferred from case reports. Acute renal failure is a possible complication of rhabdomyolysis, but its frequency is unknown. (serranolorenzo2022clinicalbiochemicaland pages 1-2) |
| Models | Drosophila **Ldh** loss-of-function mutants exhibit exercise intolerance, reduced mobility, and demand-dependent lethality; muscle and peripheral glial LDH are implicated | Reducing locomotor demand through altered food presentation can rescue viability | This disease-oriented model is reported in a **2026 non-peer-reviewed preprint**, outside the 2023–2024 priority period. Mouse LDHA inhibition and conditional models generally address other diseases and do not fully reproduce congenital human GSD XI. (rai2026drosophilamelanogasterlactate pages 1-5, rai2026drosophilamelanogasterlactate pages 20-24, lai2018specificinhibitionof pages 10-11) |


*Table: Compact knowledge-base summary of LDHA-related GSD XI, separating demonstrated human findings from review aggregates, mechanistic inference, and unavailable evidence. Quantitative estimates retain their original denominators and key ascertainment caveats.*

## 1. Disease information

### Definition and identifiers

The disease is a disorder of terminal anaerobic glycolysis rather than a primary defect of glycogen synthesis or glycogenolysis. It is nevertheless conventionally classified among muscle glycogenoses because symptoms emerge when contracting muscle depends heavily on glycogen-derived glycolytic ATP.

* **Preferred unambiguous name:** LDHA-related glycogen storage disease type XI.
* **OMIM:** **612933**.
* **Orphanet:** **ORPHA:284426**.
* **Causal gene:** **LDHA**; OMIM gene entry **150000**.
* **Chromosomal locus:** **11p15.1**.
* **Synonyms:** glycogenosis type XI; GSD XI/GSD 11; lactate dehydrogenase A deficiency; LDH-A deficiency; lactate dehydrogenase M-subunit deficiency; hereditary LDH-M deficiency; muscle lactate dehydrogenase deficiency; muscle LDH deficiency. (serranolorenzo2022clinicalbiochemicaland pages 1-2, ellingwood2018biochemicalandclinical pages 12-16, kanungo2018glycogenmetabolismand pages 5-6)
* **MONDO:** a disease-specific MONDO identifier was not established by the retrieved evidence and should not be guessed. A database curator should reconcile the current MONDO release against OMIM 612933/ORPHA 284426.
* **MeSH:** no specific LDHA-deficiency descriptor was established; broader indexing under glycogen storage disease, carbohydrate-metabolism inborn errors, metabolic myopathy, rhabdomyolysis, and lactate dehydrogenase is appropriate.
* **ICD:** no validated disease-specific ICD-10/ICD-11 code was identified. A 2026 ClinicalTrials.gov protocol uses **E74.09** for GSD XI, but this registry usage should not be treated as a universally authoritative disease-specific mapping. (NCT07459582 chunk 1)

**Nomenclature warning:** “GSD XI” has also been used for **GLUT2/SLC2A2-deficient Fanconi–Bickel syndrome**. Knowledge bases should therefore store the gene-qualified label “LDHA-related GSD XI” and should not merge it with Fanconi–Bickel syndrome. (ellingwood2018biochemicalandclinical pages 12-16)

The evidence is aggregated disease-level literature and individual published cases/families, not an EHR-derived cohort. The modern primary data are two index cases and their relatives; historical summaries aggregate published cases with substantial reporting bias. (serranolorenzo2022clinicalbiochemicaland pages 5-7, ariceta2021hepaticlactatedehydrogenase pages 2-4)

## 2. Etiology, risk, and protective factors

### Causal factor

The established cause is **biallelic germline LDHA loss of function**. The 2022 pedigrees showed homozygosity or compound heterozygosity in affected individuals, heterozygosity in clinically unaffected relatives, and absence of M-containing LDH isoenzymes, supporting autosomal-recessive causation. (serranolorenzo2022clinicalbiochemicaland pages 5-7)

### Genetic risk factors

A person is at risk when inheriting two pathogenic LDHA alleles. The best-characterized recent variants are:

* **NM-dependent genomic transcript notation:** **c.410C>A (p.Ser137Ter)**, homozygous in one patient.
* **c.410C>A (p.Ser137Ter)** plus **c.750G>A (p.Trp250Ter)**, compound heterozygous in the second.

Both are nonsense/null alleles predicted to truncate the 333-amino-acid protein. Segregation, Sanger confirmation, premature termination, and isoenzyme electrophoresis supported pathogenicity; the report classified them as pathogenic under ACMG criteria. A shared neighboring haplotype suggested a possible founder origin for p.Ser137Ter, but this was not proven epidemiologically. (serranolorenzo2022clinicalbiochemicaland pages 5-7, serranolorenzo2022clinicalbiochemicaland pages 7-9)

Historical reports include a 20-bp exon-6 truncating/deletion allele and other molecularly heterogeneous LDHA mutations. Phenotypic severity can differ despite similar enzyme activity or genotype; no reliable genotype–phenotype relationship has been established. (serranolorenzo2022clinicalbiochemicaland pages 7-9, takahashi1995geneticanalysisof pages 4-4)

Population allele frequencies, carrier frequency, penetrance estimates, and complete ClinVar/gnomAD classifications were not available in the retrieved evidence. Somatic mutation is not the disease mechanism.

### Environmental and lifestyle modifiers

Strenuous, short-duration, high-intensity or anaerobic exercise is the major **trigger**, not the primary cause. It exposes the limited capacity for glycolytic NAD⁺ recycling and can precipitate myalgia, pigmenturia, or rhabdomyolysis. Symptoms may occur in the days following medium-to-high-intensity exertion. Stress and season were reported to modify skin lesions. Pregnancy and sustained uterine contraction have precipitated uterine pain/stiffness in a historical case. (serranolorenzo2022clinicalbiochemicaland pages 9-11, serranolorenzo2022clinicalbiochemicaland pages 1-2, serranolorenzo2022clinicalbiochemicaland pages 2-5)

No toxin, radiation, pollution, smoking, alcohol, occupational exposure, or infectious agent has been shown to cause the disorder. No validated genetic protective allele or modifier gene is known. Avoidance of extreme anaerobic workload is plausibly protective against attacks, but no controlled prevention study exists.

## 3. Phenotypes

| Phenotype | Type and characteristics | Frequency/evidence | Suggested HPO term |
|---|---|---|---|
| Exercise intolerance | Symptom; especially brief, intense anaerobic activity; episodic and workload-dependent | Core finding; 2/2 in the 2022 series | **HP:0003546 Exercise intolerance** |
| Myalgia/muscle pain | Symptom; exertional or post-exertional, variable severity | Common in cases; no patient-level population frequency | **HP:0003326 Myalgia** |
| Muscle cramps/contractures or stiffness | Symptom/sign; precipitated by intense exertion | Historical cases | **HP:0003394 Muscle cramps**; consider **HP:0003552 Muscle stiffness** |
| Rhabdomyolysis | Acute clinical/laboratory event; recurrent and exertional in some patients | 2/2 modern cases; historical synthesis: 4/14 families | **HP:0003201 Rhabdomyolysis** |
| Myoglobinuria/dark urine | Symptom/laboratory sign after exertion | Reported in both modern families and historical cases | **HP:0002913 Myoglobinuria** |
| Hyper-CK-emia | Laboratory abnormality; may be mild at baseline and marked during attacks | Basal CK about 2–5× reference in the two modern cases | **HP:0003236 Elevated circulating creatine kinase concentration** |
| Muscle weakness | Sign; absent in one modern case but reported in the other/historical disease | Variable | **HP:0001324 Muscle weakness** |
| Psoriasiform dermatitis | Cutaneous sign; psoriasis-like, sometimes stress- or season-responsive; may occur with or without myopathy | 1/2 modern cases; 8/14 historical families | **HP:0003765 Psoriasiform dermatitis** |
| Abnormal lactate response | Functional laboratory phenotype: absent/flat exercise-associated lactate rise | 2/2 modern cases | **HP:0011968 Abnormality of circulating lactate concentration**; annotate test context explicitly |
| Exaggerated ammonia response | Functional laboratory abnormality after forearm exercise | About 25–30× increase in the modern cases | **HP:0001987 Hyperammonemia** only with caution; this is transient exercise-induced ammonium elevation, not necessarily resting hyperammonemia |
| Elevated pyruvate after exercise | Laboratory abnormality that may distinguish LDHA deficiency from McArdle disease | Historical/diagnostic literature; frequency unknown | **HP:0011907 Abnormality of circulating pyruvate concentration** |
| Acute kidney injury | Complication secondary to severe rhabdomyolysis | Reported as possible; frequency unknown | **HP:0001919 Acute kidney injury** |
| Uterine pain/stiffness in pregnancy | Smooth-muscle manifestation during labor/pregnancy | Isolated historical report | Use descriptive annotation; no confidently verified specific HPO mapping from retrieved evidence |

The 2022 patients were 17 and 18 years old when characterized, but this does not establish typical onset. One reported no fixed weakness; the other described weakness and delayed symptoms after exercise. Severity and expression vary even among patients with comparable biochemical deficiency. (serranolorenzo2022clinicalbiochemicaland pages 2-5, serranolorenzo2022clinicalbiochemicaland pages 7-9)

Quantitative interpretation requires care. A 2021 review identified 14 historical patients—6 female and 8 male—and counted 23 reported manifestations, 17/23 (74%) of which were muscular. A separate 2022 family-level synthesis reported recurrent rhabdomyolysis in 4/14 and dermatitis in 8/14 families. These denominators represent manifestations, patients, and families and must not be combined into patient prevalence estimates. (serranolorenzo2022clinicalbiochemicaland pages 7-9, ariceta2021hepaticlactatedehydrogenase pages 2-4)

No EQ-5D, SF-36, PROMIS, disability scale, or disease-specific quality-of-life study was found. Likely burdens include restriction of vigorous activity, pain, fear of rhabdomyolysis, emergency care, and dermatologic morbidity, but these have not been formally quantified.

## 4. Genetic and molecular information

**LDHA** encodes the A/M subunit of tetrameric lactate dehydrogenase. LDHA and LDHB subunits form five isoenzymes; skeletal muscle is enriched for the M-containing LDH-4 and LDH-5 forms. The gene contains seven exons and spans approximately 12 kb at 11p15.1. (serranolorenzo2022clinicalbiochemicaland pages 1-2)

The established molecular consequence is loss of function. In the 2022 patients, electrophoresis showed absence of every M-containing tetramer and persistence only of **LDH-1 (H4)**, composed solely of LDHB subunits. Total plasma LDH was normal or only slightly raised, demonstrating why total LDH concentration is an insensitive diagnostic screen. (serranolorenzo2022clinicalbiochemicaland pages 5-7, serranolorenzo2022clinicalbiochemicaland pages 7-9)

No validated dominant-negative, gain-of-function, somatic, mosaic, chromosomal, copy-number, epigenetic, methylation, or imprinting mechanism was found. No disease-modifying gene has been established. The condition lies near an imprinted region of 11p15, but no evidence supports imprinting as its disease mechanism.

Suggested annotations include **HGNC:6540** for LDHA, subject to database verification; GO molecular function **L-lactate dehydrogenase activity**; GO biological processes **glycolytic process**, **NADH oxidation**, **pyruvate metabolic process**, and **lactate metabolic process**; and GO cellular component **cytosol**. Exact GO identifiers should be resolved against the current GO release rather than inferred from names.

## 5. Environmental information

There is no evidence for environmental causation or an infectious trigger. Exercise, physiologic stress, and possibly temperature/season function as exposure-dependent modifiers of manifestations. High-intensity exercise increases ATP demand and dependence on anaerobic glycolysis; the inherited enzyme defect converts this otherwise normal exposure into a risk of muscle injury. (serranolorenzo2022clinicalbiochemicaland pages 9-11, serranolorenzo2022clinicalbiochemicaland pages 2-5)

No evidence supports smoking cessation, alcohol restriction, a specific macronutrient diet, supplements, or vaccination as disease-specific interventions, although general avoidance of dehydration and prompt management during rhabdomyolysis are clinically reasonable.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic LDHA variants lead to** absent or severely reduced functional LDH-A/M subunits.
2. **Loss of M subunits leads to** disappearance of M-containing LDH tetramers in skeletal muscle and blood isoenzyme profiles, leaving LDHB H4 activity. This is demonstrated in molecularly confirmed patients. (serranolorenzo2022clinicalbiochemicaland pages 5-7)
3. **Loss of muscle-type LDH leads to** impaired conversion of pyruvate + NADH to lactate + NAD⁺ during high glycolytic flux.
4. **Impaired NAD⁺ regeneration leads to** restriction of glycolytic throughput and rapid substrate-level ATP production during intense anaerobic contraction; this step is biochemically well grounded but direct intramuscular NAD⁺/ATP flux measurements in patients are unavailable. (serranolorenzo2022clinicalbiochemicaland pages 1-2, rai2026drosophilamelanogasterlactate pages 20-24)
5. **Restricted anaerobic glycolysis leads to** a flat exercise lactate curve and accumulation/diversion of pyruvate. The flat lactate response is demonstrated; the complete pyruvate-flux model is partly inferred. (serranolorenzo2022clinicalbiochemicaland pages 7-9, serranolorenzo2022clinicalbiochemicaland pages 5-7)
6. **Reduced glycolytic ATP availability leads to** compensatory adenylate-nucleotide degradation through AMP deaminase, resulting in exaggerated exercise-induced ammonium release; the 25–30-fold ammonium response is demonstrated, whereas the precise flux partition is inferred. (serranolorenzo2022clinicalbiochemicaland pages 7-9)
7. **Energetic mismatch during contraction leads to** exercise intolerance, myalgia, cramps/stiffness, membrane injury, CK/myoglobin release, and episodic rhabdomyolysis. Severe rhabdomyolysis can secondarily lead to acute kidney injury. (serranolorenzo2022clinicalbiochemicaland pages 1-2, serranolorenzo2022clinicalbiochemicaland pages 2-5)
8. **Branch—skin:** reduced LDHA-dependent NAD⁺/ATP homeostasis in keratinocytes may lead to disturbed calcium handling and release of IL-8, VEGF, and TNF-α, resulting in psoriasiform inflammation. This mechanism is proposed, not directly demonstrated in affected skin. (serranolorenzo2022clinicalbiochemicaland pages 9-11)
9. **Branch—smooth muscle:** increased glycolytic demand during uterine contraction may lead to uterine pain/stiffness and elevated pyruvate; evidence is limited to an isolated pregnancy-associated observation. (serranolorenzo2022clinicalbiochemicaland pages 1-2)

### Cells, tissues, and pathways

The primary affected cell is the **skeletal muscle fiber/myocyte**; suggested Cell Ontology annotation is **skeletal muscle fiber (CL:0000188, verify current release)**. Keratinocytes are implicated by the skin phenotype; smooth-muscle cells may be involved during uterine contraction. The disease is not primarily an mTOR, Wnt, MAPK, or PI3K-AKT signaling disorder. Its upstream lesion is metabolic/redox failure in glycolysis. Secondary inflammatory signaling in skin remains hypothetical.

Recent work refines general lactate biology but is not direct GSD-XI evidence. A 2024 mouse study found that MCT1-mediated lactate transport influences skeletal-muscle mitochondrial biogenesis and TCA flux, underscoring that lactate is a fuel and signaling metabolite rather than simply waste. A 2023 T-cell study showed that altering LDHA/LDHB isoenzyme composition changes glycolysis, NAD⁺/NADH balance, proliferation, and differentiation. These findings support broad roles for isoenzyme balance but cannot be used to assign immune or mitochondrial disease phenotypes to human GSD XI. (liang2016exerciseinduciblelactate pages 1-2)

No disease-specific human transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or multi-omics dataset from 2023–2024 was identified. Human biochemical profiling is currently limited chiefly to CK, LDH isoenzymes, lactate, pyruvate, and ammonium.

## 7. Anatomical structures affected

* **Primary organ/system:** skeletal muscle and muscular system; suggested **UBERON:0001134 skeletal muscle tissue** and **UBERON:0000383 skeletal musculature**, subject to release verification.
* **Secondary tissue:** skin/epidermis, particularly keratinocytes, in the psoriasiform phenotype; suggested **UBERON:0002097 skin of body** and **CL:0000312 keratinocyte**.
* **Possible smooth-muscle site:** uterus/myometrium during pregnancy or labor; evidence is isolated and insufficient to call routine uterine disease.
* **Secondary complication:** kidney injury from myoglobin released during rhabdomyolysis; the kidney is not established as a primary site of LDHA-deficiency pathology.
* **Subcellular compartment:** cytosol, where the terminal glycolytic LDH reaction and redox coupling occur. Mitochondria are downstream users of pyruvate/reducing equivalents but are not the primary defective organelle.
* **Lateralization:** diffuse/bilateral systemic muscle involvement; no consistent unilateral or asymmetric pattern.

## 8. Temporal development

The genetic defect is congenital and lifelong, but clinical manifestations can remain latent until sufficiently intense exertion. Published presentation spans youth and adulthood; the modern cases were evaluated at 17–18 years. The onset pattern is typically acute or subacute after exertion against a chronic inherited background. (serranolorenzo2022clinicalbiochemicaland pages 2-5)

The course is **episodic rather than steadily progressive**: patients may be relatively well between attacks, with recurrent exercise-triggered myalgia, pigmenturia, and rhabdomyolysis. Fixed weakness is variable. Dermatitis may fluctuate with season or stress. No validated stages, progression rate, remission definition, or longitudinal natural-history cohort exists. (serranolorenzo2022clinicalbiochemicaland pages 9-11, serranolorenzo2022clinicalbiochemicaland pages 7-9)

Critical vulnerability windows are periods of high anaerobic demand—sprinting, heavy resistance activity, strenuous unaccustomed exertion, and possibly sustained uterine contraction. Early molecular diagnosis permits trigger education and emergency planning, although benefit has not been quantified.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two known heterozygous parents, standard Mendelian recurrence expectations are 25% affected, 50% carrier, and 25% unaffected/non-carrier per pregnancy, assuming no complicating factors. Heterozygous relatives in the 2022 pedigrees were clinically asymptomatic. (serranolorenzo2022clinicalbiochemicaland pages 5-7)

Penetrance among biallelic individuals cannot be estimated. Expressivity is variable, ranging from predominantly muscle disease to dermatitis, combined disease, or apparently milder manifestations. No anticipation or germline mosaicism has been reported. Consanguinity has occurred in historical families but is not required. (serranolorenzo2022clinicalbiochemicaland pages 7-9, takahashi1995geneticanalysisof pages 4-4)

A 2021 review identified 14 historical patients: 11 from seven Japanese families, one from an Italian family, and two from two U.S. families; six were female and eight male. The 2022 report added two young Spanish women from separate families. These observations show multinational occurrence but do not establish ethnic susceptibility or a sex ratio. (serranolorenzo2022clinicalbiochemicaland pages 1-2, ariceta2021hepaticlactatedehydrogenase pages 2-4)

No population prevalence per 100,000, annual incidence, carrier frequency, founder-population frequency, or geographic registry estimate is available. Published case counts suggest an ultra-rare and probably underdiagnosed disorder.

## 10. Diagnostics

### Practical diagnostic approach

1. **Clinical suspicion:** recurrent exercise intolerance, myalgia, cramps, hyper-CK-emia, pigmenturia, or rhabdomyolysis after short intense exertion, especially with psoriasiform dermatitis.
2. **Baseline/attack laboratories:** CK, creatinine, electrolytes, urinalysis and urine/plasma myoglobin during attacks; total LDH may be normal and cannot exclude disease.
3. **LDH isoenzyme electrophoresis:** a highly informative functional test showing absence of M-containing LDH-2 through LDH-5 and persistence of LDH-1/H4. (serranolorenzo2022clinicalbiochemicaland pages 5-7, serranolorenzo2022clinicalbiochemicaland pages 7-9)
4. **Non-ischemic forearm exercise testing:** molecularly confirmed cases showed a flat lactate response rather than the normal 4–6-fold increase and ammonium increases of approximately 25–30-fold rather than 5–10-fold. Measuring pyruvate may help distinguish LDHA deficiency from McArdle disease, which can also produce a flat lactate curve. Testing should be conducted in a specialist metabolic/neuromuscular setting because exertion can provoke injury. (serranolorenzo2022clinicalbiochemicaland pages 2-5, serranolorenzo2022clinicalbiochemicaland pages 7-9)
5. **Molecular confirmation:** sequence **LDHA**, including exon–intron boundaries; deletion/duplication analysis should follow if sequencing finds fewer than two pathogenic alleles. Segregation testing is appropriate.

A metabolic-myopathy/rhabdomyolysis panel is efficient when the phenotype is nonspecific; the 2022 investigation used a 32-gene panel and excluded common **PYGM** and **CPT2** disease-associated variants before confirming LDHA findings. WES or WGS is reasonable for unresolved cases, but RNA sequencing has no validated routine role. CMA, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing are not first-line tests unless another phenotype suggests them. (serranolorenzo2022clinicalbiochemicaland pages 2-5)

### Differential diagnosis

Important alternatives include **McArdle disease/PYGM (GSD V)**, **phosphofructokinase deficiency/PFKM (GSD VII)**, phosphoglycerate mutase deficiency, other glycolytic defects, **CPT2** and other fatty-acid oxidation disorders, **LPIN1**-related rhabdomyolysis, RYR1-related exertional rhabdomyolysis, mitochondrial myopathy, inflammatory myopathy, and acquired toxic/exertional rhabdomyolysis. A high pyruvate response and LDH isoenzyme pattern favor LDHA deficiency over McArdle disease. (serranolorenzo2022clinicalbiochemicaland pages 7-9)

No standardized society diagnostic criteria or validated diagnostic score exists. There is no routine biochemical newborn screening program. Targeted genomic newborn screening could technically detect biallelic LDHA variants, but evidence of clinical utility is absent; the retrieved BabyDetect protocol screened broad panels of treatable diseases and did not establish LDHA-deficiency-specific outcomes. (NCT05687474 chunk 1)

## 11. Outcome and prognosis

Survival into adulthood is documented, and available cases suggest that the dominant morbidity is episodic rather than relentlessly degenerative. Nevertheless, attacks can involve severe rhabdomyolysis, myoglobinuria, and possible acute renal failure. The frequency of chronic weakness, renal sequelae, hospitalization, or disability is unknown. (serranolorenzo2022clinicalbiochemicaland pages 1-2)

No 5- or 10-year survival estimate, life expectancy, mortality rate, disease-specific death count, validated prognostic model, or prognostic biomarker exists. Attack severity, CK/myoglobin burden, renal function, hydration, and delay to treatment are clinically plausible acute prognostic factors but have not been validated in this disease. Genotype does not reliably predict phenotype. (serranolorenzo2022clinicalbiochemicaland pages 7-9)

## 12. Treatment

No approved disease-modifying treatment or evidence-based therapeutic algorithm was identified. Management is extrapolated from metabolic myopathy and rhabdomyolysis practice:

* Avoid or carefully titrate brief maximal/anaerobic exertion and unaccustomed strenuous exercise.
* Develop an individualized activity plan with metabolic/neuromuscular and rehabilitation specialists; activity should not be indiscriminately eliminated because controlled evidence defining safe training is absent.
* Stop activity when severe pain, stiffness, weakness, or dark urine occurs.
* During suspected rhabdomyolysis, urgently assess CK, renal function, potassium and other electrolytes, urine output, and myoglobin; provide hydration and standard acute management as clinically indicated.
* Treat psoriasis-like dermatitis with dermatology input; no LDHA-specific dermatologic regimen or response rate is known.
* Provide genetic counseling and cascade testing.

Suggested NCIT intervention concepts include **Genetic Counseling**, **Genetic Testing**, **Physical Therapy**, **Supportive Care**, and **Intravenous Fluid Therapy**; exact NCIT codes should be verified against the current thesaurus.

There is no established enzyme replacement, small molecule, gene replacement, genome editing, cell therapy, ASO, siRNA, or mRNA therapy for congenital LDHA deficiency. Importantly, hepatic LDHA inhibition is being developed for primary hyperoxaluria; that strategy models partial tissue-selective suppression and is not a treatment for systemic LDHA deficiency. (lai2018specificinhibitionof pages 10-11, ariceta2021hepaticlactatedehydrogenase pages 2-4)

No disease-specific therapeutic ClinicalTrials.gov study was found. **NCT07459582**, first posted 10 March 2026, is an observational study of home lactate and glucose meters in ten participants across GSD Ia, Ib, and XI; it is not a treatment trial and is not restricted to LDHA deficiency. (NCT07459582 chunk 1)

## 13. Prevention

Because the causal variants are inherited, primary prevention by lifestyle or vaccination is not possible.

* **Primary reproductive prevention/options:** carrier testing in relatives, partner testing where appropriate, prenatal diagnosis, and preimplantation genetic testing when familial pathogenic variants are known. These are options requiring nondirective genetic counseling, not recommendations that affected pregnancies be avoided.
* **Secondary prevention:** early diagnosis after characteristic exertional episodes; cascade testing of relatives; anticipatory education before severe attacks.
* **Tertiary prevention:** avoid individually identified high-risk exertion, maintain hydration during illness/exercise, recognize pigmenturia promptly, and institute early rhabdomyolysis/renal monitoring.

No prophylactic drug, immunization, public-health screening recommendation, or controlled behavioral-prevention trial exists.

## 14. Other species and natural disease

No naturally occurring veterinary analogue, breed association, zoonotic potential, or cross-species transmission was identified. The disease is genetic and noncommunicable. Orthologous LDH genes are deeply conserved across animals, supporting comparative study, but conservation alone does not establish naturally occurring disease in another species.

Suggested taxonomy annotations include **Homo sapiens, NCBI Taxon 9606** for the natural human disease, **Mus musculus, Taxon 10090** for experimental mouse work, and **Drosophila melanogaster, Taxon 7227** for the emerging invertebrate model. Exact ortholog gene identifiers should be imported directly from NCBI/Alliance releases.

## 15. Model organisms

No established animal model was found that fully reproduces the human congenital syndrome and has been validated for preclinical therapy.

* **Drosophila Ldh loss of function:** a 2026 bioRxiv preprint reported reduced mobility, exercise intolerance, and food-consistency-dependent lethality. Tissue-specific work implicated muscle and peripheral glia; reducing the mechanical demand of feeding rescued viability. This supports a demand-dependent neuromuscular-energy model, but it is a non-peer-reviewed larval fly study and postdates the requested 2023–2024 priority window. It does not establish the human skin or rhabdomyolysis phenotype. (rai2026drosophilamelanogasterlactate pages 1-5, rai2026drosophilamelanogasterlactate pages 20-24)
* **Mouse LDHA inhibition/conditional deletion:** available models primarily investigate liver-directed inhibition in primary hyperoxaluria, cardiac stress, cancer, or other metabolic questions. They clarify tissue-specific LDHA biology but are not validated GSD-XI models. Liver-directed siRNA studies measure lactate/pyruvate and exercise effects while intentionally sparing skeletal muscle, limiting disease relevance. (lai2018specificinhibitionof pages 10-11, dai2020lactatedehydrogenasea pages 11-12)
* **Cellular systems:** LDHA knockout cells demonstrate effects on glycolysis and redox balance in several biological contexts, but no patient-derived myotube, iPSC-muscle, skin organoid, or CRISPR-corrected GSD-XI platform was identified in the retrieved literature.

Priority model-development needs are patient-derived myotubes and keratinocytes, conditional skeletal-muscle LDHA knockout models, isotope-resolved NAD⁺/NADH and pyruvate/lactate flux studies, and exercise paradigms that quantify CK, myoglobin, histologic injury, renal complications, and rescue.

## Recent developments and expert assessment

The most disease-specific modern advance remains the **11 October 2022** Genes report, which added two Spanish families, two nonsense alleles, segregation data, a reproducible exercise-test signature, and functional isoenzyme confirmation. Its abstract states: **“LDH-A deficiency is an autosomal recessive disorder (glycogenosis type XI, OMIM#612933) caused by mutations in the LDHA gene,”** and reports **“two young adult female patients presenting with intolerance to anaerobic exercise, episodes of rhabdomyolysis, and, in one of the patients, psoriasis-like dermatitis.”** It concludes that **“a flat lactate curve on the forearm exercise test, along with the clinical combination of myopathy and psoriatic-like dermatitis, can also lead to the diagnosis.”** DOI: https://doi.org/10.3390/genes13101835. A PMID was not present in the retrieved record and is therefore not supplied. (serranolorenzo2022clinicalbiochemicaland pages 1-2, serranolorenzo2022clinicalbiochemicaland pages 9-11)

The authoritative 2023 Nature Reviews Disease Primers overview places GSDs within disorders of glycogen handling and emphasizes their organ-specific heterogeneity, but the retrieved evidence did not provide new GSD-XI patient data. Likewise, recent 2023–2024 work on muscle fatigue, lactate transport, mitochondrial adaptation, and LDH isoenzyme balance improves biological context rather than changing diagnosis or treatment. Thus, the current expert interpretation should remain conservative: the biochemical lesion and exercise phenotype are compelling, but epidemiology, penetrance, natural history, optimal exercise prescription, skin mechanism, and therapy remain unresolved.

## Evidence limitations

The disease literature consists mainly of isolated families, retrospective descriptions, and reviews that reuse the same cases. Frequencies are highly vulnerable to ascertainment and publication bias. Family-level counts cannot be interpreted as patient prevalence; normal total LDH does not exclude disease; and mechanistic claims about NAD⁺, ATP, calcium, or inflammatory mediators should be labeled inferred unless measured in affected tissue. No verified disease-specific PMID was available from the retrieved full-text records, so DOI URLs and publication dates are supplied rather than fabricated PMID mappings.

References

1. (serranolorenzo2022clinicalbiochemicaland pages 5-7): Pablo Serrano-Lorenzo, María Rabasa, Jesús Esteban, Irene Hidalgo Mayoral, Cristina Domínguez-González, Agustín Blanco-Echevarría, Rocío Garrido-Moraga, Alejandro Lucia, Alberto Blázquez, Juan C. Rubio, Carmen Palma-Milla, Joaquín Arenas, and Miguel A. Martín. Clinical, biochemical, and molecular characterization of two families with novel mutations in the ldha gene (gsd xi). Oct 2022. URL: https://doi.org/10.3390/genes13101835, doi:10.3390/genes13101835. This article has 10 citations.

2. (serranolorenzo2022clinicalbiochemicaland pages 1-2): Pablo Serrano-Lorenzo, María Rabasa, Jesús Esteban, Irene Hidalgo Mayoral, Cristina Domínguez-González, Agustín Blanco-Echevarría, Rocío Garrido-Moraga, Alejandro Lucia, Alberto Blázquez, Juan C. Rubio, Carmen Palma-Milla, Joaquín Arenas, and Miguel A. Martín. Clinical, biochemical, and molecular characterization of two families with novel mutations in the ldha gene (gsd xi). Oct 2022. URL: https://doi.org/10.3390/genes13101835, doi:10.3390/genes13101835. This article has 10 citations.

3. (serranolorenzo2022clinicalbiochemicaland pages 7-9): Pablo Serrano-Lorenzo, María Rabasa, Jesús Esteban, Irene Hidalgo Mayoral, Cristina Domínguez-González, Agustín Blanco-Echevarría, Rocío Garrido-Moraga, Alejandro Lucia, Alberto Blázquez, Juan C. Rubio, Carmen Palma-Milla, Joaquín Arenas, and Miguel A. Martín. Clinical, biochemical, and molecular characterization of two families with novel mutations in the ldha gene (gsd xi). Oct 2022. URL: https://doi.org/10.3390/genes13101835, doi:10.3390/genes13101835. This article has 10 citations.

4. (ariceta2021hepaticlactatedehydrogenase pages 2-4): Gema Ariceta, Kelly Barrios, Bob D. Brown, Bernd Hoppe, Ralf Rosskamp, and Craig B. Langman. Hepatic lactate dehydrogenase a: an rna interference target for the treatment of all known types of primary hyperoxaluria. Apr 2021. URL: https://doi.org/10.1016/j.ekir.2021.01.029, doi:10.1016/j.ekir.2021.01.029. This article has 43 citations and is from a peer-reviewed journal.

5. (ellingwood2018biochemicalandclinical pages 12-16): Sara S. Ellingwood and Alan Cheng. Biochemical and clinical aspects of glycogen storage diseases. The Journal of endocrinology, 238 3:R131-R141, Sep 2018. URL: https://doi.org/10.1530/joe-18-0120, doi:10.1530/joe-18-0120. This article has 184 citations.

6. (kanungo2018glycogenmetabolismand pages 5-6): Shibani Kanungo, Kimberly Wells, Taylor Tribett, and Areeg El-Gharbawy. Glycogen metabolism and glycogen storage disorders. Dec 2018. URL: https://doi.org/10.21037/atm.2018.10.59, doi:10.21037/atm.2018.10.59. This article has 271 citations.

7. (serranolorenzo2022clinicalbiochemicaland pages 2-5): Pablo Serrano-Lorenzo, María Rabasa, Jesús Esteban, Irene Hidalgo Mayoral, Cristina Domínguez-González, Agustín Blanco-Echevarría, Rocío Garrido-Moraga, Alejandro Lucia, Alberto Blázquez, Juan C. Rubio, Carmen Palma-Milla, Joaquín Arenas, and Miguel A. Martín. Clinical, biochemical, and molecular characterization of two families with novel mutations in the ldha gene (gsd xi). Oct 2022. URL: https://doi.org/10.3390/genes13101835, doi:10.3390/genes13101835. This article has 10 citations.

8. (serranolorenzo2022clinicalbiochemicaland pages 9-11): Pablo Serrano-Lorenzo, María Rabasa, Jesús Esteban, Irene Hidalgo Mayoral, Cristina Domínguez-González, Agustín Blanco-Echevarría, Rocío Garrido-Moraga, Alejandro Lucia, Alberto Blázquez, Juan C. Rubio, Carmen Palma-Milla, Joaquín Arenas, and Miguel A. Martín. Clinical, biochemical, and molecular characterization of two families with novel mutations in the ldha gene (gsd xi). Oct 2022. URL: https://doi.org/10.3390/genes13101835, doi:10.3390/genes13101835. This article has 10 citations.

9. (rai2026drosophilamelanogasterlactate pages 20-24): Madhulika Rai, Shefali A. Shefali, Jason P. Tourigny, Minseo Kim, Travis Nemkov, Angelo D’Alessandro, and Jason M. Tennessen. <i>drosophila melanogaster</i> lactate dehydrogenase deficiency recapitulates the exercise intolerance of human glycogen storage disease type xi. Jul 2026. URL: https://doi.org/10.64898/2026.07.09.736989, doi:10.64898/2026.07.09.736989. This article has 0 citations.

10. (NCT07459582 chunk 1):  Accuracy of Home Lactate Meter and Accu-chek Glucometer in Patients With Glycogen Storage Disease. Connecticut Children's Medical Center. 2026. ClinicalTrials.gov Identifier: NCT07459582

11. (rai2026drosophilamelanogasterlactate pages 1-5): Madhulika Rai, Shefali A. Shefali, Jason P. Tourigny, Minseo Kim, Travis Nemkov, Angelo D’Alessandro, and Jason M. Tennessen. <i>drosophila melanogaster</i> lactate dehydrogenase deficiency recapitulates the exercise intolerance of human glycogen storage disease type xi. Jul 2026. URL: https://doi.org/10.64898/2026.07.09.736989, doi:10.64898/2026.07.09.736989. This article has 0 citations.

12. (lai2018specificinhibitionof pages 10-11): Chengjung Lai, Natalie Pursell, Jessica Gierut, Utsav Saxena, Wei Zhou, Michael Dills, Rohan Diwanji, Chaitali Dutta, Martin Koser, Naim Nazef, Rachel Storr, Boyoung Kim, Cristina Martin-Higueras, Eduardo Salido, Weimin Wang, Marc Abrams, Henryk Dudek, and Bob D. Brown. Specific inhibition of hepatic lactate dehydrogenase reduces oxalate production in mouse models of primary hyperoxaluria. Aug 2018. URL: https://doi.org/10.1016/j.ymthe.2018.05.016, doi:10.1016/j.ymthe.2018.05.016. This article has 133 citations and is from a highest quality peer-reviewed journal.

13. (takahashi1995geneticanalysisof pages 4-4): Yoshitomo TAKAHASHI, Hiroaki MIYAJIMA, and Eizo KANEKO. Genetic analysis of a family of lactate dehydrogenase a subunit deficiency. Internal medicine, 34 5:326-9, May 1995. URL: https://doi.org/10.2169/internalmedicine.34.326, doi:10.2169/internalmedicine.34.326. This article has 18 citations and is from a peer-reviewed journal.

14. (liang2016exerciseinduciblelactate pages 1-2): Xijun Liang, Lin Liu, Tingting Fu, Qian Zhou, Danxia Zhou, Liwei Xiao, Jing Liu, Yan Kong, Hui Xie, Fanchao Yi, Ling Lai, Rick B. Vega, Daniel P. Kelly, Steven R. Smith, and Zhenji Gan. Exercise inducible lactate dehydrogenase b regulates mitochondrial function in skeletal muscle. Dec 2016. URL: https://doi.org/10.1074/jbc.m116.749424, doi:10.1074/jbc.m116.749424. This article has 132 citations and is from a domain leading peer-reviewed journal.

15. (NCT05687474 chunk 1): Laurent Servais. Baby Detect : Genomic Newborn Screening. Centre Hospitalier Universitaire de Liege. 2022. ClinicalTrials.gov Identifier: NCT05687474

16. (dai2020lactatedehydrogenasea pages 11-12): Chongshan Dai, Qinfeng Li, Herman I. May, Chao Li, Guangyu Zhang, Gaurav Sharma, A. Dean Sherry, Craig R. Malloy, Chalermchai Khemtong, Yuannyu Zhang, Yingfeng Deng, Thomas G. Gillette, Jian Xu, David T. Scadden, and Zhao V. Wang. Lactate dehydrogenase a governs cardiac hypertrophic growth in response to hemodynamic stress. Cell reports, 32:108087-108087, Sep 2020. URL: https://doi.org/10.1016/j.celrep.2020.108087, doi:10.1016/j.celrep.2020.108087. This article has 119 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Glycogen_Storage_Disease_Due_To_Lactate_Dehydrogenase_M-subunit_Deficiency-deep-research-falcon_artifacts/artifact-00.md)

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
| Terms checked | 20 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

18 of 20 terms resolved to a current term; the rest could not be looked up either way.
