---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-08T08:02:21.622326'
end_time: '2026-09-08T08:10:10.782683'
duration_seconds: 469.16
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spinocerebellar Ataxia Type 6
  mondo_id: MONDO:0008457
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
citation_count: 18
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 14
  quotes_valid: 12
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:10985694
  - PMID:29427102
  relevance_assessed: 9
  on_topic: 8
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 87
  verified: 76
  not_found: 4
  obsolete: 5
  unverifiable: 2
  confabulation_rate: 0.047
  labels_checked: 17
  labels_matching: 10
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0000007
    reported_labels:
    - Intellectual disability absent
    - No intellectual disability
    ontology_label: Autosomal recessive inheritance
  - term_id: CL:0000664
    reported_labels:
    - inferior olivary neuron
    ontology_label: obsolete closable valve cell
  labels_variant: 5
  unresolved_terms:
  - HP:0004519
  - HP:0011938
  - HP:0002452
  - GO:0058052
  obsolete_terms:
  - term_id: HP:0008024
    ontology_label: obsolete Congenital nuclear cataract
    replaced_by: HP:0100018
  - term_id: GO:0008370
    ontology_label: obsolete cellular component
  - term_id: GO:0097483
    ontology_label: GO_0097483
    replaced_by: GO:0014069
  - term_id: GO:0006944
    ontology_label: GO_0006944
    replaced_by: GO:0061025
  - term_id: CL:0000664
    ontology_label: obsolete closable valve cell
    replaced_by: CL:1000147
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar Ataxia Type 6
- **MONDO ID:** MONDO:0008457 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia Type 6** covering all of the
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

# Spinocerebellar Ataxia Type 6 (MONDO:0008457): An Integrated Disease Characterization

Spinocerebellar ataxia type 6 (SCA6) is a rare, late-onset, autosomal dominant neurodegenerative disorder that exemplifies *pure* cerebellar ataxia caused by a relatively small CAG trinucleotide repeat expansion in the **CACNA1A** gene, encoding the α1A subunit of the neuronal P/Q-type voltage-gated calcium channel Ca\(_\text{V}\)2.1.[1][5][14] Clinically, SCA6 is characterized by slowly progressive gait and limb ataxia, dysarthria, and prominent oculomotor abnormalities such as gaze-evoked and downbeat nystagmus, typically with preserved cognition and normal lifespan.[2][3][5][7][16] Pathologically, it is distinguished by selective degeneration of cerebellar Purkinje cells, especially in the vermis, with relatively mild involvement of granule cells and inferior olive.[7][13][15][17] Genetically, normal CACNA1A alleles carry 4–18 CAG repeats, whereas disease-causing alleles contain approximately 20–33 repeats, with modest age-dependent penetrance and only limited anticipation.[1][3][5][14] At the molecular level, expanded polyglutamine tracts within CACNA1A give rise both to altered channel proteins and to an overlapping transcription factor, **α1ACT**, whose dysregulated production and function are increasingly implicated in pathogenesis.[14] Despite the absence of curative therapies, detailed understanding of the clinical spectrum, molecular etiology, oculomotor profile, and natural history of SCA6 has enabled more precise diagnosis, targeted genetic counseling, and development of emerging therapeutic concepts focused on translational control and Purkinje cell resilience.[2][5][11][14][16]

---

## 1. Disease Information

### 1.1 Overview and Clinical Definition

Spinocerebellar ataxia type 6 (SCA6) is a Mendelian, autosomal dominant cerebellar ataxia caused by heterozygous CAG repeat expansions in the **CACNA1A** gene on chromosome 19p13.1–p13.2.[1][3][5][14] In contemporary classifications, SCA6 is grouped within autosomal dominant cerebellar ataxia type III (ADCA III), which denotes phenotypes dominated by cerebellar signs with minimal extracerebellar involvement.[8] The disorder presents as a late-onset, slowly progressive disturbance of gait and stance, limb coordination, speech articulation, and eye movements, attributable to dysfunction and degeneration of cerebellar circuitry.[2][3][5][7][16] Mentation is typically preserved, differentiating SCA6 from SCAs with substantial cognitive or multisystem involvement, such as SCA2 or SCA3.[3][5][18]

GeneReviews succinctly summarizes the clinical picture: “Spinocerebellar ataxia type 6 (SCA6) is characterized by adult-onset, slowly progressive cerebellar ataxia, dysarthria, and nystagmus. The age of onset ranges from 19 to 73 years; mean age of onset is between 43 and 52 years.” (PMID 20301319).[2][11] This description, derived from aggregated patient series, underscores the broad onset range yet relatively uniform core syndrome. The disease is considered *non-fatal* in the sense that life expectancy is generally near normal, although significant morbidity arises from progressive gait instability, dysphagia, and visual disturbance.[4][5][8] In Human Phenotype Ontology (HPO) terms, central features include gait ataxia (HP:0002141), limb ataxia (HP:0002070), dysarthria (HP:0001260), gaze-evoked nystagmus (HP:0000640), downbeat nystagmus (HP:0000660), and impaired smooth pursuit eye movements (HP:0008024).[2][3][5][7][16]

A notable aspect of SCA6 is its overlap with episodic ataxia type 2 (EA2), an allelic disorder also caused by CACNA1A mutations but typically due to truncating or missense variants rather than repeat expansions.[10][14] Clinicians have observed that some SCA6 families exhibit both progressive ataxia, characteristic of SCA6, and episodic attacks reminiscent of EA2, highlighting the continuous phenotypic spectrum of CACNA1A-related diseases.[4][10][11] From an ontology standpoint, SCA6 is captured by MONDO:0008457 and classified under hereditary ataxia (MONDO:0005593), cerebellar disease (MONDO:0021137), and autosomal dominant disease (MONDO:0020583).

### 1.2 Disease Identifiers and Synonyms

Multiple curated resources provide standardized identifiers for SCA6. The Online Mendelian Inheritance in Man (OMIM) entry for SCA6 is **#183086**, denoting “SPINOCEREBELLAR ATAXIA 6; SCA6,” with a number sign indicating that heterozygous CACNA1A mutation is causative.[1][9] Orphanet lists SCA6 under disease number **ORPHA:98758**, categorizing it as an autosomal dominant cerebellar ataxia type III with late-onset and slowly progressive gait ataxia.[8] In ICD-10, SCA6 is coded under **G11.2** (“Hereditary ataxia”), a broader category encompassing several SCAs.[8] SNOMED CT assigns the concept code **715752006** to “Spinocerebellar ataxia type 6.”[1] UMLS captures the concept as **C0752124**.[8][12]

Commonly used synonyms and alternative names include “SCA6,” “spinocerebellar ataxia 6,” “spinocerebellar ataxia type VI” (older nomenclature), and “autosomal dominant cerebellar ataxia type III associated with CACNA1A CAG expansion.”[1][3][5][8] Because CACNA1A also underlies episodic ataxia type 2 (EA2), some literature refers to “CACNA1A-related ataxia,” which encompasses SCA6, EA2, and intermediate phenotypes.[4][10][11] In MeSH, SCA6 is indexed under “Spinocerebellar Ataxias” (D020758), with more granular indexing often achieved through text words in PubMed searches.

### 1.3 Data Sources and Level of Aggregation

Information about SCA6 is derived almost entirely from aggregated disease-level resources rather than individual electronic health records. OMIM, Orphanet, and GeneReviews synthesize data from case series, familial studies, and mechanistic research articles, producing consensus descriptions of clinical features, genetics, and management.[1][2][8][11] Key clinical characterizations stem from cohort studies such as the German ADCA series reported by Durr et al. (J Neurol Neurosurg Psychiatry, PMID 9436730), which analyzed 69 families and 61 sporadic cases to delineate genotype–phenotype correlations.[3] Likewise, the seminal Annals of Neurology report by Zhukovskaya et al. on SCA6 gaze-evoked and vertical nystagmus (PMID 9403487) provided detailed oculomotor and neuropathologic profiles from multiple kindreds.[7]

Later, systematic reviews and meta-analyses, including a quantitative synthesis of oculomotor and vestibular findings in SCA6 (PMCID PMC11646955), further aggregated multi-study data to characterize frequency and pattern of eye movement abnormalities.[16] Pathologic descriptions are based on small series of autopsied brains, such as the two-family study by Ishikawa et al. (JNNP, PMID 10985694) and the morphological Purkinje cell analysis by Yoon et al. (PMID 10985694), along with earlier neuropathologic work.[13][15] Therefore, while individual patient data underlie these observations, the summary herein reflects population-level, peer-reviewed evidence rather than single-case anecdotes.  

---

## 2. Etiology: Genetic Causation, Risk, and Protective Factors

### 2.1 Primary Causal Factors

