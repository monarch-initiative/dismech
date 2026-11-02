---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T23:34:02.641355'
end_time: '2026-10-31T00:15:44.368898'
duration_seconds: 2501.73
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Early-onset Lafora Body Disease
  mondo_id: MONDO:0014717
  category: Mendelian
  causal_genes: PRDM8
  omim_id: OMIM:616640
  synonyms: EPM10; epilepsy, progressive myoclonic, 10; epilepsy, progressive myoclonic,
    type 10
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
citation_count: 14
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 17
  quotes_valid: 16
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:34399803
  relevance_assessed: 14
  on_topic: 4
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 25
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Early-onset_Lafora_Body_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Early-onset_Lafora_Body_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Early-onset Lafora Body Disease
- **MONDO ID:** MONDO:0014717 (if available)
- **Causal gene(s):** PRDM8
- **OMIM:** OMIM:616640
- **Synonyms:** EPM10; epilepsy, progressive myoclonic, 10; epilepsy, progressive myoclonic, type 10
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Early-onset Lafora Body Disease** covering all of the
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

# Early-onset Lafora Body Disease (EPM10) — Comprehensive Disease Characterization Report

**Disease:** Early-onset Lafora body disease (progressive myoclonic epilepsy type 10, EPM10)
**Causal gene:** **PRDM8** (PR/SET domain 8)
**MONDO ID:** MONDO:0014717 · **OMIM:** 616640 · **Locus:** 4q21.21
**Inheritance:** Autosomal recessive · **Category:** Mendelian, ultra-rare

---

## Summary

