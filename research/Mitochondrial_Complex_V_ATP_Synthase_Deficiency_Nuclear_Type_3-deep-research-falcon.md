---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T10:25:50.403875'
end_time: '2026-09-02T10:37:13.852331'
duration_seconds: 683.45
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mitochondrial complex V (ATP synthase) deficiency, nuclear type 3
    (MC5DN3), caused by biallelic variants in the nuclear gene ATP5F1E (ATP5E) encoding
    the epsilon subunit of the F1 catalytic head. NOT the maternally inherited MT-ATP6
    diseases (NARP, Leigh) and NOT combined OXPHOS deficiency
  mondo_id: MONDO:0013547
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 46
  verified: 44
  not_found: 0
  obsolete: 2
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0013547
    reported_labels:
    - if available
    ontology_label: mitochondrial complex V (ATP synthase) deficiency, nuclear type
      3
  - term_id: CL:0000540
    reported_labels:
    - Candidate affected cell types:** neuron
    ontology_label: neuron
  obsolete_terms:
  - term_id: GO:0005753
    ontology_label: obsolete mitochondrial proton-transporting ATP synthase complex
    replaced_by: GO:0045259
  - term_id: GO:0000275
    ontology_label: obsolete mitochondrial proton-transporting ATP synthase complex,
      catalytic sector F(1)
    replaced_by: GO:0045259
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Mitochondrial_Complex_V_ATP_Synthase_Deficiency_Nuclear_Type_3-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial complex V (ATP synthase) deficiency, nuclear type 3 (MC5DN3), caused by biallelic variants in the nuclear gene ATP5F1E (ATP5E) encoding the epsilon subunit of the F1 catalytic head. NOT the maternally inherited MT-ATP6 diseases (NARP, Leigh) and NOT combined OXPHOS deficiency
- **MONDO ID:** MONDO:0013547 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial complex V (ATP synthase) deficiency, nuclear type 3 (MC5DN3), caused by biallelic variants in the nuclear gene ATP5F1E (ATP5E) encoding the epsilon subunit of the F1 catalytic head. NOT the maternally inherited MT-ATP6 diseases (NARP, Leigh) and NOT combined OXPHOS deficiency** covering all of the
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
- **Disease Name:** Mitochondrial complex V (ATP synthase) deficiency, nuclear type 3 (MC5DN3), caused by biallelic variants in the nuclear gene ATP5F1E (ATP5E) encoding the epsilon subunit of the F1 catalytic head. NOT the maternally inherited MT-ATP6 diseases (NARP, Leigh) and NOT combined OXPHOS deficiency
- **MONDO ID:** MONDO:0013547 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial complex V (ATP synthase) deficiency, nuclear type 3 (MC5DN3), caused by biallelic variants in the nuclear gene ATP5F1E (ATP5E) encoding the epsilon subunit of the F1 catalytic head. NOT the maternally inherited MT-ATP6 diseases (NARP, Leigh) and NOT combined OXPHOS deficiency** covering all of the
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


# Research report: ATP5F1E-related mitochondrial complex V deficiency, nuclear type 3

## Executive summary and evidence limits

Mitochondrial complex V deficiency, nuclear type 3 (MC5DN3) is an **autosomal-recessive, nuclear-encoded, isolated ATP-synthase deficiency** caused by biallelic pathogenic variants in **ATP5F1E** (historical symbol **ATP5E**), which encodes the ε subunit of the mitochondrial F1 catalytic head/central stalk. It is distinct from maternally inherited **MT-ATP6** disorders, including NARP and MT-ATP6-associated Leigh syndrome, and from combined oxidative-phosphorylation deficiencies.

The evidence base is exceptionally small. Through the 2024 systematic review, only **three affected individuals from three unrelated families** had been reported, all homozygous for the same missense allele, **c.35A>G (p.Tyr12Cys)**. Thus, apparent phenotype frequencies below describe three published patients, not robust population estimates. The 2024 review added synthesis but no new ATP5F1E allele or patient. (zech2022variantsinmitochondrial pages 7-8, tauchmannova2024variabilityofclinical pages 15-16)

