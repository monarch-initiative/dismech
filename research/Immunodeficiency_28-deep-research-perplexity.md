---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-15T20:32:18.897638'
end_time: '2026-09-15T20:38:29.342508'
duration_seconds: 370.44
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 28
  mondo_id: MONDO:0013953
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
citation_count: 22
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 43
  verified: 39
  not_found: 1
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.024
  labels_checked: 37
  labels_matching: 22
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0002721
    reported_labels:
    - Recurrent mycobacterial infections
    ontology_label: Immunodeficiency
  - term_id: HP:0002715
    reported_labels:
    - Recurrent bacterial infections
    ontology_label: Abnormality of the immune system
  - term_id: HP:0031644
    reported_labels:
    - Recurrent salmonella infections
    ontology_label: Fusiform abdominal aortic aneurysm
  - term_id: HP:0001897
    reported_labels:
    - Abnormal chest radiograph
    ontology_label: Normocytic anemia
  - term_id: HP:0012430
    reported_labels:
    - Elevated circulating interferon-gamma level
    ontology_label: Cerebral white matter hypoplasia
  - term_id: HP:0032150
    reported_labels:
    - Abnormal response to interferon-gamma
    ontology_label: Paroxysmal rectal pain
  - term_id: CL:0000913
    reported_labels:
    - T helper 1 cell
    ontology_label: effector memory CD8-positive, alpha-beta T cell
  - term_id: GO:0005887
    reported_labels:
    - integral component of plasma membrane
    ontology_label: GO_0005887
  labels_variant: 7
  unresolved_terms:
  - HP:0005385
  obsolete_terms:
  - term_id: GO:0005887
    ontology_label: GO_0005887
    replaced_by: GO:0005886
  unresolvable_prefixes:
  - OMIM
  - Orphanet
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 28
- **MONDO ID:** MONDO:0013953 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 28** covering all of the
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

# Immunodeficiency 28 (IFNGR2 Deficiency / MONDO:0013953): Comprehensive Disease Characteristics

Immunodeficiency 28 (IMD28), also known as interferon-gamma receptor 2 (IFNGR2) deficiency, is a very rare, predominantly pediatric primary immunodeficiency belonging to the spectrum of Mendelian susceptibility to mycobacterial disease (MSMD), defined by a selective predisposition to severe infections with Bacille Calmette–Guérin (BCG) vaccine strains, environmental non-tuberculous mycobacteria, and sometimes *Mycobacterium tuberculosis*, in otherwise immunocompetent individuals.[1][2][9][11] Clinically, complete autosomal recessive IFNGR2 deficiency causes early-onset, often disseminated and life-threatening mycobacterial disease, typically before three years of age, with high plasma interferon-γ (IFN-γ) levels and an undetectable cellular response to IFN-γ, whereas partial deficiencies (autosomal recessive or dominant) permit residual signaling and are associated with later-onset, recurrent but sometimes curable infections and more circumscribed granulomatous lesions.[2][11][13][15][18] At the molecular level, pathogenic variants in IFNGR2 on chromosome 21q22.11 disrupt the signal-transducing chain of the IFN-γ receptor complex, preventing appropriate activation of STAT1-dependent macrophage effector responses that are essential for the control of mycobacteria and certain intracellular pathogens.[10][11][16][18] Fewer than a few dozen patients have been reported worldwide—Orphanet notes “only ten children” with complete IFN-γR2 deficiency—mostly from consanguineous families in regions where BCG vaccination is universal and environmental mycobacteria are prevalent, illustrating both strong genetic determinism and critical gene–environment interactions.[11][14][15][18] Diagnosis relies on a combination of clinical suspicion, functional immunologic assays showing absent or reduced IFN-γ responsiveness, flow cytometric evaluation of IFN-γ receptor expression, and confirmatory IFNGR2 sequencing, while management centers on aggressive antimycobacterial chemotherapy, stringent avoidance of live BCG vaccination, and hematopoietic stem cell transplantation (HSCT) as the only established curative option for complete deficiency.[10][12][15][19] Despite its rarity, Immunodeficiency 28 has provided fundamental insights into human IFN-γ biology, revealing that quantitative and qualitative variation in IFN-γ signaling—spanning complete receptor loss-of-function, partial receptor defects, and even cytokine deficiency—directly shapes the spectrum of mycobacterial disease and informs precision immunotherapy strategies.[11][13][16][17][18]

## 1. Disease Information

### 1.1 Definition and Clinical Overview

Immunodeficiency 28 (IMD28) is defined in Online Mendelian Inheritance in Man (OMIM) as “Immunodeficiency 28, mycobacteriosis,” caused by homozygous or compound heterozygous mutations in the IFNGR2 gene encoding the interferon-gamma receptor 2 chain on chromosome 21q22.11.[1][18] It belongs to the broader category of Mendelian susceptibility to mycobacterial disease (MSMD), a group of inborn errors of IFN-γ–mediated immunity characterized by selective vulnerability to mycobacteria and a limited set of other pathogens, especially *Salmonella*.[11][13][20] The clinical hallmark of IMD28 is severe and often disseminated disease due to moderately virulent mycobacterial species such as BCG vaccine strains and environmental non-tuberculous mycobacteria (NTM), frequently accompanied by failure to control infection despite appropriate antimicrobial therapy.[1][2][9][10] Patients with complete autosomal recessive IFNGR2 deficiency typically present in infancy or early childhood with lymphadenopathy, hepatosplenomegaly, bone lesions, pulmonary involvement, and systemic symptoms after BCG vaccination or environmental mycobacterial exposure, and most succumb to complications within the first decade of life in the absence of HSCT.[11][14][15][19] Partial IFNGR2 deficiency, whether recessive or dominant, is associated with a milder but still serious phenotype of recurrent or chronic mycobacterial infections, sometimes localized (for example multifocal osteomyelitis) and compatible with survival into adolescence or adulthood, especially when promptly treated.[2][11][13][18]

From a conceptual standpoint, IMD28 is a prototypical monogenic immunodeficiency where the primary defect lies in a specific cytokine receptor pathway rather than generalized lymphocyte development or function; affected individuals may have normal lymphocyte counts, immunoglobulin levels, and vaccine responses to non-live antigens, yet are profoundly unable to mount protective IFN-γ–dependent macrophage activation against mycobacteria.[10][11][13] This selective immunologic vulnerability distinguishes IMD28 from broader combined immunodeficiencies and underscores the importance of considering MSMD in any child with severe BCG or NTM disease in the setting of otherwise unremarkable routine immunologic work-up.[11][13][15] The disease has also been subdivided—in Orphanet and MSMD reviews—into “MSMD due to complete IFN-γR2 deficiency” and “MSMD due to partial IFN-γR2 deficiency,” which are clinically overlapping but differ in molecular mechanisms and residual signaling capacity.[11][13][15][18]

### 1.2 Identifiers, Synonyms, and Ontology Mapping

Several authoritative resources assign distinct identifiers to Immunodeficiency 28 and its IFNGR2-related MSMD variants. OMIM lists IMD28 under MIM number 614889, with IFNGR2 itself under MIM 147569 and maps the phenotype to cytogenetic location 21q22.11.[1][6][8][18] Orphanet catalogs “Mendelian susceptibility to mycobacterial diseases due to complete interferon gamma receptor 2 deficiency” as Orphanet ID 319547 and “MSMD due to partial IFN-gammaR2 deficiency” as a related entry, both with autosomal recessive inheritance and very low prevalence.[9][15] The MONDO disease ontology references Immunodeficiency 28 as MONDO:0013953, explicitly linking it to IFNGR2 deficiency and susceptibility to mycobacterial infections.[5][7] In ClinVar, IFNGR2 deficiency is associated with the condition name “Immunodeficiency 28 (IMD28)” and cross-referenced to OMIM:614889, Orphanet:319547/319574, MedGen C4013947, and MONDO:0013953.[5]

Common synonyms and alternative names include “IFNGR2 deficiency,” “IFN-gamma receptor 2 deficiency,” “Mendelian susceptibility to mycobacterial diseases due to complete interferon gamma receptor 2 deficiency,” “MSMD due to partial IFN-gammaR2 deficiency,” and “Immunodeficiency 28, mycobacteriosis.”[1][2][9][11][15][18] Clinically, the condition is frequently described simply as “IFN-γR2 deficiency” within the MSMD literature, which recognizes IFNGR2 among a panel of at least 11 genes (including IL12B, IL12RB1, STAT1, IFNGR1, and others) whose inborn defects confer susceptibility to mycobacteria.[11][13][20] Under ICD-10, there is no specific code uniquely assigned to IMD28; affected patients are generally coded under broader immunodeficiency categories such as D84.8 (“Other specified immunodeficiencies”) or D89.8 (“Other specified disorders involving the immune mechanism”), and under ICD-11 they fall in the group of “primary immunodeficiencies predominantly affecting cellular and humoral immunity.” These generic codes reflect the rarity and sub-specialist nature of the diagnosis rather than a lack of clinical significance.

Because IMD28 is a well-defined monogenic entity, most information is derived from aggregated disease-level resources that synthesize case reports and series rather than from large electronic health record (EHR) datasets. OMIM, Orphanet, MalaCards, and authoritative reviews in *Human Molecular Genetics*, *Journal of Clinical Investigation*, and *Frontiers in Immunology* collate phenotypic and mechanistic data from approximately 30–40 reported patients, including at least ten with complete IFN-γR2 deficiency and additional individuals with partial deficiencies.[11][13][14][15][18][20] Individual EHR-based epidemiologic analyses are essentially nonexistent due to the extreme rarity of the condition; instead, knowledge is driven by detailed clinical immunology work-ups, family-based genetic studies, and mechanistic experiments in patient-derived cells.

