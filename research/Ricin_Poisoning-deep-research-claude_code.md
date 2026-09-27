---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-17T23:40:42.014390'
end_time: '2026-09-17T23:46:04.512541'
duration_seconds: 322.5
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Ricin Poisoning
  mondo_id: MONDO:0035511
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
  - claude-sonnet-5
  web_search_requests: 26
  num_turns: 28
  total_cost_usd: 1.8571474
  session_id: dc83c613-1fba-53b8-9741-f63fb2448a6e
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 62
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 31
  on_topic: 18
  validator_version: 0.2.1
term_validation:
  total_terms: 47
  verified: 46
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 3
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0000975
    reported_labels:
    - verify
    ontology_label: Hyperhidrosis
  - term_id: HP:0006515
    reported_labels:
    - verify
    ontology_label: Interstitial pneumonitis
  - term_id: HP:0001626
    reported_labels:
    - cardiac
    ontology_label: Abnormality of the cardiovascular system
  - term_id: CL:0000584
    reported_labels:
    - Enterocytes / intestinal epithelial cells
    ontology_label: enterocyte
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0030433
    ontology_label: obsolete ubiquitin-dependent ERAD pathway
    replaced_by: GO:0036503
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ricin Poisoning
- **MONDO ID:** MONDO:0035511 (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Ricin Poisoning** covering all of the
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

I'll research ricin poisoning comprehensively across the requested domains. Let me start by gathering information from primary literature and toxicology databases.

I now have comprehensive, well-sourced material across all major domains. Compiling the final report.

---

# Ricin Poisoning: Comprehensive Research Report

## 1. Disease Information

### Overview
Ricin poisoning is an acute, potentially life-threatening toxidrome caused by exposure — via ingestion, inhalation, injection, or (rarely) ocular/dermal contact — to ricin, a highly potent ribosome-inactivating protein (RIP) lectin found in the seeds ("castor beans") of *Ricinus communis* L. (family Euphorbiaceae), the castor oil plant. The condition is not a genetic disease but an environmentally/intentionally acquired **toxin-mediated cellular injury syndrome**: a single ricin molecule reaching the cytosol can inactivate ribosomes at a rate of ~1,500 per minute and is considered potentially lethal to that cell [StatPearls NBK441948](https://www.ncbi.nlm.nih.gov/books/NBK441948/). Clinical severity and organ pattern depend heavily on the route of exposure, with inhalation being the most toxic route per unit dose, followed by parenteral injection, then ingestion [StatPearls; NORD](https://rarediseases.org/mondo-disease/ricin-poisoning/).

Ricin is produced as a defensive protein in the endosperm of castor seeds; the waste "mash" remaining after industrial extraction of castor oil (used for lubricants, biodiesel, and pharmaceutical excipients) contains approximately 5% ricin by weight, making it a large-scale, low-cost byproduct with genuine dual-use/bioterrorism concern [StatPearls; CDC](https://www.cdc.gov/chemical-emergencies/chemical-fact-sheets/ricin.html). Ricin is one of the most acutely toxic substances known — reported to be roughly 400× more toxic than cobra venom, 1,000× more toxic than cyanide, and 4,000× more toxic than arsenic on a molar/weight basis [WebSearch synthesis of toxicology reviews].

### Key Identifiers
- **MONDO:** MONDO:0035511 (ricin poisoning) — as provided in the task; cross-referenced by NORD/[rarediseases.org MONDO page](https://rarediseases.org/mondo-disease/ricin-poisoning/) and MalaCards ([Ricin Poisoning – MalaCards](https://www.malacards.org/card/ricin_poisoning)).
- **ICD-10-CM:** T62.2X– series ("Toxic effect of other ingested (parts of) plant(s)"), with 5th/6th/7th-character modifiers for intent (accidental T62.2X1–, intentional self-harm T62.2X2–, assault T62.2X3–, undetermined T62.2X4–) and encounter type (initial A, subsequent D, sequela S) [ICD List](https://icdlist.com/icd-10/T62.2X1A). No dedicated ICD-10 code exists specifically for "ricin" as distinct from generic plant-toxin ingestion; inhalational/parenteral ricin exposure would code under the corresponding T-code sections for those routes (curators should verify per current ICD-10-CM/ICD-11 tabular index rather than relying on T62.2 alone for non-oral routes).
- **CDC Select Agent status:** Ricin toxin is a **CDC Category B bioterrorism agent** and is listed as a **Schedule 1 toxic chemical under the Chemical Weapons Convention** [WebSearch synthesis; CDC/NIOSH].
- **CHEBI:** A specific curator-verified CHEBI accession for ricin (the ~65 kDa heterodimeric holotoxin) was **not confirmed** through available web search in this session — ChEBI is queryable at ebi.ac.uk/chebi, but no authoritative ID could be extracted from search snippets alone. **This should be verified directly via OAK/ChEBI lookup before binding any CHEBI CURIE** (per the project's "never write an ontology identifier from memory" rule).
- **NCIT:** Not confirmed from search results; verify via `runoak -i sqlite:obo:ncit search "ricin"` for the correct term prior to binding.
- **Structural biology:** Ricin is a ~65 kDa disulfide-linked AB-toxin glycoprotein: the **A chain (RTA, ~32 kDa)** is the catalytic N-glycosidase; the **B chain (RTB, ~34 kDa)** is a galactose/N-acetylgalactosamine-specific lectin. Isoforms D and E have been characterized [Medical Countermeasures against Ricin Intoxication, *Toxins* 2023, doi:10.3390/toxins15020100](https://doi.org/10.3390/toxins15020100); [A Monoclonal Antibody with High Affinity for Ricin Isoforms D and E, *Toxins* 2024](https://www.mdpi.com/2072-6651/16/10/412).

### Synonyms / Alternative Names
Ricin toxin; castor bean toxin; *Ricinus communis* agglutinin II (RCA-II, to distinguish the toxic lectin from the non-toxic agglutinin RCA-I); "the perfect poison" (media/forensic shorthand); castor bean poisoning; ricinus toxicosis (veterinary usage).

### Data Provenance
Information here derives from aggregated disease-level literature — case reports/series, systematic reviews, toxicology textbooks (StatPearls), CDC/NIOSH/OSHA fact sheets, and mechanistic bench-science publications — rather than a single large EHR cohort. No dedicated disease registry or large aggregated-EHR cohort for ricin poisoning was identified; most epidemiological and clinical-course data come from individual case reports, small case series, forensic/medico-legal case compilations, and animal-model extrapolation.

---

## 2. Etiology

### Disease Causal Factor
Ricin poisoning has a single, well-defined **toxicological (non-genetic, non-infectious) etiology**: exposure to ricin protein, either from crude castor-seed material (chewed/crushed seeds, seed mash, homemade extracts) or from purified/semi-purified ricin preparations (forensic/bioterrorism scenarios). As few as **two chewed castor seeds** can cause toxicity in a child, although some adult patients have survived ingesting up to 30 seeds because intact (unchewed) seed coats resist digestion and pass through the GI tract without releasing ricin [StatPearls NBK441948](https://www.ncbi.nlm.nih.gov/books/NBK441948/).

### Risk Factors

**Environmental/exposure risk factors (the dominant causal axis for this entry):**
- Occupational exposure in castor-oil processing facilities (seed handling, mash disposal)
- Deliberate/criminal exposure (bioterrorism, assassination, self-harm) — historically documented incidents include the 1978 Georgi Markov assassination (injected ricin-laden pellet), the 2003/2004 White House and Senate mail incidents, and the 2013 letters mailed to President Obama and others [Wikipedia: List of incidents involving ricin; FBI press releases](https://www.fbi.gov/contact-us/field-offices/newyork/news/press-releases/manhattan-u.s.-attorney-and-fbi-assistant-director-announce-arrest-of-new-york-man-for-attempting-to-acquire-deadly-toxin-ricin)
- Accidental pediatric ingestion of ornamental castor bean plant seeds (castor bean is a common ornamental/landscaping plant)
- Ingestion of adulterated herbal remedies containing castor bean material
- Route of exposure itself strongly modifies risk: inhalation LD (5–10 µg/kg) << injection << ingestion (1–20 mg/kg) [StatPearls]
- Age: pediatric patients are at higher risk from smaller absolute seed quantities due to lower body weight and greater likelihood of exploratory ingestion

**Genetic/host risk and modifying factors (mechanistic, not classic Mendelian susceptibility):**
- A genome-wide mammalian genetic-interaction screen identified ~200 host factors that sensitize or protect cells from ricin, clustering around the retrograde-transport pathway, ribosome biogenesis, and cholesterol biosynthesis (HMG-CoA reductase inhibitors dose-dependently protect ricin-exposed cells) [A Systematic Mammalian Genetic Interaction Map Reveals Pathways Underlying Ricin Susceptibility, *Cell* 2013](https://www.cell.com/fulltext/S0092-8674(13)00082-2)
- Cell-surface glycosylation state modulates susceptibility: inactivation of the sialyltransferase responsible for Lewis X modification increases ricin sensitivity, while its overexpression confers relative resistance — i.e., host glycan "sugar code" is a documented modifier of cellular vulnerability [A vital sugar code for ricin toxicity, *Cell Research* 2017](https://www.nature.com/articles/cr2017116)
- No human Mendelian susceptibility locus or population-level genetic risk variant for ricin poisoning has been established in the literature surveyed; this is fundamentally an acute environmental exposure, not a heritable disease.

**Protective factors:**
- Active immunization (RiVax/RVEc vaccines — see Treatment/Prevention) confers antibody-mediated protection in vaccinated individuals
- Passive immunization with neutralizing anti-ricin monoclonal antibodies administered pre- or shortly post-exposure
- Small-molecule retrograde-transport inhibitors (Retro-2) in preclinical models
- HMGCR inhibitors (statins) show in vitro protective effects against ricin cytotoxicity, an unconfirmed but mechanistically plausible protective lead
- Unbroken/unchewed seed coat (intact castor seeds largely resist gastric digestion, limiting toxin release)

### Gene-Environment Interaction
There is no established classical gene-environment interaction for human disease susceptibility to ricin analogous to pharmacogenomic drug-metabolism variability. The closest documented analog is the cell-intrinsic host-factor network above (glycosylation machinery, retrograde-transport genes, cholesterol biosynthesis genes) that determines cellular — not organismal — susceptibility in experimental systems, which is a mechanistic rather than epidemiological GxE finding.

---

## 3. Phenotypes

Ricin poisoning phenotypes are strongly **route-dependent**. All are acute-onset (minutes to ~24 hours), non-progressive in a chronic sense (the condition either resolves with supportive care or evolves to multi-organ failure/death over days), and none currently have HPO frequency data (this is an acute toxidrome, not a chronic Mendelian phenotype set, so classic HPO frequency percentages from cohort studies are largely unavailable — most frequency information below is qualitative/case-series-derived).

### A. Ingestion (oral) route
| Phenotype | Suggested HP term | Onset/Notes |
|---|---|---|
| Nausea | HP:0002018 Nausea | Onset 15 min–20 h post-ingestion |
| Vomiting | HP:0002013 Vomiting | Early, prominent |
| Diarrhea (often hemorrhagic) | HP:0002014 Diarrhea | — |
| Abdominal pain / colic | HP:0002027 Abdominal pain | — |
| Hematemesis | HP:0002248 Hematemesis (or closest available HPO term) | Indicates GI mucosal necrosis |
| Melena | (search for closest HP GI-bleeding term) | — |
| Hepatic necrosis | HP:0001395 Hepatic necrosis (verify exact term) | Multi-organ target |
| Renal tubular necrosis / acute kidney injury | HP:0000083 Renal insufficiency / acute tubular necrosis term | — |
| Splenic necrosis | (verify HPO term) | Reported at autopsy in fatal cases |
| Hypovolemic shock | HP:0032263 or closest shock term | Late-stage |

[StatPersk; Ricin intoxication by lethal dose of castor seeds ingestion: a case report, *PMC* 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11363666/)

### B. Inhalation route
| Phenotype | Suggested HP term | Notes |
|---|---|---|
| Cough | HP:0012735 Cough | — |
| Wheezing | HP:0030828 Wheezing | — |
| Dyspnea | HP:0002094 Dyspnea | — |
| Sore throat / pharyngeal congestion | (verify HP term) | — |
| Fever | HP:0001945 Fever | — |
| Chest tightness | (verify HP term) | — |
| Diaphoresis | HP:0000975 (verify) | — |
| Pulmonary edema | HP:0100598 Pulmonary edema | Onset within hours |
| Interstitial pneumonia / necrotizing pneumonia | HP:0006515 (verify) | Documented in animal inhalation models and human case reports |
| Respiratory failure | HP:0002878 Respiratory failure | Terminal event in severe cases |

Animal inhalation-model pathology corroborates the human picture: mice exposed to sublethal inhaled ricin show "marked interstitial pneumonia, neutrophil infiltration, pro-inflammatory cytokine response, alveolar macrophage and alveolar epithelial type II cell death and edema" over days 1–7, with residual peribronchial/perivascular inflammation, alveolar wall thickening, and possible mild fibrosis of respiratory bronchioles by day 34–96 [Short- and long-term outcomes of pulmonary exposure to a sublethal dose of ricin in mice, *Scientific Reports* 2024](https://www.nature.com/articles/s41598-024-62222-9); [Comparative Aspects of Ricin Toxicity by Inhalation, *Toxins* 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10145923/).

### C. Injection/parenteral route
| Phenotype | Suggested HP term | Notes |
|---|---|---|
| Localized erythema/induration at injection site | (verify HP term) | Immediate |
| Blistering | HP:0008066 Bullous skin lesions (verify closest) | — |
| Capillary leak syndrome | (search HP; may need free text) | Systemic vascular injury |
| Localized tissue necrosis | HP:0031630 or verify | — |
| Coagulopathy / prolonged PT-APTT | HP:0001928 Abnormal coagulation | Documented in mouse/swine IM models |
| Thrombocytopenia | HP:0001873 Thrombocytopenia | 4–5-fold platelet decrease by 48–72h in mouse IM models |
| Shock | — | — |
| Multi-organ failure | HP:0001626 (cardiac) plus organ-specific terms | — |

The classic Markov-case clinical course: "pain developed immediately at the injection site, weakness developed within 5 hours, fever and vomiting developed within 24 hours, followed by shock and multi-organ failure, and death within 3 days" [Ricin and the Assassination of Georgi Markov](https://www.researchgate.net/publication/23781130_Ricin_and_the_Assassination_of_Georgi_Markov).

### D. Systemic / laboratory phenotypes (multiple routes)
- **Hypoglycemia**: parenteral ricin exposure in mice induces fatal hypoglycemia via cytokine-mediated suppression of hepatic glucose-6-phosphatase expression [Parenteral Exposure of Mice to Ricin Toxin Induces Fatal Hypoglycemia by Cytokine-Mediated Suppression of Hepatic Glucose-6-Phosphatase Expression, *PMC* 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9786807/) — a plausible-but-model-organism-only finding (evidence_source: MODEL_ORGANISM)
- **Cytokine storm**: sudden acute rise in circulating pro-inflammatory cytokines (TNF-α rises early/rapidly; IL-6, IL-1, IFN-γ, IL-17 rise later, if at all) [Frontiers in Immunology 2022](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2022.900755/xml)
- **Endothelial glycocalyx shedding**: elevated soluble heparan sulfate, hyaluronic acid, and syndecan-1 in blood, with microvascular flow abnormality [Intramuscular Exposure to a Lethal Dose of Ricin Toxin Leads to Endothelial Glycocalyx Shedding, *PMC* 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8618821/)
- **Leukocytosis, electrolyte abnormalities, hepatic/renal failure markers** on routine labs [StatPearls]

### Quality of Life Impact
Acute survivors generally recover fully with no long-term sequelae if supportive care is prompt (see Prognosis); however, animal inhalation models show residual pulmonary fibrosis and inflammatory changes persisting for weeks to months after sublethal exposure, raising the possibility of long-term respiratory impairment in inhalation survivors — no dedicated human quality-of-life instrument data (EQ-5D/SF-36) for ricin-poisoning survivors were identified in this search.

---

## 4. Genetic/Molecular Information

**Ricin poisoning has no causal human gene** — it is a toxin-exposure syndrome, not an inherited disease. This section is therefore reframed around the toxin's own molecular biology and the host genes it acts on/through, rather than a human disease-gene table.

### The toxin's own molecular identity (source organism: *Ricinus communis*, not human)
- Ricin is encoded by a gene family in castor bean; the mature protein is ~65 kDa, two chains (RTA ~32 kDa, RTB ~34 kDa) joined by a single disulfide bond [ScienceDirect Topics: Ricin overview](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/ricin)
- RTA is a **type II ribosome-inactivating protein (RIP)** N-glycosidase (EC 3.2.2.22)
- Isoforms D and E have been distinguished serologically, with isoform-specific monoclonal antibodies now characterized [*Toxins* 2024](https://www.mdpi.com/2072-6651/16/10/412)

### Host genes/targets relevant to mechanism (for `genetic:` or `biological_processes` annotation purposes, not as causal disease genes)
- **Ricin's molecular target:** a single, universally conserved adenine (**A4324** in humans) within the **sarcin-ricin loop (SRL)** of **28S rRNA**, in the GAGA tetraloop motif — this is an RNA target, not a protein-coding gene, but is essential to describing mechanism
- **ASNA1/TRC40**: mediates ER-targeting/insertion of tail-anchored proteins; required for ricin's translocation route and is the target of the protective small molecule Retro-2 [Retro-2 protects cells from ricin toxicity by inhibiting ASNA1-mediated ER targeting, *eLife* 2019](https://elifesciences.org/articles/48434)
- **HMGCR** (HMG-CoA reductase): cholesterol-biosynthesis pathway gene whose inhibition (statins) protects cells from ricin in vitro [*Cell* 2013 genetic interaction map]
- Sialyltransferase genes controlling Lewis X modification: loss increases ricin sensitivity in cellular models [*Cell Research* 2017]
- **ASGR1** (asialoglycoprotein receptor 1, hgnc-bound gene): plays a well-established role in hepatocyte receptor-mediated endocytosis of galactose/GalNAc-terminal glycoproteins generally, and ricin's B chain binds β-1,4-linked galactose residues on cell-surface glycoproteins/glycolipids broadly — however, a specific literature link establishing ASGR1 as ricin's primary hepatocyte entry receptor was **not confirmed** in this search; ricin's B-chain lectin binding is generally described as promiscuous across galactose/GalNAc-bearing surface receptors rather than ASGR1-specific, and this claim should not be curated without a direct primary-literature citation.

### Variant classification / population frequency
Not applicable — there is no ClinVar/gnomAD-relevant human germline variant catalog for this toxin-exposure condition.

### Epigenetics
No disease-specific epigenetic (DNA methylation/histone) literature for ricin poisoning was identified; this is outside scope for an acute-toxicity condition without chronic epigenetic reprogramming data in the literature surveyed.

### Chromosomal abnormalities
Not applicable.

---

## 5. Environmental Information

### Environmental/Toxicological Factor
The entry's entire "genetic/environmental" causal weight sits on the environmental side: **ricin exposure from *Ricinus communis*** is the sole documented cause. Key environmental-curation points:

- **Source material:** castor bean seed, castor-oil-extraction waste mash (~5% ricin by weight)
- **Routes:** ingestion (seeds, contaminated food/herbal products), inhalation (aerosolized powder — the highest bioterrorism/military concern route), injection (targeted assassination/self-harm), and rarely ocular or transdermal (with abraded skin) contact
- **Toxin stability:** ricin is heat-labile above ~80°C but stable at room temperature for extended periods in dried/powdered form, relevant to environmental persistence and forensic sample handling

### Occupational/Lifestyle Factors
- Castor-oil industry workers handling seed mash
- Home gardeners/ornamental-plant exposure (castor bean is a popular landscaping plant with visually distinctive but attractive spiny seed capsules, posing accidental pediatric ingestion risk)
- Illicit drug/extraction-kit exposure (do-it-yourself extraction from online "recipes," as documented in the 2013 Dutschke case, where beans were purchased on eBay and processed with a coffee grinder [FBI press release](https://www.fbi.gov/contact-us/field-offices/newyork/news/press-releases/manhattan-u.s.-attorney-and-fbi-assistant-director-announce-arrest-of-new-york-man-for-attempting-to-acquire-deadly-toxin-ricin))

### Infectious Agents
Not applicable — ricin poisoning is a non-infectious toxin exposure.

---

## 6. Mechanism / Pathophysiology

### Ordered Causal Chain

1. **Exposure** to ricin-containing material (chewed/crushed castor seeds, extracted toxin powder, or purified ricin) **leads to** systemic or local absorption of the ricin heterodimer, depending on route (GI mucosa for ingestion; alveolar epithelium for inhalation; direct tissue/vascular deposition for injection).
2. The **RTB lectin domain binds** cell-surface glycoproteins/glycolipids bearing terminal β-1,4-linked galactose or N-acetylgalactosamine residues, which **leads to** receptor-mediated (clathrin-dependent or -independent, depending on the specific surface ligand engaged) **endocytosis** of the ricin holotoxin [Ricin transport into cells: studies of endocytosis and intracellular transport, PMID:11111920](https://pubmed.ncbi.nlm.nih.gov/11111920/).
3. Internalized ricin **traffics retrogradely** — early endosome → trans-Golgi network → Golgi → endoplasmic reticulum — bypassing lysosomal degradation via this non-canonical retrograde route, which **is required for** cytotoxicity (this retrograde step is the target of the experimental inhibitor Retro-2) [Inhibition of Retrograde Transport Protects Mice from Lethal Ricin Challenge, *Cell* 2010](https://www.cell.com/fulltext/S0092-8674(10)00078-4).
4. In the ER, **protein disulfide isomerase reduces** the single A-chain/B-chain disulfide bond, and the partially unfolded RTA is **translocated** across the ER membrane into the cytosol via the Sec61 translocon (co-opting the ER-associated degradation/ERAD pathway meant for misfolded host proteins) — this dislocation step **utilizes host ER-targeting/tail-anchored-protein machinery including ASNA1/TRC40** [Dislocation of Ricin Toxin A Chains in Human Cells Utilizes Selective Cellular Factors, *PMC* 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3122183/); [Retro-2 mechanism, *eLife* 2019](https://elifesciences.org/articles/48434).
5. Cytosolic, catalytically active **RTA hydrolyzes the N-glycosidic bond** of a single, universally conserved adenine (**A4324**) within the **sarcin-ricin loop (SRL)** of the 28S ribosomal RNA in the 60S large ribosomal subunit, **irreversibly depurinating** this residue while leaving the RNA phosphodiester backbone intact [Structures and Ribosomal Interaction of Ribosome-Inactivating Proteins, *PMC* 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6273143/).
6. SRL depurination **abolishes** elongation-factor-1-dependent aminoacyl-tRNA binding and elongation-factor-2-dependent GTP hydrolysis at the ribosome, **arresting protein synthesis at the elongation step** — one RTA molecule can inactivate ~1,500 ribosomes/minute, so a very small number of cytosolic RTA molecules is sufficient to shut down a cell's entire translational output.
7. In parallel to (and partly downstream of) direct ribosome inactivation, the damaged sarcin-ricin loop itself **acts as a stress signal**, activating the **ribotoxic stress response (RSR)**: the MAP3K **ZAK** senses SRL damage and **activates p38 MAPK and JNK** stress-activated protein kinase (SAPK) cascades [Structures and Ribosomal Interaction of RIPs; Identification of Small Molecules That Suppress Ricin-Induced Stress-Activated Signaling Pathways, *PLOS ONE*](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0049075).
8. SAPK/RSR activation **drives two convergent downstream branches**:
   - **(8a) Apoptotic branch**: ricin/RTA activates **both the extrinsic (death-receptor) and intrinsic (mitochondrial) apoptosis pathways**, with JNK signaling required for apoptosis in nontransformed epithelial cells [Ricin A-chain requires JNK to induce apoptosis, *PMC*](https://pmc.ncbi.nlm.nih.gov/articles/PMC2783365/).
   - **(8b) Pro-inflammatory branch**: SAPK activation **increases production of pro-inflammatory cytokines** (TNF-α rising early; IL-6, IL-1, IFN-γ, IL-17 rising later in a delayed "cytokine storm" pattern), with airway epithelial NF-κB activation documented after inhalational exposure [Frontiers Immunology 2022](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2022.900755/xml).
9. The combined loss of protein synthesis (step 6), apoptotic cell death (8a), and cytokine-driven inflammation (8b) **leads to** organ-specific tissue injury whose pattern tracks the exposure route: alveolar epithelial/macrophage death, neutrophil infiltration and pulmonary edema after inhalation; enterocyte/hepatocyte/splenocyte necrosis and hemorrhagic GI mucosal injury after ingestion; and local tissue necrosis with systemic vascular injury after injection.
10. Systemically, ricin **binds preferentially to vascular endothelium**, **causing endothelial glycocalyx shedding** (elevated circulating heparan sulfate, hyaluronic acid, syndecan-1) and **microvascular flow abnormality**, which **leads to capillary leak syndrome**, **coagulopathy** (prolonged PT/APTT, thrombocytopenia), and **widespread hemorrhage** [Intramuscular Exposure to a Lethal Dose of Ricin Toxin Leads to Endothelial Glycocalyx Shedding, *PMC* 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8618821/); [Intramuscular Ricin Poisoning of Mice Leads to Widespread Damage in the Heart, Spleen, and Bone Marrow, *Toxins* 2019](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6628730/).
11. A cytokine-mediated suppression of **hepatic glucose-6-phosphatase** expression **contributes to** fatal hypoglycemia in parenteral-exposure mouse models — an additional, partially independent lethal mechanism layered on top of direct cytotoxicity (evidence: MODEL_ORGANISM only) [*PMC* 2022, PMID search](https://pmc.ncbi.nlm.nih.gov/articles/PMC9786807/).
12. The cumulative effect of (9)–(11) — hypovolemic/distributive shock, multi-organ (hepatic, renal, splenic, cardiac, bone-marrow, pulmonary) failure, and refractory cardiovascular collapse — **is the proximate cause of death** in fatal cases, typically within 36–72 hours of severe untreated exposure.

### Molecular Pathways (GO/pathway suggestions)
- Ribosome inactivation / translational elongation arrest: **GO:0017148** (negative regulation of translation), **GO:0006414** (translational elongation)
- rRNA N-glycosidase activity: **GO:0030598** (rRNA N-glycosylase activity)
- Ribotoxic stress response / SAPK activation: **GO:0007254** (JNK cascade), **GO:0038066** (p38MAPK cascade)
- Apoptotic signaling, extrinsic and intrinsic: **GO:0097191** (extrinsic apoptotic signaling pathway), **GO:0097193** (intrinsic apoptotic signaling pathway)
- Retrograde vesicle-mediated transport, Golgi to ER: **GO:0042147** (retrograde transport, endosome to Golgi)
- Endoplasmic-reticulum-associated protein catabolic process (ERAD, co-opted for translocation): **GO:0030433**
- Cytokine-mediated inflammatory response: **GO:0002526** (acute inflammatory response), **GO:0032640** (TNF production)

### Cell Types Involved (CL term suggestions — verify via OAK before binding)
- Alveolar type I/II pneumocytes (CL:0002062, CL:0002063) and alveolar macrophages (CL:0000583) — inhalation route
- Enterocytes / intestinal epithelial cells (CL:0000584) — ingestion route
- Hepatocytes (CL:0000182), splenocytes, renal tubular epithelial cells (CL:1001318 or nearest), vascular endothelial cells (CL:0000115), cardiomyocytes (CL:0000746), bone marrow hematopoietic cells
- Neutrophils (CL:0000775) — prominent infiltrating effector cell in pulmonary injury

### Anatomical structures targeted (UBERON — verify via OAK)
Lung/respiratory epithelium (inhalation), small/large intestine mucosa (ingestion), liver, spleen, kidney (particularly renal tubules), bone marrow, heart, and systemic vasculature/microvasculature (all routes, secondary to endothelial tropism).

### Molecular profiling
No large-scale human transcriptomic/proteomic/metabolomic dataset specific to ricin poisoning was identified; mouse pulmonary gene-expression profiling after inhaled ricin has been reported [Pulmonary gene expression profiling of inhaled ricin, *Toxicology* 2003](https://www.sciencedirect.com/science/article/abs/pii/S0041010103000357), and serum peptide/MALDI-TOF profiling has been explored as a murine diagnostic approach [Detection of Ricin Intoxication in Mice Using Serum Peptide Profiling by MALDI-TOF/MS, *PMC*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3497349/).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Route-dependent — lungs (inhalation), gastrointestinal tract (ingestion), skin/soft tissue at injection site (parenteral)
- **Organ level (secondary/systemic, all severe cases):** liver (hepatic necrosis/failure), kidney (acute tubular necrosis), spleen (necrosis, reported at autopsy), heart (myocyte necrosis, collagen deposition in mouse IM models), bone marrow (widespread damage documented in mouse IM studies)
- **Body systems:** respiratory, gastrointestinal, hepatic, renal, cardiovascular (via endothelial/coagulation injury), hematologic (thrombocytopenia, coagulopathy), immune (cytokine storm)
- **Tissue level:** alveolar epithelium and interstitium, intestinal mucosa (hemorrhagic necrosis), vascular endothelium/glycocalyx (a specific, mechanistically central tissue target), skeletal/cardiac muscle at injection sites
- **Subcellular level:** ribosome (60S large subunit, specifically the sarcin-ricin loop of 28S rRNA — GO Cellular Component: cytosolic large ribosomal subunit, GO:0022625), endoplasmic reticulum (site of A-chain translocation), Golgi/trans-Golgi network (retrograde transport waypoint), mitochondria (intrinsic apoptosis)
- **Localization:** generally systemic/bilateral once absorbed; injection-site findings are unilateral/localized initially before systemic spread

---

## 8. Temporal Development

### Onset
- **Acute onset** in all routes; this is not a congenital/developmental-onset condition
- Ingestion: symptom onset from as early as 15 minutes up to 20 hours post-exposure [WebSearch synthesis of case reports]
- Inhalation: symptoms typically within a few hours
- Injection: pain immediate at site; systemic symptoms (weakness, fever, vomiting) within 5–24 hours in the Markov case

### Progression
- **Rapid progression** pattern: mild, nonspecific prodromal GI or respiratory symptoms → hypovolemic/distributive shock → multi-organ failure → refractory cardiovascular collapse in severe/fatal cases [Medico-legal aspects of fatal ricin poisoning systematic review, *Int J Legal Med* 2026, PMID:42560523](https://link.springer.com/article/10.1007/s00414-026-03949-0)
- **Time to death** in severe, untreated exposure: typically 36–72 hours
- **No chronic/relapsing-remitting course** — the condition is monophasic: either resolves with supportive care within days, or progresses to death within roughly 3–5 days
- Long-term pulmonary sequelae (peribronchial/perivascular inflammation, mild fibrosis) can persist for weeks to months in inhalation-exposure survivors based on animal-model long-term follow-up [Scientific Reports 2024; Long-Term Pulmonary Damage in Surviving Antitoxin-Treated Mice, *Toxins* 2024](https://doi.org/10.3390/toxins16020103)

### Patterns
- No spontaneous remission pattern reported beyond simple resolution of acute intoxication with supportive care in survivors
- Critical intervention window: earliest possible decontamination/supportive care (within the first hour for GI decontamination) is repeatedly emphasized as the dominant modifiable prognostic factor

---

## 9. Inheritance and Population

### Epidemiology
- Ricin poisoning is **rare** as a clinical presentation; there is no formal population-based prevalence or incidence rate (cases per 100,000) reported in the literature, consistent with its status as an intentional/accidental toxin-exposure event rather than an endemic disease
- Multiple discrete, well-documented **bioterrorism/forensic incidents** in the US and UK from 1978–2013 constitute the bulk of "epidemiological" data: Georgi Markov (1978, fatal), Vladimir Kostov (1978, survived), Boris Korczak (1981), 2003/2004 White House/Senate mail incidents, 2013 letters to President Obama and others (James Everett Dutschke case, and the 2013 Spokane, WA mailings) [Wikipedia: List of incidents involving ricin](https://en.wikipedia.org/wiki/List_of_incidents_involving_ricin); [April 2013 ricin letters](https://en.wikipedia.org/wiki/April_2013_ricin_letters); [2003 ricin letters](https://en.wikipedia.org/wiki/2003_ricin_letters)
- The FBI has noted a possible increase in ricin-related copycat incidents attributed to the relative accessibility of extraction methods online [Seattle Times coverage of 2013 cases](https://www.seattletimes.com/nation-world/the-perfect-poison-ricin-used-in-3-recent-cases/)

### Inheritance Pattern
**Not applicable** — ricin poisoning is not a heritable Mendelian, X-linked, mitochondrial, or polygenic condition. There is no penetrance, expressivity, genetic anticipation, germline mosaicism, founder effect, consanguinity role, or carrier frequency to report, as this is an acquired toxic exposure.

### Population Demographics
- No specific ethnic/demographic predisposition documented (would be expected to track exposure opportunity rather than biological susceptibility)
- Castor bean cultivation and endemic accidental-exposure risk is geographically concentrated where *Ricinus communis* is grown commercially or ornamentally (tropical/subtropical regions for cultivation; globally for ornamental garden use)
- Age distribution: pediatric accidental ingestion cases (ornamental seed exposure) and adult intentional/forensic cases are the two dominant demographic clusters reported in case literature
- No consistent sex ratio has been established from the sparse case-report literature

---

## 10. Diagnostics

### Clinical/Laboratory Tests
- **Routine labs:** leukocytosis, electrolyte abnormalities, elevated liver enzymes/renal function markers, coagulation panel abnormalities (prolonged PT/APTT), thrombocytopenia [StatPearls NBK441948]
- **Imaging:** chest radiography (may be normal early, or show pulmonary edema/infiltrates/pneumonia pattern in inhalational exposure)
- **Histopathology (post-mortem or biopsy):** hemorrhagic necrosis of GI tract, hepatic injury, renal tubular necrosis, cerebral/pulmonary edema, hepatic steatosis — from the 2026 medico-legal systematic review of fatal cases [PMID:42560523](https://pubmed.ncbi.nlm.nih.gov/42560523/)

### Specific/Confirmatory Diagnostic Methods
- **Ricinine biomarker (urine/serum)**: Ricinine (3-cyano-4-methoxy-N-methyl-2-pyridone), a minor castor-bean alkaloid co-extracted with ricin, is measurable by **LC-MS/MS** (including dried urine/blood spot methods) as a biomarker of castor-bean-product exposure. Reported urine concentrations 12–41 hours post-intoxication: **20–58 ng/mL**, versus background population detection in only 1.2% of urine specimens (range 0.186–4.15 ng/mL) [Analysis of a Ricin Biomarker, Ricinine, in 989 Individual Human Urine Samples, PMID:23471955](https://pubmed.ncbi.nlm.nih.gov/23471955/); [Serial ricinine levels in serum and urine after ricin intoxication, PMID:23592744](https://pubmed.ncbi.nlm.nih.gov/23592744/). **Important limitation:** ricinine is a marker of castor-bean-product exposure, not of purified ricin — it "may be absent or present only in negligible amounts" in highly purified/criminal ricin preparations, so a negative ricinine result does not exclude purified-ricin poisoning.
- **Direct ricin detection**: LC-MS/MS-based rapid serum ricin identification methods [Rapid, Sensitive and Reliable Ricin Identification in Serum Samples Using LC–MS/MS, doi:10.3390/toxins13020079](https://doi.org/10.3390/toxins13020079); immunoassays (ELISA-type); ambient mass spectrometry two-tiered screening approaches [A Proof-of-Concept, Two-Tiered Approach for Ricin Detection Using Ambient Mass Spectrometry, PMID:35173958](https://pubmed.ncbi.nlm.nih.gov/35173958/)
- **Molecular/forensic depurination assay**: RT-PCR-based (reverse transcription-ligase-PCR) detection of the specific depurinated adenine signature left in 28S rRNA after ricin action, usable on biological samples as a functional/mechanistic confirmatory test rather than direct toxin immunodetection [Determination of ricin intoxication in biological samples by monitoring depurinated 28S rRNA, *Forensic Toxicology* 2018, doi:10.1007/s11419-017-0377-6](https://link.springer.com/article/10.1007/s11419-017-0377-6)
- **Nanopore direct RNA sequencing** to identify depurination events induced by ricin and other RIPs — an emerging research-grade method [bioRxiv 2021](https://www.biorxiv.org/content/10.1101/2021.08.13.456275.full.pdf)

### Genetic Testing
Not applicable — no genetic test is diagnostic for this acquired toxin exposure.

### Clinical Criteria / Epidemiologic Diagnostic Pattern
Per StatPearls, recognition often depends on **exposure-pattern epidemiology** rather than a single confirmatory bedside test: simultaneous presentation of multiple patients at one location with consistent symptoms (e.g., "sudden onset of respiratory distress among several people in one place") should raise suspicion for aerosolized/inhalational exposure; multi-patient GI-symptom clusters suggest ingestion exposure [StatPearls NBK441948](https://www.ncbi.nlm.nih.gov/books/NBK441948/).

### Differential Diagnosis
Cellulitis, pneumonia, sepsis, *Salmonella*/*Shigella* enteric infection, tularemia, Q fever, phosgene toxicity, staphylococcal enterotoxin B exposure, and myocardial infarction (for the shock/cardiovascular-collapse presentation) [StatPearls NBK441948].

### Veterinary diagnosis (comparative)
In livestock, diagnosis "is based primarily on exposure history, compatible clinical signs, and identification of castor bean plants or seeds within the environment," since "bloodwork results are usually not specific to ricin poisoning" [castor bean toxicosis review, various veterinary sources].

---

## 11. Outcome/Prognosis

### Survival and Mortality
- With prompt supportive care, **approximately 98% of people who ingest ricin survive**, reflecting the relatively high oral LD (1–20 mg/kg) and the buffering effect of intact seed coats limiting toxin release [WebSearch synthesis of clinical toxicology sources]
- **Very limited human outcome data exist for inhalation or injection routes**, given their rarity; these routes are associated with substantially lower LD (5–10 µg/kg inhalation) and historically higher lethality in documented forensic cases (e.g., Markov, fatal within days)
- **Severe/untreated exposure**: progression to fatality within **36–72 hours**, characterized by rapid evolution from nonspecific GI/respiratory prodrome to hypovolemic shock, multi-organ failure, and refractory cardiovascular collapse [Systematic review, *Int J Legal Med* 2026, PMID:42560523]

### Morbidity/Function
- Full recovery is typical in survivors of mild-to-moderate exposure managed supportively — e.g., a documented case of a 47-year-old woman who ingested six castor beans, received symptomatic treatment, and was "discharged home after a complete recovery three days later" [case report, *ScienceDirect*/PubMed synthesis]
- Long-term pulmonary impairment is a plausible but human-data-sparse concern for inhalation survivors, based on residual fibrotic/inflammatory changes documented in mouse models up to day 96 post-exposure

### Complications
Hypovolemic/distributive shock, disseminated coagulopathy and thrombocytopenia, capillary leak syndrome, hepatic and renal failure, hypoglycemia (model-organism evidence), and respiratory failure/ARDS-like picture in inhalation cases.

### Prognostic Factors
- **Dose and route of exposure** are the two dominant prognostic determinants
- **Time to initiation of supportive care** is repeatedly emphasized in clinical sources as the single most important modifiable survival factor ("the single most important factor in survival is how quickly someone gets to emergency care after exposure")
- No validated ricin-specific prognostic biomarker/severity score was identified in this search.

---

## 12. Treatment

### No Approved Antidote
**There is currently no FDA-approved antidote or specific antitoxin for human ricin poisoning.** Management is exclusively **supportive care**, and this is the single most important treatment-section fact to encode [StatPearls NBK441948; multiple corroborating sources].

### Supportive Care (by route) — suggested NCIT terms
| Intervention | Route context | Suggested NCIT |
|---|---|---|
| Gastric lavage (within ~1 hour of ingestion) | Ingestion | NCIT:C15329 (Surgical/procedural) or nearest procedure term — verify |
| Activated charcoal administration | Ingestion (after airway secured) | verify NCIT term |
| Fluid resuscitation / IV fluids | All routes | NCIT:C15986 Pharmacotherapy (supportive) |
| Vasopressor support for shock | All routes, severe | NCIT:C15986 Pharmacotherapy |
| Mechanical ventilation / respiratory support | Inhalation | verify device/procedure term |
| Wound/skin decontamination (soap and water) | Dermal/injection-site | NCIT:C15747 Supportive Care |
| Correction of electrolyte/coagulopathy abnormalities | All routes, severe | NCIT:C15747 Supportive Care |
| Seizure management | Severe systemic cases | NCIT:C15986 Pharmacotherapy |
| ICU admission and monitoring | All symptomatic suspected exposures | NCIT:C15747 Supportive Care |

"All symptomatic patients with suspected ricin exposure should be admitted" for monitoring [StatPearls NBK441948].

### Experimental / Investigational Countermeasures
- **Passive immunotherapy — anti-ricin monoclonal antibodies**: e.g., monoclonal antibody RicE5 conferred >90% survival in a murine model when given 6 hours post-intoxication, with 35% survival even at 24 hours post-exposure treatment; other monoclonal antibodies target isoforms D and E specifically [PMC 2024, *Toxins*](https://www.mdpi.com/2072-6651/16/10/412)
- **Active immunization / vaccines**:
  - **RiVax**: a recombinant RTA-based vaccine with two point mutations that genetically inactivate both the ribotoxic (N-glycosidase) active site and the vascular-leak-syndrome-inducing epitope; advanced through Phase 1A (dose-escalation, no adjuvant, 20/50/100 µg doses) and Phase 1B (alum-adjuvanted, safe/well-tolerated, improved neutralizing-antibody titers) human clinical trials [Pilot Phase IB Clinical Trial of an Alhydrogel-Adsorbed Recombinant Ricin Vaccine, *Clin Vaccine Immunol*, doi:10.1128/cvi.00381-12](https://journals.asm.org/doi/10.1128/cvi.00381-12); FDA granted Soligenix "Fast Track" designation for RiVax [Global Biodefense](https://globalbiodefense.com/newswire/fda-grants-soligenix-fast-track-designation-for-rivax-in-the-prevention-of-ricin-poisoning/)
  - **RVEc™**: another recombinant ricin-toxin vaccine candidate with reported Phase 1 safety/immunogenicity data [ScienceDirect, *Vaccine* 2015](https://www.sciencedirect.com/science/article/abs/pii/S0264410X15015509)
  - Thermostable lyophilized subunit vaccine formulations have been shown to elicit durable immunity in preclinical models [*PMC* 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8565519/)
  - Vaccine-induced serum antibody correlates of protection against aerosolized ricin have been profiled in rhesus macaques [*npj Vaccines* 2022](https://www.nature.com/articles/s41541-022-00582-x)
- **Small-molecule retrograde-transport inhibitors**: **Retro-2** blocks ricin's retrograde trafficking at the early-endosome/TGN interface by inhibiting ASNA1/TRC40-mediated ER-targeting of tail-anchored proteins; "rescued mice from lethal doses of ricin" and was "tolerated at high doses" in preclinical studies — "the first small molecule that shows efficacy against ricin in animal experiments" [*Cell* 2010](https://www.cell.com/fulltext/S0092-8674(10)00078-4); [*eLife* 2019](https://elifesciences.org/articles/48434). A related "novel small molecule retrograde transport blocker" has shown **post-exposure** protection in preclinical models [PMID:32140395](https://pubmed.ncbi.nlm.nih.gov/32140395/).
- **Immunomodulatory/anti-inflammatory approaches**: activation of the cholinergic anti-inflammatory pathway reduced ricin-induced mortality and organ failure in mice [*Molecular Medicine*, doi:10.2119/molmed.2008.00105](https://link.springer.com/article/10.2119/molmed.2008.00105); small molecules suppressing ricin-induced SAPK stress signaling have been identified in screens [*PLOS ONE*](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0049075)
- **Post-exposure antitoxin in large-animal models**: post-exposure anti-ricin treatment protected swine against lethal systemic and pulmonary exposures [*PMC* 2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7354453/)

### Treatment Strategy Notes for Curation
For a dismech `Treatment` entry, the mainstay entry should be `treatment_term: NCIT:C15747 Supportive Care` (verify exact NCIT code via OAK) with `description` covering airway/fluid/electrolyte management, and a **separate** experimental-treatment cluster for RiVax (`therapeutic_modality: VACCINE`) and anti-ricin monoclonal antibodies (`therapeutic_modality: MONOCLONAL_ANTIBODY`), each carrying its own PMID evidence and clearly marked as investigational/not FDA-approved.

---

## 13. Prevention

### Primary Prevention
- **Occupational controls**: PPE and engineering controls in castor-oil processing facilities to limit dust/mash exposure (OSHA hazard guidance exists: [OSHA Ricin Hazard Recognition](https://www.osha.gov/ricin/hazards))
- **Restriction of access to purified ricin**: Schedule 1 Chemical Weapons Convention controls and CDC Select Agent Program registration requirements for laboratories handling ricin toxin
- **Public/consumer safety**: awareness messaging about ornamental castor bean plant seed toxicity, particularly for households with young children
- **Active immunization** (RiVax/RVEc) is being developed specifically as a **pre-exposure primary-prevention** countermeasure for at-risk populations (military personnel, laboratory workers), not yet in general public use

### Secondary Prevention / Early Detection
- Rapid clinical recognition using the exposure-pattern heuristics above (clustered presentations)
- Rapid decontamination protocols: GI decontamination (gastric lavage/activated charcoal) within the first hour of suspected ingestion; skin decontamination with soap and water for dermal exposure
- Forensic/public-health mail-screening programs (developed in response to the 2003/2013 mail incidents) for early interception of intentional exposures

### Tertiary Prevention
Aggressive ICU-level supportive care to prevent progression to multi-organ failure once poisoning is confirmed or strongly suspected.

### Genetic Counseling / Screening
Not applicable — no heritable component to counsel on.

### Public Health / Biodefense
Ricin's CDC Category B and CWC Schedule 1 status drive a public-health/biodefense prevention framework (select-agent regulation, law-enforcement interdiction, mail-screening infrastructure) distinct from the individual clinical-prevention measures above.

---

## 14. Other Species / Natural Disease

### Taxonomy
- Source organism: ***Ricinus communis*** L. (NCBITaxon:3988), family Euphorbiaceae
- Affected species: broadly mammalian (and likely other vertebrate) susceptibility, given the conserved eukaryotic ribosomal sarcin-ricin loop target

### Natural/Accidental Veterinary Disease
Castor bean toxicosis is a well-documented **naturally occurring accidental poisoning in livestock and companion animals**:

- **Relative species susceptibility**: "Horses are the most susceptible of the farm animals; sheep, cattle and pigs are intermediate; and poultry are the most resistant" [Mad Barn veterinary summary; academic castor-bean-toxicosis reviews]
- **Toxic dose thresholds**: seeds ingested at ~0.2% of body weight caused toxicosis in cattle; ~0.01% of body weight was toxic in horses
- **Onset/course**: clinical signs appear 6–30 hours after seed ingestion; clinical evolution to death ranges from 4–56 hours across species
- **Clinical signs**: predominantly gastrointestinal — diarrhea, vomiting, and colic (notably prominent in horses) — mirroring the human ingestion phenotype
- **Mechanistic prerequisite**: "chewing of the beans is vital in releasing the ricin, as the seed coat is very hard and the seed will pass harmlessly through the digestive tract unless the seed coat is broken" — the same intact-seed-coat protective mechanism documented in human cases
- Documented case reports/series: castor bean toxicosis in a sheep flock [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S004101010600403X); accidental poisoning by castor bean cake in horses in Brazil [SciELO](https://www.scielo.br/j/pvb/a/XwzKzyyw97sqWQj9Ch6n3Br/?lang=en)

### Comparative Biology
The core molecular mechanism (RTA-mediated depurination of the conserved sarcin-ricin loop) is expected to be conserved across all eukaryotic species studied, since the SRL is a near-universally conserved rRNA element — this underlies both the broad mammalian veterinary susceptibility pattern and the utility of non-mammalian/cell-based systems (including yeast, *Saccharomyces cerevisiae*) for mechanistic dissection [Ribosome Depurination Is Not Sufficient for Ricin-Mediated Cell Death in *Saccharomyces cerevisiae*, *PMC*](https://pmc.ncbi.nlm.nih.gov/articles/PMC1828414/) — notably, this yeast study demonstrates that depurination alone is *not sufficient* for ricin-mediated cell death, implying additional downstream cytotoxic mechanisms beyond simple translational arrest, an important nuance for the mechanism-chain description above.

### Transmission / Zoonotic Potential
Not applicable — ricin poisoning is a direct toxin exposure, not a transmissible infectious disease; there is no zoonotic transmission concept relevant here, only shared plant-source exposure risk across species.

---

## 15. Model Organisms

### Mouse Models
- **Intranasal instillation**: LD50 in rodents 3.5–4.8 µg/kg
- **Aerosolized inhalation**: LD50 in mice 10–20 µg/kg (higher than intranasal instillation, attributed to nasal turbinate filtering of inhaled aerosol particles) [Comparative Aspects of Ricin Toxicity by Inhalation, *Toxins* 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10145923/)
- **Intramuscular/parenteral models**: demonstrate widespread damage to heart, spleen, and bone marrow, with diffuse hemorrhages, myocyte necrosis, collagen deposition, coagulopathy, and severe thrombocytopenia — closely recapitulating human injection-route pathology [*Toxins* 2019, PMID:31208156](https://pubmed.ncbi.nlm.nih.gov/31208156/)
- **Pulmonary/inhalation models**: recapitulate acute interstitial pneumonia, neutrophilic infiltration, pro-inflammatory cytokine response, and alveolar epithelial cell death (days 1–7), with residual inflammatory/fibrotic changes at days 21–96, closely tracking presumed human inhalation-injury biology (fidelity: **HIGH** to **MODERATE** for acute-phase pulmonary injury; long-term fibrosis correlation to humans is **UNCONFIRMED** due to sparse human inhalation-survivor data) [*Scientific Reports* 2024](https://www.nature.com/articles/s41598-024-62222-9)
- **Hypoglycemia model**: parenteral mouse exposure reveals a cytokine-mediated hepatic glucose-6-phosphatase suppression mechanism not yet confirmed in human cases — a clear candidate for `HUMAN_MODEL_MISMATCH`/translational-uncertainty flagging if curated [PMC:9786807](https://pmc.ncbi.nlm.nih.gov/articles/PMC9786807/)
- **Antitoxin/vaccine efficacy models**: RiVax, RVEc, monoclonal antibody (RicE5 and others), and Retro-2 efficacy have all been established primarily in mouse lethal-challenge models, with confirmatory work extending to **rhesus macaques** (vaccine correlate-of-protection studies) and **swine** (post-exposure antitoxin efficacy for both systemic and pulmonary exposure, and endothelial glycocalyx/microvascular-flow pathology) [*npj Vaccines* 2022](https://www.nature.com/articles/s41541-022-00582-x); [*PMC* 2020 swine antitoxin](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7354453/); [*PMC* 2021 swine glycocalyx](https://pmc.ncbi.nlm.nih.gov/articles/PMC8618821/)

### Cellular/Genetic Screening Models
- Genome-wide mammalian cell (haploid/CRISPR) genetic-interaction screens have identified ~200 sensitizing/protective host factors, clustering in retrograde transport, ribosome biogenesis, and cholesterol biosynthesis pathways — providing a systems-level map of cellular ricin susceptibility determinants usable for mechanistic annotation [*Cell* 2013](https://www.cell.com/fulltext/S0092-8674(13)00082-2)
- Yeast (*S. cerevisiae*) models have been used to dissect depurination-vs-cytotoxicity relationships, showing depurination is necessary but not sufficient for cell death [*PMC*, PMID search](https://pmc.ncbi.nlm.nih.gov/articles/PMC1828414/)

### Model Limitations
- Nasal-anatomy differences between rodents and humans (turbinate filtering) complicate direct LD50 extrapolation for inhalation exposure
- Most severe systemic pathophysiology data (coagulopathy, glycocalyx shedding, cytokine storm kinetics) derive from **parenteral (IM/IV)** rodent/swine models rather than the clinically more common ingestion route in humans — a route-mismatch worth flagging in any model-to-mechanism link (`model_scale`/`divergences` per dismech's `ModelMechanismLink` conventions)
- No engineered genetic (knockout/transgenic) mouse model of "ricin poisoning" exists in the conventional sense, since this is an induced-exposure rather than genetic model; genetic screens instead identify modifier genes in cultured cells

### Resources
No dedicated ricin-poisoning model repository/database catalog (comparable to IMPC/MGI for genetic disease models) was identified — model access is via individual published studies (MGI/RGD apply only incidentally, for strain-background documentation of the mice used in the cited studies).

---

## Summary of Curation-Relevant Gaps and Cautions

1. **No confirmed CHEBI or NCIT CURIE for ricin** was extracted from this search — these must be looked up directly via OAK/ChEBI before binding, per dismech's ontology-term contract.
2. **ASGR1-specific ricin hepatocyte-entry claim is unconfirmed** — do not curate this link without a direct primary citation; ricin's B-chain lectin binding is generally described as broadly galactose/GalNAc-receptor-promiscuous rather than ASGR1-specific in the sources found.
3. Most severe-pathophysiology mechanistic detail (hypoglycemia, glycocalyx shedding, cytokine kinetics, coagulopathy) is **MODEL_ORGANISM evidence** (mouse/swine), not confirmed in human case series — grade `evidence_source` accordingly and consider `HUMAN_MODEL_MISMATCH` discussion entries where translational fidelity to human ricin poisoning is untested.
4. HPO term suggestions above are **illustrative and unverified** — every HP CURIE must be confirmed via OAK lookup (`just validate-terms`) before use; several suggested terms are marked "(verify exact term)" because exact-match searches were not run against the live HPO in this session.
5. This is fundamentally a **toxicology/environmental** entry with minimal true "genetic" content — Sections 4/9 genetic subsections are appropriately sparse and should not be padded to fit a template designed primarily for Mendelian disease.

---

### Sources
- [Determination of ricin intoxication in biological samples by monitoring depurinated 28S rRNA (Forensic Toxicology, 2018)](https://link.springer.com/article/10.1007/s11419-017-0377-6)
- [Using Oxford Nanopore Technology direct RNA sequencing to identify depurination events (bioRxiv, 2021)](https://www.biorxiv.org/content/10.1101/2021.08.13.456275.full.pdf)
- [Ribosome Depurination Is Not Sufficient for Ricin-Mediated Cell Death in *S. cerevisiae* (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1828414/)
- [Structures and Ribosomal Interaction of Ribosome-Inactivating Proteins (PMC, 2018)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6273143/)
- [Ricin Toxicity — StatPearls (NCBI Bookshelf)](https://www.ncbi.nlm.nih.gov/books/NBK441948/)
- [Medical Countermeasures against Ricin Intoxication (Toxins, 2023)](https://doi.org/10.3390/toxins15020100)
- [Fine-Specificity Epitope Analysis Identifies Contact Points on Ricin Toxin (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6372112/)
- [Intracellular Transport and Cytotoxicity of the Protein Toxin Ricin (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6628406/)
- [ricin poisoning — National Organization for Rare Disorders](https://rarediseases.org/mondo-disease/ricin-poisoning/)
- [Ricin intoxication by lethal dose of castor seeds ingestion: a case report (PMC, 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11363666/)
- [Intentional ricin intoxication: A case report and review of the literature](https://www.jclinmedcasereports.com/articles/OJCMCR-1966.html)
- [Analysis of a Ricin Biomarker, Ricinine, in 989 Individual Human Urine Samples — PubMed (PMID:23471955)](https://pubmed.ncbi.nlm.nih.gov/23471955/)
- [Serial ricinine levels in serum and urine after ricin intoxication — PubMed (PMID:23592744)](https://pubmed.ncbi.nlm.nih.gov/23592744/)
- [Medico-legal aspects of fatal ricin poisoning: a systematic review (Int J Legal Med, 2026, PMID:42560523)](https://link.springer.com/article/10.1007/s00414-026-03949-0)
- [Rapid, Sensitive and Reliable Ricin Identification in Serum Samples Using LC–MS/MS (Toxins, 2021)](https://doi.org/10.3390/toxins13020079)
- [A Proof-of-Concept, Two-Tiered Approach for Ricin Detection Using Ambient Mass Spectrometry — PubMed (PMID:35173958)](https://pubmed.ncbi.nlm.nih.gov/35173958/)
- [Post-Exposure Anti-Ricin Treatment Protects Swine against Lethal Systemic and Pulmonary Exposures (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7354453/)
- [Ricin A-Chain requires JNK to induce apoptosis (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2783365/)
- [Identification of Small Molecules That Suppress Ricin-Induced Stress-Activated Signaling Pathways (PLOS ONE / PMC)](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0049075)
- [Role of Apoptotic Signaling Pathways in Regulation of Inflammatory Responses to Ricin in Primary Murine Macrophages (PMC)](https://ncbi.nlm.nih.gov/pmc/articles/PMC1880874)
- [Intramuscular Ricin Poisoning of Mice Leads to Widespread Damage in the Heart, Spleen, and Bone Marrow (Toxins, 2019, PMID:31208156)](https://pubmed.ncbi.nlm.nih.gov/31208156/)
- [Intramuscular Exposure to a Lethal Dose of Ricin Toxin Leads to Endothelial Glycocalyx Shedding and Microvascular Flow Abnormality in Mice and Swine (PMC, 2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8618821/)
- [Georgi Markov — Wikipedia](https://en.wikipedia.org/wiki/Georgi_Markov)
- [Ricin and the Assassination of Georgi Markov (ResearchGate)](https://www.researchgate.net/publication/23781130_Ricin_and_the_Assassination_of_Georgi_Markov)
- [Pilot Phase IB Clinical Trial of an Alhydrogel-Adsorbed Recombinant Ricin Vaccine (Clin Vaccine Immunol)](https://journals.asm.org/doi/10.1128/cvi.00381-12)
- [A Monoclonal Antibody with a High Affinity for Ricin Isoforms D and E (Toxins, 2024)](https://www.mdpi.com/2072-6651/16/10/412)
- [Safety and immunogenicity of ricin vaccine, RVEc™, in a Phase 1 clinical trial (Vaccine, 2015)](https://www.sciencedirect.com/science/article/abs/pii/S0264410X15015509)
- [Durable Immunity to Ricin Toxin Elicited by a Thermostable, Lyophilized Subunit Vaccine (PMC, 2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8565519/)
- [Serum antibody profiling identifies vaccine-induced correlates of protection against aerosolized ricin toxin in rhesus macaques (npj Vaccines, 2022)](https://www.nature.com/articles/s41541-022-00582-x)
- [Short- and long-term outcomes of pulmonary exposure to a sublethal dose of ricin in mice (Scientific Reports, 2024)](https://www.nature.com/articles/s41598-024-62222-9)
- [Comparative Aspects of Ricin Toxicity by Inhalation (Toxins, 2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10145923/)
- [Csf2ra deletion attenuates acute lung injuries induced by intratracheal inoculation of aerosolized ricin in mice (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9531258/)
- [Long-Term Pulmonary Damage in Surviving Antitoxin-Treated Mice following a Lethal Ricin Intoxication (Toxins, 2024)](https://doi.org/10.3390/toxins16020103)
- [Pulmonary gene expression profiling of inhaled ricin (Toxicology, 2003)](https://www.sciencedirect.com/science/article/abs/pii/S0041010103000357)
- [Parenteral Exposure of Mice to Ricin Toxin Induces Fatal Hypoglycemia by Cytokine-Mediated Suppression of Hepatic Glucose-6-Phosphatase Expression (PMC, 2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9786807/)
- [Activation of the Cholinergic Antiinflammatory Pathway Reduces Ricin-Induced Mortality and Organ Failure in Mice (Molecular Medicine)](https://link.springer.com/article/10.2119/molmed.2008.00105)
- [A Systematic Mammalian Genetic Interaction Map Reveals Pathways Underlying Ricin Susceptibility (Cell, 2013)](https://www.cell.com/fulltext/S0092-8674(13)00082-2)
- [A vital sugar code for ricin toxicity (Cell Research, 2017)](https://www.nature.com/articles/cr2017116)
- [Retro-2 protects cells from ricin toxicity by inhibiting ASNA1-mediated ER targeting (eLife, 2019)](https://elifesciences.org/articles/48434)
- [Inhibition of Retrograde Transport Protects Mice from Lethal Ricin Challenge (Cell, 2010)](https://www.cell.com/fulltext/S0092-8674(10)00078-4)
- [Novel small molecule retrograde transport blocker confers post-exposure protection against ricin intoxication — PubMed (PMID:32140395)](https://pubmed.ncbi.nlm.nih.gov/32140395/)
- [Dislocation of Ricin Toxin A Chains in Human Cells Utilizes Selective Cellular Factors (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3122183/)
- [Ricin transport into cells: studies of endocytosis and intracellular transport — PubMed (PMID:11111920)](https://pubmed.ncbi.nlm.nih.gov/11111920/)
- [Castor bean (Ricinus communis) toxicosis in a sheep flock (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S004101010600403X)
- [Accidental poisoning by castor bean cake in horses (SciELO)](https://www.scielo.br/j/pvb/a/XwzKzyyw97sqWQj9Ch6n3Br/?lang=en)
- [Castor Bean (Ricin) Toxicosis in Horses (Mad Barn)](https://madbarn.com/castor-bean-poisoning-in-horses/)
- [List of incidents involving ricin — Wikipedia](https://en.wikipedia.org/wiki/List_of_incidents_involving_ricin)
- [April 2013 ricin letters — Wikipedia](https://en.wikipedia.org/wiki/April_2013_ricin_letters)
- [2003 ricin letters — Wikipedia](https://en.wikipedia.org/wiki/2003_ricin_letters)
- [FBI: Manhattan U.S. Attorney and FBI Assistant Director Announce Arrest of New York Man for Attempting to Acquire Deadly Toxin, Ricin](https://www.fbi.gov/contact-us/field-offices/newyork/news/press-releases/manhattan-u.s.-attorney-and-fbi-assistant-director-announce-arrest-of-new-york-man-for-attempting-to-acquire-deadly-toxin-ricin)
- [Ricin: Technical Background and Potential Role in Terrorism (EveryCRSReport.com)](https://www.everycrsreport.com/reports/RS21383.html)
- [Ricin — Hazard Recognition (OSHA)](https://www.osha.gov/ricin/hazards)
- [Ricin | Chemical Emergencies (CDC)](https://www.cdc.gov/chemical-emergencies/chemical-fact-sheets/ricin.html)
- [ICD-10-CM Diagnosis Code T62.2X1A (ICD List)](https://icdlist.com/icd-10/T62.2X1A)
- [Ricin Poisoning — MalaCards](https://www.malacards.org/card/ricin_poisoning)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 31 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 8 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000975` (1 mention) - the report calls it "verify"; HP calls it **Hyperhidrosis**
- `HP:0006515` (1 mention) - the report calls it "verify"; HP calls it **Interstitial pneumonitis**
- `HP:0001626` (1 mention) - the report calls it "cardiac"; HP calls it **Abnormality of the cardiovascular system**
- `CL:0000584` (1 mention) - the report calls it "Enterocytes / intestinal epithelial cells"; CL calls it **enterocyte**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0030433` (obsolete ubiquitin-dependent ERAD pathway) (1 mention) - replaced by `GO:0036503`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C15329` (1 mention) - the report calls it "Surgical/procedural"; NCIT calls it **Surgical Procedure**