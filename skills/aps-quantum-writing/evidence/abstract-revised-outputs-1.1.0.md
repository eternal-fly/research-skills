# APS Quantum Writing: bounded qualitative application

These five abstracts apply the supplied skill to synthetic factual briefs. They are a one-shot qualitative application, not a performance benchmark or a validation of the underlying research.

## 1. PRA Letter

The narrowing of a response resonance in a dissipative system raises the question of which dynamical process controls its width. In a finite two-mode linear model, we show that tuning the coherent coupling narrows the resonance through transfer to the weakly damped mode. Exact poles identify the spectral change associated with this transfer. The time evolution provides a complementary dynamical account of the same process. A detuning control distinguishes this mechanism from an artifact of the drive amplitude. The correspondence between spectral and temporal evidence supplies a physical interpretation of resonance narrowing in terms of the coupled dissipative dynamics.

## 2. PRA Regular Article

An exact master-equation representation and a variational principle provide unique definitions of work and heat in the finite driven model considered here. Equivalent representations of the same evolution otherwise leave their assignment ambiguous. The variational principle resolves this freedom by selecting the minimum dissipative part from the equivalent representations. This selection gives the formal representation a thermodynamic role: it fixes the decomposition used to distinguish work from heat while retaining the exact dynamics of the model. The resulting definitions therefore follow from an explicit selection criterion, connecting the representation of the evolution to its energetic interpretation and resolving the ambiguity within the specified model.

## 3. PRX Quantum theory abstract

A known convex mixture of unitary channels specifies a quantum operation that can be implemented by sampling its components. We give an algorithm that draws a unitary according to the mixture weights and implements that unitary with circuit depth bounded by D. Averaging the resulting output over the sampling randomness reproduces the target random-unitary channel exactly. The equality follows because the probability of each implemented unitary is its weight in the channel decomposition. The guarantee thus concerns the expected output; an individual trajectory implements the sampled unitary and need not equal the mixed-channel output. This construction connects an ensemble channel description to a sampled implementation with a depth bound on each realization.

## 4. PRB

The evolution of correlations with interaction strength can be examined alongside spectral information to distinguish physical regimes in a finite lattice. For lattices of 12–24 sites, we find a correlation peak whose position shifts as the interaction strength varies. Independent spectral data support interpreting the observed behavior as a crossover. The correlation and spectral results serve as complementary diagnostics: their agreement supports a common interpretation of the finite-system behavior. This comparison connects the shifting correlation peak to a crossover picture while keeping the evidence at the sizes studied. The thermodynamic character of the behavior remains undetermined.

## 5. PRL

We improve the established approximation ratio from 0.60 to 0.62 for a specified family of sparse Hamiltonians by constructing states that attain a certified objective bound. The key step decomposes a feasible local moment matrix into preparable block states and combines these states with certified weights. This construction turns the information in the local moments into a reconstructed state whose objective value satisfies the claimed bound. Under bounded degree, both the decomposition and state preparation are polynomial in the number of sites. The result strengthens the guaranteed approximation within this Hamiltonian family and supplies a constructive connection between local moment feasibility and an attainable state objective.

## Files consulted

Only the following skill files were consulted:

- `SKILL.md`
- `references/branch-writing.md`
- `references/abstract-narrative.md`
- `references/pra.md`
- `references/prb.md`
- `references/prx-quantum.md`
- `references/prl.md`

No evaluation outputs, intake documents, underlying manuscripts, or external sources were consulted.

## Concrete uncertainties and missing inputs

- **PRA Letter:** The model equations, damping rates, coupling and detuning ranges, and magnitude of the resonance narrowing were not supplied. The abstract therefore does not assign a direction or amount to the coupling change, or a quantitative width to the resonance.
- **PRA Regular Article:** The driven model, class of equivalent representations, variational functional defining the minimum dissipative part, and conditions supporting uniqueness were not supplied. The abstract preserves the stated uniqueness of work and heat without asserting uniqueness of the full representation.
- **PRX Quantum:** The mixture, gate set, dependence of D on problem parameters, and cost of sampling were not supplied. The stated resource guarantee is the depth bound for implementing the sampled unitary; the brief does not support a total runtime or sampling-complexity claim.
- **PRB:** The lattice Hamiltonian and boundary conditions, the correlation observable, the coordinate and direction of the peak shift, and the specific spectral diagnostic were not supplied. These omissions prevent naming the regimes or a microscopic mechanism. The evidence supports the given finite-size crossover interpretation, with no thermodynamic transition established.
- **PRL:** The precise Hamiltonian family, optimization objective and ratio convention, local moment constraints, allowed block states, and certificate construction were not supplied. A fully specified theorem abstract would require these particulars; the draft preserves only the stated ratio, construction, and bounded-degree polynomial scaling.
- **Shared boundary:** The scientific statements were accepted as synthetic premises rather than independently verified. Current journal submission requirements were not checked externally. The skill itself flags a conflict in PRL abstract-length guidance, so these approximately 90–140-word drafts do not certify submission-format compliance.
