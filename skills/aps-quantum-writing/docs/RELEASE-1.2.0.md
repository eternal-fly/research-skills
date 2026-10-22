# APS Quantum Writing 1.2.0 validation

Release date: 2026-10-22. Base: published 1.1.0 commit
`36979d40c0023d2dde07b774e1195db86cbf7c0f`. The release integrates the supplied
figure-planning candidate and explicitly extends the same scientific narrative
and direct prose to the main text and supporting material.

## Input and changes

The supplied `aps-quantum-writing-1.2.0-rc1.zip` has SHA-256
`ac7cf4f06e007863a488a529e01feab48daf6e8b2630d1b34af7c4844cf8a0bc`.
All 128 listed file checksums matched. Relative to 1.1.0, the input adds 19
files, changes 10 and omits none. Its original checksum list is retained as
`evidence/rc1-SHA256SUMS`; the 1.1.0 checksum list is also preserved.

The figure branch now starts with the physical comparison, assigns flexible
panel roles and records source data, conditions, uncertainty, text placement
and final-size layout decisions. Twenty-one conditional quantum-task routes
remain supporting references. Single column is the starting preference, with
mechanism, geometry and readability as reasons to use more width. The optional
checker validates record structure, not research truth or visual quality.

The writing branch now states the whole-body path explicitly: central question,
obstacle, key idea, proof or evidence, physical answer. These are reasoning
relationships rather than mandatory sections. Appendices, End Matter,
Supplemental Material and captions retain the same direct scientific style.
Necessary assumptions, uncertainty and negative results remain next to their
inferences; deleted self-defense is not moved to supporting sections.

## Fresh behavior checks

Three fixed synthetic requests were executed with the unmodified rc1 and again
with the revised writing rules, using one fresh agent per case and version.
The result is **six complete compact manuscripts with six substantive
Supplements**. All were read in full against the declared nine-criterion rubric.

- **PRA theory:** collective-noise protection with a retained differential-field
  signal; generator restriction, factor-four decay and phase convention.
- **PRB numerical interpretation:** finite-size/window memory trends; all supplied
  values, SEM meaning, shared-realization covariance and finite-domain conclusion.
- **PRX Quantum method:** exact observable-bias correction, variance cost,
  sufficient concentration bound, fixed calibration mismatch and clipping.

No critical narrative or scientific-boundary failure was found in either arm.
The rc1 baseline was already usable; these cases do not demonstrate an
improvement in performance. Five additional short Supplement passages were
rewritten once without a skill and once with the revised skill. Three control
passages retained unrelated omission lists; all five revised passages retained
their scientific facts while removing such lists. This comparison does not
isolate the incremental effect of the rc1-to-final patch.

See the [full qualitative review and raw outputs](../evidence/maintext-behavior-1.2.0/review.md),
[machine-readable results](../evidence/maintext-behavior-1.2.0/results.json), and
[reusable requests](../tests/maintext-narrative-cases/). These are non-blind,
small, synthetic applications, not a statistical benchmark or new physics.
No real manuscript, novel theorem, spin-chain computation or manuscript TeX
compilation was certified by the prose review.

## Fresh figure execution

One synthetic analytic plot was generated from the estimator case, exported as
an **85 x 76 mm PDF and PNG**, and visually inspected, including the PDF rendered
by Poppler. A misplaced ideal-reference label in the first rendering was moved
next to the dashed R=1 baseline. The final output has readable labels and
markers, no clipping, and a near-square scalar plotting area. Four marked theory
values were checked against the stipulated formula evaluations.

The [source, data, record and visual review](../evidence/figure-smoke-1.2.0/figure-plan.json)
are retained together. This was a manually executed smoke test by the release
integrator, not an independent model benchmark. It exercises one scalar
single-column layout, not the double-column decision or complex device schemes.
No manuscript insertion/TeX rendering or aesthetic comparison was performed.

## Automated checks and portability

The skill's automated suite comprises **27 methods**: six distribution,
two mechanism methods (one file-presence and one numerical-model check),
14 figure-plan structural checks, and five review-bookkeeping/link checks.
The source and extracted-archive runs are recorded in
[public-release-validation-1.2.0.json](../evidence/public-release-validation-1.2.0.json).
Repeated runs are not additional distinct test cases.

The candidate passed in Python UTF-8 mode. Independent review then reproduced
a failure of the ordinary Windows command: the new review-ledger test used the
GBK default to read UTF-8 JSON and failed in setup before running any method.
The four new ledger/source reads and two template reads now specify UTF-8.
The same unmodified ordinary command then ran the five review tests successfully;
the complete suite is rerun for final packaging. The skill-frontmatter check
uses Python UTF-8 mode because the external validator uses a locale-default read.

Independent review also reproduced a local packaging mismatch: the builder
listed Git-index filenames but could package an unstaged root README. The
1.2.0 builder now rejects unstaged tracked changes before writing any archive.
Two separate repository-level regression methods exercise a real clean Git
fixture and an unstaged change. The latter failed before the fix and both pass
after it. These are additional to the 27 skill methods; CI runs both suites.

A new distribution regression also reproduces a false Markdown link detected
inside a TeX dissipator in the raw narrative output. The scanner now excludes
math and code contexts while checking real prose links. The regression passed
after the fix; raw manuscripts remain unchanged.

## Inherited and supplied evidence

- The supplied rc1 records report 432 substantive source revisits and 29 papers
  inspected as pixels. Integration verifies its file hashes and bookkeeping;
  those source reads and image inspections were **not repeated** here. The
  original [rc1 report](FIGURE-REVISION-2026-10-22.md) remains dated rc1 evidence.
- The five-example REVTeX 4.2f audit, 120 checks and PDF inspection were executed
  on 2026-10-20 and are carried forward unchanged. They are not new 1.2.0 runs.
- The historical 29-source/32-assertion heading matrix, 700-paper corpus review,
  and 1.1.0 abstract cases were not rerun for 1.2.0. The earlier 16 abstract
  scenarios are not counted as new successful applications.
- Existing examples and licenses are preserved byte-for-byte. No new official
  APS-policy or reference-paper review, journal-acceptance estimate, broad
  model-success estimate or user-machine installation is claimed.

## Packaging and publication

The frozen 1.2.0 builder requires tracked worktree files to match the index,
checks manifest coverage and file hashes, then reads
every archive member back against the input bytes. The installable ZIP is
extracted and checked separately. The publication workflow binds v1.2.0 to its
own source commit, tests source and extracted files, uploads a draft, downloads
and verifies its checksums, and publishes only after those steps. It refuses to
overwrite an existing release or a different existing tag. A workflow definition
alone is not a successful run; consult the Actions run for the published commit.
