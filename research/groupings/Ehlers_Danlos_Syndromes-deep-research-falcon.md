---
title: Ehlers-Danlos Syndromes grouping deep research
keywords:
- grouping
- ehlers-danlos
- connective-tissue
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-13T16:23:58.238309'
end_time: '2026-06-13T16:53:20.616116'
duration_seconds: 1762.38
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_tokens: 12000
    max_embedded_images: 8
citation_count: 59
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Ehlers_Danlos_Syndromes-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Ehlers_Danlos_Syndromes-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Ehlers_Danlos_Syndromes-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

Prepare a focused, citation-rich deep research report for a dismech disease grouping called 'Ehlers-Danlos Syndromes'. The grouping should be an explicit curated union of Disease entries, not merely a MONDO hierarchy clone. Current likely candidate members in the knowledge base include any Ehlers-Danlos syndrome entries and related brittle cornea/periodontal/vascular/classical/hypermobile/kyphoscoliotic/arthrochalasia/dermatosparaxis/spondylodysplastic/musculocontractural/myopathic/cardiac-valvular EDS entries if present. Research objectives: 1. define shared EDS pathophysiology across collagen fibrillogenesis, extracellular matrix assembly, collagen processing/crosslinking, glycosaminoglycan biosynthesis, complement/vascular wall branches, and connective-tissue fragility; 2. distinguish major subtype mechanisms and genes including COL5A1/COL5A2 classical EDS, COL3A1 vascular EDS, TNXB/classic-like EDS, PLOD1/FKBP14 kyphoscoliotic EDS, ADAMTS2 dermatosparaxis EDS, COL1A1/COL1A2 arthrochalasia or cardiac-valvular overlap, B4GALT7/B3GALT6/SLC39A13 spondylodysplastic EDS, CHST14/DSE musculocontractural EDS, C1R/C1S periodontal EDS, and AEBP1 classical-like EDS; 3. recommend a defensible grouping boundary and explicitly flag disorders to exclude, such as Marfan syndrome, Loeys-Dietz syndrome, osteogenesis imperfecta, and nonsyndromic joint hypermobility unless curated as EDS entries; 4. list differentiating mechanisms for existing and high-value missing subtype entries; 5. identify appropriate MONDO mapping, HPO phenotype criteria, and any dismech module-conformance criteria or module gaps for the grouping YAML; 6. provide primary literature, GeneReviews, and authoritative review citations with PMID identifiers wherever possible; 7. flag knowledge gaps and model-system limitations relevant to connective tissue, vascular rupture, and therapeutic evidence. Do not invent citations; prefer PubMed-indexed sources and provide exact PMID identifiers for key claims.

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

Prepare a focused, citation-rich deep research report for a dismech disease grouping called 'Ehlers-Danlos Syndromes'. The grouping should be an explicit curated union of Disease entries, not merely a MONDO hierarchy clone. Current likely candidate members in the knowledge base include any Ehlers-Danlos syndrome entries and related brittle cornea/periodontal/vascular/classical/hypermobile/kyphoscoliotic/arthrochalasia/dermatosparaxis/spondylodysplastic/musculocontractural/myopathic/cardiac-valvular EDS entries if present. Research objectives: 1. define shared EDS pathophysiology across collagen fibrillogenesis, extracellular matrix assembly, collagen processing/crosslinking, glycosaminoglycan biosynthesis, complement/vascular wall branches, and connective-tissue fragility; 2. distinguish major subtype mechanisms and genes including COL5A1/COL5A2 classical EDS, COL3A1 vascular EDS, TNXB/classic-like EDS, PLOD1/FKBP14 kyphoscoliotic EDS, ADAMTS2 dermatosparaxis EDS, COL1A1/COL1A2 arthrochalasia or cardiac-valvular overlap, B4GALT7/B3GALT6/SLC39A13 spondylodysplastic EDS, CHST14/DSE musculocontractural EDS, C1R/C1S periodontal EDS, and AEBP1 classical-like EDS; 3. recommend a defensible grouping boundary and explicitly flag disorders to exclude, such as Marfan syndrome, Loeys-Dietz syndrome, osteogenesis imperfecta, and nonsyndromic joint hypermobility unless curated as EDS entries; 4. list differentiating mechanisms for existing and high-value missing subtype entries; 5. identify appropriate MONDO mapping, HPO phenotype criteria, and any dismech module-conformance criteria or module gaps for the grouping YAML; 6. provide primary literature, GeneReviews, and authoritative review citations with PMID identifiers wherever possible; 7. flag knowledge gaps and model-system limitations relevant to connective tissue, vascular rupture, and therapeutic evidence. Do not invent citations; prefer PubMed-indexed sources and provide exact PMID identifiers for key claims.

## Deep research report: Curated disease grouping “Ehlers–Danlos Syndromes” (EDS)

### Scope and deliverable
This report defines a **dismech disease grouping** named **“Ehlers–Danlos Syndromes”** as an **explicit curated union of disease entries** (not a MONDO hierarchy clone), with mechanistic rationale spanning collagen fibrillogenesis/processing, extracellular matrix (ECM) organization, collagen folding/crosslinking, glycosaminoglycan (GAG)/proteoglycan biosynthesis, and (uniquely) complement-pathway–linked periodontal disease. The goal is to support grouping YAML curation, subtype-aware mechanistic modeling, and phenotype-based inclusion checks. (damme2022theehlers–danlossyndromes pages 1-2, chiarelli2019cellularandmolecular pages 3-5)

---

## 1) Key concepts and definitions (current understanding)

### 1.1 What “Ehlers–Danlos syndromes” means in modern nosology
Across authoritative mechanistic and diagnostic syntheses, **EDS is defined as a clinically and genetically heterogeneous group of heritable connective tissue disorders** whose shared clinical core includes combinations of **joint hypermobility**, **skin hyperextensibility/fragility**, and **generalized tissue fragility** (including visceral and vascular complications in some subtypes). (chiarelli2019cellularandmolecular pages 3-5, damme2022theehlers–danlossyndromes pages 1-2)

A mechanistic framing consistent with the 2017-era classification and subsequent updates partitions EDS into categories affecting:
- **Collagen primary structure and collagen processing** (fibrillar collagens; processing proteases). (chiarelli2019cellularandmolecular pages 3-5, zoppi2018multifacedrolesof pages 3-5)
- **Collagen folding and crosslinking** (enzymes/chaperones; ER folding quality control). (chiarelli2019cellularandmolecular pages 3-5, damme2022theehlers–danlossyndromes pages 2-3)
- **ECM organization/bridging molecules** (non-collagen structural regulators). (damme2022theehlers–danlossyndromes pages 15-16)
- **GAG/proteoglycan biosynthesis** (linker-region glycosyltransferases; dermatan sulfate biosynthesis enzymes). (damme2022theehlers–danlossyndromes pages 13-15, yoshizawa2023mousemodelsof pages 1-2)
- **Complement pathway involvement** (periodontal EDS). (kapfererseebacher2016periodontalehlersdanlossyndrome pages 2-3, kapfererseebacher2016periodontalehlersdanlossyndrome pages 1-2)
- **Intracellular processes influencing ECM homeostasis** (e.g., zinc transport, transcriptional regulation). (chiarelli2019cellularandmolecular pages 3-5, zoppi2018multifacedrolesof pages 3-5)

### 1.2 Shared pathophysiology (cross-subtype)
Despite diverse primary genetic causes, EDS types converge on **loss of tissue tensile strength and impaired ECM integrity**. Reviews emphasize shared downstream themes:
- **ECM disorganization and abnormal remodeling/turnover** with altered interactions among collagens, fibronectin/fibrillins, and integrins. (chiarelli2019cellularandmolecular pages 5-7, chiarelli2019cellularandmolecular pages 1-3)
- **Intracellular stress and proteostasis dysfunction** in collagen-producing cells (e.g., ER homeostasis perturbation, altered autophagy) as misfolded ECM proteins accumulate or trafficking fails. (chiarelli2019cellularandmolecular pages 1-3, chiarelli2019cellularandmolecular pages 3-5)
- **DAMP-like signaling from matrix fragments** and related innate immune/inflammatory activation contributing to pain and tissue dysfunction (especially emphasized for hEDS where primary gene is unknown). (chiarelli2019cellularandmolecular pages 3-5, chiarelli2019cellularandmolecular pages 1-3)

---

## 2) Proposed grouping boundary (explicit curated union) + exclusions

### 2.1 Defensible grouping boundary (include only explicit EDS disease entries)
The recommended boundary is:
- **Include**: diseases that are explicitly Ehlers–Danlos syndrome subtypes (including later-recognized subtypes such as **AEBP1-related classical-like EDS type 2**) and are represented as disease entries. (chiarelli2019cellularandmolecular pages 3-5, ritelli2019expandingtheclinical pages 1-3)
- **Conditionally include**: EDS-adjacent disorders (e.g., brittle cornea syndrome) *only if they exist as explicit “EDS-related” disease entries* in the knowledge base, rather than being included via MONDO ancestry alone. (zoppi2018multifacedrolesof pages 3-5, dijk2024clinicaldiagnosisof pages 3-4)

### 2.2 Explicit exclusions (flagged)
Exclude disorders that overlap phenotypically but are not EDS subtypes:
- **Marfan syndrome** (FBN1) and **Loeys–Dietz syndrome** (TGFβ-pathway genes) are distinct heritable connective tissue disorders/aortopathies despite overlap. (bowen2023diagnosisandmanagement pages 7-8)
- **Osteogenesis imperfecta** and other collagen bone fragility disorders unless explicitly curated as an EDS overlap entry. (damme2022theehlers–danlossyndromes pages 15-16, kapfererseebacher2020dentalmanifestationsof pages 1-2)
- **Arterial tortuosity syndrome**, **cutis laxa**, etc., unless explicitly curated as EDS-related. (zoppi2018multifacedrolesof pages 3-5)
- **Nonsyndromic generalized joint hypermobility / hypermobility spectrum disorders (HSD)**, unless the entry is explicitly an EDS diagnosis (to avoid conflating common hypermobility with rare monogenic EDS). (zschocke2024geneticdiagnosisof pages 1-2, morlino2023placingjointhypermobility pages 7-7)

