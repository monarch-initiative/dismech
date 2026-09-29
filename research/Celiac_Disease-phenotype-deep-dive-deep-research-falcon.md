---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T16:25:10.471613'
end_time: '2026-09-25T16:40:41.895787'
duration_seconds: 931.42
template_file: templates/disease_phenotype_mechanism_deep_dive.md
template_sha: "31982cf5035a6a4f9bb42f4a296b39495d9b2883"
template_variables:
  disease_name: Celiac Disease
  mondo_id: MONDO:0005130
  phenotype_focus: Dental Enamel Defects (developmental enamel hypoplasia in permanent
    dentition); Recurrent Aphthous Stomatitis; Arthritis (celiac-associated arthropathy);
    Female infertility (and adverse pregnancy outcomes attributed to celiac disease);
    Constipation (as a presenting bowel habit despite enteropathy); Elevated Hepatic
    Transaminases (celiac hepatitis and its gluten-free-diet reversibility)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 76
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 26
  on_topic: 3
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0005130
    reported_labels:
    - if available
    ontology_label: celiac disease
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Celiac_Disease-phenotype-deep-dive-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Phenotype Mechanism Deep-Dive Research Template

## Target Disease
- **Disease Name:** Celiac Disease
- **MONDO ID:** MONDO:0005130 (if available)

## Scope

This is a narrow, per-phenotype deep dive — not a disease survey. The disease's
core pathophysiology is already curated and is not in question here. The
subject is a small set of clinical manifestations whose **mechanistic link to
the disease is unsettled, contested, or obscure**, and which a broad
mechanism survey would gloss over:

Dental Enamel Defects (developmental enamel hypoplasia in permanent dentition); Recurrent Aphthous Stomatitis; Arthritis (celiac-associated arthropathy); Female infertility (and adverse pregnancy outcomes attributed to celiac disease); Constipation (as a presenting bowel habit despite enteropathy); Elevated Hepatic Transaminases (celiac hepatitis and its gluten-free-diet reversibility)

## Research Objective

For **each** phenotype listed above, report:

1. **Every mechanistic hypothesis in the literature** for how the disease
   produces this phenotype — including minority and historical hypotheses.
   For each hypothesis: the proposed causal chain, step by step, and who has
   proposed or tested it.
2. **The human evidence for and against each hypothesis**: PMIDs with exact
   quotes from the abstracts. Interventional evidence (improvement or
   resolution on disease-specific treatment, e.g. dietary withdrawal) counts
   for causation; note where it is absent.
3. **Non-causal explanations**, treated as first-class competitors: shared
   genetic susceptibility (e.g. HLA haplotypes), coincident autoimmune
   disease, nutritional confounding, medication effects, surveillance or
   ascertainment bias. Say which of these the literature has actually tested
   and what was found.
4. **A verdict per phenotype**, one of:
   - SETTLED — one mechanism is established in humans and generally accepted
   - CONTESTED — two or more live hypotheses with meaningful support each
   - UNKNOWN — association documented, mechanism not established
   Plus: which single study design or observation would most efficiently
   resolve a CONTESTED or UNKNOWN verdict.
5. **Timing and reversibility facts** that constrain mechanism: does the
   phenotype precede diagnosis, does it remit with treatment, is it
   irreversible once formed (for example, defects fixed during tissue
   development), does it track disease activity or persist independently?

**Honesty requirement:** UNKNOWN is a correct and valuable answer. Do not
promote a plausible hypothesis to SETTLED to make the report tidier. Where the
best available evidence is old, small, or indirect, say so.

## Output Format

- One subsection per phenotype, headed by the phenotype name exactly as
  listed above, containing: the competing hypotheses each with its causal
  chain and evidence, the non-causal alternatives and their status, the
  verdict, the resolving experiment, and the timing/reversibility facts.
- Suggested ontology terms where applicable: HP for the phenotype, GO for
  biological processes, CL for cell types.

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Include direct quotes from abstracts to support key statements
- Never cite a paper for a claim its abstract does not make


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

# Phenotype Mechanism Deep-Dive Research Template

## Target Disease
- **Disease Name:** Celiac Disease
- **MONDO ID:** MONDO:0005130 (if available)

## Scope

This is a narrow, per-phenotype deep dive — not a disease survey. The disease's
core pathophysiology is already curated and is not in question here. The
subject is a small set of clinical manifestations whose **mechanistic link to
the disease is unsettled, contested, or obscure**, and which a broad
mechanism survey would gloss over:

Dental Enamel Defects (developmental enamel hypoplasia in permanent dentition); Recurrent Aphthous Stomatitis; Arthritis (celiac-associated arthropathy); Female infertility (and adverse pregnancy outcomes attributed to celiac disease); Constipation (as a presenting bowel habit despite enteropathy); Elevated Hepatic Transaminases (celiac hepatitis and its gluten-free-diet reversibility)

## Research Objective

For **each** phenotype listed above, report:

1. **Every mechanistic hypothesis in the literature** for how the disease
   produces this phenotype — including minority and historical hypotheses.
   For each hypothesis: the proposed causal chain, step by step, and who has
   proposed or tested it.
2. **The human evidence for and against each hypothesis**: PMIDs with exact
   quotes from the abstracts. Interventional evidence (improvement or
   resolution on disease-specific treatment, e.g. dietary withdrawal) counts
   for causation; note where it is absent.
3. **Non-causal explanations**, treated as first-class competitors: shared
   genetic susceptibility (e.g. HLA haplotypes), coincident autoimmune
   disease, nutritional confounding, medication effects, surveillance or
   ascertainment bias. Say which of these the literature has actually tested
   and what was found.
4. **A verdict per phenotype**, one of:
   - SETTLED — one mechanism is established in humans and generally accepted
   - CONTESTED — two or more live hypotheses with meaningful support each
   - UNKNOWN — association documented, mechanism not established
   Plus: which single study design or observation would most efficiently
   resolve a CONTESTED or UNKNOWN verdict.
5. **Timing and reversibility facts** that constrain mechanism: does the
   phenotype precede diagnosis, does it remit with treatment, is it
   irreversible once formed (for example, defects fixed during tissue
   development), does it track disease activity or persist independently?

**Honesty requirement:** UNKNOWN is a correct and valuable answer. Do not
promote a plausible hypothesis to SETTLED to make the report tidier. Where the
best available evidence is old, small, or indirect, say so.

## Output Format

- One subsection per phenotype, headed by the phenotype name exactly as
  listed above, containing: the competing hypotheses each with its causal
  chain and evidence, the non-causal alternatives and their status, the
  verdict, the resolving experiment, and the timing/reversibility facts.
- Suggested ontology terms where applicable: HP for the phenotype, GO for
  biological processes, CL for cell types.

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Include direct quotes from abstracts to support key statements
- Never cite a paper for a claim its abstract does not make


# Celiac Disease (MONDO:0005130): Phenotype–Mechanism Deep Dive

## Scope and evidence standard

This report addresses six manifestations whose association with celiac disease (CeD) is better documented than their mechanism. **GFD** means gluten-free diet; **TG2/tTG** means tissue transglutaminase 2. “Human evidence” is separated from animal or cell-culture evidence. Where the retrieved record did not expose a PMID, I provide the DOI/URL rather than inventing one. Quoted language below is restricted to statements available in the retrieved abstracts or article extracts.

Recent evidence does not justify labeling any of these phenotype mechanisms fully settled. The strongest causal evidence concerns GFD-responsive celiac hepatitis, but even there the downstream hepatic mediator remains uncertain.

