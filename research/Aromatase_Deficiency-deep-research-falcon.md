---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:00:44.324665'
end_time: '2025-12-15T09:09:45.955582'
duration_seconds: 541.63
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Aromatase Deficiency
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 11
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Aromatase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Aromatase Deficiency**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


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

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Aromatase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Aromatase Deficiency**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


Plan
We identified recent authoritative sources, extracted mechanistic details and ontology-friendly annotations, compiled an ontology artifact, and synthesized clinical applications and expert perspectives (2023–2024). We now present a comprehensive, citable research report.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Aromatase Deficiency (CYP19A1 loss-of-function)
- MONDO ID: MONDO:0009735 (Aromatase deficiency; if subtyping required, consult ontology updates)
- Category: Genetic (autosomal recessive disorder of steroidogenesis)

Pathophysiology description
Aromatase deficiency is caused by biallelic pathogenic variants in CYP19A1 encoding microsomal aromatase (P450 19A1), the enzyme that converts C19 androgens (androstenedione, testosterone, 16α‑OH‑DHEA) into C18 estrogens (estrone, estradiol, estriol). Placental, gonadal, adipose, bone, brain, and other tissue expression means loss of aromatase produces systemic estrogen deficiency with accumulation of androgens. In pregnancy, failure of placental aromatase prevents conversion of fetal adrenal precursors (notably 16‑OH‑DHEAS) to estriol, allowing maternal exposure to androgen excess and leading to maternal virilization; concurrently, female (46,XX) fetuses are virilized by excess androgens. Core downstream effects include disruption of estrogen receptor signaling (ESR1/ESR2/GPER), disinhibited hypothalamic–pituitary–gonadal (HPG) axis drive (hypergonadotropic hypogonadism), impaired bone maturation and remodeling (delayed epiphyseal fusion, low bone mass), and adverse metabolic profiles (insulin resistance, dyslipidemia). “Pathogenic variants in the CYP19A1 gene lead to aromatase deﬁciency, causing androgen excess,” and placental/fetal aromatase normally “protects the mother from virilization” by metabolizing fetal androgens; deficiency therefore causes maternal and fetal virilization with very low estrogens and elevated androgens (46,XX DSD) (abalı2024diagnosisandmanagement pages 1-2, abalı2024diagnosisandmanagement pages 4-5, stancampiano202446xxdifferencesof pages 8-9). The clinical physiology of complete aromatase loss includes 46,XX ambiguous genitalia at birth, progressive virilization, and in both sexes estrogen‑dependent bone effects such as “delayed epiphyseal closure and osteopenia/osteoporosis,” with tall stature described in males due to unfused epiphyses (blakemore2016aromatasecontributionsto pages 5-7).

Core Pathophysiology
- Primary mechanisms: loss of aromatase-mediated androgen→estrogen conversion; prenatal placental failure of estriol synthesis; systemic estrogen deficiency with androgen excess (stancampiano202446xxdifferencesof pages 8-9, abalı2024diagnosisandmanagement pages 1-2).
- Dysregulated pathways: steroidogenesis flux (C19 accumulation), estrogen receptor signaling (ESR1/ESR2/GPER), HPG feedback (↑LH/FSH from low estrogen), bone remodeling (↑RANKL signaling with hypoestrogenism), metabolic regulation (insulin sensitivity, lipid homeostasis) (blakemore2016aromatasecontributionsto pages 5-7, abalı2024diagnosisandmanagement pages 5-6).
- Affected cellular processes: ER-resident P450 catalysis; ligand-activated transcription via nuclear ERs; membrane-initiated estrogen signaling; endochondral ossification and growth plate fusion; ovarian folliculogenesis dependent on granulosa aromatase (blakemore2016aromatasecontributionsto pages 5-7, stancampiano202446xxdifferencesof pages 8-9).

