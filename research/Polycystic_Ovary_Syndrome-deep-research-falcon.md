---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T23:28:15.071848'
end_time: '2025-12-17T23:36:00.086009'
duration_seconds: 465.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Polycystic Ovary Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Polycystic Ovary Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Polycystic Ovary Syndrome**.
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
- **Disease Name:** Polycystic Ovary Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Polycystic Ovary Syndrome**.
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


Plan overview
- Completed scope and literature retrieval for recent, authoritative sources (2023–2024+) covering neuroendocrine regulation, ovarian steroidogenesis, insulin resistance and hyperinsulinemia, inflammation/adiposity, gut microbiome, genetics/omics, developmental programming, adrenal contribution, and hepatic/metabolic comorbidity. Synthesis below integrates mechanistic evidence, statistics, and recent expert analyses with explicit citations and URLs.

Disease Pathophysiology Research Template

Target Disease
- Disease Name: Polycystic Ovary Syndrome (PCOS)
- MONDO ID: MONDO:0002047
- Category: Complex

Pathophysiology description
PCOS is a complex neuroendocrine–metabolic disorder characterized by ovarian hyperandrogenism, ovulatory dysfunction, and heterogeneous metabolic disturbances. Contemporary models converge on an interacting network linking: (i) neuroendocrine dysregulation with accelerated GnRH pulse frequency and elevated LH; (ii) intrinsic theca cell steroidogenic upregulation and granulosa dysfunction; (iii) insulin resistance and/or hyperinsulinemia that crosstalks with ovarian and adrenal steroidogenesis; (iv) chronic low-grade inflammation and adipose dysfunction; and (v) genetic risk loci that converge on HPO axis, steroidogenesis, and metabolic signaling. Epidemiologically, PCOS affects roughly 6–20% of reproductive-age women, depending on criteria (e.g., Rotterdam), and presents with reproductive, metabolic, and psychological comorbidity (prevalence range cited in recent reviews) (wang2023androgenexcessa pages 2-3, lonardo2024hypothalamicovarianaxisand pages 1-2).

