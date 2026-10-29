---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-10-29T05:19:14.426799'
end_time: '2026-10-29T05:26:03.195762'
duration_seconds: 408.77
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Familial Encephalopathy With Neuroserpin Inclusion Bodies
  mondo_id: MONDO:0011412
  category: Mendelian
  causal_genes: SERPINI1
  omim_id: OMIM:604218
  synonyms: FENIB
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
  web_search_requests: 7
  num_turns: 44
  total_cost_usd: 3.1760171
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 6
citation_count: 6
reference_validation:
  total_references: 43
  verified: 43
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 3
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:15291813
  relevance_assessed: 43
  on_topic: 36
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 51
  verified: 48
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 6
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0011412
    reported_labels:
    - MONDO
    ontology_label: familial encephalopathy with neuroserpin inclusion bodies
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Encephalopathy With Neuroserpin Inclusion Bodies
- **MONDO ID:** MONDO:0011412 (if available)
- **Causal gene(s):** SERPINI1
- **OMIM:** OMIM:604218
- **Synonyms:** FENIB
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Familial Encephalopathy With Neuroserpin Inclusion Bodies** covering all of the
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

Stub entry. Let me read the cached abstracts.

I'm pulling PubMed titles and abstracts for the core FENIB papers so the report has checked citations.

I've collected the core clinical and genetic papers. Now I'm filling a few gaps: the model studies and therapy citations. Then I'll write the report.

# Familial Encephalopathy With Neuroserpin Inclusion Bodies (FENIB): Research Report

**Scope.** This report covers MONDO:0011412 / OMIM:604218. The causal gene is **SERPINI1**, also called *PI12*. It encodes neuroserpin, a serine protease inhibitor made mainly in neurons.

**About the existing entry.** `kb/disorders/Familial_Encephalopathy_With_Neuroserpin_Inclusion_Bodies.yaml` is still a stub. It has one pathophysiology node and one phenotype (Dementia), and no evidence.

**About the quotes.** Every quote below came through NCBI or Europe PMC web interfaces and was capped at 125 characters. Most are sentence fragments. None has been checked against `references_cache/` yet. Before using any of them as a `snippet:`, run `just fetch-reference PMID:…` and then `just count-verified-snippets`.

**About ontology IDs.** Labels were checked against the repo's `cache/*/terms.csv` where a row existed. IDs marked **(verify)** were not in any cache and must be looked up before binding.

---

## 1. Disease Information

**Overview.** FENIB is a rare autosomal dominant neurodegenerative disease. It is a "serpinopathy": a missense variant in SERPINI1 makes neuroserpin unstable, so it polymerizes inside the endoplasmic reticulum (ER) of neurons. The polymers build up as eosinophilic, PAS-positive, diastase-resistant inclusions called **Collins bodies**. Clinically, the disease ranges from:
- presenile dementia of the frontal (dysexecutive) type, starting in the 40s–50s, to
- childhood or adolescent progressive myoclonus epilepsy (PME) with fast cognitive decline.

How severe and how early the disease is tracks how strongly each variant destabilizes the protein.

- Davis et al. 1999, Nature (PMID:10517635), described a disease "characterized clinically as an autosomal dominantly inherited dementia", "histologically by unique neuronal inclusion bodies" and "biochemically by polymers of the neuron-specific serpin, neuroserpin."
- Roussel et al. 2016, Epileptic Disord (PMID:27618835): "Familial encephalopathy with neuroserpin inclusion bodies (FENIB) is a conformational proteinopathy"… "Presenting clinically as a familial dementia-epilepsy syndrome".

**Identifiers**

| Resource | ID | Note |
|---|---|---|
| MONDO | MONDO:0011412 | Matches the entry's `disease_term` |
| OMIM | 604218 | |
| Orphanet | ORPHA:85110 | Taken from aggregators (PhenoDis, GARD); confirm in the Orphadata cache with `just fetch-reference ORPHA:85110` |
| MedGen / GTR | C1858680 | |
| GARD | 10037 | |
| ICD-10 / ICD-11 | No specific code | MedlinePlus lists none; G31.8 or a PME code would only be a broad match |
| MeSH | No dedicated descriptor | Indexed under "Serpins/genetics", "Neuroserpin", "Myoclonic Epilepsies, Progressive" |

