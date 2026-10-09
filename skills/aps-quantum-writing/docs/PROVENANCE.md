# Provenance and evidence boundaries

This is the stable provenance record for the public English edition of APS Quantum Writing. It summarizes the source archive faithfully while excluding private working material and paper content. It does not certify publication or APS endorsement.

## What the numbers mean

The public [paper index](../evidence/papers.json) contains **700 unique DOIs across seven journals, 100 per journal**; a [CSV copy](../evidence/papers.csv) is also available. These are metadata records, not 700 newly read papers for this English edition. Dates, titles, links, source versions, ranks, and review-group identities come from the source archive. A recorded `main_text_reviewed` value describes that archive's review, not a new reading during translation.

- **Legacy 400:** PRL, PRA, PRB, and PRX Quantum, reviewed in the earlier source work through October 6, 2026. The original archive contains 390 original observation snippets and 10 PRL late-reserved placeholders; 128 snippets carry truncation markers. This edition preserves metadata and rule-level provenance, rather than republishing or completing those historical notes. It does not reconstruct missing text.
- **Added 300:** Physical Review Applied, Physical Review X, and Physical Review Research, 100 each. The source expansion on October 9, 2026 records reading the complete main body and main figure/table captions. These were new reviews in that expansion; this English edition inherits them. Applied used 100 pinned arXiv author manuscripts; PRX and Research each used 100 official version-of-record JATS sources.
- **Actual image inspection:** the added-journal review separately inspected six Applied papers, one PDF page each; two PRX papers, four figures; and five Research papers, seven figures. That is 13 papers with limited image inspection. Page and figure counts have different units and are not combined into an invented image total. Reading captions does not establish image inspection.
- **Synthetic example inspection:** checking this package's generated illustrations and five-page heading preview is a separate activity. It does not enlarge the paper-review or source-image sample.

Machine-readable counts and limitations are in [coverage.json](../evidence/coverage.json). The [legacy ledger](../references/evidence-ledger.md) and [added-journal ledger](../references/evidence-ledger-v12.md) give sampling and version details.

## Four kinds of support

1. **Official requirements:** APS author pages, length guidance, style guidance, and specific policies. These determine submission requirements within their stated scope. Historical checks do not replace rechecking a current submission page.
2. **Published-paper observations:** identifiable passages or images of a stated version. An author manuscript is not evidence of final APS copyediting or production appearance.
3. **Editorial recommendations:** conditional judgments derived from examples. They are not APS mandates, prevalence statistics, evidence of improved acceptance rates, or causal findings about writing quality.
4. **Configurable preferences:** direct prose, a central-claim workflow, compact graphics, and particular label placement. These never override scientific truth, necessary uncertainty, or actual journal requirements.

## Rule-to-evidence map

[Rules and locators](../evidence/rules.json) preserve 40 editorial rule identifiers: 23 legacy rules and 17 added-journal rules. Their English descriptions are translations or faithful summaries of original review observations. Each rule retains source DOIs and locators, with version information either in the rule or the paper index. Listed counterexamples and protected boundaries remain visible. The 23 legacy rules each have five listed source examples; some examples are cautions rather than positive demonstrations. Added-journal rules have two to five examples, as actually recorded, not an invented common minimum.

| Configuration | Rule identifiers | Scope |
|---|---|---|
| [PRA](../references/pra.md) | PRA-C01–C05 | Problem-to-contribution links; argument dependencies; conditions; resource accounting; safe compression |
| [PRB](../references/prb.md) | PRB-R01–R05 | Evidence structure; approximation levels; metrics and conditioning; resource/limit claims; abstract consistency |
| [PRL](../references/prl.md) | PRL-R01–R04 | Precise contribution; figures and equations in the argument; truth conditions; qualified conclusions |
| [PRX Quantum](../references/prx-quantum.md) | PRXQ-R01–R09 | Gap, overview, full cost, evidence level, matched comparisons, demonstrated capability, assumptions, captions, structure |
| [Physical Review Applied](../references/prapplied.md) | APP-E01–E06 | Physical evidence for application metrics; costs; derivation order; failures; scientific workflows; aligned visual comparisons |
| [Physical Review X](../references/prx.md) | PRX-R01–R05 | Connected contributions; reader-oriented proof; mechanisms and alternatives; performance accounting; spatial correspondence |
| [Physical Review Research](../references/prresearch.md) | PRR-C01–C06 | Central question; baselines and resources; construction and validation; claim boundaries; matched panels; traceable scientific objects |

The general writing and figure branches apply these judgments conditionally. They do not imply that every indexed paper was coded for every feature. There is no complete feature denominator and no basis here for journal-wide style frequencies or causal comparisons between journals.

## Official sources and conflicts

The [official-source register](../evidence/official-sources.json) records public URLs and source-archive check dates. The working guides are [APS format](../references/aps-format.md) and [heading microtypography](../references/microtypography.md). Primary references include:

