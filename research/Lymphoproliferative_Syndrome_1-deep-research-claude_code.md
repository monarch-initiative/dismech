---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-13T23:56:07.016349'
end_time: '2026-10-13T23:57:16.277640'
duration_seconds: 69.26
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Lymphoproliferative Syndrome 1
  mondo_id: MONDO:0013081
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
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 7
  total_cost_usd: 0.7340413999999998
  session_id: aa4f0803-31cb-5b9b-8409-a0195ed1b485
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 7
reference_validation:
  total_references: 2
  verified: 2
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 2
  on_topic: 2
  validator_version: 0.3.0
term_validation:
  total_terms: 17
  verified: 16
  not_found: 1
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.059
  labels_checked: 10
  labels_matching: 7
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0005406
    reported_labels:
    - CD4 lymphopenia
    ontology_label: Recurrent bacterial skin infections
  labels_variant: 2
  unresolved_terms:
  - HP:0002482
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lymphoproliferative Syndrome 1
- **MONDO ID:** MONDO:0013081 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Lymphoproliferative Syndrome 1** covering all of the
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

# Lymphoproliferative Syndrome 1 (LPFS1, ITK deficiency): research report

**Source limits for this report.**
- It rests on three web searches. They returned secondary databases (MedGen, MalaCards, NORD, LOVD, a Disease Ontology mirror) and two review articles.
- Full text of the reviews could not be read. PMC returned a reCAPTCHA page, so no quote below is verified against a paper.
- I have **no verified PMIDs**. Two reviews are cited by PMCID, which is what the searches returned. A PMID written from memory would be a lead, not a citation, so I have left them out.
- Statements marked *[model knowledge]* come from my background knowledge, not from a source I retrieved. Check them before they go into YAML.
- No search was run on OMIA, MGI or IMPC (§14–15), HPO annotations, ClinGen, GeneReviews, trial registries, or treatment-outcome series. Those sections are largely model knowledge.

---

## 1. Disease information

