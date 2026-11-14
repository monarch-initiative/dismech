# Dioctophymiasis Deep Research Note

## Scope and source mode

No external deep-research provider was used for this follow-up pass. The initial
curation already had a source list in
`research/Dioctophymiasis-literature-sweep-codex.md`; this local Codex review
re-read the cached references under `references_cache/` to check for missed
mechanistic nodes, phenotypes, prevalence evidence, diagnosis records,
treatments, and ontology bindings.

## Cached sources re-read

- PMID:30963996 — the global 2019 review of 37 human cases.
- PMID:40867017 — the 2025 molecularly confirmed Korean gastric-wall larva.
- PMID:28299768 — the Iranian renal case detected by ultrasound and computed
  tomography.
- PMID:24095916 — the molecularly confirmed subcutaneous larval infection.
- PMID:26952087 — a renal infection co-occurring with renal-cell carcinoma.
- PMID:21158627 — a fatal bilateral renal-infection case.

## Mechanistic and clinical findings

The cached review supports keeping the pathograph split between ingested L3
larvae, the mammalian gastric-wall to hepatic migration route, adult renal
residence with parenchymal destruction, and ectopic larval residence. The
life-cycle details in PMID:40867017 describe the conserved mammalian cycle, so
animal-host background is indirect support for the human migration node rather
than direct human clinical evidence.

PMID:30963996 remains the best compact source for human frequencies and the
case count. It reviewed 32 papers with 37 human cases through October 2018,
found that 31 of 37 involved kidneys, and reported loin pain and hematuria in
22 of 37 cases each. The same clinical section lists fever, anemia, abdominal
pain, weight loss, frequent urination, urgent urination, urinary retention,
pyuria, and proteinuria as less frequent renal-case manifestations.

The ectopic-tissue evidence supports replacing a generic tissue binding with
the named sites in the cached papers: liver, abdominal cavity, retroperitoneal
space, subcutaneous tissue, and the stomach wall. The South Korean case adds a
gastric-wall mass presentation, while PMID:24095916 supports the subcutaneous
nodule presentation.

## Diagnosis and treatment findings

Morphologic identification of eggs or worms in urine or histopathologic tissue
sections remains the core diagnostic method for renal disease and ectopic
nodules. PCR followed by ribosomal or mitochondrial DNA sequencing is useful for
unusual ectopic larvae, especially where morphology overlaps Gnathostoma or
Anisakis. Renal ultrasound and computed tomography detect mass-like renal
infection but still feed into morphologic confirmation when a worm or tissue is
recovered.

Surgical or endoscopic removal remains the only structured treatment in this
entry. The human-case review notes isolated ivermectin and albendazole
successes but also states that anthelmintic treatment had not been established
as the proper course of action, so those drugs are intentionally left out of
the treatment block until stronger evidence is available.

## Ontology checks

Local OAK lookups resolved the new exact bindings used in the review patch:

- `HP:0100515` Pollakisuria for urinary frequency.
- `UBERON:0001167` wall of stomach.
- `UBERON:0003684` abdominal cavity.
- `UBERON:0003693` retroperitoneal space.
- `UBERON:0002072` hypodermis, represented with `preferred_term:
  subcutaneous tissue`.
- `NCIT:C16853` Microscopy.
- `NCIT:C153598` DNA Sequencing.
- `NCIT:C16502` Diagnostic Imaging Testing.
- `NCIT:C15329` Surgical Procedure.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.
