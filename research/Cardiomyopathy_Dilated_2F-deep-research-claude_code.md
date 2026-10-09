---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-08T14:29:08.064756'
end_time: '2026-10-08T14:34:18.049153'
duration_seconds: 309.98
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cardiomyopathy Dilated 2F
  mondo_id: MONDO:0030680
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
  - claude-opus-5-5
  web_search_requests: 9
  num_turns: 33
  total_cost_usd: 2.470265900000001
  session_id: a4211faa-84ac-4a83-a085-7d0e2be1ca89
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 4
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 17
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 34
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: DOID:0081162
    reported_labels:
    - DOID
    ontology_label: dilated cardiomyopathy 2F
  labels_variant: 2
  unresolvable_prefixes:
  - OMIM
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cardiomyopathy Dilated 2F
- **MONDO ID:** MONDO:0030680 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cardiomyopathy Dilated 2F** covering all of the
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

Let me fetch the primary abstracts for exact quotes and PMIDs.

I'm pulling the BAG5/CMD2F primary papers into the reference cache so the report can quote their exact wording. Next I'll read them.

Reading the cached Gupta 2016 paper and confirming the BAG5–Hsp70 structural paper; the report comes after that.

# Cardiomyopathy, Dilated, 2F (CMD2F; BAG5-related autosomal recessive dilated cardiomyopathy): research report

*Prepared 2026-10-08 for the dismech entry `kb/disorders/Cardiomyopathy_Dilated_2F.yaml`. Quotes marked "verbatim" are copied from cached abstracts or full texts in `references_cache/`. Ontology terms marked ✔ were checked against the local `cache/<prefix>/terms.csv` label caches. Those caches confirm that a CURIE exists and has that label. They do not confirm membership in a dynamic enum.*

---

## Summary

CMD2F is a rare, early-onset, severe dilated cardiomyopathy. It is caused by **biallelic loss-of-function (truncating) variants in *BAG5*** (hgnc:941 ✔). *BAG5* encodes a five-BAG-domain co-chaperone that acts as a **nucleotide exchange factor for HSC70/Hsp70**. Patients present in the teens or twenties with severe systolic dysfunction and refractory ventricular arrhythmias. Many progress to an LVAD or heart transplantation.

Two mechanisms have been proposed, both from mouse work:
- **Junctional membrane complex and calcium-handling failure under catecholamine stress** (Hakui 2022).
- **An impaired cardiomyocyte ER-stress response leading to apoptosis** (Wongong 2024; Gupta 2016).

AAV9-*BAG5* gene replacement rescued the knock-in mouse phenotype. About 12 cases from roughly 7 families have been published, so the evidence base is small.

---

## 1. Disease information