**Identifiers**
- OMIM 613011, MONDO:0013081, Orphanet 538963, MedGen 765548, GARD 0017979, DOID:0060707.
- Source class: structured databases ([MedGen](https://https.ncbi.nlm.nih.gov/medgen/765548), [MONDO concept via SAIL](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0013081/), [LOVD](https://databases.lovd.nl/shared/diseases/03228)).
- The search summary described the OMIM title as "Lymphoproliferative syndrome, EBV-associated, autosomal, 1".
- I did not retrieve the OMIM or Orphanet pages themselves. Treat the cross-references as reported by aggregators.

**Synonyms:** LPFS1, ITK deficiency, ITK lymphoproliferative syndrome (MedGen / MONDO).

**Concept.** LPFS1 is an autosomal recessive primary immunodeficiency caused by biallelic *ITK* mutation. Onset is in early childhood, with EBV-associated immune dysregulation (MedGen).

**Lump/split note.**
- This is the germline syndrome.
- The EBV-driven Hodgkin and non-Hodgkin lymphomas it predisposes to are somatic tumours. Under design-decisions §3a they stay separate from this entry.
- Other EBV-susceptibility inborn errors are separate entities, e.g. XLP1 (*SH2D1A*), XIAP deficiency (XLP2), and CD27/CD70 deficiency.
- I have not checked the MONDO class hierarchy here.

---

## 2. Etiology

- **Cause:** homozygous or compound-heterozygous loss of *ITK* at 5q32 (MONDO / LOVD). The entry is Mendelian and AR.
- **Environmental trigger:** EBV. The aggregator text lists a high EBV viral load. MedGen states the open question: it is unknown whether *ITK* mutations cause lymphoma or hypogammaglobulinemia independently of EBV.
- **Protective factors / gene-environment:** none established in the retrieved sources. EBV exposure is the main interaction. Whether EBV-naive patients develop disease is not settled in what I retrieved.

---

## 3. Phenotypes

Sources: MedGen and [PanelApp Australia](https://panelapp-aus.org/panels/223/gene/ITK/), both aggregators. The 2018 review is [PMC5951928](https://pmc.ncbi.nlm.nih.gov/articles/PMC5951928/), via the search snippet only. No per-phenotype frequencies were retrievable.

| Phenotype | HPO (proposed *[model knowledge]*, not looked up; verify) | Support |
|---|---|---|
| Hodgkin lymphoma | HP:0012189 | MedGen; 2018 review snippet |
| Non-Hodgkin lymphoma | HP:0012539 | review snippet |
| Lymphomatoid granulomatosis | no term proposed | MedGen |
| EBV-driven B-cell lymphoproliferation | no confident term | review snippet |
| Hemophagocytic lymphohistiocytosis | HP:0002482 | MedGen |
| Hypogammaglobulinemia / dysgammaglobulinemia | HP:0003587 or HP:0004313 | MedGen; review |
| CD4 lymphopenia | HP:0005406 | PanelApp |
| Cytopenias | no term proposed | PanelApp |
| Hepatosplenomegaly | HP:0001433 | PanelApp |
| Autoimmune hemolytic anemia | HP:0001890 | MedGen |
| Autoimmune renal disease | no term proposed | MedGen |
| Reduced invariant NKT cells (laboratory) | no HPO term proposed | MedGen |
| High EBV viral load | no HPO term proposed | MedGen |

- **Onset:** early childhood (MedGen).
- **Course:** episodic EBV-triggered disease, with progressive hypogammaglobulinemia in the index sibs (see §11).

---

## 4. Genetic / molecular

- **Gene:** *ITK*, IL2-inducible T-cell kinase, a Tec-family non-receptor tyrosine kinase. HGNC ID not looked up; do not write one from memory.
- **Index variant:** homozygous R335W, found by genome-wide linkage in two sisters from a consanguineous Turkish family (2018 review snippet). R335W is in the kinase domain *[model knowledge]*.
- **Cohort size:** the 2018 review reports *ITK* mutations in 17 patients from Greece, India, Italy, Iran, Morocco, Pakistan, Palestine and elsewhere. An earlier review ([PMC4220104](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4220104/)) describes nine patients. Both counts are from search summaries.
- **Mechanism class:** loss of function. R335W causing protein deficiency is *[model knowledge]*.
- **Other variants, gnomAD frequencies, ClinVar and ClinGen classification:** not retrieved. No ClinGen validity assertion was checked, so `gene_disease_validity` should stay absent until a CGGV record is found.

---

## 5. Environmental information

- **Infectious agent:** Epstein-Barr virus, a human herpesvirus 4 (NCBITaxon ID not looked up). The disease is defined by the EBV-associated phenotype.
- **Toxins and lifestyle:** none reported.

---

## 6. Mechanism / pathophysiology

**Causal chain** (most steps *[model knowledge]*; only steps 1, 5, 6 and 7 are directly supported by the retrieved sources):
1. Biallelic *ITK* loss of function. Supported.
2. Loss of ITK removes TCR-proximal signalling, i.e. the PLCγ1/Ca²⁺/NFAT axis. Inferred from known Tec-kinase biology.
3. T-cell development and function are impaired, with CD4 depletion, as reported in PanelApp. Reduced iNKT cells are reported in MedGen.
4. Cytotoxic and iNKT-mediated control of EBV-infected B cells is impaired. This is inferred, not demonstrated in the retrieved sources.
5. EBV viral load rises (MedGen) and EBV-driven B-cell lymphoproliferation follows (2018 review).
6. Branches:
   - Hodgkin or non-Hodgkin lymphoma, or lymphomatoid granulomatosis.
   - HLH.
   - Hypogammaglobulinemia. The mechanism is unestablished. The 2018 review links hypogammaglobulinemia to low CD27⁺ memory B cells across EBV-susceptibility defects, but I did not see ITK-specific evidence.
   - Autoimmunity (AIHA, renal disease).
7. Open question (MedGen): whether lymphoma and hypogammaglobulinemia occur without EBV.

Proposed ontology terms, to verify by lookup:
- Cell types: CL:0000084 (T cell), CL:0000624 (CD4+ αβ T cell), CL:0000236 (B cell), CL:0000814 (mature NK T cell).
- GO: T cell receptor signaling pathway (GO:0050852).

No transcriptomics, proteomics or single-cell data were searched.

---

## 7. Anatomical structures

- **Organs:** lymph nodes, spleen, liver, kidney (autoimmune), bone marrow (cytopenias, HLH). UBERON IDs were not looked up.
- **Cells:** T cells, iNKT cells, EBV-infected B cells.
- **Subcellular:** cytoplasm and plasma membrane (TCR signalling). No further detail was retrieved.

---

## 8. Temporal development

- Onset is in early childhood (MedGen). Course is progressive in untreated patients.
- Index sisters: one had progressive hypogammaglobulinemia, then Hodgkin lymphoma, and died of *Pneumocystis* pneumonia at age 10. The other had EBV-associated Hodgkin lymphoma and died during aplasia after salvage haploidentical transplant (2018 review snippet).
- No stage or remission data were retrieved.

---

## 9. Inheritance and population

- **Inheritance:** AR, bound to HP:0000007 *[model knowledge]*.
- **Consanguinity:** present in the index family.
- **Geography:** patients come from Turkey, Greece, India, Italy, Iran, Morocco, Pakistan and Palestine (2018 review snippet). A founder effect is not established in the retrieved sources.
- **Prevalence:** no figure retrieved. Orphanet 538963 may carry a class; I did not check it.
- **Sex ratio:** not retrieved.

---

## 10. Diagnostics

All from model knowledge unless noted:
- Lymphocyte subsets (low CD4, low iNKT).
- Immunoglobulins.
- EBV PCR.
- Tissue biopsy of lymphoproliferation.
- Genetic testing: *ITK* appears on the Australian PanelApp "Combined Immunodeficiency" panel (supported by the PanelApp snippet). WES or a primary immunodeficiency panel is the practical route.
- ITK protein expression by flow or immunoblot is a plausible functional test.
- I found no diagnostic criteria or screening programme.
- Differentials: XLP1, XIAP deficiency, CD27/CD70 deficiency, other EBV-susceptibility inborn errors, and lymphomas without a germline cause.

---

## 11. Prognosis

- Mortality is high in the described patients: both index sisters died. No survival series was retrieved.
- The 2018 review advocates early definitive HSCT.
- Complications: lymphoma, HLH, opportunistic infection (*Pneumocystis*), autoimmunity.

---

## 12. Treatment

- **Definitive:** HSCT (NCIT:C15431, hematopoietic cell transplantation). The recommendation is from the 2018 review snippet. No outcome data were retrieved.
- **Supportive** *[model knowledge]*:
  - Immunoglobulin replacement.
  - *Pneumocystis* prophylaxis.
  - Anti-CD20 therapy (rituximab) for EBV B-cell proliferation.
  - Lymphoma-directed chemotherapy.
- **Experimental:** no trials were searched.
- **Pharmacogenomics:** none known.

---

## 13. Prevention

- Genetic counselling for AR recurrence.
- Cascade testing of sibs.
- Prenatal or preimplantation diagnosis once the familial variants are known.
- EBV avoidance is not realistic.
- The retrieved sources contain no guideline.

---

## 14. Other species

Not researched. Please do not infer from absence. *ITK* orthologues exist in mouse. OMIA was not queried.

---

## 15. Model organisms

- *Itk*-knockout mice are known from the literature *[model knowledge]*. I retrieved no source on their phenotype or on how well they recapitulate the human disease.
- MGI, IMPC and ZFIN were not searched.
- The `animal_models` section should wait for a primary citation.

---

## Gaps to close before curating

1. Get verified PMIDs by `just fetch-reference` for:
   - The 2009 index-family paper.
   - The ITK deficiency cohort papers.
   - PMC4220104 and PMC5951928, via their PMIDs.
2. Confirm the Orphanet 538963 and OMIM 613011 text, including any prevalence class and the OMIM title wording.
3. Look up every HPO, CL, GO and UBERON term above. None was read from a source in this session.
4. Check ClinGen for an *ITK* validity record.
5. Find an HSCT outcomes series, and check for any ITK-specific therapy.
6. Find *Itk*-knockout evidence.

Sources:
- [MedGen 765548](https://https.ncbi.nlm.nih.gov/medgen/765548)
- [MONDO:0013081 via SAIL concept library](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0013081/)
- [LOVD disease 03228](https://databases.lovd.nl/shared/diseases/03228)
- [PanelApp Australia, Combined Immunodeficiency, *ITK*](https://panelapp-aus.org/panels/223/gene/ITK/)
- [ITK Deficiency: Clinical and Molecular Aspects, PMC4220104](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4220104/)
- [ITK Deficiency: New Patients, New Insight?, PMC5951928](https://pmc.ncbi.nlm.nih.gov/articles/PMC5951928/)
- [MalaCards LPFS1](https://malacards.org/card/lymphoproliferative_syndrome_1)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 2 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 17 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 10 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0005406` (1 mention) - the report calls it "CD4 lymphopenia"; HP calls it **Recurrent bacterial skin infections**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002482` (1 mention), reported as "Hemophagocytic lymphohistiocytosis" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000624` (1 mention) - the report calls it "CD4+ αβ T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `GO:0050852` (1 mention) - the report calls it "GO: T cell receptor signaling pathway"; GO calls it **T cell receptor signaling pathway**