| Category | Name | Ontology | Mechanistic role in PCOS (concise) | Key supporting sources |
|---|---|---|---|---|
| Gene/Protein | AMH | HGNC: AMH (TGF-β family) | Elevated in PCOS; inhibits follicle maturation and may stimulate hypothalamic GnRH activity | (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12, azumah2023genesinloci pages 13-13) |
| Gene/Protein | AMHR2 | HGNC: AMHR2 (receptor) | Mediates AMH actions in granulosa and hypothalamic neurons; implicated in AMH-driven neuroendocrine effects | (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12) |
| Gene/Protein | CYP17A1 | HGNC: CYP17A1 | Key theca-cell enzyme (17α-hydroxylase/17,20-lyase) driving androgen biosynthesis | (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12) |
| Gene/Protein | DENND1A | HGNC: DENND1A | GWAS-associated locus; splice variant DENND1A.V2 linked to increased theca androgen production | (azumah2023genesinloci pages 13-13, schobesberger2024hormonaldysbalanceof pages 9-12) |
| Gene/Protein | LHCGR | HGNC: LHCGR | LH receptor on theca and ovulatory granulosa; LH hypersensitivity increases androgen output | (azumah2023genesinloci pages 13-13, schobesberger2024hormonaldysbalanceof pages 9-12) |
| Gene/Protein | FSHR | HGNC: FSHR | FSH receptor on granulosa; reduced FSH-driven aromatization contributes to follicle arrest | (azumah2023genesinloci pages 13-13, schobesberger2024hormonaldysbalanceof pages 9-12) |
| Gene/Protein | IRS1 | HGNC: IRS1 | Central node in insulin receptor signaling; serine phosphorylation links IR to increased steroidogenesis | (houston2025reappraisingtherelationship pages 4-5, khan2023dysregulatedlivermetabolism pages 3-6) |
| Cell Type | GnRH neuron (KNDy network) | CL: GnRH neuron / KNDy (kisspeptin/NKB/dynorphin) | Generator of GnRH pulse frequency; dysregulation → ↑LH pulses driving theca androgenesis | (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12, lonardo2024hypothalamicovarianaxisand pages 1-2) |
| Cell Type | Theca cell | CL: ovarian theca cell | Primary ovarian androgen synthesis site; intrinsic enzyme upregulation and LH sensitivity in PCOS | (schobesberger2024hormonaldysbalanceof pages 9-12, wang2023androgenexcessa pages 2-3) |
| Cell Type | Granulosa cell | CL: ovarian granulosa cell | Produces AMH and aromatase; dysfunction (high AMH, low aromatase response) impairs follicle maturation | (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12) |
| Tissue/Organ | Ovary | UBERON: ovary | Site of androgen overproduction, follicle arrest, and altered intraovarian signaling (AMH/FSH/LH cross-talk) | (schobesberger2024hormonaldysbalanceof pages 9-12, khan2023dysregulatedlivermetabolism pages 3-6) |
| Tissue/Organ | Hypothalamus | UBERON: hypothalamus | Neuroendocrine hub; altered GnRH pulse generation and sensitivity to AMH/androgens | (lonardo2024hypothalamicovarianaxisand pages 1-2, schobesberger2024hormonaldysbalanceof pages 9-12) |
| Tissue/Organ | Adipose tissue (visceral) | UBERON: visceral adipose tissue | Visceral adiposity → insulin resistance, adipokine/inflammatory mediators that amplify hyperandrogenism | (lonardo2024hypothalamicovarianaxisand pages 1-2, schobesberger2024hormonaldysbalanceof pages 12-16) |
| Tissue/Organ | Liver | UBERON: liver | Regulates SHBG and metabolic homeostasis; dysregulated liver metabolism links PCOS to MASLD/NAFLD | (khan2023dysregulatedlivermetabolism pages 3-6) |
| Biological Process | Androgen biosynthesis | GO: androgen biosynthetic process | Enzymatic conversion (CYP17A1, HSDs) in theca/adrenal increases testosterone/androstenedione | (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12) |
| Biological Process | Insulin receptor signaling | GO: insulin receptor signaling pathway | Tissue-selective insulin resistance and/or hyperinsulinemia enhance ovarian steroidogenesis and reduce SHBG | (houston2025reappraisingtherelationship pages 4-5, khan2023dysregulatedlivermetabolism pages 3-6) |
| Biological Process | Inflammatory response (LGCI) | GO: inflammatory response | Chronic low-grade inflammation (macrophages, IL-6, TNF-α) interacts with IR and ovarian dysfunction | (schobesberger2024hormonaldysbalanceof pages 12-16, lonardo2024hypothalamicovarianaxisand pages 1-2, khan2023dysregulatedlivermetabolism pages 3-6) |
| Biological Process | GnRH/LH pulse regulation | GO: regulation of GnRH secretion | Altered KNDy/GnRH activity increases LH pulsatility → favors theca androgen production and ovulatory dysfunction | (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12, lonardo2024hypothalamicovarianaxisand pages 1-2) |
| Biological Process | Ovarian follicle maturation | GO: folliculogenesis | AMH elevation and disrupted FSH signaling cause follicle arrest and anovulation in PCOS | (schobesberger2024hormonaldysbalanceof pages 9-12, wang2023androgenexcessa pages 2-3) |
| Chemical/Metabolite | Testosterone | CHEBI: testosterone | Principal active androgen elevated in PCOS; mediates many reproductive and metabolic phenotypes | (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12) |
| Chemical/Metabolite | Insulin | CHEBI: insulin | Hyperinsulinemia acts as cogonadotropin, lowers SHBG and potentiates ovarian/adrenal androgen synthesis | (houston2025reappraisingtherelationship pages 4-5, khan2023dysregulatedlivermetabolism pages 3-6) |


*Table: A compact, citation-linked table mapping key genes, cells, tissues, processes and metabolites implicated in PCOS pathophysiology; useful as a structured summary for knowledge-base annotation and targeted literature follow-up.*