| Field | Value | Source / status |
|---|---|---|
| MONDO | MONDO:0030680 "cardiomyopathy, dilated, 2F" ✔ | local MONDO cache |
| OMIM phenotype | 619747 (CMD2F) | secondary sources ([MGI disease page](https://informatics.jax.org/disease/OMIM:619747), [DrugMap](https://drugmap.idrblab.net/data/disease/details/DIS6YW38)); confirm on OMIM |
| OMIM gene | 603885 (*BAG5*) | [PanelApp Australia](https://panelapp-aus.org/panels/95/gene/BAG5/) via search snippet; confirm |
| DOID | DOID:0081162 | [Disease Ontology](https://disease-ontology.org/term/DOID:0081162) |
| Orphanet | No disease-specific ORPHA code found | Probably sits under familial isolated DCM; not verified |
| ICD-10-CM / ICD-11 | No specific code. Generic DCM codes apply (ICD-10 I42.0) | — |
| Synonyms | CMD2F; BAG5-related dilated cardiomyopathy; autosomal recessive DCM due to BAG5 deficiency | — |
| Gene locus | 14q32 (per DOID) | — |

All information comes from aggregated case reports and family studies. There is no EHR- or registry-level data.

**Grouping context:** CMD2F belongs to the recessive "CMD2" series (2A *TNNI3*, 2B *GATAD1*, 2C *PPCS*, 2D *RPL3L*, …), and to the BAG family of cardiomyopathy genes alongside *BAG3* (autosomal dominant CMD1HH). The 2026 ClinGen DCM reassessment lists BAG5 among nine newly assessed genes classified as **high evidence** (PMID:42708185):

> "Nine newly assessed genes were classified as high evidence: BAG5, FLII, LMOD2, MYLK3, MYZAP, NRAP, PPA2, PPP1R13L, and RPL3L. Twelve genes (11 newly appraised) were rated as high evidence with an autosomal recessive (AR) MOI." (verbatim)

---

## 2. Etiology

**Primary cause:** biallelic germline truncating *BAG5* variants (PMID:35044787):

> "we identified that homozygous truncating mutations in the gene encoding Bcl-2–associated athanogene (BAG) co-chaperone 5 (BAG5) caused inherited DCM in five patients among four unrelated families with complete penetrance." (verbatim)

**Genetic risk factors**
- **Biallelic truncation** is the cause: homozygous, or compound heterozygous as in Inoue 2023 (PMID:37873655).
- **Heterozygous truncation** may predispose to **tachycardia-induced cardiomyopathy**, but this has not been established. PMID:35044787 reports:

  > "We also identified heterozygous truncating mutations in three patients with tachycardia-induced cardiomyopathy, a reversible DCM subtype associated with abnormal calcium homeostasis." (verbatim)

  This is a separate, susceptibility-level claim. Do not fold it into the CMD2F inheritance block.
- **Heterozygous carriers** were clinically unaffected in Hakui 2022. In Wongong 2024, two of three female heterozygous relatives had mild or borderline ECG abnormalities (PMID:38796549):

  > "suggesting a potential predisposition to arrhythmia in female carriers of the BAG5 variant." (verbatim)

**Environmental and stress modifiers.** These are inferred from mouse models only:
- **Catecholamine (β-adrenergic) stimulation** unmasked dilatation, arrhythmia and death in *Bag5* knock-in mice (PMID:35044787).
- **ER stress** (tunicamycin) was required to reveal systolic dysfunction in a second knock-in line (PMID:38796549):

  > "To develop DCM in Bag5 point mutant KI mice, ER stress is required." (verbatim; full-text Discussion)

  The equivalent human triggers have not been identified. Tachyarrhythmia, adrenergic surges and intercurrent illness are plausible candidates but unproven.

**Protective factors and gene-environment interactions:** none reported in humans. The mouse data suggest a gene × adrenergic/ER-stress interaction, which is a hypothesis.

---

## 3. Phenotypes

| Phenotype | HPO (✔ = cache-verified) | Onset / frequency | Key evidence |
|---|---|---|---|
| Dilated cardiomyopathy | HP:0001644 ✔ | Second decade in 4 of 5, age 34 in 1 (Hakui cohort, per PanelApp); ages 12–17 in Wongong family; 100% of biallelic cases | PMID:35044787; PMID:38796549 |
| Reduced LVEF | HP:0012664 ✔ | All. LVEF 36–46% in the Thai/Middle Eastern sibship; "severely reduced" in the Japanese cases | PMID:38796549 (verbatim: "definite DCM with left ventricular ejection fraction (LVEF) by echocardiography of 40% and 36%, respectively") |
| Left ventricular dilatation | Use DCM term, or check "Left ventricular dilatation" in HPO | Proband LVEDD 5.8 cm, Z +4.8 | PMID:38796549 |
| Ventricular arrhythmia (refractory VT/VF) | HP:0004308 ✔ / HP:0004756 ✔ / HP:0001663 ✔ | Frequent, a defining feature | PMID:36130910 (Hakui 2022 Circ J case; no abstract cached); PMID:37873655 |
| Congestive heart failure, advanced | HP:0001635 ✔ | All Japanese cases needed an LVAD; at least one was transplanted | PMID:35044787 title; PanelApp |
| Sudden cardiac death / death awaiting transplant | HP:0001645 ✔ | One sibling died at 12 years awaiting transplant | PMID:38796549 (verbatim: "III-6 passed away at the age of 12 years old while waiting for a heart transplantation.") |
| ECG abnormalities (low limb-lead voltage, inferolateral T-wave inversion, poor R progression) | HP:0003115 Abnormal EKG ✔ (more specific HPO terms should be looked up) | 3 of 3 affected siblings | PMID:38796549 (verbatim: "all available patients, III-2, III-4, and III-5 had a low voltage of the limb lead, T wave inversion in the infero-lateral leads, and poor R progression in precordial leads") |
| Elevated BNP | Laboratory finding. LOINC BNP / NT-proBNP; HPO term to look up | Reported in the Japanese cases | PanelApp summary (secondary) |

- **Severity:** severe and progressive. Wongong 2024 describes "consistently severe manifestations of the disease."
- **Quality of life:** no formal measures have been published. The burden is that of NYHA III–IV heart failure in adolescents and young adults, including an LVAD and/or transplant, an ICD and recurrent shocks.
- **Extracardiac features:** none reported. Note that *Bag5*-null male mice are infertile (IMPC), but human fertility has not been studied.

---

## 4. Genetic and molecular information

**Gene:** *BAG5* (BCL2-associated athanogene 5), hgnc:941 ✔, chromosome 14q32. RefSeq used by Wongong: NM_001015049.2.

**Reported pathogenic alleles.** Variant list per Wongong 2024 discussion (PMID:38796549, verbatim: "c.589C > T (p.Arg197Ter), c.1168C > T (p.Arg390Ter) and c.18dupA (p.His7ThrTer5)"):

| Variant | Type | Zygosity / families | Source |
|---|---|---|---|
| c.589C>T, p.Arg197Ter | Nonsense | Homozygous (Hakui 2022); compound heterozygous with p.Arg390Ter (Inoue 2023) | PMID:35044787; PMID:37873655 |
| c.1168C>T, p.Arg390Ter | Nonsense | Homozygous (Hakui 2022); compound heterozygous (Inoue 2023) | same |
| c.18dupA, p.His7ThrfsTer5 | Frameshift | Homozygous (Hakui 2022) | PMID:35044787 |
| c.444_445delGA, p.Lys149AsnfsTer6 | Frameshift | Homozygous, 3 siblings, consanguineous Middle Eastern family; ClinVar VCV003918808.1 | PMID:38796549 |

**Caveats on this table**
- Wongong describes the Hakui variants as "de novo homozygous". That wording is almost certainly inaccurate, because homozygosity implies inheritance. Do not copy it.
- The Inoue 2023 variant assignments come from Wongong's summary. The Inoue abstract could not be retrieved (`PMID_37873655.md` is cached as `content_type: unavailable`).

**Other gene-level facts**
- **ACMG/ClinGen:** ClinGen Gene-Disease Validity, *BAG5*–dilated cardiomyopathy (MONDO:0005021), **AR, Moderate**, DCM GCEP, 2024-06-14 (cached `CGGV:assertion_97fe83b7-…-2024-06-14T160000.000Z`). Quotable row: `BAG5 | HGNC:941 | dilated cardiomyopathy | MONDO:0005021 | AR | Moderate`.
  - The assertion is for the broader DCM term, not MONDO:0030680. Under the repository's *Gene-Disease Validity Is Copied, Never Assigned* rule, check whether it counts as "this entry's disease" before recording it in `gene_disease_validity`.
  - GenCC also lists a Moderate AR submission. PanelApp Australia rates *BAG5* Green.
- **Variant class / functional consequence:** all reported alleles are truncating. The proposed mechanism is loss of function. Hakui showed reduced protein; Wongong found Bag5 protein "completely absent" in knock-in hearts. Inoue reported reduced BAG5 and SERCA2 immunostaining in patient myocardium, per Wongong's summary. Suggested slot value: `functional_impact_category: LOSS_OF_FUNCTION`.
- **Origin:** germline.
- **Allele frequency:** not systematically reported. Wongong filtered at <1% in gnomAD and 1000 Genomes. Check gnomAD for p.Arg197Ter and p.Arg390Ter, because recurrence in Japanese families raises the possibility of a founder allele. This is unverified.
- **Modifier genes, epigenetics, chromosomal abnormalities:** none reported.
- **Lesurf 2022** (npj Genomic Medicine 7:18, a whole-genome sequencing study of early-onset cardiomyopathy) is listed by GenCC as a BAG5 evidence source. Its BAG5-specific finding was not verified.

---

## 5. Environmental information

There is no environmental, lifestyle or infectious cause. The only "exposures" with data are experimental stressors in mice: isoproterenol/catecholamine and tunicamycin. These belong in `animal_models` or `experimental_models`, not in `environmental:`.

---

## 6. Mechanism and pathophysiology

### Causal chain

1. **Biallelic truncating *BAG5* variants** lead to **loss of BAG5 protein** through nonsense-mediated decay or truncation. This is demonstrated in knock-in mouse hearts and inferred from reduced immunostaining in patient tissue.
2. **Loss of BAG5** leads to **loss of nucleotide-exchange activity on HSC70/Hsp70**, so ADP release slows and chaperone-mediated folding is less efficient. The biochemistry is demonstrated in vitro (Arakawa 2010, PMID:20223214; PMID:35044787: "BAG5 acts as a nucleotide exchange factor for heat shock cognate 71 kDa protein (HSC70), promoting adenosine diphosphate release and activating HSC70-mediated protein folding"). That this is the operative cardiac lesion is inferred.
3. The pathway then branches:
   - **3a. JMC/calcium branch** (Hakui 2022, mouse plus cardiomyocytes). Under catecholamine stimulation, BAG5 deficiency leads to **reduced abundance of functional junctional membrane complex (JMC) proteins and disrupted JMC structure**, which results in **abnormal Ca²⁺ handling**. PMID:35044787 (verbatim): "BAG5 localized to junctional membrane complexes (JMCs), critical microdomains for calcium handling. Bag5-mutant mouse cardiomyocytes exhibited decreased abundance of functional JMC proteins under catecholamine stimulation, disrupted JMC structure, and calcium handling abnormalities."
     - The specific JMC proteins named in the full text (e.g., JPH2, RyR2, LTCC) were not verified from the abstract.
     - Human support for this branch is reduced SERCA2 in patient myocardium (Inoue 2023, as reported secondhand by Wongong).
   - **3b. ER-stress branch** (Wongong 2024; Gupta 2016). During ER stress, BAG5 normally stabilises GRP78 (HSPA5) and limits CHOP-mediated apoptosis (in vitro, rat cardiomyocytes). PMID:26729625 (verbatim): "Bag5 protein expression is significantly increased in the ER during ER stress and that this in turn modulates GRP78 protein stability and reduces ER stress." Without BAG5, ER stress leads to **excess cardiomyocyte apoptosis** (TUNEL in knock-in mice, n = 1 per genotype). PMID:38796549 (verbatim): "Their cardiac tissues exhibited a notable increase in apoptotic cells, despite non-distinctive changes in CHOP and GRP78 levels." The CHOP-independent result means the downstream effector is unresolved. The authors suggest ATF6 or XBP1, which is speculation.
4. **Ca²⁺ mishandling** leads to **triggered and re-entrant ventricular arrhythmias** (mouse arrhythmogenicity under catecholamine stress; refractory VT/VF in patients). It also contributes to **contractile dysfunction**.
5. **Cardiomyocyte loss and contractile failure** lead to **LV dilatation and systolic dysfunction (DCM)**, then **advanced heart failure** (LVAD or transplant), and **sudden death**. The step from 3a/3b to DCM is shown in mice under stress. In humans it is inferred.

**Which steps are upstream:** steps 1–2 are upstream and certain. Branch 3a has the stronger evidence: a rescue experiment plus the arrhythmia phenotype. Branch 3b rests on small-n data. The two branches are not mutually exclusive.

### Suggested annotations (✔ cache-verified)

| Category | Terms |
|---|---|
| Molecular function | GO:0000774 adenyl-nucleotide exchange factor activity ✔ |
| Biological processes | GO:0006457 protein folding ✔; GO:0034976 response to endoplasmic reticulum stress ✔; GO:0030968 endoplasmic reticulum unfolded protein response ✔; GO:0070059 intrinsic apoptotic signaling pathway in response to endoplasmic reticulum stress ✔; GO:0006874 intracellular calcium ion homeostasis ✔; GO:0010881 regulation of cardiac muscle contraction by regulation of the release of sequestered calcium ion ✔; GO:0060048 cardiac muscle contraction ✔ |
| Cellular component | GO:0014701 junctional sarcoplasmic reticulum membrane ✔ is the closest cached term to "JMC". Search GO for a better JMC term before binding. |
| Cell types | CL:0000746 cardiac muscle cell ✔ |
| Anatomy | UBERON:0002084 heart left ventricle ✔; UBERON:0000948 heart ✔ |

### Molecular profiling, single-cell, spatial and CRISPR data

None has been published for CMD2F. No GEO datasets were identified. The structural PDB entry 3A8Y covers the BAG5 BD5–Hsp70 NBD complex (Arakawa 2010).

---

## 7. Anatomical structures affected

- **Organ:** the heart. The **left ventricle** is primary (UBERON:0002084 ✔). Right-ventricular involvement is not well described.
- **Tissue and cells:** ventricular myocardium and cardiomyocytes (CL:0000746 ✔).
- **Subcellular:** junctional membrane complexes (sarcolemma/T-tubule–junctional SR dyads) and the ER/SR. BAG5 also has reported mitochondrial and cytosolic roles in non-cardiac cells, which may not be relevant here.
- **Secondary organs:** those affected by low-output heart failure.
- **Laterality:** not applicable.

---

## 8. Temporal development

- **Onset:** adolescence to young adulthood. The youngest reported death was at 12 years and the oldest diagnosis at 34. Onset is insidious, sometimes first noticed as an arrhythmia.
- **Progression:** rapid and progressive toward advanced heart failure. Wongong describes "consistently severe" disease that is less variable than *BAG3* DCM. There are no natural-history cohorts, and no remission has been reported.
- **Suggested `progression:` phases:** preclinical (carrier or presymptomatic homozygote); symptomatic DCM with arrhythmia; advanced HF needing mechanical support or transplant.

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007 ✔), with complete penetrance in biallelic individuals (PMID:35044787).
- **Expressivity:** severe but variable. In the Wongong sibship LVEF ranged from 36% to 46%, and one sibling had a normal LV size.
- **Heterozygotes:** possible minor ECG findings in women, and possible susceptibility to tachycardia-induced cardiomyopathy. Both are unconfirmed.
- **Consanguinity:** one Middle Eastern consanguineous family (PMID:38796549).
- **Populations:** Japanese (Hakui and Inoue, Osaka and Tokyo) and Middle Eastern (studied in Thailand).
- **Prevalence:** unknown, ultra-rare. About 12 published patients (GenCC counts 12 cases across 5 publications). Suggested encoding: `measure_type: CASES_IN_LITERATURE`.
- **Sex ratio, anticipation, mosaicism:** not reported, and anticipation is not expected for this mechanism.

---

## 10. Diagnostics

- **Genetic testing:** a DCM multigene panel, exome or genome sequencing. *BAG5* is now on PanelApp Green lists, and Hakui 2022 recommends adding it to testing. Confirm biallelic status with parental segregation and Sanger sequencing. Truncating variants are well detected by exome sequencing.
- **Imaging:** echocardiography (LVEDD Z-score, LVEF) and cardiac MRI (hypokinesia). LGE patterns have not been reported.
- **ECG and Holter:** low limb-lead voltage, inferolateral T-wave inversion, poor R progression, and VT/VF.
- **Biomarkers:** BNP/NT-proBNP elevated (non-specific).
- **Histology:** reduced BAG5 and SERCA2 immunostaining in explanted myocardium (Inoue 2023). This is research-level, not diagnostic.
- **Differential diagnosis:**
  - other recessive and early-onset DCMs: *TNNI3*-AR, *GATAD1*, *RPL3L*, *NRAP*, *PPA2*, *PLEKHM2*;
  - *BAG3* DCM (dominant, broader age range);
  - arrhythmogenic cardiomyopathy (*DSP*, *FLNC*, *PLN* — overlapping arrhythmic DCM);
  - myocarditis;
  - tachycardia-induced cardiomyopathy (reversible after rate control);
  - neuromuscular and metabolic DCMs (Duchenne/Becker, Barth, mitochondrial).
- **Screening:** cascade testing of siblings in affected families, followed by echo and ECG surveillance of biallelic relatives.

---

## 11. Outcome and prognosis

- Reported outcomes are poor. Every patient in the founding Japanese cohort needed an LVAD and at least one was transplanted (PanelApp summary of PMID:35044787). One Middle Eastern sibling died at 12 years awaiting transplant.
- Arrhythmic burden is high and refractory (PMID:36130910).
- No survival statistics exist.
- Prognostic factors are not established. Biallelic truncation appears uniformly severe.

---

## 12. Treatment

No disease-specific therapy is approved. Management follows standard heart-failure care for DCM.

| Intervention | Suggested NCIT ✔ | Notes |
|---|---|---|
| Guideline-directed HF pharmacotherapy (β-blocker, ACEi/ARNI, MRA, SGLT2i) | NCIT:C15986 Pharmacotherapy ✔; agent NCIT:C29576 Beta-Adrenergic Antagonist ✔ | β-blockade is mechanistically attractive given the catecholamine-triggered phenotype in mice. This is an inference, not trial evidence. |
| ICD | NCIT:C80435 Implantable Cardioverter-Defibrillator Placement ✔ | Refractory VT/VF |
| LVAD | NCIT:C172327 Left Ventricular Assist Device Insertion ✔ | Used in all Hakui patients |
| Heart transplantation | NCIT:C15246 Heart Transplantation ✔ | Definitive therapy |
| AAV9-*BAG5* gene replacement (preclinical) | NCIT:C15238 Gene Therapy ✔; modality `GENE_THERAPY`; delivery `VIRAL_VECTOR` | PMID:35044787 (verbatim): "administration of an adeno-associated virus 9 vector carrying the wild-type BAG5 gene could fully ameliorate these DCM phenotypes" |

- **Clinical trials:** no NCT or ICTRP trials specific to *BAG5* were found.
- **Pharmacogenomics:** none.

---

## 13. Prevention

- **Primary prevention:** genetic counselling (NCIT:C15240), carrier testing in consanguineous kindreds, and prenatal or preimplantation diagnosis for families with known variants.
- **Secondary prevention:** cascade genotyping of siblings, then echo and ECG surveillance of biallelic relatives.
- **Tertiary prevention:** an ICD to prevent sudden death and early referral for advanced HF therapy.
- **Avoiding catecholamine excess:** plausible from mouse data, but not validated.

---

## 14. Other species and natural disease

No naturally occurring *BAG5* cardiomyopathy has been reported in animals, and OMIA lists none. The mouse orthologue is *Bag5* (MGI:1917619). BAG5 is conserved across vertebrates.

---

## 15. Model organisms

| Model | Genotype | Phenotype | Fidelity and limitations | Ref |
|---|---|---|---|---|
| *Bag5* mutant knock-in mouse (Osaka) | Patient-equivalent truncation | Ventricular dilatation, arrhythmogenicity and poor survival under catecholamine stimulation; JMC disruption; Ca²⁺ mishandling; rescued by AAV9-*BAG5* | Recapitulates DCM plus arrhythmia, but only under stress (catecholamine). The human disease appears without a known trigger. | PMID:35044787 (verbatim: "Bag5 mutant knock-in mice exhibited ventricular dilatation, arrhythmogenicity, and poor prognosis under catecholamine stimulation, recapitulating the human DCM phenotype") |
| *Bag5* p.Lys149fs-equivalent knock-in mouse (delCA, C57BL/6N; Chulalongkorn) | +/− and −/− | Normal to 12 months and on treadmill testing. After tunicamycin (2 mg/kg IP), LVEF and LVFS fall, apoptosis rises, and sinus pauses occur in males only; one −/− male died suddenly. | Stress-dependent; n = 3 per group; sex-discordant with the human carrier findings (ECG changes were in human females but mouse males). Suited to a `HUMAN_MODEL_MISMATCH` discussion. | PMID:38796549 (verbatim: "Bag5-/- mice displayed no abnormalities up to 12 months old and showed no anomalies during an exercise stress test.") |
| IMPC *Bag5* knockout (Bag5^em1(IMPC)Mbp) | Null | Male infertility (acephalic sperm); eye and brain calls. Cardiac phenotype not highlighted. | Supports a non-cardiac function; human fertility unknown | [IMPC MGI:1917619](https://mousephenotype.org/data/genes/MGI:1917619) |
| Neonatal rat ventricular cardiomyocytes (in vitro) | *Bag5* siRNA knockdown or adenoviral overexpression | Knockdown leads to cell death; overexpression protects against ER-stress apoptosis and lowers CHOP | Rat, neonatal, acute knockdown; not a disease model | PMID:26729625 (`evidence_source: IN_VITRO`) |

---

## Key references

| PMID | Citation | Cache status |
|---|---|---|
| 35044787 | Hakui H et al. Loss-of-function mutations in the co-chaperone protein BAG5 cause dilated cardiomyopathy requiring heart transplantation. *Sci Transl Med* 2022;14:eabf3274 | abstract cached |
| 36130910 | Hakui H et al. Refractory ventricular arrhythmias in a patient with DCM caused by a nonsense mutation in BAG5. *Circ J* 2022;86:2043 | no quotable text; do not cite snippets |
| 37873655 | Inoue S et al. Compound heterozygous truncating variants in the BAG5 gene as a cause of early-onset DCM. *Circ Genom Precis Med* 2023;16:e004282 | no quotable text; retry with `--force` |
| 38796549 | Wongong R et al. A novel BAG5 variant impairs the ER stress response pathway, causing DCM and arrhythmia. *Sci Rep* 2024;14:11980 | full text cached |
| 26729625 | Gupta MK et al. GRP78 interacting partner Bag5 responds to ER stress and protects cardiomyocytes from ER stress-induced apoptosis. *J Cell Biochem* 2016;117:1813 | full text cached |
| 20223214 | Arakawa A et al. BAG5 as Hsp70 NEF (structure). *Structure* 2010;18:309 | not cached |
| 42708185 | Jordan E et al. An updated evidence assessment of the genetic causes of DCM. *Circulation* 2026 | abstract cached |
| CGGV:assertion_97fe83b7-…-2024-06-14T160000.000Z | ClinGen BAG5 / DCM, AR, Moderate | cached |

**Gaps:**
- The Inoue 2023 and Hakui 2022 Circ J abstracts could not be retrieved.
- The JMC protein names and per-patient clinical details from Hakui 2022 need the full text.
- The OMIM numbers come from secondary sources.
- There are no prevalence, natural-history or trial data.

**Repository note:** this research run added the following files to `references_cache/`, generated with `just fetch-reference`:
- `PMID_35044787.md`, `PMID_38796549.md`, `PMID_42708185.md`, `PMID_26729625.md` — usable.
- `PMID_37873655.md`, `PMID_36130910.md` — cached with no quotable text.
- `PMID_39712638.md` — an unrelated sevoflurane paper picked up by the PubMed search. My attempt to delete it was not approved. Delete it before committing.

---

Sources:
- [Osaka University press release (Hakui/Asano 2022)](https://www.med.osaka-u.ac.jp/eng/activities/results/2022year/asano2022-0120)
- [GenCC BAG5 submission](https://search.thegencc.org/submissions/GENCC_000102-HGNC_941-MONDO_0005021-HP_0000007-GENCC_100003)
- [GenCC SGC-106981.2](https://thegencc.org/submissions/SGC-106981.2)
- [GenCC BAG5 gene page](https://search.thegencc.org/genes/HGNC:941)
- [Wongong et al. 2024, PMC11127938](https://pmc.ncbi.nlm.nih.gov/articles/PMC11127938/)
- [PanelApp Australia BAG5](https://panelapp-aus.org/panels/95/gene/BAG5/)
- [MGI OMIM:619747](https://informatics.jax.org/disease/OMIM:619747)
- [Disease Ontology DOID:0081162](https://disease-ontology.org/term/DOID:0081162)
- [DrugMap DIS6YW38](https://drugmap.idrblab.net/data/disease/details/DIS6YW38)
- [genebe BAG5](https://genebe.net/gene/hg38/BAG5)
- [NORD MONDO page](https://rarediseases.org/mondo-disease/cardiomyopathy-dilated-2f/)
- [Gupta et al. 2016, PMC4909508](https://pmc.ncbi.nlm.nih.gov/articles/PMC4909508)
- [RCSB PDB 3A8Y](https://rcsb.org/structure/3a8y)
- [IMPC Bag5](https://mousephenotype.org/data/genes/MGI:1917619)
- [Cyagen Bag5 KO](https://www.cyagen.com/mouseatlas/S-KO-13318)
- [Lesurf 2022 (BSC record)](https://bsc.es/es/printpdf/research-and-development/publications/whole-genome-sequencing-delineates-regulatory-copy-number-and)
- [medRxiv Lesurf preprint](https://www.medrxiv.org/content/10.1101/2020.10.12.20211474v1)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0081162` (5 mentions) - the report calls it "DOID"; DOID calls it **dilated cardiomyopathy 2F**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0005021` (2 mentions) - the report calls it "ACMG/ClinGen:** ClinGen Gene-Disease Validity, *BAG5*–dilated cardiomyopathy"; MONDO calls it **dilated cardiomyopathy**, and lists "familial dilated cardiomyopathy" among its other names
- `NCIT:C15240` (1 mention) - the report calls it "Primary prevention:** genetic counselling"; NCIT calls it **Genetic Counseling**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `MGI`.