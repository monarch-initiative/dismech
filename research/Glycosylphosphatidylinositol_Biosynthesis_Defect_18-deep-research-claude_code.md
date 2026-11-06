---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-19T12:34:15.732404'
end_time: '2026-10-19T12:40:06.162224'
duration_seconds: 350.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Glycosylphosphatidylinositol Biosynthesis Defect 18
  mondo_id: MONDO:0029140
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
  web_search_requests: 7
  num_turns: 42
  total_cost_usd: 3.0947896
  session_id: 5824abc7-ea73-438f-ace5-8fdb25665abc
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 5
citation_count: 15
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 19
  quotes_valid: 17
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:30269814
  - PMID:11483512
  relevance_assessed: 10
  on_topic: 6
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 58
  verified: 56
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 4
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: DOID:0070382
    reported_labels:
    - DOID
    ontology_label: developmental and epileptic encephalopathy 95
  - term_id: HP:0000007
    reported_labels:
    - unverified; it does not appear in the cache lookups above
    ontology_label: Autosomal recessive inheritance
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glycosylphosphatidylinositol Biosynthesis Defect 18
- **MONDO ID:** MONDO:0029140 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Glycosylphosphatidylinositol Biosynthesis Defect 18** covering all of the
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

I'm pulling PubMed abstracts on PIGS deficiency (GPIBD18/DEE95) so the report can quote them exactly.

The Nguyen 2018 and cryo-EM transamidase abstracts are cached. Next I'm reading the three follow-up case papers and searching for any later cohorts.

Now caching the core biochemistry papers on PIGS and its complex, plus a few IGD reviews, so I can quote them too.

Identifiers are confirmed. Last, I'm checking for ClinGen/Orphanet records and the HPO terms before writing the report.

# GPI Biosynthesis Defect 18 (PIGS deficiency; DEE95): research report

**Status of the evidence.** The clinical literature is small: four primary case papers covering about 14 individuals (12 born, 2 fetuses) from about 11 families (PMIDs 30269814, 32612635, 33410539, 37035392). The functional evidence comes from GPI-transamidase biochemistry and structural studies. A PubMed search of `PIGS[tiab] AND (GPI OR glycosylphosphatidylinositol)` plus clinical terms found no further PIGS case series up to October 2026. Many results for that query were about the animal (swine), not the gene.

All quotes below are copied from abstracts or full texts now cached in `references_cache/` via `just fetch-reference`:
- PMID_30269814, PMID_33410539, PMID_32612635 and PMID_37035392 (the clinical papers);
- PMID_11483512, PMID_30914202, PMID_35165458, PMID_34576938 and PMID_12802054 (the biochemistry and structure papers);
- a ClinGen CGGV record that was already in the cache.

Ontology IDs were checked against the repository term caches (`cache/hp`, `cache/go`, `cache/cl`, `cache/chebi`, `cache/ncit`) or against HGNC, OLS and MONDO. The few I could not check are marked **(unverified)**.

---

## 1. Disease information

**Overview.** GPIBD18 is an autosomal recessive inherited GPI-anchor deficiency (IGD), a subgroup of the congenital disorders of glycosylation. It is caused by biallelic loss-of-function variants in *PIGS*, which encodes a subunit of the GPI transamidase (GPI-T). The clinical range runs from fetal akinesia, at the lethal end, to an early-infantile developmental and epileptic encephalopathy (DEE). Other features include hypotonia, microcephaly, coarse facies, visual and hearing impairment, and brain atrophy. The seizures sometimes respond to pyridoxine.

> "We present a study of six individuals from three unrelated families in which WES or WGS identified bi-allelic phosphatidylinositol glycan class S (PIGS) biosynthesis mutations. Phenotypes included severe global developmental delay, seizures (partly responding to pyridoxine), hypotonia, weakness, ataxia, and dysmorphic facial features." (PMID:30269814, Nguyen et al., *Am J Hum Genet* 2018)

