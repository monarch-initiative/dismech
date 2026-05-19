---
provider: scanner
model: claude-sonnet-4-6
cached: true
start_time: '2026-05-18T00:00:00Z'
end_time: '2026-05-18T00:00:00Z'
duration_seconds: 0
template_file: templates/disease_pathophysiology_research_scanner.md
template_variables:
  disease_name: Congenital Hypofibrinogenemia
  mondo_id: MONDO:0015096
  category: Genetic
provider_config:
  source: cached_references
  references_used:
  - PMID:29316703
  - PMID:36055263
  - PMID:30076675
---

## Question

Pathophysiology and clinical mechanisms of Congenital Hypofibrinogenemia (simple form). Core disease mechanisms, molecular and cellular pathways, involved genes and proteins, affected cell types and anatomical structures, disease progression, major clinical phenotypes and complications, and treatment-relevant mechanism papers.

## Output

# Scanner Research Synthesis: Congenital Hypofibrinogenemia (Simple Quantitative Form)

This report is based on cached reference abstracts available in `references_cache/`.

---

## Disease Identity

- **Preferred name**: Congenital Hypofibrinogenemia (simple quantitative form)
- **MONDO**: MONDO:0015096 (familial hypofibrinogenemia)
- **ISTH classification**: Type I (quantitative) congenital fibrinogen disorder
- **OMIM**: 202400 (afibrinogenemia, autosomal recessive); hypofibrinogenemia is the heterozygous form with partial deficiency
- **Note**: This entry covers the simple LOF form only. Hepatic Fibrinogen Storage Disease (HFSD/HHHS), caused by specific FGG missense variants driving hepatocyte ER aggregation, is a mechanistically distinct entity treated separately.

---

## Core Pathophysiology

### Genetic Mechanism

Congenital hypofibrinogenemia is caused by **heterozygous loss-of-function mutations** in one of three fibrinogen chain genes: **FGA** (Aα chain), **FGB** (Bβ chain), or **FGG** (γ chain), clustered at chromosome 4q28.

Causative mutation classes (PMID:29316703):
1. **Null mutations** — complete loss of expression from one allele (large deletions, frameshift, nonsense, splice-site variants)
2. **Hypomorphic/secretion-impairing missense mutations** — protein produced but mis-folded or retained intracellularly, reducing secretion

Because fibrinogen is a heterohexamer (2×Aα + 2×Bβ + 2×γ), loss of one chain prevents normal hexamer assembly from that allele. Heterozygosity reduces hepatic output by approximately 50%, resulting in circulating fibrinogen levels between 0.5–1.5 g/L (normal range: 2–4 g/L).

### Molecular Pathway

1. **Heterozygous LOF allele (FGA/FGB/FGG)** →
2. **Reduced fibrinogen hexamer assembly and secretion by hepatocytes** →
3. **Low circulating fibrinogen (hypofibrinogenemia; Fg:C <1.5 g/L)** →
4. **Limited substrate for thrombin-mediated fibrin polymerization** →
5. **Impaired fibrin clot formation** →
6. **Level-dependent bleeding diathesis** (typically mild; prothrombotic Fg:C >1.0 g/L is broadly protective)

### Key Liver Biology

Fibrinogen is an **acute-phase protein** synthesized exclusively by **hepatocytes** (CL:0000182). All three chains are co-expressed, assembled in the ER, and secreted as intact hexamers. In the simple quantitative form, liver morphology is normal (no intracellular aggregation), distinguishing this from HFSD.

---

## Clinical Phenotype

### Severity Spectrum

Severity correlates directly with residual fibrinogen level (PMID:29316703):
- **Fg:C ≥1.0 g/L**: Generally asymptomatic; most heterozygous carriers fall here
- **Fg:C 0.7–1.0 g/L**: Mild-to-moderate bleeding risk, typically provoked
- **Fg:C <0.7 g/L**: Increased spontaneous bleeding risk; approaches afibrinogenemia spectrum

### Major Phenotypes

**Hematologic:**
- Hypofibrinogenemia (obligate, defining) — HP:0011900
- Abnormal bleeding (variable severity) — HP:0001892
- Persistent bleeding after trauma/surgery — HP:0001934

**Reproductive (females):**
- Menorrhagia — HP:0000132 (level-dependent)
- Obstetrical complications including recurrent placental abruption — reflects fibrinogen requirement for placental integrity. Fibrinogen is necessary for cytotrophoblast spreading at 4–6 weeks gestation and fetal-maternal vascular development (PMID:29316703).

### Laboratory Findings

- Prolonged PT and aPTT (proportional to fibrinogen level)
- Reduced plasma fibrinogen by both Clauss clotting assay and immunologic antigen assay (both low, distinguishing from dysfibrinogenemia where ratio differs)
- Thromboelastography: reduced clot amplitude and firmness

---

## Genetics

| Gene | HGNC | Chain | Mutation classes |
|------|------|-------|-----------------|
| FGA | hgnc:3661 | Aα | Null and missense; >200 variants described |
| FGB | hgnc:3662 | Bβ | Null and missense |
| FGG | hgnc:3694 | γ | Null and missense (non-polymerization-pocket missense; HFSD-causing γ variants are excluded from this entry) |

**Inheritance**: Autosomal dominant (heterozygous LOF). Afibrinogenemia (biallelic null) is autosomal recessive. Hypofibrinogenemia is the heterozygous carrier state of autosomal recessive afibrinogenemia alleles, and also arises de novo.

---

## Treatment

**Fibrinogen replacement (on-demand and prophylactic)**:
- Fibrinogen concentrate (e.g., Haemocomplettan/RiaSTAP; NCIT:C81126 Fibrinogen Human) is the therapeutic cornerstone (PMID:36055263)
- Targets: Fg:C ≥1.0 g/L (general hemostasis), ≥1.5–2.0 g/L perioperatively, ≥2.0 g/L peripartum
- Cryoprecipitate (contains fibrinogen, FVIII, vWF, FXIII) is an alternative where concentrate is unavailable
- Antifibrinolytics (tranexamic acid) are useful adjuncts for minor bleeds and dental procedures

**Asymptomatic management**:
- Many patients with Fg:C >1.0 g/L require no prophylactic treatment
- Awareness of obstetric risks and perioperative prophylaxis planning are important for female patients

---

## Key References

| PMID | Authors | Title | Key content |
|------|---------|-------|-------------|
| 29316703 | de Moerloose et al. (2018) | Clinical Consequences and Molecular Bases of Low Fibrinogen Levels | Main review covering pathophysiology, phenotype, obstetric complications |
| 36055263 | Casini et al. (2022) | One Hundred Years of Congenital Fibrinogen Disorders | Classification evolution, fibrinogen concentrate, 100-year review |
| 30076675 | Casini et al. (2018) | Diagnosis and classification of congenital fibrinogen disorders | ISTH SSC classification framework |

---

## Scope Note

This entry models the **simple quantitative (Type I, LOF, liver-normal) form** of hypofibrinogenemia. Two mechanistically distinct entities in the congenital fibrinogen disorder family are treated separately:
- **Afibrinogenemia**: biallelic null (AR); more severe
- **Hepatic Fibrinogen Storage Disease (HFSD)**: gain-of-toxic-function FGG missense → hepatocyte ER aggregation → hepatopathy (see sibling entry)

Tracker issue: #2727.
