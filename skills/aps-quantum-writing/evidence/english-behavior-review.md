# Independent English-skill behavior and source-equivalence review

Review date: 2026-10-09. Reviewed skill: the public English edition of `aps-quantum-writing`. Comparison source: the verified original Chinese 1.0 skill archive.

## Result and limits

**All seven requested behavior areas pass this qualitative application review.** No substantive loss of the tested Chinese-source instructions was found. The English rules preserve the operative decisions, exceptions, conditions, and stopping boundaries, rather than merely retaining recognizable keywords.

This is a manual, non-blind application and source-equivalence review by a separate reviewer. The complete constructed prompts and reviewer-produced answers appear below. It is not an independent human assessment, a repeated model benchmark, a causal test of writing quality, or proof that a future model will always comply. No manuscript was compiled, no new figure was drawn, and no rendered appearance is certified by this review. No existing skill instructions or assets were edited; this report was added separately.

At the first inspection the figure references were already available in English; they were fully included, not left pending. The provenance documentation appeared during review and was subsequently read. `docs/PROVENANCE.md`, `THIRD_PARTY_NOTICES.md`, and `evidence/visual-inspection.json` were present by the final file check. The linked `evidence/public-release-validation.json` was initially pending at 15:53 UTC and was confirmed present at 15:56 UTC. Its presence is an assembly check, not independent verification of every result it records. Historical records intentionally excluded from the public package are not misclassified as missing translations.

## Scenario 1: independent theorems, complementary evidence, and collage

### Test prompt

A quantum-algorithm manuscript has two independently proved theorems under the same input-access model, error criterion, and resource accounting. One gives an achievable upper bound and the other a matching lower bound for the same task. Neither proof uses the other theorem. A second proposed manuscript instead combines a state-reconstruction theorem and a routing theorem that merely use the same Hamiltonian; deleting either leaves the other question and answer complete. Must the first paper be split? Can the second be made unified by a stronger title? Explain the A–D grades and apply deletion and splitting tests.

### Application output

The first manuscript can be strongly unified even though its proofs are independent. Its central question is the task's optimal resource scaling. The upper bound establishes achievability; the matching lower bound establishes the limit. Deleting the upper bound loses a construction attaining the limit, while deleting the lower bound loses optimality. Splitting the results would fragment the complete answer. Given the stated matching assumptions and resource conventions, this is an **A-level unity** case. State those common conditions precisely; do not hide differences in the access model, error, or resource definitions under a shared title.

The second manuscript is presently a **D-level assortment** if the only connection is the shared Hamiltonian. Its two results remain complete and answer separate questions when split. A stronger title cannot create a scientific relationship. Retain a result as supporting material only if it has a genuine supporting role; otherwise narrow the manuscript or develop separate papers. Do not invent a connecting theorem, causal dependency, or resource equivalence to keep them together.

The scale concerns the relationships between results:

- **A:** one clear answer, with necessary dependencies or irreplaceable complementary evidence.
- **B:** a substantially coherent answer with local connections that need explanation or strengthening.
- **C:** a plausible central thread whose major results do not yet contribute clearly enough to the same answer.
- **D:** separate results collected together without a substantive common answer.

Proof independence alone determines none of these grades. Correctness, mathematical novelty, and scientific importance need separate judgments. Familiar tools do not invalidate a contribution, and theorem count does not establish importance. Verify the closest literature at the level of task, assumptions, result, and new understanding before asserting novelty or its absence.

### Finding

**PASS.** English `references/conceptual-unity.md:7–23,27–33` preserves both tests, independent complementarity, the A–D definitions, and the ban on invented connections. It also retains the separate novelty/correctness/importance assessment and the obligation to repair existing-evidence problems before the final evaluation.

## Scenario 2: optional PRL headings, Outlook, current punctuation, and historical exceptions

### Test prompt

My PRL opening should have no Introduction heading, and I want the closing section called Outlook. I have current main-level headings written as `Model.—`, a `Note added.—`, and an old 2023 style reference. Should I normalize every period-dash combination? Must I add a Conclusion heading?

### Application output