| Domain | Finding | Evidence type | Strength/limitation |
|---|---|---|---|
| Established cases and variant | Three affected individuals from unrelated families have been reported with the same homozygous **ATP5F1E** (formerly **ATP5E**) missense variant, **c.35A>G (p.Tyr12Cys)**. The original patient was reported in 2010; two additional individuals were identified in a 2,962-exome analysis published in 2022. (zech2022variantsinmitochondrial pages 7-8, mayr2010mitochondrialatpsynthase pages 1-2) | Human clinical-genetic; case report plus cohort/gene-matching study | Strong variant-level recurrence and phenotype concordance, but only three known patients and one reported disease allele severely limit genotype–phenotype inference and frequency estimates. |
| Core clinical phenotype and natural history | Neonatal or infantile metabolic disease included lactic acidosis, sometimes 3-methylglutaconic aciduria, vomiting, respiratory distress or transient respiratory failure, impaired consciousness, and seizures. Later findings included developmental or intellectual disability, ataxia, peripheral axonal-demyelinating neuropathy, gait impairment, and limb or generalized dystonia; visual and hearing deficits occurred in one patient. Metabolic abnormalities improved or normalized later. The original patient remained clinically non-progressive over an 11-year follow-up to age 33, although neurologic disability persisted; another patient developed progressive generalized dystonia with poor medication response. (zech2022variantsinmitochondrial pages 7-8, tauchmannova2024variabilityofclinical pages 15-16, mayr2010mitochondrialatpsynthase pages 1-2) | Human clinical; three individual patients with longitudinal follow-up for one | Direct disease-specific evidence, but frequencies are unstable because the denominator is three and clinical documentation differs among patients. |
| Human fibroblast biochemical evidence | Original-patient fibroblasts showed a **67% reduction** in oligomycin-sensitive ATPase activity, **77% reduction** in aurovertin-sensitive activity, and mitochondrial ATP synthesis reduced by **74%** with pyruvate/malate and **71%** with succinate. Oligomycin-sensitive ATPase was **<10 mU/mg protein** versus **43–190** in controls. ATP synthase content was reduced by about **70%**, whereas complexes I–IV were normal or increased; assembled-complex labeling was **55% lower**. The complex retained normal size and incorporated mutant epsilon subunit, while subunit c accumulated in detergent-insoluble material. A second patient had markedly reduced ATP5F1A staining, undetectable ATP5F1A in leukocytes and thrombocytes, and significantly reduced oxygen-consumption rate. (zech2022variantsinmitochondrial pages 7-8, mayr2010mitochondrialatpsynthase pages 2-3, mayr2010mitochondrialatpsynthase pages 1-2, mayr2010mitochondrialatpsynthase pages 3-4) | Human patient-derived fibroblast and blood-cell functional assays | Strong evidence for an isolated complex-V abundance/assembly defect with impaired ATP production. Measurements derive mainly from one fibroblast line; no standardized multicenter replication or rescue experiment with wild-type ATP5F1E was reported. |
| Inheritance | All affected individuals were homozygous for p.Tyr12Cys, while available unaffected parents were heterozygous, supporting **autosomal-recessive** inheritance. (zech2022variantsinmitochondrial pages 7-8) | Human segregation evidence | Strong for the reported families; penetrance, carrier frequency, germline mosaicism, and modifier effects cannot be estimated from three cases. |
| Yeast model and limitation | The orthologous **Saccharomyces cerevisiae** substitution, epsilon **p.Tyr11Cys**, did not significantly impair growth on non-fermentable substrates, ATP synthase activity, or complex assembly/stability. Investigators concluded that ATP synthase biogenesis differs between yeast and humans and proposed that the human mutant protein may undergo defective mitochondrial import, incorporation, or proteolytic stability. (sardin2015biochemicalinvestigationof pages 1-2, sardin2015biochemicalinvestigationof pages 5-7) | Variant-specific model organism; biochemical and structural inference | Useful negative/comparative result, but it fails to reproduce the defining human assembly phenotype and therefore has limited fidelity for therapeutic testing. |
| 2024 review update | A 2024 systematic review retained only the three p.Tyr12Cys patients and summarized a comparatively mild, survivable phenotype without reported cardiac involvement: early lactic acidosis and 3-methylglutaconic aciduria followed by neurodevelopmental impairment, ataxia, neuropathy, seizures, dystonia, and—in two patients—respiratory crises; metabolic abnormalities improved later. (tauchmannova2024variabilityofclinical pages 15-16) | Recent authoritative systematic review of reported isolated ATP-synthase defects | Confirms that no broader ATP5F1E allelic series or additional published patients had emerged by 2024; conclusions remain dependent on the 2010 and 2022 reports. |
| Treatment and trial evidence gaps | No ATP5F1E-specific disease-modifying therapy, gene/RNA/cell therapy, controlled treatment study, response rate, or relevant registered interventional trial was identified. One patient’s generalized dystonia responded poorly to unspecified trialed medications. General mitochondrial-disease care is supportive and phenotype-directed, but it is not evidence of efficacy in MC5DN3. (zech2022variantsinmitochondrial pages 7-8, zech2022variantsinmitochondrial pages 10-11, klopstock2021mitochondrialdisorders pages 2-3) | Disease-specific literature and trial-search gap; general expert guidance | Major evidence gap: absence of published or registered evidence is not proof that an intervention is ineffective, and management must be individualized by a mitochondrial-disease specialist. |


*Table: Compact evidence matrix for ATP5F1E-related mitochondrial complex V deficiency, separating direct human findings from model evidence and documented knowledge gaps. It highlights the extremely small case base and the quantitative functional evidence supporting pathogenicity.*

## 1. Disease information

### Definition and scope

MC5DN3 is a Mendelian mitochondrial energy-metabolism disorder in which defective ATP5F1E causes markedly reduced abundance and activity of assembled respiratory-chain complex V. Complexes I–IV are relatively preserved, making this an **isolated complex-V deficiency**. The phenotype begins neonatally or in infancy with lactic acidosis and metabolic/respiratory decompensation and evolves into a predominantly neurologic syndrome involving development, cerebellar function, peripheral nerves, seizures, and dystonia. Cardiac involvement has not been reported in the three known patients. (tauchmannova2024variabilityofclinical pages 15-16, mayr2010mitochondrialatpsynthase pages 2-3, mayr2010mitochondrialatpsynthase pages 1-2)

### Identifiers and names

- **MONDO:** MONDO:0013547, as specified for this entry.
- **OMIM disease:** **614053**, mitochondrial complex V deficiency, nuclear type 3.
- **OMIM gene:** **ATP5F1E, 606153**.
- **Gene symbols:** current **ATP5F1E**; historical **ATP5E**.
- **Common names:** mitochondrial complex V deficiency, nuclear type 3; ATP5F1E-related mitochondrial disease; ATP5E-related ATP-synthase deficiency; mitochondrial ATP-synthase ε-subunit deficiency.
- **Orphanet:** no confidently verified disease-specific ORPHA identifier was found; it may be represented under broader mitochondrial ATP-synthase/oxidative-phosphorylation deficiency categories.
- **ICD-10/ICD-11 and MeSH:** no specific code/descriptor was identified. Coding ordinarily uses a broader mitochondrial-metabolism or mitochondrial-disease category, with the molecular diagnosis recorded separately.

The primary literature consists of individual patient observations and patient-derived cell experiments. OMIM/MONDO and reviews are aggregated disease-level resources derived largely from those same reports; they should not be interpreted as independent cohorts.

## 2. Etiology and risk/protective factors

### Causal factor

The demonstrated cause is a **germline biallelic ATP5F1E variant**. All known patients carry homozygous c.35A>G (p.Tyr12Cys), while tested unaffected parents were heterozygous, establishing autosomal-recessive segregation. The variant was absent from the control data used in the 2022 study. (zech2022variantsinmitochondrial pages 7-8)

The causal relationship is supported by recurrence in unrelated families, segregation, conservation of Tyr12, and a highly specific patient-cell phenotype: isolated loss of assembled complex V, reduced ATP synthesis, and reduced oxygen-consumption capacity. (zech2022variantsinmitochondrial pages 7-8, mayr2010mitochondrialatpsynthase pages 1-2, mayr2010mitochondrialatpsynthase pages 3-4)

