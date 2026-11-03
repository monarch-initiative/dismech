---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-15T15:31:28.383021'
end_time: '2026-10-15T15:35:53.664553'
duration_seconds: 265.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Arthrogryposis, Cleft Palate, Craniosynostosis, and Impaired Intellectual
    Development
  mondo_id: MONDO:0032642
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
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 5
  num_turns: 30
  total_cost_usd: 2.2546899999999996
  session_id: 2e517c33-ca91-436f-9826-11d751a58e0f
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  - mcp__pubmed__search_articles
  assistant_text_blocks: 3
citation_count: 9
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 11
  on_topic: 8
  off_topic: 1
  off_topic_references:
  - PMID:33338510
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 60
  verified: 56
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 22
  labels_variant: 6
  unresolvable_prefixes:
  - OMIM
  - MIM
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Arthrogryposis, Cleft Palate, Craniosynostosis, and Impaired Intellectual Development
- **MONDO ID:** MONDO:0032642 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Arthrogryposis, Cleft Palate, Craniosynostosis, and Impaired Intellectual Development** covering all of the
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

Gathering the remaining primary sources (full-text variant details and the 2021 regulatory-domain series), then I'll write the report.

Still collecting sources — now checking ClinVar and OMIM-derived records for the exact autoinhibitory-domain variants.

# Research report: Arthrogryposis, Cleft Palate, Craniosynostosis, and Impaired Intellectual Development (ACCIID; PPP3CA gain of function)

**Scope and limits of this report.**
- **Very little literature exists.** The disorder rests on two published patients in a single paper (Mizuguchi et al. 2018, PMID:29432562). No follow-up series of autoinhibitory-domain cases turned up in a Europe PMC sweep of 155 PPP3CA hits.
- **Two kinds of section.** Sections that depend on population data, natural history, trials or animal models are mostly marked *not available*. Others are filled from the closely related PPP3CA loss-of-function disorder, DEE91. Those are labelled as cross-disorder inference.
- **What I could and could not read.** I read the Mizuguchi abstract verbatim from the repository's cached copy (`references_cache/PMID_29432562.md`). The full text is behind a paywall and has no PMC copy, so I did not read it. Variant positions come from UniProt Q08209 and phenotype frequencies from the HPO annotation file for OMIM:618265. Both were read directly.
- **Unverified items.** The PubMed MCP search was not authorised in this session. Any PMID below marked "(unverified)" is from memory and must be checked with `just fetch-reference` before it is cited.

---

## 1. Disease information

**Overview.** ACCIID is an autosomal dominant multiple congenital anomaly syndrome. It is caused by de novo heterozygous missense variants in the **autoinhibitory (AI) domain** of *PPP3CA*, which encodes calcineurin A-alpha, the catalytic subunit of the Ca²⁺/calmodulin-dependent serine/threonine phosphatase. The variants activate calcineurin. Loss-of-function variants in the catalytic domain cause a different disorder, developmental and epileptic encephalopathy 91 (DEE91, OMIM 617711). This is a striking allelic split by functional direction.

The source paper states it directly (PMID:29432562): *"the AI domain mutations were associated with multiple congenital abnormalities including craniofacial dysmorphism, arthrogryposis and short stature"* and *"the catalytic and AI domain mutations visibly result in decreased and increased calcineurin signaling, respectively."*

**UniProt (Q08209) disease summary for ACCIID (MIM:618265), paraphrased:** an autosomal dominant disorder with moderate to severe intellectual disability, craniosynostosis, cleft palate, micrognathia, arthrogryposis and short stature. Some patients have bone abnormalities or generalised seizures.

| Identifier | Value |
|---|---|
| MONDO | MONDO:0032642 ("arthrogryposis, cleft palate, craniosynostosis, and impaired intellectual development") |
| OMIM | 618265 |
| Orphanet | ORPHA:565858 (from MONDO xref; Orphanet page not readable this session) |
| GARD | 0018001 |
| MedGen / UMLS | 1648372 / C4748872 |
| ICD-11 | LD2F.1Y (per KEGG H02641) |
| MeSH | D000015 (Abnormalities, Multiple; per KEGG) |
| KEGG DISEASE | H02641 |
| Synonyms | ACCIID; PPP3CA-related multiple congenital anomaly syndrome; PPP3CA gain-of-function syndrome |

