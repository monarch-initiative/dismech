---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-24T13:23:22.500418'
end_time: '2026-08-24T13:27:31.236376'
duration_seconds: 248.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Short Stature, Amelogenesis Imperfecta, and Skeletal Dysplasia with
    Scoliosis
  mondo_id: ''
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
  web_search_requests: 13
  num_turns: 22
  total_cost_usd: 1.5449382
  session_id: d5430dc8-cc9c-5a8f-9365-64cb735827c4
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 14
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 8
  on_topic: 8
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Short Stature, Amelogenesis Imperfecta, and Skeletal Dysplasia with Scoliosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Short Stature, Amelogenesis Imperfecta, and Skeletal Dysplasia with Scoliosis** covering all of the
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

I'll research this rare Mendelian disorder using web search and fetch tools to gather primary literature.

This disease (SSASKS, OMIM #618363) is caused by **SLC10A7**, not LTBP3 — a related but distinct LTBP3 disorder exists separately. Let me pull the primary sources on SLC10A7.

Now I have comprehensive data. Compiling the full research report.

# Short Stature, Amelogenesis Imperfecta, and Skeletal Dysplasia with Scoliosis (SSASKS)

## 1. Disease Information

**Overview:** Short Stature, Amelogenesis Imperfecta, and Skeletal Dysplasia with Scoliosis (SSASKS) is an ultra-rare autosomal recessive skeletal dysplasia first delineated in 2018. It is caused by biallelic loss-of-function variants in **SLC10A7**, encoding an orphan 10-transmembrane-domain Golgi/plasma-membrane transporter previously of unknown function. The disorder begins with pre- and postnatal growth failure and evolves into a multisystem phenotype dominated by disproportionate short stature, hypomineralized/hypoplastic amelogenesis imperfecta, progressive skeletal dysplasia with large-joint dislocations, and severe scoliosis, with variable facial dysmorphism, hearing impairment, and mild intellectual disability ([Nature Communications 2018](https://www.nature.com/articles/s41467-018-05191-8); [OMIM #618363](https://www.omim.org/entry/618363)).

Mechanistically it is classified as a **congenital disorder of glycosylation (CDG)** — specifically "SLC10A7-CDG" — because loss of SLC10A7 disrupts Golgi calcium homeostasis, downstream glycosyltransferase activity, glycosaminoglycan (GAG)/proteoglycan biosynthesis, and post-Golgi glycoprotein trafficking, converging on a phenotype affecting bone, cartilage, and tooth enamel ([PMID:34999954](https://pubmed.ncbi.nlm.nih.gov/34999954/)).

**Key identifiers:**
- **OMIM:** #618363 (phenotype, SSASKS); *611459 (gene, SLC10A7)
- **Gene:** SLC10A7 (HGNC:23088), chromosome 4q31.21
- **Inheritance:** Autosomal recessive
- **Suggested MONDO term:** MONDO entity mapping to OMIM 618363 (curator should verify the exact MONDO CURIE via OLS/Monarch, as searches did not return a definitive standalone MONDO number distinct from the OMIM cross-reference)
- **Also known as:** SLC10A7-related skeletal dysplasia; SLC10A7-CDG; "skeletal dysplasia with amelogenesis imperfecta mediated by GAG biosynthesis defects" (descriptive name from the founding paper)

**Evidence base:** This is a very rare, literature-derived (aggregated case-series) knowledge base — not EHR-derived. Only **~12–13 patients** have been reported worldwide as of the most recent case report (2023), spanning six original families (Turkish, Iranian, Dutch) in the 2018 founding paper, plus subsequent single-family reports from France, Netherlands, and China ([PMC10691085](https://pmc.ncbi.nlm.nih.gov/articles/PMC10691085/)).

---

## 2. Etiology

**Disease Causal Factors:** SSASKS is purely genetic/monogenic — biallelic (homozygous or compound heterozygous) pathogenic variants in **SLC10A7**. No environmental, infectious, or acquired causal factors have been reported.

**Genetic risk factors:**
- **Consanguinity** is a major risk factor: the founding cohort included four families from consanguineous unions in Turkey and Iran, plus two distantly related Dutch families ([PMID:30082715](https://pubmed.ncbi.nlm.nih.gov/30082715/)).
- **Variant spectrum identified to date:**
  - Two splice-site mutations (exons 9–10)
  - Missense: p.Leu74Pro (exon 3), p.Gly130Arg (exon 4), p.Pro303Leu (exon 11 — associated with a milder phenotype; [PMID:31191616](https://pubmed.ncbi.nlm.nih.gov/31191616/))
  - Nonsense: p.Gln172* (exon 7); p.Gly34* (exon 1, novel, first reported in a Han Chinese patient; [PMC10691085](https://pmc.ncbi.nlm.nih.gov/articles/PMC10691085/))
  - Functional studies confirm these variants reduce SLC10A7 protein expression/stability at the plasma membrane and Golgi.
- **Genotype–phenotype correlation:** The p.Pro303Leu missense variant, located near the C-terminus, is associated with a milder skeletal phenotype (growth retardation of −3SD vs. −4 to −10SD in other cases, absence of multiple joint dislocations), suggesting variant position and residual protein function modulate severity ([PMC6546871](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6546871/)).

**Environmental/other risk factors:** None established; the disease is fully genetically determined.

**Protective factors:** None reported in the literature.

**Gene-environment interactions:** Not applicable/not studied — no evidence of environmental modulation of expressivity.

---

## 3. Phenotypes

### Skeletal/Growth (onset: prenatal/congenital, progressive)
- **Disproportionate short stature** — the cardinal feature, present in ~95% of reported cases, with birth length often <−3 SD and adult/childhood heights ranging from −3SD to as severe as −10SD in some patients. Suggested term: **HP:0004322** (Short stature)
- **Multiple large-joint dislocations** with a characteristic "monkey wrench"/"Swedish key" femoral head appearance (radiographically shared with Desbuquois dysplasia) — HP:0001373 (Joint dislocation)
- **Advanced carpal/tarsal bone ossification** — HP:0006247
- **Platyspondyly/abnormal vertebral bodies** — HP:0000926
- **Progressive scoliosis/kyphoscoliosis**, present in ~80% of cases, often severe and requiring surgical intervention — HP:0002650 (Scoliosis)
- **Genu valgum, short long bones, small epiphyses, horizontal acetabula** — HP:0002857, HP:0003026
- **Brachydactyly and progressive joint contractures** in some patients — HP:0001156

### Dental (essentially fully penetrant — 100%)
- **Amelogenesis imperfecta**, hypoplastic/hypomineralized type — thin (~80 μm vs. ~700 μm control), yellow-brown, rough-surfaced enamel — HP:0000705 (Abnormality of dental enamel) / HP:0009805 (hypoplastic amelogenesis imperfecta)
- **Delayed tooth eruption** (91.6%) — HP:0000684
- **Oligodontia/hypodontia/tooth agenesis** (88%) — HP:0000696

### Craniofacial
- **Facial dysmorphism** — flat face, micro/retrognathia, microretrognathia, Pierre-Robin sequence in some cases — HP:0000271
- Ptosis, in individual case reports — HP:0000508

### Sensory/Neurologic
- **Moderate bilateral hearing impairment** in a subset of patients — HP:0000407
- **Mild intellectual disability/learning difficulties** — variable, not universal — HP:0001256
- **Optic nerve atrophy** reported in at least one case — HP:0000648

### Other
- **Cardiac defects** — aortic sinus dilation, patent foramen ovale reported in individual patients — HP:0004942
- **Obesity** noted in older patients in the founding cohort
- **Whole-body edema** (in the zebrafish model correlate; not consistently reported in humans)

**Quality of life impact:** Not formally studied with validated instruments (EQ-5D/SF-36); qualitatively, the disease imposes major cumulative burden from repeated orthopedic surgeries (documented case: 7 surgeries over 12 years for scoliosis management), chronic joint instability, and dental rehabilitation needs.

---

## 4. Genetic/Molecular Information

- **Causal gene:** SLC10A7 (HGNC:23088, OMIM *611459), chromosome 4q31.21, encoding a 10-transmembrane-domain protein of the SLC10 (sodium/bile acid cotransporter) family. Despite structural homology to bile-acid transporters, SLC10A7 shows **no transport activity for canonical SLC10 substrates** and is classified as an "orphan carrier" ([PMID:34999954](https://pubmed.ncbi.nlm.nih.gov/34999954/)).
- **Variant classification:** All reported variants are biallelic loss-of-function or hypomorphic (missense) — consistent with **ACMG pathogenic/likely pathogenic** — no VUS controversies reported to date given the small case series and strong functional validation.
- **Variant types:** Missense (p.Leu74Pro, p.Gly130Arg, p.Pro303Leu), nonsense (p.Gln172*, p.Gly34*), splice-site (exons 9–10).
- **Allele frequency:** Given the ultra-rare presentation (~12–13 reported cases worldwide, primarily from consanguineous unions), population database (gnomAD) frequencies for specific pathogenic alleles are expected to be exceedingly low or absent (no specific data returned in this search — should be verified directly in gnomAD/ClinVar during curation).
- **Somatic vs. germline:** Germline only — a classic recessive Mendelian disorder.
- **Functional consequences:** Loss-of-function/reduced protein expression at the Golgi/plasma membrane, leading to:
  1. Dysregulated **intracellular (Golgi) calcium homeostasis** — patient fibroblasts show significantly increased Ca²⁺ influx upon calcium challenge, and SLC10A7 has been separately characterized as "a novel negative regulator of intracellular calcium signaling" ([PMID:32350310](https://pubmed.ncbi.nlm.nih.gov/32350310/))
  2. Reduced **heparan sulfate (GAG) biosynthesis** (~2–2.5-fold reduction in Slc10a7−/− mouse cartilage and patient fibroblasts), with total GAG preserved via compensatory chondroitin sulfate synthesis
  3. Abnormal **N-glycosylation** — increased high-mannose glycans, glycans lacking GlcNAc, and decreased sialylated glycans on plasma glycoproteins (e.g., transferrin), plus mislocalized/defective post-Golgi glycoprotein transport ([PMC10691085](https://pmc.ncbi.nlm.nih.gov/articles/PMC10691085/); [HMG 2018, Ashikov et al.](https://academic.oup.com/hmg/article/27/17/3029/5033379))
- **Modifier genes:** None identified.
- **Epigenetic information:** Not studied for this disorder.
- **Chromosomal abnormalities:** Not applicable — point/splice-site variants only, no reported CNVs.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors have been identified or are biologically plausible given the purely monogenic glycosylation/transporter mechanism. Not applicable to this entry.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Trigger (molecular scale):** Biallelic SLC10A7 loss-of-function variant → loss/reduction of functional SLC10A7 transporter at the Golgi and plasma membrane.
2. **Golgi calcium dysregulation:** SLC10A7 normally regulates intracellular (Golgi-lumen) Ca²⁺ homeostasis; its loss causes increased cytosolic/ER-store Ca²⁺ influx in patient fibroblasts. Suggested GO term: **GO:0051480** (regulation of cytosolic calcium ion concentration); **GO:0032468** (Golgi calcium ion homeostasis).
3. **Downstream glycosylation defect:** Golgi Ca²⁺ dysregulation impairs Ca²⁺-dependent glycosyltransferase activity, producing:
   - **Congenital disorder of glycosylation (CDG) signature** — abnormal N-glycan profiles on serum glycoproteins (increased high-mannose species, decreased sialylation) — GO:0006486 (protein glycosylation)
   - **Reduced heparan sulfate GAG chain synthesis** on proteoglycans in cartilage and fibroblasts — GO:0015012 (heparan sulfate proteoglycan biosynthetic process)
   - **Defective post-Golgi trafficking** of glycoproteins/proteoglycans to the extracellular matrix — GO:0006891 (intra-Golgi vesicle-mediated transport)
4. **Tissue-level consequences (cellular/tissue scale):**
   - **Growth plate chondrocyte disorganization** — thinned growth plates, disorganized proliferative/hypertrophic zones, reduced Safranin O (sulfated GAG) staining in Slc10a7−/− mouse cartilage
   - **Ameloblast dysfunction** — missing aprismatic enamel layer, enamel hypoplasia, due to disrupted secretory-pathway glycoprotein trafficking in ameloblasts
   - **Osteoblast/matrix mineralization defect** — zebrafish slc10a7 morphants show near-absent bone mineralization (Alizarin red staining), implicating a role in extracellular matrix mineralization via proteoglycan/glycoprotein delivery
5. **Organismal-level phenotype:** Growth plate and enamel matrix disruption → disproportionate short stature, brachyolmia-type skeletal dysplasia, joint laxity/dislocation (proteoglycan-dependent cartilage/ligament integrity), and amelogenesis imperfecta; spinal deformity progresses to severe scoliosis.

**Cell types involved:** Growth-plate chondrocytes (CL:0000138 chondrocyte), ameloblasts (CL:0000414), osteoblasts (CL:0000062), dermal fibroblasts (CL:0000057, used as the patient-derived disease model).

**Molecular profiling evidence:**
- **Glycomics:** Abnormal serum/plasma N-glycan and O-glycan profiles in patients (isoelectric focusing of transferrin showing hypoglycosylation pattern consistent with CDG type II).
- No transcriptomic, proteomic, or single-cell datasets specific to this ultra-rare disease were identified in this search; the mechanistic work has been carried out primarily via targeted biochemical assays (Ca²⁺ imaging, GAG quantification, glycan mass spectrometry) in patient fibroblasts and animal models rather than omics screens.

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- Skeletal system (primary) — long bones, vertebral column, joints, cranium (UBERON:0001434 skeletal system)
- Dentition — tooth enamel specifically (UBERON:0001754 tooth enamel)
- Craniofacial skeleton (UBERON:0001456)
- Auditory system (secondary — hearing impairment) (UBERON:0001690 ear)
- Cardiovascular system (secondary, in some patients — aortic root/valve) (UBERON:0002012 aorta)
- Central nervous system (secondary — optic nerve, mild cognitive involvement) (UBERON:0001784 optic nerve)

**Tissue/cell level:**
- Growth-plate cartilage (UBERON:0002514 epiphyseal cartilage) — chondrocytes (CL:0000138)
- Enamel organ/ameloblasts (CL:0000414)
- Bone matrix/osteoblasts (CL:0000062)
- Synovial joint capsule/ligament — connective tissue affected by GAG deficiency (UBERON:0000982 ligament)

**Subcellular level:**
- **Golgi apparatus** (GO:0005794) — primary site of SLC10A7 localization and dysfunction
- Plasma membrane (GO:0005886) — SLC10A7's other reported localization
- Secretory pathway vesicles (GO:0030133)

**Localization:** Bilateral/symmetric skeletal involvement; scoliosis typically thoracolumbar; dental involvement affects both primary and permanent dentition diffusely.

---

## 8. Temporal Development

- **Onset:** Congenital/prenatal — growth restriction is detectable pre- and postnatally (birth length often <−3SD; one reported case had birth height of 42 cm). Amelogenesis imperfecta is evident with primary tooth eruption.
- **Onset pattern:** Insidious, with progressive worsening through childhood.
- **Progression:** Skeletal dysplasia and scoliosis are **progressive** — the documented surgical case shows scoliosis requiring intervention beginning at age 3.5 years and continuing through age 14.2 years (growth-rod placement → lengthening procedures → dual-rod conversion → definitive fusion). Joint contractures are also described as progressive.
- **Disease course pattern:** Chronic, progressive, non-relapsing/non-remitting (no spontaneous remission reported).
- **Critical periods:** Early childhood is a critical intervention window for scoliosis management (growth-friendly rod systems) to preserve spinal/thoracic growth before definitive fusion at skeletal maturity.
- **Disease duration:** Lifelong; no evidence this is self-limited. Life expectancy has not been formally quantified in the literature but no early mortality has been reported in the ~12 documented cases.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** Ultra-rare; only ~12–13 cases described in the world literature to date across 3 primary publications (2018 founding cohort of 6 patients from 4 families; 2019 single French case; 2023 single Chinese case), plus at least one additional 2021 case (splicing variant, brachyolmia with AI). No formal prevalence estimate (e.g., per 100,000) has been published — likely falls in the "<1/1,000,000" (ultra-rare) band.
- **Incidence:** Not calculable given the extremely small reported case count.

**Inheritance pattern:** Autosomal recessive (AR).
**Penetrance:** Appears complete for the core triad (short stature, AI, skeletal dysplasia) among reported homozygous/compound heterozygous individuals, though severity is variable.
**Expressivity:** Variable — genotype-correlated (e.g., the p.Pro303Leu missense case showed a substantially milder skeletal phenotype than nonsense/splice-site cases).
**Founder effects:** Multiple independent founder-type events plausible given consanguineous Turkish and Iranian families in the original cohort, plus two distantly related Dutch families sharing ancestry.
**Consanguinity:** A major contributing factor — 4 of the 6 original index families were from consanguineous unions.
**Carrier frequency:** Not established (too rare for population-level carrier frequency data).

**Population demographics:**
- Cases reported from Turkey, Iran, the Netherlands, France, and China — no clear single ethnic predominance, consistent with a pan-ethnic ultra-rare AR disorder that surfaces preferentially in consanguineous populations.
- **Sex ratio:** No skewing reported (autosomal gene).
- **Age distribution:** All reported cases are pediatric/adolescent at diagnosis given the congenital onset.

---

## 10. Diagnostics

**Clinical tests:**
- **Imaging (primary diagnostic modality):** Skeletal radiographic survey showing platyspondyly, "Swedish key"/monkey-wrench femoral heads, advanced carpal/tarsal bone age, multiple large-joint dislocations, and progressive scoliosis on spine films. Suggested RadLex/imaging term: skeletal survey for skeletal dysplasia.
- **Dental examination:** Clinical and radiographic assessment of enamel thickness/mineralization (enamel ~80 μm vs. ~700 μm normal in one measured case).
- **Biochemical/glycomics:** Serum transferrin isoelectric focusing / N-glycan mass spectrometry showing a CDG type II-like abnormal glycosylation pattern (increased high-mannose glycans, decreased sialylation) — a distinguishing biomarker supporting the CDG mechanism.
- **Audiometry:** For hearing impairment assessment.
- **Ophthalmologic exam:** For optic nerve atrophy screening in symptomatic patients.
- **Echocardiography:** To screen for aortic root dilation/cardiac anomalies given at least one reported case with aortic sinus dilation and PFO.

**Genetic testing:**
- **Gene panel/exome sequencing** is the diagnostic approach of choice — all reported cases were solved via whole-exome sequencing given the absence of a prior clinical gestalt pointing specifically to SLC10A7 (initial presentations often resembled Desbuquois dysplasia or other multiple-dislocation skeletal dysplasias).
- **Single-gene Sanger confirmation** of SLC10A7 variants in proband and segregation testing in parents (both heterozygous carriers in consanguineous families) is standard follow-up.
- No chromosomal microarray, karyotype, or mitochondrial DNA testing is relevant (single-gene AR point/splice variants only).

**Clinical/differential diagnosis:** Because the "monkey wrench"/"Swedish key" femoral appearance and advanced carpal ossification overlap radiographically with the **Desbuquois dysplasia spectrum** (multiple-dislocation group of chondrodysplasias, itself associated with CANT1 and XYLT1 — also glycosylation/proteoglycan pathway genes), SSASKS should be differentiated from:
- Desbuquois dysplasia 1/2 (CANT1, XYLT1) — OMIM #251450
- Geleophysic dysplasia (ADAMTSL2, FBN1, LTBP3) — a related but molecularly and phenotypically distinct entity
- LTBP3-related "Dental Anomalies and Short Stature" (DASS, OMIM #601216) — **an important, easily confused related disorder**: LTBP3 biallelic variants cause brachyolmia with amelogenesis imperfecta and short stature, with cardiovascular complications (aortic aneurysm, mitral valve prolapse) as a more prominent feature; distinguishing molecular testing is essential since clinical overlap (short stature + AI + skeletal dysplasia + scoliosis) is substantial.
- Other multiple-dislocation/AI-associated dysplasias.

**The single most consistent distinguishing clinical clue** across the literature is: "AI is the key feature indicative of SLC10A7 mutations in patients with skeletal dysplasia" — i.e., near-100% penetrant, severe hypomineralized amelogenesis imperfecta in combination with a multiple-dislocation skeletal dysplasia should trigger SLC10A7 testing ([PMC6546871](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6546871/)).

**Screening:** No population or newborn screening program exists (or is warranted) given the ultra-rare frequency; diagnosis is case-by-case via clinical suspicion + exome sequencing.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No deaths have been reported among the ~12–13 documented cases; formal survival statistics do not exist given the small numbers.
- **Morbidity:** Substantial — driven by progressive scoliosis (requiring multi-stage surgical correction across childhood/adolescence), joint dislocations/contractures affecting mobility, and dental rehabilitation needs due to severe enamel loss.
- **Disease course:** Chronic and progressive through childhood; the well-documented surgical case achieved a favorable final Cobb angle (16.3°) after a 12-year, 7-surgery growth-friendly-rod-to-fusion protocol, suggesting that with aggressive orthopedic management, functional spinal outcomes can be reasonably favorable.
- **Complications:** Progressive scoliosis, chronic joint instability/dislocation, hearing loss, dental complications (oligodontia, enamel loss requiring restorative dentistry), and in a subset, cardiac (aortic root dilation) and ophthalmologic (optic atrophy) complications.
- **Prognostic factors:** Variant type/location appears prognostic — missense variants near the C-terminus (e.g., p.Pro303Leu) are associated with a milder phenotype than nonsense/splice-site null alleles, which produce more severe growth failure and more extensive joint dislocation.
- **Quality of life:** Not formally measured with validated QOL instruments in the literature to date.

---

## 12. Treatment

There is **no disease-modifying or gene-specific therapy** for SSASKS/SLC10A7-CDG; management is entirely symptomatic/supportive and multidisciplinary.

**Surgical/interventional (primary management for the skeletal phenotype):**
- **Growth-friendly spinal instrumentation** (single-side growth rods progressing to dual-rod systems with expanded screw fixation) for progressive early-onset scoliosis, followed by **definitive spinal fusion** at skeletal maturity — documented in detail in the 2023 case report (7 procedures over 12 years, from age 3.5 to 14.2 years). Suggested NCIT term: NCIT:C15329 (Surgical Procedure); more specifically, spinal fusion/instrumentation.
- **Orthopedic management of large-joint dislocations** (surveillance, bracing, and surgical reduction/stabilization as needed) — NCIT:C16186 (Orthopedic Surgical Procedure).

**Dental/restorative:**
- **Restorative dental care for amelogenesis imperfecta** — crowns, restorative bonding, or prosthodontic rehabilitation for severely hypomineralized/hypoplastic enamel; management of oligodontia (implants/prosthetics) — NCIT:C15329 (Surgical/dental procedure) as broad category; no specific NCIT dental-restoration term identified in this search.

**Supportive care:**
- **Audiologic support** (hearing aids) for moderate hearing impairment — NCIT:C15747 (Supportive Care).
- **Physical/occupational therapy** for joint contractures and mobility — NCIT:C15302 (Physical Therapy).
- **Cardiology follow-up** (echocardiographic surveillance) for patients with aortic root involvement.
- **Genetic counseling** for affected families, given AR inheritance and elevated recurrence risk (25%) in future pregnancies, particularly relevant in consanguineous populations — NCIT:C15240 (Genetic Counseling).

**Experimental/pharmacotherapy:** No clinical trials (ClinicalTrials.gov) or investigational drug therapies specific to SLC10A7-CDG were identified in this search. Given the CDG mechanism (defective glycosylation via Golgi Ca²⁺ dysregulation), this disorder is mechanistically distinct from the classical PMM2-CDG/mannose-supplementation-responsive CDGs, and no analogous small-molecule or dietary intervention has been proposed in the literature reviewed.

**Treatment outcomes:** The single well-documented surgical case achieved good radiographic correction (final Cobb angle 16.3°) with "no implant complications," suggesting growth-friendly instrumentation is an effective, if burdensome, strategy for the scoliosis component.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the population sense; the only actionable prevention lever is **genetic counseling and carrier testing** in families with a known proband, particularly in consanguineous populations, to inform reproductive decision-making (prenatal diagnosis or preimplantation genetic testing for known familial SLC10A7 variants).
- **Secondary prevention:** Early clinical recognition (short stature + amelogenesis imperfecta + skeletal dysplasia triad) followed by prompt genetic diagnosis can enable earlier orthopedic surveillance and growth-friendly spinal intervention before scoliosis becomes severe.
- **Tertiary prevention:** Multidisciplinary surveillance (orthopedic, dental, audiologic, cardiac, ophthalmologic) to detect and manage complications early.
- **Screening:** No population-level newborn or carrier screening program exists given the extreme rarity; cascade testing within affected families is the practical approach.
- **Public health/environmental interventions:** Not applicable — purely monogenic disorder with no environmental modifiers.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary cases of SLC10A7-related disease have been reported in companion animals or wildlife (this appears to be an engineered/induced model space only — see Model Organisms below). No OMIA (Online Mendelian Inheritance in Animals) entries or veterinary case series were identified in this search.

---

## 15. Model Organisms

### Mouse (Slc10a7−/−)
- **Type:** Genetic knockout, constitutive.
- **Phenotype recapitulation — high fidelity:**
  - Shortened long bones and growth retardation (measurable at birth and at 8 weeks)
  - Growth plate disorganization: markedly thinned growth plates with disorganized proliferative/hypertrophic chondrocyte zones
  - Altered long-bone morphology matching the human "Swedish key" femoral appearance
  - Tooth enamel anomalies including missing aprismatic enamel layer and enamel hypoplasia
  - Reduced Safranin O staining (decreased sulfated GAG content) in cartilage, mechanistically linking to the ~2–2.5-fold reduction in heparan sulfate measured biochemically
  - Source: [PMID:30082715](https://pubmed.ncbi.nlm.nih.gov/30082715/) (Dubail et al., Nature Communications 2018)
- **Limitations:** Not explicitly detailed in the sources reviewed, but as a constitutive null it cannot dissect tissue-specific/temporal requirements for SLC10A7.

### Zebrafish (slc10a7 morpholino knockdown)
- **Type:** Morpholino-based transient knockdown (induced model).
- **Phenotype:**
  - Dose-dependent severity: low-dose morpholino → mild skeletal/craniofacial defects; high-dose (12 ng/nl) → severe phenotype with whole-body edema, reduced head/eye size, curled body
  - Cartilage/craniofacial malformation (bent-down jaw cartilage) on Alcian blue staining
  - Near-absent bone mineralization on Alizarin red staining at high knockdown doses
  - Source: [Ashikov et al., Human Molecular Genetics 2018](https://academic.oup.com/hmg/article/27/17/3029/5033379) — "Integrating glycomics and genomics uncovers SLC10A7 as essential factor for bone mineralization by regulating post-Golgi protein transport and glycosylation"
- **Applications:** Used to functionally validate patient-derived variants and to study the glycosylation/bone-mineralization mechanism in vivo.
- **Limitations:** Morpholino knockdown is transient/dose-dependent rather than a stable genetic model, and severe phenotypes (edema, curled body) may reflect broader developmental toxicity beyond the specific human skeletal/dental phenotype.

### Patient-derived fibroblasts (in vitro, human)
- Used extensively to demonstrate increased Ca²⁺ influx upon calcium challenge, reduced heparan sulfate synthesis, and abnormal N-glycan profiles — directly bridging the mouse/zebrafish mechanistic data to human disease biology.

**Resource note:** No entries for SLC10A7 knockout mice were located in this search under standard identifiers (MGI, IMPC) — the model described in Dubail et al. 2018 appears to be a custom-generated line rather than a repository-deposited allele; this should be confirmed against MGI/IMPC directly during curation.

---

## Summary of Key Ontology Term Suggestions for Curation

| Category | Suggested term |
|---|---|
| Disease | OMIM:618363; Gene OMIM:611459 (SLC10A7) |
| Gene | hgnc:23088 (SLC10A7) |
| Phenotypes | HP:0004322 (Short stature), HP:0009805/HP:0000705 (Amelogenesis imperfecta/enamel abnormality), HP:0002650 (Scoliosis), HP:0001373 (Joint dislocation), HP:0000684 (Delayed eruption of teeth), HP:0000696 (Oligodontia), HP:0000407 (Hearing impairment), HP:0001256 (Intellectual disability, mild), HP:0000271 (Facial dysmorphism), HP:0000926 (Abnormal vertebral morphology) |
| Biological processes (GO) | GO:0051480 (regulation of cytosolic Ca²⁺), GO:0006486 (protein glycosylation), GO:0015012 (heparan sulfate proteoglycan biosynthesis), GO:0006891 (intra-Golgi vesicle transport) |
| Cell types (CL) | CL:0000138 (chondrocyte), CL:0000414 (ameloblast), CL:0000062 (osteoblast), CL:0000057 (fibroblast) |
| Anatomy (UBERON) | UBERON:0002514 (epiphyseal/growth-plate cartilage), UBERON:0001754 (tooth enamel), UBERON:0001434 (skeletal system) |
| Cellular component (GO) | GO:0005794 (Golgi apparatus), GO:0005886 (plasma membrane) |
| Treatment (NCIT) | NCIT:C16186 (Orthopedic Surgical Procedure — spinal instrumentation/fusion), NCIT:C15302 (Physical Therapy), NCIT:C15240 (Genetic Counseling), NCIT:C15747 (Supportive Care) |

---

## Important Curation Caveat

**Do not confuse SSASKS (SLC10A7, OMIM #618363) with the phenotypically overlapping LTBP3-related disorder** "Dental Anomalies and Short Stature" (DASS, OMIM #601216, also called brachyolmia with amelogenesis imperfecta). Both present with short stature + amelogenesis imperfecta + skeletal dysplasia/scoliosis, but they are molecularly and mechanistically distinct: SLC10A7 disease is a Golgi-calcium/glycosylation defect (GAG biosynthesis), while LTBP3 disease involves dysregulated TGF-β signaling and carries a more prominent cardiovascular phenotype (thoracic aortic aneurysm/dissection, mitral valve prolapse). Early web/AI searches for this exact title can misattribute the gene to LTBP3 — this is a **named-entity-confusion risk** given the near-identical clinical description; the correct causal gene for the title exactly as given ("Short Stature, Amelogenesis Imperfecta, and Skeletal Dysplasia with Scoliosis") is **SLC10A7**, per OMIM #618363.

---

### Sources
- [OMIM #618363 — SHORT STATURE, AMELOGENESIS IMPERFECTA, AND SKELETAL DYSPLASIA WITH SCOLIOSIS; SSASKS](https://www.omim.org/entry/618363)
- [OMIM *611459 — SLC10A7](https://omim.org/entry/611459)
- [OMIM #601216 — DENTAL ANOMALIES AND SHORT STATURE; DASS (LTBP3, related/differential disorder)](https://www.omim.org/entry/601216)
- Dubail J, et al. "SLC10A7 mutations cause a skeletal dysplasia with amelogenesis imperfecta mediated by GAG biosynthesis defects." Nat Commun. 2018. [PMID:30082715](https://pubmed.ncbi.nlm.nih.gov/30082715/) / [PMC6078967](https://pmc.ncbi.nlm.nih.gov/articles/PMC6078967/)
- Ashikov A, et al. "Integrating glycomics and genomics uncovers SLC10A7 as essential factor for bone mineralization by regulating post-Golgi protein transport and glycosylation." Hum Mol Genet. 2018. [Oxford Academic](https://academic.oup.com/hmg/article/27/17/3029/5033379)
- "A New SLC10A7 Homozygous Missense Mutation Responsible for a Milder Phenotype of Skeletal Dysplasia With Amelogenesis Imperfecta." Front Genet. 2019. [PMID:31191616](https://pubmed.ncbi.nlm.nih.gov/31191616/) / [PMC6546871](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6546871/)
- "SLC10A7, an orphan member of the SLC10 family involved in congenital disorders of glycosylation." 2021. [PMID:34999954](https://pubmed.ncbi.nlm.nih.gov/34999954/)
- "The orphan solute carrier SLC10A7 is a novel negative regulator of intracellular calcium signaling." [PMID:32350310](https://pubmed.ncbi.nlm.nih.gov/32350310/)
- "Identification of novel homozygous nonsense SLC10A7 variant causing short stature, amelogenesis imperfecta, and skeletal dysplasia with scoliosis and surgical management of spine." Orphanet J Rare Dis. 2023. [PMC10691085](https://pmc.ncbi.nlm.nih.gov/articles/PMC10691085/)
- "A Rare Case of Brachyolmia with Amelogenesis Imperfecta Caused by a New Pathogenic Splicing Variant in LTBP3." Genes (Basel). 2021. [PMC8470690](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8470690/)
- GeneCards: [SLC10A7](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SLC10A7)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 8 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.