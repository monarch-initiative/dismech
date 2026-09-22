# Therapeutic modalities and oligonucleotides

### Therapeutic Modality and Oligonucleotide (ASO / siRNA) Detail

A treatment's **modality** (the kind of therapeutic platform) is captured by the
enum-backed `therapeutic_modality` slot — **not** the free-text `role` slot, which
is overloaded across host roles, pathophysiology-node roles, and treatment roles.
Prefer `therapeutic_modality` for platform classification so treatments are
queryable by modality across diseases.

Examples of `therapeutic_modality` values (consult the schema for the full enum): `SMALL_MOLECULE`, `MONOCLONAL_ANTIBODY`,
`ANTISENSE_OLIGONUCLEOTIDE`, `SIRNA`, `MRNA_THERAPY`, `GENE_THERAPY`,
`GENE_EDITING`, `CELL_THERAPY`, `PROTEIN_REPLACEMENT`, `PEPTIDE`, `VACCINE`,
`RADIOTHERAPY`, `SURGERY`, `DEVICE`, `BEHAVIORAL`, `OTHER`.

`therapeutic_modality` complements (does not replace) `treatment_term` (the treatment
action) and `therapeutic_agent` (the specific drug). A pharmacotherapy ASO still
uses `NCIT:C15986` for `treatment_term` and an NCIT/CHEBI `therapeutic_agent`.

#### `therapeutic_modality` *is* the `treatment_category` discriminator (issue #972)

Issue #972 proposed a `treatment_category: DRUG | PROCEDURE | DIETARY | OTHER`
discriminator for cleaner filtering. That's already `therapeutic_modality` — just
at finer granularity than 4 coarse buckets. Do not add a second, redundant
category slot; populate `therapeutic_modality` instead. Coarse-bucket mapping,
if you need to collapse to the issue's original 4 categories:

| Coarse bucket | `therapeutic_modality` values |
|---|---|
| DRUG | `SMALL_MOLECULE`, `MONOCLONAL_ANTIBODY`, `NANOBODY`, `ANTISENSE_OLIGONUCLEOTIDE`, `SIRNA`, `MRNA_THERAPY`, `GENE_THERAPY`, `GENE_EDITING`, `CELL_THERAPY`, `PROTEIN_REPLACEMENT`, `PEPTIDE`, `VACCINE` |
| PROCEDURE | `SURGERY`, `RADIOTHERAPY`, `DEVICE` |
| DIETARY / lifestyle | `BEHAVIORAL` (explicitly covers "behavioral, physical, dietary, or lifestyle intervention") |
| OTHER | `OTHER` |

