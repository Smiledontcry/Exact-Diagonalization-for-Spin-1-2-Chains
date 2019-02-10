'''This module deals with the next nearest neighbour, Heisenberg interaction,
spin half chains.

In a spin chain of length l, we will sum over the interactions
s1 dot s3, s2 dot s4 and so on, all the way to s(l-1) dot sl.

Here, we sum over all of the sites and combine the hamiltonian matrices.

The complete spin chain hamiltonian matrix is thus summation n Ham_n.

This function takes the value of j1 and length of the spin chain as inputs.
It returns the complete spin chain hamiltonian matrix for the entire chain.'''

from nnn_Ham_n import nnn_Ham_n
import numpy as np

def nnn_Ham_chain(j2, l):
    
    dim = 2 ** l
    Ham = np.zeros((dim, dim)) #The empty hamiltonian matrix is initialised.
    
    for i in range(1, l-1):
        
        Ham_iter = nnn_Ham_n(i, j2, l) #This temp matrix for every site is added to the original empty hamiltonian matrix.
        
        for j in range(dim):
            for k in range(dim):
                Ham[j][k] += Ham_iter[j][k]
    
    return(Ham)

print(nnn_Ham_chain(1, 3))


