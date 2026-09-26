# Grouping Review: Tubulinopathies (2026-08-20)

Review of `kb/groupings/Tubulinopathies.yaml` — grouping structure and MONDO alignment,
completeness of the curated member set, per-member content review, currency against the
2024–2026 literature, and the scientific knowledge gaps that literature opens.

## Scope

| Member entry | Lines | Compliance | Evidence items | Distinct refs | Newest ref |
|---|---:|---:|---:|---:|---:|
| `TUBA1A-related_Tubulinopathy` | 645 | 78.9% | 23 | 5 | 2017 |
| `TUBB2A_TUBB2B-related_Cortical_Malformation` | 1423 | 93.2% | 71 | 8 | 2021 |
| `TUBB3-related_Tubulinopathy` | 1330 | 95.7% | 64 | 8 | 2023 |
| `TUBB_TUBB5-related_Microcephaly` | 698 | 79.3% | 22 | 4 | 2017 |
| **Total** | **4,096** | — | **180** | **21** | — |

Grouping: `grouping_basis: [SHARED_GENE_FAMILY, SHARED_MECHANISM]`, one `NECESSARY`
criteria block whose logic is a single `CONFORMS_TO_MODULE` leaf on
`microtubule_dependent_neuronal_migration_failure#Microtubule Apparatus Perturbation`.

## Method

1. **Structural + membership audit** — `just check-groupings`, `just validate-grouping`,
   `just compliance` per member, section-coverage matrix across the four entries.
2. **MONDO alignment** — EBI OLS4 API: descendants of `MONDO:0100153` (tubulinopathy),
   hierarchical ancestors of each member's `disease_term`, and definitions of the whole
   CDCBM (complex cortical dysplasia with other brain malformations) series to recover
   each type's causal gene.
3. **Literature sweep** — NCBI E-utilities over `tubulinopath*`, each member gene, and
   `TUBG1`/`TUBA8`, restricted to 2023–2026, with abstracts retrieved for every paper
   cited below. All PMIDs and titles in this report come from PubMed `esummary`/`efetch`
   responses, not from recall.

---

## 1. Grouping structure — sound

`check-groupings` reports `structure: OK` and all four listed members `SATISFIED` against
the NECESSARY criterion. The design decisions are defensible and well argued in the file:

- **`NECESSARY`, not `NECESSARY_AND_SUFFICIENT`, is the right semantics.** The
  `grouping_rationale` correctly observes that microtubule-dependent migration failure
  also arises from non-tubulin genes (LIS1/PAFAH1B1, DCX, and — from the module — KIF5C,
  KIF2A, DYNC1H1), so the mechanism cannot be sufficient. MONDO agrees: CDCBM2 is KIF5C
  and CDCBM3 is KIF2A, both non-tubulin.
- **Declining a `HAS_GENE` leaf is justified.** With ~27 human tubulin genes, enumerating
  the isotypes in the logic would be brittle, and under audit-only NECESSARY semantics
  it would buy nothing the curated member list does not already convey.
- **Keeping the four as separate `Disease` entries, not one lump, is correct** and is now
  better supported than when the grouping was written — see §5F on isotype-specific
  C-terminal tails and expression timing.

One structural observation, not a defect: the criterion tests the *migration* module's
trigger node, so any tubulin disease that is not a cortical-malformation disorder fails it
automatically. That makes criterion and intended scope agree — but the scope itself was
stated only in `display_name`. Fixed in this review (§7).

## 2. MONDO alignment — the mapping is right, the upstream hierarchy is not

The `skos:exactMatch` to `MONDO:0100153` is appropriate. The interesting finding is that
**MONDO's own `tubulinopathy` subtree is internally inconsistent**, which is what made the
grouping's member/MONDO alignment look worse than it is.

`MONDO:0100153` has exactly five is-a descendants:

| CURIE | Label | Gene |
|---|---|---|
| `MONDO:0010912` | fibrosis of extraocular muscles, congenital, 3A | TUBB3 |
| `MONDO:0014337` | complex cortical dysplasia with other brain malformations 5 | TUBB2A |
| `MONDO:0018763` | tubulinopathy-associated dysgyria | (tubulin, unspecified) |
| `MONDO:0100144` | Uner Tan Syndrome | TUBB2B p.Arg390Gln |
| `MONDO:0100154` | TUBB3-related tubulinopathy | TUBB3 |

But the CDCBM series is **definitionally** tubulin-caused for five of its types, and only
one of those five is linked to `tubulinopathy`:

| Term | Type | Gene (from MONDO definition) | is-a descendant of MONDO:0100153? |
|---|---|---|---|
| `MONDO:0013541` | CDCBM1 | TUBB3 | **no** |
| `MONDO:0014116` | CDCBM2 | KIF5C | n/a (not a tubulin) |
| `MONDO:0014170` | CDCBM3 | KIF2A | n/a (not a tubulin) |
| `MONDO:0014171` | CDCBM4 | **TUBG1** | **no** |
| `MONDO:0014337` | CDCBM5 | TUBB2A | yes |
| `MONDO:0014341` | CDCBM6 | TUBB | **no** |
| `MONDO:0012399` | CDCBM7 | TUBB2B | **no** |

So CDCBM5 is classified as a tubulinopathy and CDCBM1/4/6/7 are not, despite all five
carrying a tubulin gene in their own definition text. Similarly `MONDO:0012703`
(lissencephaly due to TUBA1A mutation) sits under *lissencephaly type 3*, not under
tubulinopathy.

**Conclusion: the "2/4 members are descendants" signal is an upstream MONDO gap, not a
DisMech membership error.** This is worth an upstream MONDO issue — adding is-a
`tubulinopathy` to CDCBM1/4/6/7 and to `MONDO:0012703` would make the subtree complete
and would make the grouping's `exactMatch` verifiable by reasoning rather than by
curator assertion.

### Uncurated MONDO tubulin concepts (DisMech curation gaps)

