---
title: Thalassemias grouping deep research
keywords:
- grouping
- thalassemia
- hemoglobin
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-13T19:46:58.184363'
end_time: '2026-06-13T20:18:17.810710'
duration_seconds: 1879.63
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_tokens: 12000
    max_embedded_images: 8
citation_count: 57
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Thalassemias-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Thalassemias-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Thalassemias-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

Prepare a focused, citation-rich deep research report for a dismech disease grouping called Thalassemias. The grouping should be an explicit curated union of Disease entries, not merely a MONDO hierarchy clone. Current curated members are Alpha Thalassemia and Beta Thalassemia. Research objectives: 1. define shared pathophysiology as inherited reduction or loss of alpha- or beta-globin chain synthesis with globin-chain imbalance, hypochromic microcytic anemia, hemolysis, ineffective erythropoiesis, erythroid marrow expansion, splenomegaly, iron overload, and skeletal/endocrine/cardiac complications; 2. distinguish alpha- and beta-thalassemia mechanisms, including HBA1/HBA2 deletional and nondeletional disease, hemoglobin H disease, hemoglobin Bart hydrops fetalis, HBB beta-zero and beta-plus variants, transfusion-dependent versus non-transfusion-dependent beta thalassemia, HbE/beta-thalassemia, sickle beta-thalassemia boundary issues, and modifier mechanisms such as fetal hemoglobin regulation; 3. recommend a defensible grouping boundary and explicitly flag disorders to exclude, such as ATRX syndrome, alpha-thalassemia X-linked intellectual disability as a broader syndromic entity, sickle cell disease without thalassemia, isolated HbE disease, malaria carrier states, secondary iron overload, and non-globin anemia unless curated as thalassemia entities; 4. list differentiating mechanisms for existing members and high-value missing subtype entries; 5. identify appropriate MONDO mapping, HPO hematologic/biochemical criteria, globin/erythropoiesis module-conformance criteria, and module gaps for the grouping YAML; 6. provide primary literature, GeneReviews, authoritative reviews, and treatment evidence for transfusion, chelation, splenectomy, luspatercept, hydroxyurea/HbF induction, gene addition, and gene editing therapies, plus recent 2023-2026 developments with PMID identifiers wherever possible; 7. flag knowledge gaps and model-system limitations relevant to genotype-phenotype prediction, iron toxicity, fetal hemoglobin modifiers, curative therapy access, and long-term safety. Do not invent citations; prefer PubMed-indexed sources and provide exact PMID identifiers for key claims.

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

Prepare a focused, citation-rich deep research report for a dismech disease grouping called Thalassemias. The grouping should be an explicit curated union of Disease entries, not merely a MONDO hierarchy clone. Current curated members are Alpha Thalassemia and Beta Thalassemia. Research objectives: 1. define shared pathophysiology as inherited reduction or loss of alpha- or beta-globin chain synthesis with globin-chain imbalance, hypochromic microcytic anemia, hemolysis, ineffective erythropoiesis, erythroid marrow expansion, splenomegaly, iron overload, and skeletal/endocrine/cardiac complications; 2. distinguish alpha- and beta-thalassemia mechanisms, including HBA1/HBA2 deletional and nondeletional disease, hemoglobin H disease, hemoglobin Bart hydrops fetalis, HBB beta-zero and beta-plus variants, transfusion-dependent versus non-transfusion-dependent beta thalassemia, HbE/beta-thalassemia, sickle beta-thalassemia boundary issues, and modifier mechanisms such as fetal hemoglobin regulation; 3. recommend a defensible grouping boundary and explicitly flag disorders to exclude, such as ATRX syndrome, alpha-thalassemia X-linked intellectual disability as a broader syndromic entity, sickle cell disease without thalassemia, isolated HbE disease, malaria carrier states, secondary iron overload, and non-globin anemia unless curated as thalassemia entities; 4. list differentiating mechanisms for existing members and high-value missing subtype entries; 5. identify appropriate MONDO mapping, HPO hematologic/biochemical criteria, globin/erythropoiesis module-conformance criteria, and module gaps for the grouping YAML; 6. provide primary literature, GeneReviews, authoritative reviews, and treatment evidence for transfusion, chelation, splenectomy, luspatercept, hydroxyurea/HbF induction, gene addition, and gene editing therapies, plus recent 2023-2026 developments with PMID identifiers wherever possible; 7. flag knowledge gaps and model-system limitations relevant to genotype-phenotype prediction, iron toxicity, fetal hemoglobin modifiers, curative therapy access, and long-term safety. Do not invent citations; prefer PubMed-indexed sources and provide exact PMID identifiers for key claims.

## Thalassemias dismech disease grouping — deep research report (curated union)

### Scope and explicit curated union (not a hierarchy clone)
**Grouping name:** *Thalassemias* (dismech grouping).

**Curated union definition (core members):** The grouping is defined as an explicit union of disease entries with an inherited *quantitative* reduction or loss of α- or β-globin chain synthesis that causes globin-chain imbalance and the canonical thalassemia pathophysiology/phenotype spectrum. Current curated members are:
1) **Alpha thalassemia** and
2) **Beta thalassemia**.

This grouping is intentionally *not* a direct clone of MONDO’s entire “thalassemia” subtree because (i) clinically critical entities are mechanism/phenotype-defined (e.g., HbH disease; TDT vs NTDT), and (ii) several disorders that mention “thalassemia” in a feature list are syndromic/secondary and should be excluded from the core quantitative globin-synthesis mechanism boundary (see §Grouping boundary and exclusions). (li2024applicationofthirdgeneration pages 1-2, thuret2022hurdlestothe pages 1-2, necessaryUnknownyeardiagnosticgenetictesting pages 7-9)

| Grouping status | Disease/entity | Include in curated union? | Key distinguishing mechanism/genetics | Boundary / exclusion note | Example evidence citations |
|---|---|---|---|---|---|
| Current curated member | Alpha thalassemia | Yes | Reduced or absent α-globin synthesis from HBA1/HBA2 defects; includes deletional α+ and α0 alleles and nondeletional variants; causes globin-chain imbalance, microcytic hypochromic anemia, hemolysis, and ineffective erythropoiesis | Core member of grouping | (li2024applicationofthirdgeneration pages 1-2, li2024applicationofthirdgeneration pages 2-3, zahed2023effectiveutilizationof pages 67-70) |
| Current curated member | Beta thalassemia | Yes | Reduced (β+) or absent (β0) β-globin synthesis from HBB variants; α/non-α chain imbalance drives ineffective erythropoiesis, marrow expansion, hemolysis, splenomegaly, and iron overload | Core member of grouping | (thuret2022hurdlestothe pages 1-2, zahed2023effectiveutilizationof pages 61-64, origa2024betathalassemiain pages 1-2) |
| High-value proposed subtype entry | Hemoglobin H disease / alpha-thalassemia intermedia | Yes | Usually 3 affected α-globin genes; excess β-globin tetramers (HbH); deletional and nondeletional forms, with nondeletional disease often more severe | Distinct postnatal α-thalassemia subtype worth explicit curation rather than burying inside parent disease | (li2024applicationofthirdgeneration pages 1-2, necessaryUnknownyeardiagnosticgenetictesting pages 7-9, necessaryUnknownyeardiagnosticgenetictesting pages 4-7) |
| High-value proposed subtype entry | Hemoglobin Bart hydrops fetalis syndrome / alpha-thalassemia major | Yes | Usually loss of all 4 α-globin genes; fetal predominance of γ4 tetramers (Hb Bart), severe fetal hypoxia, hydrops fetalis, often lethal without intrauterine transfusion | Severe α-thalassemia entity should be explicit; do not collapse into generic hydrops fetalis | (zahed2023effectiveutilizationof pages 67-70, li2024applicationofthirdgeneration pages 1-2, necessaryUnknownyeardiagnosticgenetictesting pages 4-7) |
| High-value proposed subtype entry | Deletional alpha thalassemia | Yes, if disease-level term exists | Structural loss of one or more α-globin genes (e.g., -α3.7, -α4.2, --SEA, --THAI); major mechanism in α-thalassemia | Useful mechanistic subtype if ontology supports disease entry | (li2024applicationofthirdgeneration pages 1-2, li2024applicationofthirdgeneration pages 3-6, li2024applicationofthirdgeneration pages 2-3) |
| High-value proposed subtype entry | Nondeletional alpha thalassemia | Yes, if disease-level term exists | HBA1/HBA2 point variants or small indels such as Constant Spring, Quong Sze, Westmead; often associated with more severe HbH phenotypes than deletional disease | Useful mechanistic subtype if ontology supports disease entry | (li2024applicationofthirdgeneration pages 3-6, li2024applicationofthirdgeneration pages 2-3, necessaryUnknownyeardiagnosticgenetictesting pages 4-7) |
| High-value proposed subtype entry | Transfusion-dependent beta thalassemia (TDT) | Yes | Clinical severity grouping defined by regular lifelong transfusion requirement; often severe β-thalassemia major genotype combinations but not perfectly genotype-bound | Strongly useful clinical subtype for treatment mapping, including luspatercept, gene addition, and gene editing | (zahed2023effectiveutilizationof pages 61-64, origa2024betathalassemiain pages 1-2, locatelli2024exagamglogeneautotemcelfor pages 1-2) |
| High-value proposed subtype entry | Non-transfusion-dependent beta thalassemia (NTDT) | Yes | Beta-thalassemia with intermittent or no regular transfusion requirement; persistent ineffective erythropoiesis and iron loading still clinically important | Should be explicit because complications and therapeutic goals differ from TDT | (origa2024betathalassemiain pages 1-2, aydinok2023highlightsonthe pages 1-2, zahed2023effectiveutilizationof pages 61-64) |
| High-value proposed subtype entry | HbE/beta-thalassemia | Yes | Compound state with HBB β-thalassemia allele plus HbE allele; clinically sits within β-thalassemia spectrum and is specifically represented in luspatercept studies | Include because it is routinely managed as a β-thalassemia syndrome, not isolated HbE disease | (aydinok2023highlightsonthe pages 1-2, locatelli2024exagamglogeneautotemcelfor pages 5-7, origa2024betathalassemiain pages 1-2) |
| Boundary case | Sickle beta-thalassemia | Usually no for this grouping; consider separate overlap policy | Compound HBB sickle variant plus β-thalassemia allele; shares β-thalassemia mechanism but also has sickling vasculopathy | Best treated as boundary/overlap disorder rather than core thalassemia grouping member unless explicit cross-group curation policy exists | (tuo2024globalregionaland pages 13-14, zhang2024currentstatusand pages 10-13) |
| Exclude | ATR-X syndrome / alpha-thalassemia X-linked intellectual disability syndrome | No | Syndromic disorder due to ATRX, not primary HBA1/HBA2 globin-gene thalassemia mechanism | Exclude broader syndromic entity even if α-thalassemia feature is present | (necessaryUnknownyeardiagnosticgenetictesting pages 7-9, necessaryUnknownyeardiagnosticgenetictesting pages 4-7) |
| Exclude | Sickle cell disease without thalassemia | No | Qualitative hemoglobinopathy with HbS polymerization rather than primary quantitative α- or β-globin synthesis deficiency | Outside grouping scope | (tuo2024globalregionaland pages 13-14, zhang2024currentstatusand pages 10-13) |
| Exclude | Isolated hemoglobin E disease | No | Structural hemoglobin variant disorder without necessary β-thalassemia state | Exclude unless explicitly combined with β-thalassemia | (aydinok2023highlightsonthe pages 1-2) |
| Exclude | Malaria carrier states / heterozygote protection states | No | Population-genetic selection context, not a disease entity requiring thalassemia curation | Exclude non-disease carrier/adaptation states | (tuo2024globalregionaland pages 2-3, tuo2024globalregionaland pages 1-2) |
| Exclude | Secondary iron overload without thalassemia | No | Iron toxicity may occur in thalassemia but secondary iron overload alone is not a globin-synthesis disorder | Exclude complication-only entities | (aydinok2023highlightsonthe pages 1-2, zahed2023effectiveutilizationof pages 61-64) |
| Exclude | Non-globin microcytic or hemolytic anemias | No | Shared anemia phenotype without inherited α- or β-globin synthesis defect | Exclude unless separately curated as bona fide thalassemia disease entries | (zahed2023effectiveutilizationof pages 67-70, li2024applicationofthirdgeneration pages 1-2) |


