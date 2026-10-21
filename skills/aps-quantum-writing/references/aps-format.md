# APS article types and source-file formatting

For section-heading format, use `journal + article_type + heading_role` to select the relevant guidance in [Heading microtypography](microtypography.md). Whether headings appear and what they are called depend on the paper: Outlook is acceptable, as is a body without headings. Check only the roles and levels actually chosen; do not add headings to every paragraph or globally redefine `\section`.

Use this reference for formatting and submission tasks. Requirements for the three additional journals and the applicability of the length formulas were rechecked on 2026-10-09; the original PRL rules were rechecked on 2026-10-07, and the original PRA/PRB rules on 2026-10-06. Recheck the relevant journal page before formal submission. Once the journal and article type are known, work directly on the applicable items.

## Article-type matrix

| Target | Length | Materials to distinguish |
|---|---|---|
| PRL Letter | Core article: 3,750 APS-equivalent words; up to 2 additional pages of End Matter | End Matter follows the references; submit a separate suitability statement of approximately 100 words |
| PRA Regular Article | No general word limit | Standard technical abstract; sections follow the needs of the argument |
| PRA Letter | 4,500 APS-equivalent words | Organize the abstract as problem → findings → work accomplished → background/outlook |
| PRB Regular Article | No general word limit | Standard technical abstract; sections follow the needs of the argument |
| PRB Letter | 4,500 APS-equivalent words | Do not reuse the old Rapid Communication word limit |
| PRX Quantum Research Article | No general word limit | A separate Popular Summary accompanies the technical abstract: approximately 150 words recommended, with a 250-word maximum on the general submission page |
| Physical Review Applied Regular Article | No general word limit | Submit a separate 100-word suitability statement; generally prefer appendices in the manuscript for technical details |
| Physical Review Applied Letter | 4,500 APS-equivalent words | Submit a separate 100-word suitability statement; do not apply the PRL End Matter exemption |
| Physical Review X Research Article | No general word limit | A Popular Summary is required before publication; the journal-specific page sets a maximum of 150 words |
| Physical Review Research Regular Article | No general word limit | Develop the argument as needed; do not assume that a Popular Summary is required |
| Physical Review Research Letter | 4,500 APS-equivalent words | The main article must be self-contained; do not apply the PRL End Matter exemption |

