---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-16T09:28:30.386788'
end_time: '2026-11-16T09:32:32.487291'
duration_seconds: 242.1
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: TPP2 Deficiency
  mondo_id: MONDO:0030971
  category: Mendelian
  causal_genes: TPP2
  omim_id: OMIM:619220
  synonyms: IMD78
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
  web_search_requests: 10
  num_turns: 25
  total_cost_usd: 2.586999495
  session_id: 6473c1de-f1c7-4a3b-8815-ae5bee055912
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 20
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 9
  off_topic: 1
  off_topic_references:
  - PMID:19841172
  needs_review: true
  validator_version: 0.6.0
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0030971
    reported_labels:
    - MONDO
    ontology_label: immunodeficiency 78 with autoimmunity and developmental delay
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TPP2 Deficiency
- **MONDO ID:** MONDO:0030971 (if available)
- **Causal gene(s):** TPP2
- **OMIM:** OMIM:619220
- **Synonyms:** IMD78
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **TPP2 Deficiency** covering all of the
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

Still researching TPP2 deficiency. PubMed's web pages are blocked, so I'm pulling the abstracts through NCBI E-utilities instead.

Checking which of the repository's cached references are actually about TPP2, which is a different gene from TPP1/CLN2.

# TPP2 Deficiency (Immunodeficiency 78 with autoimmunity and developmental delay, IMD78): research report

**Identifiers to curate against:** MONDO:0030971 · OMIM #619220 · causal gene **TPP2** (tripeptidyl peptidase 2, chromosome 13q33.1) · autosomal recessive.

## How to read this report

- **Abstracts were not quoted in full.** PubMed's web pages returned a cookie wall, and the sandbox refused direct E-utilities calls. Europe PMC confirmed the titles and PMIDs, but only short excerpts could be copied. Every quote below came from a search snippet or a short Europe PMC excerpt. **Treat each one as a lead.** Run `just fetch-reference PMID:<id>` and check every snippet against the cached abstract before it goes into the YAML.
- **No ontology CURIEs are given.** Phenotype, GO, CL, UBERON and NCIT terms are suggested by label only, because repository rules forbid writing identifiers from memory. Look each one up with `runoak` or the term caches when binding it. HGNC and OMIM gene IDs are left for the same lookup.
- **Do not confuse TPP2 with TPP1.** Most `references_cache/` hits for "tripeptidyl peptidase" are about TPP1 (CLN2 neuronal ceroid lipofuscinosis, treated with cerliponase alfa). That is a different gene, enzyme and disease. TPP2 is a giant cytosolic serine exopeptidase, not a lysosomal enzyme.

---

## 1. Disease information

**Overview.** TPP2 deficiency is a very rare autosomal recessive inborn error of immunity caused by biallelic loss-of-function variants in **TPP2**. Its core features are:
- combined immunodeficiency with recurrent viral and respiratory infections;
- early-onset autoimmune cytopenias, often Evans syndrome (autoimmune haemolytic anaemia plus immune thrombocytopenia);
- premature immunosenescence of T and B cells;
- in many patients, developmental delay or intellectual disability.

A milder adult-onset form, caused by missense variants, presents as chronic sterile brain inflammation that mimics multiple sclerosis.

