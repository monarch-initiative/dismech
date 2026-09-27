# gnomAD analysis execution log (sanitized)

Date: 2026-09-07
Endpoint: https://gnomad.broadinstitute.org/api (GraphQL, POST)
Tool: OpenScientist `execute_code` (python), allowed stdlib + numpy/requests/matplotlib.
Outcome: SUCCEEDED.

## Preflight
- POST constraint query -> HTTP 200. Returned pLI=2.497951398334237e-16, oe_lof=0.7291,
  oe_lof_upper(LOEUF)=0.8964, lof_z=2.169, mis_z=1.518, syn_z=0.172.

## Attempt 1 (FAILED): gene(...).variants full-field query
- Timed out after 60 s (server compute). Reduced to transcript-level query with fewer fields.

## Attempt 2 (PARTIAL then adjusted): file write to CWD
- `open('asxl1_gnomad_variants.json','w')` -> PermissionError (execute_code sandbox CWD read-only).
- Recovered by performing all computation in-memory within single cells; figure written to /tmp
  inside the sandbox (sandbox-local only; NOT copied to the artifact bundle — see limitation).

## Attempt 3 (SUCCEEDED): transcript ENST00000375687 variants, gnomad_r4
- 5,429 transcript variants returned.
- Consequence breakdown: missense 2060, intron 1342, synonymous 863, frameshift 523,
  5'UTR 225, stop_gained 190, splice_region 87, 3'UTR 53, inframe_del 42, splice_acceptor 15,
  start_lost 10, splice_donor 10, inframe_ins 4, protein_altering 2, stop_lost 2.
- pLoF (stop_gained + frameshift + splice_donor + splice_acceptor) = 738; 714 mapped to aa.

## Derived results (see ../data/*.csv)
- Region densities: N-term 0.325 var/aa; Hotspot(580-1000) 1.038 var/aa; Distal 0.165 var/aa.
- Hotspot holds 61.2% of distinct pLoF and 76.8% of pLoF allele burden over 27% of protein length.
- Top hotspot allele p.Gly646TrpfsTer12 (c.1934dupG) AC=685 AF=4.7e-4 — canonical ASXL1 CHIP/AML driver.
- Hotspot: 44% singletons, all AF < 0.1% (median 6.8e-7).

## Limitations
- gnomAD exome/genome counts do not separate somatic (CHIP) from germline at variant level via these
  fields; CHIP attribution is an inference from ASXL1 biology + variant identity + AF/singleton profile.
- Amino-acid mapping uses genomic->CDS offset on the + strand canonical transcript; frameshift/splice
  variants are mapped by genomic position (approximate protein coordinate).
- The output PNG (asxl1_plof_distribution.png) was generated inside the code sandbox and auto-saved by
  the harness; it is NOT included as a static file in this bundle (sandbox FS is separate from the
  job FS). Re-run code/gnomad_asxl1_analysis.py to regenerate. Marked LOCAL-ONLY / regenerable.