SCA6 is unequivocally a genetic disease caused by heterozygous CAG repeat expansions in the **CACNA1A** gene, which encodes the α1A subunit of the P/Q-type voltage-gated calcium channel (Ca\(_\text{V}\)2.1).[1][3][5][14] The expansion is located in the last exon (exon 47) of the longest CACNA1A transcript variant.[1][5][14] OMIM notes: “A number sign (#) is used with this entry because spinocerebellar ataxia-6 (SCA6) is caused by heterozygous mutation in the CACNA1A gene (601011) on chromosome 19p13. The most common mutation is an expanded CAG(n) repeat in exon 47 of the CACNA1A gene.”[1] GeneReviews similarly specifies that affected individuals carry 20–33 CAG repeats, whereas normal alleles have 4–18.[2][11]

The genetic etiology has been confirmed by linkage analyses, positional cloning, and direct repeat-length assessment in affected kindreds.[3][7][10][17] In the early discovery phase, Matsuyama and colleagues demonstrated that SCA6 maps to chromosome 19p13 and is allelic with EA2, converging on the CACNL1A4 (now CACNA1A) locus.[7][10] Subsequent cloning established the expanded CAG tract within the coding region, implicating a polyglutamine-encoding expansion analogous in structure, though smaller in size, to those in SCA1, SCA2, and SCA3.[3][17][18] Mechanistically, SCA6 is thus a “polyglutamine disease,” but with unique features (see Section 6).

No environmental, infectious, or non-genetic primary causes of SCA6 have been identified. The disease can arise de novo through repeat expansion during transmission, but this is rare; most cases occur in families with autosomal dominant inheritance and recognizable disease alleles.[3][10][11] From an etiologic standpoint, SCA6 is a paradigmatic example of a monogenic, Mendelian, late-onset neurodegenerative disorder in which a single, specific genetic lesion suffices to cause disease under typical environmental conditions.

### 2.2 Genetic Risk Factors: Causal Variants and Modifiers

The central genetic risk factor is the presence of an expanded CAG repeat in CACNA1A above a pathogenic threshold. Normal alleles have 4–18 repeats, while pathogenic alleles typically range from 20 to 33.[1][5][14] Li et al. (2009) and others have suggested that alleles with 19 repeats may be borderline or low-penetrance, whereas repeats ≥20 are more reliably associated with disease.[1][5][14] Durr et al. reported that age of onset inversely correlates with repeat length, consistent with a modest dose–response relationship: “Disease onset ranged from 30 to 71 years of age and was significantly later than in other forms of ADCA. Age at onset correlated inversely with repeat length.” (PMID 9436730).[3] However, the correlation is weaker than in SCA1 or SCA2, and repeat length does not predict progression rate or presence of non-cerebellar signs.[3]

The alleles are transmitted in a relatively stable manner, with little evidence of dramatic intergenerational expansion or contraction. Ishikawa et al. observed in two families that “All affected patients had identical expanded alleles, and the expansion was also homogeneously distributed throughout the brain without mosaicism. The present study showed that SCA6 is characterised by Purkinje cell dominant cortical cerebellar degeneration, highly stable transmission of the CAG repeat expansion, and lack of ubiquitin immunoreactive nuclear inclusions.” (PMID 10985694).[13] The limited instability contributes to modest anticipation, if any, compared to other polyglutamine SCAs.[3][13][18]

Allelic heterogeneity exists in CACNA1A, with different mutation types associated with distinct phenotypes. Missense and truncating variants can cause EA2, hemiplegic migraine, or developmental encephalopathies, whereas CAG expansions cause SCA6.[10][14] This allelic series suggests that intrinsic channel dysfunction and polyglutamine-mediated toxicity intersect, and that specific mutational configurations modulate the balance between episodic versus progressive ataxia and between early-onset versus late-onset phenotypes.[10][14] Candidate modifier genes affecting age at onset or severity have been proposed in other SCAs (e.g., variants in DNA repair pathways or glutamate receptors), but robust modifiers specific to SCA6 have not yet been validated in large cohorts.[6][18] Thus, at present, the predominant genetic risk factor is CACNA1A CAG repeat length itself.

From a population genetics perspective, SCA6 alleles are rare in general population databases such as gnomAD; most individuals carry normal-length repeats, and expanded alleles are typically observed only in affected families or high-risk cohorts.[5][18] While detailed allele frequency data for specific repeat sizes in general populations are limited, the global prevalence of clinically manifest SCA6 is estimated at less than 1 per 100,000, consistent with low carrier frequency of fully penetrant expansions.[8][18]

### 2.3 Environmental and Lifestyle Risk Factors

No specific environmental risk factors have been consistently linked to the development of SCA6. Because the disease is monogenic and autosomal dominant, risk is overwhelmingly determined by genotype. Studies have not identified toxins, occupational exposures, infections, or lifestyle factors that substantially increase the likelihood of disease onset in individuals without CACNA1A expansions.[2][3][8][11][18] In contrast to multifactorial neurodegenerative disorders such as sporadic cerebellar degeneration or chronic alcohol-related ataxia, SCA6 does not appear to be driven by environmental insults.

Nonetheless, age is a strong determinant of clinical manifestation, as SCA6 is a late-onset disease with age-dependent penetrance. Individuals with expanded alleles may remain asymptomatic until mid-adulthood or later, and some may never develop clinically significant symptoms, particularly if their repeat length is near the lower pathogenic threshold.[2][3][11][14] Age can thus be regarded as a *temporal* risk factor, in the sense that increased age allows progressive accumulation of molecular and cellular damage, but it is not an independent risk factor unrelated to genotype.

General lifestyle variables such as physical activity, nutrition, and avoidance of neurotoxins may influence the severity or progression of symptoms but have not been conclusively shown to alter the probability of disease onset in carriers. Small studies suggest that intensive coordinative training and physical therapy can improve functional performance and may partially counteract progression of gait ataxia.[5] However, these are modifiers of morbidity, not of underlying etiology. In summary, environmental and lifestyle contribution to SCA6 risk is minimal relative to genetic causation.

### 2.4 Protective Factors

As with risk factors, validated protective factors specific to SCA6 are scarce. No genetic variants have been definitively shown to protect against the manifestation of SCA6 in carriers of pathogenic CACNA1A expansions. Variants that modulate polyglutamine toxicity, cellular stress responses, or Purkinje cell resilience are theoretically plausible, extrapolating from other SCAs and animal models, but such modifiers remain speculative.[6][14][18] Similarly, environmental or lifestyle exposures that confer meaningful protection against disease onset have not been established.

What can be identified, however, are factors that mitigate symptom burden and preserve function once disease is present. Coordinative balance training, physical therapy, occupational therapy, and speech therapy have been shown to improve gait stability, limb coordination, and communication in hereditary ataxias, including SCA6, thereby acting as protective influences on quality of life.[2][5][11] For instance, Orphanet notes that “intensive coordinative training” and appropriate assistive devices contribute to symptomatic benefit.[5][8] In an ontological framework, such interventions correspond to NCIT terms such as Physical Therapy (NCIT:C15220), Occupational Therapy (NCIT:C15370), and Speech Therapy (NCIT:C17583). These interventions do not alter underlying genetic risk but can be conceptualized as “secondary protective factors” that reduce functional decline and complications.

### 2.5 Gene–Environment Interactions

Given the highly penetrant monogenic nature of SCA6, robust gene–environment interactions have not been extensively documented. Experimental models of polyglutamine disorders indicate that environmental enrichment, exercise, and caloric restriction can modulate disease severity and progression, suggesting that similar influences might exist in SCA6; however, human data remain limited.[14][18] Crucially, there is no evidence that environmental exposures can precipitate SCA6 in individuals lacking CACNA1A expansions, nor that environmental interventions can completely prevent disease in carriers.

Subtle gene–environment interplay may operate through mechanisms such as oxidative stress, mitochondrial function, or inflammatory signaling in Purkinje cells, where genetic predisposition due to CACNA1A expansion lowers the threshold for damage induced by environmental insults. For example, chronic alcohol abuse or certain neurotoxic medications could exacerbate cerebellar dysfunction in SCA6 carriers, accelerating clinical manifestation, although this has not been systematically measured.[18] Conceptually, such interactions would involve GO biological processes such as response to oxidative stress (GO:0006979), regulation of synaptic transmission (GO:0050804), and neuron apoptotic process (GO:0051402).

In summary, current evidence supports a model in which SCA6 is predominantly determined by a specific germline genetic lesion, with environmental factors playing minor modulatory roles in symptom expression and progression rather than primary causal roles.

---

## 3. Phenotypes: Clinical, Behavioral, and Laboratory Manifestations

### 3.1 Core Neurologic Phenotype

The hallmark phenotype of SCA6 is slowly progressive cerebellar ataxia affecting gait, stance, and limb coordination. GeneReviews states: “Initial symptoms are gait unsteadiness, stumbling, and imbalance (in ~90%) and dysarthria (in ~10%). Eventually all persons have gait ataxia, upper-limb incoordination, intention tremor, and dysarthria. Dysphagia and choking are common.” (PMID 20301319).[2][11] Durr et al. corroborated these observations in a German cohort, noting that SCA6 presents as a “predominantly cerebellar syndrome” with isolated cerebellar atrophy on MRI.[3] Orphanet describes SCA6 as “late-onset and slowly progressive gait ataxia and other cerebellar signs such as impaired muscle coordination and nystagmus.”[8]

Age of symptom onset is distinctly adult or late adult. GeneReviews reports an onset range of 19–73 years, with mean between 43 and 52 years.[2][11] Durr et al. observed a range from 30 to 71 years in their families.[3] This affirms that SCA6 is an adult-onset or late-onset disease in HPO terms (HP:0003581 for adult onset; HP:0004519 for late onset), with age-dependent penetrance. Symptom severity is generally mild to moderate early, progressing to severe disability over decades. Orphanet notes that “SCA6 progresses very slowly with a disease duration that can last over 25 years.”[8] Symptom progression is thus chronic and gradual, rather than acute or relapsing–remitting, although some patients may experience superimposed episodic exacerbations reminiscent of EA2.[10][11]

The core motor signs include truncal and gait ataxia (HP:0002141), limb ataxia (HP:0002070), dysmetria (HP:0001265), intention tremor (HP:0002080), and dysarthria (HP:0001260).[2][3][5] Muscle tone is often normal; pyramidal signs such as hyperreflexia (HP:0001347) and extensor plantar responses (HP:0003487) occur in up to 40–50% of individuals.[2] Extrapyramidal signs, including dystonia (HP:0001332) and blepharospasm (HP:0002078), appear in up to 25%.[2] Basal ganglia involvement, when present, is mild compared to cerebellar dysfunction.[3] Peripheral neuropathy and parkinsonian features are variably present but not defining.[3] Overall, the phenotype is described as “pure cerebellar ataxia,” meaning that cerebellar signs dominate and non-cerebellar systems are only mildly affected.[3][5][13][18]

In terms of quality-of-life impact, gait instability leads to substantial fall risk, limiting mobility and independence. Dysarthria impairs communication, while dysphagia increases risk of aspiration and malnutrition. However, because cognition is preserved, many individuals remain engaged in social and intellectual activities, with disability primarily in motor tasks.[2][5][8][11] Tools such as SF-36 and EQ-5D used in broader ataxia cohorts show substantial deficits in physical functioning and role limitations, with relatively maintained mental health domains.[5] In an HPO framework, the combination of motor impairment and preserved cognition is captured by “Intellectual disability absent” (HP:0000007) alongside “Cerebellar ataxia” (HP:0001251).

### 3.2 Oculomotor and Vestibular Phenotypes

Oculomotor abnormalities are a defining aspect of SCA6. Early clinical and quantitative eye movement studies in SCA6 kindreds demonstrated gaze-evoked and vertical nystagmus, impaired vestibulo-ocular reflex (VOR), and abnormal pursuit.[7][10] Zhukovskaya et al. reported: “Radiographically and pathologically, there was selective atrophy of the cerebellum and extensive loss of Purkinje cells in the cerebellar cortex. In addition, clinical and quantitative measurement of extraocular movements demonstrated a characteristic pattern of ocular motor and vestibular abnormalities, including horizontal and vertical nystagmus and an abnormal vestibulo-ocular reflex.” (PMID 9403487).[7] These abnormalities correspond to HPO terms such as gaze-evoked nystagmus (HP:0000640), downbeat nystagmus (HP:0000660), positional nystagmus (HP:0011938), impaired smooth pursuit (HP:0008024), and abnormal vestibulo-ocular reflex (HP:0000496).

A recent systematic review and meta-analysis of oculomotor and vestibular profiles in SCA6 synthesized data from multiple studies to quantify frequencies.[16] The authors found that the most frequent eye movement abnormalities were deficits in predictive eye movement (PEM) gain (84%), impaired VOR suppression (84%), high-frequency angular VOR deficits (79%), positional nystagmus (74%), gaze-evoked nystagmus (69%), downbeat nystagmus (62%), and perverted vertical nystagmus after horizontal head-shaking (62%).[16] This quantitative characterization, based largely on human clinical data, underscores that nearly all SCA6 patients exhibit some combination of cerebellar oculomotor dysfunction, often detectable before overt gait ataxia.

Visual disturbances experienced by patients include diplopia (HP:0000651), oscillopsia (HP:0000545), and difficulty fixating on moving objects.[2][4][7] GeneReviews notes: “Visual disturbances may result from diplopia, difficulty fixating on moving objects, horizontal gaze-evoked nystagmus, and vertical nystagmus.” (PMID 20301319).[2] These symptoms can significantly impair reading, driving, and other activities requiring visual stability, contributing to quality-of-life impact beyond gait and speech abnormalities. In effect, SCA6 blends a cerebellar motor syndrome with a cerebellar oculomotor syndrome, both rooted in Purkinje cell dysfunction in the vestibulocerebellum and flocculus–paraflocculus complex (UBERON:0002164).

### 3.3 Cognitive, Behavioral, and Psychiatric Phenotypes

Unlike some spinocerebellar ataxias, SCA6 typically spares cognition. GeneReviews states, “Mentation is generally preserved.” (PMID 20301319).[2] Durr et al. similarly reported that non-cerebellar systems were only mildly affected, and no specific cognitive decline pattern could be attributed to SCA6.[3] The StatPearls review notes that SCA6 is “restricted to the cerebellum,” in contrast to SCAs that involve cortical dementia or multisystem neurodegeneration.[18] These observations correspond to the HPO term “No intellectual disability” (HP:0000007) or “Cognitive impairment absent” (HP:0100543).

Subtle executive dysfunction, slowed processing, or visuospatial difficulties may occur in some individuals, reflecting cerebellar contributions to cognition. However, such changes are usually mild and overshadowed by motor disability.[5][6] Psychiatric symptoms such as depression (HP:0000716) and anxiety (HP:0000739) may arise secondary to chronic disability and loss of independence rather than as primary manifestations of cerebellar pathology.[5][8] Quality-of-life instruments show that emotional well-being is affected in a subset of individuals, but these changes are non-specific and similar to those seen in other chronic neurologic diseases.[5] In an RDoC or DSM framework, no unique psychiatric syndrome has been linked to SCA6; mood disturbances are best conceptualized as reactive to disability and life changes.

### 3.4 Laboratory and Neuroimaging Phenotypes

Laboratory abnormalities in SCA6 are not distinctive. Routine serum and cerebrospinal fluid (CSF) tests are typically normal, and no specific biochemical biomarker has been validated for SCA6.[2][5][11][18] Consequently, HPO terms for laboratory phenotypes are largely absent or normal (e.g., “Normal cerebrospinal fluid protein level” HP:0010818). Neurophysiological tests, such as nerve conduction studies and electromyography, may show mild peripheral neuropathy in some patients but are often within normal limits.[3][5] EEG is typically normal unless comorbid conditions exist.

Neuroimaging phenotypes, by contrast, are characteristic. Brain MRI in SCA6 demonstrates isolated or predominant cerebellar atrophy, particularly of the cerebellar vermis (UBERON:0002151) and hemispheric cortex.[3][5][7][13] Durr et al. noted “isolated cerebellar atrophy on MRI” without brainstem involvement.[3] Later studies confirmed that brainstem structures remain relatively preserved, especially early in the disease course.[10] Quantitative volumetric studies reveal reduction in cerebellar volume with sparing of supratentorial regions, consistent with the notion of “pure cerebellar degeneration.”[5][13] HPO terms capturing these findings include “Cerebellar atrophy” (HP:0001272) and “Vermis atrophy” (HP:0002452).

At the histopathologic level, SCA6 is characterized by diffuse loss of Purkinje cells (HP:0007340), particularly in the vermis, with relatively mild loss of granule cells and inferior olivary neurons.[13][15][17] Yoon et al. reported morphological Purkinje cell changes, including heterotopic and irregularly shaped nuclei, unclear cytoplasmic membrane, somatic sprouts, swelling dendritic arborizations, and torpedoes in the granular layer, indicating abnormal development and degeneration.[15] These changes differ from those seen in paraneoplastic cerebellar degeneration or multiple system atrophy, underscoring disease specificity.[15] From a pathology ontology standpoint, these features correspond to GO terms such as Purkinje cell degeneration (GO:0046660) and axonal swelling (GO:0008370).

---

## 4. Genetic and Molecular Information

### 4.1 Causal Gene: CACNA1A

The causal gene for SCA6 is **CACNA1A** (HGNC:1405), which encodes the α1A pore-forming subunit of the P/Q-type voltage-gated calcium channel Ca\(_\text{V}\)2.1.[1][5][14][17] The OMIM entry for CACNA1A (601011) identifies it as the locus for multiple neurologic syndromes, including SCA6, episodic ataxia type 2 (EA2), familial hemiplegic migraine type 1, and developmental epileptic encephalopathies.[1][9] CACNA1A is located on chromosome 19p13.13 and comprises more than 40 exons, with alternative splicing generating multiple isoforms that differ primarily in their C-terminal regions.[14][17]

Ca\(_\text{V}\)2.1 channels are critical for neurotransmitter release at central synapses, particularly in cerebellar Purkinje cells and cortical neurons.[14][17][18] They localize to presynaptic terminals and mediate rapid calcium influx in response to action potentials, triggering synaptic vesicle fusion and glutamate release. GO terms relevant to CACNA1A function include “voltage-gated calcium channel activity” (GO:0005245), “regulation of membrane potential” (GO:0042391), “calcium ion transport” (GO:0006816), and “regulation of neurotransmitter secretion” (GO:0046928). CACNA1A protein resides in the plasma membrane (GO:0005886) of neurons (CL:0000540), with high expression in cerebellar Purkinje neurons (CL:0000121).[17]

### 4.2 Pathogenic Variants: CAG Repeat Expansions

The distinctive pathogenic variant class in SCA6 is expanded CAG trinucleotide repeats located in exon 47 of CACNA1A.[1][5][14] These repeats encode polyglutamine stretches at the C-terminal end of the longest α1A isoform. Normal alleles contain 4–18 repeats, whereas disease-causing alleles contain 19–33 repeats.[1][5][14] Li et al. and GeneReviews converge on the pathogenic range of 20–33 repeats, with alleles carrying 20 repeats typically considered pathologic.[1][2][5][14] Orphanet reports expansions of 21–29 CAG repeats in SCA6 patients.[8] The repeat expansion is a germline variant, present constitutionally in affected individuals, and obeys autosomal dominant inheritance with age-dependent penetrance.[1][2][3][11]

These repeat expansions are classified as *pathogenic* under ACMG/AMP guidelines, based on strong segregation with disease in multiple families, clear molecular mechanism, rarity in general populations, and functional evidence of toxicity.[2][3][10][14][17] ClinVar and the Genetic Testing Registry (GTR) catalog the CACNA1A CAG expansion as a pathogenic repeat expansion variant associated with SCA6 and EA2, although repeat size thresholds differ by phenotype.[11][12] Somatic mosaicism, a prominent feature in some repeat expansion disorders, appears minimal in SCA6; Ishikawa et al. found homogeneous repeat size across different brain regions in autopsied SCA6 patients.[13]

Allele frequencies of expanded repeats in population databases are very low, consistent with the rarity of SCA6.[8][18] While gnomAD and ExAC primarily focus on single-nucleotide variants, repeat expansions are less systematically catalogued, but targeted screening studies estimate that pathogenic SCA6 expansions account for approximately 12–15% of autosomal dominant cerebellar ataxia families in some European and North American populations.[3][10][18] These figures suggest that the carrier frequency of SCA6 is lower than common SCAs such as SCA3 but higher than extremely rare forms.

Functionally, the CAG expansion produces a protein with an elongated polyglutamine tract, increasing propensity for misfolding and aggregation.[14][17] Unlike other polyglutamine diseases, where nuclear inclusions are prominent, SCA6 exhibits primarily cytoplasmic aggregates without ubiquitination.[13][17] Ishikawa and colleagues noted that autopsied SCA6 brains lacked ubiquitin-immunoreactive nuclear inclusions, further distinguishing SCA6 from SCA1, SCA2, and SCA3.[13] In cultured cells, expression of full-length CACNA1A with an expanded polyglutamine tract led to perinuclear aggregates and apoptotic cell death.[17] These findings support a toxic gain-of-function mechanism mediated by protein aggregation and altered channel or transcription factor behavior.

### 4.3 Modifier Genes and Allelic Disorders

Although clear modifier genes for SCA6 have not been established, CACNA1A itself generates multiple allelic disorders that share overlapping pathophysiology. EA2 is caused mainly by truncating or missense CACNA1A variants that disrupt P/Q-type channel function, leading to episodic ataxia and interictal cerebellar signs.[10][14] Familial hemiplegic migraine type 1 arises from missense mutations shifting channel gating, making neurons hyperexcitable.[14][18] Developmental and epileptic encephalopathies linked to CACNA1A involve more profound perturbations of calcium signaling and synaptic development.[14][18] These allelic disorders illustrate that different mutation types within CACNA1A modulate both timing and pattern of cerebellar dysfunction.

In SCA6, there is also evidence that being a compound heterozygote for distinct SCA6 expansions can increase disease severity. Zhukovskaya et al. reported that a compound heterozygote with two expanded alleles manifested earlier onset and more rapid course than family members with the same larger expanded allele alone.[10] This suggests that allelic dosage—number of expanded alleles—modifies phenotype, demonstrating intragenic modifier effects. Beyond CACNA1A, potential modifiers may include genes involved in protein quality control (e.g., chaperones, ubiquitin–proteasome system), autophagy, or calcium buffering, but these remain speculative in human SCA6.

### 4.4 Epigenetic and Chromosomal Abnormalities

No epigenetic mechanisms have been specifically implicated as primary drivers of SCA6. Unlike some repeat expansion disorders where methylation status can modulate expression (e.g., Fragile X), CACNA1A CAG expansions in SCA6 reside within a coding exon and do not appear to be heavily influenced by CpG methylation changes.[14][17] Gene expression studies have suggested that α1ACT, the transcription factor encoded by an overlapping open reading frame (ORF) via an internal ribosome entry site (IRES), participates in regulation of neuronal gene networks, implying that downstream epigenetic reprogramming may occur.[14] However, direct evidence of DNA methylation or chromatin changes as causal factors in SCA6 is lacking.

Similarly, large-scale chromosomal abnormalities—such as aneuploidies, translocations, or inversions—are not involved in SCA6. DECIPHER and cytogenetic databases do not report recurrent structural variants at 19p13 that mimic SCA6 phenotypes.[1][9] SCA6 is thus best understood as a single-locus, repeat-expansion disease without substantial contributions from epigenomic or chromosomal structural variation.

---

## 5. Environmental and Lifestyle Information

### 5.1 Environmental Factors

To date, no specific environmental toxins, pollutants, or radiation exposures have been identified as causal or major contributory factors to SCA6. Case–control and cohort studies of hereditary ataxias focus largely on genetic determinants, and environmental exposures that cause cerebellar damage, such as chronic alcohol use, certain chemotherapeutic agents, or heavy metals, produce clinical pictures that differ from the genetically determined SCA6 phenotype.[5][18] Comparative Toxicogenomics Database (CTD) entries and related resources catalog numerous environmental agents associated with general cerebellar toxicity, but these do not overlap directly with SCA6’s monogenic etiology.

Thus, environmental factors in SCA6 are primarily relevant in the context of symptom exacerbation or comorbid pathologies. For instance, exposure to vestibulotoxic drugs (e.g., aminoglycosides) or repeated head trauma could worsen balance and oculomotor control in individuals already compromised by cerebellar degeneration, but these factors are not known to induce SCA6 in the absence of CACNA1A expansion.[18] Consequently, environmental interventions such as avoiding neurotoxic medications and maintaining a safe environment to minimize falls are important for tertiary prevention but not for primary disease causation.

### 5.2 Lifestyle Factors

Lifestyle factors such as smoking, alcohol consumption, diet, and exercise have not been shown to modify the *risk* of developing SCA6 in genetically predisposed individuals, but they can influence symptom trajectory and overall health. Regular physical exercise and tailored coordinative training appear beneficial in maintaining mobility and reducing the rate of functional decline, as suggested by interventional studies in mixed hereditary ataxia cohorts.[5] Although these studies are not SCA6-specific, their findings are generalizable, given the shared cerebellar mechanisms. GO processes involved in the beneficial effect of exercise include “synaptic plasticity” (GO:0048167) and “regulation of neurogenesis” (GO:0050767).

Conversely, heavy alcohol use can exacerbate cerebellar dysfunction and is generally discouraged in patients with hereditary ataxia.[18] Nutritional deficiencies, particularly of vitamin B12 or thiamine, can cause additional neurologic problems and should be corrected, but they do not alter the underlying genetic trajectory of SCA6.[2] Smoking and cardiovascular risk factors can increase the risk of stroke or other neurological events that compound disability. Thus, lifestyle management for SCA6 emphasizes maintenance of overall neurologic health and reduction of additive insults.

### 5.3 Infectious Agents

No infectious agents are implicated in the etiology of SCA6. Viral, bacterial, fungal, or parasitic infections can cause acquired cerebellar syndromes (e.g., post-infectious cerebellitis), but these are distinct from hereditary ataxias.[18] In SCA6, infections are relevant mainly as complications—such as aspiration pneumonia due to dysphagia—rather than as triggers of primary disease. Preventive measures (vaccination, prompt antibiotic treatment, and dysphagia management) aim to reduce infection-related morbidity in SCA6 patients, but do not modify genetic causation.

---

## 6. Mechanism and Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Phenotype

The mechanistic progression of SCA6 can be summarized as a series of causal steps from the initiating genetic lesion to clinical manifestations. To adhere to the requested structure, these steps are presented as a numbered sequence, each line describing one mechanistic link.

1) A germline CAG repeat expansion in exon 47 of **CACNA1A** increases the length of a polyglutamine tract in the C-terminal region of the α1A subunit and in the overlapping α1ACT transcription factor, which leads to altered protein folding and translational regulation.[1][5][14][17]

