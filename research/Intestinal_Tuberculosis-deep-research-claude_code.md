---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-27T23:14:40.637964'
end_time: '2026-11-27T23:18:15.416145'
duration_seconds: 214.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Intestinal Tuberculosis
  mondo_id: MONDO:0001678
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: intestine tuberculosis; tuberculosis of intestine
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
  web_search_requests: 18
  num_turns: 22
  total_cost_usd: 1.0265711
  session_id: 89651666-293b-44b5-9605-05d6d2e21409
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 21
  retrieval_calls: 19
  assistant_text_blocks: 2
citation_count: 56
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 3
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMC:PMC8323646
  - PMC:PMC7106693
  - PMID:19240705
  - PMC:PMC3211607
  relevance_assessed: 32
  on_topic: 12
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 2
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0001678
    reported_labels:
    - given in the template
    ontology_label: intestinal tuberculosis
  service_unreachable: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intestinal Tuberculosis
- **MONDO ID:** MONDO:0001678 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** intestine tuberculosis; tuberculosis of intestine
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Intestinal Tuberculosis** covering all of the
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

Still gathering sources (searching for risk factors, pathology, animal models and guidelines); the report follows after that.

# Intestinal Tuberculosis (MONDO:0001678): Disease Characteristics Research Report

**How I scoped this report.** Intestinal tuberculosis (ITB) is an infectious disease. It has **no causal human gene**: it is caused by bacteria of the *Mycobacterium tuberculosis* complex, mainly *M. tuberculosis* and, less often, *M. bovis*. The causal-gene and OMIM fields in the template are therefore "not applicable", not merely "not recorded". I covered gastrointestinal (luminal) TB and included the overlapping literature on abdominal TB, which also covers peritoneal and mesenteric lymph-node disease, where intestine-specific data were missing.

**Limits on the evidence.**
- Direct PubMed access was blocked in this session, so all evidence comes from web search results.
- Quotations are taken from search snippets of abstracts and reviews. Check them against the primary records before entering them in a knowledge base.
- I only give PMIDs that appeared in retrieved URLs or snippets. Other sources are cited by PMC ID, DOI or URL.
- Following the citation rules, I give ontology terms (HPO, GO, CL, UBERON, NCIT, CHEBI) as **labels only, without IDs**, because I did not retrieve their identifiers in this session. The IDs need a lookup before use.

---

## 1. Disease Information

