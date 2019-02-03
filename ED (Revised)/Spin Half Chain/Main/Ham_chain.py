'''In a spin chain of length l, we will sum over the interactions
s1 dot s2, s2 dot s3 and so on, all the way to s(l-1) dot sl.'''

from Ham_n import Ham_n
import numpy as np

def Ham_chain(j1, l):
    
    dim = 2 ** l
    Ham = np.zeros((dim, dim))
    
    for i in range(1, l):
        
        Ham_iter = Ham_n(i, j1, l)
        
        for j in range(dim):
            for k in range(dim):
                Ham[j][k] += Ham_iter[j][k]
    
    return(Ham)
    