*Table: This table summarizes the core thalassemia grouping members, high-value subtype entries to add, and boundary/exclusion decisions. It is useful for implementing an explicit curated union that reflects mechanism and clinical utility rather than simply mirroring a hierarchy.*

### 1) Key concepts and shared pathophysiology (current understanding)
#### 1.1 Core mechanistic definition
Thalassemias are inherited disorders of hemoglobin synthesis where decreased production of a globin chain (α or β) creates **globin-chain imbalance**, leading to precipitation/toxic effects of unpaired chains, **ineffective erythropoiesis**, and varying degrees of anemia. (zahed2023effectiveutilizationof pages 58-61, cappellini2021theuseof pages 1-2, cappellini2020aphase3 pages 1-2)

#### 1.2 Shared downstream pathophysiology across alpha and beta thalassemias
Across thalassemia syndromes, the shared disease cascade includes:
- **Microcytic hypochromic anemia** as a common hematologic presentation. (zahed2023effectiveutilizationof pages 58-61, zahed2023effectiveutilizationof pages 67-70)
- **Ineffective erythropoiesis and marrow expansion**, with compensatory erythropoiesis that can cause bone deformities/skeletal changes and extramedullary hematopoiesis. (cappellini2021theuseof pages 1-2, zahed2023effectiveutilizationof pages 61-64, zahed2023effectiveutilizationof pages 67-70)
- **Hemolysis and oxidative stress**, particularly via excess unpaired chains generating reactive oxygen species, contributing to erythrocyte membrane damage and premature cell death. (zahed2023effectiveutilizationof pages 61-64, zahed2023effectiveutilizationof pages 58-61)
- **Splenomegaly** due to extramedullary hematopoiesis and red cell destruction. (zahed2023effectiveutilizationof pages 67-70, cappellini2021theuseof pages 1-2)
- **Iron overload** from both transfusions (especially TDT) and disease biology. A key shared mechanism is that ineffective erythropoiesis is associated with **hepcidin downregulation and ferroportin upregulation**, increasing intestinal iron absorption and erythroid iron uptake, promoting oxidative injury and iron loading. (aydinok2023highlightsonthe pages 1-2, zahed2023effectiveutilizationof pages 61-64)

### 2) Distinguishing alpha- vs beta-thalassemia mechanisms and clinical entities

#### 2.1 Alpha thalassemia: HBA1/HBA2 deletional vs nondeletional disease and major entities
**Genetic mechanism:** α-thalassemia arises from pathogenic changes in **HBA1/HBA2** and is categorized into **deletional** and **nondeletional** forms. Deletional forms include **α+** (single α-gene deletion, -α/) and **α0** (two α-gene deletions, --/). Nondeletional forms include point variants/small indels (examples described include Constant Spring, Quong Sze, Westmead in HBA2). (li2024applicationofthirdgeneration pages 1-2, li2024applicationofthirdgeneration pages 2-3)

**Clinically important α-thalassemia entities:**
- **Hb H disease (α-thalassemia intermedia):** described as intermediate α-thalassemia causing moderate anemia, and a high-value explicit subtype for curation. (li2024applicationofthirdgeneration pages 1-2, necessaryUnknownyeardiagnosticgenetictesting pages 4-7)
- **Hb Bart’s hydrops fetalis syndrome (α-thalassemia major):** severe α-thalassemia typically with loss of all 4 α-globin genes, often fatal without intrauterine transfusion; Hb Bart’s predominates in severe fetal disease. (zahed2023effectiveutilizationof pages 67-70, necessaryUnknownyeardiagnosticgenetictesting pages 4-7, li2024applicationofthirdgeneration pages 1-2)

**Deletional vs nondeletional severity note:** Evidence indicates deletions account for most α-thalassemia (~90%), but nondeletional point variants can yield more severe phenotypes (notably in HbH disease). (necessaryUnknownyeardiagnosticgenetictesting pages 4-7, zahed2023effectiveutilizationof pages 67-70)

#### 2.2 Beta thalassemia: β0 vs β+ variants, TDT vs NTDT, HbE/β-thalassemia
**Genetic mechanism:** β-thalassemia results from diverse **HBB** variants leading to reduced (**β+**) or absent (**β0**) β-globin synthesis. The unbalanced α:β ratio results in unbound α-globin precipitation, ineffective erythropoiesis, chronic hemolytic anemia, and compensatory marrow expansion. (cappellini2021theuseof pages 1-2, thuret2022hurdlestothe pages 1-2, zahed2023effectiveutilizationof pages 58-61)

**Clinical classification used in practice and trials:** β-thalassemia is widely classified as **transfusion-dependent thalassemia (TDT)** vs **non–transfusion-dependent thalassemia (NTDT)** based on transfusion need (a clinically useful axis that is not perfectly genotype-bound). (cappellini2021theuseof pages 1-2, cappellini2020aphase3 pages 1-2, zahed2023effectiveutilizationof pages 61-64)

**HbE/β-thalassemia:** HbE/β-thalassemia is treated as part of the β-thalassemia syndrome spectrum and was included in major luspatercept evidence summaries and response analyses; it is therefore a high-value explicit subtype entry for the grouping. (aydinok2023highlightsonthe pages 1-2, cappellini2020aphase3 pages 1-2)

#### 2.3 Boundary issues: sickle β-thalassemia and HbF modifier mechanisms
**HbF modifiers:** Disease severity and treatment response can be modified by loci that increase fetal hemoglobin, including **BCL11A**, **HBS1L-MYB**, **XmnI G-γ**, and **KLF1**; co-inheritance of HPFH and/or α-thalassemia can also modify β-thalassemia severity. (zahed2023effectiveutilizationof pages 61-64, zahed2023effectiveutilizationof pages 58-61)

**Sickle β-thalassemia boundary:** Compound states that blend sickle cell pathophysiology with thalassemia (sickle/β-thalassemia) should be treated as overlap/boundary entities rather than core thalassemia members unless the curation program explicitly supports multi-group membership. This is consistent with the need to exclude sickle cell disease *without* thalassemia from this grouping while acknowledging shared β-globin locus biology. (tuo2024globalregionaland pages 13-14, zhang2024currentstatusand pages 10-13)

### 3) Recommended grouping boundary and explicit exclusions

