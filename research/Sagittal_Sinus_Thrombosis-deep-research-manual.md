# Sagittal Sinus Thrombosis manual research notes

## Provider attempts

- Falcon attempt 1: `just research-disorder falcon Sagittal_Sinus_Thrombosis` was started from the worktree with `EDISON_API_KEY` exported from `/home/harry/dismech/edison_tok`; it remained silent and produced no report file after an extended wait, so it was terminated.
- Falcon attempt 2: retried with the same command under a 900 second timeout; it timed out and produced no report file.
- Cyberian fallback: `just research-disorder cyberian Sagittal_Sinus_Thrombosis` was run under a 900 second timeout; it also timed out and produced no report file.

Because neither provider produced a generated report or citations file, curation
was grounded manually in fetched PubMed references and validated against the
repository schema and reference workflow.

## Source-backed findings used for curation

- PMID:25073867 supports the clinical presentation spectrum, diagnostic
  confirmation by MR/MR venography or venous CT, risk-factor context, acute
  heparin anticoagulation, selected thrombolysis/thrombectomy, decompressive
  surgery, and post-acute anticoagulation.
- PMID:17183977 supports the two linked pathophysiology patterns: local venous
  infarction with focal signs and global raised intracranial pressure from an
  obstructed venous system.
- PMID:29039017 supports seizure complications, focal neurological deficits,
  bleeding/lobar lesions, and the association of superior sagittal sinus
  thrombosis with secondary seizures in a CVST cohort.
- PMID:38050259 supports the broader CVT epidemiology pattern, variable
  presentation from headache to loss of consciousness, diagnostic difficulty,
  first-line heparin treatment, and generally favorable recovery in many
  patients.
- PMID:39492709 supports contemporary treatment statements: LMWH or
  unfractionated heparin as first-line acute treatment, decompressive
  craniectomy for life-threatening intracranial pressure, and specialist-center
  use of endovascular therapy in complex cases.
- PMID:25899238 supports mechanical thrombectomy as a possible option for
  patients who do not respond to anticoagulation, while preserving uncertainty
  because controlled studies are required.

## Ontology decisions

- Disease term: MONDO:0002695, label `sagittal sinus thrombosis`.
- Location term: UBERON:0001642, label `superior sagittal sinus`.
- Phenotype terms used after OAK verification include HP:0002315 Headache,
  HP:0002516 Increased intracranial pressure, HP:0001085 Papilledema,
  HP:0001250 Seizure, HP:0001269 Hemiparesis, HP:0001342 Cerebral hemorrhage,
  and HP:0001259 Coma.
- Treatment terms use broad but verified actions: MAXO:0000058
  pharmacotherapy with CHEBI:28304 heparin, NCIT:C52003 Thrombectomy, and
  MAXO:0000004 surgical procedure.

## Curation notes

- Category was retained as `Complex`; the literature supports multifactorial
  thrombotic risk rather than a single Mendelian mechanism for the disorder
  page as curated here.
- Evidence snippets in the YAML were copied from fetched reference-cache
  abstracts and kept as direct substrings.
- Unrelated PMIDs fetched during source discovery were not used in the page and
  should not be staged.