| CURIE | Label | Status in DisMech |
|---|---|---|
| `MONDO:0014171` | CDCBM4 (TUBG1) | **no entry at all** — see §3 |
| `MONDO:0100144` | Uner Tan Syndrome (TUBB2B R390Q) | not covered by any entry or subtype |
| `MONDO:0014337` | CDCBM5 (TUBB2A) | subsumed by the TUBB2A/2B entry, but its `TUBB2A` subtype carries no `term:` and the entry has no `mappings:` block |
| `MONDO:0012399` | CDCBM7 (TUBB2B) | same |
| `MONDO:0013541` | CDCBM1 (TUBB3) | subsumed by the TUBB3 entry (`MONDO:0100154`), no mapping recorded |
| `MONDO:0010912` | CFEOM3A (TUBB3) | curated as a *phenotype* of the TUBB3 entry, not as a mapping |

Per the CLAUDE.md MONDO-coverage rule, only `disease_term` and `has_subtypes` terms (and
`skos:exactMatch`/`narrowMatch` mappings) retire a concept from the queue. **None of the
four members carries a `mappings:` block**, so five of the six concepts above remain
formally uncovered even where the biology is fully curated. Adding subtype `term:` values
to the TUBB2A/2B subtypes and a `mappings.mondo_mappings` block to TUBB3 would close four
of them cheaply.

## 3. Membership completeness

### The one clear gap: TUBG1

**TUBG1-related tubulinopathy (CDCBM4, `MONDO:0014171`) belongs in this grouping and has
no DisMech entry.** It passes both criteria on inspection — gamma-tubulin is a tubulin
isotype gene, and the disease is a lissencephaly/microlissencephaly cortical malformation.
The evidence for its in-scope status is already inside the KB: the TUBA1A member entry
quotes PMID:24860126 as *"The core phenotype of TUBA1A and TUBG1 tubulinopathies are
lissencephalies and microlissencephalies"*, `Lissencephaly_Spectrum_Disorders` already
carries TUBG1 as a lissencephaly gene with an `hgnc:` binding, and the TUBA1A entry's own
`notes` explicitly says TUBA1A is "deliberately split from the beta-tubulin
(TUBB2B/TUBB3/TUBB5) and **gamma-tubulin (TUBG1)** tubulinopathies".

It is also well-supported in the current literature, so it is a curatable entry today, not
a stub:

| PMID | Year | Contribution |
|---|---|---|
| `PMID:40298439` | 2025 | Two new cases expanding the phenotypic spectrum of TUBG1 missense variants |
| `PMID:41070651` | 2025 | Clinical phenotype and genetic analysis of a child with CDCBM4 and epilepsy |
| `PMID:39215931` | 2025 | `tubg1` somatic-mutant zebrafish showing tubulinopathy-associated neurodevelopmental phenotypes — a ready `animal_models` entry |
| `PMID:42177523` | 2026 | Gene-specific long-term course, outcome and QoL including a TUBG1 lissencephaly patient |
| `PMID:38919239` | 2024 | Craniosynostosis with a novel TUBG1 variant — phenotype expansion |
| `PMID:38912084` | 2024 | TUBG1 lissencephaly and microcephaly case |

Note `PMID:37475831` ("A novel TUBG1 mutation with neurodevelopmental disorder…") is
**retracted** and must not be cited.

**Recommendation:** file a `claim` issue for TUBG1-related tubulinopathy (CDCBM4,
`MONDO:0014171`), curate the entry, and add it as a fifth member.

### A contested candidate: TUBA8

`TUBA8` is associated with autosomal-recessive polymicrogyria with optic nerve hypoplasia
and appears in polymicrogyria gene panels (`PMID:36211152`, 2022). It is *not* in the KB
at all. It should not be added to the grouping without resolving a genuine gene–disease
validity question first: the `Tuba8` mouse knockout has **no** brain phenotype
(`PMID:28388629`), and `PMID:28687668` is titled, pointedly, *"Tubulin isotype specificity
in neuronal migration: Tuba8 can't fill in for Tuba1a"*. Against that, `PMID:32097653`
(2020) reports Tuba8 driving cortical radial glia differentiation into apical intermediate
progenitors via tubulin C-terminal modification, and `PMID:41105144` (2026) reports TUBA8
promoting dendrite development. **Recommendation:** treat as a `KNOWLEDGE_GAP`-worthy
candidate, not a member; a ClinGen-style validity check should precede any entry.

### Deliberately out of scope (now documented in the grouping)

These are tubulin-family diseases that do **not** conform to the migration module, so the
NECESSARY criterion excludes them correctly — but nothing in the file said so before this
review:

- **TUBB4A** — H-ABC hypomyelinating leukodystrophy / DYT4 dystonia. Still active
  research (`PMID:42044700`, 2026: H-ABC exhibits a cytoskeletal defect associated with
  microtubule stability; `PMID:41547109`/`PMID:41685412`, 2026: taiep rat model).
- **TUBB4B** — Leber congenital amaurosis with early-onset deafness. **Already curated in
  DisMech** (`kb/disorders/Leber_Congenital_Amaurosis_with_Early-Onset_Deafness.yaml`) and
  deliberately modeled as a ciliopathy. New: `PMID:41057290` (2025) extends it to
  cone-rod dystrophy with SNHL outside the canonical hotspot; `PMID:41459724` (2026)
  identifies TUBB4B as the most abundant isotype governing ependymal ciliary polarity.
- **TUBA4A** — ALS/FTD, and now **myo-tubulinopathies**, newly delineated in
  `PMID:41678358` (*Brain*, 2026): 31 individuals from 19 families, with 17 families
  presenting myopathy **without any CNS involvement**, and — notably for a "dominant
  tubulinopathy" framing — three probands with recessive homozygous variants whose
  heterozygous carriers were asymptomatic.
- **TUBGCP2 / TUBGCP6** — gamma-tubulin *complex* genes rather than tubulin isotypes.
  `PMID:42472988` (2026) reports a TUBGCP2-related tubulinopathy with cystic
  leukomalacia. If the grouping is ever re-scoped to "tubulin and tubulin-complex genes",
  this is the boundary that moves.

