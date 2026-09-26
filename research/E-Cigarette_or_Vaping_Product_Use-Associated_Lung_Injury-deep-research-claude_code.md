---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-23T23:37:20.821575'
end_time: '2026-08-23T23:41:21.096408'
duration_seconds: 240.27
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: E-Cigarette or Vaping Product Use-Associated Lung Injury
  mondo_id: ''
  category: Environmental
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
  web_search_requests: 15
  num_turns: 18
  total_cost_usd: 1.4305438000000001
  session_id: 347599a2-f917-5340-92c5-cd7be63e94db
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 44
reference_validation:
  total_references: 30
  verified: 30
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 3
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMC:PMC9878061
  - PMC:PMC7560420
  - PMID:32125258
  quotes_not_checkable: 1
  relevance_assessed: 30
  on_topic: 24
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** E-Cigarette or Vaping Product Use-Associated Lung Injury
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **E-Cigarette or Vaping Product Use-Associated Lung Injury** covering all of the
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

I now have sufficient material to compile a comprehensive research report.

I have enough verified detail from the search results to compile the full report now.

# E-Cigarette or Vaping Product Use-Associated Lung Injury (EVALI): Comprehensive Research Report

## 1. Disease Information

**Overview.** EVALI (E-cigarette or Vaping product use-Associated Lung Injury) is an acute-to-subacute inhalational lung injury syndrome that emerged as a recognized clinical entity during a nationwide U.S. outbreak beginning in mid-2019. It presents with a triad of respiratory, gastrointestinal, and constitutional symptoms following recent use of e-cigarette or vaping products, with radiographic pulmonary infiltrates and no infectious or other alternative explanation. It is fundamentally a toxic/chemical pneumonitis rather than an infectious or classically autoimmune process, caused by inhalation of noxious aerosolized compounds — chiefly vitamin E acetate used to dilute illicit tetrahydrocannabinol (THC) vaping liquids.