### 1.3 Relationship to Mendelian Susceptibility to Mycobacterial Disease

MSMD is an umbrella clinical and genetic concept that encompasses a heterogeneous group of rare inborn errors of immunity conferring “selective susceptibility to weakly virulent mycobacteria, including Bacille Calmette–Guérin (BCG) vaccine substrains and various environmental mycobacteria, in otherwise healthy patients.”[11][13][20] IFNGR2 deficiency is one of the core MSMD-causing defects, alongside IFNGR1 deficiency, IL-12 p40 and IL-12 receptor β1 deficiencies, STAT1 defects, and several other conditions affecting IFN-γ production or signaling.[11][13][20] Within this framework, IMD28 corresponds to those MSMD cases in which the proximal lesion resides in the signal-transducing chain of the IFN-γ receptor complex, IFNGR2, rather than in ligand production (IFNG) or the ligand-binding chain IFNGR1.[11][17][18]

The MSMD literature emphasizes that IFNGR2 deficiency exists in multiple forms. Complete autosomal recessive deficiency is defined functionally by an undetectable cellular response to IFN-γ, in terms of STAT1 phosphorylation, gene induction, and microbicidal activity, and is almost always lethal in childhood without HSCT.[11][13][15][20] Partial deficiencies, whether autosomal recessive due to hypomorphic alleles or autosomal dominant due to haploinsufficiency, produce a continuum of reduced IFN-γ signaling with variable penetrance for mycobacterial disease, thereby illustrating that human IFN-γ responsiveness is a quantitative trait.[11][13][17][18] The MSMD classification and its mechanistic dissection have been instrumental in demonstrating that IFN-γ functions physiologically not as a general antiviral cytokine, as initially described, but as the key macrophage-activating factor required for host defense against mycobacteria and related intracellular pathogens.[11][13]

## 2. Etiology

### 2.1 Primary Causal Factors: Genetic and Mechanistic

The primary cause of Immunodeficiency 28 is germline mutation in IFNGR2, the gene encoding the signal-transducing β chain of the human interferon-gamma receptor complex.[1][18] IFNGR2 is located on chromosome 21q22.11 and encodes a type I membrane protein that associates with IFNGR1 to form the functional receptor for IFN-γ at the cell surface of macrophages, monocytes, dendritic cells, and other immune cells.[1][10][16][18] Pathogenic IFNGR2 variants—mostly biallelic in the case of complete deficiency—disrupt receptor expression, folding, trafficking, glycosylation, or intracellular signaling motifs, thereby abrogating or attenuating IFN-γ–induced STAT1 activation and downstream antimicrobial programs.[11][14][16][18][20] OMIM and Orphanet categorize IMD28 and related MSMD forms as Mendelian monogenic disorders with autosomal recessive inheritance for complete and partial forms and autosomal dominant inheritance for some partial forms due to haploinsufficiency.[1][11][15][18]

Several mechanistic classes of IFNGR2 mutations have been defined. The earliest reported case of IFNGR2 deficiency involved a mutation in the extracellular domain that prevented cell surface expression of the receptor, leading to absent IFN-γ signaling and disseminated mycobacterial disease in childhood.[18][20] Vogt and colleagues later described a missense mutation, T168N, that creates a novel N-linked glycosylation site in IFNGR2; the attached carbohydrate moiety sterically prevents recruitment of IFNGR2 into the IFN-γ receptor signaling complex despite preserved IFNGR1 engagement, thus abolishing cellular responses to IFN-γ while leaving the receptor present at the surface.[16][18] More recent work has identified splice site mutations, such as c.207-1G>A, causing an in-frame deletion of three amino acids in the extracellular fibronectin type 3 domain, which destabilizes the receptor or impairs signaling and presents clinically with recurrent infections and familial BCG-related deaths.[14] Additional hypomorphic mutations affecting translation initiation codons or early coding sequence have been shown to confer partial AR deficiency with residual but reduced IFN-γ responsiveness and milder MSMD phenotypes.[13][17]

Mechanistically, the disease reflects loss of function of IFNGR2. Both complete and partial deficiencies are characterized by impaired or absent STAT1 phosphorylation upon IFN-γ stimulation, defective upregulation of IFN-γ–inducible genes such as CXCL10, GBP family members, and IRF1, and insufficient activation of macrophage microbicidal effector functions including reactive nitrogen and oxygen species production.[10][11][13][20] The result is a failure to contain mycobacterial replication within granulomas, leading to uncontrolled bacterial proliferation and tissue destruction despite otherwise intact lymphocyte development and immunoglobulin production. In partial dominant forms, the mechanism is haploinsufficiency rather than dominant-negative interference, contrasting with AD IFNGR1 deficiency, which involves truncated receptor tails that prevent recycling and signaling.[11][17][18]

### 2.2 Genetic Risk Factors and Susceptibility Modifiers

Beyond the primary IFNGR2 mutations that directly cause Immunodeficiency 28, other genetic factors can modulate susceptibility to mycobacterial disease in patients or heterozygous carriers. The MSMD spectrum includes multiple genes whose defects can mimic or compound the clinical phenotype, including IFNGR1, STAT1, IL12B, IL12RB1, ISG15, TYK2, IRF8, SPPL2A, NEMO, and CYBB.[11][13][20] These genes collectively define the IL-12/IFN-γ axis, and their polymorphisms may influence the severity or breadth of infection in IFNGR2-deficient individuals. For example, hypomorphic alleles in IL12RB1 or STAT1 could theoretically exacerbate an already compromised IFN-γ signaling environment, although specific data on genetic modifiers in IMD28 are limited.

Autosomal dominant partial IFNGR2 deficiency, acting by haploinsufficiency, represents a form of quantitative genetic risk factor: heterozygous carriers of particular IFNGR2 mutations have reduced IFN-γ responsiveness and increased—but incompletely penetrant—risk for MSMD.[11][17][18] Casanova and colleagues have emphasized that IFN-γ–related traits in humans, including cytokine production, receptor expression, and signaling capacity, are quantitative and polygenic; however, the strongest effects in MSMD are due to rare, high-impact variants rather than common susceptibility polymorphisms.[11][17] Population databases such as gnomAD document numerous IFNGR2 variants at low frequency, most of which are benign or of uncertain significance; nonetheless, the presence of rare, predicted loss-of-function alleles in apparently healthy individuals highlights the possibility of low penetrance or incomplete ascertainment.[5][18]

ClinVar records specific IFNGR2 variants, such as NM_005534.4: c.879+32dup (rs143248516), which has been submitted as benign for Immunodeficiency 28, underscoring the necessity of careful pathogenicity assessment according to ACMG/AMP guidelines.[5] The benign classification suggests that some intronic or synonymous changes that alter reference sequences are tolerated in humans without causing IFN-γR2 deficiency, and that not all IFNGR2 sequence variation translates into disease risk. At present, there is no evidence for common GWAS-identified susceptibility loci for IMD28, reflecting both its rarity and its strongly Mendelian etiology.

### 2.3 Environmental and Infectious Risk Factors

Environmental exposures play a decisive role in determining clinical expression of IFNGR2 deficiency. The most critical environmental factor is exposure to mycobacteria, especially BCG vaccine strains and environmental NTM. In regions where BCG vaccination is routinely administered in the neonatal period, infants with complete IFN-γR2 deficiency invariably develop disseminated BCG disease, often leading to early death.[9][10][11][14][15] Orphanet notes that “severe and often fatal BCG and environmental mycobacteria infections begin in early childhood (before the age of 3)” in complete IFN-γR2 deficiency, reflecting the rapid unmasking of the genetic defect by vaccine exposure.[15] In countries without BCG vaccination or with delayed schedules, initial presentations may instead involve environmental mycobacteria or *M. tuberculosis*, and age of onset may be slightly later.

The IL-12/IFN-γ pathway is also essential for control of *Salmonella* infections, and MSMD patients—including some with IFNGR2 deficiency—have been reported to suffer severe or recurrent salmonellosis.[10][11][20] Geographic regions with high NTM and *Salmonella* exposure, coupled with widespread BCG vaccination and a background of consanguinity, are therefore epidemiologic “hotspots” for the manifestation of IFNGR2 defects, as seen in reported cases from Saudi Arabia, Iran, Turkey, India, and Lebanon.[14][17][18][20] Other environmental factors such as malnutrition, co-infections with HIV, and exposure to immunosuppressive medications could, in principle, aggravate disease, but detailed data specific to IMD28 are lacking.

### 2.4 Protective Factors and Gene–Environment Interactions

Specific protective genetic factors for Immunodeficiency 28 have not been clearly defined. The majority of reported cases involve high-impact loss-of-function IFNGR2 mutations that confer near-obligate risk for severe MSMD when combined with typical environmental exposure to mycobacteria.[11][13][15][18][20] In theory, genetic variants that enhance IFN-γ–independent mycobacterial control pathways—for example, polymorphisms increasing TNF-α production, autophagy efficiency, or alternative macrophage activation routes—could mitigate disease severity, but such modifiers have not yet been systematically identified in IMD28. Likewise, there is no evidence that common protective alleles in IFNG or IFNGR1 alter penetrance of IFNGR2 defects, though polygenic background likely contributes to inter-individual variability.

