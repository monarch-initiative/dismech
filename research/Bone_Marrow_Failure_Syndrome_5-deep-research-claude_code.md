---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-13T20:25:33.642691'
end_time: '2026-10-13T20:26:45.346745'
duration_seconds: 71.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Bone Marrow Failure Syndrome 5
  mondo_id: MONDO:0032573
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
  web_search_requests: 2
  num_turns: 11
  total_cost_usd: 0.7955933999999999
  session_id: aa4f0803-31cb-5b9b-8409-a0195ed1b485
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 2
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 7
  on_topic: 7
  validator_version: 0.3.0
term_validation:
  total_terms: 14
  verified: 13
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 2
  obsolete_terms:
  - term_id: GO:0007050
    ontology_label: GO_0007050
    replaced_by: GO:0051726
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bone Marrow Failure Syndrome 5
- **MONDO ID:** MONDO:0032573 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bone Marrow Failure Syndrome 5** covering all of the
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

I'm pulling the OMIM entry for BMFS5 to confirm the variants and the cancer-risk detail. After that I'll write the report from the cached primary papers.

# Bone Marrow Failure Syndrome 5 (BMFS5; germline TP53 C-terminal activation syndrome): research report

**Source basis.** Every claim below comes from the PubMed abstracts cached in `references_cache/` (PMIDs 30146126, 30624728, 35084091, 35362179, 36198537, 37834388, 42104732), or from a web-search summary of the OMIM entry, which I labelled as a lead where I used it. Full texts were not read for the case reports, and the OMIM page itself failed to load (HTTP 420). Statements that rest only on model inference are marked **[inferred]**. Items I could not source are marked **[gap]**. Nothing here was checked against ClinVar, gnomAD, HPO annotations, or ClinicalTrials.gov.

## 1. Disease information

- **Identifiers.**
  - MONDO:0032573, from the repo stub, with parent MONDO:0000159 (bone marrow failure syndrome).
  - OMIM #618165, from the OMIM web-search summary (lead).
  - Causal gene: TP53, hgnc:11998. The stub lists it as MONDO's causal gene.
  - Orphanet, ICD-10/11, and MeSH IDs: **[gap]**, not retrieved.
- **Definition.** An autosomal dominant inherited bone marrow failure syndrome (IBMFS). It is caused by de novo germline TP53 variants that truncate the C-terminal domain (CTD) and **increase** p53 transcriptional activity.
  - Toki et al. (PMID:30146126, Am J Hum Genet 2018, primary, human genetics plus zebrafish and iPSC): *"unique de novo TP53 germline variants found in two individuals with an IBMFS accompanied by hypogammaglobulinemia, growth retardation, and microcephaly mimicking DBA and DC."*
  - Ito (PMID:36198537, review) names it "germline TP53 activation syndrome (bone marrow failure syndrome 5)".
- **Synonyms.** Germline p53 activation syndrome (PMID:35362179). TP53-associated Diamond-Blackfan anemia / DBA-like phenotype (PMID:35084091, PMID:42104732).
- **Lump/split call to surface.** This is a germline entity. It is distinct from Li-Fraumeni syndrome (DNA-binding-domain loss of function, cancer predisposition) and from somatic TP53-mutant myeloid neoplasms (design decisions §3a). Whether the DBA-like cases should instead sit under Diamond-Blackfan anemia (RP-gene) as a subtype is a nosology question. DBA is defined by ribosomal-protein genes, and PMID:35084091 and PMID:42104732 frame these patients as "DBA-like" or "TP53-associated DBA". I would keep BMFS5 as its own entry and cross-reference DBA.
- **Data level.** The literature is aggregated case reports (n≈2 in the discovery paper, then a handful of further patients), not EHR-derived.

## 2. Etiology

- **Cause.** Heterozygous de novo germline TP53 frameshift variants clustered in the C-terminal domain.
  - Toki: *"the variants found in the two individuals studied here caused the same truncation of the protein, resulting in the loss of 32 residues from the C-terminal domain (CTD). Unexpectedly, the p53 mutant had augmented transcriptional activities, an observation not previously described in humans."*
  - Kumar et al. (PMID:35362179): third reported individual, *"a germline heterozygous C-terminal frameshift variant in TP53 similar to others that activate the transcription factor."*
  - Moisan et al. (PMID:42104732, 2026): two French patients with *NM_000546.5: c.1077delA; p.(Ser362AlafsTer8)*.
  - Fedorova et al. (PMID:35084091): two patients with "germline de novo variants in the TP53 gene". The abstract gives no cDNA change.
  - The Toki index-case nucleotide changes are **[gap]**. The shared outcome is a 32-residue CTD loss, which is consistent with the codon ~362 frameshift region. A ClinVar Miner search hit lists TP53 c.1083del p.Ser362fs, a lead that is not verified.
- **Genetic risk factors.** No modifier genes or susceptibility loci identified **[gap]**.
- **Environmental risk and protective factors; gene-environment interaction.** None reported in the sources **[gap]**.
- **Related evidence on germline p53 hyperactivation.** Rakotopare & Toledo (PMID:37834388, review): *"germline mutations affecting TP53 or its regulator MDM4 may cause short telomeres and alter hematopoiesis, but also revealed features of Diamond-Blackfan anemia (DBA) or Fanconi anemia (FA)."*