**Source type.** The information is aggregated at disease level (OMIM, HPO, UniProt), but all of it derives from two individual case descriptions.

## 2. Etiology

- **Cause.** Germline, de novo, heterozygous gain-of-function missense variants in the PPP3CA AI domain (residues 465–487 in UniProt). OMIM/PanelApp summarise: *"In 2 patients with ACCIID, Mizuguchi et al. (2018) identified de novo heterozygous mutations in the autoinhibitory domain of the PPP3CA gene… Using a yeast model, the mutations were found to be constitutively activating."*
- **Genetic risk factors.** Only the causal gene is known. No modifier genes, susceptibility loci or GWAS signals have been reported.
- **Environmental risk factors.** None reported. The disorder is not expected to have any; it is a de novo monogenic developmental disorder.
- **Protective factors and gene–environment interactions.** None reported.
- **Evidence strength.**
  - Genomics England / PanelApp Australia list PPP3CA as green (high evidence) on the arthrogryposis panel.
  - The VCGS fetal-anomalies panel rates the gain-of-function association amber: *"only 2 individuals reported."*
  - No ClinGen gene–disease validity record for PPP3CA–ACCIID was found. Record `gene_disease_validity` only if a CGGV assertion exists; leave it absent otherwise.

## 3. Phenotypes

All phenotype data come from the HPO annotation file for OMIM:618265, which cites only PMID:29432562 (n = 2). Frequencies are therefore n/2, and n/1 where only one patient was assessed. Onset is congenital for the structural anomalies. The HPO file also carries "Congenital onset" (1/2) and "Third trimester onset" (1/2), the latter reflecting the prenatal hydrops case.

| Phenotype | HP term | Freq. | Type / notes |
|---|---|---|---|
| Arthrogryposis multiplex congenita | HP:0002804 | 2/2 | Congenital sign; defining feature |
| Cleft palate | HP:0000175 | 2/2 | Congenital malformation |
| Craniosynostosis | HP:0001363 | 2/2 | Severe in one patient (abstract: "severe craniosynostosis") |
| Trigonocephaly | HP:0000243 | 1/2 | Suture-specific skull shape |
| Plagiocephaly | HP:0001357 | 1/2 | |
| Decreased calvarial ossification | HP:0005474 | 1/1 | Co-occurs with synostosis in the severe case |
| Micrognathia | HP:0000347 | 2/2 | |
| Retrognathia | HP:0000278 | 2/2 | |
| Brachydactyly | HP:0001156 | 2/2 | |
| Short stature | HP:0004322 | 2/2 | |
| Decreased body weight | HP:0004325 | 2/2 | |
| Thin ribs | HP:0000883 | 1/2 | Abstract: "gracile bones (severe bone slenderness and perinatal fractures)" |
| Slender long bone | HP:0003100 | 1/1 | |
| Perinatal fractures | suggest HP:0002659 *Increased susceptibility to fractures* | 1/2 | Stated in the abstract; not in the HPO annotation file. Verify the term. |
| Global developmental delay | HP:0001263 | 2/2 | Neurodevelopmental |
| Intellectual disability | HP:0001249 | 2/2 | UniProt: moderate to severe |
| Generalized-onset seizure | HP:0002197 | 1/2 | Far less prominent than in DEE91 |
| Nonimmune hydrops fetalis | HP:0001790 | 1/2 | Prenatal |
| Hydronephrosis | HP:0000126 | 1/2 | Renal / urinary tract |
| Vesicoureteral reflux | HP:0000076 | 1/2 | |

**Severity, progression and quality of life.**
- Structural anomalies are congenital and static.
- Neurodevelopmental impairment is lifelong.
- The fracture and bone-fragility phenotype is described in one perinatal case only.
- No QoL instruments or longitudinal data exist. Burden would plausibly come from contractures, cleft palate (feeding, speech) and ID, but this is inference, not data.

