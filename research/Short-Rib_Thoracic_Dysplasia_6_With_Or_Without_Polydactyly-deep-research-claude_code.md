---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T14:49:56.815283'
end_time: '2026-08-27T14:54:05.736846'
duration_seconds: 248.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Short-Rib Thoracic Dysplasia 6 With or Without Polydactyly
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
  web_search_requests: 14
  num_turns: 26
  total_cost_usd: 1.1453592
  session_id: 98b3127c-432a-57dc-acc9-774218ba8a79
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 22
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 1
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:21211617
  - PMID:22876582
  relevance_assessed: 14
  on_topic: 5
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Short-Rib Thoracic Dysplasia 6 With or Without Polydactyly
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Short-Rib Thoracic Dysplasia 6 With or Without Polydactyly** covering all of the
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

I now have sufficient primary-literature-grounded material to compile the full report.

# Short-Rib Thoracic Dysplasia 6 With or Without Polydactyly (SRTD6) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Short-rib thoracic dysplasia 6 with or without polydactyly (SRTD6) is an autosomal recessive skeletal ciliopathy caused by biallelic mutation of the *NEK1* gene on chromosome 4q33. It belongs to the short-rib thoracic dysplasia (SRTD) group of disorders — historically also called short rib–polydactyly syndrome (SRPS) — and corresponds specifically to **short rib–polydactyly syndrome type II, Majewski type**. SRTD6 is a lethal osteochondrodysplasia in its classic (homozygous-null) presentation, characterized by a severely constricted, narrow thoracic cage; short, horizontally oriented ribs; short long bones; and a "trident" (three-pronged) acetabular roof, together with variable polydactyly and multiorgan visceral anomalies (OMIM #263520; DOID:0110092).

**Key identifiers:**
- **OMIM:** #263520 — SHORT-RIB THORACIC DYSPLASIA 6 WITH OR WITHOUT POLYDACTYLY; SRTD6 ([omim.org/entry/263520](https://omim.org/entry/263520))
- **MONDO:** MONDO:0009894
- **Disease Ontology:** DOID:0110092
- **ICD-10-CM:** Q77.2 (Asphyxiating thoracic dysplasia)
- **Gene:** NEK1 (HGNC), OMIM gene entry *604588*, chr4q33
- **UMLS/MedGen concept:** C0024507 ([NCBI GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C0024507/))