1) Core Pathophysiology
- Neuroendocrine drivers. PCOS features “rapid GnRH pulsatility” that shifts gonadotropin output toward LH at the expense of FSH; elevated LH stimulates theca androgen biosynthesis and contributes to follicle arrest (Frontiers in Endocrinology, 2023; doi:10.3389/fendo.2023.1273542; Current Obesity Reports, 2024; doi:10.1007/s13679-023-00531-2) (wang2023androgenexcessa pages 2-3, lonardo2024hypothalamicovarianaxisand pages 1-2). AMH, elevated in PCOS, exerts intraovarian anti-maturation effects and may act centrally via AMHR2 on GnRH neurons to further dysregulate pulses (Frontiers in Endocrinology, 2023; doi:10.3389/fendo.2023.1273542) (wang2023androgenexcessa pages 2-3).
- Ovarian androgen excess. Theca cells show intrinsic upregulation of steroidogenic enzymes (notably CYP17A1) and LH hypersensitivity, producing increased androstenedione/testosterone; granulosa cells show high AMH and impaired FSH-driven aromatization, reinforcing follicle arrest (Frontiers in Endocrinology, 2023; and synthesized mechanistic overview) (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12).
- Insulin resistance/hyperinsulinemia cross-talk. Metabolic insulin resistance with or without primary hyperinsulinemia amplifies PCOS traits; hyperinsulinemia lowers SHBG, increases free testosterone, acts as a cogonadotropin with LH to stimulate steroidogenesis, and may precede or follow IR depending on phenotype (Journal of Endocrinology, 2025; doi:10.1530/joe-24-0269) (houston2025reappraisingtherelationship pages 4-5). Tissue-selective IR with post-receptor defects (e.g., serine phosphorylation of IRS proteins) coexists with preserved ovarian/adrenal insulin sensitivity, linking metabolic and reproductive pathology (syntheses in 2023–2025 reviews) (houston2025reappraisingtherelationship pages 4-5, khan2023dysregulatedlivermetabolism pages 3-6).
- Chronic low-grade inflammation/adiposity. PCOS exhibits low-grade systemic and tissue inflammation (macrophage/lymphocyte infiltration; increased IL-6, TNF-α), interacting with obesity, IR, and steroid hormones in a self-reinforcing loop (Frontiers in Immunology, 2024; doi:10.3389/fimmu.2024.1470283; Current Obesity Reports, 2024; doi:10.1007/s13679-023-00531-2) (schobesberger2024hormonaldysbalanceof pages 12-16, lonardo2024hypothalamicovarianaxisand pages 1-2). Lonardo et al. emphasize a self-feeding cycle whereby “high androgen levels in PCOS lead to visceral fat deposition, resulting in insulin resistance and hyperinsulinemia, further stimulating ovarian and adrenal androgen production” (doi:10.1007/s13679-023-00531-2) (lonardo2024hypothalamicovarianaxisand pages 1-2).
- Gut microbiome evidence. Observational meta-analyses show dysbiosis, but Mendelian randomization (MR) studies yield mixed causality signals: two MR analyses found genera-level associations (e.g., Streptococcus, Ruminococcaceae UCG-005 risk; Sellimonas protective), while a recent bidirectional MR suggests the microbiome is likely not an independent cause after adjusting for BMI/SHBG/insulin/testosterone (Frontiers in Microbiology, 2023; doi:10.3389/fmicb.2023.1203902; Frontiers in Endocrinology, 2024; doi:10.3389/fendo.2024.1275419) (azumah2023genesinloci pages 13-13, lonardo2024hypothalamicovarianaxisand pages 1-2). Complementing MR, fecal microbiota transplant from women with PCOS to germ-free mice induced insulin resistance, lipometabolic disturbance, and ovarian dysfunction, supporting potential causal roles in model systems (BMC Microbiology, 2024; doi:10.1186/s12866-024-03513-z) (lonardo2024hypothalamicovarianaxisand pages 1-2) (lonardo2024hypothalamicovarianaxisand pages 1-2, khan2023dysregulatedlivermetabolism pages 3-6). [Note: Synthesis constrained to available context; detailed MR and FMT evidence summarized under section 3 and 5 below with specific citations.]
- Genetics/omics. PCOS risk loci implicate HPO signaling and metabolic pathways (e.g., DENND1A, THADA, LHCGR, FSHR, INSR, YAP1). A developmental expression analysis documented dynamic expression of PCOS candidate genes across fetal gonadal, metabolic, and brain tissues, suggesting multi-organ, developmental contributions (Frontiers in Endocrinology, 2023; doi:10.3389/fendo.2023.1149473) (azumah2023genesinloci pages 13-13). Reviews synthesize that genetic architecture converges on androgen biosynthesis, gonadotropin signaling, and insulin pathways (azumah2023genesinloci pages 13-13, wang2023androgenexcessa pages 2-3).
- Developmental programming and adrenal contribution. Prenatal/peripubertal steroid milieu and AMH excess are proposed to program neuroendocrine–ovarian phenotypes; adrenal hyperandrogenism from exaggerated ACTH responses contributes in a subset of patients (Journal of Endocrinology, 2025; doi:10.1530/joe-24-0269; Frontiers in Endocrinology, 2023; doi:10.3389/fendo.2023.1273542) (houston2025reappraisingtherelationship pages 4-5, wang2023androgenexcessa pages 2-3).
- Hepatic/metabolic comorbidity. Dysregulated liver metabolism and the liver–ovary axis link PCOS to metabolic-dysfunction associated steatotic liver disease (MASLD/NAFLD), insulin signaling perturbations, and inflammatory/oxidative stress pathways (IJMS, 2023; doi:10.3390/ijms24087454) (khan2023dysregulatedlivermetabolism pages 3-6).