## 4. Genetic and molecular information

**Gene.** *PPP3CA*, HGNC:9314 (repository form `hgnc:9314`; verify against `cache/hgnc/terms.csv`). NCBI Gene 5530. Chromosome 4q24. OMIM gene 114105 (verify).

**Protein architecture** (UniProt Q08209):
- catalytic phosphatase domain, with Fe³⁺/Zn²⁺ metal ligands His90, His92, Asp118, His150, His199 and His281
- calcineurin B-binding helix: 341–369
- calmodulin-binding region: 392–406
- autoinhibitory segment: 407–414
- **autoinhibitory domain: 465–487**

**ACCIID variants (UniProt variant annotations):**

| Variant | Domain | Origin | Functional class |
|---|---|---|---|
| p.Phe470Leu (F470L; VAR_081902) | AI domain | de novo, heterozygous | Gain of function (increased signalling in yeast) |
| p.Ala473Thr (A473T) | AI domain | de novo, heterozygous | Gain of function |

- **cDNA nomenclature.** c. notation (NM_000944.5) was not confirmed in this session. Read it from the full text or ClinVar before curating.
- **ClinVar.** About 60 PPP3CA records carry the ACCIID trait, but nearly all are VUS lumped across DEE91 and ACCIID by testing laboratories. Examples:
  - c.1427T>C p.Leu476Ser: VUS, ACCIID only. It lies in the AI domain, so it is a candidate, not an established case.
  - c.1302C>A p.Ser434Arg: VUS.
  - c.1246_1248dup p.Glu416_Ser417insGlu: VUS.

  Do not cite these as disease-causing.
- **Allele frequency.** Expected to be absent from gnomAD. PPP3CA is strongly constrained, which fits de novo dominant disease. The exact gnomAD values for F470L/A473T were not checked.
- **Origin.** Germline de novo. No somatic or mosaic cases reported.
- **Functional consequence.** `functional_impact_category: GAIN_OF_FUNCTION`; HYPERMORPHIC may be more precise once the full text is read. The mechanism is relief of autoinhibition, giving calcineurin activity that is constitutive or Ca²⁺/CaM-independent.

**Allelic contrast (important for curation):**
- **Catalytic-domain missense** (e.g. H92R, N150I, D234E, H281Q, E282K) and some frameshifts cause **DEE91**, which is loss of function (PMID:29432562). E282K has since been shown to shift substrate dephosphorylation by altering active-site recruitment (Shirakawa et al. 2026, Nat Commun, PMID:41698888).
- **Truncating variants in the regulatory domain** (e.g. p.Gln442Ter, Δ442–521, Δ445–521) remove the CaM-binding and AI regions. In vitro the recombinant truncated enzyme is **constitutively active**: *"results in constitutive activation of the enzyme"* (Rydzanicz et al. 2019, PMID:30254215). Yet in patient cells *"despite normal mRNA abundance the protein expression level is strongly reduced"* (same paper). These patients have refractory epilepsy, not ACCIID.
- Panneerselvam et al. 2021 (PMID:33963760) found that truncating variants *"are all located within a 26-amino acid region in the regulatory domain (RD)"*. There was *"apparent RNA expression from the mutant allele, but no detectable mutant protein"*, and these patients had *"more severe earlier onset seizures."*
- **Implication.** Activation alone does not produce ACCIID. A stable, full-length AI-domain missense protein appears to be needed. That is an inference from the contrast across these papers, not a demonstrated mechanism.

**Modifiers, epigenetics, chromosomal abnormalities.** None reported for ACCIID. 4q24 deletions that include PPP3CA would be expected to cause loss of function, not ACCIID.

**Isoforms.** Castiglioni et al. 2024 (PMID:39707491) reports that the PPP3CA isoform balance matters, with *"splicing isoform 1 prevailing over isoform 2 in the central nervous system."* Their cases were truncating or splice variants, not ACCIID.

## 5. Environmental information

Not applicable. There are no environmental, lifestyle or infectious factors. If the entry has an `environmental:` section, it should be empty or omitted.

