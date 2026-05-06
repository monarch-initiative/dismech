# Basal Cell Carcinoma Research Synthesis

## Provider Coverage

- Falcon: `Basal_Cell_Carcinoma-deep-research-falcon.md`
- OpenScientist: `Basal_Cell_Carcinoma-deep-research-openscientist.md`

## Agreement

Both providers identify Hedgehog pathway activation as the central mechanism of basal cell carcinoma, usually through PTCH1 loss of function or SMO activation, followed by GLI transcriptional activation and basal-cell proliferation. They agree that ultraviolet radiation is the dominant environmental risk factor, that BCC is usually locally invasive rather than metastatic, and that most routine disease is managed surgically.

Both reports also agree on key therapeutic categories: Mohs or standard excision for localized disease, Hedgehog pathway inhibitors for locally advanced or metastatic disease, topical therapies and photodynamic therapy for selected superficial lesions, and PD-1 blockade after Hedgehog inhibitor failure.

## Differences

Falcon emphasized guideline-facing clinical management, recurrence benchmarks, systemic photoprotection, and NCCN-style treatment placement. OpenScientist added broader pathway context including Wnt/beta-catenin, TP53, PI3K/AKT/mTOR, immune microenvironment, dermoscopy, imaging, AI-assisted diagnosis, and animal/model-system information.

## YAML Integration

Integrated into `kb/disorders/Basal_Cell_Carcinoma.yaml`:

- Confirmed that the core PTCH1/SMO/Hedgehog/GLI cascade is already represented.
- Confirmed subtype, clinical phenotype, UV exposure, PTCH1, SMO, TP53, SUFU, surgery, Hedgehog inhibitors, topical therapy, photodynamic therapy, radiation, and immune checkpoint inhibitor content.
- Backfilled top-level references with `found_in` provenance for Falcon and OpenScientist citation trails.

## Not Integrated

Nicotinamide chemoprevention was left as provenance rather than promoted to treatment because the cited evidence is mixed and partly oriented toward broader non-melanoma skin cancer or squamous-cell prevention. Detailed dermoscopy patterns, AI diagnostic tooling, and model-organism variants were also left in research provenance.
