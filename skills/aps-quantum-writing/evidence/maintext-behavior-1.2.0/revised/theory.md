**Synthetic editorial test**

# Differential-field response in a two-qubit encoding under collective dephasing

## Abstract

A two-qubit encoding can preserve a differential longitudinal-field signal while eliminating collective Markovian dephasing. For states supported on $\{|01\rangle,|10\rangle\}$, both basis states have zero total $Z$, whereas their differential-field energies have opposite signs. Restricting the generator to this invariant subspace therefore removes the common field and collective dissipator while retaining the logical Hamiltonian $\delta Z_L$. Independent dephasing of strength $\epsilon$ on each qubit gives the exact coherence $c(t)=c(0)e^{-4\epsilon t-2i\delta t}$. An equal logical superposition consequently produces an oscillatory signal with contrast $e^{-4\epsilon t}$. The encoding separates the collective noise channel from the differential signal through their distinct actions on the same two states.

## I. INTRODUCTION

A longitudinal field changes the relative phase between states with different longitudinal polarization. This phase can carry a field signal, but dephasing can erase the coherence needed to read it. For two qubits, the spatial dependence of the coupling supplies an additional distinction: a common field couples to the sum of their polarizations, whereas a differential field couples to their difference. The question is whether a coherent two-state encoding can be insensitive to fluctuations in the sum while remaining responsive to the difference.

Suppressing a noise term is useful for this task only if the encoded states still accumulate a signal-dependent relative phase. If the signal Hamiltonian acts identically on both states, removing dephasing would preserve a coherence that carries no information about that signal. The encoding must therefore satisfy two conditions together: the collective coupling must fail to distinguish its basis states, and the differential Hamiltonian must distinguish them. These conditions concern the operators acting within the encoding, rather than the relative magnitudes of the field and noise parameters.

We examine these conditions for a constant Markovian generator containing collective and independent longitudinal dephasing. The states $|01\rangle$ and $|10\rangle$ each have zero total polarization but opposite polarization differences. This structure permits an exact reduction to one logical qubit. The reduction identifies which terms disappear, determines the residual coherence decay, and connects the resulting phase evolution to a logical observable. It also makes the role of independent dephasing explicit: that channel acts within the encoding and sets the decay of the field-dependent signal.

## II. MODEL AND ENCODING

With $\hbar=1$, the two-qubit density operator obeys

$$
\frac{d\rho}{dt}=-i[H,\rho]+\gamma\mathcal D[Z_1+Z_2]\rho
+\epsilon\bigl(\mathcal D[Z_1]\rho+\mathcal D[Z_2]\rho\bigr),
\tag{1}
$$

where

$$
H=\frac{\Omega}{2}(Z_1+Z_2)+\frac{\delta}{2}(Z_1-Z_2),\qquad
\mathcal D[A]\rho=A\rho A^\dagger-\frac12\{A^\dagger A,\rho\}.
\tag{2}
$$

The parameters are constant, $\gamma,\epsilon\geq0$, and $Z_1$ and $Z_2$ act on the first and second qubits. We use $Z|0\rangle=|0\rangle$ and $Z|1\rangle=-|1\rangle$. The parameter $\Omega$ sets the common field, while $\delta$ sets the differential field whose effect is to be retained.

Define the logical basis and its longitudinal and transverse operators by

$$
|0_L\rangle=|01\rangle,\quad |1_L\rangle=|10\rangle,\quad
Z_L=|0_L\rangle\langle0_L|-|1_L\rangle\langle1_L|,\quad
X_L=|0_L\rangle\langle1_L|+|1_L\rangle\langle0_L|.
\tag{3}
$$

The initial state has support on $\mathcal C=\operatorname{span}\{|0_L\rangle,|1_L\rangle\}$. Every operator in Eq. (1) is diagonal in the computational basis and maps $\mathcal C$ into itself. Its jump and anticommutator terms therefore preserve this support, so the logical description remains closed throughout the evolution. This invariance is necessary for interpreting a restriction of the generator as the full dynamics of an initially encoded state.

The task is to establish whether this closed evolution retains dependence on $\delta$ while eliminating dependence on $\gamma$. The common field and independent dephasing are kept in the calculation so that their distinct roles follow from the same reduction. The encoding is passive: the evolution in Eq. (1) contains no recovery operation.

## III. EXACT LOGICAL DYNAMICS

The cancellation of the collective terms follows directly from the two logical basis states. Their total-$Z$ eigenvalues are

$$
(Z_1+Z_2)|01\rangle=(1-1)|01\rangle=0,\qquad
(Z_1+Z_2)|10\rangle=(-1+1)|10\rangle=0.
\tag{4}
$$