## 4. Per-member review

### Section coverage across the four members

| Section | TUBA1A | TUBB2A/2B | TUBB3 | TUBB/TUBB5 |
|---|:--:|:--:|:--:|:--:|
| `disease_term` | ✓ | ✓ | ✓ | **added in this review** |
| `inheritance` | — | 1 | 1 | 1 |
| `epidemiology` | — | 2 | — | — |
| `prevalence` | — | 1 | — | — |
| `diagnosis` | — | 2 | 2 | — |
| `progression` | — | — | 2 | — |
| `clinical_burden` | — | — | ✓ | — |
| `animal_models` | — | — | 1 | — |
| `has_subtypes` | — | 2 | — | — |
| `datasets` | — | — | 0 | — |
| `mappings` | — | — | — | — |
| `biological_scale` on nodes | — | ✓ | ✓ | — |
| pathophysiology nodes | 3 | 3 | 5 | 5 |
| phenotypes | 6 | 18 | 13 | 5 |
| treatments | 3 | 3 | 3 | 3 |

### TUBA1A-related Tubulinopathy — the weakest entry for the most important disease

This is the review's headline finding. TUBA1A is the **commonest and most severe**
tubulinopathy — the grouping's own `differentiating_mechanisms` says so, and the entry's
own evidence quantifies it (~1% of classic lissencephaly and ~30% of lissencephaly with
cerebellar hypoplasia, `PMID:20466733`). Yet it is the thinnest entry in the grouping:
645 lines, 23 evidence items, **5 distinct references, the newest from 2017**, and 78.9%
compliance.

Concretely missing: `inheritance` (the entry asserts "heterozygous, almost always de novo"
in prose but never as a structured `Inheritance` block bound to `HP:0000006`),
`epidemiology`/`prevalence`, `diagnosis`, `progression`, `clinical_burden`,
`animal_models` (despite `PMID:17218254` describing the founding ENU mouse, which the
entry *already cites* as `MODEL_ORGANISM` evidence — it is a ready `AnimalModel` +
`modeled_mechanisms` link), `biological_scale` tags on all three nodes, and `mappings`.

The 6 curated phenotypes are all neuroanatomical. The entry's `notes` is explicit and
honest about why the clinical phenotypes (intellectual disability, motor delay,
drug-resistant epilepsy, ataxia, ocular impairment) were left in prose: no quotable
abstract snippet was found in the cited papers. **That constraint has now lifted** —
`PMID:42593952`, `PMID:42472988` and `PMID:42177523` (§5I) all provide quantified,
quotable clinical outcome statements.

### TUBB/TUBB5-related Microcephaly — a schema-visible defect, now fixed

The entry had **no `disease_term` at all** — a gap the grouping's own MONDO consistency
note recorded. Fixed in this review: bound to `MONDO:0014341` (CDCBM6, whose MONDO
definition is precisely "cause of the disease is a mutation in the TUBB gene"); term
validation and schema validation pass, and both the label cache and the `diseaseterm`
enum-membership cache accepted the CURIE.

Remaining: 79.3% compliance, 22 evidence items, 4 references (newest 2017), 5 phenotypes,
no `biological_scale` tags, and no `animal_models` despite the Breuss mouse (`PMID:23246003`,
already cited) and the brand-new zebrafish (`PMID:42241496`, §5C). One discussion
(`gap_tubb_tubb5_natural_history_and_phenotype_breadth`) has **no evidence at all** —
flagged by `just compliance` as `discussions[1] … evidence: MISSING`. This is the entry's
one outright schema-recommended omission and is now easy to fill from `PMID:41152456`
(Korean β-tubulinopathy cohort, which includes TUBB5) and `PMID:42015805` (2026,
intrafamilial variability with a novel missense TUBB variant).

### TUBB2A/TUBB2B-related Cortical Malformation — structurally the best-built entry

93.2% compliance, 18 phenotypes, `has_subtypes` correctly used to hold the two genes as
separate branches, `epidemiology` + `prevalence` present, and an explicit
`gap_tubb2ab_lumping_boundary` discussion that argues the lump. Content is sound.

Two observations. First, the subtypes carry `genes` but no `term:`, so `MONDO:0014337`
(CDCBM5) and `MONDO:0012399` (CDCBM7) are not retired. Second, the lumping argument's
premise — "the published case evidence [for TUBB2A] is thinner than for TUBB2B" — is now
weaker than when written: 2025–2026 produced a TUBB2A mutational hotspot paper
(`PMID:41080462`), a TUBB2A epilepsy genotype–phenotype series (`PMID:41872443`), an
adult TUBB2A ataxia phenotype (`PMID:42050746`), and a TUBB2A SUDEP report
(`PMID:42472988`). The lump may still be right, but the `gap_tubb2ab_lumping_boundary`
discussion should be re-argued against this evidence rather than left standing on the
2021 position.

### TUBB3-related Tubulinopathy — the strongest member

