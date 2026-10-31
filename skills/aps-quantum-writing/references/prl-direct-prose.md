# Remove Defensive Prose: Let the Physical Results Carry the Argument

Apply this reference when drafting or revising manuscript prose and before delivering the text. It draws on PRL's narrative logic without forcing manuscripts into a fixed paragraph template. The same editorial preference applies in the manuscript's requested language.

## Omit unfinished work instead of describing its absence

Write the scientific work actually completed, the result it supports, and its physical meaning. Delete statements whose only content is what this paper does not claim, has not solved, has not proved, has not tested, or has not operated or deployed. The omission rule also covers work closely related to the central question; it is not limited to unrelated extensions or repeated disclaimers.

Do not leave these statements in an impersonal form such as "remains unresolved", "has not been jointly deployed", "does not yet constitute a validated protocol", "remains to be verified", or "future work should". Do not preserve their meaning under a synonym, move them into the conclusion or Supplement, or replace them with a promise of work that has not been performed. If a sentence contains only an unfinished task, delete it without inventing a replacement result. Discuss an inventory of open problems, limitations, or future tasks only when the user explicitly requests that separate content.

Scope the affirmative claim through the actual study design. Write "in simulation", "in separately evaluated local-response tests", "for the measured sizes", or the relevant model assumptions when supported by the materials. A component test should remain a component test, without a second sentence announcing the absence of a complete-system demonstration. If an existing claim exceeds the evidence, narrow that claim itself. Omitting an undone operation must never turn it into a completed operation.

This rule does not delete an observed failure, a null measurement, a counterexample, uncertainty in a measured quantity, or a condition needed to reproduce the work. Those describe the actual result or method. The central question addressed by the paper also remains part of its scientific argument. Identify these directly rather than framing them as an authorial disclaimer or a list of questions left for others.

## State the supported scope directly in the manuscript

Build the text around the system under study, the mechanism or theoretical relationship, the evidence, and the results. Readers should understand what happens, the basis for that conclusion, and the insight it provides. Each sentence should perform new scientific work. Rather than describing what the authors have not studied, proved, or claimed, state directly the objects, settings, conditions, and evidence types for which the result holds.

Decide where a boundary belongs by asking whether readers need it to interpret the adjacent conclusion correctly:

- If removing it would turn an approximation into an exact result, a numerical fit into a theorem, or an entanglement witness into a Bell test, state the approximation, fit, or certified property in the result sentence itself. Usually one clear local statement is enough; this is not permission to append what has not been proved or tested.
- If it concerns an unperformed operation, unsolved extension, or different apparatus, omit that inventory. Its relevance to the present topic does not make it a result. Do not move it to the Discussion, ending, or a limitations section.
- If the negative statement is itself a finding, such as a no-go result, null result, counterexample, excluded mechanism, or boundary of a proof, state it directly as scientific content and retain it in the argument.

A standalone abstract, principal result, and independently readable caption each require enough conditions to be understood correctly. Necessary restatement across those locations is not mechanical repetition.

## Appendices and Supplemental Material

The same standard applies to supporting proofs, methods, convergence checks, End Matter, and supplementary captions. Their purpose is to establish or reproduce a specific result. State the relevant model and conditions, carry out the derivation or comparison, and explain its consequence for the main text. Keep information needed to interpret a null result or a proof's domain; remove author-centered defenses and inventories of work not performed. A deleted main-text caveat must not reappear merely because the Supplement has more space.

Use the same [punctuation and literature wording](prose-conventions.md) in these supporting passages. Their additional technical detail does not require narrative colons, explanatory dashes, publication-status labels or preprint numbers. Mathematical notation, heading joins and bibliography metadata retain their distinct roles.

For example, when the supplied calculation gives a decay under a constant Markovian generator, state that generator and the decay law. A list of unstudied devices or noise environments adds no support. When shared disorder realizations determine a comparison's uncertainty, retain the pairing and covariance requirement: that changes the statistical inference. These are scientific decisions, not a ban on negative sentences. Apply the same check to independently read supporting sections, with enough local definitions and assumptions to make each derivation usable.

