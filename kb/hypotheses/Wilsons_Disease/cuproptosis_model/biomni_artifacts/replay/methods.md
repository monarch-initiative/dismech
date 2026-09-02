# Methods

Inputs were directly retrieved from NCBI GEO (two series matrices and two platform annotations).
Series-matrix files were parsed by reading !Sample_* metadata lines (tab-delimited, quoted) and the expression table between the begin/end markers.
Group assignments derived from sample metadata fields (title, source_name_ch1, characteristics_ch1*), not by column positions.
Platform mapping via GPL annotations; gene symbols extracted and split on delimiters.
Transform decisions based on metadata and distributional heuristics; applied log2(x+epsilon) only if needed.
Per-probe statistics on the log2 scale with Welch's t-test, BH FDR across the full platform, and pooled-SD Cohen's d.
Gene-level representative chosen as the probe with highest global mean across all samples before group labels; all-probe sensitivity recorded.
Reproducibility: analysis.py runs offline with --input-dir raw --output-dir OUTPUT; replay verified byte identity for key tables.