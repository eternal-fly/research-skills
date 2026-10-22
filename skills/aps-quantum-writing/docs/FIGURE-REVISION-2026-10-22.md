# Figure-planning revision 1.2.0-rc1

Prepared 2026-10-22 from public 1.1.0 commit
`36979d40c0023d2dde07b774e1195db86cbf7c0f`. This is a complete review package,
not a GitHub publication, installation, or automatic replacement of a user's
customized skill.

## Changes

- Physical discrimination comes before assigning flexible panel roles. The
  roles organize available evidence rather than require all role types.
- A fixed figure/panel record unifies claim, conditions, comparison, provenance,
  uncertainty, scientific challenge, semantic mappings, manuscript placement
  and layout decision. Existing records can be linked instead of duplicated.
- Twenty-one conditional quantum-task routes are grouped into many-body (8),
  information/computation (7), and devices/learning (6). They are loaded only
  when relevant and have source-linked observations and counterexamples.
- Single column is the starting preference. Essential mechanism/comparison,
  scientific geometry and final-size readability can justify double column.
  Near-square scalar plotting areas and their scientific exceptions remain.
- An optional dependency-free JSON record checker catches absent fields,
  explicit unresolved placeholders in `ready` records, missing/mock evidence,
  duplicate panel IDs and inconsistent column assessments. It neither opens
  data sources nor judges scientific truth or rendered appearance.

All new instructions and code are independently authored. The earlier public
comparison informed general workflow ideas; no third-party implementation or
prose is incorporated. Existing author attribution, license, figure assets,
abstract guidance and TeX helpers are retained.

## Source-review scope

The [fresh review](../evidence/quantum-figure-review/README.md) screened the existing
700 records and substantively revisited 432 original sources: 428 selected local
inference chains and 4 complete main texts. Another 74 excerpt screens and 3
limited definition reads are explicitly not substantive rereads; 191 remained
metadata-only. Pixels were inspected for 29 papers. This is neither 700 new
full-paper reads nor a census of visual practice. The active guides cite 106
substantively reviewed sources. Publication versions and review extents are
retained per paper.

## Validation boundary

The original seven automated tests passed on the unmodified baseline. New tests
exercise the optional record checker and provenance bookkeeping. An independent
source-level review found two validator defects (oversized JSON integers and
unresolved template sentinels passing readiness), plus a missing explicit
journal/article-type field; all were corrected with regression tests.

Final executed results are recorded in [validation.json](../evidence/quantum-figure-review/validation.json).
The test classes distinguish distribution integrity, the existing illustrative
numerical model, record structure and evidence-link consistency. Passing these
checks does not establish improved writing/plotting behavior, actual research
validity, a successful model benchmark, or final-size quality of a new figure.

No new manuscript or scientific figure was generated in this revision. Existing
figure/heading assets are retained and compared byte-for-byte to the baseline;
older compilation/visual reports remain historical, not rerun claims. No new
TeX compilation, empirical aesthetic comparison, four-skill benchmark or
acceptance-probability evaluation is implied.

The complete ZIP is extracted and checked separately. Internal hashes identify
its source files; the external checksum identifies the ZIP. The original
historical release records remain unchanged.
