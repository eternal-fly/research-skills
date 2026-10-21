# Manuscript-format reference: titles, abstracts, figure placement, and column layout

Treat the paper title and section headings separately. Whether section headings appear and what they are called follow the argument. Once chosen, use `journal + article_type + heading_role` in [Heading microtypography](microtypography.md) to check typeface, numbering, run-in versus displayed placement, and punctuation. Handle acknowledgments, the Data Availability Statement (DAS), and appendices according to their own roles.

This reference belongs to the [PLANNING branch](branch-planning.md). Load it only when work on the title/abstract, formatting, or whole-manuscript assembly requires it; it is not a fourth branch. For the scientific narrative, see [WRITING](branch-writing.md); for panel selection and visualization, see [FIGURES](branch-figures.md). Layout serves the argument and the actual journal rules.

## First choose the target and article type

Consult [APS article types and REVTeX](aps-format.md) for the target: PRL Letter; Regular Article or Letter in PRA, PRB, Physical Review Applied, or Physical Review Research; or PRX/PRX Quantum Research Article. Handle each type's length and additional materials separately. Do not automatically offer a Letter route for PRX. Check the current official journal page and [Length Guide](https://journals.aps.org/authors/length-guide), and record the date; existing checks are only a starting point. The introduction length, reference count, and figure layout of observed papers are not submission limits.

## The narrative jobs of the title and abstract

For abstract drafting or revision, read [Abstract narrative](abstract-narrative.md): route by journal, article type, and contribution; connect the supported physical answer to its evidence and meaning; check both sentence continuity and the whole argument. This format reference controls presentation; the dedicated writing reference controls the scientific narrative.


The title should foreground the actual subject and central relationship or finding, distinguishing a physical mechanism from a method name. Avoid vague importance claims and unsupported universality or priority. When useful, offer a small number of substantively different candidates rather than a list of synonymous rewrites.

The abstract should stand on its own: state the necessary element of the problem or context, the main answer, the key means of obtaining it, and its physical significance. Let the research type determine the content; do not impose a fixed sentence count. An abstract condenses established results, whereas an introduction develops the reasoning from prior work to the unresolved problem. Retain the conditions, nature of the evidence, and credible orders of magnitude needed to understand the main result. A standard APS technical abstract is a single paragraph without displayed equations, tables, or numbered citations; check the official page for article-specific requirements. Write the PRX Quantum Popular Summary separately rather than relabeling the technical abstract.

Propose a provisional working title after the outline. After completing the first full draft, rewrite the title and abstract around the actual main result, then check them against the introduction, conclusion, and captions. Confirm that the title, abstract, promises in the introduction, and conclusion point to the same central physical proposition. If the abstract only lists methods, restore the actual answer; if the answer has not been established, rhetoric must not fill the gap.

## Sketch the spatial plan for the whole manuscript first

Before detailed figure production, sketch the relative placement of the main argument, key equations, figures and captions, necessary tables, and references/End Matter. Leave room for the introduction to develop the problem and closest literature, and for the conclusion to synthesize the answer. For a length-limited Letter, estimate with the official equivalent-word formulas; the text word count is not the complete length.

Figure aspect ratios affect both length conversion and readability: a tall single-column figure does not necessarily save space, and a wide, shallow two-column figure does not necessarily consume more pages. Choose dimensions from each figure's evidential needs, calculate the draft budget, then revise the panel organization. Do not shrink every label to force the material onto the page. Figure and table captions take space too. Leave room for float movement, long equations, and reference pagination; validate the final result against actual compilation and the official rules.

## Choose the column width for each figure

- **Single-column `figure`:** normally insert at the actual `columnwidth`/`linewidth`. Approximately 85 mm is APS guidance for single-column artwork; the target template is authoritative. This format suits one clear relationship, a small group of shared-axis panels, or a compact control comparison.
- **Two-column `figure*`:** use the actual `textwidth`. The package's 178 mm value is a configurable working default, not a uniform requirement across the journals. This format suits long axes, a main mechanism figure, or composite evidence requiring side-by-side comparison.
- Draw at the final width first. Keep type sizes and line weights consistent between single- and two-column figures; different heights and aspect ratios are allowed. Recheck all text and markers after any later scaling.
- The same distinction applies to single-column `table` and two-column `table*`. Use tables for precise comparisons of values, definitions, or conditions; do not turn editable tables into screenshots. Put titles above the tables and use Roman-numeral numbering; consult the APS guide for detailed ruling conventions.

## Where figures and tables belong

Number figures in the order of their first mention in the main text and place them near their first substantive discussion where possible. Insert the float at a suitable source location. The text should first pose the question the figure distinguishes, then explain the panel evidence; do not merely write “see figure” without stating what it supports.

REVTeX's `figure` and `figure*` environments are floats. Two-column figures in particular are often constrained to positions such as the top of a page. Source location and `[tbp]` are placement suggestions, not guarantees of exact coordinates after a paragraph. Do not attempt to solve every layout issue with repeated negative `vspace`, arbitrary `[H]` placement, or unverified float patches. First revise the figure grouping, aspect ratio, float order, and nearby text, then compile and inspect. The first figure need not be forced onto page one, and figures and tables need not all be moved to the end.

```latex
% Put near its first substantive discussion; actual float placement is compiled.
\begin{figure}[tb]
\centering
\includegraphics[width=\columnwidth]{assets/mechanism-examples/pole_trajectory.pdf}
\caption{State the scientific comparison, quantities, conditions, and data identity.}
\label{fig:poles}
\end{figure}
\begin{figure*}[t]
\centering
\includegraphics[width=\textwidth]{assets/mechanism-examples/response_map.pdf}
\caption{Explain the dominant map and supporting cuts without repeating the entire results section.}
\label{fig:response}
\end{figure*}
```

## Captions and final checks

Start each caption with the comparison or subject, then explain the panels, symbols or curves, quantities and units, key parameters, and statistical meaning. Readers should be able to distinguish data, theory, and schematic content, and to understand normalization, uncertainties, and controls. The interpretation must not exceed the evidence in the main text. Supply detail without unnecessarily repeating the results section.

After compiling the complete sources, inspect the title/abstract opening; the actual page positions of single- and two-column figures; first citations and numbering; the readability of axis labels and captions at final size; clipping and overflow; missing and duplicate references; and the placement of the main text, appendices/End Matter, and supplementary material. When tools and complete inputs are available, carry out the full cycle: compile → inspect each page and final-size figure → correct substantive problems → recompile, until the current changes pass inspection. Do not leave this as generic advice for the user to execute. If no compilation was performed, explicitly label the result “source example; compilation not verified.” A schematic page is neither a REVTeX rendering nor proof of length compliance.
