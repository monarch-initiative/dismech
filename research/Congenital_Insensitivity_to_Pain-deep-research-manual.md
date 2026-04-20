# Congenital Insensitivity to Pain Deep Research Notes

## Modeling choices applied from PR review

- This revision treats congenital insensitivity to pain as a thin
  phenotype-grouping page, not as a claim that all CIP branches are one cleanly
  unified disease entity.
- I did not split this PR into five standalone subtype pages because that would
  require a larger ontology and evidence expansion than the review was asking
  for. Instead, I trimmed the umbrella and made the shared pathograph explicit.
- The ontology anchor remains `MONDO:0015364` (`hereditary sensory and
  autonomic neuropathy`) only because the exact umbrella term requested in MONDO
  NTR `#10031` is not yet available.
- Subtype-specific disease identity is retained through child MONDO terms for
  `NTRK1` / HSAN IV, `NGF` / HSAN V, `SCN9A` AR-CIP, `SCN11A` / HSAN VII, and
  `PRDM12` / HSAN VIII.

## Disease identity and scope

- PMID:32219415
- Evidence source: `OTHER`
- Quote:
  > Congenital insensitivity to pain (CIP) is caused by extremely rare Mendelian genetic disorders.
- Curation implication:
  This page is valid as a phenotype grouping, but the plural "disorders" argues
  against treating it as a single mechanistic disease record.

## Mechanistic synthesis used in the YAML curation

### 1. PRDM12-dependent nociceptor specification is upstream and distinct

- PMID:32219415
- Evidence source: `OTHER`
- Quote:
  > PRDM12 and CLTCL1 are important in the differentiation from a neural crest cell to a precursor sensory neuron.
- PMID:32219415
- Evidence source: `OTHER`
- Quote:
  > The recent finding that PRDM12 activated NTRK1 expression in nociceptor precursors further cemented the absolute importance of NGF-TRKA signalling for nociceptor genesis.
- Curation implication:
  I split PRDM12-related specification failure into its own atomic node upstream
  of NGF-TRKA trophic signaling rather than hiding it inside a bundled
  developmental umbrella.

### 2. NGF-TRKA trophic failure and developmental apoptosis are separate steps

- PMID:32219415
- Evidence source: `OTHER`
- Quote:
  > The importance of nerve growth factor-tropomyosin receptor kinase A (NGF-TRKA) signalling for nociceptor genesis and subsequent pain sensing.
- PMID:32219415
- Evidence source: `OTHER`
- Quote:
  > CIP can be clinically divided into two groups: developmental disorders where nociceptors fail to develop or undergo early apoptosis through lack of trophic signals;
- PMID:14976160
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > A severe reduction of unmyelinated nerve fibers and a moderate loss of thin myelinated nerve fibers are observed in the patients.
- Curation implication:
  The YAML now separates trophic signaling failure, developmental apoptosis, and
  reduced small-fiber innervation into distinct nodes with explicit downstream
  links.

### 3. SCN9A and SCN11A are grouped only at the level of impaired excitability

- PMID:32219415
- Evidence source: `OTHER`
- Quote:
  > So, activating mutations in SCN9A produce paroxysmal neuropathic pain, with no other obvious clinical features. And bi-allelic non-functional mutations cause congenital painlessness, with the only other consequence being anosmia.
- PMID:24036948
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > Mutant Nav1.9 channels displayed excessive activity at resting voltages, causing sustained depolarization of nociceptors, impaired generation of action potentials and aberrant synaptic transmission.
- Curation implication:
  I kept `SCN9A` and `SCN11A` as separate atomic channelopathy nodes and only
  converged them downstream at "Impaired nociceptor excitability" and then
  "Loss of protective pain perception".

### 4. Shared morbidity belongs on the grouping page

- PMID:32219415
- Evidence source: `OTHER`
- Quote:
  > Coincident with teething in the first year of life, self-mutilation of lips, tongue, fingers and toes often occur.
- PMID:32219415
- Evidence source: `OTHER`
- Quote:
  > Long bone fractures can heal, if allowed to do so, but it is the joint injuries that inevitably lead to Charcot’s joints, and hence progressive orthopaedic deformities.
- Curation implication:
  These findings support keeping a small `phenotypes` block on the grouping page
  even though detailed natural history should eventually move to subtype pages.

### 5. Developmental CIP has a distinctive Staphylococcus aureus complication axis

- PMID:32219415
- Evidence source: `OTHER`
- Quote:
  > Increased susceptibility to Staphylococcus aureus infection is a consequence of deficient NGF-TRKA signalling.
- PMID:32219415
- Evidence source: `OTHER`
- Quote:
  > Distinctive to HSANs is a significant susceptibility to Staphylococcus aureus infections manifest as grumbling skin infections, osteomyelitis and septic arthritis.
- Curation implication:
  The revised YAML now includes a macrophage-centered pathophysiology node and a
  developmental-subtype osteomyelitis phenotype so this clinically important
  complication is not lost.

### 6. HSAN IV should explicitly carry cognitive impairment

- PMID:16138253
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > They had the characteristic clinical features of an abnormally high pain threshold, and mental retardation;
- PMID:14976160
- Evidence source: `HUMAN_CLINICAL`
- Quote:
  > The loss of pain perception in this family is characterized by impairment in the sensing of deep pain and temperature but with normal mental abilities and with most other neurological responses intact.
- Curation implication:
  I added `Intellectual disability` specifically to the HSAN IV branch and left
  HSAN V described as cognitively relatively preserved.

## Deliberate omissions in this revision

- I did not add umbrella-level treatments because management is heavily driven by
  injury surveillance, orthopedic complications, ocular protection, and
  subtype-specific autonomic issues rather than one shared mechanism-directed
  therapy.
- I did not create standalone subtype files in this PR; the current revision is
  intended to satisfy the review by making the grouping page thinner and more
  explicit, not by performing a full subtype decomposition.
