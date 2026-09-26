---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: true
start_time: '2026-08-27T04:34:31.156205'
end_time: '2026-08-27T04:34:31.160438'
duration_seconds: 0.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Robinow Syndrome 1
  mondo_id: ''
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 17
  num_turns: 22
  total_cost_usd: 1.2112770000000002
  session_id: 00937d02-a143-56ac-a731-3747f9ee4c64
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 26
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 8
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Robinow Syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Robinow Syndrome 1** covering all of the
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

I now have enough well-sourced material to write the comprehensive report. Compiling it now.

# Autosomal Dominant Robinow Syndrome 1 (DRS1) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Robinow syndrome is a rare, genetically heterogeneous skeletal dysplasia first described in 1969 by Meinhard Robinow, Frederic Silverman, and Hugo Smith, who reported a mother and three children with "mesomelic brachymelia, hemivertebrae, peculiar facies and genital hypoplasia," a constellation they termed a form of dwarfism with fetal facies [Robinow, Silverman & Smith, *Am J Dis Child*, 1969] ([PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4562051/), [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4717695/)). **Autosomal Dominant Robinow Syndrome 1 (DRS1)** is the specific molecular subtype caused by heterozygous pathogenic variants in **WNT5A** (chromosome 3p14.3) — the original locus in the family Robinow himself described. It is distinguished from the more recently identified dominant subtypes DRS2 (*DVL1*, 1p36.33) and DRS3 (*DVL3*, 3q27.1), and from the autosomal recessive forms caused by biallelic *ROR2* or *NXN* variants ([OMIM #180700](https://omim.org/entry/180700); [OMIM #616331](https://www.omim.org/entry/616331); GeneReviews NBK268648).

**Key identifiers:**
- **OMIM:** #180700 (ROBINOW SYNDROME, AUTOSOMAL DOMINANT 1; DRS1)
- **Disease Ontology:** DOID:0060766
- **Orphanet:** ORPHA:3107 (Autosomal dominant Robinow syndrome)
- **Gene:** WNT5A (HGNC:12784), chromosome 3p14.3
- **MedGen:** C4551475 ("Autosomal dominant Robinow syndrome 1")
- **Related dominant entries:** OMIM #616331 (DRS2/DVL1), #616894 (DRS3/DVL3)
- **Related recessive entries:** OMIM #268310 (RRS1/ROR2)

**Synonyms:** Robinow syndrome, dominant type; Fetal face syndrome; Mesomelic dwarfism, Robinow type; Robinow-Silverman-Smith syndrome (historic).

