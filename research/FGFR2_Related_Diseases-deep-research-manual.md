---
provider: manual_pubmed_review
model: n/a
cached: false
start_time: '2026-03-27T15:10:00Z'
end_time: '2026-03-27T15:40:00Z'
duration_seconds: 1800.0
citation_count: 20
notes: >
  This is a grouped FGFR2 cross-entry research note, so the single-disorder
  justfile targets were not used. Automated provider runs using the direct
  `uv run deep-research-client research --input-file ...` pattern stalled in
  this environment (openai and falcon both remained silent and produced no
  output files). Manual deep research was completed from primary PubMed and
  authoritative NCBI/FDA/NCI sources.
---

## Question

Provide a grouped mechanistic review of FGFR2-related human diseases, with emphasis on genotype-phenotype correlations, why different FGFR2 variants produce different syndromes, and which somatic FGFR2 alteration classes matter across cancers.

## Automated Command

Use a direct grouped input file rather than `just research-disorder`:

```bash
uv run deep-research-client research \
  --input-file research/FGFR2_Related_Diseases-deep-research-query.md \
  --provider openai \
  --model o3-deep-research-2025-06-26 \
  --title "FGFR2-related diseases" \
  --keyword FGFR2 \
  --keyword craniosynostosis \
  --keyword cholangiocarcinoma \
  --output research/FGFR2_Related_Diseases-deep-research-openai.md \
  --separate-citations research/FGFR2_Related_Diseases-deep-research-openai.md.citations.md
```

Fallback provider:

```bash
uv run deep-research-client research \
  --input-file research/FGFR2_Related_Diseases-deep-research-query.md \
  --provider falcon \
  --title "FGFR2-related diseases" \
  --keyword FGFR2 \
  --keyword craniosynostosis \
  --keyword cholangiocarcinoma \
  --output research/FGFR2_Related_Diseases-deep-research-falcon.md \
  --separate-citations research/FGFR2_Related_Diseases-deep-research-falcon.md.citations.md
```

## Output

# FGFR2-Related Diseases: Mechanistic Summary

## Bottom line

FGFR2-related disease separates into three broad mechanistic groups:

1. Germline craniosynostosis and skeletal dysplasia syndromes driven mostly by heterozygous gain-of-function missense variants in the extracellular or transmembrane region.
2. Germline developmental disorders driven by reduced FGFR2b signaling, especially the FGF10-FGFR2b epithelial-mesenchymal pathway.
3. Somatic cancers driven by FGFR2 fusions/rearrangements, activating mutations, or amplification/overexpression depending on tumor type.

Why one mutation causes one syndrome and not another is partly understood. The strongest determinants are mutation class, exact residue, domain, isoform context, and developmental tissue context. The cleanest example is Apert syndrome, where the recurrent linker mutations p.Ser252Trp and p.Pro253Arg alter ligand affinity and ligand specificity. In contrast, the Crouzon/Jackson-Weiss/Pfeiffer boundary is only partly discrete: there are clear syndrome-enriched alleles, but multiple identical FGFR2 alleles have been reported across more than one named syndrome.

## Mendelian Disorders