95.7% compliance, 5 pathophysiology nodes including the module's `Axon Guidance and
Projection Wiring Defects` branch (the only member that uses it), a real `animal_models`
entry with two `modeled_mechanisms` links, `progression`, `clinical_burden`, `diagnosis`,
three well-formed discussions, `review_notes`, and the only `therapeutic_modality`-tagged
treatment in the grouping. This entry is the template the other three should be raised to.

Minor: the `Cranial Motor Nerve Maldevelopment and Ocular Dysmotility` node has no
`conforms_to`, because the migration module has no node for cranial-motor-nerve
maldevelopment. That is a reasonable local specialization, not a defect, but it is the
one place where the module under-covers a member.

### Cross-cutting

- **No member has `datasets:`** (0% on all four).
- **No member has `mappings:`.**
- **No treatment in any member uses `target_mechanisms`**, so the module's drug-target
  pattern is entirely unexercised across the grouping. Historically correct — management
  was purely supportive — but §5B changes that.
- Treatments are near-identical triplets (anti-seizure medication, supportive care,
  genetic counseling) with `therapeutic_modality` unset except on TUBB3's surgery entry.
  None of these has a mechanical `treatment_term.term.id` → modality mapping in
  CLAUDE.md's backfill table, so each needs a per-entry look rather than a blind rule.

## 5. Latest literature (2024–2026) and the knowledge gaps it opens

**The whole grouping is 3–9 years behind the literature.** The newest reference anywhere
in the four entries is `PMID:35915025` (2023, TUBB3 only); TUBA1A and TUBB/TUBB5 both stop
at 2017. Nothing from 2024, 2025 or 2026 is cited anywhere. The 2025–2026 window has been
unusually productive for this field, and several papers do not merely add citations — they
open mechanism branches the pathographs do not model.

### A. Ciliogenesis is a second, evidenced pathogenic arm — currently absent from the KB

`PMID:41309602` (*Nat Commun*, Nov 2025) — **Mutations in the β-tubulin TUBB impair
ciliogenesis and are associated with ciliopathy-like phenotypes.** A de novo heterozygous
TUBB missense variant produces features of *both* ciliopathy and tubulinopathy. In
patient-derived cells and gene-edited isogenic lines the variant impairs early cilium
formation by altering microtubule dynamics and structure; knock-in mice show decreased
ciliation in cerebellum and kidney. Two further conclusions matter for curation: the
mechanism is explicitly **not haploinsufficiency**, and *other* patient TUBB mutations also
affect cilium formation — so this is a subset mechanism, not a one-variant curiosity.

`PMID:42091926` (*npj Genom Med*, May 2026) — **Bridging the gap: an emerging link between
tubulinopathies and ciliopathies** — is the review that frames it.

**Gap.** `TUBB_TUBB5-related_Microcephaly` currently models a single chain (tubulin →
spindle/cell-cycle → p53 apoptosis → microcephaly). A ciliogenesis branch is missing
entirely, and DisMech has both a `ciliopathy_dysfunction` module and a `Ciliopathies`
grouping for it to conform to. This is the single highest-value mechanistic addition
identified by this review, and it also bears on the DisMech boundary between the
`Tubulinopathies` and `Ciliopathies` groupings — and on the TUBB4B LCA entry, which
DisMech already models as a ciliopathy.

### B. The first mutation-independent therapeutic strategy

`PMID:42589608` (*Int J Mol Sci*, Aug 2026) — **Restoring the Balance: CRISPRa-Driven
β-Tubulin Compensation as a Strategy for Tubulinopathy Treatment.** CRISPR-Cas9
activation upregulates *non-mutated* β-tubulin isotypes; the authors demonstrate
restoration of the microtubule network and of primary cilium formation. The design
rationale is precisely the problem the grouping exists to describe: mutations are
scattered across distinct tubulin genes, which defeats per-variant editing, so the
strategy targets the shared downstream state instead.

**Gap.** No member entry has any disease-modifying treatment, and none uses
`target_mechanisms`. This is the first candidate that would attach to a mechanism node
(`GENE_THERAPY`/`GENE_EDITING` modality, `target_mechanisms` → the microtubule-apparatus
node), and it should be curated with its preclinical status stated plainly.

### C. A rescuable Notch arm in TUBB5

`PMID:42241496` (*Hum Mol Genet*, Jun 2026) — **tubb5 knockout in zebrafish causes
neurodevelopmental defects via notch pathways.** `tubb5`-null larvae show developmental
delay, craniofacial malformation, uncoordinated movement, increased seizure
susceptibility and impaired photomotor response. Transcriptomics show upregulated
`notch1a`/`her5` (which inhibit neural progenitor differentiation), with decreased
`neurogenin1`/`huc`-positive and increased `sox2`-positive cells — i.e. progenitors stuck
undifferentiated. **DAPT (γ-secretase inhibition) rescued both developmental and
locomotor deficits**; carbamazepine and valproate ameliorated locomotor dysfunction and
PTZ-induced seizure susceptibility.

**Gap.** This is (i) a ready `animal_models` entry for TUBB/TUBB5, which currently has
none, with `PERTURBS`/`RESCUES` `modeled_mechanisms` links and concrete readouts; (ii) a
*distinct* mechanistic arm from the entry's existing p53-apoptosis chain; and (iii) a
second `target_mechanisms` treatment candidate. Curate it with its species caveat explicit
— `HUMAN_MODEL_MISMATCH` is the right `kind` for the DAPT rescue arm.

### D. A complete functional atlas of TUBA1A variants

`PMID:42213754` (*PNAS*, Jun 2026) — **Comprehensive mutagenesis defines the functional
landscape of human α-tubulin.** All **2,683** single-nucleotide coding variants of TUBA1A
profiled by high-content live-cell imaging, resolving **distinct mutation classes that
disrupt folding, chaperone engagement, and protofilament geometry**, with MD simulations
showing how perturbations in GTP binding, dimer contacts and lateral interfaces propagate
to filament architecture, and a predictive framework that generalizes across isotypes.

**Gap.** The TUBA1A entry currently models a single undifferentiated "Altered
Alpha-Tubulin Function" node whose evidence is from 2007–2010. This paper supplies a
variant-class structure the pathograph does not have, and it partially answers the entry's
own open `gap_tuba1a_human_organoid_translatability` question — which should be re-scoped
rather than left as originally posed.

### E. Dominant-negative / gain-of-function is now a *resolved* question, and uncurated

No member entry carries a `functional_impact_category` on any `GeneticContext`, or
discusses the mechanism class at all. The literature has settled it: tubulinopathy
variants are missense-only (no nonsense, frameshift or whole-gene deletion), `PMID:41309602`
states outright that the TUBB mechanism "is not haploinsufficiency", and `PMID:30517687`
(2019) shows TUBA1A R402C/R402H patient alleles **dominantly** disrupt cortical migration
in the developing mouse brain and **impair dynein activity**.

**Gap.** Per CLAUDE.md's decision tree, this belongs in
`GeneticContext.functional_impact_category` (`DOMINANT_NEGATIVE`, and where supported
`GAIN_OF_FUNCTION`), *not* in a descriptor `modifier`. Adding it makes an important,
well-evidenced, currently-invisible claim machine-queryable across all four members.
`PMID:30517687` is also a missing mechanistic anchor for TUBA1A in its own right — the
dynein link is the mechanistic bridge to the module's motor-protein biology.

### F. The tubulin code — the evidence for the grouping's own central claim

The grouping's `grouping_rationale` asserts that members stay separate because isotypes
have "distinct expression timing and binding partners". That claim is currently
**unevidenced anywhere in the KB**, and 2026 supplied the evidence:

- `PMID:42179625` (2026) — C-terminal tails of TUBB2A/2B/2C/3/4A/5 differentially regulate
  cytoplasmic dynein motility; isotype-specific lateral protofilament interactions
  determine β-CTT proximity to the dynein microtubule-binding domain.
- `PMID:42275208` (2026) — spatial and temporal atlas of tubulin isotype gene expression
  during vertebrate embryonic development.
- `PMID:41847015` (2026) — the same for neural crest EMT.
- `PMID:41902449` (2026) — methods for visualizing specific tubulin isotypes and
  pathogenic variants in cellular microtubule arrays.
- `PMID:36943622` (2023) — role of α- and β-tubulin isotypes in early brain development.
- `PMID:41501376` (2026) — autoregulatory control of tubulin abundance, the mechanism that
  determines whether isotype compensation (§5B) can work.

**Gap.** The `microtubule_dependent_neuronal_migration_failure` module is the natural home
for an isotype-specificity discussion; the grouping's rationale should cite it rather than
assert it.

### G. Phenotype expansion beyond what the entries model

| PMID | Year | Expansion | Affects |
|---|---|---|---|
| `PMID:42310787` | 2026 | Dandy-Walker malformation reclassified into the tubulinopathy spectrum (TUBB2B, TUBB3) | TUBB2A/2B, TUBB3 |
| `PMID:41153399` | 2025 | TUBB2B p.Ile202Thr causes **syndromic CFEOM** | crosses the grouping's asserted TUBB3-owns-CFEOM boundary |
| `PMID:42050746` | 2026 | TUBB2A ataxia with preserved ambulation **into adulthood** | TUBB2A/2B — far milder than curated |
| `PMID:41872443` | 2026 | TUBB2A-related epilepsy, novel variants + genotype–phenotype | TUBB2A/2B |
| `PMID:40729534` | 2025 | TUBA1A infantile epileptic spasms syndrome + atypical absence seizures | TUBA1A |
| `PMID:42472988` | 2026 | SUDEP in TUBB2A; movement disorders (dystonia, mirror movements) in 33% | all |
| `PMID:41048055`, `PMID:37713978` | 2026/2023 | Congenital mirror movements (TUBB2B, TUBB3) | TUBB2A/2B, TUBB3 |
| `PMID:42015805` | 2026 | Marked **intrafamilial** phenotypic variability, novel TUBB variant | TUBB/TUBB5 |

The `PMID:41153399` finding deserves emphasis: the grouping's `differentiating_mechanisms`
for TUBB3 says CFEOM3 is what distinguishes it from its siblings. A TUBB2B variant causing
syndromic CFEOM does not invalidate that, but it does mean the differentiator is a
tendency rather than a boundary, and the wording should soften.

### H. Prenatal diagnosis is now a defined modality

`PMID:41901019` (2026, narrative review of prenatal neurosonography in tubulinopathy) and
`PMID:41171976` (2026, prenatal diagnosis with a novel TUBA1A variant). TUBA1A and
TUBB/TUBB5 have **no `diagnosis:` block at all**; TUBB2A/2B and TUBB3 have postnatal ones.
Given that these are severe, often prenatally detectable malformations, a prenatal
neurosonography `diagnosis` entry is a real content gap for all four.

### I. Natural history and outcome data now exist for exactly this member set

`PMID:42593952` (*Am J Intellect Dev Disabil*, Jul 2026) — **Developmental Profiles
Associated with TUBA1A, TUBB2A, TUBB2B, and TUBB3 Tubulinopathy Conditions.** Caregiver
Developmental Profile Scales-4 ratings for 32 individuals across *precisely* the grouping's
gene set. Findings: challenges across all domains, **motor skills most severely affected**;
**TUBB3 conditions relatively milder**; co-occurring vision impairment in **71%**, and
those individuals showed greater overall delays.

`PMID:42177523` (*Orphanet J Rare Dis*, May 2026) — gene-specific long-term course,
neurodevelopmental outcome and quality of life across LIS1/DCX/DYNC1H1/**TUBA1A**/**TUBG1**
lissencephaly, with PedsQL Family Impact Module scores (parental HRQL mean 61.23) and
supportive-therapy effectiveness data.

`PMID:41152456` (2026, Korean β-tubulinopathy cohort, n=12) and `PMID:42472988` (2026,
Turkish multicentre cohort, n=15, seven genes) and `PMID:40179460` (2025, Japanese
single-centre retrospective) supply the frequency denominators that phenotype `frequency:`
qualifiers require (see `docs/frequency-evidence-guidelines.md`).

**Gap.** Only TUBB3 has `progression` and `clinical_burden`. `PMID:42593952` directly
substantiates the grouping-level claim that TUBB3 is the mildest member — which is
currently nowhere in the KB — and would be strong evidence in the grouping's own
`differentiating_mechanisms`.

## 6. Prioritized recommendations

| # | Action | Target | Effort |
|---|---|---|---|
| 1 | Curate **TUBG1-related tubulinopathy** (CDCBM4, `MONDO:0014171`) and add as a fifth member | grouping | new entry |
| 2 | Add the **ciliogenesis branch** to `TUBB_TUBB5-related_Microcephaly` (`PMID:41309602`, `PMID:42091926`), with `conforms_to` on `ciliopathy_dysfunction` | TUBB/TUBB5 | medium |
| 3 | **Raise TUBA1A to parity** — `inheritance`, `diagnosis` (incl. prenatal), `progression`, `clinical_burden`, `animal_models` (ENU mouse, already cited), `biological_scale` tags, and clinical phenotypes now that quotable cohort text exists | TUBA1A | large |
| 4 | Add `animal_models` for the **tubb5 zebrafish** with the Notch arm and DAPT rescue (`PMID:42241496`) | TUBB/TUBB5 | medium |
| 5 | Curate **CRISPRa β-tubulin compensation** (`PMID:42589608`) as an emerging `target_mechanisms` treatment — the grouping's first non-supportive therapy | module or all members | medium |
| 6 | Add `functional_impact_category: DOMINANT_NEGATIVE` to the `GeneticContext` blocks, with `PMID:41309602` / `PMID:30517687` | all four | small |
| 7 | Fill the empty `evidence` on `gap_tubb_tubb5_natural_history_and_phenotype_breadth` (`PMID:41152456`, `PMID:42015805`) | TUBB/TUBB5 | small |
| 8 | Add `mappings.mondo_mappings` and subtype `term:` values to retire CDCBM1/5/6/7 and CFEOM3A | all four | small |
| 9 | Refresh `gap_tubb2ab_lumping_boundary` against 2025–2026 TUBB2A evidence | TUBB2A/2B | small |
| 10 | Soften the TUBB3 `differentiating_mechanisms` CFEOM claim in light of `PMID:41153399` | grouping | small |
| 11 | Add the isotype-specificity evidence (`PMID:42179625`, `PMID:42275208`) to the migration module, supporting the grouping's split rationale | module | small |
| 12 | File an upstream MONDO issue: link CDCBM1/4/6/7 and `MONDO:0012703` under `MONDO:0100153` | upstream | small |

## 7. Changes applied

> **Update, same day.** After this review was delivered, all twelve recommendations in §6
> were applied. See §9 for what was done and for the two places where doing the work
> corrected the review itself.

The review pass itself was deliberately minimal. Three defects that the grouping file
already named were fixed:

1. **`kb/disorders/TUBB_TUBB5-related_Microcephaly.yaml`** — added the missing
   `disease_term` (`MONDO:0014341`, complex cortical dysplasia with other brain
   malformations 6). Term validation and schema validation pass; `cache/mondo/terms.csv`
   and `cache/enums/diseaseterm_*.csv` picked up the CURIE.
2. **`kb/groupings/Tubulinopathies.yaml`** — rewrote the MONDO `consistency.notes` so it
   is accurate after fix 1 and records the upstream MONDO inconsistency (§2) as the actual
   cause of the 2/4-descendant signal.
3. **`kb/groupings/Tubulinopathies.yaml`** — added a **scope boundary** paragraph to
   `notes` naming the deliberately-excluded tubulin diseases (TUBB4A, TUBB4B, TUBA4A,
   TUBGCP2/6) and a **known membership gap** paragraph naming TUBG1 and Uner Tan syndrome,
   so that an in-scope gap is no longer indistinguishable from an out-of-scope exclusion.

## 8. Verification

- `just check-groupings kb/groupings/Tubulinopathies.yaml` — `structure: OK`, all four
  members `SATISFIED`.
- `just validate-grouping kb/groupings/Tubulinopathies.yaml` — passed.
- `just validate kb/disorders/TUBB_TUBB5-related_Microcephaly.yaml` — passed;
  `Snippets checked: 22/22 verified against cached references`.
- `just validate-terms kb/disorders/TUBB_TUBB5-related_Microcephaly.yaml` — passed.
- Every PMID and title in this report was retrieved live from NCBI E-utilities during the
  review. `PMID:37475831` is flagged above as **retracted**. No PMID cited here has yet
  been added to a `kb/` entry — doing so requires `just fetch-reference` plus exact-quote
  snippet verification per the evidence SOP.

---

## 9. Follow-up: all twelve recommendations applied (2026-08-20)

Every recommendation in §6 was carried out. Two of them could not be applied as written,
and the reasons are findings in their own right.

### The review was wrong about mechanism class (recommendation 6)

Recommendation 6 said to add `functional_impact_category: DOMINANT_NEGATIVE` to all four
members. Reading the primary sources to write the annotation showed that is only right for
two of them, and actively wrong for a third:

| Member | Applied value | Why |
|---|---|---|
| TUBA1A | `DOMINANT_NEGATIVE` | `PMID:30517687` resolves it directly — mutant α-tubulin "acts dominantly by populating microtubules with defective binding sites for dynein", and dynein impairment scales with mutant expression. A poisoning mechanism. |
| TUBB3 | `DOMINANT_NEGATIVE` | Folded mutant heterodimers still polymerize and a subset disrupts the kinesin interaction — a subunit that incorporates and degrades a motor-binding surface. |
| **TUBB / TUBB5** | **`GAIN_OF_FUNCTION`** | `PMID:41309602` tests haploinsufficiency directly and excludes it (TUBB-haploid cells ciliate normally), and concludes the variants "all act in a gain-of-function fashion". The review had read "not haploinsufficiency" as implying dominant-negative. It does not. |
| **TUBB2A / TUBB2B** | **`UNKNOWN`** | Impaired heterodimer formation is evidenced for both, but that finding does not discriminate a poisoning subunit from a reduced functional-heterodimer pool. `UNKNOWN` here means *examined and unresolved*, and is paired with a new `gap_tubb2ab_functional_impact_class` discussion. |

The distinction is not bookkeeping: it decides whether the isotype-compensation strategy of
§5B should be expected to work, since adding wild-type subunits dilutes a poisoning allele
but does not remove it.

### The ciliopathy module had to be widened first (recommendation 2)

`TUBB_TUBB5` could not honestly `conforms_to`
`ciliopathy_dysfunction#Basal Body and Transition Zone Dysfunction` as the node was
written: it admitted only lesions in basal body, transition zone, BBSome or IFT component
genes, and TUBB is none of those. Rather than force the conformance or drop it, the module
node was widened to admit a third entry route — a dominant tubulin-subunit variant
impairing cilium assembly directly — with `PMID:41309602` and `PMID:42091926` as evidence,
plus two guardrails in the module notes: conformance needs evidenced ciliary impairment in
that disorder (not merely a microtubule lesion), and a tubulin loss-of-function lesion is
*not* evidence for this route, since the mechanism is dose-dependent gain-of-function.

