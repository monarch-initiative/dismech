# Anisakiasis literature sweep

This curation sweep checked recent and classic Anisakiasis reviews and open
full-text case series before creating `kb/disorders/Anisakiasis.yaml`.

## Sources used

- **PMID:20804423** — CID review of anisakidosis. Used for agent scope, raw or
  undercooked marine fish/squid acquisition, gastric mucosal invasion, allergic
  anisakidosis, endoscopic diagnosis and removal, anti-*A. simplex* IgE
  serology, and occasional surgical removal.
- **PMID:30058531** — open full-text retrospective analysis of confirmed Italian
  human anisakiasis cases. Used for the marine-mammal → crustacean → fish/squid
  life cycle, humans as accidental hosts, raw-anchovy exposure in the Italian
  cases, worldwide and Japanese incidence, gastric/intestinal/ectopic site
  distribution, abdominal-pain frequency, eosinophilic granuloma histopathology,
  allergic-reaction details, surgery and albendazole treatment details, and the
  confirmed-case prevalence row.
- **PMID:24441579** — open full-text CT series of 20 gastric and 21 intestinal
  anisakiasis cases. Used for the larval wall-invasion mechanism,
  eosinophilic-granuloma pathophysiology, ascites, and characteristic CT
  findings.
- **PMID:10629469** — 20 patients with gastroscopically confirmed acute
  parasitism by *Anisakis simplex* among emergency patients with allergic
  reactions. Used for the gastro-allergic symptom spectrum, including
  bronchospasm and anaphylaxis.
- **PMID:31529811** — open full-text case report and review of gastro-allergic
  anisakiasis. Used for the two-mechanism framing of direct nematode injury plus
  immediate IgE-mediated hypersensitivity and for endoscopic extraction as the
  effective therapy.
- **PMID:40974456** — 2025 case report and review of small-bowel perforation.
  Used only for the rare complicated intestinal-perforation phenotype.

## Lump/split decision

`stubs/Anisakiasis.yaml` carries no MONDO descendants and lists `MONDO:0005656`
Ascaridida infectious disease and `MONDO:0002243` intestinal helminthiasis as
parents, so it was curated as a leaf infectious disorder. The entry deliberately
uses the named clinical syndrome rather than splitting gastric, intestinal,
ectopic, and allergic presentations into subtypes: the same exposure and
infective larval stage cause the organ-site presentations, while the
gastro-allergic form adds an IgE-mediated branch rather than a distinct
taxonomic agent.

The infectious-agent descriptor is bound to `NCBITaxon:6267` Anisakidae rather
than only `NCBITaxon:6269` *Anisakis simplex*. The CID review defines the human
syndrome as Anisakidae infection caused most commonly by *A. simplex* and
*Pseudoterranova decipiens*, and the Italian review notes rare *Contracaecum*
infections; a family-level binding keeps those agents inside the disease without
curating pathotype-like pseudo-subtypes.

## Exclusions

- **Gastrointestinal cancer association** was left out. PMID:31529811 mentions a
  proposed risk relationship through chronic inflammation and parasite
  secretions, but the statement is secondary and not central to the acute,
  dead-end larval infection modeled here.
- **Occupational sensitization** was not modeled as transmission. The entry is
  for active anisakid larval infection after seafood ingestion; allergy after
  fish-handling exposure can occur without a live larva penetrating the
  gastrointestinal mucosa.
- **Food-preparation prevention** was not modeled. Freezing and cooking fish are
  documented by PMID:20804423 and the Italian review, but the pathograph
  represents the disease state after viable-larva ingestion rather than public
  health or kitchen controls that prevent the exposure.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.
