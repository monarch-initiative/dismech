---
provider: codex
model: gpt-5.4
cached: false
start_time: '2026-04-13T05:52:00Z'
end_time: '2026-04-13T05:58:00Z'
duration_seconds: 360
citation_count: 13
---

## Output

# Malignant Peritoneal Mesothelioma Research Notes

## Scope

This research note supports a disease-level dismech curation for malignant peritoneal mesothelioma (MPeM), anchored to `MONDO:0005512`. The entry is modeled as a single mechanism-graph unit, with subtype axes used for histology, molecular context, and inherited predisposition context rather than as separate dismech pages.

## Disease Identity

MPeM is a rare aggressive mesothelial malignancy arising from the peritoneal lining. Compared with pleural mesothelioma, asbestos attribution is less consistent, while the disease remains strongly defined by locoregional intraperitoneal progression and a BAP1-dominant genomic landscape (PMID:27813512, PMID:32206577, PMID:35704798, PMID:36138075).

NCIT provides a useful exact disease mapping at the cancer-modeling level:

- `NCIT:C9350` Peritoneal Malignant Mesothelioma

## Core Mechanistic Program

### 1. BAP1 tumor suppressor loss is the dominant recurrent driver

Multiple genomic series converge on BAP1 as the most frequent recurrent alteration in MPeM. In a targeted sequencing cohort, "The most frequent genetic alteration was biallelic inactivation of the BAP1 gene" (PMID:27813512). In an independent series, "Overall, 73% of the malignant peritoneal mesotheliomas analyzed carried at least one inactivated BAP1 allele" (PMID:28034829). This supports a core atomic mechanism node centered on BAP1 tumor suppressor inactivation rather than a generic omnibus "genomic instability" node.

### 2. Chromatin and epigenetic control are recurrently disrupted

MPeM is enriched for alterations affecting chromatin-associated regulators including `BAP1`, `SETD2`, `DDX3X`, and in larger profiling studies `PBRM1` (PMID:27813512, PMID:35704798). The most useful disease-graph abstraction is an atomic chromatin/epigenetic dysregulation node downstream of BAP1 loss rather than a bundled multi-pathway node.

### 3. PI3K-AKT-mTOR signaling contributes to the malignant proliferative state

Review synthesis specific to diffuse malignant peritoneal mesothelioma states that "The overexpression of the phosphatidylinositol 3-kinase (PI3K)/AKT ... /mTOR signaling pathway drives the malignant phenotype of DMPM" (PMID:36684194). This supports a separate proliferative signaling node rather than collapsing signaling and proliferation into one step.

### 4. Clinical morbidity is driven by locoregional peritoneal expansion

MPeM morbidity is dominated by local abdominal progression. A concise disease-defining quote is: "Morbidity and mortality of the disease are related to progressive locoregional effects within the abdominal cavity" (PMID:32206577). This justifies a downstream node for locoregional peritoneal tumor expansion that explains major abdominal phenotypes.

## Subtype Axes Used for Modeling

### Histologic axis

Histology is the most important subtype axis and should remain flat rather than generating separate disease pages.

- `NCIT:C162940` Peritoneal Epithelioid Mesothelioma
- `NCIT:C168805` Peritoneal Biphasic Mesothelioma
- `NCIT:C168804` Peritoneal Sarcomatoid Mesothelioma

Large profiling data distinguish epithelioid from nonepithelioid tumors, with biphasic and sarcomatoid grouped together molecularly and clinically (PMID:35704798). Outcome data also support epithelioid histology and absence of necrosis as favorable features (PMID:33060816).

### Molecular axis

`ALK` rearrangement is a rare but important molecular subtype axis. The key quote is: "ALK rearrangements were only observed in MPeM" (PMID:35704798). This is better modeled as a molecular subtype facet than as a separate disease page.

### Predisposition-context axis

Inherited `BAP1` predisposition is a host-context subtype axis rather than a distinct peritoneal mesothelioma disease entity. A relevant grounding term is:

- `MONDO:0013692` BAP1-related tumor predisposition syndrome

Case-based evidence directly links this syndrome to peritoneal mesothelioma susceptibility (PMID:30001711).

## Histopathology and Biomarkers

Useful pathology-layer features for disease-level curation include:

- Epithelioid histotype as the favorable histologic pattern (PMID:33060816)
- Composite nuclear grade as a validated prognostic feature in epithelioid disease (PMID:33060816)
- Tumor necrosis as an adverse feature (PMID:33060816)
- Loss of nuclear `BAP1` staining as a malignancy-supporting diagnostic biomarker (PMID:27813512, PMID:36684194)
- `WT1` positivity as part of the sensitive immunohistochemical panel for peritoneal mesothelioma (PMID:36684194)

## Phenotype Layer

The dominant phenotype set is abdominal and locoregional rather than systemic-metastatic:

- Ascites (PMID:22104079, PMID:36059360)
- Abdominal pain (PMID:22104079, PMID:36059360)
- Abdominal distention (PMID:32206577, PMID:36059360)
- Early satiety (PMID:32206577)
- Intestinal obstruction (PMID:32206577)
- Weight loss (PMID:22104079)

## Treatment Implications

The clearest treatment program for resectable disease is cytoreductive surgery plus HIPEC. Review and consensus support are consistent:

- "The standard of care for patients with resectable disease remains cytoreductive surgery and hyperthermic intraperitoneal chemotherapy (CRS-HIPEC)" (PMID:32206577)
- "The panel unanimously recommended CRS-HIPEC" for a carefully selected subset of DMPM patients (PMID:39609952)

For unresectable or previously treated disease, the structured entry should preserve systemic options with exact supporting studies:

- Pemetrexed plus cisplatin showed meaningful disease control in first-line treatment (PMID:28594258)
- Atezolizumab plus bevacizumab demonstrated activity in advanced previously treated MPeM (PMID:34261675)

## Curation Takeaways

- Keep the page at the disease level for `MONDO:0005512`.
- Use NCIT mappings routinely for cancer-specific disease and histologic subtype grounding.
- Treat histology, molecular status, and predisposition context as flat subtype axes.
- Keep pathophysiology nodes atomic: BAP1 loss, chromatin dysregulation, PI3K-AKT-mTOR activation, transformed mesothelial proliferation, and locoregional abdominal expansion.
- Avoid creating separate dismech pages for epithelioid, biphasic, sarcomatoid, ALK-rearranged, or BAP1-predisposition-context cases unless future evidence shows a genuinely distinct causal program.
