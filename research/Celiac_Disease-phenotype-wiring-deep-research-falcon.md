---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T16:41:51.007147'
end_time: '2026-09-25T16:58:42.267757'
duration_seconds: 1011.26
template_file: templates/disease_phenotype_wiring_research.md
template_sha: "e4c8898a5d741502b1868031e5dbb9e7ad91d698"
template_variables:
  disease_name: Celiac Disease
  mondo_id: MONDO:0005130
  mechanism_nodes: 1. Gluten-Triggered Immune Response (TG2 deamidation of gliadin,
    HLA-DQ2/DQ8 presentation, CD4 T-cell activation); 2. Mixed Th1/Th17/IL-21 Mucosal
    Cytokine Response; 3. Intestinal Epithelial Damage (IL-15/NKG2D-MICA intraepithelial
    lymphocyte cytotoxicity, villous atrophy, crypt hyperplasia); 4. Autoantibody
    Production (anti-TG2 IgA, anti-deamidated-gliadin-peptide antibodies, plasma cells);
    5. Barrier Dysfunction (zonulin, tight junction disruption, increased permeability);
    6. Microbiome Dysbiosis
  phenotype_names: Chronic Diarrhea; Abdominal Pain; Bloating; Constipation; Villous
    Atrophy; Weight Loss; Iron Deficiency Anemia; Fatigue; Growth Failure in Children;
    Dermatitis Herpetiformis; Reduced Bone Mineral Density; Dental Enamel Defects;
    Recurrent Aphthous Stomatitis; Peripheral Neuropathy; Cerebellar Ataxia; Elevated
    Hepatic Transaminases; Vitamin D Deficiency; Small intestinal lymphoma; Osteoporosis;
    Arthritis; Short stature; Female infertility
  established_axis: Dietary gluten leads to TG2-mediated deamidation of gliadin peptides,
    which bind HLA-DQ2/DQ8 with high affinity and activate gluten-reactive CD4 T cells;
    the resulting mixed Th1/Th17/IL-21 cytokine response, together with IL-15-driven
    innate epithelial activation, licenses NKG2D/MICA-mediated intraepithelial lymphocyte
    cytotoxicity, producing villous atrophy and crypt hyperplasia, with anti-TG2 autoantibody
    production by B cells. Corroborated by the ZED1227 TG2-inhibitor randomized trial,
    HLA-DQ2 tetramer studies, and gluten-free-diet remission.
  priority_hubs: '(a) Nutrient malabsorption cascade: villous atrophy leads to reduced
    absorptive surface area and loss of brush-border transporters, producing deficiency
    of iron, folate, vitamin B12, vitamin D, calcium, zinc and fat-soluble vitamins,
    which in turn produce iron deficiency anemia, reduced bone mineral density and
    osteoporosis (also via secondary hyperparathyroidism), growth failure and short
    stature in children, weight loss, and fatigue. Detail which nutrient deficit drives
    which phenotype and where deficiency-independent (inflammatory, e.g. RANKL/OPG
    or cytokine-mediated) contributions are documented, especially for bone disease.
    (b) Extraintestinal autoimmunity by epitope spreading: anti-transglutaminase-3
    (TG3) IgA and dermal IgA-TG3 deposits leading to dermatitis herpetiformis; anti-transglutaminase-6
    (TG6) antibodies and cerebellar Purkinje cell injury leading to gluten ataxia;
    the disputed role of humoral versus T-cell mechanisms in gluten neuropathy. (c)
    Lymphomagenesis: chronic IL-15-driven activation and clonal expansion of intraepithelial
    lymphocytes leading to refractory celiac disease type II (aberrant clonal IELs,
    often with JAK1/STAT3 mutations) progressing to enteropathy-associated T-cell
    lymphoma, and the epidemiological protection conferred by gluten-free diet adherence.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 65
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 27
  on_topic: 2
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 66
  verified: 64
  not_found: 0
  obsolete: 2
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
  obsolete_terms:
  - term_id: CL:0000729
    ontology_label: obsolete tertiary pigment cell
  - term_id: GO:0098742
    ontology_label: obsolete cell-cell adhesion via plasma-membrane adhesion molecules
    replaced_by: GO:0098609
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Celiac_Disease-phenotype-wiring-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Mechanism-to-Phenotype Wiring Research Template

## Target Disease
- **Disease Name:** Celiac Disease
- **MONDO ID:** MONDO:0005130 (if available)

## Context: What Is Already Curated

This disease's knowledge base entry already models the following pathophysiology
mechanism nodes:

1. Gluten-Triggered Immune Response (TG2 deamidation of gliadin, HLA-DQ2/DQ8 presentation, CD4 T-cell activation); 2. Mixed Th1/Th17/IL-21 Mucosal Cytokine Response; 3. Intestinal Epithelial Damage (IL-15/NKG2D-MICA intraepithelial lymphocyte cytotoxicity, villous atrophy, crypt hyperplasia); 4. Autoantibody Production (anti-TG2 IgA, anti-deamidated-gliadin-peptide antibodies, plasma cells); 5. Barrier Dysfunction (zonulin, tight junction disruption, increased permeability); 6. Microbiome Dysbiosis

It also records the following clinical phenotypes, each already evidenced as
occurring in the disease:

Chronic Diarrhea; Abdominal Pain; Bloating; Constipation; Villous Atrophy; Weight Loss; Iron Deficiency Anemia; Fatigue; Growth Failure in Children; Dermatitis Herpetiformis; Reduced Bone Mineral Density; Dental Enamel Defects; Recurrent Aphthous Stomatitis; Peripheral Neuropathy; Cerebellar Ataxia; Elevated Hepatic Transaminases; Vitamin D Deficiency; Small intestinal lymphoma; Osteoporosis; Arthritis; Short stature; Female infertility

The core disease mechanism is already curated in depth and is NOT the subject of
this report. Treat it as established context and do not re-derive, re-survey, or
re-justify it:

Dietary gluten leads to TG2-mediated deamidation of gliadin peptides, which bind HLA-DQ2/DQ8 with high affinity and activate gluten-reactive CD4 T cells; the resulting mixed Th1/Th17/IL-21 cytokine response, together with IL-15-driven innate epithelial activation, licenses NKG2D/MICA-mediated intraepithelial lymphocyte cytotoxicity, producing villous atrophy and crypt hyperplasia, with anti-TG2 autoantibody production by B cells. Corroborated by the ZED1227 TG2-inhibitor randomized trial, HLA-DQ2 tetramer studies, and gluten-free-diet remission.

## Research Objective

The missing layer is the **causal wiring between the mechanism nodes and the
clinical phenotypes**: which pathophysiological process produces which clinical
manifestation, through what intermediates. For **each phenotype listed above**,
report:

1. **The mechanistic chain** from the established disease process to that
   phenotype, as an ordered sequence of steps, one per line, with explicit
   causal verbs ("leads to", "results in"). Start each chain from whichever of
   the existing mechanism nodes is the true proximal upstream step.
2. **Missing intermediate processes**: where the chain passes through a
   process that is NOT in the mechanism node list above (for example a
   malabsorption step, a distinct autoantibody specificity, a clonal expansion
   step), name it explicitly and flag it as a proposed new node.
3. **Primary human evidence** for each causal step: PMIDs with exact quotes
   from the abstracts. Prefer human clinical and interventional studies
   (dietary-withdrawal reversal counts as interventional evidence for a causal
   link). Distinguish evidence source types: human clinical, model organism,
   in vitro, computational.
4. **An evidence grade for the chain as a whole**, one of:
   - ESTABLISHED — causal chain demonstrated in humans, widely accepted
   - SUPPORTED — plausible chain with direct human evidence for most steps
   - PROPOSED — hypothesis in the literature, key steps not demonstrated
   - NOT_ESTABLISHED — the association is documented but no mechanistic chain
     has been demonstrated; competing explanations remain open
5. **Non-causal alternatives** where they are live: if the phenotype may be
   associated through shared genetic background (for example shared HLA
   haplotypes), coincident autoimmunity, or ascertainment rather than through
   downstream causation, say so explicitly.

**Honesty requirement:** "NOT_ESTABLISHED, mechanism unknown" is a correct and
valuable answer. Do NOT manufacture a mechanistic chain to satisfy the request.
A phenotype with no settled mechanism should be reported as exactly that, with
the competing hypotheses named and graded. It is expected that several
phenotypes in the list will end up NOT_ESTABLISHED.

## Priority Hubs

The following convergence hubs are anticipated to route several phenotypes and
must NOT be given shallow treatment. For each, report the full mechanistic
detail and per-branch citations:

