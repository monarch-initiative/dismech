# 46,XX Testicular DSD Deep Research Fallback

## Provider Attempts

- 2026-05-08T15:00Z: `just research-disorder asta 46_XX_Testicular_DSD` failed:
  `ERROR - No research providers available. Please set API keys` (no
  `ASTA_API_KEY` configured in this environment).
- 2026-05-08T15:00Z: `just research-disorder openai 46_XX_Testicular_DSD` failed
  with the same provider-unavailable error (no `OPENAI_API_KEY`).
- 2026-05-08T15:00Z: `just research-disorder perplexity 46_XX_Testicular_DSD`
  failed with the same provider-unavailable error (no `PERPLEXITY_API_KEY`).
- 2026-05-08T15:00Z: `just research-disorder falcon 46_XX_Testicular_DSD`
  failed with the same provider-unavailable error (no provider keys at all,
  including Edison/Falcon).

`just research-providers` confirmed no providers are configured in this
worktree. No provider-generated research artifact was available to integrate.
Curation therefore proceeded from the PubMed-cached abstracts already
referenced in `kb/disorders/46_XX_Testicular_DSD.yaml`, without
hand-editing any `references_cache/*.md` files.

## Evidence Scope Used For Curation

- PMID:31336995 (Terribile et al. 2019, Medicina) — case report + systematic
  review of 46,XX testicular DSD. Used as the canonical clinical-presentation
  reference: SRY-positive vs SRY-negative classification, adult presentation
  with infertility, hypergonadotropic hypogonadism, gynecomastia, small
  testes, cryptorchidism (~15%) and anterior hypospadias (~10%), and the
  rationale for long-term testosterone replacement.
- PMID:36341017 (Kouvidi et al. 2022) — two new cases plus literature review
  cohort. Used for SRY-translocation epidemiology (84.4% SRY-positive, 98.5%
  Xp), absence of AZF regions, and quantitative phenotype frequencies in the
  cohort: small testes (90.2%), small penis (31.8%), gynecomastia (26.8%),
  poor hair distribution (15.4%). The "small penis (31.8%)" figure is the
  source for the new Micropenis (HP:0000054) phenotype entry.
- PMID:25077096 (Lee et al. 2014, Ann Pediatr Endocrinol Metab) — Korean boy
  with 46,XX testicular DSD caused by SOX9 duplication. Supports the
  SRY-negative SOX9 gain-of-function mechanism in which duplications
  upstream of SOX9 drive ectopic testis determination in 46,XX gonads.
- PMID:34050715 (Qian et al. 2021) — whole-genome sequencing of an
  SRY-negative 46,XX ovotesticular DSD case identifying a cryptic SOX9
  regulatory-element duplication. Reinforces the SOX9 enhancer-duplication
  mechanism and shows how cryptic non-coding variants can be missed by
  standard cytogenetics.
- PMID:36064700 (Wei et al. 2022) — SRY-negative 46,XX male with SOX3
  duplication and prostatic utricle. Supports SOX3 duplication as an
  alternative SRY-independent driver of testis determination, expanding the
  set of SRY-negative genetic etiologies beyond SOX9.
- PMID:29575617 (Tallapaka et al. 2018, Am J Med Genet A) — novel RSPO1
  mutation causing SRY-negative 46,XX testicular DSD with palmoplantar
  keratoderma. Defines the RSPO1-associated subtype and establishes
  palmoplantar hyperkeratosis as the pathognomonic extra-gonadal feature
  that clinically distinguishes RSPO1 cases from other SRY-negative
  etiologies.

## Curation Conclusions

46,XX testicular disorder of sex development is a sex-reversal phenotype in
which 46,XX gonads commit to the testis pathway despite the absence of a
typical Y chromosome. Two broad mechanistic classes account for nearly all
cases. In SRY-positive 46,XX testicular DSD (~85% of patients), aberrant
paternal-meiosis recombination translocates SRY onto the X chromosome (most
commonly Xp22), with rare autosomal landings; the translocated SRY drives
Sertoli-cell specification and the canonical SOX9-mediated testis cascade,
producing essentially complete masculinization at birth and an adult
presentation dominated by hypergonadotropic hypogonadism, azoospermia, and
infertility. In SRY-negative 46,XX testicular DSD, testis determination is
driven by genetic perturbations that bypass SRY: gain-of-function copy-number
gains around SOX9 (including cryptic enhancer duplications detectable only by
whole-genome sequencing), SOX3 duplications that act as ectopic SRY-like
inducers, and biallelic loss of RSPO1 that disrupts the WNT/RSPO1/CTNNB1
ovarian-determining program and permits default testis differentiation. The
RSPO1 subtype is uniquely identifiable by palmoplantar keratoderma — the
clinically distinguishing extra-gonadal feature.

Regardless of upstream genetic mechanism, the downstream gonadal pathology
converges on dysgenetic testes lacking germ-cell development. Loss of the
AZF regions on Yq and absence of normal seminiferous tubule architecture
result in azoospermia in essentially all affected individuals; testicular
sperm extraction is generally unsuccessful. Sertoli-cell and Leydig-cell
function is partially preserved in childhood (giving rise to externally
masculine genitalia and pubertal initiation), but post-pubertal Leydig-cell
insufficiency manifests as low testosterone with elevated LH/FSH —
hypergonadotropic hypogonadism — driving the adult clinical phenotype:
small testes (~90% of patients), small penis (~32%), gynecomastia (~27%),
sparse body hair (~15%), reduced bone mineral density, and infertility.
SRY-negative cases more commonly show ambiguous or undermasculinized
external genitalia at birth (hypospadias, cryptorchidism), reflecting
attenuated fetal androgen production, and may present in childhood rather
than adulthood.

Treatment is supportive and lifelong. Long-term testosterone replacement
(captured here as MAXO:0000058 pharmacotherapy with CHEBI:17347 testosterone
as the therapeutic agent) addresses hypogonadism, supports secondary
sexual characteristics, and protects bone health. Genetic counseling
addresses the rare familial recurrence risk (notably for RSPO1 biallelic
families and inherited SOX3/SOX9 CNVs) and the reproductive limitations.
Assisted-reproduction options are restricted to donor sperm with
intrauterine insemination or IVF, since affected individuals are
azoospermic. Surgical correction is appropriate for hypospadias and
cryptorchidism in SRY-negative presentations.