Key Molecular Players
- Genes/Proteins (HGNC): CYP19A1/AROMATASE (HGNC:2594) causal; ERs ESR1 (HGNC:3467), ESR2 (HGNC:3468) and GPER1 (HGNC:4485) as signaling mediators; POR (HGNC:9208) as differential diagnosis affecting multiple microsomal P450s including CYP19A1; NR5A1 (HGNC:2510) may modify DSD phenotypes but is not causal in AroD (abalı2024diagnosisandmanagement pages 4-5, stancampiano202446xxdifferencesof pages 8-9, blakemore2016aromatasecontributionsto pages 5-7).
- Chemical entities (CHEBI): androgens (androstenedione CHEBI:28689; testosterone CHEBI:17347) accumulate; estrogens (estrone CHEBI:17263; estradiol CHEBI:16469; estriol CHEBI:16490) are reduced; fetal precursor DHEA-S (CHEBI:28941) normally feeds placental estriol synthesis; antiandrogens (flutamide CHEBI:5102; spironolactone CHEBI:9606) are used adjunctively (stancampiano202446xxdifferencesof pages 8-9, abalı2024diagnosisandmanagement pages 1-2).
- Cell types (CL): granulosa cells (ovarian estrogen synthesis); trophoblast (placental aromatase and maternal protection); Leydig cells (androgen production); osteoblasts/osteoclasts (bone remodeling under estrogen control); adipocytes (peripheral aromatization) (stancampiano202446xxdifferencesof pages 8-9, blakemore2016aromatasecontributionsto pages 5-7).
- Anatomical locations (UBERON): ovary, placenta, uterus, testis, bone, adipose tissue, brain are key affected sites (stancampiano202446xxdifferencesof pages 8-9, blakemore2016aromatasecontributionsto pages 5-7).

Biological Processes (GO)
- Steroid biosynthetic process (GO:0006694); estrogen biosynthetic process (GO:0006703) directly impaired by CYP19A1 loss (stancampiano202446xxdifferencesof pages 8-9).
- Androgen metabolic process (GO:0008209) with accumulation of C19 substrates (abalı2024diagnosisandmanagement pages 1-2).
- Estrogen receptor signaling pathway (GO:0030520) diminished systemically (blakemore2016aromatasecontributionsto pages 5-7).
- Regulation of gonadotropin secretion (GO:0032274) disrupted, producing hypergonadotropic hypogonadism (blakemore2016aromatasecontributionsto pages 5-7).
- Bone remodeling (GO:0046849) and endochondral ossification (GO:0001958) altered with delayed epiphyseal closure (blakemore2016aromatasecontributionsto pages 5-7).

Cellular Components
- Endoplasmic reticulum membrane (GO:0005789) and microsomes (GO:0005792) host aromatase catalysis; estrogen receptors act at plasma membrane (GPER1) and nucleus (ESR1/ESR2), with systemic effects mediated via the extracellular hormone milieu (GO:0005886, GO:0005634, GO:0005615) (stancampiano202446xxdifferencesof pages 8-9, blakemore2016aromatasecontributionsto pages 5-7).

Disease Progression
- Fetal: placental aromatase failure → maternal virilization in pregnancy; 46,XX fetal virilization due to transplacental and fetal androgen excess; estriol production markedly reduced (stancampiano202446xxdifferencesof pages 8-9, abalı2024diagnosisandmanagement pages 1-2).
- Neonatal/Childhood: 46,XX ambiguous genitalia (clitoromegaly, posterior labial fusion, urogenital sinus); elevated androgens, very low estrogens; ovarian changes may include enlarged/multicystic or hypoplastic ovaries (abalı2024diagnosisandmanagement pages 5-6).
- Puberty: hypergonadotropic hypogonadism with delayed/absent thelarche; progressive virilization if untreated; residual activity variants may show partial breast development (abalı2024diagnosisandmanagement pages 5-6).
- Adulthood: fertility impairment in 46,XX; bone health complications (low BMD, delayed epiphyseal closure); metabolic features (insulin resistance, dyslipidemia) (blakemore2016aromatasecontributionsto pages 5-7, abalı2024diagnosisandmanagement pages 5-6).

Phenotypic Manifestations
- 46,XX: prenatal virilization with ambiguous genitalia; pubertal failure with amenorrhea and hypergonadotropic hypogonadism; ovarian macrocysts or multicystic ovaries; progressive virilization; reduced estradiol with elevated androgens (abalı2024diagnosisandmanagement pages 5-6, abalı2024diagnosisandmanagement pages 1-2, stancampiano202446xxdifferencesof pages 8-9).
- 46,XY: external genitalia typically normal or mildly affected; prominent estrogen-deficiency skeletal findings (tall stature, delayed epiphyseal closure, osteopenia/osteoporosis), reduced libido; metabolic derangements (blakemore2016aromatasecontributionsto pages 5-7).

