---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-13T20:13:24.216342'
end_time: '2026-10-13T20:15:24.072614'
duration_seconds: 119.86
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Intellectual Developmental Disorder, X-Linked, Syndromic, With Pigmentary
    Mosaicism And Coarse Facies
  mondo_id: MONDO:0859080
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
  web_search_requests: 3
  num_turns: 17
  total_cost_usd: 1.8847569999999998
  session_id: 118cd90a-6d61-4fda-8c49-1fb9d4893517
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  - mcp__pubmed__search_articles
  assistant_text_blocks: 2
citation_count: 6
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 8
  quotes_valid: 8
  relevance_assessed: 6
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 42
  verified: 42
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 2
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0859080
    reported_labels:
    - MONDO
    ontology_label: intellectual developmental disorder, X-linked, syndromic, with
      pigmentary mosaicism and coarse facies
  - term_id: UBERON:0001434
    reported_labels:
    - growth
    ontology_label: skeletal system
  - term_id: UBERON:0002107
    reported_labels:
    - one case
    ontology_label: liver
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Developmental Disorder, X-Linked, Syndromic, With Pigmentary Mosaicism And Coarse Facies
- **MONDO ID:** MONDO:0859080 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Developmental Disorder, X-Linked, Syndromic, With Pigmentary Mosaicism And Coarse Facies** covering all of the
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

I've read the six papers already cached in the repository and am now running a few web searches for newer cohorts and models.

# TFE3-associated X-linked syndromic intellectual disability with pigmentary mosaicism and coarse facies (MONDO:0859080): research report

**Date:** 2026-10-13

**How this was compiled.** The main sources are the six PubMed records already cached in this worktree's `references_cache/`. I read them directly, and I read one of them (PMID:36608670) in full text. I added targeted web searches. The PubMed search tool was not authorised in this session, so I could not run a systematic literature sweep beyond the cached papers. Anything below marked **[unverified]** comes from memory or a secondary web summary, and its identifier needs a lookup before it goes into the knowledge base.

---

## 1. Disease information

**Overview.** This is a neurodevelopmental syndrome caused by de novo variants in **TFE3**, a gene on the X chromosome at Xp11.23. TFE3 encodes a transcription factor of the MiT/TFE family (bHLH-leucine zipper type). The core features are:
- severe intellectual disability (ID)
- epilepsy
- skin pigmentation anomalies along Blaschko's lines ("pigmentary mosaicism")
- coarse, storage-disorder-like facial features
- growth retardation

Lehalle et al. (2020) summarise the series:
> "The 12 females and 5 males presented with pigmentation anomalies on Blaschko's lines, severe ID, epilepsy, storage disorder-like features, growth retardation and recognisable facial dysmorphism." (PMID:32409512)

**Identifiers**

