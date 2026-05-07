# Bazex-Dupre-Christol Syndrome Deep Research Fallback

## Scope

This fallback artifact supports curation of Bazex-Dupre-Christol syndrome
(BDCS), represented by MONDO:0010535 and the structured hereditary Orphanet
record ORPHA:113.

## Structured Sources

- ORPHA:113 provides the hereditary BDCS definition, synonyms, X-linked dominant
  inheritance, neonatal/infancy onset, ultra-rare worldwide prevalence, and 15
  HPO phenotype-frequency rows.
- ORPHA:166113 describes adult-onset paraneoplastic acrokeratosis of Bazex. It
  shares the ambiguous label "Bazex syndrome" but is clinically distinct from
  hereditary BDCS; its phenotype rows were not imported.

## PubMed and Guideline Sources Used

- PMID:35986704: eight-family copy-number study identifying noncoding Xq26.1
  duplications and likely ARHGAP36 dysregulation as the current causal model.
- PMID:28869610: ACTRT1/eRNA inherited and sporadic basal-cell-carcinoma study
  supporting Hedgehog pathway activation in a BDCS-associated mechanism, used
  as mechanistic context because newer work argues ACTRT1 loss-of-function is
  unlikely to be the primary BDCS cause.
- PMID:33972689: ARP-T1-associated BDCS tissue/cell study supporting shortened
  cilia and ciliopathy-like skin-cancer biology.
- PMID:29808590: clinical/molecular review summarizing the classic BDCS triad
  and missed counseling/follow-up opportunity with delayed diagnosis.
- PMID:8782050: Scottish family report supporting X-linked dominant inheritance,
  hair follicle disorder framing, and early-onset/familial BCC differential
  diagnosis.
- PMID:18304168: mother-child report supporting early-life follicular, hair,
  milia, hypohidrosis, and basal-cell features.
- PMID:8129412: large family report supporting clinical pattern, sex-dependent
  expression, and X-linked dominant inheritance.
- PMID:40015599: recent family report confirming the Xq26.1 duplication in an
  additional family.
- DOI:10.1111/ddg.15566: basal cell carcinoma guideline supporting surgical
  removal as first-choice management for most BCC lesions.

## Curation Boundaries

- All ORPHA:113 HPO phenotype-frequency rows are represented.
- ORPHA:166113 phenotypes were deliberately excluded because that record is a
  distinct paraneoplastic condition rather than hereditary BDCS.
- The genetic section uses Xq26.1 duplication-mediated ARHGAP36 dysregulation as
  the primary current model, while retaining ACTRT1/ARP-T1 ciliary and Hedgehog
  evidence only as mechanistic context.
- Treatment curation is limited to lesion-directed surgical removal of basal
  cell carcinomas and genetic counseling because those have quotable cached
  evidence in the current source set.

## Provider Attempts

- `timeout 75s just research-disorder falcon
  Bazex_Dupre_Christol_Syndrome` was terminated by the timeout
  (signal 15 / exit 124) before producing a provider artifact.
- `timeout 75s just research-disorder openai
  Bazex_Dupre_Christol_Syndrome` was terminated by the timeout
  (signal 15 / exit 124) before producing a provider artifact.

The curation was completed from structured Orphanet rows and cached
PubMed/guideline evidence to avoid blocking on provider availability.