## Delete, rewrite, or retain

First determine what scientific information the sentence adds, then choose the action. The categories and checklist need not be delivered to the user.

**Delete:** A sentence merely says "we do not claim," "we have not proved," "remains unresolved," or otherwise reports an unfinished task. Delete it even at its first occurrence and even when the task concerns the same system. If the adjacent result needs a condition, add that supported condition to the result instead of retaining the disclaimer.

**Rewrite:** The sentence contains useful information but is framed around what the authors did not do. State the established object, conditions, evidence type, or observable result directly. The positive form comes from the expression, not from a stronger conclusion. “Not yet proved” cannot become “observed,” “numerically supported,” or “false” unless the source materials provide the corresponding evidence.

If one sentence combines a necessary assumption with an unperformed extension, retain the assumption and omit the extension. Analyze a particular open scientific question as a separate task only when the user explicitly requests it. The fact that work was not performed is not itself a result of the present paper.

**Retain:** The sentence supplies an actual condition of applicability, counterexample, measured negative result, or reproducible evaluation design. Preserve that scientific content directly. An inventory of absent proof, deployment, validation, or generalization does not become indispensable merely by being called an "evidence boundary". Reducing the number of negative words is not an editing objective.

## English revision examples

The following are original synthetic examples, not quotations from or research results of the papers listed below. Use them only when the source materials actually contain the corresponding information.

### 1. Remove repetition without removing the approximation

Before: “Within the second-order approximation, the linewidth decreases with detuning. We do not claim that this is an exact result. The prediction is limited to the second-order approximation.”

After: “Within the second-order approximation, the linewidth decreases with detuning.”

The first sentence already states the condition; the next two add no information.

### 2. State the observable evidence without promoting a fit to a law

Before: “We do not claim to have proved quadratic scaling. A fit to the data for N = 8, 16, and 32 gives τ ∝ N².”

After: “For N = 8, 16, and 32, a fit to the data gives τ ∝ N².”

The finite sizes and the word “fit” already establish the evidence type. Do not rewrite this as “The relaxation time scales quadratically in the thermodynamic limit.”

### 3. Retain only the supported domain

Before: “For N = 8, 16, and 32, the calculated gap is positive. We have not proved that the gap remains finite as N → ∞.”

After: “The calculated gap is positive for N = 8, 16, and 32.”

The manuscript's conclusion concerns calculations at three sizes; do not add a thermodynamic-limit sentence. If the input contains only “not yet proved” and no positive result, remove the defensive sentence and request the genuinely needed result in the task note. Do not invent finite-size calculations or a universal theorem.

### 4. Retain the assumption and omit the unrelated extension

Before: “We assume Markovian dephasing and have not investigated colored noise. Under this assumption, the coherence decays exponentially.”

After: “Under Markovian dephasing, the coherence decays exponentially.”

The Markovian condition remains next to the result. Colored noise does not reappear in the discussion or ending.

### 5. Change the subject while preserving the interpretive boundary of the evidence

Before: “The calibrated witness certifies entanglement. We do not claim a Bell-inequality violation. We emphasize that this is not a test excluding local hidden-variable models.”

After: “The calibrated witness certifies entanglement.”

Delimit the interpretation through the property actually certified. Retain entanglement as the conclusion throughout, with the established calibration assumptions; do not rename it Bell nonlocality. If the paper actually compares the two tests, explain their mathematical criteria, observables, and assumptions as scientific content rather than adding an authorial disclaimer.

### 6. Omit an unstudied capability without adding a new promise

Before, results: “The measured coherence time is 12 μs. We have not demonstrated dissipative stabilization, and whether this setup can support it is still unknown.”

After: “The measured coherence time is 12 μs.”

Do not add an outlook on dissipative stabilization or rewrite this as “The setup provides a route to dissipative stabilization.”

