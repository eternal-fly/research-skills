# Usage guide

## Supply the scientific material

For a full manuscript, provide the intended audience, target journal and article type, core model or experiment, definitions, derivations, numerical/experimental data, trustworthy references, and any existing draft. State the working language and relevant constraints. The agent should use what is available and ask only about gaps that block a scientific conclusion or an authorized action.

The workflow is continuous: background and research context → journal/type → central question and claim → conceptual-unity check → outline and working title → evidence/figure plan → draft → title/abstract revision → compile and inspect → substantive assessment. It resumes from the current state; it does not restart all stages for a paragraph edit.

## Full-manuscript prompt

```text
Use aps-quantum-writing for this manuscript, targeting Physical Review X.
Use the supplied derivations and data as the factual source of truth.
First state the single scientific question and the evidence needed to answer it.
Plan an outline and figure set around that question, then continue drafting.
Keep mathematically distinct results only when their role in the answer is clear.
Finish with a conceptual-unity assessment and a concrete revision priority.
```

A good result is a readable argument with traceable evidence, not a list of every theorem available. Complementary measurements or independent theoretical bounds may belong together even without a direct theorem-to-theorem dependency.

## Theory and proof exposition

```text
Rewrite this proof so a physicist can follow why each step is needed.
Introduce the question, obstacle, and useful construction before technical lemmas.
Define each symbol at first use. Give a small example where it improves understanding.
Preserve the assumptions and proof strength; separately verify the dependency graph.
```

The reader's order of understanding need not equal the order in which lemmas were first proved. Avoid circular reliance even when the exposition presents a main idea before its technical justification.

## Natural academic prose

```text
Improve this section's clarity and rhythm while preserving its scientific meaning.
Use standard terms, concrete subjects, and direct statements of the conditions
under which the result applies. Remove unnecessary commentary about work not done.
Keep genuine uncertainty, relevant counterexamples, and negative findings accurate.
```

This is not an authorship-detector evasion tool. Natural prose comes from precise meaning, logical transitions, selective emphasis, and revision. Do not invent a personal voice, evidence, limitations, or claims of novelty.

## Data-figure prompt

```text
Design figures from these data to test the paper's central claim.
For each panel, state the scientific question, observable, comparison, units,
uncertainty treatment, and source. Select the plot type accordingly.
Render at final publication size; inspect tick labels, y-axis-label extent,
bottom-label centering, aspect ratio, legends, and shared panel alignment.
Provide editable source, final exports, and a stand-alone caption.
```

Use curves for dependence, scatter plots for relationships, distributions for variability, heat maps for two-dimensional structure, and tables for compact exact comparisons when appropriate. Match chart type to what the reader needs to judge. Do not generate synthetic points to fill missing research data.

## Scientific-schematic prompt

```text
Build a compact, information-dense scientific schematic for this method.
Show the actual relevant components and their internal structure, not three generic boxes.
Label what each arrow carries. Distinguish training, inference, feedback,
calibration, and frozen parameters wherever they occur in the method.
Use recognizable model/device structures, a restrained functional color system,
and readable labels at final size. Verify the science as well as the composition.
```

A neural-network diagram is useful only when the architecture matters; a hardware inset is useful only when the physical implementation matters. Detail earns space by explaining a mechanism, interface, or condition. Dense does not mean crowded.

## Heading and layout prompt

```text
Audit this PRA Letter for heading microtypography.
Preserve the author's chosen heading names and unheaded sections.
Route by journal, article type, and heading role. Check the rendered PDF for
run-in versus display structure, font, numbering, punctuation, and natural wrapping.
Check acknowledgments, data availability, and appendix roles separately.
```

Use [microtypography](../references/microtypography.md) and the [five-page preview](../assets/heading-examples/APS-heading-layout-examples.pdf). Current PRL main labels use an em dash; other Letters' selected labels use a period. A long run-in label may wrap naturally. An explicitly forced paragraph break after the label is a different issue.

## Final scientific assessment

Ask for the central question in one sentence, the assumptions → result → significance of major contributions, and the technical or complementary role of each. Apply deletion and split tests, distinguish novelty from importance, assess whether an oracle/toy model represents the claimed problem, and compare the title/abstract with the actual evidence.

The final assessment should assign A–D conceptual unity, give the reader's one-sentence takeaway, decide whether the manuscript principally solves an important problem or displays provable results, and prioritize the next revision. Journal positioning requires current comparisons and concrete evidence; theorem count, proof difficulty, or crowded keywords are not proxies.

## Deliverables and boundaries

Keep the manuscript's organization appropriate to its journal; do not impose one file per section. Retain editable figure sources, data provenance, build instructions, and a concise record of what was actually compiled or visually checked. A source edit, a successful export, and a visually accepted page are different milestones.

Use this project within [its license](../LICENSE). Private local changes are permitted for authorized use. Public modifications, repackaging, and commercial uses require the specified permission. Research manuscripts and figures are covered by the separate output clause, not automatically relicensed as this skill.
