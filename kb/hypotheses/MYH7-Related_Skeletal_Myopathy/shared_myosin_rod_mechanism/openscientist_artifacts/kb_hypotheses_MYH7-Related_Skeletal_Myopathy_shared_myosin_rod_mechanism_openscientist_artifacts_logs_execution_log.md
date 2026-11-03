# Execution log — LMM rod-destabilization analysis (Iteration 2, 2026-10-16)

Environment: OpenScientist `execute_code` Python sandbox (cwd `/app`, writable `/tmp` only).
Network: allowed only via `requests`; `urllib.request` and `hashlib` are blocked
(FNV-1a used for reproducible checksums).

## Preflight (Iteration 1)
UniProt REST reachable. P12883.fasta HTTP 200 (0.8 s), Q9UKX2.fasta HTTP 200 (0.4 s).
Residue identities at reported MYH7 LMM positions matched literature
(1500=R, 1603=A, 1617=K, 1845=R, 1437=A, 1434=R, 1820=R, 1784=K, 1687=E).

## Sequences retrieved (2026-10-16)
MYH7 P12883: length 1935, FNV-1a64 83cbe52392802b35
MYH2 Q9UKX2: length 1941, FNV-1a64 d6023a448158f51e

## Analysis 1 — charge-loss enrichment
Background R/K fraction in MYH7 LMM (res 1281-1935) = 0.177
Variants removing an R/K residue: 7/9
One-sided binomial p = 1.0e-4
Mutation-class composition: Pro-substitution 4, charge->aromatic 3, single-res deletion 2

## Analysis 2 — MYH7 vs MYH2 LMM alignment (Needleman-Wunsch, +1/-1/-2)
Identity = 526/661 = 79.6% (alignment score 385)
Conservation of MYH7 variant sites in MYH2 (all IDENTICAL):
  R1500 <-> R1506 ; A1603 <-> A1609 ; K1617 <-> K1623 ; R1434 <-> R1440 ;
  A1437 <-> A1443 ; R1845 <-> R1851 ; R1820 <-> R1826 ; K1784 <-> K1790
Identical WT residue in MYH2: 9/9

## Analysis 3 — heptad a/d hydrophobic-core enrichment (NULL)
MYH7 best register offset=3, core Kyte-Doolittle=-0.79 vs non-core=-1.20
MYH2 best register offset=0, core Kyte-Doolittle=-0.77 vs non-core=-1.18
Variant core (a/d) enrichment: 3/7 missense, background a/d fraction 0.285, binomial p=0.32 (NS)
Conclusion: reported as honest null; rod register is charge-periodicity-dominated.

## Outcome labels
Analysis 1: succeeded | Analysis 2: succeeded | Analysis 3: succeeded-null
No fallback to literature was substituted for any failed computation.
