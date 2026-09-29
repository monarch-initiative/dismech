---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T12:50:03.554978'
end_time: '2026-09-04T13:03:42.256777'
duration_seconds: 818.7
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Epiphyseal dysplasia multiple with myopia and conductive deafness,
    EDMMD, OMIM 132450, also called Stickler dysplasia with brachydactyly, caused
    by the heterozygous COL2A1 arginine-to-cysteine substitution p.Arg704Cys in exon
    39
  mondo_id: MONDO:0007562
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
reference_validation:
  total_references: 8
  verified: 7
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.125
  relevance_assessed: 7
  on_topic: 4
  unresolved_references:
  - DOI:10.1002/(sici)1096-8628(19981102)80:1
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 41
  verified: 40
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0007562
    reported_labels:
    - if available
    ontology_label: multiple epiphyseal dysplasia, Beighton type
  obsolete_terms:
  - term_id: GO:0062023
    ontology_label: obsolete collagen-containing extracellular matrix
    replaced_by: GO:0031012
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Multiple_Epiphyseal_Dysplasia_Beighton_Type-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Epiphyseal dysplasia multiple with myopia and conductive deafness, EDMMD, OMIM 132450, also called Stickler dysplasia with brachydactyly, caused by the heterozygous COL2A1 arginine-to-cysteine substitution p.Arg704Cys in exon 39
- **MONDO ID:** MONDO:0007562 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Epiphyseal dysplasia multiple with myopia and conductive deafness, EDMMD, OMIM 132450, also called Stickler dysplasia with brachydactyly, caused by the heterozygous COL2A1 arginine-to-cysteine substitution p.Arg704Cys in exon 39** covering all of the
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
- **Disease Name:** Epiphyseal dysplasia multiple with myopia and conductive deafness, EDMMD, OMIM 132450, also called Stickler dysplasia with brachydactyly, caused by the heterozygous COL2A1 arginine-to-cysteine substitution p.Arg704Cys in exon 39
- **MONDO ID:** MONDO:0007562 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Epiphyseal dysplasia multiple with myopia and conductive deafness, EDMMD, OMIM 132450, also called Stickler dysplasia with brachydactyly, caused by the heterozygous COL2A1 arginine-to-cysteine substitution p.Arg704Cys in exon 39** covering all of the
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


# Epiphyseal dysplasia, multiple, with myopia and deafness (EDMMD): research report

## Executive summary and evidence boundaries

EDMMD (OMIM 132450), also called **multiple epiphyseal dysplasia with myopia and deafness**, **Stickler-like syndrome with brachydactyly**, or **Stickler dysplasia with brachydactyly**, is an exceptionally rare, autosomal-dominant type-II collagenopathy associated with heterozygous **COL2A1 p.Arg704Cys**. The defining evidence consists of one South African Afrikaner family with four affected members and two subsequently reported unrelated probands—approximately six directly characterized individuals. Consequently, exact prevalence, penetrance, long-term prognosis, and treatment-response estimates are unavailable. Findings from ordinary COL2A1-related Stickler syndrome are clinically useful but must be treated as extrapolation, not as EDMMD-specific evidence. (hoornaert2006thephenotypicspectrum pages 2-4, ballo1998sticklerlikesyndromedue pages 1-3)

| Domain | Exact-variant finding | Evidence base/sample | Confidence or caveat |
|---|---|---|---|
| Identity / variant | EDMMD (OMIM 132450), also described as “Stickler-like syndrome” or “Stickler dysplasia with brachydactyly,” is associated with heterozygous **COL2A1 p.Arg704Cys (R704C)** in the collagen II triple helix. The original report used **C2503T, exon 39**; later transcript-based sources may number the nucleotide differently. | Defining Afrikaner pedigree plus later genotype–phenotype series (ballo1998sticklerlikesyndromedue pages 1-3, ballo1998sticklerlikesyndromedue pages 3-5, hoornaert2006thephenotypicspectrum pages 2-4) | **High** for the amino-acid substitution and phenotype association; nucleotide/exon notation must be normalized against the laboratory’s reference transcript before database entry. |
| Inheritance | Autosomal dominant segregation: an affected mother and three affected children; an unaffected child and the mother’s parents/siblings were normal. The variant cosegregated without exception and was absent from unaffected relatives and 54 controls. | Four affected relatives in one family; two later unrelated R704C probands had no affected relatives reported (ballo1998sticklerlikesyndromedue pages 1-3, ballo1998sticklerlikesyndromedue pages 3-5, hoornaert2006thephenotypicspectrum pages 2-4) | **High** for autosomal dominant inheritance; exact penetrance cannot be estimated from these small samples. |
| Ocular phenotype | Early severe/high myopia is characteristic. The original four had myopia; cataracts and asteroid hyalosis were variable. Two later probands had approximately −15 to −18 D myopia, and one developed retinal detachment in childhood. | Four-person pedigree plus two unrelated probands; literature summary reported myopia in 4/4 of the original family (hoornaert2006thephenotypicspectrum pages 2-4, hoornaert2006thephenotypicspectrum pages 5-6, ballo1998sticklerlikesyndromedue pages 1-3) | **High** for severe myopia; **moderate/low** for exact frequencies of cataract, vitreous changes, retinal thinning, and detachment because only about six directly described individuals are available. |
| Auditory phenotype | Bilateral **conductive deafness** predominated in the original family; the two later R704C probands were reported with **sensorineural hearing loss**, demonstrating either variable auditory expression or differences in ascertainment/classification. | Four original relatives and two later unrelated patients (hoornaert2006thephenotypicspectrum pages 2-4, ballo1998sticklerlikesyndromedue pages 1-3) | **High** that hearing loss belongs to the phenotype; hearing-loss type is **variable**, so “conductive deafness” should not be treated as invariant. |
| Skeletal / digital phenotype | Mild generalized epiphyseal dysplasia, platyspondyly, flattened epiphyses, broad femoral necks, small squared iliac wings, and short metacarpals/phalanges. Brachydactyly/stubby digits with short nails is especially characteristic; stature ranges from normal to about −2 SD. | Original four-person family and two unrelated probands with detailed radiographs (hoornaert2006thephenotypicspectrum pages 2-4, hoornaert2006thephenotypicspectrum pages 5-6, ballo1998sticklerlikesyndromedue pages 1-3) | **High** for brachydactyly and epiphyseal/vertebral dysplasia; **moderate** for short stature and arthropathy because expression is variable and longitudinal data are sparse. |
| Mechanism | R704C replaces a basic arginine with cysteine in the Gly-X-Y triple-helical domain. The proposed mechanism is inefficient secretion and incorporation of structurally abnormal collagen II into extracellular matrix, disrupting fibril interactions; abnormal disulfide-linked dimers/trimers were demonstrated for analogous Arg→Cys collagen-II substitutions. | Human segregation plus biochemical analogy and mechanistic interpretation in the defining paper (hoornaert2006thephenotypicspectrum pages 5-6, ballo1998sticklerlikesyndromedue pages 3-5) | **Moderate/inferred** dominant-negative mechanism: no direct R704C cell, cartilage, secretion, ER-stress, or fibrillogenesis assay was reported. Canonical cytotoxic unfolded-protein-response activation should not be assumed. |
| Epidemiology | No population prevalence, incidence, sex ratio, carrier frequency, founder frequency, or geographic distribution estimate is available. Published direct evidence comprises one South African family and two later unrelated patients. | Approximately six directly described affected individuals across the defining and later studies (hoornaert2006thephenotypicspectrum pages 2-4, ballo1998sticklerlikesyndromedue pages 1-3) | **Very low precision**; the disorder is ultra-rare, but “ultra-rare” is qualitative rather than a measured prevalence. The Afrikaner pedigree alone does not establish a founder effect. |
| Management | No R704C-specific therapeutic trials or outcome studies exist. Management is phenotype-directed: urgent vitreoretinal surveillance, refractive correction, audiology and middle-ear assessment, hearing support, skeletal monitoring, pain/physical therapy, and orthopedic intervention when indicated. Retinal prophylaxis may be discussed at an expert Stickler center. | Extrapolated from type-II collagen disorder guidance and broader COL2A1/Stickler evidence; retrospective prophylaxis data show markedly reduced detachment risk, but not specifically for R704C (savarirayan2019bestpracticeguidelines pages 8-10, snead2020therapeuticanddiagnostic pages 3-5, savarirayan2019bestpracticeguidelines pages 2-3) | **Guideline-supported but extrapolative**. Individual retinal anatomy and genotype should guide prophylaxis; randomized evidence and variant-specific response rates are unavailable. |
| Recent research | No R704C-specific 2023–2024 clinical or mechanistic study was identified. A 2023 family study reinforced mutation-specific COL2A1 expressivity, while 2024 iPSC-cartilage studies of other COL2A1 variants advanced investigation of defective procollagen folding, secretion, and matrix deposition. | Broader COL2A1 studies, not R704C; a Stickler scleral-buckle trial was withdrawn with enrollment 0, and a prospective laser trial began after 2024 (jacobson2023characteristicsofa pages 1-2, yammine2024erprocollagenstoragea pages 30-33, NCT04465188 chunk 1, NCT07146516 chunk 1) | **Indirect/emerging**. These platforms and trials are relevant to future research but do not establish R704C biomarkers, disease-modifying therapy, or clinical efficacy. |