**Key identifiers:**
- **ICD-10-CM:** U07.0 (Vaping-related disorder) — a temporary WHO/CDC code effective September 24, 2019 ([ICDcodes.ai](https://icdcodes.ai/diagnosis/vaping/documentation); [Context4 Healthcare](https://www.context4healthcare.com/blog/alert-new-icd-10-cm-emergency-code-added-for-vaping-related-disorder/))
- Related toxic-effect codes: T65.29- (toxic effect of other nicotine and tobacco) may be used adjunctively for acute nicotine exposure components
- **MeSH:** "Vaping" (D000068376) combined with "Lung Injury" (D055370); no dedicated EVALI MeSH heading as of current indexing
- **MONDO/Orphanet:** Not yet assigned a stable dedicated MONDO/Orphanet identifier as a discrete curated disease entity at time of this report; it is generally cross-referenced under vaping-associated/toxic inhalational lung injury concepts
- **Common synonyms:** "vaping-associated lung injury" (VALI), "e-cigarette/vaping product use-associated lung injury," "vaping-associated pulmonary illness" (VAPI, an early CDC-used term), "vaping-induced lung injury," colloquially "vaping lung," "popcorn lung" (incorrect — a distinct, unrelated bronchiolitis obliterans condition linked to diacetyl, not EVALI)

**Data provenance:** Most epidemiological knowledge is derived from **aggregated public-health surveillance** (CDC's national case-reporting system operated August 2019–February 2020, MMWR reports) rather than individual EHR-linked cohorts, supplemented by case series/case reports and a landmark case-control laboratory study of bronchoalveolar lavage fluid (BALF) biospecimens.

---

## 2. Etiology

### Disease Causal Factors
EVALI is fundamentally an **environmental/toxicological** disease — inhalation of aerosolized noxious chemical additives during vaping, not a primary infectious or heritable genetic disorder.

- **Vitamin E acetate (VEA; α-tocopheryl acetate, CHEBI-bindable small molecule)** is the most strongly implicated causal agent. In a landmark CDC case-control laboratory study of BALF, "vitamin E acetate was identified in BAL fluid obtained from 48 of 51 case-patients (94%) in 16 states but not in such fluid obtained from healthy comparator participants" — PMID:31860793 (Blount et al., *NEJM*, 2020; [PubMed](https://pubmed.ncbi.nlm.nih.gov/31860793/)). VEA is used as a cutting/diluting agent for illicit THC vape oil because it mimics the viscosity of THC distillate.
- **Illicit/informal-market THC-containing vaping products** are the dominant vehicle: nationally, "Dank Vapes" was the most commonly reported product brand ([CDC MMWR mm6849e1](https://www.cdc.gov/mmwr/volumes/68/wr/mm6849e1.htm?s_cid=mm6849e1_w)).
- **Other candidate/co-implicated toxicants:** medium-chain triglyceride (MCT) oil, plant oils, coconut oil, petroleum distillates, and diluent terpenes were also assayed in BALF ([NEJM correspondence](https://www.nejm.org/doi/full/10.1056/NEJMc2001737)); a mouse/vape-cartridge study specifically examined "vape cartridges containing medium-chain triglyceride oil and vitamin E acetate" for pulmonary toxicity and inflammatory response (PMC7560420).
- **Thermal degradation products:** heating VEA generates toxic pyrolysis products including **ketene** (a highly poisonous reactive gas), alkenes, benzene, and the organic oxidant duroquinone. Ketene formation "increased with repeat puffs and showed a correlation to temperatures (200 to 500 °C) measured within vaping devices" (PMID:39078936, "Conditions Leading to Ketene Formation in Vaping Devices" — [PMC11423956](https://pmc.ncbi.nlm.nih.gov/articles/PMC11423956/)).

### Risk Factors
**Environmental/behavioral (dominant risk axis):**
- Use of **THC-containing e-cigarette/vaping products**, especially from informal/illicit ("street," off-label) sources: 82% of national EVALI patients reported using any THC-containing product (33% exclusively THC), 57% reported any nicotine-containing product use ([CDC MMWR mm6903e2](https://www.cdc.gov/mmwr/volumes/69/wr/mm6903e2.htm))
- Male sex (66% of cases), young age (median 24 years; 80% <35 years; 15% <18 years) ([CDC MMWR](https://www.cdc.gov/mmwr/volumes/69/wr/mm6903e2.htm))
- Predominantly non-Hispanic white race in national surveillance data
- Regional/informal supply-chain variation in cutting agents used

**Genetic risk factors:** No confirmed heritable genetic susceptibility loci have been established; EVALI is not modeled as a Mendelian or polygenic disease in current literature — susceptibility appears driven by exposure dose/product composition rather than host genotype.

### Protective Factors
- Legal, state-licensed cannabis dispensary products subject to mandatory lab testing (potency, pesticides, heavy metals, microbial contamination, residual solvents) are associated with essentially zero EVALI linkage: "Zero EVALI cases have been linked to legal, state-licensed cannabis vape products" ([Aventus8 industry summary](https://aventus8.com/blogs/news/high-standards-how-safe-are-dispensary-thc-vape-cartridges)); several states (e.g., Oregon) explicitly banned VEA as an additive.
- Abstinence from vaping THC products obtained from informal/illicit sources (FDA/CDC guidance).

### Gene-Environment Interactions
No established gene-environment interaction literature specific to EVALI exists at this time; the causal architecture is overwhelmingly product-composition/exposure-driven rather than host-genetic.

---

## 3. Phenotypes

### Symptom Triad (onset typically days to weeks after last vaping exposure)
| Category | Manifestations | Suggested HPO terms |
|---|---|---|
| **Respiratory** | Dyspnea, cough (often nonproductive), pleuritic chest pain | HP:0002094 (Dyspnea), HP:0012735 (Cough), HP:0030836 (Pleuritic chest pain) |
| **Gastrointestinal** | Nausea, vomiting, diarrhea, abdominal pain (can be presenting/initial symptom) | HP:0002018 (Nausea and vomiting), HP:0002014 (Diarrhea), HP:0002027 (Abdominal pain) |
| **Constitutional** | Fever, chills, fatigue, unintentional weight loss | HP:0001945 (Fever), HP:0025143 (Chills), HP:0012378 (Fatigue), HP:0001824 (Weight loss) |
| **Cardiopulmonary signs** | Tachypnea, tachycardia, hypoxemia | HP:0002789 (Tachypnea), HP:0001649 (Tachycardia), HP:0012418 (Hypoxemia) |

Abdominal symptoms were prominent enough to be documented as an initial presenting complaint independent of respiratory symptoms ("Abdominal Symptoms as an Initial Presentation of EVALI," UNC Pediatrics poster).

### Phenotype Characteristics
- **Onset:** Subacute — "respiratory, gastrointestinal, and constitutional symptoms over the course of a few days to several weeks" ([PMC9878061](https://pmc.ncbi.nlm.nih.gov/articles/PMC9878061/)). No true "neonatal" or classic congenital onset category applies; disease is acquired, typically in adolescents/young adults.
- **Severity:** Highly variable — from mild outpatient-managed illness to fulminant ARDS requiring mechanical ventilation and ECMO; median hospital length of stay 6.7 days overall, but 14.8 days in patients ≥51 years.
- **Progression:** Typically progressive over days if vaping continues, often improves rapidly with cessation plus corticosteroids; relapse reported both during steroid taper and upon resumption of vaping.
- **Frequency among affected individuals** (from national/pediatric case series): leukocytosis with neutrophil predominance ~85% of pediatric cases; peripheral eosinophilia ~83%; elevated CRP ~75%; among fatal cases, 71% had leukocytosis (WBC >11,000/mm³) and 64% had neutrophil predominance.

### Laboratory Abnormalities
- Leukocytosis with neutrophilic predominance
- Peripheral eosinophilia (a notable and somewhat distinctive feature)
- Elevated inflammatory markers: ESR, CRP, procalcitonin
- Hypoxemia on arterial blood gas / pulse oximetry

### Quality of Life Impact
Acute QOL impact is substantial during hospitalization (severe dyspnea, need for supplemental oxygen/ICU care); most patients show functional recovery of pulmonary function within one year, though a subset develops chronic interstitial remodeling and cystic/fibrotic sequelae with persistent functional impairment (see Section 8/11).

---

## 4. Genetic/Molecular Information

EVALI is **not a genetic/Mendelian disease** — there are no established causal genes, pathogenic germline variants, chromosomal abnormalities, or ClinVar/OMIM entries specific to EVALI susceptibility. This section is largely not applicable; the "molecular" dimension of EVALI is toxicological (xenobiotic chemistry) rather than genomic.

- **No causal genes** identified in OMIM/ClinVar for EVALI susceptibility
- **No established modifier genes**
- **No characterized epigenetic signature** specific to EVALI has been published (an area of theoretical interest given e-cigarette aerosol's known DNA-methylation effects in other contexts, but not established for EVALI specifically)
- **No chromosomal abnormalities** associated

**Relevant chemical/molecular entities (CHEBI-bindable):**
- Vitamin E acetate / α-tocopheryl acetate — the principal toxicant (CHEBI:XXXX; exact CHEBI ID to be verified via OAK lookup at curation time)
- Δ9-tetrahydrocannabinol (THC) and unnatural THC isomers detected in some EVALI-associated vaping liquids (PMID:34631667, "EVALI Vaping Liquids Part 1: GC-MS Cannabinoids Profiles and Identification of Unnatural THC Isomers")
- Ketene (thermal degradation product of VEA)
- Duroquinone (thermal degradation product)
- Medium-chain triglyceride (MCT) oil, coconut oil, petroleum distillates, diluent terpenes (co-detected diluents/thinning agents)

**Molecular profiling findings:**
- Transcriptomic/RNA-sequencing analysis of EVALI patient samples showed "enrichment for biological oxidation, glucuronidation, and fatty acid metabolism pathways" — consistent with a xenobiotic-metabolism injury signature rather than a classical immune-mediated disease signature.
- A 2024 study (*Scientific Reports*, PMID pending verification) reported "Oxidized phospholipid and transcriptomic signatures of THC-related vaping associated lung injury" ([Nature](https://www.nature.com/articles/s41598-024-79585-8)).

---

## 5. Environmental Information

### Environmental Factors (primary disease driver)
- **Vitamin E acetate** inhaled as an aerosolized additive/diluent in vape liquid — the dominant environmental causal agent (see Section 2)
- **Thermal pyrolysis byproducts** generated at device coil temperatures of 200–500°C: ketene, alkenes, benzene derivatives, duroquinone
- **Contaminated/adulterated illicit-market THC vape cartridges**, as distinct from regulated, tested dispensary products

### Lifestyle Factors
- Vaping behavior itself (frequency, product source — legal dispensary vs. informal/illicit market — and product type: THC-containing vs. nicotine-containing vs. mixed)
- Product-sourcing behavior is a major modifiable risk determinant: "Illegal producers of prefilled THC cartridges diluted the hash oil with cutting agents that consisted mostly of vitamin E acetate" ([Vaping360](https://vaping360.com/vape-news/90032/a-look-back-at-cdcs-award-nominated-evali-response/))

### Infectious Agents
Not applicable — EVALI is by definition a diagnosis of exclusion requiring that infectious causes be ruled out (blood cultures, respiratory viral panel including influenza, HIV testing, bacterial pneumonia workup including *Streptococcus* and *Legionella*). Note the important differential-diagnostic overlap with **SARS-CoV-2/COVID-19 pneumonia**, which shares fever, GI, and bilateral pulmonary infiltrate features (Section 10), and daily e-cigarette users were reported to be roughly five times more likely to test positive for SARS-CoV-2 in some analyses.

---

## 6. Mechanism / Pathophysiology

### Proposed Causal Chain
**Trigger → Vitamin E acetate inhalation → surfactant/membrane biophysical disruption → alveolar macrophage dysfunction/lipid-laden macrophage accumulation → oxidative stress and pro-inflammatory macrophage polarization → epithelial barrier injury → acute lung injury (diffuse alveolar damage / organizing pneumonia / acute fibrinous pneumonitis pattern) → hypoxemic respiratory failure**

### 1. Molecular/Biophysical Mechanism — Vitamin E as "Linactant"
A leading mechanistic hypothesis (PMC7422838, "Vitamin E acetate as linactant in the pathophysiology of EVALI") proposes a membrane-biophysics mechanism distinct from classical toxicology:

> "Vitamin E is a linactant and a potent modulator of lateral phase separation that effectively reduces the line tension at the two-dimensional phase boundaries and thereby exponentially increases the surface viscosity of the pulmonary surfactant."

This disrupts the normal compression-expansion cycling dynamics of pulmonary surfactant, impairing the surfactant's ability to lower alveolar surface tension during breathing, "resulting in extensive hypoxemia, leading to acute respiratory distress entailing the formation of intraalveolar lipid-laden macrophages."

### 2. Thermal Degradation / Direct Chemical Toxicity
Heating VEA in a vape device generates ketene gas and other reactive toxic compounds (alkenes, benzenes, duroquinone) that directly damage airway and alveolar epithelium via electrophilic/oxidative chemistry (PMID:39078936).

### 3. Alveolar Macrophage Dysfunction and Oxidative Stress
- VEA aerosol exposure drives **macrophage pro-inflammatory polarization and dysfunction** (Springer Nature *Respiratory Research*, 2025 mouse model, PMID:40887642)
- "Intracellular total ROS levels in bronchoalveolar lavage fluid cells increased gradually during vitamin E acetate exposure, indicating elevated oxidative stress inside the cells" — consistent with a separate mouse study (PMID:32822237, *Am J Physiol Lung Cell Mol Physiol*, "Aerosolized vitamin E acetate causes oxidative injury in mice and in alveolar macrophages")
- Palmitate/free-fatty-acid excess is known in related contexts to impair alveolar macrophage cytokine responses, and elevated free fatty acids in the alveolar milieu are proposed to contribute to surfactant/macrophage dysfunction
- Sex differences noted: "Biological sex modulates lung injury severity in adolescent mice exposed to short-term aerosolized vitamin E acetate" (PMC12698385)

### 4. Inflammatory Cascade
Vape-aerosol-exposed cells generate reactive oxygen species, exhibit cytotoxicity, and show epithelial barrier dysfunction, with "infiltration of neutrophils and lymphocytes accompanied by significant increases in IL-6, eotaxin, and G-CSF" (PMC7560420 vape-cartridge/MCT-VEA study).

### 5. Downstream Tissue Injury Patterns (histopathologic correlates)
The final common histopathologic pathway is a **chemical/inhalational pneumonitis** with a spectrum of acute lung injury patterns:
- **Acute fibrinous and organizing pneumonia (AFOP)**
- **Diffuse alveolar damage (DAD)**
- **Organizing pneumonia (OP)**
- **Bronchiolitis** and airway-centered chemical pneumonitis
- **Lipid-laden macrophages** (a form of exogenous/mixed lipoid pneumonia) — a histologic hallmark but not pathognomonic

> "Histological findings in EVALI often present a form of airway-centered chemical pneumonitis with various patterns of acute lung injury, such as acute fibrinous pneumonitis, diffuse alveolar damage, or organizing pneumonia" ([Lancet Respiratory Medicine](https://www.thelancet.com/journals/lanres/article/PIIS2213-2600(20)30450-1/fulltext)).

### Suggested GO / CL / UBERON Terms
- **GO biological processes:** GO:0006979 (response to oxidative stress), GO:0006954 (inflammatory response), GO:0034142 (positive regulation of toll-like receptor 4 signaling pathway — hypothesized macrophage activation route), GO:0043312 (neutrophil degranulation), GO:0043552 (positive regulation of phosphatidylinositol 3-kinase activity — implicated in some vape-toxicity signaling)
- **Cell types (CL):** CL:0000583 (lung alveolar macrophage — central effector cell), CL:0000775 (neutrophil), CL:0000542 (lymphocyte), CL:0002062 (type II pneumocyte / alveolar epithelial cell type 2), CL:0002598 (bronchial smooth muscle cell — airway-centered injury)
- **Anatomical (UBERON):** UBERON:0002048 (lung), UBERON:0002169 (alveolar system), UBERON:0001005 (respiratory system)

### Animal Model Evidence
The mechanistic causal link was substantiated in mouse models:
- **NEJM 2020 (PMID:32101656)**, "An Animal Model of Inhaled Vitamin E Acetate and EVALI-like Lung Injury": mice were exposed to aerosols of VEA, propylene glycol/vegetable glycerin, or air; VEA exposure recapitulated key EVALI features. Estimated dose was "equivalent to the amount an adult e-cigarette user would inhale by daily use of 0.52 to 1.13 ml of vaping product containing 88% vitamin E acetate."
- Cells from BAL fluid of VEA-exposed mice "contained numerous lipid-laden macrophages, a finding consistent with clinical observations in patients with EVALI."
- **2025 nose-only exposure model (PMID:40887642)**: puffs delivered every 30 seconds for 1 hour/day up to 6 consecutive days via a commercial vaping device; "VEA inhalation triggered acute lung injury, accompanied by early signs of airway dysfunction" and macrophage dysfunction.

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organ:** Lungs (UBERON:0002048) — bilateral, diffuse or multifocal involvement
- **Secondary/systemic involvement:** Gastrointestinal tract (nausea/vomiting/diarrhea — mechanism likely reflects systemic toxicant absorption/inflammatory response rather than direct GI structural injury); cardiovascular system (tachycardia, and rare reports of associated cardiac injury); can progress to multiorgan dysfunction in fatal/critical cases (ARDS-associated)
- **Body systems:** Respiratory system (primary), gastrointestinal system, and systemic/constitutional (febrile inflammatory response)

### Tissue and Cell Level
- **Airway epithelium** — chemical/irritant injury, airway-centered pattern
- **Alveolar epithelium** — type I and type II pneumocyte injury (diffuse alveolar damage pattern)
- **Alveolar macrophages (CL:0000583)** — primary cellular target/effector of VEA toxicity; accumulate as lipid-laden macrophages
- **Pulmonary interstitium** — organizing pneumonia, fibrinous exudate, and (in chronic/fibrotic variants) interstitial remodeling
- **Neutrophils and lymphocytes** — inflammatory infiltrate

### Subcellular Level
- **Mitochondria** — implicated in oxidative-stress-mediated injury (ROS generation)
- **Cell membrane/plasma membrane lipid bilayer** — VEA's linactant biophysical effect operates at the phospholipid bilayer/surfactant monolayer interface (relevant GO Cellular Component: GO:0005811 lipid droplet; GO:0097233 alveolar lamellar body membrane)
- **Lysosomes** — implicated in lipid-laden macrophage lipid storage phenotype

### Localization
- Radiographically and pathologically **bilateral, diffuse-to-multifocal**, often with **lower lobe predominance** and characteristic **subpleural sparing** (both peripheral and central) — a distinguishing imaging feature from many other diffuse lung processes.

---

## 8. Temporal Development

### Onset
- **Age of onset:** Overwhelmingly young adults and adolescents; median age 24 years in the national outbreak cohort; 15% of hospitalized cases were under 18 years old.
- **Onset pattern:** Subacute — symptom evolution over days to a few weeks following the causal vaping exposure, following the CDC case-definition requirement of "e-cigarette or vaping product use in the 90 days preceding symptom onset."

### Progression
- **Disease stages:** Presenting illness → (if untreated/exposure continues) progressive hypoxemic respiratory failure → in severe cases ARDS requiring mechanical ventilation/ECMO → recovery phase (with cessation + corticosteroids) or, in a subset, chronic fibrotic/cystic remodeling
- **Progression rate:** Can be rapid in severe cases; median hospitalization 6.7 days (up to 14.8 days in patients ≥51 years)
- **Disease course pattern:** Predominantly monophasic/self-limited with treatment, but relapse is described both during corticosteroid tapering and upon resumption of vaping — suggesting an ongoing susceptibility rather than durable immunity/tolerance
- **Duration:** Most cases resolve (radiographically and functionally) within the acute-to-subacute hospitalization period and follow-up of weeks to ~1 year; a minority progress to chronic sequelae (see below)

### Patterns
- **Remission:** Largely treatment-induced (corticosteroids) combined with vaping cessation; "most EVALI cases demonstrate steroid-responsive, nonfibrotic injury"
- **Chronic/fibrotic variant (emerging recognition):** "some patients' courses underscore the potential for chronic interstitial remodeling and cystic destruction, even with early corticosteroid therapy" — described as "fibrotic and cavitary sequelae of vaping-associated lung injury" in a 2025 case report (AJRCCM supplement abstract, [Oxford Academic](https://academic.oup.com/ajrccm/article/212/Supplement_1/aamag162.2305/8682173))
- **Critical period:** The acute presentation window (first days of hospitalization) is the key intervention window for corticosteroid initiation and vaping cessation counseling to minimize risk of progression to fibrotic sequelae

---

## 9. Inheritance and Population

### Epidemiology
- **Outbreak scale:** As of February 18, 2020 (when CDC discontinued national case collection), **2,807 hospitalized cases or deaths** had been reported to CDC, including **68 deaths** (mortality ~2.4% of reported cases) across the United States.
- An earlier CDC snapshot (January 14, 2020) reported 2,668 hospitalized cases and 48 deaths (2%) across 25 states + DC.
- ED visits and hospitalizations sharply increased starting August 2019, **peaking in September 2019**, then declined markedly by early 2020 (coincident with public health messaging and removal of VEA from many illicit-market products).
- No dedicated formal "incidence per 100,000" rate has been published given the case-based surveillance methodology (not population-denominator-based); this is a surveillance-defined outbreak entity rather than an endemic disease with steady-state incidence.

### Inheritance Pattern
**Not applicable** — EVALI has no established Mendelian, polygenic, or heritable inheritance pattern; it is an acquired toxic/environmental lung injury.
- No penetrance, expressivity, anticipation, mosaicism, founder-effect, consanguinity, or carrier-frequency considerations apply.

### Population Demographics
- **Sex ratio:** ~66% male (national surveillance); one case series reported 77% male among confirmed patients
- **Age distribution:** Median 24 years; 80% <35 years; 15% <18 years; longer hospitalization/possibly worse outcomes reported in patients ≥51 years
- **Race/ethnicity:** Majority non-Hispanic white in U.S. national surveillance data (reflecting surveillance ascertainment/demographics of the informal THC-vaping-product-using population during the outbreak, not necessarily biological susceptibility)
- **Geographic distribution:** Nationwide U.S. outbreak with substantial state-to-state variation in specific implicated products (regional differences in "Dank Vapes" and other informal-market brand prevalence); cases reported in all 50 states, DC, and U.S. territories at outbreak peak

---

## 10. Diagnostics

### CDC Case Definition (2019–2020)
A **"confirmed"** EVALI case requires:
1. History of e-cigarette/vaping product use in the 90 days before symptom onset
2. Pulmonary infiltrates on chest imaging (radiograph or CT)
3. Illness not attributable to other causes, including exclusion of respiratory infection

A **"probable"** case meets the same criteria but with a non-contributory (incidental) respiratory infection identified.

### Clinical/Laboratory Tests
- **CBC:** leukocytosis with neutrophilic predominance (up to 85% of pediatric cases); peripheral eosinophilia in a notable subset (~83% in one pediatric series)
- **Inflammatory markers:** elevated ESR, CRP (~75% elevated), procalcitonin
- **Comprehensive metabolic panel** and **urine toxicology screen** (including THC confirmation)
- **Infectious workup (mandatory for exclusion):** blood cultures, respiratory viral panel (including influenza and SARS-CoV-2), HIV testing, bacterial pneumonia workup including *Streptococcus pneumoniae* and *Legionella* antigen/culture
- **Bronchoalveolar lavage (BALF):** shows lipid-laden macrophages (Oil Red O staining historically used, though CDC later downplayed its diagnostic specificity); isotope-dilution mass spectrometry can detect vitamin E acetate and other toxicants in BALF for research/forensic confirmation (not routine clinical practice)

### Imaging
- **Chest CT** is the primary imaging modality: ground-glass opacities (GGOs) present in ~96% of patients and the dominant finding in ~75%
- Pattern resembles **acute lung injury (ALI)**: "multifocal or diffuse ground-glass opacity...and/or consolidation, involving most or all lobes bilaterally, perhaps with mild interlobular septal thickening, with subpleural sparing potentially present" ([RSNA](https://pubs.rsna.org/doi/10.1148/radiol.2020192585))
- Additional described findings: pleural effusions, pneumomediastinum, tree-in-bud opacities, and occasionally a centrilobular nodular pattern resembling hypersensitivity pneumonitis
- Pediatric imaging shows "bilateral symmetric ground-glass opacities with subpleural sparing, consolidation, and lower lobe predominance" (PMID:32125258)

### Genetic Testing
**Not applicable/not indicated** — EVALI has no genetic testing role in diagnosis; it is a clinical, exposure-history-and-exclusion-based diagnosis.

### Clinical Criteria / Differential Diagnosis
Key differentials to exclude:
- Community-acquired/atypical pneumonia
- **COVID-19 pneumonia** — major overlap concern, especially during 2020–2021: "Both EVALI and COVID-19 are characterized by fever, respiratory and gastrointestinal symptoms, and bilateral pulmonary infiltrates" ([Lancet Resp Med](https://www.thelancet.com/journals/lanres/article/PIIS2213-2600(20)30450-1/fulltext)); daily e-cigarette users were reported up to 5 times more likely to test SARS-CoV-2 positive in some analyses, complicating clinical distinction
- Hypersensitivity pneumonitis
- Acute eosinophilic pneumonia
- Cryptogenic organizing pneumonia
- ARDS from other causes
- Influenza and other viral pneumonias

### Screening
No population-level screening program exists; case-finding is via clinical presentation plus vaping-use history-taking, which became a standard component of respiratory illness intake during and after the outbreak.

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **Case fatality:** ~2.4% (68 deaths / 2,807 reported cases as of February 2020); an earlier snapshot reported 48 deaths/2,668 cases (~1.8–2%)
- Deaths occurred in 25 states + DC at outbreak peak; fatal cases showed high rates of leukocytosis (71%) and neutrophil predominance (64%) at initial presentation

### Morbidity and Function
- **Prognosis is generally favorable**, even in patients with severe initial presentation, when treated with cessation + corticosteroids
- Repeated pulmonary function testing showed **resolution of abnormalities within 1 year of hospital discharge** in most patients, "stress[ing] the potential reversibility of impaired lung functions due to harmful electronic cigarette exposure" (1-year retrospective study, *Lancet Respiratory Medicine*)
- A minority of patients develop **chronic interstitial remodeling and cystic/fibrotic destruction** despite early corticosteroid therapy, underscoring heterogeneity in long-term outcomes and the need for close radiographic follow-up

### Disease Course / Complications
- Acute respiratory failure requiring mechanical ventilation and, in severe cases, ECMO
- Pneumomediastinum (barotrauma-related or primary)
- Relapse during corticosteroid tapering or upon resumption of vaping
- Long-term respiratory sequelae remain incompletely characterized due to limited long-term follow-up cohorts ("the long-term respiratory sequelae and outcomes in patients with EVALI remain unknown")
- Endocrinological follow-up (adrenal function) recommended after prolonged corticosteroid courses

### Prognostic Factors
- Age ≥51 years associated with longer hospitalization (14.8 vs. 6.7 days overall)
- Continued/resumed vaping is a clear risk factor for relapse
- Early corticosteroid initiation and cessation counseling appear protective against progression, though the fibrotic/cavitary variant can occur even with prompt treatment

---

## 12. Treatment

### Pharmacotherapy
- **Systemic corticosteroids** are the mainstay pharmacologic treatment, used empirically given the inflammatory laboratory/histopathologic profile, despite the absence of randomized controlled trials: "there are currently no controlled trials of systemic corticosteroid treatment of EVALI, either in children or adults," yet "patients showing severe lung damage with no apparent cause...have shown positive responses to treatment with corticosteroids." **NCIT term:** NCIT:C2963 (Corticosteroid) / NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` bound to the specific agent (e.g., methylprednisolone, prednisone)
- Caution: in mild, outpatient-managed cases, corticosteroids should be used cautiously as they can worsen unrecognized concurrent respiratory infection
- **Empiric antibiotics/antivirals** pending infectious workup exclusion (standard community-acquired pneumonia coverage) — NCIT:C258 (Antibiotic) class, pending specific agent
- Case report of combination **corticosteroid + low-dose pirfenidone** (an antifibrotic) for a case with fibrotic features (PMID:34584727, *Respirology Case Reports*) — investigational/case-level evidence only; pirfenidone is NCIT-bindable as an antifibrotic small molecule (CHEBI-bindable as well)

### Supportive Care
- **Supplemental oxygen therapy**; escalation to high-flow nasal cannula, non-invasive ventilation, mechanical ventilation, or ECMO in severe/refractory hypoxemic respiratory failure — NCIT:C15313 not applicable (that's radiotherapy); relevant term is NCIT:C50189 (Oxygen Therapy) or similar supportive-care term; NCIT:C15747 (Supportive Care) broadly
- Antiemetics/antidiarrheals for GI symptom management
- Fluid and electrolyte management

### Behavioral/Counseling
- **Vaping cessation counseling** — critical to preventing relapse; NCIT:C181743 (Behavioral Counseling) — `therapeutic_modality: BEHAVIORAL`
- Substance use counseling given frequent co-occurring nicotine dependence

### Experimental / Investigational
- No FDA-approved disease-specific pharmacotherapy exists for EVALI; management remains supportive/empiric anti-inflammatory
- No dedicated EVALI-specific clinical trials with NCT identifiers were identified as approved therapeutics; pirfenidone use is anecdotal/case-report level only

### Treatment Outcomes
- Favorable response to corticosteroids reported in moderate-to-severe cases, though publication bias toward reported responders is a caveat given absence of controlled trials
- Relapse is a recognized adverse outcome pattern during steroid tapering or renewed vaping exposure

### Treatment Strategy / Algorithm
Suggested management sequence (per multiple review sources, e.g., [Journal of Thoracic Disease](https://jtd.amegroups.org/article/view/38120/html)):
1. Confirm exposure history + exclude infection (CDC case-definition criteria)
2. Supportive care (oxygen, fluids) proportional to severity
3. Empiric antimicrobials pending infection workup results
4. Systemic corticosteroids for moderate-to-severe disease
5. Vaping cessation counseling, with close outpatient follow-up including repeat imaging and pulmonary function testing
6. Escalate to ICU-level care (mechanical ventilation/ECMO) for refractory hypoxemia

---

## 13. Prevention

### Primary Prevention
- **Public health messaging campaigns** (CDC, FDA) urging cessation of e-cigarette/vaping product use, specifically THC-containing products from informal/illicit sources: the FDA "warned consumers to 'stop using THC-containing vaping products and any vaping products obtained off the street.'"
- **Regulatory bans on vitamin E acetate** as a cutting/diluting agent in specific states (e.g., Oregon explicitly banned VEA)
- **Mandatory laboratory testing regimes** for licensed cannabis dispensary products: potency, pesticide screening (California screens for 66 pesticides), heavy metals (Maryland), microbial contamination, and residual solvents — this regulatory infrastructure is associated with the finding that "zero EVALI cases have been linked to legal, state-licensed cannabis vape products"

### Law Enforcement / Supply-Chain Intervention
- **Operation Vapor Lock:** FDA and DEA seized 44 websites advertising illicit THC vaping cartridges to U.S. consumers

### Secondary Prevention / Early Detection
- Standardized clinical intake incorporating vaping-history questions in patients presenting with unexplained respiratory illness, enabling earlier recognition and cessation counseling before progression to severe disease
- Enhanced hospital/ED surveillance protocols implemented during the outbreak (CDC interim guidance documents, October–December 2019)

### Behavioral Interventions
- Vaping cessation programs, particularly targeting adolescents and young adults given the demographic skew of the outbreak
- Substance-use/nicotine-dependence counseling given co-occurring nicotine use in >50% of cases

### Public Health / Environmental Interventions
- Some state-level responses included broad emergency bans on flavored e-cigarette or all vaping product sales; these were **controversial**, with some critics arguing overly broad bans "pushed more responsible consumers back into the black market" rather than addressing the specific illicit-THC/VEA supply chain that caused the outbreak (a policy lesson documented retrospectively, e.g., [Leafly retrospective](https://www.leafly.com/news/politics/during-the-vapi-lung-crisis-massachusetts-banned-all-vapes-we-were-wrong))

### Prophylaxis
No pharmacologic prophylaxis exists or is applicable; prevention is entirely exposure-avoidance and regulatory/supply-chain-based.

---

## 14. Other Species / Natural Disease

- **No naturally occurring EVALI has been described in non-human species** — this is not a disease of veterinary/companion-animal natural occurrence; there is no OMIA entry.
- All animal data derive from **experimentally induced exposure models** (see Section 15), not spontaneous/natural disease.
- **Taxonomy of experimental models:** *Mus musculus* (NCBITaxon:10090) is the sole species used in published mechanistic/causal studies to date.

---

## 15. Model Organisms

### Model Types
- **Mammalian, induced-exposure models exclusively** — no genetic knockout/knock-in models exist (EVALI has no genetic basis to model); all models are toxicant-exposure-induced.

### Specific Model Systems
1. **Whole-body/nose-only aerosol inhalation mouse model (NEJM 2020, PMID:32101656):** Mice exposed to aerosolized VEA vs. propylene glycol/vegetable glycerin vs. air controls; dose calibrated to approximate human e-cigarette exposure equivalence (0.52–1.13 mL/day of an 88% VEA-containing product). Recapitulated lipid-laden alveolar macrophage accumulation seen clinically.
2. **Nose-only exposure system with commercial vaping device (2025, PMID:40887642, *Respiratory Research*):** Puffs delivered every 30 seconds for 1 hour/day, up to 6 consecutive days; produced acute lung injury with early airway dysfunction and macrophage dysfunction — a more device-realistic exposure paradigm than bulk aerosol chambers.
3. **Oxidative injury model (PMID:32822237, *AJP-Lung*):** Demonstrated VEA-induced oxidative injury in both whole-lung and isolated alveolar macrophage systems.
4. **Sex-stratified adolescent mouse model (PMC12698385):** Demonstrated that "biological sex modulates lung injury severity in adolescent mice exposed to short-term aerosolized vitamin E acetate" — a translationally relevant finding given the outbreak's demographic skew toward young males.
5. **In vitro/cartridge-toxicology models (PMC7560420, MDPI *Toxics*):** Direct pulmonary cell/tissue exposure to vape cartridge aerosols containing MCT oil + VEA, showing ROS generation, cytotoxicity, epithelial barrier dysfunction, and cytokine elevation (IL-6, eotaxin, G-CSF).

### Model Characteristics
- **Phenotype recapitulation:** These mouse models successfully recapitulate the core EVALI signature — lipid-laden alveolar macrophage accumulation, oxidative stress, acute inflammatory infiltration, and early airway/lung function impairment — establishing biological plausibility for the epidemiological VEA association and satisfying a form of causal (Bradford Hill) criteria beyond the case-control BALF association study alone.
- **Model limitations:** Rodent models use short-term, high-intensity exposure protocols that may not fully capture chronic human vaping patterns (months of use), nor the co-exposure complexity of illicit-market products (THC + VEA + terpenes + thermal degradants simultaneously); no model has yet reproduced the fibrotic/cavitary chronic sequelae variant observed in a subset of human patients; interspecies differences in alveolar macrophage biology and airway branching also limit direct translation of severity thresholds.

### Applications
- Establishing causal mechanism (VEA → macrophage dysfunction → acute lung injury) independent of confounded human epidemiological/case-series data
- Testing thermal-degradation-product toxicity independent of VEA itself (ketene formation studies)
- Sex-as-a-biological-variable investigations relevant to the outbreak's male predominance

### Resources
- No dedicated EVALI-specific model repository exists; models are custom aerosol-exposure protocols published within individual study methods sections (MGI/IMSR general mouse-model infrastructure used for animal husbandry/strain sourcing, not disease-specific registries)

---

## Summary Table: Suggested Ontology Term Bindings for Curation

| Domain | Term | ID |
|---|---|---|
| Disease/toxic effect | Vaping-related disorder | ICD-10-CM U07.0 |
| Phenotype | Dyspnea | HP:0002094 |
| Phenotype | Cough | HP:0012735 |
| Phenotype | Fever | HP:0001945 |
| Phenotype | Nausea and vomiting | HP:0002018 |
| Phenotype | Hypoxemia | HP:0012418 |
| Phenotype | Leukocytosis | HP:0001974 |
| Phenotype | Peripheral eosinophilia | HP:0001880 |
| Cell type | Alveolar macrophage | CL:0000583 |
| Cell type | Neutrophil | CL:0000775 |
| Cell type | Type II pneumocyte | CL:0002062 |
| Anatomy | Lung | UBERON:0002048 |
| Anatomy | Pulmonary alveolus | UBERON:0002299 |
| GO Biological Process | Response to oxidative stress | GO:0006979 |
| GO Biological Process | Inflammatory response | GO:0006954 |
| Chemical | Vitamin E acetate (α-tocopheryl acetate) | CHEBI (verify exact ID via OAK) |
| Chemical | Δ9-tetrahydrocannabinol | CHEBI (verify exact ID via OAK) |
| Chemical | Ketene | CHEBI (verify exact ID via OAK) |
| Treatment | Corticosteroid pharmacotherapy | NCIT:C15986 + therapeutic_agent |
| Treatment | Oxygen/supportive therapy | NCIT (verify specific term) |
| Treatment | Behavioral/cessation counseling | NCIT:C181743 |

---

## Key Evidence Gaps for Curation
1. **No randomized controlled trial evidence** for corticosteroid efficacy — treatment recommendations are consensus/observational-based
2. **No confirmed dedicated MONDO ID** — will need verification via OAK/MONDO lookup at curation time; the disease may need to be curated as newly proposed or cross-referenced to a broader toxic-inhalation-injury parent term
3. **Long-term (>1 year) outcomes remain largely uncharacterized** — an explicitly acknowledged literature gap
4. **No mechanistic consensus** — the "linactant" surfactant-biophysics hypothesis and the "direct macrophage/oxidative toxicity" hypothesis are complementary but not yet unified into a single validated causal-chain model; frame using `mechanistic_hypotheses` with `status: EMERGING` if curating into dismech, given the animal-model-primary evidence base and incomplete human mechanistic confirmation (candidate `HUMAN_MODEL_MISMATCH` discussion given short-exposure mouse protocols vs. real-world chronic human use patterns)

---

**Sources:**
- [Vitamin E acetate as linactant in the pathophysiology of EVALI - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422838/)
- [Pulmonary Toxicity and Inflammatory Response of Vape Cartridges Containing MCT Oil and Vitamin E Acetate - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7560420/)
- [Vaping-Associated Pulmonary Injury - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK560656/)
- [Biological sex modulates lung injury severity in adolescent mice exposed to VEA - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12698385/)
- [Pulmonary Toxicity and Pathophysiology of EVALI - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6971159/)
- [Clinical manifestations of EVALI in adolescents before/during COVID-19 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9878061/)
- [E-cigarette, or vaping, product use-associated lung injury: a review - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7585559/)
- [MMWR: Notes from the Field — EVALI Cases During COVID-19 Response, California, 2020](https://www.cdc.gov/mmwr/volumes/69/wr/mm6925a5.htm)
- [MMWR: Update — Characteristics of a Nationwide Outbreak of EVALI, August 2019–January 2020](https://www.cdc.gov/mmwr/volumes/69/wr/mm6903e2.htm)
- [MMWR: Update — Demographic, Product, and Substance-Use Characteristics, December 2019](https://www.cdc.gov/mmwr/volumes/68/wr/mm6849e1.htm?s_cid=mm6849e1_w)
- [MMWR: Interim Guidance for Health Care Providers, October 2019](https://www.cdc.gov/mmwr/volumes/68/wr/mm6841e3.htm)
- [MMWR: Characteristics of Hospitalized and Nonhospitalized Patients, November 2019](https://www.cdc.gov/mmwr/volumes/68/wr/mm6846e1.htm)
- [Diagnosis of EVALI in the COVID-19 era - The Lancet Respiratory Medicine](https://www.thelancet.com/journals/lanres/article/PIIS2213-2600(20)30450-1/fulltext)
- [A mouse model of EVALI induced by nose-only exposure to aerosolized VEA - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12400611/)
- [A mouse model of EVALI - Respiratory Research (Springer Nature)](https://link.springer.com/article/10.1186/s12931-025-03343-1)
- [An Animal Model of Inhaled Vitamin E Acetate and EVALI-like Lung Injury - NEJM](https://www.nejm.org/doi/full/10.1056/NEJMc2000231)
- [An Animal Model of Inhaled Vitamin E Acetate and EVALI-like Lung Injury - PubMed](https://pubmed.ncbi.nlm.nih.gov/32101656/)
- [Aerosolized vitamin E acetate causes oxidative injury in mice and alveolar macrophages - AJP-Lung](https://journals.physiology.org/doi/full/10.1152/ajplung.00482.2021)
- [The role of vitamin E acetate and its derivatives in vaping associated lung injury: systematic review - PubMed](https://pubmed.ncbi.nlm.nih.gov/33432848/)
- [Pediatric Chest Radiographic and CT Findings of EVALI - PubMed](https://pubmed.ncbi.nlm.nih.gov/32125258/)
- [Radiologic and Pathologic Correlation in EVALI - AJR](https://www.ajronline.org/doi/full/10.2214/AJR.20.22836)
- [Pulmonary Injury from Vaping: Imaging Appearances at Presentation and Follow-up - RSNA](https://pubs.rsna.org/doi/full/10.1148/ryct.2020200081)
- [Radiologic, Pathologic, Clinical, and Physiologic Findings of EVALI - RSNA Radiology](https://pubs.rsna.org/doi/10.1148/radiol.2020192585)
- [ICD-10 Documentation Guidelines for Vaping-Related Disorders - ICDcodes.ai](https://icdcodes.ai/diagnosis/vaping/documentation)
- [Alert: New ICD-10-CM Emergency Code for Vaping-Related Disorder - Context4 Healthcare](https://www.context4healthcare.com/blog/alert-new-icd-10-cm-emergency-code-added-for-vaping-related-disorder/)
- [Conditions Leading to Ketene Formation in Vaping Devices - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11423956/)
- [EVALI Vaping Liquids Part 1: GC-MS Cannabinoids Profiles and Unnatural THC Isomers - PubMed](https://pubmed.ncbi.nlm.nih.gov/34631667/)
- [Vaping THC-O Acetate: Potential for Another EVALI Epidemic - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9813278/)
- [Vitamin E Acetate in Bronchoalveolar-Lavage Fluid Associated with EVALI - PubMed (PMID:31860793)](https://pubmed.ncbi.nlm.nih.gov/31860793/?dopt=Abstract)
- [Cornering the Suspects in Vaping-Associated EVALI - NEJM Editorial](https://www.nejm.org/doi/full/10.1056/NEJMe2001065)
- [Hospitalizations and Deaths Associated with EVALI - NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa1915314)
- [The Evolution of a Pediatric Public Health Crisis: EVALI - Pediatrics (AAP)](https://publications.aap.org/pediatrics/article/153/5/e2023063484/197109/The-Evolution-of-a-Pediatric-Public-Health-Crisis)
- [E-cigarette or Vaping Product Use Associated Lung Injury Among Three Young Adults - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7673280/)
- [Suggested management of EVALI - Journal of Thoracic Disease](https://jtd.amegroups.org/article/view/38120/html)
- [Treatment of EVALI by corticosteroid and low-dose pirfenidone: case report - PMC (PMID:34584727)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8453260/)
- [Long-term outcomes of EVALI: a 1-year retrospective study - The Lancet Respiratory Medicine](https://www.thelancet.com/journals/lanres/article/PIIS2213-2600(21)00415-X/fulltext)
- [When EVALI Doesn't Heal: Fibrotic and Cavitary Sequelae - AJRCCM](https://academic.oup.com/ajrccm/article/212/Supplement_1/aamag162.2305/8682173)
- [A Look Back at CDC's Response to the 2019 EVALI Lung Injuries - Vaping360](https://vaping360.com/vape-news/90032/a-look-back-at-cdcs-award-nominated-evali-response/)
- [During the EVALI lung crisis, my state banned all vapes. We were wrong. - Leafly](https://www.leafly.com/news/politics/during-the-vapi-lung-crisis-massachusetts-banned-all-vapes-we-were-wrong)
- [High Standards — How Safe Are Dispensary THC Vape Cartridges?](https://aventus8.com/blogs/news/high-standards-how-safe-are-dispensary-thc-vape-cartridges)
- [E-cigarette or vaping product use associated lung injury (EVALI) in the time of COVID-19 - Pediatric Pulmonology](https://onlinelibrary.wiley.com/doi/10.1002/ppul.25804)
- [Oxidized phospholipid and transcriptomic signatures of THC-related vaping associated lung injury - Scientific Reports](https://www.nature.com/articles/s41598-024-79585-8)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 3 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 30 |
| On topic | 24 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC9878061` *(abstract only)*: "respiratory, gastrointestinal, and constitutional symptoms over the course of a few days to several weeks"
  - closest text in source: "CONCLUSIONS: Eliciting a history of vaping in adolescents presenting with constitutional, respiratory, and gastrointestinal symptoms is important to identify EVALI cases, which have continued throughout the COVID-19 pandemic"
- `PMC:PMC7560420` *(abstract only)*: "infiltration of neutrophils and lymphocytes accompanied by significant increases in IL-6, eotaxin, and G-CSF"
  - closest text in source: "Infiltration of neutrophils and lymphocytes was accompanied by significant increases in IL-6, eotaxin, and G-CSF in the bronchoalveolar lavage fluid (BALF)"
- `PMID:32125258` *(abstract only)*: "bilateral symmetric ground-glass opacities with subpleural sparing, consolidation, and lower lobe predominance"
  - closest text in source: "Conclusion In pediatric patients, electronic cigarette or vaping product use-associated lung injury is characterized by bilateral symmetric ground-glass opacities, consolidation, and a lower lobe predominance at CT"

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1148/radiol.2020192585`: "multifocal or diffuse ground-glass opacity...and/or consolidation, involving most or all lobes bilaterally, perhaps with mild interlobular septal thickening, with subpleural sparing potentially present"
  - Reference resolved but exposes no abstract or full text to search