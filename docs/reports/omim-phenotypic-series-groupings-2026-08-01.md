# OMIM phenotypic series as dismech groupings — a heterogeneity audit

**Date:** 2026-08-01
**Data:** MONDO `releases/2026-07-06` (`mondo.obo`), dismech `kb/` at time of writing
**Script:** [`scripts/omimps_grouping_audit.py`](https://github.com/monarch-initiative/dismech/blob/main/scripts/omimps_grouping_audit.py)
**Table:** [`data/omimps-phenotypic-series-heterogeneity-2026-08-01.tsv`](data/omimps-phenotypic-series-heterogeneity-2026-08-01.tsv)

## The question

A Mondo audit (2026-07-31) found 42 broad clinical grouping classes carrying
`has_characteristic MONDO:0021152 ! inherited`, sourced solely to an OMIM phenotypic series
(OMIMPS) `equivalentTo` xref. Two questions follow for dismech:

**(a)** Does it make sense to create `kb/groupings/` entries for these OMIMPS-derived objects
(or are some of them just distinct diseases)?

**(b)** How heterogeneous is each — in particular, does it combine **genetic and acquired**
forms?

Short answer to both: **an OMIM phenotypic series is not one kind of thing, and only one of
the four kinds is a grouping.** 16 of the 42 (38%) are not series of diseases at all — they
are series of **risk loci** or **linkage-mapped loci** for a single disease, and the correct
dismech treatment is one `Disease` entry with `genetic:` risk-factor rows, not a grouping
with members. Celiac disease, the case that prompted the ticket, is the cleanest example.

## Method

Everything below is computed offline from `mondo.obo`, so it is reproducible:

```bash
uv run python scripts/omimps_grouping_audit.py --tsv out.tsv     # downloads mondo.obo if needed
uv run python scripts/omimps_grouping_audit.py --detail MONDO:0005130
uv run python scripts/omimps_grouping_audit.py --focus all       # all 608 OMIMPS-equivalent classes
```

Each audited class's is-a descendants are typed:

| Tier | Signal in MONDO |
|---|---|
| `MENDELIAN` | `has_material_basis_in_germline_mutation_in <gene>` |
| `SUSCEPTIBILITY` | `predisposition` subset, or "susceptibility to" in the label (the OMIM `{braces}` convention) |
| `UNMAPPED_LOCUS` | an `OMIM:` equivalentTo xref but **no** gene relation — the proxy for OMIM phenotype mapping key 2 (locus mapped, gene unknown) |
| `SOMATIC` | `has_material_basis_in_somatic_mutation_in` |
| `INFECTIOUS` | under `MONDO:0005550`, or `disease_has_infectious_agent` |
| `ACQUIRED` | label names the acquiring process (senile, drug-induced, traumatic, diabetic, …) |
| `UNSPECIFIED` | everything else — morphological/clinical subdivisions, groupers |

Each descendant gets **exactly one** tier: the signals are not independent flags but are tested
in precedence order `INFECTIOUS > SUSCEPTIBILITY > MENDELIAN > SOMATIC > ACQUIRED >
UNMAPPED_LOCUS`. Two of those orderings carry the argument. Susceptibility outranks Mendelian,
so an OMIM `{braces}` risk locus that MONDO has nonetheless given a gene relation is counted as
a risk locus, not as a Mendelian disease — the distinction this whole audit turns on. And the
gene relation outranks the ACQUIRED label test, so a gene-defined disease whose label happens
to contain "diabetic" is not miscounted as acquired. The practical consequence for anyone
summing columns out of the TSV: a class can appear in `R` while also carrying a gene.

Descendants alone would miss the most important members. MONDO deliberately keeps OMIM
`{susceptibility}` entries **out** of the is-a tree of the disease they predispose to: they are
`is_a MONDO:0020573 inherited disease susceptibility`, with an explicit `excluded_subClassOf`
and a `predisposes_towards` link. So the count of inbound **predisposers** is reported
alongside, and is the single sharpest signal that an OMIMPS is a risk-locus series.

**Known limits.** The `ACQUIRED` count is a floor, not an estimate — it can only see acquired
forms MONDO actually models *under* the class, and MONDO models them sparsely (see
"Latent vs contradicted" below). The `UNMAPPED_LOCUS` tier is a proxy: OMIM's phenotype
mapping key is not in MONDO, so a locus whose gene MONDO simply has not linked yet is
indistinguishable from a true linkage-only locus. The `mondo_recipient_candidate` column is
advisory string-matching and needs a human read.

## The celiac case, in full

```
$ uv run python scripts/omimps_grouping_audit.py --detail MONDO:0005130
# celiac disease (MONDO:0005130) OMIMPS:212750  kind=SUSCEPTIBILITY_SERIES
* UNSPECIFIED     MONDO:0800124    Lane Hamilton syndrome
  PREDISPOSES_TO  MONDO:0008930    celiac disease, susceptibility to, 1
  PREDISPOSES_TO  MONDO:0012340    celiac disease, susceptibility to, 2
  …                                (13 in total)
```

PS212750's 15 rows are all `{Celiac disease, susceptibility to, N}` — brace-annotated
susceptibility entries, not diseases. Only three rows carry phenotype mapping key 3
(molecular basis known): the two 6p21.32 rows, `HLA-DQA1` and `HLA-DQB1`, and CELIAC4 at
19p13.1. The remaining twelve are key 2 — a linkage/association interval with no gene:
the eleven anonymous celiac loci (CELIAC2, 3, 5–13) plus the co-mapped 4q27
`{Autoimmune disease, susceptibility to, 5}` row. Several are recognisable as GWAS regions rather than loci in the Mendelian
sense; CELIAC6 at 4q27, for instance, is the IL2/IL21 region.

Three consequences:

1. **There is nothing to group.** MONDO has all thirteen susceptibility classes, and has
   already ruled that they are *not* subclasses of celiac disease — `excluded_subClassOf
   MONDO:0005130` is asserted explicitly on them. The only is-a descendant of celiac disease
   in MONDO is Lane-Hamilton syndrome (celiac disease with idiopathic pulmonary
   hemosiderosis), which is not a member of the series. A `kb/groupings/Celiac.yaml` would
   have no members.
2. **The disease is genuinely gene–environment, not inherited.** Celiac disease requires
   both an HLA-DQ2/DQ8 background and dietary gluten; monozygotic-twin concordance is
   incomplete and the disease remits on gluten withdrawal. It is not a hereditary disease in
   the sense `MONDO:0003847` defines ("caused by genetic modifications … inherited from a
   parent's genome"), and dismech already types it correctly: `category: Complex`,
   `inheritance: Polygenic inheritance (HP:0010982)`, with gluten exposure in the
   `environmental:` block.
3. **The dismech shape is already right** — one `Disease` entry whose risk loci live in
   `genetic:` as risk-factor rows. This PR makes that shape explicit (see "Changes made").

The Mondo audit's disposition for celiac disease was **STRIP**, and this analysis agrees: the
OMIMPS `equivalentTo` xref is the sole remaining source of the `inherited` claim, and MONDO's
own `excluded_subClassOf` axioms already contradict the claim it produces.

## Why it matters more than descendant counts suggest

The audit measured harm by descendant count, so classes with one or zero descendants
(celiac disease, visceral leishmaniasis, IgA glomerulonephritis, thyrotoxic periodic
paralysis) looked harmless. In the *materialized* release they are not. `hereditary disease`
is only one of a family of classes defined as `<genus> and has_characteristic some inherited`,
and a class picks up **every** one whose genus it also falls under. What that produces today:

| Class | is-a superclasses acquired from the `inherited` claim |
|---|---|
| Waldenstrom macroglobulinemia `MONDO:0100280` | hereditary disease; **inborn errors of metabolism** |
| thyrotoxic periodic paralysis `MONDO:0019201` | **familial periodic paralysis**; **inborn errors of metabolism**; hereditary neurological disease |
| primary biliary cholangitis `MONDO:0005388` | **cirrhosis, familial** |
| IgA glomerulonephritis `MONDO:0005342` | **hereditary nephritis**; inherited kidney disorder |
| age-related macular degeneration `MONDO:0005150` | **inherited retinal dystrophy**; hereditary neurological disease |
| otosclerosis `MONDO:0005349` | **inherited auditory system disease** |
| progressive supranuclear palsy `MONDO:0019037` | **inherited neurodegenerative disorder** |
| temporal lobe epilepsy `MONDO:0005115` | **familial partial epilepsy** |
| carpal tunnel syndrome `MONDO:0007275` | hereditary neuromuscular disease; hereditary neurological disease |
| systemic lupus erythematosus `MONDO:0007915` | hereditary disorder of connective tissue |
| psoriasis `MONDO:0005083`, chronic mucocutaneous candidiasis `MONDO:0015279` | hereditary skin disorder |
| visceral leishmaniasis `MONDO:0005445` | hereditary disease — for a parasitic infection |

A B-cell lymphoma classified as an inborn error of metabolism, and sporadic PSP classified as
an inherited neurodegenerative disorder, are not latent problems. The damage is **lateral**
(each class gains spurious hereditary-X superclasses) as well as downward, and it is
independent of how many descendants the class has.

**One false positive.** `MONDO:0020836 autism, susceptiblity to` is *correctly* placed: it is
already `is_a MONDO:0020573 inherited disease susceptibility`, is in the `predisposition`
subset, and all 26 of its descendants are susceptibility classes. The `inherited`
characteristic is appropriate on a susceptibility grouper. It should come off the audit's
PATTERN list.

## Latent vs contradicted: the acquired axis is under-counted

The audit's "contradicted today" column counts descendants already provably non-genetic. It
reads low (7 across all 42) because MONDO models acquired forms of these entities sparsely,
not because the entities lack them. Two illustrations from the same release:

- **Diabetic cataract** (`MONDO:0001687`) and **diabetes-mellitus-type-2-associated
  cataract** (`MONDO:0005408`) are children of cataract, so they inherit the hereditary
  claim today. The Mondo audit's "contradicted" column did not count them because their
  labels carry no "senile"/"acquired" marker; this audit initially missed them for the same
  reason, and counts them only because the `ACQUIRED` label list was extended with
  `diabet(ic|es)` after review. That is the shape of the whole problem: the count moves with
  the vocabulary you happen to have enumerated.
- **Drug-induced lupus erythematosus** (`MONDO:0016474`) escapes only by an accident of
  placement: it is a *sibling* of SLE under `lupus erythematosus`, not a child.
- **Tetanic cataract** (`MONDO:0001811`, hypocalcaemic) is still uncounted here — an acquired
  form whose label names neither an agent nor an age.

Neither MONDO nor this audit models secondary craniosynostosis, acquired hypogonadotropic
hypogonadism, secondary parkinsonism, or acquired bronchiectasis at all — every one a real,
common clinical entity that would silently inherit the defect the moment someone adds it. So
read the `A` column as **"acquired forms MONDO happens to have"**, and the `MENDELIAN+RISK_LOCUS`
axis label as "no acquired form *in MONDO*", not "no acquired form".

## The four kinds of OMIM phenotypic series

| Kind | n | What the members are | dismech shape |
|---|---:|---|---|
| `SUSCEPTIBILITY_SERIES` | 7 | Brace-annotated OMIM risk loci; MONDO holds them outside the is-a tree as predisposers | **one Disease**, loci as `genetic:` rows with `relationship_type: SUSCEPTIBILITY` |
| `LOCUS_SERIES` | 9 | Numbered linkage intervals, gene mostly unidentified (MYP1-25, IBD1-30, PBC1-5, OTSC1-10) | **one Disease**; add members only as genes are identified |
| `MIXED_GENETIC_ACQUIRED` | 3 | Gene-defined diseases *and* infectious/acquired forms under one clinical umbrella | **grouping over the genetic subset only** — never over the clinical parent |
| `MENDELIAN_SERIES` | 22 | Germline gene-defined diseases; no acquired form in MONDO | **grouping** is well-formed, if dismech has ≥3 member entries |

Heterogeneity axes across all 42: `M+R` 24, `R` only 8, `M` only 6, `M+R+A` 3, `M+A` 1. So
**28 of 42 (67%) mix at least two member kinds**, and only 6 are a clean Mendelian series
(a further 8 are pure risk-locus series with no Mendelian member at all). The
dominant mixture is not genetic-plus-acquired — it is **genetic-plus-risk-locus**, the OMIM
series bundling `{susceptibility}` entries with gene-defined Mendelian diseases under one PS
number. That is the heterogeneity that actually bites, and it is invisible in the `inherited`
flag because both kinds of member are "genetic" in a loose sense.

## Beyond the 42

`--focus all` runs the same typing over **all 608** MONDO classes carrying an OMIMPS
`equivalentTo` xref, not just the 42 broad ones the audit flagged:

| Series kind | n | % |
|---|---:|---:|
| MENDELIAN_SERIES | 457 | 75% |
| LOCUS_SERIES | 49 | 8% |
| SUSCEPTIBILITY_SERIES | 31 | 5% |
| SPARSE | 62 | 10% |
| MIXED_GENETIC_ACQUIRED | 9 | 1% |

So the OMIMPS pattern is right three times out of four, and the risk-locus problem is a
**13% tail (80 classes)** rather than a systematic failure — but that tail is heavily
concentrated in exactly the broad clinical classes the audit selected (38% there vs 13%
overall). dismech already anchors a `Disease` entry on 231 of the 608, which is the natural
worklist for a follow-up sweep.

## Full table

`M / R / A` = Mendelian / risk-locus (susceptibility + unmapped locus + predisposers) /
acquired (infectious + acquired + somatic) member counts.

| Class | OMIMPS | Series kind | M / R / A | Axes | dismech members | dismech disposition |
|---|---|---|---|---:|---:|---|
| autism, susceptiblity to `MONDO:0020836` | PS209850 | SUSCEPTIBILITY_SERIES | 0 / 26 / 0 | R | 0 | SINGLE_DISEASE |
| systemic lupus erythematosus `MONDO:0007915` | PS601744 | SUSCEPTIBILITY_SERIES | 8 / 19 / 0 | M+R | 0 | SINGLE_DISEASE |
| psoriasis `MONDO:0005083` | PS177900 | SUSCEPTIBILITY_SERIES | 2 / 12 / 0 | M+R | 1 | SINGLE_DISEASE |
| celiac disease `MONDO:0005130` | PS212750 | SUSCEPTIBILITY_SERIES | 0 / 13 / 0 | R | 0 | SINGLE_DISEASE |
| thyrotoxic periodic paralysis `MONDO:0019201` | PS188580 | SUSCEPTIBILITY_SERIES | 0 / 3 / 0 | R | 0 | SINGLE_DISEASE |
| visceral leishmaniasis `MONDO:0005445` | PS608207 | SUSCEPTIBILITY_SERIES | 0 / 3 / 0 | R | 0 | SINGLE_DISEASE |
| Waldenstrom macroglobulinemia `MONDO:0100280` | PS153600 | SUSCEPTIBILITY_SERIES | 0 / 2 / 0 | R | 0 | SINGLE_DISEASE |
| inflammatory bowel disease `MONDO:0005265` | PS266600 | LOCUS_SERIES | 12 / 22 / 3 | M+R+A | 0 | SINGLE_DISEASE |
| myopia `MONDO:0001384` | PS160700 | LOCUS_SERIES | 10 / 19 / 0 | M+R | 0 | SINGLE_DISEASE |
| orofacial cleft `MONDO:0000358` | PS119530 | LOCUS_SERIES | 9 / 13 / 0 | M+R | 1 | SINGLE_DISEASE |
| chronic mucocutaneous candidiasis `MONDO:0015279` | PS114580 | LOCUS_SERIES | 5 / 7 / 0 | M+R | 1 | SINGLE_DISEASE |
| keratoconus `MONDO:0015486` | PS148300 | LOCUS_SERIES | 2 / 7 / 0 | M+R | 0 | SINGLE_DISEASE |
| otosclerosis `MONDO:0005349` | PS166800 | LOCUS_SERIES | 1 / 10 / 0 | M+R | 0 | SINGLE_DISEASE |
| primary biliary cholangitis `MONDO:0005388` | PS109720 | LOCUS_SERIES | 0 / 5 / 0 | R | 0 | SINGLE_DISEASE |
| preeclampsia `MONDO:0005081` | PS189800 | LOCUS_SERIES | 2 / 3 / 0 | M+R | 0 | SINGLE_DISEASE |
| multinodular goiter `MONDO:0000334` | PS138800 | LOCUS_SERIES | 0 / 3 / 0 | R | 0 | SINGLE_DISEASE |
| immunodeficiency disease `MONDO:0021094` | PS300755 | MIXED_GENETIC_ACQUIRED | 182 / 56 / 1 | M+R+A | 16 | GROUPING_CANDIDATE |
| cataract `MONDO:0005129` | PS116200 | MIXED_GENETIC_ACQUIRED | 35 / 15 / 5 | M+R+A | 0 | NO_DISMECH_BASIS |
| central precocious puberty `MONDO:0019165` | PS176400 | MIXED_GENETIC_ACQUIRED | 2 / 0 / 3 | M+A | 0 | NO_DISMECH_BASIS |
| spermatogenic failure `MONDO:0004983` | PS258150 | MENDELIAN_SERIES | 106 / 7 / 0 | M+R | 0 | NO_DISMECH_BASIS |
| craniosynostosis `MONDO:0015469` | PS123100 | MENDELIAN_SERIES | 34 / 27 / 0 | M+R | 6 | COVERED_BY_GROUPING |
| hypogonadotropic hypogonadism `MONDO:0018555` | PS147950 | MENDELIAN_SERIES | 56 / 7 / 0 | M+R | 6 | GROUPING_EXISTS |
| arthrogryposis multiplex congenita `MONDO:0015168` | PS617468 | MENDELIAN_SERIES | 26 / 5 / 0 | M+R | 3 | GROUPING_CANDIDATE |
| Parkinson disease `MONDO:0005180` | PS168600 | MENDELIAN_SERIES | 14 / 12 / 0 | M+R | 3 | GROUPING_CANDIDATE |
| holoprosencephaly `MONDO:0016296` | PS236100 | MENDELIAN_SERIES | 11 / 5 / 0 | M+R | 3 | GROUPING_EXISTS |
| lymphoproliferative syndrome `MONDO:0016537` | PS308240 | MENDELIAN_SERIES | 11 / 2 / 0 | M+R | 3 | COVERED_BY_GROUPING |
| hypotrichosis `MONDO:0003037` | PS605389 | MENDELIAN_SERIES | 13 / 4 / 0 | M+R | 1 | GROUPING_DEFERRED |
| visceral heterotaxy `MONDO:0018677` | PS306955 | MENDELIAN_SERIES | 14 / 3 / 0 | M+R | 0 | NO_DISMECH_BASIS |
| age-related macular degeneration `MONDO:0005150` | PS603075 | MENDELIAN_SERIES | 10 / 6 / 0 | M+R | 0 | NO_DISMECH_BASIS |
| hyperinsulinemic hypoglycemia `MONDO:0005803` | PS256450 | MENDELIAN_SERIES | 8 / 0 / 0 | M | 0 | NO_DISMECH_BASIS |
| paraganglioma `MONDO:0000448` | — | MENDELIAN_SERIES | 7 / 0 / 0 | M | 0 | NO_DISMECH_BASIS |
| temporal lobe epilepsy `MONDO:0005115` | PS600512 | MENDELIAN_SERIES | 4 / 4 / 0 | M+R | 0 | NO_DISMECH_BASIS |
| Moyamoya disease `MONDO:0016820` | PS252350 | MENDELIAN_SERIES | 4 / 4 / 0 | M+R | 0 | NO_DISMECH_BASIS |
| hydatidiform mole `MONDO:0006248` | PS231090 | MENDELIAN_SERIES | 4 / 0 / 0 | M | 0 | NO_DISMECH_BASIS |
| bone Paget disease `MONDO:0005382` | PS167250 | MENDELIAN_SERIES | 3 / 2 / 0 | M+R | 0 | NO_DISMECH_BASIS |
| fetal and neonatal alloimmune thrombocytopenia `MONDO:0019415` | PS621264 | MENDELIAN_SERIES | 3 / 0 / 0 | M | 0 | NO_DISMECH_BASIS |
| spastic quadriplegic cerebral palsy `MONDO:0016215` | PS612900 | MENDELIAN_SERIES | 3 / 0 / 0 | M | 0 | NO_DISMECH_BASIS |
| progressive supranuclear palsy `MONDO:0019037` | PS601104 | MENDELIAN_SERIES | 2 / 2 / 0 | M+R | 0 | NO_DISMECH_BASIS |
| bronchiectasis `MONDO:0004822` | PS211400 | MENDELIAN_SERIES | 2 / 1 / 0 | M+R | 0 | NO_DISMECH_BASIS |
| chronic recurrent multifocal osteomyelitis `MONDO:0009813` | PS609628 | MENDELIAN_SERIES | 2 / 1 / 0 | M+R | 0 | NO_DISMECH_BASIS |
| carpal tunnel syndrome `MONDO:0007275` | PS115430 | MENDELIAN_SERIES | 2 / 0 / 0 | M | 0 | NO_DISMECH_BASIS |
| IgA glomerulonephritis `MONDO:0005342` | — | SPARSE | 0 / 1 / 0 | R | 0 | NO_DISMECH_BASIS |

`dismech members` counts **distinct dismech `Disease` entries** anchored on gene-defined
descendants — not distinct MONDO ids, because one entry can anchor several ids through
`has_subtypes`, and a one-entry "series" is a subtype catalog, not a grouping.

## (a) Does it make sense to create dismech groupings?

**For 16 of 42, no — and not because of curation capacity, but because the object is not a
union of diseases.** A dismech `Grouping` is an explicit, curated union that *lists its
members*; where the OMIMPS members are risk loci that MONDO itself keeps out of the disease
hierarchy, a grouping would be an empty union. These belong in an existing `Disease` entry's
`genetic:` block, exactly as `GeneDiseaseRelationshipEnum` already provides for:

```yaml
genetic:
- name: PTPN22
  gene_term: {preferred_term: PTPN22, term: {id: hgnc:9652, label: PTPN22}}
  association: GWAS
  relationship_type: SUSCEPTIBILITY   # "in combination with other genetic or environmental factors"
```

dismech already holds a `Disease` entry on 19 of the 42 audited classes (celiac disease,
psoriasis, SLE, PBC, IgA nephropathy, Waldenström, preeclampsia, Moyamoya, PSP, …), so for
most of the `SINGLE_DISEASE` rows there is nothing to create — only risk-locus rows to enrich.

**For a further 18, not yet, for a different reason:** these are genuine Mendelian series
(spermatogenic failure with 106 gene-defined members, visceral heterotaxy with 14, …) but
dismech curates none or one of their members. A grouping is a union over *existing* entries;
these are curation targets first, groupings later.

**For 5, yes — as groupings over the *genetic subset*, never over the clinical parent.**
Two of these are built in this PR (marked ✅ below). In
descending order of readiness (member entries already in `kb/disorders/` shown):

1. **immunodeficiency disease** (16 member entries). But see below — dismech has already
   solved this one.
2. ✅ **hypogonadotropic hypogonadism** (6): FGFR1-Related Hypogonadotropic Hypogonadism,
   Boucher-Neuhauser, Cerebellar Ataxia-Hypogonadism, Woodhouse-Sakati, Schaaf-Yang, Bosma
   Arhinia Microphthalmia. MONDO already has the recipient class,
   `MONDO:0015770 congenital hypogonadotropic hypogonadism` (32 gene-defined descendants).
   The grouping as built has **7** members: curating it added Kallmann Syndrome, which the
   automated count missed because MONDO models `MONDO:0018800` as a grouper with no
   `has_material_basis_in_germline_mutation_in` relation, so it typed as `UNSPECIFIED`
   rather than `MENDELIAN`. Expect the automated member counts to run one or two low for
   this reason wherever the disease has a genetically heterogeneous grouper class.
3. **arthrogryposis multiplex congenita** (3): Marden-Walker, Wieacker-Wolff, X-Linked
   Infantile SMA.
4. **Parkinson disease** (3): PRKN-Related Juvenile PD, PARK7-Related Early-Onset PD,
   Kufor-Rakeb. Note dismech already has `Parkinsonism_Dopaminergic_Degeneration_Disorders`,
   whose members are Parkinson's Disease and Manganism — an idiopathic + acquired union. The
   monogenic entries are *not* members. Either extend it or mint a sibling
   `Monogenic_Parkinson_Disease`; do not create a grouping that silently re-lumps the acquired
   member.
5. ✅ **holoprosencephaly** (3): SHH Holoprosencephaly Spectrum, HPE9, HPE12.

**For 2, already covered.** `craniosynostosis` members sit in `FGFR-Related Skeletal
Dysplasias`; `lymphoproliferative syndrome` members sit in `Immune Dysregulation IEIs`. No new
grouping.

**dismech has independently already done the recommended fix for the largest class.** The
Mondo audit proposes minting a genetic-form child under `hereditary.yaml` for
`MONDO:0021094 immunodeficiency disease`. dismech's `Inborn_Errors_of_Immunity` grouping is
mapped `skos:exactMatch` to `MONDO:0003778 inborn error of immunity` — which already exists,
and which is precisely the right recipient. The pathology is that in MONDO,
`MONDO:0003778` is a **sibling** of `MONDO:0021094` (both under `immune system disorder`), and
**it is the clinical class, not the inborn-error class, that carries the `inherited`
characteristic**. AIDS being classified as a hereditary disease is the direct consequence.
Moving `OMIMPS:300755` and the characteristic onto `MONDO:0003778` needs no new class.

## (b) Genetic vs acquired heterogeneity

Only three of the 42 mix genetic and acquired members *in MONDO today*
(`immunodeficiency disease`, `cataract`, `central precocious puberty`) — and, as flagged
above, that is a floor set by MONDO's coverage of acquired forms, not a finding about the
diseases. Of the audited classes, the ones whose real-world scope is unambiguously
genetic+acquired and where the grouping boundary therefore has to be drawn carefully:

- **immunodeficiency disease** — primary (inborn errors of immunity) vs secondary (HIV,
  drug-induced, malignancy-associated, malnutrition). MONDO already exhibits the contradiction
  via AIDS.
- **cataract** — congenital/genetic vs senile, diabetic, traumatic, steroid-induced,
  radiation. Three senile classes are counted; diabetic cataract is a descendant and not
  counted by the label heuristic.
- **inflammatory bowel disease** — monogenic VEO-IBD (IL10RA/IL10RB, XIAP, …) vs polygenic
  adult Crohn/UC vs infectious colitis, two of which sit under the class today. MONDO has
  no "monogenic IBD" grouper, so this one *would* need a new class minted.
- **craniosynostosis** — syndromic/gene-defined vs secondary (metabolic, hematologic,
  deformational). MONDO models none of the secondary forms, but
  `MONDO:0015338 syndromic craniosynostosis` (30 gene-defined descendants) is a ready-made
  recipient.
- **hypogonadotropic hypogonadism** — congenital (Kallmann and normosmic forms) vs acquired
  (pituitary tumor, opioid-induced, functional). MONDO models none of the acquired forms;
  recipient `MONDO:0015770` exists.
- **Parkinson disease** — monogenic PD vs idiopathic PD vs secondary parkinsonism
  (drug-induced, manganism, vascular). dismech models this correctly *already*, and better
  than MONDO does, by grouping Manganism with idiopathic PD.
- **bronchiectasis, preeclampsia, temporal lobe epilepsy, keratoconus** — each has a small
  gene-defined arm and a large acquired/idiopathic arm that MONDO does not model.

The generalisable rule: **the OMIMPS names the genetic arm; the MONDO class it is mapped to
names the whole clinical entity.** Every one of the 42 defects is an instance of that single
mismatch, and both the dismech question and the Mondo question reduce to it. In dismech terms
— the genetic arm is the grouping, the clinical entity is a `Disease`, and where the genetic
arm is a set of risk loci rather than of diseases, there is no grouping at all.

## Changes made in this PR

- `scripts/omimps_grouping_audit.py` — the reproducible audit.
- `docs/reports/data/omimps-phenotypic-series-heterogeneity-2026-08-01.tsv` — full per-class table.
- `kb/groupings/Hedgehog_Pathway_Holoprosencephaly.yaml` — worked example of a
  `SHARED_PATHWAY` grouping minted over the **genetic subset**: SHH (ligand), GLI2
  (terminal transcriptional activator), CNOT1 (post-transcriptional regulator of SHH
  repression), with the non-genetic causes of holoprosencephaly — maternal
  pregestational diabetes, teratogens, trisomy 13 — deliberately outside the boundary.
  All three members audit SATISFIED against the AND(holoprosencephaly, smoothened
  signalling) criterion.
- `kb/groupings/Congenital_and_Syndromic_Hypogonadotropic_Hypogonadism.yaml` — worked
  example of the harder case: a shared *final common mechanism* (deficient GnRH drive)
  reached by two routes the OMIM series and the MONDO class do not distinguish —
  **developmental** (Kallmann/ANOS1, FGFR1: GnRH neurons never arrive or never signal)
  versus **degenerative** (Gordon Holmes/RNF216, Boucher-Neuhauser/PNPLA6: normal
  puberty, then loss) — plus three syndromic members. That split is the thing the
  grouping records and neither source does.
- `kb/disorders/FGFR1_Hypogonadotropic_Hypogonadism.yaml` — a curation defect the
  grouping audit surfaced: the entry annotated its cardinal phenotype with the parent
  term HP:0000135 (Hypogonadism) despite hypogonadotropic hypogonadism being its
  defining feature. Refined to HP:0000044, supported by a GeneReviews sentence already
  cited elsewhere in the same file.
- `kb/disorders/Celiac_Disease.yaml` — the worked example of the recommended shape: the ten
  GWAS risk genes gain `gene_term` HGNC bindings and `relationship_type: SUSCEPTIBILITY`, and
  the HLA-DQ2/DQ8 haplotype rows gain `relationship_type: RISK_FACTOR` with a note recording
  that they are the CELIAC1 (`OMIM:212750`, HLA-DQA1/HLA-DQB1 at 6p21.32) locus of PS212750.
  No new claims are asserted — `relationship_type` is a controlled restatement of the existing
  free-text `association`, and the term bindings are validated by `just validate-terms`.

## Follow-ups

- **dismech:** two of the four recommended groupings are built here (holoprosencephaly,
  hypogonadotropic hypogonadism). Remaining: **fetal akinesia / arthrogryposis multiplex
  congenita** (Marden-Walker, Wieacker-Wolff, CHRNA1 fetal hypokinesia, X-linked infantile
  SMA, and Schaaf-Yang, which reaches it through distal arthrogryposis — note dismech
  already holds an `Arthrogryposis Multiplex Congenita` umbrella Disease entry, so this one
  takes the `Diabetes_Mellitus` shape of Grouping-beside-umbrella-Disease); and **monogenic
  Parkinson disease**, best done by extending the existing
  `Parkinsonism_Dopaminergic_Degeneration_Disorders` grouping (currently idiopathic PD +
  Manganism) rather than minting a new one, since a fresh grouping would silently re-lump
  the acquired member. Separately, enrich the risk-locus blocks of the other
  `SINGLE_DISEASE` entries dismech already holds. Two curation gaps the grouping audits
  surfaced: `Schaaf-Yang Syndrome` documents hypogonadism without a gonadotropin profile
  (retained as a member and flagged, not silently admitted), and
  `SHH_Holoprosencephaly_Spectrum` has four subtypes with no `subtype_term` bindings.
- **Mondo:** (i) drop autism from the PATTERN list — it is correctly placed under
  `inherited disease susceptibility`; (ii) for the 16 susceptibility/locus series, STRIP rather
  than PATTERN — there is no genetic subset to group; (iii) for immunodeficiency disease,
  craniosynostosis, hypogonadotropic hypogonadism, hyperinsulinemic hypoglycemia and
  paraganglioma the recipient class already exists (`MONDO:0003778`, `MONDO:0015338`,
  `MONDO:0015770`, `MONDO:0017182`, `MONDO:0017366`) — relocate rather than mint;
  (iv) re-rank the work by materialized superclass damage, not descendant count, or
  single-descendant classes like Waldenström macroglobulinemia (currently an inborn error of
  metabolism) stay at the bottom of the list.
