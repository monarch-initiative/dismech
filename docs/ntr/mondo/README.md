# Mondo new term requests from dismech

Requests for diseases curated in dismech that have no matching Mondo term. Six have been
filed, as marked in the table below; the other 15 are drafts. Each file follows the fields of Mondo's "Add new term (generic)" issue
form, in order.

Two things make a solid request: literature showing the disease concept exists and can
be defined, and similar concepts already in Mondo. Each draft gives both, under
"Evidence that the concept exists" and "Similar terms already in Mondo".

**Scope.** All 61 entries in `kb/disorders/` with no `disease_term`, checked against
Mondo release 2026-11-03 by label, synonym, cross-reference and causal gene, and against
Mondo's issue tracker. Another 71 entries have a `disease_term` and also a
`skos:broadMatch` mapping; those were not reviewed and may hold more candidates.

## Filed and ready to file (21)

"Open question" is what a Mondo curator is most likely to push back on.

| Request | Proposed parent | Similar terms in Mondo | Open question |
|---|---|---|---|
| [arsenic poisoning](arsenic-poisoning.md) ([filed as Mondo issue 10860](https://github.com/monarch-initiative/mondo/issues/10860)) | heavy metal poisoning | lead, mercury, cadmium, thallium poisoning | None |
| [e-cigarette or vaping product use-associated lung injury](e-cigarette-or-vaping-product-use-associated-lung-injury.md) ([filed as Mondo issue 10861](https://github.com/monarch-initiative/mondo/issues/10861)) | acute lung injury | toxic bronchiolitis, silicosis | None; has ICD-10-CM U07.0 |
| [propofol infusion syndrome](propofol-infusion-syndrome.md) ([filed as Mondo issue 10862](https://github.com/monarch-initiative/mondo/issues/10862)) | poisoning | statin toxicity, neuroleptic malignant syndrome | Best parent |
| [mucopolysaccharidosis type 1, attenuated form](mucopolysaccharidosis-type-1-attenuated-form.md) ([filed as Mondo issue 10863](https://github.com/monarch-initiative/mondo/issues/10863)) | mucopolysaccharidosis type 1 | the same split for type 2 | None |
| [spaceflight associated neuro-ocular syndrome](spaceflight-associated-neuro-ocular-syndrome.md) ([filed as Mondo issue 10864](https://github.com/monarch-initiative/mondo/issues/10864)) | eye disorder | space motion sickness | Best parent |
| [Usutu virus disease](usutu-virus-disease.md) ([filed as Mondo issue 10865](https://github.com/monarch-initiative/mondo/issues/10865)) | Flaviviridae infectious disease | non-human Usutu term, West Nile fever | None |
| [diethylene glycol poisoning](diethylene-glycol-poisoning.md) | poisoning | ethylene glycol poisoning | None |
| [amatoxin poisoning](amatoxin-poisoning.md) | poisoning | ciguatera, ackee, ricin poisoning | Mondo has no mushroom poisoning class to sit under |
| [aconitine poisoning](aconitine-poisoning.md) | poisoning | digitalis, colchicine poisoning | None |
| [carbamate poisoning](carbamate-poisoning.md) | poisoning | organophosphate poisoning | Class-level agent |
| [chemotherapy-induced diarrhea](chemotherapy-induced-diarrhea.md) | chemotherapy-induced toxicity; diarrheal disease | chemotherapy-induced alopecia, mucositis, neuropathy | Symptom or disease |
| [chemotherapy-induced neutropenia](chemotherapy-induced-neutropenia.md) | chemotherapy-induced toxicity; neutropenia | as above | Mondo retired `acquired neutropenia`; reason not reviewed |
| [chemotherapy-induced nausea and vomiting](chemotherapy-induced-nausea-and-vomiting.md) | chemotherapy-induced toxicity | as above | Most likely of the three to be called a symptom |
| [deployment-related constrictive bronchiolitis](deployment-related-constrictive-bronchiolitis.md) | toxic bronchiolitis obliterans | transplant-related, postinfectious forms | Exposure varies between patients |
| [dyssegmental dysplasia](dyssegmental-dysplasia.md) | spondyloepiphyseal dysplasia | its two subtypes (proposed children) | Umbrella term |
| [Chlamydia pneumoniae pneumonia](chlamydia-pneumoniae-pneumonia.md) | pneumonia caused by chlamydia | Mycoplasma pneumoniae pneumonia | The parent has a wrong *C. trachomatis* superclass, which needs fixing first |
| [FLNC-related dilated cardiomyopathy](flnc-related-dilated-cardiomyopathy.md) | familial dilated cardiomyopathy | hypertrophic cardiomyopathy 26 (also FLNC) | Allele-specific: truncating variants only |
| [ANK2-related complex neurodevelopmental disorder](ank2-related-complex-neurodevelopmental-disorder.md) | complex neurodevelopmental disorder | GRIN2B-, CACNA1A-related terms | None; ClinGen Definitive |
| [WAPL-related developmental disorder](wapl-related-developmental-disorder.md) | Mendelian neurodevelopmental disorder | chromosome 10q23 deletion syndrome | Rests on one study (27 individuals) |
| [RAB5C-related neurodevelopmental disorder with macrocephaly](rab5c-related-neurodevelopmental-disorder-with-macrocephaly.md) | Mendelian neurodevelopmental disorder | DDX17-, SETD2-related terms | Rests on one study (12 individuals) |
| [KIF5B-related kyphomelic dysplasia](kif5b-related-kyphomelic-dysplasia.md) | bent bone dysplasia | kyphomelic dysplasia (CCN2 form) | Rests on one study (4 individuals) plus OMIM:621644; Mondo may prefer to restructure `MONDO:0008881` |

## Not drafted

**Already requested. Do not file again.**

| Entry | Existing Mondo issue |
|---|---|
| `CKD-Mineral_Bone_Disorder` | #10128 |
| `MEK_Inhibitor_Induced_Cardiomyopathy` | #10805 |
| `RNU4-2-Related_Autosomal_Recessive_Neurodevelopmental_Disorder` | #10806 |
| `Human_Metapneumovirus_Infection` | #10428, #10412 |
| `Adenovirus_Respiratory_Infection` | #10430, #10414 |
| `Seasonal_Coronavirus_Infection` | #10429, #10413 |

**Mondo already has a term.** Each was compared with the entry's scope.

| Entry | Term | Outcome |
|---|---|---|
| `KATNB1-related_Cortical_Malformation` | `MONDO:0014534` lissencephaly 6 with microcephaly | Bound as `disease_term` |
| `GOLGA2-Related_Golgin_A2_Deficiency` | `MONDO:0859375` developmental delay with hypotonia, myopathy, and brain abnormalities | Bound as `disease_term` |
| `EEFSEC_Deficiency` | `MONDO:0976233` neurodevelopmental disorder with progressive spasticity and brain abnormalities | Bound as `disease_term` |
| `PGM2L1_Deficiency` | `MONDO:0859347` neurodevelopmental disorder with hypotonia, dysmorphic facies, and skin abnormalities | Bound as `disease_term` |
| `Developmental_Stuttering` | `MONDO:0000723` stutter disorder | `skos:closeMatch` only; Mondo's term is hereditary and familial persistent, while the entry covers the common childhood-onset disorder including recovery |
| `USP8-related_pituitary_adenoma_4` | `MONDO:0009050` Cushing disease due to pituitary adenoma | Shared `disease_term` as a narrower stratum (`skos:broadMatch`); `Cushing_Disease` records `skos:exactMatch` |
| `SRPX2-related_Speech_Epilepsy_Polymicrogyria` | `MONDO:0010388` rolandic epilepsy, impaired intellectual development, and speech dyspraxia, X-linked | `skos:narrowMatch` only; the entry also covers polymicrogyria |
| `SLC26A1-Related_Oxalate_Transporter_Deficiency` | `MONDO:0020722` nephrolithiasis susceptibility caused by SLC26A1 | Unchanged `skos:closeMatch`; Mondo models it as a susceptibility, not a recessive disease |
| `CCN2-Related_Kyphomelic_Dysplasia` | `MONDO:0008881` kyphomelic dysplasia | Unchanged `skos:closeMatch`; the term's label covers a heterogeneous group, and its structure depends on the KIF5B request |
| `HHV-8-Associated_Multicentric_Castleman_Disease` | `MONDO:0019754` multicentric Castleman disease | Unchanged `skos:broadMatch`; split requested in [Mondo issue 10866](https://github.com/monarch-initiative/mondo/issues/10866) |

`MONDO:0019754` is labelled as all multicentric Castleman disease but carries the HHV-8
form as an exact synonym, while the idiopathic form (`MONDO:0035838`) sits beside it, not
under it. This is why a split was requested instead of a new term.

**Name collision.** `FICUS_syndrome` is family intensive care unit syndrome, but
`MONDO:0978296` FICUS syndrome is a different, hereditary disease (OMIM:621193). See
Mondo issue #9902 before requesting anything.

**Reversal of a Mondo decision.** `Sarcopenia`: Mondo obsoleted `MONDO:0006516` as "a
natural aging process, and not a disease" (issue #6008). A request has to argue against
that decision directly, using the EWGSOP2 consensus and ICD-10-CM M62.84, so it is a
different kind of request.

**Better suited to a grouping request.** These are umbrellas over existing Mondo terms or
dismech-specific groupings, so a new disease term is the wrong form: `SPOP-Related_Neurodevelopmental_Disorder`,
`TRIO-Related_Neurodevelopmental_Disorder`, `MYO6_Hearing_Loss`,
`SLC5A6-Related_Multivitamin_Transporter_Deficiency`, `BEST1_Bestrophinopathies`,
`KRT1_Keratinopathies`, `MITF_Waardenburg_Tietz_Spectrum`, `ZRS-Related_Limb_Malformation`,
`BBSome-Related_Retinitis_Pigmentosa`, `U4_and_U6_snRNA_Gene-Related_Retinitis_Pigmentosa`,
`Obesity_Due_to_MC4R_Pathway_Disruption`.

**Evidence or fit too thin for now.**

| Entry | Reason |
|---|---|
| `BBOX1-Related_Carnitine_Biosynthesis_Deficiency` | Single first report |
| `HAO1-Related_Glycolate_Oxidase_Deficiency` | Two case reports of a mainly biochemical finding; Mondo rejected a comparable laboratory trait in #10609 |
| `SLC26A6-Related_Hyperoxaluria_and_Nephrolithiasis` | One family |
| `IHH-Related_Polysyndactyly` | One family |
| `Lone_Star_Virus_Infection` | One human case with uncertain attribution |
| `Chlorophacinone_Poisoning` | A broader anticoagulant rodenticide poisoning term would serve better |
| `Transient_Neonatal_Pustular_Melanosis` | Little usable evidence in the entry, and no clear similar term |
| `Volumetric_Muscle_Loss` | An injury; similar human terms are limited to crush syndrome |

**Likely out of scope.** These describe a symptom or a normal-aging process, the reason
given for obsoleting sarcopenia: `Dorsalgia`, `Acute_Post-Surgical_Pain`,
`Ageing_Associated_Decline_in_Intrinsic_Capacity`.

## Corrections for dismech

- `Deployment-Related_Constrictive_Bronchiolitis` records `MONDO:0100127` as `skos:narrowMatch`. The entry is the narrower concept, so this should be `skos:broadMatch`.
