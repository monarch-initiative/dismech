---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-12T15:57:40.271801'
end_time: '2026-10-12T15:59:24.188398'
duration_seconds: 103.92
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: absence of fingerprints-congenital milia syndrome
  mondo_id: ''
  category: ''
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
  num_turns: 14
  total_cost_usd: 0.8384554
  session_id: c5bca049-79dd-565a-9d58-3e2354d3de80
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 6
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:21820097
  relevance_assessed: 16
  on_topic: 8
  off_topic: 1
  off_topic_references:
  - PMID:31011502
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 16
  verified: 16
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 0
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0007507
    reported_labels:
    - MONDO
    ontology_label: absence of fingerprints-congenital milia syndrome
  - term_id: HP:0010293
    reported_labels:
    - Present from birth, defining feature; stable
    ontology_label: Aplasia/Hypoplasia of the uvula
  - term_id: HP:0007410
    reported_labels:
    - check
    ontology_label: Palmoplantar hyperhidrosis
  - term_id: HP:0001188
    reported_labels:
    - check
    ontology_label: Hand clenching
  - term_id: HP:0001597
    reported_labels:
    - check
    ontology_label: Abnormal nail morphology
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** absence of fingerprints-congenital milia syndrome
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **absence of fingerprints-congenital milia syndrome** covering all of the
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

I'll load the search tools first, then run the literature searches.

Bash is gated; I'll use WebFetch against Europe PMC instead.

# Research report: absence of fingerprints–congenital milia syndrome (Basan syndrome)

**Scope and verification limits.** I ran a limited set of searches. Europe PMC returned titles and abstracts. PubMed and PMC full text were blocked from this environment (bot checks). Four consequences follow:
- Items marked **[verified]** come from an abstract or record I actually saw.
- Items marked **[unverified]** come from an aggregator or my own recall. Resolve them with `just fetch-reference` and OAK before binding.
- I have not provided exact abstract quotes. Take snippets from the cached references after `just fetch-reference PMID:<id>`.
- Per the CURIE rule in CLAUDE.md, every ontology ID below is a lead until it has been looked up.

---

## 1. Disease information

**Overview.** Basan syndrome is a rare autosomal dominant ectodermal dysplasia-like genodermatosis. It features congenital absence of dermatoglyphs (adermatoglyphia), transient facial milia, and neonatal acral blistering. Reduced or absent sweating is also described. It is caused by variants that disrupt the skin-specific isoform of *SMARCAD1*. A 2021 paper describes it as having "congenital adermatoglyphia (absent fingerprints), transient facial milia, neonatal acral bullae, and absent or reduced sweating", with only about 10 kindreds reported worldwide (PMID:34909722) [verified, paraphrased].

**Identifiers.**

| System | Value | Status |
|---|---|---|
| OMIM (Basan syndrome) | 129200 | secondary aggregator [unverified] |
| Orphanet | 1658 | aggregator [unverified] |
| MONDO | MONDO:0007507 | aggregator [unverified] |
| MedGen | 140808 | aggregator [unverified] |
| OMIM (isolated adermatoglyphia, AD) | 136000 | my recall [unverified] |

**Synonyms.** These come from the OMIM text quoted by GeneBe [verified]:
- Basan syndrome
- Baird syndrome
- Adermatoglyphia with congenital facial milia and acral blisters, digital contractures, and nail abnormalities
- Absence of fingerprints-congenital milia syndrome

Related terms are "SMARCAD syndrome" and "immigration delay disease" (the isolated form, PMID:20619487).

**Nosology (important for lump/split).** A 2018 report proposes that Basan syndrome and isolated autosomal dominant adermatoglyphia (ADG, which includes hypohidrosis) are one spectrum, which it calls "SMARCAD syndrome" (PMID:30289605) [verified]. A 2022 paper adds Huriez syndrome as allelic (PMID:35212137) [verified].
- The 2016 Chinese-family study found the same splice variant (c.378+1G>T) in Basan syndrome and in a previously reported isolated-ADG family (PMID:26932190) [verified].
- Recommendation: enter this as a `DISEASE` with `has_subtypes` or `mondo_mappings` for ADG. Consider a `Grouping` for the SMARCAD1 skin-isoform spectrum (Basan, ADG, Huriez), and read the lump/split rules before deciding.

**Data source.** All sources are aggregated literature on families. There is no EHR-derived data.