### Risk factors

- **Genetic:** carrying two pathogenic ATP5F1E alleles is the primary risk. No susceptibility loci, modifier genes, polygenic effects, founder haplotype, or established genotype–phenotype modifiers have been reported.
- **Family history/consanguinity:** recessive inheritance makes parental relatedness a theoretical enrichment factor, but consanguinity was not documented in the retrieved patient reports.
- **Environmental/lifestyle:** no toxin, diet, smoking, alcohol, occupational exposure, sex, or age-related factor causes the disorder.
- **Physiologic stress:** infection precipitated metabolic deterioration in the original patient during early childhood; these episodes later resolved. Infection is therefore a **trigger of decompensation**, not an etiologic infectious agent. (zech2022variantsinmitochondrial pages 7-8)

### Protective factors and gene–environment interaction

No protective allele, modifier, diet, supplement, or lifestyle intervention has been demonstrated. Avoidance and prompt treatment of fasting, dehydration, fever, and infection are biologically reasonable mitochondrial-disease precautions, but have not been tested specifically in MC5DN3. The only observed gene–environment interaction is infection-triggered decompensation in one patient. (zech2022variantsinmitochondrial pages 7-8)

## 3. Phenotypes

Because the denominator is three, counts are provisional. Suggested HPO terms should be validated against the current HPO release before database import.

| Phenotype | Type, onset/course, observed frequency | Suggested HPO term |
|---|---|---|
| Lactic acidosis/elevated lactate | Laboratory abnormality; neonatal/infantile; **3/3**; improved or normalized later | HP:0003128 Lactic acidosis; HP:0002151 Increased serum lactate |
| Developmental delay/intellectual disability | Neurodevelopmental; **3/3**; persistent, mild in the original adult and more substantial in the others | HP:0012758 Neurodevelopmental delay; HP:0001249 Intellectual disability |
| Ataxia/gait impairment | Neurologic sign; **2/3 clearly described**, with later gait disability | HP:0001251 Ataxia; HP:0002066 Gait ataxia; HP:0001288 Gait disturbance |
| Peripheral neuropathy | Neurologic/electrophysiologic; **2/3 clearly described**; axonal-demyelinating in the adult | HP:0009830 Peripheral neuropathy; HP:0003477 Peripheral axonal neuropathy; HP:0007108 Demyelinating peripheral neuropathy |
| Dystonia | Movement disorder; **2/3 clearly described**; limb dystonia in one, progressive generalized dystonia in another | HP:0001332 Dystonia; HP:0007325 Generalized dystonia |
| Seizures | Neurologic; **2/3**; neonatal/infantile or generalized tonic–clonic episodes | HP:0001250 Seizure; HP:0002069 Generalized tonic-clonic seizure |
| Respiratory distress/failure | Acute clinical sign; **2/3**; neonatal or infantile and transient in one | HP:0002098 Respiratory distress; HP:0002878 Respiratory failure |
| Vomiting/impaired consciousness | Acute metabolic presentation; reported in patient 2 | HP:0002013 Vomiting; HP:0004372 Reduced consciousness/confusion as locally appropriate |
| Visual and hearing deficits | Sensory manifestations; **1/3** | HP:0000505 Visual impairment; HP:0000365 Hearing impairment |
| Exercise intolerance | Symptom; reported in the original patient | HP:0003546 Exercise intolerance |
| 3-methylglutaconic aciduria | Urinary biochemical abnormality; explicitly reported in the original patient | HP:0003535 3-Methylglutaconic aciduria |

The clinical source describes neonatal/infantile lactic acidosis, respiratory crises and seizures, followed by developmental disability, ataxia, neuropathy and dystonia. In all three, metabolic abnormalities improved later in life. (zech2022variantsinmitochondrial pages 7-8, tauchmannova2024variabilityofclinical pages 15-16)

**Quality of life:** no EQ-5D, SF-36, PROMIS, caregiver-burden, or disease-specific quality-of-life study exists. Nevertheless, gait impairment, neuropathy, sensory deficits, intellectual disability, seizures and generalized dystonia plausibly impair mobility, education, communication and independence. This is clinical inference, not quantified MC5DN3 evidence.

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** ATP5F1E; historical ATP5E.
- **Function:** nuclear-encoded mitochondrial ATP synthase F1 subunit ε, a component of the γ–δ–ε central stalk linking the F1 catalytic head to the Fo rotor.
- **Genomic origin:** nuclear DNA; the disease is therefore Mendelian and **not maternally inherited**.
- **Variant origin:** germline; no somatic ATP5F1E cause is implicated.

### Pathogenic variant

The sole established disease allele is **c.35A>G (p.Tyr12Cys)**, homozygous in all three patients. It is a missense substitution at a conserved N-terminal residue. The original report demonstrated homozygosity and parental carrier status; the 2022 report found the same genotype in two additional unrelated patients. (zech2022variantsinmitochondrial pages 7-8, mayr2010mitochondrialatpsynthase pages 3-4)

Functionally, p.Tyr12Cys behaves primarily as a **hypomorphic loss-of-function/assembly-stability allele**, rather than a catalytic-null allele: assembled complexes containing mutant ε were normal in size and apparently retained near-normal activity per assembled enzyme, but total assembled complex was reduced by approximately 70%. (sardin2015biochemicalinvestigationof pages 5-7, mayr2010mitochondrialatpsynthase pages 1-2, mayr2010mitochondrialatpsynthase pages 3-4)

A contemporary clinical laboratory should classify the allele using current ACMG/AMP criteria, including segregation, rarity, recurrence and strong phenotype-specific functional evidence. No independent current ClinVar classification or exact gnomAD allele frequency was verified in the retrieved evidence; the 2022 study states it was unobserved in controls. (zech2022variantsinmitochondrial pages 7-8)

No pathogenic nonsense, frameshift, canonical splice, copy-number, structural or chromosomal ATP5F1E variant has been established for MC5DN3 in the literature reviewed through 2024. No modifier gene or disease-specific epigenetic signature is known.

## 5. Environmental information