- [APS Style Guide, February 2026](https://res.cloudinary.com/apsphysics/image/upload/APS_Journals_Style_Guide_Authors022326_guzwhx.pdf), including printed pages 12–15, 19, 21, 23, and 25
- [APS Style Basics](https://journals.aps.org/authors/style-basics), [length guidance](https://journals.aps.org/authors/length-guide), and [Supplemental Material instructions](https://journals.aps.org/authors/supplemental-material-instructions)
- Author instructions for [PRL](https://journals.aps.org/prl/authors), [PRA](https://journals.aps.org/pra/authors), [PRB](https://journals.aps.org/prb/authors), [PRX Quantum](https://journals.aps.org/prxquantum/authors), [Applied](https://journals.aps.org/prapplied/authors), [PRX](https://journals.aps.org/prx/authors), and [Research](https://journals.aps.org/prresearch/authors)
- [REVTeX](https://journals.aps.org/revtex), [REVTeX FAQ](https://journals.aps.org/revtex/revtex-faq), and the [official 4.2f distribution](https://cdn.journals.aps.org/test/345f0cd4-cab7-4271-9a46-7331fb57618a/revtex-tds-2023-05-30.zip)
- [APS AI-tool policy](https://journals.aps.org/authors/appropriate-use-ai-tools); stylistic editing does not remove applicable disclosure obligations

Two source conflicts are deliberately preserved:

- PRX's journal page listed a 150-word Popular Summary maximum while the generic submission page listed 250. The source configuration chooses the tighter journal-specific limit and asks for a submission-time recheck.
- The February 2026 guide's broad non-PRL data-availability/appendix heading language differs from observed Letter production. Directly checked examples include [PRA 113, L030201](https://doi.org/10.1103/qw5d-5ztg), PDF page 3; [Research 8, L032025](https://doi.org/10.1103/2pg6-vd1j), page 5; [Research 8, L032046](https://doi.org/10.1103/g2z2-2w2h), page 5; and [Applied 24, L021002](https://doi.org/10.1103/7ktx-4h8m), page 6. They show italic, period-ended run-in headings. This is observed production evidence, not an explicit exception in the broad guide. For new submissions, follow the current journal's specific template/editor instruction; absent one, follow the general guide and flag the discrepancy. The optional example previews show the observed production route. PRB Letter data-availability/appendix appearance was not directly verified.

## Typography provenance and verification boundary

The [inherited typography audit](../evidence/typography-audit.json) records **32 passing assertions** and **29 standalone TeX source fixtures**, each compiled twice in the source audit. Four fixtures deliberately used unsupported options and produced the expected warnings; three tested fail-closed guards. They are not additional supported journal configurations. The source audit also rendered and visually inspected all five representative preview pages.

The audited environment used pdfTeX 1.40.26, LaTeX2e 2024-11-01 patch level 2, and REVTeX 4.2f. The current English-release checks are separate and are reported in the release validation documentation. Inherited pass flags are not claims that those checks were rerun during this translation.

Material findings preserved in the English configuration:

- REVTeX 4.2f supports `prl`, `pra`, `prb`, `prapplied`, and `prx`. `physrev` is a supported generic working-draft fallback for PRX Quantum and Research. `prxquantum`, `prresearch`, `letter`, and `rapid` were negative controls that produced PDFs with unused-option warnings. PDF existence does not prove class-option support.
- Native PRL section commands do not generate the observed current italic run-in headings. Explicit helpers provide a preview without inventing mandatory Introduction or Conclusion labels, creating section counters, or globally redefining section commands.
- Current PRL main labels use an italic em dash without a preceding period. The named Note added exception retains its period. A [2023 PRL historical example](https://doi.org/10.1103/PhysRevLett.131.191001), pages 2 and 6, documents the older period-plus-dash form; the exact transition date was not established.
- Non-PRL Letter preview labels use an italic title and period with upright text in the same paragraph. Long titles may wrap naturally.
- Native regular third-level headings in 4.2f were italic but not bold; the 2026 guide calls for bold italic. A guarded opt-in preview hook changes only the appropriate formatting hooks. Guard tests covered PRL, existing custom hooks, and altered dispatchers.
- The helpers do not reproduce production fonts, full-width End Matter, exact publisher geometry, pagination, or official word counts. The preview is synthetic and is not an APS-supplied template or a publisher facsimile.

## Attribution and distribution

Luofei Wang is the author identified for this release. The author-approved original-project terms are in [LICENSE](../LICENSE), a custom noncommercial source-available license, not an OSI open-source license. Third-party components retain their own licenses and are outside any added noncommercial restriction.

[Third-party notices](../THIRD_PARTY_NOTICES.md) distinguish upstream MIT material, embedded DejaVu fonts, embedded AMS Computer Modern fonts, public bibliographic metadata, and unbundled dependencies. The exact upstream MIT copyright line remains in its unmodified license file. The [font record](../evidence/embedded-fonts.json) identifies 10 source asset PDFs and 53 embedded font resources. It applies to those hashed assets; replacing an asset requires a fresh check.

Five redundant generated EPS exports are excluded from this lightweight edition. The retained PDFs, PNGs, editable sources, and generation scripts preserve the examples and the ability to regenerate those exports. The unchanged source archive is separate from this public distribution.

Included evidence is limited to bibliographic metadata, public source links, original rule-level observations and locators, scope summaries, source fingerprints, and component/font records. Excluded materials include downloaded paper PDFs, full abstracts, JATS bodies, original paper figures, screenshots of source papers, private paths, identifying email addresses, credentials, conversation records, and historical execution logs. The unmodified license files necessarily retain their legal notices. [Source fingerprints](../evidence/source-fingerprints.json) identify archival inputs without distributing those inputs or promising that excluded working records are publicly accessible.

No part of this evidence constitutes independent proof verification, experimental or numerical reproduction, human expert certification, legal certification of every possible right, or endorsement by APS or another cited organization.