## 3. Phenotypes

Frequencies cannot be given because only about 6–8 patients are reported. HPO terms below are suggestions from my own recall and are **unverified**, so look each up before binding it.

| Phenotype | Source | Suggested HPO (verify) |
|---|---|---|
| Infantile-onset severe, transfusion-requiring anemia / red cell aplasia | OMIM summary (lead); PMID:35084091 (*"onset of macrocytic anemia within the first year of life, paucity of erythroid precursors in bone marrow"*); PMID:35362179 (*"red cell aplasia, which was steroid responsive"*) | HP:0001903 anemia, HP:0001927/other macrocytosis terms, erythroid hypoplasia |
| Hypogammaglobulinemia | PMID:30146126 | HP:0004313 |
| Growth retardation / short stature | PMID:30146126, PMID:35362179 | HP:0004322 |
| Microcephaly | PMID:30146126, PMID:35362179 | HP:0000252 |
| Intellectual disability, seizures | PMID:35362179; OMIM summary lists developmental delay and seizures | HP:0001249, HP:0001250 |
| Cellular radiosensitivity | PMID:35362179 | no confident HPO term |
| Normal telomere length | PMID:35362179; OMIM summary (lead) | not a phenotype term |
| Transient neutropenia, normocytic anemia, "distinct neurological impairments" | PMID:42104732 | HP:0001875 |

- **Variability.**
  - Steroid response differed across patients. One patient was steroid-responsive (PMID:35362179). Neither French patient responded (PMID:42104732).
  - Anemia was normocytic in the French patients and macrocytic in the Russian ones.
  - Neurological involvement varies.
- **Quality-of-life data:** none **[gap]**.

## 4. Genetic and molecular information

- **Gene.** TP53, hgnc:11998, 17p13.
- **Variant class.** C-terminal frameshifts that remove the last 32 residues (PMID:30146126). This is a gain-of-function / hyperactivating effect on transcription, not the dominant-negative DNA-binding-domain effect typical of Li-Fraumeni. For the KB slot, `functional_impact_category: GAIN_OF_FUNCTION` fits, but check whether a finer value is warranted.
- **Origin.** De novo germline in all reported cases (PMID:30146126; PMID:35084091). Parental mosaicism and recurrence risk are **[gap]**.
- **Population frequency, ACMG classification, and ClinGen gene-disease validity:** **[gap]**. A ClinGen assertion would be worth looking up in the `CGGV:` cache. I did not check it.
- **Epigenetic and chromosomal findings:** none reported.

## 5. Environmental information

None reported. A cellular radiosensitivity finding in one patient (PMID:35362179) is a cell-level observation, not an environmental risk factor. No infectious or lifestyle contributors are reported.

## 6. Mechanism and pathophysiology (causal chain)

1. **De novo TP53 frameshift in the C-terminal domain** deletes 32 residues (PMID:30146126, human genetics).
2. Loss of the CTD **increases p53 transcriptional activity**. Toki reports *"the p53 mutant had augmented transcriptional activities"* (in vitro). The CTD normally restrains DNA binding, so I infer the restraint is lost **[inferred]**.
3. p53 hyperactivation **leads to** impaired erythropoiesis. Expression in zebrafish and human iPSCs gave *"impaired erythrocyte production"* (PMID:30146126, model organism and in vitro).
4. Impaired erythropoiesis **results in** early-onset red cell aplasia / anemia, a DBA-like picture.
5. **Branch, non-hematologic.** Constitutive p53 activity **likely leads to** growth failure, microcephaly, and hypogammaglobulinemia **[inferred]**. The supporting data are mouse knock-ins (see section 15) and the review PMID:30624728, which states *"increased p53 activity underlies the developmental defects in a wide range of genetic syndromes."*

- **Positive feedback context.** In other BMFS, ribosomal, telomere, or DNA-repair defects activate p53, and p53-DREAM represses further BMFS-related genes (PMID:37834388, review, partly computational). BMFS5 is the reverse case, where p53 activation is primary and not a downstream consequence of another defect.
- **Suggested terms (verify).**
  - GO: positive regulation of apoptotic process, GO:0043065; cell cycle arrest, GO:0007050; erythrocyte differentiation, GO:0030218.
  - CL: erythroid progenitor / hematopoietic stem cell.
  - Omics: no single-cell, proteomic, or metabolomic data found **[gap]**.

## 7. Anatomical structures affected

- Bone marrow (UBERON:0002371), especially the erythroid lineage.
- Brain (microcephaly, seizures), by phenotype.
- Immune system (humoral).
- Growth axis.

Lateralization is not applicable.

## 8. Temporal development

- **Onset.** Infancy. Macrocytic anemia appeared within the first year in the Russian patients (PMID:35084091); the OMIM summary says infantile onset.
- **Course and remission.**
  - Two patients became transfusion-independent "probably due to L-leucine therapy" (PMID:35084091).
  - One patient was steroid-responsive (PMID:35362179).
  - Long-term natural history **[gap]**.