**Synonyms** (MedlinePlus): FENIB; familial dementia with neuroserpin inclusion bodies; neuroserpin encephalopathy; neuroserpinosis; progressive myoclonus epilepsy associated with neuroserpin inclusion bodies; encephalopathy, familial, with Collins bodies.

**Where the information comes from.** Almost everything is case reports and family studies, about 15–20 families or sporadic cases in total, plus experimental models. There is no registry or EHR-based cohort.

---

## 2. Etiology

**Cause.** The cause is a heterozygous missense variant in SERPINI1 (3q26.1). The variant changes the shear or breach region of the serpin fold, so the protein forms loop–sheet polymers. Davis 1999 (PMID:10517635) reported "the cosegregation of point mutations in the neuroserpin gene (PI12) with the disease in two families". Both of the first variants sit in the "shutter" domain.

**Genetic risk factors.** The only established genetic factor is the causal SERPINI1 variant. No modifier genes or GWAS loci have been reported. A *SERPINI1–PDCD10* bidirectional promoter is described (PMID:17212813), but it has no known role in FENIB. Common SERPINI1 polymorphisms have been studied for stroke risk, with negative or inconclusive results (PMID:17961231, PMID:21487809); they are not relevant to FENIB.

**Environmental risk factors, protective factors, gene–environment interactions.** None reported. Two experimental observations suggest age matters:
- In *C. elegans*, ageing interacts with ER overload to drive aggregation (Schipanski 2013, PMID:23335331).
- In mice, accumulation of G392E neuroserpin depends on age and gene dosage (Takasawa 2008, PMID:18940798).

---

## 3. Phenotypes

The best frequency data come from Yang et al. 2022, Seizure (PMID:36417830): one new case plus 13 earlier cases.
- "All the patients presented with myoclonus, and 12 patients had experienced at least one other type of seizure."
- "Progressive cognitive decline was observed in all the patients, and 10 out of 13 patients had dyskinesia."
- "9 out of 12 patients did not respond to ASMs."

This review leans toward the PME/early-onset end of the spectrum, so adult-onset dementia families (for example Syracuse) are under-represented in these percentages.

| Phenotype | HPO (cache-checked) | Onset / course | Frequency | Key source |
|---|---|---|---|---|
| Dementia / progressive cognitive decline | HP:0000726 Dementia; HP:0034332 Cognitive regression | Childhood to 5th–6th decade; progressive | 100% (14/14 in Yang review) | PMID:10595921, PMID:36417830 |
| Frontal / dysexecutive syndrome: inattention, poor response regulation, recall relatively spared | HP:0000734 Disinhibition; HP:0000751 Personality changes; HP:0002354 Memory impairment (relatively spared) | Often the first sign | Common in adult-onset families | PMID:11559315, PMID:17606885, PMID:38166833 |
| Myoclonus / progressive myoclonus epilepsy | HP:0001336 Myoclonus; HP:0002123 Generalized myoclonic seizure | Childhood to adolescence in severe variants | 100% in Yang review | PMID:36417830, PMID:17606885 |
| Other seizures (generalized tonic-clonic, focal) | HP:0001250 Seizure; HP:0007359 Focal-onset seizure | Progressive, often drug-resistant | 12/13 | PMID:36417830 |
| Status epilepticus, including electrical status epilepticus during slow sleep (ESES/CSWS) | HP:0002133 Status epilepticus | Juvenile (G392R) | Rare | PMID:18591508 (no abstract; MeSH only) |
| Dyskinesia / involuntary movements | HP:0100660 Dyskinesia | | 10/13 | PMID:36417830 |
| Tremor, dysarthria | HP:0001337; HP:0001260 | Advanced disease | Occasional (case-level) | MedlinePlus; case reports |
| Psychiatric presentation (psychosis, catatonia) | HP:0000709 Psychosis | | Case report | PMID:39257502 (catatonia) |
| Cerebral cortical atrophy | HP:0002120; HP:0002283 Global brain atrophy | Late | Seen in the most severe cases | PMID:11559315 |
| Neuronal loss / gliosis (pathology) | HP:0002529; HP:0002171 | | Autopsy | PMID:10595921 |

