---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-05T15:56:25.082150'
end_time: '2026-09-05T16:00:59.722603'
duration_seconds: 274.64
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hearing Loss Autosomal Recessive 108
  mondo_id: MONDO:0033200
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
  web_search_requests: 12
  num_turns: 21
  total_cost_usd: 1.1659278
  session_id: d2f2c749-eca0-5b09-bf19-ec3a462953e3
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - mcp__pubmed__search_articles
  assistant_text_blocks: 4
citation_count: 11
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 37
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 10
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: CL:0002131
    reported_labels:
    - "auditory hair cell / inner hair cell \u2014 verify exact CL ID"
    ontology_label: regular ventricular cardiac myocyte
  - term_id: CL:0002062
    reported_labels:
    - "outer hair cell \u2014 verify"
    ontology_label: pulmonary alveolar type 1 cell
  - term_id: UBERON:0001846
    reported_labels:
    - cochlea
    ontology_label: internal ear
  - term_id: UBERON:0002105
    reported_labels:
    - inner ear
    ontology_label: vestibulo-auditory system
  unresolvable_prefixes:
  - MGI
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hearing Loss Autosomal Recessive 108
- **MONDO ID:** MONDO:0033200 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Recessive 108** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

I'll research this using PubMed and web search tools. Let me first load the necessary tool schemas, then search for authoritative information on this specific rare hearing loss locus.

Now let me pull the full PNAS paper for exact detail, and check ClinVar/gnomAD/GeneCards for supplementary data on ROR1.