Sources: [PRL](https://journals.aps.org/prl/authors), [PRA](https://journals.aps.org/pra/authors), [PRB](https://journals.aps.org/prb/authors), [PRX Quantum](https://journals.aps.org/prxquantum/authors), and [Popular Summary submission guidance](https://journals.aps.org/authors/web-submission-guidelines-physical-review). Additional sources: [Physical Review Applied](https://journals.aps.org/prapplied/authors), [Physical Review X](https://journals.aps.org/prx/authors), and [Physical Review Research](https://journals.aps.org/prresearch/authors). PRX does not currently list Letter as an article type. Check Perspectives, Tutorials, Reviews, Comments, and other types separately; do not transfer the original-research configuration to them unchanged.

PRX's journal-specific Popular Summary limit of 150 words differs from the 250-word limit on the general submission page. Use the more specific and stricter 150-word limit, and recheck it before submission. For PRX Quantum, retain its own recommendation of approximately 150 words together with the general page's maximum. Prepare the technical abstract, Popular Summary, editorial suitability statement, and promotional Author Summary as distinct items.

The technical abstract is a self-contained single paragraph, without displayed equations, tables, or numbered citations. General abstract guidance is approximately 5% of the main text and fewer than 500 words; this is not a hard PRL limit of 250 words. Use section headings where they help the argument, without imposing a uniform IMRaD structure. Appendices normally precede the references; PRL End Matter is an exception. Keep essential reasoning in the article, with supplementary material carrying additional detail. See [APS Style Basics](https://journals.aps.org/authors/style-basics).

## Abstract guidance update, 2026-10-21

Use [Abstract narrative](abstract-narrative.md) for the story and article-type distinctions. The February 2026 APS Style Guide, E. Abstract, additionally states PRL abstracts should not exceed 600 characters, in tension with observed published abstracts. Preserve this unresolved source conflict and verify the current journal page/submission system before asserting length compliance. Do not silently interpret characters as words or replace an official limit with a sample-based limit. This update does not revalidate the unrelated formatting rules above.

## REVTeX: select the correct class options first

The publicly available APS version checked for this reference is REVTeX 4.2f; the class name remains `revtex4-2`. The `prl`, `pra`, and `prb` options correspond to those journals; the distribution also supports `prapplied` and `prx`. The `reprint` option provides a journal-like layout; `preprint` provides a single-column, double-spaced review layout. An internal two-column draft can start with the following, replacing `prb` as appropriate:

```latex
\documentclass[aps,prb,reprint,amsmath,amssymb]{revtex4-2}
\usepackage{graphicx}
```

PRX Quantum: the checked 4.2f distribution has no `prxquantum` option. A general APS working draft can use the supported `physrev` option. For formal submission, use the journal's currently accepted template; do not describe `prx` as a verified PRX Quantum-specific option. A layout preview does not certify final length compliance. See the [REVTeX home page](https://journals.aps.org/revtex) and [REVTeX FAQ](https://journals.aps.org/revtex/revtex-faq).

Use `aps,prapplied,reprint` for a Physical Review Applied working draft and `aps,prx,reprint` for PRX. A check of the same official 4.2f distribution on 2026-10-09 found no `prresearch` option. A Physical Review Research working draft may use the supported generic `physrev` option; recheck the currently accepted template before submission, and do not call this a journal-specific option. These checks concern source-level option support and do not establish that a new manuscript has been compiled.

## Mathematics, figures, captions, and citations

- Equations are parts of sentences: maintain grammatical continuity and complete punctuation. Use `label`/`ref` for automatic numbering and cross-references. For multiline derivations, choose an appropriate alignment environment so that the mathematical relationships remain readable.
- Scale a single-column `figure` to `columnwidth` or `linewidth`; use `figure*` and `textwidth` for a two-column figure. Axis labels, symbols, and lines must remain distinguishable at the final size.
- As a configurable working preference, bring the full visible content of data figures, including the y-axis title and tick labels, close to the left edge of the text column while keeping a safe margin. Check internal figure whitespace, undersized centered inserts, and blank export-page margins separately. Follow [Data-figure layout](figure-style.md) and assess the result in the final manuscript. Keep x-axis titles and bottom notes or legends centered on their respective reference spans; captions still follow the journal template.
- Captions explain what the figure tests and supply the quantities, units or normalization, curve identities, and parameters needed to read the panels. State the statistical meaning of error bars; do not invent uncertainty information when none is supplied.
- Number figures in the order of their first citation, and label panels `(a)`, `(b)`, and so on. Number tables with Roman numerals. Let REVTeX/BibTeX handle citations and bibliography formatting, and verify titles, authors, and DOIs in the database.

The following source example illustrates syntax only. Its symbols and physical relationship are not results from a particular paper:

```latex
The response is
\begin{equation}
R = a x + b,
\label{eq:response}
\end{equation}
where $a$ and $b$ are the fitted coefficients.
Figure~\ref{fig:response} compares Eq.~(\ref{eq:response}) with data.
\begin{figure}
\centering
\includegraphics[width=\columnwidth]{response.pdf}
\caption{Response $R$ versus control parameter $x$.
The curve is Eq.~(\ref{eq:response}); symbols denote the supplied data.}
\label{fig:response}
\end{figure}
\bibliographystyle{apsrev4-2}
\bibliography{references}
```

Published reference lists for PRB, Physical Review Applied, PRX, and Physical Review Research include article titles. PRA and PRX Quantum encourage their inclusion, and PRL encourages consistent inclusion. REVTeX 4.2's APS BibTeX style displays article titles by default, provided that the database contains them. After changing source files, compile when the full environment and assets are available, then check for overflow, missing references, and figure readability. If no compilation was performed, distinguish source repairs from a verified PDF. See the [REVTeX documentation](https://journals.aps.org/revtex).

## Length conversion for length-limited articles

The APS count includes the main text, figure and table captions, and notes, together with equivalent-word contributions from displayed equations, figures, and tables. It excludes items such as the title, author information, abstract, references, and acknowledgments. Do not report only a word processor's text count.

The following aspect-ratio formulas apply to APS Letter/short-article counting; they are not a universal algorithm for every article type. For single-column material: count 16 words per equation line; `150 / aspect ratio + 20` words per figure; and `13 + 6.5 × number of rows` words per table. For two-column material: count 32 words per equation line; `600 / aspect ratio + 40` words per figure; and `26 + 13 × number of rows` words per table. PRL End Matter has a separate page count. Conservatively include ordinary appendices in the full manuscript budget for Applied/Research Letters; do not use PRL-specific End Matter to evade their limits. Calculate from the complete assets and leave reasonable layout headroom. See the [APS Length Guide](https://journals.aps.org/authors/length-guide).

The class options were checked by read-only inspection of `aps4-2.rtx` in the [official APS 4.2f distribution](https://cdn.journals.aps.org/test/345f0cd4-cab7-4271-9a46-7331fb57618a/revtex-tds-2023-05-30.zip).

The official length guide separately lists a counting table for PRX and Review articles in certain journals: 170 words for each single-column figure and 340 for each two-column figure. This does not create a word limit for PRX Research Articles. For non-Letter types, first select the applicable table.

## Submission compliance and AI-tool use

Prepare the Data Availability Statement from the actual research and writing process, and check the [APS policy on appropriate AI-tool use](https://journals.aps.org/authors/appropriate-use-ai-tools) before submission. Distinguish light copyediting from substantive scientific reasoning, literature synthesis, drafting conclusions, generating graphics, and analyses that affect results. When disclosure is required, record the actual tool and version, its purpose, and the authors' verification; place the disclosure in the methods, acknowledgments, or relevant caption as the policy requires. Natural-sounding prose does not change disclosure obligations, and tool versions must not be invented. Authors remain responsible for verifying scientific results, citations, notation, and figures.
