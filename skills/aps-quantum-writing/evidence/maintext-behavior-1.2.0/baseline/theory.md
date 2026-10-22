**Synthetic editorial test**

# Differential-field sensitivity in a two-qubit encoding protected from collective dephasing

## ABSTRACT

A two-qubit encoding can retain a differential longitudinal-field signal while suppressing collective Markovian dephasing. The states |01⟩ and |10⟩ have the same eigenvalue of the collective coupling but opposite eigenvalues of the differential coupling. Restricting the master equation to their span therefore removes both collective dephasing and the common field, while retaining a logical Hamiltonian proportional to the differential field. The encoded coherence acquires a phase at angular frequency 2δ and decays at rate 4ε, where ε is the coefficient of each independent dephasing channel. This exact evolution gives an oscillatory logical-qubit signal whose contrast is controlled entirely by independent dephasing; at ε = 0, the collective dephasing strength has no effect.

## I. INTRODUCTION

Longitudinal-field sensing uses the relative phase accumulated between states with different field-dependent energies. Dephasing acts directly on the same coherence, so preserving a phase signal requires distinguishing the desired coupling from the coupling responsible for its decay. In a two-qubit system, spatially common and differential fields provide such a distinction: the former couples to the sum of the two longitudinal operators, whereas the latter couples to their difference. The relevant question is whether a pair of states can be indistinguishable to the common coupling and still distinguishable to the differential coupling.

The states |01⟩ and |10⟩ meet these two requirements simultaneously. Each has zero total longitudinal polarization, but their differential polarizations have opposite signs. Encoding a qubit in their span consequently gives the common and differential terms different roles. A collective dephasing channel sees no difference between the logical basis states, while a differential field separates their energies and produces a relative phase. Protection of the coherence and retention of the signal can thus follow from the same choice of subspace.

This argument must also account for noise that acts independently on the two physical qubits. Although each independent longitudinal operator preserves the encoded subspace, it distinguishes the logical basis states and can therefore dephase their superposition. Here the full Markovian generator is restricted exactly to the encoded sector. Its solution identifies which terms disappear, which signal remains, and which rate sets the surviving coherence time. The resulting logical observable makes these distinctions explicit without requiring a perturbative comparison of collective and independent noise strengths.

## II. MODEL AND LOGICAL SUBSPACE

With ℏ = 1, the density operator obeys

\[
\frac{d\rho}{dt}=-i[H,\rho]
+\gamma\mathcal D[Z_1+Z_2]\rho
+\epsilon\bigl(\mathcal D[Z_1]\rho+\mathcal D[Z_2]\rho\bigr),
\tag{1}
\]

where

\[
H=\frac{\Omega}{2}(Z_1+Z_2)
+\frac{\delta}{2}(Z_1-Z_2),\qquad
\mathcal D[A]\rho=A\rho A^\dagger
-\frac12\{A^\dagger A,\rho\}.
\tag{2}
\]

All parameters are constant, and γ, ε ≥ 0. The Pauli convention is Z|0⟩ = |0⟩ and Z|1⟩ = −|1⟩. Thus Ω specifies the common-field term and δ the differential-field term, with their normalization fixed by Eq. (2). The coefficients γ and ε multiply the dissipators as written; the coherence-decay rates follow from the eigenvalue differences of their operators.

Define the logical basis and projector by

\[
|0_L\rangle=|01\rangle,\qquad
|1_L\rangle=|10\rangle,\qquad
P=|0_L\rangle\langle0_L|+|1_L\rangle\langle1_L|.
\tag{3}
\]

The initial state satisfies ρ(0) = Pρ(0)P. Within this subspace, the logical operators are

\[
Z_L=|0_L\rangle\langle0_L|-|1_L\rangle\langle1_L|,
\qquad
X_L=|0_L\rangle\langle1_L|+|1_L\rangle\langle0_L|.
\tag{4}
\]

Every operator in Eq. (1) is diagonal in the physical computational basis. In particular, the Hamiltonian and each dissipative operator preserve the span in Eq. (3). A state initially supported there therefore remains there throughout the evolution, and its dynamics can be represented by a two-dimensional density matrix. This invariance is what makes restriction to the logical sector an exact reduction of the stated master equation.

## III. EXACT ENCODED EVOLUTION

