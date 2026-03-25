---
name: create-definitions-from-ohdsi
description: Generate dismech definitions from OHDSI/ATLAS cohort definitions or other computable phenotype logic. Use when converting OMOP cohort JSON, drafting PheKB-style phenotype algorithms, or mapping FHIR/CQL/OMOP rules into dismech `definitions` blocks.
---

# Create Definitions From OHDSI

Use this skill to convert OHDSI/ATLAS cohort definitions into dismech `definitions` blocks and to map FHIR/CQL logic into the same structure.

## Quick start

1. Export an ATLAS/WebAPI cohort definition JSON.
2. Generate a YAML fragment:

```bash
uv run python .claude/skills/create-definitions-from-ohdsi/scripts/ohdsi_cohort_to_definition.py /path/to/cohort.json --wrap
```

3. Paste the fragment into the target disorder file under `definitions`.
4. Normalize to dismech norms (add evidence snippets, scope, criteria set names, and any available term objects).
5. Validate:

```bash
just validate kb/disorders/<Disease>.yaml
```

## Workflow guardrails

- Keep logic concise: express cohort entry, inclusion rules, and exit criteria in `criteria_sets`.
- Use `minimum_required` for numeric logic; put temporal logic in `description`.
- Add evidence snippets from abstracts when the algorithm is derived from a publication.
- Only add `term` objects when the CURIE is in a configured prefix (ICD10CM, NCIT, HP, etc.).

## References

- Mapping guide: `references/model-mapping.md` (FHIR/OHDSI/CQL to dismech)

## Scripts

- `scripts/ohdsi_cohort_to_definition.py`: Convert ATLAS/WebAPI cohort JSON to a dismech definition fragment.
  - Use `--wrap` to emit a top-level `definitions` key.