| Disease | OMIM / note | Germline vs somatic | Alteration class | Recurrent variants | Core mechanism | Key distinguishing phenotype | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Apert syndrome | OMIM 101200 | Germline AD | Mostly heterozygous missense; rare splice / rearrangement | p.Ser252Trp, p.Pro253Arg | Altered ligand affinity and loss of normal FGFR2b/FGFR2c ligand specificity; ectopic ligand-dependent signaling | Multisuture craniosynostosis plus severe symmetric syndactyly | Very strong |
| Crouzon syndrome | OMIM 123500 | Germline AD | Heterozygous missense, splice, rare indel | p.Gln289Pro, p.Trp290Gly/Arg, p.Cys342Tyr/Arg/Ser, p.Ala344Gly | Mostly activating extracellular-domain alleles, often affecting IgIII; many preserve limbs | Craniosynostosis, midface retrusion, normal hands and feet | Very strong |
| Jackson-Weiss syndrome | OMIM 123150 | Germline AD | Heterozygous missense and rare truncating variants | p.Cys342Arg, p.Cys342Ser, p.Gln289Pro, p.Ala344Gly | Overlaps the Crouzon/Pfeiffer allelic spectrum; likely activating or abnormal-dimerization alleles | Craniosynostosis with characteristic foot anomalies | Strong, but boundary with Crouzon/Pfeiffer is spectrum-like |
| Pfeiffer syndrome | OMIM 101600 | Germline AD | Heterozygous missense; FGFR2 major cause of severe disease | p.Trp290Cys, p.Tyr340Cys, p.Cys342Arg, p.Ser351Cys | Activating alleles, often severe extracellular-domain changes; some codon-specific cysteine-creating alleles are strongly syndrome-enriched | Broad medially deviated thumbs and halluces; severe types 2/3 with cloverleaf skull | Very strong |
| Beare-Stevenson cutis gyrata syndrome | OMIM 123790 | Germline AD | Heterozygous missense | p.Ser372Cys, p.Tyr375Cys / p.Tyr394Cys current transcript numbering | Likely constitutive activation affecting epithelial and mesenchymal contexts; mouse data support downstream p38 activation | Craniosynostosis plus cutis gyrata, acanthosis nigricans, anogenital / umbilical anomalies | Strong |
| Bent bone dysplasia syndrome 1 | OMIM 614592 | Germline AD | Heterozygous transmembrane missense | p.Tyr381Asp, p.Met391Arg | Distinct from classic craniosynostosis GOF: deficient canonical membrane signaling with abnormal nucleolar FGFR2 activity, ribosomal stress, and impaired osteoblast differentiation | Bent long bones, hypomineralization, craniosynostosis, perinatal lethality or extreme severity | Strong but ultra-rare |
| LADD syndrome / LADD1 | OMIM 149730 | Germline AD | Heterozygous kinase-domain missense | p.Ala628Thr, p.Ala648Thr, p.Arg649Ser | Reduced FGFR2 tyrosine kinase activity and attenuated FGF10-FGFR2b signaling; dominant-negative effect is supported experimentally | Lacrimal, auricular, dental, and digital malformations without craniosynostosis | Strong |
| Ectrodactyly with pulmonary acinar dysplasia due to FGFR2 | One reported family | Germline AR | Homozygous missense | p.Arg255Gln | Partial loss of function in homozygosity | Ectrodactyly plus lethal pulmonary acinar dysplasia | Limited but mechanistically compelling |

## Other Reported FGFR2 Associations

- FGFR2-related Antley-Bixler syndrome has been reported, especially with p.Ser351Cys, but the historical assignment is not clean. The original 1998 FGFR2 case was followed by published objections that the phenotype may not have been true Antley-Bixler syndrome. Treat this association as limited and label-sensitive rather than as a core definitive FGFR2 disease.
- GeneReviews also notes rare FGFR2-associated isolated coronal synostosis, but explicitly flags uncertainty about whether some reported infants later evolved recognizable syndromic phenotypes.

## Somatic Cancer Entities

| Disease | Germline vs somatic | Alteration class | Recurrent alterations | Core mechanism | Notes | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Intrahepatic cholangiocarcinoma | Somatic | Fusions / rearrangements | Multiple in-frame FGFR2 fusions and rearrangements preserving the kinase domain | Fusion-driven constitutive signaling; strongest FGFR2 cancer indication | Clinically established target with pemigatinib and futibatinib approvals / approval summaries | Very strong |
| Gastric / gastroesophageal adenocarcinoma | Somatic | Amplification and FGFR2b overexpression; less often other classes | FGFR2 amplification, FGFR2b-positive tumors | Copy-number-driven oncogene addiction in a subset; ligand/receptor pathway activation | Strong recurrent segment, especially diffuse / scirrhous-type biology; clinically important but not as settled as cholangiocarcinoma | Strong |
| Endometrial carcinoma, especially endometrioid subtype | Somatic | Activating missense and splice variants | Multiple activating FGFR2 mutations, some paralleling germline craniosynostosis codons | Oncogenic FGFR2 signaling, including EGFR and Notch crosstalk in experimental systems | Recurrent and biologically convincing | Strong |
| Urothelial carcinoma | Somatic | Historically FGFR2/3 mutations and fusions; currently FGFR3 dominates approved use | Mixed FGFR2 or FGFR3 susceptible alterations in the 2019 accelerated label | FGFR-driven subset exists, but FGFR2 contribution is weaker and less central than FGFR3 | Current full FDA approval is FGFR3-specific, not FGFR2/3 | Moderate for FGFR2 specifically |

