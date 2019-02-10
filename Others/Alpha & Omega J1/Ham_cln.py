'''This function returns the complete hamiltonian matrix of the interaction
between the 1st site and the nth site, in a spin chain of length l.'''

from H1cln import H1cln
from H2cln import H2cln
from H3cln import H3cln
import numpy as np

def Ham_cln(n, j1, l):
    
    dim = 2 ** l
        
    Ham = np.zeros((dim, dim)) #The empty hamiltonian matrix is initialised.
        
    H1cln_mat = (H1cln(n, j1, l)) #The 3 parts of the hamiltonian are invoked.
    H2cln_mat = (H2cln(n, j1, l))
    H3cln_mat = (H3cln(n, j1, l))
    
    for i in range(dim):
        for j in range(dim): #Combining the 3 parts of the hamiltonian now.
            Ham[i][j] = H1cln_mat[i][j] + H2cln_mat[i][j] + H3cln_mat[i][j]
    
    return(Ham)
    
print(Ham_cln(2, 1, 4))
