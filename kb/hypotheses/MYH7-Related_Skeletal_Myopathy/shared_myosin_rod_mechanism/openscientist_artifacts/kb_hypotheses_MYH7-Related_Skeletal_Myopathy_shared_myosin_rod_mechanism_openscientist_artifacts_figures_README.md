# figures/

`lmm_variant_map.png` is **EXTERNAL / not in this bundle**.

The OpenScientist `execute_code` sandbox writes only to its own `/tmp`, which is not
shared with the job filesystem, and the harness auto-saves generated plots to a separate
UI plot store. The binary PNG therefore could not be copied into this bundle.

The figure is fully reproducible by running `../code/lmm_rod_analysis.py` (it regenerates
`lmm_variant_map.png`). All numeric content the figure depicts is in
`../data/lmm_variant_heptad_analysis.csv` and `../logs/execution_log.md`:
- 9 MYH7 LMM variants mapped along the LMM region (res 1281–1935);
- 7/9 remove a conserved R/K charge (binomial p = 1.0e-4);
- all 9 sites identical in MYH2 (LMM 79.6% identical).
