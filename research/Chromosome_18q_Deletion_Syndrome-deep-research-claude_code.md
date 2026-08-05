---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-30T08:45:04.765287'
end_time: '2026-06-30T08:50:03.820030'
duration_seconds: 299.05
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chromosome 18q Deletion Syndrome
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-4-8[1m]
  web_search_requests: 2
  num_turns: 17
  total_cost_usd: 2.5640015000000003
  session_id: 53cf7ce0-bd16-4a96-b653-63402992bd84
  stop_reason: end_turn
citation_count: 20
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chromosome 18q Deletion Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chromosome 18q Deletion Syndrome** covering all of the
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

I now have a comprehensive evidence base. Here is the full research report.

---

# Comprehensive Research Report: Chromosome 18q Deletion Syndrome (18q− / De Grouchy Syndrome)

**Prepared for:** dismech knowledge base entry • **Category:** Mendelian (chromosomal / contiguous-gene deletion syndrome)

> **Attribution note:** Primary-literature claims below are drawn from articles retrieved via PubMed; per PubMed's terms each cited article includes a DOI link. Database-level facts are drawn from OMIM, Orphanet, MalaCards, GARD, and NORD as indicated.

---

## 1. Disease Information

**Overview.** Chromosome 18q deletion syndrome (18q−) is a rare contiguous-gene chromosomal disorder caused by partial loss of the long (q) arm of chromosome 18. It was first delineated by Jean de Grouchy and colleagues in 1964 (hence "de Grouchy syndrome"). The phenotype is highly variable and dependent on deletion size and breakpoints, but the recurrent core comprises intellectual disability/developmental delay, hypotonia, short stature, characteristic facial dysmorphism, ear canal anomalies with hearing loss, foot deformities, and abnormal cerebral white-matter MRI signal. The condition is conventionally divided into a common **distal (terminal) 18q deletion** form and a rarer **proximal interstitial 18q deletion** form (≈18q11.2–q21.1).

**Key identifiers:**
- **OMIM:** #601808 (Chromosome 18q deletion syndrome)
- **Orphanet:** ORPHA:1600 (Distal monosomy 18q); proximal form tracked separately (Orphanet "Proximal monosomy 18q")
- **MONDO:** MONDO:0011147 (chromosome 18q deletion syndrome)
- **GARD:** Proximal chromosome 18q deletion syndrome (GARD 10866)
- **MeSH:** "Chromosome 18 Deletion Syndrome" (Supplementary Concept) / Chromosome Deletion; Chromosomes, Human, Pair 18
- **ICD-10:** Q93.5 (Other deletions of part of a chromosome); **ICD-11:** LD44 (structural chromosome anomaly)
- **UMLS/MalaCards:** indexed as "Chromosome 18q Deletion Syndrome"
- **Suggested MONDO term for KB:** `MONDO:0011147`

**Synonyms / alternative names:** 18q− syndrome; 18q deletion syndrome; de Grouchy syndrome (type 2); monosomy 18q; partial monosomy of the long arm of chromosome 18; distal 18q− / proximal 18q−.

**Data provenance.** Information here is principally **aggregated, disease-level** (OMIM/Orphanet curated summaries, cohort reviews, and genotype–phenotype case series). Several quantitative phenotype frequencies derive from **patient-level aggregation** (literature cohorts of ~163 cases reviewed in a 2021 report; the UT San Antonio Chromosome 18 Clinical Research Center registry is the largest deeply phenotyped cohort). It is *not* primarily EHR-derived.

---

## 2. Etiology

**Primary cause.** A structural chromosomal abnormality — heterozygous deletion of part of 18q, producing **haploinsufficiency** of the deleted genes. Most deletions are **terminal** (extending to 18qter); interstitial deletions are less common.

