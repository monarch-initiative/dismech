---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-09-21T10:09:05.519465'
end_time: '2026-09-21T10:09:08.891872'
duration_seconds: 3.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: IHH locus large 2q35 tandem duplication-associated polysyndactyly
    as reported in PMID 22234151, distinct from small enhancer duplications and KIF7-related
    acrocallosal syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    query_char_limit: 500
    paper_limit: 50
    snippet_limit: 20
    snippet_paper_limit: 50
    restrict_snippets_to_papers: false
    paper_fields: title,abstract,authors,year,url,venue,journal,tldr,publicationDate,citationCount,influentialCitationCount,externalIds
    publication_date_range: ''
    venues: ''
    inserted_before: ''
fell_back: true
requested_provider: claude_code
provider_attempts:
- provider: claude_code
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: asta
  succeeded: true
citation_count: 18
reference_validation:
  total_references: 33
  verified: 33
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 33
  on_topic: 9
  off_topic: 2
  off_topic_references:
  - PMID:38099104
  - DOI:10.4103/ijd.ijd_649_21
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 2
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - OMIM
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IHH locus large 2q35 tandem duplication-associated polysyndactyly as reported in PMID 22234151, distinct from small enhancer duplications and KIF7-related acrocallosal syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **IHH locus large 2q35 tandem duplication-associated polysyndactyly as reported in PMID 22234151, distinct from small enhancer duplications and KIF7-related acrocallosal syndrome** covering all of the
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

# Asta Literature Retrieval: Disease Characteristics Research Template Target Disease Disease Name: IHH locus large 2q35 tandem duplication-associ...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 18
- Snippets retrieved: 20

## Relevant Papers

### [1] Partial trisomy 2q33.3-q37.3 in a patient with an inverted duplicated neocentric marker chromosome
- Authors: Ruiyu Ma, Ying Peng, Yang-Hui Zhang, Yan Xia, Guizhi Tang et al.
- Year: 2015
- Venue: Molecular Cytogenetics
- URL: https://www.semanticscholar.org/paper/7e6c80b2e44da1f8d21199b9583461c3d6248db0
- DOI: 10.1186/s13039-015-0111-1
- Summary: The first case of a patient with partial trisomy 2q33.3-37.3 presenting an inverted duplicated neocentric marker chromosome is reported, to help further understanding the genotype/phenotype correlations of partial 2q3 duplication and exploring the relationship between neocentric sSMC and human diseases.
- Evidence snippets:
  - Snippet 1 (score: 0.673)
    > Genes are dosagesensitive and become defective by loss rather than by gain of function. Furthermore, we also noticed that the chromosome 2q35 duplication syndrome (OMIM:185900) was located within the duplication interval in our  patient. This syndrome is characterized by syndactyly type I and Philadelphia-type craniosynostosis. Klopocki et al. [34] identified a 59 kb microduplication at the IHH (OMIM:600726) locus on chromosome 2q35 and a minimum region of 9.1 kb region located 40 kb 5' of the IHH gene, in three families associated with variable degrees of syndactyly and craniosynostosis. Our patient carries this microduplication but does not have these characteristics, showing only mild facial dysmorphism and delayed psychomotor development. One reason may be because of the broader duplicated region which encompasses more genes and gene regulatory regions. A large fragment repeat of the gene regulatory region may act as a group affecting gene expression differently, by controlling the expression of genes either within the region or outside, therefore, resulting in different phenotypes. Moreover, this novel rearrangement may lead to chromatin changes, and the presence of the neocentromere in the marker chromosome may influence gene expression [35]. Finally, it is difficult to explain a clear genotype/phenotype correlation for the 2q3 duplication syndrome because of variable clinical situations and the ambiguous breakpoints. The specific pathogenesis remains to be explored with precise breakpoint position mapping and related functional studies.

### [2] Partial trisomy 2q33.3-q37.3 in a patient with an inverted duplicated neocentric marker chromosome
- Authors: Ruiyu Ma, Ying Peng, Yang-Hui Zhang, Yan Xia, Guizhi Tang et al.
- Year: 2015
- Venue: Molecular Cytogenetics
- URL: https://www.semanticscholar.org/paper/1c242a18aafd1e62656cee7e66209075ea0b3eaa
- DOI: 10.1186/s13039-015-0111-1
- PMID: 25774219
- PMCID: 4359772
- Citations: 7
- Summary: The first case of a patient with partial trisomy 2q33.3-37.3 presenting an inverted duplicated neocentric marker chromosome is reported, which will help further understanding the genotype/phenotype correlations of partial 2q3 duplication and exploring the relationship between neocentric sSMC and human diseases.
- Evidence snippets:
  - Snippet 1 (score: 0.672)
    > Genes are dosagesensitive and become defective by loss rather than by gain of function. Furthermore, we also noticed that the chromosome 2q35 duplication syndrome (OMIM:185900) was located within the duplication interval in our  patient. This syndrome is characterized by syndactyly type I and Philadelphia-type craniosynostosis. Klopocki et al. [34] identified a 59 kb microduplication at the IHH (OMIM:600726) locus on chromosome 2q35 and a minimum region of 9.1 kb region located 40 kb 5' of the IHH gene, in three families associated with variable degrees of syndactyly and craniosynostosis. Our patient carries this microduplication but does not have these characteristics, showing only mild facial dysmorphism and delayed psychomotor development. One reason may be because of the broader duplicated region which encompasses more genes and gene regulatory regions. A large fragment repeat of the gene regulatory region may act as a group affecting gene expression differently, by controlling the expression of genes either within the region or outside, therefore, resulting in different phenotypes. Moreover, this novel rearrangement may lead to chromatin changes, and the presence of the neocentromere in the marker chromosome may influence gene expression [35]. Finally, it is difficult to explain a clear genotype/phenotype correlation for the 2q3 duplication syndrome because of variable clinical situations and the ambiguous breakpoints. The specific pathogenesis remains to be explored with precise breakpoint position mapping and related functional studies.

