---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-23T13:33:45.826000'
end_time: '2026-08-23T13:37:42.119348'
duration_seconds: 236.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Iron Poisoning
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
  web_search_requests: 16
  num_turns: 18
  total_cost_usd: 1.4233671999999995
  session_id: 347599a2-f917-5340-92c5-cd7be63e94db
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 45
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 7
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Iron Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Iron Poisoning** covering all of the
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

I now have sufficient information to compile a comprehensive research report. Let me write the full report.

I now have comprehensive material to write the full report.

---

# Iron Poisoning (Acute Iron Toxicity) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Iron poisoning (acute iron toxicity) is a potentially lethal toxidrome resulting from ingestion of excessive elemental iron, most commonly from iron-containing dietary supplements, prenatal vitamins, or ferrous salt medications (ferrous sulfate, ferrous gluconate, ferrous fumarate). It is distinct from *chronic* iron overload disorders (hereditary hemochromatosis, transfusional hemosiderosis) — iron poisoning is an acute, dose-dependent, environmentally/behaviorally mediated toxic exposure rather than a genetic disorder of iron regulation, although both converge on overlapping downstream cellular iron-toxicity mechanisms (oxidative stress, ferroptosis). It remains "one of the leading causes of fatal poisoning in children under 6 years of age" historically, and continues to be an important cause of both unintentional pediatric poisoning and intentional (self-harm) poisoning in adolescents/adults ([StatPearls: Iron Toxicity](https://www.ncbi.nlm.nih.gov/books/NBK459224/); [Wikipedia: Iron poisoning](https://en.wikipedia.org/wiki/Iron_poisoning)).

