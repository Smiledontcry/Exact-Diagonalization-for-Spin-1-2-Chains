'''The function diamondspinchain(j1, j2, l) takes in the two different values
of coupling coefficient j1 and j2, and returns the Hamiltonian matrix of the 
corresponding closed looped diamond spin half chain (abbreviated as DSC for 
brevity). The illustration is available in the same directory as this script.

All interactions are Heisenberg interactions. The only values valid for the 
length l should be integer multiples of 4, with each multiple covering a period. 
Thus, l = 4 corrsponds to an one-diamond "chain", l = 8 corresponds to a 
two-diamond chain and so on. Of course, it makes no sense that the diamond 
chain's length should be less than 4, since that number of sites constitutes 
the first period. 

We are treating each periodic interactions separately. It is highly recommended 
that you read the next parts while referencing the illustration, which is a
DSC of length l = 12. 

Firstly, we created a zero square matrix of size 2^l. We call it Ham which is
intially empty, and sum over all of the interactions in the chain.

1. Between sites 1 and 2, 3 and 4, 5 and 6, 7 and 8, 9 and 10, 11 and 12... 
we have the j1 coefficient nearest neighbour interaction. For these sites 
on the DSC, we will apply the Ham_n function on sites 1, 3, 5 ,7, 9... with j1
and add the output hamiltonian to the original.

2. Between sites 2 and 3, 4 and 5, 6 and 7, 8 and 9, 10 and 11... 
we have the j2 coefficient nearest neighbour interaction. For these sites 
on the DSC, we will apply the Ham_n function on sites 2, 4, 6, 8, 10... with j2
and add the output hamiltonian to the original.

3. Between sites 2 and 4, 3 and 5, 6 and 8, 7 and 9, 10 and 12... 
we have the j2 coefficient nearest neighbour interaction. For these sites 
on the DSC, we will apply the nnn_Ham_n function on sites 2, 3, 6, 7, 10... 
with j2 and add the output hamiltonian to the original.

4. Finally, we complete the loop by summing over the j2 interactions for 
both the penultimate site and the final site with the first site.
'''

from nnn_Ham_n import nnn_Ham_n
from Ham_n import Ham_n 
from Ham_cln import Ham_cln
import numpy as np

def diamondspinchain(j1, j2, l):

    dim = 2 ** l
    Ham = np.zeros((dim, dim)) #The empty hamiltonian matrix is initialised.
    
    
    
    #Part One
    #Firstly, we will tackle the j1 nn interactions, which begins at site 1, 3, 5, 7, 9...
    for i in range(1, l, 2):
        Ham_iter = Ham_n(i, j1, l) #This temp matrix for every site is added to the original empty hamiltonian matrix.
           
        for j in range(dim): #This is simply copying every iteration to the original hamiltonian.
            for k in range(dim): #It will be repeated for every stage so I will only write it once.
                Ham[j][k] += Ham_iter[j][k]
    
    
    
    
    
    #Part Two
    #Next, we will tackle the j2 nn interactions, which begins at site 2, 4, 6, 8...
    #Keep in mind that the final site is not included.
    for i in range(2, l, 2):
        Ham_iter = Ham_n(i, j2, l) 
            
        for j in range(dim):
            for k in range(dim):
                Ham[j][k] += Ham_iter[j][k]
    
    
    
    
    
    #Part Three
    #Now, we will tackle the j2 nnn interactions, which begins at site 2, 3, 6, 7...
    #We will split it into 2 sequences: 2, 6, 10... and 3, 7, 11(Keep in mind that
    #this is not included in a length 12 DSC)...
    #Sequence 1: 2, 6, 10, 14...
    for i in range(2, l, 4):
        Ham_iter = nnn_Ham_n(i, j2, l) 
        for j in range(dim):
            for k in range(dim):
                Ham[j][k] += Ham_iter[j][k]       
    #Sequence 2: 3, 7, 11, 15...
    for i in range(3, l-1, 4): #We used l-1 since this does not apply to the penultimate site.
        Ham_iter = nnn_Ham_n(i, j2, l) #This temp matrix for every site is added to the original empty hamiltonian matrix.
            
        for j in range(dim):
            for k in range(dim):
                Ham[j][k] += Ham_iter[j][k]  
    
    
    
    
    
    #Finally, we complete the loop by summing over the j2 nn interactions for both the penultimate
    #site and the final site.
    for i in (l-1, l): #Both the interactions between the penultimate site and the final site with the
                        #first site and included.
        Ham_iter = Ham_cln(i, j2, l) 
            
        for j in range(dim):
            for k in range(dim):
                Ham[j][k] += Ham_iter[j][k]  
    
    return(Ham)
    

