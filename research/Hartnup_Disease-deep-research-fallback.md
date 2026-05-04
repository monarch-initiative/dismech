# Hartnup Disease Deep Research Fallback

Date: 2026-05-04

## Provider Attempts

- `timeout 120 just research-disorder falcon Hartnup_Disease`
  - Result: timed out after the bounded 120-second run and was terminated by signal 15.
  - Completed artifact: none.
- `timeout 120 just research-disorder openai Hartnup_Disease`
  - Result: timed out after the bounded 120-second run and was terminated by signal 15.
  - Completed artifact: none.

## Evidence Scope Used For Curation

The YAML curation therefore used structured Orphanet evidence plus cached PubMed
records with exact snippet audit coverage.

### Structured Source

- `ORPHA:2116` Hartnup disease structured record
  - Exact MONDO cross-reference: `MONDO:0009324`
  - Exact OMIM cross-reference: `OMIM:234500`
  - Inheritance: autosomal recessive
  - Genes: `SLC6A19` and `CLTRN`
  - Phenotypes: neutral hyperaminoaciduria, cutaneous photosensitivity, ataxia,
    neuropsychiatric features, ocular findings, malabsorption, elevated urinary
    indican, and other HPO annotations

### PubMed Records

- `PMID:15286787` Kleta et al. 2004
  - Identifies SLC6A19/B0AT1 mutations in the original Hartnup family and
    Japanese families.
  - Supports impaired neutral amino acid transport across renal proximal tubule
    and intestinal mucosa.
- `PMID:15286788` Seow et al. 2004
  - Independently identifies SLC6A19 as the Hartnup gene.
  - Shows tested disease-causing mutations reduce neutral amino acid transport
    in vitro.
- `PMID:16052352` Broer et al. 2006
  - Reviews the molecular basis of neutral aminoacidurias and B0AT1/SLC6A19
    involvement in kidney and intestine.
- `PMID:2472426` Jonas and Butler 1989
  - Reports tryptophan ethyl ester bypass of defective gastrointestinal neutral
    amino acid transport in a child with Hartnup disease.
- `PMID:40852587` Alkhofash and Ali 2025
  - Tests Hartnup disease-causing B0AT1 variants and supports ER retention /
    plasma membrane trafficking defects as a mechanism for transport loss.
- `PMID:7955499` Oakley and Wallace 1994
  - Reports adult pellagra presentation diagnosed by urinary amino acid
    chromatography and responsive to oral nicotinamide.

## Integration Notes

The YAML integrates the evidence into a mechanism chain:

1. SLC6A19/B0AT1 transporter loss of function.
2. Variant trafficking defects for selected B0AT1 alleles.
3. Renal and intestinal neutral amino acid transport defect.
4. Neutral hyperaminoaciduria, malabsorption, elevated urinary indican, and
   reduced tryptophan availability.
5. Pellagra-like neurocutaneous manifestations responsive to nicotinamide in
   symptomatic disease and experimentally bypassed by tryptophan ethyl ester.

The provider timeouts mean no additional narrative deep-research synthesis was
available beyond the evidence-backed curation and local audits.
