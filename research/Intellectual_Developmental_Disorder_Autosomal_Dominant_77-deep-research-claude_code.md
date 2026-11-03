---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-16T18:26:11.938028'
end_time: '2026-10-16T18:29:09.181233'
duration_seconds: 177.24
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Intellectual Developmental Disorder, Autosomal Dominant 77
  mondo_id: MONDO:0980748
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
  web_search_requests: 2
  num_turns: 16
  total_cost_usd: 2.1180953
  session_id: 9d0652b1-2a97-4a16-9b81-775d13d1f340
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 8
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 19
  quotes_valid: 16
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:31582721
  - PMID:21610080
  - PMID:39256359
  relevance_assessed: 18
  on_topic: 8
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 42
  verified: 41
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 16
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0980748
    reported_labels:
    - MONDO
    ontology_label: intellectual developmental disorder, autosomal dominant 77
  - term_id: HP:5200001
    reported_labels:
    - confirm
    ontology_label: Selective mutism
  labels_variant: 4
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Developmental Disorder, Autosomal Dominant 77
- **MONDO ID:** MONDO:0980748 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Developmental Disorder, Autosomal Dominant 77** covering all of the
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

Pulling the details I need from the cached references, then I'll write the report.

Now confirming the OMIM/Orphanet identifiers and checking for any reports newer than the cached ones.

# Intellectual Developmental Disorder, Autosomal Dominant 77 (MRD77; LRRC7-related neurodevelopmental disorder): Research Report

**MONDO:** MONDO:0980748 · **Category:** Mendelian · **Gene:** *LRRC7* (densin-180), 1p31.1
**Report date:** 2026-10-16

**Evidence base.** Almost everything known about this disorder in humans comes from one paper: Sachdev et al., *Nat Commun* 2024, "Variants in LRRC7 lead to intellectual disability, autism, aggression and abnormal eating behaviors" (PMID:39256359, doi:10.1038/s41467-024-52095-x). It describes 33 individuals. One further case report (PMID:41916897, *J Gene Med* 2026) adds a variant of uncertain significance. The mechanism comes from mouse knockout and mutant studies and from cell biology. All quotes below are exact abstract or full-text strings from the locally cached references, which are marked [cached]. Web sources are cited at the end.

---

## 1. Disease Information

**Overview.** MRD77 is an autosomal dominant neurodevelopmental disorder. It is caused by heterozygous missense or loss-of-function variants in *LRRC7*. The gene encodes densin-180, a brain-specific scaffold protein in the postsynaptic density of excitatory synapses. Its family is the LAP proteins, which carry leucine-rich repeats and a PDZ domain. The core features are intellectual disability (ID) and delayed speech. A large share of patients have behavioural abnormalities: aggression, impulsivity, ADHD, autism and selective mutism. A smaller subset has seizures, mild brain malformations on MRI, or hyperphagia leading to obesity.

> "We identify here 33 individuals (one of them previously described) with a dominant neurodevelopmental disorder due to heterozygous missense or loss-of-function variants in LRRC7." (PMID:39256359) [cached]

> "We conclude that LRRC7 encodes a major determinant of intellectual development and behaviour." (PMID:39256359) [cached]

**Identifiers**

| System | ID | Note |
|---|---|---|
| MONDO | MONDO:0980748 | "intellectual developmental disorder, autosomal dominant 77" |
| OMIM (phenotype) | 621415 | Taken from the MGI disease page; the OMIM entry itself was not opened. Check before binding |
| OMIM (gene) | 614453 (*LRRC7*) | From secondary sources; check |
| HGNC | hgnc:18531 (*LRRC7*) | Lowercase prefix, following the repo convention |
| Orphanet / ICD-10 / ICD-11 / MeSH | None specific | Falls under generic ID codes (ICD-10 F70–F79; ICD-11 6A00) |
| GeneReviews | None | The draft entry records that an online check found no chapter |
| ClinGen gene–disease validity | No record in the committed export | Not yet curated by ClinGen |

