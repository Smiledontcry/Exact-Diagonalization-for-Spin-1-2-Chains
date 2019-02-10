'''We have divided the energy operator in a spin-half chain, 
between the 1st electron site and the nth site into three parts: 
    
    Hcln = H1cln + H2cln + H3cln

This function seeks to apply the first part of the energy operator between the
1st site and the nth site, which is (S1z Snz) to the horizontal eigenstates,
then taking the inner product of the horizontal eigenstates with the vertical 
eigenstates, thereby returning the first part of the hamiltonian matrix H1cl.

It is important to take note that only the diagonal entries of the matrix is being 
affected, since when applied to an eigenstate, H1 does not change it to a 
different eigenstate.'''

import itertools
import numpy as np

def H1cln(n, j1, l):
    
    list1 = list(itertools.product([0, 1], repeat = l)) #All elements of list1 are tuples.
    
    dim = 2 ** l
    
    Ham = np.zeros((dim, dim)) #The empty hamiltonian matrix is initialised.
    
    for i in range(len(list1)): #The elements of list1 are converted to lists instead of tuples.
        list1[i] = list(list1[i]) 
                
    for i in range(dim): #All 4 possible cases are taken into account below.
        
        if list1[i][0] == 0 and list1[i][n-1] == 0:
            Ham[i][i] +=0.25 * j1
        elif list1[i][0] == 1 and list1[i][n-1] == 0:
            Ham[i][i] += -0.25 * j1
        elif list1[i][0] == 0 and list1[i][n-1] == 1:
            Ham[i][i] += -0.25 * j1
        else:
            Ham[i][i] += 0.25 * j1


    return(Ham)
    

