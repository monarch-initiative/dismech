---
provider: codex
model: gpt-5
date: '2026-04-19'
issue: 1507
focus: phenotype section only
---

## Question

Make the phenotype section of `kb/disorders/Pycnodysostosis.yaml` as complete
and evidence-backed as possible using exact PMID-supported phenotype evidence,
while avoiding an unrelated broad rewrite.

## Selected PMID-backed phenotype evidence

- `PMID:8703060`
  Foundational clinical description supporting generalized osteosclerosis and
  short stature.
- `PMID:21569238`
  Review of 159 reported patients supporting the typical core phenotype set of
  short stature, increased bone density with pathologic fractures, and open
  fontanels/sutures.
- `PMID:11474477`
  Eight-child cohort supporting delayed fontanel closure, obtuse mandibular
  angle, delayed tooth eruption, enamel hypoplasia, clavicular dysplasia,
  proptosis, and nail dysplasia.
- `PMID:28576543`
  Eight-patient ENT series supporting brachydactyly/short digits, blue sclerae,
  midfacial hypoplasia, micrognathia, proptosis, malocclusion, and sleep apnea.
- `PMID:38532649`
  Dedicated oro-dental cohort supporting dental crowding and dental
  malocclusion.
- `PMID:40523612`
  Systematic review of 69 reported patients supporting frontal bossing,
  unclosed cranial sutures, midfacial hypoplasia, micrognathia, obtuse gonial
  angle, and severe dental crowding.

## Curation decisions

- Replaced the overly broad `HP:0011002` `Osteopetrosis` mapping with
  `HP:0005789` `Generalized osteosclerosis`.
- Split the prior broad open-fontanelle claim into `Delayed closure of the
  anterior fontanelle` and `Delayed cranial suture closure`.
- Added only phenotypes directly named in abstracts or abstract result lines.
- Kept phenotype ontology terms specific but avoided terms that were more
  specific than the abstract wording could safely support.
- Omitted `frequency:` and structured `onset:` annotations because the
  available quantitative signals were cohort- or review-specific and not clean
  whole-disease estimates.
