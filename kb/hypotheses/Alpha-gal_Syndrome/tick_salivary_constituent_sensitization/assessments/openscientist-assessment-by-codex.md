# Assessment of the OpenScientist tick-intrinsic salivary report

## Overall assessment

**Verdict on the integrated mechanism: partially supported.**

The report identifies the strongest current model, but it closes the
antigen-source question more tightly than its experiments permit. Ticks have
functional alpha-gal biosynthetic machinery; alpha-gal-bearing material is
present in tick saliva; and tick salivary-gland extract or tick bites can
sensitize alpha-gal-deficient mice. Those are substantial and mutually
compatible observations.

They are not a single source-tracing experiment. Several of the cited studies
used blood-fed ticks, and none follows a specifically tick-synthesized molecule
from biosynthesis through a natural human bite to IgE class switching.
`PARTIALLY_SUPPORTED` is therefore the right verdict, while the report's
recommended upgrade to fully supported is premature.

## Evidence that should be retained

### Ticks can synthesize alpha-gal

[PMID:30242261](https://pubmed.ncbi.nlm.nih.gov/30242261/) combines
heterologous expression with tick RNAi and supports endogenous alpha-gal
production in *Ixodes scapularis*. It rules out the old assumption that all
tick alpha-gal must be acquired. The paper itself is more careful than the
report: it calls for further work to determine whether endogenous,
host-acquired, or both sources have the major role in AGS.

### Tick saliva contains functionally recognizable alpha-gal material

Proteomic and mass-spectrometric studies support alpha-gal-bearing proteins and
glycolipids in saliva. The basophil assays in
[PMID:39053323](https://pubmed.ncbi.nlm.nih.gov/39053323/) demonstrate
recognition by alpha-gal-IgE-armed effector cells. That is an effector assay,
not a sensitization experiment, but antigen presence is a real component of
the proposed chain.

### Salivary extract and bites can sensitize AGKO mice

[PMID:34034363](https://pubmed.ncbi.nlm.nih.gov/34034363/) establishes that
repeated intradermal salivary-gland extract produces alpha-gal-specific IgE and
meat-challenge reactions in AGKO mice. The species-comparison bite experiment
in [PMID:38390396](https://pubmed.ncbi.nlm.nih.gov/38390396/) further supports
variation in the sensitizing capacity of tick species and a relevant salivary
context.

## Where the source attribution fails

### The mouse extract was partially blood-fed

The report says the mouse study excluded blood-meal remnants and pathogens.
The primary paper explicitly calls the inoculum “partially blood fed TSGE.”
It reports no axenic preparation or pathogen/endosymbiont screen, and its
discussion lists endogenous, microbiome-derived, and feeding-induced alpha-gal
as unresolved possibilities. The experiment establishes extract sufficiency,
not source identity.

### The glycolipid paper calls origin inconclusive

[PMID:39053323](https://pubmed.ncbi.nlm.nih.gov/39053323/) collected saliva
from *Amblyomma americanum* partially fed on sheep. Its discussion states that
direct derivation from host blood versus tick synthesis from host precursors
is inconclusive and even notes that the glycolipids may be host-blood sourced.
The report's use of this result as direct evidence of a tick-endogenous
glycolipid source is not supported by the paper.

### Vegetation-collected adults are not a lifecycle-naive control

[PMID:38741222](https://pubmed.ncbi.nlm.nih.gov/38741222/) compared adult
*Hyalomma lusitanicum* collected from vegetation with adult males partially
fed on deer. Similar antibody reactivity supports independence from feeding in
the current adult stage and is compatible with endogenous production. It does
not show that the adults “had never taken a blood meal,” chemically trace the
glycan, or make a residual contribution impossible.

## Additional calibration

The tsetse-fly report
([PMID:40485140](https://pubmed.ncbi.nlm.nih.gov/40485140/)) is an intriguing
case-series lead. It found trace whole-body alpha-gal, none in the sampled
midgut protein extract, and galactosyltransferase transcripts; its authors call
endogenous production putative. It does not yet generalize the mechanism
beyond ticks.

The immune-population statement is also misattributed.
[PMID:41317280](https://pubmed.ncbi.nlm.nih.gov/41317280/) is a review; the
corresponding primary single-cell and cytometry study is
[PMID:41098729](https://pubmed.ncbi.nlm.nih.gov/41098729/). Those human data
identify altered circulating populations but do not establish an iNKT/CD1d
route to alpha-gal-specific class switching.

## Provenance and curation implication

The report says it reviewed more than 80 primary papers, while the committed
frontmatter exposes 23 citations and no screening log. The larger retrieval set
cannot be audited from the artifact.

Keep the mechanism only partially supported unless the status is narrowly
defined as “ticks possess endogenous alpha-gal biosynthetic capacity.” Preserve
explicit gaps for source attribution in natural bites, salivary adjuvants,
antigen presentation, and IgE class switching. The current disease YAML already
uses the report's stronger source-closure language; that should be corrected in
a separate evidence-curation change rather than silently altered by this
assessment.