### [3] A multidisciplinary review of triphalangeal thumb
- Authors: Jacob W. P. Potuijt, R. Galjaard, P. J. van der Spek, C. V. van Nieuwenhoven, N. Ahituv et al.
- Year: 2018
- Venue: The Journal of Hand Surgery, European Volume
- URL: https://www.semanticscholar.org/paper/d708ce3869c3ee3fc96f1e4c71c86b13d80bcdd6
- DOI: 10.1177/1753193418803521
- PMID: 30318985
- PMCID: 6297887
- Citations: 21
- Influential citations: 2
- Summary: A review that summarizes a number of scientifically relevant topics that involve the triphalangeal thumb phenotype can lead to a better understanding of the pathogenesis and molecular mechanisms of this condition as well as other congenital upper limb anomalies.
- Evidence snippets:
  - Snippet 1 (score: 0.641)
    > Compared with point mutations in the ZRS, genomic duplications overlapping the ZRS lead to more severe phenotypes such as TPT-PS, Haas-Type Polysyndactyly and Laurin-Sandrow Syndrome (LSS). It has been suggested that duplications smaller than 80 kb cause LSS and mutations larger than 80 kb result in TPT-PS and Haas-type polysyndactyly (Lohan et al., 2014). Although the duplication size and severity of the phenotype are clearly correlated, these three phenotypes cannot be typed as single entities as these different phenotypes are observed in families with the same duplication size (Table 2). Therefore, these three phenotypes should be viewed in a gradual spectrum of phenotypic expression associated with duplications of the ZRS rather than different phenotypic entities caused by different sizes of genomic duplications.
    > The mechanism by which duplications of the ZRS occur and that result in severe TPT-phenotypes remains unknown. One theory could be that genomic duplications affect the dose sensitivity of regulatory elements as shown in other loci like Indian Hedgehog (IHH) (Will et al., 2017). Another known feature of genomic duplications is their ability to rearrange the three-dimensional chromatin architecture of the genome (Franke et al., 2016). Considering the severity of the phenotypes of TPT-PS, Haas-type Polysyndactyly and LSS, the ability of genomic duplications to disrupt the boundary of the topological associated domain (TAD) of SHH and LMBR1 can be regarded as a valid hypothesis. These duplications can disrupt the entire chromosomal architecture and leads to difficulties in the folding of regulatory elements towards SHH, which is required for appropriate gene regulation (Lupianez et al., 2016).

### [4] A genome-wide mutational constraint map quantified from variation in 76,156 human genomes
- Authors: Siwei Chen, L. Francioli, J. Goodrich, Ryan L. Collins, Qingbo S Wang et al.
- Year: 2022
- Venue: bioRxiv
- URL: https://www.semanticscholar.org/paper/b5d7cbe080e748d2fa2abb8fe68f928b2845b884
- DOI: 10.1101/2022.03.20.485034
- Citations: 260
- Influential citations: 46
- Summary: It is demonstrated that this genome-wide constraint map provides an effective approach for characterizing the non-coding genome and improving the identification and interpretation of functional human genetic variation.
- Evidence snippets:
  - Snippet 1 (score: 0.633)
    > c, CNVs at the IHH locus associated with synpolydactyly and craniosynostosis. The four implicated duplications (grey bars) overlap in a ~10kb region that exhibit high non-coding constraint (blue), with the highest Z score coinciding with the major IHH enhancers (dark blue). Each blue bar shows the constraint Z score of a 1kb window within the locus; gaps indicate windows removed by quality filters.

