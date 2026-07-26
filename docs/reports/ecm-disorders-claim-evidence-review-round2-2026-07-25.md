# ECM Disorder Claim–Evidence Review, Round 2 (2026-07-25)

Second batch of ten extracellular-matrix (ECM) disorder entries, reviewed with the
same method as
[round 1](ecm-disorders-claim-evidence-review-2026-07-25.md): does each cited snippet
actually support the claim it is attached to, at the strength and scope the entry
asserts?

Round 1 covered fibrillin, collagens I–VII and elastic-fibre mineralisation. This
round deliberately widens the biology — proteoglycan core-protein glycosylation,
sulfate transport, basement-membrane laminin, copper-dependent crosslinking, and an
*acquired* collagen defect — to test whether the round-1 patterns were specific to
fibrillar-collagen entries.

## Scope

| Entry | ECM compartment / lesion | Evidence items |
|---|---|---|
| `Loeys-Dietz_Syndrome` | TGF-β receptor aortopathy | 84 |
| `Osteogenesis_Imperfecta_Type_III` | collagen I, severe structural | 45 |
| `Spondylodysplastic_Ehlers-Danlos_Syndrome` | B4GALT7 proteoglycan linker | 101 |
| `Hypermobile_Ehlers-Danlos_Syndrome` | no validated gene | 44 |
| `Junctional_Epidermolysis_Bullosa` | laminin-332 / BMZ | 73 |
| `Diastrophic_Dysplasia` | SLC26A2 sulfate transport | 78 |
| `Fibrochondrogenesis` | collagen XI | 64 |
| `Spondyloepiphyseal_Dysplasia_Congenita` | collagen II | 80 |
| `Menkes_Disease` | copper → lysyl oxidase crosslinking | 79 |
| `Scurvy` | vitamin C → prolyl/lysyl hydroxylation (acquired) | 14 |

**662 evidence items.** Cumulative across both rounds: **~1,280 items in 20 entries.**

## Mechanical pass: clean again

Every snippet re-verified as a substring of its `references_cache/` file. Six
apparent misses, all in `Loeys-Dietz_Syndrome`, all benign quoting artifacts:

- four Greek-letter transliterations (`TGFβ` quoted as `TGFbeta`, `β-Blockade` as
  `Beta-Blockade`)
- one dropped closing parenthesis — the source reads `Loeys–Dietz syndrome (LDS), an
  autosomal-dominant…`, quoted as `LDS, an autosomal-dominant…`

**No fabricated snippets, no wrong-paper PMIDs, no Named Entity Confusion** — the
same result as round 1. Across ~1,280 items in twenty entries the anti-hallucination
layer is holding.