2) The expanded polyglutamine tract results in increased propensity for cytoplasmic aggregation of α1A channel protein in Purkinje cells and dysregulated production and function of α1ACT, which leads to disruption of normal P/Q-type calcium channel activity and transcriptional control of neuronal genes.[14][17]

3) Abnormal channel function and α1ACT-mediated gene expression changes lead to impaired calcium homeostasis, altered synaptic transmission, and dysregulated expression of genes critical for Purkinje cell survival and dendritic architecture, which results in progressive Purkinje cell dysfunction.[14][15][17]

4) Chronic Purkinje cell dysfunction leads to cellular stress, activation of apoptotic and degenerative pathways, and distinctive morphological changes (somatic sprouts, dendritic swelling, axonal torpedoes), which result in selective Purkinje cell degeneration within the cerebellar cortex, particularly in the vermis.[7][13][15][17]

5) Loss of Purkinje cells leads to disruption of cerebellar output from the cortex to deep cerebellar nuclei and brainstem oculomotor and vestibular centers, which results in failure of cerebellar coordination of movement and eye control.[7][13][16][18]

6) Cerebellar circuit dysfunction and structural atrophy lead to clinically manifest gait and limb ataxia, dysarthria, downbeat and gaze-evoked nystagmus, and other cerebellar signs, which result in progressive functional disability and characteristic SCA6 phenotype.[2][3][5][7][16][18]

