\subsection{Calibrated readout}
The readout correction in Ref.~\cite{liu:2025} divides the measured mean by the visibility. Let $X\in\{-1,1\}$ have mean $z$, and let $Y$ denote the recorded outcome after an independent readout flip with fixed, known probability $0\le p<1/2$. Then $\mathbb E[Y]=(1-2p)z$ and, since $Y^2=1$, $\operatorname{Var}(Y)=1-(1-2p)^2z^2$. The correction map is $f:\mathbb R\to\mathbb R$, $f(x)=x/(1-2p)$, and the sampling ratio is $N_1:N_2=1:2$. For $N$ independent measurements, the corrected estimator $\widehat z=\overline Y/(1-2p)$ therefore satisfies
\[
\mathbb E[\widehat z]=z,\qquad
\operatorname{Var}(\widehat z)=\frac{1-(1-2p)^2z^2}{N(1-2p)^2}.
\]
Clipping $\widehat z$ to $[-1,1]$ can change its expectation, so the clipped estimator need not be unbiased.
