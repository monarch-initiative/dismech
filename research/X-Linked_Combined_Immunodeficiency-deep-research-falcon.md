---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-09T11:41:04.717077'
end_time: '2026-09-09T11:51:36.821226'
duration_seconds: 632.1
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: X-linked combined immunodeficiency (XCID, CIDX, moderate X-linked
    combined immunodeficiency, OMIM 312863), the attenuated hypomorphic IL2RG common-gamma-chain
    disorder described by Brooks et al 1990 and also called atypical or leaky X-linked
    SCID - not X-linked severe combined immunodeficiency SCIDX1 OMIM 300400
  mondo_id: MONDO:0010730
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 68
  verified: 63
  not_found: 1
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.016
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0010730
    reported_labels:
    - if available
    ontology_label: combined immunodeficiency, X-linked
  unresolved_terms:
  - HP:0005351
  unresolvable_prefixes:
  - Gene
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: X-Linked_Combined_Immunodeficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** X-linked combined immunodeficiency (XCID, CIDX, moderate X-linked combined immunodeficiency, OMIM 312863), the attenuated hypomorphic IL2RG common-gamma-chain disorder described by Brooks et al 1990 and also called atypical or leaky X-linked SCID - not X-linked severe combined immunodeficiency SCIDX1 OMIM 300400
- **MONDO ID:** MONDO:0010730 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **X-linked combined immunodeficiency (XCID, CIDX, moderate X-linked combined immunodeficiency, OMIM 312863), the attenuated hypomorphic IL2RG common-gamma-chain disorder described by Brooks et al 1990 and also called atypical or leaky X-linked SCID - not X-linked severe combined immunodeficiency SCIDX1 OMIM 300400** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** X-linked combined immunodeficiency (XCID, CIDX, moderate X-linked combined immunodeficiency, OMIM 312863), the attenuated hypomorphic IL2RG common-gamma-chain disorder described by Brooks et al 1990 and also called atypical or leaky X-linked SCID - not X-linked severe combined immunodeficiency SCIDX1 OMIM 300400
- **MONDO ID:** MONDO:0010730 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **X-linked combined immunodeficiency (XCID, CIDX, moderate X-linked combined immunodeficiency, OMIM 312863), the attenuated hypomorphic IL2RG common-gamma-chain disorder described by Brooks et al 1990 and also called atypical or leaky X-linked SCID - not X-linked severe combined immunodeficiency SCIDX1 OMIM 300400** covering all of the
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


# X-linked combined immunodeficiency due to hypomorphic **IL2RG**

## Scope and evidence standard

This report concerns the attenuated common-γ-chain disorder historically described as **X-linked combined immunodeficiency (XCID/CIDX), moderate X-linked combined immunodeficiency, atypical X-SCID, or leaky X-SCID**—not the usual null-allele **SCID-X1** phenotype catalogued as OMIM 300400. The distinction is functional: XCID retains allele-dependent IL2RG activity, thymopoiesis, or lineage-restricted activity through somatic reversion. It nevertheless belongs to the IL2RG disease continuum and can progress to life-threatening combined immunodeficiency.

Evidence is principally from individual patients and small families, not population cohorts. Percentages below therefore describe published cases and are vulnerable to referral and publication bias. PMID values could not be verified reliably in the retrieved full texts and are consequently not invented; DOI URLs and publication dates are supplied.

A compact knowledge-base summary precedes the detailed report.

