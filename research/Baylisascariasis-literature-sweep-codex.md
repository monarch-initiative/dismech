# Baylisascariasis literature sweep

This curation sweep checked core Baylisascariasis clinical reviews, a 2025
scoping review of published human infections, a 2025 MMWR on two Los Angeles
pediatric cases, and neurology-focused reviews before creating
`kb/disorders/Baylisascariasis.yaml`.

## Sources used

- **PMID:16223954** — open full-text 2005 *Clinical Microbiology Reviews*
  review. Used for the organism identity, raccoon-latrine egg ingestion as the
  human exposure route, pica/geophagia risk, CNS larval invasion, diagnosis
  with serology or rare tissue larvae, treatment limits after CNS invasion, and
  prevention framing.
- **PMID:26960940** — open full-text 2016 update review. Used for the
  Ascarididae placement of *Baylisascaris procyonis*, direct and indirect life
  cycles, raccoons as definitive hosts, humans as paratenic hosts, eggs
  embryonating to infective L3 larvae, accidental CNS and eye migration, and the
  recommendation for early albendazole with corticosteroids.
- **PMID:40671903** — open full-text 2025 scoping review. Used to summarize 60
  published human infections, the counts of neurological versus ocular-only
  disease, neurological outcomes, ocular vision-loss outcomes, pica/geophagia
  and raccoon-latrine risk, first-reported neurologic sign frequencies,
  peripheral and CSF eosinophilia frequencies, MRI white-matter abnormalities,
  serologic test use, and limits of case-report literature for estimating
  incidence.
- **PMID:40742893** — open full-text 2025 MMWR report. Used for two recent
  pediatric Los Angeles County cases, the raccoon-feces exposure investigation,
  eosinophilic meningitis with peripheral and CSF eosinophilia, MRI
  abnormalities, rBpRAG1 immunoblot testing at CDC, albendazole and
  corticosteroid treatment, and the prophylactic treatment window after
  high-suspicion oral exposure.
- **PMID:23829916** — neurology review abstract. Used for compact support of
  neural larva migrans with CSF and peripheral eosinophilia, diagnosis by
  larvae/epidemiology/serology/CNS imaging, ocular larva migrans as DUSN, and
  photocoagulation of intraocular larvae.
- **PMID:15715975** — CNS severe/fatal disease review abstract. Used as an
  older check on the diagnostic challenge of CNS Baylisascariasis and the
  importance of prevention given poor treatment outcomes.

## Lump/split decision

`stubs/Baylisascariasis.yaml` carried no MONDO descendants and listed only
`Ascaridida infectious disease` as a parent, so it was curated as a leaf
infectious disease rather than a grouping. The disease is caused by
*Baylisascaris procyonis* and was bound to `NCBITaxon:6259`; the definitive host
raccoon was bound to `NCBITaxon:9654`.

## Exclusions and term decisions

- **Other *Baylisascaris* species** were left out of the structured
  `infectious_agent`. Related species from skunks, badgers, and kinkajous can
  cause larva migrans, but the reviews identify *B. procyonis* as the prevalent
  and pathogenic agent for recognized human Baylisascariasis.
- **Dogs with patent intestinal infection** were left out of the life-cycle
  hosts because the 2025 scoping review notes they may harbor patent infections
  only rarely; the conserved human exposure route remains raccoon fecal egg
  contamination.
- **More than 150 paratenic bird and mammal species** were carried in prose
  rather than enumerated in `agent_life_cycle.hosts` because they are a broad
  ecological range rather than a clinically necessary list for the human disease
  entry.
- **Diffuse unilateral subacute neuroretinitis** is modeled as its own node
  downstream of retinal larva localization, while the phenotype record stays at
  `HP:0000505` visual impairment because the phenotype only needs to capture the
  vision-loss outcome rather than create an unsupported retinal-diagnosis term.
- **Visceral larva migrans** remains outside the structured graph. The scoping
  review found one eosinophilic cardiac pseudotumor among 60 published
  infections, while the conserved, literature-rich branches are neural and
  ocular larva migrans.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.
