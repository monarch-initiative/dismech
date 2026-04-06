# Feature Request: Configuration for Unsupported Reference Prefixes

## Summary

The `linkml-reference-validator` needs a configuration option to control behavior for unsupported or unfetchable reference types. Currently, any reference with an unsupported prefix (e.g., `sra:`, `mgnify:`) results in a hard `ERROR`, blocking validation even when the data is otherwise correct.

## Current Behavior

When validating data with references that use prefixes without registered source handlers:

```
[ERROR] Could not fetch reference: sra:PRJNA290729
[ERROR] Could not fetch reference: mgnify:MGYS00000596
[ERROR] Could not fetch reference: bioproject:PRJNA566284
```

The validator exits with code 1, treating these as validation failures equivalent to actual data errors (like title mismatches).

## Problem

In the `dismech` knowledge base, we have datasets with accessions from multiple sources:
- **Supported**: `geo:GSExxxxx`, `PMID:xxxxxxxx`
- **Unsupported**: `sra:PRJNAxxxxxx`, `mgnify:MGYSxxxxxxxx`, `bioproject:PRJNAxxxxxx`

The unsupported sources are legitimate dataset references that we want to keep in our data, but they cause validation failures that block all edits to affected files, even when fixing unrelated GEO title mismatches.

## Registered Sources (v0.1.4rc5)

From `linkml_reference_validator/etl/sources/__init__.py`:

| Prefix | Handler | Status |
|--------|---------|--------|
| `PMID` | PMIDSource | Working |
| `DOI` | DOISource | Working |
| `GEO` | GEOSource | Working |
| `BIOPROJECT` | BioProjectSource | Exists but Entrez API issues |
| `BIOSAMPLE` | BioSampleSource | Unknown |
| `file` | FileSource | Working |
| `url` | URLSource | Working |
| `NCT` | ClinicalTrialsSource | Working |
| `SRA` | - | **Not implemented** |
| `MGNIFY` | - | **Not implemented** |

## Current Configuration Options

`ReferenceValidationConfig` (from `models.py`):

```python
class ReferenceValidationConfig(BaseModel):
    cache_dir: Path = Path("references_cache")
    reference_base_dir: Optional[Path] = None
    rate_limit_delay: float = 0.5
    email: str = "linkml-reference-validator@example.com"
    supporting_text_regex: Optional[str] = None
    text_group: int = 1
    ref_group: int = 2
    reference_prefix_map: dict[str, str] = {}  # For aliasing, not skipping
```

**Missing**: No option to skip, ignore, or downgrade severity for unsupported prefixes.

Note: `RepairConfig` has `skip_references: list[str]` but this only applies to repair operations, not validation.

## Proposed Solutions

### Option A: `skip_prefixes` configuration

Add a list of prefixes to skip entirely during validation:

```yaml
# .linkml-reference-validator.yaml
validation:
  skip_prefixes:
    - SRA
    - MGNIFY
    - BIOPROJECT
```

These references would be silently skipped with no validation result generated.

### Option B: `unknown_prefix_severity` configuration

Control severity level for references with unknown/unregistered prefixes:

```yaml
# .linkml-reference-validator.yaml
validation:
  unknown_prefix_severity: WARNING  # or ERROR (default), SKIP, INFO
```

This would affect all unknown prefixes uniformly.

### Option C: Per-prefix severity configuration

More granular control:

```yaml
# .linkml-reference-validator.yaml
validation:
  prefix_severity:
    SRA: WARNING
    MGNIFY: SKIP
    BIOPROJECT: WARNING  # Known API issues
```

### Option D: `unfetchable_severity` configuration

Control severity specifically for "could not fetch" errors (distinct from title mismatches):

```yaml
# .linkml-reference-validator.yaml
validation:
  unfetchable_severity: WARNING  # Default: ERROR
```

## Implementation Notes

The change would need to be in:

1. **`models.py`**: Add new config field(s) to `ReferenceValidationConfig`

2. **`supporting_text_validator.py`**: Modify `validate_title()` and `validate()` methods to check config before returning ERROR severity for unfetchable references:

```python
# Current (line 77-85):
if not reference:
    return ValidationResult(
        is_valid=False,
        reference_id=reference_id,
        supporting_text="",
        severity=ValidationSeverity.ERROR,  # Always ERROR
        message=f"Could not fetch reference: {reference_id}",
        path=path,
    )

# Proposed:
if not reference:
    prefix = self._extract_prefix(reference_id)
    severity = self._get_unfetchable_severity(prefix)  # Check config
    if severity == "SKIP":
        return None  # Or ValidationResult with INFO
    return ValidationResult(
        is_valid=severity != ValidationSeverity.WARNING,
        ...
        severity=severity,
        ...
    )
```

3. **CLI**: No changes needed if config is loaded via existing `--config` mechanism

## Workarounds (Current)

1. **Remove unsupported datasets**: Undesirable - loses valuable data
2. **Disable reference validation entirely**: Loses all validation benefits
3. **Custom hook logic**: Adds complexity, not portable, violates separation of concerns

## Impact

Files in `dismech` affected by this issue:
- `Irritable_Bowel_Syndrome.yaml` (bioproject, mgnify)
- `Obesity.yaml` (4x sra)
- `Parkinsons_Disease.yaml` (4x sra)
- `Type_2_Diabetes_Mellitus.yaml` (4x sra)

## Related Issues

- BioProjectSource exists but fails with Entrez DTD parsing error:
  ```
  Failed to fetch Entrez summary for BIOPROJECT:PRJNA566284:
  Failed to find tag 'ERROR' in the DTD.
  ```
  This is a separate bug but would also benefit from configurable severity.

## Recommendation

**Option A (`skip_prefixes`)** is the simplest and most immediately useful. It allows users to explicitly list prefixes that should be ignored, with clear semantics.

Combined with **Option D (`unfetchable_severity`)** as a fallback for unlisted prefixes, this would provide both explicit control and graceful handling of unknown types.

## Example Config

```yaml
# .linkml-reference-validator.yaml
validation:
  cache_dir: references_cache
  skip_prefixes:
    - SRA
    - MGNIFY
  unfetchable_severity: WARNING  # For unlisted prefixes like BIOPROJECT
```

This would:
1. Completely skip SRA and MGNIFY references (no output)
2. Report BIOPROJECT fetch failures as warnings (non-blocking)
3. Still error on title mismatches for supported prefixes (GEO, PMID, etc.)