### Recommendation 12 landed as a DisMech issue, not an upstream one

This session has no push access to `monarch-initiative/mondo`, so the upstream request is
filed as `monarch-initiative/dismech#9113` with the full evidence table, for someone with
upstream access to carry over.

### What changed, by file

| File | Change |
|---|---|
| `kb/disorders/TUBG1-related_Tubulinopathy.yaml` | **New entry** (R1). CDCBM4 / `MONDO:0014171`, 4 pathophysiology nodes, 8 phenotypes, 2 animal models, 2 knowledge gaps, 50/50 snippets verified. |
| `kb/groupings/Tubulinopathies.yaml` | TUBG1 added as fifth member (R1); TUBB3 CFEOM differentiator softened with evidence (R10); MONDO consistency note and scope/gap notes updated. |
| `kb/disorders/TUBA1A-related_Tubulinopathy.yaml` | Raised to parity (R3): inheritance, epidemiology, 3 diagnosis entries incl. prenatal neurosonography, 3 progression phases, clinical burden, 2 animal models, scale tags, 7 clinical phenotypes, `DOMINANT_NEGATIVE` context. 78.9% → ~88% compliance. |
| `kb/disorders/TUBB_TUBB5-related_Microcephaly.yaml` | Ciliogenesis node (R2), Notch node + zebrafish model with DAPT rescue (R4), `GAIN_OF_FUNCTION` context (R6), gap evidence filled (R7), new translatability discussion. |
| `kb/disorders/TUBB2A_TUBB2B-related_Cortical_Malformation.yaml` | Lumping gap re-argued against 2025–26 evidence (R9), `UNKNOWN` context + new mechanism-class gap (R6), Uner Tan boundary discussion, subtype terms + mappings (R8). |
| `kb/disorders/TUBB3-related_Tubulinopathy.yaml` | `DOMINANT_NEGATIVE` context (R6), CDCBM1 + CFEOM3A mappings (R8), inherited-allele qualifier. |
| `kb/modules/microtubule_dependent_neuronal_migration_failure.yaml` | CRISPRa β-tubulin compensation treatment with `target_mechanisms` (R5) — the grouping's first non-supportive therapy; isotype-specificity knowledge gap (R11). |
| `kb/modules/ciliopathy_dysfunction.yaml` | Trigger node widened to admit tubulin-subunit lesions, with guardrails (R2). |

