# CX2 and NDEx Publishing

This document describes the current `dismech` workflow for exporting disorder pathographs to CX2 and publishing them to NDEx.

## Overview

The CX2 export is built from the same pathograph graph used in the HTML disorder pages. It preserves all pathograph node types, including:

- pathophysiology and other event nodes
- phenotypes
- treatments
- experimental models
- environmental and biochemical nodes
- genetic and variant nodes

The exporter also adds NDEx-oriented metadata:

- disease-level `MONDO` label on the network
- NDEx/iQuery-friendly typing for gene-referencing nodes
- ontology links on event nodes for `CL`, `GO`, `UBERON`, and related terms when present in the source YAML

## Current Commands

Export one disorder to CX2 JSON:

```bash
just export-cx2 kb/disorders/Stargardt_Disease.yaml -o /tmp/Stargardt_Disease.cx2.json
```

Export all disorders to a directory:

```bash
just export-cx2-all -o /tmp/cx2
```

Upload one disorder directly to the NDEx test server:

```bash
just upload-cx2-test kb/disorders/Stargardt_Disease.yaml
```

Upload all disorders directly to the NDEx test server:

```bash
just upload-cx2-test-all
```

## Important Behavior

`just upload-cx2-test` and `just upload-cx2-test-all` do not read previously exported JSON files. They re-run the exporter from the disorder YAML files and upload directly from that fresh CX2 output.

This means:

- run `just export-cx2-all -o /tmp/cx2` only when you want local JSON files for spot-checking
- run `just upload-cx2-test-all` when you want to publish the current exporter output
- you do not need to export first before uploading

Disorders with no pathograph edges are skipped rather than treated as errors.

## NDEx Visibility

The current default upload visibility is `PUBLIC`.

That default applies to:

- `uv run dismech-cx2 ... --ndex-upload`
- `just upload-cx2-test`
- `just upload-cx2-test-all`

To override for a one-off upload:

```bash
just upload-cx2-test kb/disorders/Stargardt_Disease.yaml --visibility PRIVATE
```

## Test Server Host

The `just` upload targets default to:

```bash
https://test.ndexbio.org
```

You can override that host with:

```bash
export NDEX_TEST_HOST=https://test.ndexbio.org
```

The uploader prints a viewer URL on the same host it uploaded to.

## Credentials and Authentication

The current uploader uses NDEx username/password authentication through the `ndex2` Python client. It does not use Google OAuth.

Set credentials in the shell before upload:

```bash
export NDEX_USERNAME=...
export NDEX_PASSWORD=...
```

Important operational notes:

- A browser login via Google does not automatically make the CLI uploader work.
- The NDEx API path used here expects username/password credentials.
- On NDEx, the API username may be the NDEx account name rather than your email address.
- The public NDEx server account and the `test.ndexbio.org` account may be different.

If `test.ndexbio.org` says your user does not exist, that usually means either:

- you used an email address instead of the actual NDEx account name
- or you do not have an account on the test server yet

## What the CX2 Export Adds for NDEx

### Gene-aware iQuery typing

Nodes that reference human gene symbols get extra NDEx-friendly attributes so they can participate in iQuery/gene-centric search:

- direct gene nodes may export as `type=gene`
- descriptive event nodes that reference genes may export as `type=proteinfamily` plus `member=[...]`
- the original dismech semantic category is preserved separately as `dismech_type`

This keeps all pathograph nodes while still exposing the small gene-relevant subset in the form NDEx expects.

### Ontology links on event nodes

Event/pathophysiology nodes now expose linked ontology context when present in the YAML:

- `cell_type_ids`, `cell_type_urls`, `cell_type_links`
- `biological_process_ids`, `biological_process_urls`, `biological_process_links`
- `molecular_function_ids`, `molecular_function_urls`, `molecular_function_links`
- `location_ids`, `location_urls`, `location_links`

This is intended to make NDEx tables and property panels more useful without changing the visible node labels.

## Recommended Workflow

For a quick JSON check:

```bash
just export-cx2 kb/disorders/Stargardt_Disease.yaml -o /tmp/Stargardt_Disease.cx2.json
```

For a full publication pass to the NDEx test server:

```bash
export NDEX_USERNAME=...
export NDEX_PASSWORD=...
just upload-cx2-test-all
```

For debugging a failed upload, first try a single disorder:

```bash
just upload-cx2-test kb/disorders/Stargardt_Disease.yaml
```

## Notes on Re-runs

Uploads create new networks. Re-running the same bulk upload will create duplicates unless you manually delete or replace the previous networks on NDEx.

The uploader makes a best-effort attempt to set NDEx `index_level=META` after upload. If that post-upload call fails on the test server, the network upload itself is still treated as successful.