**Synonyms.** MRD77; LRRC7-related neurodevelopmental disorder; densin-180-related ID.

**Data provenance.** All data are aggregated case-series data: 11 discovery and 22 replication individuals, collected through GeneMatcher-style collaboration and the UK 100,000 Genomes Project. No EHR or registry data exist.

**Separate LRRC7 association.** GeneCards lists a different LRRC7-associated condition (alacrima, achalasia and impaired intellectual development). Its evidence was not assessed here and it should not be merged with MRD77.

---

## 2. Etiology

**Cause.** The cause is monogenic: a heterozygous germline *LRRC7* variant, either de novo or inherited.

**How the gene was found.** A genome-wide rare-variant association study in the 100,000 Genomes Project implicated *LRRC7* before the case series was assembled:

> "our recent genetic association analysis of 77,539 participants in the 100,000 Genomes Project (100KGP) found that high-impact rare variants in LRRC7 are associated with intellectual disability (ID)" (PMID:39256359) [cached]

> "Out of the 42 genes associated with this class, LRRC7 ranked 19th, with a PPA almost equal to 1" (PMID:39256359) [cached]

Earlier, *LRRC7* had been named a candidate gene for childhood emotional dysregulation (PMID:31582721: "LRRC7 has been identified as a candidate gene for severe childhood emotional dysregulation.") [cached].

**Risk factors.**
- *Genetic.* The causal variant is the only established risk factor. Family history matters in inherited cases.
- *Environmental.* None reported.

**Protective factors and modifiers.** None identified. Penetrance is incomplete, which implies modifiers exist, but none has been characterised.

**Gene–environment interaction.** No data.

---

## 3. Phenotypes

Frequencies come from PMID:39256359. Where the paper restricts a figure to individuals with predicted loss-of-function (pLoF) variants, the table says so. Onset is developmental (infancy to early childhood) for all neurodevelopmental features. Hyperphagia begins between 4 and 10 years.

| Phenotype | Suggested HPO | Frequency | Quote |
|---|---|---|---|
| Intellectual disability | HP:0001249 | 81% (pLoF group) | "in addition to ID (81%), the affected individuals with pLoF LRRC7 variants displayed neurodevelopmental delay (84%), delayed development of speech (81%), delayed motor development (45%) and global developmental delay (30%)" |
| Neurodevelopmental delay | HP:0012758 | 84% (pLoF) | same quote |
| Delayed speech and language development | HP:0000750 | 81% (pLoF) | "The core phenotype of these individuals consists of ID and delayed language development, in addition to ADHD, autism and seizures in several cases." |
| Motor delay | HP:0001270 | 45% (pLoF) | same quote as ID |
| Global developmental delay | HP:0001263 | 30% (pLoF) | same quote as ID |
| Atypical behavior | HP:0000708 | 90% | "atypical behaviour (90%) in terms of selective mutism and impulsive and aggressive or auto-aggressive behaviour was reported, pointing to a neurobehavioral phenotype." |
| Aggressive behavior | HP:0000718 | 8/22 (36%) of the replication cohort | "Aggression was observed equally in male and female patients (8 patients, out of 22 individuals in the replication cohort)." |
| Impulsivity | HP:0100710 | 9/22 for aggressive *or* impulsive behaviour | "aggressive or impulsive behaviour is prevalent in many cases reported here (six males, three females out of 22 cases in the replication cohort)." |
| Self-injurious (auto-aggressive) behavior | HP:0100716 | Named, no frequency given | see the atypical-behaviour quote |
| Selective mutism | HP:5200001 (confirm) | Named, no frequency given | see the atypical-behaviour quote |
| Autism | HP:0000717 | 24% | "Several patients were affected by autism spectrum disorder (ASD; 24%) as well as ADHD (24%)." |
| ADHD | HP:0007018 | 24% | same quote |
| Seizure | HP:0001250 | 6/33 (18%), varied types | "Varying types of seizures were reported in six patients; and five patients exhibited moderate brain malformations upon MRI." |
| Abnormal brain morphology | HP:0012443 | 5/33 (15%), type not stated | same quote. A coarse term, so the entry needs `coarse_binding_basis: SOURCE_UNSPECIFIED` |
| Hyperphagia | HP:0002591 (label "Polyphagia") | 4/14 truncating-variant cases (29%) | "Hyperphagia was observed in 4 out of 14 cases with truncating variants … several of the other patients were still too young to observe this phenotype" |
| Class II obesity | HP:0025500 | 3/33 | "Four patients with truncating variants in the central part of the mRNA/protein (exons 20/21) showed hyperphagia due to reduced satiety, leading to class II obesity in three of them." |