No environmental toxin, radiation exposure, pollutant, occupational factor, lifestyle exposure, or pathogen causes MC5DN3. Infection can increase energy demand and precipitate metabolic decompensation, as observed in one patient, but is not part of the inherited cause. (zech2022variantsinmitochondrial pages 7-8)

There is no disease-specific evidence that smoking, alcohol, exercise, diet or supplements alter penetrance. Exercise should be individualized because the reported phenotype includes exercise intolerance and neuropathy; prolonged inactivity may also worsen deconditioning. General mitochondrial guidance—not MC5DN3 trial evidence—supports supervised endurance and strength activity where tolerated. (klopstock2021mitochondrialdisorders pages 2-3)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic ATP5F1E c.35A>G (p.Tyr12Cys) leads to** production of a structurally altered ε subunit at a conserved central-stalk residue.
2. **The altered ε subunit leads to** reduced incorporation, mitochondrial import, or stability of ε during mammalian complex-V biogenesis; the exact proximal defect remains inferred rather than directly resolved. (sardin2015biochemicalinvestigationof pages 5-7)
3. **Defective ε availability leads to** impaired assembly/stability of the F1 sector and reduced formation of intact F1Fo ATP synthase.
4. **Reduced complex-V assembly results in** approximately 60–70% loss of ATPase/ATP-synthetic capacity while complexes I–IV remain preserved or increased. (mayr2010mitochondrialatpsynthase pages 2-3, mayr2010mitochondrialatpsynthase pages 1-2, mayr2010mitochondrialatpsynthase pages 3-4)
5. **Insufficient ATP-synthase capacity leads to** impaired ADP-stimulated respiration and diminished ATP production; respiratory-chain capacity exceeds phosphorylating capacity. (mayr2010mitochondrialatpsynthase pages 2-3)
6. **The bioenergetic mismatch leads to** increased reliance on glycolysis and lactate production, producing neonatal/infantile lactic acidosis and vulnerability during infection or other metabolic stress; this metabolic interpretation is strongly supported but the exact tissue flux has not been profiled in vivo.
7. **Chronic ATP insufficiency in high-demand neural and neuromuscular cells leads to** developmental impairment, seizures, ataxia, peripheral neuropathy and dystonia; the cell-type link is inferred from phenotype rather than demonstrated by patient brain tissue.
8. **Branch—aberrant assembly results in** accumulation of Fo subunit c in detergent-insoluble material, which may contribute to proteostatic or membrane stress; its direct role in clinical injury is unproven. (mayr2010mitochondrialatpsynthase pages 1-2)
9. **Branch—inadequate phosphorylation capacity may lead to** elevated membrane potential and reactive-oxygen-species production, a mechanism described for isolated ATP-synthase deficiency, but not directly quantified in these three patients. (mayr2010mitochondrialatpsynthase pages 2-3)

### Quantitative disease-specific biochemistry

Original-patient fibroblasts had a 67% reduction in oligomycin-sensitive ATPase activity and 77% reduction in aurovertin-sensitive activity. ATP synthesis fell 74% using pyruvate/malate and 71% using succinate. Oligomycin-sensitive ATPase activity was **<10 mU/mg protein**, compared with **43–190** in controls. ATP-synthase content fell about 70%, while complexes I–IV were normal or increased; pulse-labeling of assembled ATP synthase was 55% lower. (mayr2010mitochondrialatpsynthase pages 2-3, mayr2010mitochondrialatpsynthase pages 1-2, mayr2010mitochondrialatpsynthase pages 3-4)

The normal-sized residual complex contained mutant ε, supporting the interpretation that p.Tyr12Cys primarily reduces enzyme abundance/assembly rather than abolishing catalysis in complexes that successfully assemble. (sardin2015biochemicalinvestigationof pages 5-7, mayr2010mitochondrialatpsynthase pages 1-2)

### Pathways and ontology suggestions

- **Reactome/biochemical pathway:** mitochondrial oxidative phosphorylation; respiratory electron transport, chemiosmotic coupling and ATP synthesis.
- **GO biological process:** GO:0006119 oxidative phosphorylation; GO:0015986 proton-motive-force-driven ATP synthesis; GO:0046034 ATP metabolic process; GO:0033108 mitochondrial respiratory-chain complex assembly; GO:0007005 mitochondrion organization.
- **GO molecular function:** GO:0046933 proton-transporting ATP synthase activity, rotational mechanism; ATPase-coupled transmembrane transporter activity where appropriate.
- **GO cellular component:** GO:0005753 mitochondrial proton-transporting ATP synthase complex; GO:0000275 mitochondrial proton-transporting ATP synthase complex, catalytic core F1; GO:0005743 mitochondrial inner membrane; GO:0005759 mitochondrial matrix.
- **CHEBI:** CHEBI:15422 ATP; CHEBI:16761 ADP; CHEBI:43474 phosphate; CHEBI:24996 lactate; CHEBI:15378 hydron.
- **Candidate affected cell types:** neuron (CL:0000540), cerebellar neuron, motor neuron (CL:0000100), Schwann cell (CL:0002573), skeletal muscle cell/myocyte (CL:0000188). These are phenotype-based candidates, not demonstrated cell-selective lesions.

No MC5DN3-specific immune, inflammatory, epigenomic, transcriptomic, single-cell, spatial, lipidomic or multi-omic disease signature has been reported. Blood-cell immunostaining in one patient showed undetectable ATP5F1A in leukocytes and thrombocytes, providing a potential cellular biomarker but not an immune mechanism. (zech2022variantsinmitochondrial pages 7-8)

## 7. Anatomical structures affected

The principal demonstrated system is neurologic/neuromuscular:

- **Central nervous system/brain**—developmental disability, seizures, ataxia and dystonia. Suggested UBERON:0000955 brain; UBERON:0002037 cerebellum; UBERON:0002420 basal ganglion. Specific regional injury is not proven.
- **Peripheral nervous system**—axonal-demyelinating neuropathy. Suggested UBERON:0000010 peripheral nervous system and UBERON terms for peripheral nerve.
- **Skeletal neuromuscular system**—exercise intolerance and gait impairment; direct myopathy was not established.
- **Sensory systems**—visual and auditory deficits in one patient; anatomical localization was not reported.
- **Respiratory system**—transient functional failure during early metabolic crises, not established primary lung pathology.
- **Heart**—not involved in the three reported ATP5F1E patients, although cardiomyopathy is important in other complex-V disorders and should still be monitored. (tauchmannova2024variabilityofclinical pages 15-16)