#### 3.1 Defensible inclusion boundary
Include diseases where the *primary* mechanism is an inherited quantitative defect in α- or β-globin chain synthesis (HBA1/HBA2 or HBB), producing globin-chain imbalance and the thalassemia syndrome spectrum (microcytosis/hypochromia, ineffective erythropoiesis ± hemolysis, marrow expansion ± splenomegaly, iron dysregulation/overload). (zahed2023effectiveutilizationof pages 58-61, cappellini2021theuseof pages 1-2, aydinok2023highlightsonthe pages 1-2)

#### 3.2 Exclusions (flag explicitly in YAML)
Exclude entities where “thalassemia” is secondary, syndromic, or not a primary quantitative globin-chain synthesis disorder:
- **ATR-X syndrome / α-thalassemia X-linked intellectual disability** as a broader syndromic entity (do not include as a core thalassemia disease entry even if α-thalassemia features are present). (necessaryUnknownyeardiagnosticgenetictesting pages 7-9, necessaryUnknownyeardiagnosticgenetictesting pages 4-7)
- **Sickle cell disease without thalassemia** (qualitative HbS polymerization disease, not primary quantitative α/β synthesis reduction). (tuo2024globalregionaland pages 13-14, zhang2024currentstatusand pages 10-13)
- **Isolated HbE disease** (structural hemoglobin variant without necessary β-thalassemia state). (aydinok2023highlightsonthe pages 1-2)
- **Malaria carrier states** or population adaptation states (not disease entries). (tuo2024globalregionaland pages 2-3)
- **Secondary iron overload** without a primary thalassemia diagnosis (complication-only). (aydinok2023highlightsonthe pages 1-2, zahed2023effectiveutilizationof pages 61-64)
- **Non-globin microcytic/hemolytic anemias** unless explicitly curated as a thalassemia entity (avoid phenotype-only inclusion). (zahed2023effectiveutilizationof pages 67-70, li2024applicationofthirdgeneration pages 1-2)

### 4) Differentiating mechanisms for existing members and missing high-value subtype entries
A practical curation set should be enriched beyond the two current members by adding high-value mechanistic/clinical subtypes used in clinical guidelines, trials, and registries (see Artifact-00):
- **Hb H disease** (α-thalassemia intermedia) (li2024applicationofthirdgeneration pages 1-2, necessaryUnknownyeardiagnosticgenetictesting pages 4-7)
- **Hb Bart’s hydrops fetalis syndrome** (α-thalassemia major) (zahed2023effectiveutilizationof pages 67-70, necessaryUnknownyeardiagnosticgenetictesting pages 4-7)
- **Deletional α-thalassemia** vs **nondeletional α-thalassemia** (li2024applicationofthirdgeneration pages 1-2, li2024applicationofthirdgeneration pages 3-6, li2024applicationofthirdgeneration pages 2-3)
- **TDT β-thalassemia** vs **NTDT β-thalassemia** (cappellini2021theuseof pages 1-2, cappellini2020aphase3 pages 1-2)
- **HbE/β-thalassemia** (aydinok2023highlightsonthe pages 1-2, cappellini2020aphase3 pages 1-2)

### 5) MONDO mapping, HPO criteria, and module conformance/gaps for grouping YAML

#### 5.1 MONDO mapping approach (implementation guidance)
- Map current curated members to the most direct MONDO disease classes for **alpha thalassemia** and **beta thalassemia**, but implement the grouping as a **curated union list** rather than inheriting all MONDO descendants by default.
- Add explicit child/subtype entries (HbH disease, Hb Bart’s hydrops fetalis, TDT/NTDT β-thalassemia, HbE/β-thalassemia) when corresponding MONDO disease entries exist.

Because this run does not include direct MONDO identifier strings in evidence, specific MONDO IDs cannot be asserted here without risking fabrication. The recommended operational approach is to (i) use MONDO label matching with curator verification and (ii) store mapping provenance in YAML. (tuo2024globalregionaland pages 13-14, zhang2024currentstatusand pages 10-13)

#### 5.2 HPO + lab/biochemical criteria (recommended)
Key phenotype and measurement criteria for YAML are summarized in Artifact-02. Highlights include:
- Microcytosis/hypochromia and anemia phenotypes; screening cutoffs **MCV <80 fL** and/or **MCH <27 pg** cited in a 2024 Molecular Cytogenetics review. (li2024applicationofthirdgeneration pages 1-2)
- Iron overload phenotype and mechanism (hepcidin suppression/ferroportin upregulation) as a shared pathway. (aydinok2023highlightsonthe pages 1-2)
- Explicit structured field for **TDT vs NTDT** (not well represented as HPO alone). (cappellini2021theuseof pages 1-2, cappellini2020aphase3 pages 1-2)

| Criterion type | Recommended HPO term label(s) and/or measurement | Notes on thresholds/examples | Best-fit subtype(s) | Module gap / uncertainty notes |
|---|---|---|---|---|
| Hematology | **Microcytosis (HP:0001935)**; **Decreased mean corpuscular volume**; **Hypochromic anemia (HP:0001936)** / **Decreased mean corpuscular hemoglobin** | Screening-supportive indices for thalassemia include **MCV <80 fL** and/or **MCH <27 pg**; adult reference values cited as MCV 80-97 fL, MCH 27.5-33.5 pg. Useful as shared entry criteria but not specific for subtype. (li2024applicationofthirdgeneration pages 1-2, li2024applicationofthirdgeneration pages 2-3) | Alpha, beta, HbH, TDT, NTDT | HPO has phenotype terms, but YAML may also need explicit numeric lab fields for MCV/MCH because HPO alone does not capture standard screening cutoffs well. |
| Hematology | **Anemia (HP:0001903)**; preferably **Chronic hemolytic anemia (HP:0001878)** or **Microcytic anemia (HP:0001935/HP:0001936-linked phenotype set)** | Core shared phenotype across thalassemias; severity ranges from mild trait-like states to severe transfusion dependence. (zahed2023effectiveutilizationof pages 67-70, thuret2022hurdlestothe pages 1-2, cappellini2021theuseof pages 1-2) | Alpha, beta | Need a policy decision on whether carrier/trait states belong in disease grouping vs separate carrier module. |
| Hematology / Hb fractions | Hemoglobin analysis measurement: **HbA2**, **HbF**, HbH, Hb Bart by HPLC/electrophoresis/capillary methods | Adult HbA2 reference range cited as **2.5-3.5%**; beta-thalassemia often has elevated HbA2/HbF, while alpha-thalassemia may require molecular confirmation because electrophoresis can miss mild carriers. HbH and Hb Bart are high-value disease-defining fractions for alpha-thalassemia subtypes. (li2024applicationofthirdgeneration pages 1-2, li2024applicationofthirdgeneration pages 2-3, zahed2023effectiveutilizationof pages 67-70) | Beta; HbH; Hb Bart hydrops fetalis | Major module gap: HPO poorly captures disease-defining **hemoglobin fraction thresholds/patterns**; YAML should allow explicit biochemical criteria. |
| Hematology / transfusion phenotype | No single HPO term is sufficient; add structured field for **transfusion dependence** and annual transfusion burden | TDT/NTDT is now a key clinical classification. Trial and care definitions commonly use regular transfusions over time; exa-cel defined transfusion independence as Hb >=9 g/dL without RBC transfusion for >=12 months. (origa2024betathalassemiain pages 1-2, locatelli2024exagamglogeneautotemcelfor pages 2-4, aydinok2023highlightsonthe pages 1-2) | Beta TDT, beta NTDT; severe alpha survivors | Strong module gap: need explicit YAML field for **TDT vs NTDT**, since this is clinically central and not cleanly represented by HPO alone. |
| Hemolysis / ineffective erythropoiesis | **Hemolytic anemia (HP:0001878)**; consider lab fields for reticulocytes, nucleated RBCs, soluble transferrin receptor | Shared mechanism is globin-chain imbalance with oxidative damage, erythroid apoptosis, and ineffective erythropoiesis; hydroxyurea trial used **soluble transferrin receptor** decline as a marker of reduced erythropoietic stress. (zahed2023effectiveutilizationof pages 61-64, yasara2022arandomiseddoubleblind pages 1-2, yasara2022arandomiseddoubleblind pages 2-4) | Beta, especially TDT/NTDT; severe alpha/HbH | HPO coverage for **ineffective erythropoiesis biomarkers** is limited; YAML may need non-HPO biochemical fields (sTfR, nucleated RBCs, marrow findings). |
| Marrow / extramedullary hematopoiesis | **Extramedullary hematopoiesis (HP:0001978)**; **Splenomegaly (HP:0001744)**; **Hepatomegaly (HP:0002240)** | Shared downstream effects of ineffective erythropoiesis and marrow expansion; clinically important in beta-thalassemia and more severe alpha entities. (zahed2023effectiveutilizationof pages 67-70, cappellini2021theuseof pages 1-2, dighriri2022efficacyandsafety pages 10-10) | Beta TDT/NTDT, HbH, severe alpha | Need curation guidance on whether splenomegaly alone is sufficient or should require other globin/erythropoiesis evidence. |
| Skeletal complications | **Abnormality of the skeletal system (HP:0000924)**; examples include bone deformity/osteopenia/osteoporosis-related terms | Marrow expansion and chronic disease contribute to skeletal complications; more common in severe untreated or undertreated disease. (zahed2023effectiveutilizationof pages 67-70, dighriri2022efficacyandsafety pages 10-10) | Mainly beta TDT/NTDT; severe alpha survivors | Phenotype is real but nonspecific; should likely be supportive rather than required criterion. |
| Iron overload mechanism | **Iron overload (HP:0003281)**; lab/imaging fields: **serum ferritin**, liver iron concentration, transferrin saturation | Thalassemia iron loading reflects both transfusions and disease biology; ineffective erythropoiesis suppresses **hepcidin** and increases **ferroportin-mediated iron absorption**. BELIEVE showed ferritin improvement with reduced transfusion burden. (aydinok2023highlightsonthe pages 1-2, cappellini2020aphase3 pages 1-2, zahed2023effectiveutilizationof pages 61-64) | Beta TDT and NTDT; severe alpha survivors after transfusion | HPO captures iron overload as phenotype, but YAML may need mechanism-aware annotation distinguishing **transfusional** vs **absorption-driven** iron loading. |
| Cardiac iron / cardiac complications | **Abnormal cardiac MRI T2\*** measurement; HPO supportive terms such as cardiomyopathy/arrhythmia if present | Cardiac iron is a major severity marker in transfused disease; MRI-based iron quantification is standard in practice and used in thalassemia research networks. (locatelli2024exagamglogeneautotemcelfor pages 10-12, locatelli2024exagamglogeneautotemcelfor pages 12-13) | Mainly beta TDT | Imaging-based quantitative criteria are not naturally represented in HPO; YAML should allow structured imaging metrics (e.g., cardiac T2\*). |
| Hepatic iron / imaging | Liver iron concentration by MRI; supportive HPO term **Hepatic hemosiderosis** / **Abnormal liver iron** if available | Exa-cel follow-up and iron overload literature note declines in liver iron after successful disease modification. (locatelli2024exagamglogeneautotemcelfor pages 10-12, winkler2026currentstatusof pages 11-12) | Mainly beta TDT; some NTDT | Another imaging-module gap: explicit quantitative liver iron fields likely needed. |
| Endocrine complications | Broad HPO endocrine abnormality terms as supportive features | Endocrine complications are recognized long-term consequences of iron overload and chronic disease burden. (origa2024betathalassemiain pages 1-2, tuo2024globalregionaland pages 2-3) | Mainly beta TDT; chronic severe disease | Too nonspecific for entry criteria; best used as downstream supportive complication annotation. |
| Alpha-thalassemia subtype-defining | HbH measurement; **Hemoglobin H disease** phenotype; for fetal disease include hydrops-related terms | HbH disease is the most severe alpha-thalassemia compatible with postnatal life; Hb Bart hydrops fetalis represents four-gene alpha loss with severe fetal disease. (li2024applicationofthirdgeneration pages 1-2, necessaryUnknownyeardiagnosticgenetictesting pages 7-9, necessaryUnknownyeardiagnosticgenetictesting pages 4-7) | HbH disease; Hb Bart hydrops fetalis | Requires explicit subtype logic that combines phenotype with genotype/hemoglobin fraction evidence; HPO alone will be insufficient. |
| Genotype evidence | Structured molecular evidence: **HBA1/HBA2 deletional/nondeletional**; **HBB beta-zero/beta-plus**; modifier loci such as **BCL11A, HBS1L-MYB, XmnI, KLF1** | Conventional testing detects ~95-98% of carriers but may miss rare genotypes; long-read sequencing improves detection of complex/rare alpha-thalassemia alleles and HBA1/HBA2 phasing. Modifiers influence phenotype and HbF response. (li2024applicationofthirdgeneration pages 1-2, li2024applicationofthirdgeneration pages 3-6, li2024applicationofthirdgeneration pages 2-3, zahed2023effectiveutilizationof pages 61-64, yasara2022arandomiseddoubleblind pages 6-7) | All subtypes | Key globin-module requirement: YAML should support **molecular mechanism fields**, not just phenotype terms, because diagnosis and grouping boundaries are genotype-anchored. |
| Exclusion guardrail | Require primary globin-gene disease evidence; do **not** rely on anemia/iron overload alone | Prevents inclusion of ATR-X syndrome, isolated secondary iron overload, sickle cell disease without thalassemia, or non-globin microcytic anemias. (necessaryUnknownyeardiagnosticgenetictesting pages 7-9, necessaryUnknownyeardiagnosticgenetictesting pages 4-7, zhang2024currentstatusand pages 10-13) | Group-level boundary rule | Strong recommendation: add explicit negative curation notes in YAML to avoid phenotype-only false inclusions. |