The hyperphagia resembles Prader-Willi syndrome: "Case descriptions are reminiscent of cases of Prader-Willi syndrome with patients foraging for food regardless of its source" (PMID:39256359) [cached].

**Additional features from a single case** (PMID:41916897, the VUS case): tonic seizures, failure to thrive (HP:0001508), mild microcephaly (HP:0040196), and hypotonia (HP:0001252):

> "a proband presenting global developmental delay (GDD), tonic seizures, failure to thrive, mild microcephaly, intellectual disability (ID), and hypotonia." [cached]

Because the variant is a VUS, these should be treated as supporting observations only.

**Severity and course.** The ID is generally described as mild to moderate (secondary-database definition). The neurodevelopmental features are static. Behaviour and eating problems emerge or change with age.

**Quality of life.** No formal measures (EQ-5D, PedsQL) have been reported. The heaviest burdens are likely aggression, self-injury and hyperphagia-driven obesity, by analogy with Prader-Willi syndrome. This is inferred, not measured.

---

## 4. Genetic / Molecular Information

**Gene.** *LRRC7* (hgnc:18531), on 1p31.1. It encodes densin-180, a LAP family member: N-terminal LRRs, a central region containing a CaMKII-binding "densin-IN" domain, and a C-terminal PDZ domain. Expression is limited to the brain.

**Variant spectrum** (PMID:39256359)
- **Truncating (more than half of cases):** "Nonsense, splice site and frameshift variants and a 99 kB deletion encompassing the last exon were observed as truncating variants." [cached] Truncations in exons 20/21 track with hyperphagia and obesity. The authors note that this region is alternatively spliced in rodent brain.
- **Missense:** These cluster at LRR consensus positions (L65S, N94S found de novo twice, C106Y, A193P, L221M, L296P). There is one PDZ-domain missense, L1567Q, inherited from the father.
  > "In summary, four variants at key positions of the LRR consensus sequence (L65, N94, C106 and L296) severely disrupt binding to all partners tested." [cached]
  > "Strikingly, all missense variants which disrupt binding to the newly identified interaction partners of the LRR occurred de novo." [cached]
- **Later VUS:** c.2660C>T p.(Pro887Leu), de novo, exon 18, NM_001370785.2. The proband had reduced *LRRC7* mRNA (PMID:41916897) [cached].

**Classification.** Most cohort variants were reported as pathogenic or likely pathogenic. The 2026 variant is a VUS under ACMG criteria. Individual ClinVar submissions were not reviewed for this report.

**Population constraint.**
> "This suggests haploinsufficiency for the encoded Densin-180 protein as a major pathomechanism, consistent with human population data from gnomAD (pLI = 1, o/e = 0.13, gnomAD v4.1.0)." [cached]

**Origin.** All variants are germline. "In at least eleven cases where both parents were available for analysis, we determined that the respective variant appeared de novo." [cached] At least eight variants were inherited.