At subcellular level, the lesion localizes to the mitochondrial matrix-facing F1 sector and central stalk of ATP synthase at the inner mitochondrial membrane. Laterality is not a meaningful disease feature.

## 8. Temporal development

Onset is neonatal or infantile. Early disease is episodic/acute-on-chronic, with lactic acidosis, vomiting, respiratory distress, impaired consciousness or seizures. Metabolic abnormalities subsequently improved or normalized in all three reported individuals. (zech2022variantsinmitochondrial pages 7-8, tauchmannova2024variabilityofclinical pages 15-16)

The later course is variable. The original patient survived to 33 years and was described as non-progressive over 11 years, although intellectual disability, ataxia, polyneuropathy, gait impairment and limb dystonia persisted. Patient 2 developed progressive generalized dystonia with poor response to unspecified medications. Patient 3 had persistent intellectual disability, ataxia and neuropathy at age 13. (zech2022variantsinmitochondrial pages 7-8)

No validated stages, remission criteria or critical therapeutic window exist. Neonatal/infantile metabolic crises are the most apparent period of vulnerability. Later improvement in lactate does not imply neurologic recovery.

## 9. Inheritance, epidemiology and population

Inheritance is **autosomal recessive**. For two heterozygous parents, each pregnancy has the conventional 25% probability of an affected child, 50% probability of an unaffected carrier and 25% probability of inheriting neither familial allele, subject to confirmation of parental genotypes.

Penetrance among p.Tyr12Cys homozygotes appears high in the three cases, but cannot be estimated. Expressivity is variable, particularly for respiratory crises, sensory deficits and dystonia. There is no evidence of anticipation. Germline mosaicism, founder effect and carrier frequency are unknown.

No population prevalence or incidence has been established. The minimum published case count through the 2024 review is three. A broader 2022 analysis found nuclear ATP-synthase-gene diagnoses in 5/1,950 (0.3%) suspected mitochondrial-disease cases, but that statistic is **not ATP5F1E-specific** and must not be used as MC5DN3 prevalence. (zech2022variantsinmitochondrial pages 10-11)

Ethnic origin, geographic clustering, sex ratio and population-specific allele distribution cannot be inferred. The three known patients were female, but this is almost certainly an unstable observation rather than evidence of sex bias.

## 10. Diagnostics

### Recommended approach

1. **Clinical suspicion:** neonatal/infantile lactic acidosis or unexplained respiratory/metabolic crisis followed by developmental disability, seizures, ataxia, neuropathy or dystonia—particularly with 3-methylglutaconic aciduria.
2. **First-line laboratory evaluation:** serum/plasma lactate, pyruvate with careful collection, blood gas, glucose, electrolytes, ammonia, liver enzymes, CK, plasma amino acids, acylcarnitines, and urine organic acids including 3-methylglutaconic acid. Lactate may normalize later and is not specific.
3. **Neurologic evaluation:** developmental assessment; EEG for seizures; nerve-conduction studies/EMG for neuropathy; ophthalmology and audiology where indicated.
4. **Imaging:** brain MRI can assess structural injury and differentials, but ATP-synthase cohort MRI findings were often nonspecific. (zech2022variantsinmitochondrial pages 10-11)
5. **Molecular confirmation:** sequencing must demonstrate pathogenic/likely pathogenic variants on both ATP5F1E alleles, with parental segregation when possible.

### Genetic testing

A mitochondrial-disease or nuclear OXPHOS panel including **ATP5F1E**, WES, or WGS is appropriate. WES/WGS is preferable when the phenotype is nonspecific because numerous nuclear genes cause complex-V deficiency or overlapping neurologic disease. General mitochondrial-disease guidance reports that exome/genome approaches can improve diagnostic yield relative to restricted panels, although that is not an ATP5F1E-specific performance estimate. (klopstock2021mitochondrialdisorders pages 2-3)

Single-gene ATP5F1E testing is efficient when c.35A>G is already suspected or a familial variant is known. Deletion/duplication analysis should be considered if sequencing finds one allele. WGS and RNA sequencing may help identify deep-intronic or structural alleles, but no such ATP5F1E disease allele has yet been reported. CMA, karyotyping, FISH and repeat-expansion testing are not primary tests unless another diagnosis is suspected.

**mtDNA sequencing does not establish MC5DN3**, although concurrent mtDNA analysis may be necessary to exclude MT-ATP6/MT-ATP8 disease in an undiagnosed complex-V phenotype.

### Functional confirmation

Useful specialist assays include:

- spectrophotometric oligomycin-sensitive complex-V ATPase activity;
- ATP synthesis in permeabilized fibroblasts;
- oxygen-consumption rate/high-resolution respirometry;
- SDS-PAGE immunoblot and BN-PAGE for complex-V abundance/assembly;
- ATP5F1A immunostaining as a surrogate for intact complex V.

The defining profile is marked complex-V deficiency with relatively preserved complexes I–IV. The original patient had <10 mU/mg oligomycin-sensitive ATPase versus 43–190 in controls. (mayr2010mitochondrialatpsynthase pages 2-3, mayr2010mitochondrialatpsynthase pages 1-2)

Muscle biopsy is not mandatory when molecular and functional evidence is conclusive. No diagnostic histopathologic signature was established. No validated liquid-biopsy, metabolomic, proteomic or epigenomic clinical assay exists.

### Differential diagnosis

Key differentials include MT-ATP6/MT-ATP8 disease; TMEM70, ATPAF2, ATP5F1A, ATP5F1D, ATP5PO and ATP5MK-related complex-V disorders; other causes of secondary 3-methylglutaconic aciduria; pyruvate-dehydrogenase deficiency; respiratory-chain disorders; organic acidemias; and nonmitochondrial developmental epileptic or dystonia syndromes. Maternal transmission/heteroplasmy supports MT-ATP6 disease, whereas MC5DN3 shows biparental nuclear inheritance. MC5DN3 has so far been milder and lacked cardiomyopathy compared with many TMEM70 or severe structural complex-V deficiencies, but this distinction is not absolute. (tauchmannova2024variabilityofclinical pages 15-16, mayr2010mitochondrialatpsynthase pages 1-2)