**Overview.** ITB is tuberculosis of the gastrointestinal tract. It most often affects the ileocecal region, but "it can involve any part of the gastrointestinal tract" ([StatPearls, NBK556115](https://ncbi.nlm.nih.gov/books/NBK556115)).

The MeSH scope note defines it as "tuberculosis that involves any region of the GASTROINTESTINAL TRACT, mostly in the distal ILEUM and the CECUM", with *M. tuberculosis* as the usual pathogen ([MeSH D014385](https://meshb.nlm.nih.gov/record/ui?ui=D014385)).

A 2021 systematic review (Al-Zanbagi & Shariff, *Saudi J Gastroenterol*, PMID 34213424, [PMC8555774](https://pmc.ncbi.nlm.nih.gov/articles/PMC8555774)) calls gastrointestinal TB a leading form of extrapulmonary TB that "can defy diagnosis", because its symptoms overlap with other gut diseases and diagnostic tests have limited accuracy.

**Identifiers**

| Resource | Identifier | Source |
|---|---|---|
| MONDO | MONDO:0001678 (given in the template) | — |
| MeSH | D014385 "Tuberculosis, Gastrointestinal" | [MeSH](https://meshb.nlm.nih.gov/record/ui?ui=D014385) |
| Disease Ontology | DOID:404 "gastrointestinal tuberculosis" (cross-references MeSH D014385 and ICD-9-CM 014) | [MGI/DO](https://www.informatics.jax.org/disease/DOID:404) |
| ICD-10 | A18.3 "Tuberculosis of intestines, peritoneum and mesenteric glands"; K93.0 is the asterisk (manifestation) code | [AAPC](https://www.aapc.com/codes/icd-10-codes/A18.3); [gesund.bund.de K93.0](https://gesund.bund.de/en/icd-code-suche/k93-0) |
| ICD-11 | Not retrieved in this session | — |
| OMIM / Orphanet | Not applicable (infectious, not a Mendelian or rare-disease entity); no entry retrieved | — |

**Synonyms:** intestine tuberculosis; tuberculosis of intestine; gastrointestinal tuberculosis; tuberculosis of gastrointestinal tract; tuberculosis of intestines, peritoneum and mesenteric glands ([DOID:404](https://www.informatics.jax.org/disease/DOID:404)). "Abdominal tuberculosis" is a broader parent concept that also includes peritoneal, nodal and solid-organ disease.

**Data source type:** The information is aggregated at disease level, from reviews, case series, cohorts, meta-analyses and RCTs. It is not drawn from individual-patient EHR data.

---

## 2. Etiology

**Causal factors (infectious).**
- The main cause is *M. tuberculosis*. *M. bovis*, the agent of zoonotic TB, is a secondary cause.
- ITB "is caused predominantly by infection with M. tuberculosis, the same bacterium responsible for pulmonary tuberculosis" ([Springer review 2025](https://link.springer.com/10.1007/s44162-025-00090-1); [UCL PDF](https://discovery-pp.ucl.ac.uk/17114/1/17114.pdf)).
- Suggested routes of entry into the gut are swallowing infected sputum, eating contaminated food (unpasteurised milk for *M. bovis*), spread through the blood, and spread from neighbouring organs. My searches did not retrieve a source that ranks these routes, so treat the list as background.

**Risk factors (environmental and host).**
- **HIV co-infection.** Extrapulmonary disease is about 20% of all TB but about 50% of TB in people with HIV ([StatPearls extrapulmonary TB](https://www.statpearls.com/point-of-care/30659)). In industrialised countries, most abdominal TB occurs in people co-infected with HIV, or in immigrants from high-prevalence regions where reactivation is the usual mechanism ([StatPearls abdominal TB](https://www.statpearls.com/point-of-care/30658)). In an HIV/TB co-infected cohort, extrapulmonary TB was 28% of cases, and abdominal TB was 11% of the extrapulmonary cases ([PMC8555774](https://pmc.ncbi.nlm.nih.gov/articles/PMC8555774)).
- **Other host factors** listed in a 2023 review: younger age, female sex, Asian ethnicity, immunosuppression, diabetes and peritoneal dialysis ([Indian J Gastroenterol 2023, doi 10.1007/s12664-023-01343-x](https://link.springer.com/10.1007/s12664-023-01343-x)).
- **Anti-TNF and other immunosuppression**, often given for IBD or for ITB misdiagnosed as Crohn's disease. In a GETAID cohort of 44 patients with IBD on anti-TNF therapy, TB developed despite negative screening before treatment and was "mostly extrapulmonary and disseminated" ([HAL 01470713](https://hal-clermont-univ.archives-ouvertes.fr/hal-01470713)).
- **Unpasteurised milk and dairy products**, for *M. bovis* ([WHO zoonotic TB roadmap](https://www.who.int/news/item/12-10-2017-tb-partners-launch-first-roadmap-to-jointly-stop-the-transmission-of-bovine-and-zoonotic-tuberculosis)).
- **Residence in or migration from a TB-endemic region** ([StatPearls](https://www.statpearls.com/point-of-care/30658)).

**Genetic risk factors (susceptibility only, not causal).**
- **ITB-specific evidence.** Yu & Chen (2019, *World J Gastroenterol* 25:2473, doi 10.3748/wjg.v25.i20.2473, [PMC6543246](https://pmc.ncbi.nlm.nih.gov/articles/PMC6543246)) studied 133 ITB patients, 128 Crohn's disease patients and 500 controls in China, genotyping SNPs in the IL-23/IL-17 axis.
  - They report that "rs2227473 and rs1143627 polymorphisms affect ITB susceptibility instead of CD".
  - They state that "the IL22 gene promoter SNP rs2227473 G allele is a risk factor for intestinal tuberculosis".
  - The abstract also reports an A-allele frequency difference with OR = 0.60, P = 0.030. The direction of the allele effect is ambiguous and needs checking in the full text.
  - The gene for rs1143627 was not confirmed from the snippets; it is commonly attributed to the *IL1B* promoter, but this was not verified here.
- **Evidence from TB in general, not ITB-specific.**
  - *NOD2*: Arg587Arg was associated with TB in Han Chinese, and a meta-analysis suggests Arg702Trp may be protective ([BMC Infect Dis 12:91](https://link.springer.com/doi/10.1186/1471-2334-12-91); [PMC3862802](https://pmc.ncbi.nlm.nih.gov/articles/PMC3862802)).
  - *SLC11A1* (NRAMP1), *VDR*, *HLA-DRB1* and *HLA-DQB1* were associated with TB in Chinese Kazakhs ([PMC3758880](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3758880/)).
  - *TLR2* rs1898830 was associated with TB in Han and Tibetan populations, while *TLR4* rs11536889 and *TOLLIP* rs3750920 were protective in Tibetans ([PMC7403954](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7403954/)).
- **Databases.** No GWAS Catalog, ClinVar or ClinGen entries specific to ITB were retrieved.

**Protective factors**
- Heat treatment of milk: "Heat-treatment of milk is key to reducing the risk to people" (WHO).
- Control of HIV.
- Screening for and treating latent TB before immunosuppression ([HAL 01470713](https://hal-clermont-univ.archives-ouvertes.fr/hal-01470713)).
- Genetic: *NOD2* Arg702Trp and the Tibetan-population *TLR4*/*TOLLIP* variants, both from TB in general.
- Yu & Chen suggest that high IL-22 expression "seems to be a protective factor for intestinal tuberculosis" ([PMC6543246](https://pmc.ncbi.nlm.nih.gov/articles/PMC6543246)).

**Gene–environment interactions**
- The best-documented interaction is iatrogenic: anti-TNF therapy (a drug blocking a host pathway) combined with latent *M. tuberculosis* infection leads to reactivation and disseminated extrapulmonary TB.
- HIV-related CD4 depletion combined with TB exposure is the other major interaction.
- I did not retrieve any formal GxE studies for ITB.

---

## 3. Phenotypes

Frequencies come from case series with different selection criteria, and surgical series over-represent obstruction ([Hong Kong series, hkmj.org](https://www.hkmj.org/system/files/hkm0608p264.pdf); [BMC Gastroenterol 5:21](https://link.springer.com/doi/10.1186/1471-230X-5-21); [JAMC](https://jamc.ayubmed.edu.pk/index.php/jamc/article/download/4269/2384/17175)).

| Phenotype | Type | Frequency | Suggested HPO label (ID to look up) |
|---|---|---|---|
| Abdominal pain | Symptom | 82% (Hong Kong); 100% (50-patient surgical series) | Abdominal pain |
| Weight loss | Sign | 20–83% (55% Hong Kong; 82.7% in a Pakistani series of 52) | Weight loss |
| Diarrhoea (more common than constipation) | Symptom | 55% (Hong Kong) | Diarrhea |
| Fever | Sign | 45% (Hong Kong) | Fever |
| Constipation / change in bowel habit | Symptom | Variable | Constipation |
| Nausea and vomiting, abdominal distension | Symptom | Variable | Nausea; Vomiting; Abdominal distention |
| Bowel obstruction | Clinical sign / complication | Common presentation in surgical series ([PMC7106693](https://pmc.ncbi.nlm.nih.gov/articles/PMC7106693)) | Intestinal obstruction |
| Perforation and peritonitis | Complication | Most common presentation in a 161-patient African surgical series | Bowel perforation; Peritonitis |
| Bleeding and fistula | Complication | Reported with ulcerative forms ([Springer 2025](https://link.springer.com/10.1007/s44162-025-00090-1)) | Gastrointestinal hemorrhage; Intestinal fistula |
| Stricture | Late sign | Follows healing of transverse ulcers | Intestinal stenosis |
| Caseating granulomas on biopsy | Laboratory / pathology finding | Hallmark; caseation has low sensitivity ([PMC4191941](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4191941/)) | Granuloma |
| Elevated CRP/ESR, anaemia, hypoalbuminaemia | Laboratory findings | Common, but I did not retrieve frequencies | Elevated C-reactive protein; Elevated erythrocyte sedimentation rate; Anemia; Hypoalbuminemia |

**Onset, severity and progression**
- Onset is usually in adulthood, though a paediatric cohort exists ([PMC3211607](https://pmc.ncbi.nlm.nih.gov/articles/PMC3211607)).
- Onset is subacute to chronic and insidious. Diagnosis "is often delayed due to its non-specific presentation" ([PMC8323646](https://pmc.ncbi.nlm.nih.gov/articles/PMC8323646)).
- Without treatment the disease progresses. Patients "usually present when complications such as bowel obstruction or perforation had occurred" ([PMC7106693](https://pmc.ncbi.nlm.nih.gov/articles/PMC7106693)).

**Quality of life:** I did not retrieve any EQ-5D or SF-36 studies specific to ITB.

---

## 4. Genetic/Molecular Information

**Human causal genes, pathogenic variants (ACMG classification), allele frequencies, somatic origin, chromosomal abnormalities and epigenetics:** none of these apply. ITB is an acquired infection.

**Host susceptibility and modifier genes:** see Section 2. The candidates are *IL22* (rs2227473), *NOD2*, *SLC11A1*, *VDR*, *TLR2*, *TLR4* and *TOLLIP*. Except for the *IL22* finding, the evidence comes from pulmonary or all-site TB, which leaves a gap for ITB specifically. A practically relevant point is that *NOD2* is the main Crohn's disease gene, yet the ITB study found the IL-23/IL-17 SNPs distinguished ITB from Crohn's disease ([PMC6543246](https://pmc.ncbi.nlm.nih.gov/articles/PMC6543246)).

**Pathogen genetics**
- *M. bovis* "is naturally resistant to one of the main first-line drugs (pyrazinamide)" ([WHO roadmap](https://www.who.int/publications/i/item/9789241513043)).
- Rifampicin resistance in ITB can be detected with Xpert MTB/RIF (see Section 10).

---

## 5. Environmental Information

- **Infectious agents:** the *Mycobacterium tuberculosis* complex, mainly *M. tuberculosis* and *M. bovis*. NCBI Taxonomy IDs were not retrieved in this session.
- **Zoonotic burden of *M. bovis*:** WHO estimated "147,000 new cases of ZTB and 12,500 deaths" in 2016. True incidence is "likely to be underestimated" because routine labs cannot tell *M. bovis* from *M. tuberculosis* ([PMC6008525](https://pmc.ncbi.nlm.nih.gov/articles/PMC6008525)).
- **Lifestyle:** drinking unpasteurised or unboiled milk and eating undercooked meat, for *M. bovis* ([WHO](https://www.who.int/news/item/16-04-2016-who-and-the-union-organize-landmark-consultation-to-galvanize-action-against-zoonotic-tb)).
- **Other factors:** crowding and poverty in endemic regions. These were not specifically retrieved for ITB.
- **Smoking and alcohol:** I found no ITB-specific data. Yu & Chen adjusted their analyses for smoking and drinking but did not report them as risk factors.

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain**

1. **Exposure.** Mycobacteria reach the gut lumen through swallowed sputum from active pulmonary TB, contaminated milk (*M. bovis*), spread through the blood, or spread from neighbouring organs. The relative weight of each route was not quantified in retrieved sources.
2. **Uptake.** Bacilli in the lumen are taken up by **M cells** of the follicle-associated epithelium over **Peyer's patches**, mostly in the ileocecal region. This step is described in reviews; the human evidence is mainly morphological, so it is partly inferred. M cells "provide a route of entry for pathogens into the mucosa and can phagocytose tubercle bacilli" ([UCL review](https://discovery-pp.ucl.ac.uk/17114/1/17114.pdf)). The ileocecal predilection is attributed to abundant lymphoid tissue and stasis, which is inferred.
3. **Infection of phagocytes.** Bacilli crossing the epithelium are "ingested by macrophages and dendritic cells in the subepithelial region". The bacilli survive inside these cells.
4. **Granuloma formation.** Innate and adaptive cell-mediated immunity (Th1/IFN-γ, TNF-dependent, and the IL-23/IL-17/IL-22 axis, which is inferred from TB biology and the ITB genetic study) leads to granulomas "initially in the mucosa or Peyer's patches". These are confluent epithelioid granulomas with Langhans giant cells, a lymphocyte cuff and **central caseous necrosis** ([UCL](https://discovery-pp.ucl.ac.uk/17114/1/17114.pdf); [Thieme](https://thieme-connect.com/products/ejournals/pdf/10.4103/0974-2727.59700.pdf)).
5. **Spread and ulceration.** Granulomas spread along the lymphatics of the bowel wall and lead to mucosal ulceration. The **transverse ulcers** are thought to follow the circumferential path of the intestinal lymphatics; this is a hypothesis, not a demonstrated mechanism.
6. **Lymphatic spread.** Spread to mesenteric lymph nodes leads to caseating lymphadenitis, which may form masses or calcify.
7. **Three branches of tissue response** ([Springer 2025](https://link.springer.com/10.1007/s44162-025-00090-1)):
   - **Ulcerative form**, the most common: transverse ulcers lead to bleeding, perforation or fistulas.
   - **Hypertrophic form**: fibroblastic and inflammatory thickening leads to an ileocecal mass and pseudotumour.
   - **Fibrostenotic form**: healing with fibrosis leads to strictures and bowel obstruction.
8. **Clinical expression.**
   - Local disease leads to pain, diarrhoea, obstruction, a mass, bleeding and peritonitis.
   - Systemic cytokine release (TNF and others) leads to fever, weight loss, anaemia and raised acute-phase reactants. This link is inferred.
9. **Immunosuppression as a modifier.** Anti-TNF therapy or HIV impairs granuloma containment, which results in disseminated disease ([PMC6942708](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6942708/); [HAL 01470713](https://hal-clermont-univ.archives-ouvertes.fr/hal-01470713)).

**Supporting detail**
- **Upstream vs downstream.** Uptake by M cells and macrophages is upstream. Granuloma formation and caseation are the core mid-chain step. Fibrosis, stricture, perforation and systemic wasting are downstream.
- **Suggested GO process labels:** phagocytosis; granuloma formation; inflammatory response; response to bacterium; interferon-gamma-mediated signaling pathway; tumor necrosis factor-mediated signaling pathway; interleukin-17-mediated signaling; necrotic cell death; tissue remodeling / fibrosis.
- **Suggested CL cell labels:** microfold cell of epithelium of small intestine (M cell); macrophage; epithelioid cell; Langhans giant cell / multinucleate giant cell; dendritic cell; CD4-positive T cell (Th1, Th17); fibroblast.
- **Immunohistochemistry:** IL-22R1 expression was higher in ITB tissue than in controls ([PMC6543246](https://pmc.ncbi.nlm.nih.gov/articles/PMC6543246)).
- **Not retrieved for ITB:** transcriptomic, proteomic, metabolomic, single-cell, spatial and CRISPR data.

---

## 7. Anatomical Structures Affected

- **Primary organs:**
  - Distal ileum and caecum (ileocecal region), the most common site ([MeSH](https://meshb.nlm.nih.gov/record/ui?ui=D014385)).
  - Ileum in 43% and ileocecal valve in 35% of a surgical series ([BMC Gastroenterol 5:21](https://link.springer.com/doi/10.1186/1471-230X-5-21)).
  - Less often the jejunum, colon, anorectum, duodenum, stomach and oesophagus.
- **Secondary involvement:** mesenteric lymph nodes, peritoneum (ascites), and coexisting pulmonary TB. Chest CT raised the sensitivity of ITB diagnosis from 26.2% to 56.9% ([Intest Res 20(2), KoreaMed](https://synapse.koreamed.org/articles/1516081332)).
- **Body systems:** digestive and immune/lymphatic, and respiratory when lung disease coexists.
- **Tissue level:** mucosa, mucosa-associated lymphoid tissue and Peyer's patches, submucosa, and serosa. Lesions are seen "mainly in the submucosal and serosal layers".
- **Subcellular level (suggested GO cellular-component labels):** phagosome; lysosome; phagolysosome. These are inferred from general TB biology.
- **Suggested UBERON labels:** ileum; cecum; ileocecal valve; Peyer's patch; jejunum; colon; mesenteric lymph node; peritoneum.
- **Laterality:** not applicable. In the abdomen, lesions are predominantly right-sided (ileocecal).

---

## 8. Temporal Development

- **Onset:** mainly young to middle-aged adults; children are also affected ([PMC3211607](https://pmc.ncbi.nlm.nih.gov/articles/PMC3211607)). Onset is insidious, usually with weeks to months of symptoms. Some patients present acutely with obstruction or perforation.
- **Stages:** there is no formal staging. The sequence is mucosal and lymphoid infection, then granuloma and ulceration, then hypertrophic or fibrostenotic healing, then complications.
- **Course:** progressive without treatment. Treatment produces remission; a 2025 review cites recurrence in 13–20% of cases even with treatment ([Springer 2025](https://link.springer.com/10.1007/s44162-025-00090-1)). This figure was not verified against primary data.
- **Critical windows:**
  - Diagnosis before complications develop.
  - Screening before anti-TNF therapy, with repeat screening for ongoing exposure ([HAL 01470713](https://hal-clermont-univ.archives-ouvertes.fr/hal-01470713)).
  - The empirical ATT trial window in uncertain ITB vs Crohn's disease, which may delay a Crohn's diagnosis (Kedia et al., *WJG* 2019;25:418, [wjgnet](https://wjgnet.com/1007-9327/abstract/v25/i4/418.htm)).

---

## 9. Inheritance and Population

- **Inheritance:** not applicable. ITB is not Mendelian; host susceptibility is multifactorial. Penetrance, anticipation, founder effects and carrier frequency do not apply.
- **Global TB context:**
  - WHO estimated about 10.8 million incident TB cases in **2023** (range 10.1–11.7 million), or 134 per 100,000 ([WHO GTB Report 2024](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2024/tb-disease-burden/1-1-tb-incidence)).
  - The 2025 report states that incidence fell in 2024 ([WHO GTB 2025](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025/tb-disease-burden/1-1-tb-incidence)).
  - Extrapulmonary TB is about 20% of all TB ([StatPearls](https://www.statpearls.com/point-of-care/30659)).
  - I did not retrieve a reliable global incidence for ITB itself.
- **Geography:** endemic in South and Southeast Asia, Africa and East Asia, which is also where most of the clinical series come from (India, China, Korea, Malaysia, Tanzania, Nigeria). In high-income countries it mainly affects migrants and people with HIV ([StatPearls](https://www.statpearls.com/point-of-care/30658)).
- **Sex and age:** a 2023 review lists female sex and younger age as risk factors for abdominal TB ([doi 10.1007/s12664-023-01343-x](https://link.springer.com/10.1007/s12664-023-01343-x)). I did not retrieve a precise sex ratio.

---

## 10. Diagnostics

**Microbiology and molecular tests on biopsies**
- **Xpert MTB/RIF.** Ding et al., *Lab Med* 2024;55(2):238, reported a pooled sensitivity of **48%** and specificity of **99%**: "limited diagnostic sensitivity … but with high specificity" ([Lab Med](https://dbpia.nl.go.kr/labmed/article/55/2/238/7235716)).
- **TB PCR.** A meta-analysis found PCR "promising and highly specific" for separating ITB from Crohn's disease (*Saudi J Gastroenterol* 2017, [PMC5329974](https://pmc.ncbi.nlm.nih.gov/articles/PMC5329974)).
- **Culture and histology.** Sending more colonoscopic biopsies for culture raises the yield, and culture and histology are complementary (Mehta et al., PMID 31111030).

**Histopathology**
- Large, confluent caseating granulomas are the hallmark, but caseation has low sensitivity.
- Confluent granulomas and ulcers lined by epithelioid histiocytes were proposed as more sensitive discriminators from Crohn's disease (*PLoS One* 2014 meta-analysis, [PMC4191941](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4191941/)).

**Interferon-gamma release assays (IGRA)**
- Chen et al. 2013 (*WJG* 19:8133) pooled a sensitivity of **0.74** and specificity of **0.87**, with LR+ 5.98 ([wjgnet](https://www.wjgnet.com/1007-9327/full/v19/i44/8133.htm)).
- Ng et al. (*J Gastroenterol Hepatol* 29:1664) found T-SPOT.TB more sensitive than QuantiFERON ([CUHK archive](https://webarchive.lib.cuhk.edu.hk/20211102153335mp_/https://onlinelibrary.wiley.com/doi/full/10.1111/jgh.12645)).
- In an endemic setting, IGRA sensitivity was only 40.68% and specificity 75.51% (Sachdeva et al., *Intest Res* 2023, [DOAJ](https://doaj.org/article/03384b832b9b4760af780623d818d1ef)).

**Imaging**
- CT and CT enterography features have been pooled in a meta-analysis ([Intest Res, KoreaMed](https://synapse.koreamed.org/articles/1516082233)).
- Chest CT for coexisting lung TB raises diagnostic sensitivity ([KoreaMed](https://synapse.koreamed.org/articles/1516081332)).
- "Imaging techniques coupled with fine needle biopsies are useful aids" (PMID 19623062).

**Clinical criteria and algorithms**
- Logan's modified criteria make "response to anti tubercular therapy … a key factor in establishing the diagnosis of ITB".
- Kedia et al. 2019 give an algorithm for following a patient on an ATT trial ([WJG 25:418](https://wjgnet.com/1007-9327/abstract/v25/i4/418.htm)).
- A combined laboratory, imaging and endoscopy model has been developed for separating Crohn's disease from ITB ([PMC8276438](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8276438/)).

**Differential diagnosis**
- **Crohn's disease.** This is the key differential, because the two "have overlapping clinical, radiological, endoscopic and histological characteristics" (PMID 17539977; also PMID 19240705). Male sex, bloody stools, perianal disease and extraintestinal manifestations favour Crohn's disease ([PMC5551982](https://pmc.ncbi.nlm.nih.gov/articles/PMC5551982)).
- **Others:** malignancy (lymphoma, caecal carcinoma), amoebiasis, *Yersinia* infection, and other granulomatous diseases.

**Genetic testing:** not applicable to diagnosis.

**Screening:** IGRA or tuberculin testing for latent TB before biologic therapy; no population screening for ITB exists.

---

## 11. Outcome/Prognosis

**Mortality**
- A prospective Malaysian cohort of 52 gastrointestinal TB patients reported 79% treatment completion, 21% adverse events, **13% mortality** and no treatment failures ([BMC Infect Dis, doi 10.1186/s12879-020-04983-y](https://link.springer.com/10.1186/s12879-020-04983-y)).
- Across surgical series the range is wide, from 0% to about 45%. One South Asian series of 25 patients reported 8% mortality from sepsis.
- Untreated mortality may exceed 40% ([Springer 2025](https://link.springer.com/10.1007/s44162-025-00090-1)).

**Prognostic factors**
- Late presentation with perforation or peritonitis.
- Emergency surgery.
- In children: older age, small-bowel involvement and surgery are "independently associated with higher mortality" ([PMC3211607](https://pmc.ncbi.nlm.nih.gov/articles/PMC3211607)).
- In an African series, moving away from early laparotomy cut morbidity from 30% to 11% and mortality from 12% to 0%.

**Complications:** obstruction, perforation, fistula, bleeding, stricture, malabsorption, and disseminated TB (especially after misdiagnosis as Crohn's disease treated with immunosuppression, which "can be fatal": [PMC6942708](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6942708/)).

**Recovery:** most patients respond to ATT; the recurrence rate is in Section 8.

**Quality-of-life and disability data:** not retrieved.

---

## 12. Treatment

**Pharmacotherapy**
- Standard first-line ATT: isoniazid, rifampicin, pyrazinamide and ethambutol for a 2-month intensive phase, then isoniazid and rifampicin. Suggested NCIT label: "Antitubercular Agent". Suggested CHEBI labels: isoniazid; rifampicin; pyrazinamide; ethambutol.
- *M. bovis* is intrinsically resistant to pyrazinamide (WHO).
- **Duration (Cochrane, Jullien et al. 2016, PMID 27801499):** "Most current guidelines recommend treating … abdominal TB … for six months". In the pooled RCTs, which were all from Asia and excluded HIV, relapse occurred in 2 of 140 patients on 6 months versus 0 of 129 on 9 months. Deaths all occurred in the first 4 months ([Cochrane](https://www.cochrane.org/evidence/CD012163_six-month-therapy-people-abdominal-tuberculosis)).
- **Makharia multicentre RCT:** 6 versus 9 months of intermittent directly observed therapy (NCT01124929, [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT01124929)).
- **Empirical treatment:** a 1998 review recommends empirical ATT when ITB is suspected, even when histology, smear and culture are negative (PMID 9625110).
- **Adverse effects:** hepatotoxicity is the main risk, including with an empirical trial ([PMC11642180](https://pmc.ncbi.nlm.nih.gov/articles/PMC11642180)).
- **Pharmacogenomics:** NAT2 acetylator status and isoniazid toxicity were not retrieved in this session.

**Surgery** (NCIT labels: "Intestinal Resection"; "Strictureplasty"; "Laparotomy")
- Indicated for diagnostic doubt, suspected neoplasm, perforation or obstruction (PMID 9625110).
- Laparotomy should be reserved for complications or a diagnosis that remains unclear (African series, above).

**Supportive care:** nutritional support and endoscopic dilation of strictures; no ITB-specific trials were retrieved.

**Biologics in co-existing IBD:** after TB, restarting anti-TNF therapy "seems safe" ([HAL 01470713](https://hal-clermont-univ.archives-ouvertes.fr/hal-01470713)). Guidance on whether to continue anti-TNF therapy during TB differs between the BTS and the ACR ([PMC3063288](https://pmc.ncbi.nlm.nih.gov/articles/PMC3063288)).

**Not applicable:** gene, cell or RNA therapies, and targeted therapies.

**Experimental:** apart from NCT01124929, I did not retrieve ITB-specific trials.

---

## 13. Prevention

- **Primary prevention:**
  - Control of pulmonary TB, which is the source of swallowed bacilli.
  - Pasteurisation of milk and control of bovine TB, under the 2017 WHO/FAO/WOAH/Union zoonotic TB roadmap and its ten priorities ([WHO](https://www.who.int/publications/i/item/9789241513043)).
  - HIV control.
- **Immunisation:** BCG. I did not retrieve ITB-specific efficacy data.
- **Secondary prevention:** screening for and treating latent TB before anti-TNF or immunosuppressive therapy, with repeat screening when exposure continues.
- **Tertiary prevention:** early ATT to prevent strictures and perforation, and avoiding immunosuppression until ITB has been excluded in endemic areas (PMID 17539977).
- **Genetic counselling:** not applicable.

---

## 14. Other Species / Natural Disease

- **Cattle (bovine TB, *M. bovis*)** are the main animal reservoir. The disease is zoonotic and spreads mainly through unpasteurised milk (WHO).
- *M. bovis* and *M. orygis* have been studied in oral-route mouse models (see Section 15).
- Intestinal involvement in natural bovine TB, wildlife reservoirs and OMIA entries were not retrieved in detail.
- Orthologous genes: not applicable, since there is no causal gene.

---

## 15. Model Organisms

- **Oral-infection mouse model:** streptomycin pretreatment before oral gavage "significantly increased organ colony forming units". This was applied to *M. bovis* and *M. orygis* ([McGill thesis](https://escholarship.mcgill.ca/downloads/db78tj62c); Duffy et al., *Gut Pathog* 2023, doi 10.1186/s13099-023-00573-w). Whether this model reproduces human-type intestinal granulomas was **not confirmed** in retrieved snippets.
- **General TB models, not intestine-specific** ([PMC6984742](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6984742/); [PMC4871865](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4871865/)):
  - **Guinea pigs** are highly susceptible and need only a few bacilli to become infected.
  - **Rabbits** have granulomas resembling human histopathology, but few commercial reagents exist.
  - **Mice** are the most common model but lack some human immune features.
  - **Zebrafish with *M. marinum*** form macrophage aggregates and granulomas and do not need BSL-3 containment.
- **Limitations:** "no animal model perfectly recapitulates the human TB syndrome". No well-validated model reproduces ileocecal transverse ulcers or fibrostenosis.
- **Genetic models:** knockout mice for IFN-γ, TNF and similar genes are widely used for TB in general, but were not retrieved here for ITB.

---

### Key gaps for curation
- Global ITB incidence.
- ICD-11 code.
- HPO, GO, CL, UBERON, NCIT and CHEBI IDs (labels are given; IDs need lookup).
- Phenotype frequencies from large cohorts.
- Omics data.
- Quality-of-life data.
- Fidelity of ITB-specific animal models.
- All quotes and PMIDs need checking against PubMed, because only search snippets were available.

### Sources
- [PMC8555774 / PMID 34213424 – Al-Zanbagi & Shariff 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8555774)
- [PMID 19623062](https://pubmed.ncbi.nlm.nih.gov/19623062/)
- [PMID 9625110](https://pubmed.ncbi.nlm.nih.gov/9625110/)
- [PMID 17539977](https://pubmed.ncbi.nlm.nih.gov/17539977/)
- [PMID 19240705](https://pubmed.ncbi.nlm.nih.gov/19240705/)
- [PMID 27801499 – Cochrane](https://www.pubmed.gov/27801499/); [Cochrane summary](https://www.cochrane.org/evidence/CD012163_six-month-therapy-people-abdominal-tuberculosis)
- [NCT01124929](https://clinicaltrials.gov/study/NCT01124929)
- [StatPearls NBK556115](https://ncbi.nlm.nih.gov/books/NBK556115); [StatPearls abdominal TB](https://www.statpearls.com/point-of-care/30658); [StatPearls extrapulmonary TB](https://www.statpearls.com/point-of-care/30659)
- [Springer 2025 review](https://link.springer.com/10.1007/s44162-025-00090-1); [UCL review](https://discovery-pp.ucl.ac.uk/17114/1/17114.pdf); [Indian J Gastroenterol 2023](https://link.springer.com/10.1007/s12664-023-01343-x)
- [MeSH D014385](https://meshb.nlm.nih.gov/record/ui?ui=D014385); [DOID:404](https://www.informatics.jax.org/disease/DOID:404); [ICD-10 A18.3](https://www.aapc.com/codes/icd-10-codes/A18.3); [K93.0](https://gesund.bund.de/en/icd-code-suche/k93-0)
- [WHO GTB 2024](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2024/tb-disease-burden/1-1-tb-incidence); [WHO GTB 2025](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2025/tb-disease-burden/1-1-tb-incidence)
- [WHO zoonotic TB roadmap](https://www.who.int/publications/i/item/9789241513043); [WHO news 2017](https://www.who.int/news/item/12-10-2017-tb-partners-launch-first-roadmap-to-jointly-stop-the-transmission-of-bovine-and-zoonotic-tuberculosis); [PMC6008525](https://pmc.ncbi.nlm.nih.gov/articles/PMC6008525)
- [PMC6543246 – IL22 SNP study](https://pmc.ncbi.nlm.nih.gov/articles/PMC6543246); [PMC3758880](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3758880/); [PMC7403954](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7403954/); [BMC Infect Dis 12:91](https://link.springer.com/doi/10.1186/1471-2334-12-91); [PMC3862802](https://pmc.ncbi.nlm.nih.gov/articles/PMC3862802)
- [PMC5551982](https://pmc.ncbi.nlm.nih.gov/articles/PMC5551982); [PMC4191941](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4191941/); [PMC5329974](https://pmc.ncbi.nlm.nih.gov/articles/PMC5329974); [Intest Res CT meta-analysis](https://synapse.koreamed.org/articles/1516082233); [Intest Res chest CT](https://synapse.koreamed.org/articles/1516081332)
- [Lab Med 2024 Xpert](https://dbpia.nl.go.kr/labmed/article/55/2/238/7235716); [WJG 2013 IGRA](https://www.wjgnet.com/1007-9327/full/v19/i44/8133.htm); [JGH 29:1664](https://webarchive.lib.cuhk.edu.hk/20211102153335mp_/https://onlinelibrary.wiley.com/doi/full/10.1111/jgh.12645); [Intest Res 2023 IGRA](https://doaj.org/article/03384b832b9b4760af780623d818d1ef)
- [Kedia WJG 2019](https://wjgnet.com/1007-9327/abstract/v25/i4/418.htm); [PMC11642180](https://pmc.ncbi.nlm.nih.gov/articles/PMC11642180); [PMC8276438](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8276438/)
- [PMC6942708](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6942708/); [HAL 01470713](https://hal-clermont-univ.archives-ouvertes.fr/hal-01470713); [PMC3063288](https://pmc.ncbi.nlm.nih.gov/articles/PMC3063288)
- [BMC Infect Dis 2020 Malaysia](https://link.springer.com/10.1186/s12879-020-04983-y); [PMC7106693](https://pmc.ncbi.nlm.nih.gov/articles/PMC7106693); [PMC3211607](https://pmc.ncbi.nlm.nih.gov/articles/PMC3211607)
- [Hong Kong series](https://www.hkmj.org/system/files/hkm0608p264.pdf); [BMC Gastroenterol 5:21](https://link.springer.com/doi/10.1186/1471-230X-5-21); [JAMC](https://jamc.ayubmed.edu.pk/index.php/jamc/article/download/4269/2384/17175); [PMC8323646](https://pmc.ncbi.nlm.nih.gov/articles/PMC8323646); [Thieme](https://thieme-connect.com/products/ejournals/pdf/10.4103/0974-2727.59700.pdf)
- [McGill thesis](https://escholarship.mcgill.ca/downloads/db78tj62c); [Gut Pathog 2023](https://link.springer.com/10.1186/s13099-023-00573-w); [PMC6984742](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6984742/); [PMC4871865](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4871865/)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 32 |
| On topic | 12 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC8323646` *(abstract only)*: "is often delayed due to its non-specific presentation"
  - closest text in source: "CONCLUSION: Abdominal TB causes a significant problem in diagnosis due to nonspecific symptomatology and lack of specific laboratory tests"
- `PMC:PMC7106693` *(abstract only)*: "usually present when complications such as bowel obstruction or perforation had occurred"
  - closest text in source: "Most patients (79%) successfully completed treatment and no treatment failure occurred, however adverse events (21%) and mortality (13%) among TB cases were high"
- `PMID:19240705` *(abstract only)*: "have overlapping clinical, radiological, endoscopic and histological characteristics"
  - closest text in source: "Different radiological, endoscopic, and pathological similarities and features that can aid the clinician in reaching a rapid diagnosis are reviewed as well"
- `PMC:PMC3211607` *(abstract only)*: "independently associated with higher mortality"
  - closest text in source: "RESULTS: In the early group of 43 patients, the morbidity rate was 30%; mortality, 12%; and median hospital stay, 18.3 days (standard deviation [SD] 6.2 d)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0001678` (2 mentions) - the report calls it "given in the template"; MONDO calls it **intestinal tuberculosis**

### Terms the ontology service could not be reached for

1 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `DOID:404` (7 mentions)