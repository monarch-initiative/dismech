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

### Entry numbers (`NOS <group>-<entry>`)

Each row of the 2023 Table 1 carries its own identifier in the form
`NOS 05-0060` / `NOS 17-0150` — the two-digit group number, then a
four-digit within-group sequence. It is the nosology's own row identifier,
not something this repo invents, and it is the most precise way to point at
a single listed entity: group numbers move between revisions and disorder
names get rewritten (see [Revision handling](#revision-handling)), but the
row number pins which line of which table a `notes:` claim came from.

The group prefix is **revision-specific**, exactly like a bare group number:
`NOS 17-0150` only resolves once you know it is a 2023 row, since the same
entity carried a 2019 group-38 number. So a quoted `NOS` id needs its revision
stated alongside it, just as the group name does.

Quoting it is optional and currently rare — most `notes:` cite the group name
plus the listed disorder name, which is enough. Use it when the entity is
easy to confuse with a neighbour, as `Pseudohypoparathyroidism` does
(`NOS 17-0150`, the row whose name changed between revisions). Always pair it
with the OMIM number when the source row has one: OMIM survives renames, and
the two together make the identification checkable without the paper.

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

**34 of the 41** active groups carry such an alias. The seven that do not split
into two distinct cases:

- **Four kept both their name *and* their number** across the two revisions, so
  there is nothing to alias: metaphyseal dysplasias, spondylometaphyseal
  dysplasias, severe spondylodysplastic dysplasias, and acromesomelic dysplasias.
- **Three are genuinely new in 2023** and have no 2019 name to record:
  proteoglycan core protein disorders, osteosclerotic disorders, and skeletal
  disorders of parathyroid hormone signaling cascade. (The first two are the
  *merge targets* of the four deprecated groups; the third is new outright.)

The four deprecated 2019 values also carry aliases, which is why a naive count
over all 45 permissible values returns 38 rather than 34.

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
classification axis, so dyadic names are **not** adopted as dismech entry
`name:` values. They are instead recorded as **synonyms**, which captures the
naming without committing dismech to it — whether dismech should adopt dyadic
naming as primary remains a scope/identity question for the
[design-decision register](explanation/design-decisions.md).

50 entries carry a dyadic synonym, added under a deliberately strict 1:1 rule:

- the entry's name stem must match a 2023 row stem (dyadic suffix stripped),
- the row's gene must be one of the entry's curated genes, and
- **exactly one** 2023 row may match that stem.

The third condition does the real work. Where 2023 splits an entity into several
gene-specific rows, the dyadic names denote *subtypes*, not synonyms of the
whole — Coffin-Siris (5 rows), Cornelia de Lange (5), Meckel (6), Loeys-Dietz
(6), Adams-Oliver (6), geleophysic dysplasia (3), sclerosteosis (SOST and LRP4).
Attaching any single one of those to the umbrella entry would assert a false
identity, so those 19 entries are skipped.

Two cases are worth knowing about:

- **Multiple sulfatase deficiency** is excluded because the published table
  reads "Multiple sulfatase deficiency, SUMF-related" while its own gene column
  says `SUMF1`. Recording a misspelt gene symbol as a searchable synonym would
  do more harm than the synonym is worth.
- **Spondylodysplastic Ehlers-Danlos syndrome** is excluded because the dismech
  entry is a three-gene umbrella (B3GALT6, B4GALT7, SLC39A13) that the 2023
  revision splits across three rows in *two different groups* (5 and 13). That
  also means its current group assignment needs re-checking in the verification
  pass.

### Known gap

The exemplar disorders named in each group description were transcribed from
Table 1 of the **2019** revision. They have been renumbered for 2023 and
corrected where the 2023 paper explicitly says a disorder moved (e.g.
trichorhinophalangeal dysplasia types 1/3 and Langer-Giedion, which left the
acromelic group for *Brachydactylies as part of syndromes*). A full
re-transcription against the 2023 table — 774 rows, already extracted — is
outstanding, as is re-verifying the existing per-entry assignments against it.
**Group 21 is the first group completed**: its description lists the actual 35
rows of the 2023 table and every dismech assignment to it cites a 2023 row —
see [Group 21](#group-21--verified-against-the-2023-table).

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
   771 entries across 552 genes in 41 groups. Quoting it for a specific
   assignment would be a snippet that does not support its claim. This mirrors
   the ICIMD convention.

### Cross-group traps

The gene most associated with a disorder is often *not* what decides its group.
Frequently mis-assigned cases:

All numbers below are **2023** group numbers. (Their 2019 equivalents differ —
see [Revision handling](#revision-handling) — which is why the guidance is to
cite a group by *name and revision*, never by a bare number.)

| Disorder | Correct group (2023) | Tempting but wrong |
|----------|----------------------|--------------------|
| Crouzon with acanthosis nigricans, Muenke craniosynostosis | 34 syndromes featuring craniosynostosis | 1 FGFR3 chondrodysplasias |
| LADD syndrome | 40 polydactyly-syndactyly-triphalangism | 1 FGFR3 chondrodysplasias |
| Hajdu-Cheney syndrome | 29 osteolysis | 26 OI and bone fragility |
| Brachydactyly-hypertension (Bilginturan) | 19 brachydactylies as part of syndromes | 17 acromelic dysplasias |
| Weyers acrofacial (acrodental) dysostosis | 35 craniofacial dysostoses | 10 skeletal ciliopathies (with Ellis-van Creveld) |
| Spondylodysplastic Ehlers-Danlos syndrome | types 1 (B4GALT7) and 2 (B3GALT6) → 5 multiple joint dislocations; type 3 (SLC39A13) → 13 SE(M)D | one group for all three |
| Acrodysostosis (PRKAR1A, PDE4D) | 17 acromelic dysplasias | 28 PTH signaling — see below |
| Albright hereditary osteodystrophy (GNAS) | 17 acromelic dysplasias | 28 PTH signaling; or the brachydactyly group, where the 2019 revision listed it as "Pseudohypoparathyroidism type IA" (2019 group 38, whose 2023 successor is group 19) |
| Meier-Gorlin syndrome (ORC1, ORC4, ORC6, CDT1, CDC6, GMNN, CDC45, MCM3/5/7, GINS2) | 21 primordial dwarfism and slender bones | 37 patellar dysostoses — the disorder's own name begins "ear-patella" |
| Seckel syndrome (ATR, RBBP8, CEP152, DNA2, TRAIP, NSMCE2) | 21 primordial dwarfism and slender bones | *not listed at all* — the 2023 table contains no row named "Seckel" |
| Lowry-Wood syndrome (RNU4ATAC) | 9 pseudoachondroplasia and multiple epiphyseal dysplasias | 21 primordial dwarfism and slender bones, where the 2019 revision listed it |

The Meier-Gorlin row is the strongest *name-based* trap in the set. The 2019
revision called it ear-patella-short stature syndrome, so the patellar
dysostoses group looks obviously right — but all eleven of its rows are in
group 21, and the 2023 rename to "ear-patella-**primordial** short stature
syndrome" is the tell. Group 37 holds only ischiopatellar dysplasia (TBX4),
nail-patella syndrome (LMX1B), and genitopatellar syndrome (KAT6B). Both the
group 21 and group 37 enum descriptions state the placement explicitly, in
both directions.

The Seckel row is the strongest *absence-based* trap, and it is a direct
consequence of dyadic naming. Searching the 2023 table for "Seckel" returns
nothing — but Seckel syndrome is in the nosology, six times over, rewritten as
`Microcephalic osteodysplastic primordial dwarfism, <GENE>-related`. The rows
are identifiable only by gene and OMIM number: ATR (210600, SCKL1), RBBP8
(606744, SCKL2), CEP152 (613823, SCKL5), DNA2 (615807, SCKL8), TRAIP (616777,
SCKL9), NSMCE2 (617253, SCKL10). Read a name miss as a naming artefact and
check the OMIM column before concluding the committee declined to list an
entity. The same renaming hides the XRCC4 row (616541), which is the entity
published as *short stature, microcephaly and endocrine dysfunction* (SSMED).

The Lowry-Wood row is a move in the opposite direction from Meier-Gorlin's. The
2019 revision listed it in the primordial dwarfism and slender bones group; the
2023 revision moved it to group 9 as `NOS 09-0110 Multiple epiphyseal dysplasia
with microcephaly and nystagmus (Lowry-Wood syndrome), RNU4ATAC-related` (OMIM
226960). RNU4ATAC therefore spans two groups — MOPD I/III and Roifman syndrome
in group 21, Lowry-Wood in group 9 — so for this gene the shared molecular cause
does not settle placement, and a 2019-derived assignment carried forward
unchecked lands in the wrong group.

The GNAS row is a rename *and* a move, which makes it easy to miss: OMIM 103580
appears in the 2019 revision as `Pseudohypoparathyroidism type IA` in group 38
(brachydactylies with extraskeletal manifestations) and in the 2023 revision as
`Albright hereditary osteodystrophy, GNAS-related` in group 17. Searching the
2023 table for "pseudohypoparathyroidism" returns nothing — the entity did not
disappear, it was renamed. The nosology's only other GNAS entries are polyostotic
fibrous dysplasia / McCune-Albright and progressive osseous heteroplasia, both in
group 30. **No GNAS disorder is in group 28.**

For the two dismech entries this affects:

- `Pseudohypoparathyroidism` **is** assigned to group 17, scoped by its `notes:`
  to the PHP1A subtype — that subtype is the listed entity (OMIM 103580). PHP1B
  and PHP2 are not in the nosology at all, so the dismech entry is broader than
  its counterpart; the note says so rather than implying the whole umbrella was
  transcribed.
- `Pseudopseudohypoparathyroidism` is **deliberately left unassigned**. Its OMIM
  (612463) has no row in the 2023 table. Do not read that omission as a claim
  that PPHP falls outside the nosology's scope — the listed row's *label* is
  Albright hereditary osteodystrophy, which PPHP manifests (AHO without hormone
  resistance), so label and OMIM disagree about coverage. Assigning on the label
  would be inference; the honest state is unassigned. If a future revision lists
  PPHP separately, group 17 is where it would go. Note that **MONDO disagrees**:
  `MONDO:0012912` pseudopseudohypoparathyroidism is a descendant of
  `MONDO:0019695` acromelic dysplasia, so the ontology already places it in this
  family. That is not evidence the entry was simply overlooked here — it is a
  second classification making its own call, and this axis transcribes the ISDS
  committee rather than deferring to MONDO (which is also why the group carries
  no `meaning:`; see [MONDO mappings](#mondo-mappings)).

The Acrodysostosis row is a live trap in the other direction. Acrodysostosis is
mechanistically a PTH/PTHrP-signalling disorder, so group 28 looks right — but
the 2023 table lists both `Acrodysostosis, PRKAR1A-related` and `Acrodysostosis,
PDE4D-related` under **group 17, acromelic dysplasias**. Group 28 contains the
PTHR1/SIK3/PTHLH disorders (Jansen and Csukasi-Krakow metaphyseal dysplasia,
Blomstrand dysplasia, Eiken dysplasia, PTHLH brachydactyly and osteolysis).
Reasoning from mechanism to placement is exactly the inference this axis must
not make: the nosology is a transcription of expert placement, not a derivation
from pathway.

### Group 21 — verified against the 2023 table

Group 21 (primordial dwarfism and slender bone dysplasias) has been fully
re-transcribed from the 2023 Table 1: **35 rows, `NOS 21-0010` through
`NOS 21-0350`**. The enum description now lists that membership rather than the
2019-derived exemplars, and every dismech assignment to the group cites a 2023
row.

| Row(s) | dismech entry |
|---|---|
| `NOS 21-0080` MOPD, RNU4ATAC-related (210710) | `Microcephalic_Osteodysplastic_Primordial_Dwarfism_Type_I` |
| `NOS 21-0090` Roifman syndrome, RNU4ATAC-related (616651) | `Roifman-syndrome` |
| `NOS 21-0100` MOPD, PCNT-related (210720) | `Microcephalic_Osteodysplastic_Primordial_Dwarfism_Type_II` |
| `NOS 21-0110`/`0120`/`0130`/`0140`/`0150`/`0160` (the six Seckel rows) | `Seckel_Syndrome` |
| `NOS 21-0190` MOPD, XRCC4-related (616541) | `Short_Stature_Microcephaly_and_Endocrine_Dysfunction` |
| `NOS 21-0250`–`0350` Meier-Gorlin, eleven pre-RC genes | `Meier-Gorlin_Syndrome` |

The remaining 12 rows have no dismech entry. They are a curation gap, not a
classification gap, so each is tracked in `stubs/` with its `NOS` row recorded
in the stub's `notes:` — `NOS 21-0010`/`0020`/`0030` 3-M syndrome, `21-0040`
Sanjad-Sakati, `21-0050` dominant Kenny-Caffey, `21-0060` osteocraniostenosis,
`21-0070` Hallermann-Streiff, `21-0200` the DONSON spectrum, `21-0210` IMAGe,
`21-0220` IMAGe/FILS (POLE), `21-0230` Saul-Wilson, and `21-0240` the SCUBE3
syndrome. Two of those (osteocraniostenosis, Saul-Wilson) and the SCUBE3 stub
were already in the queue from the rare-disease-identification seeding.

One row is not stubbed: `NOS 21-0180`, MOPD CRIPT-related (OMIM 615789). MONDO
has no term that resolves cleanly to it, and a stub's `mondo_id` is required, so
it is recorded here rather than seeded with a guessed identifier.

**Lumping and splitting.** The nosology splits this group by gene, dismech does
not, and the difference is deliberate on both sides. Three dismech entries are
*broader* than the rows they cite and say so in their `notes:`:

- `Seckel_Syndrome` is the Seckel umbrella, covering six rows at once, and also
  curates CENPJ (SCKL4, OMIM 613676) and RTTN, which appear nowhere in the 2023
  table. Splitting it into six gene-specific dismech entries would track the
  nosology's naming rather than the clinical entity, and would strand the two
  unlisted genes.
- `Meier-Gorlin_Syndrome` covers eleven rows plus DONSON, whose Meier-Gorlin
  association postdates the table; DONSON is listed separately at `NOS 21-0200`,
  in the same group, so the single-valued assignment still holds.
- `Microcephalic_Osteodysplastic_Primordial_Dwarfism_Type_I` covers MOPD I and
  the historically separate MOPD III, which the committee also lumps into one
  row.

Only `Roifman-syndrome` and the XRCC4/SSMED entry are 1:1 with a single row.
That MOPD I, MOPD II and Roifman syndrome are three dismech files rather than
one RNU4ATAC/PCNT umbrella follows the committee, which lists them as distinct
entities despite two of them sharing a gene.

**Deliberate non-assignments.** Four dismech entries sit close enough to this
group to be proposed for it, and each is left unassigned on purpose:

| Entry | Why not group 21 |
|---|---|
| `Autosomal_Recessive_Primary_Microcephaly` | MCPH is not in the nosology as an entity. Exactly one of its genes, CENPE, has a row (`NOS 21-0170`, OMIM 616051 = MCPH13), under an MOPD name. A gene-level overlap does not make an umbrella entry "an unambiguous subtype or synonym of a listed disorder", which is the bar rule 2 sets. |
| `Warsaw_breakage_syndrome` | DDX11 appears nowhere in the 2023 table. |
| `Silver_Russell_Syndrome` | Shares CDKN1C with the IMAGe row (`NOS 21-0210`), but SRS is a different entity and is not listed. |
| `Isolated_Growth_Hormone_Deficiency_Type_IA` | Its own entry notes that older literature called it a form of primordial dwarfism. That is a historical label for a GH1 endocrine deficiency, not a nosology placement, and the committee does not list it. |

As with `Pseudopseudohypoparathyroidism` elsewhere in this axis, these are
recorded rather than silently skipped, so nobody re-proposes them.

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

**Three of the 41 groups are mapped.** The bar is deliberately high — a candidate
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
| 17 | `MONDO:0019695` acromelic dysplasia | contains the trichorhinophalangeal syndromes and Langer-Giedion (moved to group 19 in 2023), terminal osseous dysplasia (group 6), and short-rib thoracic dysplasia 9 (group 10). The earlier rationale also cited pseudohypoparathyroidism type 1A — that no longer applies, because 2023 renamed it Albright hereditary osteodystrophy and placed it *inside* group 17 |
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
