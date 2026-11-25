# Exact queries issued

All endpoints are public and were queried unauthenticated. No credentials, tokens or
signed URLs were used, so none appear in this bundle.

## 1. gnomAD v4.1.0 GraphQL

- Endpoint: `https://gnomad.broadinstitute.org/api` (POST, `application/json`)
- Dataset: `gnomad_r4`, reference genome GRCh38
- Retrieved: 2026-11-25
- HTTP 200, 4,038,505 bytes, 16,637 variants, gene_id `ENSG00000198947`,
  canonical_transcript_id `ENST00000357033`

```graphql
query DMD {
  gene(gene_symbol: "DMD", reference_genome: GRCh38) {
    gene_id
    canonical_transcript_id
    variants(dataset: gnomad_r4) {
      variant_id pos consequence hgvsc hgvsp lof lof_filter transcript_id
      exome  { ac an ac_hemi }
      genome { ac an ac_hemi }
    }
  }
}
```

Follow-up single-variant query used to adjudicate the 140-hemizygote outlier
(response saved at `logs/gnomad_v4_outlier_variant_response.json`):

```graphql
{ variant(variantId: "X-31121883-CTCTGCCCAAATCA-C", dataset: gnomad_r4) {
  variant_id flags
  exome  { ac an ac_hemi filters populations { id ac an } }
  genome { ac an ac_hemi filters }
  transcript_consequences { gene_symbol transcript_id hgvsc hgvsp lof lof_filter lof_flags major_consequence }
} }
```

Filters applied downstream in code, not at the endpoint:
- consequence in {frameshift_variant, stop_gained, splice_acceptor_variant, splice_donor_variant}
- `lof == "HC"` (LOFTEE high confidence)
- hemizygote count = exome.ac_hemi + genome.ac_hemi
- comparator class: `consequence == "synonymous_variant"` in the same gene

## 2. NCBI E-utilities, ClinVar

- Endpoint: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/`
- Database: `clinvar`. Retrieved 2026-11-25. No API key.
- esearch term (3,530 records):

```
DMD[gene] AND ("clinsig pathogenic"[Properties] OR "clinsig likely pathogenic"[Properties])
```

- esummary must be issued as POST with form-encoded `id=`; a GET with ~3,500 ids
  exceeds the URL length limit and returns a payload lacking the `result` key.
- Condition-field subsetting for the reading-frame test used
  `traits contains "Duchenne"` XOR `traits contains "Becker"`, giving N = 1,419.

### Negative search, recorded as a source-level absence

- Database: ClinVar via NCBI E-utilities, snapshot 2026-11-25
- Question: can ClinVar condition annotations reproduce the DMD/BMD reading-frame rule?
- Result: no. Fisher OR 1.57 (95% CI 0.47-5.26), p = 0.45, N = 1,419.
- Cause: the dominant condition term is the composite "Duchenne/Becker muscular
  dystrophy", and submitter usage of the separate terms is inconsistent.
- This is a verified absence for ClinVar specifically. It is NOT evidence against the
  reading-frame rule, which is supported by LOVD/TREAT-NMD/UMD-DMD registries that were
  NOT queried in this run (see MANIFEST `not_accessed`).

## 3. Ensembl REST

- `https://rest.ensembl.org/lookup/id/ENST00000357033?expand=1;content-type=application/json`
- `https://rest.ensembl.org/sequence/region/human/X:31121858..31121920:1?content-type=application/json`
- Retrieved 2026-11-25. ENST00000357033 = DMD-203, minus strand, 79 exons,
  coding exon lengths sum to exactly 11,058 bp (3,686 codons), asserted in code.

## 4. ClinicalTrials.gov API v2

- `https://clinicaltrials.gov/api/v2/studies`
- `query.cond = "Duchenne Muscular Dystrophy"`, `pageSize = 100`, paged via `nextPageToken`
- Retrieved 2026-11-25, 504 studies. Full snapshot in `logs/`.

## 5. GEO

- Series matrix: `GSE6011_series_matrix.txt.gz`, 4,565,454 bytes, HTTP 200
- Platform annotation: `GPL96.annot.gz`, 4,522,748 bytes, HTTP 200
- Retrieved 2026-11-25 over the GEO HTTPS mirror. Preflight log in
  `logs/geo_preflight_log.json`.
- Preflight failure recorded: `GPL6244.annot.gz` returned **HTTP 404**, so the planned
  replication in GSE38417 (HuGene 1.0 ST) was **NOT run**. It is listed as skipped in
  MANIFEST, not as a result.

## 6. PubMed

Searched through the `search_pubmed` MCP tool, 2026-11-25. 53 abstracts retrieved.
Operational note: queries longer than roughly six words returned "No papers found",
and one `efetch` returned HTTP 429, so queries were kept short and spaced. Queries that
returned usable results include: `presymptomatic DMD infant muscle transcriptome`,
`calpain 3 secondary deficiency dystrophin`, `nNOS delocalization dystrophin ischemia`,
`satellite cell polarity dystrophin asymmetric division`, `microtubule NOX2 X-ROS mdx`,
`TRPV2 TRPC1 dystrophic muscle calcium`, `exon skipping dystrophin restoration outcome`.
