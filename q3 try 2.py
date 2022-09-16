#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 21:09:23 2022

@author: jashansingh
"""
import numpy as np                      # import numpy
import matplotlib.pyplot as plt         # import matplotlib.pyplot
from numpy import zeros                 # import zeros func. from zeros module
from numpy import ones                  # import ones func. from ones module
from time import time                   # import time func. from 'time' module
# define two matrices of size [n x n]

time_N = []
time_N3 = []
time_dot =[]
array_N = []
array_N3 = []
array_dot = []

n = 2
while n < 10:
    # We are going to use nested FOR loop. 
    a = ones([n,n],float)*3
    b = ones([n,n],float)
    # define empty matrix of [n,n], we will insert final answer into this matrix
    c = zeros([n,n],float)
    
    start_1 = time()                        # Save start time of N^3
    for i in range(n):                      # Loop "i" goes around N^3 times
        for j in range(n):                  # Loop "j" goes around N^2 times
            start_2 = time()                # Save start time of N
            for k in range(n):              # Loop "k" goes around N times
                c[i,j] += a[i,k]*b[k,j]
            end_2 = time()                  # Save end time of N  
    end_1 = time()                          # Save end time of N^3 
    diff_1 = end_1 - start_1
    time_N3.append(diff_1)
    array_N3.append(n)
    diff_2 = end_2 - start_2 
    time_N.append(diff_2)
    array_N.append(n)
    # Dot product from numpy.dot cmd.
    start_3 = time()
    dot_product = np.dot(a,b)
    end_3 = time()
    diff_3 = end_3 - start_3
    time_dot.append(diff_3)
    array_dot.append(n)
    
    n += 1
print("Time  of function N = \n",time_N)
print("Time of function N^3 =\n",time_N3)
print("Time of numpy.dot function =",time_dot)
print('\n',"Since N is the innerproduct (only loop k), it takes less time." 
      "Total time taken to solve the product of matrices is given by "
      "outerproduct which is product of all loops (N^3)")


""" Plot N vs time , N^3 vs Time  and numpy.dot Vs Time"""
plt.plot(time_N,array_N,label='N')
# plt.title('N Vs Time Plot')
# plt.xlabel('Time (s)')
# plt.ylabel("N")

plt.plot(time_N3,array_N3,label='N^3')
# plt.title('N^3 Vs Time Plot')
# plt.xlabel('Time (s)')
# plt.ylabel('N^3')

plt.plot(time_dot,array_dot,label='Numpy.dot')
# plt.title('N^3 Vs Time Plot')
# plt.xlabel('Time (s)')
# plt.ylabel('N^3')
plt.legend()