Keep the opening unheaded and retain Outlook if it suits the argument. Introductory and concluding content is needed; printed headings named Introduction and Conclusion are not mandatory.

For a current PRL principal body heading, use an unnumbered, nonbold italic run-in label ending in an em dash without a preceding period: `Model—` and `Outlook—`. The following body text returns to upright type within the same paragraph. Natural wrapping is allowed; do not force the label into a separate displayed block.

Keep the period in `Note added.—`. It is a separate current exception, so a global replacement of all `.—` sequences is wrong. If the task explicitly requests the historical 2023 appearance, period-plus-dash principal headings can be retained and labeled historical. A historical sample does not establish a universal transition date or change the current default.

Handle acknowledgments, data availability, and End Matter/appendices by role. Their typography and placement are not obtained by globally redefining every section command. Native REVTeX appearance is an approximate author preview; inspect the compiled result before calling it verified. The supplied helpers do not reproduce the full production End Matter container.

### Finding

**PASS.** English `SKILL.md:22–24` and `references/microtypography.md:5,21–41,43–56,71–109` retain heading optionality, Outlook, current versus historical punctuation, the Note added exception, and native/helper/production limitations. The Chinese source contains the same distinctions.

## Scenario 3: PRA Letter DAS conflict and body/appendix font levels

### Test prompt

I am preparing a new PRA Letter. A checked 2026 version of record has italic run-in `Data availability.` and `Appendix.` headings, but the general APS guide describes principal headings. Which should I use? Separately, should every heading numbered `1.` be bold italic in a PRA Regular Article and its appendices?

### Application output

For the new PRA Letter, first follow an explicit current journal template or editorial instruction. If there is no more specific instruction, follow the guide's principal-heading route for the DAS and appendix, flag the conflict with observed Letter production, and confirm the intended treatment before submission. Do not describe the guide and the observed production as identical.

For an explicitly requested reproduction of the checked version of record, or a production-appearance preview, the nonbold italic, period-ended run-in forms `Data availability.` and `Appendix.` are supported by the cited PRA example. Label that choice **observed production style**, rather than claiming an official PRA-specific exception. Main-level body headings in a non-PRL Letter use the italic run-in period route independently of this DAS/appendix conflict. Do not transfer observed PRA/Applied/Research DAS behavior to PRB as if PRB had been directly verified.

In a Regular Article, a third-level **body** heading numbered `1.` is centered, displayed, and bold italic. An appendix heading numbered `1.` is instead its second level and is centered, displayed, and bold upright. The regular appendix's third level uses `a.` in bold italic; its fourth uses `i.` in italic run-in form. Determine the role and level before choosing the font; the character `1.` cannot determine it by itself.

Native REVTeX 4.2f regular third-level output was observed to be italic without bold. The optional guarded preview hook addresses that appearance only for the appropriate Regular/Research route; it does not turn a Letter into a Regular Article or supersede the submission template. Preserve semantic section and appendix commands and check the rendered page.

### Finding

**PASS.** English `references/microtypography.md:23–32,56–69,87–91` and `references/pra.md:3` preserve the official/observed distinction, target-specific decision branch, PRB evidence limit, appendix-versus-body numbering, and opt-in REVTeX caveat. There is no source-equivalence omission in this difficult exception.

## Scenario 4: a crowded hardware/neural workflow with unknown freeze boundaries

### Test prompt

Redesign an overcrowded workflow. The methods specify two coupled resonator modes with a drive and a measured output record y; encoder E maps the record to latent z; decoder D reconstructs y; head H maps z to an estimate of the coupling g. Training first minimizes a reconstruction objective and then a supervised coupling-estimation objective, but layer dimensions and which parameters are frozen or updated in each stage are not stated. Validation is simulated. Show the hardware/network relationship and a dense journal-quality method figure. Do not invent missing details.

### Application output

Use the main artwork to make the physical structure, computation, and training interfaces visible. A row of boxes labeled Hardware, Encoder, Decoder, and Prediction would lose the information this figure needs to explain.

