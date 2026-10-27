---
name: aps-quantum-writing
description: Use when writing, restructuring, or formatting quantum-research manuscripts and scientific figures for PRL, PRA, PRB, PRX Quantum, Physical Review Applied, Physical Review X, or Physical Review Research.
---

# APS Quantum Research: Planning, Writing, and Figures

See [VERSION](VERSION) for the current release and the [usage guide](USE_GUIDE.md) for a quick start.

Connect the manuscript and its figures through one central physical question: where existing explanations fall short, what answer the evidence provides, and how that answer changes understanding. Preserve the source manuscript's facts, mathematical meaning, and strength of evidence. Write directly, develop the necessary background, and let scientific purpose determine the figures.

## Three conditional branches

This is one skill with three task-dependent branches. Do not load every reference by default.

- **PLANNING**: For a complete manuscript's goals, progression from background to the central question, outline, working title, text–figure layout, continuous execution, and final assessment, read the [planning branch](references/branch-planning.md). Manuscript titles and abstracts, heading microtypography, REVTeX, and single- or double-column floats are on-demand references within this branch.
- **WRITING**: For drafting, developing, or restructuring manuscripts, introductions, proofs, conclusions, appendices, Supplemental Material, citations, and prose, read the [writing branch](references/branch-writing.md). Fully develop the physical problem and literature gap, and explain the reasoning clearly. A local one-sentence edit can be handled directly.
- **FIGURES**: For designing, generating, and checking scientific data plots and mechanism, apparatus, or workflow diagrams, read the [figures branch](references/branch-figures.md). First choose discriminating evidence and physical relationships; then use its fixed figure-plan fields, assign flexible panel roles, and choose the figure type, layout, and style. Quantum-domain recipes are on-demand references. Start single-column unless specified otherwise, widening only when mechanism, geometry, or final-size readability requires it.

PLANNING coordinates WRITING and FIGURES for a complete manuscript. These are the only three top-level branches. The user's existing choices of journal, language, data, structure, and layout take precedence.

## Abstract tasks: use the dedicated writing reference

The abstract must communicate the core contribution, core method, and core reasoning in a coherent, rigorous narrative that follows natural reading and writing habits. Preserve the decisive scientific idea rather than replacing it with a generic method label or omitting it for a smoother “physical story.” Distinguish necessary reasoning from full proof or implementation detail. Apply this through the manuscript's own scientific relationships, not a template copied from a particular example. Treat this as this skill's editorial standard, not a universal APS sentence template.

For any substantive abstract task, load [Abstract narrative](references/abstract-narrative.md) and the selected journal/article-type profile. Establish the physical question or organizing contribution, preserve the evidence and conditions, and connect findings to their scientific meaning. Check local transitions and the whole-paragraph answer. This remains part of WRITING, coordinated by PLANNING; it is not a new top-level branch. Keep Technical Abstract, Popular Summary, and suitability statement separate.

## Headings: decide whether they are needed before checking their form

Whether headings exist and what they are called depend on the manuscript's argument. Content-specific headings, an Outlook, or an unsectioned main text may all be appropriate. Do not require Introduction or Conclusion headings, or add a heading to every paragraph. When heading format matters, consult [heading microtypography](references/microtypography.md) using `journal + article_type + heading_role`; check type style, numbering, display versus run-in placement, and punctuation. The current PRL main-level form is italic run-in `Heading—`; treat `Note added.—` as a separate special case. Non-PRL Letters use italic run-in `Heading.` at the main level. Regular/Research articles use displayed `I.` / `A.` / `1.` levels. Distinguish acknowledgments, data availability statements (DAS), and appendices by role rather than rewriting every `\section` globally. Load detailed exceptions and optional helpers only when needed.

## Continue to completion rather than requesting approval at every stage

For a complete manuscript, load PLANNING and resume from the existing state: background → journal/article type → central question and claim → unity and outline → working title → figure set → complete draft → title/abstract revision → compilation and visual checks → brief substantive assessment. Continue when the materials are sufficient. Ask only about specific gaps that affect scientific conclusions or required authorization. For a local task, enter the relevant branch directly without repeating the full workflow.

## Shared requirements

- In narrative main text and supporting-material prose, use connected sentences without colons or parenthetical/explanatory dashes. Preserve a dash that joins a correctly formatted run-in heading to its body. Introduce cited work through its scientific contribution, using existing research or verified authors' recent work rather than publication-status labels or preprint identifiers. For short conference or journal manuscripts using fuller reference material, retain the original scientific wording without adding extended/expanded-version labels. Apply this even to local edits; follow [prose punctuation and literature wording](references/prose-conventions.md) for scope, heading choices, and preservation of mathematical and bibliographic syntax. These are editorial preferences, not APS requirements.
- Support one central physical claim with sufficient evidence. State directly the objects, setting, conditions, and evidence type for which it holds. Apply the same direct scientific style to the main text, appendices, End Matter, Supplemental Material, and captions. Do not fill these with statements about what the authors have not studied, proved, or claimed, or relocate removed self-defense to another part of the paper. Describe genuine unknowns, negative results, and counterexamples accurately as scientific content. For defensive prose, read [direct scientific prose](references/prl-direct-prose.md).
- The configurable default for a complete manuscript is usually about 30–40 references, adjusted naturally to its content rather than made identical across manuscripts. This is a writing default that users may override, not an APS requirement. Include only real, verified references that serve the argument. If coverage is thin, review the literature needs and search before considering the count; never pad the bibliography.
- Do not invent results, uncertainties, citations, or priority claims, or present synthetic examples as research data. When evidence is insufficient, deliver the usable portion and identify the specific gap blocking the conclusion.
- Deliver a usable manuscript or reproducible figure sources. Perform routine checks without automatically appending a long audit table. State which figures and source files were actually generated, rendered, or compiled.

Read the [historical 400-paper evidence ledger](references/evidence-ledger.md) and the [additional 300-paper, three-journal ledger](references/evidence-ledger-v12.md) only when tracing sources. The underlying corpus contains 100 records for each of seven journals, totaling 700 unique DOIs. As documented in [provenance](docs/PROVENANCE.md), the recovered historical archive contains 390 short observation notes and 10 holdout placeholders; 128 of those notes carry truncation markers. The additional 300 papers have individual main-text and principal-caption review records; actual image inspection is counted separately. Do not claim that all 700 papers were reread closely or have 700 complete commentaries. These observations support conditional editorial choices; they neither replace current APS rules nor provide causal statistics on writing effectiveness.
