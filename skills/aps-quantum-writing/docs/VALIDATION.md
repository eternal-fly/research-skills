# Validation and reproducibility

For the current 1.2.1 release, see [the release report](RELEASE-1.2.1.md) and [machine-readable validation](../evidence/public-release-validation-1.2.1.json). The [1.2.0 report](RELEASE-1.2.0.md), [1.1.0 report](RELEASE-1.1.0.md), supplied rc1 review records and original 1.0.0 record remain dated historical evidence. The sections below retain their original execution context.

The subsequent [same-version short-format refinement](PROSE-FOLLOWUP-2026-10-28.md) has its own source-validation record. It does not rewrite the v1.2.1 release report or imply that the original release archives contain the later wording.

## What is tested

The English edition is a translation and public-packaging pass on the existing 1.0 skill. It does not claim that translating the documentation reran the literature review or every historical visual experiment.

The release checks distinguish:

1. **Distribution:** English active instructions, required documents, local Markdown targets, unique balanced DOI metadata, and the three primary branches.
2. **Numerical examples:** the bundled two-mode model's poles, response, time evolution, dissipation, and figure-size arguments.
3. **Behavior:** scenario-based use of the English instructions, compared with the source rules.
4. **Visual assets:** preserved artifact identity and manuscript-specific checks described in the figure branch.

Run the complete automated suite from the skill root:

```sh
python -m unittest discover -s tests -v
```

## English-release checks (2026-10-09)

The untranslated baseline failed the new distribution checks as expected: Chinese instructions and missing public documentation/provenance were detected. The release process then translated the active rules, supplied public documentation, and reran the checks. Final results are recorded in [release validation](../evidence/public-release-validation.json).

The numerical tests were rerun in Python 3.12.14 with NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8. Both example-generation scripts completed in a new output directory and produced 24 output files. These versions document an observed environment, not minimum supported versions or a guarantee for every platform.

All 26 input PDF, PNG, and EPS assets matched their verified input bytes before selection. The public package retains 21 unchanged PDFs/PNGs and omits five redundant EPS exports, which the supplied scripts can regenerate. Text captions were translated separately. This confirms preservation, not that each older figure now exemplifies every later layout preference.

## Inherited heading verification

The original 1.0 audit compiled 29 standalone TeX sources twice. Four intentionally invalid-option controls still generated PDFs while emitting warnings; they are not supported journal configurations. Thirty-two font, baseline, punctuation, and guard checks passed. Five portable example sources were rebuilt and their final pages visually inspected.

The English edition retained the same five-page heading PDF and sources. The 2026-10-09 packaging environment did not provide a discoverable REVTeX class, so those historical TeX results remain recorded as inherited, not as a fresh compile during release packaging.

## Independent five-example revalidation (2026-10-20)

The exact v1.0.0 sources were subsequently compiled with official REVTeX 4.2f and pdfTeX 1.40.24. All five public examples passed two compilation passes, 120 newly defined PDF/log checks, and full-page visual inspection. A clean replay of the final reproduction script also passed. No TeX fixes were needed. See the [detailed report](HEADING-REVALIDATION-2026-10-20.md), [machine-readable record](../evidence/heading-revalidation-2026-10-20.json), and [reproduction evidence bundle](../evidence/heading-revalidation-2026-10-20.zip).

This fresh result does not rerun or replace the historical 29-source/32-assertion matrix or its invalid-option controls. The original release-validation JSON remains unchanged as a dated metadata record. Its reported seven distribution and two numerical tests must not be confused with the checked-in v1.0.0 suite, which contains five distribution methods and two mechanism methods, seven total. See the heading report for this distinction and the current release report for newly executed checks.

The helpers cover explicit run-in labels and an opt-in Regular third-level font preview. They do not reproduce proprietary publisher fonts, certify article length, or implement a publisher-identical PRL End Matter container. Consult [microtypography](../references/microtypography.md) for these boundaries and the official/observed Letter DAS distinction.

## Behavioral review

Review scenarios include independent complementary results versus theorem collage, optional PRL headings, Note added punctuation, Letter versus Regular typography, appendix-level fonts, complete scientific schematics, y-axis versus bottom-label alignment, motivated proofs, and missing-data integrity. The qualitative English-release review is summarized in the validation JSON. It is not a statistical model benchmark or a journal-acceptance prediction.

## Release archive and installation smoke test

The distributable ZIP contains one top-level `aps-quantum-writing` folder. Release preparation extracts it into a fresh temporary directory, checks the entry and relative resources, and runs the complete test suite there. SHA-256 checksums identify the released ZIP and preview PDF.

Repository CI runs the automated suite; its result must be checked for the actual published commit. A workflow file existing in the repository is not evidence that CI has passed.
