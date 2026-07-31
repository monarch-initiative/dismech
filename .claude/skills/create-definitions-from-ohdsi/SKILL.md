---
name: create-definitions-from-ohdsi
description: Generate dismech definitions from OHDSI/ATLAS cohort definitions or other computable phenotype logic. Use when converting OMOP cohort JSON, drafting PheKB-/OHDSI-style phenotype algorithms, or mapping FHIR/CQL/OMOP rules into dismech `definitions` blocks.
---

# Create Definitions From OHDSI

Use this skill to convert OHDSI/ATLAS cohort definitions into dismech `definitions` blocks and to map FHIR/CQL logic into the same structure.

## Quick start

You can convert either a **local ATLAS JSON export** or a **live WebAPI cohort**.

1. Get the cohort logic, one of:
   - Export an ATLAS/WebAPI cohort definition JSON to a file, or
   - Note a running WebAPI base URL + cohort id (public demo:
     `https://atlas-demo.ohdsi.org/WebAPI`).
2. Generate a YAML fragment:

```bash
# From a local file
uv run python .claude/skills/create-definitions-from-ohdsi/scripts/ohdsi_cohort_to_definition.py /path/to/cohort.json --wrap

# Live from a WebAPI (fetches GET {url}/cohortdefinition/{id})
uv run python .claude/skills/create-definitions-from-ohdsi/scripts/ohdsi_cohort_to_definition.py \
    --webapi-url https://atlas-demo.ohdsi.org/WebAPI --cohort-id 1782168 --wrap
```

3. Paste the fragment into the target disorder file under `definitions`.
4. Normalize to dismech norms (add evidence snippets, scope, criteria set names, and any available term objects).
   - A cohort pulled from the **OHDSI Phenotype Library** (or another validated
     source) can carry `derivation_basis: ESTABLISHED_CRITERIA`; an ad-hoc or
     mechanism-predicated cohort should not (see the design register §11).
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
  - Positional `json_path` reads a local ATLAS export.
  - `--webapi-url <base>` + `--cohort-id <id>` fetches the cohort live from a
    WebAPI (`GET {base}/cohortdefinition/{id}`); `--timeout` bounds the request
    (default 30s). The two input modes are mutually exclusive.
  - Use `--wrap` to emit a top-level `definitions` key.
  - `--name` / `--description` / `--scope` override the derived fields.

  A synced copy lives at `scripts/ohdsi_cohort_to_definition.py` in the repo
  root — keep the two identical when editing.