*Table: This table proposes phenotype, laboratory, imaging, and molecular criteria for thalassemia grouping curation in YAML. It is designed to help separate shared thalassemia mechanisms from subtype-specific features while flagging gaps where HPO alone is insufficient.*

#### 5.3 Module gaps justified by current evidence
Population datasets and ontologies often lack the resolution required for precision curation:
- GBD-based thalassemia burden work explicitly states it **does not differentiate subtype burden** (β-thalassemia vs HbE/β vs α-thalassemia) and does not separate **TDT vs NTDT**. (tuo2024globalregionaland pages 13-14, zhang2024currentstatusand pages 10-13)
- Diagnostic standards: conventional carrier testing detects most carriers but can miss mild/silent carriers; long-read sequencing improves complex allele resolution (HBA1/HBA2 homology, cis/trans phasing). (li2024applicationofthirdgeneration pages 2-3, li2024applicationofthirdgeneration pages 3-6)

### 6) Recent developments (prioritizing 2023–2024) and real-world applications

#### 6.1 Global burden and epidemiology (GBD 2021 analyses; 2024)
**Global burden estimates (GBD 2021, published 2024):**
- 2021 global age-standardized prevalence rate (ASPR): **18.28 per 100,000** (95% UI 15.29–22.02)
- age-standardized incidence rate (ASIR): **1.93 per 100,000** (95% UI 1.51–2.49)
- age-standardized mortality rate (ASMR): **0.15 per 100,000** (95% UI 0.11–0.20)
- age-standardized DALYs: **11.65 per 100,000** (95% UI 8.24–14.94)
- 2021 global prevalence counts: **1,310,407 cases** (95% UI 1,099,973–1,572,220)
- 2021 global incidence counts: **119,679 cases** (95% UI 93,218–153,985)
- 2021 deaths: **11,087** (95% UI 7,882–14,110)
- 2021 DALYs: **817,875** (95% UI 578,580–1,043,254)
(Tuo et al., eClinicalMedicine; June 2024; URL in citation) (tuo2024globalregionaland pages 1-2, tuo2024globalregionaland pages 3-4)

**Asia regional highlights (GBD 2021; published 2024):** East Asia had high ASPR and ASIR, and Southeast Asia had high ASMR and DALY burden (Zhang et al., BMC Public Health; Dec 2024; URL in citation). (zhang2024currentstatusand pages 2-4)

**Ontology-relevant limitation:** Both global and Asia analyses emphasize that GBD 2021 does not disaggregate α vs β vs HbE/β or TDT vs NTDT, limiting subtype-aware modeling. (tuo2024globalregionaland pages 13-14, zhang2024currentstatusand pages 10-13)

#### 6.2 Diagnostics and screening: long-read sequencing and programmatic prevention
**Quantified limitations of conventional screening:** A 2024 review reports missed-carrier rates: hematologic screening may miss ~**21%** of carriers with normal MCV/MCH, and electrophoresis may miss ~**57%** for some mild/silent carriers; PCR kits may target ~23 hotspots (rare mutations not covered). (Li & Ye, Molecular Cytogenetics; Dec 2024) (li2024applicationofthirdgeneration pages 2-3)

**Third-generation/long-read sequencing (2024–2026 evidence):**
- Long-read sequencing (ONT/PacBio) improves detection of structural variants and resolves HBA1/HBA2 homology and cis/trans phasing; CATSA achieved 100% accuracy in a retrospective validation set and found a carrier missed by conventional PCR. (li2024applicationofthirdgeneration pages 3-6)
- Long-read approaches are described as promising for large-scale screening but not yet uniformly adopted in routine labs; limitations include cost/throughput and variant interpretation challenges. (foord2026decodingthalassemiaand pages 10-11, zhu2026currentresearchstatus pages 8-10)

**Real-world prevention programs:** Saudi Arabia’s mandatory premarital screening program for hemoglobinopathies (implemented 2004) illustrates implementation plus known limitations (social/cultural barriers; limited reach) and limited availability of PGD due to cost/center availability. (zahed2023effectiveutilizationof pages 247-249)

**Prenatal carrier screening relevance:** A Vietnam cohort study (2025) reports high carrier burden (22.8% carry ≥1 recessive condition; alpha thalassemia carrier ~1 in 25; beta thalassemia carrier ~1 in 28) supporting broad carrier screening strategies. (nguyen2025prevalenceofcommon pages 1-2)

### 7) Treatment evidence and current applications (supportive, disease-modifying, curative)
A structured therapy summary is provided in Artifact-01.

