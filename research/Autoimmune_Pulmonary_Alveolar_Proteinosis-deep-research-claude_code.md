---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-01T23:52:18.036931'
end_time: '2026-08-01T23:56:52.941764'
duration_seconds: 274.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autoimmune Pulmonary Alveolar Proteinosis
  mondo_id: ''
  category: Respiratory Disease
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 18
  num_turns: 20
  total_cost_usd: 1.8668789000000001
  session_id: 4b874b6c-0743-5172-8708-51d0132f07ee
  stop_reason: end_turn
citation_count: 64
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autoimmune Pulmonary Alveolar Proteinosis
- **MONDO ID:**  (if available)
- **Category:** Respiratory Disease

## Research Objectives

Please provide a comprehensive research report on **Autoimmune Pulmonary Alveolar Proteinosis** covering all of the
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

Found it: MONDO:0012579. I now have sufficient sourced material to write the full comprehensive report.

# Autoimmune Pulmonary Alveolar Proteinosis (aPAP): Comprehensive Research Report

## 1. Disease Information

**Overview:** Autoimmune pulmonary alveolar proteinosis (aPAP) is a rare diffuse lung disease characterized by accumulation of surfactant-derived lipoproteinaceous material within alveoli and terminal bronchioles, caused by circulating neutralizing autoantibodies against granulocyte-macrophage colony-stimulating factor (GM-CSF). It accounts for approximately 90% of all pulmonary alveolar proteinosis (PAP) cases, making it the dominant clinical form of the broader PAP syndrome [ATS Journal, Trapnell et al.](https://www.atsjournals.org/doi/full/10.1164/rccm.202112-2742SO). The disease is now understood as "a myeloid cell dysfunction, abnormal pulmonary surfactant accumulation, and innate immune deficiency" driven by autoantibody neutralization of GM-CSF ([Current Pulmonology Reports 2024](https://link.springer.com/article/10.1007/s13665-024-00356-x)).

**Key identifiers:**
- **Orphanet:** ORPHA:747 ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=747); [OLS/ORDO](https://ebi.ac.uk/ols4/ontologies/ordo/classes/http:/www.orpha.net/ORDO/Orphanet_747))
- **MONDO:** MONDO:0012579 (autoimmune pulmonary alveolar proteinosis) — distinct from **MONDO:0012580** (hereditary pulmonary alveolar proteinosis) ([Monarch Initiative](https://monarchinitiative.org/MONDO:0012579))
- **OMIM:** 610910 — "Pulmonary Alveolar Proteinosis, Acquired" ([OMIM](https://omim.org/entry/610910))
- **ICD-10-CM:** J84.01 — Alveolar proteinosis ([ICD10Data](https://www.icd10data.com/ICD10CM/Codes/J00-J99/J80-J84/J84-/J84.01))
- **GARD (NIH):** Disease ID 7499 ([GARD](https://rarediseases.info.nih.gov/diseases/7499/autoimmune-pulmonary-alveolar-proteinosis)) — aggregates Orphanet, OMIM, and MONDO data

**Synonyms:** Acquired pulmonary alveolar proteinosis; primary autoimmune PAP; idiopathic PAP (older term, largely superseded now that the GM-CSF autoantibody mechanism is understood); aPAP.

**Data derivation:** Most published knowledge derives from aggregated disease-level resources — national/regional patient registries (notably Japanese nationwide cohorts), single- and multi-center case series, and a handful of randomized controlled/phase 3 trials (IMPALA, IMPALA-2) — rather than large-scale individual-level EHR mining, reflecting the disease's rarity.

---

## 2. Etiology

**Primary cause:** aPAP is caused by polyclonal, high-titer, neutralizing IgG autoantibodies directed against GM-CSF. These autoantibodies bind and block GM-CSF from engaging its receptor (CSF2RA/CSF2RB) on alveolar macrophages and other myeloid cells, abrogating GM-CSF-dependent alveolar macrophage terminal differentiation and surfactant catabolism ([Nature Communications 2015](https://www.nature.com/articles/ncomms8375); [PMC8647160](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8647160/)). Recent work shows that **total autoantibody titer does not correlate with disease severity**; rather, **epitope specificity and binding affinity** are the key determinants of pathogenicity — a 2026 Nature Communications study characterized "affinity- and epitope-dependent pathogenicity of GM-CSF autoantibodies" ([Nature Communications 2026](https://www.nature.com/articles/s41467-026-74717-2)).

**Genetic risk factors:** A genome-wide association study of 198 Japanese aPAP patients versus 395 controls identified two independent MHC risk loci:
- **HLA-DRB1\*08:03** (OR 5.2) — also associated with higher anti-GM-CSF antibody titers
- **HLA-DPβ1** epitope (OR 0.28, protective)
([Nature Communications 2021, "Genetic determinants of risk in autoimmune pulmonary alveolar proteinosis"](https://www.nature.com/articles/s41467-021-21011-y); [PMC7884840](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7884840/)).

However, this HLA association has **not been consistently replicated**: a separate study of 41 aPAP patients versus 1,000 ethnic-matched controls found no HLA association ([PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0213179); [PMC6405167](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6405167/)), suggesting population-specific or study-power-dependent genetic architecture.

**Environmental/lifestyle risk factors:**
- **Age and cigarette smoking** are established risk factors for aPAP; smoking and dust inhalation are hypothesized to accelerate onset ([ATS Journal review](https://www.atsjournals.org/doi/full/10.1164/rccm.202112-2742SO)). A case report documented fluctuating radiographic disease burden tracking with cigarette smoke exposure ([PMC7170098](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170098/)).
- **Occupational/inhalational exposures** (silica, aluminum dust) are more clearly linked to *secondary* PAP than to autoimmune PAP; in a German cohort, silica dust exposure was reported in 21% and aluminum dust in 18% of cases, though causal attribution to the autoimmune subtype specifically remains uncertain.
- Vaping/e-cigarette exposure and vitamin E acetate have been reported in individual case reports of aPAP ([PMC8521389](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8521389/)).

**Gene-environment interactions:** The prevailing model is a "two-hit" framework — an HLA-conferred (or otherwise genetically determined) predisposition to break tolerance to GM-CSF, combined with an environmental trigger (inhalational exposure, infection, or another autoimmune process) that precipitates autoantibody production. This remains incompletely characterized mechanistically and is an area of active investigation.

**Protective factors:** No specific protective genetic or environmental factors are firmly established beyond the HLA-DPβ1 protective epitope noted above.

---

## 3. Phenotypes

**Symptom onset and course:** Onset is typically insidious/gradual in patients aged 20–50 years, though pediatric and elderly-onset cases occur ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=747); [GARD](https://rarediseases.info.nih.gov/diseases/7499/autoimmune-pulmonary-alveolar-proteinosis)).

| Phenotype | Frequency/notes | Suggested HPO term |
|---|---|---|
| Dyspnea (exertional progressing to rest) | Most common presenting symptom | HP:0002094 (Dyspnea) |
| Cough (dry or with whitish/frothy sputum) | Second most common symptom | HP:0012735 (Cough) |
| Fatigue | Common | HP:0012378 (Fatigue) |
| Weight loss | Occurs with disease progression | HP:0001824 (Weight loss) |
| Chest pain | Reported | HP:0100749 (Chest pain) |
| Low-grade fever | Reported, especially with superimposed infection | HP:0001945 (Fever) |
| Hemoptysis | Uncommon | HP:0002105 (Hemoptysis) |
| Crackles on auscultation | Fine bibasilar crackles common | HP:0030830 (Crackles) |
| Hypoxemia | Progressive with disease severity | HP:0012418 (Hypoxemia) |
| Cyanosis | Late/severe disease | HP:0000961 (Cyanosis) |
| Digital clubbing | **Uncommon/atypical** — its presence should prompt consideration of alternative or complicating diagnoses (e.g., fibrosis) | HP:0100759 (Clubbing) |
| Asymptomatic/incidental finding | Up to ~30% identified incidentally on imaging | — |

Source: [GARD](https://rarediseases.info.nih.gov/diseases/7499/autoimmune-pulmonary-alveolar-proteinosis), [NORD](https://rarediseases.org/rare-diseases/autoimmune-pulmonary-alveolar-proteinosis/), [Cleveland Clinic](https://my.clevelandclinic.org/health/diseases/17398-pulmonary-alveolar-proteinosis), [PMC12180566 "Dyspnea and Deception"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12180566/).

**Severity and progression:** Disease course is heterogeneous — ranging from spontaneous remission, to stable/indolent disease, to progressive respiratory failure. Severity correlates with radiographic burden (crazy-paving extent on HRCT), gas exchange parameters (PaO2, A-a gradient), and DLCO. Chinese multi-center cohorts have developed composite severity/prognosis scores (DSS, SPSP, and an updated SPSPII incorporating smoking status, symptoms, PaO2, %-predicted DLCO, and HRCT score) that outperform earlier single-parameter staging ([PMC9941621](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9941621/)).

**Quality of life impact:** Progressive dyspnea and fatigue substantially impair daily functioning; disease-specific QoL instruments are not well standardized in aPAP, and most QoL data come from case series rather than validated instruments (EQ-5D/SF-36 data are sparse in the primary literature).

---

## 4. Genetic/Molecular Information

Unlike hereditary PAP, autoimmune PAP is **not a Mendelian genetic disease** — no single causal gene mutation is required. However:

- **HLA-DRB1\*08:03** and **HLA-DPβ1** are associated risk/protective MHC alleles in at least one large Japanese GWAS (see Etiology, above) ([Nature Communications 2021](https://www.nature.com/articles/s41467-021-21011-y)).
- **MUC1 gene polymorphisms** are associated with serum KL-6 levels and degree of pulmonary dysfunction in PAP, acting as a modifier of the biomarker/severity relationship rather than a causal driver ([PMC4841967](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4841967/)).
- The causal molecular lesion is **autoantibody-mediated functional GM-CSF deficiency** rather than a structural gene defect — functionally analogous to but molecularly distinct from hereditary PAP (CSF2RA/CSF2RB loss-of-function mutations; HGNC:2435/HGNC:2436) and to the original description of PAP as a state where "GM-CSF gene expression is normal but protein release is absent" in some contexts ([PubMed 9412586](https://pubmed.ncbi.nlm.nih.gov/9412586/)).
- **Somatic vs. germline:** The autoantibodies are a somatically generated (B-cell/plasma-cell derived), polyclonal humoral immune product — not a germline or somatic DNA lesion.
- Relevant gene/protein identifiers: **CSF2** (GM-CSF ligand, HGNC:2434), **CSF2RA** (HGNC:2435), **CSF2RB** (HGNC:2436), **PPARG** (HGNC:9236), **ABCG1** (HGNC:14638), **PU.1/SPI1** (HGNC:11241) — all implicated in the downstream signaling/lipid-clearance axis (see Mechanism, below).

**Epigenetics:** No well-established disease-specific epigenetic signature has been reported in the primary literature reviewed; this remains an evidence gap.

---

## 5. Environmental Information

- **Toxin/occupational exposures:** Silica and aluminum dust are the most frequently implicated inhalational hazards in cohorts that include PAP broadly, though their causal role is more firmly established for secondary PAP than for the autoimmune subtype specifically.
- **Smoking:** An established accelerant/risk factor, with case evidence of disease activity fluctuating with smoking exposure ([PMC7170098](https://pmc.ncbi.nlm.nih.gov/articles/PMC7170098/)).
- **Vaping/inhalant substance use:** Case reports link vaping and chronic inhalant/substance abuse to PAP presentations, including one describing vitamin E-acetate-positive BAL fluid in a vaping-associated aPAP case ([PMC8521389](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8521389/); [PMC5828087](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5828087/)).
- **Infectious agents:** Infections are not established as causal triggers of aPAP itself, but the GM-CSF-autoantibody state independently and bidirectionally interacts with infection risk (see Mechanism/Diagnostics — opportunistic infection section). Notably, GM-CSF autoantibodies have been identified in patients presenting primarily with **disseminated nocardiosis, cryptococcal meningitis, and disseminated mycobacterial infection**, sometimes in the absence of overt PAP ([PMC9552154](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9552154/); [JACI 2024](https://www.jacionline.org/article/S0091-6749(24)01381-2/fulltext); [J Clin Immunol 2024](https://link.springer.com/article/10.1007/s10875-024-01775-w)).

---

## 6. Mechanism / Pathophysiology

**Causal chain (trigger → clinical manifestation):**

1. **Trigger/upstream:** Loss of immune tolerance to GM-CSF (influenced by HLA-DRB1\*08:03 and possibly environmental co-factors) → polyclonal B-cell production of high-affinity, epitope-specific neutralizing anti-GM-CSF IgG autoantibodies ([Nat Commun 2026](https://www.nature.com/articles/s41467-026-74717-2)).
2. **Molecular pathway disruption:** Circulating autoantibodies bind and neutralize/clear serum and local GM-CSF, preventing engagement of the GM-CSF receptor (CSF2RA/CSF2RB heterodimer) on alveolar macrophages. GM-CSF receptor signaling normally operates through two concentration-dependent branches: at low ligand concentration, phosphorylation of receptor serine585 couples to 14-3-3/PI3K/Akt signaling; at high concentration, phosphorylation of tyrosine577 couples to STAT5- and Shc-dependent pathways driving macrophage survival, activation, and proliferation ([review, PMC11241585](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11241585/)).
3. **Cellular consequence:** Loss of GM-CSF signaling impairs alveolar macrophage **terminal differentiation**, in particular failure to upregulate **PU.1 (SPI1)** and **PPAR-γ**, which are required for the **GM-CSF–PU.1–PPARγ–ABCG1 axis** governing cholesterol/lipid efflux and surfactant lipid catabolism in alveolar macrophages ([PMC8647160](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8647160/); ATS Journal mechanistic review). Disruption of this axis is described as "dysregulation of cholesterol export within alveolar macrophages," where cholesterol accumulation impedes surfactant clearance ([Current Pulmonology Reports 2024](https://link.springer.com/article/10.1007/s13665-024-00356-x)).
4. **Tissue-level consequence:** Progressive accumulation of PAS-positive, lipid-rich (oil-red-O-positive) surfactant material within alveolar macrophages and free within alveolar spaces → alveolar filling, impaired gas exchange, and the radiographic "crazy-paving" pattern.
5. **Downstream/organism-level:** Restrictive-to-mixed physiology, hypoxemia, and in a subset of patients, secondary **pulmonary fibrosis** — hypothesized to result from chronic retained lipoproteinaceous material, silica co-exposure, and/or superimposed infection causing epithelial injury ([ERS 2024, "Pulmonary fibrosis in patients with autoimmune pulmonary alveolar proteinosis"](https://publications.ersnet.org/content/erjor/10/6/00314-2024)). Hyaluronan has also been implicated in the fibrogenic cascade in aPAP-associated fibrosis ([PMC12440733](https://pmc.ncbi.nlm.nih.gov/articles/PMC12440733/)).

**Immune system involvement:** aPAP is now conceptually framed as a combined **autoimmune disease + acquired innate immunodeficiency**: the same autoantibodies that drive alveolar macrophage dysfunction also impair GM-CSF-dependent functions in circulating **neutrophils** (phagocytosis, chemotaxis, microbicidal activity) and other myeloid cells, producing a state of susceptibility to opportunistic infection independent of overt lung disease severity ([PMC8647160](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8647160/)).

**Cell types involved (Cell Ontology suggestions):**
- Alveolar macrophage — CL:0000583
- Type II pneumocyte (surfactant-producing) — CL:0002063
- Neutrophil — CL:0000775
- Plasma cell (autoantibody-producing) — CL:0000786

**GO biological process suggestions:**
- Surfactant homeostasis — GO:0043129
- Macrophage differentiation — GO:0030225
- Cholesterol efflux — GO:0033344
- Regulation of phagocytosis — GO:0050764
- Humoral immune response — GO:0006959

**Molecular profiling:** Serum and BAL proteomic/biomarker studies (KL-6, SP-A, SP-D, CYFRA21-1, CEA, LDH) are the primary "omics" layer characterized to date (see Diagnostics, below); large-scale transcriptomic/single-cell atlases specific to aPAP alveolar macrophages are limited in the literature surfaced here and represent a research gap.

---

## 7. Anatomical Structures Affected

- **Primary organ:** Lung (respiratory system), specifically the **alveoli and terminal bronchioles** — UBERON:0002048 (lung); UBERON:0002299 (alveolar system); UBERON:0001991 (pulmonary alveolus)
- **Secondary/systemic involvement:** Because GM-CSF autoantibodies impair neutrophil function systemically, extrapulmonary sites of **opportunistic infection** occur — notably CNS (Nocardia and Cryptococcal CNS infection) and disseminated mycobacterial disease, representing a secondary/complication-driven organ involvement rather than primary pathophysiology.
- **Tissue/cell level:** Alveolar epithelium (type II pneumocytes, surfactant source) and alveolar macrophages (the primary dysfunctional effector cell) — Cell Ontology terms above.
- **Subcellular level:** Macrophage lysosomes/phagolysosomes (site of impaired surfactant lipid catabolism) — GO:0005764 (lysosome); mitochondria and lipid droplets in lipid-laden ("foamy") macrophages.
- **Localization/laterality:** Diffuse, typically bilateral, often basal-predominant or perihilar "bat-wing" distribution on imaging; classically patchy with sharp demarcation between affected and unaffected lung ("geographic" distribution).

---

## 8. Temporal Development

- **Onset:** Typically insidious in adults 20–50 years old; pediatric-onset and elderly-onset (including cases in the 70s–80s) reported, the latter sometimes overlapping in presentation with hereditary PAP work-up.
- **Progression:** Variable — a substantial minority follow an indolent/stable course, some undergo spontaneous remission, and others progress to hypoxemic respiratory failure. Disease severity scoring systems (DSS, SPSP, updated SPSPII) stratify HRCT extent, PaO2, and DLCO to track progression ([PMC9941621](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9941621/)).
- **Complications over time:** Pulmonary fibrosis develops in a variable proportion of patients over years of follow-up — reported rates range widely (1.4% with severe fibrotic respiratory failure in a 223-patient Japanese cohort, versus 26% with any fibrosis on CT at median 3.6 years follow-up in another cohort), reflecting differences in fibrosis definition/detection threshold across studies ([ERS 2024](https://publications.ersnet.org/content/erjor/10/6/00314-2024)).
- **Remission patterns:** Both spontaneous and treatment-induced (post-WLL, post-GM-CSF therapy) remission are documented; relapse can occur, particularly if autoantibody titers/affinity remain elevated.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Not Mendelian — aPAP is an acquired autoimmune disease, though HLA-linked genetic susceptibility modifies risk (see Etiology).
- **Prevalence:** Estimates vary substantially by region and case-ascertainment method:
  - Japan: ~1/38,000 (higher due to a national registry and greater case-finding) ([NORD](https://rarediseases.org/rare-diseases/autoimmune-pulmonary-alveolar-proteinosis/))
  - United States: ~1/150,000 (likely an underestimate due to underdiagnosis)
  - A separate cross-national estimate: PAP prevalence 6.87 ± 0.33 per million population overall, similar between sexes, increasing with age ([Orphanet J Rare Dis 2018](https://link.springer.com/article/10.1186/s13023-018-0846-y); [PMC6069872](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6069872/))
  - A 2025 Japanese administrative claims database study provides updated national epidemiology ([PubMed 39872388](https://pubmed.ncbi.nlm.nih.gov/39872388/))
- **Sex ratio:** Historically described with male predominance, though more recent population-level data suggest near-equal sex distribution once ascertainment bias is accounted for.
- **Age distribution:** Peak presentation 20–50 years; pediatric and elderly-onset cases occur but are less common.
- **Founder effects/consanguinity/carrier frequency:** Not applicable — these concepts apply to the hereditary (CSF2RA/CSF2RB) form, not autoimmune PAP.
- **Geographic distribution:** No strong endemic geographic clustering reported beyond registry-driven detection differences (Japan's higher reported prevalence reflects a mature national PAP registry rather than a true regional excess).

---

## 10. Diagnostics

**Imaging:** High-resolution CT (HRCT) shows the classic **"crazy-paving" pattern** — ground-glass opacities with superimposed interlobular septal thickening — often with sharp geographic demarcation between affected and normal parenchyma ([AJR](https://ajronline.org/doi/10.2214/ajr.176.5.1761287); [PMC5354367](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5354367/)). Quantitative CT scoring correlates with pulmonary function test results.

**Bronchoalveolar lavage (BAL):** Usually diagnostic without biopsy. Lavage fluid is grossly **milky/opaque**; cytology shows large, foamy alveolar macrophages and extracellular eosinophilic proteinaceous material that is **PAS-positive and Alcian-blue-negative**, with oil-red-O-positive lipid content ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK482308/); [Hindawi CRJ 2016](https://www.hindawi.com/journals/crj/2016/4064539/)).

**Serologic diagnosis:** Elevated serum anti-GM-CSF autoantibody titer (typically measured by ELISA) is considered diagnostic/confirmatory for the autoimmune subtype and distinguishes it from hereditary and secondary PAP.

**Serum biomarkers (disease activity/monitoring):**
- **KL-6** (high-molecular-weight MUC1 mucin) — elevated in serum and BAL in most aPAP patients, correlates with disease activity, decreases post-WLL, and is a validated **predictor of outcome/mortality** ([Orphanet J Rare Dis 2013](https://link.springer.com/article/10.1186/1750-1172-8-53); [PMC3629718](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3629718/)). MUC1 polymorphisms modify baseline KL-6 levels ([PMC4841967](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4841967/)).
- **SP-A and SP-D** (surfactant proteins) — elevated; SP-A/SP-D show transient post-WLL rises distinct from KL-6's decline pattern.
- **CYFRA21-1** — reported as a more sensitive severity biomarker than some traditional markers ([PMC8725332](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8725332/)).
- **LDH, CEA, CA15-3, NSE** — correlate positively with disease severity score and A-a gradient in Chinese cohort studies.

**Genetic/molecular testing:** Not required for diagnosis of the autoimmune form per se, but CSF2RA/CSF2RB sequencing is used to exclude hereditary PAP, particularly in atypical-age presentations or when anti-GM-CSF antibodies are unexpectedly negative.

**Suggested LOINC/SNOMED considerations:** BAL cytology PAS stain, serum KL-6 assay, and anti-GM-CSF antibody assay are the key laboratory studies; specific LOINC codes should be confirmed against local lab compendia at curation time.

**Differential diagnosis:** Hereditary PAP (CSF2RA/CSF2RB mutation, GM-CSF-antibody-negative, earlier onset), secondary PAP (hematologic malignancy, immunodeficiency, chronic infection, pneumotoxic exposure — macrophage number/function reduced by an underlying condition rather than autoantibody-mediated), other interstitial lung diseases with ground-glass/crazy-paving patterns (e.g., NSIP, organizing pneumonia, lipoid pneumonia, PJP pneumonia).

**Complications requiring diagnostic vigilance:** Because of the associated innate immune deficiency, clinicians are advised to maintain a high index of suspicion for **opportunistic infection** (Nocardia, Cryptococcus, nontuberculous/tuberculous mycobacteria) in patients with elevated GM-CSF autoantibodies, even in the absence of classic PAP radiographic findings ([Open Forum Infect Dis 2022](https://academic.oup.com/ofid/article/9/5/ofac146/6565987)).

---

## 11. Outcome/Prognosis

- **Survival:** Approximately **80% five-year survival with treatment** (GARD/NORD estimates). Disease course ranges from spontaneous remission through chronic stable disease to death from respiratory failure or secondary infection.
- **Mortality drivers:** Progressive hypoxemic respiratory failure; secondary pulmonary fibrosis (a "rare but potentially life-threatening complication," with severe fibrotic respiratory failure in ~1.4% of a 223-patient Japanese cohort); opportunistic infection (disseminated nocardiosis, cryptococcal meningitis, mycobacterial disease) related to the GM-CSF-antibody-driven innate immune defect.
- **Prognostic biomarkers:** Serum KL-6 is a validated predictor of outcome ([PMC3629718](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3629718/)); composite severity scores (DSS/SPSP/SPSPII incorporating HRCT score, PaO2, %-predicted DLCO, smoking status) predict prognosis and treatment response in Chinese multi-center cohorts ([PMC9941621](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9941621/)).
- **Recovery potential:** WLL and GM-CSF augmentation therapy substantially improve gas exchange and reduce disease burden; complete resolution occurs in only ~30% with WLL alone, improved further by combination with inhaled GM-CSF therapy.
- **COVID-19 interaction:** A single-center study specifically examined outcomes of COVID-19 infection in aPAP patients, relevant given the innate immune deficiency component of the disease ([PMC10638736](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10638736/)).

---

## 12. Treatment

**First-line — Whole Lung Lavage (WLL):** Remains the standard of care; performed under general anesthesia, sequential lavage of each lung with large-volume saline to mechanically remove accumulated surfactant material. WLL alone achieves complete resolution in only ~30% of patients ([CHEST/journal.chestnet.org](https://journal.chestnet.org/article/S0012-3692(25)05502-3/abstract)). NCIT suggestion: therapeutic bronchoalveolar lavage procedure (closest available NCIT clinical-intervention term should be verified via OAK, e.g. under Therapeutic Procedure NCIT:C49236).

**GM-CSF augmentation therapy (pharmacotherapy, pathogenesis-driven):**
- **Inhaled sargramostim** (recombinant human GM-CSF) — restores alveolar macrophage GM-CSF signaling/function locally, bypassing circulating neutralizing antibodies to some degree. A phase II randomized trial showed inhaled sargramostim following WLL reduced need for repeat WLL, improved lung function, and was safe and more effective than WLL alone ([PubMed 37973175](https://pubmed.ncbi.nlm.nih.gov/37973175/); [NEJM 2019](https://www.nejm.org/doi/full/10.1056/NEJMoa1913590)).
- **Inhaled molgramostim** (recombinant GM-CSF, Savara Inc.) — the most advanced pharmacotherapy in development:
  - Phase 2/3 **IMPALA** trial: NEJM 2020 ([NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa1816216))
  - Phase 3 **IMPALA-2** trial (164 patients, 300 μg once daily × 48 weeks): significantly greater improvement in DLCO (hemoglobin-adjusted, % predicted at week 24, primary endpoint) versus placebo ([NEJM 2025](https://www.nejm.org/doi/full/10.1056/NEJMoa2410542); [PubMed 40834301](https://pubmed.ncbi.nlm.nih.gov/40834301/); [plain-language summary](https://www.tandfonline.com/doi/full/10.1080/21548331.2024.2367955))
  - Regulatory status (as of the search date): BLA (brand name **Molbreevi**) submitted to FDA December 2025; PDUFA target action date extended to **November 22, 2026**; an FDA-permitted Early Access Program has been running since September 2024 ([Drugs.com](https://www.drugs.com/history/molbreevi.html); [CHEST Physician](https://www.chestphysician.org/phase-3-impala-2-clinical-trial-shows-inhaled-molgramostim-promising-for-autoimmune-pulmonary-alveolar-proteinosis/)). **Not yet FDA-approved** at time of this report.

**Refractory disease (per ERS treatment sequencing):** 
1. WLL 
2. Inhaled GM-CSF 
3. **Rituximab** (anti-CD20 B-cell depletion, typically 1000 mg × 2 doses two weeks apart) — reduces anti-GM-CSF titers, improves oxygenation, decreases WLL frequency
4. **Plasmapheresis** — case-level evidence of reduced anti-GM-CSF antibody levels (e.g., 24.8 → 2.7 mcg/mL after a 5-day protocol) correlating with reduced WLL need, improved DLCO, and symptomatic benefit, though responses are inconsistent across reported cases; some patients remain refractory to both rituximab and plasmapheresis despite antibody reduction ([PMC8818429](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8818429/); [PubMed 25557091](https://pubmed.ncbi.nlm.nih.gov/25557091/))
   ([Drugs journal 2025, pharmacotherapy review](https://link.springer.com/article/10.1007/s40265-025-02228-3))

**Advanced/last-resort:** **Lung transplantation** for suitable patients with severe disease refractory to all other therapies; notably, PAP recurrence post-transplant has been reported ([PMC7199162](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7199162/)).

**Suggested NCIT terms:**
- Rituximab — NCIT:C1197 (verify via OAK)
- Plasmapheresis — closest NCIT therapeutic-procedure term (verify)
- Lung transplantation — NCIT:C15289 (Organ Transplantation)
- Pharmacotherapy (generic, for GM-CSF biologics) — NCIT:C15986, with `therapeutic_agent` bound to sargramostim/molgramostim (CHEBI or NCIT drug term — verify exact identifiers via OAK before curation)

**Emerging/experimental:** Pulmonary macrophage transplantation has shown efficacy in preclinical (murine Csf2ra−/−) models of hereditary PAP and is conceptually relevant as a future cell-therapy direction, though this is currently demonstrated in the hereditary rather than autoimmune model system.

---

## 13. Prevention

No established primary prevention (e.g., vaccination) exists for aPAP, as the autoimmune trigger is not fully characterized. Reasonable extrapolated measures based on identified risk factors:
- **Smoking cessation counseling** — since smoking is an established risk/aggravating factor
- **Avoidance of inhalational occupational hazards** (silica, aluminum dust) where feasible, particularly relevant to reducing secondary-PAP risk and possibly aPAP severity/fibrosis progression
- **Secondary prevention/surveillance:** Given the innate immune deficiency, clinicians monitoring known aPAP or GM-CSF-autoantibody-positive patients should maintain heightened surveillance for opportunistic infection (Nocardia, Cryptococcus, mycobacteria), enabling earlier detection and treatment of disseminated infection.
- **Genetic counseling:** Not applicable in the classic sense (non-Mendelian), though differentiating from hereditary PAP is relevant for family counseling when hereditary PAP is in the differential.

---

## 14. Other Species / Natural Disease

- Naturally occurring autoimmune PAP driven by spontaneous anti-GM-CSF autoantibodies has not been robustly documented as a natural veterinary disease in the literature surfaced by this search; PAP-like presentations in animals are more typically studied via engineered genetic models (below) rather than spontaneous autoimmune disease.
- Comparative biology of the GM-CSF/alveolar macrophage axis is well conserved across mammals, underpinning the utility of mouse models (below).

---

## 15. Model Organisms

**GM-CSF-deficient (Csf2−/−) mice:** The original and foundational model. GM-CSF knockout mice spontaneously develop a PAP-like phenotype due to defective surfactant clearance from failure of alveolar macrophage terminal differentiation, closely paralleling human PAP pathology, with impaired innate immunity to pulmonary pathogens as a shared feature ([BMC Immunology 2013, "mixed M1/M2 phenotypes"](https://bmcimmunol.biomedcentral.com/articles/10.1186/1471-2172-14-41)).

**Csf2ra−/− mice (hereditary PAP model, mechanistically relevant to the shared downstream pathway):** A more recent, refined murine model in which macrophages cannot bind or signal through GM-CSF, exhibiting functional defects in phagocytosis, cholesterol clearance, and surfactant clearance; mice develop time-dependent, progressive lung disease closely paralleling human hereditary PAP clinical, physiological, histopathological, biochemical, and biomarker features ([Am J Physiol Lung Cell Mol Physiol 2021](https://journals.physiology.org/doi/full/10.1152/ajplung.00175.2021)). This model has been used to test **pulmonary macrophage transplantation (PMT)** without myeloablation, achieving long-term engraftment and durable restoration of GM-CSF responsiveness over 6 months of follow-up.

**Humanized IL-3/GM-CSF knock-in mice:** Engineered to express human IL-3/GM-CSF, supporting human alveolar macrophage development and human immune responses in the lung — a translational bridge model for studying human myeloid biology in vivo ([PNAS 2011](https://www.pnas.org/doi/10.1073/pnas.1019682108); [PMC3038773](https://pmc.ncbi.nlm.nih.gov/articles/PMC3038773/)).

**Model limitations:** None of these genetic models fully recapitulates the **autoimmune** (autoantibody-driven, HLA-associated) etiology of human aPAP — they model the shared *downstream* GM-CSF-signaling-loss pathophysiology rather than the *upstream* autoimmune breakdown of tolerance. A true autoantibody-mediated aPAP model (e.g., passive transfer of anti-GM-CSF antibodies, or an induced-autoimmunity model) was not identified as a well-established standard model in this search and represents a documented modeling gap — relevant to a `HUMAN_MODEL_MISMATCH` framing if curated into a mechanistic knowledge base, since model organisms recapitulate the surfactant-clearance/macrophage-dysfunction phenotype but not the autoimmune trigger itself.

**Resources:** MGI (Mouse Genome Informatics) for Csf2/Csf2ra/Csf2rb knockout allele records; IMPC/KOMP for conditional/knockout mouse line availability.

---

## Summary of Suggested Ontology Terms for Curation

| Category | Term |
|---|---|
| Disease | MONDO:0012579 (autoimmune PAP); ORPHA:747; OMIM:610910; ICD-10-CM:J84.01 |
| Related/differential disease | MONDO:0012580 (hereditary PAP) |
| Causal gene/protein (ligand) | CSF2 / GM-CSF, HGNC:2434 |
| Receptor genes | CSF2RA (HGNC:2435), CSF2RB (HGNC:2436) |
| Downstream TFs/transporters | SPI1/PU.1 (HGNC:11241), PPARG (HGNC:9236), ABCG1 (HGNC:14638) |
| Key phenotype (HP) | Dyspnea HP:0002094; Cough HP:0012735; Hypoxemia HP:0012418; Crackles HP:0030830 |
| Key cell types (CL) | Alveolar macrophage CL:0000583; Type II pneumocyte CL:0002063; Neutrophil CL:0000775 |
| Key anatomy (UBERON) | Lung UBERON:0002048; Pulmonary alveolus UBERON:0001991 |
| Key GO processes | Surfactant homeostasis GO:0043129; Macrophage differentiation GO:0030225; Cholesterol efflux GO:0033344 |
| Treatments (NCIT, verify via OAK before use) | Pharmacotherapy NCIT:C15986; Organ Transplantation NCIT:C15289 |

*(All ontology term IDs above should be independently verified against the live OAK adapters before insertion into any dismech YAML entry, per project SOP — this report is a research input, not pre-validated curation content.)*

---

## Notes on Evidence Gaps

- No MONDO/Orphanet-listed formal ICD-11 mapping was independently confirmed in this pass (ICD-10-CM J84.01 was confirmed; the ICD-11 equivalent should be separately verified).
- Precise 5-year survival and mortality figures come from patient-advocacy/aggregator summaries (NORD/GARD) rather than a single primary epidemiological study with a directly quotable abstract sentence — a primary-source survival curve (e.g., from a national registry cohort paper) should be sourced and quoted verbatim before use as curated evidence.
- A dedicated autoantibody-mediated (rather than genetic-knockout) mouse/model-organism system for aPAP was not identified; this is a genuine translational gap, not a search omission.
- HLA association findings are population-inconsistent (positive in one Japanese GWAS, negative in another cohort) — this contradiction should be preserved as a `KNOWLEDGE_GAP`/nuanced etiology claim rather than flattened to a single "HLA-DRB1\*08:03 causes aPAP" statement.

Sources:
- [Affinity- and epitope-dependent pathogenicity of GM-CSF autoantibodies (Nat Commun 2026)](https://www.nature.com/articles/s41467-026-74717-2)
- [The Role of GM-CSF Autoantibodies in Infection and Autoimmune PAP: A Concise Review (PMC8647160)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8647160/)
- [Inhaled GM-CSF for Pulmonary Alveolar Proteinosis (NEJM 2020)](https://www.nejm.org/doi/full/10.1056/NEJMoa1816216)
- [Autoimmune Pulmonary Alveolar Proteinosis (ATS Journal, State of the Art review)](https://www.atsjournals.org/doi/full/10.1164/rccm.202112-2742SO)
- [Neutralization and clearance of GM-CSF by autoantibodies in PAP (Nat Commun 2015)](https://www.nature.com/articles/ncomms8375)
- [Orphanet: Autoimmune pulmonary alveolar proteinosis (ORPHA:747)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=747)
- [GARD: Autoimmune pulmonary alveolar proteinosis](https://rarediseases.info.nih.gov/diseases/7499/autoimmune-pulmonary-alveolar-proteinosis)
- [Prevalence and healthcare burden of pulmonary alveolar proteinosis (Orphanet J Rare Dis 2018)](https://link.springer.com/article/10.1186/s13023-018-0846-y)
- [Epidemiology of PAP: Japanese administrative claims database (PubMed 39872388)](https://pubmed.ncbi.nlm.nih.gov/39872388/)
- [OMIM 610910: Pulmonary Alveolar Proteinosis, Acquired](https://omim.org/entry/610910)
- [Monarch Initiative: MONDO:0012579](https://monarchinitiative.org/MONDO:0012579)
- [Monarch Initiative: MONDO:0012580 (hereditary PAP)](https://monarchinitiative.org/MONDO:0012580)
- [ICD10Data: J84.01 Alveolar proteinosis](https://www.icd10data.com/ICD10CM/Codes/J00-J99/J80-J84/J84-/J84.01)
- [Inhaled recombinant GM-CSF reduces need for WLL (PubMed 37973175)](https://pubmed.ncbi.nlm.nih.gov/37973175/)
- [Inhaled Molgramostim Therapy in aPAP (NEJM 2019)](https://www.nejm.org/doi/full/10.1056/NEJMoa1913590)
- [Whole Lung Lavage in PAP (CHEST)](https://journal.chestnet.org/article/S0012-3692(25)05502-3/abstract)
- [Pulmonary alveolar proteinosis, a primary immunodeficiency of impaired GM-CSF stimulation of macrophages (PubMed 19796925)](https://pubmed.ncbi.nlm.nih.gov/19796925/)
- [A Comprehensive Outlook on Pulmonary Alveolar Proteinosis (PMC11241585)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11241585/)
- [Pathogenesis-driven treatment of primary PAP (ERS review)](https://publications.ersnet.org/content/errev/33/173/240064)
- [CT Features of Pulmonary Alveolar Proteinosis (AJR)](https://ajronline.org/doi/10.2214/ajr.176.5.1761287)
- [Dyspnea and Deception: Overcoming Diagnostic Hurdles in PAP (PMC12180566)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12180566/)
- [Serum KL-6 is a predictor of outcome in PAP (Orphanet J Rare Dis 2013 / PMC3629718)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3629718/)
- [MUC1 gene polymorphisms and serum KL-6 in PAP (PMC4841967)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4841967/)
- [CYFRA21-1 as a sensitive severity biomarker in PAP (PMC8725332)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8725332/)
- [Genetic determinants of risk in autoimmune PAP (Nat Commun 2021)](https://www.nature.com/articles/s41467-021-21011-y)
- [PAP: an autoimmune disease lacking an HLA association (PLOS ONE / PMC6405167)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6405167/)
- [A murine model of hereditary PAP caused by Csf2ra disruption (Am J Physiol Lung Cell Mol Physiol 2021)](https://journals.physiology.org/doi/full/10.1152/ajplung.00175.2021)
- [Human IL-3/GM-CSF knock-in mice support human alveolar macrophage development (PNAS 2011)](https://www.pnas.org/doi/10.1073/pnas.1019682108)
- [Alveolar macrophages of GM-CSF knockout mice exhibit mixed M1/M2 phenotypes (BMC Immunology 2013)](https://bmcimmunol.biomedcentral.com/articles/10.1186/1471-2172-14-41)
- [Nocardia Infections in 3 Patients with Anti-GM-CSF Autoantibodies (JACI 2024)](https://www.jacionline.org/article/S0091-6749(24)01381-2/fulltext)
- [Disseminated nocardiosis and anti-GM-CSF antibodies (Eur J Clin Microbiol Infect Dis 2024)](https://link.springer.com/article/10.1007/s10096-024-04785-z)
- [Pathogenic Role of Anti-GM-CSF Autoantibodies in Nocardiosis with CNS Involvement (J Clin Immunol 2024)](https://link.springer.com/article/10.1007/s10875-024-01775-w)
- [Neutralizing GM-CSF autoantibodies in PAP, cryptococcal meningitis and severe nocardiosis (PMC9552154)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9552154/)
- [Opportunistic Infection Associated With Elevated GM-CSF Autoantibodies (Open Forum Infect Dis 2022)](https://academic.oup.com/ofid/article/9/5/ofac146/6565987)
- [Pulmonary Alveolar Proteinosis Refractory to Plasmapheresis and Rituximab (PMC8818429)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8818429/)
- [A plasmapheresis protocol for refractory PAP (PubMed 25557091)](https://pubmed.ncbi.nlm.nih.gov/25557091/)
- [Pharmacotherapy for Autoimmune PAP (Drugs, 2025)](https://link.springer.com/article/10.1007/s40265-025-02228-3)
- [Phase 3 Trial of Inhaled Molgramostim in Autoimmune PAP (NEJM 2025)](https://www.nejm.org/doi/full/10.1056/NEJMoa2410542)
- [Molbreevi (molgramostim) approval history (Drugs.com)](https://www.drugs.com/history/molbreevi.html)
- [Phase 3 IMPALA-2 clinical trial coverage (CHEST Physician)](https://www.chestphysician.org/phase-3-impala-2-clinical-trial-shows-inhaled-molgramostim-promising-for-autoimmune-pulmonary-alveolar-proteinosis/)
- [Updated severity and prognosis score of PAP: multi-center cohort study in China (PMC9941621)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9941621/)
- [Pulmonary fibrosis in patients with autoimmune PAP: nationwide cohort study (ERS 2024)](https://publications.ersnet.org/content/erjor/10/6/00314-2024)
- [Hyaluronan in the pathogenesis of lung fibrosis in aPAP (PMC12440733)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12440733/)
- [Comorbidity of autoimmune diseases in patients with autoimmune PAP (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S2212534526000985)
- [Effects of COVID-19 infection in patients with autoimmune PAP (PMC10638736)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10638736/)
- [Autoimmune Pulmonary Alveolar Proteinosis: A Review of Pathogenesis and Emerging Therapies (Curr Pulmonol Rep 2024)](https://link.springer.com/article/10.1007/s13665-024-00356-x)
- [NORD: Autoimmune Pulmonary Alveolar Proteinosis](https://rarediseases.org/rare-diseases/autoimmune-pulmonary-alveolar-proteinosis/)
- [Cleveland Clinic: Pulmonary Alveolar Proteinosis](https://my.clevelandclinic.org/health/diseases/17398-pulmonary-alveolar-proteinosis)
- [StatPearls: Pulmonary Alveolar Proteinosis](https://www.ncbi.nlm.nih.gov/books/NBK482308/)