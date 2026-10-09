# Natural Scientific Prose: Make the Reasoning Connect

Use this reference when prose is templated, awkwardly translated, inflated, or excessively compressed. It does not require a separate style report for every manuscript. Making prose sound less machine-generated means improving scientific writing, not hiding tool use, evading detection, or promising a detector score. Handle any required author disclosure according to actual tool use and current journal requirements.

## Repair the logic before changing the voice

Identify the judgment readers should gain from the paragraph: what is known, which evidence changes the understanding, and how far the resulting claim can reach. Let each sentence take up a physical object, contradiction, quantity, or question from the preceding one. Connectives mark genuine relationships; they cannot replace reasoning. Causal words require causal evidence. A paragraph may include definitions, explanations, counterexamples, or turns in the argument; it need not always resolve into the same three-sentence rhythm.

Use stable terminology and specific verbs to describe physical relationships. Remove wording that merely announces importance, novelty, or noteworthiness while retaining sentences that carry objects, conditions, data, units, and explanations. Let reasoning determine sentence length. Avoid both chains of long modifiers and splitting necessary information into uniformly short sentences. Preserve original prose that is already natural and accurate. An uncommon word or a negative word is not automatically an error.

Aim for natural, elegant, readable prose. Restrained wit can be appropriate to the academic context, but do not add jokes to appear human. Prefer standard terminology and concrete explanation to undefined symbols, unclear references, or invented abstract nouns. New mathematical objects must be needed and clearly defined. Explain proofs in an order that supports understanding and discovery while checking their detailed dependencies internally.

After revision, compare the original and new scientific content: symbols, quantifiers, approximations, values and uncertainties, units, reference baselines, citations, and LaTeX commands must retain their meaning. Observations, fits, model-specific calculations, conjectures, and theorems must retain their evidence status. Following [direct scientific prose](prl-direct-prose.md), state the supported domain and conditions, and omit unrelated unperformed work. Preserve genuine no-go results, null results, counterexamples, and uncertainties in full.

## Original before-and-after examples

These are illustrations of writing. Their evidence must already exist in the input; do not treat them as ready-made scientific facts.

**Empty emphasis → an actual relationship**

Before: “It is important to emphasize that our highly versatile framework provides remarkable insights into the intricate interplay of coherent coupling and dissipation.”

After: “Coherent coupling transfers excitation between the two modes, while their unequal decay rates select the long-lived component.”

Use the revision only if the model and evidence establish these relationships. If the input supplies only a method name, obtain the scientific content first rather than creating a mechanism through rhetoric.

**A list of steps → a question-driven connection**

Before: “First, we calculate the spectrum. Furthermore, we simulate the dynamics. Finally, we compare the results.”

After: “The spectrum separates two decay rates. To identify their time-domain signatures, we resolve the population in each mode. The late-time decay follows the slower spectral component.”

This requires a spectrum, resolved dynamics, and the comparison result for the same model. Without the last piece of evidence, state only which relationship the calculation will test; the result sentence must wait for the actual calculation.

**Excessive compression → restored evidence status**

Before: “The lifetime scales as N².”

After: “A fit to the lifetimes at N = 8, 16, and 32 gives τ ∝ N².”

Here the input is a finite-size fit. Restore the sizes and the fact that it is a fit rather than repairing an extrapolation by adding “we have not proved…”

**Translation-like formality → a natural explanation**

Before: “It is worth noting that this method uses its unique capabilities to achieve deep insight into complex behavior.”

After: “Changing the relative phase of the two excitation paths broadens the response peak. The phase scan links the change in linewidth to interference between the paths.”

The input must contain the actual phase scan and corresponding evidence. Advance through physical relationships rather than aiming for empty formality.

## Short, ready-to-use prompts (original)

**Local revision:** “Rewrite this passage using the manuscript's model, evidence, and an appropriate APS tone. Make the sentence-to-sentence logic natural, preserving symbols, citations, numbers, conditions, and evidence levels. Leave already natural wording alone. State the supported domain and setting directly; remove unrelated unperformed work without replacing it with an ‘unresolved’ closing sentence. Explain proofs in an order readers can understand, define every symbol, and prefer standard terminology. Deliver the revised text, listing separately only gaps that affect scientific judgment.”

**Materials to a complete first draft:** “Use the supplied background, data, model, and literature to develop a complete APS working manuscript continuously. Resume from the existing state, addressing the background, article type, central claim, outline, working title, figure set, and main text, then revise the title/abstract and compile and check the manuscript. Continue wherever materials suffice; ask only about gaps that block scientific conclusions.”

**Final logic check:** “Check that the title, abstract, introductory question, main-text evidence, and conclusion express the same claim. Correct contradictions, reasoning gaps, and terminology drift that change the physics. Preserve accurate wording rather than editing for its own sake. Report compilation and figure checks actually completed, along with remaining blockers.”

For selectively adopted ideas and material not adopted, see [provenance](../docs/PROVENANCE.md). The examples and prompts are original to this skill, not excerpts from an upstream repository.