| Group | Disease label | Key gene(s)/mechanism anchor | Rationale for include/exclude |
|---|---|---|---|
| Include core | Classical Ehlers-Danlos syndrome (cEDS) | COL5A1, COL5A2; rare COL1A1; type V collagen / collagen fibrillogenesis | Core 2017 EDS subtype; prototypic collagen-fibrillogenesis disorder with skin fragility, joint hypermobility, and ECM disorganization, fitting the shared EDS connective-tissue fragility mechanism (chiarelli2019cellularandmolecular pages 3-5) |
| Include core | Vascular Ehlers-Danlos syndrome (vEDS) | COL3A1; type III collagen / vascular wall fragility | Core 2017 EDS subtype with arterial and organ fragility; mechanistically central to the collagen-primary-structure branch and a major real-world surveillance/management target (chiarelli2019cellularandmolecular pages 3-5, buso2024currentevidenceand pages 1-2) |
| Include core | Hypermobile Ehlers-Danlos syndrome (hEDS) | Molecular basis unresolved; clinical EDS subtype | Included because it is an explicit EDS subtype in the modern classification even though no monogenic cause is established; should not be replaced by nonsyndromic hypermobility/HSD (zschocke2024geneticdiagnosisof pages 1-2) |
| Include core | Classical-like Ehlers-Danlos syndrome, TNXB-related (clEDS1) | TNXB; tenascin-X / ECM organization | Core monogenic EDS subtype; fits ECM-organization branch rather than primary fibrillar-collagen defect, but still converges on connective-tissue fragility (zoppi2018multifacedrolesof pages 3-5, damme2022theehlers–danlossyndromes pages 2-3) |
| Include core | Classical-like Ehlers-Danlos syndrome type 2, AEBP1-related (clEDS2) | AEBP1; ACLP / collagen fibrillogenesis, ECM organization | High-value inclusion beyond the original 13-type framework: now recognized as an EDS subtype with collagen-binding/ECM roles and reported vascular complications in some patients (chiarelli2019cellularandmolecular pages 3-5, ritelli2019expandingtheclinical pages 1-3) |
| Include core | Cardiac-valvular Ehlers-Danlos syndrome (cvEDS) | COL1A2; absent pro-α2(I), α1(I) homotrimers | Explicit EDS subtype with type I collagen mechanism and distinctive valvular phenotype; belongs in curated EDS union (zoppi2018multifacedrolesof pages 3-5, damme2022theehlers–danlossyndromes pages 2-3) |
| Include core | Arthrochalasia Ehlers-Danlos syndrome (aEDS) | COL1A1, COL1A2; exon 6 skipping / N-propeptide retention | Explicit EDS subtype with distinctive type I procollagen processing defect and severe congenital joint laxity (zoppi2018multifacedrolesof pages 3-5, damme2022theehlers–danlossyndromes pages 2-3) |
| Include core | Dermatosparaxis Ehlers-Danlos syndrome (dEDS) | ADAMTS2; procollagen N-proteinase / absent N-propeptide cleavage | Explicit EDS subtype in the collagen-processing branch; classic mechanism of abnormal collagen maturation and tissue fragility (zoppi2018multifacedrolesof pages 3-5, damme2022theehlers–danlossyndromes pages 2-3) |
| Include core | Kyphoscoliotic Ehlers-Danlos syndrome, PLOD1-related | PLOD1; lysyl hydroxylase 1 / impaired collagen cross-linking | Explicit EDS subtype in the collagen-folding/cross-linking branch; gene-stratified entry is useful for curation because mechanism differs from FKBP14-kEDS (chiarelli2019cellularandmolecular pages 3-5, damme2022theehlers–danlossyndromes pages 2-3) |
| Include core | Kyphoscoliotic Ehlers-Danlos syndrome, FKBP14-related | FKBP14; FKBP22 collagen chaperone / ER folding defect | Explicit EDS subtype; should be represented separately where the KB supports gene-stratified diseases because the mechanism is collagen chaperoning rather than lysyl hydroxylation (brady2017theehlers–danlossyndromes pages 2-3, damme2022theehlers–danlossyndromes pages 2-3) |
| Include core | Spondylodysplastic Ehlers-Danlos syndrome, B4GALT7-related | B4GALT7; GAG linker-region biosynthesis | Explicit EDS subtype in the proteoglycan/GAG-biosynthesis branch; mechanistically distinct from collagen-gene EDS and should be preserved as a separate subtype entry (ritelli2017expandingtheclinical pages 1-2, damme2022theehlers–danlossyndromes pages 13-15) |
| Include core | Spondylodysplastic Ehlers-Danlos syndrome, B3GALT6-related | B3GALT6; GAG linker-region biosynthesis | Explicit EDS subtype in the same GAG-biosynthesis branch; merits separate inclusion if present because gene-specific disease entries are valuable for mechanism curation (ritelli2017expandingtheclinical pages 1-2, damme2022theehlers–danlossyndromes pages 13-15) |
| Include core | Spondylodysplastic Ehlers-Danlos syndrome, SLC39A13-related | SLC39A13 (ZIP13); intracellular zinc transport affecting ECM/collagen homeostasis | Explicit EDS subtype; preserves the intracellular-process branch within EDS and prevents flattening all spEDS into a purely collagen-centric grouping (chiarelli2019cellularandmolecular pages 3-5, ritelli2017expandingtheclinical pages 1-2) |
| Include core | Musculocontractural Ehlers-Danlos syndrome, CHST14-related | CHST14 (D4ST1); dermatan sulfate biosynthesis / decorin-collagen network | Explicit EDS subtype; key mechanistic exemplar of DS-proteoglycan failure causing collagen-network disorganization and multisystem fragility (yoshizawa2023mousemodelsof pages 1-2, damme2022theehlers–danlossyndromes pages 13-15) |
| Include core | Musculocontractural Ehlers-Danlos syndrome, DSE-related | DSE; dermatan sulfate epimerase / decorin-collagen network | Explicit EDS subtype in the same DS branch; should be represented separately where possible because CHST14 and DSE are nonredundant biochemical steps (yoshizawa2023mousemodelsof pages 1-2, damme2022theehlers–danlossyndromes pages 13-15) |
| Include core | Periodontal Ehlers-Danlos syndrome (pEDS) | C1R, C1S; classical complement pathway / complement-ECM-periodontium link | Explicit EDS subtype and uniquely important because it expands EDS mechanisms beyond collagen/GAG pathways into complement-mediated connective-tissue pathology (kapfererseebacher2016periodontalehlersdanlossyndrome pages 2-3, kapfererseebacher2016periodontalehlersdanlossyndrome pages 1-2) |
| Include core | Myopathic Ehlers-Danlos syndrome (mEDS) | COL12A1; type XII collagen / ECM-myopathy overlap | Explicit EDS subtype; keeps the myomatrix/ECM-overlap branch inside the curated EDS union (zoppi2018multifacedrolesof pages 3-5, damme2022theehlers–danlossyndromes pages 2-3) |
| Conditional | Brittle cornea syndrome (BCS) | ZNF469, PRDM5; ECM/intracellular regulation of connective tissue | Include only if the knowledge base explicitly curates it as an EDS-related disease entry; it is discussed alongside EDS-related disorders but is not always treated as a core EDS subtype (zoppi2018multifacedrolesof pages 3-5, dijk2024clinicaldiagnosisof pages 3-4) |
| Conditional | Other explicit “EDS-related disorder” entries in the KB | Mechanism varies; usually ECM/collagen pathway adjacency | Accept only when the disease entry itself is curated as EDS-related rather than inferred from broad MONDO ancestry; this preserves an explicit curated union boundary (brady2017theehlers–danlossyndromes pages 2-3, dijk2024clinicaldiagnosisof pages 1-2) |
| Exclude | Marfan syndrome | FBN1; fibrillin-1 / aortopathy | Exclude because it is a distinct heritable connective-tissue disorder, not an EDS subtype, despite overlap in skeletal/vascular signs (bowen2023diagnosisandmanagement pages 7-8) |
| Exclude | Loeys-Dietz syndrome | TGFβ-pathway genes; signaling/aortopathy | Exclude because it is a separate syndromic aortopathy with overlapping vascular findings but different nosology and mechanism (bowen2023diagnosisandmanagement pages 7-8) |
| Exclude | Osteogenesis imperfecta (including non-EDS OI entities) | Usually COL1A1/COL1A2 and related bone-fragility pathways | Exclude unless a disease entry is explicitly curated as an EDS overlap; overlap alone is insufficient for EDS grouping membership (damme2022theehlers–danlossyndromes pages 15-16, kapfererseebacher2020dentalmanifestationsof pages 1-2) |
| Exclude | Cutis laxa | Elastic-fiber/ECM disorders distinct from EDS | Exclude because it is a different connective-tissue disorder family, even though there can be skin/ECM overlap (damme2022theehlers–danlossyndromes pages 15-16) |
| Exclude | Arterial tortuosity syndrome | SLC2A10 / ECM-vascular remodeling disorder distinct from EDS | Exclude because it is presented as a separate HCTD, not an EDS subtype, despite some shared vascular/ECM biology (zoppi2018multifacedrolesof pages 3-5) |
| Exclude | Hypermobility spectrum disorder (HSD) / nonsyndromic generalized joint hypermobility | No established monogenic EDS mechanism; symptomatic hypermobility spectrum | Exclude unless the entry is explicitly an EDS diagnosis; recent reviews warn against conflating nonspecific hypermobility with EDS grouping membership (zschocke2024geneticdiagnosisof pages 1-2, morlino2023placingjointhypermobility pages 7-7) |


*Table: This table proposes a defensible curated union for an Ehlers-Danlos syndromes grouping, separating core subtype members from optional EDS-related inclusions and explicit exclusions. It is useful for YAML curation because it anchors membership decisions to subtype labels and shared mechanisms rather than to a broad ontology hierarchy alone.*

