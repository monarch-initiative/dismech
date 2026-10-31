---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-18T22:59:44.878785'
end_time: '2026-10-18T23:02:00.896440'
duration_seconds: 136.02
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Inflammatory Bowel Disease 30
  mondo_id: MONDO:0033643
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
  num_turns: 12
  total_cost_usd: 1.8271081999999996
  session_id: 069d7646-5450-47b5-b126-9033fc3f3c44
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 8
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 10
  quotes_valid: 9
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:29408806
  relevance_assessed: 12
  on_topic: 12
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 17
  verified: 17
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 1
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Inflammatory Bowel Disease 30
- **MONDO ID:** MONDO:0033643 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Inflammatory Bowel Disease 30** covering all of the
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

I've confirmed the identifiers (OMIM 619079, gene CARD8). Now a last search on recent CARD8 biology before writing the report.

# Inflammatory Bowel Disease 30 (IBD30; CARD8-associated Crohn disease): research report

**Summary.** IBD30 is a provisional monogenic form of Crohn disease. It rests on a single kindred in which three relatives carried one copy of a missense change, p.V44I, in the T60 isoform of CARD8. CARD8 normally restrains the NLRP3 inflammasome. In this kindred the variant protein failed to bind NLRP3 and also blocked the normal CARD8 protein from doing so, which is a dominant-negative effect. The result was excess interleukin-1β (IL-1β). The proband's disease did not respond to anti-TNF therapy but did respond to IL-1 blockade (PMID:29408806). Most of the sections the template asks for, such as epidemiology, natural history, penetrance and animal models, have no disease-specific data. Those gaps are marked below rather than filled in.

> **Before using any ontology ID in this report:** the CURIEs suggested here are leads only. Under the repository's term contract, each one must be looked up (runoak or the `cache/<prefix>/terms.csv` files) and confirmed with `just validate-terms` before it is bound.

---

## 1. Disease information