Rare FGFR2 alterations are also reported across other solid tumors, but current evidence is most mature for cholangiocarcinoma, gastric / GEJ cancer, and endometrial carcinoma. Common germline intronic FGFR2 breast cancer risk SNPs are important susceptibility loci, but they do not define a Mendelian FGFR2 disease and should not be mixed with the high-penetrance syndromic disorders above.

## Why Different FGFR2 Mutations Produce Different Diseases

### 1. Exact residue matters, not just the domain

The clearest mutation-specific split is in the craniosynostosis spectrum:

- Apert syndrome is overwhelmingly caused by p.Ser252Trp or p.Pro253Arg in the IgII-IgIII linker.
- Severe Pfeiffer syndrome is strongly enriched for cysteine-creating alleles such as p.Trp290Cys and p.Tyr340Cys.
- Non-cysteine substitutions at the same or adjacent codons, such as p.Trp290Gly / p.Trp290Arg and p.Tyr340His, are preferentially associated with Crouzon syndrome.

This is strong evidence that syndrome assignment depends on the biochemical consequence of the amino acid change, not just on mutation proximity.

### 2. Isoform and tissue context matter

FGFR2 has epithelial FGFR2b and mesenchymal FGFR2c splice isoforms. Apert syndrome is the best understood example of isoform boundary failure: the canonical linker mutations loosen ligand specificity so that ligands normally restricted to one isoform can activate the other. This creates ectopic signaling across epithelial-mesenchymal developmental boundaries and plausibly explains the syndactyly and broader tissue involvement that distinguish Apert syndrome from Crouzon syndrome.

For LADD syndrome, the relevant axis is different: the disease reflects reduced signaling through the epithelial FGF10-FGFR2b pathway that is required for branching morphogenesis of lacrimal and salivary glands and other organs. That explains why LADD produces glandular, dental, ear, and digital malformations rather than craniosynostosis.

### 3. Some variants act mainly by constitutive activation, others by altered ligand recognition, and others by reduced signaling

- Apert: altered ligand affinity / altered ligand specificity with retained ligand dependence.
- Many Crouzon / Pfeiffer / Jackson-Weiss alleles: activating extracellular-domain alleles, often involving abnormal cysteine chemistry or abnormal dimerization.
- Beare-Stevenson: likely constitutive activation with strong skin as well as skull effects.
- Bent bone dysplasia: not well explained by the usual plasma-membrane gain-of-function model; transmembrane variants show deficient canonical signaling but abnormal nucleolar activity and ribosomal-stress biology.
- LADD and acinar dysplasia: reduced signaling / partial loss of function rather than gain of function.

### 4. Shared alleles show that named syndromes are partly labels on a continuous allelic series

This is the main reason the boundary between Crouzon, Jackson-Weiss, and Pfeiffer is only partly predictable from genotype:

- The same FGFR2 variant has been reported in different named syndromes.
- GeneReviews notes that individuals with the same pathogenic variant have been diagnosed with either Pfeiffer or Crouzon syndrome.
- Shared alleles are well documented for p.Cys342Arg, p.Cys342Ser, p.Gln289Pro, and p.Ala344Gly.

The inference is that variant effect is necessary but not always sufficient for categorical syndrome assignment. Modifier loci, developmental background, ascertainment, and syndrome labeling conventions still matter.

### 5. Evidence strength is uneven across the FGFR2 disease map

Most secure mechanistic rules:

- Apert: very strong
- Severe Pfeiffer codons p.Trp290Cys and p.Tyr340Cys vs Crouzon p.Trp290Gly / p.Trp290Arg and p.Tyr340His: strong
- LADD as reduced FGF10-FGFR2b signaling: strong
- Bent bone dysplasia as a distinct FGFR2 mechanism: strong but based on very rare disease

Less settled areas:

- Exact rules separating Crouzon from Jackson-Weiss
- Whether all historical FGFR2-related Antley-Bixler labels represent the same entity
- How much syndrome assignment reflects true biology vs historical clinical naming

## Variant-Level Craniosynostosis / Skeletal Spectrum

