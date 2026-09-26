---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-25T18:48:52.723874'
end_time: '2026-09-25T18:58:23.018354'
duration_seconds: 570.29
template_file: templates/disease_coverage_gap_research.md
template_sha: "10ed156e354b9080637624e4e1053f08c24ef096"
template_variables:
  disease_name: Celiac Disease
  mondo_id: MONDO:0005130
  existing_phenotypes: 'Gastrointestinal: chronic diarrhea, abdominal pain, bloating,
    constipation, villous atrophy. Systemic: weight loss, fatigue. Hematologic: iron
    deficiency anemia. Growth: growth failure in children, short stature. Dermatological:
    dermatitis herpetiformis. Musculoskeletal: reduced bone mineral density, arthritis.
    Skeletal: osteoporosis. Dental: dental enamel defects. Oral: recurrent aphthous
    stomatitis. Neurological: peripheral neuropathy, cerebellar ataxia. Hepatic: elevated
    hepatic transaminases. Metabolic: vitamin D deficiency. Neoplasm: small intestinal
    lymphoma. Reproductive: female infertility. Serology already recorded: anti-tTG
    IgA, anti-endomysial antibodies, anti-deamidated-gliadin-peptide antibodies, total
    IgA.'
  existing_mechanism: 'Gluten-triggered immune response (TG2 deamidation of gliadin,
    HLA-DQ2/DQ8 presentation, CD4 T-cell activation); mixed Th1/Th17/IL-21 mucosal
    cytokine response; intestinal epithelial damage (IL-15, NKG2D/MICA intraepithelial
    lymphocyte cytotoxicity, villous atrophy, crypt hyperplasia); autoantibody production;
    barrier dysfunction (zonulin, tight junctions); microbiome dysbiosis; generalized
    nutrient malabsorption; secondary hyperparathyroidism; aberrant clonal intraepithelial
    lymphocyte expansion (refractory disease type II, JAK1/STAT3 gain-of-function)
    leading to enteropathy-associated T-cell lymphoma. Treatment recorded: gluten-free
    diet, nutritional supplementation, corticosteroids for refractory disease, dietitian
    counseling, probiotics/prebiotics, HLA-DQ2/DQ8 genetic testing.'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 44
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 1
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 31
  verified: 31
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
  path: Celiac_Disease-coverage-gap-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Coverage-Gap Research Template

## Target Disease
- **Disease Name:** Celiac Disease
- **MONDO ID:** MONDO:0005130 (if available)

## What Is Already Curated — Do Not Re-Derive Any Of It

Clinical features already recorded, by organ system:

Gastrointestinal: chronic diarrhea, abdominal pain, bloating, constipation, villous atrophy. Systemic: weight loss, fatigue. Hematologic: iron deficiency anemia. Growth: growth failure in children, short stature. Dermatological: dermatitis herpetiformis. Musculoskeletal: reduced bone mineral density, arthritis. Skeletal: osteoporosis. Dental: dental enamel defects. Oral: recurrent aphthous stomatitis. Neurological: peripheral neuropathy, cerebellar ataxia. Hepatic: elevated hepatic transaminases. Metabolic: vitamin D deficiency. Neoplasm: small intestinal lymphoma. Reproductive: female infertility. Serology already recorded: anti-tTG IgA, anti-endomysial antibodies, anti-deamidated-gliadin-peptide antibodies, total IgA.

Mechanism already recorded:

Gluten-triggered immune response (TG2 deamidation of gliadin, HLA-DQ2/DQ8 presentation, CD4 T-cell activation); mixed Th1/Th17/IL-21 mucosal cytokine response; intestinal epithelial damage (IL-15, NKG2D/MICA intraepithelial lymphocyte cytotoxicity, villous atrophy, crypt hyperplasia); autoantibody production; barrier dysfunction (zonulin, tight junctions); microbiome dysbiosis; generalized nutrient malabsorption; secondary hyperparathyroidism; aberrant clonal intraepithelial lymphocyte expansion (refractory disease type II, JAK1/STAT3 gain-of-function) leading to enteropathy-associated T-cell lymphoma. Treatment recorded: gluten-free diet, nutritional supplementation, corticosteroids for refractory disease, dietitian counseling, probiotics/prebiotics, HLA-DQ2/DQ8 genetic testing.

**Everything above is done.** Do not restate it, re-justify it, or return it as a
finding. A report that re-describes the established mechanism has failed this
brief.

## Research Objective — Absences Only

Report what a complete account of this disease would contain that the list
above does **not**. Two passes:

### Pass 1 — Organ-system fan-out for missing clinical features

Work through each organ system in turn — gastrointestinal, hepatic,
hematologic, skeletal, endocrine, cardiovascular, renal, respiratory,
neurologic, psychiatric, dermatologic, oral and dental, reproductive and
obstetric, ophthalmic, immune and infectious susceptibility, neoplastic — and
for each, name any clinical feature of this disease **not** in the list above.
For each new feature report:

- the feature, with a suggested HPO term
- its frequency among affected individuals, as reported, with the source
- whether it is a feature of the disease, a treatment effect, or a feature of a
  comorbid condition that travels with the disease — these are different claims
  and must not be blended
- one PMID with an exact quote from the abstract

Say explicitly when an organ system has nothing to add. An empty system is a
useful result, not a gap in the report.

### Pass 2 — Missing structured dimensions

For each of the following, report what the literature establishes, or state
that the dimension does not apply to this disease:

- **Histopathology and grading.** The named histological classification used in
  practice, its grades or stages in order, and what distinguishes each from the
  one before it. Give the classification's own terminology.
- **Disease subtypes and clinical forms.** The recognized forms, what defines
  each, and their relative frequency. Include forms defined by absence of a
  usual feature, and treatment-refractory forms.
- **Progression and natural history.** Ordered phases, what drives movement
  between them, and what is reversible at each.
- **Animal models.** Species, genotype or intervention, which disease features
  each reproduces, and which it fails to reproduce.
- **Non-animal experimental models.** Organoids, organ-chips, primary or iPSC
  cultures: what each system captures and what it omits.
- **Interventional trials.** Registered trials of disease-modifying therapy,
  with registry identifiers, phase, status, and primary result where reported.
- **Comorbid conditions** that co-occur at above-background rates, with the
  measured strength of association, and whether shared genetic susceptibility
  is the proposed explanation.
- **Biomarkers and laboratory monitoring** beyond the diagnostic antibodies
  already listed, including reference intervals where standardized.

## Rules

- **Absence is the deliverable.** If a dimension is genuinely well covered by
  what is already curated, say so in one line and move on.
- **Do not inflate.** A feature reported once in a single case report is
  reported as exactly that. Do not present a case report as a disease feature.
- **Distinguish the disease from its treatment.** Where a feature is caused by
  the therapy rather than the disease, say so.
- Cite primary literature with PMIDs and exact abstract quotes. Never cite a
  paper for a claim its abstract does not make. Where a registry identifier is
  the right citation, give the registry identifier.


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

# Coverage-Gap Research Template

## Target Disease
- **Disease Name:** Celiac Disease
- **MONDO ID:** MONDO:0005130 (if available)

## What Is Already Curated — Do Not Re-Derive Any Of It

Clinical features already recorded, by organ system:

Gastrointestinal: chronic diarrhea, abdominal pain, bloating, constipation, villous atrophy. Systemic: weight loss, fatigue. Hematologic: iron deficiency anemia. Growth: growth failure in children, short stature. Dermatological: dermatitis herpetiformis. Musculoskeletal: reduced bone mineral density, arthritis. Skeletal: osteoporosis. Dental: dental enamel defects. Oral: recurrent aphthous stomatitis. Neurological: peripheral neuropathy, cerebellar ataxia. Hepatic: elevated hepatic transaminases. Metabolic: vitamin D deficiency. Neoplasm: small intestinal lymphoma. Reproductive: female infertility. Serology already recorded: anti-tTG IgA, anti-endomysial antibodies, anti-deamidated-gliadin-peptide antibodies, total IgA.

