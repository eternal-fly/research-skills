# Full-manuscript and Supplemental Material behavior review

Date: 2026-10-22. Method: bounded, non-blind qualitative review of synthetic
scientific premises and completed manuscripts. This record concerns actual
generated prose, not a search for required phrases in skill instructions.

## Design and artifacts

Three fixed [requests](../../tests/maintext-narrative-cases/) each asked for a
complete compact main manuscript (title, abstract, introduction, model/task,
developed results or proof, conclusion) and a substantive Supplement. The
requests supplied equations, assumptions, data or exact results, including
defensively worded source notes. They required English prose and prohibited
invented references, results and external searches. No real private manuscript
was used. These are short synthetic research-article applications, not complete
submission packages: no bibliography, TeX compilation or manuscript figures
were requested.

One fresh agent per case used the unmodified supplied rc1 skill. Three other
fresh agents used the revised writing rules. They did not see the other arm's
outputs or the review rubric. Each complete artifact includes its Supplement;
these are **six manuscripts with six Supplements**, not twelve independent
manuscript tests. Consulted-resource and execution-limit records are retained
beside the raw outputs. Only local path prefixes in process records were
normalized; the generated manuscripts were not edited after evaluation.

The release integrator read all six main texts and all six Supplements against
the nine criteria in [rubric.json](rubric.json). The evaluator knew the version
and supplied facts. There is no blinded scoring, sampling-based success rate,
or causal improvement estimate. Small wording and equation-reference style
differences are not scientific or narrative failures.

## Case findings

| Case and outputs | Question, idea and reasoning | Physical answer and supporting material | Review |
|---|---|---|---|
| PRA encoding: [rc1](baseline/theory.md), [revised](revised/theory.md) | Both explain why collective noise and a differential signal must act differently on the same encoding before restricting the generator. Invariance precedes use of the reduced equation. | Both recover constant populations and coherence exp(-4 epsilon t - 2 i delta t). The factor four, phase convention, initial support and constant Markovian parameters remain explicit. The Supplement derives the operator restriction and connects it to the main readout. | No critical failure in either arm. |
| PRB finite-size memory: [rc1](baseline/finite_size.md), [revised](revised/finite_size.md) | Both connect the plateau question to size comparisons and later-window comparisons, rather than listing the table. All eight rows of supplied means and SEMs are retained. | Both distinguish stronger finite-time retention from an undetermined infinite-time thermodynamic plateau. The Supplement derives SEM and the covariance term needed for paired differences; no paired significance is fabricated. Independent-size endpoint SEM is approximately 0.033 at W=6. | No critical failure in either arm. |
| PRX Quantum estimator: [rc1](baseline/estimator.md), [revised](revised/estimator.md) | Both introduce observable attenuation and inversion before variance and concentration. The inverse response explains both unbiasedness and its sampling cost. | Both retain known fixed p, independent shots, exact variance, a sufficient rather than optimal concentration bound, fixed calibration mismatch and clipping bias. The Supplement supplies derivations instead of unrelated hardware/advantage disclaimers. | No critical failure in either arm. |

In the revised theory case, the introduction says the collective coupling must
fail to distinguish the basis states while the differential Hamiltonian must
distinguish them. The subsequent generator calculation establishes exactly that
idea. Its Supplement begins by identifying the main-text equation it derives.
This is an observed question-to-idea-to-proof connection, not merely the
presence of the words “question” and “proof.”

In the revised finite-size case, uncertainty stays attached to the inference:
the window comparison needs covariance because the same disorder realizations
are reused. The independent-size comparison uses a different sampling relation.
The ending answers the memory question with finite-domain evidence; it does not
invent a mechanism or thermodynamic limit to make the narrative sound complete.

In the revised estimator case, the text explains that a target error eta
corresponds to an error a*eta in the attenuated measured mean. This connects the
concentration step to the physical measurement response. The Supplement's
one-shot clipping counterexample preserves a genuine negative result without
authorial self-defense.

## Short supporting-prose controls

Five distinct [short passages](../../tests/maintext-narrative-cases/micro.md)
were each rewritten once without a writing skill and once with the revised
skill. The same five passages were bundled in one agent per arm, so these are
five applications per condition, not five independent agent repetitions.
The control agent completed these passages before reading rc1 for the estimator
case; the revised agent completed its passages before its revised estimator
manuscript. Thus the estimator cases have this disclosed preceding task.

All ten rewrites were read in full: [control](micro-control.md),
[revised](micro-revised.md). Three control cases retained clearly unrelated
omissions: “Colored noise and laboratory drift lie outside the scope,” an
experimental-performance/quantum-advantage list, and “other disorder
distributions were not compared.” These are the observed style failures, not
inferred failures of rc1. The convergence and time-window cases were treated
as interpretive-boundary examples rather than penalized for negative words.

All five revised passages retain their supplied scientific facts while removing
the unrelated inventories. In particular, the constant Markovian condition,
the two basis-size values, exact noiseless-circuit probabilities, the 25-sample
SEM and finite time window, and the shared 20 disorder realizations with paired
SD all remain. No uncertainty is promoted to certainty. The narrow change made
the direct-prose rule explicitly apply to supporting material and forbids merely
relocating deleted defenses there.

## Interpretation and limits

The supplied rc1 already produced coherent full manuscripts in these cases.
The new body guidance consolidates the whole-paper reasoning path, and the
supporting-material route makes the user's requested scope explicit. These
results establish that the revised skill was actually applied to complete
synthetic main texts and Supplements. They do **not** show that 1.2.0 improves
upon rc1, that every manuscript will succeed, or that all seven journal types
were behavior-tested. The no-skill micro-control does not isolate the effect
of the small rc1-to-final wording change from the rest of the skill.

The cases use stipulated scientific premises, with straightforward deductions
checked during editorial review. They do not reproduce spin-chain simulations,
establish new physical discoveries, or certify arbitrary manuscript proofs.
The 1.1.0 abstract cases, original historical reviews and heading compilation
remain separate dated evidence, not additional executions in this campaign.
