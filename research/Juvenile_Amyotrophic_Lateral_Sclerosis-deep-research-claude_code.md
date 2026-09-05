---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-20T13:47:36.213598'
end_time: '2026-08-20T13:53:31.472324'
duration_seconds: 355.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Juvenile Amyotrophic Lateral Sclerosis
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
  web_search_requests: 14
  num_turns: 21
  total_cost_usd: 2.1385019
  session_id: 8e4fd1dc-e86d-5f10-b20a-5d834583d85f
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 53
reference_validation:
  total_references: 37
  verified: 37
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 4
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:28054830
  - PMID:34946884
  - PMC:PMC5841203
  relevance_assessed: 37
  on_topic: 23
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Juvenile Amyotrophic Lateral Sclerosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Juvenile Amyotrophic Lateral Sclerosis** covering all of the
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

I'll research Juvenile Amyotrophic Lateral Sclerosis (JALS) across genetics, phenotype, mechanism, and clinical management, then compile a comprehensive report.

# Juvenile Amyotrophic Lateral Sclerosis (JALS): Comprehensive Research Report

## 1. Disease Information

### Overview
Juvenile amyotrophic lateral sclerosis (JALS) is a clinically and genetically heterogeneous group of motor neuron disorders defined operationally by **symptom onset before age 25 years**, involving progressive degeneration of both upper motor neurons (UMN, corticospinal tract) and lower motor neurons (LMN, anterior horn cells/bulbar nuclei). It is distinguished from adult-onset ALS (AO-ALS) by three major features, as summarized in the principal review of the field:
1. A markedly higher genetic yield — **~40% of JALS cases have an identifiable causative gene mutation, versus ~10% of AO-ALS cases**
2. A highly variable disease course, "from very aggressive to a more indolent" trajectory, in contrast to the relatively uniform ~2–3 year mortality of typical AO-ALS
3. A greater propensity for syndromic, multi-system neurodegeneration extending beyond the motor system (cognitive, cerebellar, sensory, or movement-disorder features), whereas AO-ALS is comparatively restricted to motor pathways
(Ghasemi & Brown/JALS review, *Genes* 2021, PMID: [34946884](https://pmc.ncbi.nlm.nih.gov/articles/PMC8701111/))

### Key Identifiers
| Resource | Identifier |
|---|---|
| MONDO | MONDO:0017593 |
| Orphanet | ORPHA:300605 (Juvenile amyotrophic lateral sclerosis); related: ORPHA:247604 (Juvenile primary lateral sclerosis); ORPHA:357043 (ALS type 4) |
| OMIM | #205100 (ALS2, juvenile ALS due to ALS2/alsin); #602433 (ALS4, SETX); #105400 (ALS1 umbrella entry, SOD1) |
| GARD (NIH) | GARD:11901 |

### Synonyms / Alternative Names
- Juvenile-onset amyotrophic lateral sclerosis (jALS)
- Early-onset ALS
- Pediatric ALS
- Gene-specific eponymous forms: ALS2 (juvenile ALS-2), ALS4 (SETX/senataxin-related juvenile ALS), ALS16 (SIGMAR1-related)
- Overlapping allelic disorders at the ALS2 locus: infantile-onset ascending hereditary spastic paralysis (IAHSP), juvenile primary lateral sclerosis (JPLS)

### Data provenance
Nearly all quantitative epidemiologic data on JALS derive from **aggregated, registry- or literature-level sources** — principally the US CDC National ALS Registry (44 confirmed/likely juvenile cases identified 2010–2018) and pooled case-series/case-report literature reviews — rather than large prospective individual-patient cohorts, reflecting the disease's rarity (Larkin et al., *Amyotroph Lateral Scler Frontotemporal Degener* 2023, PMID: [37789566](https://pmc.ncbi.nlm.nih.gov/articles/PMC11299517/)).

---

## 2. Etiology

### Disease Causal Factors
JALS is primarily a **monogenic/oligogenic disorder** in the ~40% of cases with an identified mutation; the remainder are presumed sporadic/idiopathic or due to as-yet-unidentified genetic causes. Fifteen genes have been reported in association with JALS, though only three — **FUS, SETX, and ALS2** — are recurrently implicated across multiple independent families, with the rest supported by single or few case reports (PMID: 34946884).

### Genetic Risk/Causal Factors (by gene; see Section 4 for full detail)
- **FUS** (fused in sarcoma) — most frequently implicated gene in JALS; predominantly *de novo* mutations
- **SETX** (senataxin) — the only recurrent **autosomal dominant** JALS gene (ALS4)
- **ALS2** (alsin) — autosomal recessive; historically enriched in North African/Middle Eastern consanguineous families
- **SIGMAR1** (sigma-1 receptor) — autosomal recessive, very early (infantile) onset
- **SOD1** — rare in JALS (3 reported cases), typically *de novo*, distinct mutation spectrum from AO-ALS SOD1
- **SPTLC1** — mostly *de novo*; one autosomal dominant family
- **SPG11** — autosomal recessive
- **UBQLN2** — X-linked dominant
- **ERLIN1, GNE, TARDBP, VRK1, SYNE1, BICD2, DDHD1** — single-family/case reports (PMID: 34946884)

### Environmental Risk Factors
No well-established environmental or occupational risk factors specific to JALS have been identified in the literature reviewed; environmental risk factor research in ALS overall (e.g., military service, heavy metal exposure, smoking, physical trauma) is concentrated in adult-onset, largely sporadic disease and has not been systematically studied in the pediatric/juvenile population. This is a **notable evidence gap**.

### Protective Factors
No specific genetic or environmental protective factors for JALS are documented in the literature surveyed. General population variant-frequency data (e.g., gnomAD) for the causal genes have not been reported as conferring disease protection.

### Gene–Environment Interactions
Not established for JALS specifically; the disease is modeled overwhelmingly as monogenic with variable expressivity/penetrance (e.g., SETX-ALS4 shows sex-dependent penetrance — see Section 9) rather than as a gene–environment interaction disorder.

---

## 3. Phenotypes

### Core Motor Phenotype
- **Progressive muscle weakness and atrophy** (LMN sign) — HPO: HP:0003324 (Generalized muscle weakness) / HP:0007358 (Progressive muscle weakness); HP:0003202 (Skeletal muscle atrophy)
- **Spasticity, hyperreflexia, extensor plantar responses** (UMN signs) — HPO: HP:0001257 (Spasticity), HP:0001347 (Hyperreflexia), HP:0003487 (Babinski sign)
- **Fasciculations** — HPO: HP:0002380
- **Dysarthria progressing to anarthria** (especially ALS2) — HPO: HP:0001260 (Dysarthria)
- **Dysphagia** — HPO: HP:0002015
- **Pseudobulbar affect** (ALS2) — HPO: HP:0000749

### Gene-Specific Phenotype Summary
| Gene | Onset pattern | UMN/LMN balance | Bulbar/respiratory | Distinctive features |
|---|---|---|---|---|
| FUS | Median 21 yrs; often bulbar onset | Combined | Frequent, early | Myoclonic jerks, tremor, occasional cognitive/frontal decline |
| SETX (ALS4) | Mean ~16 yrs, slow | Balanced, distal-predominant LMN | **Spared** | Finger-to-nose dysmetria/ataxia in ~50%; sex-dependent penetrance |
| ALS2 | Mean 4.9 yrs (1–20) | UMN-prominent early | Early, frequent (anarthria in 1st decade) | Pseudobulbar affect, scoliosis, preserved cognition |
| SIGMAR1 | 1–2 yrs | LMN (distal, forearm/hand) | Spared | Cognition preserved; overlaps distal HMN |
| SOD1 (JALS) | Late 2nd–early 3rd decade | Combined | Variable | Rapid, respiratory failure <2 yrs |
| SPTLC1 | 4–15 yrs | Mixed | Yes | Elevated serum ceramide |
| SPG11 | 7–23 yrs (2nd decade typical) | Balanced | Early/common | No cognitive impairment, no corpus callosum thinning (unlike HSP) |
| UBQLN2 | 16–24 yrs (rare juvenile cases) | Variable | Variable | Frontotemporal dementia common |
(All PMID: 34946884)

### Onset, Severity, Progression, Frequency
- **Age of onset:** ranges from infancy (SIGMAR1, ALS2) through the third decade (SOD1, TARDBP), with the operational upper bound at 25 years.
- **Severity/progression:** bimodal — rapidly fatal (FUS, SOD1: death from respiratory failure within 1–2 years) vs. slowly progressive over decades (SETX, ALS2, SPG11 [27–40 yr duration], UBQLN2 [~4 decades]) (PMID: 34946884).
- **Frequency of specific signs:** quantitative frequency data are limited to small case series; e.g., SETX-ALS4 penetrance is markedly sex-skewed (31% of males vs. 13% of females symptomatic) (PMID: 34946884; Grunseich et al., *Ann Neurol* 2020, [10.1002/ana.25681](https://onlinelibrary.wiley.com/doi/abs/10.1002/ana.25681)).

### Quality of Life
Disease-specific QoL instruments (EQ-5D, SF-36, ALSFRS-R-based QoL substudies) have been applied in adult ALS but are not reported as validated or systematically applied in pediatric/juvenile ALS in the literature surveyed. The functional impact is inferable from the clinical course: progressive loss of ambulation, speech, swallowing, and (in FUS/SOD1 forms) respiratory independence, with earlier and longer-duration disability in indolent forms (SETX, ALS2, SPG11) due to decades-long disease courses beginning in childhood/adolescence — a distinct QoL burden (loss of developmental milestones, prolonged pediatric-to-adult disability) compared with AO-ALS.

---

## 4. Genetic/Molecular Information

### Causal Genes (detailed)

**FUS** (Fused in Sarcoma; RNA-binding protein)
- Most common JALS gene; predominantly *de novo* heterozygous mutations, often clustered in the C-terminal nuclear localization signal (NLS) domain
- **P525L** mutation: consistently associated with the most severe/earliest-onset form (median onset 21 yrs), higher bulbar involvement, shortest survival (Waibel et al., *Neurology* 2010, PMID: [20668260](https://pubmed.ncbi.nlm.nih.gov/20668260/); Bäumer et al., PMID: [20668260](https://pubmed.ncbi.nlm.nih.gov/20668260/))
- De novo R503fs frameshift reported in a 17-year-old female with sporadic JALS, rapid course, death 15 months from onset (PMID: [32501131](https://pubmed.ncbi.nlm.nih.gov/32501131/))
- Y526C novel C-terminal mutation strengthens FUS as "the most frequent genetic factor in aggressive juvenile ALS" (PMID: [28054830](https://pubmed.ncbi.nlm.nih.gov/28054830/))
- FUS-P525L reported with intellectual disability and expanded phenotype (*Neurol Genet* 2024, [10.1212/NXG.0000000000200009](https://www.neurology.org/doi/10.1212/NXG.0000000000200009))
- **Neuropathology:** cytoplasmic basophilic inclusions in Betz cells of motor cortex, with 12–15 nm tubulofilamentous ultrastructure — distinct from the TDP-43 pathology of sporadic ALS (PMID: 34946884)

**SETX** (Senataxin; DNA/RNA helicase, ALS4)
- Autosomal dominant, gain-of-function heterozygous mutations (chr 9q34); the only recurrent AD gene in JALS
- Series of 31 patients: mean onset 16 years, slowly progressive, normal life span (PMID: 34946884; Grunseich 2020)
- Allele-specific silencing of a dominant SETX mutation as a therapeutic strategy is under preclinical investigation (bioRxiv 2024, [10.1101/2024.10.11.617871](https://www.biorxiv.org/content/10.1101/2024.10.11.617871.full.pdf))
- SETX also causes the allelic disorder ataxia with oculomotor apraxia type 2 (AOA2, recessive), with ALS4 mutations occurring at distinct SETX protein locations from AOA2 mutations (PMID: 34946884)

**ALS2** (Alsin; Rho guanine nucleotide exchange factor, chr 2q33)
- Autosomal recessive; loss-of-function (often nonsense/frameshift, premature stop codon) mutations distributed across the gene with no hotspot
- Encodes a ~180–185 kDa multidomain protein with three GEF domains for Rab5 and other small GTPases (PMID: 34946884)
- Allelic spectrum: infantile-onset ascending hereditary spastic paralysis (IAHSP) → juvenile primary lateral sclerosis (JPLS) → juvenile ALS2, representing a phenotypic continuum of severity (PMC: [4180207](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4180207/); PMC: [8721836](https://pmc.ncbi.nlm.nih.gov/articles/PMC8721836/))
- Novel splice-site ALS2 mutation reported establishing diagnosis in a family with early anarthria and generalized dystonia (PMC: [4256290](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4256290/))

**SIGMAR1** (Sigma-1 receptor; ER chaperone, ALS16)
- Autosomal recessive; onset 1–2 years; distal (forearm/hand) LMN-predominant, spared bulbar/respiratory function, preserved cognition
- Also causes a distinct allelic phenotype, distal hereditary motor neuropathy (dHMN), without the rapid progression/widespread neurogenic damage typical of ALS (ScienceDaily 2011, [link](https://www.sciencedaily.com/releases/2011/08/110812091545.htm); PMID: 34946884; PMC: [6060428](https://pmc.ncbi.nlm.nih.gov/articles/PMC6060428/); PMC: [12041004](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12041004/))

**SOD1** (Cu/Zn superoxide dismutase 1)
- Only 3 reported JALS cases; predominantly de novo, distinct mutation spectrum and inheritance pattern from typical AO-ALS SOD1 (usually AD, mean onset 5th decade)
- Rapid progression, death from respiratory failure <2 years; neuropathology shows anterior horn degeneration with Bunina bodies and gliosis (PMID: 34946884)

**SPTLC1** (Serine palmitoyltransferase long-chain base subunit 1)
- Mostly de novo (one AD family); onset 4–15 years; catalyzes the rate-limiting step of de novo sphingolipid synthesis; elevated serum ceramide (distinct from the elevated deoxysphingolipids seen in SPTLC1-associated HSAN)
- One patient trialed serine supplementation, which produced weight gain but uncertain disease benefit and theoretical risk of worsening sphingolipid overproduction (PMID: 34946884)

**SPG11** (Spatacsin)
- Autosomal recessive; onset 7–23 years (2nd decade typical); "SPG11-ARJALS" clinically distinguished from SPG11-hereditary spastic paraplegia (HSP) by absence of cognitive impairment and absence of corpus callosum thinning on MRI (Orhan et al., *Neurol Genet* 2016, [10.1212/NXG.0000000000000025](https://www.neurology.org/doi/10.1212/NXG.0000000000000025); PMID: 34946884)

**UBQLN2** (Ubiquilin 2)
- X-linked dominant; mutations cluster in the PXX domain; regulates ubiquitinated protein degradation; frequently associated with frontotemporal dementia (PMID: 34946884)

**Other single-case/single-family genes:** ERLIN1 (Turkish family, homozygous, ER lipid-raft protein), GNE (sialic acid synthesis), TARDBP (p.Gly348Val, one JALS case), VRK1 (kinase, with sensory neuropathy and intellectual deterioration), SYNE1 (nuclear envelope–actin linker), BICD2 (motor adaptor protein), DDHD1 (mitochondrial phospholipase) (all PMID: 34946884).

### Variant Classification & Population Frequency
Systematic gnomAD/ClinVar-level population-frequency and ACMG/AMP classification data specific to JALS-causing variants were not comprehensively retrieved in this search; individual variants (e.g., FUS P525L, SETX L389S/R2136H) are reported as pathogenic/likely pathogenic in the primary literature and ClinGen curations (see ClinGen Gene-Disease Validity records for SETX/ALS4).

### Somatic vs. Germline
All reported JALS-causing variants are **germline** (constitutional), including de novo germline events in FUS, SOD1, and SPTLC1 forms.

### Functional Consequences
- **FUS:** gain-of-toxic-function via cytoplasmic mislocalization, aberrant U1 snRNA interaction, and stress granule incorporation (see Section 6)
- **SETX:** gain-of-function affecting R-loop resolution and TGF-β pathway activation
- **ALS2:** loss-of-function (GEF activity loss) affecting Rab5-dependent endosomal trafficking
- **SIGMAR1:** loss-of-function affecting ER chaperone activity

### Epigenetic / Chromosomal Information
No JALS-specific epigenetic (DNA methylation/histone) or large-scale chromosomal abnormality (aneuploidy/translocation) mechanisms were identified in the literature surveyed; JALS is modeled as point mutation/small indel-driven monogenic disease.

---

## 5. Environmental Information

No JALS-specific environmental toxin, occupational, lifestyle, or infectious-agent risk factors were identified in the literature surveyed. This contrasts with adult sporadic ALS, where environmental epidemiology (e.g., military deployment, heavy metals, pesticides, β-N-methylamino-L-alanine/BMAA) is more extensively studied but still not disease-defining. No infectious trigger has been established for JALS. This represents a clear knowledge gap suitable for flagging as `KNOWLEDGE_GAP` in a curated entry.

---

## 6. Mechanism / Pathophysiology

### Causal Chains by Gene

**FUS pathway:** *De novo* NLS-domain mutation → impaired nuclear import of FUS protein → cytoplasmic mislocalization of FUS in motor neurons → incorporation into stress granules (co-localizing with TIAR) and aberrant trapping of U1 snRNP biogenesis intermediates via aberrant Sm-site zinc-finger interaction with U1 snRNA → disrupted RNA metabolism/splicing and pathological stress-granule dynamics (shift to unstructured, AU-rich transcriptome) → dose-dependent gain of toxic function, RBP insolubility → progressive motor neuron loss (in FUS-P525L knock-in mice, ~30% lumbar motor neuron loss by 12 months and 37% NMJ denervation by 1 year) without obligate cytoplasmic aggregate formation → denervation, weakness, bulbar dysfunction, respiratory failure.
Sources: Vance et al. (PMID: [20699327](https://pubmed.ncbi.nlm.nih.gov/20699327/)); Sun et al. (PMC: [7733473](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7733473/)); PMC: [7705167](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7705167/); ALZFORUM hFUS-P525L model summary.

**SETX (ALS4) pathway:** Heterozygous gain-of-function SETX mutation (helicase domain, e.g., L389S, R2136H) → impaired DNA/RNA helicase function and R-loop resolution → genomic instability (altered Rad51 recruitment), dysregulated transcriptional termination, and TGF-β pathway activation → downstream **TDP-43 nuclear clearing and cytoplasmic mislocalization** in spinal motor neurons (both in knock-in mouse models and human ALS4 postmortem tissue) → nucleocytoplasmic transport dysfunction (Ran/RanGAP1 nuclear-membrane abnormalities, delayed nuclear import) and enhanced stress granule formation → autophagy dysregulation → slowly progressive distal LMN degeneration with UMN signs, sparing bulbar/respiratory neurons.
Source: Bennett et al., *Acta Neuropathol* 2018, PMID: [29725819](https://pubmed.ncbi.nlm.nih.gov/29725819/); PMID: 34946884.

**ALS2 (alsin) pathway:** Biallelic loss-of-function ALS2 mutation → loss of alsin GEF activity for Rab5 → impaired Rab5-dependent endosome fusion and macropinocytosis-associated trafficking → disturbed endosomal transport of IGF1 and BDNF receptors, excessive Rab5-positive vesicle accumulation, reduced endosomal motility and increased endosome-to-lysosome conversion → impaired trophic signaling and microtubule/actin cytoskeletal remodeling defects in corticospinal and lower motor neurons → retrograde degeneration of upper motor neurons of the pyramidal tract (predominant early), later LMN involvement → progressive spasticity, dysarthria/anarthria, slow disease course.
Sources: Devon et al., *PNAS* 2006, [10.1073/pnas.0510197103](https://www.pnas.org/doi/10.1073/pnas.0510197103); Deng et al., PMC: [2842444](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2842444/); PMC: [2364715](https://pmc.ncbi.nlm.nih.gov/articles/PMC2364715/); Molecular Brain 2009, [link](https://molecularbrain.biomedcentral.com/articles/10.1186/1756-6606-2-23).

**SIGMAR1 pathway:** Loss-of-function mutation in the ER chaperone sigma-1 receptor → failure to prevent misfolded protein accumulation, and dysregulated lipid transport/ion channel regulation, particularly in motor neurons of brainstem/spinal cord (high SIGMAR1 expression sites) → distal LMN-predominant degeneration sparing bulbar/respiratory and cognitive function.

**SPTLC1 pathway:** Gain-of-function/altered-specificity mutation in the rate-limiting sphingolipid biosynthesis enzyme → elevated serum ceramide → lipotoxic stress in motor neurons → mixed UMN/LMN degeneration with early spasticity.

**SPG11 (spatacsin) pathway:** Biallelic loss-of-function → impaired cytoskeletal stability and synaptic vesicle transport regulation → distal LMN + UMN degeneration, early bulbar involvement, without the corpus callosum thinning/cognitive impairment characteristic of SPG11-HSP.

### Cellular Processes & Biological Processes (GO term suggestions)
- Endosomal transport/protein trafficking (GO:0016197 endosomal transport) — ALS2
- Stress granule assembly (GO:0034063 stress granule assembly) — FUS
- mRNA processing / U1 snRNP biogenesis (GO:0006397 mRNA processing; GO:0000387 spliceosomal snRNP assembly) — FUS
- DNA damage response / R-loop resolution (GO:0000724 double-strand break repair via homologous recombination; GO:0061077 chaperone-mediated protein folding) — SETX
- Nucleocytoplasmic transport (GO:0006913 nucleocytoplasmic transport) — SETX
- Autophagy (GO:0006914 autophagy) — SETX, ALS2
- Sphingolipid biosynthetic process (GO:0030148 sphingolipid biosynthetic process) — SPTLC1
- ER protein quality control / chaperone activity (GO:0034975 protein folding in endoplasmic reticulum) — SIGMAR1
- Protein ubiquitination/proteasomal degradation (GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process) — UBQLN2

### Protein Dysfunction Modes
- FUS: cytoplasmic mislocalization + gain of toxic function (no obligate aggregation required for toxicity in knock-in models)
- SOD1: misfolding/aggregation, loss of antioxidant enzymatic function
- ALS2/alsin: complete loss of GEF function (LOF)
- SIGMAR1: loss of chaperone function (LOF)

### Tissue Damage / Neurodegeneration Mechanisms
Motor neuron death via a combination of proteostatic stress, impaired axonal/vesicular transport, glial activation (astrocytosis and microgliosis observed in FUS-P525L mouse spinal cord), oxidative stress (rationale for edaravone), and secondary denervation of neuromuscular junctions.

### Molecular Profiling
Transcriptomic/proteomic profiling of stress-granule composition in ALS-FUS models shows a shift to a more unstructured, AU-rich RNA content (Oxford NAR 2024, [10.1093/nar/gkad739](https://academic.oup.com/nar/article/52/21/13269/7874844)). Broader multi-omic (single-cell, spatial transcriptomic) characterization specific to JALS tissue was not identified in this search and likely represents a gap given tissue scarcity in pediatric cases.

### Suggested Cell Types (CL terms)
- Upper motor neuron / Betz cell (CL:0011005 corticospinal neuron / betz cell terminology varies)
- Lower motor neuron / spinal cord motor neuron (CL:0000100 motor neuron; CL:0011012 alpha motor neuron)
- Astrocyte (CL:0000127) — reactive astrocytosis
- Microglial cell (CL:0000129) — microgliosis

---

## 7. Anatomical Structures Affected

### Organ/System Level
- **Primary:** central nervous system — motor cortex (Betz cells/UMN), corticospinal tract, brainstem motor nuclei, spinal cord anterior horn (LMN) (UBERON:0002298 brainstem; UBERON:0002240 spinal cord; UBERON:0002771 femoral motor neuron / generic UBERON:0000010 peripheral nervous system for LMN axons)
- **Secondary:** skeletal muscle (denervation atrophy; UBERON:0001134 skeletal muscle tissue), neuromuscular junction (UBERON:0031594), respiratory musculature (diaphragm — UBERON:0001103) in aggressive forms (FUS, SOD1)
- **Body systems:** nervous system (primary), musculoskeletal system (secondary — scoliosis in ALS2, contractures), respiratory system (bulbar/respiratory forms)

### Tissue/Cell Level
- Corticospinal (upper) motor neurons of the motor cortex
- Spinal/bulbar (lower) motor neurons
- Reactive astrocytes and microglia in affected spinal cord segments

### Subcellular Level (GO Cellular Component)
- Nucleus/nuclear pore complex (FUS mislocalization, SETX nucleocytoplasmic transport defect) — GO:0005634, GO:0005643
- Cytoplasmic stress granules — GO:0010494
- Endosomes/Rab5-positive vesicles (ALS2) — GO:0005768
- Endoplasmic reticulum (SIGMAR1 chaperone) — GO:0005783
- Mitochondria (DDHD1 phospholipase regulation) — GO:0005739

### Localization/Lateralization
JALS motor neuron degeneration is typically **symmetric/bilateral**; asymmetric onset is reported in some SOD1-JALS cases. Imaging correlates: FUS shows T2/FLAIR pyramidal tract hyperintensity plus frontal atrophy/hypoperfusion; ALS2 shows mild cortical atrophy and corticospinal tract thinning; SYNE1 shows mild cerebellar atrophy (PMID: 34946884).

---

## 8. Temporal Development

### Onset
- Congenital/infantile: SIGMAR1 (1–2 yrs)
- Early childhood: ALS2 (mean 4.9 yrs, range 1–20)
- Childhood/adolescent (first–second decade): SETX (mean 16), SPTLC1 (4–15), SPG11 (7–23, typically 2nd decade), SYNE1 (11–12), ERLIN1 (before 24 in 6/12 family members)
- Late second/third decade: FUS (median 21), SOD1 (late 2nd–early 3rd decade), GNE (mean 26, range 12–35), TARDBP (24), UBQLN2 (16–24)
Onset is typically **insidious**, with symptom progression over months before diagnosis rather than acute presentation (PMID: 34946884).

### Progression
- **Rapid (1–2 year mortality):** FUS, SOD1
- **Intermediate (1–2 decades):** GNE (mean 13.4 yrs), SYNE1 (death ~age 39)
- **Slow (multiple decades, near-normal lifespan possible):** SETX/ALS4 ("normal life span" per OMIM #602433), ALS2, SIGMAR1, SPTLC1, SPG11 (27–40 yr disease duration), UBQLN2 (~4 decades), ERLIN1 (death 5th–6th decade) (PMID: 34946884)

### Patterns
No spontaneous remission is described for JALS. "Critical periods" are not formally defined, though the operational <25-year onset window itself demarcates the diagnostic category. Disease course is generally **monophasic progressive** rather than relapsing-remitting, distinguishing JALS from its phenocopies (e.g., HSP, which can show more static/slowly progressive UMN-only courses).

---

## 9. Inheritance and Population

### Epidemiology
- **US National ALS Registry (2010–2018):** 44 confirmed/likely juvenile ALS cases (onset <25 yrs) identified nationally; age-adjusted prevalence rose from 0.21/100,000 (2015) to 0.24/100,000 (2018) (Larkin et al. 2023, PMID: [37789566](https://pmc.ncbi.nlm.nih.gov/articles/PMC11299517/))
- Overall ALS prevalence (all ages, US) is ~9.9 per 100,000 for context; only ~5% of all ALS cases have onset before age 30, and ~13% before age 40 (Target ALS summary; general ALS epidemiology literature)
- Demographics from the registry: 79.5% male / 20.5% female (>3:1 male predominance); 54.5% non-white / 45.5% non-Hispanic white — an "inverse" pattern relative to general ALS demographics (which skew white); geographic distribution: Northeast 29.5%, Midwest 25%, South/West 15.9% each (PMID: 37789566)

### Inheritance Patterns (genetic forms)
| Gene | Inheritance |
|---|---|
| ALS2, SIGMAR1, SPG11, ERLIN1, GNE, VRK1 | Autosomal recessive |
| SETX | Autosomal dominant (only recurrent AD gene) |
| FUS, SOD1, SPTLC1 (most) | De novo (dominant, non-inherited) |
| UBQLN2 | X-linked dominant |
(PMID: 34946884)

### Penetrance / Expressivity
SETX-ALS4 shows **incomplete, sex-dependent penetrance** — males symptomatic 31% vs. females 13%, with males also showing greater disease burden and higher serum creatine kinase (PMID: 34946884; Grunseich 2020, [10.1002/ana.25681](https://onlinelibrary.wiley.com/doi/abs/10.1002/ana.25681)). Variable expressivity is evident across the phenotypic continuum of ALS2 mutations (IAHSP–JPLS–JALS2).

### Genetic Anticipation, Mosaicism, Founder Effects
Not systematically documented for JALS in the literature surveyed. ALS2 was historically over-represented in **consanguineous North African and Middle Eastern families**, consistent with a founder/consanguinity effect for autosomal recessive disease, though the gene is now recognized globally (PMID: 34946884).

### Consanguinity
Elevated relevance for the autosomal recessive forms (ALS2, SIGMAR1, SPG11) given their original ascertainment in consanguineous pedigrees.

### Carrier Frequency
Population carrier-frequency data (gnomAD-derived) specific to JALS-causing recessive alleles were not retrieved in this search and would need dedicated gnomAD querying per gene/variant.

---

## 10. Diagnostics

### Clinical Criteria
JALS diagnosis rests on: (1) age of onset <25 years, and (2) evidence of combined UMN + LMN degeneration, applying the same clinical framework used for AO-ALS (revised El Escorial / Awaji criteria), which have recognized limitations in sensitivity, particularly in atypical/pediatric presentations (search results on El Escorial criteria, 2024–2025 literature). The principal JALS review states: "Patients presenting with combined upper and lower motor neuron disorders before age 25 should be carefully examined for genetic mutations" (PMID: 34946884).

### Electrodiagnostics (EMG/NCS)
Pattern across JALS genes: active denervation with chronic neurogenic changes and **no sensory abnormalities** on nerve conduction studies (consistent with a pure motor neuronopathy), though it "confirms LMN involvement but [is] not useful in distinguishing the different gene mutations." SETX is a partial exception, showing low/absent motor NCS amplitudes with normal sensory studies (PMID: 34946884).

### Imaging
- MRI often normal or shows only mild abnormality
- FUS: pyramidal tract T2/FLAIR hyperintensity, frontal atrophy/hypoperfusion
- ALS2: mild cortical atrophy, corticospinal tract thinning
- SETX: muscle MRI shows distal lower-extremity fatty infiltration
- SYNE1: mild cerebellar atrophy
(PMID: 34946884)

### Genetic Testing
Given the 40% genetic yield, **multigene panel testing (or WES) covering ALS2, SETX, FUS, SIGMAR1, SOD1, SPTLC1, SPG11, UBQLN2, and the rarer genes** is the recommended diagnostic approach once combined UMN/LMN signs with onset <25 years are established. Single-gene testing may be prioritized by phenotype (e.g., SETX first for AD family history with distal, bulbar-sparing disease; ALS2 for AR consanguineous families with very early anarthria/spasticity).

### Differential Diagnosis ("JALS mimics")
- **Juvenile Primary Lateral Sclerosis (JPLS):** UMN-only, ALS2-associated
- **Hereditary Spastic Paraplegia (HSP):** UMN-predominant, sensory neuropathy, no bulbar involvement typically; SPG11, ALS2, ERLIN1, DDHD1-associated; MRI corpus callosum thinning (contrasting with SPG11-ARJALS)
- **Spinal muscular atrophy (SMA):** pure LMN, no UMN signs — the key discriminator per differential-diagnosis literature
- **Distal hereditary motor neuropathy (dHMN):** LMN-only (SIGMAR1 allelic overlap)
- **NBIA (neurodegeneration with brain iron accumulation):** reported mimicking JALS initially in one case (10-year-old girl) before basal ganglia iron deposition emerged
(PMID: 34946884)

---

## 11. Outcome/Prognosis

### Survival/Mortality
Prognosis is **strongly gene-dependent** rather than uniform:
- **Poor prognosis / rapid mortality:** FUS (death from respiratory failure within 1–2 years, especially P525L), SOD1-JALS (documented deaths <2 years)
- **Favorable/near-normal prognosis:** SETX/ALS4 (OMIM: "normal life span"), ALS2 (slow progression despite early onset), SPG11 (27–40 year disease duration), UBQLN2 (~4-decade course)
(PMID: 34946884)

### Morbidity/Functional Outcomes
Long-duration forms (ALS2, SETX, SPG11) accrue substantial cumulative disability (progressive spasticity, anarthria, loss of ambulation) over a period spanning childhood through adulthood — a distinct morbidity profile from AO-ALS's shorter but more uniformly fatal course.

### Prognostic Factors
The causative gene is itself the dominant prognostic factor; the review states, "hereditary patterns and coexisting features may be useful in determining prognosis," and that gene identification "allows for a better prediction of prognosis and early diagnostic testing in other affected family members" (PMID: 34946884). No validated biomarker-based prognostic score specific to JALS was identified (contrast with AO-ALS, where plasma neurofilament light chain (NfL) is an emerging prognostic/pharmacodynamic biomarker, notably used in tofersen trials).

---

## 12. Treatment

### Pharmacotherapy
- **Riluzole** — the only agent broadly used across ALS with proven (modest) survival benefit in adults (2–3 month prolongation of tracheostomy-free survival); pediatric/juvenile use is described in the literature as "less established," used at some centers on a case-by-case basis (Healthline; NCBI Bookshelf review; PMID search results)
- **Edaravone** — FDA-approved 2017 for AO-ALS (antioxidant, reduces oxidative/free-radical injury); pediatric investigation described as ongoing/limited, with regional variation in approval status
- **Tofersen** (antisense oligonucleotide) — FDA accelerated approval April 2023, specifically for **SOD1-mutant ALS**; intrathecally administered, binds SOD1 mRNA to reduce toxic SOD1 protein and CSF SOD1 levels; reduces plasma neurofilament light chain, though ALSFRS-R functional benefit has been variable across trials (NEJM 2022, PMID: [35379992]; systematic review PMC: [12003547](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12003547/)). Given SOD1's rarity as a JALS cause (3 reported cases) but its druggability, this is the clearest example of a genotype-matched precision therapy potentially applicable to a JALS subgroup, though pediatric/juvenile-specific trial data were not identified in this search.
- **Serine supplementation** (SPTLC1) — trialed in one SPTLC1-JALS patient, produced weight gain; "utility... is uncertain and may potentially worsen the overproduction of sphingolipids" (PMID: 34946884)

### Advanced/Experimental Therapeutics
- Antisense oligonucleotide silencing approaches are in preclinical development for **FUS** (PMC: [8799464](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8799464/)) and for the dominant **SETX** ALS4 mutation via allele-specific silencing (bioRxiv 2024)
- Gene therapy trials (e.g., NCT04632225, "Engensis"/VM202) are registered for ALS broadly but not JALS-specific

### Supportive/Rehabilitative Care
Multidisciplinary clinic management (neurology, pulmonology, PT/OT, speech-language pathology, nutrition, social work, ALS association support) is standard of care; respiratory support ranges from noninvasive to invasive mechanical ventilation as disease progresses (search results, general ALS management literature; NCIT:C15302 Physical Therapy, NCIT:C15315 Rehabilitation, NCIT:C15747 Supportive Care).

### Treatment Algorithm Notes
No JALS-specific clinical practice guideline algorithm was identified; management is extrapolated from AO-ALS guidelines with genotype-informed personalization emphasized as the field's stated future direction: "With the future of personalized medicine, the identification of a disease-causing gene mutation may lead to treatment" (PMID: 34946884).

**Suggested NCIT terms:** NCIT:C15986 (Pharmacotherapy) for riluzole/edaravone; NCIT:C15238 (Gene Therapy) for ASO approaches (tofersen, investigational FUS/SETX ASOs); NCIT:C15240 (Genetic Counseling); NCIT:C15315 (Rehabilitation); NCIT:C15313 not applicable (no radiotherapy role).

---

## 13. Prevention

### Primary/Secondary Prevention
No primary prevention strategy exists (genetic, non-modifiable causal factors dominate). Secondary prevention centers on **genetic counseling and cascade family testing** once a proband's causative variant is identified, given that gene identification "allows for... early diagnostic testing in other affected family members" (PMID: 34946884).

### Screening
- No population-based newborn or carrier screening program specific to JALS genes was identified.
- For autosomal recessive forms (ALS2, SIGMAR1, SPG11) in populations with known consanguinity/founder variants, **targeted carrier screening and prenatal/preimplantation genetic testing** would be a plausible clinical application, though not documented as an established program in the literature surveyed.

### Genetic Counseling
Recommended for families with a confirmed pathogenic variant, particularly for the autosomal dominant (SETX) and X-linked (UBQLN2) forms where risk to relatives is high and predictable, and for autosomal recessive forms where carrier status and reproductive risk counseling is relevant.

### Public Health / Prophylaxis
Not applicable — no infectious or environmentally preventable component has been established for JALS.

---

## 14. Other Species / Natural Disease

No naturally occurring juvenile-onset ALS phenocopy in non-human species was identified in this search. (Note: dismech's existing `Amyotrophic_Lateral_Sclerosis` entry documents naturally occurring **canine degenerative myelopathy** [SOD1 E40K homozygous dogs] as an adult/older-onset model informative for general ALS motor neuron degeneration — PMID:19188595 — but this is not described as a juvenile-onset natural disease analog and would need independent verification before being cited under a JALS-specific entry.) Comparative/orthologous gene information (ALS2, SETX, FUS, SOD1 orthologs) is well established across model organisms per Alliance of Genome Resources/MGI/RGD but was not separately queried here.

---

## 15. Model Organisms

### Mouse Models
- **Als2−/− (alsin knockout) mice:** Decreased locomotor activity, small but significant decrease in cortical motor neuron size; "four ALS2-deficient mouse models have been generated by different groups... though these mouse models largely fail to recapitulate hallmarks of motor neuron disease" — i.e., **fidelity is LOW/MODERATE and should be flagged as a HUMAN_MODEL_MISMATCH** in curation. Mechanistically, Als2−/− neurons show disturbed Rab5-dependent endosomal transport of IGF1/BDNF receptors, excess Rab5-positive vesicle accumulation, reduced endosomal motility (Devon et al., PNAS 2006, [10.1073/pnas.0510197103](https://www.pnas.org/doi/10.1073/pnas.0510197103); PMC: [2364715](https://pmc.ncbi.nlm.nih.gov/articles/PMC2364715/)). Als2 loss also **exacerbates** motor dysfunction when crossed onto a SOD1-H46R AO-ALS mouse background, via disturbed endolysosomal trafficking (Deng et al., PMC: [2842444](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2842444/)) — a genetic-modifier/epistasis model rather than a standalone JALS model.
- **SETX knock-in mice (L389S and R2136H):** Both transgenic and knock-in approaches yield mice with neuromuscular phenotypes and motor neuron degeneration; critically, they recapitulate **TDP-43 nuclear clearing and cytoplasmic mislocalization**, matching human ALS4 postmortem spinal cord pathology — a relatively **high-fidelity** model for the TDP-43 pathology arm, with additional readouts of nucleocytoplasmic transport dysfunction (Ran/RanGAP1 abnormalities) and enhanced stress granule formation (Bennett et al., *Acta Neuropathol* 2018, PMID: [29725819](https://pubmed.ncbi.nlm.nih.gov/29725819/)).
- **FUS-P525L humanized knock-in mice ("hFUS-P525L"):** Progressive, age-dependent lumbar motor neuron loss (~30% by 12 months), NMJ denervation (37% loss of tibialis NMJs by 1 year), astrocytosis/microgliosis, occurring via a **dose-dependent gain-of-toxic-function mechanism without obligate cytoplasmic aggregation** — an important negative/nuanced finding: "the ALS FUS knock-in model... showed neuronal dysfunction and degeneration in the absence of cytoplasmic FUS protein accumulation, suggesting aggregates may not be the initial drivers of neuronal dysfunction" (ALZFORUM hFUS-P525L summary; related "FUSΔ14" knock-in model, PMC: [5841203](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5841203/)).

### Other Model Systems
- *C. elegans* FUS knock-in models show disrupted autophagy and neuronal dysfunction (bioRxiv, [10.1101/799932](https://www.biorxiv.org/content/10.1101/799932.full.pdf))
- A separate TDP-43 knock-in mouse model (independent of SETX) is described as "a robust TDP-43 knock-in mouse model of ALS" relevant to the broader TDP-43 proteinopathy shared across ALS subtypes (PMC: [6975031](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6975031/))
- iPSC-derived motor neurons: a human iPSC line carrying a *de novo* pathogenic FUS mutation identified in a juvenile ALS patient was differentiated into motor neurons showing pathological characteristics recapitulating patient disease features (PMC: [7507938](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7507938/)) — a patient-derived cellular model with inherently high genotype fidelity.

### Model Limitations Summary
Across all mouse models, a recurring limitation is that **rodent lifespan/physiology compresses or alters the decades-long human juvenile disease course**, and that Als2 knockout mice in particular fail to fully recapitulate the human motor neuron disease phenotype despite the biochemical (endosomal trafficking) defect being conserved — an explicit candidate for a `HUMAN_MODEL_MISMATCH` discussion node in any curated pathophysiology entry.

---

## Summary of Key Evidence Gaps
1. **Environmental risk/protective factors** for JALS are essentially unstudied as a distinct question from AO-ALS.
2. **Population genetics** (gnomAD carrier frequencies, penetrance estimates) for most JALS genes beyond SETX are not well quantified.
3. **JALS-specific treatment trial data** (riluzole/edaravone/tofersen efficacy in patients <25 years) are sparse; most evidence is extrapolated from adult trials or single case reports.
4. **Quality-of-life instruments** validated specifically for pediatric/juvenile ALS were not identified.
5. **Als2 mouse models' translational fidelity is explicitly reported as poor**, an important caveat for any pathophysiology narrative built on this model.

---

## Sources

- [Juvenile Amyotrophic Lateral Sclerosis: A Review (Genes, 2021) — PMID 34946884](https://pmc.ncbi.nlm.nih.gov/articles/PMC8701111/)
- [A brief report on juvenile ALS cases in the US National ALS Registry: 2010–2018 — PMID 37789566](https://pmc.ncbi.nlm.nih.gov/articles/PMC11299517/)
- [105400 - Amyotrophic Lateral Sclerosis 1 (OMIM)](https://omim.org/entry/105400)
- [Entry #602433 - Amyotrophic Lateral Sclerosis 4, Juvenile (OMIM)](https://www.omim.org/entry/602433)
- [Entry #205100 - Amyotrophic Lateral Sclerosis 2, Juvenile (OMIM)](https://omim.org/entry/205100)
- [Amyotrophic Lateral Sclerosis 4, Juvenile (ALS4) - MalaCards](https://www.malacards.org/card/amyotrophic_lateral_sclerosis_4_juvenile)
- [DNA/RNA Helicase Gene Mutations in a Form of Juvenile ALS (ALS4)](https://www.sciencedirect.com/science/article/pii/S0002929707628407)
- [Genotype-phenotype relationship in hereditary ALS - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4513711/)
- [A Novel Splice-Site Mutation in ALS2 Establishes the Diagnosis of Juvenile ALS](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4256290/)
- [Allele-specific silencing of a dominant SETX mutation in ALS4 (bioRxiv 2024)](https://www.biorxiv.org/content/10.1101/2024.10.11.617871.full.pdf)
- [Investigation of genetic and clinical features in Chinese patients with juvenile ALS - PMID 28429524](https://pubmed.ncbi.nlm.nih.gov/28429524/)
- [A de novo c.1509dupA:p.R503fs mutation of FUS - PMID 32501131](https://pubmed.ncbi.nlm.nih.gov/32501131/)
- [De novo FUS P525L mutation in Juvenile ALS with dysphonia and diplopia - PMID 27123482](https://pubmed.ncbi.nlm.nih.gov/27123482/)
- [Novel FUS Y526C mutation - PMID 28054830](https://pubmed.ncbi.nlm.nih.gov/28054830/)
- [FUS mutations in sporadic juvenile ALS - PMID 20668260](https://pubmed.ncbi.nlm.nih.gov/20668260/)
- [Human iPSC line carrying de novo FUS mutation from juvenile ALS patient](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7507938/)
- [FUS-P525L Juvenile ALS and Intellectual Disability - Neurology Genetics](https://www.neurology.org/doi/10.1212/NXG.0000000000200009)
- [FUS P525L mutation causing ALS and movement disorders - PMID 32307925](https://pubmed.ncbi.nlm.nih.gov/32307925/)
- [FUS Mutations in Pediatric ALS: Case Report and Review - PMID 32281455](https://pubmed.ncbi.nlm.nih.gov/32281455/)
- [Infantile Ascending HSP with Extrapyramidal/Extraocular Manifestations - ALS2](https://pmc.ncbi.nlm.nih.gov/articles/PMC8721836/)
- [Infantile-Onset Ascending HSP Associated with Alsin Gene Mutations](https://www.sciencedirect.com/science/article/pii/S0002929707603322)
- [Alsin Related Disorders: Literature Review and Case Study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4180207/)
- [Clinical and Molecular Aspects of Senataxin Mutations in ALS4 (Grunseich, Ann Neurol 2020)](https://onlinelibrary.wiley.com/doi/abs/10.1002/ana.25681)
- [Senataxin mutations elicit motor neuron degeneration phenotypes and TDP-43 mislocalization - PMID 29725819](https://pubmed.ncbi.nlm.nih.gov/29725819/)
- [A novel SETX gene mutation associated with Juvenile ALS](https://onlinelibrary.wiley.com/doi/10.1002/brb3.1066)
- [SETX functions in autophagy regulation - PMID 32686621](https://pubmed.ncbi.nlm.nih.gov/32686621/)
- [Juvenile Amyotrophic Lateral Sclerosis - MalaCards](https://www.malacards.org/card/juvenile_amyotrophic_lateral_sclerosis)
- [Orphanet: Juvenile amyotrophic lateral sclerosis (ORPHA:300605)](https://www.orpha.net/en/disease/detail/300605)
- [GARD: Juvenile amyotrophic lateral sclerosis](https://rarediseases.info.nih.gov/diseases/11901/juvenile-amyotrophic-lateral-sclerosis)
- [Mutation in SIGMAR1 gene linked to juvenile ALS (ScienceDaily)](https://www.sciencedaily.com/releases/2011/08/110812091545.htm)
- [Novel SIGMAR1 missense mutation - dHMN phenotype mimicking juvenile ALS](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12041004/)
- [SIGMAR1 gene mutation causing dHMN in a Portuguese family](https://pmc.ncbi.nlm.nih.gov/articles/PMC6060428/)
- [Turkish families with juvenile motor neuron disease broaden SPG11 phenotype](https://www.neurology.org/doi/10.1212/NXG.0000000000000025)
- [Tofersen - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK594270/)
- [Tofersen for SOD1 ALS: systematic review and meta-analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12003547/)
- [Als2-deficient mice exhibit disturbances in endosome trafficking (PNAS)](https://www.pnas.org/doi/10.1073/pnas.0510197103)
- [Loss of ALS2/Alsin Exacerbates Motor Dysfunction in SOD1-H46R Mouse Model](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2842444/)
- [Alsin and the Molecular Pathways of ALS](https://pmc.ncbi.nlm.nih.gov/articles/PMC2364715/)
- [Regulation of endosomal motility and degradation by ALS2/alsin](https://molecularbrain.biomedcentral.com/articles/10.1186/1756-6606-2-23)
- [hFUS-P525L mouse model - ALZFORUM](https://www.alzforum.org/research-models/hfus-p525l)
- [Panel of Mouse Models: Mutated FUS Gains Toxic Function - ALZFORUM](https://www.alzforum.org/news/research-news/panel-mouse-models-agree-mutated-fus-gains-toxic-function)
- [Humanized mutant FUS drives motor neuron degeneration in FUSΔ14 knockin mice](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5841203/)
- [A robust TDP-43 knock-in mouse model of ALS](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6975031/)
- [Antisense oligonucleotide silencing of FUS as therapeutic approach](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8799464/)
- [Mutant FUS proteins incorporate into stress granules - PMID 20699327](https://pubmed.ncbi.nlm.nih.gov/20699327/)
- [Aberrant FUS-U1 snRNA interaction mechanism](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7733473/)
- [Stress Granule Dysregulation in ALS](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7705167/)
- [ALS-associated FUS mutation reshapes RNA/protein composition of stress granules](https://academic.oup.com/nar/article/52/21/13269/7874844)
- [Establishing Diagnostic and Differential Diagnostic Criteria for ALS](https://doi.org/10.3390/jcm15010287)
- [Diagnosis and differential diagnosis of MND/ALS: IFCN handbook chapter](https://www.sciencedirect.com/science/article/pii/S2467981X23000355)
- [Juvenile ALS: Symptoms, Diagnosis, Treatment (Healthline)](https://www.healthline.com/health/juvenile-als)
- [Juvenile ALS: How Common is ALS in Your 20s? - Target ALS](https://targetals.org/news/juvenile-als-how-common-is-als-in-your-20s/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 4 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 37 |
| On topic | 23 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

2 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:28054830` *(abstract only)*: "the most frequent genetic factor in aggressive juvenile ALS"
  - closest text in source: "Although amyotrophic lateral sclerosis (ALS) typically occurs around 60 years, numerous publications report an onset of ALS before the age of 25 years that define juvenile ALS (jALS)"
- `PMID:34946884`: "utility... is uncertain and may potentially worsen the overproduction of sphingolipids"
  - closest text in source: "Treatment with serine was initiated in one patient and resulted in weight gain, [57] although the utility of this approach is uncertain and may potentially worsen the overproduction of spingolipids [58]"
- `PMC:PMC5841203` *(abstract only)*: "the ALS FUS knock-in model... showed neuronal dysfunction and degeneration in the absence of cytoplasmic FUS protein accumulation, suggesting aggregates may not be the initial drivers of neuronal dysfunction"
  - closest text in source: "Using our new FUSDelta14 ALS mouse-antibody system we show that neurodegeneration occurs in the absence of FUS protein aggregation"