## 6. Mechanism and pathophysiology

**Ordered causal chain:**

1. **De novo heterozygous missense variant in the PPP3CA AI domain** (F470L or A473T). *Demonstrated (sequencing).*
2. → **Disrupts the AI domain's occupancy of the catalytic cleft**, which leads to **loss of autoinhibition**. *Inferred* from domain location and structural modelling (the paper's MeSH terms include "Models, Molecular", "Protein Conformation").
3. → **Results in increased (constitutive or Ca²⁺-independent) calcineurin phosphatase activity**. *Demonstrated in yeast:* the AI mutants gave "increased calcineurin signaling" (PMID:29432562; IN_VITRO / model-organism yeast assay, Crz1-dependent reporter likely; check the full text).
4. → **Leads to excessive dephosphorylation and nuclear translocation of NFAT transcription factors**, which then alter NFAT-dependent transcription. *Inferred*: the canonical calcineurin effector, not measured in patient cells.
5. → **Branches into tissue-level developmental consequences** (all *inferred*; no patient-tissue or animal-model data):
   - **5a. Skeletal and craniofacial.** Dysregulated calcineurin–NFATc1 signalling in osteoblasts and osteoclasts and in cranial-suture mesenchyme results in craniosynostosis with *paradoxically* decreased calvarial ossification, gracile (slender) long bones and ribs, perinatal fractures, short stature and brachydactyly. Calcineurin/NFAT is a known regulator of osteoblast and osteoclast differentiation and bone mass (review: PMID:33338510, Gene 2021).
   - **5b. Palate.** Abnormal palatal shelf development or elevation leads to cleft palate. This may be secondary to micrognathia and retrognathia (a Pierre Robin–type sequence). *Inferred*: the abstract does not discuss it.
   - **5c. Neuromuscular / fetal movement.** Calcineurin regulates skeletal-muscle fibre type (NFAT/MEF2) and neuronal activity. Fetal hypokinesia leads to arthrogryposis multiplex congenita, and possibly to hydrops fetalis through the fetal akinesia deformation sequence. *Inferred.*
   - **5d. CNS.** Calcineurin controls synaptic plasticity, dendritic morphology and neuronal excitability (dephosphorylation of dynamin-1, amphiphysin, NMDA/AMPA receptor regulation). Altered neurodevelopment leads to intellectual disability, global developmental delay and occasional generalised seizures. *Inferred.*
   - **5e. Kidney / urinary tract.** Calcineurin–NFAT signalling contributes to ureteric/renal development, and its disruption leads to hydronephrosis and vesicoureteral reflux. *Inferred and weak (1/2 patients).*

**Suggested ontology terms** (verify every CURIE with OAK or the term caches before writing it):
- **GO BP:** calcineurin-mediated signaling (GO:0097720); calcineurin-NFAT signaling cascade (GO:0033173); protein dephosphorylation (GO:0006470); ossification (GO:0001503); osteoblast differentiation (GO:0001649); roof of mouth development (GO:0060021); skeletal system development (GO:0001501); regulation of synaptic plasticity (GO:0048167).
- **GO MF:** calcium-dependent protein serine/threonine phosphatase activity (GO:0004723); calmodulin binding (GO:0005516).
- **GO CC:** calcineurin complex (GO:0005955); cytosol; nucleus (NFAT target).
- **CL:** osteoblast (CL:0000062); osteoclast (CL:0000092); chondrocyte (CL:0000138); neural crest cell (CL:0000333, cranial mesenchyme source); neuron (CL:0000540); skeletal muscle fiber (CL:0008002).
- **Modifier.** Use `GAIN_OF_FUNCTION` on the calcineurin activity node, because the claim is loss of regulatory control, not merely more activity. Use `INCREASED` on downstream NFAT signalling.
- **`biological_scale`:**
  - Step 3: MOLECULAR
  - Step 4: CELLULAR
  - Steps 5a–e: TISSUE

**Molecular profiling, omics, single-cell, CRISPR screens.** None available for ACCIID.

## 7. Anatomical structures affected

