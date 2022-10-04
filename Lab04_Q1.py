# Braulio Ojeda Valencia, Jashandeep Singh
# WORKLOAD: Jashan
# PURPOSE:
    
# Pseudocode:
# Import necessary modules ( numpy, matplotlib)
# Define Gauss Elimination algorithm function
# Define Partail Pivoting algorithm function
# Use equation 6.16 in Partail Pivoting method to get the equation 6.2
# Print Answer to 6.2 equation
# Set N = 150 (question 1b)
# Define Empty list that would be used later in while loop to save results
# Initialize the While loop
# In while loop, calculate the time taken to solve the matrix and error in 
# vector v for each method 
# Plot N vs Time taken to solve the matrix
# Plot N vs Error in final solution


# Code:
# Import necessary modules (numpy, matplotlib)
import numpy as np
from numpy import empty, copy
from numpy.random import rand
from numpy.linalg import solve
from time import time
import matplotlib.pyplot as plt

##################### GaussELim without Partail Pivot Function ################
# Definr Gauss Elimination algorithm function
def GaussElim_nopivot(A_in, v_in):
    """Implement Gaussian Elimination. This should be non-destructive for input
    arrays, so we will copy A and v to
    temporary variables
    IN:
    A_in, the matrix to pivot and triangularize
    v_in, the RHS vector
    OUT:
    x, the vector solution of A_in x = v_in """
    # copy A and v to temporary variables using copy command
    A = copy(A_in)
    v = copy(v_in)
    N = len(v)

    for m in range(N):
        # Divide by the diagonal element
        div = A[m, m]
        A[m, :] /= div
        v[m] /= div

        # Now subtract from the lower rows
        for i in range(m+1, N):
            mult = A[i, m]
            A[i, :] -= mult*A[m, :]
            v[i] -= mult*v[m]

    # Backsubstitution
    # create an array of the same type as the input array
    x = empty(N, dtype=v.dtype)
    for m in range(N-1, -1, -1):
        x[m] = v[m]
        for i in range(m+1, N):
            x[m] -= A[m, i]*x[i]
    return x


##################### GaussELim with Partail Pivot Function ###################
# Definr Partail Pivoting algorithm function
def GaussElim_pivot(A_in, V_in):
    """Implement Gaussian Elimination. This should be non-destructive for input
    arrays, so we will copy A and v to
    temporary variables
    IN:
    A_in, the matrix to pivot and triangularize
    v_in, the RHS vector
    OUT:
    x, the vector solution of A_in x = v_in """
    # copy A and v to temporary variables using copy command
    
    A = copy(A_in)
    v = copy(V_in)
    A,v = PartialPivot2(A,v)
    N = len(v)

    for m in range(N):
        # Divide by the diagonal element
        div = A[m, m]
        A[m, :] /= div     #A[m,:] is row, m is postion then : row
        v[m] /= div

        # Now subtract from the lower rows
        for i in range(m+1, N):
            mult = A[i, m]
            A[i, :] -= mult*A[m, :]
            v[i] -= mult*v[m]

    # Backsubstitution
    # create an array of the same type as the input array
    x = empty(N, dtype=v.dtype)
    for m in range(N-1, -1, -1):
        x[m] = v[m]
        for i in range(m+1, N):
            x[m] -= A[m, i]*x[i]
    return x

def PartialPivot2(A_in, v_in):
    """ At mth row, function check to see which of the rows below has the 
    largest mth element then swap this row with the current  mth value and 
    proceed with Gaussian elimination"""
    # Check if A[m,m] is the largest value from elements bellow and perform swapping
    A = copy(A_in)
    v = copy(v_in)
    N = len(v_in)
    # print("===================")
    # print("Original Matrix and Vector")
    # print(A, v)
    # print("===================")
    for m in range(N):
        for i in range(m+1,N):
            if A[m,m] < A[i,m]:
                A[[m,i],:] = copy(A[[i,m],:])	
                v[[m,i]] = copy(v[[i,m]])
    # print("===================")
    # print("Pivoted Matrix and Vector")
    # print(A, v)
    # print("===================")
    return A, v

# Print Answer to 6.2 equation
print('Question 1 a \n')
matrix_A = np.array([[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]],float)
Vector_v = np.array([-4,3,9,7],float)  
sol = GaussElim_pivot(matrix_A, Vector_v )
print(sol,'\n')



# ############################### Question 1b #################################
print("Question 1b\n")
# Set N = 150
N = 100
# Define some empty list that would be used later in while loop to save results

gauss_elim_time = []   # time taken todo the computation with Gauss elim. method
gauss_p = []           # time taken todo the computation with Gauss elim. pivot method
LU_de = []                # time taken todo the computation with LU method
error_gauss_elim = []         # error in gauss elimination method
error_gauss_p = []    # error in  gauss pivot elimination method
error_LU = []                 # error in  LU-decom. method
x_axis = []
# Impliment While loop
n = 0
# In while loop, calculate the time taken to solve the matrix and error in 
# vector v for each method 
while n < N:
    
    A = rand(n,n)
    v = rand(n)
    
    start1 = time()     # Save start time
    x1 = GaussElim_nopivot(A,v)
    #x_vec1.append(x1)
    end1 = time()       # Save end time 
    diff1 = np.abs(start1-end1)
    gauss_elim_time.append(diff1)
    # Counting err in gauss elimination method
    vsol1 = np.dot(A,x1)
    err1  = np.mean(np.abs(v-vsol1))
    error_gauss_elim.append(err1)   # saving err1 outside the loop
    
    
    
    start2 = time()      # Save start time
    x2 = GaussElim_pivot(A,v)
    #x_vec2.append(x2)
    end2 = time()        # Save end time 
    diff2 = np.abs(start2-end2)
    gauss_p.append(diff2)
    # Counting err in gauss pivot elimination method
    vsol2 = np.dot(A,x2)
    err2  = np.mean(np.abs(v-vsol2))
    error_gauss_p.append(err2)   # saving err2 outside the loop
   
    start3 = time()       # Save start time
    x3 = solve(A,v)
    #x_vec3.append(x3)
    end3 = time()         # Save end time 
    diff3 = np.abs(start3-end3)
    LU_de.append(diff3)
    # Counting err in LU decom. method
    vsol3 = np.dot(A,x3)
    err3  = np.mean(np.abs(v-vsol3))
    error_LU.append(err3)   # saving err3 outside the loop
    x_axis.append(n)
    n += 1

# Plot N vs Time taken to solve the matrix

plt.loglog(x_axis[5:],gauss_elim_time[5:],c='blue',label= 'Gauss Elim')
plt.loglog(x_axis[5:],gauss_p[5:], c='r',label= 'Partail Pivoting')
plt.loglog(x_axis[5:],LU_de[5:], c='green',label= 'LU Decomp')
plt.title(' N vs Time',fontsize=13)
plt.xlabel('N',fontsize=13)
plt.ylabel('Time (s)',fontsize=13)
plt.legend(loc='lower right')
plt.figure() 

# Plot N vs Error in final solution

plt.loglog(x_axis[5:],error_gauss_elim[5:],c='blue',label= 'Gauss Elim')
plt.loglog(x_axis[5:],error_gauss_p[5:], c='r',label= 'Partail Pivoting')
plt.loglog(x_axis[5:],error_LU[5:], c='green',label= 'LU Decomp')
plt.title(' N vs Error',fontsize=13)
plt.xlabel('N',fontsize=13)
plt.ylabel('Error',fontsize=13)
plt.legend(loc='lower right')























            
            
    