## 2. Etiology

- **Cause.** Germline heterozygous variants in *SMARCAD1* affecting the skin-specific isoform. Apart from one large deletion, all reported variants are point mutations in the donor splice site of the alternative exon 1 that defines that isoform (PMID:34909722) [verified].
- **Genetic risk and modifiers.** No modifier genes or protective alleles are reported in what I found.
- **Environmental risk, protective factors and gene-environment interactions.** None are reported. Heat exposure matters only as a complication of reduced sweating (see §11).

## 3. Phenotypes

Frequencies are not quantified in the abstracts I saw. Entries are qualitative. HPO IDs are leads, not verified.

| Phenotype | Notes | HPO lead |
|---|---|---|
| Adermatoglyphia | Present from birth, defining feature; stable | HP:0010293 |
| Facial milia, congenital | Transient; extensive in some neonates (PMID:33486784) | HP:0001056 |
| Neonatal acral blistering | Hands and feet; recurrent in infancy | HP:0007410 (check) |
| Hypohidrosis / reduced sweating | Described in Basan and ADG (PMID:30289605, PMID:34909722) | HP:0000966 |
| Digital contractures | Part of the OMIM-described syndrome | HP:0001188 (check) |
| Nail dystrophy / nail abnormalities | Part of the OMIM-described syndrome | HP:0001597 (check) |
| Hyperpigmentation, knuckle pads | Seen in some members of a Chinese pedigree (PMID:26932190) | HP:0000953, HP:0001806 (check) |

- **Onset.** Congenital or neonatal. Milia regress in early life [inferred].
- **Quality of life.** Mainly practical. Fingerprint-based identification fails (PMID:31011502, PMID:36578701). Heat intolerance is possible. No QoL instrument data found.
- **Cancer.** A report of cutaneous SCC in a Basan family (PMID:35592705) was **retracted** (PMID:37387737). Do not cite it. SCC risk is a feature of the allelic Huriez syndrome (PMID:40806836).

## 4. Genetic/molecular information

- **Gene.** *SMARCAD1* (4q22-q23; the linkage region in the Nousbeck family was 4q22). HGNC `hgnc:18398` and NCBI Gene 56916 are my recall [unverified]. Look the CURIE up before binding.
- **Variants** [verified unless noted]:
  - ADG family: a heterozygous donor-splice-site mutation in a skin-specific exon of the short isoform. Minigene assays show aberrant splicing that destabilises the short RNA isoform (PMID:21820097).
  - Chinese family: c.378+1G>T (NG_031945.1), segregating with disease, LOD 3.01 (PMID:26932190).
  - Sporadic case: NM_001254949.1:c.-10+2T>G in the skin-isoform exon 1 donor site. The six reported splice variants all affect this donor (PMID:30289605).
  - Canadian family: a complex structural variant (deletion plus nontandem inverted duplication) removing the first nine exons, including the skin-isoform exon 1. The authors infer that one copy of full-length SMARCAD1 suffices, but not of the skin isoform (PMID:34909722).
  - Dutch family: a 12-bp deletion spanning the exon-intron junction of the skin-specific exon 1 (PMID:34909722).
  - South Indian family: a novel variant (PMID:37966719; details not retrieved).
- **Consequence.** Loss of the skin-specific isoform. This is a loss-of-function / isoform-specific haploinsufficiency model (`functional_impact_category` likely LOSS_OF_FUNCTION, but the sources frame it as isoform loss).
- **Epigenetic and chromosomal.** *SMARCAD1* encodes a chromatin remodeller; no methylation signature has been reported. Other than the structural variant above, no chromosomal abnormalities are reported.

## 5. Environmental information

No environmental, lifestyle or infectious factors are reported.

## 6. Mechanism / pathophysiology

**Causal chain.**
1. A heterozygous germline splice-donor (or exon-1-deleting) variant in the skin-specific *SMARCAD1* exon 1 alters splicing of the skin isoform (demonstrated by minigene assay, PMID:21820097).
2. This destabilises the short, skin-specific transcript, so there is less skin-specific SMARCAD1 protein (demonstrated at RNA level; protein level inferred).
3. Reduced SMARCAD1, a SNF2-family helicase and chromatin remodeller, is presumed to impair chromatin remodelling in developing epidermis (inferred; the reviewed sources describe the mechanism as unclear).
4. The authors "conclude that the skin-specific isoform plays a role in dermatoglyph development" (PMID:21820097, paraphrased). This leads to failure of epidermal ridge patterning (adermatoglyphia).
5. **Branch, inferred:** altered epidermal and appendage development leads to the features seen in Basan syndrome. These are milia (probably retention of keratinising structures), acral blistering and impaired sweat gland function (hypohidrosis).
6. Some of the milder, ridge-only presentations correspond to the isolated ADG end of the spectrum. The determinants of this variability are unknown.

