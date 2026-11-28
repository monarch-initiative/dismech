---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-28T15:19:28.616438'
end_time: '2026-11-28T15:23:04.296242'
duration_seconds: 215.68
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Pulpitis
  mondo_id: MONDO:0006937
  category: Infectious
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: inflammation of dental pulp; dental pulp inflammation
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
  - claude-opus-5-5
  web_search_requests: 22
  num_turns: 29
  total_cost_usd: 1.2083682999999998
  session_id: 4099ddfb-2d01-4861-aab8-04a3aa7d1919
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  tool_calls: 28
  retrieval_calls: 23
  assistant_text_blocks: 3
citation_count: 56
reference_validation:
  total_references: 44
  verified: 44
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 8
  quotes_valid: 3
  quotes_unsupported: 5
  unsupported_quote_references:
  - PMC:PMC12785836
  - PMC:PMC6094490
  - PMC:PMC4619960
  - PMC:PMC12521540
  relevance_assessed: 44
  on_topic: 18
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 22
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0006937
    reported_labels:
    - Mondo
    ontology_label: pulpitis
  - term_id: DOID:11121
    reported_labels:
    - Disease Ontology
    ontology_label: pulpitis
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pulpitis
- **MONDO ID:** MONDO:0006937 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** inflammation of dental pulp; dental pulp inflammation
- **Category:** Infectious

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Pulpitis** covering all of the
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

Let me use Write then run separately.

I've collected identifiers, classification systems, microbiology, mechanisms, biomarkers and treatment evidence. Two more searches on pain management and quality of life, then I'll write the report.

# Pulpitis (MONDO:0006937): disease characteristics research report

**Scope and interpretation:** Pulpitis is an acquired inflammatory disease of the dental pulp. **It has no causal gene.** None is recorded, and no gene appears in Mondo, OMIM or ClinVar. The genetic sections below therefore cover susceptibility factors, expression changes and epigenetic findings, not Mendelian causation.

**Method limits:** Direct PubMed E-utilities queries were blocked in this session, so I gathered evidence through web search of PubMed, PMC, Cochrane, ClinicalTrials.gov, AAE and Mondo records. I give a PMID only where one appeared on a retrieved page. Everything else is cited by PMC ID, DOI or URL. Most quotations are short excerpts from search-indexed abstracts, not full-text reads. I did not do a dedicated lookup of HPO, GO, CL, UBERON, CHEBI or NCIT. Ontology terms are marked "suggested" and need to be checked against the ontology browsers.

---

## 1. Disease information