I have sufficient depth from primary literature (OMIM #617654, PNAS 2016/PMID:27162350, ClinVar) plus supporting general-management literature. I'll now compile the comprehensive report.

# Hearing Loss, Autosomal Recessive 108 (DFNB108) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Autosomal recessive deafness-108 (DFNB108) is an ultra-rare, nonsyndromic form of hereditary hearing loss caused by biallelic mutation of **ROR1** (Receptor tyrosine kinase-like Orphan Receptor 1) on chromosome 1p31.3. It was first delineated in 2016 in a single consanguineous Turkish kindred, in which two affected siblings had congenital, profound sensorineural hearing loss accompanied by a distinctive inner-ear malformation (fusion of the cochlea and vestibule into a common cavity) and electrophysiologic features of auditory neuropathy (Tang et al., *PNAS* 2016, PMID:27162350). To date this remains, per the literature identified in this search, the founding and principal report defining the locus; the entry is otherwise sparsely represented in subsequent case series, consistent with its designation as an ultra-rare DFNB subtype.

**Key identifiers:**
- **OMIM:** #617654 — DEAFNESS, AUTOSOMAL RECESSIVE 108; DFNB108 (phenotype); causative gene *ROR1*, OMIM *602336 (chromosome 1p31.3)
- **MONDO:** MONDO:0033200
- **GARD (NORD/NCATS) ID:** 22658
- **Gene:** ROR1 — HGNC:10256; NCBI Gene ID 4919; RefSeq transcript NM_005012.4; genomic span chr1:63,774,017–64,181,498 (GRCh38), band 1p31.3
- **Inheritance:** Autosomal recessive
- No distinct ICD-10/ICD-11 code exists beyond the generic hereditary sensorineural hearing loss codes (ICD-10 H90.3/H90.5); no MeSH heading specific to DFNB108 was found — it is subsumed under "Deafness" (MeSH D003638) and "Hearing Loss, Sensorineural" more broadly.

**Synonyms:** Autosomal recessive nonsyndromic deafness 108; Deafness, autosomal recessive 108; DFNB108.

**Provenance of current knowledge:** This is a single-family, aggregated clinical-genetic disease-level description (OMIM/MONDO curation of one primary report), **not** an EHR-derived or population-registry-derived entity. All clinical detail traces to one kindred; no independent replication family was identified in this search.

Sources:
- [617654 - DEAFNESS, AUTOSOMAL RECESSIVE 108 - OMIM](https://omim.org/entry/617654)
- [hearing-loss-autosomal-recessive-108 - NORD/MONDO](https://rarediseases.org/mondo-disease/hearing-loss-autosomal-recessive-108/)
- [ROR1 is essential for proper innervation of auditory hair cells and hearing in humans and mice - PubMed](https://pubmed.ncbi.nlm.nih.gov/27162350/)

---

## 2. Etiology

**Disease causal factor:** Purely monogenic/genetic — homozygous missense mutation in *ROR1*. No environmental, infectious, or acquired contributing factor has been reported; this is a pure Mendelian etiology, not a multifactorial or gene-environment interaction disease.

**Genetic risk factor (the causal variant):** NM_005012.4(ROR1):c.2207G>C, p.(Arg736Thr) ("R736T"), identified by whole-exome sequencing and confirmed by Sanger sequencing in two affected siblings of a consanguineous Turkish family; it segregated with hearing loss in the pedigree (autozygosity consistent with consanguinity). ClinVar Variation ID 437889 (Accession VCV000437889.1); genomic position chr1:64,178,248 (GRCh38).

**Population frequency:** The variant was absent from ExAC, the Exome Variant Server (EVS), and 1000 Genomes Project, and was not found in 330 ethnicity-matched Turkish control chromosomes — consistent with a private, family-specific ultra-rare allele rather than a founder variant with broader carrier frequency. No gnomAD frequency data beyond "absent/not observed" were retrievable in this search.

**Modifier genes:** None reported — no modifier locus or second hit has been described for DFNB108.

**Protective factors:** None identified in the literature (genetic or environmental) — as an ultra-rare monogenic disorder, no protective-allele or lifestyle-protective-factor studies exist.

**Gene-environment interactions:** Not applicable/not reported; there is no evidence of environmental modulation of ROR1-related hearing loss.

**Consanguinity:** Directly implicated — the index family were consanguineous Turkish parents, and homozygosity for a rare private variant is the expected mechanism in such pedigrees (autozygosity mapping context implied by exome sequencing approach in a consanguineous family).

Sources:
- [NM_005012.4(ROR1):c.2207G>C (p.Arg736Thr) AND Hearing loss, autosomal recessive 108 - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000504579.2//)
- [VCV000437889.1 - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/variation/437889/)
- [617654 - OMIM](https://omim.org/entry/617654)

---

## 3. Phenotypes

All phenotype data derive from the two affected siblings in the single reported kindred (OMIM Clinical Synopsis #617654; Tang et al. 2016).

| Phenotype | Type | Onset | Severity/course | Frequency in reported cases | Suggested HPO term |
|---|---|---|---|---|---|
| Sensorineural hearing loss | Clinical sign / audiologic finding | Congenital (infancy) | Profound, apparently stable/non-progressive (no progression reported) | 2/2 reported cases | **HP:0000407** Sensorineural hearing impairment; **HP:0008619** Congenital sensorineural hearing impairment |
| Auditory neuropathy (present distortion-product otoacoustic emissions [DPOAEs] with absent/abnormal auditory brainstem response) | Laboratory/electrophysiologic abnormality | Congenital | — | 2/2 | **HP:0000407** context; auditory neuropathy is not yet a distinct dedicated HPO term in common use — best captured as sensorineural hearing loss with preserved OAEs (electrophysiologic dissociation) |
| Inner ear malformation — cochleovestibular common cavity (fusion of cochlea and vestibule into a single cavity) | Structural/imaging finding (HRCT temporal bone) | Congenital | Severe structural anomaly | 2/2 | **HP:0002655** Abnormal cochlea morphology; **HP:0011387** Abnormality of the inner ear (closest general term); common cavity deformity itself maps most precisely to **HP:0031409** or similar cochleovestibular anomaly terms — verify exact HPO ID before curation |
| Normal vestibular function / no imbalance | Negative clinical finding | Congenital (assessed) | Stable — no vestibular dysfunction despite the structural common-cavity anomaly | 2/2 | **HP:0002321** (absence of) Vertigo / balance normal — record as explicit negative |
| Normal neuromotor/gross motor development | Developmental finding | — | Normal | 2/2 | Not applicable (normal finding) |
| Speech and language delay | Developmental/behavioral | Early childhood (secondary to congenital deafness) | Present, expected consequence of profound prelingual deafness | 2/2 | **HP:0000750** Delayed speech and language development |

**Quality-of-life impact:** Not formally measured with QOL instruments in the primary report; profound prelingual, congenital deafness carries the generic QOL burden of hereditary nonsyndromic hearing loss (impact on spoken-language acquisition, communication, and, per general common-cavity literature, cochlear-implant candidacy/outcomes are typically **poorer** than in structurally normal ears — see Treatment section).

**Note on evidentiary basis:** All phenotype frequencies above are "2 of 2" because the entire phenotype description rests on a single sibling pair; this is not a population-level frequency estimate and should be flagged as such in any curated entry (small-n, single-family denominator).

Source: [Clinical Synopsis - #617654 - OMIM](https://omim.org/clinicalSynopsis/617654) (content inferred from cached search-engine excerpts of the OMIM synopsis and the PNAS primary report; OMIM's own pages returned HTTP 403 to direct fetch in this session — treat exact OMIM synopsis wording as unverified pending direct access)

---

## 4. Genetic/Molecular Information

**Causal gene:** *ROR1* (Receptor Tyrosine Kinase-Like Orphan Receptor 1), OMIM *602336, HGNC:10256, NCBI Gene 4919, chr1p31.3.

**Pathogenic variant:**
- **cDNA change:** c.2207G>C (NM_005012.4)
- **Protein change:** p.Arg736Thr (R736T)
- **Zygosity/origin:** Homozygous, germline (both affected siblings; consanguineous parents presumed obligate heterozygous carriers)
- **Variant type/class:** Missense
- **Domain affected:** Falls within/near the intracellular tyrosine-kinase domain of ROR1 (ROR1 is classified as a pseudokinase — see Mechanism). Molecular modeling in the primary report indicated the mutated residue maps to the kinase catalytic domain region and predicted a conformational change potentially impairing substrate/ligand-response interactions.
- **ACMG/ClinVar classification:** Listed in ClinVar (Variation ID 437889 / RCV000504579.2) associated with "Hearing loss, autosomal recessive 108" — classification category not independently confirmed in this search (recommend verifying current ClinVar star-rating/classification directly before citing as "Pathogenic").
- **Population frequency:** Absent from ExAC, EVS, 1000 Genomes, and 330 Turkish control chromosomes — i.e., not present in any queried reference population database, consistent with an ultra-rare/private allele.
- **Functional consequence:** Loss-of-function-type mechanism at the cell-biology level — in heterologous transfection (MDCK II cells), wild-type ROR1 trafficked normally to the plasma membrane, whereas the R736T mutant showed markedly reduced membrane localization. Functionally, in the presence of the ROR1 ligand WNT5A, mutant ROR1 failed to activate NF-κB signaling (wild-type ROR1 does activate NF-κB upon WNT5A stimulation). This supports a **loss-of-function** mechanism (`FunctionalImpactEnum: LOSS_OF_FUNCTION`, or `PARTIAL_LOSS_OF_FUNCTION` given some low residual membrane expression was noted).

**Modifier genes:** None reported.

**Epigenetic information:** No DNA methylation, histone-modification, or chromatin studies of ROR1 in the context of hearing loss were identified.

**Chromosomal abnormalities:** Not applicable — this is a single-gene missense disorder, not a copy-number or structural chromosomal disease.

**Somatic vs. germline:** Germline only in the context of DFNB108. (Note: ROR1 is separately and extensively studied as a **somatically overexpressed** oncofetal antigen in chronic lymphocytic leukemia and multiple solid tumors — this is an entirely distinct disease context and must not be conflated with the germline deafness mechanism; per dismech design decision to keep germline and somatic mechanisms separate.)

**Suggested ontology terms:**
- Gene: `hgnc:10256` (ROR1)
- GO Molecular Function candidates: GO:0004714 (transmembrane receptor protein tyrosine kinase activity) — noting ROR1 is a pseudokinase with debated catalytic activity; GO:0005112 (Notch binding) not relevant; more precisely GO:0038131 (neuregulin receptor activity) is not correct either — recommend verifying the most specific current GO MF annotation for ROR1 (Wnt receptor activity, GO:0042813, is a strong candidate given its Frizzled-like CRD domain) via OAK/AmiGO before binding.
- GO Biological Process: GO:0060042 (retina morphogenesis in camera-type eye) not relevant; better candidates: GO:0007605 (sensory perception of sound) is too generic; GO:0021675 (nerve development) and axon guidance/fasciculation terms (GO:0007409 axonogenesis; GO:0033563 dorsal/ventral axon guidance) are more mechanistically apt given the mouse phenotype (see Mechanism section) — verify each against OAK before binding.

Sources:
- [617654 & 602336 - OMIM](https://omim.org/entry/617654)
- [VCV000437889.1 - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/variation/437889/)
- [ROR1 Gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=ROR1)

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents have been reported to cause or modify DFNB108 — it is a purely monogenic disorder with no described gene-environment interaction, ototoxic exposure link, or infectious trigger. This section is **not applicable** for this entry beyond noting the general principle (shared with most nonsyndromic hereditary hearing loss) that maternal ototoxic drug exposure, perinatal infection (e.g., CMV), and noise exposure are differential-diagnostic considerations for congenital SNHL generally, but none is implicated specifically in the ROR1-associated cases reported.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (as currently supported by the primary human-genetic and mouse-model evidence; several steps are inferred from the mouse model rather than directly demonstrated in human tissue — flagged below)

1. Homozygous *ROR1* c.2207G>C (p.R736T) missense mutation **leads to** a conformational change in the ROR1 protein's kinase-domain region *(demonstrated: molecular modeling, PMID:27162350)*.
2. This conformational change **results in** impaired trafficking of ROR1 to the plasma membrane, demonstrated directly in transfected MDCK II cells (mutant protein shows markedly reduced membrane localization vs. wild-type) *(demonstrated: in vitro/heterologous cell system — evidence_source: IN_VITRO)*.
3. Reduced membrane-localized ROR1 **results in** failure to transduce the WNT5A (non-canonical Wnt) signal upon ligand binding — specifically, mutant ROR1 fails to activate NF-κB signaling in response to WNT5A, whereas wild-type ROR1 does *(demonstrated: in vitro functional assay)*.
4. Loss of WNT5A→ROR1→NF-κB (and, by extension, non-canonical Wnt/planar-cell-polarity–type) signaling in the developing inner ear **leads to** (inferred primarily from the *Ror1*-mutant mouse model, not directly shown in human tissue — evidence_source: MODEL_ORGANISM, directness: INDIRECT relative to the human disease):
   - **Branch A — Cochlear morphogenesis defect:** impaired convergent-extension-type morphogenesis **results in** an under-coiled, shortened cochlea, phenocopying the disrupted-Wnt-PCP cochlear elongation phenotype seen with loss of other Wnt5a-pathway components (*Wnt5a*-knockout mice independently show a shortened cochlea and rotated stereociliary bundles, supporting a shared pathway). In the human patients this branch is presumed to correspond to the **common cavity inner-ear malformation** seen on HRCT (fusion of cochlea and vestibule) — this specific structural correspondence between the mouse cochlear-coiling defect and the human common-cavity anomaly is an **inference**, not a demonstrated one-to-one mapping.
   - **Branch B — Spiral ganglion neuron (SGN) innervation defect:** loss of ROR1 function in spiral ganglion neuron growth cones **leads to** axon fasciculation defects, which **result in** (i) impaired/absent synapse formation between type I SGN afferents and inner hair cells (with postsynaptic glutamate receptor clusters not detectable at some contacts), and (ii) aberrant, mistargeted projections of type II SGN afferents through the sensory epithelium (normally type II afferents innervate outer hair cells). This SGN innervation failure **is proposed to explain** the human auditory-neuropathy electrophysiologic pattern (preserved cochlear amplifier function → present otoacoustic emissions, but absent/abnormal neural transmission → profound hearing loss on auditory brainstem response) — again, this human-mouse correspondence is inferred by analogy rather than directly tested in human inner-ear tissue (which is inaccessible for biopsy).
5. The combined structural (cochlear shortening) and neural (afferent innervation failure) deficits **culminate in** profound congenital sensorineural hearing loss with an auditory-neuropathy electrophysiologic signature, while sparing vestibular function — consistent with the mouse model showing **normal vestibular anatomy, no circling/balance abnormality, and normal rotarod performance** despite the cochlear and SGN phenotypes, and consistent with the human patients' normal balance/neuromotor development.

### Category detail

- **Molecular pathways:** Non-canonical WNT signaling (WNT5A–ROR1 axis) → NF-κB activation; ROR1 also participates more broadly in planar cell polarity (PCP)–type signaling relevant to cochlear duct elongation (a mechanism it likely shares with other PCP genes implicated in cochlear coiling defects, though this was not itself directly tested in the primary report beyond the parallel drawn to *Wnt5a*-null mice).
- **Cellular processes:** Axon guidance/fasciculation of spiral ganglion neurons; convergent-extension-type morphogenetic movements during cochlear duct elongation; synaptogenesis (afferent neuron–hair cell synapse formation).
- **Protein dysfunction:** ROR1 is normally a type I transmembrane glycoprotein with an extracellular immunoglobulin-like domain, a Frizzled-homologous cysteine-rich domain (CRD, the WNT5A-binding module), and a kringle domain, plus an intracellular tyrosine-kinase-like (pseudokinase) domain. The R736T mutation causes **defective membrane trafficking** (protein retained intracellularly rather than reaching the plasma membrane) — a loss-of-function mechanism at the level of protein localization, compounding any intrinsic catalytic/signaling defect.
- **Biochemical abnormality:** Failure of ligand (WNT5A)-induced NF-κB pathway activation — an intracellular signal-transduction defect downstream of a receptor-trafficking defect.
- **Tissue damage mechanism:** Not classical damage (necrosis/fibrosis) but a **developmental patterning/innervation failure** — i.e., this is a malformation/miswiring disorder rather than a degenerative one; no evidence of postnatal progressive hair-cell death was reported.
- **Immune system involvement:** None directly relevant to the deafness mechanism, despite NF-κB (canonically an immune/inflammatory pathway) being the downstream readout used experimentally — its role here is developmental/neuronal, not immunological.
- **Epigenetic changes:** None reported.
- **Molecular/omics profiling:** No transcriptomic, proteomic, or single-cell profiling of ROR1-mutant human or mouse inner ear was identified in this search beyond the targeted immunohistochemistry/electrophysiology used in the primary paper (SGN axon tracing, synaptic marker staining, ABR/DPOAE electrophysiology, HRCT imaging).

**Suggested GO/CL terms for pathophysiology nodes** (verify each via OAK before binding, per dismech term-validation policy):
- GO:0007409 axonogenesis / GO:0042060 wound healing (not relevant) — better: axon fasciculation-specific GO terms should be searched directly (e.g., GO:0007413 axonal fasciculation)
- GO:0060429 epithelium development / cochlear duct morphogenesis-specific terms (search GO for "cochlear duct morphogenesis")
- Cell types: CL:0000101 (sensory neuron) is too generic — spiral ganglion neuron type I and type II afferent subtypes should be searched in CL specifically (e.g., "type I spiral ganglion neuron," "type II spiral ganglion neuron") if present; inner hair cell (CL:0002131) and outer hair cell (CL:0002062) as the postsynaptic/target cell types.

**Note on evidence-source discipline:** Per dismech curation rules, the human-derived findings (variant identification, segregation, HRCT imaging, audiometry/ABR/OAE) are `HUMAN_CLINICAL`; the transfection/membrane-trafficking and NF-κB signaling assays are `IN_VITRO`; the *Ror1*-knockout mouse cochlear, SGN, and behavioral phenotyping is `MODEL_ORGANISM`. The mouse-to-human mechanistic bridge (steps 4–5 above) should be flagged in any dismech entry as model-organism-derived mechanistic inference, not directly demonstrated human pathophysiology — a candidate for a `HUMAN_MODEL_MISMATCH`-type discussion node given that human inner-ear tissue was never directly examined.

Source: [ROR1 is essential for proper innervation of auditory hair cells and hearing in humans and mice - PNAS/PubMed, PMID:27162350](https://pubmed.ncbi.nlm.nih.gov/27162350/)

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary organ: Inner ear (cochlea and vestibule) — bilateral involvement implied (both siblings affected, bilateral profound SNHL).
- Secondary/systemic involvement: None — this is a **nonsyndromic** disorder; no other organ system is affected. Speech/language delay is a downstream developmental consequence of deafness, not a direct disease manifestation of another organ.
- Body system: Auditory/nervous system (cochleovestibular apparatus and its afferent innervation by the VIIIth cranial nerve/spiral ganglion).

**Tissue/cell level:**
- Cochlear duct epithelium; organ of Corti (inner and outer hair cells); spiral ganglion (bipolar sensory neurons, type I afferents to inner hair cells, type II afferents to outer hair cells).
- Suggested Cell Ontology terms: CL:0002131 (auditory hair cell / inner hair cell — verify exact CL ID), CL:0002062 (outer hair cell — verify), spiral ganglion neuron subtypes (search CL directly for type I/II).

**Subcellular level:**
- Plasma membrane (site of normal ROR1 localization; defective in the R736T mutant) — GO Cellular Component: GO:0005886 (plasma membrane).
- Axon growth cone (site of ROR1-mediated axon guidance) — GO:0030426 (growth cone).

**Localization:**
- Bilateral (both ears affected in both siblings; no laterality asymmetry reported).
- Suggested UBERON terms: UBERON:0000955 is brain (not this); relevant terms — UBERON:0001846 (cochlea), UBERON:0001846-adjacent vestibule terms, UBERON:0002105 (inner ear) — verify exact IDs via OAK before binding; "common cavity" as a malformed fused cochleovestibular structure may not have a precise single UBERON term and could require a qualifier/descriptor approach.

---

## 8. Temporal Development

- **Onset:** Congenital — hearing loss is present from birth/infancy in both reported cases; no reported cases of later-onset or progressive worsening.
- **Onset pattern:** Not acute/insidious in the acquired-disease sense — it is a static congenital malformation/miswiring defect present from birth.
- **Progression:** No progression documented; the report does not describe worsening over the observation period (available follow-up duration in the two siblings was not detailed further in retrievable sources — recommend flagging as "stability status incompletely documented beyond initial diagnosis" if precise longitudinal follow-up data cannot be confirmed from the primary paper).
- **Disease course pattern:** Stable/non-progressive as best described (congenital and static, characteristic of a structural/developmental innervation defect rather than a degenerative process).
- **Disease duration:** Lifelong (congenital sensorineural hearing loss is permanent).
- **Critical period:** The critical developmental window is prenatal cochlear/SGN morphogenesis (ROR1-dependent inner-ear patterning and afferent innervation occurs during embryonic and early postnatal inner-ear development in the mouse model) — i.e., pathogenesis is complete before or shortly after birth, meaning there is no known postnatal therapeutic window to prevent the structural/innervation defect (in contrast to some progressive hearing-loss genes where early intervention could theoretically slow decline).

---

## 9. Inheritance and Population

- **Epidemiology:** No prevalence or incidence estimate exists — DFNB108 has been described in a single consanguineous family (2 affected siblings), making it one of the rarest of the >100 known DFNB loci. It cannot be assigned even an Orphanet numeric prevalence band; classify (per dismech `PrevalenceClassEnum`) as effectively `CASES_IN_LITERATURE` / ultra-rare, with only 2 reported cases worldwide in the literature identified by this search.
- **Inheritance pattern:** Autosomal recessive (DFNB nomenclature confirms this — "DFNB" prefix denotes autosomal recessive nonsyndromic deafness loci, as opposed to DFNA [dominant] or DFNX [X-linked]).
- **Penetrance:** Presumed complete in the homozygous state (both homozygous siblings affected); no data on incomplete penetrance.
- **Expressivity:** Consistent between the two reported siblings (both had profound congenital SNHL with the same common-cavity malformation) — apparently uniform expressivity, though n=2 limits generalization.
- **Genetic anticipation:** Not applicable (missense variant, not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported/assessed.
- **Founder effect:** Not established — the variant was not found in 330 Turkish population controls, arguing against a Turkish founder allele; more consistent with a private familial variant arising independently in this consanguineous pedigree.
- **Consanguinity:** Central to this family's presentation — parents were consanguineous, consistent with autozygosity for a rare recessive allele, the classic mechanism by which private recessive-deafness alleles are discovered in relatively small, well-documented pedigrees.
- **Carrier frequency:** Unknown/not estimated in any population database (absent from ExAC, EVS, 1000 Genomes).
- **Affected population/geographic distribution:** Reported only in a Turkish family; no other ethnic group or geographic region has been reported to carry this variant or locus to date, per this search.
- **Sex ratio:** No sex bias expected or reported (autosomal recessive; both reported affected siblings' sexes were not specified in the retrievable abstracts).
- **Age distribution:** Congenital onset only — no adult-onset cases described.

---

## 10. Diagnostics

**Clinical/audiologic tests:**
- Standard newborn hearing screening (otoacoustic emissions [OAE] + automated auditory brainstem response [AABR]) would be expected to show a characteristic **"pass" on OAE but "refer/abnormal" on ABR** pattern — the auditory-neuropathy signature reported in this family (present DPOAEs with absent/abnormal ABR) is diagnostically important because it distinguishes cochlear (hair-cell) causes of deafness from neural/synaptic causes, and should prompt genetic and imaging work-up rather than being dismissed as a screening artifact.
- Pure-tone/behavioral audiometry once developmentally feasible: profound bilateral SNHL.
- Suggested LOINC: standard audiometry and ABR/OAE LOINC codes apply generically; no disease-specific biomarker or laboratory test exists.

**Imaging:**
- High-resolution CT (HRCT) of the temporal bones is the key imaging diagnostic — identifies the **common cavity deformity** (fusion of cochlea and vestibule into one chamber), a major/hallmark structural finding in this family. MRI of the internal auditory canals could complementarily assess the cochlear nerve.

**Genetic testing:**
- Given the auditory-neuropathy-plus-inner-ear-malformation phenotype and lack of a distinctive syndromic pattern, whole-exome sequencing (as used in the discovery family) or a comprehensive hereditary hearing-loss gene panel (which would need to specifically include *ROR1*, since it is not part of most legacy/older deafness panels given its very recent disease association) is the appropriate testing strategy. Single-gene *ROR1* Sanger sequencing is reasonable for segregation confirmation once a proband variant is found, and in populations/families with known consanguinity, homozygosity mapping/autozygosity analysis alongside exome sequencing is efficient (as was done in the discovery family).
- Chromosomal microarray/karyotype/FISH: Not applicable — DFNB108 is not caused by a copy-number or chromosomal rearrangement.
- Mitochondrial DNA testing: Not applicable (nuclear gene disorder).

**Differential diagnosis:** Other DFNB loci associated with inner-ear malformations and/or auditory neuropathy should be considered, including *OTOF*-related auditory neuropathy (DFNB9, normal inner-ear anatomy typically), *PJVK/DFNB59*, and other cochleovestibular malformation syndromes (e.g., Pendred syndrome/*SLC26A4* for enlarged vestibular aqueduct — distinguishable by imaging pattern and syndromic features such as goiter). Common cavity deformity itself has a broad differential including CHARGE syndrome and other inner-ear dysplasias, which should be excluded by absence of syndromic features.

**Screening:** Standard universal newborn hearing screening would detect the profound hearing loss; there is no ROR1-specific population carrier-screening program given the ultra-rarity of the variant/locus.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No excess mortality — DFNB108 is a nonsyndromic hearing-only disorder with no reported systemic or life-limiting complications; normal life expectancy is expected.
- **Morbidity/function:** The principal morbidity is profound, permanent, prelingual sensorineural hearing loss with attendant speech and language delay if unaddressed. No other organ dysfunction.
- **Disease course:** Static/stable rather than progressive, based on available data; no reported additional complications (vestibular symptoms, balance problems) despite the structural inner-ear anomaly — vestibular function was specifically documented as preserved.
- **Recovery potential/treatment response:** With early identification (newborn screening) and appropriate intervention (hearing aids trial, then cochlear implantation given the profound/neuropathy phenotype and poor expected benefit from amplification alone), speech-language outcomes can be substantially improved, though outcomes in common-cavity-deformity ears are documented in the general cochlear-implant literature to be **worse on average** than implantation in structurally normal cochleae (see Treatment, below) — no DFNB108-specific implant outcome data exist; this is an inference from the general common-cavity-deformity literature.
- **Prognostic factors:** Timing of diagnosis and intervention (implantation) is the major modifiable prognostic factor for language outcomes, as with any prelingual profound SNHL; the structural common-cavity anomaly itself is a general negative prognostic factor for cochlear-implant electrode-neural interface efficacy.

---

## 12. Treatment

**Pharmacotherapy:** None — there is no drug therapy for DFNB108; it is a structural/developmental sensorineural hearing loss, not a treatable inflammatory, metabolic, or channelopathic process.

**Advanced therapeutics (gene therapy, RNA-based therapy):** None developed or in trials specific to ROR1-related deafness. (Note: ROR1-targeted therapeutics — monoclonal antibodies such as cirmtuzumab, and ROR1-directed CAR-T cell therapies — exist in active clinical development, but these target **somatic ROR1 overexpression in malignancy** (e.g., CLL, mantle cell lymphoma) and are wholly unrelated to the germline hearing-loss mechanism; they must not be conflated with a treatment for DFNB108.)

**Devices/surgical/interventional (the actual standard of care for this phenotype):**
- **Hearing aids:** First-line trial for amplification, though likely of limited benefit given the auditory-neuropathy component (poor benefit from amplification is typical when neural synchrony/transmission, not just cochlear amplification, is impaired).
- **Cochlear implantation:** The most relevant intervention given profound bilateral SNHL with an auditory-neuropathy pattern and common-cavity malformation. Suggested NCIT term: `NCIT:C15329` (Surgical Procedure) for `treatment_term`, with `preferred_term` capturing "cochlear implantation," and (per the dismech device-binding convention) a `qualifiers` predicate-value pair for `NCIT:C157820` (Cochlear Implant) as the device, following the pattern used in other inner-ear malformation entries (e.g., Jervell and Lange-Nielsen Syndrome 1, Labyrinthitis). General common-cavity-deformity literature (not DFNB108-specific) reports overall poorer — but still meaningful — auditory performance and speech-intelligibility gains post-implantation compared with structurally normal ears; trans-mastoid labyrinthotomy is a commonly used surgical approach, and electrode-to-cavity-wall contact is an important technical determinant of outcome in these malformed cavities.
- **Speech and language therapy / early intervention (NCIT:C159273 Speech Therapy):** Central to management given the expected speech-language delay from prelingual profound deafness.
- **Genetic counseling (NCIT:C15240):** Recommended for the family given the autosomal recessive inheritance and consanguinity, including recurrence-risk counseling (25% recurrence risk for future pregnancies of carrier parents) and discussion of prenatal/carrier testing options for at-risk relatives.

**Experimental/clinical trials:** No NCT-registered clinical trial for DFNB108 specifically was identified.

**Treatment strategy:** Standard hereditary-profound-SNHL pathway — newborn screening → confirmatory audiologic/electrophysiologic testing (revealing the auditory-neuropathy pattern) → temporal bone imaging (revealing common cavity) → genetic diagnosis → hearing aid trial (likely limited benefit) → cochlear implantation as definitive intervention, ideally early in infancy to optimize the critical period for spoken-language development → ongoing speech-language therapy and audiologic follow-up.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the classic sense (no modifiable exposure to avoid); the only "primary prevention" lever is reproductive/genetic — carrier testing and reproductive counseling in families with a known pathogenic *ROR1* allele, and general avoidance of consanguineous union is a population-level (not disease-specific) recommendation relevant to reducing recessive-disease burden broadly.
- **Secondary prevention (early detection):** Universal newborn hearing screening (OAE + AABR) is the key secondary-prevention/early-detection tool — critically, because this disorder produces a "pass" pattern on OAE-only screening protocols (auditory neuropathy spares outer hair cell/cochlear amplifier function), screening programs that rely on OAE alone without AABR risk missing this phenotype; AABR-inclusive protocols (as used in most modern universal newborn hearing screening programs) are essential for detection.
- **Genetic/carrier screening:** Given the ultra-rarity and family-specific nature of the reported variant, population carrier screening is not currently feasible or recommended; testing is appropriate for at-risk relatives once a familial variant is identified, and preimplantation genetic diagnosis / prenatal testing could be offered to carrier couples on request.
- **Genetic counseling:** As above — 25% recurrence risk per pregnancy for two carrier parents; standard autosomal recessive counseling framework.
- **Public health/environmental interventions:** Not applicable (no environmental risk factor to mitigate).
- **Prophylaxis:** None.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *ROR1* orthologs are highly conserved; the relevant model species is mouse (*Mus musculus*, NCBITaxon:10090).
- **Gene ortholog:** *Ror1* (mouse), MGI:1347520, NCBI Gene (mouse Ror1) — direct ortholog of human ROR1, used to generate the knockout model central to mechanistic understanding.
- **Naturally occurring disease in other species:** No naturally occurring (spontaneous) *Ror1*-associated deafness has been reported in companion animals or wildlife (unlike, e.g., some other deafness genes with recognized veterinary counterparts in dogs); the only *Ror1*-deficient animal model identified is an engineered laboratory knockout mouse, not a spontaneously occurring veterinary disease. No OMIA (Online Mendelian Inheritance in Animals) entry for a natural ROR1-associated deafness was found in this search.
- **Comparative biology:** The mouse *Ror1* knockout recapitulates the core human phenotype components — profound deafness, cochlear structural anomaly (shortened/under-coiled cochlea, analogous in principle to the human common-cavity malformation, though not anatomically identical), and afferent innervation defects — while diverging in that mouse vestibular anatomy and function are preserved, mirroring (and here directly informing/confirming) the preserved vestibular function seen in the human patients.
- **Zoonotic potential/cross-species susceptibility:** Not applicable (non-infectious, monogenic disorder).

---

## 15. Model Organisms

**Primary model: *Ror1*-knockout mouse (MGI:1347520)**

- **Model type:** Mammalian, genetic knockout (constitutive loss-of-function, not a knock-in of the specific human R736T missense allele — an important fidelity caveat, since it models complete loss of ROR1 function rather than the specific partial-trafficking-defect mechanism of the human missense variant).
- **Phenotype recapitulation:**
  - **High-fidelity recapitulation:** Severe deafness; cochlear structural anomaly (under-coiled, shortened cochlea, with increased hair-cell density toward the apex consistent with impaired convergent extension); spiral ganglion neuron axon fasciculation defects; impaired/absent type I afferent synapses onto inner hair cells (postsynaptic glutamate receptor clusters not detected); aberrant type II afferent projections through the sensory epithelium; **preserved otoacoustic emissions** (directly mirroring the human auditory-neuropathy electrophysiologic signature); **normal vestibular anatomy and function** (no circling behavior, normal rotarod performance) — directly mirroring the human patients' preserved balance.
  - **Partial/uncertain correspondence:** Organ of Corti width appears unaffected; stereociliary bundle orientation is normal at P5 in the mouse — the mouse model's cochlear malformation (shortened/under-coiled duct) is not anatomically identical to the human "common cavity" (complete fusion of cochlea and vestibule), representing a **species/anatomical-scale divergence** worth flagging as a `PROXY_QUANTITY` or `BOUNDARY_OMISSION`-type divergence if curated under the dismech `modeled_mechanisms` framework: the model demonstrates a cochlear coiling/morphogenesis defect and an SGN innervation defect (both at the tissue/cellular scale) that are used to explain, by inference, the human common-cavity structural anomaly and auditory-neuropathy phenotype — but the mouse model was generated as a constitutive null, not a knock-in of the exact patient variant, so it tests loss of ROR1 function generally rather than the specific partial-trafficking-defective allele found in the family.
- **Model limitations:** (1) Constitutive knockout vs. patient-specific missense knock-in — mechanistic fidelity to the precise molecular lesion (partial membrane-trafficking defect) is inferred, not proven, since the mouse model was not engineered to carry the R736T-equivalent allele; (2) the mouse cochlear malformation (shortened/under-coiled duct) is not a direct anatomical phenocopy of the human common-cavity deformity (complete cochleovestibular fusion) — an interspecies anatomical-scale/severity divergence; (3) no independent human inner-ear histopathology exists to confirm that the SGN innervation defects seen in mouse actually occur identically in the human patients (inaccessible tissue) — this is an upward extrapolation from a cellular/tissue-scale mouse observation to an inferred human mechanism.
- **Applications:** The model has been used to dissect the WNT5A–ROR1–NF-κB signaling axis in cochlear afferent innervation and duct morphogenesis, and to establish that ROR1 loss produces an auditory-neuropathy-type electrophysiologic signature (preserved OAE, disrupted neural transmission) analogous to the human presentation.
- **Resources:** MGI:1347520 (Ror1); International Mouse Phenotyping Consortium (IMPC) gene page for Ror1 (mousephenotype.org) — for anyone seeking additional standardized phenotyping data beyond the primary research report.

**Other model systems:** No zebrafish, *Drosophila*, *C. elegans*, yeast, iPSC-derived, or organoid model of ROR1-associated hearing loss was identified in this search. The MDCK II (Madin-Darby Canine Kidney) cell transfection system used for the membrane-trafficking and NF-κB signaling assays is an **in vitro heterologous cell-line model**, not a disease-relevant inner-ear cell system — useful for testing the specific variant's biochemical/trafficking consequence, but not for recapitulating tissue-level auditory phenotypes.

---

## Summary Table of Key Ontology/Identifier Suggestions for Curation

| Domain | Suggested term (verify via OAK before binding) |
|---|---|
| Disease | MONDO:0033200; OMIM:617654 |
| Gene | hgnc:10256 (ROR1) |
| Variant | ClinVar VCV000437889.1; NM_005012.4:c.2207G>C (p.Arg736Thr) |
| Phenotype | HP:0000407 (Sensorineural hearing impairment); HP:0008619 (Congenital SNHL); HP:0000750 (Delayed speech and language development); HP:0002655 or nearest cochlear-morphology term (verify exact common-cavity-deformity HPO ID) |
| Anatomy | UBERON term for cochlea/inner ear (verify exact ID) |
| Cell types | Spiral ganglion neuron (type I / type II afferent), inner/outer hair cell — verify exact CL IDs |
| GO Molecular Function | ROR1/WNT5A receptor activity — verify exact GO ID |
| GO Biological Process | Axon fasciculation / cochlear duct morphogenesis-related terms — verify exact GO IDs |
| Treatment | NCIT:C15329 (Surgical Procedure, for cochlear implantation) + qualifier NCIT:C16830 (Medical Device)/NCIT:C157820 (Cochlear Implant); NCIT:C159273 (Speech Therapy); NCIT:C15240 (Genetic Counseling) |
| Model organism | MGI:1347520 (mouse Ror1) |

---

### Important evidentiary caveats for curation

1. **Single-family disease.** Essentially all clinical/phenotypic content in Sections 3, 7–11 traces to one consanguineous Turkish kindred (2 affected siblings) reported in a single primary paper (PMID:27162350). No independent replication cohort was found in this search — treat any "typically" or frequency-style statement as n=2, not a population estimate.
2. **OMIM direct-access limitation.** Both OMIM URLs (entry #617654 and its Clinical Synopsis) returned HTTP 403 to direct WebFetch in this session; the content attributed to OMIM above was reconstructed from third-party search-engine cached excerpts and cross-referenced against the PNAS primary paper and ClinVar. Before finalizing any dismech YAML entry, the exact OMIM clinical synopsis wording and the PNAS full-text (Methods/Results, particularly exact family pedigree structure, precise electrophysiology traces, and any additional case detail) should be independently re-verified from primary sources (e.g., via `just fetch-reference PMID:27162350` and direct OMIM/PNAS access) rather than relying on this search-engine-mediated report.
3. **PubMed MCP tool access was denied by permission** in this session, so full abstract text and citation-linked metadata for PMID:27162350 could not be independently confirmed beyond what surfaced through general web search; the PMID itself is corroborated by multiple independent search results (PubMed, PNAS, ClinVar) and should be considered reliable, but exact quoted abstract text should be pulled directly before use as a `snippet:` in any evidence item.

Sources:
- [617654 - DEAFNESS, AUTOSOMAL RECESSIVE 108; DFNB108 - OMIM](https://omim.org/entry/617654)
- [Clinical Synopsis - #617654 - OMIM](https://omim.org/clinicalSynopsis/617654)
- [602336 - RECEPTOR TYROSINE KINASE-LIKE ORPHAN RECEPTOR 1; ROR1 - OMIM](https://omim.org/entry/602336)
- [ROR1 is essential for proper innervation of auditory hair cells and hearing in humans and mice - PubMed (PMID:27162350)](https://pubmed.ncbi.nlm.nih.gov/27162350/)
- [ROR1 is essential for proper innervation of auditory hair cells and hearing in humans and mice - PNAS](https://www.pnas.org/doi/full/10.1073/pnas.1522512113)
- [hearing loss, autosomal recessive 108 - NORD/MONDO/GARD](https://rarediseases.org/mondo-disease/hearing-loss-autosomal-recessive-108/)
- [NM_005012.4(ROR1):c.2207G>C (p.Arg736Thr) AND Hearing loss, autosomal recessive 108 - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000504579.2//)
- [VCV000437889.1 - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/variation/437889/)
- [ROR1 Gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=ROR1)
- [Ror1 MGI Mouse Gene Detail - MGI:1347520](https://www.informatics.jax.org/marker/MGI:1347520)
- [Analysis of Long-Term Cochlear Implantation Outcomes and Correlation With Imaging Characteristics in Patients With Common Cavity Deformity - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8983960/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 14 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CL:0002131` (2 mentions) - the report calls it "auditory hair cell / inner hair cell — verify exact CL ID"; CL calls it **regular ventricular cardiac myocyte**
- `CL:0002062` (2 mentions) - the report calls it "outer hair cell — verify"; CL calls it **pulmonary alveolar type 1 cell**
- `UBERON:0001846` (2 mentions) - the report calls it "cochlea"; UBERON calls it **internal ear**
- `UBERON:0002105` (1 mention) - the report calls it "inner ear"; UBERON calls it **vestibulo-auditory system**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MGI:1347520` - called "Ror1", "mouse Ror1"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`, `OMIM`.