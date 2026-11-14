# Amoebiasis due to *Entamoeba histolytica*: cached-source completeness pass

This is a local literature sweep produced from the full-text PubMed references already cached for the pull request. No external deep-research provider was used.

## Source set

| Reference | Role in this pass |
| --- | --- |
| PMID:41809248 | Main 2025 clinical review covering epidemiology, risk modifiers, progression from asymptomatic carriage to invasive colitis and liver abscess, severe fulminant colitis, diagnostics, serology, tissue/luminal therapy, and selected liver-abscess drainage. |
| PMID:36519347 | Virulence review supporting the cyst/trophozoite life cycle, Gal/GalNAc adhesion, cysteine-protease inflammatory invasion, asymptomatic versus invasive infection, and bloody dysentery manifestations. |
| PMID:30046644 | Burden, diagnostic, and treatment review supporting fecal-oral and fecal-sexual cyst transmission, excystation and encystation, and diagnostic distinctions between *E. histolytica* and non-pathogenic *Entamoeba* species. |

## Completeness cross-check

- Pathophysiology now distinguishes asymptomatic luminal cyst carriage, epithelial adhesion and cytolysis, cysteine-protease inflammatory invasion, amoebic colitis, portal spread to liver, amoebic liver abscess formation, and fulminant amoebic colitis.
- All phenotype leaves in the entry are connected to upstream pathophysiology nodes: colitis and bloody diarrhea from amoebic colitis; liver abscess, right upper quadrant abdominal pain, fever, weight loss, and hepatomegaly from amoebic liver abscess formation; toxic megacolon and intestinal perforation from fulminant colitis.
- The `progression:` block records the infectious-disease ladder from asymptomatic luminal carriage to invasive amoebic colitis, extraintestinal liver abscess, and the rare fulminant necrotising-colitis branch.
- Major clinical modifiers from the cached review are represented by corticosteroid or immunosuppressive therapy as an exacerbating factor for fulminant amoebic colitis.
- Diagnosis includes stool or liver-aspirate PCR, Gal/GalNAc lectin antigen ELISA, and IgG antibody serology.
- Treatment separates nitroimidazole tissue amoebicides from luminal amoebicides so each targets the mechanism it acts on.

## Deferred or bounded items

- Amoeboma is documented as rare in PMID:41809248 but was left out because the entry already captures the common colitis and liver-abscess branches plus the severe fulminant-colitis branch.
- Stool microscopy is documented in PMID:41809248 but was left out because the entry already records species-discriminating PCR and antigen testing, and microscopy cannot morphologically distinguish *E. histolytica* cysts from cysts of non-pathogenic species.
- Percutaneous drainage of amoebic liver abscess is documented for selected high-risk abscesses or lack of early medical response, but the pharmacologic tissue/luminal amoebicide split was the treatment gap most likely to change the pathograph.
