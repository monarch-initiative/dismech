# Development Notes

## 2025-12-08

### linkml-data-qc Now on PyPI

Updated project to use `linkml-data-qc` from PyPI instead of local development install:
- Removed local path override from `pyproject.toml`
- Added `[viz]` extras for dashboard visualization features
- Version 0.1.0 installed with matplotlib, seaborn, pillow dependencies

### QC Dashboard

Added new `just gen-dashboard` target that generates a visual HTML dashboard:
- Uses `linkml-data-qc --dashboard-dir dashboard/`
- Creates `dashboard/index.html` with charts and tables
- Shows slot compliance comparison across all 56 disorder files
- Highlights the 10 lowest-compliance files as priority curation targets
- Includes detailed per-file charts for priority files

Dashboard contents:
- `index.html` - Main dashboard page
- `comparison.png` - Slot compliance bar chart
- `detail_*.png` - Per-file heatmaps for priority files
- `reports.json` - Raw report data

### Reference Validation Findings

Ran comprehensive reference validation (`just validate-references-all`) and discovered significant issues with fabricated evidence snippets in several Mendelian disease files.

#### Key Issues Found

1. **Fabricated snippets**: Evidence snippets were AI-generated paraphrases rather than actual quotes from cited papers. The reference validator correctly flagged these with low similarity scores (0-37%).

2. **Wrong PMIDs**: Several PMIDs pointed to completely unrelated papers:
   - `PMID:30084541` in Dravet_syndrome.yaml was about "Black Phosphorus Nanosheets Passivation Using a Tripeptide" - not Dravet syndrome
   - `PMID:22267103` was about "How to use insulin-like growth factor 1 (IGF1)" - not Dravet syndrome
   - `PMID:34812478` was about "catastrophic natural disasters impact on arts nonprofits" - not Dravet syndrome
   - `PMID:31428203` in Fanconi_Anemia.yaml was about "insulin-glucose metabolism in diabetic mice" - not Fanconi anemia

#### Files Fixed

**Fanconi_Anemia.yaml:**
- Replaced 5 fabricated snippets with real quotes from PMID:35596788 (Peake & Noguchi 2022 review) and PMID:20301575 (GeneReviews)
- Removed 8 unverifiable evidence items, converted claims to `notes` fields
- Quotes now use exact text from abstracts (with proper YAML quoting for colons)

**Dravet_syndrome.yaml:**
- Removed all evidence citing wrong PMIDs (30084541, 22267103, 34812478)
- Used only PMID:21463282 (Oakley et al. 2011 "Insights into pathophysiology and therapy from a mouse model of Dravet syndrome")
- Added 4 verified quotes from that paper
- Moved unverifiable claims to `notes` fields

#### Lessons Learned

1. **Always validate references**: The reference validator is essential for catching AI hallucinations. Run `just validate-references file` before committing evidence items.

2. **Use actual quotes**: Snippets must be exact quotes from abstracts, not paraphrases. The validator checks substring matching.

3. **Verify PMIDs independently**: Don't trust that a PMID is correct - check the cached abstract in `references_cache/pmid_*.md` or fetch it fresh.

4. **When in doubt, use notes**: If a claim is well-established but you can't find a quotable snippet, put it in `notes` rather than fabricating evidence.

### Compliance Analysis

Ran `just compliance-weighted` with the QC config:

- **Global compliance**: 56.1%
- **Weighted compliance**: 75.3%
- **Term coverage**: 93.0%
- **Evidence coverage**: 77.7%
- **Description coverage**: 26.4%

Critical paths are meeting thresholds:
- `phenotypes[].phenotype_term.term`: 99.5% (threshold: 90%)
- `disease_term.term`: 98.2% (threshold: 95%)
- `pathophysiology[].cell_types[].term`: 100% (threshold: 85%)
- `treatments[].treatment_term.term`: 100% (threshold: 80%)

Violations are in sparse data paths (locations, chemical_entities, pathways) indicating areas for future data enrichment, not config issues.