Steps 3 to 5 are not experimentally demonstrated in the sources I saw.

- **Cell types and structures.** Epidermal keratinocytes (CL:0000312, lead), eccrine sweat gland, and the dermal-epidermal junction.
- **GO leads.** Chromatin remodeling (GO:0006338), nucleosome remodeling, epidermis development (GO:0008544). Verify each by lookup.
- **Molecular profiling.** No omics data found.
- **Other mechanisms.** *SMARCAD1* interacts with TFIIIC and architectural proteins (PMID:37761933), and zebrafish *smarcad1a* loss accelerates nerve sheath tumorigenesis (PMID:34296799). These are context for the gene, not shown to be disease mechanisms here.

## 7. Anatomical structures affected

- **Primary.** Skin of the fingertips, palms and soles (UBERON:0002097 skin; fingertip and palm are leads), face (milia), acral skin (blisters), and nails.
- **Secondary.** Eccrine sweat glands; joints and digits (contractures).
- **Laterality.** Bilateral, symmetric [inferred].

## 8. Temporal development

- **Onset.** Congenital. Blistering is neonatal.
- **Course.** Milia are transient. Absent dermatoglyphs are permanent. No progression has been described.

## 9. Inheritance and population

- **Inheritance.** Autosomal dominant (HP:0000006, lead). Penetrance for adermatoglyphia is apparently complete in the reported families; expressivity of the extracutaneous features varies. This is partly my reading and not quantified in the sources.
- **Epidemiology.** Only about 10 kindreds have been reported worldwide (PMID:34909722). No prevalence or incidence estimate was found; consider `prevalence_class` of `NOT_YET_DOCUMENTED` or an ultra-rare class, supported by the "~10 kindreds" statement, with `measure_type: CASES_IN_LITERATURE`.
- **Population.** Families are reported from Switzerland and the Middle East (ADG), China, Canada, the Netherlands and India. No founder effect is established.
- **De novo cases.** The sporadic case in PMID:30289605 suggests *de novo* occurrence is possible.

## 10. Diagnostics

- **Clinical.** Examination shows absent ridge patterns, neonatal milia and acral blisters, and a family history.
- **Genetic.** Sequence *SMARCAD1*, **including the non-canonical exon 1 of the skin isoform**. Standard exome panels may miss it, and a structural variant may need optical mapping or WGS (PMID:34909722; PMID:26932190 used WGS).
- **Differential.** Huriez syndrome (palmoplantar keratoderma, sclerodactyly, SCC risk, allelic), other ectodermal dysplasias, and epidermolysis bullosa for the neonatal blistering. Features to distinguish them are not fully sourced here.
- **Screening.** None applicable. No biochemical or imaging markers are known.

## 11. Outcome/prognosis

- **Survival.** No life-shortening is reported in the sources found. No survival data.
- **Complications.** Heat intolerance from hypohidrosis; practical identification problems (PMID:31011502); contractures and nail dystrophy.
- **Cancer.** Not established for Basan syndrome (retracted report, above).

## 12. Treatment

No disease-specific therapy exists. Management is supportive: wound care for blisters, avoiding overheating, hand therapy for contractures, and genetic counselling. NCIT leads such as `NCIT:C15747` (Supportive Care) and `NCIT:C15240` (Genetic Counseling) are those listed in CLAUDE.md. I found no clinical trials; a ClinicalTrials.gov search should be run before recording that none exist. No pharmacogenomics or gene therapy has been reported.

## 13. Prevention

Genetic counselling for autosomal dominant transmission, prenatal or preimplantation diagnosis if the family variant is known, and counselling about heat avoidance. No primary or secondary prevention is established.

## 14. Other species / natural disease

I did not search OMIA, so I cannot say whether a naturally occurring analogue exists. *Smarcad1* orthologues exist in mouse and zebrafish. A zebrafish *smarcad1a* loss study exists, but it concerns tumour suppression (PMID:34296799).

