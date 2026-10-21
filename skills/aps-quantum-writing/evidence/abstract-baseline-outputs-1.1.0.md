# APS Quantum Writing: bounded qualitative baseline

This is a one-shot qualitative baseline using the current skill tree and the five supplied synthetic scenarios. It is not a performance benchmark. The abstracts preserve the supplied claims without independently verifying the underlying research. No web sources, intake overlay, or abstract guides outside the specified tree were consulted.

## 1. PRA Letter

We examine how coherent coupling narrows a response resonance in a finite two-mode linear dissipative model. The narrowing is governed by transfer to the weakly damped mode. Exact poles of the response and the calculated time evolution identify the same transfer process, connecting the spectral feature to the dynamics of the two modes. A detuning control separates this mechanism from a drive-amplitude artifact. These complementary calculations establish how the coupled-mode dynamics produce the narrow response and identify the physical role of the weakly damped mode in the specified model.

## 2. PRA Regular Article

Separating work from heat can become ambiguous when equivalent master-equation representations assign different contributions to the same driven dynamics. We resolve this ambiguity for a specified finite driven model by combining an exact master-equation representation with a variational principle. The principle selects the minimum dissipative part among equivalent representations, thereby fixing a unique definition of work and heat within the model. The exact representation describes the dynamics, while the variational selection determines which decomposition is used for the thermodynamic assignment. This construction makes the role of the formalism explicit: it removes representation freedom from the work–heat distinction under the stated model assumptions.

## 3. PRX Quantum theory abstract

A quantum channel specified as a convex mixture of unitary operations admits a direct sampling implementation. We present an algorithm that draws a unitary according to the known mixture probabilities and implements it with circuit depth at most D. Averaging the resulting output states over the sampling reproduces the prescribed random-unitary channel exactly for every input state. The equality is an ensemble statement: an individual realization applies the sampled unitary channel. This establishes a depth-bounded implementation of the specified mixture, with the channel guarantee determined by the sampling distribution and the resource guarantee applying to the unitary executed in each realization.

## 4. PRB

We study the interaction dependence of a correlation peak in finite lattices containing 12–24 sites. The peak shifts as the interaction strength is varied, indicating a change in the correlation structure across the studied range. Independent spectral data support interpreting this behavior as a crossover. The correlation and spectral observations supply complementary evidence for the same finite-system interpretation, with neither serving as a causal explanation of the other. Their agreement supports a crossover description for these lattices and provides a consistent account of the interaction-dependent behavior at the sizes examined.

## 5. PRL

We establish a constructive approximation ratio of 0.62 for a specified family of sparse Hamiltonians, improving the established value of 0.60. The key step converts a feasible local moment matrix into a state that attains the required objective bound. We decompose the matrix into preparable block states and combine these states with certified weights, so that the reconstruction carries the matrix bound into the state objective. For bounded-degree Hamiltonians in this family, both the decomposition and state preparation are polynomial in the number of sites. The result makes the improved ratio attainable through an explicit construction under these assumptions.

## Files consulted

All paths below are relative to ``.

- `SKILL.md`
- `references/branch-writing.md`
- `references/branch-planning.md`
- `references/pra.md`
- `references/prb.md`
- `references/prx-quantum.md`
- `references/prl.md`
- `references/branch-format.md`
- `references/physics-narrative.md`
- `references/prl-direct-prose.md`
- `references/aps-format.md`

## Concrete uncertainties and missing inputs

The supplied facts suffice for these synthetic abstracts. A submission-ready version would require the following concrete identifiers or definitions; none were invented here.

1. **PRA Letter:** The model equations, damping rates, coupling and detuning ranges, and size of the linewidth change were not supplied. The abstract therefore gives no quantitative narrowing factor or additional time-domain feature.
2. **PRA Regular Article:** The finite model, admissible representation changes, mathematical measure of the dissipative part, and work and heat definitions were not supplied. The stated uniqueness is accepted as part of the scenario; its proof was not available for checking.
3. **PRX Quantum:** The mixture, gate set, dependence of D on problem parameters, and costs of sampling and specifying the unitaries were not supplied. Only the given per-realization unitary-depth bound and equality after averaging are stated.
4. **PRB:** The lattice model and geometry, correlation observable, variable on which the peak is located, direction of the shift, interaction range, uncertainties, and diagnostic spectral feature were not supplied. The article type was also unspecified. The conclusion remains a crossover interpretation for 12–24-site systems.
5. **PRL:** The Hamiltonian family, objective and approximation-ratio conventions, full theorem hypotheses, form of the certified weights, and polynomial exponents were not supplied. The two ratios and bounded-degree construction are accepted as stipulated; the theorem and certificate were not independently checked.

The journal-specific guidance was read locally. Current submission requirements were not rechecked online because this baseline explicitly excluded browsing.