Mechanism already recorded:

Gluten-triggered immune response (TG2 deamidation of gliadin, HLA-DQ2/DQ8 presentation, CD4 T-cell activation); mixed Th1/Th17/IL-21 mucosal cytokine response; intestinal epithelial damage (IL-15, NKG2D/MICA intraepithelial lymphocyte cytotoxicity, villous atrophy, crypt hyperplasia); autoantibody production; barrier dysfunction (zonulin, tight junctions); microbiome dysbiosis; generalized nutrient malabsorption; secondary hyperparathyroidism; aberrant clonal intraepithelial lymphocyte expansion (refractory disease type II, JAK1/STAT3 gain-of-function) leading to enteropathy-associated T-cell lymphoma. Treatment recorded: gluten-free diet, nutritional supplementation, corticosteroids for refractory disease, dietitian counseling, probiotics/prebiotics, HLA-DQ2/DQ8 genetic testing.

**Everything above is done.** Do not restate it, re-justify it, or return it as a
finding. A report that re-describes the established mechanism has failed this
brief.

## Research Objective — Absences Only

Report what a complete account of this disease would contain that the list
above does **not**. Two passes:

### Pass 1 — Organ-system fan-out for missing clinical features

Work through each organ system in turn — gastrointestinal, hepatic,
hematologic, skeletal, endocrine, cardiovascular, renal, respiratory,
neurologic, psychiatric, dermatologic, oral and dental, reproductive and
obstetric, ophthalmic, immune and infectious susceptibility, neoplastic — and
for each, name any clinical feature of this disease **not** in the list above.
For each new feature report:

- the feature, with a suggested HPO term
- its frequency among affected individuals, as reported, with the source
- whether it is a feature of the disease, a treatment effect, or a feature of a
  comorbid condition that travels with the disease — these are different claims
  and must not be blended
- one PMID with an exact quote from the abstract

Say explicitly when an organ system has nothing to add. An empty system is a
useful result, not a gap in the report.

### Pass 2 — Missing structured dimensions

For each of the following, report what the literature establishes, or state
that the dimension does not apply to this disease:

- **Histopathology and grading.** The named histological classification used in
  practice, its grades or stages in order, and what distinguishes each from the
  one before it. Give the classification's own terminology.
- **Disease subtypes and clinical forms.** The recognized forms, what defines
  each, and their relative frequency. Include forms defined by absence of a
  usual feature, and treatment-refractory forms.
- **Progression and natural history.** Ordered phases, what drives movement
  between them, and what is reversible at each.
- **Animal models.** Species, genotype or intervention, which disease features
  each reproduces, and which it fails to reproduce.
- **Non-animal experimental models.** Organoids, organ-chips, primary or iPSC
  cultures: what each system captures and what it omits.
- **Interventional trials.** Registered trials of disease-modifying therapy,
  with registry identifiers, phase, status, and primary result where reported.
- **Comorbid conditions** that co-occur at above-background rates, with the
  measured strength of association, and whether shared genetic susceptibility
  is the proposed explanation.
- **Biomarkers and laboratory monitoring** beyond the diagnostic antibodies
  already listed, including reference intervals where standardized.

## Rules

- **Absence is the deliverable.** If a dimension is genuinely well covered by
  what is already curated, say so in one line and move on.
- **Do not inflate.** A feature reported once in a single case report is
  reported as exactly that. Do not present a case report as a disease feature.
- **Distinguish the disease from its treatment.** Where a feature is caused by
  the therapy rather than the disease, say so.
- Cite primary literature with PMIDs and exact abstract quotes. Never cite a
  paper for a claim its abstract does not make. Where a registry identifier is
  the right citation, give the registry identifier.


# Celiac disease (MONDO:0005130): coverage-gap report

## Scope and evidentiary limitation

This report contains **only information absent from the supplied curated record**. It does not repeat the recorded manifestations, serology, mechanism, or treatment.

A strict limitation is necessary: the retrieved corpus supplied DOI-level full text and abstract text but did **not consistently expose PubMed identifiers**. Therefore, I give a PMID only where it was verifiable from the retrieved evidence; I do not invent PMIDs. Likewise, quotation marks below are used only for text actually present in a retrieved abstract. Features lacking a feature-specific primary abstract, frequency, and PMID are explicitly marked **insufficient for strict HPO curation**, even when reviews describe an association.

The principal high-confidence gaps are summarized here:

