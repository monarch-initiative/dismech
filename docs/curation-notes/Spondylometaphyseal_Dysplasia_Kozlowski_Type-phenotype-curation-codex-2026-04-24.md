# Spondylometaphyseal Dysplasia Kozlowski Type phenotype curation notes

Date: 2026-04-18
Curator: Codex
Target file: `kb/disorders/Spondylometaphyseal_Dysplasia_Kozlowski_Type.yaml`

## Scope

Focused only on the phenotype section. Goal was to keep clinically important
manifestations that could be supported with exact PMID-backed abstract snippets,
add missing phenotype findings that were directly supported, and remove or
soften unsupported claims.

## Phenotypes retained or strengthened

- Disproportionate short-trunk short stature
  - PMID:39825918 supports progression from age 5.
  - PMID:8233993 supports the classic adult height range and that children may
    not be recognized at birth.
- Platyspondyly
  - PMID:41225599 and PMID:39825918 support platyspondyly, with persistent
    severe platyspondyly into later childhood/adulthood.
- Metaphyseal irregularity
  - PMID:19232556 supports mild pelvic metaphyseal abnormalities.
  - PMID:39825918 supports proximal femoral irregularity with later femoral
    head destruction.
- Scoliosis
  - PMID:19232556 and PMID:41225599 support scoliosis as a defining feature.
- Kyphosis
  - PMID:39825918 supports increasing kyphosis with age.
- Brachydactyly
  - PMID:24830047 supports brachydactyly across TRPV4 skeletal dysplasias.
  - PMID:38721578 confirms brachydactyly in an SMDK case.
- Bone pain
  - PMID:39825918 supports onset around age 5 and age-related worsening.

## Phenotypes added

- Pectus carinatum
  - PMID:8233993
- Genu varum
  - PMID:8233993 describes mild bowleg deformity.
- Limitation of joint mobility
  - PMID:8233993 describes limited elbow and hip movement.
  - PMID:38721578 describes knee and elbow contractures in a complicated case.
- Atlantoaxial instability
  - PMID:38721578
- Myelopathy
  - PMID:38721578

## Phenotypes removed or softened

- Removed unsupported frequency qualifiers throughout the phenotype section.
- Removed unsupported `Barrel-Shaped Chest`.
- Removed unsupported `Waddling Gait`.
- Removed unsupported `Short Neck`.
- Removed unsupported `Delayed Ossification of Carpal Bones`.
- Replaced `Hypoplasia of the Odontoid Process` with the directly supported
  complication `Atlantoaxial Instability`.

## Notes

- OMIM/Orphanet comparison suggested additional findings such as carpal
  ossification abnormalities and pelvic/hip features, but these were only kept
  when an exact abstract-backed PMID could support the claim in the disorder
  YAML.
- Frequency and onset were only retained in narrative form when directly
  supported by an abstract snippet.