### [5] Disruptions of Topological Chromatin Domains Cause Pathogenic Rewiring of Gene-Enhancer Interactions
- Authors: D. Lupiáñez, K. Kraft, V. Heinrich, P. Krawitz, F. Brancati et al.
- Year: 2015
- Venue: Cell
- URL: https://www.semanticscholar.org/paper/183d2e4d4d1dbe2905f336b726a8a6be9dc21090
- DOI: 10.1016/j.cell.2015.04.004
- PMID: 25959774
- PMCID: 4791538
- Citations: 1986
- Influential citations: 63
- Summary: The results demonstrate the functional importance of TADs for orchestrating gene expression via genome architecture and indicate criteria for predicting the pathogenicity of human structural variants, particularly in non-coding regions of the human genome.
- Evidence snippets:
  - Snippet 1 (score: 0.622)
    > its genetic cause remained unknown (Camera et al., 1995;Thiele et al., 2004). We used whole-exome sequencing to detect mutations in genes located in the linkage interval but were not able to identify any potentially pathogenic changes. To search for non-coding mutations and structural variations, we used whole-genome sequencing. We detected a 1.1-Mb heterozygous inversion in family F1 and a 1.4-Mb heterozygous duplication, arranged in direct tandem orientation, in family F2. The telomeric breakpoints were located 1.4 Mb away from the EPHA4 gene within the gene desert in the case of the inversion and 1.2 Mb in the case of the duplication. The centromeric breakpoints were located centromeric and telomeric of WNT6 in the duplication and inversion, respectively ( Figure 1C). Of note, both rearrangements bring the centromeric portion of the EPHA4-containing TAD into close proximity of the WNT6 gene.
    > Third, we studied a family that carries a heterozygous 900-kb duplication in chromosomal region 2q35 that results in severe polysyndactyly and craniofacial abnormalities (Figure 1D) (Yuksel-Apak et al., 2012). The phenotype is reminiscent of the doublefoot (Dbf) mouse mutant, which also features massive polysyndactyly and was shown to be caused by a 600-kb deletion affecting the same region (Babbs et al., 2008). Of note, both the human and the mouse alleles bring the IHH/Ihh gene in proximity to the centromeric portion of the EPHA4-containing TAD.
    > Chromatin Interaction Landscape of the Extended WNT6/IHH/EPHA4/PAX3 Region To elucidate the genetic basis of these birth defects, we sought to examine the regulatory landscape at this locus in more detail. In addition to EPHA4, we focused on the IHH, WNT6, and PAX3 genes due to their location near breakpoints in patients and their involvement in other developmental processes (Geetha-Loganathan et al., 2010;Goulding et al.,

### [6] Chromatin Insulators and Topological Domains: Adding New Dimensions to 3D Genome Architecture
- Authors: Navneet Matharu, S. H. Ahanger
- Year: 2015
- Venue: Genes
- URL: https://www.semanticscholar.org/paper/100bc95489221fca74e85e85b2f89af3c2b573d8
- DOI: 10.3390/genes6030790
- PMID: 26340639
- PMCID: 4584330
- Citations: 20
- Influential citations: 1
- Summary: The classical view and the renewed understanding of insulators as global genome organizers are discussed and the plasticity of chromatin structure and its re-organization during pluripotency and differentiation and in situations of cellular stress are discussed.
- Evidence snippets:
  - Snippet 1 (score: 0.621)
    > A recent study demonstrated how structural anomalies in the genome could disrupt TAD organization and result in at least three related human genetic disorders [56]. Three different types of limb malformations, namely brachydactyly (short digits), F-syndrome syndactyly (fused axial digits), and polysyndactyly (duplicated and fused digits), identified in three different families, were investigated. By performing comparative genomic hybridization (CGH), the above mentioned malformations were shown to be associated with genomic aberrations in the q arm of chromosome 2, having four important coding genes, WNT6, IHH, EPHA4, and PAX3. Investigating the TAD organization of the locus revealed that it is structurally divided into three independent TADs, PAX3-TAD, EPHA4-TAD, and WNT6/IHH-TAD (Figure 2a). The brachydactyly family has a deletion that encompasses portions of EPHA4-TAD as well as the boundary separating it from PAX3-TAD (Figure 2b). The F-syndrome family has inversions or duplication having breakpoints within WNT6/IHH TAD and EPHA4-TAD, encompassing the TAD boundary between these two (Figure 2c). The polysyndactyly family has duplications and deletions within WNT6/IHH TAD, also disturbing its TAD boundary (Figure 2d). All these chromosomal aberrations were re-engineered in a mouse model using the CRSIPR/Cas9 system as well as in hESC (human embryonic stem cells) to map genomic interactions using 4C. The gene expression profile of the locus revealed non-cognate association of the gene promoter with the enhancers. These severe limb malformations clearly resulted from perturbations in the TAD structure and its boundaries, which relocate enhancers with gene promoters. These TAD boundaries are associated with CTCF-loop domains in mouse limbs. This study provides strong evidence that disruption of TADs and TAD boundaries could cause severe developmental disorders in humans. Deciphering the structural basis of X-inactivation in Caenorhabditis elegans also revealed the importance of TAD boundaries.

### [7] Utility of Optical Genome Mapping for Accurate Detection and Fine-Mapping of Structural Variants in Elusive Rare Diseases
- Authors: C. Orellana, M. Roselló, A. Sanchís, L. Pedrola, Carla Martín-Grau et al.
- Year: 2025
- Venue: International Journal of Molecular Sciences
- URL: https://www.semanticscholar.org/paper/5677116ff9ce9b9e7051b0a51695013dfe86da78
- DOI: 10.3390/ijms26031244
- PMID: 39941010
- PMCID: 11818634
- Citations: 5
- Summary: Optical genome mapping is utilized to investigate two patients with RDs whose genetic etiology remained unresolved despite prior genomic analyses, highlighting OGM’s efficacy in identifying complex SVs and underline novel pathogenic mechanisms in rare genetic disorders.
- Evidence snippets:
  - Snippet 1 (score: 0.610)
    > OGM demonstrates high sensitivity for low-frequency alterations, simplifies the interpretation of complex alterations, and operates independently of coverage or sequencing challenges associated with arrays and NGS. This renders OGM a valuable tool, especially for analyzing mosaics and SVs that are difficult to identify with other technologies. Although the deletion does not directly affect the IHH gene, it alters the genomic organization, potentially leading to ectopic interactions between enhancers and promoters, and causing aberrant gene expression patterns as previously suggested (Figure 2c). A very similar deletion in the nearby distal region of the IHH gene was identified in the Doublefoot (Dbf) mouse model [11]. This mutant mouse displays phenotypic features very similar to our Patient 2, including preaxial polydactyly with 6-9 triphalangeal digits on all four limbs, tibial hypoplasia, widened skull, hydrocephalus, and thickened curled tail. In humans, another comparable case was a female fetus with a microdeletion overlapping that of Patient 2, where the centromeric breakpoint is located 429 base pairs downstream of the transcription start site of the IHH gene [12] (Figure 2d). Clinical findings included, among other malformations, extensive polydactyly, with eight fingers on each hand with a mirror image of the right hand, seven fingers on the left foot and six fingers on the right foot with an enlarged hallux. Additionally, there is a remarkable clinical resemblance between Patient 2 and other individuals presenting features similar to acrocallosal syndrome. This individual exhibited extensive polysyndactyly of the hands and feet, craniofacial abnormalities including macrocephaly, agenesis of the corpus callosum, dysplastic and low-set ears, severe hypertelorism, and profound psychomotor delay caused by a large duplication involving the IHH locus [10] (Figure 2d).
  - Snippet 2 (score: 0.603)
    > This individual exhibited extensive polysyndactyly of the hands and feet, craniofacial abnormalities including macrocephaly, agenesis of the corpus callosum, dysplastic and low-set ears, severe hypertelorism, and profound psychomotor delay caused by a large duplication involving the IHH locus [10] (Figure 2d).
    > Although haploinsufficiency of some of the genes contained in the deletion may partially contribute to the phenotype in the patient, none of them have been directly linked to polydactyly nor do they show constraint scores suggestive of being haploinsufficient (LOEUF < 0.3), and hence to be sensitive to heterozygous deletions [17]. Notably, the proximal breakpoint of the deletion in Patient 2 is located very close to the IHH gene. This gene encodes a member of the Hedgehog protein family, essential secreted signaling molecules that regulate a variety of developmental processes including growth, pattern formation and morphogenesis. The protein encoded by the IHH gene plays a specific role in bone growth and differentiation. Mutations in this gene are the cause of brachydactyly type A1, characterized by shortened or malformed fingers and toes, and acrocapitofemoral dysplasia. Furthermore, Lupiañez et al. [18], using CRISPR/Cas genome editing and expression studies in mouse limb tissue and patient-derived fibroblasts, demonstrated that disruption of TADs (Topologically Associated Domains) can rewire long-range regulatory architecture and result in pathogenic phenotypes. Their study revealed that distinct human limb malformations are caused by deletions, inversions or duplications altering the structure of the TAD-spanning WNT6/IHH/EPHA4/PAX3 locus. Several disease-relevant structural changes cause ectopic interactions between promoters and non-coding DNA, and a cluster of limb enhancers normally associated with EPHA4 is misplaced relative to TAD boundaries and drives ectopic limb expression of another gene in the locus. This rewiring occurred only when the variant disrupted a CTCF-associated boundary domain.
  - Snippet 3 (score: 0.571)
    > C > A; p.(Ser102 Tyr) in the BHLHA9 gene, which was ruled out as causative after familial segregation analysis.
    > OGM study identified a mosaic heterozygous 682 kb deletion of the chromosomal region 2q35 (ogm[GRCh38] 2q35(219132322_219826404) x1), involving 30 different genes (NHEJ1, SLC23A3, CNPPD1, RETREG2, ZFAND2B, ABCB6, ATG9A, ANKZF1, GLB1L, STK16, TUBA4A, TUBA4B, DNAJB2, PTPRN, MIR153-1, RESP18, DNPEP, DNPEP-AS1, DES, SPEG, SPEGNB, GMPPA, ASIC4, CHPF, TMEM198, MIR3132, OBSL1, INHA, STK11IP, and SLC4A3) (Figure 2a). This mosaic alteration, with a variant allelic frequency of 0.27, had remained undetected in all previous genetic analysis, including genomic array studies. However, a posterior visual inspection of the region in the array confirmed a slight decrease in the signal intensity for all probes in the affected region, without reaching the threshold value established by the manufacturer for variant calling (Figure 2b). This deletion is not reported in the population control databases (DGV). It should be noted that one of the breakpoints of the deleted region is located very close to the IHH gene (Indian Hedgehog). This deletion was considered as pathogenic on evidence from similar deletions or duplications near the IHH gene that have been previously associated with a highly similar phenotype.

### [8] DB2: a probabilistic approach for accurate detection of tandem duplication breakpoints using paired-end reads
- Authors: Gökhan Yavas, M. Koyutürk, Meetha P. Gould, S. Mcmahon, T. LaFramboise
- Year: 2014
- Venue: BMC Genomics
- URL: https://www.semanticscholar.org/paper/278b026ea09b068002c2c538bd4ed4df54ff10a6
- DOI: 10.1186/1471-2164-15-175
- PMID: 24597945
- PMCID: 4234483
- Citations: 7
- Summary: This paper proposes a new method, Distribution Based detection of Duplication Boundaries (DB2), for accurate detection of tandem duplication breakpoints, an important class of structural variation, with high precision and recall, and demonstrates its efficacy using both simulated paired-end reads and newly discovered tandem duplications.
- Evidence snippets:
  - Snippet 1 (score: 0.602)
    > Structural variation is a class of genetic variation that includes insertions, inversions, translocations, deletions, and duplications of segments of DNA. Tandem duplications are serially repeated segments of the human genome which may have repeat units several hundred kilobases in size. Many studies have implicated tandem duplications in a variety of diseases. In one such study [1], it was shown that a subset of ovarian cancers share a marked tandem duplication phenotype with triple-negative breast cancers. An internal tandem duplication of the FLT3 gene (FLT3/ITD) is recurrent in acute myeloid leukemia (AML) and myelodysplastic syndrome (MDS) with frequencies of 20 and 3-15%, respectively [2,3]. Additionally, 5% to 10% of patients with AML possess the rearrangement of the mixed-lineage leukemia (MLL, also known as ALL1 or HRX) gene as the result of a partial tandem duplication (PTD) [4]. Germline tandem duplications have also been associated with human disease. In one recent study [5], it was shown that a patient and his half-sister with extensive polysyndactyly of the hands and feet, and craniofacial abnormalities carried identical 900-kb tandem duplications of the Indian hedgehog (IHH) locus. Another study [6] reported a father and daughter, both with a history of compulsive over-eating in childhood, carrying a small tandem duplication within exon 1 of the SNURF/SNRPN gene on chromosome 15. These studies underscore the need for computational methods for identifying tandem duplications.
    > Next-generation sequencing (NGS) technology was first used to detect structural variations by Korbel et al. [7]. In that study, the paired-end sequences of two samples' genomes were generated and the read pairs with discordant paired-end orientation and mapped distance were used to find basic structural variations. Subsequently, [8] used NGS to discover genome rearrangements in tumor DNA.

### [9] The Clinical and Genetic Characteristics in Children with Idiopathic Hypogonadotropin Hypogonadism
- Authors: Qiong Zhou, Wenbin Sheng, Suhong Yang, Chaochun Zou
- Year: 2022
- Venue: Journal of Oncology
- URL: https://www.semanticscholar.org/paper/265c800a4b85da460a7a5fc948bd4d0399c76f56
- DOI: 10.1155/2022/7973726
- PMID: 36245975
- PMCID: 9553531
- Citations: 5
- Summary: Investigating the characteristics of various IHH-associated genes and the correlation between IHH genes and phenotype concluded that variations in the studied genes could lead to the IHH.
- Evidence snippets:
  - Snippet 1 (score: 0.597)
    > Abnormalities in CHD7, PROKR2, ANOS1, FGFR1, SEMA3A, or NDNF genes can lead to IHH, with or without extragenital manifestations.IHH should be highly suspected in males with small penises and/or cryptorchidism.New 6 reported variants and 10 new variants (5 genes, including entire duplicates of ANSO1) were identified in IHH with different symptoms.A small proportion of patients may be affected by oligogenic inheritance.For CHD7 variants, the RSV of P or LP is more commonly associated with CHARGE syndrome.These findings provide more references and suggestions for the diagnosis and research of IHH.

### [10] Cloning, expression, and chromosomal location of SHH and IHH: two human homologues of the Drosophila segment polarity gene hedgehog.
- Authors: Valeria Marigo, D. Roberts, Scott M. K. Lee, O. Tsukurov, T. Levi et al.
- Year: 1995
- Venue: Genomics
- URL: https://www.semanticscholar.org/paper/e28d997446b03523effdd3e03dcc255eb3ddc8b2
- DOI: 10.1006/GENO.1995.1104
- PMID: 7590746
- Citations: 222
- Influential citations: 8
- Summary: The hedgehog genes encode signaling molecules that play a role in regulating embryonic morphogenesis and have cloned and sequenced human cDNA copies of two of these genes, SHH and IHH, which are expressed in adult kidney and liver.
- Evidence snippets:
  - Snippet 1 (score: 0.595)
    > The hedgehog genes encode signaling molecules that play a role in regulating embryonic morphogenesis. We have cloned and sequenced human cDNA copies of two of these genes, SHH and IHH. The SHH clone includes the full coding sequence and encodes a protein 92.4% identical to its murine homologue. The IHH clone is 89% complete and encodes a protein 94.6% identical to its murine homologue. IHH is expressed in adult kidney and liver. SHH expression was not detected in adult tissues examined; however, it is expressed in fetal intestine, liver, lung, and kidney. SHH mapped to chromosome 7q and IHH to chromosome 2 by PCR with DNA from a panel of rodent-human somatic cell hybrids. To identify the chromosomal location of SHH more precisely, a P1 genomic clone of SHH was isolated. This phage contained a CA repeat sequence tagged site that was used to map SHH relative to a polysyndactyly disease locus, using DNA prepared from affected and unaffected members of a large pedigree. SHH is closely linked, but distinct from the polysyndactyly disease locus at 7q36 (maximum lod score = 4.82, theta = 0.05) tightly linked to the EN2 locus. The murine homologues Shh, Ihh, and Dhh were mapped using (C57BL/6J x Mus spretus)F1 x C57BL/6J interspecific backcross. Shh mapped to a position 0.6 cM distal to En2 and 1.9 cM proximal to Il6 on mouse chromosome 5. This location is closely linked but distinct from the murine limb mutation Hx and syntenic to human chromosome 7q36.

### [11] Enhancers and chromatin structures: regulatory hubs in gene expression and diseases
- Authors: Zhen-Hua Hu, Wee-Wei Tee
- Year: 2017
- Venue: Bioscience Reports
- URL: https://www.semanticscholar.org/paper/0904a1b89195c3ab266af9411c1654c7e3b5ee88
- DOI: 10.1042/BSR20160183
- PMID: 28351896
- PMCID: 5408663
- Citations: 64
- Summary: It is emphasized that the enhancer–promoter interaction landscape provides a critical context to understand the aetiologies and mechanisms behind numerous complex human diseases and provides new avenues for effective transcription-based interventions.
- Evidence snippets:
  - Snippet 1 (score: 0.579)
    > that by limiting enhancer access to a small but privileged group of pioneer TFs, tighter control on tissue-specific gene expression may be achieved [52]. An extra TAD, due to the genomic duplication of the IHH locus and its associated TAD border (blue), leads to polydactyly. In contrast, brachydactyly is caused by a genomic deletion across the TAD border separating the EPHA4 and PAX3 loci (red and green respectively), resulting in the dysregulation of PAX3 by an ectopic EPHA4 enhancer. Finally, a genomic inversion involving IHH locus (blue) and its neighbouring TAD (red) exposes IHH to toxic regulation by an EPHA4 enhancer, leading to F-syndrome.

### [12] Chromatin Conformation in Development and Disease
- Authors: Ilias Boltsis, F. Grosveld, G. Giraud, Petros Kolovos
- Year: 2021
- Venue: Frontiers in Cell and Developmental Biology
- URL: https://www.semanticscholar.org/paper/1b7f9b44ad0860b82d8159aa748d0502983cf68e
- DOI: 10.3389/fcell.2021.723859
- PMID: 34422840
- PMCID: 8371409
- Citations: 47
- Influential citations: 1
- Summary: New findings, which have linked chromatin conformation with development, differentiation and diseases and hypothesized on various models are discussed, while integrating all recent findings on how chromatin architecture affects gene expression during development, evolution and disease are integrated.
- Evidence snippets:
  - Snippet 1 (score: 0.572)
    > Wnt6/Epha4 locus F-syndrome An inversion at the Wnt6/Epha4 locus that misplaces the Epha4 enhancers near Wnt6 gene, causing its mis-expression in the developing limb bud (Lupiáñez et al., 2015;Kraft et al., 2019) Ihh/Epha4 locus Polydactyly Duplications of the previous enhancers and rearranging them in front of the Ihh gene induce overexpression of Ihh (Kraft et al., 2019) TFAP2A locus Branchio-oculofacial syndrome Inversion of the TFAP2A TAD resulted in lower TFAP2A expression due to the fact that the promoter was separated from its associated enhancers (Laugsch et al., 2019) Shh locus Digit syndactyly An inversion at the Shh locus places the Shh gene in a TAD together with a limb enhancer, that induces its activation (Lettice et al., 2011) MEF2C locus 5q14.3 microdeletion syndrome Patients with balanced MEF2C translocations have been shown to be affected by the separation of promoters from their associated enhancers. The influence of these translocations was confirmed in patient-derived LCLs, which showed lower MEF2C expression (Redin et al., 2017) GATA2 locus Acute myeloid leukemia sub-types A chromosomal inversion and translocation in chromosome 3 at two different breakpoints place the GATA2 enhancer in the same TAD as the EVI1 oncogene. The enhancer is then in close proximity with the EVI1 promoter triggering its activation, which is responsible for the development of the disease (Gröschel et al., 2014) IGF2 locus Colorectal cancer Recurrent tandem duplications encompassing a TAD boundary result into new interactions between IGF2 and a cell specific super-enhancer located in the adjacent TAD, leading to its > 250-fold overexpression (Weischenfeldt et al., 2017).

### [13] Unilateral Syndactyly, Hemihypertrophy, and Hyperpigmentation with Mosaic 2q35 Deletion
- Authors: Akhtar Ali, Ajeet Kumar, Pawan K. Dubey, Vivek Pandey, Ankur Singh
- Year: 2023
- Venue: Indian Journal of Dermatology
- URL: https://www.semanticscholar.org/paper/742cedaf776caac2e2dcec9c6fa46f943abc01ab
- DOI: 10.4103/ijd.ijd_649_21
- PMID: 38099104
- PMCID: 10718247
- Citations: 1
- Summary: This case of a 1-year-old child with a unique constellation of symptoms of unilateral syndactyly, hemihypertrophy, and skin hyperpigmentation is presented, and genetic study established the molecular basis of symptoms.
- Evidence snippets:
  - Snippet 1 (score: 0.569)
    > The size of this deletion lies between 4.5 and 5.5 MB. One of the important genes found in this deleted area is IHH (Indian Hedgehog Homolog). IHH gene-coded proteins play a role in bone growth and differentiation. Mutations in this gene are the cause of Brachydactyly type A1 which is characterized by malformations of toes and fingers. [16] Chromosomal abnormality in the mosaic state is a commonly observed genetic aberration in the largest  [5] Similar case of hemihypertrophy, syndactyly, and PM was reported in a 6-year-old male child having a normal karyotype performed on peripheral blood sample, although no karyotype from fibroblast culture was mentioned (Srinivas et al. 2015). [17] The present case and the one reported by Sriniwas et al. [17] showed extra-cutaneous manifestation of asymmetry of limbs and nonosseous syndactyly of third and fourth fingers of the right hand. Extracutaneous manifestations are common in PM. These involve mainly neurological deficits, learning disability, epilepsy, hypotonia, spasticity, of limbs, kyphoscoliosis, and syndactyly. [18] e present case highlights the importance of analyzing karyotype from the affected areas. This way, there is a high chance of detecting chromosomal aberration in such cases. The 2q35 deletion in the mosaic state has not been previously reported. The mosaic 2q35 deletion from the affected areas significantly correlates with the clinical manifestations in the present case.

### [14] A duplication on chromosome 16q12 affecting the IRXB gene cluster is associated with autosomal dominant cone dystrophy with early tritanopic color vision defect
- Authors: S. Kohl, Pablo Llavona, A. Sauer, Peggy Reuter, N. Weisschuh et al.
- Year: 2021
- Venue: Human Molecular Genetics
- URL: https://www.semanticscholar.org/paper/44349d6c9eed641a56ab4dd0622d69c51150b55f
- DOI: 10.1093/hmg/ddab117
- PMID: 33891002
- PMCID: 8212766
- Citations: 3
- Summary: It is proposed that the disease underlies a misregulation of the IRXB gene cluster on chromosome 16q12 and demonstrated that overexpression of Irx5a and Irx6a, the two orthologous genes in zebrafish, results in visual impairment in 5-day-old zebra fish larvae.
- Evidence snippets:
  - Snippet 1 (score: 0.562)
    > A single 9.5 kp duplication covering IRX6 alone was predicted from short read whole genome sequencing in an anamnestically healthy but anonymous Turkish male subject (28); if this patient truly does not have a retinal phenotype, this would rule out that the duplication of IRX6 alone is the cause of the disease in our patients but would favor the hypothesis that the duplications observed in our families result in a misregulation of part or the whole the IRXB cluster.
    > To the best of our knowledge no human disease has been associated with variants or aberrations of IRX6 or CNVs covering the SRO, whereas loss-of-function missense and small indel variant in IRX5 have been associated with autosomal recessive Hamamy syndrome (MIM 611174) characterized by craniofacial dysmorphology, osteopenia, severe myopia, hearing loss and mild intellectual disability (29)(30)(31). No such disease features were observed in our adCD families with duplications at the IRXB gene cluster, except for the high myopia in 5/16 subjects and the hearing difficulties in four subjects of family ZD3. Notably, we did not find any putative pathogenic point mutation in IRX5 and IRX6 in our cohort of unsolved adCD/adCRD patients, but in total four families with large overlapping duplications, suggesting that the disease mechanism underlying this form of adCD is linked to these duplications, and possibly an increase in gene dosage of genes located at this locus.
    > Interpreting the genomic and phenotypic consequences of CNVs can be challenging. Whereas deletion CNVs often lead to haploinsufficiency, duplications may cause disease through triplosensitivity, gene disruption or gene fusion at breakpoints (32). Actually, Newman and coworkers showed that most duplications are in tandem in direct orientation adjacent to the original locus (32), as it is also the case in all three independent duplications identified in this study.

### [15] Molecular Mechanisms of Syndromic Cryptorchidism: Data Synthesis of 50 Studies and Visualization of Gene-Disease Network
- Authors: Kristian Urh, Živa Kolenc, Majcen Hrovat, Luka Svet, P. Dovč et al.
- Year: 2018
- Venue: Frontiers in Endocrinology
- URL: https://www.semanticscholar.org/paper/6684afc5248469573171ca8770afef7c3ee8c77f
- DOI: 10.3389/fendo.2018.00425
- PMID: 30093884
- PMCID: 6070605
- Citations: 14
- Influential citations: 1
- Summary: To catalog published cases of syndromes which include cryptorchidism in the clinical picture and associated genomic information, data was extracted from Public/Publisher MEDLINE and Web of Science databases using the keywords including: syndrome, crypt orchidism, undescended testes, loci, and gene.
- Evidence snippets:
  - Snippet 1 (score: 0.561)
    > Data were retrieved from PubMed and WoS. Study types of obtained publications including relevant genomic information were performed using different study approaches including: case reports, association, and functional studies, genomewide and single locus studies, and different omics types. Syndromes that include cryptorchidism in clinical picture were reported to be associated with protein-coding genes and chromosomal mutations. Table 1 includes protein coding genes associated with syndromic cryptorchidism, which are alphabetically ordered by their locus names. Proteins, encoded by the genes listed include enzymes (BRCC3), hormones (AMH), transcription inhibitors (ANKRD11), inhibitors of enzymes (CDKN1C), transmembrane receptors (RET), and many other types and subtypes of regulatory proteins. Table 2 includes chromosomal mutations associated with syndromic cryptorchidism. Chromosomal mutations include microdeletions or microduplications, of various size ranging from 3.5 to 43.7 Mb. In some cases chromosomal mutations were associated with candidate genes, in total 8 possibly responsible for cryptorchidism phenotype. Each row in the catalog represents a genetic origin of a syndrome, containing gene or cytogenetic location of mutation, deletion or duplication, name of a syndrome, DOID (Disease ontology ID if available), reference of a publication in which the connection to cryptorchidism was proposed and PMID (PubMed ID) or OMIM ID. Chromosomal mutations are ordered by the chromosome number. The systematic approach enables future researchers to use this manually checked data in further studies more efficiently.

### [16] Whole-exome sequencing identifies a novel IHH insertion in an Ontario family with brachydactyly type A1
- Authors: Rosettia Ho, A. McIntyre, Brooke A. Kennedy, R. Hegele
- Year: 2018
- Venue: SAGE Open Medical Case Reports
- URL: https://www.semanticscholar.org/paper/d1addc655463b7b29e0be7e8c27d37ec7017e88e
- DOI: 10.1177/2050313X18818711
- PMID: 30574312
- PMCID: 6295682
- Citations: 6
- Summary: An Ontario family with mild brachydactyly is described in which whole-exome sequencing identified a novel variant for brachysylltely type A1, the first IHH in-frame insertion causingBrachydACTylytype A1.
- Evidence snippets:
  - Snippet 1 (score: 0.554)
    > We report an Ontario family with autosomal dominant BDA1, characterized by variably short stature and shortened digits. Ascertained 15 years ago, this case was left unsolved following Sanger sequencing of all known brachydactyly genes. With the recent use of whole-exome sequencing, it was found that affected family members carry a heterozygous in-frame insertion in IHH, designated c.285_287dupGAA, p.Glu95_ Asn96insLys, explaining their brachydactyly phenotype (Figures 1 and 2). This IHH variant is predicted to exert a damaging effect on protein function from multiple in silico prediction tools, co-segregates with disease status in the family, is considered novel in multiple control population databases, and has not been previously reported in the literature.
    > BDA1 results from causative mutations within the Indian hedgehog gene (IHH) [6][7][8] on chromosome 2q35-36. IHH encodes the IHH protein, a member of the hedgehog family of signalling proteins. Along with sonic and desert hedgehog, IHH regulates patterning processes in both vertebrate and invertebrate development. 9 The hedgehog family is involved in limb polarity and chondrogenesis, with IHH playing a critical role in human skeletal development. IHH mutations impair chondrocyte maturation and proliferation, with failure of osteoblast development in endochondral bones. 10 In Ihh -/- mice, the loss of IHH signalling leads to reduction defects in the forelimbs and digits. 11 Dominant mutations in IHH are causative of BDA1, while recessive mutations have been linked to acrocapitofemoral dysplasia, which features short stature, short limbs, and cone-shaped epiphyses. 12 everal other mutations in the IHH gene have been previously reported. All mutations responsible for BDA1 have been limited to the N-terminal active fragment of IHH. 5 These mutations have predominantly affected codon positions 95, 100, 131, and 154, with ours as no exception. 7,13,14

### [17] Ciliary Signalling and Mechanotransduction in the Pathophysiology of Craniosynostosis
- Authors: Federica Tiberio, O. Parolini, W. Lattanzi
- Year: 2021
- Venue: Genes
- URL: https://www.semanticscholar.org/paper/c9f23a073dfb3dcad742c654c47e1a826379fefd
- DOI: 10.3390/genes12071073
- PMID: 34356089
- PMCID: 8306115
- Citations: 14
- Summary: The implication of the primary cilium components and active signalling in CS pathophysiology is highlighted, dissecting their biological functions in craniofacial development and in suture biomechanics.
- Evidence snippets:
  - Snippet 1 (score: 0.552)
    > Genes implicated in the HH pathway cause different syndromic CS, classified as ciliopathies. These include, Joubert syndrome spectrum, typical ciliopathies with severe neurodevelopmental disorder, eye and kidney abnormalities, and a multiorgan involvement, has been extended to include midline CS, defining the Joubert syndrome 2. This is associated with homozygous mutations in the gene encoding the transmembrane protein 216 (TMEM216). TMEM216 is a membrane protein expressed at the ciliary base-TZ, as part of the tectonic-like complex, which regulates the HH pathway, is required for tissue-specific ciliogenesis and regulates ciliary membrane composition [99].
    > In the context of HH signalling, microduplications of the IHH gene locus on 2q35 have been found to segregate with the Syndactyly type 1 phenotype, unrelated multigeneration kindreds, featuring sagittal CS [100,101]. The critical duplicated region included a regulatory sequence upstream the gene, that was predicted to serve as a long-range enhancer of IHH, regulating its expression during bone formation, hence affecting digit and skull development [100].
    > A somatic mosaic mutation in the SMO receptor gene causes the Curry-Jones syndrome, a multisystem disorder characterised by brain malformations, unicoronal craniosynostosis, patchy skin lesions, polysyndactyly, iris colobomas, microphthalmia, and intestinal malrotation with myofibromas or hamartomas [102].
    > Heterozygous loss-of-function mutations of GLI3 cause the Greig Cephalopolysyndactyly syndrome, with a widely variable expressivity, in which digital malformations are associated with sagittal and metopic CS [103].

### [18] A 6.4MB duplication of the alpha-synuclein locus causing fronto-temporal dementia and parkinsonism - phenotype-genotype correlations
- Authors: E. Kara, A. Kiely, C. Proukakis, N. Giffin, S. Love et al.
- Year: 2014
- Venue: JAMA neurology
- URL: https://www.semanticscholar.org/paper/e2c848277efb207619a7999aaa38027404feb020
- DOI: 10.1001/jamaneurol.2014.994
- PMID: 25003242
- PMCID: 4362700
- Citations: 64
- Influential citations: 1
- Summary: Gender was significantly associated with both disease risk and severity; males compared to females had increased disease risk and severity and the corresponding odds ratios from the univariate analyses were 8.36 (1.97 to 35.42) and 5.55 (1.39 to 22.22) respectively.
- Evidence snippets:
  - Snippet 1 (score: 0.542)
    > Importance SNCA locus duplications are associated with variable clinical features and reduced penetrance but the reasons underlying this variability are unknown. Objective 1) To report a novel family carrying a heterozygous 6.4Mb duplication of the SNCA locus with an atypical clinical presentation strongly reminiscent of frontotemporal dementia (FTD) and late-onset pallidopyramidal syndromes. 2) To study phenotype-genotype correlations in SNCA locus duplications. Design, Setting, Participants and Data sources We report the clinical and neuropathologic features of a family carrying a 6.4Mb duplication of the SNCA locus. To identify candidate disease modifiers, we undertake a genetic analysis in the family and conduct statistical analysis on previously published cases carrying SNCA locus duplication using regression modelling with robust standard errors to account for clustering at the family level. Main outcome measures To assess whether length of the SNCA locus duplication influences disease penetrance and severity, and whether extra-duplication factors have a disease-modifying role. Results We identified a large 6.4Mb duplication of the SNCA locus in this family. Neuropathological analysis showed extensive α-synuclein pathology with minimal phospho-tau pathology. Genetic analysis showed an increased burden of PD-related risk factors and the disease-predisposing H1/H1 MAPT haplotype. Statistical analysis of previously published cases suggested that there is a trend towards increasing disease severity and disease penetrance with increasing duplication size. The corresponding odds ratios (95% CI) from the univariate analyses were 1.17 (0.81 to 1.68) and 1.34 (0.78 to 2.31) respectively. Gender was significantly associated with both disease risk and severity; males compared to females had increased disease risk and severity and the corresponding odds ratios (95% CI) from the univariate analyses were 8.36 (1.97 to 35.42) and 5.55 (1.39 to 22.22) respectively. Conclusions and relevance These findings further expand the phenotypic spectrum of SNCA locus duplications. Increased dosage of genes located within the duplicated region probably cannot increase disease risk and disease severity without the contribution of additional risk

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 33 |
| On topic | 9 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:38099104` (1 mention) - Unilateral Syndactyly, Hemihypertrophy, and Hyperpigmentation with Mosaic 2q35 Deletion.
  - shared terms: genetic, deletion
- `DOI:10.4103/ijd.ijd_649_21` (1 mention) - Unilateral Syndactyly, Hemihypertrophy, and Hyperpigmentation with Mosaic 2q35 Deletion
  - shared terms: genetic, deletion

Weighed against this report's own most characteristic terms: `snippet`, `gene`, `score`, `year`, `url`, `ihh`, `duplication`, `venue`, `locus`, `disease`, `associated`, `human`, `phenotype`, `genetic`, `mutation`, `syndrome`, `chromosome`, `deletion`, `genomic`, `patient`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 0 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

No term could be looked up either way, so nothing here was confirmed or contradicted.