⚠️ With the caveat that `linkml-reference-validator` currently reports
`Total checks: 0` (see [#7024](https://github.com/monarch-initiative/dismech/issues/7024)),
so the mechanical gate may not actually be running in CI. Verification here used an
offline substring checker implementing the same contract.

## Verdict

Round 2 is **markedly cleaner than round 1** on the axes round 1 stressed. The
`supports`-vs-`explanation` lint proposed in
[#6955](https://github.com/monarch-initiative/dismech/issues/6955) returns exactly one
hit across 662 items, and it is a false positive (a concession clause about biology,
not about evidence quality). Only two claims in the whole batch carry no evidence at
all.

But the batch surfaces one **large new problem** that round 1 only glimpsed, and it
is the dominant finding here.

---

## The dominant finding: frequency bands with no frequency evidence

**32 phenotypes across 5 entries carry a `frequency:` band whose evidence contains no
quantitative or frequency-band language of any kind.**

| Entry | banded phenotypes | unsupported |
|---|---|---|
| `Junctional_Epidermolysis_Bullosa` | 12 | **11** |
| `Menkes_Disease` | 13 | **11** |
| `Diastrophic_Dysplasia` | 18 | 7 |
| `Spondylodysplastic_Ehlers-Danlos_Syndrome` | 5 | 2 |
| `Scurvy` | 7 | 1 (fixed) |

This is precisely what
[`docs/frequency-evidence-guidelines.md`](../frequency-evidence-guidelines.md) warns
about — the band is a *separate quantitative claim* from the disease–phenotype
association, and most snippets support only the association.

Worked examples:

- **`Menkes_Disease` → `Cutis laxa`, `FREQUENT` (30–79%)**, supported by a single case
  report: *"His skin was dry and wrinkled with a post-mature quality, and loose and
  redundant on the back and trunk."* One patient cannot establish a population band.
- **`Junctional_Epidermolysis_Bullosa` → `Congenital Pyloric Atresia`,
  `VERY_FREQUENT` (80–99%)**, supported by a generic diagnostic-criteria sentence
  listing the five JEB genes — which says nothing about pyloric atresia at any
  frequency.
- **`Menkes_Disease` → `Pili torti`, `FREQUENT`**, supported by *"the peculiar 'kinky'
  hair are the main manifestations"* — qualitative, and the explanation is candid
  that pili torti is a best-fit HPO mapping rather than the quoted term.

**Root cause is visible in the data.** The five affected entries are exactly the ones
with **no Orphanet evidence at all**. Entries that cite ORPHA rows (Marfan, Stickler,
Loeys-Dietz with 46 rows) get their bands from a curated frequency source; entries
without one appear to have had bands assigned from clinical impression. This is a
tractable, targeted gap rather than a diffuse quality problem.

Tracked as [#7026](https://github.com/monarch-initiative/dismech/issues/7026).

---

## Round-1 patterns that recur

### JEB is a fourth instance of the subtype-scoping problem (#6951)

`Junctional_Epidermolysis_Bullosa` defines **four subtypes** and uses the `subtype:`
foreign key **zero times**, with three phenotypes carrying a disease-level
`frequency:` restricted only by free-text notes — *"Specific to JEB with pyloric
atresia subtype"*, *"Primarily in JEB severe (Herlitz) subtype"*. Identical in shape
to `Dystrophic_Epidermolysis_Bullosa` in round 1.

**KB-wide scale, measured:** of **652 entries that define `has_subtypes`, 382 (59%)
never use the `subtype:` FK anywhere.** Largest: `Joubert_syndrome` (39 subtypes
defined, none referenced), `Dystroglycanopathy` (20), `Familial_Atrial_Fibrillation`
(18), `Cystic_Fibrosis` (12), `Meckel_Syndrome` (12). Added to #6951.

### Orphanet `evidence_source` drift is KB-wide, not a one-off (#7026)

Round 1 found `Osteogenesis_Imperfecta_Type_I` tagging Orphanet rows
`HUMAN_CLINICAL` instead of the conventional `OTHER`. Round 2 found the same in
`Osteogenesis_Imperfecta_Type_III` (6 rows) and `Hypermobile_Ehlers-Danlos_Syndrome`
(8 rows) — so it is a pattern, not an outlier.

**KB-wide:** of 6,184 ORPHA evidence items, **372 across 52 files** use a non-`OTHER`
source — 366 `HUMAN_CLINICAL`, 5 `IN_VITRO`, and 1 `MODEL_ORGANISM`. The last two are
plainly wrong: an Orphanet structured record is neither a cell-culture experiment nor
an animal study. Scripted fix; tracked as
[#7027](https://github.com/monarch-initiative/dismech/issues/7027).

### Model-organism-only support for a human phenotype

`Spondylodysplastic_Ehlers-Danlos_Syndrome` → **`Bowing of the Long Bones`** is a
human phenotype claim ("a radiographic finding reported in spEDS") whose only
evidence is a **zebrafish** study reporting *bowed pectoral fins*. The entry is candid
about this in the description, but a pectoral fin is a longer inferential reach than
the mouse-GBM case in round 1 (Alport, #6952). Added to #6952.

### `evidence_source` absent file-wide

`Scurvy` had **0 of 14** items tagged — the same systematic gap round 1 found in
`Ehlers-Danlos_Syndrome_COL5A1-related`. Fixed here (both cited papers are human).

---

## Entry-specific findings

### `Loeys-Dietz_Syndrome`

1. **`Extracellular Matrix Degradation` carries no evidence at all** — despite being a
   central node with **13 downstream edges** and a specific mechanistic claim (MMP
   upregulation, reduced tissue inhibitors, elastic-fibre and collagen degradation).
   The largest evidence gap found in either round. Tracked in
   [#7026](https://github.com/monarch-initiative/dismech/issues/7026).
2. **`Noncanonical MAPK Pathway Activation` asserted LDS-specific activation on
   Marfan-mouse evidence.** The description said these pathways "are prominently
   activated in **LDS aortic tissue**"; the sole citation (PMID:21493862) is titled
   *"Noncanonical TGFβ signaling contributes to aortic aneurysm progression in **Marfan
   syndrome mice**"* and its snippet says "in MFS mice". **Fixed:** description now
   states the evidence is from Marfan models and the extension to LDS rests on the
   shared TGF-β axis; evidence downgraded to `PARTIAL`.
3. **`Immune Dysregulation` asserted "food allergy (31%)"** in both the node
   description and the explanation, while the quoted snippet contained no figures. The
   31% and 6–8% figures *are* in the paper's full text. **Fixed** by extending the
   snippet to carry them.

### `Scurvy`

- **`Ecchymoses` quoted the wrong sentence** — a statement about the patient's diet
  ("staying indoors and inadequate intake of fruits or vegetables"), while the
  explanation described ecchymoses of the lower extremities. The on-point sentence was
  present in the same abstract and already used under `Arthralgias`. **Fixed** by
  swapping in the correct sentence.
- **`Fatigue` asserted `VERY_FREQUENT`** on a sentence that quantifies nothing
  ("nonspecific constitutional symptoms, including weakness, malaise, and fatigue").
  **Fixed** by removing the band with a `notes:` explaining why.
- The core disease mechanism — vitamin C as cofactor for prolyl/lysyl hydroxylases —
  rests on a single vague sentence ("its role in the biochemical reactions of
  connective tissue synthesis"). Thin for the entry's central and ECM-relevant claim;
  not fixed, needs a biochemistry citation.

### Clean entries

`Fibrochondrogenesis` and `Spondyloepiphyseal_Dysplasia_Congenita` produced no
findings on any axis checked. `Osteogenesis_Imperfecta_Type_III` and
`Hypermobile_Ehlers-Danlos_Syndrome` had only the Orphanet `evidence_source` tagging
issue (fixed). hEDS deserves specific credit: an entry for a disease with **no
validated causal gene** is the easiest place to overclaim, and it consistently uses
`PARTIAL` for its cell-model evidence and states plainly that "no underlying genetic,
epigenetic, or metabolomic etiology has been identified."

---

## Disposition

### Fixed in this round

| Entry | Fix |
|---|---|
| `Scurvy` | wrong-sentence snippet on `Ecchymoses`; unsupported `Fatigue` band removed; `evidence_source` added to all 14 items |
| `Loeys-Dietz_Syndrome` | MAPK node qualified + `SUPPORT`→`PARTIAL`; immune snippet extended to carry the 31% figure |
| `Osteogenesis_Imperfecta_Type_III` | 6 Orphanet rows → `OTHER` |
| `Hypermobile_Ehlers-Danlos_Syndrome` | 8 Orphanet rows → `OTHER` |

### Tracked as issues

| Issue | Content |
|---|---|
| [#7026](https://github.com/monarch-initiative/dismech/issues/7026) | 32 frequency bands without frequency evidence; LDS evidence-free ECM node; Scurvy mechanism citation |
| [#7027](https://github.com/monarch-initiative/dismech/issues/7027) | KB-wide Orphanet `evidence_source` drift (372 items, 52 files) |
| [#6951](https://github.com/monarch-initiative/dismech/issues/6951) | extended with JEB + the 382/652 unused-`subtype:` measurement |
| [#6952](https://github.com/monarch-initiative/dismech/issues/6952) | extended with the spEDS zebrafish-only phenotype |
| [#7024](https://github.com/monarch-initiative/dismech/issues/7024) | reference validator reporting `Total checks: 0` |

## What two rounds suggest

- **Fabrication is not the problem.** Zero fabricated snippets or wrong-paper PMIDs in
  ~1,280 items. The SOP works where it is applied.
- **Frequency bands are the weak point.** They are a second, quantitative claim that
  rides along on association-level evidence, and nothing validates them. This is the
  single highest-yield target for new tooling.
- **Structured-source availability predicts quality.** Entries citing Orphanet have
  defensible bands; entries without one are where the unsupported bands cluster. The
  fix is often "cite the ORPHA record", not "find new literature".
- **The `subtype:` FK is the KB's most under-used correctness tool** — 59% of entries
  that define subtypes never reference them, pushing scope qualifications into free
  text where nothing can check them.