- **Skeletal system:**
  - skull and cranial sutures: UBERON:0003685 *cranial suture*; calvaria UBERON:0004339
  - mandible: UBERON:0001684
  - secondary palate: UBERON:0001716
  - ribs: UBERON:0002228
  - long bones: UBERON:0002495
  - hand digits
- **Joints and muscle (contractures):** multiple joints, bilateral.
- **CNS:** brain, UBERON:0000955.
- **Urinary tract:** kidney (UBERON:0002113) and ureter (UBERON:0000056).
- **Fetal compartment:** hydrops.
- **Subcellular:** cytosolic calcineurin complex; NFAT shuttling to the nucleus.
- **Lateralization:** craniofacial and contracture findings are generally bilateral or midline. Plagiocephaly is asymmetric.

## 8. Temporal development

- **Onset:** prenatal or congenital. One case had third-trimester onset with nonimmune hydrops, and perinatal fractures were present.
- **Course:** static structural anomalies with lifelong neurodevelopmental disability. No staging. No natural-history data.
- **Critical period:** embryonic and fetal skeletal, craniofacial and neuromuscular development (inferred).

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006). Both cases were **de novo**, so there are no penetrance data and no multigeneration families. Consanguinity has no role.
- **Recurrence risk:** low, but nonzero because of possible parental germline mosaicism. This is general genetic-counselling practice; no PPP3CA-specific data exist.
- **Prevalence:** unknown. Use `measure_type: CASES_IN_LITERATURE` with 2 cases (PMID:29432562), plus later presumed cases if any are verified. A qualitative `ULTRA_RARE` class with that measure type is permissible.
- **Sex ratio, founder effects, geographic or ancestry distribution:** not determinable. The original cohort was Japanese-led and included an Israeli collaborator (Ekhilevitch), but patient ancestry is not confirmed from the abstract.

## 10. Diagnostics

- **Genetic testing:** exome or genome sequencing, typically trio-based, is the practical route. Both cases were found by WES and confirmed by Sanger sequencing. PPP3CA appears on arthrogryposis and fetal-anomaly panels (PanelApp Australia / Genomics England). Single-gene testing is impractical without a recognisable gestalt.
- **Variant interpretation:** domain location decides which disorder a variant causes:
  - AI-domain missense (465–487): ACCIID
  - catalytic missense: DEE91
  - regulatory-domain truncation: early-onset refractory epilepsy

  Functional assays support classification. Options are the yeast calcineurin reporter (PMID:29432562) and recombinant phosphatase activity (PMID:30254215).
- **Imaging:**
  - skull radiograph or CT for suture fusion and calvarial ossification
  - skeletal survey for slender ribs and long bones, and fractures
  - renal ultrasound for hydronephrosis and VUR (voiding cystourethrogram)
  - prenatal ultrasound for hydrops, contractures and micrognathia
- **EEG:** if seizures occur.
- **Biomarkers or lab tests:** none specific.
- **Differential diagnosis:**
  - other arthrogryposis syndromes (fetal akinesia deformation sequence; distal arthrogryposis due to *PIEZO2* or *MYH3*)
  - syndromic craniosynostoses (FGFR-related, *TWIST1*, *TCF12*)
  - craniosynostosis with bone fragility: Cole–Carpenter syndrome (*P4HB*, *SEC24D*); osteogenesis imperfecta with craniosynostosis
  - *B3GAT3*-related disorder with craniosynostosis and bone fragility
  - DEE91 (same gene, opposite mechanism, no congenital anomalies)
- **Screening:** no newborn or carrier screening. Prenatal ultrasound may detect anomalies, and prenatal exome is possible.

## 11. Outcome and prognosis

No survival, mortality or QoL data exist. One case presented with hydrops and perinatal fractures, which suggests a potentially severe perinatal course. Expected morbidity comes from ID, contractures, cleft palate, craniosynostosis (risk of raised intracranial pressure) and bone fragility. Prognostic factors are unknown.

## 12. Treatment

No disease-specific therapy exists, and no clinical trials exist (none found). Management is supportive and multidisciplinary. Suggested NCIT terms below must be verified as descendants of `NCIT:C25218`.

