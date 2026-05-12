# Chronic Intestinal Pseudoobstruction Deep Research Fallback

## Provider Attempts

No deep-research provider was invoked for this root-level entry. The
existing subtype dismech entry (`FLNA_Intestinal_Pseudoobstruction`)
has its own `-deep-research-falcon.md` artifact from prior curation;
this root-level record was curated **directly from the verified
literature already cached in `references_cache/`** for the FLNA-CIPO
subtype, plus the foundational `DOI:10.3389/fped.2022.837462`
pediatric-CIPO review, plus ORPHA-grounded subtype identifiers for
the X-linked and mitochondrial forms.

## Integrated Literature Synthesis

Chronic intestinal pseudoobstruction (CIPO) is a rare, severe disorder
of gastrointestinal motility in which patients experience episodes that
mimic mechanical bowel obstruction in the absence of any physical
luminal blockage. The pediatric review
`DOI:10.3389/fped.2022.837462` ("Pediatric Intestinal Pseudo-Obstruction:
Progress and Challenges") frames CIPO as "the most severe form of
gastrointestinal dysmotility with significant morbidity and mortality."
That review also distinguishes Pediatric Intestinal Pseudo-Obstruction
(PIPO) as biologically and clinically distinct from adult CIPO.

**Mechanistic heterogeneity.** Primary CIPO partitions along three
mechanistic axes that this root entry models as separate atomic
pathophysiology nodes converging on a shared `Intestinal Dysmotility`
endpoint:

- **Neuropathic** (enteric nervous system defects). The flagship
  example is X-linked FLNA loss-of-function (PMID:17357080,
  PMID:18854860), curated in the existing
  `FLNA_Intestinal_Pseudoobstruction` dismech entry. The truncated
  filamin A protein fails to support proper enteric neuron
  development. Other neuropathic mechanisms include enteric
  ganglionitis and acquired enteric neuropathies.
- **Myopathic** (visceral myopathies). Intrinsic smooth-muscle defects
  produce poorly contractile or acontractile intestinal smooth muscle.
  No dedicated dismech entry yet for the visceral-myopathy gene set
  (e.g., ACTG2, MYLK, MYH11, LMOD1) — scoped as follow-up curation.
- **Mitochondrial / MNGIE.** Mitochondrial DNA depletion / instability,
  classically due to biallelic TYMP (thymidine phosphorylase)
  loss-of-function, causes mitochondrial neurogastrointestinal
  encephalomyopathy. MONDO:0011283 (mitochondrial DNA depletion
  syndrome 1) is the canonical MONDO grounding; this root entry lists
  TYMP under `genetic[]` so that a future dedicated MNGIE dismech
  entry has a starting point.

**Clinical syndrome.** Six core phenotypes are captured (Intestinal
pseudo-obstruction `HP:0004389`, Abdominal distention `HP:0003270`,
Vomiting `HP:0002013`, Constipation `HP:0002019`, Feeding difficulties
`HP:0011968`, Failure to thrive `HP:0001508`). Frequency tags were
deliberately omitted from this root entry per the dismech
frequency-evidence SOP — the cited literature supports the existence
of these features in CIPO but does not provide subtype-pooled
quantitative frequencies appropriate for the umbrella entry.

**Management.** The supportive-care ladder is captured in
`treatments[]`: parenteral nutrition (`NCIT:C29484`, the mainstay
for patients whose motility cannot sustain enteral intake), enteral
nutritional support (`MAXO:0000088`, preferred when tolerated),
surgical management (`MAXO:0000004`), intestinal transplantation
(`MAXO:0010039`, reserved for irreversible intestinal failure with
TPN complications), and genetic counseling (`MAXO:0000079`) for
heritable subtypes.

## Out of scope for the root entry

- Subtype-specific molecular detail for X-linked FLNA-CIPO — already
  curated in `FLNA_Intestinal_Pseudoobstruction`.
- MNGIE / mitochondrial DNA depletion mechanisms beyond the TYMP
  genetic link — scoped as a dedicated dismech entry.
- Visceral-myopathy gene-level entries (ACTG2, MYLK, MYH11, LMOD1,
  etc.) — scoped as follow-up.
- Secondary CIPO (postsurgical, post-infectious, paraneoplastic,
  systemic-sclerosis-associated, drug-induced) — explicitly excluded
  from the primary-CIPO categories enumerated here.