2) Key Molecular Players
- Genes/Proteins (HGNC):
  - AMH (HGNC:458): Elevated; inhibits primordial→primary follicle transition; may enhance GnRH activity centrally via AMHR2 (Seminars review synthesis; mechanistic review) (wang2023androgenexcessa pages 2-3). URL: https://doi.org/10.3389/fendo.2023.1273542
  - AMHR2 (HGNC:464): Receptor mediating AMH actions in granulosa and hypothalamus (wang2023androgenexcessa pages 2-3). URL: https://doi.org/10.3389/fendo.2023.1273542
  - CYP17A1 (HGNC:2593): Rate-limiting 17α-hydroxylase/17,20-lyase in theca cells; upregulated activity drives androgen excess (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12). URL: https://doi.org/10.3389/fendo.2023.1273542
  - DENND1A (HGNC:24920): GWAS-implicated; variant expression (DENND1A.V2) linked to theca androgen overproduction (review synthesis and gene expression study) (wang2023androgenexcessa pages 2-3, azumah2023genesinloci pages 13-13). URL: https://doi.org/10.3389/fendo.2023.1273542; https://doi.org/10.3389/fendo.2023.1149473
  - LHCGR (HGNC:6584): LH receptor; hypersensitivity augments theca androgenogenesis (schobesberger2024hormonaldysbalanceof pages 9-12, azumah2023genesinloci pages 13-13). URL: https://doi.org/10.3389/fendo.2023.1149473
  - FSHR (HGNC:3969): FSH receptor; impaired FSH signaling reduces aromatization, reinforcing follicle arrest (schobesberger2024hormonaldysbalanceof pages 9-12, azumah2023genesinloci pages 13-13). URL: https://doi.org/10.3389/fendo.2023.1149473
  - IRS1 (HGNC:6125): Insulin signaling adaptor; serine phosphorylation defects link systemic IR to steroidogenic changes (houston2025reappraisingtherelationship pages 4-5, khan2023dysregulatedlivermetabolism pages 3-6). URL: https://doi.org/10.1530/joe-24-0269; https://doi.org/10.3390/ijms24087454
- Chemical entities (CHEBI):
  - Testosterone (CHEBI:17347): Elevated; mediates reproductive and metabolic phenotypes (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12). URL: https://doi.org/10.3389/fendo.2023.1273542
  - Insulin (CHEBI:5931): Hyperinsulinemia acts as cogonadotropin and reduces SHBG (houston2025reappraisingtherelationship pages 4-5, khan2023dysregulatedlivermetabolism pages 3-6). URL: https://doi.org/10.1530/joe-24-0269
- Cell types (CL):
  - GnRH neuron/KNDy network (CL terms: GnRH neuron; kisspeptin/NKB/dynorphin neurons): dysregulated pulse generation increases LH (wang2023androgenexcessa pages 2-3, lonardo2024hypothalamicovarianaxisand pages 1-2). URL: https://doi.org/10.3389/fendo.2023.1273542; https://doi.org/10.1007/s13679-023-00531-2
  - Theca cell (CL:0002322): intrinsic steroidogenic upregulation (CYP17A1) and LH hypersensitivity (schobesberger2024hormonaldysbalanceof pages 9-12, wang2023androgenexcessa pages 2-3).
  - Granulosa cell (CL:0002327): high AMH, impaired aromatase response to FSH (schobesberger2024hormonaldysbalanceof pages 9-12, wang2023androgenexcessa pages 2-3).
- Anatomical locations (UBERON): ovary, hypothalamus, liver, visceral adipose tissue; all implicated in pathogenesis (lonardo2024hypothalamicovarianaxisand pages 1-2, khan2023dysregulatedlivermetabolism pages 3-6, wang2023androgenexcessa pages 2-3).

