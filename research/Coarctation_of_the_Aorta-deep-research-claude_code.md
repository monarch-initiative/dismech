---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-10T14:06:56.307892'
end_time: '2026-08-10T14:12:19.651513'
duration_seconds: 323.34
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Coarctation of the Aorta
  mondo_id: ''
  category: Congenital
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
  web_search_requests: 20
  num_turns: 24
  total_cost_usd: 2.0469775000000006
  session_id: ccd9973f-d61b-50a6-8cfe-0a77b122d0f2
  stop_reason: end_turn
citation_count: 3
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Coarctation of the Aorta
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Coarctation of the Aorta** covering all of the
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

I now have sufficient material across all sections. Writing the comprehensive report now.

# Coarctation of the Aorta: Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Coarctation of the aorta (CoA) is a congenital cardiovascular malformation characterized by a discrete (or, less commonly, long-segment/tubular) narrowing of the aortic lumen, most typically located at the aortic isthmus — the short segment of the descending thoracic aorta between the origin of the left subclavian artery and the site of insertion of the ductus arteriosus. Orphanet describes it as "a rare, non-syndromic, congenital heart malformation characterized by a narrowing of the proximal thoracic aorta, most commonly occurring after the origin of the brachiocephalic vessels" (Orphanet ORPHA:1457). It can occur as an isolated ("simple") anomaly or in combination with other left heart obstructive lesions (bicuspid aortic valve, mitral valve anomalies, subaortic stenosis, ventricular septal defect) as part of a "Shone complex" spectrum, and it is one of the left ventricular outflow tract malformations (LVOTO) that overlap mechanistically and genetically with hypoplastic left heart syndrome (HLHS) and interrupted aortic arch (IAA).