| Identifier | Value |
|---|---|
| MONDO | MONDO:0029140, *glycosylphosphatidylinositol biosynthesis defect 18* |
| OMIM (phenotype) | 618143 |
| OMIM (gene) | 610271 (*PIGS*) |
| DOID | DOID:0070382 |
| GARD | 0025503 |
| MedGen / UMLS | 1648478 / C4748357 |
| Orphanet | No MONDO xref; probably filed under a broad IGD / CDG grouping. The orpha.net search page blocked automated access, so this is not confirmed. |
| ICD-10/11 | No specific code. It falls under the CDG/GPI-deficiency rubrics (ICD-10 E77.8 grouping level). |

**Synonyms:** GPIBD18; developmental and epileptic encephalopathy 95 (DEE95); PIGS deficiency; PIGS-related inherited GPI deficiency; PIGS-CDG. The older literature also uses "early infantile epileptic encephalopathy" (EIEE) (PMID:33410539).

**Source type.** All of the evidence comes from individual case reports and small case series, collected into disease-level resources (OMIM, ClinGen, GenCC). There are no EHR or registry data.

---

## 2. Etiology

- **Cause:** biallelic germline *PIGS* variants. These reduce GPI-T activity, and less GPI-anchored protein (GPI-AP) reaches the cell surface.
- **Genetic risk factors:**
  - Parental consanguinity or shared ancestry. In 4 of 5 Efthymiou families the parents were consanguineous and the variants homozygous (PMID:33410539).
  - One Mexican family came from "the same small rural community" (PMID:30269814).
  - East Asian recurrent allele c.1141_1164dup (p.Asp381_Val388dup). It has been found in three unrelated East Asian probands and is "seen in gnomAD in a heterozygous carrier state in five individuals of East Asian ethnicity" (PMID:33410539, 32612635, 37035392).
- **Environmental risk, protective factors, G×E:** none reported. Fever and infection make seizures worse ("aggravated by fevers or infections", PMID:32612635), but that is a trigger for seizures, not a cause of the disease.
- **Modifier genes:** none reported.

---

## 3. Phenotypes

The frequencies below are pooled from the published cases. The denominators are small and not every feature was assessed in every case.

| Phenotype | HPO (cache-verified) | Frequency / notes | Key source |
|---|---|---|---|
| Global developmental delay (severe), absent speech | HP:0001263 Global developmental delay; HP:0000750 Delayed speech and language development | All liveborn cases | 30269814, 33410539 |
| Seizures / DEE, early infantile onset (1–12 mo; under 3 mo in 8/11) | HP:0001250 Seizure; HP:0200134 Epileptic encephalopathy | 12/12 liveborn; refractory in 10/12 | 37035392 |
| Infantile spasms, hypsarrhythmia | HP:0012469 Infantile spasms; HP:0002521 Hypsarrhythmia | 1 case (Zhang); pseudohypsarrhythmia in the Efthymiou cohort | 32612635 |
| Focal, myoclonic and febrile seizures; burst suppression | HP:0007359; HP:0002123; HP:0002373; HP:0010851 | Focal was the commonest first seizure type (7/10) | 37035392, 33410539 |
| Hypotonia | HP:0001252 | Nearly all | all |
| Muscle weakness, ataxia | HP:0001324; HP:0001251 | Nguyen families 1–2 | 30269814 |
| Microcephaly | HP:0000252 | 6/6 in Efthymiou ("−3 SD"); the Li 2023 case was normocephalic | 33410539 |
| Coarse facies, arched eyebrows, thick helices, gingival hypertrophy | HP:0000280; HP:0000212 Gingival overgrowth | Most | 30269814, 32612635 |
| Brachytelephalangy | HP:0009882 Short distal phalanx of finger | Families 1–2 (Nguyen); 3/6 (Efthymiou) | 30269814, 33410539 |
| Visual impairment / cortical blindness; nystagmus | HP:0000505; HP:0000639 | About 50% | 33410539, 32612635 |
| Hearing impairment | HP:0000365 | 2/6 in Efthymiou; Zhang case | 33410539, 32612635 |
| Brain atrophy (frontotemporal), pontine hypoplasia, cerebellar vermian atrophy, thin corpus callosum, delayed myelination | HP:0002120; HP:0012110; HP:0002079; HP:0012448 | 6/6 had abnormal MRI; pontine hypoplasia 4/6 | 33410539 |
| Fetal akinesia / multiple joint contractures | HP:0001989 Fetal akinesia sequence | 2 fetuses (family 3) | 30269814 |
| Renal malformation / glomerular cysts | HP:0000077 (coarse; would need a `coarse_binding_basis`); HP:0000107 Renal cyst | 1/6 + 1 fetus | 33410539, 30269814 |
| Ventricular septal defect | HP:0001629 | 1 case | 37035392 |
| Autistic features, excessive laughing or crying | HP:0000717 Autism | 2 siblings | 33410539 |
| Feeding difficulty, recurrent respiratory infections | HP:0011968; HP:0002205 | Cause of death in several cases | 32612635, 33410539 |
| Acquired arthrogryposis | (contractures) | 2/6 | 33410539 |
| Lab: reduced GPI-APs on granulocytes (CD16, FLAER) | — | Every patient tested | 30269814, 33410539 |
| Lab: alkaline phosphatase usually normal | — | Normal in 3; mildly raised in 1 | 33410539, 37035392 |