| Variant / codon | Domain / exon context | Isoform relevance | Syndrome(s) reported | Interpretation |
| --- | --- | --- | --- | --- |
| p.Ser252Trp, p.Pro253Arg | IgII-IgIII linker, exon 7 / exon IIIa or U in older literature | Common to FGFR2b and FGFR2c; disrupts normal ligand selectivity across the splice boundary | Apert syndrome | Near-canonical Apert alleles; strongest syndrome-specific FGFR2 genotype-phenotype rule |
| p.Gln289Pro | Amino-terminal part of IgIII, exon common to both splice forms | May affect both splice forms | Crouzon, Jackson-Weiss | Shared allele argues that background / modifier effects matter |
| p.Trp290Gly, p.Trp290Arg | IgIII common region | Can affect both splice forms, but craniofacial mesenchymal phenotype dominates | Crouzon | Crouzon-enriched non-cysteine substitutions |
| p.Trp290Cys | Same codon as above | Same structural neighborhood, different biochemical consequence | Pfeiffer, especially severe | Strong example that cysteine-creating change at same codon shifts syndrome and severity |
| p.Tyr340His | IgIII extracellular region | Mostly FGFR2c-relevant craniosynostosis context | Crouzon | Crouzon-enriched |
| p.Tyr340Cys | Same codon | Cysteine-creating activating change | Pfeiffer, especially severe | Same-codon syndrome divergence |
| p.Cys342Arg / Ser / Tyr and related C342 substitutions | IgIII extracellular region | Classic FGFR2 craniosynostosis hot spot | Crouzon, Jackson-Weiss, Pfeiffer | Shared hot-spot group; poor syndrome specificity |
| p.Ala344Gly | IgIIIc | FGFR2c-heavy context | Crouzon, Jackson-Weiss | Shared allele; supports allelic-series model |
| p.Ser351Cys | IgIII extracellular region | FGFR2 craniosynostosis context | Severe Pfeiffer; historical FGFR2-related Antley-Bixler case | Severe allele, but disease label may vary |
| p.Ser372Cys, p.Tyr375Cys / p.Tyr394Cys | Juxtamembrane extracellular region | Likely affects epithelial and mesenchymal contexts | Beare-Stevenson | Strong syndrome enrichment because skin phenotype accompanies craniosynostosis |
| p.Tyr381Asp, p.Met391Arg | Transmembrane domain | Shared by both splice isoforms but mechanistically distinct from classic extracellular GOF | Bent bone dysplasia | Syndrome-specific mechanism with nucleolar stress biology |
| p.Ala628Thr, p.Ala648Thr, p.Arg649Ser | Kinase domain | Best understood in FGFR2b developmental signaling | LADD | Reduced kinase output / dominant-negative developmental signaling, not craniosynostosis |
| p.Arg255Gln in homozygosity | IgIII domain | Developmental loss-of-function context | Ectrodactyly with acinar dysplasia | Single-family, recessive partial LOF |

## Established vs Inference

### Established from primary / authoritative sources

- FGFR2 definitively causes Apert, Crouzon, Jackson-Weiss, Pfeiffer, Beare-Stevenson, bent bone dysplasia, and LADD syndrome.
- Apert syndrome is mechanistically distinct because the canonical p.Ser252Trp and p.Pro253Arg variants alter ligand affinity and ligand specificity.
- Crouzon, Jackson-Weiss, and Pfeiffer syndromes are an overlapping FGFR2 allelic series with both syndrome-enriched and shared variants.
- FGFR2 fusion / rearrangement-positive intrahepatic cholangiocarcinoma is the clearest somatic FGFR2 cancer entity.
- Gastric cancer is the clearest recurrent FGFR2 amplification / FGFR2b overexpression setting.
- Endometrial carcinoma contains recurrent activating FGFR2 mutations.

### Inference or still not fully resolved

- The exact threshold at which a shared FGFR2 allele becomes clinically labeled Crouzon vs Jackson-Weiss vs Pfeiffer.
- The full role of modifier genes and tissue background in the craniosynostosis spectrum.
- Whether all older FGFR2-related Antley-Bixler reports represent one coherent disease entity.
- How broadly non-cholangiocarcinoma FGFR2 fusion tumors should be grouped into stable disease entities rather than basket-trial molecular subsets.

## References

- PMID:7581378
- PMID:9700203
- PMID:8696350
- PMID:9385368
- PMID:9605588
- PMID:11121055
- PMID:16418739
- PMID:16501574
- PMID:17525745
- PMID:17682060
- PMID:22387015
- PMID:22585574
- PMID:23493349
- PMID:27323706
- PMID:28595297
- PMID:37289037
- NCBI Bookshelf: FGFR Craniosynostosis Syndromes Overview
- FDA / NCI drug and approval pages for pemigatinib and erdafitinib
