---
reference_id: "PHEKB:18"
title: "Type 2 Diabetes Mellitus"
database: "PheKB"
content_type: "structured_record"
---

# PHEKB:18  Type 2 Diabetes Mellitus

**Type 2 Diabetes Mellitus** — phenotype algorithm page from PheKB (node 18).

## Record

| Field | Value |
|---|---|
| Phenotype ID | 18 |
| Date Created | Monday, February 6, 2012 |
| Status | Final |
| Authors | Jennifer Pacheco and Will Thompson |
| Institution | Northwestern University |
| Network Associations | eMERGE |
| Owner Phenotyping Groups | eMERGE Northwestern Group |
| Structured data | ICD9 |
| Data Source/clinical domain | observations; medications |
| Data Model | OMOP |
| Phenotype Attributes | ICD 9 Codes; Laboratories; Medications |
| Type of Phenotype | Disease or Syndrome |
| Age | Adult |
| PubMed References | PMID:22101970; PMID:22249968; PMID:31325501 |

## Description

This describes the Northwestern University Type 2 diabetes mellitus (T2DM) algorithms for extracting both T2DM cases and T2DM controls from the electronic medical record (EMR).
Comprehensive documentation of the algorithms can be found
here
. The documentation includes instructions for installing executable versions of the algorithms implemented as
workflows
for the Konstanz Information Miner (
KNIME
) data mining tool,
and sample files for both
cases
and
controls
are included.

## Files

- T2DM Algorithm
- Data Dictionary
- DiabetesChartReview-AbstractionForm7_19_10_Marshfield.doc
- DiabetesChartReview-CodeBook7_22_10_Marshfield.doc
- KNIME workflow with T2DM algorithm logic
- example potential cases file for input into KNIME workflow
- example potential controls file for input into KNIME workflow
- UPDATED list of ICD diagnosis codes inc. ICD-10
- UPDATED list of DM meds inc. NDC, RxNorm, and RegEx
- eMERGE OMOP MS SQL version of the original T2DM case algorithm

## Attachment: T2DM Algorithm