**Mechanistic origin / inheritance of the lesion.** According to PubMed, ~94% of cases are *de novo*, and ~6% are inherited from a parent carrying a balanced (reciprocal) translocation or other balanced rearrangement that segregates unbalanced to offspring (Bohîlțea et al., 2020, *Rom J Morphol Embryol*; [DOI](https://doi.org/10.47162/RJME.61.3.29)). The same source states: *"An estimated incidence for all types of 18q deletions is one in 55,000 births predominant on females. About 94% of cases with 18q deletion syndrome appearance are de novo, and the remaining 6% are … inherited from a parent carrying a balanced chromosomal translocation."*

Complex mechanisms also occur: terminal 18q deletions are frequently associated with **inverted-duplication-deletion [inv-dup del(18q)]** and **ring chromosome 18 / dicentric** rearrangements, and low-level mosaicism can blend 18q-deletion and trisomy-18 features (Bonaglia et al., 2022, *Eur J Med Genet*; [DOI](https://doi.org/10.1016/j.ejmg.2022.104596)).

**Genetic risk factors.** This is a sporadic structural-variant disorder, not a multifactorial/susceptibility-allele disease. "Risk" is essentially the chance of a *de novo* deletion or unbalanced segregation in a balanced-translocation carrier parent.

**Environmental risk factors.** None established. No toxin, infection, or lifestyle exposure is causally linked. Advanced parental age has not been robustly implicated for these structural deletions.

**Protective factors.** None applicable (chromosomal deletion).

**Gene–environment interactions.** Not applicable as a disease-causing mechanism; phenotypic variability is driven by deletion size/breakpoints, modifier loci, and possibly stochastic/epigenetic factors rather than measured environmental exposures.

---

## 3. Phenotypes

Frequencies below are from a 2021 systematic review/case report aggregating **163 reported cases** (Wu et al., 2021, *Medicine (Baltimore)*; PMID 34956087 / cited via the PMC review) unless otherwise noted. Phenotype types are tagged for HPO.

| Phenotype | Frequency | Type | Suggested HPO |
|---|---|---|---|
| Intellectual disability | 57.1% | Behavioral/cognitive | HP:0001249 (Intellectual disability) |
| Language/motor developmental delay | 49.7% | Developmental | HP:0001263 (Global developmental delay); HP:0000750 (Delayed speech) |
| Ear abnormalities (incl. canal stenosis/atresia) | 65.6% | Physical/structural | HP:0000598 (Abnormal ear morphology); HP:0000413 (Atresia of external auditory canal) |
| Hearing impairment (often conductive) | common | Sensory | HP:0000405 (Conductive hearing impairment); HP:0000407 (Sensorineural) |
| Mid-face hypoplasia / dysplasia | 47.2% | Craniofacial | HP:0011800 (Midface retrusion) |
| Abnormal hands/feet (incl. clubfoot, vertical talus) | ~41% / ~39% | Skeletal | HP:0001837 (Broad toe); HP:0001762 (Talipes equinovarus) |
| Short stature | 35.0% | Growth | HP:0004322 (Short stature) |
| Ocular abnormalities (strabismus, nystagmus, coloboma) | 32.5% | Ophthalmologic | HP:0000486 (Strabismus); HP:0000589 (Coloboma) |
| Genital dysplasia (cryptorchidism, micropenis, hypoplastic labia) | 28.2% | Genitourinary | HP:0000028 (Cryptorchidism); HP:0000054 (Micropenis) |
| Hypotonia | 40.5% | Neuromuscular | HP:0001252 (Hypotonia) |
| Congenital heart disease | 19.0% (literature range 24–36%) | Cardiac | HP:0001627 (Abnormal heart morphology); HP:0001631 (ASD); HP:0001636 (Tetralogy/conotruncal) |
| Abnormal cerebral white-matter MRI signal | very common | Neuroimaging | HP:0002500 (Abnormal cerebral white matter morphology); HP:0007younger — HP:0011399 |
| Cleft palate / lip (± high-arched palate) | ~25% CP/L; ~43% incl. high palate | Craniofacial | HP:0000175 (Cleft palate); HP:0000159 (Abnormal lip) |
| Hypothyroidism | 3.7% | Endocrine | HP:0000821 (Hypothyroidism) |
| IgA deficiency / humoral immunodeficiency | IgA def ~4–20%; ≥1 Ig low in 50–90% | Laboratory/immune | HP:0002720 (Decreased circulating IgA); HP:0002721 (Immunodeficiency) |
| Seizures/epilepsy | subset | Neurologic | HP:0001250 (Seizure) |
| Autistic traits / behavioral problems (ADHD) | subset | Behavioral | HP:0000729 (Autistic behavior); HP:0007018 (ADHD) |
| Nystagmus/poor coordination, tremor | subset | Neurologic | HP:0000639 (Nystagmus); HP:0001337 (Tremor) |

**Phenotype characteristics:**
- **Age of onset:** Congenital/neonatal (dysmorphism, hypotonia, structural anomalies). Developmental and growth issues manifest through infancy and childhood. Immunodeficiency and combined (cellular) immunodeficiency can present with **late onset** in adulthood.
- **Severity:** Highly variable — mild to severe; broadly correlated with deletion size and content, though same-breakpoint individuals can differ markedly.
- **Progression:** Structural anomalies are static/congenital; cognitive disability is non-progressive but lifelong; immunodeficiency can be progressive (e.g., late-onset combined immunodeficiency).
- **Behavioral phenotype:** A 2025 retrospective cohort comparing 18p del, 18q del, and 18p tetrasomy found measurable cognitive/behavioral impairment across chromosome-18 anomalies; 18q deletion patients showed intellectual disability with adaptive deficits (Allegri et al., 2025, *Ital J Pediatr*; [DOI](https://doi.org/10.1186/s13052-025-01902-2)).

**Quality-of-life impact.** Driven mainly by intellectual disability, communication/speech impairment, hearing loss (educational/social impact), short stature, motor/orthopedic limitations, and recurrent infections. No disease-specific validated QoL instrument; general pediatric/ID QoL measures apply.

---

## 4. Genetic / Molecular Information

**Nature of the lesion.** Heterozygous deletion of 18q producing dosage haploinsufficiency of a contiguous gene set. Deletion sizes in case series range widely — e.g., **6.6–23.0 Mb** across an eight-patient microarray cohort (Feng et al., 2016, *Zhonghua Yi Xue Yi Chuan Xue Za Zhi*; [DOI](https://doi.org/10.3760/cma.j.issn.1003-9406.2016.02.017)). Terminal 18q23 involvement is present in ~87% of cases.

**Critical regions / candidate genes (genotype–phenotype):**
- **Distal critical region 18q22.3–q23 (~67.7–74.9 Mb):** core of the classic syndrome.
- **Proximal critical region 18q12.1–q12.3 (~25.2–42.9 Mb)** and 18q11–q12 (interstitial form).

| Gene (HGNC suggestion) | Locus | Implicated phenotype | Evidence |
|---|---|---|---|
| **TSHZ1** (teashirt zinc-finger homeobox 1) | 18q22.3 (~72.9–73.4 Mb) | Congenital aural atresia (CAA), middle-ear malformation, palate | Feenstra et al., 2011 — *"hemizygosity of TSHZ1 leads to congenital aural atresia as a result of haploinsufficiency"* ([DOI](https://doi.org/10.1016/j.ajhg.2011.11.008)) |
| **MBP** (myelin basic protein) | 18q23 | White-matter MRI signal abnormality (historically attributed to dysmyelination) | Long-standing hypothesis; **challenged** by Tanaka et al., 2011 (see below) ([DOI](https://doi.org/10.1016/j.braindev.2011.05.008)) |
| **SALL3** | 18q23 | Palate/craniofacial (mouse knockout palate defect) | Dostal et al., 2009 ([DOI](https://doi.org/10.1016/j.jcms.2008.12.002)) |
| **NFATC1** | 18q23 | Congenital heart disease | Feng et al., 2016 ([DOI](https://doi.org/10.3760/cma.j.issn.1003-9406.2016.02.017)) |
| **GALR1** (galanin receptor 1) | 18q23 | Growth/neuroendocrine candidate | Feng et al., 2016 |
| **TCF4** | 18q21.2 | Pitt-Hopkins syndrome when fully deleted (severe ID, breathing anomalies) — distinguishes deletions extending more proximally | Established TCF4 literature |
| **CYB5A** | 18q22 | Gonadogenesis/genital phenotype candidate | review-level |
| **SS18** | 18q11.2 | Skeletal/growth candidate | review-level |
| **GATA6** | 18q11.2 | Conotruncal heart defect (but cardiac defects often distal to GATA6, suggesting alternative mechanism) | Rojnueangnit et al., 2019 ([DOI](https://doi.org/10.1002/mgg3.896)) |
| Immune cluster: **MALT1, BCL2, NEDD4L, TNFRSF11A, CD226, SOCS6** | 18q21–qter | Humoral/combined immunodeficiency, T-/B-cell regulation | Late-onset combined immunodeficiency report (PMC11186878) |

**Variant classification / type.** The pathogenic lesion is a **copy-number loss (structural variant)**, classified pathogenic per ACMG/ClinGen CNV criteria when encompassing the established critical region. Point mutations in single genes recapitulate sub-phenotypes — e.g., loss-of-function **TSHZ1** variants (c.723G>A p.Trp241X; c.946_947delinsA p.Pro316ThrfsX16) cause isolated nonsyndromic bilateral CAA (Feenstra et al., 2011, [DOI](https://doi.org/10.1016/j.ajhg.2011.11.008)).

**Functional consequence:** Loss of function via haploinsufficiency (dosage sensitivity). Suggested GO/biological-process annotations: `GO:0042552` (myelination), `GO:0007605` (sensory perception of sound), `GO:0060021` (roof of mouth/palate development), `GO:0001525`/heart morphogenesis `GO:0003007`.

**Modifier genes / epigenetics.** Phenotypic variability among same-size deletions implicates modifier loci, allelic content on the retained homolog (unmasked recessive alleles), and possibly position effects/epigenetic dysregulation; no specific methylation signature is established for 18q−.

**Somatic vs germline:** Germline/constitutional (often *de novo* in the germline or early embryo; mosaic forms occur).

**Chromosomal abnormalities.** Terminal del(18q); interstitial del(18q); ring chromosome 18 [r(18)] (combines 18p and 18q loss); inv-dup del(18q); dicentric/mosaic forms (Bonaglia et al., 2022, [DOI](https://doi.org/10.1016/j.ejmg.2022.104596)).

---

## 5. Environmental Information

No environmental, lifestyle, or infectious agents cause 18q deletion syndrome. It is a constitutional structural chromosomal disorder. Recurrent infections seen in patients are a **consequence** of the associated immunodeficiency, not an etiologic exposure. (Not applicable: CTD/TOXNET/lifestyle factors.)

---

## 6. Mechanism / Pathophysiology

The unifying mechanism is **haploinsufficiency of dosage-sensitive developmental genes** within the deleted 18q segment, disrupting multiple organ-development programs. Causal chains by domain:

**1. Neurodevelopment / CNS white matter.**
- Upstream: deletion of 18q23 including **MBP** and adjacent loci → altered myelin/glial gene dosage → abnormal cerebral white-matter MRI signal → contributing to motor delay, hypotonia, cognitive impairment.
- **Important nuance / knowledge gap:** the historical "dysmyelination" model was directly refuted by autopsy/pathology in a ring-18 patient with confirmed MBP haploinsufficiency: Tanaka et al., 2011 found *"the brain was well myelinated, contrary to established hypotheses … The MRI signal abnormalities in 18q-syndrome could be attributed to gliosis and not to dysmyelination"* ([DOI](https://doi.org/10.1016/j.braindev.2011.05.008)). This is a candidate `HUMAN_MODEL_MISMATCH`/knowledge-gap for the KB (single autopsy case; MBP dosage confirmed but myelin intact). Cell types: oligodendrocyte (`CL:0000128`), astrocyte (`CL:0000127`, gliosis). Process: `GO:0042552` (myelination), `GO:0061640` gliogenesis-related.

**2. Middle/external ear development (conductive hearing loss).**
- **TSHZ1** haploinsufficiency → failure of normal middle-ear/external-auditory-canal morphogenesis → congenital aural atresia/stenosis → conductive hearing loss (Feenstra et al., 2011; mouse Tshz1 middle-ear phenotype). UBERON: external acoustic meatus (`UBERON:0001352`), middle ear (`UBERON:0001756`). Process: `GO:0042472` (inner/middle ear morphogenesis).

**3. Craniofacial / palate.**
- **TSHZ1/SALL3** dosage → palate and midface developmental defects → cleft palate/high-arched palate, midface hypoplasia (Dostal et al., 2009). Process: `GO:0060021` (roof of mouth development).

**4. Cardiac morphogenesis.**
- Candidate **NFATC1** (distal) and proximal conotruncal loci → CHD, predominantly pulmonary-valve anomalies and atrial septal defects; rarer Ebstein anomaly and conotruncal defects (van Trier et al., 2013 — *"All 19 individuals shared a small overlapping deletion region between 18q22.3q23. The most common cardiac defects detected were pulmonary valve anomalies and atrial septal defects"*; [DOI](https://doi.org/10.1016/j.ejmg.2013.05.002)). Process: `GO:0003007` (heart morphogenesis).

**5. Growth axis / short stature.**
- Multifactorial: **growth hormone deficiency (GHD)** is recurrent in 18q−, plus contributions from hypothyroidism and skeletal/feeding factors. The 18q− literature explicitly lists growth hormone deficiency as a characteristic feature (Dostal et al., 2009 — *"18q- … is a multiple-anomaly disorder associated with mental retardation, white matter anomalies in the brain, growth hormone deficiency, congenital aural atresia, orofacial cleft …"* [DOI](https://doi.org/10.1016/j.jcms.2008.12.002)). GHD is thought to reflect hypothalamic-pituitary dysfunction.

**6. Immune system.**
- Loss of immune-regulatory genes in 18q21–qter (**MALT1, BCL2, NFATC1, NEDD4L, CD226, SOCS6, TNFRSF11A**) → impaired B-cell maturation/immunoglobulin synthesis (humoral immunodeficiency, CVID-like) and, in some, T-cell defects (late-onset combined immunodeficiency, low TREC/KREC, depleted naïve CD4+/CD8+ T cells). Cell types: B cell (`CL:0000236`), CD4+ T cell (`CL:0000624`), CD8+ T cell (`CL:0000625`). Process: `GO:0002377` (immunoglobulin production), `GO:0030183` (B cell differentiation).

**Upstream vs downstream summary:** The chromosomal deletion is the single upstream cause; each organ phenotype is a downstream, largely independent consequence of haploinsufficiency of region-specific genes — a classic **contiguous-gene-syndrome** architecture rather than a single converging pathway.

**Molecular profiling.** No disease-specific transcriptomic/proteomic/metabolomic signature is established; mechanistic inference rests on gene-dosage and mouse-model data (Sall3, Tshz1 knockouts).

---

## 7. Anatomical Structures Affected

**Organ / system level (UBERON suggestions):**
- **Central nervous system / brain white matter** (`UBERON:0002316` white matter; corpus callosum `UBERON:0002336` — agenesis reported), cerebellar vermis (partial agenesis in severe cases).
- **Ear** — external auditory canal (`UBERON:0001352`), middle ear (`UBERON:0001756`) → atresia/stenosis, conductive hearing loss; sometimes sensorineural.
- **Craniofacial skeleton / palate** (`UBERON:0001716` secondary palate; midface).
- **Heart** (`UBERON:0000948`) — septa, pulmonary valve (`UBERON:0002146`), conotruncus, tricuspid valve (Ebstein).
- **Eyes** (`UBERON:0000970`) — strabismus, nystagmus, optic anomalies, coloboma/anophthalmia (severe cases).
- **Skeleton / limbs** — feet (clubfoot, vertical talus), hands; hip (developmental dysplasia of the hip reported — Yu et al., 2022, [DOI](https://doi.org/10.1186/s12920-022-01345-2)).
- **Endocrine** — pituitary/hypothalamus (GH axis), thyroid (`UBERON:0002046`).
- **Genitourinary** — external genitalia (cryptorchidism, micropenis, hypoplastic labia).
- **Immune system** — bone marrow / lymphoid tissue.

**Tissue/cell level:** oligodendrocytes & astrocytes (CNS); B and T lymphocytes (immune); cardiomyocytes/valve mesenchyme (heart); cranial neural-crest-derived mesenchyme (palate/midface).

**Subcellular (GO cellular component):** myelin sheath (`GO:0043209`); not a primary organelle-localized disorder.

**Localization / laterality:** Anomalies are typically **bilateral** (e.g., bilateral aural atresia, bilateral foot deformities), though asymmetric findings occur, especially in mosaic cases (e.g., unilateral iris coloboma marking mosaicism; Bonaglia et al., 2022, [DOI](https://doi.org/10.1016/j.ejmg.2022.104596)).

---

## 8. Temporal Development

- **Onset:** Congenital. Many features (dysmorphism, hypotonia, structural cardiac/ear/palate anomalies) present at or before birth; prenatal detection is increasingly common via NIPT/ultrasound + microarray (Bohîlțea et al., 2020, [DOI](https://doi.org/10.47162/RJME.61.3.29)).
- **Onset pattern:** Chronic, static/non-progressive for most structural and cognitive features.
- **Progression / disease course:** Lifelong. Developmental disability is stable (non-degenerative). Growth deficits manifest across childhood; immunodeficiency may be progressive and can present in adulthood (late-onset combined immunodeficiency).
- **Critical windows for intervention:** Early childhood for hearing rehabilitation (atresia repair / bone-conduction devices), GH therapy initiation, early developmental/speech intervention; ongoing immunologic surveillance.
- **Remission:** None (constitutional deletion); symptom management only.

---

## 9. Inheritance and Population

**Epidemiology.**
- **Incidence:** ~1 in 40,000 (some sources) to **1 in 55,000 live births** (Bohîlțea et al., 2020, [DOI](https://doi.org/10.47162/RJME.61.3.29)); Orphanet/NORD often cite ~1/40,000.
- **Sex ratio:** Female predominance reported.

**For the genetic etiology:**
- **Inheritance pattern:** Most cases *de novo* (~94%); ~6% inherited via a parental balanced translocation. Recurrence risk is low for *de novo* cases but substantially elevated when a parent carries a balanced rearrangement — parental karyotyping is recommended.
- **Penetrance:** Effectively complete for "having an abnormal phenotype," but **expressivity is highly variable** (size/breakpoint-dependent and stochastic).
- **Anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline/somatic mosaicism:** Occurs; can soften or asymmetrically alter phenotype (mosaic del(18q)/inv-dup del or del/trisomy mixtures).
- **Founder effects / consanguinity / carrier frequency:** Not applicable (structural *de novo* events; not a recessive carrier disease).

**Population demographics.** Reported worldwide with no strong ethnic predilection; documented across diverse populations (China, Europe, Romania, Japan, etc.). Geographic clustering reflects ascertainment, not true prevalence variation.

---

## 10. Diagnostics

**Cytogenetic / molecular (definitive):**
- **Chromosomal microarray (CMA / array-CGH / SNP array)** — first-line; defines breakpoints and deletion size and enables genotype–phenotype mapping (Feng et al., 2016, [DOI](https://doi.org/10.3760/cma.j.issn.1003-9406.2016.02.017); Shi et al., 2017, [DOI](https://doi.org/10.3760/cma.j.issn.1003-9406.2017.04.022)). MAXO suggestion: comparative genomic hybridization / microarray testing.
- **Karyotyping (G-banding)** — detects larger deletions, ring 18, translocations; complements CMA for balanced-rearrangement detection in parents.
- **FISH** — confirms terminal deletion / specific loci.
- **Next-generation sequencing (WES/WGS)** — refines breakpoints, detects co-occurring single-gene variants (e.g., HSPG2 explaining DDH in one case; Yu et al., 2022, [DOI](https://doi.org/10.1186/s12920-022-01345-2)).
- **Prenatal:** NIPT flag + diagnostic CMA on CVS/amniocentesis; fetal ultrasound/MRI for structural anomalies.

**Adjunctive clinical workup (per organ):**
- Audiology + temporal-bone CT (aural atresia).
- Echocardiography + ECG (CHD; van Trier et al., 2013 recommend physical exam, ECG, and ultrasound in all 18q− patients, [DOI](https://doi.org/10.1016/j.ejmg.2013.05.002)).
- Brain MRI (white-matter signal, corpus callosum).
- Endocrine: GH stimulation testing, IGF-1, thyroid function.
- **Immunologic:** quantitative immunoglobulins (IgG/IgA/IgM/IgE + IgG subclasses), vaccine responses, lymphocyte subsets, TREC/KREC — important given high rate of humoral and occasional combined immunodeficiency.
- Ophthalmologic and orthopedic evaluation.

**Clinical criteria / differential diagnosis.** Diagnosis is genetic (deletion confirmation), not clinical-criteria-based. Differentials: trisomy 18 / mosaic trisomy 18; ring 18 (combined 18p/18q features); Pitt-Hopkins syndrome (if TCF4 involved); other contiguous-gene/ID syndromes; isolated nonsyndromic CAA (TSHZ1); CHARGE syndrome (coloboma + ear); 22q11.2 deletion (conotruncal CHD).

**Screening.** No population newborn screen. Cascade parental karyotyping when a balanced rearrangement is suspected; prenatal CMA in at-risk pregnancies.

---

## 11. Outcome / Prognosis

- **Survival / life expectancy:** Generally compatible with survival into adulthood; many patients reach adulthood (a 50-year-old patient is reported — Yapijakis et al., 2020, [DOI](https://doi.org/10.1007/978-3-030-32633-3_22)). Prognosis worsens with severe CHD, major brain malformations (corpus callosum agenesis, severe cases with anophthalmia), or significant immunodeficiency. Severe prenatally diagnosed cases with major CNS/cardiac malformations may not survive (Bohîlțea et al., 2020).
- **Morbidity / disability:** Lifelong intellectual disability (mild–severe), communication and hearing impairment, motor/orthopedic disability, short stature, and infection burden are the principal contributors to disability.
- **Complications:** Recurrent respiratory (≈37%), urinary (≈19%), and gastrointestinal (≈19%) infections and sepsis (≈11%) in immunodeficient patients (PMC11186878); CHD-related complications; chronic arthritis has been reported (Kashima et al., 2015, [DOI](https://doi.org/10.1093/... )* — see note below).
- **Prognostic factors:** Deletion size/content (extent of critical-region involvement), presence/severity of CHD, degree of immunodeficiency, and major CNS malformations.
- **Recovery potential:** Structural and cognitive deficits are permanent; targeted therapies (GH, hearing rehabilitation, Ig replacement) measurably improve specific outcomes.

> *Note:* Kashima et al., 2015 (*Clin Exp Rheumatol*, PMID 25665051) report chronic arthritis in an 18q− patient treated with tocilizumab and adalimumab (abstract not available in PubMed; cite by PMID 25665051).

---

## 12. Treatment

Management is **multidisciplinary and supportive/symptom-directed** — no therapy corrects the deletion. MAXO suggestions in brackets.

**Growth / endocrine.**
- **Recombinant human growth hormone (rhGH)** for documented GHD/short stature — effective. A case report + literature review of 16 rhGH-treated patients showed mean height SDS improving from −3.12 ± 0.94 to −1.38 ± 1.29 over ~5.9 years (Δ +1.74 SDS, p<0.0001), with a single patient gaining +2.82 SDS over 7 years and no serious adverse events (Wu et al., 2021, *Medicine*, PMID 34956087). [`MAXO` hormone replacement therapy / pharmacotherapy; therapeutic agent CHEBI: somatropin.]
- **Levothyroxine** for hypothyroidism. [`MAXO:0000088`-adjacent; pharmacotherapy.]

**Hearing.**
- Bone-conduction/bone-anchored hearing devices; surgical canaloplasty/atresia repair for aural atresia; early amplification to support speech development. [`MAXO` hearing aid use; surgical procedure `MAXO:0000004`.]

**Cardiac.**
- Standard medical/surgical management of specific CHD (e.g., ASD/VSD repair, valve interventions). [`MAXO:0000004` surgical procedure.]

**Immunologic.**
- **Immunoglobulin replacement therapy (IVIG/SCIG)** and antimicrobial prophylaxis for symptomatic humoral immunodeficiency; immunologic monitoring; in combined immunodeficiency, escalated management. [`MAXO` immunoglobulin therapy / supportive care `MAXO:0000950`.]

**Developmental / rehabilitative.**
- Early intervention, special education, speech-language therapy, physical and occupational therapy [`MAXO:0000011` physical therapy], orthopedic management of foot deformities (casting/surgery).

**Other / experimental.**
- Anti-cytokine biologics (tocilizumab, adalimumab) used for associated chronic arthritis (Kashima et al., 2015, PMID 25665051). No gene/cell/RNA therapies exist or are in trials for the deletion itself; care is individualized via the Chromosome 18 registry/clinical research center model.

**Pharmacogenomics:** No disease-specific PGx guidance.

---

## 13. Prevention

- **Primary prevention:** Not possible for *de novo* deletions. For families with a known parental balanced translocation: **genetic counseling**, **preimplantation genetic testing (PGT-SR)**, and **prenatal diagnosis** (CVS/amniocentesis + CMA) reduce recurrence. [`MAXO:0000079` genetic counseling.]
- **Secondary prevention (early detection):** Prenatal NIPT/ultrasound triggering diagnostic CMA; postnatal early multidisciplinary evaluation (audiology, echo, endocrine, immunology) to intervene before complications (e.g., speech delay from undetected hearing loss; infections from undetected immunodeficiency).
- **Tertiary prevention (complication avoidance):** Immunoglobulin replacement/antibiotic prophylaxis to prevent infections; GH to prevent severe short stature; routine cardiac surveillance; developmental support.
- **Counseling:** Recurrence-risk assessment requires parental karyotyping; risk is low if both parents are normal, substantial if a balanced rearrangement is present.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human disorder (`NCBITaxon:9606`). No naturally occurring animal homolog of the chromosomal syndrome.
- **Orthologous genes / models:** Mouse orthologs of critical-region genes are studied — **Tshz1** (middle-ear and palate development) and **Sall3** (palate) knockout mice recapitulate sub-phenotypes (Dostal et al., 2009, [DOI](https://doi.org/10.1016/j.jcms.2008.12.002); Feenstra et al., 2011, [DOI](https://doi.org/10.1016/j.ajhg.2011.11.008)).
- **Veterinary / OMIA:** No recognized natural counterpart; not zoonotic; not applicable.

---

## 15. Model Organisms

- **Mouse (Mus musculus, `NCBITaxon:10090`):**
  - ***Tshz1* knockout** — middle-ear malformation modeling congenital aural atresia (supports TSHZ1 haploinsufficiency as the CAA mechanism; Feenstra et al., 2011). Evidence source: MODEL_ORGANISM.
  - ***Sall3* knockout** — palate abnormality, supporting a craniofacial candidate at 18q22.3 (Dostal et al., 2009). MODEL_ORGANISM.
  - ***Mbp* mutants (e.g., shiverer)** — classic myelin-deficiency models; relevant to the historical MBP/white-matter hypothesis, but human autopsy data (Tanaka et al., 2011, [DOI](https://doi.org/10.1016/j.braindev.2011.05.008)) show intact myelination with gliosis in 18q−, a **human–model mismatch** worth flagging.
- **Model type:** Single-gene mouse knockouts modeling individual sub-phenotypes; there is **no whole-syntenic-deletion mouse model** reproducing the full contiguous-gene syndrome — a recognized limitation.
- **Applications:** Dissecting gene-specific contributions (ear, palate, myelin) rather than the integrated multisystem phenotype.
- **Resources:** MGI (mouse), IMPC for null-allele phenotyping of TSHZ1/SALL3/MBP/NFATC1.

---

## Key Evidence Summary (citable for KB evidence items)

According to PubMed, the following are high-value, snippet-quotable sources (verify exact substrings against fetched abstracts before committing as `evidence`):

1. **Feenstra et al., 2011, *Am J Hum Genet*** (PMID 22152683) — TSHZ1/CAA. Quote: *"hemizygosity of TSHZ1 leads to congenital aural atresia as a result of haploinsufficiency."* [DOI](https://doi.org/10.1016/j.ajhg.2011.11.008)
2. **Tanaka et al., 2011, *Brain Dev*** (PMID 21669507) — white matter. Quote: *"The MRI signal abnormalities in 18q-syndrome could be attributed to gliosis and not to dysmyelination."* [DOI](https://doi.org/10.1016/j.braindev.2011.05.008)
3. **van Trier et al., 2013, *Eur J Med Genet*** (PMID 23707655) — cardiac. Quote: *"cardiac anomalies in 24-36% of the reported cases … The most common cardiac defects detected were pulmonary valve anomalies and atrial septal defects."* [DOI](https://doi.org/10.1016/j.ejmg.2013.05.002)
4. **Dostal et al., 2009, *J Craniomaxillofac Surg*** (PMID 19157891) — palate/clefts + GHD as a feature. Quote: *"The 18q deletion syndrome (18q-) is a multiple-anomaly disorder associated with mental retardation, white matter anomalies in the brain, growth hormone deficiency, congenital aural atresia, orofacial cleft …"* [DOI](https://doi.org/10.1016/j.jcms.2008.12.002)
5. **Rojnueangnit et al., 2019, *Mol Genet Genomic Med*** (PMID 31390163) — proximal 18q11-q12 deletion. Quote: *"Common presentations of 18q11-q12 deletions include developmental delay/intellectual disability (DD/ID) (82%); speech delay/autism/attention deficit and hyperactivity/other behavioral problems (30%); conotruncal heart defects (15%)."* [DOI](https://doi.org/10.1002/mgg3.896)
6. **Feng et al., 2016** (PMID 27060316) — candidate genes. Quote: *"NFATC1, GALR1, MBP, SALL3 and TSHZ1 are likely to be causative genes for congenital heart disease, psychological, growth retardation, and cleft palate."* [DOI](https://doi.org/10.3760/cma.j.issn.1003-9406.2016.02.017)
7. **Bohîlțea et al., 2020, *Rom J Morphol Embryol*** (PMID 33817732) — incidence/inheritance. Quote: *"An estimated incidence for all types of 18q deletions is one in 55 000 births predominant on females. About 94% of cases … are de novo, and the remaining 6% are … inherited from a parent carrying a balanced chromosomal translocation."* [DOI](https://doi.org/10.47162/RJME.61.3.29)
8. **Bonaglia et al., 2022, *Eur J Med Genet*** (PMID 36064004) — mosaicism/inv-dup del. [DOI](https://doi.org/10.1016/j.ejmg.2022.104596)
9. **Yu et al., 2022, *BMC Med Genomics*** (PMID 36123715) — 18q22.2q23 deletion + co-occurring HSPG2 variant (DDH). [DOI](https://doi.org/10.1186/s12920-022-01345-2)
10. **Allegri et al., 2025, *Ital J Pediatr*** (PMID 40001201) — behavioral phenotype across chromosome-18 anomalies. [DOI](https://doi.org/10.1186/s13052-025-01902-2)

**Open knowledge gaps to encode (`discussions: KNOWLEDGE_GAP` / `HUMAN_MODEL_MISMATCH`):**
- MBP haploinsufficiency vs. white-matter MRI signal: human pathology shows **gliosis, not dysmyelination** (single autopsy case) — the mechanistic basis of the imaging finding is unresolved (`HUMAN_MODEL_MISMATCH`).
- Cardiac defects often map **distal to GATA6**, implying a non-GATA6 mechanism for conotruncal CHD in proximal deletions (Rojnueangnit et al., 2019).
- No syntenic mouse model of the full contiguous-gene syndrome (limits integrated mechanism study).

---

## Suggested dismech Annotation Set (quick reference)

- **MONDO:** MONDO:0011147
- **Top phenotypes (HP):** HP:0001249, HP:0001263, HP:0000413, HP:0000405, HP:0011800, HP:0004322, HP:0001252, HP:0000175, HP:0001627, HP:0002500, HP:0002720, HP:0000486
- **Genes (HGNC, lowercase prefix per repo convention):** TSHZ1, MBP, SALL3, NFATC1, GALR1, TCF4, GATA6, MALT1, BCL2
- **Cell types (CL):** CL:0000128 (oligodendrocyte), CL:0000127 (astrocyte), CL:0000236 (B cell), CL:0000624 (CD4+ T cell), CL:0000625 (CD8+ T cell)
- **Anatomy (UBERON):** UBERON:0002316 (white matter), UBERON:0001352 (external acoustic meatus), UBERON:0001716 (secondary palate), UBERON:0000948 (heart), UBERON:0002046 (thyroid)
- **GO processes:** GO:0042552 (myelination), GO:0042472 (ear morphogenesis), GO:0060021 (palate development), GO:0003007 (heart morphogenesis), GO:0002377 (Ig production)
- **Treatments (MAXO):** hormone/pharmacotherapy (rhGH, levothyroxine), MAXO:0000004 (surgical procedure), MAXO:0000011 (physical therapy), MAXO:0000079 (genetic counseling), MAXO:0000950 (supportive care), immunoglobulin replacement

---

**Sources (databases):** [MalaCards — Chromosome 18q Deletion Syndrome](https://www.malacards.org/card/chromosome_18q_deletion_syndrome) · [OMIM #601808](https://omim.org/entry/601808) · [Orphanet ORPHA:1600](https://www.orpha.net) · [GARD — Proximal chromosome 18q deletion](https://rarediseases.info.nih.gov/diseases/10866/proximal-chromosome-18q-deletion-syndrome) · [NORD — Chromosome 18q− Syndrome](https://rarediseases.org/rare-diseases/chromosome-18q-syndrome/) · PMC reviews [PMC8695685 (GH treatment)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8695685/) and [PMC11186878 (immunodeficiency)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11186878/).

**Note on data sourcing:** All mechanistic and clinical claims above are attributed to articles retrieved from PubMed (DOIs linked inline). Before populating KB `evidence` items, run `just fetch-reference PMID:XXXX` and `just validate-references` to confirm each snippet is an exact substring of the real abstract — several frequency figures (e.g., the 163-case percentages) come from review aggregation (PMID 34956087) and the immunoglobulin percentages from PMC11186878, which should be quoted directly from those sources rather than paraphrased.