Seven history records were written under `history/`. 30 new references were fetched with
`just fetch-reference`; every snippet in every file above is quoted from a cached abstract
and verified.

### Two things deliberately not done

- **TUBA8 was not added as a member.** §3 flagged its gene–disease validity as contested,
  and nothing in this pass resolved it. It stays a candidate.
- **TUBG1 was not added to `Lissencephaly_and_Neuronal_Migration_Disorders`**, where it
  would also fit. Recommendation 1 scoped it to this grouping; widening to a second
  grouping is a separate call.

---

## 10. Coverage pass: every tubulin-family disease curated (2026-08-20)

The review above is scoped to the grouping — five members, all cortical-malformation
diseases. A follow-on pass extended coverage to the whole tubulin gene family, on the
principle that a disease should not go uncurated merely because it falls outside one
grouping's boundary. Eight new entries:

| Entry | MONDO | What it is |
|---|---|---|
| `TUBB4A-related_Neurologic_Disorder` | `MONDO:0800470` | H-ABC hypomyelinating leukodystrophy / DYT4 dystonia — myelin, not migration |
| `TUBA4A-related_Disorder` | `MONDO:0014531` | ALS22/FTD, hereditary spastic ataxia, and the 2026 myo-tubulinopathies (17/19 families with no CNS disease at all) |
| `TUBB8-related_Oocyte_Maturation_Defect` | `MONDO:0021573` | Meiotic spindle assembly failure; a primate-specific isotype, so no mouse model is possible |
| `TUBB1-related_Macrothrombocytopenia` | `MONDO:0800047` | Megakaryocyte marginal-band failure |
| `TUBGCP4-related_Microcephaly_and_Chorioretinopathy` | `MONDO:0014592` | γ-TuRC component; microcephaly **without** cortical malformation |
| `TUBGCP6-related_Microcephaly_and_Chorioretinopathy` | `MONDO:0009624` | As above, plus retinal dysfunction |
| `TUBA8-related_Polymicrogyria_with_Optic_Nerve_Hypoplasia` | *(none)* | Curated as `association: Suspected` — see below |
| `Uner_Tan_Syndrome` | `MONDO:0100144` | Biallelic TUBB2B p.Arg390Gln; the recessive, cerebellar, basal-ganglia-sparing outlier |

