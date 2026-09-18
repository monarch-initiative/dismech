---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-02T13:17:56.352082'
end_time: '2026-09-02T13:26:42.035973'
duration_seconds: 525.68
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: SETD1A-Related Early-Onset Epilepsy
  mondo_id: ''
  category: Mendelian
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 33
  num_turns: 58
  total_cost_usd: 2.5738471999999994
  session_id: a7ad17b6-3a08-5da2-b864-d177f77ddc2f
  stop_reason: end_turn
  assistant_text_blocks: 2
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:26974950
  relevance_assessed: 21
  on_topic: 18
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 63
  verified: 58
  not_found: 1
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.017
  labels_checked: 37
  labels_matching: 27
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0000238
    reported_labels:
    - Frontal bossing
    ontology_label: Hydrocephalus
  - term_id: HP:0005605
    reported_labels:
    - Capillary hemangioma
    ontology_label: Large cafe-au-lait macules with irregular margins
  - term_id: GO:0006119
    reported_labels:
    - oxidative phosphorylation / mitochondrial respiratory chain complex I assembly
    ontology_label: oxidative phosphorylation
  - term_id: UBERON:0002616
    reported_labels:
    - hippocampal formation, implicated via memory studies
    ontology_label: regional part of brain
  labels_variant: 6
  unresolved_terms:
  - HP:0000342
  obsolete_terms:
  - term_id: GO:0051568
    ontology_label: obsolete histone H3-K4 methylation
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SETD1A-Related Early-Onset Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SETD1A-Related Early-Onset Epilepsy** covering all of the
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

I'll research SETD1A-related early-onset epilepsy using web searches, gathering primary literature and database information across the requested categories.

# SETD1A-Related Early-Onset Epilepsy: Comprehensive Research Report

## 1. Disease Information

**Overview.** SETD1A-related early-onset epilepsy is a rare, monogenic neurodevelopmental disorder caused by heterozygous (typically de novo) loss-of-function or missense variants in *SETD1A* (SET Domain Containing 1A), a gene encoding the catalytic subunit of the human COMPASS (Complex Proteins Associated with Set1) histone H3 lysine-4 (H3K4) methyltransferase complex. *SETD1A* haploinsufficiency produces a clinically heterogeneous, age-dependent spectrum: infants and young children most often present with global developmental delay, hypotonia, dysmorphic facial features, and early-onset epilepsy, while older children, adolescents, and adults are more likely to present with intellectual disability, autism-spectrum features, obsessive-compulsive symptoms, and — in a genome-wide-significant fraction of cases — schizophrenia and other psychotic disorders (PMID:26974950, PMID:32346159).

