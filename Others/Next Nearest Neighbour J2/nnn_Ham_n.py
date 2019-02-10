'''This function returns the complete hamiltonian matrix of the interaction
between the nth site and the (n+2)th site.'''

from nnn_H1n import nnn_H1n
from nnn_H2n import nnn_H2n
from nnn_H3n import nnn_H3n
import numpy as np

def nnn_Ham_n(n, j2, l):
    
    dim = 2 ** l
        
    Ham = np.zeros((dim, dim)) #The empty hamiltonian matrix is initialised.
        
    H1n_mat = (nnn_H1n(n, j2, l)) #The 3 parts of the hamiltonian are invoked.
    H2n_mat = (nnn_H2n(n, j2, l))
    H3n_mat = (nnn_H3n(n, j2, l))
    
    for i in range(dim):
        for j in range(dim): #Combining the 3 parts of the hamiltonian now.
            Ham[i][j] = H1n_mat[i][j] + H2n_mat[i][j] + H3n_mat[i][j]
    
    return(Ham)
    