The source-supported backbone is the driven pair of coupled modes, its readout port and output record y, the actual encoder structure E, latent representation z, and a branch to the decoder D and estimation head H. The decoder output is the reconstructed record; the head output is the estimate of g. Distinguish physical coupling from readout and from computational data flow. Label the apparatus **model/schematic; simulation validation** rather than depicting a measured chip or completed hardware deployment. A circuit-only picture would not satisfy the requested physical structure.

The visual brief is: a compact horizontal backbone with the two-mode physical structure beside its readout interface; source-supported encoder/decoder/head operations shown as nested structures rather than empty named cards; input records in one role color, central transformations in another, outputs in a third, and pale neutral grouping areas; short, continuous main-flow connections; visibly subordinate supervision/update paths; labels beside the transferred objects and symbolic dimensions where necessary. Reuse the manuscript's established color meanings if they already exist.

For the training portion, show the reconstructed record and its target entering the stated reconstruction objective, and the predicted coupling and its supplied target entering the supervised objective. Keep the two training stages identifiable. The sources do not determine the update targets or frozen boundaries, so do not add locks, frozen labels, or guessed loss-to-parameter arrows. Ask: **Which parameters of E, D, and H are updated and which are fixed in each training stage?** The operational diagram remains provisional at that specific boundary while the supported hardware and forward paths can proceed.

Retain known layer hierarchy and connections with symbolic dimensions. Do not fabricate widths, layer counts, bottlenecks, losses, or feedback. If the methods specify only modules and no internal architecture, request the actual architecture needed for the desired structural view; do not turn a generic network icon into purported architecture. Conceptual structure can still be drawn at the level supported by the source.

Obtain density by removing repeated titles, empty frames, excessive padding, and long arrow corridors. Allocate most area to the mechanism, fit containers to readable content and routing, and add an anchored enlargement only if it explains a new internal relationship. Preserve actual branches and label merges or operators explicitly. Do not globally shrink text, invent a node-count target, or add decorative unsupported complexity. If the figure needs more area, use a suitable two-column width or layered composition.

Before delivery, check the rendered figure at its final physical width for traceable inputs, operations, outputs, endpoints, smallest glyphs, and simulation identity. Separately compare its actual structures, color-fill weight, and spatial organization with the requested visual reference. A technically readable rendering can still fail the desired visual style. This answer is a design and dependency diagnosis; it does not claim that artwork has been rendered or visually accepted.

### Finding

**PASS.** English `references/scheme-design.md:5–19,21–41,47–80,101–125`, `references/branch-figures.md:20–21,49–55`, and `references/figure-style.md:43–52` retain the detailed scientific-density principles. The translation preserves physical and neural structural representation, actual interfaces, unknown-dimension handling, fixed/update uncertainty, distinct forward and update paths, role-color implementation, and separate visual acceptance. These were compared paragraph by paragraph with the Chinese source, not judged by the presence of “hardware” or “network.”

## Scenario 5: the outer-left y boundary, centered bottom elements, and near-square exceptions

### Test prompt

Make two stacked scalar plots align with the text column's left edge. One has long y tick labels and a ×10⁻³ offset. Should I push the axes frame to the edge and left-align both x labels and the shared bottom legend? Must a long time trace be square, and does near-square mean equal x/y units?

### Application output

Align the complete visible content boundary, including the y title, tick labels, scientific-notation offset, panel labels, and any required legend or colorbar. Keep a small safe clipping margin. Do not force the axes frame against the column edge and thereby lose its annotations.

For comparable stacked panels, align the left and right plotting frames and use a shared reference line for y titles. Reserve enough room for the longest annotations. Different-width tick labels need not have identical left edges, and the ×10⁻³ offset must remain associated with its own axis.

Keep each x-axis title centered on its own plotting area. Center a shared bottom legend or note on the panels or group it describes. Tightening the y side does not change this centering. The manuscript caption continues to follow the journal template; it is not governed by this bottom-label rule.

Start ordinary scalar plots with near-square physical axes boxes. This is not a requirement that the complete canvas or stacked group be square, nor does it impose equal x/y data-unit scales. A box-aspect setting can be a starting point; an equal-data-aspect setting needs a scientific reason.

