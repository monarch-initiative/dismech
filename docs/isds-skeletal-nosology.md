# ISDS Skeletal-Dysplasia Classification

dismech tags genetic skeletal disorders with their group in the **Nosology and
Classification of Genetic Skeletal Disorders**, the expert-consensus nosology
maintained by the Nosology Committee of the International Skeletal Dysplasia
Society (ISDS). The encoded edition is the **2019 revision** — the tenth — which
lists **461 disorders in 42 groups**:

> Mortier GR, Cohn DH, Cormier-Daire V, Hall C, Krakow D, Mundlos S, Nishimura G,
> Robertson S, Sangiorgi L, Savarirayan R, Sillence D, Superti-Furga A, Unger S,
> Warman ML. *Nosology and classification of genetic skeletal disorders: 2019
> revision.* Am J Med Genet A. 2019;179(12):2393-2419.
> [PMID:31633310](https://pubmed.ncbi.nlm.nih.gov/31633310/),
> [doi:10.1002/ajmg.a.61366](https://doi.org/10.1002/ajmg.a.61366)

| Artifact | Path |
|----------|------|
| LinkML enum (42 groups) | `src/dismech/schema/classifications/isds_skeletal_nosology.yaml` |
| Assignment class | `ISDSNosologyAssignment` in `src/dismech/schema/dismech.yaml` |
| Slot | `classifications.isds_skeletal_category` |
| Curator guidance | `.claude/skills/disease-classification/SKILL.md` |

## What the nosology is

The ISDS Nosology is the reference list of *recognized* genetic skeletal
entities. A disorder is included only if it has significant skeletal
involvement, is published and catalogued (PubMed/OMIM), has a proven genetic
basis, and has **nosologic autonomy** — it is an independent entity rather than
a variant of an existing one. That last criterion is why the nosology is worth
encoding: it is a curated statement about *which skeletal entities are real and
distinct*, not merely a convenient bucketing.

Groups mix organizing principles deliberately:

| Groups | Organizing principle |
|--------|----------------------|
| 1-8 | Shared causal gene or gene family (FGFR3, type 2 / type 11 collagen, sulphation, perlecan, aggrecan, filamin, TRPV4) |
| 9 | Ciliary (skeletal ciliopathies) |
| 10-14 | Radiographic — which segment of the growing bone is affected (epiphyseal, metaphyseal, spondylo-) |
| 15-17 | Limb-segment pattern (acromelic, acromesomelic, mesomelic) |
| 18-21 | Bent bones, primordial dwarfism, joint dislocations, chondrodysplasia punctata |
| 22-26 | Bone density and mineralization (osteosclerosis, osteopetrosis, OI, mineralization) |
| 27-31 | Storage, osteolysis, disorganized development, overgrowth, inflammatory |
| 32-36 | Dysostoses (cleidocranial, craniosynostosis, craniofacial, vertebral/costal, patellar) |
| 37-42 | Limb malformation, reduction defects, synostoses |

Two groups were renamed in the 2019 revision: group 18 became the "Bent bone
dysplasia group" (from "Campomelic dysplasia and related disorders") and group
19 became "Primordial dwarfism and slender bones group" (from "Slender bone
dysplasia group").

## How to assign it

```yaml
classifications:
  harrisons_chapter:
  - classification_value: GENETICS_ENVIRONMENT_DISEASE
  isds_skeletal_category:
  - classification_value: fgfr3_chondrodysplasia
    notes: >-
      ISDS Nosology and Classification of Genetic Skeletal Disorders,
      2019 revision (Mortier et al., PMID:31633310), Table 1 group 1
      "FGFR3 chondrodysplasia group"; listed as "Achondroplasia".
```

Three rules follow from how the nosology is built:

1. **One group per disorder.** The committee lists each disorder exactly once,
   "to avoid redundancy in the Nosology". Overlap between groups is handled by
   Table 1's *see also* cross-references, not by dual membership. The slot is
   multivalued only to accommodate a dismech entry that lumps several distinct
   nosology disorders.
2. **Assign only to listed disorders.** The enum is a transcription of an expert
   nosology, not an inference engine. Many disorders with skeletal phenotypes
   were deliberately excluded (chiefly for lack of *significant* skeletal
   involvement); do not extend the classification to them. An unambiguous
   subtype or synonym of a listed disorder is fine.
3. **Use `notes:`, not `evidence:`.** The paper's PubMed record is abstract-only.
   No exact-quote snippet from the abstract can support a per-disorder group
   placement — the abstract states only that the nosology exists and contains
   461 disorders in 42 groups. Quoting it for a specific assignment would be a
   snippet that does not support its claim. This mirrors the ICIMD convention.

### Cross-group traps

The gene most associated with a disorder is often *not* what decides its group.
Frequently mis-assigned cases:

| Disorder | Correct group | Tempting but wrong |
|----------|---------------|--------------------|
| Crouzon with acanthosis nigricans, Muenke craniosynostosis | 33 (craniosynostosis) | 1 (FGFR3) |
| LADD syndrome | 41 (polydactyly-syndactyly-triphalangism) | 1 (FGFR3) |
| Hajdu-Cheney syndrome | 28 (osteolysis) | 25 (decreased bone density) |
| Brachydactyly-hypertension (Bilginturan) | 38 (brachydactyly with extraskeletal features) | 15 (acromelic) |
| Weyers acrofacial (acrodental) dysostosis | 34 (craniofacial dysostoses) | 9 (skeletal ciliopathies, with Ellis-van Creveld) |
| Spondylodysplastic Ehlers-Danlos syndrome | 13 (SLC39A13) / 25 (B4GALT7) | one group for both |

## Relationship to other classification axes

`isds_skeletal_category` is orthogonal to the other axes and should be set
alongside them, not instead of them:

- `harrisons_chapter` — usually `GENETICS_ENVIRONMENT_DISEASE`.
- `icimd_category` — the storage disorders in ISDS group 27 (dysostosis
  multiplex) are inborn errors of metabolism and also carry an ICIMD group;
  likewise `lysosomal_storage_category`.
- `mechanistic_category` — ISDS group 9 members are ciliopathies, which is a
  mechanism statement rather than a nosology placement.

Groups are **not** ontology-bound. No `meaning:` is asserted, because several
groups have no MONDO equivalent and, where a superficially similar MONDO
grouping term exists, its extension usually differs from the ISDS group's
membership. Asserting an inexact mapping would be worse than asserting none.

## Refreshing to a later revision

The ISDS Nosology is revised every few years (2002, 2007, 2011, 2015, 2019,
2023). The enum is deliberately pinned to a single named revision, with the
revision recorded in the schema description and in every assignment's `notes:`.
When moving to a later edition, add or rename permissible values rather than
silently redefining existing ones, and update the `notes:` template so an
assignment always says which revision it came from — group numbering is not
guaranteed stable across revisions.