| Intervention | NCIT suggestion | `therapeutic_modality` |
|---|---|---|
| Cranial vault surgery for craniosynostosis | Surgical Procedure, NCIT:C15329 (or a more specific craniofacial term if one exists) | SURGERY |
| Cleft palate repair | Surgical Procedure, NCIT:C15329 | SURGERY |
| Physical / occupational therapy for contractures | Physical Therapy NCIT:C15302; Occupational Therapy NCIT:C121351 | BEHAVIORAL |
| Orthopaedic management (casting, contracture release) | Orthopedic Surgical Procedure, NCIT:C16186 | SURGERY |
| Speech-language therapy | NCIT:C159273 | BEHAVIORAL |
| Antiseizure medication when seizures occur | Pharmacotherapy, NCIT:C15986 | SMALL_MOLECULE (agent unspecified) |
| Genetic counselling | NCIT:C15240 | — |

**Mechanism-based hypothesis (not a treatment).** Calcineurin inhibitors such as tacrolimus or ciclosporin could in principle counteract gain of function. There are **no reports** of their use in ACCIID. Their immunosuppressive, nephrotoxic and neurotoxic profile, and the fact that the malformations are prenatal, make postnatal benefit speculative. If included, record this as a `KNOWLEDGE_GAP` discussion, not as a treatment.

**Pharmacogenomics:** none.

## 13. Prevention

- **Primary prevention:** not possible (de novo).
- **Genetic counselling:** low empirical recurrence risk, with possible parental gonadal mosaicism. Prenatal diagnosis or PGT is possible in a subsequent pregnancy once the familial variant is known.
- **Tertiary prevention:** fracture precautions in the perinatal period; monitoring for raised intracranial pressure; renal surveillance; feeding support for cleft palate.

## 14. Other species and natural disease

- No naturally occurring animal disease was found. OMIA was not queried, so this is unconfirmed.
- Orthologs:
  - mouse *Ppp3ca* (MGI)
  - zebrafish *ppp3ca* (ZFIN ZDB-GENE-091113-24)
  - *Drosophila* CanA genes
  - yeast *CNA1/CNA2* (*S. cerevisiae*), which were used for functional testing
- The calcineurin–NFAT axis is conserved in vertebrates. Calcineurin–Crz1 signalling is the yeast counterpart used as the assay readout.
- No zoonotic or transmission relevance.

## 15. Model organisms

| Model | Relevance | Status |
|---|---|---|
| *S. cerevisiae* calcineurin complementation / reporter assay with human PPP3CA variants | Showed the AI variants increase signalling (PMID:29432562) | IN_VITRO-type functional model. Records the molecular gain of function only, with no tissue phenotype. Upward-extrapolation caveat: MOLECULAR model → TISSUE phenotypes. |
| *E. coli*-expressed recombinant calcineurin | Enzyme activity of a regulatory-domain truncation (PMID:30254215) | Not an ACCIID variant |
| Patient-derived EBV lymphoblasts and reprogrammed neurons | Protein downregulation in a truncation case (PMID:30254215) | Not ACCIID |
| *Ppp3ca* knockout mouse | Loss of function. Reported neuronal and memory and T-cell phenotypes; models DEE91 more than ACCIID | Cited from memory; verify the primary reference |
| Constitutively active calcineurin or NFATc1 transgenic mice (e.g. osteoblast-targeted) | Would test the ACCIID bone/suture hypothesis | Not confirmed in this session; literature exists on calcineurin/NFAT and bone mass. Verify before citing. |
| AI-domain knock-in (F470L / A473T) mouse or zebrafish | **None reported.** This is the key human-model gap. | Candidate `KNOWLEDGE_GAP` / `HUMAN_MODEL_MISMATCH` discussion |

---

## Curation notes for the dismech entry