**Functional consequence.**
- Truncating variants: loss of function through haploinsufficiency, with transcripts expected to undergo nonsense-mediated decay.
- LRR missense variants: loss of binding to partner proteins (PP1α, MACF1, Erbin, DDX3X). This is loss of function at the domain level. A dominant-negative effect has not been tested.
- L1567Q: reduced δ-catenin binding and mistargeting away from synapses.

**Modifier genes, epigenetics, chromosomal abnormalities.** None reported. The 99 kb deletion is the only structural variant. No contiguous-gene 1p31.1 syndrome has been defined.

**Panel inclusion.** Genomics England PanelApp lists *LRRC7*. PanelApp Australia lists it on the "Severe early-onset obesity" panel.

---

## 5. Environmental Information

No environmental, lifestyle or infectious factors are known. This section does not apply.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **A heterozygous *LRRC7* variant** (truncating, or missense in the LRR or PDZ domain) **leads to** reduced densin-180 dosage or loss of specific protein interactions.
   - *Branch A, truncating:* nonsense-mediated decay, which **results in** haploinsufficiency. This is inferred from the variant class plus pLI = 1. Protein reduction has not been measured in patient tissue.
   - *Branch B, LRR missense:* loss of binding to PP1α, MACF1, Erbin and DDX3X. This is shown by co-immunoprecipitation in 293T cells. L296P also fails to reach the postsynapse.
   - *Branch C, PDZ missense (L1567Q):* reduced δ-catenin binding and **therefore** fewer densin clusters at Shank3-positive synapses (shown in neurons).
2. **Loss of densin-180 scaffolding leads to** (a) loss of the CaMKIIα–densin–PP1α complex and mistargeting of PP1; (b) reduced postsynaptic mGluR5 (and DISC1); (c) reduced surface Cav1.2 channels and weaker Cav1.2-to-nucleus signalling.
   - (a) "These data are compatible with a model where Densin-180 may scaffold a αCaMKII/Densin-180/PP1α triple complex." (PMID:39256359, in vitro)
   - (b) "loss of densin results in reduced levels of α-actinin in the brain and selective reduction in the localization of mGluR5 and DISC1 in the PSD fraction" (PMID:22072671, knockout mouse)
   - (c) "the cell surface levels of Cav1.2 in the brain, as well as Cav1.2 current density and signaling to the nucleus, are reduced in neurons from densin KO mice." (PMID:28363979)
3. **Those changes lead to** altered phosphorylation of synaptic substrates and **impaired long-term depression (LTD)**, both mGluR-dependent and NMDA receptor-dependent.
   - "deletion of densin results in impairment of mGluR- and NMDA receptor-dependent forms of long-term depression, alters the early dynamics of regulation of CaMKII by NMDA-type glutamate receptors, and produces a change in spine morphology." (PMID:22072671)
   - The PP1 link is proposed, not demonstrated: "we propose a pathomechanism where disruption of the Densin-180/PP1 complex leads to alter targeting of PP1 to its substrates, thus changing the phosphorylation status of synaptic proteins during synaptic plasticity." (PMID:39256359)
4. **In parallel**, densin loss **leads to** reduced dendritic arborisation, neurite outgrowth and changed spine morphology.
   - "Sholl analysis showed reduced branching of dendrites for some of the LRR variants, which became significant for L65S, N94S and L296P variants" (PMID:39256359)
   - "mutant primary neurons had impaired neurite outgrowth which was rescued by CDPPB treatment." (PMID:31582721)
5. **Impaired plasticity and altered circuit structure lead to** intellectual disability and speech delay. This step is inferred by analogy with other ID syndromes: "A linkage between ID and deficits in synaptic plasticity (in particular LTD) has been established for other ID syndromes" (PMID:39256359).
6. **Reduced mGluR5 signalling leads to** aggression, anxiety and social dysfunction. This is supported by pharmacological rescue in mice: "The pivotal role of mGluR5 signaling was demonstrated by rescue of behavioral defects with augmentation of mGluR5 receptor activity by … (CDPPB)." (PMID:31582721)
7. **Hyperphagia and obesity:** the mechanism is **unknown**. It is confined to central truncations (exons 20/21), and the cohort paper says it is unresolved. No upstream node should be asserted for it.