---

## 3) Subtype mechanisms and genes (requested subtype set)

### 3.1 Collagen primary structure/processing and fibrillogenesis branch
- **Classical EDS (cEDS)**: primarily **COL5A1/COL5A2 (type V collagen)**; one source notes pathogenic variants in COL5A1/COL5A2 are identified in **>90%** of patients, with rare COL1A1 variants also described. (ritelli2019expandingtheclinical pages 1-3, chiarelli2019cellularandmolecular pages 3-5)
- **Vascular EDS (vEDS)**: **COL3A1 (type III collagen)**; genotype class (dominant-negative vs haploinsufficiency) affects severity and surveillance intensity. (schonherr2024diagnosisofvascular pages 2-3, byers2025vascularehlersdanlossyndrome pages 5-7)
- **Dermatosparaxis EDS (dEDS)**: **ADAMTS2**, a procollagen N-proteinase; absence of N-propeptide cleavage is a defining mechanism. (damme2022theehlers–danlossyndromes pages 2-3)
- **Arthrochalasia EDS (aEDS)**: **COL1A1/COL1A2**; splice/deletion mechanisms leading to abnormal N-propeptide processing (e.g., exon 6-related effects) are highlighted in a review. (damme2022theehlers–danlossyndromes pages 2-3)
- **Cardiac-valvular EDS (cvEDS)**: **COL1A2**; mechanism includes absent pro-α2(I) chains with α1(I) homotrimers and propensity to valve disease. (damme2022theehlers–danlossyndromes pages 2-3)

### 3.2 Collagen folding/crosslinking branch
- **Kyphoscoliotic EDS (kEDS), PLOD1-related**: **PLOD1** (lysyl hydroxylase 1) → deficient lysyl hydroxylation and impaired crosslink formation. (damme2022theehlers–danlossyndromes pages 2-3)
- **Kyphoscoliotic EDS (kEDS), FKBP14-related**: **FKBP14** (collagen chaperone) → ER accumulation/folding defects. (damme2022theehlers–danlossyndromes pages 2-3)

### 3.3 ECM organization/bridging branch
- **Classical-like EDS (clEDS1)**: **TNXB** (tenascin-X). (zoppi2018multifacedrolesof pages 3-5, damme2022theehlers–danlossyndromes pages 2-3)
- **Classical-like EDS type 2 (clEDS2)**: **AEBP1** encoding ACLP, an ECM collagen-associated protein; AEBP1 alterations are presented as defining a new EDS subtype and support a collagen fibrillogenesis/ECM organization mechanism. (ritelli2019expandingtheclinical pages 1-3, damme2022theehlers–danlossyndromes pages 15-16)
- **Myopathic EDS (mEDS)**: **COL12A1** (type XII collagen), described as an ECM-related myopathy/EDS overlap mechanism. (damme2022theehlers–danlossyndromes pages 2-3, zoppi2018multifacedrolesof pages 3-5)

### 3.4 GAG/proteoglycan biosynthesis branch
- **Spondylodysplastic EDS (spEDS)**: biallelic variants in **B4GALT7**, **B3GALT6** (Golgi linker-region galactosyltransferases for proteoglycans), and **SLC39A13 (ZIP13)** (zinc influx regulator), creating a mechanistically heterogeneous subtype group (GAG linker biosynthesis vs intracellular metal homeostasis). (ritelli2017expandingtheclinical pages 1-2)
- **Musculocontractural EDS (mcEDS)**: **CHST14 (D4ST1)** or **DSE** disrupt **dermatan sulfate (DS) biosynthesis**; DS-containing proteoglycans (decorin/biglycan) normally bridge collagen fibrils, so DS depletion yields collagen network disorganization and fragility. Mouse models (Chst14−/−, Dse−/−) recapitulate key phenotypes including skin fragility and deformed collagen fibrils. (yoshizawa2023mousemodelsof pages 1-2)

### 3.5 Complement/vascular wall branch
- **Periodontal EDS (pEDS)** is caused by **heterozygous C1R or C1S variants**, linking a monogenic connective-tissue syndrome with the **classical complement pathway**. In a 2016 AJHG cohort of **19 families (107 individuals)**, variants in **C1R (15 families)** or **C1S (2 families)** were found in **17/19 families**, and the authors emphasize this as a unique link between connective-tissue pathology and complement biology. Variants cluster in interaction/stabilizing domains and are associated with intracellular retention/ER changes, supporting altered protein folding/assembly rather than simple catalytic loss. (kapfererseebacher2016periodontalehlersdanlossyndrome pages 2-3, kapfererseebacher2016periodontalehlersdanlossyndrome pages 1-2)

| EDS subtype | Gene(s) | Primary mechanistic category | Key differentiating phenotypes | Recommended diagnostic approach | Key supporting citations |
|---|---|---|---|---|---|
| Classical EDS (cEDS) | COL5A1, COL5A2; rare COL1A1 | Collagen primary structure/processing | Skin hyperextensibility with atrophic scarring, generalized joint hypermobility, abnormal wound healing; type V collagen-related ECM disarray | Clinical suspicion followed by targeted monogenic EDS gene panel / sequencing; molecular confirmation expected in most cases | (zschocke2024geneticdiagnosisof pages 1-2, zoppi2018multifacedrolesof pages 3-5, ritelli2019expandingtheclinical pages 1-3, dijk2024clinicaldiagnosisof pages 1-2) |
| Vascular EDS (vEDS) | COL3A1 | Collagen primary structure/processing | Arterial aneurysm/dissection/rupture, bowel or uterine rupture, thin translucent skin, characteristic facial appearance; severity varies by variant class/location | Strong clinical suspicion plus COL3A1-inclusive gene panel/NGS with CNV analysis; surveillance begins after confirmation | (buso2024currentevidenceand pages 1-2, buso2024despiteceliprololtherapy pages 4-6, zoppi2018multifacedrolesof pages 3-5, schonherr2024diagnosisofvascular pages 2-3, bowen2023diagnosisandmanagement pages 8-11) |
| Hypermobile EDS (hEDS) | Unknown | ECM/inflammatory remodeling with unresolved primary cause | Generalized joint hypermobility with multisystem symptoms, chronic pain/fatigue; lacks confirmed monogenic test | Clinical criteria only; genetic testing is not confirmatory and broad panels in nonspecific hypermobility have limited utility | (zschocke2024geneticdiagnosisof pages 1-2, chiarelli2019cellularandmolecular pages 3-5, chiarelli2019cellularandmolecular pages 1-3) |
| Classical-like EDS type 1 (clEDS1) | TNXB | ECM organization | Marked skin hyperextensibility, easy bruising, joint laxity; typically lacks atrophic scarring compared with cEDS | Clinical suspicion followed by monogenic EDS panel; may require attention to technically challenging TNXB region | (zoppi2018multifacedrolesof pages 3-5, ritelli2019expandingtheclinical pages 1-3, damme2022theehlers–danlossyndromes pages 2-3, zschocke2024geneticdiagnosisof pages 8-9) |
| Classical-like EDS type 2 (clEDS2) | AEBP1 | ECM organization | cEDS-like phenotype with hyperextensible skin, atrophic scars, generalized joint hypermobility; some reported vascular complications; collagen fibrillogenesis defects | Gene panel / sequencing when cEDS-like phenotype is unexplained by COL5A1/COL5A2/TNXB | (chiarelli2019cellularandmolecular pages 3-5, damme2022theehlers–danlossyndromes pages 15-16, ritelli2019expandingtheclinical pages 1-3) |
| Kyphoscoliotic EDS, PLOD1-related | PLOD1 | Folding/crosslinking | Congenital/early kyphoscoliosis, hypotonia, generalized joint hypermobility, tissue fragility from defective lysyl hydroxylation/crosslinks | Clinical suspicion plus gene panel; duplication-sensitive methods may be needed for recurrent exon duplications | (damme2022theehlers–danlossyndromes pages 2-3, dijk2024clinicaldiagnosisof pages 1-2, zschocke2024geneticdiagnosisof pages 8-9) |
| Kyphoscoliotic EDS, FKBP14-related | FKBP14 | Folding/crosslinking | Kyphoscoliosis with hypotonia and joint hypermobility, often hearing loss; collagen-chaperone/ER-folding defect | Clinical suspicion plus gene panel / sequencing | (damme2022theehlers–danlossyndromes pages 2-3, dijk2024clinicaldiagnosisof pages 1-2) |
| Dermatosparaxis EDS (dEDS) | ADAMTS2 | Collagen primary structure/processing | Severe skin fragility with defective procollagen N-propeptide cleavage and abnormal collagen maturation | Clinical suspicion plus gene panel / sequencing | (zoppi2018multifacedrolesof pages 3-5, damme2022theehlers–danlossyndromes pages 2-3, dijk2024clinicaldiagnosisof pages 3-4) |
| Arthrochalasia EDS (aEDS) | COL1A1, COL1A2 | Collagen primary structure/processing | Severe generalized joint hypermobility with congenital bilateral hip dislocation; exon 6 skipping/N-propeptide retention | Clinical suspicion plus gene panel / sequencing | (zoppi2018multifacedrolesof pages 3-5, damme2022theehlers–danlossyndromes pages 2-3) |
| Cardiac-valvular EDS (cvEDS) | COL1A2 | Collagen primary structure/processing | Severe progressive cardiac valvular disease with type I collagen abnormality; α1(I) homotrimer mechanism | Clinical suspicion plus gene panel / sequencing | (zoppi2018multifacedrolesof pages 3-5, damme2022theehlers–danlossyndromes pages 2-3) |
| Spondylodysplastic EDS (spEDS) | B4GALT7, B3GALT6, SLC39A13 | GAG biosynthesis / intracellular | Short stature, muscle hypotonia, radiographic abnormalities, skin hyperextensibility, facial dysmorphism, joint laxity; B4GALT7 cases may show radioulnar synostosis/hypermetropia | Clinical suspicion using subtype criteria, but definite diagnosis requires molecular testing with gene panel | (ritelli2017expandingtheclinical pages 1-2, damme2022theehlers–danlossyndromes pages 13-15) |
| Musculocontractural EDS (mcEDS) | CHST14, DSE | GAG biosynthesis | Congenital malformations with progressive connective-tissue fragility, recurrent dislocations/deformities, skin fragility; dermatan sulfate/decorin-collagen network disruption | Clinical suspicion plus gene panel / sequencing; mechanistic support from fibroblast, mouse, and in vitro collagen network models | (yoshizawa2023mousemodelsof pages 1-2, damme2022theehlers–danlossyndromes pages 13-15) |
| Periodontal EDS (pEDS) | C1R, C1S | Complement | Severe early-onset periodontitis, lack of attached gingiva, pretibial hyperpigmentation, easy bruising/fragility; unique complement-pathway EDS | Clinical suspicion from characteristic periodontal phenotype plus gene panel / sequencing | (kapfererseebacher2016periodontalehlersdanlossyndrome pages 2-3, kapfererseebacher2016periodontalehlersdanlossyndrome pages 1-2) |
| Myopathic EDS (mEDS) | COL12A1 | ECM organization | EDS/myopathy overlap with ECM-related myopathic features | Clinical suspicion plus gene panel / sequencing | (zoppi2018multifacedrolesof pages 3-5, damme2022theehlers–danlossyndromes pages 2-3) |