**Synonyms:** Majewski syndrome; Short rib-polydactyly syndrome, type II (SRPS2); Short rib-polydactyly syndrome type IIA (SRPS2A); Polydactyly with neonatal chondrodystrophy, type II; Short-rib polydactyly syndrome type Majewski ([JAX DOID browser](https://www.informatics.jax.org/disease/DOID:0110092)).

**Data provenance:** Knowledge is derived almost entirely from aggregated disease-level resources (OMIM, GeneReviews-style skeletal-ciliopathy reviews, structured case-report literature and prenatal case series) rather than large EHR cohorts — this is a rare Mendelian disorder without a dedicated national registry, so most quantitative data (mutation counts, cilia measurements) come from individual research cohorts/case series of a few dozen families total ([Thiel et al. 2011, PMID:21211617](https://pubmed.ncbi.nlm.nih.gov/21211617/); [El Hokayem et al. 2012, PMID:22499340](https://pubmed.ncbi.nlm.nih.gov/22499340/)).

## 2. Etiology

**Primary genetic cause.** SRTD6 is caused by homozygous or compound heterozygous loss-of-function mutation in *NEK1*, which encodes a NIMA-related serine/threonine kinase (NEK1) required for cilium assembly, and separately implicated in DNA double-strand-break repair/checkpoint control and neuronal development ([OMIM #263520](https://omim.org/entry/263520); [Thiel et al. 2011](https://pubmed.ncbi.nlm.nih.gov/21211617/)). NEK1 has relatively high expression in the growth plate, consistent with the skeletal phenotype.

**Founding mutations.** In the discovery study (Thiel et al., *AJHG* 2011, PMID:21211617), homozygosity mapping in two consanguineous families identified:
- Family 1: homozygous nonsense mutation **c.379C>T (p.Arg127X)**
- Family 2: homozygous splice-site mutation **c.869-2A>G**
- Family 3: heterozygous frameshift insertion **c.1640dup** in *NEK1* together with a heterozygous missense variant in *DYNC2H1*

**Digenic/oligogenic inheritance.** A distinctive etiologic feature of SRTD6 is documented **digenic diallelic inheritance**: a proband can be affected by combined heterozygosity for one loss-of-function *NEK1* allele and one pathogenic *DYNC2H1* allele, producing "combined haploinsufficiency of cilia formation and intraflagellar transport (IFT)" ([Thiel et al. 2011](https://pubmed.ncbi.nlm.nih.gov/21211617/)). This was substantiated in a larger follow-up cohort: El Hokayem et al. (*J Med Genet* 2012, PMID:22499340) screened 13 SRP type II (Majewski) and 7 SRP type IV (Beemer-Langer) cases, finding homozygous *NEK1* mutations in 5/13 type II cases, compound heterozygous *DYNC2H1* mutations in 4/12 type II cases, and one case with double heterozygosity across both genes — while both genes were excluded in all type IV (Beemer-Langer) cases, establishing that NEK1/DYNC2H1 involvement is specific to the Majewski subtype. The authors noted residual genetic heterogeneity, since neither gene explained all screened cases, implying additional unidentified causal genes remain. Mutation-negative SRP type II cases in that cohort notably presented with holoprosencephaly and polymicrogyria, absent in mutation-positive cases — suggesting phenotypic clues to underlying gene.

**Risk factors:**
- *Genetic:* consanguinity substantially raises risk given the autosomal recessive, homozygous-null mechanism seen in the founding families.
- *Environmental:* No environmental, infectious, or lifestyle risk factors are established; this is a purely monogenic/digenic ciliopathy.
- *Gene-environment interaction:* None reported.

**Protective factors:** None specifically described for SRTD6. In the broader ciliopathy spectrum, allelic severity is thought to be genotype-dependent — hypomorphic (partial-function) alleles of ciliary genes generally produce milder, non-lethal SRTD phenotypes (e.g., Mainzer-Saldino, isolated Jeune-type disease) versus complete loss-of-function alleles producing lethal Majewski-type disease, though this specific genotype-severity correlation has not been formally established for *NEK1* itself.

## 3. Phenotypes

Because SRTD6 aggregates clinical data across a small number of published families/case reports, phenotype frequencies below are qualitative characterizations from the SRTD/SRPS Majewski-type literature rather than large-cohort percentages.

**Skeletal phenotype (core, congenital/prenatal onset):**
- Narrow, constricted thoracic cage — HP:0000774 (Narrow chest)
- Short ribs — HP:0000773 (Short ribs)
- Short-limbed dwarfism/micromelia — HP:0004970 (Mesomelia) / HP:0009824 (Progressive shortening of the extremities)
- Disproportionately short, ovoid tibiae or tibial agenesis (the most distinctive Majewski-type finding, distinguishing it from other SRP subtypes) — HP:0005843 (Micromelia); HP:0009825
- Polydactyly (pre- and postaxial), variably present — HP:0100259 (Postaxial polydactyly) / HP:0001161 (Preaxial polydactyly)
- Trident-shaped acetabular roof on radiography — HP:0003026 (Trident acetabular roof)

**Craniofacial:**
- Dysmorphic facial features — HP:0001999
- Cleft lip/palate (part of the broader SRTD non-skeletal spectrum) — HP:0000175 (Cleft palate) / HP:0100333 (Unilateral cleft lip)
- Relatively proportionate head size at birth progressing to microcephaly

**Visceral/organ anomalies:**
- Cystic/polycystic kidney disease with dilated collecting tubules and glomeruli of variable size — HP:0000113 (Polycystic kidney dysplasia)
- Intestinal malrotation — HP:0002566
- Congenital heart defects — HP:0001627
- Hepatic anomalies (periportal fibrosis, biliary dysgenesis characteristic of the broader ciliopathy spectrum) — HP:0006560
- Lingual/gingival hamartomas reported in a substantial minority of NEK1-related cases
- Genital anomalies

**Growth:** Severe intrauterine growth restriction is characteristic of the Majewski (type II) presentation ([search summary of Tonni et al. 2014, PMID:24854045](https://pubmed.ncbi.nlm.nih.gov/24854045/)).

**Onset/severity/progression.** Onset is prenatal/congenital in essentially all cases; the classic homozygous-null presentation is uniformly severe and lethal in the perinatal/neonatal period due to pulmonary hypoplasia secondary to the restrictive thoracic cage (respiratory insufficiency). At least one report describes "a short rib polydactyly syndrome overlapping both lethal and nonlethal types" (PMID:22876582), suggesting a phenotypic continuum exists at the milder end even within Majewski-type presentations, potentially correlating with residual NEK1/DYNC2H1 function in digenic or hypomorphic cases.

**Quality of life impact.** For the lethal neonatal presentation, QOL data are not applicable given perinatal mortality; for surviving/milder cases (analogous non-lethal SRTD forms), impact centers on chronic respiratory insufficiency, orthopedic disability from limb shortening, and renal/hepatic morbidity — but disease-specific QOL instruments have not been applied to this specific ultra-rare entity.

## 4. Genetic/Molecular Information

**Causal gene:** *NEK1* (HGNC:7744; NCBI Gene ID 4750), OMIM *604588, chromosome 4q33.

**Variant spectrum documented in the literature:**
| Variant | Type | Zygosity | Source |
|---|---|---|---|
| c.379C>T (p.Arg127X) | Nonsense | Homozygous | Thiel 2011, Family 1 |
| c.869-2A>G | Splice-site (canonical acceptor) | Homozygous | Thiel 2011, Family 2 |
| c.1640dup | Frameshift insertion | Heterozygous (digenic with DYNC2H1) | Thiel 2011, Family 3 |
| c.2255A>G (p.Glu752Gly) | Missense | — | [ClinVar RCV000625335](https://www.ncbi.nlm.nih.gov/clinvar/RCV000625335/) |
| c.1020+1G>A | Splice-site | — | [ClinVar RCV003106460](https://www.ncbi.nlm.nih.gov/clinvar/RCV003106460/) |

**Digenic partner gene:** *DYNC2H1* (cytoplasmic dynein 2 heavy chain 1), OMIM *603297, encoding the retrograde IFT motor protein; biallelic *DYNC2H1* mutations alone cause the allelic disorder SRTD3/short-rib polydactyly type I (Saldino-Noonan). El Hokayem et al. found compound heterozygous *DYNC2H1* mutations independently causal in 4/12 SRTD6-consistent cases, and demonstrated true digenic (both-gene) inheritance in at least one further case.

**Functional consequence:** Loss-of-function (nonsense/frameshift/splice-disrupting) — patient fibroblasts show a severe ciliogenesis defect: only ~27% of cells possessed cilia versus 92% in controls; residual cilia averaged 1.7 ± 0.7 μm in length versus 6.2 ± 1.2 μm in controls, with a "severely reduced length, broad base, and thin apex," and electron microscopy showed ciliogenesis arrested at stage 1, preventing axoneme elongation (Thiel et al. 2011).

**Allele frequency/population data:** No specific gnomAD/population carrier-frequency figures for these specific pathogenic *NEK1* alleles were identified in this search; *NEK1* loss-of-function variants overall are not vanishingly rare in the population because they also confer risk (in monoallelic form) for a distinct, later-onset adult disease (see below), implying population-level heterozygote carriers of *NEK1* LoF alleles exist at appreciable frequency, though homozygous/compound-heterozygous null combinations producing SRTD6 remain very rare.

**Notable pleiotropy — NEK1 and ALS.** *NEK1* is independently one of the most robustly replicated ALS risk genes: heterozygous *NEK1* loss-of-function variants are found in ~2–3% of both familial and sporadic amyotrophic lateral sclerosis cases ([van Rheenen et al., *Nat Genet* 2016](https://www.nature.com/articles/ng.3626); [Rifai et al. 2025, PMID:38986433](https://pmc.ncbi.nlm.nih.gov/articles/PMC11669413/)). NEK1 is implicated in cilia formation, DNA-damage response, microtubule stability, and axonal polarity; the missense variant p.Arg261His has specifically been linked to increased ALS susceptibility, and NEK1 loss-of-function has been shown to induce DNA damage accumulation in ALS patient-derived motor neurons ([Higelin et al. 2018, PMID:29929116](https://pubmed.ncbi.nlm.nih.gov/29929116/)) and to disrupt microtubule homeostasis/nuclear import ([PMC10431718](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10431718/)). This represents an important gene-dosage relationship for curation purposes: monoallelic NEK1 LoF → ALS susceptibility in adults; biallelic (or digenic NEK1+DYNC2H1) LoF → lethal perinatal skeletal ciliopathy (SRTD6).

**Epigenetics/chromosomal abnormalities:** No epigenetic mechanism or large chromosomal rearrangement mechanism has been described for SRTD6; it is a classical biallelic point-mutation/small-indel Mendelian disorder.

## 5. Environmental Information

No environmental toxins, lifestyle factors, or infectious triggers are documented as contributing to SRTD6 — it is a fully genetically determined ciliopathy with no reported gene-environment modulation.

## 6. Mechanism / Pathophysiology

**Molecular pathway:** NEK1 is a NIMA-family serine/threonine kinase that localizes to the centrosome and basal body of the primary cilium and is required for the initiation and elongation of ciliogenesis. Together with its digenic partner DYNC2H1 (the motor subunit of cytoplasmic dynein-2, which drives retrograde intraflagellar transport, IFT), NEK1 loss disrupts both the assembly and the trafficking machinery of the primary cilium.

**Causal chain (upstream → downstream):**
1. **Molecular trigger:** Biallelic loss-of-function *NEK1* variants (or digenic NEK1+DYNC2H1 haploinsufficiency) abolish or truncate functional NEK1 kinase.
2. **Cellular process:** Ciliogenesis is arrested at an early stage (stage 1 by EM), producing severely reduced cilium number and grossly abnormal (short, broad-based, thin-apex) cilium morphology in patient fibroblasts.
3. **Tissue/organ process:** Impaired Hedgehog and other cilium-dependent signaling in the growth plate disrupts endochondral ossification, producing shortened long bones, short ribs, and the constricted trident-shaped thoracic skeleton; impaired ciliary signaling in the kidney nephron produces cystic dilatation of tubules/glomeruli; impaired ciliary signaling during organogenesis produces situs/laterality-adjacent defects such as intestinal malrotation and congenital heart defects.
4. **Organism-level outcome:** The severely restricted thoracic cage causes pulmonary hypoplasia and, in the classic lethal presentation, fatal neonatal respiratory insufficiency.

**Cell types/biological processes involved:**
- Chondrocytes and growth-plate cells (GO:0001501 skeletal system development; GO:0060173 limb development) — CL:0000138 chondrocyte
- Ciliated epithelial cells across multiple organs (GO:0060271 cilium assembly; GO:0003341 cilium movement)
- Renal tubular epithelial cells (CL:1000838 kidney collecting duct principal cell / general nephron epithelium)
- Centrosome/basal body machinery (GO:0005929 cilium; GO:0005813 centrosome)

**Protein dysfunction:** NEK1 truncating/nonsense/splice variants are predicted to produce a nonfunctional or absent kinase; DYNC2H1 missense/compound-heterozygous variants impair motor-protein function within the IFT-B/dynein-2 retrograde transport complex.

**Molecular profiling / advanced omics:** No transcriptomic, proteomic, single-cell, or spatial-omics dataset specific to SRTD6/NEK1 patient tissue was identified in this search; the mechanistic evidence base rests on classic cellular/EM ciliary phenotyping in patient-derived fibroblasts (Thiel et al. 2011) rather than -omics profiling.

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: skeletal system (rib cage, long bones, pelvis/acetabulum), lungs (secondary hypoplasia)
- Secondary/associated: kidneys (cystic dysplasia), liver, intestines (malrotation), heart, oral cavity (lingual/gingival hamartomas), craniofacial structures (cleft lip/palate)
- Body systems: skeletal, respiratory, renal, hepatobiliary, gastrointestinal, cardiovascular

**Tissue/cell level:** Cartilage and growth-plate chondrocytes (endochondral bone), renal tubular/glomerular epithelium, ciliated epithelial cell populations broadly (UBERON:0000922 embryonic structures during organogenesis are relevant given the developmental timing).

**Subcellular level:** Primary cilium and basal body/centrosome (GO:0005929 cilium; GO:0036064 ciliary basal body; GO:0005813 centrosome) — the direct organelle-level site of NEK1/DYNC2H1 dysfunction.

**Anatomical terms (UBERON):**
- UBERON:0002228 rib
- UBERON:0002228 thoracic cage / UBERON:0000915 thoracic segment
- UBERON:0002203 pelvic girdle / acetabulum
- UBERON:0002113 kidney
- UBERON:0002370 thymus (not specifically implicated but general organogenesis context)
- UBERON:0002049 tibia

**Laterality:** No consistent lateralization pattern reported; skeletal changes are typically bilateral/symmetric, consistent with a systemic skeletal dysplasia rather than a focal or asymmetric process.

## 8. Temporal Development

- **Onset:** Congenital/prenatal — detectable by second-trimester ultrasound (short-limb dwarfism, narrow thorax, polydactyly).
- **Onset pattern:** Present from early fetal development; not acquired or adult-onset in the classic SRTD6 presentation.
- **Progression:** In the lethal (classic biallelic-null) form, the disease is present at birth and rapidly fatal in the neonatal period from respiratory failure; there is no "stage" progression in a clinical-course sense — it is a fixed developmental malformation syndrome rather than a degenerative disease.
- **Course pattern:** Non-progressive skeletal malformation with static structural anomalies; the acute driver of mortality is respiratory insufficiency at or shortly after birth.
- **Duration:** For the lethal type, self-limited by neonatal death; case reports of milder "overlapping lethal/nonlethal" phenotypes suggest occasional survivors, in which case the skeletal features would presumably persist as a chronic, non-progressive dysplasia (as in analogous non-lethal SRTD entities such as Jeune syndrome, where survivors can have chronic thoracic insufficiency).
- **Critical periods:** Second-trimester prenatal ultrasound is the key window for detection; the perinatal period is the critical window of vulnerability for respiratory mortality.

## 9. Inheritance and Population

**Epidemiology:** No SRTD6-specific incidence figure was located; the short-rib thoracic dysplasia group as a whole (encompassing Jeune/asphyxiating thoracic dystrophy, the SRPS types, Mainzer-Saldino, and Ellis-van Creveld) is estimated at **1:100,000 to 1:130,000 live births** ([search summary citing SRTD group literature](https://link.springer.com/rwe/10.1007/978-3-319-66816-1_1651-1); consistent with Jeune-syndrome-specific figures at [NORD](https://rarediseases.org/rare-diseases/dystrophy-asphyxiating-thoracic/)). SRTD6/Majewski-type specifically is a small fraction of this pool — the discovery and follow-up cohorts each comprised only a handful to ~13-20 families.

**Inheritance pattern:** Autosomal recessive (biallelic *NEK1*), with documented **digenic diallelic inheritance** (heterozygous *NEK1* + heterozygous *DYNC2H1*) as an alternative genetic architecture in some families — an important nuance beyond simple monogenic AR inheritance.

**Penetrance/expressivity:** The classic homozygous/compound-heterozygous null genotype appears fully penetrant for the lethal phenotype; variable expressivity is suggested by reports of milder/non-lethal overlap phenotypes (PMID:22876582), potentially reflecting hypomorphic alleles or digenic combinations with partial residual function.

**Consanguinity:** The founding genetic mapping studies used consanguineous families (homozygosity mapping design), consistent with an increased risk in consanguineous unions given the rare recessive allele frequency.

**Founder effects/carrier frequency/geographic distribution:** No specific founder mutation or population-enriched carrier frequency was identified for SRTD6-causing *NEK1* alleles in this search.

**Demographics:** No sex ratio skew is reported (autosomal, not X-linked); affected individuals are, by definition, prenatal/neonatal in age given the classic lethal presentation.

## 10. Diagnostics

**Prenatal imaging:** Second- and third-trimester ultrasound is the primary diagnostic modality — short/micromelic long bones, narrow thorax, polydactyly, and (in Majewski type specifically) disproportionately short/ovoid tibiae are characteristic findings ([Tonni et al. 2014, PMID:24854045](https://pubmed.ncbi.nlm.nih.gov/24854045/); prenatal case series [ScienceDirect 2012](https://www.sciencedirect.com/science/article/pii/S1028455912000216)).

**Postnatal/autopsy radiography:** Short horizontal ribs, "trident" acetabular roof, shortened tubular bones — the classic radiographic constellation defining the SRTD/SRPS group and distinguishing Majewski (type II) from Saldino-Noonan (type I), Verma-Naumoff (type III), and Beemer-Langer (type IV) by specific limb-bone morphology (particularly tibial involvement in Majewski type).

**Histopathology:** Chondral growth-plate histology and renal/hepatic histopathology have been characterized in autopsy/prenatal-diagnosis case series (Tonni et al. 2014, PMC2890924).

**Genetic testing:**
- Single-gene *NEK1* sequencing or *NEK1*+*DYNC2H1* dual testing given documented digenic inheritance
- Skeletal dysplasia/ciliopathy gene panels (which would include *NEK1*, *DYNC2H1*, and other SRTD genes — the field now recognizes ~25 genes across the skeletal ciliopathy spectrum)
- Exome/genome sequencing, particularly valuable given genetic heterogeneity within SRP type II (only ~9/13 cases explained by NEK1 or DYNC2H1 in the largest published cohort) and the possibility of digenic combinations that single-gene panels might miss if not designed to flag compound findings across two genes
- Chromosomal microarray/karyotype are not primary diagnostic tools here (this is not a copy-number or aneuploidy disorder)

**Differential diagnosis:** Other SRTD/SRPS subtypes (Saldino-Noonan/type I, Verma-Naumoff/type III, Beemer-Langer/type IV), Ellis-van Creveld syndrome, Jeune syndrome (asphyxiating thoracic dystrophy), Mainzer-Saldino syndrome, and other lethal skeletal dysplasias (e.g., thanatophoric dysplasia) presenting with narrow thorax and limb shortening on prenatal ultrasound — differentiation is largely radiographic (limb-bone pattern) plus molecular confirmation ([MDPI 2022 differential-diagnosis case report](https://www.mdpi.com/2073-4425/13/8/1339)).

**Screening:** No population-based newborn or carrier screening program specific to SRTD6 exists; detection is via targeted prenatal ultrasound in at-risk (e.g., consanguineous or previously affected) families, followed by confirmatory molecular testing.

## 11. Outcome/Prognosis

**Mortality:** The classic (biallelic-null) SRTD6/Majewski-type presentation is **lethal in the neonatal period**, with death from respiratory insufficiency secondary to pulmonary hypoplasia driven by the severely restricted thoracic cage — consistent with SRP types 1–4 broadly being "lethal in the newborn period because of severe pulmonary hypoplasia and other associated anomalies."

**Milder/overlap phenotypes:** At least one report describes a short rib-polydactyly phenotype "overlapping both lethal and nonlethal types" (PMID:22876582), indicating that the digenic or hypomorphic-allele end of the spectrum may permit survival, analogous to surviving forms of the broader SRTD group (e.g., Jeune syndrome, where children can survive infancy but face chronic thoracic insufficiency and progressive renal/hepatic disease).

**Prognostic factors:** Genotype severity (complete null biallelic NEK1 vs. digenic/hypomorphic combinations) likely drives the lethal-vs-survivable distinction, though this has not been formally quantified in a genotype-phenotype correlation study for SRTD6 specifically.

## 12. Treatment

There is no disease-modifying or curative therapy for SRTD6; management is supportive and, for survivors of the perinatal period (extrapolating from the broader Jeune-syndrome/SRTD survivor literature), centers on mechanical thoracic expansion.

- **Respiratory support:** Mechanical ventilation for neonatal respiratory insufficiency (NCIT term: supportive care).
- **Thoracic expansion surgery** for thoracic insufficiency syndrome in surviving SRTD patients (established chiefly in Jeune syndrome, the closest well-studied analog):
  - **Vertical Expandable Prosthetic Titanium Rib (VEPTR)** — FDA-approved 2004, an adjustable device that separates ribs and straightens the spine to permit lung growth; reported survival ~68% in treated Jeune-syndrome cohorts versus 70–80% mortality historically without treatment ([PMID:25575358](https://pubmed.ncbi.nlm.nih.gov/25575358/)). NCIT term: `NCIT:C15329` (Surgical Procedure); therapeutic modality: `DEVICE`.
  - Lateral thoracic expansion, vertical thoracic expansion, sternal/rib elevation, and progressive internal sternal distraction techniques have all been reported, with no consensus on optimal timing/approach given disease rarity ([PMC10562558](https://pmc.ncbi.nlm.nih.gov/articles/PMC10562558/)).
- **Renal management:** Supportive care/monitoring for cystic kidney disease; dialysis/transplantation would be considered in survivors with progressive renal failure (extrapolated from the general ciliopathy-nephropathy paradigm).
- **Orthopedic/rehabilitative care:** For limb-shortening sequelae in survivors — NCIT:C15302 (Physical Therapy).
- **Genetic counseling:** NCIT:C15240 — essential given autosomal recessive/digenic inheritance and high recurrence risk (25% for simple AR; more complex for digenic combinations) in future pregnancies.
- **No pharmacotherapy, gene therapy, or targeted molecular therapy** has been developed or trialed specifically for NEK1-related ciliopathy; ClinicalTrials.gov searches did not surface active SRTD6-specific interventional trials in this search.

## 13. Prevention

- **Prenatal diagnosis/reproductive options:** Given the poor prognosis of the classic lethal phenotype, second-trimester ultrasound screening in at-risk families (prior affected child, known consanguinity, known carrier status) enables early prenatal diagnosis and informed reproductive decision-making.
- **Carrier/genetic counseling:** Recommended for families with a prior affected pregnancy or child, particularly given the digenic (NEK1+DYNC2H1) inheritance pattern, which complicates simple recurrence-risk counseling beyond standard 25% AR recurrence.
- **Preimplantation genetic testing (PGT-M):** A theoretically applicable option for known-carrier couples, though no SRTD6-specific PGT case series was identified.
- No primary (population-level), immunization-based, or public-health prevention strategy applies, as this is a rare monogenic/digenic disorder with no modifiable environmental component.

## 14. Other Species / Natural Disease

No naturally occurring SRTD6/Majewski-type ciliopathy has been reported in non-human species in this search; this appears to be a human-specific clinical entity in the veterinary/comparative literature reviewed.

## 15. Model Organisms

**Mouse model — *Nek1^kat2J^* (the "kat" mouse, for **k**idney, **a**nemia, **t**estis phenotype):**
- A spontaneous *Nek1*-null mouse mutant (*kat2J* allele) is the principal genetic model connecting *Nek1* loss to ciliopathy phenotypes. *Nek1* localizes to centrosomes and the primary cilium in this model, and *kat2J* homozygous mice develop **polycystic kidney disease**: kidney development is aberrant early, prior to gross cyst appearance — cortical zones are thin, populated by immature glomeruli, with excessive apoptosis across several cell types; cysts subsequently form postnatally in Bowman's space and multiple tubular subtypes ([PMC4422189](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4422189/); [Springer 2014](https://link.springer.com/article/10.1186/s12929-014-0063-5)).
- Nek1 expression in the embryonic kidney is most prominent in cells destined to become podocytes and proximal tubules.
- This model is explicitly framed in the primary literature as modeling "the ciliopathy polycystic kidney disease caused by abnormal ciliary structure or signaling" and directly links *Nek1* mutation to a human ciliopathy (short-rib polydactyly syndrome type Majewski).
- **Limitation:** The *kat2J* mouse model's published phenotyping emphasizes the **renal cystic phenotype** rather than the full skeletal (short-rib/short-limb/polydactyly) phenotype defining human SRTD6 — i.e., it recapitulates the ciliopathy/renal-cystic component with apparent fidelity but the mouse literature reviewed here does not establish whether it reproduces the diagnostic skeletal dysplasia, representing an open human-model-fidelity question for the skeletal component specifically. No dedicated skeletal-phenotyping publication for *kat2J* mice was surfaced in this search.
- **Cellular models:** Patient-derived dermal fibroblasts are the key human cellular model used to establish the ciliogenesis defect (severely reduced cilium number/length, arrested ciliogenesis at stage 1) — this is IN_VITRO evidence directly from affected individuals, distinct from the mouse model (Thiel et al. 2011).
- No zebrafish, Drosophila, C. elegans, iPSC-derived, or organoid model specific to *NEK1*-related SRTD6 was identified in this search (note: zebrafish morpholino/CRISPR knockdown of *nek1* has been used in some ciliopathy contexts more broadly, but a dedicated citation was not surfaced here and should be verified against primary literature before curation).

**Suggested Cell Ontology/model terms:** CL:0000057 (fibroblast, for the patient-fibroblast ciliogenesis assay); NCBITaxon:10090 (Mus musculus, for the *kat2J* model); NCBITaxon:9606 (Homo sapiens, for fibroblast studies).

---

## Summary of Key Ontology Term Suggestions for Curation

| Category | Suggested term |
|---|---|
| Disease (MONDO) | MONDO:0009894 |
| Gene 1 (HGNC) | hgnc:7744 (NEK1) |
| Gene 2, digenic (HGNC) | hgnc:2794 (DYNC2H1) |
| Inheritance (HP) | HP:0000007 (Autosomal recessive); HP:0010984 (Digenic inheritance) — for the NEK1+DYNC2H1 combination |
| Phenotype | HP:0000774 (Narrow chest), HP:0000773 (Short ribs), HP:0100259 (Postaxial polydactyly), HP:0003026 (Trident acetabular roof), HP:0000113 (Polycystic kidney dysplasia), HP:0002566 (Intestinal malrotation), HP:0001627 (Abnormal heart morphology), HP:0000175 (Cleft palate) |
| GO Biological Process | GO:0060271 (cilium assembly), GO:0007049 (cell cycle), GO:0006302 (double-strand break repair) |
| GO Cellular Component | GO:0005929 (cilium), GO:0036064 (ciliary basal body), GO:0005813 (centrosome) |
| Cell Type (CL) | CL:0000138 (chondrocyte), CL:0000057 (fibroblast) |
| Anatomy (UBERON) | UBERON:0002228 (rib), UBERON:0002113 (kidney), UBERON:0002049 (tibia) |
| Treatment (NCIT) | NCIT:C15329 (Surgical Procedure — thoracic expansion/VEPTR), NCIT:C15240 (Genetic Counseling) |

---

### Sources

- [Entry #263520 — SHORT-RIB THORACIC DYSPLASIA 6 WITH OR WITHOUT POLYDACTYLY; SRTD6 - OMIM](https://omim.org/entry/263520)
- [NEK1 mutations cause short-rib polydactyly syndrome type Majewski — PubMed (PMID:21211617)](https://pubmed.ncbi.nlm.nih.gov/21211617/) / [PMC3014367](https://pmc.ncbi.nlm.nih.gov/articles/PMC3014367)
- [NEK1 and DYNC2H1 are both involved in short rib polydactyly Majewski type but not in Beemer Langer cases — PubMed (PMID:22499340)](https://pubmed.ncbi.nlm.nih.gov/22499340/)
- [Short rib-polydactyly syndrome type II (Majewski): Prenatal diagnosis, perinatal imaging findings and molecular analysis of the NEK1 gene — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1028455912000216)
- [Majewski syndrome (short-rib polydactyly syndrome type II): Prenatal diagnosis and histological features — PubMed (PMID:24854045)](https://pubmed.ncbi.nlm.nih.gov/24854045/)
- [A short rib polydactyly syndrome overlapping both lethal and nonlethal types — PubMed (PMID:22876582)](https://pubmed.ncbi.nlm.nih.gov/22876582/)
- [short-rib thoracic dysplasia 6 with or without polydactyly — Disease Ontology Browser, DOID:0110092 (JAX/MGI)](https://www.informatics.jax.org/disease/DOID:0110092)
- [Short-rib thoracic dysplasia 6 with or without polydactyly — NIH Genetic Testing Registry (GTR), C0024507](https://www.ncbi.nlm.nih.gov/gtr/conditions/C0024507/)
- [NM_001199397.3(NEK1):c.2255A>G (p.Glu752Gly) — ClinVar RCV000625335](https://www.ncbi.nlm.nih.gov/clinvar/RCV000625335/)
- [NM_001199397.3(NEK1):c.1020+1G>A — ClinVar RCV003106460](https://www.ncbi.nlm.nih.gov/clinvar/RCV003106460/)
- [Expression of Nek1 during kidney development and cyst formation in the Nek1-deficient kat2J mouse model of PKD — PMC4422189](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4422189/) / [Journal of Biomedical Science](https://link.springer.com/article/10.1186/s12929-014-0063-5)
- [NEK1 variants confer susceptibility to amyotrophic lateral sclerosis — Nature Genetics](https://www.nature.com/articles/ng.3626)
- [Clinicopathological analysis of NEK1 variants in amyotrophic lateral sclerosis — PMC11669413 / PubMed (PMID:38986433)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11669413/)
- [NEK1 loss-of-function mutation induces DNA damage accumulation in ALS patient-derived motoneurons — PubMed (PMID:29929116)](https://pubmed.ncbi.nlm.nih.gov/29929116/)
- [Loss of function of the ALS-associated NEK1 kinase disrupts microtubule homeostasis and nuclear import — PMC10431718](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10431718/)
- [Management of Thoracic Insufficiency Syndrome in Patients With Jeune Syndrome Using the 70 mm Radius VEPTR — PubMed (PMID:25575358)](https://pubmed.ncbi.nlm.nih.gov/25575358/)
- [A simple and reliable approach for progressive internal distraction of the sternum for Jeune syndrome — PMC10562558](https://pmc.ncbi.nlm.nih.gov/articles/PMC10562558/)
- [Asphyxiating Thoracic Dystrophy — NORD](https://rarediseases.org/rare-diseases/dystrophy-asphyxiating-thoracic/)
- [Short-Rib Thoracic Dysplasia (SRTD) — Springer Nature reference work](https://link.springer.com/rwe/10.1007/978-3-319-66816-1_1651-1)
- [Prenatal Diagnosis of Jeune Syndrome — differential diagnosis of lethal skeletal dysplasias — MDPI Genes 2022](https://www.mdpi.com/2073-4425/13/8/1339)
- MONDO term lookup via OLS4 API (EBI): MONDO:0009894

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 14 |
| On topic | 5 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:21211617` *(abstract only)*: "combined haploinsufficiency of cilia formation and intraflagellar transport (IFT)"
  - closest text in source: "We found that absence of functional full-length NEK1 severely reduces cilia number and alters ciliar morphology in vivo"
- `PMID:22876582` *(abstract only)*: "overlapping both lethal and nonlethal types"
  - closest text in source: "SRPSs are a continuous spectrum of both lethal and nonlethal forms"