**Key identifiers:**
- **OMIM:** 120000 (Coarctation of Aorta) — [OMIM 120000](https://www.omim.org/entry/120000)
- **Orphanet:** ORPHA:1457 — [Orphanet: Coarctation of aorta](https://www.orpha.net/en/disease/detail/1457)
- **MONDO:** MONDO:0007345
- **ICD-10-CM:** Q25.1 (Coarctation of aorta) — [ICD10Data Q25.1](https://www.icd10data.com/ICD10CM/Codes/Q00-QA0/Q20-Q28/Q25-/Q25.1)
- **ICD-11:** LA8B.21
- **MeSH:** D001017 (Aortic Coarctation)
- **HPO:** HP:0001680 (Coarctation of aorta)

**Synonyms/alternative names:** Aortic coarctation; CoA; juxtaductal coarctation; preductal/postductal coarctation (older anatomic classification); "adult-type"/"infantile-type" coarctation (older terminology, largely superseded by isthmic-position terminology); aortic isthmus stenosis.

**Data provenance:** Most published knowledge is derived from **aggregated disease-level resources** — clinical case series, single- and multi-center cohort studies, national/regional birth-defect registries (e.g., EUROCAT, Utah Birth Defect Network, National Birth Defects Prevention Study), and genetic-association cohorts (e.g., the Pediatric Cardiac Genomics Consortium, deCODE genetics in Iceland) — rather than large-scale individual-patient EHR mining, reflecting CoA's status as a well-characterized but comparatively rare structural anomaly.

---

## 2. Etiology

### Disease Causal Factors
CoA is fundamentally a disorder of **abnormal aortic arch morphogenesis during fetal development**, with a **multifactorial** etiology combining genetic susceptibility, altered fetal hemodynamics, and (rarely) monogenic/chromosomal causes. It is not caused by a single deterministic gene in the vast majority of cases; isolated non-syndromic CoA is best understood as a complex-trait cardiac malformation with substantial heritability (**estimated at 58%**) but incomplete penetrance and variable expressivity (search results, family-study literature; PMID:1018301, "A family study of coarctation of the aorta").

### Genetic Risk Factors

**Causal/high-confidence genes:**
- **NOTCH1** — the most consistently implicated gene in isolated (non-syndromic) CoA. NOTCH1 encodes a transmembrane receptor central to endocardial cushion epithelial-to-mesenchymal transition (EMT) and left ventricular outflow tract (LVOT) development. A targeted resequencing study found the **p.R1279H** variant "significantly overrepresented in patients with aortic coarctation" — identified in **14% of CoA cases vs. 2% of controls** — leading investigators to propose it as a disease-susceptibility allele (Freylikhman et al. 2014, *Congenital Heart Disease*, PMID:24418111). NOTCH1 mutations were separately shown to reduce ligand-induced Notch signaling in individuals with LVOT malformations (PMID:18593716).
- **MYH6** (myosin heavy chain 6, α-myosin heavy chain) — an Icelandic population-based GWAS/sequencing study (120 cases, >355,000 controls, using whole-genome sequencing imputed across the population) identified the rare missense variant **p.Arg721Trp (R721W)** with a striking effect size: **OR = 44.2, P = 5.0×10⁻²²**, present in up to **20% of Icelandic CoA cases vs. ~1% of controls** — "the first mutation associated with non-familial or sporadic CoA at a population level" (Gudbjartsson/Helgadottir et al. 2018, *European Heart Journal*, PMID:29590334). The variant lies in the converter domain of α-myosin heavy chain, critical for the ATP-hydrolysis-driven conformational change of the myosin lever arm, and separately associates with bicuspid aortic valve, sick sinus syndrome, and atrial fibrillation.
- **MCTP2** (multiple C2 and transmembrane domain-containing 2) — identified through 15q26.2 microdeletions in patients with CoA and hypoplastic left heart syndrome; a dosage-sensitive gene required for cardiac outflow tract development. Zebrafish/functional studies show Mctp2 morphants fail endocardial-to-mesenchymal transition in the outflow tract, phenocopying Notch1-deficient models (PMC3792692; QJM case report of a novel heterozygous MCTP2 mutation, academic.oup.com/qjmed).
- **SMAD6** — a negative regulator of BMP/TGF-β signaling (pathways essential for cardiac and aortic arch development); loss-of-function SMAD6 variants have been reported in probands with LVOT anomalies including CoA, bicuspid aortic valve, and hypoplastic transverse arch, sometimes with additional dysmorphic/developmental features when co-occurring with other variants (e.g., SMARCA4).
- **GATA5** — implicated alongside NOTCH1 and SMAD6 in bicuspid aortic valve and associated aortic arch abnormalities.
- **NKX2-5** — cardiac transcription factor found mutated in one or a few CoA individuals (typically in the context of broader congenital heart disease).
- Copy-number-variant-associated genes with CoA-like phenotypes on mouse knockout: **MATR3**, **FOXC1** (both found within CNV regions in CoA patients).
- **PRDM6** — recently reported in association with patent ductus arteriosus and coarctation of the aorta (PMID:38071433).

**Susceptibility loci / polygenic contribution:** Beyond single high-effect variants, CoA shows evidence of a broader oligogenic/polygenic architecture; a 2022 study ("Rare and Common Variants Uncover the Role of the Atria in Coarctation of the Aorta," *Genes* 2022, doi:10.3390/genes13040636) implicates additional common and rare variant burden, including an atrial-development component.

**Chromosomal/syndromic associations:**
- **Turner syndrome (45,X)** — one of the strongest genetic risk associations. Bicuspid aortic valve was found in **34%** of 45,X individuals and aortic coarctation in **12.5%** (PMID:23825392, "Bicuspid aortic valve and aortic coarctation are linked to deletion of the X chromosome short arm in Turner syndrome"). Haploinsufficiency for Xp genes is implicated in abnormal aortic valve/arch development.
- **22q11.2 deletion syndrome** — CoA occurs occasionally among the conotruncal/aortic-arch anomaly spectrum of this syndrome (alongside interrupted aortic arch type B, vascular rings, and aberrant subclavian origin), though it is far less characteristic than in Turner syndrome.
- **PHACE(S) syndrome** — more than **30%** of PHACES patients have coarctation of the aorta or other aortic anomalies (arch atresia, aberrant subclavian origin, descending thoracic aortic hypoplasia, double aortic arch).
- **Noonan syndrome, Williams syndrome (elastin arteriopathy)** — reported with distinctive, though generally less frequent, patterns of aortic arch/CoA involvement, consistent with each syndrome's characteristic cardiovascular phenotype spectrum.
- **Generalized arterial calcification of infancy (ABCC6/ENPP1 mutations)** — can mimic severe neonatal coarctation clinically (PMC9807665) — a Named-Entity-Confusion-relevant differential to note in curation.

### Environmental Risk Factors
Direct literature-confirmed environmental/maternal risk factors specific to CoA are less robustly characterized than for some other congenital heart defects, but general congenital-heart-defect teratogen/exposure literature (maternal pregestational diabetes, certain teratogenic medication exposures, maternal obesity, and other periconceptional exposures) is broadly implicated in left-sided obstructive lesions as a class; CoA is conventionally modeled as arising from the interaction of a genetic susceptibility background with **altered fetal intracardiac and aortic arch flow dynamics** (see Mechanism, below) rather than from a single discrete teratogen.

### Protective Factors
No well-established genetic or environmental protective factors specific to CoA are documented in the literature reviewed; this is an area flagged as a knowledge gap.

### Gene-Environment Interactions
The dominant mechanistic gene-by-hemodynamics interaction is the **"hemodynamic theory"**: any genetic or structural lesion that reduces fetal blood flow through the left ventricle, aortic valve, and transverse aortic arch/isthmus during development (e.g., a ventricular septal defect that shunts flow preferentially to the right heart and pulmonary circulation, reducing left-to-aortic flow) predisposes to arch underdevelopment and coarctation — i.e., low-flow states during a critical developmental window interact with baseline genetic susceptibility to produce the coarctation phenotype (PMC11846778, "The onset of coarctation of the aorta before birth: Mechanistic insights from fetal arch anatomy and haemodynamics").

---

## 3. Phenotypes

CoA's phenotypic presentation is strongly age- and severity-dependent, spanning neonatal cardiogenic shock to incidental adult hypertension.

### Cardinal signs (all ages)
| Phenotype | HPO term (suggested) | Notes |
|---|---|---|
| Coarctation of aorta (the lesion itself) | HP:0001680 | |
| Upper-extremity hypertension | HP:0004420 (Hypertension) | Systolic BP gradient >20 mmHg between upper and lower extremities is considered diagnostic |
| Diminished/absent/delayed femoral pulses | HP:0031650 (Decreased pulse pressure) / clinical sign, "brachial-femoral delay" | Pathognomonic physical exam finding |
| Systolic ejection murmur (interscapular/back) | HP:0030148 (Heart murmur) | |
| Differential cyanosis (lower body, if PDA-dependent with right-to-left shunt) | HP:0025487 | Neonatal, ductal-dependent presentations |

### Neonatal/infant presentation (severe/critical CoA)
- Heart failure, respiratory distress, poor feeding (HP:0001635, Congestive heart failure; HP:0011098; HP:0011968, feeding difficulties)
- Tachypnea, hepatomegaly (HP:0031692; HP:0002240)
- Poor perfusion: mottling, cool/pale lower extremities, weak/absent femoral pulses
- Cardiogenic shock and metabolic acidosis when the ductus arteriosus closes ("ductal-dependent" critical CoA), typically manifesting in the **first 1–2 weeks of life**

### Older children/adolescent/adult presentation (milder/undiagnosed CoA)
- Headache, epistaxis, dizziness (HP:0002315, HP:0000421)
- Lower-limb claudication/exercise intolerance, leg fatigue (HP:0003546, Claudication)
- Exertional dyspnea, fatigue
- Systemic (upper-body) hypertension, often incidentally discovered
- Cold extremities/leg cramps with exertion

### Radiographic/imaging signs
- **Rib notching** (posterior/inferior rib erosion from dilated, tortuous intercostal collateral arteries) — a classically taught pathognomonic chest radiograph finding, HP:0000895 (Abnormality of the ribs) or more specifically the descriptive term "rib notching."
- "**3-sign**"/"figure-3 sign" on chest X-ray from the indented coarctation segment with pre- and post-stenotic dilation.
- Extensive collateral circulation (internal mammary, intercostal, scapular arterial network) visible on CT/MR angiography.

### Associated structural cardiac anomalies (frequently co-occurring, not strictly "phenotypes" of CoA per se but part of the disease spectrum)
- **Bicuspid aortic valve** — present in **~50%** of CoA patients (and, conversely, ~10% of BAV patients have CoA) (HP:0001647, Bicuspid aortic valve)
- Ventricular septal defect
- Mitral valve anomalies (parachute mitral valve)
- Hypoplasia of the transverse aortic arch
- Subaortic stenosis (as part of Shone complex)

### Characteristics
- **Age of onset:** Bimodal — critical/severe CoA presents neonatally (ductal-dependent, first days to 2 weeks of life); milder discrete CoA can remain silent until childhood, adolescence, or adulthood, when it is discovered via hypertension workup or incidental exam.
- **Severity:** Highly variable — from a mild, hemodynamically insignificant narrowing to a critical, ductal-dependent obstruction causing neonatal shock.
- **Progression:** In unrepaired disease, the obstruction and its downstream consequences (hypertension, collateral formation, LV hypertrophy) are generally progressive over years to decades; sudden decompensation occurs in neonates coincident with ductal closure.
- **Frequency data:** BAV co-occurs in ~50% of CoA cases; intracranial aneurysm prevalence is significantly elevated versus the general population (see Outcome/Prognosis, below, for pooled estimates).

### Quality of Life Impact
Long-term QoL burden centers on: chronic antihypertensive medication dependence, exercise limitation/claudication symptoms, anxiety around recoarctation/aneurysm surveillance imaging, and, in a subset, neurocognitive or psychosocial burden associated with lifelong cardiology follow-up starting in infancy. Dedicated CoA-specific EQ-5D/SF-36 data are less commonly reported in the literature surveyed than general adult congenital heart disease (ACHD) quality-of-life studies; this is flagged as an area with a data gap.

---

## 4. Genetic/Molecular Information

### Causal Genes (summary table)
| Gene | HGNC/Gene ID | Role in CoA | Key variant | Evidence type |
|---|---|---|---|---|
| NOTCH1 | HGNC:7881 | LVOT/endocardial cushion EMT | p.R1279H | Human cohort, functional |
| MYH6 | HGNC:7576 | Cardiac sarcomere (α-MHC) | p.R721W (rs150793538) | Population GWAS/WGS |
| MCTP2 | HGNC:29669 | Outflow tract EMT (Ca²⁺-sensing membrane protein) | 15q26.2 microdeletion; point mutations | Human CNV + zebrafish morphant |
| SMAD6 | HGNC:6771 | BMP/TGF-β signaling negative regulator | Loss-of-function variants | Human cohort |
| GATA5 | HGNC:4174 | Cardiac transcription factor | Rare variants | Human cohort |
| NKX2-5 | HGNC:2488 | Cardiac transcription factor | Rare variants | Human cohort (few individuals) |
| PRDM6 | HGNC:14002 | Transcriptional regulator, vascular smooth muscle | Rare variants | Human case reports |
| MATR3, FOXC1 | — | CNV-region candidate genes | CNV | Mouse knockout phenocopy |

### Variant classification / functional consequences
- **NOTCH1 p.R1279H:** Missense; proposed disease-susceptibility allele; reduces ligand-induced Notch signaling.
- **MYH6 p.R721W:** Missense (Arg→Trp), located in the myosin converter domain; large effect size (OR 44.2) but incomplete penetrance, consistent with a **major-effect risk allele** rather than a fully penetrant Mendelian mutation; also confers risk for BAV and arrhythmia phenotypes (sick sinus syndrome, atrial fibrillation), indicating pleiotropy across cardiac structural and electrical phenotypes.
- **MCTP2:** Haploinsufficiency mechanism (dosage-sensitive gene); microdeletion (15q26.2, ~2.2 Mb in reported half-siblings) and point mutations both implicated — **loss-of-function**.
- **SMAD6:** Predicted loss-of-function (pLOF) variants reported; consistent with de-repression of BMP/TGF-β signaling.

### Allele frequency / population data
- MYH6 p.R721W: population frequency **0.34%** in the Icelandic reference population (gnomAD/deCODE data), markedly enriched in cases (up to 20%).
- NOTCH1 p.R1279H: present in ~2% of controls vs. 14% of CoA cases (still detectable at low frequency in the general population, consistent with reduced penetrance / susceptibility-allele model rather than fully penetrant disease-causing mutation).

### Somatic vs. germline origin
All reported CoA-associated variants are **germline**; there is no established somatic-mosaicism or acquired-mutation literature for CoA (as expected for a congenital structural malformation).

### Modifier genes
Formal modifier-gene literature specific to CoA severity is sparse; MYH6 p.R721W's pleiotropic association with arrhythmia phenotypes suggests it may act as a modifier of long-term cardiovascular risk beyond the structural lesion itself, but this is not yet formally established as a "modifier" in the strict sense.

### Epigenetic Information
No CoA-specific DNA methylation/histone-modification/chromatin studies were identified in the literature surveyed; this is a knowledge gap. (General congenital-heart-disease epigenomic studies exist but are not CoA-specific.)

### Chromosomal Abnormalities
- **45,X (Turner syndrome)** — most significant recurring chromosomal association (see Etiology).
- **22q11.2 deletion** — occasional CoA co-occurrence within its broader conotruncal/aortic arch anomaly spectrum.
- **15q26.2 terminal deletion** (encompassing MCTP2) — reported in CoA/HLHS.

### Suggested ontology terms
- **HGNC:** NOTCH1 (HGNC:7881), MYH6 (HGNC:7576), MCTP2 (HGNC:29669), SMAD6 (HGNC:6771), GATA5 (HGNC:4174), NKX2-5 (HGNC:2488)
- **GO (biological process):** GO:0007507 (heart development), GO:0003151 (outflow tract morphogenesis), GO:0003172 (determination of heart left/right asymmetry — for arch laterality anomalies), GO:0001570 (vasculogenesis), GO:0007219 (Notch signaling pathway), GO:0030509 (BMP signaling pathway)
- **GO (molecular function):** GO:0005112 (Notch binding)

---

## 5. Environmental Information

- **Environmental factors:** No specific toxin, radiation, or occupational-exposure literature dedicated to CoA was identified; CoA is grouped within the broader congenital-heart-defect teratogen literature.
- **Lifestyle factors:** Maternal factors generally implicated in congenital heart defects as a class (pregestational diabetes, obesity) are relevant risk-modulators; CoA-specific quantification (odds ratios) was not identified in this search pass and should be sourced from national birth-defect registry studies (e.g., National Birth Defects Prevention Study) in a follow-up literature pass if precise ORs are required for curation.
- **Infectious agents:** Not applicable — CoA is not an infectious disease. (Note: infective endocarditis is a downstream *complication* of CoA, not a cause — see Outcome/Prognosis.)

This section is flagged as an area with comparatively thin direct literature relative to the genetic etiology; downstream curation should treat environmental risk factors as a secondary/contributory layer atop the dominant genetic-hemodynamic model.

---

## 6. Mechanism / Pathophysiology

### Causal chain overview
CoA pathophysiology operates on two nested timescales: **(1) developmental** — how the coarctation forms in utero/perinatally, and **(2) hemodynamic/systemic** — how the fixed anatomic narrowing produces its downstream physiological and vascular consequences across the lifespan.

### 6a. Developmental mechanism: two complementary/competing theories

**1. Ductal tissue theory.** The dominant unifying mechanism: the ductus arteriosus is largely composed of **oxygen-sensitive smooth muscle** arranged longitudinally/spirally, histologically distinct from the aorta's circumferentially arranged elastic fibers. Ectopic ductal smooth-muscle tissue can extend into (or migrate into) the periductal aortic wall at the isthmus. After birth, rising arterial oxygen tension triggers **constriction of this ductal-type smooth muscle** — the same physiological signal that normally closes the ductus arteriosus — and because this tissue is embedded circumferentially or eccentrically within the juxtaductal aortic wall, its contraction produces a discrete luminal narrowing of the aorta itself, not just ductal closure ("Pathology and molecular mechanisms of coarctation of the aorta and its association with the ductus arteriosus," *J Physiol Sci*, link.springer.com/article/10.1007/s12576-016-0512-x). This explains why some neonates with critical coarctation and a **closed** ductus arteriosus still respond to prostaglandin E1 (PGE1) infusion by **relaxing ectopic ductal tissue surrounding the isthmus**, relieving obstruction independent of reopening the ductus arteriosus itself (Springer, *Pediatric Cardiology* 2003, "Effectiveness of Prostaglandin E1 in Relieving Obstruction in Coarctation of the Aorta Without Opening the Ductus Arteriosus").

**2. Hemodynamic (flow) theory.** Coarctation results from **reduced fetal blood flow volume** through the aortic arch and isthmus during development. Any lesion diverting left ventricular output away from the ascending aorta/arch (e.g., a large ventricular septal defect preferentially shunting flow to the pulmonary circuit, or intrinsically reduced left heart forward flow) reduces the trophic flow stimulus needed for normal isthmic growth, producing arch underdevelopment/hypoplasia and coarctation. This is supported by embryologic/biomechanical modeling work (PMC11846778, "The onset of coarctation of the aorta before birth: Mechanistic insights from fetal arch anatomy and haemodynamics") and explains the strong empirical association between CoA and lesions that reduce left-sided flow (VSD, mitral stenosis, hypoplastic left heart spectrum).

These two theories are not mutually exclusive — abnormal ductal tissue and reduced fetal arch flow likely interact, with genetic lesions (NOTCH1, MYH6, MCTP2, SMAD6) predisposing to both defective outflow-tract EMT/morphogenesis and to the downstream flow abnormalities that exacerbate isthmic underdevelopment.

### 6b. Embryologic basis
The aortic arch system derives from the pharyngeal (branchial) arch arteries. The **left 4th aortic arch** forms the thoracic aortic arch/isthmus; the **left 6th aortic arch** forms the ductus arteriosus. Coarctation is attributed to abnormal embryologic development/remodeling of the left 4th and 6th arches at their isthmic junction — mechanistically related to, but distinct from, the pharyngeal-arch neural-crest-patterning defects captured elsewhere in cardiac malformation biology (this dismech instance's `pharyngeal_arch_patterning_serial_homology` module models the craniofacial/neural-crest arm; CoA's arch-artery-remodeling defect is a related but separate vascular morphogenesis process, chiefly involving cardiac neural crest and second heart field contributions to the outflow tract/aortic arch rather than the facial skeletal neural crest program).

### 6c. Cellular/molecular processes at the lesion
- **Endocardial-to-mesenchymal transition (EMT) failure** in the outflow tract/endocardial cushions — the shared mechanistic node linking NOTCH1 and MCTP2: Notch1-deficient mouse embryos "fail to form endocardial cushions" with "absence of mesenchymal cells migrating from the endocardium," phenotypically mirrored in Mctp2 morphants, which show "intact myocardial and endocardial layers of the outflow tract in the presence of cardiac jelly," indicating failed EMT (PMC3792692).
- **Vascular smooth muscle cell (VSMC) phenotypic modulation:** Within the coarctation segment itself, "smooth muscle cells in the intima of CoA stenotic segments dedifferentiate at an early stage and redifferentiate in older populations." The lesion is characterized by **intimal thickening, impaired elastic fiber formation, and phenotypic modulation** of VSMCs.
- **Systemic arteriopathy beyond the discrete lesion:** Resected pre-stenotic aortic tissue shows **reduced contractility, increased collagen deposition, and reduced smooth muscle content** — indicating CoA is "a systemic vascular disease rather than a simple mechanical obstruction that can be resolved through surgical intervention alone." This underlies the persistence of hypertension and proatherogenic vascular changes even after anatomically successful repair.

### 6d. Post-lesion hemodynamic cascade (the causal chain from anatomic lesion to clinical manifestation)
1. **Fixed luminal obstruction** at the aortic isthmus →
2. **Increased afterload on the left ventricle** proximal to the coarctation, and **reduced perfusion pressure** distal to it →
3. **Compensatory collateral arterial network formation** — blood is rerouted anterogradely through the subclavian/internal mammary/intercostal arterial system with **retrograde flow through the intercostal arteries** back into the descending aorta distal to the coarctation, producing the radiographically visible **rib notching** sign (from chronic pulsatile pressure erosion of the inferior rib cortex) →
4. **Left ventricular hypertrophy/remodeling** from chronic pressure overload →
5. **Persistent systemic (upper-body) hypertension**, mediated in part by **altered aortic arch baroreceptor function**: baroreceptors situated in the abnormally rigid/dilated pre-stenotic aortic segment are activated less at a given pressure than baroreceptors in a normally distensible vessel, resetting the baroreflex to tolerate — and defend — a higher systemic pressure ("Hypertension and coarctation of the aorta: an inevitable consequence of developmental pathophysiology," *Hypertension Research*, nature.com/articles/hr201122) →
6. **Downstream end-organ consequences:** premature atherosclerosis/coronary artery disease, intracranial (berry) aneurysm formation and rupture, aortic aneurysm/dissection at or near the repair site, left ventricular dysfunction/heart failure, and increased infective endocarditis risk from turbulent flow across the lesion or associated bicuspid valve.

Critically, this arteriopathy/baroreflex-resetting mechanism explains the clinically important observation that **hypertension frequently persists after anatomically successful surgical or catheter-based repair**, since the systemic vascular and baroreceptor abnormalities are not confined to the resected/dilated segment alone — "CoA is a lifelong disease strongly associated with long-term hypertension, regardless of age at diagnosis or quality of repair" (*Hypertension*, AHA Journals, "Coarctation of the Aorta: Modern Paradigms Across the Lifespan," doi:10.1161/HYPERTENSIONAHA.123.19454).

### Suggested GO / CL / UBERON terms for pathophysiology modeling
- **GO:BP:** GO:0007507 (heart development), GO:0003151 (outflow tract morphogenesis), GO:0001525 (angiogenesis, for collateral formation), GO:0001974 (blood vessel remodeling), GO:0035904 (aorta development), GO:0003416 (endochondral bone growth — n/a), GO:0006940 (regulation of smooth muscle contraction)
- **GO:CC:** GO:0005886 (plasma membrane, for VSMC phenotypic markers)
- **CL:** CL:0000359 (vascular associated smooth muscle cell), CL:0002350 (endocardial cell), CL:0000057 (fibroblast, for collagen deposition), CL:0000669 (pericyte, if collateral vessel remodeling context needed)
- **UBERON:** UBERON:0001496 (aortic arch), UBERON:0001508 (descending aorta), UBERON:0009834 (aortic isthmus — check exact term availability), UBERON:0002049 (ductus arteriosus / vasculature of the heart region), UBERON:0002100 (trunk vasculature)

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary:** Aorta (specifically the aortic isthmus/proximal descending thoracic aorta), left ventricle (pressure-overload hypertrophy secondary to obstruction).
- **Secondary/complication-related organs:** Brain (intracranial/berry aneurysm, hemorrhagic stroke risk), coronary arteries (premature atherosclerosis), kidneys (renin-angiotensin activation contributing to hypertension), heart valve (bicuspid aortic valve, frequently co-occurring), lower extremities (hypoperfusion, claudication).
- **Body systems involved:** Cardiovascular system primarily; secondary CNS and renal involvement via hypertension-mediated end-organ effects.

### Tissue and cell level
- Aortic tunica media/intima at the coarctation segment: smooth muscle phenotypic modulation, intimal thickening, disrupted elastic lamellae.
- Pre-stenotic aortic wall: increased collagen, reduced smooth muscle content, reduced contractility (systemic arteriopathy).
- Collateral vessel network: internal mammary arteries, intercostal arteries, scapular anastomotic network — chronically dilated/tortuous.

### Subcellular level
Not deeply characterized in CoA-specific literature at the organelle level; the dominant subcellular process is **VSMC phenotypic switching** (contractile → synthetic phenotype), a broadly recognized vascular biology process (GO:0035886, vascular associated smooth muscle cell differentiation).

### Localization
- **Anatomical site:** Aortic isthmus (junction of aortic arch and descending thoracic aorta), typically juxtaductal (adjacent to the ductus arteriosus insertion) — UBERON term for aortic isthmus should be verified via OAK lookup during curation.
- **Laterality:** Not applicable in the traditional bilateral-organ sense, but note the "differential cyanosis" pattern (lower body vs. upper body) in ductal-dependent neonatal presentations reflects the coarctation's position relative to the ductus arteriosus and brachiocephalic vessel origins.

---

## 8. Temporal Development

### Onset
- **Congenital** — the anatomic lesion is present at birth (or forms perinatally via ductal-tissue constriction as described above), though clinical **detection** may be delayed.
- **Onset pattern:** Can be **acute** (neonatal ductal-dependent presentation, days 1–14 of life, precipitated by ductus arteriosus closure) or **insidious/chronic** (asymptomatic until incidental hypertension detection in childhood, adolescence, or adulthood).

### Progression
- **Neonatal critical CoA:** Rapid, life-threatening progression to cardiogenic shock/multiorgan hypoperfusion within days of ductal closure if unrecognized — a true pediatric cardiac emergency.
- **Milder/undiagnosed CoA:** Slowly progressive over years to decades — progressive collateral formation, progressive LV hypertrophy, progressive systemic hypertension, and (without early diagnosis) potential progression to intracranial hemorrhage, aortic dissection, or premature coronary disease by the third–fourth decade of life if untreated.
- **Post-repair:** Recoarctation can develop at the repair site over months to years; aortic aneurysm formation at the repair site is a recognized late complication requiring lifelong surveillance.

### Patterns
- **Disease course:** Predominantly a fixed anatomic lesion with **superimposed progressive systemic vascular sequelae** (arteriopathy, hypertension) rather than a relapsing-remitting pattern.
- **Critical period:** The **perinatal window around ductal closure** (typically the first 1–2 weeks of life) is the single most important critical period — this is when ductal-dependent critical coarctation manifests and when prostaglandin E1 rescue is time-sensitive and life-saving.
- **No spontaneous remission** — the anatomic narrowing does not resolve without surgical or catheter-based intervention.

---

## 9. Inheritance and Population

### Epidemiology
- **Birth prevalence:** approximately **1/2,500** live births (isolated CoA); alternative estimates cite **3–4 per 10,000 live births**, or **~29–49 per 100,000** live births — broadly consistent figures across sources.
- **Proportion of congenital heart defects:** CoA accounts for **4–6%** of all congenital heart defects, making it one of the more common structural cardiac anomalies.

### Inheritance pattern
- CoA is generally considered **multifactorial/complex** rather than following simple Mendelian inheritance in the large majority of non-syndromic cases, though it clusters in families more strongly than most other congenital heart lesions.
- **Heritability estimate: 58%** (family-based studies).
- **Sibling recurrence risk:** Historical teaching cited ~1 in 200 (0.5%), but more recent, better-powered estimates report a sibling recurrence risk of **4.0% (95% CI: 2.1–6.7%)** — notably elevated (reportedly >30-fold) relative to the general-population baseline risk for any congenital heart defect (~1%). If more than one sibling is already affected, recurrence risk can rise to **~10%**. (PMID:1018301, "A family study of coarctation of the aorta"; supplementary recurrence-risk literature.)
- **Penetrance:** Reduced/incomplete for the identified susceptibility alleles (NOTCH1 p.R1279H present at low frequency even in unaffected controls; MYH6 p.R721W similarly not fully penetrant), consistent with a complex-trait, multi-hit model rather than classic Mendelian dominant/recessive inheritance for isolated CoA. (Syndromic CoA, e.g., in the context of a defined 15q26.2 deletion or Turner syndrome, follows the inheritance/penetrance pattern of the underlying chromosomal condition.)
- **Genetic anticipation:** Not reported/applicable.
- **Founder effects:** The Icelandic MYH6 p.R721W finding — enriched to ~20% of local CoA cases — is consistent with a population-specific (founder-influenced) allele frequency effect, illustrating how population genetic background modulates observed genetic architecture.
- **Consanguinity:** Not specifically highlighted as a major driver in the literature surveyed (befitting the multifactorial rather than autosomal-recessive model).

### Population demographics
- **Sex ratio:** Consistent **male predominance**, reported across sources at roughly **1.3:1 to 1.7:1** male:female (some individual series report up to 59%:41% or higher); this is one of relatively few congenital heart defects with a clear male excess.
- **Geographic/ethnic distribution:** No strong evidence of major geographic clustering beyond population-specific allele frequency effects (e.g., the Icelandic MYH6 founder variant); Turner syndrome-associated CoA prevalence is a function of Turner syndrome's own population frequency (~1/2,000–2,500 live female births) rather than an independent geographic pattern.
- **Age distribution:** Bimodal clinical detection — neonatal/infant presentation for severe/critical lesions, and childhood-through-adult presentation (often via incidental hypertension screening) for milder lesions.

---

## 10. Diagnostics

### Clinical/physical examination
- **Four-limb blood pressure measurement** is a cornerstone diagnostic maneuver — a **systolic BP gradient >20 mmHg** between upper and lower extremities is considered suggestive of significant coarctation; guideline-based pediatric hypertension evaluation includes four-limb BP assessment.
- **Brachial-femoral pulse delay/differential** — "pathognomonic" on exam alongside the BP gradient.
- Auscultation: systolic murmur, often best heard over the back/interscapular region.

### Imaging
- **Transthoracic echocardiography (TTE):** the **preferred first-line diagnostic modality** for both initial diagnosis and follow-up; most CoA cases are diagnosed by echo.
- **Cardiac MRI / CT angiography:** second-line advanced imaging providing detailed anatomic delineation of the arch, isthmus, and collateral vessels; particularly valuable for surgical/interventional planning and long-term adult surveillance (repair-site aneurysm, recoarctation).
- **Chest radiograph:** classic but non-sensitive supportive findings — **rib notching** (from chronic intercostal collateral erosion of the inferior rib margins) and the **"figure-3 sign"** from the indented coarctation segment with pre-/post-stenotic dilation; "regression of rib notching following surgery" has been documented radiographically, useful as an indirect marker of successful repair.

### Fetal/prenatal diagnosis
- **Fetal echocardiography** allows prenatal detection but remains **challenging** — the intracardiac structures are typically normal in isolated CoA, and the aortic arch/isthmus itself is technically difficult to visualize directly in utero.
- Diagnosis is most often **inferred indirectly** from **right-left ventricular and great-vessel size disproportion** (right-sided predominance) — but this sign alone has limited specificity: in one study, **only ~30%** of fetuses flagged for suspected coarctation based on ventricular disproportion were confirmed postnatally (i.e., a substantial false-positive rate with ventricular disproportion as sole criterion).
- Multi-parameter prediction models improve accuracy: **aortic valve z-score (best cutoff −1.25)** and **distal transverse aortic arch z-score (best cutoff −0.37)** were identified as the best individual predictors of postnatal CoA confirmation; combining multiple third-trimester echocardiographic parameters improves prediction over any single criterion.

### Genetic testing
- No single-gene test is diagnostic for the majority of isolated CoA cases, given its multifactorial/complex architecture; genetic testing is generally targeted at:
  - **Chromosomal microarray/karyotype** — particularly indicated to evaluate for **Turner syndrome (45,X)** in females and for **22q11.2 deletion** when other syndromic features or additional conotruncal anomalies are present.
  - **Gene panel testing** for LVOT-malformation-associated genes (NOTCH1, MYH6, SMAD6, GATA5, NKX2-5) may be considered in familial or syndromic presentations, though clinical-grade panels and their yield are still evolving given the incomplete-penetrance, complex-trait nature of most isolated cases.
- **Whole exome/genome sequencing** has been the primary discovery tool for the individual gene associations above (research rather than routine first-line clinical context in most isolated cases currently).

### Clinical criteria / differential diagnosis
Differential diagnosis for the BP-gradient/hypertension presentation includes: essential/primary hypertension, other causes of secondary pediatric hypertension (renal artery stenosis, pheochromocytoma), interrupted aortic arch (more severe, complete discontinuity rather than narrowing), and — importantly for evidence-quality curation — **generalized arterial calcification of infancy (GACI, ABCC6/ENPP1)**, which can mimic severe neonatal coarctation on imaging (PMC9807665) — a differential worth flagging in curation to avoid conflating the two entities.

### Screening
No population-wide dedicated newborn screening test exists for CoA specifically; **pulse oximetry-based critical congenital heart disease (CCHD) newborn screening**, implemented broadly in the US and many other health systems, is the principal population-level early-detection tool, since severe CoA can produce detectable pre-/post-ductal oxygen saturation differentials before overt clinical decompensation.

---

## 11. Outcome/Prognosis

### Survival and mortality
- Untreated **critical/severe neonatal CoA** is a life-threatening ductal-dependent lesion with high mortality if unrecognized and PGE1/surgical intervention is delayed.
- With modern surgical/catheter-based repair, **survival into adulthood is the norm** for isolated CoA, but **adults with repaired CoA carry increased long-term cardiovascular mortality** compared to the general population, driven chiefly by hypertension-related sequelae (premature coronary disease, stroke, aortic complications) rather than the repaired lesion itself.
- Untreated milder CoA historically carried a substantially reduced life expectancy by the third–fourth decade due to complications (hypertension, LV failure, dissection, intracranial hemorrhage), which is the historical rationale for early surgical correction once the lesion was recognized.

### Morbidity / disease course complications
- **Persistent/recurrent hypertension** post-repair: reported in roughly **30–50%** of adults even after technically successful repair — the single most important chronic morbidity, reflecting the systemic arteriopathy/baroreflex-resetting mechanism described above rather than simple failure of the mechanical repair.
- **Recoarctation:** recurrent narrowing at or near the repair site, requiring repeat catheter or surgical intervention in a meaningful subset of patients; risk factors for recurrence have been specifically studied in pediatric surgical cohorts (e.g., "Risk factors for recurrence after surgical repair of coarctation of the aorta in children: a single-center experience based on 51 children," PMC10267975).
- **Aortic aneurysm/pseudoaneurysm** at the repair site — a recognized late complication, more frequent after certain repair techniques (notably historic Dacron patch aortoplasty) and after bare-metal stent placement (fatal complications including aortic rupture reported with bare stents, motivating the shift toward covered stents).
- **Premature coronary artery disease** — increased risk of angina, MI, and sudden cardiac death.
- **Intracranial (berry) aneurysm:** significantly elevated prevalence compared with the general population, with **earlier age at rupture** than typical sporadic intracranial aneurysms; a systematic review/meta-analysis specifically quantified this elevated prevalence (JACC: Advances, "Prevalence of Intracranial Aneurysms in Patients With Coarctation of the Aorta: A Systematic Review and Meta-Analysis," doi:10.1016/j.jacadv.2023.100394).
- **Infective endocarditis** risk, related to turbulent flow across the coarctation and/or an associated bicuspid aortic valve.
- **Aortic dissection/rupture**, particularly in longstanding untreated hypertensive disease.
- **Left ventricular hypertrophy and dysfunction/heart failure** from chronic pressure overload, particularly if diagnosis/repair is delayed.

### Recovery potential / prognostic factors
- Earlier diagnosis and repair are associated with better long-term blood pressure control and reduced cardiovascular morbidity; delayed diagnosis (into later childhood/adulthood) is associated with a higher burden of established hypertension and arteriopathy that may not fully normalize even after mechanically successful repair.
- Presence of associated lesions (bicuspid aortic valve, arch hypoplasia, VSD) and the extent of pre-existing systemic arteriopathy at the time of repair are relevant prognostic modifiers, though CoA-specific quantitative prognostic scoring systems were not identified in this search pass.

---

## 12. Treatment

### Overarching goal
Eliminate (or substantially reduce) the aortic pressure gradient and relieve/prevent systemic hypertension, ideally with early intervention following diagnosis.

### Pharmacotherapy
- **Prostaglandin E1 (alprostadil)** — the critical first-line neonatal stabilization agent for ductal-dependent/critical CoA. Maintains (or, notably, can act even after) ductal patency and, importantly, **directly relaxes ectopic ductal smooth-muscle tissue within the coarctation segment itself**, relieving obstruction even without reopening a closed ductus arteriosus (a mechanistically distinct, dual-action benefit specific to CoA among ductal-dependent lesions). A Cochrane review addresses PGE1 use for maintaining ductal patency broadly across ductal-dependent cardiac lesions (Akkinapally et al. 2018, Cochrane Library, doi:10.1002/14651858.CD011417.pub2).
  - **NCIT suggestion:** NCIT:C15986 (Pharmacotherapy) as `treatment_term`, with `therapeutic_agent` bound to alprostadil (CHEBI or NCIT term — verify via OAK).
- **Antihypertensive medications** for pre- and post-repair blood pressure management (ACE inhibitors/ARBs, beta-blockers commonly used in adult ACHD hypertension management, per general hypertension pharmacotherapy classes) — NCIT:C15986 Pharmacotherapy with an appropriate `therapeutic_agent` per specific drug class.

### Surgical and interventional
- **Surgical repair** remains the treatment of choice, particularly for neonates/young infants and for complex/long-segment coarctation not amenable to catheter approaches. Techniques include resection with end-to-end (or extended end-to-end) anastomosis, subclavian flap aortoplasty, and patch aortoplasty (historically associated with higher late aneurysm risk). NCIT suggestion: NCIT:C15329 (Surgical Procedure) or a more specific cardiothoracic/vascular surgical procedure term.
- **Balloon angioplasty** — catheter-based dilation of the coarctation segment; now the **preferred therapy for recurrent (post-surgical) coarctation** when anatomy is favorable.
- **Stent implantation (bare-metal or covered):** increasingly used, especially in older children/adults with native or recurrent coarctation. **Covered balloon-expandable stents** have emerged specifically to mitigate the aortic rupture/pseudoaneurysm risk associated with bare stents (Frontiers in Cardiovascular Medicine, "Endovascular treatment of aortic coarctation using covered balloon-expandable stents—a systematic review and meta-analysis," 2024, doi:10.3389/fcvm.2024.1439458).
- **Hybrid approaches** — combined surgical/catheter strategies for complex arch anatomy (e.g., "Two stage hybrid approach for complex aortic coarctation repair," PMC2652448).
- NCIT suggestion for catheter-based intervention: a specific NCIT interventional cardiology/angioplasty term (verify via OAK; general fallback NCIT:C49236 Therapeutic Procedure).

### Supportive care
Neonatal stabilization (inotropic support, correction of metabolic acidosis, mechanical ventilation as needed) pending definitive PGE1 stabilization and surgical/catheter repair in critical presentations.

### Treatment outcomes / adverse events
- Bare-metal stents: associated with **fatal complications including aortic rupture, pseudoaneurysm formation, and post-implantation aneurysm** — a key driver of the shift toward covered stents.
- Catheter interventions overall: "good [outcomes] in skilled hands, but residual or recurrent coarctation with resultant hypertension and repair site aneurysms can occur."

### Treatment strategy / algorithms
- **Neonatal critical CoA:** PGE1 stabilization → surgical repair (most common in this age group) or catheter intervention depending on center expertise/anatomy.
- **Recurrent/recoarctation:** catheter-based balloon angioplasty ± stent is now generally preferred over reoperation when anatomy permits.
- **Adult native or recurrent CoA:** individualized surgical vs. covered-stent decision-making based on anatomy, arch hypoplasia, and aneurysm risk.

### Experimental / clinical trials
Specific active CoA-focused NCT-registered interventional trials were not individually enumerated in this pass; a dedicated ClinicalTrials.gov search (e.g., for covered stent devices, novel antihypertensive regimens in ACHD, or long-term arteriopathy-targeted therapy) would be the appropriate follow-up step for curation requiring specific NCT identifiers.

---

## 13. Prevention

### Primary prevention
No established primary prevention strategy exists for CoA itself, given its developmental/multifactorial etiology; general prenatal care optimization (glycemic control in pregestational diabetes, avoidance of known teratogens) is the applicable general congenital-heart-defect prevention framework rather than a CoA-specific intervention.

### Secondary prevention (early detection)
- **Pulse oximetry-based critical congenital heart disease newborn screening** — the principal population-level early-detection tool, since it can flag pre-/post-ductal saturation differentials in severe CoA before overt decompensation.
- **Four-limb blood pressure screening** in the context of routine pediatric hypertension evaluation serves as an important later-childhood/adolescent detection mechanism for milder, previously undiagnosed CoA.
- **Fetal echocardiography** in pregnancies with risk factors (e.g., known familial CoA, other detected cardiac anomalies with left-right ventricular disproportion, Turner syndrome diagnosis) enables prenatal detection and delivery planning at a center capable of neonatal cardiac care, though — as noted — sensitivity/specificity limitations remain (see Diagnostics).

### Tertiary prevention (preventing complications in diagnosed/repaired patients)
- Lifelong cardiology follow-up with periodic imaging (echo, CT, or MRI) for recoarctation and aneurysm surveillance.
- Aggressive blood pressure control post-repair to mitigate the premature coronary disease, intracranial aneurysm, and aortic complication risks driven by persistent hypertension.
- Endocarditis-precaution counseling where indicated by associated valve pathology, per standard infective endocarditis prophylaxis guidelines.

### Genetic counseling
Given the elevated sibling recurrence risk (~4%, and up to ~10% with more than one affected sibling) relative to the general congenital-heart-defect baseline, **genetic counseling for families with an index CoA case** is warranted, incorporating both the empirical recurrence-risk data and consideration of targeted testing (karyotype/microarray for Turner/22q11.2, gene panel where clinically indicated) depending on the presence of syndromic features.

### Public health / screening programs
CoA detection is embedded within broader national/regional **newborn CCHD pulse-oximetry screening programs** rather than having a dedicated standalone public health screening program.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Naturally occurring CoA has been documented in **dogs** (*Canis lupus familiaris*, NCBITaxon:9615) and, per the veterinary literature, is described as occurring (rarely) in **cats** as well; it has also been used as an induced/surgical model in **rabbits** and **pigs**.
- **Natural disease in companion animals:** MSD/Merck Veterinary Manual describes CoA in animals as "a rare condition of dogs and cats" involving narrowing of the aorta distal to the subclavian artery, typically at/near the ductus arteriosus site, producing concentric left ventricular hypertrophy from pressure overload — directly analogous to the human mechanism. Documented breed case reports include a **Great Dane** with a large fusiform post-stenotic aneurysm and a **Vizsla** with juxtaductal coarctation identified at postmortem following sudden collapse/cardiopulmonary arrest during a stressful event (ScienceDirect, "Sudden death in a dog with aortic coarctation").
- **Clinical presentation in animals:** Forelimb blood pressure readings are characteristically higher than hindlimb readings, directly mirroring the human upper-vs-lower-extremity gradient sign.
- **Veterinary relevance:** Naturally occurring CoA remains rare in veterinary practice — "although AoCo is a well-recognized congenital defect in humans, it has been reported only rarely in animals" — with the available literature dominated by individual case reports rather than large breed-prevalence cohort studies; no confirmed OMIA (Online Mendelian Inheritance in Animals) breed-heritability entry was identified in this search pass.
- **Comparative pathology:** The fundamental structural mechanism (juxtaductal narrowing, pressure-overload LV hypertrophy) is conserved across species, supporting the translational relevance of large-animal (porcine, ovine) surgical/hemodynamic coarctation models to human disease biology.

---

## 15. Model Organisms

### Genetic/induced models
- **Mouse:**
  - *Notch1* haploinsufficient mice develop **ascending aortic aneurysms**, and Notch1-deficient mouse embryos fail endocardial cushion formation with absent endocardial-to-mesenchymal transition — directly modeling the EMT-failure mechanism proposed for human LVOT malformations including CoA (PMID:29093270, "Notch1 haploinsufficiency causes ascending aortic aneurysms in mice").
  - Myeloid-specific *Notch1* knockout mice have been used to study aneurysm progression via TLR/oxidative-stress/SHP2 signaling pathways, offering a complementary post-natal vascular-inflammation angle on Notch1-related aortic pathology (PMC10866402).
- **Zebrafish:**
  - **Mctp2 morphants** recapitulate failed outflow-tract EMT with intact myocardial/endocardial layers persisting in the presence of cardiac jelly — closely phenocopying the Notch1-deficient mouse defect and directly supporting MCTP2's causal role in human CoA/HLHS (PMC3792692, "MCTP2 is a dosage-sensitive gene required for cardiac outflow tract development").
- **Induced large-animal models:**
  - **Porcine (growing pig) model** of surgically created/treated aortic coarctation, used for structural and mechanical wall analysis of treated vs. untreated coarctation over growth (bioRxiv, "Structural and Mechanical Analysis of Treated and Untreated Aortic Coarctation in a Growing Porcine Model," 2025).
  - **Rabbit computational/surgical model** examining ventricular and ascending aortic remodeling in response to induced coarctation (bioRxiv, "A Computational Model of Coarctation of the Aorta in Rabbits: Ventricular and Ascending Aortic Remodeling," 2023).
  - These large-animal surgical models are chiefly used to study the **downstream hemodynamic/remodeling consequences** of a fixed aortic narrowing (LV hypertrophy, ascending aortic wall remodeling, collateral development) rather than the developmental genetic etiology, complementing the developmental-genetics focus of the mouse/zebrafish models above.

### Model characteristics and limitations
- The **mouse/zebrafish genetic models** (Notch1, Mctp2) recapitulate the developmental/EMT-failure mechanism believed to underlie human outflow-tract and arch malformations but do not, on their own, produce a discrete adult-onset coarctation lesion identical to the human anatomic phenotype — they primarily model the upstream cellular defect (failed EMT, endocardial cushion formation) rather than the mature juxtaductal narrowing itself.
- The **large-animal surgically-induced models** (porcine, rabbit) directly reproduce the mature anatomic lesion and its hemodynamic consequences but do not model the underlying developmental/genetic etiology — they are mechanical/hemodynamic models rather than etiologic models. This is a clear example of a **model-fidelity split** worth flagging for `HUMAN_MODEL_MISMATCH`-type discussion during curation: genetic models capture "why" the lesion forms; surgical large-animal models capture "what happens" once it exists — no single model captures both arms.
- **Applications:** Genetic models are used to dissect the molecular/cellular basis of arch/outflow-tract malformation; surgically-induced large-animal models are used to study post-repair vascular remodeling, wall mechanics, and to test/optimize interventional devices (stents, angioplasty balloons) before human use.

---

## Summary of Key Suggested Ontology Terms for KB Curation

| Category | Term(s) |
|---|---|
| Disease | MONDO:0007345; OMIM:120000; Orphanet:1457; ICD-10:Q25.1; HP:0001680 |
| Phenotypes | HP:0004420 (Hypertension), HP:0001647 (Bicuspid aortic valve), HP:0001635 (CHF), HP:0003546 (Claudication), HP:0000895 (rib abnormality/notching) |
| Genes | HGNC:7881 (NOTCH1), HGNC:7576 (MYH6), HGNC:29669 (MCTP2), HGNC:6771 (SMAD6), HGNC:4174 (GATA5), HGNC:2488 (NKX2-5) |
| GO:BP | GO:0007507, GO:0003151, GO:0007219, GO:0030509, GO:0001974 |
| CL | CL:0000359 (vascular smooth muscle cell), CL:0002350 (endocardial cell) |
| UBERON | UBERON:0001496 (aortic arch), UBERON:0001508 (descending aorta), ductus arteriosus term (verify) |
| NCIT (treatment) | NCIT:C15986 (Pharmacotherapy — PGE1, antihypertensives), NCIT:C15329 (Surgical Procedure), catheter/angioplasty term (verify) |
| Associated syndromes | Turner syndrome (MONDO term), 22q11.2 deletion syndrome (MONDO term), PHACE syndrome |

---

## Key Citations (PMID/DOI where available)

1. Freylikhman et al. 2014. Variants in the NOTCH1 gene in patients with aortic coarctation. *Congenit Heart Dis.* PMID:24418111
2. Garg et al. NOTCH1 mutations in individuals with left ventricular outflow tract malformations reduce ligand-induced signaling. PMID:18593716
3. Gudbjartsson/Helgadottir et al. 2018. A rare missense mutation in MYH6 associates with non-syndromic coarctation of the aorta. *Eur Heart J* 39(34):3243. PMID:29590334
4. "Rare and Common Variants Uncover the Role of the Atria in Coarctation of the Aorta." *Genes* 2022, 13(4):636. doi:10.3390/genes13040636 (PMC9032275)
5. "MCTP2 is a dosage-sensitive gene required for cardiac outflow tract development." PMC3792692
6. Novel heterozygous mutation of MCTP2 gene in a patient with coarctation of the aorta. *QJM*. academic.oup.com/qjmed
7. Sharma et al. Bicuspid aortic valve and aortic coarctation are linked to deletion of the X chromosome short arm in Turner syndrome. PMID:23825392
8. "A family study of coarctation of the aorta." PMID:1018301 / PMC1013466
9. Freud et al. Notch1 haploinsufficiency causes ascending aortic aneurysms in mice. PMID:29093270
10. "Pathology and molecular mechanisms of coarctation of the aorta and its association with the ductus arteriosus." *J Physiol Sci*. link.springer.com/article/10.1007/s12576-016-0512-x
11. "Hypertension and coarctation of the aorta: an inevitable consequence of developmental pathophysiology." *Hypertens Res*. nature.com/articles/hr201122
12. "Coarctation of the Aorta: Modern Paradigms Across the Lifespan." *Hypertension* (AHA), doi:10.1161/HYPERTENSIONAHA.123.19454
13. "The onset of coarctation of the aorta before birth: Mechanistic insights from fetal arch anatomy and haemodynamics." PMC11846778
14. "Effectiveness of Prostaglandin E1 in Relieving Obstruction in Coarctation of the Aorta Without Opening the Ductus Arteriosus." *Pediatr Cardiol* 2003. link.springer.com
15. Akkinapally et al. 2018. Prostaglandin E1 for maintaining ductal patency in neonates with ductal-dependent cardiac lesions. *Cochrane Database Syst Rev.* doi:10.1002/14651858.CD011417.pub2
16. "Endovascular treatment of aortic coarctation using covered balloon-expandable stents—a systematic review and meta-analysis." *Front Cardiovasc Med* 2024. doi:10.3389/fcvm.2024.1439458
17. "Prevalence of Intracranial Aneurysms in Patients With Coarctation of the Aorta: A Systematic Review and Meta-Analysis." *JACC Adv* 2023. doi:10.1016/j.jacadv.2023.100394
18. "Risk factors for recurrence after surgical repair of coarctation of the aorta in children." PMC10267975
19. Coarctation of the Aorta - StatPearls. NCBI Bookshelf NBK430913
20. Coarctation of the Aorta in Animals. MSD Veterinary Manual.
21. PRDM6 variants: Patent ductus arteriosus and coarctation of the aorta in association with PRDM6 variants. PMID:38071433
22. SMAD6 pLOF variants in LVOT anomalies (multiple sources, ScienceDirect P218 abstract; PMC7549564)
23. "Isolated Coarctation of the Aorta: Current Concepts and Perspectives." PMC9174545
24. Orphanet: Coarctation of aorta. orpha.net/en/disease/detail/1457
25. OMIM 120000 — Coarctation of Aorta. omim.org/entry/120000

**Note on evidence gaps for curation:** Direct quantified environmental/lifestyle risk-factor data specific to CoA (as opposed to congenital heart defects generally), CoA-specific quality-of-life instrument data, epigenomic/methylation studies, and an authoritative OMIA veterinary heritability entry were not identified in this search pass and should be treated as open items for a follow-up literature sweep before being asserted as curated claims with citations.