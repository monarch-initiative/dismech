---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-03T04:14:30.830547'
end_time: '2026-07-03T04:18:35.642944'
duration_seconds: 244.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Rubella
  mondo_id: ''
  category: Infectious Disease
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
  web_search_requests: 21
  num_turns: 23
  total_cost_usd: 1.7951063000000003
  session_id: 520ca325-e58e-5587-b817-abe96e2a26c5
  stop_reason: end_turn
citation_count: 51
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rubella
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Rubella** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

I now have sufficient depth across all sections to compile the comprehensive report.

# Rubella and Congenital Rubella Syndrome: Comprehensive Research Report

## 1. Disease Information

**Overview:** Rubella (German measles, "three-day measles") is a mild, self-limited exanthematous viral illness in children and adults, caused by rubella virus (RuV), the sole member of genus *Rubivirus*, family *Togaviridae* (previously classified with alphaviruses, now its own genus, sometimes placed with the newly described *Matonaviridae* family). Its major public-health importance is not the mild postnatal illness but its severe **teratogenic potential**: maternal infection during pregnancy, especially the first trimester, can produce **Congenital Rubella Syndrome (CRS)**, a multisystem birth-defect syndrome combining sensorineural deafness, cataract/ocular defects, and congenital heart disease, plus a range of other findings ([StatPearls, Congenital Rubella](https://www.ncbi.nlm.nih.gov/books/NBK507879/); [MSD Manual](https://www.msdmanuals.com/professional/pediatrics/infections-in-neonates/congenital-rubella)).

**Key identifiers:**
- **OMIM:** 267000 (Congenital Rubella Syndrome)
- **Orphanet:** ORPHA:290 (Congenital rubella syndrome) ([Orphanet](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=290&Lng=GB))
- **MONDO:** Mondo integrates OMIM/Orphanet/ICD-11/NCIt mappings for disease identity resolution ([Mondo Disease Ontology](https://mondo.monarchinitiative.org/))
- **ICD-11:** 1F02 (Rubella), congenital form under LA91/childhood-onset codes; **ICD-10:** B06 (Rubella [German measles]), P35.0 (Congenital rubella syndrome)
- **MeSH:** D012409 (Rubella), D012410 (Rubella Syndrome, Congenital)
- **GARD (NIH):** Congenital rubella syndrome entry (GARD 4744) ([GARD](https://rarediseases.info.nih.gov/diseases/4744/congenital-rubella-syndrome))

**Synonyms:** German measles, three-day measles (postnatal rubella); Gregg syndrome, congenital rubella infection, CRS (congenital form).

**Data source type:** Information here is derived from aggregated disease-level resources (surveillance case series, systematic reviews, cohort/registry studies) rather than individual EHR record review, supplemented by virology/molecular mechanistic studies (cell culture, organoid models).

---

## 2. Etiology

**Disease causal factor:** Rubella is caused by infection with rubella virus, a positive-sense single-stranded RNA virus. It is the **sole cause** of both postnatal rubella and CRS — an infectious, not genetic, etiology; CRS is a teratogenic consequence of vertical (transplacental) transmission during a susceptible gestational window.

**Genome/virology:** RuV has a ~9,762-nucleotide, positive-sense ssRNA genome with two ORFs — a 5′ ORF encoding nonstructural proteins (p150/p90, replicase complex) and a 3′ ORF (translated from a subgenomic RNA) encoding three structural proteins: capsid (C, ~31 kDa), and envelope glycoproteins E2 (42–47 kDa) and E1 (58 kDa) ([PMC3574052](https://pmc.ncbi.nlm.nih.gov/articles/PMC3574052/); [NCBI Bookshelf NBK8200](https://www.ncbi.nlm.nih.gov/books/NBK8200/)). Only one serotype exists worldwide, though genotypes (2 clades, ~13 genotypes) are used for molecular epidemiologic surveillance.

**Risk factors:**
- *Environmental/host:* Lack of immunity (unvaccinated or seronegative status) is the dominant risk factor for both acquiring rubella and for transmitting to a fetus. Timing of maternal infection relative to gestational age is the single largest determinant of CRS risk and severity (see Temporal Development, below).
- *Genetic (host susceptibility to infection/vaccine response, not causal variants):* Twin/heritability studies show ~50% of variance in rubella-vaccine antibody response is genetically determined; the HLA system alone explains ~20% of this variance. Specific alleles (HLA-B*27:05, HLA-DPA1*02:01, HLA-DPB1*04:01, and HLA-DQA1/DQB1 loci) are associated with variation in antibody titer and IL-2 cytokine responses to vaccination ([PMC4096048](https://pmc.ncbi.nlm.nih.gov/articles/PMC4096048/); [J Infect Dis 211:898](https://academic.oup.com/jid/article/211/6/898/2910563); [PMC2957833](https://pmc.ncbi.nlm.nih.gov/articles/PMC2957833/)). HLA homozygosity restricts epitope-presentation diversity and is associated with poorer immune response ([PMC2815167](https://ncbi.nlm.nih.gov/pmc/articles/PMC2815167)).
- Genetic susceptibility to *diabetes as a late CRS manifestation* is HLA-linked: CRS patients with the HLA A1-B8 haplotype (more common in Caucasians) show higher rates of insulin-dependent diabetes mellitus by adulthood (~20% by age 35).

**Protective factors:** Prior natural infection or vaccination confers durable (often lifelong) immunity via neutralizing antibody to E1/E2. No genetic protective variants against infection per se are well described (rubella has one serotype and near-universal human susceptibility absent immunity).

**Gene-environment interaction:** The principal G×E axis is host-genetic (HLA/cytokine gene) modulation of vaccine-induced immune response combined with environmental exposure (vaccination timing/coverage) — determining population-level herd immunity and residual susceptible cohorts (e.g., unvaccinated pregnant women) who remain at risk for CRS.

---

## 3. Phenotypes

### Postnatal (acquired) rubella
- **Symptoms/signs:** Low-grade fever, malaise, headache, mild conjunctivitis, coryza — prodrome mild or absent in children.
- **Lymphadenopathy:** Classic and early — postauricular, occipital, posterior cervical nodes (HP:0002716, Lymphadenopathy), may precede rash.
- **Rash:** Erythematous, maculopapular (HP:0001030), cephalocaudal spread, generalizes <24h, resolves in ~3 days without desquamation typically.
- **Arthralgia/arthritis (HP:0001369/HP:0001367):** Especially in adult women — up to 70% develop arthritis/arthralgia (fingers, wrists, knees, ankles), typically resolving within 2 weeks, occasionally chronic ([HKMJ 25:134](https://www.hkmj.org/abstracts/v25n2/134.htm)).
- Onset: Acute; course: self-limited (days); severity: mild in most, but significant in a subset of adults (arthritis).

### Congenital Rubella Syndrome (CRS)
**Classic triad (highest specificity):**
- **Sensorineural hearing loss** (HP:0000407) — most common single manifestation, up to ~60-90% of symptomatic CRS.
- **Congenital heart defects** (HP:0001627) — present in >50% of symptomatic infants; branch pulmonary artery stenosis (HP:0004415) in 78% of those with cardiac findings, patent ductus arteriosus (HP:0001643) in 62%, both together in 49% ([PMID 19697432](https://pubmed.ncbi.nlm.nih.gov/19697432/); [PMC10474486](https://pmc.ncbi.nlm.nih.gov/articles/PMC10474486/)).
- **Ocular defects** (~43% of patients overall): cataract (HP:0000518, 93.1% of those with ocular involvement), microphthalmia (HP:0000568, 85.1%), iris abnormalities (58.6%), pigmentary retinopathy "salt and pepper" (HP:0007737, 37.9%), congenital glaucoma (HP:0000520, 6%), nystagmus (50%), strabismus (26%), optic atrophy (4.6%).

**Neonatal manifestations:** low birth weight/IUGR (HP:0001518, >50% of clinically apparent cases), hepatosplenomegaly (HP:0001433), thrombocytopenia/purpura (HP:0001873), "blueberry muffin" dermal erythropoiesis rash (HP:0031391-type finding; ~5% of CRS cases), jaundice/hepatitis (HP:0000952), meningoencephalitis (HP:0001260), metaphyseal "celery-stalk" long-bone radiolucencies (HP:0004425-type), microcephaly (HP:0000252), generalized lymphadenopathy, cryptorchidism, inguinal hernia, dermatoglyphic abnormalities ([Congenital Rubella overview - ScienceDirect](https://www.sciencedirect.com/topics/neuroscience/congenital-rubella-syndrome); [PMC4316306](https://pmc.ncbi.nlm.nih.gov/articles/PMC4316306/)).

**Delayed/extended manifestations (occurring months–decades later):**
- Endocrinopathies: insulin-dependent diabetes mellitus (~20% by age 35, HLA A1-B8 linked), thyroid disease, growth hormone deficiency.
- Progressive rubella panencephalitis (HP:0002500-type, rare, fatal): onset 4–14 years after infection, insidious dementia, seizures, ataxia, cognitive decline ([PMID 4001724](https://pubmed.ncbi.nlm.nih.gov/4001724/); [ScienceDirect](https://www.sciencedirect.com/topics/neuroscience/progressive-rubella-panencephalitis)).
- Autism spectrum disorder: historical cohort found ~12.5% of CRS survivors developed autism (8/64 in a 1960s Texas cohort) — one of the earliest recognized "infectious" causes of autism ([PMID 5172438](https://pubmed.ncbi.nlm.nih.gov/5172438/); [PMC6801530](https://pmc.ncbi.nlm.nih.gov/articles/PMC6801530/)).
- Vascular effects and progressive hearing/ocular deterioration.

**Quality of life impact:** Deafness, blindness/severe visual impairment, cardiac disease, intellectual disability, and autism collectively produce substantial lifelong disability; CRS is a major historical driver of pediatric deafblindness programs pre-vaccine era.

---

## 4. Genetic/Molecular Information

CRS is **not a genetic (Mendelian) disease** — it is an acquired teratogenic viral syndrome. There are no causal human genes; rather, the "genetics" of relevance are:
- **Viral genome:** capsid, E1, E2 (structural); p150/p90 nonstructural replicase proteins (5′ ORF) — see Etiology section.
- **Host receptor:** Myelin oligodendrocyte glycoprotein (**MOG**, HGNC gene) was identified as a cellular receptor binding RuV E1 glycoprotein; anti-MOG antibody blocks infection, and ectopic MOG expression renders non-permissive cells (293T) permissive ([PMC3194935](https://pmc.ncbi.nlm.nih.gov/articles/PMC3194935/); J Virol 10.1128/jvi.05398-11). However, MOG is not the sole receptor — MOG-independent infection occurs in keratinocytes (HaCaT cells lacking MOG), and first-trimester trophoblast cells are relatively **resistant** to RuV in vitro, an important observation relevant to placental barrier biology ([PMC5795436](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5795436/)).
- **Host susceptibility variants:** HLA-B*27:05, HLA-DPA1*02:01, HLA-DPB1*04:01, HLA-DQA1/DQB1 polymorphisms affect vaccine antibody/cytokine response magnitude (see Etiology). SNPs in viral-receptor/attachment-factor genes are also associated with variation in humoral immunity post-vaccination ([PMC4063777](https://pmc.ncbi.nlm.nih.gov/articles/PMC4063777/)).
- **Epigenetics/chromosomal abnormalities:** Not a feature of CRS pathogenesis (distinguishing it from genetic congenital syndromes); rather cell-intrinsic viral effects (below) drive pathology.

---

## 5. Environmental Information

- **Infectious agent:** Rubella virus (genus *Rubivirus*), transmitted via respiratory droplets (postnatal) and transplacentally (congenital route).
- **Environmental/lifestyle factors:** The dominant environmental determinant is vaccination coverage/herd immunity gaps; no toxin, occupational, or dietary risk factor is implicated. Maternal age, prior immune status, and geographic/community rubella circulation determine exposure risk.
- **Reservoir:** Humans are the only known natural reservoir/host — no zoonotic animal reservoir for classical rubella virus (though recently discovered related "rustrela virus" and "rubella-like" viruses exist in rodents/bats, suggesting an ancient zoonotic origin for the *Matonaviridae*, but these are not the same pathogen) ([Nature Microbiology Community](https://naturemicrobiologycommunity.nature.com/posts/bats-mice-zoos-and-noses-the-zoonotic-origins-of-rubella-virus)).

---

## 6. Mechanism / Pathophysiology

**Causal chain — postnatal infection:** Respiratory droplet exposure → viral replication in nasopharyngeal/respiratory epithelium and regional lymph nodes → viremia (5-7 days before rash) → dissemination to skin (rash), joints (immune-complex-mediated arthritis in adults), and (if pregnant) transplacental spread to fetus.

**Causal chain — congenital infection/CRS (the core teratogenic mechanism):**
1. **Maternal viremia → placental infection.** RuV crosses the placenta hematogenously.
2. **Vascular/placental damage.** RuV induces necrotic damage to endothelial cells of placental and myocardial capillaries/larger vessels, with occasional occlusion of arterial intima of medium/large vessels — "angiopathy" compromising fetal blood supply ([Congenital Rubella, StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK507879/)).
3. **Non-cytolytic persistent infection of fetal cells.** Unlike many cytolytic infections, wild-type RuV establishes **persistent, non-cytopathic infection** of human fetal endothelial cells (HUVEC) — it productively infects without gross cytopathology, without inhibiting host protein synthesis grossly, but subtly impairing cell function ([PMC3734309](https://ncbi.nlm.nih.gov/pmc/articles/PMC3734309); PLOS ONE 10.1371/journal.pone.0073014).
4. **Angiogenesis inhibition.** RuV infection of endothelial cells induces type I/III interferon (IFN-β) and CXCL10, which reduces angiogenic and migratory capacity of endothelial cells; blocking IFN-β receptor or CXCL10 reverses this anti-angiogenic effect — providing a direct molecular link between viral infection and the vascular hypoplasia underlying organ defects ([PMC10060672](https://pmc.ncbi.nlm.nih.gov/articles/PMC10060672/); Gene expression profiling [PMC4736114](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4736114/)).
5. **Direct cellular injury: apoptosis, mitotic inhibition, cytoskeletal disruption.** RuV infection of fetal cells induces apoptosis and disrupts cell-cycle progression/mitosis, causing organ hypoplasia. Mechanistically, the **capsid protein binds host mitochondrial matrix protein p32**, causing capsid-mediated mitochondrial redistribution, blocking mitochondrial protein import, and thereby **inhibiting apoptosis** in some contexts while promoting persistent infection ([J Virol 10.1128/jvi.01348-09](https://journals.asm.org/doi/10.1128/jvi.01348-09); [PMC112044](https://pmc.ncbi.nlm.nih.gov/articles/PMC112044/); [PMID 16051872](https://pubmed.ncbi.nlm.nih.gov/16051872/)). Intracellular actin assembly is also inhibited by RuV, restricting cytoskeletal-dependent mitosis and precursor-cell proliferation.
6. **Neural progenitor/CNS involvement.** RuV infects neuronal progenitor cells and, in human brain organoid/microglia-containing models, triggers a profound interferon response predominantly in neurons/neural progenitor cells, while in primary human brain tissue RuV predominantly infects **microglia** — the resident CNS immune cell — implicating neuroinflammatory and interferon-driven mechanisms in the microcephaly/neurodevelopmental phenotype (including autism) ([eLife 10.7554/eLife.87696](https://elifesciences.org/articles/87696); PMID 37327049/37470786). Microcephaly and neurodevelopmental delay arise from neuronal apoptosis and disrupted cortical migration secondary to progenitor infection.
7. **Cumulative organ hypoplasia/malformation.** The combination of (a) direct cytopathic/apoptotic injury to actively dividing organ precursor cells during critical organogenesis windows, (b) vascular/angiogenic insufficiency, and (c) chromosomal/mitotic disruption in infected cells yields the multi-organ hypoplasia pattern (small eye [microphthalmia], small brain [microcephaly], hypoplastic pulmonary arteries, cochlear/organ of Corti damage causing deafness, lens opacification/cataract).
8. **Postnatal persistence and late manifestations.** Virus can persist in immunologically privileged sites (lens, inner ear, CNS) for years, shedding for up to a year postnatally; slow ongoing viral replication in CNS underlies progressive rubella panencephalitis; pancreatic islet cell involvement (direct infection and/or autoimmune HLA-linked mechanism) underlies late-onset diabetes.

**Key GO/CL/UBERON suggestions:**
- GO:0006915 (apoptotic process), GO:0001525 (angiogenesis) — inhibited, GO:0034341 (response to type I interferon), GO:0060337 (type I interferon signaling pathway), GO:0007049 (cell cycle), GO:0000281 (mitotic cytokinesis)
- CL:0000115 (endothelial cell), CL:0000540 (neuron), CL:0002319 (neural progenitor cell), CL:0000129 (microglial cell), CL:0000653 (podocyte-type not relevant), CL:0000216 (Sertoli — not relevant); relevant: CL:0000584 (enterocyte not relevant) — focus on CL:0000115, CL:0002319, CL:0000129, CL:0000210 (photoreceptor, for retinopathy), CL:0000596 (organ of Corti hair cell-type for deafness — sensorineural_hair_cell_loss module relevant), CL:0000359 (vasculature-associated smooth muscle — for PDA/PA stenosis).
- UBERON:0000955 (brain), UBERON:0000966 (retina), UBERON:0001690 (ear), UBERON:0000948 (heart), UBERON:0001987 (placenta), UBERON:0002037 (cerebellum).

**Note for dismech curation:** This mechanism maps naturally to a "viral teratogenesis" pattern — direct viral cytopathic/apoptotic injury to proliferating organ-precursor cells + IFN-mediated angiogenesis inhibition + persistent non-cytolytic infection — analogous in structure to `viral_oncogenesis` but for teratogenic (not oncogenic) viral mechanism; could be a candidate future mechanism module (no existing dismech module currently captures "viral congenital infection teratogenesis").

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Eye (lens, retina, cornea), ear (cochlea/organ of Corti), heart (great vessels, septa), brain (cortex, cerebellum) — the classic triad organs. Secondary: liver (hepatitis), spleen, bone marrow (thrombocytopenia, dermal erythropoiesis), pancreas (islet cells, late diabetes), thyroid, long bones (metaphyses), gonads (cryptorchidism), skin.
- **Body systems:** Cardiovascular, nervous, sensory (auditory, visual), endocrine, hematologic, hepatic, skeletal, integumentary.
- **Tissue/cell level:** Vascular endothelium (placental and fetal capillaries/arteries), neural progenitor cells and microglia (CNS), lens epithelium, cochlear hair cells and spiral ganglion, cardiac myocardium/endothelium (pulmonary artery branches, ductus arteriosus smooth muscle), hepatocytes, megakaryocytes/platelets, dermal erythropoietic foci (blueberry muffin lesions), pancreatic islet β-cells.
- **Subcellular:** Mitochondria (capsid-p32 interaction, GO:0005739), actin cytoskeleton (GO:0015629), replication complexes on modified endosomal/lysosomal membranes (GO:0005768-related structures) for the nonstructural replicase.
- **Localization/laterality:** Typically bilateral for sensory organs (bilateral cataracts, bilateral sensorineural hearing loss common); cardiac defects are structural (branch pulmonary artery stenosis often bilateral branch involvement).

---

## 8. Temporal Development

- **Onset (postnatal):** Incubation 14 days (range 12–23); prodrome 1-5 days; acute self-limited illness.
- **Onset (congenital):** Timing of maternal infection relative to gestational age is the principal determinant:
  - Infection 0–11 weeks post-conception (first trimester): up to **90%** fetal infection/defect risk (some sources cite 85-100% depending on precise window).
  - Infection weeks 12–16: ~35-50% risk, defects still substantial (deafness alone can occur).
  - Infection weeks 13–16: ~50% risk of congenital defect.
  - Late second half of second trimester: ~25% risk.
  - After 20 weeks gestation: defects rare; but risk of infection (not necessarily defect) rises again in the third trimester, with transmission approaching ~100% near term (isolated deafness can still occur late).
  - Vertical transmission rates: up to 90% in first 12 weeks, dip in mid-pregnancy, rising again to near 100% by term (a U-shaped transmission curve, but a steadily declining defect-risk curve) ([MDPI 2077-0383/14/11/3986](https://www.mdpi.com/2077-0383/14/11/3986)).
- **Progression:** CRS is not "staged" like cancer; instead it is categorized into **neonatal**, **extended** (persisting/appearing through infancy), and **delayed** manifestations (endocrinopathies, panencephalitis — years to decades later).
- **Disease course pattern:** Postnatal rubella — acute, self-limited. CRS — static structural defects (cataract, heart defect, deafness) generally non-progressive once established, but a distinct subset of manifestations (hearing loss, diabetes, panencephalitis) are progressive/delayed-onset, appearing after an apparently normal interval.
- **Critical period:** Organogenesis window (first trimester) is the critical vulnerability period — coincides with lens, cochlear, and cardiac outflow tract development.

---

## 9. Inheritance and Population

- **Inheritance pattern:** None — acquired infectious disease, not Mendelian. (Susceptibility to complications like diabetes is polygenic/HLA-associated, not classically inherited.)
- **Epidemiology (global):**
  - Pre-vaccine era: rubella was endemic worldwide with epidemic cycles every 6–9 years.
  - Estimated global CRS burden: ~119,000 cases in 1996, ~105,000–110,000 in 2010, declining to an estimated **~32,000 cases annually by 2019** (95% CI 13,000–60,000) as vaccination coverage expanded ([PMC10689248](https://pmc.ncbi.nlm.nih.gov/articles/PMC10689248/); [PMC4786291](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4786291/)).
  - By 2010, CRS incidence fell to <2 per 100,000 live births in the Americas/Europe (regions with mature RCV programs) versus 90-121 per 100,000 live births persisting in parts of Africa and Southeast Asia lacking vaccination programs.
  - As of 2023, the WHO Western Pacific Region verified 7 countries/areas (Korea, Australia, Hong Kong SAR, Singapore, New Zealand, Macao SAR, Brunei) as having eliminated rubella; the Americas region achieved elimination in 2015 (first WHO region to do so, and the US sustains elimination as of 2022–2024) ([PMC12974482](https://pmc.ncbi.nlm.nih.gov/articles/PMC12974482/)). The WHO European Region reported 345 cases across 17 countries in 2023, concentrated in Poland, Kyrgyzstan, Tajikistan, Türkiye, Ukraine — reflecting immunity gaps. China reported 583,418 cumulative rubella cases 2004–2021 (average annual incidence 2.40/100,000) ([PMC12174117](https://pmc.ncbi.nlm.nih.gov/articles/PMC12174117/)).
- **Sex ratio:** Postnatal rubella affects males and females roughly equally, but arthritis complications are markedly more common in adult women (up to 70%). CRS itself shows no strong sex predilection in offspring.
- **Age distribution:** Historically a childhood disease pre-vaccine; in the vaccine era, outbreaks increasingly occur in unvaccinated young adults (including women of childbearing age), which is the population of greatest concern for CRS.
- **Geographic/population variance:** Endemic transmission persists where vaccination coverage is incomplete (parts of Africa, South/Southeast Asia at time of these reports); genetic modifiers of complication risk (e.g., HLA A1-B8 for diabetes) vary by ancestry (higher in Caucasian populations).
- **Consanguinity/founder effects/mosaicism:** Not applicable — infectious, not genetic, disease.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **RT-PCR (molecular):** Confirms acute infection; rubella RNA detectable from ~2 days before to 4 days after rash onset in respiratory specimens (also urine, oral fluid, and for congenital cases: urine, throat swab, CSF). All RT-PCR-positive specimens undergo sequencing at CDC/APHL reference centers for genotyping/surveillance ([CDC Chapter 14](https://www.cdc.gov/surv-manual/php/table-of-contents/chapter-14-rubella.html)).
- **Serology:**
  - IgM capture EIA (preferred over indirect IgM EIA for specificity) — indicates recent infection; false positives increase as background incidence falls, so results should be interpreted alongside RT-PCR and epidemiologic linkage.
  - IgG avidity testing — low avidity suggests recent infection; high avidity suggests past immunity; particularly useful for early pregnancy risk assessment ([CDC Serology Testing](https://www.cdc.gov/rubella/php/laboratories/serology-testing.html)).
- **Congenital diagnosis:** IgM in neonatal serum (does not cross placenta, so positive = congenital infection); persistently elevated/rising IgG beyond maternal antibody decline; viral RNA detection via RT-PCR from nasopharyngeal/urine/CSF specimens; virus can be shed for up to a year in congenitally infected infants.
- **Imaging:** Echocardiography for structural cardiac defects (branch PA stenosis, PDA) — echocardiography noted as key confirmatory tool in CRS case series ([PMC5440835](https://pmc.ncbi.nlm.nih.gov/articles/PMC5440835/)); long-bone radiographs show metaphyseal lucencies ("celery stalking"); cranial ultrasound/CT/MRI for microcephaly, calcifications, ventriculomegaly.
- **Ophthalmologic exam:** Slit-lamp for cataract, fundoscopy for "salt and pepper" retinopathy.
- **Audiology:** Brainstem auditory evoked response (BAER)/otoacoustic emissions for sensorineural hearing loss.
- **Genetic testing:** Not applicable (no causal germline variant); however, genetic/genomic tools ARE used for viral genotyping (whole-genome sequencing of RuV strains for molecular epidemiology, e.g., [PMC3574052](https://pmc.ncbi.nlm.nih.gov/articles/PMC3574052/)) — distinct from human genetic testing.
- **Standardized clinical criteria:** CDC/WHO surveillance case definitions classify CRS into "clinically confirmed," "laboratory confirmed," and "congenital rubella infection" (CRI, asymptomatic but lab-confirmed) categories, requiring ≥2 major findings (cataract/congenital glaucoma, congenital heart disease, hearing loss, pigmentary retinopathy) or 1 major + 1 minor finding, per [CDC Chapter 15](https://www.cdc.gov/surv-manual/php/table-of-contents/chapter-15-congenital-rubella-syndrome.html).
- **Screening:** Prenatal rubella IgG screening (universal in most antenatal care) to identify susceptible pregnant women; postpartum vaccination of susceptible women; no newborn screening panel specific to CRS (diagnosis is clinical/serologic in symptomatic or exposed neonates).

---

## 11. Outcome/Prognosis

- **Postnatal rubella:** Excellent prognosis; self-limited, rarely fatal; rare complications include encephalitis (~1/6000 cases) and hemorrhagic manifestations (thrombocytopenic purpura, ~1/3000).
- **CRS survival/mortality:** Historically significant infant mortality in severely affected (multi-organ) cases, particularly with cardiac and CNS involvement, hepatosplenomegaly with DIC, or severe thrombocytopenia; surviving infants often face lifelong multi-system disability.
- **Morbidity:** Deafness (often the sole finding in later-gestation infections) is the single most common and often most functionally significant permanent morbidity; combined sensory (deaf-blind) impairment carries major QoL burden; cardiac defects may require surgical correction; intellectual disability and autism spectrum disorder add substantial lifelong care needs.
- **Progressive rubella panencephalitis:** Rare but **uniformly fatal** over a course of months to a few years once symptomatic, occurring 4–14 years after infection.
- **Prognostic factors:** Gestational age at maternal infection (earlier = worse), number/severity of organ systems involved at birth, access to surgical/rehabilitative/audiologic intervention.
- **Recovery potential:** Structural defects (cataract, heart defect) do not spontaneously resolve but are surgically correctable; hearing loss is generally permanent though partially manageable with hearing aids/cochlear implants; developmental effects are lifelong but partially mitigated by early intervention.

---

## 12. Treatment

**Pharmacotherapy:** No specific antiviral therapy exists for rubella or CRS; treatment is entirely supportive ([droracle.ai summary](https://www.droracle.ai/articles/648851/what-is-the-treatment-for-rubella); [Medscape Pediatric Rubella Treatment](https://emedicine.medscape.com/article/968523-treatment)).
- Postnatal: symptomatic care — antipyretics/analgesics (e.g., acetaminophen), NSAIDs for arthralgia/arthritis, rest.
- No approved gene therapy, cell therapy, RNA-based therapy, targeted therapy, or immunotherapy exists for rubella infection itself (these modalities are not applicable to this acute viral illness).

**Surgical/interventional (for CRS sequelae):**
- Cataract extraction surgery (MAXO surgical procedure term; NCIT:C15329 Surgical Procedure) — often complicated by microphthalmia/glaucoma making surgical timing/technique challenging.
- Cardiac surgical repair for significant structural defects (PDA ligation/closure, pulmonary artery stenosis intervention) (NCIT:C16186 relevant, or a cardiac-specific surgical term).
- Cochlear implantation / hearing aid fitting for sensorineural hearing loss (MAXO surgical/device term; NCIT device categories).
- Glaucoma surgical/medical management.

**Supportive/rehabilitative:**
- NICU supportive care for complicated neonates (respiratory support, phototherapy/exchange transfusion for severe jaundice/hyperbilirubinemia, management of DIC/thrombocytopenia).
- Early intervention/developmental therapy programs (physical, occupational, speech-language therapy) — MAXO:0000011 (physical therapy) relevant.
- Endocrine management: insulin therapy for CRS-associated diabetes mellitus; thyroid hormone replacement for CRS-associated hypothyroidism; growth hormone therapy where deficient.
- Genetic counseling is generally not applicable (non-genetic disease), though reproductive/prenatal counseling regarding rubella immunity status is standard obstetric practice.

**Experimental:** No current active antiviral drug development pipeline of note for rubella specifically (the disease is targeted almost exclusively through vaccination-based prevention rather than treatment).

**Treatment strategy:** Management is fundamentally multidisciplinary and organ-system-specific (ophthalmology, cardiology, audiology, endocrinology, neurology, developmental pediatrics) rather than a unified antiviral algorithm.

---

## 13. Prevention

**This is the dominant "treatment" modality for rubella/CRS — prevention rather than cure.**

- **Primary prevention — vaccination:** Live-attenuated RA27/3 strain, developed by Stanley Plotkin and Leonard Hayflick (1965–1969) via serial low-temperature passage in human diploid fibroblast strain WI-38 ([PMID 3890107](https://pubmed.ncbi.nlm.nih.gov/3890107/); [Embryo Project](https://embryo.asu.edu/pages/stanley-alan-plotkins-development-rubella-vaccine-1969)). Molecular basis of attenuation involves mutations in the 5′ UTR, nonstructural protease region, and capsid gene. Combined MMR vaccine introduced 1972; MMRV (adding varicella) subsequently available.
  - **Efficacy:** ≥95% seroconversion after one dose; durable protection (>90% protected at 15 years); protects against viremia, not just symptomatic disease; induces mucosal plus systemic immunity ([ScienceDirect Rubella Vaccine overview](https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/rubella-vaccine)).
  - MAXO term: MAXO:0001017 (vaccination).
- **Secondary prevention:** Prenatal IgG serologic screening to identify susceptible pregnant women (not itself preventive, but enables risk counseling and postpartum vaccination); no treatment exists to prevent CRS once a susceptible pregnant woman is infected, making pre-conception immunity confirmation critical.
- **Tertiary prevention:** Early diagnosis and multidisciplinary management of CRS complications (see Treatment) to minimize secondary disability.
- **Public health interventions:** Population-based two-dose MMR immunization schedules, catch-up campaigns for adults (especially women of childbearing age), congenital rubella syndrome and rubella case-based surveillance (WHO/CDC), and regional elimination verification programs (Americas achieved elimination 2015; Western Pacific — 7 countries verified 2023; ongoing challenges in WHO European and Eastern Mediterranean regions due to immunity gaps) ([PMC11679470](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11679470/); [PMC11281523](https://pmc.ncbi.nlm.nih.gov/articles/PMC11281523/); [PMC11209032](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11209032/)).
- **Prophylaxis:** Post-exposure immunoglobulin has limited/uncertain efficacy in preventing CRS in exposed susceptible pregnant women and is not routinely recommended as reliable prophylaxis; the primary prophylactic strategy is pre-pregnancy vaccination.
- **Modeling of vaccine impact:** A 2025 CDC/MMWR modeling study projected current and future CRS incidence with/without rubella vaccine introduction across 19 countries through 2055, underscoring continued vaccination as essential to sustaining elimination gains ([MMWR mm7418a3](https://www.cdc.gov/mmwr/volumes/74/wr/mm7418a3.htm)).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Rubella virus infects humans exclusively as a natural host; **no known natural non-human reservoir** for classical rubella virus — "man is the only known natural reservoir," which underlies its candidacy (along with measles/polio) for global eradication given an effective vaccine ([NCBI Bookshelf NBK8200](https://www.ncbi.nlm.nih.gov/books/NBK8200/)).
- **Related zoonotic viruses:** Recently discovered relatives within the expanded *Matonaviridae* family — "rustrela virus" (found in yellow-necked field mice, and linked to a fatal encephalitis in captive zoo animals) and "rubella-like" viruses in bats — suggest an ancient zoonotic evolutionary origin for the rubella virus lineage, though these are distinct viruses, not rubella virus itself infecting animals naturally ([Nature Microbiology Community blog](https://naturemicrobiologycommunity.nature.com/posts/bats-mice-zoos-and-noses-the-zoonotic-origins-of-rubella-virus); [bioRxiv rustrela in vivo models](https://www.biorxiv.org/content/10.1101/2025.11.10.687696.full.pdf)).
- **Experimental infection:** Various laboratory animals (rabbits, mice, ferrets, non-human primates) can be experimentally infected, but **no animal reliably reproduces symptomatic human rubella or CRS** — a major limitation for pathogenesis research.
- **Veterinary relevance:** None as natural disease; rustrela virus is an emerging veterinary/zoo-animal concern (fatal non-suppurative meningoencephalomyelitis in various captive species) but is mechanistically and taxonomically distinct from classical CRS teratogenesis.

---

## 15. Model Organisms

- **No validated whole-animal model of CRS exists** — this is a significant and often-cited limitation in rubella research, since there is no animal model that reproduces the human congenital teratogenic syndrome (no reliable in vivo model of symptomatic infection or transplacental teratogenesis).
- **In vitro/cell-based models (primary research tools):**
  - Primary human fetal/umbilical vein endothelial cells (HUVEC) — used to model persistent non-cytolytic infection and angiogenesis inhibition ([PMC3734309](https://ncbi.nlm.nih.gov/pmc/articles/PMC3734309); [PMC10060672](https://pmc.ncbi.nlm.nih.gov/articles/PMC10060672/)).
  - Human brain organoids (with and without incorporated primary human microglia) — used to model neurotropism, cell-type-specific interferon responses, and CNS pathogenesis ([eLife 87696](https://elifesciences.org/articles/87696); eLife 89265 commentary).
  - Human primary brain tissue explants — show RuV predominantly infects microglia.
  - Keratinocyte cell lines (HaCaT) — used to demonstrate MOG-independent infection routes.
  - First-trimester trophoblast primary cell cultures — used to show relative resistance to RuV infection in vitro, informing placental-barrier biology ([PMC5795436](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5795436/)).
  - 293T cells with ectopic MOG expression — used to demonstrate MOG receptor sufficiency for viral entry.
- **Genetic/reverse-genetics models:** Infectious cDNA clones of the RA27/3 vaccine strain permit reverse-genetics dissection of attenuation determinants (5′ UTR, nonstructural protease region, capsid gene) ([PMID 10891421](https://pubmed.ncbi.nlm.nih.gov/10891421/)).
- **Applications:** These in vitro/organoid systems allow study of (1) viral tropism and receptor usage, (2) interferon/CXCL10-mediated angiogenesis inhibition, (3) capsid-p32-mitochondrial interaction and apoptosis modulation, (4) cell-type-specific innate immune responses in the developing CNS, and (5) vaccine-strain attenuation mechanisms — but none can model the intact maternal-fetal-placental unit or reproduce the full multi-organ CRS phenotype, which remains a major translational gap (a candidate `HUMAN_MODEL_MISMATCH` knowledge-gap framing for a future dismech entry, given that current organoid/cell-culture systems capture discrete mechanistic nodes — endothelial angiogenesis inhibition, neural progenitor/microglial infection — without validated whole-organism or whole-placental-unit confirmation of the integrated teratogenic cascade).
- **Resources:** No dedicated MGI/RGD/ZFIN rubella-disease model repository exists given the absence of a genetic-model paradigm; relevant cell lines are cataloged via ATCC/Cellosaurus (HUVEC, HaCaT, 293T) rather than whole-organism model databases.

---

## Summary for Knowledge-Base Curation

Rubella/CRS is best curated as an **infectious/teratogenic disease entry** (not a genetic disease), with:
- Evidence_source classification: predominantly HUMAN_CLINICAL for epidemiology/phenotype/diagnostics; IN_VITRO for most mechanistic pathophysiology claims (endothelial, organoid, capsid-p32 studies — note these should NOT be treated as sufficient to support human phenotype claims alone per dismech SOP); MODEL_ORGANISM evidence is essentially absent/limited given the lack of validated animal models — flag this explicitly as a knowledge gap.
- Strong candidate for a `HUMAN_MODEL_MISMATCH` discussion node given the well-documented absence of an animal model reproducing CRS.
- Causal chain suitable for a pathophysiology node structure: maternal viremia → placental/endothelial infection → (a) direct apoptotic/mitotic injury to organ precursor cells, (b) IFN-β/CXCL10-mediated angiogenesis inhibition, (c) capsid-p32 mitochondrial interaction sustaining persistent non-cytolytic infection → organ hypoplasia/malformation (classic triad) → delayed manifestations (diabetes, panencephalitis, autism).

Sources are cited throughout via PMID/PMC links; all figures given (percentages, timing windows, burden estimates) are drawn from the cited primary/secondary literature above and should be independently re-verified against cached abstracts per dismech's evidence-validation SOP before use as `snippet:` values in any KB entry.