**Quotes from the sources:**

> "All individuals presented with hypotonia, severe global developmental delay, microcephaly, intractable early infantile epilepsy, and structural brain abnormalities. Additional findings include vision impairment, hearing loss, renal malformation, and hypotonic facial appearances with minor dysmorphic features but without a distinctive facial gestalt. Four individuals died due to neurologic complications." (PMID:33410539)

> "The third family had two fetuses with multiple joint contractures consistent with fetal akinesia." (PMID:30269814)

> "Of the 12 patients with epilepsy, 11 patients had detailed data related to age at seizure onset (range 1 to 12 months). Onset before 3 months of age occurred in 8 patients." (PMID:37035392)

**Onset, course and quality of life.** Onset is prenatal or early infantile. The course is progressive or static, and in some cases hypotonia got worse over time (PMID:37035392). The impact on quality of life is profound: no independent sitting or speech in most cases, and complete dependency. No formal QoL instrument data exist.

---

## 4. Genetic / molecular information

- **Gene:** *PIGS*, HGNC:14937 (write it as `hgnc:14937` in the repo); 17q11.2; Entrez 94005; UniProt Q96S52; Ensembl ENSG00000087111; transcript NM_033198.
- **ClinGen gene–disease validity: Definitive, AR.** Congenital Disorders of Glycosylation GCEP, 2025-06-06. Citable as `CGGV:assertion_38cb0b29-5a46-44c4-a92b-67d69e3347c4-2025-06-06T160000.000Z`. Quotable row:
  > "PIGS | HGNC:14937 | glycosylphosphatidylinositol biosynthesis defect 18 | MONDO:0029140 | AR | Definitive"

  ClinGen also notes: "87 unique variants … have been reported in humans by ClinVar; 13 of these variants are classified as pathogenic or likely pathogenic in ClinVar."

**Reported variants (NM_033198)**

| Variant | Type | State | Evidence |
|---|---|---|---|
| c.108G>A p.(Trp36*) | Nonsense; downstream-Met reinitiation gives residual activity | Compound het with c.101T>C p.(Leu34Pro), a transmembrane-helix missense | PIGS mRNA up to 50% lower, protein reduced; partial rescue in PIGS-KO HEK293 (PMID:30269814) |
| c.1316_1352delins p.(Thr439_Lys451delinsArgLeuLeu) | In-frame delins | Homozygous | Reduced CD16/FLAER (30269814) |
| c.923A>G p.(Glu308Gly) + c.468+1G>C | Missense + canonical splice | Compound het (fetal akinesia family) | CD24 on amniocytes 85% lower (30269814) |
| c.148C>T p.(Gln50*) + c.1141_1164dup p.(Asp381_Val388dup) | Nonsense + in-frame dup | Compound het | Reduced CD59/FLAER (32612635) |
| c.174G>C p.(Gln58His) | Exonic; exon-2 skipping → p.Glu12Alafs*31 | Homozygous (2 families) | Minigene splicing assay (33410539) |
| c.1070G>A p.(Gly357Asp); c.986C>G p.(Pro329Arg) | Missense | Homozygous | In silico prediction only (33410539) |
| c.734G>A p.(Trp245*) + c.1141_1164dup | Nonsense + dup | Compound het | Reduced CD16, FLAER and CD14 (33410539) |
| c.935-6C>G + c.1141_1164dup | Intronic splice (exon 10 skipping) + dup | Compound het | RT-PCR (37035392) |

