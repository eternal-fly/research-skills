# Remove Defensive Prose: Let the Physical Results Carry the Argument

Use this reference when the user explicitly asks to remove self-defense or repeated qualifications, or when such sentences interrupt the physical argument. It draws on PRL's narrative logic without forcing manuscripts into a fixed paragraph template.

## State the supported scope directly in the manuscript

Build the text around the system under study, the mechanism or theoretical relationship, the evidence, and the results. Readers should understand what happens, the basis for that conclusion, and the insight it provides. Each sentence should perform new scientific work. Rather than describing what the authors have not studied, proved, or claimed, state directly the objects, settings, conditions, and evidence types for which the result holds.

Decide where a boundary belongs by asking whether readers need it to interpret the adjacent conclusion correctly:

- If removing it would turn an approximation into an exact result, a numerical fit into a theorem, or an entanglement witness into a Bell test, retain it beside the relevant definition, result, or explanation. Usually one clear local statement is enough.
- If it concerns only an unperformed extension, a different apparatus, or a matter unrelated to the present claim, omit it. Do not automatically move it to the Discussion, ending, or a limitations section.
- If the negative statement is itself a finding, such as a no-go result, null result, counterexample, excluded mechanism, or boundary of a proof, state it directly as scientific content and retain it in the argument.

A standalone abstract, principal result, and independently readable caption each require enough conditions to be understood correctly. Necessary restatement across those locations is not mechanical repetition.

## Appendices and Supplemental Material

The same standard applies to supporting proofs, methods, convergence checks, End Matter, and supplementary captions. Their purpose is to establish or reproduce a specific result. State the relevant model and conditions, carry out the derivation or comparison, and explain its consequence for the main text. Keep information needed to interpret a null result or a proof's domain; remove author-centered defenses and unrelated inventories of work not performed. A deleted main-text caveat must not reappear merely because the Supplement has more space.

For example, when the supplied calculation gives a decay under a constant Markovian generator, state that generator and the decay law. A list of unstudied devices or noise environments adds no support. When shared disorder realizations determine a comparison's uncertainty, retain the pairing and covariance requirement: that changes the statistical inference. These are scientific decisions, not a ban on negative sentences. Apply the same check to independently read supporting sections, with enough local definitions and assumptions to make each derivation usable.

## Delete, rewrite, or retain

First determine what scientific information the sentence adds, then choose the action. The categories and checklist need not be delivered to the user.

**Delete:** The scope and evidence strength have already been stated locally, and the next sentence merely repeats “we do not claim,” “we have not proved,” or “this does not imply” as self-defense. Remove the repeated sentence and let the argument continue.

**Rewrite:** The sentence contains useful information but is framed around what the authors did not do. State the established object, conditions, evidence type, or observable result directly. The positive form comes from the expression, not from a stronger conclusion. “Not yet proved” cannot become “observed,” “numerically supported,” or “false” unless the source materials provide the corresponding evidence.

If one sentence combines a necessary assumption with an unperformed extension, retain the assumption and omit the extension. Analyze a particular open scientific question as a task only when the user explicitly requests it. The fact that work was not performed is not itself a result of the present paper.

**Retain:** The sentence supplies a condition of applicability, counterexample, negative result, or interpretive boundary indispensable to the present conclusion. Preserve the scientific content, shortening the phrasing if useful. Reducing the number of negative words is not an editing objective.

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

## Literature basis: examine placement and function, not counts of negative sentences

These are a small number of examples whose main text was checked in the source review. They support editorial judgment, not mandatory APS rules, universal frequency claims, or a fixed manuscript structure.

- [ATLAS, Measurements of Z-Boson Pair Entanglement…](https://doi.org/10.1103/y1nh-1b82), published PRL, PDF page 2: while explaining the assumptions needed to interpret angular correlations and quantum inseparability, the paper distinguishes its study from testing alternatives to quantum mechanics through Bell inequalities. This illustrates why a necessary interpretive boundary belongs beside the relevant claim rather than always being moved to the discussion.
- [Durst et al., Anisotropic and Nonadditive Interactions…](https://doi.org/10.1103/38vj-6fqc), published PRL: the abstract proceeds through the framework, Rydberg platform, interaction mechanism, and resonance result; page 3 states the trimer truncation at the actual calculation; the ending on page 4 discusses extensions to other impurity systems and bipolarons. This records how that paper places computational conditions and future extensions. It does not establish a requirement in this skill to retain unperformed work.
- [Ramírez et al., Superradiant Phase Is a Finite Size Effect…](https://doi.org/10.1103/syq9-z93n), published PRL, ending on PDF page 5: whether dissipation can stabilize a genuine superradiant phase remains open. The paper's negative and finite-size results are findings in the main text. Its choice to discuss an open question does not justify adding an outlook by default under this skill.

These papers do use negative sentences. The useful lessons are the focus of the physical argument and the reasons and locations for necessary conditions. This skill's default is to omit unrelated unperformed work.