| Phenotype | Leading causal hypotheses | Strongest human evidence | Key competing/non-causal explanations | Timing/reversibility | Verdict | Single most efficient resolving study |
|---|---|---|---|---|---|---|
| Dental Enamel Defects (developmental enamel hypoplasia in permanent dentition) | Ameloblast-directed IgA autoimmunity and food-antigen cross-reactivity; calcium/vitamin-D deficiency during amelogenesis; systemic inflammation; genetic susceptibility | Enamel-directed antibodies occur in celiac cohorts, but direct causal experiments are mainly animal-based; observational studies show symmetric chronological defects, while one controlled study found no significant association | Developmental illness, nutritional deficiency unrelated to celiac disease, fluorosis, genetic enamel disorders, regional ascertainment and diagnostic variation | Arises only while enamel is forming; established defects are irreversible. Early diagnosis/GFD may prevent defects in teeth not yet mineralized | CONTESTED | Prospective birth cohort measuring nutrient status and enamel-specific antibodies before and during permanent-tooth mineralization, with standardized dental imaging and treated-versus-untreated exposure analysis |
| Recurrent Aphthous Stomatitis | Hematinic deficiency from malabsorption; gluten-driven mucosal immune inflammation; cytokine-mediated injury; direct oral autoimmunity | RAS is enriched in case-control cohorts; in a small biopsy-confirmed series, four adherent patients improved within six months of GFD, but no mechanism-specific intervention exists | Idiopathic RAS; iron, folate or B12 deficiency from other causes; Behçet disease, Crohn disease, infection, immunodeficiency and medication effects | May precede gastrointestinal symptoms or be the sole presentation; recurrent lesions can improve on GFD, but persistence is possible and individual ulcers heal independently | UNKNOWN | Randomized gluten-withdrawal/gluten-challenge study in newly diagnosed celiac patients with RAS, stratified by corrected versus uncorrected hematinic deficiencies and using blinded ulcer counts |
| Arthritis (celiac-associated arthropathy) | Gluten-driven systemic immune activation; increased permeability and gut–joint trafficking; microbiome-mediated inflammation; nutrient deficiency and altered bone–muscle physiology | A carefully investigated 2023 case had sterile, non-erosive inflammatory polyarthritis resolving within three weeks of GFD; observational ultrasound studies report more synovitis with gluten exposure, but controlled mechanistic evidence is absent | Rheumatoid, psoriatic, reactive or spondyloarthritis; infection; crystal disease; vitamin-D deficiency; coincident autoimmunity; nonspecific arthralgia and referral bias | Can precede celiac diagnosis and occur without gastrointestinal symptoms; some cases remit rapidly on GFD, whereas persistence suggests another rheumatic disorder | UNKNOWN | Prospective inception cohort with rheumatologist-confirmed synovitis, synovial-fluid profiling and blinded ultrasound before GFD and during controlled gluten challenge after remission |
| Female infertility (and adverse pregnancy outcomes attributed to celiac disease) | Anti-TG2 binding inhibits endometrial angiogenesis and trophoblast invasion and promotes apoptosis; placental TG2 inhibition; malabsorption-related iron, folate, B12 or zinc deficiency; systemic inflammation | Patient antibodies bind human syncytiotrophoblast and damage primary trophoblasts in vitro; epidemiologic studies show excess infertility and adverse outcomes concentrated in undiagnosed/untreated disease, with risks attenuated after diagnosis/GFD | Age, BMI, smoking and socioeconomic confounding; thyroid or other autoimmunity; endometriosis/PCOS; shared HLA susceptibility; infertility-clinic selection and surveillance bias | Infertility or miscarriage may precede celiac diagnosis; risks generally diminish after diagnosis and GFD, although robust prospective fertility-treatment trials are lacking | CONTESTED | Multicenter prospective preconception cohort measuring anti-TG2, nutrients and placental/endometrial function before and after GFD, with antibody-negative celiac and nutrient-matched controls |
| Constipation (as a presenting bowel habit despite enteropathy) | Inflammation-mediated enteric neuromuscular and hormonal dysregulation; autonomic dysfunction; dysbiosis; impaired absorption; low-fiber, ultra-processed GFD after diagnosis | In 12 newly diagnosed patients, four weeks of GFD shortened small-bowel and colonic transit and increased contractility; dietitian-led fiber-quality intervention improved hard stools in treated children | IBS-C, pelvic-floor dysfunction, hypothyroidism, medications, ordinary chronic constipation and low-fiber dietary substitution; small studies lack healthy controls | May present before diagnosis; motility can improve within weeks, but constipation may persist despite mucosal treatment and can also arise from the GFD itself | CONTESTED | Larger controlled longitudinal study combining colonic transit, anorectal manometry, mucosal inflammation, microbiome and quantified fiber intake before and after GFD |
| Elevated Hepatic Transaminases (celiac hepatitis and its gluten-free-diet reversibility) | Increased intestinal permeability permits microbial products and antigens to activate hepatic innate immunity; circulating cytokines; anti-TG2 deposition or activity inhibition; malnutrition-related injury | Classic adult cohort: 67/158 had elevated enzymes and 60/67 normalized after one year of GFD; gluten challenge has reproduced abnormalities. Permeability correlates with AST, but the precise mediator is unproven | Viral or autoimmune hepatitis, MASLD/steatosis, alcohol, medication toxicity, Wilson disease, hemochromatosis and false-positive celiac serology in chronic liver disease | Often present at diagnosis and usually normalize within 6–12 months; persistence requires adherence review and investigation for another liver disease, though some pediatric abnormalities persist beyond one year | CONTESTED | Prospective GFD intervention with serial permeability, portal microbial-product, cytokine and anti-TG2 measurements, paired liver assessment, rigorous adherence monitoring and prespecified exclusion of competing liver diseases |


*Table: Concise synthesis of the six phenotype-specific mechanistic verdicts, reversibility constraints, major alternatives, and highest-yield resolving studies, based on the gathered human and translational evidence (procaccini2007lackofassociation pages 4-5, cobosquevedo2024effectofa pages 4-5, bardella1995prevalenceofhypertransaminasemia pages 1-2, gruper2023autoimmuneamelogenesisimperfecta pages 7-8, anjum2009maternalceliacdisease pages 1-2, tersigni2014celiacdiseaseand pages 7-8, mougui2023isolatedpolyarthritisrevealing pages 2-4).*

## Dental Enamel Defects (developmental enamel hypoplasia in permanent dentition)

### Competing mechanistic hypotheses

**1. Malabsorption during amelogenesis.** The proposed chain is: active childhood CeD → villous injury → reduced calcium, phosphate, vitamin-D and other micronutrient availability → disturbed ameloblast function and enamel mineralization → symmetric, chronologically distributed hypoplasia or hypomineralization. A 2023 overview identifies calcium/vitamin-D malabsorption and immunity as the principal candidate mechanisms and stresses that completed defects are irreversible. A 2007 ultrastructural study likewise contrasted hypocalcemia from malabsorption with ameloblast-directed immunity but did not experimentally distinguish them. (wieser2023dentalmanifestationsand pages 1-2, bossu2007enamelhypoplasiain pages 1-2)

