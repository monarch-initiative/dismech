---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-15T12:34:21.200577'
end_time: '2026-10-15T12:41:51.628229'
duration_seconds: 450.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Autosomal Recessive Spinocerebellar Ataxia 10
  mondo_id: MONDO:0013392
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 21
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 8
  validator_version: 0.3.0
term_validation:
  total_terms: 49
  verified: 44
  not_found: 1
  obsolete: 3
  unverifiable: 1
  confabulation_rate: 0.021
  labels_checked: 44
  labels_matching: 21
  labels_mismatched: 11
  mislabelled_terms:
  - term_id: HP:0004311
    reported_labels:
    - Coenzyme Q10 deficiency
    ontology_label: Abnormal macrophage morphology
  - term_id: HP:0000646
    reported_labels:
    - Downbeat nystagmus
    ontology_label: Amblyopia
  - term_id: HP:0000519
    reported_labels:
    - Saccadic eye movements
    ontology_label: Developmental cataract
  - term_id: HP:0006887
    reported_labels:
    - Executive dysfunction
    ontology_label: obsolete Intellectual disability, progressive
  - term_id: HP:0006956
    reported_labels:
    - Frontal lobe dysfunction
    ontology_label: Lateral ventricle dilatation
  - term_id: HP:0001605
    reported_labels:
    - Stridor
    ontology_label: Vocal cord paralysis
  - term_id: HP:0000558
    reported_labels:
    - Retinal degeneration
    ontology_label: Rieger anomaly
  - term_id: HP:0001750
    reported_labels:
    - Young adult onset
    ontology_label: Single ventricle
  - term_id: CHEBI:1709
    reported_labels:
    - coenzyme Q10
    ontology_label: CHEBI_1709
  - term_id: GO:0032839
    reported_labels:
    - axonal degeneration
    ontology_label: dendrite cytoplasm
  - term_id: GO:0014002
    reported_labels:
    - glial activation
    ontology_label: astrocyte development
  labels_variant: 12
  unresolved_terms:
  - HP:0003408
  obsolete_terms:
  - term_id: HP:0006887
    ontology_label: obsolete Intellectual disability, progressive
    replaced_by: HP:0001249
  - term_id: CHEBI:1709
    ontology_label: CHEBI_1709
    replaced_by: CHEBI:15494
  - term_id: GO:0070997
    ontology_label: obsolete neuron death
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Spinocerebellar Ataxia 10
- **MONDO ID:** MONDO:0013392 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Spinocerebellar Ataxia 10** covering all of the
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

# Autosomal Recessive Spinocerebellar Ataxia 10 (SCAR10): Comprehensive Disease Characteristics Report

Autosomal recessive spinocerebellar ataxia 10 (SCAR10), also known as adult-onset autosomal recessive cerebellar ataxia associated with ANO10, is a very rare monogenic neurodegenerative disorder characterized by slowly progressive cerebellar ataxia, pyramidal signs, oculomotor abnormalities, and variable cognitive decline, peripheral neuropathy, epilepsy, and bladder or bowel dysfunction.[4][5][9] At the molecular level, SCAR10 is caused by biallelic loss-of-function variants in the ANO10 gene, which encodes anoctamin 10 (TMEM16K), a broadly expressed member of the calcium-activated chloride channel family with particularly high expression in the cerebellum and cerebral cortex.[14][18] Clinical series and case reports since the first description in 2010 have refined the phenotype, highlighted coenzyme Q10 (CoQ10) deficiency as a potentially treatable biochemical feature, and increasingly documented extracebellar involvement including corticospinal tract signs, frontal lobe hypometabolism, and motor neuron involvement.[10][15][19] Recent in vitro work using CRISPR/Cas9-engineered ANO10-deficient neuronal cell lines has provided the first proteomic map of SCAR10-related cellular perturbations, implicating disrupted synaptic function, cell cycle regulation, extracellular matrix remodeling, and immune homeostasis as calcium-linked pathways that may drive neurodegeneration.[7] This report synthesizes current knowledge across clinical, genetic, mechanistic, and translational domains to support structured representation of SCAR10 in a disease knowledge base, with explicit attention to ontology mapping (MONDO, HPO, GO, CL, UBERON, NCIT), evidence types, and remaining knowledge gaps.

## 1. Disease Information

### 1.1 Definition and Clinical Overview