| Domain | High-confidence finding | Suggested ontology IDs | Evidence caveat |
|---|---|---|---|
| Identity / scope | Attenuated **IL2RG** common-γ-chain disorder, variably called XCID, atypical X-SCID, or leaky X-SCID; residual γc function distinguishes it from classic, usually T−B+NK− SCID-X1. Requested identifier: **OMIM 312863**. | MONDO:0010730 **as requested** | OMIM/MONDO mapping should be manually verified because databases may merge this phenotype with SCID-X1 (OMIM 300400) or broader combined immunodeficiency. (tuovinen2020novelhemizygousil2rg pages 1-2, lim2019il2rghypomorphicmutation pages 1-2) |
| Causal gene | **IL2RG**, encoding interleukin-2 receptor subunit γ/common γ chain (CD132), is causal. | HGNC:6010; NCBI Gene:3561; ENSG00000147168 | Disease association is established, but “hypomorphic” requires phenotype and preferably functional confirmation rather than gene identity alone. (OpenTargets Search: X-linked combined immunodeficiency-IL2RG, arcasgarcia2020theil2rgr328x pages 1-2) |
| Inheritance | X-linked recessive germline disease: hemizygous males are predominantly affected; heterozygous mothers may be clinically asymptomatic carriers. | HP:0001419 | Rare symptomatic females could theoretically result from skewed X-inactivation or chromosomal abnormalities, but no disease-specific frequency is established. (hou2021somaticreversionof pages 5-6, gratz2024functionalcharacterizationof pages 21-26) |
| Core immunophenotype | Variable **T-low B+ NK+ or NK-low/−** phenotype; normal total lymphocyte counts do not exclude disease. Common findings include low CD4 cells, inverted CD4:CD8 ratio, low TRECs, skewed TCR repertoire, dysgammaglobulinemia, impaired proliferation, and reduced cytokine-induced STAT phosphorylation. | HP:0005403; HP:0002850; HP:0005351; HP:0004313 | No single immunophenotype is universal; residual function, age, and somatic reversion produce marked variability. (arcasgarcia2020theil2rgr328x pages 1-2, gratz2024functionalcharacterizationof pages 26-29, tuovinen2020novelhemizygousil2rg pages 9-10, hou2021somaticreversionof pages 6-11) |
| Hallmark clinical features | Recurrent sinopulmonary and opportunistic infections, chronic viral skin disease—especially warts/HPV and molluscum—bronchiectasis, diarrhea/enteropathy, candidiasis, failure to thrive, eczema or granulomatous inflammation, arthritis, and EBV-associated lymphoproliferation/lymphoma may occur. | HP:0002205; HP:0002110; HP:0032180; HP:0000960; HP:0002028; HP:0001508; HP:0000988; HP:0001369 | Frequencies derive mainly from small case series: among 29 literature cases, 97% had infections and 45% opportunistic infections; ascertainment bias is substantial. (arcasgarcia2020theil2rgr328x pages 1-2, lin2020progressivebcell pages 3-5, tuovinen2020novelhemizygousil2rg pages 9-10) |
| Molecular mechanism | Hypomorphic γc dysfunction partially impairs signaling by receptors for IL-2, IL-4, IL-7, IL-9, IL-15, and IL-21. Reduced γc surface localization or γc–JAK3 coupling leads to deficient JAK3/STAT5 signaling, impaired thymopoiesis and T/NK-cell proliferation, and defective T–B cooperation. | GO:0038110; GO:0042100; GO:0030217; GO:0001779; CL:0000084; CL:0000623; CL:0000624; CL:0000625 | Cytokine pathways are affected unequally by different alleles; alternative/JAK3-independent residual STAT5 activation has been demonstrated for p.Arg328Ter. (arcasgarcia2020theil2rgr328x pages 1-2, tuovinen2020novelhemizygousil2rg pages 1-2, lim2019il2rghypomorphicmutation pages 4-6) |
| Key variants | Documented hypomorphic alleles include **NM_000206.3:c.172C>T, p.(Pro58Ser)**; **c.455T>C, p.(Val152Ala)**; **c.458T>C, p.(Ile153Thr)**; **c.664C>T, p.(Arg222Cys)**; and **c.982C>T, p.(Arg328Ter)**. | Sequence Ontology: SO:0001583 (missense); SO:0001587 (stop-gained) | Transcript/version and ClinVar classifications must be checked variant by variant. p.Arg222Cys has produced both atypical and classic X-SCID, illustrating imperfect genotype–phenotype correlation. (arcasgarcia2020theil2rgr328x pages 1-2, lin2020progressivebcell pages 5-6, tuovinen2020novelhemizygousil2rg pages 9-10, hou2021somaticreversionof pages 6-11, tuovinen2020novelhemizygousil2rg pages 1-2) |
| Somatic reversion / modifier | Back mutation or compensatory second-site variation can selectively restore γc function in lymphoid clones, attenuating disease but causing mosaic, oligoclonal, or lineage-restricted immunity. | SO:0001777 (somatic variant); HP:0001442 (somatic mosaicism) | Reversion is not reliably protective: progressive B-cell loss, restricted TCR diversity, infection, and immune dysregulation can still occur. (lin2020progressivebcell pages 5-6, hou2021somaticreversionof pages 6-11, lin2020progressivebcell pages 8-9) |
| Diagnostics | Evaluate CBC/differential, lymphocyte subsets and naïve/memory populations, immunoglobulins and vaccine antibodies, mitogen/antigen proliferation, TRECs, TCR diversity, CD132 expression, and cytokine-induced STAT3/5/6 phosphorylation; confirm with **IL2RG** sequencing plus deletion/duplication analysis. Deep sequencing of sorted lineages can identify reversion. | HP:0031406; HP:0004313; NCIT:C171178 (next-generation sequencing) | CD132 expression may be normal despite dysfunctional signaling. WES/WGS or an IEI panel is useful when the presentation is atypical; CMA, karyotype, mtDNA, and repeat testing are not first-line absent another indication. (arcasgarcia2020theil2rgr328x pages 1-2, tuovinen2020novelhemizygousil2rg pages 1-2, hou2021somaticreversionof pages 6-11) |
| Screening | Newborn dried-blood-spot TREC screening can identify some leaky SCID cases; abnormal results require prompt flow cytometry and molecular evaluation. Cascade testing is indicated for maternal relatives. | HP:0031406; NCIT:C15644 (genetic testing) | Residual thymopoiesis can yield TRECs above program cutoffs, so newborn screening does **not** exclude hypomorphic IL2RG disease. (lim2019il2rghypomorphicmutation pages 1-2, hou2024challengeswithgene pages 10-14) |
| Management | Specialist immunology care; individualized immunoglobulin replacement, antimicrobial/Pneumocystis prophylaxis, rapid treatment of infections, avoidance of live vaccines when cellular immunity is inadequate, respiratory surveillance, and definitive consideration of allogeneic HSCT or investigational autologous IL2RG gene therapy. | NCIT:C15246 (hematopoietic stem-cell transplantation); NCIT:C16387 (gene therapy); NCIT:C15691 (immunoglobulin therapy) | Direct XCID treatment trials are lacking. HSCT and lentiviral-gene-therapy outcome estimates largely come from classic SCID-X1 and should not be assumed identical; early γ-retroviral therapy caused insertional leukemia. (blanco2020immunereconstitutionafter pages 1-2, blanco2020immunereconstitutionafter pages 2-3, lin2020progressivebcell pages 3-5) |
| Prognosis | Course ranges from survival into adulthood with recurrent infections to progressive lymphocyte loss, bronchiectasis, enteropathy, multiorgan granulomatous disease, malignancy, or death. Early recognition before irreversible infection or immune dysregulation is considered favorable. | HP:0002721; HP:0002110 | No XCID-specific survival curve or life-expectancy estimate exists. Somatic reversion and apparently mild childhood disease do not ensure long-term stability. (lin2020progressivebcell pages 3-5, lin2020progressivebcell pages 8-9) |
| Epidemiology | Extremely rare; no reliable incidence, prevalence, carrier-frequency, founder-effect, ethnic, or geographic-distribution estimates are available. One literature review identified **39 atypical patients among 362 observed IL2RG mutations/cases**, approximately 10%. | ORDO prevalence class not established | The reported proportion is a literature-derived mutation/case series, not a population prevalence estimate, and is vulnerable to publication and classification bias. (lim2019il2rghypomorphicmutation pages 1-2, lim2019il2rghypomorphicmutation pages 4-6) |
| Animal models | Engineered **Il2rg/IL2RG-deficient mice and pigs** model γc-dependent lymphoid failure; IL2RG-edited pigs can show X-linked T−B+NK− SCID, thymic hypoplasia, and arrest of T-cell development, supporting transplantation, humanization, and gene-therapy studies. | NCBI Taxon:10090 (*Mus musculus*); NCBI Taxon:9823 (*Sus scrofa*) | Available models generally use null or large-disruption alleles and therefore resemble classic SCID-X1 more closely than human hypomorphic XCID; allele-specific leaky models are limited. |


*Table: Compact knowledge-base summary of attenuated hypomorphic IL2RG-associated XCID, explicitly distinguished from classic SCID-X1. Identifier uncertainty and evidence limitations are flagged to prevent overinterpretation.*

## 1. Disease information

### Definition

XCID is an X-linked Mendelian combined immunodeficiency caused by **germline hypomorphic IL2RG variants**, sometimes further attenuated by somatic rescue. Unlike classic SCID-X1—with profound T- and NK-cell deficiency and dysfunctional B cells—XCID commonly has measurable T cells and sometimes NK cells, later onset, and prolonged survival. Normal total lymphocyte counts do not exclude it. Lim et al. identified 39 atypical patients among 362 reported IL2RG observations; approximately 10% of reported IL2RG mutations/cases were associated with atypical phenotypes. This is not a population prevalence estimate. (tuovinen2020novelhemizygousil2rg pages 1-2, lim2019il2rghypomorphicmutation pages 1-2, lim2019il2rghypomorphicmutation pages 4-6)

A useful direct abstract statement is: **“Atypical X-linked severe combined immunodeficiency (X-SCID) is a variant of cellular immunodeficiency due to hypomorphic mutations in the interleukin 2 receptor gamma (IL2RG) gene.”** Lim et al., published January 2019, DOI: https://doi.org/10.1186/s13223-018-0317-y. (lim2019il2rghypomorphicmutation pages 1-2)

### Identifiers and synonyms