Environmental protective factors are better defined pragmatically. Avoidance of live BCG vaccination in neonates known to carry IFNGR2 mutations, or in families with previously affected children, effectively prevents the most severe early-onset disease manifestation.[10][15] Rigorous infection control practices to reduce exposure to environmental mycobacteria, including water and soil sources, might also be beneficial, although this is difficult to implement comprehensively. Early recognition and treatment of localized infections can prevent dissemination and reduce mortality, representing a form of secondary environmental protection. High-quality nutrition and absence of secondary immunosuppressive conditions may support residual host defenses—but these factors are general to many infections and not specific to IFNGR2 deficiency.

Gene–environment interactions in IMD28 are striking and instructive. Bi-allelic IFNGR2 loss-of-function is necessary but not sufficient for disease; its clinical impact depends crucially on exposure to mycobacteria and perhaps to particular environmental strains. Casanova and colleagues have argued, based on MSMD cohorts, that the phenotype of IFN-γ pathway defects is shaped by both genotype and pathogen virulence, with weakly virulent mycobacteria disproportionately revealing inborn errors of IFN-γ immunity that might otherwise remain clinically silent.[11][17][20] This interaction explains why some heterozygous carriers of partial IFNGR2 mutations remain asymptomatic in low-exposure settings, whereas others develop MSMD when confronted with high pathogen burdens. The case reports of families in which multiple siblings succumbed to BCG disease after vaccination while others, including heterozygous parents, remained healthy vividly illustrate this interplay between a Mendelian lesion and a specific environmental trigger.[14][15][18]

## 3. Phenotypes

### 3.1 Core Clinical Phenotypes: Mycobacterial and Salmonella Infections

The central phenotype of Immunodeficiency 28 is increased susceptibility to mycobacterial infections, particularly those caused by BCG vaccine strains and environmental non-tuberculous mycobacteria. OMIM, MalaCards, Mendelian.co, and Orphanet all emphasize this defining characteristic. MalaCards describes IMD28 as “a primary immunodeficiency disease characterized by increased susceptibility to mycobacterial disease, high levels of IFNG in the plasma, and absence of cellular response to IFNG.”[2] Similarly, Mendelian.co summarily notes that “IMD28 is caused by autosomal recessive IFNGR2 deficiency… characterized by severe and often fatal infections with BCG and other environmental mycobacteria,” and lists “recurrent mycobacterial infections” as a key phenotype.[9] Orphanet reports that complete IFN-γR2 deficiency causes “severe and often fatal BCG and EM infections” beginning in early childhood.[15]

Clinically, these infections manifest as persistent or progressive local disease at the site of BCG inoculation (for example ulceration or abscess) followed by regional lymphadenitis, systemic dissemination with hepatosplenomegaly, bone and joint involvement, pulmonary lesions, and constitutional symptoms such as fever and weight loss.[14][15][18][20] Environmental mycobacteria such as *Mycobacterium avium*, *M. fortuitum*, *M. abscessus*, and *M. chelonae* feature prominently in case descriptions.[1][2][9][14][18][20] Dorman and Holland’s original 1998 report of an IFNGR2 mutation described a child with disseminated *M. fortuitum* and *M. avium* complex infections associated with absent IFN-γ signaling.[18][20] Later, Vogt et al. documented three children with MSMD who were homozygous for the T168N IFNGR2 mutation and suffered severe mycobacterial disease.[18]

Salmonella infections are also noted as part of the MSMD phenotype, reflecting the shared dependence on IL-12/IFN-γ pathway for host defense. The immunodeficiencysearch.com resource summarizing IFN-γ pathway defects states that patients with autosomal recessive complete IFN-γ receptor deficiency often experience severe salmonella infections in addition to mycobacterial disease.[10] Although specific salmonella phenotypes in IFNGR2-deficient patients are less frequently detailed in the literature than mycobacterial infections, severe or recurrent non-typhoidal salmonellosis should be considered part of the syndrome and influences differential diagnosis and management.

In Human Phenotype Ontology (HPO) terms, these core phenotypes can be mapped as follows: “Recurrent mycobacterial infections” (HP:0002721), “Bacille Calmette–Guérin infection” (HP:0005381), “Disseminated Bacille Calmette–Guérin infection” (HP:0005385), “Recurrent bacterial infections” (HP:0002715), and “Recurrent salmonella infections” (HP:0031644). These infection-related phenotypes are generally severe and progressive in complete IFN-γR2 deficiency, appearing in infancy or early childhood, while in partial deficiency they may be moderately severe or episodic, with onset in later childhood or adolescence.[11][13][15][18]

### 3.2 Age of Onset, Severity, and Progression

Age of symptom onset is consistently reported as neonatal or early childhood for complete IFNGR2 deficiency. Orphanet states that “severe and often fatal BCG and environmental mycobacteria infections begin in early childhood (before the age of 3)” in complete IFN-γR2 deficiency.[15] The first reported IFNGR2-deficient patient presented with persistent cough and subsequently developed lymphadenopathy, hepatosplenomegaly, and fevers in childhood.[14][18] In the Frontiers in Immunology case series, two surviving siblings with a novel splice site mutation presented in infancy with recurrent infections and had a history of two other siblings who died shortly after BCG vaccination.[14] These observations support mapping IMD28 onset under HPO term “Onset in early childhood” (HP:0003623), with some cases meeting “Infantile onset” (HP:0003593) or “Neonatal onset” (HP:0003623) depending on timing of vaccination and exposure.

Symptom severity is typically severe in complete deficiency, with high risk of disseminated disease and death. Orphanet notes that prognosis is poor, with “most patients not living past 10 years of age” without HSCT.[15] MSMD reviews emphasize that complete IFN-γR1 and IFN-γR2 deficiencies “are always lethal before the third decade of life in the absence of hematopoietic stem cell transplantation.”[11][20] Partial deficiencies exhibit a broader severity spectrum: recessive hypomorphic mutations can cause moderately severe recurrent infections that are often localized and potentially curable, whereas dominant haploinsufficient forms may have very low penetrance and present with single episodes of BCG disease or NTM osteomyelitis.[11][13][17][18]

Symptom progression in complete IFNGR2 deficiency tends to be progressive and relentless in the absence of adequate therapy. Initial local or regional disease frequently evolves into disseminated multi-organ involvement, with episodes of apparent control followed by relapse, reflecting partial suppression by antimycobacterial drugs but fundamental inability to sterilize infection.[14][15][19] In some partial deficiencies, progression may be more episodic, with recurrent flares of disease triggered by new exposures and intervals of remission. Overall disease course can be classified as chronic lifelong, requiring ongoing vigilance, even though individual infection episodes may be brought under control.

### 3.3 Additional Clinical Signs and Laboratory Abnormalities

Beyond infections, IMD28 patients often display clinical signs related to granulomatous inflammation and organ involvement. Hepatomegaly, splenomegaly, generalized lymphadenopathy, bone pain and deformities due to osteomyelitis, and pulmonary infiltrates are commonly described.[14][15][18][20] These features correspond to HPO terms such as “Hepatosplenomegaly” (HP:0001433), “Lymphadenopathy” (HP:0002716), “Osteomyelitis” (HP:0002754), and “Abnormal chest radiograph” (HP:0001897). The granulomatous lesions in IFNGR2 deficiency may differ from those in intact IFN-γ immunity, particularly in complete deficiency, where patients fail to form well-circumscribed granulomas and instead show poorly organized, necrotic inflammatory lesions.[10][11][20]

A distinctive laboratory abnormality in IFN-γ receptor deficiencies, including IFNGR2, is markedly elevated plasma IFN-γ levels coupled with absent cellular responsiveness. MalaCards notes that IMD28 is “associated with high plasma IFNG levels and absence of cellular response to IFNG.”[2] MSMD reviews corroborate that patients with complete IFN-γR1 or IFN-γR2 deficiency exhibit high circulating IFN-γ concentrations, reflecting unchecked production by T cells and NK cells in response to persistent antigenic stimulation and lack of negative feedback mediated by receptor signaling.[11][13][20] Functionally, leukocytes and fibroblasts from complete IFN-γR2 deficient patients do not respond to IFN-γ in vitro, as measured by STAT1 phosphorylation and target gene induction.[10][15][20] These findings can be mapped to HPO terms such as “Elevated circulating interferon-gamma level” (HP:0012430) and “Abnormal response to interferon-gamma” (HP:0032150).

Routine hematology may be relatively unremarkable, aside from anemia of chronic disease or leukocytosis during infection. Immunoglobulin levels are frequently normal, and responses to non-live vaccines can be preserved, underscoring the specificity of the defect.[11][13][20] Thus, IMD28 presents a paradoxical profile: severe infections with particular pathogens despite apparently normal general immune parameters. This phenotype challenges diagnostic heuristics based solely on standard immunologic screening.

### 3.4 Quality of Life Impact

The quality of life impact of Immunodeficiency 28 is profound, particularly in complete deficiency. Children with disseminated BCG or NTM disease experience chronic fevers, malaise, pain from bone and joint involvement, respiratory distress from pulmonary infiltrates, and functional limitations due to organomegaly and skeletal lesions.[14][15][19] Frequent hospitalizations, prolonged courses of multidrug antimycobacterial therapy, invasive diagnostics, and the psychosocial burden of a life-threatening condition in early childhood all impair daily functioning and psychosocial well-being. Parents and caregivers face immense stress, particularly in families with multiple affected children due to consanguinity and autosomal recessive inheritance.

While formal quality-of-life studies using instruments such as EQ-5D or SF-36 have not been reported specifically for IMD28, extrapolation from other severe pediatric primary immunodeficiencies suggests major deficits across physical, emotional, and social domains. HSCT, when successful, can dramatically improve survival and long-term health, but entails its own acute morbidity, including graft-versus-host disease, infections, and prolonged immunosuppression.[12][19] Life course trajectories for survivors of partial IFNGR2 deficiency are somewhat better, with possible return to near-normal functioning, yet the risk of recurrent infections and need for lifelong medical surveillance remain.