Autosomal recessive spinocerebellar ataxia 10 (SCAR10) is an inherited neurodegenerative ataxia that primarily affects the cerebellum and corticospinal tracts, leading to progressive impairment of gait, limb coordination, speech, and eye movements.[5][10][12] OMIM describes SCAR10 (MIM #613728) as “an autosomal recessive neurodegenerative disorder with onset in the teenage or young adult years of gait and limb ataxia, dysarthria, and nystagmus associated with marked cerebellar atrophy on brain imaging,” based on the original multi-family description by Vermeer et al. in 2010 (Am J Hum Genet 87:813–819, PMID: 21092923).[10][14] Orphanet similarly defines “adult-onset autosomal recessive cerebellar ataxia” under ORPHA:284289—explicitly equating it with SCAR10—as a rare cerebellar ataxia presenting in adulthood with slowly progressive spinocerebellar ataxia, gait and appendicular ataxia, dysarthria, ocular movement anomalies, increased deep tendon reflexes, and progressive cognitive decline, with additional variable features such as proximal leg muscle wasting and fasciculations, pes cavus, inspiratory stridor, epilepsy, retinal degeneration, cataracts, and lower motor neuron involvement on EMG.[9] MedGen (Concept ID C3150998) echoes this definition and emphasizes the autosomal recessive inheritance and ANO10 locus on chromosome 3p22.1–p21.33.[3][5]

Clinically, SCAR10 belongs to the broader category of autosomal recessive cerebellar ataxias (ARCA) and autosomal recessive spinocerebellar ataxias (SCAR), which are characterized by progressive cerebellar degeneration often accompanied by involvement of corticospinal tracts, peripheral nerves, and sometimes extra-neurological systems.[4][12][17] SCAR10 is among the better-defined but still extremely rare subtypes, with prevalence estimated by Orphanet at less than 1 per 1,000,000 in the general population.[9] The disorder typically begins in late adolescence or early adulthood, although reported onset ages range from early teens to the fourth decade, and progression is generally slow over many years.[4][5][10] Neuroimaging consistently shows marked cerebellar atrophy, and newer functional imaging data reveal hypometabolism not only in the cerebellum but also in the frontal lobes, suggesting broader network involvement.[1][19]

It is important to distinguish SCAR10 from spinocerebellar ataxia 10 (SCA10), an autosomal dominant repeat expansion disorder caused by ATTCT pentanucleotide expansion in the ATXN10 gene on chromosome 22q13.31 (OMIM #603516), which has a different inheritance pattern, genetic mechanism, and phenotype.[2][6] The use of “spinocerebellar ataxia 10” in older literature without explicit reference to autosomal recessive inheritance or ANO10 can cause confusion; current classifications (OMIM, Orphanet, MedGen, GeneReviews) consistently reserve “SCAR10” or “autosomal recessive spinocerebellar ataxia 10” for the ANO10-linked recessive disorder.[5][9][10][12]

### 1.2 Key Identifiers and Ontology Mapping

SCAR10 is referenced across multiple biomedical databases with a fairly consistent set of identifiers and synonyms, which facilitates ontology alignment for knowledge-base representation. OMIM assigns phenotype entry #613728 to “Spinocerebellar ataxia, autosomal recessive 10” and links it to the ANO10 gene (MIM #613726) at 3p22.1–p21.33.[10][14] Orphanet lists “Adult-onset autosomal recessive cerebellar ataxia” with ORPHA:284289 and explicitly notes “Autosomal recessive spinocerebellar ataxia type 10; SCAR10” as synonyms.[9] MedGen maps the concept “Autosomal recessive spinocerebellar ataxia 10” to UMLS C3150998 with ANO10 as the associated gene and cross-references OMIM 613728.[3][5]

The disease is included in the Mondo Disease Ontology as MONDO:0013392 (“autosomal recessive spinocerebellar ataxia 10”), as noted in ClinGen’s Gene Curation Coalition (GenCC) submissions confirming the gene–disease relationship.[11][16] SNOMED CT includes terms such as “SCAR10 - autosomal recessive spinocerebellar ataxia type 10” and “Adult-onset autosomal recessive cerebellar ataxia” under codes like 785302009.[3][9] ICD-10 coding generally uses G11.2 (“hereditary ataxia”) as the most appropriate category, consistent with Orphanet’s mapping.[9] There is not yet an ICD-11-specific code uniquely dedicated to SCAR10; instead, it would fall under hereditary or degenerative ataxia groupings. In Human Phenotype Ontology (HPO), SCAR10 is associated with terms such as “Ataxia” (HP:0001251), “Gait ataxia” (HP:0002066), “Cerebellar atrophy” (HP:0001272), “Dysarthria” (HP:0001260), “Nystagmus” (HP:0000639), “Hyperreflexia” (HP:0001347), and “Coenzyme Q10 deficiency” (HP:0004311).[5][12][15]

From a gene standpoint, ANO10 is recorded in HGNC as “ANO10” (HGNC ID corresponding to gene symbol ANO10) and in NCBI Gene as Gene ID 55129 (“anoctamin 10”), described as encoding a transmembrane protein in the TMEM16/anoctamin family of calcium-activated chloride channels.[18][14] This gene is directly associated with SCAR10 in ClinGen/GenCC, OMIM, MedGen, Orphanet, and GeneReviews.[5][10][12][16] Collectively, these identifiers provide a coherent ontology backbone for SCAR10 that can be mapped to MONDO, UMLS, SNOMED CT, ICD-10, HPO, HGNC, and other vocabularies.

### 1.3 Synonyms and Alternative Names

SCAR10 has accumulated several synonyms reflecting its discovery history and evolving nosology. OMIM notes that “autosomal recessive spinocerebellar ataxia-10 (SCAR10) is also known as autosomal recessive cerebellar ataxia type 3 (ARCA3).”[4][10] Orphanet lists “Autosomal recessive spinocerebellar ataxia type 10” and “SCAR10” as synonyms for “Adult-onset autosomal recessive cerebellar ataxia.”[9] MedGen similarly enumerates “Autosomal recessive spinocerebellar ataxia type 10; autosomal recessive spinocerebellar ataxia type 10 (SCAR10); Spinocerebellar ataxia, autosomal recessive 10” under a single concept ID.[3][5]

Early genetic reports also refer to “autosomal recessive cerebellar ataxia type 3 (ARCA3)” and “autosomal recessive spinocerebellar ataxia type 10” as essentially synonymous entities linked to ANO10 mutations.[4][10][19] GeneReviews includes SCAR10 within the broader category of autosomal recessive cerebellar ataxias and abbreviates it as “SCAR10 (ANO10-related ARCA).”[12][17] In clinical practice, “ANO10-related ataxia” or “ANO10-associated autosomal recessive cerebellar ataxia” are sometimes used to emphasize the genetic basis. All of these terms refer to the same ANO10-driven disorder and should be harmonized in a knowledge base to avoid duplication.

### 1.4 Nature of Information Sources

Current knowledge about SCAR10 is derived almost entirely from aggregated analyses of individual patients, including family-based linkage studies, case reports, small case series, and a few gene-focused screening cohorts, rather than large registries or population-level datasets. The foundational description by Vermeer et al. (2010, Am J Hum Genet, PMID: 21092923) involved linkage analysis and targeted next-generation sequencing in a few consanguineous families, culminating in the identification of ANO10 mutations as the cause of autosomal recessive cerebellar ataxia.[10][14][16] Subsequent reports such as Balreira et al. (2014, J Neurol, PMID: 25182700) and Nanetti et al. (2019, J Neurol, PMID: 30515630) add additional families and refine phenotypic details, but each involves relatively small numbers of affected individuals.[15][18][19]

Orphanet and MedGen synthesize data from these published cases and expert-curated resources into disease-level summaries, and ClinGen/GenCC provides structured gene–disease validity assessments based on the same underlying body of literature.[3][5][11][16] The rare nature of SCAR10 means that large-scale epidemiological studies, randomized clinical trials, and longitudinal registries have not yet been reported. Thus, most clinical statistics (such as prevalence, age of onset distributions, and phenotype frequencies) are inferred from a small number of patients and should be considered approximations. Mechanistic data, by contrast, increasingly include in vitro experimental results, particularly the recent proteomic profiling of ANO10-deficient neuronal cell lines, but still lack extensive in vivo animal model characterization in the provided sources.[7]

## 2. Etiology

### 2.1 Primary Causal Factors: ANO10 Variants

SCAR10 is fundamentally a Mendelian monogenic disorder caused by biallelic pathogenic variants in the ANO10 gene, encoding the anoctamin 10 / TMEM16K protein.[4][5][10] OMIM states explicitly that “autosomal recessive spinocerebellar ataxia-10 (SCAR10) is caused by homozygous or compound heterozygous mutation in the ANO10 gene (613726) on chromosome 3p22,” based on genetic linkage and sequencing data from three unrelated families in which affected individuals carried such variants.[10][14] Vermeer et al. demonstrated that, in a remotely consanguineous Dutch family with autosomal recessive cerebellar ataxia, homozygosity mapping identified a 12.5 Mb region on chromosome 3p, and targeted next-generation sequencing within this interval revealed homozygous or compound heterozygous ANO10 mutations segregating with disease.[10][14][16] In additional consanguineous families of Romani origin, similar homozygous ANO10 variants were found in affected siblings with cerebellar ataxia, confirming the causal relationship.[10][14]

Subsequent studies have consistently linked ANO10 mutations to SCAR10 phenotypes. Balreira et al. identified compound heterozygous ANO10 variants in two adults with cerebellar ataxia and CoQ10 deficiency, noting that “mutations in ANO10… [are] the causative gene for autosomal recessive spinocerebellar ataxia-10 (SCAR10)” and that the variants segregated with disease in their families.[15][18] Nanetti et al. performed mutational screening in recessive ataxia cohorts and confirmed that ANO10 mutations account for a subset of unexplained ataxia cases, helping refine the clinical phenotype.[18][19] ClinGen’s GenCC curation summarizes that there is “definitive evidence supporting the relationship between ANO10 and autosomal recessive cerebellar ataxia,” based on replicated findings in both research and diagnostic settings over time.[16][11]

At the molecular level, the ANO10 protein is a member of the anoctamin (TMEM16) family of presumed calcium-activated chloride channels, with eight transmembrane domains and cytosolic N- and C-termini.[14][18] Quantitative expression analyses show that ANO10 is highly expressed in adult brain, especially cerebellum and frontal and occipital cortices, with lower expression in fetal brain, and is also found in retina and heart, consistent with the neurological and sometimes ophthalmologic manifestations of SCAR10.[14] The causal factor in SCAR10 is therefore a germline, biallelic loss-of-function in ANO10 leading to disruption of calcium-dependent membrane transport functions in neurons and possibly other cell types, as expanded in the mechanistic section.

### 2.2 Genetic Risk Factors and Variant Spectrum

Within the monogenic etiologic framework, the main genetic risk factor is carrying two pathogenic ANO10 alleles, either in the homozygous or compound heterozygous state. OMIM and associated literature describe multiple variant types, including splice-site mutations, nonsense mutations, frameshift insertions or deletions, and possibly some missense variants that severely impair protein function.[10][14][18] For example, Vermeer et al. reported a G-to-T transversion in intron 9 (1476+1G>T) predicted to disrupt splicing, and a deletion at nucleotide 1604 leading to premature termination at codon 535 (L535X), in affected individuals from one of the original families.[10][14] Balreira et al. found compound heterozygous mutations c.132_133insT (p.Asp45Argfs*53) in exon 2 and c.1315G>T (p.Glu382*) in exon 6 in two unrelated patients with ataxia and CoQ10 deficiency.[15][18]

More recent case reports continue to expand the mutational spectrum. A Japanese patient was found to harbor a novel homozygous deletion c.616delG (p.Glu206Lysfs*17), causing a frameshift and early truncation; the authors note that this variant leads to adult-onset slowly progressive spastic ataxia with cerebellar atrophy and mild cognitive decline.[4] Another study reports SCAR10 associated with a c.289delA ANO10 variant, illustrating that small frameshift deletions are recurring loss-of-function mechanisms.[8] Widening phenotype series describe additional ANO10 variants, some novel, in compound heterozygous configurations in adults with ataxia, corticospinal signs, and executive cognitive dysfunction.[1][19] ClinVar includes at least one splice-site variant, NM_018075.5(ANO10):c.1219-1G>T, classified as pathogenic based on ACMG guidelines and clinical testing, further reinforcing that canonical splice disruption is a recognized disease mechanism.[13]

At present, there is no evidence from the provided sources that heterozygous ANO10 variants alone confer an increased risk of ataxia or related phenotypes; heterozygous carriers in families appear clinically unaffected, consistent with the autosomal recessive inheritance pattern.[10][15][16] Nor are there reports of common susceptibility alleles, modifier polymorphisms, or GWAS-identified risk loci specific to SCAR10 in population-based studies. Thus, ANO10 loss-of-function variants act as necessary and sufficient genetic causal factors when biallelic, with carrier status being the primary genetic risk factor at the family-planning level but not for clinical disease in a single generation.

### 2.3 Environmental and Lifestyle Risk Factors

Available SCAR10 literature and curated resources do not identify any specific environmental, occupational, or lifestyle exposures that increase the risk of developing the disease beyond the genetic requirement of biallelic ANO10 mutation. Orphanet notes autosomal recessive inheritance and adult onset but does not list environmental risk modifiers such as toxins, diet, or physical activity.[9] OMIM, MedGen, ClinGen, and GeneReviews focus entirely on the genetic basis and clinical phenotype, without implicating particular environmental exposures.[5][10][12][16] Unlike multifactorial neurodegenerative disorders such as sporadic ataxias or Parkinson disease, SCAR10 does not appear to have a significant non-genetic component in its etiology.

Nevertheless, as with other hereditary ataxias, general factors such as age and sex may influence disease expression or progression. SCAR10 typically manifests in teenage years or young adulthood, implying an age-dependent penetrance associated with neurodevelopmental or neurodegenerative processes.[5][10] There is no clear sex predilection described, and case series include both male and female patients.[4][10][19] Lifestyle factors such as alcohol consumption, smoking, and physical activity levels may modulate symptom severity or progression in a nonspecific manner, but this has not been systematically studied or reported for SCAR10. In the absence of disease-specific data, environmental risk factors are best considered unknown or negligible relative to the overriding genetic cause.

### 2.4 Protective Factors and Gene–Environment Interactions

No genetic protective variants specifically mitigating SCAR10 risk have been reported in the ANO10 locus or elsewhere. The rarity of the disease and the small size of reported cohorts make it difficult to detect protective alleles or modifier loci, and no GWAS or candidate-gene studies aimed at SCAR10 susceptibility or severity have been conducted in the literature represented by the provided sources.[5][10][16] Similarly, there is no evidence of environmental exposures that reduce the risk of SCAR10 in individuals with biallelic ANO10 mutations.

However, there is emerging evidence that metabolic supplementation—specifically coenzyme Q10—may exert a protective or disease-modifying effect in individuals with SCAR10 who exhibit CoQ10 deficiency. Balreira et al. observed that “in two patients with adult-onset cerebellar ataxia and coenzyme Q10 (CoQ10) deficiency in muscle, whole exome sequencing revealed mutations in ANO10,” and they further reported that “some patients have low levels of CoQ10 in muscle and may show some clinical improvement with CoQ10 treatment.”[5][15] This suggests that CoQ10 supplementation could partially compensate for mitochondrial dysfunction secondary to ANO10 loss, thereby modifying disease course. Such an effect would be categorized as a tertiary preventive or therapeutic protective factor rather than a primary etiologic modifier.

Gene–environment interactions specific to SCAR10 have not been characterized. One illustrative but possibly incidental finding from the 2022 case series is that one SCAR10 patient with temporal lobe epilepsy carried a heterozygous variant in CACNB4, a gene associated with epilepsy risk, suggesting a potential genetic interaction influencing seizure propensity.[1][19] The authors treat CACNB4 as a potential risk gene for epilepsy superimposed on SCAR10, but the causal relationship remains speculative. Beyond this, no systematic gene–environment interaction studies (e.g., CTD, PheGenI, GxE analyses) are available for SCAR10. For the purposes of knowledge-base modeling, SCAR10 should therefore be represented as a primarily monogenic disorder with minimal known environmental etiologic contribution, while allowing room for future discovery of modifiers.

## 3. Phenotypes

### 3.1 Core Neurological Phenotype

SCAR10 is defined clinically by a triad of gait and limb ataxia, dysarthria, and nystagmus, all associated with marked cerebellar atrophy on brain imaging.[5][9][10] Vermeer et al. reported that affected siblings in Dutch and Romani families developed “spinocerebellar ataxia between ages 20 and 35 years,” with features including “impaired coordination of limbs and gait, dysarthria, hyperreflexia, and gaze-evoked downbeat nystagmus with hypermetric saccades.”[10][14] Orphanet similarly describes adult-onset “slowly progressive spinocerebellar ataxia, manifesting with gait and appendicular ataxia, dysarthria, ocular movement anomalies (e.g. horizontal, vertical, and/or downbeat nystagmus, hypermetric saccades), [and] increased deep tendon reflexes.”[9] These neurological manifestations fall under HPO categories such as Ataxia (HP:0001251), Gait ataxia (HP:0002066), Limb ataxia (HP:0003390), Dysarthria (HP:0001260), Nystagmus (HP:0000639), Hyperreflexia (HP:0001347), and Pyramidal signs (e.g., Spasticity, HP:0001257).

The progression of motor symptoms is typically slow but inexorable. Balreira et al. note that their two patients “presented with slowly progressive ataxia and dysarthria leading to severe disability in the sixth decade,” indicating several decades of symptom evolution.[15] The Japanese case described adult-onset “slowly progressive spastic ataxia” with cerebellar atrophy and mild cognitive decline.[4] Nanetti et al., in a mutational screening cohort, report that ANO10 mutations are associated with cerebellar ataxia with variable additional features, but consistently involve progressive gait and limb coordination impairment.[18][19] Functionally, these core phenotypes severely affect daily activities including walking, balance, fine motor tasks, and speech, and map to quality-of-life domains such as mobility, self-care, and usual activities in tools like EQ-5D or SF-36, although formal QOL studies specific to SCAR10 have not been published in the provided sources.

From a pathophysiological standpoint, these core symptoms reflect degeneration and dysfunction of cerebellar Purkinje cells and circuits, as supported by imaging and mechanistic data. Brain MRI universally shows marked cerebellar atrophy, often with relative sparing of supratentorial structures, particularly early in disease.[4][5][10] HPO terms “Cerebellar atrophy” (HP:0001272) and “Cerebellar degeneration” (HP:0007033) are therefore integral to SCAR10’s phenotype ontology. The pyramidal signs (spasticity, hyperreflexia) suggest additional involvement of corticospinal tracts, consistent with the “spinocerebellar” designation.[4][9][10] Collectively, these features define SCAR10 as a mixed cerebellar–pyramidal ataxia syndrome with slow progression.

### 3.2 Oculomotor, Cognitive, and Motor Neuron Features

Beyond core ataxia, SCAR10 frequently involves oculomotor abnormalities, cognitive changes, and lower motor neuron signs. Oculomotor anomalies, including horizontal, vertical, and downbeat nystagmus and hypermetric saccades, are reported in the original OMIM summary and in Orphanet’s description.[9][10] GeneReviews lists ANO10-related ataxia among hereditary ataxias characterized by downbeat nystagmus and fasciculations.[12][17] These manifestations can be represented by HPO terms such as “Downbeat nystagmus” (HP:0000646), “Saccadic eye movements” (HP:0000519), and “Abnormal ocular motility” (HP:0000496), and they contribute to visual instability, reading difficulties, and dizziness, impacting daily functioning.

Cognitive impairment, particularly executive dysfunction, is increasingly recognized in SCAR10. Orphanet notes “progressive cognitive decline” as part of the core description.[9] The 2022 case series explicitly states that both reported patients “presented corticospinal tract signs, eye movement abnormalities and cognitive executive impairment” and that FDG-PET demonstrated reduced metabolic activity in the cerebellum and frontal lobes.[1][19] The Japanese case had “mild cognitive decline,” while Balreira et al. mention that some SCAR10 patients in the literature exhibit cognitive deficits.[4][15] These findings align with the concept of cerebellar cognitive affective syndrome, wherein cerebellar pathology leads to frontal-executive and affective disturbances via cerebrocerebellar circuits. HPO terms such as “Cognitive impairment” (HP:0100543), “Executive dysfunction” (HP:0006887), and “Frontal lobe dysfunction” (HP:0006956) are appropriate mappings.

Lower motor neuron involvement is documented by Orphanet and OMIM. Orphanet notes that EMG “shows evidence of lower motor neuron involvement,” and OMIM reports that two siblings in Vermeer’s Dutch family had “mild atrophy of the upper part of the lower limbs with fasciculations and EMG evidence of lower motor neuron involvement.”[9][10] These features correspond to HPO terms “Muscle weakness” (HP:0001324), “Muscle atrophy” (HP:0003202), and “Fasciculations” (HP:0003408), and they contribute to functional decline in walking, standing, and fine motor control. Their presence underscores that SCAR10 is not purely a cerebellar disorder but involves broader motor system degeneration.

### 3.3 Additional Neurological and Systemic Features

SCAR10 can present with a range of additional, variably penetrant features involving peripheral nerves, bladder and bowel function, sensory systems, and seizure propensity. Orphanet lists “proximal leg muscle wasting and fasciculations, pes cavus, inspiratory stridor, epilepsy, retinal degeneration and cataracts” as additional variable features in adult-onset autosomal recessive cerebellar ataxia/SCAR10.[9] The OMIM summary and Balreira’s report mention that some patients have bladder and bowel dysfunction, including vesicorectal disturbances.[4][5][15] Polyneuropathy is also noted as a possible manifestation in SCAR10 patients, implying peripheral nerve degeneration.[4][9]

Epilepsy appears to be an occasional but noteworthy feature. Orphanet lists epilepsy among variable manifestations, and the 2022 case series describes a woman with SCAR10 who had temporal lobe epilepsy and carried a heterozygous CACNB4 variant, which the authors considered a potential epilepsy risk gene.[1][9][19] The Japanese case report notes that epilepsy is part of the broader SCAR10 phenotype spectrum.[4] HPO terms such as “Seizure” (HP:0001250), “Epilepsy” (HP:0001250), and more specific descriptors (e.g., “Temporal lobe epilepsy,” HP:0002269) can be applied where detailed seizure types are known.

Non-neurological features, though less common, may include retinal degeneration and cataracts, as noted by Orphanet, suggesting ocular involvement beyond oculomotor symptoms.[9] Autonomic dysfunction manifesting as bladder and bowel disturbances, inspiratory stridor, and vesicorectal problems indicates involvement of autonomic pathways or muscles of respiration and pelvic floor.[4][5][9][15] These can be mapped to HPO terms such as “Neurogenic bladder” (HP:0000011), “Constipation” (HP:0002019), “Stridor” (HP:0001605), and “Retinal degeneration” (HP:0000558). While not present in all patients, these features expand SCAR10 from a purely motor ataxia to a multisystem neurodegenerative syndrome.

### 3.4 Age of Onset, Severity, Progression, and Quality-of-Life Impact

SCAR10 typically begins in adolescence or young adulthood, but onset can range from early teens to mid-adulthood. OMIM summarizes that onset is “in the teenage or young adult years,” with ages 13–15 in Romani siblings and 20–35 in the Dutch family.[10] Orphanet defines adult onset by noting that the disorder appears in adulthood and progresses slowly.[9] Case reports confirm variability: the Japanese patient had adult-onset spastic ataxia, while Balreira’s patients developed symptoms in adulthood and became severely disabled in their sixth decade.[4][15] Thus, the typical age-of-onset category for HPO mapping is “Young adult onset” (HP:0001750) or “Adult onset” (HP:0003581), with possible “Adolescent onset” (HP:0003621) in some cases.

Severity varies but tends to progress to substantial disability, particularly in motor domains. Balreira et al. explicitly state that their patients’ slowly progressive ataxia and dysarthria led to “severe disability in the sixth decade,” implying dependence on aids or caregivers for mobility and communication.[15] The Japanese case was described as slowly progressive but had accumulating spasticity and ataxia.[4] Long-term natural history data are limited, but the progressive nature of cerebellar atrophy and core symptoms is clear across case series.[4][5][10][15][19] Disease progression is best characterized as chronic and slowly progressive rather than relapsing or episodic, fitting HPO “Progressive” (HP:0003677) disease course.

Quality-of-life impact is profound, although detailed quantitative studies using established QOL instruments are not available in the provided sources. Impairments in gait, coordination, speech, and vision directly interfere with mobility, communication, employment, and social participation. Cognitive decline and executive dysfunction further affect decision-making, planning, and independence.[1][9][19] Autonomic and motor neuron features contribute to difficulties with continence, breathing, and muscle function, adding to overall disability. In a knowledge base, SCAR10 should be linked to generic QOL terms reflecting severe limitations in mobility, self-care, and usual activities, similar to other progressive hereditary ataxias described in GeneReviews.[12][17] Clinically, comprehensive assessment of functional status using scales like the Scale for the Assessment and Rating of Ataxia (SARA) or modified Rankin Scale would be valuable, though SCAR10-specific data have not been systematically reported.

## 4. Genetic and Molecular Information

### 4.1 ANO10 Gene Structure, Function, and Expression

ANO10 (anoctamin 10; TMEM16K) is the sole causal gene for SCAR10 in current knowledge. OMIM locates ANO10 at chromosome 3p22.1–p21.33 and notes that the protein belongs to the family of calcium-activated chloride channels reviewed by Hartzell et al. (2009).[14] NCBI Gene describes ANO10 as encoding a transmembrane protein with eight membrane-spanning domains and cytosolic N- and C-termini, belonging to the anoctamin/transmembrane 16 family.[18] These channels typically mediate calcium-dependent chloride conduction across membranes, influencing processes such as membrane excitability, secretion, and cell volume regulation.

Expression studies cited by OMIM indicate that ANO10 is broadly expressed, with highest levels in adult brain, followed by retina and heart, and lower expression in fetal brain.[14] Within adult brain, ANO10 expression peaks in frontal and occipital cortices and in the cerebellum, which aligns with SCAR10’s characteristic cerebellar atrophy, frontal lobe hypometabolism on FDG-PET, and potential visual pathway involvement.[1][14][19] This spatial expression pattern helps explain why ANO10 loss-of-function manifests predominantly as cerebellar ataxia with corticospinal and cognitive involvement, and supports the use of anatomical ontology terms such as UBERON “cerebellum,” “frontal lobe,” and “occipital cortex” in disease modeling.

At the functional level, ANO10 is hypothesized to act as an intracellular or plasma-membrane Ca\(^{2+}\)-dependent Cl\(^{-}\) transporter in neurons, particularly Purkinje cells, contributing to calcium homeostasis and synaptic function.[7][14][18] GeneReviews and OMIM cite previous work proposing ANO10-mediated calcium dysregulation in Purkinje cells as a key pathogenic mechanism in SCAR10.[7][12][14] Although detailed electrophysiological characterization of ANO10 channels is limited in the provided sources, the protein’s membership in the TMEM16 family and the association of SCAR10 with calcium-linked pathways in proteomic studies support the assignment of GO molecular function terms such as “calcium-activated chloride channel activity” (GO:0005227) and biological process terms like “regulation of calcium ion transport” (GO:0051924) and “synaptic transmission” (GO:0007268).

### 4.2 Spectrum and Classification of Pathogenic Variants

SCAR10-related ANO10 variants span multiple classes, predominantly loss-of-function changes. Vermeer et al. reported four different mutations across three families, including a splice-site mutation (1476+1G>T) and a frameshift leading to truncation at codon 535 (L535X), both predicted to abolish normal protein function.[10][14] Balreira et al. found c.132_133insT (p.Asp45Argfs*53), a frameshift insertion in exon 2, and c.1315G>T (p.Glu382*), a nonsense mutation in exon 6, again producing truncated proteins.[15][18] The Japanese case featured c.616delG (p.Glu206Lysfs*17), a novel homozygous deletion causing early truncation.[4] A separate report associated SCAR10 with c.289delA, another frameshift deletion.[8] These variants fall into ACMG classes “pathogenic” or “likely pathogenic” based on predicted loss-of-function in a gene where such variants are a known disease mechanism, segregation with disease, and absence or rarity in population databases.[10][13][15][18]

ClinVar provides an example of a splice-site variant, NM_018075.5(ANO10):c.1219-1G>T, classified as pathogenic by a single clinical laboratory using ACMG criteria.[13] GenCC’s ClinGen curation, drawing on multiple reports, concludes that evidence for ANO10’s association with autosomal recessive cerebellar ataxia is “definitive,” emphasizing that numerous pathogenic variants have been identified across independent families and research cohorts.[16][11] NCBI Gene’s bibliographic references include Nanetti et al. (2019), who performed mutational screening in AR ataxia and found ANO10 variants in approximately 5% of a particular cohort, suggesting that while ANO10 mutations are rare overall, they are a noteworthy cause among unexplained recessive ataxias.[18][19]

Allele frequency data for specific ANO10 variants are not detailed in the provided sources. However, the nature of the mutations—frameshift, nonsense, and canonical splice-site changes—combined with the extreme rarity of SCAR10 and the observation that these variants are absent or extremely rare in population databases (e.g., gnomAD) in the original publications strongly supports their classification as loss-of-function, disease-causing variants.[10][15][18] For knowledge-base purposes, ANO10 variants should be mapped to HGNC “ANO10,” OMIM 613726, and classified as germline, autosomal recessive, loss-of-function pathogenic variants, with variant types annotated as frameshift, nonsense, splice-site, and sometimes missense where functional data confirm pathogenicity.

### 4.3 Germline Origin, Penetrance, and Somatic Considerations

All SCAR10-causal ANO10 variants described in the literature and curated resources are germline, inherited in an autosomal recessive fashion. Vermeer et al.’s linkage analysis in consanguineous families, the segregation of variants with disease in Balreira’s families, and the consanguineous context of the Japanese and Romani families all support germline inheritance.[4][10][15] ClinVar’s pathogenic ANO10 variants are noted as germline in origin.[13] There is no indication of somatic ANO10 mutations contributing to SCAR10 or other neurologic phenotypes in the provided data, and databases like COSMIC or TCGA are not referenced in relation to ANO10 in these contexts.[13][18]

Penetrance appears to be high for individuals with biallelic loss-of-function ANO10 variants, as virtually all reported homozygous or compound heterozygous individuals have developed ataxia and related symptoms by early or mid-adulthood.[4][5][10][15][19] Age-dependent penetrance is implicit in the typical teenage–young adult onset. Heterozygous carriers, including parents and siblings in affected families, are described as clinically unaffected, consistent with recessive inheritance and near-complete penetrance among biallelic carriers.[10][15][16] Germline mosaicism has not been reported, likely due to the rarity of SCAR10 and the scarcity of large multigenerational pedigrees.

### 4.4 Modifier Genes, Epigenetics, and Structural Genomic Features

Specific modifier genes that alter SCAR10 severity or presentation have not been identified in the provided sources. The heterozygous CACNB4 variant in a SCAR10 patient with temporal lobe epilepsy suggests a potential genetic interaction influencing seizure susceptibility, but evidence is anecdotal and insufficient to classify CACNB4 as a formal modifier gene for SCAR10.[1][19] Other genes with co-occurring variants in Balreira’s exome analysis were considered but rejected because only ANO10 segregated with disease and was a known ataxia gene.[15] Thus, no established modifier loci exist for SCAR10, and the phenotypic variability is likely driven by variant-specific effects within ANO10, general genetic background, and environmental factors that remain poorly characterized.

Epigenetic mechanisms such as DNA methylation, histone modification, or chromatin changes altering ANO10 expression have not been studied in SCAR10 according to the provided data. OMIM, GeneReviews, and NCBI Gene do not mention epigenetic regulation as a contributor to SCAR10.[12][14][18] Structural genomic abnormalities, such as large deletions, duplications, translocations, or inversions involving ANO10 or chromosome 3p, are also not described. All reported ANO10 variants are single-nucleotide or small indel changes, not copy-number variants.[10][14][15][18] DECIPHER or dbVar entries linking structural variation to SCAR10 are not referenced in MedGen or OMIM.[3][5][10] For now, SCAR10 should be modeled as arising from sequence-level loss-of-function mutations in ANO10 without known structural genomic or epigenetic contributions.

## 5. Mechanism / Pathophysiology

### 5.1 Causal Chain from ANO10 Loss to Clinical Manifestation

In individuals with SCAR10, biallelic loss-of-function variants in the ANO10 gene lead to reduction or absence of functional anoctamin 10 protein in neurons and other ANO10-expressing cells.[10][14][18] This deficit in ANO10 impairs calcium-activated chloride channel activity and associated calcium-dependent signaling processes, particularly in cerebellar Purkinje cells and other neurons where ANO10 expression is high.[7][14][18] Disrupted calcium homeostasis in these neurons results in downstream alterations in synaptic function, cell cycle regulation, extracellular matrix remodeling, and immune homeostasis, as demonstrated by proteomic changes in ANO10-deficient SH-SY5Y neuronal cell lines.[7] These cellular perturbations, together with secondary mitochondrial dysfunction and CoQ10 deficiency observed in some patients, lead over time to progressive neuronal dysfunction and degeneration in cerebellar and frontal cortical circuits.[5][7][15] The cumulative tissue damage manifests clinically as slowly progressive cerebellar ataxia, pyramidal signs, oculomotor abnormalities, cognitive decline, peripheral neuropathy, epilepsy, and autonomic dysfunction, with marked cerebellar atrophy and frontal hypometabolism visible on MRI and FDG-PET imaging.[1][4][5][10][19]

This causal chain integrates upstream molecular events (ANO10 loss-of-function), mid-level cellular and metabolic consequences (calcium signaling disruption, synaptic and cell-cycle changes, CoQ10 deficiency), and downstream tissue and clinical outcomes (cerebellar and frontal neurodegeneration leading to ataxia and cognitive impairment). Some steps, especially the precise mechanisms linking ANO10 deficiency to CoQ10 depletion and immune/ECM alterations, are inferred from correlative data rather than fully demonstrated causal experiments and should be marked as hypotheses to be tested.

### 5.2 Molecular Pathways: Calcium Signaling, Synaptic Function, and CoQ10 Metabolism

At the molecular level, ANO10’s function as a putative calcium-activated chloride channel situates SCAR10 within calcium signaling and synaptic regulation pathways. OMIM notes that ANO10 belongs to the anoctamin family of calcium-activated chloride channels and that expression is highest in brain regions critical for motor coordination and cognition.[14] The recent proteomic profiling study by ANO10-deficient SH-SY5Y neuronal cell lines provides direct evidence that ANO10 loss perturbs calcium-linked pathways. The authors report that “comparative proteomic analysis revealed disruptions in synaptic function, cell cycle regulation, extracellular matrix remodelling, and immune homeostasis as candidate pathways potentially contributing to SCAR10 pathogenesis,” and emphasize that “all four processes are functionally linked to calcium signalling, aligning with previous reports implicating abnormal calcium homeostasis in spinocerebellar ataxias.”[7] These findings support the assignment of GO biological process terms such as “regulation of synaptic transmission” (GO:0050804), “cell cycle” (GO:0007049), “extracellular matrix organization” (GO:0030198), and “immune system process” (GO:0002376) to SCAR10 pathophysiology.

CoQ10 metabolism appears as a metabolic pathway linked to SCAR10. Balreira et al. discovered that their SCAR10 patients had skeletal muscle CoQ10 deficiency and concluded that “ANO10 defects cause secondary low CoQ10 and SCAR10 patients may benefit from CoQ10 supplementation.”[15][18] MedGen references Balreira’s observations and notes that “some patients have low levels of coenzyme Q10 (CoQ10) in muscle and may show some clinical improvement with CoQ10 treatment.”[5] This suggests that ANO10-mediated calcium or membrane transport may influence mitochondrial function or CoQ10 biosynthesis or turnover, although the mechanistic details remain unclear. Relevant GO terms include “ubiquinone biosynthetic process” (GO:0006744) and “mitochondrial electron transport, ubiquinol to cytochrome c” (GO:0006122), and chemical ontology mapping can use CHEBI “coenzyme Q10” (CHEBI:1709).

Given the evidence, SCAR10’s molecular pathophysiology can be summarized as loss of ANO10-mediated calcium-activated chloride transport leading to dysregulated intracellular calcium signaling, altered synaptic protein composition, disturbed cell cycle and ECM dynamics, perturbed immune-related pathways, and secondary mitochondrial CoQ10 deficiency. These molecular disturbances predispose neurons—especially Purkinje cells and frontal cortical neurons—to dysfunction and death under physiological and environmental stress.

### 5.3 Cellular Processes: Neuronal Dysfunction, Cell Cycle, ECM, and Immune Homeostasis

The proteomic study in ANO10-deficient SH-SY5Y cells offers the most detailed window into cellular processes affected by ANO10 loss.[7] Using CRISPR/Cas9 editing, the investigators generated a knockout line and three lines harboring recurrent SCAR10-associated pathogenic ANO10 variants, then performed mass spectrometry-based proteomics and bioinformatic analyses to identify differentially expressed proteins and pathways.[7] They found that ANO10 deficiency leads to disturbances in proteins associated with synaptic function, including those that modulate neurotransmitter release and receptor trafficking, suggesting altered synaptic vesicle dynamics and signal transduction at neuronal synapses. This aligns with the cerebellar ataxia phenotype, which is often driven by impaired Purkinje cell synaptic integration of afferent signals.

Cell cycle regulation emerged as another affected process. While mature neurons are post-mitotic, aberrant activation of cell cycle pathways in neurons is a known mechanism of neurodegeneration, leading to apoptotic or necrotic cell death when neurons attempt unscheduled cell-cycle re-entry.[7] ANO10-deficient cells displayed altered abundance of cell cycle-associated proteins, indicating dysregulated cell cycle control that may predispose neuronal precursor cells or glial cells to abnormal proliferation or death. GO terms like “regulation of cell cycle” (GO:0051726) and “neuronal apoptotic process” (GO:0051402) are appropriate.

Extracellular matrix remodeling is another category highlighted by the proteomic data. Changes in ECM components and remodeling enzymes can alter synaptic architecture, axon guidance, and neurovascular interactions.[7] Disrupted ECM could contribute to cerebellar circuit disorganization and eventually to neuronal degeneration, mapping to GO:0030198 “extracellular matrix organization” and related processes. Immune homeostasis perturbations, reflected by changes in immune-related proteins, suggest altered neuroimmune interactions—possibly microglial activation, cytokine signaling, or complement pathways—that can influence neurodegeneration and repair.[7] GO terms such as “immune response” (GO:0006955) and “microglial cell activation” (GO:0001774) may be relevant, though direct cell-type data are lacking in the provided study.

Taken together, these cellular processes—synaptic dysfunction, aberrant cell cycle regulation, ECM remodeling, and immune dysregulation—form mid-level steps between ANO10 molecular dysfunction and tissue-level neurodegeneration in SCAR10. While the proteomic data are in vitro and require validation in vivo, they provide plausible mechanistic links that can be captured in a knowledge base as experimental (cell-line) evidence.

### 5.4 Tissue Damage Mechanisms: Cerebellar and Frontal Neurodegeneration

At the tissue level, SCAR10 causes marked cerebellar atrophy, and increasingly recognized frontal lobe involvement, culminating in the clinical phenotype. OMIM and MedGen repeatedly emphasize “marked cerebellar atrophy on brain imaging” as a defining feature.[5][10] Vermeer et al. reported MRI evidence of “marked cerebellar atrophy” in all affected siblings.[10][14] Orphanet notes brain imaging “reveals marked cerebellar atrophy,” consistent with adult-onset autosomal recessive cerebellar ataxia.[9] The Japanese and other case reports confirm cerebellar volume loss, particularly affecting the vermis and hemispheres.[4][19]

The 2022 case series extends tissue-level understanding by reporting FDG-PET findings: both SCAR10 patients had “pronounced cerebellar atrophy on cerebral magnetic resonance imaging (MRI) and reduced metabolic activity in cerebellum as well as in the frontal lobes on 2-deoxy-2-(18F)fluoro-D-glucose positron emission tomography (FDG PET) scans,” indicating hypometabolism and likely neurodegeneration in frontal cortices.[1][19] These imaging data align with cognitive executive impairments observed clinically and further support the concept of cerebrocerebellar network involvement. Tissue damage mechanisms likely include chronic excitotoxicity, oxidative stress from mitochondrial dysfunction, and neuroinflammation, although these specific processes are not detailed in the provided sources.

HPO terms such as “Cerebellar atrophy” (HP:0001272) and “Cerebral cortical atrophy” (HP:0002059) can be used to represent structural changes, while imaging ontology terms (e.g., RadLex classes for “cerebellar volume loss” and “hypometabolic frontal cortex”) can capture radiologic phenotypes. The underlying biological processes include “neuronal death” (GO:0070997), “axonal degeneration” (GO:0032839), and “glial activation” (GO:0014002), though direct evidence in SCAR10 is inferred rather than empirically shown in the literature.

### 5.5 Biochemical Abnormalities: CoQ10 Deficiency and Mitochondrial Dysfunction

The key biochemical abnormality documented in SCAR10 is coenzyme Q10 deficiency in skeletal muscle biopsies of some patients. Balreira et al. report that in two adults with cerebellar ataxia, muscle CoQ10 levels were significantly reduced, and whole-exome sequencing revealed ANO10 mutations, leading them to conclude that “ANO10

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 3 |
| Unverifiable | 1 |
| Terms whose name was checked | 44 |
| Terms named correctly | 21 |
| Terms named as a **different** term | 11 |
| Terms whose name is worth a second look | 12 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0004311` (1 mention) - the report calls it "Coenzyme Q10 deficiency"; HP calls it **Abnormal macrophage morphology**
- `HP:0000646` (1 mention) - the report calls it "Downbeat nystagmus"; HP calls it **Amblyopia**
- `HP:0000519` (1 mention) - the report calls it "Saccadic eye movements"; HP calls it **Developmental cataract**
- `HP:0006887` (1 mention) - the report calls it "Executive dysfunction"; HP calls it **obsolete Intellectual disability, progressive**
- `HP:0006956` (1 mention) - the report calls it "Frontal lobe dysfunction"; HP calls it **Lateral ventricle dilatation**
- `HP:0001605` (1 mention) - the report calls it "Stridor"; HP calls it **Vocal cord paralysis**
- `HP:0000558` (1 mention) - the report calls it "Retinal degeneration"; HP calls it **Rieger anomaly**
- `HP:0001750` (1 mention) - the report calls it "Young adult onset"; HP calls it **Single ventricle**
- `CHEBI:1709` (1 mention) - the report calls it "coenzyme Q10"; CHEBI calls it **CHEBI_1709**
- `GO:0032839` (1 mention) - the report calls it "axonal degeneration"; GO calls it **dendrite cytoplasm**
- `GO:0014002` (1 mention) - the report calls it "glial activation"; GO calls it **astrocyte development**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0003408` (1 mention), reported as "Fasciculations" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0006887` (obsolete Intellectual disability, progressive) (1 mention) - replaced by `HP:0001249`
- `CHEBI:1709` (CHEBI_1709) (1 mention) - replaced by `CHEBI:15494`
- `GO:0070997` (obsolete neuron death) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0007033` (1 mention) - the report calls it "Cerebellar degeneration"; HP calls it **Cerebellar dysplasia**
- `HP:0000496` (1 mention) - the report calls it "Abnormal ocular motility"; HP calls it **Abnormality of eye movement**, and lists "Abnormal eye motility" among its other names
- `HP:0003202` (1 mention) - the report calls it "Muscle atrophy"; HP calls it **Skeletal muscle atrophy**, and lists "Muscle atrophy" among its other names
- `HP:0001250` (2 mentions) - the report calls it "Seizure", "Epilepsy"; HP calls it **Seizure**, and lists "Epilepsy" among its other names
- `HP:0003621` (1 mention) - the report calls it "Adolescent onset"; HP calls it **Juvenile onset**
- `HP:0003677` (1 mention) - the report calls it "Progressive"; HP calls it **Slowly progressive**
- `GO:0005227` (1 mention) - the report calls it "calcium-activated chloride channel activity"; GO calls it **calcium-activated cation channel activity**
- `GO:0007268` (1 mention) - the report calls it "synaptic transmission"; GO calls it **chemical synaptic transmission**, and lists "synaptic transmission" among its other names
- `GO:0050804` (1 mention) - the report calls it "regulation of synaptic transmission"; GO calls it **modulation of chemical synaptic transmission**, and lists "regulation of synaptic transmission" among its other names
- `GO:0051402` (1 mention) - the report calls it "neuronal apoptotic process"; GO calls it **neuron apoptotic process**
- `HP:0002059` (1 mention) - the report calls it "Cerebral cortical atrophy"; HP calls it **Cerebral atrophy**
- `GO:0070997` (1 mention) - the report calls it "neuronal death"; GO calls it **obsolete neuron death**, and lists "neuronal cell death" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001250` - called "Seizure", "Epilepsy"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.