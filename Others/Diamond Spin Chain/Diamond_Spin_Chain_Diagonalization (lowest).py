'''This function serves to diagonalize an input matrix, and prints the 
eigenvectors and their corresponding eigenvalues. 
It also prints the lowest eigenvalue and its corresponding eigenvector.'''

import numpy as np
from Diamond_Spin_Chain import diamondspinchain

def dssmall(j1, j2, l):

    Ham = diamondspinchain(j1, j2, l)
    
    print(Ham)

    eigenvalues, eigenvectors = np.linalg.eig(Ham)

    #initializing the biggest eigenvalue
    smalleigvalue = eigenvalues[0] 
    smalleigvector = eigenvectors[0] 

    for i in range(2 ** l):
        print(i+1)
        print('The eigenvalue', i+1, 'is', eigenvalues[i], '.')
        print('The corresponding eigenvector ', i+1, 'is', eigenvectors[i], '.')
        print('='*100)
        if eigenvalues[i] < smalleigvalue:
            smalleigvalue = eigenvalues[i]
            smalleigvector = eigenvectors[i]
        
    print('The lowest eigenvalues is ', smalleigvalue, 'with its corresponding eigenvector ', smalleigvector, '.')

dssmall(1, 2, 4)
