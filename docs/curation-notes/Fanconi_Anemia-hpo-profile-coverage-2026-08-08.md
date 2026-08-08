# Fanconi anemia phenotype coverage against the FCF-guideline HPO profile

**Date:** 2026-08-08
**Entry:** `kb/disorders/Fanconi_Anemia.yaml`
**PR:** [monarch-initiative/dismech#8190](https://github.com/monarch-initiative/dismech/pull/8190)
**Feedback to profile authors / schema issue:** [monarch-initiative/dismech#8179](https://github.com/monarch-initiative/dismech/issues/8179)
**Trigger:** Connelly *et al.*, *A custom phenotypic profile for Fanconi anemia: Addressing
gaps in existing disease annotations* (manuscript; profile published at
<https://github.com/ehurwitz/FA-custom-profile>).

## What prompted this

The Connelly manuscript reports a 264-term HPO profile for Fanconi anemia (FA) extracted
from the complete Fanconi Cancer Foundation Clinical Care Guidelines (5th ed., 2020) with
OntoGPT + manual curation. 161 of those terms (61%) are absent from both OMIM (215 terms
across 22 complementation-group entries) and Orphanet (106 terms, ORPHA:84), which
themselves share only 36 terms.

The question asked was whether the dismech FA entry already accounted for those
phenotypes. It did not: the gap fell almost exactly where the manuscript says the
guideline-derived novelty lies.

## Method

The manuscript names only ~29 HPO terms inline, so the comparison was run against the full
profile (`FA-custom-profile.hpoa`, 264 terms) from the repository the paper's data
availability statement points to. Coverage was assessed by HPO closure, not string
matching: for each profile term absent from the entry, we asked whether the entry asserts
an **ancestor** (we cover it, less specifically), a **descendant** (we cover it, more
specifically), or nothing at all.

```
                     before   after
exact match             78     116
parent-only             56      50
child-only              21      22
not represented        109      76
```

(Initial figures were 118/52/21/73; the four-term difference is the review pass
described under "Corrections after review" below.)

## Evidence policy for this pass

**The paper and its `.hpoa` were used only to identify gaps — never as evidence.** Every
phenotype added here carries an independent primary-literature citation with a snippet
verified against the cached PubMed abstract (`just count-verified-snippets`: 388/388).
Where the literature would only support a treatment sequela rather than a disease
phenotype, the term was left uncurated (see "Deliberately not added").

## What was added (41 phenotype blocks)

This table reflects the **final** state after the review pass; two terms curated in the
first draft (recurrent aphthous stomatitis, narrow palpebral fissure) were withdrawn and
the moyamoya and microcornea sources were replaced. See "Corrections after review" below.

| Domain | Terms | Key sources |
|---|---|---|
| Oral / dental | gingivitis, gingival overgrowth, periodontitis, microdontia, tooth agenesis, tooth malposition, hyposalivation, oral ulcer, oral leukoplakia | PMID:17688024, PMID:11759873, PMID:16169820, PMID:18543739, PMID:15139958, PMID:36054728 |
| Psychiatric | anxiety, depression, diminished mental health | PMID:40272053 |
| Endocrine / metabolic | osteoporosis, insulin resistance, GH deficiency | PMID:17426088, PMID:32529760, PMID:25575015 |
| Immune | recurrent infections, reduced NK cell count | PMID:21542827, PMID:24240977, PMID:31990462, PMID:15139958 |
| Haematologic | marrow hypocellularity, neutropenia, petechiae, bruising, transfusional iron overload | PMID:37303314, PMID:39559288, PMID:31990462, PMID:22510772 |
| Cellular | crosslinker-induced chromosomal breakage, DNA repair defect, radiosensitivity | PMID:20301575, PMID:25827349, PMID:21930984 |
| Neoplasm | AML, basal cell carcinoma, oral/oropharyngeal SCC, medulloblastoma, nephroblastoma | PMID:20301575, PMID:38907138, PMID:26484938, PMID:40478605, PMID:26691948 |
| Skeletal / limb | abnormal rib morphology, scapular hypoplasia, radial ray anomaly spectrum, thumb duplication (preaxial polydactyly) | PMID:17006268, PMID:35360980 |
| Ocular | microcornea | PMID:20022637, PMID:23648176 |
| Dermatologic | freckling | PMID:32822789 |
| Other | pulmonary fibrosis, ectopic kidney, moyamoya phenomenon, holoprosencephaly, feeding difficulties | PMID:9096763, PMID:35197271, PMID:38510908, PMID:25719591, PMID:29278735, PMID:20301575 |

Three added terms (`HP:0002745` oral leukoplakia, `HP:0000882` hypoplastic scapulae,
`HP:0040218` reduced total NK cell count) are **not** in the Connelly profile. They were
added because they are what the located evidence actually supports — the profile's
`HP:0000912` Sprengel anomaly, for instance, is not what PMID:17006268 describes (bilateral
scapular hypoplasia with winging), and `HP:0012178` is obsolete in current HPO.

## Deliberately not added

- **Keratoconjunctivitis sicca** (`HP:0001097`) — the one FA cohort that quantifies it
  (PMID:34774576) attributes it to ocular GVHD after HSCT. That is a transplant sequela,
  which the Connelly profile's own inclusion rule excludes.
- **Verrucae** (`HP:0200043`) — the available FA case (PMID:31718429) describes genital
  warts arising three years post-HSCT under multiple immunosuppressants.
- **Melanoma** (`HP:0002861`) — no FA-specific primary source located. The NCI
  non-melanoma skin cancer study (PMID:38907138) is explicitly *non*-melanoma.
- **Frequency bands** were assigned only where a cited percentage maps cleanly onto a
  `FrequencyEnum` band, per `docs/frequency-evidence-guidelines.md`. Osteoporosis carries
  no band: the block now quotes the phenotype-expansion sentence from PMID:17426088, which
  states no rate at all, and the 92% figure in the same paper covers osteopenia *or*
  osteoporosis in patients aged ≥18 rather than osteoporosis across the population.

## Corrections after review (PR #8190)

The automated reviewer raised eight items on the first pass; all were accepted, four of
them changing what is asserted:

- **`HP:0045025` Narrow palpebral fissure — block removed.** The supporting sentence
  measures palpebral fissure *length*, which is `HP:0012745` Short palpebral fissure
  (already asserted in this entry), not fissure *height*. The two terms are not
  ontologically related, so this was a straight term error. `HP:0045025` returns to the
  unevidenced list.
- **`HP:0011107` Recurrent aphthous stomatitis — block removed.** The quoted sentence
  (ulcer healing after transfusion) supports neither recurrence nor stomatitis, and the
  block was redundant with `Oral Ulceration` from the same source.
- **`HP:0011834` Moyamoya phenomenon — evidence replaced.** The original citation
  (PMID:35978939) is an alpha-thalassemia case report naming FA only in a background
  list, which fails this pass's own evidence policy. Replaced with two FA-specific cases
  (PMID:38510908, PMID:25719591), and the category corrected from Cardiac to Neurologic.
- **`HP:0000482` Microcornea — evidence replaced.** The original snippet was truncated to
  dodge a bracket-stripping interaction in the validator and fell below the minimum
  snippet length. Replaced with the NCI ophthalmic cohort (PMID:20022637, microcornea in
  55% of 22 patients) and an independent series (PMID:23648176).

`references_cache/PMID_34774576.md` and `PMID_35978939.md` were removed with the evidence
that cited them; PMID:34774576 is still referenced in prose above as the source for the
keratoconjunctivitis-sicca exclusion, so re-fetch it with `just fetch-reference` if that
term is ever curated.

Two further items were term-precision fixes that preserve profile coverage by closure:
`HP:0000782` → `HP:0000882` Hypoplastic scapulae (exact match to the quoted finding), and
`HP:0010442` → `HP:0001177` Preaxial hand polydactyly (a descendant, so `HP:0010442`
stays covered). Three were name collisions with pre-existing blocks, resolved by renaming
rather than deleting (`Reduced Circulating Growth Hormone Concentration`,
`Early-Onset Osteoporosis`, `Radial Ray Anomaly Spectrum`), with the osteoporosis block
also re-quoted so it no longer reuses a snippet already carried elsewhere in the entry.

## Remaining worklist

The largest surviving cluster is fine-grained **hand/upper-limb radiographic detail**
(absent/small scaphoid and trapezium, carpal bone hypoplasia, forearm bowing, humeral
anomalies, wrist/elbow motion limits). PMID:35360980 characterises the radial ray spectrum
but its abstract does not enumerate individual carpal bones; resolving these needs the
full text of a radiographic series.

The second cluster is **gastrointestinal symptomatology** (GERD, dysphagia, odynophagia,
nausea, constipation, diarrhoea, gastroparesis, malabsorption, abdominal pain). These are
prominent in the FCF guidelines but repeated PubMed searches found no FA-specific primary
study quantifying them; the one cohort that reports a GI figure (PMID:31990462) gives only
"gastrointestinal system abnormality was 5.7%", i.e. structural anomalies, not symptoms.
This looks like a genuine primary-literature gap rather than a search failure, and is
worth flagging back to the profile authors.

## Not represented at all (76)

### Abnormality of limbs (18)

- `HP:0031095` Abnormal humerus morphology
- `HP:0011835` Absent scaphoid
- `HP:0004253` Absent trapezium
- `HP:0001166` Arachnodactyly
- `HP:0005743` Avascular necrosis of the capital femoral epiphysis
- `HP:0003956` Bowed forearm bones
- `HP:0001156` Brachydactyly
- `HP:0001498` Carpal bone hypoplasia
- `HP:0034681` Finger joint contracture
- `HP:0002996` Limited elbow movement
- `HP:0006248` Limited wrist movement
- `HP:0100559` Lower limb asymmetry
- `HP:0006190` Radially deviated wrists
- `HP:0005792` Short humerus
- `HP:0001238` Slender finger
- `HP:0004247` Small scaphoid
- `HP:0004255` Small trapezium
- `HP:0003031` Ulnar bowing

### Abnormality of the digestive system (15)

- `HP:0002027` Abdominal pain
- `HP:0005912` Biliary atresia
- `HP:0002607` Bowel incontinence
- `HP:0002019` Constipation
- `HP:0002014` Diarrhea
- `HP:0002015` Dysphagia
- `HP:0040183` Encopresis
- `HP:0002020` Gastroesophageal reflux
- `HP:0002578` Gastroparesis
- `HP:0005214` Intestinal obstruction
- `HP:0002024` Malabsorption
- `HP:0004395` Malnutrition
- `HP:0030996` Megaduodenum
- `HP:0002018` Nausea
- `HP:0032043` Odynophagia

### Abnormality of head or neck (8)

- `HP:0032154` Aphthous ulcer
- `HP:0011109` Chronic sinusitis
- `HP:0001363` Craniosynostosis
- `HP:0001097` Keratoconjunctivitis sicca
- `HP:0045025` Narrow palpebral fissure
- `HP:0002691` Platybasia
- `HP:0011107` Recurrent aphthous stomatitis
- `HP:0000506` Telecanthus

### Abnormality of the integument (7)

- `HP:0025127` Actinic keratosis
- `HP:0000958` Dry skin
- `HP:0025474` Erythematous plaque
- `HP:0040189` Scaling skin
- `HP:0200036` Skin nodule
- `HP:0001072` Thickened skin
- `HP:0200043` Verrucae

### Abnormality of the nervous system (6)

- `HP:0001331` Absent septum pellucidum
- `HP:0009592` Astrocytoma
- `HP:0002308` Chiari malformation
- `HP:5200320` Diminishment of relationship seeking
- `HP:0012174` Glioblastoma multiforme
- `HP:0003006` Neuroblastoma

### Abnormality of the musculoskeletal system (5)

- `HP:0010305` Absence of the sacrum
- `HP:0008839` Hypoplastic pelvis
- `HP:0004590` Hypoplastic sacrum
- `HP:0000912` Sprengel anomaly
- `HP:0025261` Stiff finger

### Abnormality of the cardiovascular system (5)

- `HP:0031640` Abnormal radial artery morphology
- `HP:0001650` Aortic valve stenosis
- `HP:0011590` Double aortic arch
- `HP:0004935` Pulmonary artery atresia
- `HP:0001642` Pulmonic stenosis

### Growth abnormality (3)

- `HP:0001508` Failure to thrive
- `HP:0025502` Overweight
- `HP:0001518` Small for gestational age

### Abnormality of the ear (3)

- `HP:0001963` Abnormal speech discrimination
- `HP:0040090` Abnormal tympanic membrane morphology
- `HP:0034585` Cochlear nerve hypoplasia

### Neoplasm (1)

- `HP:0002861` Melanoma

### Abnormality of the genitourinary system (1)

- `HP:0008661` Urethral stenosis

### Abnormality of the endocrine system (1)

- `HP:0012285` Abnormal hypothalamus physiology

### Abnormality of prenatal development or birth (1)

- `HP:0034057` Fetal anomaly

### Abnormality of the immune system (1)

- `HP:0410028` Recurrent oral herpes

### Constitutional symptom (1)

- `HP:6000064` Excessive eructation

## Represented only by a broader parent term (50)

- `HP:0010704` 1-2 finger cutaneous syndactyly — entry has `HP:0006101` Finger syndactyly
- `HP:0006482` Abnormal dental morphology — entry has `HP:0000164` Abnormality of the dentition
- `HP:0010461` Abnormality of the male genitalia — entry has `HP:0000078` Abnormality of the genital system
- `HP:0000140` Abnormality of the menstrual cycle — entry has `HP:0000078` Abnormality of the genital system
- `HP:0003974` Absent radius — entry has `HP:0006501` Aplasia/Hypoplasia of the radius
- `HP:0010469` Absent testis — entry has `HP:0000035` Abnormal testis morphology, `HP:0000078` Abnormality of the genital system
- `HP:0000141` Amenorrhea — entry has `HP:0000078` Abnormality of the genital system
- `HP:0009892` Anotia — entry has `HP:0000377` Abnormal pinna morphology
- `HP:0003982` Aplasia of the ulna — entry has `HP:0006495` Aplasia/Hypoplasia of the ulna
- `HP:0000151` Aplasia of the uterus — entry has `HP:0000078` Abnormality of the genital system, `HP:0000130` Abnormality of the uterus
- `HP:0003250` Aplasia of the vagina — entry has `HP:0000078` Abnormality of the genital system
- `HP:0001915` Aplastic anemia — entry has `HP:0001876` Pancytopenia
- `HP:0001638` Cardiomyopathy — entry has `HP:0001627` Abnormal heart morphology
- `HP:0004602` Cervical C2/C3 vertebral fusion — entry has `HP:0002949` Fused cervical vertebrae
- `HP:0030079` Cervix cancer — entry has `HP:0000078` Abnormality of the genital system, `HP:0000130` Abnormality of the uterus
- `HP:0000041` Chordee — entry has `HP:0000078` Abnormality of the genital system
- `HP:0012622` Chronic kidney disease — entry has `HP:0000083` Renal insufficiency
- `HP:0001374` Congenital hip dislocation — entry has `HP:0001385` Hip dysplasia, `HP:0002827` Hip dislocation
- `HP:0000144` Decreased fertility — entry has `HP:0000078` Abnormality of the genital system
- `HP:0000868` Decreased fertility in females — entry has `HP:0000078` Abnormality of the genital system
- `HP:0008734` Decreased testicular size — entry has `HP:0000035` Abnormal testis morphology, `HP:0000078` Abnormality of the genital system
- `HP:0000696` Delayed eruption of permanent teeth — entry has `HP:0000164` Abnormality of the dentition
- `HP:0009603` Deviation of the thumb — entry has `HP:0001172` Abnormal thumb morphology
- `HP:0000819` Diabetes mellitus — entry has `HP:0011014` Abnormal glucose homeostasis
- `HP:0009942` Duplication of thumb phalanx — entry has `HP:0001172` Abnormal thumb morphology
- `HP:0003241` External genital hypoplasia — entry has `HP:0000078` Abnormality of the genital system
- `HP:0000085` Horseshoe kidney — entry has `HP:0012210` Abnormal renal morphology, `HP:0100542` Abnormal localization of kidney
- `HP:0000126` Hydronephrosis — entry has `HP:0012210` Abnormal renal morphology
- `HP:0003074` Hyperglycemia — entry has `HP:0011014` Abnormal glucose homeostasis
- `HP:0000013` Hypoplasia of the uterus — entry has `HP:0000078` Abnormality of the genital system, `HP:0000130` Abnormality of the uterus
- `HP:0040270` Impaired glucose tolerance — entry has `HP:0011014` Abnormal glucose homeostasis
- `HP:0000858` Irregular menstruation — entry has `HP:0000078` Abnormality of the genital system
- `HP:0000132` Menorrhagia — entry has `HP:0000078` Abnormality of the genital system
- `HP:0030260` Microphallus — entry has `HP:0000078` Abnormality of the genital system
- `HP:0000876` Oligomenorrhea — entry has `HP:0000078` Abnormality of the genital system
- `HP:0009944` Partial duplication of thumb phalanx — entry has `HP:0001172` Abnormal thumb morphology
- `HP:0001741` Phimosis — entry has `HP:0000078` Abnormality of the genital system, `HP:0100587` Abnormal preputium morphology
- `HP:0002718` Recurrent bacterial infections — entry has `HP:0002719` Recurrent infections
- `HP:0002841` Recurrent fungal infections — entry has `HP:0002719` Recurrent infections
- `HP:0004429` Recurrent viral infections — entry has `HP:0002719` Recurrent infections
- `HP:0000104` Renal agenesis — entry has `HP:0008678` Renal hypoplasia/aplasia, `HP:0012210` Abnormal renal morphology
- `HP:0000110` Renal dysplasia — entry has `HP:0012210` Abnormal renal morphology
- `HP:0000089` Renal hypoplasia — entry has `HP:0008678` Renal hypoplasia/aplasia, `HP:0012210` Abnormal renal morphology
- `HP:0004712` Renal malrotation — entry has `HP:0012210` Abnormal renal morphology
- `HP:0009660` Short phalanx of the thumb — entry has `HP:0001172` Abnormal thumb morphology, `HP:0006265` Aplasia/Hypoplasia of fingers
- `HP:0009778` Short thumb — entry has `HP:0001172` Abnormal thumb morphology, `HP:0006265` Aplasia/Hypoplasia of fingers
- `HP:0034231` Sigmoid kidney — entry has `HP:0000086` Ectopic kidney, `HP:0012210` Abnormal renal morphology
- `HP:0011069` Supernumerary tooth — entry has `HP:0000164` Abnormality of the dentition
- `HP:0000029` Testicular atrophy — entry has `HP:0000035` Abnormal testis morphology, `HP:0000078` Abnormality of the genital system
- `HP:6000942` Thumb hypoplasia grade 4 — entry has `HP:0001172` Abnormal thumb morphology, `HP:0006265` Aplasia/Hypoplasia of fingers
