---
provider: antigravity
model: gemini-4-carbon-medium
cached: false
start_time: '2026-11-19T17:02:07.629375'
end_time: '2026-11-19T17:17:07.409831'
duration_seconds: 899.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Multiple Mitochondrial Dysfunctions Syndrome 10
  mondo_id: MONDO:0975806
  category: Mendelian
  causal_genes: CIAO1
  omim_id: OMIM:620960
  synonyms: not recorded
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agy_executable: agy
    skip_permissions: false
    disable_slash_commands: true
    add_dirs: []
    timeout: 1800
    health_probe_timeout: 30
    min_report_chars: 200
    extra_args: []
run_metadata:
  model: gemini-4-carbon-medium
  status: SUCCESS
  num_turns: 1
  duration_seconds: 891.180081845
  conversation_id: 4ef3c9bb-1711-43bf-8e9c-0758de9ddc06
  usage:
    input_tokens: 97319
    output_tokens: 26305
    thinking_tokens: 4501
    cache_read_tokens: 284372
    total_tokens: 123624
  tool_calls: 48
  retrieval_calls: 48
citation_count: 13
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 6
  validator_version: 0.8.0
term_validation:
  total_terms: 81
  verified: 67
  not_found: 0
  obsolete: 1
  unverifiable: 13
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 5
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0975806
    reported_labels:
    - Mondo Disease Ontology
    ontology_label: multiple mitochondrial dysfunctions syndrome 10
  - term_id: NCBITaxon:6239
    reported_labels:
    - Nematode
    ontology_label: Caenorhabditis elegans
  obsolete_terms:
  - term_id: GO:0006461
    ontology_label: GO_0006461
    replaced_by: GO:0065003
  unresolvable_prefixes:
  - OMIM
  - UniProt
  - ORPHA
  - Gene
  - LOINC
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Multiple Mitochondrial Dysfunctions Syndrome 10
- **MONDO ID:** MONDO:0975806 (if available)
- **Causal gene(s):** CIAO1
- **OMIM:** OMIM:620960
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Multiple Mitochondrial Dysfunctions Syndrome 10** covering all of the
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

# Comprehensive Disease Characteristics Report: Multiple Mitochondrial Dysfunctions Syndrome 10 (MMDS10)

> **Scope and Interpretation Note:** This report characterizes **Multiple Mitochondrial Dysfunctions Syndrome 10** (**MONDO:0975806**; **OMIM:620960**), an ultra-rare autosomal recessive disorder caused by biallelic hypomorphic/loss-of-function variants in the ***CIAO1*** gene (**HGNC:14280**). Because OMIM `#620960` was established following the 2024 clinical and mechanistic delineation of *CIAO1* deficiency by Maio et al. (PMID: 38950322) and a concurrent 2024 report by van Karnebeek et al. (PMID: 38411040) identified biallelic *CIAO1* variants—including the shared recurrent `c.193C>T` (p.Arg65Trp) allele—in a more severe neurodegenerative and secondary dihydropyrimidine dehydrogenase (DPD)-deficient presentation, both primary cohorts (and 2025–2026 functional follow-up data, PMID: 41131702) are synthesized here while explicitly distinguishing the canonical MMDS10 neuromuscular phenotype from the broader allelic *CIAO1* deficiency spectrum.

---

## 1. Disease Information

