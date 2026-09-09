---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-09T11:17:07.134943'
end_time: '2026-09-09T11:35:55.218576'
duration_seconds: 1128.08
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Peroxisome biogenesis disorder 12A (PBD12A, Zellweger syndrome, OMIM
    614886) caused by biallelic PEX19 variants, historically peroxisome biogenesis
    disorder complementation group J - not the PEX3-associated PBD10A
  mondo_id: MONDO:0013951
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 44
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 3
  off_topic: 1
  off_topic_references:
  - DOI:10.1136/bcr-2022-252014
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 48
  verified: 47
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0013951
    reported_labels:
    - if available
    ontology_label: peroxisome biogenesis disorder 12A (Zellweger)
  obsolete_terms:
  - term_id: GO:0030259
    ontology_label: obsolete lipid glycosylation
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Peroxisome_Biogenesis_Disorder_12A_Zellweger-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peroxisome biogenesis disorder 12A (PBD12A, Zellweger syndrome, OMIM 614886) caused by biallelic PEX19 variants, historically peroxisome biogenesis disorder complementation group J - not the PEX3-associated PBD10A
- **MONDO ID:** MONDO:0013951 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome biogenesis disorder 12A (PBD12A, Zellweger syndrome, OMIM 614886) caused by biallelic PEX19 variants, historically peroxisome biogenesis disorder complementation group J - not the PEX3-associated PBD10A** covering all of the
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
- **Disease Name:** Peroxisome biogenesis disorder 12A (PBD12A, Zellweger syndrome, OMIM 614886) caused by biallelic PEX19 variants, historically peroxisome biogenesis disorder complementation group J - not the PEX3-associated PBD10A
- **MONDO ID:** MONDO:0013951 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome biogenesis disorder 12A (PBD12A, Zellweger syndrome, OMIM 614886) caused by biallelic PEX19 variants, historically peroxisome biogenesis disorder complementation group J - not the PEX3-associated PBD10A** covering all of the
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


# Peroxisome biogenesis disorder 12A due to **PEX19**

## Scope and evidence standard

This report concerns **PBD12A/Zellweger syndrome caused by biallelic PEX19 variants**, historically complementation group J. It does **not** concern PEX3-associated PBD10A. The distinction is important because older complementation-group nomenclature varies among laboratories.

The PEX19-specific human evidence is exceptionally small: three primary case publications describe **four molecularly confirmed children and one highly suggestive, untested sibling**. Consequently, percentages calculated from these patients would be unstable and ascertainment-biased. Statements below are labeled **PEX19-specific** where directly demonstrated; otherwise they are identified as **Zellweger-spectrum (ZSD) extrapolation**.