### 7. Retain a genuine negative result

Before: “We do not find a statistically resolved difference between the two preparations: Δ = 0.01 ± 0.03.”

After: “The two preparations show no statistically resolved difference, Δ = 0.01 ± 0.03.”

Here, “no difference” is a measurement conclusion rather than authorial self-defense. It does not mean the two preparations are exactly identical.

### 8. Retain counterexamples and proof boundaries

Before: “We prove uniqueness for a finite irreducible chain. We do not claim uniqueness for a reducible chain: the two disconnected components each support a stationary state.”

After: “For a finite irreducible chain, the stationary state is unique. Two disconnected components each support a stationary state, so uniqueness need not hold for a reducible chain.”

Preserve the assumption and concrete counterexample; do not strengthen “need not” into “never.” Even if the abstract already states irreducibility, the full theorem in the main text still needs the condition.

### 9. Name the completed evaluation and remove the deployment inventory

Before: "Independent local-response tests give a low mean target-wise error for arrays with up to 16 sites. The selected channels have not been deployed jointly, so the results do not yet constitute a validated array-calibration protocol. Cross-platform transfer remains unresolved. Future work should measure the joint-deployment cost."

After: "Independent local-response tests give a low mean target-wise error for arrays with up to 16 sites."

"Independent local-response tests" identifies the completed evaluation. Retain that design and the tested sizes, then omit the undone deployment, unresolved extension, and future task. Do not rewrite the result as a complete-array calibration or an experimentally demonstrated deployment.

## Final manuscript pass

Inspect the actual revised prose, including its last paragraphs and all supporting material. Locate phrases equivalent to "we do not claim", "has not been done", "remains unresolved", "not yet validated", "does not yet constitute", and "future work should" in the requested language. Check their function, not just their spelling. Delete inventories of unfinished work; rewrite a mixed sentence to retain its completed result or necessary method condition. Read again to ensure the deleted claim has not reappeared as a synonym, future promise, or qualification elsewhere.

Confirm that actual approximations, simulation or experiment status, tested sizes, measurement uncertainty, citation keys, and genuine negative findings remain intact. A word search is only a review aid. Keep a necessary process-status report or a request for an indispensable missing input outside the manuscript; this editorial rule never turns an unexecuted validation into a passed test.

## Literature basis: examine placement and function, not counts of negative sentences

These are a small number of examples whose main text was checked in the source review. They support editorial judgment, not mandatory APS rules, universal frequency claims, or a fixed manuscript structure.

- [ATLAS, Measurements of Z-Boson Pair Entanglement…](https://doi.org/10.1103/y1nh-1b82), published PRL, PDF page 2: while explaining the assumptions needed to interpret angular correlations and quantum inseparability, the paper distinguishes its study from testing alternatives to quantum mechanics through Bell inequalities. This illustrates why a necessary interpretive boundary belongs beside the relevant claim rather than always being moved to the discussion.
- [Durst et al., Anisotropic and Nonadditive Interactions…](https://doi.org/10.1103/38vj-6fqc), published PRL: the abstract proceeds through the framework, Rydberg platform, interaction mechanism, and resonance result; page 3 states the trimer truncation at the actual calculation; the ending on page 4 discusses extensions to other impurity systems and bipolarons. This records how that paper places computational conditions and future extensions. It does not establish a requirement in this skill to retain unperformed work.
- [Ramírez et al., Superradiant Phase Is a Finite Size Effect…](https://doi.org/10.1103/syq9-z93n), published PRL, ending on PDF page 5: whether dissipation can stabilize a genuine superradiant phase remains open. The paper's negative and finite-size results are findings in the main text. Its choice to discuss an open question does not justify adding an outlook by default under this skill.

These papers do use negative sentences. The useful lessons are the focus of the physical argument and the reasons and locations for necessary conditions. This skill's default is to omit inventories of unperformed work, including related extensions, while stating the actual result and its conditions directly.