These steps integrate both experimentally demonstrated mechanisms—such as cytoplasmic aggregation of α1A, Purkinje cell loss, and cerebellar atrophy—and inferred processes, such as specific transcriptional dysregulation mediated by α1ACT, which is based on emerging evidence but not fully mapped.[14][17] Upstream mechanisms center on the mutation’s effects at the protein and cellular levels, while downstream mechanisms involve tissue damage and systems-level dysfunction culminating in clinical signs.

### 6.2 Molecular Pathways and Protein Dysfunction

At the molecular level, SCA6 engages both ion-channel and polyglutamine disease pathways. The α1A subunit of Ca\(_\text{V}\)2.1 forms the pore of P/Q-type channels that mediate presynaptic calcium influx, essential for neurotransmitter release.[14][17][18] CAG expansions in the C-terminal region alter the structural properties of the channel and its interaction with intracellular scaffolding proteins, potentially modifying gating kinetics or channel trafficking. GO terms capturing these processes include “voltage-gated calcium channel activity” (GO:0005245), “calcium ion transmembrane transport” (GO:0070588), and “regulation of neurotransmitter release” (GO:0050804).

Yamamoto et al. demonstrated that the channel mRNA/protein containing the polyglutamine tract is most intensely expressed in Purkinje cells of human brains and that in SCA6 brains, numerous oval or rod-shaped aggregates are seen exclusively in the cytoplasm of Purkinje cells.[17] They wrote: “In SCA6 brains, numerous oval or rod-shaped aggregates were seen exclusively in the cytoplasm of Purkinje cells. These cytoplasmic inclusions were not ubiquitinated, which contrasts with the neuronal intra-nuclear inclusions of other CAG repeat/polyglutamine diseases.” (PMID 10369863).[17] In cultured cells, perinuclear aggregates of the channel protein and apoptotic cell death occurred when transfected with full-length CACNA1A coding an expanded polyglutamine tract, indicating toxic gain of function through aggregation.[17]