**Early-onset Lafora body disease (EPM10) is an ultra-rare, autosomal-recessive progressive myoclonus epilepsy (PME) caused by biallelic mutations in *PRDM8*,** a PR/SET-domain histone-methyltransferase transcriptional co-repressor located at chromosome 4q21.21. The disease was defined in 2012 when Turnbull and colleagues mapped a new Lafora-body PME to 4q21.21, identified *PRDM8* as the causal gene, and characterized the relationship of its protein product with the glycogen-regulating proteins laforin and malin ([PMID: 22961547](https://pubmed.ncbi.nlm.nih.gov/22961547/)). To date, only **two families worldwide** have been reported — one Pakistani (index family) and one Iranian — both consanguineous, establishing the recessive inheritance and extreme rarity of the condition ([PMID: 35034233](https://pubmed.ncbi.nlm.nih.gov/35034233/)).

Clinically, EPM10 presents **earlier than classic Lafora disease** — around **age 5 years** — with the triad of **dysarthria, myoclonus, and ataxia**, later broadening to generalized epileptiform seizures, cognitive decline, and (in the Iranian family) spasticity that initially prompted a diagnosis of complicated hereditary spastic paraplegia. A key diagnostic distinction from classic Lafora disease is that **axillary skin biopsy for Lafora bodies was NEGATIVE in both PRDM8 families**, so genetic testing (homozygosity mapping plus exome sequencing) — not biopsy — is definitive. The index pathogenic variant, *PRDM8* c.473T>C (p.Leu158Pro), is a homozygous missense change currently classified in ClinVar as a **Variant of Uncertain Significance (VUS)**.

Mechanistically, PRDM8 sits at the intersection of two biology threads: (1) as an obligate co-repressor partner of the transcription factor BHLHE22 (Bhlhb5), it controls neuronal differentiation and circuit assembly (neocortical layer-4 neurons, telencephalic axon targeting, retinal rod bipolar cells), and (2) it physically interacts with laforin and malin, the glycogen-quality-control proteins mutated in classic Lafora disease. The downstream "Lafora-body"/polyglucosan component of EPM10 pathology is **inferred by analogy rather than demonstrated** (skin biopsies were negative). Because the evidence rests on two families and a VUS, EPM10/*PRDM8* is best regarded as a **limited-validity gene–disease relationship**. There is no disease-specific therapy; management is symptomatic with PME anti-seizure medications (valproate first-line; levetiracetam, clonazepam, perampanel, zonisamide as add-ons; carbamazepine, phenytoin, and lamotrigine avoided). Prognosis is extrapolated from classic Lafora disease, which is relentlessly progressive and fatal (median survival ~11 years).

---

## Key Findings

### F001 — PRDM8 is the causal gene; disease maps to 4q21.21; only two families reported

Early-onset Lafora body disease is caused by **biallelic *PRDM8* mutations** mapped to chromosome **4q21.21**. Turnbull et al. (2012) reported the condition as a *new* progressive myoclonus epilepsy associated with Lafora bodies, stating they "**report a new progressive myoclonus epilepsy associated with Lafora bodies, early-onset Lafora body disease, map its locus to chromosome 4q21.21, identify its gene and mutation and characterize the relationship of its gene product with laforin and malin**" ([PMID: 22961547](https://pubmed.ncbi.nlm.nih.gov/22961547/)). The disease received the designation **EPM10** (OMIM 616640; MONDO:0014717). A decade later, the second report confirmed rarity, noting that "**a mutation in PRDM8 has been reported only once in a Pakistani family affected with early-onset Lafora disease**" before describing the second (Iranian) family ([PMID: 35034233](https://pubmed.ncbi.nlm.nih.gov/35034233/)). Both families are consanguineous and show autosomal-recessive inheritance.

### F002 — Early childhood onset (~5 years) with dysarthria, myoclonus, and ataxia; broad PME phenotype

EPM10 presents earlier than classic Lafora disease. Turnbull et al. state directly: "**Early-onset Lafora body disease presents early, at 5 years, with dysarthria, myoclonus and ataxia**" ([PMID: 22961547](https://pubmed.ncbi.nlm.nih.gov/22961547/)). The ~5-year onset and early dysarthria distinguish EPM10 from classic Lafora disease, which typically begins in the teenage years. The second family further expanded the phenotype: two affected Iranian individuals were "**initially diagnosed as complicated hereditary spastic paraplegia (HSP)**" and underwent careful neurologic examination, with generalized epileptiform EEG discharges ([PMID: 35034233](https://pubmed.ncbi.nlm.nih.gov/35034233/)). Thus the phenotype spans dysarthria, myoclonus, ataxia, seizures, cognitive decline, and spasticity.

**Suggested HPO terms:** Myoclonus (HP:0001336); Progressive myoclonic epilepsy (HP:0007099); Dysarthria (HP:0001260); Ataxia (HP:0001251); Generalized tonic-clonic seizures (HP:0002069); Progressive neurologic deterioration/cognitive decline (HP:0002344); Spasticity (HP:0001257); Abnormal EEG with generalized epileptiform discharges (HP:0011198).

### F003 — PRDM8 is a PR/SET-domain transcriptional co-repressor partnering BHLHE22 (Bhlhb5)

PRDM8 functions as an obligate co-repressor of the transcription factor **BHLHE22/Bhlhb5**. Ross et al. (2012) showed "**the Olig-related transcription factor Bhlhb5 (also known as Bhlhe22) forms a repressor complex with the PR/SET domain protein, Prdm8**," and that "**mice lacking either Bhlhb5 or Prdm8 have strikingly similar cellular and behavioral phenotypes, including axonal mistargeting by neurons of the dorsal telencephalon and abnormal itch-like behavior**" ([PMID: 22284184](https://pubmed.ncbi.nlm.nih.gov/22284184/)). The complex represses target genes including **Cadherin-11**. Independently, Inoue et al. (2015) showed that "**the deletion of Prdm8 causes growth retardation and a reduced brain weight**," impairing development of upper-layer neocortical neurons ([PMID: 26283595](https://pubmed.ncbi.nlm.nih.gov/26283595/)). This establishes PRDM8's core role in neuronal differentiation and circuit assembly.

### F004 — Molecular identity and identifiers; interaction with laforin and malin

PRDM8 = **PR/SET domain 8**; **HGNC:13993**; **NCBI Gene 56978**; **Ensembl ENSG00000152784**; **UniProt Q9NQV8**; locus **4q21.21** (GRCh38 chr4:80,183,879–80,260,318, + strand); aliases **EPM10, KMT8D, PFM5**. It is a histone methyltransferase-family protein (a negative transcriptional regulator with an N-terminal SET domain and a double zinc-finger). Critically, the RefSeq annotation and Turnbull et al. note that the protein "**has been shown to interact with the phosphatase laforin and the ubiquitin ligase malin, which regulate glycogen construction in the cytoplasm**"; Turnbull et al. explicitly set out to "**characterize the relationship of its gene product with laforin and malin**" ([PMID: 22961547](https://pubmed.ncbi.nlm.nih.gov/22961547/)). **gnomAD constraint:** pLI = 0.999, LOEUF (oe_lof_upper) = 0.44, lof_z = 4.17 (observed 13 vs expected 46.5 LoF) — i.e., **strongly loss-of-function intolerant**; missense is not constrained (mis_z = −0.59). This heterozygous LoF-intolerance combined with recessive disease is consistent with hypomorphic (partial LoF) biallelic variants.

### F005 — Prognosis: fatal, median survival ~11 years (classic Lafora disease as closest analog)

No EPM10-specific survival data exist (both families were described in earlier disease stages). The closest natural-history analog is classic Lafora disease. Pondrelli et al. (2021), an individual-participant meta-analysis of 298 genetically confirmed cases, reported: "**Overall survival rates in 272 cases were 93% [95% CI 89–96] at 5 years, 62% [95% CI 54–69] at 10 years and 57% [95% CI 49–65] at 15 years. Median survival time was 11 years**" ([PMID: 34399803](https://pubmed.ncbi.nlm.nih.gov/34399803/)). Loss of autonomy reached 45% at 5 years and 75% at 10 years (median 6 years); Asian origin and onset <18 years were negative prognostic factors. A follow-up study found the "**NHLRC1 genotype PT/PT was associated with shorter survival [HR 2.88; 95% CI 1.23–6.78]**" ([PMID: 37658439](https://pubmed.ncbi.nlm.nih.gov/37658439/)), demonstrating genotype–prognosis correlation in Lafora disease.

### F006 — Diagnostics: skin biopsy Lafora-body NEGATIVE; genetics definitive; EEG and FDG-PET supportive

A hallmark diagnostic distinction of EPM10 is that **skin biopsy is negative for Lafora bodies in both families**: "**like the Pakistani family, the search for Lafora bodies in their skin biopsies was negative**" ([PMID: 35034233](https://pubmed.ncbi.nlm.nih.gov/35034233/)). This contrasts with classic Lafora disease, which "**can easily be confirmed by axillar skin biopsy with proof of Lafora bodies (polyglucosan aggregates) in the sweat duct cells**" ([PMID: 17304172](https://pubmed.ncbi.nlm.nih.gov/17304172/)). Because biopsy fails, **diagnosis relies on homozygosity mapping plus whole-exome sequencing**. Supportive investigations include EEG (generalized epileptiform discharges that may precede clinical seizures) and FDG-PET, which in Lafora-type PME "**revealed posterior hypometabolism, consistent with the well-known posterior impairment in this disease**" ([PMID: 20163446](https://pubmed.ncbi.nlm.nih.gov/20163446/)).

### F007 — Model-organism phenotypes: cortical layer-4 neurons, telencephalic axon targeting, retinal bipolar cells

*Prdm8*-knockout mice define the cell-type-specific consequences of PRDM8 loss. Komai et al. (2009) showed that Prdm8 expression "**became restricted predominantly to the rod bipolar cells when retinogenesis was completed**," as well as to cortical layer-4 neurons ([PMID: 19616129](https://pubmed.ncbi.nlm.nih.gov/19616129/)). Jung et al. (2015) found that "**By adulthood, rod bipolar (RB) and type 2 OFF-cone bipolar (CB) cells were nearly absent from Prdm8-null mice**," producing a non-progressive ERG b-wave deficit resembling incomplete congenital stationary night blindness, with PKCα/Prkca a putative PRDM8 target ([PMID: 26023183](https://pubmed.ncbi.nlm.nih.gov/26023183/)). Inoue et al. (2015) reported that "**the relative UL [upper layer] thickness, but not the thickness of the deep layer (DL), was significantly reduced in Prdm8 KO mice**" ([PMID: 26283595](https://pubmed.ncbi.nlm.nih.gov/26283595/)). Together with the axon-mistargeting and itch phenotypes shared with Bhlhb5-null mice ([PMID: 22284184](https://pubmed.ncbi.nlm.nih.gov/22284184/)), these establish PRDM8 as a master regulator of neuronal subtype identity.

**Suggested CL terms:** retinal rod bipolar cell (CL:0000751); OFF-bipolar cell (CL:0000749); amacrine cell (CL:0000561); neocortical layer-4 neuron / cortical interneuron.

### F008 — Experimental therapeutics target glycogen synthesis (GYS1-ASO) and drug repurposing (empagliflozin)

No EPM10/PRDM8-specific therapy exists; experimental strategies derive from classic Lafora disease and target the shared polyglucosan mechanism. Antisense-oligonucleotide knockdown of glycogen synthase 1 (Gys1-ASO), delivered intracerebroventricularly to Epm2a−/− and Epm2b−/− mice, provided proof of concept that "**an antisense oligonucleotide targeting the GYS1 mRNA could prevent, and halt progression of, this catastrophic epilepsy**" ([PMID: 33993268](https://pubmed.ncbi.nlm.nih.gov/33993268/)). In Epm2b−/− mice, "**the mice treated with Gys1-ASO exhibited decreased Gys1 protein levels, decreased glycogen aggregation, and reduced epileptiform discharges compared to untreated Epm2b−/− mice**" ([PMID: 37700152](https://pubmed.ncbi.nlm.nih.gov/37700152/)). A prospective pilot trial is repurposing the SGLT2 inhibitor **empagliflozin** in early/intermediate Lafora disease ([PMID: 40407475](https://pubmed.ncbi.nlm.nih.gov/40407475/)). Symptomatic PME pharmacotherapy follows standard guidance: "**Valproic acid is the drug of choice, except for PMEs due to mitochondrial diseases. Levetiracetam and clonazepam should be considered as the first add-on treatment**" ([PMID: 28799509](https://pubmed.ncbi.nlm.nih.gov/28799509/)); perampanel and zonisamide are also used; carbamazepine, phenytoin, and lamotrigine are avoided because they can aggravate myoclonus.

**Suggested NCIT terms:** Valproic Acid (C920); Levetiracetam (C29140); Clonazepam (C28936); Perampanel; Zonisamide (C47793); Antisense Oligonucleotide Therapy.

### F009 — Mechanistic causal chain: PRDM8 loss → dysregulated neuronal gene repression (+ inferred polyglucosan handling) → neurodegeneration/epilepsy

The proposed mechanism integrates human genetics with mouse/in-vitro inference. Its molecular core is that "**Bhlhb5 binds to sequence-specific DNA elements and then recruits Prdm8, which mediates the repression of target genes**" ([PMID: 22284184](https://pubmed.ncbi.nlm.nih.gov/22284184/)). The downstream Lafora-body component is inferred by analogy to classic Lafora disease, where overlong-branched insoluble glycogen "**precipitate[s] and accumulate[s] into Lafora bodies, which drive a neuroinflammatory response and neurodegeneration**" ([PMID: 33993268](https://pubmed.ncbi.nlm.nih.gov/33993268/)). See the Mechanistic Model section below for the full ordered chain.

### F010 — Inheritance and epidemiology: autosomal recessive, consanguinity-driven, ultra-rare

EPM10 is autosomal recessive. Both reported families are consanguineous and originate from the Middle East/South Asia (Pakistan — Turnbull 2012; Iran — Davarzani 2022), diagnosed via homozygosity mapping. The second report notes "**Both reported PRDM8-related families presented intra and inter-familial heterogeneity and they have originated from the M[iddle East/South Asia]**" ([PMID: 35034233](https://pubmed.ncbi.nlm.nih.gov/35034233/)). No prevalence or incidence estimate exists (fewer than ~5 affected individuals reported worldwide). gnomAD shows PRDM8 is strongly LoF-constrained (pLI 0.999), so biallelic null carriers are essentially absent in the general population, consistent with extreme rarity. No founder variant is established; each family carries a private homozygous variant.

### F011 — Other species and orthologs: highly conserved; no naturally occurring animal disease reported

PRDM8 is evolutionarily conserved (HomoloGene 129760) with orthologs in mouse (*Prdm8*, GeneID 77630), rat (305198), zebrafish (*prdm8*, 557162), *Xenopus tropicalis* (733976), dog (487823), cow (507890), rhesus macaque (696013), and chimpanzee (104001124). Jung et al. describe PRDM8 as "**a highly conserved transcription factor that is abundantly expressed in mouse retina**" ([PMID: 26023183](https://pubmed.ncbi.nlm.nih.gov/26023183/)). **No naturally occurring PRDM8/EPM10 disease has been reported in companion animals or wildlife** (OMIA has no PRDM8 entry). By contrast, classic Lafora disease occurs naturally in dogs (e.g., miniature wirehaired dachshunds, via an *NHLRC1* dodecamer repeat expansion). EPM10 disease knowledge derives entirely from laboratory *Prdm8*-knockout mice and the two human case reports.

### F012 — Pathogenic variant: homozygous missense p.Leu158Pro (c.473T>C); recessive hypomorphic; ClinVar VUS

ClinVar links **NM_001099403.2(PRDM8):c.473T>C (p.Leu158Pro)** to "Early-onset Lafora body disease" (the Turnbull 2012 Pakistani-family variant), currently classified as **Uncertain significance**. Turnbull et al. identified "**its gene and mutation**" in the index family ([PMID: 22961547](https://pubmed.ncbi.nlm.nih.gov/22961547/)); for the Iranian family, "**Linkage to chromosome 4 and a mutation in the PRDM8 gene were identified**" — a distinct private homozygous variant ([PMID: 35034233](https://pubmed.ncbi.nlm.nih.gov/35034233/)). The variant class is **missense** (not protein-truncating), **germline**, and **biallelic (homozygous by consanguinity)**. The functional consequence is interpreted as **partial loss of function (hypomorphic)** — consistent with gnomAD LoF-intolerance (pLI 0.999) yet recessive inheritance, since complete biallelic null may be more severe or embryonically affecting.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic hypomorphic *PRDM8* variants** (e.g., c.473T>C / p.Leu158Pro, homozygous by consanguinity) **reduce PRDM8 (PR/SET histone-methyltransferase, KMT8D) function.** *(demonstrated — human genetics)*
2. This **leads to loss of PRDM8–BHLHE22 (Bhlhb5) co-repressor activity**, resulting in **de-repression of target genes** (e.g., Cadherin-11, Prkca/PKCα) and failed epigenetic (H3K9-type) silencing. *(demonstrated in mouse/in-vitro; [PMID: 22284184](https://pubmed.ncbi.nlm.nih.gov/22284184/), [PMID: 26023183](https://pubmed.ncbi.nlm.nih.gov/26023183/))*
3. De-repression **results in abnormal neuronal differentiation and circuit assembly** — upper-layer/layer-4 neocortical neurons, telencephalic axon targeting, and retinal bipolar-cell identity. *(demonstrated in mouse; [PMID: 26283595](https://pubmed.ncbi.nlm.nih.gov/26283595/), [PMID: 19616129](https://pubmed.ncbi.nlm.nih.gov/19616129/))*
4. **Branch (inferred):** Because PRDM8 physically interacts with **laforin and malin**, its loss is **inferred to perturb the laforin–malin glycogen-quality-control axis**, leading to overlong-branched insoluble glycogen (polyglucosans) that would aggregate as **Lafora bodies**. *(inferred — skin biopsies in both human families were NEGATIVE for Lafora bodies; [PMID: 22961547](https://pubmed.ncbi.nlm.nih.gov/22961547/), [PMID: 35034233](https://pubmed.ncbi.nlm.nih.gov/35034233/))*
5. Polyglucosan/neuronal dysfunction **leads to a neuroinflammatory response (astrogliosis) and neurodegeneration.** *(inferred by analogy to EPM2A/EPM2B Lafora disease; [PMID: 33993268](https://pubmed.ncbi.nlm.nih.gov/33993268/))*
6. These **result in the clinical manifestations**: dysarthria, myoclonus, ataxia, generalized epileptiform seizures, cognitive decline, and spasticity. *(demonstrated — human clinical)*

```
   PRDM8 biallelic hypomorphic mutation (4q21.21)
                │
      ┌─────────┴───────────┐
      ▼                     ▼
 Loss of PRDM8–BHLHE22   Loss of PRDM8 interaction
 co-repression          with laforin / malin  (INFERRED)
      │                     │
      ▼                     ▼
 De-repression of      Perturbed glycogen
 target genes          quality control
 (Cadherin-11, PKCα)        │
      │                     ▼
      ▼              Overlong-branched insoluble
 Abnormal neuronal   glycogen → polyglucosans →
 differentiation /   "Lafora bodies"  (INFERRED;
 circuit assembly    skin biopsy NEGATIVE)
 (cortex L4, retina        │
  bipolar, axons)          ▼
      │              Neuroinflammation (astrogliosis),
      └────────┬─────  neurodegeneration
               ▼
   Dysarthria, myoclonus, ataxia, seizures,
   cognitive decline, spasticity (onset ~5 yr)
```

### Upstream vs downstream

- **Upstream (demonstrated):** PRDM8 loss → transcriptional de-repression → defective neuronal subtype specification.
- **Downstream (inferred):** polyglucosan accumulation → neuroinflammation → neurodegeneration → PME phenotype.
- The **central uncertainty** is whether EPM10 is primarily a *transcriptional/neurodevelopmental* disorder, a *glycogen-storage (polyglucosan)* disorder, or both. The negative skin biopsies argue that the classic peripheral polyglucosan phenotype is at least attenuated, favoring a larger contribution from the transcriptional/neurodevelopmental arm.

**Suggested GO terms:** negative regulation of transcription, DNA-templated (GO:0045892); histone methyltransferase activity (GO:0042054); regulation of neuron differentiation (GO:0045664); glycogen metabolic process (GO:0005977); cerebral cortex neuron differentiation (GO:0021895). **Subcellular (GO CC):** nucleus (GO:0005634); cytosol where laforin–malin act on glycogen (GO:0005829). **UBERON:** cerebral cortex (UBERON:0000956); retina (UBERON:0000966); dorsal telencephalon; brain (UBERON:0000955). **CHEBI:** glycogen (CHEBI:28087); glucose-6-phosphate (CHEBI:4170).

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|------|-----------------|---------------|----------|
| [22961547](https://pubmed.ncbi.nlm.nih.gov/22961547/) | *Early-onset Lafora body disease* (Turnbull 2012) | Human genetics (index family) | F001, F002, F004, F012 — gene mapping, onset, laforin/malin interaction, index variant |
| [35034233](https://pubmed.ncbi.nlm.nih.gov/35034233/) | *The second family affected with a PRDM8-related disease* (Davarzani 2022) | Human clinical/genetics | F001, F002, F006, F010, F012 — second family, phenotype expansion, negative biopsy, AR/consanguinity |
| [22284184](https://pubmed.ncbi.nlm.nih.gov/22284184/) | *Bhlhb5 and Prdm8 form a repressor complex* (Ross 2012) | Mouse / molecular | F003, F009 — co-repressor mechanism, shared KO phenotypes |
| [26283595](https://pubmed.ncbi.nlm.nih.gov/26283595/) | *Deletion of Prdm8 impairs upper-layer neocortical neurons* (Inoue 2015) | Mouse KO | F003, F007 — cortical layering, brain weight |
| [19616129](https://pubmed.ncbi.nlm.nih.gov/19616129/) | *Expression of Prdm8 in developing CNS* (Komai 2009) | Mouse expression | F007 — rod bipolar / layer-4 restriction |
| [26023183](https://pubmed.ncbi.nlm.nih.gov/26023183/) | *PRDM8 required for rod bipolar / OFF-cone survival* (Jung 2015) | Mouse KO | F007, F009, F011 — retinal phenotype, conservation |
| [34399803](https://pubmed.ncbi.nlm.nih.gov/34399803/) | *Natural history of Lafora disease* (Pondrelli 2021) | Human meta-analysis | F005 — survival analog |
| [37658439](https://pubmed.ncbi.nlm.nih.gov/37658439/) | *Prognostic value of variants in Lafora disease* (Pondrelli 2023) | Human meta-analysis | F005 — genotype–prognosis |
| [17304172](https://pubmed.ncbi.nlm.nih.gov/17304172/) | *Lafora's disease (EPM2)* | Review | F006 — biopsy contrast |
| [20163446](https://pubmed.ncbi.nlm.nih.gov/20163446/) | *Posterior glucose hypometabolism in Lafora disease* | Human imaging | F006 — FDG-PET |
| [33993268](https://pubmed.ncbi.nlm.nih.gov/33993268/) | *Gys1 antisense therapy rescues murine Lafora disease* (Ahonen 2021) | Mouse therapeutics | F008, F009 — GYS1-ASO, downstream chain |
| [37700152](https://pubmed.ncbi.nlm.nih.gov/37700152/) | *Gys1 antisense prevents aggregates* (Donohue 2023) | Mouse therapeutics | F008 — preclinical efficacy |
| [40407475](https://pubmed.ncbi.nlm.nih.gov/40407475/) | *Empagliflozin repurposing for Lafora disease* (d'Orsi 2025) | Clinical trial protocol | F008 — drug repurposing |
| [28799509](https://pubmed.ncbi.nlm.nih.gov/28799509/) | *Pharmacological treatment of PMEs* | Review | F008 — symptomatic drugs |

**How the evidence fits together:** The two human reports ([PMID: 22961547](https://pubmed.ncbi.nlm.nih.gov/22961547/), [PMID: 35034233](https://pubmed.ncbi.nlm.nih.gov/35034233/)) anchor the gene–disease relationship, clinical phenotype, inheritance, and the negative-biopsy diagnostic feature. The mouse literature ([PMID: 22284184](https://pubmed.ncbi.nlm.nih.gov/22284184/), [PMID: 26283595](https://pubmed.ncbi.nlm.nih.gov/26283595/), [PMID: 19616129](https://pubmed.ncbi.nlm.nih.gov/19616129/), [PMID: 26023183](https://pubmed.ncbi.nlm.nih.gov/26023183/)) supplies the demonstrated upstream mechanism (transcriptional co-repression → neuronal subtype specification). The classic-Lafora-disease literature supplies the *inferred* downstream mechanism and the prognosis/therapeutics by analogy, but — crucially — the **negative skin biopsies challenge a straightforward polyglucosan interpretation** and leave the Lafora-body arm unproven in EPM10.

---

## Supported and Refuted Hypotheses

No formal hypotheses were registered as supported/rejected during the investigation (this was a characterization task). However, the weight of evidence supports the following conclusions and tensions:

- **Supported:** *PRDM8* is the causal gene for EPM10 (two independent consanguineous families; concordant linkage/exome data).
- **Supported:** PRDM8 acts as a BHLHE22-partnered transcriptional co-repressor essential for neuronal differentiation (robust mouse genetics).
- **Partially supported / inferred:** The "Lafora-body"/polyglucosan mechanism — supported by documented PRDM8–laforin–malin interaction but **not** by tissue pathology (skin biopsies negative in both families).
- **Uncertain:** Pathogenicity of the index variant (ClinVar VUS); the gene–disease relationship is of **limited validity** by ClinGen-style criteria given only two families.

---

## Section-by-Section Characterization Summary

**1. Disease information:** Ultra-rare AR PME; EPM10; MONDO:0014717; OMIM 616640; synonyms EPM10, "epilepsy, progressive myoclonic, 10/type 10." Information is disease-level/aggregated from two published consanguineous families plus model-organism data (not EHR-derived).

**2. Etiology:** Monogenic — biallelic hypomorphic *PRDM8* variants. Principal risk factor is **consanguinity**. No environmental, infectious, protective, or gene–environment factors established.

**3. Phenotypes:** Myoclonus, dysarthria, ataxia (onset ~5 yr), generalized epileptiform seizures, cognitive decline, spasticity; progressive; severe QoL impact (loss of autonomy by analogy to Lafora disease).

**4. Genetic/molecular:** *PRDM8* (HGNC:13993; 4q21.21). Index variant c.473T>C/p.Leu158Pro (missense, germline, homozygous, ClinVar VUS). Second family: distinct private homozygous variant. LoF-intolerant (pLI 0.999). No modifier/epigenetic/chromosomal abnormalities established.

**5. Environmental:** None implicated beyond consanguinity (a population-genetic rather than environmental factor).

**6. Mechanism:** See ordered causal chain above — transcriptional de-repression (demonstrated) + inferred laforin/malin-axis polyglucosan handling → neurodegeneration/epilepsy.

**7. Anatomy:** Primary organ — brain (cerebral cortex, including layer-4 neurons; dorsal telencephalon); retina affected in mouse models; nervous system only. Subcellular: nucleus (transcription) and cytosol (glycogen/laforin–malin). Bilateral CNS involvement.

**8. Temporal development:** Pediatric onset (~5 yr), chronic-progressive course; relentless neurodegeneration; no remission; critical intervention window likely early (pre-aggregation), by analogy to GYS1-ASO timing.

**9. Inheritance/population:** AR; consanguinity-driven; ultra-rare (2 families, Pakistani and Iranian); no prevalence estimate; private variants (no founder effect); presumed complete penetrance in biallelic state.

**10. Diagnostics:** Genetic testing (homozygosity mapping + WES/WGS or PME gene panels) is definitive. **Skin biopsy for Lafora bodies is negative** (key distinction from classic LD). EEG shows generalized epileptiform discharges; FDG-PET shows posterior hypometabolism.

**11. Prognosis:** No EPM10-specific data; by analogy to Lafora disease — progressive, fatal, median survival ~11 years, early loss of autonomy.

**12. Treatment:** Symptomatic only — valproate (first-line), levetiracetam, clonazepam, perampanel, zonisamide; avoid carbamazepine/phenytoin/lamotrigine. Experimental (classic LD): GYS1-ASO, empagliflozin. No PRDM8-specific therapy.

**13. Prevention:** Genetic counseling for consanguineous families; carrier/cascade testing; prenatal/preimplantation diagnosis once a familial variant is known. No primary-prevention or vaccination strategy applicable.

**14. Other species:** PRDM8 highly conserved; orthologs across vertebrates; no natural animal disease (OMIA has no PRDM8 entry). Classic Lafora disease occurs naturally in dogs via *NHLRC1*.

**15. Model organisms:** *Prdm8*-knockout mouse is the principal model — recapitulates neurodevelopmental/retinal phenotypes (cortical layer-4 deficits, reduced brain weight, near-absent rod bipolar cells, axon mistargeting, itch behavior) but has **not** been shown to reproduce the human seizure/Lafora-body phenotype, a key limitation.

---

## Limitations and Knowledge Gaps

1. **Only two families worldwide** — the gene–disease relationship is of limited validity; penetrance, expressivity, and the full phenotypic spectrum are poorly defined.
2. **Index variant is a ClinVar VUS** (p.Leu158Pro); functional validation of pathogenicity is lacking.
3. **The core "Lafora-body" mechanism is inferred, not demonstrated** — skin biopsies were negative in both families, so whether EPM10 truly involves polyglucosan accumulation in brain remains unproven.
4. **No EPM10-specific natural history, survival, imaging, or biomarker data** — prognosis is entirely extrapolated from EPM2A/EPM2B Lafora disease.
5. **No *Prdm8* model recapitulating the human epilepsy phenotype** has been reported; existing KO phenotypes are neurodevelopmental/retinal.
6. **No disease-specific therapy; experimental therapeutics (GYS1-ASO, empagliflozin) target the EPM2A/EPM2B polyglucosan axis**, and their relevance to PRDM8 biology is assumed rather than established.
7. **Potential nosological ambiguity:** PRDM8 also appears as a candidate in other neurological contexts (e.g., ADCA-DN transcriptomics), so care is needed to keep EPM10 distinct.

---

## Proposed Follow-up Experiments / Actions

1. **Identify and phenotype additional families** via GeneMatcher/Matchmaker Exchange and PME gene-panel registries to strengthen the gene–disease validity and define penetrance/expressivity.
2. **Functionally validate p.Leu158Pro and the second family's variant** in vitro — assess PRDM8 repressor activity, BHLHE22 binding, and laforin/malin interaction — to move the ClinVar classification from VUS toward pathogenic/likely-pathogenic.
3. **Test brain tissue (autopsy or iPSC-derived neurons/organoids) for polyglucosan/Lafora-body accumulation** to directly confirm or refute the inferred glycogen-storage arm, given negative skin biopsies.
4. **Generate a Prdm8 knock-in mouse carrying the patient missense allele** (rather than full KO) and characterize for seizures, EEG, glycogen handling, and neurodegeneration to build a faithful disease model.
5. **Perform brain-focused glycogen/metabolic assays** (glycogen chain-length, phosphorylation, GYS1 activity) in PRDM8-deficient neurons to test whether the laforin–malin axis is perturbed.
6. **If the polyglucosan mechanism is confirmed, evaluate GYS1-ASO and empagliflozin** in the PRDM8 model to assess whether EPM2A/EPM2B therapeutic strategies translate to EPM10.
7. **Establish genetic-counseling and cascade-screening protocols** for affected consanguineous kindreds, including prenatal/PGD once the familial variant is validated.

---

*Report compiled from 12 confirmed findings and 35 reviewed papers over 5 iterations. Evidence types are distinguished throughout as human clinical/genetic, model-organism, in vitro, or computational/inferred.*


## Artifacts

- [OpenScientist final report](Early-onset_Lafora_Body_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Early-onset_Lafora_Body_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 17 |
| Quoted claims found in source | 16 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 14 |
| On topic | 4 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:34399803` *(abstract only)*: "**Overall survival rates in 272 cases were 93% [95% CI 89–96] at 5 years, 62% [95% CI 54–69] at 10 years and 57% [95% CI 49–65] at 15 years. Median survival time was 11 years**"
  - closest text in source: "Overall survival rates in 272 cases were 93% [95% CI 89-96] at 5 years, 62% [95% CI 54-69] at 10 years and 57% [95% CI 49-65] at 15 years"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |

24 of 25 terms resolved to a current term; the rest could not be looked up either way.