### 3.5 Suggested HPO Terms

Based on the clinical profile described above, key HPO terms for Immunodeficiency 28 include: “Recurrent mycobacterial infections” (HP:0002721), “Bacille Calmette–Guérin infection” (HP:0005381), “Disseminated Bacille Calmette–Guérin infection” (HP:0005385), “Recurrent bacterial infections” (HP:0002715), “Recurrent salmonella infections” (HP:0031644), “Hepatosplenomegaly” (HP:0001433), “Lymphadenopathy” (HP:0002716), “Osteomyelitis” (HP:0002754), “Elevated circulating interferon-gamma level” (HP:0012430), “Abnormal response to interferon-gamma” (HP:0032150), “Infantile onset” (HP:0003593), and “Early childhood onset” (HP:0003623). These terms can be annotated with qualitative frequencies: core infection phenotypes occurring in the majority of complete deficiency cases, while some manifestations such as multifocal osteomyelitis or severe salmonellosis may be present in a subset.[11][13][15][18][20]

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: IFNGR2

The causal gene for Immunodeficiency 28 is IFNGR2 (interferon-gamma receptor 2), located on chromosome 21q22.11 and designated OMIM number 147569.[1][6][8][18] IFNGR2 encodes the β or signal-transducing chain of the heterodimeric IFN-γ receptor, which associates with the α chain IFNGR1 to form the functional receptor complex at the surface of responsive cells.[16][18] Upon IFN-γ binding to IFNGR1, IFNGR2 is recruited to the ligand-bound complex, enabling the juxtaposition of intracellular Janus kinases JAK1 and JAK2 and subsequent phosphorylation of STAT1 on tyrosine 701, a critical step in the transcriptional activation of IFN-γ–responsive genes.[11][16][18][20]

The IFNGR2 protein comprises an extracellular fibronectin type 3 (FN3) domain responsible for co-receptor interactions, a single transmembrane segment, and a cytoplasmic tail containing motifs necessary for JAK2 binding and downstream signaling.[16][18] Genetic defects in IFNGR2 can therefore affect receptor structure and function at multiple levels: extracellular domain mutations may impair ligand-induced assembly or stability; transmembrane or trafficking mutations may prevent cell surface expression; and cytoplasmic tail mutations may abrogate JAK2 recruitment or STAT1 activation.[11][16][18][20] In IMD28, characterized by IFNGR2 deficiency, these mechanistic disruptions result in either complete loss or marked reduction of IFN-γ signaling in immune cells.

### 4.2 Pathogenic Variant Classes and Functional Consequences

The repertoire of pathogenic IFNGR2 variants underlying Immunodeficiency 28 includes missense mutations, nonsense mutations, splice site variants, small insertions/deletions, and, in some cases, larger structural alterations. The OMIM entry for IFNGR2 catalogues specific disease-associated alleles, including the T168N missense mutation and the extracellular domain mutation originally described by Dorman and Holland.[18][20] Vogt et al. identified three children with MSMD who were homozygous for a 503C→A transversion leading to the T168N substitution; this mutation creates a new N-glycosylation site in the FN3 domain, resulting in a neoglycan whose steric bulk prevents IFNGR2 from docking to the high-affinity IFN-γ–IFNGR1 intermediate complex.[16][18] Structural studies by Mendoza and colleagues, who determined the crystal structure of the IFN-γ–IFNGR1–IFNGR2 signaling complex, confirmed that T168 lies precisely at the interface required for IFNGR2 recruitment, and that glycosylation at this site sterically blocks assembly of the full hexameric signaling complex.[16][18]

The Frontiers in Immunology report by Desai et al. describes a novel splice acceptor site variant c.207-1G>A in intron 2 of IFNGR2, identified in two affected siblings with recurrent infections and a family history of BCG-related deaths.[14] This mutation leads to deletion of three amino acids (Thr70–Ser72) in the FN3 domain of IFNGR2, located in the extracellular region within Tissue_fac and FN3 domains important for receptor function.[14] Functional characterization suggested that this deletion destabilizes receptor expression or impairs ligand-induced signaling, contributing to partial or complete deficiency. The authors note that more than 27 patients had been reported with IFNGR2-related MSMD by that time, encompassing diverse etiologies such as abolished or maintained expression of IFNGR2, complete or partial deficiency with or without cell surface expression, expression of non-functional IFNGR2 on the cell surface, and creation of new glycosylation sites that cause misfolding or steric hindrance.[14]

Human Molecular Genetics and JCI reviews of MSMD further classify IFNGR2 defects according to inheritance (AR or AD), degree of deficiency (complete or partial), and presence or absence of receptor expression. One table lists IFNGR2 variants as AR complete with extracellular expression positive (E+) or negative (E−), AR partial with expression of mutant or wild-type protein, and AD partial with preserved surface expression.[11][13][17][20] Complete AR IFNGR2 deficiency encompasses both “non-expressive” forms, where receptor is absent from the cell surface due to trafficking or folding defects, and “expressive” forms, where receptor is present but non-functional due to altered glycosylation or signaling motifs.[11][13][18][20] Partial AR forms generally involve hypomorphic mutations that reduce but do not abolish receptor expression or function, whereas AD forms act via haploinsufficiency and often show low penetrance.[11][17][18]

Functionally, most disease-causing IFNGR2 mutations are loss-of-function, resulting in absent or severely impaired IFN-γ signaling. The T168N neoglycosylation mutation is a gain-of-glycosylation variant, but its net effect is a loss of signaling due to steric blocking of receptor recruitment.[16][18] Splice site and truncating mutations usually produce non-functional proteins or lead to nonsense-mediated decay. There is no evidence for dominant-negative IFNGR2 mutations analogous to the truncated tail variants seen in AD IFNGR1 deficiency; instead, AD IFNGR2 deficiency operates by reduced gene dosage and haploinsufficiency.[11][17][18] Thus, in ACMG/AMP terms, pathogenic IFNGR2 variants in IMD28 are overwhelmingly classified as pathogenic or likely pathogenic loss-of-function alleles, with rare hypomorphic variants classified as pathogenic partial loss-of-function. ClinVar submissions and gnomAD frequencies help distinguish pathogenic from benign variants, as in the case of c.879+32dup (rs143248516), which is benign and relatively more frequent.[5]

### 4.3 Allele Frequencies, Population Data, and Somatic vs Germline Origin

Due to the extreme rarity of Immunodeficiency 28, most pathogenic IFNGR2 variants are absent or occur at extremely low frequencies in population databases such as gnomAD, 1000 Genomes, and ExAC. Many reported mutations arise in consanguineous families, implying local founder effects, but the small number of cases precludes robust carrier frequency estimation.[14][15][18][20] Orphanet estimates prevalence of complete IFN-γR2 deficiency as less than 1 per 1,000,000, and notes that “only ten children have been identified to date,” suggesting that even carriers are scarce in the general population or remain undiagnosed.[15]

All disease-causing IFNGR2 variants in IMD28 are germline; there is no evidence for somatic IFNGR2 mutations causing acquired immunodeficiency in humans. Somatic mutations in IFN-γ signaling components can occur in cancers and may influence tumor immune evasion, but those are distinct from the inherited immunodeficiency described here and are catalogued in oncology datasets rather than MSMD literature. The condition is thus a purely germline, congenital disorder, and genetic counseling focuses on autosomal recessive and, in some partial forms, autosomal dominant inheritance.

### 4.4 Modifier Genes and Epigenetic Information

Specific modifier genes that alter the severity or expression of IFNGR2 deficiency have not been systematically identified. Nonetheless, the broader MSMD field has revealed that defects in IL-12, STAT1, and other IFN-γ pathway components can independently cause mycobacterial disease, indicating that the interplay of multiple pathways may modulate phenotype.[11][13][20] Patients with combined defects (for example, IFNGR2 mutation plus another immunologic lesion) would be expected to have particularly severe disease, although such compound cases have not yet been reported.

Epigenetic alterations in IFNGR2 or in IFN-γ pathway genes have not been implicated in IMD28. Regulation of IFNGR2 expression and chromatin state under inflammatory conditions is an active area of basic immunology research, but no disease-causing epigenetic lesions have been described. Given the monogenic nature and early onset of the condition, genetic defects are sufficient to explain the phenotype without invoking epigenetic dysregulation.

### 4.5 Chromosomal Abnormalities

No large-scale chromosomal abnormalities such as aneuploidies, translocations, or inversions have been associated specifically with Immunodeficiency 28. The IFNGR2 locus resides within the distal long arm of chromosome 21, but its position is distinct from regions implicated in Down syndrome phenotypes. There is no evidence that trisomy 21 per se alters IFNGR2 function in a way that mimics IMD28. Likewise, no recurrent microdeletions or microduplications encompassing IFNGR2 have been described as causes of MSMD. Instead, disease arises from point mutations and small insertions/deletions within the gene.

## 5. Environmental Information

### 5.1 Environmental Factors: Toxins, Radiation, Pollution, Occupational Exposure

Non-infectious environmental factors such as chemical toxins, radiation, and occupational exposures have not been implicated in the etiology of Immunodeficiency 28. The disease is fundamentally driven by inborn defects in IFNGR2, and environmental modifiers act primarily through infectious exposure rather than through direct toxicity to immune cells. There is no evidence that pollutants or radiation cause de novo IFNGR2 mutations at rates sufficient to influence disease burden; instead, the genetic lesions arise in germ cells and are transmitted hereditarily.

