"""Enumerate YAML inputs before running bounded LinkML validation batches.

Exit 1 for validation failures; exit 2 for enumeration or process-launch errors.
Used by validate-history-all and validate-schema-all so corpus growth never
expands the recipe command line. LinkML still owns all validation semantics.
"""

import argparse
import os
from pathlib import Path
import stat
import subprocess
import sys


# Leave ample room for the environment and fixed arguments on macOS.
MAX_PATH_BYTES = 32 * 1024
MAX_FILES = 100


def batches(files):
    batch = []
    size = 0
    for path in files:
        cost = len(os.fsencode(path)) + 1
        if batch and (len(batch) >= MAX_FILES or size + cost > MAX_PATH_BYTES):
            yield batch
            batch, size = [], 0
        batch.append(path)
        size += cost
    if batch:
        yield batch


def enumerate_files(root, history):
    """Do not silently accept an incomplete walk when a directory is unreadable."""

    def raise_error(error):
        raise error

    # stat distinguishes a missing root from permissions and other I/O failures.
    if not stat.S_ISDIR(root.stat().st_mode):
        raise NotADirectoryError(str(root))
    return sorted(
        str(Path(directory) / name)
        for directory, _, names in os.walk(root, onerror=raise_error)
        for name in names
        if name.endswith(".yaml")
        and (history or not name.endswith(".history.yaml"))
        and (Path(directory) / name).is_file()
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=["history", "disorders"])
    parser.add_argument("root", type=Path)
    parser.add_argument("schema")
    args = parser.parse_args(argv)
    history = args.kind == "history"
    try:
        files = enumerate_files(args.root, history)
    except FileNotFoundError as error:
        if history and error.filename == str(args.root):
            print("No history directory found.")
            return 0
        print(f"Cannot enumerate {args.kind} YAML files: {error}", file=sys.stderr)
        return 2
    except OSError as error:
        print(f"Cannot enumerate {args.kind} YAML files: {error}", file=sys.stderr)
        return 2
    if not files:
        if history:
            print(f"No history YAML files found in {args.root}.")
            return 0
        print(
            f"No disorder YAML files found in {args.root} (after excluding *.history.yaml)."
        )
        return 1
    if history:
        print(f"Validating {len(files)} history record(s).", flush=True)
    else:
        print(f"Validating {len(files)} disorder files (schema)...", flush=True)
    command = [
        "linkml-validate",
        "--schema",
        args.schema,
        "--target-class",
        "HistoryRecord" if history else "Disease",
    ]
    failed = False
    for number, batch in enumerate(batches(files), 1):
        print(
            f"Batch {number}: {len(batch)} files ({batch[0]} through {batch[-1]})",
            flush=True,
        )
        try:
            result = subprocess.run([*command, *batch], check=False)
        except OSError as error:
            print(f"Cannot launch validation batch {number}: {error}", file=sys.stderr)
            return 2
        if result.returncode:
            failed = True
            print(
                f"Validation batch {number} failed (exit {result.returncode}); inputs:",
                file=sys.stderr,
            )
            for path in batch:
                print(f"  {path}", file=sys.stderr)
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