There are no standardized MC5DN3 clinical criteria and no population newborn screen. Familial cascade testing is appropriate after molecular diagnosis.

## 11. Outcomes and prognosis

No survival curves, five- or ten-year survival rates, mortality rate, life-expectancy estimate or validated prognostic biomarker exists. All three published patients survived beyond infancy; one reached age 33. This suggests that p.Tyr12Cys can permit long-term survival, but it cannot define prognosis for other hypothetical ATP5F1E genotypes. (zech2022variantsinmitochondrial pages 7-8)

Morbidity is principally neurologic: persistent developmental/cognitive disability, ataxia, neuropathy, gait impairment, seizures, dystonia and occasional sensory impairment. Metabolic crises may diminish with age while neurologic disability persists or dystonia progresses. (zech2022variantsinmitochondrial pages 7-8, tauchmannova2024variabilityofclinical pages 15-16)

Potential adverse prognostic indicators—based on general mitochondrial medicine rather than validated MC5DN3 models—include recurrent metabolic crises, refractory epilepsy, progressive respiratory dysfunction, severe dysphagia, cardiomyopathy and loss of mobility. No molecular marker predicts course.

## 12. Treatment

### Disease-specific evidence

There is **no approved or demonstrated ATP5F1E-targeted treatment**, no published controlled trial, and no relevant registered interventional study identified by the ClinicalTrials.gov search. No response rate or adverse-event profile is available. Patient 2’s generalized dystonia responded poorly to unspecified medications. (zech2022variantsinmitochondrial pages 7-8, zech2022variantsinmitochondrial pages 10-11)

### Supportive management

Management should be multidisciplinary and phenotype-directed:

- acute metabolic illness: avoid prolonged fasting; provide hydration, glucose/calories as clinically appropriate, correct acid–base/electrolyte abnormalities, and promptly treat infection;
- epilepsy: standard antiseizure treatment individualized to seizure type and mitochondrial safety; the 2024 InterERN consensus provides general primary-mitochondrial-disease guidance, not MC5DN3-specific efficacy evidence;
- dystonia: individualized oral agents, botulinum toxin for focal components, and specialist movement-disorder assessment; evidence in MC5DN3 is anecdotal and poor;
- neuropathy/ataxia: physical and occupational therapy, gait aids, orthotics, fall prevention and neuropathic-pain management;
- developmental/sensory needs: speech/language therapy, educational support, audiology and ophthalmology;
- nutrition/swallowing: monitor growth, feeding safety and aspiration risk;
- surveillance: neurologic, respiratory, hearing, vision and metabolic follow-up; general mitochondrial guidance supports periodic ECG/echocardiography even when asymptomatic. (klopstock2021mitochondrialdisorders pages 2-3)

Routine “mitochondrial cocktails,” coenzyme Q10, riboflavin, thiamine, carnitine, antioxidants or ketogenic diet have no demonstrated MC5DN3 benefit. Supplement deficiencies when documented and use ketogenic therapy only for an appropriate specialist indication.

Suggested NCIT intervention concepts include Genetic Counseling, Physical Therapy, Occupational Therapy, Speech Therapy, Nutritional Support, Anticonvulsant Therapy, Botulinum Toxin Therapy, Hearing Assessment and Cardiac Monitoring; exact NCIT identifiers should be checked against the current release.

### Advanced/experimental therapies

No ATP5F1E gene replacement, gene editing, mRNA, antisense, cell or mitochondrial-transplant therapy has entered clinical testing for MC5DN3. Conceptually, nuclear-gene replacement is more tractable than editing mtDNA, but delivery to brain and peripheral nerve, dosage control and absence of validated models remain major barriers.

## 13. Prevention

There is no lifestyle or immunization strategy that prevents the genetic disorder.

- **Primary reproductive prevention:** genetic counseling; carrier testing of the reproductive partner/relatives; prenatal diagnosis by CVS or amniocentesis for known familial variants; and preimplantation genetic testing for monogenic disease.
- **Secondary prevention:** cascade testing can identify at-risk relatives or affected siblings early. Population or newborn screening is not available.
- **Tertiary prevention:** minimize fasting and promptly manage infection; monitor seizures, swallowing, mobility, hearing, vision, respiration and cardiac status; provide rehabilitation and adaptive support.

Because this is a nuclear autosomal-recessive disease, mitochondrial-replacement therapy designed to prevent maternal mtDNA transmission is **not applicable**.

## 14. Other species and natural disease

No naturally occurring ATP5F1E-related homologous disease in companion animals, livestock or wildlife was identified, and there is no zoonotic or cross-species transmission issue.

The ε subunit and its role in rotary ATP synthesis are evolutionarily conserved, but species differ importantly in complex-V biogenesis. Suggested taxonomy for the principal experimental model is **Saccharomyces cerevisiae, NCBI Taxon 4932**. Ortholog identifiers should be verified in NCBI Gene/Alliance before database loading.

## 15. Model organisms and experimental systems

### Human patient-derived cells

Primary skin fibroblasts are the most faithful available model. They reproduce the isolated loss of assembled complex V, reduced ATP synthesis, low oligomycin-sensitive ATPase activity, impaired ADP-stimulated respiration and altered subunit-c handling. Blood-cell ATP5F1A immunostaining also showed marked depletion in one patient. (zech2022variantsinmitochondrial pages 7-8, mayr2010mitochondrialatpsynthase pages 2-3, mayr2010mitochondrialatpsynthase pages 3-4)

No ATP5F1E patient-derived iPSC, neuron, organoid, CRISPR human-cell, mouse, rat, zebrafish, Drosophila or C. elegans disease model was identified through 2024.

### Yeast model

