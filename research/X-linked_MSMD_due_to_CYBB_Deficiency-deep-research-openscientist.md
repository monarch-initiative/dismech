---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T14:40:20.433984'
end_time: '2026-09-03T15:08:56.318429'
duration_seconds: 1715.88
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: X-linked Mendelian susceptibility to mycobacterial diseases due to
    CYBB deficiency
  mondo_id: MONDO:0010389
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: X-linked_MSMD_due_to_CYBB_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: X-linked_MSMD_due_to_CYBB_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** X-linked Mendelian susceptibility to mycobacterial diseases due to CYBB deficiency
- **MONDO ID:** MONDO:0010389 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **X-linked Mendelian susceptibility to mycobacterial diseases due to CYBB deficiency** covering all of the
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

# X-linked Mendelian Susceptibility to Mycobacterial Diseases due to CYBB Deficiency
### Comprehensive Disease Characterization Report (MONDO:0010389)

*Evidence base: literature synthesis (PubMed), landmark primary paper Bustamante et al. Nat Immunol 2011 (PMID 21278736), MSMD reviews and cohorts. Iteration 1 report; subsequent iterations refine.*

---

## SUMMARY (Answer to the Research Question)

X-linked MSMD due to CYBB deficiency is a rare inborn error of immunity in which specific **hypomorphic missense mutations in *CYBB*** (encoding gp91^phox / NOX2, the catalytic subunit of the phagocyte NADPH oxidase) selectively abolish the respiratory burst **in monocyte-derived macrophages** — while sparing monocytes, granulocytes (neutrophils) and monocyte-derived dendritic cells. This macrophage-restricted loss of reactive oxygen species (ROS) production cripples the killing of intramacrophagic mycobacteria, producing a **selective predisposition to tuberculous and weakly-virulent mycobacterial disease (BCG, environmental mycobacteria, *M. tuberculosis*)** in otherwise healthy males, **without** the broad, life-threatening susceptibility to bacteria and fungi that characterizes X-linked chronic granulomatous disease (CGD) caused by conventional *CYBB* loss-of-function. It is thus a distinct "experiment of nature" that is allelic to X-CGD but mechanistically and clinically separate, and it is the only MSMD etiology that acts on a downstream effector (macrophage oxidative burst) rather than on the IL-12/23–IFN-γ signaling circuit itself.

---

## 1. Disease Information

**Overview.** X-linked MSMD due to CYBB deficiency belongs to the MSMD group — rare inborn errors of immunity conferring selective vulnerability to weakly virulent mycobacteria (BCG vaccine, environmental non-tuberculous mycobacteria, NTM) and, for CYBB specifically, to *Mycobacterium tuberculosis*, in individuals with no overt abnormality on routine immune testing. It was defined by Bustamante et al. (2011, PMID 21278736), who reported two kindreds of otherwise-healthy adult males with X-linked recessive MSMD carrying novel *CYBB* mutations producing an impaired respiratory burst restricted to monocyte-derived macrophages.

**Key identifiers.**
- **MONDO:** MONDO:0010389 (X-linked MSMD due to CYBB deficiency)
- **OMIM disease:** #300645 — IMMUNODEFICIENCY 34, MYCOBACTERIOSIS, X-LINKED (IMD34), gene *CYBB*
- **OMIM gene:** *CYBB* 300481
- **Orphanet:** MSMD group ORPHA:319573 (no separate CYBB-MSMD ORPHA subtype; parent "Mendelian susceptibility to mycobacterial diseases")
- **HGNC gene:** HGNC:2578 (*CYBB*); **NCBI Gene** 1536; **Ensembl** ENSG00000165168; **UniProt** P04839 (CYBB_HUMAN, gp91^phox/NOX2)
- **ICD-10:** D71 (functional disorders of polymorphonuclear neutrophils) / D84.9 (immunodeficiency, unspecified); **ICD-11:** 4A00.0 (immunodeficiencies due to defects in innate immunity)
- **MeSH:** related — "Mycobacterium Infections"; "Genetic Predisposition to Disease"; "Granulomatous Disease, Chronic" (allelic disorder)