**Overview.** OMIM describes IBD30 as abdominal pain with watery or bloody diarrhoea, plus intestinal changes consistent with Crohn disease. It is inherited as autosomal dominant. OMIM marks the gene–phenotype link with "?", meaning it is provisional ([MedGen C5436750](https://https.ncbi.nlm.nih.gov/medgen/1737985); [OMIM 609051 mirror](https://0-www-ncbi-nlm-nih-gov.brum.beds.ac.uk/omim/609051)).

| Identifier | Value |
|---|---|
| MONDO | MONDO:0033643, *inflammatory bowel disease 30* ([SAIL concept library](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0033643/)) |
| OMIM (phenotype) | 619079 |
| OMIM (gene) | 609051, *CARD8*, chromosome 19q13.33 |
| HGNC | hgnc:17057, CARD8 (already bound in the draft entry) |
| MedGen | C5436750 |
| Orphanet / ICD-10 / ICD-11 / MeSH | No disease-specific code was found. The parent classification is Crohn disease (ICD-10 K50; MeSH D003424). |

- **Synonyms:** IBD30; inflammatory bowel disease (Crohn disease) 30; CARD8-associated Crohn disease.
- **Type of source:** everything known comes from individual patients: one family plus one case report. There is no aggregated, registry-level data.
- **Gene panels:** Genomics England PanelApp rated CARD8 amber (moderate evidence) for monogenic IBD in 2024, up from red in 2020 ([PanelApp GE](https://panelapp.genomicsengland.co.uk/panels/398/gene/CARD8/); [PanelApp Australia](https://panelapp-aus.org/panels/123/gene/CARD8)).

## 2. Etiology

**Primary cause.** A heterozygous germline missense variant in *CARD8*:

> "Whole exome sequencing and PCR studies identified the affected individuals as having a V44I mutation in a single allele of the T60 isoform of CARD8." (PMID:29408806, human clinical)

**Genetic risk factors beyond the monogenic variant.** The common nonsense polymorphism CARD8 rs2043211 (p.Cys10Ter) has been studied as a susceptibility allele. These studies concern ordinary IBD, not IBD30.

- In Koreans: "rs2043211 of CARD8 showed significant association with UC (P = 0.011; odds ratio = 1.50…)". The stop allele was linked to higher serum IL-1β, but only in female patients with ulcerative colitis (PMID:21248762).
- A meta-analysis found no overall association with Crohn disease (OR 0.93, 95% CI 0.87–1.01). It did find associations in subgroups: ileal CD (OR 0.83) and stenotic or fistulizing CD (OR 0.81) (PMID:26462578).
- CARD8 variants have also been associated with juvenile idiopathic arthritis (PMID:24295199), asbestos-related fibrosis (PMID:24142982) and diabetic nephropathy (PMID:33164551). These show the gene's general role in inflammasome biology, but none of them is IBD30 evidence.

**Environmental risk factors:** none have been reported for IBD30.

**Protective factors:** none have been reported. Some common CARD8 variants were associated with a lower risk of diabetic nephropathy (PMID:33164551), but that does not apply here.

**Gene–environment interactions:** none have been reported. The rs2043211 association results differ between populations, which has been attributed to interactions with NLRP3 or NOD2 variants (PMID:21248762), but this was never tested in IBD30.

## 3. Phenotypes

All phenotypes below come from 3 affected members of a single kindred, so frequencies cannot be estimated.

| Phenotype | Type | Evidence | HPO lead (verify) |
|---|---|---|---|
| Crohn disease of varying severity | clinical | "three members of a kindred (the proband, his mother and his aunt), each with Crohn's disease of varying severity" (PMID:30455704, review by the discovery group) | Crohn's disease HP:0100280 |
| Abdominal pain | symptom | OMIM clinical synopsis; the proband's abdominal symptoms resolved on IL-1 blockade (PMID:30455704) | Abdominal pain HP:0002027 |
| Watery or bloody diarrhoea | symptom | OMIM clinical synopsis | Diarrhea HP:0002014; Bloody diarrhea HP:0025085 |
| Raised fecal calprotectin | laboratory | It fell with treatment in the proband (PMID:30455704) | search HPO for "fecal calprotectin" |
| Raised serum IL-1β | laboratory | "The serum levels of IL-1β in the affected individuals were increased compared with those in healthy controls" (PMID:29408806) | search HPO for "interleukin-1 beta"; there may be no term |
| Monocytes overproduce IL-1β and IL-18 after NLRP3 stimulation | cellular / ex vivo | PMID:29408806; PMID:30455704 | cellular phenotype (IN_VITRO evidence) |
| Inflammatory-bowel-disease-associated arthritis and sacroiliitis | possible extra-intestinal feature | One child with a CARD8 variant of uncertain significance (VUS) had arthritis and sacroiliitis, followed by Crohn colitis with calprotectin above 8000 µg/g (PMID:37724393). Treat as unconfirmed. | Arthritis HP:0001369; Sacroiliitis HP:0100775 |

- **Age at onset:** not reported in the abstracts. The kindred spans two generations, so onset is presumably in adolescence or adulthood. The VUS case presented at age 7.
- **Severity:** variable within the family. The proband had severe, anti-TNF-refractory disease.
- **Course:** chronic. Remission was induced with IL-1 blockade.
- **Quality of life:** no disease-specific measures exist.

## 4. Genetic and molecular information

**Gene.** *CARD8* (caspase recruitment domain family member 8; also called TUCAN or CARDINAL), hgnc:17057, OMIM 609051. It has several isoforms:
- **T48** is the canonical isoform.
- **T60** has an extended N-terminus. This is the isoform that binds NLRP3 (PMID:29408806) and NLRP1 (PMID:36426349).

**Variant.** p.V44I is a missense variant in T60, inherited in the germline and present on one allele (heterozygous). The 2018 paper (PMID:29408806) and its abstract do not give a ClinVar classification, gnomAD allele frequency, or HGVS transcript notation. Look these up in ClinVar and gnomAD before curating them; none was verified for this report.

**Functional consequence.** The variant causes loss of function with a dominant-negative mechanism:

> "mutated T60 CARD8 failed to downregulate the NLRP3 inflammasome because it did not bind to NLRP3 and inhibit its oligomerization… mutated T60 CARD8 exerted a dominant-negative effect by its capacity to bind to and form oligomers with unmutated T60 or T48 CARD8 that impeded their binding to NLRP3." (PMID:29408806)

> "intact but not mutated CARD8 prevented NLRP3 deubiquitination and serine dephosphorylation." (PMID:29408806)

In the schema this maps to `functional_impact_category: DOMINANT_NEGATIVE`.

**Other variants:**
- The VUS in the 2023 paediatric case is not named in the abstract (PMID:37724393).
- A WES case report of Crohn disease with neuropsychiatric symptoms and IgG1 deficiency points to inflammasome-gene variants (PMID:35538558). Its abstract does not confirm a CARD8 variant, so check the full text before citing it.

**Modifier genes, epigenetics, chromosomal abnormalities:** none reported.

## 5. Environmental information

There are no known environmental, lifestyle or infectious triggers specific to IBD30.

One point of background biology: the CARD8 inflammasome senses HIV-1 protease activity, which leads to pyroptosis of quiescent CD4 T cells ([bioRxiv 2022](https://www.biorxiv.org/content/10.1101/2022.10.04.510817.full.pdf)). This is CARD8 acting as a sensor through its own pathway, which is separate from its role as an NLRP3 inhibitor. It has no established link to IBD30.

## 6. Mechanism and pathophysiology

**Causal chain:**

1. A heterozygous germline *CARD8* p.V44I variant changes the N-terminal extension of the T60 isoform (PMID:29408806).
2. This leads to loss of the binding between T60 CARD8 and NLRP3, so the variant protein no longer inhibits NLRP3 oligomerization (shown in HEK293 and patient monocytes; PMID:29408806).
3. In parallel, the dominant-negative effect works as follows. The variant T60 forms oligomers with wild-type T60 and T48 and keeps them from binding NLRP3. As a result, one allele is enough to cause an overall loss of CARD8 function (PMID:29408806, PMID:30455704).
4. Without CARD8 restraint, NLRP3 is deubiquitinated and dephosphorylated at serine residues. This licenses inflammasome assembly with ASC and pro-caspase-1 (PMID:29408806; CARD8 as an NLRP3 brake is shown independently in PMID:24517500).
5. Caspase-1 activation leads to more processing and secretion of IL-1β and IL-18 by monocytes and macrophages (patient monocytes ex vivo; PMID:29408806, PMID:30455704).
6. Systemic and mucosal IL-1β then drive intestinal inflammation. This step is **inferred**: the paper did not report any tissue measurement of IL-1β in the gut lesions. The inference rests on the clinical response to IL-1 blockade.
7. The result is chronic Crohn disease: abdominal pain, diarrhoea and raised calprotectin.

**Side branch (likely contributing, not demonstrated in IBD30).** T60 CARD8 also directly inhibits assembly of the NLRP1 inflammasome (PMID:36426349). A T60 variant could therefore also de-repress NLRP1, but this has not been tested for V44I.

**Separate biology, not part of the IBD30 chain.** CARD8 can act as an inflammasome sensor in its own right. It is held in check by DPP8 and DPP9, and when activated it triggers caspase-1/GSDMD pyroptosis in resting T cells (PMID:32840892).

**Why the IL-1 response matters.** The discovery group argues that, compared with IL-10 or IL-10R deficiency, "the CARD8 mutation provides more definite proof that increased and excessive IL-1β is capable of causing Crohn's disease because in this case the NLRP3 abnormality is not coupled with another abnormality" (PMID:30455704).

**Ontology leads (verify each before binding):**
- **GO processes:** NLRP3 inflammasome complex assembly (GO:0044546); interleukin-1 beta production (GO:0032611); negative regulation of NLRP3 inflammasome complex assembly (the function the variant loses); pyroptotic process.
- **CL cell types:** monocyte (CL:0000576); macrophage (CL:0000235); possibly intestinal epithelial cell.
- **Molecular profiling** (transcriptomics, single-cell, CRISPR screens): none specific to IBD30.

## 7. Anatomical structures affected

- **Organ:** the gastrointestinal tract, with a Crohn pattern. The distribution within the bowel in this kindred is not given in the abstracts. UBERON leads: intestine UBERON:0000160, ileum UBERON:0002116, colon UBERON:0001155.
- **Other organs:** the joints, but only in the VUS case (PMID:37724393).
- **Cells:** circulating monocytes (where the defect was shown) and lamina propria myeloid cells (inferred).
- **Subcellular:** cytosol, where the inflammasome assembles.

## 8. Temporal development

The onset age, stages and progression rate have not been reported. The disease is chronic, and remission in the proband was induced by treatment. In the 2023 VUS case, arthritis came before the intestinal disease (PMID:37724393).

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006); provisional in OMIM.
- **Penetrance and expressivity:** expressivity is variable ("varying severity"). Penetrance is unknown.
- **Prevalence:** unknown. The discovery group itself calls for studies "to determine the frequency of excess IL-1β secretion in Crohn's disease patient populations due to CARD8 mutations" (PMID:30455704). In schema terms: `prevalence_class: NOT_YET_DOCUMENTED`, or `CASES_IN_LITERATURE`.
- **Founder effects, consanguinity, sex ratio, geography:** none known.

## 10. Diagnostics

- **Clinical work-up:** standard Crohn disease work-up: ileocolonoscopy with biopsy, fecal calprotectin, CRP and ESR, and cross-sectional imaging.
- **Genetic testing:** CARD8 is included on monogenic IBD and very-early-onset IBD panels (PanelApp, amber). Exome sequencing found the original variant (PMID:29408806).
- **Functional testing (research only):** serum IL-1β, and IL-1β/IL-18 release from monocytes stimulated with LPS plus an NLRP3 activator such as ATP or nigericin (PMID:29408806).
- **Differential diagnosis:** ordinary polygenic Crohn disease; IL-10 or IL-10R deficiency; chronic granulomatous disease colitis (another IL-1-responsive form; PMID:30455704); other monogenic IBDs (XIAP, NOD2); NLRP3-associated autoinflammatory disease (CAPS). Note that NLRP3 proteins carrying CAPS mutations escape CARD8 restraint (PMID:24517500).
- **Screening:** cascade testing of relatives is reasonable, but no guideline addresses it.

## 11. Outcome and prognosis

There are no survival or mortality data. The prognosis appears to depend on recognising the disease as IL-1-driven: "patients with anti-TNF-α-resistant CD may respond to this treatment option" (PMID:29408806).

## 12. Treatment

| Treatment | Outcome | NCIT action term (lead) | Agent |
|---|---|---|---|
| Anti-TNF-α (adalimumab / infliximab) | Not effective in the proband (PMID:29408806). The VUS child responded to adalimumab plus methotrexate (PMID:37724393). | Pharmacotherapy NCIT:C15986 | monoclonal antibody NCIT:C20401, or NCIT drug terms for adalimumab / infliximab |
| Anakinra (IL-1 receptor antagonist) | Induced response, with abdominal symptoms and fecal calprotectin both falling (PMID:30455704) | Pharmacotherapy NCIT:C15986 | look up "Anakinra" in NCIT |
| Canakinumab (anti-IL-1β antibody) | Used for maintenance after anakinra, with continued response (PMID:30455704) | Pharmacotherapy NCIT:C15986 | look up "Canakinumab" in NCIT |
| Corticosteroids, supportive care | Standard Crohn disease care; nothing IBD30-specific | — | — |

- `therapeutic_modality`: `PEPTIDE` or `OTHER` for anakinra (a recombinant protein); `MONOCLONAL_ANTIBODY` for canakinumab.
- No clinical trials specific to IBD30 exist. NLRP3 inhibitors such as MCC950 reduced colitis in mouse models (PMID:30455704), but have not been tested in IBD30.

## 13. Prevention

No primary prevention is known. Tertiary prevention means early genotype-guided use of IL-1 blockade to avoid failed anti-TNF courses. Genetic counselling should cover the 50% risk of transmission, with penetrance unknown.

## 14. Other species

- **Natural disease:** none reported in OMIA.
- **Orthologs:** "the absence of a murine orthologue of CARD8, which would require the use of a humanized mouse model" (PMID:32840892). CARD8 "has been reported to function as a negative regulator of NLRs in human, but not in rodents" (PMID:36426349). The HIV-protease cleavage site in CARD8 is unique to humans ([bioRxiv](https://www.biorxiv.org/content/10.1101/2022.10.04.510817.full.pdf)).

## 15. Model organisms

- **No faithful animal model exists**, because mice have no CARD8. Proxy models of the mechanism:
  - mice with increased NLRP3 activity, such as hematopoietic *miR-223* deficiency, have worse DSS colitis that responds to anakinra and MCC950;
  - p40phox-deficient (CGD) mice have worse TNBS colitis.

  Both are summarised in PMID:30455704. NLRP3-knockout colitis results conflict with each other (PMID:30455704).
- **Cell systems:** HEK293 reconstitution of the inflammasome; patient and donor peripheral monocytes; monocyte-derived macrophages with CARD8 knocked down by siRNA (PMID:29408806, PMID:24517500).
- **Suggested curation:**
  - `HUMAN_MODEL_MISMATCH` discussion: mice lack CARD8;
  - `KNOWLEDGE_GAP` discussions: frequency of the variant in Crohn disease cohorts, penetrance, and whether V44I also de-represses NLRP1.

---

## Evidence quality

| Claim | Evidence | Strength |
|---|---|---|
| The V44I variant segregates with Crohn disease | 1 kindred, 3 affected members | Weak (provisional in OMIM) |
| Dominant-negative loss of NLRP3 inhibition | In vitro plus patient cells | Moderate (one laboratory) |
| IL-1β drives the disease | Treatment response in one patient | Suggestive |
| Arthritis is part of the phenotype | 1 VUS case | Unconfirmed |

## Sources

- PMIDs cited above; all are cached in `references_cache/`: 29408806, 30455704, 37724393, 24517500, 36426349, 32840892, 21248762, 26462578, 24295199, 24142982, 33164551, 35538558.
- [MedGen C5436750](https://https.ncbi.nlm.nih.gov/medgen/1737985)
- [OMIM 609051 (mirror)](https://0-www-ncbi-nlm-nih-gov.brum.beds.ac.uk/omim/609051)
- [Genomics England PanelApp, CARD8](https://panelapp.genomicsengland.co.uk/panels/398/gene/CARD8/)
- [PanelApp Australia, CARD8](https://panelapp-aus.org/panels/123/gene/CARD8)
- [SAIL concept library, MONDO:0033643](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0033643/)
- [JCI 2018 article page](https://www.jci.org/articles/view/98642/pdf)
- [bioRxiv: human-specific CARD8 motif and HIV-1](https://www.biorxiv.org/content/10.1101/2022.10.04.510817.full.pdf)
- [DPP9 and CARD8 (MSKCC)](https://synapse.mskcc.org/synapse/works/157673)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 10 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 12 |
| On topic | 12 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:29408806` *(abstract only)*: "mutated T60 CARD8 failed to downregulate the NLRP3 inflammasome because it did not bind to NLRP3 and inhibit its oligomerization… mutated T60 CARD8 exerted a dominant-negative effect by its capacity to bind to and form oligomers with unmutated T60 or T48 CARD8 that impeded their binding to NLRP3."
  - closest text in source: "In addition, these studies showed that mutated T60 CARD8 exerted a dominant-negative effect by its capacity to bind to and form oligomers with unmutated T60 or T48 CARD8 that impeded their binding to NLRP3"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 3 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0044546` (1 mention) - the report calls it "GO processes:** NLRP3 inflammasome complex assembly"; GO calls it **NLRP3 inflammasome complex assembly**
- `CL:0000576` (1 mention) - the report calls it "CL cell types:** monocyte"; CL calls it **monocyte**

Every term resolved, and every label the report gave matched.