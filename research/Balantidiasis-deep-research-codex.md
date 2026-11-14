# Balantidiasis: cached-source completeness pass

This is a local literature sweep produced from the PubMed references already cached for the pull request. No external deep-research provider was used.

## Source set

| Reference | Role in this pass |
| --- | --- |
| PMID:18854484 | Full-text *Clinical Microbiology Reviews* synthesis. Used for the direct cyst-trophozoite life cycle, the environmental resistance of cysts, fecally contaminated water as a transmission vehicle, cecal and colonic trophozoite habitat, the asymptomatic/chronic/fulminant clinical spectrum, flask-shaped submucosal lesions, hyaluronidase as a proposed ulceration factor, abdominal pain in chronic trophozoite invasion, stool wet-mount microscopy, and tetracycline/metronidazole therapy. |
| PMID:35146143 | Full-text review of *Balantioides coli* cyst detection and environmental viability. Used for the current *Balantioides* naming, direct trophozoite/cyst life cycle, fecal-oral food/water transmission, infective cyst framing, and severe colitis. |
| PMID:34339668 | Human systematic review and meta-analysis through 2020. Used for pig-proximity association, the 997-person case-count literature summary, predominant dysentery in analyzed human infections, and the count of 27 extraintestinal infections left out of the conserved intestinal pathograph. |
| PMID:33183780 | 2021 *Research in Veterinary Science* review. Used for infectious-agent identity, the main pig reservoir, pig-contact and sanitation risk factors, the asymptomatic/chronic/acute progression framing, and iodoquinol/nitroimidazole treatment. |
| PMID:31688855 | Human fatal colonic balantidiasis case report and review. Used for colonoscopy/fresh-sample/biopsy diagnosis and rare intestinal perforation. |
| PMID:35734242 | Contemporary human stool-microscopy case report. Used for stool wet-mount diagnosis, tenesmus, and a metronidazole-treated human case. |
| PMID:1190365 | Human metronidazole treatment series. Used for primary evidence of metronidazole-associated parasitologic clearance in 20 human balantidiasis cases. |

## Completeness cross-check

- The prevalence block now keeps PMID:34339668 as a literature case-count record and no longer treats the heterogeneous 3.98% in the systematic review as a population prevalence.
- The `progression:` block records asymptomatic carriage, chronic intermittent diarrhea, and acute dysenteric disease from the cached 2021 review.
- The pathophysiology graph separates intestinal trophozoite colonization, colonic mucosal invasion, and hyaluronidase-associated colonic ulceration.
- Diarrhea, bloody diarrhea, colitis, abdominal pain, tenesmus, and intestinal perforation are all causally connected to trophozoite invasion or ulceration.
- Bloody diarrhea now carries the systematic-review finding that dysentery was the predominant symptom in the analyzed clinical and epidemiologic human literature.
- Abdominal pain now has review-level support from the chronic-presentation description in PMID:18854484 in addition to the stool-confirmed case report.
- The history record now links PR #17781 and lists only sections the entry actually carries.

## Deferred or bounded items

- Extraintestinal balantidiasis remains out of the structured graph because the systematic review found only 27 extraintestinal infections among a heterogeneous literature pool, and the conserved Balantidiasis pathograph in this entry is intestinal.
- Other proposed reservoirs, including camels, cattle, donkeys, sheep, and goats, remain out of the host list because PMID:33183780 describes pigs as the main reservoir.
- Secnidazole remains unmodeled as a separate treatment row. The current entry covers the major tetracycline, metronidazole, and iodoquinol regimens, while the cached 2021 review lists secnidazole only as a member of the broader 5-nitroimidazole treatment class.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.