### Concise Overview
**Multiple Mitochondrial Dysfunctions Syndrome 10 (MMDS10)** (**MONDO:0975806**; **OMIM:620960**) is an autosomal recessive multisystem neurometabolic and neuromuscular disorder caused by biallelic pathogenic variants in ***CIAO1*** (*Cytosolic Iron-Sulfur Assembly Component 1*; **HGNC:14280**, **OMIM:604333**), located on chromosome 2q11.2 ([OMIM:620960](https://omim.org/entry/620960); [UniProt:O76071](https://www.uniprot.org/uniprotkb/O76071/entry); PMID: 38950322). Unlike classical Multiple Mitochondrial Dysfunctions Syndromes (MMDS1–MMDS9) that disrupt intramitochondrial iron-sulfur (`[Fe-S]`) cluster synthesis directly, MMDS10 impairs a core WD40-repeat scaffold subunit of the **cytosolic iron-sulfur protein assembly (CIA) targeting complex** (`CIAO1–CIAO2B–MMS19` and `CIAO1–CIAO2A`), compromising the maturation of extramitochondrial (cytoplasmic and nuclear) `[Fe-S]` enzymes required for DNA replication, DNA repair, iron homeostasis, and pyrimidine catabolism, accompanied by secondary mitochondrial morphological enlargement and lipoylation defects (PMID: 38950322; PMID: 38411040).

Clinically, the canonical MMDS10 presentation (PMID: 38950322) features early-childhood to adolescent-onset slowly progressive proximal and axial muscle weakness, fluctuating serum creatine kinase (CK) elevation, restrictive respiratory insufficiency, central nervous system (CNS) manifestations (learning difficulties, neurobehavioral comorbidities, and deep brain nuclei iron deposition), mild normocytic-to-macrocytic anemia, and gastrointestinal dysmotility. A severe allelic presentation of biallelic *CIAO1* deficiency (PMID: 38411040) manifests with congenital microcephaly, simplified cortical gyration, progressive neurodegeneration, secondary dihydropyrimidine dehydrogenase (DPD) deficiency (elevated body-fluid uracil and thymine), recurrent severe infections, and premature death in infancy or late adolescence.

### Key Identifiers
| Resource / Ontology | Identifier | Label / Mapping Status | Reference |
| :--- | :--- | :--- | :--- |
| **Mondo Disease Ontology** | `MONDO:0975806` | Multiple mitochondrial dysfunctions syndrome 10 | Mondo / Genomics England |
| **OMIM (Phenotype)** | `OMIM:620960` | Multiple mitochondrial dysfunctions syndrome 10 (MMDS10) | [omim.org/entry/620960](https://omim.org/entry/620960) |
| **OMIM (Causal Gene)** | `OMIM:604333` | Cytosolic iron-sulfur assembly component 1 (*CIAO1*) | [omim.org/entry/604333](https://omim.org/entry/604333) |
| **NCBI MedGen** | `C5975413` | Multiple mitochondrial dysfunctions syndrome 10 | [ncbi.nlm.nih.gov/medgen/1874943](https://www.ncbi.nlm.nih.gov/medgen/1874943) |
| **Orphanet (ORPHA)** | Not yet assigned a standalone subtype code | Grouped under broader *Multiple mitochondrial dysfunctions syndrome* (`ORPHA:314616`) | Orphanet |
| **ICD-10** | `G71.3` / `E88.8` | *Mitochondrial myopathy, not elsewhere classified* / *Other specified metabolic disorders* (broad clinical coding; no MMDS10-specific code) | ICD-10 |
| **ICD-11** | `5C53.2Y` | *Other specified inborn errors of mitochondrial metabolism* (broad category; no MMDS10-specific code) | ICD-11 |
| **MeSH** | `D028361` / `D008659` | *Mitochondrial Diseases* / *Metabolic Diseases* (no dedicated MeSH descriptor assigned yet) | NCBI MeSH |

### Synonyms and Alternative Names
- **MMDS10** ([OMIM:620960](https://omim.org/entry/620960); [UniProt:O76071](https://www.uniprot.org/uniprotkb/O76071/entry))
- **Multiple mitochondrial dysfunctions syndrome type 10** (`MONDO:0975806`)
- **CIAO1-related neuromuscular disorder** / **CIAO1 deficiency** (descriptive clinical terms used in primary discovery cohorts: PMID: 38950322; PMID: 38411040)

### Nature of Source Evidence
Current disease knowledge derives almost entirely from **individual patient-level deep phenotyping and multi-center research cohorts** (6 genetically confirmed probands across two 2024 discovery studies: 4 unrelated individuals P1–P4 in Maio et al., PMID: 38950322, and 2 compound heterozygous individuals in van Karnebeek et al., PMID: 38411040), supplemented by **patient-derived cellular assays, structural biology, and model organism studies**, and curated into aggregated disease-level entries (`OMIM:620960`, `MONDO:0975806`, `UniProt:O76071`). Large-scale electronic health record (EHR) or epidemiological registry aggregations do not yet exist because the disorder was first delineated in 2024.

---

## 2. Etiology

### Disease Causal Factors
- **Primary Genetic Cause (`[Human clinical]`, `[In vitro / patient-derived cellular]`):** MMDS10 is a monogenic Mendelian disorder caused by germline **biallelic (homozygous or compound heterozygous) hypomorphic / partial loss-of-function variants in *CIAO1*** (`HGNC:14280`, `NCBI Gene:9391`) on chromosome 2q11.2 (PMID: 38950322; PMID: 38411040). Because *CIAO1* is an essential housekeeping gene whose complete null state is cell-lethal and embryonic-lethal in model organisms, all viable human patients harbor at least one missense allele retaining partial residual activity (PMID: 38950322; PMID: 38411040; PMID: 41131702).
  > *"Our study revealed that patients with biallelic loss of function in CIAO1 developed proximal and axial muscle weakness, fluctuating creatine kinase elevation, and respiratory insufficiency."* — Maio et al., *J Clin Invest*, 2024 (PMID: 38950322) `[Human clinical]`
- **Primary Mechanistic Cause (`[In vitro / patient-derived cellular]`):** Destabilization of the CIAO1 β-propeller protein and/or disruption of its binding interfaces prevents formation of functional CIA targeting complexes (`CIAO1–CIAO2B–MMS19` and `CIAO1–CIAO2A`), blocking `[4Fe-4S]` (`CHEBI:49883`) cofactor delivery to nucleocytoplasmic apoproteins and triggering downstream defects in genome maintenance, cellular iron regulation, pyrimidine catabolism, and mitochondrial homeostasis (PMID: 38950322; PMID: 38411040).

### Risk Factors
- **Genetic Risk Factors (`[Human clinical]`, `[Population database / computational]`):**
  - **Parental carrier status / family history:** Autosomal recessive inheritance confers a 25% recurrence risk per pregnancy when both parents are heterozygous carriers of pathogenic or hypomorphic *CIAO1* alleles (PMID: 38950322; PMID: 38411040).
  - **Population carrier variant `c.193C>T` (p.Arg65Trp; `rs11544859`):** Present at a minor allele frequency of approximately `0.00101` (~0.10% in gnomAD v2; ~0.16% in gnomAD v4, predominantly in non-Finnish Europeans) with **zero homozygotes** observed in population controls; acts as a recurrent trans-acting hypomorphic disease allele when paired with a more severe missense or deletion variant (PMID: 38950322; PMID: 38411040; PMID: 41131702).
  - **Susceptibility loci / GWAS:** No common polygenic susceptibility loci for MMDS10 have been reported in the GWAS Catalog or PheGenI.
- **Environmental and Pharmacological Risk Factors (`[Human clinical]`, `[Model organism]`):**
  - **Fluoropyrimidine exposure (`5-fluorouracil`, `CHEBI:46345`, `NCIT:C505`):** Biallelic hypomorphic *CIAO1* variants cause secondary deficiency of the `[4Fe-4S]`-dependent enzyme dihydropyrimidine dehydrogenase (DPD), creating extreme pharmacogenetic vulnerability to severe or lethal 5-fluorouracil (5-FU) toxicity (PMID: 38411040; PMID: 41131702).
  - **Intercurrent respiratory infections:** Viral, bacterial, and fungal respiratory tract infections precipitated acute decompensation and fatal respiratory/multi-organ failure in severe *CIAO1*-deficient patients (PMID: 38411040).
  - **Other environmental exposures:** No causal toxin, occupational, smoking, or dietary exposures have been linked to disease onset in CTD, EPA, CDC, or WHO databases.

### Protective Factors
- **Genetic Protective Factors:** No human protective alleles or genetic suppressors have been reported in PubMed or gnomAD. Experimentally, lentiviral re-expression of wild-type *CIAO1* completely rescues cellular phenotypes in patient-derived cells (`[In vitro / patient-derived cellular]`, PMID: 38950322).
- **Environmental Protective Factors:** No dietary or lifestyle protective factors are known to prevent disease onset in biallelic individuals. Avoidance of fluoropyrimidine chemotherapeutic agents (`CHEBI:46345`) prevents drug-induced toxicity in individuals with *CIAO1*-mediated DPD deficiency (PMID: 38411040; PMID: 41131702).

### Gene–Environment Interactions
1. ***CIAO1* × 5-Fluorouracil (`CHEBI:46345`) Pharmacogenetic Interaction (`[Human clinical]`, `[Model organism]`):** Hypomorphic *CIAO1* variants (`p.Arg65Trp`, `p.Trp184Cys`, `p.His193Tyr`) impair `[Fe-S]` cluster insertion into DPD (`DPYD`), abolishing or severely reducing pyrimidine catabolism. In CRISPR-edited *Caenorhabditis elegans* (`ciao-1` knock-in strains), exposure to environmental 5-FU causes severe embryonic lethality and reduced hatch rates compared with wild-type animals (PMID: 41131702; [doi:10.1093/genetics/iyaf228](https://doi.org/10.1093/genetics/iyaf228)).
2. ***CIAO1* × Infectious Pathogens (`[Human clinical]`):** Defective maturation of cytosolic/nuclear `[Fe-S]` proteins required for innate/antiviral host defense and DNA replication interacts with common respiratory pathogens (e.g., bronchiolitis viruses, bacterial/fungal superinfections) to produce life-threatening infections and septic decompensation (PMID: 38411040).

---

## 3. Phenotypes

### Phenotype Catalog and Characteristics
Phenotypic data below integrate the canonical neuromuscular MMDS10 cohort (*n* = 4 probands, P1–P4; Maio et al., 2024, PMID: 38950322) and the severe neurodegenerative/DPD-deficient *CIAO1* cohort (*n* = 2 probands; van Karnebeek et al., 2024, PMID: 38411040). Because total reported cases remain small (*N* = 6), frequencies are stated per published cohort rather than extrapolated as population percentages.

| Phenotype | Type | Suggested HPO Term | Onset | Severity | Progression | Cohort Frequency & Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Proximal muscle weakness** | Clinical sign / symptom | `HP:0003701` (Proximal muscle weakness); `HP:0001324` (Muscle weakness) | Early childhood to adolescence | Moderate to severe | Slowly progressive | Core feature in 4/4 MMDS10 probands (PMID: 38950322) and late-teen progressive weakness causing wheelchair dependency in 1/2 probands in PMID: 38411040 `[Human clinical]` |
| **Axial muscle weakness** | Clinical sign / symptom | `HP:0003327` (Axial muscle weakness) | Early childhood to adolescence | Moderate to severe | Slowly progressive | Core feature in MMDS10 cohort (PMID: 38950322) `[Human clinical]` |
| **Generalized hypotonia** | Clinical sign | `HP:0001290` (Generalized hypotonia) | Neonatal to childhood | Mild to severe | Persistent / progressive | Reported across MMDS10 / *CIAO1* clinical spectrum (PMID: 38950322; MedGen `C5975413`) `[Human clinical]` |
| **Respiratory insufficiency** | Clinical sign / functional | `HP:0002094` (Dyspnea / Respiratory insufficiency) | Neonatal (severe) or childhood to adulthood (myopathic) | Moderate to lethal | Progressive (often requiring BiPAP / noninvasive ventilation) | Core feature in MMDS10 cohort (PMID: 38950322) and both probands in PMID: 38411040 (neonatal respiratory distress in Patient 1; teen respiratory insufficiency in Patient 2) `[Human clinical]` |
| **Elevated serum creatine kinase (CK)** | Laboratory abnormality | `HP:0003236` (Elevated circulating creatine kinase concentration) | Childhood to adolescence | Mild to moderate | **Fluctuating** | Characteristic hallmark of MMDS10 cohort (PMID: 38950322; LOINC `2157-6`) `[Human clinical]` |
| **Learning difficulties / Intellectual disability & Global developmental delay** | Cognitive / neurodevelopmental | `HP:0001249` (Intellectual disability); `HP:0001256` (Mild intellectual disability / developmental delay) | Infancy to childhood | Mild (MMDS10) to profound (neurodegenerative form) | Stable (mild) to progressive regression (severe) | Present in MMDS10 probands (PMID: 38950322) and severe progressive developmental impairment in 2/2 probands in PMID: 38411040 `[Human clinical]` |
| **Neurobehavioral comorbidities (including autism spectrum features & hyperkinetic movements)** | Behavioral / neurological | `HP:0000738` (Behavioral abnormality) | Childhood | Mild to moderate | Chronic | Neurobehavioral comorbidities noted in MMDS10 cohort (PMID: 38950322); autism spectrum disorder and hyperkinetic movement disorder in Patient 2 of PMID: 38411040 `[Human clinical]` |
| **Deep brain nuclei iron accumulation** | Neuroimaging / physical sign | `HP:0002454` (basal ganglia / globus pallidus iron anomaly context; no active generic brain iron HPO ID verified after `HP:0002491` obsolescence) | Childhood to adulthood | Mild to moderate | Progressive | Iron deposition in deep brain nuclei (globus pallidus, substantia nigra) on MRI in MMDS10 cohort (PMID: 38950322) `[Human clinical]` |
| **Microcephaly and congenital brain malformations (simplified gyral pattern)** | Physical / neuroimaging | `HP:0000252` (Microcephaly); `HP:0009878` (Simplified gyral pattern) | Prenatal / congenital | Severe | Progressive neurodegenerative | Present in severe allelic presentation (PMID: 38411040, notably Patient 1 with IUGR, microcephaly, and simplified gyral pattern) `[Human clinical]` |
| **Normocytic to macrocytic anemia & altered iron indices** | Laboratory abnormality | `HP:0001897` (Normocytic anemia); `HP:0001972` (Macrocytic anemia); `HP:0012463` (Elevated transferrin saturation) | Childhood to adulthood | Mild | Chronic | Mild normocytic to macrocytic anemia reported in MMDS10 cohort (PMID: 38950322) `[Human clinical]` |
| **Gastrointestinal symptoms (constipation, gastroesophageal reflux, failure to thrive)** | Clinical symptom | `HP:0002019` (Constipation); `HP:0002020` (Gastroesophageal reflux); `HP:0001508` (Failure to thrive) | Infancy to adulthood | Mild to severe | Chronic | GI symptoms reported in MMDS10 cohort (PMID: 38950322); failure to thrive in 2/2 probands in PMID: 38411040 `[Human clinical]` |
| **Uraciluria and thyminuria (secondary DPD deficiency)** | Laboratory / metabolic abnormality | No specific HPO ID retrieved in session (tested via LOINC `25140-5` uracil, `48157-2` thymine) | Infancy to adolescence | Marked biochemical elevation | Persistent | Elevated uracil (`CHEBI:17568`) and thymine (`CHEBI:17821`) in body fluids in 2/2 *CIAO1* patients tested in PMID: 38411040 `[Human clinical]` |
| **Recurrent severe infections** | Clinical sign / immunological | `HP:0002719` (Recurrent infections) | Infancy to adolescence | Severe / fatal | Episodic / recurrent | Prominent in severe *CIAO1* cohort (2/2 fatal infection-associated outcomes in PMID: 38411040) `[Human clinical]` |

### Quality of Life (QoL) Impact
No formal standardized QoL instrument scores (EQ-5D, SF-36, WHOQOL, or PROMIS) have been published for MMDS10 to date. Clinically documented functional impacts include:
- **Mobility and Ambulation:** Progressive proximal and axial skeletal muscle weakness impairs posture, stair climbing, and independent ambulation, progressing to wheelchair dependency in severe adolescent disease (PMID: 38950322; PMID: 38411040).
- **Respiratory Dependence:** Diaphragmatic and axial respiratory muscle weakness necessitates nocturnal or continuous noninvasive ventilatory support (e.g., BiPAP) and predisposes to life-threatening respiratory decompensation during infections (PMID: 38950322; PMID: 38411040).
- **Educational and Psychosocial Functioning:** Learning difficulties, autism spectrum traits, neurobehavioral comorbidities, chronic fatigue, and gastrointestinal dysmotility require multidisciplinary educational accommodations and caregiver support (PMID: 38950322; PMID: 38411040).

---

## 4. Genetic / Molecular Information

### Causal Gene
- **Gene Symbol:** *CIAO1* (*Cytosolic Iron-Sulfur Assembly Component 1*; aliases: *WDR39*, *CIA1*)
- **Identifiers:** `HGNC:14280` | `OMIM:604333` | `NCBI Gene:9391` | `Ensembl:ENSG00000144021` | `UniProt:O76071` | RefSeq mRNA: `NM_004804`
- **Genomic Locus:** Chromosome **2q11.2** (`GRCh38`: chr2:96,266,159–96,274,173) ([HGNC:14280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14280); [NCBI Gene:9391](https://www.ncbi.nlm.nih.gov/gene/9391)).
- **Gene Constraint (`[Population database / computational]`):** Strongly constrained against loss-of-function (`pLI` near `1.0`, low LOEUF score) and missense variation in gnomAD, reflecting its status as a pan-eukaryotic essential gene in CRISPR/Cas9 dropout screens (PMID: 38950322; PMID: 41131702).

### Pathogenic and Disease-Associated Variants (`NM_004804`)
All reported disease-causing *CIAO1* variants are **germline** in origin and act via an **autosomal recessive loss-of-function / hypomorphic** mechanism (no dominant-negative or gain-of-function mechanism has been observed; somatic *CIAO1* driver mutations are not implicated in MMDS10) (PMID: 38950322; PMID: 38411040).

| Variant (`NM_004804`) | Protein Change | dbSNP ID | Variant Class | Classification (Literature / UniProt / ClinVar Context) | gnomAD Population Frequency | Functional Consequence & Cohort Occurrence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`c.193C>T`** | **p.Arg65Trp** (R65W) | `rs11544859` | Missense | Likely pathogenic (`UniProt:O76071` / ACMG functional reclassification); historically listed as VUS in ClinVar prior to 2024–2025 functional studies | ~`0.00101` (~0.10% in gnomAD v2; ~0.16% in gnomAD v4, mainly non-Finnish European); **0 homozygotes** | Surface residue alteration; reduces binding to CIAO2B, MMS19, and HSC20; abolishes recruitment of ERCC2 and POLD1; causes DPD deficiency and 5-FU hypersensitivity in *C. elegans*. Recurrent in P2 & P3 (PMID: 38950322) and Patients 1 & 2 (PMID: 38411040; PMID: 41131702). |
| **`c.905A>C`** | **p.His302Pro** (H302P) | `rs756234455` | Missense | Pathogenic (`UniProt:O76071`; PMID: 38950322) | Ultra-rare; 0 homozygotes | Severe protein destabilization; complete loss of interaction with CIAO2B, MMS19, ERCC2, POLD1, and HSC20. Recurrent in P1, P2, and P3 (in trans with exon 7 deletion in P1, and in trans with `p.Arg65Trp` in P2 & P3; PMID: 38950322). |
| **`c.512A>G`** | **p.Asp171Gly** (D171G) | Not recorded in retrieved summary | Missense | Likely pathogenic (`UniProt:O76071`; PMID: 38950322) | Ultra-rare; 0 homozygotes | Reduced protein stability; decreased interaction with CIAO2B, MMS19, and HSC20; loss of interaction with ERCC2 and POLD1. Compound heterozygous with `p.His251Leu` in P4 (PMID: 38950322). |
| **`c.752A>T`** | **p.His251Leu** (H251L) | `rs748223775` | Missense | Likely pathogenic (`UniProt:O76071`; PMID: 38950322) | Ultra-rare; 0 homozygotes | Disrupts CIA targeting complex stability and client recruitment. Compound heterozygous with `p.Asp171Gly` in P4 (PMID: 38950322). |
| **Exon 7 deletion** | Multi-exon / intragenic exon deletion | Not assigned | Structural / intragenic deletion | Pathogenic (null allele) | Absent / ultra-rare | Paternally inherited loss-of-function deletion in trans with `p.His302Pro` in P1 (PMID: 38950322). |
| **`c.552G>C`** | **p.Trp184Cys** (W184C) | Not recorded in retrieved summary | Missense | Pathogenic / hypomorphic (historically VUS in ClinVar; validated in PMID: 38411040 & PMID: 41131702) | Ultra-rare; 0 homozygotes | Reduces CIAO1 protein stability and impairs DPD maturation. Compound heterozygous with `p.Arg65Trp` in Patient 2 (died age 19 yr; PMID: 38411040). |
| **`c.577C>T`** | **p.His193Tyr** (H193Y) | Not recorded in retrieved summary | Missense | Pathogenic / hypomorphic (historically VUS in ClinVar; validated in PMID: 38411040 & PMID: 41131702) | Ultra-rare; 0 homozygotes | Reduces CIAO1 protein stability and impairs DPD maturation. Compound heterozygous with `p.Arg65Trp` in Patient 1 (died age 18 mo; PMID: 38411040). |

### Modifier Genes, Epigenetics, and Chromosomal Abnormalities
- **Modifier Genes:** No validated human genetic modifiers of *CIAO1* disease severity have been identified. Phenotypic severity correlates primarily with the residual functional capacity of the two inherited *CIAO1* alleles (genotype–phenotype hypomorphic dosage model; PMID: 38950322; PMID: 38411040).
- **Epigenetic Information:** No primary or secondary DNA methylation, histone modification, or chromatin accessibility signatures have been reported for MMDS10 in PubMed, ENCODE, or Roadmap Epigenomics.
- **Chromosomal Abnormalities:** Large-scale chromosomal aneuploidies, translocations, or inversions are not implicated; structural variation to date is limited to an intragenic paternal **exon 7 deletion** in compound heterozygosity with a missense allele (PMID: 38950322).

---

## 5. Environmental Information

- **Environmental Factors:** No environmental toxins, radiation, or occupational pollutants cause MMDS10. However, pharmacological exposure to **5-fluorouracil (`CHEBI:46345`, `NCIT:C505`)** or capecitabine/fluoropyrimidine prodrugs poses an acute, potentially lethal toxicity hazard due to secondary DPD enzyme deficiency (`[Human clinical]`, `[Model organism]`; PMID: 38411040; PMID: 41131702).
- **Lifestyle Factors:** No smoking, alcohol, or dietary triggers cause MMDS10. Physical overexertion may exacerbate muscle fatigue or contribute to fluctuating serum CK elevations, though controlled studies are lacking (PMID: 38950322).
- **Infectious Agents:** MMDS10 is non-infectious in origin, but respiratory viral, bacterial, and fungal pathogens act as **secondary clinical triggers** of fatal decompensation in patients with compromised CIA-dependent antiviral/innate immunity and respiratory muscle weakness (`[Human clinical]`; PMID: 38411040).
  > *"The critical function of the cytosolic iron-sulfur protein assembly machinery for antiviral host defense may well explain the recurrent severe infections occurring in our patients."* — van Karnebeek et al., *Genet Med*, 2024 (PMID: 38411040) `[Human clinical]`

---

## 6. Mechanism / Pathophysiology

### Ordered Causal Chain

1. **Initiating genetic lesion:** Germline biallelic hypomorphic/loss-of-function mutations in *CIAO1* (`c.193C>T` p.Arg65Trp, `c.905A>C` p.His302Pro, `c.512A>G` p.Asp171Gly, `c.752A>T` p.His251Leu, `c.552G>C` p.Trp184Cys, `c.577C>T` p.His193Tyr, or exon 7 deletion) **lead to** amino acid substitutions within or structural truncation of the 7-bladed WD40 β-propeller protein CIAO1 (`[Demonstrated: Human clinical & biochemical]`, PMID: 38950322; PMID: 38411040).
2. **CIAO1 protein destabilization and surface interface disruption:** Mutant CIAO1 polypeptides **result in** reduced steady-state CIAO1 protein stability (e.g., p.His302Pro, p.Asp171Gly, p.Trp184Cys, p.His193Tyr) and/or altered surface interaction interfaces (e.g., p.Arg65Trp) (`[Demonstrated: In vitro biochemical]`, PMID: 38950322; PMID: 38411040).
3. **Impaired assembly of CIA targeting complexes:** Reduced CIAO1 abundance and defective binding **lead to** impaired assembly of the canonical **CIA targeting complex (`CIAO1–CIAO2B/FAM96B–MMS19`)** and the specialized **`CIAO1–CIAO2A/FAM96A` complex**, as well as reduced interaction with the co-chaperone HSC20 (`[Demonstrated: Structural & co-immunoprecipitation assays]`, PMID: 32632277; PMID: 38950322; `UniProt:O76071`).
4. **Failure of extramitochondrial `[4Fe-4S]` cluster transfer:** Defective CIA targeting complexes **result in** failure to recruit cytosolic and nuclear `[Fe-S]` apoproteins and failure to insert `[4Fe-4S]` (`CHEBI:49883`) cofactors downstream of the mitochondrial iron-sulfur cluster (ISC) export machinery (`[Demonstrated: Patient-derived cellular assays]`, PMID: 38950322; PMID: 38411040), **whereupon the pathogenic cascade branches into four downstream cellular arms**:
   - **Branch A — Nuclear Genome Maintenance & Replication Arm:**
     - **4A.** Failure to mature nuclear `[4Fe-4S]` client enzymes—including DNA polymerase δ catalytic subunit (`POLD1`), TFIIH repair helicase (`ERCC2`/XPD), and telomere/repair helicase (`RTEL1`)—**leads to** destabilization and loss of enzymatic activity of DNA polymerases, helicases, and DNA repair complexes (`[Demonstrated: Patient fibroblasts/cells]`, PMID: 38950322).
     - **5A.** Compromised DNA replication (`GO:0006260`) and DNA repair (`GO:0006281`) **result in** replicative stress, DNA damage accumulation, and impaired proliferation/regeneration in mitotically active progenitors (neuroepithelium, satellite cells, erythroid precursors) (`[Demonstrated in cells; tissue-specific progenitor exhaustion partially inferred]`, PMID: 38950322; PMID: 38411040).
     - **6A.** Impaired neural progenitor proliferation and post-mitotic neuronal DNA repair **lead to** congenital microcephaly, simplified cortical gyration, learning difficulties, and progressive neurodegeneration, while impaired erythropoiesis **contributes to** mild normocytic-to-macrocytic anemia (`[Demonstrated clinically; causal link from nuclear Fe-S client loss inferred from cellular assays]`, PMID: 38950322; PMID: 38411040).
   - **Branch B — Cellular Iron Homeostasis & Brain Iron Accumulation Arm:**
     - **4B.** Impaired `CIAO1–CIAO2A` and CIA pathway function **leads to** defective `[4Fe-4S]` cluster insertion into cytosolic aconitase (`ACO1` / IRP1) and altered turnover of iron regulatory protein 2 (`IREB2` / IRP2) (`[Demonstrated: Biochemical/cellular studies]`, PMID: 38950322; `UniProt:O76071`).
     - **5B.** Dysregulated IRP1/IRP2 iron-responsive element signaling **results in** perturbed intracellular iron ion homeostasis (`GO:0006879`) and inappropriate cellular iron uptake/sequestration (`[Demonstrated in cells; regional CNS vulnerability inferred]`, PMID: 38950322).
     - **6B.** Chronic regional iron dyshomeostasis **leads to** iron deposition in deep brain nuclei (globus pallidus `UBERON:0001875` and substantia nigra `UBERON:0002038`) on MRI and systemic iron/erythropoietic abnormalities (`[Demonstrated clinically on MRI; upstream IRP link inferred]`, PMID: 38950322).
   - **Branch C — Mitochondrial Morphology & Bioenergetic Cross-Talk Arm:**
     - **4C.** Cytosolic `[Fe-S]` assembly failure and intracellular iron/metabolic stress **lead to** secondary mitochondrial dysfunction, characterized by mildly diminished levels of lipoylated mitochondrial enzyme complexes (e.g., pyruvate/`α`-ketoglutarate dehydrogenase subunits such as `DLAT`) and markedly enlarged, structurally abnormal skeletal muscle mitochondria without classical isolated COX-negative fibers (`[Demonstrated in patient muscle biopsies; exact molecular bridge from cytosolic CIAO1 to mitochondrial lipoylation/enlargement remains partially inferred]`, PMID: 38950322).
     - **5C.** Combined myofiber genomic/regenerative stress (from Branch A) and secondary mitochondrial bioenergetic/structural pathology **result in** mixed myopathic and dystrophic myofiber degeneration with sarcolemmal leakage (`[Demonstrated in muscle histopathology]`, PMID: 38950322).
     - **6C.** Progressive myofiber degeneration in limb-girdle, trunk, and diaphragmatic muscles **leads to** fluctuating serum CK elevation, proximal and axial muscle weakness, and restrictive respiratory insufficiency (`[Demonstrated clinically]`, PMID: 38950322).
   - **Branch D — Cytosolic Metabolic & Antiviral Host-Defense Arm:**
     - **4D.** Failure to insert `[4Fe-4S]` clusters into cytosolic metabolic and innate-immune client enzymes—specifically dihydropyrimidine dehydrogenase (`DPYD`) and antiviral/translational `[Fe-S]` factors (such as `ABCE1` and `RSAD2`/viperin)—**results in** severe depletion of functional DPD protein and impaired host antiviral defense (`[Demonstrated for DPD in patient cells, zebrafish, and C. elegans; antiviral client link inferred in PMID: 38411040]`, PMID: 38411040; PMID: 41131702).
     - **5D.** Loss of DPD enzymatic activity **leads to** blocked pyrimidine nucleobase catabolism (`GO:0006208`), causing systemic accumulation of uracil (`CHEBI:17568`) and thymine (`CHEBI:17821`) and inability to catabolize 5-fluorouracil (`CHEBI:46345`), while defective antiviral `[Fe-S]` enzymes **result in** susceptibility to severe viral/bacterial/fungal infections (`[Demonstrated clinically and experimentally]`, PMID: 38411040; PMID: 41131702).

---

### Mechanistic Details by Functional Category

#### Molecular Pathways & Protein Dysfunction (`[Structural / biochemical]`, `[In vitro / patient-derived cellular]`)
- **Pathway:** Reactome `R-HSA-2564830` (*Cytosolic iron-sulfur cluster assembly*). Following intramitochondrial synthesis of a sulfur-containing precursor exported to the cytosol via `ABCB7` and initial `[4Fe-4S]` scaffold assembly by `NUBP1–NUBP2` with electron transfer via `CIAPIN1` and `CIAO3` (`NARFL`), the late-acting **CIA targeting complex (CTC)** transfers `[Fe-S]` clusters (`CHEBI:30408`) to target apoproteins ([UniProt:O76071](https://www.uniprot.org/uniprotkb/O76071/entry)).
- **Structural Architecture (`PDB:6TC0`, `6TBL`, `6TBN`; PMID: 32632277):** Crystal and cryo-EM structures by Kassube & Thomä (2020) demonstrated that `CIAO2B` acts as a central bridging subunit connecting the 7-bladed WD40 β-propeller of **CIAO1** to the HEAT-repeat client-adaptor protein **MMS19**, forming a bipartite client-recognition platform.
- **Mutational Dysfunction (PMID: 38950322; PMID: 38411040):**
  > *"Mutational analysis revealed reduced stability of the variants compared with wild-type CIAO1. Functional assays demonstrated failure of the variants identified in patients to recruit Fe-S recipient proteins, resulting in compromised activities of DNA helicases, polymerases, and repair enzymes that rely on the CIA complex to acquire their Fe-S cofactors. Lentivirus-mediated restoration of CIAO1 expression reversed all patient-derived cellular abnormalities."* — Maio et al., *J Clin Invest*, 2024 (PMID: 38950322) `[In vitro / patient-derived cellular]`

#### Cellular Processes, Metabolic Changes & Biochemical Abnormalities
- **Genome Maintenance & Mitosis:** Loss of `[4Fe-4S]` cluster delivery impairs `POLD1`, `ERCC2`, and `RTEL1` (`GO:0006261` DNA-templated DNA replication; `GO:0006281` DNA repair). CIAO1 also participates in the mitotic `MMXD` complex (`MMS19–CIAO2B–CIAO1–ERCC2–ANT2`) required for chromosome segregation (`GO:0007051`) (`UniProt:O76071`).
- **Pyrimidine Catabolism (`GO:0006208`):** Mammalian DPD (`DPYD`) requires two `[4Fe-4S]` clusters per monomer for electron transfer from NADPH to uracil/thymine. Biallelic *CIAO1* mutations destabilize apo-DPD, reducing DPD protein levels and enzymatic activity and elevating urinary/plasma uracil (`CHEBI:17568`) and thymine (`CHEBI:17821`) despite wild-type *DPYD* sequence (`[Human clinical]`, `[In vitro]`; PMID: 38411040).
- **Iron Homeostasis (`GO:0006879`) & Secondary Mitochondrial Bioenergetics (`GO:0006119`):** Impaired `ACO1` (`IRP1`) `[4Fe-4S]` holoenzyme conversion and `IREB2` (`IRP2`) regulation perturb cellular iron sensing, while skeletal muscle shows enlarged mitochondria and mildly decreased lipoylated complexes (`DLAT`) without classical COX-negative ragged-red fibers (PMID: 38950322).

#### Immune System Involvement & Tissue Damage Mechanisms
- **Innate / Antiviral Immunity:** Cytosolic `[Fe-S]` client enzymes including `RSAD2` (viperin, a radical SAM antiviral enzyme) and `ABCE1` (ribosome recycling / RNase L regulation) depend on the CIA targeting complex; their compromise explains recurrent, fatal viral/bacterial/fungal respiratory infections in severe *CIAO1* deficiency (PMID: 38411040).
- **Tissue Injury:** Skeletal muscle undergoes chronic myopathic and dystrophic degeneration with myofiber size variability and sarcolemmal CK release; deep brain nuclei accumulate excess iron, promoting regional neurotoxicity (PMID: 38950322).

#### Molecular Profiling & Advanced Technologies (`[In vitro / patient-derived cellular]`, `[Computational / functional genomics]`)
- **Multi-Omics Integration (PMID: 38411040):** Untargeted **proteomics, metabolomics, and lipidomics** in *CIAO1*- and *MMS19*-deficient patient-derived skin fibroblasts (`CL:0000057`) demonstrated profound global remodeling across all three omics layers, including broad depletion of cytosolic/nuclear `[Fe-S]` client proteins, accumulation of pyrimidine bases, and widespread lipidome remodeling.
  > *"Profound alterations in the proteome, metabolome, and lipidome were observed in patient-derived fibroblasts."* — van Karnebeek et al., *Genet Med*, 2024 (PMID: 38411040) `[In vitro / patient-derived cellular]`
- **Functional Genomics Screens:** Genome-wide CRISPR/Cas9 knockout screens (e.g., DepMap) classify *CIAO1* as a **pan-essential ("common essential") gene** across human cell lines, corroborating why complete biallelic null genotypes are not observed in living humans.
- **Single-Cell & Spatial Transcriptomics / Epigenomics:** No disease-specific single-cell RNA-seq, spatial transcriptomic, or epigenomic profiling datasets have been published for MMDS10 to date.

### Summary of Ontology Annotations for Pathophysiology
- ** Biological Process (GO):** `GO:0016226` (iron-sulfur cluster assembly), `GO:0006461` (protein complex assembly), `GO:0006260` / `GO:0006261` (DNA replication), `GO:0006281` (DNA repair), `GO:0007051` (chromosome segregation), `GO:0006879` (intracellular iron ion homeostasis), `GO:0006208` (pyrimidine nucleobase catabolic process), `GO:0006119` (oxidative phosphorylation — secondary).
- **Molecular Function (GO):** `GO:0046914` (transition metal ion binding), `GO:0051659` (metal cluster binding / protein binding).
- **Cell Types (CL):** Extrafusal skeletal muscle fiber (`CL:0008046`), neuron (`CL:0000540`), erythrocyte (`CL:0000232`), fibroblast (`CL:0000057` — experimentally profiled).

---

## 7. Anatomical Structures Affected

### Organ and System Level (`[Human clinical]`, PMID: 38950322; PMID: 38411040)
- **Primary Organs / Systems Directly Affected:**
  - **Musculoskeletal system / Skeletal muscle (`UBERON:0001134`):** Proximal limb-girdle and axial/paraspinal/diaphragmatic musculature (bilateral, symmetric myopathy).
  - **Central nervous system (`UBERON:0001010`):** Cerebral cortex (microcephaly, simplified gyral pattern in severe cases; cognitive/neurobehavioral dysfunction) and deep gray matter basal ganglia/midbrain nuclei—specifically the **globus pallidus (`UBERON:0001875`)** and **substantia nigra (`UBERON:0002038`)**, showing bilateral symmetric iron deposition on brain MRI.
- **Secondary / Multisystem Organ Involvement:**
  - **Respiratory system (`UBERON:0001004`):** Secondary restrictive ventilatory insufficiency due to respiratory muscle weakness and recurrent lower respiratory tract infections/bronchiolitis/pneumonia.
  - **Hematopoietic system / Red bone marrow (`UBERON:0002371` / `UBERON:0000361`):** Mild normocytic-to-macrocytic anemia.
  - **Gastrointestinal tract (`UBERON:0001555` / `UBERON:0005409`):** Gastroesophageal reflux and constipation.

### Tissue and Cell Level
- **Muscle tissue:** Striated skeletal muscle tissue (`UBERON:0001134`) and **extrafusal skeletal muscle fibers (`CL:0008046`)**, showing mixed myopathic/dystrophic changes and enlarged mitochondria (PMID: 38950322).
- **Nervous tissue:** CNS **neurons (`CL:0000540`)** and developing neural progenitors in cerebral cortex and basal ganglia (PMID: 38950322; PMID: 38411040).
- **Hematopoietic / Blood cells:** **Erythrocytes (`CL:0000232`)** and erythroid precursors; immune effector cells mediating antiviral defense (PMID: 38950322; PMID: 38411040).
- **Connective tissue (experimental):** Dermal **fibroblasts (`CL:0000057`)** exhibit diagnostic proteomic, metabolomic, lipidomic, and `[Fe-S]` enzyme defects (PMID: 38950322; PMID: 38411040).

### Subcellular Level (Gene Ontology Cellular Component)
- **Cytosol (`GO:0005829`) / Cytoplasm (`GO:0005737`):** Primary site of CIAO1 localization and the CIA targeting complex (`CIAO1–CIAO2B–MMS19` and `CIAO1–CIAO2A`) (`UniProt:O76071`).
- **Nucleus (`GO:0005634` / nucleoplasm `GO:0005654`):** Site of CIAO1 nuclear pool, mitotic `MMXD` complex, and target `[4Fe-4S]` DNA replication/repair client enzymes (`POLD1`, `ERCC2`, `RTEL1`) (`UniProt:O76071`; PMID: 38950322).
- **Mitochondrion (`GO:0005739`):** Site of upstream sulfur precursor export and secondary ultrastructural enlargement and mild lipoylation deficiency in MMDS10 skeletal muscle (PMID: 38950322).

### Localization and Lateralization
Muscle weakness (proximal and axial) and deep brain nuclei iron accumulation (`UBERON:0001875`, `UBERON:0002038`) are **bilateral and symmetric** (PMID: 38950322).

---

## 8. Temporal Development

### Onset (`[Human clinical]`)
- **Age of Onset:** Spans **prenatal/congenital/neonatal** (in severe neurodegenerative *CIAO1* deficiency presenting with IUGR, congenital microcephaly, simplified gyral pattern, and neonatal respiratory distress; PMID: 38411040) to **early childhood through adolescence** (in canonical neuromuscular MMDS10; PMID: 38950322). Adult- or geriatric-onset presentations have not been reported, although surviving childhood-onset MMDS10 patients have been followed into adulthood (PMID: 38950322).
- **Onset Pattern:** Typically **insidious / chronic** for neuromuscular weakness and cognitive symptoms (PMID: 38950322), punctuated by **acute decompensations** triggered by respiratory infections (PMID: 38411040).

### Progression
- **Disease Stages:** Formal clinical staging systems (e.g., WHO or neuromuscular staging scales) have not been established. Informally, progression spans early ambulatory proximal weakness $\rightarrow$ progressive axial/diaphragmatic weakness requiring noninvasive ventilation and mobility aids/wheelchair $\rightarrow$ advanced respiratory or infectious complications (PMID: 38950322; PMID: 38411040).
- **Progression Rate & Course Pattern:** **Variable, genotype-dependent progressive course**—**slowly progressive** over decades in canonical MMDS10 (`P1–P4` remained alive under clinical management in Maio et al., PMID: 38950322), whereas **rapidly progressive** in infantile neurodegenerative disease (fatal at **18 months** in Patient 1 of PMID: 38411040) or intermediate juvenile progression (fatal at **19 years** in Patient 2 of PMID: 38411040). Serum CK levels follow a **fluctuating** biochemical course (PMID: 38950322).
- **Disease Duration:** **Chronic, lifelong** genetic condition (or life-limiting in childhood/adolescence in severe alleles).

### Patterns
- **Remission Patterns:** **None.** Neither spontaneous nor treatment-induced disease remission occurs in humans.
- **Critical Periods:** **Prenatal corticogenesis** (vulnerability to microcephaly and gyral simplification when residual CIA activity is severely depressed; PMID: 38411040) and **periods of acute respiratory infection or fluoropyrimidine drug administration**, which represent critical windows for life-saving supportive care or drug avoidance (PMID: 38411040; PMID: 41131702).

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence and Incidence:** **Ultra-rare (`<1 per 1,000,000`).** Exact point prevalence and annual incidence per 100,000 have not been established in Orphanet, CDC, WHO, or Global Burden of Disease (GBD) registries; as of 2024–2026 primary literature, **6 genetically confirmed probands from 6 unrelated families** have been described across the two foundational cohorts (4 probands in PMID: 38950322; 2 probands in PMID: 38411040).

### Genetic Inheritance Characteristics
- **Inheritance Pattern:** **Autosomal recessive (AR)** ([OMIM:620960](https://omim.org/entry/620960); PMID: 38950322; PMID: 38411040).
- **Penetrance:** **Complete (100% inferred among known biallelic pathogenic cases)**, though milder hypomorphic genotypes could theoretically remain underdiagnosed due to VUS classification in ClinVar (PMID: 41131702).
- **Expressivity:** **Markedly variable**, ranging from viable childhood/adolescent-onset myopathy with mild CNS involvement (MMDS10; PMID: 38950322) to congenital microcephaly, DPD deficiency, and infantile lethality (PMID: 38411040). Noticeably, the `c.193C>T` (p.Arg65Trp) allele appears in *both* milder neuromuscular cases (in trans with `p.His302Pro` in P2 and P3; PMID: 38950322) and lethal neurodegenerative/DPD-deficient cases (in trans with `p.His193Tyr` or `p.Trp184Cys`; PMID: 38411040).
- **Genetic Anticipation:** **Not applicable** (non-repeat-expansion disorder).
- **Germline Mosaicism:** Not reported to date, though standard low theoretical recurrence risk applies as in any Mendelian disorder.
- **Founder Effects & Consanguinity:** All 6 reported *CIAO1* probands in PMID: 38950322 and PMID: 38411040 were **compound heterozygotes** rather than homozygotes from consanguineous unions—consistent with homozygosity for severe alleles being embryonic lethal and homozygosity for `p.Arg65Trp` being either extremely rare or unrecorded in gnomAD. `p.Arg65Trp` (`rs11544859`) is enriched in individuals of **non-Finnish European** ancestry (PMID: 38950322; PMID: 41131702).
- **Carrier Frequency (`[Population database / computational]`):** For `c.193C>T` (p.Arg65Trp) alone, allele frequency is ~`0.10%–0.16%` in gnomAD (corresponding to a heterozygous carrier frequency of ~`1 in 300` to `1 in 500` in non-Finnish European populations), whereas ultra-rare severe trans alleles (`p.His302Pro`, `p.Asp171Gly`, `p.His251Leu`, `p.Trp184Cys`, `p.His193Tyr`, exon deletions) are orders of magnitude rarer, explaining the ultra-low disease incidence (PMID: 38950322; PMID: 41131702).

### Population Demographics
- **Affected Populations & Geography:** Cases have been identified primarily through European and North American neuromuscular and metabolic referral centers (UK, US, Canada, Netherlands/Europe; PMID: 38950322; PMID: 38411040).
- **Sex Ratio:** Both **males and females** are affected (autosomal locus on 2q11.2; e.g., 1 female and 1 male in PMID: 38411040, plus male and female probands including female P4 in PMID: 38950322); sample size (*N* = 6) is too small for formal sex-ratio statistics.
- **Age Distribution:** Diagnosed from infancy (neonatal–18 months) through childhood, adolescence, and adulthood (PMID: 38950322; PMID: 38411040).

---

## 10. Diagnostics

### Clinical and Laboratory Tests (`[Human clinical]`)
- **Serum & Urine Biochemistry:**
  - **Serum Creatine Kinase (`LOINC:2157-6`):** Mildly to moderately elevated with characteristic **fluctuations** over time in MMDS10 (PMID: 38950322).
  - **Complete Blood Count & Iron Studies:** Mild normocytic (`HP:0001897`) to macrocytic (`HP:0001972`) anemia and altered iron indices (PMID: 38950322).
  - **Urine / Plasma Purine and Pyrimidine Panel (`LOINC:25140-5` uracil/creatinine; `LOINC:48157-2` thymine):** Markedly **elevated uracil (`CHEBI:17568`) and thymine (`CHEBI:17821`)** diagnostic of secondary DPD deficiency in *DPYD*-negative patients (PMID: 38411040).
- **Imaging Studies:**
  - **Brain MRI (with susceptibility-weighted / T2\* iron-sensitive sequences):** Demonstrates **iron accumulation in deep brain nuclei** (globus pallidus `UBERON:0001875` and substantia nigra `UBERON:0002038`) in MMDS10 (PMID: 38950322), or microcephaly and congenital cortical malformations such as **simplified gyral pattern (`HP:0009878`)** in severe infantile disease (PMID: 38411040).
  - **Muscle MRI:** Evaluates pattern of proximal and axial muscle fatty replacement/atrophy (PMID: 38950322).
- **Functional & Electrophysiological Tests:**
  - **Pulmonary Function Testing (spirometry, upright/supine forced vital capacity, nocturnal oximetry/capnography):** Essential to detect restrictive respiratory insufficiency and nocturnal hypoventilation early (PMID: 38950322).
  - **Electromyography (EMG) / Nerve Conduction Studies:** Demonstrates myopathic motor unit potentials without primary demyelinating neuropathy (PMID: 38950322).
- **Muscle Biopsy & Pathology Findings (`[Human clinical]`, PMID: 38950322):**
  - **Light Microscopy & Histochemistry:** Mixed **myopathic and dystrophic** features (fiber size variation, internal nuclei, mild endomysial fibrosis). Crucially, unlike classical mtDNA or intramitochondrial ISC myopathies, biopsies typically **lack COX-negative ragged-red fibers or isolated succinate dehydrogenase (SDH) deficiency**.
  - **Electron Microscopy (Ultrastructure):** Strikingly **enlarged, structurally abnormal mitochondria**.
  - **Immunoblotting:** Reduced steady-state CIAO1 levels and mildly diminished levels of lipoylated mitochondrial enzyme complexes (e.g., `DLAT`).

### Genetic Testing
- **Recommended Diagnostic Approach:** **Whole Exome Sequencing (WES)** or **Whole Genome Sequencing (WGS)** (trio-based preferred to establish *in trans* compound heterozygosity and detect coding deletions such as the exon 7 deletion in P1; PMID: 38950322; PMID: 38411040).
- **Gene Panels:** *CIAO1* (`HGNC:14280`) is increasingly incorporated into updated **Mitochondrial Disorders**, **Congenital Myopathy / Limb-Girdle Muscular Dystrophy**, and **NBIA (Neurodegeneration with Brain Iron Accumulation)** panels (e.g., Genomics England PanelApp). Older panels curated prior to mid-2024 may omit *CIAO1*, necessitating WES/WGS reanalysis.
- **Single-Gene Testing & Deletion/Duplication Analysis:** Useful for targeted familial cascade/carrier testing or confirming intragenic exon deletions (e.g., exon 7 deletion).
- **Variant Interpretation Caveat:** Because missense alleles such as `p.Arg65Trp`, `p.Trp184Cys`, and `p.His193Tyr` have historically appeared as **VUS** in ClinVar, ACMG/AMP curation must integrate `PM3` (compound heterozygosity in trans), `PS3` (published functional validation in patient fibroblasts, yeast/zebrafish/*C. elegans*), and biochemical biomarkers (uraciluria/thyminuria) (PMID: 38950322; PMID: 38411040; PMID: 41131702).
- **CMA, Karyotyping, FISH, mtDNA Sequencing, Repeat Expansion Testing:** Low primary diagnostic yield for *CIAO1* missense variants; mtDNA sequencing is normal and serves primarily to exclude primary mitochondrial DNA myopathies, while high-resolution exon-level CNV calling or WGS is superior to standard low-resolution CMA/karyotyping for single-exon *CIAO1* deletions.

### Omics-Based Diagnostics (`[In vitro / research]`)
- **Metabolomics / Targeted Pyrimidine Profiling:** Urine/plasma uracil and thymine quantification serves as an accessible functional biomarker of *CIAO1*-related DPD deficiency (PMID: 38411040).
- **Proteomics & Lipidomics:** Untargeted fibroblast proteomics and lipidomics confirm global depletion of CIA client proteins (`DPYD`, `POLD1`, `ERCC2`, `RTEL1`) and CIAO1 instability on a research basis (PMID: 38950322; PMID: 38411040). RNA-seq (to confirm splicing/deletion impact) and liquid biopsy are not routine clinical diagnostics for MMDS10.

### Clinical Criteria & Differential Diagnosis
- **Standardized Criteria:** No formal international society diagnostic criteria exist; definitive diagnosis requires **clinical neuromuscular/neurodevelopmental compatibility + biallelic pathogenic/likely pathogenic variants in *CIAO1***.
- **Differential Diagnosis:**
  1. **MMDS1–MMDS9 (`NFU1`, `BOLA3`, `IBA57`, `ISCA2`, `ISCA1`, `PMPCB`, `FDX2`, `IND1/NUBPL`, `ISD11/LYRM4`):** Share lipoylation defects and mitochondrial encephalopathy/myopathy, but typically show severe primary OXPHOS/complex I–II deficiencies and lactic acidosis rather than isolated cytosolic `[Fe-S]` / DPD defects.
  2. ***MMS19* Deficiency (PMID: 38411040):** Direct binding partner in the CIA targeting complex; shares microcephaly, neurodegeneration, recurrent infections, and secondary DPD deficiency (`uraciluria`/`thyminuria`).
  3. **Limb-Girdle Muscular Dystrophies (LGMD) & Congenital Myopathies (e.g., *SELENON*, *LMNA*, *COL6A1–3*, *RYR1*):** Overlap proximal/axial weakness, fluctuating CK, and early respiratory insufficiency, but lack brain iron accumulation and uraciluria.
  4. **Neurodegeneration with Brain Iron Accumulation (NBIA, e.g., *PANK2*, *WDR45*, *PLA2G6*, *FTL*):** Share globus pallidus/substantia nigra iron deposition (`HP:0002454`), distinguished by *CIAO1*'s prominent myopathy and elevated CK (PMID: 38950322).
  5. **Primary DPD Deficiency (*DPYD*):** Shares elevated uracil/thymine and 5-FU toxicity, distinguished by normal *DPYD* sequencing and multisystem CIA pathology in *CIAO1* deficiency (PMID: 38411040).

### Screening
- **Newborn Screening (NBS):** Not included on current ACMG Recommended Uniform Screening Panels (RUSP).
- **Cascade & Carrier Screening:** Targeted *CIAO1* sequencing is indicated for parents and siblings of confirmed probands.
- **Pre-Chemotherapy Pharmacogenetic Screening (`[Emerging translational implication]`):** Li et al. (2025/2026; PMID: 41131702) highlight that biallelic hypomorphic *CIAO1* variants explain a subset of *DPYD*-negative DPD deficiency and severe 5-FU toxicity.

---

## 11. Outcome / Prognosis

### Survival and Mortality (`[Human clinical]`)
- **Overall Survival & Mortality:** Quantitative 5-year and 10-year actuarial survival rates cannot be calculated from *N* = 6 published cases, but survival bifurcates sharply across the allelic spectrum:
  - **Canonical Neuromuscular MMDS10 Cohort (PMID: 38950322):** **4 of 4 probands (100%) were alive** at publication (spanning childhood to adulthood) with ongoing respiratory and neuromuscular management.
  - **Severe Neurodegenerative / DPD-Deficient *CIAO1* Cohort (PMID: 38411040):** **2 of 2 probands (100% mortality)** died prematurely—Patient 1 at **18 months** (respiratory failure from bronchiolitis with bacterial and fungal superinfection) and Patient 2 at **19 years** (multi-organ failure following carnificating pneumonia, septic cardiomyopathy, and intracranial hemorrhages).

### Morbidity, Disability, and Quality of Life
- **Long-Term Disability:** Chronic progressive axial and proximal myopathy causing impaired ambulation or wheelchair dependence, chronic restrictive respiratory failure requiring nocturnal/continuous BiPAP, mild-to-severe cognitive/neurobehavioral disability, chronic anemia, and GI dysmotility (PMID: 38950322; PMID: 38411040). Formal ICF or EQ-5D/SF-36 metrics have not been published.

### Disease Course, Complications, and Recovery Potential
- **Major Complications:** Restrictive respiratory failure, recurrent severe viral/bacterial/fungal pneumonia, sepsis and septic cardiomyopathy, intracranial hemorrhage (reported in sepsis context in Patient 2, PMID: 38411040), progressive loss of ambulation, and potential lethal toxicity if exposed to fluoropyrimidines.
- **Recovery Potential:** Structural CNS malformations and genetic myopathy are **irreversible** without disease-modifying gene replacement; however, respiratory failure and infectious complications are partially modifiable with proactive noninvasive ventilation and aggressive infection management.

### Prognostic Factors and Biomarkers
- **Genotype / Residual CIAO1 Stability:** Combinations retaining higher residual CIAO1 protein levels/complex assembly correlate with survival into adulthood, whereas more severely destabilizing compound genotypes correlate with infantile cortical malformations and early mortality (PMID: 38950322; PMID: 38411040).
- **Clinical Prognostic Indicators:** Congenital microcephaly/simplified gyration, neonatal respiratory distress, and recurrent severe infections portend poor survival (PMID: 38411040). Validated quantitative prognostic circulating biomarkers have not yet been established in FDA or BEST biomarker databases.

---

## 12. Treatment

No FDA- or EMA-approved disease-specific pharmacotherapies or curative interventions currently exist for MMDS10. Clinical care relies on multidisciplinary **supportive care (`NCIT:C15747` / `NCIT:C15426`)** tailored to affected organ systems.

### Pharmacotherapy & Pharmacogenomics
- **Pharmacological Treatments:** No small-molecule drug restores CIAO1 function in humans. Empirical mitochondrial cofactor cocktails have not been evaluated in controlled trials for MMDS10. Symptomatic medications (e.g., osmotic laxatives for constipation, proton-pump inhibitors/antireflux therapy for gastroesophageal reflux, targeted antimicrobials/antifungals for superinfections) are used per standard clinical guidelines (PMID: 38950322; PMID: 38411040).
- **Pharmacogenomics (Critical Contraindication — `[Human clinical]`, `[Model organism]`):** Because biallelic *CIAO1* variants cause secondary **dihydropyrimidine dehydrogenase (DPD) deficiency**, systemic **5-fluorouracil (`CHEBI:46345`, `NCIT:C505`)** and related fluoropyrimidines (e.g., capecitabine, tegafur) are **strictly contraindicated or require extreme caution/avoidance** due to risk of catastrophic, life-threatening fluoropyrimidine toxicity (PMID: 38411040; PMID: 41131702).

### Advanced Therapeutics (`[Preclinical / in vitro]`)
- **Gene Therapy (`NCIT:C15238`):** No clinical gene therapy exists; however, **preclinical proof-of-concept** was demonstrated by Maio et al. (2024; PMID: 38950322), where **lentivirus-mediated restoration of wild-type *CIAO1* expression reversed all cellular and biochemical `[Fe-S]` client enzyme abnormalities** in patient-derived cells (`[In vitro / patient-derived cellular]`).
- **Cell Therapy, RNA-Based Therapies, Targeted Therapies, Immunotherapies:** None developed or evaluated for MMDS10.

### Surgical, Supportive, and Rehabilitative Management
- **Respiratory Support (`Noninvasive Ventilation`, `NCIT:C178949`):** Nocturnal or daytime bilevel positive airway pressure (**BiPAP**) / noninvasive ventilation, airway clearance / cough-assist devices, and prompt respiratory support during intercurrent illnesses are cornerstone life-sustaining interventions for restrictive respiratory insufficiency (PMID: 38950322).
- **Rehabilitation (`Physical Therapy`, `NCIT:C63536`):** Individualized physical therapy, occupational therapy, orthotic/postural support for axial weakness, mobility assistive devices, and neurodevelopmental/educational support for learning and neurobehavioral comorbidities (PMID: 38950322).
- **Nutritional & GI Care (`Supportive Care`, `NCIT:C15747`):** Nutritional optimization for failure to thrive and medical management of gastroesophageal reflux and constipation (PMID: 38950322; PMID: 38411040).
- **Surgical Interventions:** No disease-specific surgeries reported (standard orthopedic/scoliosis or gastrostomy evaluations apply if clinically indicated by axial weakness or severe dysphagia/failure to thrive).

### Experimental Treatments & Clinical Trials
- **ClinicalTrials.gov / EU CTR / WHO ICTRP Status:** **Zero active, recruiting, or completed interventional clinical trials** targeting *CIAO1* or MMDS10 were identified as of November 2026.
- **Treatment Outcomes, Response Rates, and Personalized Strategy:** Formal response rates and FAERS adverse event profiles do not exist due to absence of disease-specific drug therapy; personalized care currently centers on **genotype-guided surveillance** (pulmonary function, brain MRI, CBC/iron, urine pyrimidines) and **strict fluoropyrimidine avoidance**.

---

## 13. Prevention

- **Primary Prevention & Genetic Counseling (`NCIT:C18195`):** Because MMDS10 is an inherited autosomal recessive disorder, primary prevention centers on **genetic counseling**, **targeted carrier testing** for at-risk relatives of confirmed cases (25% recurrence risk per pregnancy in carrier couples), **prenatal genetic diagnosis** (chorionic villus sampling or amniocentesis), and **preimplantation genetic testing for monogenic disorders (PGT-M)**.
- **Secondary Prevention (Early Detection):** Early WES/WGS diagnosis in infants/children with unexplained proximal/axial myopathy, fluctuating CK, or *DPYD*-negative uraciluria/thyminuria enables **pre-symptomatic pulmonary surveillance** (detecting nocturnal hypoventilation before acute respiratory arrest) and **pharmacogenetic medical alert flagging** against 5-fluorouracil (`NCIT:C505`) (PMID: 38950322; PMID: 38411040; PMID: 41131702).
- **Tertiary Prevention & Immunization:** Preventing life-threatening infectious decompensation via **routine and seasonal respiratory immunizations** (influenza, pneumococcal, RSV, COVID-19 vaccines per CDC/WHO schedules unless specific immunological contraindications exist), prompt antimicrobial therapy for respiratory infections, noninvasive ventilation (`NCIT:C178949`), and physical rehabilitation (`NCIT:C63536`) to prevent contractures and aspiration (PMID: 38950322; PMID: 38411040).
- **Behavioral, Public Health, and Environmental Interventions:** Standard respiratory infection-control precautions in vulnerable patients; no population-wide environmental or public health vector interventions apply.

---

## 14. Other Species / Natural Disease

### Taxonomy and Orthologous Genes
*CIAO1* is deeply conserved across all eukaryotes as an essential component of the cytosolic `[Fe-S]` assembly machinery:

| Species | Common Name | NCBI Taxon ID | Ortholog Symbol | NCBI Gene ID | Additional Database ID |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *Homo sapiens* | Human | `NCBITaxon:9606` | `CIAO1` | `9391` | `HGNC:14280` |
| *Mus musculus* | House mouse | `NCBITaxon:10090` | `Ciao1` | `26371` | `MGI:1346998` |
| *Danio rerio* | Zebrafish | `NCBITaxon:7955` | `ciao1` | `561726` | ZFIN `ciao1` |
| *Drosophila melanogaster* | Fruit fly | `NCBITaxon:7227` | `Ciao1` (`CG12797`) | `38415` | FlyBase |
| *Caenorhabditis elegans* | Nematode | `NCBITaxon:6239` | `ciao-1` (`Y18D10A.9`) | `180415` | WormBase |
| *Saccharomyces cerevisiae* | Baker's yeast | `NCBITaxon:4932` | `CIA1` (`YDR267C`) | `853327` | SGD |

### Natural Disease in Other Species, Comparative Biology & Transmission
- **Naturally Occurring Animal Disease & Breed Associations:** **None known.** A search of **OMIA (Online Mendelian Inheritance in Animals)** and veterinary literature retrieves **no spontaneous/naturally occurring *CIAO1*-related disease** in companion animals, livestock, or wildlife; consequently, no Vertebrate Breed Ontology (VBO) breed associations exist.
- **Comparative Biology:** Across yeast, nematodes, insects, teleost fish, and mammals, the WD40 β-propeller fold of CIAO1 and its bridging interaction with `CIAO2B` and `MMS19` are evolutionarily invariant (`PDB:6TC0` used *Drosophila*/*Homo sapiens* conserved components; PMID: 32632277). Complete loss of function is uniformly lethal across species, explaining why natural veterinary disease would only arise from rare biallelic hypomorphic alleles.
- **Transmission / Zoonotic Potential:** **Not applicable.** MMDS10 is a non-communicable germline Mendelian disorder with zero zoonotic or cross-species transmission potential.

---

## 15. Model Organisms

### Experimental Model Systems (`[Model organism]`, `[In vitro / patient-derived cellular]`)

| Organism / System | Model Type & Genetic Design | Key Phenotypes & Recapitulation | Limitations & Research Applications | Primary References & Databases |
| :--- | :--- | :--- | :--- | :--- |
| **Zebrafish (*Danio rerio*, `NCBITaxon:7955`)** | *In vivo* vertebrate genetic deficiency model (`ciao1` loss-of-function / knockout alongside `mms19` models) | Recapitulates **detrimental neurodevelopmental, morphological, and biochemical consequences** of human *CIAO1* deficiency, validating systemic failure of cytosolic/nuclear `[Fe-S]` protein maturation | Does not model adult-onset chronic human limb-girdle/axial myopathy or upright diaphragmatic mechanics; ideal for developmental CNS and metabolic rescue screening | van Karnebeek et al., 2024 (PMID: 38411040); ZFIN (`NCBI Gene:561726`) |
| **Nematode (*Caenorhabditis elegans*, `NCBITaxon:6239`)** | *In vivo* invertebrate **CRISPR/Cas9 humanized/orthologous knock-in allelic series** in `ciao-1` (`NCBI Gene:180415`), modeling human `p.Arg65Trp` (`ciao-1(p.Arg71Trp)`), `p.Trp184Cys`, and `p.His193Tyr`, paired with `dpyd-1` studies | Recapitulates **hypomorphic partial loss of function**, **secondary DPD (`dpyd-1`) destabilization**, and **markedly heightened 5-fluorouracil (`CHEBI:46345`) sensitivity** (severe embryonic lethality and reduced hatch rates upon 5-FU drug challenge) | Lacks vertebrate brain nuclei, lungs, and erythroid marrow; serves as a rapid, quantitative *in vivo* platform to reclassify human *CIAO1* VUS alleles and test fluoropyrimidine pharmacogenetics | Li et al., *Genetics*, 2025/2026 (PMID: 41131702; PMCID: `PMC12774842`); WormBase |
| **Mouse (*Mus musculus*, `NCBITaxon:10090`)** | Mammalian constitutional knockout (`Ciao1`, `MGI:1346998`, `NCBI Gene:26371`) | Complete systemic knockout results in **early embryonic lethality**, confirming absolute developmental essentiality of mammalian *Ciao1* | Constitutional null lethality precludes postnatal study of chronic myopathy or brain iron accumulation; tissue-specific conditional (`Cre-loxP`) or hypomorphic knock-in mouse models are required to model postnatal MMDS10 | MGI (`MGI:1346998`); IMPC |
| **Fruit fly (*Drosophila melanogaster*, `NCBITaxon:7227`) & Yeast (*Saccharomyces cerevisiae*, `NCBITaxon:4932`)** | Invertebrate (`Ciao1` / `CG12797`) and unicellular eukaryotic (`CIA1` / `YDR267C`) depletion/knockout and recombinant structural expression systems | Complete depletion causes **cell/organismal lethality** and loss of cytosolic/nuclear `[Fe-S]` enzyme maturation (e.g., DNA polymerases, Leu1, Rad3/XPD); recombinant proteins enabled high-resolution crystal/cryo-EM structure of the CIA targeting complex (`PDB:6TC0`) | Unicellular/invertebrate physiology cannot model mammalian organ pathology; foundational for dissecting biochemical `[4Fe-4S]` transfer and client recognition | Kassube & Thomä, 2020 (PMID: 32632277); FlyBase; SGD |
| **Patient-Derived Primary Cells (Human skin fibroblasts `CL:0000057` & lentiviral rescue lines)** | *In vitro* human cellular disease model from MMDS10 and severe *CIAO1* probands, with **lentiviral wild-type *CIAO1* complementation** | Directly recapitulates **CIAO1 protein instability**, failed recruitment/activity of `POLD1`, `ERCC2`, `RTEL1`, and `DPYD`, and **global proteome, metabolome, and lipidome perturbations**; all cellular defects are **reversed by lentiviral *CIAO1* restoration** | Monolayer fibroblasts do not form contractile myofibers or deep brain nuclei; patient iPSC-derived myotubes/organoids have not yet been reported | Maio et al., 2024 (PMID: 38950322); van Karnebeek et al., 2024 (PMID: 38411040) |

---

## Primary References Cited

1. **Maio N, Orbach R, Zaharieva IT, Töpf A, Donkervoort S, Munot P, et al. (incl. Rouault TA, Bönnemann CG).** *Loss of function of the cytoplasmic Fe-S assembly protein CIAO1 causes a neuromuscular disorder with compromise of nucleocytoplasmic Fe-S enzymes.* **The Journal of Clinical Investigation.** 2024 Jun;134(12):e179559. **PMID: 38950322** | DOI: [10.1172/JCI179559](https://doi.org/10.1172/JCI179559) | PubMed: [https://pubmed.ncbi.nlm.nih.gov/38950322/](https://pubmed.ncbi.nlm.nih.gov/38950322/)
2. **van Karnebeek CDM, Tarailo-Graovac M, Leen R, Meinsma M, Correard S, Jansen-Meijer J, et al.** *CIAO1 and MMS19 deficiency: A lethal neurodegenerative phenotype caused by cytosolic Fe-S cluster protein assembly disorders.* **Genetics in Medicine.** 2024 Jun (Epub 2024 Feb 24);26(6):101104. **PMID: 38411040** | DOI: [10.1016/j.gim.2024.101104](https://doi.org/10.1016/j.gim.2024.101104) | PubMed: [https://pubmed.ncbi.nlm.nih.gov/38411040/](https://pubmed.ncbi.nlm.nih.gov/38411040/)
3. **Li X, Menendez Perdomo IM, van Kuilenburg ABP, Tarailo-Graovac M.** *Functional studies of human variants in C. elegans link iron metabolism to DPD deficiency and 5-FU sensitivity.* **Genetics.** 2025 Oct / 2026 Jan;iyaf228. **PMID: 41131702** | PMCID: `PMC12774842` | DOI: [10.1093/genetics/iyaf228](https://doi.org/10.1093/genetics/iyaf228) | PubMed: [https://pubmed.ncbi.nlm.nih.gov/41131702/](https://pubmed.ncbi.nlm.nih.gov/41131702/)
4. **Kassube SA, Thomä NH.** *Structural insights into Fe-S protein biogenesis by the CIA targeting complex.* **Nature Structural & Molecular Biology.** 2020;27:735–742. **PMID: 32632277** | PDB: `6TC0`, `6TBL`, `6TBN` | PubMed: [https://pubmed.ncbi.nlm.nih.gov/32632277/](https://pubmed.ncbi.nlm.nih.gov/32632277/)
5. **Online Mendelian Inheritance in Man (OMIM).** *#620960 — Multiple Mitochondrial Dysfunctions Syndrome 10; MMDS10* and *\*604333 — Cytosolic Iron-Sulfur Assembly Component 1; CIAO1*. URLs: [https://omim.org/entry/620960](https://omim.org/entry/620960) | [https://omim.org/entry/604333](https://omim.org/entry/604333)
6. **UniProtKB / Swiss-Prot.** *O76071 (CIAO1_HUMAN) — Probable cytosolic iron-sulfur protein assembly protein CIAO1.* URL: [https://www.uniprot.org/uniprotkb/O76071/entry](https://www.uniprot.org/uniprotkb/O76071/entry)
7. **HGNC / NCBI Gene / MedGen.** *HGNC:14280 (CIAO1)* ([https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14280)); *NCBI Gene: 9391* ([https://www.ncbi.nlm.nih.gov/gene/9391](https://www.ncbi.nlm.nih.gov/gene/9391)); *MedGen: C5975413* ([https://www.ncbi.nlm.nih.gov/medgen/1874943](https://www.ncbi.nlm.nih.gov/medgen/1874943)).

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 81 |
| Resolved | 67 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 13 |
| Terms whose name was checked | 7 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0975806` (5 mentions) - the report calls it "Mondo Disease Ontology"; MONDO calls it **multiple mitochondrial dysfunctions syndrome 10**
- `NCBITaxon:6239` (2 mentions) - the report calls it "Nematode"; NCBITaxon calls it **Caenorhabditis elegans**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006461` (GO_0006461) (1 mention) - replaced by `GO:0065003`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `UniProt`, `ORPHA`, `Gene`, `LOINC`, `MGI`.