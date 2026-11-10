# Finding 6 of the Noonan alternative-models report is a false negative — 2026-11-10

Scope: `research/Noonan_Syndrome-alternative-models-deep-research-openscientist.md`,
the OpenScientist run commissioned for the RAF1 cardiac axis of
`kb/disorders/Noonan_Syndrome.yaml` (PR #16394).

**Anyone reading that report's Finding 6 should know that one of its two
"confirmed-empty" search campaigns is wrong.** The study it reports as
unretrievable exists, is cited six times in the disease entry committed in the
same pull request, and is the entry's only human, loaded, multicellular model
on the cardiac axis.

The report itself is left exactly as the provider returned it. Research reports
under `research/` are the raw output of a run, and no committed report in this
repository has been edited after creation; a correction belongs here, not in
the provider's bytes.

## What the report claims

Finding 6 is headed "Confirmed-empty systems: human Noonan myocardial
slices/explants and loaded RASopathy 3D cardiac models", and reports that a
search campaign for

> Human Noonan myocardial tissue — slices, explants or resected surgical tissue
> with contractility or calcium-handling readouts

returned no Noonan/RASopathy-specific study. It names three queries it ran, and
concludes that the Cardiomyocyte Hypertrophy node "currently has no model that
carries haemodynamic load *plus* a human genome *plus* multicellular
(fibroblast/endothelial) compartments", and that an engineered heart tissue
"would be the missing ExperimentalModel".

## What exists

Hamers et al. 2025, *ESC Heart Failure* (`PMID:39573843`):

> Trametinib alters contractility of paediatric Noonan syndrome-associated
> hypertrophic myocardial tissue slices.

Contracting right ventricular slices cut from myocardium resected at surgery
from a child with RASopathy-associated hypertrophic cardiomyopathy, cultivated
in biomimetic cultivation chambers under electrical stimulation, with
contractile force, force-frequency relationship and post-pause potentiation
measured before and after trametinib. That is the first campaign's target
description, point for point.

It is curated in the entry as the `Paediatric Noonan syndrome myocardial tissue
slice model`, with two readouts, and is cited six times.

## What follows for a reader

- **The gap Finding 6 identifies is narrower than it states.** A human, loaded,
  multicellular system on this axis exists. What does not exist, as far as that
  campaign searched, is an *engineered* heart tissue built from RASopathy
  iPSC-cardiomyocytes — a different and still-open gap.
- **The report's closing suggestion is weakened by the same study.** It proposes
  a loaded human system as "the ideal platform to test the
  therapeutic-versus-toxicity question directly". The slices already speak to
  that question: trametinib lowered developed force while improving calcium
  handling in the same tissue, which is the only dataset in the entry touching
  both directions of MEK inhibition at once.
- **The report's hedge is accurate and worth keeping in view.** Finding 6 says
  in its own text that it is "a reported-empty result, not a claim of
  non-existence". That caveat is correct and is what distinguishes this from a
  fabrication. The finding is still wrong in substance, and the hedge did not
  stop it from driving a conclusion about what is missing.

## Why this is recorded rather than fixed in place

A negative-existence claim is the one assertion in a research report that no
gate can reach. Reference validation on this run was clean — 16 citations
checked, 16 resolved, zero unresolved — because that check asks whether cited
identifiers resolve, not whether an uncited study exists. Term validation was
likewise clean. Nothing in the pipeline could have caught this, and nothing
will catch the next one.

The study was found independently, from PubMed, while assembling the citations
the entry needed. The report was commissioned afterwards and did not surface it.
That ordering is the reason the error was visible at all: a curator who had
relied on the report alone would have recorded the gap as the report described
it.

See also `research/Noonan_Syndrome-alternative-models-deep-research-openscientist.md`
and the entry's `Paediatric Noonan syndrome myocardial tissue slice model`.