Sardin et al. introduced the orthologous **p.Tyr11Cys** change into S. cerevisiae. The mutant showed no significant defect in growth on nonfermentable carbon sources, ATP synthase activity or complex assembly/stability. The authors’ abstract states that the mutation’s “strong impact on the assembly of the ATP synthase complex in humans” had “no significant impact” in yeast, indicating biologically important species differences. (sardin2015biochemicalinvestigationof pages 1-2, sardin2015biochemicalinvestigationof pages 5-7)

The yeast model is useful for structural and comparative biogenesis questions but has poor face validity for the defining human assembly defect and is therefore inadequate as the sole preclinical efficacy model.

## Recent developments and expert assessment, 2023–2024

The most important recent disease-specific development is the August 2024 systematic review by Tauchmannová et al., which consolidated the three p.Tyr12Cys cases and emphasized their comparatively survivable, predominantly neurologic phenotype with later metabolic improvement and no reported cardiac involvement. It did not identify additional ATP5F1E patients or alleles. DOI: https://doi.org/10.33549/physiolres.935407. (tauchmannova2024variabilityofclinical pages 15-16)

A 2024 expert review framed dystonia as an increasingly recognized manifestation of ATP-synthase dysfunction and noted that movement disorders can become prominent after acute metabolic manifestations stabilize. This interpretation fits the MC5DN3 trajectories but is partly extrapolated from other ATP-synthase genes. DOI: https://doi.org/10.1002/mds.29657; published November 2024. (indelicato2024dystoniainatp pages 6-6, indelicato2024dystoniainatp pages 2-2)

The current expert interpretation is therefore cautious: ATP5F1E is a well-supported disease gene for isolated complex-V deficiency, and p.Tyr12Cys is functionally established, but the phenotypic spectrum, penetrance, population frequency, prognosis and treatability remain fundamentally uncertain because only three patients and one allele are known.

## Key source details and abstract quotations

1. **Mayr JA et al.** “Mitochondrial ATP synthase deficiency due to a mutation in the ATP5E gene for the F1 epsilon subunit.” *Human Molecular Genetics*. Advance publication **1 July 2010**; 19:3430–3439. DOI: https://doi.org/10.1093/hmg/ddq254. Abstract: “Here, we describe a patient with a homozygous p.Tyr12Cys mutation in the [epsilon] subunit encoded by the nuclear gene ATP5E.” It further reports that fibroblasts “showed 60–70% decrease in both oligomycin-sensitive ATPase activity and mitochondrial ATP synthesis.” (mayr2010mitochondrialatpsynthase pages 1-2)

2. **Zech M et al.** “Variants in Mitochondrial ATP Synthase Cause Variable Neurologic Phenotypes.” *Annals of Neurology*. **January 2022**; 91:225–237. DOI: https://doi.org/10.1002/ana.26293. The study identified three ATP5F1E patients with the same homozygous c.35A>G (p.Tyr12Cys) allele and documented the expanded neurologic spectrum and long-term follow-up. (zech2022variantsinmitochondrial pages 7-8)

3. **Sardin E et al.** “Biochemical investigation of a human pathogenic mutation in the nuclear ATP5E gene using yeast as a model.” *Frontiers in Genetics*. Published **23 April 2015**; 6:159. DOI: https://doi.org/10.3389/fgene.2015.00159. Abstract: the yeast-equivalent mutation had “no significant impact on the assembly/stability of this complex in yeast, suggesting that biogenesis of this complex differs significantly.” (sardin2015biochemicalinvestigationof pages 1-2)

4. **Tauchmannová K et al.** “Variability of Clinical Phenotypes Caused by Isolated Defects of Mitochondrial ATP Synthase.” *Physiological Research*. **August 2024**; 73(Suppl 1):S243–S278. DOI: https://doi.org/10.33549/physiolres.935407. This is the most recent comprehensive disease-family review located and confirms the three-case ATP5F1E evidence base. (tauchmannova2024variabilityofclinical pages 15-16)

## Knowledge-base curation cautions

1. Do not merge this entity with MT-ATP6-associated NARP/Leigh disease, ATP5F1A/ATP5F1D/ATP5PO/TMEM70 disease, or combined OXPHOS deficiency.
2. Record frequencies as **n/3 published patients**, with a prominent small-denominator warning.
3. Treat p.Tyr12Cys as an assembly/stability hypomorph supported by human-cell evidence; do not describe it as a proven catalytic-null allele.
4. Mark ROS injury, cell-type selectivity, and exact mutant-protein degradation/import mechanisms as inferred.
5. Record no disease-specific prevalence, standardized criteria, validated biomarker, targeted treatment, vertebrate model or clinical trial as available through the searched 2024 literature.

References

1. (zech2022variantsinmitochondrial pages 7-8): Michael Zech, Robert Kopajtich, Katja Steinbrücker, Céline Bris, Naig Gueguen, René G. Feichtinger, Melanie T. Achleitner, Neslihan Duzkale, Maximilien Périvier, Johannes Koch, Harald Engelhardt, Peter Freisinger, Matias Wagner, Theresa Brunet, Riccardo Berutti, Dmitrii Smirnov, Tharsini Navaratnarajah, Richard J.T. Rodenburg, Lynn S Pais, Christina Austin‐Tse, Melanie O'Leary, Sylvia Boesch, Robert Jech, Somayeh Bakhtiari, Sheng Chih Jin, Friederike Wilbert, Michael C Kruer, Saskia B. Wortmann, Matthias Eckenweiler, Johannes A. Mayr, Felix Distelmaier, Robert Steinfeld, Juliane Winkelmann, and Holger Prokisch. Variants in mitochondrial <scp>atp</scp> synthase cause variable neurologic phenotypes. Jan 2022. URL: https://doi.org/10.1002/ana.26293, doi:10.1002/ana.26293. This article has 58 citations and is from a highest quality peer-reviewed journal.

2. (tauchmannova2024variabilityofclinical pages 15-16): K. Tauchmannová, A. Pecinová, J. Houštěk, and T. Mrázek. Variability of clinical phenotypes caused by isolated defects of mitochondrial atp synthase. Aug 2024. URL: https://doi.org/10.33549/physiolres.935407, doi:10.33549/physiolres.935407. This article has 18 citations and is from a peer-reviewed journal.

