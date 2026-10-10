# Noggin dose-response in the S-ONTX34 neural tube closure model

Scripts that run and score the published agent-based model of neural tube
closure (Berkhout et al. 2025, PMID:40034255; BioStudies
[S-ONTX34](https://www.ebi.ac.uk/biostudies/ontox/studies/S-ONTX34)) at partial
Noggin (NOG) expression levels. They test the
`bmp_antagonism_dlhp_failure` hypothesis in
`kb/disorders/Spina_Bifida_Cystica.yaml`: that loss of BMP antagonism at the
dorsolateral hinge points leads to failed posterior neural tube closure.

No simulation results are committed here yet. The batch needs about 45
CPU-hours, which is more than an OpenScientist job or a cloud agent session
gets (see issue #13616), so it is set up to run on a workstation or cluster.

## What the deposited runs already show

The authors deposited 20 runs each of control, NOG knockout (level 0) and NOG
at twice wild-type expression (level 2.0; 18 runs). Scored with
`scripts/classify.py`:

| Condition | n | normal | midline fusion | open NTD | closed NTD |
|---|---|---|---|---|---|
| Control | 20 | 20 | 0 | 0 | 0 |
| NOG 0 (knockout) | 20 | 11 | 9 | 0 | 0 |
| NOG 2.0 | 18 | 1 | 1 | 1 | 15 |

The model's NOG knockout gives no open neural tube defect, while Noggin-null
mice have lumbar spina bifida (PMID:16712836). The dose-response asks whether
partial loss (0.25, 0.5, 0.75) behaves like the knockout, like control, or
does something in between. That decides whether the knockout result is a
threshold effect or a structural limit of the model.

## The scorer and how far to trust it

The authors scored outcomes by eye. `classify.py` scores a run's final frame
from the cell-type lattice with three measurements: whether the surface
ectoderm is one continuous sheet, the area of the enclosed lumen, and the size
of the dorsal gap in the neural tissue. Its docstring gives the rules.

`validate_classifier.py` compares it with the authors' own labels, which are
typed into their `Create_NTD_prob_graphs_fig4.py`. On control and NOG knockout
it agrees on 39 of 40 runs: one control run the authors called midline fusion
is scored normal. The authors did not label the NOG 2.0 runs. Across all nine
genes it agrees on 273 of 340, because the authors' "midline fusion" calls for
the SHH, GLI and PTCH1 knockouts include runs with an open lumen. Use it on the
NOG axis only.

## Running the batch

Run these from this directory (`analyses/ntc_abm`).

1. Download and unpack the model (66 KB):

   ```bash
   curl -LO https://ftp.ebi.ac.uk/biostudies/fire/S-ONTX/034/S-ONTX34/Files/WP7-9files/WP9/NTC_model/cNTC_Model.zip
   unzip cNTC_Model.zip
   MODEL=$PWD/cNTC_Model/Invitro_NTC_2D_main
   ```

2. Install CompuCell3D 4.6.0 (conda, mamba or micromamba):

   ```bash
   micromamba create -n cc3d -c compucell3d -c conda-forge python=3.10 compucell3d=4.6.0
   export CC3D_PYTHON=$(micromamba run -n cc3d which python)
   ```

3. Run the queue. Each line of `queue.txt` is `CONDITION GENE LEVEL
   REPLICATE`: 10 replicates at each of NOG 0.25, 0.5 and 0.75, plus 4 control
   replicates to check that this installation reproduces the deposited
   controls. With four processes:

   ```bash
   WORK=$PWD/ntc_runs
   xargs -P 4 -L 1 sh -c 'python3 scripts/simulate.py "$0" "$1" "$2" "$3" "$4" "$5"' "$MODEL" "$WORK" < queue.txt
   ```

   `simulate.py` uses only the standard library, so any Python 3.9+ can run
   it. A run takes about 77 minutes on one core (12,000 Monte Carlo steps at
   about 2.6 per second), so 34 runs take about 11 hours on four cores. A
   finished run leaves a `DONE` marker and is skipped if the command is run
   again, so an interrupted batch picks up where it stopped.

   On a SLURM cluster, one array task per queue line:

   ```bash
   #SBATCH --array=1-34
   #SBATCH --cpus-per-task=1
   #SBATCH --time=03:00:00
   set -- $(sed -n "${SLURM_ARRAY_TASK_ID}p" queue.txt)
   python3 scripts/simulate.py "$MODEL" "$WORK" "$1" "$2" "$3" "$4"
   ```

4. Score the runs. This needs numpy, scipy and matplotlib; the `cc3d`
   environment has the first two:

   ```bash
   micromamba install -n cc3d -c conda-forge matplotlib
   $CC3D_PYTHON scripts/classify.py "$WORK" outcomes.csv
   ```

## What to send back

`outcomes.csv` and the printed table, or the `run.json` files plus each run's
final frame (`*_celldata/12000_cell_data.pkl`, about 1 MB each) if you would
rather the scoring were redone. Those go into a hypothesis analysis bundle
under `kb/hypotheses/Spina_Bifida_Cystica/` with a manifest and replay record,
as described in `docs/hypothesis-report-assessments.md`.

## Checking the scorer yourself

`fetch_zip_members.py` pulls only the 377 final frames (about 370 MB) out of the
5.7 GB deposited `Model_generated_data.zip`, using HTTP range requests:

```bash
python3 scripts/fetch_zip_members.py \
  https://ftp.ebi.ac.uk/biostudies/fire/S-ONTX/034/S-ONTX34/Files/WP7-9files/WP9/NTC_model/Model_generated_data.zip \
  '_celldata/12000_cell_data\.pkl$' deposited/
curl -LO https://ftp.ebi.ac.uk/biostudies/fire/S-ONTX/034/S-ONTX34/Files/WP7-9files/WP9/NTC_model/Analysis_scripts.zip
unzip Analysis_scripts.zip
$CC3D_PYTHON scripts/validate_classifier.py deposited/Model_generated_data \
  Analysis_scripts/Create_NTD_prob_graphs_fig4.py validation.csv
$CC3D_PYTHON scripts/render.py nog_ko.png "NOG knockout" deposited/Model_generated_data/NOG/NOG_0/celldata/*/12000_cell_data.pkl
```

## Model details that matter here

- Gene expression is set per run in `Simulation/parameters.py`,
  `gene_status_dict`: 1.0 is wild type, 0 a knockout, 2.0 the authors'
  hyperactivation. `simulate.py` changes only that entry and the output path.
- `ATRA` in that dictionary is never read by the model code (retinoic acid
  follows a fixed time ramp), so changing it does nothing.
- Cell types: 5-7 medial hinge point, 8-13 neural plate, 14 and 15 left and
  right surface ectoderm, 17 ECM, 19-22 neural crest. The notochord is not
  written to the cell data files.