### Supporting detail

- **CaMKII.** Densin-180 binds CaMKIIα and CaMKIIβ through a central densin-IN domain that resembles CaMKIIN. It inhibits CaMKII selectively by substrate: "Phosphorylation of … Ser-831 in AMPA receptor GluA1 subunits is fully inhibited by densin. However, CaMKII phosphorylation of Ser-1303 in NMDA receptor GluN2B subunits is not effectively inhibited" (PMID:21610080, *J Biol Chem* 2011) [cached].
- **Cav1.3.** "densin is required for Ca(2+)-dependent facilitation of Ca(v)1.3 channels" (PMID:20392935, *J Neurosci* 2010, HEK293T cells) [cached].
- **Memory.** Knocking down densin-180 in ventral hippocampus impairs 24-hour contextual fear memory and lowers basal CaMKIIα phosphorylation at T286 and T305 (PMID:33064361, *Brain Behav* 2020) [cached].
- **Invertebrate conservation.** Edits to the *C. elegans* LAP orthologue *let-413* at the residue matching a patient variant (L248P) are embryonic lethal and disrupt adherens junctions: "let-413[L248P] embryos display an epidermal integrity defect." (PMID:39256359)

### Suggested ontology terms

- **GO biological processes:** GO:0060292 long-term synaptic depression; GO:0006470 protein dephosphorylation; GO:0099072 regulation of postsynaptic membrane neurotransmitter receptor levels; GO:0007216 G protein-coupled glutamate receptor signaling pathway; GO:0061577 calcium ion transmembrane transport via high voltage-gated calcium channel; GO:0048813 dendrite morphogenesis.
- **GO cellular components:** GO:0014069 postsynaptic density; GO:0043197 dendritic spine.
- **CL cell types:** CL:1001571 hippocampal pyramidal neuron; CL:0000679 glutamatergic neuron.
- **CHEBI:** a CHEBI ID for CDPPB was not looked up for this report and needs a lookup before binding.

**Not involved:** immune, metabolic and tissue-damage mechanisms. No omics, single-cell or spatial datasets specific to this disorder were found.

---

## 7. Anatomical Structures Affected

- **Organ and system:** brain (UBERON:0000955), nervous system. Hippocampus (UBERON:0002421) is the main site of the mechanistic work. Cerebral cortex (UBERON:0000956) is plausible.
- **Secondary:** obesity is a systemic consequence of the eating behaviour, not of disease in the adipose tissue itself.
- **Cells:** excitatory glutamatergic neurons (dendrites and spines).
- **Subcellular:** postsynaptic density and dendritic spine.
- **Lateralisation:** not applicable. The MRI malformations were not described in enough detail to say.

---

## 8. Temporal Development