**TUBA8 is the entry that changed shape while being written.** The `check-title-snippets`
gate refused a title-quoted snippet, which forced a read of the full PMID:28388629
abstract — where the authors report re-analysing the *original* human subjects by exome
sequencing and finding a homozygous loss-of-function **SNAP29** variant, "suggesting that
SNAP29 deficiency, rather than TUBA8 deficiency, may underlie most or all of the
neurodevelopmental anomalies." The linked-bystander scenario raised in §3 as a
hypothetical had in fact already been found. The entry is curated with the SNAP29 finding
as `supports: REFUTE`, and the gene–disease relationship as `Suspected`. This is a
worked example of a validation gate catching a *substantive* error rather than a
formatting one.

None of the eight joined the Tubulinopathies grouping: the `NECESSARY` criterion tests
migration-module conformance, and none of them conform.

---

## 11. QA pass (2026-08-22)

An adversarial re-read of everything above. Cross-entry foreign-key checking over the
13 tubulin-family entries (every `downstream.target`, `conforms_to` anchor,
`target_mechanisms` target, model link, discussion `attaches_to`, and subtype FK) came
back clean, as did duplicate-`disease_term` checking across all 2,099 entries. The pass
found five things worth fixing, three of them errors in the work above.

### One more disease was uncurated