Supporting quotes:
- Bradshaw 2001 (PMID:11559315): deficits in "restricted attention, concentration, and response regulation functions"; "In general, recall memory was not as affected as other cognitive domains."; "The MRI findings were noncontributory except in the 2 most severe cases, which showed global cortical atrophy."
- Gourfinkel-An 2007 (PMID:17606885): "progressive myoclonic epilepsy was associated with a frontal syndrome."
- Handa 2024 (PMID:38166833), case report: an H338R carrier aged 23 had inattention and disinhibition before myoclonic epilepsy, with ventromedial prefrontal grey-matter loss on voxel-based morphometry.

**Quality of life.** No EQ-5D or SF-36 data exist. The impact can be inferred: progressive loss of independence, drug-resistant seizures, and shortened life expectancy. MedlinePlus lists status epilepticus and pneumonia as causes of death.

---

## 4. Genetic / Molecular Information

**Gene.** SERPINI1 (neuroserpin; OMIM gene *602445). The HGNC ID was **not** in `cache/hgnc/terms.csv`, so look it up (**verify**); do not copy one from memory. The UniProt accession, Q99574, also needs a lookup.

**Pathogenic variants.** All are heterozygous missense changes. They are germline, or de novo germline. All polymerize.

| Variant (protein) | Name | Typical presentation | Source |
|---|---|---|---|
| p.Ser49Pro (S49P) | Syracuse | Mildest: dementia "after age 45 years" | PMID:10517635, PMID:12103288 |
| p.Ser52Arg (S52R) | Portland | Earlier onset; dementia with PME; frontal syndrome | PMID:10517635, PMID:17606885, PMID:15291813 |
| p.His338Arg (H338R) | — | Adolescent or young-adult PME with frontal deficits | PMID:12103288, PMID:38166833 |
| p.Gly392Glu (G392E), c.1175G>A | — | Most severe: PME "at age 13 years"; can be de novo | PMID:12103288, PMID:36417830 |
| p.Gly392Arg (G392R) | — | Juvenile; ESES/CSWS at age 11 (from secondary sources) | PMID:18591508 |
| p.Leu47Pro (L47P) | — | PME and cognitive decline from age 26; death at 34 | PMID:21435071 (Hagen 2011) |

- Davis 2002 (PMID:12103288): "the most severely disruptive mutation (G392E)"; "The least disruptive of these mutations (S49P)".
- Yang 2022 (PMID:36417830): "a de novo heterozygous c.1175G>A (p.G392E) variant of the SERPINI1 gene", called pathogenic under ACMG criteria.
- Ansari 2022 (PMID:36408789) describes a strand-1A variant with more aggregation and no loss of inhibition, but it is in vitro only and its disease link is uncertain.

**Variant classification and frequency.** The listed variants are absent or ultra-rare in population databases (expected for a dominant disease; check gnomAD and ClinVar per variant). Population-screen variants of uncertain pathogenicity are discussed in D'Acunto 2021 (PMID:34405255).

**Functional consequence.** The main effect is toxic gain of function: the protein misfolds and polymerizes, which is a conformational change, not a new activity. There is a secondary partial loss of function: polymerized or latent neuroserpin cannot inhibit tissue plasminogen activator (tPA). For example, Portland neuroserpin "is trapped as an inactive intermediate that rapidly forms polymers" (PMID:15291813). For the KB:
- Use `functional_impact_category: GAIN_OF_FUNCTION` only after careful thought; the literature frames this as a "conformational / dominant toxic" mechanism.
- A `NEOMORPHIC` or `DOMINANT_NEGATIVE` label is not established. Heteropolymers with wild-type protein are possible, but that has not been shown in patients.

**Modifier genes, epigenetics, chromosomal abnormalities.** None reported.

---

## 5. Environmental Information

