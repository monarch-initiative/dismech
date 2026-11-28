---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-27T23:10:40.320872'
end_time: '2026-11-27T23:14:46.465139'
duration_seconds: 246.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Chronic Pyelonephritis
  mondo_id: MONDO:0001110
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: pyelonephritis, chronic
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
  web_search_requests: 23
  num_turns: 32
  total_cost_usd: 1.3894223499999998
  session_id: f97738de-576f-4031-a312-bcc01b4f6c8d
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  tool_calls: 42
  retrieval_calls: 36
  assistant_text_blocks: 3
citation_count: 61
reference_validation:
  total_references: 44
  verified: 44
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 5
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMC:PMC2873976
  - PMID:20850815
  - PMC:PMC10341809
  - PMID:28882930
  relevance_assessed: 44
  on_topic: 29
  off_topic: 1
  off_topic_references:
  - PMC:PMC10341809
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 2
  verified: 2
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: DOID:1076
    reported_labels:
    - cross-reference in the same record
    ontology_label: chronic pyelonephritis
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chronic Pyelonephritis
- **MONDO ID:** MONDO:0001110 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** pyelonephritis, chronic
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Chronic Pyelonephritis** covering all of the
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

Shell access to PubMed seems restricted; I'm switching to single curl calls and web search.

Gathering a final round of sources (XGP, mouse reflux model, transcriptomics), then writing the report.

**Interpretation and scope:** This report covers **chronic pyelonephritis (MONDO:0001110)** as it is clinically defined: kidney damage from infection that persists or keeps recurring, almost always on top of a structural problem in the urinary tract. Pathologists and pediatricians now often call the vesicoureteral reflux (VUR) form **reflux nephropathy**, so that literature is included. Xanthogranulomatous pyelonephritis (XGP), a rare chronic destructive variant, is covered briefly. **No causal gene is recorded for this entry, and none exists.** It is an acquired infectious and inflammatory disease. Germline variants act only as susceptibility factors: through innate-immunity genes such as *CXCR1* and *TLR4*, and through genes that cause the underlying VUR or urinary tract malformation, such as *PAX2*, *TNXB*, *GATA3*, *SLIT2* and *ROBO2*.

**Method limitations:** Direct PubMed E-utilities calls were not allowed in this session, and PubMed article pages often returned a cookie interstitial. Evidence therefore comes from web-search retrieval of PubMed, PMC, Bookshelf, MSD Manuals and other pages. PMIDs are given only where retrieved; otherwise PMC IDs or URLs are given. Quotes are taken from abstract or page text as retrieved and should be spot-checked against the full abstract before curation. Per instructions, I have **not** supplied ontology IDs (HPO, GO, CL, UBERON, CHEBI, NCIT) that I did not retrieve. Term *labels* are suggested for mapping, and only retrieved identifiers are stated.

---

## 1. Disease Information

