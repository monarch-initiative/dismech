# Acanthocephaliasis literature sweep

This curation sweep checked recent case reports and the consolidated human
acanthocephaliasis review before creating
`kb/disorders/Acanthocephaliasis.yaml`.

## Sources used

- **PMID:34076470** — open full-text 2021 review of human
  acanthocephaliasis. Used as the main source for the Acanthocephala phylum,
  the dominant documented human agents (*Macracanthorhynchus hirudinaceus*,
  *M. ingens*, and *Moniliformis moniliformis*), arthropod intermediate hosts,
  the egg-to-acanthor-to-acanthella-to-cystacanth cycle, human infection after
  ingestion of cystacanth-infected arthropods or paratenic hosts, the toddler
  exposure skew, proboscis attachment to small-intestinal mucosa, the symptom
  spectrum, attachment-site pathology, adult-worm stool diagnosis,
  concentrated-wet-mount diagnosis in rare patent infections, and the
  unstandardized treatment record.
- **PMID:39979033** — 2024 pediatric *M. moniliformis* case. Used for a recent
  summary of direct arthropod ingestion and the rodent/cockroach-to-human
  cycle, for a case of adult-worm passage in stool after cockroach exposure, and
  for clearance after three 11 mg/kg pyrantel pamoate doses separated by two
  weeks.
- **PMID:17570979** — open full-text Iranian *M. moniliformis* case report.
  Used for the protrusible hooked proboscis, small-intestinal residence in
  incidental human hosts, and proboscis penetration and reattachment as the
  immediate cause of mucosal inflammation, ulceration, and hemorrhage.

## Lump/split decision

`stubs/Acanthocephaliasis.yaml` carried no MONDO descendants and listed only
`helminthiasis` as a parent, so `MONDO:0000295` was curated as a leaf infectious
disease entry rather than as a grouping.

## Exclusions and term decisions

- **Individual agent species** were kept in prose and evidence rather than
  structured as multiple `infectious_agent` records. Acanthocephaliasis is a
  phylum-level human disease caused mostly by three species, but rarer
  *Acanthocephalus*, *Pseudoacanthocephalus*, *Corynosoma*, and *Bolbosoma*
  infections are still within the disease scope.
- **A raccoon host term** was left out because the core mammal/arthropod/human
  cycle is enough to explain the mechanism, and a host list that also named
  raccoon for *M. ingens* but omitted marine whale, pinniped, crustacean, and
  fish hosts would imply a false completeness.
- **Acanthor, acanthella, and cystacanth** were modeled in prose rather than
  bound to OPL because the local OPL cache contains reusable `egg stage` and
  `adult parasitic worm stage` terms but no acanthocephalan-specific larval
  stage terms.
- **Pyrantel pamoate** was bound after `runoak -i ols:chebi search pyrantel`
  returned `CHEBI:8655` Pyrantel pamoate. Levamisole, niclosamide,
  mebendazole, ivermectin, thiabendazole, and piperazine citrate were kept in
  prose because the human treatment record is case-report based and explicitly
  unstandardized; only the pyrantel pattern was structured as a treatment
  because it is the best supported repeated regimen for mild cases.
- **Nausea, anorexia, abdominal distension, ileus, and peripheral
  eosinophilia** were added after review as separate phenotype nodes. HPO's
  canonical label for `HP:0003270` is Abdominal distention, while the entry
  keeps the source spelling in `preferred_term`.