There are no known environmental, lifestyle or infectious contributors. The environmental section should stay empty. It needs no "Left deliberately uncited" waiver unless an `environmental[]` item is added.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **heterozygous SERPINI1 missense variant** (shutter or breach region: S49P, S52R, L47P, H338R, G392E, G392R) **destabilizes the neuroserpin fold**, making it easy for the protein to open β-sheet A (PMID:10517635, PMID:15664988).
2. Destabilized neuroserpin **forms loop–sheet polymers in the ER** soon after it is made, instead of being secreted (in vitro, PMID:15090543: "Mutant neuroserpin is retained within the endoplasmic reticulum as polymers"). S49P can also form a latent conformer that then polymerizes (PMID:15664988).
3. **Branch A (gain of toxicity):**
   - 3a. Polymers are partly cleared by **ERAD**, via the lectin OS-9 and Hrd1 and the proteasome (PMID:24795221; PMID:21507957), and partly by ER-to-lysosome-associated degradation (PMID:42569303; PMID:18940798). Sterol/SREBP signaling controls polymer degradation (PMID:23814041).
   - 3b. When clearance is outpaced, which is age- and dose-dependent, polymers **accumulate as Collins bodies** (PMID:17392169, PMID:18940798).
   - 3c. Accumulation triggers an **ER overload response** — a Ca²⁺-dependent **NF-κB activation** — **without a canonical unfolded protein response** (cells: PMID:35864382, PMID:23814041). In Tg-Syracuse mice the UPR is only limited, possibly because GRP78 and GRP94 are trapped in the inclusions (PMID:26733586).
   - 3d. Polymer load disrupts **ER–mitochondria contacts and mitochondrial membrane potential**, and adds oxidative stress (PMID:35864382; Guadagno 2017, a neural progenitor model).
   - 3e. These lead to **neuronal dysfunction and loss** in cortex and subcortical nuclei. Davis 2002 (PMID:12103288) concluded "inclusion-body formation is in itself a sufficient cause of neurodegeneration". The intermediate steps from 3c–3d to neuron death in humans are **inferred** from cell and mouse data.
4. **Branch B (loss of inhibition, inferred):** retained or inactive neuroserpin reduces the neuroserpin available to inhibit **tPA** at synapses, so tPA activity is left unchecked. This is thought to add to cortical hyperexcitability and seizures (PMID:27618835: "caused by loss of protease inhibition"; PMID:15291813). Supporting points: G392E mice are "much more susceptible to seizures induced by kainate administration" (PMID:18940798). Extracellular G392E polymers are **not** synaptotoxic (PMID:33888787), which points toward intracellular toxicity plus loss of function.
5. Cortical (especially frontal) and subcortical neuronal dysfunction → **frontal-dysexecutive dementia**. Cortical hyperexcitability → **myoclonus, PME and status epilepticus**.
6. **Severity and onset follow polymerization rate.** Davis 2002 (PMID:12103288): "the onset and severity of the disease is associated with the rate and magnitude of neuronal protein aggregation." Miranda 2008 (PMID:18267959): "We show a direct correlation between the severity of the disease-causing mutation" and how much accumulates.

### Checklist

| Aspect | Content | Suggested term |
|---|---|---|
| Protein dysfunction | Serpin misfolding and loop–sheet polymerization; latent conformer (S49P) | GO:0051258 protein polymerization (cache-checked); GO:0006457 protein folding |
| Molecular function lost | Serine protease (tPA) inhibition | GO:0004867 serine-type endopeptidase inhibitor activity (`modifier: DECREASED`) |
| Proteostasis | ERAD; lysosomal degradation; ER stress without UPR | GO:0036503 ERAD pathway; GO:0034976 response to endoplasmic reticulum stress |
| Signaling | Ca²⁺ → NF-κB via the ER overload response | GO:0043123 positive regulation of canonical NF-kappaB signal transduction (`modifier: INCREASED`) |
| Organelles | ER lumen, lysosome, inclusion body, mitochondria | GO:0005783, GO:0005788, GO:0005764, GO:0016234, GO:0007005 mitochondrion organization |
| Physiological role | Axogenesis, synaptic plasticity, neurite outgrowth | GO:0031175 neuron projection development (PMID:35244780) |
| Immune / inflammation | Limited inflammation in mice | PMID:26733586 |
| Cell types | Neurons, cortical and subcortical | CL:0000540 neuron (cache-checked). Cortical pyramidal neurons and substantia nigra neurons need a lookup |
| Omics | No patient transcriptomic or proteomic datasets found. Proteomics exists only for neuroserpin-*deficient* mice (PMID:38535505; not FENIB) | — |
| Functional genomics | Patient iPSC neurons with adenine base-editing correction (PMID:39877004) | — |

---

## 7. Anatomical Structures Affected

**Organ and system.** The central nervous system only; no systemic involvement. Secondary complications include aspiration pneumonia.

**Regions.**
- Davis 1999 (PMID:10595921): inclusions "distributed throughout the gray matter of the cerebral cortex".
- Gourfinkel-An 2007 (PMID:17606885): Collins bodies "abundant in the frontal cortex" and caudate, "but spared the cerebellum."
- D'Acunto 2021 (PMID:34405255): inclusions also in the substantia nigra, spinal cord and dorsal root ganglia.