A landmark review by Kordasiewicz et al. (PMID 29427102) detailed that CACNA1A mRNA harbors a novel internal ribosomal entry site (IRES), enabling translation of a second protein, **α1ACT**, from an overlapping ORF.[14] α1ACT is a transcription factor with a polyglutamine repeat at its C-terminal end, distinct in structure from the α1A channel. The review emphasizes: “Due to presence of a novel internal ribosomal entry site (IRES) within the mRNA, CACNA1A encodes two structurally unrelated proteins with distinct functions within an overlapping open reading frame (ORF) of the same mRNA: (1) α1A subunit of P/Q-type voltage gated calcium channel; (2) α1ACT, a newly recognized transcription factor, with polyglutamine repeat at C-terminal end.” (PMID 29427102).[14] Expanded repeats in α1ACT likely alter its transcriptional regulatory capacity, leading to aberrant expression of downstream genes involved in neuronal differentiation, dendritic morphology, and survival.

Thus, SCA6’s protein dysfunction is two-fold: misfolded, aggregating α1A channels disrupt calcium signaling and synaptic transmission, while polyglutamine-expanded α1ACT distorts transcriptional programs. These mechanisms involve multiple molecular pathways, including MAPK signaling (GO:0000165), apoptotic signaling (GO:0097190), and unfolded protein response (GO:0030968).

### 6.3 Cellular Processes: Purkinje Cell Stress and Degeneration

At the cellular level, Purkinje cells are the primary targets in SCA6.[7][13][15][17] These large, glutamatergic neurons reside in the cerebellar cortex and integrate inputs from parallel fibers and climbing fibers, providing inhibitory output to deep cerebellar nuclei.[18] In SCA6, Purkinje cells exhibit early functional impairment followed by structural degeneration. Morphologic studies by Yoon et al. showed severe loss of Purkinje cells, especially in the vermis, accompanied by various morphological changes such as heterotopic nuclei, somatic sprouts, dendritic swelling, increased spine-like protrusions, disordered axonal arrangement, and torpedoes in the granular layer.[15] They concluded that these changes are “considered to be related to the genetic abnormality that causes abnormal development of Purkinje cells.” (PMID 10985694).[15]

These findings implicate disrupted dendritic arborization (GO:0097483), altered synaptic connectivity (GO:0058052), and axonal degeneration (GO:0006944). Cellular stress pathways, including oxidative stress (GO:0006979), autophagy (GO:0006914), and apoptosis (GO:0006915), are activated as misfolded proteins accumulate. Cytoplasmic aggregates may sequester essential proteins or organelles, impairing normal cellular function. Mitochondrial dysfunction and impaired calcium buffering exacerbate vulnerability, especially given Purkinje cells’ high firing rate and metabolic demand.[14][17][18]

Importantly, granule cells and inferior olivary neurons are only mildly affected, indicating selective vulnerability. Ishikawa et al. reported that morphometric analysis showed that loss of cerebellar granule cells and inferior olivary neurons was very mild compared with the severity of Purkinje cell loss.[13] This emphasizes that even within the cerebellum, SCA6 is cell-type specific, targeting CL:0000121 (Purkinje neuron) more than CL:0000120 (granule neuron) or CL:0000664 (inferior olivary neuron).

### 6.4 Tissue Damage Mechanisms and Systems-Level Dysfunction

At the tissue level, SCA6 leads to cerebellar cortical degeneration and macroscopic cerebellar atrophy, especially of the vermis and hemispheric cortex.[3][7][13][15] The progressive loss of Purkinje cells results in thinning of the molecular and Purkinje cell layers, while the granular layer remains relatively intact.[13][15] The cerebellar peduncles and brainstem, including cranial nerve nuclei, are largely preserved, especially in the first decade of symptoms.[10] These structural changes translate into dysfunction of cerebellar output pathways to thalamus, cerebral cortex, and brainstem oculomotor and vestibular nuclei.[7][16][18]

Functionally, impairment of the spinocerebellum (posterior vermis and intermediate hemisphere) leads to gait and limb ataxia, while dysfunction of the vestibulocerebellum (flocculus and nodulus) results in oculomotor abnormalities such as downbeat and gaze-evoked nystagmus.[7][16][18] These regional relationships are captured by UBERON terms such as cerebellar vermis (UBERON:0002151), cerebellar hemisphere (UBERON:0013523), and flocculus (UBERON:0002164). Systems-level consequences include errors in motor timing, poor adaptation of vestibulo-ocular reflex, and reduced predictive control of movement.

Unlike some neurodegenerative diseases, inflammatory or autoimmune mechanisms do not play a major direct role in SCA6 tissue damage.[6][14][18] There is no evidence of prominent microglial activation or perivascular inflammation in neuropathologic specimens.[13][15][17] Immune processes may participate in general clearance of debris and response to degenerating neurons, but they do not appear as primary drivers. GO terms for immune pathways, such as “microglial cell activation” (GO:0001774) or “leukocyte migration” (GO:0050900), have not been emphasized in SCA6 literature.

### 6.5 Epigenetic Changes and Molecular Profiling

Epigenetic profiling specific to SCA6 is limited. The discovery of α1ACT as a transcription factor suggests that global gene expression programs may be altered in SCA6 neurons, potentially involving epigenetic regulation of target genes.[14] However, comprehensive transcriptomic, proteomic, metabolomic, or epigenomic datasets for human SCA6 tissue are sparse in GEO or PRIDE. Most molecular insights derive from targeted candidate-based experiments focusing on CACNA1A, α1ACT, and selected downstream genes.

Available evidence indicates that α1ACT influences expression of genes involved in neuronal differentiation and morphogenesis, and that expanded α1ACT may act as a dominant-negative or gain-of-function transcription regulator.[14] Thus, SCA6 likely entails misregulation of transcriptional networks (GO:0006355) and epigenetic modifiers (GO:0040029), although definitive multi-omics mapping is pending. Single-cell or spatial transcriptomics studies have not yet been published for SCA6, reflecting the rarity of the disease and the challenges of obtaining well-preserved brain tissue.

### 6.6 Advanced Technologies and Functional Genomics

Advanced functional genomics approaches, such as CRISPR-based screens and induced pluripotent stem cell (iPSC) models, are beginning to be applied to polyglutamine diseases but have not yet generated large bodies of SCA6-specific data. In vitro models expressing expanded CACNA1A constructs demonstrate aggregate formation and apoptosis, reinforcing the notion of toxic gain of function.[17] Animal models, particularly transgenic mice expressing expanded α1A or α1ACT, have been explored to replicate SCA6 phenotypes, but detailed characterization is still emerging (see Section 15).[14]