3. (mayr2010mitochondrialatpsynthase pages 1-2): J. A. Mayr, V. Havlickova, F. Zimmermann, I. Magler, V. Kaplanova, P. Jesina, A. Pecinova, H. Nuskova, J. Koch, W. Sperl, and J. Houstek. Mitochondrial atp synthase deficiency due to a mutation in the atp5e gene for the f1 epsilon subunit. Human molecular genetics, 19 17:3430-9, Sep 2010. URL: https://doi.org/10.1093/hmg/ddq254, doi:10.1093/hmg/ddq254. This article has 193 citations and is from a domain leading peer-reviewed journal.

4. (mayr2010mitochondrialatpsynthase pages 2-3): J. A. Mayr, V. Havlickova, F. Zimmermann, I. Magler, V. Kaplanova, P. Jesina, A. Pecinova, H. Nuskova, J. Koch, W. Sperl, and J. Houstek. Mitochondrial atp synthase deficiency due to a mutation in the atp5e gene for the f1 epsilon subunit. Human molecular genetics, 19 17:3430-9, Sep 2010. URL: https://doi.org/10.1093/hmg/ddq254, doi:10.1093/hmg/ddq254. This article has 193 citations and is from a domain leading peer-reviewed journal.

5. (mayr2010mitochondrialatpsynthase pages 3-4): J. A. Mayr, V. Havlickova, F. Zimmermann, I. Magler, V. Kaplanova, P. Jesina, A. Pecinova, H. Nuskova, J. Koch, W. Sperl, and J. Houstek. Mitochondrial atp synthase deficiency due to a mutation in the atp5e gene for the f1 epsilon subunit. Human molecular genetics, 19 17:3430-9, Sep 2010. URL: https://doi.org/10.1093/hmg/ddq254, doi:10.1093/hmg/ddq254. This article has 193 citations and is from a domain leading peer-reviewed journal.

6. (sardin2015biochemicalinvestigationof pages 1-2): Elodie Sardin, Stéphanie Donadello, Jean-Paul di Rago, and Emmanuel Tetaud. Biochemical investigation of a human pathogenic mutation in the nuclear atp5e gene using yeast as a model. Frontiers in Genetics, Apr 2015. URL: https://doi.org/10.3389/fgene.2015.00159, doi:10.3389/fgene.2015.00159. This article has 4 citations and is from a peer-reviewed journal.

7. (sardin2015biochemicalinvestigationof pages 5-7): Elodie Sardin, Stéphanie Donadello, Jean-Paul di Rago, and Emmanuel Tetaud. Biochemical investigation of a human pathogenic mutation in the nuclear atp5e gene using yeast as a model. Frontiers in Genetics, Apr 2015. URL: https://doi.org/10.3389/fgene.2015.00159, doi:10.3389/fgene.2015.00159. This article has 4 citations and is from a peer-reviewed journal.

8. (zech2022variantsinmitochondrial pages 10-11): Michael Zech, Robert Kopajtich, Katja Steinbrücker, Céline Bris, Naig Gueguen, René G. Feichtinger, Melanie T. Achleitner, Neslihan Duzkale, Maximilien Périvier, Johannes Koch, Harald Engelhardt, Peter Freisinger, Matias Wagner, Theresa Brunet, Riccardo Berutti, Dmitrii Smirnov, Tharsini Navaratnarajah, Richard J.T. Rodenburg, Lynn S Pais, Christina Austin‐Tse, Melanie O'Leary, Sylvia Boesch, Robert Jech, Somayeh Bakhtiari, Sheng Chih Jin, Friederike Wilbert, Michael C Kruer, Saskia B. Wortmann, Matthias Eckenweiler, Johannes A. Mayr, Felix Distelmaier, Robert Steinfeld, Juliane Winkelmann, and Holger Prokisch. Variants in mitochondrial <scp>atp</scp> synthase cause variable neurologic phenotypes. Jan 2022. URL: https://doi.org/10.1002/ana.26293, doi:10.1002/ana.26293. This article has 58 citations and is from a highest quality peer-reviewed journal.

9. (klopstock2021mitochondrialdisorders pages 2-3): Thomas Klopstock, Claudia Priglinger, Ali Yilmaz, Cornelia Kornblum, Felix Distelmaier, and Holger Prokisch. Mitochondrial disorders. Nov 2021. URL: https://doi.org/10.3238/arztebl.m2021.0251, doi:10.3238/arztebl.m2021.0251. This article has 81 citations.

10. (indelicato2024dystoniainatp pages 6-6): Elisabetta Indelicato, Sylvia Boesch, Niccolo' E. Mencacci, Daniele Ghezzi, Holger Prokisch, Juliane Winkelmann, and Michael Zech. Dystonia in atp synthase defects: reconnecting mitochondria and dopamine. Movement Disorders, 39:29-35, Nov 2024. URL: https://doi.org/10.1002/mds.29657, doi:10.1002/mds.29657. This article has 7 citations and is from a highest quality peer-reviewed journal.

11. (indelicato2024dystoniainatp pages 2-2): Elisabetta Indelicato, Sylvia Boesch, Niccolo' E. Mencacci, Daniele Ghezzi, Holger Prokisch, Juliane Winkelmann, and Michael Zech. Dystonia in atp synthase defects: reconnecting mitochondria and dopamine. Movement Disorders, 39:29-35, Nov 2024. URL: https://doi.org/10.1002/mds.29657, doi:10.1002/mds.29657. This article has 7 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Mitochondrial_Complex_V_ATP_Synthase_Deficiency_Nuclear_Type_3-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013547` (2 mentions) - the report calls it "if available"; MONDO calls it **mitochondrial complex V (ATP synthase) deficiency, nuclear type 3**
- `CL:0000540` (1 mention) - the report calls it "Candidate affected cell types:** neuron"; CL calls it **neuron**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005753` (obsolete mitochondrial proton-transporting ATP synthase complex) (1 mention) - replaced by `GO:0045259`
- `GO:0000275` (obsolete mitochondrial proton-transporting ATP synthase complex, catalytic sector F(1)) (1 mention) - replaced by `GO:0045259`