(a) Nutrient malabsorption cascade: villous atrophy leads to reduced absorptive surface area and loss of brush-border transporters, producing deficiency of iron, folate, vitamin B12, vitamin D, calcium, zinc and fat-soluble vitamins, which in turn produce iron deficiency anemia, reduced bone mineral density and osteoporosis (also via secondary hyperparathyroidism), growth failure and short stature in children, weight loss, and fatigue. Detail which nutrient deficit drives which phenotype and where deficiency-independent (inflammatory, e.g. RANKL/OPG or cytokine-mediated) contributions are documented, especially for bone disease. (b) Extraintestinal autoimmunity by epitope spreading: anti-transglutaminase-3 (TG3) IgA and dermal IgA-TG3 deposits leading to dermatitis herpetiformis; anti-transglutaminase-6 (TG6) antibodies and cerebellar Purkinje cell injury leading to gluten ataxia; the disputed role of humoral versus T-cell mechanisms in gluten neuropathy. (c) Lymphomagenesis: chronic IL-15-driven activation and clonal expansion of intraepithelial lymphocytes leading to refractory celiac disease type II (aberrant clonal IELs, often with JAK1/STAT3 mutations) progressing to enteropathy-associated T-cell lymphoma, and the epidemiological protection conferred by gluten-free diet adherence.

## Output Format

- One subsection per phenotype, headed by the phenotype name exactly as listed
  above, containing: the numbered causal chain, the evidence grade, PMIDs with
  exact abstract quotes per step, and suggested ontology terms (GO for
  biological processes, CL for cell types, HP for the phenotype itself).
- A final section titled **Proposed New Mechanism Nodes** listing every
  intermediate process flagged in item 2, each with: a suggested node name, its
  upstream node (from the existing list or another proposed node), its
  downstream phenotypes, and the strongest single citation for its causal
  placement.
- A final section titled **Unwired Phenotypes** listing every phenotype graded
  NOT_ESTABLISHED, with one sentence each on what evidence would settle it.

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

# Mechanism-to-Phenotype Wiring Research Template

## Target Disease
- **Disease Name:** Celiac Disease
- **MONDO ID:** MONDO:0005130 (if available)

## Context: What Is Already Curated

This disease's knowledge base entry already models the following pathophysiology
mechanism nodes:

1. Gluten-Triggered Immune Response (TG2 deamidation of gliadin, HLA-DQ2/DQ8 presentation, CD4 T-cell activation); 2. Mixed Th1/Th17/IL-21 Mucosal Cytokine Response; 3. Intestinal Epithelial Damage (IL-15/NKG2D-MICA intraepithelial lymphocyte cytotoxicity, villous atrophy, crypt hyperplasia); 4. Autoantibody Production (anti-TG2 IgA, anti-deamidated-gliadin-peptide antibodies, plasma cells); 5. Barrier Dysfunction (zonulin, tight junction disruption, increased permeability); 6. Microbiome Dysbiosis

It also records the following clinical phenotypes, each already evidenced as
occurring in the disease:

Chronic Diarrhea; Abdominal Pain; Bloating; Constipation; Villous Atrophy; Weight Loss; Iron Deficiency Anemia; Fatigue; Growth Failure in Children; Dermatitis Herpetiformis; Reduced Bone Mineral Density; Dental Enamel Defects; Recurrent Aphthous Stomatitis; Peripheral Neuropathy; Cerebellar Ataxia; Elevated Hepatic Transaminases; Vitamin D Deficiency; Small intestinal lymphoma; Osteoporosis; Arthritis; Short stature; Female infertility

The core disease mechanism is already curated in depth and is NOT the subject of
this report. Treat it as established context and do not re-derive, re-survey, or
re-justify it:

Dietary gluten leads to TG2-mediated deamidation of gliadin peptides, which bind HLA-DQ2/DQ8 with high affinity and activate gluten-reactive CD4 T cells; the resulting mixed Th1/Th17/IL-21 cytokine response, together with IL-15-driven innate epithelial activation, licenses NKG2D/MICA-mediated intraepithelial lymphocyte cytotoxicity, producing villous atrophy and crypt hyperplasia, with anti-TG2 autoantibody production by B cells. Corroborated by the ZED1227 TG2-inhibitor randomized trial, HLA-DQ2 tetramer studies, and gluten-free-diet remission.

## Research Objective

The missing layer is the **causal wiring between the mechanism nodes and the
clinical phenotypes**: which pathophysiological process produces which clinical
manifestation, through what intermediates. For **each phenotype listed above**,
report:

1. **The mechanistic chain** from the established disease process to that
   phenotype, as an ordered sequence of steps, one per line, with explicit
   causal verbs ("leads to", "results in"). Start each chain from whichever of
   the existing mechanism nodes is the true proximal upstream step.
2. **Missing intermediate processes**: where the chain passes through a
   process that is NOT in the mechanism node list above (for example a
   malabsorption step, a distinct autoantibody specificity, a clonal expansion
   step), name it explicitly and flag it as a proposed new node.
3. **Primary human evidence** for each causal step: PMIDs with exact quotes
   from the abstracts. Prefer human clinical and interventional studies
   (dietary-withdrawal reversal counts as interventional evidence for a causal
   link). Distinguish evidence source types: human clinical, model organism,
   in vitro, computational.
4. **An evidence grade for the chain as a whole**, one of:
   - ESTABLISHED — causal chain demonstrated in humans, widely accepted
   - SUPPORTED — plausible chain with direct human evidence for most steps
   - PROPOSED — hypothesis in the literature, key steps not demonstrated
   - NOT_ESTABLISHED — the association is documented but no mechanistic chain
     has been demonstrated; competing explanations remain open
5. **Non-causal alternatives** where they are live: if the phenotype may be
   associated through shared genetic background (for example shared HLA
   haplotypes), coincident autoimmunity, or ascertainment rather than through
   downstream causation, say so explicitly.

**Honesty requirement:** "NOT_ESTABLISHED, mechanism unknown" is a correct and
valuable answer. Do NOT manufacture a mechanistic chain to satisfy the request.
A phenotype with no settled mechanism should be reported as exactly that, with
the competing hypotheses named and graded. It is expected that several
phenotypes in the list will end up NOT_ESTABLISHED.

## Priority Hubs

The following convergence hubs are anticipated to route several phenotypes and
must NOT be given shallow treatment. For each, report the full mechanistic
detail and per-branch citations:

(a) Nutrient malabsorption cascade: villous atrophy leads to reduced absorptive surface area and loss of brush-border transporters, producing deficiency of iron, folate, vitamin B12, vitamin D, calcium, zinc and fat-soluble vitamins, which in turn produce iron deficiency anemia, reduced bone mineral density and osteoporosis (also via secondary hyperparathyroidism), growth failure and short stature in children, weight loss, and fatigue. Detail which nutrient deficit drives which phenotype and where deficiency-independent (inflammatory, e.g. RANKL/OPG or cytokine-mediated) contributions are documented, especially for bone disease. (b) Extraintestinal autoimmunity by epitope spreading: anti-transglutaminase-3 (TG3) IgA and dermal IgA-TG3 deposits leading to dermatitis herpetiformis; anti-transglutaminase-6 (TG6) antibodies and cerebellar Purkinje cell injury leading to gluten ataxia; the disputed role of humoral versus T-cell mechanisms in gluten neuropathy. (c) Lymphomagenesis: chronic IL-15-driven activation and clonal expansion of intraepithelial lymphocytes leading to refractory celiac disease type II (aberrant clonal IELs, often with JAK1/STAT3 mutations) progressing to enteropathy-associated T-cell lymphoma, and the epidemiological protection conferred by gluten-free diet adherence.

## Output Format

- One subsection per phenotype, headed by the phenotype name exactly as listed
  above, containing: the numbered causal chain, the evidence grade, PMIDs with
  exact abstract quotes per step, and suggested ontology terms (GO for
  biological processes, CL for cell types, HP for the phenotype itself).
- A final section titled **Proposed New Mechanism Nodes** listing every
  intermediate process flagged in item 2, each with: a suggested node name, its
  upstream node (from the existing list or another proposed node), its
  downstream phenotypes, and the strongest single citation for its causal
  placement.
- A final section titled **Unwired Phenotypes** listing every phenotype graded
  NOT_ESTABLISHED, with one sentence each on what evidence would settle it.

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Include direct quotes from abstracts to support key statements
- Never cite a paper for a claim its abstract does not make


# Mechanism-to-Phenotype Wiring Report: Celiac Disease

**Disease:** Celiac disease; **MONDO:** MONDO:0005130.  
**Scope:** This report starts from the six already-curated mechanism nodes and does not re-derive the core gluten–HLA–TG2–T-cell pathway. “Proposed new node” means an intermediate process absent from the supplied node list. Evidence grades describe the **entire chain**, not merely the disease–phenotype association.

A compact overview precedes the phenotype-level wiring.

