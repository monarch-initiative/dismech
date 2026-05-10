# Hereditary Angioedema Deep Research Fallback

## Provider Attempts

- `falcon`: `timeout --foreground 120s just research-disorder falcon Hereditary_Angioedema` produced no usable content and was terminated with signal 15.
- `openai`: `timeout --foreground 120s just research-disorder openai Hereditary_Angioedema` produced no usable content and was terminated with signal 15.

Because the preferred deep-research providers did not return usable content in
bounded attempts, this fallback records the literature scope used for curation.
All YAML evidence was taken from generated Orphanet and PubMed reference caches,
not from hand-created reference text.

## Structured Source Scope

Hereditary angioedema corresponds to MONDO:0019623 and Orphanet ORPHA:91378.
ORPHA:91378 is an Orphanet clinical-group record and was not emitted by the
current structured Orphanet cache builder, which caches generated leaf disease
and subtype records. The curation therefore used generated caches for
ORPHA:528623 hereditary angioedema with C1Inh deficiency, ORPHA:528647
hereditary angioedema with normal C1Inh, and subtype records ORPHA:100050,
ORPHA:100051, ORPHA:100054, ORPHA:537072, and ORPHA:599418.

ORPHA:528647 currently lists obsolete MONDO:0033947 as its cross-reference.
Local MONDO resolves the active replacement as MONDO:0100567 hereditary
angioedema with normal C1Inh, and the YAML uses that active term.

## Literature Scope

Clinical definition, inheritance, genetic heterogeneity, diagnostic testing, and
pathophysiology were anchored with contemporary review, guideline, consensus,
and prevalence papers: PMID:36609679, PMID:35442579, PMID:35006617,
PMID:40053270, and PMID:39827848. These sources support autosomal dominant
classic HAE, SERPING1-related type 1 and type 2 disease, normal-C1-INH genetic
subdivision, C1-INH/C4 laboratory testing, excess bradykinin production,
increased vascular permeability, and worldwide rarity.

Treatment evidence was anchored to human clinical trials or extensions:
PMID:28328347 for subcutaneous C1 inhibitor prophylaxis, PMID:20818888 for
icatibant acute attack therapy, PMID:21481442 for ecallantide acute attack
therapy, PMID:40886933 for oral sebetralstat attack therapy, PMID:30480729 for
lanadelumab prophylaxis, PMID:33866032 for berotralstat prophylaxis, and
PMID:41767175 for donidalorsen long-term prophylaxis.

## Curation Decisions

- Used MONDO:0019623 as the disease term and modeled the major clinical and
  etiologic branches as subtypes.
- Included active subtype terms for C1-INH deficiency, type 1, type 2,
  normal-C1-INH HAE, F12-related HAE, PLG-related HAE, and the non-F12/non-PLG
  normal-C1-INH subtype group.
- Recorded ORPHA frequent and very frequent phenotype rows from ORPHA:528623
  and ORPHA:528647, but did not retain contradictory urticaria rows from the
  HAE type 1 subtype table because the disease-level records define HAE attacks
  as occurring without urticaria and mark urticaria as excluded.
- Recorded decreased C4 and decreased C1 inhibitor concentration as
  C1-INH-deficiency-specific findings because ORPHA:528647 excludes decreased
  C4 in normal-C1-INH HAE.
- Did not bind a C1 inhibitor therapeutic agent in the treatment section: the
  available local NCIT C1 inhibitor term validates as a protein/gene product
  but not as a pharmacologic-substance descendant for the `therapeutic_agent`
  slot. The same NCIT term is retained in the pathophysiology gene-product
  descriptor, where it validates.
