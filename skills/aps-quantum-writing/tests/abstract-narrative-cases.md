# Abstract revision acceptance scenarios

These are editorial regression scenarios, not automated measurements of model performance. Prepared 2026-10-21. Use source facts as constraints and inspect a generated abstract against the expected behavior. Static review of the rules is reported separately; no claim is made that these cases have passed repeated model runs or an A/B test.

## A. Pure theorem and construction

Input: A polynomial-time quantum construction improves a proven approximation guarantee for a specified Hamiltonian family. No wall-clock benchmark or classical runtime separation is established.

Expected: Explain the improved achievable guarantee and the state-preparation/task consequence, retain the Hamiltonian family and efficiency conditions, and distinguish constructivity from existence. Do not manufacture a mechanism, hardware demonstration, or speedup. The abstract may be a complete theoretical story.

## B. Ambiguous demonstration verb

Input: The draft says “we demonstrate”; available evidence consists of finite-size numerical simulations only.

Expected: State numerical evidence, system sizes/regime when consequential, and the actual result. Do not turn “demonstrate” into an experimental observation or numerical agreement into proof of thermodynamic-limit behavior.

## C. Bit flips and coherent information

Input: A device has a very long bit-flip time but cannot prepare the coherent superposition required for a quantum memory in the reported experiment.

Expected: Preserve the measured achievement and the limitation that determines its interpretation. Do not claim a complete quantum memory, logical qubit operation, or scalable error correction. Affirmative scope can streamline prose but must not hide the missing capability.

## D. Valid formalism-first abstract

Input: An exact master-equation representation and a variational principle uniquely define work and heat in a stated model setting. These formal objects are the main contribution.

Expected: Keep enough formalism to explain why the definitions are meaningful. Do not remove all method names or insert generic quantum-technology motivation. Connect the principle to the physical quantities it fixes.

## E. PRA Letter versus Regular Article

Input: The same evidence is being organized for a PRA Letter, then a PRA Regular Article.

Expected: For the Letter, follow the current author-linked problem → main finding → work → broader context instruction, preserving the recommended sentence ranges as stated in that instruction. For the Regular Article, do not impose this sequence/count as an official universal rule. Neither version may change the scientific claims.

## F. Technical abstract versus Popular Summary

Input: A PRX Quantum theory paper requires both items.

Expected: Preserve the technical assumptions and mathematical/operational result in the abstract. Write the summary separately for its audience and applicable current rules. Do not impose the Popular Summary's approximate length guidance on the abstract or merely rename the same paragraph.

## G. Coherent paragraph without causal invention

Input: Two independent measurements support the same interpretation, but neither causes the other.

Expected: Explain their complementary role. Avoid “therefore” where it asserts unsupported causation. Global topic continuity matters as well as adjacent transitions.

## H. Method with a restricted domain

Input: A low-depth simulation method applies to random-unitary channels, not arbitrary channels.

Expected: Include the domain near the claim and explain the structural reason for the method. Do not simplify into arbitrary open-system simulation. Physical significance may be access to this channel class rather than discovery of a new mechanism.

## I. Applied tradeoff

Input: A feedback method suppresses long-term drift while slightly increasing shot-to-shot fluctuations.

Expected: State the useful improvement and the relevant tradeoff; do not say all noise is reduced. The closing sentence may be the concrete tradeoff rather than a broad applications claim.

## J. PRB finite-model boundary

Input: A model calculation produces monotonic energy decrease toward a lowest-energy state in the accessible symmetry sector. Implementation cost is not established.

Expected: Keep sector and model qualifications. Do not imply arbitrary global ground-state preparation, polynomial total algorithmic complexity, or a realized device.

## K. PRX platform and projections

Input: Hundreds of modes are demonstrated; a route toward tens of thousands is proposed.

Expected: Organize performance and limiting physics around usable scaling, preserving observed versus proposed sizes. No “paradigm revolution” is required.

## L. Contradictory formal length sources

Input: A guide gives a PRL character limit while published abstracts exceed it.

Expected: Record the conflict and verify the applicable current instructions; never change characters to words or claim the draft is compliant merely because a sample is longer. Do not present an arbitrary sampled length as an official rule.

## M. Essential idea hidden behind a generic label

Input: The supplied research establishes a result through an identifiable key idea, but the candidate abstract describes only an unnamed “framework” or “approach.”

Expected: Explain what the key idea does and why it matters for the result. The required content comes from the supplied research, not a prescribed technique. Avoid reproducing routine procedures or every intermediate argument.

## N. Core reasoning removed for a smoother story

Input: A draft states the contribution, names the method, and describes its significance, but leaves the reader unable to see why the method or evidence supports the result.

Expected: Restore the necessary inferential or evidential connection. Do not invent causation or demand a specific proof style. Natural prose cannot substitute for a missing scientific relationship.

## O. All ingredients present but narration fragmented

Input: A paragraph separately lists a contribution, a method, a result, and an importance claim, joined by generic transition words.

Expected: Organize these around their actual scientific relationships, clarify referents, and adjust information order and sentence load for comprehension. No fixed order is required. Mere inclusion of all ingredients does not pass.

## P. A reference example dictates the new manuscript

Input: A writing example is clear and successful, but the manuscript being edited addresses a different question through a different kind of contribution and evidence.

Expected: Transfer only the writing principles: identifiable contribution, decisive idea, warranted reasoning, coherent information order, and supported significance. Do not copy the example's scientific objects, method, proof route, claim type, or sentence sequence. Distinguish inherited knowledge from the new contribution using the manuscript's actual prior-work comparison.

## Review rubric, including the core-content requirement

For each output, inspect factual preservation; the organizing contribution; the core method and its logical link to the result; local and global continuity; supported physical or operational meaning; evidence status and boundaries; journal/article-type fit; and separation of abstract, summary, and suitability statement. Critical failures include an omitted or obscured essential method, invented results/causation, evidence-level upgrades, omitted truth-changing scope, or false official requirements. A fluent paragraph can still fail.
