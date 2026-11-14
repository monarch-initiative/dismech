---
disease_name: Acanthocephaliasis
mondo_id: MONDO:0000295
note_type: cached-source completeness pass
source_set: cached PR references
---

# Acanthocephaliasis cached-source completeness pass

This is a local completeness pass produced from the PubMed references already
cached for the pull request. No external deep-research provider was used.

## Source set

| Reference | Role in this pass |
| --- | --- |
| PMID:34076470 | Open full-text review of human acanthocephaliasis. Used for the dominant human agents, arthropod and paratenic-host transmission, the multihost egg-to-cystacanth-to-adult cycle, the 8-12 week prepatent maturation interval, most diagnosed cases having no overt symptoms, the mild-to-severe gastrointestinal symptom spectrum, peripheral eosinophilia as an occasional finding, attachment-site ulceration and leukocyte infiltration, adult-worm and stool-egg diagnosis, pyrantel pamoate treatment of mild cases, and endoscopic or surgical removal in invasive cases. |
| PMID:39979033 | Recent pediatric Moniliformis moniliformis case report. Used for direct cockroach ingestion preceding adult-worm passage, absence of systemic symptoms in that child, M. moniliformis background life-cycle context, and clearance after three 11 mg/kg pyrantel pamoate doses separated by two weeks. |
| PMID:17570979 | Open full-text Iranian M. moniliformis case report. Used for the hooked protrusible proboscis and its role in intestinal mucosal penetration, reattachment, inflammation, ulceration, and hemorrhage. |

## Completeness cross-check

- The Acanthocephala phylum binding keeps the entry aligned with
  MONDO:0000295 while the description names the dominant human agents:
  Macracanthorhynchus hirudinaceus, Macracanthorhynchus ingens, and
  Moniliformis moniliformis.
- Bolbosoma and Corynosoma remain deliberately lumped because the published
  fish-borne marine cases share the same adult-worm attachment mechanism and
  are a sparse case-report stratum rather than a separate MONDO child. Their
  paratenic-host route and enrichment for severe invasive symptoms are recorded
  in the transmission and phenotype evidence.
- The life cycle now separates shed acanthor-containing eggs, arthropod
  acanthor-to-cystacanth maturation, prepatent attachment over about 8-12
  weeks, and patent adult-worm infection.
- Adult-worm passage is called out as the usual diagnostic trigger, and the
  review's statement that most diagnosed infections have no overt symptoms is
  captured in that phenotype row.
- Nausea, anorexia, abdominal distension, ileus, and increased eosinophil count
  were all rechecked against the 2021 review and added as separate phenotype
  rows.
- The attachment-site histopathology now cites the review sentence supporting
  both mucosal ulceration and neutrophil, eosinophil, or lymphocyte
  infiltration.
- Pyrantel pamoate now has a structured NCIT pharmacotherapy action and a
  ChEBI agent binding to `CHEBI:8655`; invasive endoscopic or surgical removal
  now carries `NCIT:C15329` Surgical Procedure.

## Deferred or bounded items

- Levamisole, niclosamide, mebendazole, ivermectin, thiabendazole, and
  piperazine citrate remain in prose because the 2021 review describes
  heterogeneous case-report successes rather than a standardized or repeated
  regimen.
- Individual host rows for raccoon, marine whales, pinnipeds, and marine fish
  remain out of the structured host list because the entry needs the conserved
  arthropod-to-incidental-human infection route, while genus-specific wildlife
  reservoirs would be incomplete without a species-resolved split.
- The Acanthocephalus and Pseudoacanthocephalus case strata remain in prose
  because their human source route is unknown or could not be reviewed in the
  cached 2021 article.
