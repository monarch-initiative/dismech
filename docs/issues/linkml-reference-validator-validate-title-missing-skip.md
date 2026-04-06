# Bug: validate_title() missing skip_prefixes logic (rc6)

## Summary

In `linkml-reference-validator` v0.1.4rc6, the `skip_prefixes` configuration is implemented in `validate()` but **not** in `validate_title()`. This means title-only validation (e.g., dataset title validation) still fails with ERROR for skipped prefixes.

## Affected Version

- `linkml-reference-validator==0.1.4rc6`

## Root Cause

In `validation/supporting_text_validator.py`:

### `validate()` - Has skip logic (lines 148-160):
```python
def validate(self, supporting_text: str, reference_id: str, ...):
    # Check if this prefix should be skipped
    prefix = reference_id.split(":")[0].upper() if ":" in reference_id else ""
    skip_prefixes_upper = [p.upper() for p in self.config.skip_prefixes]

    if prefix and prefix in skip_prefixes_upper:
        return ValidationResult(
            is_valid=True,
            severity=ValidationSeverity.INFO,
            message=f"Skipping validation for reference with prefix '{prefix}': {reference_id}",
            ...
        )
    # ... rest of validation
```

### `validate_title()` - Missing skip logic (lines 50-85):
```python
def validate_title(self, reference_id: str, expected_title: str, ...):
    reference = self.fetcher.fetch(reference_id)  # No skip check before this

    if not reference:
        return ValidationResult(
            is_valid=False,
            severity=ValidationSeverity.ERROR,  # Hardcoded ERROR
            message=f"Could not fetch reference: {reference_id}",
            ...
        )
```

## Impact

When validating data with title fields but no excerpt fields (e.g., dataset entries), the plugin calls `validate_title()` directly. This bypasses the `skip_prefixes` check, causing:

```
[ERROR] Could not fetch reference: sra:PRJNA290729
[ERROR] Could not fetch reference: mgnify:MGYS00000596
[ERROR] Could not fetch reference: bioproject:PRJNA566284
```

Even with this config:
```yaml
skip_prefixes:
  - SRA
  - MGNIFY
  - BIOPROJECT
```

## Fix Required

Add the same skip logic to `validate_title()`:

```python
def validate_title(self, reference_id: str, expected_title: str, ...):
    # Check if this prefix should be skipped
    prefix = reference_id.split(":")[0].upper() if ":" in reference_id else ""
    skip_prefixes_upper = [p.upper() for p in self.config.skip_prefixes]

    if prefix and prefix in skip_prefixes_upper:
        return ValidationResult(
            is_valid=True,
            reference_id=reference_id,
            supporting_text="",
            severity=ValidationSeverity.INFO,
            message=f"Skipping title validation for reference with prefix '{prefix}': {reference_id}",
            path=path,
        )

    reference = self.fetcher.fetch(reference_id)
    # ... rest of method
```

Also apply `unknown_prefix_severity` config to the "could not fetch" case (line 82).

## Workaround

Comment out the `title:` field for datasets with unsupported prefixes. The user has done this for mgnify entries:

```yaml
- accession: mgnify:MGYS00000596
  # title: American Gut Project IBS microbiome analysis  # Commented out
  description: >-
    ...
```

## Related

- GitHub Issue: https://github.com/linkml/linkml-reference-validator/issues/28