- **OMIM:** 312863, “immunodeficiency, X-linked, with magnesium defect…” should not be inferred here; the user-specified mapping of **312863 to XCID requires direct OMIM verification**. Historical databases frequently merge attenuated IL2RG disease into SCID-X1/OMIM 300400.
- **MONDO:** MONDO:0010730 was supplied in the request but was not independently confirmed by retrieved evidence. Open Targets instead returned IL2RG under broader “combined immunodeficiency,” MONDO:0015131; this illustrates ontology-mapping instability rather than disproving the requested mapping. (OpenTargets Search: X-linked combined immunodeficiency-IL2RG)
- **Gene:** IL2RG; HGNC:6010; NCBI Gene 3561; Ensembl ENSG00000147168.
- **Protein:** interleukin-2 receptor subunit γ/common γ chain, γc, CD132.
- **Synonyms:** XCID, CIDX, moderate X-linked combined immunodeficiency, atypical X-SCID, leaky X-SCID, hypomorphic IL2RG deficiency, attenuated SCID-X1.
- **ICD/MeSH:** no retrieved dedicated code separates XCID from SCID/combined immunodeficiency. Coding generally falls under combined immunodeficiency or SCID; local verification is required.
- **Source granularity:** most clinical data are patient/family observations subsequently aggregated in reviews, not EHR-derived estimates.

## 2. Etiology

### Causal factor

The primary cause is a **hemizygous germline partial-loss-of-function IL2RG variant**. IL2RG is the shared receptor chain for IL-2, IL-4, IL-7, IL-9, IL-15, and IL-21. Residual receptor expression, membrane trafficking, JAK3 coupling, or downstream STAT activation produces the attenuated phenotype. (arcasgarcia2020theil2rgr328x pages 1-2, tuovinen2020novelhemizygousil2rg pages 1-2, gratz2024functionalcharacterizationof pages 8-13)

### Genetic risk and modifiers

Documented attenuated alleles include:

- NM_000206.3:**c.172C>T, p.(Pro58Ser)**—reduced surface expression through aberrant ER/Golgi interactions and impaired plasma-membrane targeting. (tuovinen2020novelhemizygousil2rg pages 1-2)
- **c.455T>C, p.(Val152Ala)**—associated with a revertant T-cell clone but progressive loss of B and NK cells. (lin2020progressivebcell pages 3-5, lin2020progressivebcell pages 5-6)
- **c.458T>C, p.(Ile153Thr)**—three brothers with T-low/B+/NK-low disease and lymphoid-predominant somatic reversion. (hou2021somaticreversionof pages 5-6, hou2021somaticreversionof pages 6-11)
- **c.664C>T, p.(Arg222Cys)**—reported in at least 18 patients; it can produce either atypical or classic X-SCID, demonstrating imperfect genotype–phenotype correlation. (tuovinen2020novelhemizygousil2rg pages 9-10)
- **c.982C>T, p.(Arg328Ter)**—exon-8 truncation with impaired JAK3 binding but partial STAT5 phosphorylation. Historical notation c.C982T/p.R328X should be normalized to the selected transcript before database entry. (arcasgarcia2020theil2rgr328x pages 1-2, lim2019il2rghypomorphicmutation pages 1-2)

These are germline variants; spontaneous reversion or second-site rescue is somatic. Population allele frequencies and current ClinVar ACMG classifications were not available in retrieved evidence and must be checked per transcript in ClinVar/gnomAD before ingestion. Pathogenicity should not be inferred from IL2RG location alone: segregation, phenotype, population rarity, and functional cytokine-signaling assays are especially important for hypomorphic alleles.

### Environmental, protective, and gene–environment factors

There is no evidence that toxins, diet, smoking, occupation, radiation, or exercise cause XCID. Male sex and maternal family history reflect X-linked inheritance, not environmental risk. Pathogen exposure determines when limited immune reserve becomes clinically evident; HPV, respiratory viruses, enteroviruses, EBV, Giardia, norovirus, Candida, and bacterial respiratory infections have acted as clinical stressors. Somatic reversion is the clearest biological modifier, but it is not reliably protective because corrected clones may be lineage-restricted and oligoclonal. (lin2020progressivebcell pages 3-5, lin2020progressivebcell pages 5-6, hou2021somaticreversionof pages 5-6, lin2020progressivebcell pages 8-9)

No reproducible protective germline allele, lifestyle factor, epigenetic modifier, or formal gene–environment interaction has been established.

## 3. Phenotypes

The phenotype is heterogeneous and age-dependent. In one literature synthesis of 29 atypical cases, **97%** had infection susceptibility and **45% (13/29)** had opportunistic infections; four opportunistic infections occurred despite normal CD3 counts. Normal immunoglobulins occurred in **41% (12/29)**, while **28% (8/29)** had skewed B-cell subsets. Eczema/rash occurred in three, inflammatory arthritis in two, interstitial lung disease in two, and inflammatory bowel disease in one. These are literature-case frequencies, not penetrance estimates. (tuovinen2020novelhemizygousil2rg pages 9-10)

### Major manifestations and suggested HPO terms

- **Recurrent upper/lower respiratory infections**—childhood through adulthood; episodic but cumulatively damaging; HP:0002205/HP:0002719.
- **Bronchiectasis**—secondary, chronic and potentially progressive; documented in children and adults; HP:0002110. (tuovinen2020novelhemizygousil2rg pages 1-2, gratz2024functionalcharacterizationof pages 26-29)
- **Opportunistic infection susceptibility**—variable; HP:0002721.
- **Persistent HPV warts / molluscum contagiosum**—often chronic or treatment-refractory; suggested HP:0032180 and HP:0000960. HPV types 2, 27, and 57 were identified in one family. (hou2021somaticreversionof pages 5-6, gratz2024functionalcharacterizationof pages 26-29)
- **Chronic diarrhea/enteropathy**, including Giardia and norovirus—episodic or progressive; HP:0002028.
- **Failure to thrive/malnutrition**—particularly with enteropathy; HP:0001508/HP:0004395. (lin2020progressivebcell pages 3-5)
- **Thrush/candidiasis**—HP:0002728.
- **Eczema, rash, or granulomatous dermatitis**—HP:0000964/HP:0000988; can reflect infection and immune dysregulation.
- **Inflammatory/reactive arthritis**—HP:0001369. (tuovinen2020novelhemizygousil2rg pages 1-2, tuovinen2020novelhemizygousil2rg pages 9-10)
- **EBV-associated lymphoma/lymphoproliferation**—rare but severe: one four-year-old with p.Arg328Ter died from EBV-related lymphoma; HP:0002664/HP:0001730. (arcasgarcia2020theil2rgr328x pages 1-2)
- **T-cell lymphopenia, especially CD4 lymphopenia**—HP:0005403. In one adult family, serial CD4 counts were 146–272/µL versus 500–2400/µL, and CD4:CD8 ratios were 0.21–0.46. (gratz2024functionalcharacterizationof pages 26-29)
- **NK-cell deficiency/lymphopenia**—HP:0005351.
- **Dysgammaglobulinemia or hypogammaglobulinemia**—HP:0004313/HP:0002723; total levels can be normal despite poor functional immunity.
- **Reduced TRECs and restricted TCR repertoire**—laboratory abnormalities indicating impaired thymic output and oligoclonality. (lin2020progressivebcell pages 5-6, hou2021somaticreversionof pages 6-11)
- **Impaired lymphocyte proliferation and cytokine-induced STAT phosphorylation**—functional laboratory abnormalities. (arcasgarcia2020theil2rgr328x pages 1-2, tuovinen2020novelhemizygousil2rg pages 1-2)

