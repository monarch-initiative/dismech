# Computable phenotypes

A computable phenotype (CP) is an algorithm that finds patients with a disease
in electronic health records: code lists, counts, time windows and the logic
that combines them. dismech records a CP as a `definitions[]` entry with
`definition_type: PHENOTYPE_ALGORITHM`, on the disorder it identifies.

This page covers the slots a CP needs beyond a diagnostic-criteria definition,
the two phenotype libraries that can be cited directly (PheKB and the HDR UK
Phenotype Library), and the check that keeps transcribed code lists honest.
Worked examples: `Sickle_Cell_Disease` (PheKB 615, HDR UK PH304 and PH3021)
and `Systemic_Lupus_Erythematosus` (PheKB 1058, HDR UK PH3024).

## Slots

| Slot | On | Says |
|---|---|---|
| `source_reference` | `Definition`, `CodeList` | The library record the definition or list was transcribed from (`PHEKB:615`, `HDRUK:PH304`). A reference CURIE with a `references_cache/` entry. |
| `criteria_set_logic` | `Definition` | `ALL_OF` or `ANY_OF`: how the `criteria_sets` combine. Omit it when the source does not say. |
| `minimum_required` | `CriteriaSet` | How many items in a set must hold (existing slot). |
| `code_lists` | `CriteriaItem` | The codes that satisfy the criterion. A record matches if it carries any code in any list. |
| `minimum_occurrences` | `CriteriaItem` | Distinct qualifying records needed, e.g. 3 for "3 or more counts of 710.0". |
| `minimum_interval_days` | `CriteriaItem` | Days between first and last qualifying record, e.g. 30 for "two visits at least 30 days apart". |

A `CodeList` has a `code_system` (`CodeSystemEnum`: `ICD9CM`, `ICD10`,
`ICD10CM`, `SNOMEDCT`, `READ2`, `CTV3`, `OPCS4`, `LOINC`, `RXNORM`), an
optional `code_system_version`, a `source_reference`, and `codes`, each an
`{id, label}` term whose id is `<code_system>:<code>`.

Rules for filling them:

- **Copy every code and its label from the source.** The label is the
  source's own description, not the code system's preferred name and not a
  tidied version. `just check-codelists` fails a label that differs from the
  cited record.
- **`ICD10` is WHO ICD-10, not ICD-10-CM.** UK records use WHO ICD-10, and the
  two systems label the same code differently (`D57.0` is "Sickle-cell anaemia
  with crisis" in one and "Hb-SS disease with crisis" in the other).
- **Record what the source states, and no more.** A count, interval or
  set-combination rule goes in its slot only when the source gives it. If the
  source leaves it implicit, describe it in `description` and leave the slot
  absent.
- **Validation status needs evidence.** `VALIDATED_AGAINST_GOLD_STANDARD`
  cites the validation study (PPV, sensitivity) through
  `validation_status.evidence`. A library record with no validation section
  gets no `validation_status`.
- **Codes the KB cannot name are left out and said so in `notes`.** CPRD
  medcodes, dm+d and BNF have no `CodeSystemEnum` value.

## Citing a library record

Both libraries are structured-source prefixes: the record is cached under
`references_cache/` and its rows can be quoted as evidence.

```bash
just fetch-reference HDRUK:PH304     # references_cache/HDRUK_PH304.md
just fetch-reference PHEKB:615       # references_cache/PHEKB_615.md
```

- **HDR UK** (`HDRUK:PH<n>`) is read from the library's public API. The cache
  holds the record metadata (including the library's own MONDO tag), the
  free-text definition, and one `| <CURIE> | <description> | <concept> |` row
  per code from the resolved code export. Library content is CC BY-SA 4.0 for
  non-commercial use. Some records state their own licence in the definition
  text, for example OpenSAFELY codelists drawn from NHS Digital refsets under
  the Open Government Licence.
- **PheKB** (`PHEKB:<node>`) is read from the phenotype page, because PheKB
  has no API. The cache holds the page's metadata and description, and the
  extracted text of each PDF attachment that is an algorithm document. A PDF
  whose first page carries a DOI is a published article: it is listed but not
  transcribed, and is cited by its PMID instead. Word, SQL and spreadsheet
  attachments are listed only. PheKB states no licence for its content.

## Converting an HDR UK record

```bash
just hdruk-definition PH304 PH3021    # prints a definitions: fragment, caches the records
```

The converter writes the fragment below. It is a draft for a curator to
finish, not finished content.

- One criteria set, "Qualifying codes", with one item per library concept.
  Each item has a code list copied code by code from the resolved export.
- One evidence item quoting the first sentence of the library's definition.
- `notes` with the record URL, the library's ontology tag, any dropped coding
  systems, and whether the record has a validation section.

Before committing, read the library's definition. Where it combines concepts
in some other way than "any code qualifies", restructure the fragment. Check
that the library's MONDO tag matches the entry's `disease_term`. Then run
`just validate` on the entry.

To write into an entry instead of printing:

```bash
just hdruk-definition PH304 --disorder kb/disorders/Sickle_Cell_Disease.yaml \
  --exclude-code-system SNOMEDCT
```

- `--disorder` appends to the entry's `definitions:` block, or adds one at
  the end of the file. Nothing else in the file changes, and the command
  refuses to write if the result would parse differently anywhere else. A
  record the entry already cites (by `source_reference`) is not added again,
  so a re-run is a no-op.
- A record is skipped, with a `SKIP` line on stderr, when its own MONDO tag
  names a different disease from the entry's `disease_term`, or when none of
  its codes has a dismech code system (for example, every code is a CPRD
  medcode or an omitted SNOMED CT code). A record with no MONDO tag is not
  refused; matching it is the curator's call.
- `--exclude-code-system` leaves every code of that system out of both the
  definition and the cached record, and both say how many were left out.
  SNOMED CT codes are excluded from bulk imports until the redistribution
  question in design decision §20 is settled. The codes remain in the library
  record, so they can be added later by re-running without the option.
- Re-fetching an omitted record with `just fetch-reference HDRUK:<id>` writes
  the full code list back into the cache, because that path omits nothing.

## Checking code lists

```bash
just check-codelists                                  # every kb/ file with a code list
just check-codelists kb/disorders/Sickle_Cell_Disease.yaml
```

`codes` is not bound to an ontology enum, so `just validate-terms` never sees
these codes. This check is the gate instead, and it runs in `just qc` and as
an ungated CI step. It fails when any of these is true:

- a code's prefix is not its list's `code_system`;
- a code is malformed for its system (e.g. `ICD9CM:2824`);
- the list's `source_reference` is not cached;
- a code and its label do not appear together in the cited record. HDR UK
  needs the exact `| <CURIE> | <label> |` row. PheKB and other text sources
  need `<code> <label>` in the body.

ICD-10-CM labels are also compared with `cache/icd10cm/terms.csv` where a row
exists. ICD-9-CM, WHO ICD-10, SNOMED CT and Read codes have no vocabulary
adapter in `conf/oak_config.yaml`. For those, the check confirms syntax and
agreement with the cited source, not membership in the vocabulary.