A long time trace can use a wider panel when that preserves the temporal structure and readable sampling. Record that reason. Preserve scientific coordinate geometry in spatial or phase-space plots, and allow tall layouts for many categories or long labels when needed. Judge each axes box separately.

Find whether excess whitespace comes from the figure layout, an undersized centered manuscript insertion, or the exported page box. Fix the actual source, retain all annotations, and remeasure physical size after any crop. Do not silently tight-crop, stretch the exported image, or shrink fonts to conceal a layout problem. Verify annotation bounds and final manuscript insertion, not just source canvas dimensions.

### Finding

**PASS.** English `references/figure-style.md:31–41` preserves every distinct reference geometry and the diagnosis of three whitespace sources. `references/branch-figures.md:23–36` preserves nonsquare exceptions without allowing them to erase the ordinary near-square default. No semantic omission was found.

## Scenario 6: motivation-first proof with undefined-symbol and dependency risks

### Test prompt

Rewrite a perturbation-bound proof so that motivation and the main idea appear before technical lemmas. The rough draft says “By Λ, δ ≤ ε” before defining any of these symbols. May a precisely stated lemma be used before its proof, and how do you avoid circularity?

### Application output

Explain the task and obstacle first, but do not use undefined symbols as a shortcut. A suitable self-contained rewrite is:

“We seek a bound on how far the largest eigenvalue can move when a Hermitian matrix is perturbed. Tracking the eigenvector directly is unnecessary: the key is that the perturbation changes every unit-vector expectation value by at most its operator norm.

Let A and B be n-by-n Hermitian matrices, with n a positive integer. Write λmax(A) for the largest eigenvalue of A, and let ||H||₂ = sup{||Hx||₂ : ||x||₂ = 1} be the operator norm induced by the Euclidean vector norm. Then

|λmax(A) − λmax(B)| ≤ ||A − B||₂.

We use the variational identity λmax(H) = max{ x*Hx : ||x||₂ = 1 } for a Hermitian matrix H, where x* denotes conjugate transpose; its proof is given below. For any unit vector x, the Cauchy–Schwarz inequality and the definition of the operator norm give |x*(A − B)x| ≤ ||A − B||₂. Thus x*Ax ≤ λmax(B) + ||A − B||₂. Maximizing over x yields one direction, and exchanging A and B yields the other.

To verify the variational identity, use an orthonormal eigenbasis of H. A unit vector's expectation is a convex combination of H's eigenvalues, so it is at most the largest eigenvalue; a corresponding unit eigenvector attains equality.”

The result and every symbol are defined before use. The variational identity is stated accurately before it is invoked, its later proof is explicitly signposted, and that proof does not rely on the perturbation bound. Exposition need not mechanically follow the proof graph, but the graph must still be checked for valid assumptions and circularity. A local rewrite should preserve the actual source theorem and evidence rather than replacing it with a stronger claim.

### Finding

**PASS.** English `references/branch-writing.md:36–40`, `references/physics-narrative.md:13–21`, and `references/precision-audit.md:13` retain motivation-first explanation, defined forward references, traceable proof, and separate dependency checks. The English adaptation does not interpret “motivation first” as permission to introduce undefined notation.

## Scenario 7: missing data, synthetic examples, direct prose, and genuine counterexamples

### Test prompt

The supplied results say only that a calculated gap is positive at N = 8, 16, 32; numerical values, uncertainties, and a reproducible model are missing. Make a smooth heatmap with error bands anyway. Also remove defensive wording from “For a finite irreducible chain, we prove a unique stationary state. We do not claim uniqueness for a reducible chain: two disconnected closed irreducible components each support a stationary state.” Make everything sound confident.

### Application output

The available statement supports “The calculated gap is positive for N = 8, 16, and 32.” It does not provide enough information for numerical curves, a heatmap, error bands, or a thermodynamic-limit claim. The useful deliverable now is a figure specification and the supported text, with a precise request for numerical values, parameter-grid definitions, and any uncertainty calculation or reproducible model. Continue any independent schematic work supported by the materials.

