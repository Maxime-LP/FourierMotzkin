# FourierMotzkin
Fourier Motzkin optimization method implementation
Implémentation de la méthode de Fourier-Motzkin pour la résolution d'un problème de minimisation sous forme standard :

\begin{cases} 
    \text{min } f(x) = \sum_{j=1}^{n}c_jx_j = c^Tx\\
    \sum_{j=1}^{n}a_{ij} \leq b_i, i=1,...,r \iff Ax \leq b \\
    x_j \geq 0, j=1,...,n \iff x\geq 0
\end{cases}

où $x=(x_1,...,x_n)^T \in \mathbb{R}^n, c=(c_1,...,c_n)^T \in \mathbb{R}^n, b=(b_1,...,b_r)^T \in \mathbb{R}^r, A \in \mathcal{M}_{r,n}(\mathbb{R})$.
