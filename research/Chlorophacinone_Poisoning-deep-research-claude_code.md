---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-09-03T14:21:41.511704'
end_time: '2026-09-03T14:35:00.004451'
duration_seconds: 798.49
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Chlorophacinone Poisoning
  mondo_id: ''
  category: Environmental
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
  - claude-opus-5
  web_search_requests: 16
  num_turns: 58
  total_cost_usd: 4.18958675
  session_id: 9ee57a85-891e-4a71-9882-564d71875e1f
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 15
reference_validation:
  total_references: 48
  verified: 47
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.021
  relevance_assessed: 47
  on_topic: 31
  unresolved_references:
  - PMID:34748846
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 45
  verified: 45
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 15
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0000132
    reported_labels:
    - not verified this session
    ontology_label: Menorrhagia
  - term_id: HP:0001903
    reported_labels:
    - not verified this session
    ontology_label: Anemia
  - term_id: HP:0001259
    reported_labels:
    - not verified
    ontology_label: Coma
  - term_id: NCBITaxon:52604
    reported_labels:
    - unverified
    ontology_label: Pleurocapsales
  - term_id: NCBITaxon:50636
    reported_labels:
    - unverified
    ontology_label: Trigoniophthalmus
  - term_id: NCBITaxon:45480
    reported_labels:
    - unverified
    ontology_label: Cynomys ludovicianus
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chlorophacinone Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Chlorophacinone Poisoning** covering all of the
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

I'll pull the existing curation artifacts in this worktree, then search the current literature.

Base cache read. Now the current literature and identifiers.

# Chlorophacinone Poisoning: Research Report

**Prepared:** 2026-09-03. **Target entry:** `kb/disorders/Chlorophacinone_Poisoning.yaml` (currently an 18-line stub). **Category:** Environmental.

A note before the content. The human literature on chlorophacinone specifically is thin. PubMed returns 109 records for the term overall, and most are ecotoxicology, analytical chemistry, or rodent-resistance work. The number of published human chlorophacinone cases with individual clinical detail is in the single digits. Nearly every strong clinical statement below therefore comes from the anticoagulant rodenticide class literature, where brodifacoum and bromadiolone dominate the case material. I have marked class-level inference wherever it occurs. Do not let a class citation become a chlorophacinone claim in the entry.

---

## 1. Disease Information

### Overview

Chlorophacinone poisoning is an acquired, toxin-induced coagulopathy. Chlorophacinone is an indanedione anticoagulant rodenticide. It inhibits vitamin K epoxide reductase in the hepatocyte, which halts regeneration of reduced vitamin K, which halts gamma-carboxylation of coagulation factors II, VII, IX and X. The clinical result is a functional deficiency of those factors and a bleeding diathesis. Onset is delayed by days. Duration is measured in weeks.

The compound was introduced in the mid-1960s by Lipha SA of France. It is used against rats, mice, voles and prairie dogs, in bait and as a tracking powder.

### Chemical identity

| Field | Value | Source |
|---|---|---|
| Name | chlorophacinone | |
| Systematic | 2-[(4-chlorophenyl)(phenyl)acetyl]-1H-indene-1,3(2H)-dione | |
| CAS | 3691-35-8 | NPIC / EPA |
| Formula | C23H15ClO3 | PubChem CID 19402 |
| MW | 374.8 g/mol (some sources give 364.8; see caveat) | |
| CHEBI | **CHEBI:81796** (label: `chlorophacinone`) | OLS4, verified |
| PubChem CID | 19402 | verified |

Caveat on molecular weight. One search result reported 364.8 for C23H15ClO3. The formula computes to roughly 374.8. Verify against PubChem directly before curating a number. I did not resolve this; the PubChem page did not render through the fetch tool.

### Disease identifiers

**There is no MONDO term for chlorophacinone poisoning, and none for anticoagulant rodenticide poisoning.** I searched MONDO through OLS4 for `rodenticide poisoning`, `poisoning by rodenticide`, and `poisoning`. The third returned 32 terms. None covers rodenticides, coumarins, warfarin, or anticoagulants.

| Resource | Value | Status |
|---|---|---|
| MONDO | **MONDO:0029000** `poisoning` | Only available anchor. A `skos:broadMatch` at best. A new MONDO term request is the correct move. |
| ICD-10-CM | **T60.4X-** Toxic effect of rodenticides | Not independently verified against the ICD browser this session |
| ICD-11 | NE61 (toxic effect of pesticides) family | Not verified |
| MeSH | `Rodenticides` (D012377), `Indans`, `Anticoagulants`, `Vitamin K 1`. Cached PubMed records for chlorophacinone cases index under `Indans/blood, poisoning` and `Rodenticides/poisoning` | Verified in `references_cache/PMID_10216974.md` |
| OMIM | Not applicable. Not a genetic disease. | |
| Orphanet | No ORPHA term found for this concept | |

Because ICD-10-CM T60.4 is not specific to chlorophacinone, electronic health record case-finding cannot separate this entity from brodifacoum, bromadiolone or bromethalin exposure without a toxicology result. That is a real constraint on any EHR-derived phenotype algorithm.

### Synonyms

- chlorophacinone intoxication
- chlorophacinone toxicosis (veterinary usage)
- indandione anticoagulant rodenticide poisoning
- Rozol poisoning, Caid poisoning, Liphadione, Raviac, Ramucide, Drat, Topitox (trade names; Rozol and Caid are the ones that appear in the literature)
- Sometimes grouped under "superwarfarin poisoning", though see the classification note below.

### A classification conflict worth recording

Chlorophacinone is repeatedly described as a **first-generation** anticoagulant, and equally repeatedly grouped with the **long-acting anticoagulant rodenticides / superwarfarins**. Both usages appear in authoritative sources. Watt et al. put it squarely in the long-acting group (PMID:16499407, verbatim): *"This group includes the second generation 4-hydroxycoumarins brodifacoum, bromadiolone, difenacoum, flocoumafen and the indanedione derivatives chlorophacinone and diphacinone."* Meanwhile EPA and pest-control sources call it a first-generation multiple-feed anticoagulant, and Esther et al. list it with warfarin and coumatetralyl as first-generation (PMID:24781908, verbatim): *"Anticoagulants of the first generation (warfarin, chlorophacinone, coumatetralyl) as well as bromadiolone and difenacoum are not an option for the control of resistant Norway rats."*

The conflict is real, not an error in one source. "Generation" is a rodent-efficacy term. "Long-acting" is a human-toxicology term. Chlorophacinone is first-generation by rodent potency and long-acting by human duration of effect. Curate that distinction explicitly, because it changes clinical expectation.

### Data provenance