- **Onset:** congenital or early childhood, noticed as developmental and speech delay. Hyperphagia starts at 4–10 years.
- **Course:** a static neurodevelopmental disorder. No regression or progression has been reported. The behaviour problems persist. Mouse data show juvenile aggression followed by anxiety and social dysfunction in adulthood (PMID:31582721).
- **Duration:** lifelong. No staging exists, and there is no remission.
- **Critical periods:** early development, for intervention on development and speech. The hyperphagia window (from about age 4) is a time to start preventing obesity. The authors call for long-term follow-up of young patients.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant (HP:0000006).
- **Penetrance:** incomplete. "In at least eight cases, the variants in LRRC7 were inherited from their parents; five of these were classified as unaffected by the enrolling clinicians, indicating that LRRC7 variants may display incomplete penetrance." [cached]
- **Expressivity:** variable. "Phenotypic heterogeneity is evident in cases who share the same variant, such as mother and daughter in pedigree Z, where the daughter has a rather typical phenotype, whereas the mother is affected by a neuropsychiatric disorder but no ID." [cached]
- **Inherited vs de novo severity:** "Currently, we did not observe that inherited variants lead to a less severe phenotype than de novo variants." [cached]
- **Prevalence:** unknown, around 35 reported cases. A suitable record is `CASES_IN_LITERATURE` with a qualitative `RARE` class.
- **Anticipation, founder effect, consanguinity, carrier frequency:** none reported or not applicable.
- **Germline mosaicism:** not reported. It should be considered in recurrence counselling, as for any de novo dominant disorder.
- **Sex ratio:** both sexes are affected. Aggression occurs equally in males and females. Mouse data show aggression in male heterozygotes: "two independent studies on Lrrc7 deficient mice have observed a strong aggression phenotype in homozygous, but also in male heterozygous ko mice" [cached].
- **Population and geography:** the cohort is international, mostly European (UK 100KGP plus a multinational replication). No population-specific variants are known.

---

## 10. Diagnostics

- **First-line test:** exome or genome sequencing, or a neurodevelopmental/ID gene panel that includes *LRRC7*. The original cohort used exome and panel sequencing, and 100KGP used genome sequencing.
- **Chromosomal microarray:** may detect deletions, such as the 99 kb last-exon deletion if resolution allows. Otherwise, use genome sequencing or targeted copy-number analysis.
- **Interpretation:** most LRR missense variants are de novo and lose partner binding. Novel missense variants (for example p.Pro887Leu) are likely to remain VUS without functional or segregation data.
- **Supporting tests:** brain MRI (malformations in 15%); EEG if seizures occur; behavioural and developmental assessment; BMI and growth monitoring. There are no biochemical biomarkers.
- **Differential diagnosis:** other monogenic causes of ID with behaviour problems. Among PSD scaffold disorders: SHANK3 (Phelan-McDermid), SYNGAP1, DLG4, CAMK2A/B. For hyperphagia with ID: Prader-Willi syndrome (methylation testing), MC4R, SIM1, and the hyperphagic subset of 16p11.2 deletion. Fragile X should be tested in males.
- **Screening:** no newborn or population screening. Cascade testing of parents is useful for recurrence risk, but incomplete penetrance complicates interpretation.

---

## 11. Outcome / Prognosis

- **Survival:** no data on reduced life expectancy. None is expected apart from complications of obesity and epilepsy (this is inferred).
- **Morbidity:** lifelong ID, with behaviour problems that are a major burden on families. Class II obesity in about 9% of the cohort overall, and more in the central-truncation subgroup.
- **Prognostic factors:** truncations in exons 20/21 predict hyperphagia and obesity. No other genotype–phenotype correlations have been established.
- **Quality-of-life studies:** none.

---

## 12. Treatment

There is no disease-specific therapy. Management is supportive and treats symptoms.

| Intervention | NCIT suggestion | Notes |
|---|---|---|
| Speech-language therapy | NCIT:C159273 (Speech Language Therapy) | For the core speech delay |
| Occupational and physical therapy | NCIT:C121351, NCIT:C15302 | For motor delay |
| Behavioural therapy | NCIT:C181743 (behavioral counseling); check label | Aggression, impulsivity, ASD |
| Pharmacotherapy for ADHD, aggression or seizures | NCIT:C15986 Pharmacotherapy + `therapeutic_agent` | Standard agents. No LRRC7-specific data |
| Dietary management and food-access restriction | NCIT:C15447 Dietary Intervention | Hyperphagia, managed as in Prader-Willi syndrome (extrapolated) |
| Genetic counselling | NCIT:C15240 | Recurrence risk; incomplete penetrance |

- **Experimental:** the mGluR5 positive allosteric modulator CDPPB reversed behavioural and neurite defects in *Lrrc7* mutant mice (PMID:31582721). This is preclinical only. No human trials exist (no ClinicalTrials.gov entries were found for *LRRC7*).
- **Advanced therapies:** none. Gene therapy and ASO approaches have not been reported.
- **Pharmacogenomics:** none.