## 15. Model organisms

I found no animal model that recapitulates adermatoglyphia. Mice lack human-type fingerprint ridges, which makes a model of ridge patterning inherently limited. Check MGI/IMPC for *Smarcad1* alleles before recording this as a `KNOWLEDGE_GAP` or `HUMAN_MODEL_MISMATCH`.

---

## Key references (PMIDs verified through Europe PMC listings)

| PMID | Year | Topic |
|---|---|---|
| 21820097 | 2011 | Nousbeck et al., *Am J Hum Genet*. Skin-specific SMARCAD1 isoform mutation causes AD adermatoglyphia |
| 20619487 | 2010/2011 | Burger et al., *J Am Acad Dermatol*. Immigration delay disease |
| 26932190 | 2016 | Chinese Basan family, c.378+1G>T, *Eur J Hum Genet* |
| 30289605 | 2018 | "Basan gets a new fingerprint", unifying SMARCAD syndrome, *Am J Med Genet A* |
| 33400266 | 2021 | Large deletion removing the skin isoform causes Huriez syndrome, *Br J Dermatol* |
| 33486784 | 2021 | Two cases with extensive congenital milia, *Pediatr Dermatol* |
| 34909722 | 2021 | Canadian and Dutch families, *JID Innovations* |
| 35212137 | 2022 | Huriez syndrome allelism, *Am J Med Genet A* |
| 37966719 | 2024 | South Indian family, *Clin Exp Dermatol* |
| 31011502 | 2019 | Biometric identification barriers, *Cureus* |
| 36578701 | 2022 | Adermatoglyphia and biometrics, *Indian J Dermatol* |
| 35592705 / 37387737 | 2022 / 2023 | SCC report and its **retraction**; do not cite as evidence |

**Gaps to close before curation.** Confirm the OMIM, Orphanet and MONDO IDs and the HGNC ID. Verify the HPO and GO leads. Obtain the phenotype frequencies from full text (especially PMID:21820097, PMID:34909722 and PMID:33486784). Check OMIA, MGI and ClinicalTrials.gov. Fetch the references and take exact snippets from the cache.

Sources:
- [Nousbeck et al. 2011, PMC3155166](https://pmc.ncbi.nlm.nih.gov/articles/PMC3155166)
- [Basan syndrome, Wikipedia](https://en.wikipedia.org/wiki/Absence_of_fingerprints-congenital_milia_syndrome)
- [Chinese Basan family, PMID 26932190](https://pubmed.ncbi.nlm.nih.gov/26932190/)
- [Basan syndrome, KEGG](https://www.kegg.jp/entry/H02296)
- [Two SMARCAD1 variants, JID Innovations](https://doaj.org/article/c088cd670cde426bb7668ad2ac3a1bc6)
- [Huriez allelism, PMID 35212137](https://pubmed.ncbi.nlm.nih.gov/35212137/)
- Europe PMC REST search results (PMIDs and abstracts)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 16 |
| On topic | 8 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:21820097` *(abstract only)*: "conclude that the skin-specific isoform plays a role in dermatoglyph development"
  - closest text in source: "Taken together, the present findings implicate a skin-specific isoform of SMARCAD1 in the regulation of dermatoglyph development."

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:31011502` (2 mentions) - Adermatoglyphia: Barriers to Biometric Identification and the Need for a Standardized Alternative.
  - shared terms: adermatoglyphia

Weighed against this report's own most characteristic terms: `smarcad1`, `milia`, `syndrome`, `found`, `variant`, `lead`, `basan`, `family`, `isoform`, `adermatoglyphia`, `verified`, `skin-specific`, `congenital`, `acral`, `adg`, `skin`, `disease`, `feature`, `genetic`, `blistering`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 5 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007507` (1 mention) - the report calls it "MONDO"; MONDO calls it **absence of fingerprints-congenital milia syndrome**
- `HP:0010293` (1 mention) - the report calls it "Present from birth, defining feature; stable"; HP calls it **Aplasia/Hypoplasia of the uvula**
- `HP:0007410` (1 mention) - the report calls it "check"; HP calls it **Palmoplantar hyperhidrosis**
- `HP:0001188` (1 mention) - the report calls it "check"; HP calls it **Hand clenching**
- `HP:0001597` (1 mention) - the report calls it "check"; HP calls it **Abnormal nail morphology**