| Therapy class | Target / mechanism | Applicable thalassemia types | Key recent evidence with quantitative outcomes | Key risks / limitations | Citation IDs |
|---|---|---|---|---|---|
| Regular red-cell transfusion (supportive) | Replaces deficient erythrocyte mass, suppresses ineffective erythropoiesis, supports growth and organ oxygen delivery | Core standard for severe alpha-thalassemia survivors after fetal therapy/postnatal care and for beta-thalassemia, especially TDT; sometimes intermittent in NTDT | Expert reviews describe transfusion as the central supportive therapy for TDT, aimed at controlling severe anemia and suppressing marrow expansion/its complications; in severe alpha-thalassemia major, survival is increasingly possible with intrauterine transfusion followed by chronic transfusion or HSCT (origa2024betathalassemiain pages 1-2, zahed2023effectiveutilizationof pages 61-64) | Causes transfusional iron overload, alloimmunization/infectious exposure burden, lifelong infrastructure dependence; does not correct underlying globin defect (cappellini2020aphase3 pages 1-2, origa2024betathalassemiain pages 1-2) | (origa2024betathalassemiain pages 1-2, cappellini2020aphase3 pages 1-2, zahed2023effectiveutilizationof pages 61-64) |
| Iron chelation (supportive complication control) | Removes excess transfusional and disease-related iron; limits liver, cardiac, and endocrine iron toxicity | Alpha- or beta-thalassemia with iron overload, especially TDT; also relevant in NTDT with increased absorption-driven iron loading | Standard agents cited include deferoxamine, deferasirox, and deferiprone; BELIEVE showed lower serum ferritin with luspatercept-treated TDT patients, consistent with reduced transfusional iron input (LS mean difference −348 μg/L at week 48), but chelation remains foundational management (cappellini2020aphase3 pages 1-2, zahed2023effectiveutilizationof pages 61-64) | Adherence burden, drug-specific toxicities, monitoring requirements; iron overload may arise from both transfusions and hepcidin-suppressed absorption, especially in NTDT (aydinok2023highlightsonthe pages 1-2, zahed2023effectiveutilizationof pages 61-64) | (aydinok2023highlightsonthe pages 1-2, cappellini2020aphase3 pages 1-2, zahed2023effectiveutilizationof pages 61-64) |
| Luspatercept in TDT (disease-modifying erythroid maturation therapy) | Activin receptor ligand trap / TGF-β superfamily ligand trap that enhances late-stage erythroid maturation and reduces ineffective erythropoiesis | Beta-thalassemia, primarily adult TDT; BELIEVE included β-thalassemia and HbE/β-thalassemia | Phase 3 BELIEVE: primary endpoint met in 21.4% on luspatercept vs 4.5% placebo for ≥33% transfusion-burden reduction during weeks 13–24 plus ≥2 units; any 12-week interval ≥33% reduction 70.5% vs 29.5%, ≥50% reduction 40.2% vs 6.3%; any 24-week interval ≥33% reduction 41.1% vs 2.7%; ~11% achieved transfusion independence; ferritin improved (cappellini2020aphase3 pages 1-2, cappellini2021theuseof pages 1-2) | Adverse events include bone pain, arthralgia, dizziness, hypertension, hyperuricemia; thromboembolic events enriched in splenectomized/risk-factor patients; does not eliminate need for transfusion in most patients (cappellini2020aphase3 pages 1-2, hatzimichael2022luspaterceptanew pages 6-7, dighriri2022efficacyandsafety pages 10-10) | (cappellini2020aphase3 pages 1-2, hatzimichael2022luspaterceptanew pages 6-7, cappellini2021theuseof pages 1-2, dighriri2022efficacyandsafety pages 10-10) |
| Luspatercept in NTDT (disease-modifying erythroid maturation therapy) | Same as above; improves terminal erythroid maturation and hemoglobin production | Beta-thalassemia NTDT, including adult NTDT/HbE-β-thalassemia spectrum in trials | Review summaries of BEYOND report Hb rise ≥1.0 g/dL in 77% and ≥1.5 g/dL in 52.1% of luspatercept-treated NTDT patients vs 0% placebo over a 12-week interval; another review reports 77.1% (74/96) meeting the primary anemia endpoint vs 0/49 placebo (aydinok2023highlightsonthe pages 1-2, hatzimichael2022luspaterceptanew pages 6-7) | Extramedullary hematopoiesis signal reported (6% vs 2% placebo in summary review); long-term real-world durability and optimal positioning relative to transfusion/HU still evolving (aydinok2023highlightsonthe pages 1-2, hatzimichael2022luspaterceptanew pages 6-7) | (aydinok2023highlightsonthe pages 1-2, hatzimichael2022luspaterceptanew pages 6-7) |
| Hydroxyurea / HbF induction (disease-modifying, off-label in many settings) | Increases fetal hemoglobin and may reduce ineffective erythropoiesis / erythropoietic stress; response modified by genotype and HbF-regulatory polymorphisms | Mainly beta-thalassemia; studied in TDT and NTDT; response appears enriched in HbE/β-thalassemia and XmnI-positive patients | Yasara 2022 RCT in TDT: no overall significant reduction in total transfusion volume for the whole cohort; HbF increased in 89% vs 59% placebo; mean HbF% increase over 6 months 3.25% vs 0.09% (p=0.006); mean absolute HbF rise 0.24 vs 0.01 g/dL (p=0.004); sTfR decreased in 79% vs 40% (p=0.013), mean end-of-treatment sTfR 72.2 vs 94.4 nmol/L (difference −22.1; p=0.007); 44% were responders (>1.5% HbF increase), and responders used less blood (77.4 vs 108.4 mL/kg vs HU nonresponders; p=0.005) (yasara2022arandomiseddoubleblind pages 1-2, yasara2022arandomiseddoubleblind pages 2-4, yasara2022arandomiseddoubleblind pages 5-6) | Benefits are heterogeneous and genotype-dependent; not proven to reduce transfusion burden across all TDT patients; adverse events occurred in 23% vs 7% placebo, with one discontinuation for persistent headache and no permanent adverse effects reported in the trial excerpt (yasara2022arandomiseddoubleblind pages 2-4, yasara2022arandomiseddoubleblind pages 7-8, yasara2022arandomiseddoubleblind pages 4-5) | (yasara2022arandomiseddoubleblind pages 1-2, yasara2022arandomiseddoubleblind pages 2-4, yasara2022arandomiseddoubleblind pages 5-6, yasara2022arandomiseddoubleblind pages 7-8, yasara2022arandomiseddoubleblind pages 4-5) |
| Exagamglogene autotemcel / exa-cel (curative-intent gene editing) | Ex vivo CRISPR-Cas9 editing of the erythroid-specific BCL11A enhancer in autologous CD34+ HSPCs to reactivate HbF | Beta-thalassemia TDT, including β0/β0 and non-β0/β0-like genotypes in phase 3 study | NEJM 2024 phase 3: 52 infused; among 35 evaluable patients, 32 (91%; 95% CI 77–98) achieved transfusion independence defined as weighted average Hb ≥9 g/dL without RBC transfusion for ≥12 consecutive months; in full analysis population, 48/52 (92%) stopped transfusions for 0.3–45.1 months; mean total Hb during durable response 13.1 g/dL and mean HbF 11.9 g/dL with pancellular distribution; responders stopped transfusions a mean 35.2 days after infusion; ferritin and liver iron decreased in follow-up summaries (locatelli2024exagamglogeneautotemcelfor pages 1-2, locatelli2024exagamglogeneautotemcelfor pages 5-7) | Requires myeloablative busulfan conditioning and transplant-grade infrastructure; short-to-medium follow-up only; adverse events largely conditioning-related; no deaths or cancers reported in interim analysis, but long-term clonal/malignancy surveillance remains essential (locatelli2024exagamglogeneautotemcelfor pages 10-12, locatelli2024exagamglogeneautotemcelfor pages 12-13, locatelli2024exagamglogeneautotemcelfor pages 2-4) | (locatelli2024exagamglogeneautotemcelfor pages 10-12, locatelli2024exagamglogeneautotemcelfor pages 1-2, locatelli2024exagamglogeneautotemcelfor pages 5-7, locatelli2024exagamglogeneautotemcelfor pages 12-13, locatelli2024exagamglogeneautotemcelfor pages 2-4) |
| Gene addition / gene therapy and broader gene-editing landscape (curative-intent class) | Autologous HSC modification by lentiviral β-globin addition or HbF-reactivating genome editing | Beta-thalassemia TDT; not current standard for alpha-thalassemia except experimental/transplant pathways | Reviews and policy analyses describe betibeglogene autotemcel and exa-cel as enabling transfusion independence in many TDT patients and changing the treatment paradigm; recent pediatric/childhood reviews note regulatory approvals in the U.S./Europe/other jurisdictions and growing use of autologous HSC-based curative strategies (thuret2022hurdlestothe pages 1-2, origa2024betathalassemiain pages 1-2) | Major barriers are cost, limited manufacturing slots, need for specialist centers, myeloablation toxicity, uncertain longest-term safety, and inequitable access—especially in LMICs where disease burden is highest (thuret2022hurdlestothe pages 1-2, origa2024betathalassemiain pages 1-2, zhang2024currentstatusand pages 10-13) | (thuret2022hurdlestothe pages 1-2, origa2024betathalassemiain pages 1-2, zhang2024currentstatusand pages 10-13) |


*Table: This table summarizes supportive, disease-modifying, and curative-intent therapies relevant to thalassemia grouping curation. It highlights mechanisms, applicable subtypes, quantitative trial outcomes, and the main safety or access limitations supported by available context citations.*