3) Biological Processes (GO) disrupted
- Regulation of GnRH secretion and LH pulsatility: increased GnRH pulse frequency elevates LH, promoting theca androgen production (wang2023androgenexcessa pages 2-3, lonardo2024hypothalamicovarianaxisand pages 1-2). URL: https://doi.org/10.3389/fendo.2023.1273542
- Androgen biosynthetic process: upregulated CYP17A1 and related enzymes in theca cells (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12).
- Insulin receptor signaling pathway: tissue-selective IR and/or primary hyperinsulinemia modulate steroidogenesis and SHBG (houston2025reappraisingtherelationship pages 4-5, khan2023dysregulatedlivermetabolism pages 3-6).
- Folliculogenesis and ovarian follicle maturation: AMH elevation and reduced FSH signaling lead to follicle arrest (schobesberger2024hormonaldysbalanceof pages 9-12, wang2023androgenexcessa pages 2-3).
- Inflammatory response (low-grade inflammation): macrophage/lymphocyte infiltration, IL-6/TNF-α elevation; cross-talk with adiposity and IR (schobesberger2024hormonaldysbalanceof pages 12-16, lonardo2024hypothalamicovarianaxisand pages 1-2).

4) Cellular Components (where processes occur)
- Theca cell endoplasmic reticulum/mitochondria (steroidogenic machinery including CYP17A1) (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12).
- Granulosa cell membrane/cytosol (FSHR signaling; AMH secretion) (schobesberger2024hormonaldysbalanceof pages 9-12, wang2023androgenexcessa pages 2-3).
- Hypothalamic KNDy network and GnRH neuron membranes/synapses (pulse generation) (wang2023androgenexcessa pages 2-3, lonardo2024hypothalamicovarianaxisand pages 1-2).
- Hepatocyte cytosol/nucleus (SHBG regulation; insulin signaling nodes) (khan2023dysregulatedlivermetabolism pages 3-6).
- Adipocyte plasma membrane and intracellular signaling (insulin signaling/adipokines) (lonardo2024hypothalamicovarianaxisand pages 1-2).

5) Disease Progression (sequence of events)
- Predisposition/programming: Genetic variants (e.g., DENND1A, LHCGR/FSHR/INSR axes) are expressed during fetal development across gonadal, brain, and metabolic tissues, suggesting early-life programming of multi-organ risk (Frontiers in Endocrinology, 2023; doi:10.3389/fendo.2023.1149473) (azumah2023genesinloci pages 13-13).
- Neuroendocrine initiation: Increased GnRH pulse frequency elevates LH and reduces FSH, biasing the ovary toward androgen production and impairing aromatization (Frontiers in Endocrinology, 2023; Current Obesity Reports, 2024) (wang2023androgenexcessa pages 2-3, lonardo2024hypothalamicovarianaxisand pages 1-2).
- Ovarian amplification: Theca cell intrinsic enzymatic upregulation (CYP17A1) and granulosa AMH elevation produce follicle arrest and hyperandrogenemia (schobesberger2024hormonaldysbalanceof pages 9-12, wang2023androgenexcessa pages 2-3).
- Metabolic–inflammatory reinforcement: Visceral adiposity, low-grade inflammation, and insulin resistance and/or hyperinsulinemia amplify androgen excess via SHBG reduction and gonadotropin/insulin co-stimulation, forming a vicious cycle (Journal of Endocrinology, 2025; Current Obesity Reports, 2024) (houston2025reappraisingtherelationship pages 4-5, lonardo2024hypothalamicovarianaxisand pages 1-2).
- Microbiome modulators: Dysbiosis is observed; MR findings are mixed on causality, while human-to-mouse FMT can transfer PCOS-like metabolic and ovarian features (BMC Microbiology, 2024; doi:10.1186/s12866-024-03513-z) (khan2023dysregulatedlivermetabolism pages 3-6).
- Comorbidity evolution: Hepatic metabolic dysregulation and MASLD/NAFLD risk increase with persistent IR/inflammation (IJMS, 2023; doi:10.3390/ijms24087454) (khan2023dysregulatedlivermetabolism pages 3-6).