| Field | Value | Source |
|---|---|---|
| MONDO | MONDO:0030971 | user-supplied |
| OMIM | #619220, "Immunodeficiency 78 with autoimmunity and developmental delay" (IMD78) | OMIM, via [MedGen](https://https.ncbi.nlm.nih.gov/medgen/1785772) and [PanelApp](https://panelapp.genomicsengland.co.uk/panels/398/gene/TPP2) |
| ICD-10 | D81.4 listed by a secondary source | [Altmeyers](https://www.altmeyers.org/en/internal-medicine/immunodeficiency-78-with-autoimmunity-and-developmental-delay-157115); not verified in WHO ICD |
| Orphanet / MeSH | Not found; check Orphadata (`just fetch-reference ORPHA:…` if a code exists) | n/a |
| Synonyms | IMD78; TPP2 deficiency; tripeptidyl peptidase II deficiency; TPPII deficiency; "Early-onset Evans syndrome, immunodeficiency and premature immunosenescence" | [rarediseases.info.nih.gov](https://rarediseases.info.nih.gov/assets/singles/17766.json) |
| IUIS classification | Listed in the IUIS inborn errors of immunity tables. Both are already cached: `PMID_35748970` (2022) and `PMID_41608114` (2024) | repo cache |
| Data basis | Aggregated case reports. About 14 published patients | [humandiseasegenes.nl](https://humandiseasegenes.nl/tpp2/professionals) |

**Naming.** Under the `entry-naming` skill, "TPP2 Deficiency" covers exactly one gene, so it passes the scope rule. The OMIM title and "IMD78" should go in `synonyms`.

## 2. Etiology

- **Cause.** The disease is purely genetic: biallelic germline TPP2 variants with loss or reduction of TPP2 protein or function. No environmental cause is known.
- **Genetic risk factors.**
  - Consanguinity is the main risk factor. Reported families include Arab, Syrian, Jordanian and Swiss ones.
  - There is a **Swiss founder allele**: a 4.4 kb deletion of exons 20–23 on a shared chromosome 13 haplotype (PMID:33586135).
- **Protective factors.** None known.
- **Gene–environment interaction.** Viral infections, especially herpesviruses, appear to trigger or worsen cytopenias and leukopenia (PMID:25414442). This is a clinical observation, not a demonstrated mechanism.

## 3. Phenotypes

The phenotype splits into two forms.
- **(A) Severe childhood-onset multisystem form:** about 10 patients, mostly with truncating variants.
- **(B) Adult-onset MS-like sterile neuroinflammation:** 4 patients, all with missense variants.

Patient counts come from [humandiseasegenes.nl](https://humandiseasegenes.nl/tpp2/clinical-characteristics). Frequencies are approximate given about 14 cases.

| Phenotype | Type | Form / onset | Frequency (qualitative) | Suggested HPO label (look up ID) | Key PMID |
|---|---|---|---|---|---|
| Evans syndrome (AIHA + ITP) | sign / lab | A, infancy to early childhood | frequent | Autoimmune hemolytic anemia; Autoimmune thrombocytopenia | 25414442 |
| Autoimmune cytopenias / pancytopenia, progressive leukopenia | lab | A | frequent | Leukopenia; Pancytopenia | 25414442 |
| Recurrent viral infections (e.g. CMV, EBV) | symptom | A | frequent | Recurrent viral infections | 25414442 |
| Recurrent respiratory infections, otitis media | symptom | A and B | common | Recurrent respiratory infections; Recurrent otitis media | 33682069 |
| Combined immunodeficiency, lymphopenia | lab | A; mild lymphopenia in B | frequent | Combined immunodeficiency; Lymphopenia | 25414442 |
| Developmental delay / intellectual disability | behavioural | A | common | Global developmental delay; Intellectual disability | 25525876, 33586135 |
| Antinuclear and other autoantibodies | lab | A | reported | Antinuclear antibody positivity | 25414442 |
| Autoimmune hepatitis, thyroiditis | sign | A | occasional | Autoimmune hepatitis; Autoimmune thyroiditis | humandiseasegenes.nl |
| Hepatosplenomegaly / lymphoproliferation | sign | A | occasional | Hepatosplenomegaly | 25414442 (verify) |
| Chronic sterile brain inflammation / demyelination mimicking MS | sign / imaging | B, adult | all 4 form B cases | CNS demyelination; Multiple sclerosis-like… (search HPO) | 30533531 |
| Psoriasis | sign | B | 2 of 4 | Psoriasiform dermatitis | humandiseasegenes.nl |
| Warts, eczema, asthma, paronychia, history of ITP | sign | mild childhood case | single case | Verruca vulgaris; Eczema; Asthma | 33682069 |

**Disease course.**
- Untreated, the immunodeficiency and autoimmunity are progressive.
- The neurological phenotype does not appear to respond to HSCT.
- Quality of life is dominated by refractory cytopenias, infections and neurodevelopmental impairment. No formal QoL instrument data exist.

**Stratifying.** A `has_subtypes` split could be justified:
- **Severe childhood multisystem.** Truncating or null alleles. The 4.4 kb deletion, the frameshift and the c.1913+5G>A splice variant belong here, although the splice case was milder.
- **Adult sterile neuroinflammation.** Missense alleles, p.Cys28Gly and p.Thr676Ile.

## 4. Genetic and molecular information

**Gene.** TPP2, tripeptidyl peptidase 2, on 13q33.1. Bind HGNC by lookup; the lowercase `hgnc:` CURIE is still needed. The protein is a subtilisin-family serine peptidase that assembles into a giant homo-oligomeric complex of about 6 MDa. It removes N-terminal tripeptides from oligopeptides, acting downstream of the proteasome.

**Reported variants** (all biallelic germline, mostly homozygous):

| Variant | Type | Phenotype | Reference |
|---|---|---|---|
| Homozygous frameshift abolishing protein expression (exact HGVS to be read from the paper) | frameshift, LoF | Evans syndrome and immunodeficiency in 2 siblings | PMID:25414442 |
| Variants reported by Lu et al. (HGVS to extract) | LoF | infections, autoimmunity, neurodevelopmental delay | PMID:25525876 |
| 4.4 kb deletion, exons 20–23 (NM_003291.4) | structural deletion → frameshift / PTC; Swiss founder | 4 individuals, 2 families: immunodeficiency, autoimmunity, intellectual disability | PMID:33586135 |
| c.1913+5G>A | splice region; predicted truncation removing the regions needed for dimerization | mild phenotype, 15-year-old girl (described as the 7th case) | PMID:33682069 |
| c.82T>G, p.Cys28Gly | missense | 3 Syrian siblings with sterile brain inflammation mimicking MS | PMID:30533531 |
| c.2027C>T, p.Thr676Ile | missense | 1 Jordanian patient with MS (from 826 MS exomes screened) | PMID:30533531 |

- **Mechanism class.** Loss of function (`functional_impact_category: LOSS_OF_FUNCTION`). Missense alleles probably act as hypomorphs (`PARTIAL_LOSS_OF_FUNCTION` only if a source states it).
- **Genotype–phenotype.** Severe patients mostly carry truncating or null alleles, while the MS-like adults carry missense variants ([humandiseasegenes.nl](https://humandiseasegenes.nl/tpp2/professionals/molecular-characteristics)).
- **Not established:**
  - ClinVar classifications and gnomAD frequencies were not retrieved. Check both.
  - No ClinGen gene–disease validity record was found. Leave `gene_disease_validity` absent unless a `CGGV:` record exists.
  - PanelApp rates TPP2 **green** (high evidence, biallelic) on both its primary immunodeficiency and intellectual disability panels.
  - No modifier genes, epigenetic changes or chromosomal abnormalities have been reported.

## 5. Environmental information

There are no environmental, lifestyle or toxic causes. Viral infections act as clinical precipitants and opportunistic pathogens, but not as causal agents, so do not bind `infectious_agent`.

## 6. Mechanism and pathophysiology

**Causal chain**

1. **Biallelic TPP2 LoF variants** → absent or reduced TPP2 protein (frameshift and deletion alleles abolish expression; PMID:25414442, 33586135).
2. **Loss of cytosolic tripeptidyl exopeptidase activity** downstream of the proteasome → impaired recycling of proteasome-generated peptides into free amino acids, giving **intracellular amino-acid insufficiency** (PMID:25525876, shown in cells).
3. **Branch A, metabolic (Lu et al. 2014):** amino-acid shortage → compensatory **increase in lysosome number** → lysosomes degrade **hexokinase-2 by chaperone-mediated autophagy** → **reduced glycolysis** → reduced effector cytokine output (IFN-γ, IL-1β) → impaired antiviral and effector immunity → **recurrent and viral infections**. Demonstrated in patient and knockout cells; the link to clinical infection is inferred.
4. **Branch B, survival and senescence:** TPP2 loss activates cell-death and senescence programmes under proliferative stress → **CD8⁺ T cells with a senescent phenotype**, poor proliferation and enhanced staurosporine-induced apoptosis (PMID:25414442, patient cells), plus **lymphopenia and leukopenia**. Mouse knockouts show premature CD8 senescence, thymic involution and lymphopenia with age (PMID:18362329).
5. **Branch C, antigen presentation:** **increased MHC class I surface expression** on patient cells (PMID:25414442). TPP2 contributes to some MHC-I peptide trimming, but in vivo knockout studies show it is largely dispensable for this (PMID:19841172). How raised MHC-I contributes to disease is unclear.
6. **Premature immunosenescence of B cells** → expansion of **T-bet⁺ CD11c⁺ age-associated B cells** plus autoantibodies (ANA, anti-nucleolar, anti-cytoplasmic) → **autoantibody-mediated destruction of red cells and platelets** → **Evans syndrome**, plus other organ autoimmunity (hepatitis, thyroiditis). The link from age-associated B cells to cytopenia is associative, not proven.
7. **Branch D, CNS (inferred):** TPP2 dysfunction in brain or immune cells → **chronic sterile neuroinflammation and demyelination** (MS-like) and **neurodevelopmental impairment**. The mechanism is undetermined. TPP2 is strongly upregulated in MS brain tissue (PMID:30533531). A 2024 mouse study links TPP2 depletion to calcium and lipid dyshomeostasis and dementia in female mice (PMID:38389851; model organism only, and not yet read).

**Suggested ontology anchors (labels only; look up IDs)**
- **GO:** tripeptidyl-peptidase activity; proteolysis; cellular amino acid homeostasis; glycolytic process (DECREASED); chaperone-mediated autophagy (INCREASED); lysosome organization; cellular senescence / T cell senescence; T cell proliferation (DECREASED); apoptotic process (INCREASED); antigen processing and presentation of peptide antigen via MHC class I; B cell activation; interferon-gamma production (DECREASED).
- **CL:** CD8-positive, alpha-beta T cell; B cell (age-associated B cells; NCIT/CL may lack a specific term, so use the `preferred_term`); erythrocyte; platelet; neuron or oligodendrocyte for the CNS branch.
- **GO cellular component:** cytosol; lysosome.

**Molecular profiling.** No public transcriptomic, proteomic or single-cell dataset specific to TPP2 deficiency was found. Run `just discover-datasets TPP2_Deficiency` and triage for relevance.

## 7. Anatomical structures

- **Primary systems:** immune system (blood, bone marrow, lymphoid organs, thymus) and haematopoietic system (red cells, platelets, leukocytes).
- **Secondary systems:**
  - brain and CNS white matter (neurodevelopment; MS-like demyelination in form B);
  - liver (autoimmune hepatitis; one patient had a liver transplant);
  - thyroid;
  - skin (psoriasis, warts, eczema);
  - spleen (splenomegaly, splenectomy).
- **Suggested UBERON labels:** blood, bone marrow, spleen, thymus, brain white matter, liver, thyroid gland.
- **Subcellular:** cytosol, where TPP2 functions; lysosome (the expanded compartment).
- **Lateralization:** not applicable (systemic).

## 8. Temporal development

- **Onset:**
  - Severe form: infancy to early childhood. Evans syndrome began in infancy in the Stepensky siblings.
  - Mild splice case: childhood ITP, then a milder course into adolescence.
  - MS-like form: adulthood.
- **Course:** chronic and progressive without HSCT. Cytopenias relapse and are often refractory, and infections worsen leukopenia. The neurological course in form B was described as mild and non-progressive in the Syrian family (PMID:30533531).
- **Critical window:** early diagnosis enables immune surveillance and timely HSCT before refractory autoimmunity or fatal infection (PMID:33586135).

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (bind the HPO autosomal recessive inheritance term by lookup). Penetrance looks complete for the severe form; expressivity is variable.
- **Prevalence:** unknown. About 14 patients were described worldwide by 2021 (10 severe, 4 adult MS-like), and the condition is probably underdiagnosed. Use `measure_type: CASES_IN_LITERATURE` with `prevalence_class: ULTRA_RARE` or `NOT_YET_DOCUMENTED`.
- **Founder effect:** Swiss exon 20–23 deletion (PMID:33586135).
- **Populations and consanguinity:** consanguineous Middle Eastern families (Syrian, Jordanian, and others, per Stepensky and Lu) and Swiss families.
- **Sex ratio:** no bias expected.
- **Not reported:** carrier frequency, anticipation, germline mosaicism.

## 10. Diagnostics

**Laboratory work-up**
- full blood count;
- direct antiglobulin test (Coombs);
- platelet antibodies;
- lymphocyte subsets: CD4/CD8, naive/memory, senescent CD8 markers such as CD57⁺ and CD28⁻;
- B-cell phenotyping for CD11c⁺ T-bet⁺ age-associated B cells;
- immunoglobulins;
- autoantibodies (ANA);
- viral PCR (CMV, EBV);
- liver and thyroid autoimmunity panels.

**Specialist and research tests:** increased MHC class I on lymphocytes; absent TPP2 protein on immunoblot; T-cell proliferation assays.

**Imaging:** brain MRI for white-matter inflammation or demyelination in the adult form. CSF may show inflammatory changes; verify against PMID:30533531.

**Genetic testing**
- Exome or genome sequencing, or an inborn errors of immunity / immune dysregulation panel. TPP2 is on Genomics England PanelApp panels for primary immunodeficiency, immune dysregulation and intellectual disability.
- Exome sequencing can miss the 4.4 kb deletion. The Swiss patients were diagnosed only after **genome** analysis (PMID:33586135), which favours genome sequencing or CNV-aware analysis.

**Differential diagnosis** (other monogenic Evans syndrome and ALPS-like disorders; see cached PMID:34447369 and PMID:30349415):
- ALPS (FAS, FASLG, CASP10);
- CTLA4 haploinsufficiency;
- LRBA deficiency;
- STAT3 gain of function;
- KRAS/NRAS-associated RALD;
- common variable immunodeficiency.

The CNS form must be distinguished from true multiple sclerosis.

**Screening:** no newborn screening exists. TREC levels are not reported as abnormal. Cascade carrier testing and prenatal or preimplantation testing are possible in families with known variants.

**Coding the diagnosis:** LOINC codes such as the direct antiglobulin test and platelet count can go in `diagnosis[].measurements`, but bind them through `just loinc-seed-cache` only.

## 11. Outcome and prognosis

- **Mortality is high without transplant.** In one summary, 3 of 5 patients treated with splenectomy, HSCT or orthotopic liver transplantation died; HSCT gave the best outcome ([humandiseasegenes.nl](https://humandiseasegenes.nl/tpp2/professionals/management)). OMIM, via MedGen, notes that many patients die young but that successful HSCT may be curative.
- **Causes of death and morbidity:** refractory cytopenias, infections, transplant complications.
- **HSCT does not appear to change the neurological phenotype.**
- **Prognostic factors:** truncating alleles (severe) versus missense (mild); response to immunosuppression; access to an HLA-matched donor.

## 12. Treatment

| Intervention | Role | Evidence | Suggested NCIT label (look up ID) | `therapeutic_modality` |
|---|---|---|---|---|
| Allogeneic HSCT. In Stepensky's case: HLA-identical sibling donor, conditioning with fludarabine, low-dose busulfan, thiotepa and ATG. At 6 months: 97% donor chimerism, no autoimmunity, off immunosuppression | only curative option for haematological and immune disease | PMID:25414442 (single case) | Hematopoietic Cell Transplantation | CELL_THERAPY |
| Corticosteroids, IVIG | first line for cytopenias | case-level; general Evans syndrome practice (PMID:30349415) | Pharmacotherapy + agent; Immunoglobulin Therapy (verify) | SMALL_MOLECULE / OTHER |
| Rituximab, mycophenolate, sirolimus, cyclosporine | second line for refractory cytopenias | reported in TPP2 cases (verify per paper) and general Evans syndrome practice | Pharmacotherapy + agent (rituximab, CHEBI/NCIT) | MONOCLONAL_ANTIBODY / SMALL_MOLECULE |
| Splenectomy | refractory cytopenias; high infection risk | case reports | Splenectomy | SURGERY |
| Antimicrobial and antiviral prophylaxis; Ig replacement | supportive | expert practice | Supportive Care | OTHER |
| Liver transplantation | performed for liver disease in one patient | humandiseasegenes.nl | Organ Transplantation | SURGERY |

- **Experimental:** Atallah et al. speculate about enzyme replacement by analogy with TPP1/CLN2. This is a hypothesis only, with no trial. Do not use cerliponase evidence here.
- No ClinicalTrials.gov trials are specific to TPP2 deficiency.
- No pharmacogenomic data.

## 13. Prevention

- **Primary and secondary:** genetic counselling, carrier testing in consanguineous or founder populations, and prenatal or preimplantation diagnosis for known familial variants.
- **Tertiary:** immune monitoring, infection prophylaxis, early HSCT referral, and avoiding live vaccines in combined immunodeficiency (general practice for inborn errors of immunity; not TPP2-specific evidence).

## 14. Other species and natural disease

- No naturally occurring animal disease is recorded; OMIA was not searched in depth.
- TPP2 is highly conserved from bacteria-like ancestors through *Drosophila* and mouse.
- **Mouse orthologue:** *Tpp2*. Get the MGI ID from Alliance and bind with the `MGI:` prefix under `animal_models[].genes`.

## 15. Model organisms

**TPPII knockout mouse (PMID:18362329, PNAS 2008)**
- Young mice are grossly normal.
- After 1 year: higher mortality, an aged appearance, thymic involution, strong lymphopenia, and premature senescence of CD8⁺ (but not CD4⁺) T cells after anti-CD3 stimulation.
- **Recapitulates:** the immunosenescence and lymphopenia branch (`PARTIALLY_RECAPITULATES`).
- **Does not reproduce:** early-onset Evans syndrome or neurodevelopmental delay. That gap is a candidate `HUMAN_MODEL_MISMATCH` discussion.

**Other mouse and cell studies**
- **TPPII-deficient mice, MHC-I presentation (PMID:19841172):** largely normal MHC class I antigen presentation in vivo. Useful as refuting or limiting evidence for an antigen-presentation-driven mechanism.
- **Patient and knockout cells, Lu et al. (PMID:25525876):** amino-acid shortage, lysosome expansion, HK2 degradation by chaperone-mediated autophagy, and reduced glycolysis. Lineage is `IN_VITRO` / `MODEL_ORGANISM`; split evidence items by source.
- **Female TPP2-depleted mice (PMID:38389851, 2024):** presenile dementia through calcium and lipid dyshomeostasis. Possibly relevant to the CNS branch, but not yet read.

---

## Next steps for the KB entry

1. Fetch and cache these references: PMID:25414442, 25525876, 33586135, 33682069, 30533531, 18362329, 19841172, and optionally 27829551 (review) and 38389851. Then pull exact snippets and run `just count-verified-snippets`.
2. Get the exact HGVS for the Stepensky and Lu variants from full text, since abstracts may give protein changes only.
3. Run `just check-genereviews`. No GeneReviews chapter is expected for TPP2; confirm it offline.
4. Look up every HPO, GO, CL, UBERON, NCIT and HGNC CURIE before writing it.

## Sources
- [Stepensky et al. 2015 Blood, PMC4463807](https://pmc.ncbi.nlm.nih.gov/articles/PMC4463807) · [RareConnect PDF](https://www.rareconnect.org/uploads/documents/early-onset-evans-syndrome-immunodeficiency-and-premature-immunosenescence-associated-with-tripeptidyl-peptidase-ii-deficiency.pdf)
- [Lu et al. 2014 Cell (Birmingham record)](https://research.birmingham.ac.uk/en/publications/dual-proteolytic-pathways-govern-glycolysis-and-immune-competence)
- [Atallah et al. 2021 Clin Genet](https://zendy.io/title/10.1111/cge.13942) · [Serval record](https://serval.unil.ch/fr/notice/serval:BIB_ED69F497CA09)
- [Stockdale et al. 2021 J Clin Immunol, PMC7937547](https://pmc.ncbi.nlm.nih.gov/articles/PMC7937547)
- [Reinthaler et al. 2018 Neurol Genet, PMC6244017](https://pmc.ncbi.nlm.nih.gov/articles/PMC6244017)
- [Huai et al. 2008 PNAS, PMC2278225](https://pmc.ncbi.nlm.nih.gov/articles/PMC2278225)
- [humandiseasegenes.nl TPP2: clinical](https://humandiseasegenes.nl/tpp2/clinical-characteristics), [molecular](https://humandiseasegenes.nl/tpp2/professionals/molecular-characteristics), [management](https://humandiseasegenes.nl/tpp2/professionals/management)
- [MedGen IMD78](https://https.ncbi.nlm.nih.gov/medgen/1785772) · [PanelApp TPP2 (PID)](https://panelapp.genomicsengland.co.uk/panels/398/gene/TPP2) · [PanelApp TPP2 (ID)](https://panelapp.genomicsengland.co.uk/panels/285/gene/TPP2/) · [PanelApp Australia](https://panelapp-aus.org/panels/229/gene/TPP2/)
- [Altmeyers IMD78](https://www.altmeyers.org/en/internal-medicine/immunodeficiency-78-with-autoimmunity-and-developmental-delay-157115) · [GARD JSON](https://rarediseases.info.nih.gov/assets/singles/17766.json) · [GeneCards TPP2](https://genecards.org/card/TPP2) · [KEGG H02526](https://www.kegg.jp/entry/H02526)
- Europe PMC REST records for PMIDs 25414442, 25525876, 33586135, 33682069, 30533531, 18362329, 19841172
- Repository cache: `references_cache/PMID_30349415.md` (Evans syndrome review naming TPP2), `PMID_34447369.md`, `PMID_35748970.md`, `PMID_41608114.md`, `PMID_37792884.md`

## Reference Validation

Checked with `linkml-reference-validator` 0.6.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 9 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:19841172` (2 mentions) - Analysis of the role of tripeptidyl peptidase II in MHC class I antigen presentation in vivo.
  - shared terms: cell

Weighed against this report's own most characteristic terms: `tpp2`, `patient`, `infection`, `evan`, `syndrome`, `variant`, `cell`, `disease`, `autoimmunity`, `immune`, `immunodeficiency`, `form`, `deficiency`, `cytopenias`, `gene`, `brain`, `humandiseasegene`, `deletion`, `viral`, `look`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030971` (2 mentions) - the report calls it "MONDO"; MONDO calls it **immunodeficiency 78 with autoimmunity and developmental delay**