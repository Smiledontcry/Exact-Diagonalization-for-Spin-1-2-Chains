'''This function seeks to apply the third part of the energy operator between the
nth site and the (n+1)th site, which is 1/2(Sn-S(n+1)+) to the horizontal eigenstates,
then taking the inner product of the horizontal eigenstates with the vertical 
eigenstates, thereby returning the third part of the hamiltonian matrix H3.'''

import itertools
import numpy as np

def H3n(n, j1, l):
    
    list1 = list(itertools.product([0, 1], repeat = l))
    list2 = list(itertools.product([0, 1], repeat = l))
    
    dim = 2 ** l
    
    Ham = np.zeros((dim, dim))
    
    for i in range(len(list1)):
        list1[i] = list(list1[i]) 
        
    for i in range(len(list2)):
        list2[i] = list(list2[i]) 
    
    
    
    for i in range(len(list2)):
        if list2[i][n-1] == 0 or list2[i][n] == 1:
            list2[i] = 0
        else:
            list2[i][n-1] = 0
            list2[i][n] = 1
      
    for i in range(dim):
        for j in range(dim):
            if list1[i] == list2[j]:
                Ham[i][j] += 0.5 * j1

    return(Ham)
           