- **Functional class:** loss of function or hypomorphic. No complete biallelic null has been seen in a liveborn patient. The most severe genotype (canonical splice plus missense) caused fetal akinesia. In the authors' words: "The low signals seen for all GPI-AP markers in individual 3b amniocytes correlates with the severe phenotypes" (PMID:30269814). This supports, though does not prove, a residual-activity–severity gradient.
- **Constraint:** "PIGS is intolerant toward both missense variants (Z = .7801) and biallelic loss of function variants (probability of being loss‐of‐function intolerant = 0, pREC = .9943)" (PMID:33410539).
- **Origin:** all germline. No somatic, epigenetic, chromosomal or CNV mechanisms have been reported.

---

## 5. Environmental information

Not applicable. There are no known environmental, lifestyle or infectious causes. Intercurrent febrile illness lowers the seizure threshold (PMID:32612635, 37035392).

---

## 6. Mechanism / pathophysiology

**Ordered causal chain**

1. **Biallelic *PIGS* LoF or hypomorphic variants** lead to less PIGS mRNA or protein, or to a dysfunctional protein. This is shown in patient LCLs (qPCR, western blot) and by HEK293 rescue (PMID:30269814).
2. **Loss of PIGS** leads to a defective GPI transamidase complex in the ER membrane. The complex has five subunits, PIGK, GPAA1, PIGT, PIGS and PIGU (PMID:35165458, 12802054).
   - Within the complex, loss of PIGS destabilizes PIGK, the catalytic subunit: "loss of PIG-S reduced the stability of PIG-K and left the other subunits unaffected" (PMID:30914202; *Drosophila*/cell model).
   - PIGK carries the "C206-H164-N58 triad that is critical for the transamination reaction" (PMID:35165458).
3. **The defective transamidase** cannot form the carbonyl intermediate, so GPI is not transferred to proproteins. The fully built GPI lipid accumulates but is not attached:
   > "PIG-S and PIG-T knockout cells were defective in transfer of GPI to proteins, particularly in formation of the carbonyl intermediates." (PMID:11483512; mouse F9 cells, IN_VITRO)
4. **Failed GPI attachment** leads to fewer GPI-APs on the cell surface: CD16 and FLAER on granulocytes, FLAER on lymphocytes, CD14 on monocytes, and CD24/CD55/CD59/CD73 on amniocytes (PMID:30269814, 33410539). Proproteins that cannot be anchored are presumably degraded by ER quality control. That step is inferred from the general IGD biology, not shown for PIGS specifically.
5. **Neural branch (inferred):** missing neural GPI-APs (synaptic, adhesion and axon-guidance proteins) lead to abnormal cortical and pontocerebellar development, atrophy and network hyperexcitability. Clinically this appears as DEE, microcephaly, frontotemporal and pontine atrophy, and developmental delay. No PIGS-specific neural experiment exists; the authors infer this from the IGD class. Efthymiou: "There are more than 150 human GPI‐APs, which often play a role in synaptic function, development of the central nervous system (CNS), and plasticity."
6. **Vitamin B6 branch (hypothesis):** less GPI-anchored tissue-nonspecific alkaline phosphatase (TNAP) means less dephosphorylation of PLP to pyridoxal and less pyridoxal transport into the brain. The result would be a CNS pyridoxal-5′-phosphate shortfall and reduced GABA synthesis, lowering the seizure threshold. This is consistent with the pyridoxine response, but CSF PLP has never been measured in PIGS patients ("we could not measure the cerebrospinal fluid pyridoxal‐5‐phosphate levels", PMID:33410539). The link to folate, through the GPI-anchored folate receptor FOLR1, is equally speculative.
7. **Developmental/musculoskeletal branch:** severe GPI-AP deficiency in the fetus leads to fetal akinesia and contractures, and to cystic hygroma and renal cysts (PMID:30269814). The mechanism is not characterized.
8. **Terminal branch:** severe hypotonia, bulbar dysfunction and feeding difficulty lead to aspiration and recurrent respiratory infection, and these drive early death (PMID:32612635, 33410539).

