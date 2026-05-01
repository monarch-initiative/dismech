---
provider: manual_pubmed_review
model: n/a
cached: false
start_time: '2026-04-19T06:45:00Z'
end_time: '2026-04-19T07:35:00Z'
duration_seconds: 3000.0
citation_count: 12
notes: >
  Manual phenotype-focused curation review for Fibrodysplasia Ossificans
  Progressiva. Scope was limited to the phenotype section of
  `kb/disorders/Fibrodysplasia_Ossificans_Progressiva.yaml`. Primary PubMed
  abstracts were fetched with `just fetch-reference`; ontology mappings were
  checked against HPO labels and refined to favor phenotype specificity without
  overclaiming unsupported frequency or onset.
---

## Question

Enhance the phenotype section for Fibrodysplasia Ossificans Progressiva with
clinically important, PMID-backed manifestations only; add onset/frequency only
when directly supported; remove or soften unsupported phenotype claims.

## Output

# FOP Phenotype Curation Note

## Scope decisions

- Kept the edit phenotype-only; no unrelated mechanism, treatment, or prevalence
  rewrites were performed.
- Replaced weak phenotype evidence that had been anchored to a mouse palovarotene
  paper with human clinical abstracts that directly describe the phenotype.
- Added missing but clinically important manifestations that recur across FOP
  case series and natural-history studies: flare-up pain/swelling, cervical
  spine anomalies, neck motion limitation, short thumb, conductive hearing loss,
  restricted mouth opening, and proximal tibial osteochondromas.
- Used structured `phenotype_contexts` only where onset was directly stated in
  the abstract.
- Kept frequency qualifiers only where an abstract gave a clear count or
  percentage that could be mapped directly to the HPO-aligned frequency bands.

## Key phenotype evidence used

### Hallux malformation

- PMID:21116899
  > A shortened great toe and hallux valgus were frequently found in patients with FOP.
- PMID:21116899
  > These findings were thought to exist from birth and may be a key to an early diagnosis.

### Heterotopic ossification

- PMID:36152026
  > FOP is characterized by painful, recurrent flare-ups, and disabling, cumulative heterotopic ossification (HO) in soft tissues.
- PMID:17572636
  > Individuals with fibrodysplasia ossificans progressiva are born with malformations of the great toes and develop a heterotopic skeleton during childhood

### Flare-up manifestations

- PMID:26564023
  > Fibrodysplasia ossificans progressiva (FOP) is a rare disorder characterized by episodes of acute pain and heterotopic ossification of soft tissue, and progressively limited physical function and social participation.
- PMID:27025942
  > The most common presenting symptoms of flare-ups were swelling (93%), pain (86%), or decreased mobility (79%).

### Axial skeletal and mobility manifestations

- PMID:7929490
  > Twenty-six (65 per cent) of the patients had scoliosis, which, according to the clinical records and the recollection of the patients, had been present during childhood.
- PMID:15959366
  > In the FOP patient group, characteristic anomalies, including large posterior elements, tall narrow vertebral bodies,and fusion of the facet joints between C2 and C7, were observed.
- PMID:15959366
  > Generalized neck stiffness and decreased range of motion were noted in most children with FOP.
- PMID:15959366
  > FOP patients exhibit a characteristic set of congenital spine malformations.

### Additional skeletal manifestations

- PMID:25343126
  > The thumb shortening and cervical spine abnormalities are other skeletal features often observed in FOP.
- PMID:18245597
  > Ninety percent of all patients had osteochondroma of the proximal part of the tibia.

### Craniofacial, auditory, and respiratory manifestations

- PMID:28390760
  > As the condition progresses, HO leads to joint ankylosis, breathing difficulties, and mouth-opening restriction, and it can shorten the patient's lifespan.
- PMID:10499116
  > The findings of both studies indicate that individuals with FOP are at risk for hearing loss and that the type of loss is predominantly conductive in nature
- PMID:40597333
  > Spirometry showed a uniform pattern of restrictive physiology in all eight participants with no significant difference amongst the group.
- PMID:20194327
  > The most common causes of death in patients with fibrodysplasia ossificans progressiva were cardiorespiratory failure from thoracic insufficiency syndrome (54%; median age, forty-two years) and pneumonia (15%; median age, forty years).

## Modeling decisions

- `HP:0011986` `Ectopic ossification` was used instead of the narrower
  muscle-only term because FOP affects fascia, tendons, and ligaments as well
  as muscle.
- `HP:0002949` `Fused cervical vertebrae` was used as the best HPO anchor for
  the congenital cervical fusion phenotype, while the `preferred_term`
  preserves the broader clinical description of the cervical anomaly pattern.
- `HP:0012531` `Pain` and `HP:0000969` `Edema` were used with more specific
  `preferred_term` labels for flare-up pain and swelling because HPO does not
  offer an FOP-specific flare-up term.
- Frequency was retained only for:
  - `Scoliosis` from 26/40 patients = 65% (`FREQUENT`)
  - `Proximal Tibial Osteochondromas` from 90% of patients (`VERY_FREQUENT`)
- Earlier blanket frequency claims for joint immobility, joint stiffness, and
  restrictive ventilatory defect were removed because the prior citations did
  not directly support those bands.