**`TUBGCP2-related_Lissencephaly_Spectrum_Disorder`** — no MONDO disease term exists (only
the gene, HGNC:18599), which is why a MONDO-driven sweep missed it. The gene–disease
relationship is nonetheless solid: AJHG 2019 delineation (PMID:31630790), independent
replication with functional work in 2021 (PMID:33458610), a 2025 literature review
(PMID:40017707), and inclusion in a 2026 multicentre cohort (PMID:42472988).

It is mechanistically the interesting one of the γ-TuRC genes. TUBGCP4 and TUBGCP6 cause
microcephaly with chorioretinopathy and a structurally normal cortex; TUBGCP2 causes frank
pachygyria and subcortical band heterotopia and **conforms to all three nodes** of the
migration module. The literature calls it a tubulinopathy — PMID:40448381 does so in its
title. It is still excluded from the grouping, on gene identity: GCP2 is a γ-tubulin
*complex* protein, not a tubulin. That is a lumping decision, not a fact, and it is now
recorded on both sides so it can be revisited. It also demonstrates why the grouping's
criterion is `NECESSARY` (audit-only) rather than `SUFFICIENT`: a disorder can satisfy the
mechanism half of the conjunction and still not be a member.

`functional_impact_category` is left `UNKNOWN` rather than defaulted to
`LOSS_OF_FUNCTION`, with a knowledge gap explaining why: the allele spectrum contains a
multi-exon deletion and a frameshift (unambiguously null) *and* a missense allele that
leaves GCP2 protein levels normal while mislocalizing γ-tubulin, HAUS6 and NEDD1.

### Three stale or contradictory statements introduced by the earlier passes

1. **The grouping described itself as alpha- and beta-tubulin only** — in both
   `description` and `grouping_rationale` — while listing TUBG1 (gamma) as a member. Added
   in the same pass that added TUBG1. Fixed.
2. **The grouping's notes said Uner Tan syndrome "is still not covered by any member entry
   or subtype."** It had been curated as its own entry two sections up in this very
   report. Fixed.
3. **The scope-boundary note listed TUBB4A / TUBB4B / TUBA4A / TUBGCP2 / TUBGCP6 as "out
   of scope"** without saying that most of them now have entries, and omitted TUBGCP4,
   TUBB8, TUBB1 and TUBA8 entirely. Rewritten to name each entry and to separate the two
   distinct exclusion reasons (fails the mechanism criterion vs. excluded on gene
   identity).

### Two scoping gaps

4. **`Uner_Tan_Syndrome` did not say that the eponym is broader than the entry.** The
   MONDO binding is correct — `MONDO:0100144` is *defined* as the TUBB2B R390Q entity —
   but the clinical literature also applies the name to VLDLR, CA8, WDR81 and ATP8A2
   families, which MONDO keeps separate as CAMRQ 1–4. A reader could have taken the entry
   as covering all of them. Caveat added; the CAMRQ concepts are not tubulin disorders and
   remain uncurated.
5. **`MONDO:1060115` (TUBB4B-related ciliopathy) was referenced nowhere in the KB**,
   despite being the direct is-a parent of the curated LCAEOD entry — the last
   tubulin-family MONDO disease concept with no KB reference. Added as `skos:broadMatch`,
   not `exactMatch`: the umbrella's own definition says diagnoses under it can include
   primary ciliary dyskinesia, which this entry does not cover. As a `broadMatch` it does
   not retire the concept from the curation queue, which is the intended outcome.

### Two additions from currency checking

The 2026 Turkish multicentre cohort (PMID:42472988) had not been read by any entry. Two
findings were curated onto `TUBB2A/TUBB2B-related Cortical Malformation`: the first report
of **probable SUDEP** in a TUBB2A patient — which makes the epilepsy here a mortality risk
to counsel, not only a seizure burden — and **movement disorders in 33.3%** including
dystonia and mirror movements. No frequency band was asserted for the latter, because the
percentage spans all seven cohort genes rather than these two. Mirror movements are worth
noting mechanistically: they implicate the module's axon-guidance branch, not the
migration branch that explains the cortical malformation.

### One deferred item closed

TUBG1 **was** added to `Lissencephaly_and_Neuronal_Migration_Disorders` (§9 left this
open), along with TUBGCP2. All 17 members of that grouping audit as `SATISFIED`.

### What changed, by file

| File | Change |
|---|---|
| `kb/disorders/TUBGCP2-related_Lissencephaly_Spectrum_Disorder.yaml` | **New entry.** 4 pathophysiology nodes conforming across all three migration-module nodes, 8 phenotypes, 2 knowledge gaps, 27/27 snippets verified, 86.8% weighted compliance. |
| `kb/groupings/Tubulinopathies.yaml` | Gamma-tubulin admitted in `description` and `grouping_rationale`; stale Uner Tan gap note corrected; scope boundary rewritten with entry names and the two exclusion classes. |
| `kb/groupings/Lissencephaly_and_Neuronal_Migration_Disorders.yaml` | TUBG1 and TUBGCP2 added as members with differentiating mechanisms. |
| `kb/disorders/TUBB2A_TUBB2B-related_Cortical_Malformation.yaml` | Probable-SUDEP evidence on the epilepsy phenotype; new Movement Disorder phenotype. Both from PMID:42472988. |
| `kb/disorders/Uner_Tan_Syndrome.yaml` | Eponym scope caveat naming the four CAMRQ concepts. |
| `kb/disorders/Leber_Congenital_Amaurosis_with_Early-Onset_Deafness.yaml` | `MONDO:1060115` broadMatch mapping. |

Four further history records written. Every new snippet is quoted from an abstract cached
by `just fetch-reference` and verified.