*Table: This table maps the major Ehlers-Danlos syndrome subtypes to genes, mechanistic class, distinguishing phenotypes, and practical diagnostic approach. It is useful for defining subtype-aware curation boundaries and choosing between clinical versus molecular diagnostic workflows.*

---

## 4) Recent developments and latest research (prioritizing 2023–2024)

### 4.1 Diagnostics (panel testing; limitations for hEDS)
2024 diagnostic reviews emphasize:
- **Monogenic EDS**: **gene panel testing with massively parallel sequencing** is the **gold standard** for confirmation, guided by careful clinical phenotyping. (dijk2024clinicaldiagnosisof pages 1-2)
- **hEDS**: no monogenic cause has been identified; hEDS **cannot be confirmed by genetic testing** and broad non-specific “EDS panels” in patients with hypermobility can yield VUS with limited clinical benefit. (zschocke2024geneticdiagnosisof pages 1-2)
- **Targeted/virtual panels** are favored over broad approaches to reduce VUS burden; exome/genome may be reserved for complex/overlapping phenotypes. (zschocke2024geneticdiagnosisof pages 8-9, byers2025vascularehlersdanlossyndrome pages 3-5)

### 4.2 vEDS surveillance and real-world implementation (2023–2024)
- A vascular-surgery perspective notes that surveillance uses **non-invasive imaging (MRA/CTA) and echocardiography**, with **monitoring intervals individualized**, often **1.5–3 years** and spanning **1–5 years** across centers; genotype tailoring is recommended (shorter intervals for dominant-negative glycine substitutions/splice variants; less frequent for haploinsufficiency/null variants with milder phenotypes). (schonherr2024diagnosisofvascular pages 2-3)
- A national UK diagnostic service reports a real-world protocol of **annual whole-body MRA** (thoracic/abdominal aorta, cervical vessels including circle of Willis, to pelvis/upper legs) with targeted CTA sparingly, plus emergency cards and electronic record alerts; it also highlights procedural avoidance (e.g., colonoscopy) because of bowel perforation risk. (bowen2023diagnosisandmanagement pages 8-11)

### 4.3 vEDS epidemiology, natural history, and outcome statistics (2023–2024)
Recent reviews and cohorts report:
- Prevalence estimates for vEDS around **~1/150,000** in one 2024 review. (buso2024currentevidenceand pages 1-2)
- Historically estimated **median life expectancy ~50 years** (also echoed in real-world therapy cohort background). (buso2024currentevidenceand pages 1-2, buso2024despiteceliprololtherapy pages 1-2)
- In a 2024 review, **major complications occur in up to 85% by age 43**, with arterial complication rates reported as ~**1.3 events per 5 years** and organ complication rates ~**1.6 events per 5 years**. (buso2024currentevidenceand pages 1-2)
- UK cohort survival estimates reported **99.1% at 1 year**, **90.5% at 5 years**, **88.2% at 10 years**. (bowen2023diagnosisandmanagement pages 8-11)

### 4.4 Therapeutic evidence (2023–2024 emphasis)
- A 2024 review highlights that the **BBEST randomized trial** showed ~**64% reduction** in arterial rupture/dissection risk with **celiprolol** versus controls; the same review emphasizes that other drugs remain investigational. (buso2024currentevidenceand pages 1-2)
- Real-world evidence: an Italian 12-year referral-center experience (vEDS, N=26) reported **yearly symptomatic vascular event risk 8.8%** despite high celiprolol uptake (80% on 400 mg/day), supporting “reduced but not eliminated risk.” (buso2024despiteceliprololtherapy pages 1-2)
- Observational data from the UK service suggest fewer events/higher survival among patients on long-term beta-blocker and/or ARB therapy compared with untreated individuals, but the authors emphasize limitations of non-randomized comparisons. (bowen2023diagnosisandmanagement pages 8-11, bowen2023diagnosisandmanagement pages 8-8)

### 4.5 Mechanism-oriented experimental/modeling advances (2023–2024)
- mcEDS: mouse-model synthesis supports DS → decorin/biglycan → collagen network mechanism and demonstrates phenotypic recapitulation relevant for therapy development. (yoshizawa2023mousemodelsof pages 1-2)
- vEDS: multi-omics profiling in patient fibroblasts is being used to identify therapeutic targets such as miRNA/ECM organization pathways (proof-of-concept: miR-29b inhibition increased ECM component expression in fibroblasts). (buso2024currentevidenceand pages 1-2)

---

## 5) Current applications and real-world implementations

### 5.1 Clinical pathways and service models
- **Specialized national diagnostic services** (e.g., UK) implement structured imaging surveillance (annual MRA), emergency information cards, cascade testing, and procedure avoidance strategies tailored to vEDS fragility risks. (bowen2023diagnosisandmanagement pages 8-11)
- **Multidisciplinary care** is repeatedly emphasized for vEDS (genetics, cardiology/vascular surgery, surgical teams experienced with tissue friability). (schonherr2024diagnosisofvascular pages 2-3, byers2025vascularehlersdanlossyndrome pages 9-11)

### 5.2 Molecular diagnostics in practice
- Current best practice for monogenic EDS is **phenotype-directed panel testing** rather than indiscriminate broad panels in hypermobility presentations, to reduce VUS burden and focus on clinically actionable diagnoses. (zschocke2024geneticdiagnosisof pages 1-2, zschocke2024geneticdiagnosisof pages 8-9)

---

## 6) Expert opinions / authoritative analyses (high-level synthesis)

### 6.1 Why a curated union (not MONDO subtree cloning) is defensible
Recent diagnostic guidance explicitly warns against conflating nonspecific hypermobility with monogenic EDS and cautions that overly broad gene panels can generate VUS and limited clinical value. This supports an explicit curated-union boundary that:
- includes named EDS subtypes (even when hEDS lacks a gene), and
- excludes adjacent connective-tissue disorders unless explicitly curated as EDS/EDS-related. (zschocke2024geneticdiagnosisof pages 1-2, morlino2023placingjointhypermobility pages 7-7)

### 6.2 Mechanistic pluralism within EDS (collagen-centric models are incomplete)
The pEDS discovery paper positions complement-pathway genes C1R/C1S as causal, emphasizing EDS mechanisms beyond collagen/GAG alone, while mcEDS and spEDS illustrate proteoglycan/GAG-based mechanisms. Together, these argue for a grouping model with multiple mechanism axes rather than a single “collagenopathy” axis. (kapfererseebacher2016periodontalehlersdanlossyndrome pages 2-3, yoshizawa2023mousemodelsof pages 1-2, ritelli2017expandingtheclinical pages 1-2)

---

## 7) Differentiating mechanisms for existing vs high-value missing subtype entries

High-value missing entries (if absent in the knowledge base) include **gene-split diseases** where mechanisms differ despite similar phenotype labels:
- **kEDS-PLOD1** vs **kEDS-FKBP14** (crosslink enzyme vs collagen chaperone). (damme2022theehlers–danlossyndromes pages 2-3)
- **mcEDS-CHST14** vs **mcEDS-DSE** (distinct biochemical steps in DS biosynthesis; nonredundant). (yoshizawa2023mousemodelsof pages 1-2)
- **spEDS-B4GALT7** vs **spEDS-B3GALT6** vs **spEDS-SLC39A13** (GAG linker biosynthesis vs intracellular zinc transport). (ritelli2017expandingtheclinical pages 1-2)
- **clEDS1-TNXB** vs **clEDS2-AEBP1** (ECM organizer vs ACLP/collagen-associated protein). (ritelli2019expandingtheclinical pages 1-3)

These should be represented as distinct disease entries whenever the curation framework allows, because they carry different mechanistic annotations and sometimes different surveillance priorities. (dijk2024clinicaldiagnosisof pages 1-2, zschocke2024geneticdiagnosisof pages 8-9)

---

## 8) MONDO mapping, HPO phenotype criteria, and dismech module conformance

### 8.1 MONDO mapping approach (no invented IDs)
Use **label-based mapping** to MONDO concepts (umbrella “Ehlers-Danlos syndrome” and each subtype label) rather than inventing identifiers. Where gene-split diseases exist, map each gene-specific label individually. This avoids hierarchy cloning and enforces explicit membership. (damme2022theehlers–danlossyndromes pages 1-2, zschocke2024geneticdiagnosisof pages 8-9)