**Process and cell terms**

| Category | Terms |
|---|---|
| GO (verified) | GO:0016255 *attachment of GPI anchor to protein* (core, decreased); GO:0034394 *protein localization to cell surface* (decreased); GO:0007399 *nervous system development*; GO:0005789 *endoplasmic reticulum membrane* (location) |
| GO (unverified) | GO:0042765 *GPI-anchor transamidase complex* |
| Not affected | GO:0006506 *GPI anchor biosynthetic process*. PIGS is not needed for GPI synthesis: "PIG-S and PIG-T are not required for GPI synthesis" (PMID:11483512). |
| CL (verified) | CL:0000540 neuron (presumed affected cell); CL:0000094 granulocyte, CL:0000542 lymphocyte, CL:0000576 monocyte (diagnostic readout cells) |

**Molecular profiling.** No transcriptomic, proteomic, metabolomic, single-cell or CRISPR-screen data specific to PIGS deficiency were found. The human GPI-T cryo-EM structure is available at 3.1 Å (PMID:35165458), and a mutagenesis screen of the transamidase subunits exists (PMID:34576938).

---

## 7. Anatomical structures affected

- **Primary organ: brain.** Frontal and anterior temporal lobes, pons, cerebellar vermis, corpus callosum and white matter (PMID:33410539). Candidate UBERON terms: cerebral cortex, pons, cerebellar vermis, corpus callosum (unverified).
- **Secondary organs:**
  - eye and visual cortex (cortical blindness, nystagmus);
  - inner ear;
  - skeleton (hands: brachytelephalangy);
  - gingiva;
  - kidney (glomerular cysts, malformation);
  - heart (VSD in one case);
  - joints (contractures);
  - respiratory system, secondarily.
- **Subcellular:** ER membrane, where the transamidase sits, and the plasma-membrane outer leaflet, where GPI-APs are lost.
- **Lateralization:** brain changes are bilateral and symmetric.

---

## 8. Temporal development