| Site | UBERON (cache-checked) |
|---|---|
| Cerebral cortex | UBERON:0000956 |
| Frontal cortex | UBERON:0001870 |
| Caudate nucleus | UBERON:0001873 |
| Substantia nigra | UBERON:0002038 |
| Spinal cord | UBERON:0002240 |
| Dorsal root ganglion | UBERON:0000044 |
| Cerebellum (largely spared) | UBERON:0002037 |

**Subcellular.** ER (polymers), lysosomes (G392E in mice), and mitochondria–ER contacts.

**Laterality.** Bilateral and symmetric.

---

## 8. Temporal Development

**Onset.** From about 8–13 years (G392E, G392R) to 40s–60s (S49P). Davis 1999 says the disease presents "clinically in the fifth decade". Onset is insidious.

**Course.** Relentlessly progressive and lifelong. Disease duration is shorter with early onset:
- L47P: onset 26, death 34 (PMID:21435071).
- Mouse inclusions accumulate "long before the development of clinical symptoms" (PMID:17392169), which points to a presymptomatic window when anti-polymerization therapy might help (inferred).

**Remission.** None reported.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant (HP:0000006, cache-checked). Sporadic cases come from de novo variants (PMID:36417830).
- **Penetrance:** appears high and age-dependent. In the Syracuse family, cognitive changes were greatest in carriers over 40 (PMID:11559315). No formal estimate exists.
- **Expressivity:** varies between variants, but is fairly consistent within a family.
- **Anticipation:** none (not a repeat expansion). **Founder effects:** none described. **Germline mosaicism:** not reported.
- **Prevalence:** unknown. MedlinePlus says at least 13 individuals reported; Orphanet says more than 5 families.
  - Suggested KB record: `measure_type: CASES_IN_LITERATURE`, `prevalence_class: ULTRA_RARE`.
  - GARD's "about 1,000 US cases" estimate is unsourced and should not be used.
- **Populations:** USA (New York State and Oregon kindreds), France, Belgium, Japan, China and others. No ethnic predilection. Sex ratio: Yang's review had 9 of 13 male, too few to mean anything.
- D'Acunto 2021 notes FENIB is likely under-diagnosed, because late-onset cases can be mistaken for senile dementia.

---

## 10. Diagnostics

**Genetic testing.** The confirmatory test is single-gene SERPINI1 sequencing, a PME/epilepsy gene panel, or exome sequencing. Yang 2022: "gene detection and brain biopsy are important means for the diagnosis of FENIB." CMA, karyotype, FISH, mtDNA and repeat testing are not relevant, except to rule out other PME causes.

**Pathology.** Brain biopsy or autopsy shows eosinophilic, PAS-positive, diastase-resistant neuronal inclusions that are immunopositive for neuroserpin (PMID:21435071: "The inclusions were immunopositive for antibodies raised against neuroserpin."). Monoclonal antibodies specific to polymeric neuroserpin exist (PMID:18267959).

**EEG.** Generalized epileptiform discharges and photoparoxysmal responses (case level). ESES has been reported with G392R.

**Imaging.**
- MRI is often normal early; global or frontal atrophy appears late.
- Voxel-based morphometry can show early ventromedial prefrontal loss (PMID:38166833).
- SPECT shows frontal hypoperfusion in milder cases and widespread hypoperfusion in severe cases (PMID:11559315).

**Biomarkers.** No validated fluid biomarker. CSF neuroserpin has been measured in AD/DLB (PMID:38850771), not in FENIB. No LOINC code is disease-specific.

**Differential diagnosis.**
- Other PMEs: Unverricht–Lundborg (*CSTB*), Lafora disease, NCLs, MERRF, sialidosis, *KCNC1*.
- Early-onset frontotemporal dementia and early-onset Alzheimer disease.
- Inclusion-body disorders: Lafora bodies are polyglucosan and stain PAS-positive too, but are not neuroserpin-positive.

**Screening.** Cascade testing of at-risk relatives with genetic counseling. No population or newborn screening.

---

## 11. Outcome / Prognosis

