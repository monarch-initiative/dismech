---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-26T02:08:03.951690'
end_time: '2026-11-26T02:12:09.238991'
duration_seconds: 245.29
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Salmonella Discitis
  mondo_id: MONDO:8000004
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Salmonella spondylodiscitis; Salmonella spondylodiskitis
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
  web_search_requests: 5
  num_turns: 11
  total_cost_usd: 0.729914435
  session_id: 534bbad0-ec7c-4f82-82d5-f6d754174936
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 32
  retrieval_calls: 29
  assistant_text_blocks: 2
citation_count: 11
reference_validation:
  total_references: 33
  verified: 33
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 33
  on_topic: 20
  validator_version: 0.8.0
term_validation:
  total_terms: 2
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:8000004
    reported_labels:
    - retrieved
    - SAIL
    ontology_label: salmonella discitis
  unresolvable_prefixes:
  - GARD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Salmonella Discitis
- **MONDO ID:** MONDO:8000004 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Salmonella spondylodiscitis; Salmonella spondylodiskitis
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Salmonella Discitis** covering all of the
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

Searching the literature and now collecting PMIDs and abstract quotes for the key papers.

**Note on scope:** This report covers MONDO:8000004, "salmonella discitis": infection of the intervertebral disc space and nearby vertebral bodies (spondylodiscitis or vertebral osteomyelitis) caused by *Salmonella enterica*, both typhoidal and non-typhoidal serovars. **The causal agent is a pathogen, not a human gene. No causal human gene is recorded, and none exists for this disease.** I treated "Salmonella discitis", "Salmonella spondylodiscitis" and "Salmonella vertebral osteomyelitis" as one entity, because the literature uses these terms interchangeably.

**Evidence limits:**
- The literature is almost entirely case reports, small case series and systematic reviews of those case reports. There are no trials, cohorts, registries or omics studies.
- Many sections of the template (genetics, epigenetics, omics, model organisms, gene therapy) do not apply.
- I could not run PubMed queries directly in this session. PubMed records were retrieved through a delegated fetch of NCBI E-utilities, plus web searches.
- I give ontology terms as labels only. I did not retrieve their numeric IDs in this session, so each one needs to be checked before entry into the knowledge base.

---

# Salmonella Discitis (Salmonella Spondylodiscitis)

## 1. Disease Information

**Overview.** In Mondo, MONDO:8000004 "salmonella discitis" is defined as discitis caused by *Salmonella* infection. Its parents are *salmonellosis*, *bacterial arthritis* and *infectious discitis*. It is cross-referenced to GARD:0027037, "Discitis caused by infection with Salmonella" ([SAIL concept library, MONDO:8000004](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:8000004/)).

*S. enterica* serovars usually cause self-limited gastroenteritis or, for Typhi and Paratyphi, enteric fever. Invasive strains can occasionally seed bone and the disc space. This is a rare complication of bacteremia.

**Identifiers**

| Resource | Identifier |
|---|---|
| Mondo | MONDO:8000004 (retrieved) |
| GARD | 0027037 (retrieved, as a Mondo cross-reference) |
| OMIM | Not applicable; this is not a Mendelian disease |
| Orphanet | None found |
| ICD-10 / ICD-11 | Not retrieved. Coding would usually combine a salmonella-infection code with a discitis or vertebral osteomyelitis code. Verify before use. |
| MeSH | No specific heading found. Use "Discitis" combined with "Salmonella Infections". |

**Synonyms:** Salmonella spondylodiscitis; Salmonella spondylodiskitis; Salmonella vertebral osteomyelitis; Salmonella spondylitis. Serovar-specific forms include "Salmonella Typhi spondylodiscitis" and "non-typhoidal Salmonella (NTS) spondylodiscitis".

**Source of information:** All knowledge is aggregated from published individual-patient case reports and pooled case reviews. There are no EHR-derived or registry datasets.

