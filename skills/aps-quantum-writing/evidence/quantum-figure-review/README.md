# Quantum figure-planning reread: scope and evidence boundaries

Date: 2026-10-22. Baseline: APS Quantum Writing 1.1.0, repository commit
`36979d40c0023d2dde07b774e1195db86cbf7c0f`. This review reused the existing
700-DOI index as a sampling frame, not as proof of new reading.

## Actual coverage

- 700 existing metadata records screened, 100 per journal; no new papers were silently substituted.
- 604 primary-source files/HTML sources accessed in this pass; access is not reading. One typeset article was read from an author-hosted university copy, with matching title, DOI and publication date verified; the source is labeled explicitly.
- 432 papers received substantive fresh review: 428 targeted local inference-chain reads and 4 complete main-text reads.
- 74 additional papers received clipped-caption/excerpt screening only. They are not counted among the 432.
- 3 received limited definition/geometry reading, also excluded from the 432.
- 191 remained metadata-only in this pass.
- Actual rendered-page pixels were inspected for 29 distinct papers. This does not mean every figure in those papers was inspected.
- 106 distinct papers are cited as support or layout examples in the active recipe guides. Every cited record has substantive review, but not every reviewed paper generates a separate rule.

| Journal | Targeted local inference | Complete main text | Excerpt-only | Limited definition | Metadata-only |
|---|---:|---:|---:|---:|---:|
| PRL | 29 | 1 | 0 | 0 | 70 |
| PRA | 100 | 0 | 0 | 0 | 0 |
| PRB | 69 | 3 | 0 | 3 | 25 |
| PRX Quantum | 100 | 0 | 0 | 0 | 0 |
| Physical Review Applied | 45 | 0 | 40 | 0 | 15 |
| PRX | 49 | 0 | 0 | 0 | 51 |
| Physical Review Research | 36 | 0 | 34 | 0 | 30 |

A **targeted local inference-chain read** covers selected complete relevant
captions and associated results, conditions and interpretive/limitation passages,
or a selected analytical result/discussion where figures are inapplicable.
Coverage varies by paper and is recorded. It is not a complete-paper read, a
complete derivation audit, or reading of every figure and appendix. The four
complete-main-text reads likewise do not imply comprehensive supplement review.
Some targeted reads use the complete figure-referencing paragraphs most relevant
to the chosen claim rather than every paragraph mentioning the figure. Counts
must retain this limited scope.

Initial clipped caption catalogs were used only to select passages; they were
upgraded to substantive status only after the selected full local context was
read. No historical `main_text_reviewed` flag was used as evidence of new work.
No claims of reproducing published scientific results or checking every proof
are made. This was an AI-assisted source review, not an independent human expert
certification or a controlled model-effectiveness study.

## How the sources support the recipes

1. Start from a physical claim and plausible alternative interpretation.
2. Inspect which observables, controls, definitions, costs and limitations the
   selected original-paper passages connect to that inference.
3. Compare multiple sources and retain counterexamples: conditional quality
   without yield; QFI without achieved readout; finite-size behavior without a
   controlled limit; spectra/proxies without sufficient certification.
4. Write a conditional evidence route rather than copy a paper's figure order,
   impose a panel quota, or infer a field-wide frequency from the sample.
5. Use pixel inspection, not captions, for claims about a particular layout.

The single-column-first preference and fixed planning fields are design choices
requested for this skill. Inspected layouts test exceptions; they do not prove
that single column is empirically optimal or required by APS. Several source
papers use author-manuscript layouts. Their version is retained explicitly and
must not be silently interpreted as publisher typography.

## Files and audit use

- [ledger.json](ledger.json): all 700 identities with current status, exact source/version,
  read extent, original observations, limitations and image-inspection locators.
- [coverage.csv](coverage.csv): compact per-paper coverage table.
- [coverage.json](coverage.json): counts derived from the normalized records.
- [sources.md](sources.md): readable notes for the 106 sources linked by active recipes.

Page locations refer to the retrieved PDF's one-based page number unless the
record specifies another convention. HTML reviews use section/figure labels.
A source-file hash, when present, identifies fetched bytes only; it does not
prove a review's quality. No downloaded papers, extracted article bodies,
copyrighted source figures, screenshot/contact sheets, private research inputs,
credentials or local execution paths are included in this evidence export.

The historical 700-paper provenance and the 2026-10-21 abstract review remain
separate records. This review does not rewrite their scope or convert any old
unread placeholder into a claimed historical reading.