The decisive distinction between the two field components follows from their action on the logical basis. Writing S = Z₁ + Z₂ gives S|01⟩ = S|10⟩ = 0. Hence SP = PS = 0. For every supported density operator, both SρS and the anticommutator with S² vanish, so the collective dissipator contributes zero. The same identity removes the common-field Hamiltonian. By contrast, Z₁ − Z₂ has eigenvalues +2 and −2 on |0_L⟩ and |1_L⟩, respectively. Its restriction gives the nonzero logical Hamiltonian δZ_L.

The independent channels survive this reduction. On the logical subspace, Z₁ acts as Z_L and Z₂ acts as −Z_L. The sign reversal disappears in a dissipator, since its two occurrences of the jump operator have the same overall sign. Consequently, the two independent channels add, and Eq. (1) becomes

\[
\dot\rho_L=-i[\delta Z_L,\rho_L]
+2\epsilon\bigl(Z_L\rho_L Z_L-\rho_L\bigr).
\tag{5}
\]

Equation (5) contains neither Ω nor γ. Their disappearance is an operator identity within the invariant subspace, so it requires no limit on their magnitudes or on their ratio to ε.

To expose the separate effects on populations and phase, write

\[
\rho_L(t)=
\begin{pmatrix}
p(t)&c(t)\\
c(t)^*&1-p(t)
\end{pmatrix},\qquad
c(t)=\langle01|\rho(t)|10\rangle.
\tag{6}
\]

The diagonal elements of both terms in Eq. (5) vanish. The off-diagonal Hamiltonian term is −2iδc, while conjugation by Z_L changes c to −c. Thus

\[
\dot p=0,\qquad
\dot c=-(4\epsilon+2i\delta)c,
\qquad
c(t)=c(0)e^{-4\epsilon t-2i\delta t}.
\tag{7}
\]

The factor four has two sources: each physical dephasing channel contributes a decay rate 2ε to this coherence, and there are two channels. The negative phase sign follows from the ordering c = ρ₀₁,₁₀ and the energy difference +δ − (−δ) = 2δ. The Supplement derives both contributions directly from the physical operators.

## IV. DIFFERENTIAL-FIELD SIGNAL AND ITS CONTRAST

For an initial logical superposition

\[
|+_L\rangle=\frac{|01\rangle+|10\rangle}{\sqrt2},
\tag{8}
\]

the populations are one half and c(0) = 1/2. Since the expectation of X_L is c + c*, Eq. (7) yields

\[
\langle X_L(t)\rangle=e^{-4\epsilon t}\cos(2\delta t).
\tag{9}
\]

The signal separates differential-field phase accumulation from independent-noise loss of contrast. Its oscillatory part depends on δ, while its envelope depends on ε. Neither the common field nor collective dephasing changes this logical observable. Retained sensitivity here means that the encoded coherence carries a differential-field-dependent phase, which appears in Eq. (9) as an oscillation; the result specifies the signal rather than an estimation protocol.

At ε = 0, the encoded state evolves unitarily under δZ_L for arbitrary γ ≥ 0. The logical coherence keeps its initial magnitude, and the superposition in Eq. (8) has unit oscillation contrast. For ε > 0, its contrast instead decays with characteristic time 1/(4ε). Increasing γ does not change that time, because the collective channel already vanishes on the subspace. Independent dephasing remains dynamically active even though it also preserves the populations and the encoded support.

The preparation of coherence is essential to the field response. A density matrix diagonal in the logical basis has c(0) = 0 and is stationary under Eq. (5); the differential field changes no relative phase observable in such a state. The superposition in Eq. (8) supplies the coherence on which the retained Hamiltonian acts. Encoding therefore selects the coupling that is suppressed, while the initial logical state determines whether the surviving coupling produces an observable signal. This protection is passive: the specified evolution contains no recovery operation or feedback step.

## V. CONCLUSION

A two-qubit state supported on span{|01⟩, |10⟩} can retain a differential longitudinal-field signal while eliminating collective Markovian dephasing. The underlying structure is the coexistence of equal collective-coupling eigenvalues and opposite differential-coupling eigenvalues. It removes the collective dissipator and common field from the exact logical generator while preserving a logical energy splitting of 2δ. Independent dephasing gives the remaining coherence decay, with rate 4ε in the stated normalization. The logical X signal consequently exhibits differential-field oscillations whose contrast is independent of γ. Within this invariant subspace, the distinction between common and independent noise directly determines which phase information survives.

---

## SUPPLEMENTAL MATERIAL

### S1. Exact restriction of the generator