*Table: Compact assessment of the evidence supporting COL2A1 p.Arg704Cys–associated EDMMD, separating exact-variant findings from broader type II collagenopathy and Stickler-syndrome extrapolation.*

## 1. Disease information

### Definition

EDMMD is a Mendelian connective-tissue disorder combining early severe myopia, hearing impairment, mild generalized epiphyseal/spondyloepiphyseal dysplasia, characteristic flat facies, and brachydactyly. The original family was initially classified as dominant multiple epiphyseal dysplasia with myopia and deafness; molecular diagnosis established it as a type-II collagenopathy overlapping Stickler syndrome type 1, but with digital shortening atypical of classical Stickler syndrome. (ballo1998sticklerlikesyndromedue pages 1-3, ballo1998sticklerlikesyndromedue pages 3-5)

The defining 1998 abstract states: **“Ocular problems and conductive deafness predominate, while skeletal changes resemble those of a mild form of multiple epiphyseal dysplasia (MED).”** It further notes that, **“In distinction to the classical form of Stickler syndrome, the affected persons have stubby digits.”** (ballo1998sticklerlikesyndromedue pages 1-3)

### Identifiers and synonyms

- **OMIM:** 132450, EDMMD.
- **MONDO:** the user-supplied **MONDO:0007562** should be verified against the current MONDO release before production ingestion. Open Targets currently maps broader Stickler syndrome to MONDO:0019354 and Stickler syndrome type 1 to MONDO:0007160, illustrating that EDMMD and broader Stickler concepts should not be collapsed automatically. (OpenTargets Search: Stickler syndrome,multiple epiphyseal dysplasia-COL2A1)
- **Gene-associated broader concept:** Stickler syndrome type 1, usually COL2A1-related.
- **Orphanet:** no EDMMD-specific Orpha number was established from the retrieved evidence.
- **ICD-10/ICD-11 and MeSH:** no unique EDMMD code/descriptor was identified. Coding generally requires broader categories such as skeletal dysplasia, Stickler syndrome, myopia, hearing loss, and retinal disease.
- **Synonyms:** epiphyseal dysplasia, multiple, with myopia and conductive deafness; multiple epiphyseal dysplasia with myopia and deafness; Stickler-like syndrome; Stickler syndrome/dysplasia with brachydactyly.

The evidence is **aggregated disease-level literature derived from family examinations and research sequencing**, not EHR-scale or population-registry data.

## 2. Etiology

### Causal factor

The established initiating lesion is a **heterozygous germline COL2A1 missense variant producing p.Arg704Cys** in the type-II procollagen triple-helical domain. The original publication described **C2503T in exon 39**; later sources have used different cDNA numbering, including c.2110C>T. These notations likely reflect historical transcript/protein conventions and must not be interchanged without transcript normalization. The stable knowledge-base representation should retain p.Arg704Cys and attach cDNA nomenclature only after validation against a specified RefSeq transcript. (snead1999clinicalandmolecular pages 3-4, hoornaert2006thephenotypicspectrum pages 5-6, ballo1998sticklerlikesyndromedue pages 3-5)

In the original family, the exon-39 change cosegregated with every affected tested individual, was absent from unaffected relatives, and was absent from 54 Afrikaner controls. In the later series, arginine-to-cysteine variants were absent from unaffected relatives and 100 controls. (hoornaert2006thephenotypicspectrum pages 2-4, ballo1998sticklerlikesyndromedue pages 3-5)

### Risk factors

- **Primary genetic risk:** carrying the heterozygous p.Arg704Cys allele.
- **Family history:** an affected heterozygous parent implies a theoretical 50% transmission probability per pregnancy.
- **Other susceptibility or modifier loci:** none demonstrated for EDMMD.
- **Environmental, lifestyle, infectious, toxic, occupational, age, or sex risk factors for disease occurrence:** none established. These factors do not cause this germline collagenopathy.
- **Secondary injury risks:** ocular trauma may plausibly increase retinal-break risk in a structurally susceptible eye, while high-impact loading may aggravate symptomatic joints, but neither interaction has been studied specifically in p.Arg704Cys carriers.

