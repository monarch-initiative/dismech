# Publisher literature supplements

These are transcriptions of published supplementary documents, not authored
research reports. The manifest records each article identifier, publisher URL,
DOCX filename, SHA-256 checksum and generated text filename.

Regenerate the visible text with:

```sh
uv run python scripts/extract_literature_supplements.py
```

For offline reproduction, download the publisher files under the manifest's
`filename` values and pass `--source-dir /path/to/downloads`. Both routes check
the same document checksums before writing anything. Word/EndNote field
instructions are omitted; displayed text and table-cell paragraphs retain their
document order. The extraction test checks this distinction.

The reference validator supports `file:` sources. A KB entry cites one by its
path relative to the repository root, e.g.
`reference: file:data/literature_supplements/CRADD_Polla_2019_Supplement.extracted.md`.

Since linkml-reference-validator 0.8.0 the validator reads a `file:` source
directly on every run and writes **no** copy to `references_cache/`
(linkml/linkml-reference-validator#173). Do not generate one: the extracted text
here is already the committed source, and a cache copy would only duplicate it
and drift from it. `just count-verified-snippets` reads the file the same way.
The relative path resolves against the working directory (the validator's
`reference_base_dir` default), so run the `just` recipes from the checkout root.

No validation settings are weakened. The extracted source and manifest travel
together so the quotations remain verifiable without publisher network access.
Do not edit generated source text by hand.