### 8.2 HPO phenotype anchors (grouping-level criteria)
At the grouping level, select a high-level HPO anchor set covering:
- joint hypermobility, skin hyperextensibility/fragility, atrophic scarring, easy bruising (core EDS phenotype space), (damme2022theehlers–danlossyndromes pages 1-2, chiarelli2019cellularandmolecular pages 3-5)
- arterial aneurysm/dissection/rupture and bowel/uterine rupture (vascular/visceral fragility), (byers2025vascularehlersdanlossyndrome pages 1-3, schonherr2024diagnosisofvascular pages 1-2)
- early-onset periodontitis / absence of attached gingiva (pEDS defining), (kapfererseebacher2016periodontalehlersdanlossyndrome pages 1-2)
- kyphoscoliosis (kEDS), congenital hip dislocation (aEDS), short stature (spEDS). (damme2022theehlers–danlossyndromes pages 2-3, ritelli2017expandingtheclinical pages 1-2)

### 8.3 DisMech module conformance criteria and gaps
Key conformance points and expected gaps:
- **hEDS**: mechanism/gene is unknown; cannot conform to “gene-required” rules but should remain in the grouping as an explicit EDS entity. (zschocke2024geneticdiagnosisof pages 1-2)
- **Complement mechanism**: ensure the data model supports pEDS’s non-collagen mechanism class. (kapfererseebacher2016periodontalehlersdanlossyndrome pages 2-3)
- **Gene-split subtypes**: ensure representation of gene-split forms for mechanistic clarity (kEDS, mcEDS, spEDS, clEDS). (ritelli2017expandingtheclinical pages 1-2, yoshizawa2023mousemodelsof pages 1-2, ritelli2019expandingtheclinical pages 1-3, damme2022theehlers–danlossyndromes pages 2-3)

| YAML field / curation element | Recommended content for EDS grouping | Evidence / rationale summary | Key citations IDs |
|---|---|---|---|
| grouping_name | `Ehlers-Danlos syndromes` | Use the explicit disease-group label used in clinical/research literature; the group should be treated as a curated union of disease entries, not as a generic connective-tissue bucket or automatic ontology subtree. | (chiarelli2019cellularandmolecular pages 3-5, dijk2024clinicaldiagnosisof pages 1-2) |
| description | `Curated union of Ehlers-Danlos syndrome (EDS) disease entries characterized by combinations of generalized tissue fragility, joint hypermobility, skin hyperextensibility/fragility, and subtype-specific complications caused by defects in collagen fibrillogenesis/processing, ECM organization, collagen folding/crosslinking, glycosaminoglycan/proteoglycan biosynthesis, complement pathway biology, or related intracellular connective-tissue homeostasis pathways.` | This wording captures the shared phenotype and the mechanistic breadth of EDS recognized in the 2017 nosology and later reviews. | (chiarelli2019cellularandmolecular pages 3-5, damme2022theehlers–danlossyndromes pages 1-2, zoppi2018multifacedrolesof pages 3-5) |
| grouping_boundary_rule | `Include only diseases explicitly curated as Ehlers-Danlos syndrome subtypes or explicit EDS-related entries in the knowledge base; do not clone an entire MONDO hierarchy or include non-EDS connective-tissue disorders solely on phenotypic overlap.` | Prevents over-inclusion of Marfan/LDS/OI/HSD and preserves a defensible disease-grouping boundary. | (brady2017theehlers–danlossyndromes pages 2-3, bowen2023diagnosisandmanagement pages 7-8, zschocke2024geneticdiagnosisof pages 1-2) |
| included_diseases | Include core entries, if present: classical EDS; vascular EDS; hypermobile EDS; classical-like EDS (TNXB-related); classical-like EDS type 2 / AEBP1-related EDS; cardiac-valvular EDS; arthrochalasia EDS; dermatosparaxis EDS; kyphoscoliotic EDS (PLOD1-related and FKBP14-related); spondylodysplastic EDS (B4GALT7-, B3GALT6-, SLC39A13-related); musculocontractural EDS (CHST14-, DSE-related); periodontal EDS; myopathic EDS. | These are the principal EDS disease entities supported by the 2017 nosology and later additions such as AEBP1-related clEDS2. Gene-split members are especially important for mechanism-aware curation. | (chiarelli2019cellularandmolecular pages 3-5, brady2017theehlers–danlossyndromes pages 2-3, ritelli2019expandingtheclinical pages 1-3, damme2022theehlers–danlossyndromes pages 2-3) |
| conditional_inclusions | `Include only if explicitly represented as EDS-related disease entries:` brittle cornea syndrome and other nosology-adjacent “EDS-related disorders”. | Some disorders are discussed adjacent to EDS but are not core EDS subtypes; they should only enter the grouping if the KB itself curates them as EDS-related disease entries. | (zoppi2018multifacedrolesof pages 3-5, dijk2024clinicaldiagnosisof pages 3-4) |
| excluded_diseases | Exclude: Marfan syndrome; Loeys-Dietz syndrome; osteogenesis imperfecta except explicit EDS-overlap entries; cutis laxa; arterial tortuosity syndrome; nonsyndromic generalized joint hypermobility; hypermobility spectrum disorder unless the entry is explicitly an EDS diagnosis. | These conditions overlap clinically but are distinct disorders/mechanisms and would dilute EDS-specific mechanistic coherence if included automatically. | (bowen2023diagnosisandmanagement pages 7-8, damme2022theehlers–danlossyndromes pages 15-16, zschocke2024geneticdiagnosisof pages 1-2) |
| mondo_mappings | Map by MONDO concept **labels**, not invented IDs: `Ehlers-Danlos syndrome` as the umbrella label plus label-based mappings to each included subtype entry (e.g., `classical Ehlers-Danlos syndrome`, `vascular Ehlers-Danlos syndrome`, `periodontal Ehlers-Danlos syndrome`, etc.). Prefer exact label matching to curated disease entries; where multiple gene-split entries exist, map each split disease label individually. | The user requested no invented MONDO IDs. Label-based mapping preserves compatibility with ontology-backed systems while avoiding speculative identifiers. | (chiarelli2019cellularandmolecular pages 3-5, dijk2024clinicaldiagnosisof pages 1-2) |
| phenotype_criteria_HPO | Use a high-level HPO anchor set including concept labels for: joint hypermobility; skin hyperextensibility; atrophic scarring; easy bruising; arterial aneurysm; arterial dissection; arterial rupture; early-onset periodontitis; lack of attached gingiva / gingival fragility; kyphoscoliosis; congenital hip dislocation; short stature. Add subtype-specific phenotype tags where needed (e.g., thin translucent skin, bowel perforation, hypotonia, radioulnar synostosis). | These phenotypes differentiate core EDS presentations across the major mechanistic branches and are repeatedly highlighted in recent clinical/diagnostic reviews. | (kapfererseebacher2016periodontalehlersdanlossyndrome pages 1-2, ritelli2017expandingtheclinical pages 1-2, damme2022theehlers–danlossyndromes pages 2-3, byers2025vascularehlersdanlossyndrome pages 1-3, schonherr2024diagnosisofvascular pages 1-2) |
| phenotype_logic | `Require at least one shared connective-tissue fragility feature plus subtype-defining features when assigning diseases to the grouping.` Example shared anchors: joint hypermobility, skin fragility/hyperextensibility, tissue/vascular fragility. | This helps prevent inclusion of unrelated diseases with only one superficial overlap feature and keeps the grouping aligned to EDS biology. | (chiarelli2019cellularandmolecular pages 3-5, damme2022theehlers–danlossyndromes pages 1-2, dijk2024clinicaldiagnosisof pages 1-2) |
| mechanism_axes | Encode one or more mechanism axes per disease: `collagen_primary_structure_processing`; `collagen_folding_crosslinking`; `ECM_organization`; `GAG_proteoglycan_biosynthesis`; `complement_pathway`; `intracellular_connective_tissue_homeostasis`. | These axes reflect the accepted mechanistic partitions across monogenic EDS types and allow grouping-wide reasoning without collapsing subtype differences. | (chiarelli2019cellularandmolecular pages 3-5, damme2022theehlers–danlossyndromes pages 1-2, zoppi2018multifacedrolesof pages 3-5) |
| mechanism_axis_examples | Examples: cEDS/vEDS/aEDS/dEDS/cvEDS → collagen primary structure/processing; kEDS-PLOD1/FKBP14 → folding/crosslinking; TNXB/AEBP1/COL12A1 → ECM organization; spEDS/mcEDS → GAG/proteoglycan biosynthesis; pEDS → complement pathway; SLC39A13 also touches intracellular homeostasis. | These examples operationalize the mechanism model for YAML curation and quality checking. | (damme2022theehlers–danlossyndromes pages 15-16, damme2022theehlers–danlossyndromes pages 13-15, yoshizawa2023mousemodelsof pages 1-2, chiarelli2019cellularandmolecular pages 3-5, damme2022theehlers–danlossyndromes pages 2-3) |
| evidence_fields | Recommended fields: `primary_literature`, `authoritative_review`, `recent_clinical_review`, `recent_natural_history_or_cohort`, `diagnostic_guidance`, `mechanism_summary`, `model_system_evidence`, `notes_on_therapeutic_evidence`. | EDS evidence spans discovery genetics, mechanistic cell/animal studies, and sparse therapy/surveillance studies; capturing each evidence type is important. | (buso2024currentevidenceand pages 1-2, kapfererseebacher2016periodontalehlersdanlossyndrome pages 2-3, chiarelli2019cellularandmolecular pages 3-5, yoshizawa2023mousemodelsof pages 1-2, zschocke2024geneticdiagnosisof pages 1-2) |
| diagnostic_notes | `Monogenic EDS:` gene-panel testing with massively parallel sequencing is the current gold standard; prefer targeted/virtual panels to reduce VUS burden. `hEDS:` retain as a clinical EDS entry but annotate that no monogenic confirmatory test exists currently. | This is one of the most important practical distinctions for module consumers. | (zschocke2024geneticdiagnosisof pages 1-2, dijk2024clinicaldiagnosisof pages 1-2, zschocke2024geneticdiagnosisof pages 8-9) |
| surveillance_notes | Add grouping-level note that surveillance is subtype-dependent, especially for vEDS; examples include baseline and longitudinal non-invasive arterial imaging (MRA/CTA, echocardiography) for vascular-risk subtypes. | Not all EDS types need the same surveillance; vEDS is the most developed example and should not be generalized indiscriminately. | (schonherr2024diagnosisofvascular pages 2-3, bowen2023diagnosisandmanagement pages 8-11, buso2024currentevidenceand pages 10-12) |
| quality_checks | Check that every included disease is either explicitly labeled as an EDS subtype or explicitly curated as EDS-related; has at least one supported mechanism axis; has at least one defining phenotype anchor; and is not included solely because of hypermobility or broad connective-tissue overlap. | These checks enforce the non-hierarchy-clone requirement and improve mechanistic consistency. | (brady2017theehlers–danlossyndromes pages 2-3, chiarelli2019cellularandmolecular pages 3-5, zschocke2024geneticdiagnosisof pages 1-2) |
| module_conformance_gap_gene_splits | Flag missing gene-split diseases where relevant: kEDS-PLOD1 vs kEDS-FKBP14; mcEDS-CHST14 vs mcEDS-DSE; spEDS-B4GALT7 vs spEDS-B3GALT6 vs spEDS-SLC39A13; clEDS1-TNXB vs clEDS2-AEBP1. | These splits carry distinct mechanisms and should not be flattened if the KB can represent them separately. | (ritelli2017expandingtheclinical pages 1-2, yoshizawa2023mousemodelsof pages 1-2, ritelli2019expandingtheclinical pages 1-3, damme2022theehlers–danlossyndromes pages 2-3) |
| module_conformance_gap_complement | Flag whether the data model can represent a non-collagen EDS branch driven by complement biology (periodontal EDS, C1R/C1S). | pEDS is a key exception to collagen-centric EDS models and should be explicitly represented. | (kapfererseebacher2016periodontalehlersdanlossyndrome pages 2-3, kapfererseebacher2016periodontalehlersdanlossyndrome pages 1-2) |
| module_conformance_gap_hEDS | Flag that hEDS lacks a confirmed gene and therefore cannot conform to a strictly monogenic/gene-required module rule. | The grouping should support clinically defined disease entries alongside monogenic entries. | (zschocke2024geneticdiagnosisof pages 1-2, dijk2024clinicaldiagnosisof pages 1-2) |
| module_conformance_gap_related_disorders | Flag ambiguity around brittle cornea syndrome and other EDS-adjacent entries; require explicit curation status before inclusion. | Prevents accidental expansion of the grouping into a generic rare connective-tissue supergroup. | (zoppi2018multifacedrolesof pages 3-5, dijk2024clinicaldiagnosisof pages 3-4) |
| curation_priority_notes | Highest-value near-term curation priorities: ensure explicit representation of pEDS, gene-split spEDS/kEDS/mcEDS entries, and AEBP1-related clEDS2; ensure vEDS has phenotype and surveillance annotations. | These areas most strongly affect mechanistic completeness and real-world clinical utility. | (buso2024despiteceliprololtherapy pages 4-6, kapfererseebacher2016periodontalehlersdanlossyndrome pages 2-3, ritelli2017expandingtheclinical pages 1-2, yoshizawa2023mousemodelsof pages 1-2, ritelli2019expandingtheclinical pages 1-3) |