### Quality of life

No XCID-specific EQ-5D, SF-36, PROMIS, or utility study was found. Case histories document repeated hospitalization, chronic airway disease, burdensome wart procedures, antimicrobial and immunoglobulin dependence, nutritional impairment, and malignancy. Thus substantial quality-of-life loss is clinically evident, but no validated quantitative score can be assigned. (gratz2024functionalcharacterizationof pages 21-26, lin2020progressivebcell pages 3-5)

## 4. Genetic and molecular information

**IL2RG** is located on Xq13.1 and encodes CD132. Variant classes producing leaky disease include missense, nonsense/truncating, and splice-altering alleles. The disease mechanism is usually partial loss of function, not gain of function or dominant negative activity.

Allele-specific consequences include:

- **Trafficking failure:** p.Pro58Ser interacts abnormally with ER/Golgi proteins, reduces cell-surface CD132, and impairs IL-2/IL-21 responses. (tuovinen2020novelhemizygousil2rg pages 1-2)
- **Impaired receptor–kinase coupling:** p.Arg328Ter truncates 42 intracellular amino acids and impairs JAK3 binding. Partial STAT5 activation may proceed through an alternative, JAK3-independent route stabilized by a nearby YSE motif. (arcasgarcia2020theil2rgr328x pages 1-2, lim2019il2rghypomorphicmutation pages 4-6)
- **Reduced signaling reserve:** p.Ile153Thr showed weaker STAT5 responses at low-dose IL-2 but near-control responses at very high IL-2; IL-7/IL-15 responses were less affected. (hou2021somaticreversionof pages 6-11)
- **Somatic rescue:** in p.Val152Ala disease, whole blood contained 93% mutant and 7% wild-type reads at age 18, whereas sorted T cells at 22 years were 112/112 wild type. This showed strong selection of a reverted T-cell lineage, yet B cells remained 0–0.4% and later became essentially absent. (lin2020progressivebcell pages 5-6)

No validated modifier gene, disease-specific methylation signature, histone abnormality, recurrent chromosomal rearrangement, or structural chromosome abnormality was found. Rare symptomatic heterozygous females are biologically plausible through skewed X-inactivation, but disease-specific evidence and frequency were not retrieved.

## 5. Environmental information

Environmental toxicants and lifestyle do not initiate the Mendelian disorder. Clinically important exposures are infectious:

- respiratory bacteria and viruses contribute to recurrent pneumonia and bronchiectasis;
- HPV and molluscum exploit impaired cellular immunity;
- EBV may drive lymphoproliferation/lymphoma;
- enterovirus, norovirus, Giardia, Candida, and Pneumocystis are relevant opportunists. (arcasgarcia2020theil2rgr328x pages 1-2, lim2019il2rghypomorphicmutation pages 1-2, lin2020progressivebcell pages 3-5, hou2021somaticreversionof pages 5-6)

No zoonotic agent, toxin, pollutant, dietary pattern, alcohol exposure, or occupation has a demonstrated etiologic role. Gene–environment interaction is best understood as **pathogen burden revealing an inherited shortage of immune signaling capacity**, not as environmental causation.

## 6. Mechanism/pathophysiology

### Ordered causal chain

1. A hemizygous hypomorphic **IL2RG** germline variant **leads to** reduced abundance, trafficking, stability, or signaling competence of CD132.
2. Defective CD132 **leads to** partial impairment of receptors for IL-2, IL-4, IL-7, IL-9, IL-15, and IL-21.
3. Impaired receptor assembly or γc–JAK3 coupling **results in** reduced JAK3 activation and allele-/dose-dependent STAT3, STAT5, or STAT6 phosphorylation.
4. Reduced IL-7 signaling **leads to** impaired thymopoiesis, low naïve T-cell output, reduced TRECs, and restricted αβ-TCR diversity.
5. Reduced IL-2 signaling **leads to** impaired T-cell proliferation, survival, activation, and regulatory/homeostatic control.
6. Reduced IL-15 signaling **leads to** reduced NK-cell development or function; preservation varies by allele.
7. Reduced IL-4/IL-21 signaling and deficient T-cell help **lead to** abnormal B-cell maturation, switched-memory deficiency, dysgammaglobulinemia, and inadequate antigen-specific antibody responses despite preserved B-cell numbers.
8. Branch A: quantitative/qualitative cellular deficiency **leads to** recurrent bacterial, viral, fungal, and parasitic infections, with downstream bronchiectasis, enteropathy, and malnutrition.
9. Branch B: restricted/oligoclonal immunity and defective homeostasis **lead to** inflammatory dermatitis, granulomas, arthritis, bowel inflammation, and possibly malignancy susceptibility.
10. Branch C: somatic reversion or a compensatory second-site variant **results in** selective expansion of corrected lymphoid clones and a milder phenotype; however, lineage restriction and oligoclonality **can lead to** later immune failure. (arcasgarcia2020theil2rgr328x pages 1-2, tuovinen2020novelhemizygousil2rg pages 1-2, lin2020progressivebcell pages 5-6, hou2021somaticreversionof pages 6-11, lin2020progressivebcell pages 8-9)

### Cells, pathways, and ontology suggestions

- **T lymphocyte** CL:0000084; CD4 T cell CL:0000624; CD8 T cell CL:0000625.
- **NK cell** CL:0000623.
- **B lymphocyte** CL:0000236.
- **Plasmacytoid dendritic cell** CL:0000784; very low numbers were observed in p.Pro58Ser disease. (tuovinen2020novelhemizygousil2rg pages 1-2)
- **Hematopoietic stem/progenitor cell** CL:0000037/CL:0000049.
- Suggested GO processes: cytokine-mediated signaling pathway GO:0019221; JAK–STAT cascade GO:0007259; T-cell differentiation GO:0030217; NK-cell differentiation GO:0001779; lymphocyte proliferation GO:0046651; immune response GO:0006955.
- Suggested GO cellular components: plasma membrane GO:0005886; endoplasmic reticulum GO:0005783; Golgi apparatus GO:0005794; cytokine receptor complex GO:0004896.