**Human evidence for:** Recent clinical syntheses consistently find more developmental enamel defects in CeD, often symmetric and chronological. A 2024 review included 18 human studies and reported prevalence ranging from 50% to 94.1%, although this unusually broad range reflects heterogeneous definitions and selected cohorts. Its abstract states: **“Symmetrical and chronological defects, according to Aine’s classification, were predominant.”** (Published February 2024; DOI/URL: https://doi.org/10.3390/jcm13051382.) (inchingolo2024celiacdiseaserelatedenamel pages 1-3)

**Human evidence against or limiting:** Nutrient measurements have generally been cross-sectional, often after the causal developmental window. Disease severity does not consistently track defects. A recent study found lower vitamin D in newly diagnosed/nonadherent children but no association between molar-incisor hypomineralization and Marsh grade, which weakens a simple “more villous injury → more enamel damage” model. (tok2025investigationofthe pages 1-2)

**2. Ameloblast-directed autoimmunity and dietary-antigen cross-reactivity.** Proposed chain: gluten-associated loss of peripheral tolerance → predominantly IgA responses against antigens shared by intestinal/food proteins and developing enamel → binding to ameloblast proteins or interference with enamel-matrix assembly → defective mineralization. Gruper et al. found strong reactivity to human κ-casein in approximately 29% of pediatric and 60% of adult CeD cases versus about 9% of controls; every κ-casein-autoantibody-positive CeD patient also recognized at least one ameloblast protein. (Published November 2023; DOI/URL: https://doi.org/10.1038/s41586-023-06776-0.) (gruper2023autoimmuneamelogenesisimperfecta pages 7-8)

**Human evidence for:** The Nature study reports predominantly IgA autoantibodies against ameloblast-specific proteins in CeD and offers antigen-level evidence beyond the older generic “autoimmunity” hypothesis. (gruper2023autoimmuneamelogenesisimperfecta pages 7-8, gruper2023autoimmuneamelogenesisimperfecta pages 1-2)

**Evidence limiting causality:** The decisive serum-transfer and AIRE-knockout experiments were in animals, principally modeling APS-1 rather than ordinary CeD. Thus, they establish that enamel autoantibodies *can* perturb amelogenesis, not that they are the dominant cause of CeD-associated defects in humans. (gruper2023autoimmuneamelogenesisimperfecta pages 18-26, gruper2023autoimmuneamelogenesisimperfecta pages 3-4)

**3. Nonspecific systemic inflammation or developmental illness.** Cytokine exposure during tooth formation could alter ameloblast differentiation and matrix maturation without nutrient deficiency or antigen-specific attack. This remains plausible but is poorly tested in human CeD cohorts.

**4. Shared genetic susceptibility.** HLA-linked immune susceptibility or independent enamel-development variants could produce association without enteropathy directly causing the defect. The literature lists genetics as a candidate, but retrieved studies did not perform family-based segregation or polygenic adjustment. (lucchese2023beyondthegut pages 1-2, cruz2018dentalandoral pages 1-2)

### Non-causal alternatives and evidence against association

Regional fluoride exposure, childhood fever or infection, prematurity, medications, inherited amelogenesis imperfecta, and examiner/classification differences are important competitors. A matched Italian case-control study found enamel hypoplasia in 26% of 50 CeD cases versus 16% of 50 controls, but the difference was nonsignificant (OR 1.84, 95% CI 0.69–4.94; p>0.2). Its abstract concludes: **“The prevalence of enamel hypoplasia was not higher in the study population than in the control group.”** (Published May 2007; DOI/URL: https://doi.org/10.1186/1746-160X-3-25.) (procaccini2007lackofassociation pages 4-5)

### Timing and reversibility

The phenotype records injury only while ameloblasts are forming a crown. It may therefore precede CeD diagnosis by years and can mark clinically silent childhood disease. Once enamel formation is complete, GFD cannot rebuild hypoplastic enamel; it can only prevent injury to teeth still developing. This developmental-window constraint also explains why adult diet-response studies cannot test reversal. (wieser2023dentalmanifestationsand pages 1-2)

### Verdict and resolving experiment

**VERDICT: CONTESTED.** Nutrient deficiency and enamel-directed autoimmunity are both live hypotheses; neither has been isolated in humans.

**Most efficient resolving study:** A prospective pediatric inception cohort enrolled before permanent-tooth mineralization, with serial enamel-protein autoantibodies, calcium/phosphate/vitamin-D status, inflammatory markers, verified gluten exposure, and blinded quantitative dental imaging. Mediation analysis should compare promptly treated children with delayed-diagnosis cases and nutrient-matched non-CeD controls.

**Suggested ontology:** HP: developmental enamel defect / enamel hypoplasia; GO: amelogenesis, biomineral tissue development, calcium-ion homeostasis, adaptive immune response; CL: ameloblast.

## Recurrent Aphthous Stomatitis

### Competing mechanistic hypotheses

**1. Hematinic deficiency.** Active CeD → iron, folate or vitamin-B12 malabsorption → impaired epithelial renewal and altered mucosal immunity → recurrent ulcers. Procaccini et al. explicitly connect RAS with iron, folate and B12 deficiency and recommend checking those deficiencies before CeD screening. (procaccini2007lackofassociation pages 4-5)

**For:** This pathway is biologically coherent, and anemia may improve with GFD. In Shakeri et al., anemia resolved by six months in the two affected biopsy-confirmed patients. (shakeri2009glutensensitivityenteropathy pages 4-5)

**Against:** Aphthae occur in CeD without documented deficiency, and correction of nutrients has not been factorially separated from gluten withdrawal. The hypothesis therefore cannot explain all cases.

**2. Gluten-driven systemic or local immune inflammation.** Gluten exposure → intestinal adaptive response and circulating inflammatory mediators → oral epithelial immune injury. A severe case remitted with the TNF inhibitor etanercept, supporting cytokine dependence, but a single biologic-response case cannot establish that ordinary CeD-associated RAS is TNF-driven. (lucchese2023beyondthegut pages 13-15)

**3. Direct oral autoimmunity.** Circulating CeD antibodies or locally produced immune responses might target oral mucosa. Evidence is weak: the retrieved recent oral-immunopathology study found no IgA, IgG, IgM or C3 deposits in sampled oral mucosa, arguing against a simple deposition mechanism.

**4. Shared immune susceptibility rather than causation.** HLA background or general autoimmunity could predispose independently to both CeD and idiopathic RAS. This has not been adequately tested with genetically matched relatives.

### Human association and intervention evidence

In the Italian case-control study, RAS occurred in 36% of CeD cases versus 12% of controls (OR 4.13, 95% CI 1.47–11.55; p=0.0091). The abstract states: **“RAS was significantly more frequent in patients with CD.”** (procaccini2007lackofassociation pages 4-5)

Shakeri et al. screened 247 patients with recurrent aphthae: seven had positive serology and compatible duodenal histology, a prevalence of 2.83% versus an estimated Iranian background prevalence of 0.9%. Four patients adhering strictly to GFD showed noticeable improvement over six months. The abstract states: **“Four patients who adhered to a strict gluten-free diet showed noticeable improvement in their aphthous lesions.”** (Published June 2009; DOI/URL: https://doi.org/10.1186/1471-230X-9-44.) This is supportive intervention evidence, but uncontrolled and based on four responders. (shakeri2009glutensensitivityenteropathy pages 4-5)

### Non-causal alternatives

Idiopathic RAS is common. Behçet disease, Crohn disease, infection, giardiasis, common variable immunodeficiency, autoimmune enteropathy, tropical sprue, peptic duodenitis, medications, trauma, stress, and non-CeD hematinic deficiency can produce similar ulcers. Ascertainment is substantial because persistent RAS prompts testing for CeD. These alternatives are recognized but rarely excluded systematically. (lucchese2023beyondthegut pages 1-2, shakeri2009glutensensitivityenteropathy pages 4-5)

### Timing and reversibility

RAS may precede gastrointestinal symptoms and can be the sole presenting feature. Individual ulcers heal, while recurrence frequency may decline within two to six months of GFD. Persistence despite mucosal healing suggests idiopathic RAS, uncorrected deficiency, continued gluten exposure, or another systemic disease. (shakeri2009glutensensitivityenteropathy pages 4-5)

### Verdict and resolving experiment

**VERDICT: UNKNOWN.** The association and occasional GFD response are credible, but no single mechanism is established.

**Most efficient resolving study:** In newly diagnosed CeD with active RAS, randomize immediate versus short deferred GFD under ethical monitoring while independently randomizing correction of iron/folate/B12 deficiency; use blinded ulcer counts and a controlled gluten challenge after remission.

**Suggested ontology:** HP: recurrent aphthous stomatitis; GO: oral mucosal immune response, epithelial wound healing, cytokine-mediated signaling; CL: oral keratinocyte, neutrophil, CD4-positive T cell.

## Arthritis (celiac-associated arthropathy)

### Mechanistic hypotheses

**1. Gluten-driven systemic immune activation.** Gluten-reactive intestinal immunity → circulating cytokines/activated lymphocytes → sterile synovitis. Oxidative stress and altered innate/adaptive immunity are repeatedly proposed, but synovial tissue has rarely been profiled. (poddighe2025prevalenceofjoint pages 1-2, poddighe2025prevalenceofjoint pages 12-13)

**2. Gut-barrier/gut–joint axis.** Enteropathy and increased permeability → translocation of microbial products or antigens → distal joint inflammation. A related microbiome model proposes dysbiosis → altered short-chain-fatty-acid production and regulatory-T-cell function → systemic inflammation. These mechanisms are extrapolated from systemic inflammatory disease and have not been demonstrated specifically in celiac synovium. (clemente2018theroleof pages 6-7)

**3. Molecular cross-reactivity or shared autoimmunity.** CeD and rheumatoid, psoriatic or spondyloarthritis may coexist because of overlapping immune susceptibility rather than CeD directly producing arthritis. This is a major competing explanation.

**4. Nutritional musculoskeletal effects.** Vitamin-D deficiency, osteomalacia, anemia or malnutrition may produce pain and weakness, but do not readily explain objectively inflammatory, leukocyte-rich synovial fluid.

### Human evidence

The clearest recent observation is a 28-year-old woman with eight weeks of sterile, nonerosive polyarthritis affecting small and large peripheral joints. Infectious studies, crystals, ANA, rheumatoid factor, anti-CCP, ANCA and HLA-B27 were negative; imaging showed synovitis without erosions. CeD was confirmed by high anti-TG2 and Marsh 3b histology. GFD produced complete joint resolution in three weeks, normalization of laboratory tests by 48 weeks, and no recurrence at two years. The abstract states: **“Her joint symptoms resolved in 3 weeks.”** (Published January 2023; DOI/URL: https://doi.org/10.1177/2050313X231186305.) This is a strong dechallenge observation but still one case. (mougui2023isolatedpolyarthritisrevealing pages 1-2, mougui2023isolatedpolyarthritisrevealing pages 2-4)

A systematic review/meta-analysis searching through November 2024 found joint complaints in 530 of 6,901 CeD patients without diagnosed rheumatic comorbidity, weighted prevalence 10.7% (95% CI 6.9–15.1). Ultrasound studies found more subclinical synovitis in gluten-consuming than GFD-treated children. However, heterogeneity, secondary outcome reporting and small-study/publication bias were substantial. (poddighe2025prevalenceofjoint pages 1-2, poddighe2025prevalenceofjoint pages 12-13)

### Non-causal alternatives

Rheumatoid arthritis, juvenile idiopathic arthritis, psoriatic arthritis, axial spondyloarthritis, reactive arthritis, infection, crystal disease, hypermobility, osteomalacia and nonspecific arthralgia must be separated from celiac-associated sterile arthritis. Shared HLA or polyautoimmunity and referral surveillance are realistic explanations. Only isolated reports have performed the breadth of exclusion seen above.

### Timing and reversibility

Arthritis can precede CeD diagnosis and occur without gastrointestinal symptoms. Some inflammatory cases resolve rapidly on GFD, while persistent, erosive, seropositive, axial or enthesitic disease should prompt a separate rheumatologic diagnosis.

### Verdict and resolving experiment

**VERDICT: UNKNOWN.** A GFD-responsive inflammatory arthropathy appears real, but its immune mechanism and population frequency are not established.

**Most efficient resolving study:** A prospective inception cohort of untreated CeD with rheumatologist-confirmed synovitis, serial blinded ultrasound/MRI and synovial-fluid immunophenotyping before and after GFD, followed—only after remission—by controlled gluten challenge.

**Suggested ontology:** HP: arthritis, polyarthritis, synovitis; GO: leukocyte migration, inflammatory response, intestinal epithelial barrier; CL: synovial fibroblast, macrophage, neutrophil, T lymphocyte.

## Female infertility (and adverse pregnancy outcomes attributed to celiac disease)

### Mechanistic hypotheses

**1. Anti-TG2 injury to endometrium and placenta.** Active CeD → circulating anti-TG2 IgA/IgG → binding to endometrial endothelial cells and trophoblast/syncytiotrophoblast TG2 → inhibition of TG2 activity, matrix metalloproteinases, angiogenesis and trophoblast invasion → impaired implantation, placentation, fetal growth or pregnancy maintenance.

Anjum et al. showed that CeD IgA bound the maternal-facing syncytiotrophoblast significantly more than control IgA (p<0.0001); preabsorption with recombinant TG2 reduced staining, and bound IgA inhibited local TG2 activity. Their abstract concludes: **“These data indicate that direct immune effects in untreated CD women may compromise placental function.”** (Published February 2009; DOI/URL: https://doi.org/10.1186/1477-7827-7-16.) This is human placental-tissue evidence, not an in-vivo pregnancy intervention. (anjum2009maternalceliacdisease pages 1-2)

Di Simone et al. exposed primary human trophoblasts to commercial anti-TG2 or IgG isolated from three untreated CeD women. Antibodies bound trophoblasts, reduced invasiveness and matrix-metalloprotease activity, and increased TUNEL/annexin-V apoptosis. The title/abstract conclusion—**“Anti-Tissue Transglutaminase Antibodies From Celiac Patients Are Responsible for Trophoblast Damage via Apoptosis In Vitro”**—accurately limits the evidence to cell culture. (Published October 2010; DOI/URL: https://doi.org/10.1038/ajg.2010.233.) (simone2010antitissuetransglutaminaseantibodies pages 1-2)

**2. Nutritional/endocrine impairment.** Villous injury → iron, folate, B12, zinc, selenium or energy deficiency → disturbed hypothalamic–pituitary–ovarian signaling, ovulation, endometrial competence and fetal growth. This likely contributes in severe malabsorptive disease, but contemporary analyses do not support nutrient deficiency as the sole explanation. (tersigni2014celiacdiseaseand pages 6-7, arvanitakis2022adversepregnancyoutcomes pages 1-2)

**3. Systemic inflammation and altered immune tolerance.** Gluten-driven inflammation could impair decidualization and maternal–fetal tolerance independently of antibody binding. Human mechanistic specificity is limited.

**4. Genital-tract dysbiosis/shared HLA susceptibility.** A 2023 study found altered vaginal/endometrial Lactobacillus composition in recurrent-pregnancy-loss patients, but similar changes occurred in both HLA-DQ2/DQ8-positive and negative groups. This argues that dysbiosis may accompany recurrent loss rather than specifically mediate CeD.

### Human epidemiology and treatment-response constraints

A 2024 Iranian case-control study found positive anti-TG2 serology in 8/100 infertile women versus 1/200 fertile controls; four infertile women had biopsy-confirmed CeD, whereas the seropositive control biopsy was negative. Adjusted association: OR 9.92 (95% CI 1.17–84.21), but the interval is very wide and infertility-clinic selection is important. Its abstract states: **“Increased levels of Anti-TTG Ab were independently associated with infertility.”** (Published May 2024; DOI/URL: https://doi.org/10.5812/semj-145384.) (rahimpour2024thefrequencyof pages 1-2)

For pregnancy, an 18-study meta-analysis found increased risks of spontaneous abortion (RR 1.35, 95% CI 1.10–1.65), fetal-growth restriction (RR 1.68, 1.34–2.10), stillbirth (RR 1.57, 1.17–2.10), preterm delivery (RR 1.29, 1.12–1.49), cesarean delivery (RR 1.10, 1.03–1.16), and mean birthweight 176 g lower. Crucially, fetal-growth restriction, stillbirth, preterm birth and lower birthweight were confined to undiagnosed CeD; early-diagnosed disease was not associated with those outcomes. The abstract concludes: **“Early CD diagnosis and appropriate management with GFD may ameliorate these associations.”** (Published December 2022; DOI/URL: https://doi.org/10.20524/aog.2022.0764.) (arvanitakis2022adversepregnancyoutcomes pages 1-2)

Earlier treatment-stratified estimates similarly showed untreated-versus-treated differences: IUGR RR 1.98 versus 1.28, low birthweight 2.47 versus 1.22, and preterm delivery 1.62 versus 1.20; treated estimates crossed unity. (tersigni2014celiacdiseaseand pages 7-8)

### Non-causal alternatives

Maternal age, BMI, smoking, socioeconomic status, thyroid disease, type-1 diabetes, antiphospholipid syndrome, endometriosis, PCOS, diminished ovarian reserve and paternal factors may confound the association. Shared HLA and heightened medical surveillance are plausible. Many cohorts adjusted incompletely for maternal age and did not objectively verify GFD adherence. (arvanitakis2022adversepregnancyoutcomes pages 12-13)

### Timing and reversibility

Infertility, miscarriage or fetal-growth restriction may be the presenting feature of silent CeD. Risk attenuation after diagnosis/GFD supports modifiability, but conception after GFD is not randomized proof. Placental injury is pregnancy-specific; enamel-like irreversibility does not apply, although damage in an established pregnancy may not be fully reversible.

### Verdict and resolving experiment

**VERDICT: CONTESTED.** Direct anti-TG2 effects are experimentally strong in human cells/tissue, while nutritional and inflammatory pathways remain credible; clinical causation is supported but not mechanism-specific.

**Most efficient resolving study:** A multicenter preconception cohort with serial anti-TG2 titers, nutrient panels, endometrial vascular imaging/biomarkers, verified GFD adherence and placental pathology, including antibody-negative CeD and nutrient-matched controls. An antibody-mediated mechanism predicts outcomes by anti-TG2 independently of villous injury and nutrient status.

**Suggested ontology:** HP: female infertility, recurrent spontaneous abortion, fetal growth restriction, stillbirth, preterm birth; GO: trophoblast migration, angiogenesis, apoptotic process, extracellular-matrix organization; CL: syncytiotrophoblast, extravillous trophoblast, endometrial endothelial cell.

## Constipation (as a presenting bowel habit despite enteropathy)

### Competing mechanistic hypotheses

**1. Enteropathy-induced dysmotility.** Gluten exposure → mucosal inflammation → disrupted enteroendocrine, enteric-neural and autonomic signaling → weaker or poorly coordinated intestinal/colonic contractions → slow transit and constipation. Hormonal imbalance, impaired absorption, dysbiosis and autonomic dysfunction are variants of this pathway. (cobosquevedo2024effectofa pages 7-8, usaisatta2018motilitydisordersin pages 1-3)

The strongest recent test enrolled 12 newly diagnosed CeD and 12 non-celiac gluten-sensitivity patients. In CeD, four weeks of GFD reduced small-bowel transit from 252±39 to 196±27 minutes and colonic transit from 2,150±1,020 to 1,450±348 minutes. Small-bowel maximum pressure rose from 109±23 to 198±17 mmHg, contractions from 1.68±1.4 to 3.74±1.3 per minute, and motility index from 136±32 to 206±24. The abstract states: **“CD patients experienced significant reductions in both intestinal and colonic transit times, along with enhanced small intestine contractility.”** (Published March 2024; DOI/URL: https://doi.org/10.3390/jcm13061716.) The absence of healthy controls, tiny sample, four-week duration and only 2/12 baseline CeD patients with constipation limit phenotype-specific inference. (cobosquevedo2024effectofa pages 1-2, cobosquevedo2024effectofa pages 4-5, cobosquevedo2024effectofa pages 8-10)

**2. Persistent low-grade inflammation.** Incomplete mucosal recovery despite GFD could sustain neuro-immunomodulatory dysfunction. Studies disagree on whether all regional motor abnormalities normalize, making this a live explanation for persistence. (usaisatta2018motilitydisordersin pages 1-3, usaisatta2018motilitydisordersin pages 4-6)

**3. Diet-induced constipation after diagnosis.** GFD products may be low in fiber and high in refined starch, sugar and fat. In 72 children, dietitian-led education increased dietary quality; 92% achieved normal bowel habits and hard stools resolved in 80% of those constipated at baseline (p<0.001). Thus, post-diagnosis constipation may be caused by the treatment diet rather than active CeD. (Published March 2021; DOI/URL: https://doi.org/10.3390/nu13041108.) (suarezgonzalez2021glutenfreedietnutritional pages 1-2)

### Non-causal alternatives

IBS-C, ordinary chronic idiopathic constipation, pelvic-floor dyssynergia, hypothyroidism, medications, low fluid/fiber intake and psychosocial factors are first-class competitors. In treated adults, constipation at diagnosis predicted persistent gastrointestinal symptoms (OR 7.5, 95% CI 1.3–42), while persistent symptoms did not correlate with follow-up duodenal histology, arguing that ongoing constipation is not necessarily active enteropathy.

### Timing and reversibility

Constipation can be the presenting bowel habit before CeD diagnosis. Objective transit may improve within four weeks of GFD, before complete histological recovery, but symptoms may persist independently. Conversely, constipation can emerge after GFD because of low-fiber substitutes.

### Verdict and resolving experiment

**VERDICT: CONTESTED.** Reversible dysmotility is demonstrated, but it is uncertain whether it explains constipation specifically, and treated-diet/functional mechanisms have independent support.

**Most efficient resolving study:** A larger untreated-CeD cohort stratified by Rome-defined constipation, with wireless transit, anorectal manometry, mucosal inflammatory/enteroendocrine markers, microbiome profiling and measured fiber intake before and after GFD.

**Suggested ontology:** HP: constipation, slow-transit constipation; GO: gastrointestinal motility, enteric nervous-system development/function, smooth-muscle contraction; CL: enteric neuron, enteroendocrine cell, intestinal smooth-muscle cell, interstitial cell of Cajal.

## Elevated Hepatic Transaminases (celiac hepatitis and its gluten-free-diet reversibility)

### Definition

“Celiac hepatitis” is mild, otherwise unexplained hepatocellular injury in confirmed CeD that resolves with GFD. It is a diagnosis of exclusion and should not be used for autoimmune hepatitis, viral hepatitis, MASLD or drug injury merely coexisting with CeD. (kim2020celiacdiseaseand pages 1-2)

### Mechanistic hypotheses

**1. Permeable gut–liver axis.** Gluten-induced zonulin/tight-junction disruption → portal delivery of microbial products, toxins, antigens and cytokines → hepatic Toll-like-receptor and innate-immune activation → hepatocyte injury and ALT/AST release. Human studies found higher lactulose–mannitol permeability ratios in CeD patients with elevated enzymes, association with AST, and improvement with GFD. This is the best-supported mechanistic pathway, but the responsible portal mediator has not been identified. (seidita2024celiacdiseaseand pages 12-13)

**2. Anti-TG2-mediated hepatic injury.** Circulating or deposited anti-TG2 IgA → altered extracellular TG2 activity in liver → impaired matrix repair or local immune injury. Anti-TG2 deposits have been observed in liver biopsy, but deposition does not explain why only a subset develops hypertransaminasemia and is not established as pathogenic. (kim2020celiacdiseaseand pages 5-6, hoffmanova2018celiacdiseaseand pages 6-8)

**3. Systemic cytokines/immune trafficking.** Intestinal inflammation may generate hepatotoxic cytokines or activated lymphocytes. Evidence remains indirect.

**4. Malnutrition, fatty liver or altered bile-acid signaling.** Severe malnutrition may promote steatosis, while after treatment, weight gain and composition of processed GFD can promote MASLD. In treated CeD, reduced FGF19 and altered bile-acid signaling have been associated with steatosis, especially with persistent anti-TG2, but this is more relevant to fatty liver than classic reversible celiac hepatitis.

### Human causation and counterevidence

In the classic cohort of 158 consecutive adults, 67 (42%) had elevated AST and/or ALT at diagnosis; after one year of strict GFD, 60/67 (95%) normalized. The abstract-level result supports a strong dechallenge effect. Of seven persistent cases, three had hepatitis B, one hepatitis C, one autoimmune hepatitis and two fatty infiltration. (Published September 1995; DOI/URL: https://doi.org/10.1002/hep.1840220322.) (bardella1995prevalenceofhypertransaminasemia pages 1-2)

Other series report normalization within 6–12 months, disappearance of CeD antibodies and occasional histologic resolution. Gluten rechallenge has reproduced aminotransferase elevation, serologic relapse and intestinal injury, followed by renewed resolution on GFD—strong evidence that gluten-sensitive liver injury exists. (kim2020celiacdiseaseand pages 1-2, kim2020celiacdiseaseand pages 2-3)

A 2024 review cites pooled hypertransaminasemia prevalence of 21.42% (95% CI 17.02–26.59) and improvement in 86.4% after GFD. However, a contemporary Sicilian pediatric cohort found only 8.1% prevalence and persistence in 53.8% of affected children at 12 months, suggesting geographic/definition differences, incomplete adherence, slower resolution or competing steatosis. (Published December 2024; DOI/URL: https://doi.org/10.3390/nu17010085.) (seidita2024celiacdiseaseand pages 12-13, seidita2024celiacdiseaseand pages 1-2)

### Non-causal alternatives

Autoimmune hepatitis, primary biliary cholangitis, primary sclerosing cholangitis, hepatitis B/C, MASLD, alcohol, medication or supplement toxicity, Wilson disease, hemochromatosis, alpha-1-antitrypsin deficiency and muscle sources of AST must be excluded. Chronic liver disease may also cause false-positive anti-tTG, so biopsy-confirmed or otherwise robust CeD diagnosis matters. Persistent elevation despite verified GFD is positive evidence for an alternative liver disease. (kim2020celiacdiseaseand pages 2-3, kim2020celiacdiseaseand pages 4-5, hoffmanova2018celiacdiseaseand pages 6-8)

### Timing and reversibility

Hypertransaminasemia is often present at CeD diagnosis and may be the only clue. Most genuine celiac hepatitis normalizes within 6–12 months; some patients need longer. Failure to decline should trigger adherence assessment and a full liver workup rather than indefinite attribution to CeD.

### Verdict and resolving experiment

**VERDICT: CONTESTED for the mechanism; the existence of a gluten-responsive hepatic phenotype is well established.** GFD dechallenge/rechallenge establishes causation in a subset, but permeability, anti-TG2, cytokines and steatosis remain competing mediators.

**Most efficient resolving study:** Prospective newly diagnosed CeD with prespecified exclusion of other liver diseases, rigorous gluten-exposure monitoring, serial intestinal-permeability testing, portal-product surrogates, cytokines, anti-TG2 deposition/activity and quantitative liver imaging before and after GFD. Mediation analysis should test whether permeability change explains ALT/AST normalization.

**Suggested ontology:** HP: elevated hepatic transaminases; GO: intestinal epithelial barrier, Toll-like-receptor signaling, response to lipopolysaccharide, hepatocyte apoptotic process; CL: hepatocyte, Kupffer cell, intestinal epithelial cell.

## Overall interpretation

Across these phenotypes, GFD response is informative but not mechanism-specific: it simultaneously removes antigen, improves enteropathy, changes nutrient absorption and substantially alters diet composition. The most important research gap is therefore not another uncontrolled before/after series, but studies that measure candidate mediators longitudinally and include antibody-negative, nutrient-matched, genetically informative and disease-control groups. Current evidence supports **CONTESTED** verdicts for enamel defects, reproductive outcomes, constipation and the mechanism of celiac hepatitis, and **UNKNOWN** verdicts for RAS and celiac-associated arthropathy.

References

1. (procaccini2007lackofassociation pages 4-5): Maurizio Procaccini, Giuseppina Campisi, Pantaleo Bufo, Domenico Compilato, Claudia Massaccesi, Carlo Catassi, and Lorenzo Lo Muzio. Lack of association between celiac disease and dental enamel hypoplasia in a case-control study from an italian central region. Head & Face Medicine, 3:25-25, May 2007. URL: https://doi.org/10.1186/1746-160x-3-25, doi:10.1186/1746-160x-3-25. This article has 89 citations and is from a peer-reviewed journal.

2. (cobosquevedo2024effectofa pages 4-5): Orestes Cobos-Quevedo, Gildardo Alfonso Hernández, Xaira Jimena Rivera-Gutiérrez, Peter Grube-Pagola, and José María Remes-Troche. Effect of a gluten-free diet on whole gut transit time in celiac disease (cd) and non-celiac gluten sensitivity (ncgs) patients: a study using the wireless motility capsule (wmc). Journal of Clinical Medicine, 13:1716, Mar 2024. URL: https://doi.org/10.3390/jcm13061716, doi:10.3390/jcm13061716. This article has 3 citations.

3. (bardella1995prevalenceofhypertransaminasemia pages 1-2): Maria Teresa Bardella, Mirella Fraquelli, Maurizio Quatrini, Nicoletta Molteni, Paolo Bianchi, and Dario Conte. Prevalence of hypertransaminasemia in adult celiac patients and effect of gluten‐free diet. Hepatology, 22:833-836, Sep 1995. URL: https://doi.org/10.1002/hep.1840220322, doi:10.1002/hep.1840220322. This article has 315 citations and is from a highest quality peer-reviewed journal.

4. (gruper2023autoimmuneamelogenesisimperfecta pages 7-8): Yael Gruper, Anette S. B. Wolff, Liad Glanz, Frantisek Spoutil, Mihaela Cuida Marthinussen, Adriana Osickova, Yonatan Herzig, Yael Goldfarb, Goretti Aranaz-Novaliches, Jan Dobeš, Noam Kadouri, Osher Ben-Nun, Amit Binyamin, Bar Lavi, Tal Givony, Razi Khalaila, Tom Gome, Tomáš Wald, Blanka Mrazkova, Carmel Sochen, Marine Besnard, Shifra Ben-Dor, Ester Feldmesser, Elisaveta M. Orlova, Csaba Hegedűs, István Lampé, Tamás Papp, Szabolcs Felszeghy, Radislav Sedlacek, Esti Davidovich, Noa Tal, Dror S. Shouval, Raanan Shamir, Carole Guillonneau, Zsuzsa Szondy, Knut E. A. Lundin, Radim Osicka, Jan Prochazka, Eystein S. Husebye, and Jakub Abramson. Autoimmune amelogenesis imperfecta in patients with aps-1 and coeliac disease. Nature, 624:653-662, Nov 2023. URL: https://doi.org/10.1038/s41586-023-06776-0, doi:10.1038/s41586-023-06776-0. This article has 25 citations and is from a highest quality peer-reviewed journal.

5. (anjum2009maternalceliacdisease pages 1-2): Naheed Anjum, Philip N Baker, Nicola J Robinson, and John D Aplin. Maternal celiac disease autoantibodies bind directly to syncytiotrophoblast and inhibit placental tissue transglutaminase activity. Reproductive Biology and Endocrinology, Feb 2009. URL: https://doi.org/10.1186/1477-7827-7-16, doi:10.1186/1477-7827-7-16. This article has 89 citations and is from a peer-reviewed journal.

6. (tersigni2014celiacdiseaseand pages 7-8): C. Tersigni, R. Castellani, C. de Waure, A. Fattorossi, M. De Spirito, A. Gasbarrini, G. Scambia, and N. Di Simone. Celiac disease and reproductive disorders: meta-analysis of epidemiologic associations and potential pathogenic mechanisms. Human reproduction update, 20 4:582-93, Jul 2014. URL: https://doi.org/10.1093/humupd/dmu007, doi:10.1093/humupd/dmu007. This article has 260 citations and is from a highest quality peer-reviewed journal.

7. (mougui2023isolatedpolyarthritisrevealing pages 2-4): Ahmed Mougui and Imane El Bouchti. Isolated polyarthritis revealing celiac disease: a case report. SAGE Open Medical Case Reports, Jan 2023. URL: https://doi.org/10.1177/2050313x231186305, doi:10.1177/2050313x231186305. This article has 2 citations and is from a peer-reviewed journal.

8. (wieser2023dentalmanifestationsand pages 1-2): Herbert Wieser, Massimo Amato, Mario Caggiano, and Carolina Ciacci. Dental manifestations and celiac disease—an overview. Journal of Clinical Medicine, 12:2801, Apr 2023. URL: https://doi.org/10.3390/jcm12082801, doi:10.3390/jcm12082801. This article has 36 citations.

9. (bossu2007enamelhypoplasiain pages 1-2): M Bossu, A Bartoli, G Orsini, and E Luppino. Enamel hypoplasia in coeliac children: a potential clinical marker of early diagnosis. Unknown journal, 2007.

10. (inchingolo2024celiacdiseaserelatedenamel pages 1-3): Alessio Danilo Inchingolo, Gianna Dipalma, Fabio Viapiano, Anna Netti, Irene Ferrara, Anna Maria Ciocia, Antonio Mancini, Daniela Di Venere, Andrea Palermo, Angelo Michele Inchingolo, and Francesco Inchingolo. Celiac disease-related enamel defects: a systematic review. Journal of Clinical Medicine, 13:1382, Feb 2024. URL: https://doi.org/10.3390/jcm13051382, doi:10.3390/jcm13051382. This article has 26 citations.

11. (tok2025investigationofthe pages 1-2): Ayşegül Tok, Nilgün Altınsoy, and Ferda Özbay Hoşnut. Investigation of the frequency of molar incisor hypomineralisation in childhood celiac disease and evaluation with nutritional factors and calcium metabolism. Frontiers in Pediatrics, Aug 2025. URL: https://doi.org/10.3389/fped.2025.1603751, doi:10.3389/fped.2025.1603751. This article has 1 citations.

12. (gruper2023autoimmuneamelogenesisimperfecta pages 1-2): Yael Gruper, Anette S. B. Wolff, Liad Glanz, Frantisek Spoutil, Mihaela Cuida Marthinussen, Adriana Osickova, Yonatan Herzig, Yael Goldfarb, Goretti Aranaz-Novaliches, Jan Dobeš, Noam Kadouri, Osher Ben-Nun, Amit Binyamin, Bar Lavi, Tal Givony, Razi Khalaila, Tom Gome, Tomáš Wald, Blanka Mrazkova, Carmel Sochen, Marine Besnard, Shifra Ben-Dor, Ester Feldmesser, Elisaveta M. Orlova, Csaba Hegedűs, István Lampé, Tamás Papp, Szabolcs Felszeghy, Radislav Sedlacek, Esti Davidovich, Noa Tal, Dror S. Shouval, Raanan Shamir, Carole Guillonneau, Zsuzsa Szondy, Knut E. A. Lundin, Radim Osicka, Jan Prochazka, Eystein S. Husebye, and Jakub Abramson. Autoimmune amelogenesis imperfecta in patients with aps-1 and coeliac disease. Nature, 624:653-662, Nov 2023. URL: https://doi.org/10.1038/s41586-023-06776-0, doi:10.1038/s41586-023-06776-0. This article has 25 citations and is from a highest quality peer-reviewed journal.

13. (gruper2023autoimmuneamelogenesisimperfecta pages 18-26): Yael Gruper, Anette S. B. Wolff, Liad Glanz, Frantisek Spoutil, Mihaela Cuida Marthinussen, Adriana Osickova, Yonatan Herzig, Yael Goldfarb, Goretti Aranaz-Novaliches, Jan Dobeš, Noam Kadouri, Osher Ben-Nun, Amit Binyamin, Bar Lavi, Tal Givony, Razi Khalaila, Tom Gome, Tomáš Wald, Blanka Mrazkova, Carmel Sochen, Marine Besnard, Shifra Ben-Dor, Ester Feldmesser, Elisaveta M. Orlova, Csaba Hegedűs, István Lampé, Tamás Papp, Szabolcs Felszeghy, Radislav Sedlacek, Esti Davidovich, Noa Tal, Dror S. Shouval, Raanan Shamir, Carole Guillonneau, Zsuzsa Szondy, Knut E. A. Lundin, Radim Osicka, Jan Prochazka, Eystein S. Husebye, and Jakub Abramson. Autoimmune amelogenesis imperfecta in patients with aps-1 and coeliac disease. Nature, 624:653-662, Nov 2023. URL: https://doi.org/10.1038/s41586-023-06776-0, doi:10.1038/s41586-023-06776-0. This article has 25 citations and is from a highest quality peer-reviewed journal.

14. (gruper2023autoimmuneamelogenesisimperfecta pages 3-4): Yael Gruper, Anette S. B. Wolff, Liad Glanz, Frantisek Spoutil, Mihaela Cuida Marthinussen, Adriana Osickova, Yonatan Herzig, Yael Goldfarb, Goretti Aranaz-Novaliches, Jan Dobeš, Noam Kadouri, Osher Ben-Nun, Amit Binyamin, Bar Lavi, Tal Givony, Razi Khalaila, Tom Gome, Tomáš Wald, Blanka Mrazkova, Carmel Sochen, Marine Besnard, Shifra Ben-Dor, Ester Feldmesser, Elisaveta M. Orlova, Csaba Hegedűs, István Lampé, Tamás Papp, Szabolcs Felszeghy, Radislav Sedlacek, Esti Davidovich, Noa Tal, Dror S. Shouval, Raanan Shamir, Carole Guillonneau, Zsuzsa Szondy, Knut E. A. Lundin, Radim Osicka, Jan Prochazka, Eystein S. Husebye, and Jakub Abramson. Autoimmune amelogenesis imperfecta in patients with aps-1 and coeliac disease. Nature, 624:653-662, Nov 2023. URL: https://doi.org/10.1038/s41586-023-06776-0, doi:10.1038/s41586-023-06776-0. This article has 25 citations and is from a highest quality peer-reviewed journal.

15. (lucchese2023beyondthegut pages 1-2): Alberta Lucchese, Dario Di Stasio, Simona De Stefano, Michele Nardone, and Francesco Carinci. Beyond the gut: a systematic review of oral manifestations in celiac disease. Jun 2023. URL: https://doi.org/10.3390/jcm12123874, doi:10.3390/jcm12123874. This article has 38 citations.

16. (cruz2018dentalandoral pages 1-2): I. Cruz, F. Fraiz, A. Celli, J. Amenábar, and Luciana-Reichert-da-Silva Assunção. Dental and oral manifestations of celiac disease. Medicina Oral, Patología Oral y Cirugía Bucal, 23:e639-e645, Nov 2018. URL: https://doi.org/10.4317/medoral.22506, doi:10.4317/medoral.22506. This article has 67 citations.

17. (shakeri2009glutensensitivityenteropathy pages 4-5): Ramin Shakeri, Farhad Zamani, Rasoul Sotoudehmanesh, Afsaneh Amiri, Mehdi Mohamadnejad, Fereydoun Davatchi, Ali Mohammadi Karakani, Reza Malekzadeh, and Farhad Shahram. Gluten sensitivity enteropathy in patients with recurrent aphthous stomatitis. BMC Gastroenterology, 9:44-44, Jun 2009. URL: https://doi.org/10.1186/1471-230x-9-44, doi:10.1186/1471-230x-9-44. This article has 82 citations and is from a peer-reviewed journal.

18. (lucchese2023beyondthegut pages 13-15): Alberta Lucchese, Dario Di Stasio, Simona De Stefano, Michele Nardone, and Francesco Carinci. Beyond the gut: a systematic review of oral manifestations in celiac disease. Jun 2023. URL: https://doi.org/10.3390/jcm12123874, doi:10.3390/jcm12123874. This article has 38 citations.

19. (poddighe2025prevalenceofjoint pages 1-2): Dimitri Poddighe, Gulsamal Zhubanova, Dinara Galiyeva, Kamilla Mussina, and Anders Forss. Prevalence of joint complaints in patients with celiac disease: a systematic review and meta-analysis. Journal of Clinical Medicine, 14:3740, May 2025. URL: https://doi.org/10.3390/jcm14113740, doi:10.3390/jcm14113740. This article has 10 citations.

20. (poddighe2025prevalenceofjoint pages 12-13): Dimitri Poddighe, Gulsamal Zhubanova, Dinara Galiyeva, Kamilla Mussina, and Anders Forss. Prevalence of joint complaints in patients with celiac disease: a systematic review and meta-analysis. Journal of Clinical Medicine, 14:3740, May 2025. URL: https://doi.org/10.3390/jcm14113740, doi:10.3390/jcm14113740. This article has 10 citations.

21. (clemente2018theroleof pages 6-7): Jose C Clemente, Julia Manasson, and Jose U Scher. The role of the gut microbiome in systemic inflammatory disease. British Medical Journal, 360:j5145, Jan 2018. URL: https://doi.org/10.1136/bmj.j5145, doi:10.1136/bmj.j5145. This article has 737 citations.

22. (mougui2023isolatedpolyarthritisrevealing pages 1-2): Ahmed Mougui and Imane El Bouchti. Isolated polyarthritis revealing celiac disease: a case report. SAGE Open Medical Case Reports, Jan 2023. URL: https://doi.org/10.1177/2050313x231186305, doi:10.1177/2050313x231186305. This article has 2 citations and is from a peer-reviewed journal.

23. (simone2010antitissuetransglutaminaseantibodies pages 1-2): Nicoletta Di Simone, Marco Silano, Roberta Castellani, Fiorella Di Nicuolo, Maria C D'Alessio, Francesco Franceschi, Alessandra Tritarelli, Antonio M Leone, Chiara Tersigni, Giovanni Gasbarrini, Nicolò G Silveri, Alessandro Caruso, and Antonio Gasbarrini. Anti-tissue transglutaminase antibodies from celiac patients are responsible for trophoblast damage via apoptosis in vitro. American Journal of Gastroenterology, 105(10):2254-2261, Oct 2010. URL: https://doi.org/10.1038/ajg.2010.233, doi:10.1038/ajg.2010.233. This article has 88 citations and is from a domain leading peer-reviewed journal.

24. (tersigni2014celiacdiseaseand pages 6-7): C. Tersigni, R. Castellani, C. de Waure, A. Fattorossi, M. De Spirito, A. Gasbarrini, G. Scambia, and N. Di Simone. Celiac disease and reproductive disorders: meta-analysis of epidemiologic associations and potential pathogenic mechanisms. Human reproduction update, 20 4:582-93, Jul 2014. URL: https://doi.org/10.1093/humupd/dmu007, doi:10.1093/humupd/dmu007. This article has 260 citations and is from a highest quality peer-reviewed journal.

25. (arvanitakis2022adversepregnancyoutcomes pages 1-2): Konstantinos D. Arvanitakis, A. Siargkas, G. Germanidis, T. Dagklis, and I. Tsakiridis. Adverse pregnancy outcomes in women with celiac disease: a systematic review and meta-analysis. Annals of Gastroenterology, 36:12-24, Dec 2022. URL: https://doi.org/10.20524/aog.2022.0764, doi:10.20524/aog.2022.0764. This article has 38 citations.

26. (rahimpour2024thefrequencyof pages 1-2): Elham Rahimpour, Sara Shojaei-Zarghani, Sedigheh Amooee, Ali Reza Safarpour, Bita Geramizadeh, and Mojgan Zahmatkeshan. The frequency of celiac disease and its association with infertility in women attending infertility clinics: a case-control study in southern iran. Shiraz E-Medical Journal, May 2024. URL: https://doi.org/10.5812/semj-145384, doi:10.5812/semj-145384. This article has 1 citations.

27. (arvanitakis2022adversepregnancyoutcomes pages 12-13): Konstantinos D. Arvanitakis, A. Siargkas, G. Germanidis, T. Dagklis, and I. Tsakiridis. Adverse pregnancy outcomes in women with celiac disease: a systematic review and meta-analysis. Annals of Gastroenterology, 36:12-24, Dec 2022. URL: https://doi.org/10.20524/aog.2022.0764, doi:10.20524/aog.2022.0764. This article has 38 citations.

28. (cobosquevedo2024effectofa pages 7-8): Orestes Cobos-Quevedo, Gildardo Alfonso Hernández, Xaira Jimena Rivera-Gutiérrez, Peter Grube-Pagola, and José María Remes-Troche. Effect of a gluten-free diet on whole gut transit time in celiac disease (cd) and non-celiac gluten sensitivity (ncgs) patients: a study using the wireless motility capsule (wmc). Journal of Clinical Medicine, 13:1716, Mar 2024. URL: https://doi.org/10.3390/jcm13061716, doi:10.3390/jcm13061716. This article has 3 citations.

29. (usaisatta2018motilitydisordersin pages 1-3): Paolo Usai-Satta, Francesco Oppia, Mariantonia Lai, and Francesco Cabras. Motility disorders in celiac disease and non-celiac gluten sensitivity: the impact of a gluten-free diet. Nutrients, 10:1705, Nov 2018. URL: https://doi.org/10.3390/nu10111705, doi:10.3390/nu10111705. This article has 35 citations.

30. (cobosquevedo2024effectofa pages 1-2): Orestes Cobos-Quevedo, Gildardo Alfonso Hernández, Xaira Jimena Rivera-Gutiérrez, Peter Grube-Pagola, and José María Remes-Troche. Effect of a gluten-free diet on whole gut transit time in celiac disease (cd) and non-celiac gluten sensitivity (ncgs) patients: a study using the wireless motility capsule (wmc). Journal of Clinical Medicine, 13:1716, Mar 2024. URL: https://doi.org/10.3390/jcm13061716, doi:10.3390/jcm13061716. This article has 3 citations.

31. (cobosquevedo2024effectofa pages 8-10): Orestes Cobos-Quevedo, Gildardo Alfonso Hernández, Xaira Jimena Rivera-Gutiérrez, Peter Grube-Pagola, and José María Remes-Troche. Effect of a gluten-free diet on whole gut transit time in celiac disease (cd) and non-celiac gluten sensitivity (ncgs) patients: a study using the wireless motility capsule (wmc). Journal of Clinical Medicine, 13:1716, Mar 2024. URL: https://doi.org/10.3390/jcm13061716, doi:10.3390/jcm13061716. This article has 3 citations.

32. (usaisatta2018motilitydisordersin pages 4-6): Paolo Usai-Satta, Francesco Oppia, Mariantonia Lai, and Francesco Cabras. Motility disorders in celiac disease and non-celiac gluten sensitivity: the impact of a gluten-free diet. Nutrients, 10:1705, Nov 2018. URL: https://doi.org/10.3390/nu10111705, doi:10.3390/nu10111705. This article has 35 citations.

33. (suarezgonzalez2021glutenfreedietnutritional pages 1-2): Marta Suárez-González, Carlos Bousoño-García, Santiago Jiménez-Treviño, and Juan José Díaz-Martín. Gluten-free diet: nutritional strategies to improve eating habits in children with celiac disease: a prospective, single-arm intervention study. Nutrients, 13:1108, Mar 2021. URL: https://doi.org/10.3390/nu13041108, doi:10.3390/nu13041108. This article has 29 citations.

34. (kim2020celiacdiseaseand pages 1-2): Jaimy Villavicencio Kim and George Y. Wu. Celiac disease and elevated liver enzymes: a review. Journal of Clinical and Translational Hepatology, 9:116-124, Dec 2020. URL: https://doi.org/10.14218/jcth.2020.00089, doi:10.14218/jcth.2020.00089. This article has 58 citations.

35. (seidita2024celiacdiseaseand pages 12-13): Aurelio Seidita, Federica Latteri, Mirco Pistone, Alessandra Giuliano, Luca Bertoncello, Giorgia Cavallo, Marta Chiavetta, Francesco Faraci, Alessia Nigro, Alessandro Termini, Laura Verona, Agnese Ammannato, Salvatore Accomando, Francesca Cavataio, Maria Letizia Lospalluti, Michele Citrano, Diana Di Liberto, Maurizio Soresi, Pasquale Mansueto, and Antonio Carroccio. Celiac disease and liver damage: the gut–liver axis strikes back (again)? a retrospective analysis in the light of a literature review. Nutrients, 17:85, Dec 2024. URL: https://doi.org/10.3390/nu17010085, doi:10.3390/nu17010085. This article has 5 citations.

36. (kim2020celiacdiseaseand pages 5-6): Jaimy Villavicencio Kim and George Y. Wu. Celiac disease and elevated liver enzymes: a review. Journal of Clinical and Translational Hepatology, 9:116-124, Dec 2020. URL: https://doi.org/10.14218/jcth.2020.00089, doi:10.14218/jcth.2020.00089. This article has 58 citations.

37. (hoffmanova2018celiacdiseaseand pages 6-8): Iva Hoffmanová, Daniel Sánchez, Ludmila Tučková, and Helena Tlaskalová-Hogenová. Celiac disease and liver disorders: from putative pathogenesis to clinical implications. Nutrients, 10:892, Jul 2018. URL: https://doi.org/10.3390/nu10070892, doi:10.3390/nu10070892. This article has 94 citations.

38. (kim2020celiacdiseaseand pages 2-3): Jaimy Villavicencio Kim and George Y. Wu. Celiac disease and elevated liver enzymes: a review. Journal of Clinical and Translational Hepatology, 9:116-124, Dec 2020. URL: https://doi.org/10.14218/jcth.2020.00089, doi:10.14218/jcth.2020.00089. This article has 58 citations.

39. (seidita2024celiacdiseaseand pages 1-2): Aurelio Seidita, Federica Latteri, Mirco Pistone, Alessandra Giuliano, Luca Bertoncello, Giorgia Cavallo, Marta Chiavetta, Francesco Faraci, Alessia Nigro, Alessandro Termini, Laura Verona, Agnese Ammannato, Salvatore Accomando, Francesca Cavataio, Maria Letizia Lospalluti, Michele Citrano, Diana Di Liberto, Maurizio Soresi, Pasquale Mansueto, and Antonio Carroccio. Celiac disease and liver damage: the gut–liver axis strikes back (again)? a retrospective analysis in the light of a literature review. Nutrients, 17:85, Dec 2024. URL: https://doi.org/10.3390/nu17010085, doi:10.3390/nu17010085. This article has 5 citations.

40. (kim2020celiacdiseaseand pages 4-5): Jaimy Villavicencio Kim and George Y. Wu. Celiac disease and elevated liver enzymes: a review. Journal of Clinical and Translational Hepatology, 9:116-124, Dec 2020. URL: https://doi.org/10.14218/jcth.2020.00089, doi:10.14218/jcth.2020.00089. This article has 58 citations.

## Artifacts

- [Edison artifact artifact-00](Celiac_Disease-phenotype-deep-dive-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 26 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005130` (2 mentions) - the report calls it "if available"; MONDO calls it **celiac disease**