- **Cancer risk.** Whether CTD-truncating carriers have an elevated cancer risk is **not addressed in the sources I read** **[gap]**. This matters for surveillance counseling, because the usual Li-Fraumeni protocols may not apply to a hyperactivating allele.

## 9. Inheritance and population

- Autosomal dominant, all reported variants de novo (PMID:30146126; PMID:35084091).
- Prevalence, incidence, sex ratio, founder effects, and penetrance: **[gap]**. Fewer than ten patients across Japan, Russia, the USA, and France.

## 10. Diagnostics

- **Laboratory.** Anemia with erythroid hypoplasia on marrow examination, hypogammaglobulinemia, and **normal telomere length**, which argues against dyskeratosis congenita (PMID:35362179).
- **Genetic testing.** TP53 variants were found by exome sequencing in the discovery paper (Ito, PMID:36198537: "using whole-exome sequencing"). The practical point is that TP53 should be on DBA / IBMFS panels. PMID:35084091 states *"The possible role of TP53 variants should be considered in patients with DBA-like phenotype and no mutations in RP genes."*
- **Differential diagnosis.** DBA (RP genes), dyskeratosis congenita (telomere biology disorders), Fanconi anemia, Li-Fraumeni syndrome (different variant class).
- **Guideline-level criteria, screening, and biomarkers:** **[gap]**.

## 11. Outcome and prognosis

- Survival and life expectancy: **[gap]**.
- Complications: reported features include growth failure and neurodevelopmental impairment.
- Recovery. The French report documents the *"only patient to date cured by hematopoietic stem cell transplantation"* from a matched sibling donor, transfusion-independent at last follow-up (PMID:42104732).

## 12. Treatment (all from case-level observations)

- **Transfusion support.** Implied by the transfusion-dependent anemia in the OMIM summary (lead).
- **Corticosteroids.** Responsive in one patient (PMID:35362179). Non-responsive in the two French patients (PMID:42104732).
- **L-leucine.** Two patients became transfusion-independent, "probably due to L-leucine therapy" (PMID:35084091). This is uncontrolled and causality is uncertain.
- **Hematopoietic stem cell transplantation.** One patient cured by matched-sibling HSCT (PMID:42104732). A single case.
- **NCIT.** NCIT C15431 (hematopoietic cell transplantation) is already in the repo's CLAUDE.md. Other drug and supportive-care NCIT terms need a lookup. I did not run one.
- No clinical trials were checked **[gap]**.

## 13. Prevention

Genetic counseling, with a de novo origin implying a low recurrence risk, except for germline mosaicism **[inferred]**. Everything else is **[gap]**.

## 14. Other species and natural disease

No naturally occurring animal disease was identified **[gap]**; OMIA was not searched.

## 15. Model organisms

- **Zebrafish and human iPSC.** Mutant p53 expression impaired erythrocyte production (PMID:30146126).
- **Mouse.** Toki points to *"close similarities to published knock-in mouse models of TP53 lacking the CTD."* The mouse primary papers are not cited in the abstract and I did not retrieve them.
- **Mouse p53 hyperactivation reviews.** PMID:30624728 (Bowen & Attardi) reports that hematopoietic, neuronal, craniofacial, cardiovascular, and pigmentation defects arise in mice with broad p53 hyperactivation, and that many are rescued by p53 loss. This is a model-organism review and not a human phenotype source.
- **Limitation.** Whether mouse CTD-deletion phenotypes map one-to-one to human BMFS5 is open; a `HUMAN_MODEL_MISMATCH` discussion may be warranted if curated.

## Notes for curation

1. **The KB file is a stub-level placeholder.** `kb/disorders/Bone_Marrow_Failure_Syndrome_5.yaml` currently has 8 lines, with only the name and `disease_term`. The seven reference-cache files are untracked.
2. **Before writing evidence snippets,** run `just count-verified-snippets`. All quotes above come from the cached abstracts and should be re-copied exactly from the cache.
3. **Priority gaps.** The Toki cDNA/protein nomenclature, ClinGen validity, cancer risk, and the mouse primary papers.

## Sources

- [PMID:30146126 – Toki et al., Am J Hum Genet 2018](https://pubmed.ncbi.nlm.nih.gov/30146126/)
- PMID:30624728 (Bowen & Attardi 2019), PMID:35084091 (Fedorova 2022), PMID:35362179 (Kumar 2022), PMID:36198537 (Ito 2022), PMID:37834388 (Rakotopare & Toledo 2023), PMID:42104732 (Moisan 2026), all from `references_cache/`
- [OMIM #618165 mirror (not loaded; used via search summary only)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/16b4b23030b9c25e5a647a69ebd82dc9aecccaad/www.ncbi.nlm.nih.gov/omim/618165)
- Repo stub `stubs/Bone_Marrow_Failure_Syndrome_5.yaml` (MONDO:0032573, TP53)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 7 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 14 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 0 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0007050` (GO_0007050) (1 mention) - replaced by `GO:0051726`

13 of 14 terms resolved to a current term; the rest could not be looked up either way.