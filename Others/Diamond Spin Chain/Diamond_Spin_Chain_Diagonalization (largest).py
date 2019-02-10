'''This function serves to diagonalize an input matrix, and prints the 
eigenvectors and their corresponding eigenvalues. 
It also prints the lowest eigenvalue and its corresponding eigenvector.'''

import numpy as np
from Diamond_Spin_Chain import diamondspinchain

def dslarge(j1, j2, l):

    Ham = diamondspinchain(j1, j2, l)
    
    print(Ham)

    eigenvalues, eigenvectors = np.linalg.eig(Ham)

    #initializing the biggest eigenvalue
    bigeigvalue = eigenvalues[0] 
    bigeigvector = eigenvectors[0] 

    for i in range(2 ** l):
        print(i+1)
        print('The eigenvalue', i+1, 'is', eigenvalues[i], '.')
        print('The corresponding eigenvector ', i+1, 'is', eigenvectors[i], '.')
        print('='*100)
        if eigenvalues[i] > bigeigvalue:
            bigeigvalue = eigenvalues[i]
            bigeigvector = eigenvectors[i]
        
    print('The highest eigenvalues is ', bigeigvalue, 'with its corresponding eigenvector ', bigeigvector, '.')

dslarge(1, 2, 4)
 