**Mechanical backfill guidance** — a treatment's `therapeutic_modality` can often
be inferred with high confidence directly from its `treatment_term.term.id`,
with no per-disease research needed, when that action term's own definition
*is* a modality (not just an action that's usually done one way):

| `treatment_term.term.id` | `therapeutic_modality` |
|---|---|
| `NCIT:C154430`, `NCIT:C15329`, `NCIT:C16186`, `NCIT:C15289` (surgical procedure / resection / transplantation) | `SURGERY` |
| `NCIT:C15313` (radiation therapy) | `RADIOTHERAPY` |
| `NCIT:C15447` (dietary intervention), `NCIT:C15302` (physical therapy), `NCIT:C159273` (speech therapy), `NCIT:C121351` (occupational therapy), `NCIT:C181743` (behavioral counseling) | `BEHAVIORAL` |
| `NCIT:C15238` (gene therapy) | `GENE_THERAPY` |
| `NCIT:C15431` (hematopoietic cell transplantation — explicitly listed as a `CELL_THERAPY` example) | `CELL_THERAPY` |
| `NCIT:C15346` (vaccination) | `VACCINE` |

(There is no reliable NCIT clinical-action term for device usage — the former
`hearing aid usage` term had no NCIT equivalent and was dropped in the MAXO
removal — so `DEVICE` cannot be inferred mechanically from `treatment_term.term.id`.)

**Do not** mechanically tag nutritional-supplementation terms (`NCIT:C15433`
Nutritional Support) as `BEHAVIORAL`.
It looks dietary but in practice names a specific chemical/vitamin compound
(biotin, carnitine, vitamin E, triheptanoin) far more often than a diet-pattern
change — the correct modality is usually `SMALL_MOLECULE`, sometimes something
else entirely, and always needs a look at the actual treatment before deciding.
This was tried and reverted during the initial backfill (2026-07-08) after it
mis-tagged real drug therapies as `BEHAVIORAL`.

Generic action terms (`NCIT:C15986` Pharmacotherapy, `NCIT:C15747` Supportive
Care, `NCIT:C15240` Genetic Counseling, `NCIT:C93352` Targeted Therapy, etc.)
are **not** in the mechanical table on purpose — the actual modality there
depends on the specific drug/agent (see `therapeutic_agent`) or isn't a
platform-classifiable action at all, and needs a real per-entry look rather
than a blind ID-based rule.

#### `oligonucleotide_details` — one block for ASOs and siRNAs

When `therapeutic_modality` is `ANTISENSE_OLIGONUCLEOTIDE` **or** `SIRNA`, add a
structured `oligonucleotide_details` block (`OligonucleotideDetail`) capturing the
molecular mechanism, RNA target, splice exon, and chemistry:

- `oligonucleotide_mechanism`: `RNASE_H_KNOCKDOWN`, `RNAI_KNOCKDOWN`,
  `SPLICE_MODULATION_EXON_SKIPPING`, `SPLICE_MODULATION_EXON_INCLUSION`,
  `STERIC_BLOCKADE`, `MIRNA_MODULATION`
- `target_gene`: `GeneDescriptor` bound to HGNC (lowercase `hgnc:` prefix)
- `target_transcript`: free text for the RNA target / element (e.g., `APOB mRNA`,
  `SMN2 ISS-N1`)
- `target_exon`: free text for splice-switching ASOs (e.g., `exon 51`). Not
  applicable to siRNA, which acts on mature mRNA rather than on splicing.
- `oligonucleotide_chemistry`: `PHOSPHOROTHIOATE`, `PHOSPHORODIAMIDATE_MORPHOLINO`,
  `TWO_PRIME_O_METHYL`, `TWO_PRIME_FLUORO`, `TWO_PRIME_O_METHOXYETHYL`,
  `LOCKED_NUCLEIC_ACID`, `CONSTRAINED_ETHYL`, `OTHER`
Record the carrier separately in Treatment-level `delivery_system`; use
`targeting_ligand` there instead of the deprecated nested `conjugation`.
See [delivery systems](../../../../docs/delivery-systems.md). The old nested
fields remain valid for existing records, but new examples below use the
current carrier home.

**One class covers both platforms on purpose.** A single-stranded ASO and a
double-stranded siRNA differ in effector — RNase H1 versus Argonaute-2 — but are
otherwise the same programmable medicine, described by the same target and chemistry
attributes, with a separate carrier block. Keeping them in one class is what makes "every treatment
in the KB that silences gene X, by any oligonucleotide route" a single query.

**`targeting_ligand` and `delivery_platform` are orthogonal.**
In `delivery_system`, `targeting_ligand` names the targeting ligand; `delivery_platform` says how the
drug is carried at all. Patisiran is `UNCONJUGATED` *and* `LIPID_NANOPARTICLE`;
vutrisiran is `GALNAC` *and* `CONJUGATE`. Recording only the conjugate would make
those two look like "no targeting" versus "GalNAc" when the real distinction is
nanoparticle versus conjugate — which is what sets route, dosing interval, and
whether premedication is needed.

**Dosing interval lives on `Treatment`, not in this block**, because it applies to
any treatment. Populate the pair together, mirroring the `Prevalence` convention of
a verbatim string plus a normalized number:

- `dosing_interval`: the label's own phrasing (`once every 3 weeks`)
- `dosing_interval_days`: normalized to days (`21`; monthly = 30, quarterly = 90,
  twice yearly = 182.5)

Record loading or induction doses in the treatment `description` rather than
bending the maintenance interval to describe them. Omit both slots rather than
guessing an interval you cannot source.

**Deprecated spellings.** `aso_details`, `aso_mechanism`, and `aso_chemistry` are
retained as deprecated aliases so entries authored before the generalization keep
validating. Do not populate them on new treatments.

**Example — RNase H knockdown ASO (mipomersen, APOB):**
```yaml
treatments:
- name: Mipomersen
  therapeutic_modality: ANTISENSE_OLIGONUCLEOTIDE
  oligonucleotide_details:
    oligonucleotide_mechanism: RNASE_H_KNOCKDOWN
    target_gene:
      preferred_term: APOB
      term:
        id: hgnc:603
        label: APOB
    target_transcript: APOB mRNA
    oligonucleotide_chemistry: TWO_PRIME_O_METHOXYETHYL
  delivery_system:
    targeting_ligand: UNCONJUGATED
    delivery_platform: UNFORMULATED
  treatment_term:
    preferred_term: Pharmacotherapy
    term:
      id: NCIT:C15986
      label: Pharmacotherapy
    therapeutic_agent:
    - preferred_term: mipomersen
      term:
        id: NCIT:C174575
        label: Mipomersen
```

**Example — splice-switching exon-skipping ASO (eteplirsen, DMD exon 51):**
```yaml
  therapeutic_modality: ANTISENSE_OLIGONUCLEOTIDE
  oligonucleotide_details:
    oligonucleotide_mechanism: SPLICE_MODULATION_EXON_SKIPPING
    target_gene:
      preferred_term: DMD
      term:
        id: hgnc:2928
        label: DMD
    target_exon: exon 51
    oligonucleotide_chemistry: PHOSPHORODIAMIDATE_MORPHOLINO
  delivery_system:
    targeting_ligand: UNCONJUGATED
    delivery_platform: UNFORMULATED
```

**Example — GalNAc-conjugated ASO (eplontersen, TTR):** same as the RNase H
example but with `delivery_system.targeting_ligand: GALNAC`,
`delivery_system.delivery_platform: CONJUGATE`, and the TTR `target_gene`.

**Example — the same transcript by two delivery platforms (ATTR amyloidosis).**
Patisiran and vutrisiran silence TTR with the same mechanism and differ only in how
the duplex is carried, which is recorded in their `delivery_system` blocks:

```yaml
- name: Patisiran
  therapeutic_modality: SIRNA
  oligonucleotide_details:
    oligonucleotide_mechanism: RNAI_KNOCKDOWN
    target_gene:
      preferred_term: TTR
      term:
        id: hgnc:12405
        label: TTR
    target_transcript: TTR mRNA
  delivery_system:
    targeting_ligand: UNCONJUGATED
    delivery_platform: LIPID_NANOPARTICLE
  dosing_interval: once every 3 weeks
  dosing_interval_days: 21

- name: Vutrisiran
  therapeutic_modality: SIRNA
  oligonucleotide_details:
    oligonucleotide_mechanism: RNAI_KNOCKDOWN
    target_gene:
      preferred_term: TTR
      term:
        id: hgnc:12405
        label: TTR
    target_transcript: TTR mRNA
  delivery_system:
    targeting_ligand: GALNAC
    delivery_platform: CONJUGATE
  dosing_interval: once every 3 months
  dosing_interval_days: 90
```

Leave `oligonucleotide_details` absent for treatments that are not oligonucleotides.
The structured fields are optional — populate what is documented and omit fields you
cannot source. In particular, do not infer `oligonucleotide_chemistry` for an siRNA
from the fact that stabilized duplexes usually mix 2'-OMe and 2'-F; the slot is
single-valued, so pick one only when a source names the design.

**Mechanism modules.** The two effector paradigms have sibling mechanism modules —
`kb/modules/antisense_oligonucleotide_therapy.yaml` (RNase H1, splice modulation,
steric blockade) and `kb/modules/rnai_gene_silencing.yaml` (RISC loading,
Argonaute-2 cleavage). A disorder whose entry models the therapy itself should
`conforms_to` the one matching its drug; they are not interchangeable.
`ATTR_Amyloidosis` is the worked RNAi conformer.