| Phenotype | Proximal existing mechanism node | Key proposed intermediate node(s) | Evidence grade | Main caveat/alternative |
|---|---|---|---|---|
| Chronic Diarrhea | Intestinal Epithelial Damage | **New:** generalized malabsorption; osmotic load; fat/bile-acid spillover; electrolyte secretion | **SUPPORTED** | Multiple mechanisms coexist; phenotype-specific human causal partitioning is limited. (montorohuguet2021smallandlarge pages 10-13, montorohuguet2021smallandlarge pages 22-24) |
| Abdominal Pain | Intestinal Epithelial Damage | **New:** mucosal nociception; luminal distension; dysmotility | **PROPOSED** | IBS, lactose/FODMAP intolerance, and other disorders may independently cause pain. (montorohuguet2021smallandlarge pages 10-13) |
| Bloating | Intestinal Epithelial Damage | **New:** brush-border enzyme loss; carbohydrate malabsorption; microbial fermentation and gas | **PROPOSED** | Direct celiac-specific human evidence for this complete chain is sparse. (montorohuguet2021smallandlarge pages 10-13, montorohuguet2021smallandlarge pages 22-24) |
| Constipation | Microbiome Dysbiosis / Intestinal Epithelial Damage | **New:** altered intestinal transit or defecatory function | **NOT_ESTABLISHED** | Mechanism is unknown; functional constipation, diet, thyroid disease, and medication effects are alternatives. (montorohuguet2021smallandlarge pages 10-13) |
| Villous Atrophy | Intestinal Epithelial Damage | None; this is the histologic expression of the curated epithelial-damage node | **ESTABLISHED** | Patchiness and sampling orientation can affect histologic ascertainment. (montorohuguet2021smallandlarge pages 10-13) |
| Weight Loss | Intestinal Epithelial Damage | **New:** macronutrient malabsorption; steatorrhea; negative energy balance | **SUPPORTED** | Reduced intake, inflammation, and fluid shifts may contribute; obesity does not exclude celiac disease. (merlotti2022bonefragilityin pages 5-7, montorohuguet2021smallandlarge pages 10-13, montorohuguet2021smallandlarge pages 22-24) |
| Iron Deficiency Anemia | Intestinal Epithelial Damage | **New:** proximal-duodenal iron malabsorption; depleted iron stores; impaired erythropoiesis; sometimes inflammation/hepcidin | **ESTABLISHED** | Menstrual or occult blood loss and persistent enterocyte defects can coexist. (montorohuguet2021smallandlarge pages 24-25) |
| Fatigue | Intestinal Epithelial Damage / Mixed Th1/Th17/IL-21 Mucosal Cytokine Response | **New:** anemia, micronutrient deficits, pain/depression, or inflammatory sickness signaling | **NOT_ESTABLISHED** | Fatigue improves on a gluten-free diet but may persist and was not associated with nutritional deficiency or disease activity in a 2023 cohort. (montorohuguet2021smallandlarge pages 24-25) |
| Growth Failure in Children | Intestinal Epithelial Damage | **New:** energy/protein and micronutrient malabsorption; reduced weight gain; disrupted GH–IGF-1 axis | **SUPPORTED** | Endocrine disease, genetics, delayed diagnosis, and socioeconomic nutrition remain alternatives. (montorohuguet2021smallandlarge pages 24-25, merlotti2022bonefragilityin pages 5-7) |
| Dermatitis Herpetiformis | Autoantibody Production | **New:** TG2→TG3 epitope spreading; anti-TG3 IgA; dermal IgA–TG3 deposition; complement/neutrophil injury | **ESTABLISHED** | TG3 deposits are highly characteristic, but their precise lesion-initiating role remains incompletely resolved. (patt2023unravelingtheimmunopathological pages 7-8, kaunisto2022antibodyresponsesto pages 1-3) |
| Reduced Bone Mineral Density | Intestinal Epithelial Damage | **New:** calcium/vitamin-D malabsorption; secondary hyperparathyroidism; increased resorption; inflammatory RANKL/OPG imbalance | **ESTABLISHED** | Hypogonadism, low weight, immobility, menopause, and persistent inflammation also contribute. (krupakozak2014pathologicbonealterations pages 4-5, altoma2022thedietaryand pages 2-4, lungaro2023osteoporosisandceliac pages 2-4) |
| Dental Enamel Defects | Intestinal Epithelial Damage / Autoantibody Production | **New:** calcium/vitamin-D deficiency during amelogenesis; possible anti-gliadin/ameloblast cross-reactivity | **PROPOSED** | Established enamel damage is irreversible; nutritional and immune branches have not been causally separated. (montorohuguet2021smallandlarge pages 24-25) |
| Recurrent Aphthous Stomatitis | Intestinal Epithelial Damage / Mixed Th1/Th17/IL-21 Mucosal Cytokine Response | **New:** oral mucosal immune dysregulation or iron/folate/B12 deficiency | **NOT_ESTABLISHED** | Association is reproducible, but trauma, infection, hematinic deficiency, and other immune diseases remain competing causes. (montorohuguet2021smallandlarge pages 24-25) |
| Peripheral Neuropathy | Autoantibody Production / Mixed Th1/Th17/IL-21 Mucosal Cytokine Response | **New:** peripheral axonopathy; anti-neural/TG6 antibodies and/or perivascular T-cell injury | **NOT_ESTABLISHED** | Humoral versus T-cell causation is unresolved; B12 deficiency, diabetes, and coincident autoimmunity must be excluded. (lauret2013celiacdiseaseand pages 6-7, rouvroye2020theneuropathologyof pages 13-15) |
| Cerebellar Ataxia | Autoantibody Production | **New:** anti-TG6/anti-Purkinje reactivity; cerebellar immune deposition; Purkinje-cell loss and gliosis | **PROPOSED** | TG6 is a biomarker/candidate antigen, not a conclusively proven human effector; non-celiac gluten sensitivity and other ataxias complicate attribution. (lauret2013celiacdiseaseand pages 6-7, rouvroye2020theneuropathologyof pages 13-15) |
| Elevated Hepatic Transaminases | Barrier Dysfunction | **New:** portal delivery of microbial products/antigens; hepatic innate immune injury (“celiac hepatitis”) | **SUPPORTED** | Autoimmune hepatitis, MASLD, drugs, and viral liver disease are alternatives; mechanism is inferred chiefly from permeability and dietary reversal. (barton2008celiacdiseaseand pages 14-16) |
| Vitamin D Deficiency | Intestinal Epithelial Damage | **New:** fat-soluble-vitamin malabsorption; steatorrhea; reduced vitamin-D uptake | **SUPPORTED** | Low intake and sunlight exposure can contribute, and deficiency may persist on a gluten-free diet. (montorohuguet2021smallandlarge pages 24-25, lungaro2023osteoporosisandceliac pages 2-4) |
| Small intestinal lymphoma | Intestinal Epithelial Damage | **New:** persistent IL-15/JAK-STAT selection; aberrant clonal IEL expansion (RCDII); JAK1/STAT3 and NF-κB lesions; EATL transformation | **ESTABLISHED** | EATL can arise without recognized RCDII; gluten-free-diet protection is observational and not absolute. (cording2022oncogeneticlandscapeof pages 1-1, chander2018pathogenesisofenteropathyassociated pages 1-2, botosso2023theroleof pages 6-8, hue2022cellularoriginsand pages 14-16) |
| Osteoporosis | Intestinal Epithelial Damage | **New:** calcium/vitamin-D malabsorption; secondary hyperparathyroidism; osteoclastogenesis; chronic cytokine/RANKL–OPG imbalance | **ESTABLISHED** | Bone density may not fully normalize; age, sex hormones, low BMI, and primary osteoporosis modify risk. (krupakozak2014pathologicbonealterations pages 4-5, altoma2022thedietaryand pages 2-4, lungaro2023osteoporosisandceliac pages 2-4, gracefarfaglia2015bonesofcontention pages 13-15) |
| Arthritis | Mixed Th1/Th17/IL-21 Mucosal Cytokine Response / Microbiome Dysbiosis | **New:** systemic immune activation or gut–joint trafficking causing synovitis | **NOT_ESTABLISHED** | Shared genetics, rheumatoid/JIA comorbidity, and ascertainment may explain association; diet alone often does not control arthritis. (barton2008celiacdiseaseand pages 14-16) |
| Short stature | Intestinal Epithelial Damage | **New:** chronic nutrient/energy deficit; impaired GH–IGF-1 signaling; reduced linear growth | **SUPPORTED** | Genetic short stature, endocrine deficiency, and failure of catch-up growth despite mucosal treatment require separate evaluation. (montorohuguet2021smallandlarge pages 24-25, merlotti2022bonefragilityin pages 5-7) |
| Female infertility | Intestinal Epithelial Damage / Autoantibody Production | **New:** zinc/folate/iron deficiency and hypothalamic–gonadal disruption; proposed anti-TG2 effects on endometrium/trophoblast/angiogenesis | **NOT_ESTABLISHED** | Human causal evidence is inadequate; shared autoimmunity, thyroid disease, HLA background, and referral bias are major alternatives. (patt2023unravelingtheimmunopathological pages 14-15) |


*Table: Compact mapping of all curated phenotypes to proximal mechanisms, proposed intermediate nodes, conservative evidence grades, and major causal alternatives. Citations identify the gathered evidence supporting each assessment.*

## Evidence interpretation and limitations

The strongest wiring is found for proximal-duodenal iron malabsorption, calcium/vitamin-D-related bone disease, TG3-associated dermatitis herpetiformis, and RCDII–EATL evolution. By contrast, constipation, fatigue, aphthous ulcers, peripheral neuropathy, arthritis, and infertility have documented associations but no uniquely demonstrated downstream mechanism.

The retrieval system exposed DOI and publication metadata more consistently than PMID fields. Accordingly, a PMID is given only when it was verifiable from the retrieved record; **“PMID not exposed” is used instead of manufacturing an identifier**. Quoted wording below is taken from retrieved abstracts unless explicitly labeled “full-text synthesis.”

# Phenotype-level wiring

## Chronic Diarrhea

