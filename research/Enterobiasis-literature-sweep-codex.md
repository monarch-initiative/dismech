---
provider: codex
model: gpt-6
harness: targeted PubMed and public-health literature sweep
cached: false
generated: '2026-11-14T07:51:08Z'
template_variables:
  disease_name: Enterobiasis
  mondo_id: MONDO:0005746
  category: Infectious Disease
verification:
  searches_run: 3
  sources_fetched: 3
  full_text_sources_fetched: 2
  abstract_only_sources_fetched: 1
note: >-
  Provenance artifact generated for the Enterobiasis new-entry PR. The sweep
  used targeted searches for Enterobius vermicularis, enterobiasis, pinworm
  life cycle, Scotch-tape diagnosis, and mebendazole/albendazole/pyrantel
  therapy. The authoritative, snippet-validated claims live in
  kb/disorders/Enterobiasis.yaml; do not import claims from this file without
  fetching the cited source into references_cache/ and validating exact
  snippets with the project reference validator.
---

# Enterobiasis literature sweep

## Scope decision

Enterobiasis is the named human pinworm disease caused by *Enterobius
vermicularis* (MONDO:0005746). The curated entry should be a separate clinical
entity rather than a row under Dientamoebiasis or a broad Rhabditida grouping:
the pinworm is the actual intestinal nematode agent here, while in the
Dientamoebiasis entry *E. vermicularis* eggs are only a proposed vehicle for
*Dientamoeba fragilis* co-transmission.

## Sources selected

| PMID | Article | Use in curation |
|---|---|---|
| PMID:31064642 | Wendt et al. 2019, *Dtsch Arztebl Int*, “The Diagnosis and Treatment of Pinworm Infection” | Main source for the direct human gastrointestinal life cycle, infective eggs within 4–6 h of oviposition, cecal and ascending-colon adult worms, nocturnal perianal oviposition, scratch-mediated egg dispersal, adhesive eggs, Scotch-tape microscopy, and the review’s treatment synthesis. |
| PMID:42267275 | Albasheer et al. 2026, *Front Public Health*, “Pinworm (*Enterobius vermicularis*) in children and adults: a practice-oriented narrative review and household-school algorithm” | Main source for the household/school transmission framing, perianal-pruritus and sleep-disturbance phenotype wording, three-drug two-dose treatment, and synchronized household treatment. |
| PMID:38288810 | Leung et al. 2025, *Curr Pediatr Rev*, “Pinworm (*Enterobius Vermicularis*) Infestation: An Updated Review” | Abstract-only corroboration for recurrence through autoinfection and for hygiene measures; not used for exact YAML evidence because fuller 2019 and 2026 reviews were available. |

## Content checklist

- **Epidemiology:** The entry captures the review's >1 billion worldwide burden
  estimate, the near-20% point prevalence among European kindergarten and
  primary-school pupils, and measured Norwegian and Estonian pediatric
  Scotch-tape survey estimates.
- **Phenotypes:** The entry captures the characteristic nocturnal perianal
  pruritus, sleep disturbance, nocturnal enuresis, impaired daytime
  concentration, and perianal dermatitis. Rare ectopic vulvovaginal migration is
  modeled narrowly through dysuria and abnormal vaginal discharge; abdominal
  pain and irritability were left out because the reviews describe them as
  nonspecific.
- **Life cycle and transmission:** The entry records the direct human life cycle
  with OPL-bound egg and adult-worm stages and a fecal-oral/autoinfection/fomite
  transmission row. Non-human reservoirs and vectors are intentionally absent:
  the 2019 review describes *E. vermicularis* as strictly human-pathogenic and
  domestic pets as irrelevant natural reservoirs.
- **Pathophysiology:** The central disease-specific mechanism is split into
  adult cecal and colonic colonization, nocturnal female migration with perianal
  oviposition, scratch-mediated egg dispersal/autoinfection, and rare
  vulvovaginal pinworm migration. A more granular itch neuroimmune mechanism was
  not modeled because neither cached review provided a disease-specific
  molecular mechanism for pinworm-induced pruritus.
- **Diagnostics:** The entry captures early-morning perianal adhesive-tape
  microscopy, the sensitivity increase from three separate mornings, and the
  reason stool ova-and-parasite testing is insensitive.
- **Treatments:** The entry splits benzimidazole therapy from pyrantel/pyrvinium
  adulticidal therapy and adds synchronized household pharmacotherapy to reduce
  reinfection. Extended pulse regimens for refractory recurrence were left out
  because the 2026 review characterizes that evidence as pragmatic observational
  evidence and expert consensus rather than randomized trials.
- **Differentials and controversies:** Appendicitis was intentionally omitted.
  The 2019 review says the role of *E. vermicularis* in acute appendicitis has
  long been controversial and that causality has not been reliably demonstrated.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.