**Evidence basis:** Robinow syndrome information is derived overwhelmingly from **aggregated, curated disease-level resources** (OMIM, GeneReviews, Orphanet) built from an accumulation of published case reports and small case series — the disease is too rare for large EHR-derived cohort data. Fewer than 80 dominant-Robinow-syndrome families have been reported across all three dominant genes combined ([GeneReviews NBK268648](https://www.ncbi.nlm.nih.gov/books/NBK268648/)); Orphanet estimates prevalence <1/1,000,000 for the dominant form with roughly 100 cases reported in the literature ([Orphanet ORPHA:3107](https://www.orpha.net/en/disease/detail/3107)).

**Suggested MONDO/HPO grounding:** MONDO term for the WNT5A subtype should map to OMIM:180700/DOID:0060766/ORPHA:3107.

---

## 2. Etiology

### Disease Causal Factor
DRS1 is caused by **heterozygous, typically de novo, missense variants (and in-frame duplications/deletion-duplications) in WNT5A**, which encodes the non-canonical Wnt ligand WNT5A ([Person et al. 2010, *Dev Dyn*, PMID:19918918](https://pubmed.ncbi.nlm.nih.gov/19918918/)). Person et al. identified two distinct missense substitutions of highly conserved cysteine residues in WNT5A — one found in all living affected members of Robinow's original family, another in a second unrelated proband — both of which caused **decreased WNT5A activity** in zebrafish and *Xenopus* functional assays.

### Genetic Risk Factors
- **Causal variants:** Missense substitutions affecting conserved cysteines and other residues clustering on one face of the WNT5A protein (modeled on WNT8 homology), thought to disrupt protein-protein interactions within the Wnt pathway rather than gross folding ([GeneReviews NBK268648](https://www.ncbi.nlm.nih.gov/books/NBK268648/)).
- The recurrent **p.Cys83Ser (C83S)** variant is the best-studied WNT5A allele. Its mechanism has been debated — dominant-negative, loss-of-function, or hypomorphic — but recent zebrafish/*Xenopus* and mouse chondrocyte-orientation work supports a **hypomorphic, non-dominant-negative** model in which the variant perturbs the spatial gradient of Wnt/PCP signaling rather than simply reducing total signal ([Human Molecular Genetics, 2019](https://academic.oup.com/hmg/article/28/14/2395/5427033); [Research Square 2025 preprint](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12776500/)).
- ~9.5% of clinically diagnosed Robinow syndrome cases overall are attributable to WNT5A missense variants, per cohort sequencing studies ([WNT Signaling Perturbations Underlie the Genetic Heterogeneity of Robinow Syndrome, *AJHG*](https://www.sciencedirect.com/science/article/pii/S0002929717304226)).
- **De novo occurrence:** Approximately half of all ADRS cases (across genes) arise de novo; the remainder are inherited from an affected, mildly-expressing parent ([GeneReviews NBK268648](https://www.ncbi.nlm.nih.gov/books/NBK268648/)).

### Environmental Risk Factors
None established. This is a monogenic Mendelian disorder with no known environmental, infectious, or lifestyle contributory factors identified in the literature.

### Protective Factors
None reported (genetic or environmental) — not applicable to this monogenic dominant disorder.

### Gene-Environment Interactions
Not established or investigated; the disorder's severity and penetrance appear driven by variant-specific effects on WNT5A protein function (genotype), not by external modifiers.

---

## 3. Phenotypes

### Craniofacial ("fetal facies")
- Broad, prominent forehead / frontal bossing — **HP:0011220** (Prominent forehead)
- Hypertelorism — **HP:0000316**
- Prominent, widely spaced eyes — **HP:0000488** / **HP:0000316**
- Short, upturned nose with depressed/wide nasal bridge — **HP:0000407** / **HP:0000431**
- Midface hypoplasia / midface retrusion — **HP:0011800**
- Broad, triangular mouth — **HP:0000175** (Bifid uvula) not applicable; use **HP:0002000** (Short columella) / free text
- Macrocephaly (often present prenatally, persisting postnatally) — **HP:0000256**
- Micrognathia in some — **HP:0000347**
- Cleft lip/palate (minority) — **HP:0000175** / **HP:0000202**

### Dental/Oral
- Malocclusion — **HP:0000689**
- Dental crowding — **HP:0000678**
- Hypodontia — **HP:0000668**
- Delayed eruption of permanent teeth — **HP:0000684**
- Gingival hypertrophy — **HP:0000212**
- Bifid/bilobed tongue — **HP:0010297**

### Skeletal
- Short stature, typically ≤ −2 SD in adults — **HP:0004322**
- **Mesomelic limb shortening**, predominantly upper limbs (forearms) — **HP:0003027**
- Brachydactyly — **HP:0001156**
- Clinodactyly — **HP:0030084**
- Hemivertebrae — **HP:0002937**
- Scoliosis — **HP:0002650**
- Radial head dislocation (minority) — **HP:0003083**
- Broad thumbs/first toes reported in some subtypes — **HP:0011304**

### Genital/Urogenital
- Males: micropenis / webbed or buried penis — **HP:0000054**; hypoplastic scrotum — **HP:0000047**; cryptorchidism — **HP:0000028**
- Females: hypoplastic clitoris and labia majora — **HP:0000053**
- Renal anomalies (minority, <25%) — **HP:0000077**

### Cardiac and Other
- Congenital cardiac defects (minority but "a major cause of morbidity and mortality" when present) — **HP:0001627**
- Nail dysplasia — **HP:0008404**
- Hearing loss (more classically reported with DVL1/DRS2) — **HP:0000365**
- Cognitive delay — rare — **HP:0001256**

**Onset/course:** Congenital; craniofacial "fetal face" gestalt is most striking in infancy/early childhood and becomes **less apparent with age**. Fetal ultrasound can detect mesomelic shortening and facial features by ~20 weeks gestation ([GeneReviews NBK268648](https://www.ncbi.nlm.nih.gov/books/NBK268648/)). The disease course is generally **stable/non-progressive** apart from scoliosis, which can worsen through growth. Severity is variable even within families carrying the same variant.

**Frequency data:** Cardiac defects, renal anomalies, radial head dislocation, vertebral defects, nail dysplasia, cleft lip/palate, and cognitive delay are each reported in **<25%** of cases; craniofacial, skeletal, dental, and genital features are near-penetrant/core diagnostic features.

**Quality of life:** No disease-specific QoL instrument was identified in the literature search; impact is inferred from surgical burden (orthopedic, dental, urogenital, cardiac interventions) and short stature. Cognitive function is typically normal, which is an important prognostic/QoL distinguishing feature versus the more severe recessive (ROR2) form.

---

## 4. Genetic/Molecular Information

**Causal gene:** WNT5A (HGNC:12784; NCBI Gene ID: 7474; Ensembl ENSG00000114251); OMIM gene entry *164975.

**Variant classes:** Predominantly **missense** substitutions (notably affecting conserved cysteine residues, e.g., p.Cys83Ser, p.Cys182Arg), plus **in-frame duplications** and **in-frame deletion-duplications** clustering on one face of the modeled WNT5A protein structure, implicating disrupted protein-protein interaction surfaces rather than global misfolding ([GeneReviews NBK268648](https://www.ncbi.nlm.nih.gov/books/NBK268648/); [Person et al. 2010, PMID:19918918](https://pubmed.ncbi.nlm.nih.gov/19918918/)).

**Variant classification (ACMG/ClinVar):** Reported WNT5A variants in Robinow syndrome are classified Pathogenic/Likely Pathogenic in ClinVar; sequence analysis detects the great majority of pathogenic variants (large deletions/duplications are not expected to be disease-relevant given the mechanism).

**Functional consequence:** Debated between **loss-of-function**, **dominant-negative**, and **hypomorphic** mechanisms; current evidence (zebrafish, *Xenopus*, and mouse Wnt5a-C83S knock-in chondrocyte-polarity studies) favors a **hypomorphic, gradient-disrupting** model rather than simple haploinsufficiency or classic dominant-negative antagonism ([HMG 2019](https://academic.oup.com/hmg/article/28/14/2395/5427033); [PMC12776500, 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12776500/)). Notably, this contrasts with the **DVL1/DVL3-associated forms (DRS2/DRS3)**, where all identified variants are heterozygous **frameshift mutations clustering in the penultimate/ultimate exon** (exon 14/15), producing truncated proteins that escape nonsense-mediated decay — consistent with a **gain-of-function** mechanism distinct from WNT5A's ([White et al. 2015, *AJHG*, PMID:25817016](https://pubmed.ncbi.nlm.nih.gov/25817016/); [Roifman et al. 2015, PMID:25817014, osteosclerotic DVL1-Robinow](https://pubmed.ncbi.nlm.nih.gov/25817014/)).

**Germline origin:** All reported DRS1 variants are germline (constitutional), inherited or de novo; no somatic/mosaic Robinow cohort data were identified.

**Modifier genes:** None formally established for DRS1; phenotypic variability within families with the same WNT5A variant suggests unidentified modifiers or stochastic developmental variation.

**Epigenetics:** No disease-specific epigenetic (DNA methylation/histone) data identified for WNT5A-Robinow syndrome in the literature searched.

**Chromosomal abnormalities:** Not a feature — DRS1 is a single-gene point-mutation disorder, not a copy-number/structural disorder.

**Suggested HGNC/gene term:** `hgnc:12784` (WNT5A).

---

## 5. Environmental Information

No environmental toxins, occupational exposures, radiation, or infectious agents are established contributors to DRS1 — it is a fully monogenic Mendelian disorder. No lifestyle/behavioral risk-modifying factors (smoking, diet, exercise) are documented in the literature. Not applicable: infectious agents.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathway
WNT5A is the prototypic ligand for **non-canonical Wnt signaling**, principally the **Wnt/Planar Cell Polarity (Wnt/PCP)** pathway, and can also modulate canonical (β-catenin-dependent) Wnt signaling depending on receptor context. WNT5A signals through the receptor tyrosine kinase **ROR2** (and related receptors) and downstream through **Disheveled (DVL1/DVL3)** as an obligate intracellular adaptor, activating small GTPases (RhoA, Rac1, Cdc42) and JNK signaling rather than β-catenin/TCF transcription ([GeneReviews NBK268648](https://www.ncbi.nlm.nih.gov/books/NBK268648/); [Mechanistic studies in Drosophila and chicken, DMM 2023, PMC10120075](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10120075/)). Suggested GO term: **GO:0035567** (non-canonical Wnt signaling pathway) / **GO:0060071** (Wnt signaling pathway, planar cell polarity pathway).

**Causal chain:** WNT5A ligand (reduced/altered activity due to missense variant) → diminished/dysregulated ROR2-mediated non-canonical Wnt signal transduction → impaired DVL-dependent PCP effector activation (Rho/Rac/JNK) → **loss of coordinated, polarized cell behavior** in developing tissues (chondrocyte columnar alignment, convergent-extension-like elongation movements) → **shortened, disorganized cartilage growth plates and abnormal skeletal elongation** (mesomelic limb shortening, short stature) plus disrupted craniofacial and genital morphogenesis.

### Cellular Processes
- **Chondrocyte planar polarity and columnar organization** in growth-plate cartilage is disrupted: WNT5A-C83S-expressing cartilage shows randomly oriented (rather than columnar) chondrocytes and diffuse (rather than polarized) Prickle protein localization, a direct readout of disrupted PCP ([Human Molecular Genetics 2019](https://academic.oup.com/hmg/article/28/14/2395/5427033); [Research Square/PMC12776500 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12776500/)).
- **Convergent-extension-like cell movements** required for axial elongation and limb bud patterning depend on non-canonical Wnt (Wnt5/Wnt11) signaling in vertebrate models; impaired Wnt5a signaling is analogous to zebrafish *pipetail* (*wnt5*) mutant phenotypes affecting gastrulation cell-shape and movement ([PMC1299299](https://pmc.ncbi.nlm.nih.gov/articles/PMC1299299/); general zebrafish CE literature).
- **Limb bud initiation, digit patterning, joint formation, limb rotation, and proximal-distal axis establishment** are all regulated by Wnt/PCP signaling gradients, explaining the mesomelic (mid-segment) predominance of limb shortening.

### Protein Dysfunction
WNT5A is a secreted, lipid-modified signaling glycoprotein. Disease variants cluster on a modeled protein surface implicated in receptor/co-receptor engagement, consistent with **altered protein-protein interaction** rather than global misfolding or complete loss of secretion.

### Tissue Damage / Organ-Level Mechanism
No classical oxidative-stress, ischemic, or fibrotic tissue-injury mechanism; pathology is **developmental/morphogenetic** rather than degenerative — abnormal patterning is established prenatally and is largely static postnatally (apart from progressive scoliosis in some).

### Comparative Genotype-Mechanism Note
This is a key mechanistic distinction curators should capture: **WNT5A (DRS1)** variants act through the **ligand** with a **hypomorphic/altered-signaling** effect, while **DVL1/DVL3 (DRS2/DRS3)** variants act through **downstream truncated adaptor proteins** with a putative **gain-of-function** effect — both converging on the same non-canonical Wnt/PCP pathway but via mechanistically distinct routes, which may explain phenotypic differences (e.g., osteosclerosis/increased bone density specifically associated with DVL1, cardiac defects more frequent with DVL3) ([GeneReviews NBK268648](https://www.ncbi.nlm.nih.gov/books/NBK268648/); [PMC10120075](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10120075/)).

### Craniofacial-Specific Mechanism
In mandibular development, abnormal WNT5A signaling has been shown to specifically cause **mandibular hypoplasia** through effects on neural-crest-derived skeletal precursors ([Hosseini-Farahabadi et al. 2017, *J Dent Res*](https://journals.sagepub.com/doi/abs/10.1177/0022034517716916)). Conditional mouse loss- vs. gain-of-function *Wnt5a* alleles produce **distinct, sometimes opposite craniofacial phenotypes** (loss-of-function: midface hypoplasia, hypertelorism trend; gain-of-function: macrocephaly, shortened hard palate, micrognathia), mirroring the phenotypic heterogeneity seen clinically across Robinow syndrome subtypes ([JBMR Plus 2024](https://academic.oup.com/jbmrplus/article/10/6/ziag060/8626061); [PMC12330612, 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12330612/)).

### Molecular Profiling / Omics
No large-scale transcriptomic, proteomic, metabolomic, or single-cell dataset specific to human WNT5A-Robinow syndrome tissue was identified; mechanistic insight instead derives from **model-organism functional assays** (zebrafish, *Xenopus*, chicken, *Drosophila*, mouse knock-in) rather than human -omics profiling — an important evidentiary caveat for curation (favor `evidence_source: MODEL_ORGANISM`/`IN_VITRO` for most mechanistic claims, `HUMAN_CLINICAL` only for phenotype/variant description).

**Suggested GO biological process terms:** GO:0035567 (non-canonical Wnt signaling pathway), GO:0060071 (PCP pathway), GO:0001501 (skeletal system development), GO:0060349 (bone morphogenesis).
**Suggested CL cell type terms:** CL:0000138 (chondrocyte), CL:0000058 (chondroblast).

---

## 7. Anatomical Structures Affected

**Organ level (primary):** Skeletal system (long bones — mesomelic segments; axial skeleton — vertebrae), craniofacial skeleton, external genitalia. **Secondary:** cardiovascular system (minority with structural heart defects), renal system (minority), dentition.

**Body systems:** Skeletal, craniofacial, genitourinary, and (variably) cardiovascular and renal systems — **UBERON**: limb (UBERON:0002101), forearm/mesomelic segment, vertebral column (UBERON:0001130), mandible (UBERON:0000926), external genitalia (UBERON:0000474), heart (UBERON:0000948), kidney (UBERON:0002113).

**Tissue/cell level:** Growth-plate **cartilage** (chondrocytes, CL:0000138) is the principal affected tissue — polarity/columnar organization defects there directly underlie the limb-shortening phenotype. Craniofacial neural-crest-derived skeletal precursors are also implicated ([Hosseini-Farahabadi 2017](https://journals.sagepub.com/doi/abs/10.1177/0022034517716916)).

**Subcellular:** WNT5A is a secreted glycoprotein (extracellular space, GO:0005615); receptor complex assembly occurs at the plasma membrane; downstream Disheveled (DVL1) acts in the cytoplasm as a scaffolding adaptor (GO:0005737).

**Localization/laterality:** Skeletal and craniofacial involvement is generally **bilateral/symmetric**; mesomelic shortening classically affects forearms more than legs.

---

## 8. Temporal Development

**Onset:** Congenital — features (mesomelic shortening, facial gestalt) are often visible on **prenatal ultrasound by ~20 weeks gestation** and are present at birth ([GeneReviews NBK268648](https://www.ncbi.nlm.nih.gov/books/NBK268648/)).

**Onset pattern:** Present from birth (not acute/insidious in the acquired-disease sense).

**Progression/course:** Largely **stable/non-progressive** developmental phenotype. The characteristic "fetal facies" gestalt is most pronounced in infancy and **becomes less distinctive with age**. Scoliosis (when hemivertebrae are present) can be progressive through growth and requires surveillance. Short stature persists into adulthood (typically ≤ −2 SD).

**Disease duration:** Chronic, lifelong condition; not self-limited.

**Remission patterns:** Not applicable (structural/developmental disorder, not a relapsing-remitting disease).

**Critical periods:** Prenatal skeletal and craniofacial morphogenesis (embryonic/fetal limb bud and branchial arch development) is the critical window during which WNT5A signaling perturbation produces the phenotype; postnatal management is chiefly supportive/corrective rather than preventive of primary pathology.

---

## 9. Inheritance and Population

**Epidemiology:** Robinow syndrome overall is very rare; approximately 200 cases have been reported cumulatively across dominant and recessive forms. For the **dominant form specifically**, Orphanet lists **~100 cases reported**, prevalence **<1/1,000,000**, equal male:female ratio, with cases described from the USA, Arab countries, Turkey, Czech Republic/Slovakia, the Indian subcontinent, and Brazil ([Orphanet ORPHA:3107](https://www.orpha.net/en/disease/detail/3107)). Fewer than 80 dominant-Robinow families total have been reported in the literature across all three known dominant genes (~8 WNT5A probands, ~18 DVL1, ~7 DVL3, per GeneReviews) ([GeneReviews NBK268648](https://www.ncbi.nlm.nih.gov/books/NBK268648/)).

**Inheritance pattern:** **Autosomal dominant.** Approximately 50% of cases are **de novo**; the remainder are inherited from an affected (often mildly expressing) parent, consistent with Robinow's original multi-generation family.

**Penetrance:** Appears high/complete for the core skeletal-craniofacial phenotype, though **expressivity is markedly variable** — severity differs even among relatives sharing the identical WNT5A variant (per Robinow's original family report).

**Genetic anticipation:** Not reported/established for WNT5A-Robinow syndrome (this is not a repeat-expansion disorder).

**Germline mosaicism:** Considered a theoretical possibility for recurrence in unaffected parents of a de novo proband; GeneReviews estimates sibling recurrence risk at roughly **~1%** in such cases, reflecting this low but non-zero mosaicism risk.

**Founder effects/consanguinity:** Not documented for the dominant WNT5A form (consanguinity and founder effects are more relevant to the **recessive** ROR2/NXN forms, which are enriched in certain consanguineous populations, e.g., Turkish, Middle Eastern, Omani cohorts — relevant differential/background context, not DRS1 itself).

**Carrier frequency:** Not applicable in the traditional sense (dominant disorder); population allele frequency of pathogenic WNT5A missense variants in gnomAD is expected to be essentially absent/private, consistent with a rare, largely de novo dominant disorder (specific gnomAD frequency data not retrieved in this search pass).

**Population demographics:** No specific ethnic enrichment established for WNT5A-associated DRS1; case reports span multiple continents/ethnicities as above. Sex ratio approximately 1:1.

---

## 10. Diagnostics

**Diagnostic criteria (GeneReviews):** Diagnosis established by **(1)** typical clinical findings (fetal facies, mesomelic limb shortening, genital hypoplasia ± vertebral/renal anomalies) and/or **(2)** identification of a heterozygous pathogenic variant in **DVL1, DVL3, or WNT5A** by molecular genetic testing ([GeneReviews NBK268648](https://www.ncbi.nlm.nih.gov/books/NBK268648/)).

**Molecular testing strategy:**
1. First-tier: sequence analysis of **DVL1 and DVL3** (the more commonly implicated genes), concurrently or sequentially
2. Reflex: **WNT5A** sequence analysis if DVL1/DVL3 negative
3. Alternative: multigene skeletal-dysplasia panel, or exome/genome sequencing
4. Detection rate: sequence analysis identifies >99% of pathogenic DVL1/DVL3 variants; deletion/duplication analysis is low-yield given the presumed gain-of-function mechanism for those genes.

**Imaging/clinical tests:**
- Skeletal radiographs (mesomelic long-bone shortening, hemivertebrae, brachydactyly)
- Prenatal ultrasound (limb shortening, facial features detectable ~20 weeks)
- Echocardiography (screen for congenital heart defects)
- Renal ultrasound (screen for renal anomalies)
- Dental/orthodontic and craniofacial evaluation
- Hearing assessment
- Developmental assessment

**Genetic testing modalities:** Single-gene sequencing (WNT5A), multigene panel (WNT5A + DVL1 + DVL3 + ROR2 + NXN + FZD2), or exome/genome sequencing. Chromosomal microarray/karyotype not diagnostically useful (point-mutation disorder). Prenatal molecular testing available once a familial variant is known.

**Differential diagnosis:**

| Condition | Distinguishing features |
|---|---|
| **ROR2-related (autosomal recessive) Robinow syndrome** | Biallelic ROR2 variants; more severe, higher rates of renal/cardiac/cognitive involvement, distal phalangeal clefting ([GeneReviews NBK1240](https://www.ncbi.nlm.nih.gov/books/NBK1240/)) |
| **NXN-related (autosomal recessive) Robinow syndrome** | Biallelic NXN variants; NXN normally stabilizes Disheveled proteins in the WNT5A-ROR2-DVL axis |
| **DVL3-related (DRS3)** | Frequent cardiac abnormalities; no osteosclerosis reported |
| **DVL1-related (DRS2)** | Distinctive macrocephaly (+2.5 to >+6 SD) with **osteosclerosis**/increased bone density, bilateral hearing loss |
| **Aarskog syndrome (X-linked)** | Shawl scrotum, widow's peak, ligamentous laxity, syndactyly; lacks mesomelic shortening |
| **Opitz G/BBB syndrome** | Higher rate of clefting (~50%), laryngotracheoesophageal defects; lacks mesomelic shortening |
| **Achondroplasia** | Rhizomelic (not mesomelic) shortening, trident hand, leg bowing |
| **FZD2-related Omodysplasia type 2** | Normal stature, rhizomelic shortening, no hypertelorism |
| **Smith-Lemli-Opitz syndrome** | Autosomal recessive cholesterol biosynthesis defect (DHCR7); 2-3 toe syndactyly, polydactyly, distinct biochemical (elevated 7-DHC) signature |

**Screening:** No population-based newborn screening exists (too rare); cascade family testing recommended once a familial variant is identified, given variable expressivity that may mean a "carrier" parent is only subtly affected.

---

## 11. Outcome/Prognosis

**Survival/mortality:** Life expectancy is generally considered **normal**, in marked contrast to some skeletal dysplasias, *except* when significant congenital cardiac defects are present — cardiac defects are explicitly described as "a major cause of morbidity and mortality" in ADRS when they occur ([GeneReviews NBK268648](https://www.ncbi.nlm.nih.gov/books/NBK268648/)).

**Morbidity/function:** Main long-term morbidity drivers are orthopedic (progressive scoliosis, limb-length/short stature issues), dental/orthodontic burden, and (for a minority) renal or cardiac complications. **Cognitive function is typically normal**, an important prognostic distinction from the recessive ROR2 form, which carries higher rates of developmental delay.

**Complications:** Progressive scoliosis from hemivertebrae, malocclusion requiring extensive orthodontic/surgical correction, cryptorchidism, hearing loss (more DVL1-associated), and — when present — structural cardiac lesions requiring surgical correction.

**Recovery/prognostic factors:** Prognosis correlates with **which organ systems are involved** (particularly cardiac and renal) more than with limb/facial severity per se; genotype (WNT5A vs. DVL1 vs. DVL3) is associated with somewhat different complication profiles (see Section 6/10).

**Pregnancy:** "Pregnancy in affected women appears to be generally uncomplicated," though cesarean delivery may be needed for abnormal fetal presentation or cephalopelvic disproportion related to maternal skeletal anatomy ([GeneReviews NBK268648](https://www.ncbi.nlm.nih.gov/books/NBK268648/)).

---

## 12. Treatment

There is **no disease-modifying/curative therapy**; management is multidisciplinary and manifestation-directed.

**Pharmacotherapy:**
- **Recombinant human growth hormone (rhGH)** has been used in children with Robinow syndrome, particularly with documented growth hormone deficiency, with reported significant increase in growth velocity (case example: 0.7 U/kg/week starting at age 4, height rising from <1st to 44th percentile) ([Robinow syndrome and its response to growth hormone treatment, PMID:36917807](https://pubmed.ncbi.nlm.nih.gov/36917807/); [PMID:10417975](https://pubmed.ncbi.nlm.nih.gov/10417975/)). Suggested NCIT term: `NCIT:C15986` (Pharmacotherapy) with a specific growth-hormone therapeutic agent.
- Hormonal therapy (hCG/testosterone) for micropenis in affected males — `NCIT:C15986`.

**Surgical/Interventional:**
- Craniofacial team surgical correction of cleft lip/palate — `NCIT:C15329` (Surgical Procedure)
- Orthopedic surgery for severe scoliosis (hemivertebral/costal anomalies), syndactyly — `NCIT:C16186` (Orthopedic Surgical Procedure)
- Orchidopexy for cryptorchidism; urological correction for anomalous penile insertion — `NCIT:C15329`
- Standard cardiothoracic surgical management for congenital heart defects when present

**Supportive/rehabilitative:**
- Orthodontic treatment for malocclusion/crowding — `NCIT:C15302`-adjacent dental care code, or general therapeutic procedure
- Bracing, casting, physical therapy as first-line for musculoskeletal issues before surgery is considered — `NCIT:C15302` (Physical Therapy)
- Hearing intervention (amplification) for documented hearing loss
- Genetic counseling — `NCIT:C15240`

**Experimental/advanced therapeutics:** No gene therapy, RNA-based therapy, or targeted molecular therapy specific to WNT5A-Robinow syndrome was identified in the literature searched; this remains a management-only (not mechanism-correcting) treatment landscape at present. No relevant ClinicalTrials.gov interventional trials specific to DRS1 were surfaced in this search.

**Treatment strategy/surveillance schedule** (per GeneReviews):
- Craniofacial/dental evaluation every 6–12 months
- Developmental assessment at each visit through childhood/adolescence
- Cardiac and renal monitoring if abnormalities identified at baseline
- Regular head-circumference measurement in infancy/childhood

---

## 13. Prevention

**Primary prevention:** Not applicable in the classic sense (monogenic disorder); the only "primary prevention" avenue is **reproductive genetic counseling and prenatal/preimplantation genetic testing** once a familial WNT5A variant is identified.

**Secondary prevention (early detection):** Prenatal ultrasound can detect the mesomelic limb-shortening and craniofacial phenotype from ~20 weeks gestation in at-risk pregnancies, enabling early postnatal multidisciplinary planning ([GeneReviews NBK268648](https://www.ncbi.nlm.nih.gov/books/NBK268648/)).

**Tertiary prevention:** Scheduled surveillance (craniofacial, cardiac, renal, developmental, scoliosis) is aimed at preventing/mitigating secondary complications rather than the primary skeletal dysplasia itself.

**Genetic counseling:** Central to prevention/family planning — 50% recurrence risk to offspring of an affected parent; ~1% empiric recurrence risk to siblings of a de novo proband (accounting for possible parental germline mosaicism); prenatal and preimplantation genetic testing available once the familial variant is known.

**Screening:** No population-level screening program exists given the extreme rarity; family cascade testing is the operative screening paradigm.

**Immunization/infectious prophylaxis:** Not applicable — non-infectious etiology.

---

## 14. Other Species / Natural Disease

**Taxonomy of affected species used in models:** *Danio rerio* (zebrafish, NCBITaxon:7955), *Xenopus laevis* (NCBITaxon:8355), *Gallus gallus* (chicken, NCBITaxon:9031), *Drosophila melanogaster* (NCBITaxon:7227), *Mus musculus* (mouse, NCBITaxon:10090).

**Naturally occurring disease in other species:** A **DVL1-related Robinow syndrome phenotype has been documented in chicken (*Gallus gallus*)**, catalogued in OMIA as **OMIA:002654-9031** ([OMIA](https://omia.org/OMIA002654/9031/)) — this is the DVL1 (DRS2) ortholog rather than WNT5A/DRS1 specifically, but is relevant comparative context within the same gene family/pathway. No naturally occurring WNT5A-specific Robinow phenotype in a companion-animal or veterinary population was identified in this search (contrast with the well-documented naturally occurring **ROR2-related "brachycephalic/mesomelic dwarfism" in some cattle and dog breeds**, which is a separate ROR2-pathway veterinary correlate worth checking OMIA directly if curating comparative content).

**Orthologous gene:** WNT5A is highly conserved across vertebrates; mouse *Wnt5a*, zebrafish *wnt5b* (a paralog performing an analogous non-canonical signaling role), chicken *WNT5A*, and *Xenopus Wnt5a* orthologs are all used experimentally (see Section 15).

**Comparative pathology:** Across species, loss or dysregulation of Wnt5a/non-canonical Wnt signaling produces convergent phenotypes of shortened/disorganized body axis, disrupted convergent-extension gastrulation movements, and craniofacial/limb skeletal patterning defects — indicating strong evolutionary conservation of the underlying PCP mechanism (see zebrafish *pipetail* mutant, PMC1299299).

**Zoonotic potential:** Not applicable — this is a developmental/genetic disorder, not a transmissible disease.

---

## 15. Model Organisms

| Model | Type | Key findings |
|---|---|---|
| **Mouse *Wnt5a* germline knockout** | Genetic (knockout), mammalian | Non-viable beyond birth; embryos show major shortening of the body axis, appendicular skeleton, and jaws, with disrupted chondrocyte polarity — directly recapitulating limb-shortening and craniofacial pathology (general Wnt5a knockout literature; [Bone Research overview](https://www.nature.com/articles/boneres20134)) |
| **Mouse *Wnt5a*-C83S knock-in** | Genetic (patient-variant knock-in), mammalian | Models the recurrent human C83S allele; shows spatially disorganized/randomized chondrocyte alignment and diffuse Prickle localization in cartilage, directly linking the human variant to PCP disruption ([HMG 2019](https://academic.oup.com/hmg/article/28/14/2395/5427033); [PMC12776500, 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12776500/)) |
| **Mouse conditional *Wnt5a* loss- and gain-of-function (craniofacial/bone-specific)** | Genetic, conditional, mammalian | Produces distinct, sometimes opposite craniofacial phenotypes (LOF: midface hypoplasia/hypertelorism; GOF: macrocephaly, shortened palate, micrognathia), modeling the phenotypic heterogeneity seen across human Robinow subtypes ([JBMR Plus 2024](https://academic.oup.com/jbmrplus/article/10/6/ziag060/8626061); [PMC12330612](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12330612/)) |
| **Zebrafish (*Danio rerio*) WNT5A functional assay** | Genetic/induced, non-mammalian vertebrate | Person et al. used zebrafish assays to demonstrate that both identified WNT5A missense variants cause **decreased WNT5A activity** ([PMID:19918918](https://pubmed.ncbi.nlm.nih.gov/19918918/)); *pipetail* (*wnt5*) mutants show classic convergent-extension gastrulation defects analogous to disrupted PCP signaling |
| ***Xenopus laevis* WNT5A overexpression/functional assay** | Genetic/induced, non-mammalian vertebrate | Used alongside zebrafish to confirm reduced signaling activity of disease variants ([PMID:19918918](https://pubmed.ncbi.nlm.nih.gov/19918918/)) |
| **Chicken (*Gallus gallus*) DVL1 mechanistic model** | Genetic/induced, avian | Used with *Drosophila* to dissect DVL1 mechanism (loss of canonical β-catenin signaling with gain of non-canonical JNK/PCP signaling) — DRS2 pathway-comparator, catalogued as naturally-relevant in OMIA:002654-9031 ([DMM 2023, PMC10120075](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10120075/)) |
| ***Drosophila melanogaster* DVL1-variant wing/disease model** | Genetic, invertebrate | Expression of patient-derived DVL1 variants causes major disorganization of wing morphology versus wild-type, supporting a gain-of-function/PCP-disruption mechanism transferable conceptually to the WNT5A pathway ([bioRxiv 2024.09.10.612347](https://www.biorxiv.org/content/10.1101/2024.09.10.612347v1.full); [Developmental Dynamics 2025](https://anatomypubs.onlinelibrary.wiley.com/doi/full/10.1002/dvdy.70056)) |

**Model limitations:** No model fully recapitulates the complete human multi-organ phenotype (craniofacial + skeletal + genital + cardiac + renal) simultaneously; mouse germline *Wnt5a* nulls are **non-viable**, limiting study of postnatal/adult phenotype, which is why **knock-in (patient-variant) and conditional models** have become the preferred tools for modeling the milder, viable human dominant phenotype. Non-mammalian models (zebrafish, *Xenopus*, chicken, *Drosophila*) are valuable for rapid functional variant classification (gain vs. loss of function) but cannot model human-specific structures (dentition, genital anatomy) or long-term skeletal growth-plate biology as faithfully as mammalian systems.

**Applications:** These models collectively support (1) variant functional classification (pathogenic missense vs. benign), (2) mechanistic dissection of canonical-vs-non-canonical Wnt pathway involvement, (3) chondrocyte planar-polarity read-outs as a cellular biomarker of pathogenicity, and (4) comparative dissection of WNT5A (ligand-level, hypomorphic) versus DVL1/DVL3 (adaptor-level, gain-of-function) disease mechanisms within the same overall pathway.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested term(s) |
|---|---|
| Disease | OMIM:180700, DOID:0060766, ORPHA:3107 |
| Causal gene | hgnc:12784 (WNT5A) |
| Pathway/BP | GO:0035567 (non-canonical Wnt signaling), GO:0060071 (Wnt/PCP pathway), GO:0001501 (skeletal system development) |
| Cell type | CL:0000138 (chondrocyte) |
| Anatomy | UBERON:0002101 (limb), UBERON:0001130 (vertebral column), UBERON:0000926 (mandible), UBERON:0000474 (external genitalia) |
| Key phenotypes | HP:0003027 (mesomelic limb shortening), HP:0004322 (short stature), HP:0000316 (hypertelorism), HP:0000256 (macrocephaly), HP:0002937 (hemivertebrae), HP:0001156 (brachydactyly), HP:0000054 (micropenis), HP:0001627 (abnormal heart morphology) |
| Treatment | NCIT:C15986 (Pharmacotherapy — GH, hCG/testosterone), NCIT:C16186 (Orthopedic Surgical Procedure), NCIT:C15302 (Physical Therapy), NCIT:C15329 (Surgical Procedure), NCIT:C15240 (Genetic Counseling) |

---

## Notable Evidence Gaps for Curators
1. **DRS1 (WNT5A) is under-represented in recent mechanistic literature relative to DRS2/DRS3 (DVL1/DVL3)** — most 2023–2025 primary mechanistic papers found in this search (Drosophila, chicken, zebrafish DVL work) concern DVL1/DVL3, not WNT5A directly; WNT5A mechanistic evidence is mostly from Person et al. 2010 plus the C83S knock-in mouse line (2019, 2025).
2. No human transcriptomic/proteomic/single-cell dataset specific to WNT5A-Robinow patient tissue was located — mechanistic claims should be sourced as `MODEL_ORGANISM`/`IN_VITRO`, not `HUMAN_CLINICAL`.
3. Exact PMID for the original 1969 Robinow, Silverman & Smith description was not resolved via search (pre-PubMed-indexing era article); if required for citation, retrieve directly from *Am J Dis Child* 1969;117:645–651 via a library/DOI lookup rather than PubMed search.
4. No NCT-registered interventional trial specific to DRS1/WNT5A-Robinow syndrome was identified.

Sources: [OMIM #180700](https://omim.org/entry/180700) · [OMIM #616331](https://www.omim.org/entry/616331) · [OMIM #616894](https://www.omim.org/entry/616894) · [GeneReviews — Autosomal Dominant Robinow Syndrome (NBK268648)](https://www.ncbi.nlm.nih.gov/books/NBK268648/) · [GeneReviews — ROR2-Related Robinow Syndrome (NBK1240)](https://www.ncbi.nlm.nih.gov/books/NBK1240/) · [Orphanet ORPHA:3107](https://www.orpha.net/en/disease/detail/3107) · [Person et al. 2010, Dev Dyn, PMID:19918918](https://pubmed.ncbi.nlm.nih.gov/19918918/) · [White et al. 2015, AJHG, PMID:25817016](https://pubmed.ncbi.nlm.nih.gov/25817016/) · [Roifman et al. 2015, PMID:25817014](https://pubmed.ncbi.nlm.nih.gov/25817014/) · [Human Molecular Genetics 2019 — WNT5A-C83S dominant interference](https://academic.oup.com/hmg/article/28/14/2395/5427033) · [PMC12776500 — Wnt5a-C83S knock-in chondrocyte polarity 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12776500/) · [PMC10120075 — DVL1 mechanistic studies in Drosophila/chicken](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10120075/) · [JBMR Plus 2024 — Wnt5a gain/loss-of-function craniofacial bone](https://academic.oup.com/jbmrplus/article/10/6/ziag060/8626061) · [PMC12330612](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12330612/) · [Hosseini-Farahabadi et al. 2017, J Dent Res](https://journals.sagepub.com/doi/abs/10.1177/0022034517716916) · [Robinow syndrome and growth hormone treatment, PMID:36917807](https://pubmed.ncbi.nlm.nih.gov/36917807/) · [PMID:10417975](https://pubmed.ncbi.nlm.nih.gov/10417975/) · [OMIA:002654-9031 (chicken DVL1-related Robinow)](https://omia.org/OMIA002654/9031/) · [Disease Ontology DOID:0060766](https://informatics.jax.org/disease/180700)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.