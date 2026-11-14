# Enterobiasis: cached-source completeness pass

This is a local literature sweep produced from the PubMed references already cached for the pull request. No external deep-research provider was used.

## Source set

| Reference | Role in this pass |
| --- | --- |
| PMID:31064642 | Full-text 2019 clinical review. Used for the human-only direct life cycle; eggs becoming infective 4-6 h after oviposition; cecal, appendiceal, and ascending-colon localization of adult worms; nocturnal perianal egg deposition; scratch-mediated egg dispersal and autoinfection; European and Scandinavian/Estonian prevalence estimates; asymptomatic/oligosymptomatic disease; enuresis and impaired concentration downstream of nocturnal pruritus; perianal excoriation/dermatitis/superinfection; Scotch-tape microscopy with the three-day sensitivity estimate; stool-microscopy limitations; benzimidazole ovicidal and adulticidal activity; pyrvinium inclusion; and simultaneous household treatment for recurrence. |
| PMID:42267275 | 2026 practice-oriented narrative review. Used for the household and school transmission framing, classic sleep-disturbance phenotype, rare vulvovaginal migration with dysuria, standard two-dose mebendazole/albendazole/pyrantel regimens, and same-day treatment of all household members regardless of symptoms. |
| PMID:38288810 | 2025 abstract-only update. Used as corroboration for the 30-40% asymptomatic fraction, three-morning tape-test sensitivity, stool-exam limitations, drug choices, and recurrence after otherwise effective pharmacotherapy. |

## Completeness cross-check

- Epidemiology now records the >1 billion worldwide burden estimate, the roughly 20% European kindergarten/primary-school point prevalence, the 18% Norwegian pediatric Scotch-tape positivity estimate with a 34% 6- to 11-year-old stratum, and the 24.4% Estonian kindergarten estimate.
- The pathophysiology graph now separates adult cecal and colonic colonization, nocturnal female migration/perianal oviposition, scratch-mediated egg dispersal/autoinfection, and rare ectopic vulvovaginal migration.
- The autoinfection loop feeds back from scratch-mediated egg dispersal to adult colonization, matching the direct anus-finger-mouth recurrence pathway described in the cached 2019 review.
- Perianal pruritus, sleep disturbance, nocturnal enuresis, diminished daytime concentration, perianal dermatitis, dysuria, and abnormal vaginal discharge are all causally connected to the relevant worm-migration or scratching mechanism.
- The `progression:` block records an oligosymptomatic/asymptomatic phase and a recurrent autoinfection phase, with the self-limited course when autoinfection does not occur.
- Diagnostics now state that three separate early-morning tape samples raise sensitivity versus a single Scotch-tape test, and a separate stool ova-and-parasite microscopy row explicitly marks stool microscopy as refuted/insensitive for pinworm eggs.
- Treatment now splits mebendazole/albendazole benzimidazoles from pyrantel/pyrvinium adulticidal therapy and adds a synchronized household pharmacotherapy row targeting the autoinfection/reinfection loop.

## Deferred or bounded items

- Appendicitis remains unmodeled because PMID:31064642 describes the relationship between *E. vermicularis* and acute appendicitis as controversial and not reliably causal.
- Abdominal pain and irritability remain unmodeled because the cached reviews describe them as nonspecific rather than as causal readouts of the characteristic perianal oviposition mechanism.
- Extended "pulse" regimens for refractory recurrence remain unmodeled because PMID:42267275 characterizes the supporting evidence as pragmatic experience and expert consensus rather than randomized-trial evidence.
