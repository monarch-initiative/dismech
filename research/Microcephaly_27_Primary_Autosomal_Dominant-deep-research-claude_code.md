---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-15T15:31:43.823126'
end_time: '2026-10-15T15:34:12.339742'
duration_seconds: 148.52
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Microcephaly 27, Primary, Autosomal Dominant
  mondo_id: MONDO:0030929
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
  web_search_requests: 9
  num_turns: 17
  total_cost_usd: 1.8440557
  session_id: 2b698290-e2af-4486-aaeb-a635c554f41b
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - mcp__pubmed__search_articles
  assistant_text_blocks: 2
citation_count: 15
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMID:16543416
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 30
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 1
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0030929
    reported_labels:
    - MONDO
    ontology_label: microcephaly 27, primary, autosomal dominant
  - term_id: DOID:0051038
    reported_labels:
    - Disease Ontology
    ontology_label: autosomal dominant primary microcephaly 27
  - term_id: HP:0003745
    reported_labels:
    - verify
    ontology_label: Sporadic
  - term_id: NCIT:C15986
    reported_labels:
    - + `therapeutic_agent` only if a source names drugs
    ontology_label: Pharmacotherapy
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Microcephaly 27, Primary, Autosomal Dominant
- **MONDO ID:** MONDO:0030929 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Microcephaly 27, Primary, Autosomal Dominant** covering all of the
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

I'm checking a few more mouse-model and mechanism citations before writing the MCPH27 report.

# Research report: Microcephaly 27, Primary, Autosomal Dominant (MCPH27, *LMNB2*)

**Scope and access.** PubMed MCP search was not permitted in this session. The report rests on two sources:

- **Full text read:** Parry et al. 2021 (PMID:33033404) and the abstract of Desgrouas et al. 2025 (PMID:40011009). Both are already in this worktree's `references_cache/`.
- **Web search only:** OMIM/LOVD, PanelApp, ClinVar Miner and the mouse-model papers. I confirmed their titles and PMIDs, but I did not read their abstracts here.

Quotes marked **[cached]** are exact text from the cache files. Everything else is paraphrased. Fetch those references with `just fetch-reference` before taking a snippet from them.

**The literature is very small.** One primary case series reports six *LMNB2* individuals. I found no follow-up case reports for 2022–2024 by web search. Several template sections therefore come back "no data".

---

## 1. Disease information

**Overview.** MCPH27 is a dominant, mostly de novo form of severe primary microcephaly. It is caused by heterozygous missense variants in *LMNB2*, which encodes lamin B2, a component of the nuclear lamina. Parry et al. described it as a new kind of laminopathy, together with the *LMNB1* form (MCPH26).

> "We identify dominant pathogenic variants in LMNB1 and LMNB2 as a genetic cause of primary microcephaly, implicating a major structural component of the nuclear envelope in its etiology and defining a new form of laminopathy." — PMID:33033404 **[cached]**

