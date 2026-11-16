# Cryptosporidiosis literature sweep

Date: 2026-11-14

## Scope

This note records the sources mined while repairing the first Cryptosporidiosis
pull request after review. The entry stays at the MONDO genus-level
cryptosporidiosis scope and models C. hominis and C. parvum as predominant
etiologic species within that entry.

## Cache-verified sources

### PMID:37764167 — pediatric Cryptosporidium/Giardia review

This review anchors the genus-level cause, oocyst life cycle, water/food/household
transmission, global pediatric burden, intestinal epithelial injury, lamina
propria inflammation, barrier permeability, fluid/electrolyte disruption,
TNF-alpha/IL-8-associated mucosal inflammation, common gastrointestinal symptoms,
extraintestinal respiratory manifestations, undernutrition and
immunodeficiency host context, MBL2 susceptibility, stool microscopy, antigen,
nucleic-acid diagnostics, nitazoxanide positioning, and supportive care.

### PMID:27219054 — GEMS burden analysis

This multisite Global Enteric Multicenter Study analysis supplies population
incidence estimates for Cryptosporidium-attributable moderate-to-severe and
less-severe diarrhea in children younger than 24 months at African and Asian
sites. The KB entry uses its African-infant moderate-to-severe diarrhea
incidence estimate as a denominator-aware annual-incidence record.

### PMID:23440042 — IL21R deficiency with biliary Cryptosporidium

The IL21R primary-immunodeficiency report supplies human clinical support that
severe cellular immune defects can permit duodenal plus bile-duct
Cryptosporidium infection with fibrosis, chronic cholangitis, and liver disease.

### PMID:11398117 — Egyptian nitazoxanide randomized trial

The prospective randomized double-blind placebo-controlled study supports
nitazoxanide as an active small-molecule treatment in cryptosporidial diarrhea:
7-day diarrhea resolution was higher with nitazoxanide than with placebo.

### PMID:12423984 — Zambian pediatric nitazoxanide randomized trial

The pediatric randomized controlled trial supports nitazoxanide benefit in
HIV-seronegative children, records lack of benefit in HIV-seropositive children,
and reinforces that persistent diarrheal cryptosporidiosis in children is linked
to malnutrition and mortality.

### PMID:11103042 — HAART and AIDS-related cryptosporidiosis

This prospective HIV-positive case series supports antiretroviral therapy as an
immune-restoring treatment for AIDS-related cryptosporidiosis: patients who
responded to HAART eradicated cryptosporidial and microsporidial organisms.

### PMID:19212310 — AIDS-related cholangiopathy review

This review supports advanced HIV/AIDS as a biliary Cryptosporidium host context
and antiretroviral therapy as protective. It also links active HIV replication
plus Cryptosporidium parvum infection to cholangiocyte apoptosis in
AIDS-related cholangiopathy.

### PMID:22459705 — CD40 agonism in X-linked hyper-IgM biliary cryptosporidiosis

The X-linked hyper-IgM study identifies CD40 ligand mutation as the primary
immune defect, describes biliary Cryptosporidium as refractory to antimicrobial
therapy in XHM, and reports two patients with biliary C. hominis infection
refractory to nitazoxanide who were treated with the investigational CD40
agonist CP-870,893.

## Open gaps

- The entry records CD40LG deficiency as a susceptibility context only. The
  investigational CD40 agonist is not curated as a treatment because PMID:22459705
  reported transient oocyst suppression and relapse after stopping therapy, not a
  standard durable treatment.
- Species-specific differences beyond C. hominis and C. parvum are deferred; the
  current entry captures the shared core intestinal and severe-immunodeficiency
  biliary mechanisms.

## Cached-source completeness pass

After review, the eight PubMed references already cached for the pull request
were re-read locally to check for missed mechanisms, phenotypes, host contexts,
diagnostics, treatments, and bounded exclusions. No external deep-research
provider was used for this pass.

- The entry stays deliberately lumped at the genus-level MONDO term and records
  C. hominis and C. parvum as the predominant human etiologic species rather
  than splitting by species.
- The life-cycle and transmission sections capture environmentally resistant
  oocysts, excystation in the mammalian small intestine, intracellular
  epithelial infection, person-to-person spread, contaminated water and food,
  and person-to-person or household exposure.
- The pathophysiology graph separates ingestion/excystation, intracellular
  epithelial infection, epithelial injury, lamina-propria inflammation and
  cytokine signaling, barrier dysfunction with fluid-electrolyte imbalance,
  excess fluid loss, nutrient malabsorption, and severe-immunodeficiency
  biliary persistence.
- Prolonged diarrhea, malnutrition, and growth delay are causally downstream of
  excess intestinal fluid loss or nutrient malabsorption; dehydration is
  downstream of fluid loss.
- Severe host susceptibility is represented from HIV/AIDS, CD40LG deficiency,
  IL21R deficiency, and MBL2 susceptibility evidence rather than as a generic
  immunodeficiency bucket.
- Nitazoxanide is kept as a small-molecule antiparasitic treatment with trial
  support and response-context caveats; antiretroviral therapy targets the
  HIV/AIDS host defect; supportive fluid/electrolyte care targets the
  dehydration branch.
- Diagnostics include stool microscopy, stool antigen detection, and
  nucleic-acid amplification, with the PCR row carrying the precise NCIT
  nucleic-acid amplification term.

## Deferred or bounded items

- Transplant and oncology host settings were not modeled because they are not
  supported by the cached pull-request source set at the same specificity as
  the HIV/AIDS, IL21R, CD40LG, and MBL2 rows.
- Calf or ruminant exposure was not forced into `agent_life_cycle.hosts`: the
  cached broad review says many non-human species occur in mammals and that
  C. parvum was described from mice and other mammals, but it also emphasizes
  that most human infection is now due to C. hominis or person-to-person
  C. parvum rather than classic zoonosis.
- High-income-country outbreaks such as Milwaukee were left out of
  `prevalence:` because the cached source uses them as waterborne-outbreak
  examples, not as stable incidence or prevalence estimates.
- Post-infectious sequelae such as reactive arthritis or persistent functional
  gastrointestinal symptoms were not modeled because the cached sources used
  here support acute/prolonged diarrhea, pediatric malnutrition and growth
  effects, and biliary disease in severe immune deficiency, but not a
  snippet-verified post-infectious mechanism.
