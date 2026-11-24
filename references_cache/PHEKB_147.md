---
reference_id: "PHEKB:147"
title: "Heart Failure (HF) with Differentiation between Preserved and Reduced Ejection Fraction"
database: "PheKB"
content_type: "structured_record"
---

# PHEKB:147  Heart Failure (HF) with Differentiation between Preserved and Reduced Ejection Fraction

**Heart Failure (HF) with Differentiation between Preserved and Reduced Ejection Fraction** — phenotype algorithm page from PheKB (node 147).

## Record

| Field | Value |
|---|---|
| Phenotype ID | 147 |
| Date Created | Sunday, February 24, 2013 |
| Status | Final |
| Authors | Suzette J. Bielinski |
| Institution | Mayo Clinic |
| Network Associations | eMERGE |
| Owner Phenotyping Groups | eMERGE Mayo Group |
| Structured data | CPT; ICD9 |
| Unstructured Data | NLP |
| Data Source/clinical domain | observations; medications |
| Phenotype Attributes | CPT Codes; ICD 9 Codes; Laboratories; Medications; Natural Language Processing |
| Type of Phenotype | Disease or Syndrome |
| Gender | Female; Male |
| Age | Adult |

## Files

- HF Validation Spreadsheet.xlsx
- Liu_CRI2013_0121_revised.pdf (journal article; cited by PMID, not transcribed)
- Heart Failure Validation Guidelines 11132013.docx
- Data Dictionary for Case/Non-Case Algorithm
- Pseudo Code for Case/Non-Case Version of Heart Failure Algorithm
- Pseudo Code for Cohort Version of Heart Failure Algorithm
- Data Dictionary for Cohort Version of Heart Failure Algorithm

## Attachment: Pseudo Code for Cohort Version of Heart Failure Algorithm

Page 1 of 11

Heart Failure

With Differentiation Between Reduced
and Preserved Ejection Fraction

Phenotype Algorithm
Pseudo Code

Cohort Version

Page 2 of 11

Contents
Introduction ..................................................................................................................................... 3
Cohort Version ................................................................................................................................ 3
Algorithm Development ................................................................................................................. 3
Web Table 1. Data Elements Required for the Heart Failure Algorithm .............................. 4
Defining Heart Failure Case Status................................................................................................. 4
Web Table 2. Characteristics of Heart Failure Status Definitions ......................................... 5
Heart Failure Date Assignment Rules..................................................................................... 5
Web Table 3. Assigning First Detected Heart Failure Dates by Case Definition .................. 5
Classifying Heart Failure in terms of Ejection Fraction ......................................................... 5
Web Figure 1. Heart Failure Algorithm Flow Chart....................................................................... 7
Appendices ...................................................................................................................................... 8
Appendix A: Natural Language Processing (NLP) Implementation Strategies .................... 8
Appendix B: Echocardiography Reports ............................................................................... 9
Web Table 4. Regular Expressions* for Reporting of Ejection Fraction in Unstructured
Reports .................................................................................................................................... 9
Web Table 5. Classification of Free Text Responses .......................................................... 10
REFERENCES ............................................................................................................................. 11

Page 3 of 11

Introduction: Heart failure (HF) is a complex syndrome characterized by the
inability of the heart to supply sufficient blood flow to the body. HF is diagnosed
clinically and further dichotomized by left ventricular ejection fraction (i.e., reduced or
preserved). In 2010, HF affected 6.6 million Americans at a cost of 34.4 billion (1, 2).
However, the syndromic nature of HF presents challenges in identification of HF cases
and controls from EHR data for research given that the diagnosis is clinical. The
Electronic Medical Records and Genomics (eMERGE) Network (3) consortium has
demonstrated the applicability and portability of EHR derived phenotype algorithms
using different types and modalities of clinical data for algorithm execution including
billing and diagnoses codes, natural language processing (NLP), laboratory
measurements, patient procedure encounters, and medication data.
Cohort Version: The cohort version of this algorithm is designed to identify heart
failure status for every patient in a defined cohort. Heart Failure case status is assigned
based on the level of evidence. Those meeting the strict case definition are classified as
“definite heart failure” and those with varying degrees of evidence as classified as
“probable” or “possible” heart failure. Only those without any indication of heart
failure are classified as controls (i.e., non-cases).
Algorithm Development: Using a gold standard cohort of 706 manually abstracted HF
cases defined according to Framingham Heart Failure Criteria (4) from the Heart