### Protective factors and gene–environment interaction

No genetic protective alleles, dietary factors, drugs, or environmental exposures are known to prevent expression. Early retinal surveillance, refractive correction, hearing treatment, and joint-preserving activity reduce complications rather than prevent the genotype. No EDMMD-specific gene–environment study exists.

## 3. Phenotypes

The frequency denominators below are tiny and subject to ascertainment bias.

### Ocular

- **Severe early-onset myopia**—clinical sign/refractive abnormality; characteristic and probably highly penetrant in reported patients. The four original relatives had early myopia; two unrelated boys had approximately −16.5/−18 D and −15/−15 D. Suggested HPO: **Myopia (HP:0000545)** and, where supported, **High myopia (HP:0011003)**. It is chronic and vision-limiting but refractively treatable. (hoornaert2006thephenotypicspectrum pages 2-4, ballo1998sticklerlikesyndromedue pages 1-3)
- **Retinal detachment**—sight-threatening complication; documented in childhood in one later R704C patient. The literature summary also records retinal thinning in the original family. Suggested HPO: **Retinal detachment (HP:0000541)** and **Retinal thinning**. Exact R704C lifetime risk is unknown. (hoornaert2006thephenotypicspectrum pages 2-4, hoornaert2006thephenotypicspectrum pages 5-6)
- **Cataract and asteroid hyalosis**—variable in the original family; the literature table reports cataract, asteroid hyalosis, and retinal thinning in 4/4, but the narrative calls cataract and asteroid hyalosis variable, so the narrative/table discrepancy should be retained rather than converted into a firm 100% frequency. Suggested HPO: **Cataract (HP:0000518)** and **Asteroid hyalosis (HP:0007968)**. (hoornaert2006thephenotypicspectrum pages 5-6, ballo1998sticklerlikesyndromedue pages 1-3)
- **Quality-of-life impact:** severe refractive error and retinal detachment can impair education, mobility, driving, and independence. No EDMMD-specific EQ-5D, SF-36, PROMIS, or vision-related quality-of-life data exist.

For context only, a systematic review of broader Stickler syndrome included 2,324 patients: myopia occurred in 83%, retinal detachment in 45%, cataract in 36% of type-1 disease, glaucoma in 10%, blindness in 6%, and unilateral vision loss in 10%. First detachment generally occurred in the second decade in type-1 Stickler syndrome. These are **not p.Arg704Cys-specific frequencies**. (snead2020therapeuticanddiagnostic pages 3-5)

### Auditory

- **Hearing loss**—reported in all directly described groups, but type varies. The original four relatives had bilateral **conductive deafness**; the two later unrelated probands had bilateral **sensorineural hearing loss**. Suggested HPO: **Hearing impairment (HP:0000365)**, **Conductive hearing impairment (HP:0000405)**, and **Sensorineural hearing impairment (HP:0000407)**. This inconsistency may reflect genuine variability, age-dependent middle-ear disease, or ascertainment/classification differences. (hoornaert2006thephenotypicspectrum pages 2-4, ballo1998sticklerlikesyndromedue pages 1-3)
- Functional impact can be substantial when hearing impairment coexists with severe visual disease. No EDMMD-specific speech/language or quality-of-life measurements are available.

In broader COL2A1 Stickler disease, approximately half have usually mild high-frequency sensorineural loss; temporary conductive loss is common in young children with middle-ear/orofacial disease. Across Stickler syndromes, hearing loss was estimated at 63%, and formal testing detects more disease than subjective reporting. These are extrapolations. (acke2022hearinglossin pages 1-2)

### Skeletal, growth, and craniofacial

- **Brachydactyly/stubby digits and short nails**—highly characteristic; radiographs show short metacarpals and phalanges, mildly flattened/broad epiphyses, and generalized shortening of tubular hand bones. Suggested HPO: **Brachydactyly (HP:0001156)**, **Short metacarpal (HP:0010049)**, and **Short phalanx of finger**. (hoornaert2006thephenotypicspectrum pages 2-4, ballo1998sticklerlikesyndromedue pages 1-3)
- **Multiple epiphyseal dysplasia**—flattened/dysplastic knee epiphyses, mildly flattened capital femoral epiphyses, slightly enlarged knee/ankle epiphyses, broad femoral necks, horizontal acetabular roofs, and small squared iliac wings. Suggested HPO: **Epiphyseal dysplasia (HP:0002656)**, **Flattened femoral epiphysis**, **Broad femoral neck**, and **Coxa valga (HP:0002673)** where documented. (hoornaert2006thephenotypicspectrum pages 2-4, hoornaert2006thephenotypicspectrum pages 5-6)
- **Platyspondyly**—mild to marked, with increased anteroposterior diameter, anterior vertebral tonguing, and endplate indentations. Suggested HPO: **Platyspondyly (HP:0000926)** and **Irregular vertebral endplates**. (hoornaert2006thephenotypicspectrum pages 2-4)
- **Prominent/hypermobile joints and arthropathy**—present in some, absent in another later patient; natural history is inadequately characterized. Suggested HPO: **Joint hypermobility (HP:0001382)**, **Prominent joints**, **Arthralgia (HP:0002829)**, and **Early-onset osteoarthritis (HP:0002758)** if clinically confirmed. (hoornaert2006thephenotypicspectrum pages 2-4, hoornaert2006thephenotypicspectrum pages 5-6)
- **Growth:** variable. One proband measured 45 cm at 39 weeks but had normal stature by age eight; another was approximately −2 SD at age five. The original literature table reports approximately −2 SD in 4/4. Suggested HPO: **Short stature (HP:0004322)**, with variable expressivity. (hoornaert2006thephenotypicspectrum pages 2-4, hoornaert2006thephenotypicspectrum pages 5-6)
- **Flat/round facies and low nasal bridge:** recurrent findings. Suggested HPO: **Flat face (HP:0012368)** and **Depressed nasal bridge (HP:0005280)**. Cleft palate was absent in reported R704C cases. (hoornaert2006thephenotypicspectrum pages 2-4, hoornaert2006thephenotypicspectrum pages 5-6)

No behavioral, neurocognitive, immune, metabolic, or characteristic laboratory phenotype has been established.

## 4. Genetic and molecular information

### Gene and variant

