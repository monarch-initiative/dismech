---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-26T13:16:53.345076'
end_time: '2026-07-26T13:22:08.259970'
duration_seconds: 314.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Abdominal Aortic Aneurysm
  mondo_id: MONDO:0005350
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
  web_search_requests: 21
  num_turns: 23
  total_cost_usd: 1.8408520999999998
  session_id: f9a4f8a6-559e-5875-b202-2cc5a4e70210
  stop_reason: end_turn
citation_count: 47
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Abdominal Aortic Aneurysm
- **MONDO ID:** MONDO:0005350 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Abdominal Aortic Aneurysm** covering all of the
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

# Abdominal Aortic Aneurysm (AAA): Comprehensive Research Report

## 1. Disease Information

**Overview:** Abdominal aortic aneurysm (AAA) is a permanent, localized dilatation of the infrarenal (and occasionally suprarenal/juxtarenal) abdominal aorta to a transverse diameter ≥3.0 cm (or ≥1.5x the expected normal diameter), representing progressive degeneration of all three layers of the aortic wall (intima, media, adventitia) that can culminate in aortic rupture. It is a degenerative pathology of the infrarenal aortic segment characterized by progressive dilation and, in advanced cases, catastrophic rupture with high mortality ([PMC10354862](https://pmc.ncbi.nlm.nih.gov/articles/PMC10354862/)).

**Key identifiers:**
- **MONDO:** MONDO:0005350 (abdominal aortic aneurysm); familial forms MONDO:0024521 and related OMIM entries
- **OMIM:** #100070 (AORTIC ANEURYSM, FAMILIAL ABDOMINAL, 1; AAA1, chromosome 19 locus); #611891 (AAA3); related loci AAA2 and others ([OMIM 100070](https://omim.org/entry/100070), [OMIM 611891](https://www.omim.org/entry/611891))
- **ICD-10:** I71.4 (abdominal aortic aneurysm, without rupture); I71.3 (ruptured abdominal aortic aneurysm)
- **ICD-11:** BD51 (Aneurysm of abdominal aorta)
- **MeSH:** D000783 (Aortic Aneurysm, Abdominal)
- **Orphanet:** Familial abdominal aortic aneurysm is catalogued as a rare disease entity distinct from sporadic/degenerative AAA, which is common and not itself an Orphanet rare-disease designation.

**Synonyms/alternative names:** AAA; infrarenal aortic aneurysm; aortic ectasia (precursor/milder dilation); "triple A."

**Data provenance:** Most epidemiological and genetic knowledge derives from **aggregated, disease-level resources** — national/regional ultrasound screening programs (e.g., UK NAAASP, Scandinavian registries), large biobank GWAS (UK Biobank, Million Veteran Program, FinnGen), vascular surgery registries (VASCUNET, VQI), and meta-analyses — rather than individual EHR chart review, though large single-institution EHR-derived case-control studies (e.g., Danish and Swedish national registries) also contribute substantially.

---

## 2. Etiology

### Disease Causal Factors
AAA is fundamentally a **multifactorial degenerative disease** arising from the interaction of hemodynamic wall stress, chronic transmural inflammation, extracellular matrix (ECM) proteolysis, oxidative stress, and vascular smooth muscle cell (VSMC) loss, occurring on a background of genetic susceptibility ([PMC10354862](https://pmc.ncbi.nlm.nih.gov/articles/PMC10354862/)). A minority of cases are monogenic, arising from heritable connective-tissue disorders (Marfan syndrome, Loeys-Dietz syndrome, vascular Ehlers-Danlos syndrome) or are secondary to infection (mycotic aneurysm) or autoimmune/IgG4-related periaortitis (inflammatory AAA).

### Genetic Risk Factors
- **Familial clustering:** First-degree relatives of AAA patients have markedly increased risk; family history is itself an established clinical risk factor incorporated into USPSTF screening criteria.
- **Linkage loci:** The AAA1 locus on chromosome 19 (OMIM #100070) was among the first mapped familial susceptibility regions ([PMC3037298](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3037298/)).
- **GWAS-confirmed common variants (candidate-gene and genome-wide, meta-analysis–supported):** *CDKN2BAS* (9p21, rs10757278), *DAB2IP*, *LRP1*, *SORT1* (rs599839), *IL6R* (rs2228145), *LPA* (rs3798220), *MMP3*, *AGTR1*, *ACE*, *APOA1* — implicating inflammation, lipid metabolism, and ECM remodeling pathways ([PMC10608078](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10608078/); note a 2015 EJVES systematic review found most candidate-gene associations were **not robustly replicated** — "Abdominal Aortic Aneurysm Genetic Associations: Mostly False?" [PMID cited via EJVES](https://www.ejves.com/article/S1078-5884(15)00681-4/fulltext)).
- **Large-scale multi-ancestry GWAS meta-analysis (Roychowdhury et al., *Nat Genet* 2023, 55:1831-1842):** identified **141 independent associations, including 97 previously unreported loci**, across 39,221 cases and 1,086,107 controls, implicating lipid metabolism, vascular development/remodeling, ECM dysregulation, and inflammation, and highlighting ***PCSK9* as a druggable target** ([Nature Genetics](https://www.nature.com/articles/s41588-023-01510-y); [PMC10632148](https://ncbi.nlm.nih.gov/pmc/articles/PMC10632148)).
- **Shared genetic architecture with cardiometabolic traits:** significant genetic correlation with 21 cardiometabolic traits including coronary artery disease, hypertension, and lipid traits, with cholesterol metabolism and inflammation as the most prominent shared pathways ([Nat Commun 2024](https://www.nature.com/articles/s41467-024-49921-7); [PMC11226445](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11226445/)).
- **Monogenic/syndromic causes:** *FBN1* (Marfan syndrome), *TGFBR1/TGFBR2* (Loeys-Dietz; also independently associated with AAA in the Dutch population), *COL3A1* (vascular Ehlers-Danlos — causes ~2% of familial AAA cases), *SMAD3*, *TGFB2/TGFB3*, *ACTA2*, *MYH11*, *LOX*, *FBLN4/EFEMP2* — genes essential for aortic wall ECM integrity and TGF-β pathway regulation ([PMC10454608](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10454608/); [PMC3557640](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3557640/)).
- **Familial inheritance pattern:** studies of AAA kindreds found ~72% consistent with autosomal recessive-appearing aggregation and ~25% autosomal dominant with incomplete penetrance, though sporadic AAA overall behaves as a complex/polygenic trait.

### Environmental Risk Factors
- **Smoking** is the single strongest modifiable risk factor: current smokers OR ≈3.28, former smokers OR ≈1.86 versus never-smokers; women who smoke have ~15-fold increased risk versus ~7-fold in men ([PMC6313801](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6313801/)).
- **Age** (risk rises sharply after 65), **male sex** (4–6:1 prevalence ratio versus women), **family history**, **hypertension**, **hyperlipidemia/atherosclerosis**, **COPD**, **Caucasian ancestry** (higher risk than Black, Hispanic, or Asian populations in most cohorts).
- **Protective factor:** **Diabetes mellitus** is paradoxically and consistently associated with *reduced* AAA risk and slower growth in observational studies — an unusual inverse relationship among cardiovascular risk factors, hypothesized to relate to glycation-related ECM stiffening or metformin exposure.

### Protective Factors
- **Genetic:** Loss-of-function *PCSK9* variants are protective (Mendelian randomization: PCSK9 inhibition proxy OR ≈0.595 for AAA risk); HMGCR inhibition (statins) shows an even stronger protective association (OR ≈0.202) in MR analyses ([PMC11367000](https://pmc.ncbi.nlm.nih.gov/articles/PMC11367000/)).
- **Environmental/lifestyle:** Regular physical activity, Mediterranean-style diet, and smoking cessation reduce risk; statin and ACE-inhibitor/metformin use associate with slower aneurysm growth in observational cohorts ([UK Aneurysm Growth Study, BJS](https://academic.oup.com/bjs/article/111/1/znad375/7459560)).
- **Estrogen signaling** is proposed to be protective in premenopausal women, dampening inflammation, oxidative stress, and proteolysis, contributing to the markedly lower AAA prevalence in women before old age ([PMC12927653](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12927653/)).

### Gene-Environment Interactions
Smoking interacts synergistically with genetic susceptibility (e.g., 9p21/*CDKN2BAS* and lipid-pathway variants) to amplify inflammatory and proteolytic ECM injury; the shared genetic architecture between AAA and cardiometabolic traits (LDL-cholesterol, hypertension) suggests that lifestyle-modifiable atherogenic burden interacts with an individual's polygenic background to determine whether subclinical aortic wall injury progresses to clinically significant aneurysm.

---

## 3. Phenotypes

Most AAA is **asymptomatic** until large or ruptured, which is why population screening exists.

| Phenotype | Type | Onset/Course | Frequency | Suggested HP term |
|---|---|---|---|---|
| Aneurysmal dilation of abdominal aorta (≥3 cm) | Physical/imaging finding | Adult/elderly onset (typically >60y), chronic-progressive | Defining feature | **HP:0004942** (Abdominal aortic aneurysm) |
| Asymptomatic (pre-rupture) | Clinical course | Chronic, often stable for years | Majority (>90% of intact AAAs) | — |
| Pulsatile abdominal mass | Physical sign | Variable, more evident in large AAA | Occasional (low sensitivity in obese patients) | HP:0100490 (Abdominal mass, if used generically) |
| Abdominal pain / back pain | Symptom | Can be episodic (expanding aneurysm) or acute (impending rupture/rupture) | Occasional pre-rupture; near-universal with rupture | HP:0002027 (Abdominal pain), HP:0003418 (Back pain) |
| Hypotension/shock (with rupture) | Clinical sign | Acute | Present in ruptured AAA | HP:0002615 (Hypotension) |
| Aortic dissection | Complication | Acute | Uncommon complication | HP:0002647 (Aortic dissection) |
| Distal embolization ("trash foot," blue toe syndrome) | Complication | Acute/subacute | Uncommon (mural thrombus embolization) | — |
| Aortocaval or aortoenteric fistula | Complication | Acute, rare | Rare | — |
| Retroperitoneal hematoma (with rupture) | Sign | Acute | Present with rupture | — |

**Severity/progression:** Growth is generally silent and gradual (mean 2.2–3 mm/year, size-dependent — 1.3 mm/year for 3 cm aneurysms up to 3.6 mm/year for larger ones), but can accelerate unpredictably ("rapid expanders," >1 cm/year), which itself is an indication for intervention independent of absolute diameter ([PMC10354862](https://pmc.ncbi.nlm.nih.gov/articles/PMC10354862/)).

**Quality of life impact:** Intact, untreated small AAA under surveillance has minimal day-to-day QoL impact beyond surveillance-related anxiety; QoL is substantially affected post-repair (open repair causes greater short-term morbidity/QoL decrement than EVAR, though long-term QoL converges) and is severely impacted after rupture (high mortality, prolonged ICU stay, multi-organ dysfunction in survivors).

---

## 4. Genetic/Molecular Information

**Causal genes for monogenic/familial forms:**
- **FBN1** (fibrillin-1, Marfan syndrome) — aneurysms typically root/thoracic but can extend
- **TGFBR1/TGFBR2** (Loeys-Dietz syndrome) — associated with AAA in Dutch cohort studies; LDS patients have more extensive arterial aneurysms than Marfan
- **COL3A1** (vascular Ehlers-Danlos syndrome, vEDS) — causes ~2% of familial AAA; high rupture risk at smaller diameters
- **SMAD3, TGFB2, TGFB3** — TGF-β pathway aortopathies
- **ACTA2, MYH11, PRKG1, MYLK** — smooth-muscle contractile apparatus genes (more classically associated with familial thoracic aortic aneurysm/dissection, but overlapping phenotypic spectrum)
- **LOX** (lysyl oxidase) — elastin/collagen crosslinking; loss of function causes aneurysms in mouse models and rare human cases
- **FBLN4/EFEMP2** — cutis laxa with arterial tortuosity/aneurysm

**Common (polygenic) risk variants** (see Etiology section for detail): *CDKN2BAS/9p21*, *DAB2IP*, *LRP1*, *SORT1*, *IL6R*, *LPA*, *MMP3*, *AGTR1*, *ACE*, *APOA1*, plus the 97 novel loci from the 2023 Nature Genetics meta-GWAS (Roychowdhury et al.) spanning lipid metabolism, ECM, vascular development, and inflammatory gene programs.

**Variant classification/type:** Monogenic-syndrome variants are typically classified via ACMG/AMP criteria in ClinVar (missense, nonsense, splice-site, and structural variants in *FBN1*/*TGFBR1/2*/*COL3A1*); common AAA-associated GWAS variants are non-coding regulatory SNPs of modest individual effect size, aggregated into polygenic risk scores (PRS) that add predictive value beyond clinical risk factors ([Nature Genetics 2023](https://www.nature.com/articles/s41588-023-01510-y)).

**Somatic vs. germline:** AAA-associated variants are essentially all **germline**; there is no established somatic-mosaicism mechanism analogous to cancer.

**Functional consequences:** Loss-of-function ECM/structural variants (FBN1, COL3A1, LOX, FBLN4) → structural fragility of the aortic wall; TGF-β pathway variants → paradoxically increased (dysregulated) TGF-β signaling promoting medial degeneration (shared mechanism with the dismech `aortopathy_tgfbeta_dysregulation` module); PCSK9 loss-of-function → reduced circulating LDL-cholesterol → reduced atherogenic/inflammatory burden on the aortic wall (protective).

**Epigenetics:** Single-cell ATAC-seq and epigenomic studies show chromatin remodeling in VSMCs accompanying phenotypic switching in aortic aneurysm/dissection, altering accessibility at contractile-gene loci and driving transitions to synthetic/inflammatory/macrophage-like states ("Epigenetic Induction of Smooth Muscle Cell Phenotypic Alterations in Aortic Aneurysms and Dissections," *Circulation* 2024).

**Chromosomal abnormalities:** No characteristic aneuploidy or recurrent structural chromosomal rearrangement is described for sporadic AAA; large deletions/duplications affecting *FBN1*, *COL3A1*, or contiguous-gene syndromes (e.g., Williams syndrome region, *ELN* haploinsufficiency causing supravalvar aortic stenosis/arteriopathy) are relevant to related but distinct arteriopathies rather than typical AAA.

---

## 5. Environmental Information

- **Toxins/pollution:** Cadmium and other heavy-metal exposures have been epidemiologically associated with AAA risk in some cohort studies, plausibly via oxidative stress; air pollution (PM2.5) has emerging associational data with cardiovascular aneurysmal disease broadly.
- **Occupational exposures:** Some studies link occupational noise/vibration and heavy physical labor to elevated blood pressure and cardiovascular strain, an indirect risk contributor; direct occupational-toxin causation for AAA specifically is not well established compared to smoking.
- **Lifestyle factors:** Cigarette smoking (dominant factor, dose- and duration-dependent), hypertension, dyslipidemia, sedentary lifestyle, and obesity are the principal modifiable contributors. Alcohol's relationship is less consistent across studies.
- **Infectious agents (mycotic aneurysm):** A distinct, less common AAA subtype arises from bacteremic seeding of the aortic wall — historically *Salmonella* species and *Staphylococcus aureus* are the classic pathogens for "mycotic" (infected) aortic aneurysms, which behave more aggressively (rapid growth, saccular morphology, higher rupture risk) than degenerative AAA and require antimicrobial therapy plus surgical management ([PMC5949581](https://pmc.ncbi.nlm.nih.gov/articles/PMC5949581/)). Syphilitic (tertiary lues) aortitis historically caused aneurysms, predominantly thoracic, now rare.
- **Autoimmune/IgG4-related periaortitis:** A distinct inflammatory AAA subtype (sometimes termed "inflammatory abdominal aortic aneurysm," IAAA) is associated with IgG4-related disease in roughly half of cases, part of the chronic periaortitis spectrum (which also includes retroperitoneal fibrosis), characterized by IgG4+ plasma cell infiltration, eosinophils, and lymphoid follicles; it must be distinguished from infectious causes via blood cultures/procalcitonin before immunosuppression is initiated ([PMC3595781](https://pmc.ncbi.nlm.nih.gov/articles/PMC3595781/); [PMID 18223321](https://pubmed.ncbi.nlm.nih.gov/18223321/)).

---

## 6. Mechanism / Pathophysiology

### Causal Chain (Degenerative AAA)
**Hemodynamic/mechanical wall stress + genetic susceptibility → chronic transmural inflammation (macrophage/T-cell/B-cell infiltration) → protease-antiprotease imbalance (MMP/TIMP dysregulation) → elastin and collagen degradation → VSMC apoptosis and phenotypic switching → medial degeneration and loss of structural integrity → progressive aortic dilation → biomechanical wall-stress increase (Laplace's law: wall tension ∝ pressure × radius) → further dilation → rupture when wall stress exceeds wall strength.**

- **Molecular pathways:** MMP-2 and MMP-9 (gelatinases) are central proteases that degrade elastin and collagen; an imbalance between MMPs and tissue inhibitors of metalloproteinases (TIMPs) drives unchecked ECM proteolysis ([PMC8880357](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8880357/)). TGF-β signaling is paradoxically **increased** (not decreased) in many aortopathies including syndromic AAA-associated conditions, contributing to maladaptive remodeling (KEGG/Reactome: TGF-beta signaling pathway). Renin-angiotensin system signaling (AT1 receptor, angiotensin II) drives VSMC dysfunction and inflammation and is exploited experimentally to induce aneurysms in mice.
- **Cellular processes:** VSMC apoptosis, VSMC phenotypic switching (contractile → synthetic/proliferative/inflammatory/macrophage-like/mesenchymal-like states — GO:0035909, aorta smooth muscle differentiation, and GO terms for negative regulation of vascular smooth muscle contraction), macrophage polarization (M1 pro-inflammatory dominant), neutrophil extracellular trap (NET) formation within intraluminal thrombus, T-cell (including cytotoxic CD8+) and B-cell/plasma-cell infiltration, oxidative stress (NADPH oxidase-derived ROS), and mitochondrial dysfunction.
- **Protein dysfunction:** Loss of elastin/collagen structural integrity (mechanical); fibrillin-1 microfibril network disruption releasing latent TGF-β (Marfan mechanism); dysfunctional contractile apparatus proteins (ACTA2, MYH11) impairing VSMC mechanosensing.
- **Metabolic changes:** Metabolomic profiling of AAA tissue/plasma shows altered lipid (sphingolipid, phospholipid), amino acid, and energy metabolism signatures, some correlating with aneurysm size ([PMC8401627](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8401627/)); local aortic wall lipid deposition and oxidized LDL contribute to macrophage recruitment (foam-cell-like biology overlapping with the `atherogenesis` module).
- **Immune system involvement:** AAA is now widely conceptualized as a chronic immune-mediated vasculopathy: adaptive immunity (T and B lymphocytes, tertiary lymphoid structures, autoantibodies against aortic wall ECM/elastin) plus innate immunity (macrophages, mast cells, complement activation, neutrophil-derived proteases including neutrophil elastase and MMP-8/9). The intraluminal thrombus (ILT), present in nearly all AAAs, is itself a major site of neutrophil activity, protease release, and hypoxia-driven signaling that perpetuates wall degeneration.
- **Tissue damage mechanisms:** Oxidative stress, chronic hypoxia beneath the ILT, proteolytic ECM degradation, mechanical (biomechanical wall stress) fatigue, and VSMC necrosis/apoptosis converge to progressively thin and weaken the media and adventitia.
- **Biochemical abnormalities:** Elevated circulating and tissue MMP-9, MMP-2, MMP-12; elevated CRP and IL-6; elevated D-dimer (reflecting chronic intraluminal thrombus turnover — see Diagnostics); reduced elastin content and altered collagen cross-linking (LOX-dependent).
- **Single-cell/spatial transcriptomics:** scRNA-seq and spatial transcriptomics of human and murine AAA tissue reveal a VSMC phenotypic landscape including T-cell-like, macrophage-like, and mesenchymal-like modulated VSMC states, two distinct fibroblast subtypes, and a *TREM2+* macrophage subtype implicated in aneurysm-specific niches ([PMC10184349](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10184349/); [PMC12131870](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12131870/); [PMC12406718](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12406718/)). Lineage tracing demonstrates VSMC-to-fibroblast and VSMC-to-macrophage-like transdifferentiation under aortic stress.
- **Sex-specific mechanistic differences:** Estrogen signaling dampens inflammation, oxidative stress, and proteolysis, contributing to lower incidence in premenopausal women; however, once an aneurysm forms, the female aortic wall (differing biomechanical/collagen properties) appears less resistant, explaining higher rupture rates at smaller diameters in women despite lower overall prevalence ([PMC12927653](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12927653/); [JAHA 2021](https://www.ahajournals.org/doi/10.1161/JAHA.120.019592)).

**Suggested ontology terms:**
- **GO (biological process):** GO:0030198 (extracellular matrix organization), GO:0030574 (collagen catabolic process), GO:0006954 (inflammatory response), GO:0007179 (TGF-beta receptor signaling pathway), GO:0006915 (apoptotic process), GO:0035909 (aorta morphogenesis)
- **CL (cell types):** CL:0000359 (vascular associated smooth muscle cell), CL:0000235 (macrophage), CL:0000084 (T cell), CL:0000542 (lymphocyte), CL:0000576 (monocyte), CL:0000499 (stromal cell/fibroblast-like), CL:0000094 (granulocyte/neutrophil)
- **CHEBI:** CHEBI:29108 (calcium — relevant to CaCl2 model), reactive oxygen species entries
- **UBERON:** UBERON:0002064 (abdominal aorta), UBERON:0001630 (tunica media), UBERON:0002037 (cerebellum — N/A), UBERON:0000317 (extracellular matrix)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Infrarenal abdominal aorta (most common site; UBERON:0002064 abdominal aorta / more specifically the infrarenal segment) — can extend to involve the iliac arteries (aortoiliac aneurysm) or, more rarely, the suprarenal/juxtarenal/pararenal segments and even the visceral-branch–bearing aorta (complex AAA, per the 2024 ESVS classification).
- **Secondary/complication-related organs:** Kidneys (renal ischemia from juxtarenal extension or embolization), lower extremities (distal embolization — "trash foot," acute limb ischemia), gastrointestinal tract (aortoenteric fistula, typically duodenum — UBERON:0002114), colon (ischemic colitis post-repair from IMA sacrifice), spinal cord (rare spinal ischemia post-repair).
- **Body systems:** Cardiovascular system primarily; secondary involvement of renal, gastrointestinal, and neurological (spinal) systems through complications or repair-related ischemia.

**Tissue and cell level:**
- Tunica media (UBERON:0001630) — site of elastin/collagen degradation and VSMC loss
- Tunica adventitia — site of adventitial inflammatory infiltrate, vasa vasorum changes
- Tunica intima — atherosclerotic change, site of intraluminal thrombus formation
- Cell populations: vascular smooth muscle cells (CL:0000359), macrophages (CL:0000235), T lymphocytes (CL:0000084), B lymphocytes/plasma cells, fibroblasts/myofibroblasts, endothelial cells (CL:0000115)

**Subcellular level:** Mitochondrial dysfunction and oxidative stress in VSMCs; ECM (extracellular region, GO:0005576) as the primary subcellular/extracellular compartment of pathology; lysosomal/autophagic changes described in VSMC senescence within the aneurysmal wall.

**Localization:**
- Most AAAs are **infrarenal** (below the renal arteries), reflecting relatively lower elastin content, sparser vasa vasorum, and greater hemodynamic wall stress at this segment compared to the thoracic aorta.
- **Lateralization:** Not applicable in the traditional sense (the aorta is a midline structure), though eccentric/asymmetric saccular dilation patterns occur and asymmetric mural thrombus distribution is common.

---

## 8. Temporal Development

**Onset:**
- Typical age of onset/detection: 65–85 years; uncommon before age 60 except in syndromic/familial forms (which can present in the 30s–50s).
- Onset pattern: **Insidious/chronic** for degenerative AAA (silent expansion over years to decades); **acute** presentation occurs only with rupture, dissection, or rapid mycotic/infectious aneurysm growth.

**Progression:**
- **Stages:** Subclinical dilation (aortic ectasia, 2.5–3.0 cm) → small AAA (3.0–5.4 cm, surveillance range) → large AAA (≥5.5 cm in men, often ≥5.0 cm threshold considered in women, intervention range) → symptomatic/rapidly expanding AAA → contained rupture → free rupture.
- **Progression rate:** Mean growth ≈2.2 mm/year overall; size-dependent (≈1.3 mm/year at 3 cm, up to 3.6 mm/year for larger aneurysms); "rapid expansion" (>1 cm/year or >0.5 cm in 6 months) is a red flag independent of absolute size ([PMC10354862](https://pmc.ncbi.nlm.nih.gov/articles/PMC10354862/)).
- **Course pattern:** Generally **progressive** (steadily enlarging), though growth can be non-linear/erratic in an individual patient; no established spontaneous regression for degenerative AAA (regression, when observed, is typically post-EVAR sac shrinkage).
- **Duration:** Chronic, lifelong once initiated — the disease does not resolve without intervention; the natural endpoint without repair (for aneurysms reaching critical diameter) is rupture.

**Patterns:**
- **Remission:** Not applicable to degenerative AAA (no spontaneous remission); inflammatory/IgG4-related AAA can respond to immunosuppressive therapy, "healing" the periaortic inflammatory component though not necessarily the aneurysm itself.
- **Critical periods/intervention windows:** The diameter threshold of 5.5 cm in men (5.0–5.5 cm often used in women, reflecting their higher rupture risk at smaller diameters) is the key decision point balancing rupture risk against elective repair risk; rapid-expansion criteria independently trigger earlier intervention.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence:** Population-screening studies report 1.6–7.2% among individuals aged 60–65+; a large US screening database found overall prevalence of ~2.82% (2.98% in the 65–75 age band) ([JVS 2020](https://www.jvascsurg.org/article/S0741-5214(19)31557-5/fulltext); [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0741521420306005)). Prevalence in women is estimated at roughly one-sixth that of men.
- **Incidence:** ~55 per 100,000/year in men aged 65–74, rising to 112 per 100,000/year at 75–84, and 298 per 100,000/year at ≥85 ([PMC4687424](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4687424/)); incidence is highest in male smokers (274/100,000/year at 65–74).
- **Global burden (GBD 2021):** 153,927 deaths from aortic aneurysm globally in 2021 (a 73.9% increase in absolute deaths from 1990, though age-standardized death rate declined 21.4% to 1.86/100,000); 3.1 million DALYs in 2021 (age-standardized rate 36.54/100,000, a 26.5% rate decline despite 62.6% increase in absolute DALYs) — reflecting population aging and growth offsetting per-capita risk reduction from smoking-cessation trends and improved management. Age-standardized death rates continue to *rise* in low/low-middle SDI regions while falling in high-SDI regions ([Frontiers Cardiovasc Med 2025](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2025.1496166/full); [PMC12137283](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12137283/)).

### For Genetic Etiology
- **Inheritance pattern:** Sporadic/degenerative AAA is **multifactorial/polygenic**; monogenic syndromic AAA (Marfan, Loeys-Dietz, vEDS) is **autosomal dominant**. Familial (non-syndromic) AAA clustering shows heterogeneous patterns — studies of AAA kindreds found ~72% with recessive-appearing aggregation and ~25% with apparent autosomal dominant inheritance with incomplete penetrance.
- **Penetrance:** Variable and age-dependent even in monogenic forms (e.g., vEDS COL3A1 carriers have high but incomplete lifetime penetrance for a vascular event).
- **Expressivity:** Highly variable, even within a single kindred/mutation (e.g., aneurysm location, age of onset, and severity differ among relatives sharing an FBN1 or COL3A1 variant).
- **Genetic anticipation:** Not a well-established feature of AAA (unlike repeat-expansion disorders).
- **Founder effects:** Not prominently described for degenerative AAA; population-specific allele frequencies at GWAS loci (e.g., differing 9p21 or lipid-locus frequencies) contribute to population risk variation.
- **Consanguinity:** Not a major recognized risk factor for typical AAA (contrasts with clearly autosomal recessive Mendelian disorders).
- **Carrier frequency:** Not applicable in the traditional recessive-carrier sense; polygenic risk score (PRS) distributions from the 2023 meta-GWAS provide population-level risk stratification instead.

### Population Demographics
- **Affected populations:** Higher prevalence reported in populations of European ancestry compared with Black, Hispanic, and Asian populations in most US/European cohort studies, though data are less complete for non-European populations globally.
- **Geographic distribution:** Historically higher in Northern Europe, UK, Australia, New Zealand, and the US; declining incidence trends reported in several high-income countries attributed to reduced smoking prevalence, while incidence/mortality trends are rising in some lower/middle-SDI regions.
- **Sex ratio:** ~4–6:1 (male:female) for intact AAA prevalence; narrower ~2:1 ratio for ruptured AAA incidence, reflecting women's disproportionately higher rupture risk at a given diameter.
- **Age distribution:** Overwhelmingly a disease of older adults (>60 years), with risk continuing to rise through the 8th and 9th decades of life.

---

## 10. Diagnostics

### Clinical Tests
- **Imaging (primary diagnostic modality):** Abdominal ultrasound/duplex ultrasonography is the standard screening and surveillance tool (non-invasive, no radiation, validated in RCTs to reduce aneurysm-related mortality). **CT angiography (CTA)** is the gold standard for pre-operative planning and definitive sizing/morphology assessment; **MR angiography (MRA)** is an alternative, particularly when iodinated contrast is contraindicated.
- **Biomarkers:** **Plasma D-dimer** shows an incremental, dose-dependent association with AAA presence and has both diagnostic value (particularly in patients with peripheral artery disease, threshold >0.675 mg/L in one study) and prognostic value for predicting future aneurysm expansion ([PMC9203886](https://pmc.ncbi.nlm.nih.gov/articles/PMC9203886/)). Elevated CRP, IL-6, and MMP-9 are research-stage biomarkers reflecting the inflammatory/proteolytic burden but are not yet standard-of-care diagnostics.
- **Functional/other tests:** Not disease-specific beyond imaging; cardiac and pulmonary functional assessment (echocardiography, PFTs) is relevant peri-operatively given shared atherosclerotic/smoking-related comorbidity burden but does not diagnose AAA itself.
- **Pathology/histopathology (typically post-surgical specimen):** Medial elastin fragmentation and loss, VSMC depletion, adventitial and medial lymphoplasmacytic/macrophage infiltration, neovascularization, and (in inflammatory AAA) dense periaortic fibroinflammatory rind with IgG4+ plasma cells in the IgG4-related subtype.

### Genetic Testing
- Not routinely performed for sporadic degenerative AAA.
- **Indicated when:** young age of onset (<60 years, especially <50), personal/family history suggestive of a connective tissue disorder (tall stature, joint hypermobility, skin/vascular fragility, ectopia lentis, multiple arterial aneurysms/dissections), or strong multi-generational family history of AAA/TAAD.
- **Approach:** Multi-gene aortopathy panels covering *FBN1, TGFBR1, TGFBR2, COL3A1, SMAD3, TGFB2, TGFB3, ACTA2, MYH11, MYLM, PRKG1, LOX, FBLN4* etc. are preferred over single-gene testing given phenotypic overlap; whole-exome sequencing is used in atypical/undiagnosed familial aortopathy; chromosomal microarray is not first-line for isolated AAA (more relevant to syndromic multi-anomaly presentations).

### Clinical Criteria
- Diagnosis is essentially definitional by **imaging-measured diameter** (≥3.0 cm, or focal dilation ≥50% above the expected normal diameter for that aortic segment) rather than a symptom-based clinical criteria set (unlike DSM/consensus-criteria diseases).
- **Differential diagnosis:** Aortic dissection, retroperitoneal fibrosis/other retroperitoneal masses, pancreatic pseudocyst, tortuous/ectatic (non-aneurysmal) aorta, para-aortic lymphadenopathy, and — for the inflammatory subtype — IgG4-related disease versus infectious (mycotic) aneurysm (distinguished via blood cultures, procalcitonin, and imaging morphology/growth rate).

### Screening
- **USPSTF (2019):** **Grade B** — one-time ultrasound screening for men aged 65–75 who have ever smoked (≥100 cigarettes lifetime). **Grade C** — selective screening for men 65–75 who have never smoked. **Recommends against** screening women 65–75 who never smoked with no family history; **insufficient evidence** for women who smoked or have a family history ([USPSTF](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/abdominal-aortic-aneurysm-screening)). A recognized care gap exists for high-risk groups outside current guidelines (e.g., male smokers 45–65).

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **Rupture mortality:** Up to 80% overall case-fatality for ruptured AAA; ~50% of patients die before reaching the hospital; historical reports cite up to 90% mortality, with contemporary surgical series still reporting ~50–75% mortality depending on repair modality and time-to-treatment ([StatPearls NBK459176](https://www.ncbi.nlm.nih.gov/books/NBK459176/); [PMC10354862](https://pmc.ncbi.nlm.nih.gov/articles/PMC10354862/)).
- **US burden:** AAA rupture accounts for roughly 15,000 deaths per year in the United States.
- **Sex-specific mortality:** In-hospital mortality after rupture is significantly higher in women (41.5%) than men (32.2%); 5-year survival post-rupture repair is 40.7% in men versus 29.1% in women ([JAHA 2021](https://www.ahajournals.org/doi/10.1161/JAHA.120.019592)).

### Morbidity and Function
- Elective repair (EVAR or open) carries substantially lower perioperative mortality (typically <1–4% for elective EVAR, somewhat higher for open repair) than emergency repair for rupture.
- Long-term morbidity after EVAR includes endoleak, need for reintervention, and continued surveillance imaging burden; open repair carries greater immediate perioperative morbidity (longer recovery, higher cardiopulmonary complication rate) but historically lower long-term reintervention rates.
- Complications of untreated/growing AAA: distal embolization, aortoenteric/aortocaval fistula, chronic back/abdominal pain from mass effect.

### Disease Course and Recovery
- Without repair, aneurysms above the critical threshold (≥5.5 cm men) or rapidly expanding continue to enlarge and eventually rupture; smaller aneurysms under surveillance have a low (but non-zero) annual rupture risk (~2%/year for 4.0–5.5 cm).
- With timely elective repair, prognosis is generally favorable relative to the natural history of large untreated aneurysms.

### Prediction
- **Prognostic factors:** Aortic diameter (the dominant predictor — 12%/year rupture risk at 5.5 cm, rising to ~35%/year above 6.5 cm), growth rate, female sex, smoking status, hypertension, family history of rupture, wall stress/biomechanical modeling parameters (peak wall stress, wall stress-to-strength ratio), aneurysm sac shape (saccular vs. fusiform), and presence/volume of intraluminal thrombus.
- **Prognostic biomarkers:** Elevated D-dimer predicts both diagnosis and future expansion; MMP-9 and inflammatory markers are investigational prognostic candidates.

---

## 12. Treatment

### Pharmacotherapy
No drug is currently FDA-approved specifically to halt AAA growth or prevent rupture; management of small AAA under surveillance emphasizes cardiovascular risk-factor control.
- **Statins:** Some large screening-population studies (Danish cohorts) show high-dose statin therapy reduces AAA growth rate, need for repair, and adverse outcomes including rupture and death; however, meta-analyses of RCT-level evidence are inconsistent, with some showing no significant growth-rate benefit ([PMC2267254](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2267254/); [Clinician.com summary](https://www.clinician.com/articles/statins-for-abdominal-aortic-aneurysms-2)).
- **Doxycycline (MMP-9 inhibition):** Reduces aortic wall neutrophil and cytotoxic T-cell content and MMP expression/activation in mechanistic human trials, but **no clinical trial has demonstrated efficacy in slowing aneurysm growth or reducing clinical events**, and MMP-inhibition strategies overall have not achieved clinical success sufficient to change standard of care ([PMID 19364980](https://pubmed.ncbi.nlm.nih.gov/19364980/?dopt=Abstract); [Circulation](https://www.ahajournals.org/doi/10.1161/circulationaha.108.806505)).
- **Beta-blockers:** Observational/cohort signal of possible benefit was **not confirmed** in three separate randomized controlled trials; beta-blockers do not appear to significantly slow AAA growth.
- **Metformin:** Observational/cohort studies suggest reduced AAA growth and complication risk, but all supporting evidence to date is non-randomized; multiple RCTs (including the Metformin Aneurysm Trial, MAT) are underway/ongoing to establish causal efficacy ([PMC8710921](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8710921/)).
- **ACE inhibitors:** Associated with slower AAA growth in the UK Aneurysm Growth Study observational cohort (alongside metformin) ([BJS 2024](https://academic.oup.com/bjs/article/111/1/znad375/7459560)).
- **PCSK9 inhibitors:** Mendelian randomization data support PCSK9 as a therapeutic target (genetically proxied inhibition reduces AAA risk), positioning PCSK9 inhibitors as a plausible but not yet clinically proven pharmacotherapy avenue.
- **Overall assessment:** "None of the matrix metalloproteinase inhibition strategies has shown clinical success adequate to replace or modify the current standard of care" for AAA growth suppression; surveillance and timely surgical repair remain the mainstay.

### Surgical/Interventional (mainstay of definitive treatment)
- **Endovascular aneurysm repair (EVAR):** Preferred first-line modality in most eligible patients per 2024 ESVS guidelines; requires anatomically suitable aneurysm neck/access and durable, well-characterized devices (guidelines now advise against off-label IFU use electively and require ≥10 years durability data for newer devices) ([ESVS 2024 guidelines](https://www.ejves.com/article/S1078-5884(23)00889-4/fulltext)).
- **Open surgical repair:** Remains standard for complex anatomy (juxtarenal/pararenal/suprarenal, thoracoabdominal extension — Type IV TAAA) or when EVAR is anatomically unsuitable; centers are now recommended to perform ≥30 AAA repairs annually (≥15 each of open and endovascular) to maintain proficiency.
- **Ruptured AAA (rAAA):** EVAR is now Class I recommended as first-line where feasible, based on RCT and large cohort evidence of improved outcomes versus open repair in the emergency setting.
- **Fenestrated/branched EVAR (F/BEVAR):** Advanced endovascular options for complex juxtarenal, pararenal, and thoracoabdominal aneurysms, expanded significantly in the 2024 ESVS guideline update (Chapter 8).

Suggested MAXO/NCIT terms: **MAXO:0000004** (surgical procedure); **NCIT:C15329** (Surgical Procedure); endovascular aneurysm repair and open aortic aneurysm repair as specific procedure terms (NCIT has coded entries for "Endovascular Aneurysm Repair" and "Abdominal Aortic Aneurysm Repair").

### Supportive/Behavioral
- Smoking cessation counseling, blood pressure control, lipid management, and cardiovascular risk-factor optimization are core supportive measures for patients under surveillance (**MAXO:0000950** supportive care).
- Surveillance imaging protocols (ultrasound every 2–3 years for 3.0–3.9 cm, annually for 4.0–5.4 cm) constitute a structured monitoring intervention.

### Experimental
- Multiple ongoing RCTs of metformin (MAT and others), continued investigation of PCSK9 inhibitors and other lipid-modifying agents, and biomechanical/AI-based individualized rupture-risk-score tools (combining precise aortic measurements with clinical factors) are in development ([ScienceDirect rupture risk score pilot](https://www.sciencedirect.com/science/article/pii/S294991272300017X)).

### Treatment Strategy
Decision algorithm: size/growth-rate threshold → elective repair candidacy assessment (anatomy, comorbidity, life expectancy, patient preference) → EVAR vs. open repair vs. complex F/BEVAR → lifelong post-EVAR surveillance for endoleak/sac behavior. Personalized/precision approaches remain nascent relative to oncology but increasingly incorporate PRS and biomechanical modeling into rupture-risk stratification.

---

## 13. Prevention

### Primary Prevention
- **Smoking cessation/avoidance** is the single most impactful primary-prevention measure given the dominant, dose-dependent smoking risk.
- Cardiovascular risk-factor modification (blood pressure control, lipid management, physical activity) reduces overall vascular degenerative burden, plausibly reducing AAA incidence, though AAA-specific primary-prevention RCT evidence (beyond smoking cessation) is limited.
- No vaccine/immunization strategy is applicable (not an infectious disease in its common degenerative form; antimicrobial prophylaxis is relevant only to mycotic-aneurysm risk populations, e.g., IV drug users, endocarditis patients).

### Secondary Prevention (Screening/Early Detection)
- **USPSTF-endorsed one-time ultrasound screening** for men 65–75 who have ever smoked (Grade B), demonstrated in population-based RCTs to reduce aneurysm-related mortality.
- Selective/family-history-triggered screening extends to men who never smoked (Grade C) and is an area of active debate for women with smoking history or family history (currently "insufficient evidence").
- Structured surveillance imaging intervals for known small AAA constitute secondary prevention of rupture via timely detection of growth crossing intervention thresholds.

### Tertiary Prevention
- Timely elective repair before rupture is the principal tertiary-prevention strategy once an AAA has been diagnosed and reaches threshold size or rapid growth criteria.
- Post-repair surveillance (particularly post-EVAR imaging for endoleak) prevents late complications from progressing to rupture or reintervention emergencies.

### Genetic Counseling
- Recommended for patients/families with suspected syndromic aortopathy (Marfan, Loeys-Dietz, vascular EDS) or strong multi-generational AAA family history, to guide cascade genetic testing, personalized surveillance intervals, and family planning/risk communication (NSGC/ACMG frameworks apply as for other heritable aortopathies).

### Public Health
- Tobacco-control public health policy (taxation, advertising restriction, cessation program funding) is the most impactful population-level lever given the magnitude of the smoking-AAA association; national screening program implementation (e.g., UK NAAASP, similar Scandinavian and US VA programs) exemplifies organized secondary prevention at scale.

---

## 14. Other Species / Natural Disease

- **Taxonomy of naturally affected species:** Aortic aneurysms (including AAA-analogous lesions) have been described in horses (*Equus caballus*, NCBITaxon:9796), dogs (*Canis lupus familiaris*, NCBITaxon:9615), cats (*Felis catus*, NCBITaxon:9685), and non-human primates, though **naturally occurring degenerative AAA analogous to the common human disease is comparatively rare in companion animals** and is more often reported as isolated case reports (dissecting aortic aneurysm in a cat: [PMC339563](https://pmc.ncbi.nlm.nih.gov/articles/PMC339563/); aortic dissection with posterior paresis in a dog).
- **Copper deficiency models:** Copper deficiency is linked to impaired lysyl-oxidase-dependent collagen/elastin cross-linking and aortic aneurysm formation in **swine** (porcine native AAA model, [FASEB 2008](https://faseb.onlinelibrary.wiley.com/doi/full/10.1096/fasebj.22.1_supplement.902.7)) and in copper-deficient **Sprague-Dawley rats** (intimal/medial arterial disruption); the role of copper deficiency in dogs, cats, or non-human primates is not well established.
- **Veterinary relevance:** Aortic aneurysm/dissection in companion animals is clinically significant but uncommon relative to human incidence; when it occurs, it is often associated with underlying connective tissue weakness, infection, neoplastic invasion, or (in horses) parasitic (verminous, *Strongylus vulgaris*) arteritis rather than the atherosclerotic/smoking-driven degenerative process dominant in humans.
- **Comparative biology:** The conserved elastin/collagen-dependent aortic wall integrity mechanism (LOX-dependent cross-linking) is evolutionarily deep, which is why copper-deficiency and *Lox*-knockout models in rodents and pigs recapitulate key aspects of human AAA pathology despite differing primary triggers.
- **Zoonotic potential:** Not applicable — AAA is not a transmissible or zoonotic disease.

---

## 15. Model Organisms

AAA lacks a single model that fully recapitulates chronic, spontaneous human AAA; four widely used **inducible mouse models** dominate the field ([JVS-Vascular Science 2021](https://jvsvs.org/article/S2666-3503(21)00002-X/fulltext); [PMC8577080](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8577080/)):

1. **Angiotensin II (AngII) infusion model** (typically in *Apoe⁻/⁻* or *Ldlr⁻/⁻* mice): chronic AngII infusion via osmotic minipump induces suprarenal/thoracoabdominal dissecting aneurysms; captures dissection and aneurysm features but the anatomic location (suprarenal/visceral) differs from typical human infrarenal AAA.
2. **Porcine pancreatic elastase (PPE) perfusion model:** intraluminal elastase perfusion of the infrarenal aorta enzymatically degrades elastin, producing reliable infrarenal dilation that best mirrors human AAA especially beyond day 7, though technically demanding.
3. **External/periadventitial elastase application (ePPE):** topical elastase applied to the aortic adventitia, avoiding intraluminal manipulation; often combined with oral β-aminopropionitrile (a lysyl oxidase inhibitor) for more advanced/faster aneurysm formation ([JoVE 66812](https://www.jove.com/t/66812/advanced-abdominal-aortic-aneurysm-modeling-mice-combination-topical)).
4. **CaCl2 (calcium chloride) periadventitial application model:** produces inflammatory vascular wall thickening and aneurysmal change through a distinct calcification/inflammation-driven mechanism.
5. **Combined elastase + AngII rupture model:** by day 28, combined elastase perfusion plus AngII infusion produced dilation progressing to AAA with a 60% rupture rate — one of the few models that reproducibly captures **rupture**, a key translational gap in single-modality models ([PMID 32171859](https://pubmed.ncbi.nlm.nih.gov/32171859/)).

**Genetic models:** *Apoe⁻/⁻* and *Ldlr⁻/⁻* knockout mice (hyperlipidemic background sensitizing to AngII-induced aneurysm), *Fbn1* hypomorphic/knock-in mice (Marfan-like aortopathy, primarily root/ascending phenotype), *Lox* knockout/hypomorph mice (elastin cross-linking failure, perinatal aortic/arterial rupture), and various MMP/TIMP transgenic and knockout lines used to dissect protease-antiprotease balance.

**Other model systems:** The **porcine native AAA / copper-deficiency model** recapitulates a connective-tissue-disorder-like aortic phenotype in a large-animal system more anatomically similar to humans, useful for device/endovascular testing. Zebrafish and *Drosophila* models of aortic/vessel wall integrity exist for specific gene pathways (e.g., elastin/fibrillin homologs) but are not primary AAA disease models. Human iPSC-derived vascular smooth muscle cells and aortic organoid/explant systems are increasingly used for in vitro mechanistic and single-cell/spatial transcriptomic studies of VSMC phenotypic switching.

**Model characteristics/limitations:** Mouse models generally fail to spontaneously rupture (a major translational limitation, addressed partially by the combined elastase+AngII model), often affect atypical anatomic locations (suprarenal in AngII model versus infrarenal in humans), and do not fully capture the decades-long chronic degenerative time course of human AAA; large-animal (porcine) and induced-rupture combination models are used to bridge this gap for device testing and rupture-risk mechanistic study.

**Applications:** Mouse and pig models are used to dissect inflammatory cell contributions (macrophage/T-cell depletion studies), test candidate pharmacotherapies (doxycycline, statins, PCSK9 modulation, metformin) pre-clinically, and validate genetic findings from human GWAS (e.g., functional follow-up of *LRP1*, *SORT1*, *DAB2IP* candidate genes) via knockout/knock-in approaches.

---

## Summary Evidence Table (Key Citable Claims)

| Claim | Source |
|---|---|
| 141 independent AAA GWAS loci, 97 novel, PCSK9 highlighted as therapeutic target | Roychowdhury et al., *Nat Genet* 2023;55:1831-1842 ([link](https://www.nature.com/articles/s41588-023-01510-y)) |
| Current smoking OR ≈3.28 for AAA; former smoking OR ≈1.86 | [PMC6313801](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6313801/) |
| Rupture risk 12%/year at 5.5 cm, up to 35%/year above 6.5 cm | [PMC10354862](https://pmc.ncbi.nlm.nih.gov/articles/PMC10354862/) |
| Women rupture at smaller diameters, 4x increased frequency at <5.5cm | [AJP-Heart Circ Physiol](https://journals.physiology.org/doi/full/10.1152/ajpheart.00519.2017); [JAHA 2021](https://www.ahajournals.org/doi/10.1161/JAHA.120.019592) |
| MMP-2/MMP-9-TIMP imbalance drives ECM proteolysis | [PMC8880357](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8880357/) |
| USPSTF: one-time US screening, men 65-75 who ever smoked (Grade B) | [USPSTF](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/abdominal-aortic-aneurysm-screening) |
| Doxycycline reduces aortic wall neutrophils/T cells but lacks proven clinical growth-rate benefit | [PMID 19364980](https://pubmed.ncbi.nlm.nih.gov/19364980/?dopt=Abstract) |
| GBD 2021: 153,927 global AA deaths, 73.9% increase in absolute deaths 1990–2021 | [Frontiers 2025](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2025.1496166/full) |
| PCSK9 loss-of-function protective (OR≈0.595); HMGCR/statin proxy more protective (OR≈0.202) | [PMC11367000](https://pmc.ncbi.nlm.nih.gov/articles/PMC11367000/) |
| COL3A1 mutations cause ~2% of familial AAA (vascular EDS) | [PMC10454608](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10454608/) |
| Combined elastase+AngII mouse model achieves 60% rupture rate | [PMID 32171859](https://pubmed.ncbi.nlm.nih.gov/32171859/) |
| D-dimer >0.675 mg/L predictive biomarker for AAA in PAD patients | [PMC9203886](https://pmc.ncbi.nlm.nih.gov/articles/PMC9203886/) |

**Notes on gaps/uncertainty:** A number of candidate-gene AAA associations from earlier literature (pre-2015) were subsequently found to be poorly replicated in systematic review/meta-analysis ("mostly false" per EJVES 2016), underscoring that only the largest, most recent multi-ancestry GWAS meta-analyses (2023–2024) should be treated as high-confidence genetic architecture. Pharmacotherapy evidence for slowing AAA growth (statins, doxycycline, beta-blockers, metformin) remains predominantly observational/mixed, with RCT-level confirmation still pending for most agents (metformin trials ongoing) — no drug currently has proven, guideline-endorsed efficacy for halting AAA progression.