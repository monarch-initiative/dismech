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

The reference validator supports `file:` sources. Generate their caches through
its normal CLI, using the repository root as the relative source base:

```sh
uv run python - <<'PY'
from pathlib import Path
import subprocess
import tempfile
import yaml

config = yaml.safe_load(Path('conf/reference_validator_config.yaml').read_text())
config['reference_base_dir'] = '.'
manifest = yaml.safe_load(Path('data/literature_supplements/manifest.yaml').read_text())
with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml') as stream:
    yaml.safe_dump(config, stream)
    stream.flush()
    for record in manifest['supplements']:
        ref = 'file:data/literature_supplements/' + record['output']
        subprocess.run([
            'scripts/run_reference_validator.sh', 'cache', 'reference', ref,
            '--force', '--config', stream.name,
        ], check=True)
PY
```

No validation settings are weakened. The extracted source, manifest and generated
cache travel together so the quotations remain verifiable without publisher
network access. Do not edit generated source text or reference caches by hand.
