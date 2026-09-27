---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-18T15:07:56.606533'
end_time: '2026-08-18T15:12:53.288859'
duration_seconds: 296.68
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder with Microcephaly, Hypotonia, and Absent
    Language
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
  web_search_requests: 11
  num_turns: 19
  total_cost_usd: 1.8747902
  session_id: 31bcdcbf-e6bc-51a8-b4d4-70544036de95
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 11
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Microcephaly, Hypotonia, and Absent Language
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Microcephaly, Hypotonia, and Absent Language** covering all of the
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

I'll research this condition using web search tools to gather accurate, current information with proper citations.

Found it — NEDMHAL is OMIM #620038, caused by biallelic PSMB1 mutations. Let me pull the OMIM entry and primary literature.

# Research Report: Neurodevelopmental Disorder with Microcephaly, Hypotonia, and Absent Language (NEDMHAL)

## 1. Disease Information

**Overview:** Neurodevelopmental disorder with microcephaly, hypotonia, and absent language (NEDMHAL) is an ultra-rare, autosomal recessive proteasome-assembly disorder ("neurodevelopmental proteasomopathy") first described in 2020 in two affected sisters from a consanguineous Pakistani family. It is caused by biallelic pathogenic variants in *PSMB1*, which encodes the β6 subunit of the 20S core proteasome. Affected individuals present with severe global developmental delay, postnatal microcephaly, axial hypotonia, absent expressive language, short stature, aggressive/behavioral abnormalities, and sensorineural hearing loss. Functional work in patient fibroblasts and a zebrafish model showed that the causal variant destabilizes 20S/26S proteasome assembly, directly linking impaired proteostasis to a human neurodevelopmental phenotype (Ansar et al., 2020, PMID:32129449).

**Key identifiers:**
- **OMIM (phenotype):** #620038 — NEURODEVELOPMENTAL DISORDER WITH MICROCEPHALY, HYPOTONIA, AND ABSENT LANGUAGE; NEDMHAL
- **OMIM (gene):** *602017 — PROTEASOME SUBUNIT, BETA-TYPE, 1; PSMB1
- **Gene location:** Chromosome 6q27
- **HGNC:** PSMB1 (HGNC:9537)
- **Inheritance:** Autosomal recessive
- **Suggested MONDO:** a MONDO term for this OMIM-derived entity is expected to exist as a cross-reference to OMIM:620038 (mapping should be confirmed directly against the MONDO release rather than assumed, since it was not independently verified in this search pass).
- Orphanet does not appear to carry a dedicated, separately numbered entry distinct from the OMIM phenotype as of this search; the PSMB1 gene page on Orphanet cross-references the associated disorder.

**Synonyms:** NEDMHAL (OMIM abbreviation); "PSMB1-related neurodevelopmental disorder"; "PSMB1-related proteasomopathy." It is one of a small family of related but molecularly distinct "neurodevelopmental proteasomopathies" (also including disorders caused by *PSMC1*, *PSMC3*, *PSMD12*, and *PSMD11*) (Cuinat et al., 2024, PMID:39220754).

**Data provenance:** The disease-defining data derive from a single aggregated case report of an index consanguineous family (two affected sisters, family "F200") combined with functional/mechanistic validation studies (patient-derived cells, in silico protein modeling, and a zebrafish model) — not from large-scale registries or EHR-based aggregation. As of this research pass, no independently published second family was identified; the entity remains defined by this single kindred plus experimental validation.