| Domain | PEX19-specific evidence | Zellweger-spectrum extrapolation | Key sources |
|---|---|---|---|
| Identity | Peroxisome biogenesis disorder 12A (PBD12A; Zellweger phenotype), **OMIM 614886**, **MONDO:0013951**, caused by biallelic **PEX19** variants; historically complementation group **J**. It is distinct from **PEX3-associated PBD10A**. | Part of the autosomal-recessive Zellweger spectrum of peroxisome-biogenesis disorders. | Open Targets disease–gene evidence (OpenTargets Search: peroxisome biogenesis disorder 12A,Zellweger syndrome-PEX19); Matsuzono et al., 1999, DOI: [10.1073/pnas.96.5.2116](https://doi.org/10.1073/pnas.96.5.2116), PMID: **10051604** (matsuzono1999humanpex19cdna pages 1-2, matsuzono1999humanpex19cdna pages 5-6) |
| Known human variants and cases | **c.763_764insA** (historically A764 insertion; C-terminal frameshift): homozygous in two brothers who died at 3 and 21 days. **c.320delA, p.Lys107SerfsTer13**: homozygous in one girl who died at 16 months. **p.Leu94Ter** (reported genomic coordinate chr1:g.160283009A>T): homozygous in a male neonate; a similarly affected sibling was not molecularly confirmed. Thus, the primary literature describes **four genetically confirmed children plus one highly suggestive sibling**. | No reliable population variant spectrum, recurrent founder allele, or genotype-specific frequency has been established because the reported cohort is extremely small. | Mohamed et al., 2010, DOI: [10.1002/ajmg.a.33560](https://doi.org/10.1002/ajmg.a.33560) (mohamed2010amutationin pages 3-4, mohamed2010amutationin pages 1-2); Adiyapatham & Murugesan, accepted **9 March 2023**, DOI: [10.1136/bcr-2022-252014](https://doi.org/10.1136/bcr-2022-252014) (adiyapatham2023novelmutationcausing pages 1-2, adiyapatham2023novelmutationcausing pages 2-3) |
| Inheritance and risk | Autosomal recessive. Reported variants were homozygous; consanguinity was present in the 2010 and 2023 families, and both parents of the c.320delA patient were carriers. | For two carrier parents, Mendelian recurrence risk is **25% affected, 50% carrier, and 25% unaffected/non-carrier per pregnancy**. Penetrance of biallelic null alleles appears high, but cannot be quantified. No anticipation, sex bias, protective allele, or established modifier is known. | Human segregation and family evidence (adiyapatham2023novelmutationcausing pages 1-2, mohamed2010amutationin pages 1-2) |
| Core phenotype | Antenatal or neonatal multisystem disease: profound hypotonia, weak cry/poor feeding and reflexes, seizures, craniofacial dysmorphism and large fontanelles/metopic suture; hydrocephalus, cerebral white-matter abnormalities, ventriculomegaly/colpocephaly or cerebellar-vermis hypoplasia; congenital heart defects; genital anomalies; corneal opacity; skeletal abnormalities or talipes. The longer-surviving child developed liver disease, global developmental delay, recurrent infection, renal tubular dysfunction and gallstones. | Other ZSD manifestations—sensorineural hearing loss, retinal degeneration, adrenal insufficiency, leukodystrophy, osteopenia/fractures and nephrolithiasis—are clinically relevant surveillance targets but have not all been demonstrated in PEX19 cases. | PEX19 cases (adiyapatham2023novelmutationcausing pages 2-3, mohamed2010amutationin pages 1-2, mohamed2010amutationin pages 2-3); broader ZSD review (argyriou2016peroxisomebiogenesisdisorders pages 9-10, argyriou2016peroxisomebiogenesisdisorders pages 7-9) |
| Diagnostic biomarkers | In the c.320delA patient: elevated plasma **C26:0**, C26:0/C22:0 and C24:0/C22:0 ratios; deficient fibroblast C26:0 and pristanate β-oxidation, phytanate α-oxidation, DHAPAT activity and plasmalogens; abnormal acyl-CoA oxidase/thiolase processing; and absent peroxisomes by immunofluorescence. Routine ammonia, lactate and organic acids were normal in the 2023 neonate, illustrating that normal routine metabolic tests do not exclude PBD12A. | Recommended ZSD testing includes plasma VLCFAs, phytanic/pristanic and pipecolic acids, C27 bile-acid intermediates and erythrocyte plasmalogens, followed by fibroblast functional studies and molecular confirmation. | Mohamed et al. (mohamed2010amutationin pages 1-2, mohamed2010amutationin pages 2-3); 2023 case (adiyapatham2023novelmutationcausing pages 1-2); aggregate diagnostic evidence (ebberink2011geneticclassificationand pages 1-2, argyriou2016peroxisomebiogenesisdisorders pages 10-16) |
| Molecular mechanism | PEX19 is a predominantly cytosolic chaperone/import receptor that binds membrane-peroxisomal targeting signals, stabilizes newly synthesized peroxisomal membrane proteins and delivers them to PEX3/PEX16 for membrane insertion. Loss causes PMP degradation or mitochondrial mistargeting, failed peroxisomal membrane assembly and loss of matrix-protein import. Wild-type PEX19 restored peroxisomes in CG-J fibroblasts and CHO mutants. PEX19-deficient human cells also show defective ether-lipid-dependent GPI-anchor remodeling. | Downstream accumulation of VLCFAs, branched fatty acids and toxic bile-acid intermediates, together with reduced plasmalogens/DHA and altered redox homeostasis, is the accepted ZSD mechanism linking peroxisome failure to brain, liver, kidney, eye and skeletal injury. Exact causal contributions to each PEX19 phenotype remain incompletely resolved. | Human/cellular studies: DOI [10.1083/jcb.200304111](https://doi.org/10.1083/jcb.200304111) (jones2004pex19isa pages 2-3, jones2004pex19isa pages 1-2); CG-J rescue (matsuzono1999humanpex19cdna pages 3-3, matsuzono1999humanpex19cdna pages 5-6); GPI remodeling, DOI [10.1194/jlr.M021204](https://doi.org/10.1194/jlr.M021204) (kanzawa2012defectivelipidremodeling pages 1-2) |
| Prognosis | All four molecularly confirmed children died early: **3 days, 21 days, approximately 15 days, and 16 months**. Respiratory failure, severe infection/sepsis, coagulopathy and liver failure contributed. No PEX19-specific survival curve or 5-/10-year survival estimate exists. | Severe Zellweger syndrome generally causes death during infancy; survival into later childhood or adulthood pertains mainly to hypomorphic PEX variants and milder ZSD, not yet established for PEX19. | Human cases (mohamed2010amutationin pages 3-4, mohamed2010amutationin pages 1-2, adiyapatham2023novelmutationcausing pages 1-2); broader ZSD prognosis (argyriou2016peroxisomebiogenesisdisorders pages 7-9) |
| Treatment and current applications | No curative or PEX19-targeted treatment is established. Reported care was supportive: ventilation/respiratory support, antiseizure treatment, nutrition, infection management, comfort/palliative care and genetic counseling. No PEX19-specific gene, RNA or cell therapy trial was identified. | ZSD-wide interventions remain supportive or investigational. Betaine was studied only in selected **PEX1** genotypes; hydroxychloroquine only in **PEX1/PEX6/PEX26** disease. Bile-acid therapy may improve hepatobiliary biomarkers or histology without proven alteration of overall course. Recruiting studies include the PBD natural-history cohort **NCT01668186** and retinopathy study **NCT06190626**; neither reports PEX19-specific outcomes. | Clinical records and review evidence (NCT01668186 chunk 1, NCT01838941 chunk 1, NCT00004442 chunk 1, argyriou2016peroxisomebiogenesisdisorders pages 18-20) |
| Epidemiology | PEX19-specific prevalence, incidence, carrier frequency, sex ratio and geographic distribution are unknown. In a 613-cell-line ZSD series, only **4/613 (0.65%)** were assigned to PEX19, versus 3/613 to PEX3; the cohort was over 90% Western European and is not population based. | Overall ZSD birth incidence is commonly estimated near **1:50,000**, with reported geographic variation as low as approximately 1:500,000 in Japan; these figures must not be presented as PBD12A incidence. | Aggregate fibroblast cohort (ebberink2011geneticclassificationand pages 3-4, ebberink2011geneticclassificationand pages 2-3); ZSD estimates (adiyapatham2023novelmutationcausing pages 1-2, argyriou2016peroxisomebiogenesisdisorders pages 7-9) |
| Evidence limitations | Evidence rests on three case publications, patient fibroblasts and experimental models. Phenotype percentages calculated from four confirmed patients would be unstable and ascertainment-biased. Allele frequencies and modern ACMG/AMP classifications were not consistently reported; the 2023 paper’s 0.002% figure came from an internal database rather than a specified population database. | Most diagnostic, surveillance and treatment recommendations necessarily derive from ZSD as a whole. No PEX19-specific natural-history cohort, randomized trial, standardized quality-of-life analysis, single-cell/spatial study or validated prognostic biomarker is available in the retrieved evidence. | Case-count and cohort limitations (adiyapatham2023novelmutationcausing pages 1-2, ebberink2011geneticclassificationand pages 1-2, ebberink2011geneticclassificationand pages 3-4); current study scope (NCT06190626 chunk 1, NCT03440905 chunk 1) |


*Table: Compact evidence map separating findings demonstrated in PEX19-associated PBD12A from broader Zellweger-spectrum extrapolations. It highlights the exceptionally small human case base and consequent limits on frequencies, prognosis and treatment inference.*

## 1. Disease information

### Definition

PBD12A is an autosomal-recessive, congenital peroxisome-biogenesis disorder in which biallelic loss-of-function variants in **PEX19** prevent normal assembly of the peroxisomal membrane. This secondarily disrupts import of peroxisomal matrix enzymes and multiple lipid-metabolic pathways. Reported patients have had the severe neonatal **Zellweger syndrome/cerebrohepatorenal syndrome** phenotype rather than an attenuated ZSD phenotype. Open Targets independently links PEX19 (ENSG00000162735) to MONDO:0013951, citing the foundational and cohort literature (PMIDs **10051604** and **20683989**) (OpenTargets Search: peroxisome biogenesis disorder 12A,Zellweger syndrome-PEX19).

### Identifiers and synonyms

- **OMIM disease:** 614886, peroxisome biogenesis disorder 12A (Zellweger).
- **MONDO:** MONDO:0013951.
- **Gene:** **PEX19**, peroxisomal biogenesis factor 19; the retrieved sources identify NM_002857.2 as a historical transcript reference (ebberink2011geneticclassificationand pages 2-3).
- **Synonyms:** PBD12A; PEX19 deficiency; PEX19-related Zellweger syndrome; Zellweger spectrum disorder due to PEX19; peroxisome biogenesis disorder complementation group J/CG-J.
- **Not synonymous with:** PEX3-associated PBD10A. PEX3 and PEX19 were separate complementation groups in the 613-cell-line series (ebberink2011geneticclassificationand pages 3-4).
- **Orphanet:** a PEX19-specific ORPHA identifier was not established in the retrieved evidence; the condition is generally indexed under Zellweger spectrum disorder.
- **ICD-10:** no specific PEX19 code; broader coding commonly falls under E71.5, disorders of peroxisomal function.
- **ICD-11/MeSH/SNOMED CT:** broader Zellweger syndrome or peroxisomal-disorder concepts should be used with a PEX19 molecular qualifier; no uniquely validated PBD12A code was recovered.

The evidence includes individual case records and patient fibroblasts, plus aggregated disease-level resources and ZSD cohorts. It is not derived from an EHR population.

## 2. Etiology, risk, and protective factors

The initiating cause is **germline biallelic PEX19 loss of function**. All reported disease alleles are truncating frameshift or nonsense variants. Homozygosity and parental carrier status where tested support autosomal-recessive inheritance (matsuzono1999humanpex19cdna pages 3-5, mohamed2010amutationin pages 1-2).

**Genetic risk factors** are carriage of two pathogenic alleles and parental relatedness. The 2010 parents were first cousins; the 2023 family reported third-degree consanguinity and recurrence in two siblings (adiyapatham2023novelmutationcausing pages 1-2, mohamed2010amutationin pages 1-2). Family history is therefore a risk indicator, not a mechanistic environmental factor.

No susceptibility loci, validated modifier genes, protective alleles, founder effects, or epigenetic risk factors are known. No toxin, diet, infection, lifestyle, age, or sex exposure causes this Mendelian disorder. Infection can worsen an affected infant’s course but is a complication rather than the etiology. No demonstrated gene–environment interaction modifies penetrance. Residual PEX19 function is a plausible genotype–severity determinant, but this inference rests principally on the c.320delA patient’s longer survival and residual fibroblast activity, not a sufficiently large genotype–phenotype series (mohamed2010amutationin pages 2-3, mohamed2010amutationin pages 3-4).

## 3. Phenotypes

### PEX19-specific clinical spectrum

All confirmed cases had antenatal or neonatal onset and severe multisystem disease.

- **Neuromuscular:** neonatal hypotonia, inactivity, poor suck, weak cry, poor primitive reflexes, apnea/poor respiratory drive, seizures and profound developmental impairment. Suggested terms: **HP:0001252 Hypotonia**, HP:0001263 Global developmental delay, HP:0001250 Seizure, HP:0001284 Areflexia, HP:0002104 Apnea (adiyapatham2023novelmutationcausing pages 1-2, mohamed2010amutationin pages 1-2).
- **Brain:** hydrocephalus in the original brothers; cerebral atrophy/diffuse demyelination in the c.320delA girl; ventriculomegaly, colpocephaly and inferior cerebellar-vermis hypoplasia in the 2023 child. Suggested terms: HP:0000238 Hydrocephalus, HP:0002119 Ventriculomegaly, HP:0001272 Cerebellar hypoplasia, HP:0002059 Cerebral atrophy (adiyapatham2023novelmutationcausing pages 2-3, mohamed2010amutationin pages 2-3).
- **Craniofacial:** large anterior/posterior fontanelles, prominent metopic suture, broad or flat nasal bridge, hypertelorism, low-set dysplastic ears and micro/retrognathia. Suggested terms: HP:0000239 Large fontanelle, HP:0000316 Hypertelorism, HP:0000347 Micrognathia, HP:0000431 Wide nasal bridge (adiyapatham2023novelmutationcausing pages 1-2, adiyapatham2023novelmutationcausing pages 2-3).
- **Ocular:** corneal clouding/opacity was reported in the 2023 proband. Suggested term: **HP:0007957 Corneal opacity**. Retinal degeneration is important in broader ZSD but has not been demonstrated in this tiny PEX19 series (adiyapatham2023novelmutationcausing pages 1-2, argyriou2016peroxisomebiogenesisdisorders pages 9-10).
- **Cardiac:** double-outlet right ventricle in the original family, ASD/PDA in the 2010 patient, and perimembranous VSD in the 2023 family. Suggested terms: HP:0001719 Double outlet right ventricle, HP:0001631 ASD, HP:0001643 PDA, HP:0001629 VSD (adiyapatham2023novelmutationcausing pages 2-3, mohamed2010amutationin pages 1-2).
- **Hepatobiliary:** neonatal liver-enzyme and bilirubin abnormalities, later liver failure, and multiple gallstones in the longest survivor. Suggested terms: HP:0001392 Abnormal liver function, HP:0002904 Hyperbilirubinemia, HP:0001081 Cholelithiasis, HP:0001399 Hepatic failure (mohamed2010amutationin pages 1-2, mohamed2010amutationin pages 2-3).
- **Renal:** the c.320delA child developed proximal tubular dysfunction with normal-anion-gap acidosis, proteinuria, aminoaciduria and glucosuria at one year. Suggested terms: HP:0000124 Renal tubular dysfunction, HP:0001997 Gout is inappropriate; use HP terms for metabolic acidosis, proteinuria, aminoaciduria and glucosuria individually (mohamed2010amutationin pages 1-2).
- **Skeletal/limb:** dense bones in the original brothers and bilateral congenital talipes equinovarus in the 2023 child. Suggested terms: HP:0011001 Increased bone mineral density and HP:0001762 Talipes equinovarus (adiyapatham2023novelmutationcausing pages 2-3, mohamed2010amutationin pages 3-4).
- **Genital:** hypospadias and cryptorchidism/undescended testis. Suggested terms: HP:0000047 Hypospadias, HP:0000028 Cryptorchidism (adiyapatham2023novelmutationcausing pages 1-2).
- **Laboratory/cellular:** elevated C26:0 and VLCFA ratios, markedly reduced plasmalogens and deficient peroxisomal oxidation/ether-lipid synthesis; absent peroxisomes by fibroblast immunofluorescence. Suggested HPO concepts include HP:0008167 Very-long-chain fatty acid accumulation and HP:0010964 Abnormality of glycolipid metabolism, supplemented by assay-specific LOINC codes (mohamed2010amutationin pages 1-2, mohamed2010amutationin pages 2-3).

Frequencies cannot be responsibly assigned. Apparent recurrence of hypotonia, dysmorphism, brain and cardiac abnormalities reflects fewer than five confirmed patients. Quality-of-life instruments have not been applied specifically to PEX19 disease. Functional impact was catastrophic: respiratory dependence, poor feeding, refractory epilepsy, repeated intensive-care admissions and death in infancy. A broader caregiver survey enrolled 92 ZSD/peroxisomal-disease families and assessed Family Quality of Life and Pediatric Inventory for Parents domains, but reported no PEX19 subgroup (NCT03440905) (NCT03440905 chunk 1).

## 4. Genetic and molecular information

### Causal gene and variants

**PEX19** encodes a 299-amino-acid, predominantly cytosolic peroxin with a C-terminal CaaX prenylation motif (matsuzono1999humanpex19cdna pages 1-2).

1. **c.763_764insA**—historically described as A764 insertion in the Met255 codon—causes a C-terminal frameshift and abnormal 24-residue tail. It was homozygous in two brothers who died at 3 and 21 days. Wild-type PEX19, but not the mutant construct, rescued their cellular defect (matsuzono1999humanpex19cdna pages 3-5, mohamed2010amutationin pages 3-4).
2. **c.320delA, p.Lys107SerfsTer13**—homozygous in a girl; both parents were carriers. She survived 16 months. Fibroblast DHAPAT activity was 0.6 nmol/hour/mg versus 0.29 and 0.39 in the original cases, providing limited evidence that residual activity tracked a less immediately lethal course (mohamed2010amutationin pages 1-2, mohamed2010amutationin pages 3-4).
3. **p.Leu94Ter**—reported as chr1:g.160283009A>T in exon 3, transcript ENST00000368072.10—was homozygous in the 2023 neonate. The paper reported an internal-database frequency of 0.002%, but did not provide a gnomAD frequency; this should not be treated as a validated population allele frequency (adiyapatham2023novelmutationcausing pages 1-2).

All are germline predicted loss-of-function alleles. No somatic PBD12A mechanism is recognized. Modern ClinVar submission status and ACMG assertions were not available in the retrieved evidence; the variants have strong disease-level evidence from homozygosity, phenotype and, for the founding allele, functional complementation. No pathogenic missense allele, structural rearrangement, chromosomal abnormality, modifier gene or disease-specific methylation signature has been established.

## 5. Environmental information

Environmental, occupational, lifestyle and infectious causes are **not applicable** to disease initiation. The 2023 sibling developed *Staphylococcus aureus* infection and the 2010 child had recurrent pneumonia and sepsis, but these were downstream complications in medically fragile infants (adiyapatham2023novelmutationcausing pages 1-2, mohamed2010amutationin pages 1-2). No diet, smoking, alcohol, radiation or pollutant association, and no proven protective exposure, has been reported.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic truncating PEX19 variants lead to** absent or severely reduced functional PEX19.
2. **Loss of PEX19 chaperone/receptor activity leads to** failure to bind and stabilize newly synthesized class-1 peroxisomal membrane proteins in the cytosol (demonstrated in human cells) (jones2004pex19isa pages 2-3, jones2004pex19isa pages 1-2).
3. **Failed PEX19–cargo delivery to PEX3/PEX16 leads to** degradation or mitochondrial mistargeting of membrane proteins and failure of peroxisomal membrane assembly (demonstrated cellularly; details of direct versus ER-vesicular routes remain debated) (argyriou2016peroxisomebiogenesisdisorders pages 5-7, jansen2019theperoxisomebiogenesis pages 1-2).
4. **Loss of a competent peroxisomal membrane leads to** failure of matrix-enzyme import and functional absence of peroxisomes. Wild-type PEX19 restores catalase/PTS1 import and morphologic peroxisomes in CG-J fibroblasts and CHO mutants, directly validating this step (matsuzono1999humanpex19cdna pages 3-3, matsuzono1999humanpex19cdna pages 5-6).
5. **Functional peroxisome loss results in** impaired VLCFA and branched-chain fatty-acid oxidation, phytanic-acid α-oxidation, plasmalogen/ether-lipid synthesis and bile-acid intermediate metabolism; the c.320delA fibroblasts directly demonstrated these defects (mohamed2010amutationin pages 1-2, mohamed2010amutationin pages 2-3).
6. **These metabolic defects lead to** VLCFA and toxic intermediate accumulation plus plasmalogen and other lipid deficiency. Defective 1-alkyl-2-acyl GPI-anchor remodeling has been demonstrated in PEX19-deficient Zellweger cells (kanzawa2012defectivelipidremodeling pages 1-2).
7. **Abnormal membrane lipids and metabolite toxicity result in** disturbed neuronal migration/myelination, hepatocellular and renal-tubular dysfunction, ocular/skeletal abnormalities and impaired organ development; assignment of individual metabolites to individual PEX19 manifestations remains partly inferred from broader ZSD biology (argyriou2016peroxisomebiogenesisdisorders pages 10-16, argyriou2016peroxisomebiogenesisdisorders pages 7-9).
8. **Multiorgan developmental dysfunction leads to** neonatal hypotonia, seizures, respiratory failure, congenital malformations, liver disease and early death.

A branch of current research concerns **peroxisome-independent PEX19 activity**: farnesylated PEX19 sorts UBXD8 and a subset of proteins to ER/lipid droplets. PEX19-null cells accumulated excess triacylglycerol and failed to mobilize neutral-lipid stores. This may modify lipid homeostasis, but its contribution to PBD12A clinical disease is unproven (lyschik2022pex19coordinatesneutral pages 1-2).

Suggested ontology annotations include **GO:0007031 peroxisome organization**, GO:0016558 protein import into peroxisome matrix, GO:0016559 peroxisome membrane biogenesis, GO:0030259 lipid glycosylation, GO:0033540 fatty-acid beta-oxidation using acyl-CoA oxidase, and GO:0006631 fatty-acid metabolic process. Relevant compartments are **GO:0005777 peroxisome**, GO:0005778 peroxisomal membrane, cytosol, ER, mitochondrion and lipid droplet.

Relevant cells include neuron (**CL:0000540**), hepatocyte (**CL:0000182**), kidney proximal-tubule epithelial cell, retinal photoreceptor, oligodendrocyte and fibroblast (**CL:0000057**). Direct cell-type mechanisms have mostly been studied in fibroblasts; assignment to neurons, hepatocytes and renal cells is based on organ pathology.

### Molecular profiling

PEX19-knockout cellular work used SILAC proteomics and lipidomics; data were deposited in PRIDE as **PXD032200** (lyschik2022pex19coordinatesneutral pages 14-15). Yeast pex19Δ profiling found altered peroxisomal and zinc-regulatory proteins, while broader ZSD models suggest peroxins can accumulate on mitochondria and impair respiration. The latter was not specifically proven in a PEX19-patient fibroblast in the retrieved text (nuebel2020msp1atad1restoresmitochondrial pages 8-10, nuebel2020msp1atad1restoresmitochondrial pages 1-3). No disease-specific single-cell, spatial-transcriptomic, epigenomic or integrated human multi-omics study was found.

## 7. Anatomical structures affected

Primary systems are the **central nervous system**, liver, kidney, eye, heart, skeleton and male genital tract; respiratory dysfunction and recurrent infection are important secondary complications. Suggested UBERON annotations include brain (**UBERON:0000955**), cerebellum (UBERON:0002037), cerebral white matter, liver (**UBERON:0002107**), kidney (**UBERON:0002113**), renal tubule, eye (**UBERON:0000970**), cornea, heart (**UBERON:0000948**), bone, testis and penis.

Pathology is generally bilateral/systemic rather than lateralized. Brain imaging changes were diffuse or bilateral in the 2010 patient, while congenital cardiac and genital lesions need not be symmetric (mohamed2010amutationin pages 1-2). At the subcellular level, the defining structure is the peroxisome/peroxisomal membrane, with secondary ER, lipid-droplet and possibly mitochondrial disturbances.

## 8. Temporal development

Onset is congenital: reduced fetal movement, growth restriction, oligohydramnios or malformations may be prenatal; hypotonia, poor feeding, apnea and dysmorphism are evident immediately after birth (mohamed2010amutationin pages 1-2). The course is rapidly progressive, not relapsing-remitting. Early stages comprise respiratory/feeding and neurologic dysfunction; later survival may reveal epilepsy, severe developmental delay, recurrent infection, liver failure, gallstones and renal Fanconi-like dysfunction. No remission has been reported.

All genetically confirmed patients died between 3 days and 16 months. The prenatal and neonatal periods are critical for diagnosis and reproductive decision-making; whether presymptomatic treatment can alter PEX19 disease is unknown.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. When both parents are heterozygous, each pregnancy has a 25% affected, 50% carrier and 25% unaffected/non-carrier probability. Penetrance of biallelic null alleles appears high, but cannot be quantified. Expressivity varies somewhat—particularly survival from days to 16 months—but remains severe. Anticipation is not expected. Germline mosaicism has not been reported but cannot be excluded after an apparently de novo result.

In the 613 unrelated ZSD fibroblast-line series, **4/613 (0.65%)** were assigned to PEX19, compared with 3/613 assigned to PEX3. This was a referral cohort, over 90% Western European, and is neither prevalence nor incidence (ebberink2011geneticclassificationand pages 3-4, ebberink2011geneticclassificationand pages 2-3). Overall ZSD birth incidence is often estimated around 1:50,000, with reported regional estimates down to 1:500,000 in Japan; these must not be represented as PBD12A-specific rates (adiyapatham2023novelmutationcausing pages 1-2, argyriou2016peroxisomebiogenesisdisorders pages 7-9).

PEX19-specific prevalence, incidence, carrier frequency, founder variants, geographic distribution and sex ratio are unknown. Confirmed cases include males and a female; no sex-dependent risk is expected for an autosomal disorder.

## 10. Diagnostics

### Recommended approach

1. Recognize a neonatal multisystem pattern: hypotonia, poor feeding/respiratory drive, seizures, dysmorphism, large fontanelles, neuronal-migration or white-matter abnormalities, hepatic dysfunction and congenital cardiac/genital/skeletal lesions.
2. Measure plasma **C26:0, C24:0/C22:0 and C26:0/C22:0**, phytanic and pristanic acids, pipecolic acid and C27 bile-acid intermediates; measure erythrocyte plasmalogens. Normal ammonia, lactate and urine organic acids do not exclude disease (adiyapatham2023novelmutationcausing pages 1-2, argyriou2016peroxisomebiogenesisdisorders pages 10-16).
3. Use fibroblast catalase/PMP immunofluorescence, VLCFA and pristanate β-oxidation, phytanate α-oxidation, DHAPAT/plasmalogen synthesis and acyl-CoA-oxidase/thiolase processing when biochemical or molecular findings are uncertain. PEX3, PEX16 and PEX19 defects are especially suggested when peroxisomal membrane remnants are absent (ebberink2011geneticclassificationand pages 1-2, mohamed2010amutationin pages 1-2).
4. Confirm two pathogenic **PEX19** alleles and parental phase. A comprehensive ZSD/peroxisomal panel is efficient; rapid trio WES or WGS is appropriate in a critically ill infant with multiple anomalies. Exome sequencing diagnosed the 2023 case after routine metabolic tests were unrevealing (adiyapatham2023novelmutationcausing pages 1-2, adiyapatham2023novelmutationcausing pages 3-4).
5. If sequencing finds one or no allele, deletion/duplication analysis, genome sequencing and RNA studies can seek structural or splice variants. CMA and karyotyping do not detect most PEX19 sequence variants and were normal in the affected sibling described in 2023 (adiyapatham2023novelmutationcausing pages 1-2).

MRI can identify neuronal migration abnormalities, delayed myelination, ventriculomegaly, colpocephaly, cerebellar hypoplasia or diffuse demyelination. EEG assesses seizures. Echocardiography, ophthalmologic evaluation, hearing testing, abdominal/renal ultrasound and serial liver, adrenal and renal-tubular studies define organ involvement.

Differential diagnoses include other PEX-gene ZSDs—especially **PEX3/PBD10A** and PEX16 disease—single-enzyme peroxisomal disorders such as ACOX1 or HSD17B4 deficiency, rhizomelic chondrodysplasia punctata, mitochondrial disease, congenital infection, lysosomal disease and other multiple-malformation syndromes. Biochemistry establishes generalized peroxisomal dysfunction; genotype identifies PBD12A.

No validated population newborn screen exists specifically for PBD12A. Cascade carrier testing and targeted familial testing are clinically applicable.

## 11. Outcome and prognosis

The observed prognosis is extremely poor. The four confirmed patients died at approximately **3 days, 21 days, 15 days and 16 months**; the untested recurrent sibling died at 15 days. Respiratory failure, pneumonia/sepsis, disseminated coagulopathy and liver failure contributed (adiyapatham2023novelmutationcausing pages 1-2, mohamed2010amutationin pages 3-4, mohamed2010amutationin pages 1-2).

There are no PEX19-specific survival curves, mortality rates or 5-/10-year survival estimates. Severe-ZSD literature indicates death usually in the first year, whereas childhood or adult survival largely concerns hypomorphic alleles in other PEX genes (argyriou2016peroxisomebiogenesisdisorders pages 7-9). No recovery has been documented. Likely adverse prognostic indicators are complete absence of peroxisomes, profoundly abnormal lipid metabolism, neonatal respiratory failure and severe liver/brain involvement; none is validated in a PEX19 prognostic model.

## 12. Treatment and real-world implementation

There is no approved curative or PEX19-directed therapy. Current care is multidisciplinary and supportive:

- respiratory support and aspiration prevention;
- individualized enteral nutrition and feeding assistance;
- antiseizure medication—phenobarbital was used in the reported sibling;
- management of cholestasis, coagulopathy and fat-soluble-vitamin deficiency;
- treatment of infection;
- renal electrolyte/bicarbonate replacement when tubular dysfunction occurs;
- hearing, vision, developmental, physical, occupational and speech support;
- orthopedic care and palliative-care involvement for severe neonatal disease (adiyapatham2023novelmutationcausing pages 1-2, mohamed2010amutationin pages 1-2).

Suggested NCIT intervention concepts include **Supportive Care**, Mechanical Ventilation, Enteral Nutrition, Anticonvulsant Therapy, Physical Therapy, Occupational Therapy, Speech Therapy, Genetic Counseling and Palliative Care.

ZSD-wide interventions should not be overgeneralized. Cholic/chenodeoxycholic/ursodeoxycholic-acid treatment has improved bile-acid biomarkers, hepatobiliary function or histology in individual cases but has not shown altered overall neurologic course (NCT00004442 chunk 1, argyriou2016peroxisomebiogenesisdisorders pages 16-18). A randomized DHA study in 48 ZSD patients showed no overall ERG or growth benefit (argyriou2016peroxisomebiogenesisdisorders pages 18-20). Betaine trial NCT01838941 enrolled 12 selected **PEX1** patients, not PEX19 cases (NCT01838941 chunk 1). Hydroxychloroquine NCT03856866 enrolled only three PEX1/PEX6/PEX26 patients and cannot support PEX19 treatment (NCT03856866 chunk 1).

Current research infrastructure includes recruiting natural-history study **NCT01668186**, estimated enrollment 244 with annual follow-up up to ten years, and retinopathy study **NCT06190626**, begun December 18, 2023 with target enrollment 30 and completion planned for 2029. Neither reports a PEX19-specific result (NCT06190626 chunk 1, NCT01668186 chunk 1). No PEX19 gene-replacement, genome-editing, RNA, cell or transplantation trial was identified.

## 13. Prevention

The molecular event cannot be prevented by lifestyle or vaccination. **Primary reproductive prevention** consists of genetic counseling, carrier testing, preimplantation genetic testing, chorionic-villus or amniotic-fluid targeted testing, and use of donor gametes where desired. The 2023 parents were specifically counseled about targeted prenatal testing in later pregnancies (adiyapatham2023novelmutationcausing pages 2-3, adiyapatham2023novelmutationcausing pages 3-4).

Secondary prevention means early molecular diagnosis and anticipatory surveillance rather than prevention of onset. Tertiary prevention includes aspiration precautions, nutritional support, vaccination according to routine schedules, prompt infection treatment, seizure control, monitoring liver/coagulation/adrenal/renal status, and sensory/rehabilitative care. No disease-specific prophylactic medication is established.

## 14. Other species and natural disease

PEX19 is evolutionarily conserved across eukaryotes. Relevant taxa include **Homo sapiens** (NCBI Taxon 9606), **Mus musculus** (10090), **Danio rerio** (7955), **Drosophila melanogaster** (7227), **Caenorhabditis elegans** (6239), *Saccharomyces cerevisiae* (4932) and *Pichia pastoris/Komagataella phaffii*.

No naturally occurring veterinary PEX19-associated syndrome, breed predisposition, zoonotic potential or cross-species transmission was identified. The disease is genetic and noninfectious. Comparative work instead uses induced mutants to establish the conserved requirement for Pex19 in organelle biogenesis (snyder1999pex19pinteractswith pages 1-2, veldhoven2013peroxisomedeficientinvertebrate pages 9-10).

## 15. Model organisms and experimental systems

- **Human patient fibroblasts:** highest disease relevance. CG-J fibroblasts lack functional peroxisomes; wild-type PEX19 restores catalase/PTS1 import and membrane assembly. Limitations are scarcity, severe/null genotypes and absence of tissue architecture (matsuzono1999humanpex19cdna pages 3-3, matsuzono1999humanpex19cdna pages 5-6).
- **Chinese hamster ovary ZP119/ZP165 cells:** rescued by human PEX19 and useful for complementation, prenylation and membrane-assembly studies. They model cell biology, not clinical organ disease (matsuzono1999humanpex19cdna pages 1-2, matsuzono1999humanpex19cdna pages 5-6).
- **Human engineered PEX19-knockout cells:** used to separate peroxisomal from lipid-droplet functions and for proteomics/lipidomics. Nonfarnesylated PEX19C296S restored catalase-positive peroxisomes in one modern study, contrasting with older experiments in which C296S did not rescue; differences in constructs and readouts indicate that the precise requirement for farnesylation remains context-dependent (matsuzono1999humanpex19cdna pages 3-5, lyschik2022pex19coordinatesneutral pages 1-2).
- ***Pichia pastoris* pex19Δ/pex19-112:** defective in PTS1/PTS2 import with cytosolic matrix proteins and small Pex3-positive membrane remnants. It is powerful for genetics and interaction mapping but lacks mammalian organs and has different prenylation requirements (snyder1999pex19pinteractswith pages 1-2).
- ***Drosophila* S2 Pex19 RNAi:** produces fewer, larger GFP-SKL-positive peroxisomes. It is a tractable morphology assay but is an incomplete knockdown in cultured insect cells (veldhoven2013peroxisomedeficientinvertebrate pages 10-11).
- ***C. elegans* Pex19 loss:** associated with embryonic lethality, demonstrating developmental essentiality but preventing later-stage analysis (veldhoven2013peroxisomedeficientinvertebrate pages 9-10).
- **Zebrafish Pex19 morpholino:** no obvious abnormality at 32 hours post-fertilization, but knockdown efficacy was not controlled; this negative result is not a validated disease model (veldhoven2013peroxisomedeficientinvertebrate pages 13-14).

No well-characterized Pex19-null mouse, patient-derived iPSC, organoid or humanized knock-in model was identified in the retrieved evidence. Generic Pex5/Pex13/Pex14 models illuminate ZSD neurodevelopment and metabolism but should not be annotated as PEX19-specific.

## Recent developments and expert interpretation

The most important recent clinical development was the **2023 report of homozygous p.Leu94Ter**, which expanded the phenotype to include corneal opacity, talipes and inferior vermian hypoplasia and showed the diagnostic utility of rapid exome sequencing when routine metabolic assays are normal (adiyapatham2023novelmutationcausing pages 1-2, adiyapatham2023novelmutationcausing pages 2-3). Current 2023–2024 mechanistic reviews retain PEX19’s receptor/chaperone role but emphasize that direct peroxisomal insertion and ER-derived vesicular routes may coexist; this uncertainty concerns trafficking detail, not the established causal relationship between PEX19 loss and membrane-biogenesis failure (rudowitz2023importandquality pages 1-2, jansen2019theperoxisomebiogenesis pages 1-2).

Representative direct abstract statements include:

> “The patient was assigned to the PEX19 complementation group.” — Mohamed et al., 2010 (mohamed2010amutationin pages 1-2)

> “Clinical exome sequencing yielded the diagnosis of Zellweger syndrome with a rare mutation in PEX-19 gene.” — Adiyapatham and Murugesan, 2023 (adiyapatham2023novelmutationcausing pages 1-2)

> PEX19 “binds and stabilizes newly synthesized PMPs in the cytosol” and functions as “both a chaperone and an import receptor.” — Jones et al., 2004 (jones2004pex19isa pages 1-2)

The principal expert conclusion is therefore high-confidence disease causality but low-confidence phenotype frequency and intervention estimates. PEX19 loss clearly abolishes an early, indispensable stage of peroxisomal membrane construction. However, the field lacks a PEX19-specific natural-history cohort, standardized outcome measures, validated prognostic biomarkers and any genotype-targeted therapy.

References

1. (OpenTargets Search: peroxisome biogenesis disorder 12A,Zellweger syndrome-PEX19): Open Targets Query (peroxisome biogenesis disorder 12A,Zellweger syndrome-PEX19, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (matsuzono1999humanpex19cdna pages 1-2): Yuji Matsuzono, Naohiko Kinoshita, Shigehiko Tamura, Nobuyuki Shimozawa, Maho Hamasaki, Kamran Ghaedi, Ronald J. A. Wanders, Yasuyuki Suzuki, Naomi Kondo, and Yukio Fujiki. Human pex19: cdna cloning by functional complementation, mutation analysis in a patient with zellweger syndrome, and potential role in peroxisomal membrane assembly. Proceedings of the National Academy of Sciences of the United States of America, 96 5:2116-21, Mar 1999. URL: https://doi.org/10.1073/pnas.96.5.2116, doi:10.1073/pnas.96.5.2116. This article has 310 citations and is from a highest quality peer-reviewed journal.

3. (matsuzono1999humanpex19cdna pages 5-6): Yuji Matsuzono, Naohiko Kinoshita, Shigehiko Tamura, Nobuyuki Shimozawa, Maho Hamasaki, Kamran Ghaedi, Ronald J. A. Wanders, Yasuyuki Suzuki, Naomi Kondo, and Yukio Fujiki. Human pex19: cdna cloning by functional complementation, mutation analysis in a patient with zellweger syndrome, and potential role in peroxisomal membrane assembly. Proceedings of the National Academy of Sciences of the United States of America, 96 5:2116-21, Mar 1999. URL: https://doi.org/10.1073/pnas.96.5.2116, doi:10.1073/pnas.96.5.2116. This article has 310 citations and is from a highest quality peer-reviewed journal.

4. (mohamed2010amutationin pages 3-4): Sarar Mohamed, Ebtisam El‐Meleagy, Abdelhaleem Nasr, Merel S. Ebberink, Ronald J.A. Wanders, and Hans R. Waterham. A mutation in pex19 causes a severe clinical phenotype in a patient with peroxisomal biogenesis disorder. American Journal of Medical Genetics Part A, 152A:2318-2321, Sep 2010. URL: https://doi.org/10.1002/ajmg.a.33560, doi:10.1002/ajmg.a.33560. This article has 15 citations.

5. (mohamed2010amutationin pages 1-2): Sarar Mohamed, Ebtisam El‐Meleagy, Abdelhaleem Nasr, Merel S. Ebberink, Ronald J.A. Wanders, and Hans R. Waterham. A mutation in pex19 causes a severe clinical phenotype in a patient with peroxisomal biogenesis disorder. American Journal of Medical Genetics Part A, 152A:2318-2321, Sep 2010. URL: https://doi.org/10.1002/ajmg.a.33560, doi:10.1002/ajmg.a.33560. This article has 15 citations.

6. (adiyapatham2023novelmutationcausing pages 1-2): Sasidharan Adiyapatham and Ambalakkuthan Murugesan. Novel mutation causing zellweger syndrome. BMJ Case Reports, 16:e252014, Mar 2023. URL: https://doi.org/10.1136/bcr-2022-252014, doi:10.1136/bcr-2022-252014. This article has 3 citations and is from a peer-reviewed journal.

7. (adiyapatham2023novelmutationcausing pages 2-3): Sasidharan Adiyapatham and Ambalakkuthan Murugesan. Novel mutation causing zellweger syndrome. BMJ Case Reports, 16:e252014, Mar 2023. URL: https://doi.org/10.1136/bcr-2022-252014, doi:10.1136/bcr-2022-252014. This article has 3 citations and is from a peer-reviewed journal.

8. (mohamed2010amutationin pages 2-3): Sarar Mohamed, Ebtisam El‐Meleagy, Abdelhaleem Nasr, Merel S. Ebberink, Ronald J.A. Wanders, and Hans R. Waterham. A mutation in pex19 causes a severe clinical phenotype in a patient with peroxisomal biogenesis disorder. American Journal of Medical Genetics Part A, 152A:2318-2321, Sep 2010. URL: https://doi.org/10.1002/ajmg.a.33560, doi:10.1002/ajmg.a.33560. This article has 15 citations.

9. (argyriou2016peroxisomebiogenesisdisorders pages 9-10): Catherine Argyriou, Maria Daniela D’Agostino, and Nancy Braverman. Peroxisome biogenesis disorders. Translational Science of Rare Diseases, 1:111-144, Sep 2016. URL: https://doi.org/10.3233/trd-160003, doi:10.3233/trd-160003. This article has 129 citations.

10. (argyriou2016peroxisomebiogenesisdisorders pages 7-9): Catherine Argyriou, Maria Daniela D’Agostino, and Nancy Braverman. Peroxisome biogenesis disorders. Translational Science of Rare Diseases, 1:111-144, Sep 2016. URL: https://doi.org/10.3233/trd-160003, doi:10.3233/trd-160003. This article has 129 citations.

11. (ebberink2011geneticclassificationand pages 1-2): Merel S. Ebberink, Petra A.W. Mooijer, Jeannette Gootjes, Janet Koster, Ronald J.A. Wanders, and Hans R. Waterham. Genetic classification and mutational spectrum of more than 600 patients with a zellweger syndrome spectrum disorder. Human Mutation, 32:59-69, Jan 2011. URL: https://doi.org/10.1002/humu.21388, doi:10.1002/humu.21388. This article has 208 citations and is from a domain leading peer-reviewed journal.

12. (argyriou2016peroxisomebiogenesisdisorders pages 10-16): Catherine Argyriou, Maria Daniela D’Agostino, and Nancy Braverman. Peroxisome biogenesis disorders. Translational Science of Rare Diseases, 1:111-144, Sep 2016. URL: https://doi.org/10.3233/trd-160003, doi:10.3233/trd-160003. This article has 129 citations.

13. (jones2004pex19isa pages 2-3): Jacob M. Jones, James C. Morrell, and Stephen J. Gould. Pex19 is a predominantly cytosolic chaperone and import receptor for class 1 peroxisomal membrane proteins. The Journal of Cell Biology, 164:57-67, Jan 2004. URL: https://doi.org/10.1083/jcb.200304111, doi:10.1083/jcb.200304111. This article has 370 citations.

14. (jones2004pex19isa pages 1-2): Jacob M. Jones, James C. Morrell, and Stephen J. Gould. Pex19 is a predominantly cytosolic chaperone and import receptor for class 1 peroxisomal membrane proteins. The Journal of Cell Biology, 164:57-67, Jan 2004. URL: https://doi.org/10.1083/jcb.200304111, doi:10.1083/jcb.200304111. This article has 370 citations.

15. (matsuzono1999humanpex19cdna pages 3-3): Yuji Matsuzono, Naohiko Kinoshita, Shigehiko Tamura, Nobuyuki Shimozawa, Maho Hamasaki, Kamran Ghaedi, Ronald J. A. Wanders, Yasuyuki Suzuki, Naomi Kondo, and Yukio Fujiki. Human pex19: cdna cloning by functional complementation, mutation analysis in a patient with zellweger syndrome, and potential role in peroxisomal membrane assembly. Proceedings of the National Academy of Sciences of the United States of America, 96 5:2116-21, Mar 1999. URL: https://doi.org/10.1073/pnas.96.5.2116, doi:10.1073/pnas.96.5.2116. This article has 310 citations and is from a highest quality peer-reviewed journal.

16. (kanzawa2012defectivelipidremodeling pages 1-2): Noriyuki Kanzawa, Nobuyuki Shimozawa, Ronald J.A. Wanders, Kazutaka Ikeda, Yoshiko Murakami, Hans R. Waterham, Satoru Mukai, Morihisa Fujita, Yusuke Maeda, Ryo Taguchi, Yukio Fujiki, and Taroh Kinoshita. Defective lipid remodeling of gpi anchors in peroxisomal disorders, zellweger syndrome, and rhizomelic chondrodysplasia punctata. Journal of Lipid Research, 53:653-663, Apr 2012. URL: https://doi.org/10.1194/jlr.m021204, doi:10.1194/jlr.m021204. This article has 29 citations and is from a peer-reviewed journal.

17. (NCT01668186 chunk 1): Nancy Braverman. Longitudinal Natural History Study of Patients With Peroxisome Biogenesis Disorders (PBD). McGill University Health Centre/Research Institute of the McGill University Health Centre. 2012. ClinicalTrials.gov Identifier: NCT01668186

18. (NCT01838941 chunk 1): Nancy Braverman. Betaine and Peroxisome Biogenesis Disorders. McGill University Health Centre/Research Institute of the McGill University Health Centre. 2013. ClinicalTrials.gov Identifier: NCT01838941

19. (NCT00004442 chunk 1):  Study of Bile Acids in Patients With Peroxisomal Disorders. University of Cincinnati. ClinicalTrials.gov Identifier: NCT00004442

20. (argyriou2016peroxisomebiogenesisdisorders pages 18-20): Catherine Argyriou, Maria Daniela D’Agostino, and Nancy Braverman. Peroxisome biogenesis disorders. Translational Science of Rare Diseases, 1:111-144, Sep 2016. URL: https://doi.org/10.3233/trd-160003, doi:10.3233/trd-160003. This article has 129 citations.

21. (ebberink2011geneticclassificationand pages 3-4): Merel S. Ebberink, Petra A.W. Mooijer, Jeannette Gootjes, Janet Koster, Ronald J.A. Wanders, and Hans R. Waterham. Genetic classification and mutational spectrum of more than 600 patients with a zellweger syndrome spectrum disorder. Human Mutation, 32:59-69, Jan 2011. URL: https://doi.org/10.1002/humu.21388, doi:10.1002/humu.21388. This article has 208 citations and is from a domain leading peer-reviewed journal.

22. (ebberink2011geneticclassificationand pages 2-3): Merel S. Ebberink, Petra A.W. Mooijer, Jeannette Gootjes, Janet Koster, Ronald J.A. Wanders, and Hans R. Waterham. Genetic classification and mutational spectrum of more than 600 patients with a zellweger syndrome spectrum disorder. Human Mutation, 32:59-69, Jan 2011. URL: https://doi.org/10.1002/humu.21388, doi:10.1002/humu.21388. This article has 208 citations and is from a domain leading peer-reviewed journal.

23. (NCT06190626 chunk 1): Nancy Braverman. Longitudinal Prospective Natural History Study of Retinopathy in Zellweger Spectrum Disorder. McGill University Health Centre/Research Institute of the McGill University Health Centre. 2023. ClinicalTrials.gov Identifier: NCT06190626

24. (NCT03440905 chunk 1):  Proxy-Reported Symptoms and Quality of Life Survey in Zellweger Spectrum Disorders. University of South Florida. 2018. ClinicalTrials.gov Identifier: NCT03440905

25. (matsuzono1999humanpex19cdna pages 3-5): Yuji Matsuzono, Naohiko Kinoshita, Shigehiko Tamura, Nobuyuki Shimozawa, Maho Hamasaki, Kamran Ghaedi, Ronald J. A. Wanders, Yasuyuki Suzuki, Naomi Kondo, and Yukio Fujiki. Human pex19: cdna cloning by functional complementation, mutation analysis in a patient with zellweger syndrome, and potential role in peroxisomal membrane assembly. Proceedings of the National Academy of Sciences of the United States of America, 96 5:2116-21, Mar 1999. URL: https://doi.org/10.1073/pnas.96.5.2116, doi:10.1073/pnas.96.5.2116. This article has 310 citations and is from a highest quality peer-reviewed journal.

26. (argyriou2016peroxisomebiogenesisdisorders pages 5-7): Catherine Argyriou, Maria Daniela D’Agostino, and Nancy Braverman. Peroxisome biogenesis disorders. Translational Science of Rare Diseases, 1:111-144, Sep 2016. URL: https://doi.org/10.3233/trd-160003, doi:10.3233/trd-160003. This article has 129 citations.

27. (jansen2019theperoxisomebiogenesis pages 1-2): Renate L. M. Jansen and Ida J. van der Klei. The peroxisome biogenesis factors pex3 and pex19: multitasking proteins with disputed functions. FEBS Letters, 593:457-474, Mar 2019. URL: https://doi.org/10.1002/1873-3468.13340, doi:10.1002/1873-3468.13340. This article has 92 citations and is from a peer-reviewed journal.

28. (lyschik2022pex19coordinatesneutral pages 1-2): Sven Lyschik, Anna A. Lauer, Tanja Roth, Daniel Janitschke, Markus Hollander, Thorsten Will, Tobias Hartmann, Ron R. Kopito, Volkhard Helms, Marcus O. W. Grimm, and Bianca Schrul. Pex19 coordinates neutral lipid storage in cells in a peroxisome-independent fashion. Frontiers in Cell and Developmental Biology, Apr 2022. URL: https://doi.org/10.3389/fcell.2022.859052, doi:10.3389/fcell.2022.859052. This article has 17 citations.

29. (lyschik2022pex19coordinatesneutral pages 14-15): Sven Lyschik, Anna A. Lauer, Tanja Roth, Daniel Janitschke, Markus Hollander, Thorsten Will, Tobias Hartmann, Ron R. Kopito, Volkhard Helms, Marcus O. W. Grimm, and Bianca Schrul. Pex19 coordinates neutral lipid storage in cells in a peroxisome-independent fashion. Frontiers in Cell and Developmental Biology, Apr 2022. URL: https://doi.org/10.3389/fcell.2022.859052, doi:10.3389/fcell.2022.859052. This article has 17 citations.

30. (nuebel2020msp1atad1restoresmitochondrial pages 8-10): Esther Nuebel, Jeffrey T Morgan, Sarah Fogarty, Jacob M Winter, Sandra Lettlova, Jordan A Berg, Yu-Chan Chen, Chelsea U Kidwell, J Alan Maschek, Katie J Clowers, Catherine Argyriou, Lingxiao Chen, Ilka Wittig, James E Cox, Minna Roh-Johnson, Nancy Braverman, Steven J Steinberg, Steven P Gygi, and Jared Rutter. Msp1/atad1 restores mitochondrial function in zellweger spectrum disease. bioRxiv, Sep 2020. URL: https://doi.org/10.1101/2020.09.19.303826, doi:10.1101/2020.09.19.303826. This article has 2 citations.

31. (nuebel2020msp1atad1restoresmitochondrial pages 1-3): Esther Nuebel, Jeffrey T Morgan, Sarah Fogarty, Jacob M Winter, Sandra Lettlova, Jordan A Berg, Yu-Chan Chen, Chelsea U Kidwell, J Alan Maschek, Katie J Clowers, Catherine Argyriou, Lingxiao Chen, Ilka Wittig, James E Cox, Minna Roh-Johnson, Nancy Braverman, Steven J Steinberg, Steven P Gygi, and Jared Rutter. Msp1/atad1 restores mitochondrial function in zellweger spectrum disease. bioRxiv, Sep 2020. URL: https://doi.org/10.1101/2020.09.19.303826, doi:10.1101/2020.09.19.303826. This article has 2 citations.

32. (adiyapatham2023novelmutationcausing pages 3-4): Sasidharan Adiyapatham and Ambalakkuthan Murugesan. Novel mutation causing zellweger syndrome. BMJ Case Reports, 16:e252014, Mar 2023. URL: https://doi.org/10.1136/bcr-2022-252014, doi:10.1136/bcr-2022-252014. This article has 3 citations and is from a peer-reviewed journal.

33. (argyriou2016peroxisomebiogenesisdisorders pages 16-18): Catherine Argyriou, Maria Daniela D’Agostino, and Nancy Braverman. Peroxisome biogenesis disorders. Translational Science of Rare Diseases, 1:111-144, Sep 2016. URL: https://doi.org/10.3233/trd-160003, doi:10.3233/trd-160003. This article has 129 citations.

34. (NCT03856866 chunk 1): Neal Sondheimer. Hydroxychloroquine Administration for Reduction of Pexophagy. The Hospital for Sick Children. 2019. ClinicalTrials.gov Identifier: NCT03856866

35. (snyder1999pex19pinteractswith pages 1-2): William B. Snyder, Klaas Nico Faber, Thibaut J. Wenzel, Antonius Koller, Georg H. Lüers, Linda Rangell, Gilbert A. Keller, and Suresh Subramani. Pex19p interacts with pex3p and pex10p and is essential for peroxisome biogenesis in pichia pastoris. Molecular biology of the cell, 10 6:1745-61, Jun 1999. URL: https://doi.org/10.1091/mbc.10.6.1745, doi:10.1091/mbc.10.6.1745. This article has 142 citations and is from a domain leading peer-reviewed journal.

36. (veldhoven2013peroxisomedeficientinvertebrate pages 9-10): Paul P. Van Veldhoven and Myriam Baes. Peroxisome deficient invertebrate and vertebrate animal models. Frontiers in Physiology, Nov 2013. URL: https://doi.org/10.3389/fphys.2013.00335, doi:10.3389/fphys.2013.00335. This article has 48 citations.

37. (veldhoven2013peroxisomedeficientinvertebrate pages 10-11): Paul P. Van Veldhoven and Myriam Baes. Peroxisome deficient invertebrate and vertebrate animal models. Frontiers in Physiology, Nov 2013. URL: https://doi.org/10.3389/fphys.2013.00335, doi:10.3389/fphys.2013.00335. This article has 48 citations.

38. (veldhoven2013peroxisomedeficientinvertebrate pages 13-14): Paul P. Van Veldhoven and Myriam Baes. Peroxisome deficient invertebrate and vertebrate animal models. Frontiers in Physiology, Nov 2013. URL: https://doi.org/10.3389/fphys.2013.00335, doi:10.3389/fphys.2013.00335. This article has 48 citations.

39. (rudowitz2023importandquality pages 1-2): Markus Rudowitz and Ralf Erdmann. Import and quality control of peroxisomal proteins. Journal of cell science, Aug 2023. URL: https://doi.org/10.1242/jcs.260999, doi:10.1242/jcs.260999. This article has 25 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Peroxisome_Biogenesis_Disorder_12A_Zellweger-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 3 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1136/bcr-2022-252014` (7 mentions) - Novel mutation causing Zellweger syndrome
  - shared terms: genetic

Weighed against this report's own most characteristic terms: `pex19`, `disease`, `peroxisome`, `patient`, `include`, `peroxisomal`, `zsd`, `disorder`, `genetic`, `fibroblast`, `biogenesis`, `severe`, `pex19-specific`, `liver`, `membrane`, `infection`, `respiratory`, `neonatal`, `renal`, `phenotype`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013951` (5 mentions) - the report calls it "if available"; MONDO calls it **peroxisome biogenesis disorder 12A (Zellweger)**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0030259` (obsolete lipid glycosylation) (1 mention)
