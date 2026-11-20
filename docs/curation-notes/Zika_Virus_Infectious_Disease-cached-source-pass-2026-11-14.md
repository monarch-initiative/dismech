# Zika Virus Infectious Disease cached-source completeness pass

Date: 2026-11-14
Curator: Codex
PR: monarch-initiative/dismech#17708

## Scope

This pass re-read the generated PubMed caches already supporting
`kb/disorders/Zika_Virus_Infectious_Disease.yaml` and one new generated cache
for the ZIKV NS5/STAT2 interferon-antagonism paper. It focused on the acquired
infection represented by `MONDO:0018661`, leaving the fetal
neural-progenitor-cytopathy arm to `Congenital_Zika_Syndrome`.

No external deep-research provider was run for this pass; the goal was to close
the concrete content gaps identified by the PR review from exact, locally
cached sources and to record the intentionally narrow scope of the entry.

## Key sources used

- PMID:19516034 — Yap Island outbreak abstract; supplied the RNA/neutralizing
  antibody diagnostic rule, probable-case handling for cross-reactive IgM, the
  dengue-serology caveat, the 73% recent-infection estimate among Yap residents
  at least 3 years old, the lack of hospitalizations/hemorrhage/deaths, and the
  Pacific `Aedes hensilli` vector note.
- PMID:27212660 — primary ZIKV NS5 functional study; supplied the STAT2-binding,
  proteasomal STAT2-degradation and type I interferon-signaling antagonism
  mechanism added as the ZIKV-specific molecular pathophysiology layer.
- PMID:26085147 — primary human-skin-cell study; continued to support the
  cutaneous inoculation and replication node and its dermal fibroblast,
  keratinocyte and dendritic-cell targets.
- PMID:39472938 — review synthesis for transmission routes, human incubation,
  dissemination from blood to systemic target tissues, acute myalgia/headache,
  Guillain-Barre syndrome associations and the absence of disease-specific
  public therapy.
- PMID:24739982 and PMID:25625872 — primary reports supporting blood-borne and
  sexual transmission routes.
- PMID:26862926, PMID:27443522 and PMID:33320867 — primary and review sources
  retained only to point from acquired maternal infection and viremic
  transplacental seeding into the separately curated congenital disorder.
- PMID:26948433 — outbreak case-control evidence for post-ZIKV
  Guillain-Barre syndrome.

## Findings added in this pass

### Diagnostic confirmation

The Yap outbreak paper explicitly separated confirmed disease, based on ZIKV
RNA or a ZIKV-specific neutralizing-antibody response, from probable disease
where IgM was present but the neutralizing-antibody response was potentially
cross-reactive. That is central to acquired ZIKV diagnosis because dengue
serology can also be positive in affected patients.

### Recent-infection prevalence in a closed island outbreak

The same paper estimated 73% recent infection among Yap residents aged 3 years
or older. This is best represented as an outbreak-period seroprevalence rather
than as a global endemic prevalence.

### Mild acquired-outbreak severity and symptomatic denominator

The Yap outbreak abstract also reports no Zika-attributed hospitalization,
hemorrhagic manifestations or death despite the high recent-infection estimate.
PMID:39472938 supplies the complementary review estimate that only 20-25% of
ZIKV-infected people develop noticeable symptoms, so the acute phenotype
frequencies are read on a symptomatic-case denominator.

### ZIKV-specific immune evasion

PMID:27212660 provides a compact molecular layer that differentiates this
pathograph from generic mosquito-borne flavivirus inoculation: ZIKV NS5 binds
human STAT2, drives proteasomal degradation of STAT2, and thereby suppresses
type I interferon signaling. The node conforms to the existing
`innate_antiviral_interferon_response#Viral Interferon Antagonism and Innate Immune Evasion`
module anchor.

### Acute phenotype wiring

`Bloodstream Dissemination and Systemic Tropism` already claimed acute systemic
symptoms. The six curated acute phenotypes — fever, skin rash, arthralgia,
myalgia, headache and conjunctivitis — therefore all belong downstream of that
dissemination node.

### Exposure and vector scope

ECTO has `ECTO:3000001` for viral exposure but no local mosquito-bite exposure
class. Local searches for `l~mosquito` and `l~arthropod` were recorded in the
entry and support keeping the current viral-exposure binding. The lifecycle
keeps only the two globally important epidemic Aedes vectors as structured
hosts but acknowledges that `Aedes hensilli` predominated in the Yap outbreak.

## Bounded topics

- The `Congenital_Zika_Syndrome` pointer subtype should remain a pointer rather
  than duplicating fetal neural-progenitor mechanisms in this acquired-infection
  entry.
- No rash-frequency upgrade was made because the currently cached Yap abstract
  only says rash was common; the exact percentage did not appear in the local
  cache.
- Clinical vaccine-trial rows were left for a later pass because the current
  entry's treatment statement only needs to say that no ZIKV-specific antiviral
  or publicly available vaccine exists.
