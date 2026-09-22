# figures/

## ezh2_weaver_lollipop.png — status: EXTERNAL / platform-stored (not copied into bundle)

The lollipop plot of Weaver-syndrome pathogenic EZH2 variant positions on the
746-aa protein was generated inside the OpenScientist `execute_code` sandbox and
auto-saved to the platform plot/provenance store (Iteration 3). The sandbox has
no write access to the job directory, so the PNG binary could not be copied here.

To regenerate deterministically, run `code/clinvar_gnomad_analysis.py` (it writes
`figures/ezh2_weaver_lollipop.png`). The figure content is fully described by
`data/ezh2_clinvar_weaver_plp.csv`:
- 21 missense variants (blue circles): positions 132,133,158 (SANT1 region) and
  626-746 (CXC/SET/post-SET catalytic module) — all in structured functional domains.
- 3 truncating variants (red squares): codons 730, 733, 738 — all C-terminal,
  downstream of the SET domain (ends aa 727), escaping nonsense-mediated decay.
