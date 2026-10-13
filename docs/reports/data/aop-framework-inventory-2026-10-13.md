# DisMech Adverse Outcome Pathway inventory: issues and PRs by gingin77

Written 2026-10-13 against dismech `main` at commit `3eb0796817`, from the GitHub history of monarch-initiative/dismech (first compiled 2026-10-08). Scope: the issues and PRs that compared dismech's causal model against the Adverse Outcome Pathway (AOP) framework and the EMOD evidence model, or that tried to derive AOPs from dismech pathographs. Assays and New Approach Methodologies are inventoried separately in [the assay and NAM inventory](../nam-methods-inventory-2026-10-13.md); the AOP 38 liver fibrosis bridge test and the TDAR assay project stay there because each centres on a NAM or an assay. An issue and the PRs that answered it share one header. Status is as of the compile date.

---

## 1. AOP and EMOD framework alignment

### Explore how exposure modelling relates to the AOP framework ([#8309](https://github.com/monarch-initiative/dismech/issues/8309), closed; PR [#10002](https://github.com/monarch-initiative/dismech/pull/10002), merged)

Opened to map dismech's exposure to mechanism to outcome layer against MIE, KE, KER and AO; gingin77 introduced the EMOD Assay, Observation and KER Evidence classes as the measurement side to compare. [#10002](https://github.com/monarch-initiative/dismech/pull/10002) delivered [`projects/AOP_EMOD_ALIGNMENT.md`](https://dismech.monarchinitiative.org/pages/projects/AOP_EMOD_ALIGNMENT.html) with the lead use case across eight lead AOPs. Findings: 20 of 36 lead KERs cite nothing yet 18 are graded High, 14 of 35 KEs map cleanly to module nodes, all five chemical MIEs have nowhere to attach. Blockers: the pilot premise was wrong, the reviewer caught a false module claim, a weight-of-evidence grade is not evidence, and the role tag was deferred.

### Comparator change and "an AOP is not a mechanism boundary" ([#10344](https://github.com/monarch-initiative/dismech/issues/10344), closed; [#10687](https://github.com/monarch-initiative/dismech/issues/10687), open; PR [#10760](https://github.com/monarch-initiative/dismech/pull/10760), merged)

