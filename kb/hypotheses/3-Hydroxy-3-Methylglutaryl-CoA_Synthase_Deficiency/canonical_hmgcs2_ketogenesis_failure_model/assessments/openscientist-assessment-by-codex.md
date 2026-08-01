# Assessment of the OpenScientist HMGCS2 report

**Provider:** OpenScientist  
**Assessor:** Codex  
**Source:** `../openscientist.md`  
**Verdict:** **SUPPORTED**

## Bottom line

The report gets the central disease mechanism right. Biallelic HMGCS2
dysfunction impairs the rate-limiting mitochondrial step of hepatic ketogenesis,
and catabolic stress can then precipitate inadequate ketone production and acute
metabolic decompensation. Variant-expression experiments, human cohorts, and
Hmgcs2 knockout models converge on that conclusion
([PMID:32952630](https://pubmed.ncbi.nlm.nih.gov/32952630/);
[PMID:39798988](https://pubmed.ncbi.nlm.nih.gov/39798988/);
[PMID:40515583](https://pubmed.ncbi.nlm.nih.gov/40515583/)).

The report is less reliable when it counts patients and database records,
generalizes selected cohort proportions, or moves from mouse physiology to
human modifiers and treatment proposals. It also contains two clear
source-search failures: ClinGen curated this relationship as definitive in
2018, and an older study assayed a patient's liver.

## What should be retained

### The canonical catalytic bottleneck

PMID:32952630 functionally tested five patient variants in expression systems:
three purified mutant proteins had no residual activity, one retained partial
activity, and another was unstable in transfected cells. The clinical reviews
confirm an autosomal-recessive disorder of ketogenesis with acute
decompensation, commonly after poor intake or illness. The canonical status is
well justified.

### Hypoglycemia is common, not required

The Vietnamese cohort observed hypoglycemia in 9 of 16 symptomatic patients
during the **first** acute presentation
([PMID:40004108](https://pubmed.ncbi.nlm.nih.gov/40004108/)). A
normoglycemic crisis and a single severe-hyperglycemia presentation are also
reported
([PMID:32905056](https://pubmed.ncbi.nlm.nih.gov/32905056/);
[PMID:40937626](https://pubmed.ncbi.nlm.nih.gov/40937626/)). This supports the
report's qualitative correction, but not its statement that roughly 56% of all
acute episodes include hypoglycemia.

### Mouse downstream mechanisms are valuable leads

Global neonatal knockout produced acetyl-CoA accumulation and mitochondrial
protein hyperacetylation
([PMID:33619377](https://pubmed.ncbi.nlm.nih.gov/33619377/)).
Liver-specific models support steatosis and an ACSL1-mediated
re-esterification route
([PMID:35421611](https://pubmed.ncbi.nlm.nih.gov/35421611/);
[PMID:40692014](https://pubmed.ncbi.nlm.nih.gov/40692014/)). These are
plausible extensions of HMGCS2D, but the cited human data concern
metabolic-steatohepatitis rather than biallelic HMGCS2 deficiency. No cited
patient study measures hepatic acetyl-CoA, acetylomes, or ER-localized ACSL1.

## Corrections

### The report does not establish more than 150 distinct patients

One review synthesized 93 reported cases and two new patients
([PMID:39798988](https://pubmed.ncbi.nlm.nih.gov/39798988/)). The other found
59 published cases and added 16 undescribed patients
([PMID:40515583](https://pubmed.ncbi.nlm.nih.gov/40515583/)). The reviews even
disagree on the published-case denominator—93 versus 59, likely because of
different inclusion criteria. Their published sets overlap and cannot be added.
No patient-level deduplication supports the report's “>150” total.

### The 4HMP fraction is not a validated sensitivity estimate

PMID:39798988 found 4HMP in 33 of 35 retrospectively tested urine samples from
acute episodes. That selected, disease-ascertained denominator is not a
prospective sensitivity study. An earlier biomarker analysis also detected
4HMP in some ketotic comparison samples and evaluated a combined
adipate-plus-4HMP cutoff in only eight decompensation samples
([PMID:25511235](https://pubmed.ncbi.nlm.nih.gov/25511235/)). Preserve
33/35, the acute-sample context, and the assay rather than promoting “94.3%
sensitivity.”

### “Incomplete penetrance” is too settled

Asymptomatic biallelic individuals exist in several families, including 3 of 19
people in the Vietnamese cohort. Because HMGCS2D is trigger-dependent and often
presents in childhood, asymptomatic relatives may be presymptomatic. One sibling
report explicitly warns that later decompensation remains possible
([PMID:40548098](https://pubmed.ncbi.nlm.nih.gov/40548098/)). Variable
expression is supported; permanent nonpenetrance is not quantified.

### Mouse acetate does not yet explain human severity

Adult inducible liver-specific knockout mice maintained glycemia and body
temperature during fasting and had higher plasma acetate
([PMID:38876267](https://pubmed.ncbi.nlm.nih.gov/38876267/)). The study did
not establish acetate's source, demonstrate that acetate supplied the
compensating fuel, or study germline HMGCS2D. The proposed human acetate
modifier remains a testable hypothesis.

### SIRT3 is not an established HMGCS2D modifier

The cited evidence comes from a cancer-metabolism review and a
cholangiocarcinoma study using cell lines, xenografts, tumor samples, and a
plasmid K310 assay
([PMID:28512002](https://pubmed.ncbi.nlm.nih.gov/28512002/);
[PMID:41960367](https://pubmed.ncbi.nlm.nih.gov/41960367/)). It supports a
biochemical SIRT3–HMGCS2 lead, not a genotype or severity modifier in HMGCS2D
patients.

### ClinGen curation is present, not absent

The ClinGen Fatty Acid Oxidation Disorders Expert Panel classified the
HMGCS2–3-hydroxy-3-methylglutaryl-CoA synthase deficiency relationship as
**definitive** on 2018-05-22, with autosomal-recessive inheritance. The report's
claimed curation gap is false.

### Patient liver was studied

PMID:9727719 measured total HMG-CoA-synthase activity in a patient's liver
homogenate and found no mitochondrial-HMGCS immunoreactive protein. The total
activity measurement could not isolate HMGCS2 from cytoplasmic or other
isoenzymes, so a modern isoenzyme-specific assay would still add value. The
report's absolute claim that no patient-liver activity measurement exists is
nevertheless false.

### The bicytopenia case is not definitive phenotype expansion

PMID:37931961 reports hepatosplenomegaly, lymphadenopathy, and bicytopenia, but
the molecular finding was described as a homozygous missense **variant of
uncertain significance**. Without functional or other definitive diagnostic
evidence, this case is a weak lead rather than a confirmed expansion of the
HMGCS2D spectrum.

### The supplementation proposal is preclinical

PMID:37503004 is the preprint later published as PMID:40692014, not an
independent study. Its L-carnitine experiments concern knockout mice,
metabolic-steatohepatitis samples, and primary hepatocytes—not HMGCS2D patients.
Neither L-carnitine nor beta-hydroxybutyrate ester should be presented as
evidence-backed disease treatment from this report.

## Ontology and provenance

OAK confirms the proposed hepatocyte, proximal-tubule, and four GO identifiers.
`CL:0000746` has the canonical label **cardiac muscle cell**, not
“Cardiomyocyte.” `OMIM:600234` is a gene entry and should not appear under
disease terms; the gene is `hgnc:5008`, and the disease is
`MONDO:0011614` **3-hydroxy-3-methylglutaryl-CoA synthase deficiency**.

The report says it systematically evaluated 41 publications, while the report
and citation sidecar expose 28 unique PMIDs. One pair—PMID:37503004 and
PMID:40692014—is a preprint and its journal update, leaving 27 distinct study
lineages. No search strings, screening log, or mapping for the remaining
publications is supplied.

## Claim-level disposition

| Claim | Disposition | Reason |
| --- | --- | --- |
| Canonical HMGCS2 ketogenesis-failure mechanism | **Retained** | Human cohorts, variant assays, and knockout models converge. |
| More than 150 distinct patients | **Rejected** | The two headline reviews overlap and cannot be summed. |
| Exact ClinVar counts | **Needs verification** | No dated query, export, filter, or accession list is supplied. |
| Hypoglycemia occurs in about 56% of all episodes | **Qualified** | 56.3% describes first presentations in one 16-person symptomatic cohort. |
| 4HMP has 94.3% sensitivity | **Qualified** | This is 33/35 selected acute samples, not a prospective performance estimate. |
| Human dual pathology through acetyl-CoA/ACSL1 | **Qualified** | Strong mouse lead; not measured in HMGCS2D patients. |
| Acetate explains variable human severity | **Needs verification** | Higher acetate was observed only in adult liver-specific knockout mice. |
| Incomplete penetrance is established | **Qualified** | Asymptomatic ascertainment does not distinguish permanent nonpenetrance. |
| SIRT3 is a clinical modifier | **Needs verification** | Evidence is from cancer models, not an HMGCS2D cohort. |
| No ClinGen curation exists | **Rejected** | A definitive ClinGen curation was approved in 2018. |
| No patient-liver activity study exists | **Rejected** | PMID:9727719 measured liver-homogenate activity and HMGCS2 protein. |
| Bicytopenia is confirmed spectrum expansion | **Qualified** | The cited case carried a VUS. |
| L-carnitine/ketone supplementation pilot | **Qualified** | It is a prospective study idea; the cited study is preclinical and disease-mismatched. |
| Ontology leads are ready verbatim | **Qualified** | One CL label and the gene/disease identifier roles need correction. |
| Forty-one publications were systematically evaluated | **Needs verification** | Only 28 PMIDs and 27 study lineages are exposed. |

## Curation boundary

Keep the hypothesis `CANONICAL`, with hypoglycemia described as frequent rather
than required. Treat acetyl-CoA/ACSL1, acetate compensation, SIRT3, and
supplementation as research leads. Do not promote the report's patient count,
formal 4HMP sensitivity, ClinGen gap, patient-liver gap, or exact database counts
into the disease YAML.