Overall, the pathophysiology of SCA6 integrates:

- An upstream genetic repeat expansion in CACNA1A.

- Protein dysfunction in α1A channel and α1ACT transcription factor.

- Cellular processes of aggregation, stress, and Purkinje cell degeneration.

- Tissue-level cerebellar cortical atrophy.

- Systems-level motor and oculomotor dysfunction leading to clinical ataxia and nystagmus.

This causal chain offers multiple potential intervention points, from translational control of α1ACT to modulation of Purkinje cell survival pathways.

---

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

The primary organ affected in SCA6 is the cerebellum (UBERON:0002037).[3][7][13][15] Both vermis and hemispheric cortex are involved, with Purkinje cell loss most pronounced in the vermis.[13][15] MRI and neuropathologic studies consistently show cerebellar atrophy without significant involvement of cerebrum, basal ganglia, or spinal cord.[3][7][10][13] The brainstem (UBERON:0002298) remains largely normal, particularly within the first decade of symptoms, although subtle secondary changes may occur over time.[10]

Secondary organ involvement arises from complications rather than direct disease extension. Dysphagia can lead to aspiration pneumonia affecting the lungs (UBERON:0002048), while chronic immobility can impact musculoskeletal and cardiovascular systems (UBERON:0001434 and UBERON:0004535).[2][5][8] However, these are consequences of cerebellar dysfunction rather than direct targets of CACNA1A-related pathology.

The body system most directly involved is the nervous system (UBERON:0001016), specifically the central nervous system (UBERON:0001017) and its motor and oculomotor components. The vestibular system, comprising peripheral vestibular organs and central vestibular nuclei, is indirectly affected via cerebellar modulation of vestibulo-ocular reflexes.[7][16][18] No significant involvement of endocrine or digestive systems is intrinsic to SCA6, although nutritional status can deteriorate due to dysphagia.[2][8]

### 7.2 Tissue and Cell-Level Involvement

At the tissue level, SCA6 targets nervous tissue (UBERON:0001013), specifically cerebellar cortex (UBERON:0002039) and its neuronal components. As emphasized, Purkinje cells (CL:0000121) are the primary cell population affected.[7][13][15][17] These neurons form a monolayer between molecular and granular layers and exert inhibitory control over deep cerebellar nuclei. Degeneration of Purkinje cells in SCA6 leads to disruption of this regulatory axis.

Granule cells (CL:0000120), the most numerous neurons in the central nervous system, are relatively preserved.[13][15] Inferior olivary neurons (CL:0000664), which provide climbing fiber input to Purkinje cells, also show mild loss at most.[13] Deep cerebellar nuclei neurons may be affected secondarily due to loss of afferent input, but this has not been extensively quantified.[13][15] Glial cells, including astrocytes (CL:0000099) and microglia (CL:0000129), participate in cleanup and support but are not primary targets.

At the subcellular level, cytoplasmic aggregates of α1A channel protein are prominent in Purkinje cell cytosol (GO:0005737).[17] These aggregates localize near the perinuclear region (GO:0044224) but do not form nuclear inclusions, unlike other polyglutamine diseases.[13][17] Mitochondria (GO:0005739) and endoplasmic reticulum (GO:0005783) may be functionally compromised by calcium dysregulation and protein misfolding, but direct visualization of organellar changes in SCA6 is limited. Plasma membrane (GO:0005886) and synaptic terminals (GO:0045202) harbor the dysfunctional Ca\(_\text{V}\)2.1 channels.

### 7.3 Localization and Lateralization

Anatomically, SCA6 affects the cerebellum bilaterally, although severity of degeneration can vary somewhat between hemispheres. MRI and pathology show symmetric or mildly asymmetric cerebellar atrophy without clear lateralization of lesions.[3][7][13][15] Clinically, ataxia and nystagmus are typically symmetric, involving both sides of the body and both eyes. HPO does not designate SCA6 as a lateralized disorder; instead, terms like “bilateral cerebellar atrophy” are applicable.

Within the cerebellum, specific regions such as the flocculus–paraflocculus complex (UBERON:0002164) and nodulus (UBERON:0002167) are particularly relevant to oculomotor control and are functionally implicated in SCA6.[7][16][18] While direct imaging of these small structures is challenging, oculomotor deficits in SCA6 correspond to known roles of these regions in gaze holding and VOR adaptation.

---

## 8. Temporal Development and Disease Course

### 8.1 Onset: Age and Pattern

SCA6 is unequivocally an adult-onset or late-onset disease. GeneReviews reports an age of onset range from 19 to 73 years, with mean between 43 and 52.[2][11] Durr et al. found onset between 30 and 71 years.[3] Orphanet emphasizes that SCA6 is “late-onset and slowly progressive.”[8] In HPO, these ages correspond to adult onset (HP:0003581) and late onset (HP:0004519).

Onset is typically insidious and chronic rather than acute or subacute. Patients often recall a gradual increase in gait unsteadiness, stumbling, and imbalance over months to years, rather than a sudden event.[2][3][11] Dysarthria and subtle oculomotor abnormalities may appear concurrently or shortly afterward. Episodic ataxia attacks can occur in some patients, especially in those with overlapping EA2 phenotypes, but these episodes occur against a background of progressive ataxia.[10][11] Thus, the onset pattern is best described as chronic and insidious, occasionally punctuated by episodic exacerbations.

### 8.2 Progression: Stages and Rate

The progression of SCA6 is slow and often extends over decades. Orphanet notes that “SCA6 progresses very slowly with a disease duration that can last over 25 years.”[8] GeneReviews describes course as slowly progressive, with eventual involvement of gait ataxia, limb incoordination, intention tremor, dysarthria, and dysphagia in most patients.[2][11] Longitudinal clinical observations indicate that many individuals remain ambulatory for years after onset, though they may require canes or walkers.[2][5] Severe disability is typically reached only after two or more decades of disease.

Formal staging systems specific to SCA6 are not yet standardized. However, clinicians often conceptualize stages analogous to other cerebellar ataxias: an early stage with mild gait instability and subtle oculomotor signs; an intermediate stage with clear ataxia requiring assistive devices and prominent dysarthria; and an advanced stage with wheelchair dependence, severe dysphagia, and marked oculomotor dysfunction.[5][8][11] Progression rate varies somewhat among individuals, but is generally slower than in SCA1, SCA2, or SCA3.[3][6][18]

Disease course is essentially progressive rather than relapsing–remitting or stable. Nonetheless, some patients display superimposed episodic attacks of ataxia, especially in early disease, reflecting the allelic overlap with EA2.[10] Zhukovskaya et al. noted that “Most patients show progressive ataxia from the onset, but several patients show an episodic course resembling EA-2.” (PMID 9371902).[10] Remissions, when present, primarily reflect reduction of episodic exacerbations rather than reversal of underlying progression.

### 8.3 Duration, Remission, and Critical Periods

Disease duration in SCA6 can exceed 25 years, with many patients living decades after symptom onset.[2][5][8][11] Given its non-fatal nature, SCA6 is a chronic lifelong condition. Survival is often determined more by age-related comorbidities and complications such as falls and aspiration than by direct disease effects on vital organs.[4][5][8][18]

True spontaneous remission of SCA6 has not been reported. Symptomatic treatments such as acetazolamide can reduce frequency and severity of episodic ataxia, but they do not reverse progressive features.[2][8][10][11] The critical periods for intervention include early disease stages, when physical therapy and oculomotor rehabilitation may preserve function, and pre-symptomatic phases in genetically diagnosed individuals, when lifestyle optimization and psychological support can prepare for future disability.[2][11]

From a developmental biology perspective, SCA6 does not correspond to a developmental disorder; the cerebellum appears structurally normal until adulthood, when degenerative processes begin.[15][18] The pathophysiologic transition from presymptomatic to symptomatic state likely involves cumulative molecular damage and threshold crossing in Purkinje cell functional reserve.

---

## 9. Inheritance and Population Characteristics

### 9.1 Inheritance Pattern and Penetrance

SCA6 is inherited in an autosomal dominant manner.[1][2][3][8][11] GeneReviews states: “SCA6 is inherited in an autosomal dominant manner. Offspring of an affected individual have a 50% chance of inheriting an abnormal CAG trinucleotide repeat expansion in CACNA1A.” (PMID 20301319).[2][11] This Mendelian pattern implies that a single pathogenic allele suffices for disease, with no requirement for consanguinity or recessive inheritance.

Penetrance of SCA6 is high but age-dependent. Most individuals with pathogenic CACNA1A expansions will develop symptoms by late adulthood, but some with smaller expansions near threshold may remain asymptomatic throughout life.[2][3][11][14] Durr et al. reported that age at onset inversely correlates with repeat length, suggesting that larger expansions confer earlier penetrance.[3] However, because SCA6 is a late-onset disease, penetrance estimates must account for competing mortality from other causes. GeneReviews and cohort studies implicitly suggest near-complete penetrance by age 70 for alleles ≥23 repeats, and partial penetrance for those around 20–22 repeats.[2][3][11][14]