**Key identifiers:**
- **ICD-10-CM:** T45.4X1A (Poisoning by iron and its compounds, accidental, initial encounter); related codes T45.4X2A (intentional self-harm), T45.4X3A (assault), T45.4X4A (undetermined intent) ([icd10data.com](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T36-T50/T45-/T45.4X1A))
- **ICD-10 (WHO):** T45.4 — Poisoning by iron and its compounds
- **MeSH:** Overlaps with "Iron Overload" (D019190) and "Poisoning" (D011041); no dedicated acute-toxicity MeSH heading distinct from the general iron/poisoning headings
- **MONDO:** No MONDO term dedicated specifically to "acute iron poisoning" was identified in this search (MONDO's iron-related terms center on hereditary iron-overload disorders, e.g., hemochromatosis, FTH1-related iron overload — [Orphanet: FTH1-related iron overload](https://www.orpha.net/en/disease/detail/247790)); acute iron poisoning is more naturally represented as a toxic/environmental exposure entity than a MONDO disease class
- **UMLS/SNOMED CT:** "Iron poisoning" / "Iron toxicity" concepts exist in clinical toxicology terminologies (WikEM, Medscape "Iron Toxicity" and "Pediatric Iron Toxicity")

**Synonyms:** Acute iron toxicity, acute iron overdose, ferrous sulfate poisoning, iron ingestion (toxic), iron salt poisoning.

**Data provenance:** Knowledge derives predominantly from aggregated poison-control-center surveillance (American Association of Poison Control Centers, AAPCC National Poison Data System), case reports/series (often intentional adult overdoses), retrospective cohort studies, and animal (mouse/rat) toxicology data — rather than large prospective clinical trials, given the acute/emergent nature and rarity of severe cases.

Sources: [PubMed: Acute iron poisoning (PMID:8187690)](https://pubmed.ncbi.nlm.nih.gov/8187690/) · [StatPearls: Iron Overload and Toxicity](https://www.ncbi.nlm.nih.gov/sites/books/NBK526131/) · [Merck Manual: Iron Poisoning](https://www.merckmanuals.com/professional/injuries-poisoning/poisoning/iron-poisoning) · [Medscape: Iron Toxicity](https://emedicine.medscape.com/article/815213-overview)

---

## 2. Etiology

**Disease causal factor:** Ingestion of a supratherapeutic dose of elemental iron, overwhelming normal intestinal mucosal regulation of iron absorption and saturating plasma iron-binding capacity (transferrin), producing free/non-transferrin-bound iron that is directly cytotoxic. This is a purely **environmental/exposure-mediated** disease process — there is no genetic causal variant required, though genetic background (e.g., HFE hemochromatosis carrier status) may theoretically modulate baseline iron handling (not well studied for acute poisoning specifically).

**Toxic dose thresholds (elemental iron, oral):**
- **<20 mg/kg:** generally non-toxic/asymptomatic
- **20–40(–60) mg/kg:** mild-to-moderate toxicity — self-limited GI symptoms (vomiting, abdominal pain, diarrhea)
- **>40–60 mg/kg:** potentially serious/severe systemic toxicity
- **>60 mg/kg:** potentially lethal
- Animal-model acute lethal dose: ~150–200 mg/kg elemental iron
- Lowest reported lethal dose in a human: a 21-month-old child who ingested 325–650 mg elemental iron as ferrous sulfate

A standard 325 mg ferrous sulfate tablet contains ~65 mg elemental iron (ferrous sulfate is ~20% elemental iron by weight); prenatal vitamins and adult-strength ferrous sulfate tablets are the highest-risk products because of their high elemental-iron density relative to pediatric multivitamins.

Sources: [California Poison Control: Iron Ingestion](https://www.rchsd.org/documents/2014/02/iron-ingestion.pdf/) · [Iron Ingestion: Evidence-Based Consensus Guideline](https://www.clintox.org/wp-content/uploads/2016/05/Iron-Ingestion.pdf) · [StatPearls (Archived): Iron Toxicity](https://www.ncbi.nlm.nih.gov/books/NBK459224/)

**Risk factors (environmental/behavioral, not genetic):**
- Age <5 years — accounts for the overwhelming majority of unintentional serious morbidity/mortality (young children accidentally ingesting adult-formulation iron tablets, mistaking them for candy due to bright coloring)
- Household presence of prenatal vitamins or high-dose ferrous sulfate (highest elemental-iron-per-tablet products)
- Adolescent/young adult female sex for **intentional** ingestion (self-harm/suicide attempts) — the dominant mechanism of severe iron poisoning in adults
- Lack of child-resistant/unit-dose packaging (historically)
- Careless storage — parents/caregivers may perceive iron/vitamin supplements as "safe," reducing vigilance

**Protective factors:**
- Unit-dose (blister) packaging and child-resistant containers for products with ≥30 mg elemental iron/dosage unit (US FDA 1997 rule, effective July 1997) — associated with a marked reduction in pediatric iron-poisoning deaths
- Label warning statements mandated by FDA guidance
- Early recognition/early chelation therapy — greatly reduces mortality

**Gene-environment interaction:** Not a defined feature of this condition in the literature reviewed; acute iron poisoning is an environmentally/behaviorally driven exposure rather than a gene-environment interaction disease. (Contrast with hereditary hemochromatosis, where HFE variants confer chronically increased iron absorption — a distinct disease entity.)

Sources: [FDA: Small Entity Compliance Guide, Iron-Containing Supplements Label Warning](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/small-entity-compliance-guide-label-warning-statements-iron-containing-supplements-and-drugs) · [Federal Register: Iron-Containing Supplements and Drugs](https://www.federalregister.gov/documents/2003/10/17/03-26188/iron-containing-supplements-and-drugs-label-warning-statements-and-unit-dose-packaging-requirements) · [PubMed: Unit-dose packaging of iron supplements and reduction of iron poisoning in young children](https://www.ncbi.nlm.nih.gov/pubmed/15939855) · [AAP: Accidental Iron Poisoning in Children](https://publications.aap.org/pediatrics/article/24/3/399/40614/Accidental-Iron-Poisoning-in-Children-Report-of)

---

## 3. Phenotypes

Iron toxicity classically progresses through **five overlapping clinical stages** (not all patients pass through every stage sequentially):

| Stage | Timing | Phenotype |
|---|---|---|
| **I — Gastrointestinal/corrosive** | 0–6 h | Direct mucosal corrosive injury: vomiting (HP:0002013), abdominal pain (HP:0002027), diarrhea (HP:0002014), often hematemesis/hematochezia (bloody vomiting/stool) from massive GI fluid/blood loss; can cause hemodynamic instability/hypovolemic shock even at this early stage |
| **II — Latent** | 6–24 h | Apparent GI improvement, but ongoing cellular toxicity: persistent tachycardia (HP:0001649), lethargy (HP:0001257), evolving metabolic acidosis (HP:0011900) — a deceptively "quiet" period that can mislead clinicians into premature discharge |
| **III — Shock/metabolic decompensation** (most deaths occur here) | 24–48+ h | Recurrent GI symptoms, worsening metabolic (lactic) acidosis, circulatory (hypovolemic/distributive) shock (HP:0001744-adjacent concepts), coagulopathy (HP:0001928), multi-organ dysfunction |
| **IV — Hepatotoxicity** | 2–5 days | Fulminant hepatic failure (HP:0006554) from direct mitochondrial/hepatocellular iron toxicity — can progress to require liver transplantation |
| **V — Late GI scarring/obstruction** | 2–8 weeks | Gastric outlet obstruction and small-bowel/pyloric strictures from mucosal scar formation — presents with recurrent vomiting, abdominal pain, and obstipation weeks after the acute event; historically treated surgically (Mikulicz procedure, gastrojejunostomy, Billroth I resection) |

**Additional/organ-specific phenotypes:**
- **Cardiovascular:** hypotension, cardiovascular collapse, cardiogenic and distributive shock
- **Hematologic:** coagulopathy — iron (Fe³⁺/non-transferrin-bound iron) reversibly inhibits serine proteases of the coagulation cascade (thrombin, factor Xa, kallikrein), causing bleeding diathesis distinct from hepatic-synthetic coagulopathy
- **Renal:** acute kidney injury from hypoperfusion/direct toxicity
- **CNS:** lethargy progressing to coma in severe cases
- **Metabolic:** anion-gap metabolic acidosis (from uncoupled oxidative phosphorylation, lactic acid accumulation, and hydrolysis of ferric iron to iron hydroxide releasing free H⁺)

**Severity/frequency:** Symptom severity is dose-dependent (see thresholds above); most pediatric exposures are asymptomatic or mild (small unintentional ingestions), while intentional adult overdoses (tens of tablets) are far more likely to reach severe/fatal stages.

**Suggested HPO terms:** HP:0002013 (Vomiting), HP:0002014 (Diarrhea), HP:0002027 (Abdominal pain), HP:0001649 (Tachycardia), HP:0001257 (Lethargy), HP:0011900 (Metabolic acidosis), HP:0001928 (Abnormal coagulation), HP:0006554 (Acute hepatic failure), HP:0100626 (Chronic hepatic failure — for late sequelae), HP:0002583 (Gastrointestinal obstruction), HP:0002014-adjacent for hematochezia/melena, HP:0001744-adjacent for shock.

**Quality of life:** Acute survivors of severe poisoning may face long-term morbidity from hepatic injury or GI stricture requiring reconstructive surgery; specific validated QoL instrument data for iron-poisoning survivors was not identified in this search.

Sources: [WikEM: Iron toxicity](https://wikem.org/wiki/Iron_toxicity) · [Medscape: Pediatric Iron Toxicity](https://emedicine.medscape.com/article/1011689-overview) · [Radiology: Fibrous Stricture of the Stomach Due to Iron (Feosol) Poisoning](https://pubs.rsna.org/doi/10.1148/71.5.732) · [PubMed: Gastrointestinal pathology in adult iron overdose (PMID:2231830)](https://pubmed.ncbi.nlm.nih.gov/2231830/) · [PMC: Liver Transplantation for Acute Hepatic Failure Following Intentional Iron Overdose](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10699863/) · [Tennessee Poison Center: Delayed manifestations of iron poisoning](https://www.vumc.org/poison-control/node/927)

---

## 4. Genetic/Molecular Information

Iron poisoning is **not a Mendelian genetic disease**; it has no causal gene in the OMIM/ClinVar sense. There are no pathogenic variants, no inheritance pattern, and no chromosomal abnormalities associated with the exposure itself.

**Relevant molecular target/pathway genes (not causal, but mechanistically involved in toxicity/handling):**
- **TF (transferrin)** — plasma iron-binding protein; saturation of TF binding capacity (normally 20–35% saturated) is the threshold event producing non-transferrin-bound iron (NTBI) toxicity
- **SLC40A1 (ferroportin)** — cellular iron export
- **FTH1/FTL (ferritin heavy/light chain)** — intracellular iron storage/sequestration; ferritin destruction is implicated as a source of catalytic free iron in iron-mediated hepatocyte injury (paralleling acetaminophen hepatotoxicity mechanisms)
- **HFE** — theoretically could modulate baseline transferrin saturation/absorption but is not established as a modifier of acute poisoning severity in the literature surveyed

**Epigenetics/somatic considerations:** Not applicable — this is an acute exogenous toxic exposure, not a heritable or somatic-mutation disease.

Sources: [PMC: Iron Load Toxicity in Medicine — Molecular and Cellular Aspects](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10454416/) · [PMC: Non-Transferrin-Bound Iron (NTBI), Labile Plasma Iron (LPI), and Iron Toxicity](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12249652/) · [ScienceDirect: Iron mediated toxicity and programmed cell death](https://www.sciencedirect.com/science/article/pii/S0167488916303275)

---

## 5. Environmental Information

**Primary environmental/exposure factors:**
- Iron-containing oral dietary supplements: ferrous sulfate, ferrous gluconate, ferrous fumarate, carbonyl iron, prenatal multivitamins
- Product form and elemental-iron density (adult-strength tablets vs. pediatric chewables) — a major determinant of exposure severity
- Household storage practices and accessibility to young children
- Packaging regulation status (unit-dose blister packaging vs. bulk bottles)

**Behavioral/lifestyle factors:**
- Deliberate self-poisoning (intentional overdose), disproportionately among adolescent and young adult females — the dominant severe-poisoning mechanism in the adult population
- Caregiver perception of supplements as "safe," reducing protective vigilance

**Infectious agents:** Not applicable — iron poisoning is a chemical/toxicologic, not infectious, process.

Suggested exposure-ontology grounding (ECTO-style): "exposure to iron salts via ingestion" / "ferrous sulfate ingestion."

Sources: [AAP: Accidental Iron Poisoning in Children](https://publications.aap.org/pediatrics/article/24/3/399/40614/Accidental-Iron-Poisoning-in-Children-Report-of) · [SAGE: Iron Packaging Regulations in the United States and Pediatric Morbidity](https://journals.sagepub.com/doi/abs/10.1177/0009922819901010)

---

## 6. Mechanism / Pathophysiology

**Causal chain (initial trigger → clinical manifestation):**

1. **Ingestion of excess elemental iron** → normal intestinal mucosal regulatory mechanisms (which limit absorption under physiologic conditions) are overwhelmed by supratherapeutic dose.
2. **Direct corrosive mucosal injury** — iron salts act as a direct GI irritant/corrosive, producing hemorrhagic gastritis/enteritis, mucosal necrosis, and erosion (Stage I phenotype). *"Iron promotes direct mucosa irritation and at the intracellular level favors free radical production, oxidative damage, hinders oxidative phosphorylation, and ultimately causes cell death"* ([ScienceDirect: Iron Poisoning overview](https://www.sciencedirect.com/topics/pharmacology-toxicology-and-pharmaceutical-science/iron-poisoning)).
3. **Systemic absorption and saturation of plasma protein binding** — once transferrin's iron-binding capacity is exceeded (pathologically detectable when transferrin saturation exceeds ~75%), **non-transferrin-bound iron (NTBI)** appears in plasma; its redox-active, chelatable fraction is termed **labile plasma iron (LPI)**. NTBI/LPI enter cells via transporters outside normal transferrin-receptor-mediated regulation, bypassing cellular iron homeostasis controls.
4. **Cellular/mitochondrial toxicity** — free iron concentrates in mitochondria and catalyzes **Fenton-type reactions**, generating reactive oxygen species (ROS) that cause lipid peroxidation of mitochondrial membranes, **uncoupling oxidative phosphorylation**, and disrupting the electron transport chain. This is mechanistically convergent with **ferroptosis** — an iron-dependent regulated cell-death pathway involving glutathione/GPX4 depletion and lipid-peroxide accumulation, a mechanism well-characterized in iron-catalyzed acetaminophen hepatotoxicity and increasingly recognized as relevant to iron-overdose hepatocyte injury.
5. **Metabolic acidosis** — arises from two convergent mechanisms: (a) impaired oxidative phosphorylation → anaerobic metabolism → lactic acidosis; (b) when plasma protein-binding capacity is saturated, ferric iron hydrolyzes with water to form iron hydroxide and free H⁺ ions, directly compounding acidosis.
6. **Coagulopathy** — non-transferrin-bound Fe³⁺ (and its hydrolytic species) **reversibly inhibits serine proteases of the coagulation cascade**: thrombin's fibrinogen-clotting and fibrinopeptide-A-generating activity is markedly suppressed, as is factor Xa and kallikrein activity. This effect is reversible with iron chelation (EDTA in vitro), and is distinct from the coagulopathy of established hepatic synthetic failure — both mechanisms can coexist in severe poisoning.
7. **Hepatotoxicity** — the liver, as the first-pass site of portal-venous iron delivery and major iron-storage organ, sustains direct mitochondrial/oxidative injury, potentially progressing to fulminant hepatic failure (Stage IV) requiring transplantation in severe/intentional overdoses.
8. **Cardiovascular collapse/shock** — from combined hypovolemia (GI fluid/blood loss), direct iron-mediated myocardial and vascular endothelial toxicity, and acidosis-driven cardiac dysfunction; this is the dominant cause of death in Stage III.
9. **Delayed structural sequelae** — the initial corrosive mucosal injury heals by fibrotic scarring, which can mechanically obstruct the gastric outlet or proximal small bowel weeks later (Stage V).

**Cell types/tissues implicated:** gastrointestinal mucosal epithelial cells (enterocytes, gastric mucosa), hepatocytes, cardiomyocytes/vascular endothelium, and — at the molecular level — mitochondria across affected cell types.

**Suggested GO terms:** GO:0006879 (cellular iron ion homeostasis), GO:0055072 (iron ion homeostasis), GO:0034614 (cellular response to reactive oxygen species), GO:0006749 (glutathione metabolic process), GO:0034599 (cellular response to oxidative stress), GO:0006119 (oxidative phosphorylation), GO:0097267 (omega-hydroxylase P450 pathway — n/a), GO:1990448 (ferroptosis-related term where available, e.g., GO:0097707 "ferroptosis").

**Suggested CHEBI terms:** CHEBI:18248 (iron atom/ion), CHEBI:29033 (Fe(II) ion), CHEBI:29034 (Fe(III) ion), CHEBI:75771 (ferrous sulfate), CHEBI:75832 (ferrous gluconate).

Sources: [PMID:8187690 — Acute iron poisoning](https://pubmed.ncbi.nlm.nih.gov/8187690/) · [PMC: Iron Load Toxicity in Medicine](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10454416/) · [PMC: Role of Mitochondrial Iron Uptake in Acetaminophen Hepatotoxicity](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11567147/) · [PubMed: Ferroptosis and Intrinsic Drug-induced Liver Injury (PMID:39649034)](https://pubmed.ncbi.nlm.nih.gov/39649034/) · [PubMed: Blood coagulation and acute iron toxicity — reversible iron-induced inactivation of serine proteases (PMID:6421970)](https://pubmed.ncbi.nlm.nih.gov/6421970/) · [PMC: Oxidation Inhibits Iron-Induced Blood Coagulation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3580830/) · [PMC: Non-Transferrin-Bound Iron, Labile Plasma Iron, and Iron Toxicity](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12249652/)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** stomach and small intestine (direct corrosive injury); liver (systemic iron trapping and hepatotoxicity)
- **Secondary/complication-related:** cardiovascular system (shock), kidneys (acute kidney injury secondary to hypoperfusion), coagulation system (functional coagulopathy)
- **Body systems:** digestive, hepatobiliary, cardiovascular, hematologic

**Tissue/cell level:**
- Gastric and intestinal mucosal epithelium (erosion, hemorrhagic necrosis)
- Hepatocytes (oxidative/mitochondrial injury, necrosis, fulminant failure)
- Vascular endothelium (increased permeability contributing to shock)
- Cardiomyocytes (direct toxic and hypoperfusion-related injury)

**Subcellular level:** mitochondria (site of iron concentration, ROS generation, oxidative-phosphorylation uncoupling); cell membranes (lipid peroxidation target)

**Suggested UBERON terms:** UBERON:0000945 (stomach), UBERON:0002108 (small intestine), UBERON:0002107 (liver), UBERON:0000948 (heart), UBERON:0002113 (kidney), UBERON:0001969 (blood plasma).

**Suggested GO Cellular Component terms:** GO:0005739 (mitochondrion), GO:0016020 (membrane).

Sources: [PubMed: Gastrointestinal pathology in adult iron overdose (PMID:2231830)](https://pubmed.ncbi.nlm.nih.gov/2231830/) · [Radiology: Fibrous Stricture of the Stomach Due to Iron Poisoning](https://pubs.rsna.org/doi/10.1148/71.5.732)

---

## 8. Temporal Development

**Onset:** Acute — symptoms typically begin within 30 minutes to 6 hours of ingestion (Stage I); onset pattern is acute/toxic rather than insidious, dose-dependent in latency and severity.

**Progression (staged, as above):**
- Stage I (0–6 h): corrosive GI phase
- Stage II (6–24 h): latent/deceptive improvement
- Stage III (24–48+ h): shock/metabolic decompensation — responsible for the majority of deaths
- Stage IV (2–5 days): hepatotoxicity/hepatic failure
- Stage V (2–8 weeks): GI stricture/obstruction

Not all patients progress through every stage; a patient with a small ingestion may resolve after Stage I, while patients with massive ingestion can rapidly develop multi-organ failure and death within the first 24–48 hours without ever exhibiting a clear "latent" phase.

**Disease course pattern:** Self-limited (in mild ingestions) to rapidly progressive/fulminant (in severe ingestions), with a distinct **delayed structural complication window** (weeks) that is atypical among acute poisonings and requires specific counseling/follow-up.

**Critical period for intervention:** Early recognition and chelation (ideally initiated in Stage I–II, before shock/organ failure) is the key modifiable window — *"[Deferoxamine] greatly reduces mortality in children, provided it is given at an early stage"* ([ScienceDirect: Deferoxamine overview](https://www.sciencedirect.com/science/article/abs/pii/S1357303907003106)).

Sources: [Medscape: Pediatric Iron Toxicity](https://emedicine.medscape.com/article/1011689-overview) · [EM Board Bombs: A Rusty Diagnosis — Acute Iron Poisoning](https://www.emboardbombs.com/study-guide/2021-9-12-a-rusty-diagnosis-acute-iron-poisoning-9et2j/) · [Tennessee Poison Center: Delayed manifestations of iron poisoning](https://www.vumc.org/poison-control/node/927)

---

## 9. Inheritance and Population

**Epidemiology (US, AAPCC data):**
- **2022:** 5,311 single exposures to iron/iron salts reported to US poison control centers — 2,154 in children <6 years, 209 in children 6–12 years, 762 in adolescents 13–19 years; **2 deaths** reported. An additional 7,565 single exposures to iron-containing multivitamins were reported, 81% in children <6 years.
- **Historical incidence:** ~11,000 iron exposures per year in US children <6 years old (2015 AAPCC data)
- **Mortality trend:** From 1983–2000, at least 43 US children died from iron supplement ingestion; from 1983–1991, iron accounted for >30% of deaths from unintentional pediatric drug-product ingestion. Fatal pediatric iron ingestions have **declined markedly since the 1990s**, coincident with unit-dose packaging/labeling regulation (1997 FDA rule) — one pediatric iron-poisoning death reported 1998–2002 following the regulation.

**Inheritance pattern:** Not applicable — iron poisoning is an acquired toxic exposure, not an inherited disease. No penetrance, expressivity, anticipation, mosaicism, founder-effect, or carrier-frequency concepts apply.

**Population demographics:**
- **Unintentional poisoning:** overwhelmingly children <5 years old ingesting adult-formulation iron products
- **Intentional/severe poisoning:** predominantly adolescent and young adult **females** attempting self-harm — the dominant mechanism behind severe/fatal adult cases described in case series (e.g., five fatal cases of suicidal ingestion of 20–60 iron/iron-folic tablets in adolescent females, with autopsy findings of multi-organ petechial hemorrhage, GI mucosal necrosis/erosion)
- **Sex ratio:** skewed toward young children of either sex for unintentional exposures; skewed toward females for intentional adult/adolescent poisoning
- **Geographic distribution:** Reported globally; incidence and severity strongly modulated by product-packaging regulation, healthcare access, and cultural availability of iron supplements (notably relevant in regions with widespread maternal iron-supplementation programs)

Sources: [UpToDate: Acute iron poisoning](https://www.uptodate.com/contents/acute-iron-poisoning) · [Medscape: Pediatric Iron Toxicity](https://emedicine.medscape.com/article/1011689-overview) · [PubMed: Unit-dose packaging of iron supplements (PMID:15939855)](https://www.ncbi.nlm.nih.gov/pubmed/15939855) · [Journal of Population Therapeutics and Clinical Pharmacology: Suicidal Acute Iron Poisoning in Adolescent Females — A Case Series](https://jptcp.com/index.php/jptcp/article/view/2366) · [PMC: Fatal Iron Toxicity in an Adult — Clinical Profile and Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC6259445/)

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Serum iron level** (peak, typically drawn 2–6 h post-ingestion): correlates with severity —
  - <300 µg/dL: mild/unlikely severe toxicity
  - 300–500 µg/dL: mild toxicological effects
  - 500–1000 µg/dL: moderate-to-severe toxicity (500 µg/dL is a classic threshold indication for deferoxamine)
  - >1000 µg/dL: death is common
- **Total iron-binding capacity (TIBC)** — historically used but now considered unreliable in acute overdose (assay interference)
- **Serum glucose and WBC count** — elevated values (glucose >150 mg/dL, WBC >15,000/µL) have been proposed as early surrogate markers correlating with significant ingestion, though sensitivity/specificity are limited
- **Arterial/venous blood gas** — assesses metabolic (anion-gap) acidosis, a marker of systemic toxicity severity
- **Coagulation studies (PT/INR, PTT, fibrinogen)** — assess iron-induced serine-protease inhibition and/or hepatic synthetic coagulopathy
- **Liver function tests** — for Stage IV hepatotoxicity surveillance
- **Abdominal X-ray (KUB)** — iron tablets are **radiopaque**; a positive film supports the diagnosis and guides need for whole bowel irrigation (WBI), though a negative film does not exclude significant ingestion (chewable/liquid formulations may not be radiopaque, and tablets may already have dissolved)

**Diagnostic/clinical criteria:** No formal DSM/ICD diagnostic-criteria instrument; diagnosis is clinical (history of ingestion + staged symptom pattern) supported by serum iron level and imaging.

**Differential diagnosis:** Other causes of anion-gap metabolic acidosis and toxic ingestion (salicylates, ethylene glycol, methanol), other causes of hematemesis/corrosive GI injury (caustic ingestion, NSAID gastropathy), sepsis/septic shock (can mimic Stage III), other causes of fulminant hepatic failure (acetaminophen, viral hepatitis).

**Genetic testing:** Not applicable/not indicated (no causal genetic variant).

**Screening:** No population screening program exists (this is an acute poisoning, not a chronic/heritable condition); the relevant "screening" analog is regulatory/product-based prevention (packaging, labeling) rather than clinical genetic or biochemical screening.

Suggested NCIT/LOINC anchors: serum iron (LOINC 2498-4), TIBC (LOINC 2500-7), abdominal X-ray (a radiologic procedure, NCIT-codable).

Sources: [Medscape: Iron Toxicity — Workup](https://emedicine.medscape.com/article/815213-overview) · [California Poison Control: Iron Ingestion](https://www.rchsd.org/documents/2014/02/iron-ingestion.pdf/) · [Iron Ingestion: Evidence-Based Consensus Guideline for Out-of-Hospital Management](https://www.tandfonline.com/doi/full/10.1081/CLT-200068842)

---

## 11. Outcome / Prognosis

**Mortality:** With prompt recognition and treatment, outcomes for mild-to-moderate unintentional pediatric ingestions are generally good, and fatal pediatric ingestions have declined substantially since packaging/labeling regulation. However, severe (typically intentional, high-dose) ingestions carry substantial mortality: *"A majority of acute iron toxicity cases [reaching severe multi-organ involvement] are fatal given the rapid progression to multi-organ failure"* in reported case series, and reported US poison-control mortality remained at 2 deaths in 2022 among >5,300 reported iron exposures.

**Morbidity:**
- Acute survivors of Stage III/IV disease may have prolonged ICU courses, need for liver transplantation in fulminant hepatic failure, and dialysis for acute kidney injury.
- Delayed morbidity: gastric outlet obstruction/intestinal stricture (Stage V) can require reconstructive GI surgery (pyloroplasty, gastrojejunostomy, gastric resection) weeks to months after the acute event.

**Prognostic factors:** Elemental iron dose ingested, peak serum iron level, time-to-treatment (chelation), presence/severity of metabolic acidosis and shock at presentation, and development of hepatic failure.

**Recovery potential:** Generally favorable with early deferoxamine chelation in symptomatic-but-not-yet-shocked patients; poor once fulminant hepatic failure or refractory shock/coagulopathy develop.

Sources: [PMC: Fatal Iron Toxicity in an Adult — Clinical Profile and Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC6259445/) · [PMC: Liver Transplantation for Acute Hepatic Failure Following Intentional Iron Overdose](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10699863/) · [PubMed: Suicidal iron overdose — case report and review of literature](https://pubmed.ncbi.nlm.nih.gov/33729557/)

---

## 12. Treatment

**Initial/supportive management:**
- Aggressive **IV fluid resuscitation** for hypovolemia/shock
- **Correction of metabolic acidosis** and electrolyte abnormalities
- **Whole bowel irrigation (WBI)** with polyethylene glycol solution (adults: 1–2 L/h; children: 25–40 mL/kg/h) when radiopaque tablets are visible on abdominal X-ray, continued until the film clears — though *"existing data are still insufficient to support or exclude its efficacy"* rigorously, it remains standard practice for radiographically confirmed significant ingestions.
- **Activated charcoal is NOT effective** — it does not adsorb iron and should be given only if co-ingestants are suspected; concurrent WBI may further reduce charcoal's efficacy for those co-ingestants.
- Endoscopic removal or, rarely, **gastrotomy** for large iron tablet bezoars/masses not clearable by WBI

**Pharmacotherapy — chelation:**
- **Deferoxamine (desferrioxamine)** — the mainstay/first-line chelator for **acute** iron poisoning. Mechanism: high affinity for ferric (Fe³⁺) iron, forming the stable octahedral complex **ferrioxamine**, 1:1 molar binding, which is renally excreted (producing the classic "vin rosé"/rusty-red urine). Indications for IV infusion: significant clinical toxicity signs, metabolic acidosis, shock, serum iron >500 µg/dL, and/or radiographically visible tablet burden. Dosing: IV infusion starting at 15 mg/kg/h (not exceeding 1 g/h), typically over 6 hours with reassessment; hypotension is the main dose-limiting adverse effect, mitigated by ensuring adequate hydration first.
- **Oral chelators (deferiprone, deferasirox)** — primarily used for *chronic* transfusional iron-overload states (e.g., thalassemia), not first-line for acute poisoning, though deferiprone has shown efficacy in **animal models of acute iron overdose** (decreased morbidity/mortality in rats) and limited human case reports (efficacy of oral deferiprone in acute iron poisoning) — these remain investigational/adjunctive for acute toxicology, with deferoxamine as standard of care given cost/access limitations of parenteral therapy being the main barrier globally.

**Surgical/interventional:**
- Late complications (gastric outlet obstruction, pyloric/small-bowel stricture) may require surgical correction: Mikulicz (Heineke-Mikulicz) pyloroplasty, gastrojejunostomy, or gastric resection with Billroth I anastomosis.
- **Liver transplantation** for fulminant hepatic failure refractory to medical management (reported in severe intentional overdoses).

**Supportive/rehabilitative care:** ICU-level monitoring, correction of coagulopathy (FFP/blood products as needed), dialysis for renal failure, nutritional support post-surgical GI reconstruction.

**Experimental:** Deferiprone as an oral alternative/adjunct for acute poisoning remains under investigation, particularly attractive in resource-limited settings lacking IV deferoxamine access.

**Treatment outcomes/adverse events:** Deferoxamine-induced hypotension (rate-related); rare deferoxamine-associated ARDS with prolonged high-dose infusion (a recognized but not detailed-in-this-search complication historically reported in the toxicology literature).

**Suggested NCIT terms:** NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` bound to CHEBI (deferoxamine — CHEBI:4058) or NCIT (deferoxamine, deferiprone, deferasirox); NCIT:C15329 (Surgical Procedure) for pyloroplasty/gastrojejunostomy/gastric resection; NCIT:C15289 (Organ Transplantation) for liver transplant; a WBI/decontamination procedure term (gastrointestinal decontamination) if a suitable NCIT concept exists.

Sources: [ScienceDirect: Deferoxamine overview](https://www.sciencedirect.com/science/article/abs/pii/S1357303907003106) · [Merck Manual: Iron Poisoning](https://www.merckmanuals.com/professional/injuries-poisoning/poisoning/iron-poisoning) · [Medscape: Pediatric Iron Toxicity Treatment & Management](https://emedicine.medscape.com/article/1011689-treatment) · [PubMed: The efficacy of oral deferiprone in acute iron poisoning](https://pubmed.ncbi.nlm.nih.gov/10674529/) · [PMC: Management of Acute Ferrous Sulfate Poisoning Using Activated Charcoal Monotherapy: A Case Report](https://pmc.ncbi.nlm.nih.gov/articles/PMC10766004/) · [PubMed: Gastrotomy and whole bowel irrigation in iron poisoning](https://pubmed.ncbi.nlm.nih.gov/1754488/) · [PMC: A Review on Iron Chelators in Treatment of Iron Overload Syndromes](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5139945/)

---

## 13. Prevention

**Primary prevention:**
- **Unit-dose (blister) packaging** for iron-containing supplements/drugs with ≥30 mg elemental iron per dosage unit — mandated by 1997 FDA rule; associated with a marked drop in pediatric iron-poisoning deaths (reduced to essentially one reported US pediatric death 1998–2002). Note: the unit-dose *packaging* mandate was later **withdrawn in 2003** following *Nutritional Health Alliance v. FDA*, which held the FDCA did not authorize FDA to regulate packaging specifically for poison prevention purposes — though label warning-statement requirements persisted.
- Child-resistant containers (general Poison Prevention Packaging Act mechanisms)
- Safe storage counseling for caregivers, particularly regarding prenatal vitamins and adult-strength ferrous sulfate

**Secondary prevention:**
- Early recognition and prompt poison-control/ED evaluation after any known or suspected iron ingestion in a child, given the deceptive Stage II latent period
- Abdominal radiography to assess ingestion burden and guide decontamination

**Behavioral/public health interventions:**
- Poison control center public-awareness campaigns (e.g., 1-800 poison helpline)
- Label warning statements on iron-containing products (bright-color tablet warnings, "keep out of reach of children")
- For adolescent/adult intentional-ingestion risk: mental health screening and access-restriction counseling in at-risk populations (given the demographic skew toward young female self-harm)

**Screening:** No genetic/biochemical population screening applies; the closest analog is regulatory product-safety oversight rather than clinical screening.

Sources: [FDA: Guidance for Industry — Iron-Containing Supplements and Drugs: Label Warning](https://downloads.regulations.gov/FDA-1997-D-0056-0004/attachment_1.pdf) · [Federal Register: Iron-Containing Supplements and Drugs; Removal of Unit-Dose Packaging Requirements](https://www.federalregister.gov/documents/2003/10/17/03-26188/iron-containing-supplements-and-drugs-label-warning-statements-and-unit-dose-packaging-requirements) · [SAGE Journals: Iron Packaging Regulations in the United States and Pediatric Morbidity](https://journals.sagepub.com/doi/abs/10.1177/0009922819901010)

---

## 14. Other Species / Natural Disease

Acute iron toxicity is well documented as an **induced/experimental toxicology model** rather than a naturally occurring veterinary disease entity in the OMIA sense. Relevant cross-species data:

- **Rats:** LD50 estimates for ferrous sulfate vary widely by study — approximately 780–1,100 mg iron/kg body weight in one estimate, and up to 2.8 g/kg in another; ferrous sulfate heptahydrate showed no acute toxicity up to 2,000 mg/kg in some OECD-guideline studies. Comparator salts: ferrous chloride oral LD50 300–2,000 mg/kg (132–881 mg Fe/kg); ferric sulfate oral LD50 500–2,000 mg/kg (females). Repeated-dose/reproductive-developmental toxicity of ferrous sulfate heptahydrate has been assessed at 30–1,000 mg/kg/day in OECD combined study designs.
- **Mice:** Used in classic iron-toxicity determination studies (e.g., "Determination of Iron Toxicity in Mice," ScienceDirect).
- **Young rats:** Comparative acute toxicity of carbonyl iron and sodium iron EDTA vs. ferrous sulfate has been specifically studied, relevant to formulating safer pediatric iron products (carbonyl iron shows a substantially better safety margin than ferrous sulfate in this context).
- **Veterinary relevance:** Accidental iron-supplement ingestion (e.g., companion animals ingesting human iron tablets/prenatal vitamins) is a recognized veterinary toxicology concern, paralleling the pediatric human scenario, though detailed OMIA/VetCompass-specific case data were not retrieved in this search.

**Comparative biology:** The core toxic mechanism — mucosal corrosion, NTBI-driven oxidative/mitochondrial injury, and coagulation-factor inhibition — is conserved across mammalian species, supporting rodent models as reasonably translatable for acute-toxicity dose-response and chelator-efficacy studies (e.g., deferiprone efficacy data derived from rat acute-overdose models).

**Suggested NCBITaxon terms:** NCBITaxon:9606 (Homo sapiens), NCBITaxon:10116 (Rattus norvegicus), NCBITaxon:10090 (Mus musculus).

Sources: [OECD SIDS Initial Assessment Profile — Ferrous compounds](https://hpvchemicals.oecd.org/ui/handler.axd?id=71ff3b32-63bb-40b5-940d-d378879d209f) · [ResearchGate: Acute Toxicity of Carbonyl Iron and Sodium Iron EDTA Compared with Ferrous Sulfate in Young Rats](https://www.researchgate.net/publication/10999326_Acute_Toxicity_of_Carbonyl_Iron_and_Sodium_Iron_EDTA_Compared_with_Ferrous_Sulfate_in_Young_Rats) · [ScienceDirect: Determination of Iron Toxicity in Mice](https://www.sciencedirect.com/science/article/abs/pii/S0022354915350218)

---

## 15. Model Organisms

**Rodent models (rat, mouse):** The dominant experimental system for acute iron-toxicity research — used to establish LD50/dose-response relationships for various iron salts (ferrous sulfate, ferrous chloride, ferric sulfate, carbonyl iron, sodium iron EDTA), and to test chelator efficacy. Notably, **oral deferiprone reduced morbidity and mortality in rat models of acute iron overdose**, directly informing the human investigational use described above (§12).

**Model characteristics:**
- Recapitulates key phenotypes: GI mucosal injury, systemic organ toxicity, mortality dose-dependence
- Used to compare relative toxicity/safety margins of different iron formulations (informing safer pediatric supplement formulation design, e.g., carbonyl iron vs. ferrous sulfate)
- Used for OECD-guideline repeated-dose and reproductive/developmental toxicity screening of iron salts

**Limitations:** Rodent GI anatomy/physiology and dosing-route pharmacokinetics differ from humans; LD50 estimates vary substantially between studies/rodent strains/iron salt forms, complicating direct extrapolation of a single "lethal dose" figure to humans (human thresholds are instead derived largely from case-series/poison-control data rather than allometric scaling from animal LD50s).

**Applications:** Dose-response characterization, chelator (deferoxamine, deferiprone) efficacy and pharmacokinetic testing, comparative formulation safety (carbonyl iron vs. ferrous salts) to inform pediatric product design and regulatory policy.

**Resources:** No dedicated genetically engineered (knockout/transgenic) mouse model is relevant here, since this is a toxic-exposure phenotype rather than a genetic disease — models are induced (dosing) rather than genetic.

Sources: [PubMed: The efficacy of oral deferiprone in acute iron poisoning](https://pubmed.ncbi.nlm.nih.gov/10674529/) · [ResearchGate: Acute Toxicity of Carbonyl Iron and Sodium Iron EDTA Compared with Ferrous Sulfate in Young Rats](https://www.researchgate.net/publication/10999326_Acute_Toxicity_of_Carbonyl_Iron_and_Sodium_Iron_EDTA_Compared_with_Ferrous_Sulfate_in_Young_Rats) · [OECD SIAM: Ferrous compounds SIDS assessment](https://hpvchemicals.oecd.org/ui/handler.axd?id=71ff3b32-63bb-40b5-940d-d378879d209f)

---

## Summary of Key Ontology Term Suggestions

| Category | Terms |
|---|---|
| **HPO** | HP:0002013 Vomiting, HP:0002014 Diarrhea, HP:0002027 Abdominal pain, HP:0001649 Tachycardia, HP:0001257 Lethargy, HP:0011900 Metabolic acidosis, HP:0001928 Abnormal coagulation, HP:0006554 Acute hepatic failure, HP:0002583 GI obstruction |
| **GO (BP)** | GO:0055072 iron ion homeostasis, GO:0034614 cellular response to ROS, GO:0034599 cellular response to oxidative stress, GO:0006119 oxidative phosphorylation, GO:0097707 ferroptosis |
| **GO (CC)** | GO:0005739 mitochondrion |
| **CL** | Gastric/intestinal mucosal epithelial cell, hepatocyte, cardiomyocyte |
| **UBERON** | UBERON:0000945 stomach, UBERON:0002108 small intestine, UBERON:0002107 liver, UBERON:0000948 heart |
| **CHEBI** | CHEBI:29033 Fe(II), CHEBI:29034 Fe(III), CHEBI:75771 ferrous sulfate, CHEBI:4058 deferoxamine |
| **NCIT** | NCIT:C15986 Pharmacotherapy (deferoxamine), NCIT:C15329 Surgical Procedure, NCIT:C15289 Organ Transplantation |
| **NCBITaxon** | NCBITaxon:9606 (human), NCBITaxon:10116 (rat), NCBITaxon:10090 (mouse) |

---

### Notes on evidence gaps
This report identified no MONDO/OMIM identifier specifically dedicated to acute iron poisoning as distinct from chronic iron-overload disorders — a curator populating a dismech-style entry should likely model this as an **environmental/toxic-exposure disease entity** (paralleling entries like Arsenic_Poisoning) rather than force-fitting it to a hereditary-iron-overload MONDO branch. Quantitative QoL data, detailed genetic-modifier studies, and single-cell/omics profiling specific to acute iron poisoning were not found and are likely genuinely sparse in the literature (this is predominantly a clinical-toxicology/emergency-medicine literature base rather than a molecular-genetics one).

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.