The p.Pro58Ser BioID result is direct proteomic/proximity-labeling evidence of ER/Golgi mislocalization. Whole-transcriptome studies in IL2RG-disrupted pigs found altered TCR- and cytokine-signaling genes, but no reproducible human XCID transcriptomic, metabolomic, lipidomic, spatial-transcriptomic, or multi-omic signature has been established. (tuovinen2020novelhemizygousil2rg pages 1-2)

A 2023 study added important single-lineage biology: γδ T cells in a p.Pro58Ser patient had normal/enhanced CD132 signaling and cytotoxicity and acquired a lineage-restricted **c.534C>A, p.(Phe178Leu)** second-site variant that improved mutant surface expression in vitro. This argues that expanded γδ cells should not automatically be interpreted as nonspecific homeostatic expansion. DOI: https://doi.org/10.1007/s10875-022-01375-6; published 2023. This is human cellular plus in-vitro evidence.

## 7. Anatomical structures affected

The primary defect resides in the **hematolymphoid system**:

- bone marrow hematopoietic precursors—UBERON:0002371;
- thymus—UBERON:0002370;
- peripheral blood—UBERON:0000178;
- lymph nodes—UBERON:0000029;
- spleen—UBERON:0002106.

Secondary injury affects:

- lung/bronchi—UBERON:0002048/UBERON:0002185, through recurrent infection and bronchiectasis;
- skin—UBERON:0002097, through HPV warts, molluscum, eczema, and granulomatous inflammation;
- intestine—UBERON:0000160, through infectious or inflammatory enteropathy;
- liver—UBERON:0002107, in severe granulomatous/cholestatic disease;
- lymphoid tissues through EBV-related lymphoma. (arcasgarcia2020theil2rgr328x pages 1-2, lin2020progressivebcell pages 3-5, gratz2024functionalcharacterizationof pages 26-29)

Subcellular compartments include plasma membrane, ER/Golgi, cytoplasmic receptor tails/JAK3 complexes, and nucleus for activated STAT transcription. Lateralization is not intrinsic; focal pulmonary disease may be asymmetric, but this is a complication rather than a disease-defining feature.

## 8. Temporal development

XCID is congenital genetically but may present from infancy to adulthood. Onset is usually insidious, with recurrent infections or viral skin disease rather than the fulminant first-month presentation of classic SCID-X1. Examples include an asymptomatic eight-month-old with abnormal immune studies; affected children at four, seven, 11, and 16 years; and adult brothers aged 23–26. (arcasgarcia2020theil2rgr328x pages 1-2, lim2019il2rghypomorphicmutation pages 1-2, gratz2024functionalcharacterizationof pages 26-29)

The course may be stable for years, episodic, or progressive. A p.Val152Ala patient improved temporarily at ages three to four, then developed Giardia at 11, granulomatous/skin disease at 13, norovirus at 17, and progressive enteropathy, malnutrition, pneumonia, and near-loss of T, B, and NK cells in adulthood. This demonstrates that childhood improvement or somatic rescue is not equivalent to durable remission. (lin2020progressivebcell pages 3-5)

Critical windows are:

1. newborn/early infancy, when low TRECs can permit presymptomatic diagnosis;
2. before chronic infection and bronchiectasis;
3. before oligoclonality, immune dysregulation, malignancy, or organ damage complicates definitive treatment. (blanco2020immunereconstitutionafter pages 1-2, lin2020progressivebcell pages 8-9)

No accepted staging system exists.

## 9. Inheritance and population

Inheritance is **X-linked recessive**. Hemizygous males predominate; heterozygous mothers may be asymptomatic carriers. Transmission risk from a carrier mother is 50% for each son to inherit the variant and 50% for each daughter to become a carrier, subject to standard Mendelian assumptions.

Expressivity is markedly variable, even within families. Penetrance among hemizygous males carrying established hypomorphic pathogenic alleles appears high but cannot be quantified; disease may be initially asymptomatic. Anticipation is not expected. Maternal germline mosaicism is possible in X-linked disease generally but no XCID-specific frequency was found. Somatic reversion is well documented and can alter blood-lineage penetrance without changing germline recurrence risk. (lin2020progressivebcell pages 5-6, hou2021somaticreversionof pages 6-11)

No reliable incidence, prevalence, carrier frequency, founder effect, ethnic enrichment, or geographic gradient is available. The 39 atypical patients among 362 reported IL2RG observations and 29-case clinical synthesis indicate extreme rarity but cannot support cases-per-100,000 estimates. (lim2019il2rghypomorphicmutation pages 1-2, tuovinen2020novelhemizygousil2rg pages 9-10)

## 10. Diagnostics

### Recommended clinical evaluation

1. CBC with differential and absolute lymphocyte count—normal values do not exclude XCID.
2. Flow cytometry: CD3, CD4, CD8, CD19/20, CD16/56; naïve/memory T cells; switched-memory and naïve B cells; γδ T cells; plasmacytoid dendritic cells where available.
3. Quantitative IgG, IgA, IgM, IgE and IgG subclasses; vaccine-specific antibodies.
4. T-cell proliferation to mitogens, anti-CD3/CD28, and recall antigens.
5. TRECs and TCR repertoire diversity by flow cytometric Vβ analysis or NGS.
6. CD132 surface expression, while recognizing that normal expression does not establish normal function.
7. Phospho-flow after IL-2, IL-4, IL-7, IL-15, and IL-21 stimulation; STAT5 is especially informative, with STAT3/6 added according to cytokine.
8. Microbiology guided by presentation: respiratory cultures/PCR, EBV/CMV viral loads, HPV typing, enteric pathogen testing, fungal studies.
9. Pulmonary CT and function testing when chronic cough, recurrent pneumonia, or bronchiectasis is suspected. (arcasgarcia2020theil2rgr328x pages 1-2, tuovinen2020novelhemizygousil2rg pages 1-2, hou2021somaticreversionof pages 5-6, hou2021somaticreversionof pages 6-11)

### Genetic testing

Preferred testing is an inborn-errors-of-immunity panel including IL2RG or direct IL2RG sequencing, with deletion/duplication analysis. WES/WGS is appropriate for atypical or panel-negative combined immunodeficiency. Deep sequencing and sequencing of sorted T, B, NK, and myeloid fractions can reveal somatic reversion that bulk blood sequencing may understate. Maternal carrier testing and cascade testing should follow. (lin2020progressivebcell pages 5-6, hou2021somaticreversionof pages 6-11)

CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not routine unless another phenotype suggests them. RNA sequencing may clarify suspected splice variants but is not a standard first-line assay. No validated metabolomic, proteomic, epigenomic, or liquid-biopsy diagnostic exists.

### Diagnostic interpretation and differentials

No universally accepted XCID-specific clinical criteria exist. Diagnosis requires a compatible phenotype plus a hemizygous IL2RG variant and, for uncertain/hypomorphic alleles, functional impairment and segregation.

