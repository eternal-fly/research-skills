# APS Quantum Writing 1.2.1 validation

Release date 2026-10-28. Baseline is public 1.2.0 commit `1e87420fdecc3463197ba99192142c4cd52b5e54`.

## Change and scope

The author's requested editorial preference applies to narrative main text and supporting material, including appendices and supplementary captions. Sentences use neither prose colons nor explanatory dashes. Genuine heading-to-body dashes remain. Mathematical operators, word hyphens, ranges, citation keys and bibliographic syntax retain their roles. Optional colon-ended secondary headings can be absorbed into the paragraph without redefining the historical typography helpers.

Literature discussion describes existing research or verified authors' recent work and its scientific contribution. Preprint identifiers and publication-status labels leave the narrative while accurate source metadata remains in references. Unknown authors and dates are not invented, old work is not relabeled recent, and a conjecture does not become a theorem. These preferences are distinct from APS journal requirements.

## Fresh behavior applications

Five paired cases produced ten unedited outputs in fresh contexts. They cover English PRL prose, a technical Supplement, Chinese body/supporting prose, incomplete attribution with a bibliography, and principal/secondary/Note added heading roles. Four baseline outputs retain requested literature-wording violations; none of the revised outputs does. All ten were manually read for scientific preservation. Both conditions already removed explanatory punctuation, so no punctuation-effectiveness improvement is claimed.

See the [raw-output review](../evidence/prose-behavior-1.2.1/review.md) and [per-case fingerprints and results](../evidence/prose-behavior-1.2.1/results.json). Five preliminary calls with incorrectly escaped inputs were excluded and all baseline cases rerun after fixture repair. This is a focused synthetic check, not a new full-manuscript benchmark or a statistical efficacy claim.

## Release checks

Actual execution results and environment are recorded in [machine-readable validation](../evidence/public-release-validation-1.2.1.json). The skill suite has 27 methods. The repository builder suite has four methods, representing the same two Git/index/archive regression behaviors for the frozen 1.2.0 and 1.2.1 builders. A repeated run after extraction does not add new test cases.

Run the skill suite from the skill root with `python -B -m unittest discover -s tests -v`. From the repository root, run `python -B -m unittest discover -s scripts -p 'test_build_release*.py' -v`. Stage the exact tested source and build with `python scripts/build_release_1_2_1.py --out dist`. Verify release assets against the external SHA256SUMS and the extracted skill against its internal manifest. The source archive root is `research-skills/`; the installable root is `aps-quantum-writing/`.

The version-specific publication workflow runs the source checks, builds and extracts the package, checks its manifest, and reruns the skill suite. It uploads a draft, downloads and checks the assets, and only then publishes. Check the Actions result for the actual release commit; this procedure is not a substitute for a completed run.

## Preserved historical evidence

The 1.2.0 full-manuscript/Supplement cases and analytic-figure render, 1.1.0 abstract applications, supplied quantum-figure literature ledger, 2026-10-20 five-example REVTeX 4.2f revalidation, and older 29-source/32-assertion typography record were not rerun. Existing examples, licensing and those evidence files are retained unchanged. Current automated bookkeeping and numerical tests do not constitute new literature reads, new plot inspection or a fresh REVTeX compile. No fresh APS-policy review is claimed.
