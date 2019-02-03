'''This function serves to diagonalize an input matrix, and prints the 
eigenvectors and their corresponding eigenvalues. 
It also prints the lowest eigenvalue and its corresponding eigenvector.'''

import numpy as np
from Ham_chain import Ham_chain

def spinhalfdiag(j1, l):

    Ham = Ham_chain(j1, l)
    
    print(Ham)

    eigenvalues, eigenvectors = np.linalg.eig(Ham)

    #initializing the biggest eigenvalue
    bigeig = eigenvalues[0] 

    for i in range(2 ** l):
        print(i+1)
        print('The eigenvalue', i+1, 'is', eigenvalues[i], '.')
        print('The corresponding eigenvector ', i+1, 'is', eigenvectors[i], '.')
        print('='*100)
        if eigenvalues[i] > bigeig:
            bigeig = eigenvalues[i]
        
    print('The largest eigenvalues is ', bigeig, '.')

spinhalfdiag(3, 3)
 
