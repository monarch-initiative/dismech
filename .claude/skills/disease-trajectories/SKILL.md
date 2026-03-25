---
name: disease-trajectories
description: Mine Disease Trajectories (DT/DisTraj) outputs for comorbidity/trajectory candidates, including parsing DT JSON/TSV, extracting directed pairs, filtering by sex or significance, and mapping signals into dismech comorbidity YAML.
---

# Disease Trajectories Mining

Use this skill when you need to mine DT (Disease Trajectories / DisTraj) artifacts and convert them into dismech comorbidity entries.

## Quick start

1) Locate a DT JSON file (often includes a `phase_dict` or edge list).
2) Extract normalized edges with the script below.
3) Pick candidate pairs and map to comorbidity YAML signals.

Example:

```
python .claude/skills/disease-trajectories/scripts/dt_extract_edges.py path/to/dt.json --format tsv > /tmp/dt_edges.tsv
```

## Workflow

### 1) Locate DT artifacts

- Search for candidate files:
  - `rg --files -g "*.json"` and look for names like `phase_dict`, `trajectories`, `edges`.
- If the DT data is external, download and keep the raw file in a scratch location (do not edit in place).

### 2) Inspect schema quickly

Use a quick introspection to identify top-level keys:

```
python - <<'PY'
import json
from pathlib import Path
p = Path("path/to/dt.json")
obj = json.loads(p.read_text())
print(type(obj))
if isinstance(obj, dict):
    print(list(obj.keys())[:20])
PY
```

If there is a `phase_dict` mapping, it usually encodes pair keys like `ICD_A-ICD_B` and may include sex stratification.
If there is an `edges`/`pairs` list, inspect the field names for A/B, sex, and directionality.

### 3) Extract normalized edges

Use the bundled script:

```
python .claude/skills/disease-trajectories/scripts/dt_extract_edges.py path/to/dt.json --format tsv > /tmp/dt_edges.tsv
```

What the script does:
- Handles `phase_dict` mappings with pair keys like `E12-L28`.
- Handles edge lists under `edges`, `links`, `pairs`, `data`, or `trajectories`.
- Normalizes fields to a consistent row format with `disease_a_id`, `disease_b_id`, directionality metrics, sex, p-value, FDR, and source path.

### 4) Filter candidate pairs

Use standard tools on the TSV output (examples):

- Filter for a specific ICD pair:
  - `rg "^E12\tL28\t" /tmp/dt_edges.tsv`
- Filter by directionality:
  - `awk -F '\t' 'NR==1 || $11=="A_BEFORE_B"' /tmp/dt_edges.tsv`
- Filter by sex:
  - `awk -F '\t' 'NR==1 || $3=="male"' /tmp/dt_edges.tsv`

### 5) Map to dismech comorbidity YAML

Create or update a comorbidity file under `kb/comorbidities/`.

Minimum signal mapping:

- `source: DISEASE_TRAJECTORIES`
- `method: EHR_TEMPORAL_COMORBIDITY`
- `signal_disorder_a_id`: ICD code from DT
- `signal_disorder_b_id`: ICD code from DT
- `directionality`: map from DT (A_BEFORE_B / B_BEFORE_A / SAME_TIME / UNKNOWN)
- `a_before_b`, `b_before_a`, `same_time`: preserve DT proportions if provided
- `demographics.sex`: set if DT is stratified
- `mapping_notes`: explain any ICD to dismech mapping or grouping

Example snippet:

```
association_signals:
  - source: DISEASE_TRAJECTORIES
    method: EHR_TEMPORAL_COMORBIDITY
    signal_disorder_a_id: ICD10:E12
    signal_disorder_b_id: ICD10:L28
    demographics:
      sex: MALE
    directionality: A_BEFORE_B
    a_before_b: 1.0
    b_before_a: 0.0
    same_time: 0.0
```

### 6) Validate

Run:

```
just validate-comorbidity kb/comorbidities/<file>.yaml
```

## Scripts

- `scripts/dt_extract_edges.py`
  - Input: DT JSON
  - Output: TSV/CSV/JSONL with normalized edge fields
  - Use when the DT format is unknown or mixed

## Notes and cautions

- Do not assume DT directionality is causal. Preserve `A_before_B`, `B_before_A`, and `same_time` metrics as reported.
- If a DT pair uses grouped ICD codes (e.g., L28), record the grouping in `mapping_notes`.
- Keep DT signals separate from literature signals; they can coexist under `association_signals`.