- **Life expectancy:** shortened, especially with early onset. Death can come within about 8–10 years of onset in juvenile and young-adult forms (L47P case). Causes are status epilepticus and pneumonia (MedlinePlus).
- **Morbidity:** progressive dependence and drug-resistant epilepsy (9/12 did not respond to antiseizure drugs, PMID:36417830).
- **Prognostic factor:** genotype, through how strongly it destabilizes the protein (S49P mildest, G392E most severe; PMID:12103288, PMID:27618835).
- No survival statistics or QoL instrument data exist.

---

## 12. Treatment

**Current care is symptomatic only** (PMID:34405255). No drug is approved for FENIB.

| Treatment | Notes | NCIT / CHEBI (cache-checked) |
|---|---|---|
| Antiseizure medication: valproate, levetiracetam, clonazepam, perampanel, piracetam | Often only partly effective for myoclonus; generic PME practice (PMID:41817056, already in references_cache) | NCIT:C15986 Pharmacotherapy + `therapeutic_agent` CHEBI:39867 valproic acid, CHEBI:6437 levetiracetam, CHEBI:3756 clonazepam, CHEBI:71013 perampanel, CHEBI:32010 Piracetam |
| Supportive and palliative care; aspiration prevention | | NCIT:C15747 Supportive Care |
| Genetic counseling | AD, 50% recurrence risk | NCIT:C15240 Genetic Counseling |

**Experimental and preclinical approaches** (none in clinical trials; no NCT identifiers found):
- **Embelin** and derivatives inhibit polymerization and break up existing polymers. Saga 2016 (PMID:26732982): "NS polymers disaggregate in the presence of EMB, and their formation is prevented." Optimization work: Visentin 2020 (PMID:32664592).
- **EGCG** binding to S52R neuroserpin (PMID:41866009, in vitro).
- **Personalized adenine base editing** in patient iPSC neurons (PMID:39877004): "ABE-treated MUT NS-GFP cells demonstrated reduced inclusion size and number."
- **Enhancing clearance** through sterol/SREBP signaling and ERAD (PMID:23814041, PMID:24795221). An inducible neural stem cell platform for drug testing exists (PMID:39749681).
- Chemical chaperones from α1-antitrypsin research have not been tested in FENIB models in vivo.

**Pharmacogenomics.** Not applicable.

---

## 13. Prevention

- **Primary:** none.
- **Reproductive options:** genetic counseling; prenatal testing or PGT-M for a known familial variant.
- **Secondary:** presymptomatic testing of relatives with counseling. There is no disease-modifying treatment yet.
- **Tertiary:** seizure control, prevention of status epilepticus, and aspiration precautions.
- **Vaccination, public health and environmental measures:** not applicable.

---

## 14. Other Species / Natural Disease

No naturally occurring FENIB is recorded in animals (OMIA search not done; nothing turned up incidentally). Neuroserpin is conserved across vertebrates: mouse *Serpini1*, zebrafish *serpini1* (knockouts show axon-extension defects and anxiety, PMID:33168193). Not zoonotic.

The serpin polymerization mechanism is shared with human α1-antitrypsin Z deficiency: the polymers have the same morphology as hepatocyte α1-antitrypsin polymers (PMID:34405255). This links FENIB to a possible "serpinopathy" mechanism module.

---

## 15. Model Organisms

| Model | Genotype | What it recapitulates | Limitations | Source |
|---|---|---|---|---|
| Mouse (Tg) | Neuron-specific human S49P or S52R | Intraneuronal inclusions "composed exclusively of mutant neuroserpin", building up before symptoms; symptoms and inclusion load "correlated with the predicted instability of the protein" | Overexpression transgene, not a knock-in | PMID:17392169 |
| Mouse (Tg) | Human G392E | Age- and dose-dependent accumulation in ER and lysosomes, only in homozygous lines; kainate seizure susceptibility | Needs high expression | PMID:18940798 |
| Mouse (Tg-Syracuse) | S49P | Limited UPR and inflammation | | PMID:26733586 |
| Drosophila | Mutant neuroserpin | "mutant neuroserpin causes locomotor deficits in the fly"; accumulation tracks severity | Invertebrate; overexpression | PMID:18267959 |
| *C. elegans* | SRP-2 H302R (FENIB-analogous)

My report was

The report was delivered through section 14 and most of section 15. Let me finish the remaining pieces cleanly.

## 15. Model Organisms (continued)

Additional systems beyond the mouse and *Drosophila* models already listed:

