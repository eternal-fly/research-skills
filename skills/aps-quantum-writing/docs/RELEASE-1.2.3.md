# APS Quantum Writing 1.2.3 validation

Release date 2026-11-17. Baseline is published 1.2.2 commit `b79de024d971ddd312f1f22248294043137f69fe`.

## Supplied revision and integration

The author supplied `aps-quantum-writing-1.2.2.zip` and `research-skills-1.2.2-source.zip`. Both contained the same 194-file skill, with 193 valid internal checksum entries; the source archive contained 212 files. The new release assigns version 1.2.3 to distinguish this revision from the previously published 1.2.2 assets.

Three reference files contain substantive changes, retained byte-for-byte from the supplied skill. Natural-prose guidance develops varied sentence and paragraph structures and concrete explanations of cross-disciplinary concepts. The Physical Review Applied profile emphasizes early metric motivation and physical mechanisms. Direct-prose guidance distinguishes inference-determining conditions from exhaustive reproducibility records. These changes preserve the existing author-selected punctuation and nondefensive-writing conventions.

Thirty-eight additional files differ only through LF/CRLF conversion. Their original released bytes are retained, including shell helpers, TeX examples, historical raw outputs and older manifests. The supplied manifest is regenerated to cover the actual integrated release. Input hashes, the three imported paths and the line-ending-only paths are recorded in [machine-readable validation](../evidence/public-release-validation-1.2.3.json).

## Executed checks and reproduction

Execution status and dependency versions are recorded in the validation JSON. The skill suite contains 27 methods. The builder suite contains eight methods, applying the same two Git/index/archive behaviors to frozen 1.2.0, 1.2.1, 1.2.2 and 1.2.3 builders. The extracted-package suite repeats the same 27 methods rather than adding new cases.

From the skill root, run `python -B -m unittest discover -s tests -v`. From the repository root, run `python -B -m unittest discover -s scripts -p 'test_build_release*.py' -v`. Stage the intended source and build with `python scripts/build_release_1_2_3.py --out dist`. Check the external SHA256SUMS and the extracted skill's internal manifest. The installable root is `aps-quantum-writing/`; the complete source root is `research-skills/`.

The versioned publication workflow runs source tests, builds and extracts the package, checks the internal manifest, repeats the skill tests, uploads a draft release and verifies downloaded assets before publication. The Actions result for the release commit records whether that workflow actually completed.

## Validation scope

This release performs source integration, automated regression checks and package validation. It does not add a model-behavior run, whole-manuscript application, visual figure review, literature review or TeX compilation. All existing behavioral records, figure examples, literature evidence, the 2026-10-20 five-example REVTeX 4.2f revalidation and the older 29-source/32-assertion typography matrix remain inherited with their original dates and bytes. Passing distribution and numerical tests does not establish general writing effectiveness.
