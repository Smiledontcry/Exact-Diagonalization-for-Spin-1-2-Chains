'''This function seeks to apply the second part of the energy operator between the
1st site and the nth site, which is 1/2(S1+Sn-) to the horizontal eigenstates,
then taking the inner product of the horizontal eigenstates with the vertical 
eigenstates, thereby returning the second part of the hamiltonian matrix H2cln.'''

import itertools
import numpy as np

def H2cln(n, j1, l):
    
    list1 = list(itertools.product([0, 1], repeat = l)) #All elements of list1 and list 2 are tuples.
    list2 = list(itertools.product([0, 1], repeat = l))
    
    dim = 2 ** l
    
    Ham = np.zeros((dim, dim)) #The empty hamiltonian matrix is initialised.
    
    for i in range(len(list1)): #The elements of list1 and list2 are converted to lists instead of tuples.
        list1[i] = list(list1[i]) 
        
    for i in range(len(list2)):
        list2[i] = list(list2[i]) 
    
    
    
    for i in range(len(list2)): #The eigenstates which cannot be further raised or lowered are killed off.
        if list2[i][0] == 1 or list2[i][n-1] == 0:
            list2[i] = 0
        else: #Eligible eigenstates experience a spin swap for adjacent sites 1 and n.
            list2[i][0] = 1
            list2[i][n-1] = 0

    for i in range(dim): #Iterating through the entire empty matrix
        for j in range(dim): #The inner product between the horizontal and vertical eigenstates is taken.
            if list1[i] == list2[j]:
                Ham[i][j] += 0.5 * j1

    return(Ham)
           