#### 7.1 Luspatercept (disease-modifying) — pivotal evidence and expert interpretation
**BELIEVE (NEJM; 2020; DOI https://doi.org/10.1056/NEJMoa1910182):** In transfusion-dependent β-thalassemia, luspatercept achieved the primary endpoint (≥33% transfusion reduction during weeks 13–24 plus ≥2 units) in **21.4%** vs **4.5%** placebo (P<0.001). Any 12-week interval ≥33% reduction occurred in **70.5%** vs **29.5%**, and ≥50% reduction in **40.2%** vs **6.3%**. Serum ferritin improved (LS mean difference **−348 µg/L** at week 48). (cappellini2020aphase3 pages 1-2)

**Safety/expert notes:** Reviews summarize venous thromboembolism signals enriched in risk-factor (e.g., splenectomized) patients and note extramedullary hematopoiesis as an observed event requiring monitoring. (hatzimichael2022luspaterceptanew pages 6-7, aydinok2023highlightsonthe pages 1-2, dighriri2022efficacyandsafety pages 10-10)

#### 7.2 Hydroxyurea/HbF induction (disease-modifying; heterogeneous response)
**Randomized placebo-controlled trial in TDT (Scientific Reports; Feb 2022; DOI https://doi.org/10.1038/s41598-022-06774-8):**
- No significant reduction in overall transfusion volume across the whole cohort.
- HbF induction: **89%** vs **59%** placebo showed increased HbF%; mean HbF% increase **3.25%** vs **0.09%** (p=0.006).
- Ineffective erythropoiesis stress marker: soluble transferrin receptor decreased in **79%** vs **40%** placebo; end-of-treatment mean sTfR difference **−22.1 nmol/L** (p=0.007).
- Responders (HbF increase >1.5%) were **44%**; responders had lower transfusion volume (e.g., **77.4 mL/kg** vs **108.4 mL/kg** in non-responders; p=0.005).
- Predictors: response enriched in **HbE/β-thalassemia** and **XmnI** polymorphism. (yasara2022arandomiseddoubleblind pages 2-4, yasara2022arandomiseddoubleblind pages 1-2)

This supports the curator view that HbF induction therapy is modifier-dependent and should be modeled with genotype/modifier context where possible. (yasara2022arandomiseddoubleblind pages 2-4, zahed2023effectiveutilizationof pages 61-64)

#### 7.3 Gene editing (curative-intent) — exa-cel phase 3 (2024)
**Exagamglogene autotemcel (exa-cel) (NEJM; May 2024; DOI https://doi.org/10.1056/NEJMoa2309673):**
- Mechanism: autologous CD34+ HSPCs edited by CRISPR–Cas9 at the erythroid BCL11A enhancer to reactivate HbF. (locatelli2024exagamglogeneautotemcelfor pages 1-2)
- Primary endpoint: transfusion independence (Hb ≥9 g/dL without transfusion for ≥12 months) achieved in **32/35 (91%)** evaluable patients; during independence mean total Hb **13.1 g/dL** and mean HbF **11.9 g/dL** with pancellular distribution. (locatelli2024exagamglogeneautotemcelfor pages 1-2, locatelli2024exagamglogeneautotemcelfor pages 5-7)
- Safety: interim analysis reports no deaths or cancers; adverse events largely consistent with myeloablative busulfan conditioning/transplant. (locatelli2024exagamglogeneautotemcelfor pages 1-2, locatelli2024exagamglogeneautotemcelfor pages 12-13)

### 8) Knowledge gaps and model-system limitations (curation-relevant)

1) **Genotype–phenotype prediction remains imperfect**: severity is shaped by allelic heterogeneity and modifier loci (BCL11A, HBS1L-MYB, XmnI, KLF1) and comorbidities; the same β+ genotype may show variable phenotype. (zahed2023effectiveutilizationof pages 61-64, zahed2023effectiveutilizationof pages 247-249)

2) **Iron toxicity is mechanistically multi-source** (transfusion + absorption) and not consistently quantified in population datasets; GBD frameworks also do not attribute burden to iron overload and infections. (aydinok2023highlightsonthe pages 1-2, zhang2024currentstatusand pages 10-13)

3) **Population-burden datasets under-resolve clinically crucial subtypes**: GBD analyses explicitly do not disaggregate α vs β vs HbE/β or TDT vs NTDT and note heterogeneous reporting/underreporting; ontology modules built directly from GBD should treat thalassemia subtype labels as missing and require supplementation from clinical sources/registries. (tuo2024globalregionaland pages 13-14, zhang2024currentstatusand pages 10-13, tuo2024globalregionaland pages 12-13)

4) **Diagnostic technology gaps**: conventional testing misses mild/silent carriers and complex genotypes; long-read sequencing improves detection but is not yet routine everywhere and introduces variant-interpretation challenges. (li2024applicationofthirdgeneration pages 2-3, foord2026decodingthalassemiaand pages 10-11, li2024applicationofthirdgeneration pages 3-6)

5) **Curative therapy access and long-term safety**: gene therapy/editing requires myeloablation and specialized centers; cost/manufacturing capacity and long-term surveillance remain major barriers to global impact. (thuret2022hurdlestothe pages 1-2, locatelli2024exagamglogeneautotemcelfor pages 12-13, origa2024betathalassemiain pages 1-2)

### 9) Practical YAML curation recommendations (actionable)
1) **Implement grouping as an explicit list** (union) anchored on quantitative globin synthesis defect mechanism; start with Alpha thalassemia + Beta thalassemia as curated members and add the high-value subtype entities listed in Artifact-00.
2) **Add explicit structured fields** beyond HPO for: transfusion-dependence status (TDT/NTDT), hemoglobin fraction patterns/thresholds (HbA2, HbF, HbH, Hb Bart), and imaging/lab iron metrics (ferritin, liver iron, cardiac T2*).
3) **Require genotype evidence where feasible** (HBA1/HBA2 deletional/nondeletional; HBB β0/β+), and treat modifier loci as optional modifiers rather than disease-defining.
4) **Enforce exclusion guardrails** so anemia/iron overload alone cannot qualify an entity for inclusion (prevents ATR-X syndromic inclusion, secondary iron overload-only entries, and non-globin anemias). (necessaryUnknownyeardiagnosticgenetictesting pages 7-9, necessaryUnknownyeardiagnosticgenetictesting pages 4-7, aydinok2023highlightsonthe pages 1-2)

### 10) Key source URLs and publication dates (selected)
- Exagamglogene autotemcel for TDT β-thalassemia (NEJM, **May 2024**): https://doi.org/10.1056/NEJMoa2309673 (locatelli2024exagamglogeneautotemcelfor pages 1-2)
- GBD 2021 thalassemia burden analysis (eClinicalMedicine, **Jun 2024**): https://doi.org/10.1016/j.eclinm.2024.102619 (tuo2024globalregionaland pages 1-2)
- Thalassemia burden in Asia (BMC Public Health, **Dec 2024**): https://doi.org/10.1186/s12889-024-20983-y (zhang2024currentstatusand pages 2-4)
- Third-generation sequencing in thalassemia testing (Molecular Cytogenetics, **Dec 2024**): https://doi.org/10.1186/s13039-024-00701-4 (li2024applicationofthirdgeneration pages 1-2)
- Luspatercept BELIEVE trial (NEJM, **Mar 2020**): https://doi.org/10.1056/NEJMoa1910182 (cappellini2020aphase3 pages 1-2)
- Hydroxyurea RCT in TDT β-thalassemia (Scientific Reports, **Feb 2022**): https://doi.org/10.1038/s41598-022-06774-8 (yasara2022arandomiseddoubleblind pages 1-2)

### 11) Note on PMID identifiers
Within the retrieved evidence context for this run, **explicit PMID numbers were not provided** for most key sources (NEJM/GBD/Scientific Reports items are cited by DOI and journal metadata). Consequently, I cannot supply verified PMIDs without introducing ungrounded identifiers. The DOIs and URLs above provide authoritative retrieval links for downstream PMID look-up in PubMed.


References

1. (li2024applicationofthirdgeneration pages 1-2): Weihao Li and Yanchou Ye. Application of third-generation sequencing technology in the genetic testing of thalassemia. Molecular Cytogenetics, Dec 2024. URL: https://doi.org/10.1186/s13039-024-00701-4, doi:10.1186/s13039-024-00701-4. This article has 7 citations and is from a peer-reviewed journal.

2. (thuret2022hurdlestothe pages 1-2): Isabelle Thuret, Annalisa Ruggeri, Emanuele Angelucci, and Christian Chabannon. Hurdles to the adoption of gene therapy as a curative option for transfusion-dependent thalassemia. Stem Cells Translational Medicine, 11:407-414, Mar 2022. URL: https://doi.org/10.1093/stcltm/szac007, doi:10.1093/stcltm/szac007. This article has 31 citations and is from a domain leading peer-reviewed journal.

3. (necessaryUnknownyeardiagnosticgenetictesting pages 7-9): M Necessary and NM Necessary. Diagnostic genetic testing for α-thalassemia. Unknown journal, Unknown year.

4. (li2024applicationofthirdgeneration pages 2-3): Weihao Li and Yanchou Ye. Application of third-generation sequencing technology in the genetic testing of thalassemia. Molecular Cytogenetics, Dec 2024. URL: https://doi.org/10.1186/s13039-024-00701-4, doi:10.1186/s13039-024-00701-4. This article has 7 citations and is from a peer-reviewed journal.

5. (zahed2023effectiveutilizationof pages 67-70): R Zahed. Effective utilization of molecular genetic screening of patients with sickle cell disease and beta thalassemia major in saudi arabia. Unknown journal, 2023.

6. (zahed2023effectiveutilizationof pages 61-64): R Zahed. Effective utilization of molecular genetic screening of patients with sickle cell disease and beta thalassemia major in saudi arabia. Unknown journal, 2023.