- **Gene:** COL2A1, collagen type II alpha-1 chain; chromosome 12q13 region; Ensembl **ENSG00000139219**. Open Targets strongly associates COL2A1 with Stickler syndrome/type 1. (OpenTargets Search: Stickler syndrome,multiple epiphyseal dysplasia-COL2A1)
- **Variant:** heterozygous p.Arg704Cys; missense; germline in the reported pedigree.
- **Molecular location:** triple-helical region of procollagen-II; the substituted arginine occupies the X position of a Gly-X-Y repeat. In the 2006 series, X-position substitutions R365C and R704C were associated with ocular disease, whereas several Y-position substitutions lacked ocular anomalies. (hoornaert2006thephenotypicspectrum pages 5-6)
- **Classification:** segregation, recurrence in unrelated probands, absence from controls, a consistent phenotype, and biologic plausibility strongly support pathogenicity. A current ClinVar assertion and ACMG evidence code set were not independently retrieved; the knowledge base should therefore record “pathogenic/established disease-causing in literature” while separately importing current ClinVar review status.
- **Population frequency:** no verified gnomAD, TOPMed, ExAC, or 1000 Genomes frequency was obtained. The variant was absent from 54 original controls and from 100 controls in the later study, which is not equivalent to a modern population-frequency estimate. (hoornaert2006thephenotypicspectrum pages 2-4, ballo1998sticklerlikesyndromedue pages 3-5)
- **Somatic versus germline:** constitutional heterozygosity with vertical transmission in the original family; no evidence of a somatic-only lesion.

### Functional consequence

The defining article proposes a **dominant-negative structural effect**: replacing positively charged arginine with cysteine may reduce triple-helix stability/secretion, introduce abnormal disulfide bonding, and allow abnormal molecules to disrupt collagen fibril assembly and matrix interactions. Biochemical studies of other Arg→Cys collagen-II mutations found overmodified α1(II) chains and abnormal disulfide-linked dimers/trimers, but no equivalent experiment was reported directly for R704C. Thus dominant negativity is compelling but **inferred rather than experimentally demonstrated for this exact allele**. (ballo1998sticklerlikesyndromedue pages 3-5)

No validated modifier genes, epigenetic signature, pathogenic structural chromosome abnormality, or allele-specific pharmacogenomic interaction is known.

## 5. Environmental information

EDMMD is not caused by toxins, radiation, pollution, occupation, diet, tobacco, alcohol, infection, or immunization. Such exposures may affect general ocular, auditory, bone, or cardiovascular health but have no demonstrated disease-specific etiologic role. Avoidance of ocular trauma and selection of low-impact exercise are prudent complication-management measures, not proven disease-modifying environmental interventions.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Heterozygous COL2A1 p.Arg704Cys leads to** replacement of a basic arginine by a cysteine within the procollagen-II Gly-X-Y triple-helical domain. (ballo1998sticklerlikesyndromedue pages 3-5)
2. **The introduced cysteine is inferred to lead to** altered local charge, folding/stability, overmodification, and potentially inappropriate interchain disulfide bonding; direct R704C biochemical testing is absent. (ballo1998sticklerlikesyndromedue pages 3-5)
3. **Abnormal folding is inferred to result in two branches:** (a) less-efficient secretion/possible ER retention, and (b) secretion of structurally abnormal collagen-II chains. Canonical cytotoxic unfolded-protein-response activation has not been demonstrated and should not be assumed. (yammine2024erprocollagenstoragea pages 30-33, ballo1998sticklerlikesyndromedue pages 3-5)
4. **Secreted mutant chains are inferred to exert a dominant-negative effect that leads to** defective type-II collagen fibril formation and altered extracellular-matrix interactions in cartilage, vitreous, and related ocular/auditory tissues. (ballo1998sticklerlikesyndromedue pages 3-5, jacobson2023characteristicsofa pages 1-2)
5. **Growth-plate and epiphyseal cartilage matrix dysfunction leads to** abnormal endochondral ossification, platyspondyly, epiphyseal dysplasia, broad/flattened joint structures, short tubular hand bones, brachydactyly, and variable short stature. (savarirayan2019bestpracticeguidelines pages 2-3, hoornaert2006thephenotypicspectrum pages 2-4)
6. **Articular-cartilage matrix weakness is expected to lead to** joint hypermobility, pain, and premature degeneration/osteoarthritis, although R704C-specific longitudinal proof is limited. (savarirayan2019bestpracticeguidelines pages 8-10, hoornaert2006thephenotypicspectrum pages 5-6)
7. **Vitreous and ocular extracellular-matrix dysfunction leads to** severe early myopia and retinal structural vulnerability, which can progress to retinal tears/detachment and irreversible visual loss. (snead2020therapeuticanddiagnostic pages 3-5, jacobson2023characteristicsofa pages 1-2)
8. **Middle-ear and/or inner-ear connective-tissue dysfunction leads to** conductive, sensorineural, or mixed hearing impairment; the precise R704C tissue mechanism remains unresolved. (acke2022hearinglossin pages 1-2, hoornaert2006thephenotypicspectrum pages 2-4)

### Pathways, processes, and cellular compartments

This is primarily an **extracellular-matrix/protein-folding disease**, not a proven Wnt, MAPK, mTOR, or PI3K-AKT signaling disorder. Relevant suggested GO annotations include:

- collagen fibril organization, **GO:0030199**;
- extracellular matrix organization, **GO:0030198**;
- cartilage development, **GO:0051216**;
- endochondral ossification, **GO:0001958**;
- skeletal system development, **GO:0001501**;
- protein folding, **GO:0006457**;
- response to endoplasmic-reticulum stress, **GO:0034976**, but only as a hypothesis/research annotation for R704C.

Suggested GO cellular components are **endoplasmic-reticulum lumen (GO:0005788)**, **collagen-containing extracellular matrix (GO:0062023)**, **collagen trimer (GO:0005581)**, and extracellular space. Candidate cell types include **chondrocyte (CL:0000138)**, growth-plate chondrocyte, articular chondrocyte, vitreous hyalocyte, scleral fibroblast, retinal supporting cells, cochlear supporting cells, and middle-ear connective-tissue cells. Only chondrocytes and ocular tissue distribution have strong general biologic support; precise R704C target-cell mapping is unavailable. COL2A1/type-II collagen forms matrix networks in cartilage, vitreous, and intervertebral discs and is expressed most strongly in vitreous, with weaker ocular expression in cornea, ciliary body, iris, lens, retina, choroid, and sclera. (jacobson2023characteristicsofa pages 1-2)

No EDMMD-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or multi-omics dataset was identified.

## 7. Anatomical structures affected

