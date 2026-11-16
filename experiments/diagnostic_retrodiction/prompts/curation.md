<!-- Time-sliced curation prompt for `claude -p` (DRAFT, to be frozen). One session per
     replicate, in an isolated worktree (README, *Curation protocol*).
     Placeholders: {DISPLAY_NAME}, {CUTOFF_DATE}, {CUTOFF_YEAR}, {ENTRY_PATH}, {PACKET_DIR}. -->
Curate a new dismech knowledge-base entry for {DISPLAY_NAME} as it could have been written on
{CUTOFF_DATE}, and save it to {ENTRY_PATH}.

Rules:
- Your only literature is the packet in {PACKET_DIR}: abstracts.jsonl (one record per line: pmid,
  date, title, abstract) and packet.tsv. Search it with Grep and read it with Read. Every
  evidence item must cite a PMID from the packet, with a snippet quoted exactly from that
  record's abstract.
- Do not use anything you know from after {CUTOFF_YEAR}. Name mechanisms, phenotypes and
  molecules only as the packet names them.
- Do not search the web, fetch URLs, or read files outside this worktree. Do not run inline
  interpreters (python -c and the like).
- Follow the repository's CLAUDE.md for the entry's schema and ontology bindings. Read term
  labels from the local caches; never write an identifier from memory.
- Build the pathograph: pathophysiology nodes with causal downstream links, phenotypes, and any
  biochemical findings the packet reports. Give every pathophysiology node evidence.
- Do not add has_subtypes. Do not add a diagnosis section for tests that the packet does not
  describe.
- When the entry is written, run `just validate {ENTRY_PATH}` and fix what it reports.

Finish by printing DONE and the entry path.