- **The only verified quotable source is PMID:29432562**, and it is already cached. Its abstract supports:
  - the AI-domain association and the congenital anomalies ("craniofacial dysmorphism, arthrogryposis and short stature")
  - the severe skeletal findings ("severe craniosynostosis and gracile bones (severe bone slenderness and perinatal fractures)")
  - the yeast gain-of-function result

  Cleft palate, ID, hydrops and the renal findings come from the HPO annotations and are **not in the abstract**. They need the full text, or an `ORPHA:565858` cache row (`just fetch-reference ORPHA:565858`), for exact-quote evidence.
- **Before citing**, fetch PMID:30254215, PMID:33963760, PMID:39707491 and PMID:41698888 with `just fetch-reference`. The quotes above came through a summarising fetch tool and must be re-checked against the cache.
- **Treat the DEE91 contrast as context.** It belongs in `notes` or discussion. The DEE91 entry (`CN-Related_Developmental_and_Epileptic_Encephalopathy` exists on the dismech site) should cross-reference this one.
- **The cache file is modified.** `references_cache/PMID_29432562.md` currently has an uncommitted change in the worktree (35+/68−). Check whether it was regenerated by the fetcher or edited by hand before committing.

## Sources

- Mizuguchi T et al. *Hum Mol Genet* 2018;27:1421–1433. PMID:29432562. doi:10.1093/hmg/ddy052
- Rydzanicz M et al. *Eur J Hum Genet* 2019;27:61–69. PMID:30254215, PMC6303256
- Panneerselvam S et al. *Clin Genet* 2021;100:227–233. PMID:33963760, PMC11698261
- Castiglioni S et al. *Orphanet J Rare Dis* 2024. PMID:39707491, PMC11662586
- Wang T et al. *Front Neurosci* 2025. PMID:40548073
- Shirakawa KT et al. *Nat Commun* 2026. PMID:41698888
- UniProt Q08209: https://rest.uniprot.org/uniprot/Q08209.txt
- HPO annotations for OMIM:618265: https://ontology.jax.org/api/network/annotation/OMIM:618265
- MONDO via OLS: https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0032642
- [KEGG H02641](https://www.kegg.jp/entry/H02641)
- [PanelApp Australia – PPP3CA](https://panelapp-aus.org/panels/47/gene/PPP3CA/)
- [VCGS PanelApp fetal anomalies – PPP3CA](https://panelapp-test.vcgs.org.au/panels/3763/gene/PPP3CA/)
- [ExPASy VAR_081902](https://web.expasy.org/variant_pages/VAR_081902.html)
- ClinVar esummary for PPP3CA records with the ACCIID trait: https://eutils.ncbi.nlm.nih.gov/
- Europe PMC search: https://www.ebi.ac.uk/europepmc/

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 11 |
| On topic | 8 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:33338510` (1 mention) - Serine/threonine phosphatases in osteoclastogenesis and bone resorption.
  - shared terms: bone

Weighed against this report's own most characteristic terms: `acciid`, `ppp3ca`, `variant`, `calcineurin`, `palate`, `bone`, `craniosynostosis`, `cleft`, `exist`, `arthrogryposis`, `patient`, `dee91`, `fracture`, `hydrop`, `novo`, `perinatal`, `yeast`, `domain`, `craniofacial`, `seizure`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 60 |
| Resolved | 56 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 28 |
| Terms named correctly | 22 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 6 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0097720` (1 mention) - the report calls it "GO BP:** calcineurin-mediated signaling"; GO calls it **calcineurin-mediated signaling**
- `GO:0004723` (1 mention) - the report calls it "GO MF:** calcium-dependent protein serine/threonine phosphatase activity"; GO calls it **calcium-dependent protein serine/threonine phosphatase activity**
- `GO:0005955` (1 mention) - the report calls it "GO CC:** calcineurin complex"; GO calls it **calcineurin complex**
- `CL:0000062` (1 mention) - the report calls it "CL:** osteoblast"; CL calls it **osteoblast**
- `UBERON:0002113` (1 mention) - the report calls it "Urinary tract:** kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names
- `NCIT:C15240` (1 mention) - the report calls it "Genetic counselling"; NCIT calls it **Genetic Counseling**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `MIM`, `ORPHA`.

56 of 60 terms resolved to a current term; the rest could not be looked up either way.