[#10344](https://github.com/monarch-initiative/dismech/issues/10344) asked the page to say why the pilot moved from AOP 17 to eight lead AOPs and to record that lead absorption and distribution are toxicokinetic nodes while ALAD inhibition is the MIE-shaped node. [#10687](https://github.com/monarch-initiative/dismech/issues/10687) arose when grouping androgen-axis KERs by parent AOP scattered one 24-edge group across 19 AOPs. [#10760](https://github.com/monarch-initiative/dismech/pull/10760) wrote both, with three rules: the AOP ID lives on the edge, is never a grouping key, and mechanisms are recovered as connected components. Blockers: every exposure entry triggers into a toxicokinetic node, so the assumed MIE correspondence is wrong; a networkFinder render disagreed on component count, so measurements were withdrawn.

### Evidence cannot record how a causal claim was measured ([#10772](https://github.com/monarch-initiative/dismech/issues/10772), closed; PR [#11394](https://github.com/monarch-initiative/dismech/pull/11394), merged)

`EvidenceItem` can say the study category but not the system or method, such as voltage clamp in rabbit sino-atrial myocytes or a FRET cAMP biosensor, which EMOD structures explicitly. [#11394](https://github.com/monarch-initiative/dismech/pull/11394) added a comparison subsection with corrected figures: 564 `assays` entries in 87 files, none bound to any OBI term, only two on a pathophysiology node; ECO types evidence, OBI types the assay. Blockers: the slot exists but curators were told not to use it, OBI has no OAK adapter or enum cache, ECO is absent, and no schema change was proposed; a back-pointer from evidence to model was recorded as the likely fix.

### Six open AOP schema questions ([#10272](https://github.com/monarch-initiative/dismech/issues/10272), open)

Spun out of [#10257](https://github.com/monarch-initiative/dismech/pull/10257) to hold what the schema cannot express: a KE cross-reference on a node, where an AO correspondence attaches, declaring `aop` prefixes, a population level in `BiologicalScaleEnum`, species applicability on a mechanism, and marking a node toxicokinetic. Nothing has merged; gingin77 noted it was created from a misunderstanding but kept it for discussion. Blockers: the bot found the prefix question near-settled by `namo:` precedent, the population scale should be a recorded no, species applicability is blocked by free-text `AnimalModel.species`, and the toxicokinetic question belongs to the aggregate exposure pathway framework.

### AOP-derived causal evidence use cases ([#10454](https://github.com/monarch-initiative/dismech/issues/10454), open) and AOP-Wiki data error inventory ([#10773](https://github.com/monarch-initiative/dismech/issues/10773), open)

[#10454](https://github.com/monarch-initiative/dismech/issues/10454) proposes a project page after KER3445, PDE inhibition to increased cAMP in AOP 558, proved false in the healthy heart and true only per isoform, compartment or disease state as measured by cytosolic and SERCA2-targeted FRET cAMP biosensors and patch-clamp. gingin77 added that a 29.41 percent completion score identifies 1,536 stub KERs. [#10773](https://github.com/monarch-initiative/dismech/issues/10773) asks for a register after AOP 552 cited DOIs resolving to other papers; the bot found 13 of 16 defective. Blockers: AOP-Wiki grades the KER High with empty evidence sections, `biological_scale` has nothing subcellular, readout choice flips disease dependence, no PR for either.

### AOP-Wiki and MIE-KER-capture skills ([#10456](https://github.com/monarch-initiative/dismech/issues/10456), closed; PR [#10464](https://github.com/monarch-initiative/dismech/pull/10464), merged)

Two locally working skills for turning AOP-Wiki Key Events into verified dismech edges needed committing, blocked until `aop_wiki_cli` was installable with uvx. [#10464](https://github.com/monarch-initiative/dismech/pull/10464) added the [aop-wiki](https://github.com/monarch-initiative/dismech/blob/main/.claude/skills/aop-wiki/SKILL.md), [mie-ker-capture](https://github.com/monarch-initiative/dismech/blob/main/.claude/skills/mie-ker-capture/SKILL.md) and [ker-evidence-triage](https://github.com/monarch-initiative/dismech/blob/main/.claude/skills/ker-evidence-triage/SKILL.md) skills, carrying the stub-KER gate with its scoring proof, the connected-components rule, and the finding that `conforms_to` is not the test since 60 percent of disorders declare none. Blockers: two CHANGES_REQUESTED rounds over a wrong KE example and a false config sentence; gingin77 held the PR to fix a claim that Key Events are organ-agnostic; the uvx ref is unpinned; AOP-Wiki remains non-citable.

## 2. Seeding AOPs from dismech, and edge confidence

### Which dismech pathographs could seed Adverse Outcome Pathways (PR [#11852](https://github.com/monarch-initiative/dismech/pull/11852), merged)

Opened to find entries holding a connected, node-measured, edge-cited causal chain usable as an AOP backbone, working [`Left_Ventricular_Noncompaction_8`](https://dismech.monarchinitiative.org/pages/disorders/Left_Ventricular_Noncompaction_8.html) and [`Skeletal_Fluorosis`](https://dismech.monarchinitiative.org/pages/disorders/Skeletal_Fluorosis.html) into AOP-Wiki vocabulary. Merged a [census report](https://github.com/monarch-initiative/dismech/blob/main/docs/reports/aop-derivable-measurable-chains-2026-09-10.md), derivations and [`scripts/aop_chain_census.py`](https://github.com/monarch-initiative/dismech/blob/main/scripts/aop_chain_census.py) behind `just aop-chain-census`. Headline: edge evidence is about thirty-five times more available than node measurability, one entry clears both screens at five nodes, and the constraint on deriving AOPs is `modeled_mechanisms` coverage, not more reading. Blockers: exposures never reach a molecular initiating event because every exposure edge lands on an unmarked toxicokinetic node; KE 18 cannot be reused for AhR under-activation; three terminal fluorosis events have no AOP-Wiki counterpart.

### A causal edge cannot carry a confidence ([#10949](https://github.com/monarch-initiative/dismech/issues/10949), open, authored by another contributor, commented)

gingin77's 2026-09-16 comment brought the measurement from [#11852](https://github.com/monarch-initiative/dismech/pull/11852): 37,247 downstream edges, 43 percent cited, and 8,390 uncited DIRECT edges indistinguishable from 3,067 declared hedges. The methods point is that AOP-Wiki grades the claim through KER weight of evidence while dismech grades the citation, and seeding AOPs requires cited edges, so a confidence slot on `CausalEdge` should be settled before the connectivity check in [#7855](https://github.com/monarch-initiative/dismech/issues/7855). Nothing has merged. Blocker: the bot wants a maintainer decision jointly with the `causal_effect` polarity question before changing the edge shape.

---

## Methods actually landed in kb/ or tooling

| Method or assay | Entry or module | Item |
|---|---|---|
| AOP chain census script | [`scripts/aop_chain_census.py`](https://github.com/monarch-initiative/dismech/blob/main/scripts/aop_chain_census.py) (`just aop-chain-census`) | [#11852](https://github.com/monarch-initiative/dismech/pull/11852) |
| AOP-Wiki, MIE-KER-capture, KER-evidence-triage skills | [aop-wiki](https://github.com/monarch-initiative/dismech/blob/main/.claude/skills/aop-wiki/SKILL.md), [mie-ker-capture](https://github.com/monarch-initiative/dismech/blob/main/.claude/skills/mie-ker-capture/SKILL.md), [ker-evidence-triage](https://github.com/monarch-initiative/dismech/blob/main/.claude/skills/ker-evidence-triage/SKILL.md) | [#10464](https://github.com/monarch-initiative/dismech/pull/10464) |

## Blockers that recur across the inventory

- Exposures land on toxicokinetic nodes, never on a molecular initiating event, and nothing marks a node toxicokinetic ([#10344](https://github.com/monarch-initiative/dismech/issues/10344), [#11852](https://github.com/monarch-initiative/dismech/pull/11852)).