- **Eye:** vitreous body, sclera/axial globe, peripheral retina, lens, and possibly other ocular connective tissues. Suggested UBERON: eye (**UBERON:0000970**), vitreous body (**UBERON:0001797**), retina (**UBERON:0000966**), lens (**UBERON:0000965**), sclera (**UBERON:0001775**).
- **Ear:** middle-ear conductive apparatus and/or cochlear structures; involvement is usually bilateral. Suggested UBERON: ear (**UBERON:0001690**), middle ear (**UBERON:0001756**), cochlea (**UBERON:0001844**).
- **Skeleton:** vertebral bodies, intervertebral discs, pelvis/acetabula, femoral heads/necks, knee and ankle epiphyses, metacarpals, and phalanges. Suggested UBERON concepts: vertebral body, intervertebral disc, pelvis, femur, knee, hand, metacarpal bone, and phalanx.
- **Tissues:** growth-plate cartilage, epiphyseal/articular cartilage, collagen-rich vitreous and connective tissue.
- **Subcellular:** procollagen biosynthetic pathway in rough ER and secretory compartments, followed by extracellular collagen fibrils. Direct R704C ER localization has not been demonstrated.

Ocular and auditory abnormalities are generally bilateral; skeletal disease is generalized rather than lateralized.

## 8. Temporal development

- **Onset:** congenital/developmental molecular lesion; myopia and hearing impairment present in early childhood. One patient was short at birth, but stature later normalized. (hoornaert2006thephenotypicspectrum pages 2-4, ballo1998sticklerlikesyndromedue pages 1-3)
- **Childhood:** severe myopia, hearing loss, brachydactyly, characteristic facies, and radiographic dysplasia are recognizable. Retinal detachment occurred in childhood in one unrelated proband. (hoornaert2006thephenotypicspectrum pages 2-4)
- **Later course:** the original family’s clinical manifestations were described as “essentially unchanged” at a 1994 review after initial ascertainment in 1978, supporting relative stability of the recognizable phenotype over that interval. Long-term retinal and arthritic risks remain incompletely measured. (ballo1998sticklerlikesyndromedue pages 1-3)
- **Disease duration:** lifelong; no spontaneous or treatment-induced remission of the genetic disorder.
- **Critical periods:** early childhood for refractive correction, hearing/language support, and retinal-risk identification; lifelong vulnerability to retinal detachment; adolescence/adulthood for joint degeneration. These windows derive partly from broader Stickler/type-II collagenopathy evidence.

## 9. Inheritance and population

### Inheritance

The original pedigree—affected mother and three affected children, with an unaffected child and unaffected maternal parents/siblings—supports **autosomal-dominant inheritance**. Segregation was complete among tested relatives. (ballo1998sticklerlikesyndromedue pages 1-3, ballo1998sticklerlikesyndromedue pages 3-5)

Penetrance appears high in this family, but complete penetrance cannot be estimated from four affected relatives. Expressivity is variable, particularly for stature, cataract/vitreous changes, retinal detachment, arthropathy, and type of hearing loss. No anticipation is expected for a missense allele, and none was reported. Germline mosaicism has not been documented for R704C. Broader type-II collagenopathy guidance reports parental somatic mosaicism in 6–10% of apparently germline cases, but this estimate is not R704C-specific. (savarirayan2019bestpracticeguidelines pages 8-10)

### Epidemiology and demographics

No prevalence, incidence, carrier-frequency, sex-ratio, age-distribution, or mortality estimate exists. Published direct evidence includes both sexes in the original family and two male later probands, too few to infer sex bias. The initial Afrikaner pedigree does not establish a founder effect; the identification of two unrelated patients argues that R704C is not confined to that family, but geographic details are insufficient. Consanguinity is not causally relevant to this dominant disorder.

## 10. Diagnostics

### Clinical diagnosis

Suspect EDMMD when the following cluster occurs:

1. severe congenital/early high myopia or abnormal vitreoretinal findings;
2. bilateral hearing impairment;
3. mild multiple-epiphyseal/spondyloepiphyseal dysplasia;
4. flat facies/low nasal bridge; and
5. conspicuous brachydactyly or stubby digits.

Recommended baseline assessment includes cycloplegic refraction, slit-lamp examination, dilated peripheral retinal examination by a vitreoretinal specialist, and ocular imaging as clinically indicated; formal audiometry plus tympanometry; skeletal survey or targeted radiographs; growth and joint examination; and clinical-genetics assessment. Routine blood, urine, enzyme, inflammatory, metabolic, or biopsy tests are not diagnostic. Type-II collagen disorder guidelines recommend routine ophthalmic and hearing monitoring. (savarirayan2019bestpracticeguidelines pages 2-3)

### Genetic testing

- **Preferred confirmation:** sequencing of COL2A1 with deletion/duplication analysis, ensuring adequate coverage of the relevant triple-helical exon and reporting the transcript.
- **Single-site testing:** appropriate for relatives after a familial p.Arg704Cys result has been validated.
- **Panel testing:** a Stickler/vitreoretinopathy or skeletal-dysplasia panel should include COL2A1; useful differentials include COL11A1, COL11A2, COL9A1–COL9A3, VCAN, COMP, MATN3, and other epiphyseal-dysplasia/retinal-detachment genes.
- **WES/WGS:** useful when phenotype-directed testing is negative or the presentation is atypical; WGS may identify noncoding or structural variants but is not necessary to detect a known coding SNV.
- **CMA, karyotype, FISH, mitochondrial DNA, and repeat-expansion testing:** not first-line for this single-nucleotide disorder unless an independent indication exists.
- **RNA sequencing/other omics:** research or variant-resolution tools, not established diagnostics.

Molecular COL2A1 testing supports anticipatory care, cascade testing, prenatal testing, reproductive counseling, and assessment for parental mosaicism. (savarirayan2019bestpracticeguidelines pages 8-10)

### Differential diagnosis

- classical COL2A1-related Stickler syndrome type 1—often similar ocular disease, but brachydactyly is less characteristic;
- COL11A1-related Stickler syndrome type 2—different vitreous phenotype and often more substantial hearing loss;
- COL11A2-related nonocular Stickler syndrome—lacks ocular disease;
- recessive COL9A1–COL9A3 Stickler syndromes;
- COMP- or MATN3-related multiple epiphyseal dysplasia—typically lacks severe myopia/vitreoretinal disease;
- Kniest dysplasia, SED congenita, mild SED with premature osteoarthritis, Wagner syndrome/VCAN vitreoretinopathy, and high-myopia/retinal-detachment syndromes.

No population or newborn-screening program exists. **Cascade testing** is the appropriate screening strategy for at-risk relatives.

## 11. Outcome and prognosis