**Overview.** MeSH defines pulpitis as inflammation of the dental pulp, "usually from bacterial infection tied to caries or tooth fracture." Chemical irritants, heat and hyperemic changes can also cause it ([MeSH D011671](https://meshb.nlm.nih.gov/record/ui?ui=D011671)).

Clinically it runs on a continuum:
- **Reversible pulpitis:** the pulp can heal once the irritant is removed.
- **Irreversible pulpitis:** without intervention the pulp will progress to necrosis ([Cleveland Clinic](https://my.clevelandclinic.org/health/diseases/23536-pulpitis); [MSD Manual](https://www.msdmanuals.com/home/mouth-and-dental-disorders/tooth-disorders/pulpitis)).

**Identifiers**

| System | ID | Source |
|---|---|---|
| Mondo | MONDO:0006937 | [Mondo node via SAIL Concept Library](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0006937/) |
| Disease Ontology | DOID:11121 | Mondo cross-reference |
| MeSH | D011671 | [MeSH](https://meshb.nlm.nih.gov/record/ui?ui=D011671) |
| UMLS / MedGen | C0034103 / 8305 | Mondo cross-reference; [MedGen](https://ncbi.nlm.nih.gov/medgen/8305) |
| ICD-10 / ICD-10-CM | K04.0 Pulpitis, under K04 "Diseases of pulp and periapical tissues" (K04.1 is necrosis of pulp) | [gesund.bund.de](https://gesund.bund.de/en/icd-code-suche/k04-0); [AAPC](https://aapc.com/codes/icd-10-codes/K04.0) |
| ICD-11 | DA09.0 (unverified; reported only by a secondary mapping site) | [autoicdapi](https://autoicdapi.com/reference/icd-10/K04.0) |
| OMIM / Orphanet | None; not a rare or Mendelian disease | — |
| DrugBank condition | DBCOND0010215 | [DrugBank](https://go.drugbank.com/conditions/DBCOND0010215) |

- In Mondo, the term sits under a dental pulp disorder grouping, with a musculoskeletal-system ancestor ([SAIL](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0006937/)).
- **Synonyms:** inflammation of dental pulp; dental pulp inflammation; "toothache of pulpal origin"; "hot tooth" (used for symptomatic irreversible pulpitis that is hard to anesthetize).
- **Clinical subtypes:**
  - The AAE 2009 terms are reversible pulpitis, symptomatic irreversible pulpitis and asymptomatic irreversible pulpitis ([AAE consensus PDF](https://www.aae.org/specialty/wp-content/uploads/sites/2/2017/07/aaeconsensusconferencerecommendeddiagnosticterminology.pdf)).
  - The Wolters 2017 system grades pulpitis as initial, mild, moderate or severe (Int Endod J 50(9); [Bristol record](https://research-information.bris.ac.uk/en/publications/minimally-invasive-endodontics-a-new-diagnostic-system-for-assess/)).
- **Data provenance:** All of the above comes from aggregated, disease-level resources (ontologies and classifications). Epidemiology comes from clinic-level cohort studies, not EHR-wide registries.

## 2. Etiology

**Causal factors**
- **Infectious:** Bacteria from dental caries are the main cause. Bacterial products diffuse through dentinal tubules before the pulp is exposed ([MeSH](https://meshb.nlm.nih.gov/record/ui?ui=D011671); [Rôças et al. 2016, PMC4852894](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4852894/)).
- **Traumatic:** Crown fractures that expose the pulp.
- **Iatrogenic:** Cavity preparation and heat generation.
- **Chemical:** Irritants, including restorative materials.
- **Thermal or hyperemic:** As listed in MeSH.

**Risk factors**
- **Deep and extremely deep caries.** The ESE defines deep caries as reaching the inner quarter of dentine, and extremely deep caries as penetrating the full thickness of dentine ([ESE position statement, Duncan et al. 2019, Int Endod J 52:923–934, doi:10.1111/iej.13080](https://munin.uit.no/handle/10037/16863)).
- **Dental trauma.**
- **Type 2 diabetes.** In a 77-patient cross-sectional study, pulpal MMP-9 and TNF-α were "significantly higher (p<0.005) in irreversible pulpits than reversible pulpits and also in Type-2 diabetics than non-diabetics" ([Eur Endod J 2023, DOAJ](https://doaj.org/article/9a09437f39bf455e8bfc4afa01921056)). This is an association with inflammatory burden, not established causation.
- **Genetic:** I found no GWAS or validated susceptibility locus for pulpitis itself.
  - Reviews say "genetic polymorphisms in disease relevant genes have suggested that individual predisposition may contribute to susceptibility to pulpal and periapical diseases" ([Front Physiol 2020, PMC7010935](https://pmc.ncbi.nlm.nih.gov/articles/PMC7010935)).
  - The best-documented variant, IL1B rs1143643, is linked to *periapical lesion* development in people with untreated deep caries ([PMC5682944](https://pmc.ncbi.nlm.nih.gov/articles/PMC5682944)). That is a downstream endpoint, not pulpitis.
  - Another review covers SNPs in endodontic pathology ([PMC11669393](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11669393/)).

**Protective factors**
- Caries control: fluoride, diet, oral hygiene.
- Early management of caries with selective removal to avoid pulp exposure ([ESE 2019](https://munin.uit.no/handle/10037/16863)).
- Reparative (tertiary) dentin formation.
- No protective genetic variants were found.

**Gene–environment interactions:** Not established. One plausible model is that cytokine-gene variants change the host's inflammatory response to the same caries-bacterial challenge; this is inferred from apical periodontitis data ([PMC5682944](https://pmc.ncbi.nlm.nih.gov/articles/PMC5682944)). CTD lookup was not done.

## 3. Phenotypes

| Phenotype | Type | Characteristics | Suggested HPO (verify) |
|---|---|---|---|
| Stimulus-evoked, short-lived tooth pain (cold or sweet) | Symptom | Reversible pulpitis: "brief, stimulus-evoked pain" ([IJMS 2025, PMC12785836](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12785836/)) | Toothache / dental pain |
| Lingering thermal pain | Symptom | Symptomatic irreversible pulpitis; working threshold of "30 seconds or longer" after the stimulus is removed ([AAE 2013](https://www.aae.org/specialty/wp-content/uploads/sites/2/2023/12/Fall2013-EndoDiagnosis.pdf)) | Thermal hyperalgesia (approximation) |
| Spontaneous pain | Symptom | Irreversible pulpitis; "prolonged, spontaneous, or radiating pain" ([PMC12785836](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12785836/)) | Toothache |
| Referred or radiating pain (ear, jaw, other teeth) | Symptom | Listed as an AAE descriptor | — |
| Usually no pain on percussion | Sign (negative) | Inflammation has not yet reached periapical tissues ([AAE](https://www.aae.org/specialty/wp-content/uploads/sites/2/2017/07/aaeconsensusconferencerecommendeddiagnosticterminology.pdf)) | — |
| Deep carious lesion or pulp exposure | Sign | Typical precursor | Dental caries (HP:0000670, verify) |
| Resistance to local anesthesia ("hot tooth") | Clinical sign | IANB success in symptomatic molars is about 15–30% ([PMC4450520](https://pmc.ncbi.nlm.nih.gov/articles/PMC4450520); [JOMA review](https://joma.amegroups.org/article/view/7696/html)) | — |
| Raised pulpal-blood MMP-9 and TNF-α | Laboratory | Higher in irreversible than reversible pulpitis ([DOAJ](https://doaj.org/article/9a09437f39bf455e8bfc4afa01921056)) | — |

- **Onset:** Childhood through old age, following caries or trauma.
- **Severity:** Ranges from mild to severe.
- **Course:** Progressive if untreated.
- **Quality of life:** A UK RCT measured oral-health-related QoL and found pulpotomy "as effective as RCT in reducing post-operative pain, and improving QoL and HRQoL" (PMID 39325552; [PMC11629050](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11629050/)). Pulpal pain drives emergency attendance (Section 9).

## 4. Genetic and molecular information

- **Causal genes, pathogenic variants, ACMG classification, allele frequencies, chromosomal abnormalities:** Not applicable. The disease is acquired, with no germline causal variants, and no ClinVar, gnomAD or DECIPHER entries are relevant.
- **Susceptibility and modifier candidates (low evidence):** IL1B, including rs1143643 and -511 C/T, mainly for apical periodontitis ([PMC5682944](https://pmc.ncbi.nlm.nih.gov/articles/PMC5682944); [Cureus 2024 review](https://assets.cureus.com/uploads/review_article/pdf/316901/20241125-1708166-hf7hqt.pdf)). I found no TLR polymorphism study in pulpitis. TLR2 and TLR4 data are expression data only; TLR2 and Dectin-1 expression were correlated in irreversibly inflamed pulp ([BMC Oral Health 2022, doi:10.1186/s12903-022-02621-4](https://doi.org/10.1186/s12903-022-02621-4)).
- **Epigenetics (in vitro):**
  - DNA methylation changes the LPS response of human dental pulp cells. In these experiments the demethylating agent 5-aza-2'-deoxycytidine altered inflammatory output, and the authors call this role weakly understood ([PMC6550546](https://pmc.ncbi.nlm.nih.gov/articles/PMC6550546)).
  - Histone methylation and acetylation, DNA methylation and non-coding RNAs are the main mechanisms discussed (Hui et al., *Oral Dis* 2017, [BL record](https://eld.bl.uk/catalog/100041365626_0x000001)).
  - HDAC inhibitors and DNMT inhibitors promote mineralization and repair in pulp cells ([Front Genet 2018, PMC6090030](https://pmc.ncbi.nlm.nih.gov/articles/PMC6090030); [PMC7016267](https://pmc.ncbi.nlm.nih.gov/articles/PMC7016267)).

## 5. Environmental information

- **Infectious agents.** The microbiome of deep caries in teeth with symptomatic irreversible pulpitis (10 teeth, next-generation sequencing) contained 14 phyla and 101 genera ([Rôças et al., PLoS ONE 2016, PMC4852894](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4852894/)):
  - The main genera were *Lactobacillus* (42.3% of sequences), *Olsenella* (13.7%), *Pseudoramibacter* (10.7%) and *Streptococcus* (5.5%).
  - Half the samples were Lactobacillus-dominated and half had very little Lactobacillus.
  - The authors call the detected taxa "candidate pathogens for irreversible pulpitis and possibly the pioneers in pulp invasion."
  - A 2015 J Endod checkerboard study by the same group found taxa "significantly associated with symptoms" ([UFRN repository](https://repositorio.ufrn.br/items/3e176222-be16-46fd-a32b-8595f0f41a54/full)).
  - In reversible pulpitis, symptomatic teeth had more *Lactobacillus* spp., *Capnocytophaga sputigena* and *Leptotrichia buccalis* ([Clin Oral Investig, doi:10.1007/s00784-020-03624-7](https://link.springer.com/article/10.1007/s00784-020-03624-7)).
  - Suggested NCBI Taxon IDs (verify): *Lactobacillus* 1578, *Streptococcus* 1301, *Olsenella* 133925.
- **Lifestyle:** Diet high in fermentable sugars and poor oral hygiene, both acting through caries. Contact sports and other trauma risks act through tooth fracture. I did not retrieve dedicated CTD or NHANES data.
- **Toxins and chemicals:** Restorative-material irritants are listed in MeSH. No CTD lookup was done.

## 6. Mechanism and pathophysiology

**Causal chain** (some steps are inferred from in vitro or animal data, as noted)

1. Cariogenic bacteria demineralize enamel and dentin. This **leads to** bacterial antigens (LPS, lipoteichoic acid) diffusing through dentinal tubules ([PMC4852894](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4852894/)).
   - **Branch:** Trauma or iatrogenic exposure gives bacteria direct access to the pulp.
2. Odontoblasts at the pulp–dentin border sense these antigens through TLR2 (Gram-positive) and TLR4 (Gram-negative). TLR2 is "upregulated in odontoblasts beneath caries lesions" ([Japanese Dental Science Review 2018, PMC6094490](https://pmc.ncbi.nlm.nih.gov/articles/PMC6094490); [PMC4619960](https://pmc.ncbi.nlm.nih.gov/articles/PMC4619960)).
3. TLR signaling **results in** NF-κB and p38 MAPK activation. This **leads to** IL-6, chemokines and other mediators (Farges et al., cited in [Front Physiol 2013, PMC3823031](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3823031/)). Evidence: in vitro and ex vivo.
4. In parallel, Aδ and C sensory fibers release substance P and CGRP within about 24 hours ([Front Dent Med 2025](https://www.frontiersin.org/journals/dental-medicine/articles/10.3389/fdmed.2025.1686734/full)). Levels of CGRP, SP and neurokinin A are significantly higher in inflamed human pulp (PMID 16640639). This **leads to** vasodilation, more vascular permeability and recruitment of immune cells (neurogenic inflammation).
5. Neutrophils, macrophages, dendritic cells and T cells are recruited (review: PMID 38959180). This **results in** release of proteases such as MMP-9 and of TNF-α ([DOAJ 2023](https://doaj.org/article/9a09437f39bf455e8bfc4afa01921056)).
6. Inflammatory mediators sensitize TRPV1 and TRPA1 on pulpal afferents, and the inflammation produces endogenous TRP agonists ([IJMS 2025, PMC12785836](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12785836/)). Upregulation of TTX-resistant sodium channels is proposed. Together these **lead to** hyperalgesia, spontaneous and lingering pain, and failure of local anesthesia ([PMC4450520](https://pmc.ncbi.nlm.nih.gov/articles/PMC4450520)). The anesthesia mechanism is only partly established.
7. Edema occurs inside the rigid, low-compliance pulp chamber. The resulting circulatory compromise is the classic explanation for spreading necrosis, but I did not retrieve a primary source this session, so treat it as inferred. Ferroptosis of pulp cells is also implicated ([Int J Oral Sci 2025, PMC12521540](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12521540/)).
   - **Branch A:** If the irritant is removed, inflammation resolves and odontoblast-like cells form reparative dentin (reversible pulpitis).
   - **Branch B:** If it persists, the condition **progresses to** pulp necrosis (K04.1), then infection of the root canal and apical periodontitis.

**Molecular profiling**
- **Single-cell RNA-seq, pulpitis:** Three pulpitis and three healthy pulps gave 40,231 cells in 12 clusters. Ferroptosis-gene changes appeared in almost every cluster, and fibroblasts, which dominate healthy pulp, "significantly decreased in pulpitis" (thymosin α1 study, [PMC12521540](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12521540/)).
- **Single-cell RNA-seq, carious pulp:** An atlas of carious versus healthy pulp found changes in immune-cell, mesenchymal stem cell and fibroblast clusters (PMID 37532703).
- **Single-cell pilot:** 6,810 cells showed altered immune-cell composition in deep caries but not in enamel caries ([Front Dent Med 2022](https://www.frontiersin.org/articles/10.3389/fdmed.2021.806294/full)).

**Suggested ontology terms (verify)**
- **GO:** inflammatory response (GO:0006954), toll-like receptor signaling pathway (GO:0002224), neutrophil chemotaxis (GO:0030593), detection of temperature stimulus involved in sensory perception of pain (GO:0050965), ferroptosis (GO:0097707), odontogenesis of dentin-containing tooth (GO:0042475).
- **CL:** odontoblast (CL:0000060), fibroblast (CL:0000057), neutrophil (CL:0000775), macrophage (CL:0000235), dendritic cell (CL:0000451), T cell (CL:0000084), sensory neuron (CL:0000101), mesenchymal stem cell (CL:0000134).

## 7. Anatomical structures

- **Organ:** Tooth; primarily the dental pulp, a connective tissue rich in nerves and blood vessels.
- **Secondary:** Periapical tissues and alveolar bone, if the condition progresses to apical periodontitis. Body system: digestive/oral.
- **Cells:** Odontoblasts, pulp fibroblasts, stem cells, immune cells and trigeminal afferents. Trigeminal ganglion TRPV1 changes have been shown in mouse models (PMID 21712529).
- **Subcellular:** Plasma membrane (TLRs, TRP channels; GO:0005886); secreted mediators in the extracellular space.
- **Suggested UBERON (verify):** dental pulp (UBERON:0001754), dentine (UBERON:0001752), tooth (UBERON:0001091), trigeminal ganglion (UBERON:0001675).
- **Lateralization:** Usually a single tooth, unilateral. Referred pain can make the tooth hard to localize.

## 8. Temporal development

- **Onset:** Acute (symptomatic) or insidious (asymptomatic irreversible pulpitis). It occurs at any age once teeth have erupted.
- **Stages:**
  - AAE: reversible, then irreversible (symptomatic or asymptomatic), then necrosis ([AAE](https://www.aae.org/specialty/wp-content/uploads/sites/2/2017/07/aaeconsensusconferencerecommendeddiagnosticterminology.pdf)).
  - Wolters: initial, mild, moderate, severe.
  - A revised Wolters model reached 100% sensitivity and specificity for separating mild from severe pulpitis, and 83% sensitivity with 85.7% specificity for moderate pulpitis. Interrater agreement was κ = 0.593 for Wolters versus 0.888 for AAE ([IEJ 2025, doi:10.1111/iej.14254; PMC12254530](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12254530/)).
- **Course:** Progressive without treatment. Reversible pulpitis can go into remission once the irritant is removed. The window for vital pulp therapy is before necrosis.
- **Revision under way:** A joint AAE/ESE committee is revising the terminology ([AAE/ESE 2025](https://www.aae.org/specialty/wp-content/uploads/sites/2/2025/07/AAE_ESE_Background_Process_ForWeb07172025.pdf); [2026 stakeholder summary](https://www.aae.org/specialty/wp-content/uploads/sites/2/2026/03/Stakeholder_Feedback_Summary_2026_Final.pdf)).

## 9. Inheritance and population

- **Inheritance:** Not inherited; multifactorial and acquired. Penetrance, anticipation, founder effects and carrier frequency do not apply.
- **Epidemiology:** I found no population prevalence or GBD-specific figure. Clinic-level data:
  - Irreversible pulpitis was the most common diagnosis (30.4%, 299 cases) among pulpal and periapical diagnoses in a Brazilian emergency clinic ([RGO 2018](https://scielo.br/j/rgo/a/xgVPBQkNxkLwMGCMFBQtwfm/?lang=en)).
  - It was 77% in an Iranian referral sample of 100 patients with pain ([BMC Oral Health 2018](https://link.springer.com/article/10.1186/s12903-018-0563-x)).
  - "Nearly 90%" of emergency dental patients have pulpal or periapical symptoms ([BDJ](https://doi.org/10.1038%2Fsj.bdj.4811641)).
- **Demographics:** These follow the burden of untreated caries. No reliable sex ratio was retrieved.

## 10. Diagnostics

- **Clinical criteria:**
  - AAE 2009: diagnosis rests on history, thermal and electric sensibility testing, percussion and radiographs. Symptomatic irreversible pulpitis is defined as "a clinical diagnosis based on subjective and objective findings indicating that the vital inflamed pulp is incapable of healing" ([AAE](https://www.aae.org/specialty/wp-content/uploads/sites/2/2017/07/aaeconsensusconferencerecommendeddiagnosticterminology.pdf)).
  - The Wolters 2017 and ESE 2019 classifications are alternatives.
- **Histologic correlation:** In 95 consecutively collected teeth, clinical "normal pulp or reversible pulpitis" matched histology in 57 of 59 (96.6%), and irreversible pulpitis matched in 27 of 32 (84.4%) (Ricucci et al., J Endod 2014;40:1932–9, PMID 25312886).
- **Imaging:** Periapical or bitewing radiographs show caries depth and rule out apical periodontitis. CBCT is an adjunct.
- **Biomarkers (investigational):**
  - Pulpal-blood MMP-9 "could be a useful ancillary diagnostic tool" (Mente 2016, J Endod).
  - MMP-9 normalized to total protein predicted pulp-capping survival in an RCT ([PMC8935528](https://pmc.ncbi.nlm.nih.gov/articles/PMC8935528)).
  - MMP-2 and MMP-9 are raised in irreversible pulpitis of primary molars ([BMC Oral Health 2024](https://link.springer.com/article/10.1186/s12903-024-04795-5)).
  - Ongoing trials: NCT06960603, NCT06514053, NCT03807674. There are no validated cut-offs.
- **Genetic testing, karyotyping, CMA, newborn or carrier screening:** Not applicable.
- **Differential diagnosis:**
  - Dentin hypersensitivity (short, sharp pain with exposed dentin).
  - Cracked tooth.
  - Pulp necrosis and apical periodontitis (no response to sensibility tests, pain on percussion, periapical radiolucency).
  - Periodontal abscess.
  - Maxillary sinusitis.
  - Trigeminal neuralgia and other non-odontogenic pain.

## 11. Outcome and prognosis

- **Mortality:** Pulpitis is essentially non-lethal. Mortality data are not applicable and none were found.
- **Morbidity:** Severe pain, emergency visits and loss of the tooth after extraction.
- **Complications:** Pulp necrosis, then apical periodontitis, abscess and, rarely, spreading odontogenic infection. These come from MeSH and the ICD hierarchy; I retrieved no cohort data on frequency.
- **Recovery:** Reversible pulpitis resolves after the cause is removed. Irreversible pulpitis responds well to treatment:
  - Pulpotomy pooled success was 86% (95% CI 76–92%; I² = 81.9%), with root development stage and biomaterial as predictors (Ather et al., Sci Rep 2022, [PMC9669040](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9669040/)).
  - Calcium silicate vital pulp therapy reached 81–90% radiographic success ([PMC8228104](https://pmc.ncbi.nlm.nih.gov/articles/PMC8228104)).
- **Prognostic factors:** Severity grade, since severe Wolters pulpitis did worse than mild ([Careddu & Duncan 2021](https://gsia.tums.ac.ir/Images/UserFiles/2986/file/Appraise%20To%20Raise/Endodontics/260322/Int%20Endodontic%20J%20-%202021%20-%20Careddu%20-%20A%20prospective%20clinical%20study%20investigating%20the%20effectiveness%20of%20partial%20pulpotomy%20after.pdf)); diabetes; and MMP-9 levels.

## 12. Treatment

**Pharmacotherapy**
- **NSAID premedication** before the inferior alveolar nerve block:
  - All NSAIDs versus placebo: RR 1.92 (1.55–2.38).
  - Ibuprofen above 400 mg: RR 1.85 (1.39–2.45).
  - Ibuprofen at or below 400 mg: RR 1.78 (0.90–3.55, not significant).
  - Sources: meta-analyses at [pubmed.gov 29709297](https://www.pubmed.gov/29709297/), [27834417](https://pubmed.ncbi.nlm.nih.gov/27834417/) and [30295006](https://www.pubmed.gov/30295006/). I could not tell from snippets which estimate comes from which PMID.
- **Anesthetic strategy:** Articaine, supplemental buccal infiltration or intraosseous injection, and larger volumes ([JOMA review](https://joma.amegroups.org/article/view/7696/html)).
- **Analgesics:** Ibuprofen and acetaminophen.
- **Antibiotics are not indicated.** The Cochrane review included one trial of 40 patients (penicillin versus placebo) and found that antibiotics "do not appear to significantly reduce toothache"; certainty was low ([Agnihotry et al. 2019, CD004969.pub5](https://www.cochrane.org/CD004969); [PMC6542501](https://pmc.ncbi.nlm.nih.gov/articles/PMC6542501)).
- **Pharmacogenomics:** None relevant.

**Procedures**
- **Indirect pulp capping and selective caries removal or stepwise excavation** to avoid exposure. A hydraulic calcium silicate or glass ionomer is placed over deep dentine ([ESE 2019](https://munin.uit.no/handle/10037/16863)).
- **Direct pulp capping; partial or full pulpotomy** with MTA, Biodentine or calcium-enriched mixture (CEM) cement.
- **Pulpectomy and root canal treatment.**
- **Extraction.**

**Key trials of pulpotomy versus root canal treatment**
- NCT03956199 (PMID 39325552): equivalent pain and QoL outcomes.
- Taha et al., J Endod 2023 (PMID 37080387 as cited; not verified).
- Systematic review PMID 37188923: "comparable clinical and patient outcomes, but insufficient evidence."
- PROVE individual-participant meta-analysis protocol ([PMC10722670](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10722670/)).
- Registered trials: NCT00748280 (multicenter, Iran), NCT06002698, NCT05726357, NCT07375576, NCT07046533.

**Experimental (preclinical)**
- Thymosin α1, which acts against ferroptosis ([PMC12521540](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12521540/)).
- HDAC and DNMT inhibitors for pulp repair ([PMC6090030](https://pmc.ncbi.nlm.nih.gov/articles/PMC6090030)).
- Gene, cell, RNA and immunotherapies: none in clinical use.

**Treatment algorithm** (ESE and AAE based): assess caries depth and symptoms, then choose by diagnosis:
- **Reversible or mild pulpitis:** selective caries removal and indirect capping.
- **Exposure in a vital pulp:** capping or partial pulpotomy, then full pulpotomy if needed.
- **Severe pulpitis or bleeding that cannot be controlled:** pulpectomy and root canal treatment.

**Suggested NCIT terms (verify):** Root Canal Therapy; Pulpotomy; Tooth Extraction; Ibuprofen (C561); Local Anesthesia.

## 13. Prevention

- **Primary:** Caries prevention (fluoride, sealants, sugar reduction, oral hygiene) and mouthguards against trauma. There is no vaccine. I did not retrieve dedicated guideline sources this session.
- **Secondary:** Regular dental examination, plus radiographs to catch deep caries before the pulp is exposed.
- **Tertiary:** Timely vital pulp therapy to prevent necrosis and apical periodontitis.
- **Not applicable:** Genetic counseling and screening.
- **Antibiotic prophylaxis:** Not supported ([Cochrane](https://www.cochrane.org/CD004969)).

## 14. Other species and natural disease

- **Dogs** (*Canis lupus familiaris*, NCBI Taxon 9615) and **cats** (*Felis catus*, 9685):
  - Pulpitis mostly follows complicated crown fractures. In dogs and cats "most cases of pulpitis are diagnosed as irreversible" ([MSD Vet Manual](https://www.msdvetmanual.com/digestive-system/dentistry/endodontic-disease-in-small-animals)).
  - The maxillary fourth premolar is a frequent site.
  - Reported tooth-fracture prevalence in dogs is 20–27% ([PMC9872002](https://pmc.ncbi.nlm.nih.gov/articles/PMC9872002)).
  - In military working dogs, prevalence of traumatic dental injury was 43.6% ([J Vet Dent](https://journals.sagepub.com/doi/10.1177/0898756420946500)).
  - Enamel–dentin–pulp fracture was the most common injury (49.6%) in a dog and cat series (PMID 26197685, as retrieved).
- **Other:** Not zoonotic, no breed predisposition was identified, and there is no OMIA entry.

## 15. Model organisms

| Model | Method | Use | Reference |
|---|---|---|---|
| Rat (*Rattus norvegicus*, 10116) | Occlusal cavity in the maxillary first molar plus *E. coli* LPS (10 mg/mL) after pulp injury; 27 rats, 54 cavities | Pulpotomy and biomaterial testing | Minic et al. 2021, PMID 34356848 |
| Rat | LPS-soaked paper tips (1 mg/mL) sealed in the pulp cavity with glass ionomer | Acute pulpitis pain | Xiao et al. 2022, PMID 35748325 |
| Rat | Systemic (intravascular) LPS | Widespread pulpitis | Bletsa et al. 2006, PMID 16527857 |
| Mouse (*Mus musculus*, 10090) | LPS applied to dentin of the maxillary first molar; TRPV1 in trigeminal ganglion | Enables genetically engineered mice for pain mechanisms | Chung et al. 2011, PMID 21712529 |
| Mouse (C57BL/6) | Pulp-cavity LPS exposure, then filling | Standardized protocol | Bio-protocol 2025, doi:10.21769/BioProtoc.5128 |
| In vitro | LPS-stimulated human dental pulp cells and odontoblast-like cells | Epigenetics, TLR signaling | [PMC6550546](https://pmc.ncbi.nlm.nih.gov/articles/PMC6550546); [PMC3823031](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3823031/) |

- **What the models capture:** Acute inflammation, cytokine and neuropeptide responses, and pain behavior.
- **What they miss:** The chronic polymicrobial carious process, slow human progression and the distinctions of human clinical grading. Rodent molars are also tiny.
- **Genetic models:** No knockout reproduces pulpitis itself. Genetically engineered mice are used inside the induced models (MGI not queried).

---

**Main evidence gaps**
- No population prevalence or GBD-level figure for pulpitis.
- No validated genetic susceptibility loci.
- No validated biomarker cut-offs.
- Several PMIDs (Taha 2023, the ibuprofen meta-analyses) need confirming on PubMed.
- Ontology IDs need to be checked in OLS.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 44 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 8 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 5 |
| References weighed for topical relevance | 44 |
| On topic | 18 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC12785836` *(abstract only)*: "brief, stimulus-evoked pain"
  - Text part not found as substring: 'brief, stimulus-evoked pain' (note: only abstract available for PMID:41516061, full text may contain this excerpt)
- `PMC:PMC12785836` *(abstract only)*: "prolonged, spontaneous, or radiating pain"
  - closest text in source: "Pulpitis elevates endogenous TRPV1 and TRPA1 agonists, while inflammatory mediators sensitize TRP channels, amplifying pain"
- `PMC:PMC6094490` *(abstract only)*: "upregulated in odontoblasts beneath caries lesions"
  - closest text in source: "Odontoblasts located in the outermost layer of dental pulp form a natural barrier between mineralized tissues, dentin, and soft tissues, dental pulp, of the vital tooth, and they first recognize caries-related pathogens and sense external irritations"
- `PMC:PMC4619960` *(abstract only)*: "upregulated in odontoblasts beneath caries lesions"
  - closest text in source: "We report, using selected examples, different strategies potentially used by odontoblasts and specialized immune cells to combat dentin-invading bacteria in vivo."
- `PMC:PMC12521540` *(abstract only)*: "significantly decreased in pulpitis"
  - Text part not found as substring: 'significantly decreased in pulpitis' (note: only abstract available for PMID:41087337, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 4 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0006937` (5 mentions) - the report calls it "Mondo"; MONDO calls it **pulpitis**
- `DOID:11121` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **pulpitis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006954` (1 mention) - the report calls it "GO:** inflammatory response"; GO calls it **inflammatory response**
- `CL:0000060` (1 mention) - the report calls it "CL:** odontoblast"; CL calls it **odontoblast**