Sources:
- [OMIM #620038 — NEDMHAL](https://omim.org/entry/620038)
- [OMIM *602017 — PSMB1](https://omim.org/entry/602017)
- [Biallelic variants in PSMB1... — PubMed](https://pubmed.ncbi.nlm.nih.gov/32129449/)
- [Understanding neurodevelopmental proteasomopathies... — PubMed](https://pubmed.ncbi.nlm.nih.gov/39220754/)

---

## 2. Etiology

**Disease causal factors:** NEDMHAL is a monogenic, purely genetic disorder — no environmental, infectious, or acquired etiology has been implicated. It is caused by biallelic (homozygous, in the reported family) loss-of-function/destabilizing missense variation in *PSMB1*.

**Genetic risk factors:**
- **Causal variant:** A homozygous *PSMB1* c.307T>C transition, predicting p.(Tyr103His) (Y103H), was identified in both affected sisters by whole-exome/genome sequencing in the index consanguineous Pakistani family (Ansar et al. 2020, PMID:32129449). The variant affects a highly conserved tyrosine residue.
- **Molecular consequence:** Structural modeling indicated the Y103H substitution "weakens the interactions between PSMB1/β6 and PSMA5/α5 proteasome subunits and thus destabilizes the 20S proteasome complex" — i.e., it is not a simple catalytic-site loss-of-function but an assembly-interface–disrupting variant.
- **Population frequency:** The Y103H variant was absent from gnomAD and from 300 in-house control chromosomes, consistent with a rare, highly penetrant recessive allele (GeneCards/PubMed).
- **Consanguinity:** The proband family was consanguineous, and autosomal recessive transmission with homozygosity was the observed inheritance mechanism — consistent with the broader pattern that recessive, biallelic proteasome-subunit disease alleles are strongly enriched by consanguinity, since core proteasome subunits are highly constrained and most heterozygous loss-of-function variants would be expected to be selected against or, in other proteasome genes (e.g., *PSMD12*), to instead cause a *dominant* de novo disorder.

**Risk-factor caveat for curation:** No independent GWAS, epidemiological, or environmental-exposure risk-factor literature exists for this ultra-rare Mendelian condition; population-level risk-factor databases (GWAS Catalog, PheGenI, CTD) were not found to carry entries for this specific disorder.

**Protective factors:** None reported. No protective variants or modifier alleles have been described.

**Gene-environment interactions:** None described; this is not currently modeled as a gene-environment interaction disease.

Sources:
- [Biallelic variants in PSMB1 — PubMed](https://pubmed.ncbi.nlm.nih.gov/32129449/)
- [PSMB1 gene — GeneCards](https://www.genecards.org/card/PSMB1)

---

## 3. Phenotypes

Based on the OMIM clinical synopsis and the founding case report, the core phenotype set is:

| Phenotype | Type | Onset/Course | Suggested HPO term (verify before curation) |
|---|---|---|---|
| Microcephaly (postnatal) | Physical/clinical sign | Present from early childhood, non-progressive but persistent | HP:0000252 Microcephaly |
| Global developmental delay | Behavioral/developmental | Infancy onset | HP:0001263 Global developmental delay |
| Severe intellectual disability | Cognitive | Persistent, non-regressive | HP:0010864 Severe intellectual disability (or HP:0001249 Intellectual disability, if severity unconfirmed) |
| Absent speech / absent language | Behavioral/developmental | Lifelong, never acquired | HP:0001344 Absent speech |
| Axial/truncal hypotonia | Clinical sign | Infantile onset | HP:0001252 Hypotonia |
| Short stature | Physical | Postnatal | HP:0004322 Short stature |
| Sensorineural hearing loss | Clinical sign/lab | Reported in affected sibs | HP:0000365 Hearing impairment (or HP:0000407 Sensorineural hearing impairment, if specified) |
| Aggressive behavior | Behavioral | Reported | HP:0000718 Aggressive behavior |

**Severity/progression:** The disorder is described as severe and non-progressive/static in its core neurodevelopmental features (developmental delay is profound from infancy rather than regressive), consistent with a primary neurodevelopmental (rather than neurodegenerative) proteasomopathy. Because the condition is known from only two affected siblings, formal frequency percentages (e.g., "80% of patients have X") cannot be computed — features should be curated as present/absent in the reported cases rather than as population frequencies. This is an important curation caveat: standard HPO frequency modifiers (FREQUENT/OCCASIONAL) are not statistically meaningful for an n=2 cohort and should be omitted or explicitly qualified as "observed in both/one of the reported patients."

**Quality-of-life impact:** Not formally studied (no EQ-5D/SF-36/QOL instrument data identified); qualitatively, the phenotype (absent language, severe ID, non-ambulatory/motor impairment implied by hypotonia) implies a high care-dependency burden, consistent with other severe recessive neurodevelopmental proteasomopathies, but no quantitative QOL data were located.

Sources:
- [OMIM #620038 clinical synopsis](https://omim.org/entry/620038)
- [Biallelic variants in PSMB1 — PubMed](https://pubmed.ncbi.nlm.nih.gov/32129449/)

---

## 4. Genetic/Molecular Information

**Causal gene:** *PSMB1* (proteasome 20S subunit beta 1; HGNC:9537; NCBI Gene ID 5689; OMIM *602017), chromosome 6q27, 6 exons, encoding the 241-amino-acid, ~26.5 kDa proteasome subunit beta type-1 protein (UniProt P20618).

**Pathogenic variant:**
- **Variant:** NM_002793 (or equivalent RefSeq) c.307T>C, p.(Tyr103His)
- **Zygosity/origin:** Homozygous, germline, inherited (biallelic transmission from unaffected consanguineous heterozygous parents)
- **ACMG classification:** Reported as pathogenic in the founding functional/genetic study; a ClinVar submission exists for at least a related *CDK19* variant in an unrelated condition (not to be confused with NEDMHAL) — curators should confirm the specific ClinVar accession for the PSMB1 Y103H allele directly rather than assume one.
- **Population frequency:** Absent from gnomAD and from 300 local control chromosomes (essentially private/ultra-rare allele).
- **Functional consequence:** Loss-of-function via **destabilization of proteasome assembly**, not loss of catalytic activity per se — the variant weakens the PSMB1(β6)–PSMA5(α5) subunit-subunit interface required for correct 20S core particle ring assembly, leading to reduced levels of properly assembled 20S and 26S proteasome complexes in patient cells.

**Modifier genes:** None described.

**Epigenetic information:** No disease-specific epigenetic (DNA methylation/histone) data were identified for NEDMHAL specifically. (Note: proteasome dysfunction across the broader "neurodevelopmental proteasomopathy" class has been linked to secondary transcriptional/interferon-signature changes — see PSMB1's paralog literature such as PSMD11 and PSMC3, which show increased type-I interferon responses — PMID:39220754 and related PSMC3 literature — but this has not been specifically reported for PSMB1/NEDMHAL itself.)

**Chromosomal abnormalities:** None reported; this is a single-nucleotide-variant disorder, not a copy-number/structural disorder.

**Related genes in the same pathway class (for KB cross-referencing / grouping consideration):** *PSMB1* sits within the broader emerging "neurodevelopmental proteasomopathy" gene set — *PSMC1* (DEE87-adjacent proteasome disorder), *PSMC3*, *PSMD12*, and *PSMD11* — each causing molecularly distinct but mechanistically related proteostasis disorders (Cuinat et al. 2024, PMID:39220754). Note that *CDK19*-related developmental and epileptic encephalopathy (DEE87, OMIM #618916) is a different, unrelated gene/disorder that surfaced in searches due to acronym/description similarity and should **not** be conflated with NEDMHAL/PSMB1 — this is a Named-Entity-Confusion risk worth flagging for curators (a "CDK19" vs "PSMB1" mixup).

Suggested ontology terms:
- Gene: `hgnc:9537` (PSMB1)
- GO Molecular Function: GO:0004298 threonine-type endopeptidase activity (proteasome core particle catalytic activity — note PSMB1/β6 is itself non-catalytic in the mature complex but part of the catalytic ring)
- GO Cellular Component: GO:0005839 proteasome core complex; GO:0000502 proteasome complex
- GO Biological Process: GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process

Sources:
- [PSMB1 gene — GeneCards](https://www.genecards.org/card/PSMB1)
- [PSMB1 — NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/5689)
- [UniProt P20618 — PSMB1](https://www.uniprot.org/uniprotkb/P20618/entry)
- [Biallelic variants in PSMB1 — PubMed](https://pubmed.ncbi.nlm.nih.gov/32129449/)

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors have been described for NEDMHAL — it is a fully penetrant monogenic recessive disorder with no reported environmental modifiers, toxin exposures, or infectious triggers in the literature identified.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular trigger (upstream):** Homozygous *PSMB1* c.307T>C (p.Y103H) destabilizes the PSMB1(β6)–PSMA5(α5) inter-subunit interface required for correct assembly of the 20S proteasome core particle ring.
2. **Proteasome assembly defect:** Reduced formation/stability of properly assembled 20S core particles and, consequently, 26S proteasome holoenzymes (20S core + 19S regulatory particle), demonstrated biochemically in patient-derived cells.
3. **Impaired proteostasis:** Reduced ubiquitin-proteasome system (UPS) capacity for degrading damaged, misfolded, and regulatory ubiquitin-tagged proteins — i.e., impaired protein homeostasis at the cellular level.
4. **Neurodevelopmental consequence:** In a zebrafish model, CRISPR/Cas9 mutagenesis and morpholino-mediated knockdown of the single zebrafish *psmb1* ortholog produced microcephaly, microphthalmia, and an overall reduction in brain size with morphologic brain abnormalities — directly linking proteasome-assembly failure to a small-brain/neurodevelopmental phenotype in vivo.
5. **Clinical manifestation:** The convergence of impaired neuronal/neural progenitor proteostasis during brain development is proposed to underlie the human phenotype of microcephaly, severe developmental delay/intellectual disability, absent language, and hypotonia.

**Cellular processes involved:** Ubiquitin-proteasome-mediated protein degradation (GO:0043161); proteostasis/protein quality control; by extension of the broader proteasomopathy literature, secondary innate-immune/interferon pathway dysregulation has been reported for sibling proteasomopathies (PSMC3, PSMD11), suggestive of a shared class-wide mechanism worth watching for in future PSMB1-specific studies, though not yet directly shown for PSMB1.

**Protein dysfunction:** Not classic misfolding/aggregation of a single client protein, but rather a structural assembly defect in a multi-subunit machine (destabilized inter-subunit ring interface), reducing the abundance/activity of functional 20S/26S proteasome complexes rather than eliminating PSMB1 protein entirely.

**Tissue/cell involvement — developing brain:** The zebrafish data implicate neural progenitor cells and developing brain tissue as the most proteasome-dependent, disease-relevant compartment, consistent with microcephaly and severe cognitive/language impairment as the dominant human phenotype.

**Advanced/omics data:** No transcriptomic, proteomic, or single-cell datasets specific to human PSMB1-mutant neural tissue were identified in this search; the zebrafish morphant/mutant model and patient fibroblast proteasome-assembly assays (native gel/glycerol gradient sedimentation-type assays implied by "impaired assembly and function of the 20S and 26S proteasomes") constitute the primary functional dataset.

Suggested ontology terms:
- GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process
- GO:0000502 proteasome complex
- GO:0005839 proteasome core complex
- CL: neural progenitor cell (CL:0011020) — implicated by the zebrafish brain-size phenotype, though not directly assayed in human neural tissue
- UBERON:0000955 brain (microcephaly/brain-size phenotype)

Sources:
- [Biallelic variants in PSMB1 — PubMed](https://pubmed.ncbi.nlm.nih.gov/32129449/)
- [Understanding neurodevelopmental proteasomopathies... — PubMed](https://pubmed.ncbi.nlm.nih.gov/39220754/)

---

## 7. Anatomical Structures Affected

- **Organ level:** Primary organ affected is the **brain/CNS** (microcephaly, developmental delay, absent language, hypotonia implying central motor-tone dysregulation). Secondary/associated systems: **auditory system** (sensorineural hearing loss), **skeletal/growth system** (short stature, implying either growth-plate or growth-hormone-axis/systemic growth involvement). Behavioral/psychiatric involvement (aggression) implicates frontal-subcortical circuitry, though this is inferred rather than directly imaged/studied.
- **Body systems involved:** Nervous system (primary); auditory system; skeletal/growth system; behavioral/psychiatric domain.
- **Tissue/cell level:** Neural tissue, specifically implicating neural progenitor/developing brain tissue based on the zebrafish model; no human neuropathology (biopsy/autopsy) data were identified.
- **Subcellular level:** Cytoplasmic and nuclear proteasome complexes (GO:0005839 proteasome core complex; the 26S proteasome localizes to both cytoplasm and nucleus).
- **Localization/laterality:** Microcephaly and developmental phenotypes are generalized/bilateral, not lateralized; no asymmetric findings reported.

Suggested ontology terms:
- UBERON:0000955 brain
- UBERON:0001846 statoacoustic ganglion / inner ear structures (hearing loss)
- UBERON:0002481 bone tissue / growth plate (short stature)
- GO:0005634 nucleus; GO:0005737 cytoplasm (proteasome subcellular localization)

Sources:
- [OMIM #620038](https://omim.org/entry/620038)

---

## 8. Temporal Development

- **Onset:** Congenital/early-infantile — microcephaly and hypotonia are apparent from infancy; developmental delay becomes evident in the first years of life; language never develops (absent rather than regressed), indicating a prenatal/perinatal neurodevelopmental origin rather than a later degenerative onset.
- **Onset pattern:** Insidious/static-developmental rather than acute.
- **Progression:** The core neurocognitive phenotype (severe ID, absent language) is described as a fixed developmental deficit rather than a progressive neurodegenerative course — consistent with a primary developmental (proteostasis-during-neurogenesis) mechanism rather than an ongoing neurodegenerative proteotoxic process, though long-term natural history data beyond the original report were not identified.
- **Disease course pattern:** Stable/non-progressive impairment (as far as reported); no remission described.
- **Disease duration:** Chronic, lifelong.
- **Critical periods:** The zebrafish functional data implicate an early embryonic/neurodevelopmental window (neurogenesis and brain morphogenesis) as the critical period of vulnerability to proteasome-assembly failure, consistent with the congenital/postnatal microcephaly phenotype in humans.

Sources:
- [OMIM #620038](https://omim.org/entry/620038)
- [Biallelic variants in PSMB1 — PubMed](https://pubmed.ncbi.nlm.nih.gov/32129449/)

---

## 9. Inheritance and Population

- **Epidemiology:** NEDMHAL is an ultra-rare disorder; to date it has been reported in only one consanguineous family (two affected sisters). No formal prevalence or incidence estimate exists (effectively "cases in literature" = 2, from a single kindred). This should be curated with `measure_type: CASES_IN_LITERATURE` and `prevalence_class: NOT_YET_DOCUMENTED` per the dismech structured-prevalence convention, rather than assigning a numeric rate.
- **Inheritance pattern:** Autosomal recessive.
- **Penetrance:** Appears complete in the two reported homozygous individuals (both affected), though the sample size is too small to formally establish penetrance statistics.
- **Expressivity:** Cannot be assessed robustly from n=2, but the two reported sisters shared the core phenotype, suggesting relatively consistent expressivity, at least within one family/genetic background.
- **Genetic anticipation:** Not applicable/not described (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effects:** Not established; the reported variant arose in a consanguineous Pakistani family, but whether it represents a population-specific founder allele versus a private familial variant has not been determined (absent from gnomAD, so allele-frequency-based founder inference is not currently possible).
- **Consanguinity:** Central to how this family's disease was unmasked — parental consanguinity produced homozygosity for a rare recessive allele, the classic ascertainment route for ultra-rare autosomal recessive proteasomopathies.
- **Carrier frequency:** Unknown/not established (variant not present in gnomAD).
- **Population demographics:** Only described in a Pakistani family to date; no broader ethnic/geographic distribution data exist. Sex ratio: both reported affected individuals are female (sisters), but this reflects the single reported family rather than an established sex bias — X-linked or sex-limited inheritance is not implicated (the gene is autosomal, 6q27).

Sources:
- [Biallelic variants in PSMB1 — PubMed](https://pubmed.ncbi.nlm.nih.gov/32129449/)
- [OMIM #620038](https://omim.org/entry/620038)

---

## 10. Diagnostics

- **Genetic testing (primary diagnostic modality):** Diagnosis is established by molecular genetic testing identifying biallelic (homozygous or compound heterozygous) pathogenic variants in *PSMB1*. In the founding case, diagnosis was made via **whole-exome/genome sequencing** in a consanguineous family with autozygosity mapping/homozygosity — the standard approach for suspected autosomal recessive neurodevelopmental disorders in consanguineous pedigrees.
  - **WES/WGS:** Appropriate first-tier or confirmatory test, especially given the absence of a well-established, larger gene panel specifically curated for this ultra-rare gene.
  - **Gene panels:** *PSMB1* may be included in broader "intellectual disability" or "microcephaly" NGS panels at some diagnostic laboratories, though no dedicated commercial panel was specifically identified in this search.
  - **Single-gene testing:** Feasible via Sanger sequencing once a specific familial variant is known (e.g., for prenatal/carrier testing in a family with a known proband).
  - **Chromosomal microarray/karyotype/FISH:** Not applicable — this is a single-nucleotide-variant disorder, not a CNV/structural disorder, so CMA/karyotype would be expected to be normal and would not establish the diagnosis (useful mainly to exclude alternative CNV etiologies in the differential).
- **Functional/biochemical confirmation:** In the research setting, proteasome assembly/activity assays (e.g., native/glycerol-gradient analysis of 20S/26S complex formation in patient fibroblasts) were used to functionally validate pathogenicity — this is a research-grade rather than routine clinical diagnostic test.
- **Clinical criteria:** No formal consensus clinical diagnostic criteria (e.g., DSM/ICD-style) exist for this molecularly defined ultra-rare disorder; diagnosis is genotype-first.
- **Differential diagnosis:** Given the clinical overlap of "microcephaly + hypotonia + absent language + ID," the differential is broad and includes the many other genetically distinct NEDxxx OMIM entries surfaced in this search (e.g., NEDMISH/FLVCR1, NMIHBA/PRUNE1, NEDHYMS, NEDMILG, NEDTCHAL) as well as other neurodevelopmental proteasomopathies (*PSMC1*, *PSMC3*, *PSMD12*, *PSMD11*-related disorders) — molecular testing is required to distinguish among these phenotypically overlapping but genetically distinct entities.
- **Screening:** No population, newborn, or carrier screening program exists for this ultra-rare condition; carrier screening would only be relevant within a known affected family/at-risk consanguineous relatives once the familial variant is identified.

Sources:
- [Biallelic variants in PSMB1 — PubMed](https://pubmed.ncbi.nlm.nih.gov/32129449/)
- [OMIM search results — related NEDxxx entries](https://omim.org)

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No mortality data reported; the condition has not been described as life-limiting in itself, though no long-term follow-up/life-expectancy data are available given the very recent description (2020) and small cohort.
- **Morbidity/function:** Severe, lifelong functional impairment is implied by absent language, severe intellectual disability, and hypotonia — likely translating to significant motor, communicative, and adaptive-functioning impairment, though no formal functional outcome scales (e.g., Vineland, GMFCS) were reported in the identified literature.
- **Quality of life:** No formal QOL instrument data available.
- **Complications:** Hearing loss and aggressive behavior are described as associated features/complications affecting management; no other organ-system complications (cardiac, renal, hepatic) have been reported.
- **Recovery potential:** None described; the neurodevelopmental phenotype (absent language, severe ID) is not expected to normalize, consistent with a developmental rather than treatable/reversible metabolic block.
- **Prognostic factors/biomarkers:** No validated prognostic biomarkers exist. The broader neurodevelopmental-proteasomopathy review (Cuinat et al. 2024, PMID:39220754) discusses the potential for **proteasome activity assays and interferon-signature biomarkers** as diagnostic/prognostic tools across this gene class generally, but no PSMB1-specific biomarker has been validated.

Sources:
- [OMIM #620038](https://omim.org/entry/620038)
- [Understanding neurodevelopmental proteasomopathies... — PubMed](https://pubmed.ncbi.nlm.nih.gov/39220754/)

---

## 12. Treatment

No disease-specific, mechanism-targeted, or curative therapy exists for NEDMHAL. Management is **supportive and symptomatic**, following the general pattern for severe monogenic neurodevelopmental disorders:

- **Supportive/rehabilitative care:**
  - Early intervention / developmental therapies for global developmental delay
  - Physical therapy for hypotonia and motor development (NCIT:C15302 Physical Therapy)
  - Speech/augmentative-communication therapy given absent language (no specific NCIT code identified for AAC; general speech-language therapy concept applies)
  - Occupational therapy for adaptive functioning
  - Audiology follow-up and hearing aid/amplification evaluation for the sensorineural hearing loss component
  - Behavioral management/intervention for aggressive behavior (NCIT:C15747 Supportive Care; behavioral therapy as a general category)
- **Genetic counseling:** Recommended for families, particularly given the autosomal recessive inheritance and the consanguinity context of the index family (NCIT:C15240 Genetic Counseling); recurrence risk of 25% for future pregnancies in carrier-carrier couples, with prenatal/preimplantation testing feasible once the familial variant is known.
- **Pharmacotherapy:** No PSMB1/NEDMHAL-specific pharmacotherapy exists. No proteasome-activity-modulating drug has been reported in a clinical or preclinical therapeutic context for this specific disorder in the literature identified (note: proteasome *inhibitors*, such as bortezomib, are used therapeutically in oncology/plasma-cell disorders for the *opposite* problem of excess proteasome activity, and are not relevant/applicable here — indeed pharmacologically boosting rather than inhibiting proteasome activity would be the theoretically desired direction, but no such approved or investigational agent for this indication was found).
- **Experimental/clinical trials:** No registered clinical trials specific to PSMB1-NEDMHAL were identified (searches of ClinicalTrials.gov were not directly performed in this pass but no trial references surfaced in general searches).
- **Advanced therapeutics (gene/RNA-based):** None reported or in development for this ultra-rare indication as of this search.

Sources:
- [OMIM #620038](https://omim.org/entry/620038)
- [Understanding neurodevelopmental proteasomopathies... — PubMed](https://pubmed.ncbi.nlm.nih.gov/39220754/)

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (not preventable via risk-factor modification, since it is a fully genetic recessive condition); the only "primary prevention" avenue is reproductive genetic counseling and reduction of consanguineous mating risk awareness in at-risk families, or use of preimplantation genetic testing (PGT-M) once a familial pathogenic variant is identified.
- **Secondary prevention:** Early diagnosis via genetic testing in at-risk consanguineous families or in infants presenting with unexplained microcephaly + hypotonia + developmental delay, enabling earlier initiation of supportive/developmental therapies.
- **Genetic counseling:** The principal "prevention" lever available — informing carrier parents of 25% recurrence risk per pregnancy, and offering prenatal diagnosis (chorionic villus sampling/amniocentesis with targeted variant testing) or PGT-M in future pregnancies once the family's causal variant is known (NCIT:C15240 Genetic Counseling).
- **Carrier/prenatal screening:** No population-based carrier screening exists for this ultra-rare, single-family-described gene; targeted familial carrier testing is the only applicable screening modality currently.
- **Public health/behavioral/immunization/prophylaxis:** Not applicable — no infectious, environmental, or behavioral prevention avenue exists for this monogenic disorder.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring PSMB1-related disease has been reported in non-human species (companion animals, wildlife); OMIA and veterinary literature searches did not surface a natural veterinary corollary in this research pass.
- **Orthologous gene:** *Psmb1* (mouse, MGI:104884, synonym *Lmpc5*); zebrafish *psmb1* ortholog (used experimentally, see below). NCBI Gene entries exist for the mouse ortholog.
- **Comparative biology / model use:** The zebrafish ortholog was used specifically to model human disease (see Section 15) rather than representing a naturally occurring disease in that species.
- **Zoonotic potential/cross-species transmission:** Not applicable — this is a non-infectious monogenic disorder.

Sources:
- [Psmb1 — MGI Mouse Gene Detail](https://www.informatics.jax.org/marker/MGI:104884)

---

## 15. Model Organisms

- **Zebrafish (*Danio rerio*) — primary disease model used to validate pathogenicity:**
  - Both **CRISPR/Cas9-mediated mutagenesis** and **morpholino-mediated knockdown** of the single zebrafish *psmb1* ortholog were performed by Ansar et al. (2020, PMID:32129449).
  - **Phenotype recapitulation:** Both approaches produced **microcephaly and microphthalmia**, with an "overall reduction in brain size and morphologic brain abnormalities" — directly recapitulating the core human microcephaly/neurodevelopmental phenotype, supporting a `RECAPITULATES` model-mechanism link (fidelity likely MODERATE-to-HIGH for the brain-size/microcephaly phenotype specifically; the model cannot assess higher-order human phenotypes such as absent language or aggressive behavior, which have no zebrafish behavioral correlate — a `HUMAN_MODEL_MISMATCH`-type caveat for those specific features).
  - **Limitations:** Zebrafish lack the capacity to model human language/speech or complex behavioral phenotypes (aggression), and morpholino knockdown carries well-known off-target/specificity caveats partially mitigated here by the concordant CRISPR mutant phenotype.
- **Patient-derived human cells (fibroblasts):** Used to directly demonstrate impaired 20S/26S proteasome assembly and function biochemically — a `MEASURES`/`RECAPITULATES`-type human cellular model rather than an animal model, providing the most direct (HIGH fidelity, since it is genuinely patient-derived) mechanistic evidence.
- **Mouse:** No PSMB1-specific mouse knockout/disease model was identified in this search (searches for *Psmb1* mouse knockout phenotype data did not return a dedicated publication describing embryonic lethality or a neurodevelopmental phenotype specifically for *Psmb1*, in contrast to sibling proteasome subunits such as *Psmc1*, *Psmc3*, *Psmc4*, *Psmd4*, *Psmd11*, and *Psmg1*, which have documented embryonic-lethal or neuropathological mouse knockout phenotypes reported in the literature). Given that PSMB1 is a core, obligate structural subunit of the proteasome, a complete knockout would plausibly be embryonic lethal by analogy to these other subunits, but this has not been directly confirmed in the literature identified here and should not be asserted without a direct source.
- **In vitro/other systems:** No organoid, iPSC-derived, or additional invertebrate (*Drosophila*, *C. elegans*, yeast) PSMB1-disease-modeling studies specific to NEDMHAL were identified, though proteasome biology broadly is heavily studied in yeast and *Drosophila* systems for basic mechanism (not disease-modeling) purposes.

Sources:
- [Biallelic variants in PSMB1 — PubMed](https://pubmed.ncbi.nlm.nih.gov/32129449/)
- [Psmb1 — MGI Mouse Gene Detail](https://www.informatics.jax.org/marker/MGI:104884)

---

## Summary and Curation Notes

NEDMHAL (OMIM #620038) is an ultra-rare autosomal recessive proteasome-assembly disorder caused by biallelic *PSMB1* (β6 subunit) variants, defined to date by a single consanguineous family (two affected sisters) carrying a homozygous p.(Tyr103His) variant that destabilizes 20S/26S proteasome assembly (Ansar et al., 2020, *Human Molecular Genetics*, PMID:32129449). It belongs to an emerging disease class termed "neurodevelopmental proteasomopathies," alongside *PSMC1*-, *PSMC3*-, *PSMD11*-, and *PSMD12*-related disorders (Cuinat et al., 2024, *Genes & Diseases*, PMID:39220754). Key curation cautions: (1) do not conflate this with *CDK19*-related DEE87 (OMIM #618916), a phenotypically similar-sounding but molecularly and genetically distinct disorder that surfaced repeatedly in searches — a clear Named-Entity-Confusion risk; (2) given the n=2 evidence base, avoid assigning HPO frequency qualifiers or numeric prevalence rates not supported by the primary literature — use `CASES_IN_LITERATURE`/`NOT_YET_DOCUMENTED`-type structured prevalence values instead; (3) the mouse *Psmb1* knockout phenotype was not confirmed in this search and should not be asserted as embryonic lethal without a direct citation; (4) treatment content should be limited to genuinely supportive/symptomatic and genetic-counseling interventions, since no disease-modifying therapy exists.

**All PMIDs and ontology-term suggestions above should be independently re-verified against PubMed abstracts, OMIM, gnomAD, and OAK/ontology lookups per standard dismech curation SOP before being committed to a KB entry** — several details here (e.g., exact HPO CURIEs, precise ClinVar accession, MONDO cross-reference ID) were inferred/recalled rather than directly confirmed against a live ontology browser in this research pass, and are flagged accordingly above.

**Sources:**
- [OMIM #620038 — NEDMHAL](https://omim.org/entry/620038)
- [OMIM *602017 — PSMB1](https://omim.org/entry/602017)
- [Biallelic variants in PSMB1 encoding the proteasome subunit β6... — PubMed (PMID:32129449)](https://pubmed.ncbi.nlm.nih.gov/32129449/)
- [Understanding neurodevelopmental proteasomopathies as new rare disease entities — PubMed (PMID:39220754)](https://pubmed.ncbi.nlm.nih.gov/39220754/)
- [Understanding neurodevelopmental proteasomopathies... — ScienceDirect full text](https://www.sciencedirect.com/science/article/pii/S2352304223004130)
- [PSMB1 gene — GeneCards](https://www.genecards.org/card/PSMB1)
- [PSMB1 — NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/5689)
- [PSMB1 — UniProt P20618](https://www.uniprot.org/uniprotkb/P20618/entry)
- [Psmb1 — MGI Mouse Gene Detail](https://www.informatics.jax.org/marker/MGI:104884)
- [Biallelic variants in PSMB1 — Human Molecular Genetics (Oxford Academic)](https://doi.org/10.1093/HMG/DDAA032)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.