| Identifier | Value | Source |
|---|---|---|
| MONDO | MONDO:0030929 | template; ClinVar Miner condition 30929 |
| OMIM (phenotype) | 619180 | [LOVD #07163](https://databases.lovd.nl/shared/diseases/07163), [PanelApp AUS](https://panelapp-aus.org/panels/250/gene/LMNB2/) |
| OMIM (gene) | *150341 LMNB2 (not verified this session) | — |
| Disease Ontology | DOID:0051038 | [DO](https://disease-ontology.org/term/DOID:0051038/owl) |
| Orphanet / ICD | No specific code found. Probably falls under a general primary microcephaly code. | — |

- **Synonyms:** MCPH27; LMNB2-related primary microcephaly; lamin B2-associated microcephaly. The broader term "lamin B-associated laminopathy" also covers MCPH26 (*LMNB1*).
- **Data type:** The phenotype comes from a research cohort analysis of individual patients (DDD exomes and 100,000 Genomes Project genomes, with HPO terms extracted per patient). It is not drawn from a disease-level aggregate.

## 2. Etiology

- **Cause:** Monoallelic *LMNB2* missense variants in the coiled-coil α-helical rod domain. Most arise de novo.
- **Genetic risk factors:** Only the causal variants (Section 4). No susceptibility loci or modifier genes have been described.
- **Environmental risk, protective factors, gene–environment interactions:** None reported. This is a monogenic developmental disorder.
- **Parental mosaicism is a real recurrence risk.** In one family the variant came from a mosaic mother who was clinically unaffected:

> "in P7, it had been inherited from the proband's mosaic, clinically unaffected, mother" — PMID:33033404 **[cached]**

## 3. Phenotypes

The data come from 13 *LMNB1*/*LMNB2* patients analysed together. The paper gives pooled figures, so per-gene frequencies for the six *LMNB2* individuals are only in its supplementary tables (S1–S3, S5), which I did not access.

| Phenotype | Type | Onset / course | Frequency (pooled) | Candidate HPO (verify every ID) |
|---|---|---|---|---|
| Severe microcephaly, OFC −5.85 ± 1.14 SD | sign | congenital, nonprogressive | 13/13 | Primary microcephaly HP:0011451 (now labelled "Congenital microcephaly"?); Severe microcephaly |
| Microcephaly present at birth | sign | neonatal | 12/13 ("all but one") | as above |
| Global developmental delay, mild to severe | neurodevelopmental | infancy | all; severe in 4/8 DDD cases | Global developmental delay HP:0001263 |
| Speech not attained | neurodevelopmental | childhood | 3 older children | Absent speech HP:0001344 |
| Intellectual disability | neurodevelopmental | childhood | implied (OMIM: "impaired intellectual development") | Intellectual disability HP:0001249 |
| Seizures | neurological | variable | 4/13 | Seizure HP:0001250 |
| Simplified gyral pattern | imaging | congenital, nonprogressive | 2/13 | Simplified gyral pattern HP:0009879 |
| Reduced white-matter volume, ventriculomegaly, wide extra-axial spaces | imaging | congenital | 2/13 | Ventriculomegaly HP:0002119; Reduced cerebral white matter volume (look up) |
| Sloping forehead | dysmorphic | congenital | "some" | Sloping forehead HP:0000340 |
| Normal birth weight and stature | negative finding | — | most | (state as absent IUGR / short stature) |

Key quotes **[cached, PMID:33033404]**:

> "All LMNB1/2 cases had severe microcephaly (OFC −5.85 ± 1.14 SD, Fig. 2a, Table S5), evident from birth in all but one case."

> "Global developmental delay of varying severity was evident and seizures present in four cases"

> "Neuroimaging demonstrated a structurally normal brain, without evidence of abnormal neuronal migration"

> "In P8, where serial scans were available, this was nonprogressive."

> "global developmental delay varied substantially between cases, classified as severe in four of eight DDD cases, with speech not attained in three older children."

**Notable negatives.** There was no IUGR, no major malformations, no consistent facial gestalt and no migration defect on imaging.

**Quality of life.** No validated QoL data exist. The disability burden is set by the severity of developmental delay and intellectual disability and by the seizures.

## 4. Genetic / molecular information

- **Gene:** *LMNB2* (lamin B2), on 19p13.3. HGNC id is probably hgnc:6638; **look it up before binding**.

**Pathogenic variants** (NM_032737.4) **[cached]**:

| Variant | Domain | Recurrence | De novo | gnomAD v2.1 |
|---|---|---|---|---|
| c.1192G>A p.(Glu398Lys) | coil 2B, intradimer interface | 5 individuals (P4, P5, P6, P7, P12) | P4, P5, P12; P7 inherited from mosaic mother | absent |
| c.160A>C p.(Asn54His) | coil 1A, intradimer interface | 1 | yes | absent |

> "We identified four microcephalic individuals from the DDD cohort (P4, P5, P6, P7) and one individual from the 100kGP study (P12) with the same variant in LMNB2 (NM_032737.4: c.1192G>A, p.Glu398Lys)" **[cached]**

- **Variant class:** Missense only. No truncating variants have been seen in dominant cases.
- **Functional consequence:** Proposed to be dominant-negative or gain of function, not haploinsufficiency:

> "The pathogenic variants reported here are most likely dominant negative rather than haploinsufficient given that microcephaly is not present in the Lmnb1+/− mouse. The recurrent nature of the pathogenic variants at specific residues and absence of truncating variants favors gain of function or dominant negative mechanisms." **[cached]**

  The "Lmnb1+/−" argument is drawn from the paralog. No *Lmnb2*+/− brain-size data were cited.
- **Origin:** Germline; de novo or inherited from a mosaic parent.
- **Classification:**
  - ClinVar Miner for MONDO condition 30929: 3 Pathogenic, 3 VUS and 1 Likely benign submissions ([ClinVar Miner](https://clinvarminer.genetics.utah.edu/variants-by-mondo-condition/30929)).
  - PanelApp Green (high evidence) for severe microcephaly in both Genomics England and Australia ([GE PanelApp](https://panelapp.genomicsengland.co.uk/panels/162/gene/LMNB2), [PanelApp AUS](https://panelapp-aus.org/panels/138/gene/LMNB2/)).
  - **I found no ClinGen gene-disease validity curation and no GenCC tier.** Leave `gene_disease_validity` absent unless a source tier is found.

**Allelic disorders of *LMNB2*** (keep these separate, see Section 9 on the lump/split question):

- **Autosomal recessive progressive myoclonus epilepsy with early ataxia.** Homozygous p.His157Tyr in a consanguineous Palestinian Arab family; the mutant protein was defective at forming assembly arrays. Damiano et al., *Hum Mol Genet* 2015, PMID:25954030 ([source](https://ncbi.nlm.nih.gov/pubmed/25954030)).
- **Susceptibility to acquired partial lipodystrophy (OMIM 608709).** Hegele et al., *AJHG* 2006, PMID:16826530. The reported variants are common in gnomAD, and PanelApp AUS rates the gene Amber with GenCC at "Limited" ([PanelApp AUS lipodystrophy](https://panelapp-aus.org/panels/130/gene/LMNB2/)).
- **Biallelic loss of function with lethal brain malformation.** A homozygous LoF variant in two related newborns (PMID:40011009, **[cached]**):

  > "Both newborns died in the perinatal period and exhibited a similar phenotype at birth, including severe brain development abnormalities, which closely mirror findings observed in several Lmnb2-deficient mouse models."

  > "Western blot and immunofluorescence cell labelling performed on the patient's fibroblasts obtained at birth confirmed the complete absence of lamin B2 and revealed an increase in lamin B1, together with alterations in alpha-tubulin and vimentin organisation."

  Genomics England changed *LMNB2*'s inheritance to "BOTH monoallelic and biallelic" in March 2026, presumably because of this report.

**Other categories:**

- **Modifier genes:** None known.
- **Epigenetics:** None disease-specific. In general, B-type lamins tether lamina-associated domains, but lamin B binding is not strictly required for silencing in mouse ESCs (Kim et al. 2011, PMID:22116031).
- **Chromosomal abnormalities:** Not part of MCPH27. Contrast *LMNB1* duplication, which causes adult-onset leukodystrophy.

## 5. Environmental information

None reported for environmental, lifestyle or infectious factors. Not applicable.

## 6. Mechanism / pathophysiology

### Ordered causal chain

1. A heterozygous germline missense variant (most often de novo p.Glu398Lys) changes a conserved residue at a dimer interface in the lamin B2 coiled-coil rod. *(Human genetic evidence: demonstrated.)*
2. **This leads to** abnormal dimer and filament assembly. *(Inferred from modelling, so computational.)*
   - Glu398 normally repels its partner chain's Glu398. Lys398 forms an ionic bond with wild-type Glu398 and over-stabilises mixed mutant/wild-type dimers (FoldX ΔΔG −2.0 kcal/mol).
   - Asn54 sits at the coil 1A intradimer interface.

   > "the heterozygous LMNB2 p.Glu398Lys substitution would result in a subset of mismatched dimers in which, instead, interaction of the two chains would be aberrantly stabilized" **[cached]**
3. **This results in** a dominant-negative "poisoning" of the higher-order lamina. *(Inferred from recurrence, the absence of truncating variants, and the LMNA analogy.)*
4. **This results in** nuclear lamin aggregates and abnormal nuclear shape. *(In vitro, with GFP fusions overexpressed in cultured cells.)*

   > "Cells expressing the LMNB1/B2 variants frequently contained nuclear aggregates and/or significantly altered nuclear morphology in comparison to cells expressing wild-type GFP-LMNB1/2" **[cached]**

5. **The pathway then branches (hypothesised, not shown in human tissue):**
   - **5a. Mitotic defect.** B-type lamins associate with the mitotic spindle. Their loss in mouse neural progenitors disturbs spindle orientation. This is proposed to shift progenitors from symmetric proliferative to asymmetric or neurogenic divisions, depleting the progenitor pool and reducing neuron output. *(Mouse: Kim et al. 2011, PMID:22116031, authors' "probably"; spindle-matrix work: Tsai et al. 2006, Science, PMID:16543416, not verified this session.)*
   - **5b. Nuclear fragility.** A mechanically fragile nucleus is more easily damaged during interkinetic nuclear migration and neuronal migration, which is proposed to increase progenitor and neuron death. *(Analogy to the LMNA equivalent of LMNB1 p.Lys33del; speculative.)*

   > "B-type lamins associate with the mitotic spindle21 with defects in spindle orientation in neuronal precursor cells reported in Lmnb1 and Lmnb2 knockout mice,17 suggesting this could be the mechanism underlying microcephaly." **[cached]**

   > "Such fragility in neuronal precursors would enhance susceptibility to mechanical stresses of interkinetic nuclear migration and neuronal migration and lead to increased cell death during brain development." **[cached]**
6. **Both branches lead to** fewer cortical neurons and a reduced cerebral cortex volume during fetal neurogenesis. *(Inferred.)*
7. **This results in** congenital microcephaly with a structurally normal or simplified-gyral brain and reduced white matter, followed by developmental delay, intellectual disability and, in some patients, seizures. *(Human clinical: demonstrated.)*

**Discordance to record.** Biallelic-null mice (and the 2025 biallelic-LoF human newborns) have migration defects and lissencephaly-like lamination. Heterozygous MCPH27 patients show no migration defect. This suggests the dominant missense mechanism is different from null loss. It is a good candidate for a `HUMAN_MODEL_MISMATCH` discussion.

### Suggested ontology terms (all IDs to be looked up; none are verified)

| Category | Suggested terms |
|---|---|
| GO biological process | nuclear envelope organization (GO:0006998); intermediate filament cytoskeleton organization; mitotic spindle orientation (GO:0000132); cerebral cortex development (GO:0021987); neuron migration (GO:0001764); neural precursor cell proliferation (GO:0061351) |
| GO cellular component | nuclear lamina (GO:0005652); nuclear envelope; spindle |
| GO molecular function | structural molecule activity / structural constituent of nuclear lamina? (check) |
| CL | neural progenitor cell (CL:0011020); radial glial cell (CL:0000681); neuron (CL:0000540) |

**Biological scale per node:** variant, dimer and filament steps are MOLECULAR; aggregates, nuclear shape and spindle orientation are CELLULAR; cortical neuron number is TISSUE; microcephaly is ORGANISM.

**Omics, single-cell and spatial data:** None disease-specific. No GEO datasets were found (`just discover-datasets` was not run).

## 7. Anatomical structures

- **Primary:** Brain, especially the cerebral cortex (UBERON:0000955 brain, UBERON:0000956 cerebral cortex) and cerebral white matter.
- **Secondary:** Lateral ventricles (ventriculomegaly) and skull or head size as a consequence.
- **Body systems:** Nervous system only.
- **Cells:** Neural progenitors / radial glia and cortical neurons (inferred).
- **Subcellular:** Nuclear lamina and nuclear envelope; possibly the spindle.
- **Lateralization:** Bilateral and symmetric.

## 8. Temporal development

- **Onset:** Prenatal or congenital (OFC reduced at birth in 12/13).
- **Course:** Static or nonprogressive. Serial MRI in one patient showed no progression.
- **Critical period:** Fetal cortical neurogenesis, roughly mid-gestation (inferred).
- **Stages and remission:** None defined; not applicable.
- **Duration:** Lifelong.

## 9. Inheritance and population

**Inheritance.** Autosomal dominant, usually de novo (HPO: Autosomal dominant inheritance HP:0000006; Sporadic HP:0003745 – verify).

**Somatic mosaicism.** One affected child inherited the variant from an unaffected mosaic mother. That is **parental mosaicism**, which the CLAUDE.md somatic-mosaicism guidance says **must not** be bound to HP:0001442. Record it as a recurrence-risk note instead.

- **Penetrance:** Appears complete in heterozygotes who are not mosaic (n=6, so very limited data).
- **Expressivity:** Variable, especially in developmental-delay severity.
- **Anticipation, founder effects, consanguinity:** None. No population or sex bias is known; the pooled cohort contained both sexes.

**Epidemiology.** Ultra-rare; about 6 *LMNB2* cases published.

- `measure_type: CASES_IN_LITERATURE`
- `prevalence_class: ULTRA_RARE` or NOT_YET_DOCUMENTED
- No incidence or carrier frequency data.

**Lump/split question for curation.** The dominant missense microcephaly (MCPH27) and the recessive LoF perinatal-lethal brain malformation (PMID:40011009) have different inheritance, mechanism (dominant-negative vs null) and severity. Treat the 2025 recessive phenotype as a separate disease or allelic note, not as a subtype of MCPH27. The progressive myoclonus epilepsy (PME) and lipodystrophy associations are also separate.

## 10. Diagnostics

- **Clinical criteria:** OFC ≤ −3 SD (here typically −5 to −6 SD) at birth, without major malformations or IUGR.
- **Imaging:** Brain MRI shows a small, structurally normal brain, sometimes with a simplified gyral pattern, reduced white matter and ventriculomegaly. No cortical migration defect, which helps distinguish it from the biallelic LoF phenotype and from lissencephaly.
- **Genetic testing:** Exome or genome sequencing, ideally as a trio (de novo calling), is the approach that found these cases.
  - Microcephaly gene panels: *LMNB2* is Green on Genomics England panel 162 (severe microcephaly) and PanelApp AUS panels 138 and 250.
  - Consider testing for low-level parental mosaicism.
  - CMA, karyotype, FISH, mtDNA testing and repeat-expansion testing are not relevant except to rule out other causes.
- **Biomarkers and laboratory tests:** None. Research fibroblast immunofluorescence can show lamin aggregates or abnormal nuclear shape, but this is not a clinical test.
- **Differential diagnosis:**
  - Other MCPH genes (*ASPM*, *WDR62*, *CDK5RAP2*, *MCPH1*, etc.; mostly autosomal recessive), and *LMNB1* MCPH26 (clinically indistinguishable).
  - Congenital infections (TORCH, Zika).
  - Fetal alcohol exposure.
  - Chromosomal syndromes.
  - Nuclear pore microcephalies (Galloway–Mowat syndrome, with nephrotic syndrome).
- **Screening:** No newborn or carrier screening.

## 11. Outcome / prognosis

- **Survival:** No data on survival or mortality. Nothing suggests reduced lifespan in heterozygotes, but this is unstudied.
- **Morbidity:** Lifelong neurodevelopmental disability ranging from mild to severe. Some patients have no speech, and some have epilepsy.
- **Prognostic factors:** Unknown, including any genotype–phenotype correlation between Glu398Lys and Asn54His.

## 12. Treatment

There is no disease-specific therapy, and there are no clinical trials (none found). Management is supportive. Candidate NCIT terms below must be verified against the `TreatmentTerm` enum.

| Intervention | Candidate NCIT term | `therapeutic_modality` |
|---|---|---|
| Antiseizure medication for seizures | Pharmacotherapy NCIT:C15986 (+ `therapeutic_agent` only if a source names drugs) | SMALL_MOLECULE |
| Early intervention: physical, occupational and speech therapy | Physical Therapy NCIT:C15302; Speech Language Therapy NCIT:C159273; Occupational therapy NCIT:C121351 | BEHAVIORAL |
| Genetic counseling (recurrence risk, parental mosaicism) | Genetic Counseling NCIT:C15240 | — |
| Developmental and educational support | Supportive Care NCIT:C15747 | — |

No primary source specific to MCPH27 supports these interventions. Cite general guidance or leave the evidence out rather than over-claim.

**Pharmacogenomics, gene therapy, RNA therapies:** None.

## 13. Prevention

- **Primary prevention:** Not applicable.
- **Genetic counseling:**
  - Recurrence risk is low for a confirmed de novo variant, but parental germline or somatic mosaicism must be considered (documented in one family).
  - An affected individual has a 50% transmission risk.
- **Reproductive options:** Prenatal or preimplantation testing for a known familial variant. Fetal ultrasound OFC monitoring in later pregnancies of mosaic carriers.

## 14. Other species / natural disease

- **Animal disease:** No naturally occurring animal disease found (OMIA not checked).
- **Orthologs:** Mouse *Lmnb2* and zebrafish *lmnb2* ([ZFIN](https://zfin.org/ZDB-GENE-990630-13)).
- **Conservation:** The mutated residues are conserved across all metazoan lamins, including *C. elegans* LMN-1 (PMID:33033404).
- **Zoonotic or transmission aspects:** None.

## 15. Model organisms

| Model | Phenotype | Recapitulation | Source |
|---|---|---|---|
| *Lmnb2*−/− mouse | Normal during development but dies soon after birth; disordered cortical layering, lissencephaly-like; neurons accumulate in the intermediate zone; hypoplastic cerebellum without sulci. Brain size not reduced at birth (per Parry). | Models biallelic LoF (the 2025 human phenotype) better than dominant MCPH27. Has a migration defect that MCPH27 lacks, so **PARTIALLY / FAILS_TO_RECAPITULATE** for MCPH27. | Coffinier et al., PNAS 2010, PMID:20145110 ([PMC2841930](https://pmc.ncbi.nlm.nih.gov/articles/PMC2841930)) |
| Forebrain-specific *Lmnb2* and *Lmnb1*/*Lmnb2* double knockout | Small forebrain with disorganized layering; elongated, comet-shaped nuclei in *Lmnb2*-deficient neurons; double knockout gives cortical atrophy. | Small forebrain fits microcephaly; mechanism is null, not dominant-negative. | Coffinier et al., MBoC 2011, PMID:21976703 ([PMC3226484](https://pmc.ncbi.nlm.nih.gov/articles/PMC3226484)) |
| *Lmnb1*/*Lmnb2* knockouts (mouse ESCs and embryos) | ESCs do not need lamins; organogenesis does. Spindle-orientation defects in neural progenitors, proposed as the cause of brain disorganization. | Supports the mitotic branch (5a) of the causal chain. | Kim et al., Science 2011, PMID:22116031 ([PMC3306219](https://pmc.ncbi.nlm.nih.gov/articles/PMC3306219)) |
| *C. elegans* LMN-1 with the ΔK46-equivalent change | Disrupted protofilament assembly; nuclear aggregates. | Shows the *LMNB1* p.Lys33del paralog mechanism, not *LMNB2* itself. | cited in PMID:33033404 |
| Cell overexpression, GFP-LMNB2 E398K/N54H | Nuclear aggregates; abnormal nuclear shape. | IN_VITRO; overexpressed above endogenous levels (a SUPRAPHYSIOLOGICAL caveat). | PMID:33033404 |

**Gaps.** There is no heterozygous knock-in (*Lmnb2* E398K) mouse, no patient-derived iPSC or cortical organoid model, and no measurement of spindle orientation with the actual dominant variants. These are the key experiments that would test chain steps 3–6.

---

## Curation notes for the dismech entry

1. **Evidence to quote:**
   - PMID:33033404 (full text cached) carries nearly every clinical and mechanistic claim. Quote the abstract or results sentences above, and grade modelling as COMPUTATIONAL, GFP experiments as IN_VITRO, and patients as HUMAN_CLINICAL.
   - The mouse-spindle sentence is the paper's discussion of other work: use `quote_role: BACKGROUND` with `MODEL_ORGANISM`.
2. **Mouse-paper quotes:** Fetch PMIDs 20145110, 21976703 and 22116031 before quoting them.
3. **Gene-disease validity:** No ClinGen tier was found, so do not record `gene_disease_validity`.
4. **Parental mosaicism:** Do not bind HP:0001442.
5. **2025 biallelic LoF report:** Keep PMID:40011009 out of the MCPH27 phenotype list, or cite it only as an allelic and mechanistic contrast (`HUMAN_MODEL_MISMATCH` discussion).
6. **CURIEs:** Every CURIE in this report must be checked with `runoak` or the cache before it is written.

**Sources:**
- [LOVD MCPH27 #07163](https://databases.lovd.nl/shared/diseases/07163)
- [PanelApp AUS – ID panel LMNB2](https://panelapp-aus.org/panels/250/gene/LMNB2/)
- [PanelApp AUS – microcephaly LMNB2](https://panelapp-aus.org/panels/138/gene/LMNB2/)
- [Genomics England PanelApp – LMNB2](https://panelapp.genomicsengland.co.uk/panels/162/gene/LMNB2)
- [PanelApp AUS – lipodystrophy LMNB2](https://panelapp-aus.org/panels/130/gene/LMNB2/)
- [Disease Ontology DOID:0051038](https://disease-ontology.org/term/DOID:0051038/owl)
- [ClinVar Miner, MONDO 30929](https://clinvarminer.genetics.utah.edu/variants-by-mondo-condition/30929)
- [Parry et al. 2021, PMC7862057](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7862057/)
- [Coffinier et al. 2010, PMC2841930](https://pmc.ncbi.nlm.nih.gov/articles/PMC2841930)
- [Coffinier et al. 2011, PMID 21976703](https://pubmed.ncbi.nlm.nih.gov/21976703)
- [Kim et al. 2011, PMC3306219](https://pmc.ncbi.nlm.nih.gov/articles/PMC3306219)
- [Damiano et al. 2015, PMID 25954030](https://ncbi.nlm.nih.gov/pubmed/25954030)
- [Hegele et al. 2006, PMID 16826530](https://www.qxmd.com/r/16826530)
- [ZFIN lmnb2](https://zfin.org/ZDB-GENE-990630-13)
- Desgrouas et al. 2025, J Med Genet, PMID:40011009 (cached)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 7 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:16543416` (1 mention) - Deconvolution of the factors contributing to the increase in global hurricane intensity.
  - shared terms: none

Weighed against this report's own most characteristic terms: `lmnb2`, `microcephaly`, `mcph27`, `variant`, `phenotype`, `found`, `cached`, `brain`, `nuclear`, `patient`, `genetic`, `novo`, `lamin`, `lmnb1`, `dominant`, `primary`, `cortical`, `mechanism`, `reduced`, `mosaicism`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 6 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030929` (1 mention) - the report calls it "MONDO"; MONDO calls it **microcephaly 27, primary, autosomal dominant**
- `DOID:0051038` (5 mentions) - the report calls it "Disease Ontology"; DOID calls it **autosomal dominant primary microcephaly 27**
- `HP:0003745` (1 mention) - the report calls it "verify"; HP calls it **Sporadic**
- `NCIT:C15986` (1 mention) - the report calls it "+ `therapeutic_agent` only if a source names drugs"; NCIT calls it **Pharmacotherapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011451` (1 mention) - the report calls it "now labelled "Congenital microcephaly"?"; HP calls it **Primary microcephaly**, and lists "Congenital microcephaly" among its other names