7. (origa2024betathalassemiain pages 1-2): Raffaella Origa and Layal Issa. Beta thalassemia in children: established approaches, old issues, new non-curative therapies, and perspectives on healing. Journal of Clinical Medicine, 13:6966, Nov 2024. URL: https://doi.org/10.3390/jcm13226966, doi:10.3390/jcm13226966. This article has 10 citations.

8. (necessaryUnknownyeardiagnosticgenetictesting pages 4-7): M Necessary and NM Necessary. Diagnostic genetic testing for α-thalassemia. Unknown journal, Unknown year.

9. (li2024applicationofthirdgeneration pages 3-6): Weihao Li and Yanchou Ye. Application of third-generation sequencing technology in the genetic testing of thalassemia. Molecular Cytogenetics, Dec 2024. URL: https://doi.org/10.1186/s13039-024-00701-4, doi:10.1186/s13039-024-00701-4. This article has 7 citations and is from a peer-reviewed journal.

10. (locatelli2024exagamglogeneautotemcelfor pages 1-2): Franco Locatelli, Peter Lang, Donna Wall, Roland Meisel, Selim Corbacioglu, Amanda M. Li, Josu de la Fuente, Ami J. Shah, Ben Carpenter, Janet L. Kwiatkowski, Markus Mapara, Robert I. Liem, Maria Domenica Cappellini, Mattia Algeri, Antonis Kattamis, Sujit Sheth, Stephan Grupp, Rupert Handgretinger, Puja Kohli, Daoyuan Shi, Leorah Ross, Yael Bobruff, Christopher Simard, Lanju Zhang, Phuong Khanh Morrow, William E. Hobbs, and Haydar Frangoul. Exagamglogene autotemcel for transfusion-dependent β-thalassemia. May 2024. URL: https://doi.org/10.1056/nejmoa2309673, doi:10.1056/nejmoa2309673. This article has 237 citations and is from a highest quality peer-reviewed journal.

11. (aydinok2023highlightsonthe pages 1-2): Yesim Aydinok. Highlights on the luspatercept treatment in thalassemia. Thalassemia Reports, 13:77-84, Feb 2023. URL: https://doi.org/10.3390/thalassrep13010008, doi:10.3390/thalassrep13010008. This article has 2 citations.

12. (locatelli2024exagamglogeneautotemcelfor pages 5-7): Franco Locatelli, Peter Lang, Donna Wall, Roland Meisel, Selim Corbacioglu, Amanda M. Li, Josu de la Fuente, Ami J. Shah, Ben Carpenter, Janet L. Kwiatkowski, Markus Mapara, Robert I. Liem, Maria Domenica Cappellini, Mattia Algeri, Antonis Kattamis, Sujit Sheth, Stephan Grupp, Rupert Handgretinger, Puja Kohli, Daoyuan Shi, Leorah Ross, Yael Bobruff, Christopher Simard, Lanju Zhang, Phuong Khanh Morrow, William E. Hobbs, and Haydar Frangoul. Exagamglogene autotemcel for transfusion-dependent β-thalassemia. May 2024. URL: https://doi.org/10.1056/nejmoa2309673, doi:10.1056/nejmoa2309673. This article has 237 citations and is from a highest quality peer-reviewed journal.

13. (tuo2024globalregionaland pages 13-14): Yuanyuan Tuo, Yang Li, Yan Li, Jianjuan Ma, Xiaoyan Yang, Shasha Wu, Jiao Jin, and Zhixu He. Global, regional, and national burden of thalassemia, 1990–2021: a systematic analysis for the global burden of disease study 2021. Jun 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102619, doi:10.1016/j.eclinm.2024.102619. This article has 245 citations and is from a peer-reviewed journal.

14. (zhang2024currentstatusand pages 10-13): Shuning Zhang, Zhangjie Chen, Meihuan Chen, and Hailong Huang. Current status and trends in thalassemia burden across south, east and southeast asia, 1990–2021 a systematic analysis for the global burden of disease study 2021. BMC Public Health, Dec 2024. URL: https://doi.org/10.1186/s12889-024-20983-y, doi:10.1186/s12889-024-20983-y. This article has 29 citations and is from a peer-reviewed journal.

15. (tuo2024globalregionaland pages 2-3): Yuanyuan Tuo, Yang Li, Yan Li, Jianjuan Ma, Xiaoyan Yang, Shasha Wu, Jiao Jin, and Zhixu He. Global, regional, and national burden of thalassemia, 1990–2021: a systematic analysis for the global burden of disease study 2021. Jun 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102619, doi:10.1016/j.eclinm.2024.102619. This article has 245 citations and is from a peer-reviewed journal.

16. (tuo2024globalregionaland pages 1-2): Yuanyuan Tuo, Yang Li, Yan Li, Jianjuan Ma, Xiaoyan Yang, Shasha Wu, Jiao Jin, and Zhixu He. Global, regional, and national burden of thalassemia, 1990–2021: a systematic analysis for the global burden of disease study 2021. Jun 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102619, doi:10.1016/j.eclinm.2024.102619. This article has 245 citations and is from a peer-reviewed journal.

17. (zahed2023effectiveutilizationof pages 58-61): R Zahed. Effective utilization of molecular genetic screening of patients with sickle cell disease and beta thalassemia major in saudi arabia. Unknown journal, 2023.

18. (cappellini2021theuseof pages 1-2): Maria Domenica Cappellini and Ali T. Taher. The use of luspatercept for thalassemia in adults. Blood advances, 5 1:326-333, Jan 2021. URL: https://doi.org/10.1182/bloodadvances.2020002725, doi:10.1182/bloodadvances.2020002725. This article has 68 citations and is from a peer-reviewed journal.

19. (cappellini2020aphase3 pages 1-2): M. Domenica Cappellini, Vip Viprakasit, Ali T. Taher, Pencho Georgiev, Kevin H.M. Kuo, Thomas Coates, Ersi Voskaridou, Hong-Keng Liew, Idit Pazgal-Kobrowski, G.L. Forni, Silverio Perrotta, Abderrahim Khelif, Ashutosh Lal, Antonis Kattamis, Efthymia Vlachaki, Raffaella Origa, Yesim Aydinok, Mohamed Bejaoui, P. Joy Ho, Lee-Ping Chew, Ping-Chong Bee, Soo-Min Lim, Meng-Yao Lu, Adisak Tantiworawit, Penka Ganeva, Liana Gercheva, Farrukh Shah, Ellis J. Neufeld, Alexis Thompson, Abderrahmane Laadem, Jeevan K. Shetty, Jun Zou, Jennie Zhang, Dimana Miteva, Tatiana Zinger, Peter G. Linde, Matthew L. Sherman, Olivier Hermine, John Porter, and Antonio Piga. A phase 3 trial of luspatercept in patients with transfusion-dependent β-thalassemia. Mar 2020. URL: https://doi.org/10.1056/nejmoa1910182, doi:10.1056/nejmoa1910182. This article has 401 citations and is from a highest quality peer-reviewed journal.

20. (locatelli2024exagamglogeneautotemcelfor pages 2-4): Franco Locatelli, Peter Lang, Donna Wall, Roland Meisel, Selim Corbacioglu, Amanda M. Li, Josu de la Fuente, Ami J. Shah, Ben Carpenter, Janet L. Kwiatkowski, Markus Mapara, Robert I. Liem, Maria Domenica Cappellini, Mattia Algeri, Antonis Kattamis, Sujit Sheth, Stephan Grupp, Rupert Handgretinger, Puja Kohli, Daoyuan Shi, Leorah Ross, Yael Bobruff, Christopher Simard, Lanju Zhang, Phuong Khanh Morrow, William E. Hobbs, and Haydar Frangoul. Exagamglogene autotemcel for transfusion-dependent β-thalassemia. May 2024. URL: https://doi.org/10.1056/nejmoa2309673, doi:10.1056/nejmoa2309673. This article has 237 citations and is from a highest quality peer-reviewed journal.

21. (yasara2022arandomiseddoubleblind pages 1-2): Nirmani Yasara, Nethmi Wickramarathne, Chamila Mettananda, Ishari Silva, Nizri Hameed, Kumari Attanayaka, Rexan Rodrigo, Nirmani Wickramasinghe, Lakshman Perera, Aresha Manamperi, Anuja Premawardhena, and Sachith Mettananda. A randomised double-blind placebo-controlled clinical trial of oral hydroxyurea for transfusion-dependent β-thalassaemia. Scientific Reports, Feb 2022. URL: https://doi.org/10.1038/s41598-022-06774-8, doi:10.1038/s41598-022-06774-8. This article has 38 citations and is from a peer-reviewed journal.

22. (yasara2022arandomiseddoubleblind pages 2-4): Nirmani Yasara, Nethmi Wickramarathne, Chamila Mettananda, Ishari Silva, Nizri Hameed, Kumari Attanayaka, Rexan Rodrigo, Nirmani Wickramasinghe, Lakshman Perera, Aresha Manamperi, Anuja Premawardhena, and Sachith Mettananda. A randomised double-blind placebo-controlled clinical trial of oral hydroxyurea for transfusion-dependent β-thalassaemia. Scientific Reports, Feb 2022. URL: https://doi.org/10.1038/s41598-022-06774-8, doi:10.1038/s41598-022-06774-8. This article has 38 citations and is from a peer-reviewed journal.