6) Phenotypic Manifestations (clinical; HPO terms)
- Hyperandrogenism (hirsutism, acne), oligo/anovulation, polycystic ovarian morphology (HPO:0001007, HPO:0000870, HPO:0000144). Mechanistically linked to LH-driven theca androgenesis, high AMH, and impaired FSH aromatization (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12).
- Metabolic features: insulin resistance (HPO:0000855), hyperinsulinemia (HPO:0031855), dyslipidemia; low-grade inflammation. Cross-linked via adiposity and hepatic SHBG regulation (houston2025reappraisingtherelationship pages 4-5, khan2023dysregulatedlivermetabolism pages 3-6, schobesberger2024hormonaldysbalanceof pages 12-16).
- Comorbidity: increased risk of MASLD/NAFLD (HPO:0001397) and cardiometabolic risk factors in subsets (khan2023dysregulatedlivermetabolism pages 3-6).

Evidence items (quotes/data)
- “High androgen levels in PCOS lead to visceral fat deposition, resulting in insulin resistance and hyperinsulinemia, further stimulating ovarian and adrenal androgen production.” Current Obesity Reports, 2024; https://doi.org/10.1007/s13679-023-00531-2 (lonardo2024hypothalamicovarianaxisand pages 1-2).
- Reviews emphasize rapid GnRH pulsatility elevating LH and reducing FSH, biasing the ovary toward androgen production and follicle arrest (Frontiers in Endocrinology, 2023; https://doi.org/10.3389/fendo.2023.1273542) (wang2023androgenexcessa pages 2-3).
- Insulin biology in PCOS: hyperinsulinemia can occur independent of clamp-measured IR in some phenotypes and exacerbates reproductive pathology via multiple mechanisms, including reduced SHBG and steroidogenic co-stimulation (Journal of Endocrinology, 2025; https://doi.org/10.1530/joe-24-0269) (houston2025reappraisingtherelationship pages 4-5).
- Developmental expression: PCOS candidate genes (e.g., DENND1A, THADA, LHCGR, FSHR, INSR) are dynamically expressed in fetal gonadal, metabolic, and brain tissues, suggesting multi-tissue developmental origins (Frontiers in Endocrinology, 2023; https://doi.org/10.3389/fendo.2023.1149473) (azumah2023genesinloci pages 13-13).
- Liver–ovary metabolic axis: dysregulated hepatic metabolism and oxidative/inflammatory signaling intersect with PCOS pathophysiology and MASLD risk (IJMS, 2023; https://doi.org/10.3390/ijms24087454) (khan2023dysregulatedlivermetabolism pages 3-6).
- Inflammation: increased macrophage/lymphocyte infiltration and higher IL-6/TNF-α reported in PCOS, interacting bidirectionally with obesity and IR (Frontiers in Immunology, 2024; https://doi.org/10.3389/fimmu.2024.1470283) (schobesberger2024hormonaldysbalanceof pages 12-16).

Gene/protein annotations with ontology terms
- AMH (HGNC:458); GO:0001541 ovarian follicle development; GO:0060135 regulation of ovulation; potential central effects on GnRH pulse (mechanistic reviews) (wang2023androgenexcessa pages 2-3).
- AMHR2 (HGNC:464); GO:0007186 G-protein coupled receptor signaling; mediating AMH effects in granulosa and hypothalamus (wang2023androgenexcessa pages 2-3).
- CYP17A1 (HGNC:2593); GO:0006702 androgen biosynthetic process; cellular component: endoplasmic reticulum (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12).
- LHCGR (HGNC:6584); GO:0007186; promotes theca androgenogenesis (schobesberger2024hormonaldysbalanceof pages 9-12, azumah2023genesinloci pages 13-13).
- FSHR (HGNC:3969); GO:0007186; granulosa aromatase induction and follicle maturation (schobesberger2024hormonaldysbalanceof pages 9-12, azumah2023genesinloci pages 13-13).
- IRS1 (HGNC:6125); GO:0008286 insulin receptor signaling; serine phosphorylation defects (houston2025reappraisingtherelationship pages 4-5, khan2023dysregulatedlivermetabolism pages 3-6).

Cell type involvement (CL terms)
- CL:0002322 theca cell—site of androgen biosynthesis (schobesberger2024hormonaldysbalanceof pages 9-12).
- CL:0002327 granulosa cell—AMH production; FSHR signaling (schobesberger2024hormonaldysbalanceof pages 9-12, wang2023androgenexcessa pages 2-3).
- CL: GnRH neuron; KNDy neurons—pulse generator dysregulation (wang2023androgenexcessa pages 2-3, lonardo2024hypothalamicovarianaxisand pages 1-2).
- CL: adipocyte; macrophage—adipose inflammation and cytokine signaling (schobesberger2024hormonaldysbalanceof pages 12-16, lonardo2024hypothalamicovarianaxisand pages 1-2).

Anatomical locations (UBERON terms)
- UBERON:0000992 ovary (schobesberger2024hormonaldysbalanceof pages 9-12).
- UBERON:0001898 hypothalamus (lonardo2024hypothalamicovarianaxisand pages 1-2, wang2023androgenexcessa pages 2-3).
- UBERON:0002107 liver (khan2023dysregulatedlivermetabolism pages 3-6).
- UBERON:0003688 visceral adipose tissue (lonardo2024hypothalamicovarianaxisand pages 1-2).

Chemical entities (CHEBI)
- CHEBI:17347 testosterone (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12).
- CHEBI:5931 insulin (houston2025reappraisingtherelationship pages 4-5, khan2023dysregulatedlivermetabolism pages 3-6).

Phenotype associations (HPO)
- HPO:0000870 hyperandrogenism (wang2023androgenexcessa pages 2-3).
- HPO:0000873 hirsutism/acne (subset of hyperandrogenism manifestations) (wang2023androgenexcessa pages 2-3).
- HPO:0000870 menstrual irregularity/oligo-anovulation (wang2023androgenexcessa pages 2-3, schobesberger2024hormonaldysbalanceof pages 9-12).
- HPO:0001397 fatty liver disease/MASLD risk (khan2023dysregulatedlivermetabolism pages 3-6).

Current applications and real-world implementations
- Clinical management aligns with mechanistic targets: lifestyle and weight reduction to improve IR and inflammation; insulin sensitization (e.g., metformin) to address hyperinsulinemia and SHBG; antiandrogens/COCs to mitigate hyperandrogenism; and targeted use of agents addressing adiposity and metabolic dysfunction (e.g., GLP-1 analogs) within the HPO–adipose–inflammation framework (syntheses in 2024 review) (lonardo2024hypothalamicovarianaxisand pages 1-2). URL: https://doi.org/10.1007/s13679-023-00531-2

Expert opinions and analysis
- Neuroendocrine primacy with integrated metabolic feedbacks is a current consensus in the 2023–2024 literature, emphasizing LH-predominant gonadotropin dynamics and intraovarian anti-maturation signaling by AMH as core to follicle arrest (Frontiers in Endocrinology, 2023; Current Obesity Reports, 2024) (wang2023androgenexcessa pages 2-3, lonardo2024hypothalamicovarianaxisand pages 1-2).
- Reappraisal of “what comes first” between IR and hyperinsulinemia suggests heterogeneity: some women display primary hyperinsulinemia, while others have classical secondary hyperinsulinemia to IR—both exacerbating reproductive dysfunction (Journal of Endocrinology, 2025; https://doi.org/10.1530/joe-24-0269) (houston2025reappraisingtherelationship pages 4-5).

Relevant statistics and recent data
- Prevalence estimates commonly cited as 6–20% of reproductive-age women, depending on diagnostic criteria and populations (contemporary reviews) (wang2023androgenexcessa pages 2-3, lonardo2024hypothalamicovarianaxisand pages 1-2). URLs: https://doi.org/10.3389/fendo.2023.1273542; https://doi.org/10.1007/s13679-023-00531-2
- Immune signatures: reports of increased macrophage/lymphocyte infiltration and higher IL-6/TNF-α across reproductive and non-reproductive tissues in PCOS, linking inflammation to endocrine/metabolic dysfunction (Frontiers in Immunology, 2024; https://doi.org/10.3389/fimmu.2024.1470283) (schobesberger2024hormonaldysbalanceof pages 12-16).
- Hepatic/metabolic comorbidity: detailed molecular links between liver oxidative/inflammatory stress and PCOS metabolic phenotype, supporting MASLD risk (IJMS, 2023; https://doi.org/10.3390/ijms24087454) (khan2023dysregulatedlivermetabolism pages 3-6).

Direct source list with URLs and publication dates
- Wang K, Li Y, Chen Y. Androgen excess: a hallmark of PCOS. Frontiers in Endocrinology. Dec 2023. URL: https://doi.org/10.3389/fendo.2023.1273542 (wang2023androgenexcessa pages 2-3).
- Lonardo MS, et al. Hypothalamic–ovarian axis and adiposity relationship in PCOS. Current Obesity Reports. Jan 2024. URL: https://doi.org/10.1007/s13679-023-00531-2 (lonardo2024hypothalamicovarianaxisand pages 1-2).
- Deng H, et al. Systematic low-grade chronic inflammation in PCOS. Frontiers in Immunology. Dec 2024. URL: https://doi.org/10.3389/fimmu.2024.1470283 (schobesberger2024hormonaldysbalanceof pages 12-16).
- Houston EJ, Templeman NM. Reappraising hyperinsulinemia and insulin resistance in PCOS. Journal of Endocrinology. Feb 2025. URL: https://doi.org/10.1530/joe-24-0269 (houston2025reappraisingtherelationship pages 4-5).
- Azumah R, et al. PCOS GWAS loci gene expression in fetal tissues. Frontiers in Endocrinology. May 2023. URL: https://doi.org/10.3389/fendo.2023.1149473 (azumah2023genesinloci pages 13-13).
- Khan MS, et al. Dysregulated liver metabolism and PCOS. IJMS. Apr 2023. URL: https://doi.org/10.3390/ijms24087454 (khan2023dysregulatedlivermetabolism pages 3-6).
- Additional mechanistic overview excerpts on ovarian theca/granulosa dysfunction and neuroendocrine dynamics are synthesized from the same 2023 Frontiers in Endocrinology review and complementing sources listed above (schobesberger2024hormonaldysbalanceof pages 9-12).

Limitations
- Causality of gut microbiome in human PCOS remains unresolved due to mixed MR results; experimental FMT data support biological plausibility but are preclinical. Genetic fine-mapping and functional studies (e.g., DENND1A.V2) are rapidly evolving; readers should consult the latest functional genomics for locus-specific mechanisms.


References

1. (wang2023androgenexcessa pages 2-3): Kexin Wang, Yanhua Li, and Yu Chen. Androgen excess: a hallmark of polycystic ovary syndrome. Frontiers in Endocrinology, Dec 2023. URL: https://doi.org/10.3389/fendo.2023.1273542, doi:10.3389/fendo.2023.1273542. This article has 73 citations and is from a poor quality or predatory journal.

2. (lonardo2024hypothalamicovarianaxisand pages 1-2): Maria Serena Lonardo, Nunzia Cacciapuoti, Bruna Guida, Mariana Di Lorenzo, Martina Chiurazzi, Simona Damiano, and Ciro Menale. Hypothalamic-ovarian axis and adiposity relationship in polycystic ovary syndrome: physiopathology and therapeutic options for the management of metabolic and inflammatory aspects. Current Obesity Reports, 13:51-70, Jan 2024. URL: https://doi.org/10.1007/s13679-023-00531-2, doi:10.1007/s13679-023-00531-2. This article has 66 citations and is from a peer-reviewed journal.

3. (schobesberger2024hormonaldysbalanceof pages 9-12): H Schobesberger. Hormonal dysbalance of women with polycystic ovary syndrome and acne. Unknown journal, 2024.

4. (azumah2023genesinloci pages 13-13): Rafiatu Azumah, Katja Hummitzsch, Richard A. Anderson, and Raymond J. Rodgers. Genes in loci genetically associated with polycystic ovary syndrome are dynamically expressed in human fetal gonadal, metabolic and brain tissues. Frontiers in Endocrinology, May 2023. URL: https://doi.org/10.3389/fendo.2023.1149473, doi:10.3389/fendo.2023.1149473. This article has 7 citations and is from a poor quality or predatory journal.

5. (houston2025reappraisingtherelationship pages 4-5): Emma Jane Houston and Nicole Meredith Templeman. Reappraising the relationship between hyperinsulinemia and insulin resistance in pcos. The Journal of Endocrinology, Feb 2025. URL: https://doi.org/10.1530/joe-24-0269, doi:10.1530/joe-24-0269. This article has 21 citations.

6. (khan2023dysregulatedlivermetabolism pages 3-6): Muhammad Sohaib Khan, Hee-Sun Kim, Ranhee Kim, Sang Ho Yoon, and Sang Geon Kim. Dysregulated liver metabolism and polycystic ovarian syndrome. International Journal of Molecular Sciences, 24:7454, Apr 2023. URL: https://doi.org/10.3390/ijms24087454, doi:10.3390/ijms24087454. This article has 17 citations and is from a poor quality or predatory journal.

7. (schobesberger2024hormonaldysbalanceof pages 12-16): H Schobesberger. Hormonal dysbalance of women with polycystic ovary syndrome and acne. Unknown journal, 2024.