Do not fabricate a grid, interpolate from an assertion of positivity, reverse-engineer samples from means, or label placeholder numbers as research data. A documented simulation actually computed from a specified model can be research evidence; the skill does not prohibit such calculations. Here the model and numerical inputs are absent. Synthetic layout demonstrations would have to be visibly identified as demonstrations and kept separate from the manuscript's evidence.

A direct revision of the theorem passage is:

“For a finite irreducible chain, the stationary state is unique. Two disconnected closed irreducible components each support a stationary state, so uniqueness need not hold for a reducible chain.”

The assumption and the concrete counterexample remain beside the result. Removing “we do not claim” improves the sentence's focus; it does not justify suppressing the counterexample, strengthening “need not” to “never,” or asserting uniqueness for all finite chains. If the input supplied only “not proved,” that could not become “numerically supported,” “observed,” or “false” without additional evidence. Necessary conditions also remain in standalone abstracts and captions even when they have appeared elsewhere.

### Finding

**PASS.** English `SKILL.md:32–35`, `references/branch-figures.md:49–55`, `references/figure-style.md:64–70`, and `references/prl-direct-prose.md:7–27,51–57,89–95` retain the complete scientific-integrity boundary. The translation distinguishes real computed simulation from arbitrary synthetic placeholders and authorial self-defense from an actual negative finding.

## Source-equivalence assessment beyond the seven answers

The review read the English entry point, all four branch/reference-routing files, conceptual unity, physics narrative, natural prose, precision audit, direct prose, APS format, heading microtypography, all seven journal profiles, figure style, schematic design, and both evidence ledgers. Corresponding Chinese-source instructional paragraphs were compared for retained conditions and exceptions.

No material instruction omission was identified in these areas:

- Exactly three top-level branches; format belongs to planning; local tasks do not trigger full-manuscript ceremony.
- Continuous work from the existing state, reversible defaults for noncritical choices, focused questions for scientific blockers, and accurate completion claims.
- Introduction development and closest-work comparison; no fixed paragraph count, mandatory IMRaD, or compulsory heading names.
- A configurable approximately 30–40-reference planning default, verified citations and claim-level support, no numerical padding, and honest gaps when search is unavailable.
- Correctness, novelty, importance, and journal positioning remain separate, conditional judgments.
- Source facts, assumptions, units, quantifiers, citations, evidence status, uncertainty, and genuine negative results remain protected during stylistic edits.
- Article-type distinctions, PRX versus PRX Quantum, journal-specific Popular Summary differences, REVTeX option caveats, and separate Letter length accounting are retained.
- Figure choice is driven by discriminating evidence; spectral versus data collapse, deterministic evolution versus single-shot trajectories, and Wigner versus histogram distinctions remain explicit.
- Render/compile/inspect requirements are not weakened into source-file-existence checks. Technical readability and actual visual-target matching remain separate acceptance questions.
- Schematic structure, role-based filled objects, connection hierarchy, actual training boundaries, and support for unknown numerical dimensions survive in full.
- Original examples remain explicitly illustrative or synthetic. Historical minimal example assets are not elevated into required layouts for new papers.

The English edition deliberately replaces personal-source preference wording with configurable package defaults in several public-facing passages. That preserves the available behavior while avoiding presenting a private user's choice as an APS mandate. Historical audit and integration-document links are consolidated into public provenance rather than falsely promising those excluded records are bundled.

The newly available provenance and ledgers preserve the key limits: 700 metadata records are not 700 new readings; 390 legacy snippets, 10 placeholders, and 128 truncation markers are disclosed; main-text/caption reading is distinct from actual image inspection; source manuscript versions are distinct from final production; the late 90/10 split is not blind or preregistered; and the evidence is neither proof verification nor an acceptance-rate study. These are summaries rather than complete translations of all historical notes, and they explicitly say so.

## Final assembly boundary

The initially pending `evidence/public-release-validation.json` was confirmed present at the final check. No file needed for these seven behavioral applications remains unavailable. This review does not certify final archive contents, licensing approval, publication, repository CI, numerical example reruns, or new LaTeX compilation; those require their own evidence.