### 5.2 Lifestyle Factors

Lifestyle factors such as smoking, diet, exercise, and alcohol consumption have not been specifically studied in IMD28. Given the usually pediatric onset of the disease, adult lifestyle habits are largely irrelevant to initial manifestation, though they may affect infection outcomes in partial deficiency cases that persist into adulthood. Good nutritional status and absence of co-morbidities may improve resilience to infection and tolerance of antimycobacterial drugs, but these are generic considerations for infectious diseases. No specific dietary or lifestyle regimen has been demonstrated to prevent mycobacterial disease in IFNGR2-deficient patients.

### 5.3 Infectious Agents: Mycobacteria and Salmonella

In contrast, infectious agents are central environmental contributors. The primary pathogens involved in IMD28 are mycobacteria and, to a lesser extent, *Salmonella* species. OMIM and MalaCards note that the most commonly encountered mycobacterial pathogens include *Mycobacterium bovis* BCG, *M. avium*, and *M. fortuitum*.[1][2][9][18] Mendelian.co adds *M. abscessus* to this list and emphasizes infections by “other environmental mycobacteria (EM).”[9] The MSMD literature documents additional species such as *M. chelonae*, which caused fatal infection in one patient with partial AR IFNGR2 deficiency.[13] Orphanet summarizes that complete IFN-γR2 deficiency leads to severe infection with BCG and environmental mycobacteria, while partial deficiency can predispose to moderately severe, recurrent infections with BCG and EM.[9][15]

Salmonella infections, both typhoidal and non-typhoidal, reflect the shared role of IFN-γ in defense against intracellular Gram-negative bacteria. Immunodeficiencysearch.com notes that IFN-γ receptor deficiencies are associated with “severe salmonella infections,” and MSMD reviews corroborate increased susceptibility to *Salmonella* species.[10][11][20] In practice, this translates into severe sepsis, focal osteomyelitis, or recurrent bacteremia following relatively minor exposures. Other pathogens, such as *Histoplasma* and certain viruses, have occasionally been reported in IFN-γ pathway defects, but in IFNGR2 deficiency, mycobacteria and *Salmonella* remain the defining infectious agents.[10][11][20]

In NCBI Taxonomy terms, the relevant species include *Mycobacterium bovis* (taxon ID 1765), *Mycobacterium avium* (1764), *Mycobacterium fortuitum* (1766), *Mycobacterium abscessus* (36809), *Mycobacterium chelonae* (1767), and *Salmonella enterica* subspecies (taxon ID 28901). These pathogens are widespread in the environment or in vaccine preparations, making exposure nearly inevitable in many settings.

## 6. Mechanism / Pathophysiology

### 6.1 Causal Chain from Mutation to Clinical Manifestation

The pathophysiology of Immunodeficiency 28 can be conceptualized as a series of causal steps linking the initiating lesion—germline IFNGR2 mutation—to the clinical phenotype of disseminated mycobacterial disease. In narrative form, these steps unfold as follows.

Step 1: Bi-allelic or mono-allelic pathogenic variants in IFNGR2 alter the structure, expression, glycosylation, or trafficking of the interferon-gamma receptor 2 chain in hematopoietic cells, leading to absent or reduced functional receptor at the cell surface.[1][14][16][18]

Step 2: This receptor defect leads to failure of IFN-γR2 recruitment to the IFN-γ–IFNGR1 complex upon ligand binding, or to failure of the assembled receptor to activate JAK2 and STAT1, resulting in markedly diminished or absent IFN-γ–induced STAT1 phosphorylation and gene transcription in macrophages, monocytes, dendritic cells, and T cells.[10][11][16][18][20]

Step 3: The impaired IFN-γ signaling leads to defective macrophage activation, including reduced induction of antimicrobial effector pathways such as production of nitric oxide, reactive oxygen species, induction of autophagy, and upregulation of key host defense genes, thereby severely compromising intracellular killing of mycobacteria and *Salmonella*.[10][11][13][20]

Step 4: In the context of exposure to BCG vaccine strains or environmental mycobacteria, this impaired macrophage effector response leads to uncontrolled replication of mycobacteria within phagosomes and failure to contain infection within well-structured granulomas, resulting in disseminated infection and widespread tissue damage.[10][11][15][20]

Step 5: Persistent antigenic stimulation due to uncontrolled infection drives excessive and prolonged IFN-γ production by T helper 1 (Th1) cells and natural killer (NK) cells, but because IFN-γ signaling is blocked at the receptor level, this cytokine cannot exert negative feedback or protective effects, resulting in high plasma IFN-γ levels without corresponding functional benefits.[2][11][13][15][20]

Step 6: The combination of uncontrolled infection and dysregulated inflammatory cytokine milieu leads to granulomatous and necrotizing lesions in multiple organs, including lymph nodes, liver, spleen, bones, and lungs, manifesting clinically as lymphadenopathy, hepatosplenomegaly, osteomyelitis, pulmonary infiltrates, and systemic inflammatory symptoms.[14][15][18][20]

Step 7: Over time, repeated infection episodes, chronic inflammation, and tissue destruction, combined with potential drug toxicity from prolonged antimycobacterial regimens, result in progressive organ dysfunction, failure to thrive, and increased mortality, unless IFN-γ–independent immunity can partially compensate or hematopoietic stem cell transplantation restores functional IFNGR2 expression.[11][12][15][19][20]

These steps are strongly supported by human genetic and immunologic data, with most aspects directly demonstrated by functional studies in patient-derived cells and recombinant proteins.[11][13][14][16][18][20] Where mechanistic links involving downstream metabolic changes or specific pathways such as autophagy are less directly measured in IFNGR2-deficient humans, they are inferred from broader IFN-γ biology and model systems.

### 6.2 Molecular Pathways: The IL-12/IFN-γ/STAT1 Axis

At the molecular level, Immunodeficiency 28 is an archetypal disease of the IL-12/IFN-γ/STAT1 axis. In normal immunity, macrophages infected with mycobacteria produce interleukin-12 (IL-12), which stimulates Th1 T cells and NK cells to produce IFN-γ.[10][11][20] IFN-γ then binds to the IFN-γ receptor composed of IFNGR1 and IFNGR2 on macrophages, triggering the JAK1/JAK2–STAT1 signaling cascade that activates transcription of IFN-γ–responsive genes involved in antimicrobial defense.[10][11][16][20] This pathway can be described by Gene Ontology (GO) terms such as “response to interferon-gamma” (GO:0034341), “interferon-gamma-mediated signaling pathway” (GO:0060333), and “positive regulation of macrophage activation” (GO:0010758).

In IFNGR2 deficiency, the proximal defect resides at the level of receptor assembly and signaling. Structural studies of the IFN-γ receptor complex have shown that IFN-γ first engages IFNGR1 to form a 2:2 IFN-γ–IFNGR1 intermediate complex, which then recruits two IFNGR2 chains to assemble a 2:2:2 hexameric signaling complex.[16][18] The T168N mutation in IFNGR2, for example, places a neoglycan directly at the site 3 interface required for IFNGR2 docking, sterically preventing recruitment of IFNGR2(T168N) to the intermediate complex.[16][18] As a result, JAK2 associated with IFNGR2 cannot be brought into proximity with JAK1 bound to IFNGR1, blocking trans-phosphorylation and downstream STAT1 activation.

The central downstream effector is STAT1, a transcription factor that translocates to the nucleus upon tyrosine 701 phosphorylation and binds gamma-activated sequence (GAS) elements to induce genes such as IRF1, CXCL9/10, inducible nitric oxide synthase (NOS2), and many others involved in host defense.[11][13][20] In IFNGR2-deficient cells, IFN-γ fails to induce STAT1 phosphorylation, although other cytokines such as type I interferons may still engage STAT1 through distinct receptors. This selective blockade explains why patients retain resistance to many viral infections while being profoundly susceptible to mycobacteria and *Salmonella*, pathogens particularly reliant on IFN-γ–driven macrophage microbicidal mechanisms.

### 6.3 Cellular Processes: Macrophage Activation, Granuloma Formation, and Inflammation

At the cellular level, IFNGR2 deficiency impairs several critical processes. Macrophage activation, as noted, is defective. IFN-γ normally enhances phagosome–lysosome fusion, phagolysosomal acidification, induction of antimicrobial peptides, and autophagy, all of which contribute to killing of intracellular mycobacteria.[11][13][20] Without functional IFN-γ signaling, macrophages exhibit diminished microbicidal capacity, allowing mycobacteria to persist and replicate within phagosomes. GO terms such as “macrophage activation” (GO:0042116), “phagocytosis” (GO:0006911), and “autophagy” (GO:0006914) capture these affected processes.

Granuloma formation is also altered. In intact IFN-γ immunity, granulomas are organized structures composed of activated macrophages, multinucleated giant cells, T cells, and fibroblasts that wall off mycobacterial infection and limit dissemination. In IFN-γ receptor deficiencies, including IFNGR2, granulomas may be absent, poorly organized, or necrotic, reflecting a failure of macrophages to differentiate into the activated phenotype required for effective containment.[10][11][20] Clinically, patients with AR complete IFN-γ receptor deficiency often “fail to form well-circumscribed mycobacterial granulomas” and suffer disseminated infection following BCG administration.[10] The CL (Cell Ontology) terms relevant here include “macrophage” (CL:0000235), “monocyte” (CL:0000576), “T helper cell” (CL:0000912), and “natural killer cell” (CL:0000623).