EDMMD-specific survival and mortality data are absent. The available phenotype does not suggest a primary life-limiting visceral disorder, so life expectancy may be near normal, but this is an inference—not a measured outcome.

Major morbidity is sensory and musculoskeletal: severe myopia, retinal detachment and possible blindness; bilateral hearing impairment; chronic joint pain, mobility limitation, and potentially premature osteoarthritis. No disease-specific disability weights, EQ-5D/SF-36/PROMIS scores, recovery rates, or prognostic biomarkers exist.

Prognosis is likely influenced by retinal phenotype/detachment history, degree and type of hearing loss, skeletal deformity, pain and osteoarthritis, and access to early multidisciplinary care. Retinal detachment is an emergency; visual recovery depends on macular involvement, detachment severity, timing, and surgical complexity. Hearing aids and treatment of reversible middle-ear disease can improve function but do not correct the collagen defect.

## 12. Treatment

There is **no approved disease-modifying, gene, RNA, cell, or targeted molecular therapy for EDMMD**. Treatment is phenotype-directed.

### Ophthalmic

- immediate refractive correction and amblyopia management in children;
- lifelong specialist retinal surveillance and education about flashes, new floaters, curtain-like field loss, or sudden visual decline;
- urgent standard retinal-detachment repair when indicated;
- cataract treatment with careful vitreoretinal risk assessment;
- individualized discussion of prophylactic cryotherapy or 360-degree laser retinopexy at an expert Stickler center.

Broader type-1 Stickler evidence—not R704C-specific—includes 487 genetically confirmed patients: untreated controls had 7.4-fold greater detachment risk than bilaterally prophylaxed patients (5.0-fold in matched controls); following first-eye detachment, untreated fellow eyes had 10.3-fold greater risk than prophylaxed eyes (8.4-fold matched), and half of second-eye detachments occurred within four years. These retrospective results support prophylaxis but do not replace individualized assessment or establish an R704C response rate. (snead2020therapeuticanddiagnostic pages 3-5)

Suggested NCIT intervention concepts include **ophthalmologic examination**, **laser photocoagulation/laser retinopexy**, **cryotherapy**, **vitrectomy**, **scleral buckling**, **cataract surgery**, and **corrective lenses**.

### Hearing

Regular age-appropriate audiometry and tympanometry; treatment of otitis media/Eustachian-tube dysfunction; hearing aids when indicated; educational accommodations; and cochlear implantation only for appropriately severe sensorineural disease. Active detection is important because formal testing identifies more hearing loss and dual sensory impairment magnifies disability. (acke2022hearinglossin pages 1-2)

Suggested NCIT concepts: **audiologic examination**, **hearing aid**, **tympanostomy**, and **cochlear implant**.

### Musculoskeletal and rehabilitation

Maintain healthy weight and low-impact activity; use physical/occupational therapy, strengthening, range-of-motion work, pacing, orthoses, and conventional analgesia as needed. Monitor hips, knees, spine, gait, contractures, and osteoarthritis. In broader type-II collagen disorders, guided growth or corrective osteotomy may address deformity, and severe hip osteoarthritis may require arthroplasty; power mobility can preserve participation when pain or deformity limits ambulation. Evidence is mainly expert consensus and case series. (savarirayan2019bestpracticeguidelines pages 8-10)

Suggested NCIT concepts include **physical therapy**, **occupational therapy**, **analgesic therapy**, **orthopedic surgery**, **osteotomy**, **guided growth procedure**, **joint replacement**, and **mobility aid**. No EDMMD-specific pharmacogenomic guidance exists.

### Trials and experimental treatment

No p.Arg704Cys-specific therapeutic trial was found. The randomized scleral-buckle prevention study **NCT04465188** was withdrawn for failure to enroll and had actual enrollment zero. (NCT04465188 chunk 1)

A prospective historically controlled study of 360-degree laser prophylaxis, **NCT07146516**, began after the requested 2023–2024 priority window and aims to enroll 500 genetically confirmed type-1/type-2 Stickler participants; it is broader Stickler research, not EDMMD-specific. (NCT07146516 chunk 1, NCT07146516 chunk 2)

## 13. Prevention

- **Primary prevention:** lifestyle or vaccination cannot prevent a transmitted pathogenic allele. Reproductive options include prenatal diagnosis and preimplantation genetic testing after familial-variant confirmation.
- **Secondary prevention:** cascade testing, early eye/hearing assessment, refractive correction, and timely retinal-risk evaluation.
- **Tertiary prevention:** retinal prophylaxis where individualized benefit outweighs risk; prompt detachment repair; hearing support; joint protection, rehabilitation, weight management, and treatment of deformity/osteoarthritis.
- **Counseling:** autosomal-dominant transmission, variable expressivity, transcript-normalized variant confirmation, and testing of apparently unaffected relatives are central. Broader COL2A1 guidance also warrants consideration of parental mosaicism when a case appears de novo. (savarirayan2019bestpracticeguidelines pages 8-10)
- **Immunization/public-health environmental control:** not disease-specific or etiologically relevant.

## 14. Other species and natural disease

COL2A1 orthologs are highly conserved across vertebrates, including mouse (*Mus musculus*, NCBI Taxon 10090), zebrafish (*Danio rerio*, Taxon 7955), dog (*Canis lupus familiaris*, Taxon 9615), and other cartilage-bearing vertebrates. However, no naturally occurring nonhuman disease caused by the exact orthologous p.Arg704Cys substitution was identified, and no breed-specific VBO annotation can be recommended.

This is not infectious and has no zoonotic or cross-species transmission. Comparative relevance lies in conserved type-II collagen function in cartilage, vitreous, hearing structures, and endochondral ossification—not transmissibility.

## 15. Model organisms and advanced models

No exact **R704C knock-in animal, cellular, organoid, or iPSC model** was identified.

Broader models include:

- mouse Col2a1 missense models reproducing combinations of spondyloepiphyseal dysplasia, hearing loss, and retinal abnormalities;
- heterozygous Col2a1-inactivation mice used to examine ocular expression and vitreous phenotype;
- zebrafish col2a1a models relevant to eye and craniofacial development;
- human iPSC-derived cartilage carrying other COL2A1 substitutions.

The principal limitation is mutation specificity: collagen-II disease mechanisms differ by variant. A 2024 iPSC-cartilage study of another Arg→Cys allele found deficient extracellular collagen-II matrix, excessive post-translational modification, modest intracellular retention and ER distention, but no detectable unfolded-protein response. This is important expert-level evidence that ER storage and extracellular dominant-negative effects can occur without a canonical stress response; it should guide—but not be substituted for—future R704C experiments. (yammine2024erprocollagenstoragea pages 30-33)