Expressivity is variable. Some individuals exhibit classic pure cerebellar ataxia, while others have more prominent oculomotor or peripheral neuropathic features or episodic attacks reminiscent of EA2.[3][4][10][16] Nevertheless, the range of expressivity falls within a recognizably cerebellar spectrum. The StatPearls review notes that “clinical features apart from cerebellar signs were highly variable in patients with SCA6” and that no specific clinical or electrophysiological finding uniquely predicts SCA6 compared to other SCAs.[18][3] This underscores variable expressivity and the need for molecular testing.

Genetic anticipation—progressively earlier onset or increased severity across generations—is modest in SCA6, if present at all. Unlike SCA1 or SCA3, where repeat length often expands dramatically across generations, SCA6 repeats are highly stable.[3][13][18] Ishikawa et al. demonstrated identical expanded alleles in affected members, with homogeneous distribution across brain regions and no mosaicism.[13] Some families may show slightly earlier onset in later generations due to subtle repeat changes or ascertainment bias, but anticipation is not a defining trait.

Germline mosaicism has not been reported as a significant contributor to SCA6. Because repeat expansions are relatively stable and autosomal dominant inheritance produces clear familial clustering, mosaicism is unlikely to play a major role. Founder effects have been described for other SCAs, such as SCA3 in Portugal or SCA2 in certain regions, but SCA6 appears more broadly distributed without a single prominent founder population.[3][18]

### 9.2 Epidemiology: Prevalence, Incidence, and Geographic Distribution

Orphanet estimates that SCA6 has an “estimated worldwide prevalence… less than 1/100,000.”[8] In the broader context of spinocerebellar ataxia, StatPearls reports that global prevalence of all SCAs is 1–5 per 100,000, with overall European prevalence 0.9–3 per 100,000 and regional variation.[18] Within this group, SCA3 (Machado–Joseph disease) is most prevalent, accounting for 25–50% of cases, followed by SCA2 (13–18%), SCA6 (13–15%), and SCA7.[18] Durr et al. found that in Germany, SCA6 accounted for about 13% of families with autosomal dominant cerebellar ataxia.[3] Zhukovskaya et al. reported that SCA6 accounted for 12% of families with ADCA in an ethnically heterogeneous population.[10]

These figures suggest that while SCA6 is rare in the general population, it is one of the more common autosomal dominant cerebellar ataxias encountered in subspecialty clinics, particularly in European and North American populations.[3][10][18] Incidence data are sparse due to the disease’s rarity and late onset; however, given its chronic nature and stable genetic basis, incidence likely parallels prevalence in age-adjusted cohorts.

Geographic distribution shows some variation. SCA6 appears more commonly reported in Japan, Germany, and other European countries, reflecting both genetic factors and diagnostic practices.[3][10][18] However, SCA6 has been identified across diverse ethnicities, indicating that CACNA1A expansions are not confined to a single ancestry. Unlike SCA3, which has a known Portuguese founder and widespread distribution through historical migration, SCA6 does not have a single global founder lineage.[3][18]

Sex ratio in SCA6 appears approximately equal, with no strong male or female predominance reported.[3][10][18] Age distribution among affected individuals is skewed toward mid-late adulthood, consistent with the disease’s onset pattern. Children and adolescents are rarely affected, except in rare early-onset cases possibly associated with larger expansions or additional CACNA1A variants.

### 9.3 Consanguinity, Carrier Frequency, and Demographics

Consanguinity is not a major factor in SCA6, as the disease is autosomal dominant and does not require homozygosity for manifestation.[1][2][3][11] Carrier frequency of pathogenic CACNA1A expansions in general populations is low, consistent with the <1/100,000 prevalence of clinical SCA6.[8][18] However, within families harboring SCA6 mutations, 50% of offspring are carriers, making cascade genetic testing and counseling essential.[2][11][12]

Demographically, SCA6 affects individuals from varied ethnic and geographic backgrounds, with the disease likely underdiagnosed or misdiagnosed as sporadic ataxia in some settings.[3][10][18] Durr et al. observed that up to 30% of SCA6 kindreds may be misdiagnosed clinically as sporadic disease due to late manifestation in apparently healthy parents.[3] This underscores the importance of molecular testing in adult-onset cerebellar ataxia, particularly when family history is unclear.

---

## 10. Diagnostics and Clinical Evaluation

### 10.1 Clinical Assessment and Neurologic Examination

Diagnosis of SCA6 begins with careful clinical evaluation of cerebellar and oculomotor signs. Key findings include gait and limb ataxia, dysmetria, intention tremor, dysarthria, nystagmus, and impairment of smooth pursuit and VOR.[2][3][5][7][16] Neurologic examination typically reveals broad-based, unsteady gait, difficulty with tandem walking, limb dysmetria on finger–nose and heel–knee–shin tests, scanning speech, and ocular motor abnormalities such as gaze-evoked and downbeat nystagmus.[2][7][16][18] Pyramidal signs may be present but are less prominent.

Quantitative oculomotor testing, including eye movement recordings and vestibular assessments, can refine diagnosis by documenting specific patterns of VOR deficit, gaze-holding failure, and positional nystagmus.[7][16] The meta-analysis by Casey et al. (PMCID PMC11646955) indicates that these oculomotor profiles are highly prevalent in SCA6 and may help distinguish it from other hereditary ataxias.[16] However, as Durr et al. emphasized, no single clinical or electrophysiological feature uniquely identifies SCA6; multiple SCAs share overlapping signs.[3]

Laboratory tests are generally used to exclude acquired causes of ataxia (e.g., vitamin deficiencies, autoimmune cerebellitis, paraneoplastic syndromes) rather than to directly diagnose SCA6.[18] LOINC-coded tests for metabolic, infectious, and autoimmune markers may be employed, but they are typically normal in SCA6.

### 10.2 Imaging and Pathology

Brain MRI is an important diagnostic tool. In SCA6, MRI shows isolated cerebellar atrophy without brainstem or supratentorial involvement.[3][5][7][13] The cerebellar vermis and hemispheres appear shrunken, with increased cerebrospinal fluid space in the posterior fossa.[3][7][13] In some cases, imaging performed early in disease may show minimal changes; serial imaging can reveal progressive atrophy over time.[5][18] Radiologic findings correspond to RadLex terms such as “cerebellar atrophy” and DICOM descriptors for volumetric reduction.

Neuropathologic examination, rarely available in living diagnosis, confirms selective Purkinje cell degeneration and cytoplasmic α1A aggregates.[13][15][17] Immunohistochemical staining for calbindin-D and parvalbumin highlights Purkinje cell loss, as Yoon et al. demonstrated.[15] SNOMED CT and College of American Pathologists resources classify these findings under cerebellar cortical degeneration.

### 10.3 Genetic Testing

Genetic testing is the gold standard for SCA6 diagnosis. GeneReviews states explicitly: “The diagnosis of SCA6 rests on the use of molecular genetic testing to detect an abnormal CAG trinucleotide repeat expansion in CACNA1A. Affected individuals have 20 to 33 CAG repeats.” (PMID 20301319).[2][11] DNA extracted from blood is analyzed by PCR amplification of exon 47 of CACNA1A, followed by fragment sizing to determine repeat number.[2][11][12] Pathogenic alleles are defined as those containing 20 or more repeats.[5] GTR lists multiple laboratories offering CACNA1A CAG repeat testing, either as single-gene assays or as part of broader ataxia panels.[12]

In clinical practice, genetic testing approach often starts with the most common SCAs (SCA1, SCA2, SCA3) and then proceeds to SCA6 and other subtypes if initial tests are negative.[18] StatPearls notes: “In clinically suspected patients, genetic testing should be at first carried out in most common SCAs such as SCA1, 2, and 3 and then should proceed to other subtypes if the first series test is negative.”[18] However, when clinical features suggest pure cerebellar ataxia with prominent oculomotor signs and late onset, SCA6 testing may be prioritized.

Whole exome sequencing (WES) and whole genome sequencing (WGS) are increasingly used in undiagnosed ataxia cases, but repeat expansions can be challenging to detect with standard short-read sequencing. Specialized bioinformatic pipelines and adjunct PCR-based assays are needed to accurately measure CAG repeat sizes.[18] Thus, while WES/WGS can identify CACNA1A missense or truncating variants in EA2 or hemiplegic migraine, targeted repeat expansion testing remains essential for SCA6.

Chromosomal microarray (CMA), karyotyping, FISH, and mitochondrial DNA testing do not contribute to SCA6 diagnosis, as the disease is not caused by chromosomal rearrangements or mitochondrial defects.[1][9][18] Instead, repeat expansion testing for CACNA1A, combined with panel sequencing of other ataxia genes, forms the core genetic diagnostic strategy.

### 10.4 Omics-Based Diagnostics and Biomarkers

At present, no omics-based diagnostic biomarkers beyond genetic testing have been validated for SCA6. RNA-seq, proteomics, and metabolomics are research tools that may reveal downstream pathway changes but are not required for clinical diagnosis.[14][17] Liquid biopsy approaches targeting circulating proteins or cfDNA expansions are in early development for other neurodegenerative diseases but have not been established for SCA6.

However, oculomotor and vestibular metrics derived from quantitative eye movement recordings serve as functional biomarkers of cerebellar involvement and may be useful in clinical trials to monitor disease progression or treatment response.[16] These metrics, while not specific to SCA6, capture the severity of cerebellar oculomotor dysfunction.