**Size of the literature:** A PubMed search for `salmonella AND (spondylodiscitis OR discitis OR vertebral osteomyelitis)` returned 155 records. The most recent include:
- PMID 43013364, multidrug-resistant (MDR) *S.* Typhi spondylodiscitis with vertebral collapse (2026).
- PMID 42291979, *S.* Java discitis after a traveller's bacteremia (2026).
- PMID 41657555, *Salmonella* spondylitis masquerading as tuberculosis in a child (2026).
- PMID 42079494, *S.* Typhi mimicking Pott's disease (2025).
- PMID 41143074, *Salmonella* vertebral osteomyelitis with bilateral psoas myositis in newly diagnosed diabetes (2025).

## 2. Etiology

**Causal factor (infectious):** *Salmonella enterica* subsp. *enterica*. Typhoidal serovars (Typhi, Paratyphi) and many non-typhoidal serovars are reported.

- **Adults (Huang et al. 2021, PMID 33942967):** In a systematic review of adult *Salmonella* osteomyelitis, "12 different serotypes" were found. The top three were *S.* Typhi (19 cases), *S.* Typhimurium (12) and *S.* Enteritidis (11). "The commonly reported involved sites were the vertebrae, femur, and tibia."
- **Children (Katzouraki et al. 2022, PMID 36553297):** In 21 children with NTS spondylodiscitis, "11 different serotypes" were reported.
- **Immunocompetent Indian series (Amritanand et al. 2010, PMID 20938384):** "Salmonella typhi was cultured in 4 and S. Paratyphi in 5 patients." In addition, "Five (50%) patients had a documented history of typhoid fever."

**Risk factors (environmental and host)**

- **Hemoglobinopathies, especially sickle cell disease.** *Salmonella* is a characteristic osteomyelitis pathogen in sickle cell disease (StatPearls "Osteomyelitis", PMID 30335283: "Salmonella spp in individuals with sickle cell disease"). The adult systematic review on *Salmonella* osteomyelitis (PMC8274199, which appears to be Huang 2021) suggests the following mechanisms: "impaired splenic function, defects in complement activation, genetic factors, deficiencies in micronutrients, and the presence of infarcted or necrotic bone." The primary paper on sickle cell osteomyelitis etiology, Burnett et al. 1998 (PMID 9445507, Pediatrics), was located but its PubMed record has no abstract, so I could not extract its figures.
- **Older age and atherosclerotic aortic disease.** Santos and Sapico (1998, PMID 9709878) reported that infected abdominal aortic aneurysms occurred exclusively in patients aged 50 years or older. All deaths in their series occurred in that group.
- **Immunosuppression and comorbidities from case reports:**
  - Chronic lymphocytic leukemia (PMID 23981545).
  - Diabetes mellitus (PMID 41143074).
  - Recurrent bacteremia in a 95-year-old (PMID 41530883).
  - An indwelling central venous catheter (PMID 42575248).
  - NSAID use. Hamada et al. 2024 (PMID 38550490) note: "It is critical to take an accurate history of non-steroidal anti-inflammatory drugs (NSAIDs) use."
- **Exposures:** Infection is acquired through contaminated food or water (fecal–oral route) and through travel to endemic areas (PMID 42291979).
- **Immunocompetent hosts are also affected.** Disease occurs in people with no predisposition (PMID 20938384, PMID 36553297).

**Genetic risk factors (host)**

- No GWAS, ClinVar or ClinGen data exist specifically for *Salmonella* discitis.
- Inborn errors of immunity predispose to invasive salmonellosis in general:
  - IL-12/IL-23–IFN-γ axis defects (Mendelian susceptibility to mycobacterial disease, MSMD): *IL12RB1* and *IL12B*. In one series, *Salmonella* occurred in 44.4% (n=4) of IL12RB1/IL12B cases (PMID 42366588). Disseminated *S.* Typhimurium has been reported in IL12RB1 deficiency (PMID 41771439).
  - Chronic granulomatous disease (CGD): one cohort reported "Salmonella spp. bacteremia in 12 of 17 patients with Salmonella infections" (PMID 42180170).