Thus the common-field Hamiltonian vanishes on $\mathcal C$. For a density operator supported there, multiplication by $Z_1+Z_2$ on either side also gives zero. Both the jump term and the anticommutator in the collective dissipator vanish. This is an exact cancellation for any $\gamma$, with no requirement that collective dephasing be weak or that one rate dominate another.

The differential operator has a different restriction. Within $\mathcal C$, $Z_1$ becomes $Z_L$ and $Z_2$ becomes $-Z_L$, giving

$$
H_L=\delta Z_L,\qquad
\frac{d\rho_L}{dt}=-i[\delta Z_L,\rho_L]+2\epsilon\mathcal D[Z_L]\rho_L.
\tag{5}
$$

Here $\rho_L$ is the density matrix in the ordered basis $(|0_L\rangle,|1_L\rangle)$. The factor two multiplying the dissipator arises because $\mathcal D[-Z_L]=\mathcal D[Z_L]$. The opposite signs of the local couplings cancel in their sum, but their separate dissipative contributions add. This distinction explains why independent dephasing remains after collective dephasing has disappeared.

To see its effect on coherence, let $c=\langle0_L|\rho_L|1_L\rangle$. Conjugating this matrix element by $Z_L$ changes its sign, while the anticommutator contributes a second negative copy. Consequently $\mathcal D[Z_L]$ acts on the off-diagonal element as $-2c$. The two independent channels together give $-4\epsilon c$. The logical energies are $+\delta$ and $-\delta$, so the Hamiltonian contributes $-2i\delta c$. Therefore

$$
\dot c=(-4\epsilon-2i\delta)c,\qquad
c(t)=c(0)e^{-4\epsilon t-2i\delta t}.
\tag{6}
$$

The diagonal elements are constant because both the commutator and the dissipator vanish on them. Writing $p=\langle0_L|\rho_L(0)|0_L\rangle$, the complete solution is

$$
\rho_L(t)=
\begin{pmatrix}
p & c(0)e^{-4\epsilon t-2i\delta t}\\
c(0)^*e^{-4\epsilon t+2i\delta t} & 1-p
\end{pmatrix}.
\tag{7}
$$

Equation (7) establishes the result for every initial density operator supported on $\mathcal C$, including mixed states. The signal changes the coherence phase, independent dephasing changes its magnitude, and neither process transfers population between the logical basis states. The Supplement derives the generator on all four logical matrix units and fixes the phase convention explicitly.

## IV. DIFFERENTIAL-FIELD SIGNAL

An equal logical superposition makes the retained field dependence directly visible. For $|+_L\rangle=(|0_L\rangle+|1_L\rangle)/\sqrt2$, the initial coherence is $1/2$. Since $X_L$ reads twice its real part, Eq. (6) gives

$$
\langle X_L\rangle(t)=e^{-4\epsilon t}\cos(2\delta t).
\tag{8}
$$

The oscillation comes from the energy difference $2\delta$ between the logical states. The envelope comes from independent dephasing. Neither contains $\Omega$ or $\gamma$: the common field and collective noise have no action on the encoded state from which the signal is obtained.

Field sensitivity here means that the encoded coherence accumulates a differential-field-dependent phase. The chosen observable converts that phase into a cosine signal. At a fixed interrogation time its slope is $-2t e^{-4\epsilon t}\sin(2\delta t)$, so the local response of this readout depends on the phase at which it is evaluated. A zero slope at an extremum of the cosine is a property of this observable's response, while the coherence itself still carries the phase in Eq. (6). Constant logical populations, by comparison, carry no time-dependent field signal in this model.

When $\epsilon=0$, the encoded evolution is exactly unitary under $\delta Z_L$ for arbitrary collective dephasing strength. For $\epsilon>0$, the same phase evolution persists with a coherence decay time $(4\epsilon)^{-1}$. Increasing $\gamma$ cannot change that time because the collective dissipator is already zero on the entire supported state. The residual decay is therefore determined by the independent noise specified in the generator, rather than by incomplete cancellation of the collective channel.

## V. CONCLUSION

The two-qubit subspace spanned by $|01\rangle$ and $|10\rangle$ retains differential longitudinal-field evolution while eliminating collective Markovian dephasing. Its basis states share a zero collective eigenvalue and have opposite differential energies, allowing noise cancellation and signal accumulation to coexist. For initially supported states, the exact logical dynamics consist of the Hamiltonian $\delta Z_L$ and independent dephasing that damps coherence at rate $4\epsilon$. The resulting logical signal separates a field-dependent phase from a noise-dependent contrast. This passive encoding consequently selects the differential coupling through the symmetry of the two physical qubits.

---

# SUPPLEMENTAL MATERIAL

## S1. Restriction of the full generator