- ***C. elegans*** — a FENIB-analogous SRP-2 variant forms aggregates; loss of HSF-1 and UPR components worsens it, and ageing interacts with ER overload (Schipanski 2013, PMID:23335331 / PMID:23814041 context).
- **Yeast** — a *FENIB yeast model* reproduces neuroserpin inclusion bodies (Vapore 2021, PMID:34361933), useful for genetic screens of modifiers of aggregation.
- **Rat** — a megsin-overexpressing rat is described as "a rat model of human FENIB" (Takano 2006, PMID:16782060): PAS-positive intraneuronal inclusions, ER stress, caspase activation and neuronal loss. Caveat: it uses a different serpin (megsin), so it models serpin-ER-accumulation toxicity, not SERPINI1 specifically.
- **Human cell / iPSC** — HEK293 and patient iPSC-derived neurons (PMID:33888787, PMID:39877004); inducible neural stem/progenitor platform for therapy testing (PMID:39749681, PMID:35864382).

**Overall model value.** Transgenic mice and *Drosophila* reproduce the core chain (polymer accumulation → inclusions → correlation with variant severity → neuronal dysfunction) well. The main gaps are: overexpression rather than knock-in dosage; incomplete reproduction of the human dementia phenotype; and the open question of how much the tPA-loss (Branch B) arm contributes in vivo — a `HUMAN_MODEL_MISMATCH` candidate for the KB.

Model resources: MGI (the G392E alleles are catalogued, e.g. MGI:3833390/3833391), ZFIN (*serpini1*), plus the published transgenic lines.

---

## Curation notes for building the entry

- **Already cached & on-topic:** PMID:41817056 (PME review) is in `references_cache/`. The other four cached PMIDs (25401298 KCNC1, 37386445 breast cancer, 39749860/24207119 SERPINB7 Nagashima PPK) are **not** about FENIB — do not cite them for this entry.
- **Fetch before citing:** every PMID above needs `just fetch-reference PMID:…`, then verify each snippet with `just count-verified-snippets`. The 125-char quote fragments here are leads, not verified snippets.
- **Highest-value primary sources:** 10517635, 10595921, 12103288, 15090543, 17392169, 18267959, 36417830, 35864382, 27618835, 34405255 (review).
- **IDs to look up, not recall:** the HGNC id for SERPINI1 (absent from `cache/hgnc/terms.csv`), UniProt Q99574, and any CL/UBERON subtypes beyond those confirmed above. Confirm ORPHA:85110 via the Orphadata cache.
- **Mechanism-module tie-ins:** serpin polymerization / ER-accumulation proteinopathy (shared with α1-antitrypsin); consider `conforms_to` against a protein-aggregation or ER-stress module if one exists (`just list-modules`).
- **Granularity:** this is a single `DISEASE` entry with variant-level detail carried in `genetic[].variants` (S49P, S52R, L47P, H338R, G392E, G392R), not separate entries. The dementia-predominant vs PME-predominant split is a phenotypic spectrum driven by variant instability, best handled with `subtype:`-stratified phenotypes rather than `has_subtypes` disease strata.

Sources I relied on most: [Davis 1999 Nature (PMID:10517635)](https://pubmed.ncbi.nlm.nih.gov/10517635/), [Davis 1999 Am J Pathol (PMID:10595921)](https://pubmed.ncbi.nlm.nih.gov/10595921/), [Davis 2002 Lancet (PMID:12103288)](https://pubmed.ncbi.nlm.nih.gov/12103288/), [Yang 2022 Seizure (PMID:36417830)](https://pubmed.ncbi.nlm.nih.gov/36417830/), [D'Acunto 2021 review (PMID:34405255)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8558161/), and [MedlinePlus Genetics: FENIB](https://medlineplus.gov/genetics/condition/familial-encephalopathy-with-neuroserpin-inclusion-bodies).

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 43 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 43 |
| On topic | 36 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:15291813` *(abstract only)*: "is trapped as an inactive intermediate that rapidly forms polymers"
  - closest text in source: "We show here that neuroserpin Portland (Ser52Arg), which causes a severe form of FENIB, also forms loop-sheet polymers but at a faster rate, in keeping with the more severe clinical phenotype"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 51 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 8 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011412` (2 mentions) - the report calls it "MONDO"; MONDO calls it **familial encephalopathy with neuroserpin inclusion bodies**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002037` (1 mention) - the report calls it "Cerebellum (largely spared)"; UBERON calls it **cerebellum**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `MGI`.