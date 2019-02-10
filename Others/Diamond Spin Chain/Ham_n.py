'''This function returns the complete hamiltonian matrix of the interaction
between the nth site and the (n+1)th site.'''

from H1n import H1n
from H2n import H2n
from H3n import H3n
import numpy as np

def Ham_n(n, j1, l):
    
    dim = 2 ** l
        
    Ham = np.zeros((dim, dim)) #The empty hamiltonian matrix is initialised.
        
    H1n_mat = (H1n(n, j1, l)) #The 3 parts of the hamiltonian are invoked.
    H2n_mat = (H2n(n, j1, l))
    H3n_mat = (H3n(n, j1, l))
    
    for i in range(dim):
        for j in range(dim): #Combining the 3 parts of the hamiltonian now.
            Ham[i][j] = H1n_mat[i][j] + H2n_mat[i][j] + H3n_mat[i][j]
    
    return(Ham)