- **Onset:** prenatal (fetal akinesia, thickened nuchal fold noted in the Li 2023 case) through early infancy. Median seizure onset is under 3 months.
- **Course:** chronic, lifelong and progressive. Seizure types change over time (focal, then myoclonic or spasms), and atrophy progresses on MRI. There is no remission without treatment. A partial or full seizure response to pyridoxine has been reported in 3–4 cases.
- **Critical period:** early infancy, when an early pyridoxine trial is recommended.

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive, HP:0000007 (unverified; it does not appear in the cache lookups above). Penetrance appears complete for biallelic pathogenic genotypes. Expressivity varies from fetal lethal to survival into childhood; the oldest reported individuals were about 7.5–9 years old.
- **Prevalence:** unknown, about 14 reported cases. Use `CASES_IN_LITERATURE`; no numeric estimate exists. IGDs as a whole may account for about 0.15% of developmental disorders: "IGDs alone might account for 0.15% of all developmental disorders" (PMID:30269814, citing the DDD study).
- **Populations:** European (twins), Mexican, Middle Eastern / South Asian (consanguineous families in the Efthymiou cohort, mainly Iran and Pakistan per the authors' recruitment, though country is not stated per family in the abstract), and Chinese (recurrent dup allele). There is no reported sex bias, though most reported cases are male.
- **Not reported:** anticipation, germline mosaicism, carrier-frequency data.

---

## 10. Diagnostics

- **Genetic testing:** trio exome or genome sequencing is the route to diagnosis in every reported case. *PIGS* is on DEE, IGD and CDG panels (Genomics England PanelApp green). RNA studies (minigene assay, RT-PCR) are needed to confirm splice variants (PMID:33410539, 37035392).
- **Flow cytometry (key functional biomarker):** reduced CD16 and FLAER on granulocytes, with CD55/CD59 variably reduced.
  > "Individual 6 had significantly lower levels of CD16 and fluorescent aerolysin (FLAER) in granulocytes, the most sensitive markers of inherited GPI deficiency" (PMID:33410539)
- **Supportive or exclusion labs:**
  - serum alkaline phosphatase, usually normal, which separates PIGS from PIGV/PIGO/PGAP3 deficiency;
  - normal transferrin isoelectric focusing;
  - no 2-oxoglutaric aciduria.

  Nguyen et al.: "Laboratory findings that can help distinguish PIGS-associated disorders … include flow-cytometry analysis with reduced CD16 expression … a lack of elevated serum tissue-nonspecific alkaline phosphatase … and normal serum transferrin isoelectric focusing" (PMID:30269814).
- **EEG:** hypsarrhythmia or pseudohypsarrhythmia, burst suppression, multifocal discharges. The EEG may be normal at onset (PMID:37035392).
- **MRI:** frontotemporal-predominant atrophy, pontine hypoplasia, vermian atrophy, delayed myelination.
- **Differential diagnosis:**
  - other IGDs, especially PIGT, GPAA1, PIGK and PIGU (the transamidase-complex disorders);
  - DOORS syndrome (*TBC1D24*);
  - other CDGs;
  - peroxisomal disorders and mucopolysaccharidoses;
  - other pyridoxine-dependent epilepsies (*ALDH7A1*, *PNPO*);
  - West syndrome of other cause.
- **Screening:** no newborn screening. Cascade carrier testing and prenatal or preimplantation testing are available once the familial variants are known.
- **LOINC:** use the Part or panel-level code for flow-cytometric GPI-AP / FLAER testing if one exists. Not looked up; do not bind without `just loinc-seed-cache`.

---

## 11. Outcome / prognosis

- **Mortality is high.** In the Efthymiou cohort, 4 of 6 died ("Four individuals died due to neurologic complications"), several from recurrent respiratory infection. The Zhang patient died at 15 months, "due to asphyxia during an epileptic seizure" (PMID:32612635). Both fetal-akinesia pregnancies were terminated.
- **Morbidity:** profound intellectual disability, no speech, non-ambulatory in most cases, cortical visual impairment and deafness.
- **Prognostic factors (tentative):** a combined splice/missense or truncating genotype with very low GPI-AP levels points toward fetal lethality. A pyridoxine response is associated with better seizure control and development.

---

## 12. Treatment

There is no disease-modifying therapy. Management is symptomatic.

| Intervention | Evidence | Terms (verified) |
|---|---|---|
| Pyridoxine (vitamin B6) trial | Seizures partly responded (Nguyen, 1 patient; 100 mg/day). Pyridoxine 15 mg/kg/day plus folinic acid 1 mg/kg/day helped 2 patients (Efthymiou). Seizure-free for ≥6 months on 7 mg/kg/day (Li 2023). | `treatment_term` NCIT:C15986 Pharmacotherapy; `therapeutic_agent` CHEBI:16709 pyridoxine |
| Folinic acid | Given together with B6, so its own effect is unproven: "there is no clear evidence describing the effect of folinic acid" | CHEBI:748997 leucovorin / NCIT:C71631 Leucovorin |
| Antiseizure medications (levetiracetam in 9 cases, valproate, topiramate) | Largely refractory | CHEBI:6437, CHEBI:39867, CHEBI:63631 |
| ACTH (for infantile spasms) | Ineffective in the one case where it was tried | CHEBI:3892 corticotropin |
| Ketogenic diet | Suggested by analogy with PIGA deficiency; no PIGS data | NCIT:C15447 Dietary Intervention (from CLAUDE.md list) |
| Supportive care: feeding, respiratory, PT/OT, vision and hearing support | Standard care | NCIT:C15747 Supportive Care; NCIT:C15302 Physical Therapy |
| Genetic counseling | Recurrence risk 25% | NCIT:C15240 Genetic Counseling |

**Quotes:**

> "We confirm that biallelic variants in PIGS cause vitamin pyridoxine-responsive epilepsy due to inherited GPI deficiency" (PMID:33410539)

> "After administration of daily oral pyridoxine (7 mg/kg/day), the patient was more active and gradually became seizure-free." (PMID:37035392)

**Gaps:** there are no clinical trials (no NCT or ICTRP registrations), no gene or RNA therapies, and no pharmacogenomic data. The proposed butyrate therapy for PIGM deficiency (a promoter variant) does not apply to *PIGS*.

---

## 13. Prevention

- **Primary prevention:** genetic counseling, carrier testing of relatives, and prenatal or preimplantation genetic diagnosis for known familial variants. These are especially relevant in consanguineous families.
- **Secondary prevention:** early exome sequencing in infantile DEE, then an early pyridoxine trial.
- **Tertiary prevention:**
  - seizure control;
  - aspiration prevention (feeding assessment, gastrostomy where needed);
  - prompt treatment of respiratory infections, the main cause of death;
  - vision and hearing screening.
- There are no vaccines, no public-health measures and no prophylactic drugs.

---

## 14. Other species / natural disease

- **Orthologs:** mouse *Pigs* (MGI:2687325) and *S. cerevisiae* GPI17. Ohishi et al.: "Saccharomyces cerevisiae … Gpi17p (YDR434W) … orthologues of … PIG-S" (PMID:11483512). There is also an *Arabidopsis* AtPIG-S (PMID:32811442, pollen-tube growth) and a *Drosophila* ortholog (PMID:30914202, 33496978).
- **Naturally occurring disease:** none found in OMIA. No veterinary relevance and no zoonotic potential.

---

## 15. Model organisms

| Model | What it shows | Relationship to the human disease | Source |
|---|---|---|---|
| *Pigs*-KO mouse F9 embryonal carcinoma cells | No surface Thy-1; GPI accumulates unattached; no carbonyl intermediate | Recapitulates the molecular defect; IN_VITRO | PMID:11483512 |
| PIGS-KO HEK293 (CRISPR) | GPI-AP loss; used to test patient variants (Trp36* partial, Leu34Pro mild) | Variant-level functional assay | PMID:30269814 |
| Patient LCLs and blood | Lower PIGS mRNA and protein; low GPI-AP | Human ex vivo | PMID:30269814 |
| *Drosophila* transamidase-subunit mutants | PIG-S needed for PIG-K stability | Complex-assembly biology; MODEL_ORGANISM | PMID:30914202 |
| Yeast *gpi17* depletion | Growth arrest, accumulation of complete GPI precursor | Conserved essential function | PMID:11483512 |

**Whole-animal gap.** No *Pigs* knockout or knock-in mouse or zebrafish has been described. IMPC returned no phenotype records for *Pigs* (MGI:2687325). Nguyen et al. explicitly propose CRISPR knock-in of human *PIGS* variants into mice. By analogy, the *Pigk* and *Pigo* homozygous knockouts in IMPC are embryonic or preweaning lethal, which suggests a null *Pigs* mouse would also be lethal and that hypomorphic knock-ins would be needed. This is an inference by analogy and a candidate `KNOWLEDGE_GAP`.

---

## Notes for the curator

- **ClinGen record.** Record the CGGV assertion above as `gene_disease_validity` (DEFINITIVE, CLINGEN) and quote its table row as evidence.
- **Evidence source per claim:**

  | Source | `evidence_source` | Covers |
  |---|---|---|
  | Ohishi 2001 (PMID:11483512) | IN_VITRO | Mechanism, steps 2–3 |
  | Kawaguchi 2019 (PMID:30914202) | MODEL_ORGANISM / IN_VITRO | PIGK destabilization |
  | Zhang 2022 (PMID:35165458) | IN_VITRO | Structural (cryo-EM) |
  | Nguyen 2018 (PMID:30269814) | HUMAN_CLINICAL | Phenotype and blood flow cytometry |
  | Nguyen 2018 (PMID:30269814) | IN_VITRO | HEK293 rescue; split it into a separate evidence item |

- **Unverified IDs:** GO:0042765, HP:0000007 and all UBERON terms. Look these up before binding them.
- **Coarse term.** HP:0000077 for renal malformation is coarse; prefer HP:0000107 *Renal cyst* for the fetal glomerular cysts.
- **Mechanism wording.** The vitamin B6/TNAP mechanism (step 6) is a hypothesis. Model it as `EMERGING`, or carry it in the description, not as an established edge.
- **Cache files.** `just fetch-reference` wrote 9 new `references_cache/PMID_*.md` files into this worktree. Commit them with the entry if they are cited, or prune them if not.

**Sources:**
- [Nguyen 2018, AJHG (PMID:30269814)](https://pubmed.ncbi.nlm.nih.gov/30269814/)
- [Efthymiou 2021, Epilepsia (PMC7898547)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7898547/)
- [Zhang 2020, Front Genet (PMID:32612635)](https://pubmed.ncbi.nlm.nih.gov/32612635/)
- [Li & Zhou 2023, Transl Pediatr (PMID:37035392)](https://pubmed.ncbi.nlm.nih.gov/37035392/)
- [Ohishi 2001, EMBO J (PMID:11483512)](https://pubmed.ncbi.nlm.nih.gov/11483512/)
- [Kawaguchi 2019, BBRC (PMID:30914202)](https://pubmed.ncbi.nlm.nih.gov/30914202/)
- [Zhang 2022, NSMB (PMID:35165458)](https://pubmed.ncbi.nlm.nih.gov/35165458/)
- [GenCC submission](https://thegencc.org/submissions/SGC-107040.2)
- [LOVD GPIBD18](https://databases.lovd.nl/shared/diseases/05544)
- [PanelApp PIGS](https://nhsgms-panelapp.genomicsengland.co.uk/entities/PIGS)
- [KEGG H01489](https://www.kegg.jp/entry/H01489)
- [HGNC PIGS](https://rest.genenames.org/fetch/symbol/PIGS)
- [OLS MONDO:0029140](https://www.ebi.ac.uk/ols4/ontologies/mondo/classes?obo_id=MONDO:0029140)
- [IMPC](https://www.mousephenotype.org/)
- [Li Shan 2024 IGD review, Acta Biochim Biophys Sin](https://doaj.org/article/72c64ed86208499dbd956743acab5744)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 10 |
| On topic | 6 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:30269814`: "Laboratory findings that can help distinguish PIGS-associated disorders … include flow-cytometry analysis with reduced CD16 expression … a lack of elevated serum tissue-nonspecific alkaline phosphatase … and normal serum transferrin isoelectric focusing"
  - closest text in source: "Laboratory findings that can help distinguish PIGS-associated disorders from other Mendelian disorders include flow-cytometry analysis with reduced CD16 expression (with or without reduced CD55 expression), a lack of elevated serum tissue-nonspecific alkaline phosphatase (observed to be elevated in a number of other IGDs but normal in others), a lack of 2-oxoglutaric aciduria (occasionally seen with TBC1D24 mutations), and normal serum transferrin isoelectric focusing (abnormal with several CDGs)"
- `PMID:11483512`: "Saccharomyces cerevisiae … Gpi17p (YDR434W) … orthologues of … PIG-S"
  - closest text in source: "Saccharomyces cerevisiae GPI16 and GPI17 are orthologues of PIG-T and PIG-S, respectively"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 58 |
| Resolved | 56 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 6 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0070382` (1 mention) - the report calls it "DOID"; DOID calls it **developmental and epileptic encephalopathy 95**
- `HP:0000007` (2 mentions) - the report calls it "unverified; it does not appear in the cache lookups above"; HP calls it **Autosomal recessive inheritance**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MGI:2687325` - called "Pigs", "Orthologs:** mouse *Pigs"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.