---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-12T23:43:56.703561'
end_time: '2026-08-12T23:49:06.656154'
duration_seconds: 309.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Biliary Atresia
  mondo_id: ''
  category: Complex
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
  web_search_requests: 22
  num_turns: 24
  total_cost_usd: 2.0889876000000003
  session_id: ae63f865-b546-577f-95c5-d1e947dfd3d2
  stop_reason: end_turn
citation_count: 84
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Biliary Atresia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Biliary Atresia** covering all of the
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

# Biliary Atresia: Comprehensive Disease Research Report

## 1. Disease Information

**Overview.** Biliary atresia (BA) is a rare, idiopathic, progressive fibro-obliterative cholangiopathy of infancy that destroys the extrahepatic bile ducts (and, in later stages, the intrahepatic ducts), producing complete obstruction of bile flow. It is the most common cause of neonatal cholestasis requiring surgery and the leading indication for pediatric liver transplantation worldwide. Untreated, it progresses to biliary cirrhosis and hepatic failure within the first 1–2 years of life ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK537262/); [PMC7273417](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7273417/)).

**Key identifiers:**
- **OMIM:** 210500 — "BILIARY ATRESIA, EXTRAHEPATIC; EHBA" ([OMIM Clinical Synopsis](https://omim.org/clinicalSynopsis/210500))
- **Orphanet:** ORPHA:498345 (Biliary atresia and associated disorders, umbrella), ORPHA:30391 (Isolated biliary atresia), ORPHA:498350 (Syndromic biliary atresia) ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Expert=30391&lng=EN))
- **ICD-11:** LB20.21 (biliary atresia)
- **MONDO:** MONDO:0008867
- **MeSH:** D001656 (Biliary Atresia)

**Synonyms:** Extrahepatic biliary atresia (EHBA); congenital biliary atresia; progressive obliterative cholangiopathy of infancy; biliary atresia splenic malformation (BASM) syndrome for the syndromic laterality-defect subtype.

**Evidence base:** Information is derived from a mixture of aggregated disease-level resources — national/regional registries (Taiwan, Korea, France, UK, Saudi Arabia, US Western Pediatric Surgery Research Consortium), multicenter cohort studies (e.g., ChiLDReN network in the US), case-control epidemiologic studies (National Birth Defects Prevention Study), and mechanistic studies in animal/organoid models — rather than single-patient EHR extraction. Genetic findings come from case series, exome-sequencing trio studies, and GWAS meta-analyses.

