"""Run replicates of the S-ONTX34 neural tube closure model at one gene expression level.

Each replicate gets its own copy of the model directory. Only two lines of
``Simulation/parameters.py`` change: ``cell_data_dir`` (so replicates do not
write into each other's output) and the gene's entry in ``gene_status_dict``
(1.0 is wild type, 0 a knockout, 2.0 the authors' hyperactivation level).

A finished replicate leaves a ``DONE`` marker and is skipped on a rerun, so an
interrupted batch can be restarted with the same command.

Usage:
    simulate.py MODEL_DIR WORK_DIR CONDITION GENE LEVEL REPLICATE [REPLICATE ...]

MODEL_DIR is ``cNTC_Model/Invitro_NTC_2D_main`` from the deposited
``cNTC_Model.zip``. The CompuCell3D interpreter is taken from ``--cc3d-python``,
then ``$CC3D_PYTHON``, then the interpreter running this script.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path


def configure(params: Path, celldata: Path, gene: str, level: float) -> None:
    text = params.read_text()
    text, n_dir = re.subn(
        r'cell_data_dir = r".*"', f'cell_data_dir = r"{celldata}"', text
    )
    text, n_gene = re.subn(rf'"{re.escape(gene)}": 1\.0', f'"{gene}": {level}', text)
    if n_dir != 1 or n_gene != 1:
        raise SystemExit(
            f"{params}: expected one cell_data_dir and one '\"{gene}\": 1.0' line, "
            f"found {n_dir} and {n_gene}"
        )
    params.write_text(text)


def run_replicate(args: argparse.Namespace, rep: int) -> None:
    run_dir = (args.work_dir / args.condition / f"rep{rep:02d}").resolve()
    if (run_dir / "DONE").exists():
        print(f"skip {run_dir} (done)")
        return
    shutil.rmtree(run_dir, ignore_errors=True)
    shutil.copytree(
        args.model_dir,
        run_dir / "model",
        ignore=shutil.ignore_patterns("__pycache__", "screenshot_data"),
    )
    configure(
        run_dir / "model/Simulation/parameters.py",
        run_dir / "celldata",
        args.gene,
        args.level,
    )
    started = time.time()
    with (run_dir / "cc3d.log").open("w") as log:
        returncode = subprocess.run(
            [
                args.cc3d_python,
                "-m",
                "cc3d.run_script",
                "--input",
                str(run_dir / "model/Invitro_NTC_2D.cc3d"),
                "--output-dir",
                str(run_dir / "cc3d_out"),
            ],
            stdout=log,
            stderr=subprocess.STDOUT,
            env={**os.environ, "QT_QPA_PLATFORM": "offscreen"},
            check=False,
        ).returncode
    record = {
        "condition": args.condition,
        "gene": args.gene,
        "level": args.level,
        "replicate": rep,
        "returncode": returncode,
        "runtime_s": round(time.time() - started, 1),
    }
    (run_dir / "run.json").write_text(json.dumps(record) + "\n")
    if returncode == 0:
        (run_dir / "DONE").touch()
    print(f"{'ok' if returncode == 0 else 'FAILED'} {run_dir} {record['runtime_s']}s")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("model_dir", type=Path)
    parser.add_argument("work_dir", type=Path)
    parser.add_argument("condition", help="output folder name, e.g. NOG_0.5 or control")
    parser.add_argument("gene", help="key in gene_status_dict, e.g. NOG")
    parser.add_argument("level", type=float)
    parser.add_argument("replicates", type=int, nargs="+")
    parser.add_argument(
        "--cc3d-python",
        default=os.environ.get("CC3D_PYTHON", sys.executable),
        help="Python interpreter with CompuCell3D 4.6.0 installed",
    )
    args = parser.parse_args()
    for rep in args.replicates:
        run_replicate(args, rep)


if __name__ == "__main__":
    main()