*Table: This table provides field-by-field guidance for constructing a dismech grouping YAML for Ehlers-Danlos syndromes. It emphasizes explicit curated membership, mechanism-aware modeling, phenotype anchors, and known module gaps such as hEDS non-monogenic status and missing complement-pathway representation.*

---

## 9) Knowledge gaps and model-system limitations (connective tissue, vascular rupture, therapy evidence)

1. **Therapeutic evidence is sparse**, particularly outside vEDS; even in vEDS, celiprolol is the only drug supported by randomized trial evidence, while observational BB/ARB comparisons are confounded. Residual risk persists despite celiprolol (8.8%/year symptomatic events in one real-world cohort). (buso2024currentevidenceand pages 1-2, buso2024despiteceliprololtherapy pages 1-2)
2. **Surveillance protocols lack consensus**: GeneReviews-style guidance and vascular-surgery reviews note variability and absence of definitive evidence for optimal screening strategies; practice varies by center and genotype. (byers2025vascularehlersdanlossyndrome pages 9-11, schonherr2024diagnosisofvascular pages 2-3)
3. **Model limitations**: fibroblast/dermal ECM models capture ECM remodeling signals but cannot fully reproduce arterial-wall biomechanics and rupture triggers; mouse models recapitulate some DS-pathway phenotypes yet species differences and severity profiles complicate translation. (yoshizawa2023mousemodelsof pages 1-2, chiarelli2019cellularandmolecular pages 3-5)
4. **hEDS molecular etiology remains unresolved**, limiting mechanistic anchoring and targeted therapy development; evidence suggests downstream ECM/inflammatory remodeling but not a singular causal gene. (zschocke2024geneticdiagnosisof pages 1-2, chiarelli2019cellularandmolecular pages 3-5)
5. **pEDS mechanism is incompletely linked to systemic complement activation**: pEDS shows a clear genetic link to complement components, but some reports note no consistent alterations in classical pathway activation assays, consistent with local/tissue-specific or structural/trafficking mechanisms rather than systemic hyperactivation alone. (kapfererseebacher2016periodontalehlersdanlossyndrome pages 5-6, kapfererseebacher2016periodontalehlersdanlossyndrome pages 3-5)

---

## 10) Source index (URLs and publication dates)
*Note:* The tool-retrieved texts frequently did not expose PMID metadata in-line; therefore this report provides **DOIs/URLs and publication months/years**. PMIDs should be added during final curation by cross-checking PubMed for each DOI/title.

Recent (2023–2024 prioritized):
- Bowen et al. **Mar 2023**. *Diagnosis and management of vascular Ehlers-Danlos syndrome: Experience of the UK national diagnostic service, Sheffield.* Eur J Hum Genet. https://doi.org/10.1038/s41431-023-01343-7 (bowen2023diagnosisandmanagement pages 8-11)
- Buso et al. **Jul 2024**. *Current evidence and future perspectives in the medical management of vascular Ehlers–Danlos syndrome: Focus on vascular prevention.* J Clin Med. https://doi.org/10.3390/jcm13144255 (buso2024currentevidenceand pages 1-2)
- Buso et al. **Dec 2024**. *Despite celiprolol therapy, patients with vascular Ehlers–Danlos syndrome remain at risk of vascular events…* Vasc Med. https://doi.org/10.1177/1358863x231215330 (buso2024despiteceliprololtherapy pages 1-2)
- Schönherr et al. **Nov 2024**. *Diagnosis of vascular Ehlers Danlos syndrome and management of vascular complications…* Medizinische Genetik. https://doi.org/10.1515/medgen-2024-2053 (schonherr2024diagnosisofvascular pages 2-3)
- Zschocke et al. **Nov 2024**. *Genetic diagnosis of the Ehlers-Danlos syndromes.* Medizinische Genetik. https://doi.org/10.1515/medgen-2024-2061 (zschocke2024geneticdiagnosisof pages 1-2)
- van Dijk et al. **Nov 2024**. *Clinical diagnosis of the monogenic Ehlers-Danlos syndromes.* Medizinische Genetik. https://doi.org/10.1515/medgen-2024-2060 (dijk2024clinicaldiagnosisof pages 1-2)

Primary subtype genetics:
- Kapferer-Seebacher et al. **Oct 2016**. *Periodontal Ehlers-Danlos Syndrome Is Caused by Mutations in C1R and C1S…* Am J Hum Genet. https://doi.org/10.1016/j.ajhg.2016.08.019 (kapfererseebacher2016periodontalehlersdanlossyndrome pages 1-2)
- Ritelli et al. **Sep 2017**. *Expanding the clinical and mutational spectrum of B4GALT7-spondylodysplastic EDS.* Orphanet J Rare Dis. https://doi.org/10.1186/s13023-017-0704-3 (ritelli2017expandingtheclinical pages 1-2)

Mechanistic reviews / model systems:
- Chiarelli et al. **Aug 2019**. *Cellular and Molecular Mechanisms in the Pathogenesis of Classical, Vascular, and Hypermobile EDS.* Genes. https://doi.org/10.3390/genes10080609 (chiarelli2019cellularandmolecular pages 3-5)
- Van Damme et al. **Jan 2022**. *The Ehlers–Danlos Syndromes against the Backdrop of Inborn Errors of Metabolism.* Genes. https://doi.org/10.3390/genes13020265 (damme2022theehlers–danlossyndromes pages 1-2)
- Yoshizawa & Kosho. **Feb 2023**. *Mouse Models of Musculocontractural EDS.* Genes. https://doi.org/10.3390/genes14020436 (yoshizawa2023mousemodelsof pages 1-2)

GeneReviews-style resource (retrieved):
- Byers. **Feb 2025**. *Vascular Ehlers-Danlos syndrome.* (GeneReviews-style content in retrieved text). https://doi.org/10.32388/y374vq (byers2025vascularehlersdanlossyndrome pages 1-3)


References

1. (damme2022theehlers–danlossyndromes pages 1-2): Tim Van Damme, Marlies Colman, Delfien Syx, and Fransiska Malfait. The ehlers–danlos syndromes against the backdrop of inborn errors of metabolism. Genes, 13:265, Jan 2022. URL: https://doi.org/10.3390/genes13020265, doi:10.3390/genes13020265. This article has 21 citations.

2. (chiarelli2019cellularandmolecular pages 3-5): Nicola Chiarelli, Marco Ritelli, Nicoletta Zoppi, and Marina Colombi. Cellular and molecular mechanisms in the pathogenesis of classical, vascular, and hypermobile ehlers‒danlos syndromes. Genes, 10:609, Aug 2019. URL: https://doi.org/10.3390/genes10080609, doi:10.3390/genes10080609. This article has 91 citations.

3. (zoppi2018multifacedrolesof pages 3-5): Nicoletta Zoppi, Nicola Chiarelli, Marco Ritelli, and Marina Colombi. Multifaced roles of the αvβ3 integrin in ehlers–danlos and arterial tortuosity syndromes’ dermal fibroblasts. International Journal of Molecular Sciences, 19:982, Mar 2018. URL: https://doi.org/10.3390/ijms19040982, doi:10.3390/ijms19040982. This article has 50 citations.

