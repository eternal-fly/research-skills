# Synthetic editing fixture

All names, citation keys, identifiers and scientific findings in this fixture are synthetic test data, not real literature. Treat the supplied metadata as facts of this editing exercise; do not browse or invent sources. The exercise date is 2026-10-28.

Use the specified APS Quantum Writing skill to edit the passage into ready-to-use manuscript prose in the requested language. Preserve the scientific meaning, conditions, uncertainty and citation keys. Keep reference metadata separate from the prose and unchanged where supplied. Deliver the revised passage and any supplied bibliography block only, without an editing report. Follow the skill's normal editorial conventions. Avoid unrelated changes.

## English Supplemental Material

Edit the complete short derivation below as one coherent supporting passage. Keep the mathematical notation and citation command usable as LaTeX. A colon inside a mapping and a colon inside a citation key are mathematical/source syntax.

Metadata supplied for editing: `liu:2025` is a journal article from 2025.

\subsection{Calibrated readout}
The published paper \cite{liu:2025} motivates the correction: divide the measured mean by the visibility. Let $X\in\{-1,1\}$ have mean $z$ and let independent readout flips occur with known probability $0\le p<1/2$. The correction map is $f:\mathbb R\to\mathbb R$, $f(x)=x/(1-2p)$; the sampling ratio is $N_1:N_2=1:2$. For $N$ independent measurements, $\widehat z=\overline Y/(1-2p)$ is unbiased—the exact variance is $[1-(1-2p)^2z^2]/[N(1-2p)^2]$. Two conditions matter: $p$ is fixed and known, and the shots are independent. Clipping $\widehat z$ to $[-1,1]$ changes its expectation—the clipped estimator need not be unbiased.

