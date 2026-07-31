# Assessment of the OpenScientist tick-microorganism report

## Overall assessment

**Verdict on the broad mechanism: weakly supported / unresolved.**

No direct experiment shows that a known co-transmitted pathogen is the primary
alpha-gal sensitizer, and the intrinsic tick route is more parsimonious. That
makes deprecation reasonable. The report nevertheless claims a class-wide
refutation using experiments that never removed or comprehensively measured
tick-associated microorganisms.

The report itself identifies the decisive caveat: laboratory ticks contain
obligate endosymbionts, and no endosymbiont-depletion or microorganism-free
reconstitution experiment has been performed. That is not a minor caveat to a
`REFUTED` verdict; it defines the untested edge.

## Useful evidence against specific versions

### The selected human pathogen panel was negative

[PMID:35382677](https://pubmed.ncbi.nlm.nih.gov/35382677/) found a strong
association between tick-bite history and alpha-gal IgE but no apparent role
for the examined Borrelia, Anaplasma, tick-borne encephalitis, and related
infection histories. This weighs against those named pathogens in that Polish
cohort.

It does not measure the microorganism present at the sensitizing bite,
endosymbionts, or the whole tick microbiome. It therefore cannot refute the
broad “another organism present in the tick” model.

### Endogenous synthesis is a stronger direct alternative

[PMID:30242261](https://pubmed.ncbi.nlm.nih.gov/30242261/) establishes
endogenous alpha-gal biosynthetic capacity in *I. scapularis*. That eliminates
the need to invoke a microbe as the only possible source. It does not show that
a microbial source or adjuvant never contributes, and the same study finds
Anaplasma-dependent modulation of tick alpha-gal biology.

### There is no direct positive sensitization result

The report correctly finds no experiment in which a co-transmitted organism is
shown to be the primary sensitizer. This supports `WEAKLY_SUPPORTED_UNRESOLVED`
and low curation priority. Absence of positive evidence is not equivalent to a
controlled refutation of every microbial candidate.

## Claims that require correction

### The salivary extract was not demonstrated pathogen-free

[PMID:34034363](https://pubmed.ncbi.nlm.nih.gov/34034363/) does not report
pathogen screening or an axenic preparation and explicitly uses partially
blood-fed salivary-gland extract. It shows that a live transmitted infection
is unnecessary, but the material could still contain microbial antigens or
endosymbiont products.

[PMID:35493735](https://pubmed.ncbi.nlm.nih.gov/35493735/) independently finds
Francisellaceae dominating laboratory-raised *Amblyomma americanum* tissues and
developmental stages. Calling the extract “pathogen-free” does not address the
seed's broader commensal/endosymbiont scope.

### Salivary alpha-gal detection does not identify a nonmicrobial source

The mass-spectrometry material in
[PMID:39053323](https://pubmed.ncbi.nlm.nih.gov/39053323/) came from ticks fed
on sheep, and the authors call the glycolipid origin inconclusive. Basophil
activation in cells armed with AGS plasma is an effector result, not a test of
which source originally produced sensitization. It cannot “eliminate the need”
to consider microbial sources.

### Bite-lesion histology does not observe class switching

[PMID:29273488](https://pubmed.ncbi.nlm.nih.gov/29273488/) reports more
basophils, eosinophils, type-2 cytokine-producing T cells, and alpha-gal IgE
after repeated bites. These are valuable compatible observations. The study
does not observe B-cell class switching, identify the presenting pathway, assay
microbes, or show that no microbial trigger is needed.

### Helminth epidemiology is not a tick-source counterfactual

Helminth-associated sensitization without recognized meat allergy highlights
the distinction between sensitization and clinical disease. Differences in
route, antigen form, ascertainment, and immune context prevent those cohorts
from identifying the source that matters during a tick bite. Calling this
“devastating” evidence against the microorganism model is rhetorical rather
than experimental.

## Provenance and curation implication

The report claims 51 papers but exposes 24 citations and no screening log.
Assessment should rest on its committed sources.

Retain the hypothesis as deprecated because it lacks direct support and has a
stronger competing model, but describe the verdict as unresolved rather than
experimentally refuted. A microorganism-free alpha-gal-plus-salivary-adjuvant
reconstitution, or a carefully controlled endosymbiont/microbiome perturbation,
would discriminate the models.

The existing disease YAML already calls the mouse extract pathogen-free and
uses limited serology as class-wide refutation. Those overstatements should be
revised in a separate disease-curation change, not silently promoted or repaired
inside this assessment PR.