Inflammation is paradoxically both impaired and excessive. On one hand, the failure of IFN-γ–mediated macrophage activation results in insufficient production of certain inflammatory mediators and reduced killing of pathogens. On the other hand, persistent infection drives chronic production of IFN-γ and other cytokines such as TNF-α, IL-6, and IL-1β, leading to systemic inflammation, fever, and tissue damage. The high plasma IFN-γ levels seen in IFNGR2 deficiency exemplify this dysregulated inflammatory environment.[2][11][15][20]

### 6.4 Protein Dysfunction: Misfolding, Misglycosylation, and Loss of Function

At the protein level, IFNGR2 mutations in IMD28 alter the receptor in several ways. Missense mutations like T168N introduce new glycosylation motifs, leading to the attachment of N-linked glycans at inappropriate positions. Mendoza et al. demonstrated that the IFNGR2(T168N) extracellular domain is glycosylated at the T168N position with almost quantitative occupancy, and that this neoglycan prevents IFNGR2 from being recruited to the signaling complex after IFN-γ addition.[16][18] This is a prototypical example of how a gain of glycosylation at a critical interface can produce a loss-of-function phenotype.

Splice site mutations, such as c.207-1G>A, cause in-frame deletions of key residues in the FN3 domain, potentially affecting folding stability and surface expression.[14] Other mutations may result in misfolded proteins that are retained in the endoplasmic reticulum or targeted for degradation, lowering cell surface receptor density. In some complete deficiencies, the extracellular domain mutations abolish cell surface expression entirely, as observed in early cases, leading to a “non-expressive” phenotype where IFNGR2 protein is absent from the membrane despite intact IFNGR1.[18][20]

Loss-of-function is the dominant functional consequence. IFN-γ cannot properly signal through defective IFNGR2, regardless of whether the receptor is absent or nonfunctional. This disrupts downstream JAK2–STAT1 activation and gene induction, as evidenced by functional assays in patient fibroblasts, EBV-transformed B cells, and primary macrophages.[13][14][20] There are no known gain-of-function IFNGR2 mutations that cause hyper-responsiveness to IFN-γ; the clinical phenotypes of MSMD are exclusively associated with reduced IFN-γ signaling.

### 6.5 Metabolic Changes and Immune System Involvement

Metabolic changes in IFNGR2 deficiency are not comprehensively characterized in human studies, but IFN-γ is known to reprogram macrophage metabolism toward a more glycolytic and oxidative state conducive to antimicrobial activity. Loss of IFN-γ signaling may maintain macrophages in a less activated metabolic state, impairing their ability to generate reactive nitrogen and oxygen intermediates necessary for mycobacterial killing. These changes can be conceptualized under GO terms such as “cellular response to cytokine stimulus” (GO:0071345) and “regulation of reactive oxygen species metabolic process” (GO:2000377).

The immune system involvement in IMD28 is highly specific. Innate immune cells such as macrophages and dendritic cells are directly affected by IFNGR2 defects, as they rely heavily on IFN-γ for activation. Adaptive immune cells, particularly Th1 cells and NK cells, produce IFN-γ but cannot achieve effective effector functions through macrophage activation. Interestingly, T cells themselves may require IFN-γ signaling for optimal differentiation and memory, but the primary clinical impact of IFNGR2 deficiency is in macrophage-mediated containment of mycobacteria.[11][13][20] Other arms of immunity, including humoral responses, cytotoxic T lymphocyte function against viruses, and complement activity, appear relatively intact.

### 6.6 Tissue Damage Mechanisms and Biochemical Abnormalities

Tissue damage in IFNGR2 deficiency arises from a combination of unchecked pathogen replication and chronic granulomatous inflammation. Mycobacteria proliferate within macrophages and disseminate via the bloodstream and lymphatics, seeding multiple organs. The host response consists of inflammatory infiltrates with macrophages, T cells, and necrosis, but the inability to organize effective granulomas leads to diffuse tissue destruction.[14][15][20] In bone, this manifests as osteomyelitis and structural deformities; in the liver and spleen, as hepatosplenomegaly and impaired function; in the lungs, as cavitary lesions and fibrosis. Mechanisms such as oxidative stress, chronic TNF-α production, and matrix metalloproteinase activity likely contribute, though these have not been specifically measured in IFNGR2-deficient tissues.

Biochemically, the signature abnormality is receptor dysfunction of the IFN-γ pathway. This can be categorized within OMIM and GO as “interferon-gamma receptor deficiency” and “abnormal STAT1 phosphorylation in response to interferon-gamma.”[10][11][15][20] Enzymatic pathways themselves are not directly defective; rather, their upstream regulatory signals are absent. The IL-12 pathway upstream of IFN-γ production generally remains intact, leading to normal or elevated IL-12 levels and IFN-γ production, making the IFNGR2 lesion a pure signaling defect.

### 6.7 Molecular Profiling and Advanced Technologies

Comprehensive molecular profiling such as transcriptomics, proteomics, and metabolomics has not yet been widely applied in cohorts of IFNGR2-deficient patients, primarily due to the rarity of the disease. However, studies of MSMD have used gene expression analyses in patient cells to document impaired induction of IFN-γ–responsive genes and preserved responses to other cytokines.[11][13][20] For example, overexpression systems and primary cell cultures have shown that IFNGR2 mutant proteins are produced in small amounts with impaired function, as demonstrated by diminished IFN-γ–induced expression of target genes in EBV-transformed B cells and fibroblasts.[13][14][20] These data align with the expected transcriptomic signature of IFN-γ receptor loss-of-function, featuring blunted upregulation of IFN-γ signature genes.

Single-cell analyses, spatial transcriptomics, and multi-omics integration have not yet been reported specifically for IMD28, though they represent promising tools for future research. CRISPR-based functional genomics screens have identified IFN-γ pathway components as critical for mycobacterial control in model systems, but IFNGR2 itself was already known as a causal gene from human genetics and has not been the target of discovery screens. As such technologies become more accessible, they may elucidate cell-type specific mechanisms and compensatory pathways in IFNGR2 deficiency.

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

Immunodeficiency 28 affects multiple organ systems, primarily through disseminated mycobacterial infection and associated granulomatous inflammation. The lymphatic system is prominently involved, with generalized lymphadenopathy reflecting widespread infection in lymph nodes. The liver and spleen are often enlarged and infiltrated by granulomas, leading to hepatosplenomegaly and potential compromise of hepatic and splenic functions.[14][15][18][20] Bones and joints are commonly affected, with multifocal osteomyelitis and arthritis due to mycobacterial seeding, particularly in partial IFN-γ receptor deficiencies where multifocal NTM osteomyelitis is a hallmark.[10][11][20] The lungs are frequently involved, showing nodular or cavitary lesions on imaging and histopathologic evidence of granulomatous inflammation.

In Uberon terms, key organs include “lymph node” (UBERON:0000029), “spleen” (UBERON:0002106), “liver” (UBERON:0002107), “bone” (UBERON:0001474), and “lung” (UBERON:0002048). Secondary organ involvement may include skin (local BCG site, cutaneous lesions), gastrointestinal tract, and central nervous system in cases of disseminated infection. The immune system as a whole (UBERON:0002405) is engaged but functionally compromised in a specific pathway.

### 7.2 Tissue and Cell-Level Targets

At the tissue level, IFNGR2 deficiency primarily affects hematopoietic tissues and mononuclear phagocyte populations. Macrophages resident in various tissues (liver Kupffer cells, alveolar macrophages, splenic macrophages) are key target cells, as they require IFN-γ signaling to become fully activated and microbicidal.[10][11][20] Monocytes circulating in blood and infiltrating infected tissues are likewise affected. Dendritic cells also express IFN-γ receptors and may have impaired maturation and antigen presentation in IFNGR2 deficiency, though clinical data on this are limited.

Cell Ontology terms relevant to IMD28 include “macrophage” (CL:0000235), “monocyte” (CL:0000576), “dendritic cell” (CL:0000451), “T helper 1 cell” (CL:0000913), and “natural killer cell” (CL:0000623). While Th1 cells and NK cells produce IFN-γ in response to infection, their own ability to respond to IFN-γ via IFNGR2 may also be compromised, potentially affecting cell-intrinsic functions such as survival and memory formation. Nevertheless, the clinical phenotype is dominated by macrophage failure to control intracellular pathogens.

Non-hematopoietic tissues such as fibroblasts can also express IFN-γ receptors and have been used in functional assays, but their dysfunction plays a lesser clinical role. Endothelial cells, epithelial cells, and other tissue-resident cell types may exhibit altered response to IFN-γ, potentially influencing local inflammation and barrier functions, but data in IFNGR2 deficiency are sparse.

### 7.3 Subcellular Localization and Compartment Involvement

At the subcellular level, IFNGR2 is a plasma membrane protein localized to the cell surface, where it participates in receptor complexes. GO cellular component terms include “plasma membrane” (GO:0005886) and “integral component of plasma membrane” (GO:0005887). Pathogenic variants can affect localization by preventing proper trafficking from the endoplasmic reticulum and Golgi to the cell surface, leading to retention in the ER (GO:0005783) or aberrant degradation. The IFN-γ receptor complex, once formed, transduces signals to the cytoplasm and nucleus, engaging “cytoplasm” (GO:0005737) and “nucleus” (GO:0005634) through JAK–STAT signaling.

Other subcellular compartments affected indirectly include phagosomes and lysosomes, where mycobacteria reside and are normally killed following IFN-γ–induced maturation and acidification. In IFNGR2 deficiency, phagosome–lysosome fusion and acidification are likely impaired, though specific GO component terms such as “phagolysosome” (GO:0045335) and “lysosome” (GO:0005764) have not been directly profiled in patient cells.

### 7.4 Localization and Lateralization

