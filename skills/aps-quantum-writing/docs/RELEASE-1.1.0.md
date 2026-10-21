# APS Quantum Writing 1.1.0: integration and validation

Prepared 2026-10-21. This release integrates the user-supplied Abstract Narrative
Revision 3 into the existing English skill. WRITING owns the new abstract guide;
PLANNING and the seven journal references route to it. There are still three
top-level branches. License terms, scientific figure assets, and TeX helper
content are unchanged.

## Source integration

The 15 supplied skill files were checked against the attachment manifest.
All 20 attachment checksums matched. For the 12 existing files, the supplied
baseline fingerprints differed from the repository: reconstruction of the
supplied patch established that, after LF normalization, each supplied baseline
had exactly one extra terminal newline. No substantive baseline conflict was
found. The merge normalizes redundant terminal blank lines and dates the new
guide as part of 1.1.0.

The supplied evidence ledger reports 29 reviewed abstracts and seven explicit
links to the inherited corpus. Those readings are attributed to the supplied
supplement; they were not independently repeated during release integration.
The 16 acceptance scenarios are editorial test material, not 16 recorded model
successes. No private manuscript or conversation is included.

## Checks executed for this release

- Full existing automated suite: **7/7 passed** in Python 3.11.7 with NumPy
  1.26.4, SciPy 1.16.0, and Matplotlib 3.8.0. This comprises five distribution
  tests and two `MechanismTests` methods (one file-presence check and one
  substantive numerical-model test). Do not describe this as seven distribution
  tests plus two new numerical tests.
- Skill frontmatter/name validation: passed with the skill-creator validator
  using Python UTF-8 mode. The first attempt using Windows' legacy default text
  encoding could not decode the skill; the successful run used `-X utf8`.
- Ten synthetic abstract drafts: five one-shot baseline requests and the same
  five requests in a separate fresh evaluation of the revised skill. All ten
  were manually reviewed for supplied facts, core method/reasoning, and evidence
  boundaries. No critical violation was found. Both runs produced usable
  drafts; these observations do **not** establish an improvement rate or a
  statistical A/B result. The revised run followed the dedicated guide and
  preserved PRA Letter finding-before-detail ordering. See the
  [qualitative review](../evidence/abstract-behavior-review-1.1.0.md).
- Release packaging verifies internal file coverage and SHA-256, then reads back
  every archive member against the source bytes. The extracted installable ZIP
  is tested separately. The dated [validation record](../evidence/public-release-validation-1.1.0.json)
  records actual completed checks. Release asset checksums cover both ZIPs, the
  original preview PDF, and the public heading evidence bundle.

The publication workflow reruns the tests on the release commit and the extracted
skill, uploads a draft, downloads the uploaded assets, verifies their checksums,
and only then makes the release public. A workflow's existence is not a passing
CI result; consult its actual run for the published commit.

## Official guidance rechecked during integration

The [PRA author page](https://journals.aps.org/pra/authors) still directs Letter
abstracts to the [2023 editorial](https://journals.aps.org/pra/edannounce/10.1103/PhysRevA.107.010001).
Its requested sequence places the finding before work details. This specific
instruction is retained without generalizing it to all APS articles.

The [PRX Quantum author page](https://journals.aps.org/prxquantum/authors) assigns
the approximate 150-word recommendation to the Popular Summary, not the
technical abstract. The [February 2026 style guide](https://res.cloudinary.com/apsphysics/image/upload/APS_Journals_Style_Guide_Authors022326_guzwhx.pdf),
printed page 11, was downloaded and read: it indeed states the PRL 600-character
limit. The supplement's conflict with observed abstracts remains explicit; this
release does not resolve it or certify submission-length compliance. Other
journal rules and the 29 sampled abstracts were not comprehensively reread.

## Heading evidence carried into 1.1.0

The [independent 2026-10-20 audit](HEADING-REVALIDATION-2026-10-20.md) compiled all
five public examples twice with official REVTeX 4.2f, passed 120 newly defined
checks, and inspected five fresh pages; its clean replay also passed. This
earlier completed audit is carried into 1.1.0, not represented as a new
2026-10-21 compilation. The original 29-source matrix, 32 assertions, and four
invalid-option controls remain inherited and were not rerun.

The public evidence bundle was prepared on 2026-10-21: only local prefixes in
text logs were replaced with placeholders. The exact inputs used by the Windows
checkout had CRLF endings; their text equals the tag's LF sources. This
checkout conversion was the only source-byte difference. PDFs, PNGs, and check
results are retained, and the public bundle has its own hash manifest. The raw
local audit is preserved separately. The official REVTeX archive can be
obtained from its recorded URL and verified against its SHA-256.

The original 1.0.0 validation JSON and frozen checksum manifest remain historical
records. The skill-root `SHA256SUMS` now describes 1.1.0. Figure generation,
the full historical source review, acceptance probabilities, and unpublished
manuscript correctness are not validated by this release.