Aggregated, not per-patient. Poison-center registries (America's Poison Centers NPDS, French PCC data in PMID:21171851), forensic case series (PMID:40974629), and individual published case reports. No disease registry exists. No EHR cohort study specific to chlorophacinone was found.

---

## 2. Etiology

### Causal factor

A single environmental cause: ingestion, and less often inhalation or dermal absorption, of chlorophacinone. The compound is the sufficient cause. There is no genetic disease here.

King and Tran, on routes (PMID:26239439, verbatim): *"Inhalational, transcutaneous, and oral routes of exposure have been documented. Most exposures are unintentional."*

Documented exposure circumstances:

1. **Unintentional pediatric ingestion of bait.** The dominant scenario by count. Almost always small amounts.
2. **Deliberate self-poisoning.** The scenario that produces severe published cases. Lagrange et al. describe a 33-year-old man who ingested 1875 mg (PMID:10216974). Vogel et al. describe an 18-year-old who ingested about 100 mg (PMID:3222685).
3. **Occupational exposure.** Reported for the class (PMID:16499407).
4. **Homicidal or covert administration.** Two homicides among 88 anticoagulant rodenticide cases (PMID:40974629). The 2007 chlorophacinone fatality was investigated as suspicious (PMID:16716547).
5. **Contaminated food chain.** Chlorophacinone transfers into sheep milk (PMID:32645465). A human dietary route exists in principle.
6. **Environmental / secondary, in animals.** Predators and scavengers eating poisoned rodents.

Ecological terms (ECTO) for these routes were not searched this session. `exposure to rodenticide` and `exposure to chemical via ingestion` are the shapes to look for. Bind nothing you have not resolved.

### Risk factors

**Environmental and behavioral.** Age under 6 years is the leading risk factor for exposure by count. King and Tran report that across 25 years of US poison-center data *"there were 315951 exposures reported with nearly 90% among children"* (PMID:26239439, verbatim). Berny et al. found French exposures *"mostly occurred in young children, with no or very limited clinical severity"* and that circumstances were *"predominantly accidental in man (77%)"* (PMID:21171851, verbatim).

Other environmental risk factors: agricultural and rural residence where field use is permitted, occupational pest control, psychiatric illness and suicidality, and access to stored bait. The lamb and calf epizootics both trace to old or spilled bait left accessible (PMID:17037620, PMID:35000500).

**Host factors, likely but not demonstrated for chlorophacinone.** Pre-existing liver disease, baseline vitamin K deficiency, malabsorption, concurrent warfarin or direct oral anticoagulant therapy, antibiotic-induced gut flora suppression, and low dietary vitamin K intake should all amplify the coagulopathy. I found no study testing any of these against chlorophacinone. Curate them as inference or not at all.

**Genetic risk factors in humans.** None established. This is a place where a plausible story could be curated into the entry incorrectly, so state the reasoning. Human `VKORC1` (**hgnc:23663**) promoter variant -1639G>A (rs9923231) and `CYP2C9` (**hgnc:2623**, not verified this session) star alleles govern warfarin dose requirement. It is mechanistically reasonable that VKORC1 haplotype modulates sensitivity to chlorophacinone, since the drug target is the same enzyme. **I found no study demonstrating this.** Do not curate a VKORC1 pharmacogenomic risk claim for chlorophacinone with a warfarin citation. That is the Named Entity Confusion failure in a different coat.

Note also that chlorophacinone is not known to be a CYP2C9 substrate in the way warfarin is, so the CYP2C9 analogy is weaker still.

**Genetic factors in rodents, which are real and well documented.** These are resistance, not human risk, and belong in the entry as target-species biology. See §4 and §14.

### Protective factors

- Adequate vitamin K1 status. Directly protective and the basis of therapy.
- Formulation dilution. Baits carry 0.005 percent to 0.25 percent active ingredient, so an accidental mouthful delivers a trivial dose. This is why 90 percent of exposures are children and 98 percent are benign.
- No genetic protective factor is known in humans.

King and Tran on outcome (PMID:26239439, verbatim): *"Fortunately, only 2% of all exposures result in morbidity or mortality."*

### Gene-environment interaction

In humans: not demonstrated. In target and non-target rodents: the central story of the field. `Vkorc1` coding variants reduce chlorophacinone binding and produce survival on lethal bait. Bermejo-Nogales et al. (PMID:35970209, verbatim): *"Computational analysis of binding predictions found out that the brown rat S149I mutation predicted a high reduction of the binding affinity of chlorophacinone and brodifacoum ARs."* That evidence is `COMPUTATIONAL` in the docking part and `MODEL_ORGANISM` in the sequencing part. Split the evidence items.

---

## 3. Phenotypes

The phenotype is a bleeding diathesis with a latent period. Category assignments below follow the dismech convention (`Clinical`, `Laboratory`).

### Frequency data

The best available frequency data is class-level, from the 88-case forensic synthesis (PMID:40974629). Verbatim: *"Multi-organ hemorrhage was the predominant clinical manifestation, with hematuria being the most frequently reported symptom (n = 39)."* That is 39 of 88, roughly 44 percent, in a series enriched for severe and fatal cases. It is not a population frequency and must not be curated as one. `measure_type` reasoning applies: this is a case-series proportion in a selected sample.

### Clinical phenotypes

| Phenotype | HPO term | ID | Notes |
|---|---|---|---|
| Hematuria | Hematuria | **HP:0000790** | Most frequently reported bleeding site in the class series (PMID:40974629, PMID:26239439). Documented in the fatal chlorophacinone case (PMID:16716547, MeSH `Hematuria/chemically induced`) |
| Epistaxis | Epistaxis | **HP:0000421** | Listed by Watt et al.; the presenting sign in the lamb epizootic |
| Gingival bleeding | Gingival bleeding | **HP:0000225** | Watt et al. |
| Bruising / ecchymoses | Subcutaneous hemorrhage | **HP:0001933** | "widespread bruising" (PMID:16499407) |
| Gastrointestinal hemorrhage | Gastrointestinal hemorrhage | **HP:0002239** | |
| Rectal bleeding | Hematochezia | **HP:0002573** | |
| Intracranial hemorrhage | Intracranial hemorrhage | **HP:0002170** | The leading cause of death. Verbatim (PMID:26239439): *"Deaths were most commonly associated with intracranial hemorrhage."* |
| Subarachnoid hemorrhage | Subarachnoid hemorrhage | **HP:0002138** | Documented in the fatal chlorophacinone case (PMID:16716547) |
| Menorrhagia | Menorrhagia | HP:0000132 (not verified this session) | |
| Hematoma | Internal hemorrhage | **HP:0011029** | Use for haemorrhage into internal organs |
| Anemia | Anemia | HP:0001903 (not verified this session) | *"anaemia may result"* (PMID:16499407) |
| Abnormal bleeding, general | Abnormal bleeding | **HP:0001892** | Parent term |
| Bleeding responsive to vitamin K | Bleeding ameliorated by vitamin K | **HP:4000177** | A genuinely apt term. It exists. Verified in OLS4. |
| Flank pain | (search `HP` for flank pain; not verified) | | *"haematuria with flank pain"* (PMID:16499407) |
| Coma | Coma | HP:0001259 (not verified) | Terminal. MeSH `Coma/chemically induced` on PMID:16716547 |
| Hypovolemic shock | (not verified) | | *"Severe blood loss may result in hypovolaemic shock, coma and death"* (PMID:16499407) |
| Cerebral venous thrombosis | Cerebral venous thrombosis (not verified) | | The paradoxical presentation. See below. |

### Laboratory phenotypes

| Finding | HPO term | ID | Data |
|---|---|---|---|
| Prolonged prothrombin time | Prolonged prothrombin time | **HP:0008151** | Median PT 100 s (range 11.6 to 300) in 88 cases (PMID:40974629) |
| Prolonged aPTT | Prolonged partial thromboplastin time | **HP:0003645** | Median aPTT 110 s (range 3.71 to 212) (PMID:40974629) |
| Elevated INR | (no clean HP term; use `HP:0008151`) | | Median INR 9, range 0.98 to 38.2 (PMID:40974629) |
| Increased PIVKA-II | Increased PIVKA-II | **HP:0045063** | Under-used. Mechanistically the most specific marker available. |
| Reduced factor X activity | Reduced factor X activity | **HP:0008321** | Vogel et al. tracked factors VII and X (PMID:3222685) |

Verbatim on the coagulation panel (PMID:40974629): *"Coagulation function tests revealed average values of aPTT, PT, and INR of aPTT: 110 (3.71 ∼ 212) s, PT: 100 (11.6 ∼ 300) s and INR: 9 (0.98 ∼ 38.2), respectively, all significantly exceeding normal ranges."* Note that snippet is list-shaped, carries three separate measurements, and would support three distinct claims. Split it if you use it more than once, and check what each node actually consumes.

King and Tran, verbatim: *"Most patients present with coagulation assay values beyond measurable limits."*

### The paradoxical thrombosis phenotype

A patient anticoagulated by a vitamin K antagonist can thrombose. Protein C and protein S are also vitamin K dependent and have shorter half-lives than factors II, IX and X, so early in the exposure the anticoagulant pathway falls before the procoagulant pathway does. That mechanism is standard for warfarin-induced skin necrosis. Papin et al. report the chlorophacinone instance, and their title states the finding: *"Lethal paradoxical cerebral vein thrombosis due to suspicious anticoagulant rodenticide intoxication with chlorophacinone"* (PMID:16716547). The abstract itself is short and does not state the protein C mechanism. Verbatim, all it says is: *"They review the literature and discuss particularities of anticoagulant rodenticide intoxication, as well as the apparent contradiction between anticoagulant intoxication and lethal thrombosis."*

That abstract cannot carry a protein C claim. King and Tran independently confirm the phenomenon at class level, verbatim: *"Long-acting anticoagulant rodenticide-induced paradoxical thrombosis and thrombotic complications accompanying hemostatic therapy have also been observed."* Use that for the phenomenon and find a separate source for the protein C explanation, or mark it inferred.

### Phenotype characteristics

- **Onset.** Adult and pediatric both, entirely determined by exposure. Not age-linked.
- **Latency.** Verbatim (PMID:40974629): *"The median latency period was 4 days (range: 1 ∼ 30)."* Watt et al., verbatim: *"The first clinical signs of bleeding may be delayed and patients may remain anticoagulated for several days (warfarin) or days, weeks or months (long-acting anticoagulants) after ingestion of large amounts."*
- **Severity.** Bimodal. Trivial in accidental pediatric ingestion. Severe to fatal in deliberate large ingestion.
- **Progression.** Episodic and relapsing during treatment. This is the signature. Vogel et al., verbatim: *"Under high dose vitamin K therapy the Quick was rapidly corrected but fell again on each vitamin K withdrawal."* Rebound is the expected course, not a complication.
- **Duration.** Verbatim (PMID:3222685): *"Prothrombin time (and vitamin K dependent factors VII and X) finally normalized only 7 weeks after chlorophacinone ingestion."*

### Quality of life

No EQ-5D, SF-36 or PROMIS data exists for this condition. Not measured. The functional burden is dominated by prolonged hospitalization, months of daily vitamin K, and repeated coagulation monitoring. Treatment courses in the class averaged 168 days (PMID:26239439). That figure is class-level and driven by brodifacoum. Chlorophacinone courses are shorter. Do not transfer it.

---

## 4. Genetic / Molecular Information

**No causal human gene. This is an acquired toxic condition.** The genetics in this entry are of three other kinds.

### The molecular target

`VKORC1`, vitamin K epoxide reductase complex subunit 1. HGNC **hgnc:23663**, verified in use at `kb/disorders/Vitamin_K_Dependent_Coagulation_Factor_Deficiency.yaml:181`. Enzyme activity term: **GO:0047057** `vitamin-K-epoxide reductase (warfarin-sensitive) activity` (verified via OLS4). The warfarin-insensitive paralog activity is GO:0047058, corresponding to `VKORC1L1`.

The downstream carboxylase is `GGCX`, gamma-glutamyl carboxylase, HGNC **hgnc:4247**, likewise already bound in the sibling entry. Its process term is **GO:0017187** `peptidyl-glutamic acid carboxylation`.

### Germline human disease at the same locus, for differential purposes

Biallelic `VKORC1` variants cause vitamin K-dependent coagulation factor deficiency type 2, and biallelic `GGCX` variants cause type 1. That entry already exists in this knowledge base as `Vitamin_K_Dependent_Coagulation_Factor_Deficiency`. It is the key genetic differential for an unexplained multi-factor deficiency, and it should be cross-linked. Distinct `VKORC1` missense variants cause hereditary warfarin resistance.

### Rodent resistance genetics

This is the substantive genetic content of the topic.

Esther et al. (PMID:24781908, verbatim): *"Polymorphisms in the vitamin K epoxide reductase complex subunit 1 (VKORC1) gene and respective substitutions of amino acids in the VKOR enzyme are the major cause for rodenticide resistance. Resistant Norway rats in Germany are characterized by the Tyr139Cys genotype, which is spread throughout the northwest of the country."*

Bermejo-Nogales et al. (PMID:35970209, verbatim): *"We identified genotypic vkorc1 variations corresponding to amino acid changes at the VKORC1 protein at the S149I - S149T and the E155K - E155Q mutations, depending on the rodent species."*

Known resistance substitutions relevant to chlorophacinone:

| Species | Variant | Effect on chlorophacinone | Evidence class |
|---|---|---|---|
| *Rattus norvegicus* | Tyr139Cys | Resistance; chlorophacinone not recommended | MODEL_ORGANISM (PMID:24781908) |
| *Rattus norvegicus* | Ser149Ile | Predicted large reduction in chlorophacinone binding affinity | COMPUTATIONAL (PMID:35970209) |
| *Rattus rattus* | Ser149Thr, Glu155Lys, Glu155Gln | Slight reduction for bromadiolone; chlorophacinone not the reported target | COMPUTATIONAL (PMID:35970209) |
| *Mus musculus* | Tyr139Cys, Leu128Ser, spretus-type quadruple (Arg12Trp/Ala26Ser/Ala48Thr/Arg61Leu) | Resistance | MODEL_ORGANISM (PMID:24781908) |

There is direct in-vivo dose-response work on Y139C house mice (PMID:36181415, *Pest Manag Sci*, 2022): "Anticoagulant rodenticide blood-clotting dose-responses and resistance factors for Tyrosine139Cysteine (Y139C) heterozygous- and homozygous-resistant house mice (Mus musculus)". I did not retrieve its abstract. Fetch it before citing a resistance factor number.

### Variant classification, allele frequency, somatic origin, epigenetics, chromosomal abnormalities

Not applicable. No ClinVar entries. No gnomAD frequencies relevant. No somatic component. No epigenetic mechanism reported. No chromosomal abnormality.

---

## 5. Environmental Information

Chlorophacinone is the environmental factor. Everything in this section is exposure characterization.

**Formulation and use.** Grain-based ready-to-use baits at 0.005 to 0.25 percent active ingredient, plus tracking powder. Rozol Prairie Dog Bait, used in the raptor study, is 0.005 percent (PMID:35633457, verbatim: *"Rozol, 0.005% active ingredient chlorophacinone, CPN"*).

**Persistence, and the fact that distinguishes chlorophacinone from the superwarfarins.** Chlorophacinone is markedly less persistent in tissue than bromadiolone or brodifacoum. A 2021 stereochemistry study (PMID:33130091) reports bromadiolone with a hepatic half-life of roughly 10 to 30 days against chlorophacinone at roughly one day in voles. I have that only through a fetch summary, not from the verbatim abstract, so treat the quoted fragment as unverified until refetched. In black-tailed prairie dogs, peak liver residue reached 5.499 mg/kg at day 3 with an estimated half-life near 6 days (PMID:25997570). Same caveat: summary, not verified quote.

**Milk transfer.** Verbatim (PMID:32645465): *"Chlorophacinone was detected in milk on day 2 post-exposure and remained quantifiable for at least 7 days in milk of these 11 ewes. Concentrations in milk were much lower than in plasma and decreased quickly (mean half-life of 2 days)."* Their conclusion, verbatim: *"consumption of dairy products derived from these ewes after a one-week withdrawal period would pose low risk to consumers."*

**Non-target environmental burden.** Chlorophacinone appears in wild raptors and mammals. In south-eastern France over 12 years, first-generation compounds were the minority. Verbatim (PMID:34748846): *"While SGARs were commonly detected (97.4% of positive samples), first-generation ARs were rarely found (7.7% of positive samples)."* And the trend, verbatim: *"While chlorophacinone exposure decreased over time, an increasing exposure trend was observed for the SGAR brodifacoum, suggesting that public policies may not be efficient at mitigating risk of exposure for non-target species."*

Spain differs. In 401 non-target animals, granivorous birds showed the highest exposure prevalence, especially to chlorophacinone (PMID:22326314). That is from a fetch summary; refetch before quoting.

**Lifestyle factors.** None. Smoking, diet, alcohol and exercise have no established relation to this poisoning.

**Infectious agents.** Not applicable.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. Chlorophacinone is ingested and absorbed from the gastrointestinal tract. This **leads to** a systemic chlorophacinone burden. Plasma concentrations after massive ingestion reach 27.6 mg/L (PMID:10216974).
2. The systemic burden **results in** hepatic distribution and accumulation. The liver is the site of both the target enzyme and the substrate proteins. Hepatic accumulation is one of the four properties Watt et al. give for the long-acting group.
3. Hepatic chlorophacinone **binds and inhibits** vitamin K epoxide reductase (VKORC1). Verbatim (PMID:16499407): *"Anticoagulant rodenticides inhibit vitamin K(1)-2,3 epoxide reductase and thus the synthesis of vitamin K and subsequently clotting factors II, VII, IX and X."*
4. VKOR inhibition **blocks** regeneration of vitamin K hydroquinone from vitamin K 2,3-epoxide. The vitamin K cycle stalls. Verbatim (PMID:31857739): *"resulting in the inability of the body to recycle vitamin K."*
5. Depletion of reduced vitamin K **deprives** gamma-glutamyl carboxylase of its obligate cofactor. This **causes** failure of gamma-carboxylation of glutamate residues on the Gla domains of the vitamin K-dependent proteins.
6. Uncarboxylated factor precursors **are secreted** as PIVKA proteins. They are antigenically present and functionally inert. They cannot bind calcium, cannot dock to anionic phospholipid membranes, and cannot assemble into the tenase and prothrombinase complexes.
7. Functional depletion **proceeds in order of factor half-life**. Factor VII goes first, at roughly 4 to 6 hours, then factor IX, then factor X, then prothrombin at roughly 60 to 72 hours. This ordering **explains** the delayed onset. It also explains why PT and INR move before aPTT.
   - *Branch, and it is the important one.* Protein C and protein S are also vitamin K-dependent and also short-lived. Their earlier loss **can produce** a transient net procoagulant window, which **leads to** thrombosis rather than bleeding. This is the mechanism usually offered for the fatal cerebral vein thrombosis case (PMID:16716547). **The half-life ordering step here is textbook coagulation physiology, inferred, not demonstrated in that paper.** Mark it inferred.
8. Combined deficiency of factors II, VII, IX and X **results in** failure of thrombin generation, which **results in** prolonged PT, prolonged aPTT and elevated INR.
9. Impaired thrombin generation **results in** failure of hemostatic plug consolidation, which **causes** spontaneous and provoked hemorrhage across mucosal and visceral sites.
10. Hemorrhage into a critical compartment **causes** death. Intracranially this is the commonest fatal route (PMID:26239439). Cumulative blood loss **causes** anemia and hypovolemic shock (PMID:16499407).
11. Slow hepatic clearance and enterohepatic recirculation of chlorophacinone **cause** persistence of step 3, which **produces** the rebound coagulopathy on withdrawal of vitamin K (PMID:3222685).

### A second, contested mechanism: mitochondrial uncoupling

Indandione anticoagulants are described in toxicology reference texts as **uncouplers of oxidative phosphorylation**, a property the 4-hydroxycoumarins lack. The claim is that this produces neurologic and cardiopulmonary injury in laboratory rats that can kill before hemorrhage does, and that it explains the direct capillary permeability damage sometimes attributed to indandiones.

I could not source this to primary literature. A PubMed query combining `chlorophacinone` with `uncoupling OR mitochondria OR oxidative phosphorylation` returned **zero records**. The same query for `indandione OR diphacinone OR pindone` with uncoupling returned **zero records**. The statement circulates in secondary sources and regulatory documents without a retrievable primary citation in the indexed literature.

Curate it as an open question or leave it out. Do not attach it to a PMID that does not say it. If it belongs anywhere, it belongs in a `discussions` entry with `kind: KNOWLEDGE_GAP`, stating that a mechanism widely repeated in reference texts has no locatable primary source. That is an honest, useful entry, and it is more valuable than a fabricated binding.

### Ontology term suggestions for the pathograph

| Node | Term type | Suggested binding | Verified |
|---|---|---|---|
| Vitamin K epoxide reductase inhibition | molecular function | **GO:0047057** `vitamin-K-epoxide reductase (warfarin-sensitive) activity`, `modifier: DECREASED` | Yes, OLS4 |
| Vitamin K cycle arrest | biological process | **GO:0042373** `vitamin K metabolic process`, `modifier: DECREASED` | Yes, in-repo use |
| Failure of Gla-domain carboxylation | biological process | **GO:0017187** `peptidyl-glutamic acid carboxylation`, `modifier: DECREASED` | Yes, in-repo use |
| Impaired thrombin generation / coagulopathy | biological process | **GO:0007596** `blood coagulation`, `modifier: DECREASED` | Yes, in-repo use |
| Cell type for all hepatic nodes | cell type | **CL:0000182** `hepatocyte` | Yes, in-repo use |
| Anatomical site of synthesis | anatomy | **UBERON:0002107** `liver` | Yes, OLS4 |
| Chemical agent | chemical | **CHEBI:81796** `chlorophacinone` | Yes, OLS4 |
| Vitamin K | chemical | **CHEBI:28384** `vitamin K`; **CHEBI:18067** `phylloquinone` for K1 | Yes; phylloquinone in-repo use |

`biological_scale` assignments, if used: VKOR inhibition is `MOLECULAR`. Failure of carboxylation is `MOLECULAR`. Hepatocyte secretion of inert PIVKA proteins is `CELLULAR`. Coagulopathy is `ORGANISM`. Site-specific hemorrhage is `TISSUE`.

### Molecular profiling

None exists. No transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial or CRISPR-screen dataset for chlorophacinone exposure was found. GEO holds nothing under this term to my knowledge; I did not run a GEO query. The one dataset resource located is an open dataset of anticoagulant rodenticide liver residues from Gran Canaria snakes and raptors (PMID:38260864, *Data in Brief*, 2024), which is residue chemistry rather than omics. Record the absence explicitly. A `datasets:` block here should be small and honest, and per repository policy would carry `publication:` and provenance `notes` rather than manufactured evidence snippets.

---

## 7. Anatomical Structures Affected

**Primary organ.** The liver, **UBERON:0002107**. It is the site of the lesion, not a site of injury. VKORC1 and GGCX both act in the hepatocyte endoplasmic reticulum. Note the distinction: the liver is where the mechanism happens; the liver is generally not damaged.

Exception. Hepatocellular necrosis was found in the poisoned lambs. Verbatim (PMID:17037620): *"Histologically hepatocellular centrolobular necrosis was observed."* Centrilobular necrosis in an exsanguinating animal is most parsimoniously hypoxic, secondary to shock, not a direct hepatotoxic effect. Do not curate chlorophacinone as a hepatotoxin on that sentence. And it is a `MODEL_ORGANISM` observation in any case.

**Secondary organs, meaning bleeding sites.** Effectively unrestricted. Watt et al., verbatim: *"haemorrhage into any internal organ."*

Sites documented in humans: nasal mucosa, gingiva, skin and subcutis, urinary tract, gastrointestinal tract, rectum, uterus, peritoneum (spontaneous haemoperitoneum is described), and brain, both subarachnoid and cerebral parenchymal.

Sites documented at necropsy in cattle (PMID:35000500, verbatim): *"moderate-to-severe hemorrhage within various tissues and body cavities, including the thymus, subcutaneous region of the neck, mediastinum, lungs, pericardial sac, heart, spleen, perirenal fat, urinary bladder, and skeletal muscle, including the diaphragm."* That is a list-shaped snippet covering eleven anatomical sites. If you use it, use it once, and only for a node that actually claims widespread multi-cavity hemorrhage.

**Body systems.** Hematologic (primary), cardiovascular, nervous, digestive, renal and urinary, respiratory, integumentary.

**Cell types.** `hepatocyte` **CL:0000182** carries the mechanism. No cell is destroyed by the toxin. Platelets are unaffected; platelet count is characteristically normal, and that is a diagnostic discriminator.

**Subcellular.** The endoplasmic reticulum membrane. VKORC1 is an ER integral membrane protein and GGCX is ER-resident. GO cellular component `endoplasmic reticulum membrane` (GO:0005789, not verified this session).

**Lateralization.** Not applicable.

---

## 8. Temporal Development

**Onset.** Acute exposure. Clinically subacute presentation. No age predilection beyond exposure opportunity.

**Latent period.** Median 4 days, range 1 to 30 (PMID:40974629). The 33-year-old with a 1875 mg ingestion had *"a normal prothrombin index (PI)"* at 8 hours post-ingestion (PMID:10216974, verbatim). That single fact is the most clinically important thing in the entry: a normal coagulation panel early after ingestion excludes nothing.

**Stages.** A usable four-phase model, mapping to the `progression:` slot with `phase` as the key:

| Phase | Window | State |
|---|---|---|
| Latent | 0 to 24 hours | Normal coagulation. Nausea and non-specific symptoms possible. |
| Coagulopathy onset | 24 to 72 hours | PT and INR rise. Factor VII falls first. Bleeding may begin. |
| Established hemorrhage | 3 to 14 days | Peak INR. Multi-site bleeding. Highest risk of intracranial hemorrhage. |
| Resolution with rebound | weeks to months | INR corrects under vitamin K and relapses on withdrawal. Full normalization at 7 weeks in the Vogel case (PMID:3222685). |

**Course.** Fluctuating and relapsing under treatment. Not progressive. Not chronic once cleared.

**Duration relative to the superwarfarins.** Shorter, and this matters therapeutically. Chlorophacinone's apparent elimination half-life under phenobarbital was 3.27 days (PMID:10216974). Brodifacoum poisoning runs for months, with class treatment courses averaging 168 days (PMID:26239439). Chlorophacinone is long-acting relative to warfarin and short-acting relative to brodifacoum.

**Dose-dependent kinetics.** Verbatim (PMID:2769823): *"The determination of half-lives was investigated and the results indicate that the greater the quantity absorbed, the longer the half-life."* That is saturable, non-linear elimination, and it means half-life from a small exposure does not predict a large one.

**A half-life conflict to resolve.** One secondary source states a blood elimination half-life of 10 hours for chlorophacinone. The published human case data are incompatible with that as a governing figure, since the pharmacodynamic effect persists for weeks and the measured apparent half-life under enzyme induction was 3.27 days. The 10-hour figure may refer to a distribution phase or a different species. Do not curate it without a primary source.

**Critical intervention windows.** Two.
- Within 1 to 2 hours of a large ingestion, activated charcoal is useful.
- At 36 to 48 hours post-exposure, the INR check that decides everything. Verbatim (PMID:16499407): *"In all other cases, the INR should be measured 36-48 hours post exposure. If the INR is normal at this time, even in the case of long-acting formulations, no further action is required."*

---

## 9. Inheritance and Population

**Inheritance.** None. Acquired toxic exposure. No inheritance pattern, no penetrance, no expressivity, no anticipation, no mosaicism, no founder effect, no consanguinity relevance, no carrier frequency. Say so in the entry rather than leaving the section empty.

### Epidemiology

There is no chlorophacinone-specific incidence or prevalence figure in the literature. What exists is class-level poison-center data.

| Measure | Value | Population | Source |
|---|---|---|---|
| Annual exposures, all long-acting anticoagulant rodenticides | 10,413 mean per year | United States | PMID:26239439 |
| Annual patients treated | 2,750 mean per year | United States | PMID:26239439 |
| Cumulative exposures over 25 years | 315,951 | United States | PMID:26239439 |
| Proportion in children | nearly 90 percent | United States | PMID:26239439 |
| Morbidity or mortality | 2 percent of exposures | United States | PMID:26239439 |
| Confirmed anticoagulant rodenticide poisonings, 2011 to 2013 | 117 | East China | PMID:30483606 |
| Mortality in that series | 1 of 117 | East China | PMID:30483606 |
| Fatality in the pooled forensic series | 6 of 88 | Global case reports since 2000 | PMID:40974629 |

Verbatim (PMID:26239439): *"In the United States, on average, there were 10413 exposures reported with 2750 patients treated annually."*

**Chlorophacinone's share of that burden is small and declining, and the direction differs by country.** In the east China series, chlorophacinone was not detected at all among 117 confirmed cases; bromadiolone accounted for 70.9 percent and brodifacoum 19.7 percent (PMID:30483606, via fetch summary). In the pooled 88-case forensic review, verbatim: *"a total of 38 cases reported 7 distinct types, with brodifacoum and bromadiolone being the most common."* Chlorophacinone is not named in that abstract.

In France, chlorophacinone matters more, because it is one of only two compounds registered for field use. Verbatim (PMID:21171851): *"In wildlife, bromadiolone and chlorophacinone are by far the most important products, being the only ones registered for field use."* And on human outcome there, verbatim: *"There is no report of mortality in the human data, and less than 1% of all exposure cases in domestic animals were fatal."*

**Geography.** Human chlorophacinone case reports cluster in France and Switzerland, which tracks the compound's registration history and market share. Livestock incidents are reported from the United States. Rodenticide poisoning in general is a much larger clinical problem in China and South Asia, but with different compounds.

**Sex ratio.** Not established for chlorophacinone. The 88-case series enumerated both sexes without reporting a ratio in the abstract. Note that male rats are reported more sensitive than females to chlorophacinone in EPA toxicology review, which is a target-species finding, not a human one.

**Age distribution.** Bimodal in the class. A large young-child peak that is clinically benign, and an adult peak of deliberate ingestion that carries the mortality.

---

## 10. Diagnostics

### Laboratory tests

**Coagulation panel first.** PT with INR is the primary and most sensitive early test, because factor VII has the shortest half-life. aPTT prolongs later. Platelet count, fibrinogen and thrombin time are characteristically normal, and their normality is the discriminator against disseminated intravascular coagulation.

LOINC terms (not verified this session, listed as leads): prothrombin time 5902-2, INR 6301-6, aPTT 3173-2, platelet count 777-3, fibrinogen 3255-7.

**Factor assays.** Reduced factors II, VII, IX and X with normal factors V and VIII. This pattern is the classic discriminator, because liver failure depresses factor V while vitamin K antagonism does not. Vogel et al. tracked factors VII and X specifically (PMID:3222685).

**PIVKA-II.** Elevated des-gamma-carboxyprothrombin is the mechanistically specific marker of vitamin K antagonism. HPO **HP:0045063** exists for it. It is established in veterinary diagnosis of anticoagulant poisoning and under-used in human toxicology. Note the pitfall: PIVKA-II is also a hepatocellular carcinoma tumor marker, and the assay is far more often ordered for that purpose. Context resolves it.

**Toxicological confirmation.** This is what makes the diagnosis specific rather than generic. Available methods, in publication order:

| Method | Matrix | Performance | Source |
|---|---|---|---|
| HPLC with UV | plasma | The original chlorophacinone method | PMID:2769823, PMID:10216974 |
| Ion chromatography with ion-trap ESI-MS | plasma | chlorophacinone-specific | PMID:19016234 |
| LC-MS/MS, validated | blood | simultaneous rodenticide panel | PMID:25595137 |
| UPLC-MS/MS with dispersive liquid-liquid microextraction | urine | LODs 0.003 to 0.03 ng/mL for nine rodenticides | PMID:29960250 |
| HPLC-MS/MS | animal serum | seven anticoagulants plus dicoumarol | PMID:36869712 |
| UPLC-MS, interlaboratory validated | animal liver | PMID:37313802 |
| LC-MS/MS, 18-analyte forensic panel | whole blood, bile, vitreous humor | FDA-validated, 8-minute run | PMID:39893780 |

The 2025 forensic panel is the current state of the art and covers chlorophacinone explicitly. Verbatim (PMID:39893780): *"a liquid chromatography-tandem mass spectrometry method capable of quantifying eighteen anticoagulant or antiplatelet compounds (apixaban, rivaroxaban, dabigatran, warfarin, acenocoumarol, fluindione, brodifacoum, bromadiolone, difenacoum, difethialone, chlorophacinone, coumatetralyl, flocoumafen, acetylsalicylic acid, clopidogrel, dipyridamole, ticagrelor, and ticlopidine) in a single run."*

**Serial concentration monitoring guides discharge, not treatment.** Verbatim (PMID:10216974): *"If PI is useful for planning phytomenadione treatment and used for therapeutic monitoring of AVK, the chlorophacinone concentrations follow-up may provide a better estimation of the duration of hospitalisation."*

And a caution that the concentration and the effect decouple. Verbatim (PMID:10216974): *"Chlorophacinone accumulation in target cells or existence of an unidentified metabolite may explain persistence of the hypocoagulability syndrome at low plasmatic concentrations of chlorophacinone."* A low plasma level does not mean the patient is safe to stop vitamin K.

### Imaging and other modalities

CT head without contrast for suspected intracranial hemorrhage. CT or ultrasound of the abdomen for haemoperitoneum. These are complication-directed, not diagnostic of the poisoning. No specific imaging finding exists.

Biopsy and pathology have no diagnostic role in the living patient. At autopsy the finding is multi-organ hemorrhage. Verbatim (PMID:40974629): *"Six fatalities occurred and autopsy findings in three cases primarily indicated multi-organ hemorrhage and necrosis."*

Electrophysiology has no role.

### Genetic testing

No role in human diagnosis. `VKORC1` sequencing is used in rodent population surveillance for resistance management, which is not diagnosis of a human patient.

### Omics diagnostics

None. No RNA-seq, proteomic, metabolomic, epigenomic or liquid-biopsy assay is used or proposed.

### Clinical criteria

No formal diagnostic criteria exist. No DSM, no society guideline defining the entity. The one relevant consensus document is the American Association of Poison Control Centers out-of-hospital management guideline for long-acting anticoagulant rodenticides (PMID:17357377, *Clin Toxicol* 2007). It is a triage guideline, not a diagnostic criterion set, and it is now nineteen years old.

The operative diagnostic posture is the one Chong and Lo state, verbatim (PMID:31857739): *"Superwarfarin poisoning should therefore be suspected in all patients with unexplained prolongation of prothrombin time, and can be confirmed by their detection in serum."*

### Differential diagnosis

| Condition | Distinguishing feature |
|---|---|
| Warfarin or other coumarin therapy or overdose | Toxicology assay separates them. Warfarin coagulopathy corrects in days, not weeks |
| Brodifacoum, bromadiolone, difenacoum poisoning | Same syndrome. Only assay separates. Duration is much longer |
| Dietary vitamin K deficiency, malabsorption, prolonged antibiotics | Corrects promptly and durably with normal-dose vitamin K, no rebound |
| Liver failure | Factor V is reduced. In vitamin K antagonism factor V is normal |
| Disseminated intravascular coagulation | Thrombocytopenia, low fibrinogen, elevated D-dimer, schistocytes |
| Vitamin K-dependent coagulation factor deficiency, VKCFD1/VKCFD2 | Lifelong history from infancy, family history, biallelic `GGCX` or `VKORC1` variants. Already curated in this repository |
| Acquired factor inhibitor | Mixing study fails to correct |
| Factitious disorder or covert administration | The reason toxicological confirmation matters. Two homicides in 88 cases (PMID:40974629) |

The mixing study deserves a line of its own. In chlorophacinone poisoning the prolonged PT corrects on mixing with normal plasma, because the defect is factor deficiency and not an inhibitor. That is a cheap, fast, widely available discriminator.

### Screening

No population screening exists and none is indicated. Occupational biomonitoring of pest-control workers is conceivable and not established practice.

---

## 11. Outcome / Prognosis

**Mortality.** Low overall, meaningful in severe deliberate ingestion.

| Measure | Value | Source |
|---|---|---|
| Morbidity or mortality across all US exposures | 2 percent | PMID:26239439 |
| Deaths in pooled global case reports | 6 of 88 | PMID:40974629 |
| Deaths in east China confirmed series | 1 of 117 | PMID:30483606 |
| Human deaths in French PCC data, 2004 to 2007 | none reported | PMID:21171851 |

The 6 in 88 figure is not a case fatality rate. It is the fatality proportion in a corpus of published case reports, which are selected for being unusual or severe. Curate it with `measure_type: CASES_IN_LITERATURE` reasoning and say so plainly.

**Leading cause of death.** Intracranial hemorrhage (PMID:26239439). Paradoxical thrombosis is a second, rare fatal route (PMID:16716547).

**Recovery.** Complete, if the patient survives the bleeding and completes vitamin K therapy. There is no chronic sequela of the toxin itself. Residual disability, when it occurs, is neurological and follows intracranial hemorrhage rather than the poisoning.

**Prognostic factors.** Amount ingested, and it is not linear, since half-life lengthens with dose (PMID:2769823). Latency to presentation. Peak INR. Whether bleeding is intracranial. Adherence to prolonged vitamin K, given the rebound pattern (PMID:3222685). Suicidal intent, which predicts both a large dose and delayed presentation.

**Quality of life instruments.** None applied. No data.

---

## 12. Treatment

### Decontamination

Activated charcoal within 1 to 2 hours of ingestion. Watt et al. index `Charcoal/therapeutic use` as a MeSH term (PMID:16499407). Cholestyramine has been used to interrupt enterohepatic recirculation for the superwarfarins; the evidence is weak and it is not standard.

- `treatment_term`: **NCIT:C15986** `Pharmacotherapy`, verified in repository use
- `therapeutic_agent`: activated charcoal, `CHEBI:37527` (not verified this session)
- `therapeutic_modality`: `SMALL_MOLECULE`

### Vitamin K1 (phytomenadione, phylloquinone). The antidote.

This is the mainstay and the one treatment with unambiguous mechanism-directed evidence. It bypasses the blocked reductase step by supplying vitamin K in quantity sufficient to drive carboxylation despite the inhibitor.

Verbatim (PMID:40974629): *"Vitamin K1 administration (intravenous or oral) was the primary treatment."*

Dosing, from the class review (PMID:26239439, verbatim): *"Treatment of acute hemorrhagic symptoms often required intravenous vitamin K1 in excess of 50 to 100 mg; chronic maintenance with 100 mg PO vitamin K1 daily was the most frequently used dose required to suppress coagulopathy. Treatment courses averaged 168 days."*

Note again that 168 days is a class figure dominated by brodifacoum. Chlorophacinone requires weeks, not months. The Vogel case normalized at 7 weeks (PMID:3222685).

The INR threshold for non-bleeding patients, verbatim (PMID:16499407): *"If there is no active bleeding and the INR is < or =4.0, no treatment is required; if the INR is > or =4.0 phytomenadione 10mg should be administered intravenously."*

- `treatment_term`: **NCIT:C15986** `Pharmacotherapy`
- `therapeutic_agent`: **CHEBI:18067** `phylloquinone` (verified in repository use)
- `therapeutic_modality`: `SMALL_MOLECULE`
- `target_mechanisms`: target the VKOR inhibition node with `treatment_effect: BYPASSES`

### Factor replacement for active bleeding

Verbatim (PMID:16499407): *"If active bleeding occurs, prothrombin complex concentrate (which contains factors II, VII, IX and X) 50 units/kg, or recombinant activated factor VII 1.2-4.8 mg or fresh frozen plasma 15 mL/kg (if no concentrate is available) and phytomenadione 10mg intravenously (100 microg/kg bodyweight for a child) should be given."*

Current practice favors four-factor PCC over fresh frozen plasma. Verbatim (PMID:31857739): *"Treatment for superwarfarin poisoning includes rapid correction of factor deficiencies with either 4-factor prothrombin complex concentrate or fresh frozen plasma in patients with active bleeding."*

- Four-factor PCC: **NCIT:C208347** `Four-factor Prothrombin Complex Concentrate` (verified via OLS4). Note that this is a product term, not a `NCIT:C25218` clinical action, so it goes in `therapeutic_agent` under a `Pharmacotherapy` action, not in the `treatment_term` slot.
- Fresh frozen plasma transfusion: the sibling entry `Vitamin_K_Dependent_Coagulation_Factor_Deficiency` already binds an FFP treatment term. Copy that binding rather than re-deriving it.
- `therapeutic_modality`: `PROTEIN_REPLACEMENT`

Watch the thrombotic hazard. Verbatim (PMID:26239439): *"thrombotic complications accompanying hemostatic therapy have also been observed."*

### Enzyme induction with phenobarbital

Chlorophacinone-specific, and one of the few interventions with chlorophacinone rather than class evidence. Verbatim (PMID:10216974): *"Under phenobarbital 200 mg/day, chlorophacinone exhibited an apparent elimination half-life (3.27 days) shorter than in previously reported cases."*

Confirmed independently. Verbatim (PMID:2769823): *"The effect of phenobarbital on the elimination of cholorophacinone could be studied in one case. An increased elimination was noted when phenobarbital was administered."*

It is a case-level observation in a total of two patients across two papers, and phenobarbital sedation in a bleeding patient is not free. Curate it as reported and not established.

### Antifibrinolytics

Both the Lagrange case and the Watt review index `Antifibrinolytic Agents/therapeutic use` in MeSH. Tranexamic acid is the agent, **CHEBI:48669** (verified in repository use). Adjunctive for mucosal bleeding.

### Supportive care

Red cell transfusion for symptomatic anemia. **NCIT:C15747** `Supportive Care`. Neurosurgical intervention for intracranial hemorrhage. Psychiatric evaluation and admission after deliberate ingestion, which is not optional in this population.

### What is not treatment

Hemodialysis does not remove chlorophacinone; it is highly protein bound and lipid soluble. No gene therapy, cell therapy, RNA therapy or immunotherapy exists or is proposed. No clinical trial is registered for chlorophacinone poisoning. I searched neither ClinicalTrials.gov nor WHO ICTRP directly this session, and I state that as a limitation rather than as a negative finding.

### Pharmacogenomics

No CPIC guideline. No PharmGKB annotation for chlorophacinone. The `VKORC1` and `CYP2C9` annotations that exist are for warfarin and acenocoumarol and must not be transferred.

---

## 13. Prevention

**Primary prevention.** Product stewardship and access control. Tamper-resistant bait stations. Bittering agents in bait. Storage away from children and livestock. The two US livestock epizootics both trace to bait accessible through a structural gap: old bait between wall studs reachable through a hole in the plywood (PMID:17037620), and *"Multiple piles and an open pail of white powdery material"* in a calf facility (PMID:35000500, verbatim). Both were preventable by housekeeping.

**Regulatory prevention.** Active and moving. The EPA's 2022 Proposed Interim Decision covers chlorophacinone with the other six anticoagulant rodenticides, and a Final Biological Evaluation was released 2024-11-21. Measures under consideration include product cancellations, added requirements, and reclassification to Restricted Use Pesticide. California's Department of Pesticide Regulation issued Enforcement Letter 24-20 in December 2024 addressing chlorophacinone and warfarin restricted-material status, and held an informal public workshop on anticoagulant rodenticide mitigation with draft regulations in September 2025. Chlorophacinone is also under EU biocide review; ECHA maintains an assessment document. These are regulatory documents rather than PMIDs, and they date fast. Cite them with retrieval dates and do not put them in evidence snippets.

**Environmental prevention.** Reduced-dose combination baiting is an active research direction. Verbatim (PMID:38638948): *"Combinations of second generation anticoagulants were more effective than the combination of chlorophacinone and second generation anticoagulants. The results indicate that combinations of different anticoagulants at multifold lower doses than the standard may provide a successful tool for brown rat control."* Note what that says: chlorophacinone combinations performed **worse** than SGAR combinations. It is not an endorsement.

Stereochemical reformulation is another. The bromadiolone cis-isomer proposal (PMID:33130091) does not apply to chlorophacinone directly but frames the approach.

**Secondary prevention.** The 36 to 48 hour INR check after known exposure (PMID:16499407). And the finding that spares most children an unnecessary blood draw, verbatim (PMID:16499407): *"There are now sufficient data in young children exposed to anticoagulant rodenticides to conclude that routine measurement of the international normalised ratio (INR) is unnecessary."* That is a strong, specific, actionable recommendation and belongs in the entry.

**Tertiary prevention.** Completing the full vitamin K course. Serial INR monitoring after discontinuation to catch rebound. The Vogel case is the argument, verbatim: *"This case emphasizes the need for prolonged clinical and laboratory follow-up for rodenticide intoxications and for vitamin K administration for several weeks."*

**Food-chain prevention.** A one-week milk withdrawal period after livestock exposure (PMID:32645465).

**Immunization, genetic screening, genetic counseling.** Not applicable. Say so.

---

## 14. Other Species / Natural Disease

Chlorophacinone toxicosis in animals is far better documented than in humans, and much of the mechanistic and pathological evidence available comes from there. Grade all of it `MODEL_ORGANISM` even when it is a spontaneous veterinary case, per repository convention.

### Species with documented natural chlorophacinone poisoning

| Species | NCBITaxon | Context | Source |
|---|---|---|---|
| Domestic cattle, *Bos taurus* | NCBITaxon:9913 | 14 calves, fatal | PMID:35000500 |
| Sheep, *Ovis aries* | NCBITaxon:9940 | 11 lambs fatal; 18 lactating ewes sublethal | PMID:17037620, PMID:32645465 |
| Domestic dog, *Canis lupus familiaris* | NCBITaxon:9615 | Over 60 percent of French domestic animal cases | PMID:21171851, PMID:9534772 |
| Red-tailed hawk, *Buteo jamaicensis* | NCBITaxon:52604 (unverified) | Experimental sublethal secondary exposure | PMID:35633457 |
| American badger, *Taxidea taxus* | NCBITaxon:50636 (unverified) | Endangered; residues detected | PMID:40252754 |
| Black-tailed prairie dog, *Cynomys ludovicianus* | NCBITaxon:45480 (unverified) | Target species; residue kinetics | PMID:25997570 |
| Norway rat, *Rattus norvegicus* | NCBITaxon:10116 | Target species | PMID:24781908, PMID:41278179 |
| House mouse, *Mus musculus* | NCBITaxon:10090 | Target species; resistance | PMID:24781908, PMID:36181415 |
| Black rat, *Rattus rattus* | NCBITaxon:10117 | Target; resistance | PMID:35970209 |
| Hares and rabbits | | Nearly 50 percent of French wildlife submissions | PMID:21171851 |

Verbatim on the French wildlife pattern (PMID:21171851): *"in wildlife hares and rabbits account for almost 50% of the submitted cases, followed by predators and scavengers."*

### The calf and lamb epizootics as comparative pathology

These are the best-documented pathological descriptions of chlorophacinone poisoning in any mammal. Verbatim (PMID:35000500): *"Significant concentrations of chlorophacinone were detected at 4.2, 3.6, and 2.9 ppm in liver."* And the summary sentence: *"Acute hemorrhage and death occurred in fourteen 1.5-mo-old, crossbred calves following ingestion of the vitamin K antagonist chlorophacinone."*

The lamb epizootic gives the tempo. Verbatim (PMID:17037620): *"Eleven lambs, approximately 1-2 months of age, suddenly developed epistaxis, respiratory distress, and facial and cervical swelling. Affected animals died within 1-2 hours from the onset of clinical signs."* Liver residues were 0.58 and 0.50 ppm.

Note the discrepancy worth curating: lambs died at liver concentrations roughly six-fold lower than the calves. Species, age and dose timing all differ. Do not derive a lethal threshold from two case reports.

### A distinctive non-hemorrhagic sign in birds

Verbatim (PMID:35633457): *"Four of the six CPN-exposed RTHAs exhibited ptiloerection, an indication of thermoregulatory dysfunction due to CPN toxicity."* And the linkage, verbatim: *"PT values were associated with ptiloerection duration and frequency; therefore, sublethal CPN exposure can directly or indirectly evoke adverse effects in wild birds."*

This is the only reported observation I found that might connect to the alleged non-anticoagulant mechanism of §6. Thermoregulatory dysfunction is not obviously a bleeding phenomenon. The authors do not attribute it to uncoupling. Do not make that leap for them. It is a good candidate for a `discussions` entry with `kind: KNOWLEDGE_GAP`.

### Veterinary relevance

Anticoagulant rodenticide poisoning is among the most common causes of poisoning in dogs worldwide. Onset in dogs and cats is 3 to 5 days. Presenting signs are lethargy, weakness, dyspnea from pulmonary or pleural hemorrhage, epistaxis, hemoptysis, melena, pale mucous membranes and swollen joints. Vitamin K1 duration differs by agent: 5 to 10 days for short-acting compounds, 21 to 30 days for long-acting ones. Oral vitamin K1 given with a fat-containing meal is 4 to 5 times more effective than vitamin K1 given alone. Coagulation should be rechecked weekly and again 5 to 6 days after stopping therapy. These are veterinary reference statements (MSD Veterinary Manual, Cornell AHDC) rather than PMIDs. Cite them as such or find primary sources.

PIVKA-II has established veterinary diagnostic use for distinguishing anticoagulant poisoning from other canine coagulopathies (doi:10.3390/ani11092612, *Animals* 2021).

### Comparative biology and evolutionary conservation

The vitamin K cycle is deeply conserved across vertebrates. `VKORC1` orthologs exist in every species listed above, and the drug target is the same protein in a rat and in a person. That conservation is precisely why a rodenticide is dangerous to non-target mammals and birds, and why rodent resistance alleles are informative about human pharmacology.

Interspecies sensitivity differs, and avian VKOR biology has been studied specifically: "Avian interspecific differences in VKOR activity and inhibition: Insights from amino acid sequence and mRNA expression ratio of VKORC1 and VKORC1L1" (*Comp Biochem Physiol C*, 2020). I did not retrieve its PMID. It is worth fetching.

Look for OMIA records under anticoagulant rodenticide toxicosis. I did not query OMIA this session.

### Zoonotic potential

None. This is a chemical, not a transmissible agent. Cross-species susceptibility is universal among vertebrates, which is a different thing and should not be recorded under transmission.

---

## 15. Model Organisms

There is no purpose-built disease model here, because the model is simply dosing an animal with the compound. That is worth stating plainly in the entry rather than leaving the section blank.

### Induced models

| System | Species | Use | Source |
|---|---|---|---|
| Acute oral dosing, laboratory rat | *Rattus norvegicus* | Efficacy and LD50 determination | Regulatory toxicology; PMID:41278179 for a 2025 Malaysian urban-rat laboratory study |
| Y139C resistant house mouse, dose-response | *Mus musculus* | Blood-clotting response and resistance factors | PMID:36181415 |
| Secondary-exposure raptor model | *Buteo jamaicensis* | Free-flying hawks fed chlorophacinone-exposed prairie dogs, then radio-tracked 33 days | PMID:35633457 |
| Prairie dog residue kinetics | *Cynomys ludovicianus* | Secondary-hazard modeling | PMID:25997570 |
| Lactating ewe accidental exposure | *Ovis aries* | Mammary transfer pharmacokinetics | PMID:32645465 |
| Fish hepatic microsomes | various | In vitro biotransformation of ARs | PMID:35085616 |

The hawk study is unusually well-designed for a toxicology field experiment and is the single best model-organism source for linking a coagulation readout to an observable clinical sign.

### Genetic models

The relevant genetic models are naturally occurring resistance genotypes in wild rodent populations, not engineered lines. `Vkorc1` Y139C, L128S, S149I, E155K, E155Q, and the *M. spretus*-derived quadruple haplotype. No `Vkorc1` knockout mouse is used for this purpose, and a full knockout would be lethal.

### Phenotype recapitulation

High. Rodents, cattle, sheep, dogs and raptors all reproduce the human sequence: delayed onset, prolonged PT, multi-site hemorrhage, response to vitamin K1. The mechanism is the same protein in every case.

For a `ModelMechanismLink` on the calf and lamb reports, `relationship: RECAPITULATES` and `fidelity: MODERATE` is defensible, with `limitations` noting that ruminant vitamin K status differs from human because of rumen microbial synthesis, that route and dose were uncontrolled, and that these are diagnostic submissions rather than designed experiments.

For the hawk study, `relationship: PARTIALLY_RECAPITULATES` against a coagulopathy node, with a `readout` for prothrombin time, `direction: INCREASED`. Ptiloerection has no human counterpart and should be recorded as a limitation, not folded into a human phenotype.

### Limitations of every model

None reproduces deliberate massive human ingestion. None addresses human dose-dependent half-life. Rodent models are confounded by the fact that the animal is the intended target, so its physiology has been selected against the compound.

### Resources

MGI, RGD, IMPC for `Vkorc1`. Alliance of Genome Resources for orthology. No model repository holds a chlorophacinone-specific line.

---

## Gaps, Conflicts, and Curation Cautions

State these in the entry rather than papering over them.

1. **No MONDO term exists.** MONDO:0029000 `poisoning` is the only anchor, and it is a `broadMatch`. A term request is the right action.
2. **The mitochondrial uncoupling mechanism has no locatable primary source.** Zero PubMed records combine chlorophacinone or the indandiones with uncoupling. The claim is in textbooks and regulatory prose. Curate as a knowledge gap or omit.
3. **Half-life is reported inconsistently.** 10 hours in one secondary source, 3.27 days measured under phenobarbital induction (PMID:10216974), and dose-dependent lengthening (PMID:2769823). Weeks of pharmacodynamic effect. Do not curate a single number.
4. **Molecular weight is reported as both 364.8 and 374.8.** Resolve against PubChem before writing it.
5. **Class citations dominate.** Watt 2005 and King 2015 are about the anticoagulant rodenticide class, in which brodifacoum and bromadiolone supply most of the case material. Every quote from them supports a class claim, not a chlorophacinone claim. Grading them as direct evidence for chlorophacinone-specific nodes would be Named Entity Confusion reached through a review article.
6. **No human VKORC1 pharmacogenomic evidence exists for chlorophacinone.** The warfarin literature is not transferable.
7. **The 88-case forensic series does not name chlorophacinone in its abstract.** It reports 7 rodenticide types across 38 cases with brodifacoum and bromadiolone commonest. Its coagulation and latency statistics are class statistics.
8. **The paradoxical thrombosis abstract is four sentences long** and does not state the protein C mechanism. Anything beyond the fact of the phenomenon needs a different source or an inferred marker.
9. **Several abstracts in this report reached me through a summarizing fetch rather than verbatim**: PMID:33130091, PMID:25997570, PMID:22326314, PMID:29960250, PMID:21033437, PMID:30483606. The quotation marks in those summaries are the summarizer's, not mine. Refetch before any of them becomes an evidence `snippet`.
10. **PMIDs cited but not yet cached in this worktree**: 31857739, 39893780, 38638948, 17037620, 32645465, 35633457, 34748846, 40252754, 30483606, 36181415, 17357377, 25595137, 29960250, 19016234, 36869712, 37313802, 38260864, 41278179. Run `just fetch-reference PMID:<id>` for each one you intend to cite, and commit the cache files, so CI does not refetch them as abstract-only and break a full-text snippet.
11. **Ontology IDs marked "not verified this session"** in the tables above were written from memory and must be resolved through OAK or OLS before binding. That set includes HP:0000132, HP:0001903, HP:0001259, GO:0005789, CHEBI:37527, hgnc:2623, and every NCBITaxon ID flagged unverified.

---

## Reference List

Cached in this worktree already:

| PMID | Citation |
|---|---|
| 40974629 | Yu Z, et al. A retrospective analysis of 88 anticoagulant rodenticide poisoning cases: Characteristics and forensic implications. *Forensic Sci Int.* 2025. doi:10.1016/j.forsciint.2025.112660 |
| 26239439 | King N, Tran MH. Long-Acting Anticoagulant Rodenticide (Superwarfarin) Poisoning: A Review of Its Historical Development, Epidemiology, and Clinical Management. *Transfus Med Rev.* 2015. doi:10.1016/j.tmrv.2015.06.002 |
| 16499407 | Watt BE, Proudfoot AT, Bradberry SM, Vale JA. Anticoagulant rodenticides. *Toxicol Rev.* 2005. doi:10.2165/00139709-200524040-00005 |
| 16716547 | Papin F, et al. Lethal paradoxical cerebral vein thrombosis due to suspicious anticoagulant rodenticide intoxication with chlorophacinone. *Forensic Sci Int.* 2007. doi:10.1016/j.forsciint.2006.04.003 |
| 10216974 | Lagrange F, et al. Toxicological management of chlorophacinone poisoning. *Acta Clin Belg.* 1999 |
| 2769823 | Burucoa C, et al. Chlorophacinone intoxication. A biological and toxicological study. *J Toxicol Clin Toxicol.* 1989. doi:10.3109/15563658909038571 |
| 3222685 | Vogel JJ, et al. [Prolonged anticoagulation following chlorophacinone poisoning]. *Schweiz Med Wochenschr.* 1988 |
| 21171851 | Berny P, et al. Prevalence of anticoagulant rodenticide poisoning in humans and animals in France and substances involved. *Clin Toxicol.* 2010. doi:10.3109/15563650.2010.533678 |
| 24781908 | Esther A, et al. [Rodenticide resistance and consequences]. *Bundesgesundheitsblatt.* 2014. doi:10.1007/s00103-013-1930-z |
| 35970209 | Bermejo-Nogales A, et al. VKORC1 single nucleotide polymorphisms in rodents in Spain. *Chemosphere.* 2022. doi:10.1016/j.chemosphere.2022.136021 |
| 35000500 | Radke SL, et al. Acute hemorrhage and death in calves following chlorophacinone exposure. *J Vet Diagn Invest.* 2022. doi:10.1177/10406387211069369 |

Cited but not yet cached:

| PMID | Citation |
|---|---|
| 31857739 | Chong YK, Lo AWI. Superwarfarin (Long-Acting Anticoagulant Rodenticides) Poisoning: from Pathophysiology to Laboratory-Guided Clinical Management. *Clin Biochem Rev.* 2019 |
| 17037620 | Chlorophacinone exposure causing an epizootic of acute fatal hemorrhage in lambs. *J Vet Diagn Invest.* 2006 |
| 32645465 | Accidental chlorophacinone exposure of lactating ewes: Clinical follow-up and human health dietary implications. *Food Chem Toxicol.* 2020 |
| 35633457 | Toxicological responses to sublethal anticoagulant rodenticide exposure in free-flying hawks. *Environ Sci Pollut Res Int.* 2022 |
| 34748846 | Exposure of predatory and scavenging birds to anticoagulant rodenticides in France. *Sci Total Environ.* 2022 |
| 40252754 | Anticoagulant rodenticide exposure in endangered American badgers and fishers from British Columbia, Canada, 1998 to 2018. *Environ Pollut.* 2025 |
| 39893780 | Simultaneous quantification of eighteen therapeutic oral anticoagulants, rodenticides, and antiplatelet agents by LC-MS/MS. *J Pharm Biomed Anal.* 2025 |
| 38638948 | A strategy to improve rodent control while reducing rodenticide release into the environment. *Heliyon.* 2024 |
| 30483606 | Anticoagulant rodenticide intoxication in east China: a three-year analysis. *Forensic Sci Res.* 2016. doi:10.1080/20961790.2016.1242042 |
| 36181415 | Anticoagulant rodenticide blood-clotting dose-responses and resistance factors for Y139C house mice. *Pest Manag Sci.* 2022 |
| 17357377 | Caravati EM, et al. Long-acting anticoagulant rodenticide poisoning: an evidence-based consensus guideline for out-of-hospital management. *Clin Toxicol.* 2007 |
| 33130091 | Water vole management: Could anticoagulant rodenticides stereochemistry mitigate the ecotoxicity issues associated to their use? *Environ Toxicol Pharmacol.* 2021 |
| 25997570 | Retention time of chlorophacinone in black-tailed prairie dogs informs secondary hazards from a prairie dog rodenticide bait. *Pest Manag Sci.* 2016 |
| 22326314 | Primary and secondary poisoning by anticoagulant rodenticides of non-target animals in Spain. *Sci Total Environ.* 2012 |
| 41278179 | Exploring the Effectiveness of Chlorophacinone in Managing Urban Rat Infestation: A Laboratory Study on the Norway Rat. *J Arthropod Borne Dis.* 2025 |
| 25595137 | A validated LC-MS-MS method for simultaneous identification and quantitation of rodenticides in blood. *J Anal Toxicol.* 2015 |
| 29960250 | Simultaneous determination of nine anticoagulant rodenticides by UPLC-MS/MS. *J Chromatogr B.* 2018 |
| 19016234 | Characterization and determination of chlorophacinone in plasma by ion chromatography coupled with ion trap ESI-MS. *Biomed Chromatogr.* 2009 |
| 36869712 | Comprehensive Evaluation of an HPLC-MS-MS Method for Quantitation of Seven Anti-Coagulant Rodenticides and Dicoumarol in Animal Serum. *J Anal Toxicol.* 2023 |
| 37313802 | Validation and interlaboratory comparison of anticoagulant rodenticide analysis in animal livers using UPLC-MS. *J Vet Diagn Invest.* 2023 |
| 38260864 | An open dataset of anticoagulant rodenticides in liver samples from California kingsnakes and raptors in Gran Canaria. *Data Brief.* 2024 |
| 35085616 | New insights on in vitro biotransformation of anticoagulant rodenticides in fish. *Chemosphere.* 2022 |
| 9534772 | [Anticoagulant rodenticide poisoning in dogs in The Netherlands]. *Tijdschr Diergeneeskd.* 1997 |
| 39688840 | Gummin DD, et al. 2023 Annual Report of the National Poison Data System: 41st Annual Report. *Clin Toxicol.* 2024 |
| 41432769 | 2024 Annual report of the National Poison Data System: 42nd annual report. *Clin Toxicol.* 2025 |

Non-PubMed sources, with retrieval date 2026-09-03:

- US EPA, Restrictions on Rodenticide Products. https://www.epa.gov/rodenticides/restrictions-rodenticide-products
- US EPA, Rodent Control Pesticide Safety Review, including the 2022 Proposed Interim Decision for the anticoagulant rodenticides and the Final Biological Evaluation of 2024-11-21. https://www.epa.gov/rodenticides/rodent-control-pesticide-safety-review
- California Department of Pesticide Regulation, Enforcement Letter 24-20 (December 2024) and the September 2025 Anticoagulant Rodenticide Mitigation Informal Public Workshop draft regulations.
- ECHA chlorophacinone assessment. https://echa.europa.eu/documents/10162/e623897b-b36e-7527-7ed4-12c9aa311639
- USDA APHIS, The Use of Chlorophacinone in Wildlife Damage Management. https://www.aphis.usda.gov/sites/default/files/26-chlorophacinone.pdf (fetch returned unparseable PDF this session; contents not extracted)
- USDA Forest Service SERA TR-056-10-03b, Chlorophacinone Human Health and Ecological Risk Assessment. https://www.fs.usda.gov/foresthealth/pesticide/pdfs/Chlorophacinone.pdf (not retrieved)
- NPIC Rodenticides Fact Sheet. https://npic.orst.edu/factsheets/rodenticides.html
- StatPearls, Rodenticide Toxicity. https://www.ncbi.nlm.nih.gov/books/NBK554428/
- MSD Veterinary Manual, Anticoagulant Rodenticide Poisoning in Animals.
- Cornell University AHDC Comparative Coagulation, Vitamin K Therapy.
- PubChem CID 19402, chlorophacinone. https://pubchem.ncbi.nlm.nih.gov/compound/Chlorophacinone
- EBI OLS4 for all verified CHEBI, GO, HP, UBERON and MONDO identifiers. https://www.ebi.ac.uk/ols4

Sources:
- [PubMed E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=chlorophacinone)
- [EBI Ontology Lookup Service 4](https://www.ebi.ac.uk/ols4)
- [PubChem CID 19402](https://pubchem.ncbi.nlm.nih.gov/compound/Chlorophacinone)
- [Anticoagulant rodenticide intoxication in east China (PMC6197128)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6197128/)
- [US EPA Restrictions on Rodenticide Products](https://www.epa.gov/rodenticides/restrictions-rodenticide-products)
- [US EPA Rodent Control Pesticide Safety Review](https://www.epa.gov/rodenticides/rodent-control-pesticide-safety-review)
- [ECHA chlorophacinone document](https://echa.europa.eu/documents/10162/e623897b-b36e-7527-7ed4-12c9aa311639)
- [NPIC Rodenticides Fact Sheet](https://npic.orst.edu/factsheets/rodenticides.html)
- [StatPearls Rodenticide Toxicity](https://www.ncbi.nlm.nih.gov/books/NBK554428/)
- [USDA APHIS chlorophacinone](https://www.aphis.usda.gov/sites/default/files/26-chlorophacinone.pdf)
- [MSD Veterinary Manual, anticoagulant rodenticide poisoning](https://www.msdvetmanual.com/toxicology/rodenticide-poisoning/anticoagulant-rodenticide-poisoning-in-animals)
- [Cornell AHDC Vitamin K Therapy](https://www.vet.cornell.edu/animal-health-diagnostic-center/laboratories/comparative-coagulation/clinical-topics/vitamin-k-therapy)
- [AAPCC out-of-hospital guideline](https://www.tandfonline.com/doi/full/10.1080/15563650600795487)
- [Superwarfarin poisoning: pathophysiology to laboratory-guided management](https://pubmed.ncbi.nlm.nih.gov/31857739/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 48 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 47 |
| On topic | 31 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:34748846` (1 mention) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 27 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000132` (2 mentions) - the report calls it "not verified this session"; HP calls it **Menorrhagia**
- `HP:0001903` (2 mentions) - the report calls it "not verified this session"; HP calls it **Anemia**
- `HP:0001259` (2 mentions) - the report calls it "not verified"; HP calls it **Coma**
- `NCBITaxon:52604` (1 mention) - the report calls it "unverified"; NCBITaxon calls it **Pleurocapsales**
- `NCBITaxon:50636` (1 mention) - the report calls it "unverified"; NCBITaxon calls it **Trigoniophthalmus**
- `NCBITaxon:45480` (1 mention) - the report calls it "unverified"; NCBITaxon calls it **Cynomys ludovicianus**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:9913` (1 mention) - the report calls it "Domestic cattle, *Bos taurus"; NCBITaxon calls it **Bos taurus**, and lists "domestic cattle" among its other names
- `NCBITaxon:9940` (1 mention) - the report calls it "Sheep, *Ovis aries"; NCBITaxon calls it **Ovis aries**
- `NCBITaxon:9615` (1 mention) - the report calls it "Domestic dog, *Canis lupus familiaris"; NCBITaxon calls it **Canis lupus familiaris**
- `NCBITaxon:10116` (1 mention) - the report calls it "Norway rat, *Rattus norvegicus"; NCBITaxon calls it **Rattus norvegicus**
- `NCBITaxon:10090` (1 mention) - the report calls it "House mouse, *Mus musculus"; NCBITaxon calls it **Mus musculus**
- `NCBITaxon:10117` (1 mention) - the report calls it "Black rat, *Rattus rattus"; NCBITaxon calls it **Rattus rattus**