Page 4 of 11

Failure in the Community Cohort (R01 HL72435), structured EHR data were combined
with analyses of the clinical note (unstructured) to identify the set of parameters needed
to reidentify all the cases. HF terms were identified using natural language processing
(NLP) (i.e., dictionary lookup, negation/probable identification with ConText (5-7)) to
identify positive hits of HF from the major and secondary problem lists of the clinical
note. The specific data elements are listed in Web Table 1.

Web Table 1. Data Elements Required for the Heart Failure Algorithm
Data Type Details
ICD9-CM Diagnoses Codes Primary Heart Failure Codes = 428.X
Patient Demographics Date of Birth, sex, race
Medication History Drug, dose, duration (mapped to RXNORM)
Echocardiography Results Average ejection fraction from echocardiography report (structured or
unstructured data) or free text EF reported by clinician (unstructured data)
*Natural Language Processing
of the Clinical Note

(See Appendix A for additional
information)
Unstructured problem list – at least one positive mention of a HF term in
diagnosis-related sections. Positive mention is defined using ConText for
assigning statuses to each NLP result – positive, probable, and negative (5-7).
Thus a positive hit for this requirement equates to a non-negative and non-
probable result. Mapping of terms is insensitive to upper/lower case.
• multi-organ failure or multiorgan failure
• cardiac failure
• CHF
• heart failure
• ventricular failure
Structured problem list – The descendant traversal of SNOMEDCT code 84114007
(heart failure)
*Appendix A includes additional information about NLP implementation strategies

Defining Heart Failure Case Status: Three data elements are used to assign heart
failure status; presence of ICD9 code(s) for heart failure, positive mention of one of the five
heart failure terms, and measurement of ejection fraction. Heart failure case status is assigned
as “definite”, “probable”, “possible”, and control (i.e., no heart failure) depending on the level
of evidence. Web Figure 1 provides an illustration of the algorithm.

Page 5 of 11

Web Table 2. Characteristics of Heart Failure Status Definitions
HF Status Presence of ICD9 AND positive
mention of HF Heart Failure Date Ejection Fraction
Definite Yes 365 day window
No EF
EF <50% (HF Type = 1)
EF ≥50% (HF Type = 2)
Probable Yes (or ≥5 unique dates of either) 365- 1825 day
window
No EF
EF <50% (HF Type = 1)
EF ≥50% (HF Type = 2)
Possible Either or none if EF <50 Unable to assign
date any
Control None N/A No EF
EF ≥50

Heart Failure Date Assignment Rules: Taking the cross product of all the unique
ICD-9 dates and NLP dates, assign the heart failure date according to the rules in Web Table 3.

Web Table 3. Assigning First Detected Heart Failure Dates by Case Definition
Definite Heart
Failure
ICD-9 and NLP date occurred within 365 days of each other – assign the earliest of
the two dates
Probable Heart
Failure
ICD-9 or NLP date occurred within 365–1825 days of each other - assign the
earliest of the two dates
Possible Heart
Failure No date is assigned for this group

Classifying Heart Failure in terms of Ejection Fraction: Electronic medical record systems
record echocardiography results including measures of ejection fraction as either structured or
unstructured data. Furthermore, ejection fraction may be reported as a quantitative variable or
by free text responses (e.g., normal). Appendix B provides details regarding the processing of
ejection fraction based on the mode in which the data is reported. Patients who are classified as
either “definite” or “probable” heart failure are further classified based on level of ejection
fraction (i.e., reduced EF or preserved EF).

