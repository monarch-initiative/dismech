# Tetanus neonatorum literature sweep

Date: 2026-10-26

## Scope

This note records the neonatal-tetanus-specific sources mined after the original
Falcon/OpenScientist deep-research attempt hung without producing an artifact.
The KB entry `kb/disorders/Tetanus_Neonatorum.yaml` uses the general tetanus
2025 review for the conserved tetanospasmin transport and SNARE-cleavage
mechanism, then uses neonatal-specific sources for cord inoculation, clinical
presentation, and global burden.

## Cache-verified neonatal sources

### PMID:9822366 — Montana neonatal tetanus case investigation

This MMWR report verifies the defining acquisition route for the subtype: a
newborn of an unimmunized mother developed tetanus after nonsterile clay was
applied to the umbilical cord. It supports both the `transmission:` route and
the environmental trigger onto `Umbilical Clostridium tetani Spore
Contamination`.

### PMID:27573092 — AAP umbilical-cord-care review

This clinical report documents why the cut neonatal cord is a permissive
bacterial-growth niche: the devitalized cord substrate can be colonized by
bacteria and gives direct access to the neonatal bloodstream. It supports the
`Devitalized Cord Germination` pathophysiology node.

### PMID:9279625 — Pakistan topical-antimicrobial case-control study

This population-based matched case-control study found that continuous topical
antimicrobial use at delivery and during the first post-delivery days was
strongly protective against neonatal tetanus even after other delivery and cord
care practices were controlled. It supports the preventive cord-care treatment.

### PMID:22322126 — Pakistan chlorhexidine cord-care cluster-randomized trial

This cluster-randomized trial in rural Pakistan tested 4% chlorhexidine
umbilical-cord cleansing by traditional birth attendants and family members. It
reported reduced omphalitis and neonatal mortality with chlorhexidine cord
application, supplying direct evidence for chlorhexidine as the cord-care
therapeutic agent in the clean antimicrobial cord-care treatment.

### PMID:9783042 — 207-newborn neonatal-tetanus series

This Erciyes University series is neonatal-specific and clinically useful:
failure to suck and twitching were the most frequent symptoms, 97 of 207
newborns died, and apnea was the most frequent first-week cause of death. It
supports the `Poor suck`, `Reflex Muscle Spasms`, `Apnea`, and
`clinical_burden:` additions.

### PMID:21240163 — Bangladesh neonatal-tetanus series

This Infectious Disease Hospital series describes a one-year cohort of neonatal
tetanus admissions in Dhaka. It gives a 52.9% overall mortality and lists common
morbidities including lock jaw, inability to suck, and abdominal rigidity, while
also identifying lack of antenatal care, untrained delivery, and unclean cord
care as risk factors. It supports the `Trismus` phenotype and reinforces
high-burden clinical classification.

### PMID:39024183 — 2024 MMWR MNTE surveillance update

This global Maternal and Neonatal Tetanus Elimination update gives the burden
context that a four-PMID disease mechanism entry otherwise lacked. It reports
the 2000-to-2021 worldwide decrease in reported neonatal tetanus cases and
estimated neonatal tetanus deaths, explains that neonatal deaths are
model-estimated because underreporting is expected in remote areas, and records
the WHO elimination benchmark of fewer than one case per 1,000 live births in
each district. It supports the `prevalence:` surveillance-incidence record and
the global mortality evidence in `clinical_burden:`.

## Curation notes

- The subtype is mechanistically justified because the neonatal disease is
  initiated through the umbilical stump rather than a later traumatic wound.
- Maternal tetanus-toxoid vaccination and clean antimicrobial cord care belong
  in this child entry because both prevent the neonatal umbilical acquisition
  route.
- Established disease management needs to keep source control, anaerobic
  antibiotics, and antitoxin separate: the first two stop further toxin
  secretion at the umbilical focus, while antitoxin neutralizes unbound toxin
  before motor-axon uptake.