4. (damme2022theehlers–danlossyndromes pages 2-3): Tim Van Damme, Marlies Colman, Delfien Syx, and Fransiska Malfait. The ehlers–danlos syndromes against the backdrop of inborn errors of metabolism. Genes, 13:265, Jan 2022. URL: https://doi.org/10.3390/genes13020265, doi:10.3390/genes13020265. This article has 21 citations.

5. (damme2022theehlers–danlossyndromes pages 15-16): Tim Van Damme, Marlies Colman, Delfien Syx, and Fransiska Malfait. The ehlers–danlos syndromes against the backdrop of inborn errors of metabolism. Genes, 13:265, Jan 2022. URL: https://doi.org/10.3390/genes13020265, doi:10.3390/genes13020265. This article has 21 citations.

6. (damme2022theehlers–danlossyndromes pages 13-15): Tim Van Damme, Marlies Colman, Delfien Syx, and Fransiska Malfait. The ehlers–danlos syndromes against the backdrop of inborn errors of metabolism. Genes, 13:265, Jan 2022. URL: https://doi.org/10.3390/genes13020265, doi:10.3390/genes13020265. This article has 21 citations.

7. (yoshizawa2023mousemodelsof pages 1-2): Takahiro Yoshizawa and Tomoki Kosho. Mouse models of musculocontractural ehlers-danlos syndrome. Genes, 14:436, Feb 2023. URL: https://doi.org/10.3390/genes14020436, doi:10.3390/genes14020436. This article has 8 citations.

8. (kapfererseebacher2016periodontalehlersdanlossyndrome pages 2-3): I. Kapferer-Seebacher, M. Pepin, Roland Werner, T. Aitman, A. Nordgren, H. Stoiber, N. Thielens, C. Gaboriaud, A. Amberger, A. Schossig, R. Gruber, C. Giunta, M. Bamshad, E. Björck, Christina Chen, D. Chitayat, M. Dorschner, Marcus Schmitt-Egenolf, Christopher J. Hale, D. Hanna, H. Hennies, Irene Heiss-Kisielewsky, A. Lindstrand, P. Lundberg, A. Mitchell, D. Nickerson, E. Reinstein, M. Rohrbach, N. Romani, M. Schmuth, R. Silver, F. Taylan, A. Vandersteen, J. Vandrovcova, R. Weerakkody, Margaret Yang, F. Pope, Kirk Zoltan Joszef Herbert Hady James K. Charles N. Usc Aleck Banki Dudas Dumfahrt Haririan Hartsfield Kag, K. Aleck, Z. Bánki, J. Dudas, H. Dumfahrt, H. Haririan, J. Hartsfield, C. Kagen, Uschi Lindert, T. Meitinger, W. Posch, C. Pritz, D. Ross, R. Schroer, G. Wick, R. Wildin, D. Wilflingseder, P. Byers, and J. Zschocke. Periodontal ehlers-danlos syndrome is caused by mutations in c1r and c1s, which encode subcomponents c1r and c1s of complement. American Journal of Human Genetics, 99:1005-1014, Oct 2016. URL: https://doi.org/10.1016/j.ajhg.2016.08.019, doi:10.1016/j.ajhg.2016.08.019. This article has 146 citations and is from a highest quality peer-reviewed journal.

9. (kapfererseebacher2016periodontalehlersdanlossyndrome pages 1-2): I. Kapferer-Seebacher, M. Pepin, Roland Werner, T. Aitman, A. Nordgren, H. Stoiber, N. Thielens, C. Gaboriaud, A. Amberger, A. Schossig, R. Gruber, C. Giunta, M. Bamshad, E. Björck, Christina Chen, D. Chitayat, M. Dorschner, Marcus Schmitt-Egenolf, Christopher J. Hale, D. Hanna, H. Hennies, Irene Heiss-Kisielewsky, A. Lindstrand, P. Lundberg, A. Mitchell, D. Nickerson, E. Reinstein, M. Rohrbach, N. Romani, M. Schmuth, R. Silver, F. Taylan, A. Vandersteen, J. Vandrovcova, R. Weerakkody, Margaret Yang, F. Pope, Kirk Zoltan Joszef Herbert Hady James K. Charles N. Usc Aleck Banki Dudas Dumfahrt Haririan Hartsfield Kag, K. Aleck, Z. Bánki, J. Dudas, H. Dumfahrt, H. Haririan, J. Hartsfield, C. Kagen, Uschi Lindert, T. Meitinger, W. Posch, C. Pritz, D. Ross, R. Schroer, G. Wick, R. Wildin, D. Wilflingseder, P. Byers, and J. Zschocke. Periodontal ehlers-danlos syndrome is caused by mutations in c1r and c1s, which encode subcomponents c1r and c1s of complement. American Journal of Human Genetics, 99:1005-1014, Oct 2016. URL: https://doi.org/10.1016/j.ajhg.2016.08.019, doi:10.1016/j.ajhg.2016.08.019. This article has 146 citations and is from a highest quality peer-reviewed journal.

10. (chiarelli2019cellularandmolecular pages 5-7): Nicola Chiarelli, Marco Ritelli, Nicoletta Zoppi, and Marina Colombi. Cellular and molecular mechanisms in the pathogenesis of classical, vascular, and hypermobile ehlers‒danlos syndromes. Genes, 10:609, Aug 2019. URL: https://doi.org/10.3390/genes10080609, doi:10.3390/genes10080609. This article has 91 citations.

11. (chiarelli2019cellularandmolecular pages 1-3): Nicola Chiarelli, Marco Ritelli, Nicoletta Zoppi, and Marina Colombi. Cellular and molecular mechanisms in the pathogenesis of classical, vascular, and hypermobile ehlers‒danlos syndromes. Genes, 10:609, Aug 2019. URL: https://doi.org/10.3390/genes10080609, doi:10.3390/genes10080609. This article has 91 citations.

12. (ritelli2019expandingtheclinical pages 1-3): Marco Ritelli, Valeria Cinquina, Marina Venturini, Letizia Pezzaioli, Anna Maria Formenti, Nicola Chiarelli, and Marina Colombi. Expanding the clinical and mutational spectrum of recessive aebp1-related classical-like ehlers-danlos syndrome. Genes, 10:135, Feb 2019. URL: https://doi.org/10.3390/genes10020135, doi:10.3390/genes10020135. This article has 48 citations.

13. (dijk2024clinicaldiagnosisof pages 3-4): Fleur S. van Dijk, Chloe Angwin, Serwet Demirdas, Neeti Ghali, and Johannes Zschocke. Clinical diagnosis of the monogenic ehlers-danlos syndromes. Medizinische Genetik, 36:225-234, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2060, doi:10.1515/medgen-2024-2060. This article has 3 citations.

14. (bowen2023diagnosisandmanagement pages 7-8): Jessica M. Bowen, Monica Hernandez, Diana S. Johnson, Claire Green, Tammy Kammin, Duncan Baker, Sylvia Keigwin, Seiko Makino, Naomi Taylor, Oliver Watson, Nigel M. Wheeldon, and Glenda J. Sobey. Diagnosis and management of vascular ehlers-danlos syndrome: experience of the uk national diagnostic service, sheffield. European Journal of Human Genetics, 31:749-760, Mar 2023. URL: https://doi.org/10.1038/s41431-023-01343-7, doi:10.1038/s41431-023-01343-7. This article has 69 citations and is from a domain leading peer-reviewed journal.

15. (kapfererseebacher2020dentalmanifestationsof pages 1-2): I. Kapferer-Seebacher, D. Schnabl, J. Zschocke, and F. Pope. Dental manifestations of ehlers-danlos syndromes: a systematic review. Acta Dermato-Venereologica, 100:adv00092-160, Mar 2020. URL: https://doi.org/10.2340/00015555-3428, doi:10.2340/00015555-3428. This article has 47 citations and is from a domain leading peer-reviewed journal.

16. (zschocke2024geneticdiagnosisof pages 1-2): Johannes Zschocke, Serwet Demirdas, and Fleur S. van Dijk. Genetic diagnosis of the ehlers-danlos syndromes. Medizinische Genetik, 36:235-245, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2061, doi:10.1515/medgen-2024-2061. This article has 5 citations.

17. (morlino2023placingjointhypermobility pages 7-7): Silvia Morlino and Marco Castori. Placing joint hypermobility in context: traits, disorders and syndromes. British Medical Bulletin, 147:90-107, Jun 2023. URL: https://doi.org/10.1093/bmb/ldad013, doi:10.1093/bmb/ldad013. This article has 31 citations and is from a peer-reviewed journal.

18. (buso2024currentevidenceand pages 1-2): Giacomo Buso, Federica Corvini, Elena Maria Fusco, Massimiliano Messina, Fabio Cherubini, Nicola Laera, Anna Paini, Massimo Salvetti, Carolina De Ciuceis, Marco Ritelli, Marina Venturini, Nicola Chiarelli, Marina Colombi, and Maria Lorenza Muiesan. Current evidence and future perspectives in the medical management of vascular ehlers–danlos syndrome: focus on vascular prevention. Journal of Clinical Medicine, 13:4255, Jul 2024. URL: https://doi.org/10.3390/jcm13144255, doi:10.3390/jcm13144255. This article has 12 citations.

19. (brady2017theehlers–danlossyndromes pages 2-3): Angela F. Brady, Serwet Demirdas, Sylvie Fournel‐Gigleux, Neeti Ghali, Cecilia Giunta, Ines Kapferer‐Seebacher, Tomoki Kosho, Roberto Mendoza‐Londono, Michael F. Pope, Marianne Rohrbach, Tim Van Damme, Anthony Vandersteen, Caroline van Mourik, Nicol Voermans, Johannes Zschocke, and Fransiska Malfait. The ehlers–danlos syndromes, rare types. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 175:115-70, Mar 2017. URL: https://doi.org/10.1002/ajmg.c.31550, doi:10.1002/ajmg.c.31550. This article has 313 citations.