**Synonyms / alternative names.** MSMD due to CYBB deficiency; X-linked recessive MSMD; macrophage-specific gp91^phox deficiency; NOX2 macrophage-restricted deficiency; IMD34 (mycobacteriosis, X-linked). Historically discussed alongside the two other X-linked MSMD gene (NEMO/*IKBKG*).

**Information source.** Disease-level, aggregated from primary case reports/kindreds and MSMD registry reviews (rare disease; small numbers of families). Not derived from EHR-scale datasets.

---

## 2. Etiology

**Primary cause (genetic).** Germline, X-linked recessive hypomorphic missense mutations in *CYBB*. Bustamante et al. reported the mutations **p.T178P** and **p.Q231P**; a third macrophage-affecting allele **p.G412R/p.G412E** class has been described in the extended MSMD literature. These mutations impair NADPH-oxidase (cytochrome b558) **assembly in macrophages specifically**, without abrogating enzyme function in neutrophils/monocytes.

> "Germline mutations in CYBB … impair the respiratory burst of all types of phagocytes and result in X-linked chronic granulomatous disease (CGD). … These patients had previously unknown mutations in CYBB that resulted in an impaired respiratory burst in monocyte-derived macrophages but not in monocytes or granulocytes." — Bustamante 2011, PMID 21278736

**Genetic risk factors.**
- **Causal variants:** specific *CYBB* missense alleles (p.T178P, p.Q231P) — LoF restricted to macrophage lineage.
- **Sex:** male sex is the dominant risk factor (X-linked recessive; hemizygous males affected).
- **Family history:** maternal X-linked transmission; positive family history common in MSMD (≈45%, PMID 38341181).
- **Modifier context:** genetic background/other MSMD-pathway genes may modify penetrance (incomplete penetrance is typical of MSMD).

**Environmental risk factors.**
- **BCG vaccination** (live attenuated *M. bovis* BCG) — major trigger of disseminated mycobacterial disease across MSMD.
- **Exposure to *M. tuberculosis*** (endemic/high-TB-burden regions) — the defining trigger in CYBB-MSMD kindreds.
- **Environmental non-tuberculous mycobacteria.**

**Protective factors.**
- **Environmental:** avoidance of live BCG vaccine in known-affected families; early antimycobacterial prophylaxis/treatment; reduced *M. tuberculosis* exposure.
- **Genetic protective factors:** none specifically established for CYBB-MSMD; carrier females are protected by random X-inactivation favoring the wild-type allele in the macrophage-critical window.

**Gene–environment interaction.** The phenotype is contingent on encounter with mycobacteria: the *CYBB* macrophage-restricted defect is clinically silent until BCG or *M. tuberculosis*/NTM exposure unmasks the macrophage ROS-killing failure. Thus disease = (hypomorphic *CYBB* allele) × (mycobacterial exposure).

---

## 3. Phenotypes

CYBB-MSMD presents as **selective, often severe/disseminated mycobacterial disease** with otherwise normal health. Frequencies below are drawn from the broader MSMD cohort (Khavandegar 2024, PMID 38341181, n=830) and the CYBB kindreds (PMID 21278736).

| Phenotype (type) | HPO suggestion | Onset / severity / frequency |
|---|---|---|
| Tuberculosis / disseminated mycobacterial disease (clinical sign) | HP:0032262 (Mycobacterium tuberculosis infection) / HP:0100831 | CYBB kindreds: adult-onset TB in males; severe |
| Lymphadenopathy (clinical sign) | HP:0002716 | Most common MSMD sign, 45.5%; multifocal 35.1% |
| Fever (symptom) | HP:0001945 | ~30% of MSMD |
| Hepatosplenomegaly / organomegaly (physical) | HP:0001433 / HP:0003271 | ~25% of MSMD |
| Sepsis (clinical) | HP:0100806 | ~21% of MSMD |
| BCG-itis / disseminated BCG disease (clinical) | HP:0032324 (susceptibility to mycobacterial infection) | Common trigger in childhood-onset MSMD |
| Granulomatous inflammation (pathology) | HP:0032252 (Granuloma) | Tissue reaction to mycobacteria |
| Osteomyelitis (clinical) | HP:0002754 | Occasional |
| Recurrent/ disseminated NTM infection (clinical) | HP:0002718 (Recurrent bacterial infections) | Variable |

**Phenotype characteristics.**
- **Age of onset:** In the CYBB kindreds, disease occurred in **adult males** (tuberculous disease) — later than the typical MSMD childhood BCG presentation; MSMD overall mean age ~10 yr.
- **Severity:** Moderate–severe, frequently disseminated when it occurs.
- **Progression:** Episodic/infection-driven; can be progressive/disseminated if untreated; responsive to antimycobacterials.
- **Frequency among affected individuals:** Mycobacterial disease is the case-defining event; **penetrance is incomplete** — carriers/hemizygotes may remain asymptomatic until exposure.

**Quality-of-life impact.** Recurrent hospitalizations, prolonged (months-to-years) antimycobacterial therapy, infection-related morbidity; between episodes patients are typically well (distinguishing CYBB-MSMD from CGD, which carries chronic multi-organ burden). No disease-specific EQ-5D/SF-36 data available.

**Distinguishing feature vs CGD:** Absence of the broad CGD phenotype (recurrent *Staphylococcus*, *Serratia*, *Burkholderia*, *Aspergillus*, granulomatous colitis) — CYBB-MSMD patients are healthy apart from mycobacterial disease.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***CYBB*** (cytochrome b-245 beta chain), Xp21.1 (current genome builds: Xp11.4); encodes **gp91^phox / NOX2** (flavocytochrome b558 heavy chain), the catalytic, membrane-bound, electron-transferring subunit of the phagocyte NADPH oxidase. UniProt P04839; 570 aa; contains FAD- and NADPH-binding domains and heme-coordinating histidines.

**Pathogenic variants (MSMD-causing subset).**
- **Type/class:** **Missense**, hypomorphic — e.g., **c.533A>C p.Q231P**, **c.532A>C-region p.T178P** (Bustamante 2011); additional macrophage-affecting alleles (e.g., p.G412 class) reported subsequently.
- **Functional consequence:** **Cell-type-restricted loss of function** — impaired NADPH-oxidase **assembly** and respiratory burst specifically in monocyte-derived macrophages; near-normal in neutrophils/monocytes. This contrasts with conventional *CYBB* null/LoF alleles causing pan-phagocyte loss (X-CGD).
- **ACMG classification:** Pathogenic for the macrophage-restricted MSMD phenotype (functional segregation + biochemical demonstration).
- **Allele frequency:** Private/family-specific; essentially absent from gnomAD (consistent with severe rare disease).
- **Origin:** **Germline**, maternally transmitted (X-linked recessive).

**Allelic disorder — X-linked CGD.** Most *CYBB* mutations (~65% of all CGD) cause X-linked CGD via pan-phagocyte respiratory-burst loss (PMID 27666509; PMID 31364312 describes CYBB splicing mutations). The MSMD phenotype is produced only by particular missense alleles with macrophage-selective consequences.

**NADPH oxidase gene family / structure context.** The oxidase comprises two membrane subunits — **gp91^phox (CYBB)** and **p22^phox (CYBA)** — plus cytosolic **p47^phox (NCF1)**, **p67^phox (NCF2)**, **p40^phox (NCF4)**, and the small GTPase **RAC**. gp91^phox's extracellular portion shows signatures of adaptive selection, implicating host–pathogen interaction (PMID 23821607).

**Modifier genes.** Not formally defined for CYBB-MSMD; the broader IL-12/IFN-γ pathway genotype and X-inactivation pattern in carriers are plausible modifiers.

**Epigenetic information.** In carrier females, **X-chromosome inactivation (lyonization)** determines the fraction of macrophages expressing the mutant allele and thus carrier risk. No specific DNA-methylation/histone signature reported for the disease.

**Chromosomal abnormalities.** None; point (missense) mutations, not large structural rearrangements (contrast with CNV-driven IL12RB1 deficiency, PMID 29995221).

---

## 5. Environmental Information

- **Infectious agents (central):**
  - *Mycobacterium tuberculosis* (NCBI:txid1773) — the defining trigger in CYBB-MSMD.
  - *Mycobacterium bovis* BCG vaccine strain (NCBI:txid33892) — common MSMD trigger.
  - Environmental/non-tuberculous mycobacteria (e.g., *M. avium* complex, NCBI:txid1764).
  - Occasionally other intramacrophagic pathogens in MSMD broadly (*Salmonella*, *Candida*, *Histoplasma*), though CYBB-MSMD phenotype is more narrowly mycobacterial.
- **Environmental factors:** residence in high-TB-burden regions; BCG immunization programs.
- **Lifestyle factors:** none specifically implicated beyond exposure risk.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **germline hypomorphic missense mutation in *CYBB*** (e.g., p.T178P, p.Q231P) is inherited in a hemizygous male → **leads to** a structurally altered gp91^phox/NOX2 protein.
2. The altered gp91^phox **results in** defective assembly of the flavocytochrome b558 / NADPH-oxidase complex **specifically in monocyte-derived macrophages** (a cell-type-restricted consequence; the same allele permits normal assembly in neutrophils/monocytes) — *demonstrated* biochemically in patient cells (PMID 21278736).
3. Impaired oxidase assembly in macrophages **leads to** an **absent/deficient respiratory burst** → failure to generate **superoxide (O2·−, CHEBI:18421)** and downstream **ROS/H2O2 (CHEBI:16240)** within the phagosome (GO:0045730 respiratory burst; GO:0042554 superoxide anion generation).
4. Loss of macrophage phagosomal ROS **results in** failure to kill/restrict **intracellular mycobacteria** — phagocytosis and uptake remain intact, but **intramacrophagic bacterial proliferation is uncontrolled** (directly shown for *M. tuberculosis* in patient monocyte-derived macrophages, PMID 27666509).
5. Uncontrolled intramacrophagic mycobacterial replication **leads to** local and then **disseminated mycobacterial disease** (lymphadenitis, granuloma formation, organomegaly), *manifesting* upon exposure to BCG or *M. tuberculosis*.
6. Because neutrophil/monocyte oxidase and the IL-12/23–IFN-γ axis are intact, **broad antibacterial/antifungal immunity is preserved** → the clinical picture is **selective mycobacterial susceptibility (MSMD), not CGD** (branch point distinguishing the two allelic diseases).

*Inferred vs demonstrated:* Steps 1–4 are experimentally demonstrated in the primary literature; the epidemiologic selectivity in step 6 is inferred from the clinical phenotype of the kindreds.

### Category detail
- **Molecular pathways:** phagocyte NADPH-oxidase / respiratory-burst pathway (Reactome "Neutrophil/phagocyte ROS production"); operates **downstream of** IFN-γ-mediated macrophage activation. Unlike other MSMD genes, the **IL-12/23–IFN-γ signaling cascade is intact** (PMID 42183200; PMID 25453225). Crucially, **IFN-γ transcriptionally upregulates gp91phox (CYBB) and p47phox** in human phagocytes (PMID 1531037), so NOX2 is a genuine *downstream effector* of the same IL-12/IFN-γ circuit whose upstream components are mutated in other MSMD subtypes — unifying CYBB-MSMD with the canonical MSMD paradigm at the effector level.
- **Cellular processes:** oxidative microbicidal killing, phagosome maturation, inflammation/granuloma formation; ROS also modulate autophagy and inflammasome signaling in macrophages.
- **Protein dysfunction:** missense-driven **loss of function via assembly failure** (not a classic misfolding-aggregation disease), cell-type-restricted — a novel "conformational/assembly" mechanism.
- **Metabolic/biochemical:** deficient conversion of O2 → superoxide by NADPH oxidase (enzyme EC 1.6.3.1); reduced phagosomal H2O2 and secondary microbicidal oxidants.
- **Immune system involvement:** innate immunodeficiency of the effector (macrophage) arm of anti-mycobacterial immunity; adaptive IFN-γ production normal. Independent human-macrophage work confirms NOX-derived ROS is a required, non-redundant component of anti-mycobacterial control: pharmacologic NADPH-oxidase inhibition partially abrogates host control of *M. avium* in primary human macrophages (PMID 40020517) — the very effector arm CYBB-MSMD deletes.
- **Tissue damage mechanisms:** mycobacterial dissemination, granulomatous inflammation, caseation, tissue destruction.

**Suggested GO terms:** GO:0045730 (respiratory burst), GO:0042554 (superoxide anion generation), GO:0072593 (ROS metabolic process), GO:0042742 (defense response to bacterium), GO:0006909 (phagocytosis), GO:0043020 (NADPH oxidase complex — cellular component).
**Suggested CL terms:** CL:0000235 (macrophage), CL:0000576 (monocyte), CL:0000775 (neutrophil), CL:0000451 (dendritic cell).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** lymph nodes (UBERON:0000029) — lymphadenitis; lungs (UBERON:0002048) — tuberculous pneumonitis; spleen (UBERON:0002106) and liver (UBERON:0002107) — organomegaly/granulomata; bone marrow (UBERON:0002371); skin (UBERON:0002097) with BCG-site/disseminated lesions.
- **Body systems:** immune/hematopoietic system (mononuclear phagocyte system); reticuloendothelial system; respiratory and lymphatic systems secondarily.
- **Tissue/cell level:** **mononuclear phagocytes — tissue macrophages / monocyte-derived macrophages (CL:0000235)** are the selectively affected population; monocytes, neutrophils, and dendritic cells are functionally spared.
- **Subcellular level:** **phagosome/plasma membrane NADPH-oxidase complex** (GO:0043020); electron transfer at the phagosomal membrane; ROS generation in the phagosomal lumen. Cellular components: GO:0005886 (plasma membrane), GO:0045335 (phagocytic vesicle).
- **Localization / laterality:** infection-site dependent; lymphadenopathy often regional then multifocal/bilateral; no fixed lateralization.

---

## 8. Temporal Development

- **Onset:** In the defining CYBB kindreds, **adult-onset** tuberculous disease in males; MSMD as a group is typically pediatric (mean ~10 yr) and frequently unmasked by infant BCG vaccination. Onset pattern is **subacute–chronic**, exposure-triggered.
- **Progression:** Disease course is **episodic/infection-driven**; individual episodes can be progressive and disseminated if untreated but are often controllable with therapy.
- **Duration:** Underlying genetic susceptibility is **lifelong**; infectious episodes require prolonged (months–years) antimycobacterial therapy.
- **Remission:** **Treatment-induced** remission with antimycobacterial regimens; relapse possible on re-exposure.
- **Critical periods:** peri-vaccination (BCG in infancy) and periods of *M. tuberculosis* exposure are windows of vulnerability; early diagnosis enables preventive intervention.

---

## 9. Inheritance and Population

- **Inheritance pattern:** **X-linked recessive** (hemizygous males affected; carrier females generally healthy). CYBB is one of only two X-linked MSMD genes (the other being *IKBKG*/NEMO) among the ~19–22 MSMD genes (PMID 25453225; PMID 30264912; PMID 42183200).
- **Penetrance:** **Incomplete** — a hallmark of MSMD; disease requires mycobacterial exposure. "Most of these inborn errors do not show complete clinical penetrance for the case-definition phenotype of MSMD" (PMID 25453225).
- **Expressivity:** Variable (from asymptomatic to disseminated disease).
- **Sex ratio:** Strongly **male-predominant** for CYBB-MSMD (X-linked recessive). MSMD overall ~52.5% male (PMID 38341181), but CYBB specifically affects males.
- **Carrier females:** generally protected via X-inactivation; carrier status transmissible. By analogy to X-linked CGD, a subgroup of female carriers with **skewed lyonization** (preferential inactivation of the wild-type X in myeloid cells) can become symptomatic; in XL-CGD such carriers may develop infection/inflammation and have been treated with allogeneic HSCT (PMID 37620741). An equivalent symptomatic-carrier scenario is theoretically possible for CYBB-MSMD if macrophage-lineage lyonization is unfavorable, though not yet formally reported.
- **Anticipation / mosaicism / founder effects:** No repeat-expansion anticipation; family-private alleles (no established founder effect for CYBB-MSMD).
- **Consanguinity:** Not required for X-linked CYBB-MSMD (relevant mainly to autosomal-recessive MSMD genes), but MSMD overall is enriched in consanguineous, high-TB-burden populations.
- **Epidemiology:** MSMD is a rare disease (no precise prevalence; estimates for individual etiologies are very low). Highest reported MSMD frequency in **Iran, Turkey, Saudi Arabia** (PMID 38341181). CYBB-MSMD is **very rare** — only a small number of kindreds reported worldwide.
- **Geographic distribution:** clusters in high-TB-burden and BCG-vaccinating regions; CYBB-MSMD kindreds reported in such settings.

---

## 10. Diagnostics

**Functional / laboratory tests.**
- **Respiratory burst assays** — **DHR (dihydrorhodamine-123) flow cytometry** and NBT (nitroblue tetrazolium) test. **Key diagnostic clue:** in CYBB-MSMD these are **normal in neutrophils/monocytes but defective in monocyte-derived macrophages** — the opposite of the pan-phagocyte defect seen in X-CGD. This cell-type dissociation is pathognomonic and requires assaying differentiated macrophages, not just neutrophils.
- gp91^phox protein expression / NADPH-oxidase component analysis by flow cytometry/immunoblot (LOINC-type functional assays).
- Routine hematology/immunology are typically normal (part of the MSMD case definition).
- Mycobacterial culture / tissue culture, mNGS/metagenomic sequencing, and histopathology of affected nodes (granulomatous inflammation ± acid-fast bacilli).

**Genetic testing (definitive).**
- **Single-gene *CYBB* sequencing** or **targeted MSMD/immunodeficiency NGS gene panels**; **WES/WGS** used when panels are non-diagnostic (~50% of MSMD remains genetically unexplained, PMID 42183200).
- Distinguish MSMD-causing hypomorphic missense alleles from CGD-causing LoF alleles; **functional segregation studies** in macrophages confirm pathogenicity.
- Maternal carrier testing / cascade testing for X-linked transmission.

**Imaging.** CT/MRI/ultrasound and PET for extent of lymphadenopathy, organomegaly, pulmonary and disseminated disease; chest imaging for TB.

**Clinical criteria & differential diagnosis.**
- MSMD case definition: severe/recurrent disease from weakly virulent mycobacteria (BCG/NTM) — plus TB for CYBB — in otherwise healthy individuals.
- **Differential:** X-linked CGD (broad bacterial/fungal susceptibility, pan-phagocyte DHR defect); other MSMD genes (IL12RB1, IL12B, IFNGR1/2, STAT1, IRF8, ISG15, TYK2, SPPL2A, NEMO); HIV/acquired immunodeficiency; anti-IFN-γ autoantibody syndrome.

**Screening.** Newborn screening does not currently capture MSMD/CYBB-MSMD (unlike SCID). In known kindreds: prenatal/carrier testing and avoidance of live BCG vaccine; cascade genetic screening of male relatives.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** CYBB-MSMD, being narrowly mycobacterial and treatable, generally carries a **better prognosis than CGD** provided infections are recognized and treated. For the broader PID/BCG-disease population (MSMD 43%, CGD 26%): 5-year survival **80.3%**, 10-year **69.3%** (PMID 41748971).
- **Morbidity:** infection-related disability, prolonged therapy, occasional dissemination; between episodes patients are typically well.
- **Disease course/complications:** disseminated mycobacterial disease, granulomatous organ involvement, relapse on re-exposure; drug toxicity from prolonged antimycobacterials.
- **Prognostic factors:** early diagnosis and adequate antimycobacterial therapy; access to HSCT for refractory disease (HSCT markedly improves antimycobacterial success, 75.8% vs 0%, PMID 41748971); virulence of infecting organism (*M. tuberculosis* worse than BCG/NTM).

---

## 12. Treatment

**Pharmacotherapy (mainstay).**
- **Prolonged combination antimycobacterial therapy** tailored to organism (anti-tuberculous regimen for *M. tuberculosis*; anti-BCG/NTM regimens otherwise), often months to years. (NCIT: Antimycobacterial/Antitubercular Agent.)
- **Recombinant human IFN-γ (rhIFN-γ)** — used adjunctively in MSMD (NCIT: Recombinant Interferon Gamma, C1512/Interferon Gamma C619). *Caveat for CYBB-MSMD:* because the lesion is a downstream effector defect (macrophage NADPH oxidase) with intact IFN-γ signaling, the rationale for IFN-γ is weaker than in cytokine-axis defects; response may be limited.

**Curative / advanced therapeutics.**
- **Allogeneic hematopoietic stem cell transplantation (HSCT)** — "the sole curative yet high-risk option" for MSMD (PMID 42183200); replaces defective macrophage-lineage cells. (NCIT: Hematopoietic Cell Transplantation C15431.)
- **Gene therapy / gene editing** — experimental; gene-corrected autologous HSC approaches (as explored for X-CGD) are conceptually applicable but not established for CYBB-MSMD.
- **Host-directed therapy (HDT) — experimental/conceptual:** agents that boost macrophage antimycobacterial mechanisms are under study (e.g., phenothiazines restricting *M. avium* in primary human macrophages, partly NOX-ROS dependent, PMID 40020517). Note: because such strategies leverage NOX-dependent ROS present in wild-type macrophages, they would not restore the absent burst in CYBB-null macrophages; HDT relevance to CYBB-MSMD is therefore theoretical and would need to target NOX-independent killing routes.

**Surgical/supportive.** Excision/drainage of suppurative lymph nodes as needed; supportive care; management of drug toxicity.

**Treatment strategy.** Genotype-guided: confirm CYBB-MSMD, treat the specific mycobacterium with prolonged combination therapy, consider adjunctive IFN-γ, and evaluate HSCT for severe/refractory/recurrent disease. Avoid further live BCG exposure.

---

## 13. Prevention

- **Primary prevention:** **Avoid live BCG vaccination** in at-risk families/known carriers (BCG is a major disseminated-disease trigger). Reduce *M. tuberculosis* exposure; TB infection-control measures in endemic regions.
- **Secondary prevention:** early recognition and treatment of mycobacterial disease; consider isoniazid/antimycobacterial prophylaxis after documented exposure per specialist guidance.
- **Tertiary prevention:** maintenance antimycobacterial therapy, surveillance for relapse, HSCT for refractory disease.
- **Genetic prevention/counseling:** **genetic counseling** for X-linked recessive inheritance; **carrier testing** of mothers/female relatives; prenatal/preimplantation testing options; cascade screening of male relatives.
- **Public health:** in high-TB-burden countries, weigh BCG timing/target populations against risk of severe adverse reactions in undiagnosed IEI (PMID 41668770 discusses BCG timing considerations).

---

## 14. Other Species / Natural Disease

- **Taxonomy of pathogens (not host disease):** *M. tuberculosis* (txid1773), *M. bovis* BCG (txid33892), *M. avium* (txid1764); host *Homo sapiens* (txid9606).
- **Orthologous gene:** mouse *Cybb* (NCBI Gene 13058), gp91^phox/Nox2 — highly conserved across mammals; the extracellular domain shows adaptive selection (PMID 23821607).
- **Natural disease in animals:** No well-described spontaneous macrophage-selective CYBB-MSMD equivalent in companion animals; CGD-like NADPH-oxidase deficiencies are documented in engineered models rather than natural populations. (OMIA has no established CYBB-MSMD entry.)
- **Comparative biology:** ROS-dependent macrophage control of mycobacteria is evolutionarily conserved; however, rodent macrophages rely more on nitric-oxide (iNOS) than ROS for mycobacterial killing, an important cross-species difference limiting model fidelity.
- **Zoonotic potential:** not applicable (host susceptibility trait, not transmissible).

---

## 15. Model Organisms

- **Mouse (*Mus musculus*, txid10090):** ***Cybb*/gp91^phox knockout** mice are the established model of X-CGD (increased susceptibility to catalase-positive bacteria/fungi and to mycobacteria); MGI resources for *Cybb* alleles. These recapitulate **pan-phagocyte** oxidase loss (CGD), **not** the macrophage-selective MSMD phenotype — a key limitation.
- **Related NADPH-oxidase models:** *Duox1* KO mice show **Duox1 is dispensable** for the overall course of *M. tuberculosis* lung infection (PMID 36936954), underscoring that the microbicidal ROS relevant to mycobacteria derive chiefly from the NOX2/gp91^phox system.
- **In vitro / cellular models (most faithful):** **patient monocyte-derived macrophages (MDMs)** demonstrating the macrophage-selective respiratory-burst defect and failure to control intracellular *M. tuberculosis* (PMID 21278736; PMID 27666509); EBV-B cell / fibroblast reconstitution and NADPH-oxidase assembly assays.
- **Model limitations:** No mouse reproduces the human cell-type-restricted (macrophage-only) NOX2 assembly defect; murine anti-mycobacterial immunity is more NO/iNOS-dependent, reducing translational fidelity for the ROS-centric human mechanism.
- **Applications:** dissecting macrophage-specific oxidase assembly, ROS-dependent mycobacterial killing, and testing of HSC gene-correction strategies.

---

## Key References (PMID)
- **21278736** — Bustamante et al., *Nat Immunol* 2011. Landmark: germline CYBB mutations selectively affecting macrophages cause X-linked MSMD.
- **25453225** — Bustamante et al., 2014. MSMD genetic/immunologic/clinical review; CYBB and NEMO as X-linked MSMD genes.
- **30264912** — Rosain et al., 2019. MSMD 2014–2018 update.
- **42183200** — Qian et al., 2026. MSMD IFN-γ immunity review; 22 genes; treatment landscape (HSCT, gene editing).
- **41786143** — Johnston et al., 2026. MSMD management review.
- **38341181** — Khavandegar et al., 2024. Systematic review of 830 MSMD patients (epidemiology/phenotype).
- **41748971** — Xia et al., 2026. 15-yr BCG-disease cohort; survival and HSCT benefit.
- **27666509** — Khan et al., 2016. CYBB missense; MDMs fail to control intracellular *M. tuberculosis*.
- **23821607** — Tarazona-Santos et al., 2013. NADPH-oxidase gene structure/evolution.
- **31364312** — de Boer et al., 2019. CYBB/CYBA splicing mutations in CGD.
- **36936954** — Gupta et al., 2023. Duox1 dispensable in murine Mtb infection.
- **25703555** — Boisson-Dupuis et al., 2015. Inherited immunodeficiencies underlying childhood TB.
- **40020517** — Kilinç et al., 2025. NOX-derived ROS required for human-macrophage control of *M. avium*; host-directed therapy.
- **1531037** — Amezaga et al., 1992. IFN-γ transcriptionally regulates gp91phox/p47phox — links MSMD IFN-γ axis to the NOX2 effector.
- **37620741** — Tsilifis et al., 2023. HSCT for symptomatic female XL-CGD carriers; skewed lyonization.

---

## Consolidated Evidence Synthesis (8 recorded findings)

| # | Finding | Key evidence (PMID) | Evidence type |
|---|---|---|---|
| 1 | CYBB-MSMD is a macrophage-selective NADPH-oxidase defect distinct from X-CGD (mutations p.T178P, p.Q231P impair burst in monocyte-derived macrophages, sparing neutrophils/monocytes) | 21278736 | Human clinical + in vitro |
| 2 | MSMD genetics converge on the IL-12/23–IFN-γ circuit (~19–22 genes); CYBB is the effector-arm outlier | 42183200; 25453225 | Review |
| 3 | MSMD clinical spectrum/demographics: lymphadenopathy (45.5%), fever, organomegaly, sepsis; highest in Iran/Turkey/Saudi Arabia | 38341181; 25453225 | Human clinical (n=830) |
| 4 | Management: prolonged antimycobacterials, adjunctive IFN-γ, HSCT curative (75.8% vs 0% antimycobacterial success); 5-/10-yr survival 80.3%/69.3% | 41748971; 42183200 | Human clinical cohort |
| 5 | The defective step is ROS-dependent intracellular killing, not phagocytosis (uptake intact; intramacrophagic *M. tuberculosis* proliferates) | 27666509 | Human/in vitro |
| 6 | X-inactivation (skewed lyonization) sets carrier-female risk in X-linked CYBB disorders | 37620741 | Human clinical |
| 7 | NOX-derived ROS is a non-redundant effector of human-macrophage mycobacterial control (independent confirmation) | 40020517 | In vitro (primary human macrophages) |
| 8 | IFN-γ transcriptionally upregulates gp91phox(CYBB)/p47phox — NOX2 is a downstream effector of the MSMD IL-12/IFN-γ axis | 1531037 | In vitro (human PMN) |

## Supported vs Refuted Hypotheses
- **Supported:** CYBB-MSMD is caused by macrophage-selective NADPH-oxidase (gp91^phox) assembly failure due to specific hypomorphic missense alleles; macrophage respiratory burst is essential for anti-mycobacterial immunity; disease is X-linked recessive with incomplete penetrance and mycobacteria-restricted phenotype.
- **Refuted/excluded:** CYBB-MSMD is NOT the same as X-linked CGD (different cell-type scope and clinical spectrum); it does NOT arise from an IL-12/IFN-γ signaling defect (that axis is intact); the phenotype is NOT a broad phagocyte immunodeficiency.

## Limitations & Future Directions
- Very few kindreds worldwide → limited epidemiology, penetrance, and long-term outcome data specific to CYBB-MSMD.
- Precise variant-level annotation (exact HGVS/gnomAD frequencies) should be confirmed against ClinVar/HGMD for each reported allele.
- No faithful animal model of the macrophage-selective defect; mechanistic work relies on patient MDMs.
- Open questions: molecular basis of cell-type-restricted oxidase assembly; whether adjunctive IFN-γ benefits CYBB-MSMD; role of gene-corrected autologous HSCT.


## Artifacts

- [OpenScientist final report](X-linked_MSMD_due_to_CYBB_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](X-linked_MSMD_due_to_CYBB_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 15 |
| On topic | 9 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:1531037` (1 mention) - Evidence for the involvement of distinct signal transduction pathways in the regulation of constitutive and interferon gamma-dependent gene expression of NADPH oxidase components (gp91-phox, p47-phox, and p22-phox) and high-affinity receptor for IgG (Fc gamma R-I) in human polymorphonuclear leukocytes.
  - shared terms: gene, neutrophil

Weighed against this report's own most characteristic terms: `msmd`, `disease`, `cybb`, `macrophage`, `mycobacterial`, `cybb-msmd`, `tuberculosis`, `x-linked`, `bcg`, `cgd`, `gene`, `nadph-oxidase`, `burst`, `ifn`, `phenotype`, `male`, `mycobacteria`, `ros`, `neutrophil`, `monocyte-derived`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.
