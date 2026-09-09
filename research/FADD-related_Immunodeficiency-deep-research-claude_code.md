---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-24T16:15:06.553722'
end_time: '2026-08-24T16:19:06.936769'
duration_seconds: 240.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: FADD-Related Immunodeficiency
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
  web_search_requests: 19
  num_turns: 26
  total_cost_usd: 1.5005385999999998
  session_id: d5430dc8-cc9c-5a8f-9365-64cb735827c4
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 9
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 6
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** FADD-Related Immunodeficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FADD-Related Immunodeficiency** covering all of the
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

I'll research FADD-Related Immunodeficiency now using web search and fetch tools, then compile a comprehensive report.

I now have sufficient material to compile the comprehensive report.

I have gathered comprehensive data. Here is the full research report.

# FADD-Related Immunodeficiency (Immunodeficiency-90 with Encephalopathy, Hepatic Dysfunction, and Cardiovascular Malformations, IMD90)

## 1. Disease Information

**Overview:** FADD-related immunodeficiency (also termed FADD deficiency or Immunodeficiency-90 with encephalopathy, functional hyposplenia, and hepatic dysfunction, IMD90) is an ultra-rare autosomal recessive primary immunodeficiency/immune dysregulation disorder caused by biallelic loss-of-function variants in *FADD* (Fas-associated protein with death domain), the central adaptor protein of the death-inducing signaling complex (DISC) in extrinsic apoptosis. It presents a phenotype that partially overlaps with autoimmune lymphoproliferative syndrome (ALPS) — impaired Fas-mediated lymphocyte apoptosis and elevated double-negative T cells — but is clinically distinct, combining recurrent severe bacterial and viral infections, functional hyposplenism, recurrent hepatopathy, and characteristic stereotyped febrile encephalopathic episodes with refractory seizures, sometimes meeting criteria for febrile infection-related epilepsy syndrome (FIRES). It was first molecularly characterized in 2010 via combined genome-wide linkage analysis and whole-exome sequencing (Bolze et al., *Am J Hum Genet* 2010;87(6):873–881, PMID:21109225) [omim.org](https://www.omim.org/entry/613759).

**Key identifiers:**
- OMIM phenotype: #613759 (IMMUNODEFICIENCY 90 WITH ENCEPHALOPATHY, FUNCTIONAL HYPOSPLENIA, AND HEPATIC DYSFUNCTION; IMD90) [omim.org](https://www.omim.org/entry/613759)
- OMIM gene: *602457 (FAS-ASSOCIATED VIA DEATH DOMAIN; FADD) [omim.org](https://omim.org/entry/602457)
- MONDO: MONDO:0013408 [thegencc.org](https://thegencc.org/genes/HGNC:3573)
- HGNC: 3573 (gene symbol FADD, also known as MORT1, GIG3) [genecards.org](https://www.genecards.org/cgi-bin/carddisp.pl?gene=FADD)
- Gene location: chromosome 11q13.3 [atlasgeneticsoncology.org](https://atlasgeneticsoncology.org/Genes/GC_FADD.html)
- Orphanet, GARD (NIH rare disease portal): "FADD-related immunodeficiency" [rarediseases.info.nih.gov](https://rarediseases.info.nih.gov/diseases/15004/fadd-related-immunodeficiency); also listed under NORD [rarediseases.org](https://rarediseases.org/mondo-disease/fadd-related-immunodeficiency/)
- NCBI GTR condition: C3151062 [ncbi.nlm.nih.gov](https://www.ncbi.nlm.nih.gov/gtr/conditions/C3151062/)
- Protein: UniProt Q13158, 208 amino acids, ~23.3 kDa [genecards.org](https://www.genecards.org/cgi-bin/carddisp.pl?gene=FADD)

**Synonyms:** FADD deficiency; MORT1 deficiency; IMD90; ALPS-like disease due to FADD deficiency.

**Evidence basis:** All published clinical information derives from aggregated case reports/case series (fewer than ~15 patients described worldwide across at least 8 published articles as of 2023–2024), not large cohort or EHR-derived data — a hallmark of an ultra-rare Mendelian disorder [figshare.com dataset cited via search](https://figshare.com/articles/dataset/Dataset_of_FADD_Deficiency_Cases/28330997).

---

## 2. Etiology

**Primary cause:** Biallelic (homozygous or compound heterozygous) pathogenic variants in *FADD*, encoding the sole adaptor protein that couples activated death receptors (FAS/CD95, TNFR1) to initiator caspases-8/-10, causing partial loss of FADD protein function/expression.

### Reported causal variants
| Variant | Zygosity | Patients | Source |
|---|---|---|---|
| c.315C>G / p.C105W (missense) | Homozygous | Original 3 affected members of a large consanguineous Pakistani kindred (not found in 282 Pakistani controls) | Bolze et al. 2010, PMID:21109225 [omim.org](https://www.omim.org/entry/613759) |
| c.313T>C / p.C105R (missense, novel) | Compound heterozygous (with a truncating allele) | 1 US infant (BJH-reported family) | Setia et al. 2023, PMID:37199216 |
| c.52_58delGACGAGC (7-bp deletion, frameshift/truncating) | Compound heterozygous (paternal allele c.313T>C) | Same infant as above | Setia et al. 2023 |
| Other compound heterozygous variants | Compound heterozygous | 2 patients (Journal of Clinical Immunology report) | PMID for "Novel Compound Heterozygote Variations..." *J Clin Immunol* 2020, PMC7253512 |
| Homozygous p.C105W | Homozygous | 1 patient presenting as FIRES | Giovannini et al. 2024, *Epilepsia* 65(7):e119–e124, DOI:10.1111/epi.18008 |

The C105 residue recurs across independent reports (C105W and C105R), suggesting it is a mechanistic hotspot in the death-effector domain (DED) region critical for DISC assembly. Both novel variants reported in 2023 are absent from gnomAD in the homozygous state, consistent with severe deleteriousness under purifying selection [pmc.ncbi.nlm.nih.gov summary via WebFetch].

**Risk factors:**
- **Genetic:** Consanguinity is a major risk factor — the founding kindred was a large consanguineous Pakistani family; homozygosity for rare deleterious *FADD* alleles is markedly more likely in consanguineous unions.
- **Environmental/infectious:** Because FADD deficiency causes functional hyposplenism and impaired interferon-mediated antiviral immunity, environmental infectious exposures (particularly encapsulated bacteria such as *Streptococcus pneumoniae*, and viruses including HHV-6) act as major disease-modifying/triggering factors for both the infectious and encephalopathic components of the phenotype.
- No protective genetic or environmental factors have been reported in the literature — the condition is too rare for population-level GWAS or protective-variant studies.

**Gene–environment interaction:** The stereotyped febrile encephalopathic episodes are typically precipitated by febrile illness/infection (in at least one reported case, immediately following MMR vaccination), implicating an infection- or immune-activation-triggered inflammatory/necroptotic cascade in genetically susceptible (FADD-deficient) neural or immune tissue as the proximate mechanism of the encephalopathy — consistent with a FIRES-like presentation.

---

## 3. Phenotypes

FADD deficiency phenotypes span immunologic, neurologic, hepatic, cardiac, splenic, and (recently recognized) ocular systems.

| Phenotype | Type | Onset | Frequency (qualitative, small case series) | Suggested HPO term |
|---|---|---|---|---|
| Recurrent severe bacterial infections (esp. invasive pneumococcal disease) | Clinical sign/symptom | Infancy | Frequent | HP:0002718 (Recurrent infections); HP:0006515 (Recurrent pneumonia) |
| Recurrent severe viral infections | Clinical sign/symptom | Infancy | Frequent | HP:0002719 |
| Functional hyposplenism (with Howell-Jolly bodies on smear) | Laboratory abnormality | Infancy/childhood | Frequent | HP:0001971 (Functional abnormality of the spleen); HP:0031913 (Howell-Jolly bodies) |
| Recurrent hepatopathy (portal inflammation, fibrosis) | Clinical sign / laboratory | Variable | Frequent | HP:0001395 (Hepatic fibrosis); HP:0001392 (Abnormal liver physiology) |
| Recurrent stereotyped febrile encephalopathic episodes with refractory seizures (some meeting FIRES criteria) | Symptom/clinical sign | Infancy–early childhood, episodic | Frequent, often the most severe/lethal feature | HP:0011146 (Encephalopathy); HP:0002373 (Febrile seizures); HP:0002373; HP:0032437 (encephalopathy episodes) |
| Cerebral atrophy | Imaging finding | Progressive with episodes | Reported in several cases | HP:0002059 |
| Cardiac malformations (ventricular septal defect, pulmonary artery atresia) | Structural anomaly | Congenital | Variable, reported subset | HP:0001629 (VSD); HP:0004935 (Pulmonary artery atresia) |
| Variable lymphadenopathy/splenomegaly | Clinical sign | Variable | Variable — milder than classic ALPS | HP:0002716 (Lymphadenopathy); HP:0001744 (Splenomegaly) |
| Increased double-negative (CD3+TCRαβ+CD4−CD8−) T cells | Laboratory abnormality | — | Consistent finding | HP:0040218 (double-negative T-lymphocytosis, ALPS-associated) |
| Elevated soluble Fas ligand (sFasL) | Laboratory abnormality | — | Consistent | (biomarker, no dedicated HPO term) |
| Elevated IL-10, IL-18 | Laboratory abnormality | — | Reported | — |
| Elevated vitamin B12 | Laboratory abnormality | — | Consistent, ALPS-like biomarker | HP:0040214 (elevated vitamin B12) |
| Ocular findings resembling familial exudative vitreoretinopathy (FEVR-like retinal vascular changes) | Clinical sign | Reported in 1 recent case | Newly described (2022) | HP:0000501 (Glaucoma)/HP:0025580 (Vitreoretinopathy) — closest match |
| Absence of appropriate isohemagglutinins despite normal immunoglobulin levels | Laboratory abnormality | — | Reported | HP:0025406 |

**Clinical course pattern:** Episodic/relapsing-remitting encephalopathic crises superimposed on a chronic background of infection susceptibility and hepatopathy; disease course is frequently rapidly fatal in early childhood (see Outcome section) but is variable-severity, as newer reports (2023–2024) describe milder or more indolent presentations and longer survival with active management [WebFetch of GARD/PMC summaries].

**Quality of life impact:** No formal QOL instrument data (EQ-5D, SF-36) exist for this ultra-rare condition; qualitative reports describe severe impact from recurrent hospitalization, status epilepticus, and, in survivors, chronic fatigue and recurrent respiratory infections managed with immunoglobulin replacement (subjective improvement in fatigue reported with subcutaneous IgG in the 2023 case).

---

## 4. Genetic/Molecular Information

- **Causal gene:** *FADD* (HGNC:3573; OMIM *602457), chromosome 11q13.3.
- **Variant classes reported:** missense (p.C105W, p.C105R) at a conserved cysteine residue implicated in DED structure/function, and a frameshift/truncating 7-bp deletion (c.52_58delGACGAGC) predicted to severely truncate the protein.
- **Population frequency:** No homozygous carriers of the reported pathogenic alleles are present in gnomAD, consistent with severe deleteriousness; the original p.C105W allele was absent from 282 ethnically matched Pakistani controls.
- **Functional consequence:** Reduced FADD protein expression and profoundly impaired Fas-mediated apoptosis in patient-derived cells ("profound deficiency in appropriate cell death" on functional apoptosis assay) — consistent with partial/hypomorphic loss of function rather than complete null (complete FADD loss is embryonic lethal in mice — see Model Organisms section), implying that surviving human patients likely carry hypomorphic alleles that retain some residual function.
- **Modifier genes:** None specifically established; phenotypic variability (e.g., presence/absence of cardiac malformations, ocular findings, severity of encephalopathy) across the small number of reported patients suggests possible modifier or stochastic effects, but this is not formally studied.
- **Somatic vs. germline:** All reported FADD deficiency variants are germline; no somatic FADD variants have been implicated (contrasting with somatic FAS variants seen in some ALPS).
- **Epigenetics/chromosomal abnormalities:** Not reported as a mechanism for FADD deficiency; not applicable. (Note: somatic 11q13.3 amplification involving FADD has separately been studied as an oncogenic driver in head and neck squamous cell carcinoma — a distinct cancer biology context, not part of the germline immunodeficiency disorder.)

**Protein structure:** FADD is a 208-amino-acid, ~23 kDa bipartite adaptor protein comprising an N-terminal death effector domain (DED, six-α-helix death-fold) and a C-terminal death domain (DD). Upon FAS/TNFR ligation, the receptor DD engages FADD's DD via homophilic interaction; FADD's DED then recruits procaspase-8/-10 DEDs to nucleate the death-inducing signaling complex (DISC), driving caspase-8/-10 activation and apoptosis execution [ncbi.nlm.nih.gov/PMC10970579; nature.com NMR structure Eberstadt et al.].

---

## 5. Environmental Information

- **Infectious triggers:** Febrile infectious illness is the principal recognized trigger for the encephalopathic crises; HHV-6 IgG elevation was documented in one recent case as the only infectious workup abnormality during an encephalopathic episode. Vaccination (MMR) preceded a fatal encephalopathic episode in an affected sibling in one family, though causality versus coincidental febrile trigger cannot be established from a single case.
- **No specific toxin, occupational, or lifestyle risk factors** have been identified — expected given the pediatric-onset, purely monogenic nature of the disease.
- **Bacterial pathogens of particular relevance:** encapsulated organisms, especially *Streptococcus pneumoniae*, causing invasive pneumococcal disease exploiting the functional hyposplenic state.

---

## 6. Mechanism / Pathophysiology

FADD deficiency illustrates a single adaptor-protein defect producing multi-system disease through at least three convergent, partially independent mechanistic arms:

### (a) Impaired Fas-mediated lymphocyte apoptosis → ALPS-like immune dysregulation
- FADD is obligate for DISC assembly downstream of FAS/CD95 ligation.
- Loss of function → failure of activation-induced cell death in T lymphocytes → accumulation of CD3+TCRαβ+CD4−CD8− double-negative T cells, elevated soluble FasL, IL-10, and vitamin B12 — the same biomarker panel used in classic ALPS (FAS/FASLG/CASP10 mutations) but **without** the massive lymphadenopathy/splenomegaly and overt autoimmune cytopenias that define clinical ALPS. Because of this partial phenotypic overlap, FADD deficiency is formally classified among the disorders in the expanding ALPS/ALPS-like spectrum, but functional Fas-apoptosis assay abnormality plus absence of FAS/FASLG/CASP10 mutation, together with the systemic (infectious/hepatic/encephalopathic) features, distinguishes it diagnostically [ncbi.nlm.nih.gov/books/NBK1108 GeneReviews ALPS].

### (b) Functional hyposplenism → bacterial infection susceptibility
- FADD-deficient patients show a functional (not anatomic) hyposplenic state, evidenced by circulating Howell-Jolly bodies, predisposing to invasive infection with encapsulated bacteria (notably pneumococcus). Bolze et al. (2010) directly attributed the bacterial-infection phenotype to this mechanism.

### (c) Impaired interferon-dependent antiviral immunity → severe viral infections
- FADD participates in TLR-independent innate antiviral signaling, contributing to induction of IRF7 and type I interferon (IFN-α) responses; its loss impairs this arm of antiviral defense, explaining the severe viral infection susceptibility independent of the hyposplenism mechanism.
- More broadly, FADD sits at a molecular decision node between apoptosis and RIPK1/RIPK3/MLKL-driven necroptosis; FADD (with caspase-8) normally restrains necroptosis, and interferon signaling intersects this node (e.g., PKR- and IRF1-dependent, FADD/caspase-licensed necrosis; RIPK3 activates parallel MLKL-necroptosis and FADD-apoptosis pathways as an antiviral defense against influenza A virus, PMID:27321907). This apoptosis/necroptosis balance, and its perturbation by partial FADD loss, is an active area of general FADD biology relevant to interpreting how hypomorphic human FADD alleles could paradoxically both impair apoptotic clearance (arm a) and dysregulate necroptotic/inflammatory tissue injury (arm d, below).

### (d) Recurrent febrile encephalopathy / FIRES-like crises
- The mechanism of the stereotyped encephalopathic episodes is incompletely defined but is hypothesized to involve infection/fever-triggered dysregulated cell death (apoptotic/necroptotic) and/or excessive inflammatory signaling in neural tissue in the FADD-hypomorphic host, producing a clinical picture indistinguishable from febrile infection-related epilepsy syndrome (FIRES) in at least one 2024-reported case (Giovannini et al., *Epilepsia* 2024).

### (e) Hepatopathy
- Recurrent portal inflammation and fibrosis are reported; the precise cellular mechanism (immune-mediated injury vs. direct dysregulated hepatocyte apoptosis/necroptosis) has not been dissected in the literature to date.

### (f) Cardiac malformations
- Ventricular septal defect and pulmonary artery atresia have been reported in a subset of patients; whether this reflects a direct developmental role for FADD-dependent apoptosis in cardiac morphogenesis (consistent with mouse data showing FADD is essential in several developmental contexts via RIPK1/RIPK3 interactions) or coincidental association is unresolved.

### (g) Ocular findings (newly recognized, 2022)
- A case report described retinal vascular findings resembling familial exudative vitreoretinopathy (FEVR) in a FADD-deficient patient, proposed as a novel manifestation potentially reflecting a role for FADD-dependent apoptosis in normal retinal vascular development/pruning — the first such report, attributed to the extreme rarity and short life expectancy of the disorder limiting prior ophthalmologic characterization.

**Suggested GO terms:** GO:0097191 (extrinsic apoptotic signaling pathway), GO:0007249 (I-kappaB kinase/NF-kB signaling), GO:0035666 (TRIF-dependent toll-like receptor signaling), GO:0002230 (positive regulation of defense response to virus by host), GO:0060548 (negative regulation of cell death), GO:0070266 (necroptotic process).
**Suggested CL terms:** CL:0000798 (gamma-delta/alphabeta double-negative T cell context — CL:0000940 CD3+TCRαβ+CD4−CD8− "double-negative" T cell), CL:0000625 (CD8-positive T cell), CL:0000909 (CD4-negative CD8-negative thymocyte).
**Suggested UBERON terms:** UBERON:0002106 (spleen), UBERON:0002107 (liver), UBERON:0000955 (brain), UBERON:0000948 (heart).

---

## 7. Anatomical Structures Affected

- **Primary organs:** Spleen (functional hyposplenism), liver (portal inflammation/fibrosis), brain (encephalopathy, cerebral atrophy, seizure focus), immune system broadly (lymphocytes — T-cell compartment).
- **Secondary/complication-level involvement:** Heart (structural malformations — VSD, pulmonary artery atresia), eyes (retinal vasculature, FEVR-like changes), lymphoid tissue (variable lymphadenopathy/splenomegaly).
- **Body systems:** Immune system, hepatobiliary system, central nervous system, cardiovascular system, hematologic system (functional splenic/Howell-Jolly changes).
- **Cellular level:** T lymphocytes (double-negative αβ T-cell accumulation), hepatocytes/portal tract immune cells, neurons/glia (encephalopathy), retinal vascular endothelium.
- **Subcellular:** Death-inducing signaling complex (DISC) assembly at the plasma membrane/cytoplasm downstream of FAS/TNFR1; mitochondrial apoptosis intersection is downstream of caspase-8 activation.

---

## 8. Temporal Development

- **Onset:** Neonatal to infantile; the majority of reported patients present in the first 1–2 years of life (index case at 14 months with febrile status epilepticus; original kindred affected as young children).
- **Onset pattern:** Insidious background susceptibility (infections, hepatopathy) punctuated by acute/subacute encephalopathic crises.
- **Progression:** Variable — historically rapidly progressive/fatal (3 of 4 original patients died before age 5), but recent reports (2023) describe patients surviving longer with modern supportive management (immunoglobulin replacement, HSCT evaluation).
- **Disease course pattern:** Episodic/relapsing-remitting for the encephalopathic component (recurrent, stereotyped febrile episodes); chronic and progressive for the hepatic fibrosis and immune dysregulation components.
- **Critical periods:** Febrile illness episodes function as recurring critical/vulnerable windows for both infectious decompensation and encephalopathic crisis triggering.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive (homozygous or compound heterozygous *FADD* variants); 25% recurrence risk for children of two carrier parents, 50% carrier risk.
- **Epidemiology:** Extremely rare — fewer than ~15 patients reported across the entire published literature as of 2023–2024, spanning at least 8 published reports; no formal prevalence or incidence estimate exists (too rare for population-based registries). Effectively an "ultra-rare" disorder in Orphanet-style banding (equivalent to <1 per 1,000,000).
- **Consanguinity:** Central risk factor — the founding/largest reported kindred was a consanguineous Pakistani family; consanguinity likely explains the concentration of biallelic cases.
- **Founder effects:** The recurrent p.C105W allele reported in both the original Pakistani kindred and (independently) in the 2024 FIRES case report suggests either a mutational hotspot at this conserved cysteine or a possible founder allele, though this is not formally established via haplotype analysis in available literature.
- **Sex ratio / geographic distribution:** No sex predilection reported; cases have been described in Pakistani, and separately in other (unspecified ethnicity, US-based) families, suggesting the disorder is not geographically restricted, though under-ascertainment outside specialized immunodeficiency/genetics centers is likely given the extreme rarity and diagnostic overlap with ALPS/FIRES/sepsis.
- **Genetic anticipation, mosaicism:** Not described/applicable for this classical biallelic recessive disorder.

---

## 10. Diagnostics

- **Functional assay:** In vitro Fas-mediated (CD95-mediated) T-cell apoptosis assay showing profoundly impaired apoptosis is a key diagnostic tool, analogous to its established role in the ALPS diagnostic algorithm (used when FAS/FASLG/CASP10 germline variants are not identified, per GeneReviews ALPS criteria) [ncbi.nlm.nih.gov/books/NBK1108].
- **Genetic testing:** Confirmatory molecular diagnosis requires identification of biallelic pathogenic/likely pathogenic *FADD* variants — achieved historically via combined genome-wide linkage analysis + whole-exome sequencing (the original discovery approach) and, in contemporary practice, via targeted primary immunodeficiency gene panels or clinical exome/genome sequencing.
- **Laboratory biomarkers:** Elevated circulating double-negative (CD3+TCRαβ+CD4−CD8−) T cells; elevated soluble FasL; elevated IL-10; elevated IL-18 (reported); elevated vitamin B12; Howell-Jolly bodies on peripheral smear (functional hyposplenism); absent isohemagglutinins despite normal total immunoglobulins; reduced FADD protein expression by immunoblot in patient cells.
- **Imaging:** Brain MRI showing cerebral atrophy in survivors of recurrent encephalopathic episodes; echocardiography for structural cardiac defects (VSD, pulmonary artery atresia).
- **Differential diagnosis:** Classic ALPS (FAS/FASLG/CASP10 germline or somatic variants — the majority, 60–70%, are ALPS-FAS), ALPS-U (undetermined genetic cause with abnormal Fas apoptosis assay), other causes of FIRES/status epilepticus with fever, other primary immunodeficiencies with hyposplenism, and other causes of infantile encephalopathy with hepatopathy.
- **Screening:** No population/newborn screening program exists given the extreme rarity; diagnosis is case-by-case via clinical suspicion (recurrent infection + hepatopathy + episodic encephalopathy + ALPS-like biomarkers) followed by genetic confirmation. Genetic/carrier counseling is recommended for consanguineous families with an affected child.

---

## 11. Outcome/Prognosis

- **Survival:** Historically poor — in the original 2010 report, 3 of 4 affected patients from the founding kindred died before age 5, from invasive pneumococcal infection or during an encephalopathic episode. A more recently reported affected sibling died at 18 months following a post-vaccination encephalopathic episode.
- **Contemporary outcomes:** More recent cases (2020, 2023) describe survival into later childhood/beyond with intensive multidisciplinary management, including immunoglobulin replacement and hematopoietic stem cell transplantation (HSCT) — two patients in the 2015 Savic et al. report (*J Allergy Clin Immunol* 2015;136(2):502-5) both underwent HSCT, though the literature does not provide detailed long-term outcome data for these transplants; a 2023-reported infant was undergoing HSCT evaluation with subjective clinical improvement on subcutaneous immunoglobulin in the interim.
- **Morbidity:** Chronic hepatic fibrosis, recurrent infections, cerebral atrophy with associated neurodevelopmental impact, and (in a subset) structural cardiac disease contribute cumulative morbidity in survivors.
- **Prognostic factors:** Severity and frequency of encephalopathic crises appear to be the dominant driver of early mortality; access to specialized immunologic/hematologic care (immunoglobulin replacement, early HSCT) may improve survival based on the trend across sequential case reports (2010 → 2015 → 2020 → 2023).

---

## 12. Treatment

No disease-specific approved therapy exists; management is supportive/empiric, extrapolated from other primary immunodeficiency and ALPS-spectrum disorders:

- **Immunoglobulin replacement therapy:** Subcutaneous immunoglobulin (e.g., 400 mg/kg/month reported) used for infection prophylaxis, with subjective reduction in fatigue and respiratory infections in a recent case. (NCIT:C15986 Pharmacotherapy; therapeutic class immunoglobulin replacement.)
- **Antimicrobial prophylaxis:** Implied by the functional-hyposplenism mechanism (analogous to management of other hyposplenic states — pneumococcal prophylaxis/vaccination, though live vaccines require caution given the reported post-MMR encephalopathic death).
- **Hematopoietic stem cell transplantation (HSCT):** Used in at least 4 reported patients (2 in Savic et al. 2015; 1 under evaluation in Setia et al. 2023) as a potentially curative approach addressing the underlying immune/hematologic defect, though outcome detail is limited in available sources. (NCIT:C15431, Hematopoietic Cell Transplantation.)
- **Seizure/encephalopathy management:** Standard antiseizure/status epilepticus management for the FIRES-like episodes; no FADD-specific anti-inflammatory or immunotherapy protocol is established, though the disease's classification within the ALPS/immune-dysregulation spectrum has prompted case-level use of immunotherapy for neuroinflammatory episodes in related literature (Vogel et al., *Clinical Genetics* 2023, referenced in search results but full detail not independently verified in this research pass).
- **Supportive care:** Management of hepatic dysfunction/fibrosis and cardiac malformations follows standard organ-specific supportive protocols; no FADD-targeted hepatoprotective therapy exists.
- **Experimental/targeted approaches:** None specific to FADD deficiency are in clinical trials (searches of ClinicalTrials.gov did not surface disease-specific interventional trials, consistent with the disorder's extreme rarity). Given FADD's centrality to the apoptosis/necroptosis balance, RIPK1/RIPK3/necroptosis-pathway-targeted agents (investigated in other contexts, e.g., RIPK1 inhibitors) represent a theoretical but unproven future therapeutic avenue.

---

## 13. Prevention

- **Primary prevention:** Not currently possible beyond genetic/reproductive counseling; no vaccination strategy specifically targets FADD deficiency, and caution regarding live-attenuated vaccines (e.g., MMR) may be warranted given a reported temporal association with a fatal encephalopathic episode (single-case observation, not established causally).
- **Genetic counseling:** Recommended for families with a diagnosed case, particularly in consanguineous populations, given the 25% recurrence risk; carrier testing and prenatal/preimplantation genetic diagnosis are theoretically applicable once a familial pathogenic variant is identified but are not specifically documented in the literature reviewed.
- **Secondary prevention:** Early recognition of the biomarker panel (double-negative T cells, elevated sFasL/IL-10/B12) in an infant with recurrent infections and hepatopathy could prompt earlier diagnosis and initiation of infection-prophylactic and immunoglobulin-replacement measures before a first severe encephalopathic crisis.
- **Public health relevance:** Given the extreme rarity, no population-level public health screening or intervention program exists or is anticipated.

---

## 14. Other Species / Natural Disease

- No naturally occurring FADD-deficiency disease has been reported in non-human species (companion animals, wildlife) in the literature surveyed; this appears to be a human-specific clinical entity, consistent with its ultra-rare Mendelian nature and the embryonic-lethal consequence of complete Fadd loss in mice (see below), which would preclude viable natural homozygous-null animal populations.
- **Orthologous gene:** Mouse *Fadd* (MGI ortholog) is the primary comparative genetics reference; no OMIA (Online Mendelian Inheritance in Animals) entry for a natural FADD-deficiency disease was identified.

---

## 15. Model Organisms

FADD biology has been extensively studied in mouse models, though these largely model the gene's fundamental developmental/immunologic roles rather than directly recapitulating the human hypomorphic-disease phenotype:

- **Global *Fadd* knockout mice:** Embryonic lethal, demonstrating FADD is essential for normal embryonic development. This lethality is mediated through necroptotic signaling — combined *Fadd*/*Ripk1* double-knockout mice rescue the embryonic lethality and the lymphocyte proliferation defects seen in single-knockout mice, directly implicating dysregulated RIPK1-dependent necroptosis (not merely loss of apoptosis) as the lethal mechanism of complete FADD loss (Nature 2011, PMID referenced as "Functional complementation between FADD and RIP1 in embryos and lymphocytes"). RIP1-kinase-activity-dependent embryonic phenotypes have also been dissected (*Cell Death Differ* 2018).
- **Conditional/tissue-specific *Fadd* knockouts:**
  - T-cell-specific conditional knockout (GFP-marked): FADD is dispensable for thymic (intrathymic) T-cell development but is essential for peripheral T-cell homeostasis, regulating both apoptotic and proliferative signals (PMID:16116191).
  - Loss of FADD in Tie2-expressing (endothelial/hematopoietic) cells causes RIPK3-mediated embryonic lethality (*Cell Death Dis* 2016, PMC5059855), underscoring FADD's endothelial developmental role — potentially relevant to the cardiac and retinal vascular anomalies reported in human FADD deficiency.
  - FADD regulates T-cell-receptor-mediated necroptosis as a negative regulator (PNAS, PMID referenced 1005997107), and RIP1 deficiency fully restores normal T-cell (but not B-cell) proliferation in *Fadd*-null lymphocytes, indicating cell-type-specific dependence on the FADD/RIPK1 necroptosis-suppression axis.
  - FADD has been shown to regulate adipose tissue inflammation, adipogenesis, and adipocyte survival (*Cell Death Discov* 2024) — an emerging, disease-adjacent role not yet linked to human phenotype.
- **Phenotype recapitulation and limitations:** Because complete murine Fadd loss is embryonic lethal, no mouse model directly phenocopies the human hypomorphic (partial loss-of-function) FADD-deficiency disease phenotype (recurrent infection, hepatopathy, encephalopathy). Conditional and hypomorphic mouse alleles instead illuminate discrete mechanistic arms (T-cell homeostasis, necroptosis suppression, endothelial/vascular development) that plausibly underlie individual human disease features (immune dysregulation, cardiac/retinal vascular anomalies) but have not been integrated into a single disease model.
- **Research applications:** These models are principally used to dissect FADD's role at the apoptosis-necroptosis decision node and its tissue-specific essentiality (immune, endothelial, adipose), providing mechanistic hypotheses (rather than direct phenocopy validation) for the multi-organ human disease.

---

## Summary of Key Evidence Sources

| Citation | Contribution |
|---|---|
| Bolze A, et al. *Am J Hum Genet* 2010;87(6):873-881. PMID:21109225 | Original discovery of human FADD deficiency (p.C105W, consanguineous kindred); established core phenotype (ALPS-like biomarkers + infections + hepatopathy + encephalopathy + cardiac malformations); hyposplenism/interferon-immunity mechanistic hypotheses |
| Savic S, et al. *J Allergy Clin Immunol* 2015;136(2):502-5 | Second report, 2 patients, both treated with HSCT |
| "Novel Compound Heterozygote Variations in FADD..." *J Clin Immunol* 2020, PMC7253512 | Additional compound heterozygous variants expanding allelic spectrum |
| Ocular findings paper, *Ophthalmology/related journal* 2022 (ScienceDirect S2451993622000512) | First report of FEVR-like retinal findings in FADD deficiency |
| Setia P, et al. *Br J Haematol* 2023;202(2):e11-e15. PMID:37199216, DOI:10.1111/bjh.18871 | Novel compound heterozygous variants (c.313T>C/p.C105R + c.52_58delGACGAGC); detailed immunophenotyping; SCIg treatment |
| Giovannini G, et al. *Epilepsia* 2024;65(7):e119-e124. DOI:10.1111/epi.18008 | FADD (p.C105W) presenting as FIRES; literature review |
| Vogel et al. *Clinical Genetics* 2023 | Immunotherapy-responsive neuroinflammation in FADD-mutant child (referenced; not independently fetched) |
| OMIM #613759 / *602457 | Curated gene-disease and allelic summary |
| PMC10970579 / MDPI *Int J Mol Sci* 2024;25(6):3228 | Review: "Cellular Dynamics of Fas-Associated Death Domain in the Regulation of Cancer and Inflammation" — general FADD mechanism update |
| GeneReviews, ALPS (NBK1108) | Diagnostic-algorithm context distinguishing FADD deficiency from classic ALPS-FAS/FASLG/CASP10 |

**Note on evidence gaps:** This is an ultra-rare disease with fewer than ~15 published patients; several details (full genotype-phenotype correlation, long-term HSCT outcomes, mechanism of hepatic and cardiac involvement, formal QOL data, population prevalence) are not established in the literature and should be flagged as data-limited/not-yet-determined in any knowledge-base entry rather than inferred.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.