Sources: [Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Expert=30391&lng=EN), [OMIM](https://omim.org/clinicalSynopsis/210500), [GARD](https://rarediseases.info.nih.gov/diseases/12010/biliary-atresia/), [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK537262/)

---

## 2. Etiology

BA is now understood as a **final common phenotype reached via multiple distinct pathogenic routes** rather than a single-cause disease ([PMC8658215 — "Biliary Atresia: Clinical Phenotypes and Aetiological Heterogeneity"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8658215/)):

### Disease Causal Factors (mechanistic/etiologic subtypes)
1. **Isolated (non-syndromic) BA** (~80–90% of cases) — thought to arise from a perinatal insult (viral infection, toxin) superimposed on a susceptible genetic background, triggering an aberrant innate/adaptive immune attack on cholangiocytes.
2. **Syndromic BA / Biliary Atresia Splenic Malformation (BASM) syndrome** (~10–20%) — a laterality/ciliopathy disorder with situs anomalies (polysplenia/asplenia, malrotation, interrupted inferior vena cava, cardiac defects, preduodenal portal vein), attributed to disrupted left-right patterning during early embryogenesis (embryonic/fetal-form BA, often diagnosed prenatally or at birth without a jaundice-free interval) ([PMC6579603](https://pmc.ncbi.nlm.nih.gov/articles/PMC6579603/)).
3. **Cystic biliary atresia** — a cyst is present within an otherwise atretic biliary remnant, sometimes detectable prenatally.
4. **Cytomegalovirus (CMV)-associated BA** — a subgroup with elevated anti-CMV IgM, later disease onset, higher GGT, and possibly worse Kasai outcomes.
5. **Toxin-associated (biliatresone) BA** — the paradigm from naturally occurring livestock disease.

### Genetic Risk Factors
- **GWAS-implicated common variants:** *ADD3* (adducin 3) — top SNP rs17095355, replicated across Chinese, Thai, and Caucasian cohorts as an eQTL; *GPC1* (glypican 1) — rs6707262/rs6750380; *ARF6*; and *EFEMP1* (2p16.1 locus, a GWAS hit in a European cohort) ([PMC7202506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7202506/); [PMC6107291](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6107291/)). Zebrafish knockdown of these genes impairs bile excretion and intrahepatic biliary network formation, functionally validating the GWAS signal.
- **BASM/laterality genes:** *CFC1* (Cryptic Family 1, NODAL co-receptor) — heterozygous mutations reported in familial heterotaxy/BASM ([PMID:18162845](https://pubmed.ncbi.nlm.nih.gov/18162845/); [PMID:31633655](https://pubmed.ncbi.nlm.nih.gov/31633655/)); **PKD1L1** — biallelic rare variants in 5 BASM subjects, a ciliary calcium-signaling gene involved in left-right axis determination, with zebrafish *pkd1l1* loss producing biliary defects ([PMC6642859](https://pmc.ncbi.nlm.nih.gov/articles/PMC6642859/); [PMC10581383](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10581383/)).
- **De novo / rare candidate variants from exome sequencing:** *STIP1* and *REV1* (HSP90 co-chaperone / DNA-repair pathway, modulate biliatresone toxicity in zebrafish and human cholangiocytes) in one 30-trio cohort, not replicated in a separate 54-trio Asian cohort; additional candidate genes *AMER1, INVS, OCRL, PCNT, KIF3B, TTC17* from family-based sequencing, reflecting genetic heterogeneity ([Nature Sci Rep 2021](https://www.nature.com/articles/s41598-021-01148-y); [PMC7026070](https://pmc.ncbi.nlm.nih.gov/articles/PMC7026070/)).
- **Copy number variation:** a candidate susceptibility region at 2q37.3 ([PMC2914625](https://pmc.ncbi.nlm.nih.gov/articles/PMC2914625/)).
- Overall inheritance is **non-Mendelian/multifactorial**: 97.1% of twin pairs are discordant (55.9% of discordant pairs monozygotic), and familial recurrence is rare (>30 multiplex families reported worldwide), implying gene–environment or epigenetic/stochastic contributions on top of genetic susceptibility ([PMID:32504124](https://pubmed.ncbi.nlm.nih.gov/32504124/); [PMID:2993572](https://pubmed.ncbi.nlm.nih.gov/2993572/)).

### Environmental Risk Factors
- **Prenatal maternal infection:** intestinal and genitourinary tract infections during pregnancy significantly associated with offspring BA in a case-control study (447 cases / 2,912 controls) ([PMC10765264](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765264/)).
- **Maternal metabolic/behavioral factors:** maternal type 2 diabetes (OR 2.17, 95% CI 1.04–4.53) and non-dependent drug abuse (OR 3.02, 95% CI 1.34–6.78) associated with increased BA risk; maternal smoking, advanced maternal age, mode of delivery, and singleton vs. multiple pregnancy were **not** significantly associated ([Pediatr Res 2022](https://www.nature.com/articles/s41390-022-02166-w)).
- **Plant/environmental toxin exposure (biliatresone):** an isoflavonoid electrophile from *Dysphania* spp. plants ("pigweed") causally linked to BA-like outbreaks in lambs and calves grazing during Australian droughts; low-dose prenatal biliatresone exposure in pregnant mice causes subclinical biliary injury in offspring, supporting an in-utero "hit" model even without overt maternal illness ([PMC10997102](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10997102/); [Penn Today](https://penntoday.upenn.edu/news/plant-toxin-causes-biliary-atresia-animal-model-according-penn-study); Biliatresone [Wikipedia](https://en.wikipedia.org/wiki/Biliatresone)).
- **Viral infection:** rotavirus (particularly group C and rhesus rotavirus, RRV) and reovirus have long been implicated as perinatal triggers of the isolated form, based on the RRV murine model recapitulating human disease (see Mechanism section).

### Protective Factors
No well-established genetic or environmental protective factors have been identified in the literature reviewed; this remains an evidence gap. gnomAD-level population allele-frequency data for candidate risk loci have not been systematically surveyed for protective alleles.

### Gene-Environment Interactions
The leading hypothesis is a **"two-hit" or susceptibility-plus-trigger model**: a genetically susceptible fetus/neonate (e.g., variants affecting glutathione/redox handling, ciliary/laterality genes, or bile duct development) is exposed to an environmental insult (viral infection or toxin) during a critical developmental window, precipitating cholangiocyte injury that is then amplified by an aberrant innate/adaptive immune response ([PMC9277099 — "Genetic Factors and Their Role in the Pathogenesis of Biliary Atresia"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9277099/); [PMC5251204 — glutathione pathway determines biliatresone susceptibility](https://pmc.ncbi.nlm.nih.gov/articles/PMC5251204/)).

Suggested ontology terms: **GENO:0000840** (susceptibility), **MONDO:0008867**, causal genes **hgnc:238** (ADD3), **hgnc:4451** (GPC1), **hgnc:9820** (PKD1L1), **hgnc:1904** (CFC1), **hgnc:11376** (STIP1), **hgnc:9958** (REV1); exposure term **ECTO** biliatresone/plant-toxin ingestion (no confirmed ECTO ID identified in this search — verify locally with OAK).

---

## 3. Phenotypes

### Core presenting triad (symptoms/signs)
| Phenotype | Onset | Frequency | Suggested HPO |
|---|---|---|---|
| Persistent/progressive jaundice beyond 2 weeks of age | Neonatal (2–8 weeks) | Nearly universal | **HP:0000952** Jaundice |
| Acholic (pale/clay-colored) stools | Presents ~2 weeks, unequivocal by 1 month | Very frequent | **HP:0011016** (abnormal stool color) / consider a more specific acholic-stool term if available in HPO |
| Dark urine | Concurrent with jaundice | Very frequent | **HP:0031829** or general "abnormal urine color" term |
| Conjugated (direct) hyperbilirubinemia | Neonatal | Universal (defining lab finding) | **HP:0002904** Hyperbilirubinemia (specify conjugated) |
| Hepatomegaly | Progressive over weeks | Frequent | **HP:0002240** Hepatomegaly |
| Elevated serum GGT | Neonatal | Frequent, diagnostic clue | **HP:0004431** Elevated hepatic transaminase / GGT-specific lab term |
| Splenomegaly (as fibrosis/portal hypertension develops) | Later infancy | Occasional-to-frequent as disease progresses | **HP:0001744** Splenomegaly |

Source: [AASLD](https://www.aasld.org/liver-fellow-network/core-series/pathology-pearls/biliary-atresia); [PMC8658215](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8658215/); [PMC9297290](https://pmc.ncbi.nlm.nih.gov/articles/PMC9297290/)

### BASM/syndromic-form associated anomalies (laterality defects)
- Polysplenia or asplenia — **HP:0009806** / **HP:0001746**
- Situs inversus / midline liver — **HP:0003363**
- Interrupted inferior vena cava, preduodenal portal vein
- Cardiac malformations: dextrocardia, Tetralogy of Fallot — **HP:0001671**
- Intestinal malrotation — **HP:0002566**

### Later/progressive phenotypes (laboratory + clinical)
- Cirrhosis and portal hypertension — **HP:0001394**
- Ascites — **HP:0001541**
- Coagulopathy (fat-soluble vitamin K malabsorption) — **HP:0001928**
- Failure to thrive/growth failure — **HP:0001508**
- Pruritus (from cholestasis)
- Variceal bleeding in advanced disease
- Cholangitis (recurrent, post-Kasai) — a major post-surgical complication

### Phenotype characteristics
- **Age of onset:** Neonatal, typically apparent by 2–8 weeks of life; the embryonic/fetal (BASM) form may be evident at birth without a preceding period of normal-colored stool, whereas the perinatal/isolated form classically has a jaundice-free interval before onset.
- **Severity/progression:** Uniformly progressive if untreated — obliterative fibrosis of the biliary tree advances to biliary cirrhosis; rate varies, but historically <10% survival to age 3 without surgical intervention.
- **Frequency among affected individuals:** The core triad (jaundice, acholic stool, dark urine, conjugated hyperbilirubinemia) is present in essentially 100% of cases by definition; BASM-associated anomalies occur in an estimated 10–20% of the total BA population.
- **Quality of life impact:** Even with successful Kasai surgery, many children experience chronic pruritus, growth impairment, recurrent cholangitis, and portal hypertension; those progressing to transplant face lifelong immunosuppression-related morbidity. Specific standardized QOL instrument data (EQ-5D/SF-36) for BA were not surfaced in this search and represent a gap.

Sources: [AASLD Pathology Pearls](https://www.aasld.org/liver-fellow-network/core-series/pathology-pearls/biliary-atresia), [PMC9297290](https://pmc.ncbi.nlm.nih.gov/articles/PMC9297290/), [PMC8658215](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8658215/)

---

## 4. Genetic/Molecular Information

**Note:** Unlike a classic monogenic Mendelian disease, BA has no single OMIM-cataloged causal gene; genetic contributions are best characterized as **susceptibility loci** (isolated form) and **candidate causal genes for the BASM subtype** (see §2). No pathogenic variant is required for diagnosis; genetic testing is used mainly to detect syndromic/laterality-associated variants or to exclude genetic cholestasis mimics (e.g., Alagille syndrome, PFIC).

- **GWAS susceptibility genes (isolated BA):** *ADD3* (hgnc:238), *GPC1* (hgnc:4451), *ARF6*, *EFEMP1* — common variants, modest effect sizes, functionally validated in zebrafish knockdown models showing impaired bile excretion/intrahepatic biliary network formation ([PMC7202506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7202506/); [PMC6107291](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6107291/)).
- **BASM candidate genes:** *PKD1L1* (biallelic, likely recessive-acting rare variants; hgnc:9820), *CFC1* (heterozygous, laterality; hgnc:1904).
- **De novo/rare candidate genes (heterogeneous, not fully replicated):** *STIP1*, *REV1* (HSP90 co-chaperone pathway), *AMER1*, *INVS*, *OCRL*, *PCNT*, *KIF3B*, *TTC17*.
- **Structural variation:** candidate CNV region at 2q37.3.
- **Somatic vs. germline:** All reported variants are germline; no somatic mosaicism mechanism has been established, though maternal microchimerism (transfer of maternal cells/DNA to the fetus) has been proposed as a non-Mendelian contributor to phenotypic heterogeneity ([PMC9539747](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9539747/)).
- **Functional consequences:** Susceptibility variants are largely regulatory/eQTL in nature (ADD3, GPC1) rather than classic loss-of-function coding lesions; PKD1L1/CFC1 variants act through disrupted ciliary/laterality signaling.
- **Allele frequency in population databases:** Specific gnomAD allele frequencies for the implicated SNPs were not retrieved in this search — recommend direct gnomAD/dbSNP lookup for rs17095355 (ADD3) and rs6707262/rs6750380 (GPC1) before curation.
- **Epigenetics:** Twin discordance (97% discordant, over half monozygotic) strongly implicates epigenetic and/or environmental-timing factors rather than pure genetic determinism; no specific DNA methylation signature for BA was identified in this search (gap — worth checking DiseaseMeth/Roadmap Epigenomics directly).
- **Chromosomal abnormalities:** No recurrent aneuploidy or translocation syndrome is a major cause of isolated BA; BA has been reported in association with trisomy 18 and other syndromic states in isolated case reports, but this is not a primary etiologic pathway.

Suggested ontology terms: **GO:0007368** (determination of left/right symmetry) for laterality-gene mechanism; **HGNC** gene IDs above; **MONDO:0008867** disease term; consider **GENO:0000845** (susceptibility to) relationship type for ADD3/GPC1/EFEMP1/ARF6 rather than a strict causal relationship.

Sources: [PMC9277099](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9277099/), [PMC6579603](https://pmc.ncbi.nlm.nih.gov/articles/PMC6579603/), [Nature Sci Rep 2021](https://www.nature.com/articles/s41598-021-01148-y)

---

## 5. Environmental Information

- **Environmental toxin:** Biliatresone (isoflavonoid electrophile, *Dysphania* spp. plants) — causally established in a naturally-occurring livestock (sheep/cattle) BA-like disease during Australian droughts; reactive α-methylene ketone group depletes cellular glutathione (GSH) selectively in extrahepatic cholangiocytes ([Biliatresone – Wikipedia](https://en.wikipedia.org/wiki/Biliatresone); [PMC5251204](https://pmc.ncbi.nlm.nih.gov/articles/PMC5251204/)). No confirmed direct human dietary exposure pathway has been established, but the model strongly supports plausibility of an as-yet-unidentified human environmental toxin.
- **Infectious agents (perinatal triggers):** Rotavirus (particularly rhesus rotavirus, RRV, and human group C rotavirus), reovirus, cytomegalovirus (CMV) — implicated as initiators of the perinatal/isolated form via cholangiocyte infection and secondary autoimmune-like injury (see Mechanism, §6). CMV-associated BA is recognized as a distinct clinical subgroup with different serology and possibly worse prognosis.
- **Maternal infections:** intestinal and genitourinary infections during pregnancy — increased offspring BA risk in case-control data ([PMC10765264](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765264/)).
- **Maternal lifestyle/health factors:** type 2 diabetes mellitus and non-dependent drug abuse increased risk; smoking, advanced maternal age, delivery mode, and singleton/multiple pregnancy showed no significant association ([Pediatr Res 2022](https://www.nature.com/articles/s41390-022-02166-w)).
- **Geography/seasonality:** BA incidence shows marked geographic variation (see §9), and some studies have examined birth-season clustering consistent with a seasonal infectious trigger, though this was not directly confirmed in the sources retrieved here.

Sources: [PMC10997102](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10997102/), [Penn Today](https://penntoday.upenn.edu/news/plant-toxin-causes-biliary-atresia-animal-model-according-penn-study), [PMC10765264](https://pmc.ncbi.nlm.nih.gov/articles/PMC10765264/)

---

## 6. Mechanism / Pathophysiology

BA pathogenesis is best modeled as a **causal chain**: developmental susceptibility → perinatal insult (viral/toxin) → cholangiocyte injury → innate immune activation → adaptive (Th1/Th17) autoimmune-like amplification → progressive fibro-obliteration → cirrhosis/liver failure.

### Upstream: Developmental susceptibility (BASM subtype)
- Disrupted **left-right patterning/ciliary signaling** during early embryogenesis (*CFC1*/NODAL pathway, *PKD1L1* ciliary calcium signaling) causes combined biliary and laterality (splenic, cardiac, situs) malformation. Cholangiocyte primary cilia in BA livers are shortened, disoriented, and reduced in number, implicating ciliary dysfunction directly in bile duct pathogenesis ([ResearchGate PKD1L1](https://www.researchgate.net/publication/330529071_Identification_of_PKD1L1_Gene_Variants_in_Children_with_the_Biliary_Atresia_Splenic_Malformation_Syndrome)).
- Suggested GO term: **GO:0007368** determination of left/right symmetry.

### Trigger: Cholangiocyte injury
- **Viral route (murine RRV model, isolated BA paradigm):** Rhesus rotavirus infects and replicates within neonatal mouse cholangiocytes, producing an obstructive cholangiopathy that closely mirrors human BA; the temporal window of susceptibility to RRV parallels human disease timing ([PMC3700947](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3700947/)). Rotavirus infection of human cholangiocytes in vitro reproduces key features of the murine model.
- **Toxin route (biliatresone model):** The electrophilic toxin binds/depletes reduced glutathione (GSH) selectively in extrahepatic cholangiocytes, inducing **redox stress**, disrupted **protein quality control** (heat-shock chaperone HSP90 pathway — *STIP1*, involving REV1), **microtubule instability**, and altered **Wnt and Hippo signaling** pathways, converging on cholangiocyte cytoskeletal collapse, loss of cell polarity, and lumen obstruction ([Pediatric Research 2024](https://www.nature.com/articles/s41390-024-03335-9); [PMC7200694](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7200694/)).
- Suggested GO terms: **GO:0006749** (glutathione metabolic process), **GO:0016055** (Wnt signaling pathway), **GO:0035329** (Hippo signaling), **GO:0007017** (microtubule-based process).

### Amplification: Innate and adaptive immune injury
- Injured cholangiocytes secrete **IL-1β, IL-6, IL-23**, and multiple chemokines, driving **Th17 commitment** (IL-1β/IL-6) and **sustained Th17 responses** (IL-23) ([Frontiers Immunology — Innate Immunity and Pathogenesis of BA](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2020.00329/full)).
- **Macrophages** are directly targeted by rotavirus and induce neutrophil chemotaxis via **Mip2/Cxcl2** ([PMID:20234283](https://pubmed.ncbi.nlm.nih.gov/20234283/)).
- The liver develops a **T-helper 1 (Th1)-dominant inflammatory profile**, mirrored between human BA liver and RRV-infected mouse liver; **T-bet deficiency attenuates bile duct injury**, and **T-bet⁺/Th1-driven bile duct injury is restrained by regulatory T cells**, indicating a Treg/Th1 balance central to disease severity ([PMC8700492](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8700492/)).
- A **dendritic cell–Th17–macrophage axis** controls cholangiocyte injury and disease progression in both mouse and human BA.
- **B cells** contribute: B-cell-deficient mice are protected from biliary obstruction in the RRV model, implicating a humoral/antibody-mediated component ([PMC3749125](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3749125/)).
- Recent single-cell/spatial transcriptomic work (2022–2025) has resolved the fibrotic immune niche: **intermediate CD14++CD16+ monocytes, scar-associated macrophages, NK T cells, transitional B cells, FCN3+ neutrophils**, and **CD177+ neutrophil activation** are enriched in BA liver, with N-acetylcysteine (NAC) treatment partially reversing this immune dysfunction ([JHEP Reports 2023](https://www.jhep-reports.eu/article/S2589-5559(23)00239-2/fulltext); [PMC9636046](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9636046/)).
- Suggested GO/CL terms: **GO:0042093** (T-helper cell differentiation), **CL:0000899** (Th17 cell), **CL:0000545** (Th1 cell), **CL:0000097** (mast cell)/**CL:0000235** (macrophage), **CL:0000097**.

### Downstream: Structural/cellular consequences
- **Hepatocyte-to-cholangiocyte reprogramming**: single-cell RNA-seq identifies reprogrammed liver cells co-expressing hepatocyte and cholangiocyte markers; upregulated **MMP7, VTCN1, LAMC2** as biliary markers and **KLF5, HNF1B** as biliary transcription factors in BA ([PMC12055120](https://pmc.ncbi.nlm.nih.gov/articles/PMC12055120/)). MMP7 in particular is an emerging serum biomarker.
- Extrahepatic cholangiocyte damage leads to progressive **peribiliary fibrosis**, ductular reaction, and eventual **biliary cirrhosis**, portal hypertension, and hepatic failure — a convergence with the dismech `fibrotic_response` module logic (tissue injury → inflammation → mesenchymal/myofibroblast activation → excessive ECM → organ dysfunction).
- Organoid studies show BA-derived extrahepatic cholangiocyte organoids exhibit increased **ER and oxidative stress**, altered drug metabolism, and cell-polarity changes relative to controls ([bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.05.04.649927v1.full)).

### Anatomical developmental context
The extrahepatic bile ducts (common bile duct, cystic duct, gallbladder) derive from the **pars cystica** of the liver bud, developmentally and transcriptomically distinct from the intrahepatic ducts (pars hepatica); this distinct origin is consistent with BA being fundamentally an extrahepatic-duct disease that can secondarily involve intrahepatic ducts as fibrosis ascends ([PMC8604670](https://pmc.ncbi.nlm.nih.gov/articles/PMC8604670/)).

Suggested overall causal-chain GO/CL/UBERON scaffold for a dismech pathophysiology block:
1. Node: "Perinatal Cholangiocyte Insult" (biological_scale: CELLULAR) — GO:0006749 glutathione metabolic process, viral infection trigger
2. Node: "Innate Immune Activation and Cytokine Release" — CL:0000235 macrophage, GO:0032612 IL-1 production
3. Node: "Th1/Th17-Driven Adaptive Autoimmune Amplification" — CL:0000899 Th17 cell, CL:0000545 Th1 cell
4. Node: "Extrahepatic Bile Duct Fibro-Obliteration" (biological_scale: TISSUE) — conforms_to `fibrotic_response`
5. Node: "Biliary Cirrhosis and Hepatic Failure" (biological_scale: ORGANISM)

Sources: [Nature Reviews Gastro & Hepatology 2015](https://www.nature.com/articles/nrgastro.2015.74), [PMC7273417](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7273417/), [PMC9277099](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9277099/), [PMC7052372](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7052372/)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Extrahepatic bile ducts (common bile duct, common hepatic duct, cystic duct), gallbladder, and liver (progressive secondary intrahepatic ductal and parenchymal involvement).
- **Secondary/complication-related:** Spleen (in BASM — poly-/asplenia), heart (in BASM — situs/structural defects), portal venous system (varices, preduodenal portal vein in BASM), intestine (malrotation in BASM; post-Kasai Roux limb).
- **Body systems:** Primarily hepatobiliary/digestive; secondarily cardiovascular (BASM) and, via chronic cholestasis, the skeletal system (rickets from fat-soluble vitamin D malabsorption) and hematologic system (coagulopathy from vitamin K malabsorption).
- Suggested UBERON: **UBERON:0002394** (extrahepatic bile duct region — verify exact term via OAK), **UBERON:0002110** (gallbladder), **UBERON:0002107** (liver), **UBERON:0002106** (spleen).

**Tissue and cell level:**
- **Cholangiocytes** (biliary epithelial cells) — the primary cellular target; suggested **CL:0000546** or more specifically extrahepatic cholangiocyte if a CL term exists.
- **Peribiliary gland cells** — proposed stem/progenitor niche relevant to biliary regeneration/repair.
- **Portal fibroblasts / hepatic stellate cells → myofibroblasts** — drive the fibrotic response (conforms to `fibrotic_response` module: **CL:0000632** hepatic stellate cell).
- **Hepatocytes** — undergo secondary reprogramming toward a biliary phenotype in advanced disease.
- **Immune infiltrate:** macrophages (CL:0000235), Th1/Th17 CD4+ T cells (CL:0000545/CL:0000899), B cells, NK T cells, neutrophils (including a CD177+ activated subset).

**Subcellular level:**
- Mitochondrial/ER oxidative stress in cholangiocytes (**GO:0005739** mitochondrion, **GO:0005783** endoplasmic reticulum).
- Cytoskeletal/microtubule disruption (**GO:0005874** microtubule).
- Primary cilium abnormalities in cholangiocytes (short, disoriented, reduced in number) — **GO:0005929** cilium.

**Localization:** Disease is centered on the porta hepatis and extrahepatic biliary tree; not classically lateralized, though BASM introduces organ-level laterality anomalies (situs abnormalities) as a distinct phenotypic axis.

Sources: [PMC8604670](https://pmc.ncbi.nlm.nih.gov/articles/PMC8604670/), [PMC7273417](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7273417/)

---

## 8. Temporal Development

- **Onset:** Neonatal, typically manifesting clinically between 2 and 8 weeks of age (perinatal/isolated form, often with an initial jaundice-free interval as physiologic neonatal jaundice resolves and pathologic jaundice supervenes) vs. present at or near birth without a jaundice-free interval (embryonic/fetal/BASM form).
- **Onset pattern:** Subacute-to-insidious in the isolated form; can be apparent congenitally in the BASM/fetal form.
- **Progression / disease stages:** Uniformly progressive fibro-obliterative process — early ductular proliferation and bile plugging → periportal fibrosis → bridging fibrosis → biliary cirrhosis → portal hypertension and hepatic decompensation. Histopathologic staging at the time of Kasai portoenterostomy (degree of fibrosis, Ki67 proliferation index) is prognostically important ([PMC7528526](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7528526/); [PMC11870969](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11870969/)).
- **Progression rate:** Rapid and relentless if untreated — median survival ~8 months, near-100% mortality by 2 years, historical <10% survival to age 3 without intervention ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK537262/)). With Kasai surgery, progression can be substantially slowed or, in a subset, arrested for decades.
- **Disease course pattern:** Progressive; a subset of Kasai-treated patients stabilizes with the native liver, while others continue to progress to transplant despite surgery — course is not relapsing-remitting.
- **Critical period:** Timing of Kasai portoenterostomy is the single most important modifiable variable — earlier surgery (ideally <45–60 days of life, before irreversible cirrhosis sets in) yields substantially better transplant-free survival ([PMID:34854975](https://pubmed.ncbi.nlm.nih.gov/34854975/)).
- **Remission:** No spontaneous remission is described; "remission" in the treated sense means durable native-liver survival with normalized bilirubin after Kasai (jaundice clearance, typically assessed at 3 and 6 months post-op).

Sources: [Western Pediatric Surgery Research Consortium study](https://pubmed.ncbi.nlm.nih.gov/34854975/), [PMC7333324](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7333324/), [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK537262/)

---

## 9. Inheritance and Population

### Epidemiology
- **Geographic variation is marked:** Incidence in Taiwan/Japan is roughly **100–500 per 100,000 live births** (i.e., ~0.12–0.19 per 1,000 in a 1997–2010 Taiwan cohort), versus **5–25 per 100,000** in Europe, and **~0.52–0.71 per 10,000** live births in Western literature broadly ([ScienceDirect — East vs West](https://www.sciencedirect.com/science/article/abs/pii/S1055858620300706)). South Korea reports an incidence of **1.06 per 10,000 live births** ([J Korean Med Sci 2017](https://jkms.org/DOIx.php?id=10.3346%2Fjkms.2017.32.4.656)).
- Orphanet lists overall point prevalence as **1–9 per 100,000**.

### Inheritance pattern
- **Multifactorial / non-Mendelian**, not simple autosomal dominant/recessive — reflected by high twin discordance (97.1% discordant pairs, 55.9% of these monozygotic) ([PMID:32504124](https://pubmed.ncbi.nlm.nih.gov/32504124/); [PMID:2993572](https://pubmed.ncbi.nlm.nih.gov/2993572/)). Suggested HPO inheritance term: **HP:0001426** (multifactorial inheritance) rather than a single Mendelian mode; syndromic BASM cases with biallelic PKD1L1 variants suggest an autosomal recessive contribution to that specific subtype.
- **Penetrance/expressivity:** Because BA is not classically monogenic, formal penetrance estimates for individual variants (e.g., ADD3, GPC1) are not established; these are population susceptibility alleles with small effect sizes, not highly penetrant Mendelian variants.
- **Familial recurrence:** Rare; >30 multiplex families reported worldwide, suggesting low but non-zero recurrence risk, likely elevated specifically for the genetically-driven syndromic (BASM) subtype.
- **Founder effects/consanguinity:** Not prominently reported in the literature surveyed here (gap).
- **Maternal microchimerism:** Proposed as a contributor to sporadic, non-Mendelian phenotypic variability (transfer of maternal cells to the fetus) ([PMC9539747](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9539747/)).

### Population demographics
- **Sex ratio:** Female predominance — adjusted prevalence ratio 1.68 (95% CI 1.33–2.12) for females vs. males ([JPeds 2022](https://www.jpeds.com/article/S0022-3476(22)00288-8/fulltext)).
- **Ethnic/geographic distribution:** Substantially higher incidence in East Asian populations (Taiwan, Japan, Korea, China) than in European or North American populations; French Polynesia and some other populations also show elevated rates. The reasons for this disparity are not fully explained but are hypothesized to involve both genetic background (ADD3/GPC1 allele frequencies differ by ancestry) and environmental exposure differences.
- **Age distribution:** By definition, an infantile-onset disease; no adult-onset form exists (survivors reaching adulthood on native liver represent successfully treated childhood-onset cases, not new adult presentations).

Sources: [PubMed 35364097](https://pubmed.ncbi.nlm.nih.gov/35364097/), [PMC9339784 — Saudi national study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9339784/), [J Korean Med Sci](https://jkms.org/DOIx.php?id=10.3346%2Fjkms.2017.32.4.656)

---

## 10. Diagnostics

### Clinical/laboratory tests
- **Liver function tests:** conjugated (direct) hyperbilirubinemia with markedly **elevated serum gamma-glutamyl transferase (GGT)** — a key discriminating lab clue from other neonatal cholestatic conditions ([Geeky Medics](https://geekymedics.com/biliary-atresia/)).
- **Fractionated bilirubin** is under investigation as a US newborn-screening strategy (measuring direct/conjugated bilirubin fraction abnormal in BA newborns).
- Additional biomarkers under study: **urine sulfated bile acids (USBA)**, serum bile acids, serum free carnitine, and serum **MMP7** (matrix metalloproteinase 7, emerging from single-cell transcriptomic work as a biliary-injury marker).

### Imaging
- **Abdominal ultrasound — "triangular cord" sign:** a triangular/tubular echogenic density cranial to the portal vein bifurcation, representing the fibrotic biliary remnant; **85% sensitivity, 100% specificity** in the original comparative study, alongside gallbladder abnormalities (absent, atretic, or non-contractile gallbladder) as the other key sonographic feature ([PMID:9396524](https://pubmed.ncbi.nlm.nih.gov/9396524/); [AJR meta-analysis](https://www.ajronline.org/doi/10.2214/AJR.15.15336)).
- **Hepatobiliary scintigraphy (Tc-99m-DISIDA / HIDA scan):** absence of tracer excretion into the gut is **96% sensitive but only 35% specific** (many non-BA cholestatic conditions also fail to excrete); presence of gut excretion effectively excludes BA.
- **Liver needle biopsy:** shows bile duct proliferation, bile plugs, and portal fibrosis; **90% sensitivity, 96% specificity** in comparative series — used when ultrasound/scintigraphy are equivocal.
- **Diagnostic algorithm:** if the triangular cord sign is present, proceed directly to exploratory laparotomy/intraoperative cholangiogram without further workup; if absent, proceed to scintigraphy, reserving liver biopsy for infants with no tracer excretion ([PMID:9396524](https://pubmed.ncbi.nlm.nih.gov/9396524/)).
- **Intraoperative cholangiogram** remains the definitive confirmatory test, demonstrating non-patency of the extrahepatic biliary tree.

### Genetic testing
- Not part of routine BA diagnosis (BA is a structural/inflammatory diagnosis, not primarily a molecular one), but targeted or exome sequencing is used **to evaluate syndromic (BASM) cases** for laterality-gene variants (*PKD1L1*, *CFC1*) and to **exclude genetic mimics** of neonatal cholestasis such as Alagille syndrome (*JAG1*/*NOTCH2*), progressive familial intrahepatic cholestasis (PFIC, *ATP8B1/ABCB11/ABCB4*), alpha-1-antitrypsin deficiency, and citrin deficiency.

### Differential diagnosis
Neonatal hepatitis, Alagille syndrome, choledochal cyst, PFIC, alpha-1-antitrypsin deficiency, inspissated bile/mucous plug syndrome, total parenteral nutrition-associated cholestasis, and various inborn errors of metabolism presenting with cholestasis.

### Screening (asymptomatic detection)
- **Infant Stool Color Card (ISCC)** is the most widely used population-based screening method (parent-administered, comparing stool color to a reference card during the first month of life). In Taiwan's national program: **sensitivity 89.7%, specificity 99.9%, PPV 28.6%**; implementation was associated with earlier Kasai surgery (66% vs. 49% performed <60 days of age) and improved 3-year jaundice-free survival (57% vs. 31.5%) versus historical controls ([PMC4998398](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4998398/)).
- A 14-year nationwide Taiwan cohort further showed stool color card screening **reduced hospitalization rates and mortality** ([PMC4998398](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4998398/)).

Sources: [AAP Pediatrics — Newborn Screening for BA](https://publications.aap.org/pediatrics/article/136/6/e1663/33927/Newborn-Screening-for-Biliary-Atresia), [PMC11357077](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11357077/), [PubMed 34817690](https://pubmed.ncbi.nlm.nih.gov/34817690/)

---

## 11. Outcome/Prognosis

### Survival and mortality
- **Untreated:** near-100% mortality by 2 years of age; median survival ~8 months; historical <10% survival to age 3 ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK537262/)).
- **After Kasai portoenterostomy:** anicteric transplant-free survival rates are approximately **60% at 5 years** and **50% at 20 years**; roughly **40.8%** of a cohort of 223 infants survived to a defined endpoint with native liver in one series; **25–35%** of Kasai patients survive >10 years without transplant in broader estimates ([PMC8160257](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8160257/); [Nature Sci Rep — Kasai follow-up](https://www.nature.com/articles/s41598-021-90860-w)).
- **Jaundice clearance:** >66% of patients become jaundice-free by 1 year post-Kasai in some series; only ~40–70% achieve jaundice clearance overall, and those who fail typically progress rapidly to transplant.
- **Liver transplantation outcomes:** patient/graft survival rates of **95.8%/91.0%** over 20 years in one high-volume single-center study; more broadly, 5-/10-year graft survival ranges **68–98%** and **71–90%** respectively across centers; a separate 20-year single-center cohort reported a **63.8% cumulative 20-year graft survival** ([Frontiers Pediatrics 2023](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2023.1242009/full); [PMC10940458](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10940458/)).

### Morbidity
- **Complications post-Kasai:** recurrent bacterial cholangitis (common and can precipitate acute decompensation), progressive portal hypertension with variceal bleeding, pruritus, growth failure, and fat-soluble vitamin deficiencies.
- **Complications post-transplant:** post-transplant lymphoproliferative disease (most frequent in the first 1–2 years of immunosuppression), and steadily increasing incidence of cholangitis and rejection over time ([Frontiers Pediatrics 2023](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2023.1242009/full)).
- BA remains the **leading indication for pediatric liver transplantation** in the US and worldwide.

### Prognostic factors
- **Age at Kasai surgery** — earlier surgery (ideally before 45–60 days of life) associated with significantly better transplant-free survival; performance at high-volume/tertiary centers also improves outcomes ([PMID:34854975](https://pubmed.ncbi.nlm.nih.gov/34854975/)).
- **Degree of liver fibrosis/cirrhosis at time of Kasai** (histopathologic staging) predicts subsequent cirrhosis progression and survival ([PMC7333324](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7333324/)).
- **Ki67 proliferation index** at the time of Kasai has been evaluated as a prognostic biomarker ([PMC7528526](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7528526/)).
- **Postoperative intestinal obstruction** after Kasai impedes biliary excretion and predisposes to subsequent transplantation ([PMC7847427](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7847427/)).
- CMV-associated BA and BASM-syndromic BA are generally associated with worse Kasai response/outcomes than isolated, non-CMV BA (a recurring theme across the phenotype-heterogeneity literature, though effect sizes vary by cohort).

Sources: [Escholarship UCSD](https://escholarship.org/content/qt78z1k348/qt78z1k348.pdf), [medRxiv Kasai prediction cohort](https://www.medrxiv.org/content/10.1101/2022.10.06.22279593.full.pdf), [ScienceDirect — long-term native liver outcomes](https://www.sciencedirect.com/science/article/pii/S1521691821000445)

---

## 12. Treatment

### Surgical (primary/definitive)
- **Kasai hepatoportoenterostomy** — the standard first-line surgical procedure; excises the fibrotic extrahepatic biliary remnant and anastomoses a Roux-en-Y jejunal limb directly to the porta hepatis to restore bile drainage from residual microscopic ductules. Suggested NCIT term: **NCIT:C154430** or a specific hepatoportoenterostomy procedure term (verify exact NCIT code via OAK); more broadly **NCIT:C15329** (Surgical Procedure).
- **Liver transplantation** — reserved for Kasai failure (persistent jaundice), progressive cirrhosis/liver failure, or recurrent decompensating cholangitis; both living-donor and deceased-donor transplantation are used; BA is the leading pediatric indication for liver transplant. Suggested NCIT term: **NCIT:C15289** (Organ Transplantation).

### Pharmacotherapy / adjuvant medical therapy
- **Ursodeoxycholic acid (UDCA)** — choleretic agent, widely used adjunctively post-Kasai to promote bile flow, though robust RCT evidence specific to BA outcomes was not directly retrieved in this search (commonly used based on extrapolation from other cholestatic diseases; NCIT drug/agent term applicable under Pharmacotherapy **NCIT:C15986** with CHEBI ursodeoxycholic acid as therapeutic_agent).
- **Corticosteroids (post-Kasai adjuvant):** The **START trial** (Steroids in Biliary Atresia Randomized Trial) — multicenter, double-blind RCT, 140 infants, IV methylprednisolone (4 mg/kg/day × 2 weeks) then oral prednisolone (2 mg/kg/day × 2 weeks, tapered over 9 weeks) vs. placebo, initiated within 72 hours of Kasai. **Primary result: no statistically significant benefit** in the overall cohort (49% vs. 59% jaundice clearance at 6 months, direction not favoring steroids significantly); a subgroup of younger infants showed a trend toward increased jaundice clearance (71.8%) that did not reach significance ([JAMA 2014](https://jamanetwork.com/journals/jama/fullarticle/1866094); [NIDDK repository](https://repository.niddk.nih.gov/study/98)). Corticosteroid use post-Kasai remains controversial/center-dependent.
- **N-acetylcysteine (NAC):** Phase 2 trial of short-term IV NAC (150 mg/kg/day × 7 days, starting 0–24h post-Kasai) targeting normalization of total serum bile acids; mechanistically supported by single-cell RNA-seq data showing NAC partially reverses hepatic immune dysfunction (CD177+ neutrophil activation) in BA liver ([PMC12150978](https://pmc.ncbi.nlm.nih.gov/articles/PMC12150978/); [JHEP Reports 2023](https://www.jhep-reports.eu/article/S2589-5559(23)00239-2/fulltext)).
- **Maralixibat (Livmarli™)** — an oral, minimally-absorbed ileal bile acid transporter (IBAT) inhibitor; FDA-approved for cholestatic pruritus in Alagille syndrome (2021) and PFIC; under late-stage clinical evaluation specifically in BA (compassionate-use case series and formal trials such as NCT04524390, "Evaluation of Maralixibat in Biliary Atresia Response Post-Kasai") with Breakthrough Therapy designation for BA; reduces serum bile acids and pruritus ([Drugs — Maralixibat First Approval](https://link.springer.com/article/10.1007/s40265-021-01649-0); [Frontiers Pediatrics — Real-World Use of Maralixibat in BA](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2026.1858862/abstract)). Suggested therapeutic_modality: SMALL_MOLECULE; treatment_term Pharmacotherapy; therapeutic_agent maralixibat (verify NCIT/CHEBI code).
- **Fat-soluble vitamin supplementation** (A, D, E, K) — supportive care for malabsorption due to cholestasis.
- **Prophylactic antibiotics** — commonly used post-Kasai to reduce cholangitis risk (center-dependent protocols).

### Emerging / experimental
- Antifibrotic agents, additional bile-acid modulators, and regenerative approaches are described as an emerging pipeline as of 2025, per industry pipeline analyses (early-stage; specific compounds/trial identifiers were not detailed in the sources retrieved) ([OpenPR — Biliary Atresia Pipeline Insight 2025](https://www.openpr.com/news/4137295/biliary-atresia-pipeline-insight-2025-emerging-regenerative)).
- Gene expression signature-guided identification of repurposable therapeutic agents has been explored computationally but is not yet in clinical use.

### Treatment outcomes / adverse events
- Corticosteroids: no consistent significant efficacy signal in the definitive RCT; risk of steroid-related adverse effects (infection, growth suppression) must be weighed.
- NAC: generally well-tolerated antioxidant; efficacy data still maturing (Phase 2).
- Maralixibat: primarily studied for pruritus/bile-acid reduction rather than as disease-modifying for the biliary obstruction itself; diarrhea is a common adverse effect of IBAT inhibitors as a class.
- Post-transplant immunosuppression carries standard risks (infection, PTLD, rejection).

### Treatment strategy
Standard algorithm: **early diagnosis (ideally via stool-color screening) → prompt Kasai hepatoportoenterostomy (<45–60 days of age) → adjuvant medical management (antibiotics, choleretics, nutritional/vitamin support, investigational NAC/steroids per center protocol) → surveillance for jaundice clearance and cholangitis → liver transplantation if Kasai fails or cirrhosis/portal hypertension progresses.**

Sources: [Translational Pediatrics — Adjuvant treatments for BA](https://tp.amegroups.org/article/view/42311/html), [PMC7347763](https://pmc.ncbi.nlm.nih.gov/articles/PMC7347763/), [Frontiers Pediatrics — Current and emerging adjuvant therapies](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2022.1007813/full)

---

## 13. Prevention

- **Primary prevention:** No established method to prevent the underlying disease process, since the precise causal environmental trigger(s) in humans (analogous to biliatresone in livestock, or a specific human viral strain) remain unconfirmed. No vaccine or prophylactic intervention exists.
- **Secondary prevention (early detection, the dominant prevention strategy in practice):** **Universal newborn screening via the infant stool color card** is the principal population-based strategy, validated most extensively in Taiwan, with adoption in Japan, parts of Europe (e.g., Switzerland), Canada (Ontario Newborn Screening), and pilot programs elsewhere. Screening enables earlier Kasai surgery and improved transplant-free survival ([PMC4998398](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4998398/); [Newborn Screening Ontario](https://www.newbornscreening.on.ca/en/screening/types-of-screening/biliary-atresia/)).
- Alternative/complementary screening strategies under investigation: **fractionated (direct) bilirubin** measurement in the newborn period, urine sulfated bile acids, serum bile acids, and serum free carnitine ([PMC11357077](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11357077/)).
- **Tertiary prevention:** Prompt Kasai surgery itself functions as tertiary prevention against progression to end-stage liver disease; post-Kasai prophylactic antibiotics aim to prevent cholangitis-driven decompensation; nutritional/vitamin support prevents secondary complications of cholestasis (rickets, coagulopathy, growth failure).
- **Genetic counseling:** Given the largely sporadic, multifactorial inheritance and high twin discordance, formal genetic counseling protocols for recurrence risk are not well standardized, though counseling may be offered for the syndromic BASM subtype where recessive contributions (e.g., PKD1L1) are more plausible.
- **Public health / environmental interventions:** No specific environmental intervention (analogous to removing Dysphania plants from livestock pasture) has been identified or implemented for human BA prevention, reflecting the unresolved human etiologic trigger.

Sources: [AAP Pediatrics](https://publications.aap.org/pediatrics/article/136/6/e1663/33927/Newborn-Screening-for-Biliary-Atresia), [PMC4998398](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4998398/)

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Naturally occurring BA-like disease has been documented in **sheep** (*Ovis aries*, NCBITaxon:9940) and **cattle** (*Bos taurus*, NCBITaxon:9913) during Australian drought conditions, causally linked to grazing on *Dysphania* spp. plants (the source of biliatresone) ([Penn Today](https://penntoday.upenn.edu/news/plant-toxin-causes-biliary-atresia-animal-model-according-penn-study); [ScienceDirect — Biliary atresia: the animal models](https://www.sciencedirect.com/science/article/abs/pii/S1055858612000273)). Sporadic case reports also describe BA or BA-like biliary obstruction in **foals, dogs, and calves** ([PMC9324346 — "Biliary Atresia Animal Models: Is the Needle in a Haystack?"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9324346/)).
- **Veterinary relevance:** The lamb outbreaks were the key discovery that led to identification of biliatresone and its mechanism, making veterinary field observation directly foundational to human BA mechanistic research — an unusually direct comparative-medicine translation.
- **OMIA:** A dedicated OMIA entry specific to biliary atresia (as distinct from anal/atresia ani, OMIA:000083) was not identified in this search; this appears to be a database coverage gap rather than an absence of the phenotype in animals.
- **Comparative biology:** The zebrafish (*Danio rerio*, NCBITaxon:7955) biliatresone model demonstrates conserved susceptibility of extrahepatic cholangiocytes across vertebrate species, and the murine RRV model demonstrates conserved rotavirus-cholangiocyte tropism and Th1/Th17 immune injury pathways, supporting deep evolutionary conservation of both the toxin-susceptibility and immune-injury arms of the mechanism.
- **Transmission/zoonotic potential:** Not applicable — BA is not an infectious/transmissible disease of humans in the classic zoonotic sense; the shared susceptibility across species is due to convergent developmental/toxicologic vulnerability of extrahepatic cholangiocytes, not cross-species pathogen transmission. Rotavirus itself is zoonotically and cross-species relevant as a pathogen family, but RRV-induced murine BA is a laboratory disease model, not natural cross-species BA transmission.

Sources: [PMC9324346](https://pmc.ncbi.nlm.nih.gov/articles/PMC9324346/), [PMID:22800971](https://pubmed.ncbi.nlm.nih.gov/22800971/)

---

## 15. Model Organisms

### Zebrafish (*Danio rerio*)
- **Biliatresone toxic-injury model:** Larval zebrafish exposed to biliatresone develop selective destruction of the extrahepatic biliary tree, closely recapitulating human/livestock BA; toxicity is determined by **glutathione antioxidant pathway activity/reserve** ([PMC5251204](https://pmc.ncbi.nlm.nih.gov/articles/PMC5251204/)), and involves **Wnt, Hippo, and microtubule pathway disruption** ([Pediatric Research 2024](https://www.nature.com/articles/s41390-024-03335-9)). Genetic modifiers (e.g., *STIP1/REV1* pathway disruption) alter biliatresone susceptibility in this model, linking the toxin model directly to human WES candidate genes.
- **GWAS-gene knockdown models:** Morpholino/CRISPR knockdown of *ADD3*, *GPC1*, and related susceptibility genes impairs bile excretion and intrahepatic biliary network formation, functionally validating human GWAS hits ([PMC7202506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7202506/)).
- ***pkd1l1* loss-of-function zebrafish:** recapitulates biliary defects relevant to BASM syndrome, directly linking a human BASM candidate gene to a ciliary/biliary phenotype ([PMC10581383](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10581383/)).
- **Strengths:** rapid, scalable, optically transparent for live imaging of biliary tree development; excellent for genetic-modifier and chemical-toxin screening.
- **Limitations:** larval zebrafish biliary anatomy and immune system differ substantially from mammalian/human systems; does not model the adaptive Th1/Th17 autoimmune-injury arm well.

### Mouse (*Mus musculus*)
- **Rhesus rotavirus (RRV)-induced murine BA model:** the dominant immune-mediated/infectious model; neonatal mice infected with RRV develop an obstructive cholangiopathy mirroring human isolated BA, including rotavirus replication within cholangiocytes with strict temporal dependence on neonatal age at infection ([PMC3700947](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3700947/)), macrophage targeting and Mip2/Cxcl2-driven neutrophil chemotaxis ([PMID:20234283](https://pubmed.ncbi.nlm.nih.gov/20234283/)), B-cell dependence (B-cell-deficient mice protected) ([PMC3749125](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3749125/)), T-bet/Th1-dependent bile duct injury restrained by regulatory T cells ([PMC8700492](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8700492/)), and a dendritic cell–Th17–macrophage disease-progression axis. A recent study further defined specific rhesus-rotavirus capsid-protein binding sites dictating the endocytosis route that induces this model ([PMC11687966](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11687966/)).
- **Biliatresone-induced murine model:** the synthetic toxin also causes BA in mice, including a low-dose prenatal exposure paradigm in pregnant mice producing **subclinical biliary disease in offspring** — modeling a spectrum of neonatal injury severity relevant to the "environmental hit during pregnancy" human hypothesis ([Lab Investigation 2020](https://www.nature.com/articles/s41374-020-0467-7); [PMC10997102](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10997102/)).
- **Strengths:** recapitulates the full innate + adaptive immune injury cascade and postnatal obstructive fibrosis; the field's primary model for immunopathogenesis and immunomodulatory drug testing.
- **Limitations:** RRV is not the confirmed human causal agent (human rotavirus/other viruses are the presumed but unconfirmed human trigger); model requires precise neonatal-age infection timing, limiting some translational aspects.

### Human iPSC-derived organoids / primary cholangiocyte cultures
- Human BA extrahepatic cholangiocyte organoids show increased ER/oxidative stress, altered drug metabolism, and cell-polarity changes relative to controls, and are being used to test genetic modifiers of biliatresone toxicity identified in zebrafish (e.g., HSP90/STIP1 pathway) ([bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.05.04.649927v1.full); [PMC10974618 — biliatresone effects on human liver organoids](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10974618/)).
- **Applications:** direct human-cell validation bridging zebrafish/mouse mechanistic findings to human biology; useful for drug screening (e.g., NAC, glutathione-repletion strategies).

### Naturally occurring large-animal models (sheep, cattle)
- Field-derived, non-induced natural disease model that originally identified biliatresone; valuable for toxin discovery but not amenable to routine laboratory-scale genetic manipulation.

### Resource databases
ZFIN (zebrafish), MGI (mouse), IMSR (mouse strain repository) are the relevant model-organism databases for locating specific BA-model alleles/lines; no dedicated BA entries were directly retrieved from these databases in this search (recommend direct query for specific allele/strain nomenclature during curation).

Sources: [PMC9324346](https://pmc.ncbi.nlm.nih.gov/articles/PMC9324346/), [PMC3700947](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3700947/), [Nature Lab Investigation 2020](https://www.nature.com/articles/s41374-020-0467-7)

---

## Summary Table: Suggested Ontology Terms for KB Curation

| Category | Term ID (verify via OAK before use) | Label |
|---|---|---|
| Disease | MONDO:0008867 | biliary atresia |
| Phenotype | HP:0000952 | Jaundice |
| Phenotype | HP:0002240 | Hepatomegaly |
| Phenotype | HP:0001394 | Cirrhosis |
| Phenotype | HP:0001541 | Ascites |
| Phenotype | HP:0001744 | Splenomegaly |
| Phenotype (BASM) | HP:0003363 | Abnormal situs |
| Gene | hgnc:238 | ADD3 |
| Gene | hgnc:4451 | GPC1 |
| Gene | hgnc:9820 | PKD1L1 |
| Gene | hgnc:1904 | CFC1 |
| Cell type | CL:0000899 | Th17 cell |
| Cell type | CL:0000545 | Th1 cell |
| Cell type | CL:0000632 | hepatic stellate cell |
| Cell type | CL:0000235 | macrophage |
| GO Process | GO:0006749 | glutathione metabolic process |
| GO Process | GO:0016055 | Wnt signaling pathway |
| GO Process | GO:0007368 | determination of left/right symmetry |
| Anatomy | UBERON:0002107 | liver |
| Anatomy | UBERON:0002110 | gallbladder |
| Treatment | NCIT:C15289 | Organ Transplantation |
| Treatment | NCIT:C15329 | Surgical Procedure (Kasai) |
| Treatment | NCIT:C15986 | Pharmacotherapy (steroids, NAC, maralixibat, UDCA) |
| Model organism taxon | NCBITaxon:7955 | Danio rerio |
| Model organism taxon | NCBITaxon:10090 | Mus musculus |

*(All term/label pairs above require verification against the live ontology via OAK before committing to a dismech entry, per repository policy — this report is a research input, not pre-validated curation content.)*

---

## Key Evidence Gaps Identified
1. No confirmed specific human environmental toxin analogous to biliatresone.
2. No systematic gnomAD/population allele-frequency data compiled here for ADD3/GPC1 risk SNPs.
3. No specific DNA methylation/epigenetic signature study for BA identified despite strong indirect evidence (twin discordance) for an epigenetic contribution.
4. No standardized quality-of-life instrument (EQ-5D/SF-36/PedsQL) data specific to BA surfaced in this search.
5. Genetic testing panels/GTR-specific BA gene panel composition not directly retrieved — recommend direct GTR query during curation.
6. No dedicated OMIA species-specific entry located for the sheep/cattle BA-like disease despite well-documented field reports.