---

## 13. Prevention

- **Primary:** not applicable.
- **Secondary:** early molecular diagnosis allows early developmental intervention.
- **Tertiary:** watch weight and eating behaviour from about age 4 to prevent obesity; screen behaviour and seizures.
- **Genetic counselling:** a de novo case carries a low recurrence risk, but parental germline mosaicism adds some. Inherited cases carry a 50% transmission risk with incomplete penetrance. Prenatal or preimplantation testing is possible once the familial variant is known.

---

## 14. Other Species / Natural Disease

- **Naturally occurring disease:** none reported in OMIA.
- **Orthologues:** mouse *Lrrc7* (densin); zebrafish *lrrc7* (ZFIN ZDB-GENE-130530-876); *C. elegans* LAP orthologue *let-413*, the single worm gene homologous to the four human LAP genes. NCBI Gene IDs were not looked up for this report.
- **Conservation:** the leucine positions in the LRR consensus are conserved down to *let-413*, and the matching edit (L248P) is lethal in worms.
- **Zoonotic potential:** not applicable.

---

## 15. Model Organisms

| Model | Phenotype recapitulation | Limitation | Ref |
|---|---|---|---|
| *Lrrc7*−/− (densin knockout) mouse | Autism- and schizophrenia-like behaviours; reduced postsynaptic mGluR5 and DISC1; impaired mGluR- and NMDA receptor-dependent LTD; altered CaMKII dynamics; changed spines; reduced surface Cav1.2 | Homozygous null, while patients are heterozygous | PMID:22072671; PMID:28363979 |
| *Lrrc7* mutant mouse (about 2% residual transcript) | Juvenile aggression, adult anxiety and social dysfunction, impaired neurite outgrowth; all rescued by CDPPB | Near-null homozygous animals; mouse aggression is an imperfect proxy | PMID:31582721 |
| Male heterozygous knockout mice | Aggression (cited in PMID:39256359) | Primary data are in the cited studies, which were not reviewed here | PMID:39256359 refs 13–14 |
| Ventral hippocampal densin knockdown (mouse) | Impaired 24-hour contextual fear memory; reduced pCaMKIIα | Acute knockdown, not germline | PMID:33064361 |
| *C. elegans let-413*[L248P] knock-in | Embryonic lethality and adherens-junction defects | Epithelial function, not neuronal | PMID:39256359 |
| Primary rat/mouse hippocampal neurons overexpressing patient variants | Synaptic mistargeting (L296P, L1567Q) and reduced dendritic branching | Overexpressed on a wild-type background | PMID:39256359 |
| 293T co-immunoprecipitation / BioID | Loss of binding to LRR partners | Non-neuronal cells | PMID:39256359 |

No iPSC-derived neurons, organoids or IMPC phenotype data specific to this disorder were found.

---

## Gaps and Caveats

1. **One defining cohort.** Frequencies are drawn from 22–33 individuals and some are restricted to the pLoF subgroup. They should not be generalised.
2. **The OMIM numbers (621415 and 614453) come from secondary sources** (MGI and database aggregators). Confirm them on omim.org before entering them.
3. **The mechanism rests on homozygous mouse models.** Haploinsufficiency at the synapse has not been shown directly, apart from aggression in male heterozygous mice.
4. **The hyperphagia mechanism is unknown.**
5. **Local cache contamination.** About 17 untracked `references_cache/` files in this worktree concern *ZBTB7A*/LRF, not *LRRC7*: PMID 9927193, 10477728, 15662416, 17495164, 19244234, 19853566, 19942610, 22500835, 26816381, 34515416, 35474350, 36907604, 37924864, 39490153, 39875952, 39886999 and 40665149. Only these caches are relevant to MRD77: PMID 39256359, 22072671, 28363979, 31582721, 21610080, 20392935, 33064361 and 41916897. Prune the unrelated files before committing.