23. (dighriri2022efficacyandsafety pages 10-10): Ibrahim M Dighriri, Khawlah K Alrabghi, Dilveen M Sulaiman, Abdulrahman M Alruwaili, Nader S Alanazi, Al-maha A Al-Sadiq, ‌‏Amal M Hadadi, Bushra Y Sahli, Basil A Qasem, Manal T Alotaibi, Taif T Asiri, Salman M Majrashi, Noura T Alotibia, Afnan T Alhamyani, and Amjad A Alharbi. Efficacy and safety of luspatercept in the treatment of β-thalassemia: a systematic review. Cureus, Nov 2022. URL: https://doi.org/10.7759/cureus.31570, doi:10.7759/cureus.31570. This article has 10 citations.

24. (locatelli2024exagamglogeneautotemcelfor pages 10-12): Franco Locatelli, Peter Lang, Donna Wall, Roland Meisel, Selim Corbacioglu, Amanda M. Li, Josu de la Fuente, Ami J. Shah, Ben Carpenter, Janet L. Kwiatkowski, Markus Mapara, Robert I. Liem, Maria Domenica Cappellini, Mattia Algeri, Antonis Kattamis, Sujit Sheth, Stephan Grupp, Rupert Handgretinger, Puja Kohli, Daoyuan Shi, Leorah Ross, Yael Bobruff, Christopher Simard, Lanju Zhang, Phuong Khanh Morrow, William E. Hobbs, and Haydar Frangoul. Exagamglogene autotemcel for transfusion-dependent β-thalassemia. May 2024. URL: https://doi.org/10.1056/nejmoa2309673, doi:10.1056/nejmoa2309673. This article has 237 citations and is from a highest quality peer-reviewed journal.

25. (locatelli2024exagamglogeneautotemcelfor pages 12-13): Franco Locatelli, Peter Lang, Donna Wall, Roland Meisel, Selim Corbacioglu, Amanda M. Li, Josu de la Fuente, Ami J. Shah, Ben Carpenter, Janet L. Kwiatkowski, Markus Mapara, Robert I. Liem, Maria Domenica Cappellini, Mattia Algeri, Antonis Kattamis, Sujit Sheth, Stephan Grupp, Rupert Handgretinger, Puja Kohli, Daoyuan Shi, Leorah Ross, Yael Bobruff, Christopher Simard, Lanju Zhang, Phuong Khanh Morrow, William E. Hobbs, and Haydar Frangoul. Exagamglogene autotemcel for transfusion-dependent β-thalassemia. May 2024. URL: https://doi.org/10.1056/nejmoa2309673, doi:10.1056/nejmoa2309673. This article has 237 citations and is from a highest quality peer-reviewed journal.

26. (winkler2026currentstatusof pages 11-12): Rebecca Winkler, Ishan Herath, Radoslaw Kaczmarek, Weidong Xiao, Roland Herzog, and Paige Severeid. Current status of clinical gene therapy for hemophilia and globin disorders. Journal of Blood Medicine, Volume 17:1-17, Feb 2026. URL: https://doi.org/10.2147/jbm.s576017, doi:10.2147/jbm.s576017. This article has 0 citations.

27. (yasara2022arandomiseddoubleblind pages 6-7): Nirmani Yasara, Nethmi Wickramarathne, Chamila Mettananda, Ishari Silva, Nizri Hameed, Kumari Attanayaka, Rexan Rodrigo, Nirmani Wickramasinghe, Lakshman Perera, Aresha Manamperi, Anuja Premawardhena, and Sachith Mettananda. A randomised double-blind placebo-controlled clinical trial of oral hydroxyurea for transfusion-dependent β-thalassaemia. Scientific Reports, Feb 2022. URL: https://doi.org/10.1038/s41598-022-06774-8, doi:10.1038/s41598-022-06774-8. This article has 38 citations and is from a peer-reviewed journal.

28. (tuo2024globalregionaland pages 3-4): Yuanyuan Tuo, Yang Li, Yan Li, Jianjuan Ma, Xiaoyan Yang, Shasha Wu, Jiao Jin, and Zhixu He. Global, regional, and national burden of thalassemia, 1990–2021: a systematic analysis for the global burden of disease study 2021. Jun 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102619, doi:10.1016/j.eclinm.2024.102619. This article has 245 citations and is from a peer-reviewed journal.

29. (zhang2024currentstatusand pages 2-4): Shuning Zhang, Zhangjie Chen, Meihuan Chen, and Hailong Huang. Current status and trends in thalassemia burden across south, east and southeast asia, 1990–2021 a systematic analysis for the global burden of disease study 2021. BMC Public Health, Dec 2024. URL: https://doi.org/10.1186/s12889-024-20983-y, doi:10.1186/s12889-024-20983-y. This article has 29 citations and is from a peer-reviewed journal.

30. (foord2026decodingthalassemiaand pages 10-11): Emelie Foord, Darius Sairafi, Monika Berg, Sofia Westerling, Toheeb Adigun, Mehmet Uzunel, Thessalia Papasavva, and Michael Uhlin. Decoding thalassemia and sickle cell disease: advances in molecular technologies for comprehensive variant detection. Frontiers in Genetics, Apr 2026. URL: https://doi.org/10.3389/fgene.2026.1810737, doi:10.3389/fgene.2026.1810737. This article has 0 citations and is from a peer-reviewed journal.

31. (zhu2026currentresearchstatus pages 8-10): Fenglin Zhu, Yunli Lai, and Sheng He. Current research status of third-generation sequencing technology in thalassemia detection. Frontiers in Pediatrics, Jan 2026. URL: https://doi.org/10.3389/fped.2025.1705599, doi:10.3389/fped.2025.1705599. This article has 0 citations.

32. (zahed2023effectiveutilizationof pages 247-249): R Zahed. Effective utilization of molecular genetic screening of patients with sickle cell disease and beta thalassemia major in saudi arabia. Unknown journal, 2023.

33. (nguyen2025prevalenceofcommon pages 1-2): Trang Thi Nguyen, Ha Thu Thi To, Anh Ngoc Thi Le, Anh Quang Pham, Nhu Duc Nguyen, Hao Huu Ha, Huyen Thi Thanh Vu, Thanh Thai Hoang, and Minh Cong Tran. Prevalence of common autosomal recessive and x-linked conditions in pregnant women in vietnam: a cross-sectional study. Scientific Reports, May 2025. URL: https://doi.org/10.1038/s41598-025-03399-5, doi:10.1038/s41598-025-03399-5. This article has 2 citations and is from a peer-reviewed journal.

34. (hatzimichael2022luspaterceptanew pages 6-7): Eleftheria Hatzimichael, Despoina Timotheatou, Epameinondas Koumpis, Leonidas Benetatos, and Alexandros Makis. Luspatercept: a new tool for the treatment of anemia related to β-thalassemia, myelodysplastic syndromes and primary myelofibrosis. Diseases, 10:85, Oct 2022. URL: https://doi.org/10.3390/diseases10040085, doi:10.3390/diseases10040085. This article has 24 citations.

35. (yasara2022arandomiseddoubleblind pages 5-6): Nirmani Yasara, Nethmi Wickramarathne, Chamila Mettananda, Ishari Silva, Nizri Hameed, Kumari Attanayaka, Rexan Rodrigo, Nirmani Wickramasinghe, Lakshman Perera, Aresha Manamperi, Anuja Premawardhena, and Sachith Mettananda. A randomised double-blind placebo-controlled clinical trial of oral hydroxyurea for transfusion-dependent β-thalassaemia. Scientific Reports, Feb 2022. URL: https://doi.org/10.1038/s41598-022-06774-8, doi:10.1038/s41598-022-06774-8. This article has 38 citations and is from a peer-reviewed journal.

36. (yasara2022arandomiseddoubleblind pages 7-8): Nirmani Yasara, Nethmi Wickramarathne, Chamila Mettananda, Ishari Silva, Nizri Hameed, Kumari Attanayaka, Rexan Rodrigo, Nirmani Wickramasinghe, Lakshman Perera, Aresha Manamperi, Anuja Premawardhena, and Sachith Mettananda. A randomised double-blind placebo-controlled clinical trial of oral hydroxyurea for transfusion-dependent β-thalassaemia. Scientific Reports, Feb 2022. URL: https://doi.org/10.1038/s41598-022-06774-8, doi:10.1038/s41598-022-06774-8. This article has 38 citations and is from a peer-reviewed journal.

37. (yasara2022arandomiseddoubleblind pages 4-5): Nirmani Yasara, Nethmi Wickramarathne, Chamila Mettananda, Ishari Silva, Nizri Hameed, Kumari Attanayaka, Rexan Rodrigo, Nirmani Wickramasinghe, Lakshman Perera, Aresha Manamperi, Anuja Premawardhena, and Sachith Mettananda. A randomised double-blind placebo-controlled clinical trial of oral hydroxyurea for transfusion-dependent β-thalassaemia. Scientific Reports, Feb 2022. URL: https://doi.org/10.1038/s41598-022-06774-8, doi:10.1038/s41598-022-06774-8. This article has 38 citations and is from a peer-reviewed journal.

38. (tuo2024globalregionaland pages 12-13): Yuanyuan Tuo, Yang Li, Yan Li, Jianjuan Ma, Xiaoyan Yang, Shasha Wu, Jiao Jin, and Zhixu He. Global, regional, and national burden of thalassemia, 1990–2021: a systematic analysis for the global burden of disease study 2021. Jun 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102619, doi:10.1016/j.eclinm.2024.102619. This article has 245 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Thalassemias-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Thalassemias-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Thalassemias-deep-research-falcon_artifacts/artifact-02.md)
