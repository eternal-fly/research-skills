# Validation and reproducibility

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

## Current English-release checks

The untranslated baseline failed the new distribution checks as expected: Chinese instructions and missing public documentation/provenance were detected. The release process then translated the active rules, supplied public documentation, and reran the checks. Final results are recorded in [release validation](../evidence/public-release-validation.json).

The numerical tests were rerun in Python 3.12.14 with NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8. Both example-generation scripts completed in a new output directory and produced 24 output files. These versions document an observed environment, not minimum supported versions or a guarantee for every platform.

All 26 input PDF, PNG, and EPS assets matched their verified input bytes before selection. The public package retains 21 unchanged PDFs/PNGs and omits five redundant EPS exports, which the supplied scripts can regenerate. Text captions were translated separately. This confirms preservation, not that each older figure now exemplifies every later layout preference.

## Inherited heading verification

The original 1.0 audit compiled 29 standalone TeX sources twice. Four intentionally invalid-option controls still generated PDFs while emitting warnings; they are not supported journal configurations. Thirty-two font, baseline, punctuation, and guard checks passed. Five portable example sources were rebuilt and their final pages visually inspected.

The English edition retains the same five-page heading PDF and sources. The current packaging environment did not provide a discoverable REVTeX class, so those historical TeX results are recorded as inherited, not claimed as a fresh compile in this environment. Use the [heading README](../assets/heading-examples/README.md) to rebuild in a working LaTeX installation.

The helpers cover explicit run-in labels and an opt-in Regular third-level font preview. They do not reproduce proprietary publisher fonts, certify article length, or implement a publisher-identical PRL End Matter container. Consult [microtypography](../references/microtypography.md) for these boundaries and the official/observed Letter DAS distinction.

## Behavioral review

Review scenarios include independent complementary results versus theorem collage, optional PRL headings, Note added punctuation, Letter versus Regular typography, appendix-level fonts, complete scientific schematics, y-axis versus bottom-label alignment, motivated proofs, and missing-data integrity. The qualitative English-release review is summarized in the validation JSON. It is not a statistical model benchmark or a journal-acceptance prediction.

## Release archive and installation smoke test

The distributable ZIP contains one top-level `aps-quantum-writing` folder. Release preparation extracts it into a fresh temporary directory, checks the entry and relative resources, and runs the complete test suite there. SHA-256 checksums identify the released ZIP and preview PDF.

Repository CI runs the automated suite; its result must be checked for the actual published commit. A workflow file existing in the repository is not evidence that CI has passed.
