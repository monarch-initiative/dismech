---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-04T01:15:32.089282'
end_time: '2026-11-04T01:21:28.793140'
duration_seconds: 356.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Oropouche Fever
  mondo_id: MONDO:0000345
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Oropouche virus disease or disorder; Oropouche virus infectious disease;
    Oropouche virus caused disease or disorder
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-5-5
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 4
  num_turns: 18
  total_cost_usd: 2.8085381
  session_id: 1c1c36b0-61fa-4300-ab5b-8c27ed6424dc
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 12
reference_validation:
  total_references: 13
  verified: 12
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.077
  relevance_assessed: 12
  on_topic: 10
  unresolved_references:
  - DOI:10.1016/j.nmni.2026.100296
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 61
  verified: 59
  not_found: 1
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.016
  labels_checked: 5
  labels_matching: 2
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: NCBITaxon:71617
    reported_labels:
    - Culicoides
    ontology_label: Tolypocladium ophioglossoides
  - term_id: NCBITaxon:161674
    reported_labels:
    - Bradypus tridactylus
    ontology_label: Tetratrichomonas sp. 1998-5003
  labels_variant: 1
  unresolved_terms:
  - HP:0007177
  obsolete_terms:
  - term_id: GO:0039503
    ontology_label: obsolete suppression by virus of host innate immune response
    replaced_by: GO:0052170
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Oropouche Fever
- **MONDO ID:** MONDO:0000345 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Oropouche virus disease or disorder; Oropouche virus infectious disease; Oropouche virus caused disease or disorder
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Oropouche Fever** covering all of the
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

I'll research Oropouche Fever to produce the research report. Let me search primary sources.

Excellent detail. Let me get pathogenesis/experimental models and the clinical-frequency systematic review.

Let me pin PMIDs and the NCBITaxon ID via PubMed/NCBI.

I have enough well-sourced material to write the report. Here it is.

---

# Oropouche Fever — Disease Characteristics Research Report

**Target:** Oropouche Fever | **MONDO:0000345** | **Category:** Infectious Disease
**Causal gene:** None — this is an arboviral infectious disease, not a Mendelian disorder. The "causal factor" is the **Oropouche virus (OROV)**, a segmented negative-sense RNA orthobunyavirus (NCBITaxon:118655; species *Orthobunyavirus oropoucheense*). There is no human causal gene; host genetics are at most minor modifiers.

> Primary anchor references used throughout: Tilston-Lunel NL, *J Gen Virol* 2024 (**PMID:39351896**, PMC11443551) — the current comprehensive review; Schwartz DA, Dashraath P, Baud D, *Viruses* 2024 (**PMID:39339911**, PMC11437435) — pregnancy/vertical transmission; and a 2026 *New Microbes and New Infections* systematic review of 1975–2025 data (DOI 10.1016/j.nmni.2026.100296).

---

## 1. Disease Information

Oropouche fever is an emerging, usually self-limiting, acute arboviral febrile illness caused by Oropouche virus, transmitted to humans chiefly by the biting midge *Culicoides paraensis*. It presents as a dengue-like syndrome (fever, headache, myalgia, arthralgia) with a characteristic **relapse/recurrence** of symptoms after apparent recovery, and in a minority of cases causes aseptic meningitis or meningoencephalitis. The 2023–2024 re-emergence across the Americas added the first reported **deaths** and the first evidence of **vertical transmission** with fetal loss and congenital microcephaly.

**Identifiers**
- **MONDO:** MONDO:0000345 (Oropouche fever)
- **ICD-11:** 1D4A.0 — Oropouche virus disease (within arthropod-borne viral fevers); **ICD-10:** A93.0 (Oropouche virus disease)
- **MeSH:** D009894 "Oropouche fever" / supplementary "Oropouche virus"
- **Pathogen:** NCBITaxon:118655 (Oropouche virus); species *Orthobunyavirus oropoucheense*
- **OMIM:** not applicable (no Mendelian gene)

