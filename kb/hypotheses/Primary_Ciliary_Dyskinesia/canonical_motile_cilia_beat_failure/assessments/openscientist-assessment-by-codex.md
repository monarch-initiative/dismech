# Assessment of the OpenScientist canonical motile-cilia report

## Overall assessment

**Verdict on the mechanism: supported.**

The report is right about the core biology: PCD-associated motile-cilia
dysfunction causes profound mucociliary-clearance impairment, which is central
to recurrent infection and chronic airway disease. It also makes a useful
curation distinction between axonemal dysfunction and reduced
multiciliogenesis. Those are different upstream mechanisms that converge on the
same clearance phenotype.

The report is less reliable when it turns plausible extensions into established
branches of the disease mechanism. The NOS, macrophage-polarization, and
inflammation-independent remodeling findings are valuable research leads, but
their current evidence does not establish independent causal routes in human
PCD.

## Findings that should be retained

The broad genetic, ultrastructural, beat-pattern, and functional-clearance
literature supports the canonical mechanism. The direct clearance study
[PMID:38076675](https://pubmed.ncbi.nlm.nih.gov/38076675/) spans 69 participants
and 26 genotypes, providing particularly useful evidence that profound
clearance impairment is not confined to one ultrastructural class.

CCNO- and MCIDAS-related disease should be represented as reduced
multiciliogenesis rather than an axonemal beat defect. Patient-cell studies
[PMID:24747639](https://pubmed.ncbi.nlm.nih.gov/24747639/) and
[PMID:25048963](https://pubmed.ncbi.nlm.nih.gov/25048963/) support that distinct
upstream route.

## Material corrections and qualifications

### Clearance is not literally universal

The report repeatedly changes “absent in most PCD patients” into “universally
absent.” The source
[PMID:38076675](https://pubmed.ncbi.nlm.nih.gov/38076675/) records residual
clearance in one CCDC103 participant. The strong conclusion is that clearance
is absent in most measured patients across many genotypes, not every patient.

### Rescue and treatment do not validate the entire chain

DNAI1 mRNA restored axonemal incorporation and beat frequency in mouse airway
culture [PMID:40963409](https://pubmed.ncbi.nlm.nih.gov/40963409/). That is
direct evidence for a proximal gene-to-ciliary-function link, but the study did
not measure clearance, infection, inflammation, lung disease, or a human
clinical outcome.

BESTCILIA showed fewer exacerbations with azithromycin
[PMID:32380069](https://pubmed.ncbi.nlm.nih.gov/32380069/). Because the trial
does not isolate antimicrobial from immunomodulatory action, it is clinical
efficacy evidence rather than a mechanistic validation of the report’s complete
infection–inflammation arm.

### Proposed parallel branches remain leads

Low bronchial and modeled alveolar NO
[PMID:23290188](https://pubmed.ncbi.nlm.nih.gov/23290188/) and deficient NOS2
induction in cultured PCD cells
[PMID:24189859](https://pubmed.ncbi.nlm.nih.gov/24189859/) support abnormal NO
biology. They do not yet establish a shared, mutation-intrinsic,
clearance-independent immune defect.

IFT88 deletion caused airway remodeling in mice without apparent inflammation
or mucus-clearance failure
[PMID:24213915](https://pubmed.ncbi.nlm.nih.gov/24213915/). IFT88 affects
nonmotile cilia and epithelial differentiation as well as motile cilia, so this
is not direct evidence for an independent remodeling branch in human axonemal
PCD.

PCD sputum induced an M2-like phenotype in healthy monocyte-derived macrophages
ex vivo [PMID:41582098](https://pubmed.ncbi.nlm.nih.gov/41582098/). That
interesting result is not enough to define a stable in-vivo PCD endotype or to
replace the established neutrophil-dominant description.

### Factual and ontology errors

The RSPH1 comparison is FEV1 73.0 versus 61.8 percent predicted with **P=0.043**,
not P=0.0 [PMID:24568568](https://pubmed.ncbi.nlm.nih.gov/24568568/).

The ontology leads also need correction before reuse. CL:0000710 is
neurecto-epithelial cell, not multiciliated cell; CL:0000235 is generic
macrophage, not M2 macrophage. GO:0060271 denotes cilium assembly rather than
multiciliated-cell differentiation. CL:0005012 (multiciliated epithelial cell)
is a suitable replacement for the intended generic multiciliated-cell concept.

## Provenance and curation implication

The citation manifest contains 50 unique PMIDs, not a reproducible record of
the asserted 135-paper corpus. The larger number should be treated as
unverified provenance rather than evidence weight.

Keep the canonical mechanism, but describe clearance as absent in *most*
measured patients. Add reduced multiciliogenesis as a parallel upstream route.
Do not promote the NOS, macrophage, or IFT88 branches as established human PCD
mechanisms without additional primary evidence. Citations in this assessment
are review context only and require the normal disease-YAML evidence workflow
before curation.