Page 6 of 11

 HF with reduced EF (HF Type = 1)
 ejection fraction <50% or free text = reduced
 HF with preserved EF (HF Type = 2)
 ejection fraction ≥50% or free text = preserved
 No qualifying EF measurements within any of the time frames considered(HF Type
= 0)
It is common in clinical practice for heart failure patients to have serial echocardiography
measurements. Therefore, to determine heart failure type (i.e., reduced or preserved), priority
is first given to measurements immediately following the diagnosis date.
1. Lowest average EF measured 0-182 days (approximately a 6 month period) after the HF
date. If missing, go to number 2.
2. Lowest average EF measured 0-182 days (approximately a 6 month period) prior to the
HF date. If missing go to number 3.
3. Lowest average EF measured 183-365 days after the HF date. If missing go to number 4.
4. Lowest average EF measured 183-365 days prior to HF date. If missing, set HF type to
none (HF Type = 0).
For free text results, if the heart failure patient had an echocardiography that indicated
“reduced” ejection fraction 365 days after or prior to the heart failure date then HF Type = 1. If
in that same timeframe all available echocardiography reports indicated “preserved” then HF
Type = 2. If there are no echocardiography reports within the time window then set HF type to
none (HF Type = 0).

Page 7 of 11

Web Figure 1. Heart Failure Algorithm Flow Chart

Page 8 of 11

Appendices

Appendix A: Natural Language Processing (NLP) Implementation Strategies

Mayo Clinic Electronic Medical Record (GE Centricity): The NLP component of the case
definition was implemented by searching the Major and Secondary problem list section of the
clinical note for at least one positive mention of one of the heart failure terms. Positive mention
is defined using ConText for assigning statuses to each NLP result – positive, probable, and
negative (5-7). Thus a positive hit for this requirement equates to a non-negative and non-
probable result. Mapping of terms is insensitive to upper/lower case. All NLP dates associated
with probable heart failure as defined by ConText were excluded. Among the remaining dates,
we assigned the earliest NLP date among those associated with the major problem list and in
the case where there was no note date associated with the major problem list; the earliest NLP
date among those associated with the secondary problem list was used.

Group Health Electronic Medical Record (EPIC): The clinical notes are in non-Clinical
Document Architecture formatted documents, thus SecTag was used to detect Diagnosis and
other sections (i.e., Chief Complaints or Impressions as the Secondary Problem List section).

Page 9 of 11

Appendix B: Echocardiography Reports

Structured Echocardiography Database: Identify all variables corresponding to ejection fraction
(EF) and average all EF measurements meeting the minimum/maximum threshold criteria to
obtain a single exam EF. When there were multiple echocardiography tests on the same day, all
EF measurements were averaged.
Unstructured Echocardiography Reports: Natural language processing (NLP) can be used to
search unstructured Echocardiography reports for EF measurements. A list of regular
expressions for reporting EF is available in Web Table 4.

Web Table 4. Regular Expressions* for Reporting of Ejection Fraction in Unstructured Reports
• Calculated EF ##%
• Calculated LVEF ##%
• Calculated LV ejection fraction ##%
• Calculated Left Ventricular ejection fraction ##%
• Calculated Ejection Fraction ##%
• Calculated Ejection Fraction ##%. Visual estimate
##%-##%
• Estimated EF ##%
• Estimated EF = ##%
• Estimated EF ##%-##%
• Estimated Ejection Fraction ##%
• Estimated Ejection Fraction ##%-##%
• Estimated Left Ventricular Ejection Fraction ##%
• Estimated Left Ventricular Ejection Fraction ##% -
##%
• Estimated Left Ventricular Ejection Fraction range
##%-##%
• EF ##%
• Ejection Fraction ##%
• LVEF ##%
• LVEF ~ ## - ##%Left Ventricular Ejection Fraction
##%
• Visual Estimate of LVEF ##%
• Visual estimate of Left Ventricular Ejection Fraction
##%
• Visual Estimate of EF ##%
• Visual Estimate of Ejection Fraction ##%
*The regular expression list above includes the variations identified during the algorithm validation at Mayo Clinic and Group
Health and thus is not an exhaustive list of every possible combination of the use of characters such as “=” or “~”.

Unstructured Free Text: Natural language processing (NLP) can be used to search
unstructured Echocardiography reports for EF measurements that are resulted as free text

Page 10 of 11

descriptions rather than numerical values. Classification of preserved or reduced based on free
text variations are included in Web Table 5.
Web Table 5. Classification of Free Text Responses
EF Result Categories Free Text Variations*
Preserved normal, supernormal, low-normal, moderate
Reduced abnormal, reduced, low, severe, decreased
*The variations included on this list were identified at a single eMERGE site and thus may not be exhaustive list.

Page 11 of 11