The priority model would be an isogenic heterozygous **COL2A1 p.Arg704Cys human iPSC line** differentiated into growth-plate and articular chondrocytes, vitreous-like cells, and auditory-supporting lineages. Relevant readouts include triple-helix folding/secretion, disulfide-linked multimers, collagen-II fibril ultrastructure, ER morphology/UPR, matrix mechanics, chondrocyte differentiation, and ocular extracellular-matrix organization.

## Recent developments and expert assessment

No p.Arg704Cys-specific paper from 2023–2024 was identified. A 2023 COL2A1 family study involving different variants reinforced that mutation-specific ocular-versus-joint expressivity remains difficult to predict and that deep phenotyping is necessary. (jacobson2023characteristicsofa pages 1-2, jacobson2023characteristicsofa pages 9-10)

Recent retinal practice is moving from retrospective prophylaxis series toward standardized prospective assessment. Nevertheless, the evidence available through 2024 remains largely retrospective, and variant-specific risk stratification for R704C is impossible. The most defensible expert position is therefore to manage EDMMD as a **high-risk COL2A1 vitreoretinal disorder with a distinctive brachydactyly/epiphyseal-dysplasia phenotype**, while avoiding the assumption that every statistic or treatment effect reported for truncating COL2A1 Stickler type 1 applies quantitatively to p.Arg704Cys. (snead2020therapeuticanddiagnostic pages 3-5, savarirayan2019bestpracticeguidelines pages 2-3)

## Primary evidence quotations and key references

1. **Ballo R, Beighton PH, Ramesar RS.** “Stickler-like syndrome due to a dominant negative mutation in the COL2A1 gene.” *American Journal of Medical Genetics*. Published November 1998;80:6–11. DOI: https://doi.org/10.1002/(SICI)1096-8628(19981102)80:1%3C6::AID-AJMG2%3E3.0.CO;2-0. Exact abstract quotation: **“DNA analysis of the exons of the COL2A1 gene documented a C-T transversion in exon 39, resulting in an Arg704Cys substitution in the triple helical domain of the type II collagen peptide.”** (ballo1998sticklerlikesyndromedue pages 1-3)

2. **Hoornaert KP et al.** “The phenotypic spectrum in patients with arginine to cysteine mutations in the COL2A1 gene.” *Journal of Medical Genetics*. 2006;43:406–413. DOI: https://doi.org/10.1136/jmg.2005.035717. The study identified six Arg→Cys substitutions in 11 unrelated probands and found a relatively consistent, site-specific R704C phenotype featuring severe myopia, hearing loss, brachydactyly, and spondyloepiphyseal changes. (hoornaert2006thephenotypicspectrum pages 1-2, hoornaert2006thephenotypicspectrum pages 2-4)

3. **Savarirayan R et al.** “Best practice guidelines regarding diagnosis and management of patients with type II collagen disorders.” *Genetics in Medicine*. Published January 2019;21:2070–2080. DOI: https://doi.org/10.1038/s41436-019-0446-9. This is broader guideline evidence, not R704C-specific. (savarirayan2019bestpracticeguidelines pages 8-10, savarirayan2019bestpracticeguidelines pages 2-3)

4. **Acke FRE, De Leenheer EMR.** “Hearing Loss in Stickler Syndrome: An Update.” *Genes*. Published September 2022;13:1571. DOI: https://doi.org/10.3390/genes13091571. Exact abstract quotation: **“Consequently, hearing loss should be actively sought for and adequately treated in Stickler syndrome patients given its high prevalence and the concomitant visual impairment in most patients.”** This is gene/syndrome-level extrapolation. (acke2022hearinglossin pages 1-2)

5. **Jacobson A, Besirli CG, Bohnsack BL.** “Characteristics of a Three-Generation Family with Stickler Syndrome Type I Carrying Two Different COL2A1 Mutations.” *Genes*. Published March 2023;14:847. DOI: https://doi.org/10.3390/genes14040847. The report supports mutation-specific expressivity and deep phenotyping but does not include p.Arg704Cys. (jacobson2023characteristicsofa pages 1-2, jacobson2023characteristicsofa pages 9-10)

## Knowledge-base curation recommendations

1. Treat EDMMD/OMIM 132450 as an **allelic COL2A1 disorder overlapping Stickler syndrome type 1**, not as ordinary COMP/MATN3 multiple epiphyseal dysplasia.
2. Normalize the variant to a current transcript before storing a cDNA coordinate; preserve historical “C2503T, exon 39” as a source-level synonym rather than the sole canonical HGVS representation.
3. Record p.Arg704Cys as heterozygous germline, autosomal dominant, literature-established pathogenic, with an **inferred dominant-negative extracellular-matrix mechanism**.
4. Store conductive and sensorineural hearing impairment as both supported phenotypes; do not define conductive deafness as invariant.
5. Do not assign exact penetrance, prevalence, retinal-detachment risk, life expectancy, or treatment-response percentages from six cases.
6. Tag broader Stickler statistics and management recommendations explicitly as **indirect/extrapolated evidence**.
7. Priority missing data are current ClinVar/gnomAD normalization, prospective natural history, standardized vitreous phenotyping, longitudinal audiology and arthropathy data, and an isogenic R704C functional model.

References

1. (hoornaert2006thephenotypicspectrum pages 2-4): Kristien P. Hoornaert, Chantal Dewinter, I. Vereecke, F. Beemer, W. Courtens, A. Fryer, H. Fryssira, M. Lees, A. Müllner‐Eidenböck, Rimoin Dl, L. Siderius, A. Superti-Furga, K. Temple, P. Willems, A. Zankl, C. Zweier, A. Paepe, P. Coucke, and G. Mortier. The phenotypic spectrum in patients with arginine to cysteine mutations in the col2a1 gene. Journal of Medical Genetics, 43:406-413, Sep 2006. URL: https://doi.org/10.1136/jmg.2005.035717, doi:10.1136/jmg.2005.035717. This article has 100 citations and is from a domain leading peer-reviewed journal.

2. (ballo1998sticklerlikesyndromedue pages 1-3): R. Ballo, P.H. Beighton, and R.S. Ramesar. Stickler-like syndrome due to a dominant negative mutation in the col2a1 gene. Nov 1998. URL: https://doi.org/10.1002/(sici)1096-8628(19981102)80:1<6::aid-ajmg2>3.0.co;2-0, doi:10.1002/(sici)1096-8628(19981102)80:1<6::aid-ajmg2>3.0.co;2-0. This article has 56 citations.

