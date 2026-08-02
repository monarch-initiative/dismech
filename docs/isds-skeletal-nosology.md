# ISDS Skeletal-Dysplasia Classification

dismech tags genetic skeletal disorders with their group in the **Nosology of
Genetic Skeletal Disorders**, the expert-consensus nosology maintained by the
Nosology Committee of the International Skeletal Dysplasia Society (ISDS). The
encoded edition is the **2023 revision** — the eleventh — with **771 entries,
552 genes, and 41 groups**:

> Unger S, Ferreira CR, Mortier GR, et al. *Nosology of genetic skeletal
> disorders: 2023 revision.* Am J Med Genet A. 2023;191(5):1164-1209.
> [PMID:36779427](https://pubmed.ncbi.nlm.nih.gov/36779427/),
> [doi:10.1002/ajmg.a.63132](https://doi.org/10.1002/ajmg.a.63132)

It supersedes the **2019 revision** (10th edition; 461 disorders, 437 genes, 42
groups; Mortier et al., [PMID:31633310](https://pubmed.ncbi.nlm.nih.gov/31633310/)),
which dismech encoded first and which is retained as provenance — see
[Revision handling](#revision-handling).

| Artifact | Path |
|----------|------|
| LinkML enum (41 groups + 4 deprecated) | `src/dismech/schema/classifications/isds_skeletal_nosology.yaml` |
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

| Groups (2023) | Organizing principle |
|--------|----------------------|
| 1-8 | Shared causal gene, gene family, or biosynthetic pathway (FGFR3, type 2 / type 11 collagen, sulfation, joint dislocations, filamins, proteoglycan core proteins, TRPV4) |
| 9-14 | Radiographic — which segment of the growing bone is affected (epiphyseal, metaphyseal, spondylo-), plus the skeletal ciliopathies at 10 |
| 15-19 | Limb-segment pattern (mesomelic, acromesomelic, acromelic) and the brachydactylies |
| 20-23 | Bent bones, primordial dwarfism, lysosomal storage, chondrodysplasia punctata |
| 24-28 | Bone density and mineralization (osteopetrosis, osteosclerosis, OI/fragility, mineralization, PTH signaling) |
| 29-32 | Osteolysis, disorganized development, overgrowth, inflammatory |
| 33-37 | Dysostoses (cleidocranial, craniosynostosis, craniofacial, vertebral/costal, patellar) |
| 38-41 | Limb reduction, split hand/foot, polydactyly-syndactyly, synostoses |

## Revision handling

The nosology is revised every few years (2002, 2007, 2011, 2015, 2019, 2023).
dismech tracks it with three LinkML constructs so a revision bump never
invalidates existing annotations:

**Keys are stable identifiers.** A permissible-value key is *not* renamed or
renumbered when a revision renames or renumbers its group — the key identifies
the group across editions, while the revision's own number and name live in the
`description`. Group numbers are emphatically not stable: the brachydactyly
groups moved from 37/38 (2019) to 18/19 (2023), and the lysosomal storage group
from 27 to 22. That is exactly why numbers are not part of any key.

**Superseded names become structured synonyms.** LinkML permissible values
accept `structured_aliases`, so the old name is retained with its predicate and
a `source` citing the revision that used it — a search for the old name still
resolves, and the citation says which edition it came from:

```yaml
craniosynostosis_syndromes:
  structured_aliases:
    - literal_form: Craniosynostosis syndromes
      predicate: EXACT_SYNONYM
      source: PMID:31633310
      description: >-
        Name of this group in the 2019 revision (10th edition), where it was
        group 33.
  description: >-
    Group 34 (2023 revision): Syndromes featuring craniosynostosis. ...
```

38 of the 41 groups carry such an alias. The three that do not — metaphyseal
dysplasias, spondylometaphyseal dysplasias, severe spondylodysplastic dysplasias
— kept both their name *and* their number across the two revisions.

**Dissolved groups are deprecated, not deleted.** When a revision merges a group
away rather than renaming it, the old value is kept with `deprecated:` and
`deprecated_element_has_possible_replacement` pointing at its successor —
*possible* rather than *exact* because a merge makes the successor broader than
the value it replaces:

```yaml
perlecan:
  deprecated: >-
    Group 5 "Perlecan group" of the 2019 revision (PMID:31633310). The 2023
    revision (PMID:36779427) dissolved it into the new group 7 "Proteoglycan
    core proteins disorders", which also absorbed the former Aggrecan group.
    Retained so existing assignments remain resolvable; do not use for new
    curation.
  deprecated_element_has_possible_replacement: proteoglycan_core_protein_disorders
```

Four 2019 groups are deprecated on that basis: **Perlecan** and **Aggrecan**
(merged into *Proteoglycan core proteins disorders*), and **Neonatal
osteosclerotic dysplasias** and **Other sclerosing bone disorders** (fused into
*Osteosclerotic disorders*). One group is new in 2023 with no 2019 counterpart:
*Skeletal disorders of parathyroid hormone signaling cascade*.

### Dyadic naming

The headline change in 2023 is **dyadic naming**: each phenotypic entity is
systematically paired with its causal gene — "Geleophysic dysplasia,
ADAMTSL2-related" — replacing list numberings and eponyms, which the committee
considers "more informative and less prone to errors."

That is a claim about *disease-entity naming and identity*, not about this
classification axis, and it is deliberately **not** imported into dismech entry
naming by this schema. Whether dismech should adopt dyadic naming is a
scope/identity question for the
[design-decision register](explanation/design-decisions.md), not something to
absorb silently into a classification enum.

### Known gap

The exemplar disorders named in each group description were transcribed from
Table 1 of the **2019** revision. They have been renumbered for 2023 and
corrected where the 2023 paper explicitly says a disorder moved (e.g.
trichorhinophalangeal dysplasia types 1/3 and Langer-Giedion, which left the
acromelic group for *Brachydactylies as part of syndromes*). A full
re-transcription against the 2023 table — 774 rows, already extracted — is
outstanding, as is re-verifying the existing per-entry assignments against it.

## How to assign it

```yaml
classifications:
  harrisons_chapter:
  - classification_value: GENETICS_ENVIRONMENT_DISEASE
  isds_skeletal_category:
  - classification_value: fgfr3_chondrodysplasia
    notes: >-
      ISDS Nosology of Genetic Skeletal Disorders, 2023 revision
      (Unger et al., PMID:36779427), group 1 "FGFR3 chondrodysplasias";
      listed as "Achondroplasia, FGFR3-related".
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
- `icimd_category` — the storage disorders in ISDS group 22 (lysosomal storage
  diseases with skeletal involvement) are inborn errors of metabolism and also carry an ICIMD group;
  likewise `lysosomal_storage_category`.
- `mechanistic_category` — ISDS group 10 members are ciliopathies, which is a
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
| 1 FGFR3 chondrodysplasias | `MONDO:0019685` FGFR3-related chondrodysplasia | Contains the group's members and, crucially, *excludes* the FGFR3 craniosynostoses (Muenke, Crouzon with acanthosis nigricans) that ISDS puts in the craniosynostosis group (34) |
| 8 TRPV4 disorders | `MONDO:0018240` TRPV4-related bone disorder | All descendants are group-8 members; parastremmatic dwarfism appears in the group's own SEMD Maroteaux row |
| 16 Acromesomelic dysplasias | `MONDO:0019696` acromesomelic dysplasia | All descendants are either group-16 members or entities ISDS does not list at all |

Rejected candidates, recorded so nobody re-proposes them:

| Group | Rejected MONDO | Straddle |
|-------|----------------|----------|
| 2 | `MONDO:0022800` type 2 collagenopathy | contains SMD 'corner fracture' type, listed in the SMD group (12) |
| 17 | `MONDO:0019695` acromelic dysplasia | contains pseudohypoparathyroidism type 1A and terminal osseous dysplasia, listed in other groups |
| 24 | `MONDO:0017198` osteopetrosis | contains melorheostosis and osteopathia striata with cranial sclerosis, now in the osteosclerotic group (25) |
| 34 | `MONDO:0015338` syndromic craniosynostosis | contains cranioectodermal dysplasia, a skeletal ciliopathy (group 10) |

Several groups have no usable class at all: either the nearest
MONDO term is obsolete (chondrodysplasia punctata) or it is *narrower* than the
ISDS group, which mixes in entities falling outside it — the OI and bone
fragility group holds cutis laxa and Singleton-Merten alongside osteogenesis
imperfecta.

Note the asymmetry that makes `close_mappings` the right relation: in every
mapped case MONDO is **broader**, because ISDS lists only entities meeting its
inclusion criteria. A mapping is rejected not for breadth but for *crossing*
into another group.

## Entities the nosology lists but declines to decompose

Fanconi anemia is the worked precedent. It is listed in the limb hypoplasia -
reduction defects group (39 in the 2019 revision, 38 in 2023), but it is the
only Table 1 row whose name carries a "(see note below)" pointer and the only
one whose gene column reads "Several" rather than naming loci. The group-39
group footnote says the complex genetic basis of Fanconi anemia and its
complementation groups "is acknowledged but not further listed in this
nosology", referring readers to OMIM or specialized reviews.

Read that precisely: the caveat is about **genetic decomposition, not
membership**. The committee does not question whether Fanconi anemia belongs in
the nosology — it lists it without qualification on that point, and
its skeletal phenotype (radial ray and thumb reduction defects) is exactly what
that group is for. What it declines to do is enumerate FA-A, FA-C, FA-D2 and the
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
