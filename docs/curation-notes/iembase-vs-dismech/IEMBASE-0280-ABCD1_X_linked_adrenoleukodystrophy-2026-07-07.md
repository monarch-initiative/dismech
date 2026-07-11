# IEMbase 0280: ABCD1-related X-linked adrenoleukodystrophy and adrenomyeloneuropathy

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 280 |
| Nosology | 14.2.01.01 |
| Gene | ABCD1 |
| External IDs | OMIM:300100; ORPHA:369942 |
| Generated mapping | UNMAPPED; weak candidate `adrenoleukodystrophy.yaml` |
| Candidate DisMech targets | `adrenoleukodystrophy.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ABCD1-related X-linked adrenoleukodystrophy and
adrenomyeloneuropathy. Prevalence is listed as 1:17,000. Treatability is
marked yes.

The characteristic clinical row is hyperpigmentation. Additional rows include
adrenal insufficiency, Addison crisis, electrolyte changes, gonadal failure,
sexual dysfunction, leukodystrophy, spastic paresis, peripheral nerve
involvement, sphincter-control problems, behavioral disorder, dementia,
epilepsy, abnormal EEG, abnormal brain evoked response audiometry, abnormal
VEP, perceptive hearing loss, vision loss or optic atrophy, and alopecia. The
biochemical hallmark is increased plasma very-long-chain fatty acids.

Treatment rows include hematopoietic stem-cell transplant, marked as lowering
VLCFA and targeting neurologic features, and lentiviral gene therapy for
cerebral adrenoleukodystrophy.

## DisMech phenotype coverage

`adrenoleukodystrophy.yaml` is the correct local target despite the generated
UNMAPPED status. The local entry models ABCD1-mediated peroxisomal fatty-acid
transport failure, VLCFA accumulation, oxidative stress, astrocyte and
microglial dysfunction, blood-brain-barrier disruption, inflammatory cerebral
demyelination, adrenomyeloneuropathy spinal-cord axonopathy, adrenocortical
dysfunction, and gonadal dysfunction. It includes childhood cerebral ALD, AMN,
and Addison-only subtypes.

The local phenotype coverage includes progressive spastic paraplegia, bladder
and bowel dysfunction, adrenal insufficiency, hyperpigmentation, weight loss,
anorexia, CNS demyelination, cerebral white-matter lesions, hypogonadism,
leukoencephalopathy, behavioral abnormality, cognitive impairment, visual loss,
progressive myelopathy, and peripheral neuropathy. Local treatments include
lentiviral gene therapy, hematopoietic stem-cell transplantation,
glucocorticoid replacement, VLCFA testing, molecular testing, and brain MRI.

## Concordance and completeness

Judgement: false negative mapping; resolve to `adrenoleukodystrophy.yaml`.

IEMbase and DisMech agree on ABCD1 identity, X-linked inheritance, elevated
plasma VLCFA, adrenal disease with hyperpigmentation, cerebral leukodystrophy,
AMN/spastic myelopathy, peripheral nerve involvement, sphincter dysfunction,
gonadal/sexual dysfunction, behavioral and cognitive disease, visual
involvement, HSCT, and lentiviral gene therapy. DisMech is richer for
mechanistic chain, subtype structure, adrenal steroid replacement, diagnostics,
and current trial context.

IEMbase adds review prompts for perceptive hearing loss, abnormal BAEP/VEP,
EEG abnormality, alopecia, and Addison-crisis wording.

## Curation actions

- Resolve this record to `adrenoleukodystrophy.yaml`.
- Treat the generated weak candidate as a true target; the low score appears to
  be a matching/naming artifact rather than a biology issue.
- Use IEMbase's hearing-test, VEP/EEG, alopecia, and Addison-crisis rows as
  enrichment prompts.