Clinically, IMD28 is a systemic disease without specific lateralization. Organ involvement is typically bilateral and symmetric, such as bilateral pulmonary infiltrates or generalized lymphadenopathy. Local manifestations, such as BCG injection site ulcers, are initially localized but often spread regionally and systemically. There is no evidence for preferential right- or left-sided involvement or particular neuroanatomical localization. Thus, lateralization descriptors are generally not applicable.

## 8. Temporal Development

### 8.1 Onset Pattern

The onset of Immunodeficiency 28 is usually congenital or early pediatric, with clinical manifestations appearing following environmental exposure to mycobacteria. In many countries, BCG vaccination is administered in the neonatal period, often within the first days of life. In infants with complete IFNGR2 deficiency, local BCG-related symptoms may emerge within weeks to months, followed by regional lymphadenitis and systemic dissemination within the first two to three years.[9][10][14][15] Orphanet emphasizes that severe infections begin “before the age of 3” in complete deficiency, while MSMD reviews note that complete IFN-γ receptor defects are “Mendelian in childhood and always lethal before the third decade of life” without HSCT.[11][15][20]

The onset pattern is typically subacute to chronic, rather than acute fulminant. Initial localized infection may be misinterpreted as typical vaccine reaction, delaying recognition of underlying immunodeficiency. As disease progresses, subacute systemic symptoms emerge, including fevers, weight loss, and progressive organ enlargement, reflecting chronic infection and granulomatous inflammation. In partial IFNGR2 deficiency, onset may be later, in school-age children or adolescents, often triggered by BCG vaccination or environmental NTM exposure, and may be more episodic.

### 8.2 Disease Progression, Stages, and Course

Progression of IMD28 can be conceptualized in stages. An early stage involves localized infection (BCG site, regional lymph nodes), with symptoms such as ulceration, lymphadenitis, and mild systemic signs. An intermediate stage involves dissemination to organs such as liver, spleen, bone, and lung, leading to hepatosplenomegaly, osteomyelitis, and pulmonary lesions. An advanced stage involves widespread organ involvement, severe systemic inflammation, possible sepsis, and organ failure, culminating in death if not effectively treated or if HSCT is unavailable.[14][15][19][20] The rate of progression is rapid to moderate in complete deficiency, often unfolding over months to a few years, whereas in partial deficiency progression may be slower and occasionally limited to specific sites.

The disease course pattern is generally chronic and progressive, punctuated by episodic exacerbations corresponding to infectious flares. Remission may occur transiently with aggressive antimycobacterial therapy, but relapse is common because underlying immunity remains defective. In partial deficiency, periods of remission may be longer, and infections may be fully cured with appropriate therapy, consistent with “curable infections with tuberculoid granulomas later in life” described for some partial IFNGR2 deficiency cases.[2][11][13]

### 8.3 Remission Patterns and Critical Periods

Remission patterns in IMD28 are primarily treatment-induced rather than spontaneous. Prolonged courses of multidrug antimycobacterial therapy can suppress pathogen burden and ameliorate symptoms, resulting in clinical improvement. However, cessation of therapy may lead to relapse, particularly if mycobacteria persist in protected niches. HSCT, when successful, can induce long-term remission or cure by reconstituting donor-derived hematopoietic cells with functional IFNGR2, thereby restoring IFN-γ signaling and enabling effective control of mycobacteria.[12][19]

Critical periods for intervention include the neonatal and early childhood windows when BCG vaccination and environmental exposure first reveal the defect. Avoidance of BCG in infants from high-risk families and early genetic testing in siblings of known cases can prevent fatal vaccine-related disease. Preemptive HSCT may be considered in complete deficiency before irreversible organ damage occurs. Likewise, early initiation of antimycobacterial therapy at the first sign of BCG or NTM disease can limit dissemination and improve outcomes.

## 9. Inheritance and Population

### 9.1 Epidemiology: Prevalence and Incidence

Immunodeficiency 28 is an ultra-rare disease. Orphanet estimates prevalence of MSMD due to complete IFN-γR2 deficiency as less than 1 per 1,000,000, and notes that “only ten children have been identified to date.”[15] This figure refers specifically to complete deficiency; partial IFNGR2 deficiencies add additional cases but remain rare. Given global population size, this translates into an incidence far below 1 per 100,000 live births per year, likely in the range of one or a few cases worldwide annually.

Because no population-based registries exist for IMD28, precise incidence and prevalence estimates are difficult. Many cases likely go undiagnosed or misdiagnosed, especially in settings with limited access to specialized immunologic and genetic testing. Nonetheless, the rarity of reported cases, coupled with the highly penetrant nature of complete deficiency and the severity of the phenotype, support the classification of IMD28 as an ultra-rare primary immunodeficiency.

### 9.2 Inheritance Pattern, Penetrance, and Expressivity

Complete IFNGR2 deficiency, corresponding to Immunodeficiency 28 as defined by OMIM and Orphanet, is inherited in an autosomal recessive manner.[1][9][15][18] Affected individuals are homozygous or compound heterozygous for pathogenic loss-of-function IFNGR2 variants, while parents are typically asymptomatic heterozygous carriers. Genetic counseling in affected families emphasizes a 25% recurrence risk for each pregnancy and the importance of carrier testing in relatives.[15] Consanguinity is common among reported families, facilitating homozygosity for rare mutations.[14][15][18][20]

Penetrance of complete IFNGR2 deficiency for severe mycobacterial disease appears to be near-complete. MSMD reviews state that complete IFN-γR1 and IFN-γR2 deficiencies are always lethal in childhood without HSCT, implying that almost all individuals with bi-allelic null mutations manifest disease.[11][20] Partial IFNGR2 deficiency, by contrast, exhibits variable penetrance. Autosomal recessive hypomorphic mutations may cause disease in homozygotes but not necessarily in heterozygotes; autosomal dominant partial deficiency due to haploinsufficiency has low penetrance, with many heterozygous carriers remaining clinically unaffected.[11][13][17][18]

Expressivity is also variable, particularly in partial deficiency. Some patients experience localized or limited disease, such as multifocal NTM osteomyelitis, while others develop disseminated infection. Age of onset, severity, and organ distribution differ among individuals with the same mutation, reflecting interaction with environmental exposures and polygenic background. In complete deficiency, expressivity is more consistently severe and early-onset, though specific organ manifestations may still vary.

Genetic anticipation, involving progressive increase in severity across generations, is not relevant to IMD28, as the disease is caused by stable, non-repeat expansion mutations. Germline mosaicism has not been reported, though in principle parents with mosaic pathogenic alleles could exist. Founder effects may occur in consanguineous communities where a particular IFNGR2 mutation is transmitted within extended families, as suggested by clusters of cases from certain regions, but detailed population genetic studies are lacking.[14][18]

Carrier frequency for IFNGR2 pathogenic alleles in the general population remains unknown. Given the rarity of reported cases, carrier frequency is likely extremely low globally, though may be higher in isolated populations with high consanguinity. gnomAD and similar databases document rare IFNGR2 variants, but most are benign or of uncertain significance; pathogenic alleles are too rare to provide meaningful carrier frequency estimates.

### 9.3 Population Demographics and Geographic Distribution

The demographic profile of IMD28 patients reflects both genetic and environmental factors. Many reported cases originate from regions with high rates of consanguineous marriage and universal BCG vaccination, including Iran, Saudi Arabia, Turkey, India, and Lebanon.[14][17][18][20] For instance, Vogt et al.’s T168N cohort included children from Iran and Saudi Arabia, all from consanguineous parents.[18] Desai et al.’s splice site mutation family was from India, with consanguineous parents and multiple affected siblings.[14] Casanova’s MSMD cohort includes multiple Middle Eastern families with IFNGR2 defects.[11][13][20]

These geographic and cultural contexts create a convergence of risk factors: autosomal recessive inheritance facilitated by consanguinity, high exposure to BCG vaccine early in life, and environmental mycobacteria prevalent in water and soil. Consequently, IMD28 may be more frequently observed in such settings, though underdiagnosis remains likely. In high-income countries without routine neonatal BCG vaccination, complete IFNGR2 deficiency might present later via environmental mycobacteria or *M. tuberculosis*, and may be misdiagnosed as atypical infections without recognition of underlying immunodeficiency.

Sex ratio in IMD28 appears roughly balanced; IFNGR2 is an autosomal gene, and there is no evidence for sex-linked differences in susceptibility or severity. Age distribution is skewed toward infancy and early childhood in complete deficiency, while partial deficiency cases may extend into adolescence and adulthood. Ethnic backgrounds of reported patients reflect their countries of origin, but there is no evidence for ethnic predisposition independent of consanguinity and genetic drift.

## 10. Diagnostics

### 10.1 Clinical and Laboratory Tests

Diagnostic evaluation of Immunodeficiency 28 begins with clinical suspicion based on severe or unusual mycobacterial infections in otherwise healthy children. Laboratory tests then assess general immune status and specific IFN-γ pathway function. Routine tests include complete blood count, immunoglobulin levels, lymphocyte subsets, and vaccine antibody responses; these often appear normal in IFNGR2 deficiency, emphasizing the need for specialized assays.[11][13][20]

Functional tests of IFN-γ responsiveness are central. The diagnosis is suggested by absent or markedly impaired STAT1 phosphorylation in response to IFN-γ stimulation in patient leukocytes or fibroblasts, measured by flow cytometry or Western blot.[10][11][15][20] Immunodeficiencysearch.com notes that diagnosis is suggested by “impaired STAT1 phosphorylation in response to IFN-gamma signaling” and “absence of IFN-gamma receptor on the surface of lymphocytes” in some forms.[10] Orphanet describes that “leukocytes and fibroblasts from patients with this immunodeficiency do not respond to IFN-gamma in vitro.”[15]