This derivation establishes Eq. (5) as the exact evolution of every density operator initially supported on $\mathcal C$. Let $P=|01\rangle\langle01|+|10\rangle\langle10|$ and assume $\rho(0)=P\rho(0)P$. The Hamiltonian and all three dephasing operators are diagonal in the computational basis. They commute with $P$ and map its range into itself. Their products in the dissipators have the same property; hence every term of $\dot\rho$ remains supported on $\mathcal C$ whenever $\rho$ does. The restriction introduces no approximation or additional dynamical assumption.

In the ordered logical basis $(|01\rangle,|10\rangle)$, the restricted operators are

$$
Z_1|_{\mathcal C}=\begin{pmatrix}1&0\\0&-1\end{pmatrix}=Z_L,
\qquad
Z_2|_{\mathcal C}=\begin{pmatrix}-1&0\\0&1\end{pmatrix}=-Z_L.
\tag{S1}
$$

It follows that $(Z_1+Z_2)P=0$ and $(Z_1-Z_2)|_{\mathcal C}=2Z_L$. For a supported density operator, the collective jump term and both anticommutator terms are separately zero. The common Hamiltonian term also vanishes. The remaining Hamiltonian is $H_L=\delta Z_L$.

For either physical qubit, $Z_j^2=I$, so $\mathcal D[Z_j]\rho=Z_j\rho Z_j-\rho$. Their restrictions yield

$$
\left(\mathcal D[Z_1]+\mathcal D[Z_2]\right)\rho_L
=Z_L\rho_LZ_L-\rho_L+(-Z_L)\rho_L(-Z_L)-\rho_L
=2(Z_L\rho_LZ_L-\rho_L).
\tag{S2}
$$

The minus sign on the second local operator occurs twice in its jump term and therefore disappears. This is the precise reason separate dephasing channels add even though their collective operator vanishes. Combining Eq. (S2) with the restricted Hamiltonian gives Eq. (5).

## S2. Matrix elements, decay rate, and phase

Let $E_{ab}=|a_L\rangle\langle b_L|$ for $a,b\in\{0,1\}$. The two diagonal matrix units commute with $Z_L$ and satisfy $Z_LE_{aa}Z_L=E_{aa}$. Every term of the logical generator therefore annihilates them. This proves that both logical populations are constants of motion.

For the off-diagonal matrix unit $E_{01}=|01\rangle\langle10|$, each independent dissipator can be evaluated before restriction. The two states have opposite eigenvalues under either $Z_1$ or $Z_2$, so

$$
Z_1E_{01}Z_1=-E_{01},\qquad Z_2E_{01}Z_2=-E_{01},
\qquad \mathcal D[Z_j]E_{01}=-2E_{01}.
\tag{S3}
$$

Multiplying by $\epsilon$ and summing over the two qubits gives $-4\epsilon E_{01}$. The factor four thus contains a factor two from each dissipator's off-diagonal action and a factor two from the number of independent channels. With the stated definition of $\mathcal D$, no further rate normalization is implicit.

The logical energies are $E_0=+\delta$ and $E_1=-\delta$. The row-$0$, column-$1$ coherence is therefore governed by

$$
-i[H_L,\rho_L]_{01}=-i(E_0-E_1)(\rho_L)_{01}
=-2i\delta c,
\qquad
\frac{dc}{dt}=(-4\epsilon-2i\delta)c.
\tag{S4}
$$

Integration with constant parameters gives Eq. (6). Hermiticity fixes the conjugate matrix element to $c(t)^*$, with the opposite phase sign. This convention can also be checked at $\epsilon=0$: the ket amplitudes evolve as $|0_L\rangle\mapsto e^{-i\delta t}|0_L\rangle$ and $|1_L\rangle\mapsto e^{+i\delta t}|1_L\rangle$. Forming the row-$0$, column-$1$ density element multiplies the first amplitude by the conjugate of the second and produces $e^{-2i\delta t}$.

The four matrix units span the entire space of logical operators. The generator annihilates the two diagonal units and multiplies each off-diagonal unit by a scalar, with conjugate scalars for the pair. Its exponential can therefore be applied separately to each component of the initial density operator. For initial population $p$ and coherence $c_0$, the result is

$$
\rho_L(t)=pE_{00}+(1-p)E_{11}
+c_0e^{-4\epsilon t-2i\delta t}E_{01}
+c_0^*e^{-4\epsilon t+2i\delta t}E_{10}.
\tag{S5}
$$

This expression preserves the trace and reproduces the initial state at zero time. Setting the independent rate to zero leaves only the conjugate phase factors. The collective rate disappears before time integration: its cancellation is an identity of the restricted generator and holds at every evolution time.

Finally, $\operatorname{Tr}(X_L\rho_L)=c+c^*=2\operatorname{Re}c$. Substituting $c(0)=1/2$ for $|+_L\rangle$ yields Eq. (8), connecting the derived coherence to the logical readout.
