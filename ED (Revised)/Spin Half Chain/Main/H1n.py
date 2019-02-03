'''This function seeks to apply the first part of the energy operator between the
nth site and the (n+1)th site, which is (Snz S(n+1)z) to the horizontal eigenstates,
then taking the inner product of the horizontal eigenstates with the vertical 
eigenstates, thereby returning the first part of the hamiltonian matrix H1.

It is important to take note that only the diagonal entries of the matrix is being 
affected, since when applied to an eigenstate, H1 does not change it to a different one.'''

import itertools
import numpy as np

def H1n(n, j1, l):
    
    list1 = list(itertools.product([0, 1], repeat = l))
    
    dim = 2 ** l
    
    Ham = np.zeros((dim, dim))
    
    for i in range(len(list1)):
        list1[i] = list(list1[i]) 
                
    for i in range(dim):
        
        if list1[i][n-1] == 0 and list1[i][n] == 0:
            Ham[i][i] +=0.25 * j1
        elif list1[i][n-1] == 1 and list1[i][n] == 0:
            Ham[i][i] += -0.25 * j1
        elif list1[i][n-1] == 0 and list1[i][n] == 1:
            Ham[i][i] += -0.25 * j1
        else:
            Ham[i][i] += 0.25 * j1


    return(Ham)