# APS Quantum Writing 1.2.4

Baseline v1.2.3 is commit `150b29f56a660a7f85bde856df480e73eb8444e8». The writing change reduces intervention in sound prose. The figure change makes physical objects, interfaces and the measured observable determine the composition.

## What happened in the writing comparison

Three independent GPT-6.2 Astra sessions received the same two synthetic excerpts in their original languages. One used the task alone, one read the released 1.2.3 guidance, and one read the revised guidance. Each condition ran once. [Task](../evidence/astra-writing-1.2.4/writing-task.md) · [Task alone](../evidence/astra-writing-1.2.4/control.txt) · [1.2.3](../evidence/astra-writing-1.2.4/baseline.txt) · [1.2.4 candidate](../evidence/astra-writing-1.2.4/revised.txt)

| Passage | Task alone | 1.2.3 | 1.2.4 candidate |
|---|---|---|---|
| A measured null at 4 K | Retained the value, standard error, citation and null finding. Rephrased the closing sentence. | Kept both sentences verbatim. | Kept both sentences verbatim. |
| A finite-chain simulation with two speculative closing sentences | Retained the three lengths and matched readout dimension. The evidence type became implicit. | Retained those conditions and identified the simulation. The independent comparison at each length became implicit. | Stated the simulation and independent comparison at each length. Kept all three lengths, the matched dimension and the direction of the mean-error result. |

All three omitted the unstudied device and scale extensions in the Chinese passage. These observations motivate a short read for meaning, especially when an affirmative closing sentence points beyond the evidence. Two excerpts and a single run per condition give no estimate of an average model effect.

## Figure checks

Ten source pages were reopened and visually inspected. The palette table gives the figure numbers, page numbers, editions and links. Four sources are APS versions of record and six are author manuscripts. The HEX values are the author's approximate samples. In the first figure FNO denotes a Fourier neural operator applied to Floquet dynamics. [Source figures and palette roles](../references/schematic-palettes.md)

The public example is a new two-spin model at 85 × 63 mm. Its circuit and time trace share a page. The position of the interaction, the reset return and the meter are readable in the color and grayscale PDF proofs. Gate fills cover the wires behind their labels. Open circles with dashes and filled squares with a solid line distinguish the traces at column width. The PDF embeds its fonts and the SVG retains vector objects and text. A separate pure-state calculation conditions on the most recent reset and checks the plotted density-matrix recurrence for both displayed probabilities and complete reset. [Figure, caption and source](../assets/schematic-examples/README.md)

## Reproduction and scope

In the extracted skill, run `python -B -m unittest discover -s tests -v». From the repository root, run `python -B -m unittest discover -s scripts -p 'test_build_release*.py' -v». Build with `python scripts/build_release_1_2_4.py --out dist» and verify the external and internal SHA256SUMS. Environment details and executed checks are in the [validation JSON](../evidence/public-release-validation-1.2.4.json).

The earlier full-manuscript and Supplement cases, journal profiles, broad paper review and REVTeX compilation keep their original scope and dates. The five-source REVTeX 4.2f revalidation and the historical 29-source, 32-assertion matrix are documented in the [validation history](VALIDATION.md).