Type 2 Diabetes Mellitus Electronic Medical
Record Case and Control Selection Algorithms
Jennifer Allen Pacheco
NUgene Informatics Lead
japacheco@northwestern.edu
Will Thompson
Senior Research Associate
wkt@northwestern.edu
August 19, 2011
1 Overview
This document describes the Northwestern University Type 2 diabetes mellitus
(T2DM) algorithms for extracting both T2DM cases and T2DM controls from
the electronic medical record (EMR). There are two main parts to this docu-
ment. The ﬁrst part (Section 2) provides descriptions of the input data elements
to be extracted from the EMR, ﬂowcharts, and pseudo-code descriptions of the
algorithms. The second part (Section 3) is an installation guide for executable
workﬂows that implement the T2D case and control selection algorithms. These
worfklows are based on the Konstanz Information Miner (KNIME) data analysis
platform.1
2 Algorithm Descriptions
The case and control selection algorithms require certain patient-level data ele-
ments to be extracted from the EMR. This information includes diagnoses, lab
results, medication orders, and physician encounter dates. Lists of codes that
satisfy various algorithm requirements (including ICD-9 codes, LOINC codes,
and RxNorm codes) are provided in tabular form in Appendix A. Additionally,
Section 3.1 contains a translation of these data elements into data dictionaries
for input into the KNIME workﬂow implementations. 2
1Questions about the core algorithms should be sent to japacheco@northwestern.edu, while
questions about the executable KNIME workﬂows should be sent to wkt@northwestern.edu.
2See also the T2D study in the ele map online tool. This study contains data elements that
were used in a T2D genome-wide association study (GWAS), using a patient cohort derived
from the EMR-based algorithm described in this document.
1
2.1 T2DM Case Selection Algorithm Logic
For the T2D case selection algorithm, the following data elements are required:
1. Counts of T1DM ICD-9 code assignment dates by diagnostic source (Table 3)
2. Counts of T2DM ICD-9 code assignment dates by diagnostic source (Table 4)
3. T1DM medications (i.e., Insulin & Symlin) order or prescription dates –
at least the earliest date of Rx (Table 5)
4. T2DM medications order or prescription dates – at least the earliest date
of Rx (Table 6)
5. Fasting blood glucose lab values – at least the maximum value (Table 7)
6. Random blood glucose lab values – at least the maximum value (Table 7)
7. HBA1c lab values – at least the maximum value (Table 7)
For the T2D case selection algorithm, the following deﬁnitions apply:
• Abnormal lab – An abnormal lab value is deﬁned as one of the following:
– Random glucose > 200 mg/dl
– Fasting glucose≥ 125 mg/dl
– Hemoglobin A1c≥ 6.5%
• Physician entered diagnosis – A physician entered diagnosis code is one
that is derived from encounter or problem list sources only (excludes billing
codes).
A ﬂowchart expressing the logic of the T2DM case selection algorithm is shown
in Figure 1. There are ﬁve paths through this ﬂowchart, and these ﬁve paths are
translated into equivalent pseudo-code in Algorithm 1. This algorithm shows
the top-level logic, with additional sub-procedures implementing the lower-level
details. These sub-procedures are also expressed below, in terms of an SQL-like
syntax that is linked to the ICD-9, LOINC, and RxNorm codes in Appendix A.3
3These are the abbreviations used in the following ﬂowcharts and algorithms:
• dx→ diagnosis
• rx→ prescription
• pt→ patient
• dt→ date
• cnt→ count
2
Figure 1: Algorithm for identifying T2DM cases in the EMR.
3
Algorithm 1 T2DM case selection algorithm. This algorithm takes a patient-
level record ( pt) as an argument, and returns the patient’s case status
({case, unknown}) as result.
t2dm-case-selection(pt)
status = unknown
1 if t1dm-dx-dt-cnt(pt) == 0 ⇐ Algorithm 2
and t2dm-dx-dt-cnt(pt) > 0 ⇐ Algorithm 3
and t2dm-rx-dt (pt)̸= null ⇐ Algorithm 4
and t1dm-rx-dt (pt)̸= null ⇐ Algorithm 5
and t2dm-rx-dt (pt) < t1dm-rx-dt(pt)
status = case
2 elseif t1dm-dx-dt-cnt(pt) == 0
and t2dm-dx-dt-cnt(pt) > 0
and t1dm-rx-dt (pt) == null
and t2dm-rx-dt (pt)̸= null
status = case
3 elseif t1dm-dx-dt-cnt(pt) == 0
and t2dm-dx-dt-cnt(pt) > 0
and t1dm-rx-dt (pt) == null
and t2dm-rx-dt (pt) == null
and abnormal-lab (pt) == true ⇐ Algorithm 6
status = case
4 elseif t1dm-dx-dt-cnt(pt) == 0
and t2dm-dx-dt-cnt(pt) == 0
and t2dm-rx-dt (pt)̸= null
and abnormal-lab (pt) == true
status = case
5 elseif t1dm-dx-dt-cnt(pt) == 0
and t2dm-dx-dt-cnt(pt) > 0
and t1dm-rx-dt (pt)̸= null
and t2dm-rx-dt (pt) == null
and t2dm-physcn-dx-dt-cnt(pt)≥ 2 ⇐ Algorithm 7
status = case
return status
4
Algorithm 2 Count of distinct dates of T1DM DX (called by Algorithm 1)
t1dm-dx-dt-cnt(pt)
count =
select count-distinct-dt(records)
from dx-table
where
dx-table . pt == pt
and dx-table . icd-9-code∈{ . . .} ⇐ Table 3
return count
Algorithm 3 Count of distinct dates of T2DM DX (called by Algorithm 1)
t2dm-dx-dt-cnt(pt)
count =
select count-distinct-dt(records)
from dx-table
where
dx-table . pt == pt
and dx-table . icd-9-code∈{ . . .} ⇐ Table 4
return count
Algorithm 4 First date of Rx for T2DM medication (called by Algorithm 1)
t2dm-rx-dt(pt)
dt =
select first-dt(records)
from rx-table
where
rx-table . pt == pt
and rx-table . rxnorm-code∈{ . . .}⇐ Table 6
return dt
5
Algorithm 5 First date of Rx for T1DM medication (called by Algorithm 1)
t1dm-rx-dt(pt)
dt =
select first-dt(records)
from rx-table
where
rx-table . pt == pt
and rx-table . rxnorm-code∈{ . . .}⇐ Table 5
return dt
Algorithm 6 Check for abnormal lab (called by Algorithm 1)
abnormal-lab(pt)
abnormal-lab = false
lab-results =
select records
from labs-table
where
labs-table . pt == pt
and labs-table . loinc-code∈{ . . .} ⇐ Table 7
for each lab∈ lab-results
if lab . type == random-glucose
and lab . value≥ 200 / /(mg/dl)
or lab . type == fasting-glucose
and lab . value≥ 125 / /(mg/dl)
or lab . type == HBA1c
and lab . value≥ 6.5 / /(percent)
abnormal-lab = true
return abnormal-lab
6
Algorithm 7 Count of distinct dates of T2DM DX made by a physician (called
by Algorithm 1)
t2dm-physcn-dx-dt-cnt(pt)
count =
select count-distinct-dt(records)
from dx-table
where
dx-table . pt == pt
and dx-table . source∈{ encounter, problem-list}
and dx-table . icd-9-code∈{ . . .} ⇐ Table 4
return count
7
2.2 T2DM Control Selection Algorithm Logic
For the T2D control selection algorithm, the following data elements are re-
quired:
1. Counts of ICD-9 codes related to diabetes (Table 9)
2. Fasting blood glucose lab values – at least the maximum value (Table 7)
3. Random blood glucose lab values – at least the maximum value (Table 7)
4. HBA1c lab values – at least the maximum value (Table 7)
5. Diabetes family history – could be supplemented with self-reported data
from a questionnaire
6. T1DM medications (i.e., Insulin & Symlin) order or prescription dates –
at least the earliest date of Rx (Table 5)
7. T2DM medications order or prescription dates – at least the earliest date
of Rx (Table 6)
8. Diabetes medical supply orders (Table 8)
9. Count of dates the patient had face-to-face outpatient clinic encounters
(in-person visits with a clinician)
For the control selection algorithm, the following deﬁnition applies:
• Abnormal lab : abnormal lab values include:
– Random glucose > 110 mg/dl
– Fasting glucose≥ 110 mg/dl
– Hemoglobin A1c≥ 6.0%
A ﬂowchart expressing the logic of the T2DM control selection algorithm is
shown in Figure 2. There is only one path through this ﬂowchart, and this path
is translated into equivalent pseudo-code in Algorithm 8. This algorithm shows
the top-level logic, with additional sub-procedures implementing the lower-level
details. These sub-procedures are also expressed below, in terms of an SQL-like
syntax that is linked to the ICD-9, LOINC, and RxNorm codes in Appendix A.
8
Figure 2: Algorithm for identifying T2DM controls in the EMR.
Algorithm 8 TT2DM control selection algorithm. This algorithm takes a
patient-level record (pt) as an argument, and returns the patient’s control status
({control, unknown}) as result.
t2dm-control-selection(pt)
status = unknown
1 if dm-dx-dt-cnt(pt) == 0 ⇐ Algorithm 9
and glucose-lab-exists (pt) == true ⇐ Algorithm 10
and abnormal-lab (pt) == false ⇐ Algorithm 11
and enctrs-dt-cnt (pt)≥ 2 ⇐ Algorithm 12
and dm-meds-supplies-rx-dt-cnt (pt) == 0 ⇐ Algorithm 13
and fam-hist-of-dm(pt) == false ⇐ Algorithm 14
status = control
return status
9
Algorithm 9 Count of distinct dates of DM-related DX (called by Algorithm 8)
dm-dx-dt-cnt(pt)
count =
select count-distinct-dt(records)
from dx-table
where
dx-table . pt == pt
and dx-table . icd-9-code∈{ . . .} ⇐ Table 9
return count
Algorithm 10 Check for glucose lab performed (called by Algorithm 8)
glucose-lab-exists(pt)
glucose-lab-exists = false
lab-results =
select records
from labs-table
where
labs-table . pt == pt
and labs-table . loinc-code∈{ . . .} ⇐ Table 7 (glucose only)
if lab-results . count > 0
glucose-lab-exists = true
return glucose-lab-exists
10
Algorithm 11 Check for abnormal lab (called by Algorithm 8)
abnormal-lab(pt)
abnormal-lab = false
lab-results =
select records
from labs-table
where
labs-table . pt == pt
and labs-table . loinc-code∈{ . . .} ⇐ Table 7
for each lab∈ lab-results
if lab . type == random-glucose
and lab . value≥ 110 / /(mg/dl)
or lab . type == fasting-glucose
and lab . value≥ 110 / /(mg/dl)
or lab . type == HBA1c
and lab . value≥ 6.0 / /(percent)
abnormal-lab = true
return abnormal-lab
Algorithm 12 Count of distinct dates for in-person oﬃce encounters with a
physician (called by Algorithm 8)
enctrs-dt-cnt(pt)
count =
select count-distinct-dt(records)
from enctrs-table
where
enctrs-table . pt == pt
and enctrs-table . type == office
return count
11
Algorithm 13 Count DM-related medications and supplies by distinct Rx date
(called by Algorithm 8)
dm-meds-supplies-rx-dt-cnt(pt)
count =
select count-distinct-dt(records)
from rx-table
where
rx-table . pt == pt
and
rx-table . rxnorm-code∈{ . . .} ⇐ Table 5
or rx-table . rxnorm-code∈{ . . .} ⇐ Table 6
or rx-table . rxnorm-code∈{ . . .} ⇐ Table 8
return count
Algorithm 14 Check for family history of DM (called by Algorithm 8)
fam-hist-of-dm(pt)
fam-hist-results =
select records
from fam-hist-table
where
fam-hist-table . pt == pt
and
fam-hist-table . t1dm == true
or fam-hist-table . t2dm == true
if fam-hist-results . count > 0
return true
else return false
12
3 KNIME workﬂow
This section describes installation of executable workﬂows that implement the
case and control algorithms described in Section 2. These workﬂows are exe-
cuted inside of the Konstanz Information Miner (KNIME) data analysis plat-
form. The workﬂows take as input comma-separated value (csv) ﬁles, with
each row corresponding to a patient (for examples, see the sample input ﬁles
dm potential cases.csv and dm potential controls.csv).
3.1 Data Dictionaries
Each row of input data consists of a set of patient-level variables. We present
here the data dictionaries that describe these patient-level input variables. The
columns of the dictionaries specify each variable’s name, type, and range of
possible values. The next column speciﬁes whether or not missing values are
permitted, and if so, what the default value of the variable is.4 The ﬁnal column
refers (where appropriate) to the table in Appendix A where corresponding code
values for the variable can be found.
Table 1: Input variables to the T2DM case selection KNIME workﬂow
Name Type Range Missing (def.) Ref.
pat id (unique) integer n≥ 1 false NA
t1dm dx cnt integer n≥ 0 true (0) Table 3
t2dm dx cnt integer n≥ 0 true (0) Table 4
t2dm physcn dx cnt integer n≥ 0 true (0) Table 4
t1dm rx dt string yyyy-mm-dd true (null) Table 5
t2dm rx dt string yyyy-mm-dd true (null) Table 6
max fast gluc lab val float n≥ 0.0 true (null) Table 7
max rndm gluc lab val float n≥ 0.0 true (null) Table 7
max hba1c lab val float (%) 0 .0≤ n≤ 100.0 true (null) Table 7
4The default value is automatically inserted for a variable when it is missing a speciﬁed
value.
13
Table 2: Input variables to the T2DM control selection KNIME workﬂow
Name Type Range Missing (def.) Ref.
pat id (unique) integer n≥ 1 false NA
fam hist of dm integer n∈{ 0, 1} true (0) NA
enctrs cnt integer n≥ 0 true (0) Table 3
max fast gluc lab val float n≥ 0.0 true (null) Table 7
max rndm gluc lab val float n≥ 0.0 true (null) Table 7
max hba1c lab val float (%) 0 .0≤ n≤ 100.0 true (null) Table 7
dm dx cnt integer n≥ 0 true (0) Table 9
dm med supplies cnt integer n≥ 0 true (0) Table 5,
Table 6,
Table 8
14
3.2 Installation and Execution
1. Download and install KNIME (version 2.4 or later). The KNIME website
contains installation instructions, as well as tutorials.
2. Download the T2D case and control workﬂows, which are contained in a
single zip ﬁle: T2D-workflows.zip. Don’t unzip the ﬁle.
3. Download the two sample input ﬁles for the workﬂows:dm potential cases.csv
and dm potential controls.csv.
4. Start KNIME. On start-up, you will see an empty workspace similar to
the screenshot in Figure 3.
5. Select File⇒ Import KNIME workﬂow. . . The resulting pop-up window
is shown in Figure 4. Click on the Select archive ﬁle: radio button, and
navigate to your local copy of the T2D-workflows.zip ﬁle. Click on the
Finish button.
6. Double-click on the Diabetes-Case-Assignment workﬂow to open it. Your
workspace will now look similar to the screenshot in Figure 5. 5
7. Double-click on the File Reader node in the workﬂow graph. You will see
the pop-up window shown in Figure 6. Click on the Browse. . . button and
navigate to your local copy of the dm potential cases.csv ﬁle. Your
pop-up window should look like the one in Figure 7. Make sure that
the read row IDs box is unchecked, while the read column headers box is
checked. Click on the OK button to close the window.
8. Double-click on the CSV Writer node in the workﬂow graph. Click on the
Browse. . . button and navigate to a directory of your choosing where the
output ﬁle dm cases.csv will be generated. Click on the OK button to
close the window.
9. The workﬂow is now ready to execute. Click on the green button with the
double arrow at the toolbar at the top, or enter Shift+F7 on the keyboard.
If the nodes of the workﬂow have already been executed 6, then ﬁrst select
all nodes ( Control+A), right click, and select Reset.
(a) The output ﬁle will be located in the directory that you chose in
Step 8.
(b) Right click on the Rule Engine node in the graphical view and select
Classiﬁed Data in order to view the output of the algorithm (Figure 8).
(c) Right click on the Histogram node in the graphical view and select
View:Histogram View to get counts of the assignments that were made
(Figure 9).
5All following steps apply also to the Diabetes-Control-Assignment workﬂow.
6An executed node will have a green indicator underneath it.
15
Figure 3: Step 4
16
Figure 4: Step 5
17
Figure 5: Step 6
18
Figure 6: Step 7
Figure 7: Step 7
19
Figure 8: Step 9b
Figure 9: Step 9c
20
A Data Elements
Table 3: T1DM diagnosis codes. Used in Algorithm 1.
Description ICD-9 code
Type 1 Diabetes 250.x1, 250.x3
Table 4: T2DM diagnosis codes. Used in Algorithm 1.
Description ICD-9 code
Type 2 Diabetes 250.x0, 250.x2
(excl. 250.10, 250.12)
Table 5: T1DM medications. Used in Algorithm 1 and Algorithm 8.
Generic Name Example Brand RxNorm CUI
(ingredient-level)
insulin 139825, 274783, 314684,
352385, 400008, 51428,
5856, 86009
pramlintide Symlin 139953
21
Table 6: T2DM medications. Used in Algorithm 1 and Algorithm 8.
Generic Name Example Brand RxNorm CUI
(ingredient-level)
acetohexamide Dymelor 173
tolazamide Tolinase 10633
chlorpropamide Diabinese 2404
glipizide Glucotrol 4821
glipizide Glucotrol XL 217360
glyburide Micronase,
Glynase,
Diabeta
4815
glimepiride Amaryl 25789
repaglinide Prandin 73044
nateglinide Starlix 274332
metformin Glucophage 6809
rosiglitazone Avandia 84108
pioglitazone ACTOS 33738
troglitazone Rezulin 72610
acarbose Precose 16681
miglitol Glyset 30009
sitagliptin Januvia 593411
exenatide Byetta 60548
Table 7: Diabetes mellitus lab codes. Used in Algorithm 1 and Algorithm 8
Description LOINC code
Fasting glucose 1558-6
Random glucose 2339-0, 2345-7
Hemoglobin A1C 4548-4, 17856-6,
4549-2, 17855-8
22
Table 8: Diabetes medical supplies. Used in Algorithm 8.
Description Source Vocab. RxNorm CUI
(ingredient-level)
Blood-glucose meters
& sensors
NDDF 126958, 412956, 412959,
637321, 668291, 668370,
686655, 692383, 748611,
880998, 881056
VANDF 751128
Insulin syringes RxNorm 847187, 847191, 847197,
847203, 847207, 847211,
847230, 847239, 847252,
847256, 847259, 847263,
847278, 847416, 847417
NDDF 806905, 806903, 408119
Table 9: Diabetes mellitus diagnosis codes. Used in Algorithm 8.
Description ICD-9 code
Diabetes mellitus (T1 & T2) 250.xx
Impaired fasting glucose 790.21
Impaired oral glucose tolerance test 790.22
Abnormal glucose not otherwise spec. 790.2, 790.29
Abnormal glucose during pregnancy 648.8x
Gestational diabetes 648.0x
Glycosuria 791.5
Dysmetabolic syndrome X 277.7
Family history of diabetes mellitus V18.0
Screening for diabetes mellitus V77.1
23

## Suggested citation

Jennifer Pacheco and Will Thompson. Northwestern University. Type 2 Diabetes Mellitus. PheKB; 2012 Available from: https://phekb.org/phenotype/18

## Source

PheKB phenotype page 18. PDF algorithm documents are transcribed by text extraction; journal articles and non-PDF attachments are listed only. PheKB states no licence for its content.

[PheKB record](https://phekb.org/node/18)