Differentials include classic SCID-X1; JAK3 deficiency; IL7R deficiency; hypomorphic RAG1/2 or DCLRE1C disease; ZAP70 deficiency; CD40L deficiency; DOCK8 deficiency; WHIM syndrome; GATA2 deficiency; XMEN; activated PI3K-δ syndrome; HIV/secondary immunodeficiency; cystic fibrosis; and primary ciliary dyskinesia. T/B/NK pattern, immunoglobulins, viral susceptibility, syndromic features, and molecular testing distinguish these.

### Screening

Dried-blood-spot **TREC newborn screening can detect some leaky SCID**, but residual thymopoiesis can yield values above program cutoffs. Therefore, a normal screen does not exclude XCID. Currier and Puck emphasized that TREC programs detect SCID and some leaky/hypomorphic cases, but positive TRECs are not gene-specific and require flow cytometry and genetic evaluation. DOI: https://doi.org/10.1016/j.jaci.2020.10.020; published February 2021. (lim2019il2rghypomorphicmutation pages 1-2, hou2024challengeswithgene pages 10-14)

## 11. Outcome and prognosis

No disease-specific five- or ten-year survival, life expectancy, mortality rate, or validated prognostic calculator exists. Outcomes range from survival well into adulthood to death in early childhood from EBV lymphoma or progressive multiorgan infectious/inflammatory disease. (arcasgarcia2020theil2rgr328x pages 1-2, lin2020progressivebcell pages 3-5)

Adverse prognostic features likely include:

- opportunistic or persistent viral infection;
- low naïve T-cell output/TRECs;
- restricted TCR repertoire;
- falling T-, B-, or NK-cell counts;
- poor proliferation or cytokine signaling;
- bronchiectasis, enteropathy, malnutrition, granulomatous disease;
- EBV lymphoproliferation or malignancy;
- delayed definitive therapy. (lin2020progressivebcell pages 5-6, lin2020progressivebcell pages 8-9)

Somatic reversion is not a guaranteed favorable biomarker. The p.Val152Ala case had completely wild-type sorted T cells but oligoclonality, progressive B-cell loss, severe infection, and organ injury. Experts therefore recommend considering definitive therapy before immune dysregulation reduces its success. (lin2020progressivebcell pages 5-6, lin2020progressivebcell pages 8-9)

No formal disability or quality-of-life datasets were found.

## 12. Treatment

### Supportive treatment—direct XCID evidence

- **Immunoglobulin replacement** when antibody production is inadequate—NCIT:C15691.
- **Antimicrobial prophylaxis**, including Pneumocystis prophylaxis when cellular immunity warrants it—NCIT:C15311 broadly.
- Prompt pathogen-directed antibacterial, antiviral, antifungal, or antiparasitic therapy.
- Avoidance of live vaccines when T-cell competence is inadequate; household and blood-product precautions should follow specialist SCID practice.
- Pulmonary surveillance, airway clearance, and bronchiectasis care.
- Nutritional support for enteropathy/failure to thrive.
- Dermatologic treatment for warts/molluscum, although local IL-2, cryotherapy, laser, keratolysis, imiquimod, retinoids, and interferon-α were variably unsuccessful in one family. (hou2021somaticreversionof pages 5-6, gratz2024functionalcharacterizationof pages 26-29, lin2020progressivebcell pages 3-5)

In three p.Ile153Thr brothers, IVIG plus antibiotic prophylaxis prevented further severe bacterial infections in the most affected brother, but warts and bronchiectasis persisted. This is uncontrolled case evidence. (gratz2024functionalcharacterizationof pages 21-26)

### Hematopoietic stem-cell transplantation

Allogeneic HSCT is the established definitive treatment—NCIT:C15246. Direct XCID outcome datasets are sparse. In classic SCID-X1, reported survival is >70% overall, >90% with an HLA-matched sibling, and about 60–75% with alternative donors; treatment before 3.5 months and absence of active infection improve survival. T-cell recovery generally begins by three to four months and normalizes by 9–12 months, while 43–66% may remain immunoglobulin-dependent because B-cell correction is variable. These statistics are **extrapolated from classic SCID-X1 and must not be presented as XCID-specific rates**. (blanco2020immunereconstitutionafter pages 1-2, blanco2020immunereconstitutionafter pages 2-3)

### Gene therapy and editing

Autologous CD34+ HSPC gene addition is NCIT:C16387. Early γ-retroviral IL2RG therapy restored T cells but caused insertional oncogenesis/T-ALL in some patients. Newer self-inactivating lentiviral vectors plus low-dose conditioning have produced broader T-, B-, and NK-cell reconstitution in classic SCID-X1, avoiding donor availability and graft-versus-host disease; long-term genotoxicity monitoring remains necessary. No trial was identified specifically for hypomorphic XCID. (blanco2020immunereconstitutionafter pages 1-2, hou2024challengeswithgene pages 10-14)

CRISPR/HDR, base editing, and prime editing are preclinical for IL2RG/XCID. A 2023 human-HSPC study modeled and corrected SCID variants by multiplex HDR, but this is not clinical efficacy evidence. DOI: https://doi.org/10.1016/j.omtn.2022.12.006; published 2023. Editing risks include off-target mutation, large on-target deletion/rearrangement, inadequate correction of long-term HSCs, and—in reverted mosaic disease—complex clonal competition.

### Trials

Retrieved SCID-X1/primary-immunodeficiency records included **NCT01410019** (completed phase I/II gene therapy; five participants), **NCT01821781** (active, not recruiting, phase II immune-disorder HSCT; 20 participants), **NCT00008450** (completed phase I transplant-conditioning study; six participants), and **NCT00006054** (terminated allogeneic transplantation study). Eligibility for an individual with hypomorphic XCID must be checked directly; none was established as an XCID-specific trial.

No pharmacogenomic rule, approved small-molecule corrective therapy, RNA therapy, surgery, or rehabilitation program is disease-specific.

## 13. Prevention

Primary prevention through lifestyle change is not possible for an inherited X-linked disorder. Reproductive options include carrier testing, cascade testing, prenatal diagnosis, and preimplantation genetic testing after the familial variant is established.

Secondary prevention comprises TREC newborn screening, early immune phenotyping, genetic confirmation, and presymptomatic evaluation of at-risk male relatives. Because TREC screening can miss residual-function disease, family-based molecular testing is more sensitive after a variant is known. (lim2019il2rghypomorphicmutation pages 1-2, hou2024challengeswithgene pages 10-14)

Tertiary prevention includes immunoglobulin and antimicrobial/Pneumocystis prophylaxis as indicated, avoidance of live vaccines with inadequate cellular immunity, irradiated/leukoreduced/CMV-appropriate blood products per specialist practice, prompt infection treatment, respiratory surveillance, EBV monitoring in high-risk patients, and definitive therapy before irreversible organ damage. (blanco2020immunereconstitutionafter pages 1-2, lin2020progressivebcell pages 3-5)

Routine inactivated vaccines may be safe but responses must be measured; vaccine strategy should be individualized by an immunologist. No diet, exercise, sanitation, or environmental intervention corrects the receptor defect.

## 14. Other species and natural disease