**Synonyms:** Oropouche virus disease; Oropouche virus infection; OROV disease; "Oropouche" is from the Oropouche River / wetland region of Trinidad, where the first isolate was obtained in 1955 (etymology: PMC5938780).

**Data basis:** Aggregated disease-level resources (outbreak surveillance, case series, systematic reviews) rather than EHR-derived individual-patient data; much of the quantitative detail comes from Brazilian and Peruvian outbreak investigations.

Sources: [J Gen Virol 2024 / PMC11443551](https://pmc.ncbi.nlm.nih.gov/articles/PMC11443551/); [systematic review / ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2052297526000296).

---

## 2. Etiology

**Primary cause — infectious.** OROV, a tri-segmented negative-sense ssRNA virus of family *Peribunyaviridae*, genus *Orthobunyavirus* (Simbu serogroup). Infection follows the bite of an infected *Culicoides paraensis* midge (urban/epidemic cycle); a sylvatic cycle involves non-human primates, sloths and possibly birds.

**Risk factors (environmental/ecological — no genetic risk loci established):**
- **Residence in / travel to endemic Amazonian and Latin American regions**; northern Brazil accounts for >80% of cases, with Amazonas the likely epicentre (PMID:39351896).
- **Rainy season** — outbreaks show seasonal behaviour with higher incidence in the wet season (Peru 2024–2025, [PMC12845246](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12845246/)).
- **Proximity to midge breeding sites** (decaying vegetation, banana/cacao plantations, wetlands); **deforestation and urbanization** bridging sylvatic and urban cycles.
- **Age 20–49** most affected — attributed to greater occupational/outdoor vector exposure, not biological susceptibility; **both sexes equally affected** (PMID:39351896).
- **Pregnancy** is a risk factor for severe outcome (fetal, not necessarily maternal).

**Protective factors:** Vector avoidance (repellents, fine-mesh screening — midges are small enough to pass standard mosquito netting), vector control, and prior infection conferring presumed homotypic immunity. No protective genetic variants described.

**Gene–environment interactions:** None characterized in humans. In model systems, **host type I interferon status** is the dominant determinant of outcome (see §6).

Sources: [PMC11443551](https://pmc.ncbi.nlm.nih.gov/articles/PMC11443551/); [Peru outbreak PMC12845246](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12845246/).

---

## 3. Phenotypes (with suggested HPO terms)

From the 2025/2026 systematic review (1975–2025) and PMID:39351896. Frequencies are approximate and vary by outbreak.

| Phenotype | Type | Frequency | HPO suggestion |
|---|---|---|---|
| Fever (often abrupt, high) | Symptom/sign | ~94% | HP:0001945 Fever |
| Headache | Symptom | ~87% | HP:0002315 Headache |
| Myalgia | Symptom | ~73% | HP:0003326 Myalgia |
| Arthralgia | Symptom | common | HP:0002829 Arthralgia |
| Chills/rigors | Symptom | common | HP:0025143 Chills |
| Malaise/fatigue | Symptom | common | HP:0012378 Fatigue |
| Nausea / vomiting | Symptom | frequent in severe | HP:0002018 Nausea; HP:0002013 Vomiting |
| Photophobia | Symptom | frequent | HP:0000613 Photophobia |
| Retro-orbital/eye pain | Symptom | frequent | HP:0000541 (retinal detachment — not apt); use HP:0025435 Retro-orbital pain if available, else HP:0000481 Abnormal cornea? → prefer **HP:0025435** |
| Dizziness/vertigo | Symptom | in CNS cases | HP:0002321 Vertigo |
| Maculopapular rash | Sign | variable | HP:0000988 Skin rash (or HP:0000509 — n/a) |
| Lymphopenia | Lab | common | HP:0001888 Lymphopenia |
| Leukopenia | Lab | common | HP:0001882 Leukopenia |
| Thrombocytopenia | Lab | common | HP:0001873 Thrombocytopenia |
| Elevated transaminases | Lab | common | HP:0002910 Elevated hepatic transaminase |
| Hemorrhage (petechiae, epistaxis, gingival) | Sign | severe cases | HP:0001892 Abnormal bleeding; HP:0000421 Epistaxis; HP:0000225 Gingival bleeding; HP:0000979 Petechiae |
| Aseptic meningitis | Sign | ~2% (1980 Pará: 22/292) | HP:0011227 Meningitis (→ HP:0100702 Aseptic meningitis if present) |
| Meningoencephalitis / neck stiffness, nystagmus, lethargy | Sign | rare | HP:0002383 Encephalitis; HP:0031179 Nuchal rigidity; HP:0000639 Nystagmus |
| Guillain-Barré syndrome (post-infectious) | Sign | rare, reported post-Cuba outbreak | HP:0007177 (acute inflammatory demyelinating polyneuropathy — GBS) |

**Characteristics**
- **Onset:** acute/abrupt, after 3–10 day incubation; **adult-predominant** by exposure.
- **Severity:** usually mild–moderate and self-limiting; severe coagulopathic/hepatic disease and death are rare (two 2024 deaths, Bahia, in healthy women 21 & 24 y with severe coagulopathy and liver impairment, no neurological signs).
- **Progression:** acute phase 2–7 days, then **recurrence of symptoms in ~60% (classically; "common")** 2–10 days later, without detectable viraemia — mechanism unknown.
- **QoL:** acute disabling febrile illness causing days–weeks of lost activity; recurrence prolongs morbidity; CNS and congenital cases carry major long-term impact.

**Congenital phenotypes** (vertical transmission): microcephaly (HP:0000252), stillbirth/fetal death (HP:0001560 fetal death; HP:0500141), congenital malformation syndrome, OROV IgM in neonatal serum/CSF.

Sources: [systematic review](https://www.sciencedirect.com/science/article/pii/S2052297526000296); [PMC11443551](https://pmc.ncbi.nlm.nih.gov/articles/PMC11443551/); [virulence review PMC13134406](https://pmc.ncbi.nlm.nih.gov/articles/PMC13134406/).

---

## 4. Genetic / Molecular Information (viral genome — no human causal gene)

OROV has a **tri-segmented, single-stranded, negative-sense RNA genome**; virions are enveloped, spherical, ~90–100 nm (PMID:39351896).

| Segment | Size | Encodes | Function / GO suggestion |
|---|---|---|---|
| **S** | 958 nt | **N** nucleoprotein (~27 kDa) + **NSs** (~11 kDa), overlapping ORFs | N: ribonucleocapsid (GO:0019013 viral nucleocapsid); NSs: **type I interferon antagonist** (GO:0039503 suppression of host innate immune response; GO:0039563) |
| **M** | 4385 nt | glycoprotein precursor → **Gn** (~32 kDa) + **Gc** (~110 kDa) + **NSm** (~27 kDa) | Gn/Gc: receptor binding & membrane fusion/entry (GO:0019064 fusion of virus membrane with host plasma membrane); NSm dispensable for mammalian replication |
| **L** | 6852 nt | **RdRp / L protein** (~261 kDa) | RNA-dependent RNA polymerase, uses **cap-snatching** (GO:0039689 negative stranded viral RNA replication; GO:0003968) |

**Reassortment is central to OROV evolution and epidemiology.** Reassortment with related Simbu-group viruses (Madre de Dios, Iquitos, Perdões, possibly Jatobal) has generated novel M segments. The 2023–2024 American lineage is a **novel reassortant** carrying Amazonian M-segment ancestry; some authors link it to altered clinical behaviour (vertical transmission, deaths) while a Peruvian study found no clear change in clinical/epidemiological behaviour across variants — this remains contested.

**Human genetics:** No causal genes, pathogenic variants, modifier genes, allele frequencies, or epigenetic signatures are established. Fields 4's human-variant subheadings are **not applicable**. Host determinant of outcome is the **innate antiviral (MAVS–IRF3/7–IFN-α/β)** pathway, characterized only in animal/cell models (§6).

Sources: [PMC11443551](https://pmc.ncbi.nlm.nih.gov/articles/PMC11443551/); reassortant pregnancy report [PMC11765011](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11765011/).

---

## 5. Environmental Information

- **Infectious agent:** Oropouche virus (NCBITaxon:118655).
- **Vectors:** Urban/epidemic — **_Culicoides paraensis_** (biting midge; NCBITaxon:71617 for genus *Culicoides*) is the principal proven vector; *Culicoides sonorensis* equally susceptible in lab. Secondary/possible — *Culex quinquefasciatus* (OROV-positive field midges/mosquitoes found in Mato Grosso, but competence not established; most *Aedes*/*Culex* are poorly competent when orally fed). Sylvatic vector unknown; OROV isolated from *Mansonia venezuelensis* and *Aedes serratus*.
- **Reservoir hosts:** Non-human primates (*Callithrix penicillata*, *Cebus olivaceus*), **pale-throated three-toed sloth** (*Bradypus tridactylus*); neutralizing antibodies in wild/domestic birds suggest possible avian carriage.
- **Ecological drivers:** Deforestation, agricultural expansion (cacao, banana), urbanization, high-density midge breeding in decaying organic matter, and climate/rainfall seasonality.
- **Lifestyle/occupational:** Outdoor and agricultural work in endemic zones; no diet/smoking/alcohol associations.

Sources: [PMC11443551](https://pmc.ncbi.nlm.nih.gov/articles/PMC11443551/); vector-competence systematic review [PMC12043118](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12043118/).

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating exposure → clinical manifestation)

1. **Infected *Culicoides paraensis* midge bites a human → inoculation of OROV into dermis** (sylvatic spillover initiates the urban cycle). *Demonstrated epidemiologically.*
2. **Gn/Gc glycoproteins mediate attachment and clathrin-dependent entry into permissive cells, followed by endosomal membrane fusion** → cytoplasmic release of the three RNP segments. *Demonstrated in vitro (Vero, mammalian cells).*
3. **L-protein RdRp transcribes/replicates the genome using cap-snatching; N encapsidates; M-encoded glycoproteins assemble at the Golgi** → new virions bud and spread. *Demonstrated.*
4. **NSs antagonizes the host type I interferon response** (suppresses host transcription / IFN-α/β induction), permitting early high-titre **viraemia** (peaks ~day 2 of symptoms). *Demonstrated; NSs deletion attenuates the virus.*
5. **Viraemia + innate immune activation (pro-inflammatory cytokines) → systemic febrile syndrome** (fever, headache, myalgia, arthralgia). *Inferred from clinical + model data.*
6. **Branch A — hepatotropism/coagulopathy:** OROV infects the **liver**, producing focal → (when IFN is antagonized) massive hepatic necrosis, transaminase elevation, thrombocytopenia and coagulopathy → severe/fatal disease in a minority. *Demonstrated in mouse models (anti-IFNAR1 lethal model); consistent with the two 2024 fatal human cases.*
7. **Branch B — neurotropism:** OROV reaches the **CNS** (viral RNA in CSF) → aseptic meningitis / meningoencephalitis; prolongs acute phase to 2–4 weeks. *Demonstrated (CSF RNA, outbreak meningitis rates).*
8. **Branch C — post-infectious autoimmunity:** molecular mimicry/immune dysregulation → **Guillain-Barré syndrome** rise after the Cuban outbreak. *Association; mechanism inferred.*
9. **Branch D — vertical transmission:** maternal viraemia → **hematogenous transplacental infection** → fetoplacental infection, fetal multi-organ infection, **neurotropic fetal CNS damage → microcephaly, fetal death/stillbirth**. *Demonstrated (fetal-tissue RNA, neonatal IgM); mouse models reproduce severe congenital disease; causality still being consolidated.*

### Supporting detail
- **Molecular pathways / cellular processes:** innate antiviral signalling (RIG-I/MAVS → IRF-3/IRF-7 → type I IFN) **restricts** OROV; OROV **NSs** counteracts it. OROV infection induces **apoptosis** and host translational shutoff (GO:0006915 apoptotic process; GO:0051607 defense response to virus; GO:0045071 negative regulation of viral genome replication).
- **Immune system:** type I IFN (IFN-α/β) is the principal restriction factor (MAVS−/−, IRF3/7−/−, IFNAR−/− mice show enhanced, often lethal, infection). Immunocompetent mice are largely resistant — hamsters and IFN-deficient mice are the tractable models.
- **Tissue damage:** hepatic necrosis (oxidative/inflammatory), CNS inflammation, placental/fetal infection.
- **Cell types (CL suggestions):** hepatocyte (CL:0000182), neuron (CL:0000540), macrophage/monocyte (CL:0000235), trophoblast (CL:0000351) / syncytiotrophoblast, endothelial cell (CL:0000115).

Sources: [virulence/pathogenesis review PMC13134406](https://pmc.ncbi.nlm.nih.gov/articles/PMC13134406/); [reporter-virus/IFN pathogenesis, JVI](https://journals.asm.org/doi/10.1128/jvi.00893-24); [acute hepatitis mouse model PMC13386938](https://pmc.ncbi.nlm.nih.gov/articles/PMC13386938/); [type I IFN controls vertical transmission, iScience](https://www.cell.com/iscience/fulltext/S2589-0042(26)00022-2); [congenital disease in embryonic mice, Nat Commun](https://www.nature.com/articles/s41467-026-77294-6).

---

## 7. Anatomical Structures Affected (UBERON / GO-CC)

- **Organ level:** blood/vasculature (viraemia; UBERON:0000178 blood), **liver** (UBERON:0002107), **central nervous system / brain & meninges** (UBERON:0000955 brain; UBERON:0002360 meninges), **placenta & fetus** (UBERON:0001987 placenta), skin (inoculation site, rash; UBERON:0002097).
- **Body systems:** immune/haematologic, hepatic, nervous, and (in pregnancy) fetoplacental; musculoskeletal (myalgia/arthralgia).
- **Tissue/cell:** hepatocytes, neurons/glia, meningeal cells, trophoblast, mononuclear phagocytes, endothelium.
- **Subcellular (GO-CC):** cytoplasm/ribonucleoprotein complex (GO:0019013), Golgi apparatus (viral assembly/budding; GO:0005794), host plasma/endosomal membranes (entry).
- **Lateralization:** systemic/bilateral; no lateralized pattern.

---

## 8. Temporal Development

- **Onset:** acute, after **3–10 day incubation**; abrupt febrile start.
- **Acute phase:** 2–7 days; viraemia peaks ~day 2.
- **Recurrence:** symptom relapse 2–10 days after acute phase is characteristic ("common"), without detectable virus — course is therefore often **biphasic/relapsing** rather than monophasic.
- **CNS cases:** extended course, 2–4 weeks.
- **Duration:** self-limited in the vast majority; full recovery typical. Rare severe (hepatic/coagulopathic) and fatal courses; post-infectious GBS has its own neurologic trajectory.
- **Remission:** spontaneous. No chronic infection established.
- **Critical period:** **pregnancy** (fetal vulnerability to vertical transmission) is the key window for adverse outcomes.

Source: [PMC11443551](https://pmc.ncbi.nlm.nih.gov/articles/PMC11443551/).

---

## 9. Inheritance and Population (Epidemiology)

- **Not heritable** — infectious; inheritance/penetrance/consanguinity/carrier-frequency subheadings are **not applicable**.
- **Historical burden:** first human recognition Trinidad 1955; Brazilian emergence Belém 1960; **>30 outbreaks 1961–1996, ~500,000 estimated cases** (PMID:39351896). Likely one of the most common arboviral infections in the Amazon, long under-diagnosed.
- **2024 re-emergence:** **9,852 confirmed cases by end of August 2024**, including 5 vertical-transmission cases and the **first 2 reported deaths**; WHO assessed regional/global risk as high.
- **Geography:** endemic — northern Brazil (>80% of cases; Amazonas epicentre), Peru, Bolivia, Ecuador, Colombia, Venezuela, Panama, Haiti, French Guiana. 2024 expansion — sustained transmission in non-endemic Brazilian states, Cuba (first time), Dominican Republic; **imported/travel cases** in the US (≥32 by Aug 2024, mostly Florida, returning from Cuba) and Europe (Italy, Spain, Germany).
- **Demographics:** both sexes equally affected; peak ages 20–49 (exposure-driven); no ethnic predisposition.

Sources: [PMC11443551](https://pmc.ncbi.nlm.nih.gov/articles/PMC11443551/); [CDC EID Nov 2024](https://wwwnc.cdc.gov/eid/article/30/11/24-1220_article).

---

## 10. Diagnostics

- **Molecular (confirmatory):** **RT-qPCR** on serum/blood within ~5 days of onset (also detectable in **saliva and urine** up to 5 days); multiplex arbovirus panels used to distinguish dengue/Zika/chikungunya. (LOINC: use a molecular-detection code for OROV RNA where available.)
- **Viral isolation:** on acute samples (≤5-day window), historically in suckling mice/Vero cells — reference labs only.
- **Serology:** IgM/IgG ELISA; plaque-reduction neutralization (specific). Older HI/complement-fixation have **low specificity and cross-reactivity** within the Simbu group.
- **Supportive lab:** leukopenia, lymphopenia, thrombocytopenia, elevated transaminases.
- **CSF:** pleocytosis and OROV RNA in meningitis/encephalitis.
- **Congenital work-up:** OROV RT-PCR of placenta/fetal tissues; neonatal serum/CSF IgM; neuroimaging for microcephaly.
- **Clinical criteria / differential:** no formal society criteria; diagnosis is clinical-epidemiological + lab. Differential: **dengue, Zika, chikungunya, mayaro, malaria, leptospirosis, other Simbu-group viruses** — overlapping dengue-like presentation makes laboratory confirmation essential; the **relapsing course** is a clinical clue.
- **Screening:** no population screening; **avoid NSAIDs** in suspected cases until dengue excluded (CDC Aug 2024 guidance, bleeding risk).

Source: [PMC11443551](https://pmc.ncbi.nlm.nih.gov/articles/PMC11443551/).

---

## 11. Outcome / Prognosis

- **Generally excellent** — self-limiting; historically **no deaths** until the 2024 outbreak (2 fatalities in young healthy women with coagulopathy/hepatic failure).
- **Morbidity:** days–weeks of disabling febrile illness; frequent symptom recurrence; aseptic meningitis usually resolves without sequelae.
- **Severe/adverse outcomes:** rare hemorrhagic/hepatic/coagulopathic disease; post-infectious **Guillain-Barré syndrome**; **fetal loss (miscarriage, stillbirth) and congenital microcephaly** following vertical transmission are the most serious recognized outcomes.
- **Prognostic factors:** pregnancy (fetal risk), severe coagulopathy/hepatic involvement, CNS involvement; host IFN competence (from models).
- **Case fatality:** historically ~0; very low even in 2024, but true denominators are uncertain due to under-ascertainment.

Sources: [PMC11443551](https://pmc.ncbi.nlm.nih.gov/articles/PMC11443551/); [Lancet Infect Dis 2024, vertical transmission & deaths](https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(24)00557-7/fulltext).

---

## 12. Treatment (NCIT suggestions)

- **No approved antiviral and no licensed vaccine** — management is **supportive care only** (NCIT:C15747 Supportive Care).
- **Symptomatic:** antipyretics/analgesics — **acetaminophen/paracetamol preferred; avoid NSAIDs and aspirin** until dengue excluded (bleeding risk). Pharmacotherapy (NCIT:C15986) with analgesic agent (acetaminophen CHEBI:46195).
- **Supportive:** hydration/fluids, rest; hospital/critical care (NCIT:C53511 Intensive Care) for severe coagulopathic/hepatic or neurologic disease.
- **Pregnancy:** vector-bite avoidance and monitoring; no specific therapy.
- **Experimental:** no agent in advanced clinical trials; antivirals and vaccine candidates are preclinical. (ClinicalTrials.gov yields no OROV-specific licensed-therapy trial as of 2025–2026.)
- **Pharmacogenomics / targeted / cell / gene / RNA therapies:** not applicable.

Source: [PMC11443551](https://pmc.ncbi.nlm.nih.gov/articles/PMC11443551/).

---

## 13. Prevention

- **Primary — vector/bite avoidance (mainstay):** insect repellents (DEET/picaridin), long sleeves, **fine-mesh screening** (midges pass standard mosquito nets), avoiding peak midge activity; vector control of *Culicoides* breeding sites; community education.
- **Immunization:** **no vaccine available** (candidates preclinical).
- **Secondary:** early recognition and lab confirmation; arbovirus surveillance; **NSAID avoidance** pending dengue exclusion.
- **Tertiary:** supportive management to prevent complications; obstetric monitoring in infected pregnant people.
- **Pregnancy-specific public health:** enhanced bite protection and risk counselling for pregnant travelers to/residents of endemic areas (CDC/PAHO advisories, 2024).
- **Public health:** environmental management (reducing organic-debris breeding habitat), reduced deforestation-driven spillover, cross-border surveillance given travel-associated spread.

Sources: [PMC11443551](https://pmc.ncbi.nlm.nih.gov/articles/PMC11443551/); [CDC EID 2024](https://wwwnc.cdc.gov/eid/article/30/11/24-1220_article).

---

## 14. Other Species / Natural Disease

- **Host taxonomy (NCBITaxon):** humans (9606); non-human primate reservoirs — *Callithrix penicillata*, *Cebus olivaceus*; **pale-throated three-toed sloth** *Bradypus tridactylus* (NCBITaxon:161674); wild/domestic birds (serological evidence).
- **Vectors:** *Culicoides paraensis*; genus *Culicoides* (NCBITaxon:71617).
- **Natural disease in animals:** reservoir hosts are generally **asymptomatic amplifying hosts**; no overt natural disease syndrome is described in sloths/primates — they maintain the sylvatic cycle. No companion-animal disease recognized.
- **Zoonotic/cross-species:** classic zoonotic spillover from a sylvatic (animal/arthropod) cycle into humans, with human amplification in the urban cycle. **Reassortment** among co-circulating Simbu-group orthobunyaviruses (Madre de Dios, Iquitos, Jatobal) is a key cross-lineage feature.

Source: [PMC11443551](https://pmc.ncbi.nlm.nih.gov/articles/PMC11443551/).

---

## 15. Model Organisms

- **Mice:** the workhorse models require **impaired type I IFN** — **IFNAR−/−**, **MAVS−/−**, **IRF-3/IRF-7−/−**, and **anti-IFNAR1-antibody-treated** mice develop productive, often lethal infection with **hepatic necrosis** and systemic spread; immunocompetent adult mice are largely resistant (sublethal). Suckling mice were the historical isolation host. A **ZsGreen reporter OROV (M-segment)** enables in vivo pathogenesis tracking. **Embryonic/pregnant mouse models** reproduce **severe congenital disease and fetoplacental infection**, with type I IFN controlling vertical transmission.
- **Hamsters:** permissive and useful for **immune/pathogenesis studies** where immunodeficient mice are limiting.
- **Cell lines / in vitro:** **Vero** (isolation/titration), plus mammalian and insect (C6/36) cells; used for entry, NSs–IFN antagonism, and reassortment studies.
- **Recapitulation / limitations:** IFN-deficient mice capture hepatotropism, CNS invasion, lethality and congenital disease but **depend on removing the very restriction factor (type I IFN)** that shapes human disease, so translational fidelity to immunocompetent humans is limited; whether the 2024 reassortant crosses the placenta more efficiently than historical strains is **not yet confirmed**.
- **Applications:** entry/replication, NSs interferon antagonism, tissue tropism (liver, CNS), vertical transmission, antiviral/vaccine preclinical testing.

Sources: [reporter virus, JVI](https://journals.asm.org/doi/10.1128/jvi.00893-24); [acute hepatitis model, PMC13386938](https://pmc.ncbi.nlm.nih.gov/articles/PMC13386938/); [iScience vertical transmission](https://www.cell.com/iscience/fulltext/S2589-0042(26)00022-2); [Nat Commun congenital disease](https://www.nature.com/articles/s41467-026-77294-6).

---

## Key citations (for KB evidence items — fetch with `just fetch-reference`)

- **PMID:39351896** — Tilston-Lunel NL. Oropouche Virus: an emerging orthobunyavirus. *J Gen Virol* 2024 (comprehensive review; genome, vectors, clinical, epidemiology).
- **PMID:39339911** — Schwartz DA, Dashraath P, Baud D. OROV in pregnancy: placental/fetal infection, stillbirth, microcephaly. *Viruses* 2024.
- Systematic review 1975–2025, *New Microbes and New Infections* — symptom frequencies ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2052297526000296)).
- Lancet Infect Dis 2024 (DOI 10.1016/S1473-3099(24)00557-7) — first vertical transmission & deaths.
- CDC EID 30(11), Nov 2024 — reemergence and US spread risk.
- JVI reporter virus / IFN pathogenesis; iScience & Nat Commun congenital models.

### Notes for curation
- This is an **infectious disease entry**: populate `infectious_agent` with **NCBITaxon:118655** (Oropouche virus), at least one `transmission` route (vector-borne, *Culicoides paraensis*; plus hematogenous **vertical transmission**), and `agent_life_cycle` with vectors (*Culicoides*) and non-human reservoirs (primates, sloths) — per the infectious-disease granularity ladder (§3e). Granularity level = **named clinical entity** (Oropouche fever); do not split by viral lineage/reassortant — carry lineage structurally if needed.
- **No human causal gene / OMIM** — leave `genetic:` empty; the virulence genetics are viral (S/M/L segments, NSs IFN antagonist).
- Before binding any term or citing any snippet, verify CURIEs with OAK/term validation and fetch each reference into `references_cache/` — several HPO suggestions above (e.g. retro-orbital pain, aseptic meningitis) and the symptom-frequency numbers should be confirmed against the fetched sources rather than taken from this report verbatim.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 10 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1016/j.nmni.2026.100296` (1 mention) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 61 |
| Resolved | 59 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 5 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCBITaxon:71617` (2 mentions) - the report calls it "Culicoides"; NCBITaxon calls it **Tolypocladium ophioglossoides**
- `NCBITaxon:161674` (1 mention) - the report calls it "Bradypus tridactylus"; NCBITaxon calls it **Tetratrichomonas sp. 1998-5003**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0007177` (1 mention), reported as "acute inflammatory demyelinating polyneuropathy — GBS" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0039503` (obsolete suppression by virus of host innate immune response) (1 mention) - replaced by `GO:0052170`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:118655` (4 mentions) - the report calls it "Oropouche virus", "Infectious agent:** Oropouche virus"; NCBITaxon calls it **Oropouche virus**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCBITaxon:118655` - called "Oropouche virus", "Infectious agent:** Oropouche virus"