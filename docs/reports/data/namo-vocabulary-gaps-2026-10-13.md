# NAMO vocabulary gaps met while curating fibrosis NAMs

Notes behind the recurring blocker in [the assay and NAM inventory](../nam-methods-inventory-2026-10-13.md): "Models involving co-cultures, gravity-linked plates and ex vivo slices, revealed some NAMO vocabulary gaps." Drawn from the threads of PR [#9935](https://github.com/monarch-initiative/dismech/pull/9935) and issue [#9997](https://github.com/monarch-initiative/dismech/issues/9997), with the follow-up in [#10313](https://github.com/monarch-initiative/dismech/issues/10313). Written 2026-10-13.

## 1. The Akura Twin liver fibrosis plate (PR #9935)

The system is a 384-well microplate whose well pairs are connected by gravity-driven flow. One well holds 3D microtissues of HepaRG hepatocytes with THP-1 monocytes, the other holds hTERT-HSC stellate microtissues. It was added to [Liver Cirrhosis](https://dismech.monarchinitiative.org/pages/disorders/Liver_Cirrhosis.html) and the [drug-induced liver injury module](https://dismech.monarchinitiative.org/pages/modules/drug_induced_liver_injury.html).

The paper calls it a microphysiological system, but NAMO's `MicrophysiologicalSystem` class could not be used, for two reasons:

- It is declared `abstract: true` in NAMO, so it cannot be bound at all.
- It requires microfluidic integration as a defining feature, with `OrganOnChip` and `TissueOnChip` beneath it. A passive interconnected-well plate is not a perfused microfluidic device, so binding it there would assert a design the paper does not describe. The same reasoning set the local type to `CO_CULTURE` rather than `ORGAN_ON_CHIP`, since the schema defines the latter as microfluidic and the three existing liver models tagged that way genuinely are perfused.

The reviewer then suggested `namo:CellLineModel`, since every component (HepaRG, hTERT-HSC, THP-1) is an established cell line. It withdrew the suggestion after checking that NAMO defines that class as `is_a: TwoDCellCulture`, which is wrong for 3D microtissues. `namo:ThreeDCellCulture`, the sibling class covering spheroids, was named as the nearest alternative.

The entry ended up as `namo:CoCulture`, "co-culture systems combining multiple cell types to mimic microenvironments and cell-cell interactions." That is accurate and agrees with the local `CO_CULTURE` type on the same defining feature. But because `namo_type` is single-valued, one feature had to win, and the binding captures the multi-cell-type arrangement rather than the gravity-linked, non-perfused format. No NAMO class names that format.

## 2. Precision-cut tissue slices (issue #9997)

When looking for an organ-agnostic model for the [fibrotic_response module](https://dismech.monarchinitiative.org/pages/modules/fibrotic_response.html), the one cross-organ fibrosis platform found was Bigaeva et al. 2020 ([PMID:31676376](https://pubmed.ncbi.nlm.nih.gov/31676376/)), which cultures murine precision-cut slices from small intestine, liver and kidney to separate conserved fibrogenesis from organ-specific features. That is almost a restatement of what the module is for.

It was left out of the module-model PR for two reasons:

- The slices are murine. Ex vivo tissue slices are `experimental_models` rather than `animal_models` under the CLAUDE.md rule, but the organism would be *Mus musculus*, which is unusual for that section.
- NAMO has no class for ex vivo tissue slices at all, so `namo_type` would have had to stay unbound. The same gap applies to the ex vivo skin platform that the senescence and photoaging modules already use.

The cross-organ result was filed separately as #10313, as a module discussion entry on where the conserved chain diverges by organ, rather than as a second model link.

A wider finding from the same search: there is no multi-organ or organ-agnostic fibrosis-on-chip or microphysiological system. The chip and organoid fibrosis literature is organ-partitioned (liver-on-chip, lung-on-chip, kidney microfluidics, dermis-on-chip). The organ-agnostic platforms are the older, simpler ones: crowded fibroblast culture (Scar-in-a-Jar, which became the module's model in [#10282](https://github.com/monarch-initiative/dismech/pull/10282)) and tissue slices.

## 3. A documentation gap that looked like a vocabulary gap

The original #9935 PR body said `namo_type` was omitted because no NAMO class fit. That was corrected the next day: the check had been made against the four classes listed as "in scope" on the [NAMO rare-disease models project page](https://dismech.monarchinitiative.org/pages/projects/NAMO_RD_MODELS.html) (`Organoid`, `OrganOnChip`, `CellLineModel`, `TwoDCellCulture`), not against NAMO itself, which defines 56 classes.

The knowledge base already used `namo:InducedPluripotentStemCellDerivedModel` outside that list, and now `namo:CoCulture` as well, so the page was behind practice and easy to mistake for the full vocabulary. The reviewer noted that the page claims its list "was verified against the current NAMO schema snapshot," which makes the drift harder to spot. Updating that list was flagged as a separate one-line change so the next curator does not repeat the omission for the same reason.

## What this means for the schema evaluation

- `namo_type` is a bare `uriorcurie` with no enum constraint and no validator, so nothing gates a wrong or missing binding. The checks above were done by reading NAMO's class definitions by hand.
- Two real vocabulary gaps on the NAMO side: a non-perfused, gravity-linked microphysiological plate, and ex vivo tissue slices.
- One process gap on the dismech side: a project page's "in scope" subset standing in for the vocabulary. A curator needs to check NAMO itself, or the page needs to say it is a subset.