Flow cytometric analysis of IFN-γ receptor surface expression can distinguish “expressive” from “non-expressive” IFNGR2 deficiency. In non-expressive forms, IFNGR2 is absent from the surface, whereas in expressive forms it is present but nonfunctional.[11][18][20] This information guides molecular interpretation of mutations and may influence therapeutic considerations. Additional IL-12/IFN-γ pathway screening studies recommended by immunodeficiencysearch.com include measurement of IFN-γ receptor surface expression, IL-12 receptor expression, and STAT1/STAT4 phosphorylation after cytokine stimulation.[10]

Measurement of plasma IFN-γ, IL-12p40, and IL-12p70 levels via ELISA can provide supporting evidence. Orphanet notes that IFN-γ, IL-12p40, and IL-12p70 levels can be measured after whole blood activation by BCG, BCG+IL-12, and BCG+IFN-γ; in IFNGR2 deficiency, IFN-γ levels are typically high, whereas IL-12 responses may be normal or elevated.[15] Elevated IFN-γ with absent cellular response is a characteristic signature.

Microbiologic testing identifies causative pathogens and informs treatment. Cultures, PCR, and histopathology of affected tissues detect BCG, NTM, or *M. tuberculosis*, and reveal granulomatous inflammation. Imaging studies such as X-ray, CT, and MRI document bone lesions, lymphadenopathy, and pulmonary involvement. Biopsy of lesions shows granulomas, necrosis, and mycobacterial organisms, confirming infection.

### 10.2 Genetic Testing

Confirmatory diagnosis of Immunodeficiency 28 requires genetic testing of IFNGR2. Single-gene sequencing of IFNGR2 by Sanger or next-generation methods is appropriate when IFN-γ pathway deficiency is suspected based on functional assays. OMIM and ClinVar provide reference sequences and mutation databases for IFNGR2; the MANE-select transcript NM_005534.4 is commonly used.[1][5][18] ClinVar lists specific variants and their clinical significance, such as the benign c.879+32dup, helping interpret test results.[5]

Whole exome sequencing (WES) has been instrumental in discovering novel IFNGR2 mutations in MSMD cohorts and familial cases. Desai et al. used WES in two affected Indian siblings and their consanguineous parents to identify the c.207-1G>A splice acceptor site variant in IFNGR2.[14] Similarly, Oleaga-Quintas et al. identified recessive IFNGR2 mutations affecting the initiation or second codon via WES, leading to partial deficiency in multiple patients.[13][17] WES is particularly useful when MSMD is suspected but specific gene defects are unknown, as it allows comprehensive evaluation of IFN-γ pathway genes.

Gene panels targeting primary immunodeficiencies or MSMD-associated genes include IFNGR2 along with IFNGR1, STAT1, IL12B, IL12RB1, ISG15, TYK2, IRF8, SPPL2A, NEMO, and CYBB.[11][13][20] These panels enable simultaneous assessment of multiple genes that can cause similar phenotypes. Chromosomal microarray, karyotyping, FISH, and mitochondrial DNA testing are generally not necessary for IMD28, as large structural changes and mitochondrial defects have not been implicated.

WGS may offer additional benefits by detecting deep intronic variants or structural changes in IFNGR2 not captured by WES, but given the known coding variants in most cases and the rarity of structural lesions, WES and targeted sequencing suffice for clinical diagnosis. Once a pathogenic IFNGR2 mutation is identified, segregation analysis in family members confirms inheritance pattern and informs carrier status.

### 10.3 Omics-based Diagnostics and Biomarkers

Omics-based diagnostics beyond targeted sequencing have limited current application in IMD28 due to its rarity. However, functional transcriptomic assays in patient cells can quantify IFN-γ–responsive gene expression and might serve as research tools to assess residual signaling in partial deficiency. Proteomics could evaluate STAT1 phosphorylation dynamics and receptor complex assembly, while metabolomics could identify signatures of impaired macrophage activation. None of these are currently standard in clinical practice for IFNGR2 deficiency.

Biomarkers for disease activity and prognosis include plasma IFN-γ levels, inflammatory markers such as C-reactive protein and TNF-α, and pathogen load assessed by cultures and imaging. Elevated IFN-γ is characteristic but not specific to IMD28, as other IFN-γ receptor deficiencies share this feature.[2][11][15][20] Nevertheless, sustained high IFN-γ despite persistent infection supports a diagnosis of receptor-level defects rather than cytokine deficiency, as AR IFN-γ deficiency itself causes MSMD but features low or absent IFN-γ levels.[17]

### 10.4 Clinical Criteria, Differential Diagnosis, and Screening

Standardized diagnostic criteria for IMD28 are not yet formalized in society guidelines, but MSMD reviews provide practical frameworks. Any child with severe or unusual mycobacterial disease, particularly disseminated BCG or environmental NTM infections, in the absence of HIV infection or generalized immunodeficiency, should prompt evaluation for MSMD, including IFNGR2 deficiency.[11][13][20] Poor or absent clinical and cellular response to IFN-γ, high plasma IFN-γ levels, and family history of similar infections strengthen suspicion.

Differential diagnosis includes other MSMD conditions such as IFNGR1 deficiency, IL12RB1 deficiency, IL12B deficiency, STAT1 deficiency, and ISG15 deficiency, as well as chronic granulomatous disease (CGD), severe combined immunodeficiency, and acquired immunodeficiency due to HIV or immunosuppressive drugs.[11][13][20] Distinguishing features include specific pathogen spectrum (for example predominance of mycobacteria and salmonella in MSMD), preserved general immune parameters in IFNGR2 deficiency, and specific functional and genetic tests.

Screening programs for asymptomatic individuals with IMD28 are not established, but cascade genetic testing in families with known IFNGR2 mutations is recommended. Prenatal diagnosis and preimplantation genetic testing can be offered to carrier couples, given the poor prognosis of complete deficiency and the availability of HSCT. Newborn screening at the population level is not currently feasible due to low prevalence and lack of simple assays, though targeted screening in high-risk families may be beneficial.

## 11. Outcome and Prognosis

### 11.1 Survival, Mortality, and Life Expectancy

The prognosis of Immunodeficiency 28 depends critically on the type of IFNGR2 deficiency and access to curative therapy. In complete autosomal recessive IFN-γR2 deficiency, survival without HSCT is poor. Orphanet reports that “prognosis is poor with most patients not living past 10 years of age,” and MSMD reviews state that complete IFN-γR1 and IFN-γR2 deficiencies are always lethal before the third decade of life in the absence of HSCT.[11][15][20] Mortality arises from uncontrolled mycobacterial infection, sepsis, and complications of chronic inflammation and organ damage.

With HSCT, survival prospects improve significantly. Tovo et al. documented “Successful hematopoietic stem cell transplantation in a patient with complete IFN-γ receptor 2 deficiency,” demonstrating that transplantation can cure the immunodeficiency by reconstituting donor-derived immune cells with functional IFNGR2.[12][19] Their case report and literature review suggest that HSCT offers the

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 37 |
| Terms named correctly | 22 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002721` (2 mentions) - the report calls it "Recurrent mycobacterial infections"; HP calls it **Immunodeficiency**
- `HP:0002715` (2 mentions) - the report calls it "Recurrent bacterial infections"; HP calls it **Abnormality of the immune system**
- `HP:0031644` (2 mentions) - the report calls it "Recurrent salmonella infections"; HP calls it **Fusiform abdominal aortic aneurysm**
- `HP:0001897` (1 mention) - the report calls it "Abnormal chest radiograph"; HP calls it **Normocytic anemia**
- `HP:0012430` (2 mentions) - the report calls it "Elevated circulating interferon-gamma level"; HP calls it **Cerebral white matter hypoplasia**
- `HP:0032150` (2 mentions) - the report calls it "Abnormal response to interferon-gamma"; HP calls it **Paroxysmal rectal pain**
- `CL:0000913` (1 mention) - the report calls it "T helper 1 cell"; CL calls it **effector memory CD8-positive, alpha-beta T cell**
- `GO:0005887` (1 mention) - the report calls it "integral component of plasma membrane"; GO calls it **GO_0005887**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0005385` (2 mentions), reported as "Disseminated Bacille Calmette–Guérin infection" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005887` (GO_0005887) (1 mention) - replaced by `GO:0005886`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0005381` (2 mentions) - the report calls it "Bacille Calmette–Guérin infection"; HP calls it **Recurrent Neisseria meningitidis infection**, and lists "Chronic menigococcal infection" among its other names
- `HP:0003623` (3 mentions) - the report calls it "Onset in early childhood", "Neonatal onset", "Early childhood onset"; HP calls it **Neonatal onset**
- `GO:0034341` (1 mention) - the report calls it "response to interferon-gamma"; GO calls it **response to type II interferon**, and lists "response to gamma-interferon" among its other names
- `GO:0010758` (1 mention) - the report calls it "positive regulation of macrophage activation"; GO calls it **regulation of macrophage chemotaxis**
- `GO:0006911` (1 mention) - the report calls it "phagocytosis"; GO calls it **phagocytosis, engulfment**
- `UBERON:0001474` (1 mention) - the report calls it "bone"; UBERON calls it **bone element**, and lists "bone" among its other names
- `GO:0045335` (1 mention) - the report calls it "phagolysosome"; GO calls it **phagocytic vesicle**, and lists "phagosome" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0003623` - called "Onset in early childhood", "Neonatal onset", "Early childhood onset"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Orphanet`.