| Dimension/system | Missing item | Quantitative evidence | Classification | Strongest source |
|---|---|---:|---|---|
| Hematologic/nutritional | Hypoproteinemia | 18.52% (20/108 adults) | Nutritional consequence of active disease | Pop et al., 2024; DOI: 10.15386/mpr-2776 (pop2024extradigestivemanifestationsof pages 2-4) |
| Hematologic/nutritional | Vitamin B12/folate-deficiency anemia | 9.26% (10/108 adults) | Nutritional consequence; distinct from iron-deficiency anemia | Pop et al., 2024; DOI: 10.15386/mpr-2776 (pop2024extradigestivemanifestationsof pages 2-4) |
| Skeletal/musculoskeletal | Osteopenia, fractures, joint pain | Osteopenia 35–42%; joint pain 20–30% at diagnosis; fracture frequency not quantified | Direct disease-associated manifestations, partly mediated by nutritional deficits | Santonicola et al., 2024; DOI: 10.3390/nu16121814 (santonicola2024associationsbetweenceliac pages 7-9) |
| Endocrine | Hashimoto thyroiditis | 14.81% (16/108 adults) | Associated autoimmune comorbidity | Pop et al., 2024; DOI: 10.15386/mpr-2776 (pop2024extradigestivemanifestationsof pages 2-4) |
| Cardiovascular/thrombotic | Venous or splanchnic thrombosis; atrial fibrillation | No reliable disease-wide frequency retrieved | Association; thrombosis may be promoted by vitamin-K/protein C/S deficiency. Atrial-fibrillation evidence is observational | Pop et al., 2024; DOI: 10.15386/mpr-2776 (pop2024extradigestivemanifestationsof pages 1-2) |
| Renal | Urolithiasis | Frequency not established | Reported disease-associated manifestation; prevalence evidence is insufficient | Lupu et al., 2024; DOI: 10.3389/fimmu.2024.1390755 (lupu2024celiacdisease pages 7-8) |
| Respiratory | Asthma | 4.63% (5/108 adults in one tertiary cohort) | Associated comorbidity, not an established direct manifestation | Pop et al., 2024; DOI: 10.15386/mpr-2776 (pop2024extradigestivemanifestationsof pages 2-4) |
| Neurologic | Headache/migraine; epilepsy | Epilepsy 2.78% (3/108 adults); headache/migraine frequency not established | Disease-associated neurologic features; epilepsy estimate is single-center | Lupu et al., 2024, DOI: 10.3389/fimmu.2024.1390755; Pop et al., 2024, DOI: 10.15386/mpr-2776 (pop2024extradigestivemanifestationsof pages 2-4, lupu2024celiacdisease pages 8-8) |
| Psychiatric | Depression; anxiety | Depression 9.26%; anxiety 8.33% in a 108-adult cohort | Associated psychiatric comorbidity | Pop et al., 2024; DOI: 10.15386/mpr-2776 (pop2024extradigestivemanifestationsof pages 2-4) |
| Dermatologic | Psoriasis; alopecia areata; atopic dermatitis | Psoriasis 7.41% (8/108 adults); no robust frequency for alopecia or atopic dermatitis | Associated inflammatory or autoimmune comorbidities | Santonicola et al., 2024, DOI: 10.3390/nu16121814; Pop et al., 2024, DOI: 10.15386/mpr-2776 (pop2024extradigestivemanifestationsof pages 2-4, santonicola2024associationsbetweenceliac pages 7-9) |
| Oral | Xerostomia; atrophic glossitis; angular cheilitis | Xerostomia 15% vs 5% of controls; glossitis 6.3% vs 0%; cheilitis not quantified | Disease-associated oral findings, potentially mediated by nutritional deficiency | Santonicola et al., 2024; DOI: 10.3390/nu16121814 (santonicola2024associationsbetweenceliac pages 2-4) |
| Reproductive/obstetric | Miscarriage, stillbirth, fetal-growth restriction, preterm delivery, low birth weight | Stillbirth before diagnosis 0.45% vs 0.29%; FGR 11.7% vs 1.7%; preterm delivery 10.4% vs 6.9%; low birth weight 14.2% vs 6.7% | Adverse outcomes associated mainly with undiagnosed or untreated disease | Santonicola et al., 2024; DOI: 10.3390/nu16121814 (santonicola2024associationsbetweenceliac pages 13-14) |
| ENT/neurologic | Sensorineural hearing loss | No dependable prevalence retrieved | Reported disease-associated manifestation; quantitative evidence is inadequate | Karunaratne & Karunaratne, 2022; DOI: 10.1177/0145561320972604 |
| Immune/infectious | Infection susceptibility | No adequate quantitative evidence retrieved | Insufficient evidence for inclusion as an independent direct feature | Evidence inadequate for a high-confidence source |
| Complicated disease | Refractory celiac disease types I and II | Prevalence 0.31–0.38%; 10-year cumulative incidence 1–4%; five-year survival up to 95% for type I and 58% for type II | Disease subtypes; type II has aberrant clonal IELs and greater lymphoma risk | Villanacci et al., 2020; DOI: 10.32074/1591-951x-157 (villanacci2020celiacdiseasehistologydifferential pages 7-9) |
| Interventional trials | ZED1227, oral TG2 inhibitor | Phase 2, 163 participants; dose-dependent preservation of villous-height:crypt-depth ratio and reduced IEL density | Investigational disease-modifying therapy | Massironi et al., 2024; DOI: 10.3748/wjg.v30.i38.4194 (massironi2024beyondtheglutenfree pages 9-10) |
| Interventional trials | KAN-101, antigen-specific immune tolerance | Phase 2 completed; 55 participants; definitive clinical efficacy not reported in retrieved evidence | Investigational disease-modifying therapy | NCT06001177; earlier NCT04248855 and NCT05574010 (kowalski2024celiacdisease—newinsights pages 8-9, buiten2021gliadinsequestrationas pages 8-9) |
| Interventional trials | Latiglutenase, gluten-degrading enzyme | Multiple completed Phase 2 studies; symptom and histology results have varied | Investigational adjunct for inadvertent gluten exposure | NCT03585478; NCT04243551 (massironi2024beyondtheglutenfree pages 4-5, buiten2021gliadinsequestrationas pages 9-10) |
| Interventional trials | Larazotide acetate | Multiple Phase 2 studies completed; Phase 3 registered; confirmatory benefit not established in retrieved evidence | Investigational barrier-directed adjunct | NCT03569007 (buiten2021gliadinsequestrationas pages 8-9, buiten2021gliadinsequestrationas pages 10-12) |
| Interventional trials | Nexvax2 peptide immunotherapy | Phase 2 discontinued after interim analysis for lack of significant protection against gluten-induced symptoms | Investigational therapy with negative efficacy signal | NCT03644069 (buiten2021gliadinsequestrationas pages 6-8, crepaldi2023emergingpharmaceuticaltherapies pages 10-11) |
| Interventional trials | Anti-IL-15 therapy | AMG714 did not prevent mucosal injury versus placebo, although some symptom and IEL signals favored 300 mg | Investigational immunomodulatory therapy | NCT02633020; PRV-015 NCT04424927 (buiten2021gliadinsequestrationas pages 6-8, crepaldi2023emergingpharmaceuticaltherapies pages 10-11) |


*Table: Compact evidence table of high-confidence clinical, subtype, and therapeutic gaps absent from the curated celiac-disease record. It separates direct manifestations, nutritional effects, associated comorbidities, and investigational treatments.*

# Pass 1 — Missing clinical features by organ system

Suggested HPO labels should be checked against the current HPO release before database ingestion.

## 1. Gastrointestinal