REFERENCES
1. Roger VL, Go AS, Lloyd-Jones DM, et al. Heart disease and stroke statistics--2012 update:
a report from the American Heart Association. Circulation. 2012;125(1):e2-e220.
2. Heidenreich PA, Trogdon JG, Khavjou OA, et al. Forecasting the future of cardiovascular
disease in the United States: a policy statement from the American Heart Association.
Circulation. 2011;123(8):933-944.
3. Kho AN, Pacheco JA, Peissig PL, et al. Electronic medical records for genetic research:
results of the eMERGE consortium. Sci Transl Med. 2011;3(79):79re71.
4. Roger VL, Weston SA, Redfield MM, et al. Trends in heart failure incidence and survival
in a community-based population. JAMA. 2004;292(3):344-350.
5. Harkema H, Dowling JN, Thornblade T, et al. ConText: an algorithm for determining
negation, experiencer, and temporal status from clinical reports. J Biomed Inform.
2009;42(5):839-851.
6. Chapman WW, Chu D, Dowling JN. ConText: an algorithm for identifying contextual
features from clinical text. Proceedings of the Workshop on BioNLP 2007: Biological,
Translational, and Clinical Language Processing. Prague, Czech Republic: Association for
Computational Linguistics, 2007:81-88.
7. Chapman BE, Lee S, Kang HP, et al. Document-level classification of CT pulmonary
angiography reports based on an extension of the ConText algorithm. J Biomed Inform.
2011;44(5):728-737.

## Suggested citation

