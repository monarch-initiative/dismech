Note that this repo is mostly geared around Claude Code.

You MUST read the full contents of @CLAUDE.md

For Codex and any other agent: never create or hand-edit `references_cache/*.md`.
Regenerate cache files with `just fetch-reference <ID>` instead.

For Codex and any other agent: `cache/dataset_accessions.json` is frozen. Never
read it, write it, edit it, or stage it — not even to "refresh" it. Dataset
accessions are verified by fetching them into `references_cache/` (`just
verify-datasets <file>`, which writes `references_cache/GEO_<ID>.md`); commit
that file instead. The shared blob is a single sorted JSON file that every
verifier run rewrote in full, so it collided between concurrent curation PRs.

For the rationale behind project scope, schema, ontology, BioLink/KGX, and evidence
decisions, consult the decision register at `docs/explanation/design-decisions.md`.
