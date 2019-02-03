from H1n import H1n
from H2n import H2n
from H3n import H3n
import numpy as np

def Ham_n(n, j1, l):
    
    dim = 2 ** l
        
    Ham = np.zeros((dim, dim))
        
    H1n_mat = (H1n(n, j1, l))
    H2n_mat = (H2n(n, j1, l))
    H3n_mat = (H3n(n, j1, l))
    
    for i in range(dim):
        for j in range(dim):
            Ham[i][j] = H1n_mat[i][j] + H2n_mat[i][j] + H3n_mat[i][j]
    
    return(Ham)