Use the ordered physical basis {|00⟩, |01⟩, |10⟩, |11⟩}. The longitudinal operators and Hamiltonian are diagonal:

\[
Z_1=\operatorname{diag}(1,1,-1,-1),\qquad
Z_2=\operatorname{diag}(1,-1,1,-1),
\tag{S1}
\]

\[
S=Z_1+Z_2=\operatorname{diag}(2,0,0,-2),\qquad
H=\operatorname{diag}(\Omega,\delta,-\delta,-\Omega).
\tag{S2}
\]

Let V = |01⟩⟨0| + |10⟩⟨1| be the isometry from a two-dimensional logical space, so V†V = I_L and VV† = P. These diagonal operators leave the image of V invariant. For a supported state ρ = Vρ_LV†, applying any term of the master equation therefore gives another supported operator. This establishes invariance before the reduction is made, rather than assuming that projection alone defines a closed evolution.

In the ordered logical basis {|0_L⟩, |1_L⟩},

\[
V^\dagger SV=0,\quad
V^\dagger HV=\delta Z_L,\quad
V^\dagger Z_1V=Z_L,\quad
V^\dagger Z_2V=-Z_L.
\tag{S3}
\]

Because SV = 0, all three terms in 𝒟[S]ρ vanish separately. For each independent channel, the anticommutator simplifies using Z_j² = I. Invariance also gives Z_jV = V(±Z_L), so conjugation reduces exactly to Z_Lρ_LZ_L. The two contributions are identical. Multiplication of the full equation by V† and V thus yields

\[
\dot\rho_L=-i[\delta Z_L,\rho_L]
+2\epsilon\mathcal D[Z_L]\rho_L,
\qquad
\mathcal D[Z_L]\rho_L=Z_L\rho_L Z_L-\rho_L.
\tag{S4}
\]

### S2. Coherence decay and phase convention

The decay coefficient can also be computed without logical notation. For a Hermitian operator A diagonal on states |m⟩ and |n⟩, with eigenvalues a_m and a_n, its dissipator acts on a matrix unit as

\[
\mathcal D[A](|m\rangle\langle n|)
=\left[a_ma_n-\frac{a_m^2+a_n^2}{2}\right]
|m\rangle\langle n|
=-\frac{(a_m-a_n)^2}{2}|m\rangle\langle n|.
\tag{S5}
\]

Take E = |01⟩⟨10|. For S, both eigenvalues are zero and Eq. (S5) gives 𝒟[S]E = 0. For Z₁, the eigenvalues are +1 and −1, yielding 𝒟[Z₁]E = −2E. For Z₂, their order is reversed, but their squared difference is again four, so 𝒟[Z₂]E = −2E. Multiplying each independent term by ε gives the total contribution −4εE. For either diagonal matrix unit, the eigenvalue difference vanishes in every channel, explaining the constant populations.

The normalization can be checked term by term. For either physical Z operator, the recycling term Z_jEZ_j equals −E. Its anticommutator term is also −E because Z_j² = I. Each channel therefore contributes two equal negative terms to the coherence equation. The coefficient ε describes one physical dissipator, whereas the rate 4ε describes the combined decay of this particular encoded matrix element.

Equation (S2) assigns energies +δ and −δ to |01⟩ and |10⟩. Therefore [H,E] = 2δE, and the Hamiltonian part of the generator is −2iδE. Since c denotes the coefficient of E in the density operator, its closed equation and solution are

\[
\dot c=(-4\epsilon-2i\delta)c,
\qquad c(t)=c(0)\exp[-4\epsilon t-2i\delta t].
\tag{S6}
\]

The conjugate matrix element multiplies E† and has the opposite phase. This sign convention also follows from the unitary factors: |01⟩ acquires e^(−iδt), whereas |10⟩ acquires e^(+iδt), giving e^(−2iδt) in |01⟩⟨10|. Independent dephasing multiplies that phase evolution by the real envelope e^(−4εt).

For |+_L⟩, the resulting density matrix is

\[
\rho_L(t)=\frac12
\begin{pmatrix}
1&e^{-4\epsilon t-2i\delta t}\\
e^{-4\epsilon t+2i\delta t}&1
\end{pmatrix}.
\tag{S7}
\]

Taking its trace with X_L adds the two off-diagonal elements and gives Eq. (9). These derivations are exact for constant parameters and supported initial states, including ε = 0 and γ = 0.
