# Braulio Ojeda Valencia, Jashandeep Singh
# WORKLOAD: Jashan
# PURPOSE:
    
# Pseudocode 3(a):
# Import necessary modules (numpy, matplotlib)
# Define all variabels and constants 
# Set up simple relaxation algorithm 
# Loop untill error is small enough
# Print the result
# Define c from 0 to 3 in steps of 0.01
# Plot x vs c 

import numpy as np
import matplotlib.pyplot as plt

"""############################################################################
############################# Question 3(a)    ################################
############################# Exercise 6.10(a) ################################                             
############################################################################"""
# Define all variabels and constants 
c = 2      # constant
accuracy = 1e-6

# This loop is set for 100 steps, however since we need only 10^-6 accuracy 
# it will stop earlier
for k in range(50):   
    x1 = 1      # inital guess for  x  
    error = 1   # inital guess for the error, set it equal to x1
    steps = 0    # Number of iterations
    
    # Loop untill error is small enough
    while error > accuracy:
        x1,x2 = 1 - np.exp(-c*x1), x1
        error =np.abs((x1-x2) / (1 - 1 / (c*np.exp(-c * x1))))
        steps += 1
print('\nQuestion 3(a):')       
print('The solution is', x1)

"""############################################################################
############################# Question 3(a)    ################################
############################# Exercise 6.10(b) ################################                             
############################################################################"""

new_c = np.arange(0,3,0.01)
accuracy = 1e-6
x_values = []
for i in range(len(new_c)):   
    x11 = 1      # inital guess for  x  
    error = 1   # inital guess for the error, set it equal to x1
    steps1 = 0    # Number of iterations
    # Loop untill error is small enough
    while error > accuracy:
        x11,x22 = 1 - np.exp(-new_c[i]*x11), x11
        error = np.abs((x11-x22) / (1 - 1 / (c*np.exp(-new_c[i] * x1))))
        steps1 += 1
    x_values.append(x11)
plt.plot(new_c,x_values,c='b')
plt.title(' Known Parameter (c) vs Unknow (x)',fontsize=13)
plt.xlabel('c',fontsize=13)
plt.ylabel('x',fontsize=13)

"""############################################################################
############################# Question 3(b)    ################################
############################# Exercise 6.11(b) ################################                             
############################# Simple Relaxation ############################"""

# Pseudocode 3(b):
# Import necessary modules (numpy, matplotlib)
# Define all variabels and constants 
# Loop untill error is small enough (10^-6)
# Print result and number of steps that programs took to get an accuracy of 10^-6
# Set omega = 0.9675 to get the best outcome
# Modify loop according to overrelation method
# Loop untill error is small enough (10^-6)
# Print the results and steps

# Define all variabels and constants 

c = 2      # constant
accuracy = 1e-6
x1 = 1      # inital guess for  x  
error = 1   # inital guess for the error, set it equal to x1
steps = 0    # Number of iterations

# Loop untill error is small enough
while error > accuracy:
    x1,x2 = 1 - np.exp(-c*x1), x1
    error = np.abs((x1-x2) / (1 - 1 / (c*np.exp(-c * x1))))
    steps += 1
    
#Print result and number of steps 
print('\nQuestion 3(b):\n')
print('Excercise 6.11(b)')       
print('The solution is', x1,'. It takes 14 steps to get an accuracy of 10^-6.')

"""############################################################################
############################# Question 3(b)    ################################
############################# Exercise 6.11(c) ################################                             
############################# Overrelaxation   #############################"""

c = 2      # constant
w = 0.9675 # omega
accuracy = 1e-6

x1 = 1      # inital guess for  x  
error = 1   # inital guess for the error, set it equal to x1
steps = 0   # Number of iterations
# Loop untill error is small enough
while error > accuracy:
    x1,x2 = ((1 + w) * (1 - np.exp(-c * x1))) - w * x1, x1
    error = np.abs((x1 - x2) / (1 - 1 / (((1+w) * (c * np.exp(-c * x1 ))) - w )))
    steps += 1
# Print the results and steps
print('\nExcercise 6.11(c)')    
print('After trying couple of different omega (w), we found, w = 0.9675, was able to get'
      ' the calculation to converge at least twice as fast as the simple relaxtion method.\n'
      'The result of overrelaxtion method is',x1,'\nIt takes',steps,'steps to get ' 
      'an accuracy of 10^-6',)







    