Two overlapping, allelic OMIM phenotype entries currently describe the *SETD1A* clinical spectrum:
- **EPEO2 — Epilepsy, Early-Onset, 2, With or Without Developmental Delay** (OMIM #618832): an autosomal dominant disorder with generalized tonic-clonic seizure onset in the first days, months, or years of life, with highly variable severity — from normal psychomotor development and normal neuroimaging to developmental delay with brain-imaging abnormalities. Caused by heterozygous missense mutations, first delineated by Yu et al. (PMID:31197650).
- **NEDSID — Neurodevelopmental Disorder with Speech Impairment and Dysmorphic Facies** (OMIM #619056): developmental delay with mild-to-moderate intellectual disability or learning difficulties, behavioral/psychiatric abnormalities, delayed speech/language, dysmorphic facies, distal limb anomalies, GI/feeding difficulties, and hypotonia. Delineated in 15 patients by Kummeling et al. (PMID:32346159).

The disorder is also frequently discussed under the umbrella name "SETD1A-associated neurodevelopmental disorder" (or "SETD1A syndrome") spanning both entries, since the epilepsy and dysmorphic-ID phenotypes overlap substantially and are caused by variants in the same gene, sometimes in the same family.

**Key identifiers:**
- **Gene (OMIM):** *611052 – SET Domain-Containing Protein 1A; SETD1A*
- **Phenotype (OMIM):** #618832 (EPEO2); #619056 (NEDSID)
- **HGNC:** hgnc:17284 (SETD1A) — NCBI Gene ID 9739
- **Orphanet:** Listed under gene page for SETD1A; disease-causing mutations associated with "Non-specific syndromic intellectual disability" (ORPHA:528084); a dedicated ORPHA number specific to the epilepsy phenotype was not identified in this search
- **MeSH:** Epilepsy (D004827); Intellectual Disability (D008607) — no SETD1A-specific MeSH descriptor exists
- **MONDO:** not directly resolved in this search; likely maps to a SETD1A-related neurodevelopmental disorder term cross-referencing OMIM 618832/619056
- **ICD-10/11:** G40.- (Epilepsy) with Q87.8 (other specified congenital malformation syndromes) as adjunct — no disease-specific code
- **Gene aliases:** KMT2F, Set1, Set1A, EPEDD, NEDSID

**Data provenance.** Nearly all published knowledge derives from aggregated case series and case reports (individual clinical/genetic case reports plus pooled cohort analyses from exome-sequencing studies of schizophrenia/developmental-disorder cohorts — e.g., the DDD study, Finnish SISu/birth-cohort exomes), not from a disease registry or large natural-history study. This is an ultra-rare, only recently delineated (2016 onward) gene-disease association.

---

## 2. Etiology

**Disease causal factor:** Purely genetic/monogenic. Heterozygous de novo (occasionally inherited, autosomal dominant) loss-of-function or missense variants in *SETD1A* are sufficient to cause disease; there is no known environmental, infectious, or multifactorial trigger required.

**Genetic risk factors:**
- *SETD1A* is exceptionally constrained against loss-of-function variation in the general population — in the founding study, only 2 LoF variants were found among 45,376 non-schizophrenia ExAC exomes, placing SETD1A "among the 3% most constrained genes in the human genome" (PMID:26974950).
- Loss-of-function variant classes: nonsense, frameshift, canonical splice-site variants (most causing NEDSID/severe phenotype), and a small number of missense variants (largely reported in the EPEO2/epilepsy phenotype).
- A recurrent splice-acceptor variant (c.4582-2delAG, NM_014712.3, exon 16) has arisen independently multiple times (≥7 occurrences across cohorts, including de novo events), consistent with a mutational hotspot (PMID:26974950).
- No common susceptibility loci or polygenic risk modifiers specific to the SETD1A-driven phenotype have been reported; however, an intronic SNP (rs11150601) has been separately associated with female schizophrenia risk in the UK Biobank — this is a common-variant association distinct from the rare monogenic LoF mechanism and should not be conflated with it.

**Environmental risk factors:** None established. Case reports occasionally note nonspecific perinatal factors (e.g., one infantile-spasms case followed mild birth asphyxia and low birth weight; PMID for case: PMC10620521/Frontiers in Neurology 2023, DOI 10.3389/fneur.2023.1278035) but these appear coincidental rather than causal, given the driving de novo genetic lesion.

**Protective factors:** None identified in the literature for humans. In mice, pharmacological rescue (see Mechanism, below) demonstrates that circuit/cognitive deficits are reversible in adulthood, implying the deficit is a dynamic functional state rather than irreversible structural damage — a form of "protective" pharmacological intervention rather than a naturally occurring protective genetic/environmental factor.

**Gene-environment interactions:** Not established; no CTD/PheGenI data specific to SETD1A gene-environment interaction were identified.

---

## 3. Phenotypes

Phenotype frequency data are drawn primarily from two pooled cohorts: the original Nature Neuroscience schizophrenia/DDD meta-analysis (PMID:26974950, n=14 LoF carriers), and the Kummeling et al. 2021 NEDSID cohort (PMID:32346159, n=15). Because case ascertainment differs (psychiatric-genetics cohort vs. pediatric neurodevelopmental cohort), frequencies below should be read as convergent signal rather than a single denominator.

### Neurological / Epilepsy Phenotypes
| Phenotype | Onset | Severity/course | Frequency | Suggested HPO |
|---|---|---|---|---|
| Generalized tonic-clonic seizures | First days to years of life (EPEO2) | Highly variable; some patients seizure-free with treatment, others drug-resistant | ~38% of reported SETD1A patients (pooled from prior literature per PMC10620521 review); ~1/10 schizophrenia LoF carriers had childhood epilepsy (PMID:26974950) | HP:0002069 (Bilateral tonic-clonic seizure) / HP:0001250 (Seizure) |
| Focal seizures with impaired awareness / motor seizures | Infancy (e.g., 3 months in one missense case) | Responsive to phenobarbital in reported case | Case-level (Frontiers 2026 case report, DOI 10.3389/fnins.2026.1864983) | HP:0002384 (Focal-onset seizure) |
| Infantile epileptic spasms syndrome (hypsarrhythmia + spasms + developmental arrest) | 6 months | Rapidly responsive to ACTH in the single reported case | First reported case: PMC10620521 (2023) | HP:0011097 (Epileptic spasm); HP:0012469 (Infantile spasms) |
| EEG abnormalities (background slowing, sharp waves, paroxysmal sharp-slow complexes) | Variable | Nonspecific | Frequent across case reports | HP:0002353 (EEG abnormality) |
| Global developmental delay | Infancy/early childhood | Mild to severe, variable | Predominant feature; present in most non-isolated-epilepsy cases (PMID:32346159; PMID:26974950) | HP:0001263 (Global developmental delay) |
| Intellectual disability / learning difficulties | Childhood onward | Mild to severe | 7/10 schizophrenia LoF carriers had learning difficulties (PMID:26974950); core NEDSID feature | HP:0001249 (Intellectual disability) |
| Delayed speech and language | Early childhood | Variable | Core NEDSID feature | HP:0000750 (Delayed speech and language development) |
| Hypotonia | Infancy | Variable | Core NEDSID feature | HP:0001252 (Hypotonia) |

### Psychiatric / Behavioral Phenotypes (age-dependent, emerging later)
- Schizophrenia with hallucinations/delusions (genome-wide-significant association, PMID:26974950); frequently requiring long-term psychiatric hospitalization (8/10 carriers in the founding cohort)
- Autism-spectrum features, aggressive behavior/autoaggression, ADHD-type behavior
- Obsessive-compulsive symptoms/personality disorder
- Bipolar I disorder — reported as a possible expansion of the clinical spectrum (PMID:38646907)
- Psychosis more broadly, reviewed systematically in Colijn et al. 2024 (Prog Neuropsychopharmacol Biol Psychiatry 129:110888), which concludes LoF *SETD1A* variants "may underlie the development of psychosis in a small percentage of individuals with schizophrenia"

Suggested HPO: HP:0000708 (Behavioral abnormality); HP:0000717 (Autism); HP:0000709 (Psychosis, historically used)/HP:0031466 (or nearest available psychosis term); HP:0000722 (Obsessive-compulsive behavior)

### Craniofacial / Dysmorphic and Other Systemic Phenotypes
- Subtle facial dysmorphism (core, mild): high forehead, macrocephaly (in some), low nasal bridge, broad/short nose, thick lips, hypertelorism, upward-slanting palpebral fissures, thin face — HP:0001999 (Abnormal facial shape), HP:0000238 (Frontal bossing), HP:0000342 (Narrow nasal bridge), HP:0000316 (Hypertelorism)
- Distal limb anomalies (broad/short hands, single palmar crease, toe deformity) — HP:0001167 (Abnormality of finger), HP:0100258 (Preaxial polydactyly, N/A generically) / HP:0001760 (Abnormality of the foot)
- GI/feeding difficulties — HP:0011968 (Feeding difficulties)
- Capillary hemangioma — HP:0005605 (Capillary hemangioma)
- Rarely, congenital structural anomalies: one case reported congenital bronchomalacia, laryngeal stridor, tracheal stenosis, atrial septal defect, patent ductus arteriosus, and pulmonary hypertension **without** any seizures or developmental delay at 2-year follow-up (PMC10063285) — illustrating markedly variable expressivity even among truncating variants.

**Quality of life impact:** No disease-specific EQ-5D/SF-36 data exist. Impact is inferred from the underlying phenotypes: epilepsy (seizure-related risk/burden), intellectual disability (educational/functional impact), and psychiatric illness (frequently requiring long-term hospitalization) — collectively substantial but unquantified in validated QOL instruments.

---

## 4. Genetic/Molecular Information

**Causal gene:** *SETD1A* (HGNC:17284; NCBI Gene 9739; OMIM *611052), located at cytoband 16p11.2, chr16:30,957,294–30,984,664 (GRCh38), spanning 23 exons and encoding a 1,707-amino-acid, ~186 kDa protein. Note: this locus lies just telomeric to (and is distinct from) the classic recurrent 16p11.2 BP4-BP5 microdeletion/duplication CNV region associated with autism/schizophrenia risk; SETD1A disease is caused by intragenic point/small indel variants, not the recurrent CNV.

**Pathogenic variant spectrum:**
- **NEDSID cohort (Kummeling et al. 2021, PMID:32346159):** 14 distinct de novo heterozygous variants in 15 unrelated patients — 5 nonsense, 6 frameshift, 2 splice-site, 1 missense; all predicted to disrupt or delete the C-terminal SET catalytic domain (truncating variants correlate with more severe phenotype).
- **EPEO2 cohort (Yu et al. 2019, PMID:31197650):** Four missense variants — p.Arg913Cys (R913C, inherited in a 4-generation family), p.Gln269Arg (Q269R, de novo), p.Gly1369Arg (G1369R, de novo), p.Arg1392His (R1392H, de novo) — all previously implicated in schizophrenia/developmental-disorder cohorts, now shown to cause early-onset epilepsy.
- Additional individual case variants: p.Ser356Phe (missense, de novo; isolated epilepsy phenotype, Frontiers 2026 case, DOI 10.3389/fnins.2026.1864983); p.Glu1002Glyfs*20 (frameshift, de novo; infantile epileptic spasms, PMC10620521); p.Gly708Argfs*117 (frameshift, de novo; NEDSID-type with seizures, PMC9300109); p.Leu699Ter (nonsense, de novo; congenital cardiac/airway phenotype without epilepsy, PMC10063285).
- Recurrent hotspot: c.4582-2delAG (splice acceptor, exon 16) — found ≥7 times independently across schizophrenia/developmental-disorder cohorts (PMID:26974950).

**Variant classification:** Almost uniformly classified pathogenic/likely pathogenic per ACMG/AMP criteria (typically PVS1+PS2+PM2 for truncating de novo variants; PS2+PM2+PP3 for missense de novo variants). ClinVar entries exist per-variant (e.g., VCV000533549) but no gene-wide systematic ClinVar tabulation of counts by variant class was retrievable in this search.

**Population frequency:** SETD1A LoF variants are essentially absent from the general population (2/45,376 non-schizophrenia ExAC exomes; PMID:26974950); gnomAD constraint metrics were not directly retrievable in this search but the gene's extreme depletion of LoF variants in population data is well established and consistent with a highly LoF-intolerant gene (historically near-ceiling pLI).

**Somatic vs. germline:** All reported disease-causing variants are germline (constitutional), predominantly de novo.

**Functional consequence:** Loss of function / haploinsufficiency is the dominant mechanism for both the epilepsy (missense, partial LOF) and NEDSID (truncating, more complete LOF) ends of the spectrum — i.e., use `functional_impact_category: LOSS_OF_FUNCTION` (with `PARTIAL_LOSS_OF_FUNCTION` plausible for hypomorphic missense alleles) rather than gain-of-function or dominant-negative, though formal functional classification per-variant (e.g., dominant-negative testing) has not been systematically reported.

**Modifier genes:** None established.

**Epigenetic information:** Targeted episignature profiling (>2 million CpGs) in 6 SETD1A patients found **no strong disease-specific DNA methylation episignature** (only 7 significant differentially methylated positions, indistinguishable from controls) — a notable negative finding that contrasts with its paralog SETD2, which shows strong, subgroup-specific episignatures (PMID:37166351). This suggests SETD1A haploinsufficiency's downstream chromatin effects are not readily captured by peripheral-blood methylation arrays, despite robust effects on H3K4 methylation and, in mouse cortex, ribosomal-gene-associated DNA methylation (see Mechanism).

**Chromosomal abnormalities:** No recurrent CNV/translocation mechanism is described; disease arises from intragenic SNVs/small indels. One case report described an 852 kb CNV deletion encompassing SETD1A as a cause of the episignature-cohort phenotype (PMID:37166351).

---

## 5. Environmental Information

No environmental toxins, occupational exposures, dietary factors, or infectious triggers have been implicated in SETD1A-related disease causation or modification. This is consistent with a fully penetrant, single-gene dominant mechanism. Isolated perinatal complications noted in case reports (mild birth asphyxia, low birth weight) appear incidental rather than causally linked.

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered, from molecular lesion to seizure phenotype)

1. **A heterozygous de novo (or rarely inherited) loss-of-function or missense variant in *SETD1A*** truncates or destabilizes the SET/n-SET catalytic domain, or (for missense alleles) partially impairs catalytic/complex-assembly function → **leads to** ~50% reduction in functional SETD1A protein/complex activity (haploinsufficiency; demonstrated directly as a ~50% drop in RNA and protein in *Setd1a+/-* mice, PMID:32937141/PMC9476630).
2. **Reduced SETD1A-COMPASS activity** → **results in** globally and locally altered histone H3 lysine-4 mono-, di-, and trimethylation (H3K4me1/2/3) at enhancers, gene bodies, and promoters genome-wide (this step is directly demonstrated in cell/mouse models; PMC8595121 review).
3. **Altered H3K4 methylation at developmental and synaptic gene loci** → **branches into at least three parallel downstream pathway disruptions** (demonstrated with varying degrees of directness across model systems):
   - **3a. Neurogenesis/neural progenitor branch:** SETD1A cooperates with histone chaperone HIRA to stabilize β-catenin, hyperactivating canonical Wnt/β-catenin signaling (GO:0060070) → **promotes** neural stem/progenitor proliferation at the expense of differentiation, and SETD1A loss independently impairs cell-cycle progression (increased G1, reduced S phase) in ESCs/NSCs/iPSCs (PMC8595121) → **contributes to** altered neuronal migration timing (a missense variant, p.R913C, accelerated migration of embryonic cortical neurons to superficial layers; PMC8595121) → **disrupts** normal cortical lamination/circuit assembly (largely inferred from mouse/embryonic-electroporation data, not directly shown in human tissue).
   - **3b. Synaptic/dendritic branch:** Dysregulated expression of synaptic genes (downregulated *Homer1*, *PTPRO*, *ABI1*; upregulated *SLITRK4*) in mouse medial prefrontal cortex → **results in** reduced dendritic spine density (especially mushroom spines), reduced excitatory drive onto L2/3 pyramidal neurons (fewer functional synapses and weaker per-synapse strength), altered NMDA-receptor subunit composition, and increased short-term synaptic depression (PMID:32937141) → **produces** working-memory deficits and aberrant sensory-cortex ensemble oscillations in adult mice (PMID:31606247). In human iPSC-neuron models, the analogous perturbation instead **increases** dendritic complexity and synaptic connectivity (glutamatergic-neuron-driven), indicating that the net synaptic phenotype (hyper- vs. hypo-connectivity) is model- and developmental-stage-dependent (PMID:35508131; PMID:40962831).
   - **3c. Mitochondrial/metabolic branch:** Consistent, developmental-stage-independent downregulation of genes enriched for mitochondrial function/respiratory complex I assembly in mouse cortex, plus age-specific (peaking at E18) disruption of synaptosomal proteins including delayed Synaptotagmin-2 (Syt2) upregulation (PMID for Clifton et al. 2022: DOI 10.1093/hmg/ddac105, PMC9476630) → **parallels** reduced metabolic capacity and reduced neurite outgrowth/spontaneous activity in human iPSC-derived SETD1A+/− neurons, which is **rescued** by exogenous metabolic-intermediate supplementation (DOI 10.1038/s41537-022-00326-9, PMC9800576) → suggests bioenergetic insufficiency as a contributing, and separately targetable, downstream mechanism.
4. **Convergent network-level dysfunction in glutamatergic circuits:** In human iPSC-derived excitatory/inhibitory neuronal networks, SETD1A+/− haploinsufficiency **results in** transcriptional upregulation of adenylyl cyclase genes (*ADCY2/3/8*) and downregulation of phosphodiesterase genes (*PDE12/PDE7A/PDE1A*) → **leads to** a hyperactive cAMP/PKA pathway (elevated baseline cAMP, elevated phospho-CREB) → **causes** increased network burst rate, shortened inter-burst intervals, and elevated miniature EPSC frequency/amplitude, driven predominantly by glutamatergic (not GABAergic) neurons (PMID:35508131). This hyperexcitable, hypersynchronized network state is **directly analogous to an ictogenic circuit phenotype** and is pharmacologically **reversible**: acute PKA inhibition (H89, KT5720) or adenylyl-cyclase inhibition (SQ22536) normalizes network bursting, as does the H3K4-demethylase-pathway inhibitor ORY-1001 — the latter also rescuing cognitive/circuit deficits in adult *Setd1a+/-* mice (PMID:31606247), demonstrating the deficit is a dynamic, reversible physiological state rather than fixed structural damage.
5. **A separate, parallel epigenetic-metabolic loop** (mouse cortex): SETD1A loss-of-function **causes** widespread hypomethylation at ribosomal-protein and RNA-processing gene loci (e.g., *Rps17*, *Rpl3*; 356 hypomethylated vs. 105 hypermethylated sites; enriched for snoRNA-associated genes), a subset of which are independently enriched for common schizophrenia GWAS signal — proposed to **impair local translation capacity** at synapses, complementing rather than explaining the seizure mechanism directly (Schizophrenia Bulletin 2024/2025, DOI 10.1093/schbul/sbaf091).
6. **Net clinical output:** the combination of (a) altered progenitor proliferation/migration timing during corticogenesis, (b) synaptic/dendritic remodeling favoring excitatory network instability, and (c) a hyperactive cAMP/PKA-driven hypersynchronous network state **converges on** a cortical excitatory/inhibitory imbalance that manifests, depending on developmental timing and residual SETD1A dosage, as early-onset seizures (infancy), global developmental delay/intellectual disability (childhood), and/or later-onset psychiatric illness including schizophrenia (adolescence/adulthood) — the "single-gene, age-dependent, multi-phenotype" pattern characteristic of this locus.

**Upstream vs. downstream:** The variant itself (upstream) → chromatin/H3K4 methylation change (proximal) → transcriptional dysregulation of neurodevelopmental, synaptic, mitochondrial and cAMP-pathway genes (intermediate) → circuit-level hyperexcitability/hypersynchrony and progenitor/migration timing defects (downstream, most proximal to phenotype).

**Cell types involved:** glutamatergic (excitatory) cortical pyramidal neurons (primary driver of the network phenotype; CL:0000679 glutamatergic neuron / CL:0000598 pyramidal neuron), GABAergic interneurons (secondary/less penetrant contribution; CL:0000617 GABAergic neuron), neural stem/progenitor cells (CL:0000047 neuronal stem cell / CL:0002608 embryonic neuroepithelial progenitor cell), induced pluripotent stem cells (CL:0002248 iPSC) and embryonic stem cells (CL:0002322 ESC) used as model systems.

**Suggested GO terms:** GO:0051568 (histone H3-K4 methylation), GO:0035097 (histone methyltransferase complex), GO:0000993 (RNA polymerase II complex binding — WDR82 recruitment), GO:0060070 (canonical Wnt signaling pathway), GO:0050808 (synapse organization), GO:0007268 (chemical synaptic transmission), GO:0007612 (learning), GO:0007613 (memory), GO:0007190 (activation of adenylate cyclase activity), GO:0006119 (oxidative phosphorylation / mitochondrial respiratory chain complex I assembly).

**Suggested UBERON/CL for anatomy:** UBERON:0000956 (cerebral cortex), UBERON:0001950 (neocortex), UBERON:0002021/UBERON:0002616 (hippocampal formation, implicated via memory studies), CL:0000540 (neuron).

---

## 7. Anatomical Structures Affected

- **Organ level:** Central nervous system (brain) is the primary organ affected; secondary/associated involvement in some patients includes cardiac (atrial septal defect, patent ductus arteriosus), respiratory/airway (bronchomalacia, laryngeal stridor, tracheal stenosis), and craniofacial/skeletal structures (dysmorphic facies, distal limb anomalies) — UBERON:0000955 (brain), UBERON:0000948 (heart), UBERON:0001004 (respiratory system), UBERON:0002204 (skeletal system).
- **Tissue/cell level:** Cerebral cortex (frontal, prefrontal, visual cortex regions studied), hippocampus (memory-related H3K4me3 dynamics), affecting glutamatergic pyramidal neurons and GABAergic interneurons predominantly, plus neural progenitor populations during corticogenesis.
- **Subcellular level:** Nucleus/chromatin (site of SETD1A-COMPASS catalytic activity; GO:0000785 chromatin), dendritic spines/postsynaptic density (structural and functional synaptic changes), mitochondria (respiratory complex I and mitochondrial assembly factor disruption; GO:0005739 mitochondrion).
- **Localization:** Bilateral, diffuse cortical involvement rather than a focal lesion (consistent with normal structural MRI in many cases, e.g., the isolated-epilepsy missense case with normal brain MRI); no consistent lateralization reported, though one EEG case showed bilateral frontal/right temporal predominance.

---

## 8. Temporal Development

- **Onset:** Markedly bimodal/age-dependent. Seizure onset ranges from the first days of life to early childhood (infantile epileptic spasms as early as 6 months; focal seizures from 3 months; generalized tonic-clonic seizures up to age 3 in some reports); developmental delay and dysmorphic features are typically noted in infancy; psychiatric phenotypes (schizophrenia, OCD, bipolar disorder) emerge later, typically adolescence to adulthood.
- **Progression:** Highly variable disease course — some patients achieve seizure freedom with treatment and normal-range cognitive outcomes (DQ 108/IQ 105 in one missense case), while others have persistent developmental delay, ongoing seizures, and evolving psychiatric illness. No formal staging system exists.
- **Course pattern:** Can be episodic (seizures responding to treatment, e.g., ACTH-responsive infantile spasms with sustained remission at 10-month follow-up) or more static/stable (fixed developmental delay/dysmorphism without progressive decline); no evidence of a neurodegenerative or regressive course.
- **Critical periods:** Embryonic/early postnatal cortical development (progenitor proliferation, neuronal migration, and synaptogenesis, corresponding to mouse E14.5–P70 developmental window studied) appears to be the critical window during which SETD1A haploinsufficiency has its most durable structural impact, though functional/circuit-level deficits (working memory, network hyperexcitability) remain pharmacologically reversible into adulthood in mouse models — an important translational implication for postnatal therapeutic windows.

---

## 9. Inheritance and Population

- **Epidemiology:** No formal prevalence/incidence estimates exist. This is an ultra-rare, only recently delineated (2016 onward) gene-disease association known almost entirely from case reports and pooled sequencing-cohort ascertainment (schizophrenia exome studies, DDD study, Finnish population cohorts). Fewer than several dozen individuals with epilepsy/NEDSID-spectrum phenotypes have been reported in the literature to date.
- **Inheritance pattern:** Autosomal dominant. The great majority of reported variants are de novo; one four-generation family with an inherited missense variant (R913C) segregating with early-onset epilepsy has been reported (PMID:31197650), demonstrating that inherited transmission with variable expressivity is possible.
- **Penetrance:** Appears high for some core features (developmental delay/ID) but variable expressivity is substantial — the same or similar variant classes (even truncating LoF) can produce isolated congenital cardiac/airway anomalies without any neurodevelopmental phenotype (PMC10063285) or isolated epilepsy with normal cognition (case reports), versus severe NEDSID-spectrum disease in others.
- **Expressivity:** Markedly variable, as above; genotype-phenotype correlation is partial — truncating variants disrupting the SET domain trend toward the more severe NEDSID phenotype, while some missense variants are associated with a relatively "pure" epilepsy phenotype (EPEO2), but exceptions exist in both directions.
- **Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically documented in the retrieved literature, though as a de novo dominant disorder it is a theoretical possibility relevant to recurrence-risk counseling (not empirically quantified here).
- **Founder effects:** None reported; the recurrent c.4582-2delAG splice variant reflects a mutational hotspot (independent recurrent mutation), not a founder haplotype.
- **Consanguinity:** Not implicated (autosomal dominant, de novo mechanism).
- **Carrier frequency:** Not applicable in the classical AR sense; population LoF variant frequency is extremely low (near-absent in ExAC/gnomAD-scale reference populations).
- **Population demographics:** Cases reported from diverse populations (UK/European schizophrenia and DDD cohorts, Finnish cohorts, Chinese case series). No specific ethnic enrichment reported. Sex distribution not systematically reported as skewed, though a mouse study specifically examined sex-dependent effects of Setd1a haploinsufficiency on development and adult behavior (PMC11324134), suggesting possible sex-modulated expressivity worth noting as an open question.

---

## 10. Diagnostics

- **Laboratory tests:** No disease-specific biochemical or enzymatic biomarker exists; standard epilepsy workup (metabolic screen) is typically normal/noncontributory (as in the reported cases with normal DQ/IQ and normal MRI).
- **Genetic testing (primary diagnostic modality):**
  - Whole-exome sequencing (WES) or whole-genome sequencing (WGS) as trio analysis is the standard approach used in essentially every reported case (de novo variant confirmation), and is the recommended first-tier test given the gene's inclusion in developmental-and-epileptic-encephalopathy and intellectual-disability gene panels.
  - Targeted epilepsy/ID gene panels including *SETD1A* are increasingly available (GTR-listed).
  - Sanger sequencing used routinely for segregation/de novo confirmation in trios.
  - Chromosomal microarray (CMA) may detect the rare CNV-deletion mechanism (e.g., the 852 kb deletion reported in the episignature cohort) but will miss the majority (SNV/indel) of pathogenic variants.
  - Methylation/episignature testing is **not currently diagnostically useful** for SETD1A, in contrast to many other chromatinopathies, since no robust disease-specific episignature was identified (PMID:37166351) — an important negative finding for diagnostic-test selection.
- **Imaging:** Brain MRI is frequently normal; when abnormal, findings can include white matter dysplasia and ventricular dilation (as in one NEDSID case, PMC9300109). No pathognomonic imaging finding exists.
- **Electrophysiology:** EEG is central to phenotyping — findings range from nonspecific background slowing/sharp waves to hypsarrhythmia (in the infantile-spasms case) to focal/multifocal sharp-slow complexes; no SETD1A-specific EEG signature exists.
- **Clinical criteria:** No formal consensus diagnostic criteria exist for "SETD1A-related epilepsy" per se; diagnosis rests on (1) a compatible phenotype (early-onset seizures ± developmental delay ± dysmorphism) plus (2) molecular confirmation of a heterozygous pathogenic/likely pathogenic *SETD1A* variant (ACMG/AMP-classified).
- **Differential diagnosis:** Other monogenic developmental and epileptic encephalopathies (e.g., SCN1A/Dravet spectrum, STXBP1, SETD1B-related disorder, other chromatinopathies such as KMT2A/Kabuki-spectrum, SETD2-related Luscan-Lumish/Rabin-Pappas syndromes) and 16p11.2 microdeletion/duplication syndrome (given genomic proximity, though mechanistically distinct) should be considered and excluded by targeted or genome-wide sequencing.
- **Screening:** No population or newborn screening program exists; case-finding is exclusively through diagnostic genetic testing in symptomatic individuals.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No mortality data specific to SETD1A-related epilepsy were identified; the disorder is not reported to be associated with increased mortality in the available literature (in contrast to many severe developmental and epileptic encephalopathies).
- **Morbidity/function:** Morbidity is driven by the combination of seizure burden, intellectual disability/developmental delay (ranging from normal-range cognition to moderate ID), and — in a subset — subsequent psychiatric illness (schizophrenia, bipolar disorder, OCD) that in the founding cohort led to long-term psychiatric hospitalization in the majority of affected schizophrenia-cohort carriers.
- **Complications:** Recurrent/breakthrough seizures after initial treatment response (documented in one case), psychiatric comorbidity, and (in a minority) associated congenital structural anomalies (cardiac, airway).
- **Recovery potential:** Several reported cases achieved good seizure control (phenobarbital response, ACTH-induced remission of infantile spasms sustained at follow-up) and age-appropriate or near-normal developmental trajectories, indicating a generally favorable seizure-outcome potential for at least a subset of patients, particularly those with missense (vs. truncating) variants and isolated epilepsy phenotypes.
- **Prognostic factors:** Variant class appears to be the most consistent prognostic signal reported — truncating/SET-domain-disrupting variants trend toward more severe, multisystem NEDSID-spectrum phenotypes, while some missense variants associate with milder, more isolated epilepsy phenotypes — though exceptions exist and this correlation is not absolute.
- **Prognostic biomarkers:** None validated.

---

## 12. Treatment

**Pharmacotherapy (symptomatic, seizure control):**
- Standard antiseizure medications have been used empirically, with reported efficacy in individual cases: phenobarbital (significant reduction in seizure frequency in one focal-seizure case), valproic acid (used in combination with ACTH for infantile spasms), levetiracetam (initial seizure control in a generalized tonic-clonic seizure case, later recurrence). No SETD1A-specific antiseizure drug trial or guideline exists; treatment is empirical, following standard pediatric epilepsy/infantile-spasms protocols.
- **ACTH (adrenocorticotropic hormone)** — used per standard infantile-epileptic-spasms-syndrome protocol; achieved rapid (within 3 days) and durable (10-month) seizure freedom in the single reported SETD1A-IESS case, with prednisone substituted after 4 weeks.
- **Vitamin B6 (pyridoxine, CHEBI:16709)** — used empirically alongside ACTH in the infantile spasms case (standard practice to exclude/treat pyridoxine-dependent epilepsy pending genetic confirmation).
- NCIT term: NCIT:C15986 (Pharmacotherapy) as the general treatment_term, with `therapeutic_agent` bound to specific agents (e.g., valproic acid CHEBI:39867, levetiracetam CHEBI:6437).

**Ketogenic diet:** Not specifically reported as trialed or validated for SETD1A-related epilepsy in the retrieved literature; SETD1A is not among the genetic etiologies with an established ketogenic-diet response signature (unlike SCN1A/Dravet, TSC1/TSC2, or UBE3A/Angelman).

**Gene/precision therapy:** No gene therapy, ASO, or targeted molecular therapy currently exists or is in clinical trials for SETD1A-related disease. However, preclinical mouse work provides proof-of-concept for a mechanistically targeted approach: the LSD1/KDM1A demethylase inhibitor **ORY-1001** rescued cognitive and synaptic-circuit deficits when administered to adult *Setd1a+/-* mice (PMID:31606247), and pharmacological cAMP/PKA-pathway inhibitors (adenylyl cyclase inhibitor SQ22536; PKA inhibitors H89, KT5720) normalized hyperactive network activity in human SETD1A+/− iPSC-neuron models (PMID:35508131) — both representing candidate repurposable small-molecule strategies, though neither has reached clinical testing.

**Supportive/rehabilitative care:** Developmental/early-intervention services, speech-language therapy (NCIT:C159273), occupational/physical therapy (NCIT:C15302, NCIT:C121351), and psychiatric management (for later-emerging schizophrenia/bipolar/OCD features) are used as clinically indicated, following standard neurodevelopmental-disorder supportive-care pathways rather than a disease-specific protocol.

**Genetic counseling:** Recommended given autosomal dominant inheritance with possible germline mosaicism and documented instances of familial transmission (NCIT:C15240, Genetic Counseling).

**Experimental treatments:** No SETD1A-specific registered clinical trials (ClinicalTrials.gov) were identified in this search.

**Treatment outcomes / algorithm:** No systematic treatment-response data or standardized treatment algorithm exists; management is individualized, symptom-driven, and extrapolated from general pediatric epilepsy and neurodevelopmental-disorder practice.

---

## 13. Prevention

- **Primary prevention:** Not applicable — the disorder arises from de novo or dominantly inherited germline variants with no known preventable environmental trigger.
- **Secondary prevention / screening:** No population or targeted screening program exists. Prenatal testing (if a familial variant is known, as in the reported 4-generation family) and preimplantation genetic diagnosis would be theoretically available through standard clinical genetics pathways for at-risk families, though this was not specifically documented in the retrieved literature.
- **Tertiary prevention:** Early diagnosis via genetic testing enables early initiation of developmental support services and prompt, protocol-driven seizure treatment (e.g., ACTH for infantile spasms), which may improve developmental outcomes given the demonstrated reversibility of circuit-level deficits in animal models.
- **Genetic counseling:** The principal prevention-adjacent intervention currently available, given autosomal dominant inheritance and the possibility of parental germline mosaicism affecting recurrence risk.

---

## 14. Other Species / Natural Disease

No naturally occurring SETD1A-associated disease has been reported in non-human species (companion animals, livestock, or wildlife) in the retrieved literature; no OMIA entries or veterinary case series were identified. This is consistent with the disorder being a very recently characterized human monogenic condition studied primarily through engineered (not spontaneous) animal and cellular models.

- **Orthology:** The mouse ortholog is *Setd1a* (MGI:2446244); the *Drosophila melanogaster* ortholog is *Set1* (dSet1/kmt2f; FlyBase, studied in Kummeling et al. 2021, PMID:32346159). Both are engineered (knockout/knockdown), not natural disease models.
- **Zoonotic potential / cross-species susceptibility:** Not applicable.

---

## 15. Model Organisms

| Model | Type | Key findings | Fidelity/limitations | Reference |
|---|---|---|---|---|
| *Setd1a+/-* mouse (constitutive heterozygous knockout) | Genetic (germline heterozygous) | Reduced excitatory synaptic transmission in mPFC L2/3 pyramidal neurons, reduced spine density, altered axonal branching, working-memory deficits, aberrant visual-cortex ensemble oscillations; deficits reversible in adulthood by LSD1 inhibitor ORY-1001 | Recapitulates cognitive/synaptic schizophrenia-relevant phenotypes; germline model may not capture developmental-timing-specific effects of a true haploinsufficient human genotype; epilepsy/seizure phenotype not directly reported in this model (behavioral/synaptic focus, not seizure monitoring) | PMID:31606247, PMID:32937141 |
| *Setd1a+/-* mouse (multi-omics developmental time-course, E14.5–P70) | Genetic | Consistent downregulation of mitochondrial-pathway genes across all ages; age-specific (peak E18) synaptosomal protein disruption (delayed Syt2 upregulation); widespread ribosomal-gene-associated DNA hypomethylation enriched for schizophrenia GWAS genes | Establishes developmental critical window and metabolic/epigenetic mechanism; again schizophrenia/synaptic-focused rather than seizure-focused | PMC9476630 (DOI 10.1093/hmg/ddac105); Schizophrenia Bulletin DOI 10.1093/schbul/sbaf091 |
| *Setd1a+/-* mouse — sex-dependent effects study | Genetic | Examines whether developmental/behavioral phenotypes differ by sex | Directly relevant to potential sex-modulated expressivity noted in humans; details of sex-specific findings not fully extracted in this search | PMC11324134 |
| *Drosophila melanogaster* dSet1/kmt2f knockdown | Genetic (RNAi/mutant, invertebrate) | dSet1 required specifically in postmitotic adult neurons for normal memory formation, complementing developmental phenotypes seen with germline loss | Confirms an evolutionarily conserved postmitotic/adult-brain requirement for SETD1A-family function, independent of any developmental confound; invertebrate nervous system has obvious translational limits (no cortical lamination, no direct seizure correlate) | PMID:32346159 |
| Human iPSC-derived neurons (isogenic CRISPR SETD1A+/− pairs, glutamatergic/GABAergic co-cultures) | Cellular (human, in vitro) | Increased dendritic complexity, increased network bursting/hypersynchrony driven by glutamatergic neurons, hyperactive cAMP/PKA signaling (elevated ADCY2/3/8, reduced PDE12/7A/1A, elevated cAMP and pCREB), rescued by PKA/adenylyl-cyclase inhibitors and ORY-1001 | Directly models human genotype and is the most epilepsy-mechanism-relevant system to date (network hyperexcitability/hypersynchrony is directly analogous to an ictogenic phenotype), but is a 2D dissociated-culture system lacking whole-brain circuit context, and derives from an exon-16 truncating genotype rather than the missense EPEO2 alleles specifically | PMID:35508131 (Cell Reports 2022); PMID:40962831 (Mol Psychiatry 2025, exon-16 premature-termination isogenic pairs) |
| Human iPSC-derived neurons — metabolic/mitochondrial study | Cellular (human, in vitro) | Reduced neurite outgrowth and spontaneous activity, altered metabolic capacity; rescued by metabolic-intermediate supplementation | Complements mouse mitochondrial-pathway findings; again schizophrenia-phenotype-focused | PMC9800576 (DOI 10.1038/s41537-022-00326-9) |
| Embryonic mouse cortex in utero electroporation (p.R913C missense variant) | Induced/genetic (mosaic overexpression) | Accelerated neuronal migration to superficial cortical layers | Directly tests a human EPEO2 missense allele in a developmental migration assay; mosaic overexpression paradigm differs from constitutive heterozygosity | Referenced in PMC8595121 review |

**Overall model-system summary:** No single model currently recapitulates the full human triad of early-onset seizures + developmental delay + later psychiatric illness. Mouse germline knockouts best capture the synaptic/cognitive and mitochondrial/epigenetic axes; human iPSC-neuron networks best capture the network-hyperexcitability axis most directly relevant to seizure genesis; Drosophila establishes a conserved postmitotic neuronal requirement. A model with directly recorded electrographic seizures (EEG-monitored in vivo) attributable to *Setd1a* haploinsufficiency was not identified in this search and represents a notable gap for future work — this is a `HUMAN_MODEL_MISMATCH`-type gap worth flagging explicitly in a dismech entry (mouse/iPSC evidence strongly supports a hyperexcitable-network mechanism, but translational confirmation via a genuine in vivo seizure/EEG phenotype in the mouse model is not yet reported).

---

## Summary Table of Suggested Ontology Bindings

| Category | Term |
|---|---|
| Gene | HGNC (hgnc:17284, SETD1A) |
| Disease (OMIM) | #618832 EPEO2; #619056 NEDSID |
| Key phenotypes (HPO) | HP:0001250 Seizure; HP:0002069 Bilateral tonic-clonic seizure; HP:0011097 Epileptic spasm; HP:0012469 Infantile spasms; HP:0001263 Global developmental delay; HP:0001249 Intellectual disability; HP:0000750 Delayed speech and language development; HP:0001252 Hypotonia; HP:0001999 Abnormal facial shape; HP:0000717 Autism; HP:0000708 Behavioral abnormality; HP:0000722 Obsessive-compulsive behavior; HP:0002353 EEG abnormality |
| Biological processes (GO) | GO:0051568 histone H3-K4 methylation; GO:0035097 histone methyltransferase complex; GO:0060070 canonical Wnt signaling pathway; GO:0050808 synapse organization; GO:0007268 chemical synaptic transmission; GO:0007190 activation of adenylate cyclase activity |
| Cell types (CL) | CL:0000679 glutamatergic neuron; CL:0000598 pyramidal neuron; CL:0000617 GABAergic neuron; CL:0000047 neuronal stem cell |
| Anatomy (UBERON) | UBERON:0000955 brain; UBERON:0000956 cerebral cortex; UBERON:0002616 hippocampal formation |
| Chemicals (CHEBI) | CHEBI:39867 valproic acid; CHEBI:6437 levetiracetam; CHEBI:16709 pyridoxine (vitamin B6) |
| Treatments (NCIT) | NCIT:C15986 Pharmacotherapy; NCIT:C15302 Physical Therapy; NCIT:C159273 Speech Therapy; NCIT:C15240 Genetic Counseling |

---

## Key Evidence Citations (PMID, with supporting quotes)

- **PMID:26974950** — Singh et al., *Nature Neuroscience* 2016. "Rare loss-of-function variants in SETD1A are associated with schizophrenia and developmental disorders." Founding statistical association (Fisher's combined P = 3.3×10⁻⁹); establishes gene constraint and initial developmental-disorder/epilepsy signal.
- **PMID:31197650** — Yu et al., *Neuroscience Bulletin* 2019. "De Novo and Inherited SETD1A Variants in Early-onset Epilepsy." Defines the EPEO2 missense-variant phenotype (R913C/Q269R/G1369R/R1392H) and underlying OMIM #618832.
- **PMID:32346159** — Kummeling et al., *Molecular Psychiatry* 2021. "Characterization of SETD1A haploinsufficiency in humans and Drosophila defines a novel neurodevelopmental syndrome." Defines NEDSID (OMIM #619056) in 15 patients with 14 distinct truncating/splice/missense variants; Drosophila memory phenotype.
- **PMID:37166351** — Lee et al., *Human Molecular Genetics* 2023. Episignature study showing no strong SETD1A-specific methylation signature (contrast with SETD2).
- **PMID:31606247** — Mukai et al., *Neuron* 2019. Reversible cognitive/synaptic deficits in *Setd1a*-deficient mice; ORY-1001 rescue.
- **PMID:32937141** — Nagahama et al., *Cell Reports* 2020. Attenuated excitatory synaptic function and schizophrenia-related behaviors in *Setd1a+/-* mice.
- **PMID:35508131** — Wang et al., *Cell Reports* 2022. cAMP/PKA-pathway hyperactivity and pharmacological network-activity rescue in human SETD1A+/− iPSC-neurons.
- **PMID:40962831** — Su et al., *Molecular Psychiatry* 2025. Synaptic transmission/plasticity dysregulation in isogenic human iPSC-neurons with exon-16 SETD1A truncating variants.
- **PMID:38646907** — Case report/meta-analysis expanding the SETD1A clinical spectrum to bipolar I disorder.
- Case reports: Frontiers 2026 (DOI 10.3389/fnins.2026.1864983, isolated epilepsy, p.S356F); PMC10620521/*Frontiers in Neurology* 2023 (DOI 10.3389/fneur.2023.1278035, first infantile-spasms case, p.Glu1002Glyfs*20); PMC9300109 (NEDSID with seizures, p.Gly708Argfs*117); PMC10063285 (congenital cardiac/airway phenotype without epilepsy, p.Leu699Ter).

**Data gaps flagged for curation:** No formal prevalence/incidence figures; no gene-wide ClinVar variant-count tabulation retrieved; no in vivo (EEG-confirmed) mouse seizure model; no SETD1A-specific clinical trial or ketogenic-diet response data; MONDO ID not directly confirmed in this search and should be verified against the MONDO release before entry creation.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 21 |
| On topic | 18 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:26974950` *(abstract only)*: "among the 3% most constrained genes in the human genome"
  - closest text in source: "By analyzing the whole-exome sequences of 4,264 schizophrenia cases, 9,343 controls and 1,077 trios, we identified a genome-wide significant association between rare loss-of-function (LoF) variants in SETD1A and risk for schizophrenia (P = 3.3 × 10(-9))"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 63 |
| Resolved | 58 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 37 |
| Terms named correctly | 27 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000238` (1 mention) - the report calls it "Frontal bossing"; HP calls it **Hydrocephalus**
- `HP:0005605` (1 mention) - the report calls it "Capillary hemangioma"; HP calls it **Large cafe-au-lait macules with irregular margins**
- `GO:0006119` (1 mention) - the report calls it "oxidative phosphorylation / mitochondrial respiratory chain complex I assembly"; GO calls it **oxidative phosphorylation**
- `UBERON:0002616` (2 mentions) - the report calls it "hippocampal formation, implicated via memory studies"; UBERON calls it **regional part of brain**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000342` (1 mention), reported as "Narrow nasal bridge" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0051568` (obsolete histone H3-K4 methylation) (2 mentions)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002384` (1 mention) - the report calls it "Focal-onset seizure"; HP calls it **Focal impaired awareness seizure**, and lists "Focal dyscognitive seizure" among its other names
- `HP:0000709` (1 mention) - the report calls it "Psychosis, historically used"; HP calls it **Psychosis**
- `HP:0100258` (1 mention) - the report calls it "Preaxial polydactyly, N/A generically"; HP calls it **Preaxial polydactyly**
- `GO:0051568` (2 mentions) - the report calls it "histone H3-K4 methylation"; GO calls it **obsolete histone H3-K4 methylation**, and lists "histone H3 K4 methylation" among its other names
- `GO:0000993` (1 mention) - the report calls it "RNA polymerase II complex binding — WDR82 recruitment"; GO calls it **RNA polymerase II complex binding**
- `UBERON:0002204` (1 mention) - the report calls it "skeletal system"; UBERON calls it **musculoskeletal system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MGI:2446244` - called "Setd1a", "Orthology:** The mouse ortholog is *Setd1a"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.