Orthologous **Il2rg/IL2RG** genes are conserved in mammals. Relevant taxa include *Mus musculus*—NCBI Taxon 10090—and *Sus scrofa*—NCBI Taxon 9823.

No well-characterized naturally occurring animal disease specifically homologous to **hypomorphic human XCID** was found. Naturally occurring SCID exists in several species, but available evidence does not establish it as the same allele class or IL2RG mechanism.

Engineered porcine IL2RG disruption produces X-linked T−B+NK− SCID, thymic aplasia/hypoplasia, and impaired T-cell development. In one partial-loss/disruption study, **8/10 pigs (80%) were athymic and 2/10 (20%) had a rudimentary thymus**; development arrested around the DN3-to-DN4 transition. DOI: https://doi.org/10.18632/oncotarget.10812; published July 2016. These pigs model classic γc failure better than variable human leaky disease.

There is no zoonotic transmission: XCID is inherited, not infectious.

## 15. Model organisms

### Available models

- **Il2rg-null mice:** widely used T/B/NK-deficient hosts and for transplantation/gene-therapy studies.
- **IL2RG-edited pigs:** large-animal models with human-like body size, anatomy, X-linked inheritance, and T−B+NK− phenotype.
- **RAG2−/−IL2RG−/− pigs:** support allogeneic and xenogeneic transplantation studies. After fetal transplantation, human CD3+ cells made up >70% of thymic cells at birth and persisted to three weeks, although circulating human CD45+ cells disappeared within two weeks and splenic cells by three weeks. DOI: https://doi.org/10.3389/fvets.2022.965316; published October 2022.
- **Patient PBMCs, HEK293 receptor-expression systems, and edited human CD34+ HSPCs:** useful for allele-specific trafficking, signaling, and correction assays. (tuovinen2020novelhemizygousil2rg pages 1-2, hou2021somaticreversionof pages 6-11)

### Applications and limitations

Models are used to study γc-dependent thymopoiesis, NK development, cytokine signaling, transplantation, humanization, viral-vector gene addition, and genome editing. Pigs improve translational assessment of dosing, conditioning, imaging, and long-term cell engraftment relative to mice.

The principal limitation is that most animal models use null or large-disruption alleles and therefore reproduce classic SCID-X1 rather than residual-function, allele-specific XCID. They inadequately model delayed onset, human pathogen exposure, HPV/EBV disease, somatic reversion, oligoclonality, and intrafamilial expressivity. Allele-specific knock-in models for p.Pro58Ser, p.Val152Ala, p.Ile153Thr, p.Arg222Cys, or p.Arg328Ter would better address XCID biology.

## Current expert interpretation and 2023–2024 developments

The current view is that XCID is not simply “mild SCID.” It is a dynamic disorder in which receptor reserve, cytokine concentration, lineage-specific selection, pathogen exposure, and somatic rescue determine phenotype. The 2023 γδ-T-cell study showed that a second-site IL2RG variant can selectively improve signaling and cytotoxic function in one lineage. The 2024 functional/editing work emphasizes that reverted mosaicism complicates both interpretation and design of corrective editing. However, the 2024 sources retrieved were dissertations rather than definitive clinical trials, so their therapeutic proposals remain preclinical. (gratz2024functionalcharacterizationof pages 44-49, hou2024challengeswithgene pages 10-14)

The most defensible clinical conclusion is that apparently preserved lymphocyte numbers or somatic reversion should not reassure clinicians without measurement of naïve T-cell output, TCR diversity, proliferation, cytokine signaling, antibody function, infection burden, and longitudinal cell counts. Early referral to an immunodeficiency/transplant center is appropriate when these markers deteriorate. (tuovinen2020novelhemizygousil2rg pages 9-10, lin2020progressivebcell pages 8-9)

## Evidence gaps requiring explicit database flags

No reliable XCID-specific population prevalence, incidence, carrier frequency, survival curve, quality-of-life score, validated diagnostic criteria, protective factor, modifier gene, epigenetic signature, metabolomic/lipidomic biomarker, approved gene therapy, randomized treatment trial, natural animal counterpart, or allele-specific animal model was identified. OMIM 312863 and MONDO:0010730 should be manually verified before production use because contemporary resources may merge this phenotype with broader IL2RG-related SCID.

References

1. (tuovinen2020novelhemizygousil2rg pages 1-2): Elina A. Tuovinen, Juha Grönholm, Tiina Öhman, Sakari Pöysti, Raine Toivonen, Anna Kreutzman, Kaarina Heiskanen, Luca Trotta, Sanna Toiviainen-Salo, John M. Routes, James Verbsky, Satu Mustjoki, Janna Saarela, Juha Kere, Markku Varjosalo, Arno Hänninen, and Mikko R. J. Seppänen. Novel hemizygous il2rg p.(pro58ser) mutation impairs il-2 receptor complex expression on lymphocytes causing x-linked combined immunodeficiency. Journal of Clinical Immunology, 40:503-514, Feb 2020. URL: https://doi.org/10.1007/s10875-020-00745-2, doi:10.1007/s10875-020-00745-2. This article has 29 citations and is from a domain leading peer-reviewed journal.

2. (lim2019il2rghypomorphicmutation pages 1-2): Che Kang Lim, Hassan Abolhassani, Sofia K. Appelberg, Mikael Sundin, and Lennart Hammarström. Il2rg hypomorphic mutation: identification of a novel pathogenic mutation in exon 8 and a review of the literature. Allergy, Asthma, and Clinical Immunology : Official Journal of the Canadian Society of Allergy and Clinical Immunology, Jan 2019. URL: https://doi.org/10.1186/s13223-018-0317-y, doi:10.1186/s13223-018-0317-y. This article has 61 citations.

