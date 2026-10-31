# APS Quantum Writing 1.2.2 validation

Release date 2026-10-31. The source baseline is the refreshed 1.2.1 commit `46a0ffdbedaaf934f6ad98186981f2b1ebf74d93`.

## Change and scope

The author requested that manuscript prose omit statements of what the paper does not claim, unresolved extensions and operations not performed. The correction applies to related work and first occurrences as well as repeated disclaimers. Passive unresolved-status wording, incomplete-validation statements, default future-work promises and moving the same caveat into Supplemental Material do not satisfy the rule.

The actual method, evaluation design, assumptions, evidence type and physical result determine the scope of the affirmative claim. Genuine measured failures, null results, counterexamples and uncertainty remain. A required final pass covers the abstract, main text, captions, conclusion, appendices and Supplemental Material. These are editorial preferences, not new APS requirements.

## Focused comparison executed before the version bump

On 2026-10-31, three fresh agent contexts each edited the same bundle of three passages under one of three conditions. The baseline was the pre-correction installed 1.2.1 snapshot. The revised condition used the corrected source instructions while VERSION still read 1.2.1. No additional model calls were made merely to label the package 1.2.2.

| Condition | Bundled passages | Passages retaining targeted defensive wording |
|---|---:|---:|
| No-guidance control | 3 | 3 |
| Original installed 1.2.1 | 3 | 1 |
| Revised instructions | 3 | 0 |

All nine outputs were manually read. The revised outputs retained supplied assumptions, evaluation scope and evidence type, the citation key, an explicit mathematical counterexample and a measured null result with uncertainty. There was one repetition per condition. The passages within one context are not independent repetitions, and these observations are not a statistical efficacy estimate or a fresh whole-manuscript test.

Two fixtures were synthetic. One included private manuscript material supplied by the author. The raw fixtures and unedited outputs are retained locally rather than distributed; the public JSON contains aggregate counts and source/output fingerprints. This public record alone cannot reproduce the private comparison. The public direct-prose guide contains a separate synthetic example for applying the rule.

## Release checks and reproduction

See [machine-readable validation](../evidence/public-release-validation-1.2.2.json) for execution status and environment. The skill suite has 27 methods. The builder suite has six methods, representing the same two Git/index/archive behaviors for frozen 1.2.0, 1.2.1 and 1.2.2 builders. Rerunning the skill suite after extraction does not add new test cases.

From the skill root, run `python -B -m unittest discover -s tests -v`. From the repository root, run `python -B -m unittest discover -s scripts -p 'test_build_release*.py' -v`. Stage the intended source and build with `python scripts/build_release_1_2_2.py --out dist`. Check the external SHA256SUMS and the extracted skill's internal manifest. The installation archive has root `aps-quantum-writing/`; the source archive has root `research-skills/`.

The publication workflow runs the source and extracted-package checks, creates a draft release, downloads its assets and verifies their checksums before publishing. Check the Actions result for the actual release commit. Workflow source is a procedure, not evidence of a completed CI run.

## Preserved historical evidence

The 1.2.1 punctuation/literature applications, 1.2.0 full-manuscript/Supplement cases and analytic-figure render, 1.1.0 abstract applications, literature and figure-image reviews, 2026-10-20 five-example REVTeX 4.2f revalidation and older 29-source/32-assertion typography record were not rerun for 1.2.2. Their files retain their original bytes and dates. New automated bookkeeping and numerical checks do not constitute a fresh visual audit or literature review.