| System | ID |
|---|---|
| MONDO | MONDO:0859080 |
| OMIM (phenotype) | 301066. PanelApp records the OMIM title; I have not confirmed it on omim.org. |
| OMIM (gene) | TFE3 *314310 **[unverified]** |
| HGNC | hgnc:11752 (TFE3) |
| Orphanet / ICD-10 / ICD-11 / MeSH | No disease-specific code found. MeSH coverage is only through the descriptors "Pigmentation Disorders", "Intellectual Disability" and "Mosaicism". |
| GenCC / ClinGen | **Definitive** for TFE3 and X-linked syndromic complex neurodevelopmental disorder (MONDO:1040018). The ClinGen ID/Autism expert panel approved this in March 2024 ([GenCC](https://search.thegencc.org/submissions/GENCC_000102-HGNC_11752-MONDO_1040018-HP_0001417-GENCC_100001)). |

**Synonyms:** TFE3-associated neurodevelopmental disorder (PMID:31833172); TFE3-related ID with pigmentary mosaicism and storage disorder-like features (PMID:32409512); hypomelanosis of Ito–like presentation due to TFE3 (PMID:35503477).

**Data provenance:** Everything comes from aggregated case reports and series: Villegas 2019 (n=5), Lehalle 2020 (n=17, which includes those 5), Diaz 2020 (n=2), Saida 2022 (n=1) and Zhang 2025 (n=1). No EHR or registry data exist.

---

## 2. Etiology

- **Cause:** Germline de novo variants in TFE3 that act by gain of function, plus post-zygotic mosaic variants in some males.
  - Villegas 2019 reported "point mutations in a Tfe3 domain required for cytoplasmic inactivation as potentially causal for a human developmental disorder" (PMID:30595499).
  - Lehalle 2020 wrote: "Functional analysis suggested these mutations to result in ectopic nuclear gain of functions" (PMID:32409512).
- **Genetic risk factors:** Only the causal variants. No susceptibility loci or modifier genes have been described.
- **Environmental risk factors, protective factors and gene–environment interactions:** None reported. Not applicable to a de novo monogenic disorder.
- **Parental age effect:** Not studied.

---

## 3. Phenotypes

Frequencies come from the Lehalle n=17 series where the abstract states them, and from the Villegas first five as restated by Diaz (PMID:31833172):
> "severe intellectual disability (5/5), coarse facial features (4/5), and Blaschkoid pigmentary mosaicism (4/5)… All patients had normal brain Magnetic Resonance Imagings (MRIs)."

| Phenotype | Suggested HPO term | Frequency | Onset and course | Source |
|---|---|---|---|---|
| Severe intellectual disability | HP:0010864 Intellectual disability, severe | 5/5; "severe ID" in the 17 | Infancy; static neurodevelopmental | 32409512, 31833172 |
| Absent speech (non-verbal) | HP:0001344 Absent speech | Nardone states "all affected individuals being non-verbal" (a secondary synthesis, BACKGROUND role) | Childhood | 36608670 |
| Global developmental delay | HP:0001263 | Implied | Infancy | 32409512 |
| Seizures / epilepsy | HP:0001250 Seizure | Frequent (listed among the core features) | Childhood | 32409512, 36608670 |
| Blaschko-line hypo- or hyperpigmentation | HP:0007400 Irregular hyperpigmentation; HP:0001010 Hypopigmentation of the skin; "Pigmentary mosaicism" / Linear hyperpigmentation (check exact HPO labels) | 4/5 (first cohort); most of the 17 | Early childhood; stable | 32409512, 35503477 |
| Coarse facial features | HP:0000280 Coarse facial features | 4/5 | Progressive coarsening reported | 31833172 |
| Storage disorder-like features (lysosomal storage enzyme screen negative) | No specific HPO term; describe in text | Core feature | Childhood | 32409512, 31833172 |
| Growth retardation / short stature | HP:0001510 Growth delay; HP:0004322 Short stature | Core feature | Postnatal | 32409512 |
| Normal brain MRI | Negative finding | 5/5 (first cohort); 2/2 (Diaz) | n/a | 31833172 |
| Neonatal cholestasis and hepatomegaly (giant-cell hepatitis); single case | HP:0002240 Hepatomegaly; HP:0002908 Conjugated hyperbilirubinemia; HP:0001396 Cholestasis | 1 male, p.Thr187Met | Neonatal (day 12) | 39584589 |

Diaz 2020 adds that, "due to significant coarsening of the facial features, both patients were initially thought to have a lysosomal storage disorder but enzyme screening and brain MRIs were negative" (PMID:31833172).

Other features are mentioned in the full texts but not in the abstracts: behavioural problems, hypotonia, recurrent infections, and skeletal or "dysostosis-like" findings. They need full-text verification before curation **[unverified]**.

**Quality of life:** No formal studies (EQ-5D, SF-36 or similar). The burden comes from severe ID, absence of speech, and epilepsy. Most affected individuals need lifelong dependent care.

---

## 4. Genetic and molecular information

- **Gene:** TFE3 (hgnc:11752), Xp11.23. It encodes a MiT/TFE bHLH-ZIP transcription factor that binds CLEAR E-box elements in the promoters of lysosomal and autophagy genes (PMID:36608670).
- **Variant spectrum:**
  - All variants are de novo.
  - All are missense except one canonical splice variant (PMID:32409512, 31833172).
  - "Eleven of the 13 variants were localised in exon 4, 2 in exon 3, and 3 were recurrent variants." (PMID:32409512)
- **Location relative to protein structure:** The variants cluster in "helix 1" (the known Rag-binding domain, about aa 106–140) and especially in "helix 2" (about aa 180–210) (PMID:36608670).
  - Nardone et al. write: "a few mutations were identified within helix 1, but the majority were located within or immediately adjacent to helix 2."
  - A named example is **p.Thr187Met (c.560C>T)**, hemizygous de novo in a male (PMID:39584589).
- **ClinVar:** Nardone et al. found further unclassified missense variants in the same hotspot in ClinVar.
- **Population frequency:** The variants are absent from gnomAD, as expected for de novo dominant alleles. Not independently checked.
- **Functional consequence:** Gain of function, through constitutive stabilisation and nuclear accumulation of TFE3. The key evidence (PMID:36608670):
  > "We show that the disease-associated missense mutations abolish the ability to interact with Rag GTPases and constitutively stabilize TFE3."
  - This is distinct from Xp11.2 translocation renal cell carcinoma. There, somatic TFE3 fusions lose the N-terminal β-TrCP phospho-degron, so in both diseases the convergent defect is loss of nutrient-regulated protein stability.
- **Germline vs somatic:**
  - Constitutional (germline) in females and in most males.
  - Post-zygotic mosaicism in at least two males (PMID:32409512).
  - Saida 2022 recommends sequencing skin as well as blood for pigmentary mosaicism. Their cohort found "De novo germline variants in USP9X, TFE3, and KCNQ5" (PMID:35503477).
- **Modifier genes, epigenetic changes, chromosomal abnormalities:** None reported. Translocations of TFE3 cause cancer, not this syndrome.

---

## 5. Environmental information

Not applicable. No environmental, lifestyle or infectious contributors are known.

---

## 6. Mechanism and pathophysiology

### Causal chain

1. **A de novo missense variant in TFE3 exon 3 or 4** changes residues in helix 1 or helix 2. *(Human genetics; PMID:32409512)*
2. **This leads to loss of binding to the active Rag GTPases (RagA/C).** The patient residues sit at a RagA docking interface. Mutating the RagA contact residues phenocopies the patient variants. *(In vitro and ColabFold modelling; PMID:36608670)*
3. **Loss of Rag binding results in two escapes:**
   - **3a.** No recruitment to the lysosome, so no mTORC1-dependent phosphorylation of the S47 phospho-degron, so no CUL1–β-TrCP ubiquitination or proteasomal degradation. The result is that TFE3 is constitutively stable. *(PMID:36608670)*
   - **3b.** Loss of cytoplasmic sequestration, which in mouse embryonic stem cells depends on Ragulator, folliculin (FLCN) and RagC/D. The result is constitutive nuclear TFE3. *(PMID:30595499)*
4. **Stable nuclear TFE3 leads to constitutive transcriptional activity.** Nardone et al. showed that stabilisation is "both necessary and partially sufficient" for CLEAR-element target activation. *(In vitro; PMID:36608670)*
5. **In pluripotent and neural progenitor cells, ectopic nuclear Tfe3 represses developmental and metabolic programmes needed for exit from pluripotency and differentiation**, which leads to impaired developmental fate transitions. *(Mouse ESC; PMID:30595499)* The step from this to human brain development is **inferred**.
6. Downstream there are **three branches**, each inferred rather than shown in patient tissue:
   - **6a. Brain:** abnormal neurodevelopment, leading to severe ID, absent speech and epilepsy. MRI is structurally normal, which suggests a functional or cellular rather than malformative lesion.
   - **6b. Skin:** in heterozygous females, random X-inactivation produces two clones (mutant-allele-expressing and normal), giving pigmentary patterning along Blaschko's lines. In mosaic males, post-zygotic mosaicism does the same. A direct effect of TFE3 on melanocyte genes, given its MiT-family overlap with MITF, is plausible but not shown.
   - **6c. Somatic:** constitutive activation of lysosomal biogenesis and autophagy programmes may produce the "storage-like" coarse facies and growth retardation (inferred). The neonatal giant-cell hepatitis may reflect hepatocyte effects (single case; mechanism unknown).

### Ontology suggestions
- **GO biological processes:**
  - GO:0007040 lysosome organization
  - GO:0006914 autophagy
  - GO:0045893 positive regulation of DNA-templated transcription
  - GO:0048863 stem cell differentiation
  - GO:0031929 TOR signaling
  - GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process (DECREASED)
- **GO molecular function:** GO:0031267 small GTPase binding (DECREASED)
- **GO cellular components:** GO:0005765 lysosomal membrane; GO:0005634 nucleus
- **Cell Ontology:** CL:0002322 embryonic stem cell; CL:0000047 neuronal stem cell; CL:0000148 melanocyte; CL:0000182 hepatocyte
- **Pathways:** mTORC1 / Rag GTPase amino-acid sensing; the CLEAR network
- Lehalle 2020 calls the disease "a novel X-linked human condition associated with mosaicism and dysregulation within the mechanistic target of rapamycin (mTOR) pathway" (PMID:32409512).

**Omics, single-cell and spatial data:** None published for patient tissue.

---

## 7. Anatomical structures affected

- **Brain:** UBERON:0000955
- **Skin:** UBERON:0002097, with a Blaschko-line distribution
- **Face / craniofacial region:** UBERON:0001456
- **Skeletal system:** UBERON:0001434 (growth)
- **Liver:** UBERON:0002107 (one case)
- **Subcellular:** lysosome (GO:0005764) and nucleus
- **Lateralisation:** The skin lesions are segmental, linear or whorled, and can be asymmetric.

---

## 8. Temporal development

- **Onset:** Congenital or infantile, with developmental delay in infancy. The pigmentary changes appear in infancy or early childhood. Liver disease was neonatal in one case.
- **Course:** A static neurodevelopmental disorder with chronic epilepsy. Facial coarsening may become more evident with age. No natural-history study exists.

---

## 9. Inheritance and population

- **Inheritance:**
  - X-linked dominant (HP:0001423), typically de novo (HP:0025352).
  - Both sexes are affected: 12 females and 5 males in the 17-patient series.
  - Somatic mosaicism occurs in some males (HP:0001442 applies only at the individual level).
- **Penetrance and anticipation:** Penetrance appears complete in the reported cases. There is no anticipation. No familial recurrence has been reported. Parental germline mosaicism is theoretically possible, but none has been reported.
- **Prevalence:** Unknown. Ultra-rare, with about 20 published cases (17 in Lehalle, plus 2 from Diaz, 1 from Saida and 1 from Zhang; there may be overlap). Measure type: CASES_IN_LITERATURE.
- **Population:** Cases come from multiple ancestries, including European, US and Japanese. No founder effect has been reported.

---

## 10. Diagnostics

- **Primary test:** Trio exome or genome sequencing. Panels for ID or pigmentary mosaicism should include TFE3; it is on Genomics England PanelApp panels 285 and 402.
- **Tissue choice:** Sequence a skin biopsy as well as blood when mosaicism is suspected, as Saida et al. recommend: "Exome sequencing, using patients' blood and skin samples is highly recommended as the first choice for detecting causative genetic variants of pigmentary mosaicism" (PMID:35503477).
- **Supporting work-up:**
  - Brain MRI (usually normal)
  - EEG
  - Lysosomal enzyme and urinary GAG/oligosaccharide screen to exclude storage diseases (negative in TFE3 cases)
  - Karyotype or chromosomal microarray on blood or skin to exclude chromosomal mosaicism (the classic cause of hypomelanosis of Ito)
  - Liver function tests in neonates
- **Differential diagnosis:**
  - Hypomelanosis of Ito caused by chromosomal mosaicism
  - MTOR, RHOA, USP9X, KCNQ5 and PHF6 pigmentary mosaicism disorders (PMID:35503477)
  - Mucopolysaccharidoses, mucolipidoses and other lysosomal storage diseases
  - Incontinentia pigmenti
  - Pallister–Killian syndrome
- **Screening:** None applicable. There is no newborn or carrier screening.

---

## 11. Outcome and prognosis

There are no survival or life-expectancy data. Morbidity comes from:
- lifelong severe ID
- absent speech
- epilepsy
- growth failure
- in one neonate, severe cholestatic liver disease

The outcome of that neonate is not stated in the abstract. No prognostic biomarkers exist.

---

## 12. Treatment

There is no disease-specific therapy. Management is supportive. Suggested NCIT terms (verify each before binding):

| Intervention | Suggested NCIT term |
|---|---|
| Antiseizure medication | NCIT:C15986 Pharmacotherapy |
| Developmental, speech, occupational and physical therapy | NCIT:C15302, NCIT:C159273, NCIT:C121351 |
| Genetic counselling | NCIT:C15240 |
| Supportive and hepatology care for cholestasis | NCIT:C15747 Supportive Care |

**Experimental or theoretical approaches:** Nardone et al. propose the RagA–TFE3 interface as a druggable site, but in the opposite direction, to *activate* TFE3 for other diseases. For this gain-of-function syndrome, the rational strategy would be to reduce TFE3 activity or nuclear levels, for example with allele-specific antisense oligonucleotides. That is purely speculative. There are no clinical trials (no NCT or ICTRP records found).

---

## 13. Prevention

- **Primary prevention:** None; the variants are de novo.
- **Genetic counselling:** Recurrence risk is low but not zero because of possible parental germline mosaicism. Prenatal or preimplantation testing can be offered in a later pregnancy.
- **Tertiary prevention:** Seizure control, nutrition and growth monitoring, and liver monitoring in infancy.

---

## 14. Other species and natural disease

- No naturally occurring animal disease is known (OMIA not checked).
- TFE3 orthologues are conserved: mouse *Tfe3* and zebrafish *tfe3a/tfe3b*.
- The β-TrCP degron is conserved back to *Drosophila* and *Hydra* (PMID:36608670).

---

## 15. Model organisms and systems

- **Mouse embryonic stem cells** (Villegas 2019, PMID:30595499): a CRISPR screen identified lysosome activity, Ragulator, FLCN and RagC/D as factors that sequester Tfe3. Nuclear Tfe3 blocks differentiation. The disease-domain mutants were used in this system.
  - This model recapitulates the molecular gain of function.
  - It does not capture the organism-level neurological or skin phenotypes.
- **Human HEK-293T and ARPE-19 cells** (Nardone 2023): patient mutants stabilise TFE3 and abolish Rag and β-TrCP binding.
- **Mouse knockouts:** *Tfe3* knockout mice are viable. *Tfe3;Mitf* double knockouts develop osteopetrosis (cited within PMID:36608670). These are loss-of-function models, so they do not model this disease.
- **Zebrafish:** overexpressing tfe3b in the macrophage lineage disrupts microglia, phenocopying *rraga* mutants (Iyer et al. 2022, per a [ZFIN figure record](https://www.zfin.org/ZDB-FIG-220905-45)) **[unverified PMID]**.
- **Mouse neural stem/progenitor cells:** TFEB/TFE3 are reported to maintain embryonic neural stem-progenitor cells (Yuizumi et al. 2021, *Stem Cells*) **[unverified]**.
- **Gap:** No patient-variant knock-in mouse or iPSC/organoid model has been published, as far as these searches found. This is a key knowledge gap, best recorded as a HUMAN_MODEL_MISMATCH / KNOWLEDGE_GAP discussion.

---

## Evidence summary (cited PMIDs, all in `references_cache/`)

| PMID | Type | Key contribution |
|---|---|---|
| 30595499 | IN_VITRO (mouse ESC), plus human genetics | Gene discovery; Rag–FLCN sequestration of Tfe3 |
| 32409512 | HUMAN_CLINICAL | 17-patient delineation; exon 3/4 clustering; male mosaicism |
| 31833172 | HUMAN_CLINICAL | Two females; splice variant; storage-disease mimic; normal MRI |
| 35503477 | HUMAN_CLINICAL | TFE3 among the monogenic causes of pigmentary mosaicism; blood + skin sequencing |
| 36608670 | IN_VITRO / COMPUTATIONAL | Mechanism: RagA interface, constitutive stabilisation |
| 39584589 | HUMAN_CLINICAL | Male p.Thr187Met; neonatal giant-cell hepatitis and cholestasis |

## Open gaps
- No confirmed OMIM or Orphanet record wording.
- No phenotype frequencies beyond the abstract-level counts; the Lehalle full text is needed.
- No animal model of the patient variants.
- No natural-history or quality-of-life data.
- No newer (2023–2025) multi-patient cohorts were found by web search; a PubMed sweep is still needed.

### Sources
- [Lehalle et al., J Med Genet 2020](https://jmg.bmj.com/content/57/12/808)
- [Genomics England PanelApp – TFE3 (panel 285)](https://panelapp.genomicsengland.co.uk/panels/285/gene/TFE3/)
- [Genomics England PanelApp – TFE3 (panel 402)](https://panelapp.genomicsengland.co.uk/panels/402/gene/TFE3/)
- [GenCC submission – TFE3 / MONDO:1040018](https://search.thegencc.org/submissions/GENCC_000102-HGNC_11752-MONDO_1040018-HP_0001417-GENCC_100001)
- [ZFIN figure ZDB-FIG-220905-45 (tfe3b / microglia)](https://www.zfin.org/ZDB-FIG-220905-45)
- [FAU CRIS record for Lehalle 2020](https://cris.fau.de/publications/238899593)
- PubMed records (cached in the repo): PMID:30595499, 32409512, 31833172, 35503477, 36608670, 39584589

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 8 |
| Quoted claims found in source | 8 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 8 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859080` (2 mentions) - the report calls it "MONDO"; MONDO calls it **intellectual developmental disorder, X-linked, syndromic, with pigmentary mosaicism and coarse facies**
- `UBERON:0001434` (1 mention) - the report calls it "growth"; UBERON calls it **skeletal system**
- `UBERON:0002107` (1 mention) - the report calls it "one case"; UBERON calls it **liver**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:1040018` (2 mentions) - the report calls it "Definitive** for TFE3 and X-linked syndromic complex neurodevelopmental disorder"; MONDO calls it **X-linked syndromic complex neurodevelopmental disorder**
- `GO:0005764` (1 mention) - the report calls it "Subcellular:** lysosome"; GO calls it **lysosome**
- `NCIT:C15240` (1 mention) - the report calls it "Genetic counselling"; NCIT calls it **Genetic Counseling**