- **Hypoproteinemia / protein-losing enteropathy phenotype** — suggested HPO: **Hypoproteinemia, HP:0003075**. Frequency: 20/108 adults (18.52%) in one 2024 tertiary-center cohort. This is best classified as a **nutritional/intestinal consequence of active disease**, not a treatment effect. Abstract quote: “Iron deficiency anemia was the most common extra-digestive manifestation, affecting 20.37% of patients, followed by hypoproteinemia (18.52%).” DOI: [10.15386/mpr-2776](https://doi.org/10.15386/mpr-2776), published July 2024. PMID was not exposed in the retrieved record. (pop2024extradigestivemanifestationsof pages 2-4)
- **Pancreatitis, duodenal ulcer, and protein-losing enteropathy as separate direct features:** reported in reviews, but no disease-wide frequency and qualifying primary abstract/PMID were retrieved. They should therefore remain **candidate associations**, not curated disease features. (lupu2024celiacdisease pages 7-8)

## 2. Hepatic

- **Non-alcoholic steatohepatitis** — suggested HPO: **Steatohepatitis, HP:0001397**. Reviews list it in pediatric celiac disease, but the retrieved evidence supplies neither a reliable frequency nor a qualifying primary abstract. Classification: **reported disease association**, presently insufficient for strict HPO curation. (lupu2024celiacdisease pages 7-8)
- **Autoimmune hepatitis and primary biliary cholangitis** belong under **comorbid autoimmune disease**, not direct manifestations. No sufficiently supported new direct hepatic feature beyond the already-recorded transaminase elevation was found.

## 3. Hematologic

- **Vitamin B12/folate-deficiency anemia** — suggested HPO: **Megaloblastic anemia, HP:0001889** or the more specific nutrient-deficiency term as applicable. Frequency: 10/108 adults (9.26%) in one cohort. Classification: **nutritional consequence**, distinct from the already-curated iron-deficiency anemia. The study’s abstract reports broad extra-digestive manifestations but does not contain this exact subgroup value; it appears in the study results, so the strict “exact abstract quote” requirement is not met. DOI: [10.15386/mpr-2776](https://doi.org/10.15386/mpr-2776), July 2024. (pop2024extradigestivemanifestationsof pages 2-4)
- **Thrombocytosis and coagulopathy** — suggested HPO: **Thrombocytosis, HP:0001894**; **Abnormality of coagulation, HP:0001928**. These are reported, plausibly secondary to inflammation or nutrient deficiency, but no robust frequency or qualifying primary abstract was retrieved. Do not treat antiphospholipid antibodies as a direct celiac feature without excluding antiphospholipid syndrome. (lupu2024celiacdisease pages 7-8)

## 4. Skeletal and musculoskeletal

- **Osteopenia** — suggested HPO: **Osteopenia, HP:0000938**. Reported prevalence was 35–42% across adult cohorts and 39.6% in a systematic review of men and premenopausal women. Classification: **disease-associated skeletal consequence**, commonly mediated by malabsorption; distinct from already-recorded osteoporosis/reduced bone density. (santonicola2024associationsbetweenceliac pages 7-9)
- **Pathologic or low-trauma fracture** — suggested HPO: **Pathologic fracture, HP:0002756**. Recognized association, but a dependable frequency was not retrieved. Classification: **downstream skeletal consequence**, not a treatment effect. (santonicola2024associationsbetweenceliac pages 7-9)
- **Arthralgia/joint pain** — suggested HPO: **Arthralgia, HP:0002829**. Frequency: approximately 20–30% at diagnosis. Classification: **disease-associated musculoskeletal manifestation**; it should not be conflated with rheumatoid arthritis or another comorbidity. (santonicola2024associationsbetweenceliac pages 7-9)
- **Myalgia** — suggested HPO: **Myalgia, HP:0003326**. Frequency not established; likely a mixed nutritional/inflammatory consequence. Evidence of treatment response is inconsistent and is not proof of primary causation. (santonicola2024associationsbetweenceliac pages 7-9)

## 5. Endocrine

- **Delayed puberty** — suggested HPO: **Delayed puberty, HP:0000823**. Reported as a pediatric association; no reliable disease-wide frequency or qualifying abstract was retrieved. Classification: **secondary endocrine/growth consequence**, potentially reversible after disease control. (lupu2024celiacdisease pages 8-8)
- **Hashimoto thyroiditis** — suggested HPO: **Autoimmune thyroiditis, HP:0002923**. Frequency: 16/108 adults (14.81%) in one tertiary cohort. Classification: **autoimmune comorbidity**, not a direct manifestation. Abstract quote: “Iron deficiency anemia was the most common extra-digestive manifestation, affecting 20.37% of patients, followed by hypoproteinemia (18.52%) and Hashimoto’s thyroiditis (14.81%).” DOI: [10.15386/mpr-2776](https://doi.org/10.15386/mpr-2776), July 2024. (pop2024extradigestivemanifestationsof pages 2-4)

## 6. Cardiovascular and thrombotic

- **Thromboembolism, including portal/splenic-vein thrombosis and Budd–Chiari syndrome** — suggested HPO: **Venous thrombosis, HP:0004936**. No reliable population frequency was retrieved. Classification: **associated complication**, potentially mediated by vitamin-K-dependent protein C/S deficiency or coexisting thrombophilia; it should not be recorded as a universal direct feature. (pop2024extradigestivemanifestationsof pages 1-2)
- **Atrial fibrillation, ischemic heart disease, cardiomyopathy, and valvular insufficiency** are observational associations. One tertiary cohort recorded “cardiovascular disease” in 12.04%, but that nonspecific category is unsuitable for HPO curation. No adequate feature-specific primary abstract/frequency was retrieved. (pop2024extradigestivemanifestationsof pages 2-4, pop2024extradigestivemanifestationsof pages 4-5)
- **Pericarditis** remains case-report-level or otherwise unconfirmed evidence and should not be promoted to a disease feature. (pop2024extradigestivemanifestationsof pages 1-2)

## 7. Renal

- **Urolithiasis** — suggested HPO: **Nephrolithiasis, HP:0000787**. Reported in reviews, but no dependable prevalence or qualifying primary abstract was retrieved. Classification: **possible disease-associated metabolic complication**, not yet high-confidence HPO evidence. (lupu2024celiacdisease pages 7-8)
- No other renal feature met the specified evidence threshold.

## 8. Respiratory

- **Asthma** occurred in 5/108 adults (4.63%) in one tertiary cohort. Suggested HPO: **Asthma, HP:0002099**. Classification: **comorbid condition**, not a demonstrated direct celiac manifestation. The value is not stated in the paper’s abstract and therefore fails the strict abstract-quotation requirement. (pop2024extradigestivemanifestationsof pages 2-4)
- **Obstructive sleep apnea** has been reported in an ENT review, but frequency and causal attribution remain inadequate; treat as an association rather than a direct feature.

## 9. Neurologic

- **Headache/migraine** — suggested HPO: **Migraine, HP:0002076**. Reviews identify it as associated, but no reliable frequency or qualifying primary abstract was retrieved. Classification: **disease-associated neurologic complaint**. (lupu2024celiacdisease pages 8-8)
- **Epilepsy** — suggested HPO: **Seizure, HP:0001250**. Frequency: 3/108 (2.78%) in one tertiary cohort. Classification: **associated neurologic condition**, not proven direct causation. The exact value is not in the abstract. (pop2024extradigestivemanifestationsof pages 2-4)
- **Cognitive impairment/“brain fog”** — suggested HPO: **Impaired cognition, HP:0100543**. A treated-cohort survey reported neurocognitive symptoms in 89% of 1,143 respondents, but selection and self-report prevent interpreting this as disease-wide prevalence or as an effect caused by the diet. (pop2024extradigestivemanifestationsof pages 4-5)
- **Sensorineural hearing loss** — suggested HPO: **Sensorineural hearing impairment, HP:0000407**. An ENT review describes it as potentially progressive and permanent, but no dependable prevalence was retrieved. It is best classified as a **reported disease-associated manifestation**, not a treatment effect.

## 10. Psychiatric

- **Depressive disorder** — suggested HPO: **Depression, HP:0000716**. Frequency: 10/108 (9.26%) in one cohort. Classification: **associated psychiatric comorbidity**; causation may involve chronic illness burden and nutritional factors. (pop2024extradigestivemanifestationsof pages 2-4)
- **Anxiety disorder** — suggested HPO: **Anxiety, HP:0000739**. Frequency: 9/108 (8.33%) in the same cohort. Classification: **associated comorbidity**, not necessarily a direct immune manifestation. (pop2024extradigestivemanifestationsof pages 2-4)
- Bipolar disorder, irritability, apathy, and sleep complaints are described in reviews, but robust disease-specific frequencies and qualifying primary abstracts were not retrieved. (pop2024extradigestivemanifestationsof pages 1-2)

## 11. Dermatologic

- **Psoriasis** — suggested HPO: **Psoriasis, HP:0003765**. Frequency: 8/108 (7.41%) in one cohort. Classification: **associated immune-mediated comorbidity**, not a direct celiac lesion. (pop2024extradigestivemanifestationsof pages 2-4)
- **Alopecia areata, atopic dermatitis, rosacea, vitiligo, chronic urticaria, and linear-IgA bullous dermatosis** are reported associations. No adequate feature-specific frequency and primary abstract were retrieved; none should be merged with the already-curated dermatitis herpetiformis. (lupu2024celiacdisease pages 7-8, santonicola2024associationsbetweenceliac pages 7-9)
- **Erythema nodosum** occurred in 1/108 (0.93%) in one cohort. This is a single-center observation, not adequate evidence for a general disease feature. (pop2024extradigestivemanifestationsof pages 2-4)

## 12. Oral and dental

- **Xerostomia** — suggested HPO: **Xerostomia, HP:0000217**. Frequency: 15% versus 5% of controls in one study. Classification: **disease-associated oral finding**. (santonicola2024associationsbetweenceliac pages 2-4)
- **Atrophic glossitis** — suggested HPO: **Atrophic glossitis, HP:0000225**. Frequency: 6.3% versus 0% of controls. Classification: **oral/nutritional consequence**. (santonicola2024associationsbetweenceliac pages 2-4)
- **Angular cheilitis** — suggested HPO: **Cheilitis, HP:0100825**. Frequency not retrieved; likely a nutritional consequence. (santonicola2024associationsbetweenceliac pages 2-4)
- **Delayed tooth eruption** — suggested HPO: **Delayed eruption of teeth, HP:0000684**. Frequency not reliably retrieved. Classification: **developmental/dental association**. (santonicola2024associationsbetweenceliac pages 2-4)
- **Dental caries and periodontitis** are reported associations but are multifactorial; no sufficiently controlled prevalence suitable for direct disease annotation was retrieved. (santonicola2024associationsbetweenceliac pages 2-4)

## 13. Reproductive and obstetric

These are principally features of **undiagnosed or untreated maternal disease**, not effects of a gluten-free diet.

- **Spontaneous abortion** — suggested HPO: **Recurrent spontaneous abortion, HP:0200067**, only when recurrent. A US survey reported 50.6% versus 40.6% in controls; 85% of losses in affected participants occurred before diagnosis. (santonicola2024associationsbetweenceliac pages 13-14)
- **Stillbirth** — suggested HPO: **Stillbirth, HP:0003826**. Danish cohort: 0.45% before diagnosis versus 0.29% in controls, but 0.32% versus 0.29% after diagnosis. This temporal pattern supports untreated disease as the risk state. (santonicola2024associationsbetweenceliac pages 13-14)
- **Fetal growth restriction** — suggested HPO: **Intrauterine growth retardation, HP:0001511**. Frequency: 11.7% versus 1.7% of controls in a Slovenian study. (santonicola2024associationsbetweenceliac pages 13-14)
- **Preterm delivery** — suggested HPO: **Premature birth, HP:0001622**. Frequency: 10.4% versus 6.9% in Israeli data. (santonicola2024associationsbetweenceliac pages 13-14)
- **Low birth weight** — suggested HPO: **Low birth weight, HP:0001518**. Frequency: 14.2% versus 6.7%. (santonicola2024associationsbetweenceliac pages 13-14)
- **Menstrual irregularity/amenorrhea and delayed puberty** are reported but lacked qualifying frequencies in the retrieved corpus. (lupu2024celiacdisease pages 8-8)

The 2024 review’s abstract-level conclusion is appropriately cautious: “Most CeD-mediated disorders can be treated with a strict gluten-free diet (GFD), but some of them are irreversible unless CeD is diagnosed in time.” DOI: [10.3390/nu16121814](https://doi.org/10.3390/nu16121814), published June 2024. (santonicola2024associationsbetweenceliac pages 13-14)

## 14. Ophthalmic

- **Central retinal-vein occlusion** appears in a pediatric review but without population frequency or adequate causal evidence. It should be treated as a **rare reported association**, not an established disease feature. (lupu2024celiacdisease pages 7-8)
- No ophthalmic manifestation met the requested combination of prevalence, primary abstract, and PMID. Therefore, **nothing high-confidence should be added** to a structured disease record from the retrieved evidence.

## 15. Immune and infectious susceptibility

- Autoimmune clustering is clear, but that belongs under comorbidities below.
- The retrieved evidence did not establish a sufficiently quantified, independent infectious-susceptibility phenotype with a qualifying primary abstract. **Nothing should be added as a direct infectious feature.** Vaccine recommendations or coverage patterns are clinical-management issues, not disease phenotypes.

## 16. Neoplastic

- Beyond the already-curated small-intestinal lymphoma/EATL risk, the retrieved evidence did not support an additional neoplasm with sufficient specificity and quantitative primary evidence. **Nothing to add.**

# Pass 2 — Missing structured dimensions

## Histopathology and grading

### Modified Marsh–Oberhuber classification

1. **Type 0, pre-infiltrative:** normal villous architecture and crypts; IEL count below the scheme’s threshold.
2. **Type 1, infiltrative:** increased IELs, with otherwise preserved architecture.
3. **Type 2, hyperplastic:** Type 1 changes plus crypt hyperplasia/increased mitotic activity; villi remain preserved.
4. **Type 3a, partial villous atrophy:** increased IELs and crypt hyperplasia plus mild/partial villous shortening.
5. **Type 3b, subtotal villous atrophy:** more marked, nearly complete villous shortening.
6. **Type 3c, total villous atrophy:** flat mucosa with complete villous loss.
7. **Type 4, hypoplastic/atrophic:** complete villous atrophy without the typical crypt hyperplasia or raised IEL count; uncommon and not part of every contemporary reporting implementation. (kowalski2024celiacdisease—newinsights pages 5-6)

IEL thresholds have varied historically—30/100 enterocytes in older formulations and commonly 25/100 in contemporary practice—so the report must name the threshold used. The ordinal score also has substantial interobserver variability; recent machine-learning work therefore quantifies IELs, villous area, and crypt/villous ratios continuously rather than relying solely on category assignment.

A 2020 pathology review states: “Biopsy of duodenal mucosa remains the gold standard in the diagnosis of celiac disease with the recognition of the spectrum of histological changes and classification of mucosa damage based on updated Corazza-Villanacci system.” DOI: [10.32074/1591-951x-157](https://doi.org/10.32074/1591-951x-157), September 2020. (villanacci2020celiacdiseasehistologydifferential pages 7-9)

### Corazza–Villanacci classification

This simplified system improves reproducibility:

- **Grade A, non-atrophic:** increased IELs with normal villous architecture.
- **Grade B1, atrophic:** villous shortening with a villous-to-crypt ratio below normal, but villi remain identifiable.
- **Grade B2, atrophic-flat:** complete villous flattening.

A simplified classification uses three villous morphologies and an IEL threshold above 25/100 enterocytes. Its purpose is to reduce the poor agreement produced by the larger Marsh–Oberhuber category set. (villanacci2020celiacdiseasehistologydifferential pages 7-9)

## Disease subtypes and clinical forms

- **Classical:** malabsorptive gastrointestinal presentation.
- **Non-classical:** extraintestinal or nonspecific presentation without the classical malabsorptive syndrome.
- **Asymptomatic/silent:** no recognized symptoms but serologic and histologic disease; usually detected by screening. “Silent” is sometimes restricted to asymptomatic villous atrophy.
- **Potential celiac disease:** positive disease-specific serology with normal small-intestinal architecture; some patients later develop enteropathy.
- **Latent:** historically used either for previously abnormal disease normalized on diet or normal mucosa that subsequently becomes abnormal; because of ambiguity, contemporary reports should define the intended meaning.
- **Seronegative celiac disease:** compatible enteropathy and clinical/genetic context despite negative standard disease serology, after exclusion of other seronegative enteropathies. No dependable relative frequency was retrieved.
- **Nonresponsive celiac disease:** persistent or recurrent symptoms, laboratory abnormalities, or enteropathy despite 6–12 months of prescribed diet; most cases are not refractory disease and require evaluation for ongoing exposure, another diagnosis, or a complication.
- **Refractory celiac disease (RCD):** persistent/recurrent malabsorptive symptoms and villous atrophy despite strict diet after alternative causes are excluded. Prevalence is approximately 0.31–0.38%; reported 10-year cumulative incidence is 1–4%. (verma2019identificationofa pages 32-37, villanacci2020celiacdiseasehistologydifferential pages 7-9)
  - **RCD type I:** phenotypically normal IELs retaining surface CD3/CD8/CD103, without monoclonal TCR rearrangement. Five-year survival may reach 95%; five-year EATL development is below 14%.
  - **RCD type II:** aberrant clonal IEL population—commonly >20–25% CD45-positive cells lacking surface CD3 by flow cytometry or >50% CD8-negative intraepithelial T cells by immunohistochemistry—with monoclonal TCR rearrangement. Five-year survival is about 58%, with substantially greater lymphoma risk. (villanacci2020celiacdiseasehistologydifferential pages 7-9)

Relative frequencies for classical, non-classical, silent, potential, and seronegative forms are highly dependent on referral and screening context; no defensible common denominator was retrieved, so none is asserted.

## Progression and natural history

A practical ordered model is:

1. **Genetic susceptibility without disease:** normal serology and mucosa; no lesion requiring reversal.
2. **Early immune/serologic phase:** disease-specific immune markers may precede enteropathy; circulating miRNA studies found candidate changes more than one year before conventional seroconversion, but these are not validated clinical predictors. (ramirezsanchez2020molecularbiomarkersfor pages 1-3)
3. **Potential disease:** positive serology with preserved villi; progression is not inevitable, and reliable individual prediction remains unavailable. (verma2019identificationofa pages 32-37)
4. **Active enteropathy:** IEL expansion, crypt hyperplasia, and increasing villous injury; removal of exposure generally improves symptoms and biochemical abnormalities before histologic recovery.
5. **Treated remission or persistent injury:** symptoms can resolve despite residual enteropathy. In one adult cohort, 36.3% still had gastrointestinal symptoms or malabsorption signs after a mean 16 months of adequate diet, and symptoms did not correlate with histology. Serology likewise correlates imperfectly with mucosal healing. (bragde2019biomarkersofinflammation pages 30-33)
6. **Nonresponsive disease:** ongoing exposure, delayed recovery, or another condition must be distinguished from true refractoriness.
7. **RCD I or clonal RCD II:** type II may progress to EATL.

Reversibility is greatest for inflammatory/nutritional abnormalities and less reliable for established dental enamel injury, advanced skeletal injury, some neurologic/ENT deficits, and clonal RCD II. Bone density often improves partially by one year and can continue for several years, but late-onset disease may not normalize fully. (santonicola2024associationsbetweenceliac pages 7-9)

## Animal models

- **HLA-DQ8 or HLA-DQ2 transgenic mice:** reproduce human HLA-restricted gluten antigen recognition and permit study of gluten-specific T cells. Most do **not spontaneously reproduce the complete human enteropathy**, autoantibody profile, and chronic natural history.
- **NOD Aβ0 DQ8 mice:** combine autoimmune-prone background with human DQ8 and can model gluten-dependent immune responses and microbiome effects. They incompletely reproduce severe spontaneous villous atrophy and the full human clinical spectrum.
- **Gliadin sensitization/challenge models and inflammatory mouse models:** can reproduce epithelial inflammation, oxidative stress, cytokine responses, or vascular dysfunction, but their induced nature limits inference about spontaneous human disease.

Accordingly, there is no single animal model that simultaneously reproduces HLA dependence, oral-gluten loss of tolerance, autoantibodies, chronic enteropathy, extraintestinal disease, and refractory clonal evolution. The retrieved literature itself notes that conventional systems cannot fully recapitulate this multifactorial disease. (ramirezsanchez2020molecularbiomarkersfor pages 1-3)

## Non-animal experimental models

- **Patient-derived intestinal organoids:** preserve donor epithelial genotype and model epithelial differentiation, barrier responses, and epithelial cytokine programs. Conventional epithelial-only organoids omit adaptive immune cells, vasculature, luminal flow, systemic metabolism, and a stable microbiome.
- **Syngeneic autoimmune organoid model (Nature, 2024):** combines patient small-intestinal epithelium with relevant immune components and identified an IL-7-dependent epithelial–immune interaction. It improves modeling of antigen-specific autoimmunity but remains reductionist and lacks whole-organ physiology and long-term systemic disease. DOI: [10.1038/s41586-024-07716-2](https://doi.org/10.1038/s41586-024-07716-2), July 2024.
- **hiPSC intestine-on-chip / barrier-on-chip:** can incorporate donor genetic risk, multiple cell types, flow, gluten, and potentially microbiota. The 2019 review says such systems can “integrate the genetic background of complex diseases, the different interacting cell types involved in disease pathology, and the modulating environmental factors such as gluten and the gut microbiome.” They still omit complete systemic immunity, neuroendocrine inputs, pharmacokinetics, and years-long disease evolution. DOI: [10.1177/2050640619836057](https://doi.org/10.1177/2050640619836057), May 2019.
- **Primary PBMC/T-cell systems:** ELISpot, cytokine-release assays, and HLA-DQ:gluten tetramers capture gluten-specific circulating T-cell responses but omit tissue architecture and epithelial injury. (ramirezsanchez2020molecularbiomarkersfor pages 1-3)

## Interventional trials of disease-modifying therapy

- **ZED1227, oral TG2 inhibitor:** Phase 2, 163 participants, six-week 3-g/day gluten challenge. Doses of 10, 50, and 100 mg produced dose-dependent preservation of villous-height:crypt-depth ratio and reduced IEL density versus placebo. This is a positive proof-of-concept result, not an approval. (massironi2024beyondtheglutenfree pages 9-10)
- **Latiglutenase/IMGX003, gluten-degrading enzymes:** completed Phase 2 studies include **NCT01255696, NCT00959114, and NCT03585478**; **NCT04243551** was active-not-recruiting as of December 2023. Histologic and symptom outcomes have varied; no definitive disease-modifying benefit is established. (massironi2024beyondtheglutenfree pages 4-5, buiten2021gliadinsequestrationas pages 9-10)
- **Larazotide acetate, barrier-directed peptide:** completed Phase 2 trials include **NCT00492960, NCT00362856, NCT01396213, NCT00620451, and NCT00889473**. Phase 3 **NCT03569007** used abdominal-domain patient-reported outcomes. The retrieved evidence does not establish confirmatory Phase 3 benefit. (massironi2024beyondtheglutenfree pages 9-10, buiten2021gliadinsequestrationas pages 8-9, buiten2021gliadinsequestrationas pages 10-12)
- **TAK-101, antigen-loaded tolerogenic nanoparticles:** Phase 2 programs **NCT03486990** and **NCT03738475** were reported as completed; **NCT04530123** evaluates immunologic and clinical responses. Early studies found acceptable safety and attenuation of gluten-challenge immune responses without generalized immunosuppression; clinical efficacy remains unconfirmed. (kowalski2024celiacdisease—newinsights pages 8-9, buiten2021gliadinsequestrationas pages 8-9)
- **KAN-101, liver-targeted antigen-specific tolerance:** first-in-human **NCT04248855**; Phase 1/2 **NCT05574010** was terminated; Phase 2 **NCT06001177** completed with 55 participants. Early pharmacodynamic data suggest blunting of gliadin-specific inflammation, but definitive clinical efficacy was not reported in the retrieved evidence. (kowalski2024celiacdisease—newinsights pages 8-9, buiten2021gliadinsequestrationas pages 8-9)
- **Nexvax2 peptide immunotherapy:** Phase 2 **NCT03644069** was discontinued after interim analysis because it did not significantly protect against gluten-induced symptoms. This is a negative efficacy result despite earlier immunologic signals. (buiten2021gliadinsequestrationas pages 6-8, crepaldi2023emergingpharmaceuticaltherapies pages 10-11, buiten2021gliadinsequestrationas pages 10-12)
- **Anti-IL-15:** AMG714 **NCT02633020** did not prevent mucosal injury versus placebo, although the 300-mg arm showed smaller IEL increases and fewer symptoms. PRV-015 **NCT04424927** is a Phase 2 program; Hu-Mik-β-1 **NCT01893775** completed Phase 1 in five participants. (buiten2021gliadinsequestrationas pages 6-8, crepaldi2023emergingpharmaceuticaltherapies pages 10-11)
- **Hookworm, Necator americanus:** **NCT02754609**, Phase 1b; very small studies reported some tolerance/histologic signals. This remains experimental and is not evidence for routine helminth therapy. (buiten2021gliadinsequestrationas pages 6-8, buiten2021gliadinsequestrationas pages 10-12)
- **Teriflunomide:** **NCT04806737**, Phase 1/2, completed, 15 participants. No primary result was available in the retrieved evidence.
- **Amlitelimab:** **NCT06557772**, Phase 2a/b, active-not-recruiting, planned enrollment 229 adults with nonresponsive disease. No result was available.

## Comorbid conditions above background

The strongest missing comorbid category is **autoimmune clustering**. Hashimoto thyroiditis, type 1 diabetes, Sjögren syndrome, psoriasis, rheumatoid inflammatory disease, autoimmune liver disease, vitiligo, and Addison disease recur across cohorts. A 2024 tertiary series found Hashimoto thyroiditis in 14.81%, lupus in 11.11%, rheumatoid polyarthritis in 8.33%, Sjögren syndrome and psoriasis in 7.41% each, and type 1 diabetes in 1.85%; these are single-center proportions, not population effect sizes. (pop2024extradigestivemanifestationsof pages 2-4)

The reverse-direction Swedish evidence is quantitatively strong: among young people with type 1 diabetes, the hazard ratio for subsequently recorded celiac disease was 11.6 (95% CI 10.6–12.6) versus controls. That estimate establishes clustering but is not directly the risk of diabetes among celiac patients. Shared HLA and broader immune-regulatory susceptibility are plausible explanations, but disease pairs differ in how much of their association is attributable to HLA versus non-HLA loci and surveillance. No uniform “shared genetics” explanation should be assigned to every comorbidity.

Asthma, depression, anxiety, and cardiovascular disease are better labeled **associated comorbidities** unless a study specifically demonstrates a gluten-dependent phenotype. (pop2024extradigestivemanifestationsof pages 2-4, pop2024extradigestivemanifestationsof pages 4-5)

## Biomarkers and laboratory monitoring beyond recorded antibodies

- **Fecal or urinary gluten-immunogenic peptides (GIP):** directly detect recent gluten exposure and can reveal dietary transgression missed by symptoms or serology. Detection windows and cutoffs are assay- and specimen-specific; there is **no universal standardized reference interval**. (bragde2019biomarkersofinflammation pages 30-33)
- **Plasma intestinal fatty-acid-binding protein (I-FABP/FABP2):** marker of enterocyte injury. In 138 children, newly diagnosed celiac disease had median 2,104 pg/mL (Q1–Q3 1,493–2,457) versus 938 pg/mL (616–1,140) in controls; it fell to 1,238 pg/mL (952–1,618) by six months of diet. These study distributions are not standardized clinical reference intervals. The abstract concludes: “Plasma, but not urinary iFABP is a candidate biomarker with better fidelity in monitoring compliance during GFD than TGA.” DOI: [10.1186/s12876-022-02334-6](https://doi.org/10.1186/s12876-022-02334-6), May 2022. (bragde2019biomarkersofinflammation pages 33-37)
- **Whole-blood gliadin-stimulated IL-2 release:** in a small study, 92% sensitivity and 100% specificity for treated HLA-DQ2.5-positive disease; estimated responsive-cell frequency was 0.5–11 cells/mL. This remains a research assay without a standardized population reference interval. The abstract states: “Whole blood IL-2 release assay using electrochemiluminescence is a sensitive test for rare gliadin-specific T cells in CD, and could aid in monitoring and diagnosis.” DOI: [10.1111/cei.13578](https://doi.org/10.1111/cei.13578), 2021. (ramirezsanchez2020molecularbiomarkersfor pages 1-3)
- **HLA-DQ:gluten tetramers, IFN-γ ELISpot, and related T-cell assays:** useful research endpoints after gluten challenge and in therapeutic trials; not standardized routine monitoring tests. (ramirezsanchez2020molecularbiomarkersfor pages 1-3)
- **Plasma citrulline:** candidate marker of enterocyte mass; no validated celiac-specific reference interval.
- **Fecal calprotectin:** nonspecific intestinal inflammatory marker; it cannot establish celiac activity independently and has no celiac-specific reference interval. (bragde2019biomarkersofinflammation pages 30-33)
- **Circulating miRNAs:** 53 candidates differed between disease and controls; eight differed within one year before conventional seroconversion, and several normalized with treatment. These remain investigational and lack validated clinical cutoffs. (ramirezsanchez2020molecularbiomarkersfor pages 1-3)
- **Histologic quantitative endpoints:** villous-height:crypt-depth ratio, IEL density, and continuous digital pathology measures are increasingly used in trials. They may be more reproducible than ordinal Marsh categories but are not blood biomarkers.
- **Nutritional and safety monitoring:** CBC, ferritin/iron indices, folate, B12, calcium, phosphate, alkaline phosphatase, vitamin D, albumin/total protein, and liver tests assess consequences rather than disease-specific immune activity. Laboratory-specific reference intervals apply; there are no celiac-specific normal ranges.

## Overall curation recommendation

The clearest additions to a structured celiac-disease account are osteopenia, arthralgia, B12/folate-deficiency anemia, hypoproteinemia, selected oral findings, adverse pregnancy outcomes specifically linked to untreated disease, formal Marsh–Oberhuber and Corazza–Villanacci grading, clinical/potential/silent/seronegative/nonresponsive forms, RCD types I and II, experimental models, trial programs, and modern exposure/injury biomarkers. Autoimmune thyroiditis, psoriasis, asthma, depression, anxiety, and most cardiovascular findings should be stored as **comorbid associations**, not intrinsic manifestations. Rare ophthalmic, hepatic, renal, and dermatologic reports lacking denominator-based primary evidence should remain uncurated candidates rather than being inflated into established disease features.

References

1. (pop2024extradigestivemanifestationsof pages 2-4): Andrei-Vasile Pop, Stefan-Lucian Popa, and Dan L. Dumitrascu. Extra-digestive manifestations of celiac disease. Jul 2024. URL: https://doi.org/10.15386/mpr-2776, doi:10.15386/mpr-2776. This article has 7 citations.

2. (santonicola2024associationsbetweenceliac pages 7-9): Antonella Santonicola, Herbert Wieser, Carolina Gizzi, Carlo Soldaini, and Carolina Ciacci. Associations between celiac disease, extra-gastrointestinal manifestations, and gluten-free diet: a narrative overview. Jun 2024. URL: https://doi.org/10.3390/nu16121814, doi:10.3390/nu16121814. This article has 36 citations.

3. (pop2024extradigestivemanifestationsof pages 1-2): Andrei-Vasile Pop, Stefan-Lucian Popa, and Dan L. Dumitrascu. Extra-digestive manifestations of celiac disease. Jul 2024. URL: https://doi.org/10.15386/mpr-2776, doi:10.15386/mpr-2776. This article has 7 citations.

4. (lupu2024celiacdisease pages 7-8): Vasile Valeriu Lupu, Maria Oana Sasaran, Elena Jechel, Iuliana Magdalena Starcea, Ileana Ioniuc, Adriana Mocanu, Solange Tamara Rosu, Valentin Munteanu, Alin Horatiu Nedelcu, Ciprian Danielescu, Delia Lidia Salaru, Anton Knieling, and Ancuta Lupu. Celiac disease - a pluripathological model in pediatric practice. Frontiers in Immunology, Apr 2024. URL: https://doi.org/10.3389/fimmu.2024.1390755, doi:10.3389/fimmu.2024.1390755. This article has 25 citations and is from a peer-reviewed journal.

5. (lupu2024celiacdisease pages 8-8): Vasile Valeriu Lupu, Maria Oana Sasaran, Elena Jechel, Iuliana Magdalena Starcea, Ileana Ioniuc, Adriana Mocanu, Solange Tamara Rosu, Valentin Munteanu, Alin Horatiu Nedelcu, Ciprian Danielescu, Delia Lidia Salaru, Anton Knieling, and Ancuta Lupu. Celiac disease - a pluripathological model in pediatric practice. Frontiers in Immunology, Apr 2024. URL: https://doi.org/10.3389/fimmu.2024.1390755, doi:10.3389/fimmu.2024.1390755. This article has 25 citations and is from a peer-reviewed journal.

6. (santonicola2024associationsbetweenceliac pages 2-4): Antonella Santonicola, Herbert Wieser, Carolina Gizzi, Carlo Soldaini, and Carolina Ciacci. Associations between celiac disease, extra-gastrointestinal manifestations, and gluten-free diet: a narrative overview. Jun 2024. URL: https://doi.org/10.3390/nu16121814, doi:10.3390/nu16121814. This article has 36 citations.

7. (santonicola2024associationsbetweenceliac pages 13-14): Antonella Santonicola, Herbert Wieser, Carolina Gizzi, Carlo Soldaini, and Carolina Ciacci. Associations between celiac disease, extra-gastrointestinal manifestations, and gluten-free diet: a narrative overview. Jun 2024. URL: https://doi.org/10.3390/nu16121814, doi:10.3390/nu16121814. This article has 36 citations.

8. (villanacci2020celiacdiseasehistologydifferential pages 7-9): Vincenzo Villanacci, Alessandro Vanoli, Giuseppe Leoncini, Giovanni Arpa, Tiziana Salviato, Luca Reggiani Bonetti, Carla Baronchelli, Luca Saragoni, and Paola Parente. Celiac disease: histology-differential diagnosis-complications.a practical approach. Pathologica, 112:186-196, Sep 2020. URL: https://doi.org/10.32074/1591-951x-157, doi:10.32074/1591-951x-157. This article has 111 citations.

9. (massironi2024beyondtheglutenfree pages 9-10): Sara Massironi, Marianna Franchina, Alessandra Elvevi, and Donatella Barisani. Beyond the gluten-free diet: innovations in celiac disease therapeutics. World Journal of Gastroenterology, 30:4194-4210, Oct 2024. URL: https://doi.org/10.3748/wjg.v30.i38.4194, doi:10.3748/wjg.v30.i38.4194. This article has 26 citations.

10. (kowalski2024celiacdisease—newinsights pages 8-9): Marek Kowalski, Danuta Domżał-Magrowska, and Ewa Izabela Malecka-Wojciesko. Celiac disease—new insights in pathogenesis, diagnosis and management. Unknown journal, Nov 2024. URL: https://doi.org/10.20944/preprints202411.0943.v1, doi:10.20944/preprints202411.0943.v1.

11. (buiten2021gliadinsequestrationas pages 8-9): Charlene B. Van Buiten and Ryan J. Elias. Gliadin sequestration as a novel therapy for celiac disease: a prospective application for polyphenols. International Journal of Molecular Sciences, 22:595, Jan 2021. URL: https://doi.org/10.3390/ijms22020595, doi:10.3390/ijms22020595. This article has 42 citations.

12. (massironi2024beyondtheglutenfree pages 4-5): Sara Massironi, Marianna Franchina, Alessandra Elvevi, and Donatella Barisani. Beyond the gluten-free diet: innovations in celiac disease therapeutics. World Journal of Gastroenterology, 30:4194-4210, Oct 2024. URL: https://doi.org/10.3748/wjg.v30.i38.4194, doi:10.3748/wjg.v30.i38.4194. This article has 26 citations.

13. (buiten2021gliadinsequestrationas pages 9-10): Charlene B. Van Buiten and Ryan J. Elias. Gliadin sequestration as a novel therapy for celiac disease: a prospective application for polyphenols. International Journal of Molecular Sciences, 22:595, Jan 2021. URL: https://doi.org/10.3390/ijms22020595, doi:10.3390/ijms22020595. This article has 42 citations.

14. (buiten2021gliadinsequestrationas pages 10-12): Charlene B. Van Buiten and Ryan J. Elias. Gliadin sequestration as a novel therapy for celiac disease: a prospective application for polyphenols. International Journal of Molecular Sciences, 22:595, Jan 2021. URL: https://doi.org/10.3390/ijms22020595, doi:10.3390/ijms22020595. This article has 42 citations.

15. (buiten2021gliadinsequestrationas pages 6-8): Charlene B. Van Buiten and Ryan J. Elias. Gliadin sequestration as a novel therapy for celiac disease: a prospective application for polyphenols. International Journal of Molecular Sciences, 22:595, Jan 2021. URL: https://doi.org/10.3390/ijms22020595, doi:10.3390/ijms22020595. This article has 42 citations.

16. (crepaldi2023emergingpharmaceuticaltherapies pages 10-11): Martina Crepaldi, Michela Palo, Daria Maniero, Luisa Bertin, Edoardo Vincenzo Savarino, Robert P. Anderson, and Fabiana Zingone. Emerging pharmaceutical therapies to address the inadequacy of a gluten-free diet for celiac disease. Pharmaceuticals, 17:4, Dec 2023. URL: https://doi.org/10.3390/ph17010004, doi:10.3390/ph17010004. This article has 15 citations.

17. (pop2024extradigestivemanifestationsof pages 4-5): Andrei-Vasile Pop, Stefan-Lucian Popa, and Dan L. Dumitrascu. Extra-digestive manifestations of celiac disease. Jul 2024. URL: https://doi.org/10.15386/mpr-2776, doi:10.15386/mpr-2776. This article has 7 citations.

18. (kowalski2024celiacdisease—newinsights pages 5-6): Marek Kowalski, Danuta Domżał-Magrowska, and Ewa Izabela Malecka-Wojciesko. Celiac disease—new insights in pathogenesis, diagnosis and management. Unknown journal, Nov 2024. URL: https://doi.org/10.20944/preprints202411.0943.v1, doi:10.20944/preprints202411.0943.v1.

19. (verma2019identificationofa pages 32-37): AK Verma. Identification of a new biomarker for celiac disease and other gluten-related disorders. Unknown journal, 2019.

20. (ramirezsanchez2020molecularbiomarkersfor pages 1-3): Aarón D. Ramírez-Sánchez, Ineke L. Tan, B.C. Gonera-de Jong, Marijn C. Visschedijk, Iris Jonkers, and Sebo Withoff. Molecular biomarkers for celiac disease: past, present and future. International Journal of Molecular Sciences, 21:8528, Nov 2020. URL: https://doi.org/10.3390/ijms21228528, doi:10.3390/ijms21228528. This article has 53 citations.

21. (bragde2019biomarkersofinflammation pages 30-33): Hanna Gustafsson Bragde. Biomarkers of inflammation and intestinal mucosa pathology in celiac disease. Linköping University Medical Dissertations, Apr 2019. URL: https://doi.org/10.3384/diss.diva-156088, doi:10.3384/diss.diva-156088. This article has 0 citations.

22. (bragde2019biomarkersofinflammation pages 33-37): Hanna Gustafsson Bragde. Biomarkers of inflammation and intestinal mucosa pathology in celiac disease. Linköping University Medical Dissertations, Apr 2019. URL: https://doi.org/10.3384/diss.diva-156088, doi:10.3384/diss.diva-156088. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Celiac_Disease-coverage-gap-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005130` (2 mentions) - the report calls it "if available"; MONDO calls it **celiac disease**