3. (OpenTargets Search: X-linked combined immunodeficiency-IL2RG): Open Targets Query (X-linked combined immunodeficiency-IL2RG, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (arcasgarcia2020theil2rgr328x pages 1-2): Andrea Arcas-García, M. García-Prat, Miriam Magallón-Lorenz, A. Martín-Nalda, O. Drechsel, S. Ossowski, Laura Alonso, Jacques G. Rivière, P. Soler-Palacín, R. Colobran, J. Sayós, M. Martínez-Gallo, and C. Franco-Jarava. The il-2rg r328x nonsense mutation allows partial stat-5 phosphorylation and defines a critical region involved in the leaky-scid phenotype. Jan 2020. URL: https://doi.org/10.1111/cei.13405, doi:10.1111/cei.13405. This article has 13 citations and is from a peer-reviewed journal.

5. (hou2021somaticreversionof pages 5-6): Yujuan Hou, Hans Peter Gratz, Guillermo Ureña-Bailén, Paul G. Gratz, Karin Schilbach-Stückle, Tina Renno, Derya Güngör, Daniel A. Mader, Elke Malenke, Justin S. Antony, Rupert Handgretinger, and Markus Mezger. Somatic reversion of a novel il2rg mutation resulting in atypical x-linked combined immunodeficiency. Genes, 13:35, Dec 2021. URL: https://doi.org/10.3390/genes13010035, doi:10.3390/genes13010035. This article has 27 citations.

6. (gratz2024functionalcharacterizationof pages 21-26): Hans Peter Gratz. Functional characterization of a novel il2rg mutation causing atypical scid. Jul 2024. URL: https://doi.org/10.15496/publikation-96566, doi:10.15496/publikation-96566. This article has 0 citations.

7. (gratz2024functionalcharacterizationof pages 26-29): Hans Peter Gratz. Functional characterization of a novel il2rg mutation causing atypical scid. Jul 2024. URL: https://doi.org/10.15496/publikation-96566, doi:10.15496/publikation-96566. This article has 0 citations.

8. (tuovinen2020novelhemizygousil2rg pages 9-10): Elina A. Tuovinen, Juha Grönholm, Tiina Öhman, Sakari Pöysti, Raine Toivonen, Anna Kreutzman, Kaarina Heiskanen, Luca Trotta, Sanna Toiviainen-Salo, John M. Routes, James Verbsky, Satu Mustjoki, Janna Saarela, Juha Kere, Markku Varjosalo, Arno Hänninen, and Mikko R. J. Seppänen. Novel hemizygous il2rg p.(pro58ser) mutation impairs il-2 receptor complex expression on lymphocytes causing x-linked combined immunodeficiency. Journal of Clinical Immunology, 40:503-514, Feb 2020. URL: https://doi.org/10.1007/s10875-020-00745-2, doi:10.1007/s10875-020-00745-2. This article has 29 citations and is from a domain leading peer-reviewed journal.

9. (hou2021somaticreversionof pages 6-11): Yujuan Hou, Hans Peter Gratz, Guillermo Ureña-Bailén, Paul G. Gratz, Karin Schilbach-Stückle, Tina Renno, Derya Güngör, Daniel A. Mader, Elke Malenke, Justin S. Antony, Rupert Handgretinger, and Markus Mezger. Somatic reversion of a novel il2rg mutation resulting in atypical x-linked combined immunodeficiency. Genes, 13:35, Dec 2021. URL: https://doi.org/10.3390/genes13010035, doi:10.3390/genes13010035. This article has 27 citations.

10. (lin2020progressivebcell pages 3-5): Connie H. Lin, Hye Sun Kuehn, Timothy J. Thauland, Christine M. Lee, Suk See De Ravin, Harry L. Malech, Timothy J. Keyes, Astraea Jager, Kara L. Davis, Maria I. Garcia-Lloret, Sergio D. Rosenzweig, and Manish J. Butte. Progressive b cell loss in revertant x-scid. Journal of Clinical Immunology, 40:1001-1009, Jul 2020. URL: https://doi.org/10.1007/s10875-020-00825-3, doi:10.1007/s10875-020-00825-3. This article has 10 citations and is from a domain leading peer-reviewed journal.

11. (lim2019il2rghypomorphicmutation pages 4-6): Che Kang Lim, Hassan Abolhassani, Sofia K. Appelberg, Mikael Sundin, and Lennart Hammarström. Il2rg hypomorphic mutation: identification of a novel pathogenic mutation in exon 8 and a review of the literature. Allergy, Asthma, and Clinical Immunology : Official Journal of the Canadian Society of Allergy and Clinical Immunology, Jan 2019. URL: https://doi.org/10.1186/s13223-018-0317-y, doi:10.1186/s13223-018-0317-y. This article has 61 citations.

12. (lin2020progressivebcell pages 5-6): Connie H. Lin, Hye Sun Kuehn, Timothy J. Thauland, Christine M. Lee, Suk See De Ravin, Harry L. Malech, Timothy J. Keyes, Astraea Jager, Kara L. Davis, Maria I. Garcia-Lloret, Sergio D. Rosenzweig, and Manish J. Butte. Progressive b cell loss in revertant x-scid. Journal of Clinical Immunology, 40:1001-1009, Jul 2020. URL: https://doi.org/10.1007/s10875-020-00825-3, doi:10.1007/s10875-020-00825-3. This article has 10 citations and is from a domain leading peer-reviewed journal.

13. (lin2020progressivebcell pages 8-9): Connie H. Lin, Hye Sun Kuehn, Timothy J. Thauland, Christine M. Lee, Suk See De Ravin, Harry L. Malech, Timothy J. Keyes, Astraea Jager, Kara L. Davis, Maria I. Garcia-Lloret, Sergio D. Rosenzweig, and Manish J. Butte. Progressive b cell loss in revertant x-scid. Journal of Clinical Immunology, 40:1001-1009, Jul 2020. URL: https://doi.org/10.1007/s10875-020-00825-3, doi:10.1007/s10875-020-00825-3. This article has 10 citations and is from a domain leading peer-reviewed journal.

14. (hou2024challengeswithgene pages 10-14): Yujuan Hou. Challenges with gene therapy based on crispr/cas9 and prime editing for somatic reverted mosaicism of x-linked combined immunodeficiency. Unknown, Mar 2024. URL: https://doi.org/10.15496/publikation-93762, doi:10.15496/publikation-93762. This article has 0 citations.

15. (blanco2020immunereconstitutionafter pages 1-2): Elena Blanco, Natalia Izotova, Claire Booth, and Adrian James Thrasher. Immune reconstitution after gene therapy approaches in patients with x-linked severe combined immunodeficiency disease. Frontiers in Immunology, Nov 2020. URL: https://doi.org/10.3389/fimmu.2020.608653, doi:10.3389/fimmu.2020.608653. This article has 51 citations and is from a peer-reviewed journal.

16. (blanco2020immunereconstitutionafter pages 2-3): Elena Blanco, Natalia Izotova, Claire Booth, and Adrian James Thrasher. Immune reconstitution after gene therapy approaches in patients with x-linked severe combined immunodeficiency disease. Frontiers in Immunology, Nov 2020. URL: https://doi.org/10.3389/fimmu.2020.608653, doi:10.3389/fimmu.2020.608653. This article has 51 citations and is from a peer-reviewed journal.

17. (gratz2024functionalcharacterizationof pages 8-13): Hans Peter Gratz. Functional characterization of a novel il2rg mutation causing atypical scid. Jul 2024. URL: https://doi.org/10.15496/publikation-96566, doi:10.15496/publikation-96566. This article has 0 citations.

18. (gratz2024functionalcharacterizationof pages 44-49): Hans Peter Gratz. Functional characterization of a novel il2rg mutation causing atypical scid. Jul 2024. URL: https://doi.org/10.15496/publikation-96566, doi:10.15496/publikation-96566. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](X-Linked_Combined_Immunodeficiency-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 68 |
| Resolved | 63 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0010730` (4 mentions) - the report calls it "if available"; MONDO calls it **combined immunodeficiency, X-linked**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0005351` (2 mentions) - HP does not contain this term

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Gene`, `Taxon`.