---

## References

**Primary literature (cached locally)**
- PMID:39256359. Sachdev et al. *Nat Commun* 2024. doi:10.1038/s41467-024-52095-x · [PMC11387733](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11387733/)
- PMID:41916897. Khan et al. *J Gene Med* 2026. doi:10.1002/jgm.70090
- PMID:22072671. Carlisle et al. *J Neurosci* 2011. doi:10.1523/JNEUROSCI.5877-10.2011
- PMID:31582721. *Transl Psychiatry* 2019. doi:10.1038/s41398-019-0580-9
- PMID:28363979. Wang et al. *J Neurosci* 2017. doi:10.1523/JNEUROSCI.2583-16.2017
- PMID:21610080. Jiao et al. *J Biol Chem* 2011. doi:10.1074/jbc.M110.216010
- PMID:20392935. Jenkins et al. *J Neurosci* 2010. doi:10.1523/JNEUROSCI.4367-09.2010
- PMID:33064361. *Brain Behav* 2020. doi:10.1002/brb3.1891

**Web sources**
- [MGI disease page, OMIM:621415](https://www.informatics.jax.org/disease/OMIM:621415)
- [MalaCards: MRD77](https://malacards.org/card/intellectual_developmental_disorder_autosomal_dominant_77)
- [GeneCards: LRRC7](https://www.genecards.org/card/LRRC7)
- [Genomics England PanelApp: LRRC7](https://nhsgms-panelapp.genomicsengland.co.uk/entities/LRRC7)
- [PanelApp Australia: Severe early-onset obesity, LRRC7](https://panelapp-aus.org/panels/3764/gene/LRRC7/)
- [ZFIN: lrrc7](https://zfin.org/ZDB-GENE-130530-876)
- [DOAJ record, Nat Commun 2024](https://doaj.org/article/fa7e561bde0647a3a38569265135f1c2)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 16 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 18 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:31582721`: "The pivotal role of mGluR5 signaling was demonstrated by rescue of behavioral defects with augmentation of mGluR5 receptor activity by … (CDPPB)."
  - closest text in source: "The pivotal role of mGluR5 signaling was demonstrated by rescue of behavioral defects with augmentation of mGluR5 receptor activity by 3-Cyano-N-(1,3-diphenyl-1H-pyrazol-5-yl)benzamide (CDPPB)"
- `PMID:21610080` *(abstract only)*: "Phosphorylation of … Ser-831 in AMPA receptor GluA1 subunits is fully inhibited by densin. However, CaMKII phosphorylation of Ser-1303 in NMDA receptor GluN2B subunits is not effectively inhibited"
  - closest text in source: "However, CaMKII phosphorylation of Ser-1303 in NMDA receptor GluN2B subunits is not effectively inhibited by densin in vitro or in intact cells"
- `PMID:39256359`: "let-413[L248P] embryos display an epidermal integrity defect."
  - closest text in source: "let-413[L248P] embryos display an epidermal integrity defect."

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 22 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0980748` (2 mentions) - the report calls it "MONDO"; MONDO calls it **intellectual developmental disorder, autosomal dominant 77**
- `HP:5200001` (1 mention) - the report calls it "confirm"; HP calls it **Selective mutism**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0100716` (1 mention) - the report calls it "Self-injurious (auto-aggressive) behavior"; HP calls it **Self-injurious behavior**
- `HP:0002591` (1 mention) - the report calls it "label "Polyphagia"; HP calls it **Polyphagia**
- `UBERON:0000955` (1 mention) - the report calls it "Organ and system:** brain"; UBERON calls it **brain**, and lists "the brain" among its other names
- `NCIT:C15240` (1 mention) - the report calls it "Genetic counselling"; NCIT calls it **Genetic Counseling**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.