20. (ritelli2017expandingtheclinical pages 1-2): Marco Ritelli, Chiara Dordoni, Valeria Cinquina, Marina Venturini, Piergiacomo Calzavara-Pinton, and Marina Colombi. Expanding the clinical and mutational spectrum of b4galt7-spondylodysplastic ehlers-danlos syndrome. Orphanet Journal of Rare Diseases, Sep 2017. URL: https://doi.org/10.1186/s13023-017-0704-3, doi:10.1186/s13023-017-0704-3. This article has 51 citations and is from a peer-reviewed journal.

21. (dijk2024clinicaldiagnosisof pages 1-2): Fleur S. van Dijk, Chloe Angwin, Serwet Demirdas, Neeti Ghali, and Johannes Zschocke. Clinical diagnosis of the monogenic ehlers-danlos syndromes. Medizinische Genetik, 36:225-234, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2060, doi:10.1515/medgen-2024-2060. This article has 3 citations.

22. (schonherr2024diagnosisofvascular pages 2-3): Laura Schönherr, Sabine Wipper, and Yskert von Kodolitsch. Diagnosis of vascular ehlers danlos syndrome and management of vascular complications: a vascular surgeons perspective. Medizinische Genetik, 36:255-259, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2053, doi:10.1515/medgen-2024-2053. This article has 0 citations.

23. (byers2025vascularehlersdanlossyndrome pages 5-7): PH Byers. Vascular ehlers-danlos syndrome. Definitions, Feb 2025. URL: https://doi.org/10.32388/y374vq, doi:10.32388/y374vq. This article has 186 citations.

24. (buso2024despiteceliprololtherapy pages 4-6): Giacomo Buso, Anna Paini, Claudia Agabiti-Rosei, Carolina De Ciuceis, Fabio Bertacchini, Deborah Stassaldi, Massimo Salvetti, Marco Ritelli, Marina Venturini, Marina Colombi, and Maria Lorenza Muiesan. Despite celiprolol therapy, patients with vascular ehlers–danlos syndrome remain at risk of vascular events: a 12-year experience in an italian referral center. Vascular Medicine, 29:265-273, Dec 2024. URL: https://doi.org/10.1177/1358863x231215330, doi:10.1177/1358863x231215330. This article has 15 citations and is from a peer-reviewed journal.

25. (bowen2023diagnosisandmanagement pages 8-11): Jessica M. Bowen, Monica Hernandez, Diana S. Johnson, Claire Green, Tammy Kammin, Duncan Baker, Sylvia Keigwin, Seiko Makino, Naomi Taylor, Oliver Watson, Nigel M. Wheeldon, and Glenda J. Sobey. Diagnosis and management of vascular ehlers-danlos syndrome: experience of the uk national diagnostic service, sheffield. European Journal of Human Genetics, 31:749-760, Mar 2023. URL: https://doi.org/10.1038/s41431-023-01343-7, doi:10.1038/s41431-023-01343-7. This article has 69 citations and is from a domain leading peer-reviewed journal.

26. (zschocke2024geneticdiagnosisof pages 8-9): Johannes Zschocke, Serwet Demirdas, and Fleur S. van Dijk. Genetic diagnosis of the ehlers-danlos syndromes. Medizinische Genetik, 36:235-245, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2061, doi:10.1515/medgen-2024-2061. This article has 5 citations.

27. (byers2025vascularehlersdanlossyndrome pages 3-5): PH Byers. Vascular ehlers-danlos syndrome. Definitions, Feb 2025. URL: https://doi.org/10.32388/y374vq, doi:10.32388/y374vq. This article has 186 citations.

28. (buso2024despiteceliprololtherapy pages 1-2): Giacomo Buso, Anna Paini, Claudia Agabiti-Rosei, Carolina De Ciuceis, Fabio Bertacchini, Deborah Stassaldi, Massimo Salvetti, Marco Ritelli, Marina Venturini, Marina Colombi, and Maria Lorenza Muiesan. Despite celiprolol therapy, patients with vascular ehlers–danlos syndrome remain at risk of vascular events: a 12-year experience in an italian referral center. Vascular Medicine, 29:265-273, Dec 2024. URL: https://doi.org/10.1177/1358863x231215330, doi:10.1177/1358863x231215330. This article has 15 citations and is from a peer-reviewed journal.

29. (bowen2023diagnosisandmanagement pages 8-8): Jessica M. Bowen, Monica Hernandez, Diana S. Johnson, Claire Green, Tammy Kammin, Duncan Baker, Sylvia Keigwin, Seiko Makino, Naomi Taylor, Oliver Watson, Nigel M. Wheeldon, and Glenda J. Sobey. Diagnosis and management of vascular ehlers-danlos syndrome: experience of the uk national diagnostic service, sheffield. European Journal of Human Genetics, 31:749-760, Mar 2023. URL: https://doi.org/10.1038/s41431-023-01343-7, doi:10.1038/s41431-023-01343-7. This article has 69 citations and is from a domain leading peer-reviewed journal.

30. (byers2025vascularehlersdanlossyndrome pages 9-11): PH Byers. Vascular ehlers-danlos syndrome. Definitions, Feb 2025. URL: https://doi.org/10.32388/y374vq, doi:10.32388/y374vq. This article has 186 citations.

31. (byers2025vascularehlersdanlossyndrome pages 1-3): PH Byers. Vascular ehlers-danlos syndrome. Definitions, Feb 2025. URL: https://doi.org/10.32388/y374vq, doi:10.32388/y374vq. This article has 186 citations.

32. (schonherr2024diagnosisofvascular pages 1-2): Laura Schönherr, Sabine Wipper, and Yskert von Kodolitsch. Diagnosis of vascular ehlers danlos syndrome and management of vascular complications: a vascular surgeons perspective. Medizinische Genetik, 36:255-259, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2053, doi:10.1515/medgen-2024-2053. This article has 0 citations.

33. (buso2024currentevidenceand pages 10-12): Giacomo Buso, Federica Corvini, Elena Maria Fusco, Massimiliano Messina, Fabio Cherubini, Nicola Laera, Anna Paini, Massimo Salvetti, Carolina De Ciuceis, Marco Ritelli, Marina Venturini, Nicola Chiarelli, Marina Colombi, and Maria Lorenza Muiesan. Current evidence and future perspectives in the medical management of vascular ehlers–danlos syndrome: focus on vascular prevention. Journal of Clinical Medicine, 13:4255, Jul 2024. URL: https://doi.org/10.3390/jcm13144255, doi:10.3390/jcm13144255. This article has 12 citations.

34. (kapfererseebacher2016periodontalehlersdanlossyndrome pages 5-6): I. Kapferer-Seebacher, M. Pepin, Roland Werner, T. Aitman, A. Nordgren, H. Stoiber, N. Thielens, C. Gaboriaud, A. Amberger, A. Schossig, R. Gruber, C. Giunta, M. Bamshad, E. Björck, Christina Chen, D. Chitayat, M. Dorschner, Marcus Schmitt-Egenolf, Christopher J. Hale, D. Hanna, H. Hennies, Irene Heiss-Kisielewsky, A. Lindstrand, P. Lundberg, A. Mitchell, D. Nickerson, E. Reinstein, M. Rohrbach, N. Romani, M. Schmuth, R. Silver, F. Taylan, A. Vandersteen, J. Vandrovcova, R. Weerakkody, Margaret Yang, F. Pope, Kirk Zoltan Joszef Herbert Hady James K. Charles N. Usc Aleck Banki Dudas Dumfahrt Haririan Hartsfield Kag, K. Aleck, Z. Bánki, J. Dudas, H. Dumfahrt, H. Haririan, J. Hartsfield, C. Kagen, Uschi Lindert, T. Meitinger, W. Posch, C. Pritz, D. Ross, R. Schroer, G. Wick, R. Wildin, D. Wilflingseder, P. Byers, and J. Zschocke. Periodontal ehlers-danlos syndrome is caused by mutations in c1r and c1s, which encode subcomponents c1r and c1s of complement. American Journal of Human Genetics, 99:1005-1014, Oct 2016. URL: https://doi.org/10.1016/j.ajhg.2016.08.019, doi:10.1016/j.ajhg.2016.08.019. This article has 146 citations and is from a highest quality peer-reviewed journal.

35. (kapfererseebacher2016periodontalehlersdanlossyndrome pages 3-5): I. Kapferer-Seebacher, M. Pepin, Roland Werner, T. Aitman, A. Nordgren, H. Stoiber, N. Thielens, C. Gaboriaud, A. Amberger, A. Schossig, R. Gruber, C. Giunta, M. Bamshad, E. Björck, Christina Chen, D. Chitayat, M. Dorschner, Marcus Schmitt-Egenolf, Christopher J. Hale, D. Hanna, H. Hennies, Irene Heiss-Kisielewsky, A. Lindstrand, P. Lundberg, A. Mitchell, D. Nickerson, E. Reinstein, M. Rohrbach, N. Romani, M. Schmuth, R. Silver, F. Taylan, A. Vandersteen, J. Vandrovcova, R. Weerakkody, Margaret Yang, F. Pope, Kirk Zoltan Joszef Herbert Hady James K. Charles N. Usc Aleck Banki Dudas Dumfahrt Haririan Hartsfield Kag, K. Aleck, Z. Bánki, J. Dudas, H. Dumfahrt, H. Haririan, J. Hartsfield, C. Kagen, Uschi Lindert, T. Meitinger, W. Posch, C. Pritz, D. Ross, R. Schroer, G. Wick, R. Wildin, D. Wilflingseder, P. Byers, and J. Zschocke. Periodontal ehlers-danlos syndrome is caused by mutations in c1r and c1s, which encode subcomponents c1r and c1s of complement. American Journal of Human Genetics, 99:1005-1014, Oct 2016. URL: https://doi.org/10.1016/j.ajhg.2016.08.019, doi:10.1016/j.ajhg.2016.08.019. This article has 146 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Ehlers_Danlos_Syndromes-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Ehlers_Danlos_Syndromes-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Ehlers_Danlos_Syndromes-deep-research-falcon_artifacts/artifact-02.md)