1. **Intestinal Epithelial Damage** leads to villous surface loss and impaired mucosal absorption.  
2. Impaired absorption leads to **generalized nutrient and fluid malabsorption** (**proposed new node**).  
3. Malabsorption results in luminal osmotic load, fat delivery to the colon, bacterial production of cathartic hydroxy-fatty acids, and—when ileal function is involved—bile-salt spillover (**proposed nodes**).  
4. These processes result in increased stool water and chronic diarrhea.

**Grade: SUPPORTED.** Human clinicopathologic association and dietary reversal are strong, but individual contributions of osmotic, fatty-acid, bile-acid, and secretory pathways have not been partitioned experimentally in celiac cohorts. A review reports that persistent villous atrophy is associated with “chronic diarrhea, steatorrhea, abdominal pain, weight loss, and nutritional deficiencies”; it also describes increased osmotic load, electrolyte secretion, and cathartic effects of malabsorbed fat and bile salts. [Human clinical synthesis; DOI 10.3390/nu13041254; April 2021; PMID not exposed](https://doi.org/10.3390/nu13041254). (montorohuguet2021smallandlarge pages 10-13, montorohuguet2021smallandlarge pages 22-24)

**Alternatives:** pancreatic insufficiency, microscopic colitis, bile-acid diarrhea, lactose intolerance, infection, IBS, and inadvertent gluten exposure can independently produce diarrhea.

**Ontology:** HP:0002014 Diarrhea; GO:0050892 intestinal absorption; CL:0000584 enterocyte.

## Abdominal Pain

1. **Intestinal Epithelial Damage** leads to mucosal inflammation and malabsorption.  
2. Inflammation and malabsorption may lead to **visceral nociceptor activation, luminal distension, and altered motility** (**proposed new nodes**).  
3. These processes may result in abdominal pain.

**Grade: PROPOSED.** Abdominal pain accompanies active and refractory enteropathy, but a celiac-specific human experiment demonstrating which intermediate causes pain is lacking. The malabsorption review documents abdominal pain with persistent villous atrophy but does not establish a unique pain pathway. [Human clinical synthesis; DOI 10.3390/nu13041254](https://doi.org/10.3390/nu13041254). (montorohuguet2021smallandlarge pages 10-13)

**Alternatives:** IBS, lactose/FODMAP intolerance, constipation, dyspepsia, endometriosis, and other gastrointestinal disease.

**Ontology:** HP:0002027 Abdominal pain; GO:0007600 sensory perception; CL:0000198 pain receptor cell/nociceptor.

## Bloating

1. **Intestinal Epithelial Damage** leads to loss or dysfunction of brush-border digestive capacity.  
2. Brush-border dysfunction may lead to **carbohydrate maldigestion and malabsorption** (**proposed new node**).  
3. Unabsorbed substrate leads to **microbial fermentation, gas production, and luminal distension** (**proposed new node**).  
4. Distension results in bloating.

**Grade: PROPOSED.** This is physiologically coherent, but retrieved celiac literature did not demonstrate the complete chain in humans. The broader malabsorption literature supports impaired assimilation, whereas phenotype-specific evidence for fermentation-driven bloating is limited. (montorohuguet2021smallandlarge pages 10-13, montorohuguet2021smallandlarge pages 22-24)

**Alternatives:** IBS, small-intestinal bacterial overgrowth, dietary FODMAPs, aerophagia, and constipation.

**Ontology:** HP:0003270 Abdominal distention; GO:0019646 aerobic/anaerobic carbohydrate metabolism; CL:0000584 enterocyte.

## Constipation

1. **NOT_ESTABLISHED, mechanism unknown.**  
2. Candidate routes—**altered transit, pelvic-floor dysfunction, dietary fiber change, or dysbiosis**—remain proposed and have not been causally placed downstream of celiac enteropathy.

**Grade: NOT_ESTABLISHED.** The available malabsorption evidence explains diarrheal phenotypes much better than constipation and provides no celiac-specific causal chain. (montorohuguet2021smallandlarge pages 10-13)

**Alternatives:** functional constipation, hypothyroidism or other coincident autoimmunity, medication effects, low-fiber gluten-free diet, and ascertainment.

**Ontology:** HP:0002019 Constipation; GO:0019229 regulation of vasoconstriction is not suitable—use the broader process label “gastrointestinal motility” pending ontology curation; CL:0000210 enteric neuron.

## Villous Atrophy

1. **Intestinal Epithelial Damage** leads directly to enterocyte loss and villous architectural shortening.  
2. Enterocyte loss results in villous atrophy.

**Grade: ESTABLISHED.** This phenotype is effectively the histologic expression of an already-curated mechanism node. Human biopsy evidence establishes reduced villus-to-crypt ratio and duodenal lymphocytosis. (montorohuguet2021smallandlarge pages 10-13)

**Alternatives:** medication-induced enteropathy, infection, immune deficiency, Crohn disease, autoimmune enteropathy, and tropical sprue can produce non-celiac villous atrophy.

**Ontology:** HP:0011473 Villous atrophy; GO:0048870 cell motility is not specific—prefer “intestinal epithelial tissue morphogenesis” as a local ontology label; CL:0000584 enterocyte.

## Weight Loss

1. **Intestinal Epithelial Damage** leads to reduced absorptive area.  
2. Reduced absorption leads to **macronutrient malabsorption and steatorrhea** (**proposed new node**).  
3. Energy loss, sometimes combined with reduced intake and inflammation, leads to **negative energy balance** (**proposed new node**).  
4. Negative energy balance results in weight loss.

**Grade: SUPPORTED.** Human studies consistently associate active enteropathy with malabsorption and weight loss. In an untreated adult cohort, the abstract states: “Malabsorption, weight loss and vitamin/mineral-deficiencies characterize classical celiac disease”; 17% were malnourished with greater than 10% undesired weight loss. [Primary human cross-sectional study; DOI 10.3390/nu5103975; September 2013; PMID not exposed](https://doi.org/10.3390/nu5103975). Reviews also connect persistent atrophy with weight loss. (merlotti2022bonefragilityin pages 5-7, montorohuguet2021smallandlarge pages 10-13, montorohuguet2021smallandlarge pages 22-24)

**Alternatives:** reduced intake, malignancy, endocrine disease, depression, and fluid shifts; obesity does not exclude active celiac disease.

**Ontology:** HP:0001824 Weight loss; GO:0006091 generation of precursor metabolites and energy; CL:0000584 enterocyte.

## Iron Deficiency Anemia

1. **Intestinal Epithelial Damage** leads to proximal-duodenal villous loss at the principal site of iron absorption.  
2. Villous loss leads to **impaired iron absorption and depleted iron stores** (**proposed new node**).  
3. Iron depletion leads to impaired hemoglobin synthesis and iron-deficiency anemia.

**Grade: ESTABLISHED.** An abstract states: “The iron absorption process develops mainly in the proximal duodenum. This portion of the intestine is typically destroyed in celiac disease… resulting in a reduction in absorption of iron and subsequent iron deficiency anemia.” It reports prevalence of 12–82% at diagnosis and notes that anemia commonly normalizes after at least six months of gluten-free diet, although iron-store recovery can take two years. [Human clinical review integrating intervention cohorts; DOI 10.3390/nu13051695; May 2021; PMID not exposed](https://doi.org/10.3390/nu13051695). Another abstract identifies villous atrophy and inflammation/anemia of chronic disease as the two main causes. (montorohuguet2021smallandlarge pages 24-25)

**Alternatives:** menstrual loss, gastrointestinal bleeding, low dietary iron, inflammation/hepcidin, H. pylori, or genetic iron-regulatory variants. Persistent anemia despite healed villi requires investigation.

**Ontology:** HP:0001891 Iron deficiency anemia; GO:0030218 erythrocyte differentiation; CL:0000232 erythrocyte; CL:0000584 enterocyte.

## Fatigue

1. **Intestinal Epithelial Damage** may lead to iron, folate, B12, or other nutrient deficits.  
2. Deficiency may lead to anemia and reduced oxygen delivery, which may contribute to fatigue.  
3. Independently, **Mixed Th1/Th17/IL-21 Mucosal Cytokine Response** may produce inflammatory sickness signaling; pain, sleep disturbance, and depression may also contribute.  
4. No single route has been demonstrated as the celiac-specific cause of fatigue.

**Grade: NOT_ESTABLISHED.** A 2023 prospective controlled study found substantial improvement after a gluten-free diet—median Fatigue Severity Scale 3.8 to 1.9 and fatigue VAS 44.5 to 15.5, all *p*<0.001—but fatigue remained above controls and was associated with depression and pain, “but not with signs of disease activity or nutritional deficiency.” [Primary human prospective intervention-follow-up; DOI 10.3389/fmed.2023.1242512; September 2023; trial NCT01551563](https://doi.org/10.3389/fmed.2023.1242512). Systematic reviewers conclude that mechanisms are poorly understood. (montorohuguet2021smallandlarge pages 24-25)

**Alternatives:** anemia, depression, sleep disorder, chronic pain, hypothyroidism, medication, and deconditioning.

**Ontology:** HP:0012378 Fatigue; GO:0006954 inflammatory response; CL:0000232 erythrocyte.

## Growth Failure in Children

1. **Intestinal Epithelial Damage** leads to energy, protein, iron, zinc, folate, vitamin-D, and calcium malabsorption.  
2. Malabsorption leads to **malnutrition and impaired weight gain** (**proposed new node**).  
3. Malnutrition and chronic inflammation may suppress the **growth-hormone–IGF-1 axis** (**proposed new node**).  
4. Reduced substrate availability and growth signaling lead to growth failure.

**Grade: SUPPORTED.** A 2024 human case-control study found stunting in 31%, low age-adjusted BMI in 20.8%, and both stunting and wasting in 5.2% of affected children; low ferritin and socioeconomic factors predicted stunting. The persistence of abnormalities despite diet shows that nutrition, adherence, and social determinants modify the chain. [Primary human case-control study; DOI 10.3390/children11091042; August 2024](https://doi.org/10.3390/children11091042). (montorohuguet2021smallandlarge pages 24-25, merlotti2022bonefragilityin pages 5-7)

**Alternatives:** constitutional or genetic short stature, growth-hormone deficiency, thyroid disease, delayed puberty, and food insecurity.

**Ontology:** HP:0001508 Failure to thrive; GO:0040007 growth; CL:0000584 enterocyte; CL:0000138 chondrocyte.

## Dermatitis Herpetiformis

1. **Autoantibody Production** leads to expansion of TG3-reactive IgA responses, plausibly through TG2/TG3 epitope spreading (**proposed new node**).  
2. Anti-TG3 IgA leads to circulating or locally formed **IgA–TG3 immune complexes** (**proposed new node**).  
3. Complexes deposit in dermal papillae and lead to complement/endothelial activation and neutrophil recruitment (**proposed new node**).  
4. Neutrophil proteases damage the dermal–epidermal junction, resulting in pruritic vesicles and dermatitis herpetiformis.

**Grade: ESTABLISHED for TG3 autoimmunity and dermal deposition; SUPPORTED—not fully established—for the terminal lesion-producing sequence.** The foundational human study states: “the IgA precipitates in the papillary dermis… contain epidermal transglutaminase” and concludes that TG3 “is the dominant autoantigen.” [Primary human serologic/tissue study; Sárdy et al.; DOI 10.1084/jem.20011299; March 2002](https://doi.org/10.1084/jem.20011299). A 2022 review’s abstract cautions that although granular IgA/TG3 deposits are the diagnostic finding, “the role of these immunocomplexes in the pathogenesis is unknown.” (patt2023unravelingtheimmunopathological pages 7-8, kaunisto2022antibodyresponsesto pages 1-3)

**Alternatives:** Shared HLA-DQ2/DQ8 explains susceptibility but not the TG3-specific phenotype. Dermal IgA deposits may occur without clinical DH, so deposition alone is insufficient.

**Ontology:** HP:0012496 Dermatitis herpetiformis; GO:0038096 Fc-gamma receptor signaling is not IgA-specific—prefer immune-complex deposition and neutrophil degranulation (GO:0043312); CL:0000775 neutrophil; CL:0000787 plasma cell.

## Reduced Bone Mineral Density

1. **Intestinal Epithelial Damage** leads to calcium and vitamin-D malabsorption.  
2. Calcium/vitamin-D deficiency leads to **secondary hyperparathyroidism** (**proposed new node**).  
3. Secondary hyperparathyroidism increases osteoclast-mediated skeletal resorption.  
4. In parallel, **Mixed Th1/Th17/IL-21 Mucosal Cytokine Response** may alter the RANKL/OPG balance and favor osteoclastogenesis (**proposed new node**).  
5. Increased resorption and impaired mineralization result in reduced BMD.

**Grade: ESTABLISHED.** The literature identifies both nutrient and inflammation branches. A review abstract says bone disease mechanisms include “malabsorption of calcium and vitamin D leading to secondary hyperparathyroidism and increased skeletal resorption” and “pro-inflammatory cytokines altering the osteoprotegerin and receptor activator of nuclear kappa-B ligand ratio favoring osteoclastogenesis.” Another 2023 synthesis reports low BMD in 30–60% of newly diagnosed patients. (krupakozak2014pathologicbonealterations pages 4-5, altoma2022thedietaryand pages 2-4, lungaro2023osteoporosisandceliac pages 2-4)

**Alternatives:** menopause, hypogonadism, low BMI, inactivity, glucocorticoids, smoking, and primary osteoporosis.

**Ontology:** HP:0004349 Reduced bone mineral density; GO:0045453 bone resorption; CL:0000092 osteoclast; CL:0000062 osteoblast.

## Dental Enamel Defects

1. **Intestinal Epithelial Damage** during amelogenesis may lead to calcium/vitamin-D and other micronutrient deficiencies.  
2. Deficiency may impair ameloblast mineralization (**proposed new node**).  
3. A parallel candidate route is **anti-gliadin or transglutaminase-associated cross-reactivity with enamel/ameloblast structures** (**proposed new node**).  
4. Disrupted amelogenesis results in symmetric chronological enamel defects.

**Grade: PROPOSED.** A 2024 systematic review found enamel-defect prevalence of 50–94.1%, but did not establish one mechanism. A 2023 review states that micronutrient malabsorption—especially calcium/vitamin D—and immunity are “considered the main cause”; established damage is irreversible. [Human systematic review; DOI 10.3390/jcm13051382; February 2024](https://doi.org/10.3390/jcm13051382).

**Alternatives:** fever or malnutrition during tooth development, fluorosis, prematurity, infection, medications, and genetic enamel disorders.

**Ontology:** HP:0006297 Enamel hypoplasia; GO:0031214 biomineral tissue development; CL:0000729 ameloblast.

## Recurrent Aphthous Stomatitis

1. **NOT_ESTABLISHED, mechanism unknown.**  
2. Proposed routes include hematinic deficiency from intestinal damage and systemic/oral immune dysregulation, but neither has been shown to be necessary or sufficient.

**Grade: NOT_ESTABLISHED.** A pediatric comparative study found aphthous-like ulcers in 40% of celiac patients versus 4.44% of controls (*p*=0.001), establishing association, not mechanism. [Primary human comparative study; DOI 10.17796/1053-4625-43.4.9; 2019](https://doi.org/10.17796/1053-4625-43.4.9).

**Alternatives:** trauma, viral disease, Behçet disease, inflammatory bowel disease, iron/folate/B12 deficiency from other causes, and idiopathic recurrent aphthosis.

**Ontology:** HP:0011107 Recurrent aphthous stomatitis; GO:0006954 inflammatory response; CL:0000066 epithelial cell.

## Peripheral Neuropathy

1. **Autoantibody Production** may lead to anti-neural, antiganglioside, or TG6 antibodies.  
2. In parallel, systemic immune activation may lead to **perivascular T-cell infiltration and peripheral axonopathy** (**proposed new node**).  
3. Axonal loss or small-fiber injury results in peripheral neuropathy.

**Grade: NOT_ESTABLISHED.** Neuropathology shows axonopathy, loss of myelinated fibers, and focal/perivascular inflammatory cells, supporting immune injury, but the review concludes that the underlying mechanism “is not yet clear” and calls for characterization of infiltrates and target epitopes. Both humoral and cell-mediated routes remain live. [Systematic neuropathology review; DOI 10.3390/nu12030822; March 2020](https://doi.org/10.3390/nu12030822). (lauret2013celiacdiseaseand pages 6-7, rouvroye2020theneuropathologyof pages 13-15)

**Alternatives:** B12, copper, or vitamin-E deficiency; diabetes; thyroid disease; paraproteinemia; and coincident autoimmune neuropathy.

**Ontology:** HP:0009830 Peripheral neuropathy; GO:0006955 immune response; CL:0000101 sensory neuron; CL:0000909 CD8-positive T cell.

## Cerebellar Ataxia

1. **Autoantibody Production** leads in a subset to anti-TG6 and anti-Purkinje-cell reactivity (**proposed new node**).  
2. Antibodies and/or lymphocytes may enter cerebellar tissue and lead to immune deposition, microglial activation, and Purkinje-cell injury (**proposed new node**).  
3. Purkinje-cell loss, gliosis, and cerebellar atrophy result in ataxia.

**Grade: PROPOSED.** Human tissue and serology strongly support association, but not antibody sufficiency. Neuropathology documents Purkinje-cell loss, gliosis, lymphocytic infiltration, and perivascular cuffing; TG6 is described as a “possible target autoantigen” requiring further investigation. Antibody titers can decline on gluten withdrawal, but irreversible neuronal loss limits clinical recovery. (lauret2013celiacdiseaseand pages 6-7, rouvroye2020theneuropathologyof pages 13-15)

**Alternatives:** genetic, degenerative, paraneoplastic, nutritional, alcohol-related, and other autoimmune ataxias; neurologic gluten sensitivity can occur without celiac enteropathy.

**Ontology:** HP:0001251 Ataxia; HP:0002072 Cerebellar atrophy; GO:0098742 cell-cell adhesion via plasma membrane; preferably use “Purkinje cell degeneration” as a local process label; CL:0000121 Purkinje cell; CL:0000129 microglial cell.

## Elevated Hepatic Transaminases

1. **Barrier Dysfunction** leads to increased portal delivery of microbial products, food antigens, and inflammatory mediators.  
2. Portal exposure may lead to **hepatic innate immune activation and nonspecific hepatocellular injury (“celiac hepatitis”)** (**proposed new node**).  
3. Hepatocyte injury releases ALT and AST, resulting in elevated transaminases.

**Grade: SUPPORTED.** Dietary withdrawal supplies human intervention evidence, but the molecular intermediary remains incompletely demonstrated. A review abstract states that “intestinal permeability may be at least one of the mechanisms” and that cryptogenic abnormalities commonly normalize after 6–12 months of strict diet. A pediatric cohort found AST elevation in 28.8%, ALT in 7.6%, and improvement in ALT after six months. [Primary human retrospective intervention-follow-up; DOI 10.5114/ceh.2021.111003; December 2021](https://doi.org/10.5114/ceh.2021.111003). (barton2008celiacdiseaseand pages 14-16)

**Alternatives:** autoimmune hepatitis, MASLD, viral hepatitis, medication, muscle disease, and shared autoimmunity. Persistent abnormalities after dietary treatment require separate evaluation.

**Ontology:** HP:0002910 Elevated hepatic transaminase; GO:0006954 inflammatory response; CL:0000182 hepatocyte; CL:0000235 macrophage/Kupffer cell.

## Vitamin D Deficiency

1. **Intestinal Epithelial Damage** leads to reduced absorptive area and, in severe disease, fat malabsorption/steatorrhea.  
2. Fat malabsorption leads to impaired uptake and enterohepatic recovery of fat-soluble vitamin D (**proposed new node**).  
3. Reduced uptake results in vitamin-D deficiency.

**Grade: SUPPORTED.** Vitamins A, D, E, and K deficiencies are reported in classical malabsorptive celiac disease. In a prospective older-adult cohort, vitamin D, B12, folate, and ferritin improved after gluten-free treatment, supporting reversibility. The 2023 bone review notes that low intake, dysbiosis, and endocrine factors can contribute even without severe atrophy. (montorohuguet2021smallandlarge pages 24-25, lungaro2023osteoporosisandceliac pages 2-4)

**Alternatives:** low sunlight exposure, low intake, obesity, liver/kidney disease, and medication.

**Ontology:** HP:0100512 Vitamin D deficiency; GO:0033280 response to vitamin D; CL:0000584 enterocyte.

## Small intestinal lymphoma

Here the phenotype is interpreted primarily as **enteropathy-associated T-cell lymphoma (EATL)**.

1. **Intestinal Epithelial Damage**, together with persistent IL-15-rich mucosal signaling, leads to prolonged activation and survival of cytotoxic/innate-like IELs.  
2. Chronic selection leads to **aberrant clonal IEL expansion—refractory celiac disease type II** (**proposed new node**).  
3. Clones acquire **JAK1/STAT3 gain-of-function and cooperating NF-κB/epigenetic lesions** (**proposed new node**).  
4. Mutated clones gain cytokine-independent survival and proliferative fitness.  
5. Expansion and additional evolution lead to overt EATL.

**Grade: ESTABLISHED for the RCDII–JAK/STAT–EATL route.** The pivotal primary human genomic study abstract states that EATL is “often preceded by low-grade clonal intraepithelial lymphoproliferation” and reports JAK1–STAT3 gain-of-function mutations in **80% of RCDII** and **90% of EATL**, with JAK1 p.G1097 in approximately 50%. JAK1 inhibition blocked malignant RCDII-cell survival/proliferation in vitro. [Primary human genomic study plus functional validation; DOI 10.1136/gutjnl-2020-322935; online 2021/issue 2022](https://doi.org/10.1136/gutjnl-2020-322935). (cording2022oncogeneticlandscapeof pages 1-1)

Recent synthesis reports median EATL survival below ten months and dissemination in 10–20%. Population studies estimate markedly elevated gut-lymphoma risk; one synthesis reports SIRs of 16–40 for gut lymphoma. (hue2022cellularoriginsand pages 14-16, pelizzaro2021theriskof pages 2-4)

**Dietary protection:** Observational cohorts suggest lower lymphoma risk with strict diet or mucosal healing, but protection is not absolute and evidence is susceptible to adherence measurement, reverse causation, and lead-time bias. In one 1,757-person cohort, nine intestinal lymphomas occurred versus 1.4 expected; only four affected patients had strictly followed a GFD. This supports—not proves—protection from reduced gluten-driven inflammation. (chander2018pathogenesisofenteropathyassociated pages 1-2, botosso2023theroleof pages 6-8)

**Alternatives:** Some EATL arises without recognized RCDII. Other small-intestinal lymphomas, particularly B-cell lymphoma and MEITL, have different causal wiring.

**Ontology:** HP:0030445 Intestinal lymphoma (confirm local release); GO:0008283 cell population proliferation; GO:0007259 JAK-STAT cascade; CL:0002496 intraepithelial lymphocyte; CL:0000910 cytotoxic T cell.

## Osteoporosis

1. **Intestinal Epithelial Damage** leads to calcium/vitamin-D malabsorption.  
2. Mineral deficiency leads to secondary hyperparathyroidism.  
3. Secondary hyperparathyroidism leads to increased bone resorption and impaired mineralization.  
4. In parallel, inflammatory cytokines alter RANKL/OPG and favor osteoclastogenesis.  
5. Sustained remodeling imbalance leads from low BMD to osteoporosis and fragility.

**Grade: ESTABLISHED.** The evidence supports a multifactorial pathway rather than vitamin deficiency alone. A systematic review found partial BMD recovery by one year and full recovery by five years in included studies, although later reviews emphasize that normalization is not universal. Calcium/vitamin-D supplementation particularly benefited malnourished patients. (krupakozak2014pathologicbonealterations pages 4-5, altoma2022thedietaryand pages 2-4, lungaro2023osteoporosisandceliac pages 2-4, gracefarfaglia2015bonesofcontention pages 13-15)

**Alternatives:** primary age-related or postmenopausal osteoporosis, hypogonadism, low body weight, inactivity, glucocorticoids, and smoking.

**Ontology:** HP:0000939 Osteoporosis; GO:0045453 bone resorption; CL:0000092 osteoclast; CL:0000062 osteoblast.

## Arthritis

1. **NOT_ESTABLISHED, mechanism unknown.**  
2. Proposed routes include systemic cytokine spillover, gut–joint lymphocyte trafficking, and dysbiosis-driven immune activation, but none is demonstrated as the causal route from celiac enteropathy to arthritis.

**Grade: NOT_ESTABLISHED.** A 2023 pediatric cohort found predominantly oligoarticular (76.9%) and asymmetric (84.6%) arthritis; 84.6% required systemic therapy, and diet alone was frequently insufficient. This argues against a simple enteropathy→arthritis chain. [Primary human retrospective cohort; DOI 10.1186/s12969-023-00822-x; May 2023](https://doi.org/10.1186/s12969-023-00822-x).

**Alternatives:** shared autoimmune genetics, juvenile idiopathic arthritis or rheumatoid arthritis as coincident disease, shared environmental triggers, and referral bias. Mendelian-randomization evidence reported no causal effect of celiac liability on RA, further supporting caution.

**Ontology:** HP:0001369 Arthritis; GO:0006954 inflammatory response; CL:0000904 CD4-positive T cell; CL:0000214 synovial cell.

## Short stature

1. **Intestinal Epithelial Damage** leads to chronic energy, protein, mineral, and micronutrient malabsorption.  
2. Malnutrition and inflammation lead to impaired GH–IGF-1 signaling and reduced growth-plate substrate availability (**proposed new node**).  
3. Reduced linear growth velocity results in short stature.

**Grade: SUPPORTED.** This is the accumulated outcome of the growth-failure branch. Recent human data show stunting in 31% of one pediatric celiac cohort and identify low ferritin and socioeconomic factors as predictors, showing that the disease pathway is neither exclusive nor deterministic. (montorohuguet2021smallandlarge pages 24-25, merlotti2022bonefragilityin pages 5-7)

**Alternatives:** familial short stature, constitutional delay, endocrine disease, Turner syndrome, chronic systemic disease, and inadequate diet after diagnosis.

**Ontology:** HP:0004322 Short stature; GO:0040007 growth; CL:0000138 chondrocyte.

## Female infertility

1. **Intestinal Epithelial Damage** may lead to iron, folate, zinc, and energy deficiency.  
2. Nutritional deficiency may disturb hypothalamic–pituitary–gonadal function, ovulation, or endometrial competence (**proposed new node**).  
3. A parallel proposed route is **anti-TG2 binding to endometrial/trophoblast structures with impaired angiogenesis or invasion** (**proposed new node**).  
4. These candidate processes may reduce conception or implantation success.

**Grade: NOT_ESTABLISHED.** Human association is inconsistent and the principal antibody mechanism is derived largely from human-cell in-vitro work and animal models, not direct causal intervention in women. A 2023 review states that anti-TG2 could hinder trophoblast invasiveness and endometrial angiogenesis, while also identifying zinc/folate deficiency; it does not prove either route in vivo. [Mechanistic review incorporating in-vitro human cells and murine evidence; DOI 10.3390/antib12040079; December 2023](https://doi.org/10.3390/antib12040079). (patt2023unravelingtheimmunopathological pages 14-15)

A 2024 recurrent-reproductive-failure study found HLA risk alleles in 69% versus 35–40% in the general population, but only 2.3% met celiac diagnostic criteria; thyroid disease and levothyroxine were also influential. This illustrates genetic confounding and coincident autoimmunity rather than a clean celiac-to-infertility pathway.

**Alternatives:** shared HLA background, autoimmune thyroid disease, endometriosis, age, male-factor infertility, referral bias, and nutritional deficiency unrelated to celiac disease.

**Ontology:** HP:0008222 Female infertility; GO:0007566 embryo implantation; CL:0000351 trophoblast cell; CL:0002255 endometrial stromal cell.

# Proposed New Mechanism Nodes

| Proposed node | Upstream node | Principal downstream phenotypes | Strongest causal-placement evidence |
|---|---|---|---|
| Generalized small-intestinal malabsorption | Intestinal Epithelial Damage | Diarrhea, weight loss, anemia, deficiencies, growth failure | Celiac mucosal injury and persistent atrophy are associated with diarrhea, steatorrhea, weight loss, and deficiencies. DOI 10.3390/nu13041254. (montorohuguet2021smallandlarge pages 10-13) |
| Brush-border digestive/transport failure | Intestinal Epithelial Damage | Diarrhea, bloating; iron/folate deficits | Site-specific nutrient absorption and reduced mucosal capacity; direct symptom partitioning remains incomplete. (montorohuguet2021smallandlarge pages 24-25, montorohuguet2021smallandlarge pages 10-13) |
| Macronutrient malabsorption and negative energy balance | Generalized malabsorption | Weight loss, growth failure, short stature | Untreated human nutritional cohort: 17% had >10% undesired weight loss. DOI 10.3390/nu5103975. |
| Proximal-duodenal iron malabsorption | Intestinal Epithelial Damage | Iron deficiency anemia, fatigue branch | Abstract directly locates iron absorption in the damaged proximal duodenum. DOI 10.3390/nu13051695. (montorohuguet2021smallandlarge pages 24-25) |
| Folate/B12 malabsorption | Intestinal Epithelial Damage | Macrocytic anemia, neuropathy alternative, fatigue | Malabsorption review and GFD-follow-up evidence. DOI 10.3390/nu13041254. (montorohuguet2021smallandlarge pages 24-25) |
| Fat-soluble-vitamin malabsorption | Intestinal Epithelial Damage | Vitamin D deficiency, bone disease | Vitamins A/D/E/K are deficient in classical malabsorption; vitamin D rises after GFD. (montorohuguet2021smallandlarge pages 24-25) |
| Calcium/vitamin-D deficiency | Generalized malabsorption | Reduced BMD, osteoporosis, dental defects | Bone literature consistently identifies this branch. (krupakozak2014pathologicbonealterations pages 4-5, lungaro2023osteoporosisandceliac pages 2-4) |
| Secondary hyperparathyroidism | Calcium/vitamin-D deficiency | Reduced BMD, osteoporosis | Human clinical synthesis links deficiency to PTH-mediated resorption. (krupakozak2014pathologicbonealterations pages 4-5, altoma2022thedietaryand pages 2-4) |
| Inflammatory RANKL/OPG imbalance | Mixed Mucosal Cytokine Response | Reduced BMD, osteoporosis | Human cytokine/biomarker studies summarized in bone reviews; contribution is documented but heterogeneous. (krupakozak2014pathologicbonealterations pages 4-5, stefano2013bonemassand pages 10-12) |
| Growth-axis suppression | Malnutrition plus inflammation | Growth failure, short stature | Pediatric observational evidence and catch-up-growth literature; exact mediator remains incompletely tested. |
| TG3-specific IgA autoimmunity/epitope spreading | Autoantibody Production | Dermatitis herpetiformis | Human sera and dermal precipitates identify TG3 as dominant autoantigen. DOI 10.1084/jem.20011299. (patt2023unravelingtheimmunopathological pages 7-8, kaunisto2022antibodyresponsesto pages 1-3) |
| Dermal IgA–TG3 deposition and neutrophilic junction injury | TG3 autoimmunity | Dermatitis herpetiformis | Deposits are diagnostic; their exact lesion-initiating role remains unresolved. (kaunisto2022antibodyresponsesto pages 1-3) |
| TG6/anti-Purkinje neuroimmunity | Autoantibody Production | Cerebellar ataxia | Human serology/tissue association and neuropathology; effector causality remains proposed. (lauret2013celiacdiseaseand pages 6-7, rouvroye2020theneuropathologyof pages 13-15) |
| Immune-mediated peripheral axonopathy | Autoantibody Production/systemic immunity | Peripheral neuropathy | Human nerve pathology supports axonopathy and inflammatory infiltrates but not one dominant effector. (rouvroye2020theneuropathologyof pages 13-15) |
| Portal antigen/endotoxin exposure and celiac hepatitis | Barrier Dysfunction | Elevated transaminases | Permeability hypothesis plus enzyme normalization on dietary withdrawal. |
| Aberrant clonal IEL expansion/RCDII | Persistent epithelial IL-15 environment | EATL | RCDII is a low-grade clonal IEL proliferation that often precedes EATL. (cording2022oncogeneticlandscapeof pages 1-1, patt2023unravelingtheimmunopathological pages 5-7) |
| JAK1/STAT3-mutant IEL selection | RCDII | EATL | 80% of RCDII and 90% of EATL carried JAK1–STAT3 gain-of-function lesions. (cording2022oncogeneticlandscapeof pages 1-1) |
| Impaired amelogenesis | Nutrient deficiency/possible autoimmunity | Dental enamel defects | Strong epidemiology, but nutritional versus antibody branches remain unresolved. |
| Oral mucosal immune injury | Systemic immune response | Aphthous stomatitis | Association only; no decisive mechanistic study. |
| Gut–joint immune trafficking | Mucosal cytokines/dysbiosis | Arthritis | Hypothesis; diet-insensitive arthritis and shared autoimmunity are competing explanations. |
| Reproductive nutrient/endocrine dysfunction | Intestinal Epithelial Damage | Female infertility | Biologically plausible but not demonstrated as the dominant human mechanism. |
| Anti-TG2 trophoblast/endometrial injury | Autoantibody Production | Female infertility/implantation failure | Supported mainly by human-cell in-vitro and murine studies, not causal human trials. |

# Unwired Phenotypes

* **Constipation — NOT_ESTABLISHED:** prospective transit studies before and after verified mucosal healing, with thyroid disease, diet, medications, and pelvic-floor dysfunction controlled, would be needed.
* **Fatigue — NOT_ESTABLISHED:** a mechanistic intervention study jointly measuring cytokines, iron and other deficiencies, sleep, pain, mood, and mucosal healing is required to distinguish inflammatory from hematinic and psychosocial routes.
* **Recurrent Aphthous Stomatitis — NOT_ESTABLISHED:** serial oral immunophenotyping and hematinic correction/GFD studies with lesion recurrence as the endpoint would settle whether deficiency or local immunity mediates the association.
* **Peripheral Neuropathy — NOT_ESTABLISHED:** prospective nerve-biopsy or validated imaging/physiology studies linked to TG6/other antibodies, T-cell clonotypes, nutritional status, and gluten withdrawal are required.
* **Arthritis — NOT_ESTABLISHED:** incident-celiac cohorts with imaging-confirmed synovitis, immunophenotyping, genetic controls, and blinded assessment after dietary treatment would distinguish downstream celiac inflammation from coincident inflammatory arthritis.
* **Female infertility — NOT_ESTABLISHED:** adequately powered prospective fertility studies stratified by biopsy-proven disease, nutrient status, thyroid autoimmunity, anti-TG2 activity, and objectively verified GFD adherence are needed; trophoblast/endometrial target engagement must be demonstrated in vivo.

## Overall conclusion

Celiac phenotypes do not arise through one uniform downstream pathway. The best-supported convergence hub is **villous injury → nutrient malabsorption**, particularly proximal-duodenal iron loss and calcium/vitamin-D–PTH–bone remodeling. Two organ-specific immune branches are also persuasive: **TG3 IgA/dermal deposition in dermatitis herpetiformis** and **IL-15-selected clonal IELs with JAK1/STAT3 lesions in RCDII/EATL**. TG6-associated ataxia has compelling biomarkers and neuropathology but remains short of demonstrated antibody causality. For constipation, fatigue, aphthous stomatitis, peripheral neuropathy, arthritis, and infertility, association should not be encoded as downstream causation until competing nutritional, genetic, autoimmune, functional, and ascertainment explanations are resolved.

References

1. (montorohuguet2021smallandlarge pages 10-13): Miguel A. Montoro-Huguet, Blanca Belloc, and Manuel Domínguez-Cajal. Small and large intestine (i): malabsorption of nutrients. Nutrients, 13:1254, Apr 2021. URL: https://doi.org/10.3390/nu13041254, doi:10.3390/nu13041254. This article has 210 citations.

2. (montorohuguet2021smallandlarge pages 22-24): Miguel A. Montoro-Huguet, Blanca Belloc, and Manuel Domínguez-Cajal. Small and large intestine (i): malabsorption of nutrients. Nutrients, 13:1254, Apr 2021. URL: https://doi.org/10.3390/nu13041254, doi:10.3390/nu13041254. This article has 210 citations.

3. (merlotti2022bonefragilityin pages 5-7): Daniela Merlotti, Christian Mingiano, Roberto Valenti, Guido Cavati, Marco Calabrese, Filippo Pirrotta, Simone Bianciardi, Alberto Palazzuoli, and Luigi Gennari. Bone fragility in gastrointestinal disorders. International Journal of Molecular Sciences, 23:2713, Feb 2022. URL: https://doi.org/10.3390/ijms23052713, doi:10.3390/ijms23052713. This article has 39 citations.

4. (montorohuguet2021smallandlarge pages 24-25): Miguel A. Montoro-Huguet, Blanca Belloc, and Manuel Domínguez-Cajal. Small and large intestine (i): malabsorption of nutrients. Nutrients, 13:1254, Apr 2021. URL: https://doi.org/10.3390/nu13041254, doi:10.3390/nu13041254. This article has 210 citations.

5. (patt2023unravelingtheimmunopathological pages 7-8): Yonatan Shneor Patt, Adi Lahat, Paula David, Chen Patt, Rowand Eyade, and Kassem Sharif. Unraveling the immunopathological landscape of celiac disease: a comprehensive review. International Journal of Molecular Sciences, 24:15482, Oct 2023. URL: https://doi.org/10.3390/ijms242015482, doi:10.3390/ijms242015482. This article has 31 citations.

6. (kaunisto2022antibodyresponsesto pages 1-3): Helka Kaunisto, Teea Salmi, Katri Lindfors, and Esko Kemppainen. Antibody responses to transglutaminase 3 in dermatitis herpetiformis: lessons from celiac disease. International Journal of Molecular Sciences, 23:2910, Mar 2022. URL: https://doi.org/10.3390/ijms23062910, doi:10.3390/ijms23062910. This article has 26 citations.

7. (krupakozak2014pathologicbonealterations pages 4-5): Urszula Krupa-Kozak. Pathologic bone alterations in celiac disease: etiology, epidemiology, and treatment. Nutrition, 30(1):16-24, Jan 2014. URL: https://doi.org/10.1016/j.nut.2013.05.027, doi:10.1016/j.nut.2013.05.027. This article has 145 citations and is from a peer-reviewed journal.

8. (altoma2022thedietaryand pages 2-4): Abdulbaqi Al-Toma, Amin Herman, Willem F. Lems, and Chris J. J. Mulder. The dietary and non-dietary management of osteoporosis in adult-onset celiac disease: current status and practical guidance. Nutrients, 14:4554, Oct 2022. URL: https://doi.org/10.3390/nu14214554, doi:10.3390/nu14214554. This article has 15 citations.

9. (lungaro2023osteoporosisandceliac pages 2-4): Lisa Lungaro, Francesca Manza, Anna Costanzini, Marianna Barbalinardo, Denis Gentili, Fabio Caputo, Matteo Guarino, Giorgio Zoli, Umberto Volta, Roberto De Giorgio, and Giacomo Caio. Osteoporosis and celiac disease: updates and hidden pitfalls. Nutrients, 15:1089, Feb 2023. URL: https://doi.org/10.3390/nu15051089, doi:10.3390/nu15051089. This article has 52 citations.

10. (lauret2013celiacdiseaseand pages 6-7): Eugenia Lauret and Luis Rodrigo. Celiac disease and autoimmune-associated conditions. BioMed Research International, 2013:1-17, Jul 2013. URL: https://doi.org/10.1155/2013/127589, doi:10.1155/2013/127589. This article has 321 citations.

11. (rouvroye2020theneuropathologyof pages 13-15): Maxine D Rouvroye, Panagiotis Zis, Anne-Marie Van Dam, Annemieke J.M. Rozemuller, Gerd Bouma, and Marios Hadjivassiliou. The neuropathology of gluten-related neurological disorders: a systematic review. Nutrients, 12:822, Mar 2020. URL: https://doi.org/10.3390/nu12030822, doi:10.3390/nu12030822. This article has 56 citations.

12. (barton2008celiacdiseaseand pages 14-16): Susan H. Barton and Joseph A. Murray. Celiac disease and autoimmunity in the gut and elsewhere. Gastroenterology clinics of North America, 37 2:411-28,vii, Jun 2008. URL: https://doi.org/10.1016/j.gtc.2008.02.001, doi:10.1016/j.gtc.2008.02.001. This article has 108 citations and is from a peer-reviewed journal.

13. (cording2022oncogeneticlandscapeof pages 1-1): Sascha Cording, Ludovic Lhermitte, Georgia Malamut, Sofia Berrabah, Amélie Trinquand, Nicolas Guegan, Patrick Villarese, Sophie Kaltenbach, Bertrand Meresse, Sherine Khater, Michael Dussiot, Marc Bras, Morgane Cheminant, Bruno Tesson, Christine Bole-Feysot, Julie Bruneau, Thierry Jo Molina, David Sibon, Elizabeth Macintyre, Olivier Hermine, Christophe Cellier, Vahid Asnafi, and Nadine Cerf-Bensussan. Oncogenetic landscape of lymphomagenesis in coeliac disease. Gut, 71:497-508, Sep 2022. URL: https://doi.org/10.1136/gutjnl-2020-322935, doi:10.1136/gutjnl-2020-322935. This article has 116 citations and is from a highest quality peer-reviewed journal.

14. (chander2018pathogenesisofenteropathyassociated pages 1-2): Udit Chander, Rebecca J. Leeman-Neill, and Govind Bhagat. Pathogenesis of enteropathy-associated t cell lymphoma. Current Hematologic Malignancy Reports, 13:308-317, Jun 2018. URL: https://doi.org/10.1007/s11899-018-0459-5, doi:10.1007/s11899-018-0459-5. This article has 65 citations.

15. (botosso2023theroleof pages 6-8): Maiara Botosso, Renatta Damasceno, and Priscila Farage. The role of the gluten-free diet in the development of malignancies in celiac disease. Celiac Disease and Gluten-Free Diet, Jun 2023. URL: https://doi.org/10.5772/intechopen.110858, doi:10.5772/intechopen.110858. This article has 3 citations.

16. (hue2022cellularoriginsand pages 14-16): Susan Swee-Shan Hue, Siok-Bian Ng, Shi Wang, and Soo-Yong Tan. Cellular origins and pathogenesis of gastrointestinal nk- and t-cell lymphoproliferative disorders. Cancers, 14:2483, May 2022. URL: https://doi.org/10.3390/cancers14102483, doi:10.3390/cancers14102483. This article has 6 citations.

17. (gracefarfaglia2015bonesofcontention pages 13-15): Patricia Grace-Farfaglia. Bones of contention: bone mineral density recovery in celiac disease—a systematic review. Nutrients, 7:3347-3369, May 2015. URL: https://doi.org/10.3390/nu7053347, doi:10.3390/nu7053347. This article has 101 citations.

18. (patt2023unravelingtheimmunopathological pages 14-15): Yonatan Shneor Patt, Adi Lahat, Paula David, Chen Patt, Rowand Eyade, and Kassem Sharif. Unraveling the immunopathological landscape of celiac disease: a comprehensive review. International Journal of Molecular Sciences, 24:15482, Oct 2023. URL: https://doi.org/10.3390/ijms242015482, doi:10.3390/ijms242015482. This article has 31 citations.

19. (pelizzaro2021theriskof pages 2-4): Filippo Pelizzaro, Ilaria Marsilio, Matteo Fassan, Francesco Piazza, Brigida Barberio, Anna D’Odorico, Edoardo V. Savarino, Fabio Farinati, and Fabiana Zingone. The risk of malignancies in celiac disease—a literature review. Cancers, 13:5288, Oct 2021. URL: https://doi.org/10.3390/cancers13215288, doi:10.3390/cancers13215288. This article has 54 citations.

20. (stefano2013bonemassand pages 10-12): Michele Di Stefano, Caterina Mengoli, Manuela Bergonzi, and Gino Corazza. Bone mass and mineral metabolism alterations in adult celiac disease: pathophysiology and clinical approach. Nutrients, 5:4786-4799, Nov 2013. URL: https://doi.org/10.3390/nu5114786, doi:10.3390/nu5114786. This article has 89 citations.

21. (patt2023unravelingtheimmunopathological pages 5-7): Yonatan Shneor Patt, Adi Lahat, Paula David, Chen Patt, Rowand Eyade, and Kassem Sharif. Unraveling the immunopathological landscape of celiac disease: a comprehensive review. International Journal of Molecular Sciences, 24:15482, Oct 2023. URL: https://doi.org/10.3390/ijms242015482, doi:10.3390/ijms242015482. This article has 31 citations.

## Artifacts

- [Edison artifact artifact-00](Celiac_Disease-phenotype-wiring-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 27 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 66 |
| Resolved | 64 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005130` (2 mentions) - the report calls it "if available"; MONDO calls it **celiac disease**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CL:0000729` (obsolete tertiary pigment cell) (1 mention)
- `GO:0098742` (obsolete cell-cell adhesion via plasma-membrane adhesion molecules) (1 mention) - replaced by `GO:0098609`