**Overview.** Chronic pyelonephritis is "continuing pyogenic infection of the kidney that occurs almost exclusively in patients with major anatomic abnormalities. Reflux of infected urine into the renal pelvis is the usual mechanism. Causes include obstructive uropathy, struvite calculi, and, most commonly, vesicoureteral reflux (VUR)" ([MSD Manual Professional – Chronic Pyelonephritis](https://www.msdmanuals.com/professional/infectious-diseases/urinary-tract-infections-utis/chronic-pyelonephritis)).

The pathology is described as "patchy interstitial scarring, tubular atrophy, and loss of nephron mass." VUR "ultimately results in chronic interstitial nephritis, tubular atrophy, and renal scarring along with glomerular hypertrophy and secondary FSGS" ([MSD – Reflux nephropathy](https://www.msdmanuals.com/professional/infectious-diseases/urinary-tract-infections/reflux-nephropathy-chronic-pyelonephritis); [StatPearls NBK526055](https://ncbi.nlm.nih.gov/books/NBK526055)).

The concept is still debated. Radiopaedia notes "no definitive consensus as to whether the condition represents an active chronic infection, arises from multiple recurrent infections, or represents stable changes from a remote single infection" ([Radiopaedia](https://radiopaedia.org/articles/36717)).

**Identifiers retrieved:**

| System | Identifier |
|---|---|
| MONDO | MONDO:0001110, "Persistent pyelonephritis"; children of chronic kidney disease and pyelonephritis ([SAIL concept library](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0001110/)) |
| Disease Ontology | DOID:1076 (cross-reference in the same record) |
| ICD-10 | N11 Chronic tubulo-interstitial nephritis (includes chronic pyelonephritis; add B95–B97 for the organism) ([AAPC](https://www.aapc.com/codes/icd-10-codes/N11)) |
| ICD-10 | N11.0 Nonobstructive reflux-associated chronic pyelonephritis; VUR NOS is excluded and coded N13.7 ([NHS ClassBrowser](https://classbrowser.nhs.uk/ICD-10-5TH-Edition/vol1/block-n10-n16.htm)) |
| ICD-10 | N11.1 Chronic obstructive pyelonephritis ([FindACode](https://www.findacode.com/icd-10-cm/icd-10-cm-diagnosis-codes-N11-group.html)) |
| OMIM / Orphanet | None. This is not a Mendelian or rare-disease entity. |
| MeSH / ICD-11 | Not retrieved in this session. Look up "Pyelonephritis" and "Pyelonephritis, Xanthogranulomatous" in MeSH. |

**Synonyms:** pyelonephritis, chronic; reflux nephropathy (the VUR-associated form); chronic atrophic pyelonephritis ([PMID 739156](https://pubmed.ncbi.nlm.nih.gov/739156/)); chronic obstructive pyelonephritis; chronic pyelitis (ICD inclusion term). XGP is a subtype.

**Data source type:** Aggregated, disease-level resources: textbooks, guidelines, registries (ANZDATA), RCTs, meta-analyses and case series. No EHR-derived data were used.

## 2. Etiology

**Causal factors.** These are infectious and mechanical:
- **Infection:** ascending bacterial infection, most often *E. coli* and *Proteus mirabilis* ([MSD](https://www.msdmanuals.com/professional/infectious-diseases/urinary-tract-infections-utis/chronic-pyelonephritis)).
- **Structural substrate:** VUR (most common), obstruction or obstructive uropathy, and struvite stones (MSD).
- **Host inflammation:** inflammation, not bacterial genotype alone, appears to drive scarring ([PMID 20850815](https://pubmed.ncbi.nlm.nih.gov/20850815/); Olson et al. 2017, [PMID 28882930](https://pubmed.ncbi.nlm.nih.gov/28882930/)).

**Risk factors**
- **Clinical:** VUR, obstruction, kidney stones, neurogenic bladder and diabetes ([BMJ Best Practice](https://bestpractice.bmj.com/topics/en-us/552)).
  - In children after a first UTI, scarring was more common with VUR: "RR: 2.6 [95% CI: 1.7–3.9]" (Shaikh et al. 2010, [PMID 21059720](https://pubmed.ncbi.nlm.nih.gov/21059720/)).
  - Recurrent UTI was a risk factor for new scarring in a RIVUR secondary analysis ([PMC4702233](https://pmc.ncbi.nlm.nih.gov/articles/PMC4702233)).
  - Bladder and bowel dysfunction is also a risk factor ([Swedish reflux trial V, PMID 20488486](https://pubmed.ncbi.nlm.nih.gov/20488486/); [PMC3968988](https://pmc.ncbi.nlm.nih.gov/articles/PMC3968988)).
- **Demographic:** Medscape reports the disease is about twice as common in females, more common in children under 2, and about three times more common in white than African-American children ([Medscape](https://img.medscape.com/pi/iphone/medscapeapp/html/A245464-business.html)).
- **Genetic susceptibility:**
  - A 2023 systematic review and meta-analysis found pooled associations of pediatric UTI with variation in *CXCR1*, *IL8* (*CXCL8*), *TGF*, *TLR4* and *VDR*, but rated the credibility as weak ([PMID 38128862](https://www.pubmed.gov/38128862/)).
  - **CXCR1:** in Lundstedt et al. 2007, when reflux was excluded, "54% of the patients had CXCR1 sequence variants" ([PMID 17786197](https://pubmed.ncbi.nlm.nih.gov/17786197/)). The work started from IL-8 receptor (mIL-8Rh) mutant mice that developed acute pyelonephritis with severe tissue damage.
  - **ACE** insertion/deletion: the D allele was associated with scarring (OR 1.73, recessive model) in an earlier meta-analysis ([Pediatr Nephrol](https://link.springer.com/article/10.1007/s00467-010-1695-7)).
  - **VUR/CAKUT genes:** in a Chinese pediatric primary-VUR registry, a monogenic cause was found in 7.39% of patients (PAX2 n=4, TNXB n=3, GATA3 n=3, SLIT2 n=3, ROBO2 n=2, TBX18 n=2). "PAX2 mutation carriers (HR 5.1 …) and TNXB mutation carriers (HR 20.3 …)" had a higher risk of ESRD ([PMID 34059960](https://pubmed.ncbi.nlm.nih.gov/34059960/)).
  - In European cohorts, a large linkage and association scan found no major VUR locus ([PMC4780477](https://pmc.ncbi.nlm.nih.gov/articles/PMC4780477); review [PMC5468264](https://pmc.ncbi.nlm.nih.gov/articles/PMC5468264)).

**Protective factors**
- **Genetic:** common *TLR4* promoter variants "may protect against severe urinary tract infection" ([PMC2873976](https://pmc.ncbi.nlm.nih.gov/articles/PMC2873976/)).
- **Uromodulin (Tamm–Horsfall protein, UMOD):** the protein is protective in mouse knockouts (Bates et al., Kidney Int 2004;65:791–797; Mo et al., Am J Physiol Renal 2004;286:F795). Urinary uromodulin was studied against UTI risk in the Cardiovascular Health Study ([PMC5409878](https://pmc.ncbi.nlm.nih.gov/articles/PMC5409878/)).
- **Environmental:** prompt treatment of febrile UTI and correction of obstruction. Treatment-delay data were not retrieved.

**Gene–environment interaction.** Disease requires both a host factor (reflux or obstruction, innate-immune variants) and bacterial exposure. In mice, sterile reflux alone did not cause reflux nephropathy; reflux plus sustained kidney infection did ([Bowen et al. 2013, PMC3701213](https://pmc.ncbi.nlm.nih.gov/articles/PMC3701213/)). Tlr4-defective C3H/HeJ mice had more severe damage than C3H/HeN mice. Bacterial *papG II* was associated with acute pyelonephritis, while "scarring was predicted by host factors rather than bacterial virulence genes" (summary of [PMID 20850815](https://pubmed.ncbi.nlm.nih.gov/20850815/)).

## 3. Phenotypes

HPO IDs were not retrieved; these are label suggestions only.

| Phenotype (suggested HPO label) | Type | Onset / course | Frequency and evidence |
|---|---|---|---|
| Recurrent urinary tract infections / recurrent pyelonephritis | sign/symptom | childhood onward; episodic | The usual presentation ([MSD](https://www.msdmanuals.com/professional/infectious-diseases/urinary-tract-infections-utis/chronic-pyelonephritis)) |
| Fever, flank pain, dysuria (during flares) | symptom | episodic | Qualitative |
| Renal cortical scarring | imaging/pathology | after febrile UTI | 15% (95% CI 11–18) on follow-up DMSA after a first childhood UTI ([PMID 21059720](https://pubmed.ncbi.nlm.nih.gov/21059720/)) |
| Hypertension | sign | adolescent/adult; progressive | About 38% in 294 adults with reflux nephropathy ([PMID 7761049](https://pubmed.ncbi.nlm.nih.gov/7761049/)); 38–60% in a review ([PMC3216353](https://pmc.ncbi.nlm.nih.gov/articles/PMC3216353/)) |
| Proteinuria | lab | progressive | About 31% of adults ([PMID 7761049](https://pubmed.ncbi.nlm.nih.gov/7761049/)); ">100 mg/day" linked to irreversible decline ([PMID 9184449](https://pubmed.ncbi.nlm.nih.gov/9184449/)) |
| Chronic kidney disease / reduced GFR | lab | slow | "Most patients have adequate renal function for ≥ 20 years after onset" (MSD) |
| Small, irregular (atrophic) kidney; calyceal blunting | imaging | chronic | Classic finding (MSD; [Radiopaedia](https://radiopaedia.org/articles/36717)) |
| Focal segmental glomerulosclerosis (secondary) | pathology | late | Qualitative ([StatPearls](https://ncbi.nlm.nih.gov/books/NBK526055)) |
| Pre-eclampsia / pregnancy-related hypertension | sign | in pregnancy | Qualitative ([PMID 3330495](https://pubmed.ncbi.nlm.nih.gov/3330495/)) |

**Quality of life:** No EQ-5D, SF-36 or PROMIS data specific to chronic pyelonephritis were retrieved. Burden is expected to follow from recurrent infections, hospitalizations, CKD and dialysis.

## 4. Genetic / Molecular Information

- **Causal genes:** None. The disease is acquired.
- **Susceptibility genes:** *CXCR1*, *TLR4*, *CXCL8*, *VDR*, *TGFB1* and *ACE* (see Section 2), plus VUR/CAKUT genes *PAX2*, *TNXB*, *GATA3*, *SLIT2*, *ROBO2* and *TBX18* ([PMID 34059960](https://pubmed.ncbi.nlm.nih.gov/34059960/)).
- **ACMG classification:** Not applicable to susceptibility alleles. *PAX2* and other CAKUT variants are classified in their own monogenic disorders.
- **Variant types:** CXCR1 variants were heterozygous polymorphisms and rare mutations predicted to reduce CXCR1 expression ([PMID 17786197](https://pubmed.ncbi.nlm.nih.gov/17786197/), as summarized in [PMC4286230](https://pmc.ncbi.nlm.nih.gov/articles/PMC4286230/)). In TNXB-associated VUR, all variant carriers tested had joint hypermobility, with no excess high-grade reflux or scarring ([PMC4780477](https://pmc.ncbi.nlm.nih.gov/articles/PMC4780477)).
- **Allele frequencies (gnomAD), epigenetics, chromosomal abnormalities:** Not retrieved, and no disease-specific data were found.
- **Germline vs. somatic:** All are germline susceptibility variants.

## 5. Environmental Information

- **Infectious agents:** *Escherichia coli* (uropathogenic) and *Proteus mirabilis* are the most common causes ([MSD](https://www.msdmanuals.com/professional/infectious-diseases/urinary-tract-infections-utis/chronic-pyelonephritis)).
  - In XGP case series (693 cases), *P. mirabilis* was found in 18.5% of positive cultures and *E. coli* in 14.8% ([PMID 33827527](https://pubmed.ncbi.nlm.nih.gov/33827527/)).
  - *Proteus* urease makes urine alkaline, which leads to struvite stones and in turn to obstruction.
- **UPEC virulence factors:** P fimbriae (PapG adhesin binding Gal(α1-4)Gal) are "strongly associated with pyelonephritis in children" ([PMC10341809](https://pmc.ncbi.nlm.nih.gov/articles/PMC10341809/)). Hemolysin is associated with renal damage.
- **Lifestyle and other factors:** Bladder and bowel dysfunction and diabetes are risk factors (BMJ Best Practice). Metabolic acidosis worsened pyelonephritis in reflux-prone mice ([PMC7543054](https://pmc.ncbi.nlm.nih.gov/articles/PMC7543054/)). No toxin or occupational data were found.

## 6. Mechanism / Pathophysiology

**Causal chain:**
1. **Structural predisposition:** congenital VUR (sometimes from *PAX2*, *TNXB* or other CAKUT gene variants), obstruction or stones *lead to* retrograde flow or stasis of urine in the renal pelvis ([MSD](https://www.msdmanuals.com/professional/infectious-diseases/urinary-tract-infections-utis/chronic-pyelonephritis); [PMID 34059960](https://pubmed.ncbi.nlm.nih.gov/34059960/)).
2. **Bacterial ascent:** UPEC, using P fimbriae/PapG, or *Proteus* colonize the bladder and then the pelvis, which *results in* intrarenal reflux of infected urine into collecting ducts, preferentially at the poles ([PMC10341809](https://pmc.ncbi.nlm.nih.gov/articles/PMC10341809/); [Radiopaedia](https://radiopaedia.org/articles/36717)).
   - *Branch:* with *Proteus*, urease produces struvite stones, which *cause* obstruction, which feeds back into step 1.
3. **Innate recognition:** TLR4 on uroepithelial and tubular cells senses LPS, which *induces* IL-8/CXCL8 secretion. This *recruits neutrophils* through CXCR1 ([PMID 17786197](https://pubmed.ncbi.nlm.nih.gov/17786197/); [PMC4286230](https://pmc.ncbi.nlm.nih.gov/articles/PMC4286230/)).
   - *Branch A (too little response):* low CXCR1 means neutrophils get trapped and bacteria are not cleared, which *leads to* severe acute pyelonephritis and scarring (shown in mice; associated in humans).
   - *Branch B (too much response):* an excessive inflammatory response *causes* collateral tubular injury. In mice "the extent of fibrosis correlates most significantly with inflammation" ([Olson 2017, PMID 28882930](https://pubmed.ncbi.nlm.nih.gov/28882930/); related [PMC5283888](https://pmc.ncbi.nlm.nih.gov/articles/PMC5283888)). The steroid rationale rests on the same idea ([PMC10393849](https://pmc.ncbi.nlm.nih.gov/articles/PMC10393849/)).
4. **Tubulointerstitial injury:** tubular rupture *releases* Tamm–Horsfall protein (uromodulin) into the interstitium. This is associated with peritubular inflammation (a histological association; causation is inferred) ([PathologyOutlines](https://www.pathologyoutlines.com/topic/kidneychronicpyelo.html)).
5. **Repair and fibrosis:** repeated or persistent injury *results in* interstitial fibrosis, tubular atrophy with "thyroidization" (dilated tubules with colloid-like casts), and obliterative endarteritis. Together these produce a coarse cortical scar over a blunted calyx ([Brown Digital Pathology](https://www.brown.edu/Courses/Digital_Path/systemic_path/renal/cp1.html)).
6. **Nephron loss:** reduced nephron mass *leads to* compensatory glomerular hyperfiltration and hypertrophy, then *secondary FSGS* and proteinuria ([StatPearls](https://ncbi.nlm.nih.gov/books/NBK526055)). The hyperfiltration step is inferred from general CKD physiology.
7. **Clinical outcome:** hypertension (the renin-angiotensin link is inconsistent; [PMC3216353](https://pmc.ncbi.nlm.nih.gov/articles/PMC3216353/)) and progressive CKD, which *can lead to* ESKD ([PMID 7761049](https://pubmed.ncbi.nlm.nih.gov/7761049/)).
   - *XGP branch:* chronic obstruction plus infection *leads to* lipid-laden macrophage (xanthoma cell) granulomatous destruction of the kidney ([PMC8434833](https://pmc.ncbi.nlm.nih.gov/articles/PMC8434833)).

**Mechanism checklist:**
- **Pathways:** toll-like receptor 4 signaling, IL-8/CXCR1 chemotaxis, TGF-β-driven fibrosis (TGF variants per [PMID 38128862](https://www.pubmed.gov/38128862/)).
- **Suggested GO process labels:** toll-like receptor 4 signaling pathway; neutrophil chemotaxis; inflammatory response; defense response to Gram-negative bacterium; extracellular matrix organization / fibrosis.
- **Suggested CL labels:** neutrophil; macrophage (foam cell in XGP); kidney tubule epithelial cell; urothelial cell; fibroblast / myofibroblast.
- **Omics:** No human transcriptomic, proteomic, metabolomic, single-cell or spatial datasets specific to chronic pyelonephritis were retrieved.

## 7. Anatomical Structures Affected

UBERON IDs were not retrieved; these are labels only.
- **Primary:** kidney (renal cortex, renal papilla, renal pelvis, calyces) and the tubulointerstitium.
- **Upper and lower urinary tract:** ureter and bladder (the source of reflux).
- **Secondary:** cardiovascular system (hypertension); placenta and pregnancy (pre-eclampsia).
- **Tissues and cells:** tubular epithelium, interstitial connective tissue, arterioles (obliterative endarteritis); neutrophils, macrophages, fibroblasts.
- **Subcellular (suggested GO cellular component labels):** extracellular matrix; tubular lumen casts containing uromodulin.
- **Localization:** scars are most common at the upper pole ([MSD reflux nephropathy](https://www.msdmanuals.com/professional/infectious-diseases/urinary-tract-infections/reflux-nephropathy-chronic-pyelonephritis)). Disease can be unilateral or bilateral. Severe bilateral scarring predicts hypertension ([PMID 7761049](https://pubmed.ncbi.nlm.nih.gov/7761049/)). XGP is usually unilateral.

## 8. Temporal Development

- **Onset:** Insidious, after childhood febrile UTIs, especially under age 2 (Medscape). XGP presents mostly in middle-aged to elderly patients ([Medscape](https://img.medscape.com/pi/iphone/medscapeapp/html/A245464-business.html)).
- **Course:** Episodic infections are superimposed on slowly progressive scarring.
  - Scarring appears 5–24 months after UTI on DMSA ([MDedge summary of PMID 21059720](https://mdedge.com/content/renal-scarring-occurs-absence-vur)).
  - Kidney function typically lasts ≥20 years (MSD).
  - About 2% of children with VUR-related disease progress to renal failure ([StatPearls](https://ncbi.nlm.nih.gov/books/NBK526055)).
- **Remission:** VUR often resolves on its own, but "resolution of reflux does not appear to correct hypertension" (StatPearls).
- **Critical period:** Infancy and early childhood, when the growing kidney is most vulnerable to scarring. Early treatment of febrile UTI is the window for intervention.

## 9. Inheritance and Population

- **Inheritance:** Multifactorial. Primary VUR itself clusters in families, with heterogeneous monogenic causes in about 7% of the Chinese cohort ([PMID 34059960](https://pubmed.ncbi.nlm.nih.gov/34059960/)). Penetrance, anticipation, founder effects and carrier frequencies are not applicable or not retrieved.
- **Burden of kidney failure:** Reflux nephropathy accounted for about 7% of pediatric ESKD in ANZDATA 2006–2011 ([ANZDATA 2012](https://anzdata.org.au/wp-content/uploads/2013/01/2012c11_paediatric_v1.9.pdf)). Structural causes as a group accounted for 35.8% ([Orr et al., PMID 19373494](https://pubmed.ncbi.nlm.nih.gov/19373494/)). Reported global estimates range from 7% to 17% ([PMC2478704](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2478704/)).
- **Prevalence and incidence:** Population-level rates per 100,000 were not retrieved.
- **XGP frequency:** 0.6–1% of pyelonephritis cases ([Medscape](https://img.medscape.com/pi/iphone/medscapeapp/html/A245464-business.html)).
- **Sex ratio:** About 2:1 female:male (Medscape).

## 10. Diagnostics

- **Laboratory:**
  - Urinalysis and urine culture.
  - Serum creatinine / eGFR.
  - Urine protein (proteinuria is a prognostic marker; [PMID 9184449](https://pubmed.ncbi.nlm.nih.gov/9184449/)).
  - In XGP, resistance profiling matters: piperacillin/tazobactam resistance was 14.3% and ceftriaxone resistance 16.6% ([PMID 33827527](https://pubmed.ncbi.nlm.nih.gov/33827527/)).
- **Imaging:**
  - DMSA scintigraphy "is the gold standard for the diagnosis of acute pyelonephritis and renal scarring" ([StatPearls](https://ncbi.nlm.nih.gov/books/NBK526055)).
  - Ultrasound and CT show a "large, deep, segmental, coarse cortical scar usually extending to one or more of the renal calyces" ([Radiopaedia](https://radiopaedia.org/articles/36717)).
  - A voiding cystourethrogram (VCUG) detects VUR. The AAP 2011 guideline recommends renal-bladder ultrasound after a first febrile UTI at age 2–24 months and does not routinely recommend VCUG (Roberts et al., Pediatrics 2011;128:595; commentary [PMID 21873698](https://pubmed.ncbi.nlm.nih.gov/21873698/)).
- **Histopathology:** patchy interstitial fibrosis with chronic inflammation, thyroidization of tubules, interstitial Tamm–Horsfall protein (PAS-positive), periglomerular fibrosis, obliterative endarteritis, and early preserved glomeruli ([PathologyOutlines](https://www.pathologyoutlines.com/topic/kidneychronicpyelo.html)). XGP shows foamy macrophages.
- **Genetic testing:** Not used for diagnosis. A CAKUT/VUR gene panel (*PAX2*, *TNXB*, *GATA3*, *SLIT2*, *ROBO2*, *TBX18*) may be considered in familial or syndromic VUR. No WGS, CMA or omics diagnostics are established.
- **Differential diagnosis:**
  - Other chronic tubulointerstitial nephritides (drug-induced, analgesic nephropathy).
  - Renal dysplasia / hypoplasia, which looks similar on imaging but is congenital.
  - Renal infarct, tuberculosis.
  - For XGP: renal cell carcinoma.
  - ADTKD-*UMOD*.
- **Screening:** There is no population screening. Imaging is targeted after febrile UTI.

## 11. Outcome / Prognosis

- **Course:** Usually slow (MSD). In 294 adults with reflux nephropathy, about 38% had hypertension and about 31% had proteinuria ([PMID 7761049](https://pubmed.ncbi.nlm.nih.gov/7761049/)).
- **Prognostic factors:** proteinuria ("the worst prognostic feature," [PMID 739156](https://pubmed.ncbi.nlm.nih.gov/739156/)); diastolic hypertension; bilateral severe scarring; reduced GFR; and *PAX2* or *TNXB* variants ([PMID 34059960](https://pubmed.ncbi.nlm.nih.gov/34059960/)).
- **Pregnancy:** outcomes are good when kidney function is near normal and hypertension is absent; risk rises with creatinine at conception ([PMID 3330495](https://pubmed.ncbi.nlm.nih.gov/3330495/); [PMID 7924016](https://pubmed.ncbi.nlm.nih.gov/7924016/)).
- **Complications:** ESKD, hypertension, pre-eclampsia, stones, and XGP or abscess. After nephrectomy for XGP, complications occurred in 73% (n=8) in one 2023 series ([Ir J Med Sci](https://link.springer.com/10.1007/s11845-023-03496-2)).
- **Transplant:** Long-term kidney transplant outcomes in CAKUT, which includes reflux nephropathy, are reported in [PMID 31309282](https://pubmed.ncbi.nlm.nih.gov/31309282/).
- **Mortality and quality-of-life figures:** Not retrieved.

## 12. Treatment

NCIT IDs were not retrieved; these are labels only.
- **Antibiotics:** For acute flares, treat febrile UTI for 7–10 days, orally where feasible (AAP; [PMC4173959](https://pmc.ncbi.nlm.nih.gov/articles/PMC4173959/)). For chronic disease, long-term antibiotics (MSD).
- **Antimicrobial prophylaxis (trimethoprim-sulfamethoxazole):**
  - **RIVUR** (NCT00405704; n=607; [PMID 24795142](https://pubmed.ncbi.nlm.nih.gov/24795142/)) halved recurrence (RR 0.55) but did not reduce scarring in the primary analysis. 63% of breakthrough *E. coli* isolates were resistant on prophylaxis vs 19% on placebo.
  - **PRIVENT** (Craig et al., NEJM 2009;361:1748; n=576) reduced recurrence modestly.
  - **Swedish reflux trial IV** reported renal damage outcomes by treatment arm ([PMID 20494369](https://pubmed.ncbi.nlm.nih.gov/20494369/)).
- **Adjuvant corticosteroids:** In the DEXCAR RCT, scarring was 22% with dexamethasone vs 21% with placebo (p=0.907), with "no evidence for an adjuvant corticosteroid treatment recommendation" ([PMID 35041042](https://pubmed.ncbi.nlm.nih.gov/35041042/)). A meta-analysis of 5 RCTs (n=498) found 14.1% vs 27.3% scarring ([PMC10393849](https://pmc.ncbi.nlm.nih.gov/articles/PMC10393849/)). This is experimental and unresolved.
- **CKD and hypertension care:** antihypertensives and renoprotection. No reflux nephropathy-specific RCTs were retrieved.
- **Surgery and interventions:** correction of obstruction, stone removal, and VUR correction (endoscopic injection or ureteral reimplantation). Nephrectomy is used for a nonfunctioning infected kidney (MSD) and is the main treatment for XGP; laparoscopic approaches are increasing and partial nephrectomy is an option for focal XGP ([PMC8434833](https://pmc.ncbi.nlm.nih.gov/articles/PMC8434833)). Dialysis and transplantation are used for ESKD.
- **Advanced therapies:** Gene, cell, RNA and targeted therapies are not applicable.
- **Pharmacogenomics:** none specific to this disease. TMP-SMX and G6PD considerations were not retrieved.

## 13. Prevention

- **Primary:** prompt diagnosis and treatment of febrile UTI in infants; treating bladder and bowel dysfunction; adequate hydration (not retrieved as evidence). There is no licensed UTI vaccine; none was retrieved.
- **Secondary:** renal ultrasound after a first febrile UTI (AAP 2011), DMSA in selected children, and blood pressure and proteinuria monitoring.
- **Tertiary:** prophylaxis in selected high-grade VUR (RIVUR, PRIVENT), surgical correction, blood pressure control, and pre-conception counseling ([PMID 3330495](https://pubmed.ncbi.nlm.nih.gov/3330495/)).
- **Genetic counseling:** relevant only for familial VUR or CAKUT.

## 14. Other Species / Natural Disease

NCBI Taxon IDs were not retrieved.
- **Pigs (sows):** the porcine cystitis-pyelonephritis complex is "a leading cause of mortality in sows," primarily caused by *Actinobaculum suis*, often with *E. coli*. Its incidence fell after artificial insemination was widely adopted ([Merck Vet Manual](https://www.merckvetmanual.com/en-ca/urinary-system/infectious-diseases-of-the-urinary-system-in-large-animals/porcine-cystitis-pyelonephritis-complex); Isling et al. 2010, [Acta Vet Scand](https://link.springer.com/doi/10.1186/1751-0147-52-48)).
- **Cattle:** contagious bovine pyelonephritis is caused by the *Corynebacterium renale* group (*C. renale*, *C. pilosum*, *C. cystitidis*). Herd prevalence is 0.5–1.5%, and up to one-third of affected animals die or are culled ([Anipedia](https://anipedia.up.ac.za/resources/corynebacterium-renale-group-infections/974)).
- **Dogs and cats:** no data retrieved.
- **Zoonotic potential:** none established.

## 15. Model Organisms

- **Mouse, male C3H/HeN surgical bladder-inoculation model** with UPEC: produces ascending pyelonephritis, abscesses and fibrosis, and antibiotic-treated mice develop scars. This models post-treatment scarring and kidney function loss (Olson et al., Dis Model Mech 2017, [PMID 28882930](https://pubmed.ncbi.nlm.nih.gov/28882930/); [PMC5719254](https://pmc.ncbi.nlm.nih.gov/articles/PMC5719254/)).
- **Mouse, C3H strains with natural VUR** (C3H/HeN vs Tlr4-defective C3H/HeJ): kidney infection is necessary for reflux nephropathy, and sterile reflux alone is not enough ([PMC3701213](https://pmc.ncbi.nlm.nih.gov/articles/PMC3701213/)). The same background was used to show metabolic acidosis worsens disease ([PMC7543054](https://pmc.ncbi.nlm.nih.gov/articles/PMC7543054/)).
- **Genetic mouse models:**
  - mIL-8Rh (Cxcr2) knockout mice develop severe acute pyelonephritis and scarring ([PMID 17786197](https://pubmed.ncbi.nlm.nih.gov/17786197/)).
  - Umod (Tamm–Horsfall protein) knockout mice are more susceptible to UTI (Bates 2004; Mo 2004).
  - Pax2 1Neu+/- mice show VUR ([PMID 17881463](https://pubmed.ncbi.nlm.nih.gov/17881463/)); Pax2/Emx2 compound heterozygotes also do ([PMC3123351](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3123351/)).
  - Robo2 mutants have CAKUT ([PMC4962383](https://pmc.ncbi.nlm.nih.gov/articles/PMC4962383/)).
- **Pig and minipig:** high-pressure sterile reflux causes scarring ([PMID 6086232](https://pubmed.ncbi.nlm.nih.gov/6086232/)). This supports a "water-hammer" component that conflicts with the mouse data, so the mechanism differs by species.
- **Methods:** methods to detect VUR and obstruction in mice are described in [PMID 22639276](https://pubmed.ncbi.nlm.nih.gov/22639276/) and [PMC3094056](https://pmc.ncbi.nlm.nih.gov/articles/PMC3094056/).
- **Limitations:** mouse models compress time (weeks rather than decades). Most models use males because surgical inoculation is needed to get reflux in males, whereas human disease is female-predominant. Hypertension and pregnancy complications are poorly modeled. Resources: MGI, IMSR.

---

### Evidence types
- **Human clinical:** RCTs (RIVUR, PRIVENT, Swedish reflux trial, DEXCAR), meta-analyses, cohorts, registries.
- **Mouse in vivo:** Olson 2017, Bowen 2013, Cxcr2/Umod/Pax2/Robo2 mice.
- **Porcine experimental:** sterile reflux study.
- **Computational / genetic association:** 2023 meta-analysis ([PMID 38128862](https://www.pubmed.gov/38128862/)).

### Gaps
1. No HPO, GO, CL, UBERON, CHEBI or NCIT identifiers were retrieved; only labels are given.
2. There are no population prevalence or incidence data, and no quality-of-life or mortality data.
3. No omics datasets specific to this disease were found.
4. Several abstracts were seen only as search snippets, not full PubMed records.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 44 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 44 |
| On topic | 29 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC2873976` *(abstract only)*: "may protect against severe urinary tract infection"
  - closest text in source: "Since TLR4 plays a vital role in susceptibility to urinary tract infection (UTI), promoter sequences were obtained from children with mild or severe disease"
- `PMID:20850815` *(abstract only)*: "scarring was predicted by host factors rather than bacterial virulence genes"
  - closest text in source: "CONCLUSIONS: Bacterial virulence factors and host factors are associated with the occurrence of acute pyelonephritis"
- `PMC:PMC10341809` *(abstract only)*: "strongly associated with pyelonephritis in children"
  - Text part not found as substring: 'strongly associated with pyelonephritis in children' (note: only abstract available for PMID:37445714, full text may contain this excerpt)
- `PMID:28882930` *(abstract only)*: "the extent of fibrosis correlates most significantly with inflammation"
  - closest text in source: "A minority of treated mice displayed persistent histological abscess at the end of treatment, despite microbiological cure of pyelonephritis; a matching fraction of mice 1 month later exhibited renal scars featuring fibrosis and ongoing inflammatory infiltrates"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC10341809` (5 mentions) - Urinary Tract Infections Caused by Uropathogenic Escherichia coli: Mechanisms of Infection and Treatment Options.
  - shared terms: uti, infection

Weighed against this report's own most characteristic terms: `reflux`, `vur`, `scarring`, `kidney`, `pyelonephritis`, `disease`, `renal`, `xgp`, `msd`, `nephropathy`, `cause`, `pax2`, `uti`, `infection`, `hypertension`, `chronic`, `cakut`, `gene`, `febrile`, `label`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:1076` (1 mention) - the report calls it "cross-reference in the same record"; DOID calls it **chronic pyelonephritis**