Suzette J. Bielinski. Mayo Clinic. Heart Failure (HF) with Differentiation between Preserved and Reduced Ejection Fraction. PheKB; 2013 Available from: https://phekb.org/phenotype/147 Log in to post comments David Carrell HF NLP system availability? Mon, 2013-04-01 12:32 Hi, Any information on when the HF NLP system will be availble, or if it is ready now where we can download it? Thanks, David Log in to post comments Jen Pacheco 2 questions: ICD-9 in PL, & no numeric EF Wed, 2013-09-04 17:01 1) in 1 of our main systems ICD-9 codes are what is recorded in the Problem List (PL); thus, should we look for ICD-9 codes 428.* to find pts meeting the PL part of the case criteria? 2) In some of the echo results there is no numeric EF (ejection fraction), only a descriptive word such as: normal/abnormal, low/moderate/severe, or reduced/decreased. This occurs for ~1,000 of our ~2,000 genotyped pts w/ EF measures, of which ~100 pts only have this type of result. How would you want us to categorize these cases, if they turn out to be cases otherwise? i.e., if normal then type 2, else throw them out? Thanks! Jen Log in to post comments David Carrell HF Case validation Tue, 2013-09-24 14:19 Hi, When conducting manual chart review validation of heart failure cases, if the manual review confirms that the patient has HF but the **index date** identified by manual review differs from the index date identified by the automated algorithm, how do you want us to classify this case for validation purposes (confirmed by manual review or not confirmed by manual review)? Does it matter how much difference there is between the two index dates, and if so, how much it too much of a difference? Thanks, David Log in to post comments Sue Bielinski HF Date Wed, 2013-11-20 11:25 We took a rather liberal approach as we found this as well. If the dates were reasonably close (arbitrary) w/i a year we accepted. As heart failure is a syndrome and exact date is not critical. Log in to post comments Jacqueline Kirby Validated? Thu, 2013-11-14 09:10 I saw this moved from Testing to Validated, but I don't see any validation results. Has GHC, the secondary site, completed it's validation? Is this ready to be implemented by the Network? Thanks, Jacqueline Log in to post comments David Carrell Validation at Group Health/UW Fri, 2013-11-15 18:16 Our validation is uderway. Controls validatated with a PPV of 100% (random sample of N=25 subjects). Cases are being validated now. Six of 27 charts selected for validation have been completed and all of them validated. Keeping fingers crossed for the remaining cases. -David Log in to post comments David Carrell In the Excel data dictionary, Fri, 2013-11-15 18:19 In the Excel data dictionary, please specify an"as of" date for vital status (which is coded as alive or dead). Is it Case Date? Data pull date? etc... Thanks VITAL STATUS Vital Status of Subject C37987 Alive C28554 Dead Log in to post comments Sue Bielinski Vital status Wed, 2013-11-20 11:26 I am editing the DD to state "as of data pull" Log in to post comments Jacqueline Kirby Priority Metric Wed, 2014-02-05 11:18 Is it correct to interpret: "Lowest EF measured 6 months after the HF date ." as the lowest Ejection fraction measured 0-6 months after the HF_date Log in to post comments Sue Bielinski Lowest EF Sat, 2014-02-08 14:44 Yes that is correct Log in to post comments Jacqueline Kirby EF values Tue, 2014-02-11 15:30 I just wanted to confirm about two situations for determining ejection fractions: 1. In our documents we have instances of "Normal" instead of a numeric value. If this is the qualifying EF, so we consider it Case type 2? 2. In our parsing algorithm, if there is a range for EF, eg 40-55, we take the average of the range as the EF value. Will this work for this algorithm? Note, if we need to change this, this will involve alot more effort to completing this. Thanks, Jacqueline Log in to post comments Sue Bielinski Determination of EF Tue, 2014-02-11 15:35 Yes for both questions. Consider as case 2 for those with normal listed and average when a range is provided. Thanks Sue Log in to post comments Jacqueline Kirby Questions on the DD Fri, 2014-02-21 11:34 1. For the BMI file, you ask for Weight in Pounds and Height in inches, but the dd standard in eMERGE tends to have this sent as kg and cm. Is there a reason you changed this? Do you need us to covert this, or can we send as kg and cm? 2. For HF_MI_Rep_measurement - I am confused by this formate. We may have multiple dates for each ICD type. I am not sure how you are wanting a row to be lined up? Because for example I may have 5 410s, 2 412s, 1 413, and no 414, how should this be represented? OR should we send a ICD file with id, ICD code name, and ICD date for icds in your list? Thanks, Jacqueline Log in to post comments Jacqueline Kirby Data Dictionary Questions Fri, 2014-02-28 09:29 1. LAST_FU_DATE - We don't have followup data as a structured field. How are you defining this? Follow-up from EF? If so, which one? Or just last date of some clinic visit? 2. For EF, you say you want this field of be an interger. Our EF data has alot of things in it that are not just #, eg. "Normal" or ranges or some > some value. Do you only want integer EFs or should we send everything? Thanks, Jacqueline Log in to post comments Sue Bielinski FU date and EF Fri, 2014-02-28 12:16 1. For FU, groups are either using a date from registration or last encounter/visit date. 2. Integer prefered - if a range is given, provide only the lowest number. If the only EF listed is normal, then indicate that - these patients will be considered Type 2 HF (normal = EF > 50%). Log in to post comments Sue Bielinski Updated Data Dictionary and Pseudo Code Tue, 2014-03-04 13:27 I have upload new versions of the data dictionary and pseudo code that address the issue of ejection fraction (EF) results being only reported as free text (e.g. normal/abnormal). Furthermore, units for weight and height were changed to kg and cm per eMERGE standard procedure. Thanks Sue Log in to post comments David Carrell RAW VALUE and FORMATTED VALUE specifications needed in data dict Tue, 2014-04-15 12:16 Hi, Can you please provide RAW VALUE and FORMATTED VALUE specs in the data dictionary for all fields? Examples where these specs are missing are HF_INDEX_DATE, HF_INDEX_EF (among others) in the HF_SUBJECT table (but the specs are missing from other tables too). Thanks! Log in to post comments David Carrell Standard date value format Tue, 2014-04-15 12:22 Meant to suggest ISO 8601 format as a standard for representing calendar dates as strings (e.g,. today's date would be the string "2014-04-15"). Log in to post comments Sue Bielinski HF limited data dictionaries Fri, 2016-07-15 13:36 We have streamlined the data dictionaries to limit to those variables needed in the GWAS analsyes. Everything has been updated on PheKb Log in to post comments Sue Bielinski HF Data dictionary Thu, 2016-08-04 09:04 We edited the Data dictionary to allow for missing values of EF per the phentoype meeting 8/3/2016. The values are still required but for those with missing data please code as follows. .=missing/unknown/unassessed/non-applicable Log in to post comments

## Source

PheKB phenotype page 147. PDF algorithm documents are transcribed by text extraction; journal articles and non-PDF attachments are listed only. PheKB states no licence for its content.

[PheKB record](https://phekb.org/node/147)