3. (ballo1998sticklerlikesyndromedue pages 3-5): R. Ballo, P.H. Beighton, and R.S. Ramesar. Stickler-like syndrome due to a dominant negative mutation in the col2a1 gene. Nov 1998. URL: https://doi.org/10.1002/(sici)1096-8628(19981102)80:1<6::aid-ajmg2>3.0.co;2-0, doi:10.1002/(sici)1096-8628(19981102)80:1<6::aid-ajmg2>3.0.co;2-0. This article has 56 citations.

4. (hoornaert2006thephenotypicspectrum pages 5-6): Kristien P. Hoornaert, Chantal Dewinter, I. Vereecke, F. Beemer, W. Courtens, A. Fryer, H. Fryssira, M. Lees, A. Müllner‐Eidenböck, Rimoin Dl, L. Siderius, A. Superti-Furga, K. Temple, P. Willems, A. Zankl, C. Zweier, A. Paepe, P. Coucke, and G. Mortier. The phenotypic spectrum in patients with arginine to cysteine mutations in the col2a1 gene. Journal of Medical Genetics, 43:406-413, Sep 2006. URL: https://doi.org/10.1136/jmg.2005.035717, doi:10.1136/jmg.2005.035717. This article has 100 citations and is from a domain leading peer-reviewed journal.

5. (savarirayan2019bestpracticeguidelines pages 8-10): R. Savarirayan, V. Bompadre, M. Bober, T. Cho, M. Goldberg, J. Hoover-Fong, M. Irving, Shawn E. Kamps, W. Mackenzie, C. Raggio, Samantha S. Spencer, and K. White. Best practice guidelines regarding diagnosis and management of patients with type ii collagen disorders. Genetics in Medicine, 21:2070-2080, Jan 2019. URL: https://doi.org/10.1038/s41436-019-0446-9, doi:10.1038/s41436-019-0446-9. This article has 28 citations and is from a highest quality peer-reviewed journal.

6. (snead2020therapeuticanddiagnostic pages 3-5): Martin Snead, Howard Martin, Peter Bale, Nick Shenker, David Baguley, Philip Alexander, Annie McNinch, and Arabella Poulson. Therapeutic and diagnostic advances in stickler syndrome. Therapeutic Advances in Rare Disease, Jan 2020. URL: https://doi.org/10.1177/2633004020978661, doi:10.1177/2633004020978661. This article has 41 citations.

7. (savarirayan2019bestpracticeguidelines pages 2-3): R. Savarirayan, V. Bompadre, M. Bober, T. Cho, M. Goldberg, J. Hoover-Fong, M. Irving, Shawn E. Kamps, W. Mackenzie, C. Raggio, Samantha S. Spencer, and K. White. Best practice guidelines regarding diagnosis and management of patients with type ii collagen disorders. Genetics in Medicine, 21:2070-2080, Jan 2019. URL: https://doi.org/10.1038/s41436-019-0446-9, doi:10.1038/s41436-019-0446-9. This article has 28 citations and is from a highest quality peer-reviewed journal.

8. (jacobson2023characteristicsofa pages 1-2): Adam Jacobson, Cagri G. Besirli, and Brenda L. Bohnsack. Characteristics of a three-generation family with stickler syndrome type i carrying two different col2a1 mutations. Genes, 14:847, Mar 2023. URL: https://doi.org/10.3390/genes14040847, doi:10.3390/genes14040847. This article has 6 citations.

9. (yammine2024erprocollagenstoragea pages 30-33): KM Yammine, S Mirda Abularach, and S Kim. Er procollagen storage defect without associated unfolded protein response drives precocious osteoarthritis. Unknown journal, 2024.

10. (NCT04465188 chunk 1):  Scleral Buckling for Retinal Detachment Prevention in Genetically Confirmed Stickler Syndrome. Assistance Publique - Hôpitaux de Paris. 2023. ClinicalTrials.gov Identifier: NCT04465188

11. (NCT07146516 chunk 1):  Retinal Detachment Prevention (Laser Prophylaxis) in Stickler Syndrome (SS). Helen Keller Eye Research Foundation. 2025. ClinicalTrials.gov Identifier: NCT07146516

12. (OpenTargets Search: Stickler syndrome,multiple epiphyseal dysplasia-COL2A1): Open Targets Query (Stickler syndrome,multiple epiphyseal dysplasia-COL2A1, 15 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

13. (snead1999clinicalandmolecular pages 3-4): Martin P Snead and John R W Yates. Clinical and molecular genetics of stickler syndrome. Journal of Medical Genetics, 36:353-359, May 1999. URL: https://doi.org/10.1136/jmg.36.5.353, doi:10.1136/jmg.36.5.353. This article has 584 citations and is from a domain leading peer-reviewed journal.

14. (acke2022hearinglossin pages 1-2): Frederic R. E. Acke and Els M. R. De Leenheer. Hearing loss in stickler syndrome: an update. Genes, 13:1571, Sep 2022. URL: https://doi.org/10.3390/genes13091571, doi:10.3390/genes13091571. This article has 32 citations.

15. (NCT07146516 chunk 2):  Retinal Detachment Prevention (Laser Prophylaxis) in Stickler Syndrome (SS). Helen Keller Eye Research Foundation. 2025. ClinicalTrials.gov Identifier: NCT07146516

16. (jacobson2023characteristicsofa pages 9-10): Adam Jacobson, Cagri G. Besirli, and Brenda L. Bohnsack. Characteristics of a three-generation family with stickler syndrome type i carrying two different col2a1 mutations. Genes, 14:847, Mar 2023. URL: https://doi.org/10.3390/genes14040847, doi:10.3390/genes14040847. This article has 6 citations.

17. (hoornaert2006thephenotypicspectrum pages 1-2): Kristien P. Hoornaert, Chantal Dewinter, I. Vereecke, F. Beemer, W. Courtens, A. Fryer, H. Fryssira, M. Lees, A. Müllner‐Eidenböck, Rimoin Dl, L. Siderius, A. Superti-Furga, K. Temple, P. Willems, A. Zankl, C. Zweier, A. Paepe, P. Coucke, and G. Mortier. The phenotypic spectrum in patients with arginine to cysteine mutations in the col2a1 gene. Journal of Medical Genetics, 43:406-413, Sep 2006. URL: https://doi.org/10.1136/jmg.2005.035717, doi:10.1136/jmg.2005.035717. This article has 100 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Multiple_Epiphyseal_Dysplasia_Beighton_Type-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 4 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1002/(sici)1096-8628(19981102)80:1` (4 mentions) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007562` (2 mentions) - the report calls it "if available"; MONDO calls it **multiple epiphyseal dysplasia, Beighton type**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0062023` (obsolete collagen-containing extracellular matrix) (1 mention) - replaced by `GO:0031012`