Current applications and real-world implementations
- Diagnostics: LC–MS/MS steroid profiling to demonstrate elevated C19 androgens with very low estrogens; genetic testing via targeted CYP19A1 sequencing or exome/genome sequencing; crucial differential diagnosis with POR deficiency (which reduces CYP19A1 activity secondarily) using gene testing and distinctive steroid profiles; prenatal suspicion with maternal virilization and low estriol (abalı2024diagnosisandmanagement pages 4-5, abalı2024diagnosisandmanagement pages 1-2).
- Management: estrogen replacement therapy for pubertal induction and maintenance in 46,XX; consider antiandrogens (e.g., flutamide, spironolactone) to mitigate virilization; monitor and treat bone health in both sexes; fertility management is individualized, with limited long-term outcome data (abalı2024diagnosisandmanagement pages 5-6, blakemore2016aromatasecontributionsto pages 5-7). Expert reviews emphasize that estrogen replacement can improve ovarian phenotype (e.g., cyst resolution) and hypogonadism, though evidence remains from case-level data (abalı2024diagnosisandmanagement pages 5-6).

Expert opinions and recent developments (2023–2024)
- 2024 DSD reviews place aromatase deficiency among non-CAH 46,XX DSD etiologies and stress advances in cytogenetic and molecular diagnostics; they reaffirm that “Pathogenic variants in the CYP19A1 gene lead to aromatase deﬁciency, causing androgen excess,” and that prenatal-onset androgen excess drives the 46,XX phenotype, with management challenges persisting due to rarity and heterogeneity (published 15 May 2024; Frontiers in Endocrinology; https://doi.org/10.3389/fendo.2024.1354759) (abalı2024diagnosisandmanagement pages 1-2).
- A 2024 review of 46,XX DSDs outside CAH summarizes CYP19A1 genetics, tissue-specific expression, and placental metabolism of fetal 16‑OH‑DHEAS to estriol, underscoring the mechanistic basis of maternal/fetal virilization in aromatase deficiency (published May 2024; Frontiers in Endocrinology; https://doi.org/10.3389/fendo.2024.1402579) (stancampiano202446xxdifferencesof pages 8-9).
- Differential with POR deficiency (2023 review) remains clinically salient since POR defects can cause “placental aromatase deficiency affected by POR,” necessitating distinct management pathways (published Aug 2023; Frontiers in Endocrinology; https://doi.org/10.3389/fendo.2023.1226387) (abalı2024diagnosisandmanagement pages 4-5).
- Foundational expert synthesis (Physiology 2016) continues to frame the phenotype spectrum and systemic estrogen roles in bone and metabolism, with quotations widely cited in current reviews for skeletal and metabolic consequences of aromatase loss (published Jul 2016; https://doi.org/10.1152/physiol.00054.2015) (blakemore2016aromatasecontributionsto pages 5-7).

Relevant statistics and data
- Case accrual remains limited; a 2024 review cites approximately 40 reported cases since the first description in 1991, reflecting the rarity of confirmed CYP19A1 biallelic loss-of-function (published May 2024) (stancampiano202446xxdifferencesof pages 8-9).
- Biochemical hallmarks summarized in recent reviews include “elevated plasma androstenedione and testosterone with very low or undetectable estrone/estradiol,” consistent across reported cases (abalı2024diagnosisandmanagement pages 5-6).

Direct quotes supporting key statements
- “Pathogenic variants in the CYP19A1 gene lead to aromatase deﬁciency, causing androgen excess.” (Frontiers in Endocrinology, 15 May 2024; https://doi.org/10.3389/fendo.2024.1354759) (abalı2024diagnosisandmanagement pages 1-2).
- Placental aromatase “protects the mother from virilization,” so deficiency leads to maternal and fetal virilization (summarized in 2024 reviews) (abalı2024diagnosisandmanagement pages 4-5, stancampiano202446xxdifferencesof pages 8-9).
- Clinical physiology includes “delayed epiphyseal closure and osteopenia/osteoporosis” with tall stature in males (Physiology, Jul 2016; https://doi.org/10.1152/physiol.00054.2015) (blakemore2016aromatasecontributionsto pages 5-7).

Gene/protein annotations with ontology terms
- CYP19A1 (HGNC:2594): aromatase, ER membrane P450; GO:0006703, GO:0006694; components GO:0005789/GO:0005792 (stancampiano202446xxdifferencesof pages 8-9).
- ESR1 (HGNC:3467), ESR2 (HGNC:3468), GPER1 (HGNC:4485): estrogen signaling; GO:0030520; nucleus GO:0005634; plasma membrane GO:0005886 (blakemore2016aromatasecontributionsto pages 5-7).
- POR (HGNC:9208): electron donor to microsomal CYPs; differential that can mimic aromatase deficiency (abalı2024diagnosisandmanagement pages 4-5).

Phenotype associations (HP terms)
- Ambiguous genitalia (HP:0000062), clitoromegaly (HP:0008665), primary amenorrhea (HP:0000786), hypergonadotropic hypogonadism (HP:0000045), ovarian cyst (HP:0000137), tall stature (HP:0000098), delayed epiphyseal closure (HP:0003070), osteoporosis (HP:0000939), insulin resistance (HP:0000855), dyslipidemia (HP:0003119) (abalı2024diagnosisandmanagement pages 5-6, blakemore2016aromatasecontributionsto pages 5-7, stancampiano202446xxdifferencesof pages 8-9).

Cell type involvement (CL terms)
- Granulosa cell (CL:0002320), trophoblast (CL:0000351), Leydig cell (CL:0000182), osteoblast (CL:0000062), osteoclast (CL:0000092), adipocyte (CL:0000136) (stancampiano202446xxdifferencesof pages 8-9, blakemore2016aromatasecontributionsto pages 5-7).

Anatomical locations (UBERON terms)
- Ovary (UBERON:0000992), placenta (UBERON:0001987), uterus (UBERON:0000995), testis (UBERON:0000473), bone (UBERON:0001474), adipose (UBERON:0001013), brain (UBERON:0000955) (stancampiano202446xxdifferencesof pages 8-9, blakemore2016aromatasecontributionsto pages 5-7).

Chemical entities (CHEBI terms)
- Androstenedione (CHEBI:28689), testosterone (CHEBI:17347), estrone (CHEBI:17263), estradiol (CHEBI:16469), estriol (CHEBI:16490), DHEA sulfate (CHEBI:28941), spironolactone (CHEBI:9606), flutamide (CHEBI:5102) (stancampiano202446xxdifferencesof pages 8-9, abalı2024diagnosisandmanagement pages 1-2).

Embedded artifact
| Category | Item (name) | Ontology ID | Notes on role in disease |
|---|---|---:|---|
| Gene / Protein | CYP19A1 | HGNC:2594 | Aromatase enzyme; loss causes androgen accumulation and estrogen deficiency. (abalı2024diagnosisandmanagement pages 1-2, stancampiano202446xxdifferencesof pages 8-9) |
| Gene / Protein | ESR1 | HGNC:3467 | Estrogen receptor alpha mediates estrogen signaling; affected by low estrogen. (blakemore2016aromatasecontributionsto pages 5-7) |
| Gene / Protein | ESR2 | HGNC:3468 | Estrogen receptor beta; tissue-specific estrogen responses diminished. (blakemore2016aromatasecontributionsto pages 5-7) |
| Gene / Protein | GPER1 | HGNC:4485 | Membrane estrogen receptor mediating rapid signaling; hypoestrogenism reduces activity. (blakemore2016aromatasecontributionsto pages 5-7) |
| Gene / Protein | NR5A1 | HGNC:2510 | Transcription factor in gonadal development; can modify DSD phenotypes. (stancampiano202446xxdifferencesof pages 8-9) |
| Gene / Protein | POR | HGNC:9208 | Electron donor to microsomal CYPs; POR defects can phenocopy aromatase issues. (abalı2024diagnosisandmanagement pages 4-5, stancampiano202446xxdifferencesof pages 8-9) |
| Cell type | Granulosa cell | CL:0002320 | Site of ovarian aromatase expression; estrogen synthesis is impaired. (stancampiano202446xxdifferencesof pages 8-9) |
| Cell type | Trophoblast | CL:0000351 | Placental aromatase site; loss causes maternal and fetal virilization. (abalı2024diagnosisandmanagement pages 1-2, stancampiano202446xxdifferencesof pages 8-9) |
| Cell type | Leydig cell | CL:0000182 | Testicular androgen source; peripheral aromatization affects systemic balance. (blakemore2016aromatasecontributionsto pages 5-7) |
| Cell type | Osteoblast | CL:0000062 | Bone-forming cell; estrogen deficiency increases bone resorption risk. (blakemore2016aromatasecontributionsto pages 5-7) |
| Cell type | Osteoclast | CL:0000092 | Bone-resorbing cell; activity increases when estrogen is low. (blakemore2016aromatasecontributionsto pages 5-7) |
| Cell type | Adipocyte | CL:0000136 | Peripheral aromatase expression site; contributes to local estrogen production. (blakemore2016aromatasecontributionsto pages 5-7, stancampiano202446xxdifferencesof pages 8-9) |
| Anatomical location | Ovary | UBERON:0000992 | Site of granulosa aromatase; ovarian development and fertility impacted. (stancampiano202446xxdifferencesof pages 8-9) |
| Anatomical location | Placenta | UBERON:0001987 | Crucial for fetal estrogen production; maternal virilization if deficient. (abalı2024diagnosisandmanagement pages 1-2, stancampiano202446xxdifferencesof pages 8-9) |
| Anatomical location | Uterus | UBERON:0000995 | Estrogen-dependent organ; hypoplasia and poor endometrial development possible. (blakemore2016aromatasecontributionsto pages 5-7) |
| Anatomical location | Testis | UBERON:0000473 | Androgen source; 46,XY genital phenotype often milder than 46,XX. (blakemore2016aromatasecontributionsto pages 5-7) |
| Anatomical location | Bone | UBERON:0001474 | Affected by estrogen deficiency causing delayed epiphyseal closure and osteopenia. (blakemore2016aromatasecontributionsto pages 5-7) |
| Anatomical location | Adipose tissue | UBERON:0001013 | Expresses aromatase; loss alters metabolic regulation and lipid profiles. (blakemore2016aromatasecontributionsto pages 5-7) |
| Anatomical location | Brain | UBERON:0000955 | Central estrogen actions on behavior and HPG axis signaling disrupted. (blakemore2016aromatasecontributionsto pages 5-7) |
| Biological process | Steroid biosynthetic process | GO:0006694 | Overall steroidogenesis altered with accumulation of androgens. (stancampiano202446xxdifferencesof pages 8-9) |
| Biological process | Estrogen biosynthetic process | GO:0006703 | Aromatase-catalyzed estrogen synthesis is impaired. (stancampiano202446xxdifferencesof pages 8-9) |
| Biological process | Androgen metabolic process | GO:0008209 | Androgen metabolism shifts toward accumulation of C19 steroids. (abalı2024diagnosisandmanagement pages 1-2) |
| Biological process | Estrogen receptor signaling pathway | GO:0030520 | Downstream estrogen signaling reduced, affecting multiple tissues. (blakemore2016aromatasecontributionsto pages 5-7) |
| Biological process | Regulation of gonadotropin secretion | GO:0032274 | HPG feedback disrupted causing hypergonadotropic hypogonadism. (blakemore2016aromatasecontributionsto pages 5-7) |
| Biological process | Bone remodeling | GO:0046849 | Imbalanced osteoblast/osteoclast activity leading to bone loss. (blakemore2016aromatasecontributionsto pages 5-7) |
| Biological process | Endochondral ossification | GO:0001958 | Delayed epiphyseal closure due to low estrogen levels. (blakemore2016aromatasecontributionsto pages 5-7) |
| Cellular component | Endoplasmic reticulum membrane | GO:0005789 | Location of microsomal aromatase P450 enzyme. (stancampiano202446xxdifferencesof pages 8-9) |
| Cellular component | Microsome | GO:0005792 | Subcellular fraction containing aromatase activity. (stancampiano202446xxdifferencesof pages 8-9) |
| Cellular component | Plasma membrane | GO:0005886 | Location of membrane estrogen receptor GPER; signaling changes. (blakemore2016aromatasecontributionsto pages 5-7) |
| Cellular component | Nucleus | GO:0005634 | Nuclear ER-mediated transcriptional responses are impaired. (blakemore2016aromatasecontributionsto pages 5-7) |
| Cellular component | Extracellular space | GO:0005615 | Circulating steroid hormones and paracrine signaling altered. (stancampiano202446xxdifferencesof pages 8-9) |
| Chemical entity | Androstenedione | CHEBI:28689 | Major aromatase substrate; accumulates when enzyme deficient. (stancampiano202446xxdifferencesof pages 8-9) |
| Chemical entity | Testosterone | CHEBI:17347 | Substrate and androgenic effector causing virilization. (stancampiano202446xxdifferencesof pages 8-9) |
| Chemical entity | Estrone | CHEBI:17263 | Estrogen product reduced leading to systemic hypoestrogenism. (stancampiano202446xxdifferencesof pages 8-9) |
| Chemical entity | Estradiol | CHEBI:16469 | Primary active estrogen decreased causing multisystem effects. (stancampiano202446xxdifferencesof pages 8-9) |
| Chemical entity | Estriol | CHEBI:16490 | Placental fetal estrogen reduced; derived from 16OH-DHEAS normally. (stancampiano202446xxdifferencesof pages 8-9) |
| Chemical entity | DHEA sulfate | CHEBI:28941 | Fetal adrenal precursor feeding placental estrogen synthesis; altered flux. (stancampiano202446xxdifferencesof pages 8-9) |
| Chemical entity | Spironolactone | CHEBI:9606 | Anti-androgen sometimes used to reduce virilization (off-label). (abalı2024diagnosisandmanagement pages 1-2) |
| Chemical entity | Flutamide | CHEBI:5102 | Androgen receptor antagonist used to counter virilization. (abalı2024diagnosisandmanagement pages 1-2) |
| Phenotype | Ambiguous genitalia | HP:0000062 | 46,XX virilization leading to atypical external genitalia. (abalı2024diagnosisandmanagement pages 1-2, stancampiano202446xxdifferencesof pages 8-9) |
| Phenotype | Clitoromegaly | HP:0008665 | Enlarged clitoris due to prenatal androgen exposure. (abalı2024diagnosisandmanagement pages 1-2) |
| Phenotype | Primary amenorrhea | HP:0000786 | Absent menses from hypergonadotropic hypogonadism. (abalı2024diagnosisandmanagement pages 1-2, blakemore2016aromatasecontributionsto pages 5-7) |
| Phenotype | Hypergonadotropic hypogonadism | HP:0000045 | Elevated gonadotropins due to low estrogen negative feedback. (blakemore2016aromatasecontributionsto pages 5-7) |
| Phenotype | Ovarian cyst | HP:0000137 | Multicystic ovaries reported from unopposed gonadotropin stimulation. (abalı2024diagnosisandmanagement pages 4-5, stancampiano202446xxdifferencesof pages 8-9) |
| Phenotype | Tall stature | HP:0000098 | Delayed epiphyseal closure results in increased final height. (blakemore2016aromatasecontributionsto pages 5-7) |
| Phenotype | Delayed epiphyseal closure | HP:0003070 | Result of estrogen deficiency impairing growth plate fusion. (blakemore2016aromatasecontributionsto pages 5-7) |
| Phenotype | Osteoporosis | HP:0000939 | Low bone mass risk due to chronic hypoestrogenism. (blakemore2016aromatasecontributionsto pages 5-7) |
| Phenotype | Insulin resistance | HP:0000855 | Metabolic alterations including insulin resistance reported. (abalı2024diagnosisandmanagement pages 5-6, stancampiano202446xxdifferencesof pages 8-9) |
| Phenotype | Dyslipidemia | HP:0003119 | Adverse lipid profile associated with low aromatase activity. (blakemore2016aromatasecontributionsto pages 5-7) |


*Table: Compact ontology table mapping key genes, cells, locations, processes, components, chemicals, and phenotypes relevant to aromatase (CYP19A1) deficiency, with concise functional notes and source citations for database use.*

Evidence items (PMIDs/DOIs/URLs; publication dates)
- Abalı ZY, Guran T. Diagnosis and management of non-CAH 46,XX DSD. Frontiers in Endocrinology. Published 15 May 2024. DOI: 10.3389/fendo.2024.1354759. URL: https://doi.org/10.3389/fendo.2024.1354759 (abalı2024diagnosisandmanagement pages 1-2).
- Stancampiano MR, et al. 46,XX DSD outside CAH. Frontiers in Endocrinology. Published May 2024. DOI: 10.3389/fendo.2024.1402579. URL: https://doi.org/10.3389/fendo.2024.1402579 (stancampiano202446xxdifferencesof pages 8-9).
- Wang C, Tian Q. POR deficiency review. Frontiers in Endocrinology. Published Aug 2023. DOI: 10.3389/fendo.2023.1226387. URL: https://doi.org/10.3389/fendo.2023.1226387 (abalı2024diagnosisandmanagement pages 4-5).
- Blakemore J, Naftolin F. Aromatase: physiology and disease. Physiology. Published Jul 2016. DOI: 10.1152/physiol.00054.2015. URL: https://doi.org/10.1152/physiol.00054.2015 (blakemore2016aromatasecontributionsto pages 5-7).

Limitations and open questions
The rarity of confirmed CYP19A1 biallelic cases limits robust natural history and interventional evidence; many management suggestions derive from small series and case reports. Contemporary reviews call for standardized diagnostic algorithms (LC–MS/MS, genomics) and longitudinal registries to clarify fertility outcomes and optimal timing/dosing of estrogen therapy (abalı2024diagnosisandmanagement pages 1-2, stancampiano202446xxdifferencesof pages 8-9).

References

1. (abalı2024diagnosisandmanagement pages 1-2): Zehra Yavas Abalı and Tulay Guran. Diagnosis and management of non-cah 46,xx disorders/differences in sex development. Frontiers in Endocrinology, May 2024. URL: https://doi.org/10.3389/fendo.2024.1354759, doi:10.3389/fendo.2024.1354759. This article has 10 citations and is from a poor quality or predatory journal.

2. (abalı2024diagnosisandmanagement pages 4-5): Zehra Yavas Abalı and Tulay Guran. Diagnosis and management of non-cah 46,xx disorders/differences in sex development. Frontiers in Endocrinology, May 2024. URL: https://doi.org/10.3389/fendo.2024.1354759, doi:10.3389/fendo.2024.1354759. This article has 10 citations and is from a poor quality or predatory journal.

3. (stancampiano202446xxdifferencesof pages 8-9): Marianna Rita Stancampiano, Silvia Laura Carla Meroni, Carmen Bucolo, and Gianni Russo. 46,xx differences of sex development outside congenital adrenal hyperplasia: pathogenesis, clinical aspects, puberty, sex hormone replacement therapy and fertility outcomes. Frontiers in Endocrinology, May 2024. URL: https://doi.org/10.3389/fendo.2024.1402579, doi:10.3389/fendo.2024.1402579. This article has 8 citations and is from a poor quality or predatory journal.

4. (blakemore2016aromatasecontributionsto pages 5-7): Jennifer Blakemore and Fredrick Naftolin. Aromatase: contributions to physiology and disease in women and men. Physiology, 31 4:258-69, Jul 2016. URL: https://doi.org/10.1152/physiol.00054.2015, doi:10.1152/physiol.00054.2015. This article has 240 citations and is from a peer-reviewed journal.

5. (abalı2024diagnosisandmanagement pages 5-6): Zehra Yavas Abalı and Tulay Guran. Diagnosis and management of non-cah 46,xx disorders/differences in sex development. Frontiers in Endocrinology, May 2024. URL: https://doi.org/10.3389/fendo.2024.1354759, doi:10.3389/fendo.2024.1354759. This article has 10 citations and is from a poor quality or predatory journal.