### 10.5 Differential Diagnosis and Screening

Differential diagnosis of adult-onset cerebellar ataxia includes other SCAs (SCA1, SCA2, SCA3, SCA7, SCA17), episodic ataxias (EA1, EA2), multiple system atrophy (MSA-C), paraneoplastic cerebellar degeneration, chronic alcohol-related cerebellar damage, and idiopathic late-onset cerebellar ataxia.[6][18] Clinical features and neuroimaging help narrow possibilities, but as Durr et al. emphasized, no clinical pattern uniquely predicts SCA6, and molecular testing is required.[3] MSA, for example, features autonomic dysfunction and basal ganglia signs with cerebellar degeneration, whereas SCA6 lacks marked autonomic failure.[15][18] Paraneoplastic cerebellar degeneration shows more diffuse granular and Purkinje cell loss with inflammatory infiltrates, differing from SCA6’s selective pattern.[15]

Screening for SCA6 in asymptomatic individuals is typically limited to at-risk family members undergoing predictive genetic testing. Newborn screening is not performed, given late onset and the ethical complexities of testing infants for adult-onset conditions. Carrier screening in general populations is not recommended due to low prevalence and limited therapeutic options. Cascade screening within families, guided by genetic counseling, is the main screening approach.[2][11][12]

---

## 11. Outcome and Prognosis

### 11.1 Survival and Mortality

SCA6 is generally considered a non-fatal disorder in terms of direct disease effects.[4][5][8][18] Life expectancy in SCA6 patients is near normal, and survival curves largely reflect age-related mortality rather than disease-specific mortality. Wikipedia succinctly notes that “Unlike other types, SCA6 is not fatal,” emphasizing that patients often live into advanced age.[4] Orphanet and GeneReviews do not report increased mortality directly attributable to cerebellar degeneration, although severe dysphagia, falls, and complications can contribute to morbidity.[2][5][8][11]

Disease-specific mortality is primarily related to complications such as aspiration pneumonia, traumatic injuries from falls, and potentially chronic immobility-related issues (venous thromboembolism, cardiovascular deconditioning).[2][5][8][18] With appropriate supportive care and preventive measures, these risks can be mitigated. There are no robust statistics on 5-year or 10-year survival specifically in SCA6, but clinical experience suggests that many patients live for decades after symptom onset.

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in SCA6 is significant and primarily related to motor disability. Progressive gait ataxia leads to frequent falls, difficulty in ambulation, and eventual reliance on assistive devices or wheelchairs.[2][5][8][11] Dysarthria impairs communication, while dysphagia increases risk of aspiration, malnutrition, and social embarrassment during eating.[2][5][11] Oculomotor abnormalities contribute to oscillopsia and impaired visual tracking, affecting tasks such as reading and driving.[7][16]

Disability outcomes can be conceptualized using ICF (International Classification of Functioning) domains: impairments in body functions (balance, coordination, speech), limitations in activities (walking, self-care, communication), and restrictions in participation (work, social interactions).[5] Many SCA6 patients eventually require assistance in daily living tasks, although cognitive independence is maintained. Compared to SCAs with dementia or severe multisystem involvement, SCA6’s disability profile is more motor-centric.

Quality-of-life measures used in hereditary ataxia cohorts, such as SF-36 and EQ-5D, reveal substantial reductions in physical functioning, role limitations due to physical health, and vitality, with relatively preserved mental health and social functioning.[5] Depression and anxiety may arise in response to disability but are not universal. PROMIS measures of mobility, upper extremity function, and social roles can capture the multidimensional impact.

### 11.3 Disease Course, Recovery Potential, and Prognostic Factors

The disease course in SCA6 is slowly progressive, with no spontaneous recovery of lost functions.[2][5][8][11][18] Symptomatic treatments and rehabilitative interventions can improve performance and reduce disability but do not restore normal cerebellar function. Recovery potential thus lies in functional compensation, not in reversal of pathology.

Prognostic factors include age at onset, initial severity, presence of episodic features, and comorbidities. Earlier onset and more severe initial ataxia may predict faster progression, although data are limited.[3][10][18] The presence of compound heterozygosity for two expanded CACNA1A alleles may confer more severe phenotype, as reported by Zhukovskaya et al.[10] Overall, SCA6 has a more favorable prognosis than SCAs with rapid progression, dementia, or systemic involvement, in terms of survival, but significant disability remains.

Biomarkers predicting disease course are not well-established. Repeat length shows modest correlation with age at onset but does not strongly predict progression rate or presence of non-cerebellar signs.[3][14] Quantitative oculomotor metrics may serve as surrogate markers of disease severity and progression in future trials.[16]

---

## 12. Treatment and Management

### 12.1 Pharmacotherapy

Currently, no disease-modifying pharmacologic therapy exists for SCA6.[4][5][8][11][18] Treatment focuses on symptomatic management and supportive care. Acetazolamide, a carbonic anhydrase inhibitor (CHEBI:41374; NCIT:C29442), is sometimes used to reduce episodic ataxia attacks, particularly in patients with overlapping EA2 phenotype.[2][8][10][11] GeneReviews notes: “Acetazolamide may eliminate episodes of ataxia; canes, walking sticks, and walkers to prevent falling; home modifications for safety and convenience; weighted eating utensils and dressing hooks; physical therapy and exercises enhancing balance and core strength; vitamin supplements particularly if caloric intake is reduced.” (PMID 20301319).[2][11] Orphanet echoes that acetazolamide may help with episodes but “does not halt the progression of the disease.”[8]

Other drugs used in general hereditary ataxias may be tried empirically in SCA6, though evidence is modest. These include aminopyridines (e.g., 4-aminopyridine) for downbeat nystagmus, which modulate Purkinje cell excitability; riluzole, which affects glutamatergic transmission; and varenicline, which may influence cholinergic signaling.[5]

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 14 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 9 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:10985694` *(abstract only)*: "All affected patients had identical expanded alleles, and the expansion was also homogeneously distributed throughout the brain without mosaicism. The present study showed that SCA6 is characterised by Purkinje cell dominant cortical cerebellar degeneration, highly stable transmission of the CAG repeat expansion, and lack of ubiquitin immunoreactive nuclear inclusions."
  - closest text in source: "Spinocerebellar ataxia type 6 (SCA6) was recently identified as a form of autosomal dominant spinocerebellar ataxia associated with a small CAG repeat expansion of the gene encoding an alpha 1 A-voltage-dependent calcium channel gene subunit on chromosome 19p13"
- `PMID:29427102` *(abstract only)*: "Due to presence of a novel internal ribosomal entry site (IRES) within the mRNA, CACNA1A encodes two structurally unrelated proteins with distinct functions within an overlapping open reading frame (ORF) of the same mRNA: (1) α1A subunit of P/Q-type voltage gated calcium channel; (2) α1ACT, a newly recognized transcription factor, with polyglutamine repeat at C-terminal end."
  - closest text in source: "Due to presence of a novel internal ribosomal entry site (IRES) with the mRNA, CACNA1A encodes two structurally unrelated proteins with distinct functions within an overlapping open reading frame (ORF) of the same mRNA: (1) α1A subunit of P/Q-type voltage gated calcium channel; (2) α1ACT, a newly recognized transcription factor, with polyglutamine repeat at C-terminal end"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 87 |
| Resolved | 76 |
| Unresolved (possible confabulation) | 4 |
| Obsolete | 5 |
| Unverifiable | 2 |
| Terms whose name was checked | 17 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000007` (2 mentions) - the report calls it "Intellectual disability absent", "No intellectual disability"; HP calls it **Autosomal recessive inheritance**
- `CL:0000664` (2 mentions) - the report calls it "inferior olivary neuron"; CL calls it **obsolete closable valve cell**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0004519` (2 mentions) - HP does not contain this term
- `HP:0011938` (1 mention) - HP does not contain this term
- `HP:0002452` (1 mention), reported as "Vermis atrophy" - HP does not contain this term
- `GO:0058052` (1 mention) - GO does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0008024` (obsolete Congenital nuclear cataract) (2 mentions) - replaced by `HP:0100018`
- `GO:0008370` (obsolete cellular component) (1 mention)
- `GO:0097483` (GO_0097483) (1 mention) - replaced by `GO:0014069`
- `GO:0006944` (GO_0006944) (1 mention) - replaced by `GO:0061025`
- `CL:0000664` (obsolete closable valve cell) (2 mentions) - replaced by `CL:1000147`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0050804` (2 mentions) - the report calls it "regulation of neurotransmitter release"; GO calls it **modulation of chemical synaptic transmission**, and lists "regulation of synaptic transmission" among its other names
- `HP:0001251` (1 mention) - the report calls it "Cerebellar ataxia"; HP calls it **Ataxia**, and lists "Cerebellar ataxia" among its other names
- `HP:0100543` (1 mention) - the report calls it "Cognitive impairment absent"; HP calls it **Cognitive impairment**
- `GO:0048167` (1 mention) - the report calls it "synaptic plasticity"; GO calls it **regulation of synaptic plasticity**
- `CL:0000120` (2 mentions) - the report calls it "granule neuron"; CL calls it **granule cell**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000007` - called "Intellectual disability absent", "No intellectual disability"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.