- I did not retrieve any report of spinal or bone infection specifically in these immunodeficiencies.
- *HBB* (sickle hemoglobin) is the main host-genetic predisposing locus by clinical association, through sickle cell disease.

**Protective factors:** No studies were retrieved. Possible protective factors include food and water hygiene and typhoid vaccination (see Section 13), and an intact splenic function and immune system.

**Gene–environment interaction:** No formal studies exist. Conceptually, host susceptibility (HbSS, IL-12/IFN-γ defects, CGD) interacts with exposure to *Salmonella* to cause invasive and bone disease.

## 3. Phenotypes

Pooled frequencies come from the case reviews cited.

| Phenotype | Type | Frequency | Suggested HPO label (ID not verified) |
|---|---|---|---|
| Back pain / localized spinal pain | Symptom | 92% of adults (Santos 1998, PMID 9709878); 90.5% of children had localized pain (PMID 36553297) | Back pain; Low back pain |
| Fever | Sign | 87% (PMID 9709878); 65.7% (44/67) of adults with *Salmonella* osteomyelitis (PMID 33942967); 52.4% of children (PMID 36553297) | Fever |
| Diarrhea / gastroenteritis history | Symptom | 17.9% (12/67) of adults (PMID 33942967); 19% of children (PMID 36553297) | Diarrhea |
| Lumbar involvement | Anatomical | 72% (PMID 9709878); L4/L5 the most common level in children (PMID 36553297); lumbar 28% and thoracic 19% of all osteomyelitis cases in a 2026 meta-analysis abstract ([PMC12791220](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12791220/)) | Abnormal lumbar spine morphology; Discitis |
| Epidural abscess | Complication | Case-level reports (PMID 23981545; [PMC8759999](https://pmc.ncbi.nlm.nih.gov/articles/PMC8759999)) | Spinal epidural abscess |
| Psoas abscess / myositis | Complication | Case-level (PMID 41143074) | Psoas abscess |
| Vertebral collapse / destruction | Sign / imaging | Case-level (PMID 43013364) | Vertebral compression fracture |
| Infected (mycotic) aortic aneurysm | Complication | Older adults (PMID 9709878, 33542000, 22759472) | Abdominal aortic aneurysm |
| Raised CRP / ESR, leukocytosis | Laboratory | Commonly reported; no pooled percentages retrieved | Elevated C-reactive protein level; Elevated erythrocyte sedimentation rate |
| Positive blood culture for *Salmonella* | Laboratory | Variable; no pooled figure retrieved | — |

**Onset, severity, course and quality of life**
- Onset is typically subacute, with symptoms lasting weeks before diagnosis. The disease can mimic tuberculous spondylitis (Pott's disease) (PMID 42079494, 41657555).
- Severity ranges from moderate to severe.
- The course is progressive without treatment.
- No quality-of-life studies (EQ-5D, SF-36) exist. The expected effects are pain-related limits on mobility and, in rare cases, neurological deficit.

## 4. Genetic/Molecular Information

- **Causal human genes:** None. This is an infectious disease.
- **Pathogenic variants:** Not applicable in the ACMG sense. Host predisposition loci are covered in Section 2 (*HBB* via sickle cell disease; *IL12RB1*, *IL12B*; CGD genes).
- **Pathogen genetics:** Antimicrobial resistance is a recognized feature. For example, MDR *S.* Typhi spondylodiscitis was reported in 2026 (PMID 43013364). I did not retrieve pathogen genomic data such as resistance genes or MLST types for spinal isolates.
- **Epigenetics and chromosomal abnormalities:** None reported. Not applicable.

## 5. Environmental Information

- **Infectious agent:** *Salmonella enterica* (genus *Salmonella* in NCBI Taxonomy; taxon ID not retrieved here).
- **Exposure routes:** Ingestion of contaminated food or water, and travel to typhoid-endemic regions (PMID 42291979, 34987856).
- **Lifestyle factors:** No specific data. NSAID use has been suggested as a factor that may mask symptoms or modify the course (PMID 38550490).
- **Toxins and occupational factors:** None reported.

## 6. Mechanism / Pathophysiology

**Causal chain.** Steps 1–5 are reasoned from general salmonellosis biology and the clinical literature, not from experimental studies of disc infection.

1. Ingestion of *S. enterica* leads to invasion of the intestinal epithelium and M cells, and uptake by macrophages. *(Inferred; general salmonellosis biology, no source retrieved here.)*
2. Intracellular survival in macrophages leads to transient or sustained bacteremia (enteric fever or invasive NTS). Bacteremia is clinically documented in most reported cases; Chen et al. 2020 (PMID 32767972) warn clinicians to "remain cautious to the occurrence of osteomyelitis in patients with Salmonella septicemia."
3. Bacteria reach the vertebrae through the blood and lodge in the end-arteriolar metaphyseal (subchondral) vertebral bone next to the endplate. The lumbar spine is the predominant site (72%, PMID 9709878). *(Inferred: the anatomical route is assumed by analogy with other hematogenous spondylodiscitis.)*
   - **Branch A (host predisposition):** In sickle cell disease, bone infarction and necrosis, together with functional asplenia and complement defects, give *Salmonella* a place to colonize bone. This mechanism is proposed in the review at [PMC8274199](https://pmc.ncbi.nlm.nih.gov/articles/PMC8274199), not demonstrated experimentally.
   - **Branch B (vascular):** Seeding of atherosclerotic aortic intima leads to an infected aortic aneurysm. The aneurysm then spreads by contiguity to adjacent vertebrae, or both sites are seeded at the same time (PMID 41530883, 23981545, 33542000). In a meta-analysis of infective native aortic aneurysms, Peng et al. 2026 (PMID 42562227) report that "Salmonella was the leading genus globally (30.6%)" and that spondylodiscitis (11.7%) was a frequent concurrent focus.
4. Neutrophil and macrophage inflammation, cytokine release and osteoclast activation lead to destruction of the endplate and vertebral body. Infection spreads into the avascular disc, causing discitis. *(Inferred.)*
5. Spread into the paraspinal tissue and epidural space leads to psoas or epidural abscess and possible cord or root compression. Bone destruction leads to vertebral collapse and kyphosis (PMID 43013364, 41143074).
6. Together these produce the clinical picture: back pain, fever, raised inflammatory markers and, in some patients, neurological deficit.

**Suggested GO process labels (IDs not verified):** symbiont entry into host cell; neutrophil chemotaxis; inflammatory response; osteoclast differentiation; bone resorption; response to bacterium; interferon-gamma-mediated signaling pathway (relevant to host susceptibility).

**Suggested CL cell-type labels (IDs not verified):** macrophage; neutrophil; osteoclast; osteoblast; chondrocyte; nucleus pulposus cell.

**Molecular profiling:** There are no transcriptomic, proteomic, metabolomic, single-cell or CRISPR studies of *Salmonella* discitis. Not available.

## 7. Anatomical Structures Affected

UBERON labels are suggestions; their IDs were not verified.

- **Primary sites:** intervertebral disc; vertebral body and endplates. By region: lumbar vertebra (most often, especially L4/L5), thoracic vertebra (PMID 32767972) and less often cervical.
- **Secondary sites:**
  - Epidural space and spinal cord.
  - Psoas muscle.
  - Abdominal or thoracic aorta (infected aneurysm).
  - Other bones in multifocal disease (femur and tibia, PMID 33942967).
  - Lung (multifocal NTS in sickle cell disease; [PMC8759999](https://pmc.ncbi.nlm.nih.gov/articles/PMC8759999)).
- **Body systems:** musculoskeletal; nervous (when compression occurs); cardiovascular (aneurysm); digestive (portal of entry).
- **Tissue and cell level:** bone tissue, cartilage (endplate) and fibrocartilage (annulus fibrosus). Cell types are listed in Section 6.
- **Subcellular level:** In host macrophages, *Salmonella* lives in a *Salmonella*-containing vacuole (phagosome-derived). This is general biology, not specific to disc infection.
- **Laterality:** Midline structure. Paraspinal abscesses can be unilateral or bilateral (bilateral psoas involvement, PMID 41143074).

## 8. Temporal Development

- **Onset:**
  - Occurs at any age. Patients are bimodal: children (often with sickle cell disease, or immunocompetent; PMID 36553297) and older adults (≥50 years, linked to aortic aneurysm; PMID 9709878).
  - Onset is subacute to chronic, which often delays diagnosis.
  - It can follow a typhoid or diarrheal episode. In the Indian series, 50% had a documented history of typhoid fever (PMID 20938384).
- **Progression:**
  - Without treatment, the disease progresses to vertebral destruction, abscess and deformity.
  - Treated, most patients are cured. Relapse occurred in 9% (PMID 9709878).
  - There is no formal staging system.
- **Critical period:** Early diagnosis, before collapse or neurological compromise and before an aneurysm ruptures, determines the outcome.

## 9. Inheritance and Population

- **Inheritance:** Not applicable (infectious). Host susceptibility through sickle cell disease follows autosomal recessive inheritance of *HBB* variants.
- **Prevalence and incidence:** Not available.
  - This is a rare disease. Santos and Sapico could find only 44 English-language cases up to 1998 (PMID 9709878).
  - Katzouraki et al. found 21 pediatric NTS cases published between 1977 and 2020 (PMID 36553297).
  - Huang et al. found 69 adult *Salmonella* osteomyelitis patients from 67 articles published 1970–2019 (PMID 33942967).
  - In a 2026 individual-case meta-analysis of *Salmonella* osteomyelitis, vertebral involvement was "53% (72/136)" ([PMC12791220](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12791220/)).
- **Geography:** Typhoidal spondylodiscitis is mainly reported from South Asia (India, PMID 20938384 and 34987856). Non-typhoidal cases are reported worldwide.
- **Sex ratio and age distribution:** No pooled figures were retrieved.

## 10. Diagnostics

- **Microbiology (the gold standard):**
  - Blood cultures.
  - CT-guided or open biopsy of the disc or vertebra for culture, followed by antimicrobial susceptibility testing. Testing is essential given MDR strains (PMID 43013364).
  - Serotyping.
- **Serology:** The Widal test can support a diagnosis of typhoidal disease but is nonspecific. I did not retrieve a primary source for this point.
- **Inflammatory markers:** CRP, ESR and white blood cell count.
- **Imaging:**
  - MRI with gadolinium is the imaging modality of choice for spondylodiscitis and abscess.
  - CT is used for bone destruction and guided biopsy.
  - CT angiography is used to screen for an infected aortic aneurysm, particularly in patients over 50.
- **Histopathology:** Acute or chronic osteomyelitis with neutrophils. The absence of caseating granulomas helps distinguish it from tuberculosis.
- **Genetic testing:** Not used for diagnosis.
  - Hemoglobin electrophoresis is relevant if sickle cell disease is suspected.
  - Inborn-errors-of-immunity panels (*IL12RB1*, *IFNGR1*, CGD genes) are a consideration for unusual or recurrent invasive salmonellosis. This is inferred from the immunodeficiency literature in Section 2, not from a guideline.
- **Omics and molecular diagnostics:** No validated diagnostics. 16S rRNA PCR or metagenomic sequencing of biopsy tissue may help in culture-negative cases (not retrieved).
- **Differential diagnosis:**
  - Tuberculous spondylitis (Pott's disease), which *Salmonella* is repeatedly reported to mimic (PMID 42079494, 41657555).
  - *Staphylococcus aureus* spondylodiscitis, the most common cause overall (PMID 30335283).
  - Brucellosis.
  - Malignancy.
  - Modic degenerative changes.
- **Guideline:** The IDSA 2015 native vertebral osteomyelitis guideline (Berbari et al., PMID 26229122; executive summary PMID 26316526) is the general framework. Its content was not extracted here.
- **Screening:** None for asymptomatic individuals.

## 11. Outcome/Prognosis

- **Santos and Sapico (PMID 9709878, 44 cases):** "The overall cure rate was 61%, and the relapse rate was 9%." All deaths occurred in patients aged 50 or older who had infected aortic aneurysms.
- **Huang et al. (PMID 33942967):** "Antibiotic therapy alone was utilized in 30 cases, and 24 patients (80.00%) were eventually cured."
- **Amritanand et al. (PMID 20938384):** One of 11 immunocompetent patients died. The remaining 10 were followed for an average of 36 months.
- **2026 meta-analysis of *Salmonella* osteomyelitis ([PMC12791220](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12791220/)):** Surgery was required in 73%. Of 134 patients with outcome data, 7 (5.2%) died.
- **Mycotic aneurysm:** Mycotic abdominal aortic aneurysms carry "an overall mortality rate of 67%" (PMID 18463907, from introductory text rather than a formal abstract).
- **Complications:** epidural or psoas abscess; neurological deficit; vertebral collapse and kyphosis; aneurysm rupture; relapse.
- **Prognostic factors:** age ≥50; concurrent infected aneurysm; immunosuppression; delayed diagnosis.
- **Not available:** formal quality-of-life or disability outcome data.

## 12. Treatment

NCIT labels are suggestions; their IDs were not verified.

- **Empirical therapy:** A third-generation cephalosporin, ceftriaxone ("Ceftriaxone"), is recommended until susceptibilities are known (adult systematic review, [PMC8274199](https://pmc.ncbi.nlm.nih.gov/articles/PMC8274199)). Cephalosporins are increasingly preferred over fluoroquinolones because of rising resistance ([PMC10480304](https://pmc.ncbi.nlm.nih.gov/articles/PMC10480304)).
- **Fluoroquinolones** (ciprofloxacin, levofloxacin) are an oral or step-down option in adults. Tendinopathy has been reported during a 12-week levofloxacin course ([PMC8553272](https://pmc.ncbi.nlm.nih.gov/articles/PMC8553272), as summarized in a search result).
- **Sequential therapy:** In the *S.* Typhi series, "All four cases were treated successfully with variable duration of ceftriaxone followed by cotrimoxazole" (PMID 34987856). Other reported step-downs include amoxicillin (PMID 41530883) and azithromycin.
- **Duration:**
  - Children: 9.6 weeks on average (PMID 36553297).
  - Generally 6 weeks or more, longer when abscess or hardware is present.
- **Surgery:**
  - Debridement with or without fusion or instrumentation for abscess, instability, neurological deficit or failure of medical therapy. In the Indian series, 5 of 11 patients were treated with antibiotics alone and 5 had debridement with or without fusion or instrumentation (PMID 20938384).
  - For an infected aneurysm: resection, debridement and extra-anatomic or in-situ bypass, or endovascular repair (PMID 9709878, 33542000, 22759472).
- **Supportive care:** analgesia; bracing or immobilization; physiotherapy and rehabilitation.
- **Not applicable:** pharmacogenomics, gene or cell therapy, RNA therapies, immunotherapy, and registered trials (no NCT trials identified).

## 13. Prevention

- **Primary prevention:**
  - Food and water safety, sanitation and hand hygiene.
  - Typhoid vaccination (Vi conjugate vaccine) for travellers and endemic regions. This is general CDC/WHO practice; no specific source was retrieved here.
  - Avoiding reptile and poultry exposure for high-risk individuals.
  - In sickle cell disease: comprehensive care, including management of functional asplenia.
- **Secondary prevention:** In patients with *Salmonella* bacteremia, especially those over 50 or with sickle cell disease, keep a high index of suspicion for bone or vascular foci (PMID 32767972) and image early.
- **Tertiary prevention:** Complete a full antibiotic course, monitor inflammatory markers to detect relapse, and screen for aortic involvement.
- **Genetic counseling:** Relevant only for the underlying sickle cell disease or inborn error of immunity.

## 14. Other Species / Natural Disease

- *Salmonella* is zoonotic. Reservoirs include poultry, cattle, pigs and reptiles.
- I did not retrieve any reports of naturally occurring *Salmonella* discitis or spondylitis in animals. Discospondylitis in dogs is classically caused by other organisms (*Staphylococcus*, *Brucella canis*); this is general veterinary knowledge and was not retrieved.
- No OMIA entry is applicable.

## 15. Model Organisms

- **No dedicated animal model of *Salmonella* discitis or vertebral osteomyelitis was identified.**
- Mouse *S.* Typhimurium infection models systemic typhoid-like disease, not bone infection. Susceptible C57BL/6 and BALB/c mice, which carry a non-functional *Slc11a1/Nramp1* allele, die within days. *Nramp1*-intact strains such as 129S6 survive acute infection and develop chronic carriage ([search summary of PMC literature](https://pmc.ncbi.nlm.nih.gov/articles/PMC3769438)). No bone involvement is described in these models.
- General hematogenous and surgical osteomyelitis models exist, mainly for *S. aureus* ([Frontiers in Veterinary Science 2022 review](https://www.frontiersin.org/articles/10.3389/fvets.2022.879630/full)). Sickle cell mice (e.g., Townes HbSS) could in principle model the hemoglobinopathy predisposition, but no Salmonella–bone study in them was retrieved.
- **Limitation:** All mechanistic inferences above are extrapolated from general salmonellosis and osteomyelitis biology.

---

### Key evidence items

| PMID | Citation | Key quote or data |
|---|---|---|
| 9709878 | Santos & Sapico, Clin Infect Dis 1998 | "Fever (87% of cases) and back pain (92% of cases)"; "primarily lumbar involvement (72% of cases)"; "The overall cure rate was 61%, and the relapse rate was 9%." |
| 36553297 | Katzouraki et al., Children 2022 | "52.4% of the patients presented with fever, 90.5% had localized pain, and only 19% had gastroenteritis." |
| 33942967 | Huang et al., Orthop Surg 2021 | "Only 12 of the 67 cases in our data (17.91%) had diarrhea symptoms"; 80% cured with antibiotics alone |
| 20938384 | Amritanand et al., Spine 2010 | "Five (50%) patients had a documented history of typhoid fever." |
| 34987856 | Saravu et al., OMCR 2021 | "treated successfully with variable duration of ceftriaxone followed by cotrimoxazole." |
| 42562227 | Peng et al., Ann Vasc Surg 2026 | "Salmonella was the leading genus globally (30.6%)" in infective native aortic aneurysm |
| 38550490 | Hamada et al., Cureus 2024 | "Local pain and fever are important indicators for the diagnosis of spondylitis caused by nontyphoidal Salmonella." |
| 32767972 | Chen et al., BMC Surg 2020 | "remain cautious to the occurrence of osteomyelitis in patients with Salmonella septicemia" |

**Web sources:**
- [MONDO:8000004 – SAIL](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:8000004/)
- [Katzouraki 2022 – PMC9776940](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9776940/)
- [Adult review – PMC8274199](https://pmc.ncbi.nlm.nih.gov/articles/PMC8274199)
- [2026 meta-analysis abstract – PMC12791220](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12791220/)
- [Sickle cell NTS multifocal case – PMC8759999](https://pmc.ncbi.nlm.nih.gov/articles/PMC8759999)
- [PMC10480304](https://pmc.ncbi.nlm.nih.gov/articles/PMC10480304)
- [PMC8553272](https://pmc.ncbi.nlm.nih.gov/articles/PMC8553272)
- [PMC10977006](https://pmc.ncbi.nlm.nih.gov/articles/PMC10977006)
- [Rohilla et al., J Lab Physicians](https://thieme-connect.com/products/ejournals/pdf/10.4103/JLP.JLP_165_18.pdf)
- [Frontiers Vet Sci 2022](https://www.frontiersin.org/articles/10.3389/fvets.2022.879630/full)
- [PMC3769438](https://pmc.ncbi.nlm.nih.gov/articles/PMC3769438)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 33 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:8000004` (8 mentions) - the report calls it "retrieved", "SAIL"; MONDO calls it **salmonella discitis**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:8000004` - called "retrieved", "SAIL"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `GARD`.