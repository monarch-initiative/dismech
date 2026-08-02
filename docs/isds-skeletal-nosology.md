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

## MONDO mappings

No group carries a `meaning:`. A `meaning:` would assert that the value *is*
an ontology class, which is never quite true: the ISDS group is a curated list,
the MONDO class is a defined extension, and the two rarely coincide. Where a
MONDO class denotes the same disease family, it is recorded as
`close_mappings:` instead.

**Three of 42 groups are mapped.** The bar is deliberately high — a candidate
is rejected if the MONDO class contains any entity that ISDS itself lists in a
*different* group, since such a mapping would silently contradict the
committee's own placement:

| Group | MONDO | Why it survives |
|-------|-------|-----------------|
| 1 FGFR3 chondrodysplasia | `MONDO:0019685` FGFR3-related chondrodysplasia | Contains the group's members and, crucially, *excludes* the FGFR3 craniosynostoses (Muenke, Crouzon with acanthosis nigricans) that ISDS puts in group 33 |
| 8 TRPV4 | `MONDO:0018240` TRPV4-related bone disorder | All descendants are group-8 members; parastremmatic dwarfism appears in the group's own SEMD Maroteaux row |
| 16 Acromesomelic dysplasias | `MONDO:0019696` acromesomelic dysplasia | All descendants are either group-16 members or entities ISDS does not list at all |

Rejected candidates, recorded so nobody re-proposes them:

| Group | Rejected MONDO | Straddle |
|-------|----------------|----------|
| 2 | `MONDO:0022800` type 2 collagenopathy | contains SMD 'corner fracture' type (group 12) |
| 15 | `MONDO:0019695` acromelic dysplasia | contains pseudohypoparathyroidism type 1A (group 38), terminal osseous dysplasia (group 7) |
| 23 | `MONDO:0017198` osteopetrosis | contains melorheostosis and osteopathia striata with cranial sclerosis (group 24) |
| 33 | `MONDO:0015338` syndromic craniosynostosis | contains cranioectodermal dysplasia (group 9) |

Groups 10, 19, 21, 25 and 27 have no usable class at all: either the nearest
MONDO term is obsolete (chondrodysplasia punctata) or it is *narrower* than the
ISDS group, which mixes in entities falling outside it — group 25, for
instance, holds cutis laxa and Singleton-Merten alongside osteogenesis
imperfecta.

Note the asymmetry that makes `close_mappings` the right relation: in every
mapped case MONDO is **broader**, because ISDS lists only entities meeting its
inclusion criteria. A mapping is rejected not for breadth but for *crossing*
into another group.

## Entities the nosology lists but declines to decompose

Fanconi anemia is the worked precedent. It is listed in group 39, but it is the
only Table 1 row whose name carries a "(see note below)" pointer and the only
one whose gene column reads "Several" rather than naming loci. The group-39
footnote says the complex genetic basis of Fanconi anemia and its
complementation groups "is acknowledged but not further listed in this
nosology", referring readers to OMIM or specialized reviews.

Read that precisely: the caveat is about **genetic decomposition, not
membership**. The committee does not question whether Fanconi anemia belongs in
the nosology — it lists it in group 39 without qualification on that point, and
its skeletal phenotype (radial ray and thumb reduction defects) is exactly what
group 39 is for. What it declines to do is enumerate FA-A, FA-C, FA-D2 and the
rest.

The curation rule that follows: assign the group to the **entity**, record the
committee's caveat in `notes:`, and do not derive per-complementation-group
placements from Table 1. Apply the same treatment to any future row the
committee flags this way.

## Refreshing to a later revision

The ISDS Nosology is revised every few years (2002, 2007, 2011, 2015, 2019,
2023). The enum is deliberately pinned to a single named revision, with the
revision recorded in the schema description and in every assignment's `notes:`.
When moving to a later edition, add or rename permissible values rather than
silently redefining existing ones, and update the `notes:` template so an
assignment always says which revision it came from — group numbering is not
guaranteed stable across revisions.
